#!/usr/bin/env python3
"""
mapas.py — Recipe Costing Kit Pro (EN) · mapas ES→EN y tabla `Conversions` generada.

SPEC: `scripts/productos-digitales/recipe-costing-kit/SPEC.md` (D7, D8, D9, §2.2, §2.3, §2.4).

Importable SIN efectos (solo constantes y funciones). Ejecutado como script corre el
autotest y, si existe `censo_es.json` al lado, lo cruza con el censo del ES v2.1:

    python3 mapas.py            # autotest + resumen
    python3 mapas.py --json     # además vuelca la tabla Conversions en JSON por stdout

Contenido:
  · FICHEROS            nombres de fichero ES→EN (research §1.2 + D17).
  · HOJAS               nombres de pestaña ES→EN (D9 + research §1.3; 12/13; «Mermas» → «Trim Loss Factors»).
  · HOJAS_ES_POR_LIBRO  pestañas de cada libro ES v2.1, en orden (para validar unicidad por libro).
  · CATEGORIAS          las 21 categorías de merma (research §1.4), en el orden de la hoja.
  · UNIDADES            unidades del desplegable ES → clave EN (§2.3: ud→each, docena→dozen…).
  · MOTIVOS             los 7 motivos de la DV del BONUS.
  · DV12                los 3 tipos del libro 12 (DV y literales de SUMIF).
  · LITERALES           literales de fórmula que se traducen (§2.4) y LITERALES_SIN_CAMBIO.
  · LISTA_UNIDADES_EN   la lista literal de la DV de unidades (D7 / E5), ≤ 255 caracteres.
  · conversions()       genera la tabla `Conversions` con la REGLA CERRADA de D7.
  · rango_vlookup(n) / area_impresion(n)  (E2).
  · autotest()          comprobaciones; devuelve un dict con n y los recuentos.

Factores exactos por definición (NIST Handbook 44, Appendix C): 1 lb = 0,45359237 kg;
1 US fl oz = 29,5735295625 ml; 1 imp gal = 4,54609 L. Se calculan con `fractions.Fraction`
y se escriben como float.
"""
import json
import os
import re
from collections import OrderedDict
from fractions import Fraction as Fr

AQUI = os.path.dirname(os.path.abspath(__file__))

# ==========================================================================
# 1. Ficheros (research §1.2; 12 y 13 de D17)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-escandallo-estandar.xlsx', '01-standard-recipe-cost-card.xlsx'),
    ('02-menu-degustacion.xlsx', '02-tasting-menu.xlsx'),
    ('03-menu-del-dia.xlsx', '03-prix-fixe-lunch-menu.xlsx'),
    ('04-cocktails-bebidas.xlsx', '04-cocktails-and-drinks.xlsx'),
    ('05-pasteleria.xlsx', '05-pastry-and-bakery.xlsx'),
    ('06-catering.xlsx', '06-catering-and-events.xlsx'),
    ('07-cafeteria-brunch.xlsx', '07-cafe-and-brunch.xlsx'),
    ('08-food-truck.xlsx', '08-food-truck.xlsx'),
    ('09-control-mermas.xlsx', '09-food-waste-tracker.xlsx'),
    ('10-calculadora-pvp.xlsx', '10-menu-price-calculator.xlsx'),
    ('11-dashboard-food-cost-mensual.xlsx', '11-monthly-food-cost-dashboard.xlsx'),
    ('12-test-de-rendimiento.xlsx', '12-yield-test.xlsx'),
    ('13-lista-precios-ingredientes.xlsx', '13-ingredient-price-list.xlsx'),
    ('BONUS-mermas-inventario.xlsx', 'BONUS-inventory-and-waste-control.xlsx'),
    ('BONUS-guia-food-cost-30-dias.pdf', 'BONUS-30-day-food-cost-guide.pdf'),
])
LIBROS_ES = [f for f in FICHEROS if f.endswith('.xlsx')]          # los 14 xlsx, en orden

# ==========================================================================
# 2. Pestañas (D9 + research §1.3). Un solo mapa global: no hay colisiones.
# ==========================================================================
HOJAS = OrderedDict([
    # comunes
    ('Instrucciones', 'Instructions'),
    ('Conversiones', 'Conversions'),
    ('Mermas', 'Trim Loss Factors'),                 # D9 / M21: no «Waste Factors»
    # 01
    ('Escandallo', 'Recipe Cost Card'),
    # 02
    ('1. Aperitivo', '1. Amuse-Bouche'),
    ('2. Entrante', '2. Starter'),
    ('3. Pescado', '3. Fish'),
    ('4. Carne', '4. Meat'),
    ('5. Postre', '5. Dessert'),
    ('6. Pase', '6. Course'),
    ('7. Pase', '7. Course'),
    ('8. Pase', '8. Course'),
    ('9. Pase', '9. Course'),
    ('Resumen', 'Summary'),
    # 03
    ('Primer Plato', 'Starter'),
    ('Segundo Plato', 'Main'),
    ('Postre', 'Dessert'),
    ('Resumen Menú', 'Menu Summary'),
    ('Rotación Semanal', 'Weekly Rotation'),
    # 04
    ('Formatos de Compra', 'Bottle Sizes'),
    ('Gin Tonic Premium', 'Gin & Tonic'),
    ('Mojito Clásico', 'Mojito'),
    ('Margarita', 'Margarita'),
    ('Aperol Spritz', 'Aperol Spritz'),
    # 05
    ('Tarta Chocolate', 'Chocolate Cake'),
    ('Croissants', 'Croissants'),
    ('Macarons', 'Macarons'),
    # 06
    ('Cocktail (por persona)', 'Reception (per guest)'),
    ('Presupuesto', 'Event Quote'),
    ('Checklist Evento', 'Event Checklist'),
    ('Presupuesto Cliente', 'Client Proposal'),
    # 07
    ('Tostada Aguacate', 'Avocado Toast'),
    ('Açaí Bowl', 'Açaí Bowl'),
    ('Eggs Benedict', 'Eggs Benedict'),
    ('Carrot Cake', 'Carrot Cake'),
    # 08
    ('Smash Burger', 'Smash Burger'),
    ('Loaded Fries', 'Loaded Fries'),
    ('Pulled Pork Sándwich', 'Pulled Pork Sandwich'),
    ('Punto de Equilibrio', 'Break-Even'),
    # 09
    ('Mermas Semanal', 'Weekly Waste Log'),
    ('Evolución', 'Trend'),
    # 10
    ('Calculadora PVP', 'Menu Price Calculator'),
    # 11
    ('Dashboard', 'Dashboard'),
    # 12 (D9 / R2T-07)
    ('Test de despiece', 'Butcher Yield Test'),
    ('Test de cocción', 'Cooking Loss Test'),
    # 13
    ('Lista de precios', 'Price List'),
    # BONUS
    ('Inventario', 'Inventory'),
    ('Ventas del periodo', 'Sales for the Period'),
    ('Checklist Mermas', 'Waste Checklist'),
])

# Pestañas de cada libro ES v2.1 publicado (medido el 24-sep sobre dl/kit-escandallos).
_ESC = ['Conversiones', 'Mermas']
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01-escandallo-estandar.xlsx', ['Instrucciones', 'Escandallo'] + _ESC),
    ('02-menu-degustacion.xlsx', ['Instrucciones', '1. Aperitivo', '2. Entrante', '3. Pescado',
                                  '4. Carne', '5. Postre', '6. Pase', '7. Pase', '8. Pase',
                                  '9. Pase', 'Resumen'] + _ESC),
    ('03-menu-del-dia.xlsx', ['Instrucciones', 'Primer Plato', 'Segundo Plato', 'Postre',
                              'Resumen Menú', 'Rotación Semanal'] + _ESC),
    ('04-cocktails-bebidas.xlsx', ['Instrucciones', 'Formatos de Compra', 'Gin Tonic Premium',
                                   'Mojito Clásico', 'Margarita', 'Aperol Spritz'] + _ESC),
    ('05-pasteleria.xlsx', ['Instrucciones', 'Tarta Chocolate', 'Croissants', 'Macarons'] + _ESC),
    ('06-catering.xlsx', ['Instrucciones', 'Cocktail (por persona)', 'Presupuesto',
                          'Checklist Evento', 'Presupuesto Cliente'] + _ESC),
    ('07-cafeteria-brunch.xlsx', ['Instrucciones', 'Tostada Aguacate', 'Açaí Bowl',
                                  'Eggs Benedict', 'Carrot Cake'] + _ESC),
    ('08-food-truck.xlsx', ['Instrucciones', 'Smash Burger', 'Loaded Fries',
                            'Pulled Pork Sándwich', 'Punto de Equilibrio'] + _ESC),
    ('09-control-mermas.xlsx', ['Instrucciones', 'Mermas Semanal', 'Evolución']),
    ('10-calculadora-pvp.xlsx', ['Instrucciones', 'Calculadora PVP']),
    ('11-dashboard-food-cost-mensual.xlsx', ['Instrucciones', 'Dashboard']),
    ('12-test-de-rendimiento.xlsx', ['Instrucciones', 'Test de despiece', 'Test de cocción']),
    ('13-lista-precios-ingredientes.xlsx', ['Instrucciones', 'Lista de precios']),
    ('BONUS-mermas-inventario.xlsx', ['Instrucciones', 'Inventario', 'Ventas del periodo',
                                      'Checklist Mermas']),
])

HOJA_PROHIBIDOS = set('[]:*?/\\')


def hoja_en(nombre_es):
    """Nombre EN de una pestaña ES (KeyError si no está en el mapa: nunca se adivina)."""
    return HOJAS[nombre_es]


def ref_hoja(nombre):
    """Forma de citar una hoja en una fórmula: entre comillas simples si hace falta."""
    if re.fullmatch(r'[A-Za-z_][A-Za-z0-9_.]*', nombre):
        return nombre
    return "'" + nombre.replace("'", "''") + "'"


# ==========================================================================
# 3. Claves-dato (§2.3)
# ==========================================================================
# 3.1 Categorías de merma (research §1.4), en el orden de la hoja «Mermas» (motor.MERMAS).
CATEGORIAS = OrderedDict([
    ('Carne roja', 'Beef & red meat'),
    ('Aves', 'Poultry'),
    ('Pescado', 'Fish'),
    ('Marisco', 'Shellfish'),
    ('Verdura hoja', 'Leafy greens'),
    ('Verdura raíz', 'Root vegetables'),
    ('Verdura fruto', 'Fruiting vegetables'),
    ('Fruta', 'Fruit'),
    ('Lácteos', 'Dairy'),
    ('Secos/granos', 'Dry goods & grains'),
    ('Congelados', 'Frozen'),
    ('Pan/bollería', 'Bread & pastry'),
    ('Huevos', 'Eggs'),
    ('Aceites/grasas', 'Oils & fats'),
    ('Especias/hierbas', 'Herbs & spices'),
    ('Chocolate/cacao', 'Chocolate & cocoa'),
    ('Bebidas/licores', 'Beverages & spirits'),
    ('Setas/hongos', 'Mushrooms'),
    ('Conservas/encurtidos', 'Canned & pickled'),
    ('Salsas/condimentos', 'Sauces & condiments'),
    ('Pasta/arroz', 'Pasta & rice'),
])

# 3.2 Unidades del desplegable ES → clave EN (§2.3). Las métricas no cambian.
UNIDADES = OrderedDict([
    ('kg', 'kg'), ('g', 'g'), ('L', 'L'), ('ml', 'ml'), ('cl', 'cl'),
    ('ud', 'each'), ('docena', 'dozen'), ('manojo', 'bunch'), ('sobre', 'packet'),
    ('lata', 'can'), ('botella', 'bottle'),
])

# 3.3 Motivos de la DV del BONUS «Checklist Mermas» (D:D).
MOTIVOS = OrderedDict([
    ('Caducidad', 'Expired'),
    ('Mal estado', 'Spoiled'),
    ('Sobreproducción', 'Overproduction'),
    ('Error de preparación', 'Prep error'),
    ('Almacenaje incorrecto', 'Improper storage'),
    ('Porcionado excesivo', 'Over-portioning'),
    ('Otro', 'Other'),
])

# 3.4 Tipos de componente del libro 12 (DV «Tipo» y literales de SUMIF) [R2T-17].
DV12 = OrderedDict([
    ('Útil', 'Usable'),
    ('Subproducto', 'By-product'),
    ('Desecho', 'Trim (no value)'),
])

# 3.5 DV del checklist de 06: no cambia («✓,—,N/A» sirven en inglés).
DV_CHECKLIST_06 = '✓,—,N/A'


def dv_lista(valores):
    """Fórmula de una DV de lista literal: '"a,b,c"'."""
    return '"' + ','.join(valores) + '"'


DV_MOTIVOS_EN = dv_lista(MOTIVOS.values())
DV12_EN = dv_lista(DV12.values())

# ==========================================================================
# 4. Literales de fórmula (§2.4)
# ==========================================================================
LITERALES = OrderedDict([
    ('revisa merma', 'check trim loss'),         # 01-08, col I (453)
    ('revisa unidades', 'check units'),          # 01-08, col J (453)
    ('ALERTA', 'ALERT'),                         # 09, 11, 13 + sus CF
    ('Útil', DV12['Útil']),                      # 12, SUMIF
    ('Subproducto', DV12['Subproducto']),
    ('Desecho', DV12['Desecho']),
])
LITERALES_SIN_CAMBIO = {'', 'OK', '?', '→', '✓', '?*', '>0'}

# ==========================================================================
# 5. Unidades EN (D7) y tabla `Conversions` (regla cerrada de D7)
# ==========================================================================
LISTA_UNIDADES_EN = ('lb,oz,kg,g,gal,qt,pt,imp pt,cup,fl oz,tbsp,tsp,L,ml,cl,each,dozen,'
                     'bunch,packet,can,bottle,15 dz case,30 dz case,50 lb bag,40 lb case,'
                     '36x1 lb case,16 kg sack,40x250 g case,4x1 gal case,12x750 ml case,'
                     '24x12 fl oz case,1/2 bbl keg,1/6 bbl keg,50 L keg')
UNIDADES_EN = LISTA_UNIDADES_EN.split(',')
DV_UNIDADES_EN = '"' + LISTA_UNIDADES_EN + '"'
MAX_LISTA_DV = 255

# Tamaños base exactos (NIST HB44 App. C).
LB_G = Fr('453.59237')
FLOZ_ML = Fr('29.5735295625')
IMP_GAL_ML = Fr('4546.09')
GAL_ML = 128 * FLOZ_ML

MASA = OrderedDict([('lb', LB_G), ('oz', LB_G / 16), ('kg', Fr(1000)), ('g', Fr(1))])   # en g
VOLUMEN = OrderedDict([                                                                 # en ml
    ('gal', GAL_ML), ('qt', 32 * FLOZ_ML), ('pt', 16 * FLOZ_ML), ('imp pt', Fr('568.26125')),
    ('cup', 8 * FLOZ_ML), ('fl oz', FLOZ_ML), ('tbsp', FLOZ_ML / 2), ('tsp', FLOZ_ML / 6),
    ('L', Fr(1000)), ('ml', Fr(1)), ('cl', Fr(10)),
])
RECUENTO = OrderedDict([('each', Fr(1)), ('dozen', Fr(12))])                           # en each
BASE = OrderedDict([('masa', MASA), ('volumen', VOLUMEN), ('recuento', RECUENTO)])
EXCLUIDOS_BEBIDA = ('cup', 'tbsp', 'tsp')      # nunca destino de barriles ni cajas de bebida

# Los 13 formatos de compra (8b-B §1.4 / §1.6). Solo ORIGEN.
#   (nombre, dimensión, tamaño en la unidad base de su dimensión, subunidades, ¿bebida?, fuente, qué es)
PACKS = [
    ('15 dz case', 'recuento', Fr(180), OrderedDict(), False,
     'American Egg Board; USDA AMS shell egg standard', 'half case of eggs'),
    ('30 dz case', 'recuento', Fr(360), OrderedDict(), False,
     'American Egg Board; USDA AMS shell egg standard', 'full case of eggs'),
    ('50 lb bag', 'masa', 50 * LB_G, OrderedDict(), False,
     'WebstaurantStore, ADM all-purpose flour 50 lb', 'e.g. flour, sugar'),
    ('40 lb case', 'masa', 40 * LB_G, OrderedDict(), False,
     "Koch Foods; Sam's Club (4 x 10 lb chicken breast)", 'e.g. chicken, 4 x 10 lb'),
    ('36x1 lb case', 'masa', 36 * LB_G, OrderedDict([('each', 36)]), False,
     'WebstaurantStore (butter, 6 brands)', '1 lb blocks, e.g. butter'),
    ('16 kg sack', 'masa', Fr(16000), OrderedDict(), False,
     'JJ Foodservice, Brakes, Costco UK (flour)', 'UK flour sack'),
    ('40x250 g case', 'masa', Fr(10000), OrderedDict([('each', 40)]), False,
     'JJ Foodservice (butter 40x250 g)', '250 g blocks, UK butter'),
    ('4x1 gal case', 'volumen', 4 * GAL_ML, OrderedDict([('each', 4)]), False,
     'GFS; Darlington Packing (milk 4 x 1 gal)', '1 gal jugs, e.g. milk'),
    ('12x750 ml case', 'volumen', Fr(9000), OrderedDict([('bottle', 12), ('each', 12)]), True,
     '27 CFR 5.203; American Craft Spirits Association', 'wine or spirits'),
    ('24x12 fl oz case', 'volumen', 288 * FLOZ_ML, OrderedDict([('can', 24), ('each', 24)]), True,
     'beer case equivalent (sbstandard.com)', 'beer or soda'),
    ('1/2 bbl keg', 'volumen', Fr(31, 2) * GAL_ML, OrderedDict(), True,
     '27 CFR 25.11 (1 barrel = 31 US gal)', 'US half barrel, 15.5 gal'),
    ('1/6 bbl keg', 'volumen', Fr(31, 6) * GAL_ML, OrderedDict(), True,
     '27 CFR 25.11 (1 barrel = 31 US gal)', 'US sixth barrel, 5.17 gal'),
    ('50 L keg', 'volumen', Fr(50000), OrderedDict(), True,
     'UK 50 L keg; 1 imp pt = 568.26125 ml (NIST HB44 App. C)', 'UK keg, 50 L ≈ 88 imp pt'),
]
PACKS_NOMBRES = [p[0] for p in PACKS]

# Envases genéricos: solo origen; destinos fl oz, ml, cl, L, each y sí mismos. Sus filas
# son fórmulas sobre UNA celda de tamaño (la fila «→ml»), que es lo único que edita el UK.
ENVASES = OrderedDict([
    ('bottle', {'ml': 750, 'nota_tam': 'bottle size in ml: 750 (US wine & spirits). UK spirits: '
                                      'type 700 here — edit only this cell'}),
    ('can', {'ml': 355, 'nota_tam': 'beverage can 12 fl oz = 355 ml (UK: 330). Edit only this cell. '
                                   'For #10 food cans buy in oz'}),
])
DESTINOS_ENVASE = ['ml', 'fl oz', 'cl', 'L', 'each']      # + identidad → 6 claves por envase

# Unidades sueltas: identidad y →each = 1, sin peso (8b-B §1.5).
SUELTAS = ['bunch', 'packet']

FILA0 = 5              # primera fila de datos de `Conversions` (cabecera en la fila 4, como el ES)
FILAS_LIBRES = 30      # filas vacías dentro del rango del VLOOKUP (R2T-15)
COL_EXPLICACION = 'C'


def _fmt(x):
    """Número para la columna C, en formato de EE. UU. (1,234.5678; sin ceros de cola)."""
    x = float(x)
    if abs(x - round(x)) < 1e-9:
        return '{:,}'.format(int(round(x)))
    if abs(x) >= 100:
        s = '{:,.2f}'.format(x)
    elif abs(x) >= 0.01:
        s = '{:,.4f}'.format(x)
    else:
        s = '{:,.6f}'.format(x)
    return s.rstrip('0').rstrip('.')


_PLURAL = {'bottle': 'bottles', 'can': 'cans'}


def dimension(u):
    """Dimensión física de una unidad EN (masa, volumen, recuento o 'suelta')."""
    for dim, tabla in BASE.items():
        if u in tabla:
            return dim
    for nombre, dim, *_ in PACKS:
        if u == nombre:
            return dim
    if u in ENVASES:
        return 'volumen'
    if u in SUELTAS:
        return 'suelta'
    raise KeyError(u)


_AVISOS_ID = {
    'oz': 'same unit (oz = weight; fl oz = volume)',
    'fl oz': 'same unit (fl oz = volume; oz = weight)',
    'pt': 'same unit (US pint = 16 fl oz; UK pint: use imp pt)',
    'imp pt': 'same unit (imperial pint = 568 ml; US pint = 473 ml)',
    'gal': 'same unit (US gallon = 128 fl oz; the UK gallon is 20% larger)',
    'cup': 'same unit (volume: pro kitchens weigh dry goods; weigh one cup once)',
}


def conversions(fila0=FILA0):
    """Tabla `Conversions` EN por la regla cerrada de D7.

    Devuelve una lista de dicts, una por fila, en el orden en que se escriben:
      fila, clave ('compra→uso'), origen, destino, regla (base|pack|envase|suelta),
      factor (float exacto), valor (float o '=fórmula'), tamano (True en la celda de tamaño
      del envase) y nota (texto EN de la columna C).
    """
    filas = []

    def add(o, d, factor, regla, nota, valor=None, tamano=False):
        filas.append({'clave': o + '→' + d, 'origen': o, 'destino': d, 'regla': regla,
                      'factor': float(factor), 'valor': float(factor) if valor is None else valor,
                      'tamano': tamano, 'nota': nota})

    # (1) base↔base de la misma dimensión, identidades incluidas (identidad primero).
    for dim, tabla in BASE.items():
        for o in tabla:
            for d in [o] + [u for u in tabla if u != o]:
                f = tabla[o] / tabla[d]
                if o == d:
                    nota = _AVISOS_ID.get(o, 'same unit')
                else:
                    nota = '1 {} = {} {}'.format(o, _fmt(f), d)
                add(o, d, f, 'base', nota)

    # (3) envases can/bottle: celda de tamaño (→ml) + fórmulas sobre ella.
    for env, info in ENVASES.items():
        add(env, env, 1, 'envase', 'same unit (bought and used as one {})'.format(env))
        add(env, 'ml', info['ml'], 'envase', info['nota_tam'], tamano=True)
        for d in DESTINOS_ENVASE:
            if d == 'ml':
                continue
            if d == 'each':
                add(env, d, 1, 'envase', 'one {} counted as one unit'.format(env))
            else:
                add(env, d, Fr(info['ml']) / VOLUMEN[d], 'envase', None)   # fórmula más abajo

    # (4) bunch / packet: identidad y →each = 1, sin peso.
    for s in SUELTAS:
        add(s, s, 1, 'suelta', 'same unit (bought and used as one {})'.format(s))
        add(s, 'each', 1, 'suelta', 'one {} counted as one unit (no default weight)'.format(s))

    # (2) packs: solo origen; identidad, subunidades y destinos base de su dimensión.
    for nombre, dim, tam, subs, bebida, _fuente, que in PACKS:
        add(nombre, nombre, 1, 'pack',
            'same unit: type the {} price as invoiced ({})'.format(nombre, que))
        for sub, cuantos in subs.items():
            add(nombre, sub, cuantos, 'pack',
                '1 × {} = {} {} ({})'.format(nombre, cuantos, _PLURAL.get(sub, sub), que))
        for d, tam_d in BASE[dim].items():
            if bebida and d in EXCLUIDOS_BEBIDA:
                continue
            if d in subs:
                continue
            f = tam / tam_d
            add(nombre, d, f, 'pack', '1 × {} = {} {}'.format(nombre, _fmt(f), d))

    # Filas y fórmulas de envase (necesitan saber la fila de la celda de tamaño).
    for i, r in enumerate(filas):
        r['fila'] = fila0 + i
    fila_tam = {r['origen']: r['fila'] for r in filas if r['tamano']}
    for r in filas:
        if r['regla'] == 'envase' and not r['tamano'] and r['destino'] in VOLUMEN \
                and r['destino'] != 'ml':
            div = VOLUMEN[r['destino']]           # ml por unidad de destino
            rt = fila_tam[r['origen']]
            # Celda de tamaño vacía, a 0 o con texto → «?» (la ficha dice «check units»), nunca 0.
            if div == 1:
                r['valor'] = '=IF(AND(ISNUMBER(B{0}),B{0}>0),B{0},"?")'.format(rt)
            else:
                r['valor'] = '=IF(AND(ISNUMBER(B{0}),B{0}>0),B{0}/{1},"?")'.format(rt, _num_formula(div))
            r['nota'] = 'from the {} size in ml (row {})'.format(r['origen'], rt)
    return filas


def _num_formula(x):
    """Constante numérica exacta para una fórmula (sin notación científica)."""
    s = '{:.10f}'.format(float(x)).rstrip('0').rstrip('.')
    assert abs(float(s) - float(x)) < 1e-9, x
    return s


def n_claves():
    return len(conversions())


def ultima_fila_rango(n=None):
    n = n_claves() if n is None else n
    return FILA0 - 1 + n + FILAS_LIBRES


def rango_vlookup(n=None):
    """Rango del VLOOKUP de las 453 fórmulas G de 01-08 (E2): $A$5:$B${4+n+30}."""
    return '$A${}:$B${}'.format(FILA0, ultima_fila_rango(n))


def area_impresion(n=None):
    """Área de impresión de `Conversions` (E2): mismas filas que el rango, columnas A:J como el ES."""
    return '$A$1:$J${}'.format(ultima_fila_rango(n))


def evaluar_valor(fila, filas):
    """Evalúa el valor de una fila (número o las fórmulas simples que genera conversions())."""
    v = fila['valor']
    if not isinstance(v, str):
        return float(v)
    por_fila = {r['fila']: r for r in filas}
    m = re.fullmatch(r'=IF\(AND\(ISNUMBER\(B(\d+)\),B\1>0\),B\1,"\?"\)', v)
    if m:
        return float(por_fila[int(m.group(1))]['valor'])
    m = re.fullmatch(r'=IF\(AND\(ISNUMBER\(B(\d+)\),B\1>0\),B\1/([0-9.]+),"\?"\)', v)
    if m:
        return float(por_fila[int(m.group(1))]['valor']) / float(m.group(2))
    raise ValueError('fórmula no reconocida: ' + v)


# ==========================================================================
# 6. Autotest
# ==========================================================================
def _check(cond, msg, fallos):
    if not cond:
        fallos.append(msg)


def autotest(censo_path=None, verbose=False):
    """Comprueba mapas y tabla. Lanza AssertionError con la lista de fallos si hay alguno."""
    fallos = []
    res = OrderedDict()

    # --- lista D7
    _check(len(UNIDADES_EN) == 34, 'D7: la lista debe tener 34 unidades (tiene {})'.format(len(UNIDADES_EN)), fallos)
    _check(len(set(UNIDADES_EN)) == len(UNIDADES_EN), 'D7: unidades repetidas en la lista', fallos)
    _check(len({u.lower() for u in UNIDADES_EN}) == len(UNIDADES_EN),
           'D7: dos unidades iguales salvo mayúsculas (VLOOKUP no distingue)', fallos)
    _check(len(LISTA_UNIDADES_EN) <= MAX_LISTA_DV,
           'D7: lista de {} caracteres > {}'.format(len(LISTA_UNIDADES_EN), MAX_LISTA_DV), fallos)
    _check('case' not in UNIDADES_EN, 'D7: no puede haber «case» genérico', fallos)
    _check(all(',' not in u and '"' not in u for u in UNIDADES_EN), 'D7: unidad con coma o comillas', fallos)
    res['lista_unidades'] = {'n': len(UNIDADES_EN), 'caracteres': len(LISTA_UNIDADES_EN),
                             'caracteres_con_comillas': len(DV_UNIDADES_EN)}
    for u in UNIDADES_EN:
        try:
            dimension(u)
        except KeyError:
            fallos.append('D7: unidad sin dimensión: ' + u)
    _check(set(PACKS_NOMBRES) <= set(UNIDADES_EN), 'D7: pack fuera de la lista', fallos)
    _check(len(PACKS) == 13, 'D7: deben ser 13 formatos de compra', fallos)
    _check(set(UNIDADES.values()) <= set(UNIDADES_EN), '§2.3: unidad ES sin destino EN en la lista', fallos)

    # --- hojas
    for es, en in HOJAS.items():
        _check(len(en) <= 31, 'D9: «{}» > 31 caracteres'.format(en), fallos)
        _check(not (set(en) & HOJA_PROHIBIDOS), 'D9: «{}» con carácter prohibido'.format(en), fallos)
        _check("'" not in en and '’' not in en, 'D9: «{}» con apóstrofo (R2T-07)'.format(en), fallos)
        _check(en.strip() == en and en, 'D9: «{}» con espacios en los bordes'.format(en), fallos)
    for libro, hojas in HOJAS_ES_POR_LIBRO.items():
        for h in hojas:
            _check(h in HOJAS, 'D9: pestaña sin mapa: {} / {}'.format(libro, h), fallos)
        ens = [HOJAS.get(h, '?') for h in hojas]
        _check(len({e.lower() for e in ens}) == len(ens),
               'D9: nombres EN repetidos en {}: {}'.format(libro, ens), fallos)
    _check(HOJAS['Mermas'] == 'Trim Loss Factors', 'D9: «Mermas» → «Trim Loss Factors»', fallos)
    _check(set(HOJAS_ES_POR_LIBRO) == set(LIBROS_ES), 'ficheros: HOJAS_ES_POR_LIBRO ≠ LIBROS_ES', fallos)
    res['hojas'] = {'es_distintas': len(HOJAS), 'libros': len(HOJAS_ES_POR_LIBRO),
                    'pestanas_total': sum(len(h) for h in HOJAS_ES_POR_LIBRO.values())}

    # --- claves-dato y literales
    _check(len(CATEGORIAS) == 21 and len(set(CATEGORIAS.values())) == 21, '§2.3: 21 categorías únicas', fallos)
    _check(len(set(MOTIVOS.values())) == 7, '§2.3: 7 motivos únicos', fallos)
    _check(len(DV_MOTIVOS_EN) - 2 <= MAX_LISTA_DV, 'DV motivos > 255', fallos)
    _check(len(set(DV12.values())) == 3 and all(',' not in v for v in DV12.values()), 'DV12', fallos)
    _check(not (set(LITERALES.values()) & LITERALES_SIN_CAMBIO), 'literal EN choca con uno sin cambio', fallos)
    _check(not (set(LITERALES) & LITERALES_SIN_CAMBIO), 'literal ES a la vez traducido y sin cambio', fallos)
    for es, en in LITERALES.items():
        _check('"' not in en, 'literal EN con comillas: ' + en, fallos)
    cats_en = ','.join(CATEGORIAS.values())
    res['categorias_inline_caracteres'] = len(cats_en)   # > 255: por eso la DV lee la hoja

    # --- Conversions
    filas = conversions()
    n = len(filas)
    res['n'] = n
    claves = [r['clave'] for r in filas]
    _check(len(set(k.lower() for k in claves)) == n, 'gate 1: claves duplicadas (sin distinguir mayúsculas)', fallos)
    por_regla = OrderedDict()
    for r in filas:
        por_regla[r['regla']] = por_regla.get(r['regla'], 0) + 1
        o, d = r['origen'], r['destino']
        _check(o in UNIDADES_EN and d in UNIDADES_EN, 'gate 2: unidad fuera de la lista en ' + r['clave'], fallos)
        try:
            dims = {dimension(o), dimension(d)}
        except KeyError as e:
            fallos.append('D7: unidad sin dimensión en {}: {}'.format(r['clave'], e))
            dims = set()
        _check(dims != {'masa', 'volumen'}, 'D7: peso↔volumen en ' + r['clave'], fallos)
        if d in PACKS_NOMBRES:
            _check(o == d, 'gate 3: pack como destino en ' + r['clave'], fallos)
        if d in ENVASES:
            _check(o == d or o in PACKS_NOMBRES, 'envase como destino en ' + r['clave'], fallos)
        if o in PACKS_NOMBRES and dict((p[0], p[4]) for p in PACKS)[o]:
            _check(d not in EXCLUIDOS_BEBIDA, 'D7: cup/tbsp/tsp como destino de bebida en ' + r['clave'], fallos)
        if o in ENVASES:
            _check(d in DESTINOS_ENVASE + [o], 'D7: destino no permitido para envase en ' + r['clave'], fallos)
            _check(d not in ('cup', 'tbsp', 'tsp', 'qt', 'gal', 'pt'), 'D7: can/bottle a medida de cocina', fallos)
        _check(r['factor'] > 0, 'factor ≤ 0 en ' + r['clave'], fallos)
        _check(isinstance(r['nota'], str) and r['nota'], 'columna C vacía en ' + r['clave'], fallos)
        try:
            v = evaluar_valor(r, filas)
            _check(abs(v - r['factor']) <= 1e-9 * max(1, abs(r['factor'])),
                   'valor ≠ factor en {} ({} vs {})'.format(r['clave'], v, r['factor']), fallos)
        except ValueError as e:
            fallos.append(str(e))
    res['por_regla'] = por_regla

    ks = set(claves)
    # (1) base↔base completo
    for dim, tabla in BASE.items():
        for o in tabla:
            for d in tabla:
                _check(o + '→' + d in ks, 'gate 3: falta base↔base ' + o + '→' + d, fallos)
    # (2) packs
    for nombre, dim, tam, subs, bebida, *_ in PACKS:
        _check(nombre + '→' + nombre in ks, 'gate 3: falta identidad ' + nombre, fallos)
        for s in subs:
            _check(nombre + '→' + s in ks, 'gate 3: falta subunidad ' + nombre + '→' + s, fallos)
        for d in BASE[dim]:
            esperado = not (bebida and d in EXCLUIDOS_BEBIDA)
            _check((nombre + '→' + d in ks) == esperado, 'gate 3: destino base {}→{}'.format(nombre, d), fallos)
        suyas = [r for r in filas if r['origen'] == nombre]
        _check(len(suyas) == 1 + len(subs) + len([d for d in BASE[dim]
                                                  if d not in subs and not (bebida and d in EXCLUIDOS_BEBIDA)]),
               'gate 3: {} tiene claves de más'.format(nombre), fallos)
    # (3) envases: 6 destinos, fórmulas sobre UNA celda de tamaño (gate 4)
    for env in ENVASES:
        suyas = [r for r in filas if r['origen'] == env]
        _check(len(suyas) == 6, 'gate 3: {} debe tener 6 claves (tiene {})'.format(env, len(suyas)), fallos)
        tam = [r for r in suyas if r['tamano']]
        _check(len(tam) == 1 and tam[0]['destino'] == 'ml' and not isinstance(tam[0]['valor'], str),
               'gate 4: {} sin una única celda de tamaño numérica en →ml'.format(env), fallos)
        if tam:
            rt = tam[0]['fila']
            for r in suyas:
                if r['destino'] in ('fl oz', 'cl', 'L'):
                    _check(isinstance(r['valor'], str) and re.search(r'\bB{}\b'.format(rt), r['valor']),
                           'gate 4: {} no sale de la celda de tamaño B{}'.format(r['clave'], rt), fallos)
    # (4) sueltas
    for s in SUELTAS:
        suyas = sorted(r['destino'] for r in filas if r['origen'] == s)
        _check(suyas == sorted([s, 'each']), 'D7: {} debe tener solo identidad y →each'.format(s), fallos)
    # toda unidad de la lista es origen con identidad
    for u in UNIDADES_EN:
        _check(u + '→' + u in ks, 'D7: {} sin identidad'.format(u), fallos)

    # Factores de control (definiciones y 8b-B §1.6)
    esperados = {
        'lb→oz': 16, 'gal→fl oz': 128, 'L→fl oz': 33.8140227, 'kg→lb': 2.20462262,
        'oz→g': 28.349523125, 'cup→ml': 236.5882365, 'tbsp→tsp': 3, 'dozen→each': 12,
        '50 lb bag→oz': 800, '40 lb case→oz': 640, '15 dz case→each': 180, '30 dz case→dozen': 30,
        '4x1 gal case→fl oz': 512, '12x750 ml case→fl oz': 304.326, '1/2 bbl keg→fl oz': 1984,
        '1/6 bbl keg→fl oz': 661.333, 'bottle→fl oz': 25.3605, 'gal→L': 3.78541,
        'imp pt→ml': 568.261, '50 L keg→imp pt': 87.9877, '50 L keg→L': 50, 'can→fl oz': 12.004, '16 kg sack→g': 16000,
        '36x1 lb case→each': 36, '12x750 ml case→bottle': 12, '24x12 fl oz case→can': 24,
    }
    fac = {r['clave']: r['factor'] for r in filas}
    for k, v in esperados.items():
        _check(k in fac and abs(fac[k] - v) <= 5e-4 * max(1, v),
               'factor de control {} = {} (esperado ≈ {})'.format(k, fac.get(k), v), fallos)

    # Rango E2
    _check(rango_vlookup(n) == '$A$5:$B${}'.format(4 + n + 30), 'E2: rango', fallos)
    res['rango_vlookup'] = rango_vlookup(n)
    res['area_impresion'] = area_impresion(n)
    res['ultima_fila_tabla'] = FILA0 - 1 + n

    # --- cruce con el censo del ES v2.1 (si existe)
    censo_path = censo_path or os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(censo_path):
        with open(censo_path, encoding='utf-8') as fh:
            censo = json.load(fh)
        libros = censo['libros']
        _check(set(libros) == set(LIBROS_ES), 'censo: libros distintos de LIBROS_ES', fallos)
        for libro, info in libros.items():
            _check(info['hojas'] == HOJAS_ES_POR_LIBRO.get(libro),
                   'censo: pestañas de {} ≠ HOJAS_ES_POR_LIBRO'.format(libro), fallos)
            for h, hd in info['hojas_detalle'].items():
                for lit in hd.get('literales', {}):
                    _check(lit in LITERALES or lit in LITERALES_SIN_CAMBIO,
                           'censo: literal de fórmula sin mapa: {!r} ({} / {})'.format(lit, libro, h), fallos)
                for lit in hd.get('literales_cf', {}):
                    _check(lit in LITERALES or lit in LITERALES_SIN_CAMBIO,
                           'censo: literal de CF sin mapa: {!r} ({} / {})'.format(lit, libro, h), fallos)
                for dv in hd.get('dv', []):
                    f1 = dv.get('formula1') or ''
                    if f1.startswith('"'):
                        items = f1.strip('"').split(',')
                        ok = (set(items) <= set(UNIDADES) or set(items) <= set(MOTIVOS)
                              or set(items) <= set(DV12) or f1.strip('"') == DV_CHECKLIST_06)
                        _check(ok, 'censo: DV literal sin mapa en {} / {}: {}'.format(libro, h, f1), fallos)
                        if set(items) <= set(UNIDADES):
                            _check(items == list(UNIDADES), 'censo: DV de unidades ES distinta de la esperada', fallos)
                    else:
                        for ref in re.findall(r"(?:'((?:[^']|'')+)'|([^\W\d][\w.]*))!", f1):
                            nom = (ref[0] or ref[1]).replace("''", "'")
                            _check(nom in HOJAS, 'censo: DV cita hoja sin mapa: ' + nom, fallos)
                for nom in hd.get('refs_hoja', {}):
                    _check(nom in HOJAS, 'censo: fórmula cita hoja sin mapa: {} ({})'.format(nom, libro), fallos)
            cats = info.get('categorias_mermas')
            if cats:
                _check(cats == list(CATEGORIAS), 'censo: categorías de Mermas ≠ CATEGORIAS en ' + libro, fallos)
        res['censo_cruzado'] = True
    else:
        res['censo_cruzado'] = False

    res['fallos'] = fallos
    if verbose:
        print(json.dumps(res, ensure_ascii=False, indent=1))
    if fallos:
        raise AssertionError('mapas.py autotest: {} fallos\n  - '.format(len(fallos)) + '\n  - '.join(fallos))
    return res


if __name__ == '__main__':
    import sys
    r = autotest()
    print('mapas.py autotest OK')
    print('  n (claves Conversions) = {}  · por regla {}'.format(r['n'], dict(r['por_regla'])))
    print('  rango VLOOKUP = {}  · área de impresión = {}'.format(r['rango_vlookup'], r['area_impresion']))
    print('  lista D7: {} unidades, {} caracteres (≤ {})'.format(
        r['lista_unidades']['n'], r['lista_unidades']['caracteres'], MAX_LISTA_DV))
    print('  hojas: {} nombres ES en el mapa, {} pestañas en {} libros'.format(
        r['hojas']['es_distintas'], r['hojas']['pestanas_total'], r['hojas']['libros']))
    print('  censo_es.json cruzado: {}'.format(r['censo_cruzado']))
    if '--json' in sys.argv:
        print(json.dumps(conversions(), ensure_ascii=False, indent=1))
