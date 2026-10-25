#!/usr/bin/env python3
"""Censo y cambio de las páginas anunciadas de las 6 guías ES v1 por las del PDF real (25-oct-2026).

`paginas-gate.py` solo mira las fichas `.ts`; esto recorre además hubs ×7, SPA, catálogo, llms, functions
(email post-compra) y las fichas, y atribuye cada «N+ páginas / N+ pages / mais de N páginas…» al producto
del slug más cercano ANTES de la mención (los bloques de los hubs y del registro empiezan por el slug/id).
El blog se excluye (carril Cursor).

    python3 scripts/productos-digitales/guias-v1-pdf/paginas_v1.py           # censo (no escribe)
    python3 scripts/productos-digitales/guias-v1-pdf/paginas_v1.py --aplicar
"""
import os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
REALES = {  # páginas del PDF A4 de LibreOffice (pdf_guias_v1.py, 25-oct-2026)
    'guia-panaderia-obrador': 14, 'guia-restaurante-casual': 21, 'guia-restaurante-japones': 23,
    'guia-restaurante-mexicano': 22, 'guia-restaurante-nikkei': 24, 'guia-restaurante-peruano': 22,
}
# Toda mención de páginas, en los 7 idiomas: prefijo opcional («mais de», «plus de»…), número, «+», unidad.
CLAIM = re.compile(r"(?P<pre>(?:mais de|plus de|más de|über|oltre|meer dan|more than|over)\s+)?"
                   r"(?P<n>\d{2,3})\s?(?P<plus>\+)?\s?(?P<u>páginas|pages|page\b|Seiten|pagine|pagina\\'s|pagina's|pagina’s|pp\b\.?|págs\.?)",
                   re.I)
SLUG = re.compile(r"(?<![a-z0-9-])(guia-[a-z0-9-]+|manual-[a-z0-9-]+|kit-[a-z0-9-]+|plan-[a-z0-9-]+|pack-[a-z0-9-]+|"
                  r"pro-prompts-ebook|mega-pack-tareas)(?![a-z0-9-])")
FICHAS = {s: 'astro-site/src/data/productos/guias/%s.ts' % s for s in REALES}


def ficheros():
    out = subprocess.run(['git', 'ls-files', 'astro-site/src', 'src', 'netlify', 'astro-site/public'],
                         cwd=ROOT, capture_output=True, text=True).stdout.split('\n')
    return [f for f in out if f and not f.startswith('astro-site/src/content/')
            and os.path.splitext(f)[1] in ('.ts', '.tsx', '.astro', '.txt', '.json', '.md', '.mjs')]


def main():
    aplicar = '--aplicar' in sys.argv
    total = 0
    for f in ficheros():
        txt = open(os.path.join(ROOT, f), encoding='utf-8').read()
        if not any(s in txt for s in REALES):
            continue
        ficha = next((s for s, p in FICHAS.items() if p == f), None)
        slugs = [(m.start(), m.group(1)) for m in SLUG.finditer(txt)]
        cambios = []
        for m in CLAIM.finditer(txt):
            prod = ficha
            if not prod:
                antes = [s for pos, s in slugs if pos < m.start()]
                prod = antes[-1] if antes else None
            if prod not in REALES:
                continue
            real = REALES[prod]
            if int(m.group('n')) <= real and not m.group('plus') and not m.group('pre'):
                continue
            # «Premium 60+ page guide» (adjetivo en inglés) → «21-page»
            nuevo = ('%d-page' if m.group('u') == 'page' else '%d %s') % ((real,) if m.group('u') == 'page' else (real, m.group('u')))
            cambios.append((m.start(), m.end(), nuevo))
            linea = txt.count('\n', 0, m.start()) + 1
            print('%s:%d [%s] «%s» → «%s»' % (f, linea, prod, m.group(0), nuevo))
        total += len(cambios)
        if aplicar and cambios:
            for a, b, nuevo in reversed(cambios):
                txt = txt[:a] + nuevo + txt[b:]
            open(os.path.join(ROOT, f), 'w', encoding='utf-8').write(txt)
    print('%d menciones %s' % (total, 'cambiadas' if aplicar else '(censo; --aplicar para escribir)'))


if __name__ == '__main__':
    main()
