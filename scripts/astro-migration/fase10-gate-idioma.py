#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gate de los árboles de idioma NO españoles (Fase 10): fr, de, pt, nl.

Es la generalización de fase9-gate-italiano.py (que queda intacto y sigue
siendo el del italiano): mismo motor —mide el RESULTADO en el HTML, no la
intención en el código, porque el castellano llegaba por cuatro vías que
ningún diff de claves ve—, con la configuración por idioma separada.

    python3 scripts/astro-migration/fase10-gate-idioma.py --lang fr             # dist
    python3 scripts/astro-migration/fase10-gate-idioma.py --lang fr --produccion
    python3 scripts/astro-migration/fase10-gate-idioma.py --lang fr --sin-red

Dos niveles, como el italiano:
  ⛔ ERROR   — objetivo y verificable (castellano en el HTML, acento del idioma
               mal puesto, carácter de otro alfabeto, clave i18n ausente,
               nombre de agente español sin traducir teniendo nombre oficial).
  ⚠  REVISAR — lo que una máquina no puede sentenciar (agente citado que no
               está en el catálogo del idioma = decisión de catálogo pendiente).

⚠ de/pt/nl llevan la config mínima: ANTES de lanzar su homologación hay que
completar sus marcadores/acentos con el mismo método que el francés (leer los
falsos positivos del comentario de cada bloque ANTES de añadir nada).
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

# Marcadores de castellano comunes a TODOS los idiomas destino: frases de UI y
# taxonomías que sólo existen en español. (El detalle fino —caracteres, palabras
# función— va por idioma, porque lo que es marcador en uno es legítimo en otro.)
MARCADORES_COMUNES = [
    '¿', '¡',
    'Descubre', 'Empieza gratis', 'Ahorra un', 'Reserva tu', 'Elige el',
    'Explorar Agente', 'Ver caso de uso', 'Sin tarjeta',
    'Creatividad Culinaria', 'Recetarios Mundiales', 'Recetarios de',
    'Conceptos de Negocio', 'Proveedores Gastro', 'Contenidos y RRSS',
    'Herramientas y Utilities', 'Gastro Conocimiento', 'Modelos IA + LLM',
    'Gerentes de Restaurantes', 'Chefs de Cocina',
    'Preguntas Frecuentes', 'miento de', ' para el ', ' del restaurante',
]

CONFIG = {
    'fr': {
        'plataforma': 'https://frapp.aichef.pro/guest',
        'doc_catalogo': 'CATALOGO_ITALIANO_PENDIENTE.md (la decisión es pentalingüe)',
        # Falsos positivos YA COMPROBADOS que NO deben volver como marcadores:
        #   'ción '  → como secuencia suelta sí es marcador (abajo), pero cuidado
        #              con recortarla: «attention», «réduction» llevan 'tion'.
        #   'ñ'      → apellidos de testimonios (Castaño, Núñez) y «Albariño»,
        #              legítimos en la página francesa (testimonialAuthor va
        #              verbatim). Mismo falso positivo que cazó el gate italiano.
        #   'Restaurante', 'Cocina' → nombres de PRODUCTO y de agente español
        #              citados a propósito (Kit de Tareas…, agente sin versión fr).
        'marcadores': [' ción', 'ción ', 'cción',
                       ' y la ', ' y el ', ' con el ', ' con la ',
                       ' los que ', ' las que ', ' que el ', ' desde el '],
        # El error más frecuente del francés generado a máquina: tildes fuera.
        # OJO falsos positivos si algún día se amplía: 'cote' (Côte/cote bursátil),
        # 'marche' (marché/marche), 'sale' (salé/sale) — NO añadirlos.
        'acentos': {'tres': 'très', 'deja': 'déjà', 'apres': 'après',
                    'cout': 'coût', 'couts': 'coûts', 'gout': 'goût',
                    'etre': 'être', 'equipe': 'équipe', 'equipes': 'équipes',
                    'menage': 'ménage', 'debut': 'début', 'creativite': 'créativité',
                    'qualite': 'qualité', 'realite': 'réalité', 'securite': 'sécurité'},
        'agentes_es_fr': [('Gerente de Restaurante Pro', 'Manager de Restaurant Pro'),
                          ('Mermas GenCal', 'Rendement GenCal'),
                          ('ID Alérgenos', 'ID Allergènes'),
                          ('¿Quién Soy?', 'Qui suis-je ?'),
                          ('Cocina Creativa', 'Cuisine Créative'),
                          ('Casual Restaurants AI+', 'Restaurants Décontractés AI+'),
                          ('Comida de Personal', 'Repas du Personnel'),
                          ('Catering AI+', 'Traiteur IA+')],
    },
    'de': {
        'plataforma': 'https://deapp.aichef.pro/guest',
        'doc_catalogo': 'CATALOGO_ITALIANO_PENDIENTE.md (la decisión es pentalingüe)',
        # Falsos positivos a NO reintroducir: 'ñ' (Jalapeño, Roscón en textos DE
        # legítimos → allowlist), 'für'-sin-umlaut como 'fur' (colisiona con
        # inglés), 'Uber' (marca). El alemán no usa á í ó ú ñ salvo préstamos.
        'marcadores': ['ción', 'cción', ' y la ', ' y el ', ' con el ',
                       ' los que ', ' que el ', ' desde el '],
        # Umlauts caídos típicos de traducción a máquina. Lista corta a propósito:
        # solo palabras donde la variante sin umlaut NO existe en alemán.
        'acentos': {'Kuche': 'Küche', 'kuche': 'küche', 'Kuchenchef': 'Küchenchef',
                    'Speisekarte': None, 'Menu': None,   # None = no comprobar (ambiguas)
                    'Getranke': 'Getränke', 'Qualitat': 'Qualität',
                    'Kalkulationsblatter': 'Kalkulationsblätter'},
        'agentes_es_fr': [('Gerente de Restaurante Pro', 'Profi Restaurantmanager'),
                          ('Mermas GenCal', 'Lebensmittelabfälle AI'),
                          ('ID Alérgenos', 'Allergen-ID'),
                          ('¿Quién Soy?', 'Wer sind Sie?'),
                          ('Cocina Creativa', 'Kreativküche'),
                          ('Comida de Personal', 'Mitarbeiteressen AI'),
                          ('Chef Ejecutivo Pro', 'Executive Chef Pro')],
    },
    'pt': {
        'plataforma': 'https://ptapp.aichef.pro/guest',
        'doc_catalogo': 'CATALOGO_ITALIANO_PENDIENTE.md (la decisión es pentalingüe)',
        # ⚠ En portugués á í ó ú son LEGÍTIMOS y «ção» es lo correcto: los
        # marcadores de castellano deben ser léxicos, no de caracteres.
        'marcadores': ['ción', 'cción'],
        'acentos': {},
        'agentes_es_fr': [],
    },
    'nl': {
        'plataforma': 'https://nlapp.aichef.pro/guest',
        'doc_catalogo': 'CATALOGO_ITALIANO_PENDIENTE.md (la decisión es pentalingüe)',
        'marcadores': ['ción', 'cción'],
        'acentos': {},
        'agentes_es_fr': [],
    },
}

# Agentes conocidos que NO existen fuera de es/en: si se citan, es la decisión
# de catálogo pendiente, no un bug de la traducción (que es fiel a propósito).
AGENTES_SOSPECHOSOS = ['Gastro Calendar', 'InstaFlow AI Pro', 'MenuDish Local SEO',
                       'Calcula Pax', 'BlogPost SEO Gen+', 'Keyword Discovery AI+',
                       'Conversor Ing', 'PinterAI Content Pro', 'GastroIMG Gen+']

# Rutas ES-only POR DISEÑO (misma lista y misma razón que el gate italiano):
# productos digitales, pSEO por ciudad, blog (fallback documentado de
# blogHubHref para idiomas sin blog propio), hub de librerías, formación.
RE_ES_POR_DISENO = re.compile(
    r'^/('
    r'kit-|pack-|plan-|guia-|mega-pack-|pro-prompts-|productos-digitales|'
    r'abrir-restaurante|escandallo-restaurante|licencia-restaurante|'
    r'plan-negocio-restaurante|software-gestion-restaurante|'
    r'seo-restaurantes-por-ciudad|'
    r'blog|libreria-de-prompts|formacion-presencial|contacto'
    r')'
)

RE_NO_LATINO = re.compile(
    "[　-〿぀-ヿ㐀-䶿一-鿿豈-﫿"
    "＀-￯가-힯Ѐ-ӿԀ-ԯ֐-׿"
    "؀-ۿ฀-๿]"
)


def cadenas_productos():
    """Nombres y descripciones ES de products-catalog.ts: los productos digitales
    son ES-only POR DISEÑO (decisión de John) y sus tarjetas pintan español en
    los 7 idiomas — no son una fuga del árbol de idioma. Se enmascaran antes de
    buscar castellano, de largo a corto."""
    src = (REPO / 'src/data/products-catalog.ts').read_text(encoding='utf-8')
    lits = re.findall(r"(?:es|name)\s*:\s*'([^']{4,120})'", src)
    lits += re.findall(r'(?:es|name)\s*:\s*"([^"]{4,120})"', src)
    return sorted(set(lits), key=len, reverse=True)


PRODUCTOS_ES = None


def texto_visible(h):
    t = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', h, flags=re.S)
    t = _html.unescape(re.sub(r'<[^>]+>', ' ', t))
    return re.sub(r'\s+', ' ', t)


def baja(url):
    try:
        return urllib.request.urlopen(url, timeout=60).read().decode('utf-8', 'replace')
    except Exception as exc:                                   # noqa: BLE001
        return f'<!--ERROR {exc}-->'


def catalogo_plataforma(url):
    try:
        h = baja(url)
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


def revisa_claves(lang):
    errores, avisos = [], []
    es = hojas(json.loads((LOCALES / 'es.json').read_text(encoding='utf-8')))
    xx = hojas(json.loads((LOCALES / f'{lang}.json').read_text(encoding='utf-8')))
    faltan = sorted(set(es) - set(xx))
    if faltan:
        errores.append(('i18n', f'{len(faltan)} claves de es.json faltan en {lang}.json '
                                f'(se pintarán en CASTELLANO): {faltan[:8]}'))
    iguales = [k for k in set(es) & set(xx)
               if isinstance(es[k], str) and es[k] == xx[k] and len(es[k]) > 25]
    if iguales:
        avisos.append(('i18n', f'{len(iguales)} cadenas largas idénticas al español '
                               f'(pueden ser nombres propios): {iguales[:5]}'))
    return errores, avisos


def revisa_pagina(ident, h, lang, cfg, re_acento):
    errores, avisos = [], []
    if h.startswith('<!--ERROR'):
        errores.append((ident, f'no se pudo descargar: {h[:90]}'))
        return errores, avisos
    t = texto_visible(h)

    marcadores = MARCADORES_COMUNES + cfg['marcadores']
    global PRODUCTOS_ES
    if PRODUCTOS_ES is None:
        PRODUCTOS_ES = cadenas_productos()
    for lit in PRODUCTOS_ES:
        t = t.replace(lit, ' ')
    hits = {m: t.count(m) for m in marcadores if m in t}
    if hits:
        primero = next(iter(hits))
        i = t.find(primero)
        errores.append((ident, f'castellano {hits} · …{t[max(0, i - 60):i + 60]}…'))

    if re_acento:
        mal = re_acento.findall(t)
        if mal:
            errores.append((ident, f'acentos sin tilde: '
                                   f'{sorted({m: cfg["acentos"][m] for m in mal}.items())[:5]}'))

    raros = RE_NO_LATINO.findall(h)
    if raros:
        nombres = []
        for c in raros[:4]:
            try:
                nombres.append(f'{c!r} ({unicodedata.name(c)})')
            except ValueError:
                nombres.append(repr(c))
        errores.append((ident, f'{len(raros)} caracteres de otro alfabeto: {nombres}'))

    if f'lang="{lang}"' not in h:
        errores.append((ident, f'el <html> no declara lang="{lang}"'))

    otros = '|'.join(l for l in ['en', 'fr', 'de', 'it', 'pt', 'nl'] if l != lang)
    for href in set(re.findall(r'href="(/[a-z0-9\-/]+)"', h)):
        if href.startswith(f'/{lang}/') or href == f'/{lang}':
            continue
        if re.match(rf'^/({otros})(/|$)', href) or href == '/':
            continue
        if RE_ES_POR_DISENO.match(href):
            continue
        avisos.append((ident, f'enlace a una ruta sin prefijo /{lang}: {href}'))
    return errores, avisos


def revisa_agentes(paginas_html, catalogo, cfg):
    if not catalogo:
        return [], [('agentes', f'no se pudo leer {cfg["plataforma"]} — comprobación omitida')]
    blob = ' '.join(paginas_html)
    avisos = []
    for n in AGENTES_SOSPECHOSOS:
        c = blob.count(n)
        if c and n not in catalogo:
            avisos.append(('agentes', f'«{n}» se cita {c} veces y NO está en la '
                                      f'plataforma — ver {cfg["doc_catalogo"]}'))
    errores = []
    for es_n, xx_n in cfg['agentes_es_fr']:
        if es_n in blob:
            errores.append(('agentes', f'«{es_n}» aparece sin traducir; el nombre '
                                       f'oficial es «{xx_n}»'))
    return errores, avisos


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--lang', required=True, choices=list(CONFIG))
    ap.add_argument('--produccion', action='store_true')
    ap.add_argument('--sin-red', action='store_true')
    args = ap.parse_args()
    lang, cfg = args.lang, CONFIG[args.lang]

    # None = palabra documentada como AMBIGUA (existe sin tilde/umlaut): se
    # excluye del regex — el gate italiano ya pagó este falso positivo con 'meta'.
    acentos_activos = [k for k, v in cfg['acentos'].items() if v]
    re_acento = (re.compile(r'\b(' + '|'.join(acentos_activos) + r')\b')
                 if acentos_activos else None)

    errores, avisos = [], []
    e, a = revisa_claves(lang)
    errores += e
    avisos += a

    if args.produccion:
        sm = baja(f'{SITE}/sitemap-0.xml')
        urls = [u for u in re.findall(r'<loc>(.*?)</loc>', sm)
                if re.match(rf'{SITE}/{lang}(/|$)', u)]
        print(f'midiendo {len(urls)} URLs /{lang} de PRODUCCIÓN…')
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
            htmls = list(ex.map(baja, urls))
        pares = list(zip([u.replace(SITE, '') for u in urls], htmls))
    else:
        if not DIST.exists():
            sys.exit(f'no hay build en {DIST} — corre antes: cd astro-site && npm run build')
        ps = [DIST / f'{lang}.html'] + sorted(DIST.glob(f'{lang}/**/*.html'))
        ps = [p for p in ps if p.exists()]
        print(f'midiendo {len(ps)} páginas /{lang} del dist…')
        pares = [(str(p.relative_to(DIST)), p.read_text(encoding='utf-8')) for p in ps]

    for ident, h in pares:
        e, a = revisa_pagina(ident, h, lang, cfg, re_acento)
        errores += e
        avisos += a

    if not args.sin_red:
        e, a = revisa_agentes([h for _, h in pares], catalogo_plataforma(cfg['plataforma']), cfg)
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
