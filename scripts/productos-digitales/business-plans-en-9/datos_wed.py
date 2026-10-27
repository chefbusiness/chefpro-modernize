#!/usr/bin/env python3
"""
datos_wed.py — Wedding Venue Business Plan Kit (EN) · los datos ES→EN que dependen del contenido: rótulos fijados
(D162-D163), POR_CELDA (D164, D167), pistas (D160, D165, D169), tokens del docx (D170), fijos y notas del docx, caso US
(D160; research §8), FORMULAS_EN (D166), cifras prohibidas y RX_WED_NO (D173) y glosario (research §9). Lo llama
`mapas_wed.instalar()` con el módulo `mapas` YA cargado con los datos de FT/CAF (FIJOS comunes del motor 2.2,
TOKENS_DOCX). Clon de `../business-plans-en-8/datos_piz.py`. Sesión Claude Code, 27-oct-2026 (F2-EN, paso 1a).

Decisiones de orquestador (27-oct, anotadas en SPEC-delta §11): (1) arrendamiento largo cuya duración CONTANDO LAS
PRÓRROGAS sea al menos la del préstamo («SBA lenders typically require…; confirm with your lender»), opción de compra o
derecho de tanteo, consentimiento del propietario a la obra y a usar el arrendamiento como garantía, TI allowance; comprar
(SBA 504) = variante del Word sin Excel · (2) FTC Cooling-Off Rule: NUNCA se afirma que aplique a un contrato de venue
(«ask your attorney whether…») · (4) lo «(resumen)» de research (The Knot, NY A20-51S, Missouri, CA Civ. Code §1671,
40 CFR 141.2, rentas, seguros, sprinklers, fosa séptica) fuera de las cifras rotundas: «typical range, get local
quotes» o «ask…» hasta que la revisión D174 lo abra.
"""
import json
import os
import re
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
PD = os.path.dirname(AQUI)
BP = os.path.join(PD, 'business-plans-en')
PIZ = os.path.join(PD, 'business-plans-en-8')
FINES = os.path.join(PD, 'plan-finca-eventos')            # ES: SPEC, research y cifras_caso_es.json

URL_WED = 'aichef.pro/en/digital-products/wedding-venue-business-plan'
_I, _S, _P, _R, _N, _E, _ES, _T, _F = ('Inversión Inicial', '0. Supuestos', 'PyG 3 Años', 'Personal', 'Instrucciones',
                                       'Punto Equilibrio', 'Escenarios', 'Tesorería 12 meses', 'Financiación')
REGLA_UNIDADES = ('MEDIDAS US (John, 13-oct; SPEC §0, D14): superficie en sq ft con los m² entre paréntesis («5,000 sq ft '
                  '(465 m²)»), distancias en miles, °F, gallons; nada de m², km, kg, litros ni °C como unidad principal '
                  '(gate); fechas mm/dd/yyyy; importes $ con coma de miles y punto decimal')

# ==========================================================================
# FIJOS (por TEXTO ES, en cualquier celda de los 2 libros). Parten de los de FT/CAF (los del motor 2.2)
# ==========================================================================
FIJOS_FUERA = ('Este fichero forma parte del producto «plan-negocio-food-truck» de AI Chef Pro.',
               'Este fichero forma parte del producto «plan-negocio-cafeteria» de AI Chef Pro.')
FIJOS_NUEVOS = OrderedDict([
    # Instrucciones!A3 del checklist con el nombre comercial (defecto del ES: el id interno; inv. §8)
    ('Este fichero forma parte del producto «plan-negocio-finca-eventos-bodas» de AI Chef Pro.',
     'This file is part of the Wedding Venue Business Plan Kit by AI Chef Pro.'),
    # títulos (D169 A1, D162 A1-A3)
    ('CHECKLIST DE APERTURA — FINCA DE EVENTOS Y BODAS', 'WEDDING VENUE STARTUP CHECKLIST'),
    ('INSTRUCCIONES DE USO — Plan financiero Finca de Eventos y Bodas',
     'HOW TO USE THIS WORKBOOK — Wedding Venue Financial Projections'),
    ('PLAN DE NEGOCIO: FINCA DE EVENTOS Y BODAS', 'WEDDING VENUE BUSINESS PLAN: BARN & EVENT VENUE'),
    ('Inversión inicial estimada — finca arrendada con edificaciones existentes y catering exclusivo concesionado',
     'Estimated Startup Costs — barn conversion on a leased property, 200 guests, exclusive caterer'),
    ('Ajusta las cifras a tu proyecto.',
     'US kit example (2026) — barn conversion on a leased property; replace with your own quotes.'),
    # D165: cabecera de la tabla D19
    ('DATOS DE REFERENCIA DEL SECTOR', 'US WEDDING VENUE BENCHMARKS (sourced) AND KIT ESTIMATES'),
    # D162: las 19 partidas de la inversión, filas 7-25 (solo rótulo: ninguna fila se mueve; la clase la fija la fila)
    ('Proyecto técnico y dirección de obra', 'Architect, engineer & code consultant (change of occupancy)'),
    ('Licencias, tasas, calificación urbanística y prestación compensatoria o canon',
     'Conditional use permit, zoning hearing, traffic & septic studies, permit fees'),
    ('Adecuación del salón: suelos, cerramientos, carpintería y pintura',
     'Barn renovation: floor, doors, insulation, fixtures & paint'),
    ('Acústica y aislamiento del salón', 'Fire sprinkler system (city water; a tank and fire pump cost more)'),
    ('Carpa estructural o pérgola para ceremonia y cóctel', 'Ceremony site: pergola, tent platform & ceremony seating'),
    ('Aseos: dos bloques y uno adaptado', 'ADA-compliant restrooms (septic upgrade quoted apart)'),
    ('Instalación eléctrica: cuadro, alumbrado exterior y de emergencia',
     'Electrical service, exterior, exit & emergency lighting'),
    ('Grupo electrógeno', 'Standby generator'),
    ('Climatización del salón', 'HVAC for the hall'),
    ('Office del catering: cámara, fregaderos, mesas inox, agua y desagüe',
     "Caterer's prep & warming kitchen: sinks, prep tables, ice machine, water & drain"),
    ('Mobiliario de ceremonia y banquete: mesas, sillas y mantelería base', 'Tables, chairs for 200 & base linens'),
    ('Zona chill-out y decoración base', "Bridal suite & groom's lounge furnishings and decor"),
    ('Sonido, limitador-registrador y proyector', 'Sound system, decibel meter & lighting'),
    ('Aparcamiento y caminos: zahorra, señalización e iluminación', 'Parking lot, driveway, signage & lighting'),
    ('Jardinería, paisajismo y riego inicial', 'Landscaping, lawn & irrigation'),
    ('Protección contra incendios, señalización de evacuación y accesibilidad',
     'Fire alarm, extinguishers, exit signs & ADA accessible routes'),
    ('Web, fotos, vídeo y marca', 'Website, photography, video & brand'),
    ('Constitución de la SL', 'LLC formation & attorney (lease and contracts)'),
    ('Lanzamiento: feria nupcial, puertas abiertas y escaparate premium',
     'Launch: bridal shows, open house & listing storefronts'),
    ('Fianza del arrendamiento', 'Lease security deposit'),
    ('Renta de la finca durante la obra', 'Rent during permitting and build-out'),
    ('Imprevistos de obra y acondicionamiento', 'Build-out contingency'),
    # D163: P&L (A2, A10, A11, A13-A16, fijos A22, A24-A35, ratio de renta)
    ('Escenario realista — finca de eventos y bodas',
     'Base case — barn wedding & event venue, 200 guests, exclusive caterer'),
    ('Ventas de alquiler del espacio y servicios del evento', 'Venue rental & event services'),
    ('Canon del catering exclusivo', 'Caterer commission (exclusive caterer)'),
    ('Coste directo del evento', 'Direct event costs'),
    ('Coste del canon (no tiene)', 'Cost of the commission (none)'),
    ('Consumibles de los montajes', 'Event consumables'),
    ('Comisiones de wedding planners y agencias', 'Commissions to planners and venue marketplaces'),
    ('Renta de la finca', 'Rent (leased property)'),
    ('Renta de la finca / Ventas', 'Rent / Sales'),
    ('Suministros (luz, agua, gasoil y teléfono)', 'Utilities (power, propane, water, internet & trash)'),
    ('Seguros (RC + multirriesgo)', 'Insurance (general liability, host liquor liability & property)'),
    ('Marketing: portales de bodas, Google Ads y redes', 'Marketing (The Knot/WeddingWire, Google Ads, social)'),
    ('Ferias nupciales y jornadas de puertas abiertas', 'Bridal shows & open houses'),
    ('Jardinería y mantenimiento externo (poda, césped y riego)', 'Grounds & landscaping contractors'),
    ('Reparaciones, pintura y reposición de mobiliario', 'Repairs, paint & furniture replacement'),
    ('Gestoría laboral, fiscal y contable', 'Accounting, payroll & legal'),
    ('Software de reservas, CRM, web y teléfono', 'Venue management software, CRM, website & phone'),
    ('Prevención de riesgos laborales y vigilancia de la salud', 'Safety training & compliance'),
    ('Tasas municipales e IBI repercutido', 'Property taxes passed through & local fees'),
    ('Revisiones de baja tensión, protección contra incendios y grupo electrógeno',
     'Sprinkler, alarm, extinguisher & generator inspections'),
    ('Limpieza general, desinsectación y desratización (DDD)', 'Cleaning supplies, pest control & septic pumping'),
    # D163: puestos de Staffing (A5:A10)
    ('Titular — gerencia, ventas y visitas', 'Owner — GM, sales & tours'),
    ('Coordinación de bodas y celebraciones (fijo discontinuo, marzo-noviembre)', 'Venue coordinator (seasonal, Mar-Nov)'),
    ('Mantenimiento y jardinería', 'Facilities & grounds'),
    ('Auxiliares de montaje, acceso y aseos (fijos discontinuos)',
     'Event attendants: setup, parking & restrooms (seasonal, part-time W-2)'),
    ('Comercial de bodas a tiempo parcial', 'Weekend sales & tours (part-time)'),
    ('Limpieza y puesta a punto a tiempo parcial', 'Housekeeping & turnover (part-time)'),
])

# Mismo ES con otro EN en ESTA celda, o texto de la finca con su EN fijado por la SPEC (D164, D167)
POR_CELDA = OrderedDict([
    # D167: Mes 1 = marzo con los pesos US de research §8
    (('WEDP', _T, 'O5'), 'Month 1 = MARCH: the permit and the build-out close over the winter before, and the venue opens '
                         'for the spring season. Peaks in October (Month 8), September (Month 7) and June (Month 4); the low '
                         'is January (Month 11). Kit weights for a US wedding venue: replace them with your own booking '
                         'pattern; if you open in another month, rotate the row. It must add up to 100%'),
    (('WEDP', _T, 'A34'), 'The quarters in this sheet are plan quarters, not calendar quarters (March-May, June-August, '
                          'September-November and December-February): with Month 1 in March, the workbook remits the '
                          'sales tax of each plan quarter in the month after it. Your state sets the real filing '
                          'calendar (monthly, quarterly or annual): check it. Income tax for year 1 is paid in year 2. The '
                          'loan payment is split into twelve equal parts following the ANNUAL schedule in "Financing", and '
                          'payroll into twelve monthly installments'),
    (('WEDP', _T, 'O13'), 'Twelve monthly payrolls (US: 12 pay periods, no extra pay months). The year adds up to the same '
                          'figure as the P&L. Payroll is spread over twelve months, but the seasonal venue coordinator and '
                          'event attendants only work March-November: this sheet makes the season look cheaper and the '
                          'winter dearer than reality. Expect your real cash at the end of November to be lower than shown '
                          'here; it evens out by February'),
    # D164: líneas de venta y su sales tax (sin nombrar estados hasta la revisión D174: decisión de orquestador 4)
    (('WEDP', _T, 'O16'), 'Each sales line at ITS rate, read from the sales tax column of the P&L: venue rental & event '
                          'services at the rate in G10 (8% in the example) and the caterer commission at the rate in G11 '
                          '(0% in the example: a fee your caterer pays you, not a retail sale). The venue sells no food or '
                          'drink: the caterer bills the menu and the bar to the client and collects that sales tax'),
    (('WEDP', _P, 'F10'), 'What couples and companies pay the venue: the site fee, the ceremony, setup, venue coordination on '
                          'the day, cleaning and parking · The sales tax this line COLLECTS is an input (green cell to the '
                          'right), 8% in the example. Whether a venue rental fee is taxable depends on the state (taxable '
                          'in some, exempt in others, sometimes only when it is billed together with catering): ask your '
                          "state's department of revenue."),
    (('WEDP', _P, 'F11'), 'What your exclusive caterer pays you for working at the venue. The plan assumes 10% of its food & '
                          'beverage sales at the venue, net of sales tax, service charge and gratuities: it is an '
                          'assumption, negotiate it · Sales tax: 0% in the example (green cell to the right), treated as '
                          'a fee your caterer pays you, not a retail sale to the couple. Confirm the treatment in your '
                          'state with your CPA.'),
    # D164: B62 = 0 «the venue sells no alcohol», B63 «no effect»
    (('WEDP', _S, 'A62'), 'Alcohol share of the venue\'s own sales (the venue sells none: keep it at zero)'),
    (('WEDP', _S, 'C62'), 'ZERO: the venue sells no alcohol. The bar belongs to the exclusive caterer (or a licensed '
                          'bartending service), which serves under its own liquor license or catering permit and bills it '
                          'to the client; the second sales line of the P&L is the commission the caterer pays you'),
    (('WEDP', _S, 'A63'), 'Sales tax on alcohol (the venue sells none)'),
    (('WEDP', _S, 'C63'), 'NO EFFECT in this plan: the venue sells no alcohol (the caterer does, under its own license) and '
                          'the commission line carries its own rate in column G of the P&L'),
    # D163: notas de Staffing (sin convenio, sin SMI, 12 pagas, W-2)
    (('WEDP', _R, 'A28'), 'The gross pay, employer payroll taxes, monthly cost and annual cost columns are TOTALS for the '
                          'row: for a position with two people they include both. "FTE" is the share of a full-time week '
                          'and is used to compare pay with the legal floor pro rata. The payroll tax rate and the number '
                          'of pay periods are in the "0. Assumptions" tab.'),
    (('WEDP', _R, 'A29'), 'The wage floor is the HIGHER of the federal minimum wage and the state or local floor you type '
                          'in "0. Assumptions"; part-time positions carry it pro rata. Seasonal staff are W-2 employees: '
                          'never pay as 1099 contractors the people whose schedule and work the venue directs. Event '
                          'servers and bartenders belong to the caterer, not to this payroll.'),
])

# ==========================================================================
# Cifras prohibidas (D173): ES de la finca (importe y frase), caso de la Pizza EN y RX_WED_NO.
# Formato: (regex, motivo, excepción sobre el texto entero)
# ==========================================================================
def _num(n):
    """192400 → patrón que casa 192,400 · 192.400 · 192 400 · 192400 (y nada pegado a más dígitos)."""
    s = str(n)
    cab, cola = s[:-3], s[-3:]
    return r'(?<![\d.,])' + cab + r'[.,   ]?' + cola + r'(?![\d])'


def _cifras_es():
    """Importes ≥ 10.000 € del caso ES (`../plan-finca-eventos/cifras_caso_es.json`: valores cuyo token se escribe en €)."""
    p = os.path.join(FINES, 'cifras_caso_es.json')
    if not os.path.exists(p):
        return set()
    d = json.load(open(p, encoding='utf-8'))
    tk, va = d.get('tokens', {}), d.get('valores', {})
    return {int(round(abs(x))) for k, x in va.items()
            if isinstance(x, (int, float)) and abs(x) >= 10000 and str(tk.get(k, '')).strip().endswith('€')}


FRASES_ES = [
    (r'(?i)€|\bEUR\b|\beuros?\b', 'moneda ES'),
    (r'(?i)\b82 (?:guests|people|attendees)\b', 'caso ES (82 invitados por evento)'),
    (r'(?i)\$?\b37(?:\.00)? (?:per|a) guest\b', 'caso ES (37 € por invitado)'),
    (r'(?i)\b120 (?:events|bookings)\b', 'caso ES (120 eventos)'),
    (r'(?i)(?:commission|canon)[^.;]{0,40}?\b12\s?%|\b12\s?%[^.;]{0,40}?(?:commission|canon)',
     'canon ES (12 %; el caso US es el 10 %)'),
    (r'(?i)\b14 (?:pay periods|payments|paychecks|salaries|monthly)', 'pagas del ES (14 pagas)'),
    (r'(?i)(?:payroll|social security|employer)[^.;]{0,60}?\b33\s?%', 'Seguridad Social del ES (33 %)'),
    (r'(?i)\b33\s?%[^.;]{0,40}?(?:payroll|social security|employer)', 'Seguridad Social del ES (33 %)'),
    (r'\b8[.,]8\s?%', 'margen neto ES (8,8 %)'),
    (r'(?i)\b20 ?% of (?:sales|bookings)\b', 'intermediarios ES (20 % de las ventas)'),
    (r'\b17[.,]094\b', 'SMI ES (17.094 €)'),
    (r'\bv1\.[01]\b|\b[Vv]ersion 1\.[01]\b', 'historia de versiones (la EN nace en 2.2)'),
]
FRASES_PIZ = [(r'(?i)\b62 covers\b', 'caso de la Pizza EN («62 covers»)'),
              (r'\$36(?:\.00)?\b', 'caso de la Pizza EN («$36»)'),
              (r'(?i)\b300 (?:opening )?days\b', 'caso de la Pizza EN («300 days»)')]

# D173: restos de la Pizza EN y de la Bakery + ES / eventos. NO «covers», «oven», «slice», «pastry» ni «bakery» sueltos
# (falsos positivos en prosa de venue y en la excepción de la tarta del contrato); «non-refundable» lo mira la revisión D174
RX_WED_NO = [
    (r'(?i)pizza|pizzaiol', 'Pizza EN («pizza»)', None),
    (r'(?i)\bdough', 'Pizza EN («dough»)', None),
    (r'(?i)wood-fired', 'Pizza EN («wood-fired»)', None),
    (r'(?i)covers per day|cover count', 'Pizza EN («covers per day»)', None),
    (r'(?i)average check', 'restaurante («average check»: aquí «revenue per guest»)', None),
    (r'(?i)croissant|sourdough|bakery business', 'Bakery EN', None),
    (r'(?i)\bfinca', 'ES («finca» → venue / property)', None),
    (r'(?i)\bcanon\b', 'ES («canon» → caterer commission)', None),
    (r'\bIVA\b', 'ES («IVA»)', None),
    (r'(?i)\bconvenio\b', 'ES («convenio»)', None),
    (r'\bSMI\b', 'ES («SMI»)', None),
    (r'(?i)\baut[oó]nomo', 'ES («autónomo»)', None),
    (r'(?i)comunidad aut', 'ES («comunidad autónoma»)', None),
    (r'(?i)ayuntamiento', 'ES («ayuntamiento»)', None),
    (r'\bSGAE\b|AGEDI', 'ES («SGAE»)', None),
    (r'(?i)\btestigo\b', 'ES («comida testigo»)', None),
    (r'TRLGDCU|\bLAU\b|\bLIVA\b', 'ES (norma española)', None),
    (r'(?i)\barras\b', 'ES («arras»)', None),
    (r'(?i)\bse[ñn]al\b', 'ES («señal» → retainer)', None),
    (r'(?i)fijos? discontinu', 'ES («fijo discontinuo» → seasonal W-2)', None),
    (r'(?i)calificaci[oó]n', 'ES («calificación urbanística»)', None),
    (r'(?i)parrill|\bbrasa\b|pitmaster|\bsmoker\b|paella', 'BBQ / Paella EN', None),
    (r'(?i)food truck', 'FT EN («food truck»)', None),
    (r'\bEspaña\b|\bSpain\b|\bSpanish\b', 'ES («España/Spain»)', None),
    (r'\bVAT\b', 'ES («VAT» fuera de la nota UK)', r'\bUK\b|United Kingdom|HMRC'),
    (r'(?i)Orden INT|RD \d|Real Decreto|BOE\b', 'norma española', None),
    # unidades (REGLA_UNIDADES): m², kg, km, litros y °C solo entre paréntesis
    (r'(?i)\d\s?(?:m²|m2|sq m|kg|km|°C|liters?|litres?)(?![\w])(?![^()]*\))',
     'unidades: métrica solo entre paréntesis (REGLA_UNIDADES)', None),
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


def _importes_research():
    """Importes en dólares ≥ 10,000 que cita la research de la finca o su SPEC: datos de ESTE producto, no se vetan."""
    out = set()
    for f in ('F1-research-us-delta.md', 'SPEC-delta.md'):
        p = os.path.join(AQUI, f)
        t = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
        out |= {int(x.replace(',', '')) for x in re.findall(r'\$\s?(\d{1,3}(?:,\d{3})+)', t)
                if int(x.replace(',', '')) >= 10000}
        out |= {int(x) * 1000 for x in re.findall(r'\$\s?(\d{2,3})K\b', t)}
        out |= {int(x.replace(',', '')) for x in re.findall(r'\b(\d{2,3},\d{3})\b', t)}
    return out


def cifras_prohibidas(valores):
    """CIFRAS_PROHIBIDAS del conjunto (D173). Fuera las cifras que coinciden con un valor del propio caso US o con un
    importe de la research/SPEC de este producto."""
    propios = {int(round(x[0])) for x in valores.values() if isinstance(x[0], (int, float))}
    propios |= _importes_research()
    out = [(_num(n), 'cifra del caso ES de la finca (D173)', None) for n in sorted(_cifras_es()) if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_ES]
    out += [(_num(n), 'cifra del caso de la Pizza EN (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(PIZ, 'cifras_caso.json'), 'piz') if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_PIZ]
    out += RX_WED_NO
    return out


# ==========================================================================
# Tokens del docx (D170): los de FT/CAF con los rótulos de la finca + partidas y métricas propias
# ==========================================================================
_ROT = OrderedDict([
    ('Clientes/día (media del año 1)', 'Invitados por evento (media del año 1)'),
    ('Clientes/día (media)', 'Invitados por evento (media)'),
    ('Clientes/día', 'Invitados por evento'),
    ('Clientes necesarios al día', 'Invitados necesarios por evento'),
    ('Clientes necesarios al día (caja)', 'Invitados necesarios por evento (caja)'),
    ('Ticket medio SIN IVA (€)', 'Precio medio por invitado SIN IVA (€)'),
    ('Ticket medio sin IVA', 'Precio medio por invitado sin IVA'),
    ('Días de apertura al año', 'Eventos al año'),
    ('Alquiler mensual del local (€)', 'Renta mensual de la finca (€)'),
    ('Suministros mensuales de luz, agua y gas (€)', 'Suministros mensuales (luz, agua, gasoil y teléfono) (€)'),
    ('Marketing y publicidad', 'Marketing: portales de bodas, Google Ads y redes'),
])
_DICT_ROT = {'ocupacion_anual': 'Renta de la finca', 'ocupacion_pct': 'Renta de la finca / Ventas'}
_DESC = OrderedDict([
    ('clientes_dia', 'average guests per event, year 1 (mix of weddings, corporate events, private celebrations and '
                     'micro weddings)'),
    ('clientes_a2', 'average guests per event, year 2 (growth is modeled on guests per event = events in dollars)'),
    ('clientes_a3', 'average guests per event, year 3'),
    ('ticket', 'average revenue per guest to the VENUE, excl. sales tax (venue rental & services + caterer commission; '
               'NOT what the couple pays for the whole wedding)'),
    ('precio_menu', 'average revenue per guest to the venue, incl. sales tax'),
    ('dias', 'events per year'),
    ('sales_tax', 'example sales tax rate on venue rental & services'),
    ('consumibles_pct', 'event consumables, % of sales'),
    ('salario_minimo_federal', 'federal minimum wage, annual full-time ($7.25/h)'),
    ('alquiler_mes', 'rent per month (leased property with an existing barn)'),
    ('suministros_mes', 'utilities per month (power, propane, water, internet & trash)'),
    ('vida_obra', 'useful life of leasehold improvements (the barn conversion), years'),
    ('ocupacion_anual', 'rent per year'),
    ('ocupacion_pct', 'rent, % of sales'),
    ('marketing_anual', 'marketing per year (The Knot/WeddingWire storefronts, Google Ads, social)'),
    ('equilibrio_clientes_dia', 'break-even guests per event at the planned number of events (accounting, depreciation in)'),
    ('equilibrio_caja_clientes_dia', 'cash break-even guests per event (loan payments in, depreciation out)'),
    ('pesimista_clientes', 'pessimistic scenario: guests per event'),
    ('optimista_clientes', 'optimistic scenario: guests per event'),
    ('pesimista_ticket', 'pessimistic scenario: revenue per guest excl. sales tax'),
    ('optimista_ticket', 'optimistic scenario: revenue per guest excl. sales tax'),
    ('pesimista_dias', 'pessimistic scenario: events per year'),
    ('optimista_dias', 'optimistic scenario: events per year'),
    ('horas_semana', 'full-time hours per week'),
])
_FUERA = ('inv_vehiculo', 'inv_adaptacion', 'inv_equipo_cocina', 'inv_generador', 'inv_permisos', 'inv_espresso',
          'inv_obra', 'inv_instalaciones', 'inv_mobiliario', 'inv_barra', 'inv_terraza', 'inv_lanzamiento',
          'inv_stock', 'aforo', 'rotaciones_dia', 'food_cost_comida', 'food_cost_bebida', 'cogs_pct', 'ventas_dia')


def _inv(rot, desc):
    return ('usd', ('fila', _I, {'wed': rot}, 'B'), desc)


def _f(fmt, hoja, rot, col, desc):
    return (fmt, ('fila', hoja, {'wed': rot}, col), desc)


TOKENS_PROPIOS = OrderedDict([
    # inversión (D162): las 19 partidas + fianza, renta previa, imprevistos y bases de amortización
    ('inv_proyecto', _inv('Proyecto técnico y dirección de obra', 'architect, engineer and code consultant (change of '
                          'occupancy drawings)')),
    ('inv_cup', _inv('Licencias, tasas, calificación urbanística y prestación compensatoria o canon',
                     'conditional use permit, zoning hearing, traffic and septic studies, permit fees')),
    ('inv_reforma', _inv('Adecuación del salón: suelos, cerramientos, carpintería y pintura',
                         'barn renovation: floor, doors, insulation, fixtures and paint')),
    ('inv_sprinklers', _inv('Acústica y aislamiento del salón', 'fire sprinkler system (city water; a tank and fire pump '
                            'cost more)')),
    ('inv_ceremonia', _inv('Carpa estructural o pérgola para ceremonia y cóctel', 'ceremony site: pergola, tent platform '
                           'and ceremony seating')),
    ('inv_aseos', _inv('Aseos: dos bloques y uno adaptado', 'ADA-compliant restrooms (septic upgrade quoted apart)')),
    ('inv_electrica', _inv('Instalación eléctrica: cuadro, alumbrado exterior y de emergencia',
                           'electrical service, exterior, exit and emergency lighting')),
    ('inv_generador', _inv('Grupo electrógeno', 'standby generator')),
    ('inv_hvac', _inv('Climatización del salón', 'HVAC for the hall')),
    ('inv_office', _inv('Office del catering: cámara, fregaderos, mesas inox, agua y desagüe',
                        "caterer's prep and warming kitchen")),
    ('inv_mobiliario', _inv('Mobiliario de ceremonia y banquete: mesas, sillas y mantelería base',
                            'tables, chairs for 200 and base linens')),
    ('inv_suite', _inv('Zona chill-out y decoración base', "bridal suite and groom's lounge furnishings and decor")),
    ('inv_sonido', _inv('Sonido, limitador-registrador y proyector', 'sound system, decibel meter and lighting')),
    ('inv_parking', _inv('Aparcamiento y caminos: zahorra, señalización e iluminación',
                         'parking lot, driveway, signage and lighting')),
    ('inv_jardin', _inv('Jardinería, paisajismo y riego inicial', 'landscaping, lawn and irrigation')),
    ('inv_pci', _inv('Protección contra incendios, señalización de evacuación y accesibilidad',
                     'fire alarm, extinguishers, exit signs and ADA accessible routes')),
    ('inv_marca', _inv('Web, fotos, vídeo y marca', 'website, photography, video and brand')),
    ('inv_llc', _inv('Constitución de la SL', 'LLC formation and attorney (lease and contracts)')),
    ('inv_lanzamiento', _inv('Lanzamiento: feria nupcial, puertas abiertas y escaparate premium',
                             'launch: bridal shows, open house and listing storefronts')),
    ('inv_fianza', _inv('Fianza del arrendamiento', 'lease security deposit')),
    ('inv_renta_previa', _inv('Renta de la finca durante la obra', 'rent paid during permitting and build-out')),
    ('inv_imprevistos', _inv('Imprevistos de obra y acondicionamiento', 'build-out contingency (a % of the build-out '
                             'items, by formula)')),
    ('base_obra', _f('usd', _I, 'Obra, instalaciones y acondicionamiento', 'B', 'depreciable leasehold improvements '
                     '(build-out items + contingency)')),
    ('base_equipo', _f('usd', _I, 'Maquinaria, mobiliario y equipos', 'B', 'depreciable furniture and equipment')),
    # supuestos
    ('aforo', _f('int', _S, 'Aforo de la finca (invitados sentados en el salón y la carpa)', 'B',
                 'seated capacity of the hall (the occupant load is set by the fire marshal)')),
    ('espacio_pct', _f('pct0', _S, 'Ventas de ESPACIO Y SERVICIOS sobre el total', 'B',
                       'venue rental & event services, % of sales')),
    ('comision_caterer_pct', _f('pct0', _S, 'Ventas del CANON DEL CATERING sobre el total', 'B',
                                'caterer commission, % of the venue\'s sales')),
    ('coste_directo_pct', _f('pct0', _S, 'Coste directo del evento sobre las ventas de ESPACIO Y SERVICIOS', 'B',
                             'direct event cost, % of venue rental & services')),
    ('intermediarios_pct', _f('pct0', _S, 'Ventas que llegan por wedding planners y agencias sobre el total', 'B',
                              'share of sales booked through planners and venue marketplaces')),
    ('comision_intermediarios_pct', _f('pct0', _S, 'Comisión de los wedding planners y agencias', 'B',
                                       'commission paid to planners and venue marketplaces on those bookings')),
    ('varios_pct', _f('pct0', _S, 'Varios e imprevistos sobre ventas', 'B', 'miscellaneous and contingency, % of sales')),
    ('meses_alquiler_previo', _f('int', _S, 'Meses de renta ANTES de abrir (obra y licencias)', 'B',
                                 'months of rent paid before opening (permits and build-out)')),
    ('imprevistos_obra_pct', _f('pct0', _S, 'Imprevistos sobre las partidas de OBRA del bloque de la finca (%)', 'B',
                                'build-out contingency, % of the build-out items')),
    # P&L
    ('ventas_espacio_a1', _f('usd', _P, 'Ventas de alquiler del espacio y servicios del evento', 'B',
                             'venue rental & event services revenue, year 1')),
    ('comision_caterer_a1', _f('usd', _P, 'Canon del catering exclusivo', 'B', 'caterer commission revenue, year 1')),
    ('comision_caterer_a3', _f('usd', _P, 'Canon del catering exclusivo', 'D', 'caterer commission revenue, year 3')),
    ('coste_directo_a1', _f('usd', _P, 'Coste directo del evento', 'B', 'direct event costs, year 1')),
    ('comisiones_intermediarios_a1', _f('usd', _P, 'Comisiones de wedding planners y agencias', 'B',
                                        'commissions to planners and venue marketplaces, year 1')),
    ('ferias_anual', _f('usd', _P, 'Ferias nupciales y jornadas de puertas abiertas', 'B',
                        'bridal shows and open houses per year')),
    ('coste_directo_ventas_pct', _f('pct1', _P, 'Coste directo del evento / Ventas', 'B',
                                    'direct event costs, % of total sales, year 1')),
    ('margen_neto_a2', _f('pct1', _P, 'Resultado neto / Ventas', 'C', 'net margin year 2')),
    ('margen_neto_a3', _f('pct1', _P, 'Resultado neto / Ventas', 'D', 'net margin year 3')),
    # personal y financiación
    ('horas_evento', _f('dec1', _R, 'Horas de trabajo por evento que hay que cubrir', 'B',
                        'hours of event-day work to cover per event')),
    ('personas_evento', _f('dec1', _R, 'Personas necesarias a la vez en cada evento', 'B',
                           'venue staff needed at the same time on an event day')),
    ('horas_estructura', _f('int', _R, 'Horas de estructura por evento, fuera del día del evento', 'B',
                            'hours of off-day work per event (tours, setup, turnover)')),
    ('sueldo_titular', _f('usd', _R, 'Titular — gerencia, ventas y visitas', 'D', "owner's gross pay per month")),
    ('holgura_caja_a2', _f('pct0', _E, 'Holgura sobre el equilibrio de CAJA (%)', 'C', 'margin of safety over cash '
                           'break-even, year 2')),
    ('holgura_caja_a3', _f('pct0', _E, 'Holgura sobre el equilibrio de CAJA (%)', 'D', 'margin of safety over cash '
                           'break-even, year 3')),
    ('dscr_a2', _f('x2', _F, 'DSCR del año 2', 'B', 'DSCR year 2')),
    ('dscr_a3', _f('x2', _F, 'DSCR del año 3', 'B', 'DSCR year 3')),
    ('exceso_fondos_pct', _f('pct1', _F, 'Diferencia sobre los usos (%)', 'B',
                             'funding surplus over the cash needed (sources − uses), %')),
    # derivados (D170: eventos de equilibrio y eventos equivalentes)
    ('ingreso_evento', ('usd', ('deriv', lambda c: c['ventas_a1'] / c['dias']),
                        'average venue revenue per event, year 1 (excl. sales tax)')),
    ('invitados_ano', ('int', ('deriv', lambda c: c['clientes_dia'] * c['dias']), 'guests per year, year 1')),
    ('equilibrio_eventos', ('ceil', ('deriv', lambda c: c['equilibrio_ventas'] / (c['ventas_a1'] / c['dias'])),
                            'break-even in events of the average size (accounting)')),
    ('equilibrio_caja_eventos', ('ceil', ('deriv', lambda c: c['equilibrio_caja_ventas'] / (c['ventas_a1'] / c['dias'])),
                                 'cash break-even in events of the average size')),
    ('eventos_equivalentes_a2', ('int', ('deriv', lambda c: c['ventas_a2'] / (c['ventas_a1'] / c['dias'])),
                                 'year-2 revenue expressed in events of the year-1 average size')),
    ('eventos_equivalentes_a3', ('int', ('deriv', lambda c: c['ventas_a3'] / (c['ventas_a1'] / c['dias'])),
                                 'year-3 revenue expressed in events of the year-1 average size')),
    ('costes_variables_pct', ('pct1', ('deriv', lambda c: 1 - c['margen_bruto_pct']),
                              'all variable costs year 1 (direct event cost + consumables + commissions + card fees + '
                              'contingency), % of sales')),
    ('pesimista_perdida', ('usd', ('deriv', lambda c: -c['pesimista_resultado']),
                           'pessimistic scenario: pre-tax LOSS as a positive amount (only if it is a loss)')),
])


def tokens_wed(base):
    out = OrderedDict()
    for t, (fmt, src, desc) in base.items():
        if t in _FUERA:
            continue
        if src[0] == 'fila':
            _, hoja, rot, col = src
            if isinstance(rot, dict):
                rot = _DICT_ROT[t]
            else:
                rot = _ROT.get(rot, rot)
            src = ('fila', hoja, {'wed': rot}, col)
        if t == 'consumibles_pct':
            fmt = 'pct1'
        out[t] = (fmt, src, _DESC.get(t, desc))
    out.update(TOKENS_PROPIOS)
    return out


# ==========================================================================
# Docx (D170): lo que escribe ensamblar_docx.py (índices del FT ES de 131 párrafos = PAEL/PIZ) y las notas por ranura
# ==========================================================================
PRODUCTOS_CIERRE_WED = ['Catering Business Plan Kit', 'Mobile Bar Business Plan Kit', 'Catering Checklists Kit Pro']


def docx_fijos(M):
    pc = PRODUCTOS_CIERRE_WED
    d = OrderedDict([
        (6, 'BUSINESS PLAN'), (7, 'Wedding & Event Venue'),
        (9, 'Complete financial plan, market analysis,\noperations strategy and startup checklist\nto open a '
            'wedding and event venue in the United States'),
        (14, 'AI Chef Pro'), (15, 'aichef.pro'), (16, 'US edition with UK notes · 2026'),
        (18, 'LEGAL NOTICE'), (19, M.AVISO_DOCX_EN), (20, '© 2026 AI Chef Pro — aichef.pro'), (22, 'CONTENTS'),
        (35, 'Appendices: Excel Financial Plan + Startup Checklist + Pricing Calculator + Rental Agreement Templates + '
             'Equivalents Guide'),
        (123, 'AI Chef Pro'), (124, 'Templates and AI tools for hospitality businesses'),
        (126, 'aichef.pro\ninfo@aichef.pro'),
        (127, '→ ' + pc[0]), (128, '→ ' + pc[1]), (129, '→ ' + pc[2]), (130, '\n' + M.URL_TIENDA),
    ])
    return OrderedDict([('wed', d)])


_ARRIENDO = ('ARRENDAMIENTO (decisión de orquestador 1): la obra (≈ {{capex}} de CAPEX) se hace sobre una propiedad '
             'ARRENDADA: exige un arrendamiento largo cuya duración CONTANDO LAS PRÓRROGAS sea al menos la del préstamo '
             '(«SBA lenders typically require…; confirm with your lender», sin citar una regla concreta), opción de '
             'compra o derecho de tanteo (right of first refusal), consentimiento del propietario a la obra y a usar el '
             'arrendamiento como garantía, y negociar una TI allowance; lease contingent on CUP approval. Comprar la '
             'propiedad (SBA 504) = variante razonada SIN Excel')
DOCX_NOTAS_PLAN = OrderedDict([
    ('wed', 'Concepto (D159): BARN / ESTATE WEDDING & EVENT VENUE en una propiedad rural o periurbana ARRENDADA a 30-60 '
            'min de una ciudad media-grande de EE. UU.: salón para {{aforo}} invitados sentados, ceremonia exterior con '
            'pérgola, bridal suite, aseos ADA, aparcamiento de grava y cocina de apoyo para el caterer. El venue factura '
            'venue rental fee + servicios y cobra una caterer commission al EXCLUSIVE CATERER, que factura comida y '
            'barra a la pareja y sirve el alcohol con SU licencia (el venue no vende alcohol). Mes 1 = marzo. «Wedding '
            'venue» en el nombre, «event venue» como descriptor, «venue» en prosa (nunca «finca», «estate» ni «farm» '
            'como nombre); volumen = guests · revenue per guest · events per year (nunca covers ni average check). Cada '
            'cifra del caso va con su token {{…}}; las de mercado solo con fuente leída (research §5.1-5.2 marca '
            '«(resumen)» casi todo: The Knot, rate cards, NY/MO, §1671, 40 CFR 141.2, rentas, seguros, sprinklers y fosa '
            'séptica van como «typical range, get local quotes» o «ask…», nunca como cifra rotunda: decisión de '
            'orquestador 4). Honestidad: el año 1 cuenta {{dias}} eventos (≈ 35 bodas) y el neto es '
            '{{margen_neto_a1}}, no los márgenes de venues en propiedad de la SERP; NINGUNA fecha firme sin CUP y '
            'certificate of occupancy (holds contingentes con devolución íntegra). ' + _ARRIENDO + '. Fuera (como '
            'alternativas razonadas en §2 y §10): comprar el inmueble, in-house catering (→ Catering Business Plan Kit), '
            'banquet hall urbano, wedding planner. Glosario research §9 obligatorio. El cierre (productos) lo escribe el '
            'ensamblador. ' + REGLA_UNIDADES),
])

_FORMA_PIZ = ('FORMA: la sección §%d de la Pizza EN (business-plans-en-8/docx_en_piz_%s.json) da el registro y la longitud; '
              'su vocabulario (pizza, covers, dine-in, oven…) y sus cifras NO valen. CONTENIDO: el párrafo ES de la finca '
              '(campo «es») adaptado a EE. UU.')
_SEC = OrderedDict([
    (1, ('a', 'Resumen ejecutivo: concepto (D159), la oportunidad (research §2: «wedding venue business plan» 1,000/mes y '
              '«event venue business plan» 720/mes, creciendo), inversión y financiación SOLO con tokens '
              '({{inversion_total}}, {{capex}}, {{prestamo}} SBA 7(a) {{tipo_prestamo}} a {{plazo_prestamo}} años, '
              '{{fondos_propios}}), ventas ({{ventas_a1}} = {{clientes_dia}} guests × {{ticket}} × {{dias}} events), '
              'neto {{margen_neto_a1}}, DSCR {{dscr_min}}; el venue vive del site fee + caterer commission')),
    (2, ('a', 'Concepto y propuesta: barn venue de 200 invitados, ceremonia exterior, bridal suite, exclusive caterer '
              '(por qué exclusivo frente a preferred vendor list o in-house catering: alternativas razonadas); el '
              'arrendamiento y sus condiciones (' + _ARRIENDO + '); buy vs lease razonado')),
    (3, ('a', 'Mercado y competencia: demanda de bodas y eventos en EE. UU. SIN cifras rotundas sin fuente leída (The Knot '
              'solo como «national wedding studies publish yearly averages: check the latest»); temporada: otoño, '
              'septiembre-octubre y junio como picos (pesos del libro, Kit); rate cards publicadas como «typical range, '
              'get local quotes»; competencia: otros barn venues, banquet halls, hoteles, venues municipales')),
    (4, ('a', 'Cliente y posicionamiento: parejas (bodas, micro weddings / elopements), empresas, celebraciones privadas '
              '(showers, quinceañeras, cumpleaños, rehearsal dinners); el precio por invitado del venue ({{ticket}}) no es '
              'lo que paga la pareja por la boda entera; peak / shoulder / off-peak y sábado / viernes-domingo / entre '
              'semana (calculadora del kit)')),
    (5, ('a', 'Marketing y ventas: venue tours, open house con el caterer, bridal shows ({{ferias_anual}}), The Knot / '
              'WeddingWire storefronts midiendo el coste por lead, Google Business Profile, planners y venue marketplaces '
              '({{intermediarios_pct}} de las ventas al {{comision_intermediarios_pct}}), pricing guide, venue '
              'management software; retainer y calendario de cobros (calculadora y contrato del kit)')),
    (6, ('b', 'Operaciones: el día del evento (setup, ceremony, reception, load-out, curfew), rain plan, occupant load '
              '(fire marshal), decibel limit, la cocina de apoyo del caterer ({{inv_office}}), sprinklers '
              '({{inv_sprinklers}}), restrooms ADA ({{inv_aseos}}), generador ({{inv_generador}}), parking '
              '({{inv_parking}}); coste directo por evento (limpieza, restrooms, generator fuel, parking attendants, '
              'security) = {{coste_directo_pct}} del espacio y servicios')),
    (7, ('b', 'Organización y personal: Owner — GM, sales & tours ({{sueldo_titular}} al mes: «draw the rest from '
              'profit»), venue coordinator seasonal W-2 (Mar-Nov), facilities & grounds, event attendants seasonal '
              'part-time W-2, weekend sales & tours, housekeeping ({{plantilla_puestos}} personas = {{plantilla_jornadas}} '
              'FTE; cobertura {{cobertura_horas}}); employer payroll taxes {{cargas_pct}}; nunca 1099 para quien el venue '
              'dirige; camareros y bartenders son del caterer')),
    (8, ('b', 'Plan financiero: TODO con tokens (ventas años 1-3, mezcla {{espacio_pct}} espacio y servicios / '
              '{{comision_caterer_pct}} comisión, costes variables {{costes_variables_pct}}, personal {{personal_pct}}, '
              'renta {{ocupacion_pct}}, EBITDA {{ebitda_pct_a1}}, neto {{margen_neto_a1}} / {{margen_neto_a3}}, equilibrio '
              '{{equilibrio_eventos}} / {{equilibrio_caja_eventos}} eventos del tamaño medio, holgura {{holgura_caja_pct}}, '
              'DSCR {{dscr_min}}, saldo mínimo {{saldo_minimo}} en el Month {{mes_saldo_minimo}}, escenarios); el Word '
              'dice la verdad: el año 1 cuenta solo {{dias}} eventos')),
    (9, ('b', 'Marco legal US (ver las notas propias de cada ranura de §9)')),
    (10, ('b', 'Hoja de ruta: el orden del checklist (84 tareas en 6 fases: business setup, zoning & permits, build-out & '
               'equipment, staff & caterer, brand & bookings, season & events); ninguna fecha firme antes del CUP y del '
               'certificate of occupancy; alternativas razonadas (comprar con SBA 504, in-house catering, preferred '
               'vendors); cierre con el Excel, la calculadora de precios, los contratos y el checklist')),
])
_RANURAS = OrderedDict([(1, range(39, 44)), (2, range(46, 51)), (3, range(53, 59)), (4, range(61, 67)),
                        (5, range(69, 76)), (6, range(78, 83)), (7, range(85, 91)), (8, range(93, 100)),
                        (9, range(102, 109)), (10, range(111, 118))])
_N9 = OrderedDict([
    (102, '§9 1/7: el marco US por niveles (federal, estatal, condado); LLC + EIN; business license y sales tax permit; '
          'ZONING ANTES DE FIRMAR: conditional / special use permit del condado (audiencia pública, condiciones: tope de '
          'eventos, horario, tráfico, ruido); lease contingent on CUP approval; ' + _ARRIENDO),
    (103, '§9 2/7: building / fire code: convertir un granero en salón = change of occupancy a assembly (Group A-2) → '
          'building permit y certificate of occupancy; sprinklers según IBC 903.2.1.2 «as adopted» (umbrales de ocupación '
          'o de superficie: «editions and local amendments vary», sin cifras rotundas); occupant load fijado y rotulado '
          'por el fire marshal; carpas con su propio permiso; «ask the building official and the fire marshal in '
          'writing»; los sprinklers con depósito y bomba, o una fosa séptica nueva, pueden doblar la partida'),
    (104, '§9 3/7: ADA Title III (public accommodation: rutas accesibles, aseos, parking; «old buildings are '
          'grandfathered» es un mito, sin cita de cifras); agua y saneamiento: septic comercial dimensionado por '
          'invitados (pídele al ingeniero el cálculo); pozo: «ask your state drinking water program whether your well '
          'counts as a public water system» (sin citar 40 CFR 141.2 hasta la revisión D174)'),
    (105, '§9 4/7: alcohol: el venue NO vende; lo sirve el exclusive caterer (o un bartending service licenciado) con su '
          'licencia o permiso de catering y su liquor liability, con el venue como additional insured; BYOB solo con '
          'bartender licenciado y host liquor liability del cliente; algunos estados regulan los venues que acogen '
          'alcohol: «ask your state ABC» (sin citar leyes estatales concretas hasta D174); ID y nada a menores ni a '
          'personas ebrias'),
    (106, '§9 5/7: sales tax del venue: el site fee tributa en unos estados y no en otros (a veces solo si se factura '
          'con catering); la comisión del caterer suele ser una fee entre empresas: el libro pone {{sales_tax}} en el '
          'espacio y 0 % en la comisión como EJEMPLO: «ask your state\'s department of revenue / your CPA» (sin nombrar '
          'estados hasta D174); música: licencias ASCAP/BMI/SESAC del venue; ruido: ordenanza del condado y condiciones '
          'del CUP (curfew, decibel limit)'),
    (107, '§9 6/7: seguros y contratos: general liability, property, umbrella, host liquor liability, workers\' comp '
          '({{seguros_anual}} al año: Kit estimate, pide cotizaciones); COI de cada vendor con el venue como additional '
          'insured; event insurance de la pareja; contrato: retainer aplicado al precio, tramos de cancelación como '
          'estimación razonable del daño (no penalty) con rebooking credit y revisión de un abogado del estado '
          '(«non-refundable» NUNCA sin ese matiz); si se firma en una bridal show o fuera del venue: «ask your attorney '
          'whether the FTC Cooling-Off Rule or your state\'s home-solicitation law applies; many venues give a short '
          'cancellation window for show-floor signings anyway» (decisión de orquestador 2: NO afirmar que aplica); '
          'seasonal W-2, I-9, salario mínimo estatal (federal $7.25/h, DOL), FLSA'),
    (108, '§9 7/7: la ceremonia: la licencia de matrimonio la da el county clerk y el officiant lo regula cada estado; '
          'el venue solo acoge; y, como ÚLTIMA frase o frases, la NOTA UK: planning permission (change of use) del '
          'council, approved premises para ceremonias civiles («check with your council»), VAT en el alquiler («ask your '
          'accountant»), premises licence + personal licence para el alcohol, fire risk assessment (Regulatory Reform '
          '(Fire Safety) Order 2005)'),
])


def _notas_docx():
    out = OrderedDict()
    for s, filas in _RANURAS.items():
        tanda, nota = _SEC[s]
        for k, i in enumerate(filas, 1):
            n = _N9.get(i) or ('§%d %d/%d: %s' % (s, k, len(filas), nota))
            out[i] = n + ' ‖ ' + _FORMA_PIZ % (s, tanda)
    return out


DOCX_NOTAS = OrderedDict([('wed', _notas_docx())])

# ==========================================================================
# Pistas por celda (extraer_textos.py → textos_es.json → tandas)
# ==========================================================================
_CASO = ('D160: caso US = 90 invitados por evento (media del año 1) × $68 por invitado (lo que factura el VENUE, sin sales '
         'tax: venue rental & services + caterer commission) × 100 eventos (35 weddings, 25 corporate, 30 private '
         'celebrations, 10 micro weddings / elopements); el venue no vende comida ni alcohol; sin cifras del ES ni historia '
         'de versiones')
CELDA_PISTAS = OrderedDict([
    (('WEDP', _S, 'A2'), 'D8: añade una vez que los importes van «in your currency» (sin símbolo)'),
    (('WEDP', _S, 'C4'), _CASO + '; mezcla (research §8, Kit): weddings 130 guests, corporate 70, private 80, micro 30 → '
                                 '9,000 guests / 100 events = 90; la capacidad (200) está más abajo'),
    (('WEDP', _S, 'C5'), _CASO + '; por mezcla (Kit): wedding $9,000 site fee + 10% × $110 F&B × 130 guests; corporate '
                                 '$3,500 + 10% × $50 × 70; private $4,000 + 10% × $55 × 80; micro $2,000 + 10% × $80 × 30 → '
                                 '≈ $68 por invitado; NO es lo que paga la pareja por la boda entera'),
    (('WEDP', _S, 'C6'), _CASO + '; el techo lo ponen los sábados de temporada (≈ 30-35 al año, Kit); es el MISMO dato del '
                                 'P&L, el equilibrio, los escenarios y las horas de personal'),
    (('WEDP', _S, 'C7'), 'D160: +8 % en el año 2 (referrals, empresas que repiten, planners); se aplica a los invitados por '
                         'evento con los mismos eventos = eventos en dólares; el personal crece con las incorporaciones de '
                         'Staffing, no con este %'),
    (('WEDP', _S, 'C8'), 'D160: +5 % sobre el año 2; el techo lo ponen los sábados de temporada y la capacidad'),
    (('WEDP', _S, 'C11'), 'D160: 88 % de las ventas del venue = venue rental & event services; el resto (12 %) = caterer '
                          'commission (10 % de la venta de F&B del caterer). Es un INPUT'),
    (('WEDP', _S, 'C13'), 'D160: 12 % de venue rental & services = coste directo del evento (limpieza, restrooms, generator '
                          'fuel, parking attendants y security, consumibles de montaje); ≈ $1,000 una boda, $500 corporate '
                          'o private, $300 micro (Kit, = calculadora)'),
    (('WEDP', _S, 'C14'), 'D160: la comisión del caterer no tiene coste para el venue (0 %)'),
    (('WEDP', _S, 'C15'), 'D160: 1.5 % (consumibles de montaje: candles, tape, restroom supplies…)'),
    (('WEDP', _S, 'C16'), 'D160: 10 % de las ventas llega por planners y venue marketplaces (Peerspace y similares); las '
                          'storefronts de The Knot / WeddingWire son coste fijo de marketing, no comisión'),
    (('WEDP', _S, 'C17'), 'D160: 15 % de comisión sobre esas reservas (Kit estimate: marketplaces publican 15-20 %; '
                          'compruébalo en tu contrato)'),
    (('WEDP', _S, 'C18'), 'D160: 2 % card processing (los retainers se cobran por ACH o tarjeta)'),
    (('WEDP', _S, 'C20'), 'D160: employer payroll taxes ≈ 10 % (FICA 7.65 % + FUTA/SUTA + workers\' comp aparte en '
                          'seguros): «check with your payroll provider»'),
    (('WEDP', _S, 'C21'), 'D160: 12 pay periods al año en el libro (sin pagas extra en EE. UU.)'),
    (('WEDP', _S, 'C22'), 'D160: federal $7.25/h × 2,080 h = $15,080; el suelo de tu estado va en «Suelo salarial» (B68)'),
    (('WEDP', _S, 'C24'), 'D160: $5,000/mes por una propiedad con un granero sin convertir (Kit estimate, sin fuente de '
                          'mercado: «get local quotes»); pacta la renta durante el permiso (meses de renta previa abajo)'),
    (('WEDP', _S, 'C26'), 'D160: $2,000/mes (power, propane, water/well, internet, trash; Kit estimate)'),
    (('WEDP', _S, 'C27'), 'D160: $12,000/año = general liability, property, umbrella, host liquor liability y workers\' '
                          'comp (Kit estimate, sin tarifa leída: «get quotes from an agent who insures venues»)'),
    (('WEDP', _S, 'C31'), 'D160: SBA 7(a) al 10 % a 10 años, sin interest-only; el préstamo lo calcula "Financing". '
                          'Decisión de orquestador 1: el arrendamiento, CONTANDO LAS PRÓRROGAS, debe durar al menos lo '
                          'que el préstamo («SBA lenders typically require…; confirm with your lender»)'),
    (('WEDP', _S, 'C51'), 'D160: 200 invitados sentados; la occupant load la fija y la rotula el fire marshal'),
    (('WEDP', _S, 'C54'), 'D160: 4 meses de renta antes de abrir (CUP y obra); mejor: lease contingent on CUP approval '
                          'y renta reducida durante el permiso'),
    (('WEDP', _S, 'C55'), 'D162: 10 % de las partidas de OBRA (por fórmula); sprinklers con depósito y bomba, una fosa '
                          'séptica nueva o un condado exigente pueden doblar partidas: «get local quotes»'),
    (('WEDP', _S, 'C58'), 'D160: 10 días medios de cobro (retainers y pagos por calendario: 25 % al firmar, 35 % a 180 '
                          'días, 40 % a 30 días del evento)'),
    (('WEDP', _S, 'C59'), 'D160: 14 días medios de pago a proveedores'),
    (('WEDP', _N, 'A5'), 'Instrucciones: la hoja de mando lista guests per event, revenue per guest excl. sales tax, events '
                         'per year, mezcla venue rental & services / caterer commission, direct event cost, rent'),
    (('WEDP', _N, 'A8'), 'SPEC §4.1 línea 4: sin divisores 1,21 → «to turn a price that includes sales tax into the '
                         'pre-tax price, divide by 1 + your sales tax rate»; P&L excl. sales tax, cash flow incl.; el '
                         'venue factura venue rental & services (8 % de ejemplo) y la comisión del caterer (0 %); el menú '
                         'y la barra los factura el caterer'),
    (('WEDP', _N, 'A10'), 'D167: Mes 1 = MARZO (el permiso y la obra se cierran en el invierno anterior); picos octubre, '
                          'septiembre y junio'),
    (('WEDP', _N, 'A12'), 'El Word cita las cifras de este Excel (si cambias el libro, manda el Excel); la calculadora de '
                          'precios y los contratos del kit usan los mismos porcentajes de cobro y cancelación'),
    (('WEDP', _R, 'J5'), 'D163: el dueño cobra $4,500/mes en nómina, por debajo de la mediana nacional de los event '
                         'planners (BLS, sin cifra): «draw the rest from profit»; el tratamiento fiscal del sueldo de un '
                         'socio de LLC depende de la elección fiscal: «ask your CPA»'),
])
for _f_, _nota in [(7, 'D162: drawings para el change of occupancy a assembly (A-2) y el building permit'),
                   (8, 'D162: CUP / SUP del condado (audiencia, estudios de tráfico y de la fosa séptica, tasas); sin '
                       'cifras de condados concretos'),
                   (9, 'D162: la obra cosmética es la parte pequeña: sprinklers, fosa séptica, aseos y accesibilidad '
                       'mandan (research §4)'),
                   (10, 'D162: «sprinklers need city water; a tank and fire pump, a new septic system or a strict county '
                        'can double this line» (research §4, sin cifras de anécdotas)'),
                   (12, 'D162: aseos ADA; la ampliación de la fosa séptica se presupuesta aparte (ingeniero)'),
                   (16, 'D162: cocina de apoyo (prep & warming), no de producción: el caterer cocina en su commissary; '
                        'health plan review si tu condado lo exige'),
                   (20, 'D162: grava, iluminación y plazas accesibles (ADA)'),
                   (24, 'D162: LLC + abogado para el arrendamiento (prórrogas, opción de compra, consentimiento a la obra '
                        'y garantía: decisión de orquestador 1) y los contratos')]:
    CELDA_PISTAS[('WEDP', _I, 'D%d' % _f_)] = _nota
for _f_ in range(7, 26):
    CELDA_PISTAS.setdefault(('WEDP', _I, 'D%d' % _f_), 'D162: nota de la partida del ejemplo US (rótulo fijado de la col. A '
                                                       'en "fijos_en"); sin marcas ni normas españolas: solo rangos con '
                                                       'fuente leída o «get local quotes»')
# Tabla D19 (Instrucciones 35-48): «US WEDDING VENUE BENCHMARKS (sourced) AND KIT ESTIMATES» (Benchmark | Value | Source |
# Note). D165 + decisión de orquestador 4: solo lo «leída» lleva fuente; lo «(resumen)» = «Kit estimate» o «ask…». Filas
# alineadas con el tema ES (A41 «Canon del catering exclusivo» es FIJO: «Caterer commission (exclusive caterer)»); la de
# «comida testigo» (46) pasa a «Venue rental fee»
_D19 = OrderedDict([
    (35, 'D165 fila → «Month 1 of the plan» · «March» · «Plan decision» · nota: el permiso y la obra se cierran en el '
         'invierno anterior; picos octubre, septiembre y junio; valle enero'),
    (36, 'D165 fila → «Event mix of the plan» · «100 events: 35 weddings, 25 corporate, 30 private celebrations, 10 micro '
         'weddings» · «Kit estimate» · nota: weddings 130 guests × ($9,000 site fee + 10% of $110 F&B per guest), corporate '
         '70 × ($3,500 + 10% of $50), private 80 × ($4,000 + 10% of $55), micro 30 × ($2,000 + 10% of $80), excl. sales tax'),
    (37, 'D165 fila → «Saturday ceiling» · «about 30-35 prime Saturdays a year» · «Kit estimate» · nota: las 35 bodas no '
         'caben todas en sábados de temporada: viernes, domingos y fuera de temporada a menor tarifa; el libro no comprueba '
         'este techo'),
    (38, 'D165 fila (sustituye «Bodas en España») → «Guests per wedding» · «about 100-150 at a barn venue» · «Kit '
         'estimate; national wedding studies publish yearly averages: check the latest» · nota: el caso usa 130 por boda '
         'y 90 de media con los demás eventos (decisión de orquestador 4: sin cifras de The Knot)'),
    (39, 'D165 fila → «Booking lead time» · «12-18 months for weddings» · «Kit estimate» · nota: la primera temporada se '
         'reserva antes de abrir, solo con holds contingentes al CUP y al certificate of occupancy; la rampa del plan dura '
         '12 meses'),
    (40, 'D165 fila → «Direct cost per event» · «$1,000 wedding · $500 corporate · $500 private · $300 micro» · «Kit '
         'estimate» · nota: limpieza, restrooms, generator fuel, parking attendants y security; camareros y cocina son del '
         'caterer'),
    (41, 'D165 fila → «Caterer commission» · «about 10% of the caterer\'s food & beverage sales at the venue» · «Kit '
         'assumption (no public benchmark)» · nota: neta de sales tax, service charge y gratuities; negocia el tuyo; '
         'liquidación mensual con derecho de auditoría'),
    (42, 'D165 fila → «Venue staff per event» · «coordinator + 1-2 attendants» · «Kit estimate» · nota: boda 2 attendants, '
         'el resto 1; servers y bartenders los pone el caterer'),
    (43, 'D165 fila (sustituye «IVA») → «Sales tax on venue charges» · «varies by state (8% example on venue rental & '
         'services; 0% on the caterer commission)» · «Your state\'s department of revenue» · nota: algunos estados gravan '
         'el site fee y otros no, a veces solo si va con catering: confírmalo antes de fijar tarifas'),
    (44, 'D165 fila (sustituye «autoprotección») → «Fire sprinklers in an assembly (A-2) venue» · «required above an '
         'occupant-load or fire-area threshold» · «IBC 903.2.1.2, as adopted by your state or county» · nota: «editions '
         'and local amendments vary: ask the building official and the fire marshal in writing» (sin cifras de umbral '
         'hasta la revisión D174)'),
    (45, 'D165 fila (sustituye «ruido RD 1367/2007») → «Noise and music curfew» · «set by your county ordinance and the '
         'conditions of your CUP» · «Your county zoning office» · nota: decibel limit, sound meter, baile final dentro, '
         'altavoces de espaldas a los vecinos'),
    (46, 'D165 fila → «Venue rental fee (peak Saturday)» · «roughly $3,500-$10,000 in published rate cards» · «Kit '
         'estimate from published venue rate cards (2026): get local quotes» · nota: viernes/domingo ≈ −15 %, entre '
         'semana ≈ −30 %, off-peak ≈ −20 % (calculadora del kit)'),
    (47, 'D165 fila (sustituye «agua de pozo RD 3/2023») → «Well water» · «a well that serves your guests may count as a '
         'public water system» · «Ask your state drinking water program» · nota: análisis y permiso antes del primer '
         'evento (sin citar 40 CFR 141.2 hasta la revisión D174)'),
    (48, 'D165 fila (sustituye «convenio») → «Minimum wage» · «federal $7.25/h + your state» · «U.S. Department of Labor '
         '(dol.gov)» · nota: el plan presupuesta ≥ $17/h para los attendants; teclea el suelo de tu estado en '
         '"0. Assumptions"'),
])
for _f_, _p in _D19.items():
    for _col in 'ABCD':
        CELDA_PISTAS[('WEDP', _N, '%s%d' % (_col, _f_))] = _p
# Checklist (D169 + decisiones de orquestador 1 y 2): la tarea US de cada fila (sin mover filas: tarea equivalente)
_CHK = OrderedDict([
    ('F1 - Constitución', [
        'LLC vs S corp: elige la forma con tu CPA (el plan tributa como sociedad: income tax en "0. Assumptions")',
        'Form the LLC ANTES de firmar el lease: el lease, la solicitud del CUP y los permisos van a su nombre',
        'EIN (IRS) y registro estatal de la LLC',
        'State payroll / unemployment (UI) accounts y cómo cobra el dueño (draw vs salary) según la elección fiscal: CPA',
        'Business license y sales tax permit: pregunta si tu venue rental fee tributa en tu estado',
        'Business bank account: retainers, caterer commission y rent separados de lo personal',
        'Bookkeeping + venue management software que siga retainers, pagos programados y la comisión del caterer',
        'Calendario de sales tax de tu estado (mensual / trimestral / anual) y tratamiento del site fee y de la comisión',
        'Estimated taxes y plan del owner\'s draw con tu CPA',
        'Lender package: plan + 2 cotizaciones SBA 7(a); el lease, CONTANDO LAS PRÓRROGAS, debe durar al menos lo que el '
        'préstamo («SBA lenders typically require…; confirm with your lender»)',
        'USPTO trademark search del nombre del venue',
        'Website privacy policy & terms (y consentimiento para fotos de eventos)',
    ]),
    ('F2 - Finca y licencia', [
        'ZONING CHECK BEFORE SIGNING: pregunta POR ESCRITO al planning office del condado si un wedding / event venue se '
        'permite en esa parcela y con qué permiso (CUP / SUP)',
        'Elegir una propiedad con un granero o edificio existente, a 30-60 min de la ciudad',
        'Agua, electricidad y fosa séptica: un ingeniero comprueba la capacidad de la septic y el pozo (¿public water '
        'system?) antes de firmar',
        'Negociar el lease: duración CONTANDO LAS PRÓRROGAS ≥ plazo del préstamo («SBA lenders typically require…; '
        'confirm with your lender»)',
        'Lease contingent on CUP approval (y certificate of occupancy): si no llega, sales sin penalización',
        'Purchase option o right of first refusal, consentimiento del propietario a la obra y a usar el lease como '
        'garantía del préstamo, y negociar una TI allowance',
        'Solicitar el conditional / special use permit: audiencia pública; condiciones (tope de eventos, horario, '
        'tráfico, ruido)',
        'Change of occupancy a assembly (Group A-2): building permit → certificate of occupancy',
        'Pregunta POR ESCRITO al building official y al fire marshal: occupant load, sprinklers, salidas, aseos y carpas',
        'Ninguna fecha firme sin CUP y certificate of occupancy: solo holds contingentes con devolución íntegra',
        'ADA Title III: rutas accesibles, aseos y parking en los planos (2010 ADA Standards)',
        'Occupant load rotulada, salidas, emergency lighting y plan de evacuación',
        'Ruido: ordenanza del condado, decibel limit y sound meter',
        'Música exterior y curfew según las condiciones del CUP',
        'Seguros: general liability, host liquor liability, property y umbrella (cotizaciones de un agente de venues)',
        'Pozo: si sirve a tus invitados, pregunta a tu state drinking water program (análisis y permiso)',
    ]),
    ('F3 - Obra y equipamiento', [
        'Tres presupuestos sobre los planos del architect / code consultant',
        'Building permit antes de empezar la obra',
        'Barn renovation: suelo, puertas, aislamiento, acabados',
        'Fire sprinkler y alarm system con la aprobación del fire marshal',
        'ADA-compliant restrooms (y la ampliación de la septic si hace falta)',
        'Electrical service, exit y emergency lighting, con inspección',
        'Standby generator',
        'HVAC del salón',
        'Prep & warming kitchen del caterer con agua y desagüe (health plan review si tu condado lo exige)',
        'Pérgola y tent platform (permiso de carpas según el fire code local)',
        '200 sillas, mesas, mantelería base y bridal suite',
        'Sound system y decibel meter',
        'Parking de grava, driveway, señalización e iluminación (plazas ADA)',
        'Landscaping, ceremony site y riego',
        'Inspecciones finales y certificate of occupancy',
    ]),
    ('F4 - Personal y catering', [
        'Contratar al venue coordinator como seasonal W-2 (offer letter, I-9, W-4)',
        'Event attendants como seasonal part-time W-2 (nunca 1099 si el venue dirige su trabajo)',
        'Facilities & grounds, weekend sales y housekeeping: salario mínimo estatal y workers\' comp',
        'Workers\' comp y new-hire reporting del estado antes de cada temporada',
        'Time records y overtime (FLSA)',
        'Seguridad básica: OSHA, primeros auxilios, escaleras y cargas',
        'Shortlist de 1-2 caterers + tasting',
        'Exclusive caterer agreement (comisión, derecho de auditoría, mínimo anual opcional)',
        'Commission statement mensual y derecho de auditoría',
        '(La «comida testigo» NO cruza) → Caterer\'s food safety plan y contacto para incidencias',
        'Alérgenos: el caterer gestiona por escrito los 9 major allergens de cada menú',
        'Licencia y health permit del caterer, su liquor license / permit y su COI con el venue como additional insured',
        'Preferred vendor list con los COI de cada proveedor',
    ]),
    ('F5 - Marca y reservas', [
        'Nombre, logo e identidad del venue',
        'Web con disponibilidad, galería y reserva de venue tours',
        'Styled shoot: fotos y vídeo profesionales del venue montado',
        'Google Business Profile y primeras reseñas',
        'The Knot / WeddingWire storefronts: mide el cost per lead',
        'Redes sociales con bodas y eventos reales',
        'Bridal shows',
        'Open house con el caterer',
        'Wedding planners y agencias de eventos',
        'Empresas y celebraciones privadas (showers, quinceañeras, cumpleaños, rehearsal dinners)',
        'Tarifas por temporada (peak / shoulder / off-peak) y día con la calculadora del kit',
        'Pricing guide / wedding brochure y dossier de empresa',
        'Venue rental agreement con retainer y tabla de cancelación revisado por un abogado de tu estado',
        'Venue management software y calendario de fechas',
    ]),
    ('F6 - Temporada y eventos', [
        'Venue tour y presupuesto por escrito',
        'Contrato firmado, retainer y recibo',
        'Firmas en una bridal show o fuera del venue: «ask your attorney whether the FTC Cooling-Off Rule or your '
        'state\'s home-solicitation law applies; many venues give a short cancellation window for show-floor signings '
        'anyway» (decisión de orquestador 2: NO afirmar que aplica)',
        'Governing law clause revisada por tu abogado',
        'Tasting con el caterer',
        'Final headcount y alergias',
        'Rain plan (calor y alertas de incendio)',
        'Setup y control de la occupancy',
        'Curfew y decibel limit',
        '(La «comida testigo» NO cruza) → Walkthrough antes de que lleguen los invitados: salidas despejadas, restrooms, '
        'COIs de los vendors del día',
        'Load-out, limpieza y revisión de daños (security deposit, deducciones detalladas)',
        'Commission statement mensual del caterer',
        'Reseña, fotos y agradecimiento',
        'Cierre trimestral: ocupación, comisión y caja',
    ]),
])
for _h, _tareas in _CHK.items():
    for _k, _t in enumerate(_tareas):
        for _col in 'BE':
            CELDA_PISTAS[('WEDC', _h, '%s%d' % (_col, 5 + _k))] = 'D169 tarea US: ' + _t
# tareas cuyo ES es un rótulo de la inversión (FIJO: el EN ya es la tarea US) y notas de Supuestos que son GM (motor)
for _k in [('WEDC', 'F3 - Obra y equipamiento', 'B%d' % _f_) for _f_ in (8, 11, 12, 16)] + \
        [('WEDP', _S, _c) for _c in ('A2', 'C20', 'C21', 'C22')] + [('WEDP', _N, 'A41')]:
    CELDA_PISTAS.pop(_k, None)

# Pistas por TEXTO propias de la finca (se suman a las de extraer_textos.PISTAS): glosario research §9
PISTAS_EXTRA = [
    (r'desplegable', 'DV de la columna OK: en el EN la lista es «✓, ☐, N/A» (CLAVES[\'—\'] = \'☐\'): escribe «☐ = pending», '
                     'NUNCA «—» (la Pizza EN publicada lo dejó con «—»: F2-NOTAS §5)'),
    (r'[Ii]nvitad', 'Glosario §9: guests · guest count · final headcount (nunca covers ni customers)'),
    (r'[Ee]ventos', 'Glosario §9: events per year · events of the average size'),
    (r'[Cc]anon', 'Glosario §9: caterer commission (% of the caterer\'s F&B sales), nunca «canon» ni «royalty»'),
    (r'[Ff]inca', 'Glosario §9: venue (el negocio) / property (el inmueble); nunca «finca», «estate» ni «farm» como nombre'),
    (r'[Cc]atering', 'Glosario §9: exclusive caterer · preferred vendor list · in-house catering'),
    (r'[Ss]e[ñn]al|[Rr]eserva', 'Glosario §9: retainer (aplicado al precio) · booking; «non-refundable» solo con la tabla '
                                'de cancelación'),
    (r'[Ff]ianza', 'Glosario §9: security deposit / damage deposit (refundable, itemized) — en la inversión: lease '
                   'security deposit'),
    (r'fij[oa]s? discontinu', 'Glosario §9: seasonal employee (W-2)'),
    (r'[Ll]icencia|[Cc]alificaci|[Uu]rban', 'Glosario §9: zoning approval: conditional (special) use permit + certificate '
                                            'of occupancy (Group A-2)'),
    (r'[Aa]foro|[Aa]utoprotecci|[Ee]vacuaci|[Ii]ncendio', 'Glosario §9: maximum occupancy / occupant load (fire marshal) '
                                                          '· sprinklers · egress'),
    (r'[Ww]edding planner|[Aa]gencia', 'Glosario §9: planners and venue marketplaces (Peerspace); The Knot / WeddingWire '
                                       'son storefronts (coste fijo)'),
    (r'[Cc]omida testigo', 'D169: NO cruza (no es norma US): elimínala o sustitúyela por el food safety plan del caterer'),
    (r'[Aa]l[eé]rgen', 'Glosario §9: 9 major allergens (los gestiona el caterer)'),
    (r'[Pp]ozo|[Aa]gua', 'Glosario §9: well (¿public water system?: ask your state drinking water program)'),
    (r'[Ll]imitador|[Rr]uido', 'Glosario §9: decibel limit / sound meter, music curfew (county ordinance + CUP)'),
    (r'\bSL\b|aut[oó]nomo', 'Glosario §9 (e): LLC'),
    (r'[Gg]estor', 'Glosario §9 (e): CPA / bookkeeper'),
    (r'[Aa]yuntamiento|[Cc]omunidad', 'Glosario §9 (e): county / state'),
    (r'IVA', 'Glosario §9 (e): sales tax (el venue: site fee al tipo de ejemplo; la comisión, 0 %)'),
    (r'SGAE|AGEDI', 'Glosario §9 (e): ASCAP/BMI/SESAC'),
    (r'[Cc]arpa|[Pp][ée]rgola', 'Glosario §9: tent / pergola / ceremony site'),
    (r'[Aa]seos', 'Glosario §9: ADA-compliant restrooms'),
    (r'[Gg]rupo electr', 'Glosario §9: standby generator'),
    (r'\b[Oo]ffice\b', 'Glosario §9: caterer\'s prep & warming kitchen'),
    (r'[Tt]emporada', 'Glosario §9: peak / shoulder / off-peak (off-season)'),
    (r'[Pp]rueba de men', 'Glosario §9: tasting'),
    (r'[Pp]uertas abiertas|[Ff]eria', 'Glosario §9: open house · bridal show'),
    (r'[Pp]ortal|[Ee]scaparate', 'Glosario §9: The Knot / WeddingWire storefront (listing)'),
    (r'[Pp]reboda|[íi]ntima', 'Glosario §9: rehearsal · micro wedding / elopement · rehearsal dinner'),
    (r'[Cc]oordinaci', 'Glosario §9: venue coordinator (del venue) ≠ day-of coordinator (de la pareja)'),
    (r'[Mm]ontaje|[Rr]ecogida', 'Glosario §9: setup / teardown (breakdown) · load-in / load-out'),
    (r'[Ll]luvia', 'Glosario §9: rain plan / inclement-weather plan'),
    (r'[Dd]esistimiento|[Ff]uero', 'Decisión de orquestador 2: «ask your attorney whether the FTC Cooling-Off Rule or '
                                   'your state\'s home-solicitation law applies…» (NO afirmar que aplica); governing law '
                                   'clause revisada por un abogado'),
]

# Glosario de la finca (research §9, OBLIGATORIO; manda sobre el de FT/CAF y el de la pizza)
GLOSARIO_WED = OrderedDict([
    ('finca de eventos', 'wedding venue / event venue (tipos: barn venue, estate venue, farm venue, banquet hall)'),
    ('alquiler del espacio', 'venue rental fee / site fee (+ «venue fee» si es % de F&B)'),
    ('catering exclusivo · homologados', 'exclusive caterer · preferred vendor list · in-house catering'),
    ('canon del catering', 'caterer commission (% of F&B) / exclusivity fee (nunca «canon» ni «royalty»)'),
    ('invitados · recuento final', 'guests · guest count · final headcount (due X days before)'),
    ('mínimo garantizado', 'guaranteed guest count · food & beverage minimum (del caterer)'),
    ('señal / reserva', 'retainer (aplicado al precio) · booking deposit; «non-refundable» solo con la tabla de cancelación'),
    ('fianza por daños', 'security deposit / damage deposit (refundable, itemized)'),
    ('barra libre · resopón', 'open bar / hosted bar (del caterer) · late-night snack'),
    ('coordinación del día', 'venue coordinator (del venue) ≠ day-of coordinator (de la pareja)'),
    ('montaje y recogida', 'setup / teardown (breakdown) · load-in / load-out'),
    ('plan B de lluvia', 'rain plan / inclement-weather plan (tent backup)'),
    ('aforo', 'maximum occupancy / occupant load (lo fija el fire marshal)'),
    ('calificación urbanística / licencia de actividad', 'zoning approval: conditional (special) use permit · certificate '
                                                          'of occupancy (assembly, Group A-2)'),
    ('prueba de menú', 'tasting'),
    ('visitas · jornada de puertas abiertas', 'venue tours / site visits · open house'),
    ('temporada alta / media / baja', 'peak / shoulder / off-peak (off-season)'),
    ('preboda · boda íntima · cena de la víspera', 'rehearsal · micro wedding / elopement · rehearsal dinner'),
    ('suite de novios', 'bridal suite · groom\'s lounge'),
    ('proveedores externos', 'outside vendors · outside catering fee · cake-cutting fee · corkage fee'),
    ('portales de bodas', 'The Knot / WeddingWire storefront (listing) · venue marketplaces (Peerspace)'),
    ('seguro RC · certificado', 'general liability · host liquor liability · event insurance · COI / additional insured'),
    ('fijo discontinuo', 'seasonal employee (W-2)'),
    ('grupo electrógeno · limitador', 'standby generator · decibel limit / sound meter, music curfew'),
    ('aseos adaptados · saneamiento · pozo', 'ADA-compliant restrooms · septic system · well (public water system)'),
    ('software de reservas', 'venue management software (Tripleseat, Perfect Venue, HoneyBook)'),
    ('invitado / ticket / días', 'guests · revenue per guest · events per year (nunca «covers» ni «average check»)'),
    ('dossier', 'wedding brochure / pricing guide'),
    ('(e) finca', 'venue (o «property» para el inmueble)'), ('(e) canon', 'caterer commission'),
    ('(e) IVA', 'sales tax'), ('(e) calificación urbanística/licencia', 'CUP + certificate of occupancy'),
    ('(e) autoprotección', 'fire code, occupant load, sprinklers'), ('(e) comida testigo', 'no aplica (eliminar)'),
    ('(e) 14 alérgenos', '9 major allergens (caterer)'), ('(e) fijos discontinuos', 'seasonal W-2'),
    ('(e) TRLGDCU / fuero del consumidor', 'state consumer law; governing law & venue clause'),
    ('(e) arras / señal', 'retainer'), ('(e) SL / autónomo', 'LLC'), ('(e) gestoría', 'CPA / bookkeeper'),
    ('(e) ayuntamiento / comunidad', 'county / state'), ('(e) SGAE', 'ASCAP/BMI/SESAC'),
    ('(e) ceremonia civil (Ley 15/2015)', 'el venue acoge; licencia (county clerk) y officiant según el estado'),
])


# ==========================================================================
# Caso de ejemplo US (D160, D162, D163, D165, D167; research §8): celdas VERDES. (corto, hoja ES, celda) → (valor, rótulo)
# ==========================================================================
def valores_wed(M):
    v = OrderedDict()
    sup = [
        ('B4', 90, 'Invitados por evento'), ('B5', 68, 'Precio medio por invitado'), ('B6', 100, 'Eventos al año'),
        ('B7', 0.08, 'Crecimiento de volumen del año 2'), ('B8', 0.05, 'Crecimiento de volumen del año 3'),
        ('B11', 0.88, 'Ventas de ESPACIO Y SERVICIOS'), ('B13', 0.12, 'Coste directo del evento sobre'),
        ('B14', 0, 'Coste del canon sobre'), ('B15', 0.015, 'Consumibles'),
        ('B16', 0.10, 'Ventas que llegan por wedding planners'), ('B17', 0.15, 'Comisión de los wedding planners'),
        ('B18', 0.02, 'Comisión de los medios de pago'), ('B20', 0.10, 'Seguridad Social'),
        ('B21', 12, 'Número de pagas'), ('B22', 15080, 'SMI anual'), ('B24', 5000, 'Renta mensual de la finca'),
        ('B25', 2, 'Fianza del arrendamiento'), ('B26', 2000, 'Suministros mensuales'), ('B27', 12000, 'Seguros'),
        ('B28', 0.01, 'Varios'), ('B30', 200000, 'Recursos propios'), ('B31', M.CALIBRAR, 'Préstamo bancario'),
        ('B32', 0.10, 'Tipo de interés'), ('B33', 10, 'Plazo del préstamo'), ('B34', 0, 'Carencia'),
        ('B35', 3, 'Fondo de maniobra'),
        ('B37', 0.25, 'Impuesto de Sociedades, nueva'), ('B38', 0.25, 'Impuesto de Sociedades, tipo'),
        ('B39', 0.08, 'IVA repercutido de restauración'), ('B40', 0.08, 'IVA repercutido/soportado'),
        ('B41', 0, 'IVA soportado en compras'), ('B42', 0, 'Bases negativas'),
        ('B44', 15, 'Vida útil de obra'), ('B45', 7, 'Vida útil de maquinaria'),
        ('B48', 0, 'Subida anual de los costes fijos'),
        ('B51', 200, 'Aforo de la finca'), ('B52', 0.45, 'Actividad del mes 1'), ('B53', 12, 'Meses hasta alcanzar'),
        ('B54', 4, 'Meses de renta ANTES'), ('B55', 0.10, 'Imprevistos sobre las partidas de OBRA'),
        ('B58', 10, 'Días medios de cobro'), ('B59', 14, 'Días medios de pago'),
        ('B62', 0, 'Bebida ALCOHÓLICA'), ('B63', 0.08, 'IVA de la bebida ALCOHÓLICA'),
        ('B65', 1.15, 'DSCR mínimo'), ('B66', 1.25, 'DSCR objetivo'), ('B67', 0.15, 'Holgura mínima'),
        ('B68', None, 'Suelo salarial anual'),
    ]
    for c, val, rot in sup:
        v[('WEDP', _S, c)] = (val, rot)
    # Inversión (D162): las 19 partidas, filas 7-25 = $503,500 (obra $370,000 · equipo $97,000 · no amortizable $36,500);
    # los imprevistos (B28) van por fórmula (B55 × obra)
    for k, val in enumerate([25000, 15000, 80000, 70000, 25000, 45000, 30000, 15000, 30000, 25000, 30000, 15000, 12000,
                             35000, 15000, 15000, 8000, 3500, 10000]):
        v[('WEDP', _I, 'B%d' % (7 + k))] = (val, None)
    # P&L (D163, D164, D165): fijos B26-B35 ($62,000); G10 (venue rental & services) 8 %, G11 (comisión) 0, G13 (IVA
    # soportado: valor en el ES) → 0; umbrales del semáforo E51, E53-E56
    for k, val in enumerate([18000, 5000, 10000, 7000, 5000, 3600, 600, 6000, 2800, 4000]):
        v[('WEDP', _P, 'B%d' % (26 + k))] = (val, None)
    v[('WEDP', _P, 'G10')] = (0.08, None)
    v[('WEDP', _P, 'G11')] = (0, None)
    v[('WEDP', _P, 'G13')] = (0, None)
    for c, val, rot in [('E51', 0.85, 'Margen bruto'), ('E53', 0.15, 'Coste directo del evento /'),
                        ('E54', 0.35, 'Coste de personal'), ('E55', 0.12, 'Renta de la finca'),
                        ('E56', 0.05, 'Resultado neto')]:
        v[('WEDP', _P, c)] = (val, rot)
    # Staffing (D163): personas (B), FTE por persona (C), bruto mes TOTAL de la fila (D); ≥ suelo, 12 pagas. Cobertura
    # B18-B23 = ES (se recalcula con E4)
    for f, (b, c, d) in zip(range(5, 11), [(1, 1.0, 4500), (1, 0.75, 3380), (1, 0.8, 3050), (2, 0.35, 2062),
                                           (1, 0.2, 763), (1, 0.25, 780)]):
        for col, val in zip('BCD', (b, c, d)):
            v[('WEDP', _R, '%s%d' % (col, f))] = (val, None)
    v.update([(('WEDP', _R, 'B13'), (8000, 'Coste anual')), (('WEDP', _R, 'B14'), (8000, 'Coste anual'))])
    # Escenarios (D160): pesimista 85 · $60 · 85 / optimista 95 · $72 · 115
    v.update([
        (('WEDP', _ES, 'B5'), (85, 'Invitados por evento')), (('WEDP', _ES, 'D5'), (95, 'Invitados por evento')),
        (('WEDP', _ES, 'B6'), (60, 'Precio medio por invitado')), (('WEDP', _ES, 'D6'), (72, 'Precio medio por invitado')),
        (('WEDP', _ES, 'B7'), (85, 'Eventos al año')), (('WEDP', _ES, 'D7'), (115, 'Eventos al año')),
    ])
    # Tesorería (D167): Mes 1 = marzo con los pesos US de research §8 (picos oct-sep-jun)
    pesos = [0.050, 0.075, 0.105, 0.120, 0.080, 0.085, 0.130, 0.145, 0.070, 0.060, 0.035, 0.045]
    assert abs(sum(pesos) - 1) < 1e-9
    for col, p in zip('BCDEFGHIJKLM', pesos):
        v[('WEDP', _T, '%s5' % col)] = (p, None)
    return v


# Calibración D15 (D160: palancas en su orden; máx. 3 vueltas). Cada celda, citada en F2-NOTAS.md (G7)
CALIBRACION_D15 = OrderedDict()


def formulas_wed():
    p = os.path.join(AQUI, 'formulas_wed.json')
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
    M.TOKENS_DOCX = tokens_wed(M.TOKENS_DOCX)
    M.PRODUCTOS_CIERRE = PRODUCTOS_CIERRE_WED
    M.DOCX_FIJOS = docx_fijos(M)
    M.DOCX_NOTAS = DOCX_NOTAS
    M.DOCX_NOTAS_PLAN = DOCX_NOTAS_PLAN
    M.FORMULAS_EN = formulas_wed()
    M.VALORES_EN = valores_wed(M)
    M.CALIBRACION_D15 = CALIBRACION_D15
    M.CELDA_PISTAS = CELDA_PISTAS
    M.PISTAS_EXTRA = PISTAS_EXTRA
    M.CIFRAS_PROHIBIDAS = cifras_prohibidas(M.VALORES_EN)
    M.RX_WED_NO = RX_WED_NO
    M.REGLA_UNIDADES = REGLA_UNIDADES
    glo = OrderedDict(M.GLOSARIO)
    for k, val in GLOSARIO_WED.items():
        glo[k] = val                          # research §9 manda (regla de jerga §0)
    M.GLOSARIO = glo
