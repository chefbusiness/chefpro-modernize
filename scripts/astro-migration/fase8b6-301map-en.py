#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8B.6 — Mapa 301 de enblog.aichef.pro → aichef.pro/en/blog.

Hermano de `fase8b-301map.py` (el del subdominio ES). Genera el bloque de reglas
que se inserta en `astro-site/public/_redirects` y lo deja delimitado por dos
marcadores, así que es IDEMPOTENTE: al reejecutar reemplaza el bloque anterior
en vez de duplicarlo.

TRES COSAS QUE NO SE PUEDEN OLVIDAR:

1. Netlify resuelve por PRIMERA COINCIDENCIA. Por eso el bloque se inserta antes
   de la genérica del subdominio ES y su orden interno es: excepciones →
   genérica /:slug → catch-all.
2. Las 50 guías de ciudad (`local-ai-guides`) NO se migran, y hay que listarlas
   UNA A UNA antes de la genérica: si no, `/:slug → /en/blog/:slug` las mandaría
   a una URL que no existe y convertiría 50 posts indexados en 50 errores 404.
   No se usan comodines de segmento parcial (`/ai-recipe-costing-for-chefs-in-*`)
   porque el splat de Netlify está pensado para el final de un path y no hay
   garantía de que case a mitad de segmento: 50 líneas explícitas no fallan.
3. Estas reglas sólo se ejecutan si enblog.aichef.pro es alias del site en
   Netlify (mismo requisito que blog.aichef.pro tuvo en el cutover 8B.5).
   Mientras el DNS siga apuntando al WordPress, el bloque es inofensivo.

Uso:
    python3 scripts/astro-migration/fase8b6-301map-en.py            # imprime
    python3 scripts/astro-migration/fase8b6-301map-en.py --apply    # inserta
"""
import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
EXPORT = Path('/root/aichef-blog-media/enblog-export')
CONTENT_EN = REPO / 'astro-site' / 'src' / 'content' / 'blog' / 'en'
REDIRECTS = REPO / 'astro-site' / 'public' / '_redirects'

SRC = 'https://enblog.aichef.pro'
DST = 'https://aichef.pro'
HUB = DST + '/en/blog'

INICIO = '# ── Fase 8B.6: enblog.aichef.pro → aichef.pro/en/blog (generado por fase8b6-301map-en.py) ──'
FIN = '# ── fin del bloque enblog.aichef.pro ──'
# Delante de esta línea se inserta el bloque (la genérica del subdominio ES).
ANCLA = '# Genérica: cualquier post A/B/C conserva su slug bajo /blog'

# Páginas del WordPress inglés → su equivalente en el sitio nuevo.
PAGINAS = [
    ('/blog', '/en/blog'),
    ('/home', '/en'),
    ('/about', '/en'),
    ('/contact', '/en'),
    # No hay roadmap ni librería de prompts en inglés: al hub, como en el ES.
    ('/roadmap', '/en/blog'),
    ('/libreria-de-prompts', '/en/blog'),
    ('/politica-de-privacidad', '/en/privacidad'),
]

# Categorías del WP inglés → destino. Sólo 2 tienen archive equivalente; el
# resto estaban vacías (count=0) o son las guías de ciudad, que no se migran.
#
# OJO CON LA BASE VACÍA: este WordPress sirve las archives en la RAÍZ
# (/ai-chef-pro/), no bajo /category/ — el campo `link` del REST lo confirma y
# /category/x/ hace 301 a /x/. Por eso cada categoría necesita DOS familias de
# regla: la de /category/… (URLs viejas) y la de raíz (las canónicas). Sin la
# segunda caen en la genérica y acaban en /en/blog/{slug-de-categoria}: un 404.
CATEGORIAS = [
    ('ai-in-gastronomy', '/en/blog/category/ai-in-gastronomy'),
    ('ai-chef-pro', '/en/blog/category/ai-chef-pro'),
    ('local-ai-guides', '/en/blog'),
    # Vacías en el WP, pero pudieron estar indexadas en su día.
    ('tutorials', '/en/blog'),
    ('prompt-library', '/en/blog'),
    ('pro-ai-recipe-book', '/en/blog'),
    ('ai-glossary-and-lexicon', '/en/blog'),
    ('culinary-science-glossary-and-lexicon', '/en/blog'),
]


def r(origen, destino):
    return '%s%s %s%s 301!' % (SRC, origen, DST, destino)


def censo():
    """(slugs migrados, slugs que se quedan fuera) según el export y la colección."""
    pub = EXPORT / 'posts-publish.jsonl'
    if not pub.exists():
        sys.exit('No está el export en %s — corre antes fase8b6-export-enblog.py' % EXPORT)
    slugs = [json.loads(l)['slug'] for l in pub.open(encoding='utf-8') if l.strip()]
    migrados = {p.stem for p in CONTENT_EN.glob('*.md')}
    huerfanos = migrados - set(slugs)
    if huerfanos:
        sys.exit('Hay .md sin post de origen (revisa el censo): %s' % sorted(huerfanos))
    return migrados, [s for s in slugs if s not in migrados]


def construir():
    migrados, fuera = censo()
    # Un slug de categoría en la raíz que coincidiera con el de un post le
    # robaría la redirección al post (first match wins). Hoy no pasa; si algún
    # día pasa, mejor parar aquí que descubrirlo en producción.
    choque = {s for s, _ in CATEGORIAS} & (migrados | set(fuera))
    if choque:
        sys.exit('Slug de categoría que choca con un post: %s' % sorted(choque))
    L = [
        INICIO,
        '# ACTIVAR SOLO EN EL CUTOVER (requiere enblog.aichef.pro como alias del site).',
        '# Orden: excepciones → genérica /:slug → catch-all. First match wins.',
        '',
        '# Portada y feed',
        r('/', '/en/blog'),
        r('/feed', '/en/blog/rss.xml'),
        r('/feed/*', '/en/blog/rss.xml'),
        r('/sitemap_index.xml', '/sitemap-index.xml'),
        '',
        '# Medios: subcarpeta propia (los nombres de fichero chocan con los del ES)',
        r('/wp-content/uploads/*', '/blog-assets/en/:splat'),
        r('/wp-content/*', '/en/blog'),
        '',
        '# Páginas del WordPress inglés',
    ]
    L += [r(o, d) for o, d in PAGINAS]
    L += ['', '# Archives de categoría WP (URLs con la base /category/)']
    L += [r('/category/%s/*' % slug, d) for slug, d in CATEGORIAS]
    L += [
        r('/category/*', '/en/blog'),
        r('/tag/*', '/en/blog'),
        r('/author/*', '/en/blog'),
        '',
        '# Las MISMAS archives en la RAÍZ, que es su URL canónica en este WP (base',
        '# de categoría vacía). Van antes de la genérica o acabarían en un 404.',
    ]
    for slug, d in CATEGORIAS:
        L.append(r('/' + slug, d))
        L.append(r('/%s/*' % slug, d))     # paginación /page/2, etc.
    L += [
        '',
        '# Las %d guías de ciudad (local-ai-guides) NO se migran → hub. Explícitas:' % len(fuera),
        '# la genérica de abajo las mandaría a un /en/blog/{slug} que no existe.',
    ]
    L += [r('/' + s, '/en/blog') for s in sorted(fuera)]
    L += [
        '',
        '# Genérica: los %d posts migrados conservan su slug bajo /en/blog' % len(migrados),
        r('/:slug', '/en/blog/:slug'),
        '# Catch-all (paths de 2+ segmentos no contemplados)',
        r('/*', '/en/blog'),
        FIN,
    ]
    return '\n'.join(L)


def aplicar(bloque):
    txt = REDIRECTS.read_text(encoding='utf-8')
    if INICIO in txt:                      # reemplaza el bloque anterior
        ini = txt.index(INICIO)
        fin = txt.index(FIN) + len(FIN)
        nuevo = txt[:ini] + bloque + txt[fin:]
    else:                                  # primera vez: antes de la genérica ES
        if ANCLA not in txt:
            sys.exit('No encuentro el ancla en _redirects: %r' % ANCLA)
        i = txt.index(ANCLA)
        nuevo = txt[:i] + bloque + '\n\n' + txt[i:]
    REDIRECTS.write_text(nuevo, encoding='utf-8')
    print('_redirects actualizado (%d líneas)' % len(nuevo.splitlines()))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='escribe en _redirects')
    args = ap.parse_args()
    bloque = construir()
    if args.apply:
        aplicar(bloque)
    else:
        print(bloque)
