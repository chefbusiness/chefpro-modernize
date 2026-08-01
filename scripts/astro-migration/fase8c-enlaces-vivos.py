#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gate: ningún enlace interno del blog puede apuntar a un 404.

Nació de un hallazgo por casualidad (2026-08-01): al desmontar el widget de
relacionados congelado apareció que enlazaba a /catering-ai-plus/, /cocina-creativa/
y /mental-coach/, tres páginas que ya no existen, repetidas en 11 posts. El
barrido completo destapó otras cuatro: /food-pairing-ai, /gastro-lexicum,
/id-alergenos y /mermas-gencal (landings de agente que nunca se migraron),
/blog/libreria-de-prompts (el hub vive en la raíz, sin /blog) y /mentoria (es
/mentoria-online).

Ninguna se veía desde el repo: son URLs absolutas a aichef.pro dentro del HTML de
los posts, así que solo se detectan preguntándole a producción.

Deduplica antes de consultar —4.100 enlaces se reducen a ~195 destinos— y por eso
tarda dos minutos y no una hora.

Uso:
    python3 scripts/astro-migration/fase8c-enlaces-vivos.py
    python3 scripts/astro-migration/fase8c-enlaces-vivos.py --base http://localhost:4321
"""
import argparse
import collections
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BLOG = REPO / 'astro-site' / 'src' / 'content' / 'blog'
PROD = 'https://aichef.pro'


def censo():
    """{destino normalizado: {posts que lo enlazan}}"""
    dest = collections.defaultdict(set)
    for lang in ('es', 'en'):
        for p in sorted((BLOG / lang).glob('*.md')):
            for h in re.findall(r'href="(https://aichef\.pro[^"]*)"',
                                p.read_text(encoding='utf-8')):
                # Se tira el query (los UTM no cambian el destino) y la barra final.
                u = h.split('?')[0].replace('&#038;', '&').rstrip('/') or PROD
                dest[u].add('%s/%s' % (lang, p.stem))
    return dest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', default=PROD,
                    help='sustituye el host para probar contra un preview local')
    args = ap.parse_args()

    dest = censo()
    print('%d destinos internos únicos en %d enlaces — consultando…\n'
          % (len(dest), sum(len(v) for v in dest.values())))
    rotos = []
    for u in sorted(dest):
        destino = u.replace(PROD, args.base.rstrip('/'))
        code = subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}',
                               '-L', '--max-time', '15', destino],
                              capture_output=True, text=True).stdout.strip()
        if code != '200':
            rotos.append((code, u, sorted(dest[u])))

    for code, u, posts in rotos:
        print('⛔ %s  %s' % (code, u.replace(PROD, '')))
        print('      lo enlazan: %s%s'
              % (', '.join(posts[:4]), ' y %d más' % (len(posts) - 4) if len(posts) > 4 else ''))
    print('\n%s' % ('─' * 72))
    print('%d destinos · %d rotos' % (len(dest), len(rotos)))
    sys.exit(1 if rotos else 0)


if __name__ == '__main__':
    main()
