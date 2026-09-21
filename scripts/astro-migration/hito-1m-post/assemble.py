#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hito 1M (2026-09-21) — ensambla el post «AI Chef Pro supera el millón de consultas».

Copia adaptada de fase12-post-assemble.py (misma lógica de reparto e idénticos gates).

QUÉ MONTA: frontmatter (con la FAQ, que es la que emite el FAQPage) + el cuerpo
que ha escrito bridge.py + 2 imágenes de cuerpo + 3 banners de producto a tres
alturas.

DECISIONES QUE VIENEN DEL REPO, no de aquí:
  · NADA de H1 en el cuerpo. El layout ya pinta el `title` como <h1> y meter otro
    da doble H1 (gate: fase8c-h1-unico.py). Al brief de bridge se le dice y aquí
    se comprueba.
  · Los BANNERS sólo en ES y EN. El catálogo de productos
    (src/data/products-catalog.ts) sólo tiene nombre y descripción en esos dos
    idiomas, y las landings de producto tampoco existen en los otros. Medido el
    2026-09-05: los 49 posts de los blogs FR/DE/IT/PT tienen CERO banners. Poner
    uno en francés mandaría al lector a un checkout en español.
  · La imagen destacada NO se repite en el cuerpo (regla capital): son 3 ficheros
    distintos, uno destacado y dos de cuerpo.
  · Los 3 banners salen de rotar_productos(), sembrado con el slug del post, para
    no vender siempre los mismos cuatro productos.

Uso:
    python3 fase12-post-assemble.py --lang es --cuerpo <fichero.md>
"""
import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
BLOG = RAIZ / 'astro-site' / 'src' / 'content' / 'blog'

# Se reutiliza el ensamblador de librerías en vez de duplicar su lógica: su
# catalogo_productos() lleva el gate que aborta si el parser ve menos productos
# de los declarados (ver CLAUDE.md, el parser perdía entradas en silencio).
_spec = importlib.util.spec_from_file_location(
    'lib8c', Path(__file__).resolve().parent.parent / 'fase8c-libreria-assemble.py')
_lib = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_lib)

IMG_DIR = '/blog-assets/2026/09'
FECHA = '2026-09-22'

# Productos temáticamente afines: el post habla de escandallos, fichas técnicas y
# gestión, así que esos van fijados y el resto los completa la rotación.
FIJADOS = ['pro-prompts-ebook']

COPY = Path(__file__).parent / 'copy'


def carga_meta(lang):
    """El copy vive en fase12-post-copy/<lang>.json (el español lo escribe una
    persona; los otros cinco salen de fase12-post-traducir.py)."""
    f = COPY / ('%s.json' % lang)
    if not f.exists():
        sys.exit('falta el copy de %s (%s)' % (lang, f))
    return json.loads(f.read_text(encoding='utf-8'))


def inserta(cuerpo, piezas):
    """Reparte `piezas` entre los BLOQUES de nivel superior del cuerpo.

    El cuerpo se trocea por líneas en blanco, así que una tabla de Markdown
    entera es UN bloque y es imposible insertar en mitad de ella —que es el
    fallo que parte la tabla en dos sin que el diff cante—. Se descartan además:

      · los dos primeros bloques (la entradilla se lee de un tirón), y
      · el hueco justo DEBAJO de un encabezado, que separaría el H2 de su
        primer párrafo.

    El reparto es uniforme sobre los huecos que quedan, para que las piezas
    caigan a distintas alturas y no apelotonadas al final.
    """
    bloques = [b for b in cuerpo.split('\n\n') if b.strip()]

    huecos = [i for i in range(2, len(bloques))
              if not bloques[i - 1].lstrip().startswith('#')]
    if len(huecos) < len(piezas):
        sys.exit('sólo hay %d huecos válidos para %d piezas — cuerpo demasiado corto'
                 % (len(huecos), len(piezas)))

    # reparto uniforme: la pieza k va al hueco que le toca por proporción
    elegidos = [huecos[round(k * (len(huecos) - 1) / max(1, len(piezas) - 1))]
                for k in range(len(piezas))]
    # si dos piezas caen en el mismo hueco, se empujan al siguiente libre
    vistos = set()
    limpio = []
    for pos in elegidos:
        while pos in vistos and pos < len(bloques):
            pos += 1
        vistos.add(pos)
        limpio.append(pos)

    for pos, pieza in sorted(zip(limpio, piezas), reverse=True):
        bloques.insert(min(pos, len(bloques)), pieza)
    return '\n\n'.join(bloques)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', default='es')
    ap.add_argument('--cuerpo', required=True, help='.md que ha devuelto bridge')
    ap.add_argument('--aplicar', action='store_true')
    ap.add_argument('--out', default=None, help='escribe el .md aquí (vista previa) en vez de en el blog')
    args = ap.parse_args()

    lang = args.lang
    m = carga_meta(lang)
    slug = m['slug']

    cuerpo = Path(args.cuerpo).read_text(encoding='utf-8').strip()

    # Gates sobre lo que ha devuelto el modelo, ANTES de montar nada.
    if re.search(r'^# ', cuerpo, re.M):
        sys.exit('el cuerpo trae un H1 — el layout ya pinta uno (ver fase8c-h1-unico.py)')
    if cuerpo.startswith('```'):
        sys.exit('el cuerpo viene envuelto en ``` — límpialo antes')
    raro = re.search(r'[　-鿿Ѐ-ӿ가-힯؀-ۿ]', cuerpo)
    if raro:
        sys.exit('caracteres de otro alfabeto en el cuerpo: %r' % raro.group(0))
    palabras = len(cuerpo.split())
    if palabras < 700:
        sys.exit('sólo %d palabras: por debajo del mínimo del blog' % palabras)

    # --- imágenes de cuerpo (la destacada NO se repite aquí) ---
    figs = [
        '<figure class="wp-block-image size-large"><img decoding="async" '
        'src="%s/un-millon-comparar-modelos.jpg" alt="%s" loading="lazy" /></figure>'
        % (IMG_DIR, m['alt_modelos']),
        '<figure class="wp-block-image size-large"><img decoding="async" '
        'src="%s/un-millon-agentes-afinados.jpg" alt="%s" loading="lazy" /></figure>'
        % (IMG_DIR, m['alt_afinados']),
    ]

    # --- banners: sólo ES y EN (ver cabecera) ---
    banners = []
    if lang in ('es', 'en'):
        prods = _lib.catalogo_productos()
        elegidos = _lib.rotar_productos(slug, prods, fijados=FIJADOS, n=3)
        banners = [_lib.banner(p, prods, slug, lang) for p in elegidos]
        print('banners: %s' % ', '.join(elegidos))
    else:
        print('banners: ninguno (el catálogo de productos sólo existe en es/en)')

    # Se INTERCALAN imágenes y banners. Si se pasan en bloque, el repartidor
    # uniforme mete las dos fotos arriba y los tres banners seguidos abajo, que
    # es justo lo contrario de «tres alturas del artículo».
    piezas = []
    for i in range(max(len(figs), len(banners))):
        if i < len(figs):
            piezas.append(figs[i])
        if i < len(banners):
            piezas.append(banners[i])

    # Enlace interno a la landing. El post es el anuncio; la landing es la
    # referencia permanente, así que el artículo tiene que empujar hacia ella.
    # Convención del repo: enlace ABSOLUTO (2.278 usos frente a 28 relativos).

    cuerpo = inserta(cuerpo, piezas)

    # --- frontmatter ---
    def esc(s):
        return s.replace('"', '\\"')

    fm = ['---',
          'title: "%s"' % esc(m['title']),
          'description: "%s"' % esc(m['description']),
          'pubDate: %s' % FECHA,
          # Sin modDate el post no entra en blog-lastmod.json y el sitemap lo
          # anuncia sin fecha (lo canta fase8b-regen-lastmod.py).
          'modDate: %s' % FECHA,
          'category: ai-chef-pro']
    # hreflang recíproco ES↔EN: es el MISMO contenido adaptado, así que el par es
    # verdadero (el esquema sólo admite es/en/it, y fr/de/pt no tienen pareja
    # declarable). Va aquí y no a mano: reensamblar el post lo borraba.
    PAREJA = {'es': ('en', 'ai-chef-pro-one-million-queries'),
              'en': ('es', 'ai-chef-pro-un-millon-de-consultas')}
    if lang in PAREJA:
        otro, otro_slug = PAREJA[lang]
        fm += ['translations:', '  %s: "%s"' % (otro, otro_slug)]
    fm += ['image: %s/un-millon-destacada.jpg' % IMG_DIR,
          'imageAlt: "%s"' % esc(m['alt_destacada']),
          'lang: %s' % lang,
          'faq:']
    for f in m['faq']:
        fm.append('  - q: "%s"' % esc(f['q']))
        fm.append('    a: "%s"' % esc(f['a']))
    fm.append('---')

    md = '\n'.join(fm) + '\n\n' + cuerpo + '\n'

    destino = BLOG / lang / ('%s.md' % slug)
    print('\n%s — %d palabras, %d banners, %d imágenes de cuerpo'
          % (destino.relative_to(RAIZ), palabras,
             md.count('utm_medium=banner'), md.count('<figure')))
    print('meta description: %d caracteres' % len(m['description']))

    if args.out:
        Path(args.out).write_text(md, encoding='utf-8')
        print('vista previa escrita en %s' % args.out)
    elif args.aplicar:
        destino.write_text(md, encoding='utf-8')
        print('ESCRITO')
    else:
        print('DRY-RUN — usa --aplicar')


if __name__ == '__main__':
    main()
