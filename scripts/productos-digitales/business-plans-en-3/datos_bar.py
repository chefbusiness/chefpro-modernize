#!/usr/bin/env python3
"""
datos_bar.py — Bar Business Plan Kit (EN) · los datos ES→EN que dependen del contenido de los libros: rótulos fijados
(D54-D55), POR_CELDA (D60), pistas, tokens del docx (D61), fijos y notas del docx, caso US (D52; research §8),
FORMULAS_EN (D59), cifras ES prohibidas (D52) y glosario del bar. Lo llama `mapas_bar.instalar()` con el módulo
`mapas` YA cargado con los datos de FT/CAF, de los que parte (FIJOS comunes del motor 2.2, TOKENS_DOCX).
Sesión Claude Code, 11-oct-2026 (F2, paso 1).
"""
import json
import os
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))

URL_BAR = 'aichef.pro/en/digital-products/bar-business-plan'
_I, _S, _P, _R, _N = 'Inversión Inicial', '0. Supuestos', 'PyG 3 Años', 'Personal', 'Instrucciones'

# ==========================================================================
# FIJOS (por TEXTO ES, en cualquier celda de los 2 libros del bar). Parten de los de FT/CAF (los del motor 2.2).
# ==========================================================================
FIJOS_FUERA = ('Este fichero forma parte del producto «plan-negocio-food-truck» de AI Chef Pro.',
               'Este fichero forma parte del producto «plan-negocio-cafeteria» de AI Chef Pro.')
_TITULO_CHECK = 'BAR OPENING CHECKLIST — NEIGHBORHOOD BAR WITH SMALL PLATES'
FIJOS_NUEVOS = OrderedDict([
    # I5 / D50: Instrucciones!A3 del checklist con el nombre comercial
    ('Este fichero forma parte del producto «plan-negocio-tapas-bar» de AI Chef Pro.',
     'This file is part of the Bar Business Plan Kit by AI Chef Pro.'),
    # títulos (D51, I9): sin «España 2026» ni «tapas bar / gastrobar»
    ('CHECKLIST APERTURA — TAPAS BAR / GASTROBAR', _TITULO_CHECK),
    ('INSTRUCCIONES DE USO — Plan financiero Tapas Bar / Gastrobar', 'HOW TO USE THIS WORKBOOK — Bar Financial Projections'),
    ('PLAN DE NEGOCIO: TAPAS BAR / GASTROBAR', 'BAR BUSINESS PLAN: NEIGHBORHOOD BAR WITH SMALL PLATES'),
    ('Inversión Inicial Estimada — España 2026', 'Estimated Startup Costs — US kit example (2026)'),
    ('Ajusta las cifras a tu proyecto. Rangos mercado español actual.',
     'US kit example (2026) — replace with your own quotes.'),
    # D58: cabecera de la tabla D19; D53: la fase 2 del checklist se llama como su pestaña («Location & Licenses»)
    ('DATOS DE REFERENCIA DEL SECTOR', 'US INDUSTRY BENCHMARKS (sourced) AND KIT ESTIMATES'),
    ('FASE 2: LOCAL Y LICENCIAS', 'PHASE 2: LOCATION & LICENSES'),
    # D54: partidas de la inversión, filas 7-24 (rótulos fijados)
    ('Constitución SL + notaría + registro', 'LLC formation + legal'),
    ('Licencia de actividad (clasificada)', 'Liquor license + local permits (non-quota state example)'),
    ('Proyecto técnico + certificación', 'Architect, MEP drawings + permit fees'),
    ('Obra civil y adecuación local', 'Build-out (second-generation space)'),
    ('Instalación eléctrica + climatización', 'Electrical + HVAC'),
    ('Fontanería + evacuación + extracciones', 'Plumbing, grease interceptor + Type I hood'),
    ('Equipamiento cocina (plancha, freidora, horno)', 'Kitchen equipment (griddle, fryer, oven)'),
    ('Equipamiento frío (cámaras, neveras barra)', 'Refrigeration (walk-in + back-bar coolers)'),
    ('Barra y mostrador de tapas', 'Bar build (bar top + underbar stations)'),
    ('Grifos cerveza + instalación', 'Draft beer system + installation'),
    ('Mobiliario sala (mesas altas + bajas + taburetes)', 'Furniture (tables, high-tops + bar stools)'),
    ('Terraza (mobiliario + toldo)', 'Patio (furniture + awning)'),
    ('Vajilla, cristalería tapas, cubertería', 'Glassware, smallwares + tableware'),
    ('Decoración + iluminación ambiente', 'Decor, lighting + sound'),
    ('Rotulación + imagen exterior', 'Exterior signage'),
    ('Marketing lanzamiento', 'Launch marketing'),
    ('Stock inicial (producto, vinos, cervezas)', 'Opening inventory (liquor, beer, wine + food)'),
    ('TPV + software gestión + comandero', 'POS + handhelds + software'),
    # D55: P&L (A2, A10, A11, fijos A25-A34 de research §8)
    ('Escenario realista — Tapas Bar / Gastrobar 40-50 plazas', 'Base case — neighborhood bar with small plates, 60 seats'),
    ('Ventas de comida (tapas, raciones y otros)', 'Food sales (small plates)'),
    ('Ventas de bebida (cerveza, vino, vermut y cócteles)', 'Beverage sales (cocktails, beer, wine + non-alcoholic)'),
    ('Seguros (RC + multirriesgo)', 'Insurance (general + liquor liability + property)'),
    ('Gestoría + contabilidad', 'Accounting + bookkeeping'),
    ('Mantenimiento equipos', 'Equipment maintenance'),
    ('Software (TPV, reservas, delivery)', 'Software (POS, reservations, inventory)'),
    ('Limpieza y productos', 'Cleaning supplies + linens'),
    ('Gestión de residuos (orgánico, cartón y aceite usado)', 'Waste + grease hauling (trash, recycling, used oil)'),
    ('Desinsectación, desratización y desinfección (DDD)', 'Pest control'),
    ('Derechos de autor por música ambiental (SGAE/AGEDI-AIE)', 'Music licensing (ASCAP/BMI/SESAC)'),
    ('Prevención de riesgos laborales y vigilancia de la salud', 'Safety + responsible-service training'),
    # D55: puestos de Staffing (A5:A11)
    ('Propietario/a y encargado/a de sala', 'Owner / general manager'),
    ('Jefe de cocina', 'Kitchen lead'),
    ('Camarero/a de barra (turno fuerte)', 'Bartenders (peak shifts)'),
    ('Camarero/a de sala y terraza', 'Servers (floor & patio)'),
    ('Ayudante de cocina', 'Line / prep cook'),
    ('Extra de fin de semana (barra y sala)', 'Barback / weekend extra'),
    ('Suplencias de vacaciones y descansos', 'Relief cover (vacations + days off)'),
])

# Mismo ES con otro EN en ESTA celda (D60; lección de BP2 §4.1: los arreglos de un libro no se heredan a ciegas)
POR_CELDA = OrderedDict([
    # D60: F2-11 seguro de RC → general liability + liquor liability (dram shop)
    (('BARC', 'F2 - Local', 'B11'), 'General liability + liquor liability (dram shop) insurance'),
    # D60: F2-8 la licencia de alcohol, responsable Owner + attorney y plazo largo (lección M1 de BP2). C8 es GM
    # («Ingeniero» → «Architect / engineer» en FT/CAF)
    (('BARC', 'F2 - Local', 'C8'), 'Owner + attorney'),
    (('BARC', 'F2 - Local', 'D8'), 'Start right after signing the lease: often 3-12 months'),
    # BP2 §4.1: «Hojas de reclamaciones…» es GM con el EN del food truck («Commissary agreement…»): en el bar, los
    # avisos obligatorios (la nota E14, reutilizada del restaurante, ya habla de health department, laborales y alcohol)
    (('BARC', 'F2 - Local', 'B14'), 'Required public notices posted (health permit, liquor license, labor law posters)'),
    # Revisión final m12 / m13: «2-4 semanas» (GM, 2 celdas) y «Control food cost semanal» (GM), «Jefe cocina» (3)
    (('BARC', 'F3 - Equipamiento', 'D5'), '1-3 months'),
    (('BARC', 'F6 - 90 Días', 'B6'), 'Weekly food and pour cost check'),
    (('BARC', 'F6 - 90 Días', 'C6'), 'Owner + kitchen lead'),
    # D57: nota del tipo del alcohol en sala con el ejemplo de Texas (la de REST no lo tenía)
    (('BARP', '0. Supuestos', 'C63'), 'Same example rate as the rest of on-site sales (8%: state + local). Some states add '
                                      'a tax on drinks served on premises; e.g. Texas: 8.25% mixed beverage sales tax '
                                      '(paid by the customer) + 6.7% gross receipts tax (paid by the bar): put the first '
                                      'here and add 6.7% × your alcohol share (about 6 points at 90%) to your beverage '
                                      'cost %. The workbook applies this rate '
                                      'only to the ALCOHOLIC part of beverage sales'),
    # E4 + D38: la nota de Staffing con el FTE ya multiplicado por personas (override c0422 del restaurante) y las
    # propinas, que el libro no modela
    (('BARP', 'Personal', 'A29'), 'The gross pay, employer payroll taxes, monthly cost and annual cost columns are '
                                  'TOTALS for the row: for a position with two people they include both. The payroll tax '
                                  'rate and the number of pay periods are in the "0. Assumptions" tab. Tips are not '
                                  'modeled: bartenders, barbacks and servers are budgeted at a base wage of at least '
                                  '$15/h. Federal rules allow a $2.13/h cash wage with a tip credit of up to $5.12 where '
                                  'the state permits it; CA, OR, WA, AK, MN, MT and NV do not (DOL)'),
])

# ==========================================================================
# Cifras del ES que no pueden llegar al EN (D52) y términos fuera del concepto (D51). (regex, motivo, excepción)
# ==========================================================================
def _num(n):
    """302400 → patrón que casa 302,400 · 302.400 · 302 400 · 302400 (y nada pegado a más dígitos)."""
    s = str(n)
    cab, cola = s[:-3], s[-3:]
    return r'(?<![\d.,])' + cab + r'[.,   ]?' + cola + r'(?![\d])'


CIFRAS_PROHIBIDAS = [(_num(n), 'cifra del caso ES (D52)', None)
                     for n in (302400, 153327, 109450, 174317, 129000, 17094, 115000, 270000)]
CIFRAS_PROHIBIDAS += [
    # 50.000 € de recursos propios del ES; el «up to $50,000» del SBA Microloan es una regla US con fuente
    (_num(50000), 'cifra del caso ES (D52: 50.000 de recursos propios)', r'(?i)microloan'),
    (r'(?i)\b34 (?:customers|guests|covers|clients|people)\b', 'equilibrio del docx ES (D52: «34 clientes»)', None),
    (r'(?i)\b14 (?:pay periods|payments|paychecks|salaries|monthly)', 'pagas del ES (D52: «14 pagas»)', None),
    (r'(?i)(?:payroll|social security|employer)[^.;]{0,60}?\b33\s?%', 'Seguridad Social del ES (D52: «33 %»)', None),
    (r'(?i)\b33\s?%[^.;]{0,40}?(?:payroll|social security|employer)', 'Seguridad Social del ES (D52: «33 %»)', None),
    (r'(?i)\bgastrobar\b', 'concepto ES (D51: «neighborhood bar with small plates»)', None),
    (r'(?i)\btapas bar\b', 'concepto ES (D51: «small plates (tapas-style)», nunca «tapas bar»)', None),
    (r'\bv1\.1\b|\b[Vv]ersion 1\.1\b', 'historia de versiones (D18: la EN nace en 2.2)', None),
]

# ==========================================================================
# Tokens del docx (D61): los de FT/CAF con los rótulos del bar («Cubiertos…» como REST) + partidas propias
# ==========================================================================
_CLIENTES = OrderedDict([
    ('Clientes/día (media del año 1)', 'Cubiertos/día (media del año 1)'),
    ('Clientes/día (media)', 'Cubiertos/día (media)'),
    ('Clientes/día', 'Cubiertos/día'),
    ('Clientes necesarios al día', 'Cubiertos necesarios al día'),
    ('Clientes necesarios al día (caja)', 'Cubiertos necesarios al día (caja)'),
])
_DESC = OrderedDict([
    ('clientes_dia', 'average covers (guests) per day, year 1'),
    ('clientes_a2', 'average covers per day, year 2'),
    ('clientes_a3', 'average covers per day, year 3'),
    ('equilibrio_clientes_dia', 'break-even covers per day (accounting)'),
    ('equilibrio_caja_clientes_dia', 'cash break-even covers per day (loan payments in, depreciation out)'),
    ('pesimista_clientes', 'pessimistic scenario: covers per day'),
    ('optimista_clientes', 'optimistic scenario: covers per day'),
    ('alquiler_mes', 'rent per month (base rent of the premises)'),
    ('vida_obra', 'useful life of build-out, years'),
    ('ocupacion_anual', 'rent per year (occupancy)'),
    ('consumibles_pct', 'consumables (napkins, straws, to-go), % of sales'),
])
_FUERA = ('inv_vehiculo', 'inv_adaptacion', 'inv_equipo_cocina', 'inv_generador', 'inv_permisos', 'inv_espresso',
          'inv_obra', 'inv_instalaciones', 'inv_mobiliario', 'inv_barra', 'inv_terraza', 'inv_lanzamiento',
          'inv_stock', 'aforo', 'rotaciones_dia')
TOKENS_PROPIOS = OrderedDict([
    ('inv_licencia', ('usd', ('fila', _I, {'bar': 'Licencia de actividad (clasificada)'}, 'B'),
                      'liquor license + local permits (non-quota state example)')),
    ('inv_proyecto', ('usd', ('fila', _I, {'bar': 'Proyecto técnico + certificación'}, 'B'),
                      'architect, MEP drawings and permit fees')),
    ('inv_obra', ('usd', ('fila', _I, {'bar': 'Obra civil y adecuación local'}, 'B'),
                  'build-out of a second-generation space')),
    ('inv_instalaciones', ('usd', ('fila', _I, {'bar': 'Instalación eléctrica + climatización'}, 'B'), 'electrical + HVAC')),
    ('inv_campana', ('usd', ('fila', _I, {'bar': 'Fontanería + evacuación + extracciones'}, 'B'),
                     'plumbing, grease interceptor and Type I hood')),
    ('inv_cocina', ('usd', ('fila', _I, {'bar': 'Equipamiento cocina (plancha, freidora, horno)'}, 'B'),
                    'kitchen equipment (griddle, fryer, oven)')),
    ('inv_frio', ('usd', ('fila', _I, {'bar': 'Equipamiento frío (cámaras, neveras barra)'}, 'B'),
                  'refrigeration (walk-in + back-bar coolers)')),
    ('inv_barra', ('usd', ('fila', _I, {'bar': 'Barra y mostrador de tapas'}, 'B'),
                   'bar build (bar top + underbar stations)')),
    ('inv_grifos', ('usd', ('fila', _I, {'bar': 'Grifos cerveza + instalación'}, 'B'), 'draft beer system + installation')),
    ('inv_mobiliario', ('usd', ('fila', _I, {'bar': 'Mobiliario sala (mesas altas + bajas + taburetes)'}, 'B'),
                        'furniture (tables, high-tops and bar stools)')),
    ('inv_terraza', ('usd', ('fila', _I, {'bar': 'Terraza (mobiliario + toldo)'}, 'B'), 'patio (furniture + awning)')),
    ('inv_lanzamiento', ('usd', ('fila', _I, {'bar': 'Marketing lanzamiento'}, 'B'), 'launch marketing budget')),
    ('inv_stock', ('usd', ('fila', _I, {'bar': 'Stock inicial (producto, vinos, cervezas)'}, 'B'),
                   'opening inventory (liquor, beer, wine + food)')),
    ('inv_tpv', ('usd', ('fila', _I, {'bar': 'TPV + software gestión + comandero'}, 'B'), 'POS + handhelds + software')),
    ('aforo', ('int', ('fila', _S, {'bar': 'Aforo del local (plazas sentadas + barra)'}, 'B'), 'seats (tables + bar)')),
    ('rotaciones_dia', ('dec1', ('fila', _S, {'bar': 'Rotaciones al día implícitas (calculado)'}, 'B'),
                        'implied seat turns per day')),
    ('comida_pct', ('pct0', ('fila', _S, {'bar': 'Ventas de COMIDA sobre el total'}, 'B'), 'food share of sales')),
    ('bebida_pct', ('pct0', ('fila', _S, {'bar': 'Ventas de BEBIDA sobre el total'}, 'B'), 'beverage share of sales')),
    ('alcohol_pct', ('pct0', ('fila', _S, {'bar': 'Bebida ALCOHÓLICA sobre el total de bebida'}, 'B'),
                     'alcohol share of beverage sales')),
    ('prime_cost_pct', ('pct1', ('deriv', lambda c: c['cogs_pct'] + c['personal_pct']),
                        'prime cost year 1 (cost of goods + labor, % of sales)')),
    # Revisión final (M1, M2, M4): cifras que el docx cita y que salen del mismo caso
    ('meses_alquiler_previo', ('int', ('fila', _S, {'bar': 'Meses de alquiler ANTES de abrir (obra y licencias)'}, 'B'),
                               'months of rent paid before opening (build-out and licenses)')),
    ('costes_variables_pct', ('pct1', ('deriv', lambda c: 1 - c['margen_bruto_pct']),
                              'all variable costs year 1 (cost of goods + card fees + disposables + contingency), % of '
                              'sales')),
    ('otros_variables_pct', ('pct1', ('deriv', lambda c: 1 - c['margen_bruto_pct'] - c['cogs_pct']),
                             'card fees + disposables + contingency, % of sales')),
    ('pesimista_perdida', ('usd', ('deriv', lambda c: -c['pesimista_resultado']),
                           'pessimistic scenario: pre-tax LOSS as a positive amount')),
    ('pesimista_perdida_operativa', ('usd', ('deriv', lambda c: -(c['pesimista_resultado'] + c['amortizacion_anual'] +
                                                                  c['intereses_a1'])),
                                     'pessimistic scenario: operating loss before depreciation and interest (positive)')),
])


def tokens_bar(base):
    out = OrderedDict()
    for t, (fmt, src, desc) in base.items():
        if t in _FUERA:
            continue
        if src[0] == 'fila':
            _, hoja, rot, col = src
            if isinstance(rot, dict):                     # ocupación: el rótulo de la cafetería es el del motor común
                rot = rot['caf']
            elif rot in _CLIENTES:
                rot = _CLIENTES[rot]
            src = ('fila', hoja, {'bar': rot}, col)
        if t == 'consumibles_pct':
            fmt = 'pct1'
        out[t] = (fmt, src, _DESC.get(t, desc))
    out.update(TOKENS_PROPIOS)
    return out


# ==========================================================================
# Docx: lo que escribe ensamblar_docx.py (portada, aviso, índice, encabezados, cierre — D22, D23, D61)
# ==========================================================================
def docx_fijos(M):
    pc = M.PRODUCTOS_CIERRE
    d = OrderedDict([
        (6, 'BUSINESS PLAN'), (7, 'Neighborhood Bar with Small Plates'),
        (9, 'Complete financial plan, market analysis,\noperations strategy and opening checklist\nto open a '
            'neighborhood bar with small plates in the United States'),
        (14, 'AI Chef Pro'), (15, 'aichef.pro'), (16, 'US edition with UK notes · 2026'),
        (18, 'LEGAL NOTICE'), (19, M.AVISO_DOCX_EN), (20, '© 2026 AI Chef Pro — aichef.pro'), (22, 'CONTENTS'),
        (35, 'Appendices: Bar Financial Projections (Excel) + Bar Opening Checklist (Excel)'),
        (124, 'AI Chef Pro'), (125, 'Templates and AI tools for food businesses'), (127, 'aichef.pro\ninfo@aichef.pro'),
        (129, '→ %s · %s' % tuple(pc[:2])), (130, '→ ' + pc[2]), (131, '→ ' + pc[3]), (132, '\n' + M.URL_TIENDA),
    ])
    return OrderedDict([('bar', d)])


DOCX_NOTAS_PLAN = OrderedDict([
    ('bar', 'Concepto (D51): NEIGHBORHOOD BAR WITH SMALL PLATES — bar de barrio con cócteles, cerveza de grifo y vino y '
            'una cocina corta de small plates para compartir; ~65 % de las ventas en bebida ({{bebida_pct}}), 60 '
            'plazas ({{aforo}}, 14 en barra) + patio, 7 días de tarde a noche. «Tapas» SOLO como «small plates '
            '(tapas-style)» la primera vez; nunca «tapas bar» ni «gastrobar». Volumen diario = «guests (covers)» la '
            'primera vez y después «covers»; nunca «customers» para el volumen. Las cifras del docx ES (115.000 €, '
            '100.000-140.000 €, 270.000 €, 320.000 / 370.000, 34 clientes a 18 €, 1,8 servicios, 12.000 € de fondo de '
            'maniobra, retorno 18-30 meses) CONTRADICEN al Excel (I1-BAR): no se traducen ni se convierten; cada cifra '
            'del caso va con su token {{…}} y las de mercado solo si están en research/SPEC con fuente. Vermú, '
            'afterwork, turismo gastronómico y cultura del tapeo españoles → su equivalente US sin cifra (happy hour, '
            'neighborhood regulars) o fuera. El cierre (productos) lo escribe el ensamblador'),
])
DOCX_NOTAS = OrderedDict([
    ('bar', OrderedDict([
        (41, '§1: la inversión y su reparto SOLO con tokens ({{inversion_total}}, {{capex}}, {{fondo_maniobra}}, '
             '{{inv_licencia}}…); fuera «115.000 €» y «100.000-140.000 € habituales» (I1-BAR). Como contexto de '
             'mercado, la encuesta de RestaurantOwner.com ($110,000-$550,000 en local alquilado, media $425,500; '
             'research §4)'),
        (42, '§1: ventas, ticket, cubiertos y rotaciones con tokens ({{ventas_a1}}, {{clientes_dia}}, {{ticket}}, '
             '{{rotaciones_dia}}); fuera «270.000 €» y «1,8 servicios por cubierto»'),
        (55, '§3: gasto medio → el ticket del caso ({{ticket}} sin impuesto, {{precio_menu}} con él); ningún dato de '
             'gasto medio de mercado sin fuente en research'),
        (57, '§3: la «cultura del vermú» española → cócteles y happy hour en EE. UU., redacción cualitativa (sin cifras '
             'de tendencia sin fuente)'),
        (59, '§3: competencia y oportunidad: fuera «100.000-140.000 €»; fuentes posibles de research §4-§5 (Restaurant365 '
             '$100,000-$850,000+, BevSpot pour cost 18-24 %)'),
        (82, '§6: equipamiento: cocina corta (griddle, fryer, oven), barra con underbar stations, draft system (líneas, '
             'glycol; lo instala el distribuidor), Type I hood + grease interceptor'),
        (83, '§6: proveedores = three-tier system (compras a distribuidores con licencia); tied-house rules limitan lo '
             'que un fabricante te da gratis (sustituye «exclusividad de cerveza por grifos gratis»)'),
        (85, '§6: control de inventario de barra: pour cost por categoría (BevSpot: cerveza 24 %, destilados 15 %, vino '
             '28 %; total 18-24 %), inventario semanal, merma; el libro usa {{food_cost_bebida}} de coste de bebida'),
        (89, '§7: la plantilla del libro: {{plantilla_puestos}} personas = {{plantilla_jornadas}} FTE; puestos de '
             'Staffing (owner / general manager, kitchen lead, bartenders, servers, line / prep cook, barback / weekend '
             'extra, relief cover)'),
        (93, '§7: costes laborales US: employer payroll taxes {{cargas_pct}}; mínimo federal ({{salario_minimo_federal}} '
             'al año a jornada completa) + el estatal; el libro NO modela tip credit ni propinas (bartenders y servers '
             'con salario base ≥ $15/h); federal $2.13/h + tip credit hasta $5.12 donde el estado lo permite; CA, OR, WA, '
             'AK, MN, MT y NV no lo permiten (DOL). Fuera «33 %» y «14 pagas»'),
        (98, '§8: inversión y financiación con tokens ({{inversion_total}}, {{capex}}, {{fondo_maniobra}}, '
             '{{necesidad_caja}}, {{fondos_propios}}, {{prestamo}}, {{tipo_prestamo}}, {{plazo_prestamo}}); fuera '
             '115.000 €'),
        (99, '§8: ventas años 1-3 ({{ventas_a1}}, {{ventas_a2}}, {{ventas_a3}}), mezcla comida/bebida ({{comida_pct}} / '
             '{{bebida_pct}}), coste de mercancía y margen bruto con tokens'),
        (100, '§8: estructura de costes: COGS {{cogs_pct}} (solo comida + bebida; los consumibles, la tarjeta y los '
              'imprevistos van aparte), personal {{personal_pct}}, alquiler {{ocupacion_pct}}, prime cost '
              '{{prime_cost_pct}}; el pour cost manda (riesgo §8.2 de la SPEC)'),
        (101, '§8: equilibrio con tokens ({{equilibrio_clientes_dia}} / {{equilibrio_caja_clientes_dia}} covers al día, '
              '{{holgura_caja_pct}} de holgura); fuera «treinta y cuatro clientes» (D52)'),
        (102, '§8: escenarios con tokens (cubiertos, ticket, días, ingresos, resultado y caja estimada de cada extremo)'),
        (106, 'D61 §9 1/5: el marco US por niveles (federal, estatal, condado, ciudad); LLC + EIN gratis en el IRS; '
              "seller's permit / sales tax registration; business license; zoning check ANTES de firmar el lease; "
              'building permits de la obra → certificate of occupancy (sustituye la licencia de apertura)'),
        (107, '§9 2/5: LIQUOR LICENSE (camino crítico): agencia estatal (ABC / control board) + aprobación local; '
              'clases beer & wine (desde ~$3,000) y full liquor ($12,000-$400,000); en estados con cupo se compra o '
              'transfiere una licencia existente a precio de mercado (Boston > $450,000); el libro presupuesta '
              '{{inv_licencia}} como ejemplo de estado SIN cupo; pídela al firmar el local: a menudo 3-12 meses; una '
              'licencia comprada es un activo intangible: «ask your CPA» (sustituye inocua / clasificada)'),
        (108, '§9 3/5: health department plan review → food establishment permit + inspección; Certified Food '
              'Protection Manager + food handler cards; FDA Food Code adoptado por el estado; 9 alérgenos mayores; '
              'cocina: Type I hood con supresión UL 300 (NFPA 96) + grease interceptor + fire marshal (sustituye el '
              'RGSEAA)'),
        (109, '§9 4/5: dram shop / liquor liability (el local puede responder del daño de un cliente servido en exceso; '
              'mediana de $2,039/año en bares pequeños, Insureon; el libro presupuesta {{seguros_anual}} con general '
              'liability + liquor liability + property); servicio responsable (TIPS / ServSafe Alcohol) y control de '
              'edad; sidewalk café / patio permit (sustituye la licencia de terraza)'),
        (110, '§9 5/5: música (ASCAP / BMI / SESAC) + entertainment permit si hay música en vivo o DJ + noise ordinance; '
              'horario y last call los fija el estado y a menudo la ciudad (parámetro, sin cifra); y, como ÚLTIMA frase '
              'o frases, la nota UK: premises licence + personal licence (Licensing Act 2003), registro del negocio de '
              'alimentos en el council 28 días antes de abrir, Food Hygiene Rating (FHIS en Escocia), VAT 20 % en el '
              'local, 14 alérgenos'),
        (116, '§10: hoja de ruta en el orden del checklist (73 tareas en 6 fases): la licencia de alcohol se pide en la '
              'fase 2, al firmar el local; fuera «lokal» y la constitución de una SL'),
    ])),
])

# ==========================================================================
# Pistas por celda (las lee extraer_textos.py → textos_es.json → tandas)
# ==========================================================================
_A8 = ('SPEC §4.1 línea 4: sin divisores 1,10/1,21 → «divide a menu price by 1 + your sales tax rate»; P&L excl. '
       'sales tax, cash flow incl.')
_CASO = ('D52: caso US = 95 covers/día × $27 (sin sales tax) × 360 días, bebida 65 %, 60 plazas; sin historia de '
         'versiones («v1.1», «el documento de este plan») ni cifras del docx ES')
CELDA_PISTAS = OrderedDict([
    (('BARP', _S, 'A2'), 'D8: añade una vez que los importes van «in your currency» (sin símbolo)'),
    (('BARP', _S, 'C4'), _CASO + '; rotaciones implícitas = cubiertos ÷ plazas (celda B50): compáralas con el techo '
                                 'de "Break-Even"'),
    (('BARP', _S, 'C5'), _CASO + '; el ticket es SIN sales tax; el precio de carta con impuesto lo calcula la fila '
                                 '"Menu price incl. sales tax"'),
    (('BARP', _S, 'C6'), _CASO + '; 360 días = 7 días a la semana menos ~5 festivos'),
    (('BARP', _S, 'C62'), 'D57: alcohol = 90 % de las ventas de bebida en el ejemplo US (cócteles, cerveza y vino; el '
                          'resto, sin alcohol)'),
    (('BARP', _S, 'C63'), 'D57: «some states add a tax on drinks served on premises; e.g. Texas: 8.25% mixed beverage '
                          'sales tax (customer) + 6.7% gross receipts tax (paid by the bar): put the first here and add '
                          'the second to your beverage cost %»'),
    (('BARP', _N, 'A8'), _A8),
    (('BARP', _N, 'A12'), 'SPEC §4.1 línea 8 (I1): el Word del kit usa las MISMAS cifras de ejemplo que este libro; si '
                          'cambias el libro, actualiza las cifras del Word (fuera «versión 1.1»)'),
    (('BARP', 'Tesorería 12 meses', 'O5'), 'SPEC §4.1: estacionalidad «your area» (sin agosto/costa de España)'),
    (('BARP', _I, 'D8'), 'D54 nota de la fila 8: «beer & wine from ~$3,000; full liquor $12,000-$400,000; in quota '
                         'states you buy an existing license at market price» (esta fila = ejemplo de estado SIN cupo); '
                         'una licencia comprada a otro dueño es un activo intangible: «ask your CPA»'),
])
for _f in list(range(7, 25)):
    CELDA_PISTAS.setdefault(('BARP', _I, 'D%d' % _f), 'D54: nota de la partida del ejemplo US (rótulo fijado de la col. A '
                                                       'en "fijos_en"); sin rangos, marcas ni normas españolas: solo '
                                                       'rangos con fuente de research §4 o ninguno')
# Tabla D19 (Instrucciones 54-69): «US INDUSTRY BENCHMARKS» (Benchmark | Value | Source | Note). D58: las filas sin
# fuente (ocupación, merma, consumiciones de barra, retorno, EBITDA) se SUSTITUYEN; Source real o «Kit estimate»
_D19 = OrderedDict([
    (54, 'D58 fila → «Food cost (small plates)» · «25-35% of food sales» · el mismo Source que la fila de food cost '
         'del Restaurant (BP2) · nota: cocina corta, aprovechamiento'),
    (55, 'D58 fila → «Pour cost, whole bar» · «18-24%» (mediana «just above 20%») · «BevSpot (bevspot.com)» · nota: '
         'el coste de bebida del ejemplo (fila "Beverage cost" de "0. Assumptions") suma garnish y merma'),
    (56, 'D58 fila → «Beer pour cost (median)» · «24%» · «BevSpot (bevspot.com)» · nota: el grifo (draft) baja el coste '
         'frente a la botella si las líneas se limpian y se controla la merma'),
    (57, 'D58 fila → «Labor cost / sales» · «≤ 35%» · «Kit estimate» · nota: incluye barbacks y extras de fin de semana; '
         'sin propinas'),
    (58, 'D58 fila → «Rent / sales» · «≤ 10%» · «Kit estimate» · nota: el umbral del semáforo del P&L'),
    (59, 'D58 fila → «Average check per guest» · «$20-$35 excl. sales tax» · «Kit estimate» · nota: small plates + '
         'drinks; el precio con impuesto de ESTE plan lo calcula "0. Assumptions"'),
    (60, 'D58 fila (sustituye «ticket gastrobar») → «Spirits pour cost (median)» · «15%» · «BevSpot (bevspot.com)» · '
         'nota: cócteles con receta estandarizada y jigger'),
    (61, 'D58 fila (sustituye «consumiciones de barra», sin fuente) → «Wine pour cost (median)» · «28%» · «BevSpot '
         '(bevspot.com)» · nota: vino por copa: controlar la botella abierta'),
    (62, 'D58 fila → «Seat turns per day» · «1.5-3» · «Kit estimate» · nota: es el techo por defecto de "Break-Even": '
         'ajústalo a tu horario y aforo'),
    (63, 'D58 fila (sustituye «ocupación entre semana», sin fuente) → «Startup costs, bar in a leased space» · '
         '«$110,000-$550,000 (survey average $425,500)» · «RestaurantOwner.com survey, via Poster (joinposter.com)» · '
         'nota: compara con el CAPEX de "Startup Costs"'),
    (64, 'D58 fila (sustituye «ocupación fin de semana», sin fuente) → «Liquor license» · «beer & wine from ~$3,000; '
         'full liquor $12,000-$400,000» · «Poster (joinposter.com)» · nota: en estados con cupo se compra una licencia '
         'existente a precio de mercado; este libro presupuesta un estado sin cupo'),
    (65, 'D58/D56 fila → «Gross margin target» · «≥ 68%» · «Kit benchmark (editable estimate)» · nota: el umbral del '
         'semáforo del P&L'),
    (66, 'D58 fila (sustituye «EBITDA objetivo», sin fuente) → «Liquor liability insurance (small bars)» · «median '
         '$2,039 a year» · «Insureon (insureon.com)» · nota: muestra de bares pequeños; un local de este tamaño paga '
         'más: el ejemplo presupuesta general + liquor liability + property juntos'),
    (67, 'D58 fila (sustituye «retorno 18-30 meses», sin fuente) → «Operating cash reserve» · «$75,000-$100,000 or six '
         'months of costs» · «RestaurantOwner.com survey, via Poster (joinposter.com)» · nota: compárala con el fondo de '
         'maniobra de "Startup Costs"'),
    (68, 'D58 fila (sustituye «merma media», sin fuente) → «Prime cost (cost of goods + labor)» · «60-65% of sales '
         '(full-service)» · «Restaurant365 (restaurant365.com)» · nota: un bar queda algo por debajo porque la bebida '
         'cuesta menos que la comida'),
    (69, 'D58 fila 69 → «Minimum wage floor» · «federal $7.25/h + your state» · «U.S. Department of Labor (dol.gov)» · '
         'nota: teclea el suelo de tu estado en "0. Assumptions"; sin convenio'),
])
for _f, _p in _D19.items():
    for _col in 'ABCD':
        CELDA_PISTAS[('BARP', _N, '%s%d' % (_col, _f))] = _p
# Checklist (SPEC delta §4, D60): equivalencias US por celda (la celda ES → su tarea US)
_CK = [
    ('F1 - Constitución', ('B5', 'E5'), 'D60: «LLC vs S corp with your accountant»'),
    ('F1 - Constitución', ('B9', 'E9'), 'D60: «EIN + state payroll / unemployment registration»; los dueños de una LLC '
                                        'no van en nómina (draws + self-employment tax)'),
    ('F1 - Constitución', ('E15',), 'D60: «POS that reports sales tax correctly» (sin Veri*factu ni RD)'),
    ('F2 - Local', ('B7', 'E7'), 'D60: «Zoning check before signing» (confirm bar / restaurant use and any '
                                 'distance rules for alcohol)'),
    ('F2 - Local', ('B8', 'E8'), 'D60: LIQUOR LICENSE: «apply right after signing the lease» (state alcohol agency + '
                                 'local approval; quota states: buy / transfer an existing license); responsable '
                                 'Owner + attorney (lección M1 de BP2: nunca un trámite de un día)'),
    ('F2 - Local', ('B9', 'E9'), 'D60: «Sidewalk café / patio permit» (renovación según la ciudad); sin «facturación '
                                 'extra 20-30 %» (sin fuente)'),
    ('F2 - Local', ('B10', 'D10', 'E10'), 'D60: «Entertainment permit if live music or DJ» (local)'),
    ('F2 - Local', ('E11',), 'D60: general liability + liquor liability (dram shop): la pide el estado o la aseguradora '
                             'con la licencia; sin «300.000 €»'),
    ('F2 - Local', ('B13', 'E13'), 'D60: «Noise ordinance check (residential neighbors)»'),
    ('F3 - Equipamiento', ('B5', 'E5'), 'D60: «Architect + MEP drawings → building permits + health department plan '
                                        'review»'),
    ('F3 - Equipamiento', ('B7',), 'D14/D60: sin kW españoles: «Electrical service sized for the kitchen line and bar '
                                   'coolers»'),
    ('F3 - Equipamiento', ('B8', 'E8'), 'D60: «Type I hood + UL 300 suppression (NFPA 96)»'),
    ('F3 - Equipamiento', ('B9', 'E9'), 'D60: «Grease interceptor (plumbing review)»'),
    ('F3 - Equipamiento', ('B11', 'C11', 'E11'), 'D60: «Draft system: distributor install (lines, glycol)»; '
                                                 'tied-house rules limit what a brewer can give you free; sin marcas '
                                                 'españolas (Mahou, Estrella)'),
    ('F4 - Personal', ('E8',), 'D60: «Offer letters, I-9, W-4; state minimum wage» (sin convenio provincial)'),
    ('F4 - Personal', ('B9',), 'D60: «New-hire reporting» (state)'),
    ('F4 - Personal', ('B11',), 'D60: «OSHA basics»'),
    ('F4 - Personal', ('B13', 'E13'), 'D60: «Bar service + responsible beverage service certification (TIPS / ServSafe '
                                      'Alcohol)»; age-ID checks'),
    ('F4 - Personal', ('B14', 'E14'), 'D60: «Allergen + food safety (Food Code)»; 9 alérgenos mayores US (UK 14)'),
    ('F5 - Marketing', ('B13', 'E13'), 'D60: «Distributor accounts (beer, wine, spirits) — three-tier system: you buy '
                                       'from licensed distributors»; sin «exclusividad por grifos gratis»'),
    ('F5 - Marketing', ('B14', 'E14'), 'D60: «Google, Yelp, OpenTable / Resy»'),
]
for _h, _celdas, _p in _CK:
    for _c in _celdas:
        CELDA_PISTAS[('BARC', _h, _c)] = _p

# Pistas por TEXTO propias del bar (se suman a las de extraer_textos.PISTAS)
PISTAS_EXTRA = [
    (r'[Cc]ubiertos?|comensales|rotaci', 'D55: el libro dice «covers» (cubiertos) y «seat turns»; nunca «customers» '
                                         'para el volumen diario'),
    (r'[Tt]apas?\b|[Rr]aciones|[Gg]astrobar', 'D51: «small plates» («small plates (tapas-style)» solo la primera vez en '
                                              'el docx); nunca «tapas bar» ni «gastrobar»'),
    (r'[Vv]ermut|vermú', 'D51: vermouth / cocktails; sin «hora del vermut» española'),
    (r'[Tt]iraje|[Gg]rifos?', 'Glosario: tiraje → «pouring / draft service»; grifos → «draft lines / taps»'),
    (r'[Bb]arra\b', 'Glosario: barra → «bar» (la del local); camarero de barra → «bartender»; ayudante → «barback»'),
    (r'[Pp]ropina|[Cc]amarer', 'D38: sin tip credit en el libro (≥ $15/h); nota federal $2.13/h + tip credit donde el '
                               'estado lo permite'),
    (r'alcohol|[Bb]ebida ALCOH|licencia de alcohol', 'D57/D60: liquor license (state + local; quota states); dram shop '
                                                     '/ liquor liability; responsible beverage service (TIPS / ServSafe '
                                                     'Alcohol)'),
    (r'Glovo|Uber Eats|delivery', 'D60: DoorDash / Uber Eats SOLO para la comida (el reparto de alcohol depende de la '
                                  'ley del estado)'),
    (r'TripAdvisor|TheFork', 'D60: Google, Yelp, OpenTable / Resy'),
    (r'Mahou|Estrella|craft', 'D60: sin marcas españolas; distribuidores con licencia (three-tier system)'),
    (r'SGAE|AGEDI', 'D55: «Music licensing (ASCAP/BMI/SESAC)»'),
]

# Glosario del bar (se suma al de FT/CAF y al del financial-kit, que mandan)
GLOSARIO_BAR = OrderedDict([
    ('cubiertos/día', 'covers per day'), ('tapas / raciones', 'small plates'), ('barra', 'bar'),
    ('camarero/a de barra', 'bartender'), ('ayudante de barra', 'barback'), ('camarero/a de sala', 'server'),
    ('terraza', 'patio / sidewalk café'), ('grifos de cerveza', 'draft beer system / taps'),
    ('tiraje', 'pouring / draft service'), ('coste de bebida', 'pour cost / beverage cost'),
    ('licencia de alcohol', 'liquor license'), ('RC por alcohol', 'liquor liability (dram shop) insurance'),
    ('servicio responsable de alcohol', 'responsible beverage service (TIPS / ServSafe Alcohol)'),
    ('distribuidor', 'licensed distributor (three-tier system)'), ('comandero', 'handheld POS'),
    ('vermut', 'vermouth'), ('cóctel', 'cocktail'),
])


# ==========================================================================
# Caso de ejemplo US (D52; F1-research-us-delta §8): celdas VERDES. (corto, hoja ES, celda) → (valor, rótulo)
# ==========================================================================
def valores_bar(M):
    v = OrderedDict()
    sup = [
        ('B4', 95, 'Cubiertos/día'), ('B5', 27, 'Ticket medio'), ('B6', 360, 'Días de apertura'),
        ('B7', 0.15, 'Crecimiento de volumen del año 2'), ('B8', 0.10, 'Crecimiento de volumen del año 3'),
        ('B11', 0.35, 'Ventas de COMIDA'), ('B13', 0.30, 'Coste de mercancía sobre las ventas de COMIDA'),
        ('B14', 0.22, 'Coste de mercancía sobre las ventas de BEBIDA'), ('B15', 0.01, 'Consumibles'),
        ('B16', 0, 'Ventas por delivery'), ('B17', 0.25, 'Comisión de la plataforma'),
        ('B18', 0.035, 'Comisión de los medios de pago'), ('B20', 0.10, 'Seguridad Social'),
        ('B21', 12, 'Número de pagas'), ('B22', 15080, 'SMI anual'), ('B24', 6500, 'Alquiler mensual'),
        ('B25', 2, 'Fianza'), ('B26', 2000, 'Suministros'), ('B27', 12000, 'Seguros'), ('B28', 0.01, 'Varios'),
        ('B30', 120000, 'Recursos propios'), ('B31', M.CALIBRAR, 'Préstamo bancario'), ('B32', 0.10, 'Tipo de interés'),
        ('B33', 10, 'Plazo del préstamo'), ('B34', 0, 'Carencia'), ('B35', 3, 'Fondo de maniobra'),
        ('B37', 0.25, 'Impuesto de Sociedades, nueva'), ('B38', 0.25, 'Impuesto de Sociedades, tipo'),
        ('B39', 0.08, 'IVA repercutido de restauración'), ('B40', 0.08, 'IVA repercutido/soportado'),
        ('B41', 0, 'IVA soportado en compras'), ('B42', 0, 'Bases negativas'),
        ('B44', 10, 'Vida útil de obra'), ('B45', 7, 'Vida útil de maquinaria'),
        ('B51', 60, 'Aforo'), ('B52', 0.55, 'Actividad del mes 1'), ('B53', 6, 'Meses hasta alcanzar'),
        ('B54', 2, 'Meses de alquiler ANTES'), ('B55', 0.10, 'Imprevistos sobre las partidas de OBRA'),
        # B58: el ES trae 0, que viola su propia DV (1-365); US: el abono de tarjeta llega el día hábil siguiente
        ('B58', 1, 'Días medios de cobro'), ('B59', 14, 'Días medios de pago'),
        ('B62', 0.90, 'Bebida ALCOHÓLICA'), ('B63', 0.08, 'IVA de la bebida ALCOHÓLICA'),
        ('B65', 1.15, 'DSCR mínimo'), ('B66', 1.25, 'DSCR objetivo'), ('B67', 0.15, 'Holgura mínima'),
        ('B68', None, 'Suelo salarial anual'),
    ]
    for c, val, rot in sup:
        v[('BARP', _S, c)] = (val, rot)
    # Inversión (D54; research §8): las 18 partidas tecleadas, filas 7-24
    for k, val in enumerate([2500, 15000, 15000, 70000, 22000, 28000, 20000, 18000, 35000, 14000, 15000, 6000, 8000,
                             18000, 5000, 7000, 15000, 5000]):
        v[('BARP', _I, 'B%d' % (7 + k))] = (val, None)
    # P&L: fijos tecleados B26-B34 (research §8) y umbrales D56 [kit benchmark]
    for k, val in enumerate([6000, 8000, 15000, 4800, 7200, 3000, 1200, 3000, 1000]):
        v[('BARP', _P, 'B%d' % (26 + k))] = (val, None)
    for c, val, rot in [('E50', 0.68, 'Margen bruto'), ('E52', 0.28, 'Coste de mercancía /'),
                        ('E53', 0.35, 'Coste de personal'), ('E54', 0.10, 'Alquiler'), ('E55', 0.05, 'Resultado neto')]:
        v[('BARP', _P, c)] = (val, rot)
    # Staffing (research §8): personas (B), FTE por persona (C), bruto mes TOTAL de la fila (D); ≥ $15/h, sin propinas
    for f, (b, c, d) in zip(range(5, 12), [(1, 1.0, 5000), (1, 1.0, 4200), (3, 0.7, 6188), (2, 0.5, 2600),
                                           (1, 0.8, 2496), (2, 0.4, 2080), (1, 0.3, 832)]):
        for col, val in zip('BCD', (b, c, d)):
            v[('BARP', _R, '%s%d' % (col, f))] = (val, None)
    v.update([
        (('BARP', _R, 'B14'), (6000, 'Coste anual')), (('BARP', _R, 'B15'), (6000, 'Coste anual')),
        (('BARP', _R, 'B19'), (40, 'Jornada completa')), (('BARP', _R, 'B20'), (50, 'Semanas')),
        (('BARP', _R, 'B21'), (9, 'Horas de servicio')), (('BARP', _R, 'B22'), (3.5, 'Personas necesarias')),
        (('BARP', _R, 'B23'), (3, 'Horas de producción')), (('BARP', _R, 'B24'), (2, 'Personas en el turno')),
    ])
    # Escenarios (research §8): la lógica del ES (−25 % / +25 % de cubiertos, −2 / +2 de ticket) sobre el caso US;
    # días 340 / 360
    v.update([
        (('BARP', 'Escenarios', 'B5'), (71, 'Cubiertos/día')), (('BARP', 'Escenarios', 'D5'), (119, 'Cubiertos/día')),
        (('BARP', 'Escenarios', 'B6'), (25, 'Ticket')), (('BARP', 'Escenarios', 'D6'), (29, 'Ticket')),
        (('BARP', 'Escenarios', 'B7'), (340, 'Días')), (('BARP', 'Escenarios', 'D7'), (360, 'Días')),
    ])
    return v


# Calibración D15 (paso 3 de la F2: aplicar_en real). Cada celda, citada en F2-NOTAS.md (G7). Vacía de momento
CALIBRACION_D15 = OrderedDict()


def formulas_bar():
    p = os.path.join(AQUI, 'formulas_bar.json')
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
    M.TOKENS_DOCX = tokens_bar(M.TOKENS_DOCX)
    M.DOCX_FIJOS = docx_fijos(M)
    M.DOCX_NOTAS = DOCX_NOTAS
    M.DOCX_NOTAS_PLAN = DOCX_NOTAS_PLAN
    M.FORMULAS_EN = formulas_bar()
    M.VALORES_EN = valores_bar(M)
    M.CALIBRACION_D15 = CALIBRACION_D15
    M.CELDA_PISTAS = CELDA_PISTAS
    M.PISTAS_EXTRA = PISTAS_EXTRA
    M.CIFRAS_PROHIBIDAS = CIFRAS_PROHIBIDAS
    glo = OrderedDict(M.GLOSARIO)
    for k, val in GLOSARIO_BAR.items():
        glo.setdefault(k, val)
    M.GLOSARIO = glo
