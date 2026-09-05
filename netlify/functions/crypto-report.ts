import type { Handler } from '@netlify/functions';
import {
  abrirLibro,
  claveOrden,
  dia,
  deleteOrder,
  esOrderId,
  listOrdersByDays,
  maskEmail,
  type BlobStore,
  type CryptoOrder,
} from '../shared/crypto-orders';

// ════════════════════════════════════════════════════════════════════════════
// crypto-report — informe de los pedidos cripto para John (2026-09-05).
//
// AUTENTICACIÓN FUERTE, la de `search-report.ts` y NO la de
// `admin-generate-access.ts` (spec PAGOS_CRYPTO_NOWPAYMENTS.md:175): cabecera
// `x-admin-password`, comparación de tiempo constante sobre digests SHA-256, y
// cupo de intentos por minuto. El endpoint es público y sin límite por IP, así
// que un `!==` —que corta en el primer byte distinto— es un canal medible con
// suficientes peticiones. Se reutiliza el ADMIN_PASSWORD que ya existe: no se
// crea variable nueva.
//
//   GET /.netlify/functions/crypto-report?days=30
//   GET /.netlify/functions/crypto-report?days=7&format=csv
//   GET /.netlify/functions/crypto-report?days=30&full=1        (email completo)
//   GET /.netlify/functions/crypto-report?purge_unpaid_before=2026-08-01  (BORRA)
//
// EL EMAIL VA ENMASCARADO SALVO `full=1`. El informe se lee a diario y se pega
// en handoffs; el dato personal completo sólo cuando de verdad hace falta para
// atender a un cliente.
//
// PURGA: los pedidos ABANDONADOS son la mayoría (alguien pulsa el botón, ve el
// importe en BTC y se va). Sin purga el store crece con emails que no
// compraron nada. Sólo se borran los que no llegaron a pago: `created`,
// `expired` o `failed`, SIN `paymentId` y sin entregar. Un pedido con pago
// —aunque fallara— es contabilidad y no se toca nunca desde aquí.
//
// GOTCHA DE BLOBS: sólo funciona DESPLEGADO. Function v1 → `connectLambda`
// antes de `getStore` (lo hace `abrirLibro`).
//
// CÓMO VERIFICAR EN PRODUCCIÓN (tras el deploy):
//   curl -s -o /dev/null -w '%{http_code}\n' \
//     https://aichef.pro/.netlify/functions/crypto-report              # 401
//   curl -s -H "x-admin-password: $ADMIN_PASSWORD" \
//     'https://aichef.pro/.netlify/functions/crypto-report?days=7'
// ════════════════════════════════════════════════════════════════════════════

const MAX_DIAS = 400;
const MAX_INTENTOS_MINUTO = 5;
const CONCURRENCIA = 25;

/** Estados que se consideran «nunca llegó a pagarse». */
const PURGABLES = new Set(['created', 'expired', 'failed']);

/** Compara en tiempo constante y sin filtrar la longitud (digests de 32 bytes). */
async function claveCorrecta(dada: string, esperada: string): Promise<boolean> {
  try {
    const { createHash, timingSafeEqual } = await import('node:crypto');
    const h = (s: string) => createHash('sha256').update(s, 'utf8').digest();
    return timingSafeEqual(h(dada), h(esperada));
  } catch {
    // Si node:crypto no estuviera disponible, NO se degrada a `===`: se deniega.
    return false;
  }
}

/** Cupo de intentos de autenticación por minuto. Fail-open si Blobs falla.
 *  Prefijo `rl/report-` para no chocar con el contador del checkout (`rl/<min>`). */
async function excedeIntentos(store: BlobStore | null, minuto: string): Promise<boolean> {
  if (!store) return false;
  const clave = `rl/report-${minuto}`;
  try {
    const actual = (await store.get(clave, { type: 'json' })) as { n?: number } | null;
    const n = actual && typeof actual.n === 'number' ? actual.n : 0;
    if (n >= MAX_INTENTOS_MINUTO) return true;
    await store.setJSON(clave, { n: n + 1 });
  } catch (err) {
    console.error('[crypto-report] cupo de intentos no verificable:', err);
  }
  return false;
}

/** Escape de CSV: comillas dobladas y celda entrecomillada si lleva separador,
 *  comillas o salto de línea. Sin esto, un `order_description` con una coma
 *  desplaza todas las columnas de esa fila. */
function csv(valor: unknown): string {
  const s = valor === null || valor === undefined ? '' : String(valor);
  return /[",\r\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
}

export const handler: Handler = async (event) => {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type, x-admin-password',
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers, body: '' };
  }
  if (event.httpMethod !== 'GET') {
    return { statusCode: 405, headers, body: JSON.stringify({ error: 'method_not_allowed' }) };
  }

  try {
    if (!process.env.ADMIN_PASSWORD) {
      return { statusCode: 500, headers, body: JSON.stringify({ error: 'ADMIN_PASSWORD not configured' }) };
    }

    // El store se abre ANTES de autenticar: hace falta para contar los intentos.
    let store: BlobStore | null = null;
    try {
      store = await abrirLibro(event);
    } catch (err) {
      console.error('[crypto-report] no se pudo abrir el libro:', err);
    }

    const minuto = new Date().toISOString().slice(0, 16);
    if (await excedeIntentos(store, minuto)) {
      return { statusCode: 429, headers, body: JSON.stringify({ error: 'rate_limited' }) };
    }

    // ── Auth ────────────────────────────────────────────────────────────────
    const cabeceras: Record<string, string> = {};
    for (const [k, v] of Object.entries(event.headers || {})) {
      if (typeof v === 'string') cabeceras[k.toLowerCase()] = v;
    }
    const pass = cabeceras['x-admin-password'] || '';
    if (!pass || !(await claveCorrecta(pass, process.env.ADMIN_PASSWORD))) {
      return { statusCode: 401, headers, body: JSON.stringify({ error: 'Unauthorized' }) };
    }

    if (!store) {
      return { statusCode: 500, headers, body: JSON.stringify({ error: 'blobs_unavailable' }) };
    }

    const qs = event.queryStringParameters || {};

    // ── Purga ───────────────────────────────────────────────────────────────
    const before = String(qs.purge_unpaid_before || '').trim();
    if (before) {
      if (!/^\d{4}-\d{2}-\d{2}$/.test(before)) {
        return { statusCode: 400, headers, body: JSON.stringify({ error: 'purge_unpaid_before_YYYY-MM-DD' }) };
      }
      const hoy = new Date().toISOString().slice(0, 10);
      if (before >= hoy) {
        return { statusCode: 400, headers, body: JSON.stringify({ error: 'before_debe_ser_anterior_a_hoy' }) };
      }

      // Se recorre el índice por día (una clave por pedido) en vez de `orders/`:
      // la fecha va en la propia clave, así que se descarta lo reciente sin
      // leer un solo pedido.
      let listado: { blobs: { key: string }[] };
      try {
        listado = await store.list({ prefix: 'day/' });
      } catch (err) {
        console.error('[crypto-report] fallo al listar para la purga:', err);
        return { statusCode: 500, headers, body: JSON.stringify({ error: 'list_failed' }) };
      }
      const candidatos = listado.blobs
        .map((b) => b.key)
        .filter((k) => {
          const partes = k.split('/'); // day/<YYYY-MM-DD>/<orderId>
          return (
            partes.length === 3 &&
            /^\d{4}-\d{2}-\d{2}$/.test(partes[1]) &&
            partes[1] < before &&
            esOrderId(partes[2])
          );
        })
        .map((k) => k.split('/')[2]);

      let borrados = 0;
      let conservados = 0;
      for (let i = 0; i < candidatos.length; i += CONCURRENCIA) {
        const tanda = candidatos.slice(i, i + CONCURRENCIA);
        const res = await Promise.all(
          tanda.map(async (id) => {
            try {
              const o = (await store!.get(claveOrden(id), { type: 'json' })) as CryptoOrder | null;
              if (!o || !o.orderId) return 'sin_pedido';
              // Sólo lo que nunca llegó a pago. Un pedido con paymentId es
              // contabilidad, aunque su estado sea `failed`.
              if (o.delivered || o.paymentId || !PURGABLES.has(o.status)) return 'conservado';
              await deleteOrder(store!, o);
              return 'borrado';
            } catch (err) {
              console.error('[crypto-report] no se pudo purgar', id, err);
              return 'error';
            }
          }),
        );
        for (const r of res) {
          if (r === 'borrado') borrados += 1;
          else if (r === 'conservado') conservados += 1;
        }
      }
      console.log(`[crypto-report] purga anterior a ${before}: ${borrados} borrados, ${conservados} conservados`);
      return {
        statusCode: 200,
        headers,
        body: JSON.stringify({ ok: true, purgado: true, before, borrados, conservados, examinados: candidatos.length }),
      };
    }

    // ── Informe ─────────────────────────────────────────────────────────────
    let days = parseInt(String(qs.days || '30'), 10);
    if (!Number.isFinite(days)) days = 30;
    days = Math.min(MAX_DIAS, Math.max(1, days));
    const full = qs.full === '1' || qs.full === 'true';

    const pedidos = await listOrdersByDays(store, days);
    const email = (o: CryptoOrder) => (full ? o.emailNorm : maskEmail(o.emailNorm));

    if (qs.format === 'csv') {
      const filas = [
        [
          'fecha',
          'orderId',
          'productId',
          'importe_eur',
          'pais',
          'geo_pais',
          'estado',
          'entregado',
          'payment_id',
          'moneda_pagada',
          'pagado',
          'outcome',
          'email',
        ].join(','),
        ...pedidos.map((o) =>
          [
            o.createdAt,
            o.orderId,
            o.productId,
            o.priceEur,
            o.country || '',
            o.geoCountry || '',
            o.status,
            o.delivered ? 'si' : 'no',
            o.paymentId || '',
            o.payCurrency || '',
            o.actuallyPaid ?? '',
            o.outcomeAmount ?? '',
            email(o),
          ]
            .map(csv)
            .join(','),
        ),
      ];
      return {
        statusCode: 200,
        headers: {
          ...headers,
          'Content-Type': 'text/csv; charset=utf-8',
          'Content-Disposition': `attachment; filename="crypto-pedidos-${days}d.csv"`,
        },
        body: `${filas.join('\n')}\n`,
      };
    }

    const porEstado: Record<string, number> = {};
    const porProducto: Record<string, number> = {};
    const porPais: Record<string, number> = {};
    let entregados = 0;
    let ingresosEur = 0;
    const conBanderas: unknown[] = [];
    for (const o of pedidos) {
      porEstado[o.status] = (porEstado[o.status] || 0) + 1;
      if (o.delivered) {
        entregados += 1;
        porProducto[o.productId] = (porProducto[o.productId] || 0) + 1;
        ingresosEur += typeof o.priceEur === 'number' ? o.priceEur : 0;
      }
      const p = o.country || o.geoCountry || '';
      if (p) porPais[p] = (porPais[p] || 0) + 1;
      if (Array.isArray(o.flags) && o.flags.length) {
        conBanderas.push({ orderId: o.orderId, productId: o.productId, flags: o.flags, status: o.status });
      }
    }

    const hoy = new Date();
    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({
        ok: true,
        days,
        desde: new Date(hoy.getTime() - (days - 1) * 86400000).toISOString().slice(0, 10),
        hasta: dia(hoy.toISOString()),
        total: pedidos.length,
        entregados,
        ingresos_eur: Math.round(ingresosEur * 100) / 100,
        por_estado: porEstado,
        por_producto: porProducto,
        por_pais: porPais,
        // Pedidos con alguna marca (infrapago, importe que no cuadra, segundo
        // pago de la misma factura): es la lista que John tiene que mirar.
        con_banderas: conBanderas,
        pedidos: pedidos.map((o) => ({
          orderId: o.orderId,
          createdAt: o.createdAt,
          productId: o.productId,
          priceEur: o.priceEur,
          country: o.country || '',
          geoCountry: o.geoCountry || '',
          status: o.status,
          delivered: Boolean(o.delivered),
          deliveredAt: o.deliveredAt || '',
          paymentId: o.paymentId || '',
          payCurrency: o.payCurrency || '',
          actuallyPaid: o.actuallyPaid ?? null,
          outcomeAmount: o.outcomeAmount ?? null,
          outcomeCurrency: o.outcomeCurrency || '',
          invoiceId: o.invoiceId || '',
          lastIpnAt: o.lastIpnAt || '',
          ipnCount: o.ipnCount || 0,
          flags: o.flags || [],
          email: email(o),
        })),
      }),
    };
  } catch (err) {
    console.error('[crypto-report] error:', err);
    return { statusCode: 500, headers, body: JSON.stringify({ error: 'server_error' }) };
  }
};
