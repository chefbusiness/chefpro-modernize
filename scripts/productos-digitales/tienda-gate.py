#!/usr/bin/env python3
"""
Gate de la TIENDA INTERNACIONAL de productos digitales (plan: TIENDA-INTERNACIONAL.md §3).

La tienda de cada idioma vive anidada bajo su hub (/en/digital-products/<slug>, …/access,
…/library) y su registro es astro-site/src/lib/tienda.ts. Tres ficheros que NO pueden
importarlo repiten sus segmentos, y si divergen el fallo es SILENCIOSO (un dashboard de
pago en el sitemap, o un dashboard rastreable): este gate los cruza.

MODOS

  (sin argumentos) — ESTÁTICO, sin red:
    1. Los segmentos de TIENDAS (tienda.ts) == los del filtro del sitemap de
       astro.config.mjs (regex de dashboards anidados), idiomas incluidos.
    2. Toda tienda ACTIVA que no sea ES tiene en robots.txt, en CADA bloque de
       user-agent, sus dos Disallow (/<lang>/<segmento>/*/access y /library), y el
       matcher de robots-gate.py confirma: gate y dashboard bloqueados, hub y landing no.
    3. Cada producto VIVO de otro idioma en FAMILIAS: su tienda está activa, su gemelo ES
       está vivo, y existen su data file (astro-site/src/data/productos-<lang>/**/<slug>.ts),
       sus 3 páginas (landing, access, library) y su entrada en zona-app.ts con lang.
    Con cero productos vivos fuera de ES pasa en verde.

  --base <url> — RED contra un deploy (preview o producción):
    Hubs de TODAS las tiendas activas (ES incluida): 200, <html lang>, canonical propio,
    hreflang recíproco completo entre todos ellos + x-default al hub ES, y exactamente 1 botón
    flotante de WhatsApp; los no-ES además pasan la revisión de texto de abajo.
    Para cada producto vivo de otro idioma:
    200; hreflang recíproco con el gemelo ES (en los dos sentidos); sin '€' en el texto
    visible; sin restos de español (heurística; se ignoran <script>, <style> y el bloque
    marcado con el atributo data-lang-es, p. ej. «¿Hablas español?»); sin caracteres no
    latinos (CJK, cirílico, hangul, árabe, hebreo, tailandés). Gate y dashboard: noindex.

  --es-identico --base <preview> — las 5 landings ES de la plantilla KitExcel
    (/kit-escandallos, /pack-appcc, /kit-inventario, /kit-gestion-personal,
    /kit-plan-financiero) del preview contra https://aichef.pro, normalizando los hashes
    de /_astro/*.js|css, el id de scope de Astro (data-astro-cid-*) y el host del preview.
    Sale 1 ante cualquier diferencia y enseña el contexto de la primera.
    ⚠️ Un preview con otras env vars de build que producción (CRYPTO_PRODUCTS, enlaces de
    Stripe) da diferencias que NO son de la plantilla: leer el contexto antes de culpar.

Uso:
    python3 scripts/productos-digitales/tienda-gate.py
    python3 scripts/productos-digitales/tienda-gate.py --base https://deploy-preview-N--aichefpro.netlify.app
    python3 scripts/productos-digitales/tienda-gate.py --es-identico --base https://deploy-preview-N--aichefpro.netlify.app
"""
from __future__ import annotations

import argparse
import importlib.util
import re
import time
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ASTRO = REPO / 'astro-site'
TIENDA_TS = ASTRO / 'src/lib/tienda.ts'
ASTRO_CONFIG = ASTRO / 'astro.config.mjs'
ROBOTS = ASTRO / 'public/robots.txt'
ZONA_APP = ASTRO / 'src/lib/zona-app.ts'
ROBOTS_GATE = REPO / 'scripts/astro-migration/robots-gate.py'
PROD = 'https://aichef.pro'
KITEXCEL_ES = ['/kit-escandallos', '/pack-appcc', '/kit-inventario', '/kit-gestion-personal', '/kit-plan-financiero']

errores: list[str] = []


def mal(msg: str) -> None:
    errores.append(msg)
    print(f'❌ {msg}')


def bien(msg: str) -> None:
    print(f'✅ {msg}')


# ------------------------------------------------------------------ registro

def leer_tiendas() -> dict[str, dict]:
    txt = TIENDA_TS.read_text(encoding='utf-8')
    tiendas = {}
    for m in re.finditer(r"^\s*([a-z]{2}): \{ hubPath: '([^']+)', segmento: '([^']+)', "
                         r"moneda: '([A-Z]{3})', activa: (true|false) \}", txt, re.M):
        tiendas[m.group(1)] = {'hub': m.group(2), 'seg': m.group(3), 'moneda': m.group(4),
                               'activa': m.group(5) == 'true'}
    if len(tiendas) != 7:
        mal(f'tienda.ts: {len(tiendas)} tiendas parseadas (esperado 7) — ¿cambió el formato de TIENDAS?')
    for lang, t in tiendas.items():
        esperado = f'/{t["seg"]}' if lang == 'es' else f'/{lang}/{t["seg"]}'
        if t['hub'] != esperado:
            mal(f'tienda.ts: {lang} hubPath {t["hub"]} != {esperado}')
    return tiendas


def leer_familias() -> list[dict]:
    txt = TIENDA_TS.read_text(encoding='utf-8')
    bloque = txt[txt.index('export const FAMILIAS'):]
    bloque = bloque[:bloque.index('\n];') + 3]
    familias = []
    for m in re.finditer(r"familia: '([^']+)',\s*productos: \{(.*?)\n    \},", bloque, re.S):
        prods = {lg: {'slug': sl, 'vivo': v == 'true'} for lg, sl, v in
                 re.findall(r"([a-z]{2}): \{ slug: '([^']+)', vivo: (true|false) \}", m.group(2))}
        familias.append({'familia': m.group(1), 'productos': prods})
    n_decl = len(re.findall(r"familia: '", bloque))
    if n_decl != len(familias):
        mal(f'tienda.ts: {n_decl} familias declaradas y {len(familias)} parseadas — el parser perdió alguna')
    return familias


def robots_gate():
    spec = importlib.util.spec_from_file_location('robots_gate', ROBOTS_GATE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ------------------------------------------------------------------ estático

def estatico() -> None:
    tiendas = leer_tiendas()
    familias = leer_familias()
    no_es = {lg: t for lg, t in tiendas.items() if lg != 'es'}

    # 1. Sitemap
    cfg = ASTRO_CONFIG.read_text(encoding='utf-8')
    m = re.search(r"/\^\\/\(([a-z|]+)\)\\/\(([a-z|-]+)\)\\/\[\^/\]\+\\/\(access\|library\)\$/", cfg)
    if not m:
        mal('astro.config.mjs: no encuentro el filtro de dashboards anidados de la tienda')
    else:
        langs_cfg, segs_cfg = set(m.group(1).split('|')), set(m.group(2).split('|'))
        if langs_cfg != set(no_es):
            mal(f'sitemap: idiomas {sorted(langs_cfg)} != tienda.ts {sorted(no_es)}')
        elif segs_cfg != {t['seg'] for t in no_es.values()}:
            mal(f'sitemap: segmentos {sorted(segs_cfg)} != tienda.ts {sorted(t["seg"] for t in no_es.values())}')
        else:
            rx = re.compile(m.group(0)[1:-1])
            muestras_fuera = [f'{t["hub"]}/x/{k}' for t in no_es.values() for k in ('access', 'library')]
            muestras_dentro = [t['hub'] for t in no_es.values()] + [f'{t["hub"]}/x' for t in no_es.values()]
            if all(rx.search(p) for p in muestras_fuera) and not any(rx.search(p) for p in muestras_dentro):
                bien(f'sitemap: filtro anidado = {len(segs_cfg)} segmentos de tienda.ts (gate/dashboard fuera, hub/landing dentro)')
            else:
                mal('sitemap: el regex anidado no separa bien dashboards de landings')

    # 2. robots.txt
    rg = robots_gate()
    grupos = rg.parse_robots(ROBOTS.read_text(encoding='utf-8'))
    raw = ROBOTS.read_text(encoding='utf-8')
    bloques = [b for b in re.split(r'\n(?=User-agent:)', raw) if b.startswith('User-agent:')]
    activas = [lg for lg, t in no_es.items() if t['activa']]
    for lg, t in no_es.items():
        lineas = [f'Disallow: {t["hub"]}/*/{k}{v}' for k in ('access', 'library') for v in ('$', '/', '?')]
        presentes = [all(l in b.splitlines() for l in lineas) for b in bloques]
        if t['activa'] and not all(presentes):
            mal(f'robots.txt: tienda {lg} ACTIVA sin sus 6 Disallow en {presentes.count(False)} de {len(bloques)} bloques')
            continue
        if not any(presentes):
            continue  # reservada y sin reglas todavía: correcto
        if not all(presentes):
            mal(f'robots.txt: tienda {lg} con sus Disallow sólo en algunos bloques de user-agent')
            continue
        fallos = []
        for g in grupos:
            for ag in g.agents:
                for p in (f'{t["hub"]}/x/access', f'{t["hub"]}/x/library', f'{t["hub"]}/x/access/',
                          f'{t["hub"]}/x/library?a=1'):
                    if rg.can_fetch(grupos, ag, p):
                        fallos.append(f'{ag} puede {p}')
                for p in (t['hub'], f'{t["hub"]}/x', f'/{lg}/blog/prompt-library-x',
                          f'{t["hub"]}/x/accessories', f'{t["hub"]}/x/library-guide'):
                    if not rg.can_fetch(grupos, ag, p):
                        fallos.append(f'{ag} NO puede {p}')
        if fallos:
            mal(f'robots.txt ({lg}): ' + '; '.join(fallos[:6]))
        else:
            bien(f'robots.txt: tienda {lg} ({"activa" if t["activa"] else "aún inactiva"}) — gate/dashboard '
                 f'bloqueados y hub/landing rastreables en los {len(bloques)} bloques')
    if not activas:
        print('ℹ️  ninguna tienda no-ES activa todavía (la EN se activa en el slice 0.C)')

    # 2-bis. Navegación: TIENDA_NOMBRE (tienda.ts) y los mapas DUPLICADOS de los gemelos React
    # (la SPA no puede importar de astro-site/) == tiendas activas. Si divergen, el header de las
    # landings de marketing enlaza a una tienda que el Header.astro no conoce, o al revés.
    txt = TIENDA_TS.read_text(encoding='utf-8')
    act = {lg: t['hub'] for lg, t in tiendas.items() if t['activa']}
    mn = re.search(r'export const TIENDA_NOMBRE[^{]*\{(.*?)\};', txt, re.S)
    nombres = dict(re.findall(r"([a-z]{2}): '([^']+)'", mn.group(1))) if mn else {}
    if set(nombres) != set(act):
        mal(f'tienda.ts: TIENDA_NOMBRE {sorted(nombres)} != tiendas activas {sorted(act)}')
    for tsx in ('src/components/ModernHeader.tsx', 'src/components/ModernFooter.tsx'):
        src = (REPO / tsx).read_text(encoding='utf-8')
        mp = re.search(r'const TIENDA_PATHS[^{]*\{([^}]*)\}', src)
        mnm = re.search(r'const TIENDA_NOMBRE[^{]*\{([^}]*)\}', src)
        paths = dict(re.findall(r"([a-z]{2}): '([^']+)'", mp.group(1))) if mp else None
        noms = dict(re.findall(r"([a-z]{2}): '([^']+)'", mnm.group(1))) if mnm else None
        if paths != act:
            mal(f'{tsx}: TIENDA_PATHS {paths} != tiendas activas de tienda.ts {act}')
        elif noms != nombres:
            mal(f'{tsx}: TIENDA_NOMBRE {noms} != tienda.ts {nombres}')
        else:
            bien(f'{tsx}: enlace a la tienda = {sorted(act)} (igual que tienda.ts)')

    # 3. Familias con producto vivo fuera de ES
    zona = ZONA_APP.read_text(encoding='utf-8')
    vivos = 0
    for f in familias:
        for lg, p in f['productos'].items():
            if lg == 'es' or not p['vivo']:
                continue
            vivos += 1
            t, slug = tiendas.get(lg), p['slug']
            tag = f'{f["familia"]}/{lg}:{slug}'
            if not t or not t['activa']:
                mal(f'{tag}: producto vivo en una tienda INACTIVA')
                continue
            if not f['productos'].get('es', {}).get('vivo'):
                mal(f'{tag}: sin gemelo ES vivo (el hreflang recíproco no tiene a quién apuntar)')
            if not list((ASTRO / f'src/data/productos-{lg}').glob(f'**/{slug}.ts')):
                mal(f'{tag}: falta astro-site/src/data/productos-{lg}/**/{slug}.ts')
            base = ASTRO / 'src/pages' / lg / t['seg']
            landing = [base / f'{slug}.astro', base / slug / 'index.astro']
            if not any(x.exists() for x in landing):
                mal(f'{tag}: falta la landing ({landing[0].relative_to(REPO)} o …/{slug}/index.astro)')
            for k in ('access', 'library'):
                if not (base / slug / f'{k}.astro').exists():
                    mal(f'{tag}: falta {(base / slug / f"{k}.astro").relative_to(REPO)}')
            if not re.search(r"productId: '" + re.escape(slug) + r"'[^\n]*\blang: '" + lg + "'", zona):
                mal(f"{tag}: falta su entrada en zona-app.ts con lang: '{lg}'")
    if vivos == 0:
        bien(f'familias: {len(familias)} registradas, 0 productos vivos fuera de ES (nada que exigir)')
    elif not any(e.startswith(tuple(f['familia'] for f in familias)) for e in errores):
        bien(f'familias: {vivos} producto(s) vivos fuera de ES con data, páginas y zona-app')


# ------------------------------------------------------------------ red

def get(url: str, intentos: int = 4) -> tuple[int, str]:
    # El CDN de los deploy previews devuelve 500 intermitentes (46 bytes) cuando se le piden
    # varias páginas seguidas: se reintenta con espera creciente antes de dar el fallo.
    req = urllib.request.Request(url, headers={'User-Agent': 'aichef-tienda-gate/1.0'})
    for n in range(intentos):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status, r.read().decode('utf-8', 'replace')
        except urllib.error.HTTPError as e:
            if e.code < 500 or n == intentos - 1:
                return e.code, ''
        except Exception as e:  # noqa: BLE001
            if n == intentos - 1:
                return 0, str(e)
        time.sleep(2 * (n + 1))
    return 0, ''


class TextoVisible(HTMLParser):
    """Texto visible sin <script>, <style>, <noscript> ni el bloque marcado data-lang-es."""
    VACIOS = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.partes: list[str] = []
        self.pila: list[bool] = []  # True = este nivel oculta su contenido

    def handle_starttag(self, tag, attrs):
        if tag in self.VACIOS:
            return
        oculta = tag in ('script', 'style', 'noscript', 'template') or any(k == 'data-lang-es' for k, _ in attrs)
        self.pila.append(oculta or (bool(self.pila) and self.pila[-1]))

    def handle_endtag(self, tag):
        if tag not in self.VACIOS and self.pila:
            self.pila.pop()

    def handle_data(self, data):
        if not (self.pila and self.pila[-1]):
            self.partes.append(data)

    def texto(self) -> str:
        return re.sub(r'\s+', ' ', ' '.join(self.partes))


RESTOS_ES = [' para ', ' con ', ' los ', ' las ', ' del ', ' una ', 'Comprar', 'COMPRAR', 'Garantía', 'Garantia',
             'escandallo', 'Escandallo', 'Productos Digitales', 'Preguntas', 'Reenviar', 'ñ', 'á', 'é', 'í', 'ó', 'ú', '¿', '¡']
# Nombres de idioma que la plantilla enseña a propósito en su lengua (píldoras «Disponible en 7 idiomas»).
EXENTOS = ['Español', 'Français', 'Português', 'Deutsch', 'Italiano', 'Nederlands']
NO_LATINOS = re.compile(r'[Ѐ-ӿ֐-׿؀-ۿ฀-๿぀-ヿ㐀-鿿가-힯]')


def contexto(txt: str, i: int, n: int = 50) -> str:
    return txt[max(0, i - n):i + n].replace('\n', ' ')


def revisar_texto(tag: str, html: str) -> None:
    p = TextoVisible()
    p.feed(html)
    txt = p.texto()
    limpio = txt
    for e in EXENTOS:
        limpio = limpio.replace(e, '')
    if '€' in limpio:
        mal(f'{tag}: «€» en el texto visible → …{contexto(limpio, limpio.index("€"))}…')
    for w in RESTOS_ES:
        if w in limpio:
            mal(f'{tag}: resto de español {w!r} → …{contexto(limpio, limpio.index(w))}…')
            break
    m = NO_LATINOS.search(txt)
    if m:
        mal(f'{tag}: carácter no latino {m.group(0)!r} → …{contexto(txt, m.start())}…')
    if '"priceCurrency":"EUR"' in html:
        mal(f'{tag}: JSON-LD con priceCurrency EUR en una tienda no-ES')
    # Sin compradores en la tienda no-ES todavía: ningún rating en el schema (el SoftwareApplication
    # global del layout lleva uno; el hub EN pasa omitGlobalApp para no heredarlo).
    if 'aggregateRating' in html:
        mal(f'{tag}: JSON-LD con aggregateRating en una tienda no-ES')


def hreflang(html: str) -> dict[str, str]:
    out = {}
    for tag in re.findall(r'<link\b[^>]*>', html):
        if 'rel="alternate"' in tag:
            hl = re.search(r'hreflang="([^"]+)"', tag)
            hr = re.search(r'href="([^"]+)"', tag)
            if hl and hr:
                out[hl.group(1)] = hr.group(1)
    return out


def comprobar_par(base: str, tag: str, lang: str, ruta: str, ruta_es: str) -> None:
    st, html = get(base + ruta)
    if st != 200:
        mal(f'{tag}: {ruta} → HTTP {st}')
        return
    st_es, html_es = get(base + ruta_es)
    if st_es != 200:
        mal(f'{tag}: gemelo ES {ruta_es} → HTTP {st_es}')
    else:
        h, h_es = hreflang(html), hreflang(html_es)
        if h.get('es') != PROD + ruta_es:
            mal(f'{tag}: {ruta} no declara hreflang es={PROD + ruta_es} (tiene {h.get("es")})')
        elif h_es.get(lang) != PROD + ruta:
            mal(f'{tag}: el gemelo ES {ruta_es} no declara hreflang {lang}={PROD + ruta} (tiene {h_es.get(lang)})')
        else:
            bien(f'{tag}: hreflang recíproco {lang}↔es')
    revisar_texto(tag, html)


WA_FLOTANTE = re.compile(r'<a[^>]*href="https://wa\.me/34744717942[^"]*"[^>]*class="[^"]*fixed bottom[^"]*"', re.S)


def comprobar_hubs(base: str, tiendas: dict[str, dict]) -> None:
    """Los hubs de TODAS las tiendas activas (ES incluida) entre sí: hreflang recíproco completo
    (exactamente los idiomas activos, cada uno a su hub, + x-default al ES), canonical propio,
    <html lang> correcto y exactamente 1 botón flotante de WhatsApp."""
    activas = {lg: t for lg, t in tiendas.items() if t['activa']}
    esperado = {lg: PROD + t['hub'] for lg, t in activas.items()}
    esperado['x-default'] = PROD + tiendas['es']['hub']
    for lg, t in activas.items():
        tag = f'hub {lg}'
        st, html = get(base + t['hub'])
        time.sleep(2)
        if st != 200:
            mal(f'{tag}: {t["hub"]} → HTTP {st}')
            continue
        h = hreflang(html)
        if h != esperado:
            faltan = sorted(set(esperado) - set(h))
            sobran = sorted(set(h) - set(esperado))
            malos = sorted(k for k in set(h) & set(esperado) if h[k] != esperado[k])
            mal(f'{tag}: hreflang no recíproco (faltan {faltan}, sobran {sobran}, mal apuntados {malos})')
        else:
            bien(f'{tag}: hreflang = {len(activas)} hubs + x-default→ES')
        can = re.search(r'<link rel="canonical" href="([^"]+)"', html)
        if not can or can.group(1) != PROD + t['hub']:
            mal(f'{tag}: canonical {can.group(1) if can else None} != {PROD + t["hub"]}')
        hl = re.search(r'<html[^>]*\blang="([^"]+)"', html)
        if not hl or hl.group(1) != lg:
            mal(f'{tag}: <html lang={hl.group(1) if hl else None}> (esperado {lg})')
        n_wa = len(WA_FLOTANTE.findall(html))
        if n_wa != 1:
            mal(f'{tag}: {n_wa} botones flotantes de WhatsApp (esperado 1)')
        if lg != 'es':
            revisar_texto(tag, html)


def red(base: str) -> None:
    base = base.rstrip('/')
    tiendas = leer_tiendas()
    familias = leer_familias()
    n = 0
    if any(t['activa'] for lg, t in tiendas.items() if lg != 'es'):
        n += 1
        comprobar_hubs(base, tiendas)
    for f in familias:
        es = f['productos'].get('es')
        for lg, p in f['productos'].items():
            if lg == 'es' or not p['vivo'] or not tiendas[lg]['activa'] or not es:
                continue
            n += 1
            hub = tiendas[lg]['hub']
            tag = f'{f["familia"]}/{lg}'
            comprobar_par(base, tag, lg, f'{hub}/{p["slug"]}', f'/{es["slug"]}')
            for k in ('access', 'library'):
                st, html = get(f'{base}{hub}/{p["slug"]}/{k}')
                if st != 200:
                    mal(f'{tag}: /{k} → HTTP {st}')
                elif not re.search(r'<meta name="robots" content="noindex', html):
                    mal(f'{tag}: /{k} sin meta robots noindex')
                else:
                    bien(f'{tag}: /{k} 200 + noindex')
    if n == 0:
        bien('red: ninguna tienda no-ES activa ni producto vivo fuera de ES — nada que comprobar')


# ------------------------------------------------------------------ ES idéntico

def normalizar(html: str, base: str) -> str:
    host = re.escape(base.rstrip('/').split('://', 1)[-1])
    html = re.sub(r'https?://' + host, PROD, html)
    html = re.sub(r'(/_astro/[\w.@-]+?)\.[A-Za-z0-9_-]{8}\.(js|css|mjs)', r'\1.X.\2', html)
    html = re.sub(r'astro-cid-[a-z0-9]+', 'astro-cid-X', html)
    # Inyección de Netlify SOLO en los deploy previews (barra de colaboración): no es del sitio.
    html = re.sub(r'<div data-netlify-deploy-id="[^"]*".*?</div>\n', '', html, flags=re.S)
    return html


def es_identico(base: str) -> None:
    iguales = 0
    for ruta in KITEXCEL_ES:
        st_p, prev = get(base.rstrip('/') + ruta)
        st_l, live = get(PROD + ruta)
        if st_p != 200 or st_l != 200:
            mal(f'{ruta}: HTTP preview {st_p} / producción {st_l}')
            continue
        a, b = normalizar(prev, base), normalizar(live, PROD)
        if a == b:
            iguales += 1
            bien(f'{ruta}: byte a byte idéntico ({len(a)} bytes normalizados)')
            continue
        i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
        mal(f'{ruta}: DIFIERE en el byte {i} (preview {len(a)} / producción {len(b)} bytes)\n'
            f'     preview   : …{a[max(0, i - 120):i + 120]!r}…\n'
            f'     producción: …{b[max(0, i - 120):i + 120]!r}…')
    print(f'\n{iguales}/{len(KITEXCEL_ES)} landings ES idénticas')


# ------------------------------------------------------------------ main

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--base', help='URL del deploy a comprobar (preview o producción)')
    ap.add_argument('--es-identico', action='store_true',
                    help='compara las 5 landings ES KitExcel del --base contra producción')
    a = ap.parse_args()
    if a.es_identico:
        if not a.base:
            ap.error('--es-identico necesita --base <preview>')
        es_identico(a.base)
    elif a.base:
        red(a.base)
    else:
        estatico()
    print(f'\n{"❌ " + str(len(errores)) + " fallo(s)" if errores else "✅ tienda-gate en verde"}')
    return 1 if errores else 0


if __name__ == '__main__':
    sys.exit(main())
