import type { Handler } from '@netlify/functions';
import { PRODUCTS, sendAccessEmail } from './verify-purchase';
import {
  getPayment,
  isKnownStatus,
  readRawBody,
  verifyIpnSignature,
  type NowPaymentsPayment,
} from '../shared/nowpayments';
import {
  abrirLibro,
  esOrderId,
  getOrderWithEtag,
  maskEmail,
  saveOrphan,
  saveRawIpn,
  updateOrder,
  type BlobStore,
  type CryptoOrder,
} from '../shared/crypto-orders';

// ════════════════════════════════════════════════════════════════════════════
// nowpayments-ipn — confirmación de pago de NOWPayments → email de acceso.
// Espejo de `stripe-webhook.ts`: misma doctrina de códigos, misma entrega
// (`jwt.sign` + `sendAccessEmail`). «Crypto es una segunda puerta a la misma
// habitación: no se duplica la entrega» (John, 2026-08-31).
//
// ⚠️ LA FIRMA NO ES SOBRE EL CUERPO CRUDO (eso es Stripe). NOWPayments firma
// `JSON.stringify(sortObjectDeep(JSON.parse(body)))` con HMAC-SHA512
// (netlify/shared/nowpayments.ts). El cuerpo se lee respetando
// `isBase64Encoded` porque el `JSON.parse` lo necesita igual.
//
// DOCTRINA DE CÓDIGOS (spec PAGOS_CRYPTO_NOWPAYMENTS.md:196):
//   · 200 en TODO lo procesado o ignorado a conciencia — si no respondemos 200,
//     NOWPayments reintenta, y un reintento eterno de algo que nunca vamos a
//     entregar es ruido que tapa los fallos de verdad.
//   · 400 sin firma o con firma mala, y nada más: ni se lee el pedido.
//   · 500 SÓLO cuando queremos que reintenten: pedido aún no visible, lock
//     ocupado, o el email no salió. Un pago legítimo nunca se pierde por eso.
//
// ORDEN DE LAS PUERTAS (spec :147, corregido por la refutación :164-:171):
//   405 → 501 sin IPN secret → 500 misconfigured (JWT/Resend/API key) →
//   cuerpo → JSON → firma → guardar IPN crudo → pedido → estado → idempotencia
//   → reconfirmación fuera de banda → lock → email → delivered → 200.
//
// POR QUÉ SE RECONFIRMA CON `GET /payment/{id}` ANTES DE ENTREGAR (spec :164):
// el `price_amount` que viene en el IPN es el que pusimos NOSOTROS al crear la
// factura, así que no detecta un infrapago. Y si algún día se filtrara el IPN
// secret, la firma sola dejaría de ser prueba de pago. La API con nuestra key
// es la fuente independiente.
//
// SIN LOGS DE SECRETOS NI EMAILS COMPLETOS: `maskEmail` en todo lo que se
// imprime (los logs de Netlify los ve cualquiera con acceso al panel).
//
// CÓMO VERIFICAR EN PRODUCCIÓN (tras el deploy):
//   curl -i -X POST https://aichef.pro/.netlify/functions/nowpayments-ipn \
//     -H 'Content-Type: application/json' -d '{"payment_id":1}'
//   → 400 missing_signature. Si devuelve 501 webhook_not_configured es que no
//     lee NOWPAYMENTS_IPN_SECRET (recuerda: tras `netlify env:set` el redeploy
//     es OBLIGATORIO, ver stripe-webhook.ts:14).
// ════════════════════════════════════════════════════════════════════════════

/** Un lock de entrega más viejo que esto se considera caducado: la function
 *  murió a mitad (timeout de 10 s, cold start desafortunado) y dejó el pedido
 *  bloqueado. Sin caducidad, esa venta no se entregaría jamás. */
const LOCK_CADUCA_MS = 10 * 60 * 1000;

/** Un pago cuyo `created_at` es más reciente que esto y cuyo pedido no
 *  aparece en el libro se trata como «todavía no visible» → 500 y reintentan.
 *  Más viejo: el pedido no es nuestro (factura creada a mano en el panel) →
 *  200 y se archiva como huérfano (spec :167). */
const VENTANA_PEDIDO_RECIENTE_MS = 24 * 60 * 60 * 1000;

const RATIO_MINIMO_DEFECTO = 0.95;

const json = (statusCode: number, body: Record<string, unknown>) => ({
  statusCode,
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(body),
});

const num = (v: unknown): number | undefined => {
  if (v === null || v === undefined || v === '') return undefined;
  const n = Number(v);
  return Number.isFinite(n) ? n : undefined;
};

/** Línea extra del email para las compras cripto: recuerda por escrito la
 *  renuncia al desistimiento que el comprador marcó en el diálogo (spec :173).
 *  Va como `extraHtml` de `sendAccessEmail`, que sin ese argumento emite
 *  exactamente el mismo HTML de siempre (la ruta de Stripe no cambia). */
const AVISO_CRIPTO = `
          <p style="color: #666; font-size: 14px; line-height: 1.6;">
            Compra pagada en criptomoneda. Al solicitar el acceso inmediato al contenido digital renunciaste al derecho de desistimiento de 14 días, tal y como marcaste al pagar. Si necesitas ayuda, escríbenos a <a href="mailto:info@aichef.pro" style="color: #FFD700;">info@aichef.pro</a> con tu número de pedido.
          </p>`;

/** Lee el pedido con su etag. Se usa también para RELEER cuando una escritura
 *  condicional gana pero la plataforma no devuelve etag, y cuando otro IPN
 *  simultáneo nos pisa: en los dos casos seguir con un etag viejo convertiría
 *  el lock siguiente en un fallo silencioso.
 *
 *  Normaliza de paso los campos que se van a mutar: el JSON pudo escribirlo
 *  otra versión de este código, y un `flags` ausente convertiría un `.push()`
 *  en un TypeError → 500 en bucle sobre un pago legítimo. */
async function refrescar(
  store: BlobStore,
  orderId: string,
): Promise<{ order: CryptoOrder; etag?: string } | null> {
  try {
    const res = await getOrderWithEtag(store, orderId);
    if (!res) return null;
    if (!Array.isArray(res.order.flags)) res.order.flags = [];
    if (typeof res.order.ipnCount !== 'number' || !Number.isFinite(res.order.ipnCount)) res.order.ipnCount = 0;
    return res;
  } catch (err) {
    console.error('[nowpayments-ipn] no se pudo releer el pedido', orderId, err);
    return null;
  }
}

export const handler: Handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return json(405, { error: 'method_not_allowed' });
  }

  const ipnSecret = String(process.env.NOWPAYMENTS_IPN_SECRET || '');
  if (!ipnSecret.trim()) {
    console.error('[nowpayments-ipn] NOWPAYMENTS_IPN_SECRET no configurado: endpoint inerte');
    return json(501, { error: 'webhook_not_configured' });
  }

  // Guardas de entorno ANTES de tocar nada (patrón stripe-webhook.ts:56).
  // `sendAccessEmail` retorna EN SILENCIO si falta RESEND_API_KEY
  // (verify-purchase.ts:427): sin esta guarda marcaríamos como entregado un
  // pedido al que nunca le salió el email. Es el modo de fallo más caro de todos.
  const apiKey = String(process.env.NOWPAYMENTS_API_KEY || '').trim();
  if (!process.env.JWT_SECRET || !process.env.RESEND_API_KEY || !apiKey) {
    console.error('[nowpayments-ipn] faltan JWT_SECRET / RESEND_API_KEY / NOWPAYMENTS_API_KEY');
    return json(500, { error: 'misconfigured' });
  }

  const raw = readRawBody(event);
  let payload: Record<string, unknown>;
  try {
    payload = JSON.parse(raw || '{}');
  } catch {
    return json(400, { error: 'invalid_json' });
  }
  if (!payload || typeof payload !== 'object' || Array.isArray(payload)) {
    return json(400, { error: 'invalid_json' });
  }

  const cabeceras: Record<string, string> = {};
  for (const [k, v] of Object.entries(event.headers || {})) {
    if (typeof v === 'string') cabeceras[k.toLowerCase()] = v;
  }
  const firma = cabeceras['x-nowpayments-sig'] || '';
  if (!firma) {
    return json(400, { error: 'missing_signature' });
  }
  if (!verifyIpnSignature(payload, firma, ipnSecret)) {
    console.warn('[nowpayments-ipn] firma inválida para el pago', String(payload.payment_id ?? '?'));
    // Durante el piloto (`CRYPTO_LOG_REJECTED_IPN=1`) se guarda también lo que
    // se rechaza: si NOWPayments firmara con una variante que no contemplamos,
    // ésta es la única evidencia para diagnosticarlo. Apagado por defecto para
    // que un curl en bucle no llene el store de basura. Nunca cambia el 400.
    if (String(process.env.CRYPTO_LOG_REJECTED_IPN || '').trim() === '1') {
      try {
        const st = await abrirLibro(event);
        await saveRawIpn(st, payload, cabeceras, raw, 'ipn-rechazados');
      } catch (err) {
        console.error('[nowpayments-ipn] no se pudo guardar el IPN rechazado:', err);
      }
    }
    return json(400, { error: 'invalid_signature' });
  }

  const pago = payload as NowPaymentsPayment;
  const paymentId = pago.payment_id != null ? String(pago.payment_id) : '';
  const estado = typeof pago.payment_status === 'string' ? pago.payment_status : '';
  const orderId = typeof pago.order_id === 'string' ? pago.order_id.trim() : '';

  let store: BlobStore;
  try {
    store = await abrirLibro(event);
  } catch (err) {
    // Sin libro no se puede comprobar la idempotencia: entregar a ciegas podría
    // mandar el mismo email en bucle con cada reintento. 500 y que reintenten.
    console.error('[nowpayments-ipn] no se pudo abrir el libro de pedidos:', err);
    return json(500, { error: 'order_not_found_retry' });
  }

  // Evidencia primero, y siempre: nunca rompe el flujo (spec :190).
  await saveRawIpn(store, payload, cabeceras, raw);

  // ── Pedido ────────────────────────────────────────────────────────────────
  let leido: { order: CryptoOrder; etag?: string } | null = null;
  if (esOrderId(orderId)) {
    leido = await refrescar(store, orderId);
  }
  if (!leido) {
    const creado = Date.parse(String(pago.created_at || ''));
    // Sólo se reintenta si el order_id tiene NUESTRO formato (32 hex): un
    // pedido nuestro que aún no es visible. Un order_id con otro formato es una
    // factura creada a mano en el panel (o de otra integración): no va a
    // aparecer nunca en el libro y reintentarla 24 h sería ruido. Si el pago no
    // se puede fechar se asume RECIENTE: perder una venta por un campo ilegible
    // es peor que un puñado de reintentos que acaban parando.
    const formatoNuestro = esOrderId(orderId);
    const reciente = formatoNuestro && (!Number.isFinite(creado) || Date.now() - creado < VENTANA_PEDIDO_RECIENTE_MS);
    await saveOrphan(store, paymentId, reciente ? 'order_not_found_retry' : 'unknown_order', {
      orderId,
      estado,
      payload,
    });
    if (reciente) {
      console.warn(`[nowpayments-ipn] pago ${paymentId} sin pedido ${orderId || '(sin order_id)'} — 500 para que reintenten`);
      return json(500, { error: 'order_not_found_retry' });
    }
    console.warn(`[nowpayments-ipn] pago ${paymentId} con order_id ajeno o caducado (${orderId || 'sin order_id'})`);
    return json(200, { ignored: 'unknown_order' });
  }

  let pedido = leido.order;
  let etag = leido.etag;

  // ── Anotar el pago (siempre) ──────────────────────────────────────────────
  // Los campos del pago SÓLO se pisan si el pedido no está entregado o si es el
  // mismo pago: si ya se entregó y llega otro payment_id (alguien pagó dos
  // veces la misma factura, que es reutilizable), sobrescribir borraría el
  // rastro del pago que sí se sirvió. Ahí sólo se cuenta el IPN y se marca.
  let mismoPago = !pedido.paymentId || pedido.paymentId === paymentId;
  const pagoAjenoSobrePedidoServido = pedido.delivered && !mismoPago;

  pedido.ipnCount = (pedido.ipnCount || 0) + 1;
  pedido.lastIpnAt = new Date().toISOString();
  if (pagoAjenoSobrePedidoServido) {
    if (!pedido.flags.includes('segundo_pago')) pedido.flags.push('segundo_pago');
  } else {
    if (paymentId) pedido.paymentId = paymentId;
    if (estado) pedido.status = estado;
    if (typeof pago.pay_currency === 'string') pedido.payCurrency = pago.pay_currency.toLowerCase();
    if (typeof pago.outcome_currency === 'string') pedido.outcomeCurrency = pago.outcome_currency.toLowerCase();
    const pa = num(pago.pay_amount);
    if (pa !== undefined) pedido.payAmount = pa;
    const ap = num(pago.actually_paid);
    if (ap !== undefined) pedido.actuallyPaid = ap;
    const oa = num(pago.outcome_amount);
    if (oa !== undefined) pedido.outcomeAmount = oa;
  }

  const tras = await updateOrder(store, pedido, etag);
  if (tras === null) {
    // Otro IPN del mismo pedido escribió a la vez: adoptamos su versión. Lo que
    // impide la doble entrega no es esta escritura, es el lock de más abajo.
    const rele = await refrescar(store, pedido.orderId);
    if (rele) {
      pedido = rele.order;
      etag = rele.etag;
      // Recalculado sobre la versión adoptada: si no, la comprobación de
      // idempotencia de abajo miraría el `paymentId` de una foto vieja y
      // etiquetaría mal un segundo pago (la entrega no corre peligro —de eso
      // se encarga el lock— pero el motivo del 200 sería engañoso).
      mismoPago = !pedido.paymentId || pedido.paymentId === paymentId;
    }
  } else {
    etag = tras || (await refrescar(store, pedido.orderId))?.etag;
  }

  const marca = `${pedido.orderId} · ${pedido.productId} · ${maskEmail(pedido.emailNorm)}`;

  // ── Estado ────────────────────────────────────────────────────────────────
  if (!isKnownStatus(estado)) {
    console.warn(`[nowpayments-ipn] estado DESCONOCIDO «${estado}» en el pago ${paymentId} (${marca}) — anotado y ninguna acción`);
    return json(200, { ignored: 'unknown_status', status: estado });
  }
  if (estado !== 'finished') {
    // `waiting`, `confirming`, `confirmed`, `sending`, `partially_paid`,
    // `failed`, `refunded`, `expired`: sólo se anotan. Únicamente `finished`
    // garantiza el cobro íntegro.
    return json(200, { ignored: estado });
  }

  // ── Idempotencia ──────────────────────────────────────────────────────────
  if (pedido.delivered) {
    if (mismoPago) {
      return json(200, { ignored: 'already_delivered' });
    }
    // Factura reutilizable pagada dos veces (spec :168): no se entrega otra vez
    // y John lo resuelve en el panel (devolución o alta manual).
    console.warn(`[nowpayments-ipn] pago ${paymentId} sobre el pedido YA SERVIDO ${marca} (servido por ${pedido.paymentId})`);
    await saveOrphan(store, paymentId, 'order_already_fulfilled', {
      orderId: pedido.orderId,
      productId: pedido.productId,
      servidoPor: pedido.paymentId,
      payload,
    });
    return json(200, { ignored: 'order_already_fulfilled' });
  }

  if (!PRODUCTS[pedido.productId]) {
    console.error(`[nowpayments-ipn] el pedido ${pedido.orderId} apunta a un producto inexistente: ${pedido.productId}`);
    return json(200, { ignored: 'unknown_product' });
  }

  // ── Reconfirmación fuera de banda ─────────────────────────────────────────
  let apiPago: NowPaymentsPayment;
  try {
    apiPago = await getPayment(paymentId, apiKey);
  } catch (err) {
    // No se pudo comprobar: NO se entrega a ciegas, pero tampoco se descarta la
    // venta. 500 → NOWPayments reintenta y la próxima vez sí se podrá confirmar.
    console.error(`[nowpayments-ipn] getPayment(${paymentId}) falló para ${marca}:`, (err as Error).message);
    return json(500, { error: 'reconfirm_failed' });
  }

  const ratioMinimo = (() => {
    const n = Number(process.env.CRYPTO_MIN_PAID_RATIO);
    return Number.isFinite(n) && n > 0 ? n : RATIO_MINIMO_DEFECTO;
  })();

  const anotarYSalir = async (motivo: string, detalle: Record<string, unknown>) => {
    if (!pedido.flags.includes(motivo)) pedido.flags.push(motivo);
    await updateOrder(store, pedido, etag).catch(() => null);
    await saveOrphan(store, paymentId, motivo, { orderId: pedido.orderId, productId: pedido.productId, ...detalle });
    console.warn(`[nowpayments-ipn] ${motivo} en ${marca}:`, JSON.stringify(detalle));
    return json(200, { ignored: motivo });
  };

  if (apiPago.payment_status !== 'finished') {
    const apiStatus = typeof apiPago.payment_status === 'string' ? apiPago.payment_status : '';
    const terminalContradictorio = ['partially_paid', 'failed', 'refunded', 'expired'].includes(apiStatus);
    if (terminalContradictorio) {
      // El IPN dice «finished» y la API un estado terminal distinto: no se
      // entrega y John lo mira en el panel.
      return await anotarYSalir('not_finished_on_api', { apiStatus });
    }
    // Estado intermedio (o vacío) en la API: puede ser propagación. NO se
    // descarta la venta con un 200 — 500 y NOWPayments reintenta; a la
    // siguiente la API ya dirá `finished`. Queda anotado por si no llega.
    if (!pedido.flags.includes('not_finished_on_api')) pedido.flags.push('not_finished_on_api');
    await updateOrder(store, pedido, etag).catch(() => null);
    await saveOrphan(store, paymentId, 'not_finished_on_api_retry', { orderId: pedido.orderId, productId: pedido.productId, apiStatus });
    console.warn(`[nowpayments-ipn] IPN finished pero la API dice «${apiStatus || '?'}» para ${marca} — 500 para que reintenten`);
    return json(500, { error: 'reconfirm_mismatch_retry' });
  }
  const monedaApi = String(apiPago.price_currency || '').toLowerCase();
  const importeApi = num(apiPago.price_amount);
  if (monedaApi !== 'eur' || importeApi === undefined || importeApi !== pedido.priceEur) {
    return await anotarYSalir('amount_mismatch', {
      esperado: `${pedido.priceEur} eur`,
      recibido: `${importeApi ?? 'null'} ${monedaApi || 'null'}`,
    });
  }
  const pagado = num(apiPago.actually_paid);
  const aPagar = num(apiPago.pay_amount);
  if (aPagar === undefined || aPagar <= 0 || pagado === undefined) {
    // Sin las dos cifras no se puede medir el infrapago. Se marca para que John
    // lo mire en el panel en vez de entregar sin comprobar.
    return await anotarYSalir('amount_mismatch', { pay_amount: aPagar ?? null, actually_paid: pagado ?? null });
  }
  const ratio = pagado / aPagar;
  if (ratio < ratioMinimo) {
    return await anotarYSalir('underpaid', { ratio: Math.round(ratio * 10000) / 10000, minimo: ratioMinimo });
  }

  // ── Lock de entrega (escritura condicional) ───────────────────────────────
  const lockPrevio = pedido.deliveryLockAt ? Date.parse(pedido.deliveryLockAt) : NaN;
  const lockVigente = Number.isFinite(lockPrevio) && Date.now() - lockPrevio < LOCK_CADUCA_MS;
  if (lockVigente) {
    console.warn(`[nowpayments-ipn] entrega ya en curso para ${marca} (lock de ${pedido.deliveryLockAt})`);
    return json(500, { error: 'delivery_in_progress' });
  }
  pedido.deliveryLockAt = new Date().toISOString();
  const trasLock = await updateOrder(store, pedido, etag);
  if (trasLock === null) {
    // Otro IPN simultáneo se llevó el lock: que entregue él.
    console.warn(`[nowpayments-ipn] lock perdido en carrera para ${marca}`);
    return json(500, { error: 'delivery_in_progress' });
  }
  etag = trasLock || (await refrescar(store, pedido.orderId))?.etag;

  // ── Entrega ───────────────────────────────────────────────────────────────
  const jwt = (await import('jsonwebtoken')).default;
  const token = jwt.sign({ email: pedido.emailNorm, product: pedido.productId }, process.env.JWT_SECRET, {
    expiresIn: '365d',
  });

  try {
    await sendAccessEmail(pedido.emailNorm, token, pedido.productId, AVISO_CRIPTO);
  } catch (err) {
    // Se libera el lock para que el reintento de NOWPayments pueda volver a
    // intentarlo; si no, el pedido quedaría bloqueado 10 minutos por nada.
    console.error(`[nowpayments-ipn] sendAccessEmail falló para ${marca}:`, err);
    pedido.deliveryLockAt = undefined;
    await updateOrder(store, pedido, etag).catch(() => null);
    return json(500, { error: 'email_failed' });
  }

  // ── Marcar entregado ──────────────────────────────────────────────────────
  pedido.delivered = true;
  pedido.deliveredAt = new Date().toISOString();
  pedido.deliveryLockAt = undefined;
  let marcado = await updateOrder(store, pedido, etag);
  if (marcado === null) {
    // Reintento único con etag fresco. NO se responde 500 pase lo que pase: el
    // email YA salió, y un 500 haría que NOWPayments reintentara y mandara otro.
    const rele = await refrescar(store, pedido.orderId);
    if (rele) {
      const fresco = rele.order;
      fresco.delivered = true;
      fresco.deliveredAt = pedido.deliveredAt;
      fresco.deliveryLockAt = undefined;
      marcado = await updateOrder(store, fresco, rele.etag).catch(() => null);
    }
    if (marcado === null) {
      console.error(`[nowpayments-ipn] ⚠ email ENVIADO a ${marca} pero el pedido NO quedó marcado como entregado — revisar a mano`);
    }
  }

  console.log(`[nowpayments-ipn] acceso enviado: ${pedido.productId} → ${maskEmail(pedido.emailNorm)} (pedido ${pedido.orderId}, pago ${paymentId})`);
  return json(200, { sent: true, product: pedido.productId });
};
