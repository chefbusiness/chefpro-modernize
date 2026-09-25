#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""generar_mercado.py — escribe mercado_en.json (Restaurant Inventory Kit Pro, F2-EN, SPEC §7 paso 3).

SPEC que manda: SPEC.md (D8, D9, D11-D15, D18, D20, D24, D25; §4, §5.1, §5.2). Sesión Claude Code, 25-sep-2026.
Modelo: recipe-costing-kit/generar_mercado.py (piloto LIVE).

Qué reúne
  · productos: la tabla maestra de §5.1 (50 + la merluza→cod de 04-06), UN registro por producto con nombre EN,
    categoría D8, unidad US D9, precio (sin símbolo, D13), par level / par max y su fuente. Los 9 libros leen de aquí.
  · b09: consumo diario, lead time, cobertura y vida útil de las 8 filas del BONUS-09, calibradas para que
    consumo × (lead + cobertura) = par level del 01 y stock máximo = par max (D14).
  · proveedores: las 6 fichas «(sample)» de §5.2 (D15).
  · familias_recepcion: NO se duplica; vive en mapas.FAMILIAS (15 filas, °F, §4) y mapas.FAMILIA_POR_CATEGORIA.
  · libros: los datos de ejemplo por celda (hoja ES y EN) que aplicar_en.py escribe tal cual. Mandan sobre la
    sustitución por cadena de «localizar» cuando una celda cambia de producto o de proveedor (04!B7, D7, G7, H7).
  · fechas_hoy: las 19 celdas de D25 como =TODAY()+k.
  · localizar: las 246 cadenas GL-mercado de textos_es.json con su EN.
  · textos_cifra_derivada: las celdas de D20 reescritas con la cifra EN recalculada (calc = la cuenta).
Todas las cifras derivadas se CALCULAN aquí desde los valores EN; nada copiado a mano ni € convertido.

Uso:  python3 generar_mercado.py            (escribe mercado_en.json y un resumen)
      python3 generar_mercado.py --stdout   (solo imprime el resumen)
"""
from __future__ import print_function

import datetime as dt
import json
import math
import os
import sys
from collections import OrderedDict
from decimal import Decimal, ROUND_HALF_UP

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import mapas  # noqa: E402

FECHA = '2026-09-25'
SALIDA = os.path.join(AQUI, 'mercado_en.json')
PILOTO = json.load(open(os.path.join(AQUI, '..', 'recipe-costing-kit', 'mercado_en.json'), encoding='utf-8'))
CAT_PIL = PILOTO['catalogo']
TEXTOS = json.load(open(os.path.join(AQUI, 'textos_es.json'), encoding='utf-8'))
CAT = mapas.CATEGORIAS
CAT_INV = {v: k for k, v in CAT.items()}
H = mapas.HOJAS

# D24: parámetros del BONUS-09 heredados del ES
COSTE_PEDIDO, ALMACEN, FACTOR_VIDA = 3, 0.25, 0.7
# D25: día de referencia de los ejemplos ES. La SPEC dice 23-ago, pero con 23-ago la merluza (caducidad 23-ago)
# queda en 0 días = «URGENT» y el 06 enseña 4 estados, no 5 (G6 fallaría). Con 24-ago salen los cinco, que es lo que
# promete 06!Instrucciones!A21 y lo que pide la acción de la fila («Retirar»). Ver «decisiones».
REF_ES = dt.date(2026, 8, 24)


def xround(x, n=0):
    """ROUND de Excel (mitad hacia arriba, no bancario)."""
    q = Decimal(1).scaleb(-n)
    return float(Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP))


def r2(x):
    return xround(x, 2)


def money(x):
    return '{:,.2f}'.format(x)


def fuente_piloto(pid):
    return CAT_PIL[pid]['fuente']


# ============================================================================ 1. Tabla maestra (§5.1, D14)
# (id, ES exacto, EN, categoría EN, unidad US, par, par max, libro01 hoja ES, precio-regla)
# precio-regla: ('pil', id)                → mismo precio y unidad que el catálogo del piloto
#               ('der', id, factor, razón) → precio del piloto × factor (cambio de formato), [derivado]
#               ('est', precio, razón)     → [estimado] con el razonamiento
E = 'est'
MAESTRA = [
    # ---- 01 Cocina → Kitchen (filas 5-24)
    ('chicken_breast', 'Pechuga de pollo', 'Boneless chicken breast', 'Meat & Poultry', 'lb', 18, 40, 'Cocina',
     (E, 3.10, 'Pechuga deshuesada sin piel en caja de 40 lb de distribuidor: rango habitual 2.60-3.50 $/lb en 2026, '
               'por debajo del precio minorista; se toma el centro. Sin listado verificado en el catálogo del piloto.')),
    ('beef_tenderloin', 'Solomillo de ternera', 'Beef tenderloin (PSMO)', 'Meat & Poultry', 'lb', 6, 18, 'Cocina',
     ('pil', 'beef_tenderloin')),
    ('salmon_fillet', 'Salmón fresco', 'Fresh salmon fillet', 'Seafood', 'lb', 8, 20, 'Cocina',
     (E, 9.95, 'Filete de salmón atlántico de acuicultura, cara entera, precio de distribuidor 9-11 $/lb; centro del '
               'rango. El piloto solo tiene salmón ahumado (28.22 $/lb), que no es el mismo producto.')),
    ('shrimp', 'Gambas', 'Shrimp 16/20', 'Seafood', 'lb', 6, 16, 'Cocina', ('pil', 'shrimp')),
    ('tomato', 'Tomate', 'Tomatoes', 'Produce', 'lb', 25, 50, 'Cocina', ('pil', 'tomato')),
    ('yellow_onion', 'Cebolla', 'Yellow onions', 'Produce', 'lb', 20, 50, 'Cocina', ('pil', 'yellow_onion')),
    ('romaine', 'Lechuga', 'Romaine lettuce', 'Produce', 'each', 12, 24, 'Cocina',
     (E, 1.60, 'Caja de 24 cabezas de romana de distribuidor a 35-45 $ → 1.45-1.90 $/cabeza; centro bajo del rango.')),
    ('potato', 'Patata', 'Russet potatoes', 'Produce', 'lb', 50, 150, 'Cocina',
     ('der', 'potato', 1 / 50.0, 'Saco de 50 lb del piloto (36.48 $) ÷ 50 = precio por lb.')),
    ('evoo', 'Aceite de oliva virgen extra', 'Extra virgin olive oil', 'Dry Goods', 'gal', 3, 8, 'Cocina',
     ('der', 'evoo', 3.785411784, 'Precio por L del piloto (4 x 3 L, 102.99 $) × 3.785411784 L/gal.')),
    ('kosher_salt', 'Sal marina', 'Kosher salt', 'Dry Goods', 'lb', 6, 18, 'Cocina', ('pil', 'kosher_salt')),
    ('black_pepper', 'Pimienta negra molida', 'Ground black pepper', 'Dry Goods', 'lb', 2, 5, 'Cocina',
     ('der', 'black_pepper', 1.0, 'Precio por lb de la pimienta en grano del piloto (bolsa de 5 lb); la molida de '
                                  'distribuidor está en el mismo rango.')),
    ('arborio', 'Arroz redondo', 'Arborio rice', 'Dry Goods', 'lb', 20, 50, 'Cocina',
     (E, 2.10, 'Arroz arborio de distribuidor en saco de 25 lb, 1.80-2.50 $/lb; centro del rango. «Arroz redondo» '
               'español → arborio, el grano redondo que se encuentra en EE. UU.')),
    ('dry_pasta', 'Pasta seca', 'Dry pasta', 'Dry Goods', 'lb', 20, 40, 'Cocina',
     (E, 1.35, 'Pasta seca de sémola en caja de 20 lb, 25-30 $ la caja → 1.25-1.50 $/lb.')),
    ('ap_flour', 'Harina de trigo', 'All-purpose flour', 'Dry Goods', 'lb', 25, 50, 'Cocina',
     ('der', 'ap_flour', 1 / 50.0, 'Saco de 50 lb del piloto (29.99 $) ÷ 50.')),
    ('eggs', 'Huevos M', 'Large eggs', 'Dairy & Eggs', 'dozen', 15, 30, 'Cocina',
     ('der', 'eggs', 1 / 15.0, 'Caja de 15 docenas del piloto (34.08 $, BLS) ÷ 15. D8: los huevos pasan de «Otros» a '
                               '«Dairy & Eggs».')),
    ('heavy_cream', 'Nata 35 % M.G.', 'Heavy cream', 'Dairy & Eggs', 'qt', 6, 16, 'Cocina', ('pil', 'heavy_cream')),
    ('butter', 'Mantequilla', 'Unsalted butter', 'Dairy & Eggs', 'lb', 6, 18, 'Cocina',
     ('der', 'butter', 1 / 36.0, 'Caja de 36 x 1 lb del piloto (116.42 $) ÷ 36.')),
    ('parmesan', 'Queso parmesano', 'Parmesan', 'Dairy & Eggs', 'lb', 4, 10, 'Cocina',
     (E, 9.50, 'Parmesano nacional (EE. UU.) en cuñas de 5 lb, 8-12 $/lb de distribuidor; el Parmigiano Reggiano '
               'DOP cuesta el doble. Centro del rango nacional.')),
    ('lemon', 'Limón', 'Lemons', 'Produce', 'each', 36, 90, 'Cocina', ('pil', 'lemon')),
    ('garlic', 'Ajo', 'Peeled garlic', 'Produce', 'lb', 5, 15, 'Cocina', ('pil', 'garlic')),
    # ---- 01 Barra → Bar (filas 5-19)
    ('coffee', 'Café en grano', 'Whole bean coffee', 'Dry Goods', 'lb', 12, 30, 'Barra',
     ('der', 'coffee', 1.0, 'Precio por lb del café del piloto (5 x 2 lb, 78.99 $); el de grano entero del mismo '
                            'surtido cuesta igual.')),
    ('whole_milk', 'Leche entera', 'Whole milk', 'Dairy & Eggs', 'gal', 6, 16, 'Barra', ('pil', 'whole_milk')),
    ('oat_milk', 'Bebida de avena', 'Oat milk (barista)', 'Non-Alcoholic Beverages', 'qt', 6, 18, 'Barra',
     ('pil', 'oat_milk')),
    ('orange_juice', 'Zumo de naranja', 'Orange juice', 'Non-Alcoholic Beverages', 'gal', 2, 5, 'Barra',
     (E, 7.50, 'Zumo de naranja refrigerado no de concentrado, caja 4 x 1 gal a 28-32 $ → 7-8 $/gal.')),
    ('cola', 'Refresco de cola', 'Cola (12 fl oz)', 'Non-Alcoholic Beverages', 'can', 48, 120, 'Barra',
     (E, 0.50, 'Caja de 24 latas de 12 fl oz a 11-13 $ en cash & carry → 0.46-0.54 $/lata.')),
    ('draft_beer', 'Cerveza de grifo (barril 30 L)', 'Draft beer (1/2 bbl)', 'Alcoholic Beverages', 'keg', 2, 6,
     'Barra', (E, 165.00, 'Barril de 1/2 bbl (15.5 gal): 120-140 $ una doméstica y 180-250 $ una craft al por mayor; '
                           'se toma un punto medio. Precio sin depósito del barril.')),
    ('water', 'Agua mineral', 'Bottled water', 'Non-Alcoholic Beverages', 'bottle', 48, 144, 'Barra',
     (E, 0.30, 'Pack de 24 botellas de 16.9 fl oz a 6-8 $ → 0.25-0.33 $/botella.')),
    ('tonic', 'Tónica', 'Premium tonic water', 'Non-Alcoholic Beverages', 'bottle', 24, 72, 'Barra',
     ('der', 'tonic', 1.0, 'Precio por unidad del piloto (24 x 6.7 fl oz, 40.99 $); «each» del piloto = «bottle» '
                           'en la lista D9, la misma botella.')),
    ('red_wine', 'Vino tinto (botella 75 cl)', 'House red wine (750 ml)', 'Alcoholic Beverages', 'bottle', 12, 36,
     'Barra', ('der', 'red_wine', 0.75, 'Precio por L del piloto (BLS APU0000720311) × 0.75 L por botella.')),
    ('white_wine', 'Vino blanco (botella 75 cl)', 'House white wine (750 ml)', 'Alcoholic Beverages', 'bottle', 12, 36,
     'Barra', ('der', 'white_wine', 0.75, 'Precio por L del piloto (BLS APU0000720311) × 0.75 L por botella.')),
    ('ice', 'Hielo en cubitos', 'Bagged ice (20 lb)', 'Frozen', 'bag', 6, 15, 'Barra',
     ('der', 'ice', 20.0, 'Precio por lb del piloto ([estimado] 0.20 $/lb) × 20 lb por bolsa.')),
    ('sugar', 'Azúcar blanquilla', 'Granulated sugar', 'Dry Goods', 'lb', 20, 50, 'Barra',
     ('der', 'sugar', 1 / 50.0, 'Saco de 50 lb del piloto (50.49 $) ÷ 50.')),
    ('bev_napkins_bar', 'Servilletas de papel (barra)', 'Beverage napkins (bar)', 'Paper & Cleaning', 'case', 2, 4,
     'Barra', (E, 28.00, 'Caja de 4,000 servilletas de cóctel de 1 capa a 25-32 $ en distribuidores de desechables.')),
    ('paper_straws', 'Pajitas de papel', 'Paper straws', 'Paper & Cleaning', 'case', 1, 2, 'Barra',
     (E, 36.00, 'Caja de 2,500-3,000 pajitas de papel envueltas a 30-45 $.')),
    ('disposable_cups', 'Vasos desechables', 'Disposable cups', 'Paper & Cleaning', 'pack', 6, 18, 'Barra',
     (E, 6.50, 'Funda de 50 vasos de plástico de 16 oz a 5-8 $.')),
    # ---- 01 Almacén → Storeroom (filas 5-19)
    ('paper_towels', 'Papel de cocina', 'Paper towels', 'Paper & Cleaning', 'roll', 12, 30, 'Almacén',
     (E, 2.40, 'Caja de 12-30 rollos de papel de cocina a 2-3 $ el rollo.')),
    ('plastic_wrap', 'Film transparente', 'Plastic wrap', 'Paper & Cleaning', 'roll', 2, 4, 'Almacén',
     (E, 24.00, 'Rollo de film de 18 in x 2,000 ft con cortador a 20-28 $; dura mucho más que el rollo español de '
                'referencia, por eso bajan los par levels.')),
    ('aluminum_foil', 'Papel de aluminio', 'Aluminum foil', 'Paper & Cleaning', 'roll', 2, 4, 'Almacén',
     (E, 34.00, 'Rollo de aluminio estándar de 18 in x 500 ft a 30-40 $.')),
    ('trash_bags', 'Bolsas de basura', 'Trash bags', 'Paper & Cleaning', 'pack', 6, 15, 'Almacén',
     (E, 18.00, 'Paquete de 50 bolsas de 55-60 gal de alta resistencia a 15-22 $.')),
    ('nitrile_gloves', 'Guantes de nitrilo', 'Nitrile gloves', 'Paper & Cleaning', 'case', 1, 2, 'Almacén',
     (E, 62.00, 'Caja de 1,000 guantes (10 cajitas de 100) a 50-75 $. El ES contaba cajitas de 100 (par 8), la '
                'unidad US es la caja de 1,000: par 1, máx. 2.')),
    ('dish_detergent', 'Detergente de lavavajillas', 'Dish machine detergent', 'Paper & Cleaning', 'gal', 5, 10,
     'Almacén', (E, 16.00, 'Detergente para lavavajillas industrial en garrafa de 5 gal a 70-90 $ → 14-18 $/gal.')),
    ('degreaser', 'Desengrasante de cocina', 'Kitchen degreaser', 'Paper & Cleaning', 'gal', 2, 4, 'Almacén',
     (E, 12.00, 'Desengrasante concentrado en garrafa de 1 gal a 10-15 $.')),
    ('sanitizer', 'Lejía alimentaria', 'Sanitizer (quat)', 'Paper & Cleaning', 'gal', 2, 4, 'Almacén',
     (E, 18.00, 'Desinfectante de amonio cuaternario concentrado, 1 gal a 15-22 $. En EE. UU. la desinfección de '
                'superficies en contacto con alimentos se hace con quat o con cloro; se elige quat.')),
    ('hotel_pans', 'Cubetas GN 1/1', 'Full-size hotel pans', 'Other', 'each', 6, 15, 'Almacén',
     (E, 18.00, 'Bandeja de acero inoxidable full-size de 2.5 in de fondo a 14-24 $.')),
    ('day_dots', 'Etiquetas FIFO', 'Day dot date labels', 'Other', 'roll', 3, 8, 'Almacén',
     (E, 7.50, 'Rollo de 1,000 etiquetas day dot de 3/4 in a 6-9 $.')),
    ('receipt_rolls', 'Rollos de ticket', 'POS receipt paper rolls', 'Other', 'pack', 5, 12, 'Almacén',
     (E, 12.00, 'Paquete de 10 rollos térmicos de 3 1/8 in a 10-15 $.')),
    ('bev_napkins_store', 'Servilletas de papel (reserva de almacén)', 'Beverage napkins (storeroom backup)',
     'Paper & Cleaning', 'case', 2, 5, 'Almacén',
     (E, 28.00, 'Mismo producto y precio que las servilletas de barra (stock por ubicación, 01!Instrucciones!A23).')),
    ('fryer_oil', 'Aceite de girasol (garrafa 5 L)', 'Canola fryer oil (35 lb jug)', 'Dry Goods', 'lb', 35, 70,
     'Almacén', ('pil', 'fryer_oil')),
    ('red_wine_vinegar', 'Vinagre de vino', 'Red wine vinegar', 'Dry Goods', 'gal', 2, 4, 'Almacén',
     (E, 9.00, 'Vinagre de vino tinto, caja 4 x 1 gal a 32-40 $ → 8-10 $/gal.')),
    ('dried_beans', 'Legumbres secas', 'Dried beans', 'Dry Goods', 'lb', 20, 50, 'Almacén',
     (E, 1.30, 'Alubias secas en saco de 25 lb a 28-36 $ → 1.10-1.45 $/lb.')),
    # ---- 04-06 (no está en el 01)
    ('cod_fillet', 'Merluza fresca (04-06)', 'Fresh cod fillet', 'Seafood', 'lb', None, None, None,
     (E, 11.50, 'Filete de bacalao fresco del Atlántico, 10-13 $/lb de distribuidor. La merluza (hake) apenas se vende '
                'fresca en EE. UU.; el cod es el pescado blanco equivalente.')),
]

# Unidades de COMPRA reales (texto informativo, «Plausible US foodservice purchase units»)
FORMATO = {
    'chicken_breast': '40 lb case', 'beef_tenderloin': 'Whole PSMO, about 6 lb (catch weight)',
    'salmon_fillet': 'Whole side, about 3 lb', 'shrimp': '20 lb case (10 x 2 lb bags)', 'tomato': '25 lb case',
    'yellow_onion': '10 lb bag', 'romaine': 'Case, 24 heads', 'potato': '50 lb bag', 'evoo': 'Case, 4 x 1 gal',
    'kosher_salt': 'Case, 12 x 3 lb boxes', 'black_pepper': '5 lb bag', 'arborio': '25 lb bag',
    'dry_pasta': '20 lb case', 'ap_flour': '50 lb bag', 'eggs': '15 dozen case', 'heavy_cream': 'Case, 12 x 1 qt',
    'butter': 'Case, 36 x 1 lb', 'parmesan': 'Case, 2 x 5 lb wedges', 'lemon': 'Case, 115 count',
    'garlic': 'Case, 4 x 5 lb jars', 'coffee': 'Case, 5 x 2 lb bags', 'whole_milk': 'Case, 4 x 1 gal',
    'oat_milk': 'Case, 12 x 1 qt', 'orange_juice': 'Case, 4 x 1 gal', 'cola': 'Case, 24 x 12 fl oz cans',
    'draft_beer': '1/2 bbl keg (15.5 gal)', 'water': 'Case, 24 x 16.9 fl oz', 'tonic': 'Case, 24 x 6.7 fl oz',
    'red_wine': 'Case, 12 x 750 ml', 'white_wine': 'Case, 12 x 750 ml', 'ice': '20 lb bag', 'sugar': '50 lb bag',
    'bev_napkins_bar': 'Case, 4,000 napkins', 'paper_straws': 'Case, 2,500 straws', 'disposable_cups': 'Sleeve, 50 cups',
    'paper_towels': 'Case, 12 rolls', 'plastic_wrap': '18 in x 2,000 ft roll', 'aluminum_foil': '18 in x 500 ft roll',
    'trash_bags': 'Pack, 50 bags', 'nitrile_gloves': 'Case, 10 x 100 gloves', 'dish_detergent': '5 gal pail',
    'degreaser': '1 gal jug', 'sanitizer': '1 gal jug', 'hotel_pans': 'Each', 'day_dots': 'Roll, 1,000 labels',
    'receipt_rolls': 'Pack, 10 rolls', 'bev_napkins_store': 'Case, 4,000 napkins', 'fryer_oil': '35 lb jug-in-box',
    'red_wine_vinegar': 'Case, 4 x 1 gal', 'dried_beans': '25 lb bag', 'cod_fillet': '10 lb case (fillets)',
}

# Productos que NO están en la tabla maestra pero entran en las líneas del historial de pedidos (03).
EXTRA = {
    'ground_beef': ('Ground beef (80/20)', 'lb', ('der', 'ground_beef', 1.0, 'Precio por lb del piloto (USDA AMS).')),
    'chicken_thighs': ('Chicken thighs (bone-in)', 'lb', ('der', 'chicken_thighs', 1.0, 'Precio por lb del piloto (BLS).')),
    'pork_cheeks': ('Pork cheeks', 'lb', ('der', 'pork_cheeks', 1.0, 'Precio por lb del piloto.')),
    'pulled_pork': ('Pulled pork (cooked)', 'lb', ('der', 'pulled_pork', 1.0, 'Precio por lb del piloto.')),
    'carrot': ('Carrots', 'lb', ('der', 'carrot', 1.0, 'Precio por lb del piloto, redondeado al céntimo.')),
    'red_onion': ('Red onions', 'lb', ('der', 'red_onion', 1.0, 'Precio por lb del piloto.')),
    'lime': ('Limes', 'each', ('der', 'lime', 1.0, 'Precio por unidad del piloto, redondeado al céntimo.')),
}


def precio_de(regla):
    if regla[0] == 'pil':
        return r2(CAT_PIL[regla[1]]['precio']), fuente_piloto(regla[1])
    if regla[0] == 'der':
        _, pid, factor, razon = regla
        base = CAT_PIL[pid]
        p = r2(base['precio'] * factor)
        return p, OrderedDict([
            ('tipo', '[derivado]'), ('razonamiento', razon),
            ('calculo', '%s × %s = %s' % (base['precio'], round(factor, 9), p)),
            ('base_piloto', OrderedDict([('id', pid), ('precio', base['precio']), ('ud_compra', base['ud_compra']),
                                         ('fuente', base['fuente'])]))])
    _, p, razon = regla
    return r2(p), OrderedDict([('tipo', '[estimado]'), ('razonamiento', razon), ('fecha', FECHA)])


PRODUCTOS = []
POR_ID = OrderedDict()
fila_zona = {'Cocina': 5, 'Barra': 5, 'Almacén': 5}
fila_b08 = 5
for (pid, es, en, cat, ud, par, pmax, zona, regla) in MAESTRA:
    precio, fuente = precio_de(regla)
    rec = OrderedDict([
        ('id', pid), ('es', es), ('en', en), ('categoria_es', 'Otros' if pid == 'eggs' else CAT_INV[cat]), ('categoria_en', cat), ('unidad', ud),
        ('precio', precio), ('par', par), ('par_max', pmax), ('formato_compra', FORMATO[pid]),
        ('id_piloto', regla[1] if regla[0] in ('pil', 'der') else None), ('fuente', fuente)])
    if zona:
        rec['libro01'] = OrderedDict([('hoja_es', zona), ('hoja_en', H[zona]), ('fila', fila_zona[zona])])
        rec['b08_fila'] = fila_b08
        fila_zona[zona] += 1
        fila_b08 += 1
    PRODUCTOS.append(rec)
    POR_ID[pid] = rec
EXTRAS = OrderedDict()
for pid, (en, ud, regla) in EXTRA.items():
    p, f = precio_de(regla)
    EXTRAS[pid] = OrderedDict([('id', pid), ('en', en), ('unidad', ud), ('precio', p), ('fuente', f)])


def P(pid):
    return POR_ID[pid]['precio'] if pid in POR_ID else EXTRAS[pid]['precio']


def EN(pid):
    return POR_ID[pid]['en']


# ============================================================================ 2. Proveedores (§5.2, D15)
PROV = [
    # es, en, cat EN, tax, licencia, contacto, tel, email, incidencias, dirección, día pedido, día reparto, lead,
    # mínimo, pago, homologado, notas directorio, notas 03, transporte, rebate, notas condiciones
    ('Cárnicas del Norte (ejemplo)', 'Prime Cut Meats (sample)', 'Meat & Poultry', '00-0000001', 'USDA Est. 00001',
     'Mike Reynolds', '(555) 555-0101', 'orders@primecutmeats.example', 'credits@primecutmeats.example · (555) 555-0102',
     '1200 Industrial Pkwy, Unit 12 · Anytown, USA 00001', 'Mon & Thu by 12 p.m.', 'Tue & Fri', 1, 300, 'Net 30', 'Y',
     'Require an invoice with lot numbers and arrival temperature.',
     'Require an invoice with lot numbers and arrival temperature', 'Free over $300', 0.02,
     '$25 delivery fee below the minimum.'),
    ('Pescados Ría Fresca (ejemplo)', 'Harbor Fresh Seafood (sample)', 'Seafood', '00-0000002', 'FDA Reg. 00000000002',
     'Dana Whitfield', '(555) 555-0103', 'orders@harborfreshseafood.example',
     'credits@harborfreshseafood.example · (555) 555-0104', 'Pier 8, Harbor Market · Anytown, USA 00002',
     'Daily by 5 p.m.', 'Tue to Sat', 1, 200, 'Net 15', 'Y', 'Arrives on ice; reject anything above 41 °F.',
     'Arrives on ice; reject anything above 41 °F', 'Free', 0, 'Market price, set the day before delivery.'),
    ('Frutas y Verduras La Huerta (ejemplo)', 'Green Valley Produce (sample)', 'Produce', '00-0000003',
     'PACA Lic. 00000003', 'Carlos Mendez', '(555) 555-0105', 'orders@greenvalleyproduce.example',
     'credits@greenvalleyproduce.example', 'Produce Terminal, Bldg 4 · Anytown, USA 00003', 'Mon, Wed & Fri by 6 p.m.',
     'Tue, Thu & Sat', 1, 150, 'COD', 'Y', 'Seasonal produce: confirm prices every week.',
     'Seasonal produce: confirm prices every week', 'Free over $150', 0, 'No order minimum on Saturdays.'),
    ('Distribuciones Economato Sur (ejemplo)', 'Pantry Foodservice Supply (sample)', 'Dry Goods', '00-0000004',
     'FDA Reg. 00000000004', 'Tom Becker', '(555) 555-0106', 'orders@pantryfoodservice.example',
     'credits@pantryfoodservice.example', '450 Commerce Dr, Suite 27 · Anytown, USA 00004', 'Tue by 2 p.m.', 'Thu', 2,
     500, 'Net 45', 'Y', '2% volume rebate on purchases over $2,000 a month.',
     '2% volume rebate on purchases over $2,000 a month', '$35 below the minimum', 0.02, 'Rebate paid quarterly.'),
    ('Bebidas y Distribución Levante (ejemplo)', 'Metro Beverage Distributors (sample)', 'Alcoholic Beverages',
     '00-0000005', 'State dist. lic. 000005', 'Jen Park', '(555) 555-0107', 'orders@metrobeverage.example',
     'credits@metrobeverage.example', '82 Route 40 · Anytown, USA 00005', 'Mon by 12 p.m.', 'Wed', 2, 250, 'Net 30',
     'Y', 'Kegs and CO2 cylinders on loan: check the deposit on every invoice.',
     'Kegs and CO2 cylinders on loan: check the deposit on every invoice', 'Free over $250', 0.03,
     'Deposit on kegs and returnable crates.'),
    ('Higiene Profesional HORECA (ejemplo)', 'ProClean Janitorial Supply (sample)', 'Paper & Cleaning', '00-0000006',
     'N/A (non-food supplier)', 'Lisa Grant', '(555) 555-0108', 'orders@procleansupply.example',
     'credits@procleansupply.example', '15 Industry Ave · Anytown, USA 00006', 'Wed by 4 p.m.', 'Fri', 2, 150, 'Net 30',
     'Pending', 'Grade D (2.2/5) at the last review: approval ON HOLD until it improves. Find an alternative before '
                'the next review.', 'Ask for the Safety Data Sheet (SDS) of every product', 'Free over $150', 0,
     'Safety Data Sheets (SDS) with every delivery.'),
]
CLAVES_PROV = ['es', 'en', 'categoria_en', 'tax_id', 'licencia', 'contacto', 'telefono', 'email', 'contacto_incidencias',
               'direccion', 'dia_pedido', 'dia_reparto', 'lead_time', 'pedido_minimo', 'condiciones_pago',
               'homologado', 'notas_directorio', 'notas_03', 'transporte', 'rebate', 'notas_condiciones']
PROVEEDORES = [OrderedDict(zip(CLAVES_PROV, p)) for p in PROV]
PV = {p['es']: p for p in PROVEEDORES}
V = [p['en'] for p in PROVEEDORES]  # V[0] = Prime Cut … V[5] = ProClean

# ============================================================================ 3. Celdas por libro
LIBROS = OrderedDict()


def celda(libro, hoja_es, ref, valor, nota=None):
    d = OrderedDict([('hoja_es', hoja_es), ('hoja_en', H[hoja_es]), ('celda', ref), ('valor', valor)])
    if nota:
        d['nota'] = nota
    LIBROS.setdefault(libro, []).append(d)


# ---- 01 · B-F y J de las tres zonas
for p in PRODUCTOS:
    if 'libro01' not in p:
        continue
    h, f = p['libro01']['hoja_es'], p['libro01']['fila']
    for col, v in (('B', p['en']), ('C', p['categoria_en']), ('D', p['unidad']), ('E', p['par']),
                   ('F', p['par_max']), ('J', p['precio'])):
        celda('01', h, '%s%d' % (col, f), v)
    for col, v in (('B', p['en']), ('C', p['categoria_en']), ('D', p['unidad']), ('E', p['precio'])):
        celda('B08', 'Conteo Rápido', '%s%d' % (col, p['b08_fila']), v)

# ---- 02 · Directorio (filas 4-9), Comparativa (4-13), Evaluación (B4:B9), Condiciones (F/J 4-9)
for i, p in enumerate(PROVEEDORES):
    f = 4 + i
    for col, k in (('B', 'en'), ('C', 'categoria_en'), ('D', 'tax_id'), ('E', 'licencia'), ('F', 'contacto'),
                   ('G', 'telefono'), ('H', 'email'), ('I', 'contacto_incidencias'), ('J', 'direccion'),
                   ('K', 'dia_pedido'), ('L', 'dia_reparto'), ('M', 'lead_time'), ('N', 'pedido_minimo'),
                   ('O', 'condiciones_pago'), ('P', 'homologado'), ('S', 'notas_directorio')):
        celda('02', 'Directorio Proveedores', '%s%d' % (col, f), p[k])
    celda('02', 'Evaluación Proveedores', 'B%d' % f, p['en'])
    celda('02', 'Condiciones Comerciales', 'F%d' % f, p['transporte'])
    celda('02', 'Condiciones Comerciales', 'J%d' % f, p['notas_condiciones'])

# Comparativa: pack price de cada proveedor; el mejor (normalizado) = precio maestro (D14)
COMPARATIVA = [
    # fila, id, formato, contenido, {col: precio del pack}
    (4, 'chicken_breast', 'Case, 40 lb', 40, {'F': 124.00, 'G': 128.00, 'H': 131.20, 'J': 126.40}),
    (5, 'beef_tenderloin', 'Whole PSMO, about 6 lb', 6, {}),
    (6, 'salmon_fillet', 'Whole side, about 3 lb', 3, {}),
    (7, 'evoo', 'Case, 4 x 1 gal', 4, {'F': 136.00, 'G': 134.00, 'H': 132.80, 'I': 129.92, 'J': 138.00}),
    (8, 'tomato', '25 lb case', 25, {'F': 51.25, 'G': 52.50, 'H': 49.50, 'I': 50.50, 'J': 49.75}),
    (9, 'romaine', 'Case, 24 heads', 24, {}),
    (10, 'arborio', '25 lb bag', 25, {}),
    (11, 'eggs', '15 dozen case', 15, {}),
    (12, 'whole_milk', 'Case, 4 x 1 gal', 4, {}),
    (13, 'parmesan', 'Case, 2 x 5 lb wedges', 10, {}),
]
for fila, pid, fmt, cont, precios in COMPARATIVA:
    celda('02', 'Comparativa Precios', 'B%d' % fila, EN(pid))
    celda('02', 'Comparativa Precios', 'C%d' % fila, POR_ID[pid]['unidad'])
    celda('02', 'Comparativa Precios', 'D%d' % fila, fmt)
    celda('02', 'Comparativa Precios', 'E%d' % fila, cont)
    for col, v in precios.items():
        celda('02', 'Comparativa Precios', '%s%d' % (col, fila), v)

# ---- 03 · Pedido Actual, Proveedores, Historial
PEDIDO = [('beef_tenderloin', 12), ('red_wine', 12), ('romaine', 10)]
celda('03', 'Pedido Actual', 'C3', V[0])
celda('03', 'Pedido Actual', 'C6', 'PO-2026-004')
subtotal_pedido = 0.0
for i, (pid, q) in enumerate(PEDIDO):
    f = 9 + i
    for col, v in (('B', EN(pid)), ('C', POR_ID[pid]['categoria_en']), ('D', POR_ID[pid]['unidad']), ('E', q),
                   ('F', P(pid))):
        celda('03', 'Pedido Actual', '%s%d' % (col, f), v)
    subtotal_pedido += q * P(pid)
subtotal_pedido = r2(subtotal_pedido)
for i, p in enumerate(PROVEEDORES):
    f = 4 + i
    for col, k in (('A', 'en'), ('B', 'categoria_en'), ('C', 'telefono'), ('D', 'email'), ('E', 'pedido_minimo'),
                   ('F', 'dia_pedido'), ('G', 'lead_time'), ('H', 'notas_03')):
        celda('03', 'Proveedores', '%s%d' % (col, f), p[k])

# Historial: cada pedido cerrado con sus líneas; impuesto 0 (Tax Rates al 0 % en las 10 categorías, D11; en EE. UU.
# la comida y la bebida para reventa van exentas con resale certificate).
HISTORIAL = [
    (5, 'PO-2026-001', V[0], [('beef_tenderloin', 12), ('chicken_breast', 40), ('ground_beef', 20),
                              ('chicken_thighs', 20), ('pork_cheeks', 10), ('pulled_pork', 10)],
     'Invoiced', 'No issues (sample)'),
    (6, 'PO-2026-002', V[4], [('draft_beer', 1), ('red_wine', 12), ('white_wine', 12), ('tonic', 24)],
     'Received', '1/2 bbl keg on deposit (sample)'),
    (7, 'PO-2026-003', V[2], [('tomato', 75), ('yellow_onion', 20), ('romaine', 24), ('potato', 50), ('lemon', 36),
                              ('garlic', 5), ('carrot', 25), ('red_onion', 25), ('lime', 30)],
     'Received with issues', 'Two cases of tomatoes pulled (sample)'),
]
HIST_OUT = []
for fila, po, prov, lineas, estado, obs in HISTORIAL:
    sub = r2(sum(q * P(pid) for pid, q in lineas))
    tax = 0.0
    celda('03', 'Historial Pedidos', 'B%d' % fila, po)
    celda('03', 'Historial Pedidos', 'C%d' % fila, prov)
    celda('03', 'Historial Pedidos', 'D%d' % fila, '%d lines' % len(lineas))
    celda('03', 'Historial Pedidos', 'E%d' % fila, sub)
    celda('03', 'Historial Pedidos', 'F%d' % fila, tax)
    celda('03', 'Historial Pedidos', 'G%d' % fila, r2(sub + tax))
    celda('03', 'Historial Pedidos', 'H%d' % fila, estado)
    celda('03', 'Historial Pedidos', 'I%d' % fila, obs)
    HIST_OUT.append(OrderedDict([('fila', fila), ('po', po), ('proveedor', prov),
                                 ('lineas', [OrderedDict([('id', pid), ('qty', q), ('precio', P(pid)),
                                                          ('importe', r2(q * P(pid)))]) for pid, q in lineas]),
                                 ('subtotal', sub), ('tax', tax), ('total', r2(sub + tax))]))

# ---- 04 · Control Recepción (4-7) e Incidencias (4-6)
RECEP = [
    # fila, prov, albarán, id, texto producto, familia EN, lote, pedido, recibido, °F, visual, incidencia, receptor
    (4, V[0], 'INV-24518', 'beef_tenderloin', 'Beef tenderloin (sample)', 'Raw beef, pork & lamb', 'L-260817', 24, 20,
     37, '✓', '4 lb short of the 24 lb ordered: credit requested by email the same day', 'Head chef'),
    (5, V[1], 'INV-0091', 'cod_fillet', 'Fresh cod fillet (sample)', 'Fresh fish & shucked shellfish', 'L-260818', 20,
     20, 46, '✗', "Arrived at 46 °F against its group's 41 °F limit: whole lot sent back with the driver", 'Sous chef'),
    (6, V[2], 'INV-7742', 'tomato', 'Tomatoes (sample)', 'Whole produce', 'L-260819', 75, 75, 48, '✗',
     'Two 25 lb cases with mold at the bottom: pulled and entered in the waste log', 'Purchasing manager'),
    (7, V[3], 'INV-7743', 'ap_flour', 'All-purpose flour, 50 lb bags (sample)', 'Dry & canned goods (ambient)',
     'L-260820', 100, 100, 72, '✓', None, 'Purchasing manager'),
]
FAM = {v[0]: v for v in mapas.FAMILIAS.values()}
RECEP_OUT = []
for (fila, prov, alb, pid, txt, fam, lote, ped, rec, temp, vis, inc, recp) in RECEP:
    for col, v in (('B', prov), ('C', alb), ('D', txt), ('E', POR_ID[pid]['categoria_en']), ('G', fam), ('H', lote),
                   ('I', ped), ('J', rec), ('L', P(pid)), ('O', temp), ('S', vis), ('T', inc), ('U', recp)):
        celda('04', 'Control Recepción', '%s%d' % (col, fila), v)
    _, mn, mx, _, _ = FAM[fam]
    if mx == 'N/A':
        estado = 'N/A'
    elif temp < mn:
        estado = '✗ REJECT (too cold)'
    elif temp <= mx:
        estado = '✓ ACCEPT'
    else:
        estado = '✗ REJECT (too warm)'
    RECEP_OUT.append(OrderedDict([('fila', fila), ('id', pid), ('familia', fam), ('min_f', mn), ('max_f', mx),
                                  ('temp_f', temp), ('estado_esperado', estado),
                                  ('diferencia', ped - rec), ('valor_diferencia', r2((ped - rec) * P(pid)))]))
celda('04', 'Control Recepción', 'N7', '2027-02-19',
      'Fecha fija (no D25): la harina tiene consumo preferente de meses; el ES ponía la de los huevos (5-sep-2026)')
INCID = [
    (4, 'INV-24518', V[0], 'Beef tenderloin (sample)', 'Wrong quantity',
     '4 lb short of the 24 lb ordered: only 20 lb received', 'Credit requested by email the same day', 'Head chef',
     r2(4 * P('beef_tenderloin')), 0, 'Claimed'),
    (5, 'INV-0091', V[1], 'Fresh cod fillet (sample)', 'Temperature out of range',
     "Arrived at 46 °F against its group's 41 °F limit", 'Whole lot (20 lb) sent back with the driver on the spot',
     'Sous chef', r2(20 * P('cod_fillet')), r2(20 * P('cod_fillet')), 'Credit received'),
    (6, 'INV-7742', V[2], 'Tomatoes (sample)', 'Poor condition', 'Two 25 lb cases with mold at the bottom',
     'Pulled and entered in the waste log', 'Purchasing manager', r2(50 * P('tomato')), 0, 'Open'),
]
for row in INCID:
    fila = row[0]
    for col, v in zip('BCDEFGHIJK', row[1:]):
        celda('04', 'Registro Incidencias', '%s%d' % (col, fila), v)

# ---- 05 · Registro (4-6), Dashboard B10, Plan (4-8)
MERMAS = [
    (4, 'beef_tenderloin', 'Beef tenderloin (sample)', 2.5, 'Prep error', 'Head chef',
     'Butcher yield test with a target yield and weighed trim'),
    (5, 'cod_fillet', 'Fresh cod fillet (sample)', 5, 'Cold chain failure', 'Sous chef',
     'Check the walk-in twice a day and make sure the door closes'),
    (6, 'romaine', 'Romaine lettuce (sample)', 6, 'Past use-by date', 'Purchasing manager',
     'Label the opening date and use in expiration order (FEFO)'),
]
total_mermas = 0.0
for fila, pid, txt, q, motivo, resp, accion in MERMAS:
    for col, v in (('B', txt), ('C', POR_ID[pid]['categoria_en']), ('D', q), ('E', POR_ID[pid]['unidad']),
                   ('F', P(pid)), ('H', motivo), ('I', resp), ('J', accion)):
        celda('05', 'Registro Diario Mermas', '%s%d' % (col, fila), v)
    total_mermas += q * P(pid)
total_mermas = r2(total_mermas)

# 07 · compras por categoría (enero) → también 05!Dashboard!B10 (mismo restaurante, mismo mes, como el ES)
GASTO_CAT = OrderedDict([
    ('Meat & Poultry', 3650), ('Seafood', 2900), ('Dairy & Eggs', 1150), ('Produce', 1700), ('Dry Goods', 1450),
    ('Frozen', 650), ('Alcoholic Beverages', 1900), ('Non-Alcoholic Beverages', 700), ('Paper & Cleaning', 550),
    ('Other', 250)])
COMPRAS_ENE = sum(GASTO_CAT.values())
celda('05', 'Dashboard Mermas', 'B10', COMPRAS_ENE, '= total de enero de 07 «Spend by Category» (como el ES: 10.400 en ambos)')
PLAN = [
    (4, 'Meat & Poultry', 'Prepped food is thrown out at the end of service',
     'Overproduction: prep is done by habit, not against the cover forecast',
     "Prep against the day's forecast and log the leftovers in the waste log before closing", 'Head chef', 250,
     'Pending'),
    (5, 'Produce', 'Expired product turns up with newer stock in front of it',
     'Date labeling is incomplete: opening dates are not written down',
     'Date-label everything you open and put what expires first in front', 'Sous chef', 175, 'In progress'),
    (6, 'Seafood', 'Product lost to a cold chain failure',
     "The walk-in isn't checked daily and the door is left open during service",
     'Temperature log twice a day and a door check at the end of every service', 'HACCP / food safety plan lead', 135,
     'Pending'),
    (7, 'Meat & Poultry', 'Butchery trim loss runs above plan', 'Every cook trims differently: there is no yield test',
     'Butcher yield test with a target yield and weighed trim once a week', 'Station chef', 110, 'Pending'),
    (8, 'Dry Goods', 'Dead stock in dry storage', 'Orders exceed real usage: nobody checks on-hand before ordering',
     'Order from the "Order Qty" column of the inventory sheet and respect the reorder point', 'Purchasing manager',
     55, 'Pending'),
]
for row in PLAN:
    fila = row[0]
    for col, v in zip(['B', 'C', 'D', 'E', 'F', 'H', 'I'], row[1:]):
        celda('05', 'Plan de Acción', '%s%d' % (col, fila), v)

# ---- 06 · Control FIFO (5-10) y Mapa Almacén (4-14)
FIFO = [
    # fila, id, texto, lote, tipo, qty, zona, posición, acción
    (5, 'cod_fillet', 'Fresh cod fillet (sample)', 'L-2609-014', 'Use-by', 8, 'Seafood cooler', 'Shelf 1',
     'Discard and enter it in the waste log'),
    (6, 'heavy_cream', 'Heavy cream (sample)', 'L-2608-221', 'Best-by', 3, 'Prepared foods cooler', 'Shelf 2',
     'Check look, smell and texture before deciding'),
    (7, 'chicken_breast', 'Boneless chicken breast (sample)', 'L-2609-107', 'Use-by', 12, 'Raw meat cooler', 'Shelf 1',
     "Use in today's service"),
    (8, 'tomato', 'Tomatoes (sample)', 'L-2609-088', 'Use-by', 25, 'Produce cooler', 'Bin 3',
     "Prioritize in this week's prep"),
    (9, 'parmesan', 'Parmesan (sample)', 'L-2605-330', 'Use-by', 4, 'Prepared foods cooler', 'Shelf 3',
     'Opened: the shelf life after opening rules, not the date on the package'),
    (10, 'arborio', 'Arborio rice (sample)', 'L-2604-012', 'Best-by', 25, 'Dry storage', 'Rack 2',
     'No risk: place it behind what expires sooner'),
]
for fila, pid, txt, lote, tipo, q, zona, pos, acc in FIFO:
    for col, v in (('B', txt), ('C', POR_ID[pid]['categoria_en']), ('D', lote), ('F', tipo), ('N', q),
                   ('O', POR_ID[pid]['unidad']), ('P', P(pid)), ('R', zona), ('S', pos), ('T', acc)):
        celda('06', 'Control FIFO', '%s%d' % (col, fila), v)
celda('06', 'Control FIFO', 'I9', 10)
MAPA = [
    (4, '41 °F (5 °C) or below', 'Raw meat, poultry and game; always on the bottom shelves', '2 shelving units',
     'Never in the same cooler as ready-to-eat food.'),
    (5, '41 °F (5 °C) or below, fish on ice', 'Fish and shellfish on ice', '1 ice bin',
     'Self-draining ice; replenish every service.'),
    (6, '41 °F (5 °C) or below', 'Dairy, house-made prep, fresh-cut produce and desserts', '3 shelving units',
     'Everything covered, labeled and dated. Never next to raw products.'),
    (7, '34-41 °F (1-5 °C)', 'Produce', '2 shelving units',
     "Don't wash until use; keep ethylene-producing fruit apart."),
    (8, '0 °F (-18 °C) or below', 'Frozen', '1 walk-in unit', 'Write the freezing date. Never refreeze thawed food.'),
    (9, '41 °F (5 °C) or below', 'Food being thawed, labeled', '1 shelving unit',
     'Rack over a tray, covered and labeled THAWING with the date; thaw at 41 °F (5 °C) or below.'),
    (10, 'Cool and dry, 50-70 °F (10-21 °C), under 60% humidity', 'Dry goods, canned goods and non-alcoholic beverages',
     '4 shelving units', 'Keep product at least 6 in (15 cm) off the floor and away from the wall.'),
    (11, '55-60 °F (13-16 °C)', 'Wine, beer and spirits', '1 wine rack',
     'No direct light or vibration; wine bottles on their side.'),
    (12, 'Ambient, separate area', 'Trash, recycling and empty containers', '3 lidded bins',
     'Away from food flow; lidded, foot-pedal bins.'),
    (13, '41 °F (5 °C) or below; shell eggs 45 °F (7 °C) or below', 'Shell eggs and dairy: always refrigerated',
     '1 shelving unit', 'Shell eggs must be held at 45 °F (7 °C) or below (21 CFR 115.50 and 118.4(e); FDA Food Code '
                        '2022 §3-202.11(C)). Store them below ready-to-eat food.'),
    (14, 'Ambient, separate and labeled', 'Cleaning chemicals, sanitizers and their Safety Data Sheets', '1 cabinet',
     'Separate and labeled; NEVER above or next to food or on work surfaces (FDA Food Code 2022 §7-201.11).'),
]
for fila, b, c, d, e in MAPA:
    for col, v in zip('BCDE', (b, c, d, e)):
        celda('06', 'Mapa Almacén', '%s%d' % (col, fila), v,
              'C8 = categoría «Frozen» (clave D8)' if (col == 'C' and fila == 8) else None)

# ---- 07 · Coste por Categoría (B4:B13), Top 20 (4-11), Dashboard (B12:B17)
for i, (cat, v) in enumerate(GASTO_CAT.items()):
    celda('07', 'Coste por Categoría', 'B%d' % (4 + i), v)
TOP20 = [
    # fila, id, cantidad mensual (ud EN), precio anterior, proveedor
    (4, 'beef_tenderloin', 60, 16.40, V[0]),
    (5, 'salmon_fillet', 120, 9.15, V[1]),
    (6, 'shrimp', 90, 8.75, V[1]),
    (7, 'chicken_breast', 270, 2.96, V[0]),
    (8, 'draft_beer', 7.5, 159.00, V[4]),
    (9, 'evoo', 18, 28.60, V[3]),
    (10, 'parmesan', 25, 9.30, V[3]),
    (11, 'potato', 375, 0.82, V[2]),
]
TOP_OUT = []
for fila, pid, qm, pant, prov in TOP20:
    gasto = r2(qm * P(pid))
    for col, v in (('B', EN(pid)), ('C', POR_ID[pid]['categoria_en']), ('D', POR_ID[pid]['unidad']), ('E', gasto),
                   ('H', pant), ('I', P(pid)), ('K', prov)):
        celda('07', 'Top 20 Productos', '%s%d' % (col, fila), v)
    TOP_OUT.append(OrderedDict([('fila', fila), ('id', pid), ('qty_mes', qm), ('precio', P(pid)), ('gasto_mes', gasto),
                                ('precio_anterior', pant), ('variacion', round(P(pid) / pant - 1, 4))]))
VENTAS, CUBIERTOS, EXIST_INI, EXIST_FIN, COMPRAS_ANT = 48700, 1450, 6100, 5900, 14300
TICKET = r2(VENTAS / float(CUBIERTOS))
for ref, v in (('B12', VENTAS), ('B13', CUBIERTOS), ('B14', EXIST_INI), ('B15', EXIST_FIN), ('B16', COMPRAS_ANT),
               ('B17', TICKET)):
    celda('07', 'Dashboard KPIs', ref, v)
FOOD_COST = (EXIST_INI + COMPRAS_ENE - EXIST_FIN) / float(VENTAS)
COSTE_CUBIERTO = (EXIST_INI + COMPRAS_ENE - EXIST_FIN - GASTO_CAT['Paper & Cleaning'] - GASTO_CAT['Other']) / float(
    CUBIERTOS)

# ---- BONUS-09 · Calculadora (4-11)
B09 = [
    # fila, id, consumo/día, lead, cobertura, vida útil, proveedor
    (4, 'chicken_breast', 9, 1, 1, 4, V[0]),
    (5, 'beef_tenderloin', 2, 2, 1, 8, V[0]),
    (6, 'salmon_fillet', 4, 1, 1, 3, V[1]),
    (7, 'whole_milk', 2, 2, 1, 12, V[3]),
    (8, 'potato', 12.5, 2, 2, 30, V[2]),
    (9, 'evoo', 0.6, 4, 1, 540, V[3]),
    (10, 'arborio', 4, 4, 1, 720, V[3]),
    (11, 'draft_beer', 0.25, 3, 5, 120, V[4]),
]
B09_OUT = []
for fila, pid, d, lead, cob, vida, prov in B09:
    p = POR_ID[pid]
    seg = d * cob
    rop = d * lead + seg
    eoq = xround(math.sqrt(2 * d * 365 * COSTE_PEDIDO / (p['precio'] * ALMACEN)), 0)
    cap = xround(d * vida * FACTOR_VIDA, 0)
    sug = min(eoq, cap, p['par_max'])
    for col, v in (('B', p['en']), ('C', p['categoria_en']), ('D', d), ('E', lead), ('F', cob), ('I', p['precio']),
                   ('J', vida), ('K', p['par_max']), ('O', prov)):
        celda('B09', 'Calculadora', '%s%d' % (col, fila), v)
    B09_OUT.append(OrderedDict([
        ('fila', fila), ('id', pid), ('consumo_dia', d), ('lead_time', lead), ('cobertura', cob), ('vida_util', vida),
        ('stock_seguridad', round(seg, 6)), ('punto_pedido', round(rop, 6)), ('par_01', p['par']),
        ('stock_max', p['par_max']), ('par_max_01', p['par_max']), ('precio', p['precio']), ('eoq', eoq),
        ('tope_vida_util', cap), ('sugerida', sug), ('frecuencia_dias', xround(sug / d, 0)),
        ('calc', '%s × (%s + %s) = %s = par 01 (%s); EOQ = ROUND(SQRT(2×%s×365×%s/(%s×%s))) = %s; tope = ROUND(%s×%s×%s) '
                 '= %s; sugerida = MIN(%s, %s, %s) = %s' % (d, lead, cob, round(rop, 6), p['par'], d, COSTE_PEDIDO,
                                                             p['precio'], ALMACEN, eoq, d, vida, FACTOR_VIDA, cap, eoq,
                                                             cap, p['par_max'], sug))]))

# ============================================================================ 4. Fechas vivas (D25)
FECHAS_ES = [
    ('06', 'Control FIFO', 'E5', dt.date(2026, 8, 20)), ('06', 'Control FIFO', 'E6', dt.date(2026, 8, 15)),
    ('06', 'Control FIFO', 'E7', dt.date(2026, 8, 23)), ('06', 'Control FIFO', 'E8', dt.date(2026, 8, 22)),
    ('06', 'Control FIFO', 'E9', dt.date(2026, 8, 17)), ('06', 'Control FIFO', 'E10', dt.date(2026, 7, 15)),
    ('06', 'Control FIFO', 'G5', dt.date(2026, 8, 23)), ('06', 'Control FIFO', 'G6', dt.date(2026, 8, 22)),
    ('06', 'Control FIFO', 'G7', dt.date(2026, 8, 25)), ('06', 'Control FIFO', 'G8', dt.date(2026, 8, 29)),
    ('06', 'Control FIFO', 'G9', dt.date(2026, 10, 23)), ('06', 'Control FIFO', 'G10', dt.date(2027, 6, 20)),
    ('06', 'Control FIFO', 'H9', dt.date(2026, 8, 19)),
    ('02', 'Comparativa Precios', 'N4', dt.date(2026, 8, 3)), ('02', 'Comparativa Precios', 'O4', dt.date(2026, 9, 2)),
    ('02', 'Comparativa Precios', 'N7', dt.date(2026, 8, 3)), ('02', 'Comparativa Precios', 'O7', dt.date(2026, 9, 2)),
    ('02', 'Comparativa Precios', 'N8', dt.date(2026, 8, 10)), ('02', 'Comparativa Precios', 'O8', dt.date(2026, 9, 9)),
]
FECHAS_HOY = []
for libro, hoja, ref, f in FECHAS_ES:
    k = (f - REF_ES).days
    FECHAS_HOY.append(OrderedDict([('libro', libro), ('hoja_es', hoja), ('hoja_en', H[hoja]), ('celda', ref),
                                   ('fecha_es', f.isoformat()), ('desfase', k),
                                   ('formula', '=TODAY()%+d' % k if k else '=TODAY()'), ('numFmtId', 14)]))


def estado_fifo(k_lim, tipo):
    if k_lim < 0:
        return '⚠ CHECK (best-by passed)' if tipo == 'Best-by' else '⛔ EXPIRED — DISCARD'
    if k_lim <= 2:
        return '🔴 URGENT'
    if k_lim <= 7:
        return '\U0001f7e1 USE SOON'
    return '\U0001f7e2 OK'


OFF = {(x['hoja_es'], x['celda']): x['desfase'] for x in FECHAS_HOY}
FIFO_OUT = []
for fila, pid, txt, lote, tipo, q, zona, pos, acc in FIFO:
    g = OFF[('Control FIFO', 'G%d' % fila)]
    lim = g
    if fila == 9:
        lim = min(g, OFF[('Control FIFO', 'H9')] + 10)
    FIFO_OUT.append(OrderedDict([('fila', fila), ('id', pid), ('dias_restantes', lim),
                                 ('estado_esperado', estado_fifo(lim, tipo)),
                                 ('valor_en_riesgo', r2(q * P(pid)))]))


def estado_cot(k):
    return '⛔ QUOTE EXPIRED' if k < 0 else ('\U0001f7e1 expires this week' if k <= 7 else '\U0001f7e2 current')


# ============================================================================ 5. Localizar (246 cadenas GL-mercado)
LOC = OrderedDict()
for p in PRODUCTOS:
    if p['id'] != 'cod_fillet':
        LOC[p['es']] = p['en']
for p in PROVEEDORES:
    LOC[p['es']] = p['en']
LOC.update(OrderedDict([
    # 02 Directorio (en el orden del ES; tax id y licencia → proveedores)
    ('B31245678', '00-0000001'), ('10.05412/NA', 'USDA Est. 00001'), ('Javier Beltrán', 'Mike Reynolds'),
    ('pedidos@ejemplo-carnicas.es', 'orders@primecutmeats.example'),
    ('incidencias@ejemplo-carnicas.es · 948 21 34 60', 'credits@primecutmeats.example · (555) 555-0102'),
    ('Pol. Ind. Landaben, nave 12 · 31012 Pamplona', '1200 Industrial Pkwy, Unit 12 · Anytown, USA 00001'),
    ('Lun y jue antes de 12:00', 'Mon & Thu by 12 p.m.'), ('Mar y vie', 'Tue & Fri'),
    ('30 días fecha factura', 'Net 30'),
    ('Exigir albarán con nº de lote y temperatura de llegada.',
     'Require an invoice with lot numbers and arrival temperature.'),
    ('B36998877', '00-0000002'), ('12.00987/PO', 'FDA Reg. 00000000002'), ('Marta Souto', 'Dana Whitfield'),
    ('pedidos@ejemplo-pescados.es', 'orders@harborfreshseafood.example'),
    ('incidencias@ejemplo-pescados.es · 986 44 12 15', 'credits@harborfreshseafood.example · (555) 555-0104'),
    ('Mercado Central, puesto 8 · 36202 Vigo', 'Pier 8, Harbor Market · Anytown, USA 00002'),
    ('Diario antes de 17:00', 'Daily by 5 p.m.'), ('Mar a sáb', 'Tue to Sat'), ('15 días fecha factura', 'Net 15'),
    ('Llega en hielo fundente; rechazar por encima de 2 °C.', 'Arrives on ice; reject anything above 41 °F.'),
    ('B46112233', '00-0000003'), ('21.024567/V', 'PACA Lic. 00000003'), ('Ana Ferrer', 'Carlos Mendez'),
    ('pedidos@ejemplo-huerta.es', 'orders@greenvalleyproduce.example'),
    ('incidencias@ejemplo-huerta.es', 'credits@greenvalleyproduce.example'),
    ('Mercavalencia, nave 4 · 46009 Valencia', 'Produce Terminal, Bldg 4 · Anytown, USA 00003'),
    ('Lun, mié y vie antes de 18:00', 'Mon, Wed & Fri by 6 p.m.'), ('Mar, jue y sáb', 'Tue, Thu & Sat'),
    ('Contado', 'COD'),
    ('Producto de temporada: confirmar precio cada semana.', 'Seasonal produce: confirm prices every week.'),
    ('B41778899', '00-0000004'), ('40.031204/SE', 'FDA Reg. 00000000004'), ('Rafael Ortega', 'Tom Becker'),
    ('pedidos@ejemplo-economato.es', 'orders@pantryfoodservice.example'),
    ('incidencias@ejemplo-economato.es', 'credits@pantryfoodservice.example'),
    ('Pol. Ind. La Red, nave 27 · 41500 Alcalá de Guadaíra', '450 Commerce Dr, Suite 27 · Anytown, USA 00004'),
    ('Mar antes de 14:00', 'Tue by 2 p.m.'), ('Jue', 'Thu'), ('45 días fecha factura', 'Net 45'),
    ('Rappel del 2 % a partir de 2.000 € al mes.', '2% volume rebate on purchases over $2,000 a month.'),
    ('B03445566', '00-0000005'), ('30.040918/A', 'State dist. lic. 000005'), ('Luis Cano', 'Jen Park'),
    ('pedidos@ejemplo-bebidas.es', 'orders@metrobeverage.example'),
    ('incidencias@ejemplo-bebidas.es', 'credits@metrobeverage.example'),
    ('Ctra. N-340, km 82 · 03008 Alicante', '82 Route 40 · Anytown, USA 00005'),
    ('Lun antes de 12:00', 'Mon by 12 p.m.'), ('Mié', 'Wed'),
    ('Cesión de barriles y CO2: revisar el depósito de envases.',
     'Kegs and CO2 cylinders on loan: check the deposit on every invoice.'),
    ('B28556677', '00-0000006'), ('No aplica (producto no alimentario)', 'N/A (non-food supplier)'),
    ('Silvia Gómez', 'Lisa Grant'), ('pedidos@ejemplo-higiene.es', 'orders@procleansupply.example'),
    ('incidencias@ejemplo-higiene.es', 'credits@procleansupply.example'),
    ('Av. de la Industria 15 · 28108 Alcobendas', '15 Industry Ave · Anytown, USA 00006'),
    ('Mié antes de 16:00', 'Wed by 4 p.m.'), ('Vie', 'Fri'),
    ('Evaluación D (2,2/5) en la última revisión: homologación EN SUSPENSO hasta que mejore. Buscar alternativa antes '
     'de la próxima revisión.', PV['Higiene Profesional HORECA (ejemplo)']['notas_directorio']),
    # 02 Condiciones
    ('Incluido desde 150 €', 'Free over $300'), ('Portes de 12 € por debajo del mínimo.',
                                                 '$25 delivery fee below the minimum.'),
    ('Incluido', 'Free'), ('Subasta: el precio se cierra la víspera.', 'Market price, set the day before delivery.'),
    ('Incluido desde 80 €', 'Free over $150'), ('Sin pedido mínimo los sábados.', 'No order minimum on Saturdays.'),
    ('18 € por debajo del mínimo', '$35 below the minimum'), ('Rappel liquidado por trimestres.',
                                                             'Rebate paid quarterly.'),
    ('Incluido desde 200 €', 'Free over $250'), ('Depósito de barriles y botelleros.',
                                                 'Deposit on kegs and returnable crates.'),
    ('Incluido desde 100 €', 'Free over $150'), ('Fichas de seguridad en cada entrega.',
                                                 'Safety Data Sheets (SDS) with every delivery.'),
    # 03
    ('PED-2026-004', 'PO-2026-004'),
    ('Exigir el albarán con el nº de lote y la temperatura de llegada',
     'Require an invoice with lot numbers and arrival temperature'),
    ('Llega en hielo fundente; rechazar por encima de 2 °C', 'Arrives on ice; reject anything above 41 °F'),
    ('Producto de temporada: confirma el precio cada semana', 'Seasonal produce: confirm prices every week'),
    ('Rappel del 2 % a partir de 2.000 € al mes', '2% volume rebate on purchases over $2,000 a month'),
    ('Cesión de barriles y CO2: revisar el depósito de envases',
     'Kegs and CO2 cylinders on loan: check the deposit on every invoice'),
    ('Pedir la ficha de datos de seguridad de cada producto', 'Ask for the Safety Data Sheet (SDS) of every product'),
    ('PED-2026-001', 'PO-2026-001'), ('6 líneas', '6 lines'), ('Sin incidencias (ejemplo)', 'No issues (sample)'),
    ('PED-2026-002', 'PO-2026-002'), ('4 líneas', '4 lines'),
    ('Barril de 30 L en depósito (ejemplo)', '1/2 bbl keg on deposit (sample)'), ('PED-2026-003', 'PO-2026-003'),
    ('9 líneas', '9 lines'), ('Dos cajas de tomate retiradas (ejemplo)', 'Two cases of tomatoes pulled (sample)'),
    # 04
    ('ALB-24518', 'INV-24518'), ('Solomillo de ternera (ejemplo)', 'Beef tenderloin (sample)'),
    ('L-260817', 'L-260817'),
    ('Faltan 2 kg de los 12 pedidos: reclamado por correo el mismo día',
     '4 lb short of the 24 lb ordered: credit requested by email the same day'),
    ('Jefe de cocina', 'Head chef'), ('ALB-0091', 'INV-0091'), ('Merluza fresca (ejemplo)', 'Fresh cod fillet (sample)'),
    ('L-260818', 'L-260818'),
    ('Llega a 5 °C con el límite de su familia en 2 °C: partida completa devuelta al transportista',
     "Arrived at 46 °F against its group's 41 °F limit: whole lot sent back with the driver"),
    ('Segundo de cocina', 'Sous chef'), ('ALB-7742', 'INV-7742'), ('Tomate (ejemplo)', 'Tomatoes (sample)'),
    ('L-260819', 'L-260819'),
    ('Dos cajas de 10 kg con moho en el fondo: retiradas y anotadas en el control de mermas',
     'Two 25 lb cases with mold at the bottom: pulled and entered in the waste log'),
    ('Encargado de compras', 'Purchasing manager'), ('ALB-7743', 'INV-7743'),
    ('Huevos M, docena (ejemplo)', 'All-purpose flour, 50 lb bags (sample)'),
    ('Faltan 2 kg de los 12 pedidos: sólo se reciben 10', '4 lb short of the 24 lb ordered: only 20 lb received'),
    ('Reclamado por correo el mismo día', 'Credit requested by email the same day'),
    ('Llega a 5 °C con el límite de su familia en 2 °C', "Arrived at 46 °F against its group's 41 °F limit"),
    ('Partida completa (8 kg) devuelta al transportista en el momento',
     'Whole lot (20 lb) sent back with the driver on the spot'),
    ('Dos cajas de 10 kg con moho en el fondo', 'Two 25 lb cases with mold at the bottom'),
    ('Retiradas y anotadas en el control de mermas', 'Pulled and entered in the waste log'),
    # 05
    ('Ficha de despiece con rendimiento objetivo y pesada del recorte',
     'Butcher yield test with a target yield and weighed trim'),
    ('Revisar la cámara dos veces al día y el cierre de la puerta',
     'Check the walk-in twice a day and make sure the door closes'),
    ('Lechuga (ejemplo)', 'Romaine lettuce (sample)'),
    ('Etiquetar la fecha de apertura y servir por orden de caducidad',
     'Label the opening date and use in expiration order (FEFO)'),
]))
PLAN_ES = [
    ('Se tira producto elaborado al cierre del servicio', PLAN[0][2]),
    ('Sobreproducción: se produce por costumbre, no contra la previsión de cubiertos', PLAN[0][3]),
    ('Producir contra la previsión del día y anotar el sobrante en el registro de mermas antes de cerrar', PLAN[0][4]),
    ('Aparece género caducado con existencias más nuevas delante', PLAN[1][2]),
    ('El etiquetado FEFO está incompleto: no se anota la fecha de apertura', PLAN[1][3]),
    ('Etiquetar toda apertura con la fecha y colocar delante lo que antes caduca', PLAN[1][4]),
    ('Género perdido por rotura de la cadena de frío', PLAN[2][2]),
    ('La cámara no se revisa a diario y la puerta queda abierta en servicio', PLAN[2][3]),
    ('Registro de temperaturas dos veces al día y revisión del cierre de puerta al terminar el servicio', PLAN[2][4]),
    ('Responsable del plan APPCC', PLAN[2][5]),
    ('La merma de despiece se va por encima de lo previsto', PLAN[3][2]),
    ('Cada cocinero limpia distinto: no hay ficha de despiece', PLAN[3][3]),
    ('Ficha de despiece con rendimiento objetivo y pesada del recorte una vez por semana', PLAN[3][4]),
    ('Jefe de partida', PLAN[3][5]),
    ('Existencias muertas en el economato', PLAN[4][2]),
    ('Se pide por encima del consumo real: no se mira el stock antes de pedir', PLAN[4][3]),
    ('Pedir contra la columna A Pedir del inventario y respetar el punto de pedido', PLAN[4][4]),
]
LOC.update(OrderedDict(PLAN_ES))
LOC.update(OrderedDict([
    # 06 Control FIFO
    ('L-2609-014', 'L-2609-014'), ('Balda 1', 'Shelf 1'), ('Retirar y anotar en el registro de mermas', FIFO[0][8]),
    ('Nata 35 % M.G. (ejemplo)', 'Heavy cream (sample)'), ('L-2608-221', 'L-2608-221'), ('Balda 2', 'Shelf 2'),
    ('Revisión organoléptica antes de decidir', FIFO[1][8]), ('Pechuga de pollo (ejemplo)', FIFO[2][2]),
    ('L-2609-107', 'L-2609-107'), ('Al servicio de hoy', FIFO[2][8]), ('L-2609-088', 'L-2609-088'),
    ('Cajón 3', 'Bin 3'), ('Priorizar en la producción de la semana', FIFO[3][8]),
    ('Queso parmesano (ejemplo)', FIFO[4][2]), ('L-2605-330', 'L-2605-330'), ('Balda 3', 'Shelf 3'),
    ('Abierto: manda la vida útil tras abrir, no la caducidad del envase', FIFO[4][8]),
    ('Arroz redondo (ejemplo)', FIFO[5][2]), ('L-2604-012', 'L-2604-012'), ('Estantería 2', 'Rack 2'),
    ('Sin riesgo: colocar detrás de lo que caduca antes', FIFO[5][8]),
    # 06 Mapa Almacén
    ('0-4 °C', MAPA[0][1]), ('Carne, aves y caza crudas; siempre por debajo de todo lo demás', MAPA[0][2]),
    ('2 estanterías', MAPA[0][3]), ('Nunca en la misma cámara que producto listo para consumo.', MAPA[0][4]),
    ('0-2 °C', MAPA[1][1]), ('Pescados y mariscos sobre hielo fundente', MAPA[1][2]), ('1 mesa fría', MAPA[1][3]),
    ('Hielo fundente con desagüe; reponer en cada servicio.', MAPA[1][4]),
    ('Lácteos, elaborados propios, 5.ª gama y postres', MAPA[2][2]), ('3 estanterías', MAPA[2][3]),
    ('Todo tapado, etiquetado y fechado. Nunca junto a crudos.', MAPA[2][4]),
    ('4-8 °C', MAPA[3][1]), ('Verduras y frutas', MAPA[3][2]),
    ('Sin lavar hasta el momento de uso; aparta la fruta que emite etileno.', MAPA[3][4]),
    ('≤ -18 °C', MAPA[4][1]), ('1 arcón', MAPA[4][3]),
    ('Anota la fecha de congelación. Nunca recongelar lo descongelado.', MAPA[4][4]),
    ('Producto en descongelación, identificado', MAPA[5][2]), ('1 estantería', MAPA[5][3]),
    ('Bandeja con rejilla, tapado y etiquetado EN DESCONGELACIÓN con fecha.', MAPA[5][4]),
    ('Lugar fresco y seco, < 25 °C y HR < 60 %', MAPA[6][1]),
    ('Secos y granos, conservas y bebidas no alcohólicas', MAPA[6][2]), ('4 estanterías', MAPA[6][3]),
    ('Producto a ≥ 10 cm del suelo y separado de la pared.', MAPA[6][4]),
    ('12-16 °C', MAPA[7][1]), ('Bebidas alcohólicas', MAPA[7][2]), ('1 botellero', MAPA[7][3]),
    ('Sin luz directa ni vibraciones; botellas tumbadas.', MAPA[7][4]),
    ('Ambiente, zona separada', MAPA[8][1]), ('Residuos y envases', MAPA[8][2]), ('3 contenedores', MAPA[8][3]),
    ('Fuera del circuito de alimentos; cubos con tapa y pedal.', MAPA[8][4]),
    ('Ambiente constante, 12-20 °C', MAPA[9][1]), ('Huevos: NO refrigerar antes de la venta', MAPA[9][2]),
    ('Sin cambios bruscos de temperatura: la condensación en la cáscara facilita la entrada de Salmonella (Reg. (CE) '
     '589/2008, art. 2).', MAPA[9][4]),
    ('Ambiente, zona separada y señalizada', MAPA[10][1]),
    ('Productos de limpieza, desinfectantes y sus fichas de datos de seguridad', MAPA[10][2]),
    ('1 armario', MAPA[10][3]),
    ('Separado y señalizado; NUNCA sobre ni junto a alimentos ni sobre superficies de trabajo (Reg. (CE) 852/2004, '
     'Anexo II, Cap. IX).', MAPA[10][4]),
]))

GL = [c for c in TEXTOS['cadenas'] if c.get('tratamiento') == 'localizar']
LOCALIZAR = []
FALTAN = []
for c in GL:
    if c['es'] not in LOC:
        FALTAN.append(c['es'])
        continue
    item = OrderedDict([('id', c['id']), ('es', c['es']), ('en', LOC[c['es']])])
    lugares = sorted(set('%s:%s' % (w['f'], w['h']) for w in c['donde']))
    if any(l.startswith('03:Listas') for l in lugares):
        item['nota'] = ('En 03 «Tax Rates»!E2:E10 la celda se VACÍA (D11: tabla de excepciones vacía); '
                        'el EN vale para el resto de apariciones.')
    if c['es'] == 'Huevos M, docena (ejemplo)':
        item['nota'] = 'Cambio de producto declarado en SPEC §4: la 4.ª línea del 04 pasa de huevos a harina (N/A).'
    LOCALIZAR.append(item)
SOBRAN = [k for k in LOC if k not in {c['es'] for c in GL}]

# ============================================================================ 6. Textos con cifra derivada (D20)
m = next(x for x in B09_OUT if x['id'] == 'whole_milk')
TCD = [
    OrderedDict([('book', '01'), ('sheet', 'Instructions'), ('cell', 'A20'),
                 ('en', '- There are free rows at the end of each zone: "Kitchen" down to row 44, "Bar" and '
                        '"Storeroom" down to row 34.'),
                 ('calc', 'Estructura duplicada sin cambios (censo_es.json): Cocina A1:M47 con datos 5-44; Barra y '
                          'Almacén con datos 5-34. 20 + 15 + 15 = 50 productos en las filas 5-24 / 5-19 / 5-19.')]),
    OrderedDict([('book', '03'), ('sheet', 'Instructions'), ('cell', 'A10'),
                 ('en', '5. The order totals are in rows 40 to 42: net amount (pre-tax), tax amount and order total. '
                        'Right below, in row 43, the file tells you whether the order MEETS THE VENDOR\'S MINIMUM and, '
                        'if not, how much you are short: that is what saves you the delivery fee. Rows 45 to 48 break '
                        'the order down by tax rate (0%, 5% and 20% by default: type the rates you actually pay).'),
                 ('calc', 'Filas iguales al ES: H40:H42 totales, A43/H43 mínimo, A45:D48 desglose; A46:A48 = 0 / 5 / 20 '
                          'editables (D11). Ejemplo EN: 12 × %s + 12 × %s + 10 × %s = %s ≥ mínimo %s → «meets».'
                          % (P('beef_tenderloin'), P('red_wine'), P('romaine'), money(subtotal_pedido),
                             PROVEEDORES[0]['pedido_minimo']))]),
    OrderedDict([('book', '04'), ('sheet', 'Instructions'), ('cell', 'A7'),
                 ('en', '3. Choose the product\'s category (the same 10 used across the kit) and the "Suggested group" '
                        'column proposes the food safety group on its own. REFINE it in the "Group" column when the '
                        'line calls for it: most raw meat, poultry, fish and dairy share the 41 °F (5 °C) limit, but '
                        'live shellfish and shell eggs may arrive at up to 45 °F (7 °C), hot food must arrive at '
                        '135 °F (57 °C) or above, and frozen food must arrive frozen. Shell eggs are bought under '
                        '"Dairy & Eggs", so switch them to "Shell eggs".'),
                 ('calc', 'mapas.FAMILIAS: máx. 41 °F en las filas 4-7, 9, 11 y 13; 45 °F en 8 (shellstock) y 15 '
                          '(shell eggs); mín. 135 °F en 12 (hot TCS); congelado ≤ 0 °F en 10. FAMILIA_POR_CATEGORIA: '
                          'Dairy & Eggs → Dairy & other refrigerated TCS (41 °F), de ahí el aviso de los huevos.'),
                 ('cita_columnas', ['Suggested group', 'Group'])]),
    OrderedDict([('book', '04'), ('sheet', 'Instructions'), ('cell', 'A8'),
                 ('en', '4. Type the measured temperature: the cell turns RED and the temperature check column says '
                        'REJECT as soon as it falls outside its group\'s range. There are five possible answers and it '
                        'pays to know them: ACCEPT · REJECT (too warm) · REJECT (too cold), because fish at -4 °F '
                        '(-20 °C) arrived frozen and lettuce at 28 °F (-2 °C) is frost-damaged · N/A when that group is '
                        'not temperature-controlled (dry goods, beverages, non-food) · and NO LIMIT FOR THIS FAMILY when '
                        'what you typed in "Group" is not in the table. That last one is not a bug: it is the file '
                        'refusing to give you an approval it cannot back up.'),
                 ('calc', '-4 °F < 30 °F (mín. de Fresh fish & shucked shellfish) → too cold; 28 °F < 32 °F (mín. de '
                          'Whole produce) → too cold; N/A = filas 16-18 de mapas.FAMILIAS. Los huevos salen de la lista '
                          'N/A del ES: en EE. UU. se controlan a 45 °F. Estados = mapas.LITERALES.'),
                 ('cita_columnas', ['Group'])]),
    OrderedDict([('book', '04'), ('sheet', 'Receiving Temps'), ('cell', 'G15'),
                 ('en', 'This is where the log\'s "Suggested group" column comes from. REFINE it in the "Group" column '
                        'when the line calls for it: live shellfish and shell eggs may arrive at up to 45 °F, hot food '
                        'must arrive at 135 °F or above, and frozen food must arrive frozen. Shell eggs are bought '
                        'under "Dairy & Eggs", whose default group is dairy (41 °F): switch them to "Shell eggs".'),
                 ('calc', 'Mismos límites que 04!Instructions!A7 (mapas.FAMILIAS filas 8, 10, 12, 15; '
                          'FAMILIA_POR_CATEGORIA[Dairy & Eggs]).'),
                 ('cita_columnas', ['Suggested group', 'Group'])]),
    OrderedDict([('book', '05'), ('sheet', 'Instructions'), ('cell', 'A8'),
                 ('en', '4. In "Waste Dashboard", type the month\'s purchases in the green cell, net of any tax you can '
                        'reclaim (in the U.S., usually the invoice subtotal). Without it the 3% target cannot be '
                        'calculated; the target percentage is editable too.'),
                 ('calc', '3 %% = Waste Dashboard!B11 = 0.03 (D24, sin cambio). Compras de ejemplo B10 = %s.'
                          % money(COMPRAS_ENE))]),
    OrderedDict([('book', '05'), ('sheet', 'Instructions'), ('cell', 'A10'),
                 ('en', 'TARGET: keep waste below 3% of the month\'s purchases. It is a percentage of YOUR purchases, '
                        'not a fixed dollar amount: $500 of waste is a lot for a bar and very little for a hotel.'),
                 ('calc', 'Objetivo con los datos de ejemplo: 0.03 × %s = %s; mermas de ejemplo = %s (%.2f %%). '
                          'Los 500 son ilustrativos (mismo papel que en el ES; D13 admite $ en texto de ejemplo US).'
                          % (money(COMPRAS_ENE), money(COMPRAS_ENE * 0.03), money(total_mermas),
                             100 * total_mermas / COMPRAS_ENE))]),
    OrderedDict([('book', '05'), ('sheet', 'Waste Dashboard'), ('cell', 'A13'),
                 ('en', 'Type the month\'s purchases in the green cell, net of recoverable tax (the subtotal of your '
                        'vendor invoices). Without it, the kit\'s own 3% target cannot be calculated: that is why the '
                        'dollar target is no longer a fixed "under $500" but that percentage of YOUR purchases.'),
                 ('calc', '0.03 × %s (B10) = %s (C4).' % (money(COMPRAS_ENE), money(COMPRAS_ENE * 0.03)))]),
    OrderedDict([('book', '07'), ('sheet', 'Instructions'), ('cell', 'A7'),
                 ('en', 'Tax you can reclaim is not part of food cost. If you copy the invoice total instead of the net '
                        'amount, your food cost comes out inflated by the tax on the invoice (up to 20% with UK VAT) and '
                        'every decision you base on it will be wrong. In the U.S., food bought for resale is usually tax '
                        'exempt, so subtotal and total often match; sales tax you cannot reclaim is a real cost and '
                        'stays in.'),
                 ('calc', '«entre un 4 % y un 21 %» (tipos de IVA ES) → el tipo de la factura; 20 % = VAT estándar UK, '
                          'la tasa más alta del desglose por defecto 0 / 5 / 20 (D11).')]),
    OrderedDict([('book', '07'), ('sheet', 'KPI Dashboard'), ('cell', 'A19'),
                 ('en', 'Sample figures consistent with January in "Spend by Category": $%s of purchases, $%s of '
                        'beginning and $%s of ending inventory, $%s of sales and %s covers give a food cost of %.1f%%, '
                        'within target. Replace them with yours.'
                        % ('{:,}'.format(COMPRAS_ENE), '{:,}'.format(EXIST_INI), '{:,}'.format(EXIST_FIN),
                           '{:,}'.format(VENTAS), '{:,}'.format(CUBIERTOS), 100 * FOOD_COST)),
                 ('calc', '(%s + %s − %s) / %s = %s / %s = %.2f %% ≤ 32 %% (C4). Compras = SUM(Spend by Category!B4:B13) '
                          '= %s. Coste por cubierto = (%s + %s − %s − %s − %s) / %s = %.2f ≤ 0.3 × %s = %.2f. '
                          'Variación = %s / %s − 1 = %.2f %% ≤ 5 %%.'
                          % (EXIST_INI, COMPRAS_ENE, EXIST_FIN, VENTAS, EXIST_INI + COMPRAS_ENE - EXIST_FIN, VENTAS,
                             100 * FOOD_COST, COMPRAS_ENE, EXIST_INI, COMPRAS_ENE, EXIST_FIN,
                             GASTO_CAT['Paper & Cleaning'], GASTO_CAT['Other'], CUBIERTOS, COSTE_CUBIERTO, TICKET,
                             0.3 * TICKET, COMPRAS_ENE, COMPRAS_ANT, 100 * (COMPRAS_ENE / float(COMPRAS_ANT) - 1)))]),
    OrderedDict([('book', 'B08'), ('sheet', 'Instructions'), ('cell', 'A14'),
                 ('en', '- There are free rows down to row 84.'),
                 ('calc', 'Estructura duplicada sin cambios: Quick Count datos 5-84 (50 de ejemplo en 5-54 + 30 libres), '
                          'total en la fila 86.')]),
    OrderedDict([('book', 'B09'), ('sheet', 'Instructions'), ('cell', 'A19'),
                 ('en', 'The milk example, with the file\'s own numbers: %s gal a day, a %s-day shelf life and a maximum '
                        'stock of %s gal. The EOQ comes out at %d gal. The shelf-life cap brings it down to %d gal, '
                        'which is 70%% of those %s days (%.1f days of use, not %s: the other 30%% is the margin for a '
                        'slow day). And the maximum stock finally sets it at %d gal.'
                        % (m['consumo_dia'], m['vida_util'], m['stock_max'], m['eoq'], m['tope_vida_util'],
                           m['vida_util'], m['vida_util'] * FACTOR_VIDA, m['vida_util'], m['sugerida'])),
                 ('calc', m['calc'])]),
    OrderedDict([('book', 'B09'), ('sheet', 'Instructions'), ('cell', 'A21'),
                 ('en', 'The parameters come with an order cost of 3 (in your currency), a 25% annual holding cost and '
                        'a 70% shelf-life factor. Replace them with yours in "Parameters": they are three green cells '
                        'and they affect all 30 lines.'),
                 ('calc', 'Parameters!D4 = %s, D5 = %s, D12 = %s (D24, heredados del ES); Reorder Calculator filas 4-33.'
                          % (COSTE_PEDIDO, ALMACEN, FACTOR_VIDA))]),
]

# ============================================================================ 7. Salida
IDENT = OrderedDict([
    ('compras_enero_07', COMPRAS_ENE), ('compras_mes_05', COMPRAS_ENE), ('food_cost_07', round(FOOD_COST, 4)),
    ('coste_por_cubierto_07', round(COSTE_CUBIERTO, 4)), ('ticket_medio_07', TICKET),
    ('pedido_actual_03', OrderedDict([('subtotal', subtotal_pedido), ('minimo', PROVEEDORES[0]['pedido_minimo']),
                                      ('estado', "✓ This order meets the vendor's minimum"
                                       if subtotal_pedido >= PROVEEDORES[0]['pedido_minimo'] else 'BELOW')])),
    ('historial_03', HIST_OUT), ('recepcion_04', RECEP_OUT), ('mermas_05_total', total_mermas),
    ('fifo_06', FIFO_OUT),
    ('cotizaciones_02', [OrderedDict([('celda', x['celda']), ('desfase', x['desfase']),
                                      ('estado_esperado', estado_cot(x['desfase']))])
                         for x in FECHAS_HOY if x['celda'].startswith('O')]),
    ('top20_07', TOP_OUT), ('b09', B09_OUT),
])

OUT = OrderedDict([
    ('_leeme', [
        'Datos de mercado del Restaurant Inventory Kit Pro (EN), SPEC D8-D9, D11-D15, D18, D20, D24, D25, §4-§5. Lo '
        'genera generar_mercado.py (no se edita a mano) y lo valida validar_mercado.py. Sesión Claude Code, 2026-09-25.',
        'Precios en USD por UNIDAD de la plantilla (D13: en los xlsx sin símbolo). Fuente del piloto (catálogo del Food '
        'Cost Kit Pro, 24-sep) por id cuando existe, [derivado] si cambia el formato, [estimado] con razonamiento si no. '
        'Ningún € convertido. «Sample prices are illustrative U.S. references: replace them with your own vendor invoices».',
        'aplicar_en.py escribe «libros» celda a celda (mandan sobre la sustitución por cadena), «fechas_hoy» como '
        'fórmulas (D25), «localizar» como sustitución de cadena en el resto de celdas GL-mercado y '
        '«textos_cifra_derivada» en su celda. Las 15 familias de recepción NO están aquí: mapas.FAMILIAS.',
        '«localizar» va en este fichero (clave «localizar»), no en textos_en/GL-mercado.json.',
    ]),
    ('fecha', FECHA),
    ('unidades_d9', mapas.UNIDADES_EN),
    ('categorias_d8', list(CAT.values())),
    ('parametros_b09', OrderedDict([('coste_pedido', COSTE_PEDIDO), ('almacenamiento_anual', ALMACEN),
                                    ('factor_vida_util', FACTOR_VIDA), ('nota', 'D24: valores del ES, «in your currency»')])),
    ('productos', PRODUCTOS),
    ('productos_extra_historial', list(EXTRAS.values())),
    ('b09', B09_OUT),
    ('proveedores', PROVEEDORES),
    ('familias_recepcion', OrderedDict([
        ('fuente', 'mapas.FAMILIAS (15 filas, Receiving Temps!A4:E18, °F) y mapas.FAMILIA_POR_CATEGORIA (G4:H13)'),
        ('duplicado', False),
        ('ejemplo_04', 'Beef tenderloin 37 °F → ACCEPT · cod 46 °F (máx. 41) → REJECT (too warm) · tomatoes 48 °F → '
                       'ACCEPT (rechazo por moho) · AP flour 72 °F → N/A (SPEC §4)')])),
    ('libros', LIBROS),
    ('fechas_hoy', FECHAS_HOY),
    ('vaciar', [OrderedDict([('libro', '03'), ('hoja_es', 'Listas'), ('hoja_en', 'Tax Rates'), ('rango', 'E2:F10'),
                             ('motivo', 'D11: tabla de excepciones de impuesto vacía (con su cabecera y nota)')])]),
    ('localizar', LOCALIZAR),
    ('textos_cifra_derivada', TCD),
    ('identidades', IDENT),
    ('decisiones', [
        'D25: desfases contra el 24-ago-2026, no el 23: con el 23 la merluza/cod (caducidad 23-ago) queda en 0 días = '
        'URGENT y el 06 enseña 4 estados; con el 24 salen los cinco (EXPIRED, CHECK, URGENT, USE SOON ×2, OK), que es lo '
        'que prometen 06!Instrucciones!A21 y la acción «Retirar» de la fila 5. En 02 los tres estados siguen «current».',
        '03 Order Log: impuesto 0.00 en las tres filas (Tax Rates al 0 % en las 10 categorías, D11; la comida y la '
        'bebida para reventa van exentas en EE. UU.). Total = subtotal. Cada subtotal = suma de líneas definidas aquí.',
        '04 fila 7: harina de Pantry Foodservice Supply (no de Green Valley), lote L-260820 y fecha N7 fija; los '
        'valores por celda mandan sobre «localizar» (que traduciría B7 a Green Valley y H7 a L-260819).',
        'Guantes de nitrilo: la unidad US «case» (1,000) sustituye a la cajita de 100 del ES; par 1 / máx. 2.',
        'Top 20 del 07: mismo orden de filas que el ES (la tabla no necesita orden; el Top 5 se ordena solo). Sin '
        'empates en E (el defecto I5 no se dispara con los datos EN).',
        '06 fila 9 (parmesano): vida útil tras abrir 10 días como el ES (los quesos duros están exentos del date '
        'marking de 7 días del Food Code §3-501.17).',
    ]),
])

if __name__ == '__main__':
    print('productos: %d (+%d extra historial) · proveedores: %d · celdas: %d · fechas_hoy: %d · localizar: %d/%d · '
          'cifra_derivada: %d' % (len(PRODUCTOS), len(EXTRAS), len(PROVEEDORES), sum(len(v) for v in LIBROS.values()),
                                  len(FECHAS_HOY), len(LOCALIZAR), len(GL), len(TCD)))
    print('compras enero %s · food cost %.2f %% · pedido 03 %s · mermas %s · FIFO %s'
          % (COMPRAS_ENE, 100 * FOOD_COST, subtotal_pedido, total_mermas, [x['estado_esperado'] for x in FIFO_OUT]))
    if FALTAN or SOBRAN:
        print('FALTAN:', FALTAN)
        print('SOBRAN:', SOBRAN)
        raise SystemExit(1)
    if '--stdout' not in sys.argv:
        with open(SALIDA, 'w', encoding='utf-8') as fh:
            json.dump(OUT, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
        print('escrito', SALIDA)
