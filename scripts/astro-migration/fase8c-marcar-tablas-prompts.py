#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Marca las tablas de prompts del blog con la clase `tabla-prompts`.

POR QUÉ. El CSS del layout envolvía TODAS las tablas del catálogo (948) en
`.table-scroll` con `width: max-content`, pensado para tablas de datos con
celdas cortas. En las tablas de prompts la primera celda es un texto de 25-60
palabras, así que la tabla crecía hasta ~3.000 px: en escritorio quedaban
**2.205 px ocultos tras un scroll horizontal** (72 % de la tabla) y en móvil el
88 %, además de desbordar la página entera. Inusable.

La solución es dar a ESAS tablas un tratamiento propio (ancho de columnas en
escritorio, tarjetas apiladas en móvil) sin tocar las otras ~770 tablas del
catálogo, que con celdas cortas se ven bien. Como el CSS no puede seleccionar
por el texto de la cabecera, se marca el contenedor con una clase.

Criterio de detección: la tabla cuya cabecera empieza por `<th>Prompt / Solicitud</th>`.
Es el molde de la línea de librerías de prompts (177 tablas en 26 posts).

Es idempotente: no vuelve a marcar lo ya marcado.

Uso:
    python3 scripts/astro-migration/fase8c-marcar-tablas-prompts.py [--check]
"""
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / 'astro-site' / 'src' / 'content' / 'blog'
# Ojo: los 5 posts de "generación B" arrastran atributos de WordPress en la
# tabla (`class="has-fixed-layout"`, `is-style-stripes`…), así que no vale
# comparar cadenas literales: hay que casar el div .table-scroll que envuelve a
# una tabla cuya cabecera es la de prompts, con las clases que sea.
PATRON = re.compile(
    r'<div class="table-scroll(?! tabla-prompts)([^"]*)"><table([^>]*)>'
    r'<thead><tr><th>Prompt / Solicitud</th>')


def marca(txt):
    return PATRON.sub(
        lambda m: '<div class="table-scroll tabla-prompts%s"><table%s>'
                  '<thead><tr><th>Prompt / Solicitud</th>' % (m.group(1), m.group(2)),
        txt)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true', help='no escribe; sale 1 si falta marcar')
    args = ap.parse_args()

    tocados = marcadas = pendientes = 0
    for md in sorted(CONTENT.glob('*/*.md')):
        txt = md.read_text(encoding='utf-8')
        n = len(PATRON.findall(txt))
        if not n:
            continue
        pendientes += n
        if args.check:
            print('  falta marcar: %-58s %d tablas' % (md.stem[:58], n))
            continue
        md.write_text(marca(txt), encoding='utf-8')
        tocados += 1
        marcadas += n

    ya = sum(t.read_text(encoding='utf-8').count('table-scroll tabla-prompts')
             for t in CONTENT.glob('*/*.md'))
    if args.check:
        print('\n%d tablas sin marcar · %d ya marcadas' % (pendientes, ya))
        return 1 if pendientes else 0
    print('%d posts tocados · %d tablas marcadas · %d marcadas en total' % (tocados, marcadas, ya))
    return 0


if __name__ == '__main__':
    sys.exit(main())
