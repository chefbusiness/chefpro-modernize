#!/usr/bin/env python3
"""
datos_mbar.py — Mobile Bar Business Plan Kit (EN) · los datos ES→EN que dependen del contenido: rótulos fijados (D87),
POR_CELDA, pistas (D18/D19, notas del caso, las 68 tareas del checklist D91), tokens del docx (D92), fijos y notas del
docx, caso US (D85; research §8), FORMULAS_EN, cifras ES prohibidas y vocabulario vetado RX_BAR_NO (D93) y glosario de
research §9 (regla de jerga §0). Lo llama `mapas_mbar.instalar()` con el módulo `mapas` YA cargado con los datos de
FT/CAF (motor 2.2), de los que parte. La fuente ES del circuito es el FOOD TRUCK ES: los rótulos ES de abajo son los
del FT; el EN de partida de cada celda es el del CATERING publicado (mapas_mbar.CAT_CELDA).
Sesión Claude Code, 13-oct-2026 (F2, paso 1).
"""
import json
import os
import sys
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
BP = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
CAT = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')

URL_MBAR = 'aichef.pro/en/digital-products/mobile-bar-business-plan'
_I, _S, _P, _R, _N, _E, _ES, _T = ('Inversión Inicial', '0. Supuestos', 'PyG 3 Años', 'Personal', 'Instrucciones',
                                   'Punto Equilibrio', 'Escenarios', 'Tesorería 12 meses')
GLOSA_DRY_HIRE = '(you supply the alcohol; we bring the bar, the bartenders and everything else)'
# Medidas (John, 13-oct): sistema US como principal y la métrica entre paréntesis (UK y Australia miden en ml)
REGLA_UNIDADES = ('MEDIDAS US (John, 13-oct): principales oz / fl oz, lb, quarts / gallons, °F, miles y sq ft; la '
                  'métrica entre paréntesis para UK y Australia: «2 oz (59 ml)», «1.5 lb (0.68 kg)», «41°F (5°C)», '
                  '«200 sq ft (19 m²)»; botellas de 750 ml («a fifth») y 1.75 L («a handle»); coolers e ice bins en '
                  'quarts, gallons o lb, nunca en litros; distancias en miles; nada de m², kg, km ni °C como unidad '
                  'principal')

# ==========================================================================
# FIJOS (por TEXTO ES del FT: valen en cualquier celda de los 2 libros) y POR_CELDA (solo esa celda)
# ==========================================================================
FIJOS_FUERA = ('Este fichero forma parte del producto «plan-negocio-cafeteria» de AI Chef Pro.',)
_TITULO_CHECK = 'MOBILE BAR STARTUP CHECKLIST — DRY-HIRE MOBILE BARTENDING COMPANY'
FIJOS_NUEVOS = OrderedDict([
    ('Este fichero forma parte del producto «plan-negocio-food-truck» de AI Chef Pro.',
     'This file is part of the Mobile Bar Business Plan Kit by AI Chef Pro.'),
    # D91: título del checklist y de la fase 2 (el título de hoja no tiene el límite de 31 de la pestaña)
    ('CHECKLIST APERTURA — FOOD TRUCK', _TITULO_CHECK),
    ('FASE 2: VEHÍCULO Y PERMISOS', 'PHASE 2: TRAILER, LIQUOR RULES, PERMITS & INSURANCE'),
    ('INSTRUCCIONES DE USO — Plan financiero Food Truck', 'HOW TO USE THIS WORKBOOK — Mobile Bar Financial Projections'),
    ('PLAN DE NEGOCIO: FOOD TRUCK', 'BUSINESS PLAN: MOBILE BAR & EVENT BARTENDING'),
    ('Ajusta las cifras a tu proyecto.', 'US kit example (2026) — replace with your own quotes.'),
    ('Escenario realista — Food Truck urbano', 'Base case — mobile bar (dry hire)'),
    ('Break-even — Food Truck', 'Break-even — Mobile Bar'),
    # D88: cabecera de la tabla D19
    ('DATOS DE REFERENCIA DEL SECTOR', 'US MOBILE BAR BENCHMARKS (sourced) AND KIT ESTIMATES'),
    # motor de eventos (B4 = eventos/año, B5 = precio por invitado, B6 = invitados por evento) en todas las hojas
    ('Ticket medio SIN IVA (€)', 'Average price per guest (excl. sales tax and alcohol; bar package + add-ons)'),
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
    # D87: el canal de «delivery» del FT son los gig marketplaces (B16/B17)
    ('Comisiones de delivery', 'Gig marketplace fees'),
    # D87: las dos líneas de venta y su coste (los mismos textos ES salen en el P&L y en Escenarios)
    ('Coste de mercancía — comida', 'Cost of goods — bar packages (mixers, garnishes, ice)'),
    ('Coste de mercancía — bebida', 'Cost of goods — add-ons'),
    ('Consumibles y envases', 'Cups, straws, napkins and bar disposables'),
])

POR_CELDA = OrderedDict([
    # 0. Supuestos (D85, D87): mezcla de ventas y canal
    (('MBP', _S, 'A11'), 'BAR PACKAGES share of sales (bartending service, bar, mixers, garnishes, ice)'),
    (('MBP', _S, 'A12'), 'ADD-ONS share of sales (travel fees, extra hours, glassware, specialty bars)'),
    (('MBP', _S, 'A13'), 'Cost of goods on BAR PACKAGE sales (mixers, garnishes, ice, N/A drinks)'),
    (('MBP', _S, 'A14'), 'Cost of goods on ADD-ON sales'),
    (('MBP', _S, 'A15'), 'Cups, straws, napkins and bar disposables as % of sales'),
    (('MBP', _S, 'A16'), 'Share of sales booked through gig marketplaces (GigSalad, The Bash, Thumbtack)'),
    (('MBP', _S, 'A17'), 'Marketplace fee on those bookings'),
    (('MBP', _S, 'A23'), 'STORAGE, TRAILER PARKING AND FIXED COSTS'),
    (('MBP', _S, 'A24'), 'Storage unit & trailer parking, per month'),
    (('MBP', _S, 'A25'), 'Storage unit deposit (months)'),
    (('MBP', _S, 'A26'), 'Monthly utilities (storage unit power and water)'),
    (('MBP', _S, 'A44'), 'Useful life of the bar trailer and its conversion (years)'),
    (('MBP', _S, 'A45'), 'Useful life of bar equipment, glassware and software (years)'),
    (('MBP', _S, 'A51'), 'Max events a year your bars and crews can handle'),
    (('MBP', _S, 'A54'), 'Months of storage rent BEFORE opening'),
    (('MBP', _S, 'A55'), 'Contingency on the trailer, conversion and fit-out lines (%)'),
    (('MBP', _S, 'A62'), 'ALCOHOL as a share of add-on sales (0% in dry hire: the host buys it)'),
    # Startup Costs filas 7-23 y base de amortización (D87; research §8)
    (('MBP', _I, 'A7'), 'Bar trailer, used (6 x 12 ft cargo / concession or horse trailer)'),
    (('MBP', _I, 'A8'), 'Trailer conversion (bar top, cabinetry, hand sink, water tanks, LED, electrical)'),
    (('MBP', _I, 'A9'), 'Wrap, signage and bar facade'),
    (('MBP', _I, 'A10'), 'Portable bar for the second crew and indoor venues'),
    (('MBP', _I, 'A11'), 'Inverter generator and power'),
    (('MBP', _I, 'A12'), 'Storage unit fit-out (shelving, glass racks, wash station)'),
    (('MBP', _I, 'A13'), 'LLC formation, contracts and legal'),
    (('MBP', _I, 'A14'), 'First-year permits and certifications (business license, sales tax permit, TABC / RBS / TIPS)'),
    (('MBP', _I, 'A15'), 'Health permit / unit inspection (only if your county requires it)'),
    (('MBP', _I, 'A16'), 'Booking software, card reader and tablet'),
    (('MBP', _I, 'A17'), 'Bar tools and smallwares (4 stations)'),
    (('MBP', _I, 'A18'), 'Opening inventory (mixers, syrups, garnishes, cups, napkins)'),
    (('MBP', _I, 'A19'), 'Website, photos, launch and first bridal show'),
    (('MBP', _I, 'A20'), 'Glassware (300 pieces + racks), coolers, ice bins and dispensers'),
    (('MBP', _I, 'A21'), 'Storage unit deposit'),
    (('MBP', _I, 'A22'), 'Storage rent before opening'),
    (('MBP', _I, 'A23'), 'Trailer and fit-out contingency'),
    (('MBP', _I, 'A31'), 'Trailer, conversion and fit-out (depreciated over the trailer life)'),
    # 3-Year P&L (D87; research §8: fijos B26-B35)
    (('MBP', _P, 'A10'), 'Bar package sales (bartending service, bar, mixers, garnishes, ice)'),
    (('MBP', _P, 'A11'), 'Add-on sales (travel fees, extra hours, glassware, specialty bars)'),
    (('MBP', _P, 'A22'), 'Storage unit & trailer parking'),
    (('MBP', _P, 'A24'), 'Utilities (storage unit power and water)'),
    (('MBP', _P, 'A25'), 'Insurance (general and liquor liability, auto, workers\' comp)'),
    (('MBP', _P, 'A26'), 'Permits and certifications renewal'),
    (('MBP', _P, 'A27'), 'Vehicle and trailer fuel, maintenance and registration'),
    (('MBP', _P, 'A30'), 'Software (booking / CRM, e-signature, POS)'),
    (('MBP', _P, 'A31'), 'Glass washing, linens and bar towels'),
    (('MBP', _P, 'A32'), 'Phone and internet'),
    (('MBP', _P, 'A33'), 'Equipment repair and breakage'),
    (('MBP', _P, 'A34'), 'Staff training and server certifications (TIPS / TABC / RBS)'),
    (('MBP', _P, 'A35'), 'Tastings and cocktail menu consultations for prospects'),
    (('MBP', _P, 'A52'), 'Cost of goods sold (bar packages + add-ons)'),
    (('MBP', _P, 'A55'), 'Storage & parking / Sales'),
    (('MBP', _N, 'A20'), 'Storage & parking / Sales'),
    # Staffing (D87): 4 puestos, cobertura por evento, nota W-2 / propinas
    (('MBP', _R, 'A5'), 'Owner & Lead Bartender (sales and operations)'),
    (('MBP', _R, 'A6'), 'Second-crew lead bartender (part-time W-2)'),
    (('MBP', _R, 'A7'), 'Event bartenders (hourly W-2)'),
    (('MBP', _R, 'A8'), 'Barbacks / setup crew (hourly W-2)'),
    (('MBP', _R, 'A15'), 'COVERAGE OF EVENT HOURS'),
    (('MBP', _R, 'A18'), 'Hours per person per event (prep, loading, travel, setup, service, breakdown)'),
    (('MBP', _R, 'A19'), 'People per event (bartenders and barbacks, average)'),
    (('MBP', _R, 'A20'), 'Event hours to cover per year'),
    (('MBP', _R, 'A24'), 'Columns D-G are TOTALS for the row. Event bartenders and barbacks are hourly W-2 employees with '
                         'payroll taxes and workers\' comp: paying them as 1099 contractors is a misclassification risk '
                         '(FLSA; California AB5). Tips belong to the staff: the employer keeps none of them (FLSA).'),
    # 12-Month Cash Flow (D87): Month 1 = mes de apertura; el depósito no se modela
    (('MBP', _T, 'O5'), 'Share of the year\'s events per month (100% in total). Month 1 = opening month (March in the '
                        'example). The 30% deposit is not modeled: it improves real cash.'),
    # notas del motor que el catering ya había reescrito (m2, m4, m11): mismas reglas, con el bar móvil
    (('MBP', _S, 'C20'), 'FICA (Social Security 6.2% + Medicare 1.45%) + federal and state unemployment taxes (FUTA / '
                         'SUTA) + workers\' comp. The example uses a lean 10% with no benefits; the benchmarks table on '
                         '"Instructions" gives the bartender wage. Ask your payroll provider and carrier for your rate.'),
    (('MBP', _S, 'C39'), 'Example rate: state + local sales tax combined, applied to the whole invoice (bar service, '
                         'add-ons and service charge). Whether bartending services are taxable varies by state: '
                         'California taxes them (cdtfa.ca.gov). UK: 20% VAT on the service.'),
    (('MBP', _S, 'C67'), 'Minimum cushion of the plan above break-even (plan ÷ break-even − 1). The drop you can absorb is '
                         '1 − break-even ÷ plan: a 15% cushion lets events fall by about 13% before costs stop being covered'),
    (('MBP', _E, 'E24'), 'How far the plan sits above the cash break-even (plan ÷ break-even − 1); the drop you can absorb '
                         'is 1 − break-even ÷ plan. The required minimum is set in the "0. Assumptions" tab'),
])

# ==========================================================================
# Cifras ES prohibidas (D93: coctelería ES de línea B, F1-inventario §7), caso del catering EN y del FT EN, y el
# vocabulario vetado RX_BAR_NO (D93, con su lista blanca). Formato: (regex, motivo, excepción sobre el texto entero)
# ==========================================================================
def _num(n):
    """40030 → patrón que casa 40,030 · 40.030 · 40 030 · 40030 (y nada pegado a más dígitos)."""
    s = str(n)
    cab, cola = s[:-3], s[-3:]
    return r'(?<![\d.,])' + cab + r'[.,   ]?' + cola + r'(?![\d])'


CIFRAS_ES = (40030, 25580, 18000, 35000, 70000, 112500, 157500, 65000, 90000, 29400, 40600, 18220, 11180, 46410, 4635,
             17220, 31058, 52500, 127500, 2880, 2420)
FRASES_ES = [
    (r'(?i)\b31 events\b', 'break-even del xlsx ES (31 eventos/año)'),
    (r'(?i)\b50 events (?:a|per) year\b', 'caso ES (50 eventos/año)'),
    (r'(?i)\b2\.6 events (?:a|per) month\b', 'caso ES (2,6 eventos/mes)'),
    (r'(?i)\b42\s?% (?:gross )?margin\b|\bmargin of 42\s?%', 'margen ES (42 %)'),
    (r'(?i)\b58\s?% variable\b', 'ratio ES (58 % variable)'),
    (r'(?i)\b38\s?% (?:safety )?margin\b', 'margen de seguridad ES (38 %)'),
    (r'(?i)[$€]\s?1[,.]?400 (?:per|an?|each) event|1[,.]?400\s?€', 'precio ES (1.400 €/evento)'),
    (r'(?i)\$169 (?:per|an?) hour', 'tarifa ES ($169/h)'),
    (r'(?i)\b12\s?[-–]\s?18 per (?:person|guest)\b', 'rango ES (12-18 por persona)'),
    (r'(?i)\b4\s?[-–]\s?7\s?x\b', 'multiplicador ES (4-7x)'),
    (r'(?i)\b4[,.]500 million\b', 'mercado ES (4.500 M)'),
    (r'(?i)\b170[,.]000 weddings\b', 'mercado ES (170.000 bodas)'),
    (r'(?i)\b96 (?:validated )?suppliers\b', 'promesa ES (96 proveedores)'),
    (r'(?i)\b71 (?:tasks|steps|milestones)\b', 'recuento del checklist ES (71 tareas)'),
    (r'(?i)\b10 (?:real|validated) examples\b', 'promesa ES (10 ejemplos reales)'),
    (r'(?i)\b18\s?[-–]\s?35\s?K\b', 'inversión ES (18-35K)'),
    (r'\bv1\.1\b|\b[Vv]ersion 1\.1\b', 'historia de versiones (la EN nace en 2.2)'),
]
# lista blanca de la regla de legal: «commissary» y «food» valen si el texto habla del condado / health department
_LEGAL = r'(?i)\bcount(?:y|ies)\b|health (?:department|permit)|FDA Food Code'
_FIRMA = r'John Guerrero'
RX_BAR_NO = [
    # heredado del FT (D72)
    (r'(?i)\bper day\b', 'vocabulario FT («per day»)', None),
    (r'(?i)\boperating days?\b', 'vocabulario FT («operating days»)', None),
    (r'(?i)(?<!corporate )\bcustomers\b', 'vocabulario FT («customers» → clients / guests / hosts)',
     r'^Synthetic paragraph \d+ of the \w+ plan for the assembly test'),
    (r'(?i)\btrucks?\b', 'vocabulario FT («truck» → tow vehicle / pickup / trailer)', None),
    (r'(?i)\bwindows?\b', 'vocabulario FT («window»)', None),
    (r'(?i)\bfestivals?\b', 'vocabulario FT («festival»)', None),
    # del catering de comida (F1-inventario §7)
    (r'(?i)(?<!mobile )(?<!FDA )\bfood\b(?! handlers?\b| code\b| vendors?\b)', 'catering de comida («food»)', _LEGAL),
    (r'(?i)\bkitchens?\b', 'catering de comida («kitchen»)', _FIRMA),
    (r'(?i)\bcommissar(?:y|ies)\b', 'catering de comida («commissary»)', _LEGAL),
    (r'(?i)(?<!AI )\b(?:sous )?chefs?\b', 'catering de comida («chef»)', _FIRMA),
    (r'(?i)\bprep cooks?\b', 'catering de comida («prep cook»)', None),
    (r'(?i)\bplated\b', 'catering de comida («plated»)', None),
    (r'(?i)\bbuffets?\b', 'catering de comida («buffet»)', None),
    (r'(?i)\bdrop-?offs?\b', 'catering de comida («drop-off»)', None),
    (r'(?i)\bfamily-style\b', 'catering de comida («family-style»)', None),
    (r'(?i)\b(?:chef-attended|themed) stations?\b', 'catering de comida («themed stations»)', None),
    (r'(?i)\bchafing\b', 'catering de comida («chafing»)', None),
    (r'(?i)\b(?:hotel|sheet) pans?\b', 'catering de comida («hotel / sheet pans»)', None),
    (r'(?i)\brecipe costing\b', 'catering de comida («recipe costing» → cost per guest)', None),
    (r'(?i)\bboxed lunch', 'catering de comida («boxed lunch»)', None),
    (r'(?i)\bezCater\b', 'catering de comida («ezCater»)', None),
    (r'(?i)\bbroadline\b', 'catering de comida («broadline»)', None),
    (r'\bHACCP\b', 'catering de comida («HACCP»)', None),
    (r'(?i)ServSafe Manager|Certified Food Protection Manager', 'catering de comida («ServSafe Manager»)', None),
    (r'(?i)(?<!alcohol )\bservers?\b(?! certification)', 'catering de comida («servers» → bartenders / barbacks)', None),
    (r'(?i)\bgrease\b', 'catering de comida («grease»)', None),
    (r'(?i)\bpest control\b', 'catering de comida («pest control»)', None),
    (r'(?i)\bper plate\b', 'catering de comida («per plate»)', None),
    # del ES de coctelería
    (r'\bEspaña\b|\bSpain\b', 'ES («España»)', None),
    (r'Bodas\.net|Zankyou|CateringClick|Hosply|\bGGM\b|Coalimentaria|\bMakro\b', 'proveedor / directorio ES', None),
    (r'\bIVA\b', 'ES («IVA»)', None),
    (r'\bVAT\b', 'ES («VAT» fuera de la nota UK)', r'\bUK\b|United Kingdom|HMRC'),
    (r'(?i)\baut[oó]nomo\b|\bRETA\b|\bICO\b', 'trámite ES (autónomo / RETA / ICO)', None),
    (r'\bEUR\b|€', 'moneda ES', None),
    # regla de jerga §0 (research §9)
    (r'(?i)\bauthor cocktails?\b', 'jerga (§0): «author cocktails» → signature cocktails', None),
    (r'(?i)\bfree-?lance', 'jerga (§0): «freelance» → W-2 event bartender', None),
    (r'(?i)\bcocktail catering\b|\bitinerant bar', 'jerga (§9a): nunca «cocktail catering» ni «itinerant bar»', None),
    (r'(?i)\balcohol handler card', 'jerga (§9 #32): nunca «alcohol handler card»', None),
]


def _cifras_caso(path, plan):
    """Importes ≥ 10,000 del caso EN publicado de otro conjunto (no se reutilizan aquí)."""
    if not os.path.exists(path):
        return []
    d = json.load(open(path, encoding='utf-8')).get(plan, {})
    out = set()
    for t, x in d.items():
        v = x.get('valor') if isinstance(x, dict) else None
        if isinstance(x, dict) and x.get('fmt') == 'usd' and isinstance(v, (int, float)) and abs(v) >= 10000:
            out.add(int(round(abs(v))))
    return sorted(out)


FRASES_CAT = [(r'(?i)\b180 events\b', 'caso del catering EN («180 events»)'),
              (r'(?i)\$60(?:\.00)? (?:per|a) guest\b', 'caso del catering EN («$60 per guest»)')]


# ==========================================================================
# Tokens del docx (D92): los del motor con descripciones de bar móvil + alias legibles + partidas propias
# ==========================================================================
_DESC = OrderedDict([
    ('clientes_dia', 'EVENTS per year, year 1 (alias heredado: usa {{eventos_a1}})'),
    ('clientes_a2', 'EVENTS per year, year 2 (alias: usa {{eventos_a2}})'),
    ('clientes_a3', 'EVENTS per year, year 3 (alias: usa {{eventos_a3}})'),
    ('ticket', 'average price per guest excl. sales tax (alias: usa {{precio_invitado}})'),
    ('precio_menu', 'price per guest incl. sales tax (alias: usa {{precio_invitado_con_tax}})'),
    ('dias', 'average guests per event (alias: usa {{invitados_evento}})'),
    ('crecimiento_a2', 'growth in EVENTS in year 2'), ('crecimiento_a3', 'growth in EVENTS in year 3'),
    ('consumibles_pct', 'cups, straws, napkins and bar disposables, % of sales'),
    ('tarjeta_pct', 'card processing fees, % of sales (private hosts pay deposits and balances by card)'),
    ('alquiler_mes', 'storage unit & trailer parking, per month'),
    ('suministros_mes', 'utilities per month (storage unit power and water)'),
    ('seguros_anual', 'insurance per year (general + liquor liability, commercial auto with the trailer, workers\' comp, '
                      'equipment)'),
    ('vida_obra', 'useful life of the bar trailer and its conversion, years'),
    ('vida_equipo', 'useful life of bar equipment, glassware and software, years'),
    ('ocupacion_anual', 'storage unit & trailer parking per year'),
    ('ocupacion_pct', 'storage unit & trailer parking, % of sales'),
    ('cogs_pct', 'cost of goods (mixers, garnishes, ice, add-ons), % of sales; no alcohol in dry hire'),
    ('equilibrio_clientes_dia', 'break-even EVENTS per year, accounting (alias: usa {{equilibrio_eventos}})'),
    ('equilibrio_caja_clientes_dia', 'cash break-even EVENTS per year (alias: usa {{equilibrio_caja_eventos}})'),
    ('pesimista_clientes', 'pessimistic scenario: events per year (alias: usa {{pesimista_eventos}})'),
    ('optimista_clientes', 'optimistic scenario: events per year (alias: usa {{optimista_eventos}})'),
    ('pesimista_ticket', 'pessimistic scenario: price per guest (alias: usa {{pesimista_precio}})'),
    ('optimista_ticket', 'optimistic scenario: price per guest (alias: usa {{optimista_precio}})'),
    ('pesimista_dias', 'pessimistic scenario: guests per event (alias: usa {{pesimista_invitados}})'),
    ('optimista_dias', 'optimistic scenario: guests per event (alias: usa {{optimista_invitados}})'),
    ('inv_vehiculo', 'bar trailer, used (6 x 12 ft cargo / concession or horse trailer)'),
    ('inv_adaptacion', 'trailer conversion (bar top, cabinetry, hand sink, water tanks, LED, electrical)'),
    ('inv_permisos', 'first-year permits and certifications (business license, sales tax permit, TABC / RBS / TIPS)'),
    ('inv_lanzamiento', 'website, photos, launch and first bridal show'),
    ('inv_stock', 'opening inventory (mixers, syrups, garnishes, cups, napkins; no alcohol)'),
    ('horas_semana', 'full-time hours per week'),
])
# fuera: ventas ÷ «días» no significa nada; las filas 9-10 del FT son aquí otras partidas (alias propios abajo); los
# nombres «food_cost_*» no se usan (alias neutros coste_paquetes_pct / coste_extras_pct)
_FUERA = ('ventas_dia', 'inv_equipo_cocina', 'inv_generador', 'food_cost_comida', 'food_cost_bebida')
TOKENS_PROPIOS = OrderedDict([
    # alias legibles del motor (las mismas celdas que los tokens heredados)
    ('eventos_a1', ('int', ('fila', _S, 'Clientes/día (media del año 1)', 'B'), 'events per year, year 1')),
    ('eventos_a2', ('int', ('fila', _P, 'Clientes/día (media)', 'C'), 'events per year, year 2')),
    ('eventos_a3', ('int', ('fila', _P, 'Clientes/día (media)', 'D'), 'events per year, year 3')),
    ('precio_invitado', ('usd2', ('fila', _S, 'Ticket medio SIN IVA (€)', 'B'),
                         'average price per guest, excl. sales tax and alcohol (bar package + add-ons)')),
    ('precio_invitado_con_tax', ('usd2', ('fila', _S, 'PVP equivalente con IVA (calculado)', 'B'),
                                 'average price per guest incl. sales tax')),
    ('invitados_evento', ('int', ('fila', _S, 'Días de apertura al año', 'B'), 'average guests per event')),
    ('capacidad_eventos', ('int', ('fila', _S, {'mbar': 'Plazas de pie y mesas altas junto al vehículo'}, 'B'),
                           'max events a year the bars and crews can handle (information only)')),
    ('cuota_paquetes_pct', ('pct0', ('fila', _S, 'Ventas de COMIDA sobre el total', 'B'),
                            'bar packages, % of sales (the rest are add-ons)')),
    ('coste_paquetes_pct', ('pct0', ('fila', _S, 'Coste de mercancía sobre las ventas de COMIDA', 'B'),
                            'cost of goods on bar package sales (mixers, garnishes, ice, N/A drinks)')),
    ('coste_extras_pct', ('pct0', ('fila', _S, 'Coste de mercancía sobre las ventas de BEBIDA', 'B'),
                          'cost of goods on add-on sales')),
    ('marketplace_pct', ('pct0', ('fila', _S, 'Ventas por delivery sobre el total', 'B'),
                         'share of sales booked through gig marketplaces (GigSalad, The Bash, Thumbtack)')),
    ('marketplace_comision', ('pct0', ('fila', _S, 'Comisión de la plataforma de delivery', 'B'),
                              'marketplace fee on those bookings')),
    ('cobro_dias', ('int', ('fila', _S, 'Días medios de cobro', 'B'), 'average collection days')),
    ('horas_evento', ('dec1', ('fila', _R, 'Horas de servicio al día que hay que cubrir', 'B'),
                      'hours per person per event (prep, loading, travel, setup, service, breakdown)')),
    ('personas_evento', ('dec1', ('fila', _R, 'Personas necesarias a la vez en cada franja', 'B'),
                         'people per event (bartenders and barbacks, average)')),
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
    # partidas de la inversión del bar móvil (D87: filas 9-20)
    ('inv_fachada', ('usd', ('fila', _I, {'mbar': 'Equipamiento cocina móvil'}, 'B'), 'wrap, signage and bar facade')),
    ('inv_barra_portatil', ('usd', ('fila', _I, {'mbar': 'Generador eléctrico o conexión'}, 'B'),
                            'portable bar for the second crew and indoor venues')),
    ('inv_energia', ('usd', ('fila', _I, {'mbar': 'Instalación gas (si aplica)'}, 'B'), 'inverter generator and power')),
    ('inv_almacen', ('usd', ('fila', _I, {'mbar': 'Depósito de agua + aguas residuales'}, 'B'),
                     'storage unit fit-out (shelving, glass racks, wash station)')),
    ('inv_llc', ('usd', ('fila', _I, {'mbar': 'Constitución SL + notaría + registro'}, 'B'),
                 'LLC formation, contracts and legal')),
    ('inv_health_permit', ('usd', ('fila', _I, {'mbar': 'Proyecto técnico sanitario'}, 'B'),
                           'health permit / unit inspection (only if the county requires it)')),
    ('inv_software', ('usd', ('fila', _I, {'mbar': 'TPV móvil + datáfono'}, 'B'), 'booking software, card reader and tablet')),
    ('inv_herramientas', ('usd', ('fila', _I, {'mbar': 'Menaje, utensilios, packaging eco'}, 'B'),
                          'bar tools and smallwares (4 stations)')),
    ('inv_cristaleria', ('usd', ('fila', _I, {'mbar': 'Toldo, mobiliario exterior plegable'}, 'B'),
                         'glassware (300 pieces + racks), coolers, ice bins and dispensers')),
    # derivadas
    ('ventas_evento', ('usd', ('deriv', lambda c: c['ventas_a1'] / c['clientes_dia']),
                       'average revenue per event, year 1 (excl. sales tax and alcohol)')),
    ('invitados_a1', ('int', ('deriv', lambda c: c['clientes_dia'] * c['dias']), 'guests served in year 1')),
    ('caida_absorbible_pct', ('pct0', ('deriv', lambda c: c['holgura_caja_pct'] / (1 + c['holgura_caja_pct'])),
                              'drop in events the plan can absorb before cash stops covering costs (1 − break-even ÷ plan)')),
])


def tokens_mbar(base):
    out = OrderedDict()
    for t, (fmt, src, desc) in base.items():
        if t in _FUERA:
            continue
        if src[0] == 'fila':
            _, hoja, rot, col = src
            if isinstance(rot, dict):
                if 'ft' not in rot:
                    continue                               # partidas de la cafetería
                src = ('fila', hoja, {'mbar': rot['ft']}, col)
        out[t] = (fmt, src, _DESC.get(t, desc))
    out.update(TOKENS_PROPIOS)
    return out


# ==========================================================================
# Docx (D92): lo que escribe ensamblar_docx.py y las notas para los redactores
# ==========================================================================
PRODUCTOS_CIERRE_MBAR = ['Bar Business Plan Kit', 'Catering Business Plan Kit', 'Restaurant Staff Scheduling Kit Pro',
                         'Gastro Pro Prompts eBook (300+ AI prompts)']


def docx_fijos(M):
    pc = PRODUCTOS_CIERRE_MBAR
    d = OrderedDict([
        (6, 'BUSINESS PLAN'), (7, 'Mobile Bar'),
        # sin «dry hire» en la portada: su primera mención (con la glosa, §0) la escribe el redactor en §1
        (9, 'Complete financial plan, market analysis,\noperations strategy and startup checklist\nto launch a mobile '
            'bar and event bartending company in the United States'),
        (14, 'AI Chef Pro'), (15, 'aichef.pro'), (16, 'US edition with UK notes · 2026'),
        (18, 'LEGAL NOTICE'), (19, M.AVISO_DOCX_EN), (20, '© 2026 AI Chef Pro — aichef.pro'), (22, 'CONTENTS'),
        (35, 'Appendices: Mobile Bar Financial Projections (Excel) + Mobile Bar Pricing Calculator (Excel) + Mobile Bar '
             'Startup Checklist (Excel)'),
        (123, 'AI Chef Pro'), (124, 'Templates and AI tools for hospitality businesses'),
        (126, 'aichef.pro\ninfo@aichef.pro'),
        (127, '→ %s · %s' % tuple(pc[:2])), (128, '→ ' + pc[2]), (129, '→ ' + pc[3]), (130, '\n' + M.URL_TIENDA),
    ])
    return OrderedDict([('mbar', d)])


DOCX_NOTAS_PLAN = OrderedDict([
    ('mbar', 'ESCRIBES, NO TRADUCES (D92). El «es» de cada párrafo es la RANURA del plan de FOOD TRUCK (solo da el '
             'papel del párrafo y su longitud aproximada); el EN publicado del catering de esa misma ranura '
             '(../business-plans-en-4/docx_en_cat_a.json / _b.json) sirve de modelo de estructura. El contenido es de '
             'un MOBILE BAR EN DRY HIRE (D84), desde fuente_es_mbar.json (plan ES de coctelería: concepto, segmentos, '
             'propuesta de valor, modalidades de precio, embudo B2B, operativa, equipo, KPIs; carta de cócteles; las '
             '10 experiencias temáticas) y research §1, §5, §6, §8 y §9 (glosario OBLIGATORIO, regla de jerga §0). '
             'Primera mención de «dry hire» con la glosa «' + GLOSA_DRY_HIRE + '». Cifras del caso SOLO con tokens '
             '{{…}}; de mercado, solo las de research «leída» con su fuente. Prohibido (gate): «food truck», «truck» '
             '(el vehículo de arrastre es «tow vehicle» o «pickup»), «per day», «operating days», «customers» (di '
             'clients / guests / hosts), «window», «festival», vocabulario de catering de comida (food salvo «food '
             'handler card» / «FDA Food Code» / «mobile food vendors», kitchen, commissary salvo hablando del condado, '
             'chef, buffet, plated, drop-off, servers salvo «alcohol server certification»), «freelance», «author '
             'cocktails», «cocktail catering», las cifras del ES de coctelería (40.030, 70.000, «50 eventos/año», «42 '
             '%», «1.400 €/evento»…) y del caso del catering ($648,000, «180 events», «$60 per guest»), «España», '
             '«ChefBusiness». «cash bar» solo para decir que está prohibida en dry hire. ' + REGLA_UNIDADES + '. El '
             'cierre (productos) lo escribe el ensamblador'),
])
_N9 = OrderedDict([
    (102, 'D92 §9 1/7: DRY HIRE = el modelo legal del kit. Missouri lo dice por escrito (Industry Circular 24-01, '
          'atc.dps.mo.gov: «There is no requirement that a person, who solely provides bartending services, must get a '
          'state liquor license») y avisa de que las entradas, propinas / gratuities / donativos y los recargos sobre '
          'el alcohol pueden ser «venta». Condiciones: el anfitrión compra y es dueño del alcohol; si lo compras tú, '
          'solo como su agente, autorizado por escrito, a coste con ticket y sin margen; lo que sobra es suyo; sin '
          'cash bar, tickets de copa ni entrada que incluya bebida; factura con el servicio separado de los reembolsos'),
    (103, '§9 2/7: Montana (revenue.mt.gov, Mobile Bars fact sheet): el bar móvil «may not pre-stock», el anfitrión '
          'compra el alcohol aparte, solo eventos privados, sin cobrar copas a los invitados. Regla general: «varies by '
          'state»: pregunta a la autoridad de alcohol de tu estado (ABC / TABC…) antes de la primera reserva y guarda '
          'la respuesta por escrito'),
    (104, '§9 3/7: full-service (con alcohol) por estado, como OPCIÓN, no el caso: TX Caterer\'s Permit auxiliar del '
          'Mixed Beverage Permit, ligado a una dirección fija; CA sin licencia en un evento privado sin entrada ni '
          'cobro por copa y con el alcohol del anfitrión, y el Type 58 solo para licenciatarios on-sale; FL: vender '
          'sin licencia es delito (barra de pago solo con un socio con licencia 13CT); NY: Caterer\'s Alcohol Permit '
          'de la SLA, por evento (nyc-business.nyc.gov) → en NY, consultar. Vías: socio licenciatario, licencia '
          'propia ligada a un local, permiso por evento donde exista'),
    (105, '§9 4/7: health permit: no hay una norma específica de «mobile bar»; algunos condados aplican por analogía '
          'las de mobile food vendors (permiso, inspección de la unidad, garnish cortado, hielo). Pregunta al health '
          'department de tu condado; usa hielo comercial embolsado; lavamanos en el remolque; el ejemplo reserva '
          '{{inv_health_permit}} para la inspección'),
    (106, '§9 5/7: sales tax: California grava el servicio del caterer «even if you do not provide the food or '
          'beverages» (cdtfa.ca.gov), así que el servicio de barra tributa; en otros estados depende de si el '
          'servicio y el alquiler de barra y cristalería tributan → el libro aplica {{sales_tax}} a toda la factura '
          '(conservador). Service charge ≠ gratuity: el obligatorio es salario (IRS Rev. Rul. 2012-18); la gratuity '
          'voluntaria va aparte y es del personal. Sales tax permit del estado'),
    (107, '§9 6/7: empleo y seguros: bartenders y barbacks W-2 (FLSA; California AB5 presume empleo), workers\' comp, '
          'I-9 / W-4; las propinas son del personal (FLSA). Seguros: general liability + liquor liability aparte (la '
          'GL suele excluir el alcohol; para un bartender móvil, desde $550 al año: insurancecanopy.com), commercial '
          'auto que cubra el remolque, workers\' comp y equipo ({{seguros_anual}} al año en el ejemplo); COI y '
          'additional insured para los venues; host liquor liability la contrata el cliente. Certificación: en TX el '
          'safe harbor (§106.14) protege al empleador con personal certificado; CA exige RBS a los licenciatarios'),
    (108, '§9 7/7: el remolque (título y registro en el DMV, commercial auto) y, como ÚLTIMA frase o frases del '
          'párrafo, la nota UK: toda venta en un local con premises licence la autoriza un titular de personal licence '
          '(18+, APLH Level 2, ante el council), que no hace falta para vender con un Temporary Event Notice (TEN: '
          '£21, menos de 500 personas, hasta 168 h, 5 al año o 50 con personal licence, 10 días hábiles antes; '
          'gov.uk); en un local con licencia se trabaja bajo la del local; una entrada que incluya bebidas es venta'),
])
_NOTAS_SECCION = OrderedDict([
    (39, '§1 1/5: la oportunidad: bares móviles para bodas, eventos de empresa y fiestas privadas en EE. UU.; demanda '
         'solo con research §2 (búsquedas: «mobile bar business» 480/mes, «dry hire mobile bar» 390) sin tamaño de '
         'mercado inventado'),
    (40, '§1 2/5: el concepto (D84): mobile bar & bartending service en DRY HIRE — PRIMERA mención con la glosa «'
         + GLOSA_DRY_HIRE + '»; remolque-barra convertido + barra portátil para el 2.º equipo; bartenders W-2 '
         'certificados, signature cocktails, mixers / garnish / hielo / vasos incluidos, setup & breakdown y una '
         'shopping list para el anfitrión'),
    (41, '§1 3/5: inversión y financiación SOLO con tokens: {{inversion_total}} = {{capex}} + {{fondo_maniobra}}; '
         '{{fondos_propios}} ({{aportacion_pct}}) + préstamo {{prestamo}} al {{tipo_prestamo}} a {{plazo_prestamo}} '
         'años; el vehículo de arrastre es el del dueño'),
    (42, '§1 4/5: proyecciones: {{eventos_a1}} eventos × {{invitados_evento}} invitados × {{precio_invitado}} → '
         '{{ventas_a1}} / {{ventas_a2}} / {{ventas_a3}}; EBITDA {{ebitda_pct_a1}}; equilibrio {{equilibrio_eventos}} '
         'eventos/año; DSCR mínimo {{dscr_min}}; y la frase honesta (D85): es el caso de un operador a tiempo '
         'completo con 2 equipos, no la media del sector'),
    (43, '§1 5/5: el equipo: Owner & Lead Bartender que también vende, second-crew lead bartender, event bartenders y '
         'barbacks W-2 ({{plantilla_puestos}} personas, {{plantilla_jornadas}} FTE); sin inventar trayectoria'),
    (46, '§2 1/5: qué vende y a quién: parejas (bodas), empresas (holiday parties, eventos de clientes) y anfitriones '
         'privados (cumpleaños, aniversarios, inauguraciones); el cliente compra una barra que funciona sin que tenga '
         'que pensar en ella, no copas'),
    (47, '§2 2/5: propuesta de valor del ES («cero complejidad»): barra, bartenders, cristalería, hielo, mixers y '
         'garnish; signature cocktails y un mocktail siempre en la carta; setup & breakdown incluidos; la shopping '
         'list para que el anfitrión compre justo lo necesario'),
    (48, '§2 3/5: paquetes y precio: bar packages por invitado ({{precio_invitado}} de media sin sales tax ni alcohol, '
         '{{ventas_evento}} por evento) con su equivalente por hora; add-ons (travel fee, extra hour of service, '
         'cristalería, champagne service, specialty bars); depósito del 30 % para bloquear la fecha (Check Cherry); '
         'gratuity voluntaria fuera; en dry hire nunca se cobran copas'),
    (49, '§2 4/5: el diferencial: specialty bars (las 10 experiencias temáticas del ES → mimosa bar, espresso martini '
         'bar, tiki, speakeasy, gin…) con recargo; carta de signature cocktails personalizada con el nombre de la '
         'pareja o de la empresa'),
    (50, '§2 5/5: los tres paquetes de la calculadora del kit (full bar – dry hire · limited bar – dry hire · full '
         'bar – licensed, solo con licencia), el mínimo de contratación y la hora extra'),
    (53, '§3 1/6: el mercado US desde el lado del cliente: research §2 (búsquedas) y §5 (Check Cherry, 1.334 reservas: '
         'mediana $750 por evento sin alcohol ni propinas, 50 % central $450-$1,275), sin tamaño de mercado inventado'),
    (54, '§3 2/6: bodas: precio por invitados y por duración (Check Cherry: 4 h $675, 101-150 invitados $1,063); '
         'reserva con 62 días de mediana; peak wedding season mayo-junio y septiembre-octubre'),
    (55, '§3 3/6: empresas y fiestas privadas: holiday parties en diciembre y eventos entre semana; cumpleaños y '
         'aniversarios; el 85 % de las reservas cae de viernes a domingo y la mitad en sábado (Check Cherry)'),
    (56, '§3 4/6: mezcla del ejemplo (Kit estimate: 60 bodas, 45 eventos de empresa y 55 fiestas privadas; las bodas '
         'son 37.5 % de los eventos y 48 % de las ventas) y estacionalidad (Month 1 = marzo; octubre ~13 %, mayo '
         '12.4 %, enero 3.8 %: Check Cherry)'),
    (57, '§3 5/6: tendencias con cuidado: mocktails y zero-proof, specialty bars, cartas personalizadas; sin cifras '
         'sin fuente'),
    (58, '§3 6/6: riesgos de demanda y REALISMO (D85): la mediana de un bar móvil nuevo hace 3 eventos el primer año '
         'y el top 10 % unos 39 (Check Cherry); el caso del kit es el de un operador a tiempo completo con 2 equipos '
         'y presupuesto de marketing, no la media'),
    (61, '§4 1/6: panorama competitivo local: otros bares móviles y bartending services, venues con barra propia, '
         'caterers con licencia, bartenders sueltos en marketplaces'),
    (62, '§4 2/6: cinco fuerzas de Porter aplicadas a un bar móvil (estructura del ES)'),
    (63, '§4 3/6: competidores directos e indirectos y cómo compararse (precio por invitado o por hora, qué incluye, '
         'reseñas en The Knot, WeddingWire, Zola, GigSalad y Google)'),
    (64, '§4 4/6: barreras de entrada: bajas con una barra portátil (desde ~$1,000, Check Cherry), más altas con un '
         'remolque convertido; seguros (liquor liability), certificaciones y reglas de alcohol de cada estado'),
    (65, '§4 5/6: factores críticos de éxito: puntualidad del montaje, servicio responsable, reseñas, relación con '
         'venues y wedding planners, una barra que sale en las fotos'),
    (66, '§4 6/6: DAFO del concepto (dry hire, remolque, 2 equipos)'),
    (69, '§5 1/7: estrategia: dos embudos (bodas: ciclo largo con degustación; empresas y fiestas: recurrencia y '
         'referidos)'),
    (70, '§5 2/7: presencia digital: web con paquetes y precios «desde», formulario de presupuesto, Google Business '
         'Profile, Instagram y Pinterest'),
    (71, '§5 3/7: directorios y marketplaces: The Knot, WeddingWire, Zola, GigSalad (comisión del libro: '
         '{{marketplace_comision}}), The Bash, Thumbtack'),
    (72, '§5 4/7: alianzas: venues (preferred vendor lists), wedding planners, fotógrafos y DJs; bridal shows'),
    (73, '§5 5/7: degustaciones y consultas de carta (su línea de coste en el P&L) y el proceso propuesta → contrato → '
         'depósito'),
    (74, '§5 6/7: fidelización y referidos: empresas que repiten cada diciembre, reseñas después de cada evento'),
    (75, '§5 7/7: presupuesto: {{marketing_anual}} al año en el ejemplo; medir el coste por evento ganado'),
    (78, '§6 1/5: la base: storage unit & trailer parking ({{alquiler_mes}} al mes en el ejemplo); qué se guarda, cómo '
         'se lava y se cuenta la cristalería'),
    (79, '§6 2/5: el equipo: bar trailer usado {{inv_vehiculo}} + conversión {{inv_adaptacion}}, barra portátil '
         '{{inv_barra_portatil}}, generador {{inv_energia}}, cristalería y coolers {{inv_cristaleria}}; el tow vehicle '
         'es el del dueño (si no lo tienes, una pickup usada cuesta $10,000-$30,000: Check Cherry)'),
    (80, '§6 3/5: la operativa de un evento del ES: brief D-21 → visita técnica D-14 → shopping list al anfitrión D-14 '
         '→ mixers, garnish y hielo D-1 → montaje 60-120 min → servicio de 4-5 h con last call → desmontaje; 1 '
         'bartender por 50 invitados con barra completa'),
    (81, '§6 4/5: hielo, garnish y copas: hielo comercial embolsado (1.5 lb, 0.68 kg, por invitado: Kit estimate), garnish '
         'cortado según lo que permita el condado; 2 copas por invitado la primera hora + 1 por hora después '
         '(eventplanning.com); mocktail siempre; alérgenos (orgeat, coco)'),
    (82, '§6 5/5: proveedores (mixers, siropes, garnish, hielo, desechables), party rentals y mantenimiento del '
         'remolque y del vehículo'),
    (85, '§7 1/6: estructura: Owner & Lead Bartender (ventas y operación), second-crew lead bartender (part-time W-2), '
         'event bartenders (hourly W-2), barbacks / setup crew (hourly W-2)'),
    (86, '§7 2/6: coste de personal: {{personal_a1}} el año 1 ({{personal_pct}} de las ventas), con el sueldo del '
         'dueño dentro'),
    (87, '§7 3/6: personal por evento: {{horas_evento}} horas por persona × {{personas_evento}} personas por evento, '
         'cobertura {{cobertura_horas}}; 1 bartender por 50 invitados con barra completa y 1 por 75 con cerveza y '
         'vino (Kit estimate)'),
    (88, '§7 4/6: W-2 frente a 1099 (FLSA; California AB5), nada de «freelance»; cargas {{cargas_pct}}; mínimo federal '
         'y estatal; sueldo de bartender BLS mayo 2025: media $19.61/h, mediana $16.51/h (incluye propinas)'),
    (89, '§7 5/6: formación: alcohol server certification (TABC, RBS, TIPS / ServSafe Alcohol), servicio responsable '
         '(ID, menores, invitados ebrios, last call), carta y specs de los signature cocktails'),
    (90, '§7 6/6: service charge frente a propina (IRS Rev. Rul. 2012-18); las propinas son del personal (FLSA); tip '
         'jar solo donde el estado no lo trate como venta (MO)'),
    (93, '§8 1/7: viabilidad: ventas del año 1 {{ventas_a1}}, margen bruto {{margen_bruto_pct}}, EBITDA {{ebitda_a1}} '
         '({{ebitda_pct_a1}}); {{ventas_evento}} por evento frente a la mediana de $750 de Check Cherry: el caso '
         'está en el cuartil alto (remolque, mixers y hielo incluidos, 2 equipos)'),
    (94, '§8 2/7: inversión con tokens: {{inv_vehiculo}}, {{inv_adaptacion}}, {{inv_fachada}}, {{inv_barra_portatil}}, '
         '{{inv_energia}}, {{inv_cristaleria}}, {{inv_permisos}}, {{inv_lanzamiento}}, {{inv_stock}} → {{capex}}; '
         'fondo de maniobra {{fondo_maniobra}}; total {{inversion_total}}; financiación'),
    (95, '§8 3/7: proyección a 3 años: {{ventas_a1}} / {{ventas_a2}} / {{ventas_a3}} (crecen los EVENTOS: '
         '{{crecimiento_a2}} y {{crecimiento_a3}}); resultado neto {{resultado_neto_a1}} / {{resultado_neto_a2}} / '
         '{{resultado_neto_a3}}'),
    (96, '§8 4/7: costes: mixers, garnish y hielo {{coste_paquetes_pct}} de los paquetes, mercancía total '
         '{{cogs_pct}}, desechables {{consumibles_pct}}, personal {{personal_pct}}, storage y parking '
         '{{ocupacion_pct}}; el alcohol lo paga el anfitrión'),
    (97, '§8 5/7: punto de equilibrio en EVENTOS al año: {{equilibrio_eventos}} (contable) y '
         '{{equilibrio_caja_eventos}} (caja) frente a {{eventos_a1}} del plan; holgura {{holgura_caja_pct}} (los '
         'eventos pueden caer {{caida_absorbible_pct}} antes de no cubrir la caja)'),
    (98, '§8 6/7: caja y retorno: saldo mínimo {{saldo_minimo}} en el mes {{mes_saldo_minimo}}, payback {{payback}}, '
         'DSCR {{dscr_min}}; el depósito del 30 % no se modela y mejora la caja real'),
    (99, '§8 7/7: escenarios: pesimista {{pesimista_eventos}} eventos × {{pesimista_precio}} × {{pesimista_invitados}} '
         'invitados → {{pesimista_ventas}}, resultado {{pesimista_resultado}} y caja estimada {{pesimista_caja}} (si '
         'es negativa, DECIRLO: la caja se agota); optimista {{optimista_ventas}}; recordar que la mediana del primer '
         'año son 3 eventos'),
    (111, '§10 1/7: conclusión: por qué el modelo se sostiene (dry hire: sin inventario de alcohol ni licencia; '
          'capital bajo; dos motores de demanda) y la advertencia honesta del caso'),
    (112, '§10 2/7: riesgos y mitigación: cancelación (depósito y política), un invitado ebrio o menor de edad '
          '(certificación, servicio responsable, liquor liability), avería del remolque o del vehículo, lluvia en '
          'exterior, rotura de cristal, falta de bartenders los sábados, cambios en las reglas de alcohol del estado'),
    (113, '§10 3/7: fortalezas competitivas (remolque que se fotografía, specialty bars, 2 equipos, contrato dry hire '
          'limpio)'),
    (114, '§10 4/7: hoja de ruta en las 6 fases del checklist (Business Setup → Trailer & Permits → Equipment → Staff '
          '→ Marketing → First 90 Days)'),
    (115, '§10 5/7: KPIs: eventos al mes, precio por invitado, coste por invitado (mixers, garnish, hielo), horas de '
          'personal por evento, conversión de propuestas, cancelaciones, reseñas'),
    (116, '§10 6/7: visión a 3 años: más empresas recurrentes, un tercer equipo o un segundo remolque; licencia propia '
          'solo si los números y el estado lo permiten'),
    (117, '§10 7/7: cierre: los siguientes pasos con el Excel, la calculadora de precios (con su shopping list) y el '
          'checklist del kit'),
])
DOCX_NOTAS = OrderedDict([('mbar', OrderedDict(sorted(list(_NOTAS_SECCION.items()) + list(_N9.items()))))])

# ==========================================================================
# Pistas por celda (extraer_textos.py → textos_es.json → tandas)
# ==========================================================================
_CASO = ('D85: caso US = 160 eventos/año × 95 invitados × $14 por invitado (sin sales tax ni alcohol: bar package + '
         'add-ons, sin la gratuity voluntaria) = $212,800 (research §8; la calibración D15 puede subir B4); drivers: B4 '
         '= eventos/año, B5 = precio por invitado, B6 = invitados por evento. Las notas describen el MÉTODO: sin cifras '
         'del caso (cambian al recalibrar)')
_GLOSA = 'PRIMERA mención de «dry hire» de este libro: con la glosa «' + GLOSA_DRY_HIRE + '»'
CELDA_PISTAS = OrderedDict([
    (('MBP', _S, 'C4'), _CASO + '; los años 2-3 crecen en EVENTOS (B7/B8); compara con la capacidad de tus 2 equipos '
                                '(fila 51)'),
    (('MBP', _S, 'C5'), _CASO + '; precio por invitado SIN sales tax y SIN alcohol (en dry hire lo compra el '
                                'anfitrión) con bartenders, barra, mixers, garnish, hielo y vasos dentro y SIN la '
                                'gratuity voluntaria; los operadores cotizan por paquete o por hora: la calculadora del '
                                'kit lo convierte a precio por invitado. ' + _GLOSA),
    (('MBP', _S, 'C6'), _CASO + '; invitados medios por evento (Check Cherry: evento típico ~80 invitados); la mezcla del '
                                'ejemplo va de fiestas privadas de 60 a bodas de 120'),
    (('MBP', _S, 'C7'), 'D85: crecimiento de EVENTOS 10 % en el año 2 (limitado por 2 equipos y por los sábados)'),
    (('MBP', _S, 'C8'), 'D85: crecimiento de EVENTOS 8 % en el año 3, por la misma razón'),
    (('MBP', _S, 'C11'), 'D85: cuota de BAR PACKAGES (bartending, barra, mixers, garnish, hielo, vasos) 85 %; el resto '
                         '(fila 12) son add-ons: travel fees, horas extra, cristalería, specialty bars. Es una ENTRADA'),
    (('MBP', _S, 'C12'), 'D85: calculado como el resto: bar packages + add-ons = 100 %'),
    (('MBP', _S, 'C13'), 'D85: coste de los paquetes 19 % = mixers, garnish, hielo y bebidas sin alcohol (Kit estimate ≈ '
                         '$2.25 por invitado); nunca alcohol en dry hire'),
    (('MBP', _S, 'C14'), 'D85: coste de los add-ons 20 % (Kit estimate: specialty bars, champagne service, cristalería '
                         'extra alquilada)'),
    (('MBP', _S, 'C15'), 'D85: desechables 4 %: vasos, pajitas, servilletas, posavasos y carta impresa (Kit estimate)'),
    (('MBP', _S, 'C16'), 'D87: cuota de reservas por gig marketplaces (GigSalad, The Bash, Thumbtack): 20 % en el ejemplo'),
    (('MBP', _S, 'C17'), 'D87: comisión 5 %: GigSalad cobra 5 % (gratis) o 2.5 % (de pago) sobre la reserva confirmada y '
                         'nada por lead (help.gigsalad.com); Thumbtack cobra por lead'),
    (('MBP', _S, 'C18'), 'D85: tarjeta 3 %: los particulares pagan con tarjeta el depósito y el saldo'),
    (('MBP', _S, 'C24'), 'D87: storage unit o garaje para el equipo + aparcamiento del remolque, por mes; si tu condado '
                         'exigiera una comisaria para el garnish o el hielo, súmala aquí (Kit estimate: +$300-800)'),
    (('MBP', _S, 'C25'), 'D87: meses de depósito del storage unit'),
    (('MBP', _S, 'C26'), 'D85: luz y agua del storage unit; el combustible del vehículo y del generador va en la fila 27 '
                         'del P&L'),
    (('MBP', _S, 'C27'), 'D85: $4,000/año = general liability + liquor liability ($600-1,000) + commercial auto con el '
                         'remolque (≈ $1,800) + workers\' comp (≈ $1,000) + equipo ($300); los venues piden COI y '
                         'additional insured (insurancecanopy.com: GL + liquor desde $550/año)'),
    (('MBP', _S, 'C28'), 'D85: varios 3 % de las ventas: imprevistos de cada evento (hielo extra, mixers de última hora, '
                         'parking en el venue); es VARIABLE. Combustible, mantenimiento y registro del vehículo y del '
                         'remolque: fila 27 del P&L'),
    (('MBP', _S, 'C30'), 'D85: fondos propios del dueño (≈ un tercio de la necesidad en el ejemplo)'),
    (('MBP', _S, 'C31'), 'D85: préstamo que calibra el libro (≈ $50,000): cabe en un SBA Microloan (tope $50,000) o un '
                         '7(a) pequeño'),
    (('MBP', _S, 'C33'), 'D85: 7 años: un remolque convertido y su equipo pierden valor antes que un local'),
    (('MBP', _S, 'C44'), 'D87: 7 años: el bar trailer, su conversión, el generador y el storage fit-out (lo que se '
                         'amortiza con el remolque)'),
    (('MBP', _S, 'C45'), 'D87: 5 años: barra portátil, kit de barra, cristalería, coolers, software y tablet'),
    (('MBP', _S, 'C51'), 'D85: DATO INFORMATIVO (no entra en ningún cálculo): el techo de eventos al año que tus barras y '
                         'tus equipos pueden atender (2 montajes × ~130 días reservables; los sábados son el cuello de '
                         'botella); compáralo con la fila 4 y con el optimista'),
    (('MBP', _S, 'C52'), 'D85: rampa 45 % → 9 meses: el primer año de un bar móvil es lento (Check Cherry: la mediana '
                         'hace 3 eventos el primer año) y las bodas se reservan con 62 días de mediana'),
    (('MBP', _S, 'C54'), 'D85: 2 meses de storage antes de abrir (construcción del remolque + preventa en bridal shows)'),
    (('MBP', _S, 'C55'), 'D87: imprevistos 10 % sobre remolque, conversión, generador, storage fit-out e inspección'),
    (('MBP', _S, 'C58'), 'D85: cobro medio 1 día: depósito del 30 % al reservar y saldo antes del evento; el libro no '
                         'modela anticipos (nota de la Tesorería)'),
    (('MBP', _S, 'C62'), 'D84/D85: alcohol 0 %: en dry hire el anfitrión compra el alcohol y es suyo; vender alcohol '
                         'exige licencia (docx §9)'),
    (('MBP', _S, 'C63'), 'D85: solo si vendieras alcohol con licencia (0 % en este plan)'),
    # Startup Costs, notas de la columna D (D87; research §4, §8)
    (('MBP', _I, 'D7'), 'D87: bar trailer usado (6 x 12 ft, cargo / concession o horse trailer). El vehículo de arrastre es el '
                        'TUYO ($0 en el plan): si no lo tienes, una pickup usada cuesta $10,000-$30,000 (Check Cherry). '
                        'Nunca «truck»: di «tow vehicle» o «pickup»'),
    (('MBP', _I, 'D8'), 'D87: conversión: barra, armarios, lavamanos y depósitos de agua, LED y eléctrico (research: '
                        '$5,000-$15,000 una conversión básica)'),
    (('MBP', _I, 'D9'), 'D87: wrap, rotulación y fachada de la barra del remolque'),
    (('MBP', _I, 'D10'), 'D87: barra portátil para el 2.º equipo y los salones donde no entra el remolque (Check Cherry: '
                         'desde ~$1,000)'),
    (('MBP', _I, 'D11'), 'D87: generador inverter silencioso y cableado (research: $800-$3,000)'),
    (('MBP', _I, 'D12'), 'D87: acondicionar el storage unit: estanterías, racks de cristalería, zona de lavado'),
    (('MBP', _I, 'D13'), 'D87: LLC + contratos tipo revisados por un abogado (cláusulas de dry hire)'),
    (('MBP', _I, 'D14'), 'D87: business license, sales tax permit y certificaciones de servidores (TABC / RBS / TIPS) del '
                         'año 1; varía mucho por estado y ciudad'),
    (('MBP', _I, 'D15'), 'D87: health permit / inspección de la unidad SOLO si tu condado lo exige (hielo, garnish, '
                         'lavamanos); si no, pon 0'),
    (('MBP', _I, 'D16'), 'D87: software de reservas y CRM (propuestas, contratos, depósitos) + lector de tarjetas + tablet'),
    (('MBP', _I, 'D17'), 'D87: kit de barra para 4 estaciones (shakers, jiggers, speed rails, strainers, ice scoops): se '
                         'amortiza'),
    (('MBP', _I, 'D18'), 'D87: inventario inicial: mixers, siropes, garnish, vasos y servilletas para los primeros eventos; '
                         'nunca alcohol en dry hire'),
    (('MBP', _I, 'D19'), 'D87: web, fotos del remolque montado, altas en The Knot / WeddingWire / Zola / GigSalad, Google '
                         'Business Profile y el primer bridal show'),
    (('MBP', _I, 'D20'), 'D87: cristalería (300 piezas + racks), coolers, ice bins y dispensadores'),
    (('MBP', _I, 'D27'), 'D87: lo que compras: remolque, conversión, equipo, lanzamiento y constitución; el colchón de caja '
                         'no es inversión'),
    # 3-Year P&L, notas (D87, D88)
    (('MBP', _P, 'F10'), 'D85: ventas de bar packages: bartending, barra, mixers, garnish, hielo y vasos por invitado '
                         '(bodas, empresas, fiestas privadas). Sin alcohol: lo compra el anfitrión'),
    (('MBP', _P, 'F11'), 'D85: ventas de add-ons: travel fees, horas extra, cristalería, champagne service, specialty bars'),
    (('MBP', _P, 'F16'), 'D87: comisiones de gig marketplaces (GigSalad, The Bash, Thumbtack) sobre las reservas de ese '
                         'canal'),
    (('MBP', _P, 'F22'), 'D87: el importe mensual se teclea en "0. Assumptions"; aquí × 12: storage unit + aparcamiento '
                         'del remolque'),
    (('MBP', _P, 'F24'), 'D85: luz y agua del storage unit'),
    (('MBP', _P, 'F32'), 'D85: teléfono e internet (móvil del negocio y datos para el lector de tarjetas en los venues)'),
    (('MBP', _P, 'F33'), 'D85: reparación de equipo y rotura de cristalería (en eventos se rompe cristal: repón cada '
                         'temporada)'),
    (('MBP', _P, 'F34'), 'D85: certificaciones de servidores del equipo (TIPS / TABC / RBS) y su renovación'),
    (('MBP', _P, 'F35'), 'D85: degustaciones y consultas de carta para parejas y planners (mixers, garnish, tiempo); '
                         'muchos operadores las descuentan si reservan'),
    (('MBP', _P, 'F51'), 'D88: suelo del margen bruto del motor 65 % (kit benchmark, editable): el margen bruto del libro '
                         'resta también tarjeta, marketplace y varios'),
    (('MBP', _P, 'F53'), 'D88: techo del coste de mercancía (paquetes + add-ons) 26 % (kit benchmark, editable); los '
                         'desechables tienen su línea; nunca alcohol en dry hire'),
    (('MBP', _P, 'F54'), 'D88: techo de personal 40 % (kit benchmark, editable), con el sueldo del dueño dentro'),
    (('MBP', _P, 'F55'), 'D88: techo de storage y parking 6 % (kit benchmark, editable): no hay local'),
    (('MBP', _P, 'F56'), 'D88: suelo del resultado neto 5 % (kit benchmark, editable)'),
    # Staffing, notas (D87)
    (('MBP', _R, 'J5'), 'D87: Owner & Lead Bartender: vende, hace las degustaciones, diseña las cartas y lleva la barra del '
                        'equipo 1 en cada evento'),
    (('MBP', _R, 'J6'), 'D87: second-crew lead bartender (part-time W-2): lleva el 2.º equipo los sábados de temporada alta'),
    (('MBP', _R, 'J7'), 'D87: event bartenders por evento, por horas y en W-2; su FTE es una fracción; las propinas '
                        'voluntarias son suyas (FLSA)'),
    (('MBP', _R, 'J8'), 'D87: barbacks / setup crew por horas y en W-2: carga, hielo, montaje y desmontaje en eventos grandes'),
    (('MBP', _R, 'J18'), 'D85: horas por persona y evento: compra y garnish, carga, viaje, montaje, 4-5 h de servicio y '
                         'desmontaje'),
    (('MBP', _R, 'J19'), 'D85: personas por evento: 1 bartender por 50 invitados con barra completa + un barback en las '
                         'bodas grandes'),
    (('MBP', _ES, 'E23'), 'D85: la MISMA plantilla en los tres escenarios; en el pesimista el coste real de event '
                          'bartenders y barbacks baja con los eventos (pagas horas por evento), así que el resultado '
                          'real sería algo mejor'),
    (('MBP', _N, 'A5'), 'D85: «0. Assumptions» es la hoja de mando: eventos al año, precio por invitado sin sales tax ni '
                        'alcohol, invitados por evento'),
    (('MBP', _N, 'A12'), 'SPEC §4.1 línea 8 (I1): el Word del kit usa las MISMAS cifras de ejemplo que este libro; si '
                         'cambias el libro, actualiza las del Word. La calculadora de precios es otro fichero y no lee '
                         'este libro'),
])
_D18 = ('D18 (bar móvil): la propuesta es la del Catering EN publicado, que ya describe el MÉTODO del libro para un '
        'negocio de eventos; reescribe SOLO lo que hable de comida, cocina, comisaria, furgoneta, catering, buffet, '
        'servers o estaciones → bar móvil en dry hire, remolque, storage unit, bartenders y barbacks, mixers, garnish y '
        'hielo. Sin cifras del caso')
for _f in range(35, 52):
    for _col in 'ABCD':
        CELDA_PISTAS[('MBP', _N, '%s%d' % (_col, _f))] = _D18
PISTA_D19_GENERICA = ('Celda a celda: escribe SOLO el texto de ESTA celda (una tabla o una tarea): mira su pista '
                      'propia')
_D19_BASE = ('D19/D88: tabla «US MOBILE BAR BENCHMARKS (sourced) AND KIT ESTIMATES» (Benchmark | Value | Source | '
             'Note). Value en formato US; Source = el DOMINIO de la fuente LEÍDA de research §4-§5, o «Kit estimate» '
             'si allí figura como «(resumen)». Esta fila: ')
_D19 = OrderedDict([
    (55, 'precio por evento (1,334 reservas desde ene-2024, sin alcohol ni propinas): mediana $750, 50 % central '
         '$450-$1,275, media $1,173 — checkcherry.com'),
    (56, 'precio por número de invitados: hasta 50 $575 · 51-100 $700 · 101-150 $1,063 · 151+ $1,438; evento típico '
         '~80 invitados — checkcherry.com'),
    (57, 'precio por duración: hasta 3 h $575 · 4 h $675 · 5 h $898 · 6+ h $1,275 — checkcherry.com'),
    (58, 'servicio solo de bartender (dry hire puro): $375 por ~4 h ≈ $75-$120 por hora y bartender — checkcherry.com'),
    (59, 'depósito y desplazamiento: depósito del 30 % típico; 26 % de las reservas cobran travel fee (mediana 36 '
         'millas, gratis hasta ~25) — checkcherry.com'),
    (60, 'estacionalidad y calendario: octubre ~13 %, mayo 12.4 %, enero 3.8 %; reserva con 62 días de mediana, 85 % '
         'de viernes a domingo — checkcherry.com'),
    (61, 'el primer año real (negocios con 12+ meses): mediana 3 eventos / $1,650; top 10 % ~39 eventos / $35,500 — '
         'checkcherry.com'),
    (62, 'copas por invitado: 2 la primera hora + 1 por hora después — eventplanning.com'),
    (63, 'ratio de bartenders: 1 por 50 invitados con barra completa; 1 por 75 con cerveza y vino — Kit estimate (la '
         'fuente no abrió)'),
    (64, 'sueldo de bartender (BLS OES 35-3011, mayo 2025): media $19.61/h, mediana $16.51/h (incluye propinas) — '
         'bls.gov'),
    (65, 'comisión de marketplace: GigSalad 5 % (plan gratis) / 2.5 % (de pago) sobre la reserva confirmada, nada por '
         'lead — gigsalad.com'),
    (66, 'coste de arranque: barra portátil desde ~$1,000, herramientas $500-$1,500, arranque «lean» $2,000-$7,000; un '
         'remolque convertido suele costar decenas de miles — checkcherry.com'),
    (67, 'seguros: general liability + liquor liability desde $550 al año; por evento desde $275 — insurancecanopy.com'),
    (68, 'hielo y mixers: 1.5 lb (0.68 kg) de hielo por invitado; mixers + garnish + hielo ≈ $2.25 por invitado — Kit '
         'estimate'),
])
for _f, _p in _D19.items():
    for _col in 'ABCD':
        CELDA_PISTAS[('MBP', _N, '%s%d' % (_col, _f))] = _D19_BASE + _p

# Checklist (D91): una pista por FILA de tarea (columnas B tarea · C responsable · D plazo · E nota práctica). Las
# ranuras del catering que sobreviven (F1-inventario §5) llevan «[sobrevive]»: su propuesta EN vale con ajustes
_CK = ('D91: escribe una TAREA de un mobile bar en DRY HIRE (B tarea · C responsable · D plazo · E nota práctica, una '
       'celda cada vez) con el checklist ES de coctelería (fuente_es_mbar.json) + research §6 y el glosario §9; ' +
       REGLA_UNIDADES + '. Esta fila: ')
TAREAS_MBAR = OrderedDict([
    ('F1 - Constitución', [
        'estructura: single-member LLC frente a sole proprietor o S corp, con tu contador (ES: autónomo / SL) '
        '[sobrevive]',
        'EIN gratis en el IRS + alta estatal de nóminas y desempleo (vas a tener bartenders W-2) [sobrevive]',
        'registrar la LLC en el Secretary of State + registered agent + operating agreement [sobrevive]',
        'cuenta bancaria del negocio y finanzas separadas [sobrevive]',
        'sales tax permit / seller\'s permit del estado: en algunos estados el servicio de barra tributa (California: '
        'cdtfa.ca.gov) [sobrevive con ajuste]',
        'business license de la ciudad o el condado (+ DBA si usas nombre comercial) [sobrevive]',
        'contador / bookkeeper y estimated taxes trimestrales [sobrevive]',
        'software de reservas y CRM para bares móviles: propuestas, contratos con firma electrónica, depósitos y saldos '
        '(ES: CRM) [sobrevive con ajuste]',
        'service agreement / event contract con abogado y cláusulas de DRY HIRE: el anfitrión compra y es dueño del '
        'alcohol, lo que sobra es suyo, sin cash bar ni tickets de copa ni entrada con bebida, gratuity pactada por '
        'escrito, depósito del 30 %, cancelación por tramos, variación de invitados, toma eléctrica, uso de fotos '
        '[sobrevive con ajuste]',
        'elegir el modelo legal: DRY HIRE por defecto (' + GLOSA_DRY_HIRE + ', glosa en esta primera mención del '
        'checklist) o full-service con licencia (socio licenciatario, licencia propia ligada a un local o permiso por '
        'evento): decide la fase 2',
        'marca: búsqueda y registro en la USPTO (ES: OEPM) y dominio web',
    ]),
    ('F2 - Vehículo', [
        'reglas de alcohol de TU estado para un servicio SOLO de bartending: MO (Circular 24-01: sin licencia estatal '
        'si solo das servicio; cuidado con entradas, tip jars y recargos), MT (no pre-stock, el anfitrión compra '
        'aparte, solo eventos privados), TX, CA, FL, NY (consultar): «varies by state», pregunta a tu ABC / TABC y '
        'guarda la respuesta',
        'alquilar el storage unit o garaje para el equipo y el aparcamiento del remolque (ES: almacén de unos 160-270 '
        'sq ft)',
        'health permit SOLO si el condado lo exige: pregunta al health department si el garnish cortado y el hielo '
        'piden permiso o comisaria; hielo comercial embolsado; lavamanos en el remolque',
        'eventos públicos: en dry hire el permiso lo pide el organizador; con licencia, temporary / special event '
        'permit',
        'requisitos del venue: COI, additional insured, horarios de carga, toma eléctrica, normas de cristal y hielo, '
        'preferred vendor lists',
        'comprar el bar trailer usado (6 x 12 ft, cargo / concession o horse trailer) con inspección; el tow vehicle es el '
        'tuyo (comprueba su capacidad de arrastre)',
        'remolque: título y registro en el DMV + commercial auto (o uso comercial del vehículo propio) que cubra el '
        'remolque [sobrevive con ajuste]',
        'conversión del remolque: barra, armarios, lavamanos y depósitos de agua, LED, eléctrico y wrap [sobrevive con '
        'ajuste]',
        'general liability; COI y «additional insured» que piden los venues [sobrevive]',
        'liquor liability aparte (la general liability suele excluir el alcohol): en la práctica, obligatoria para '
        'entrar en los venues [sobrevive]',
        'workers\' comp (obligatorio con empleados en casi todos los estados) [sobrevive]',
        'inland marine / equipment floater para la barra portátil, la cristalería y el equipo en tránsito (ES: '
        'multirriesgo y transporte)',
        'solo si vas a full-service: el permiso de caterer de tu estado (TX Caterer\'s Permit ligado al Mixed Beverage '
        'Permit; CA Type 58 solo licenciatarios on-sale; FL 13CT; NY Caterer\'s Alcohol Permit por evento) o un socio '
        'con licencia; si no, márcala como «not applicable»',
    ]),
    ('F3 - Equipamiento', [
        'barra portátil (portable bar) para el 2.º equipo y los salones donde no entra el remolque',
        'proveedor de hielo comercial embolsado + ice bins y coolers de 60 lb (27 kg) o en quarts, nunca en litros; '
        'regla de 1.5 lb (0.68 kg) por invitado (Kit estimate) (ES: máquina de hielo → hielo comprado)',
        'coolers y neveras para mixers y para las bebidas del anfitrión (capacidad en quarts, ES: nevera de 200 L ≈ 210 '
        'quarts)',
        'cristalería (300 piezas + racks) o vasos desechables de calidad según el venue',
        'kit de barra para 4 estaciones: shakers, jiggers, speed rails, strainers, cucharas, abrebotellas, '
        'dispensadores',
        'props y carta impresa de los specialty bars (mimosa bar, espresso martini bar…): el diferencial (ES: '
        'decoración temática)',
        'iluminación LED y generador inverter: prueba de carga con todo encendido',
        'acuerdo con una empresa de party rentals (cristalería extra, mesas, mantelería) con tarifa pactada [sobrevive]',
        'proveedores de mixers, siropes y garnish (restaurant supply o club store) y cuentas abiertas',
        'desechables: vasos, pajitas, servilletas, posavasos y carteles de la carta',
        'inventario y etiquetado de TODO el equipo + checklist de carga del remolque',
        'ensayo completo de un evento (dry run) con el equipo: montaje, servicio y desmontaje cronometrados '
        '[sobrevive]',
    ]),
    ('F4 - Personal', [
        'plan de personal por evento: 1 bartender por 50 invitados con barra completa, 1 por 75 con cerveza y vino, '
        'barback en eventos grandes (Kit estimate) [sobrevive con ajuste]',
        'pool de event bartenders y barbacks en nómina W-2 (no 1099 ni «freelance»: FLSA; California AB5) [sobrevive]',
        'offer letters, I-9 y W-4; salario mínimo estatal [sobrevive]',
        'new-hire reporting al estado [sobrevive]',
        'proveedor de nóminas y workers\' comp en marcha [sobrevive]',
        'edad mínima para servir alcohol en TU estado y food handler card SOLO si el estado o el condado la exige para '
        'manipular hielo y garnish',
        'alcohol server certification de todos los bartenders (TABC en TX, RBS en CA, TIPS / ServSafe Alcohol): la '
        'piden venues y aseguradoras [sobrevive]',
        'OSHA basics: cortes de cristal, cargas, conducción con remolque [sobrevive con ajuste]',
        'servicio responsable: comprobar el ID, negarse a servir a menores y a invitados ebrios, last call, protocolo '
        'de incidentes (ES: formación)',
        'política de propinas y service charge: las propinas son del personal (FLSA); el service charge es salario '
        '(IRS Rev. Rul. 2012-18); tip jar solo donde el estado no lo trate como venta (MO) [sobrevive con ajuste]',
    ]),
    ('F5 - Marketing', [
        'marca, logo, carta de signature cocktails y fotos profesionales del remolque montado [sobrevive con ajuste]',
        'web con paquetes, precios «desde» por invitado y formulario de presupuesto [sobrevive]',
        'Google Business Profile y reseñas [sobrevive]',
        'perfiles en The Knot, WeddingWire y Zola (ES: Bodas.net / Zankyou) [sobrevive con ajuste]',
        'gig marketplaces: GigSalad (5 % / 2.5 % por reserva confirmada), The Bash, Thumbtack (pago por lead)',
        'prospección B2B: event planners, office managers y HR para holiday parties y eventos de empresa [sobrevive]',
        'acuerdos con venues, wedding planners, fotógrafos y DJs (preferred vendor lists, cross-promo) [sobrevive]',
        'política de degustaciones y consultas de carta para parejas y planners [sobrevive]',
        'Instagram, Pinterest y reels con eventos reales [sobrevive]',
        'plantilla de presupuesto con la calculadora del kit y seguimiento en el CRM [sobrevive]',
        'programa de referidos y reseñas después de cada evento [sobrevive]',
        'bridal show local + showcase / tasting para planners y venues; los 3 primeros eventos piloto para el '
        'portfolio [sobrevive con ajuste]',
    ]),
    ('F6 - 90 Días', [
        'briefing con el cliente D-21: invitados, horas, paquete, specialty bar, venue, restricciones [sobrevive]',
        'visita o llamada técnica al venue D-14: acceso del remolque, toma eléctrica, agua, normas del venue '
        '[sobrevive con ajuste]',
        'shopping list al anfitrión en D-14 (la saca la calculadora del kit: botellas por categoría, cerveza, vino, '
        'hielo) y compra de mixers, garnish y hielo en D-1',
        'checklist de carga y transporte del remolque (enganche, luces, sujeción de la cristalería) [sobrevive con '
        'ajuste]',
        'montaje 60-120 min antes, servicio y last call [sobrevive con ajuste]',
        'desmontaje y recuento de cristalería; el alcohol que sobra se queda con el anfitrión; devolución de '
        'alquileres [sobrevive con ajuste]',
        'factura del saldo antes del evento y control de depósitos; gratuity pactada en la factura [sobrevive con '
        'ajuste]',
        'pedir reseña y fotos a las 48 h; seguimiento en el CRM [sobrevive]',
        'revisión mensual del coste por invitado, las horas de personal y los desechables frente a la calculadora '
        '[sobrevive con ajuste]',
        'revisión a los 90 días: precios por invitado, mínimos, paquetes y specialty bars; formación continua y ferias '
        'del sector (Bar Convent Brooklyn, Tales of the Cocktail; sin cifras) [sobrevive con ajuste]',
    ]),
])
for _h, _ts in TAREAS_MBAR.items():
    for _k, _t in enumerate(_ts):
        for _col in 'BCDE':
            CELDA_PISTAS[('MBC', _h, '%s%d' % (_col, 5 + _k))] = _CK + 'fase %s, tarea %d/%d: %s' % (
                _h[1], _k + 1, len(_ts), _t)

# Pistas por TEXTO propias del bar móvil (se suman a las de extraer_textos.PISTAS)
PISTAS_EXTRA = [
    (r'^Días fuera de rango$|^Los días van de 1 a 365', 'D86: esta validación cubre a la vez B6 (INVITADOS por evento), '
                                                         'B58/B59 (días de cobro y de pago) y los invitados de '
                                                         'Escenarios: un texto que valga para todos'),
    (r'[Cc]lientes?|[Tt]icket|[Dd]ías de apertura|al día|por día',
     'D86: motor de eventos: «events per year» (B4), «price per guest» (B5), «guests per event» (B6); nunca «customers», '
     '«per day» ni «operating days» (gate)'),
    (r'[Vv]ehícul|[Ff]ood ?[Tt]ruck|[Cc]amión|[Rr]emolque', 'D84/D87: el bar trailer (remolque-barra convertido) que '
                                                            'arrastra el vehículo del dueño («tow vehicle»); nunca '
                                                            '«truck» (gate)'),
    (r'[Vv]entanilla|[Ff]estival|[Mm]ercados|[Aa]mbulante|[Cc]alle', 'D84: bar móvil en el evento del cliente; sin '
                                                                     'ventanilla, festivales, mercados ni venta '
                                                                     'ambulante (gate)'),
    (r'[Aa]parcamiento|base del vehículo|comisar', 'Glosario: «storage unit & trailer parking»'),
    (r'[Gg]enerador|gas\b|propano', 'D87: «inverter generator and power»'),
    (r'[Dd]elivery|[Gg]lovo|[Uu]ber', 'D87: gig marketplaces (GigSalad, The Bash, Thumbtack), no apps de delivery'),
    (r'[Cc]omida|[Cc]ocina|[Mm]enú|COMIDA', 'D86: no hay comida: bar packages (bartending, mixers, garnish, hielo) y '
                                            'add-ons; «drink menu» / «signature cocktails»; nunca food, kitchen ni menu '
                                            'a secas (gate)'),
    (r'm²|m2\b|\bkg\b|\bkm\b|[Ll]itros?\b|\b\d+ ?L\b|\bml\b|°C|ºC', REGLA_UNIDADES),
    (r'[Ee]ventos?|[Bb]odas?', 'Glosario §9: mobile bar, dry hire, bar packages, signature cocktails, weddings, '
                               'corporate events / holiday parties, private parties'),
]

# Glosario de research §9 (OBLIGATORIO: regla de jerga §0). Se suma al de FT/CAF y al del financial-kit
GLOSARIO_MBAR = OrderedDict([
    ('empresa de coctelería para eventos', 'mobile bar company / business'),
    ('servicio de barra (sinónimo)', 'mobile bartending service · bar service'),
    ('el cliente compra el alcohol', 'dry hire ' + GLOSA_DRY_HIRE + ' — glosa en la 1.ª mención de cada entregable'),
    ('con alcohol incluido y licencia', 'full-service / licensed bar (solo como opción)'),
    ('lista de la compra para el cliente', 'shopping list'),
    ('barra móvil (mueble)', 'portable bar (≠ «mobile bar», que es el negocio)'),
    ('remolque-barra', 'bar trailer · converted trailer · horse trailer bar'),
    ('vehículo que lo arrastra', 'tow vehicle (nunca «truck»: di «pickup»)'),
    ('raíl de botellas · cubeta de hielo · lavamanos · depósitos', 'speed rail · ice bin · hand sink · fresh / gray water '
                                                                   'tank'),
    ('montaje y desmontaje', 'setup & breakdown'),
    ('hora extra', 'extra hour of service'),
    ('precio por invitado', 'per person / per guest pricing'),
    ('paquetes cerrados', 'bar packages'),
    ('solo bartender', 'bartender-only service'),
    ('barra libre pagada por el anfitrión', 'open bar / hosted bar'),
    ('barra de pago', 'cash bar (prohibida en dry hire)'),
    ('por consumo', 'consumption bar (solo full-service)'),
    ('solo cerveza y vino (+1 cóctel)', 'limited bar · beer & wine bar'),
    ('cóctel de autor / carta de la casa', 'signature cocktails · custom cocktail menu (nunca «author cocktails»)'),
    ('carta impresa en la barra', 'personalized menu / menu sign'),
    ('bebidas sin alcohol', 'mocktails · N/A drinks · zero-proof'),
    ('brindis con espumoso', 'champagne service / champagne toast'),
    ('mezcladores, garnish, hielo, vasos', 'mixers · garnishes · ice & coolers · plastic cups, napkins & straws'),
    ('hielo por invitado', 'ice per guest (1.5 lbs per guest, 0.68 kg)'),
    ('medidas (John, 13-oct)', 'US customary first, metric in parentheses: oz / fl oz (ml), lb (kg), quarts / gallons, '
                               '°F (°C), miles, sq ft (m²); 750 ml bottle = a fifth, 1.75 L = a handle'),
    ('desplazamiento', 'travel fee'),
    ('mínimo de contratación', 'minimum · bar minimum'),
    ('señal / anticipo / fianza', 'deposit'),
    ('propina', 'gratuity · tip jar (riesgo de «venta» en MO)'),
    ('recargo de servicio', 'service charge (≠ gratuity: es salario)'),
    ('jefe de barra', 'lead bartender · Owner & Lead Bartender'),
    ('ayudante de barra', 'barback'),
    ('certificado de servicio responsable', 'TABC-certified (TX) · RBS (CA) · TIPS / ServSafe Alcohol (nunca «alcohol '
                                            'handler card»)'),
    ('seguro de RC por alcohol', 'liquor liability insurance · general liability'),
    ('certificado del seguro · asegurado adicional', 'COI · additional insured'),
    ('requisitos de la sala', 'venue requirements'),
    ('seguro del anfitrión', 'host liquor liability (lo contrata el cliente)'),
    ('coste por copa / escandallo', 'cost per guest (dry hire) · pour cost (solo full-service)'),
    ('última ronda', 'last call'),
    ('experiencias temáticas', 'specialty bars / themed bars (mimosa bar, espresso martini bar…)'),
    ('coctelería de autor', 'signature / craft cocktails'),
    ('autónomo', 'sole proprietor o single-member LLC (el caso: LLC)'),
    ('bartender freelance', 'W-2 event bartender (nunca «freelance»)'),
    ('licencia de actividad', 'business license + sales tax permit'),
    ('autorización puntual', 'temporary / special event permit (solo full-service)'),
    ('IVA', 'sales tax'),
    ('wedding planner', 'wedding planner / coordinator'),
    ('contrato', 'service agreement / event contract'),
    ('hostelero / sala', 'venue'),
    ('evento de empresa', 'corporate event / holiday party'),
    ('temporada alta', 'peak wedding season (May-June, Sept-Oct)'),
])


# ==========================================================================
# Caso de ejemplo US (D85; research §8 tal cual): celdas VERDES del FT. (corto, hoja ES, celda) → (valor, rótulo ES)
# ==========================================================================
def valores_mbar(M):
    v = OrderedDict()
    sup = [
        ('B4', 160, 'Clientes/día'), ('B5', 14, 'Ticket medio'), ('B6', 95, 'Días de apertura'),
        ('B7', 0.10, 'Crecimiento de volumen del año 2'), ('B8', 0.08, 'Crecimiento de volumen del año 3'),
        ('B11', 0.85, 'Ventas de COMIDA'), ('B13', 0.19, 'Coste de mercancía sobre las ventas de COMIDA'),
        ('B14', 0.20, 'Coste de mercancía sobre las ventas de BEBIDA'), ('B15', 0.04, 'Consumibles'),
        ('B16', 0.20, 'Ventas por delivery'), ('B17', 0.05, 'Comisión de la plataforma'),
        ('B18', 0.03, 'Comisión de los medios de pago'), ('B20', 0.10, 'Seguridad Social'),
        ('B21', 12, 'Número de pagas'), ('B22', 15080, 'SMI anual'), ('B24', 600, 'Alquiler mensual'),
        ('B25', 1, 'Fianza'), ('B26', 100, 'Suministros'), ('B27', 4000, 'Seguros'), ('B28', 0.03, 'Varios'),
        ('B30', 26000, 'Recursos propios'), ('B31', M.CALIBRAR, 'Préstamo bancario'), ('B32', 0.10, 'Tipo de interés'),
        ('B33', 7, 'Plazo del préstamo'), ('B34', 0, 'Carencia'), ('B35', 3, 'Fondo de maniobra'),
        ('B37', 0.25, 'Impuesto de Sociedades, nueva'), ('B38', 0.25, 'Impuesto de Sociedades, tipo'),
        ('B39', 0.08, 'IVA repercutido de restauración'), ('B40', 0.08, 'IVA repercutido/soportado'),
        ('B41', 0, 'IVA soportado en compras'), ('B42', 0, 'Bases negativas'),
        ('B44', 7, 'Vida útil de obra'), ('B45', 5, 'Vida útil de maquinaria'), ('B48', 0, 'Subida anual'),
        ('B51', 260, 'Plazas de pie'), ('B52', 0.45, 'Actividad del mes 1'), ('B53', 9, 'Meses hasta alcanzar'),
        ('B54', 2, 'Meses de alquiler del aparcamiento'), ('B55', 0.10, 'Imprevistos sobre las partidas'),
        ('B58', 1, 'Días medios de cobro'), ('B59', 7, 'Días medios de pago'),
        ('B62', 0, 'Bebida ALCOHÓLICA'), ('B63', 0.08, 'IVA de la bebida ALCOHÓLICA'),
        ('B65', 1.15, 'DSCR mínimo'), ('B66', 1.25, 'DSCR objetivo'), ('B67', 0.15, 'Holgura mínima'),
        ('B68', None, 'Suelo salarial anual'),
    ]
    for c, val, rot in sup:
        v[('MBP', _S, c)] = (val, rot)
    # Inversión (D87; research §8): las 14 partidas tecleadas, filas 7-20 (rótulos ES del FT) = $43,300
    for k, (val, rot) in enumerate([
            (9000, 'Vehículo'), (12000, 'Adaptación'), (2500, 'Equipamiento cocina'), (2000, 'Generador'),
            (1800, 'Instalación gas'), (1000, 'Depósito de agua'), (1500, 'Constitución'), (1000, 'Licencias'),
            (500, 'Proyecto técnico'), (800, 'TPV'), (1200, 'Menaje'), (1500, 'Stock'), (5000, 'Marketing'),
            (3500, 'Toldo')]):
        v[('MBP', _I, 'B%d' % (7 + k))] = (val, rot)
    # P&L: fijos B26-B35 (research §8: $22,100) y umbrales D88 [kit benchmark]
    for k, (val, rot) in enumerate([
            (500, 'Permisos'), (4000, 'Mantenimiento'), (9000, 'Marketing'), (2400, 'Gestoría'), (1500, 'Software'),
            (1200, 'Limpieza'), (900, 'Gestión de residuos'), (1200, 'Desinsectación'), (400, 'Prevención'),
            (1000, 'Derechos de autor')]):
        v[('MBP', _P, 'B%d' % (26 + k))] = (val, rot)
    for c, val, rot in [('E51', 0.65, 'Margen bruto'), ('E53', 0.26, 'Coste de mercancía /'),
                        ('E54', 0.40, 'Coste de personal'), ('E55', 0.06, 'Aparcamiento'), ('E56', 0.05, 'Resultado neto')]:
        v[('MBP', _P, c)] = (val, rot)
    # Staffing (D87; research §8): personas (B), FTE por persona (C), bruto mes TOTAL de la fila (D) = $5,937/mes
    for f, (b, c, d) in zip(range(5, 9), [(1, 1.0, 3250), (1, 0.25, 867), (5, 0.10, 1560), (2, 0.05, 260)]):
        for col, val in zip('BCD', (b, c, d)):
            v[('MBP', _R, '%s%d' % (col, f))] = (val, None)
    v.update([
        (('MBP', _R, 'B11'), (3000, 'Coste anual')), (('MBP', _R, 'B12'), (3000, 'Coste anual')),
        (('MBP', _R, 'B16'), (40, 'Jornada completa')), (('MBP', _R, 'B17'), (50, 'Semanas')),
        (('MBP', _R, 'B18'), (8, 'Horas de servicio')), (('MBP', _R, 'B19'), (2.2, 'Personas necesarias')),
    ])
    # Escenarios (research §8): −25 % / +25 % de eventos, −10 % / +10 % de precio e invitados
    v.update([
        (('MBP', _ES, 'B5'), (120, 'Clientes/día')), (('MBP', _ES, 'D5'), (200, 'Clientes/día')),
        (('MBP', _ES, 'B6'), (12.6, 'Ticket')), (('MBP', _ES, 'D6'), (15.4, 'Ticket')),
        (('MBP', _ES, 'B7'), (86, 'Días')), (('MBP', _ES, 'D7'), (105, 'Días')),
    ])
    # Estacionalidad (research §8, forma de Check Cherry): apertura en MARZO → Month 1-12 (suma 100 %)
    for col, val in zip('BCDEFGHIJKLM', (0.075, 0.105, 0.124, 0.09, 0.056, 0.065, 0.115, 0.13, 0.085, 0.075, 0.038,
                                         0.042)):
        v[('MBP', _T, '%s5' % col)] = (val, 'Estacionalidad')
    return v


# Calibración D15 (SPEC D85): holgura ≥ 15 %; si no, B4 de 10 en 10 hasta 180; si la caja mínima ≤ 0 por la rampa,
# B35 3 → 4 antes de tocar el precio. Dry-run del paso 1 con research §8 tal cual: D15 VERDE sin tocar B4 ni B35
# (holgura 20.3 %, DSCR mín 2.77, saldo mín > 0, cobertura 131 %), pero el punto fijo del préstamo daba $52,000, por
# encima del tope de $50,000 del SBA Microloan en el que D85 encaja el caso. Con B30 = 28,000 el punto fijo da $49,000.
# Cada celda, citada en F2-NOTAS §3 (G7)
CALIBRACION_D15 = OrderedDict([
    (('MBP', _S, 'B30'), (28000, 'D85: fondos propios 26,000 → 28,000: el préstamo (punto fijo) baja de $52,000 a '
                                 '$49,000, dentro del tope de $50,000 del SBA Microloan; D15 ya estaba en verde')),
])


# ==========================================================================
# FORMULAS_EN: las del FT con la fila del Break-Even y las listas de la inversión del bar móvil
# ==========================================================================
_PE_MBAR = ('=IFERROR("With the average price per guest excl. sales tax above, you need "&TEXT(ROUNDUP(B15,0),"0")&" '
            'events a year at your average of "&TEXT(B11,"0")&" guests per event to avoid losing money (accounting '
            'break-even, depreciation included), and "&TEXT(ROUNDUP(B20,0),"0")&" for cash to hold (cash break-even: '
            'depreciation out, because it is not paid, and the year\'s loan payment in"&IF(B12=0,"; no principal is '
            'repaid this year (interest-only period or no loan)","")&"). The ""Revenue needed per year"" rows show the '
            'same figures in your currency.","")')
_C9_MBAR = ('=IFERROR("Price per guest excl. sales tax plus the weighted sales tax of your sales lines ("&TEXT('
            "SUMPRODUCT('3-Year P&L'!$E$10:$E$11,'3-Year P&L'!$G$10:$G$11)*100,\"0\")&\"%), rounded. In the US the "
            'quote adds sales tax on top, and whether the bartending service and the service charge are taxable '
            'depends on the state (California taxes them); in the UK, VAT is included in the price.","")')
_F18_MBAR = ('=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$28,"0%")&" of sales: a cushion for unbudgeted event costs '
             '(extra ice, last-minute mixers, venue parking). It is a VARIABLE cost: it moves with the number of '
             'events, so it cannot sit in fixed costs (fuel, maintenance and registration of the tow vehicle and the '
             'trailer are in row 27)","")')


_F13_MBAR = ('=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$13,"0%")&" of BAR PACKAGE sales (mixers, garnishes, ice), not of '
             'total sales: add-ons have their own line","")')
_F14_MBAR = '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$14,"0%")&" of ADD-ON sales","")'


def formulas_mbar():
    sys.path.insert(0, BP)
    import formulas_en as F                                                    # noqa: E402
    out = OrderedDict()
    for h, d in F._COMUNES.items():
        for c, f in d.items():
            out[('MBP', h, c)] = f
    out[('MBP', _S, 'C9')] = _C9_MBAR
    out[('MBP', _P, 'F18')] = _F18_MBAR
    out[('MBP', _P, 'F13')] = _F13_MBAR
    out[('MBP', _P, 'F14')] = _F14_MBAR
    out[('MBP', _T, 'O11')] = out[('MBP', _T, 'O11')].replace('Food and beverage purchases, consumables',
                                                              'Mixers, garnishes, ice, disposables')
    out[('MBP', _E, 'A26')] = _PE_MBAR
    for c, f in F._inversion('D21', 'D22', 'D23', 'D25', 'D26', 'D28', 'D31', 'D32', 'D33', 24, 26, 31, 32,
                             'used bar trailer, trailer conversion, inverter generator, storage unit fit-out and the '
                             'health permit / unit inspection',
                             'LLC formation and legal, first-year permits and certifications, opening inventory, '
                             'website, photos and launch, the storage unit deposit, pre-opening storage rent and the '
                             'working capital reserve').items():
        out[('MBP', _I, c)] = (f.replace('when the lease ends', 'when the storage unit lease ends')
                               .replace(' of build-out and permits before opening', ' of trailer build, permits and '
                                        'pre-sales before opening'))
    return out


def cifras_prohibidas(valores):
    """CIFRAS_PROHIBIDAS del conjunto (D93): ES de coctelería (importe y frase) + caso del catering EN + caso del FT EN
    + vocabulario RX_BAR_NO. Fuera las cifras que coinciden con un valor del propio caso (no son prohibidas aquí)."""
    propios = {int(round(x[0])) for x in valores.values() if isinstance(x[0], (int, float))}
    out = [(_num(n), 'cifra del ES de coctelería (D93)', None) for n in CIFRAS_ES if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_ES]
    out += [(_num(n), 'cifra del caso del catering EN publicado (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(CAT, 'cifras_caso.json'), 'cat') if n not in propios]
    calibrado_b4 = CALIBRACION_D15.get(('MBP', _S, 'B4'), (None,))[0]
    out += [(rx, motivo, None) for rx, motivo in FRASES_CAT if not (calibrado_b4 == 180 and '180' in rx)]
    out += [(_num(n), 'cifra del caso FT EN publicado (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(BP, 'cifras_caso.json'), 'ft') if n not in propios]
    out += RX_BAR_NO
    return out


def completar(M):
    fijos = OrderedDict((k, v) for k, v in M.FIJOS.items() if k not in FIJOS_FUERA)
    fijos.update(FIJOS_NUEVOS)
    M.FIJOS = fijos
    M.POR_CELDA = POR_CELDA
    M.TOKENS_DOCX = tokens_mbar(M.TOKENS_DOCX)
    M.PRODUCTOS_CIERRE = PRODUCTOS_CIERRE_MBAR
    M.DOCX_FIJOS = docx_fijos(M)
    M.DOCX_NOTAS = DOCX_NOTAS
    M.DOCX_NOTAS_PLAN = DOCX_NOTAS_PLAN
    M.FORMULAS_EN = formulas_mbar()
    M.VALORES_EN = valores_mbar(M)
    M.CALIBRACION_D15 = CALIBRACION_D15
    M.CELDA_PISTAS = CELDA_PISTAS
    M.PISTAS_EXTRA = PISTAS_EXTRA
    M.PISTA_D19 = PISTA_D19_GENERICA          # la pista D19 de verdad va por celda (filas 55-68); las tareas, también
    M.CIFRAS_PROHIBIDAS = cifras_prohibidas(M.VALORES_EN)
    M.RX_BAR_NO = RX_BAR_NO
    M.GLOSA_DRY_HIRE = GLOSA_DRY_HIRE
    M.REGLA_UNIDADES = REGLA_UNIDADES
    glo = OrderedDict(M.GLOSARIO)
    for k in ('cliente/día', 'ticket medio sin IVA', 'PVP con IVA', 'aparcamiento y base del vehículo', 'venta ambulante'):
        glo.pop(k, None)                      # glosario del food truck que no vale aquí
    glo.update([('cliente/día → (motor)', 'events per year'), ('ticket medio sin IVA → (motor)',
                                                               'average price per guest (excl. sales tax and alcohol)'),
                ('días de apertura → (motor)', 'average guests per event'),
                ('aparcamiento y base del vehículo', 'storage unit & trailer parking')])
    for k, val in GLOSARIO_MBAR.items():
        glo[k] = val                          # research §9 manda (regla de jerga §0)
    M.GLOSARIO = glo
