#!/usr/bin/env python3
"""
datos_cat.py — Catering Business Plan Kit (EN) · los datos ES→EN que dependen del contenido: rótulos fijados (D72-D74),
POR_CELDA, pistas (D18/D19, notas del caso, las 68 tareas del checklist D77), tokens del docx (D78), fijos y notas del
docx, caso US (D70; research §8), FORMULAS_EN (D72), cifras ES prohibidas y vocabulario del food truck (D70, D72) y
glosario de catering. Lo llama `mapas_cat.instalar()` con el módulo `mapas` YA cargado con los datos de FT/CAF (motor
2.2), de los que parte. La fuente ES del circuito es el FOOD TRUCK ES: los rótulos ES de abajo son los del FT.
Sesión Claude Code, 11-oct-2026 (F2, paso 1).
"""
import json
import os
import sys
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
BP = os.path.join(os.path.dirname(AQUI), 'business-plans-en')

URL_CAT = 'aichef.pro/en/digital-products/catering-business-plan'
_I, _S, _P, _R, _N, _E, _ES, _T = ('Inversión Inicial', '0. Supuestos', 'PyG 3 Años', 'Personal', 'Instrucciones',
                                   'Punto Equilibrio', 'Escenarios', 'Tesorería 12 meses')

# ==========================================================================
# FIJOS (por TEXTO ES del FT: valen en cualquier celda de los 2 libros) y POR_CELDA (solo esa celda)
# ==========================================================================
FIJOS_FUERA = ('Este fichero forma parte del producto «plan-negocio-cafeteria» de AI Chef Pro.',)
_TITULO_CHECK = 'CATERING STARTUP CHECKLIST — FULL-SERVICE EVENT CATERER'
FIJOS_NUEVOS = OrderedDict([
    # D68 / I5: Instrucciones!A3 del checklist con el nombre comercial (el ES es el del food truck)
    ('Este fichero forma parte del producto «plan-negocio-food-truck» de AI Chef Pro.',
     'This file is part of the Catering Business Plan Kit by AI Chef Pro.'),
    # D77: título del checklist y fase 2 (el título de hoja no tiene el límite de 31 de la pestaña)
    ('CHECKLIST APERTURA — FOOD TRUCK', _TITULO_CHECK),
    ('FASE 2: VEHÍCULO Y PERMISOS', 'PHASE 2: KITCHEN, VAN & PERMITS'),
    ('INSTRUCCIONES DE USO — Plan financiero Food Truck', 'HOW TO USE THIS WORKBOOK — Catering Financial Projections'),
    ('PLAN DE NEGOCIO: FOOD TRUCK', 'BUSINESS PLAN: FULL-SERVICE EVENT CATERER'),
    ('Ajusta las cifras a tu proyecto.', 'US kit example (2026) — replace with your own quotes.'),
    ('Escenario realista — Food Truck urbano', 'Base case — full-service event caterer'),
    ('Break-even — Food Truck', 'Break-even — Event Catering'),
    # D75: cabecera de la tabla D19
    ('DATOS DE REFERENCIA DEL SECTOR', 'US CATERING BENCHMARKS (sourced) AND KIT ESTIMATES'),
    # D72: el motor permutado (B4 = eventos/año, B5 = precio por invitado, B6 = invitados por evento) en TODAS las
    # hojas que citan esos rótulos (Supuestos, P&L, Break-Even, Escenarios)
    ('Ticket medio SIN IVA (€)', 'Average price per guest (excl. sales tax, service included)'),
    ('PVP equivalente con IVA (calculado)', 'Price per guest incl. sales tax (calculated)'),
    ('Ticket medio sin IVA', 'Average price per guest (excl. sales tax)'),
    ('Clientes/día (media del año 1)', 'Events per year (year-1 average)'),
    ('Clientes/día (media)', 'Events per year (average)'),
    ('Clientes/día', 'Events per year'),
    ('Días de apertura al año', 'Average guests per event'),
    ('Coste variable por cliente', 'Variable cost per guest'),
    ('Margen de contribución por cliente', 'Contribution margin per guest'),
    ('Ticket menos coste variable unitario', 'Price per guest minus variable cost per guest'),
    ('Clientes necesarios al año', 'Guests needed per year'),
    ('Clientes necesarios al día', 'Events needed per year'),
    ('Clientes necesarios al año (caja)', 'Guests needed per year (cash)'),
    ('Clientes necesarios al día (caja)', 'Events needed per year (cash)'),
    ('Clientes/día previstos en el plan', 'Events per year in the plan'),
    ('Clientes/día para el equilibrio', 'Events per year to break even'),
    ('Clientes al año por jornada equivalente', 'Guests per year per full-time equivalent'),
    # D74: el canal de «delivery» del FT es el marketplace de catering corporativo (B16/B17)
    ('Comisiones de delivery', 'Corporate marketplace commissions'),
])

POR_CELDA = OrderedDict([
    # 0. Supuestos (D72, D74)
    (('CATP', _S, 'A16'), 'Corporate catering marketplace share of sales (e.g. ezCater)'),
    (('CATP', _S, 'A17'), 'Marketplace commission on those sales'),
    (('CATP', _S, 'A23'), 'COMMISSARY KITCHEN AND FIXED COSTS'),
    (('CATP', _S, 'A24'), 'Commissary kitchen (hours + storage) & van parking, per month'),
    (('CATP', _S, 'A25'), 'Commissary deposit (months)'),
    (('CATP', _S, 'A44'), 'Useful life of the van and its upfit (years)'),
    (('CATP', _S, 'A51'), 'Max events a year your kitchen and crew can handle'),
    (('CATP', _S, 'A54'), 'Months of commissary rent BEFORE opening'),
    (('CATP', _S, 'A55'), 'Contingency on the van, upfit and fit-out lines (%)'),
    # Startup Costs filas 7-23 (D74; research §8)
    (('CATP', _I, 'A7'), 'Refrigerated cargo van (used)'),
    (('CATP', _I, 'A8'), 'Van upfit (racks, shelving, wrap)'),
    (('CATP', _I, 'A9'), 'Kitchen and refrigeration equipment (own)'),
    (('CATP', _I, 'A10'), 'Portable cooking and power (induction, burners, generator)'),
    (('CATP', _I, 'A11'), 'Van refrigeration unit + install'),
    (('CATP', _I, 'A12'), 'Commissary storage fit-out'),
    (('CATP', _I, 'A13'), 'LLC formation and legal'),
    (('CATP', _I, 'A14'), 'First-year permits and licenses'),
    (('CATP', _I, 'A15'), 'Health plan review (only if you lease your own kitchen)'),
    (('CATP', _I, 'A16'), 'Catering software + card reader'),
    (('CATP', _I, 'A17'), 'Smallwares, hotel and sheet pans'),
    (('CATP', _I, 'A18'), 'Opening inventory'),
    (('CATP', _I, 'A19'), 'Website, photography, launch marketing'),
    (('CATP', _I, 'A20'), 'Chafing dishes, insulated carriers, serving ware'),
    (('CATP', _I, 'A21'), 'Commissary deposit'),
    (('CATP', _I, 'A22'), 'Commissary rent before opening'),
    (('CATP', _I, 'A23'), 'Van and fit-out contingency'),
    (('CATP', _I, 'A31'), 'Van, upfit and fit-out (depreciated over the van life)'),
    # 3-Year P&L (D74)
    (('CATP', _P, 'A22'), 'Commissary kitchen rent & van parking'),
    (('CATP', _P, 'A27'), 'Van fuel, maintenance and inspections'),
    (('CATP', _P, 'A34'), 'Food safety and alcohol service training (ServSafe, TIPS)'),
    (('CATP', _P, 'A35'), 'Tastings for prospects'),
    (('CATP', _P, 'A55'), 'Commissary / Sales'),
    (('CATP', _N, 'A20'), 'Commissary / Sales'),
    # Staffing (D73, opción A): 4 puestos, cobertura por evento, nota W-2 / AB5 con la E4
    (('CATP', _R, 'A5'), 'Owner / executive chef & sales'),
    (('CATP', _R, 'A6'), 'Sous chef / kitchen lead'),
    (('CATP', _R, 'A7'), 'Event staff (servers, bartenders, attendants; hourly W-2)'),
    (('CATP', _R, 'A8'), 'Prep cook / driver'),
    (('CATP', _R, 'A15'), 'COVERAGE OF EVENT HOURS'),
    (('CATP', _R, 'A18'), 'Hours per event to cover (production, loading, service, pack-down)'),
    (('CATP', _R, 'A19'), 'People needed per event (average)'),
    (('CATP', _R, 'A20'), 'Event hours to cover per year'),
    (('CATP', _R, 'A24'), 'The gross pay, employer payroll taxes, monthly cost and annual cost columns are TOTALS for the '
                          'row: the event staff row covers all the people in it. Event staff (servers, bartenders, '
                          'attendants) are budgeted as hourly W-2 employees with employer payroll taxes and workers\' '
                          'comp: paying them as 1099 contractors is a misclassification risk (FLSA economic-reality test; '
                          'California AB5 presumes employment). The payroll tax rate and the number of pay periods are '
                          'in the "0. Assumptions" tab.'),
    # 12-Month Cash Flow (D74): Month 1 = mes de apertura; anticipos fuera del modelo
    (('CATP', _T, 'O5'), 'Share of the year\'s events in each month (adds up to 100%). Month 1 = your opening month: '
                         'the example opens in March, so it starts with spring weddings and peaks in October and '
                         'December (holiday parties); to open in another month, rotate the row. Deposits (25-50% when '
                         'the contract is signed) are not modeled: they make your real cash flow better than this sheet.'),
])

# ==========================================================================
# Cifras ES prohibidas (D70: catering ES de línea B), cifras del caso FT EN y vocabulario FT (D72)
# ==========================================================================
def _num(n):
    """302400 → patrón que casa 302,400 · 302.400 · 302 400 · 302400 (y nada pegado a más dígitos)."""
    s = str(n)
    cab, cola = s[:-3], s[-3:]
    return r'(?<![\d.,])' + cab + r'[.,   ]?' + cola + r'(?![\d])'


CIFRAS_PROHIBIDAS = [(_num(n), 'cifra del caso ES de catering (D70)', None)
                     for n in (603700, 303364, 8520, 21410, 54440, 10560, 846720, 2200, 4500, 5500, 11500)]
CIFRAS_PROHIBIDAS += [
    (r'(?i)\b14 events? (?:a|per) month\b', 'equilibrio de la ficha ES (D70: «14 eventos/mes»)', None),
    (r'(?i)\b55\s?%[^.;]{0,30}margin|margin[^.;]{0,30}\b55\s?%', 'margen tecleado del ES (D70: «55 %»)', None),
    (r'(?i)\b(?:110|108) (?:milestones|tasks|steps)\b', 'recuento del checklist ES (L13: «110 hitos»)', None),
    (r'(?i)\b10 validated examples\b|\bvalidated by (?:a|our) (?:lawyer|attorney)\b', 'promesa del ES sin respaldo (L12)',
     None),
    (r'(?i)\b96 (?:validated )?suppliers\b', 'promesa del ES sin respaldo (L14: «96 proveedores»)', None),
    (r'(?i)\b(?:12|twelve) (?:world )?cuisines\b', 'concepto ES multicocina (D69: estaciones temáticas, no 12 cocinas)',
     None),
    (r'\bv1\.1\b|\b[Vv]ersion 1\.1\b', 'historia de versiones (D18: la EN nace en 2.2)', None),
    # D72: gate de vocabulario del food truck = 0 en el kit EN
    (r'(?i)\bper day\b', 'vocabulario FT (D72: «per day»)', None),
    (r'(?i)\boperating days?\b', 'vocabulario FT (D72: «operating days»)', None),
    # excepción: la FRASE sintética de `ensamblar_docx.py --autotest` (código común) dice «customers a day»; no es
    # contenido y no puede aparecer en un docx real
    (r'(?i)(?<!corporate )\bcustomers\b', 'vocabulario FT (D72: «customers» → clients / guests)',
     r'^Synthetic paragraph \d+ of the \w+ plan for the assembly test'),
    (r'(?i)\btrucks?\b', 'vocabulario FT (D72: «truck» → van)', None),
    (r'(?i)\bwindows?\b', 'vocabulario FT (D72: «service window»)', None),
    (r'(?i)\bfestivals?\b', 'vocabulario FT (D72: «festival»)', None),
]


def _cifras_ft():
    """Importes del caso FT EN publicado (≥ 10,000) que no pueden aparecer en el catering (reuso del EN del FT)."""
    p = os.path.join(BP, 'cifras_caso.json')
    out = []
    if not os.path.exists(p):
        return out
    ft = json.load(open(p, encoding='utf-8')).get('ft', {})
    for t, d in ft.items():
        v = d.get('valor')
        if d.get('fmt') == 'usd' and isinstance(v, (int, float)) and abs(v) >= 10000:
            out.append(int(round(abs(v))))
    return sorted(set(out))


# ==========================================================================
# Tokens del docx (D78): los del motor (FT) con descripciones de catering + alias legibles + partidas propias
# ==========================================================================
_DESC = OrderedDict([
    ('clientes_dia', 'EVENTS per year, year 1 (alias heredado: usa {{eventos_a1}})'),
    ('clientes_a2', 'EVENTS per year, year 2 (alias: usa {{eventos_a2}})'),
    ('clientes_a3', 'EVENTS per year, year 3 (alias: usa {{eventos_a3}})'),
    ('ticket', 'average price per guest excl. sales tax (alias: usa {{precio_invitado}})'),
    ('precio_menu', 'price per guest incl. sales tax (alias: usa {{precio_invitado_con_tax}})'),
    ('dias', 'average guests per event (alias: usa {{invitados_evento}})'),
    ('crecimiento_a2', 'growth in EVENTS in year 2'), ('crecimiento_a3', 'growth in EVENTS in year 3'),
    ('consumibles_pct', 'disposables (plates, cutlery, drop-off packaging), % of sales'),
    ('tarjeta_pct', 'card / payment processing fees, % of sales (companies often pay by ACH or check)'),
    ('alquiler_mes', 'commissary kitchen (hours + storage) & van parking, per month'),
    ('suministros_mes', 'utilities per month (most are included in the commissary fee)'),
    ('seguros_anual', 'insurance per year (general liability / BOP + commercial auto + liquor liability)'),
    ('vida_obra', 'useful life of the van and its upfit, years'),
    ('ocupacion_anual', 'commissary kitchen rent & van parking per year'),
    ('ocupacion_pct', 'commissary kitchen rent & van parking, % of sales'),
    ('equilibrio_clientes_dia', 'break-even EVENTS per year, accounting (alias: usa {{equilibrio_eventos}})'),
    ('equilibrio_caja_clientes_dia', 'cash break-even EVENTS per year (alias: usa {{equilibrio_caja_eventos}})'),
    ('pesimista_clientes', 'pessimistic scenario: events per year (alias: usa {{pesimista_eventos}})'),
    ('optimista_clientes', 'optimistic scenario: events per year (alias: usa {{optimista_eventos}})'),
    ('pesimista_ticket', 'pessimistic scenario: price per guest (alias: usa {{pesimista_precio}})'),
    ('optimista_ticket', 'optimistic scenario: price per guest (alias: usa {{optimista_precio}})'),
    ('pesimista_dias', 'pessimistic scenario: guests per event (alias: usa {{pesimista_invitados}})'),
    ('optimista_dias', 'optimistic scenario: guests per event (alias: usa {{optimista_invitados}})'),
    ('inv_vehiculo', 'refrigerated cargo van (used)'), ('inv_adaptacion', 'van upfit (racks, shelving, wrap)'),
    ('inv_equipo_cocina', 'kitchen and refrigeration equipment (own)'),
    ('inv_generador', 'portable cooking and power (induction, burners, generator)'),
    ('inv_permisos', 'first-year permits and licenses'), ('inv_lanzamiento', 'website, photography and launch marketing'),
    ('inv_stock', 'opening inventory'), ('horas_semana', 'full-time hours per week'),
])
_FUERA = ('ventas_dia',)                       # ventas ÷ «días» no significa nada con el motor permutado
_FT = {'clientes_dia': 'Clientes/día (media del año 1)', 'ticket': 'Ticket medio SIN IVA (€)'}
TOKENS_PROPIOS = OrderedDict([
    # alias legibles del motor permutado (las mismas celdas que los tokens heredados)
    ('eventos_a1', ('int', ('fila', _S, 'Clientes/día (media del año 1)', 'B'), 'events per year, year 1')),
    ('eventos_a2', ('int', ('fila', _P, 'Clientes/día (media)', 'C'), 'events per year, year 2')),
    ('eventos_a3', ('int', ('fila', _P, 'Clientes/día (media)', 'D'), 'events per year, year 3')),
    ('precio_invitado', ('usd2', ('fila', _S, 'Ticket medio SIN IVA (€)', 'B'),
                         'average price per guest, excl. sales tax, service included')),
    ('precio_invitado_con_tax', ('usd2', ('fila', _S, 'PVP equivalente con IVA (calculado)', 'B'),
                                 'average price per guest incl. sales tax')),
    ('invitados_evento', ('int', ('fila', _S, 'Días de apertura al año', 'B'), 'average guests per event')),
    ('capacidad_eventos', ('int', ('fila', _S, {'cat': 'Plazas de pie y mesas altas junto al vehículo'}, 'B'),
                           'max events a year the kitchen and crew can handle (information only)')),
    ('marketplace_pct', ('pct0', ('fila', _S, 'Ventas por delivery sobre el total', 'B'),
                         'share of sales through corporate catering marketplaces (e.g. ezCater)')),
    ('marketplace_comision', ('pct0', ('fila', _S, 'Comisión de la plataforma de delivery', 'B'),
                              'marketplace commission on those sales')),
    ('cobro_dias', ('int', ('fila', _S, 'Días medios de cobro', 'B'), 'average collection days')),
    ('horas_evento', ('dec1', ('fila', _R, 'Horas de servicio al día que hay que cubrir', 'B'),
                      'hours per event to cover (production, loading, service, pack-down)')),
    ('personas_evento', ('dec1', ('fila', _R, 'Personas necesarias a la vez en cada franja', 'B'),
                         'people needed per event (average)')),
    ('equilibrio_eventos', ('ceil', ('fila', _E, 'Clientes necesarios al día', 'B'),
                            'break-even events per year (accounting)')),
    ('equilibrio_caja_eventos', ('ceil', ('fila', _E, 'Clientes necesarios al día (caja)', 'B'),
                                 'cash break-even events per year (loan payments in, depreciation out)')),
    ('pesimista_eventos', ('int', ('fila', _ES, 'Clientes/día', 'B'), 'pessimistic scenario: events per year')),
    ('optimista_eventos', ('int', ('fila', _ES, 'Clientes/día', 'D'), 'optimistic scenario: events per year')),
    ('pesimista_precio', ('usd2', ('fila', _ES, 'Ticket medio sin IVA', 'B'), 'pessimistic scenario: price per guest')),
    ('optimista_precio', ('usd2', ('fila', _ES, 'Ticket medio sin IVA', 'D'), 'optimistic scenario: price per guest')),
    ('pesimista_invitados', ('int', ('fila', _ES, 'Días de apertura al año', 'B'), 'pessimistic scenario: guests per event')),
    ('optimista_invitados', ('int', ('fila', _ES, 'Días de apertura al año', 'D'), 'optimistic scenario: guests per event')),
    # partidas de la inversión propias del catering (D74)
    ('inv_frio', ('usd', ('fila', _I, {'cat': 'Instalación gas (si aplica)'}, 'B'), 'van refrigeration unit + install')),
    ('inv_almacen', ('usd', ('fila', _I, {'cat': 'Depósito de agua + aguas residuales'}, 'B'), 'commissary storage fit-out')),
    ('inv_llc', ('usd', ('fila', _I, {'cat': 'Constitución SL + notaría + registro'}, 'B'), 'LLC formation and legal')),
    ('inv_software', ('usd', ('fila', _I, {'cat': 'TPV móvil + datáfono'}, 'B'), 'catering software + card reader')),
    ('inv_menaje', ('usd', ('fila', _I, {'cat': 'Menaje, utensilios, packaging eco'}, 'B'), 'smallwares, hotel and sheet pans')),
    ('inv_menaje_servicio', ('usd', ('fila', _I, {'cat': 'Toldo, mobiliario exterior plegable'}, 'B'),
                             'chafing dishes, insulated carriers, serving ware')),
    # derivadas
    ('ventas_evento', ('usd', ('deriv', lambda c: c['ventas_a1'] / c['clientes_dia']),
                       'average revenue per event, year 1 (excl. sales tax)')),
    ('invitados_a1', ('int', ('deriv', lambda c: c['clientes_dia'] * c['dias']), 'guests served in year 1')),
])


def tokens_cat(base):
    out = OrderedDict()
    for t, (fmt, src, desc) in base.items():
        if t in _FUERA:
            continue
        if src[0] == 'fila':
            _, hoja, rot, col = src
            if isinstance(rot, dict):
                if 'ft' not in rot:
                    continue                               # partidas de la cafetería
                src = ('fila', hoja, {'cat': rot['ft']}, col)
        out[t] = (fmt, src, _DESC.get(t, desc))
    out.update(TOKENS_PROPIOS)
    return out


# ==========================================================================
# Docx (D78): lo que escribe ensamblar_docx.py y las notas para los redactores
# ==========================================================================
def docx_fijos(M):
    pc = M.PRODUCTOS_CIERRE
    d = OrderedDict([
        (6, 'BUSINESS PLAN'), (7, 'Event Catering'),
        (9, 'Complete financial plan, market analysis,\noperations strategy and startup checklist\nto launch a '
            'full-service event catering company in the United States'),
        (14, 'AI Chef Pro'), (15, 'aichef.pro'), (16, 'US edition with UK notes · 2026'),
        (18, 'LEGAL NOTICE'), (19, M.AVISO_DOCX_EN), (20, '© 2026 AI Chef Pro — aichef.pro'), (22, 'CONTENTS'),
        (35, 'Appendices: Catering Financial Projections (Excel) + Catering Pricing Calculator (Excel) + Catering '
             'Startup Checklist (Excel)'),
        (123, 'AI Chef Pro'), (124, 'Templates and AI tools for food businesses'), (126, 'aichef.pro\ninfo@aichef.pro'),
        (127, '→ %s · %s' % tuple(pc[:2])), (128, '→ ' + pc[2]), (129, '→ ' + pc[3]), (130, '\n' + M.URL_TIENDA),
    ])
    return OrderedDict([('cat', d)])


DOCX_NOTAS_PLAN = OrderedDict([
    ('cat', 'ESCRIBES, NO TRADUCES (D78). El «es» de cada párrafo es la RANURA del plan de FOOD TRUCK (sirve solo para '
            'el papel del párrafo y su longitud aproximada): el contenido es de CATERING, desde fuente_es_cat.json '
            '(concepto, mezcla particulares/empresas, política comercial —anticipo, cancelación—, operativa de un evento '
            'en 6 fases, riesgos) y research §1-§6 (F1-research-us-delta.md). Concepto (D69): FULL-SERVICE OFF-SITE '
            'EVENT CATERER desde una cocina comisaria compartida con permiso + una furgoneta refrigerada; empresas entre '
            'semana (drop-off, buffets, recepciones, fiestas de diciembre) y particulares el fin de semana (bodas, '
            'fiestas privadas); estilos drop-off · buffet · family-style · plated · stations; diferencial = '
            'chef-attended themed stations (NO «12 cocinas del mundo»); sin alcohol propio (lo compra el cliente y lo '
            'sirven bartenders certificados). Cifras del caso SOLO con tokens {{…}}; de mercado, solo las de research '
            'con su fuente. Prohibido (gate): «food truck», «truck», «per day», «operating days», «customers» (di '
            'clients / guests; «corporate customers» sí), «window», «festival», «España», «ChefBusiness», las cifras '
            'del ES de catering (603.700, 2.200, 4.500, 5.500, 11.500, «14 eventos/mes», «55 %»), «60+ páginas», «96 '
            'proveedores», «10 ejemplos validados», porcentajes sin fuente. El cierre (productos) lo escribe el '
            'ensamblador'),
])
_N9 = OrderedDict([
    (102, 'D78 §9 1/7: cocina con permiso OBLIGATORIA: el FDA Food Code incluye la «catering operation» entre los food '
          'establishments; CA exige cocina con permiso y acuerdo escrito, prohíbe preparar en casa (fuente: '
          'eldoradocounty.ca.gov, Caterers). Cottage food (solo no perecederos envasados) y el MEHKO de California no '
          'permiten catering. Por eso el plan alquila una cocina comisaria compartida'),
    (103, '§9 2/7: catering / health permit del condado (cuota anual + plan review solo si alquilas cocina propia + '
          'inspección) + Certified Food Protection Manager (p. ej. ServSafe) + food handler cards según estado + plan de '
          'seguridad alimentaria basado en HACCP; 9 alérgenos mayores (sésamo desde 2023)'),
    (104, '§9 3/7: permisos por evento: en eventos comunitarios o públicos el permiso de catering no vale y hace falta '
          'un Temporary Food Facility / temporary event permit; fire marshal para llama abierta, combustible de chafing '
          'y carpas; los venues piden certificado de seguro (COI) y a veces «additional insured»'),
    (105, '§9 4/7: alcohol: por defecto el caterer NO lo vende (exige licencia on-sale + permiso de caterer: TX '
          'Caterer\'s Permit, CA Type 58, autorización por evento). Lo habitual: el cliente compra el alcohol y lo '
          'sirven bartenders certificados (TIPS / TABC) con liquor liability; como opción, la licencia y el dram shop '
          '(en una frase, sin cifras)'),
    (106, '§9 5/7: sales tax: en muchos estados grava TODA la factura de catering (comida, personal, menaje; CA: '
          'cdtfa.ca.gov; NY: TB-ST-110) y el service charge según el estado (CA: el obligatorio tributa; NY: la '
          '«gratuity» separada que va íntegra al personal no; TX: excluido si ≤ 20 % separado y repartido). IRS Rev. '
          'Rul. 2012-18: el service charge obligatorio es SALARIO, no propina; la propina voluntaria va aparte. '
          'Seller\'s permit del estado. Ejemplo del libro: {{sales_tax}}'),
    (107, '§9 6/7: empleo y seguros: personal de eventos en nómina W-2 (servers y bartenders de eventos son casi '
          'siempre empleados: FLSA; California AB5 presume empleo), workers\' comp, I-9 / W-4 / new-hire reporting; '
          'seguros: general liability / BOP + commercial auto + liquor liability ({{seguros_anual}} al año en el '
          'ejemplo; Insureon publica medias por póliza)'),
    (108, '§9 7/7: la furgoneta (registro y título en el DMV, commercial auto; CDL solo con GVWR ≥ 26,001 lb, una '
          'cargo van no lo necesita) y, como ÚLTIMA frase o frases del párrafo, la nota UK: registrar el negocio de '
          'alimentos en el council 28 días antes de empezar (gratis), Food Hygiene Rating 0-5, VAT 20 % en el catering '
          'de eventos (HMRC VAT Notice 709/1), alcohol con Temporary Event Notice (£21, < 500 personas) o premises '
          'licence, 14 alérgenos'),
])
_NOTAS_SECCION = OrderedDict([
    (39, '§1 1/5: la oportunidad: catering de eventos en EE. UU. con dos motores (empresas entre semana; particulares el '
         'fin de semana); demanda con fuente solo de research §2 (p. ej. «wedding catering», «corporate catering»)'),
    (40, '§1 2/5: el concepto (D69): full-service off-site event caterer desde cocina comisaria compartida + furgoneta '
         'refrigerada; estilos de servicio; diferencial de estaciones temáticas atendidas por chef'),
    (41, '§1 3/5: inversión y financiación SOLO con tokens: {{inversion_total}} = {{capex}} + {{fondo_maniobra}}; '
         '{{fondos_propios}} ({{aportacion_pct}}) + préstamo {{prestamo}} al {{tipo_prestamo}} a {{plazo_prestamo}} '
         'años; sin cocina propia'),
    (42, '§1 4/5: proyecciones: {{eventos_a1}} eventos × {{invitados_evento}} invitados × {{precio_invitado}} → '
         '{{ventas_a1}} / {{ventas_a2}} / {{ventas_a3}}; EBITDA {{ebitda_pct_a1}}; equilibrio {{equilibrio_eventos}} '
         'eventos/año; DSCR mínimo {{dscr_min}}'),
    (43, '§1 5/5: el equipo: dueño-chef ejecutivo que también vende, sous chef, pool de event staff W-2, prep cook / '
         'driver ({{plantilla_puestos}} personas, {{plantilla_jornadas}} FTE); sin inventar trayectoria'),
    (46, '§2 1/5: qué vende y a quién: empresas (oficinas, HR, event planners) y particulares (bodas, fiestas); el '
         'cliente compra un evento que sale bien, no solo comida'),
    (47, '§2 2/5: propuesta de valor en tres pilares del ES de catering: estaciones temáticas en directo, dietas '
         'especiales y alérgenos al mismo nivel, degustación previa y menú con la marca del cliente'),
    (48, '§2 3/5: modelo económico: precio por invitado {{precio_invitado}} sin sales tax con el servicio incluido, '
         '{{ventas_evento}} por evento de media; service charge ≠ propina; anticipo para bloquear fecha (35 %, Kit '
         'estimate; research: 25-50 %)'),
    (49, '§2 4/5: posicionamiento frente a restaurantes que hacen catering, grandes caterers y marketplaces; di «mobile '
         'food vendors», nunca «food trucks»'),
    (50, '§2 5/5: estilos de servicio y menús (drop-off · buffet · family-style · plated · stations), mínimo de '
         'invitados; la calculadora del kit presupuesta cada estilo'),
    (53, '§3 1/6: el mercado US desde el lado del cliente (research §2: wedding / corporate / event / drop off catering), '
         'sin tamaño de mercado inventado'),
    (54, '§3 2/6: cliente social: bodas ($80 por plato de media en 2024, The Knot 2025 Real Weddings Study vía Fox '
         'Business) y fiestas privadas; temporada sin porcentajes de fuentes «resumen»'),
    (55, '§3 3/6: cliente corporativo: drop-off y boxed lunch, buffets, recepciones, fiestas de fin de año; pago a 30 '
         'días; marketplaces corporativos (comisión en el libro: {{marketplace_comision}})'),
    (56, '§3 4/6: mezcla de canales del ejemplo (empresas ≈ 3 de cada 4 eventos y ≈ la mitad de las ventas: Kit '
         'estimate) y estacionalidad (Month 1 = marzo; picos en octubre y diciembre)'),
    (57, '§3 5/6: tendencias con cuidado (dietas especiales, experiencias en directo, desechables compostables) sin '
         'cifras sin fuente'),
    (58, '§3 6/6: riesgos de demanda: temporada de bodas, cancelaciones, presupuestos corporativos'),
    (61, '§4 1/6: panorama competitivo local: caterers establecidos, restaurantes con catering, marketplaces, bandejas '
         'de supermercado'),
    (62, '§4 2/6: cinco fuerzas de Porter aplicadas al catering de eventos'),
    (63, '§4 3/6: competidores directos e indirectos y cómo compararse (precio por invitado, servicio, reseñas en The '
         'Knot, WeddingWire y Google)'),
    (64, '§4 4/6: barreras de entrada: cocina con permiso (no desde casa), seguros, permisos por evento, personal'),
    (65, '§4 5/6: factores críticos de éxito: puntualidad, seguridad alimentaria en el transporte, reseñas, relación '
         'con venues y wedding planners'),
    (66, '§4 6/6: DAFO del concepto'),
    (69, '§5 1/7: estrategia: dos embudos (bodas: ciclo largo con degustación; empresas: recurrencia)'),
    (70, '§5 2/7: presencia digital: web con menús y precios «desde», formulario de presupuesto, Google Business '
         'Profile, reseñas'),
    (71, '§5 3/7: directorios y marketplaces: The Knot, WeddingWire, ezCater'),
    (72, '§5 4/7: venta B2B directa: office managers, HR, event planners, venues (preferred vendor lists)'),
    (73, '§5 5/7: degustaciones para prospectos (su línea de coste en el P&L) y el proceso propuesta → contrato'),
    (74, '§5 6/7: fidelización y referidos: clientes corporativos recurrentes, reseñas después de cada evento'),
    (75, '§5 7/7: presupuesto: {{marketing_anual}} al año en el ejemplo; medir el coste por evento ganado'),
    (78, '§6 1/5: la cocina comisaria compartida (horas, almacenaje, parking: {{alquiler_mes}} al mes en el ejemplo; '
         'research: $15-$45/h) y el commissary agreement por escrito'),
    (79, '§6 2/5: equipo propio frente a alquiler; furgoneta refrigerada usada {{inv_vehiculo}} + unidad de frío '
         '{{inv_frio}}; chafing dishes y cajas isotermas {{inv_menaje_servicio}}'),
    (80, '§6 3/5: la operativa de un evento en 6 fases del ES (briefing D-21, visita técnica D-14, compras D-7/D-1, '
         'producción y carga, montaje 60-90 min y servicio, recogida y cobro del saldo en 24-48 h)'),
    (81, '§6 4/5: seguridad alimentaria en el transporte (hot / cold holding, registros de temperatura) y alérgenos'),
    (82, '§6 5/5: proveedores (distribuidor broadline + especialistas), alquileres de party rental y mantenimiento de la '
         'furgoneta'),
    (85, '§7 1/6: estructura: dueño-chef ejecutivo y ventas, sous chef, pool de event staff, prep cook / driver'),
    (86, '§7 2/6: personal fijo y su coste: {{personal_a1}} el año 1 ({{personal_pct}} de las ventas)'),
    (87, '§7 3/6: personal por evento: {{horas_evento}} horas × {{personas_evento}} personas por evento, cobertura '
         '{{cobertura_horas}}; ratio orientativo de servers por invitados según estilo (Kit estimate)'),
    (88, '§7 4/6: W-2 frente a 1099 (FLSA; California AB5); cargas {{cargas_pct}}; mínimo federal y estatal'),
    (89, '§7 5/6: formación: Certified Food Protection Manager, food handler cards, alcohol server certification (TIPS '
         '/ ServSafe Alcohol), protocolo de servicio'),
    (90, '§7 6/6: service charge frente a propina (IRS Rev. Rul. 2012-18) y cómo se reparte la propina voluntaria'),
    (93, '§8 1/7: viabilidad: ventas del año 1 {{ventas_a1}}, margen bruto {{margen_bruto_pct}}, EBITDA {{ebitda_a1}} '
         '({{ebitda_pct_a1}})'),
    (94, '§8 2/7: inversión con tokens: {{inv_vehiculo}}, {{inv_adaptacion}}, {{inv_frio}}, {{inv_equipo_cocina}}, '
         '{{inv_menaje_servicio}}, {{inv_permisos}}, {{inv_lanzamiento}}, {{inv_stock}} → {{capex}}; fondo de maniobra '
         '{{fondo_maniobra}}; total {{inversion_total}}; financiación'),
    (95, '§8 3/7: proyección a 3 años: {{ventas_a1}} / {{ventas_a2}} / {{ventas_a3}} (crecen los EVENTOS: '
         '{{crecimiento_a2}} y {{crecimiento_a3}}); resultado neto {{resultado_neto_a1}} / {{resultado_neto_a2}} / '
         '{{resultado_neto_a3}}'),
    (96, '§8 4/7: costes: comida {{food_cost_comida}}, mercancía total {{cogs_pct}}, desechables {{consumibles_pct}}, '
         'personal {{personal_pct}}, comisaria {{ocupacion_pct}}; benchmarks de research §5 (food cost 28-35 %, '
         'personal 25-35 %, neto 7-8 %)'),
    (97, '§8 5/7: punto de equilibrio en EVENTOS al año: {{equilibrio_eventos}} (contable) y '
         '{{equilibrio_caja_eventos}} (caja) frente a {{eventos_a1}} del plan; holgura {{holgura_caja_pct}}'),
    (98, '§8 6/7: caja y retorno: saldo mínimo {{saldo_minimo}} en el mes {{mes_saldo_minimo}}, payback {{payback}}, '
         'DSCR {{dscr_min}}; los anticipos no se modelan y mejoran la caja real'),
    (99, '§8 7/7: escenarios: pesimista {{pesimista_eventos}} eventos × {{pesimista_precio}} × {{pesimista_invitados}} '
         'invitados → {{pesimista_ventas}}, resultado {{pesimista_resultado}}; optimista {{optimista_ventas}}; en el '
         'pesimista el coste real del personal de eventos baja con los eventos'),
    (111, '§10 1/7: conclusión: por qué el modelo se sostiene (sin cocina propia, dos motores de demanda)'),
    (112, '§10 2/7: riesgos y mitigación (tabla de riesgos del ES): cancelación (anticipo y política), intoxicación '
          '(HACCP, seguros), avería de la furgoneta, impago de empresas, falta de personal, alergias, lluvia en exterior'),
    (113, '§10 3/7: fortalezas competitivas'),
    (114, '§10 4/7: hoja de ruta en las 6 fases del checklist (Business Setup → Kitchen, Van & Permits → Equipment → '
          'Staff → Marketing → First 90 Days)'),
    (115, '§10 5/7: KPIs: eventos al mes, precio por invitado, food cost, personal por evento, conversión de propuestas, '
          'cancelaciones, repetición de empresas, reseñas'),
    (116, '§10 6/7: visión a 3 años: más empresas recurrentes, segunda furgoneta, cocina propia solo cuando los números '
          'lo pidan'),
    (117, '§10 7/7: cierre: los siguientes pasos con el Excel, la calculadora de precios y el checklist del kit'),
])
DOCX_NOTAS = OrderedDict([('cat', OrderedDict(sorted(list(_NOTAS_SECCION.items()) + list(_N9.items()))))])

# ==========================================================================
# Pistas por celda (extraer_textos.py → textos_es.json → tandas)
# ==========================================================================
_CASO = ('D70: caso US = 180 eventos/año (calibrado D15; research: 170) × 60 invitados × $60 por invitado (sin sales '
         'tax, servicio incluido) = $648,000; drivers permutados: B4 = eventos/año, B5 = precio por invitado, B6 = '
         'invitados por evento. Las notas describen el MÉTODO: sin cifras del caso (cambian al recalibrar)')
CELDA_PISTAS = OrderedDict([
    (('CATP', _S, 'C4'), _CASO + '; los años 2-3 crecen en EVENTOS (B7/B8); compara con la capacidad (fila 51)'),
    (('CATP', _S, 'C5'), _CASO + '; precio por invitado SIN sales tax con el personal y el service charge incluidos y '
                                 'SIN la propina voluntaria; la calculadora del kit lo saca por estilo de servicio'),
    (('CATP', _S, 'C6'), _CASO + '; invitados medios por evento (research: 50-75 es lo típico); la mezcla del ejemplo '
                                 'va de drop-off de 40 a bodas de 120'),
    (('CATP', _S, 'C15'), 'D70: desechables 3 % (platos, cubiertos y envases de los drop-off)'),
    (('CATP', _S, 'C16'), 'D74: marketplaces de catering corporativo (p. ej. ezCater): 10 % de las ventas en el ejemplo'),
    (('CATP', _S, 'C17'), 'D74: comisión del marketplace 15 % (ezCater cobra ~15 % sobre comida y entrega: Kit '
                          'estimate)'),
    (('CATP', _S, 'C18'), 'D70: 2.5 % (muchas empresas pagan por ACH o cheque)'),
    (('CATP', _S, 'C24'), 'D74: cocina comisaria compartida: horas (≈ 100 h/mes) + almacenaje + parking de la furgoneta; '
                          'research: $15-$45/h (The Food Corridor, 2023 Shared Kitchen Operator Survey)'),
    (('CATP', _S, 'C27'), 'D70: $6,000/año = BOP + commercial auto + liquor liability (Insureon publica medias)'),
    (('CATP', _S, 'C44'), 'D70: 5 años para la furgoneta y su adaptación'),
    (('CATP', _S, 'C51'), 'D70: DATO INFORMATIVO (no entra en ningún cálculo): el techo de eventos al año que tu cocina y '
                          'tu equipo pueden atender; compáralo con la fila 4 y con el escenario optimista'),
    (('CATP', _S, 'C52'), 'D70: rampa 50 % → 8 meses (las bodas se reservan con meses de antelación)'),
    (('CATP', _S, 'C54'), 'D70: 1 mes de comisaria antes de abrir'),
    (('CATP', _S, 'C58'), 'D70: cobro medio 14 días (bodas prepagadas, empresas a 30 días); el libro no admite '
                          'anticipos: mejoran la caja real (nota de la Tesorería)'),
    (('CATP', _S, 'C62'), 'D69/D70: alcohol 0 %: el cliente compra el alcohol y lo sirven bartenders certificados (no '
                          'hace falta licencia propia por defecto)'),
    (('CATP', _N, 'A12'), 'SPEC §4.1 línea 8 (I1): el Word del kit usa las MISMAS cifras de ejemplo que este libro; si '
                          'cambias el libro, actualiza las cifras del Word (fuera «versión 1.1»)'),
    (('CATP', _ES, 'E23'), 'D73: la MISMA plantilla en los tres escenarios; en el pesimista el coste REAL del personal de '
                           'eventos baja con los eventos (pagas horas por evento), así que el resultado real sería algo '
                           'mejor'),
])
_D18 = ('D18 (catering): la propuesta es la del Food Truck; describe el MÉTODO del libro y reescribe lo que hable de '
        'clientes/día, días de apertura, ticket, camión o aparcamiento → eventos al año, invitados por evento, precio por '
        'invitado, furgoneta, cocina comisaria')
for _f in range(35, 52):
    for _col in 'ABCD':
        CELDA_PISTAS[('CATP', _N, '%s%d' % (_col, _f))] = _D18
PISTA_D19_GENERICA = ('Celda a celda: escribe SOLO el texto de ESTA celda (una tabla o una tarea): mira su pista '
                      'propia')
_D19_BASE = ('D19/D75: tabla «US CATERING BENCHMARKS (sourced) AND KIT ESTIMATES» (Benchmark | Value | Source | Note). '
             'Value en formato US; Source = el DOMINIO de la fuente LEÍDA de research §4-§5, o «Kit estimate» si allí '
             'figura como «(resumen)» o [estimado]. Esta fila: ')
_D19 = OrderedDict([
    (55, 'food cost 28-35 % (alta gama ~25 %, volumen ~40 %) — galleysolutions.com'),
    (56, 'margen bruto 65-70 % — galleysolutions.com'),
    (57, 'coste de personal 25-35 % de las ventas — galleysolutions.com (itsacheckmate.com da 20-35 %)'),
    (58, 'margen neto 7-8 % de media — itsacheckmate.com'),
    (59, 'precio por invitado en bodas: $80 por plato de media (2024) — The Knot 2025 Real Weddings Study vía '
         'foxbusiness.com'),
    (60, 'precio por invitado general $20-$80 y evento medio de 50-75 personas — Kit estimate (snippet de yelp.com, no '
         'leído)'),
    (61, 'almuerzo corporativo: boxed lunch $12-$35+, drop-off buffet $20-$38 — Kit estimate (zerocater, resumen)'),
    (62, 'comisión de marketplace corporativo ~15 % (ezCater sobre comida + entrega) — Kit estimate (resumen)'),
    (63, 'anticipo 25-50 % al firmar y saldo 5-7 días antes; empresas a 30 días — Kit estimate (contratos de ejemplo, '
         'resumen)'),
    (64, 'sueldos: chef / gerente $25-$35/h, prep cook $15-$18/h, servers y bartenders $18-$25/h, cargas +15-30 % — '
         'restroworks.com'),
    (65, 'cocina compartida $15-$45/h (el 42 % cobra $20-$29/h) — thefoodcorridor.com (2023 Shared Kitchen Operator '
         'Survey)'),
    (66, 'inversión de arranque $20,000-$65,000 con cocina compartida; $250,000+ con cocina propia — restroworks.com'),
    (67, 'seguros (Insureon, < 5 empleados): general liability $45/mes, commercial auto $204/mes, liquor liability $28/mes '
         '— insureon.com'),
    (68, 'ratio de personal de servicio: 1 server por 10-12 invitados (plated) o 20-25 (buffet) — Kit estimate'),
])
for _f, _p in _D19.items():
    for _col in 'ABCD':
        CELDA_PISTAS[('CATP', _N, '%s%d' % (_col, _f))] = _D19_BASE + _p

# Checklist (D77): una pista por FILA de tarea (columnas B tarea · C responsable · D plazo · E nota práctica)
_CK = 'D77: escribe una TAREA de catering (B tarea · C responsable · D plazo · E nota práctica, una celda cada vez) ' \
      'condensando el checklist ES de catering (fuente_es_cat.json) + research §6. Esta fila: '
TAREAS_CAT = OrderedDict([
    ('F1 - Constitución', [
        'estructura: LLC frente a S corp con tu contador (ES: alta autónomo / SL)',
        'EIN gratis en el IRS + alta estatal de nóminas y desempleo',
        'registrar la LLC en el Secretary of State + registered agent + operating agreement',
        'cuenta bancaria del negocio y finanzas separadas',
        'seller\'s permit / registro de sales tax del estado (en muchos estados tributa toda la factura de catering)',
        'business license de la ciudad o el condado (+ DBA si usas nombre comercial)',
        'contador / bookkeeper y estimated taxes trimestrales (ES: modelo 130)',
        'software de catering: propuestas, contratos, anticipos y facturas',
        'contrato tipo con un abogado: anticipo, cancelación, mínimo de invitados, service charge frente a propina (ES: '
        'desistimiento → cancelación)',
        'plan de seguridad alimentaria basado en HACCP y SOP de transporte (ES: APPCC)',
        'Certified Food Protection Manager (ServSafe Manager) del dueño o chef (ES: manipulador)',
    ]),
    ('F2 - Vehículo', [
        'elegir cocina comisaria compartida: horas, almacenaje frío y seco, parking de la furgoneta (visita y precios)',
        'commissary agreement por escrito (lo exige el health department)',
        'catering / health permit del condado (plan review solo si alquilas cocina propia; inspección)',
        'temporary food event permits para eventos comunitarios o públicos',
        'fire marshal: llama abierta, combustible de chafing y carpas (según venue y ciudad)',
        'comprar la furgoneta refrigerada usada (inspección mecánica + unidad de frío)',
        'registro y título en el DMV + commercial auto insurance (CDL solo con GVWR ≥ 26,001 lb)',
        'adaptación de la furgoneta: estanterías, sujeción de cargas, rotulación',
        'general liability + BOP; certificado de seguro (COI) y «additional insured» que piden los venues',
        'liquor liability si sirves alcohol que compra el cliente (bartenders certificados)',
        'workers\' comp (obligatorio con empleados en casi todos los estados)',
        'residuos y grasa con un hauler con licencia (a menudo lo gestiona la comisaria)',
        'control de plagas con empresa con licencia (vía comisaria) y avisos obligatorios publicados',
    ]),
    ('F3 - Equipamiento', [
        'lista de equipo propio frente a alquiler (party rental) por estilo de servicio',
        'chafing dishes, cajas isotermas y termómetros calibrados',
        'cocina portátil: inducción, quemadores y energía para el lugar del evento',
        'menaje GN: hotel pans, sheet pans, utensilios',
        'menaje de servicio y presentación para estaciones temáticas (displays, bandejas)',
        'cuentas con un distribuidor broadline (US Foods, Sysco, Restaurant Depot) (ES: proveedores españoles → US)',
        'proveedores especializados para las estaciones temáticas',
        'acuerdo con una empresa de alquileres (mesas, mantelería, vajilla) con tarifa pactada',
        'desechables y envases para drop-off (compostables si la ciudad lo exige)',
        'registros de temperatura en el transporte (data logger)',
        'montar el espacio en la comisaria: estanterías, etiquetado, FIFO',
        'ensayo completo de un evento (dry run) con el equipo',
    ]),
    ('F4 - Personal', [
        'plan de personal por evento según el estilo de servicio (ratio de servers por invitados)',
        'pool de event staff en nómina W-2 (no 1099: FLSA; California AB5)',
        'offer letters, I-9 y W-4; salario mínimo estatal',
        'new-hire reporting al estado',
        'proveedor de nóminas y workers\' comp en marcha',
        'food handler cards del equipo',
        'alcohol server certification (TIPS / ServSafe Alcohol / TABC) de los bartenders',
        'OSHA basics: quemaduras, cargas, conducción',
        'formación de servicio y protocolo del evento (uniforme, briefing, 9 alérgenos mayores)',
        'política de service charge y propinas (Rev. Rul. 2012-18: el service charge es salario)',
    ]),
    ('F5 - Marketing', [
        'marca, logo, menú de estaciones temáticas y fotos profesionales',
        'web con menús, precios «desde» por invitado y formulario de presupuesto',
        'Google Business Profile y reseñas',
        'perfiles en The Knot y WeddingWire (ES: Bodas.net / Zankyou)',
        'alta en ezCater (marketplace corporativo) (ES: CateringClick)',
        'prospección B2B: office managers, HR, event planners (lista y visitas)',
        'acuerdos con venues y wedding planners (preferred vendor lists)',
        'política de degustaciones para prospectos',
        'Instagram y redes con fotos de eventos (ES: WhatsApp → texto / SMS)',
        'plantilla de propuesta con la calculadora del kit y seguimiento en el CRM',
        'programa de referidos y reseñas después de cada evento',
        'evento de lanzamiento / showcase para planners y empresas',
    ]),
    ('F6 - 90 Días', [
        'briefing con el cliente D-21: invitados, dietas, timeline del evento',
        'visita técnica al venue D-14: accesos, cocina, enchufes, agua',
        'compras D-7 / D-1 y lista de producción',
        'checklist de carga y transporte con temperaturas',
        'montaje 60-90 min antes y servicio',
        'recogida, limpieza y devolución de alquileres',
        'factura del saldo y cobro en 24-48 h; control de anticipos',
        'pedir reseña y fotos; seguimiento en el CRM',
        'revisión semanal de food cost y personal por evento frente a la calculadora',
        'revisión a los 90 días: precios por invitado, mínimos y paquetes',
    ]),
])
for _h, _ts in TAREAS_CAT.items():
    for _k, _t in enumerate(_ts):
        for _col in 'BCDE':
            CELDA_PISTAS[('CATC', _h, '%s%d' % (_col, 5 + _k))] = _CK + 'fase %s, tarea %d/%d: %s' % (
                _h[1], _k + 1, len(_ts), _t)

# Pistas por TEXTO propias del catering (se suman a las de extraer_textos.PISTAS)
PISTAS_EXTRA = [
    (r'^Días fuera de rango$|^Los días van de 1 a 365', 'D72: esta validación cubre a la vez B6 (INVITADOS por evento), '
                                                         'B58/B59 (días de cobro y de pago) y los invitados de '
                                                         'Escenarios: un texto que valga para todos (p. ej. «Out of '
                                                         'range» / «Enter a whole number from 1 to 365: guests per '
                                                         'event or days.»)'),
    (r'[Cc]lientes?|[Tt]icket|[Dd]ías de apertura|al día|por día',
     'D72: motor permutado: «events per year» (B4), «price per guest» (B5), «guests per event» (B6); nunca «customers», '
     '«per day» ni «operating days» (gate)'),
    (r'[Vv]ehícul|[Ff]ood ?[Tt]ruck|[Cc]amión|[Rr]emolque', 'D69: la furgoneta refrigerada («refrigerated van»); nunca '
                                                            '«truck» (gate)'),
    (r'[Vv]entanilla|[Ff]estival|[Mm]ercados|[Aa]mbulante|[Cc]alle', 'D69: catering de eventos en el lugar del cliente; '
                                                                     'sin ventanilla, festivales, mercados ni venta '
                                                                     'ambulante (gate)'),
    (r'[Aa]parcamiento|base del vehículo|comisar', 'Glosario: «commissary kitchen (hours + storage) & van parking»'),
    (r'[Gg]enerador|gas\b|propano', 'D74: «portable cooking and power (induction, burners, generator)»'),
    (r'[Dd]elivery|[Gg]lovo|[Uu]ber', 'D74: marketplaces de catering corporativo (p. ej. ezCater), no apps de delivery'),
    (r'[Ee]ventos?|[Bb]odas?', 'Glosario: event catering; weddings; corporate events; drop-off, buffet, family-style, '
                               'plated, stations'),
]

# Glosario de catering (se suma al de FT/CAF y al del financial-kit, que mandan)
GLOSARIO_CAT = OrderedDict([
    ('evento', 'event'), ('invitados / comensales', 'guests'), ('precio por invitado / por cubierto', 'price per guest'),
    ('cocina comisaria / cocina compartida', 'commissary kitchen / shared kitchen'),
    ('furgoneta refrigerada', 'refrigerated (cargo) van'), ('presupuesto', 'quote / proposal'),
    ('anticipo / señal', 'deposit'), ('cancelación', 'cancellation'), ('degustación', 'tasting'),
    ('estación temática', 'chef-attended (themed) station'), ('bufé', 'buffet'), ('emplatado', 'plated'),
    ('servicio a la mesa compartido', 'family-style'), ('entrega sin servicio', 'drop-off'),
    ('camarero de eventos', 'event server / event staff'), ('cargo por servicio', 'service charge'),
    ('propina voluntaria', 'gratuity (voluntary tip)'), ('alquileres (mesas, mantelería)', 'party rentals'),
    ('organizador de bodas', 'wedding planner'), ('espacio del evento', 'venue'),
    ('mínimo de invitados', 'guest minimum'), ('chafing', 'chafing dish'), ('caja isoterma', 'insulated food carrier'),
    ('cliente corporativo', 'corporate client'), ('particular', 'private / social client'),
])


# ==========================================================================
# Caso de ejemplo US (D70; research §8 tal cual): celdas VERDES del FT. (corto, hoja ES, celda) → (valor, rótulo ES)
# ==========================================================================
def valores_cat(M):
    v = OrderedDict()
    sup = [
        ('B4', 170, 'Clientes/día'), ('B5', 60, 'Ticket medio'), ('B6', 60, 'Días de apertura'),
        ('B7', 0.15, 'Crecimiento de volumen del año 2'), ('B8', 0.10, 'Crecimiento de volumen del año 3'),
        ('B11', 0.88, 'Ventas de COMIDA'), ('B13', 0.30, 'Coste de mercancía sobre las ventas de COMIDA'),
        ('B14', 0.25, 'Coste de mercancía sobre las ventas de BEBIDA'), ('B15', 0.03, 'Consumibles'),
        ('B16', 0.10, 'Ventas por delivery'), ('B17', 0.15, 'Comisión de la plataforma'),
        ('B18', 0.025, 'Comisión de los medios de pago'), ('B20', 0.10, 'Seguridad Social'),
        ('B21', 12, 'Número de pagas'), ('B22', 15080, 'SMI anual'), ('B24', 2500, 'Alquiler mensual'),
        ('B25', 1, 'Fianza'), ('B26', 250, 'Suministros'), ('B27', 6000, 'Seguros'), ('B28', 0.03, 'Varios'),
        ('B30', 40000, 'Recursos propios'), ('B31', M.CALIBRAR, 'Préstamo bancario'), ('B32', 0.10, 'Tipo de interés'),
        ('B33', 7, 'Plazo del préstamo'), ('B34', 0, 'Carencia'), ('B35', 3, 'Fondo de maniobra'),
        ('B37', 0.25, 'Impuesto de Sociedades, nueva'), ('B38', 0.25, 'Impuesto de Sociedades, tipo'),
        ('B39', 0.08, 'IVA repercutido de restauración'), ('B40', 0.08, 'IVA repercutido/soportado'),
        ('B41', 0, 'IVA soportado en compras'), ('B42', 0, 'Bases negativas'),
        ('B44', 5, 'Vida útil de obra'), ('B45', 7, 'Vida útil de maquinaria'), ('B48', 0, 'Subida anual'),
        ('B51', 250, 'Plazas de pie'), ('B52', 0.50, 'Actividad del mes 1'), ('B53', 8, 'Meses hasta alcanzar'),
        ('B54', 1, 'Meses de alquiler del aparcamiento'), ('B55', 0.10, 'Imprevistos sobre las partidas'),
        ('B58', 14, 'Días medios de cobro'), ('B59', 7, 'Días medios de pago'),
        ('B62', 0, 'Bebida ALCOHÓLICA'), ('B63', 0.08, 'IVA de la bebida ALCOHÓLICA'),
        ('B65', 1.15, 'DSCR mínimo'), ('B66', 1.25, 'DSCR objetivo'), ('B67', 0.15, 'Holgura mínima'),
        ('B68', None, 'Suelo salarial anual'),
    ]
    for c, val, rot in sup:
        v[('CATP', _S, c)] = (val, rot)
    # Inversión (D74): las 14 partidas tecleadas, filas 7-20 (rótulos ES del FT)
    for k, (val, rot) in enumerate([
            (32000, 'Vehículo'), (4000, 'Adaptación'), (12000, 'Equipamiento cocina'), (5000, 'Generador'),
            (9000, 'Instalación gas'), (1500, 'Depósito de agua'), (2000, 'Constitución'), (2500, 'Licencias'),
            (500, 'Proyecto técnico'), (2000, 'TPV'), (5000, 'Menaje'), (6000, 'Stock'), (7000, 'Marketing'),
            (9000, 'Toldo')]):
        v[('CATP', _I, 'B%d' % (7 + k))] = (val, rot)
    # P&L: fijos B26-B35 (research §8: $36,200) y umbrales D75 [kit benchmark]
    for k, (val, rot) in enumerate([
            (1500, 'Permisos'), (6000, 'Mantenimiento'), (12000, 'Marketing'), (3600, 'Gestoría'), (3000, 'Software'),
            (4800, 'Limpieza'), (1200, 'Gestión de residuos'), (300, 'Desinsectación'), (800, 'Prevención'),
            (3000, 'Derechos de autor')]):
        v[('CATP', _P, 'B%d' % (26 + k))] = (val, rot)
    # E51: D75 dice 62 %, pero el margen bruto del motor resta tarjeta, marketplace y varios (no solo mercancía +
    # desechables, que es lo que daba el 67.6 % de research): con el caso sale 60.6 % → umbral 60 % (F2-NOTAS §4)
    for c, val, rot in [('E51', 0.60, 'Margen bruto'), ('E53', 0.35, 'Coste de mercancía /'),
                        ('E54', 0.38, 'Coste de personal'), ('E55', 0.08, 'Aparcamiento'), ('E56', 0.05, 'Resultado neto')]:
        v[('CATP', _P, c)] = (val, rot)
    # Staffing (D73; research §8): personas (B), FTE por persona (C), bruto mes TOTAL de la fila (D)
    for f, (b, c, d) in zip(range(5, 9), [(1, 1.0, 5000), (1, 1.0, 3640), (8, 0.22, 5796), (1, 0.75, 2210)]):
        for col, val in zip('BCD', (b, c, d)):
            v[('CATP', _R, '%s%d' % (col, f))] = (val, None)
    v.update([
        (('CATP', _R, 'B11'), (8000, 'Coste anual')), (('CATP', _R, 'B12'), (8000, 'Coste anual')),
        (('CATP', _R, 'B16'), (40, 'Jornada completa')), (('CATP', _R, 'B17'), (50, 'Semanas')),
        (('CATP', _R, 'B18'), (12, 'Horas de servicio')), (('CATP', _R, 'B19'), (4.3, 'Personas necesarias')),
    ])
    # Escenarios (research §8): −25 % / +25 % de eventos, −10 % / +10 % de precio e invitados
    v.update([
        (('CATP', _ES, 'B5'), (128, 'Clientes/día')), (('CATP', _ES, 'D5'), (213, 'Clientes/día')),
        (('CATP', _ES, 'B6'), (54, 'Ticket')), (('CATP', _ES, 'D6'), (66, 'Ticket')),
        (('CATP', _ES, 'B7'), (55, 'Días')), (('CATP', _ES, 'D7'), (65, 'Días')),
    ])
    # Estacionalidad (research §8): apertura en MARZO → Month 1-12 (suma 100 %)
    for col, val in zip('BCDEFGHIJKLM', (0.07, 0.08, 0.095, 0.10, 0.07, 0.07, 0.10, 0.11, 0.085, 0.115, 0.05, 0.055)):
        v[('CATP', _T, '%s5' % col)] = (val, 'Estacionalidad')
    return v


# Calibración D15 (paso 3 de la F2: aplicar_en real). Cada celda, citada en F2-NOTAS.md (G7). Vacía de momento: el
# dry-run de este paso dice si hace falta subir B4 (de 10 en 10 hasta 190)
CALIBRACION_D15 = OrderedDict([
    # Dry-run del paso 1 con research §8 tal cual: holgura de caja 14.2 % (< 15 %). Regla D70: B4 de 10 en 10 → 180
    (('CATP', _S, 'B4'), (180, 'D15: holgura de caja 14.2 % → ≥ 15 % (regla D70: B4 de 10 en 10 hasta 190)')),
    (('CATP', _ES, 'B5'), (135, 'mismas proporciones que research §8 (−25 %) sobre los 180 eventos calibrados')),
    (('CATP', _ES, 'D5'), (225, 'mismas proporciones que research §8 (+25 %) sobre los 180 eventos calibrados')),
    # con 180 eventos, 12 h × 4.3 personas × 180 = 9,288 h frente a 9,020 contratadas (97.1 % < 98 %): el pool de
    # personal de eventos sube de 0.22 a 0.23 FTE por persona y su bruto de la fila, en proporción ($19/h)
    (('CATP', _R, 'C7'), (0.23, 'D15: cobertura ≥ 98 % con 180 eventos (8 personas × 0.23 FTE)')),
    (('CATP', _R, 'D7'), (6060, 'D15: 8 × 0.23 FTE × 173.33 h × $19 (el coste sube con las horas)')),
])


# ==========================================================================
# FORMULAS_EN (D72): las del FT con la fila del Break-Even y las listas de la inversión de catering
# ==========================================================================
_PE_CAT = ('=IFERROR("With the average price per guest excl. sales tax above, you need "&TEXT(ROUNDUP(B15,0),"0")&" '
           'events a year at your average of "&TEXT(B11,"0")&" guests per event to avoid losing money (accounting '
           'break-even, depreciation included), and "&TEXT(ROUNDUP(B20,0),"0")&" for cash to hold (cash break-even: '
           'depreciation out, because it is not paid, and the year\'s loan payment in"&IF(B12=0,"; no principal is '
           'repaid this year (interest-only period or no loan)","")&"). The ""Revenue needed per year"" rows show the '
           'same figures in your currency.","")')
_C9_CAT = ('=IFERROR("Price per guest excl. sales tax plus the weighted sales tax of your sales lines ("&TEXT('
           "SUMPRODUCT('3-Year P&L'!$E$10:$E$11,'3-Year P&L'!$G$10:$G$11)*100,\"0\")&\"%), rounded. In the US the "
           'quote adds sales tax on top, and many states tax the whole catering invoice (food, staff, rentals and the '
           'service charge); in the UK, VAT is included in the price.","")')


def formulas_cat():
    sys.path.insert(0, BP)
    import formulas_en as F                                                    # noqa: E402
    out = OrderedDict()
    for h, d in F._COMUNES.items():
        for c, f in d.items():
            out[('CATP', h, c)] = f
    out[('CATP', _S, 'C9')] = _C9_CAT
    out[('CATP', _E, 'A26')] = _PE_CAT
    for c, f in F._inversion('D21', 'D22', 'D23', 'D25', 'D26', 'D28', 'D31', 'D32', 'D33', 24, 26, 31, 32,
                             'used refrigerated van, van upfit, van refrigeration unit, commissary storage fit-out and '
                             'health plan review',
                             'LLC formation and legal, first-year permits, opening inventory, website, photography and '
                             'launch marketing, the commissary deposit, pre-opening commissary rent and the working '
                             'capital reserve').items():
        out[('CATP', _I, c)] = f
    return out


def completar(M):
    fijos = OrderedDict((k, v) for k, v in M.FIJOS.items() if k not in FIJOS_FUERA)
    fijos.update(FIJOS_NUEVOS)
    M.FIJOS = fijos
    M.POR_CELDA = POR_CELDA
    M.TOKENS_DOCX = tokens_cat(M.TOKENS_DOCX)
    M.DOCX_FIJOS = docx_fijos(M)
    M.DOCX_NOTAS = DOCX_NOTAS
    M.DOCX_NOTAS_PLAN = DOCX_NOTAS_PLAN
    M.FORMULAS_EN = formulas_cat()
    M.VALORES_EN = valores_cat(M)
    M.CALIBRACION_D15 = CALIBRACION_D15
    M.CELDA_PISTAS = CELDA_PISTAS
    M.PISTAS_EXTRA = PISTAS_EXTRA
    M.PISTA_D19 = PISTA_D19_GENERICA          # la pista D19 de verdad va por celda (filas 55-68); las tareas, también
    ft = [(_num(n), 'cifra del caso FT EN publicado (no se reutiliza)', None) for n in _cifras_ft()
          if n not in {int(x[0]) for x in M.VALORES_EN.values() if isinstance(x[0], (int, float))}]
    M.CIFRAS_PROHIBIDAS = CIFRAS_PROHIBIDAS + ft
    glo = OrderedDict(M.GLOSARIO)
    for k in ('cliente/día', 'ticket medio sin IVA', 'PVP con IVA', 'aparcamiento y base del vehículo', 'venta ambulante'):
        glo.pop(k, None)                      # glosario del food truck que no vale en catering
    glo.update([('cliente/día → (motor)', 'events per year'), ('ticket medio sin IVA → (motor)',
                                                               'average price per guest (excl. sales tax)'),
                ('días de apertura → (motor)', 'average guests per event'),
                ('aparcamiento y base del vehículo', 'commissary kitchen & van parking')])
    for k, val in GLOSARIO_CAT.items():
        glo.setdefault(k, val)
    M.GLOSARIO = glo
