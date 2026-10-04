#!/usr/bin/env python3
"""
comparar_publicados.py — prueba de NO regresión de la generalización (F2 tanda 1 de Restaurant + Bakery Business Plan
Kit, sesión Claude Code, 4-oct-2026): los entregables de food truck y cafetería regenerados con el código común
generalizado deben ser IDÉNTICOS a los publicados en `astro-site/public/dl/{food-truck,coffee-shop}-business-plan/`.

Compara fichero a fichero (6: 4 xlsx + 2 docx):
  · sha256 del fichero tal cual (informativo: openpyxl y python-docx sellan la fecha de guardado y el zip guarda la
    hora de cada miembro, así que dos guardados del mismo contenido NO dan el mismo sha256 del fichero);
  · sha256 CANÓNICO = sha256 de la lista ordenada (nombre del miembro, sha256 de su contenido descomprimido), con
    `docProps/core.xml` sin `dcterms:created` / `dcterms:modified`. Es la prueba de identidad: mismo XML byte a byte
    en todas las hojas, estilos, cadenas compartidas, caché de fórmulas, DV, CF, docProps (salvo las 2 fechas) y
    document.xml del Word;
  · si el canónico difiere, lista los miembros distintos.

    python3 comparar_publicados.py --dir /tmp/bp-regen [--repo /root/wt-bp2]
        --dir: carpeta con subcarpetas <slug>/ (la salida de `aplicar_en.py --dry-run --salida` + los docx de
        `ensamblar_docx.py --salida`). Sale con 1 si algún canónico difiere.
"""
import argparse
import hashlib
import os
import re
import sys
import zipfile

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
FICHEROS = [
    ('food-truck-business-plan', 'food-truck-financial-projections.xlsx'),
    ('food-truck-business-plan', 'food-truck-startup-checklist.xlsx'),
    ('food-truck-business-plan', 'food-truck-business-plan.docx'),
    ('coffee-shop-business-plan', 'coffee-shop-financial-projections.xlsx'),
    ('coffee-shop-business-plan', 'coffee-shop-opening-checklist.xlsx'),
    ('coffee-shop-business-plan', 'coffee-shop-business-plan.docx'),
]
RX_FECHAS = re.compile(rb'<dcterms:(created|modified)[^>]*>[^<]*</dcterms:\1>')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def miembros(path):
    out = {}
    with zipfile.ZipFile(path) as z:
        for n in sorted(z.namelist()):
            b = z.read(n)
            if n == 'docProps/core.xml':
                b = RX_FECHAS.sub(b'', b)
            out[n] = sha(b)
    return out


def canonico(m):
    return sha(''.join('%s=%s\n' % kv for kv in sorted(m.items())).encode())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', required=True)
    ap.add_argument('--repo', default=REPO)
    a = ap.parse_args()
    malos = 0
    for slug, f in FICHEROS:
        pub = os.path.join(a.repo, 'astro-site/public/dl', slug, f)
        reg = os.path.join(a.dir, slug, f)
        if not os.path.exists(reg):
            print('FALTA   %s' % reg)
            malos += 1
            continue
        mp, mr = miembros(pub), miembros(reg)
        cp, cr = canonico(mp), canonico(mr)
        fp, fr = sha(open(pub, 'rb').read()), sha(open(reg, 'rb').read())
        igual = cp == cr
        malos += not igual
        print('%s %-42s canónico %s %s · fichero %s %s' % ('IGUAL  ' if igual else 'DISTINTO', f, cp[:16],
                                                          '=' if igual else '≠ ' + cr[:16], fp[:16],
                                                          '=' if fp == fr else '≠ ' + fr[:16]))
        if not igual:
            for n in sorted(set(mp) | set(mr)):
                if mp.get(n) != mr.get(n):
                    print('         miembro distinto: %s' % n)
    print('comparar_publicados: %s' % ('6/6 IDÉNTICOS (canónico)' if not malos else '%d DISTINTOS' % malos))
    return 1 if malos else 0


if __name__ == '__main__':
    sys.exit(main())
