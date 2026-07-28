#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8B — Regenera `astro-site/src/lib/blog-lastmod.json` desde los .md.

POR QUÉ EXISTE: el sitemap toma el lastmod real de cada post de ese JSON
(astro.config.mjs → BLOG_LASTMOD). Lo genera el conversor `fase8b-wp2md.py`,
pero el conversor sólo se ejecuta al portar desde WordPress; el ensamblador de
refresh (`fase8b-refresh-assemble.py`) actualiza el `modDate` del .md y NO toca
el JSON. Sin este paso, cada slice de refresh deja el sitemap anunciando una
fecha vieja para los posts que sí cambiaron.

Es idempotente y no depende del export de WP: sólo lee los .md de la colección.
Misma semántica que fase8b-wp2md.py:266-273 (clave `/blog/<slug>`, valor
`modDate`, orden alfabético, indent=0).

8B.6: recorre TODOS los idiomas de la colección, no sólo `es`. La clave es la
URL real de cada post: `/blog/<slug>` en español (sin prefijo) y
`/<lang>/blog/<slug>` en el resto — el mismo esquema que construye
`blogBase()` en src/lib/blog.ts y que compara `serialize()` del sitemap.

Uso:
    python3 scripts/astro-migration/fase8b-regen-lastmod.py [--check]
`--check` no escribe: sale con código 1 si el JSON está desactualizado
(pensado para el gate / CI).
"""
import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / 'astro-site' / 'src' / 'content' / 'blog'
DEST = REPO / 'astro-site' / 'src' / 'lib' / 'blog-lastmod.json'
DEFAULT_LANG = 'es'   # español sin prefijo de idioma (paridad 1:1 con el WP)


def url_de(lang, slug):
    return ('/blog/' if lang == DEFAULT_LANG else '/%s/blog/' % lang) + slug


def construir():
    lastmod = {}
    sin_moddate = []
    for d in sorted(p for p in CONTENT.iterdir() if p.is_dir()):
        lang = d.name
        for md in sorted(d.glob('*.md')):
            txt = md.read_text(encoding='utf-8')
            m = re.search(r'^modDate: (\d{4}-\d{2}-\d{2})', txt, re.M)
            if m:
                lastmod[url_de(lang, md.stem)] = m.group(1)
            else:
                sin_moddate.append('%s/%s' % (lang, md.stem))
    return lastmod, sin_moddate


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true',
                    help='no escribe; falla si está desactualizado')
    args = ap.parse_args()

    nuevo, sin_moddate = construir()
    actual = json.loads(DEST.read_text(encoding='utf-8')) if DEST.exists() else {}

    cambios = {k: (actual.get(k), v) for k, v in nuevo.items() if actual.get(k) != v}
    eliminados = sorted(set(actual) - set(nuevo))

    if sin_moddate:
        print('⚠️  %d posts sin modDate (no entran al sitemap): %s'
              % (len(sin_moddate), ', '.join(sin_moddate[:5])))

    if not cambios and not eliminados:
        print('✅ blog-lastmod.json al día (%d entradas)' % len(nuevo))
        return

    for k, (antes, ahora) in sorted(cambios.items()):
        print('  %s: %s → %s' % (k, antes or '(nuevo)', ahora))
    for k in eliminados:
        print('  %s: ELIMINADO (ya no existe el .md)' % k)

    if args.check:
        sys.exit('❌ blog-lastmod.json desactualizado: %d cambios, %d bajas '
                 '— ejecuta fase8b-regen-lastmod.py' % (len(cambios), len(eliminados)))

    DEST.write_text(
        json.dumps(nuevo, ensure_ascii=False, indent=0, sort_keys=True),
        encoding='utf-8')
    print('✅ escrito: %d entradas (%d cambios, %d bajas)'
          % (len(nuevo), len(cambios), len(eliminados)))


if __name__ == '__main__':
    main()
