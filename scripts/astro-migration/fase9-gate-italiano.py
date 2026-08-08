#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gate del árbol ITALIANO de aichef.pro (Fase 9).

Nace del 2026-08-08, cuando una auditoría descubrió que 52 de las 83 URLs
italianas servían título, meta description y CUERPO ENTERO en castellano bajo
`<html lang="it">`, con index,follow y hreflang recíproco con su gemela
española. En inglés eran 0 de 83. La causa no era una sola: había castellano
llegando por CUATRO vías distintas, y ninguna se veía en un diff de claves.

    1. Backfill de datos      — use-cases.ts hacía `IT[id] ?? es`
    2. Fallback de i18n       — translations.ts cae al español si falta la clave
    3. Copy hardcodeado       — COPY/UI definidos sólo para es/en en un .astro
    4. Esquema de claves      — la traducción existía, colgada de otro árbol

Este gate mide el RESULTADO en el HTML, no la intención en el código, porque
sólo el HTML sabe cuál de las cuatro vías se coló.

Dos niveles, a propósito:
  ⛔ ERROR   — objetivo y verificable (castellano en el HTML, acento italiano
               mal puesto, carácter de otro alfabeto, clave i18n ausente,
               nombre de agente que no existe en la plataforma). Falla el gate.
  ⚠  REVISAR — lo que una máquina no puede sentenciar (un agente citado que no
               está en el catálogo italiano puede ser una decisión pendiente,
               no un error). Se lista para leerlo a ojo.

Uso:
    python3 scripts/astro-migration/fase9-gate-italiano.py              # sobre el dist
    python3 scripts/astro-migration/fase9-gate-italiano.py --produccion # contra aichef.pro
    python3 scripts/astro-migration/fase9-gate-italiano.py --sin-red    # sin tocar la red

El modo por defecto necesita un build reciente en astro-site/dist.
"""
import argparse
import concurrent.futures
import html as _html
import json
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DIST = REPO / 'astro-site' / 'dist'
LOCALES = REPO / 'src' / 'i18n' / 'locales'
SITE = 'https://aichef.pro'
PLATAFORMA_IT = 'https://itapp.aichef.pro/ospite'

# ── 1. Castellano ────────────────────────────────────────────────────────────
# Marcadores que en italiano NO existen o serían falta grave. Cada uno costó una
# medición: los que están comentados son FALSOS POSITIVOS comprobados el
# 2026-08-08 y NO deben volver a añadirse sin releer esta nota.
#
#   'gratis'      → es palabra italiana correcta («prova gratis»).
#   'ñ'           → sale en apellidos de testimonio (Castaño, Núñez, Iñaki), en
#                   «Albariño» y en la terminología peruana (criolla, costeña,
#                   andina, amazónica). Todos correctos en un texto italiano.
#   'Restaurante' → es el nombre de PRODUCTO «Kit de Tareas Restaurante Casual»,
#                   que se vende así y no se traduce (decisión de John).
#   'Cocina'      → aparece dentro de nombres propios de agente.
MARCADORES_ES = [
    '¿', '¡',
    'Descubre', 'Empieza gratis', 'Ahorra un', 'Reserva tu', 'Elige el',
    'Explorar Agente', 'Ver caso de uso', 'Sin tarjeta',
    'Creatividad Culinaria', 'Recetarios Mundiales', 'Recetarios de',
    'Conceptos de Negocio', 'Proveedores Gastro', 'Contenidos y RRSS',
    'Herramientas y Utilities', 'Gastro Conocimiento', 'Modelos IA + LLM',
    'Gerentes de Restaurantes', 'Chefs de Cocina',
    'ción ', 'ciones ', 'miento de', ' para el ', ' del restaurante',
    ' que el ', ' los que ', ' las que ', 'Preguntas Frecuentes',
]

# ── 2. Acentuación italiana ──────────────────────────────────────────────────
# El error más visible y más frecuente de un italiano generado por máquina.
ACENTOS = {
    'perche': 'perché', 'piu': 'più', 'gia': 'già', 'cosi': 'così',
    'puo': 'può', 'percio': 'perciò', 'cioe': 'cioè', 'sara': 'sarà',
    'citta': 'città', 'qualita': 'qualità', 'attivita': 'attività',
    'possibilita': 'possibilità', 'novita': 'novità', 'realta': 'realtà',
    'meta': None,   # 'meta' sin acento existe (meta = objetivo) → sólo REVISAR
}
RE_ACENTO = re.compile(r'\b(' + '|'.join(k for k, v in ACENTOS.items() if v) + r')\b')

# ── 2b. Rutas que son ES-only POR DISEÑO ─────────────────────────────────────
# No son fugas: son decisiones de producto que afectan por igual a los 6 idiomas
# no españoles (el inglés tampoco las tiene). Enlazarlas desde /it es lo
# esperado, así que no deben ensuciar el informe.
#   · Productos digitales (~120 páginas): kit-*, pack-*, plan-*, guia-*,
#     mega-pack-*, pro-prompts-*, productos-digitales. Ver
#     PRODUCTOS_DIGITALES_PENDIENTE.md.
#   · pSEO por ciudad (76 URLs): sólo español por decisión explícita en
#     src/lib/pseo-cities.ts.
#   · /blog y /blog/*: fallback documentado de blogHubHref() mientras no exista
#     blog italiano. En cuanto exista, QUITAR de esta lista para que el gate
#     empiece a exigir /it/blog.
#   · /libreria-de-prompts: el hub de librerías no tiene versión italiana
#     todavía; promptHubHref() cae al español a propósito.
RE_ES_POR_DISENO = re.compile(
    r'^/('
    r'kit-|pack-|plan-|guia-|mega-pack-|pro-prompts-|productos-digitales|'
    r'abrir-restaurante|escandallo-restaurante|licencia-restaurante|'
    r'plan-negocio-restaurante|software-gestion-restaurante|'
    r'seo-restaurantes-por-ciudad|'
    r'blog|libreria-de-prompts|formacion-presencial|'
    # /contacto sólo existe en español — tampoco hay /en/contact. Afecta por
    # igual a los 6 idiomas, así que no es un defecto italiano; queda anotado
    # como gap del sitio, no del árbol /it.
    r'contacto'
    r')'
)

# ── 3. Otros alfabetos ───────────────────────────────────────────────────────
# Los 7 idiomas del grupo son de alfabeto latino: cualquier cosa de aquí dentro
# es contaminación del modelo. Mismo criterio que guard_idioma() de bridge.py.
RE_NO_LATINO = re.compile(
    "[　-〿぀-ヿ㐀-䶿一-鿿豈-﫿"
    "＀-￯가-힯Ѐ-ӿԀ-ԯ֐-׿"
    "؀-ۿ฀-๿]"
)


def texto_visible(h):
    t = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', h, flags=re.S)
    t = _html.unescape(re.sub(r'<[^>]+>', ' ', t))
    return re.sub(r'\s+', ' ', t)


def paginas_dist():
    if not DIST.exists():
        sys.exit(f'no hay build en {DIST} — corre antes: cd astro-site && npm run build')
    return [DIST / 'it.html'] + sorted(DIST.glob('it/**/*.html'))


def paginas_produccion():
    sm = urllib.request.urlopen(f'{SITE}/sitemap-0.xml', timeout=60).read().decode()
    return [u for u in re.findall(r'<loc>(.*?)</loc>', sm)
            if re.match(rf'{SITE}/it(/|$)', u)]


def baja(url):
    try:
        return urllib.request.urlopen(url, timeout=60).read().decode('utf-8', 'replace')
    except Exception as exc:                                   # noqa: BLE001
        return f'<!--ERROR {exc}-->'


def catalogo_italiano():
    """Los nombres de agente que sirve HOY la plataforma. Fuente autorizada."""
    try:
        h = baja(PLATAFORMA_IT)
        pares = re.findall(r'"formid"\s*:\s*"[^"]+"\s*,\s*"formtitle"\s*:\s*"([^"]+)"', h)
        return {p.strip().replace('\\u0026', '&') for p in pares}
    except Exception:                                          # noqa: BLE001
        return set()


def hojas(o, p=''):
    out = {}
    if isinstance(o, dict):
        for k, v in o.items():
            out.update(hojas(v, f'{p}.{k}' if p else k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            out.update(hojas(v, f'{p}[{i}]'))
    else:
        out[p] = o
    return out


def revisa_claves():
    """Vía 2 y 4: clave ausente → translations.ts la pinta en ESPAÑOL."""
    errores, avisos = [], []
    es = hojas(json.loads((LOCALES / 'es.json').read_text(encoding='utf-8')))
    it = hojas(json.loads((LOCALES / 'it.json').read_text(encoding='utf-8')))
    faltan = sorted(set(es) - set(it))
    if faltan:
        errores.append(('i18n', f'{len(faltan)} claves de es.json faltan en it.json '
                                f'(se pintarán en CASTELLANO): {faltan[:8]}'))
    huerfanas = sorted(set(it) - set(es))
    if huerfanas:
        avisos.append(('i18n', f'{len(huerfanas)} claves de it.json no existen en es.json. '
                               f'Suelen ser restos de un esquema viejo que nadie lee: '
                               f'{huerfanas[:6]}'))
    # Valor idéntico al español en cadenas largas: sospechoso de no traducido.
    iguales = [k for k in set(es) & set(it)
               if isinstance(es[k], str) and es[k] == it[k] and len(es[k]) > 25]
    if iguales:
        avisos.append(('i18n', f'{len(iguales)} cadenas largas idénticas al español '
                               f'(pueden ser nombres propios): {iguales[:5]}'))
    return errores, avisos


def revisa_pagina(ident, h):
    """Vías 1 y 3: lo que acabó en el HTML, venga de donde venga."""
    errores, avisos = [], []
    if h.startswith('<!--ERROR'):
        errores.append((ident, f'no se pudo descargar: {h[:90]}'))
        return errores, avisos
    t = texto_visible(h)

    hits = {m: t.count(m) for m in MARCADORES_ES if m in t}
    if hits:
        primero = next(iter(hits))
        i = t.find(primero)
        errores.append((ident, f'castellano {hits} · …{t[max(0, i - 60):i + 60]}…'))

    mal = RE_ACENTO.findall(t)
    if mal:
        errores.append((ident, f'acentos italianos sin tilde: '
                               f'{sorted({m: ACENTOS[m] for m in mal}.items())[:5]}'))

    raros = RE_NO_LATINO.findall(h)
    if raros:
        nombres = []
        for c in raros[:4]:
            try:
                nombres.append(f'{c!r} ({unicodedata.name(c)})')
            except ValueError:
                nombres.append(repr(c))
        errores.append((ident, f'{len(raros)} caracteres de otro alfabeto: {nombres}'))

    if 'lang="it"' not in h and '<!--ERROR' not in h:
        errores.append((ident, 'el <html> no declara lang="it"'))

    # Enlace con etiqueta italiana que aterriza en una página española. Se
    # exime lo que es ES-only POR DISEÑO, no por descuido: los ~120 productos
    # digitales y las 76 URLs de pSEO por ciudad no existen en ningún otro
    # idioma (tampoco en inglés), y el blog ES es el fallback documentado de
    # blogHubHref() mientras no haya blog italiano.
    for href in set(re.findall(r'href="(/[a-z0-9\-/]+)"', h)):
        if href.startswith('/it/') or href == '/it':
            continue
        if re.match(r'^/(en|fr|de|pt|nl)(/|$)', href) or href == '/':
            continue
        if RE_ES_POR_DISENO.match(href):
            continue
        avisos.append((ident, f'enlace a una ruta sin prefijo /it: {href}'))
    return errores, avisos


def revisa_agentes(paginas_html, catalogo):
    """Un agente citado que no existe en itapp es fricción justo tras el clic."""
    if not catalogo:
        return [], [('agentes', 'no se pudo leer el catálogo de itapp.aichef.pro '
                                '— comprobación omitida')]
    blob = ' '.join(paginas_html)
    # Nombres de agente conocidos que NO están en la plataforma italiana.
    sospechosos = ['Gastro Calendar', 'InstaFlow AI Pro', 'MenuDish Local SEO',
                   'Calcula Pax', 'BlogPost SEO Gen+', 'Keyword Discovery AI+',
                   'Conversor Ing', 'PinterAI Content Pro', 'GastroIMG Gen+']
    avisos = []
    for n in sospechosos:
        c = blob.count(n)
        if c and n not in catalogo:
            avisos.append(('agentes', f'«{n}» se cita {c} veces y NO está en la '
                                      f'plataforma italiana (ver CATALOGO_ITALIANO_PENDIENTE.md)'))
    # Nombres claramente españoles que deberían ir traducidos.
    for es_n, it_n in [('Gerente de Restaurante Pro', 'Manager Ristorante Pro'),
                       ('Mermas GenCal', 'Sprechi GenCal'),
                       ('ID Alérgenos', 'ID Allergeni'),
                       ('¿Quién Soy?', 'Chi sono?'),
                       ('Cocina Creativa', 'Cucina Creativa'),
                       ('Casual Restaurants AI+', 'Ristoranti Casual AI+')]:
        if es_n in blob:
            return ([('agentes', f'«{es_n}» aparece sin traducir; el nombre oficial '
                                 f'italiano es «{it_n}»')], avisos)
    return [], avisos


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--produccion', action='store_true',
                    help='mide contra aichef.pro en vez del dist local')
    ap.add_argument('--sin-red', action='store_true',
                    help='omite lo que necesita red (catálogo de agentes)')
    args = ap.parse_args()

    errores, avisos = [], []

    e, a = revisa_claves()
    errores += e
    avisos += a

    if args.produccion:
        urls = paginas_produccion()
        print(f'midiendo {len(urls)} URLs italianas de PRODUCCIÓN…')
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
            htmls = list(ex.map(baja, urls))
        pares = list(zip([u.replace(SITE, '') for u in urls], htmls))
    else:
        ps = paginas_dist()
        print(f'midiendo {len(ps)} páginas italianas del dist…')
        pares = [(str(p.relative_to(DIST)), p.read_text(encoding='utf-8')) for p in ps]

    for ident, h in pares:
        e, a = revisa_pagina(ident, h)
        errores += e
        avisos += a

    if not args.sin_red:
        e, a = revisa_agentes([h for _, h in pares], catalogo_italiano())
        errores += e
        avisos += a

    limpias = len(pares) - len({i for i, _ in errores if i not in ('i18n', 'agentes')})
    print(f'\n  páginas sin un solo problema: {limpias} de {len(pares)}')

    if avisos:
        print(f'\n⚠  REVISAR ({len(avisos)})')
        for ident, m in avisos[:30]:
            print(f'   · {ident}: {m}')
        if len(avisos) > 30:
            print(f'   … y {len(avisos) - 30} más')

    if errores:
        print(f'\n⛔ ERROR ({len(errores)})')
        for ident, m in errores[:40]:
            print(f'   · {ident}: {m}')
        if len(errores) > 40:
            print(f'   … y {len(errores) - 40} más')
        print('\nGATE ROJO')
        sys.exit(1)

    print('\nGATE VERDE')
    sys.exit(0)


if __name__ == '__main__':
    main()
