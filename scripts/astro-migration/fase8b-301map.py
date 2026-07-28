#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8B — Generador del mapa 301 de blog.aichef.pro → aichef.pro/blog.

Estrategia (formato _redirects de Netlify, host-scoped: se activará cuando el
subdominio blog.aichef.pro se añada como alias del site de producción en el
cutover del blog — NO antes):
  1. Excepciones explícitas PRIMERO (first-match-wins): Tier D, archives de
     categoría, páginas WP, feed, uploads.
  2. Regla genérica /:slug → /blog/:slug (cubre los ~346 posts A/B/C sin
     enumerarlos: el slug se conserva verbatim).
  3. Catch-all → /blog.

Salida: scripts/astro-migration/fase8b-redirects-blog.txt
        (revisar y pegar/incluir en astro-site/public/_redirects en el cutover 8B.5)
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TIERS = REPO / 'scripts' / 'astro-migration' / 'fase8b-tiers.json'
OUT = REPO / 'scripts' / 'astro-migration' / 'fase8b-redirects-blog.txt'

HOST = 'https://blog.aichef.pro'
DEST = 'https://aichef.pro'

# Archives de categoría WP → categorías destino (BLOG_CATEGORIES).
CAT_ARCHIVES = {
    'tutoriales': 'tutoriales',
    'ai-chef-pro': 'ai-chef-pro',
    'ia-en-gastronomia': 'ia-en-gastronomia',
    'libreria-de-prompts-blog': 'libreria-de-prompts',
    'glosario-y-lexico-ai': 'glosario',
    'glosario-y-lexico-cientifico-culinario': 'glosario',
    'recetario-pro-ai': 'recetas',  # fusionada en Recetas (John 2026-07-19)
    'guias-ia-locales': None,  # Tier D → hub
}

# ─────────────────────────────────────────────────────────────────────────────
# TODO LO QUE VIVE EN UN SOLO SEGMENTO necesita regla propia. Ese es el radio de
# acción de la genérica `/:slug → /blog/:slug`: trata como post cualquier cosa
# que le llegue con un único segmento, así que sin estas entradas las páginas,
# los sitemaps y hasta el robots.txt del WordPress acaban en /blog/<lo-que-sea>,
# que no existe → 301 a un 404. Auditado el 2026-07-28 contra el censo completo
# del export (408 posts + 7 páginas + 8 categorías + 237 tags + infra).
# ─────────────────────────────────────────────────────────────────────────────

# Páginas del WP → su equivalente en el sitio nuevo ('libreria-de-prompts' tiene
# su propio bloque más arriba).
WP_PAGES = {
    'about': '/sobre-nosotros',
    'contact': '/contacto',
    'home': '/',
    'blog': '/blog',
    'roadmap': '/blog',                    # no hay página de roadmap en Astro
    'politica-de-privacidad': '/privacidad',
}

# Infraestructura del WP. Los nombres de los sitemaps hijos NO se inventan: son
# los que declara el sitemap_index de la instancia (post-sitemap1..3 en el ES).
WP_INFRA = {
    'robots.txt': '/robots.txt',
    'favicon.ico': '/favicon.ico',
    'sitemap.xml': '/sitemap-index.xml',
    'post-sitemap.xml': '/sitemap-index.xml',
    'post-sitemap1.xml': '/sitemap-index.xml',
    'post-sitemap2.xml': '/sitemap-index.xml',
    'post-sitemap3.xml': '/sitemap-index.xml',
    'page-sitemap.xml': '/sitemap-index.xml',
    'category-sitemap.xml': '/sitemap-index.xml',
    'post_tag-sitemap.xml': '/sitemap-index.xml',
    'author-sitemap.xml': '/sitemap-index.xml',
    'amp': '/blog',
    'xmlrpc.php': '/blog',
    'wp-login.php': '/blog',
    'wp-admin': '/blog',
    # Archives de fecha con un solo segmento (/2024/09 ya lo coge el catch-all).
    '2024': '/blog',
    '2025': '/blog',
    '2026': '/blog',
}

# Idiomas GTranslate históricos (los 402/301 actuales): todo → hub del blog.
LANGS = ('en fr de it pt nl fa ka uz uk bg el ru ko ja zh-TW ar cs hr lt lv ms '
         'sl tr vi hy mn id iw pl sk ro bs mk kk ky af tl la gd eu').split()


def main():
    tiers = json.loads(TIERS.read_text(encoding='utf-8'))
    lines = [
        '# ── Fase 8B: blog.aichef.pro → aichef.pro/blog (generado por fase8b-301map.py) ──',
        '# ACTIVAR SOLO EN EL CUTOVER 8B.5 (requiere blog.aichef.pro como alias del site).',
        '# Orden: excepciones → genérica /:slug → catch-all. First match wins.',
        '',
        '# Portada y feed',
        '%s/ %s/blog 301!' % (HOST, DEST),
        '%s/feed %s/blog/rss.xml 301!' % (HOST, DEST),
        '%s/feed/* %s/blog/rss.xml 301!' % (HOST, DEST),
        '%s/sitemap_index.xml %s/sitemap-index.xml 301!' % (HOST, DEST),
        '',
        '# Hub librería (página WP 234) → categoría (interino hasta hub 8C)',
        '%s/libreria-de-prompts %s/blog/categoria/libreria-de-prompts 301!' % (HOST, DEST),
        '%s/libreria-de-prompts/* %s/blog/categoria/libreria-de-prompts 301!' % (HOST, DEST),
        '',
        '# Medios: misma estructura year/month en /blog-assets',
        '%s/wp-content/uploads/* %s/blog-assets/:splat 301!' % (HOST, DEST),
        '%s/wp-content/* %s/blog 301!' % (HOST, DEST),
        '',
        '# Archives de categoría WP',
    ]
    for wp_slug, dest_cat in sorted(CAT_ARCHIVES.items()):
        target = '%s/blog/categoria/%s' % (DEST, dest_cat) if dest_cat else '%s/blog' % DEST
        lines.append('%s/category/%s/* %s 301!' % (HOST, wp_slug, target))
    lines += [
        '%s/category/* %s/blog 301!' % (HOST, DEST),
        '%s/tag/* %s/blog 301!' % (HOST, DEST),
        '%s/author/* %s/blog 301!' % (HOST, DEST),
        '',
        '# Las MISMAS archives SIN la base /category/: ese WordPress tiene la base',
        '# vacía, así que su URL canónica (el campo `link` del REST) es /{slug}/ en',
        '# la raíz. Sin estas reglas caen en la genérica de abajo y acaban en',
        '# /blog/{slug-de-categoria}, que no existe: 301 a un 404. Cazado el',
        '# 2026-07-28 con la batería del cutover EN, llevaba live desde 8B.5.',
    ]
    for wp_slug, dest_cat in sorted(CAT_ARCHIVES.items()):
        target = '%s/blog/categoria/%s' % (DEST, dest_cat) if dest_cat else '%s/blog' % DEST
        lines.append('%s/%s %s 301!' % (HOST, wp_slug, target))
        lines.append('%s/%s/* %s 301!' % (HOST, wp_slug, target))   # /page/2, etc.
    # Un slug de página/infra que coincida con el de un post le robaría la
    # redirección (first match wins). Hoy no ocurre; si ocurre, parar aquí.
    choque = (set(WP_PAGES) | set(WP_INFRA)) & set(tiers)
    if choque:
        raise SystemExit('Slug de página/infra que choca con un post: %s' % sorted(choque))

    lines += ['', '# Páginas del WordPress (un solo segmento → sin regla caerían en la genérica)']
    for slug, dest in sorted(WP_PAGES.items()):
        lines.append('%s/%s %s%s 301!' % (HOST, slug, DEST, dest))
    lines += ['', '# Infraestructura del WP: sitemaps, robots, basura de bots y archives de año']
    for slug, dest in sorted(WP_INFRA.items()):
        lines.append('%s/%s %s%s 301!' % (HOST, slug, DEST, dest))

    lines += [
        '',
        '# Idiomas GTranslate históricos (MT muerta) → hub',
    ]
    for l in LANGS:
        lines.append('%s/%s/* %s/blog 301!' % (HOST, l, DEST))

    lines += ['', '# Tier D — excepciones explícitas (NO migran a /blog/{slug})']
    n_d = 0
    for slug, v in sorted(tiers.items()):
        if v['tier'] != 'D':
            continue
        n_d += 1
        why = v['why']
        if 'pSEO' in why:
            target = '%s/abrir-restaurante' % DEST
        elif 'duplicado' in why:
            target = '%s/blog/%s' % (DEST, why.split('301 a ')[-1].strip())
        else:  # escuelas US y resto
            target = '%s/blog' % DEST
        lines.append('%s/%s %s 301!' % (HOST, slug, target))

    lines += [
        '',
        '# Genérica: cualquier post A/B/C conserva su slug bajo /blog',
        '%s/:slug %s/blog/:slug 301!' % (HOST, DEST),
        '# Catch-all (paths de 2+ segmentos no contemplados)',
        '%s/* %s/blog 301!' % (HOST, DEST),
        '',
    ]
    OUT.write_text('\n'.join(lines), encoding='utf-8')
    print('Escrito %s — %d líneas (%d excepciones Tier D)' % (OUT, len(lines), n_d))


if __name__ == '__main__':
    main()
