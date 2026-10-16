#!/usr/bin/env python3
"""Ensambla las tandas EN en los tres .md de la guía «How to Open a Pastry Shop» (inverso de split_md.py).

    tandas/en/T.. → en/how-to-open-a-pastry-shop.md
    tandas/en/B.. → en/BONUS-12-opening-decisions.md
    tandas/en/P.. → en/sample-business-plan-pastry-shop.md

Se niega (exit 1) si falta una tanda o si alguna no pasa `gate_md_en.py --final`. Después
comprueba sobre el documento entero que la estructura (títulos, tablas, separadores) es la
del .md ES original. Uso: python3 ensamblar_md.py [--solo guia|bonus|plan]
"""
import argparse
import sys
from pathlib import Path

import gate_md_en as G
from split_md import ES as DIR_ES, TANDAS as PLAN_ES

AQUI = Path(__file__).resolve().parent
SALIDA = AQUI / 'en'
DOCS = {
    'guia': ('guia-pasteleria-obrador.md', 'how-to-open-a-pastry-shop.md'),
    'bonus': ('BONUS-12-decisiones-de-apertura.md', 'BONUS-12-opening-decisions.md'),
    'plan': ('business-plan-modelo-pasteleria.md', 'sample-business-plan-pastry-shop.md'),
}


def ensamblar(clave):
    md_es, md_en = DOCS[clave]
    tandas = [t for t, _ in PLAN_ES[md_es]]
    faltan = [t for t in tandas if not (G.TANDAS_EN / ('%s.md' % t)).exists()]
    if faltan:
        print('%s: faltan las tandas %s' % (md_en, ' '.join(faltan)))
        return False
    malas, trozos = [], []
    for t in tandas:
        E, A, _ = G.revisar(t, final=True)
        print('  %s: %s (%d errores, %d avisos)' % (t, 'OK' if not E else 'FALLA', len(E), len(A)))
        if E:
            malas.append(t)
        texto = (G.TANDAS_EN / ('%s.md' % t)).read_text(encoding='utf-8')
        # la tanda siguiente empieza con «## »: tiene que caer a principio de línea
        trozos.append(texto if texto.endswith('\n') else texto + '\n')
    if malas:
        print('%s: NO se ensambla; corre `gate_md_en.py --tanda <T> --final` en %s'
              % (md_en, ' '.join(malas)))
        return False
    doc = ''.join(trozos)
    # estructura del documento entero contra el ES original
    es = (DIR_ES / md_es).read_text(encoding='utf-8')
    h_es, t_es, hr_es, _ = G.estructura(G.parsear_con_lineas(es))
    h_en, t_en, hr_en, _ = G.estructura(G.parsear_con_lineas(doc))
    nivel = lambda hs: [h[0] for h in hs]  # noqa: E731
    filas = lambda ts: [c for _, c, _ in ts]  # noqa: E731
    if nivel(h_es) != nivel(h_en) or filas(t_es) != filas(t_en) or len(hr_es) != len(hr_en):
        print('%s: la estructura del documento ensamblado no es la del ES (títulos %d/%d, '
              'tablas %d/%d, separadores %d/%d)' % (md_en, len(h_en), len(h_es), len(t_en),
                                                   len(t_es), len(hr_en), len(hr_es)))
        return False
    SALIDA.mkdir(exist_ok=True)
    (SALIDA / md_en).write_text(doc, encoding='utf-8')
    print('%s: %d palabras · %d títulos · %d tablas → %s'
          % (md_en, G.palabras(doc), len(h_en), len(t_en), SALIDA / md_en))
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--solo', choices=sorted(DOCS))
    a = ap.parse_args()
    ok = all([ensamblar(c) for c in DOCS if not a.solo or c == a.solo])
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
