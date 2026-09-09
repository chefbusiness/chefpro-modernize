#!/usr/bin/env python3
"""Mide el solape de frases entre los bloques de un MISMO capítulo (Jaccard sobre
tokens, umbral 0,55 por defecto) y sirve de gate: exit 1 si hay algún par.

Uso: python3 solape.py <dir_txt> [umbral]

Generalización (2026-09-10) del `manual-chef-ejecutivo/build/docs/solape.py`, que
estaba clavado a su carpeta y a 20 capítulos. Aquí los capítulos se DESCUBREN por
glob (`cap*_b*.txt`) en el directorio que se le pase, así que vale para cualquier
producto y también para la carpeta de un bonus (`…/txt/BONUS-xxx`). No es
recursivo a propósito: cada bonus se mide aparte, que es como se escribe.

Existe porque `documentos.py` entregaba a los 2-3 redactores de un capítulo la
lista COMPLETA de `puntos` y todos desarrollaban lo mismo: 41 pares ≥ 0,55 en 15
de los 20 capítulos del Manual del Chef Ejecutivo. Con `repartir_puntos()` el
número debe quedarse en 0; este script es lo que lo demuestra.
"""
import re, glob, os, sys, unicodedata


def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return set(t for t in re.findall(r'[a-z0-9]{3,}', s))


def frases(t):
    t = re.sub(r'^###.*$', '', t, flags=re.M)
    return [f.strip() for f in re.split(r'(?<=[.!?])\s+', t) if len(f.split()) >= 8]


def capitulos_de(dir_txt):
    """{nº de capítulo: [ficheros ordenados]} descubiertos por nombre."""
    caps = {}
    for ruta in sorted(glob.glob(os.path.join(dir_txt, 'cap*_b*.txt'))):
        m = re.match(r'cap(\d+)_b(\d+)\.txt$', os.path.basename(ruta))
        if m:
            caps.setdefault(int(m.group(1)), []).append(ruta)
    return caps


def pares_solapados(ficheros, umbral):
    fr = [(os.path.basename(b), f)
          for b in ficheros
          for f in frases(open(b, encoding='utf-8').read())]
    hits = []
    for i in range(len(fr)):
        for j in range(i + 1, len(fr)):
            if fr[i][0] == fr[j][0]:      # el solape dentro de un mismo tramo
                continue                  # no es el defecto que se persigue
            a, b = norm(fr[i][1]), norm(fr[j][1])
            if not a or not b:
                continue
            jac = len(a & b) / len(a | b)
            if jac >= umbral:
                hits.append((jac, fr[i][1][:90], fr[j][1][:90]))
    return hits, len(fr)


def main(argv):
    if len(argv) < 2:
        raise SystemExit('Uso: solape.py <dir_txt> [umbral]')
    dir_txt = os.path.abspath(argv[1])
    umbral = float(argv[2]) if len(argv) > 2 else 0.55
    if not os.path.isdir(dir_txt):
        raise SystemExit(f'ABORTADO: no existe el directorio {dir_txt}')
    caps = capitulos_de(dir_txt)
    if not caps:
        raise SystemExit(f'ABORTADO: ni un «capNN_bM.txt» en {dir_txt}')
    total = 0
    for cap in sorted(caps):
        hits, n_frases = pares_solapados(caps[cap], umbral)
        total += len(hits)
        peor = f' · peor {max(hits)[0]:.2f}: «{max(hits)[1]}»' if hits else ''
        print(f'cap {cap:02d}: {len(hits):2d} pares ≥{umbral} '
              f'· frases {n_frases}{peor}')
    print('TOTAL pares solapados:', total)
    return 1 if total else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
