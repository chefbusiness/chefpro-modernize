#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CRO home (Keak, 20-sep-2026) — GATE del HTML servido: comprueba que las tres
secciones v2 están en las 7 portadas, la pricing v2 en las 7 páginas de precios y
en las 112 páginas con island de precios, y que no quedan restos de la versión vieja.

Funciona contra un directorio `dist/` (VPS, tras `astro build`) o contra una URL base
(deploy preview de Netlify / producción) con `--base`. No usa navegador: sólo HTML.

Qué exige por página (marcadores que emiten los componentes, ver CRO_HOME_KEAK_2026-09-20.md §5):
  · portada: 1× data-keak="hero-v2", 1× data-keak="business-v2", 1× data-keak="pricing-v2"
  · pricing-v2: 5 tarjetas data-plan (member, premium-pro/premium_pro…), 4 data-role-chip,
    EXACTAMENTE 1 data-popular y que sea premium_plus, 5 CTAs con utm_content de plan,
    0 claves i18n crudas («v2_» literal en el texto = traducción que faltó)
  · restos: 0× class="popular-plan" (pricing viejo), 0× data-app-url (business viejo),
    0× «SEE RESOURCES»/«VER RECURSOS» en el hero (cambio 1 lo quitó)
  · hero-v2: el H1 contiene hero-dynamic-word y la sección hero enlaza a la página de precios del idioma
  · 50+ (no 75+) en fr/de/it/pt/nl dentro de pricing-v2 y hero-v2
Uso:
    python3 keak-dist-gate.py                      # astro-site/dist local (VPS)
    python3 keak-dist-gate.py --base https://deploy-preview-86--aichefpro.netlify.app
"""
import argparse, json, re, sys, urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DIST = RAIZ / 'astro-site' / 'dist'
LANGS = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl']
HOME = {'es': '/', 'en': '/en', 'fr': '/fr', 'de': '/de', 'it': '/it', 'pt': '/pt', 'nl': '/nl'}
PRICING = {'es': '/precios', 'en': '/en/pricing', 'fr': '/fr/tarifs', 'de': '/de/preise',
           'it': '/it/prezzi', 'pt': '/pt/precos', 'nl': '/nl/prijzen'}
SECUNDARIOS = {'fr', 'de', 'it', 'pt', 'nl'}
PLANES = ['member', 'premium_pro', 'premium_plus', 'premium_max', 'premium_plus_annual']
SLUGS = ['member', 'premium-pro', 'premium-plus', 'premium-max', 'premium-max-annual']


def rutas_islands():
    """Las páginas Astro que montan un island con bloque de precios (8 landings + 6 tools) × 7."""
    pages = RAIZ / 'astro-site' / 'src' / 'pages'
    islas = ('ReducirCostesRestaurante|ChatGPTRestaurantes|MenuRestaurante|RecetasIARestaurantes|'
             'SoftwareGestionCocina|EscandallosRestaurante|HerramientasIARestaurantes|MarketingRestaurante|'
             'CalendarioContenidos|TestDigitalizacion|GeneradorMenuDegustacion|CalculadoraBrigada|'
             'DetectorAlergenos|GeneradorTextosCarta')
    out = []
    for p in pages.rglob('*.astro'):
        if re.search('(?:' + islas + ')Island', p.read_text(encoding='utf-8')):
            rel = p.relative_to(pages).with_suffix('')
            out.append('/' + str(rel).replace('\\', '/'))
    return sorted(out)


def leer(base, ruta):
    if base:
        url = base.rstrip('/') + ruta
        req = urllib.request.Request(url, headers={'User-Agent': 'keak-dist-gate/1.0'})
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.read().decode('utf-8', 'replace')
    # build.format 'file': /en -> en.html, / -> index.html, /precios -> precios.html
    rel = ruta.strip('/')
    cand = [DIST / (rel + '.html') if rel else DIST / 'index.html', DIST / rel / 'index.html']
    for c in cand:
        if c.exists():
            return c.read_text(encoding='utf-8')
    raise FileNotFoundError(ruta)


def lang_de(ruta):
    m = re.match(r'^/(en|fr|de|it|pt|nl)(/|$)', ruta)
    return m.group(1) if m else 'es'


def seccion(html, marcador):
    """Recorta desde data-keak="X" hasta el cierre de SU <section> (ninguna de las
    tres anida secciones). Recortar «hasta el siguiente data-keak» arrastraba las
    secciones intermedias (FeaturedApps lleva data-app-url) y daba falsos positivos."""
    i = html.find(f'data-keak="{marcador}"')
    if i < 0:
        return ''
    j = html.find('</section>', i)
    return html[i:j if j > 0 else None]


def revisar_pricing(html, lang, errores, ruta):
    s = seccion(html, 'pricing-v2')
    if not s:
        errores.append(f'{ruta}: falta pricing-v2'); return
    for p in PLANES:
        if f'data-plan="{p}"' not in s:
            errores.append(f'{ruta}: falta tarjeta {p}')
    # Sólo los <a data-role-chip>: el selector del script inline también contiene la cadena.
    chips = len(re.findall(r'<a[^>]*\bdata-role-chip', s))
    if chips != 4:
        errores.append(f'{ruta}: {chips} chips de rol (esperados 4)')
    pop = re.findall(r'<article[^>]*data-plan="([^"]+)"[^>]*data-popular|<article[^>]*data-popular[^>]*data-plan="([^"]+)"', s)
    pops = [a or b for a, b in pop]
    if pops != ['premium_plus']:
        errores.append(f'{ruta}: data-popular en {pops} (esperado solo premium_plus)')
    for slug in SLUGS:
        if f'utm_content={slug}' not in s:
            errores.append(f'{ruta}: falta CTA utm_content={slug}')
    cruda = re.search(r'>[^<]*\bv2_[a-z_]+', s)
    if cruda:
        errores.append(f'{ruta}: clave i18n cruda en pricing-v2: {cruda.group(0)[:60]!r}')
    if lang in SECUNDARIOS and '75+' in re.sub(r'<[^>]+>', ' ', s):
        errores.append(f'{ruta}: «75+» en pricing-v2 de un idioma que anuncia 50+')
    if 'class="popular-plan' in html or "popular-plan " in html:
        errores.append(f'{ruta}: resto del pricing viejo (.popular-plan)')


def revisar_home(html, lang, errores, ruta):
    for m in ('hero-v2', 'business-v2', 'pricing-v2'):
        veces = html.count('data-keak="%s"' % m)
        if veces != 1:
            errores.append(f'{ruta}: data-keak={m} aparece {veces} veces')
    h = seccion(html, 'hero-v2')
    if h:
        if 'id="hero-dynamic-word"' not in h:
            errores.append(f'{ruta}: hero sin palabra rotatoria')
        if f'href="{PRICING[lang]}"' not in h:
            errores.append(f'{ruta}: el hero no enlaza a {PRICING[lang]}')
        if re.search(r'SEE RESOURCES|VER RECURSOS', h):
            errores.append(f'{ruta}: sigue el botón de recursos en el hero')
        texto = re.sub(r'<[^>]+>', ' ', h)
        if lang in SECUNDARIOS and '75+' in texto:
            errores.append(f'{ruta}: «75+» en el hero de un idioma que anuncia 50+')
        if re.search(r'\bv2_[a-z_]+', texto):
            errores.append(f'{ruta}: clave i18n cruda en hero-v2')
    b = seccion(html, 'business-v2')
    if b:
        if b.count('data-tool=') != 6:
            errores.append(f'{ruta}: business-v2 con {b.count("data-tool=")} herramientas (esperadas 6)')
        if 'data-app-url' in b:
            errores.append(f'{ruta}: business-v2 conserva botones viejos (data-app-url)')
        if f'href="{PRICING[lang]}"' not in b:
            errores.append(f'{ruta}: business-v2 no enlaza a {PRICING[lang]}')
        if re.search(r'\bv2_[a-z_]+', re.sub(r'<[^>]+>', ' ', b)):
            errores.append(f'{ruta}: clave i18n cruda en business-v2')
    revisar_pricing(html, lang, errores, ruta)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', help='URL base (preview/producción); sin ella lee astro-site/dist')
    ap.add_argument('--solo-home', action='store_true')
    a = ap.parse_args()
    errores, n = [], 0
    for lang in LANGS:
        ruta = HOME[lang]
        try:
            revisar_home(leer(a.base, ruta), lang, errores, ruta); n += 1
        except Exception as e:
            errores.append(f'{ruta}: no se pudo leer ({e})')
    if not a.solo_home:
        for lang in LANGS:
            ruta = PRICING[lang]
            try:
                revisar_pricing(leer(a.base, ruta), lang, errores, ruta); n += 1
            except Exception as e:
                errores.append(f'{ruta}: no se pudo leer ({e})')
        islas = rutas_islands()
        for ruta in islas:
            try:
                revisar_pricing(leer(a.base, ruta), lang_de(ruta), errores, ruta); n += 1
            except Exception as e:
                errores.append(f'{ruta}: no se pudo leer ({e})')
        print(f'islands con precios censados: {len(islas)}')
    if errores:
        print('\n'.join(errores))
        print(f'\n✗ GATE dist: {len(errores)} errores en {n} páginas')
        return 1
    print(f'✓ GATE dist: {n} páginas, todas con la v2 completa y sin restos')
    return 0


if __name__ == '__main__':
    sys.exit(main())
