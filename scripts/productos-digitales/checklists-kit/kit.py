#!/usr/bin/env python3
"""
kit.py — elige el kit del circuito de checklists EN: el base (Restaurant Checklists Kit Pro) o un vertical.
Sesión Claude Code, 18-oct-2026 (Bar Checklists Kit Pro, el primer hermano; SPEC base §9). Verticales dados de
alta: VERTICALES (bar = Bar Checklists Kit Pro · cafe = Coffee Shop Checklists Kit Pro · catering = Catering
Checklists Kit Pro, con el 09 como libro propio: cobros por evento, no caja · pizza = Pizza Shop Checklists Kit Pro ·
burger = Burger Joint Checklists Kit Pro · ghost = Ghost Kitchen Checklists Kit Pro · icecream = Ice Cream Shop
Checklists Kit Pro, molde híbrido: el 01-07 y los bonus en el molde ligero del catering, el 08 y el 09 en el del base ·
chocolate = Chocolate Shop Checklists Kit Pro · pastry = Pastry Shop Checklists Kit Pro, con 4 libros propios del 10 al 13 ·
hotel = Hotel Checklists Kit Pro, 19 libros: 01-15 y los bonus en el molde ligero, el 18 y el 19 = el 08 y el 09 del base ·
taco = Taco Shop Checklists Kit Pro, mapa de libros propio en el molde del base y SIN libro de caja ·
foodtruck = Food Truck Checklists Kit Pro, el primero en el MOLDE PLANO de origen ChefBusiness: una hoja por libro,
sin «Instrucciones», sin contadores ni versión, título en A2 y SIN libro de caja; ganchos de F2 en foodtruck/SPEC.md).

    python3 extraer_textos.py --kit bar          # o CHECKLISTS_KIT=bar python3 extraer_textos.py
    python3 extraer_textos.py --kit cafe
    python3 extraer_textos.py --kit catering
    python3 extraer_textos.py --kit pizza
    python3 extraer_textos.py --kit burger
    python3 extraer_textos.py --kit ghost
    python3 extraer_textos.py --kit icecream
    python3 extraer_textos.py --kit chocolate
    python3 extraer_textos.py --kit pastry
    python3 extraer_textos.py --kit hotel
    python3 extraer_textos.py --kit taco
    python3 extraer_textos.py --kit foodtruck

Sin --kit (ni la variable) todo es el kit base de siempre, byte a byte: `mapas.py`, origen `dl/kit-tareas` y los
datos junto a los scripts (censo_es.json, textos_es.json, textos_en/). Con --kit <v>:

  · mapas  = <v>/mapas_<v>.py: importa `mapas.py` y SOLO añade o sobrescribe lo del vertical (pestañas, puestos,
             POR_CELDA, ADAPTAR, ficheros, producto). Lo demás (glosario, hora_us, caja, calendario US) se hereda.
  · DATOS  = <v>/ (censo_es.json, textos_es.json, textos_en/ con heredado.json + G<n>.json).
  · ORIGEN = dl/<mapas.ORIGEN_ES> (p. ej. dl/kit-tareas-bar), SOLO LECTURA.

El kit queda en la variable de entorno para que lo hereden los subprocesos. Importable sin efectos salvo esa
variable y sys.path.
"""
import importlib
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)


def _de_argv(argv):
    for i, x in enumerate(argv):
        if x == '--kit' and i + 1 < len(argv):
            return argv[i + 1]
        if x.startswith('--kit='):
            return x.split('=', 1)[1]
    return None


VERTICALES = ('bar', 'cafe', 'catering', 'pizza', 'burger', 'ghost', 'icecream', 'chocolate', 'pastry', 'hotel',
              'taco', 'foodtruck')     # <v>/mapas_<v>.py, SPEC en <v>/SPEC.md
NOMBRE = _de_argv(sys.argv) or os.environ.get('CHECKLISTS_KIT') or 'base'
os.environ['CHECKLISTS_KIT'] = NOMBRE
BASE = NOMBRE == 'base'

import mapas as mapas_base                                       # noqa: E402

if BASE:
    mapas = mapas_base
    DATOS = AQUI
else:
    DATOS = os.path.join(AQUI, NOMBRE)
    if not os.path.isfile(os.path.join(DATOS, 'mapas_%s.py' % NOMBRE)):
        raise SystemExit('kit desconocido %r: falta %s/mapas_%s.py' % (NOMBRE, NOMBRE, NOMBRE))
    if DATOS not in sys.path:
        sys.path.insert(0, DATOS)
    mapas = importlib.import_module('mapas_' + NOMBRE)

ORIGEN = os.path.join(REPO, 'astro-site', 'public', 'dl', getattr(mapas, 'ORIGEN_ES', 'kit-tareas'))
TEXTOS_EN = os.path.join(DATOS, 'textos_en')


def argumento(ap):
    """Declara --kit en el argparse de cada script (ya se leyó al importar este módulo)."""
    ap.add_argument('--kit', default=NOMBRE,
                    help='kit: base (Restaurant) o un vertical con <v>/mapas_<v>.py (%s)' % ', '.join(VERTICALES))
