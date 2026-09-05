import type { Handler } from '@netlify/functions';

// ════════════════════════════════════════════════════════════════════════════
// log-search — registro de las búsquedas del buscador del hub de productos
// digitales (/productos-digitales). Endpoint PÚBLICO y sin auth: lo llama el
// navegador de cualquier visitante anónimo.
//
// QUÉ GUARDA (store de Netlify Blobs `search-queries`, un blob por evento):
//   { q, q_norm, n, n_filtrado, coming, tag, lang, path, sin_resultados,
//     detalle, email, origen, country, ts }
// QUÉ NO GUARDA, NUNCA: ni IP ni user-agent ni ninguna cabecera identificativa.
// Del visitante solo se conserva el código de país (cabecera de geo de Netlify)
// y, si él mismo lo escribe en el formulario de «no encuentro lo que busco»,
// su email. Ver scripts/productos-digitales/BUSCADOR-HUB.md.
//
// `n` ES EL CONTEO SIN EL CHIP DE CATEGORÍA, a propósito: un 0 provocado por el
// filtro activo no es demanda no cubierta, es un filtro puesto — y el producto
// existe. Lo que el visitante tenía delante va en `n_filtrado`.
//
// POR QUÉ UN BLOB POR EVENTO Y NO UN JSON QUE CRECE: dos visitantes buscando a
// la vez se pisarían la escritura (leer-modificar-escribir) y se perderían
// eventos en silencio. La clave es `<YYYY-MM-DD>/<ts>-<aleatorio>`, así que el
// informe puede listar por prefijo de día sin recorrer todo el store.
//
// CONTRATO: 204 siempre que la entrada sea válida — incluso si Blobs falla (el
// buscador del hub NUNCA debe fallar por culpa del registro; el fallo se ve en
// los logs de la function, no en la cara del visitante). 400 solo si el JSON es
// inválido o los campos no pasan la validación. 405 si el método no es
// POST/OPTIONS. 429 si se supera el cupo por minuto (ver MAX_EVENTOS_MINUTO).
//
// RETENCIÓN: los eventos NO caducan solos. La purga es manual y va en el otro
// endpoint: `search-report?purge=1&before=YYYY-MM-DD` (borra días completos y
// con ellos los emails de contacto). Política y plazo en BUSCADOR-HUB.md §2.
//
// GOTCHA DE BLOBS: solo funciona DESPLEGADO en Netlify. En local no hay store
// (`netlify dev` monta uno propio, pero aquí no se levanta nada local: regla
// térmica del Mac). Y al ser una function v1 (Lambda-compat, `Handler` de
// @netlify/functions) hay que llamar a `connectLambda(event)` ANTES de
// `getStore`: el contexto de Blobs viaja en `event.blobs`, que el tipo público
// de HandlerEvent no declara (de ahí el cast).
//
// CÓMO VERIFICAR EN PRODUCCIÓN (tras el deploy):
//   curl -i -X POST https://aichef.pro/.netlify/functions/log-search \
//     -H 'Content-Type: application/json' \
//     -d '{"q":"prueba curl","n":0,"coming":0,"sin_resultados":true,"path":"/productos-digitales"}'
//   → HTTP/2 204. Y después, el informe:
//   curl -s -H "x-admin-password: $ADMIN_PASSWORD" \
//     'https://aichef.pro/.netlify/functions/search-report?days=1' | head -40
//   (o directamente `python3 scripts/productos-digitales/buscador-report.py --days 1`)
// ════════════════════════════════════════════════════════════════════════════

const STORE = 'search-queries';

// Límites de TAMAÑO de cada evento. OJO: acotan lo que OCUPA un evento, no
// cuántos se pueden mandar — el cupo por minuto de más abajo es lo que impide
// que un bucle de curl infle el almacenamiento y contamine la señal de demanda
// (antes este comentario decía que los límites eran esa defensa; era falso).
const MAX_BODY = 4000;
const MAX_Q = 120;
const MAX_TAG = 40;
const MAX_LANG = 5;
const MAX_PATH = 120;
const MAX_DETALLE = 600;
const MAX_EMAIL = 120;
const MAX_ORIGEN = 12;

// Techo de los contadores. Sin él `Number.isInteger(1e308)` es true, y un solo
// POST anónimo con ese valor hace que la media del informe salga Infinity, se
// serialice como null y reviente el formateo del script de lectura.
const MAX_CONTEO = 10000;

// CUPO: eventos aceptados por minuto (todo el site). El tráfico real de la
// tienda son unos pocos eventos por visitante y sesión; un bucle de curl hace
// miles. Contador aproximado en un blob `rl/<YYYY-MM-DDTHH:mm>`: dos peticiones
// simultáneas pueden leer el mismo valor y colarse una de más, que para una
// guarda de coste da igual. Si Blobs falla se deja pasar (fail-open): el
// registro es telemetría y jamás debe tumbar el buscador.
const MAX_EVENTOS_MINUTO = 120;

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

// Caracteres de control (C0 + DEL + C1), declarados por ESCAPE a propósito.
const CONTROL_RE = /[\u0000-\u001f\u007f-\u009f]/g;

/** Quita caracteres de control y colapsa espacios. `trim()` solo limpia los
 *  extremos: sin esto un visitante anónimo puede meter secuencias ANSI (ESC +
 *  "[2J") en `q` o en `detalle` y falsear lo que el operador ve en su terminal
 *  al leer el informe — que es con lo que se decide qué producto se fabrica. El
 *  `\s` del regex de email tampoco cubre esos caracteres. */
function limpiar(s: string): string {
  return s.replace(CONTROL_RE, ' ').replace(/\s+/g, ' ').trim();
}

/** minúsculas · sin acentos (ñ→n) · cualquier no-alfanumérico → espacio.
 *
 *  ⚠ TIENE QUE PRODUCIR LA MISMA CADENA que `normalizarBusqueda` del front
 *  (astro-site/src/lib/normalizar-busqueda.ts) y que `norm()` de
 *  scripts/productos-digitales/buscador-report.py. Antes aquí solo se
 *  colapsaban espacios: «APPCC.», «appcc?» y «appcc» generaban TRES q_norm
 *  distintas, ninguna llegaba al umbral --min-veces del informe y la marca de
 *  «demanda no cubierta» —el único output que justifica esta feature— se
 *  perdía. Y el dedup de sesión del front usaba su normalización mientras el
 *  servidor agregaba por la suya: ni siquiera eran la misma clave. */
function normalizar(s: string): string {
  return s
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, ' ')
    .trim();
}

function esConteoValido(v: unknown): boolean {
  return typeof v === 'number' && Number.isInteger(v) && v >= 0 && v <= MAX_CONTEO;
}

/** SOLO las tres cabeceras de geo. No se lee (ni se copia a memoria) ninguna otra:
 *  ni user-agent, ni client-ip, ni x-forwarded-for. Ver BUSCADOR-HUB.md §2. */
function pais(raw: Record<string, string | undefined> | undefined): string {
  const h = raw || {};
  const leer = (nombre: string): string => {
    const v = h[nombre] ?? h[nombre.toUpperCase()];
    return typeof v === 'string' ? v : '';
  };
  const directo = leer('x-country') || leer('x-nf-country');
  if (/^[A-Za-z]{2}$/.test(directo)) return directo.toUpperCase();
  // x-nf-geo: JSON en base64 con { country: { code, name }, … }
  const geo = leer('x-nf-geo');
  if (geo) {
    try {
      const json = JSON.parse(Buffer.from(geo, 'base64').toString('utf-8'));
      const code = json?.country?.code;
      if (typeof code === 'string' && /^[A-Za-z]{2}$/.test(code)) return code.toUpperCase();
    } catch {
      /* geo ilegible: se ignora, no es motivo para perder el evento */
    }
  }
  return '';
}


function aleatorio(): string {
  const c = (globalThis as { crypto?: { randomUUID?: () => string } }).crypto;
  if (c?.randomUUID) return c.randomUUID().slice(0, 8);
  return Math.random().toString(36).slice(2, 10);
}

type Store = {
  get: (key: string, opts: { type: 'json' }) => Promise<unknown>;
  setJSON: (key: string, value: unknown) => Promise<unknown>;
};

/** Cupo por minuto. Devuelve true si hay que rechazar con 429. Fail-open. */
async function excedeCupo(store: Store, ts: string): Promise<boolean> {
  const clave = `rl/${ts.slice(0, 16)}`; // rl/YYYY-MM-DDTHH:mm
  try {
    const actual = (await store.get(clave, { type: 'json' })) as { n?: number } | null;
    const n = actual && typeof actual.n === 'number' ? actual.n : 0;
    if (n >= MAX_EVENTOS_MINUTO) return true;
    await store.setJSON(clave, { n: n + 1 });
  } catch (err) {
    console.error('log-search: cupo no verificable (se deja pasar):', err);
  }
  return false;
}

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
    return { statusCode: 405, headers, body: JSON.stringify({ error: 'Method not allowed' }) };
  }

  try {
    if ((event.body || '').length > MAX_BODY) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'body_too_large' }) };
    }

    let datos: Record<string, unknown>;
    try {
      datos = JSON.parse(event.body || '{}');
    } catch {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'invalid_json' }) };
    }
    if (!datos || typeof datos !== 'object' || Array.isArray(datos)) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'invalid_json' }) };
    }

    // Honeypot: el formulario pinta un campo `website` oculto (#pd-ask-website en
    // ProductosDigitalesHubPage.astro) que ninguna persona rellena. Si viene con
    // algo, es un bot → 204 sin escribir nada (no se le dice que ha sido detectado).
    const honeypot = datos.website;
    if (typeof honeypot === 'string' && honeypot.trim() !== '') {
      return { statusCode: 204, headers, body: '' };
    }

    // ── Validación ────────────────────────────────────────────────────────
    const q = typeof datos.q === 'string' ? limpiar(datos.q) : '';
    if (q.length < 1 || q.length > MAX_Q) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'invalid_q' }) };
    }

    const n = datos.n === undefined || datos.n === null ? 0 : datos.n;
    if (!esConteoValido(n)) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'invalid_n' }) };
    }

    // Lo que el visitante tenía DELANTE (con el chip de categoría aplicado). Si no
    // viene, se asume igual a `n`: sin chip no hay diferencia entre los dos.
    const nFiltrado = datos.n_filtrado === undefined || datos.n_filtrado === null ? n : datos.n_filtrado;
    if (!esConteoValido(nFiltrado)) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'invalid_n_filtrado' }) };
    }

    const coming = datos.coming === undefined || datos.coming === null ? 0 : datos.coming;
    if (!esConteoValido(coming)) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'invalid_coming' }) };
    }

    const tag = typeof datos.tag === 'string' ? limpiar(datos.tag) : '';
    if (tag.length > MAX_TAG) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'invalid_tag' }) };
    }

    const lang = typeof datos.lang === 'string' ? limpiar(datos.lang) : '';
    if (lang.length > MAX_LANG) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'invalid_lang' }) };
    }

    const path = typeof datos.path === 'string' ? limpiar(datos.path) : '';
    if (path.length > MAX_PATH) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'invalid_path' }) };
    }

    const detalle = typeof datos.detalle === 'string' ? limpiar(datos.detalle) : '';
    if (detalle.length > MAX_DETALLE) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'invalid_detalle' }) };
    }

    const email = typeof datos.email === 'string' ? limpiar(datos.email) : '';
    if (email.length > MAX_EMAIL || (email !== '' && !EMAIL_RE.test(email))) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'invalid_email' }) };
    }

    // 'form' = lo mandó el formulario «Dinos qué buscabas», que repite una `q` ya
    // registrada 1,2 s antes: lo nuevo son el detalle y el email. El informe no lo
    // cuenta en `veces` para no contar dos veces la misma búsqueda.
    const origen = typeof datos.origen === 'string' ? limpiar(datos.origen).slice(0, MAX_ORIGEN) : '';

    // Si no viene el booleano, se deduce: ni productos ni «próximamente».
    const sin_resultados =
      typeof datos.sin_resultados === 'boolean' ? datos.sin_resultados : (n as number) === 0 && (coming as number) === 0;

    const ts = new Date().toISOString();
    const entrada = {
      q,
      q_norm: normalizar(q),
      n: n as number,
      n_filtrado: nFiltrado as number,
      coming: coming as number,
      tag,
      lang,
      path,
      sin_resultados,
      detalle,
      email,
      origen,
      country: pais(event.headers as Record<string, string | undefined>),
      ts,
    };

    // ── Escritura (nunca bloquea la respuesta con un error) ───────────────
    try {
      const { connectLambda, getStore } = await import('@netlify/blobs');
      // Function v1: el contexto de Blobs llega en event.blobs (no declarado
      // en HandlerEvent). Si el runtime ya lo inyectó por env var, esto no
      // estorba; si falla, getStore lo intentará por su cuenta.
      try {
        connectLambda(event as unknown as { blobs: string; headers: Record<string, string> });
      } catch {
        /* runtime sin event.blobs: seguimos y probamos getStore igualmente */
      }
      const store = getStore(STORE) as unknown as Store;

      if (await excedeCupo(store, ts)) {
        return { statusCode: 429, headers, body: JSON.stringify({ error: 'rate_limited' }) };
      }

      // `:` y `.` fuera de la clave para no depender de las reglas de claves.
      const clave = `${ts.slice(0, 10)}/${ts.replace(/[:.]/g, '-')}-${aleatorio()}`;
      await store.setJSON(clave, entrada);
    } catch (err) {
      // El registro es telemetría: si Blobs no está disponible el buscador
      // tiene que seguir funcionando igual. Queda en los logs de la function.
      console.error('log-search: no se pudo escribir en Blobs:', err);
    }

    return { statusCode: 204, headers, body: '' };
  } catch (err) {
    console.error('log-search error:', err);
    // Ni siquiera un fallo inesperado debe romper el buscador del hub.
    return { statusCode: 204, headers, body: '' };
  }
};
