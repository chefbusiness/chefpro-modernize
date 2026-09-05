import type { Handler } from '@netlify/functions';
import { PRODUCTS } from './verify-purchase';
import { productoLabel } from './crypto-checkout';
import { getPayment, isKnownStatus, type NowPaymentsPayment } from '../shared/nowpayments';
import {
  abrirLibro,
  esOrderId,
  getOrderWithEtag,
  maskEmail,
  updateOrder,
  type CryptoOrder,
} from '../shared/crypto-orders';

// ════════════════════════════════════════════════════════════════════════════
// crypto-order-status — lo que consulta la página `/pago-cripto?o=<orderId>`
// mientras el comprador espera las confirmaciones de la red (2026-09-05).
//
// EL `orderId` ES EL SECRETO. 32 hex aleatorios, exactamente igual que hoy el
// `session_id` de Stripe en las páginas `-access`: quien lo tiene es quien
// acaba de pagar. Por eso este endpoint no pide contraseña — y por eso NO
// devuelve el email completo (`maskEmail`), sólo lo justo para que el comprador
// reconozca a qué dirección va a llegarle el enlace.
//
// POR QUÉ CONSULTA A LA API Y NO SE FÍA DEL LIBRO: **NOWPayments no manda IPN
// cuando un pago expira** (spec PAGOS_CRYPTO_NOWPAYMENTS.md:171). Sin esto, un
// pago caducado se quedaría para siempre en «esperando confirmaciones» y el
// comprador mirando una rueda que no gira. Se consulta sólo si hay `paymentId`
// (si el comprador nunca eligió moneda no hay pago que consultar: es un
// abandono), el estado no es terminal, y hace más de 10 minutos del último IPN
// — así una página que hace polling cada pocos segundos no dispara una llamada
// a la API por cada sondeo.
//
// CÓMO VERIFICAR EN PRODUCCIÓN (tras el deploy):
//   curl -s -o /dev/null -w '%{http_code}\n' \
//     'https://aichef.pro/.netlify/functions/crypto-order-status?o=zz'   # 400
//   curl -s 'https://aichef.pro/.netlify/functions/crypto-order-status?o='$(python3 -c "print('0'*32)")
//   → 404 {"error":"not_found"}
// ════════════════════════════════════════════════════════════════════════════

/** Estados en los que ya no hay nada más que esperar: no se vuelve a preguntar. */
const TERMINALES = new Set(['finished', 'failed', 'refunded', 'expired']);

/** Antigüedad mínima del último IPN para molestar a la API de NOWPayments. */
const REFRESCO_MS = 10 * 60 * 1000;

const num = (v: unknown): number | undefined => {
  if (v === null || v === undefined || v === '') return undefined;
  const n = Number(v);
  return Number.isFinite(n) ? n : undefined;
};

export const handler: Handler = async (event) => {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers, body: '' };
  }
  if (event.httpMethod !== 'GET') {
    return { statusCode: 405, headers, body: JSON.stringify({ error: 'method_not_allowed' }) };
  }

  const orderId = String((event.queryStringParameters || {}).o || '').trim();
  if (!esOrderId(orderId)) {
    return { statusCode: 400, headers, body: JSON.stringify({ error: 'invalid_order' }) };
  }

  try {
    const store = await abrirLibro(event);
    const leido = await getOrderWithEtag(store, orderId);
    if (!leido) {
      return { statusCode: 404, headers, body: JSON.stringify({ error: 'not_found' }) };
    }

    let pedido: CryptoOrder = leido.order;
    const etag = leido.etag;

    // ── Refresco contra la API (cubre la expiración sin IPN) ────────────────
    const apiKey = String(process.env.NOWPAYMENTS_API_KEY || '').trim();
    const desdeUltimoIpn = pedido.lastIpnAt ? Date.now() - Date.parse(pedido.lastIpnAt) : Infinity;
    const conviene = Boolean(
      apiKey &&
        pedido.paymentId &&
        !pedido.delivered &&
        !TERMINALES.has(pedido.status) &&
        (!Number.isFinite(desdeUltimoIpn) || desdeUltimoIpn > REFRESCO_MS),
    );

    if (conviene) {
      let apiPago: NowPaymentsPayment | null = null;
      try {
        apiPago = await getPayment(pedido.paymentId as string, apiKey);
      } catch (err) {
        // La página de estado nunca debe romperse por la pasarela: se devuelve
        // lo que hay en el libro y el comprador vuelve a sondear.
        console.warn(`[crypto-order-status] getPayment(${pedido.paymentId}) falló:`, (err as Error).message);
      }
      const nuevo = apiPago && typeof apiPago.payment_status === 'string' ? apiPago.payment_status : '';
      if (nuevo && isKnownStatus(nuevo) && nuevo !== pedido.status) {
        pedido.status = nuevo;
        const pa = num(apiPago?.pay_amount);
        if (pa !== undefined) pedido.payAmount = pa;
        const ap = num(apiPago?.actually_paid);
        if (ap !== undefined) pedido.actuallyPaid = ap;
        if (typeof apiPago?.pay_currency === 'string') pedido.payCurrency = apiPago.pay_currency.toLowerCase();
        // Escritura condicional: si un IPN escribió entre medias, gana él (su
        // información es más fresca que nuestra consulta) y aquí no se insiste.
        const res = await updateOrder(store, pedido, etag).catch(() => null);
        if (res === null) {
          const rele = await getOrderWithEtag(store, orderId).catch(() => null);
          if (rele) pedido = rele.order;
        }
        console.log(`[crypto-order-status] ${orderId} refrescado por API: ${nuevo}`);
      }
    }

    // ── Respuesta ───────────────────────────────────────────────────────────
    const config = PRODUCTS[pedido.productId];
    let accessUrl: string | undefined;
    if (pedido.delivered && config) {
      if (process.env.JWT_SECRET) {
        const jwt = (await import('jsonwebtoken')).default;
        // MISMOS claims que la entrega por email y que Stripe: el gate
        // `ProductAccessGate` sólo mira `?jwt=` (src/components/shared/
        // ProductAccessGate.tsx:28), así que la ruta cripto entra por ahí sin
        // tocar ninguno de los 46 gates. Dominio literal, igual que
        // `sendAccessEmail` (verify-purchase.ts:430).
        const token = jwt.sign({ email: pedido.emailNorm, product: pedido.productId }, process.env.JWT_SECRET, {
          expiresIn: '365d',
        });
        accessUrl = `https://aichef.pro${config.accessPath}?jwt=${token}`;
      } else {
        console.error('[crypto-order-status] JWT_SECRET no configurado: no se puede acuñar el acceso');
      }
    }

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({
        orderId: pedido.orderId,
        status: pedido.status,
        productId: pedido.productId,
        productLabel: productoLabel(pedido.productId),
        emailMasked: maskEmail(pedido.emailNorm),
        delivered: Boolean(pedido.delivered),
        ...(accessUrl ? { accessUrl } : {}),
      }),
    };
  } catch (err) {
    console.error('[crypto-order-status] error:', err);
    return { statusCode: 500, headers, body: JSON.stringify({ error: 'server_error' }) };
  }
};
