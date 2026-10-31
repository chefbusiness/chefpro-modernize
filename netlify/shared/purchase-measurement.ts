/**
 * Importe de una Checkout Session de Stripe, para medirlo en el gate `-access`.
 *
 * Solo Stripe. NOWPayments no crea una Checkout Session: el acceso cripto llega
 * por el IPN y el magic link `?jwt=`, y esa respuesta no lleva `purchase`.
 *
 * `amount_total` viene en la unidad menor de la moneda (céntimos en EUR/USD).
 * Adaptive Pricing puede cobrar en otra divisa: se respeta la de la sesión.
 */

export interface PurchaseMeasurement {
  /** Importe en unidades mayores (14.5 = 14,50 €). */
  value: number;
  /** ISO 4217 en mayúsculas, tal como cobró Stripe. */
  currency: string;
  /** `pi_…` si hay payment_intent; si no, el id de la sesión `cs_…`. */
  transactionId: string;
  sessionId: string;
  paymentId: string | null;
  productId: string;
}

export interface StripeSessionMedible {
  id: string;
  amount_total: number | null;
  currency: string | null;
  payment_intent?: string | { id: string } | null;
  payment_status?: string | null;
}

const SESSION_RE = /^cs_(?:test|live)_[A-Za-z0-9]{8,}$/;
const PAYMENT_RE = /^pi_[A-Za-z0-9]{8,}$/;
const SLUG_RE = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

/** Monedas sin decimales, según la lista de Stripe. El resto de las habituales van a 2. */
const ZERO_DECIMAL = new Set([
  'BIF', 'CLP', 'DJF', 'GNF', 'JPY', 'KMF', 'KRW', 'MGA', 'PYG', 'RWF',
  'UGX', 'VND', 'VUV', 'XAF', 'XOF', 'XPF',
]);
const THREE_DECIMAL = new Set(['BHD', 'JOD', 'KWD', 'OMR', 'TND']);

function aUnidadesMayores(amountMinor: number, currency: string): number {
  if (ZERO_DECIMAL.has(currency)) return amountMinor;
  const factor = THREE_DECIMAL.has(currency) ? 1000 : 100;
  const decimals = THREE_DECIMAL.has(currency) ? 3 : 2;
  return Number((amountMinor / factor).toFixed(decimals));
}

/**
 * null si la sesión no está pagada, no parece de Checkout, o no trae importe
 * y moneda. El caller (verify-purchase) ya exige `payment_status === 'paid'`.
 */
export function purchaseFromSession(
  session: StripeSessionMedible,
  productId: string,
): PurchaseMeasurement | null {
  if (session.payment_status != null && session.payment_status !== 'paid') return null;
  if (!SESSION_RE.test(session.id) || !SLUG_RE.test(productId)) return null;
  if (typeof session.amount_total !== 'number' || !Number.isFinite(session.amount_total) || session.amount_total < 0) {
    return null;
  }
  const currency = (session.currency || '').trim().toUpperCase();
  if (!/^[A-Z]{3}$/.test(currency)) return null;

  const pi = session.payment_intent;
  const rawPayment = typeof pi === 'string' ? pi : pi?.id;
  const paymentId = rawPayment && PAYMENT_RE.test(rawPayment) ? rawPayment : null;

  return {
    value: aUnidadesMayores(session.amount_total, currency),
    currency,
    transactionId: paymentId ?? session.id,
    sessionId: session.id,
    paymentId,
    productId,
  };
}
