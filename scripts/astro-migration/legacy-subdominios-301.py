#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mapa 301 de los subdominios legacy de aichef.pro.

Qué cubre
  · blog.aichef.pro/{slug}          ya está en _redirects (cutover 8B.5, Netlify).
    Este script lo AUDITA: el destino tiene que existir como post o como página.
  · blog.aichef.pro/{en,fr,de,it,pt,nl}/{slug}
    GTranslate. Hoy el comodín manda al índice de ESE idioma (red de seguridad).
    El 1:1 lo sirve la edge function legacy-blog-lang, con el mapa que esto genera:
    mismo slug si el post existe en ese idioma; si no, un equivalente curado;
    si no hay, el índice del blog de ese idioma. Nunca la home en español.
  · enblog.aichef.pro               WordPress en Hostinger. Las reglas ya están
    en _redirects pero el DNS no apunta a Netlify, así que aquí se vuelcan a
    .htaccess (LiteSpeed) y a un CSV del plugin Redirection.

Salidas
  scripts/astro-migration/legacy-subdominios-301.csv
  scripts/astro-migration/legacy-subdominios-huerfanos.csv
  scripts/astro-migration/hostinger/enblog.htaccess
  scripts/astro-migration/hostinger/enblog-redirection.csv
  astro-site/netlify/edge-functions/legacy-blog-lang-map.ts

No toca la red salvo el censo de enblog (REST de WordPress). Si ese GET falla,
el script para: no reescribe el mapa inglés a ciegas.
"""
import csv
import importlib.util
import json
import re
import sys
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / 'astro-site' / 'src' / 'content' / 'blog'
PAGES = REPO / 'astro-site' / 'src' / 'pages'
PUBLIC = REPO / 'astro-site' / 'public'
REDIRECTS = PUBLIC / '_redirects'
EDGE_MAP = REPO / 'astro-site' / 'netlify' / 'edge-functions' / 'legacy-blog-lang-map.ts'
OUT_CSV = REPO / 'scripts' / 'astro-migration' / 'legacy-subdominios-301.csv'
OUT_HUER = REPO / 'scripts' / 'astro-migration' / 'legacy-subdominios-huerfanos.csv'
OUT_HT = REPO / 'scripts' / 'astro-migration' / 'hostinger' / 'enblog.htaccess'
OUT_RED = REPO / 'scripts' / 'astro-migration' / 'hostinger' / 'enblog-redirection.csv'

SITE = 'https://aichef.pro'
LANGS = ('en', 'fr', 'de', 'it', 'pt', 'nl')
HUB = {lang: 'https://aichef.pro/%s/blog' % lang for lang in LANGS}

# URLs con el slug TRADUCIDO (GTranslate no siempre conserva el slug español).
# Salen de la búsqueda del índice, no de un sitemap: el sitemap del subdominio
# ya redirige. Wayback (CDX) no respondió en esta pasada.
DESCUBIERTAS = [
    'https://blog.aichef.pro/fr/Application-de-cuisine-IA : comment-intégrer-les-outils-d\'intelligence-artificielle-dans-les-opérations-quotidiennes/',
    'https://blog.aichef.pro/fr/architecture--design--restaurants--cuisines-professionnelles/',
    'https://blog.aichef.pro/fr/L\'IA-dans-la-production-de-bière-artisanale/',
    'https://blog.aichef.pro/fr/22-techniques-de-nouilles-pad-thaï-cuisine-thaïlandaise-ai/',
    'https://blog.aichef.pro/fr/design-uniforme-et-élégant-pour-la-cuisine/',
    'https://blog.aichef.pro/it/cual-es-la-mejor-ia-para-la-alimentacion/',
    'https://blog.aichef.pro/it/Guida-completa-agli-assistenti-virtuali-per-cucine-professionali/',
    'https://blog.aichef.pro/it/Cottura-a-bassa-temperatura:-concetto-e-definizione/',
    'https://blog.aichef.pro/it/Carbonara-romana-autentica--ricetta-originale/',
    'https://blog.aichef.pro/pt/empresas-de-catering-ia-eventos-corporativos/',
    'https://blog.aichef.pro/pt/definição-do-conceito-de-goma-xantana/',
    'https://blog.aichef.pro/pt/receita-de-iskender-kebab-turca-bursa/',
    'https://blog.aichef.pro/pt/ai-chef-pro-revolucionando-a-culinária-além-dos-métodos-tradicionais/',
]

# Primera regla que case gana. Los destinos tienen que existir como .md.
# Un idioma ausente significa «no hay equivalente»: índice, no un post a la fuerza.
REGLAS = [
    ('comparativa-7-apps', (
        'las-7-mejores-apps', '7-mejores-apps', '15-herramientas-de-ia',
        'cual-es-la-mejor-ia', 'meilleures-applications', 'meilleures-apps',
        'migliori-app', 'migliori-applicazioni', 'melhores-aplicativos',
        'melhores-aplicacoes', 'melhores-apps', 'best-ai-tools',
    ), {'en': 'best-ai-tools-for-chefs-2026'}),
    ('mejor-ia-cocinar', ('mejor-ia-para-cocinar',),
     {'en': 'ai-cooking-assistant-professional-chefs'}),
    ('mejor-ia-restaurantes', ('mejor-ia-para-restaurantes',),
     {'en': 'best-restaurant-management-software-2026'}),
    ('calculadoras-food-cost', ('mejores-calculadoras-food-cost', 'best-recipe-costing'),
     {'en': 'best-recipe-costing-software-compared', 'it': 'food-cost',
      'pt': 'food-cost', 'de': 'wareneinsatz-berechnen'}),
    ('agentes-gmail', ('agentes-ia-conectados-gmail', 'agents-ia-connectes-gmail',
                       'agenti-ia-collegati', 'agentes-ia-ligados',
                       'ki-agenten-gmail', 'ai-agents-connect-gmail',
                       'gmail-sheets-instagram'),
     {'en': 'ai-agents-connect-gmail-sheets-instagram',
      'fr': 'agents-ia-connectes-gmail-sheets-instagram',
      'de': 'ki-agenten-gmail-sheets-instagram',
      'it': 'agenti-ia-collegati-gmail-sheets-instagram',
      'pt': 'agentes-ia-ligados-gmail-sheets-instagram'}),
    ('millon-consultas', ('un-millon-de-consultas', 'un-million-de-requetes',
                          'eine-million-anfragen', 'un-milione-di-richieste',
                          'um-milhao-de-consultas', 'one-million-queries'),
     {'en': 'ai-chef-pro-one-million-queries',
      'fr': 'ai-chef-pro-un-million-de-requetes',
      'de': 'ai-chef-pro-eine-million-anfragen',
      'it': 'ai-chef-pro-un-milione-di-richieste',
      'pt': 'ai-chef-pro-um-milhao-de-consultas'}),
    ('haccp', ('haccp', 'appcc', '7-principi-haccp', 'haccp-konzept'),
     {'en': 'haccp-food-safety-7-principles-restaurants',
      'fr': 'haccp', 'de': 'haccp-konzept', 'it': '7-principi-haccp', 'pt': 'haccp'}),
    ('higiene', ('higiene-alimentaria', 'hygiene-alimentaire', 'higiene-e-seguranca',
                 'seguridad-alimentaria', 'personalhygiene', 'lmhv'),
     {'fr': 'hygiene-alimentaire', 'de': 'lmhv',
      'pt': 'higiene-e-seguranca-alimentar',
      'en': 'haccp-food-safety-7-principles-restaurants'}),
    ('alergenos', ('alergen', 'allergen', 'allergene', 'alergenio'),
     {'fr': 'tableau-des-allergenes', 'de': '14-allergene',
      'it': 'lista-allergeni-alimentari', 'pt': 'alergenios', 'nl': 'allergenenlijst'}),
    ('salsas-madre', ('salsas-madre', 'sauces-meres', 'salse-madri', 'grundsaucen'),
     {'fr': 'sauces-meres', 'de': 'grundsaucen', 'it': 'salse-madri'}),
    ('food-cost', ('food-cost', 'escandallo', 'wareneinsatz', 'kalkulation-gastronomie'),
     {'en': 'ai-food-cost-calculator-reduce-costs', 'it': 'food-cost',
      'pt': 'food-cost', 'de': 'wareneinsatz-berechnen',
      'fr': 'fiche-technique-cuisine'}),
    ('menu-engineering', ('ingenieria-menu', 'menu-engineering', 'carta-restaurante-rentable'),
     {'en': 'menu-engineering-software-complete-guide', 'fr': 'menu-engineering'}),
    ('fermentacion', ('fermentacion', 'lacto-fermentation', 'fermentieren'),
     {'fr': 'lacto-fermentation', 'de': 'fermentieren'}),
    ('molecular', ('cocina-molecular', 'cucina-molecolare', 'molekularkueche'),
     {'it': 'cucina-molecolare', 'de': 'molekularkueche'}),
    ('sous-vide', ('sous-vide', 'coccion-a-baja-temperatura', 'cottura-a-bassa'),
     {'de': 'sous-vide-tabelle'}),
    ('cortes', ('tipos-de-cortes', 'tailles-de-decoupe', 'cortes-de-legumes', 'brunoise'),
     {'fr': 'tailles-de-decoupe', 'pt': 'cortes-de-legumes-mirepoix-brunoise'}),
    ('dark-kitchen', ('dark-kitchen', 'ghost-kitchen', 'cocina-fantasma'),
     {'it': 'dark-kitchen', 'en': 'ghost-kitchen-complete-guide'}),
    ('fondo-bruno', ('fondo-oscuro', 'fondo-bruno', 'fond-brun'),
     {'it': 'fondo-bruno'}),
    ('limpieza', ('protocolos-de-limpieza', 'plan-de-nettoyage'),
     {'fr': 'plan-de-nettoyage-cuisine'}),
    ('frollatura', ('maduracion-carne', 'frollatura'),
     {'it': 'frollatura-carne'}),
    ('carbonara', ('carbonara',), {}),
    ('goma-xantana', ('goma-xantana', 'xantana'), {}),
]

# Comparativas que John señaló (o la misma familia) y que NO tienen post nativo.
HUERFANOS_REGLA = {
    'comparativa-7-apps': 'primaria',
    'mejor-ia-cocinar': 'secundaria',
    'mejor-ia-restaurantes': 'secundaria',
}
TITULOS_GSC = {
    'en': '22117 impresiones en blog.aichef.pro/en (dato de John, 2026-10-22); no hay desglose por URL en este entorno',
    'fr': '13544 impresiones en blog.aichef.pro/fr (dato de John, 2026-10-22); no hay desglose por URL en este entorno',
    'it': '10481 impresiones en blog.aichef.pro/it (dato de John, 2026-10-22); no hay desglose por URL en este entorno',
    'pt': '8404 impresiones en blog.aichef.pro/pt (dato de John, 2026-10-22); no hay desglose por URL en este entorno',
    'de': '2450 impresiones en blog.aichef.pro/de (dato de John, 2026-10-22); no hay desglose por URL en este entorno',
    'nl': '1347 impresiones en blog.aichef.pro/nl (dato de John, 2026-10-22); no hay desglose por URL en este entorno',
}

STEM = {
    'conceito': 'concepto', 'concetto': 'concepto', 'konzept': 'concepto', 'concept': 'concepto',
    'definicao': 'definicion', 'definizione': 'definicion', 'definition': 'definicion',
    'receita': 'receta', 'ricetta': 'receta', 'rezept': 'receta', 'recipe': 'receta',
    'cozinha': 'cocina', 'cucina': 'cocina', 'cuisine': 'cocina', 'kueche': 'cocina', 'kitchen': 'cocina',
    'aplicacoes': 'aplicaciones', 'applicazioni': 'aplicaciones', 'applications': 'aplicaciones',
    'melhores': 'mejores', 'migliori': 'mejores', 'meilleures': 'mejores',
    'inteligencia': 'inteligencia', 'artificielle': 'inteligencia', 'artificial': 'inteligencia',
    'temperatur': 'temperatura', 'temperature': 'temperatura',
}
STOP = set('''de la el los las un una y en con para por del al que es su se the of and for to
le les des du et dans une qui est il di da per che gli delle os as do da dos das em um uma com
die der das und mit fur von het een van voor naar au aux ce se son sur par les des'''.split())


def cargar_auditor():
    ruta = REPO / 'scripts' / 'astro-migration' / 'fase8b-auditar-301.py'
    spec = importlib.util.spec_from_file_location('auditar301', ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def normalizar(path):
    """Gemelo de normalizePath() en legacy-blog-lang.ts."""
    path = urllib.parse.unquote(path)
    path = path.replace('\u00a0', ' ').replace('\u202f', ' ')
    path = unicodedata.normalize('NFKD', path)
    path = ''.join(c for c in path if not unicodedata.combining(c))
    path = path.lower().split('?')[0].split('#')[0]
    if not path.startswith('/'):
        path = '/' + path
    path = re.sub(r'[^a-z0-9/]+', '-', path)
    path = re.sub(r'-{2,}', '-', path)
    path = path.replace('-/', '/').replace('/-', '/')
    path = path.rstrip('/')
    return path or '/'


def tokens(texto):
    plano = normalizar('/' + texto).strip('/')
    out = []
    for t in plano.split('-'):
        if not t or t in STOP or len(t) < 3:
            continue
        out.append(STEM.get(t, t))
    return set(out)


def titulo_de(md):
    texto = md.read_text(encoding='utf-8', errors='replace')[:600]
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', texto, re.M)
    return m.group(1) if m else md.stem


def posts():
    out = {}
    for lang_dir in CONTENT.iterdir():
        if not lang_dir.is_dir():
            continue
        out[lang_dir.name] = {p.stem: titulo_de(p) for p in lang_dir.glob('*.md')}
    return out


def rutas_estaticas():
    rutas = {'/'}
    for p in PAGES.rglob('*.astro'):
        rel = p.relative_to(PAGES).with_suffix('')
        partes = list(rel.parts)
        if partes[-1] == 'index':
            partes = partes[:-1]
        if any(x.startswith('[') for x in partes):
            continue
        rutas.add('/' + '/'.join(partes) if partes else '/')
    for nombre in ('robots.txt', 'favicon.ico', 'sitemap-index.xml'):
        if (PUBLIC / nombre).exists() or nombre == 'sitemap-index.xml':
            rutas.add('/' + nombre)
    return rutas


def destino_existe(url, corpus, estaticas):
    if not url.startswith(SITE):
        return False
    path = url[len(SITE):].split('?')[0].rstrip('/') or '/'
    if path in estaticas:
        return True
    m = re.fullmatch(r'(?:/(en|fr|de|it|pt|nl))?/blog/([^/]+)', path)
    if m:
        lang = m.group(1) or 'es'
        return m.group(2) in corpus.get(lang, {})
    if re.fullmatch(r'(?:/(en|fr|de|it|pt|nl))?/blog', path):
        return True
    if path.startswith('/blog-assets/'):
        return True
    if re.fullmatch(r'(?:/(en|fr|de|it|pt|nl))?/blog/(categoria|category|categorie|kategorie)/[^/]+', path):
        return True
    # pSEO de ciudades: /abrir-restaurante/{ciudad}. El índice pelado es un 404.
    ciudades = {
        'madrid', 'barcelona', 'valencia', 'sevilla', 'malaga', 'bilbao', 'zaragoza',
        'ciudad-de-mexico', 'guadalajara', 'monterrey', 'queretaro', 'bogota',
        'medellin', 'buenos-aires', 'santiago',
    }
    m = re.fullmatch(r'/abrir-restaurante/([^/]+)', path)
    if m and m.group(1) in ciudades:
        return True
    return False


def match_lang(lang, slug, corpus):
    if slug in corpus.get(lang, {}):
        return '%s/%s' % (HUB[lang], slug), 'mismo', 'slug idéntico en /%s/blog' % lang
    for regla, señales, destinos in REGLAS:
        if any(s in slug for s in señales):
            elegido = destinos.get(lang)
            if elegido and elegido in corpus.get(lang, {}):
                return '%s/%s' % (HUB[lang], elegido), 'parecido', regla
            return HUB[lang], 'indice', regla
    return HUB[lang], 'indice', 'sin-equivalente'


def aterriza_es(slug, resolver, reglas_blog):
    """Slug español tras las 301 ya publicadas (consolidaciones incluidas)."""
    dest, _pat = resolver('/' + slug, reglas_blog)
    if not dest:
        return slug, 'sin-regla'
    path = dest.replace(SITE, '').rstrip('/')
    m = re.fullmatch(r'/blog/([^/]+)', path)
    if m:
        return m.group(1), 'post'
    return None, path or '/'


def censo_enblog():
    def get(path):
        req = urllib.request.Request(
            'https://enblog.aichef.pro/wp-json/wp/v2/' + path,
            headers={'User-Agent': 'aichef-legacy-301'},
        )
        with urllib.request.urlopen(req, timeout=40) as r:
            return json.loads(r.read().decode())
    posts_ = get('posts?per_page=100&_fields=slug,link,title')
    pages = get('pages?per_page=100&_fields=slug,link,title')
    cats = get('categories?per_page=100&_fields=slug,link')
    return posts_, pages, cats


def bloque_enblog(texto):
    ini = texto.find('# ── Fase 8B.6:')
    fin = texto.find('# ── fin del bloque enblog.aichef.pro ──')
    if ini < 0 or fin < 0:
        sys.exit('No encuentro el bloque enblog en _redirects')
    lineas = []
    for linea in texto[ini:fin].splitlines():
        linea = linea.strip()
        if not linea or linea.startswith('#'):
            continue
        partes = linea.split()
        if len(partes) < 2:
            continue
        lineas.append((partes[0], partes[1]))
    return lineas


def a_htaccess(src, dst):
    path = src.replace('https://enblog.aichef.pro', '') or '/'
    if path.rstrip('/') in ('/wp-admin', '/wp-login.php'):
        return None
    if path == '/':
        return 'RewriteRule ^/?$ %s [R=301,L]' % dst
    if path == '/:slug':
        return 'RewriteRule ^([^/]+)/?$ %s [R=301,L]' % dst.replace(':slug', '$1')
    if path == '/*':
        return 'RewriteRule ^(.+)$ %s [R=301,L]' % dst
    if path.endswith('/*'):
        base = re.escape(path[1:-2])
        if ':splat' in dst:
            return 'RewriteRule ^%s/(.+)$ %s [R=301,L]' % (base, dst.replace(':splat', '$1'))
        return 'RewriteRule ^%s(/.*)?$ %s [R=301,L]' % (base, dst)
    exacto = re.escape(path.lstrip('/'))
    return 'RewriteRule ^%s/?$ %s [R=301,L]' % (exacto, dst)


def regla_redirection(src, dst):
    """Una fila del CSV de importación del plugin Redirection. None = no entra
    (comodines y admin: el .htaccess los cubre y un comodín se comería wp-admin)."""
    path = src.replace('https://enblog.aichef.pro', '') or '/'
    if path.rstrip('/') in ('/wp-admin', '/wp-login.php', '/wp-json'):
        return None
    if any(tok in path for tok in (':slug', ':splat', '*')):
        return None
    origen = path if path.startswith('/') else '/' + path
    return origen.rstrip('/') or '/', dst


def solape_es(slug_norm, corpus_es):
    """Slug traducido → slug español, solo si el solape es claro y único."""
    toks = tokens(slug_norm)
    if len(toks) < 3:
        return None
    mejor, segundo = (0, None), (0, None)
    for es_slug in corpus_es:
        otros = tokens(es_slug)
        if not otros:
            continue
        inter = len(toks & otros)
        jac = inter / len(toks | otros)
        if jac > mejor[0]:
            segundo = mejor
            mejor = (jac, es_slug)
        elif jac > segundo[0]:
            segundo = (jac, es_slug)
    if mejor[0] < 0.55 or mejor[0] - segundo[0] < 0.1:
        return None
    return mejor[1]


def fila(origen, destino, tipo, motivo, capa, nota=''):
    return {
        'origen': origen,
        'destino': destino,
        'tipo': tipo,
        'motivo': motivo,
        'capa': capa,
        'nota': nota,
    }


def main():
    aud = cargar_auditor()
    corpus = posts()
    estaticas = rutas_estaticas()
    for _regla, _sig, destinos in REGLAS:
        for lang, slug in destinos.items():
            if slug not in corpus.get(lang, {}):
                sys.exit('Regla apunta a un post que no existe: %s/%s' % (lang, slug))

    reglas_blog = aud.reglas('https://blog.aichef.pro')
    es_slugs = set(corpus['es']) | set(json.loads(
        (REPO / 'scripts/astro-migration/fase8b-tiers.json').read_text(encoding='utf-8')))

    filas = []
    exactos = {}  # path normalizado → destino absoluto (solo los que no son el índice)
    huerfanos = []
    rotos_es = []

    for slug in sorted(es_slugs):
        dest, pat = aud.resolver('/' + slug, reglas_blog)
        origen = 'https://blog.aichef.pro/' + slug
        if not dest:
            rotos_es.append((slug, 'sin regla'))
            continue
        if not destino_existe(dest, corpus, estaticas):
            rotos_es.append((slug, dest))
        aterrizaje, clase = aterriza_es(slug, aud.resolver, reglas_blog)
        nota = '' if aterrizaje == slug or clase != 'post' else 'consolidado hacia ' + aterrizaje
        tipo = 'mismo' if (clase == 'post' and aterrizaje == slug) else 'excepcion'
        filas.append(fila(origen, dest, tipo, 'redirects ES ya publicados (%s)' % (pat or ''), 'redirects', nota))

        for lang in LANGS:
            origen_lang = 'https://blog.aichef.pro/%s/%s' % (lang, slug)
            if clase != 'post':
                destino, tipo_l, motivo = HUB[lang], 'indice', 'el español va a %s' % clase
            else:
                destino, tipo_l, motivo = match_lang(lang, aterrizaje, corpus)
            filas.append(fila(origen_lang, destino, tipo_l, motivo, 'edge' if tipo_l != 'indice' else 'indice'))
            if tipo_l != 'indice':
                exactos[normalizar('/%s/%s' % (lang, slug))] = destino
            if (tipo_l == 'indice' and motivo in HUERFANOS_REGLA and aterrizaje == slug):
                huerfanos.append({
                    'prioridad': HUERFANOS_REGLA[motivo],
                    'idioma': lang,
                    'url_antigua': origen_lang,
                    'slug_espanol': slug,
                    'titulo_es': corpus['es'].get(slug, ''),
                    'destino_propuesto': destino,
                    'por_que': 'No hay post nativo en %s. En inglés el más cercano es /en/blog/best-ai-tools-for-chefs-2026 (o el de la regla %s).' % (lang, motivo),
                    'impresiones': TITULOS_GSC[lang],
                })

    vistos = {normalizar(urllib.parse.urlparse(f['origen']).path) for f in filas}
    for url in DESCUBIERTAS:
        ruta = urllib.parse.urlparse(url).path
        clave = normalizar(ruta)
        if clave in vistos:
            continue
        vistos.add(clave)
        partes = [p for p in clave.split('/') if p]
        if not partes or partes[0] not in HUB:
            continue
        lang, resto = partes[0], partes[1] if len(partes) > 1 else ''
        es = solape_es(resto, es_slugs)
        if es:
            aterrizaje, clase = aterriza_es(es, aud.resolver, reglas_blog)
            if clase == 'post':
                destino, tipo_l, motivo = match_lang(lang, aterrizaje, corpus)
                motivo = 'slug traducido → %s (%s)' % (es, motivo)
            else:
                destino, tipo_l, motivo = HUB[lang], 'indice', 'slug traducido → %s, que en ES no es un post' % es
        else:
            destino, tipo_l, motivo = HUB[lang], 'indice', 'slug traducido sin par español claro'
        filas.append(fila(url.split('?')[0].rstrip('/'), destino, tipo_l, motivo,
                          'edge' if tipo_l != 'indice' else 'indice', 'descubierta en el índice, slug traducido'))
        if tipo_l != 'indice':
            exactos[clave] = destino

    # enblog: censo vivo + reglas ya escritas
    try:
        posts_en, pages_en, cats_en = censo_enblog()
    except Exception as e:
        sys.exit('No pude leer el REST de enblog (%s). No reescribo el mapa.' % e)
    reglas_en = aud.reglas('https://enblog.aichef.pro')
    vistos_en = set()
    for item, familia in (
        *[(p, 'post') for p in posts_en],
        *[(p, 'pagina') for p in pages_en],
        *[(c, 'categoria') for c in cats_en],
    ):
        slug = item['slug']
        vistos_en.add(slug)
        dest, pat = aud.resolver('/' + slug, reglas_en)
        titulo = ''
        if isinstance(item.get('title'), dict):
            titulo = item['title'].get('rendered', '')
        if not dest:
            rotos_es.append(('enblog/' + slug, 'sin regla'))
            continue
        if not destino_existe(dest, corpus, estaticas):
            rotos_es.append(('enblog/' + slug, dest))
        tipo = 'mismo' if slug in corpus.get('en', {}) else 'indice'
        filas.append(fila(
            'https://enblog.aichef.pro/' + slug, dest, tipo,
            'enblog %s, regla %s' % (familia, pat or ''),
            'htaccess+redirects', titulo,
        ))

    if rotos_es:
        print('DESTINOS QUE NO EXISTEN:')
        for slug, dest in rotos_es:
            print(' ', slug, '→', dest)
        sys.exit(1)

    # sitemap del repo: ningún fichero público debe citar los subdominios
    for p in list(PUBLIC.rglob('*.xml')) + list(PUBLIC.rglob('*.txt')):
        if 'blog-assets' in p.parts:
            continue
        texto = p.read_text(encoding='utf-8', errors='replace')
        if 'blog.aichef.pro' in texto or 'enblog.aichef.pro' in texto:
            # _redirects y robots no son el sitemap; robots no debe citarlos como Sitemap
            if p.name == '_redirects':
                continue
            if p.name == 'robots.txt' and 'Sitemap: https://aichef.pro/' in texto:
                if re.search(r'Sitemap:\s+https?://(blog|enblog)\.aichef\.pro', texto):
                    sys.exit('robots.txt anuncia un sitemap del subdominio: %s' % p)
                continue
            sys.exit('El fichero público %s cita un subdominio legacy' % p)

    campos = ['origen', 'destino', 'tipo', 'motivo', 'capa', 'nota']
    with OUT_CSV.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, campos)
        w.writeheader()
        w.writerows(filas)
    campos_h = ['prioridad', 'idioma', 'url_antigua', 'slug_espanol', 'titulo_es',
                'destino_propuesto', 'por_que', 'impresiones']
    with OUT_HUER.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, campos_h)
        w.writeheader()
        w.writerows(huerfanos)

    # mapa de la edge function: solo los 1:1 (el índice es el fallback del código)
    lineas = [
        '// Generado por scripts/astro-migration/legacy-subdominios-301.py — no editar a mano.',
        '// Clave: path normalizado de blog.aichef.pro. Valor: destino absoluto.',
        '// Lo que no está aquí cae al índice del idioma (HUB en legacy-blog-lang.ts).',
        'export const LEGACY_LANG_EXACT: Record<string, string> = {',
    ]
    for clave in sorted(exactos):
        lineas.append('  %s: %s,' % (json.dumps(clave), json.dumps(exactos[clave])))
    lineas.append('};')
    lineas.append('')
    EDGE_MAP.write_text('\n'.join(lineas), encoding='utf-8')

    # .htaccess y CSV del plugin, en el mismo orden que _redirects
    texto = REDIRECTS.read_text(encoding='utf-8')
    pares = bloque_enblog(texto)
    reglas_ht = []
    filas_red = []
    for src, dst in pares:
        ht = a_htaccess(src, dst)
        if ht:
            reglas_ht.append(ht)
        red = regla_redirection(src, dst)
        if red:
            filas_red.append(red)
    # El comodín :slug no entra en el CSV del plugin (se tragaría wp-admin).
    # Cada URL censada se escribe explícita, con el mismo destino que _redirects.
    ya = {origen for origen, _dst in filas_red}
    for item in list(posts_en) + list(pages_en) + list(cats_en):
        origen = '/' + item['slug']
        if origen in ya:
            continue
        dest, _pat = aud.resolver(origen, reglas_en)
        if not dest:
            continue
        filas_red.append((origen, dest))
        ya.add(origen)
    OUT_HT.parent.mkdir(parents=True, exist_ok=True)
    OUT_HT.write_text('\n'.join([
        '# enblog.aichef.pro → aichef.pro/en/blog',
        '# Generado por scripts/astro-migration/legacy-subdominios-301.py',
        '#',
        '# DÓNDE PEGARLO. hPanel → Archivos → administrador de archivos del',
        '# WordPress de enblog → public_html (o la carpeta de ese subdominio) →',
        '# .htaccess. Estas líneas van ENCIMA de «# BEGIN WordPress». Si caen',
        '# dentro, WordPress las borra al guardar los enlaces permanentes.',
        '# LiteSpeed (el header x-litespeed de este sitio) sí lee .htaccess.',
        '# Después: hPanel → caché / CDN → purgar enblog.aichef.pro. La hCDN',
        '# estaba sirviendo 200 cacheados.',
        '#',
        '# /wp-admin y /wp-login.php NO se redirigen: si no, el panel queda cerrado',
        '# y no hay forma de quitar este fichero. Cuando el DNS pase a Netlify,',
        '# las reglas del repo sí apartan el admin.',
        '#',
        '# NO hace falta tocar el DNS para que esto funcione. Apuntar el',
        '# subdominio a Netlify es el cierre (el mismo mapa ya está en',
        '# astro-site/public/_redirects) pero Hostinger recrea las A records si',
        '# enblog sigue siendo el dominio principal de la instancia WordPress:',
        '# primero desvincularla. Ver CUTOVER_ENBLOG_PENDIENTE.md.',
        '<IfModule mod_rewrite.c>',
        'RewriteEngine On',
        '# Si este fichero acabara en otro sitio del hosting, no redirige nada.',
        'RewriteCond %{HTTP_HOST} !^enblog\\.aichef\\.pro$ [NC]',
        'RewriteRule ^ - [L]',
        'RewriteRule ^wp-admin(/|$) - [L]',
        'RewriteRule ^wp-login\\.php$ - [L]',
        'RewriteRule ^wp-json(/|$) - [L]',
        *reglas_ht,
        '</IfModule>',
        '',
    ]), encoding='utf-8')
    with OUT_RED.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['source', 'target', 'regex', 'code'])
        for origen, destino in filas_red:
            w.writerow([origen, destino, '0', '301'])

    from collections import Counter
    c = Counter((f['capa'], f['tipo']) for f in filas)
    print('Filas CSV: %d' % len(filas))
    for k, n in sorted(c.items()):
        print('  %s %s: %d' % (k[0], k[1], n))
    print('1:1 en la edge function: %d' % len(exactos))
    print('Huérfanos a recrear: %d' % len(huerfanos))
    print('Reglas htaccess: %d · filas plugin: %d' % (len(reglas_ht), len(filas_red)))
    print('Posts enblog vivos: %d · sin .md EN (van al índice, ya excepcionados): %d' % (
        len(posts_en), sum(1 for p in posts_en if p['slug'] not in corpus['en'])))


if __name__ == '__main__':
    main()
