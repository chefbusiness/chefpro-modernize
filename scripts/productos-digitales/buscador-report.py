#!/usr/bin/env python3
"""
Informe del buscador del hub de productos digitales (aichef.pro/productos-digitales).

Lee las búsquedas que registra la function `log-search` (store de Netlify Blobs
`search-queries`, informe en `search-report`) y las CRUZA contra:

  (a) el catálogo LIVE del hub  → astro-site/src/components/pages/ProductosDigitalesHubPage.astro
      (arrays `products` y `comingSoon`: nombre, slug y tags)
  (b) la cola de productos nuevos → scripts/productos-digitales/CALENDARIO-V2-SEMANAL.md
      (§3 «Micro-proyecto productos nuevos» + las líneas «Cómo Montar» / «Manual» / «Kit»)

Imprime una tabla «consulta · veces · resultados medios · ¿existe? · ¿en cola? · países»
y marca con ⚠ las consultas DEMANDADAS (≥ --min-veces, por defecto 2) que el BUSCADOR LIVE
no resolvió (media de resultados = 0) y que además no están en la cola: ésa es la señal de
producto que se puede vender y no tenemos.

El criterio es el dato de producción, no el grep: «¿existe?» es una pista de contexto. El
cruce usa el MISMO corpus (nombre + slug + tags + alias + descripción + features) y los
MISMOS sinónimos (astro-site/src/lib/sinonimos-buscador.json) que el buscador del hub, para
que esta tabla no contradiga a la página.

Uso:
  python3 scripts/productos-digitales/buscador-report.py                 # últimos 30 días
  python3 scripts/productos-digitales/buscador-report.py --days 7
  python3 scripts/productos-digitales/buscador-report.py --min-veces 3
  python3 scripts/productos-digitales/buscador-report.py --json          # salida JSON

Requisitos:
  · ADMIN_PASSWORD en el entorno (OBLIGATORIO en la práctica: la variable está marcada
    como SECRETA en Netlify y `netlify env:get` devuelve un valor de relleno de 20
    caracteres que NO es la contraseña — comprobado el 2026-09-05: con ese valor la
    function responde 401). Uso: `ADMIN_PASSWORD='…' python3 buscador-report.py --days 30`.
  · Nada más: HTTP con `curl` por subprocess (el python3 del Mac no trae CA
    bundle y urllib revienta con SSL — mismo motivo que en gate-flujo-postpago.py).
    La contraseña viaja en un fichero de configuración de curl leído por STDIN,
    NUNCA en argv (no aparece en `ps`).

Gotcha: Netlify Blobs solo existe DESPLEGADO. Si el informe devuelve 0 eventos,
comprueba primero que las functions están en producción (ver BUSCADOR-HUB.md).
"""
import argparse
import json
import os
import re
import subprocess
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_URL = os.environ.get('AICP_BASE_URL', 'https://aichef.pro')
ENDPOINT = '/.netlify/functions/search-report'
HUB = os.path.join(ROOT, 'astro-site', 'src', 'components', 'pages', 'ProductosDigitalesHubPage.astro')
CALENDARIO = os.path.join(ROOT, 'scripts', 'productos-digitales', 'CALENDARIO-V2-SEMANAL.md')
# MISMO fichero que usan el frontmatter del hub y el <script> del buscador. Si el cruce
# de aquí no expandiera los sinónimos, marcaría como «demanda no cubierta» consultas que
# el buscador SÍ resuelve: medido, 22 de 52 (42 %) — «costeo de recetas», «haccp»,
# «gerente», «alérgenos», «mermas»… justo el vocabulario de Hispanoamérica.
SINONIMOS = os.path.join(ROOT, 'astro-site', 'src', 'lib', 'sinonimos-buscador.json')

SITE_ID = os.environ.get('AICP_SITE_ID', 'ee5802cf-34bb-4354-90d9-aa9f628b4038')
ACCOUNT = os.environ.get('AICP_NETLIFY_ACCOUNT', 'chebfusiness')

# Palabras que no aportan nada al cruce (y que si se exigieran darían falsos negativos).
STOP = {
    'de', 'del', 'la', 'el', 'los', 'las', 'un', 'una', 'unos', 'unas', 'para', 'por', 'con',
    'sin', 'que', 'como', 'mi', 'tu', 'su', 'y', 'o', 'en', 'al', 'lo', 'me', 'se', 'es',
}


# ── Normalización ────────────────────────────────────────────────────────────
# LA MISMA que netlify/functions/log-search.ts y que `normalizarBusqueda` del front
# (astro-site/src/lib/normalizar-busqueda.ts). Antes aquí (y en la function) solo se
# colapsaban espacios: «APPCC.», «appcc?» y «appcc» daban tres q_norm distintas, se
# repartían las veces y ninguna alcanzaba el umbral --min-veces. Cualquier cambio en
# una de las tres hay que replicarlo en las otras dos.
def norm(s):
    """minúsculas · sin acentos (ñ→n) · cualquier no-alfanumérico → espacio."""
    s = unicodedata.normalize('NFD', str(s))
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r'[^0-9a-z]+', ' ', s).strip()


# Caracteres de control: el backend ya los limpia, pero el informe se imprime en la
# terminal de John y los eventos viejos (o los de otro origen) pueden traerlos.
CONTROL = re.compile(r'[\x00-\x1f\x7f-\x9f]')


def sinonimos():
    """(grupos, frases, alias) del JSON compartido con el buscador. Si falta, se sigue
    sin expansión: el informe es una herramienta de lectura, no puede caerse por esto."""
    try:
        with open(SINONIMOS, encoding='utf-8') as f:
            d = json.load(f)
        return d.get('grupos', []), d.get('frases', []), d.get('alias', {})
    except Exception as e:  # noqa
        print(f'⚠ no se pudo leer {os.path.relpath(SINONIMOS, ROOT)}: {e} '
              f'(el cruce irá SIN sinónimos y marcará de más)', file=sys.stderr)
        return [], [], {}


GRUPOS, FRASES, ALIAS = sinonimos()


def variantes(q):
    """Expande las frases sinónimas sobre la consulta entera (igual que el front)."""
    out = [q]
    for a, b in FRASES:
        for v in list(out):
            if a in v:
                out.append(v.replace(a, b))
            elif b in v:
                out.append(v.replace(b, a))
    return out[:6]


def token_en(blob, t):
    """¿Está el token en el blob, con límite de palabra o vía sinónimo?

    El límite de palabra importa: sin él «bar» casaba con «barra» y «gastrobar», e «ia»
    con «guia» y «ingenieria» — el informe inventaba un «¿existe?» para consultas que el
    buscador nunca resuelve así."""
    if re.search(r'(?:^| )' + re.escape(t), blob):
        return True
    if len(t) < 3:
        return False
    for grupo in GRUPOS:
        if not any(g.startswith(t) for g in grupo):
            continue
        if any(re.search(r'(?:^| )' + re.escape(g), blob) for g in grupo):
            return True
    return False


def tokens(q):
    return [t for t in re.split(r'[^0-9a-z]+', norm(q)) if len(t) >= 3 and t not in STOP]


# ── Credencial ───────────────────────────────────────────────────────────────
def netlify_env():
    """PATH con el pnpm del Mac (donde vive el CLI de Netlify), como en gate-flujo-postpago.py."""
    return dict(os.environ, PATH=os.path.expanduser('~/Library/pnpm') + ':' + os.environ.get('PATH', ''))


def admin_password():
    pw = os.environ.get('ADMIN_PASSWORD')
    if pw:
        return pw.strip()
    env = netlify_env()
    # 1) netlify env:get (necesita el site enlazado en la carpeta)
    try:
        r = subprocess.run(['netlify', 'env:get', 'ADMIN_PASSWORD'], capture_output=True, text=True,
                           timeout=60, env=env, cwd=ROOT)
        for ln in reversed((r.stdout or '').split('\n')):
            ln = ln.strip().strip('│').strip()
            if ln and not ln.startswith(('┌', '└', '├', '─', 'Value', '.Env', 'No value')) and ' ' not in ln:
                return ln
    except Exception:
        pass
    # 2) netlify api getEnvVars (patrón ya probado en este repo)
    try:
        data = json.dumps({'account_id': ACCOUNT, 'site_id': SITE_ID})
        r = subprocess.run(['netlify', 'api', 'getEnvVars', '--data', data], capture_output=True,
                           text=True, timeout=60, env=env)
        for v in json.loads(r.stdout):
            if v.get('key') == 'ADMIN_PASSWORD':
                for val in v.get('values') or []:
                    if val.get('value'):
                        return val['value']
    except Exception:
        pass
    return None


# ── HTTP (curl; la contraseña por stdin, nunca en argv) ──────────────────────
def pedir_informe(pw, days, raw=False):
    url = f'{BASE_URL}{ENDPOINT}?days={days}' + ('&raw=1' if raw else '')
    esc = lambda s: s.replace('\\', '\\\\').replace('"', '\\"')  # noqa: E731
    config = (
        f'url = "{esc(url)}"\n'
        f'header = "x-admin-password: {esc(pw)}"\n'
        'max-time = 120\n'
        'silent\n'
        'show-error\n'
        'write-out = "\\nHTTP_STATUS:%{http_code}\\n"\n'
    )
    try:
        r = subprocess.run(['curl', '-K', '-'], input=config.encode('utf-8'),
                           capture_output=True, timeout=180)
    except Exception as e:  # noqa
        return None, -1, str(e)
    salida = r.stdout.decode('utf-8', 'ignore')
    m = re.search(r'HTTP_STATUS:(\d+)\s*$', salida)
    status = int(m.group(1)) if m else -1
    cuerpo = salida[:m.start()] if m else salida
    if status != 200:
        return None, status, (r.stderr.decode('utf-8', 'ignore') + cuerpo)[:300]
    try:
        return json.loads(cuerpo), status, ''
    except Exception as e:  # noqa
        return None, status, f'respuesta no-JSON: {e}: {cuerpo[:200]!r}'


# ── Catálogo del hub ─────────────────────────────────────────────────────────
def _bloque(src, nombre):
    m = re.search(rf'^const {nombre} = \[(.*?)^\];', src, re.S | re.M)
    return m.group(1) if m else ''


def _campo(blk, clave):
    m = re.search(rf"{clave}:\s*'((?:[^'\\]|\\.)*)'", blk)
    return m.group(1).replace("\\'", "'") if m else ''


def _tags(blk):
    m = re.search(r'tags:\s*\[(.*?)\]', blk, re.S)
    return re.findall(r"'([^']+)'", m.group(1)) if m else []


def _features(blk):
    """Las viñetas de venta. El data-search del hub las indexa, así que sin ellas este
    cruce dice «no existe» de consultas que el buscador resuelve: medido, «fichas
    tecnicas» y «precios» solo aparecen ahí, y «escandallo» pasa de 16 a 11 aciertos."""
    m = re.search(r'features:\s*\[(.*?)\]', blk, re.S)
    return re.findall(r"'((?:[^'\\]|\\.)*)'", m.group(1)) if m else []


def catalogo():
    """[(etiqueta, nombre, nombre+slug+tags, +descripción)] de products + comingSoon del hub LIVE.

    Se guardan tres niveles para poder distinguir un acierto en el NOMBRE (el producto
    existe y se llama así) de un acierto solo en la descripción (parecido, se marca «≈»).
    """
    with open(HUB, encoding='utf-8') as f:
        src = f.read()
    out = []

    def add(blk, es_coming):
        name = _campo(blk, 'name')
        if not name:
            return
        tags = _tags(blk)
        slug = _campo(blk, 'slug')
        desc = _campo(blk, 'description') or _campo(blk, 'desc')
        etiqueta = ('🔜 ' if es_coming else '') + name
        estrecho = norm(' '.join([name, slug] + tags + [ALIAS.get(slug, '')]))
        ancho = norm(' '.join([estrecho, desc] + _features(blk)))
        out.append((etiqueta, norm(name), estrecho, ancho))

    for nombre, es_coming in (('products', False), ('comingSoon', True)):
        bloque = _bloque(src, nombre)
        if not bloque:
            print(f'⚠ no se pudo leer el array `{nombre}` de {os.path.relpath(HUB, ROOT)}', file=sys.stderr)
            continue
        antes = len(out)
        # products: un objeto multilínea por entrada.
        for m in re.finditer(r'^  \{(.*?)^  \},?$', bloque, re.S | re.M):
            add(m.group(1), es_coming)
        # comingSoon: una línea por entrada (el patrón de bloque no casa).
        if len(out) == antes:
            for ln in bloque.split('\n'):
                add(ln, es_coming)
    return out


# ── Cola de productos nuevos (CALENDARIO §3 + líneas Cómo Montar/Manual/Kit) ──
def cola():
    """[(nombre, nombre, nombre, nombre)] de los productos que YA están en la cola.

    Fuente: §3 del CALENDARIO (lista numerada de productos nuevos) + cualquier línea del
    fichero que nombre en negrita un producto de las familias «Cómo Montar», «Manual»,
    «Guía», «Kit», «Plan» o «Pack». Se cruza SOLO contra el nombre: usar la línea entera
    daba falsos positivos (una línea que menciona de pasada «panadería» no es una cola).
    """
    with open(CALENDARIO, encoding='utf-8') as f:
        src = f.read()
    m = re.search(r'^## 3\..*?(?=^## |\Z)', src, re.S | re.M)
    seccion = m.group(0) if m else ''
    familias = re.compile(r'^(guia|manual|kit|plan|pack|mega|como montar|ebook)', re.I)

    nombres = []
    for ln in seccion.split('\n'):
        if re.match(r'\s*\d+\.\s', ln):  # la lista numerada de productos nuevos
            nombres += re.findall(r'\*\*(.+?)\*\*', ln)
    for ln in src.split('\n'):
        if re.search(r'Cómo Montar|Manual del|Manual de|\bKit\b|\bGuía\b|\bPlan de Negocio\b', ln):
            nombres += re.findall(r'\*\*(.+?)\*\*', ln)

    out, visto = [], set()
    for nombre in nombres:
        nombre = re.sub(r'[«»`*]', '', nombre).strip(' .·—-')
        n = norm(nombre)
        if len(nombre) <= 3 or not familias.match(n) or n in visto:
            continue
        # «Guía X» y «Guía X a mediados de octubre» son el mismo producto: se queda el corto.
        if any(n.startswith(v) or v.startswith(n) for v in visto):
            continue
        visto.add(n)
        out.append((nombre, n, n, n))
    return out


# ── Cruce ────────────────────────────────────────────────────────────────────
def buscar(q_norm, corpus):
    """Etiqueta del primer elemento que cubre la consulta.

    Tres pasadas, de más fuerte a más débil: nombre → nombre+slug+tags+alias →
    +descripción+features. La tercera se devuelve marcada con «≈» (parecido, no es el
    producto). La consulta se expande con los MISMOS sinónimos que el buscador y todo se
    compara con límite de palabra: si aquí no se hiciera, esta columna contradiría a la
    página — que es lo que la volvía inservible para decidir un producto.
    """
    consultas = [v for v in variantes(q_norm) if v]
    # tokens() es la ÚNICA definición de la regla (≥3 caracteres y fuera las stopwords):
    # duplicarla aquí sería repetir el error que este mismo informe viene a corregir.
    listas = [(v, tokens(v)) for v in consultas]
    for nivel, marca in ((1, ''), (2, ''), (3, '≈ ')):
        for entrada in corpus:
            etiqueta, blob = entrada[0], entrada[nivel]
            for v, ts in listas:
                # Consulta corta o toda stopwords: se exige la frase con límite de palabra
                # (sin él, «ia» casaba dentro de «guia» y de «ingenieria»).
                if not ts:
                    if v and re.search(r'(?:^| )' + re.escape(v), blob):
                        return marca + etiqueta
                    continue
                if all(token_en(blob, t) for t in ts):
                    return marca + etiqueta
    return ''


def paises_txt(d):
    if not d:
        return '—'
    return ' '.join(f'{k}:{v}' for k, v in sorted(d.items(), key=lambda kv: -kv[1])[:4])


def recorta(s, n):
    # El texto viene de un endpoint público: un visitante anónimo podría haber metido
    # secuencias ANSI y falsear lo que se lee en la terminal. El backend ya las limpia;
    # esto es el cinturón para los eventos que se escribieron antes.
    s = CONTROL.sub(' ', str(s))
    return s if len(s) <= n else s[: n - 1] + '…'


def main():
    ap = argparse.ArgumentParser(description='Informe cruzado del buscador del hub de productos digitales.')
    ap.add_argument('--days', type=int, default=30, help='ventana en días (1-365, por defecto 30)')
    ap.add_argument('--min-veces', type=int, default=2,
                    help='umbral para marcar ⚠ una consulta como demanda no cubierta (por defecto 2)')
    ap.add_argument('--json', action='store_true', help='vuelca el cruce completo en JSON')
    args = ap.parse_args()

    days = max(1, min(365, args.days))
    pw = admin_password()
    if not pw:
        print('✖ No hay ADMIN_PASSWORD. Exporta la variable o autentica el CLI de Netlify:\n'
              '   export ADMIN_PASSWORD=…   (o `netlify link` en el repo)', file=sys.stderr)
        return 2

    informe, status, err = pedir_informe(pw, days)
    if informe is None:
        print(f'✖ El informe falló (HTTP {status}): {err}', file=sys.stderr)
        if status == 401:
            print('  → ADMIN_PASSWORD no coincide con la del site.', file=sys.stderr)
        if status == 404:
            print('  → ¿está desplegada netlify/functions/search-report.ts?', file=sys.stderr)
        return 1

    cat, queue = catalogo(), cola()

    filas = []
    sin_res = {f['q_norm']: f for f in informe.get('sin_resultados', [])}
    for f in informe.get('top_queries', []):
        q = f.get('q_norm', '')
        existe = buscar(q, cat)
        en_cola = buscar(q, queue)
        s = sin_res.get(q, {})
        veces = f.get('veces', 0)
        try:
            media = float(f.get('media_resultados') or 0)
        except (TypeError, ValueError):
            media = 0.0
        # PRIORIDAD INVERTIDA (antes mandaba el grep del catálogo y marcaba 22 de 52
        # consultas resueltas como «demanda no cubierta»): manda el dato LIVE del
        # buscador —cuántos productos vio de verdad el visitante—, que ya viene en el
        # informe y es autoritativo. La columna «¿existe?» pasa a ser una pista.
        no_cubierta = (media == 0) or bool(veces and s.get('veces', 0) >= veces)
        filas.append({
            'q_norm': q,
            'ejemplo': f.get('ejemplo', q),
            'veces': veces,
            'media_resultados': media,
            'veces_sin_resultados': s.get('veces', 0),
            'existe': existe,
            'en_cola': en_cola,
            'paises': f.get('paises', {}),
            'detalles': s.get('detalles', []),
            'emails': s.get('emails', []),
            'oportunidad': (no_cubierta and not en_cola and veces >= args.min_veces),
        })

    if args.json:
        print(json.dumps({
            'base_url': BASE_URL,
            'days': days,
            'min_veces': args.min_veces,
            'total_eventos': informe.get('total', 0),
            'por_dia': informe.get('por_dia', {}),
            'por_pais': informe.get('por_pais', {}),
            'catalogo_entradas': len(cat),
            'cola_entradas': len(queue),
            'consultas': filas,
        }, ensure_ascii=False, indent=2))
        return 0

    total = informe.get('total', 0)
    print(f'\n🔎 Buscador del hub — {BASE_URL} · últimos {days} días '
          f'({informe.get("desde", "?")} → {informe.get("hasta", "?")})')
    print(f'   {total} búsquedas registradas · {len(filas)} consultas distintas · '
          f'catálogo: {len(cat)} productos · cola: {len(queue)} candidatos')
    if informe.get('truncado'):
        print('   ⚠ el informe venía TRUNCADO (demasiados eventos para la ventana pedida)')
    if not filas:
        print('\n   (sin datos todavía — comprueba en BUSCADOR-HUB.md que las functions están desplegadas)\n')
        return 0

    print(f'\n{"consulta":36} {"veces":>5} {"res.":>6}  {"¿existe?":26} {"¿en cola?":24} países')
    print('─' * 118)
    for f in sorted(filas, key=lambda x: (-x['veces'], x['q_norm'])):
        marca = '⚠ ' if f['oportunidad'] else '  '
        print(f'{marca}{recorta(f["ejemplo"], 34):34} {f["veces"]:5} {f["media_resultados"]:6.1f}  '
              f'{recorta(f["existe"] or "NO", 26):26} {recorta(f["en_cola"] or "no", 24):24} '
              f'{paises_txt(f["paises"])}')

    oportunidades = [f for f in filas if f['oportunidad']]
    if oportunidades:
        print(f'\n⚠ DEMANDA NO CUBIERTA (≥ {args.min_veces} búsquedas, ni en el catálogo ni en la cola):')
        for f in sorted(oportunidades, key=lambda x: -x['veces']):
            print(f'   · «{f["ejemplo"]}» — {f["veces"]} búsquedas · {paises_txt(f["paises"])}')
            for d in f['detalles'][:3]:
                print(f'       ↳ «{recorta(d, 100)}»')
            if f['emails']:
                print(f'       ↳ contacto: {", ".join(f["emails"][:5])}')
    else:
        print('\n✓ Ninguna consulta demandada se queda fuera del catálogo y de la cola.')

    por_pais = informe.get('por_pais', {})
    if por_pais:
        print(f'\nPor país: {paises_txt(por_pais)}')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
