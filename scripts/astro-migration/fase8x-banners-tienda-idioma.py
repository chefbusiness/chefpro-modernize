#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Re-apunta los banners de un producto en el blog de OTRO idioma a su landing de esa tienda.

Por qué (TIENDA-INTERNACIONAL.md §3.10, 25-sep-2026): cuando un producto nace en la tienda
inglesa, sus banners del blog EN siguen vendiendo la landing ESPAÑOLA con el nombre y el
precio de antes («Get Recipe Costing Kit Pro for €12» → /kit-escandallos). El catálogo
(`src/data/products-catalog.ts`) ya sabe la landing y el precio de cada tienda (`urlByLang`,
`priceByLang`), pero lo publicado no se entera solo: hay que pasar por el corpus.

Y eso NO lo puede hacer el ensamblador (`fase8c-libreria-assemble.py`), que reconstruye el
cuerpo entero desde el .txt de bridge y pisa lo publicado (CLAUDE.md). Esto es un parche
quirúrgico: solo toca el `<aside>` del banner.

Qué hace, por post de `astro-site/src/content/blog/<lang>/`:
  1. Localiza cada `<aside>…</aside>` que enlaza a la landing ES del producto con UTM de
     banner (`?utm_source=blog&amp;utm_medium=banner&amp;utm_content=<x>`).
  2. Lo sustituye por `banner(producto, catálogo, <x>, lang)` del ensamblador (importado, no
     copiado): nombre, landing y precio del catálogo, y el MISMO `utm_content`.
  3. Gates, por banner y por fichero:
     - el banner viejo tiene que ser el mismo molde que el nuevo con solo tres campos
       distintos (nombre, URL y texto del botón); si difiere en algo más, no se toca;
     - deshacer (nuevo → viejo) devuelve el fichero original BYTE A BYTE;
     - fuera de los banners, el fichero no cambia ni un carácter.
  No toca el `modDate`: el artículo no cambia; cambia a dónde apunta un banner de producto.

Uso:
    python3 scripts/astro-migration/fase8x-banners-tienda-idioma.py --producto kit-escandallos --lang en
    python3 scripts/astro-migration/fase8x-banners-tienda-idioma.py --producto kit-escandallos --lang en --aplicar

Dry-run por defecto. Idempotente: un banner que ya es el del catálogo se cuenta y no se toca.
"""
import argparse
import html
import importlib.util
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BLOG = REPO / 'astro-site' / 'src' / 'content' / 'blog'
ASSEMBLE = Path(__file__).parent / 'fase8c-libreria-assemble.py'
ASIDE = re.compile(r'<aside\b(?:(?!</aside>).)*?</aside>', re.S)


def cargar_ensamblador():
    spec = importlib.util.spec_from_file_location('fase8c_assemble', ASSEMBLE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def campos(bloque):
    """(nombre del h3, href, texto del botón) de un banner, o None si no tiene el molde."""
    m = re.search(r'<h3\b[^>]*>(.*?)</h3>.*?<a href="([^"]+)"[^>]*>(.*?)</a>\s*</aside>$', bloque, re.S)
    return m.groups() if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--producto', required=True, help='id del catálogo (p. ej. kit-escandallos)')
    ap.add_argument('--lang', required=True, help='idioma del corpus y de la tienda (p. ej. en)')
    ap.add_argument('--aplicar', action='store_true', help='escribe los .md (sin esto, dry-run)')
    args = ap.parse_args()

    mod = cargar_ensamblador()
    prods = mod.catalogo_productos()
    if args.producto not in prods:
        sys.exit('%s no está en products-catalog.ts' % args.producto)
    d = prods[args.producto]
    url_es = d['url']
    url_lang = mod.url_producto(d, args.lang)
    if url_lang == url_es:
        sys.exit('%s no tiene landing propia en %r (urlByLang): no hay nada que re-apuntar'
                 % (args.producto, args.lang))
    corpus = BLOG / args.lang
    if not corpus.is_dir():
        sys.exit('no existe el corpus %s' % corpus)

    utm = re.compile(r'href="(?:%s|%s)\?utm_source=blog&amp;utm_medium=banner&amp;utm_content=([\w-]+)"'
                     % (re.escape(url_es), re.escape(url_lang)))
    cambiados, ya, errores, ficheros = 0, 0, [], []
    for md in sorted(corpus.glob('*.md')):
        orig = md.read_text(encoding='utf-8')
        trozos, cursor, sustituciones = [], 0, []
        for m in ASIDE.finditer(orig):
            viejo = m.group(0)
            u = utm.search(viejo)
            if not u:
                continue
            nuevo = mod.banner(args.producto, prods, u.group(1), args.lang)
            if viejo == nuevo:
                ya += 1
                continue
            cv, cn = campos(viejo), campos(nuevo)
            if not cv or not cn:
                errores.append('%s: banner sin el molde esperado' % md.name)
                continue
            # Mismo molde, solo tres campos distintos: el nuevo con los campos del viejo
            # tiene que reproducir el viejo exacto.
            reconstruido = nuevo
            for a, b in zip(cn, cv):
                reconstruido = reconstruido.replace(a, b, 1)
            if reconstruido != viejo:
                errores.append('%s: el banner difiere en algo más que nombre, URL y botón; '
                               'no se toca' % md.name)
                continue
            trozos.append(orig[cursor:m.start()])
            trozos.append(nuevo)
            cursor = m.end()
            sustituciones.append((viejo, nuevo, cv, cn))
        if not sustituciones:
            continue
        trozos.append(orig[cursor:])
        salida = ''.join(trozos)
        # Gate 1: deshacer devuelve el original byte a byte.
        deshecho = salida
        for viejo, nuevo, _, _ in sustituciones:
            deshecho = deshecho.replace(nuevo, viejo, 1)
        if deshecho != orig:
            errores.append('%s: GATE — deshacer no devuelve el original' % md.name)
            continue
        # Gate 2: fuera de los banners no cambia nada.
        if ASIDE.sub('', salida) != ASIDE.sub('', orig):
            errores.append('%s: GATE — cambió algo fuera de los banners' % md.name)
            continue
        cambiados += len(sustituciones)
        ficheros.append(md)
        for viejo, nuevo, cv, cn in sustituciones:
            print('%s\n   %s | %s | %s\n → %s | %s | %s'
                  % (md.name, html.unescape(cv[0]), cv[1], html.unescape(cv[2]),
                     html.unescape(cn[0]), cn[1], html.unescape(cn[2])))
        if args.aplicar:
            md.write_text(salida, encoding='utf-8')

    print('\n%s: %d banner(es) re-apuntados en %d post(s) · %d ya al día · %d error(es)'
          % ('APLICADO' if args.aplicar else 'DRY-RUN', cambiados, len(ficheros), ya, len(errores)))
    for e in errores:
        print('  ⛔', e)
    sys.exit(1 if errores else 0)


if __name__ == '__main__':
    main()
