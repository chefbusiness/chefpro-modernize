#!/usr/bin/env python3
"""
datos_rp.py — Restaurant + Bakery Business Plan Kit (EN) · los datos ES→EN que dependen del contenido de los libros
(FIJOS D34-D36, pistas por celda, tokens del docx D43, fijos del docx D44, fórmulas con texto, caso US). Lo llama
`mapas_rp.instalar()` con el módulo `mapas` YA cargado con los datos de FT/CAF, de los que parte (FIJOS comunes,
redacción de FORMULAS_EN, TOKENS_DOCX). Sesión Claude Code, 4-oct-2026 (F2 tanda 1).
"""
import json
import os
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))

URL_REST = 'aichef.pro/en/digital-products/restaurant-business-plan'

# ==========================================================================
# FIJOS (por TEXTO ES, en cualquier celda de los 4 libros). Parten de los de FT/CAF (los comunes del motor 2.2).
# ==========================================================================
FIJOS_NUEVOS = OrderedDict([
    # I5: Instrucciones!A3 del checklist con el nombre comercial
    ('Este fichero forma parte del producto «plan-negocio-bar-restaurante» de AI Chef Pro.',
     'This file is part of the Restaurant Business Plan Kit by AI Chef Pro.'),
    ('Este fichero forma parte del producto «plan-negocio-panaderia» de AI Chef Pro.',
     'This file is part of the Bakery Business Plan Kit by AI Chef Pro.'),
    # D34: marca ChefBusiness DENTRO del xlsx del restaurante → AI Chef Pro; títulos A2/A3 sin «España 2026»
    ('ChefBusiness Consultoría Gastronómica', 'AI Chef Pro'),
    ('ChefBusiness.co — Plan de Negocio: Bar-Restaurante', 'AI Chef Pro · ' + URL_REST),
    ('Plan de Negocio: Bar-Restaurante / Restaurante Casual — España 2026',
     'Restaurant Business Plan: Casual Restaurant & Bar — US example (2026)'),
    ('Inversión Inicial — Bar-Restaurante', 'Startup Costs — Restaurant & Bar'),
    ('Cuenta de Resultados Previsional — 3 Años', '3-Year Projected P&L'),
    ('Punto de Equilibrio (Break-Even) — Bar-Restaurante', 'Break-Even Analysis — Restaurant & Bar'),
    ('Análisis de Escenarios — Año 1', 'Scenario Analysis — Year 1'),
    ('NOTA: Todos los importes son estimaciones basadas en precios de mercado en España 2026. Ajusta cada partida a '
     'tu situación real.', 'NOTE: all amounts are US kit-example estimates (2026); replace them with your own quotes.'),
    # D36 (E3): la col. H del P&L de la panadería es la parte EXENTA del sales tax
    ('Pan común sobre la línea (%)', 'Tax-exempt share of the line (%)'),
])
FIJOS_FUERA = ('Este fichero forma parte del producto «plan-negocio-food-truck» de AI Chef Pro.',
               'Este fichero forma parte del producto «plan-negocio-cafeteria» de AI Chef Pro.')

# ==========================================================================
# Tokens del docx (D43): los de FT/CAF con los rótulos del restaurante («Cubiertos…») y de la panadería
# («Transacciones…»), más las partidas de inversión propias
# ==========================================================================
_CLIENTES = OrderedDict([
    ('Clientes/día (media del año 1)', ('Cubiertos/día (media del año 1)', 'Transacciones/día (media del año 1)')),
    ('Clientes/día (media)', ('Cubiertos/día (media)', 'Transacciones/día (media)')),
    ('Clientes/día', ('Cubiertos/día', 'Transacciones/día')),
    ('Clientes necesarios al día', ('Cubiertos necesarios al día', 'Transacciones necesarias al día')),
    ('Clientes necesarios al día (caja)', ('Cubiertos necesarios al día (caja)', 'Transacciones necesarias al día (caja)')),
])
_DESC = OrderedDict([
    ('clientes_dia', 'average covers (restaurant) or transactions (bakery) per day, year 1'),
    ('clientes_a2', 'average covers / transactions per day, year 2'),
    ('clientes_a3', 'average covers / transactions per day, year 3'),
    ('equilibrio_clientes_dia', 'break-even covers / transactions per day (accounting)'),
    ('equilibrio_caja_clientes_dia', 'cash break-even covers / transactions per day (loan payments in, depreciation out)'),
    ('pesimista_clientes', 'pessimistic scenario: covers / transactions per day'),
    ('optimista_clientes', 'optimistic scenario: covers / transactions per day'),
    ('alquiler_mes', 'rent per month (base rent of the premises)'),
    ('vida_obra', 'useful life of build-out, years'),
    ('ocupacion_anual', 'rent per year (occupancy)'),
])
_SOLO_FTCAF = ('inv_vehiculo', 'inv_adaptacion', 'inv_equipo_cocina', 'inv_generador', 'inv_permisos', 'inv_obra',
               'inv_instalaciones', 'inv_espresso', 'inv_mobiliario', 'inv_barra', 'inv_terraza', 'inv_lanzamiento',
               'inv_stock', 'aforo', 'rotaciones_dia')
_I, _S = 'Inversión Inicial', '0. Supuestos'
TOKENS_PROPIOS = OrderedDict([
    ('inv_lanzamiento', ('usd', ('fila', _I, {'rest': 'Campaña lanzamiento RRSS + inauguración'}, 'B'),
                         'grand opening / launch marketing budget')),
    ('inv_stock', ('usd', ('fila', _I, {'rest': 'Primera compra de despensa y cámaras',
                                        'pan': 'Stock inicial (harinas, levaduras, etc.)'}, 'B'),
                   'opening food inventory (bakery: flour, yeast and other ingredients)')),
    ('inv_stock_barra', ('usd', ('fila', _I, {'rest': 'Primera compra de bodega y barra'}, 'B'),
                         'opening bar inventory (wine, beer, spirits)')),
    ('inv_obra', ('usd', ('fila', _I, {'rest': 'Obra civil y reforma local'}, 'B'), 'build-out of the premises')),
    ('inv_cocina', ('usd', ('fila', _I, {'rest': 'Cocina industrial (fuegos + plancha)'}, 'B'),
                    'cooking line (range + griddle)')),
    ('inv_campana', ('usd', ('fila', _I, {'rest': 'Campana extractora + motor'}, 'B'),
                     'Type I hood with UL 300 fire suppression')),
    ('inv_barra', ('usd', ('fila', _I, {'rest': 'Barra de bar (fabricación + instalación)'}, 'B'), 'bar (build and install)')),
    ('inv_sala', ('usd', ('fila', _I, {'rest': 'Mesas y sillas (12 mesas x 4 sillas)'}, 'B'), 'dining tables and chairs')),
    ('inv_licencias', ('usd', ('fila', _I, {'rest': 'Licencias y permisos varios'}, 'B'),
                       'liquor license and permits (non-quota state example)')),
    ('inv_horno', ('usd', ('fila', _I, {'pan': 'Horno de pisos / rotativo profesional'}, 'B'), 'deck / rack oven')),
    ('inv_amasadora', ('usd', ('fila', _I, {'pan': 'Amasadora espiral (25-50 kg)'}, 'B'), 'spiral mixer')),
    ('inv_fermentacion', ('usd', ('fila', _I, {'pan': 'Cámara de fermentación controlada'}, 'B'),
                          'proofer / retarder (controlled fermentation cabinet)')),
    ('inv_vitrina', ('usd', ('fila', _I, {'pan': 'Vitrina expositor + mostrador'}, 'B'), 'display case and counter')),
    ('inv_electricidad', ('usd', ('fila', _I, {'pan': 'Instalación eléctrica (potencia 30-40 kW)'}, 'B'),
                          'electrical service upgrade for the ovens')),
    ('aforo', ('int', ('fila', _S, {'rest': 'Aforo del local (plazas sentadas + barra)'}, 'B'), 'seats (tables + bar)')),
    ('rotaciones_dia', ('dec1', ('fila', _S, {'rest': 'Rotaciones al día implícitas (calculado)'}, 'B'),
                        'implied seat turns per day')),
])


def tokens_rp(base):
    out = OrderedDict()
    for t, (fmt, src, desc) in base.items():
        if t in _SOLO_FTCAF:
            continue
        if src[0] == 'fila':
            _, hoja, rot, col = src
            if isinstance(rot, dict):                     # ocupación: el rótulo de la cafetería es el del motor común
                rot = rot['caf']
                rot = {'rest': rot, 'pan': rot}
            elif rot in _CLIENTES:
                rot = {'rest': _CLIENTES[rot][0], 'pan': _CLIENTES[rot][1]}
            elif t == 'marketing_anual':
                rot = {'rest': rot, 'pan': 'Marketing'}
            src = ('fila', hoja, rot, col)
        out[t] = (fmt, src, _DESC.get(t, desc))
    out.update(TOKENS_PROPIOS)
    return out


# ==========================================================================
# Docx: lo que escribe ensamblar_docx.py (portada, aviso, índice, encabezados, cierre — D22, D23, D44)
# ==========================================================================
def docx_fijos(M):
    pc = M.PRODUCTOS_CIERRE
    comun = OrderedDict([(6, 'BUSINESS PLAN'), (14, 'AI Chef Pro'), (15, 'aichef.pro'),
                         (16, 'US edition with UK notes · 2026'), (18, 'LEGAL NOTICE'), (19, M.AVISO_DOCX_EN),
                         (20, '© 2026 AI Chef Pro — aichef.pro'), (22, 'CONTENTS')])
    rest = OrderedDict(comun)
    rest.update([
        (7, 'Restaurant & Bar'),
        (9, 'Complete financial plan, market analysis,\noperations strategy and opening checklist\nto open a casual '
            'restaurant with a bar in the United States'),
        (35, 'Appendices: Restaurant Financial Projections (Excel) + Restaurant Opening Checklist (Excel)'),
        (137, 'AI Chef Pro'), (138, 'Templates and AI tools for food businesses'),
        (140, 'Built on more than 29 years in professional kitchens and restaurant consulting.\nAI agents, templates '
              'and digital products for restaurants, cafes, bars and bakeries.\n\naichef.pro\ninfo@aichef.pro'),
        (142, 'Complete this plan with our digital products:'),
        (143, '→ ' + pc[0]), (144, '→ ' + pc[1]), (145, '→ ' + pc[2]), (146, '→ ' + pc[3]), (147, '\n' + M.URL_TIENDA),
    ])
    pan = OrderedDict(comun)
    pan.update([
        (7, 'Bakery'),
        (9, 'Complete financial plan, market analysis,\noperations strategy and opening checklist\nto open a retail '
            'and wholesale bakery in the United States'),
        (35, 'Appendices: Bakery Financial Projections (Excel) + Bakery Opening Checklist (Excel)'),
        (124, 'AI Chef Pro'), (125, 'Templates and AI tools for food businesses'), (127, 'aichef.pro\ninfo@aichef.pro'),
        (128, '→ %s · %s' % tuple(pc[:2])), (129, '→ %s · %s' % tuple(pc[2:])), (130, '\n' + M.URL_TIENDA),
    ])
    return OrderedDict([('rest', OrderedDict(sorted(rest.items()))), ('pan', OrderedDict(sorted(pan.items())))])


# Notas por párrafo para los traductores (D44 §9; las repite el brief)
DOCX_NOTAS = OrderedDict([
    ('rest', OrderedDict([
        (115, 'D44 §9 1/8: el marco US por niveles (federal, estatal, condado, ciudad): qué regula cada uno; LLC vs '
              'sole proprietorship (Secretary of State, operating agreement) + EIN gratis en el IRS. Fuente: sba.gov'),
        (116, "§9 2/8: health department plan review ANTES de la obra → food establishment permit + inspección previa; "
              "seller's permit / sales tax registration y business license de la ciudad (sustituye el certificado de "
              'denominación y la constitución en notaría)'),
        (117, '§9 3/8: zoning check antes de firmar el lease + building, electrical, plumbing y gas permits con sus '
              'inspecciones → certificate of occupancy (sustituye la licencia de actividad clasificada)'),
        (118, '§9 4/8: cocina: campana Type I con supresión UL 300 (NFPA 96), separador de grasas (grease interceptor) '
              'según el código de fontanería local, inspección del fire marshal; sidewalk café permit si hay terraza '
              '(sustituye la licencia de terraza)'),
        (119, '§9 5/8: LIQUOR LICENSE: licencia estatal (ABC) + aprobación local; en estados con cupo se compra una '
              'licencia existente y el coste cambia un orden de magnitud (el libro presupuesta {{inv_licencias}} como '
              'ejemplo de estado sin cupo); plazos de meses; liquor liability en el seguro; formación de servicio '
              'responsable (TIPS / ServSafe Alcohol) y cartel de edad. Sustituye el párrafo del RGSEAA'),
        (120, '§9 6/8: empleo: I-9, W-4, new-hire reporting, carteles laborales, workers\' comp; salario mínimo federal y '
              'estatal; propinas: el libro NO modela tip credit (servers a ≥ $15/h); federal $2.13/h + tip credit '
              'donde el estado lo permite; CA, OR, WA, AK, MN, MT y NV no lo permiten (DOL). Sustituye el RGPD'),
        (121, '§9 7/8: seguridad alimentaria y seguros: Certified Food Protection Manager + food handler cards, FDA Food '
              'Code adoptado por el estado, 9 alérgenos mayores y consumer advisory en la carta (crudo / poco hecho); '
              'general liability + liquor liability + property + workers\' comp (el libro presupuesta {{seguros_anual}})'),
        (122, '§9 8/8: plazos (de 4 a 8 meses hasta abrir, el más largo suele ser la licencia de alcohol o el plan '
              'review) y, como ÚLTIMA frase o frases, la nota UK: premises licence + personal licence para el alcohol '
              '(Licensing Act 2003), registro del negocio de alimentos en el council 28 días antes de abrir, Food Hygiene '
              'Rating (FHIS en Escocia), VAT 20 % en el local, 14 alérgenos'),
    ])),
    ('pan', OrderedDict([
        (106, 'D44 §9 1/5: obrador COMERCIAL frente a cottage food (D39): las cottage food laws permiten vender desde '
              'casa productos de bajo riesgo con topes de ventas; este plan es una panadería comercial con tienda y '
              'mayorista → licencia de cocina comercial del health department o del departamento de agricultura '
              'según el estado; LLC + EIN + business license (sustituye la licencia de actividad clasificada)'),
        (107, '§9 2/5: plan review e inspección antes de abrir; zoning (retail bakery / light food manufacturing) → '
              'certificate of occupancy; ventilación del obrador y gas de los hornos con sus permisos; ampliación del '
              'servicio eléctrico (trifásico) con la compañía (sustituye el RGSEAA y la salida de humos)'),
        (108, "§9 3/5: sales tax: en muchos estados la bollería para llevar está exenta y el consumo en el local tributa "
              '(p. ej. California y su regla 80/80 — «check your state»); la venta a un café que revende va con resale '
              'certificate; el libro modela la parte exenta en la línea de pan (sustituye el horno y su instalación)'),
        (109, '§9 4/5: mayorista: FDA food facility registration solo si lo mayorista domina (las panaderías con venta '
              'mayoritaria al consumidor suelen estar exentas como retail food establishment); etiquetado de producto '
              'envasado (ingredientes, 9 alérgenos mayores, peso neto); Certified Food Protection Manager + food '
              'handler cards (sustituye el APPCC)'),
        (110, '§9 5/5: seguros (general liability, product liability para el mayorista, property, workers\' comp; el libro '
              'presupuesta {{seguros_anual}}) y, como ÚLTIMA frase o frases, la nota UK: la mayoría del pan y la bollería '
              'para llevar es zero-rated en VAT y el consumo en el local va al 20 %; registro del negocio de alimentos en '
              'el council 28 días antes de abrir; 14 alérgenos; Food Hygiene Rating'),
    ])),
])
DOCX_NOTAS_PLAN = OrderedDict([
    ('rest', 'Concepto (D30): restaurante casual con barra, unas 60 plazas, servicio de comida y cena y barra con '
             'alcohol (no es un bar de copas). En el EN se habla de «covers» (cubiertos) y de «guests», nunca de '
             '«customers» para el volumen diario. Las cifras del docx ES (133.000 €, 350.000 €, 40 cubiertos a 22 €, '
             'préstamo de 80.000 € con ICO, retorno en 30-40 meses) CONTRADICEN al Excel (I1-R): no se traducen; cada '
             'cifra del plan va con su token {{…}}. El cierre (productos) lo escribe el ensamblador'),
    ('pan', 'Concepto (D30): panadería artesana con tienda, un pequeño rincón de café y venta mayorista a cafés '
            '(«artisan bakery with a storefront, a small café corner and wholesale to cafés»). Volumen diario = '
            '«transactions». Lo mayorista va DENTRO de la línea de pan (no es un canal modelado aparte) y los escenarios '
            'mueven transacciones, ticket y días, no el mix (R8). Las cifras del docx ES (105.000 €, 200.000 €, 110 '
            'transacciones a 5 €, equilibrio en 114 a 4,5 €, 4-5 personas, retorno en 24-36 meses, mayorista 40 % / '
            '25-35 %) CONTRADICEN al Excel (I1-P): no se traducen; cada cifra va con su token {{…}}. Sin leasing de '
            'horno (R7)'),
])


def completar(M):
    fijos = OrderedDict((k, v) for k, v in M.FIJOS.items() if k not in FIJOS_FUERA)
    fijos.update(FIJOS_NUEVOS)
    M.FIJOS = fijos
    M.POR_CELDA = OrderedDict()
    M.TOKENS_DOCX = tokens_rp(M.TOKENS_DOCX)
    M.DOCX_FIJOS = docx_fijos(M)
    M.DOCX_NOTAS = DOCX_NOTAS
    M.DOCX_NOTAS_PLAN = DOCX_NOTAS_PLAN
    M.FORMULAS_EN = OrderedDict()
    M.VALORES_EN = OrderedDict()
    M.CALIBRACION_D15 = OrderedDict()
    M.CELDA_PISTAS = OrderedDict()
