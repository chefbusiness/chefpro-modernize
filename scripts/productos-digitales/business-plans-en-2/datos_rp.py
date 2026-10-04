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
    ('Cuadro de Personal y Coste Laboral', 'Staffing Plan & Labor Cost'),
    ('Checklist Apertura — Bar-Restaurante / España 2026', 'Opening Checklist — Restaurant & Bar (US example, 2026)'),
    ('ChefBusiness.co — Checklist Apertura Bar-Restaurante / España 2026', 'AI Chef Pro · ' + URL_REST),
    # D37: la fila de licencias del restaurante es la de alcohol; ejemplo de estado SIN cupo
    ('Licencias y permisos varios', 'Liquor license + permits (non-quota state example)'),
    # I9: título de la inversión de la panadería sin «España 2026»; D37: B63 de la panadería
    ('Inversión Inicial — España 2026', 'Startup Costs — US example (2026)'),
    ('IVA de la bebida ALCOHÓLICA servida en mostrador', 'Sales tax rate on alcohol served at the counter'),
    # D36 (E3): la col. H del P&L de la panadería es la parte EXENTA del sales tax
    ('Pan común sobre la línea (%)', 'Tax-exempt share of the line (%)'),
])
# Mismo ES con dos EN según el libro (D35/I8 y SPEC delta §3): solo en ESA celda
POR_CELDA = OrderedDict([
    (('RESTC', 'Instrucciones', 'A5'), 'OK column: choose ✓ (done), — (pending) or N/A (not applicable). N/A items do '
                                       'not count toward the total.'),
    (('RESTC', 'Checklist Apertura', 'B52'), 'Consumer advisory and allergen notice on the menu'),
    (('PANC', 'F2', 'B13'), 'Ingredient and allergen labels for packaged and wholesale products'),
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
    ('inv_lanzamiento', ('usd', ('fila', _I, {'rest': 'Campaña lanzamiento RRSS + inauguración',
                                              'pan': 'Marketing lanzamiento'}, 'B'),
                         'grand opening / launch marketing budget')),
    ('inv_stock', ('usd', ('fila', _I, {'rest': 'Primera compra de despensa y cámaras',
                                        'pan': 'Stock inicial (harinas, levaduras, etc.)'}, 'B'),
                   'opening food inventory (bakery: flour, yeast and other ingredients)')),
    ('inv_stock_barra', ('usd', ('fila', _I, {'rest': 'Primera compra de bodega y barra'}, 'B'),
                         'opening bar inventory (wine, beer, spirits)')),
    ('inv_obra', ('usd', ('fila', _I, {'rest': 'Obra civil y reforma local', 'pan': 'Obra civil y adecuación local'},
                          'B'), 'build-out of the premises')),
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
    # F2 tanda 2: el docx REST cita el prime cost de referencia (60-65 %, Restaurant365) y ahora también el del caso
    ('prime_cost_pct', ('pct1', ('deriv', lambda c: c['cogs_pct'] + c['personal_pct']),
                        'prime cost year 1 (cost of goods + labor, % of sales)')),
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
        if t == 'consumibles_pct':
            fmt = 'pct1'                  # F2 tanda 2: el 1.5 % del restaurante salía «2%» con pct0
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


# ==========================================================================
# Pistas por celda y por texto (las lee extraer_textos.py → textos_es.json → tandas)
# ==========================================================================
_A8 = ('SPEC §4.1 línea 4: sin divisores 1,10/1,21/1,04 → «divide a menu price by 1 + your sales tax rate»; P&L excl. '
       'sales tax, cash flow incl.')
CELDA_PISTAS = OrderedDict([
    (('RESTP', '0. Supuestos', 'A2'), 'D8: añade una vez que los importes van «in your currency» (sin símbolo)'),
    (('PANP', '0. Supuestos', 'A2'), 'D8: añade una vez que los importes van «in your currency» (sin símbolo)'),
    (('RESTP', 'Instrucciones', 'A8'), _A8),
    (('PANP', 'Instrucciones', 'A8'), _A8 + '; en la panadería, la parte exenta de la línea de pan (col. H del P&L, D36) '
                                          'no lleva sales tax'),
    (('PANP', 'Instrucciones', 'A12'), 'SPEC §4.1 línea 8 (I1): el Word del kit usa las MISMAS cifras de ejemplo que '
                                       'este libro; si cambias el libro, actualiza las cifras del Word'),
    (('RESTP', '6. Tesorería 12 meses', 'O5'), 'SPEC §4.1: estacionalidad «your area» (sin agosto/costa de España)'),
    (('PANP', 'Tesorería 12 meses', 'O5'), 'SPEC §4.1: estacionalidad «your area» (sin agosto/costa de España)'),
    # D36: nota de la col. H (F10) y su cabecera
    (('PANP', 'PyG 3 Años', 'F10'), 'D36 (E3): la col. H es la parte EXENTA del sales tax de la línea (bollería para '
                                    'llevar + venta mayorista a un café que revende, con resale certificate); ejemplo '
                                    '0.80; CA exime la bollería para llevar y grava el consumo en el local (regla '
                                    '80/80) — «check your state»; con 0 el libro grava toda la línea; UK: zero-rated '
                                    'para llevar, 20 % en el local. Solo afecta a la tesorería (el P&L va sin impuesto)'),
    # D37: alcohol en el restaurante
    (('RESTP', '0. Supuestos', 'C63'), 'D37: algunos estados y ciudades añaden un impuesto por consumición de alcohol al '
                                       'sales tax → teclea aquí el tipo COMBINADO; 8 % de ejemplo'),
    (('RESTP', '0. Supuestos', 'C62'), 'D37: alcohol = 70 % de las ventas de bebida en el ejemplo US (barra con '
                                       'cerveza, vino y cócteles)'),
    # D38: propinas
    (('RESTP', '5. Personal', 'A29'), 'D38: el libro NO modela propinas ni tip credit: servers y bartenders a ≥ $15/h '
                                      'de salario base; federal $2.13/h + tip credit hasta $5.12 donde el estado lo '
                                      'permite; CA, OR, WA, AK, MN, MT y NV no lo permiten (DOL). Suelo = el MAYOR '
                                      'entre el mínimo federal y el estatal/local de "0. Assumptions"'),
    # D19 del restaurante: las filas de cierre de restaurantes no tienen fuente (I10) → otras filas con fuente
    (('RESTP', 'Instrucciones', 'A56'), 'I10/D37: esta fila ES («tasa de cierre 25 %», sin fuente) se SUSTITUYE por '
                                        '«Liquor license (state + local)» · «from $50 to $300,000+» · webstaurantstore.com '
                                        '· «this workbook budgets a non-quota state example; in quota states you buy an '
                                        'existing license»'),
    (('RESTP', 'Instrucciones', 'A57'), 'I10: esta fila ES («cierre a 5 años 50 %», sin fuente) se SUSTITUYE por «Prime '
                                        'cost (food + labor)» · «60-65% of sales» · restaurant365.com'),
])
for _col in 'BCD':
    CELDA_PISTAS[('RESTP', 'Instrucciones', '%s56' % _col)] = CELDA_PISTAS[('RESTP', 'Instrucciones', 'A56')]
    CELDA_PISTAS[('RESTP', 'Instrucciones', '%s57' % _col)] = CELDA_PISTAS[('RESTP', 'Instrucciones', 'A57')]
# Equivalencias de los checklists y del docx (SPEC delta §3): pista por TEXTO, como mapas.PISTAS
PISTAS_EXTRA = [
    (r'SL con capital|certificación negativa|denominación', 'SPEC delta §3: LLC; business name availability search + '
                                                             'DBA si se opera con otro nombre'),
    (r'[Ee]scritura|Registro Mercantil|alta de autónomos|notar', 'SPEC delta §3: articles of organization (Secretary of '
                                                                 'State); operating agreement; owners\' draws y '
                                                                 'self-employment tax (accountant)'),
    (r'[Pp]royecto técnico|licencia de obras|[Bb]oletines', 'SPEC delta §3: architect + MEP drawings; building, '
                                                           'electrical, plumbing and gas permits con inspecciones finales'),
    (r'[Dd]eclaración responsable|licencia de actividad|[Ll]icencia actividad|clasificada',
     'SPEC delta §3: zoning check (retail bakery / light food manufacturing use) → certificate of occupancy'),
    (r'[Ee]xtracción|salida de humos|[Cc]ampana|potencia|kW', 'SPEC delta §3: Type I hood + UL 300 suppression (NFPA 96) '
                                                              '· oven ventilation permit · utility service upgrade '
                                                              '(3-phase) con la compañía eléctrica'),
    (r'Registro Sanitario|RGSEAA', 'SPEC delta §3: health department plan review → food establishment permit (PAN: o '
                                   'licencia estatal de agricultura si hay mayorista; FDA facility registration solo si '
                                   'lo mayorista domina)'),
    (r'[Tt]erraza', 'SPEC delta §3: sidewalk café / outdoor dining permit'),
    (r'alcohol a menores|[Ll]icencia de alcohol|bebidas alcohólicas', 'SPEC delta §3 / D37: liquor license (state ABC + '
                                                                       'local; quota states: license transfer) + '
                                                                       'responsible beverage service training + age '
                                                                       'signage'),
    (r'[Hh]ojas de reclamaciones', 'SPEC delta §3: REST consumer advisory and allergen notice on the menu · PAN '
                                   'ingredient and allergen labels for packaged and wholesale products'),
    (r'[Dd]esperdicio|Ley 1/2025', 'SPEC delta §3: food donation program (Bill Emerson Good Samaritan Act) + reglas '
                                   'locales de reciclaje orgánico donde existan'),
    (r'[Cc]omunicación de apertura|centro de trabajo', 'SPEC delta §3: state new-employer registration + carteles '
                                                       'laborales federales y estatales'),
    (r'OEPM|[Mm]arca registrada', 'SPEC delta §3: USPTO trademark (opcional)'),
    (r'InfoJobs|Indeed', 'SPEC delta §3: Indeed, Culinary Agents, Poached'),
    (r'[Cc]asera|[Oo]brador|mayorista|reparto|HORECA', 'D30/D39: panadería COMERCIAL con tienda, rincón de café y '
                                                       'mayorista a cafés; cottage food = otro comprador (venta desde '
                                                       'casa con topes); lo mayorista va DENTRO de la línea de pan'),
    (r'[Cc]ubiertos?|comensales|rotaci', 'D43: el restaurante habla de «covers» (cubiertos) y «seat turns»'),
    (r'[Tt]ransacciones', 'D43: la panadería habla de «transactions»'),
    (r'[Pp]ropina|[Cc]amarer', 'D38: sin tip credit en el libro (servers ≥ $15/h); nota federal $2.13/h + tip credit '
                               'donde el estado lo permite'),
]


# ==========================================================================
# Caso de ejemplo US (D42, F1-research-us-delta §7): celdas VERDES. (corto, hoja ES, celda) → (valor, rótulo)
# ==========================================================================
def valores_rp(M):
    v = OrderedDict()
    sup = OrderedDict((c, rot) for c, _vals, rot in M._SUP_COMUN)
    comun = OrderedDict([('B6', 310), ('B13', 0.30), ('B16', 0), ('B17', 0.25), ('B18', 0.035), ('B20', 0.10),
                         ('B21', 12), ('B22', 15080), ('B25', 2), ('B31', M.CALIBRAR), ('B32', 0.10), ('B33', 10),
                         ('B34', 0), ('B37', 0.25), ('B38', 0.25), ('B39', 0.08), ('B40', 0.08), ('B41', 0), ('B42', 0),
                         ('B44', 10), ('B45', 7), ('B58', 1), ('B59', 14), ('B63', 0.08), ('B65', 1.15), ('B66', 1.25),
                         ('B68', None)])
    # REST B51 = 68 (F2 tanda 2): la inversión presupuesta «15 tables × 4 chairs» + «Bar stools (8 units)» y el rótulo
    # de A51 dice «seats at tables + bar»: 60 + 8 = 68 (research §7 hablaba de «60 plazas» solo de mesas)
    propios = {
        'RESTP': [('B4', 125, 'Cubiertos/día'), ('B5', 28, None), ('B11', 0.70, 'Ventas de COMIDA'), ('B14', 0.24, None),
                  ('B15', 0.015, None), ('B24', 7000, None), ('B26', 2500, None), ('B27', 9000, None),
                  ('B30', 130000, None), ('B51', 68, 'Aforo'), ('B62', 0.70, None)],
        'PANP': [('B4', 210, 'Transacciones/día'), ('B5', 10, None), ('B11', 0.85, 'Ventas de COMIDA'),
                 ('B14', 0.22, None), ('B15', 0.03, None), ('B24', 4200, None), ('B26', 1500, None), ('B27', 4500, None),
                 ('B30', 70000, None), ('B62', 0, None)],
    }
    for corto in ('RESTP', 'PANP'):
        for c, val in comun.items():
            v[(corto, '0. Supuestos', c)] = (val, sup.get(c))
        for c, val, rot in propios[corto]:
            v[(corto, '0. Supuestos', c)] = (val, rot or sup.get(c))
    inv_rest = [(7, 3000), (8, 90000), (9, 18000), (10, 10000), (15, 14000), (16, 9000), (17, 4000), (18, 6000),
                (19, 16000), (20, 25000), (21, 8000), (22, 8000), (23, 9000), (24, 3000), (26, 25000), (27, 15000),
                (28, 2400), (29, 8000), (30, 1500), (31, 6000), (32, 2500), (33, 8000), (34, 5000), (35, 8000),
                (37, 5000), (38, 3000), (39, 8000), (41, 2500), (42, 15000), (44, 8000), (45, 10000)]
    for f, val in inv_rest:
        v[('RESTP', '1. Inversión Inicial', 'B%d' % f)] = (val, None)
    # PAN: research §7 da 18 partidas para 19 filas; la 9 («Proyecto técnico + certificación») = arquitecto y planos
    # MEP del obrador, 6,000 [kit estimate] (F2-NOTAS §4)
    inv_pan = [1500, 2500, 6000, 35000, 10000, 10000, 25000, 9000, 7000, 10000, 9000, 5000, 8000, 9000, 4000, 2500,
               3000, 4000, 3000]
    for k, val in enumerate(inv_pan):
        v[('PANP', 'Inversión Inicial', 'B%d' % (7 + k))] = (val, None)
    for k, val in enumerate([6000, 18000, 9000, 4800, 9600, 3600, 1200, 1200, 1000, 3000, 4800]):
        v[('RESTP', '2. P&L 3 Años', 'B%d' % (27 + k))] = (val, None)
    for k, val in enumerate([3600, 4000, 7200, 1800, 2400, 1200, 1200, 900, 600, 500]):
        v[('PANP', 'PyG 3 Años', 'B%d' % (26 + k))] = (val, None)
    # umbrales D41 [kit benchmark] y la parte exenta de la línea de pan (D36)
    for c, val, rot in [('E53', 0.65, 'Margen bruto'), ('E55', 0.32, 'Coste de mercancía'),
                        ('E56', 0.35, 'Coste de personal'), ('E57', 0.10, 'Alquiler'), ('E58', 0.05, 'Resultado neto')]:
        v[('RESTP', '2. P&L 3 Años', c)] = (val, rot)
    for c, val, rot in [('E51', 0.60, 'Margen bruto'), ('E53', 0.33, 'Coste de mercancía'),
                        ('E54', 0.38, 'Coste de personal'), ('E55', 0.10, 'Alquiler'), ('E56', 0.05, 'Resultado neto'),
                        ('H10', 0.80, 'Ventas de pan')]:
        v[('PANP', 'PyG 3 Años', c)] = (val, rot)
    # Personal (research §7): personas (B), jornada por persona (C), bruto mes TOTAL de la fila (D); sin tip credit
    for f, (b, c, d) in zip(range(6, 13), [(1, 1, 4500), (1, 1, 4200), (2, 1, 6400), (2, 1, 5200), (2, 0.5, 2600),
                                           (1, 0.75, 1950), (1, 0.2, 520)]):
        for col, val in zip('BCD', (b, c, d)):
            v[('RESTP', '5. Personal', '%s%d' % (col, f))] = (val, None)
    for f, (b, c, d) in zip(range(5, 11), [(1, 1, 4000), (1, 1, 3300), (1, 1, 2800), (3, 0.67, 5200), (1, 0.4, 1040),
                                           (1, 0.15, 390)]):
        for col, val in zip('BCD', (b, c, d)):
            v[('PANP', 'Personal', '%s%d' % (col, f))] = (val, None)
    v.update([
        (('RESTP', '5. Personal', 'B15'), (8000, 'Coste anual')), (('RESTP', '5. Personal', 'B16'), (8000, 'Coste anual')),
        (('RESTP', '5. Personal', 'B20'), (40, 'Jornada completa')), (('RESTP', '5. Personal', 'B21'), (50, 'Semanas')),
        (('RESTP', '5. Personal', 'B22'), (12, 'Horas de servicio')),
        (('RESTP', '5. Personal', 'B23'), (4, 'Personas necesarias')),
        (('PANP', 'Personal', 'B13'), (6000, 'Coste anual')), (('PANP', 'Personal', 'B14'), (6000, 'Coste anual')),
        (('PANP', 'Personal', 'B18'), (40, 'Jornada completa')), (('PANP', 'Personal', 'B19'), (50, 'Semanas')),
        (('PANP', 'Personal', 'B20'), (12, 'Horas de servicio')), (('PANP', 'Personal', 'B21'), (1.5, 'Personas')),
        (('PANP', 'Personal', 'B22'), (4, 'Horas de producción')), (('PANP', 'Personal', 'B23'), (2, 'Personas')),
    ])
    # Escenarios [kit estimate]: mismas proporciones que el ES (REST 58/80/95 · 15.90/18.20/18.50 · 300/310/320;
    # PAN 120/180/200 · 4.20/5.50/6.00 · 300/310/320) sobre el caso base US
    v.update([
        (('RESTP', '4. Escenarios', 'B6'), (91, 'Cubiertos/día')), (('RESTP', '4. Escenarios', 'D6'), (148, 'Cubiertos/día')),
        (('RESTP', '4. Escenarios', 'B7'), (24.46, 'Ticket')), (('RESTP', '4. Escenarios', 'D7'), (28.46, 'Ticket')),
        (('RESTP', '4. Escenarios', 'B8'), (300, 'Días')), (('RESTP', '4. Escenarios', 'D8'), (320, 'Días')),
        (('PANP', 'Escenarios', 'B5'), (140, 'Transacciones/día')), (('PANP', 'Escenarios', 'D5'), (233, 'Transacciones/día')),
        (('PANP', 'Escenarios', 'B6'), (7.64, 'Ticket')), (('PANP', 'Escenarios', 'D6'), (10.91, 'Ticket')),
        (('PANP', 'Escenarios', 'B7'), (300, 'Días')), (('PANP', 'Escenarios', 'D7'), (320, 'Días')),
    ])
    return v


# ==========================================================================
# Calibración D15 (F2 tanda 2; F2-NOTAS.md §7 la explica celda a celda: G7 exige la cita). UNA palanca por plan
# ==========================================================================
CALIBRACION_D15 = OrderedDict([
    # REST: margen bruto 64.8 % < 65 % (ámbar los 3 años). Food cost de la comida 30 % → 29 %, dentro del 25-35 % de
    # research §4 (Papaya) y de la tabla D19 (fila 51). Margen bruto 65.5 %; el ticket y el volumen no se tocan
    (('RESTP', '0. Supuestos', 'B13'), (0.29, 'D41: margen bruto 64.8 % → 65.5 %; food cost dentro del 25-35 % de research')),
    # PAN: la cobertura de horas salía 138 % con 1.5 personas en el mostrador: 210 transacciones/día con rincón de café
    # piden 2 a la vez durante las 12 h. No cambia ningún coste (es la comprobación de Staffing): cobertura 112 %
    (('PANP', 'Personal', 'B21'), (2, 'D15: cobertura 138 % → 112 %; 2 personas en el mostrador durante el servicio')),
])


def formulas_rp():
    p = os.path.join(AQUI, 'formulas_rp.json')
    out = OrderedDict()
    if os.path.exists(p):
        for k, d in json.load(open(p, encoding='utf-8')).items():
            c, h, x = k.split('|')
            out[(c, h, x)] = d['en']
    return out


def completar(M):
    fijos = OrderedDict((k, v) for k, v in M.FIJOS.items() if k not in FIJOS_FUERA)
    fijos.update(FIJOS_NUEVOS)
    M.FIJOS = fijos
    M.POR_CELDA = POR_CELDA
    M.TOKENS_DOCX = tokens_rp(M.TOKENS_DOCX)
    M.DOCX_FIJOS = docx_fijos(M)
    M.DOCX_NOTAS = DOCX_NOTAS
    M.DOCX_NOTAS_PLAN = DOCX_NOTAS_PLAN
    M.FORMULAS_EN = formulas_rp()
    M.VALORES_EN = valores_rp(M)
    M.CALIBRACION_D15 = CALIBRACION_D15
    M.CELDA_PISTAS = CELDA_PISTAS
    M.PISTAS_EXTRA = PISTAS_EXTRA
