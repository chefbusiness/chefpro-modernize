// ════════════════════════════════════════════════════════════════════════════
// Libro de pedidos cripto — Netlify Blobs, store `crypto-orders` (2026-09-05).
//
// EL LIBRO ES LA ÚNICA VERDAD. El `order_id` que viaja a NOWPayments es opaco
// (32 hex, sin productId ni HMAC dentro, spec PAGOS_CRYPTO_NOWPAYMENTS.md:165):
// producto, importe y email salen SIEMPRE de aquí, nunca del IPN. Así un IPN
// forjado con `order_id` inventado no puede pedir la entrega de otro producto.
//
// CONSISTENCIA FUERTE CUANDO EL RUNTIME LA SOPORTA (spec :166). En `log-search`
// una lectura obsoleta cuesta una línea de telemetría; aquí cuesta un reintento:
// el IPN puede llegar segundos después del checkout que escribió el pedido, y
// con consistencia eventual leería «no existe» → 500 → NOWPayments reintenta y
// a la siguiente lo encuentra. Ver `abrirLibro`: en functions v1 la fuerte no
// está disponible y se cae a eventual (medido en el deploy preview 78).
//
// ⚠️ GOTCHA DE BLOBS (el mismo de log-search.ts:35): sólo funciona DESPLEGADO
// en Netlify. Y al ser functions v1 (Lambda-compat, `Handler` de
// @netlify/functions) hay que llamar a `connectLambda(event)` ANTES de
// `getStore`: el contexto viaja en `event.blobs`, que el tipo público de
// HandlerEvent no declara — de ahí el cast. Si el runtime ya lo inyectó por
// variable de entorno, la llamada no estorba; si falla, `getStore` lo intenta
// por su cuenta. En local no hay store y todo esto lanza: por eso el checkout
// trata un fallo de Blobs como error duro (sin pedido no se puede entregar) y
// el IPN sólo lo hace best-effort donde no compromete la entrega.
//
// ESCRITURA CONDICIONAL (verificado contra @netlify/blobs 10.7.13,
// `dist/main.d.ts`): `store.setJSON(key, value, { onlyIfNew: true })` y
// `{ onlyIfMatch: etag }` devuelven `{ modified: boolean, etag?: string }`.
// ⚠️ NO LANZAN cuando la condición no se cumple: devuelven `modified: false`.
// Quien llame TIENE que mirar `modified`; ignorarlo convierte el lock de
// entrega en un adorno y manda dos emails por el mismo pago.
// `getWithMetadata(key, { type: 'json' })` devuelve `{ data, etag, metadata }`
// o `null`, y es la única forma de obtener el etag para el `onlyIfMatch`.
// ════════════════════════════════════════════════════════════════════════════

import { createHash, randomBytes } from 'node:crypto';

export const CRYPTO_STORE = 'crypto-orders';

/** Estado del pedido en el libro. `created` = factura abierta, nadie ha pagado
 *  (o el comprador ni siquiera eligió moneda: entonces no hay `paymentId` y no
 *  hay nada que consultar a la API — spec :171). El resto son los 9 estados
 *  oficiales de NOWPayments tal cual llegan. */
export type OrderStatus = 'created' | string;

export interface CryptoOrder {
  orderId: string;
  productId: string;
  /** Email tal cual lo escribió el comprador (para depurar diferencias). */
  email: string;
  /** Minúsculas y sin espacios: es la clave del índice y la que recibe el email. */
  emailNorm: string;
  priceEur: number;
  currency: 'eur';
  /** País de facturación declarado en el diálogo (ISO-2 mayúsculas). */
  country: string;
  /** País de la cabecera geo de Netlify. Evidencia independiente del anterior. */
  geoCountry: string;
  acceptedPolicyAt: string;
  waivedWithdrawalAt: string;
  createdAt: string;
  status: OrderStatus;
  invoiceId?: string;
  invoiceUrl?: string;
  paymentId?: string;
  payCurrency?: string;
  payAmount?: number;
  actuallyPaid?: number;
  outcomeAmount?: number;
  outcomeCurrency?: string;
  lastIpnAt?: string;
  ipnCount: number;
  delivered: boolean;
  deliveredAt?: string;
  /** ISO del momento en que un IPN cogió el lock de entrega. Caduca a los 10 min. */
  deliveryLockAt?: string;
  /** Marcas para el informe: 'underpaid', 'amount_mismatch', 'foreign_payment'… */
  flags: string[];
}

/** Subconjunto de la API de Blobs que se usa aquí. Tipado a mano —igual que en
 *  log-search.ts y search-report.ts— para no depender de los tipos del paquete
 *  en tiempo de compilación de esbuild. Las firmas están copiadas del
 *  `dist/main.d.ts` de @netlify/blobs 10.7.13. */
export interface BlobStore {
  get: (key: string, opts: { type: 'json' }) => Promise<unknown>;
  getWithMetadata: (
    key: string,
    opts: { type: 'json' },
  ) => Promise<{ data: unknown; etag?: string; metadata?: Record<string, unknown> } | null>;
  setJSON: (
    key: string,
    value: unknown,
    opts?: { metadata?: Record<string, unknown>; onlyIfNew?: boolean; onlyIfMatch?: string },
  ) => Promise<{ modified: boolean; etag?: string }>;
  list: (opts: { prefix: string }) => Promise<{ blobs: { key: string; etag?: string }[] }>;
  delete: (key: string) => Promise<unknown>;
}

/** Consistencia con la que quedó abierto el libro en esta instancia (para logs). */
export let consistenciaLibro: 'strong' | 'eventual' | 'sin-abrir' = 'sin-abrir';

/** Abre el store, con consistencia FUERTE si el runtime la soporta. Lanza si
 *  Blobs no está disponible.
 *
 *  ⚠️ MEDIDO EN EL DEPLOY PREVIEW 78 (2026-09-06): en una function v1
 *  (Lambda-compat) el contexto que llega por `connectLambda(event)` NO trae la
 *  propiedad `uncachedEdgeURL`, y cualquier lectura con `consistency:'strong'`
 *  lanza `BlobsConsistencyError` («the environment has not been configured
 *  with a 'uncachedEdgeURL' property»). Por eso aquí se hace una LECTURA DE
 *  PRUEBA con consistencia fuerte y, si falla por eso, se reabre en eventual
 *  y se avisa en los logs. La idempotencia de la entrega NO depende de esto:
 *  las escrituras condicionales (`onlyIfMatch`/`onlyIfNew`) se validan en el
 *  origen, así que una lectura obsoleta a lo sumo cuesta un 500 y un reintento
 *  del IPN, nunca una doble entrega. */
export async function abrirLibro(event: unknown): Promise<BlobStore> {
  const blobs = await import('@netlify/blobs');
  const abrir = (consistency: 'strong' | 'eventual'): BlobStore =>
    blobs.getStore({ name: CRYPTO_STORE, consistency }) as unknown as BlobStore;

  // 1) Contexto de entorno completo (NETLIFY_BLOBS_CONTEXT): si existe, trae
  //    la URL sin caché y la consistencia fuerte funciona. `getStore` lanza
  //    MissingBlobsEnvironmentError si no hay contexto → pasamos al plan 2.
  let store: BlobStore | null = null;
  try {
    store = abrir('strong');
  } catch {
    store = null;
  }
  // 2) Contexto del evento (functions v1): puede venir sin `uncachedEdgeURL`.
  if (!store) {
    try {
      blobs.connectLambda(event as { blobs: string; headers: Record<string, string> });
    } catch {
      /* sin event.blobs: getStore volverá a lanzar y el error sube al llamador */
    }
    store = abrir('strong');
  }
  // 3) Lectura de prueba: la fuerte sólo falla en el momento de leer.
  try {
    await store.get('__probe__', { type: 'json' });
    consistenciaLibro = 'strong';
    return store;
  } catch (err) {
    const msg = String((err as Error)?.message || err);
    if (!/uncachedEdgeURL|BlobsConsistencyError|strong consistency/i.test(msg)) throw err;
    if (consistenciaLibro !== 'eventual') {
      console.warn('[crypto-orders] consistencia fuerte no disponible en este runtime; libro en consistencia EVENTUAL');
    }
    consistenciaLibro = 'eventual';
    return abrir('eventual');
  }
}

// ── Utilidades ──────────────────────────────────────────────────────────────

/** 32 hex. Opaco e imposible de adivinar: es el secreto que da acceso a la
 *  página de estado del pedido, igual que hoy el `session_id` de Stripe. */
export function newOrderId(): string {
  return randomBytes(16).toString('hex');
}

export function esOrderId(v: unknown): v is string {
  return typeof v === 'string' && /^[0-9a-f]{32}$/.test(v);
}

export function sha256(s: string): string {
  return createHash('sha256').update(s, 'utf8').digest('hex');
}

/** `juan.perez@gmail.com` → `j********z@gmail.com`. Ni los logs ni la página de
 *  estado (que es pública si alguien tiene el orderId) devuelven el email
 *  completo: sirve para que el comprador reconozca el suyo, no para leerlo. */
export function maskEmail(email: string): string {
  const e = String(email || '').trim();
  const at = e.lastIndexOf('@');
  if (at <= 0) return e ? '***' : '';
  const local = e.slice(0, at);
  const dominio = e.slice(at);
  if (local.length <= 2) return `${local.slice(0, 1)}***${dominio}`;
  return `${local[0]}${'*'.repeat(Math.min(8, local.length - 2))}${local[local.length - 1]}${dominio}`;
}

/** Claves de Blobs sin caracteres raros: los ids de NOWPayments son numéricos,
 *  pero un valor inesperado en el IPN no debe poder inventarse una ruta. */
export function claveSegura(s: unknown): string {
  return String(s ?? '')
    .replace(/[^A-Za-z0-9_-]/g, '-')
    .slice(0, 80) || 'sin-id';
}

export const claveOrden = (orderId: string) => `orders/${orderId}`;
export const dia = (iso: string) => iso.slice(0, 10);

// ── Pedidos ─────────────────────────────────────────────────────────────────

/** Alta del pedido. `onlyIfNew` para que una colisión de orderId (imposible en
 *  la práctica con 128 bits, pero gratis de descartar) no pise un pedido vivo. */
export async function createOrder(store: BlobStore, order: CryptoOrder): Promise<void> {
  const res = await store.setJSON(claveOrden(order.orderId), order, { onlyIfNew: true });
  if (!res || res.modified === false) {
    throw new Error(`crypto-orders: el pedido ${order.orderId} ya existía`);
  }
}

export async function getOrderWithEtag(
  store: BlobStore,
  orderId: string,
): Promise<{ order: CryptoOrder; etag?: string } | null> {
  const res = await store.getWithMetadata(claveOrden(orderId), { type: 'json' });
  if (!res || !res.data || typeof res.data !== 'object') return null;
  return { order: res.data as CryptoOrder, etag: res.etag };
}

/** Escritura condicional. Devuelve el etag NUEVO si se aplicó, o `null` si otro
 *  proceso escribió entre medias (hay que releer y decidir). Sin etag se
 *  escribe incondicionalmente: sólo para pedidos recién creados en la misma
 *  petición, nunca en la ruta de entrega. */
export async function updateOrder(
  store: BlobStore,
  order: CryptoOrder,
  etag?: string,
): Promise<string | null> {
  const opts = etag ? { onlyIfMatch: etag } : undefined;
  const res = await store.setJSON(claveOrden(order.orderId), order, opts);
  if (!res || res.modified === false) return null;
  return res.etag ?? '';
}

/** Índices por email (autorrecuperación en resend-access) y por día (informe).
 *  Se guarda una copia mínima —no el pedido entero— para que el informe pueda
 *  listar sin leer 46 blobs y para que un cambio de estado no obligue a
 *  reescribir los índices. El email va HASHEADO en la clave: un listado del
 *  store no debe ser un volcado de direcciones. */
export async function indexOrder(store: BlobStore, order: CryptoOrder): Promise<void> {
  const ref = { orderId: order.orderId, productId: order.productId, createdAt: order.createdAt };
  await Promise.all([
    store.setJSON(`email/${sha256(order.emailNorm)}/${order.orderId}`, ref),
    store.setJSON(`day/${dia(order.createdAt)}/${order.orderId}`, ref),
  ]);
}

async function leerPedidos(store: BlobStore, claves: string[]): Promise<CryptoOrder[]> {
  const CONCURRENCIA = 25;
  const out: CryptoOrder[] = [];
  for (let i = 0; i < claves.length; i += CONCURRENCIA) {
    const tanda = claves.slice(i, i + CONCURRENCIA);
    const res = await Promise.all(
      tanda.map(async (k) => {
        try {
          return (await store.get(k, { type: 'json' })) as CryptoOrder | null;
        } catch (err) {
          console.error('[crypto-orders] pedido ilegible', k, err);
          return null;
        }
      }),
    );
    for (const o of res) if (o && typeof o === 'object' && o.orderId) out.push(o);
  }
  return out;
}

/** Pedidos de un email, del más reciente al más antiguo. */
export async function listOrdersByEmail(store: BlobStore, emailNorm: string): Promise<CryptoOrder[]> {
  let res: { blobs: { key: string }[] };
  try {
    res = await store.list({ prefix: `email/${sha256(emailNorm)}/` });
  } catch (err) {
    console.error('[crypto-orders] no se pudo listar el índice por email:', err);
    return [];
  }
  const ids = res.blobs.map((b) => b.key.slice(b.key.lastIndexOf('/') + 1)).filter(esOrderId);
  const pedidos = await leerPedidos(store, ids.map(claveOrden));
  return pedidos.sort((a, b) => String(b.createdAt || '').localeCompare(String(a.createdAt || '')));
}

/** Pedidos de los últimos N días (UTC), del más reciente al más antiguo.
 *  Los `list()` por día van en paralelo: en serie serían N round-trips ANTES de
 *  leer un solo pedido (la lección de search-report.ts:35). */
export async function listOrdersByDays(store: BlobStore, days: number): Promise<CryptoOrder[]> {
  const DIAS_EN_PARALELO = 10;
  const hoy = Date.now();
  const listaDias: string[] = [];
  for (let i = 0; i < days; i++) listaDias.push(new Date(hoy - i * 86400000).toISOString().slice(0, 10));

  const ids: string[] = [];
  for (let i = 0; i < listaDias.length; i += DIAS_EN_PARALELO) {
    const tanda = listaDias.slice(i, i + DIAS_EN_PARALELO);
    const res = await Promise.all(
      tanda.map(async (d) => {
        try {
          const r = await store.list({ prefix: `day/${d}/` });
          return r.blobs.map((b) => b.key.slice(b.key.lastIndexOf('/') + 1));
        } catch (err) {
          console.error('[crypto-orders] fallo al listar el día', d, err);
          return [] as string[];
        }
      }),
    );
    for (const grupo of res) for (const id of grupo) if (esOrderId(id)) ids.push(id);
  }

  const pedidos = await leerPedidos(store, ids.map(claveOrden));
  return pedidos.sort((a, b) => String(b.createdAt || '').localeCompare(String(a.createdAt || '')));
}

/** Borra un pedido y sus dos índices. Sólo lo usa la purga de `crypto-report`. */
export async function deleteOrder(store: BlobStore, order: CryptoOrder): Promise<void> {
  await Promise.all([
    store.delete(claveOrden(order.orderId)),
    store.delete(`email/${sha256(order.emailNorm)}/${order.orderId}`),
    store.delete(`day/${dia(order.createdAt)}/${order.orderId}`),
  ]);
}

// ── IPN crudos y huérfanos ──────────────────────────────────────────────────

/** Guarda el IPN tal cual llegó (cuerpo + cabeceras), ≥ 30 días (spec :190).
 *  Es la única evidencia si hay que discutir un pago con NOWPayments o
 *  reconstruir una entrega a mano. NUNCA rompe el flujo: si Blobs falla, el
 *  pago se sigue procesando y el fallo queda en los logs. */
export async function saveRawIpn(
  store: BlobStore,
  payload: Record<string, unknown>,
  headers: Record<string, unknown>,
  raw: string,
  prefijo: 'ipn' | 'ipn-rechazados' = 'ipn',
): Promise<void> {
  const ts = new Date().toISOString();
  const clave = `${prefijo}/${dia(ts)}/${claveSegura(payload.payment_id)}-${claveSegura(payload.payment_status)}-${ts.replace(/[:.]/g, '-')}`;
  try {
    await store.setJSON(clave, { ts, raw, payload, headers });
  } catch (err) {
    console.error('[crypto-orders] no se pudo guardar el IPN crudo:', err);
  }
}

/** Pago que no cuadra con ningún pedido servible: sin pedido, infrapagado o
 *  segundo pago de una factura ya entregada. John lo resuelve a mano desde el
 *  panel. Se sobrescribe por `paymentId` a propósito: interesa el último
 *  estado de ese pago, no su historial (que ya está en `ipn/`). */
export async function saveOrphan(
  store: BlobStore,
  paymentId: unknown,
  motivo: string,
  datos: Record<string, unknown>,
): Promise<void> {
  try {
    await store.setJSON(`orphans/${claveSegura(paymentId)}`, {
      ts: new Date().toISOString(),
      motivo,
      ...datos,
    });
  } catch (err) {
    console.error('[crypto-orders] no se pudo guardar el huérfano:', err);
  }
}

// ── Cupo por minuto (patrón log-search.ts:154) ──────────────────────────────

/** Devuelve true si hay que rechazar con 429. Contador aproximado en
 *  `rl/<YYYY-MM-DDTHH:mm>`: dos peticiones simultáneas pueden leer el mismo
 *  valor y colarse una de más, que para una guarda de coste da igual.
 *  FAIL-OPEN si Blobs falla — pero ojo, aquí eso sólo afecta al contador: si
 *  Blobs está caído, el checkout falla igualmente al crear el pedido. */
export async function rateLimitExceeded(store: BlobStore, maxPerMinute: number): Promise<boolean> {
  const clave = `rl/${new Date().toISOString().slice(0, 16)}`;
  try {
    const actual = (await store.get(clave, { type: 'json' })) as { n?: number } | null;
    const n = actual && typeof actual.n === 'number' ? actual.n : 0;
    if (n >= maxPerMinute) return true;
    await store.setJSON(clave, { n: n + 1 });
  } catch (err) {
    console.error('[crypto-orders] cupo no verificable (se deja pasar):', err);
  }
  return false;
}
