/**
 * Medición de una compra de producto digital YA verificada por verify-purchase.
 *
 * Se llama en el gate `-access`, antes de entrar al dashboard, y solo si la
 * respuesta trae `purchase` (Checkout Session pagada). El magic link `?jwt=`
 * y las compras cripto no lo traen.
 *
 * Google Ads ya tiene label. GA4 (`G-7SWN171DEX`) se configura en todo el sitio
 * desde `GoogleTag.astro` y aquí solo añade el `purchase`. Meta sigue vacío:
 * no se dispara y no hace esperar al dashboard. El `purchase` tampoco espera.
 */

/** Misma cuenta que `GOOGLE_ADS_ID` en astro-site/src/components/GoogleTag.astro. */
export const GOOGLE_ADS_ID = 'AW-17829651892';

/**
 * Label de la acción «compra de producto digital» en AW-17829651892.
 * `send_to` queda `AW-17829651892/ARzvCKiTuq8dELTL67VC`.
 */
export const GOOGLE_ADS_PURCHASE_LABEL = 'ARzvCKiTuq8dELTL67VC';

/**
 * Propiedad GA4 de aichef.pro. La misma cadena va en `GoogleTag.astro`, que
 * hace el `gtag('config')` de cada página (Consent Mode ya fijado). Vacío =
 * no se envía `purchase`.
 */
export const GA4_MEASUREMENT_ID = 'G-7SWN171DEX';

/** Píxel de Meta. Vacío = no se carga fbevents.js ni se envía `Purchase`. */
export const META_PIXEL_ID = '';

const SESSION_RE = /^cs_(?:test|live)_[A-Za-z0-9]{8,}$/;
const PAYMENT_RE = /^pi_[A-Za-z0-9]{8,}$/;
const SLUG_RE = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

export interface CompraVerificada {
  value: number;
  currency: string;
  transactionId: string;
  sessionId: string;
  paymentId: string | null;
  productId: string;
}

export function adsLabelActivo(label: string): boolean {
  return label.length > 0
    && label !== 'PENDIENTE_LABEL'
    && /^[A-Za-z0-9_-]{6,}$/.test(label);
}

export function ga4Activo(id: string): boolean {
  return /^G-[A-Z0-9]{6,}$/.test(id);
}

export function metaActivo(id: string): boolean {
  return /^[0-9]{8,20}$/.test(id);
}

/** Acepta solo el objeto que construye purchaseFromSession. Lo demás no se mide. */
export function compraDesdeRespuesta(raw: unknown): CompraVerificada | null {
  if (!raw || typeof raw !== 'object') return null;
  const o = raw as Record<string, unknown>;
  const value = typeof o.value === 'number' ? o.value : Number.NaN;
  const currency = typeof o.currency === 'string' ? o.currency.toUpperCase() : '';
  const transactionId = typeof o.transactionId === 'string' ? o.transactionId : '';
  const sessionId = typeof o.sessionId === 'string' ? o.sessionId : '';
  const productId = typeof o.productId === 'string' ? o.productId : '';
  const paymentId = o.paymentId == null ? null : (typeof o.paymentId === 'string' ? o.paymentId : '');
  if (!Number.isFinite(value) || value < 0 || value > 100_000) return null;
  if (!/^[A-Z]{3}$/.test(currency)) return null;
  if (!SESSION_RE.test(sessionId) || !SLUG_RE.test(productId)) return null;
  if (paymentId !== null && !PAYMENT_RE.test(paymentId)) return null;
  const transactionOk = transactionId === sessionId || (paymentId !== null && transactionId === paymentId);
  if (!transactionOk) return null;
  return { value, currency, transactionId, sessionId, paymentId, productId };
}

export function claveMedicion(transactionId: string): string {
  return `aichef_compra_v1_${transactionId}`;
}

type Gtag = (...args: unknown[]) => void;

interface Fbq {
  (...args: unknown[]): void;
  callMethod?: (...args: unknown[]) => void;
  queue: unknown[][];
  loaded: boolean;
  version: string;
  push: Fbq;
}

interface VentanaMedicion extends Window {
  gtag?: Gtag;
  aichefLeeConsent?: () => string | null;
  fbq?: Fbq;
}

function ventana(): VentanaMedicion {
  return window as VentanaMedicion;
}

function yaMedida(transactionId: string): boolean {
  try {
    return sessionStorage.getItem(claveMedicion(transactionId)) === '1';
  } catch {
    return false;
  }
}

function marcarMedida(transactionId: string): void {
  try {
    sessionStorage.setItem(claveMedicion(transactionId), '1');
  } catch {
    /* modo privado: Google Ads deduplica por transaction_id */
  }
}

function asegurarPixel(pixelId: string): void {
  const w = ventana();
  if (w.fbq) return;
  const fbq = function (...args: unknown[]) {
    if (fbq.callMethod) fbq.callMethod.apply(fbq, args);
    else fbq.queue.push(args);
  } as Fbq;
  fbq.push = fbq;
  fbq.queue = [];
  fbq.loaded = true;
  fbq.version = '2.0';
  w.fbq = fbq;
  const s = document.createElement('script');
  s.async = true;
  s.src = 'https://connect.facebook.net/en_US/fbevents.js';
  document.head.appendChild(s);
  fbq('init', pixelId);
}

function esperarConversion(gtag: Gtag, fields: Record<string, unknown>): Promise<void> {
  return new Promise((resolve) => {
    let settled = false;
    const finish = () => {
      if (settled) return;
      settled = true;
      resolve();
    };
    gtag('event', 'conversion', { ...fields, event_callback: finish });
    window.setTimeout(finish, 800);
  });
}

/**
 * Encola la conversión y resuelve cuando Google confirma el hit, o a los 800 ms.
 * Si ningún canal está configurado, resuelve al momento: el dashboard no espera.
 * No lanza: un fallo de medición no puede dejar al comprador sin acceso.
 */
export function medirCompraVerificada(compra: CompraVerificada, itemName: string): Promise<void> {
  try {
    if (yaMedida(compra.transactionId)) return Promise.resolve();
    const ads = adsLabelActivo(GOOGLE_ADS_PURCHASE_LABEL);
    const ga4 = ga4Activo(GA4_MEASUREMENT_ID);
    const consentimiento = ventana().aichefLeeConsent?.() ?? null;
    const meta = metaActivo(META_PIXEL_ID) && consentimiento === 'accepted';
    const gtag = ventana().gtag;
    const puedeGtag = typeof gtag === 'function';
    if ((!ads && !ga4 && !meta) || (!puedeGtag && !meta)) return Promise.resolve();

    marcarMedida(compra.transactionId);
    const waits: Promise<void>[] = [];
    if (puedeGtag && ads) {
      waits.push(esperarConversion(gtag, {
        send_to: `${GOOGLE_ADS_ID}/${GOOGLE_ADS_PURCHASE_LABEL}`,
        value: compra.value,
        // EUR en los Payment Links en euros; si Stripe cobra en otra, esa.
        currency: compra.currency,
        transaction_id: compra.transactionId,
      }));
    }
    if (puedeGtag && ga4) {
      // `send_page_view: false`: GoogleTag ya mandó la página. `send_to` deja
      // el purchase solo en GA4; la conversión de Ads sigue en el evento de arriba.
      gtag('config', GA4_MEASUREMENT_ID, { send_page_view: false });
      gtag('event', 'purchase', {
        send_to: GA4_MEASUREMENT_ID,
        transaction_id: compra.transactionId,
        value: compra.value,
        currency: compra.currency,
        items: [{
          item_id: compra.productId,
          item_name: itemName,
          price: compra.value,
          quantity: 1,
        }],
      });
    }
    if (meta) {
      asegurarPixel(META_PIXEL_ID);
      ventana().fbq?.('track', 'Purchase', {
        value: compra.value,
        currency: compra.currency,
        content_ids: [compra.productId],
        content_name: itemName,
        content_type: 'product',
        num_items: 1,
      }, { eventID: compra.transactionId });
    }
    return Promise.all(waits).then(() => undefined);
  } catch {
    return Promise.resolve();
  }
}
