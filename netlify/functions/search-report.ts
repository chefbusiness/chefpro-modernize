import type { Handler } from '@netlify/functions';

// ════════════════════════════════════════════════════════════════════════════
// search-report — informe de las búsquedas registradas por log-search.
//
// GET, protegido por la cabecera `x-admin-password` (mismo ADMIN_PASSWORD que
// usa netlify/functions/admin-generate-access.ts — NO se crea env var nueva).
// La comparación es de tiempo constante sobre digests SHA-256: el endpoint es
// público y sin intentos limitados por IP, así que un `!==` (que corta en el
// primer byte distinto) es un canal medible con suficientes peticiones.
//
//   GET /.netlify/functions/search-report?days=30
//   GET /.netlify/functions/search-report?days=7&raw=1          (entradas crudas)
//   GET /.netlify/functions/search-report?purge=1&before=2026-06-01   (BORRA)
//
// Devuelve JSON con:
//   total, por_dia, top_queries (q_norm, veces, media de resultados, tag,
//   países), sin_resultados (+ detalles y emails), por_pais.
// `raw=1` devuelve las entradas tal cual, de la más reciente a la más antigua.
//
// El consumidor pensado es scripts/productos-digitales/buscador-report.py, que
// además cruza cada consulta contra el catálogo del hub y contra la cola de
// productos nuevos del CALENDARIO-V2-SEMANAL.md. Documentación:
// scripts/productos-digitales/BUSCADOR-HUB.md.
//
// TECHOS Y POR QUÉ SON ESTOS (una function síncrona de Netlify tiene 10 s por
// defecto y 6 MB de respuesta):
//   · MAX_ENTRADAS 3.000 — 20.000 lecturas ni siquiera caben en el tiempo.
//   · MAX_RAW 1.500 — a ~1,3 KB por entrada (los topes de log-search), 5.000
//     daban 6,11 MB y la respuesta se cortaba con un error de plataforma en
//     vez de con un JSON.
//   · MAX_FILAS 500 por tabla — la agregación emitía una fila por consulta
//     distinta, sin tope: crecía con el corpus hasta reventar el mismo límite.
//   · Los `list()` por día van en PARALELO (antes eran 365 round-trips en
//     serie ANTES de leer un solo blob) y las lecturas de 50 en 50.
// Cuando algo se recorta, la respuesta lo dice: `truncado`, `*_total`.
//
// GOTCHA DE BLOBS: solo funciona DESPLEGADO en Netlify (en local no hay store).
// Function v1 (Lambda-compat) → `connectLambda(event)` antes de `getStore`.
//
// CÓMO VERIFICAR EN PRODUCCIÓN (tras el deploy):
//   curl -s -o /dev/null -w '%{http_code}\n' \
//     https://aichef.pro/.netlify/functions/search-report            # 401
//   curl -s -H "x-admin-password: $ADMIN_PASSWORD" \
//     'https://aichef.pro/.netlify/functions/search-report?days=1'   # JSON
// ════════════════════════════════════════════════════════════════════════════

const STORE = 'search-queries';
const MAX_RAW = 1500; // techo de entradas crudas que se devuelven con raw=1
const MAX_ENTRADAS = 3000; // techo de lectura para la agregación
const CONCURRENCIA = 50; // blobs leídos en paralelo
const DIAS_EN_PARALELO = 10; // list() simultáneos (son independientes entre sí)
const MAX_FILAS = 500; // filas por tabla agregada
const MAX_INTENTOS_MINUTO = 5; // intentos de autenticación por minuto

interface Entrada {
  q?: string;
  q_norm?: string;
  n?: number;
  n_filtrado?: number;
  coming?: number;
  tag?: string;
  lang?: string;
  path?: string;
  sin_resultados?: boolean;
  detalle?: string;
  email?: string;
  origen?: string;
  country?: string;
  ts?: string;
}

interface Agregado {
  veces: number;
  eventos: number;
  suma_n: number;
  paises: Record<string, number>;
  tags: Record<string, number>;
  detalles: string[];
  emails: string[];
  ejemplo: string;
}

type Store = {
  get: (key: string, opts: { type: 'json' }) => Promise<unknown>;
  setJSON: (key: string, value: unknown) => Promise<unknown>;
  list: (opts: { prefix: string }) => Promise<{ blobs: { key: string }[] }>;
  delete: (key: string) => Promise<unknown>;
};

/** Días en formato YYYY-MM-DD (UTC), del más reciente al más antiguo. */
function dias(n: number): string[] {
  const out: string[] = [];
  const hoy = Date.now();
  for (let i = 0; i < n; i++) {
    out.push(new Date(hoy - i * 86400000).toISOString().slice(0, 10));
  }
  return out;
}

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

/** Cupo de intentos de autenticación por minuto. Fail-open si Blobs falla. */
async function excedeIntentos(store: Store | null, minuto: string): Promise<boolean> {
  if (!store) return false;
  const clave = `rl/report-${minuto}`;
  try {
    const actual = (await store.get(clave, { type: 'json' })) as { n?: number } | null;
    const n = actual && typeof actual.n === 'number' ? actual.n : 0;
    if (n >= MAX_INTENTOS_MINUTO) return true;
    await store.setJSON(clave, { n: n + 1 });
  } catch (err) {
    console.error('search-report: cupo de intentos no verificable:', err);
  }
  return false;
}

/** Lee las claves en tandas para no abrir miles de conexiones a la vez. */
async function leerTodas(store: Store, claves: string[]): Promise<Entrada[]> {
  const out: Entrada[] = [];
  for (let i = 0; i < claves.length; i += CONCURRENCIA) {
    const tanda = claves.slice(i, i + CONCURRENCIA);
    const res = await Promise.all(
      tanda.map(async (k) => {
        try {
          return (await store.get(k, { type: 'json' })) as Entrada | null;
        } catch (err) {
          console.error('search-report: blob ilegible', k, err);
          return null;
        }
      }),
    );
    for (const e of res) {
      if (e && typeof e === 'object') out.push(e);
    }
  }
  return out;
}

/** Lista los blobs de varios días EN PARALELO (tandas de DIAS_EN_PARALELO). */
async function listarDias(store: Store, listaDias: string[]): Promise<Record<string, string[]>> {
  const out: Record<string, string[]> = {};
  for (let i = 0; i < listaDias.length; i += DIAS_EN_PARALELO) {
    const tanda = listaDias.slice(i, i + DIAS_EN_PARALELO);
    const res = await Promise.all(
      tanda.map(async (dia) => {
        try {
          const r = await store.list({ prefix: `${dia}/` });
          return { dia, claves: r.blobs.map((b) => b.key) };
        } catch (err) {
          console.error('search-report: fallo al listar', dia, err);
          return { dia, claves: [] as string[] };
        }
      }),
    );
    for (const r of res) out[r.dia] = r.claves;
  }
  return out;
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
    return { statusCode: 405, headers, body: JSON.stringify({ error: 'Method not allowed' }) };
  }

  try {
    if (!process.env.ADMIN_PASSWORD) {
      return { statusCode: 500, headers, body: JSON.stringify({ error: 'ADMIN_PASSWORD not configured' }) };
    }

    // El store se abre ANTES de autenticar: hace falta para contar los intentos.
    let store: Store | null = null;
    try {
      const { connectLambda, getStore } = await import('@netlify/blobs');
      try {
        connectLambda(event as unknown as { blobs: string; headers: Record<string, string> });
      } catch {
        /* runtime sin event.blobs: getStore lo intentará por env var */
      }
      store = getStore(STORE) as unknown as Store;
    } catch (err) {
      console.error('search-report: no se pudo abrir el store:', err);
    }

    const minuto = new Date().toISOString().slice(0, 16);
    if (await excedeIntentos(store, minuto)) {
      return { statusCode: 429, headers, body: JSON.stringify({ error: 'rate_limited' }) };
    }

    // ── Auth ──────────────────────────────────────────────────────────────
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

    // ── Parámetros ────────────────────────────────────────────────────────
    const qs = event.queryStringParameters || {};
    let days = parseInt(qs.days || '30', 10);
    if (!Number.isFinite(days)) days = 30;
    days = Math.min(365, Math.max(1, days));
    const raw = qs.raw === '1' || qs.raw === 'true';

    // ── Purga (retención) ─────────────────────────────────────────────────
    // Los eventos no caducan solos: sin esto el store crece sin techo y los
    // emails de contacto se guardan indefinidamente. Borra días COMPLETOS
    // anteriores a `before` (y los contadores del cupo de esos días).
    if (qs.purge === '1' || qs.purge === 'true') {
      const before = (qs.before || '').trim();
      if (!/^\d{4}-\d{2}-\d{2}$/.test(before)) {
        return { statusCode: 400, headers, body: JSON.stringify({ error: 'before_requerido_YYYY-MM-DD' }) };
      }
      const hoy = new Date().toISOString().slice(0, 10);
      if (before >= hoy) {
        return { statusCode: 400, headers, body: JSON.stringify({ error: 'before_debe_ser_anterior_a_hoy' }) };
      }
      let borrados = 0;
      for (const prefijo of ['', 'rl/']) {
        let res: { blobs: { key: string }[] };
        try {
          res = await store.list({ prefix: prefijo });
        } catch (err) {
          console.error('search-report: fallo al listar para purga', prefijo, err);
          continue;
        }
        const viejas = res.blobs
          .map((b) => b.key)
          .filter((k) => {
            const dia = k.startsWith('rl/') ? k.slice(3, 13) : k.slice(0, 10);
            return /^\d{4}-\d{2}-\d{2}$/.test(dia) && dia < before;
          });
        for (let i = 0; i < viejas.length; i += CONCURRENCIA) {
          const tanda = viejas.slice(i, i + CONCURRENCIA);
          await Promise.all(
            tanda.map(async (k) => {
              try {
                await store!.delete(k);
                borrados += 1;
              } catch (err) {
                console.error('search-report: no se pudo borrar', k, err);
              }
            }),
          );
        }
      }
      return { statusCode: 200, headers, body: JSON.stringify({ ok: true, purgado: true, before, borrados }) };
    }

    // ── Lectura ───────────────────────────────────────────────────────────
    const listaDias = dias(days);
    const porDiaClaves = await listarDias(store, listaDias);

    const claves: string[] = [];
    const porDia: Record<string, number> = {};
    let truncado = false;
    for (const dia of listaDias) {
      const delDia = porDiaClaves[dia] || [];
      // Se anota lo REALMENTE encolado, no lo listado: si la truncación parte
      // este día, `por_dia` declararía eventos que nadie ha leído y la suma no
      // cuadraría con `total` sin más aviso que el flag.
      let anadidos = 0;
      for (const k of delDia) {
        if (claves.length >= MAX_ENTRADAS) {
          truncado = true;
          break;
        }
        claves.push(k);
        anadidos += 1;
      }
      porDia[dia] = anadidos;
      if (truncado) break;
    }

    const entradas = await leerTodas(store, claves);
    // Más reciente primero (la clave empieza por el día y el timestamp).
    entradas.sort((a, b) => String(b.ts || '').localeCompare(String(a.ts || '')));

    if (raw) {
      return {
        statusCode: 200,
        headers,
        body: JSON.stringify({
          ok: true,
          days,
          desde: listaDias[listaDias.length - 1],
          hasta: listaDias[0],
          total: entradas.length,
          truncado: truncado || entradas.length > MAX_RAW,
          entradas: entradas.slice(0, MAX_RAW),
        }),
      };
    }

    // ── Agregación ────────────────────────────────────────────────────────
    const porConsulta = new Map<string, Agregado>();
    const sinResultados = new Map<string, Agregado>();
    const porPais: Record<string, number> = {};

    const acumula = (mapa: Map<string, Agregado>, clave: string, e: Entrada, contar: boolean) => {
      let a = mapa.get(clave);
      if (!a) {
        a = { veces: 0, eventos: 0, suma_n: 0, paises: {}, tags: {}, detalles: [], emails: [], ejemplo: e.q || clave };
        mapa.set(clave, a);
      }
      a.eventos += 1;
      if (contar) {
        a.veces += 1;
        a.suma_n += typeof e.n === 'number' && Number.isFinite(e.n) ? e.n : 0;
        const c = e.country || '';
        if (c) a.paises[c] = (a.paises[c] || 0) + 1;
        const t = e.tag || '';
        if (t) a.tags[t] = (a.tags[t] || 0) + 1;
      }
      if (e.detalle && !a.detalles.includes(e.detalle)) a.detalles.push(e.detalle);
      if (e.email && !a.emails.includes(e.email)) a.emails.push(e.email);
    };

    for (const e of entradas) {
      const clave = (e.q_norm || e.q || '').trim();
      if (!clave) continue;
      // El evento del formulario «Dinos qué buscabas» repite una `q` que ya se
      // registró automáticamente 1,2 s antes: contarlo sumaría dos veces la
      // misma búsqueda. Aporta el detalle y el email, y eso sí se guarda.
      const contar = e.origen !== 'form';
      acumula(porConsulta, clave, e, contar);
      if (e.sin_resultados) acumula(sinResultados, clave, e, contar);
      if (contar) {
        const c = e.country || '';
        if (c) porPais[c] = (porPais[c] || 0) + 1;
      }
    }

    // Los detalles y los emails solo se devuelven en `sin_resultados`: son la
    // señal de demanda no cubierta (lo que el visitante buscaba y no existe).
    const aFila = (clave: string, a: Agregado, conContacto: boolean) => {
      const media = a.veces ? a.suma_n / a.veces : 0;
      return {
        q_norm: clave,
        ejemplo: a.ejemplo,
        veces: a.veces,
        eventos: a.eventos,
        media_resultados: Number.isFinite(media) ? Math.round(media * 100) / 100 : 0,
        paises: a.paises,
        tags: a.tags,
        ...(conContacto ? { detalles: a.detalles.slice(0, 20), emails: a.emails.slice(0, 20) } : {}),
      };
    };

    const ordena = (mapa: Map<string, Agregado>, conContacto: boolean) =>
      [...mapa.entries()]
        .map(([k, v]) => aFila(k, v, conContacto))
        .sort((x, y) => y.veces - x.veces || x.q_norm.localeCompare(y.q_norm))
        .slice(0, MAX_FILAS);

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({
        ok: true,
        days,
        desde: listaDias[listaDias.length - 1],
        hasta: listaDias[0],
        total: entradas.length,
        truncado,
        por_dia: porDia,
        top_queries: ordena(porConsulta, false),
        top_queries_total: porConsulta.size,
        sin_resultados: ordena(sinResultados, true),
        sin_resultados_total: sinResultados.size,
        por_pais: porPais,
      }),
    };
  } catch (err) {
    console.error('search-report error:', err);
    return { statusCode: 500, headers, body: JSON.stringify({ error: 'Server error' }) };
  }
};
