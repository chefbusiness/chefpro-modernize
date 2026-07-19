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
    'recetario-pro-ai': 'recetario-pro-ai',
    'guias-ia-locales': None,  # Tier D → hub
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
