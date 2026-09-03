#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fase 8F — Inserción QUIRÚRGICA de la «Guía Food Cost + Ingeniería de Menú» en
los 6 posts ES del tema (SPEC del producto, decisión D11).

POR QUÉ EXISTE: `fase8e-banners-corpus.py` salta todo post que ya lleve
banners (325/325 desde el 2026-08-31), así que un producto nuevo NO entra en
el blog reejecutando la rotación. Y el ensamblador `fase8c-libreria-assemble.py`
reconstruye el cuerpo entero y pisaría lo publicado. Este script hace dos cosas
y sólo dos, por post:
  1. sustituye UN banner existente (el menos afín, por lista de prioridad)
     por el de la guía, con el MISMO `banner()` y UTM del ensamblador;
  2. añade un párrafo con enlace contextual justo antes del primer `## `.
Y lo demuestra: deshace las dos ediciones sobre el resultado y exige que el
texto vuelva a ser IDÉNTICO al original. También sube el `modDate`.

    python3 scripts/astro-migration/fase8f-guia-food-cost-blog.py           # dry-run
    python3 scripts/astro-migration/fase8f-guia-food-cost-blog.py --apply
Después: python3 scripts/astro-migration/fase8b-regen-lastmod.py
"""
import argparse
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BLOG = ROOT / 'astro-site/src/content/blog/es'
PRODUCTO = 'guia-food-cost-ingenieria-menu'
HOY = '2026-09-03'

# El banner que se SUSTITUYE en cada post: el menos afín de los tres publicados
# (los kits de tareas de otro concepto, planes de negocio y guías de apertura
# no tienen nada que ver con un post de costes; kit-escandallos y kit-inventario
# NO se tocan nunca: son los afines).
PRIORIDAD_SUSTITUIR = ['kit-tareas-', 'plan-negocio-', 'guia-panaderia', 'guia-restaurante',
                       'guia-dark-kitchen', 'mega-pack', 'pro-prompts', 'pack-appcc',
                       'kit-gestion-personal', 'kit-plan-financiero']
NUNCA = ('kit-escandallos', 'kit-inventario', PRODUCTO)

POSTS = {
    '8-errores-que-destruyen-el-food-cost-en-tu-restaurante':
        'Los ocho errores de este artículo se corrigen con método, no con una fórmula suelta: '
        'el IVA por canal, el food cost teórico frente al real, el prime cost y la ingeniería de '
        'menú con varios modelos están desarrollados, con sus plantillas Excel, en la '
        '<a href="https://aichef.pro/guia-food-cost-ingenieria-menu">Guía Food Cost + Ingeniería de Menú</a>.',
    'food-cost-ia-escenarios-inflacionarios-2026':
        'Si quieres el protocolo completo de re-escandallado cuando sube el proveedor, con el '
        'simulador de precios por canal y la matriz de ingeniería de menú en Excel, está en la '
        '<a href="https://aichef.pro/guia-food-cost-ingenieria-menu">Guía Food Cost + Ingeniería de Menú</a>.',
    'mejores-calculadoras-food-cost-ia-comparativa':
        'Una calculadora te da el número; decidir qué hacer con él es otra disciplina. El método '
        'completo, con ocho herramientas Excel de fórmulas vivas, está en la '
        '<a href="https://aichef.pro/guia-food-cost-ingenieria-menu">Guía Food Cost + Ingeniería de Menú</a>.',
    'escandallos-ia-cocina-profesional':
        'Este artículo enseña a escandallar un plato. Lo que viene después —fijar el precio por '
        'cuatro métodos, clasificar la carta y ajustar el delivery— lo desarrolla la '
        '<a href="https://aichef.pro/guia-food-cost-ingenieria-menu">Guía Food Cost + Ingeniería de Menú</a>.',
    'carta-restaurante-rentable-ingenieria-menu-ia':
        'La matriz de este artículo es la de Kasavana y Smith. Cruzarla con Miller, Pavesic y el '
        'Goal Value, y ver en qué platos discrepan, es el corazón de la '
        '<a href="https://aichef.pro/guia-food-cost-ingenieria-menu">Guía Food Cost + Ingeniería de Menú</a>, '
        'que trae la matriz multi-método en Excel.',
    'que-son-las-mermas-en-cocina':
        'La merma medida con tu proveedor y tu cuchillo, y no la de una tabla genérica, es el '
        'primer capítulo práctico de la '
        '<a href="https://aichef.pro/guia-food-cost-ingenieria-menu">Guía Food Cost + Ingeniería de Menú</a>, '
        'que incluye la plantilla del test de rendimiento.',
}

RX_ASIDE = re.compile(r'<aside class="not-prose[^"]*">.*?utm_medium=banner.*?</aside>', re.S)
RX_SLUG = re.compile(r'href="/([a-z0-9-]+)\?utm_source=blog')


def cargar_ensamblador():
    ruta = ROOT / 'scripts/astro-migration/fase8c-libreria-assemble.py'
    spec = importlib.util.spec_from_file_location('asm', ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def elegir_victima(slugs):
    for pref in PRIORIDAD_SUSTITUIR:
        for s in slugs:
            if s.startswith(pref) and not s.startswith(NUNCA):
                return s
    sys.exit('ningún banner sustituible en %s' % slugs)


def procesar(slug, texto, mod, prods):
    asides = RX_ASIDE.findall(texto)
    if len(asides) != 3:
        sys.exit('%s: esperaba 3 banners, hay %d' % (slug, len(asides)))
    slugs = [RX_SLUG.search(a).group(1) for a in asides]
    if PRODUCTO in slugs:
        sys.exit('%s: ya lleva el banner del producto' % slug)
    victima = elegir_victima(slugs)
    viejo = asides[slugs.index(victima)]
    nuevo = mod.banner(PRODUCTO, prods, slug, 'es')
    assert texto.count(viejo) == 1
    salida = texto.replace(viejo, nuevo)

    parrafo = '<p>' + POSTS[slug] + '</p>'
    m = re.search(r'^## ', salida, re.M)
    if not m:
        sys.exit('%s: sin «## » donde anclar el párrafo' % slug)
    pos = m.start()
    antes = '' if salida[:pos].endswith('\n\n') else '\n'
    salida = salida[:pos] + antes + parrafo + '\n\n' + salida[pos:]

    md_old = re.search(r'^modDate: (\d{4}-\d{2}-\d{2})$', salida, re.M)
    assert md_old, '%s: sin modDate' % slug
    salida = salida.replace(md_old.group(0), 'modDate: ' + HOY, 1)

    # Gate: deshacer las tres ediciones devuelve el original byte a byte.
    deshecho = salida.replace(nuevo, viejo).replace(antes + parrafo + '\n\n', '', 1)
    deshecho = deshecho.replace('modDate: ' + HOY, md_old.group(0), 1)
    if deshecho != texto:
        sys.exit('%s: el gate de reversibilidad NO cuadra' % slug)
    assert len(RX_ASIDE.findall(salida)) == 3
    return salida, victima


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()
    mod = cargar_ensamblador()
    prods = mod.catalogo_productos()
    if PRODUCTO not in prods:
        sys.exit('el producto no está en products-catalog.ts')
    for slug in POSTS:
        ruta = BLOG / (slug + '.md')
        texto = ruta.read_text(encoding='utf-8')
        salida, victima = procesar(slug, texto, mod, prods)
        print('%s %-58s sustituye %-32s +%d bytes' % (
            'APPLY ' if args.apply else 'dry   ', slug, victima, len(salida) - len(texto)))
        if args.apply:
            ruta.write_text(salida, encoding='utf-8')
    if not args.apply:
        print('(dry-run: nada escrito; --apply para aplicar)')


if __name__ == '__main__':
    main()
