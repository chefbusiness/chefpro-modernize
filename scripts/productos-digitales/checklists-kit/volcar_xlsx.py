#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
volcar_xlsx.py — volcado legible (texto plano) de los xlsx de una carpeta, para la revisión adversarial sin openpyxl.
Sesión Claude Code, 17-oct-2026 (Restaurant Checklists Kit Pro, F2). Solo LEE.

    python3 volcar_xlsx.py <carpeta> <salida.txt> [--orden es|en]

Por libro (en el orden de mapas.FICHEROS) y hoja: docProps, protección, área y títulos de impresión, paneles, papel,
pie; celda → valor (los saltos de línea como «⏎»); fórmulas como fórmula y su valor en caché; DV con tipo, ítems y
mensajes; CF con tipo, fórmula y texto. El mismo formato para el ES y el EN: se comparan lado a lado.
"""
import argparse
import logging
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import openpyxl                                          # noqa: E402

import kit                                               # noqa: E402  (--kit base|bar: kit.py)
from kit import mapas                                    # noqa: E402

logging.disable(logging.CRITICAL)


def txt(v):
    if isinstance(v, str):
        return v.replace('\r', '').replace('\n', ' ⏎ ')
    return repr(v)


def volcar(path, out):
    wf = openpyxl.load_workbook(path)
    wv = openpyxl.load_workbook(path, data_only=True)
    p = wf.properties
    out.append('#' * 100)
    out.append('# %s' % os.path.basename(path))
    out.append('# docProps: title=%r · subject=%r · keywords=%r · description=%r · category=%r · creator=%r'
               % (p.title, p.subject, p.keywords, p.description, p.category, p.creator))
    for ws in wf.worksheets:
        out.append('')
        out.append('=== Hoja «%s» · protegida=%s · área=%s · títulos=%s · paneles=%s · papel=%s · orientación=%s'
                   % (ws.title, bool(ws.protection.sheet), ws.print_area, ws.print_title_rows, ws.freeze_panes,
                      ws.page_setup.paperSize, ws.page_setup.orientation))
        pie = ws.oddFooter.center.text
        if pie:
            out.append('    pie: %s' % pie)
        vv = wv[ws.title]
        for c in sorted(ws._cells.values(), key=lambda c: (c.row, c.column)):
            if c.value is None:
                continue
            if c.data_type == 'f':
                out.append('%-6s = %s   → caché %s' % (c.coordinate, c.value, txt(vv[c.coordinate].value)))
            else:
                out.append('%-6s : %s' % (c.coordinate, txt(c.value)))
        for dv in ws.data_validations.dataValidation:
            out.append('DV %s · %s %s · f1=%s · f2=%s · errorTitle=%s · error=%s · promptTitle=%s · prompt=%s'
                       % (dv.sqref, dv.type, dv.operator or '', dv.formula1, dv.formula2, txt(dv.errorTitle),
                          txt(dv.error), txt(dv.promptTitle), txt(dv.prompt)))
        for cf in ws.conditional_formatting:
            for r in cf.rules:
                out.append('CF %s · %s %s · fórmula=%s · texto=%s' % (cf.sqref, r.type, r.operator or '', r.formula,
                                                                     r.text))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('carpeta')
    ap.add_argument('salida')
    ap.add_argument('--orden', choices=('es', 'en'), default='en')
    kit.argumento(ap)
    a = ap.parse_args()
    nombres = list(mapas.FICHEROS) if a.orden == 'es' else list(mapas.FICHEROS.values())
    out = ['Volcado de %d xlsx de %s (orden de mapas.FICHEROS)' % (len(nombres), a.carpeta)]
    for n in nombres:
        volcar(os.path.join(a.carpeta, n), out)
    with open(a.salida, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    print('%s: %d líneas' % (a.salida, len(out)))


if __name__ == '__main__':
    main()
