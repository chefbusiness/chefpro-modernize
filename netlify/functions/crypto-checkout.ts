import type { Handler } from '@netlify/functions';
import { PRODUCTS } from './verify-purchase';
import { PRODUCT_PRICES } from '../shared/product-prices';
import { createInvoice, NowPaymentsError } from '../shared/nowpayments';
import {
  abrirLibro,
  createOrder,
  indexOrder,
  newOrderId,
  rateLimitExceeded,
  updateOrder,
  type BlobStore,
  type CryptoOrder,
} from '../shared/crypto-orders';

// ════════════════════════════════════════════════════════════════════════════
// crypto-checkout — abre la segunda puerta: crea la factura de NOWPayments y
// devuelve la URL de su página alojada (2026-09-05, Fase 1 del piloto).
//
// LO QUE NO SE ACEPTA DEL CLIENTE, NUNCA: el importe. El precio sale sólo de
// `netlify/shared/product-prices.ts` (GENERADO desde el `schema.price` de la
// ficha de cada producto). Si el navegador pudiera mandar `price_amount`, la
// guía de 85 € se compraría por 1 €. Del cliente sólo entran producto, email,
// país declarado y los dos consentimientos (spec PAGOS_CRYPTO_NOWPAYMENTS.md:173).
//
// ORDEN DE LAS GUARDAS (spec :195). Cada una responde antes de gastar nada:
//   OPTIONS/CORS → 405 → 503 crypto_disabled (interruptor de emergencia:
//   `CRYPTO_PRODUCTS` vacía apaga el botón en todo el sitio) → 501 sin API key
//   → 403 origin_not_allowed → 429 cupo → 400 validación → 403
//   product_not_enabled (allowlist del piloto) → precio → pedido en el libro →
//   invoice (5 s, cero reintentos) → 200 {url, orderId}.
//
// EL PEDIDO SE ESCRIBE ANTES DE LLAMAR A NOWPAYMENTS, a propósito: si el IPN
// llegara antes de que volviéramos a escribir el invoiceId, el libro ya tiene
// producto, email e importe, que es lo único que hace falta para entregar.
//
// CERO REINTENTOS de la invoice: no es idempotente y las facturas de
// NOWPayments **no se pueden borrar**. Un timeout se responde 503 y el
// comprador vuelve a pulsar; reintentar aquí llenaría el panel de basura.
//
// CUPO POR MINUTO (patrón log-search.ts): un bucle de curl podría crear miles
// de facturas imborrables. El cupo es global al site, no por IP: aquí no se
// lee ninguna cabecera identificativa.
//
// CÓMO VERIFICAR EN PRODUCCIÓN (tras el deploy):
//   curl -i -X POST https://aichef.pro/.netlify/functions/crypto-checkout \
//     -H 'Content-Type: application/json' \
//     -d '{"product":"no-existe","email":"a@b.co","country":"ES","acceptPolicy":true,"waiveWithdrawal":true}'
//   → 400 unknown_product (si devuelve 503 crypto_disabled, falta CRYPTO_PRODUCTS;
//     si 501, falta NOWPAYMENTS_API_KEY — y recuerda que tras `netlify env:set`
//     el redeploy es OBLIGATORIO, ver stripe-webhook.ts:14).
// ════════════════════════════════════════════════════════════════════════════

const MAX_BODY = 2000;
const MAX_EMAIL = 120;
const MAX_FACTURAS_MINUTO = 30;
const TIMEOUT_INVOICE_MS = 5000;
const MAX_DESCRIPCION = 200;

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

const json = (statusCode: number, body: Record<string, unknown>, headers: Record<string, string>) => ({
  statusCode,
  headers,
  body: JSON.stringify(body),
});

// ── Configuración por entorno ───────────────────────────────────────────────

/** Base pública del site. En un deploy preview se apunta a la URL del preview
 *  para que `ipn_callback_url` y `success_url` no manden al de producción. */
export function siteUrl(): string {
  return String(process.env.CRYPTO_SITE_URL || 'https://aichef.pro').trim().replace(/\/+$/, '');
}

/** `'1'`/`'true'` (insensible a mayúsculas) → true. Cualquier otra cosa, false:
 *  los defaults documentados son 0 en las dos (spec :178) porque encarecen la
 *  comisión del 1 % al 1,5 %, y `is_fixed_rate` además caduca a los 10 min. */
function flag(nombre: string): boolean {
  const v = String(process.env[nombre] || '').trim().toLowerCase();
  return v === '1' || v === 'true';
}

/** Allowlist del piloto. Vacía o ausente = botón apagado en TODO el sitio
 *  (interruptor de emergencia). `all` = los 46. Si no, CSV de productIds. */
export function allowlist(): { activa: boolean; todos: boolean; ids: Set<string> } {
  const raw = String(process.env.CRYPTO_PRODUCTS || '').trim();
  if (!raw) return { activa: false, todos: false, ids: new Set() };
  if (raw.toLowerCase() === 'all') return { activa: true, todos: true, ids: new Set() };
  const ids = new Set(
    raw
      .split(',')
      .map((s) => s.trim())
      .filter(Boolean),
  );
  return { activa: ids.size > 0, todos: false, ids };
}

// ── Producto: etiqueta legible y landing ────────────────────────────────────

/** `'Tu acceso al Kit de Escandallos Pro'` → `'Kit de Escandallos Pro'`.
 *  El nombre comercial no existe como campo propio en `PRODUCTS`, pero el
 *  `emailSubject` de los 46 empieza por «Tu acceso a/al/a la/a los/a las …».
 *  Se usa como `order_description` de la factura (lo que el comprador ve en la
 *  página de NOWPayments y en el historial de John) y como `productLabel` de
 *  la página de estado. Alternativa si algún día hace falta más precisión:
 *  el campo `productLabel` de `astro-site/src/lib/zona-app.ts`. */
export function productoLabel(productId: string): string {
  const asunto = PRODUCTS[productId]?.emailSubject || '';
  const limpio = asunto.replace(/^Tu acceso a(?:l| la| los| las)?\s+/i, '').replace(/&amp;/g, '&').trim();
  return (limpio || productId).slice(0, MAX_DESCRIPCION);
}

/** Landing pública del producto, para el `cancel_url`.
 *
 *  La regla general es `accessPath` sin el sufijo `-access`. Falla en DOS de
 *  los 46 y los dos son quirks históricos documentados en
 *  `astro-site/src/lib/zona-app.ts:62` (kit-tareas-hotel: el accessPath lleva
 *  un «-completo-» que la landing no tiene) y `:97` (pro-prompts-ebook: la
 *  landing se llama por el eBook y el acceso por la Library). Comprobado
 *  contra los 46 `landingPath` de ese registro: sólo divergen estos dos. */
const LANDINGS_IRREGULARES: Record<string, string> = {
  'kit-tareas-hotel': '/kit-tareas-hotel',
  'pro-prompts-ebook': '/pro-prompts-ebook',
};

export function landingPath(productId: string): string {
  if (LANDINGS_IRREGULARES[productId]) return LANDINGS_IRREGULARES[productId];
  const acceso = PRODUCTS[productId]?.accessPath || '';
  const derivada = acceso.replace(/-access$/, '');
  return derivada || `/${productId}`;
}

// ── Origen ──────────────────────────────────────────────────────────────────

/** aichef.pro, www y cualquier `*.netlify.app` (deploy previews). Un Origin
 *  AUSENTE se deja pasar: los navegadores lo mandan siempre en un POST, así que
 *  no puede venir de una página de terceros — es curl, y curl es como se
 *  verifican los contratos en el runbook. Lo que se rechaza es un Origin
 *  presente y ajeno. La defensa del dinero no es esto: es que el importe sale
 *  del mapa del servidor y que hay cupo por minuto. */
function origenPermitido(origin: string): boolean {
  if (!origin) return true;
  let host: string;
  try {
    const u = new URL(origin);
    if (u.protocol !== 'https:' && u.protocol !== 'http:') return false;
    host = u.hostname.toLowerCase();
  } catch {
    return false;
  }
  return host === 'aichef.pro' || host === 'www.aichef.pro' || host.endsWith('.netlify.app');
}

/** SÓLO las cabeceras de geo (mismo criterio que log-search.ts:117: ni IP, ni
 *  user-agent, ni nada identificativo). Es evidencia de IVA junto al país que
 *  el comprador declara en el diálogo, no un sustituto de él. */
function paisGeo(raw: Record<string, string | undefined> | undefined): string {
  const h = raw || {};
  const leer = (nombre: string): string => {
    const v = h[nombre] ?? h[nombre.toUpperCase()];
    return typeof v === 'string' ? v : '';
  };
  const directo = leer('x-country') || leer('x-nf-country');
  if (/^[A-Za-z]{2}$/.test(directo)) return directo.toUpperCase();
  const geo = leer('x-nf-geo'); // JSON en base64 con { country: { code, name }, … }
  if (geo) {
    try {
      const datos = JSON.parse(Buffer.from(geo, 'base64').toString('utf-8'));
      const code = datos?.country?.code;
      if (typeof code === 'string' && /^[A-Za-z]{2}$/.test(code)) return code.toUpperCase();
    } catch {
      /* geo ilegible: se ignora, no es motivo para perder la venta */
    }
  }
  return '';
}

// ── Handler ─────────────────────────────────────────────────────────────────

export const handler: Handler = async (event) => {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers, body: '' };
  }
  if (event.httpMethod !== 'POST') {
    return json(405, { error: 'method_not_allowed' }, headers);
  }

  // Interruptor de emergencia antes que nada: sin allowlist no hay botón, y
  // tampoco hace falta tocar Blobs ni NOWPayments para decirlo.
  const lista = allowlist();
  if (!lista.activa) {
    return json(503, { error: 'crypto_disabled' }, headers);
  }

  const apiKey = String(process.env.NOWPAYMENTS_API_KEY || '').trim();
  if (!apiKey) {
    console.error('[crypto-checkout] NOWPAYMENTS_API_KEY no configurada: endpoint inerte');
    return json(501, { error: 'crypto_not_configured' }, headers);
  }

  const cabeceras: Record<string, string> = {};
  for (const [k, v] of Object.entries(event.headers || {})) {
    if (typeof v === 'string') cabeceras[k.toLowerCase()] = v;
  }
  if (!origenPermitido(cabeceras['origin'] || '')) {
    console.warn('[crypto-checkout] origen rechazado:', cabeceras['origin']);
    return json(403, { error: 'origin_not_allowed' }, headers);
  }

  try {
    // ── Libro y cupo ────────────────────────────────────────────────────────
    let store: BlobStore;
    try {
      store = await abrirLibro(event);
    } catch (err) {
      // Sin libro no se puede entregar después: mejor no crear la factura.
      console.error('[crypto-checkout] no se pudo abrir el libro de pedidos:', err);
      return json(503, { error: 'gateway_unavailable' }, headers);
    }

    if (await rateLimitExceeded(store, MAX_FACTURAS_MINUTO)) {
      console.warn('[crypto-checkout] cupo por minuto superado');
      return json(429, { error: 'rate_limited' }, headers);
    }

    // ── Validación ──────────────────────────────────────────────────────────
    if ((event.body || '').length > MAX_BODY) {
      return json(400, { error: 'invalid_request' }, headers);
    }
    let datos: Record<string, unknown>;
    try {
      datos = JSON.parse(event.body || '{}');
    } catch {
      return json(400, { error: 'invalid_request' }, headers);
    }
    if (!datos || typeof datos !== 'object' || Array.isArray(datos)) {
      return json(400, { error: 'invalid_request' }, headers);
    }

    const productId = typeof datos.product === 'string' ? datos.product.trim() : '';
    if (!productId || !PRODUCTS[productId]) {
      return json(400, { error: 'unknown_product' }, headers);
    }

    const emailBruto = typeof datos.email === 'string' ? datos.email.trim() : '';
    const emailNorm = emailBruto.toLowerCase();
    if (!emailBruto || emailBruto.length > MAX_EMAIL || !EMAIL_RE.test(emailBruto)) {
      return json(400, { error: 'invalid_email' }, headers);
    }

    const country = (typeof datos.country === 'string' ? datos.country.trim().toUpperCase() : '');
    if (!/^[A-Z]{2}$/.test(country)) {
      return json(400, { error: 'invalid_country' }, headers);
    }

    // Los dos consentimientos son SEPARADOS y los dos obligatorios (spec :173):
    // aceptar condiciones no es lo mismo que renunciar al desistimiento de 14
    // días, y con un contenido digital de entrega inmediata hacen falta ambos.
    if (datos.acceptPolicy !== true || datos.waiveWithdrawal !== true) {
      return json(400, { error: 'consent_required' }, headers);
    }

    // ── Allowlist del piloto ────────────────────────────────────────────────
    if (!lista.todos && !lista.ids.has(productId)) {
      return json(403, { error: 'product_not_enabled' }, headers);
    }

    // ── Precio: SÓLO del mapa generado ──────────────────────────────────────
    const precio = PRODUCT_PRICES[productId]?.eur;
    if (typeof precio !== 'number' || !Number.isFinite(precio) || precio <= 0) {
      // No debería poder pasar: `sync-product-prices.py --check` exige 46/46
      // contra PRODUCTS. Si pasa, es que se añadió un producto sin regenerar el
      // mapa, y cobrar cero o NaN es peor que no vender.
      console.error(`[crypto-checkout] ${productId} sin precio en PRODUCT_PRICES — correr sync-product-prices.py`);
      return json(500, { error: 'price_not_configured' }, headers);
    }

    // ── Pedido en el libro (antes de llamar a NOWPayments) ──────────────────
    const ahora = new Date().toISOString();
    const orderId = newOrderId();
    const pedido: CryptoOrder = {
      orderId,
      productId,
      email: emailBruto,
      emailNorm,
      priceEur: precio,
      currency: 'eur',
      country,
      geoCountry: paisGeo(event.headers as Record<string, string | undefined>),
      acceptedPolicyAt: ahora,
      waivedWithdrawalAt: ahora,
      createdAt: ahora,
      status: 'created',
      ipnCount: 0,
      delivered: false,
      flags: [],
    };

    try {
      await createOrder(store, pedido);
      await indexOrder(store, pedido);
    } catch (err) {
      console.error('[crypto-checkout] no se pudo registrar el pedido:', err);
      return json(503, { error: 'gateway_unavailable' }, headers);
    }

    // ── Factura ─────────────────────────────────────────────────────────────
    const base = siteUrl();
    let invoice;
    try {
      invoice = await createInvoice(
        {
          price_amount: precio,
          price_currency: 'eur',
          order_id: orderId,
          order_description: productoLabel(productId),
          ipn_callback_url: `${base}/.netlify/functions/nowpayments-ipn`,
          success_url: `${base}/pago-cripto?o=${orderId}`,
          cancel_url: `${base}${landingPath(productId)}#comprar`,
          partially_paid_url: `${base}/pago-cripto?o=${orderId}&estado=parcial`,
          is_fixed_rate: flag('CRYPTO_FIXED_RATE'),
          is_fee_paid_by_user: flag('CRYPTO_FEE_PAID_BY_USER'),
          // `pay_currency` se omite a propósito: así el comprador elige moneda
          // y red en la página alojada, que además le avisa de los mínimos.
        },
        apiKey,
        { timeoutMs: TIMEOUT_INVOICE_MS },
      );
    } catch (err) {
      const e = err as NowPaymentsError;
      console.error(`[crypto-checkout] createInvoice falló (${e.status ?? '?'}) para ${productId}:`, e.message, e.body || '');
      return json(503, { error: 'gateway_unavailable' }, headers);
    }

    const url = typeof invoice.invoice_url === 'string' ? invoice.invoice_url : '';
    if (!url) {
      console.error('[crypto-checkout] la invoice llegó sin invoice_url:', JSON.stringify(invoice).slice(0, 300));
      return json(503, { error: 'gateway_unavailable' }, headers);
    }

    // Segunda escritura: invoiceId + invoiceUrl. Si falla, la venta NO se cae —
    // el pedido ya tiene lo necesario para entregar y el IPN llega por
    // `order_id`. Sólo se pierde el enlace de la factura en el informe.
    pedido.invoiceId = invoice.id != null ? String(invoice.id) : undefined;
    pedido.invoiceUrl = url;
    try {
      await updateOrder(store, pedido);
    } catch (err) {
      console.error(`[crypto-checkout] pedido ${orderId} creado pero no se pudo guardar la invoice:`, err);
    }

    console.log(`[crypto-checkout] pedido ${orderId} · ${productId} · ${precio} EUR · invoice ${pedido.invoiceId ?? '?'}`);
    return json(200, { url, orderId }, headers);
  } catch (err) {
    console.error('[crypto-checkout] error inesperado:', err);
    return json(500, { error: 'server_error' }, headers);
  }
};
