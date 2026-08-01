#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Restos de WordPress serializados en el cuerpo de los posts.

Bloques que en WordPress eran funcionales y al exportar quedaron congelados como
HTML muerto dentro del `.md`. No son contenido: son mobiliario del CMS anterior.

QUÉ QUITA, y por qué cada uno:

  · **wp-block-jetpack-donations** (35 posts) — «Haz una donación única / mensual
    / anual» con botones «Donar». Pide donaciones en el blog de un SaaS comercial,
    y los botones son `jetpack-donations-fallback-link`: enlaces SIN href, que no
    llevan a ninguna parte. Mete además 3 <h4> por post (105 encabezados falsos
    en total) que ensucian el esquema.

  · **CTA de newsletter del glosario** (1 post) — «📬 Suscríbete al Glosario»
    apuntando a /newsletter, que da 404, con la cifra «+2.500 chefs ya reciben
    nuestro contenido exclusivo». El formulario de newsletter del pie está
    explícitamente desconectado en el código (Footer.astro: «no wired»), así que
    no hay newsletter detrás ni forma de comprobar esa cifra. Decisión de John
    (2026-08-01): quitarlo.

Hermano de `fase8c-quitar-relacionados.py`, que se ocupa del widget de posts
relacionados. Mismo criterio: se delimita por firma estructural, nunca adivinando
dónde acaba.

Uso:
    python3 scripts/astro-migration/fase8c-restos-wordpress.py            # censo
    python3 scripts/astro-migration/fase8c-restos-wordpress.py --aplicar
"""
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BLOG = REPO / 'astro-site' / 'src' / 'content' / 'blog'

RESTOS = [
    ('donaciones Jetpack', re.compile(r'<div class="wp-block-jetpack-donations">.*?</div>\s*', re.S)),
]


def quita(cuerpo):
    fuera = []
    for nombre, patron in RESTOS:
        while True:
            m = patron.search(cuerpo)
            if not m:
                break
            # El bloque tiene que ser autocontenido: si hay un <div> anidado, el
            # primer </div> no es su cierre y el corte se comería contenido real.
            if '<div' in m.group(0)[40:]:
                sys.exit('⚠ %s: hay un <div> anidado, el corte no es fiable' % nombre)
            fuera.append((nombre, m.group(0)))
            cuerpo = cuerpo[:m.start()] + cuerpo[m.end():]
    return cuerpo, fuera


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--aplicar', action='store_true')
    args = ap.parse_args()

    tocados = 0
    for lang in ('es', 'en'):
        for p in sorted((BLOG / lang).glob('*.md')):
            txt = p.read_text(encoding='utf-8')
            cabeza, fm, cuerpo = txt.split('---', 2)
            limpio, fuera = quita(cuerpo)
            if not fuera:
                continue
            tocados += 1
            antes = len(re.sub(r'<[^>]+>', ' ', cuerpo).split())
            print('  [%s] %-52s −%d palabras · %d encabezados falsos · %s'
                  % (lang, p.stem[:52],
                     antes - len(re.sub(r'<[^>]+>', ' ', limpio).split()),
                     sum(len(re.findall(r'<h[1-6]', h)) for _, h in fuera),
                     ', '.join(sorted({n for n, _ in fuera}))))
            if args.aplicar:
                # Balance de <div>: si el corte lo rompiera, el HTML del post
                # quedaría mal anidado y el fallo no se vería hasta el navegador.
                a, c = len(re.findall(r'<div\b', limpio)), len(re.findall(r'</div>', limpio))
                if a != c:
                    sys.exit('⚠ %s: el corte desbalancea los <div> (%d/%d)' % (p.stem, a, c))
                p.write_text('---'.join([cabeza, fm, limpio]), encoding='utf-8')

    print('\n%s\n%d posts con restos%s' % ('─' * 72, tocados,
                                           ' — LIMPIADOS' if args.aplicar else ''))
    if tocados and not args.aplicar:
        print('Censo solamente. Añade --aplicar para escribirlo.')
    sys.exit(1 if tocados and not args.aplicar else 0)


if __name__ == '__main__':
    main()
