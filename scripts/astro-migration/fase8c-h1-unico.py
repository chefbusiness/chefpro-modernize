#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Un solo <h1> por página del blog.

El layout ya pinta el `title` del frontmatter como <h1>. Cuando el cuerpo trae
otro, la página sirve DOS, y eso pasó inadvertido nueve días tras el cutover
porque el <h1> del cuerpo llega por dos vías distintas:

  · HTML crudo `<h1 class="wp-block-heading">…</h1>`, herencia del export de WP.
  · Markdown `# Título`, que Astro compila a <h1> igual.

Un censo que sólo mire una de las dos —o sólo una carpeta de idioma— da un falso
verde. Aquí se miran las dos, en los dos idiomas.

QUÉ HACE CON CADA UNO, y por qué no es lo mismo:

  · **Idéntico al `title`** → se ELIMINA. Es la repetición literal del titular que
    el layout ya pinta; degradarlo a <h2> dejaría el mismo texto dos veces
    seguidas en pantalla.
  · **Distinto del `title`** → se degrada a <h2>. Ahí no hay duplicación sino un
    patrón deliberado: el `title` va recortado y optimizado para la SERP mientras
    el titular de la página es más largo y natural. Borrarlo perdería contenido
    escrito a propósito. Como <h2> hace de entradilla y el <h1> queda único.

Además hay un efecto que no es de SEO: un <h1> incrustado ESCONDE contenido a
cualquier parser que trocee el post por <h2>. En `recetario-cocina-creativa-ai`
había un bloque entero de 15 prompts bajo <h1>, invisible para el generador
inglés; en `burger-pro-ai`, la sección de tips completa.

Uso:
    python3 scripts/astro-migration/fase8c-h1-unico.py            # censo, no toca nada
    python3 scripts/astro-migration/fase8c-h1-unico.py --aplicar
"""
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BLOG = REPO / 'astro-site' / 'src' / 'content' / 'blog'
IDIOMAS = ('es', 'en')

RE_H1_HTML = re.compile(r'[ \t]*<h1([^>]*)>(.*?)</h1>[ \t]*\n?', re.S)
RE_H1_MD = re.compile(r'^# (?!#)(.+)$\n?', re.M)


def limpio(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>|[*_`]', '', s)).strip()


def analiza(p):
    """(frontmatter, cuerpo, título, [(clase, texto, 'html'|'md', match)])"""
    t = p.read_text(encoding='utf-8')
    cabeza, fm, cuerpo = t.split('---', 2)
    m = re.search(r'^title: "(.*?)"$', fm, re.M | re.S)
    titulo = limpio(m.group(1)) if m else ''
    hallazgos = [('html', limpio(x.group(2)), x) for x in RE_H1_HTML.finditer(cuerpo)]
    hallazgos += [('md', limpio(x.group(1)), x) for x in RE_H1_MD.finditer(cuerpo)]
    return cabeza, fm, cuerpo, titulo, hallazgos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--aplicar', action='store_true')
    args = ap.parse_args()

    quitados = degradados = 0
    for lang in IDIOMAS:
        for p in sorted((BLOG / lang).glob('*.md')):
            cabeza, fm, cuerpo, titulo, hallazgos = analiza(p)
            if not hallazgos:
                continue
            # De atrás hacia delante: cada sustitución mueve los índices siguientes.
            for tipo, texto, m in sorted(hallazgos, key=lambda h: h[2].start(), reverse=True):
                if texto == titulo:
                    accion, nuevo = 'elimina (duplica el title)', ''
                    quitados += 1
                elif tipo == 'html':
                    accion = 'h1 → h2 (titular propio)'
                    nuevo = '<h2%s>%s</h2>\n' % (m.group(1), m.group(2))
                    degradados += 1
                else:
                    accion = '# → ## (titular propio)'
                    nuevo = '## %s\n' % m.group(1)
                    degradados += 1
                print('  [%s] %-46s %s' % (lang, p.stem[:46], accion))
                cuerpo = cuerpo[:m.start()] + nuevo + cuerpo[m.end():]
            if args.aplicar:
                p.write_text('---'.join([cabeza, fm, cuerpo]), encoding='utf-8')

    total = quitados + degradados
    print('\n%s' % ('─' * 70))
    print('%d <h1> en el cuerpo: %d eliminados (duplicaban el title), %d degradados a h2'
          % (total, quitados, degradados))
    if total and not args.aplicar:
        print('Censo solamente. Añade --aplicar para escribirlo.')
    sys.exit(1 if total and not args.aplicar else 0)


if __name__ == '__main__':
    main()
