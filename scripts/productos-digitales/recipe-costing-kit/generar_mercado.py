#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""generar_mercado.py — escribe mercado_en.json (Food Cost Kit Pro, F2-EN).

SPEC que manda: SPEC.md (D5-D7, D10-D12, D19-D20, §2.1, §2.5). Sesión Claude Code, 24-sep-2026.

Qué hace
  Reúne en un solo JSON los DATOS DE MERCADO de la versión inglesa:
    · catálogo de precios USD por ingrediente, cada uno con su fuente o «[estimado]» (D11);
    · las filas EN de los 8 escandallos (01-08): nombre, categoría, unidad de compra, precio,
      cantidad y unidad de uso, merma (D10) — una fila EN por cada fila de ingrediente ES;
    · precio de carta US de referencia por receta y el food cost implícito contra D12;
    · 04 «Bottle Sizes» (E3, ml), valores por defecto de 06, 08, 09, 10, 11 y el BONUS;
    · libro 12 (test US del solomillo PSMO + cocción de la smash burger) y libro 13 generado
      desde las recetas EN (R2-10);
    · textos con cifra derivada (M5) reescritos con la cifra recalculada;
    · lista blanca de rangos no-D12 para el gate de texto.
  Las cifras derivadas se CALCULAN aquí a partir de los valores EN (nada copiado a mano).

Fuentes
  · BLS Average Price Data (api.bls.gov, serie APU0000xxxxxx, agosto de 2026), consultada hoy.
  · USDA AMS LM_XB459 (boxed beef, 18-sep-2026), texto extraído del PDF en local.
  · WebstaurantStore: listados en mercado_fuentes_web.json (título, precio y URL, leídos hoy).
  · Resúmenes de buscador (fuente secundaria) con su URL, solo donde no hubo nada mejor.
  · «[estimado]» con el razonamiento, cuando no hay fuente. Nunca se convierte un € del ES.

Uso:  python3 generar_mercado.py            (escribe mercado_en.json y un resumen)
      python3 generar_mercado.py --stdout   (solo imprime el resumen)
"""
from __future__ import print_function

import json
import math
import os
import sys
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import mapas  # noqa: E402

FECHA = '2026-09-24'
SALIDA = os.path.join(AQUI, 'mercado_en.json')
WEB = json.load(open(os.path.join(AQUI, 'mercado_fuentes_web.json'), encoding='utf-8'))['listados']
FAC = {r['clave']: r['factor'] for r in mapas.conversions()}
CAT = mapas.CATEGORIAS


def fac(de, a):
    return FAC[de + '→' + a]


def r2(x):
    return round(x + 0.0, 2)


def rp(x):
    """Precio por unidad: 2 decimales desde 1 $, 4 por debajo (una loncha, un bollo)."""
    return round(x, 2) if x >= 1 else round(x, 4)


# ==========================================================================
# 1. Fuentes
# ==========================================================================
def wss(titulo, contenido, unidad, extra=''):
    """Listado de WebstaurantStore: precio del formato ÷ contenido en la unidad de compra."""
    l = WEB[titulo]
    return {'tipo': 'distribuidor', 'distribuidor': 'WebstaurantStore', 'producto': l['titulo'],
            'precio_formato': l['precio_usd'], 'contenido_formato': contenido,
            'unidad_contenido': unidad, 'url': l['url'], 'fecha': FECHA,
            'calculo': '%.2f $ ÷ %s %s' % (l['precio_usd'], contenido, unidad) + (('; ' + extra) if extra else '')}


BLS = {  # serie: (artículo BLS, precio ago-2026, precio ago-2025, unidad)
    'APU0000701111': ('Flour, white, all purpose', 0.548, 0.557, 'lb'),
    'APU0000702111': ('Bread, white, pan', 1.823, 1.841, 'lb'),
    'APU0000706212': ('Chicken legs, bone-in', 1.670, 1.797, 'lb'),
    'APU0000708111': ('Eggs, grade A, large', 2.272, 3.587, 'dozen'),
    'APU0000709112': ('Milk, fresh, whole, fortified', 4.229, 4.171, 'gal'),
    'APU0000711211': ('Bananas', 0.652, 0.666, 'lb'),
    'APU0000711311': ('Oranges, Navel', 1.709, 1.795, 'lb'),
    'APU0000711415': ('Strawberries, dry pint', 2.578, 2.408, 'dry pint'),
    'APU0000712211': ('Lettuce, iceberg', 1.471, 1.673, 'lb'),
    'APU0000712311': ('Tomatoes, field grown', 1.977, 1.925, 'lb'),
    'APU0000720311': ('Wine, red and white table, all sizes, any origin', 13.747, 13.951, 'L'),
}


def bls(serie, extra=''):
    art, v, v25, u = BLS[serie]
    return {'tipo': 'BLS', 'serie': serie, 'articulo': art, 'valor': v, 'unidad': u,
            'periodo': 'Aug 2026 (U.S. city average, retail)', 'valor_aug_2025': v25,
            'url': 'https://fred.stlouisfed.org/series/' + serie,
            'api': 'https://api.bls.gov/publicAPI/v2/timeseries/data/' + serie, 'fecha': FECHA,
            'nota': 'Precio minorista urbano: techo razonable, no precio de distribuidor.' + ((' ' + extra) if extra else '')}


USDA_URL = 'https://www.ams.usda.gov/mnreports/ams_2461.pdf'


def usda(item, cwt, rango, extra=''):
    return {'tipo': 'USDA AMS', 'informe': 'LM_XB459 National Weekly Boxed Beef Cuts - Negotiated Sales',
            'semana': '2026-09-18', 'base': 'FOB plant, Choice, $/cwt (100 lb)', 'item': item,
            'media_ponderada_cwt': cwt, 'rango_cwt': rango, 'por_lb': round(cwt / 100, 4),
            'url': USDA_URL, 'fecha': FECHA,
            'nota': 'Texto extraído del PDF en local (no el resumen de WebFetch).' + ((' ' + extra) if extra else '')}


USDA_RET_URL = 'https://www.ams.usda.gov/mnreports/fvwretail.pdf'


def usda_ret(item, unidad, precio, anuncios, extra=''):
    """USDA AMS National Retail Report - Specialty Crops (FVWRETAIL): precio medio ponderado anunciado."""
    return {'tipo': 'USDA AMS', 'informe': 'FVWRETAIL National Retail Report - Specialty Crops',
            'semana': '2026-09-18 (anuncios del 12 al 24-sep-2026)', 'item': item, 'unidad': unidad,
            'media_ponderada': precio, 'anuncios': anuncios, 'url': USDA_RET_URL, 'fecha': FECHA,
            'nota': 'Precio anunciado al consumidor (media ponderada nacional, «this week»): techo razonable del '
                    'precio de distribuidor, como las series BLS. Sustituye al listado de WebstaurantStore, que '
                    'envía fruta y verdura por mensajería a través de terceros y sale 2-3 veces más caro que el '
                    'distribuidor de un restaurante (revisión R1 EN, CHEF-12).' + ((' ' + extra) if extra else '')}


def snip(url, dato, extra=''):
    return {'tipo': 'fuente secundaria (resumen de buscador)', 'url': url, 'dato': dato, 'fecha': FECHA,
            'nota': extra}


def est(razon):
    return {'tipo': '[estimado]', 'razonamiento': razon, 'fecha': FECHA}


def deriv(razon, *partes):
    return {'tipo': '[derivado]', 'razonamiento': razon, 'partes': list(partes), 'fecha': FECHA}


# ==========================================================================
# 2. Catálogo de ingredientes EN (precio por UNIDAD DE COMPRA de las fichas)
#    fmt13 = (texto de factura, contenido, unidad base del 13, precio del formato)
# ==========================================================================
C = OrderedDict()


def ing(iid, nombre, cat_es, ud, precio, fuente, fmt13, prov, alt_ud=None):
    assert cat_es in CAT, cat_es
    f13 = None if fmt13 is None else OrderedDict([('texto', fmt13[0]), ('contenido', fmt13[1]),
                                                  ('unidad_base', fmt13[2]), ('precio_formato', fmt13[3])])
    C[iid] = OrderedDict([('id', iid), ('nombre_en', nombre), ('categoria_es', cat_es),
                          ('categoria_en', CAT[cat_es]), ('ud_compra', ud), ('precio', precio),
                          ('fuente', fuente), ('formato13', f13), ('proveedor13', prov)])
    if alt_ud:
        C[iid]['otras_ud_compra'] = alt_ud   # {ud: precio} — misma base de precio, otra unidad


def w(titulo):
    return WEB[titulo]['precio_usd']


L_PER_QT = fac('qt', 'L')
L_PER_GAL = fac('gal', 'L')

# --- Carne, ave, pescado y marisco -----------------------------------------
T_TEND = 1720.88
ing('beef_tenderloin', 'Beef tenderloin (whole, PSMO)', 'Carne roja', 'lb', rp(T_TEND / 100),
    usda('189A Loin, tenderloin, trimmed, heavy (PSMO)', T_TEND, [1660.00, 1973.50],
         'Precio de mayorista a pie de planta; el reparto del distribuidor lo sube.'),
    ('Catch weight — price per lb', 1, 'lb', rp(T_TEND / 100)), 'Meat purveyor')
T_GB = 333.28
ing('ground_beef', 'Ground beef (80/20 blend)', 'Carne roja', 'lb', rp(T_GB / 100),
    usda('Ground Beef 81% (10 lb chub basis)', T_GB, [295.00, 393.96]),
    ('40 lb case (4 x 10 lb chubs)', 40, 'lb', r2(40 * rp(T_GB / 100))), 'Meat purveyor')
T_TOP = 509.88   # 184 top butt, boneless: valor de sustitución de las puntas (libro 12)
ing('pork_cheeks', 'Pork cheeks', 'Carne roja', 'lb', 5.75,
    snip('https://localpig.square.site/product/pork-cheeks-1-pound/1054',
         'Local Pig butcher shop, «Pork Cheeks - 1 Pound»: $5.75/lb',
         'Sustituye a la carrillera ibérica (D10): sin fuente de precio en EE. UU.; el plato se mantiene.'),
    ('Price per lb', 1, 'lb', 5.75), 'Meat purveyor')
ing('pulled_pork', 'Pulled pork (fully cooked, sauceless)', 'Carne roja', 'lb',
    rp(w("Smithfield SmokeN'Fast 5 lb. Sauceless Pulled Pork - 2/Case") / 10),
    wss("Smithfield SmokeN'Fast 5 lb. Sauceless Pulled Pork - 2/Case", 10, 'lb'),
    ('10 lb case (2 x 5 lb bags)', 10, 'lb', w("Smithfield SmokeN'Fast 5 lb. Sauceless Pulled Pork - 2/Case")),
    'Broadline distributor')
ing('chicken_thighs', 'Chicken thighs (bone-in)', 'Aves', 'lb', 1.67,
    bls('APU0000706212', 'Proxy: la serie BLS agrupa muslos y contramuslos con hueso («legs and drumsticks»).'),
    ('Catch weight — price per lb', 1, 'lb', 1.67), 'Meat purveyor')
ing('ahi_tuna', 'Sushi-grade ahi tuna (8 oz portions)', 'Pescado', 'lb',
    rp(w('8 oz. Sushi Grade Ahi Tuna Portions - 10 lb.') / 10),
    wss('8 oz. Sushi Grade Ahi Tuna Portions - 10 lb.', 10, 'lb',
        'Sustituye al atún rojo (D10): sin fuente de precio del lomo de bluefin; el plato se mantiene.'),
    ('10 lb case (8 oz portions)', 10, 'lb', w('8 oz. Sushi Grade Ahi Tuna Portions - 10 lb.')),
    'Seafood distributor')
ing('branzino', 'Branzino (whole, farm-raised)', 'Pescado', 'lb', 10.99,
    snip('https://app.warehouserunner.com/costco/44796-fresh-whole-branzino-farm-raised-per-lb',
         'Costco #44796 «Fresh Whole Branzino Farm Raised per lb — $8.99 (down from $10.99)»; se toma el precio normal',
         'Branzino = lubina (Dicentrarchus labrax) de granja: la «lubina salvaje» no se encuentra en EE. UU. (D10).'),
    ('Whole fish — price per lb', 1, 'lb', 10.99), 'Seafood distributor')
ing('smoked_salmon', 'Smoked salmon (sliced)', 'Pescado', 'lb',
    rp(w('Trident Seafoods 3 lb. Atlantic Smoked Salmon') / 3),
    wss('Trident Seafoods 3 lb. Atlantic Smoked Salmon', 3, 'lb'),
    ('3 lb pack', 3, 'lb', w('Trident Seafoods 3 lb. Atlantic Smoked Salmon')), 'Seafood distributor')
ing('scallops', 'Sea scallops U10 (dry-pack)', 'Marisco', 'lb', 30.00,
    est('Sin listado de distribuidor. Un agregador de precios da 25,52 $/lb para vieiras en EE. UU. (jun-2026, '
        'https://www.selinawamucii.com/insights/prices/united-states-of-america/scallops/, fuente secundaria) sin '
        'distinguir calibre; las U10 «dry-pack» de alta cocina cotizan por encima: 30 $/lb.'),
    ('Price per lb', 1, 'lb', 30.00), 'Seafood distributor')
ing('shrimp', 'White shrimp 16/20 (easy-peel)', 'Marisco', 'lb',
    rp(w('Seamazz 16/20 Size Split and Deveined Easy Peel Raw White Shrimp 2 lb. Bag - 10/Case') / 20),
    wss('Seamazz 16/20 Size Split and Deveined Easy Peel Raw White Shrimp 2 lb. Bag - 10/Case', 20, 'lb',
        '«Langostino» del ES = gamba/langostino (Penaeus); en EE. UU. «langostino» es otro animal (squat lobster), '
        'así que el equivalente es la gamba blanca (D10).'),
    ('20 lb case (10 x 2 lb bags)', 20, 'lb',
     w('Seamazz 16/20 Size Split and Deveined Easy Peel Raw White Shrimp 2 lb. Bag - 10/Case')),
    'Seafood distributor')
ing('serrano', 'Serrano ham (bone-in leg, carved on site)', 'Carne roja', 'lb', rp(99.0 / 14),
    snip('https://www.costco.com/p/-/noel-consorcio-serrano-ham-reserva-leg-14-lbs/100592455',
         'Costco, «Noel Consorcio Serrano Ham Reserva Leg, 14 lbs»: $99 en tienda ($119.99 online), según '
         'https://www.today.com/food/groceries/costco-serrano-ham-rcna181641',
         'Sustituye al jamón ibérico loncheado (D10, el ejemplo de la propia SPEC).'),
    ('Bone-in leg, 14 lb', 14, 'lb', 99.0), 'Specialty foods supplier')
ing('croquettes', 'Ham croquettes', 'Congelados', 'each',
    rp(w('Rico Foods Cuban Ham Croquettes 1.1 oz. - 40/Case') / 40),
    wss('Rico Foods Cuban Ham Croquettes 1.1 oz. - 40/Case', 40, 'each'),
    ('Case, 40 x 1.1 oz', 40, 'each', w('Rico Foods Cuban Ham Croquettes 1.1 oz. - 40/Case')),
    'Broadline distributor')
ing('mini_quiche', 'Mini quiches', 'Congelados', 'each',
    rp(w('Cuisine Innovations Mini Quiche Assortment 0.8 oz. - 100/Case') / 100),
    wss('Cuisine Innovations Mini Quiche Assortment 0.8 oz. - 100/Case', 100, 'each'),
    ('Case, 100 x 0.8 oz', 100, 'each', w('Cuisine Innovations Mini Quiche Assortment 0.8 oz. - 100/Case')),
    'Broadline distributor')
ing('mini_rolls', 'Mini brioche rolls', 'Pan/bollería', 'each',
    rp(w('Turano 2 3/4" Sliced Mini Brioche Slider Bun - 216/Case') / 216),
    wss('Turano 2 3/4" Sliced Mini Brioche Slider Bun - 216/Case', 216, 'each'),
    ('Case, 216 rolls', 216, 'each', w('Turano 2 3/4" Sliced Mini Brioche Slider Bun - 216/Case')),
    'Bakery supplier')

# --- Lácteos y huevos -------------------------------------------------------
B = w('Grassland Unsalted Grade AA Butter Solid 1 lb. - 36/Case')
ing('butter', 'Butter (unsalted, Grade AA)', 'Lácteos', '36x1 lb case', B,
    wss('Grassland Unsalted Grade AA Butter Solid 1 lb. - 36/Case', 1, '36x1 lb case'),
    ('36x1 lb case', 36, 'lb', B), 'Dairy distributor')
ISI = 'Isigny Sainte-Mere Unfractionated Unsalted Lamination Butter Sheet 82% Butterfat 2.2 lb. - 10/Case'
LAM = w(ISI)
ing('lamination_butter', 'Lamination butter sheets (82% butterfat)', 'Lácteos', 'lb', rp(LAM / 22),
    wss(ISI, 22, 'lb',
        '«Mantequilla seca (82 % MG)» del ES = mantequilla de hojaldrar en placas: el mismo producto.'),
    ('Case, 10 x 2.2 lb sheets', 22, 'lb', LAM), 'Dairy distributor')
HC = w('Grade A Ultra-Pasteurized 40% Heavy Cream 32 fl. oz. - 12/Case')
ing('heavy_cream', 'Heavy cream (40%)', 'Lácteos', 'qt', rp(HC / 12),
    wss('Grade A Ultra-Pasteurized 40% Heavy Cream 32 fl. oz. - 12/Case', 12, 'qt'),
    ('Case, 12 x 32 fl oz', round(12 * L_PER_QT, 4), 'L', HC), 'Dairy distributor')
ing('whole_milk', 'Whole milk', 'Lácteos', 'gal', 4.23,
    bls('APU0000709112'),
    ('4x1 gal case', round(4 * L_PER_GAL, 4), 'L', r2(4 * 4.229)), 'Dairy distributor',
    alt_ud={'4x1 gal case': r2(4 * 4.229)})
ing('eggs', 'Large eggs (grade A)', 'Huevos', '15 dz case', r2(15 * 2.272),
    deriv('15 docenas × el precio BLS por docena (la caja de 15 docenas es el formato de hostelería, '
          'American Egg Board). Precio minorista: la caja real del distribuidor suele salir más barata.',
          bls('APU0000708111')),
    ('15 dz case', 180, 'each', r2(15 * 2.272)), 'Dairy distributor', alt_ud={'dozen': 2.27})
EW = w("Papetti's Frozen Liquid Egg Whites 5 lb. - 6/Case")
ing('egg_whites', 'Liquid egg whites (pasteurized)', 'Huevos', 'lb', rp(EW / 30),
    wss("Papetti's Frozen Liquid Egg Whites 5 lb. - 6/Case", 30, 'lb'),
    ('Case, 6 x 5 lb cartons', 30, 'lb', EW), 'Dairy distributor')
ing('feta', 'Feta cheese', 'Lácteos', 'lb', rp(w('Krinos Greek Feta Cheese Pail 10 lb.') / 10),
    wss('Krinos Greek Feta Cheese Pail 10 lb.', 10, 'lb'),
    ('10 lb pail', 10, 'lb', w('Krinos Greek Feta Cheese Pail 10 lb.')), 'Dairy distributor')
ing('manchego', 'Aged Manchego-style cheese', 'Lácteos', 'lb',
    rp(w('Santa Marta 4-Month Aged Manchego-Style Cheese Wheel 7 lb. - 2/Case') / 14),
    wss('Santa Marta 4-Month Aged Manchego-Style Cheese Wheel 7 lb. - 2/Case', 14, 'lb'),
    ('Case, 2 x 7 lb wheels', 14, 'lb', w('Santa Marta 4-Month Aged Manchego-Style Cheese Wheel 7 lb. - 2/Case')),
    'Specialty foods supplier')
ing('cream_cheese', 'Cream cheese', 'Lácteos', 'lb',
    rp(w('Philadelphia Original Firm Cream Cheese Block 3 lb. - 6/Case') / 18),
    wss('Philadelphia Original Firm Cream Cheese Block 3 lb. - 6/Case', 18, 'lb'),
    ('Case, 6 x 3 lb blocks', 18, 'lb', w('Philadelphia Original Firm Cream Cheese Block 3 lb. - 6/Case')),
    'Dairy distributor')
ing('american_cheese', 'American cheese (slices)', 'Lácteos', 'each',
    rp(w('Kraft Sliced Yellow American Cheese - 640/Case') / 640),
    wss('Kraft Sliced Yellow American Cheese - 640/Case', 640, 'each'),
    ('Case, 640 slices', 640, 'each', w('Kraft Sliced Yellow American Cheese - 640/Case')), 'Dairy distributor')
ing('cheddar', 'Shredded cheddar cheese', 'Lácteos', 'lb',
    rp(w('Cornerstone 5 lb. Shredded Cheddar Cheese - 4/Case') / 20),
    wss('Cornerstone 5 lb. Shredded Cheddar Cheese - 4/Case', 20, 'lb'),
    ('Case, 4 x 5 lb bags', 20, 'lb', w('Cornerstone 5 lb. Shredded Cheddar Cheese - 4/Case')), 'Dairy distributor')

# --- Verdura, fruta y hierbas -----------------------------------------------
ing('potato', 'White potatoes', 'Verdura raíz', '50 lb bag', w('White Chef Potato 50 lb.'),
    wss('White Chef Potato 50 lb.', 1, '50 lb bag'), ('50 lb bag', 50, 'lb', w('White Chef Potato 50 lb.')),
    'Produce distributor')
ing('asparagus', 'Green asparagus', 'Verdura hoja', 'lb', 3.99,
    usda_ret('Asparagus, GREEN, per lb', 'lb', 3.99, 95, 'Mismo informe, misma semana de 2025: 3,63 $/lb.'),
    ('Price per lb', 1, 'lb', 3.99), 'Produce distributor')
ing('avocado', 'Hass avocado', 'Fruta', 'each', rp(w('Fresh #1 Grade Hass Avocados 48 Count') / 48),
    wss('Fresh #1 Grade Hass Avocados 48 Count', 48, 'each'),
    ('Case, 48 count', 48, 'each', w('Fresh #1 Grade Hass Avocados 48 Count')), 'Produce distributor')
ing('cauliflower', 'Cauliflower (whole heads)', 'Verdura hoja', 'lb', 2.36,
    usda_ret('Cauliflower, per lb', 'lb', 2.36, 836,
             'Coliflor entera, como el ES: vuelve la merma de la pieza (30 %) en lugar de los ramilletes.'),
    ('Price per lb (whole heads)', 1, 'lb', 2.36), 'Produce distributor')
ing('shallot', 'Shallots', 'Verdura raíz', 'lb', rp(w('Unpeeled Shallots 10 lb.') / 10),
    wss('Unpeeled Shallots 10 lb.', 10, 'lb'), ('10 lb bag', 10, 'lb', w('Unpeeled Shallots 10 lb.')),
    'Produce distributor')
ing('fennel', 'Fennel bulbs', 'Verdura raíz', 'lb', rp(w('Fresh Fennel Bulbs 18 lb.') / 18),
    wss('Fresh Fennel Bulbs 18 lb.', 18, 'lb'), ('18 lb case', 18, 'lb', w('Fresh Fennel Bulbs 18 lb.')),
    'Produce distributor')
ing('carrot', 'Carrots', 'Verdura raíz', 'lb', rp(w('Loose Jumbo Carrots 25 lb.') / 25),
    wss('Loose Jumbo Carrots 25 lb.', 25, 'lb'), ('25 lb bag', 25, 'lb', w('Loose Jumbo Carrots 25 lb.')),
    'Produce distributor')
ing('sweet_potato', 'Sweet potatoes', 'Verdura raíz', '40 lb case', w('Fresh Sweet Potatoes US #1 40 lb.'),
    wss('Fresh Sweet Potatoes US #1 40 lb.', 1, '40 lb case'),
    ('40 lb case', 40, 'lb', w('Fresh Sweet Potatoes US #1 40 lb.')), 'Produce distributor')


def manojo(iid, nombre, titulo, oz_manojo):
    precio_oz = w(titulo) / (2.2 * 16)
    ing(iid, nombre, 'Especias/hierbas', 'bunch', r2(precio_oz * oz_manojo),
        deriv('Precio por onza del listado × peso de un manojo [estimado: %s oz]. En EE. UU. las hierbas se '
              'compran por manojo; el ES también usa «manojo».' % oz_manojo, wss(titulo, 2.2, 'lb')),
        ('Price per bunch', 1, 'bunch', r2(precio_oz * oz_manojo)), 'Produce distributor')


manojo('rosemary', 'Fresh rosemary', 'Rosemary 2.2 lb.', 1.0)
manojo('mint', 'Mint', 'Fresh Mint 2.2 lb.', 1.5)
manojo('chives', 'Chives', 'Chives 2.2 lb.', 1.0)
ing('microgreens', 'Microgreens (local grower)', 'Verdura hoja', 'oz', rp(30.00 / 16),
    snip('https://onthegrow.net/pages/best-microgreens-for-restaurants',
         'Microgreens a restaurantes: 20-40 $/lb según variedad y mercado (productores locales); los distribuidores '
         'nacionales venden los de gama básica a 12-18 $/lb (resumen de buscador, sep-2026)',
         'Se toma el punto medio del productor local, 30 $/lb = 1,88 $/oz: un restaurante de mantel los compra al '
         'productor. El listado de WebstaurantStore (micro rúcula a 4,05 $/oz = 64,80 $/lb) era 2 veces el techo.'),
    ('Price per lb', 1, 'lb', 30.00), 'Local grower')
ing('lemon', 'Lemon', 'Fruta', 'each', rp(w('Choice Lemon - 115/Case') / 115),
    wss('Choice Lemon - 115/Case', 115, 'each'), ('Case, 115 count', 115, 'each', w('Choice Lemon - 115/Case')),
    'Produce distributor')
ing('lime', 'Lime', 'Fruta', 'each', rp(w('Fresh Limes - 200/Case') / 200),
    wss('Fresh Limes - 200/Case', 200, 'each'), ('Case, 200 count', 200, 'each', w('Fresh Limes - 200/Case')),
    'Produce distributor')
ing('orange', 'Orange', 'Fruta', 'each', rp(w('Fresh Oranges - 88/Case') / 88),
    wss('Fresh Oranges - 88/Case', 88, 'each'), ('Case, 88 count', 88, 'each', w('Fresh Oranges - 88/Case')),
    'Produce distributor')
CT = w('Fresh Mixed Color Cherry Tomatoes 1 Pint - 12/Case')
ing('cherry_tomato', 'Cherry tomatoes', 'Verdura fruto', 'lb', rp(CT / 7.5),
    deriv('Caja de 12 tarrinas de 1 pinta; peso por tarrina [estimado: 10 oz] → 7,5 lb por caja.',
          wss('Fresh Mixed Color Cherry Tomatoes 1 Pint - 12/Case', 7.5, 'lb')),
    ('Case, 12 x 1 pint (about 7.5 lb)', 7.5, 'lb', CT), 'Produce distributor')
ing('cucumber', 'Persian cucumbers', 'Verdura fruto', 'lb', rp(4.42 / 2),
    usda_ret('Cucumbers, PERSIAN - Greenhouse, 32 oz bag', '32 oz bag', 4.42, 428, '4,42 $ ÷ 2 lb = 2,21 $/lb.'),
    ('Price per lb', 1, 'lb', rp(4.42 / 2)), 'Produce distributor')
ing('red_onion', 'Red onions', 'Verdura raíz', 'lb', rp(w('Jumbo Red Onion 25 lb.') / 25),
    wss('Jumbo Red Onion 25 lb.', 25, 'lb'), ('25 lb bag', 25, 'lb', w('Jumbo Red Onion 25 lb.')),
    'Produce distributor')
ing('yellow_onion', 'Yellow onions', 'Verdura raíz', 'lb', rp(w('Spanish Yellow Onion 10 lb.') / 10),
    wss('Spanish Yellow Onion 10 lb.', 10, 'lb'), ('10 lb bag', 10, 'lb', w('Spanish Yellow Onion 10 lb.')),
    'Produce distributor')
ing('garlic', 'Peeled garlic', 'Especias/hierbas', 'lb', rp(w('Peeled Garlic 5 lb. - 4/Case') / 20),
    wss('Peeled Garlic 5 lb. - 4/Case', 20, 'lb'),
    ('Case, 4 x 5 lb jars', 20, 'lb', w('Peeled Garlic 5 lb. - 4/Case')), 'Produce distributor')
ing('spring_mix', 'Spring mix', 'Verdura hoja', 'lb', rp(w('Fresh Spring Mix Salad 3 lb. - 4/Case') / 12),
    wss('Fresh Spring Mix Salad 3 lb. - 4/Case', 12, 'lb'),
    ('Case, 4 x 3 lb bags', 12, 'lb', w('Fresh Spring Mix Salad 3 lb. - 4/Case')), 'Produce distributor')
ing('roma_tomato', 'Roma tomatoes', 'Verdura fruto', 'lb', rp(w('Plum Tomatoes 25 lb.') / 25),
    wss('Plum Tomatoes 25 lb.', 25, 'lb'), ('25 lb case', 25, 'lb', w('Plum Tomatoes 25 lb.')),
    'Produce distributor')
ing('tomato', 'Tomatoes', 'Verdura fruto', 'lb', 1.98, bls('APU0000712311'),
    ('Price per lb', 1, 'lb', 1.98), 'Produce distributor')
ing('iceberg', 'Iceberg lettuce', 'Verdura hoja', 'lb', 1.47, bls('APU0000712211'),
    ('Price per lb', 1, 'lb', 1.47), 'Produce distributor')
ing('red_pepper', 'Red bell peppers', 'Verdura fruto', 'lb', 2.75,
    est('Sin listado con precio ni serie BLS vigente (APU0000712406 sin datos de 2026). Pimiento rojo de '
        'mayorista en EE. UU.: caja de 11 lb habitualmente entre 25 y 35 $ → ~2,75 $/lb.'),
    ('Price per lb', 1, 'lb', 2.75), 'Produce distributor')
ing('banana', 'Bananas', 'Fruta', 'lb', 0.65, bls('APU0000711211'), ('Price per lb', 1, 'lb', 0.65),
    'Produce distributor')
ing('blueberries', 'Blueberries (IQF)', 'Fruta', 'lb', rp(w('IQF Blueberries 30 lb. Case') / 30),
    wss('IQF Blueberries 30 lb. Case', 30, 'lb'), ('30 lb case', 30, 'lb', w('IQF Blueberries 30 lb. Case')),
    'Broadline distributor')
ing('raspberries', 'Frozen raspberries (IQF)', 'Congelados', 'lb', rp(w('IQF Red Raspberries 10 lb. Bag') / 10),
    wss('IQF Red Raspberries 10 lb. Bag', 10, 'lb'), ('10 lb bag', 10, 'lb', w('IQF Red Raspberries 10 lb. Bag')),
    'Broadline distributor')
FRUTA = (0.652 + 1.709 + 2.578 / 0.75) / 3
ing('assorted_fruit', 'Assorted fruit', 'Fruta', 'lb', r2(FRUTA),
    deriv('Media simple de tres series BLS (plátano, naranja navel, fresa); la pinta seca de fresas se pasa a '
          'libras con un peso [estimado] de 0,75 lb.', bls('APU0000711211'), bls('APU0000711311'),
          bls('APU0000711415')),
    ('Price per lb', 1, 'lb', r2(FRUTA)), 'Produce distributor')
ing('coleslaw_mix', 'Coleslaw mix', 'Verdura hoja', 'lb', rp(w('Plain Cabbage Slaw 5 lb. - 4/Case') / 20),
    wss('Plain Cabbage Slaw 5 lb. - 4/Case', 20, 'lb'),
    ('Case, 4 x 5 lb bags', 20, 'lb', w('Plain Cabbage Slaw 5 lb. - 4/Case')), 'Produce distributor')
PF = w('Les Vergers Boiron Passion Fruit 100% Fruit Puree 2.2 lb. - 6/Case')
ing('passion_puree', 'Passion fruit purée (100% fruit)', 'Fruta', 'kg', rp(PF / 6),
    wss('Les Vergers Boiron Passion Fruit 100% Fruit Puree 2.2 lb. - 6/Case', 6, 'kg',
        'La fruta de la pasión fresca no tiene distribuidor con precio; la pastelería de EE. UU. usa el puré (D10).'),
    ('Case, 6 x 1 kg', round(6 * fac('kg', 'lb'), 4), 'lb', PF), 'Specialty foods supplier')
ing('black_truffle', 'Black truffle (fresh)', 'Setas/hongos', 'oz', 45.00,
    snip('https://www.onlyfinefoods.com/products/fresh-burgundy-black-truffles',
         '«Fresh Burgundy Black Truffles … $45» por onza (sep-2026, temporada de Tuber uncinatum)',
         'En septiembre la trufa negra fresca en EE. UU. es la de Borgoña; la de invierno (melanosporum) va de diciembre a marzo y cuesta más.'),
    ('Price per oz', 0.0625, 'lb', 45.00), 'Specialty foods supplier')

# --- Secos, aceites, salsas -------------------------------------------------
ing('evoo', 'Extra virgin olive oil', 'Aceites/grasas', 'L',
    rp(w('Hometown Provisions Extra Virgin Olive Oil 3 Liter - 4/Case') / 12),
    wss('Hometown Provisions Extra Virgin Olive Oil 3 Liter - 4/Case', 12, 'L'),
    ('Case, 4 x 3 L tins', 12, 'L', w('Hometown Provisions Extra Virgin Olive Oil 3 Liter - 4/Case')),
    'Broadline distributor')
ing('sesame_oil', 'Sesame oil', 'Aceites/grasas', 'L',
    rp(w('Lee Kum Kee 1.65 Liter Premium Pure Sesame Oil - 10/Case') / 16.5),
    wss('Lee Kum Kee 1.65 Liter Premium Pure Sesame Oil - 10/Case', 16.5, 'L'),
    ('Case, 10 x 1.65 L', 16.5, 'L', w('Lee Kum Kee 1.65 Liter Premium Pure Sesame Oil - 10/Case')),
    'Broadline distributor')
SOY = w('Kikkoman Traditionally Brewed Soy Sauce 1 Gallon - 4/Case')
ing('soy_sauce', 'Soy sauce', 'Salsas/condimentos', '4x1 gal case', SOY,
    wss('Kikkoman Traditionally Brewed Soy Sauce 1 Gallon - 4/Case', 1, '4x1 gal case'),
    ('4x1 gal case', round(4 * L_PER_GAL, 4), 'L', SOY), 'Broadline distributor')
ing('sesame_seeds', 'Toasted sesame seeds', 'Secos/granos', 'lb', rp(w('Regal Hulled White Sesame Seeds 5 lb.') / 5),
    wss('Regal Hulled White Sesame Seeds 5 lb.', 5, 'lb'),
    ('5 lb bag', 5, 'lb', w('Regal Hulled White Sesame Seeds 5 lb.')), 'Broadline distributor')
ing('fleur_de_sel', 'Fleur de sel', 'Secos/granos', 'lb',
    w('Regal Spanish Natural Flower of Salt (Fleur de Sel) 1 lb.'),
    wss('Regal Spanish Natural Flower of Salt (Fleur de Sel) 1 lb.', 1, 'lb'),
    ('1 lb tub', 1, 'lb', w('Regal Spanish Natural Flower of Salt (Fleur de Sel) 1 lb.')), 'Broadline distributor')
ing('black_pepper', 'Black peppercorns', 'Especias/hierbas', 'lb', rp(w('Regal Whole Black Peppercorn 5 lb.') / 5),
    wss('Regal Whole Black Peppercorn 5 lb.', 5, 'lb'),
    ('5 lb bag', 5, 'lb', w('Regal Whole Black Peppercorn 5 lb.')), 'Broadline distributor')
ing('flaky_salt', 'Flaky sea salt', 'Secos/granos', 'lb', rp(w('Maldon Sea Salt Bucket 3.1 lb.') / 3.1),
    wss('Maldon Sea Salt Bucket 3.1 lb.', 3.1, 'lb'),
    ('3.1 lb bucket', 3.1, 'lb', w('Maldon Sea Salt Bucket 3.1 lb.')), 'Broadline distributor')
ing('kosher_salt', 'Kosher salt', 'Secos/granos', 'lb',
    rp(w('Morton Bulk Coarse Kosher Salt 3 lb. - 12/Case') / 36),
    wss('Morton Bulk Coarse Kosher Salt 3 lb. - 12/Case', 36, 'lb'),
    ('Case, 12 x 3 lb boxes', 36, 'lb', w('Morton Bulk Coarse Kosher Salt 3 lb. - 12/Case')), 'Broadline distributor')
ing('fine_salt', 'Fine sea salt', 'Secos/granos', 'lb', rp(w('Regal Bulk Fine Sea Salt 25 lb.') / 25),
    wss('Regal Bulk Fine Sea Salt 25 lb.', 25, 'lb'),
    ('25 lb bag', 25, 'lb', w('Regal Bulk Fine Sea Salt 25 lb.')), 'Broadline distributor')
for iid, nom, tit in [('sugar', 'Granulated sugar', 'Domino Pure Cane Extra Fine Granulated Sugar - 50 lb.'),
                      ('brown_sugar', 'Light brown sugar', 'Golden Barrel Light Brown Sugar 50 lb.'),
                      ('powdered_sugar', 'Powdered sugar', 'Domino 10X Confectioners Sugar 50 lb.'),
                      ('ap_flour', 'All-purpose flour', 'ADM All Purpose Flour 50 lb.'),
                      ('bread_flour', 'Bread flour', 'King Arthur Flour Special Patent Flour 50 lb.')]:
    ing(iid, nom, 'Secos/granos', '50 lb bag', w(tit), wss(tit, 1, '50 lb bag'),
        ('50 lb bag', 50, 'lb', w(tit)), 'Broadline distributor')
ing('almond_flour', 'Almond flour (blanched)', 'Secos/granos', 'lb',
    rp(w('Blue Diamond Gluten-Free Almond Flour 25 lb.') / 25),
    wss('Blue Diamond Gluten-Free Almond Flour 25 lb.', 25, 'lb'),
    ('25 lb bag', 25, 'lb', w('Blue Diamond Gluten-Free Almond Flour 25 lb.')), 'Broadline distributor')
ing('cocoa_powder', 'Cocoa powder (Dutch-process)', 'Chocolate/cacao', 'lb',
    rp(w("HERSHEY'S 10-12% Fat Dutch Cocoa Powder 25 lb.") / 25),
    wss("HERSHEY'S 10-12% Fat Dutch Cocoa Powder 25 lb.", 25, 'lb'),
    ('25 lb bag', 25, 'lb', w("HERSHEY'S 10-12% Fat Dutch Cocoa Powder 25 lb.")), 'Broadline distributor')
DC = w('Callebaut Recipe 70/30 Dark Chocolate Callets™ 22 lb.')
ing('dark_chocolate', 'Dark chocolate 70%', 'Chocolate/cacao', 'lb', rp(DC / 22),
    wss('Callebaut Recipe 70/30 Dark Chocolate Callets™ 22 lb.', 22, 'lb'),
    ('22 lb bag (callets)', 22, 'lb', DC), 'Broadline distributor')
WC = w('Callebaut Recipe CW2 White Chocolate Callets™ 22 lb.')
ing('white_chocolate', 'White chocolate', 'Chocolate/cacao', 'lb', rp(WC / 22),
    wss('Callebaut Recipe CW2 White Chocolate Callets™ 22 lb.', 22, 'lb'),
    ('22 lb bag (callets)', 22, 'lb', WC), 'Broadline distributor')
CB = w('Cacao Barry Deodorized Cocoa Butter Pistoles 6.6 lb.')
ing('cocoa_butter', 'Cocoa butter', 'Chocolate/cacao', 'lb', rp(CB / 6.6),
    wss('Cacao Barry Deodorized Cocoa Butter Pistoles 6.6 lb.', 6.6, 'lb'), ('6.6 lb bag', 6.6, 'lb', CB),
    'Broadline distributor')
Y = w("Fleischmann's Fresh Compressed Yeast 1 lb. - 24/Case")
ing('fresh_yeast', 'Fresh yeast (compressed)', 'Secos/granos', 'lb', rp(Y / 24),
    wss("Fleischmann's Fresh Compressed Yeast 1 lb. - 24/Case", 24, 'lb'), ('Case, 24 x 1 lb', 24, 'lb', Y),
    'Bakery supplier')
VA = w("Shank's Premium Pure Vanilla Extract 16 fl. oz.")
ing('vanilla', 'Pure vanilla extract', 'Especias/hierbas', 'pt', VA,
    wss("Shank's Premium Pure Vanilla Extract 16 fl. oz.", 1, 'pt'),
    ('16 fl oz bottle', round(fac('pt', 'L'), 4), 'L', VA), 'Broadline distributor')
CA = w('Torani Puremade Caramel Flavoring Sauce 64 fl. oz. - 4/Case')
ing('caramel', 'Caramel sauce', 'Salsas/condimentos', 'gal', rp(CA / 2),
    wss('Torani Puremade Caramel Flavoring Sauce 64 fl. oz. - 4/Case', 2, 'gal', '4 x 64 fl oz = 256 fl oz = 2 gal'),
    ('Case, 4 x 64 fl oz', round(2 * L_PER_GAL, 4), 'L', CA), 'Broadline distributor')
OL = w('Large Pitted Kalamata Olives 9 lb. (4.4 lb. Dr. Wt.)')
ing('olives', 'Kalamata olives (pitted)', 'Conservas/encurtidos', 'lb', rp(OL / 4.4),
    wss('Large Pitted Kalamata Olives 9 lb. (4.4 lb. Dr. Wt.)', 4.4, 'lb', 'precio sobre el peso escurrido'),
    ('9 lb pail (4.4 lb drained)', 4.4, 'lb', OL), 'Broadline distributor')
JU = w('Regal Juniper Berries 12 oz.')
ing('juniper', 'Juniper berries', 'Especias/hierbas', 'lb', rp(JU / 0.75),
    wss('Regal Juniper Berries 12 oz.', 0.75, 'lb'), ('12 oz jar', 0.75, 'lb', JU), 'Broadline distributor')
CO = w('Chefmaster 10.5 oz. Super Red Liqua-Gel Food Coloring')
ing('food_coloring', 'Red gel food coloring (10.5 oz bottle)', 'Secos/granos', 'each', CO,
    wss('Chefmaster 10.5 oz. Super Red Liqua-Gel Food Coloring', 1, 'each'),
    ('10.5 oz bottle', 1, 'each', CO), 'Bakery supplier')
ing('granola', 'Granola', 'Secos/granos', 'lb', rp(w("Bob's Red Mill 25 lb. Classic Granola") / 25),
    wss("Bob's Red Mill 25 lb. Classic Granola", 25, 'lb'),
    ('25 lb bag', 25, 'lb', w("Bob's Red Mill 25 lb. Classic Granola")), 'Broadline distributor')
ing('coconut', 'Shredded coconut (unsweetened)', 'Secos/granos', 'lb',
    rp(w("Bob's Red Mill Unsweetened Shredded Coconut 25 lb.") / 25),
    wss("Bob's Red Mill Unsweetened Shredded Coconut 25 lb.", 25, 'lb'),
    ('25 lb bag', 25, 'lb', w("Bob's Red Mill Unsweetened Shredded Coconut 25 lb.")), 'Broadline distributor')
ing('honey', 'Honey', 'Secos/granos', 'lb', rp(w('Hometown Provisions Clover Honey 60 lb.') / 60),
    wss('Hometown Provisions Clover Honey 60 lb.', 60, 'lb'),
    ('60 lb pail', 60, 'lb', w('Hometown Provisions Clover Honey 60 lb.')), 'Broadline distributor')
ing('walnuts', 'Walnut halves & pieces', 'Secos/granos', 'lb',
    rp(w('Hometown Provisions Walnut Halves and Pieces 5 lb.') / 5),
    wss('Hometown Provisions Walnut Halves and Pieces 5 lb.', 5, 'lb'),
    ('5 lb bag', 5, 'lb', w('Hometown Provisions Walnut Halves and Pieces 5 lb.')), 'Broadline distributor')
ing('cinnamon', 'Ground cinnamon', 'Especias/hierbas', 'lb', rp(w('Regal Ground Cinnamon 4 lb.') / 4),
    wss('Regal Ground Cinnamon 4 lb.', 4, 'lb'), ('4 lb jar', 4, 'lb', w('Regal Ground Cinnamon 4 lb.')),
    'Broadline distributor')
SUN = w('Roasted Unsalted Sunflower Seeds 30 lb.') / 30
PUM = w('Roasted Unsalted Pumpkin Seeds 12 lb.') / 12
ing('mixed_seeds', 'Mixed seeds (sunflower & pumpkin)', 'Secos/granos', 'lb', r2((SUN + PUM) / 2),
    deriv('Mezcla 1:1 de pipa de girasol y de calabaza tostadas, cada una con su listado.',
          wss('Roasted Unsalted Sunflower Seeds 30 lb.', 30, 'lb'), wss('Roasted Unsalted Pumpkin Seeds 12 lb.', 12, 'lb')),
    ('Price per lb (1:1 blend)', 1, 'lb', r2((SUN + PUM) / 2)), 'Broadline distributor')
SD = w('Bakery de France 32 oz. Sliced Sourdough Bread Loaf - 6/Case')
ing('sourdough', 'Sourdough bread (thick slice)', 'Pan/bollería', 'lb', rp(SD / 12),
    wss('Bakery de France 32 oz. Sliced Sourdough Bread Loaf - 6/Case', 12, 'lb'),
    ('Case, 6 x 32 oz loaves', 12, 'lb', SD), 'Bakery supplier')
ing('english_muffin', 'English muffin', 'Pan/bollería', 'each',
    rp(w("Thomas' Original English Muffins  - 72/Case") / 72),
    wss("Thomas' Original English Muffins  - 72/Case", 72, 'each'),
    ('Case, 72 muffins', 72, 'each', w("Thomas' Original English Muffins  - 72/Case")), 'Bakery supplier')
ing('brioche_bun', 'Brioche bun (4.5 in)', 'Pan/bollería', 'each',
    rp(w('Turano 4 1/2" Sliced Brioche Bun - 80/Case') / 80),
    wss('Turano 4 1/2" Sliced Brioche Bun - 80/Case', 80, 'each'),
    ('Case, 80 buns', 80, 'each', w('Turano 4 1/2" Sliced Brioche Bun - 80/Case')), 'Bakery supplier')
ing('brioche_bun_large', 'Brioche bun, large (5 in)', 'Pan/bollería', 'each',
    rp(w('Turano 5" Sliced Brioche Bun - 80/Case') / 80),
    wss('Turano 5" Sliced Brioche Bun - 80/Case', 80, 'each'),
    ('Case, 80 buns', 80, 'each', w('Turano 5" Sliced Brioche Bun - 80/Case')), 'Bakery supplier')
AC = w('Sambazon Unsweetened Organic Acai 3.5 oz. Pack - 80/Case')
ing('acai', 'Frozen açaí (unsweetened packs)', 'Congelados', 'lb', rp(AC / 17.5),
    wss('Sambazon Unsweetened Organic Acai 3.5 oz. Pack - 80/Case', 17.5, 'lb', '80 x 3.5 oz = 17.5 lb'),
    ('Case, 80 x 3.5 oz packs', 17.5, 'lb', AC), 'Broadline distributor')
OA = w('Oatly Barista Edition Oat Milk 32 fl. oz. - 12/Case')
ing('oat_milk', 'Oat milk (barista)', 'Bebidas/licores', 'qt', rp(OA / 12),
    wss('Oatly Barista Edition Oat Milk 32 fl. oz. - 12/Case', 12, 'qt'),
    ('Case, 12 x 32 fl oz', round(12 * L_PER_QT, 4), 'L', OA), 'Broadline distributor')
BBQ = w("Sweet Baby Ray's BBQ Sauce 1 Gallon - 4/Case")
ing('bbq_sauce', 'BBQ sauce', 'Salsas/condimentos', '4x1 gal case', BBQ,
    wss("Sweet Baby Ray's BBQ Sauce 1 Gallon - 4/Case", 1, '4x1 gal case'),
    ('4x1 gal case', round(4 * L_PER_GAL, 4), 'L', BBQ), 'Broadline distributor')
PK = w('Del Sol 1 Gallon Sliced Dill Pickle Chips - 4/Case')
ing('pickles', 'Dill pickle chips', 'Conservas/encurtidos', 'lb', rp(PK / 18),
    deriv('Caja de 4 garrafas de 1 gal; peso escurrido [estimado: 4,5 lb por galón] → 18 lb por caja.',
          wss('Del Sol 1 Gallon Sliced Dill Pickle Chips - 4/Case', 18, 'lb')),
    ('Case, 4 x 1 gal jars (about 18 lb drained)', 18, 'lb', PK), 'Broadline distributor')
MAYO = w('Hometown Provisions Extra Heavy Mayonnaise 1 Gallon - 4/Case') / (4 * 128)        # $/fl oz
KET = w('Heinz #10 Fancy Tomato Ketchup Pouch 114 oz. Pack - 6/Case') / (6 * 100)           # $/fl oz
SAUCE_QT = r2((2 * MAYO + KET) / 3 * 32)
ing('special_sauce', 'Special sauce (house-made)', 'Salsas/condimentos', 'qt', SAUCE_QT,
    deriv('Salsa de la casa, 2 partes de mayonesa y 1 de kétchup. Kétchup: bolsa de 114 oz de peso ≈ 100 fl oz '
          '[estimado, densidad ≈ 1,14].',
          wss('Hometown Provisions Extra Heavy Mayonnaise 1 Gallon - 4/Case', 4, 'gal'),
          wss('Heinz #10 Fancy Tomato Ketchup Pouch 114 oz. Pack - 6/Case', 600, 'fl oz')),
    ('House-made — cost per qt', round(L_PER_QT, 4), 'L', SAUCE_QT), 'House-made')
ing('veal_stock', 'Dark veal stock', 'Salsas/condimentos', 'qt', 10.00,
    est('Sin listado de fondo de ternera listo para usar con precio. El fondo oscuro congelado de proveedores '
        'de alta cocina ronda 8-14 $ el cuarto de galón; el hecho en casa sale más barato. Se toma 10 $/qt: '
        'sustitúyelo por tu coste real.'),
    ('Price per qt', round(L_PER_QT, 4), 'L', 10.00), 'Specialty foods supplier')
ing('px_sherry', 'Pedro Ximénez (PX) sherry', 'Bebidas/licores', 'L', rp(16.99 / 0.375),
    snip('https://www.wine-searcher.com/find/gonzalez+byass+nectar+pedro+ximenez+dolce+sherry+jerez+andalucia+spain/1/usa',
         'González Byass Nectar Pedro Ximénez 375 ml: $14.99-16.99 en tiendas de EE. UU.; se toma $16.99',
         'Se compra por litro: 16,99 $ ÷ 0,375 L.'),
    ('375 ml bottle', 0.375, 'L', 16.99), 'Liquor distributor')
ing('white_wine', 'Dry white wine', 'Bebidas/licores', 'L', r2(13.747),
    bls('APU0000720311', 'Vino tranquilo de mesa (tinto y blanco), por litro.'),
    ('750 ml bottle', 0.75, 'L', r2(13.747 * 0.75)), 'Liquor distributor')
ing('red_wine', 'Dry red wine', 'Bebidas/licores', 'L', r2(13.747),
    bls('APU0000720311', 'Vino tranquilo de mesa (tinto y blanco), por litro.'),
    ('750 ml bottle', 0.75, 'L', r2(13.747 * 0.75)), 'Liquor distributor')
TON = w('Q Mixers Premium Tonic Water Bottle 6.7 fl. oz. - 24/Case')
ing('tonic', 'Premium tonic water (6.7 fl oz bottle)', 'Bebidas/licores', 'each', rp(TON / 24),
    wss('Q Mixers Premium Tonic Water Bottle 6.7 fl. oz. - 24/Case', 24, 'each'),
    ('Case, 24 x 6.7 fl oz bottles', 24, 'each', TON), 'Broadline distributor')
SO = w('Polar 1 Liter Club Soda - 12/Case')
ing('soda', 'Club soda', 'Bebidas/licores', 'L', rp(SO / 12), wss('Polar 1 Liter Club Soda - 12/Case', 12, 'L'),
    ('Case, 12 x 1 L bottles', 12, 'L', SO), 'Broadline distributor')
ing('ice', 'Ice', 'Congelados', 'lb', 0.20,
    est('Hielo en bolsa comprado: una bolsa de 20 lb cuesta 3-5 $ al por menor → ~0,20 $/lb. El de máquina propia '
        'cuesta bastante menos (agua y luz): pon el tuyo.'),
    ('Price per lb (bagged ice)', 1, 'lb', 0.20), 'Ice supplier')
COF = w('Hometown Provisions Premium Blend Coarse Ground Coffee 2 lb. - 5/Case')
ing('coffee', 'Ground coffee', 'Bebidas/licores', 'lb', rp(COF / 10),
    wss('Hometown Provisions Premium Blend Coarse Ground Coffee 2 lb. - 5/Case', 10, 'lb'),
    ('Case, 5 x 2 lb bags', 10, 'lb', COF), 'Broadline distributor')
FO = w('Admiration Canola Frying Oil - 35 lb.')
ing('fryer_oil', 'Canola oil', 'Aceites/grasas', 'lb', rp(FO / 35),
    wss('Admiration Canola Frying Oil - 35 lb.', 35, 'lb', 'se vende al peso (jug-in-box de 35 lb)'),
    ('35 lb jug-in-box', 35, 'lb', FO), 'Broadline distributor')
BEV = 5 / 12.0 * 13.747 + 7 / 12.0 * 0.50
ing('beverage_mix', 'Beverage (house wine + water)', 'Bebidas/licores', 'L', r2(BEV),
    deriv('Partida compuesta por invitado: 5 fl oz de vino de la casa (BLS) + 7 fl oz de agua [estimado: 0,50 $/L]. '
          'Igual que en el ES, no es un producto de proveedor y NO entra en el 13.', bls('APU0000720311')),
    None, None)

# --- Destilados: la ficha compra en L y enlaza «Bottle Sizes» (E3) ----------------------------
BOT = OrderedDict([  # iid: (nombre EN, precio botella 750 ml, fuente, dónde se usa)
    ('gin', ('Premium gin', 27.99,
             snip('https://www.walmart.com/ip/Tanqueray-London-Dry-Gin-750-mL-47-ABV/12167200',
                  'Tanqueray London Dry Gin 750 ml: $22.97 en oferta, precio normal $27.99; se toma el normal'),
             'Gin & Tonic')),
    ('rum', ('White rum', 18.99,
             snip('https://www.totalwine.com/spirits/rum/silver-rum/flor-de-cana-4-year-rum-extra-seco/p/60255750',
                  'Flor de Caña 4 Extra Seco 750 ml: $14.99-24.99 según tienda (Target, Total Wine, K&L…); la '
                  'mayoría entre $15 y $19; se toma $18.99',
                  'Ron blanco de barra. Con un ron de batalla (Bacardi Superior 11,98 $) el mojito quedaría en un '
                  'pour cost del 12 %, fuera del 18-24 % de D12.'),
             'Mojito')),
    ('tequila', ('Reposado tequila', 24.99,
                 snip('https://www.totalwine.com/spirits/tequila/reposado/espolon-reposado-tequila/p/96444750',
                      'Espolòn Reposado 750 ml: $24.99 en Total Wine ($29.99-33.99 en otras)'),
                 'Margarita')),
    ('triple_sec', ('Triple sec / Cointreau', 36.98,
                    snip('https://www.walmart.com/ip/Cointreau-Orange-Liqueur-Triple-Sec-750-ml-Single-Glass-Bottle-40-ABV/102824681',
                         'Cointreau 750 ml: $36.98 (antes $50.59)'),
                    'Margarita')),
    ('aperol', ('Aperol', 28.73,
                snip('https://www.walmart.com/ip/Aperol-Italian-Liqueur-750-ml-Bottle-11-ABV/163504086',
                     'Aperol 750 ml: $28.73'),
                'Aperol Spritz')),
    ('prosecco', ('Prosecco', 11.99,
                  snip('https://www.totalwine.com/wine/champagne-sparkling-wine/prosecco/zonin-prosecco/p/108038750',
                       'Zonin Prosecco 750 ml: $11.99 en Total Wine ($12.99-14.99 en otras)',
                       'Prosecco de barra. La Marca (18,99 $ en Walmart) pondría el spritz por encima del 24 % de pour cost.'),
                  'Aperol Spritz')),
    ('house_wine', ('House white wine (by the glass)', r2(13.747 * 0.75),
                    deriv('BLS vino de mesa por litro × 0,75 L.', bls('APU0000720311')),
                    '(add your own bottles below)')),
])
for iid, (nom, pb, fu, uso) in BOT.items():
    ing(iid, nom, 'Bebidas/licores', 'L', rp(pb / 0.75), fu, ('750 ml bottle', 0.75, 'L', pb), 'Liquor distributor')
    C[iid]['botella_750ml'] = pb
    C[iid]['donde_se_usa'] = uso
KEG = 110.0
KEG_ML = float(fac('1/6 bbl keg', 'ml'))

# ==========================================================================
# 3. Recetas EN (01-08): una fila EN por fila ES
#    (fila, nombre ES, id catálogo, nombre EN de la fila, cantidad, ud uso, merma, [ud compra], [nota])
# ==========================================================================
# Libro 12 primero: la merma del solomillo de la 01 sale de él (R2-13).
Y12 = OrderedDict([
    ('producto', 'Whole beef tenderloin, PSMO (IMPS 189A: peeled, side muscle on)'),
    ('peso_ap_lb', 89 / 16.0),
    ('precio_ap_lb', C['beef_tenderloin']['precio']),
    ('porcion_oz', 7),
    ('unidades_porcion_por_unidad_peso', 16),
])
COMP12 = [  # (pieza, tipo EN, oz, valor $/lb o None, fuente)
    ('Center-cut and head, trimmed (steaks and roasts)', 'Usable', 54, None,
     'For Love of the Table (ago-2010), test pesado de un solomillo entero sin limpiar de 5 lb 9 oz: «3 lbs. 6 oz. '
     'meat appropriate for steaks or roasts (60.7% of the original weight)» = 54 oz. '
     'https://www.forloveofthetable.com/2010/08/how-to-trim-whole-beef-tenderloin.html'),
    ('Tips and small pieces (for sautés)', 'By-product', 6, rp(T_TOP / 100),
     'Peso: mismo test, «6 oz. of small pieces for quick sautés (6.7%)». Valor: sustitución por la carne que '
     'reemplazan en un salteado, el top sirloin butt deshuesado de USDA AMS LM_XB459 (184, Choice, media ponderada '
     '509,88 $/cwt, 18-sep-2026).'),
    ('Chain, cleaned (for grind or stock)', 'By-product', 5, C['ground_beef']['precio'],
     'Peso: mismo test, «5 oz. of usable trimmed chain meat (5.6%)». Valor: la carne picada 80/20 de la plantilla 08 '
     '(USDA AMS, Ground Beef 81 %), la misma lógica que el ES.'),
    ('Fat, silverskin and sinew', 'Trim (no value)', 24, None,
     'Mismo test: «1 1/2 lbs. unusable scrap (27% of the original weight)» = 24 oz.'),
]
ap_lb = Y12['peso_ap_lb']
p_ap = Y12['precio_ap_lb']
util_lb = sum(c[2] for c in COMP12 if c[1] == 'Usable') / 16.0
subp = sum(c[2] / 16.0 * c[3] for c in COMP12 if c[1] == 'By-product')
coste_ap = ap_lb * p_ap
neto = coste_ap - subp
coste_lb_util = neto / util_lb
merma12 = 1 - p_ap / coste_lb_util
MERMA_TEND = round(merma12, 4)
porciones12 = int(math.floor(round(util_lb * 16 / Y12['porcion_oz'], 6)))
sobra12 = util_lb * 16 - porciones12 * Y12['porcion_oz']

R = []   # recetas


def receta(libro, hoja_es, tipo, target, qf, raciones, filas, precio_ref, fuente_ref, titulo_en=None,
           nota=None, precio_por='receta'):
    R.append(OrderedDict([('libro', libro), ('hoja_es', hoja_es), ('hoja_en', mapas.hoja_en(hoja_es)),
                          ('titulo_en', titulo_en), ('tipo_local', tipo), ('target_fc', target),
                          ('q_factor', qf), ('raciones', raciones), ('filas', filas),
                          ('precio_carta_ref', precio_ref), ('precio_carta_fuente', fuente_ref),
                          ('precio_por', precio_por), ('nota', nota)]))


def F(fila, nombre_es, iid, nombre_en, cant, ud_uso, merma, ud=None, nota=None, cambio=None):
    c = C[iid]
    ud = ud or c['ud_compra']
    precio = c['precio'] if ud == c['ud_compra'] else c['otras_ud_compra'][ud]
    d = OrderedDict([('fila', fila), ('nombre_es', nombre_es), ('id', iid), ('nombre_en', nombre_en),
                     ('categoria_en', c['categoria_en']), ('ud_compra', ud), ('precio', precio),
                     ('cantidad', cant), ('ud_uso', ud_uso), ('merma', merma)])
    if nota:
        d['nota'] = nota
    if cambio:
        d['cambio_cantidad'] = cambio
    return d


# --- 01 -------------------------------------------------------------------
receta('01', 'Escandallo', 'fine_dining', 0.30, 0.10, 1, [
    F(5, 'Solomillo de ternera', 'beef_tenderloin', 'Beef tenderloin (whole, PSMO)', 7, 'oz', MERMA_TEND,
      nota='Catch weight (D20). Merma = «Trim loss % for your cost card» del libro 12 EN (R2-13).'),
    F(6, 'Patata agria', 'potato', 'Potato (all-purpose white)', 5, 'oz', 0.12,
      nota='D10: la variedad Agria apenas se distribuye en EE. UU.; patata blanca de uso general.'),
    F(7, 'Espárrago verde', 'asparagus', 'Green asparagus', 3, 'oz', 0.25),
    F(8, 'Mantequilla', 'butter', 'Butter', 1, 'oz', 0.03),
    F(9, 'Vino Pedro Ximénez', 'px_sherry', 'Pedro Ximénez (PX) sherry', 1.75, 'fl oz', 0.02),
    F(10, 'Fondo oscuro de ternera', 'veal_stock', 'Dark veal stock', 2.75, 'fl oz', 0.07),
    F(11, 'Aceite de oliva virgen extra', 'evoo', 'Extra virgin olive oil', 1, 'fl oz', 0.03),
    F(12, 'Flor de sal', 'fleur_de_sel', 'Fleur de sel', 0.1, 'oz', 0.02),
    F(13, 'Pimienta negra', 'black_pepper', 'Black pepper', 0.07, 'oz', 0.2),
    F(14, 'Microgreens (bandeja 50 g)', 'microgreens', 'Microgreens', 0.1, 'oz', 0),
], 62.00, est('Solomillo de 7 oz con reducción de PX y espárragos en un restaurante de mantel de EE. UU.: '
              'el filet mignon de 7-8 oz se carta entre 55 y 70 $; se toma 62 $.'))

# --- 02 (precio de carta del MENÚ; los pases reparten ese precio en proporción a su coste) ------
receta('02', '1. Aperitivo', 'fine_dining', 0.30, 0.10, 1, [
    F(5, 'Atún rojo (lomo)', 'ahi_tuna', 'Sushi-grade ahi tuna', 3, 'oz', 0.10,
      nota='D10: bluefin sin fuente de precio → ahi en porciones de 8 oz; al venir porcionado, la merma baja del '
           '35 % (lomo entero) al 10 % [estimado].'),
    F(6, 'Aguacate Hass', 'avocado', 'Hass avocado', 0.5, 'each', 0,
      nota='Por pieza (each→each): la piel y el hueso ya van dentro del ½ aguacate, así que la merma es 0 %, la regla '
           'de Instrucciones (revisión R1 EN, CHEF-08).'),
    F(7, 'Sésamo tostado', 'sesame_seeds', 'Toasted sesame seeds', 0.2, 'oz', 0.02),
    F(8, 'Salsa de soja', 'soy_sauce', 'Soy sauce', 1, 'tbsp', 0.02, nota='Formato de caja de la lista D7.'),
    F(9, 'Aceite de sésamo', 'sesame_oil', 'Sesame oil', 2, 'tsp', 0.03),
], None, None, precio_por='menu')
receta('02', '2. Entrante', 'fine_dining', 0.30, 0.10, 1, [
    F(5, 'Vieira fresca (grande)', 'scallops', 'Sea scallops (U10, dry-pack)', 2, 'oz', 0.05,
      nota='Vieira limpia (dry-pack): solo se quita el músculo lateral; la merma del 45 % del ES era la genérica de '
           'marisco con concha [estimado 5 %].'),
    F(6, 'Coliflor', 'cauliflower', 'Cauliflower', 3.5, 'oz', 0.3,
      nota='Coliflor entera (USDA AMS, precio por lb) con la merma de la pieza del ES, 30 % (revisión R1 EN, CHEF-12).'),
    F(7, 'Trufa negra', 'black_truffle', 'Black truffle (fresh)', 5, 'g', 0.1,
      nota='La trufa se pesa en gramos también en EE. UU.; compra por onza.'),
    F(8, 'Nata 35% MG', 'heavy_cream', 'Heavy cream (40%)', 1.75, 'fl oz', 0.03),
    F(9, 'Mantequilla', 'butter', 'Butter', 0.75, 'oz', 0.03),
], None, None, precio_por='menu')
receta('02', '3. Pescado', 'fine_dining', 0.30, 0.10, 1, [
    F(5, 'Lubina salvaje', 'branzino', 'Branzino (whole)', 5.5, 'oz', 0.55,
      nota='Pescado redondo entero → filete con piel: rinde un 40-50 %. Merma 55 % [estimado] en lugar del 40 % '
           'del ES (revisión R1 EN, CHEF-04).'),
    F(6, 'Chalota', 'shallot', 'Shallots', 1, 'oz', 0.15),
    F(7, 'Vino blanco seco', 'white_wine', 'Dry white wine', 1.25, 'fl oz', 0.02),
    F(8, 'Mantequilla', 'butter', 'Butter', 1.5, 'oz', 0.03),
    F(9, 'Hinojo fresco', 'fennel', 'Fennel', 2, 'oz', 0.25),
], None, None, precio_por='menu')
receta('02', '4. Carne', 'fine_dining', 0.30, 0.10, 1, [
    F(5, 'Carrillera ibérica', 'pork_cheeks', 'Pork cheeks', 7, 'oz', 0.15,
      nota='D10: carrillera de cerdo de EE. UU. en lugar de la ibérica (sin fuente de precio).'),
    F(6, 'Vino tinto reserva', 'red_wine', 'Dry red wine', 3.5, 'fl oz', 0.02),
    F(7, 'Zanahoria', 'carrot', 'Carrot', 1.75, 'oz', 0.12),
    F(8, 'Puré de boniato', 'sweet_potato', 'Sweet potato (for purée)', 3.5, 'oz', 0.15,
      nota='Formato de caja de la lista D7 (40 lb case).'),
    F(9, 'Romero fresco (1 rama ≈ 1/12 manojo)', 'rosemary', 'Fresh rosemary (1 sprig ≈ 1/12 bunch)', 0.083,
      'bunch', 0.2),
], None, None, titulo_en='Meat — Pork Cheek Braised in Red Wine', precio_por='menu')
receta('02', '5. Postre', 'fine_dining', 0.30, 0.10, 1, [
    F(5, 'Chocolate negro 70%', 'dark_chocolate', 'Dark chocolate 70%', 60, 'g', 0.05,
      nota='Pastelería: en gramos (8b-A C4).'),
    F(6, 'Fruta de la pasión', 'passion_puree', 'Passion fruit purée', 40, 'g', 0,
      nota='D10: puré 100 % fruta en lugar de fruta fresca. Los 40 g del ES eran pulpa neta (E), así que se '
           'mantienen y la merma pasa a 0 %.'),
    F(7, 'Nata 35% MG', 'heavy_cream', 'Heavy cream (40%)', 2, 'fl oz', 0.03),
    F(8, 'Azúcar', 'sugar', 'Sugar', 25, 'g', 0.02),
    F(9, 'Manteca de cacao', 'cocoa_butter', 'Cocoa butter', 15, 'g', 0.05),
], None, None, precio_por='menu')
MENU02 = OrderedDict([('precio_carta_ref', 115.00),
                      ('fuente', est('Menú degustación de 5 pases en un restaurante de mantel de EE. UU.: 95-150 $ '
                                     'por persona antes de impuestos y propina; se toma 115 $.')),
                      ('tipo_local', 'fine_dining'), ('target_fc', 0.30),
                      ('target_fc_justificacion', 'El ES usa 25 %; D12 fine dining = 30-35 % (research §2.3: el ES '
                                                  'está por debajo de toda fuente). Se sube al 30 %, el suelo del rango. '
                                                  'Sigue siendo el único food cost objetivo del libro (Summary).')])

# --- 03 -------------------------------------------------------------------
receta('03', 'Primer Plato', 'casual', 0.32, 0.10, 1, [
    F(5, 'Lechuga variada', 'spring_mix', 'Spring mix', 3, 'oz', 0.05,
      nota='Mezcla ya lavada: merma 5 % [estimado] en lugar del 25 % de la lechuga entera.'),
    F(6, 'Tomate pera', 'roma_tomato', 'Roma tomato', 3.5, 'oz', 0.1),
    F(7, 'Pepino', 'cucumber', 'Persian cucumber', 2, 'oz', 0.12),
    F(8, 'Cebolla morada', 'red_onion', 'Red onion', 1, 'oz', 0.12),
    F(9, 'Aceitunas negras', 'olives', 'Kalamata olives (pitted)', 0.75, 'oz', 0.02),
    F(10, 'Queso feta', 'feta', 'Feta cheese', 1.5, 'oz', 0.03),
    F(11, 'AOVE', 'evoo', 'EVOO', 4, 'tsp', 0.03),
], None, None, precio_por='menu')
receta('03', 'Segundo Plato', 'casual', 0.32, 0.10, 1, [
    F(5, 'Contramuslo de pollo', 'chicken_thighs', 'Chicken thigh (bone-in)', 9, 'oz', 0.25),
    F(6, 'Patata', 'potato', 'Potato', 7, 'oz', 0.12),
    F(7, 'Pimiento rojo', 'red_pepper', 'Red bell pepper', 2, 'oz', 0.15),
    F(8, 'Ajo', 'garlic', 'Peeled garlic', 0.35, 'oz', 0.03,
      nota='Ajo pelado (el formato con precio de distribuidor): merma 3 % [estimado] en lugar del 15 % de la cabeza.'),
    F(9, 'Romero fresco (1 rama ≈ 1/12 manojo)', 'rosemary', 'Fresh rosemary (1 sprig ≈ 1/12 bunch)', 0.083,
      'bunch', 0.2),
    F(10, 'AOVE', 'evoo', 'EVOO', 0.75, 'fl oz', 0.03),
], None, None, precio_por='menu')
receta('03', 'Postre', 'casual', 0.32, 0.10, 1, [
    F(5, 'Huevo campero', 'eggs', 'Large egg', 0.5, 'each', 0, ud='dozen'),
    F(6, 'Leche entera', 'whole_milk', 'Whole milk', 5, 'fl oz', 0.03),
    F(7, 'Azúcar', 'sugar', 'Sugar', 1.5, 'oz', 0.02),
    F(8, 'Vainilla (extracto)', 'vanilla', 'Vanilla extract', 0.5, 'tsp', 0.05),
    F(9, 'Caramelo líquido', 'caramel', 'Caramel sauce', 0.75, 'tbsp', 0.05,
      nota='Peso → volumen con densidad ≈ 1,3 [estimado]: 15 g ≈ 0,4 fl oz ≈ ¾ tbsp.'),
], None, None, precio_por='menu')
BREAD_BUTTER = r2(2 / 16.0 * 1.823 + 0.5 / 16.0 * (B / 36))
MENU03 = OrderedDict([
    ('precio_carta_ref', 22.00),
    ('fuente', est('Menú de mediodía de tres platos (prix fixe lunch) en un bistró o restaurante casual de EE. UU.: '
                   '22-32 $ antes de impuestos y propina; se toma 22 $, el extremo bajo (24 $ en la F2; con los precios '
                   'de verdura del USDA de la revisión R1 el menú quedaba en el 27,6 %, fuera de D12 casual).')),
    ('tipo_local', 'casual'), ('target_fc', 0.32),
    ('target_fc_justificacion', 'El ES usa 33 %; D12 casual = 28-32 %. Se baja al 32 %, el techo del rango: el menú '
                                'del día es un producto de margen ajustado, como en el ES.'),
    ('extras', OrderedDict([
        ('bread_and_butter', OrderedDict([('rotulo', 'Bread & butter (per guest)'), ('valor', BREAD_BUTTER),
                                          ('fuente', deriv('2 oz de pan (BLS pan blanco 1,823 $/lb) + 0,5 oz de '
                                                           'mantequilla (caja 36x1 lb de la plantilla).',
                                                           bls('APU0000702111')))])),
        ('drink', OrderedDict([('rotulo', 'Drink (if included)'), ('valor', 0),
                               ('nota', 'En EE. UU. la bebida no suele entrar en el menú: 0 por defecto; escribe su '
                                        'coste si la incluyes.')])),
        ('coffee', OrderedDict([('rotulo', 'Coffee (if included)'), ('valor', 0),
                                ('nota', 'Igual que la bebida: 0 por defecto.')])),
    ])),
])

# --- 04 -------------------------------------------------------------------
receta('04', 'Gin Tonic Premium', 'bar', 0.20, 0.05, 1, [
    F(5, 'Ginebra premium', 'gin', 'Premium gin', 1.5, 'fl oz', 0.02, nota='Pour estándar de EE. UU., 1.5 fl oz (NIAAA).'),
    F(6, 'Tónica premium', 'tonic', 'Premium tonic water (6.7 fl oz bottle)', 0.5, 'each', 0,
      cambio='Media botella (≈ 3,4 fl oz), la proporción 1:2-1:3 de un gin & tonic en EE. UU.; el ES ponía la botella entera.'),
    F(7, 'Limón', 'lemon', 'Lemon', 0.25, 'each', 0,
      nota='Por pieza: ¼ de limón (los 20 g netos del ES); merma 0 % por ser unidad (regla de Instrucciones).'),
    F(8, 'Pepino', 'cucumber', 'Persian cucumber', 0.35, 'oz', 0.12),
    F(9, 'Enebro (bayas)', 'juniper', 'Juniper berries', 0.07, 'oz', 0.05),
    F(10, 'Hielo', 'ice', 'Ice', 5, 'oz', 0),
], 14.00, est('Gin & tonic con ginebra premium en un bar de cócteles de EE. UU.: 12-16 $; se toma 14 $.'))
receta('04', 'Mojito Clásico', 'bar', 0.20, 0.05, 1, [
    F(5, 'Ron blanco', 'rum', 'White rum', 2, 'fl oz', 0.02),
    F(6, 'Lima', 'lime', 'Lime', 0.5, 'each', 0, nota='Por pieza: ½ lima (30 g netos del ES); merma 0 %.'),
    F(7, 'Hierbabuena (1 rama ≈ 1/12 manojo)', 'mint', 'Mint (1 sprig ≈ 1/12 bunch)', 0.083, 'bunch', 0.2),
    F(8, 'Azúcar', 'sugar', 'Sugar', 0.5, 'oz', 0.02),
    F(9, 'Soda/agua con gas', 'soda', 'Club soda', 2, 'fl oz', 0),
    F(10, 'Hielo', 'ice', 'Ice', 5, 'oz', 0),
], 10.00, est('Mojito en un bar o restaurante casual de EE. UU.: 10-14 $; se toma 10 $.'))
receta('04', 'Margarita', 'bar', 0.20, 0.05, 1, [
    F(5, 'Tequila reposado', 'tequila', 'Reposado tequila', 1.5, 'fl oz', 0.02),
    F(6, 'Triple Sec / Cointreau', 'triple_sec', 'Triple sec / Cointreau', 0.75, 'fl oz', 0.02),
    F(7, 'Lima (zumo)', 'lime', 'Lime (for juice)', 1, 'each', 0,
      nota='Una lima da ≈ 1 fl oz de zumo; el ES pedía 30 g de zumo con 50 % de merma (60 g de fruta).'),
    F(8, 'Sal (para borde)', 'kosher_salt', 'Kosher salt (for rim)', 0.2, 'oz', 0.5),
    F(9, 'Hielo', 'ice', 'Ice', 3.5, 'oz', 0),
], 14.00, est('Margarita con reposado y Cointreau en un bar de EE. UU.: 12-16 $; se toma 14 $.'))
receta('04', 'Aperol Spritz', 'bar', 0.20, 0.05, 1, [
    F(5, 'Aperol', 'aperol', 'Aperol', 1.5, 'fl oz', 0.02,
      cambio='Pour estándar de 1.5 fl oz (SPEC §2.5 fila 04); el 3-2-1 del ES (2 fl oz) daba un pour cost del 26 % a 15 $.'),
    F(6, 'Prosecco', 'prosecco', 'Prosecco', 3, 'fl oz', 0.05),
    F(7, 'Soda', 'soda', 'Club soda', 1, 'fl oz', 0),
    F(8, 'Naranja (rodaja)', 'orange', 'Orange (slice)', 0.125, 'each', 0,
      nota='Por pieza: una rodaja ≈ ⅛ de naranja; merma 0 %.'),
    F(9, 'Hielo', 'ice', 'Ice', 5, 'oz', 0),
], 15.00, est('Aperol Spritz en un bar de EE. UU.: 13-18 $; se toma 15 $.'))

# --- 05 -------------------------------------------------------------------
receta('05', 'Tarta Chocolate', 'pastry_bakery', 0.25, 0.10, 12, [
    F(5, 'Chocolate negro 70%', 'dark_chocolate', 'Dark chocolate 70%', 400, 'g', 0.05,
      nota='Se funde para la masa, no se templa: merma 5 % [estimado: bol y espátula] en lugar del 12 % de templado '
           '(revisión R1 EN, CHEF-11).'),
    F(6, 'Mantequilla', 'butter', 'Butter', 250, 'g', 0.03, nota='Formato de caja de la lista D7 (36x1 lb case).'),
    F(7, 'Huevos (unidades)', 'eggs', 'Eggs', 6, 'each', 0, nota='Formato de caja de la lista D7 (15 dz case).'),
    F(8, 'Azúcar', 'sugar', 'Sugar', 200, 'g', 0.02, nota='50 lb bag.'),
    F(9, 'Harina floja', 'ap_flour', 'All-purpose flour', 120, 'g', 0.08, nota='50 lb bag (29,99 $, 8b-B §1.7).'),
    F(10, 'Nata 35% MG', 'heavy_cream', 'Heavy cream (40%)', 200, 'ml', 0.03),
    F(11, 'Cacao en polvo', 'cocoa_powder', 'Cocoa powder', 30, 'g', 0.05),
    F(12, 'Sal', 'fine_salt', 'Salt', 3, 'g', 0.02),
], 5.00, est('Porción de tarta de chocolate (1/12 de un molde de 9 in) en una pastelería-café de EE. UU.: 5-7 $; se toma 5 $.'))
receta('05', 'Croissants', 'pastry_bakery', 0.25, 0.10, 20, [
    F(5, 'Harina de fuerza', 'bread_flour', 'Bread flour', 1000, 'g', 0.08,
      cambio='×2: el ES hace 20 piezas de ~50 g de masa (tamaño mini); un croissant de EE. UU. lleva ~100 g.'),
    F(6, 'Mantequilla seca (82% MG)', 'lamination_butter', 'Lamination butter sheets (82% butterfat)', 560, 'g', 0.03,
      cambio='×2 (mismo motivo).'),
    F(7, 'Leche entera', 'whole_milk', 'Whole milk', 300, 'ml', 0.03, ud='4x1 gal case',
      cambio='×2 (mismo motivo).', nota='Formato de caja de la lista D7 (4x1 gal case).'),
    F(8, 'Azúcar', 'sugar', 'Sugar', 120, 'g', 0.02, cambio='×2 (mismo motivo).'),
    F(9, 'Levadura fresca', 'fresh_yeast', 'Fresh yeast', 40, 'g', 0.05, cambio='×2 (mismo motivo).'),
    F(10, 'Sal', 'fine_salt', 'Salt', 20, 'g', 0.02, cambio='×2 (mismo motivo).'),
    F(11, 'Huevo (para pintar)', 'eggs', 'Egg (for egg wash)', 1, 'each', 0,
      nota='El huevo para pintar no escala con la masa: se queda en 1.'),
], 3.50, est('Croissant de mantequilla de tamaño normal en una panadería-café de EE. UU.: 3,25-4,50 $; se toma 3,50 $.'))
PRECIO_VITRINA_MACARON = 2.75   # [estimado] precio de vitrina en EE. UU. (2,50-3,50 $), solo para el texto
receta('05', 'Macarons', 'pastry_bakery', 0.25, 0.10, 30, [
    F(5, 'Harina de almendra', 'almond_flour', 'Almond flour', 150, 'g', 0.02),
    F(6, 'Azúcar glas', 'powdered_sugar', 'Powdered sugar', 150, 'g', 0.02),
    F(7, 'Claras de huevo', 'egg_whites', 'Egg whites', 110, 'g', 0.05),
    F(8, 'Azúcar', 'sugar', 'Sugar', 150, 'g', 0.02),
    F(9, 'Frambuesa congelada', 'raspberries', 'Frozen raspberries', 100, 'g', 0.07),
    F(10, 'Chocolate blanco', 'white_chocolate', 'White chocolate', 80, 'g', 0.05,
      nota='Se funde para la ganache, no se templa: merma 5 % [estimado] en lugar del 12 % (revisión R1 EN, CHEF-11).'),
    F(11, 'Colorante rojo (bote 50 g · 2 g/tanda)', 'food_coloring', 'Red gel food coloring (10.5 oz bottle · 2 g/batch)',
      0.007, 'each', 0, nota='2 g de un bote de 10,5 oz (297,7 g) = 0,0067 → 0,007 botes.'),
], 0.95, est('PRECIO MAYORISTA por pieza (a cafeterías y catering): 0,85-1,25 $. En vitrina un macaron cuesta '
             '2,50-3,50 $ y su food cost cae al ~9 %: el precio paga la mano de obra. Con el precio de vitrina '
             'quedaría fuera del 25-35 % de D12, por eso la referencia es la mayorista, y el libro lo DICE: título '
             '«(wholesale to cafés)» y una línea en Instructions (revisión R1 EN, CHEF-09).'),
    titulo_en='Raspberry Macarons — 30 pieces (wholesale to cafés)',
    nota='La única receta cuyo precio de referencia es mayorista; el título y las Instrucciones lo declaran.')

# --- 06 -------------------------------------------------------------------
receta('06', 'Cocktail (por persona)', 'catering', 0.35, 0.10, 1, [
    F(5, 'Jamón ibérico (loncheado)', 'serrano', 'Serrano ham (carved from the leg)', 1.5, 'oz', 0.5,
      nota='D10: Serrano en lugar de ibérico (ejemplo de la SPEC). Se compra la pata entera (con fuente) y se corta '
           'en el evento: merma 50 % [estimado: hueso, corteza y grasa exterior].'),
    F(6, 'Queso manchego curado', 'manchego', 'Aged Manchego-style cheese', 1.5, 'oz', 0.1),
    F(7, 'Salmón ahumado', 'smoked_salmon', 'Smoked salmon', 1, 'oz', 0.1),
    F(8, 'Langostino cocido', 'shrimp', 'Shrimp 16/20, poached (shrimp cocktail)', 1.75, 'oz', 0.35,
      nota='Gamba cruda sin cabeza, pelada y cocida: 35 % [estimado: cáscara ≈ 15 % + cocción ≈ 20 %], frente al 45 % '
           'del langostino con cabeza del ES.'),
    F(9, 'Croquetas (ud)', 'croquettes', 'Ham croquettes (each)', 3, 'each', 0.05),
    F(10, 'Mini quiche (ud)', 'mini_quiche', 'Mini quiches (each)', 2, 'each', 0.05),
    F(11, 'Pan mini (ud)', 'mini_rolls', 'Mini brioche rolls (each)', 3, 'each', 0.1),
    F(12, 'Fruta variada', 'assorted_fruit', 'Assorted fruit', 2, 'oz', 0.15),
    F(13, 'Bebida (vino + agua)', 'beverage_mix', 'Beverage (house wine + water)', 12, 'fl oz', 0.05),
    F(14, 'Café', 'coffee', 'Coffee', 0.35, 'oz', 0, nota='10 g de café molido por taza.'),
], 48.00, est('Recepción con aperitivos contundentes (heavy hors d\'oeuvres) de un catering de EE. UU.: 35-55 $ por '
              'invitado solo la comida, antes de servicio, personal e impuestos; se toma 48 $.'),
    titulo_en='Spanish-Style Cocktail Reception — Cost per Guest')

# --- 07 -------------------------------------------------------------------
receta('07', 'Tostada Aguacate', 'cafe', 0.28, 0.10, 1, [
    F(5, 'Pan de masa madre (rebanada gruesa)', 'sourdough', 'Sourdough bread (2 thick slices)', 4, 'oz', 0,
      cambio='2 rebanadas (4 oz) en lugar de 1: la ración de una cafetería de EE. UU. a 13 $.'),
    F(6, 'Aguacate Hass (½ pieza)', 'avocado', 'Hass avocado (¾ each)', 0.75, 'each', 0,
      cambio='¾ de aguacate en lugar de 0,4 (misma razón).',
      nota='Por pieza (each→each): merma 0 %, la regla de Instrucciones (revisión R1 EN, CHEF-08).'),
    F(7, 'Huevo campero', 'eggs', 'Eggs', 2, 'each', 0,
      cambio='2 huevos pochados en lugar de 1 (misma razón).', nota='15 dz case.'),
    F(8, 'Tomate cherry', 'cherry_tomato', 'Cherry tomatoes', 1.5, 'oz', 0.05),
    F(9, 'Semillas mix', 'mixed_seeds', 'Mixed seeds', 0.35, 'oz', 0.02),
    F(10, 'AOVE', 'evoo', 'EVOO', 2, 'tsp', 0.03),
    F(11, 'Sal en escamas', 'flaky_salt', 'Flaky sea salt', 0.07, 'oz', 0.02),
], 13.00, est('Avocado toast con huevo pochado en una cafetería de EE. UU.: 11-15 $; se toma 13 $. Con la ración del '
              'ES (1 rebanada, 0,4 aguacate, 1 huevo) el food cost quedaba en el 17 %.'),
    titulo_en='Avocado Toast with Poached Eggs')
receta('07', 'Açaí Bowl', 'cafe', 0.28, 0.10, 1, [
    F(5, 'Açaí congelado', 'acai', 'Frozen açaí (2 packs)', 7, 'oz', 0.07,
      cambio='2 packs de 3,5 oz: la base de un bowl «regular» en EE. UU.; el ES llevaba 100 g (1 pack).'),
    F(6, 'Plátano', 'banana', 'Banana', 4, 'oz', 0.25),
    F(7, 'Leche de avena', 'oat_milk', 'Oat milk', 2.75, 'fl oz', 0.03),
    F(8, 'Granola artesanal', 'granola', 'Granola', 1.5, 'oz', 0.02),
    F(9, 'Arándanos', 'blueberries', 'Blueberries (IQF)', 1, 'oz', 0.05),
    F(10, 'Coco rallado', 'coconut', 'Shredded coconut', 0.35, 'oz', 0.02),
    F(11, 'Miel', 'honey', 'Honey', 0.5, 'oz', 0.03),
], 14.50, est('Açaí bowl en una cafetería de EE. UU.: 12-16 $; se toma 14,50 $.'))
receta('07', 'Eggs Benedict', 'cafe', 0.28, 0.10, 1, [
    F(5, 'English muffin', 'english_muffin', 'English muffin (split)', 1, 'each', 0,
      cambio='1 muffin abierto en dos = 2 bases: el ES contaba 2 unidades.'),
    F(6, 'Huevo campero', 'eggs', 'Eggs', 2, 'each', 0, nota='15 dz case.'),
    F(7, 'Salmón ahumado', 'smoked_salmon', 'Smoked salmon', 2, 'oz', 0.05),
    F(8, 'Mantequilla (hollandaise)', 'butter', 'Butter (hollandaise)', 1.75, 'oz', 0.03),
    F(9, 'Limón', 'lemon', 'Lemon', 0.125, 'each', 0, nota='Por pieza: ⅛ de limón para la holandesa; merma 0 %.'),
    F(10, 'Cebollino (1 rama ≈ 1/12 manojo)', 'chives', 'Chives (1 sprig ≈ 1/12 bunch)', 0.083, 'bunch', 0.2),
], 19.00, est('Eggs Benedict con salmón ahumado en un brunch de EE. UU.: 16-22 $; se toma 19 $.'))
receta('07', 'Carrot Cake', 'cafe', 0.25, 0.10, 12, [
    F(5, 'Zanahoria', 'carrot', 'Carrots', 450, 'g', 0.2, nota='Pastelería: en gramos (8b-A C4).'),
    F(6, 'Harina floja', 'ap_flour', 'All-purpose flour', 300, 'g', 0.02),
    F(7, 'Azúcar moreno', 'brown_sugar', 'Light brown sugar', 280, 'g', 0.02),
    F(8, 'Huevo campero', 'eggs', 'Eggs', 6, 'each', 0),
    F(9, 'Aceite de girasol', 'fryer_oil', 'Canola oil', 220, 'g', 0,
      nota='D10: en EE. UU. el carrot cake se hace con canola (o «vegetable oil»), no con girasol; el mismo aceite '
           'de canola de la plantilla 08. 0,24 L × 0,92 g/ml ≈ 220 g: la pastelería pesa el aceite, y el formato se '
           'vende al peso (revisión R1 EN, CHEF-15).'),
    F(10, 'Nueces peladas', 'walnuts', 'Walnuts', 120, 'g', 0.05),
    F(11, 'Canela molida', 'cinnamon', 'Ground cinnamon', 8, 'g', 0.02),
    F(12, 'Queso crema (frosting)', 'cream_cheese', 'Cream cheese (frosting)', 450, 'g', 0.03),
    F(13, 'Azúcar glas (frosting)', 'powdered_sugar', 'Powdered sugar (frosting)', 200, 'g', 0.02),
    F(14, 'Mantequilla (frosting)', 'butter', 'Butter (frosting)', 120, 'g', 0.03),
], 4.25, est('Porción de carrot cake (1/12 de un molde de 8 in de dos pisos) en una cafetería de EE. UU.: '
             '4,25-6 $; se toma el extremo bajo, 4,25 $, porque la porción es pequeña.'))

# --- 08 -------------------------------------------------------------------
receta('08', 'Smash Burger', 'food_truck', 0.30, 0.10, 1, [
    F(5, 'Carne picada (mezcla 80/20)', 'ground_beef', 'Ground beef (80/20), 2 x 3 oz balls', 6, 'oz', 0),
    F(6, 'Pan brioche', 'brioche_bun', 'Brioche bun', 1, 'each', 0),
    F(7, 'Queso americano', 'american_cheese', 'American cheese (slices)', 2, 'each', 0),
    F(8, 'Cebolla', 'yellow_onion', 'Onion', 1.5, 'oz', 0.12),
    F(9, 'Lechuga', 'iceberg', 'Iceberg lettuce', 0.75, 'oz', 0.25),
    F(10, 'Tomate', 'tomato', 'Tomato', 1, 'oz', 0.1),
    F(11, 'Salsa especial', 'special_sauce', 'Special sauce', 0.75, 'fl oz', 0.05),
    F(12, 'Pepinillo', 'pickles', 'Pickle chips', 0.75, 'oz', 0.02),
], 11.00, est('Doble smash burger con queso en un food truck de EE. UU.: 10-14 $; se toma 11 $.'))
receta('08', 'Loaded Fries', 'food_truck', 0.30, 0.10, 1, [
    F(5, 'Patata para freír', 'potato', 'Potatoes (for fries)', 9, 'oz', 0.12, nota='50 lb bag.'),
    F(6, 'Pulled pork', 'pulled_pork', 'Pulled pork', 3.5, 'oz', 0.1),
    F(7, 'Queso cheddar rallado', 'cheddar', 'Shredded cheddar cheese', 1.5, 'oz', 0.03),
    F(8, 'Salsa BBQ', 'bbq_sauce', 'BBQ sauce', 1, 'fl oz', 0.05, nota='Formato de caja de la lista D7 (4x1 gal case).'),
    F(9, 'Cebollino (1 rama ≈ 1/12 manojo)', 'chives', 'Chives (1 sprig ≈ 1/12 bunch)', 0.083, 'bunch', 0.2),
    F(10, 'Aceite de girasol (fritura)', 'fryer_oil', 'Fryer oil (canola)', 3.25, 'oz', 0,
      nota='Se vende al peso: 0,1 L × 0,92 ≈ 3,25 oz. Las Instrucciones (D20) permiten llevarlo al Q-factor.'),
], 11.00, est('Loaded fries con pulled pork en un food truck de EE. UU.: 10-13 $; se toma 11 $.'))
receta('08', 'Pulled Pork Sándwich', 'food_truck', 0.30, 0.10, 1, [
    F(5, 'Pulled pork', 'pulled_pork', 'Pulled pork', 5.5, 'oz', 0.1),
    F(6, 'Pan brioche grande', 'brioche_bun_large', 'Brioche bun, large', 1, 'each', 0),
    F(7, 'Coleslaw (mix)', 'coleslaw_mix', 'Coleslaw mix', 2, 'oz', 0.1),
    F(8, 'Salsa BBQ', 'bbq_sauce', 'BBQ sauce', 1, 'fl oz', 0.05),
    F(9, 'Pepinillos', 'pickles', 'Pickle chips', 0.75, 'oz', 0.02),
], 15.00, est('Sándwich de pulled pork en un food truck de EE. UU.: 12-15 $; se toma 15 $, el extremo alto, porque '
              'el pulled pork comprado ya cocinado es caro (8,28 $/lb).'))


# ==========================================================================
# 4. Cálculo (el mismo que hacen las fórmulas de la ficha)
# ==========================================================================
def coste_fila(f):
    g = fac(f['ud_compra'], f['ud_uso'])
    ap = f['cantidad'] / (1 - f['merma'])
    return ap * f['precio'] / g, ap


for r in R:
    tot = 0
    for f in r['filas']:
        c, ap = coste_fila(f)
        f['factor'] = g = fac(f['ud_compra'], f['ud_uso'])
        f['cant_ap'] = round(ap, 6)
        f['coste'] = round(c, 6)
        tot += c
    r['coste_ingredientes'] = round(tot, 6)
    r['coste_total'] = round(tot * (1 + r['q_factor']), 6)
    r['coste_racion'] = round(r['coste_total'] / r['raciones'], 6)
    r['pvp_sugerido'] = round(r['coste_racion'] / r['target_fc'], 4)


def menu(libro, meta, extras=0.0):
    rs = [r for r in R if r['libro'] == libro]
    platos = sum(r['coste_racion'] for r in rs)
    total = platos + extras
    fc = total / meta['precio_carta_ref']
    for r in rs:
        # Los pases no se venden sueltos: «Current menu price» del pase queda VACÍO, como en el ES; el precio del
        # menú va en una nota del Summary (revisión R1 EN, CHEF-03, opción A).
        r['precio_carta_ref'] = None
        r['precio_carta_fuente'] = None
    meta['coste_platos'] = round(platos, 4)
    meta['coste_menu'] = round(total, 4)
    meta['fc_implicito'] = round(fc, 4)
    return meta


MENU02 = menu('02', MENU02)
MENU03 = menu('03', MENU03, extras=BREAD_BUTTER)

D12 = OrderedDict([
    ('fine_dining', ('Fine Dining', 0.30, 0.35)), ('casual', ('Casual Dining', 0.28, 0.32)),
    ('fast_casual', ('Fast Casual', 0.27, 0.32)), ('cafe', ('Café', 0.25, 0.30)),
    ('catering', ('Catering', 0.28, 0.35)), ('food_truck', ('Food Truck', 0.28, 0.35)),
    ('hotel_fb', ('Hotel F&B', 0.30, 0.35)), ('pastry_bakery', ('Pastry & Bakery', 0.25, 0.35)),
    ('bar', ('Bar & Cocktails', 0.18, 0.24)), ('delivery', ('Delivery', 0.28, 0.32)),
])
for r in R:
    if r['precio_por'] == 'receta':
        r['fc_implicito'] = round(r['coste_racion'] / r['precio_carta_ref'], 4)
    else:
        r['fc_implicito'] = None           # el food cost se mide a nivel de menú (menu_02 / menu_03)
    lo, hi = D12[r['tipo_local']][1:]
    r['rango_d12'] = [lo, hi]


def _pct1(x):
    return '{:.1f}%'.format(x * 100)


# Nota del Summary (CHEF-03): el precio real del menú y cómo se lee su food cost. Cifras calculadas.
MENU02['nota_resumen'] = OrderedDict([
    ('celda', 'B23'),
    ('texto', 'Example: this menu sells at ${:,.0f} (pre-tax), so its actual food cost is TOTAL MENU COST ÷ {:,.0f} = {}. '
              'Courses aren\'t sold separately, which is why each course leaves "Current menu price" blank.'
              .format(MENU02['precio_carta_ref'], MENU02['precio_carta_ref'], _pct1(MENU02['fc_implicito'])))])
MENU03['nota_resumen'] = OrderedDict([
    ('celda', 'B18'),
    ('texto', 'Example: this prix fixe sells at ${:,.0f} (pre-tax), so its actual food cost is TOTAL PRIX FIXE MENU '
              'COST ÷ {:,.0f} = {}. Dishes aren\'t sold separately, which is why each one leaves "Current menu '
              'price" blank.'.format(MENU03['precio_carta_ref'], MENU03['precio_carta_ref'],
                                     _pct1(MENU03['fc_implicito'])))])

# ==========================================================================
# 5. Bottle Sizes (E3), 06, 08, 09, 10, 11, BONUS
# ==========================================================================
BOTTLE_SIZES = []
fila = 5
for iid, (nom, pb, fu, uso) in BOT.items():
    BOTTLE_SIZES.append(OrderedDict([('fila', fila), ('producto', nom), ('ml', 750), ('precio_botella', pb),
                                     ('precio_litro', round(pb * 1000 / 750, 4)), ('donde', uso), ('id', iid),
                                     ('fuente', C[iid]['fuente'])]))
    fila += 1
BOTTLE_SIZES.append(OrderedDict([
    ('fila', fila), ('producto', 'Draft beer, 1/6 bbl keg (sixtel)'), ('ml', round(KEG_ML, 1)), ('precio_botella', KEG),
    ('precio_litro', round(KEG * 1000 / KEG_ML, 4)), ('donde', '(draft beer — see Instructions)'), ('id', 'keg'),
    ('fuente', est('Barril de 1/6 bbl (5,17 gal = %.1f ml, 27 CFR 25.11) de cerveza artesana: 90-130 $ de '
                   'distribuidor según marca y estado; se toma 110 $.' % KEG_ML))]))

LABOR = OrderedDict([('oews_servers', 17.00), ('fica', 0.0765), ('agencia', 30.0)])
W2 = LABOR['oews_servers'] * (1 + LABOR['fica'])
EVENT = OrderedDict([
    ('C5_invitados', 50), ('C9_invitados_por_camarero', 25), ('C11_horas_camarero', 5),
    ('C12_coste_hora_camarero', 25.0), ('C13_horas_jefe_sala', 6), ('C14_coste_hora_jefe_sala', 35.0),
    ('C17_rentals_por_invitado', 3.50), ('C19_transporte', 150.0), ('C20_montaje', 200.0),
    ('C24_fc_comida', 0.35), ('C25_markup_servicios', 0.20), ('C28_minimo', 1000.0), ('C31_impuesto', 0.0),
    ('C25_rotulo', 'Markup on services (%)'),
    ('C25_nota', 'Uso interno: margen sobre personal, rentals, transporte y montaje. NO es un service charge '
                 '(R2T-04, R2-01); la fórmula no cambia.'),
    ('fuentes', OrderedDict([
        ('C9', 'Ratios del sector (fuente secundaria, 8b-A §4.4): emplatado 1:10-12, buffet 1:20, cóctel con pase 1:25, '
               'barra 1 bartender por 50.'),
        ('C12', '[estimado] 25 $/h = punto medio entre el coste W-2 (OEWS mayo-2025 «food servers, nonrestaurant» '
                '17,00 $ × 1,0765 de FICA = %.2f $, https://www.bls.gov/news.release/ocwage.t01.htm) y la tarifa de '
                'agencia (~30 $/h con mínimo de 4 h, fuente secundaria). «Replace with your own rates».' % W2),
        ('C14', '[estimado] 35 $/h: misma proporción que el ES (22/16 × 25 $ = 34,4 $). Suelo W-2: OEWS supervisores de '
                'F&B 21,19 $ × 1,0765 = 22,81 $; los capitanes de agencia cobran más.'),
        ('C17', '[estimado] vajilla y cubertería básicas desde ~3 $/persona + copa (fuente secundaria, 8b-A §4.4).'),
        ('C19_C20', '[estimado] sin fuente: valores que el usuario sustituye (8b-A §4.4).'),
        ('C28', '[estimado] mínimo de facturación por evento.'),
    ])),
])
BREAKEVEN = OrderedDict([
    ('lineas', [
        OrderedDict([('fila', 6), ('rotulo', 'Commissary & parking'), ('valor', 45.0),
                     ('cuenta', '[estimado] commissary ~1.000 $/mes ÷ 22 días de servicio (rango 500-1.500 $/mes, '
                                'mobilefoodmath.com, fuente secundaria)')]),
        OrderedDict([('fila', 7), ('rotulo', 'Insurance, permits & licenses (daily share)'), ('valor', 25.0),
                     ('cuenta', '[estimado] (5.000 $ de seguro + 1.500 $ de permisos al año) ÷ 260 días')]),
        OrderedDict([('fila', 8), ('rotulo', 'Fuel, propane & generator'), ('valor', 30.0),
                     ('cuenta', '[estimado] generador y propano ~500 $/mes ÷ 22 = 23 $ + desplazamientos')]),
        OrderedDict([('fila', 9), ('rotulo', 'Staff (2 people per shift)'), ('valor', 300.0),
                     ('cuenta', '[estimado] 2 × 8 h × 17 $ × 1,0765 (FICA) = 293 $ → 300 $ (OEWS cooks 17,98 $, '
                                'fast food 15,00 $; M20)')]),
        OrderedDict([('fila', 10), ('rotulo', 'Truck & equipment depreciation'), ('valor', 50.0),
                     ('cuenta', '[estimado] camión equipado 90.000 $ ÷ 7 años ÷ 260 días')]),
        OrderedDict([('fila', 11), ('rotulo', 'Cleaning, water & waste'), ('valor', 15.0),
                     ('cuenta', '[estimado] agua y residuos 5-25 $ por visita si no van con el commissary')]),
    ]),
    ('mix', [0.5, 0.25, 0.25]), ('B25_impuesto', 0.0),
])
BREAKEVEN['total'] = sum(l['valor'] for l in BREAKEVEN['lineas'])

WASTE09 = OrderedDict([
    ('familias_con_ejemplo', [
        OrderedDict([('fila', 5), ('familia', 'Beef & red meat'), ('compra', 2200), ('desperdicio', 88)]),
        OrderedDict([('fila', 7), ('familia', 'Fish'), ('compra', 1400), ('desperdicio', 98)]),
        OrderedDict([('fila', 9), ('familia', 'Leafy greens'), ('compra', 700), ('desperdicio', 43)]),
        OrderedDict([('fila', 12), ('familia', 'Dairy'), ('compra', 550), ('desperdicio', 14)]),
        OrderedDict([('fila', 15), ('familia', 'Bread & pastry'), ('compra', 350), ('desperdicio', 38)]),
    ]),
    ('semanas', [OrderedDict([('fila', 7), ('compra', 5000), ('desperdicio', 238)]),
                 OrderedDict([('fila', 8), ('compra', 4800), ('desperdicio', 194)]),
                 OrderedDict([('fila', 9), ('compra', 5100), ('desperdicio', 179)])]),
    ('objetivo_global', 0.04), ('objetivos_familia', 'Los 16 objetivos mín./típico/máx. del ES se mantienen (lista blanca).'),
    ('fuente', est('Compras semanales de un restaurante de servicio completo de EE. UU. con ~17.000 $ de ventas netas '
                   'por semana a un 30 % de food cost (≈ 5.200 $), repartidas por familia como en el ES. El % de '
                   'desperdicio de cada familia se conserva del ES para que los estados (OK/ALERT) enseñen lo mismo.')),
])
CALC10 = OrderedDict([
    ('C4_coste_racion', 5.50), ('C5_impuesto', 0.0),
    ('C4_fuente', est('Coste por ración de un principal casual de EE. UU.: a 30 % de food cost sale a ~18 $.')),
    ('filas', [OrderedDict([('fila', 9 + i), ('tipo', k), ('rotulo', v[0]), ('fc_min', v[1]), ('fc_max', v[2]),
                            ('comision', 0.25 if k == 'delivery' else 0.0)]) for i, (k, v) in enumerate(D12.items())]),
    ('comision_delivery', 0.25), ('comision_nota', 'UK ≈ 30 %'),
])
DASH11 = OrderedDict([
    ('D3_anio', 2026), ('D4_objetivo', 0.30),
    ('meses', [OrderedDict([('fila', 7), ('stock_ini', 4000), ('compras', 20000), ('stock_fin', 4800), ('ventas', 64000)]),
               OrderedDict([('fila', 8), ('stock_ini', 4800), ('compras', 21600), ('stock_fin', 4400), ('ventas', 60000)]),
               OrderedDict([('fila', 9), ('stock_ini', 4400), ('compras', 20800), ('stock_fin', 5200), ('ventas', 68000)])]),
    ('fuente', est('Restaurante de EE. UU. con 60.000-68.000 $ de ventas netas al mes (~780.000 $ al año). Mismos '
                   'porcentajes que el ES (30,0 %, 36,7 %, 29,4 %; 31,9 % en el total) para que el ejemplo enseñe '
                   'lo mismo: son las cifras del ES × 4, no un cambio de moneda.')),
])

# BONUS: un factor por producto (stock C:E y matriz C5:Q14) → la desviación relativa H/F no cambia (M10).
TEND01 = [f for f in R[0]['filas'] if f['fila'] == 5][0]['cant_ap'] / 16.0          # lb AP por ración (01)
POT01 = [f for f in R[0]['filas'] if f['fila'] == 6][0]['cant_ap'] / 16.0
BUT01 = [f for f in R[0]['filas'] if f['fila'] == 8][0]['cant_ap'] / 16.0
KG_LB = fac('kg', 'lb')
BONUS_ES = [  # (fila, producto ES, ud ES, stock ES (C,D,E), precio ES, id, nombre EN, ud EN, factor)
    (5, 'Solomillo ternera', 'kg', (8, 28, 8.5), 26, 'beef_tenderloin', 'Beef tenderloin (PSMO)', 'lb', TEND01 / 0.22),
    (6, 'Contramuslo pollo', 'kg', None, 4.2, 'chicken_thighs', 'Chicken thighs', 'lb', KG_LB),
    (7, 'Lubina', 'kg', (6, 27, 5), 14, 'branzino', 'Branzino (whole)', 'lb', KG_LB),
    (8, 'Langostino', 'kg', None, 18, 'shrimp', 'Shrimp 16/20', 'lb', KG_LB),
    (9, 'Patata', 'kg', (25, 30, 22), 1.1, 'potato', 'Potatoes', 'lb', POT01 / 0.18),
    (10, 'Tomate', 'kg', (6, 12, 6.5), 2.4, 'tomato', 'Tomatoes', 'lb', KG_LB),
    (11, 'Lechuga', 'kg', (4, 18, 4.5), 1.8, 'spring_mix', 'Spring mix', 'lb', KG_LB),
    (12, 'Mantequilla', 'kg', (3, 2, 2.5), 9, 'butter', 'Butter', 'lb', BUT01 / 0.02),
    (13, 'Aceite oliva', 'L', (10, 5, 11.5), 8.5, 'evoo', 'Extra virgin olive oil', 'L', 1.0),
    (14, 'Vino blanco', 'L', (12, 6, 14), 4.5, 'white_wine', 'Dry white wine', 'L', 1.0),
    (15, 'Harina', 'kg', None, 0.9, 'ap_flour', 'All-purpose flour', 'lb', KG_LB),
    (16, 'Azúcar', 'kg', None, 1.2, 'sugar', 'Sugar', 'lb', KG_LB),
    (17, 'Huevos', 'docena', None, 3.6, 'eggs', 'Eggs', 'dozen', 1.0),
    (18, 'Nata', 'L', None, 2.8, 'heavy_cream', 'Heavy cream', 'qt', fac('L', 'qt')),
    (19, 'Chocolate', 'kg', None, 11, 'dark_chocolate', 'Dark chocolate 70%', 'lb', KG_LB),
]
MATRIZ_ES = {  # plato: (raciones, {producto ES: cantidad ES por ración})
    'Solomillo al Pedro Ximénez': (120, {'Solomillo ternera': 0.22, 'Patata': 0.18, 'Mantequilla': 0.02, 'Vino blanco': 0.03}),
    'Lubina a la plancha': (80, {'Lubina': 0.34, 'Patata': 0.12, 'Aceite oliva': 0.02}),
    'Ensalada de la casa': (150, {'Tomate': 0.07, 'Lechuga': 0.11, 'Aceite oliva': 0.01}),
}
PLATOS_EN = {'Solomillo al Pedro Ximénez': 'Beef Tenderloin with PX Sherry Reduction',
             'Lubina a la plancha': 'Grilled Branzino', 'Ensalada de la casa': 'House Salad'}


def precio_en_ud(iid, ud):
    c = C[iid]
    if ud == c['ud_compra']:
        return c['precio']
    return c['precio'] / fac(c['ud_compra'], ud)   # precio por la unidad del inventario


# Compras en formatos que se compran de verdad en EE. UU. (revisión R1 EN, CHEF-13): cajas enteras donde el producto
# se vende por caja; peso real (catch weight) con 2 decimales donde se factura por peso. El consumo real
# F = C + D − E se conserva (= factor × F del ES, a ±0,005), así que H/F sigue siendo la del ES (M10).
COMPRA_BONUS = {  # producto ES: (compras EN, cómo se compra, decimales del stock inicial)
    'Solomillo ternera': (None, 'catch weight', 2),
    'Lubina': (None, 'catch weight', 2),
    'Patata': (50, '1 × 50 lb bag', 1),
    'Tomate': (25, '1 × 25 lb case', 1),
    'Lechuga': (36, '3 × 12 lb cases (4 x 3 lb)', 1),
    'Mantequilla': (6, '6 × 1 lb blocks', 1),
    'Aceite oliva': (6, '2 × 3 L tins', 1),
    'Vino blanco': (6, '8 × 750 ml bottles', 1),
}
BONUS = OrderedDict([('productos', []), ('platos', [])])
for (fila, nes, ues, st, pes, iid, nen, uen, k) in BONUS_ES:
    d = OrderedDict([('fila', fila), ('producto_es', nes), ('ud_es', ues), ('id', iid), ('producto_en', nen),
                     ('ud_en', uen), ('factor', round(k, 6)),
                     ('precio_unitario', rp(precio_en_ud(iid, uen)))])
    if st:
        compra, como, dec = COMPRA_BONUS[nes]
        consumo = (st[0] + st[1] - st[2]) * k                   # F EN exacto
        c_en = round(st[0] * k, dec)
        d_en = round(st[1] * k, 2) if compra is None else float(compra)
        e_en = round(c_en + d_en - consumo, 2)
        d['stock_ini'], d['compras'], d['stock_fin'] = c_en, d_en, e_en
        d['compras_formato'] = como
        d['consumo_exacto'] = round(consumo, 6)
        d['stock_es'] = list(st)
    BONUS['productos'].append(d)
KF = {p['producto_es']: p['factor'] for p in BONUS['productos']}
for plato, (rac, cant) in MATRIZ_ES.items():
    BONUS['platos'].append(OrderedDict([('plato_es', plato), ('plato_en', PLATOS_EN[plato]), ('raciones', rac),
                                        ('por_racion', OrderedDict((p, round(q * KF[p], 6)) for p, q in cant.items())),
                                        ('por_racion_es', cant)]))
BONUS['anclas_ap_01'] = OrderedDict([('Solomillo ternera', round(TEND01, 4)), ('Patata', round(POT01, 4)),
                                     ('Mantequilla', round(BUT01, 4))])
BONUS['regla'] = ('Un solo factor por producto multiplica el consumo real (F = C + D − E) y la cantidad por ración '
                  '(C5:Q14), así que la desviación relativa H/F es la del ES (M10, a ±0,0005). El factor es la conversión '
                  'kg→lb (o L→L, docena→docena, L→qt) salvo en el solomillo, la patata y la mantequilla, cuya ración del '
                  'plato 1 = la AP qty de la 01 EN (SPEC §2.5, fila BONUS). Las compras (D) van en formatos de compra de '
                  'EE. UU. (cajas enteras o catch weight) y el stock en 1-2 decimales: E se calcula para que F no cambie '
                  '(revisión R1 EN, CHEF-13). Las raciones siguen con 6 decimales.')

# ==========================================================================
# 6. Libro 12
# ==========================================================================
coste_porcion12 = Y12['porcion_oz'] / 16.0 * coste_lb_util
f01 = [f for f in R[0]['filas'] if f['fila'] == 5][0]
LIBRO12 = OrderedDict([
    ('despiece', OrderedDict([
        ('titulo', 'Butcher Yield Test — Whole Beef Tenderloin (PSMO)'),
        ('C5_producto', Y12['producto']),
        ('C8_peso_ap_lb', round(ap_lb, 4)), ('C8_fuente', 'For Love of the Table (ago-2010): «5 pound 9 ounce whole tenderloin» = 89 oz.'),
        ('C9_precio_lb', p_ap), ('C9_fuente', 'El mismo de la 01 EN, fila 5 (USDA AMS 189A).'),
        ('C11_unidades_porcion', 16),
        ('componentes', [OrderedDict([('fila', 14 + i), ('pieza', c[0]), ('tipo', c[1]), ('peso_lb', round(c[2] / 16.0, 4)),
                                      ('oz', c[2]), ('valor_lb', c[3]), ('fuente', c[4])]) for i, c in enumerate(COMP12)]),
        ('C36_porcion_oz', Y12['porcion_oz']),
        ('resultado', OrderedDict([
            ('peso_util_lb', round(util_lb, 4)), ('valor_subproductos', round(subp, 4)),
            ('coste_ap', round(coste_ap, 4)), ('coste_neto_util', round(neto, 4)),
            ('rendimiento_bruto', round(util_lb / ap_lb, 4)), ('coste_lb_util', round(coste_lb_util, 4)),
            ('factor_coste', round(coste_lb_util / p_ap, 4)), ('merma_para_ficha', round(merma12, 6)),
            ('coste_porcion', round(coste_porcion12, 4)), ('porciones_por_pieza', porciones12),
            ('sobra_oz', round(sobra12, 2)), ('perdida_de_corte_lb', 0.0)])),
        ('comprobacion_01', OrderedDict([('merma_fila5_01', f01['merma']), ('coste_fila5_01', round(f01['coste'], 4)),
                                         ('diferencia_rel', round(abs(f01['coste'] - coste_porcion12) / coste_porcion12, 6))])),
    ])),
    ('coccion', OrderedDict([
        ('titulo', 'Cooking Loss Test — Smash Burger (Template 08)'),
        ('C5_elaboracion', '80/20 ground beef, in 3 oz balls'),
        ('C7_peso_crudo_lb', 3.75), ('C7_fuente', '[derivado] 10 hamburguesas × 6 oz de la plantilla 08 EN = 60 oz.'),
        ('C8_precio_lb', C['ground_beef']['precio']),
        ('C9_peso_cocinado_lb', round(3.75 * 0.74, 4)),
        ('C9_fuente', '[derivado] 3,75 lb × 0,74. USDA Food Buying Guide, Section 1: «Beef, Ground, fresh or frozen, no '
                      'more than 20% fat … 1 lb AP = 0.74 lb cooked, drained, lean meat». '
                      'https://foodbuyingguide.fns.usda.gov/files/Reports/USDA_FBG_Section1_MeatsAndMeatAlternatesYieldTable.pdf '
                      '(la misma fuente que el ES). No es una medida.'),
        ('C10_merma_despiece', 0), ('C11_unidades_porcion', 16),
        ('C12_porcion_cocinada_oz', round(6 * 0.74, 2)),
        ('C12_fuente', '[derivado] 6 oz crudos × 0,74 = 4,44 oz: con 2 decimales, la ficha 08 y el test dan el mismo coste.'),
    ])),
])
coc = LIBRO12['coccion']
coc['resultado'] = OrderedDict([
    ('perdida_coccion', round(1 - coc['C9_peso_cocinado_lb'] / coc['C7_peso_crudo_lb'], 4)),
    ('coste_lb_cocinado', round(coc['C8_precio_lb'] / 0.74, 4)),
    ('coste_porcion_cocinada', round(coc['C12_porcion_cocinada_oz'] / 16 * coc['C8_precio_lb'] / 0.74, 4)),
    ('coste_ficha08', round(6 / 16.0 * C['ground_beef']['precio'], 4)),
    ('porciones_tanda', int(math.floor(round(coc['C9_peso_cocinado_lb'] * 16 / coc['C12_porcion_cocinada_oz'], 6)))),
])

# ==========================================================================
# 7. Libro 13 (generado desde las recetas EN, R2-10)
# ==========================================================================
uso = OrderedDict()
for r in R:
    for f in r['filas']:
        uso.setdefault(f['id'], OrderedDict()).setdefault(r['libro'], [])
        if r['hoja_en'] not in uso[f['id']][r['libro']]:
            uso[f['id']][r['libro']].append(r['hoja_en'])
ORDEN_CAT = list(CAT.keys())
DEMO = {'evoo': 7.78, 'beef_tenderloin': 16.90}
filas13 = []
for iid in sorted(uso, key=lambda i: (ORDEN_CAT.index(C[i]['categoria_es']), C[i]['nombre_en'].lower())):
    c = C[iid]
    if c['formato13'] is None:
        continue   # partida compuesta (bebida del cóctel del 06): no se compra a un proveedor
    notas = 'Used in: ' + ' · '.join('%s %s' % (lib, ', '.join('"%s"' % h for h in hs)) for lib, hs in uso[iid].items()) + '.'
    d = OrderedDict([('ingrediente', c['nombre_en']), ('id', iid), ('categoria', c['categoria_en']),
                     ('proveedor', c['proveedor13']), ('formato', c['formato13']['texto']),
                     ('contenido', c['formato13']['contenido']), ('unidad_base', c['formato13']['unidad_base']),
                     ('precio_formato', c['formato13']['precio_formato']),
                     ('precio_unidad_base', round(c['formato13']['precio_formato'] / c['formato13']['contenido'], 4))])
    if iid in DEMO:
        d['precio_anterior'] = DEMO[iid]
        d['variacion'] = round(d['precio_unidad_base'] / DEMO[iid] - 1, 6)
        notas += ' Sample data: the previous price is just an example, so you can see how the alert works. Delete it.'
    d['notas'] = notas
    filas13.append(d)
FILAS_TABLA13 = 154 - 10 + 1          # A10:A154 del ES v2.1 (se conserva por paridad)
LIBRO13 = OrderedDict([
    ('umbral_alerta', 0.05), ('filas_vacias', 30), ('n_ingredientes', len(filas13)), ('filas', filas13),
    ('fechas', 'vacías (R2-10)'),
    ('demo_fuente', est('Precios anteriores ilustrativos para enseñar una ALERT (aceite +10,3 %) y un OK (solomillo '
                        '+1,8 %) con el umbral del 5 %. La fila lo dice en «Notes».')),
    ('proveedores', 'Genéricos, sin marcas (SPEC §2.5 fila 13).'),
])


# ==========================================================================
# 8. Textos con cifra derivada (M5): reescritura EN con la cifra recalculada
# ==========================================================================
def money(x):
    return '${:,.2f}'.format(x)


def pct(x, d=1):
    s = ('{:.%df}' % d).format(x * 100)
    return (s.rstrip('0').rstrip('.') if '.' in s else s) + '%'


gin = BOT['gin'][1]
gin_l = gin / 0.75
g15 = 1.5 / fac('L', 'fl oz') * gin_l
cost_row_gin = [f for f in R if f['hoja_es'] == 'Gin Tonic Premium'][0]['filas'][0]['coste']
ev10 = EVENT
food10 = 10 * [r for r in R if r['libro'] == '06'][0]['coste_racion']
staff10 = math.ceil(10 / ev10['C9_invitados_por_camarero']) * ev10['C11_horas_camarero'] * ev10['C12_coste_hora_camarero'] + \
    ev10['C13_horas_jefe_sala'] * ev10['C14_coste_hora_jefe_sala']
serv10 = staff10 + 10 * ev10['C17_rentals_por_invitado'] + ev10['C19_transporte'] + ev10['C20_montaje']
pvp10 = max(food10 / ev10['C24_fc_comida'] + serv10 * (1 + ev10['C25_markup_servicios']), ev10['C28_minimo'])
pp10 = pvp10 / 10
d12t = {k: '%d-%d%%' % (round(v[1] * 100), round(v[2] * 100)) for k, v in D12.items()}
eggs13 = [f for f in filas13 if f['id'] == 'eggs'][0]
dz = C['eggs']['otras_ud_compra']['dozen']
TAX_US = 0.0753
TXT_TAX_TABLE = ('US: leave 0% — menu prices are pre-tax and sales tax is added to the check (or type your local rate '
                 'to see the price incl. tax). UK: 20% VAT, and menu prices include it. Canada: prices are shown before '
                 'GST/HST (5-15%). Australia: 10% GST, included in menu prices.')
T = []


def txt(es, en, calc, donde=None):
    T.append(OrderedDict([('es', es), ('en', en), ('calculo', calc)] + ([('donde', donde)] if donde else [])))


txt('▸ Tipo de IVA (%): editable. 10 % en hostelería en España; cámbialo si te aplica otro tipo (IGIC en Canarias, o el IVA/ITBIS/IVU de tu país en Latinoamérica).',
    '▸ Tax rate (%): editable, 0% by default. ' + TXT_TAX_TABLE,
    'D6: 0 % por defecto y la tabla por mercado (research §3.1).')
txt('▸ C5 es editable: 10 % en hostelería en España. Cámbialo si te aplica otro tipo (IGIC en Canarias, o el IVA/ITBIS/IVU de tu país en Latinoamérica).',
    '▸ C5 is editable, 0% by default. ' + TXT_TAX_TABLE, 'D6.')
txt('El IVA es una celda: 10 % en hostelería en España; cámbialo si te aplica otro tipo (IGIC en Canarias, o el IVA/ITBIS/IVU de tu país). El «Multiplicador» es 1 ÷ media del rango de food cost: es el número por el que multiplicas el coste para sacar el PVP.',
    'Tax is a single cell, 0% by default: US menu prices are pre-tax; UK 20% VAT, Australia 10% GST (both included in '
    'menu prices); Canada 5-15% GST/HST (added on top). The "Multiplier" is 1 ÷ the average of the food cost range: '
    "it's the number you multiply the cost by to get the menu price.", 'D6.')
txt('▸ «Conversiones»: equivalencias Ud. Compra → Ud. Uso. Va SIN protección: añade las parejas que te falten y corrige el tamaño de los formatos (la botella viene a 70 cl y la lata a 33 cl; si tu vino es de 75 cl, cambia el 70 por 75 en «botella→cl»).',
    '▸ "Conversions": Purchase unit → Recipe unit equivalents. It is NOT protected: add any pairs you\'re missing and fix '
    'the container sizes. The bottle is set to %d ml and the can to %d ml (U.S. sizes); in the UK spirits come in 700 ml '
    'bottles and cans in 330 ml — change the number in "bottle→ml" or "can→ml" and every related row follows.'
    % (mapas.ENVASES['bottle']['ml'], mapas.ENVASES['can']['ml']), 'D7/E3: celdas de tamaño de mapas.ENVASES.')
cost_gin_sheet = g15 / (1 - 0.02)
txt('▸ Las cantidades de destilados van en CL y el precio en €/L: el Factor (columna G) hace la conversión. 5 cl de una ginebra de 28 €/L son 1,40 € de producto (1,43 € en la hoja, porque esa fila lleva además un 2 % de merma de servicio), no 140 €.',
    '▸ Spirit quantities are in FL OZ and the price is per liter: the Factor (column G) does the conversion. 1.5 fl oz of '
    'a %s/liter gin is %s of product (%s on the sheet, because that row also carries a 2%% spillage allowance), not %s.'
    % (money(gin_l), money(g15), money(cost_gin_sheet), money(1.5 * gin_l)),
    '1,5 fl oz ÷ 33,814 × %.4f $/L = %.4f; ÷ 0,98 = %.4f; error típico 1,5 × %.2f.' % (gin_l, g15, cost_gin_sheet, gin_l))
txt('▸ Pestaña «Formatos de Compra»: convierte el precio de la BOTELLA de la factura (70 cl los destilados, 75 cl el vino y el espumoso) en el €/L que pide la columna «Precio/Ud». Es el error que más cuesta: una ginebra de 19,60 € la botella son 28 €/L.',
    '▸ "Bottle Sizes" tab: turns the invoice BOTTLE price (750 ml in the US for spirits, wine and sparkling wine; UK '
    'spirits 700 ml) into the price per liter that the Price/Unit column needs. It\'s the costliest mistake: a %s bottle '
    'of gin is %s per liter.' % (money(gin), money(gin_l)), '%.2f ÷ 0,75.' % gin)
txt('La columna «Precio/Ud (€)» del escandallo pide €/LITRO, pero la factura del proveedor viene por botella. Escribe aquí el formato y lo que pagas por botella, y copia el «Precio por litro» a la columna «Precio/Ud» de la pestaña del cóctel. Los destilados se compran en botella de 70 cl y el vino y el espumoso en 75 cl: teclear el precio de la botella tal cual infravalora el coste un 30 %.',
    'The Price/Unit column on the recipe cost card needs a PRICE PER LITER, but your supplier invoices by the bottle. '
    'Enter the size (in ml) and what you pay per bottle here. The example bottles are already linked to their cocktail '
    'tabs; for bottles you add below, copy Price per Liter into the Price/Unit column of the cocktail tab. In the US '
    'spirits, wine and sparkling wine all come in 750 ml bottles: typing the bottle price '
    'as-is understates the cost by 25% (30% with a UK 700 ml bottle).', '1 − 0,75 = 25 %; 1 − 0,70 = 30 %.')
txt('El «Precio/Ud (€)» de las pestañas de cóctel está ENLAZADO a la columna «Precio por litro» de esta hoja (celdas azules): cambia aquí el precio de la botella y el escandallo se recalcula solo. Una ginebra de 19,60 € la botella de 70 cl son 28 €/L, que es lo que aparece en «Gin Tonic Premium».',
    'The Price/Unit on the cocktail tabs is LINKED to the Price per Liter column on this sheet (blue cells): change the '
    'bottle price here and the recipe cost card recalculates on its own. A %s bottle of gin (750 ml) is %s per liter, '
    'which is what shows up on "Gin & Tonic".' % (money(gin), money(gin_l)), '%.2f ÷ 0,75.' % gin)
txt('▸ Food cost objetivo de referencia en barra: 20-25 %.',
    '▸ Reference pour cost at the bar: %s (spirits 18-20%%, draft beer about 20%%, bottled beer about 25%%, wine higher).'
    % d12t['bar'], 'D12 bar + desglose por categoría (lista blanca).')
txt('▸ Food cost objetivo de referencia en pastelería: 20-30 %.',
    '▸ Reference target food cost for pastry & bakery: %s.' % d12t['pastry_bakery'], 'D12.')
txt('▸ Food cost objetivo de referencia en catering: 30-40 %.',
    '▸ Reference target food cost for catering: %s.' % d12t['catering'], 'D12 (el borrador EN decía 30-40 %).')
txt('▸ Food cost objetivo de referencia en cafetería: 25-30 %.',
    '▸ Reference target food cost for a café: %s.' % d12t['cafe'], 'D12.')
txt('▸ Food cost objetivo de referencia en street food: 28-35 %.',
    '▸ Reference target food cost for a food truck: %s.' % d12t['food_truck'], 'D12.')
txt('El food cost objetivo se aplica SÓLO a la comida (C7 ÷ C24). El personal, el menaje, el transporte y el montaje no llevan food cost: van a coste más el margen de servicios de C25. Aplicar el 35 % al coste total multiplicaba el presupuesto por 2,9 y perdías el evento. C35 te enseña qué food cost de comida te queda sobre el total facturado. Ojo con los eventos pequeños: el transporte, el montaje y el jefe de sala son fijos, así que con 10 comensales el precio por persona se dispara por encima de los 100 €. No es un error de la hoja: es lo que cuesta de verdad mover un catering para diez. Ajusta esas tres celdas verdes a la realidad de tu evento pequeño.',
    'The target food cost applies ONLY to the food (C7 ÷ C24). Staff, rentals, transport and setup carry no food cost: '
    'they go in at cost plus the markup on services in C25. Applying the %s target to the total cost would multiply the '
    'quote by %.1f and lose you the event. C35 shows the food cost left over the total billed (excluding any service '
    'charge). Watch out with small events: transport, setup and the floor manager are fixed, so with 10 guests the price '
    'per guest jumps to about %s. That\'s not a spreadsheet error — it\'s what it really costs to run a catering job for '
    'ten. Adjust those three green cells to fit your small event.'
    % (pct(ev10['C24_fc_comida'], 0), 1 / ev10['C24_fc_comida'], '${:,.0f}'.format(round(pp10 / 10.0) * 10)),
    '1 ÷ 0,35 = 2,9. 10 invitados: comida %.2f ÷ 0,35 + (personal %.0f + rentals %.0f + 150 + 200) × 1,2 = %.2f → %.2f $/invitado.'
    % (food10, staff10, 10 * ev10['C17_rentals_por_invitado'], pvp10, pp10))
txt('Nº de camareros según el Presupuesto (1 por cada 22 pax)',
    'Number of servers per the Event Quote (1 per %d guests)' % ev10['C9_invitados_por_camarero'], 'SPEC §2.5 fila 06.')
txt('▸ Es la fila que más se equivoca todo el mundo. Aplicar el PVP de «Casual Dining» a una carta de Glovo o Uber Eats significa regalar la comisión: con un 30 % de comisión, un plato de 18 € deja 12,60 €.',
    '▸ It\'s the row everyone gets wrong. Using the "Casual Dining" menu price on DoorDash, Uber Eats or Grubhub (UK: '
    'Deliveroo, Just Eat) means giving the commission away: at a %s commission, an $18 dish leaves you %s.'
    % (pct(CALC10['comision_delivery'], 0), money(18 * (1 - CALC10['comision_delivery']))),
    '18 × (1 − 0,25). El plato de 18 $ = C4 5,50 $ × 3,33 (casual).')
txt('▸ Su food cost objetivo (28-32 %) se mide sobre el ingreso NETO, ya descontada la comisión. Un 30 % sobre neto equivale a un ~21 % sobre el PVP bruto: por eso el precio de la carta de delivery sale alto.',
    '▸ Its target food cost (%s) is measured on NET revenue, after the commission. A 30%% food cost on net is about %s '
    'of the gross menu price (%s with a UK 30%% commission) — which is why the delivery menu price comes out high.'
    % (d12t['delivery'], pct(0.30 * (1 - CALC10['comision_delivery'])), pct(0.30 * 0.70)),
    '0,30 × (1 − 0,25) = 22,5 %; 0,30 × 0,70 = 21 %.')
txt('Delivery: la comisión de la plataforma (25-35 %) se descuenta ANTES de calcular el precio, así que el PVP de la carta de delivery sale muy por encima del de sala — es la única forma de que te quede el mismo dinero en el bolsillo. Su food cost objetivo (28-32 %) se mide sobre el INGRESO NETO, no sobre el precio de la carta: un 30 % sobre neto equivale a un ~21 % sobre el PVP bruto, y por eso el precio de delivery sube. Si vendes por tu propia web, pon la comisión a 0 %.',
    'Delivery: the platform commission (15-30%% in the US depending on the plan, about 30%% in the UK; %s by default) '
    'comes off BEFORE the price is calculated, so the delivery menu price ends up well above your dine-in price — it\'s '
    'the only way to keep the same money in your pocket. Its target food cost (%s) is measured on NET revenue, not on '
    'the menu price: 30%% on net is about %s of the gross price, which is why the delivery price goes up. If you sell '
    'through your own website, set the commission to 0%%.'
    % (pct(CALC10['comision_delivery'], 0), d12t['delivery'], pct(0.30 * (1 - CALC10['comision_delivery']))),
    'Comisiones: DoorDash 15/25/30 % (Basic/Plus/Premier), Uber Eats UK 30 % (research §2.3).')
txt('▸ Compras y ventas van SIN IVA. Si tu TPV te da las ventas con IVA incluido, divídelas entre 1,10 (o entre 1 + tu tipo) antes de escribirlas.',
    '▸ Purchases and sales go in NET: no recoverable tax, and food sales without tax, service charges or tips — drinks '
    'are tracked separately, with their own pour cost. If your POS reports sales including tax, divide them by 1 + your '
    'rate (1.20 with UK VAT) before you type them in.', 'D6/D19 (sin el ID de la SPEC: revisión R1 EN, CHEF-05/T2).')
txt('▸ Con las ventas en bruto el food cost sale unos 3 puntos mejor de lo real y te crees que vas bien.',
    '▸ With gross sales (tax included) your food cost looks better than it is: about %s points at a %s sales tax (the US '
    'average) and %s points with 20%% UK VAT — so you think you\'re on track when you\'re not.'
    % ('{:.0f}'.format(round((0.30 - 0.30 / (1 + TAX_US)) * 100)), pct(TAX_US, 1),
       '{:.0f}'.format((0.30 - 0.30 / 1.2) * 100)),
    'FC 30 %%: 30 − 30/1,0753 = %.1f puntos (media de EE. UU. 7,53 %%, Tax Foundation jul-2026); 30 − 30/1,2 = 5 puntos.'
    % ((0.30 - 0.30 / (1 + TAX_US)) * 100))
txt('Food cost = (stock inicial + compras − stock final) ÷ ventas. NO es compras ÷ ventas: una compra fuerte a fin de mes te movería el indicador varios puntos sin que hubiera cambiado nada en la cocina. Todo SIN IVA: si tu TPV te da las ventas con IVA, divídelas entre 1,10 antes de escribirlas.',
    'Food cost = (beginning inventory + purchases − ending inventory) ÷ net food sales. It is NOT purchases ÷ sales: a big '
    'order at the end of the month would move the number several points without anything changing in the kitchen. '
    'Everything NET: purchases without recoverable tax, and food sales only (drinks go in their own pour cost) without '
    'tax, service charges or tips. If your POS reports sales including tax, divide them by 1 + your rate (1.20 with UK '
    'VAT) before you type them in.', 'D6/D19; ventas de comida (revisión R1 EN, CHEF-02).')
res = LIBRO12['despiece']['resultado']
txt('▸ RACIONES POR PIEZA: peso útil × gramos por kilo ÷ porción estándar, redondeado hacia abajo, porque una ración incompleta no se sirve. En el ejemplo, los 2,100 kg útiles dan 10 raciones de 200 g (sobran 100 g): es la cifra para saber cuántas piezas pedir.',
    '▸ PORTIONS PER PIECE: usable weight × ounces per pound ÷ standard portion, rounded down, because you don\'t serve a '
    'partial portion. In the example, the %s lb of usable meat give %d portions of %d oz (%s oz left over): that\'s the '
    'number that tells you how many pieces to order.'
    % ('{:.3f}'.format(res['peso_util_lb']), res['porciones_por_pieza'], Y12['porcion_oz'],
       '{:g}'.format(res['sobra_oz'])),
    '%.3f × 16 ÷ %d = %.2f → %d.' % (res['peso_util_lb'], Y12['porcion_oz'], res['peso_util_lb'] * 16 / Y12['porcion_oz'],
                                     res['porciones_por_pieza']))
cr = coc['resultado']
txt('▸ Raciones de la tanda: peso cocinado × 1.000 ÷ porción cocinada. En el ejemplo, 1,332 × 1.000 ÷ 133 = 10 hamburguesas.',
    '▸ Portions in the batch: cooked weight × 16 ÷ cooked portion. In the example, %s × 16 ÷ %s = %d patties.'
    % ('{:g}'.format(coc['C9_peso_cocinado_lb']), '{:g}'.format(coc['C12_porcion_cocinada_oz']), cr['porciones_tanda']),
    '2,775 × 16 ÷ 4,44 = 10,0.')
txt('▸ Despiece: el solomillo de ternera entero, con cordón, que compra la plantilla 01, a 28,50 €/kg. Es un ejemplo orientativo, no un test pesado: una pieza de 2,8 kg (las enteras pesan entre 2,5 y 3,2 kg) con una merma de limpieza del 25 %, la referencia habitual para el solomillo entero con cordón. El reparto entre el cordón que se aprovecha y lo que se tira, y el valor del cordón, son estimaciones: pon los tuyos.',
    '▸ Butchering: the whole beef tenderloin (PSMO) that Template 01 (Recipe Cost Card) buys, at %s/lb. The '
    'example follows a published weigh-in of a 5 lb 9 oz whole tenderloin: 3 lb 6 oz of center and head for steaks, '
    '6 oz of tips and 5 oz of chain you can use, and 1 lb 8 oz of fat and silverskin (27%% of the piece). The value of '
    'the tips and the chain is an estimate — weigh and price your own.' % money(p_ap), 'libro12.despiece.')
txt('▸ Con ese despiece, la merma del solomillo para la ficha es del 23,5 % (el 25 % de limpieza menos lo que vale el cordón) y no del 20 % genérico de «Carne roja»: es la que lleva ahora la plantilla 01 en la fila del solomillo.',
    '▸ With that yield test, the tenderloin\'s trim loss for the card is %s (the %s you trim off, minus what the tips '
    'and chain are worth), not the generic 20%% for "Beef & red meat": that\'s the figure Template 01 now carries in the '
    'tenderloin row.' % (pct(merma12), pct(1 - res['rendimiento_bruto'])),
    '1 − 17,21 ÷ %.4f = %.4f; pérdida bruta 1 − 54/89 = %.4f.' % (coste_lb_util, merma12, 1 - res['rendimiento_bruto']))
txt('▸ La merma del solomillo (23,5 %) no es la genérica de «Carne roja» (20 %): sale del test de despiece de la plantilla 12 (Test de Rendimiento), que ya descuenta lo que vale el cordón. Mide tu propia merma con la plantilla 12.',
    '▸ The tenderloin\'s trim loss (%s) isn\'t the generic Beef & red meat rate (20%%): it comes from the butcher\'s yield '
    'test of a whole PSMO tenderloin in template 12 (Yield Test), which already credits what the tips and chain are '
    'worth. Measure your own trim loss with template 12.' % pct(merma12), '= libro 12.')
txt('▸ Cocción: la smash burger de la plantilla 08, 10 hamburguesas de 180 g de mezcla 80/20. El peso cocinado aplica el rendimiento de referencia del USDA para picada de vacuno con un 20 % de grasa (0,74 kg cocinados por kg crudo). No es una medida: pesa la tuya, porque la plancha, el grosor y el punto lo cambian.',
    '▸ Cooking: the smash burger from Template 08 (Food Truck), 10 burgers of 6 oz of 80/20 ground beef (two 3 oz '
    'balls each). The cooked weight applies the USDA reference yield for ground beef with no more than 20% fat (0.74 lb '
    'cooked per lb raw). It\'s not a measurement — weigh your own, because the flat-top, the thickness and the doneness '
    'all change it.', 'libro12.coccion.')
txt('▸ La picada se compra lista, así que su merma de despiece es 0 %, y la ficha 08 lleva también un 0 % en esa fila: con los 180 g en crudo cuesta lo mismo en la ficha que aquí.',
    '▸ Ground beef is bought ready to cook, so its butchering trim loss is 0%%, and card 08 also carries 0%% in that row: '
    'at 6 oz raw it costs the same on the card as it does here (%s).' % money(cr['coste_ficha08']),
    '6/16 × 3,33 = 1,2488 = 4,44/16 × 3,33/0,74.')
txt('En crudo y ya limpia: la ficha 01 usa 200 g.', 'Raw and trimmed: card 01 uses %d oz.' % Y12['porcion_oz'], '01 fila 5.')
txt('Ejemplo orientativo, no un test pesado: pieza entera de 2,8 kg con la merma de limpieza del 25 % que se da como referencia para el solomillo entero con cordón. El reparto entre el cordón que se aprovecha y lo que se tira, y el valor del cordón, son estimaciones: pesa el tuyo. Duplica la pestaña para otro test (clic derecho sobre la pestaña → Mover o copiar → Crear una copia).',
    'Example based on a published weigh-in of a 5 lb 9 oz whole tenderloin (For Love of the Table, 2010), not on your '
    'piece. The value of the tips and chain is an estimate: weigh and price your own. Duplicate the tab for another test '
    '(right-click the tab → Move or Copy → Create a copy).', 'libro12.')
txt('Mezcla de vacuno picada 80/20, en bolas de 90 g', '80/20 ground beef, in 3 oz balls', 'libro12.coccion.')
txt('La que sirves: 180 g crudos de la ficha 08 × 0,74.', 'The one you serve: 6 oz raw from card 08 × 0.74.', '6 × 0,74 = 4,44.')
txt('Ejemplo: 10 hamburguesas de la plantilla 08 (180 g de mezcla 80/20 cada una). El peso cocinado aplica el rendimiento de referencia del USDA para picada de vacuno con un 20 % de grasa: 0,74 kg cocinados por kg crudo. No es una medida: pesa el tuyo, porque la plancha, el grosor y el punto lo cambian.',
    'Example: 10 burgers from Template 08 (Food Truck), 6 oz of 80/20 ground beef each. The cooked weight applies the '
    'USDA reference yield for ground beef with no more than 20% fat: 0.74 lb cooked per lb raw. It\'s not a measurement '
    '— weigh your own, because the flat-top, the thickness and the doneness all change it.', 'libro12.coccion.')
txt('▸ Viene cargada con los 115 ingredientes de las recetas de ejemplo del kit (plantillas 01 a 08) y sus precios, más 30 filas vacías al final para lo que te falte. Escribe encima de los ejemplos o vacíalos seleccionando solo las columnas verdes y pulsando Supr: las blancas son fórmulas y la hoja no deja borrarlas.',
    '▸ It comes preloaded with the %d ingredients from the kit\'s example recipes (templates 01 to 08) and their prices, '
    'plus %d blank rows at the end for anything you\'re missing. Type over the examples, or clear them by selecting only '
    'the green columns and pressing Delete: the white ones are formulas and the sheet won\'t let you delete them.'
    % (LIBRO13['n_ingredientes'], FILAS_TABLA13 - LIBRO13['n_ingredientes']),
    'len(libro13.filas); filas libres = %d filas de la tabla (A10:A154) − ingredientes.' % FILAS_TABLA13)
txt('▸ Contenido del formato: cuántas unidades base trae (25 en un saco de 25 kg; 0,7 en una botella de 70 cl si la unidad base es el litro).',
    '▸ Format content: how many base units it holds (50 in a 50 lb bag; 0.75 in a 750 ml bottle if the base unit is the '
    'liter).', 'D7.')
txt('▸ 3. En «Ud. Compra» de la ficha pon la unidad base de la lista. Ejemplo: los huevos camperos se compran por docena en la plantilla 03 (3,60 €/docena); en esta lista van por unidad (0,3000 €/ud). Si pegas 0,30, cambia «Ud. Compra» a «ud».',
    '▸ 3. In "Purchase unit" on the card, put the base unit from the list. Example: eggs are bought by the dozen in '
    'template 03 (%s/dozen); in this list they\'re priced per each (%s/each, from the %s). If you paste %s, change '
    '"Purchase unit" to "each".' % (money(dz), '${:.4f}'.format(eggs13['precio_unidad_base']), eggs13['formato'],
                                    '{:.4f}'.format(eggs13['precio_unidad_base'])),
    '34,08 ÷ 180 = 0,1893; 2,27 ÷ 12 = 0,1892.')
txt('▸ El colorante se escandalla por bote: 2 g de un bote de 50 g = 0,04 botes, no 0,1 «unidades».',
    '▸ Food coloring is costed by the bottle: 2 g from a 10.5 oz (298 g) bottle = 0.007 bottles.',
    '2 ÷ (10,5 × 28,35) = 0,0067.')
TEXTOS = T
TEXTOS_REGLAS = [
    'Notas «Used in… Template 07 uses a different supplier» del 13 ES: en EN no existen, porque cada ingrediente tiene '
    'un único precio (las unidades distintas del mismo producto —docena/caja, gal/caja— salen de la misma base).',
    'Filas de «Conversions» (bottle/can): las regenera mapas.py con sus notas exactas (E1, D7); no se reescriben aquí.',
    'Filas de datos del 13 (formato, contenido, precio, notas): se generan desde libro13.filas (R2-10).',
    'Nombres de ingrediente, títulos de receta sustituidos y valores de las fichas: mandan estas filas sobre textos_en.',
]

LISTA_BLANCA = [
    OrderedDict([('rango', '18-20%'), ('contexto', 'pour cost de destilados'), ('fuente', 'getbackbar.com (research §2.1)')]),
    OrderedDict([('rango', '20%'), ('contexto', 'pour cost de cerveza de barril (≈)'), ('fuente', 'getbackbar.com')]),
    OrderedDict([('rango', '25%'), ('contexto', 'pour cost de cerveza embotellada (≈)'), ('fuente', 'getbackbar.com')]),
    OrderedDict([('rango', '60-65%'), ('contexto', 'prime cost objetivo (NRA)'), ('fuente', '8b-A §4.1')]),
    OrderedDict([('rango', '65%'), ('contexto', 'prime cost < 65 % de ventas'), ('fuente', 'research §2.1')]),
    OrderedDict([('rango', '15-30%'), ('contexto', 'comisión de plataformas de delivery en EE. UU. por plan'), ('fuente', 'research §2.3')]),
    OrderedDict([('rango', '25%'), ('contexto', 'comisión de delivery por defecto (D12)'), ('fuente', 'D12')]),
    OrderedDict([('rango', '30%'), ('contexto', 'comisión de delivery en UK (≈)'), ('fuente', 'D12')]),
    OrderedDict([('rango', '18-22%'), ('contexto', 'service charge de catering en EE. UU.'), ('fuente', '8b-A §2.1')]),
    OrderedDict([('rango', '12.5%'), ('contexto', 'service charge discrecional en UK'), ('fuente', '8b-A §2.1')]),
    OrderedDict([('rango', '2-3% · 3-5% · 5-8% · 1-2% · 5-10%'), ('contexto', 'objetivos de desperdicio del 09 (y los 16 mín./típico/máx.)'), ('fuente', 'ES 09, se mantienen')]),
    OrderedDict([('rango', '4%'), ('contexto', 'objetivo global de desperdicio del 09'), ('fuente', 'ES 09')]),
    OrderedDict([('rango', '20% · 25% · 35% · 45% …'), ('contexto', 'tabla «Trim Loss Factors» (21 categorías, típica/mín./máx.)'), ('fuente', 'ES Mermas')]),
    OrderedDict([('rango', '12% · 8%'), ('contexto', 'mermas de obrador del 05 (cobertura, harinas)'), ('fuente', 'ES 05')]),
    OrderedDict([('rango', '%s · %s · 27%% · 60.7%%' % (pct(merma12), pct(1 - res['rendimiento_bruto']))), ('contexto', 'rendimientos y mermas del libro 12'), ('fuente', 'libro12')]),
    OrderedDict([('rango', '26%'), ('contexto', 'pérdida por cocción de la smash burger (1 − 0,74)'), ('fuente', 'USDA FBG')]),
    OrderedDict([('rango', '29.6% · 28.5% · 30.6% · 35.1-36.4%'), ('contexto', 'food cost de cadenas cotizadas (Chipotle, Shake Shack, Darden, Texas Roadhouse)'), ('fuente', '8b-A §4.1')]),
    OrderedDict([('rango', '30/30/30/10'), ('contexto', 'regla de reparto de costes (con su matiz)'), ('fuente', '8b-A §4.1')]),
    OrderedDict([('rango', '1:10-12 · 1:20 · 1:25 · 1:50'), ('contexto', 'ratios de personal de catering'), ('fuente', '8b-A §4.4')]),
    OrderedDict([('rango', '5%'), ('contexto', 'umbral de alerta del 13 y «Spillage & ice allowance» del 04'), ('fuente', 'SPEC')]),
    OrderedDict([('rango', '10%'), ('contexto', 'Q-factor por defecto y menaje de repuesto del 06'), ('fuente', 'SPEC D8 / ES')]),
    OrderedDict([('rango', '20%'), ('contexto', 'VAT del Reino Unido; «Markup on services» del 06'), ('fuente', 'D6 / §2.5')]),
    OrderedDict([('rango', '10%'), ('contexto', 'GST de Australia'), ('fuente', 'D6')]),
    OrderedDict([('rango', '5-15%'), ('contexto', 'GST/HST de Canadá'), ('fuente', 'D6')]),
    OrderedDict([('rango', '7.5% · 7.53%'), ('contexto', 'sales tax medio de EE. UU. (Tax Foundation)'), ('fuente', 'research §3.1')]),
    OrderedDict([('rango', '+9.8% · −30.8% · +3.6%'), ('contexto', 'inflación USDA ERS 2026 (vacuno, huevos, fuera de casa)'), ('fuente', '8b-A §4.2')]),
]

# ==========================================================================
# 9. Salida
# ==========================================================================
OUT = OrderedDict([
    ('_leeme', [
        'Datos de mercado del Food Cost Kit Pro (EN), SPEC D5-D7, D10-D12, D19-D20, §2.1, §2.5. Lo genera '
        'generar_mercado.py (no se edita a mano) y lo valida validar_mercado.py. Sesión Claude Code, ' + FECHA + '.',
        'Precios en USD por UNIDAD DE COMPRA de la ficha (D5: en los xlsx sin símbolo). Cada precio lleva su fuente o '
        '[estimado]/[derivado] con el razonamiento. Ningún precio de ingrediente se ha tocado para cuadrar un porcentaje '
        '(D11): donde el food cost caía fuera de D12 se corrigió la CANTIDAD (con «cambio_cantidad») o el precio de carta '
        'de referencia ([estimado]).',
        'Las cantidades EN son la conversión del ES redondeada a cifras de cocina (oz, fl oz, tsp/tbsp, each; gramos y '
        'ml en pastelería). Las mermas son las del ES salvo donde cambia el formato de compra (nota en la fila).',
        'aplicar_en.py escribe desde aquí: filas de las fichas (A-F y H), «Current menu price» (D10), Bottle Sizes (E3), '
        'valores por defecto de 03/06/08/09/10/11, el BONUS, los libros 12 y 13, y los textos con cifra derivada.',
    ]),
    ('fecha', FECHA),
    ('d12', OrderedDict((k, OrderedDict([('rotulo', v[0]), ('min', v[1]), ('max', v[2])])) for k, v in D12.items())),
    ('catalogo', C),
    ('recetas', R),
    ('menu_02', MENU02),
    ('menu_03', MENU03),
    ('bottle_sizes', BOTTLE_SIZES),
    ('catering_06', EVENT),
    ('break_even_08', BREAKEVEN),
    ('waste_09', WASTE09),
    ('calculadora_10', CALC10),
    ('dashboard_11', DASH11),
    ('bonus', BONUS),
    ('libro12', LIBRO12),
    ('libro13', LIBRO13),
    ('textos_cifra_derivada', TEXTOS),
    ('textos_reglas', TEXTOS_REGLAS),
    ('lista_blanca_rangos', LISTA_BLANCA),
])


def resumen():
    n_src = n_est = 0
    for c in C.values():
        t = c['fuente']['tipo']
        if t in ('[estimado]',):
            n_est += 1
        else:
            n_src += 1
    print('catálogo: %d ingredientes · con fuente/derivado %d · [estimado] %d' % (len(C), n_src, n_est))
    for r in R:
        if r['precio_carta_ref'] is None:
            print('  %s %-24s coste/ración %8.4f · pase de menú (sin precio propio)' % (
                r['libro'], r['hoja_en'], r['coste_racion']))
            continue
        print('  %s %-24s coste/ración %8.4f · ref %7.2f · FC %5.1f%% · D12 %s-%s%%%s' % (
            r['libro'], r['hoja_en'], r['coste_racion'], r['precio_carta_ref'], r['fc_implicito'] * 100,
            int(r['rango_d12'][0] * 100), int(r['rango_d12'][1] * 100),
            '' if r['rango_d12'][0] <= r['fc_implicito'] <= r['rango_d12'][1] else '  <<< FUERA'))
    print('  menú 02: coste %.2f / %.2f → %.1f%% · menú 03: coste %.2f / %.2f → %.1f%%' % (
        MENU02['coste_menu'], MENU02['precio_carta_ref'], MENU02['fc_implicito'] * 100,
        MENU03['coste_menu'], MENU03['precio_carta_ref'], MENU03['fc_implicito'] * 100))
    print('  libro 12: merma %.4f · coste porción %.4f · 01 fila 5 %.4f · porciones %d' % (
        merma12, coste_porcion12, f01['coste'], porciones12))
    print('  libro 13: %d ingredientes · break-even 08: %.0f $/día · 10 invitados: %.2f $/invitado' % (
        LIBRO13['n_ingredientes'], BREAKEVEN['total'], pp10))


if __name__ == '__main__':
    resumen()
    if '--stdout' not in sys.argv:
        with open(SALIDA, 'w', encoding='utf-8') as fh:
            json.dump(OUT, fh, ensure_ascii=False, indent=1)
        print('escrito', os.path.relpath(SALIDA, AQUI))
