#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quita el bloque «También te puede interesar» congelado dentro del cuerpo.

QUÉ ES: un widget de posts relacionados que quedó SERIALIZADO en el HTML al
exportar de WordPress (bloque `wp-block-blocksy-query` del tema Blocksy). No es
contenido del post: es una consulta que en WordPress se resolvía en cada carga y
que aquí quedó congelada con los resultados de un día concreto de 2026.

POR QUÉ SE VA, con datos medidos (2026-08-01):

  · **Duplica al layout.** BlogPost.astro ya pinta sus propios relacionados de la
    misma categoría («Sigue leyendo» / «Keep reading»).
  · **Está muerto.** De los 7 destinos que enlaza, TRES dan 404:
    /catering-ai-plus/, /cocina-creativa/ y /mental-coach/. Son enlaces rotos
    dentro de contenido publicado, repetidos en 11 posts.
  · **Destroza el esquema de encabezados.** Mete entre 2 y 16 <h2> falsos por
    post —títulos de los posts relacionados—, uno de ellos repetido cinco veces.
  · **Disfraza contenido delgado.** En `que-es-el-food-pairing` el widget es el
    77 % del cuerpo y en `procesamiento-de-lenguaje-natural` el 84 %: posts que
    parecen largos y casi no tienen artículo.
  · **Envenena cualquier censo.** Por su culpa 5 librerías de prompts parecían
    tener 12-16 imágenes cuando las suyas son 2-9.

CÓMO SE DELIMITA, que es lo delicado: NO por «la siguiente sección conocida».
Se probó y se tragaba contenido real — `que-es-el-food-pairing` escribe
«Preguntas frecuentes» en minúscula y un patrón con mayúscula se llevaba por
delante toda su FAQ. Se usa la firma ESTRUCTURAL del bloque: el <h2> de cabecera,
seguido de `<div data-id="X" class="wp-block-blocksy-query">`, que cierra con su
propio `<style>[data-id='X']…</style></div>`. El data-id ata principio y fin.

Uso:
    python3 scripts/astro-migration/fase8c-quitar-relacionados.py            # censo
    python3 scripts/astro-migration/fase8c-quitar-relacionados.py --aplicar
"""
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BLOG = REPO / 'astro-site' / 'src' / 'content' / 'blog'
CABECERA = re.compile(r'<h2[^>]*>\s*También te [Pp]uede [Ii]nteresar\s*</h2>\s*')
APERTURA = re.compile(r'<div data-id="([^"]+)" class="wp-block-blocksy-query">')


def palabras(html):
    return len(re.sub(r'<[^>]+>', ' ', html).split())


def recorta(cuerpo):
    """Devuelve (cuerpo_limpio, [trozos_quitados]).

    Se parte del BLOQUE, no del encabezado. Buscarlo por el <h2> dejaba fuera 4
    posts donde la rejilla de tarjetas aparece a media página SIN título ninguno
    —peor para el lector: posts ajenos soltados en mitad del texto sin avisar—.
    Y hay un tercer caso: el <h2> huérfano sin bloque detrás.
    """
    quitados = []
    # De atrás hacia delante: cada corte mueve los índices de lo que va después.
    for ap in reversed(list(APERTURA.finditer(cuerpo))):
        cierre = re.compile(r"<style>\[data-id='%s'\].*?</style></div>"
                            % re.escape(ap.group(1)), re.S)
        fin = cierre.search(cuerpo, ap.end())
        if not fin:
            sys.exit('⚠ bloque %s abierto sin su <style> de cierre — no se toca'
                     % ap.group(1))
        # Si lleva su «También te puede interesar» justo delante, se va con él.
        ini = ap.start()
        cab = CABECERA.search(cuerpo[max(0, ini - 90):ini])
        if cab and (ini - (max(0, ini - 90) + cab.end())) <= 8:
            ini = max(0, ini - 90) + cab.start()
        quitados.append(cuerpo[ini:fin.end()])
        cuerpo = cuerpo[:ini] + cuerpo[fin.end():].lstrip('\n')
    # Encabezados HUÉRFANOS que quedan: prometen relacionados y no los dan. Se
    # quita solo el <h2>; el </div> que a veces le sigue cierra un contenedor
    # legítimo (los divs de estos posts están balanceados) y tocarlo rompe el HTML.
    while True:
        cab = CABECERA.search(cuerpo)
        if not cab:
            break
        quitados.append(cab.group(0))
        cuerpo = cuerpo[:cab.start()] + cuerpo[cab.end():]
    return cuerpo, quitados


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--aplicar', action='store_true')
    args = ap.parse_args()

    tocados, delgados = 0, []
    for lang in ('es', 'en'):
        for p in sorted((BLOG / lang).glob('*.md')):
            txt = p.read_text(encoding='utf-8')
            cabeza, fm, cuerpo = txt.split('---', 2)
            limpio, trozos = recorta(cuerpo)
            if not trozos:
                continue
            tocados += 1
            widget = ''.join(trozos)
            antes, despues = palabras(cuerpo), palabras(limpio)
            print('  [%s] %-46s −%d palabras (%d → %d) · %d h2 falsos · %d imgs%s'
                  % (lang, p.stem[:46], antes - despues, antes, despues,
                     len(re.findall(r'<h2', widget)), len(re.findall(r'<img', widget)),
                     '' if len(trozos) == 1 else ' · %d bloques' % len(trozos)))
            if despues < 400:
                delgados.append((p.stem, despues))
            if args.aplicar:
                p.write_text('---'.join([cabeza, fm, limpio]), encoding='utf-8')

    print('\n%s' % ('─' * 72))
    print('%d posts con el widget%s' % (tocados, ' — LIMPIADOS' if args.aplicar else ''))
    if delgados:
        print('\n⚠ QUEDAN POR DEBAJO DE 400 PALABRAS (contenido delgado que el widget '
              'disfrazaba; decidir si ampliar o consolidar):')
        for s, n in sorted(delgados, key=lambda x: x[1]):
            print('   %4d palabras  %s' % (n, s))
    if tocados and not args.aplicar:
        print('\nCenso solamente. Añade --aplicar para escribirlo.')
    sys.exit(1 if tocados and not args.aplicar else 0)


if __name__ == '__main__':
    main()
