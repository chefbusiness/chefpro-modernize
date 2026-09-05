// ════════════════════════════════════════════════════════════════════════════
// Cliente de NOWPayments + verificación de la firma del IPN (2026-09-05).
//
// POR QUÉ SIN SDK: el SDK oficial de Node arrastra dependencias para tres
// llamadas HTTP y una función de firma. Aquí sólo se usan `fetch` (nativo en el
// runtime de Netlify) y `node:crypto`. Vive en `netlify/shared/` y NO en
// `netlify/functions/` para que el bundler no lo tome por una function.
//
// ⚠️ LA FIRMA DEL IPN NO SE CALCULA SOBRE EL CUERPO CRUDO (eso es Stripe).
// NOWPayments firma `JSON.stringify(sortObjectDeep(JSON.parse(body)))` con
// HMAC-SHA512 y el *IPN secret* del panel (`.trim()`). Ver spec
// PAGOS_CRYPTO_NOWPAYMENTS.md:163 y :149. La prosa de la documentación oficial
// que dice `JSON.stringify(params, Object.keys(params).sort())` es INCORRECTA:
// el segundo argumento de JSON.stringify es un *replacer*, no un comparador, y
// además no baja a los objetos anidados. No usarla.
//
// MONEDAS SIEMPRE EN MINÚSCULAS (`'eur'`): la API las acepta en ambos casos
// pero las devuelve en minúscula, y el IPN se compara contra lo que guardamos.
//
// CERO REINTENTOS al crear la factura: `POST /invoice` no es idempotente y una
// factura de NOWPayments **no se puede borrar**. Un reintento por timeout deja
// facturas huérfanas en el panel de John para siempre. Timeout 5 s (spec :172),
// dentro de los 10 s de presupuesto de una function síncrona.
// ════════════════════════════════════════════════════════════════════════════

import { createHmac, timingSafeEqual } from 'node:crypto';

const API_BASE_DEFAULT = 'https://api.nowpayments.io/v1';

/** Base de la API sin barra final. `NOWPAYMENTS_API_BASE` permite apuntar al
 *  sandbox (`https://api-sandbox.nowpayments.io/v1`) desde un deploy preview. */
export function apiBase(): string {
  const raw = String(process.env.NOWPAYMENTS_API_BASE || '').trim();
  return (raw || API_BASE_DEFAULT).replace(/\/+$/, '');
}

// ── Estados oficiales (spec :181) ───────────────────────────────────────────
// Los 9 y sólo los 9. Cualquier otro valor se registra como desconocido y NO
// rompe el IPN: si NOWPayments añadiera un estado nuevo, la function debe
// responder 200 (o reintentarían en bucle) en vez de reventar.
export const PAYMENT_STATUSES = [
  'waiting',
  'confirming',
  'confirmed',
  'sending',
  'partially_paid',
  'finished',
  'failed',
  'refunded',
  'expired',
] as const;

export type PaymentStatus = (typeof PAYMENT_STATUSES)[number];

export function isKnownStatus(value: unknown): value is PaymentStatus {
  return typeof value === 'string' && (PAYMENT_STATUSES as readonly string[]).includes(value);
}

// ── Tipos (permisivos a propósito) ──────────────────────────────────────────
// Los campos son los de la colección Postman oficial citada en la spec :158.
// El índice `[k: string]: unknown` es deliberado: NOWPayments añade campos sin
// avisar (`fee`, `burning_percent`, `expiration_estimate_date`…) y un tipo
// cerrado obligaría a tocar este fichero cada vez. Lo que NO se hace es leer
// campos que no estén declarados aquí sin comprobarlos antes.

export interface NowPaymentsInvoiceBody {
  price_amount: number;
  price_currency: string;
  pay_currency?: string;
  payout_currency?: string;
  ipn_callback_url?: string;
  order_id?: string;
  order_description?: string;
  success_url?: string;
  cancel_url?: string;
  partially_paid_url?: string;
  is_fixed_rate?: boolean;
  is_fee_paid_by_user?: boolean;
  [k: string]: unknown;
}

export interface NowPaymentsInvoice {
  id?: string | number;
  invoice_url?: string;
  order_id?: string;
  price_amount?: string | number;
  price_currency?: string;
  created_at?: string;
  [k: string]: unknown;
}

/** Payload del IPN y respuesta de `GET /payment/{id}`: los mismos campos. */
export interface NowPaymentsPayment {
  payment_id?: string | number;
  payment_status?: string;
  pay_address?: string;
  price_amount?: string | number;
  price_currency?: string;
  pay_amount?: string | number;
  actually_paid?: string | number;
  pay_currency?: string;
  order_id?: string;
  order_description?: string;
  purchase_id?: string | number;
  outcome_amount?: string | number;
  outcome_currency?: string;
  invoice_id?: string | number;
  created_at?: string;
  updated_at?: string;
  [k: string]: unknown;
}

/** Error tipado: lleva el status HTTP y el cuerpo para que quien llama pueda
 *  distinguir «NOWPayments dijo que no» (4xx) de «no contestó» (status 0). */
export class NowPaymentsError extends Error {
  readonly status: number;
  readonly body: string;

  constructor(message: string, status: number, body: string) {
    super(message);
    this.name = 'NowPaymentsError';
    this.status = status;
    this.body = body;
  }
}

interface CallOptions {
  timeoutMs?: number;
}

/** Minúsculas en las tres claves de moneda del cuerpo de la invoice. */
function normalizaMonedas(body: NowPaymentsInvoiceBody): NowPaymentsInvoiceBody {
  const out: NowPaymentsInvoiceBody = { ...body };
  for (const clave of ['price_currency', 'pay_currency', 'payout_currency'] as const) {
    const v = out[clave];
    if (typeof v === 'string') out[clave] = v.trim().toLowerCase();
  }
  return out;
}

/** Una llamada, sin reintentos, con AbortController. */
async function llamar(
  url: string,
  init: { method: 'GET' | 'POST'; body?: string },
  apiKey: string,
  timeoutMs: number,
): Promise<unknown> {
  const control = new AbortController();
  const alarma = setTimeout(() => control.abort(), timeoutMs);
  let res: Response;
  try {
    res = await fetch(url, {
      method: init.method,
      headers: {
        'x-api-key': apiKey,
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
      body: init.body,
      signal: control.signal,
    });
  } catch (err) {
    // Timeout o fallo de red. status 0 = «no hubo respuesta»: quien llama debe
    // responder 503 gateway_unavailable y NO reintentar (la factura podría
    // haberse creado igualmente al otro lado).
    const motivo = (err as Error)?.name === 'AbortError' ? `timeout tras ${timeoutMs} ms` : String((err as Error)?.message || err);
    throw new NowPaymentsError(`NOWPayments no respondió: ${motivo}`, 0, '');
  } finally {
    clearTimeout(alarma);
  }

  const texto = await res.text();
  if (!res.ok) {
    throw new NowPaymentsError(`NOWPayments ${res.status}`, res.status, texto.slice(0, 500));
  }
  try {
    return JSON.parse(texto) as unknown;
  } catch {
    throw new NowPaymentsError('NOWPayments devolvió un cuerpo no-JSON', res.status, texto.slice(0, 500));
  }
}

/** POST /invoice. Lanza `NowPaymentsError` en cualquier fallo. Sin reintentos. */
export async function createInvoice(
  body: NowPaymentsInvoiceBody,
  apiKey: string,
  opts: CallOptions = {},
): Promise<NowPaymentsInvoice> {
  const timeoutMs = opts.timeoutMs ?? 5000;
  const data = await llamar(
    `${apiBase()}/invoice`,
    { method: 'POST', body: JSON.stringify(normalizaMonedas(body)) },
    apiKey,
    timeoutMs,
  );
  return (data || {}) as NowPaymentsInvoice;
}

/** GET /payment/{id} — reconfirmación fuera de banda antes de entregar
 *  (spec :146 y :164). Sólo necesita la API key. */
export async function getPayment(
  paymentId: string | number,
  apiKey: string,
  opts: CallOptions = {},
): Promise<NowPaymentsPayment> {
  const timeoutMs = opts.timeoutMs ?? 5000;
  const data = await llamar(
    `${apiBase()}/payment/${encodeURIComponent(String(paymentId))}`,
    { method: 'GET' },
    apiKey,
    timeoutMs,
  );
  return (data || {}) as NowPaymentsPayment;
}

// ── Firma del IPN ───────────────────────────────────────────────────────────

/** Ordena las claves de los objetos planos RECURSIVAMENTE. Arrays y `null` se
 *  respetan (spec :149): un array conserva su orden y sigue siendo un array —
 *  la variante ingenua del SDK de Node (`Object.keys(arr).sort().reduce`)
 *  convertiría `[1,2]` en `{"0":1,"1":2}` y produciría otra firma. Con los
 *  payloads reales de NOWPayments (objetos planos + `fee` anidado) las dos
 *  coinciden; la divergencia sólo aparecería si algún día mandan un array. */
export function sortObjectDeep(value: unknown): unknown {
  if (Array.isArray(value)) {
    return value.map((v) => sortObjectDeep(v));
  }
  if (value === null || typeof value !== 'object') {
    return value;
  }
  const origen = value as Record<string, unknown>;
  const out: Record<string, unknown> = {};
  for (const clave of Object.keys(origen).sort()) {
    out[clave] = sortObjectDeep(origen[clave]);
  }
  return out;
}

/** Variante LITERAL del `sortObject` del ejemplo oficial de Node (colección
 *  Postman): `Object.keys(obj).sort().reduce(...)` aplicado a TODO lo que sea
 *  `typeof 'object'` no nulo — arrays incluidos. Un array `[a, b]` se convierte
 *  en `{"0": a, "1": b}` (las claves enteras de un objeto JS se serializan
 *  siempre en orden numérico, haga lo que haga el `sort`). Es lo que un
 *  servidor escrito con ese mismo snippet produciría. Se conserva porque NO SABEMOS con cuál de las dos
 *  variantes firma NOWPayments cuando el payload lleva un array (la respuesta
 *  de `GET /payment/{id}` trae `payment_extra_ids: [...]`): la verificación
 *  acepta cualquiera de las dos, que son igual de seguras (las dos son un HMAC
 *  con el secreto). Con payloads sin arrays producen exactamente lo mismo. */
export function sortObjectLegacy(value: unknown): unknown {
  if (value && typeof value === 'object') {
    const origen = value as Record<string, unknown>;
    return Object.keys(origen)
      .sort()
      .reduce<Record<string, unknown>>((acc, clave) => {
        acc[clave] = sortObjectLegacy(origen[clave]);
        return acc;
      }, {});
  }
  return value;
}

/** HMAC-SHA512 hex del JSON con claves ordenadas. El secreto va con `.trim()`:
 *  copiarlo del panel arrastra un salto de línea con una facilidad pasmosa y el
 *  fallo sería «firma inválida» en TODOS los pagos, sin más pista. */
export function computeIpnSignature(payload: unknown, secret: string): string {
  return createHmac('sha512', String(secret).trim())
    .update(JSON.stringify(sortObjectDeep(payload)))
    .digest('hex');
}

/** Misma firma con la variante legacy (arrays → objetos). Ver `sortObjectLegacy`. */
export function computeIpnSignatureLegacy(payload: unknown, secret: string): string {
  return createHmac('sha512', String(secret).trim())
    .update(JSON.stringify(sortObjectLegacy(payload)))
    .digest('hex');
}

function iguales(dada: string, esperada: string): boolean {
  if (dada.length !== esperada.length) return false;
  const a = Buffer.from(dada, 'hex');
  const b = Buffer.from(esperada, 'hex');
  // Buffer.from con hex inválido trunca en silencio → longitudes distintas.
  if (a.length === 0 || a.length !== b.length) return false;
  try {
    return timingSafeEqual(a, b);
  } catch {
    return false;
  }
}

/** Comparación en tiempo constante contra las DOS variantes oficiales de
 *  ordenación (ver `sortObjectLegacy`). Devuelve false —nunca lanza— si la
 *  firma está vacía, no es hex, o los buffers no miden lo mismo
 *  (`timingSafeEqual` lanza `RangeError` con longitudes distintas). Se evalúan
 *  siempre las dos para no filtrar por tiempo cuál coincidió. */
export function verifyIpnSignature(payload: unknown, signature: unknown, secret: string): boolean {
  const dada = typeof signature === 'string' ? signature.trim() : '';
  if (!dada || !secret) return false;
  let moderna: string;
  let legacy: string;
  try {
    moderna = computeIpnSignature(payload, secret);
    legacy = computeIpnSignatureLegacy(payload, secret);
  } catch {
    return false;
  }
  const okModerna = iguales(dada, moderna);
  const okLegacy = iguales(dada, legacy);
  return okModerna || okLegacy;
}

/** Cuerpo crudo del evento respetando `isBase64Encoded` (spec :163). Netlify
 *  entrega el cuerpo en base64 cuando el content-type no está en su lista de
 *  tipos de texto; leerlo sin decodificar rompería la firma y el JSON.parse. */
export function readRawBody(event: { body?: string | null; isBase64Encoded?: boolean }): string {
  const body = event?.body || '';
  if (!body) return '';
  return event.isBase64Encoded ? Buffer.from(body, 'base64').toString('utf8') : body;
}
