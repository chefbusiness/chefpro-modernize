#!/usr/bin/env python3
"""
datos_bbq.py — BBQ Catering Business Plan Kit (EN) · los datos ES→EN que dependen del contenido: rótulos fijados
(D102-D103), POR_CELDA, pistas (D18/D19, notas del caso, las 68 tareas del checklist D107), tokens del docx (D108), fijos
y notas del docx, caso US (D100; research §8), FORMULAS_EN, cifras prohibidas y vocabulario vetado RX_BBQ_NO (D110) y
glosario de research §9 (regla de jerga §0). Lo llama `mapas_bbq.instalar()` con el módulo `mapas` YA cargado con los
datos de FT/CAF (motor 2.2), de los que parte. La fuente ES del circuito es el FOOD TRUCK ES: los rótulos ES de abajo son
los del FT; el EN de partida de cada celda es el del CATERING publicado (mapas_bbq.CAT_CELDA). Estructura de
`../business-plans-en-5/datos_mbar.py`; contenido de comida de `../business-plans-en-4/datos_cat.py` (D101).
Sesión Claude Code, 24-oct-2026 (F2, paso 1).
"""
import json
import os
import sys
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
BP = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
CAT = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')
MBAR = os.path.join(os.path.dirname(AQUI), 'business-plans-en-5')
PAR = os.path.join(os.path.dirname(AQUI), 'parrillero-2_2')

URL_BBQ = 'aichef.pro/en/digital-products/bbq-catering-business-plan'
_I, _S, _P, _R, _N, _E, _ES, _T = ('Inversión Inicial', '0. Supuestos', 'PyG 3 Años', 'Personal', 'Instrucciones',
                                   'Punto Equilibrio', 'Escenarios', 'Tesorería 12 meses')
# Medidas (John, 13-oct; SPEC §0): sistema US como principal y la métrica entre paréntesis; temperaturas de calidad y de
# seguridad, siempre distinguidas
REGLA_UNIDADES = ('MEDIDAS US (John, 13-oct; SPEC §0): principales lb y oz, °F, miles, gallons / quarts y sq ft; la '
                  'métrica entre paréntesis para UK y Australia: «12 lb (5.4 kg)», «225 °F (107 °C)», «5 gallons (19 '
                  'liters)», «200 sq ft (19 sq m)» (el gate común no admite «m²»); nada de kg, km, litros ni °C como '
                  'unidad principal (gate). TEMPERATURAS: la de CALIDAD (brisket ≈ 203 °F, Kit estimate) y el MÍNIMO '
                  'SEGURO del FDA Food Code (145 / 155 / 165 °F, hot holding 135 °F) nunca en la misma columna ni en la '
                  'misma frase sin decir cuál es cuál')

# ==========================================================================
# FIJOS (por TEXTO ES del FT: valen en cualquier celda de los 2 libros) y POR_CELDA (solo esa celda)
# ==========================================================================
FIJOS_FUERA = ('Este fichero forma parte del producto «plan-negocio-cafeteria» de AI Chef Pro.',)
_TITULO_CHECK = 'BBQ CATERING STARTUP CHECKLIST — OFF-SITE BBQ CATERER'
FIJOS_NUEVOS = OrderedDict([
    ('Este fichero forma parte del producto «plan-negocio-food-truck» de AI Chef Pro.',
     'This file is part of the BBQ Catering Business Plan Kit by AI Chef Pro.'),
    # D107: título del checklist y de la fase 2 (el título de hoja no tiene el límite de 31 de la pestaña)
    ('CHECKLIST APERTURA — FOOD TRUCK', _TITULO_CHECK),
    ('FASE 2: VEHÍCULO Y PERMISOS', 'PHASE 2: COMMISSARY, SMOKER TRAILER, FIRE RULES & PERMITS'),
    ('INSTRUCCIONES DE USO — Plan financiero Food Truck', 'HOW TO USE THIS WORKBOOK — BBQ Catering Financial Projections'),
    ('PLAN DE NEGOCIO: FOOD TRUCK', 'BUSINESS PLAN: BBQ CATERING COMPANY'),
    ('Ajusta las cifras a tu proyecto.', 'US kit example (2026) — replace with your own quotes.'),
    ('Escenario realista — Food Truck urbano', 'Base case — BBQ caterer (smoked meats, off-site)'),
    ('Break-even — Food Truck', 'Break-even — BBQ Catering'),
    # D104: cabecera de la tabla D19
    ('DATOS DE REFERENCIA DEL SECTOR', 'US BBQ CATERING BENCHMARKS (sourced) AND KIT ESTIMATES'),
    # motor de eventos (B4 = eventos/año, B5 = precio por invitado, B6 = invitados por evento) en todas las hojas
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
    # D103: el canal de «delivery» del FT son los marketplaces de catering corporativo (B16/B17)
    ('Comisiones de delivery', 'Corporate catering marketplace fees'),
    # no hay «to go»: alcohol solo si algún día vendes con licencia (0 % en el caso)
    ('IVA repercutido/soportado general', 'Sales tax rate on alcohol sold (licensed only)'),
    # D103: las dos líneas de venta adoptadas y su coste (los mismos textos ES salen en el P&L y en Escenarios)
    ('Coste de mercancía — comida', 'Cost of goods — BBQ packages (meat, sides, bread & sauces)'),
    ('Coste de mercancía — bebida', 'Cost of goods — add-ons'),
    ('Consumibles y envases', 'Disposables, wood & cooking fuel'),
])

POR_CELDA = OrderedDict([
    # 0. Supuestos (D100, D103): mezcla de ventas, canal, commissary
    (('BBQP', _S, 'A11'), 'BBQ PACKAGES share of sales (smoked meats, sides, bread & sauces, staffing)'),
    (('BBQP', _S, 'A12'), 'ADD-ONS share of sales (live pit on site, desserts, appetizers, non-alcoholic drinks, rentals, '
                          'travel fees)'),
    (('BBQP', _S, 'A13'), 'Cost of goods on BBQ PACKAGE sales (raw meat, sides, bread, sauces)'),
    (('BBQP', _S, 'A14'), 'Cost of goods on ADD-ON sales'),
    (('BBQP', _S, 'A15'), 'Disposables, wood & cooking fuel as % of sales'),
    (('BBQP', _S, 'A16'), 'Corporate catering marketplace share of sales (e.g. ezCater)'),
    (('BBQP', _S, 'A17'), 'Marketplace commission on those sales'),
    (('BBQP', _S, 'A23'), 'COMMISSARY KITCHEN, TRAILER PARKING AND FIXED COSTS'),
    (('BBQP', _S, 'A24'), 'Commissary kitchen rent & smoker trailer parking, per month'),
    (('BBQP', _S, 'A25'), 'Commissary deposit (months)'),
    (('BBQP', _S, 'A26'), 'Monthly utilities (water, power and phone not covered by the commissary)'),
    (('BBQP', _S, 'A44'), 'Useful life of the smoker trailer, van and fit-outs (years)'),
    (('BBQP', _S, 'A45'), 'Useful life of the live-fire rig, holding equipment, pit tools and software (years)'),
    (('BBQP', _S, 'A51'), 'Max events a year your pit and crew can handle'),
    (('BBQP', _S, 'A54'), 'Months of commissary rent BEFORE opening'),
    (('BBQP', _S, 'A55'), 'Contingency on the trailer, van and fit-out lines (%)'),
    (('BBQP', _S, 'A62'), 'ALCOHOL as a share of add-on sales (0%: no liquor license; the client supplies any alcohol)'),
    # Startup Costs filas 7-23 y base de amortización (D102: orden del inventario §3; solo se mueven filas)
    (('BBQP', _I, 'A7'), 'Smoker trailer (offset / reverse-flow, 500-gal class, new)'),
    (('BBQP', _I, 'A8'), 'Smoker trailer upfit (warming cabinet, hand sink + water tanks if your county requires, '
                         'storage boxes, lights)'),
    (('BBQP', _I, 'A9'), 'Live-fire rig (Santa Maria grill, Argentine parrilla, asado crosses, La Caja China)'),
    (('BBQP', _I, 'A10'), 'Commissary storage fit-out (racks, meat lugs, vacuum sealer)'),
    (('BBQP', _I, 'A11'), 'Used cargo van'),
    (('BBQP', _I, 'A12'), 'Van upfit (shelving, racks, tie-downs, wrap)'),
    (('BBQP', _I, 'A13'), 'LLC formation, contracts and legal'),
    (('BBQP', _I, 'A14'), 'First-year permits and certifications (catering / health permit, MFU or temporary event '
                          'permits, fire inspection, ServSafe Manager)'),
    (('BBQP', _I, 'A15'), 'Plan review / trailer inspection (only if your county requires it)'),
    (('BBQP', _I, 'A16'), 'Catering software, card reader and tablet'),
    (('BBQP', _I, 'A17'), 'Smallwares & pit tools (knives, hotel pans, probe thermometers, butcher paper)'),
    (('BBQP', _I, 'A18'), 'Opening inventory (meat for test cooks, rubs, sauces, wood, disposables)'),
    (('BBQP', _I, 'A19'), 'Website, photos, launch and first bridal show'),
    (('BBQP', _I, 'A20'), 'Holding & service equipment (insulated food carriers, hot boxes, chafing dishes, coolers, '
                          'canopy, carving board)'),
    (('BBQP', _I, 'A21'), 'Commissary deposit'),
    (('BBQP', _I, 'A22'), 'Commissary rent before opening'),
    (('BBQP', _I, 'A23'), 'Smoker trailer, van and fit-out contingency'),
    (('BBQP', _I, 'A31'), 'Smoker trailer, van and fit-outs (depreciated over the vehicle life)'),
    # 3-Year P&L (D103; research §8: fijos B26-B35 = 30,300)
    (('BBQP', _P, 'A10'), 'BBQ package sales (smoked meats, sides, bread & sauces, staffing)'),
    (('BBQP', _P, 'A11'), 'Add-on sales (live pit on site, desserts, appetizers, drinks, rentals, travel fees)'),
    (('BBQP', _P, 'A22'), 'Commissary kitchen rent & smoker trailer parking'),
    (('BBQP', _P, 'A24'), 'Utilities (water, power and phone not covered by the commissary)'),
    (('BBQP', _P, 'A25'), 'Insurance (general liability, commercial auto with the trailer, workers\' comp, inland marine)'),
    (('BBQP', _P, 'A26'), 'Annual permits and licenses (catering / health permit, MFU or event permits, fire inspections)'),
    (('BBQP', _P, 'A27'), 'Vehicle & trailer fuel, maintenance and registration'),
    (('BBQP', _P, 'A30'), 'Software (catering / CRM, e-signature, POS, website)'),
    (('BBQP', _P, 'A31'), 'Linens, uniforms and cleaning'),
    (('BBQP', _P, 'A32'), 'Waste, grease and ash disposal'),
    (('BBQP', _P, 'A33'), 'Smoker & equipment repair'),
    (('BBQP', _P, 'A34'), 'Food safety training (ServSafe Manager, food handler cards)'),
    (('BBQP', _P, 'A35'), 'Tastings for prospects'),
    (('BBQP', _P, 'A52'), 'Cost of goods sold (BBQ packages + add-ons)'),
    (('BBQP', _P, 'A55'), 'Commissary & parking / Sales'),
    (('BBQP', _N, 'A20'), 'Commissary & parking / Sales'),
    # Staffing (D103): 4 puestos W-2, cobertura por evento, nota W-2 / pit cook
    (('BBQP', _R, 'A5'), 'Owner / Pitmaster & Sales'),
    (('BBQP', _R, 'A6'), 'Pit cook / lead cook (W-2)'),
    (('BBQP', _R, 'A7'), 'Event staff (servers, buffet attendants, carvers; hourly W-2)'),
    (('BBQP', _R, 'A8'), 'Prep cook / driver (part-time W-2)'),
    (('BBQP', _R, 'A15'), 'COVERAGE OF EVENT HOURS'),
    (('BBQP', _R, 'A18'), 'Hours per person per event (portioning, overnight cook, loading, travel, setup, service, '
                          'breakdown)'),
    (('BBQP', _R, 'A19'), 'People per event (pit crew and event staff, average)'),
    (('BBQP', _R, 'A20'), 'Event hours to cover per year'),
    (('BBQP', _R, 'A24'), 'Columns D-G are TOTALS for the row. Event staff (servers, buffet attendants, carvers) are hourly '
                          'W-2 employees with payroll taxes and workers\' comp: paying them as 1099 contractors is a '
                          'misclassification risk (FLSA; California AB5). One pit cook can watch several cooks at once.'),
    # 12-Month Cash Flow (D103): Month 1 = mes de apertura (marzo); el depósito del 50 % no se modela
    (('BBQP', _T, 'O5'), 'Share of the year\'s events per month (100% in total). Month 1 = opening month (March in the '
                         'example). The 50% deposit is not modeled: it improves real cash.'),
    # notas del motor que el catering y el bar móvil ya habían reescrito (m2, m4, m8, m11, m15)
    (('BBQP', _S, 'C20'), 'FICA (Social Security 6.2% + Medicare 1.45%) + federal and state unemployment taxes (FUTA / '
                          'SUTA). Workers\' comp is in the insurance line. The example uses a lean 10% with no benefits; '
                          'ask your payroll provider for your rate.'),
    (('BBQP', _S, 'A2'), 'Change the GREEN cells: the rest of the workbook recalculates on its own. Expense items are typed '
                         'on their own tab (also in green) and are not repeated here. Amounts are in US dollars (or your own '
                         'currency).'),
    (('BBQP', _S, 'C39'), 'Example rate: state + local sales tax combined, applied to the whole invoice (food, staffing, '
                          'rentals and the service charge). It varies widely by state and city: look up yours. UK: 20% VAT '
                          'applies to catering for events and functions (VAT Notice 709/1).'),
    (('BBQP', _S, 'C67'), 'Minimum cushion of the plan above break-even (plan ÷ break-even − 1). The drop you can absorb is '
                          '1 − break-even ÷ plan: a 15% cushion lets events fall by about 13% before costs stop being covered'),
    (('BBQP', _E, 'E24'), 'How far the plan sits above the cash break-even (plan ÷ break-even − 1); the drop you can absorb '
                          'is 1 − break-even ÷ plan. The required minimum is set in the "0. Assumptions" tab'),
])

# ==========================================================================
# Cifras prohibidas (D110): ES del parrillero 2.2 (importe y frase), casos EN ajenos (catering, mobile bar, FT) y el
# vocabulario vetado RX_BBQ_NO (con su lista blanca). Formato: (regex, motivo, excepción sobre el texto entero)
# ==========================================================================
def _num(n):
    """190000 → patrón que casa 190,000 · 190.000 · 190 000 · 190000 (y nada pegado a más dígitos)."""
    s = str(n)
    cab, cola = s[:-3], s[-3:]
    return r'(?<![\d.,])' + cab + r'[.,   ]?' + cola + r'(?![\d])'


# F1-inventario §7: los 31 importes de `parrillero-2_2/cifras_caso_es.json` (LIVE) + los previos a la calibración ES
CIFRAS_ES = (190000, 205200, 215460, 76522, 54596, 21926, 87357, 65400, 15737, 160401, 151894, 182179, 192570, 109706,
             80294, 92616, 57983, 14527, 16887, 15403, 17090, 19867, 20538, 138000, 243100, 40588, 12934, 10835, 6145,
             4912, 4251, 49900, 62000)
FRASES_ES = [
    # D110: los redondos ES solo como frase con € o EUR (como importe chocarían con importes US plausibles)
    (r'(?i)(?:€|\bEUR)\s?(?:77|84|22)[.,]?000\b|\b(?:77|84|22)[.,]?000\s?(?:€|EUR\b)', 'redondo ES con € (77.000 / 84.000 / '
                                                                                        '22.000)'),
    (r'(?i)\b95 events\b', 'caso ES (95 eventos/año)'),
    (r'(?i)\b80 guests (?:per|an?|each) event\b|\baverage of 80 guests\b', 'caso ES (80 invitados por evento)'),
    (r'(?i)\b81 events\b', 'equilibrio ES (81 eventos)'),
    (r'(?i)\b76 events\b', 'equilibrio de caja ES (76 eventos)'),
    (r'(?i)\b75\s?[-–]\s?80 events\b', 'rango ES (75-80 eventos)'),
    (r'(?i)\b6\.7 events (?:a|per) month\b', 'caso ES (6,7 eventos/mes)'),
    (r'(?i)\b25\s?€|€\s?25\b|\b27\.51\b', 'precio ES (25 €/invitado)'),
    (r'\b57\.7\s?%', 'ratio ES (57,7 %)'), (r'\b31\.8\s?%', 'ratio ES (31,8 %)'), (r'\b30\.5\s?%', 'ratio ES (30,5 %)'),
    (r'\b25\.1\s?%', 'ratio ES (25,1 %)'),
    (r'(?i)\bDSCR (?:of )?1\.51\b', 'DSCR ES (1,51)'),
    (r'(?i)\b83 (?:tasks|steps|milestones)\b', 'recuento del checklist ES (83 tareas)'),
    (r'(?i)\b93 (?:validated )?suppliers\b', 'promesa ES (93 proveedores)'),
    (r'(?i)\b11 deliverables\b', 'recuento ES (11 entregables)'),
    (r'(?i)\b8 (?:autonomous )?regions\b', 'anexo CCAA del ES (8 comunidades)'),
    (r'(?i)\b18 cuts\b|\b12[- ]cut menu\b', 'erratas ES («18 cortes», «carta 12 cortes»: D113)'),
    (r'\bv1\.1\b|\b[Vv]ersion 1\.1\b', 'historia de versiones (la EN nace en 2.2)'),
]
# lista blanca (D110): chimichurri, Argentine asado, picanha, provoleta, commissary, food handler, smoker trailer, pickup,
# «BBQ food trucks», «carving station», «cocktail hour», «AI Chef Pro» y la firma; «chefs and head cooks» solo en la fila
# OEWS de la D19 (decisión SPEC); VAT solo en la nota UK
_FIRMA = r'John Guerrero'
_OEWS = r'John Guerrero|\bchefs and head cooks\b[^.]*\b(?:OEWS|35-1011|BLS)\b|\b(?:OEWS|35-1011|BLS)\b[^.]*\bchefs and head cooks\b'
RX_BBQ_NO = [
    # heredado del FT (D72)
    (r'(?i)\bper day\b', 'vocabulario FT («per day»)', None),
    (r'(?i)\boperating days?\b', 'vocabulario FT («operating days»)', None),
    (r'(?i)(?<!corporate )\bcustomers\b', 'vocabulario FT («customers» → clients / guests / hosts)',
     r'^Synthetic paragraph \d+ of the \w+ plan for the assembly test'),
    (r'(?i)(?<!BBQ food )\btrucks?\b(?! Business Plan Kit)', 'vocabulario FT («truck» → tow vehicle / pickup / smoker '
                                                              'trailer; solo «BBQ food trucks» y el nombre del kit)', None),
    (r'(?i)\bwindows?\b', 'vocabulario FT («window»)', None),
    (r'(?i)\bfestivals?\b', 'vocabulario FT («festival»)', None),
    # del catering EN (F1-inventario §7)
    (r'(?i)\bplated\b', 'catering genérico («plated»)', None),
    (r'(?i)\b(?:chef-attended|themed|action) stations?\b', 'catering genérico («themed / action stations»)', None),
    (r'(?i)\bchef-attended\b', 'catering genérico («chef-attended»)', None),
    (r'(?i)(?<!AI )\b(?:executive |sous )?chefs?\b', 'catering genérico («chef» → pitmaster)', _OEWS),
    (r'(?i)\binduction\b', 'catering genérico («induction»)', None),
    (r'(?i)\btaco bars?\b', 'catering genérico («taco bar»)', None),
    (r'(?i)\bpasta\b', 'catering genérico («pasta»)', None),
    (r'(?i)\b(?:12|twelve) (?:world )?cuisines\b', 'catering genérico («12 cuisines»)', None),
    (r'(?i)\brefrigerated (?:cargo )?vans?\b', 'catering genérico («refrigerated van»: aquí la van no es frigorífica)',
     None),
    # del bar móvil (por si algo se copia de -5/)
    (r'(?i)\bcocktails?\b(?! hour)', 'bar móvil («cocktails»; solo «cocktail hour»)', None),
    (r'(?i)\bbartend(?:er|ers|ing)\b', 'bar móvil («bartender»)', None),
    (r'(?i)\bdry hire\b', 'bar móvil («dry hire»)', None),
    (r'(?i)\bmobile bars?\b', 'bar móvil («mobile bar»)', None),
    (r'(?i)\bbarbacks?\b', 'bar móvil («barback»)', None),
    (r'(?i)\bmixers?\b', 'bar móvil («mixers»)', None),
    (r'(?i)\bspecialty bars?\b|\bcash bars?\b', 'bar móvil («specialty / cash bar»)', None),
    # del ES del parrillero
    (r'\bEspaña\b|\bSpain\b', 'ES («España»)', None),
    (r'\bIVA\b', 'ES («IVA»)', None),
    (r'\bVAT\b', 'ES («VAT» fuera de la nota UK)', r'\bUK\b|United Kingdom|HMRC'),
    (r'(?i)\baut[oó]nomo\b|\bfijos? discontinuos?\b|\bETT\b', 'trámite ES (autónomo / fijo discontinuo / ETT)', None),
    (r'\bSL\b|\bIAE\b|\bAESAN\b|\bAPPCC\b|\bCCAA\b|\bINFOCA\b|\bATP\b|\bFACe\b|Veri\*?factu', 'trámite / norma ES',
     None),
    (r'\bRD \d|Reglamento \(CE\)|Real Decreto', 'norma ES (RD / Reglamento)', None),
    (r'Bodas\.net|Zankyou|Hosply|\bGGM\b|Brogas|Texfire', 'proveedor / directorio ES', None),
    (r'(?i)\bparrilleros?\b|chulet[oó]n|lechazo|cochinillo|\bcarn[eé] de\b|\bcarné\b', 'ES (parrillero, chuletón, '
                                                                                       'lechazo, cochinillo, carné)', None),
    (r'\bEUR\b|€', 'moneda ES', None),
    (r'(?i)\bfree-?lance', 'jerga (§0): «freelance» → part-time hourly W-2 staff', None),
    # regla de jerga §0 (research §9)
    (r'(?i)\bgrill ?masters?\b', 'jerga (§0): «grill master» → pitmaster', None),
    (r'(?i)\bsupport kitchen\b', 'jerga (§0): «support kitchen» → commissary', None),
    (r'(?i)\bgrill catering\b|\broast catering\b|\bparrilla service\b', 'jerga (§9a): nombre del negocio = BBQ catering',
     None),
    (r'\bCambros?\b', 'jerga (§0): «Cambro» es marca → insulated food carriers / hot boxes', None),
    (r'\bD\s?[-–+]\s?\d{1,2}\b', 'calco ES «D-21 / D-14 / D-1» → «3 weeks out / 2 weeks out / day before»', None),
    # unidades (REGLA_UNIDADES): kg, km, litros, °C y m² solo entre paréntesis
    (r'(?i)\d\s?(?:kg|km|°C|liters?|litres?)\b(?![^()]*\))', 'unidades: métrica solo entre paréntesis (REGLA_UNIDADES)',
     None),
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
FRASES_MBAR = [(r'(?i)\b160 events\b', 'caso del mobile bar EN («160 events»)'),
               (r'(?i)\$14(?:\.00)? (?:per|a) guest\b', 'caso del mobile bar EN («$14 per guest»)')]


# ==========================================================================
# Tokens del docx (D108): los del motor con descripciones de BBQ + alias legibles + partidas propias. Cada token apunta a
# SU celda (decisión SPEC: la ranura [98] del ES usa {DIAS_COBRO} para los pagos a proveedores; aquí {{pago_dias}})
# ==========================================================================
_DESC = OrderedDict([
    ('clientes_dia', 'EVENTS per year, year 1 (alias heredado: usa {{eventos_a1}})'),
    ('clientes_a2', 'EVENTS per year, year 2 (alias: usa {{eventos_a2}})'),
    ('clientes_a3', 'EVENTS per year, year 3 (alias: usa {{eventos_a3}})'),
    ('ticket', 'average price per guest excl. sales tax (alias: usa {{precio_invitado}})'),
    ('precio_menu', 'price per guest incl. sales tax (alias: usa {{precio_invitado_con_tax}})'),
    ('dias', 'average guests per event (alias: usa {{invitados_evento}})'),
    ('crecimiento_a2', 'growth in EVENTS in year 2'), ('crecimiento_a3', 'growth in EVENTS in year 3'),
    ('consumibles_pct', 'disposables, wood & cooking fuel (charcoal, pellets, propane backup), % of sales'),
    ('tarjeta_pct', 'card processing fees, % of sales (private clients pay deposits and balances by card)'),
    ('alquiler_mes', 'commissary kitchen rent & smoker trailer parking, per month'),
    ('suministros_mes', 'utilities per month (water, power and phone not covered by the commissary)'),
    ('seguros_anual', 'insurance per year (general liability / BOP, commercial auto covering the trailer, workers\' comp, '
                      'inland marine)'),
    ('vida_obra', 'useful life of the smoker trailer, van and fit-outs, years'),
    ('vida_equipo', 'useful life of the live-fire rig, holding equipment, pit tools and software, years'),
    ('ocupacion_anual', 'commissary kitchen rent & smoker trailer parking per year'),
    ('ocupacion_pct', 'commissary kitchen rent & smoker trailer parking, % of sales'),
    ('cogs_pct', 'cost of goods (BBQ packages + add-ons), % of sales'),
    ('equilibrio_clientes_dia', 'break-even EVENTS per year, accounting (alias: usa {{equilibrio_eventos}})'),
    ('equilibrio_caja_clientes_dia', 'cash break-even EVENTS per year (alias: usa {{equilibrio_caja_eventos}})'),
    ('pesimista_clientes', 'pessimistic scenario: events per year (alias: usa {{pesimista_eventos}})'),
    ('optimista_clientes', 'optimistic scenario: events per year (alias: usa {{optimista_eventos}})'),
    ('pesimista_ticket', 'pessimistic scenario: price per guest (alias: usa {{pesimista_precio}})'),
    ('optimista_ticket', 'optimistic scenario: price per guest (alias: usa {{optimista_precio}})'),
    ('pesimista_dias', 'pessimistic scenario: guests per event (alias: usa {{pesimista_invitados}})'),
    ('optimista_dias', 'optimistic scenario: guests per event (alias: usa {{optimista_invitados}})'),
    ('inv_vehiculo', 'smoker trailer (offset / reverse-flow, 500-gal class, new)'),
    ('inv_adaptacion', 'smoker trailer upfit (warming cabinet, hand sink + water tanks if the county requires, storage '
                       'boxes, lights)'),
    ('inv_permisos', 'first-year permits and certifications (catering / health permit, MFU or temporary event permits, '
                     'fire inspection, ServSafe Manager)'),
    ('inv_lanzamiento', 'website, photos, launch and first bridal show'),
    ('inv_stock', 'opening inventory (meat for test cooks, rubs, sauces, wood, disposables)'),
    ('horas_semana', 'full-time hours per week'),
])
# fuera: ventas ÷ «días» no significa nada; las filas 9-10 del FT son aquí otras partidas (alias propios abajo); los
# nombres «food_cost_*» se sustituyen por alias neutros (coste_paquetes_pct / coste_extras_pct)
_FUERA = ('ventas_dia', 'inv_equipo_cocina', 'inv_generador', 'food_cost_comida', 'food_cost_bebida')
TOKENS_PROPIOS = OrderedDict([
    # alias legibles del motor (las mismas celdas que los tokens heredados)
    ('eventos_a1', ('int', ('fila', _S, 'Clientes/día (media del año 1)', 'B'), 'events per year, year 1')),
    ('eventos_a2', ('int', ('fila', _P, 'Clientes/día (media)', 'C'), 'events per year, year 2')),
    ('eventos_a3', ('int', ('fila', _P, 'Clientes/día (media)', 'D'), 'events per year, year 3')),
    ('precio_invitado', ('usd2', ('fila', _S, 'Ticket medio SIN IVA (€)', 'B'),
                         'average price per guest of the event mix, excl. sales tax, staffing and service included')),
    ('precio_invitado_con_tax', ('usd2', ('fila', _S, 'PVP equivalente con IVA (calculado)', 'B'),
                                 'average price per guest incl. sales tax')),
    ('invitados_evento', ('int', ('fila', _S, 'Días de apertura al año', 'B'), 'average guests per event')),
    ('capacidad_eventos', ('int', ('fila', _S, {'bbq': 'Plazas de pie y mesas altas junto al vehículo'}, 'B'),
                           'max events a year the pit and crew can handle (information only)')),
    ('cuota_paquetes_pct', ('pct0', ('fila', _S, 'Ventas de COMIDA sobre el total', 'B'),
                            'BBQ packages, % of sales (the rest are add-ons)')),
    ('coste_paquetes_pct', ('pct0', ('fila', _S, 'Coste de mercancía sobre las ventas de COMIDA', 'B'),
                            'cost of goods on BBQ package sales (raw meat, sides, bread, sauces)')),
    ('coste_extras_pct', ('pct0', ('fila', _S, 'Coste de mercancía sobre las ventas de BEBIDA', 'B'),
                          'cost of goods on add-on sales')),
    ('marketplace_pct', ('pct0', ('fila', _S, 'Ventas por delivery sobre el total', 'B'),
                         'share of sales through corporate catering marketplaces (e.g. ezCater)')),
    ('marketplace_comision', ('pct0', ('fila', _S, 'Comisión de la plataforma de delivery', 'B'),
                              'marketplace commission on those sales')),
    ('cobro_dias', ('int', ('fila', _S, 'Días medios de cobro', 'B'), 'average days to collect from clients')),
    ('pago_dias', ('int', ('fila', _S, 'Días medios de pago a proveedor', 'B'), 'average days to pay suppliers')),
    ('horas_evento', ('dec1', ('fila', _R, 'Horas de servicio al día que hay que cubrir', 'B'),
                      'hours per person per event (portioning, overnight cook, loading, travel, setup, service, breakdown)')),
    ('personas_evento', ('dec1', ('fila', _R, 'Personas necesarias a la vez en cada franja', 'B'),
                         'people per event (pit crew and event staff, average)')),
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
    # partidas de la inversión del BBQ caterer (D102: filas 9-20 con el orden del inventario §3)
    ('inv_rig', ('usd', ('fila', _I, {'bbq': 'Equipamiento cocina móvil'}, 'B'),
                 'live-fire rig (Santa Maria grill, Argentine parrilla, asado crosses, La Caja China)')),
    ('inv_almacen', ('usd', ('fila', _I, {'bbq': 'Generador eléctrico o conexión'}, 'B'),
                     'commissary storage fit-out (racks, meat lugs, vacuum sealer)')),
    ('inv_furgoneta', ('usd', ('fila', _I, {'bbq': 'Instalación gas (si aplica)'}, 'B'), 'used cargo van')),
    ('inv_furgoneta_upfit', ('usd', ('fila', _I, {'bbq': 'Depósito de agua + aguas residuales'}, 'B'),
                             'van upfit (shelving, racks, tie-downs, wrap)')),
    ('inv_llc', ('usd', ('fila', _I, {'bbq': 'Constitución SL + notaría + registro'}, 'B'),
                 'LLC formation, contracts and legal')),
    ('inv_inspeccion', ('usd', ('fila', _I, {'bbq': 'Proyecto técnico sanitario'}, 'B'),
                        'plan review / trailer inspection (only if the county requires it)')),
    ('inv_software', ('usd', ('fila', _I, {'bbq': 'TPV móvil + datáfono'}, 'B'), 'catering software, card reader and tablet')),
    ('inv_herramientas', ('usd', ('fila', _I, {'bbq': 'Menaje, utensilios, packaging eco'}, 'B'),
                          'smallwares & pit tools (knives, hotel pans, probe thermometers, butcher paper)')),
    ('inv_holding', ('usd', ('fila', _I, {'bbq': 'Toldo, mobiliario exterior plegable'}, 'B'),
                     'holding & service equipment (insulated food carriers, hot boxes, chafing dishes, coolers, canopy, '
                     'carving board)')),
    # derivadas
    ('ventas_evento', ('usd', ('deriv', lambda c: c['ventas_a1'] / c['clientes_dia']),
                       'average revenue per event, year 1 (excl. sales tax)')),
    ('invitados_a1', ('int', ('deriv', lambda c: c['clientes_dia'] * c['dias']), 'guests served in year 1')),
    ('caida_absorbible_pct', ('pct0', ('deriv', lambda c: c['holgura_caja_pct'] / (1 + c['holgura_caja_pct'])),
                              'drop in events the plan can absorb before cash stops covering costs (1 − break-even ÷ plan)')),
])


def tokens_bbq(base):
    out = OrderedDict()
    for t, (fmt, src, desc) in base.items():
        if t in _FUERA:
            continue
        if src[0] == 'fila':
            _, hoja, rot, col = src
            if isinstance(rot, dict):
                if 'ft' not in rot:
                    continue                               # partidas de la cafetería
                src = ('fila', hoja, {'bbq': rot['ft']}, col)
        if t == 'consumibles_pct':
            fmt = 'pct1'                               # M1 de REVISION-FINAL: 3.5 %, no 4 %
        out[t] = (fmt, src, _DESC.get(t, desc))
    out.update(TOKENS_PROPIOS)
    return out


# ==========================================================================
# Docx (D108): lo que escribe ensamblar_docx.py y las notas para los redactores
# ==========================================================================
PRODUCTOS_CIERRE_BBQ = ['Catering Business Plan Kit', 'Food Truck Business Plan Kit', 'Food Cost Kit Pro',
                        'HACCP Food Safety Kit Pro']


def docx_fijos(M):
    pc = PRODUCTOS_CIERRE_BBQ
    d = OrderedDict([
        (6, 'BUSINESS PLAN'), (7, 'BBQ Catering'),
        (9, 'Complete financial plan, market analysis,\noperations strategy and startup checklist\nto launch an off-site '
            'BBQ catering company in the United States'),
        (14, 'AI Chef Pro'), (15, 'aichef.pro'), (16, 'US edition with UK notes · 2026'),
        (18, 'LEGAL NOTICE'), (19, M.AVISO_DOCX_EN), (20, '© 2026 AI Chef Pro — aichef.pro'), (22, 'CONTENTS'),
        (35, 'Appendices: BBQ Catering Financial Projections (Excel) + BBQ Catering Pricing Calculator (Excel) + BBQ '
             'Catering Startup Checklist (Excel)'),
        (123, 'AI Chef Pro'), (124, 'Templates and AI tools for food businesses'),
        (126, 'aichef.pro\ninfo@aichef.pro'),
        (127, '→ %s · %s' % tuple(pc[:2])), (128, '→ ' + pc[2]), (129, '→ ' + pc[3]), (130, '\n' + M.URL_TIENDA),
    ])
    return OrderedDict([('bbq', d)])


DOCX_NOTAS_PLAN = OrderedDict([
    ('bbq', 'ESCRIBES, NO TRADUCES (D108). El «es» de cada párrafo es la RANURA del plan de FOOD TRUCK (solo da el papel '
            'del párrafo y su longitud aproximada); el EN publicado del catering de esa misma ranura '
            '(../business-plans-en-4/docx_en_cat_a.json / _b.json) sirve de modelo de estructura; la nota de cada '
            'párrafo trae al final el párrafo ES 2.2 DEL PARRILLERO de la MISMA ranura (contenido de referencia: sus '
            'cifras, sus {TOKENS} en mayúsculas y todo lo español NO se usan). El contenido es de un FULL-SERVICE '
            'OFF-SITE BBQ CATERER (D99): ahúma en el patio de la commissary, hot holding en insulated food carriers / hot '
            'boxes, staffed buffet con carving station, smoker trailer al evento solo como «live pit on site» (add-on '
            'de pago), drop-off corporativo como segunda línea, live-fire premium. Fuentes: research §1, §5, §6, §8 y '
            '§9 (glosario OBLIGATORIO, regla de jerga §0) de business-plans-en-6/F1-research-us-delta.md. Cifras del '
            'caso SOLO con tokens {{…}}; de mercado, solo las de research «leída» con su fuente. Prohibido (gate '
            'RX_BBQ_NO): «truck» (el vehículo de arrastre es «tow vehicle» o «pickup»; solo «BBQ food trucks» para el '
            'competidor), «per day», «operating days», «customers» (di clients / guests), «window», «festival», «chef» '
            '(di pitmaster / pit cook), «plated», «themed / chef-attended / action stations» (sí «carving station»), '
            '«induction», «refrigerated van», «cocktails» (sí «cocktail hour»), «bartender», «grill master», «support '
            'kitchen», «Cambro», «freelance», «D-21» y similares, kg / °C / litros fuera de paréntesis, las cifras del '
            'ES del parrillero (190.000, «95 eventos», «80 invitados por evento», «25 €»…) y de los casos del catering '
            '(«180 events», «$60 per guest») y del bar móvil («160 events», «$14 per guest»), «España», «ChefBusiness». '
            + REGLA_UNIDADES + '. Lo no verificado por la research va como «check your county / state rules» o «check '
            'with your fire marshal», nunca como cifra. El cierre (productos) lo escribe el ensamblador'),
])
# §9 = el núcleo legal (D108); research §6
_N9 = OrderedDict([
    (102, 'D108 §9 1/7: commissary OBLIGATORIA y nada de cocina de casa: FDA Food Code 2022 §3-201.11(B) «FOOD prepared '
          'in a private home may not be used» (fda.gov) y (A) «obtained from sources that comply with LAW»; el cottage '
          'food excluye la carne (Texas: «any foods, except… meat, meat products, poultry», dshs.texas.gov); California: '
          'catering ligado a una cocina con permiso y el MEHKO no permite catering. Por eso el plan ahúma en una '
          'commissary con permiso y firma un commissary agreement por escrito'),
    (103, '§9 2/7: permisos y personas: catering / health permit del condado (cuota + inspección; plan review del '
          'trailer solo si lo piden: {{inv_inspeccion}} en el ejemplo) + Certified Food Protection Manager (ServSafe '
          'Manager) + food handler cards según el estado + plan de seguridad alimentaria basado en HACCP con las '
          'normas del FDA Food Code 2022 (3-401.11): 145 °F 15 s carne intacta, whole roasts 145 °F 4 min, 155 °F 17 s '
          'carne inyectada, ablandada o picada (sausage incluida: inyectar un brisket o un pork butt lo vuelve '
          'non-intact), 165 °F aves; hot holding ≥ 135 °F (3-501.16); enfriado «to 70 °F within 2 hours and to 41 °F '
          'within a total of 6 hours» (3-501.14, una sola regla); recalentado a 165 °F (3-403.11). Approved source: '
          'carne con inspección USDA o estatal; la custom exempt va marcada «not for sale» (nichemeatprocessing.org): '
          'el whole hog, de planta inspeccionada. 9 alérgenos mayores'),
    (104, '§9 3/7: el smoker trailer en el evento: en TEXAS una mobile food unit «shall operate from a central '
          'preparation facility or other fixed food establishment», con parte diario, lavamanos, agua potable y CFPM '
          '(25 TAC §228.221, law.cornell.edu); Florida (DBPR) y North Carolina (15A NCAC 18A .2670) piden algo '
          'parecido; California, no verificado. Regla: «ask your county» si ahumar o servir desde el trailer en el '
          'evento lo convierte en mobile food unit y qué permiso pide; si no hay permiso, ahúma en la commissary y '
          'lleva la carne en hot boxes. Eventos públicos o comunitarios: temporary food establishment permit. Los '
          'venues piden COI y a veces additional insured'),
    (105, '§9 4/7: fuego (IFC 2021 según lo adopte tu ciudad; boletín del Corpus Christi Fire Department, '
          'corpuschristitx.gov): «solid fuel cooking appliances (wood burning, BBQ pits)» con extintor Class K de 2.5 '
          'gallons (906.4.1) + 2A:10BC; 10 ft entre puestos; propano ≤ 200 lb (319.8.1); algunos municipios piden '
          'permiso por despliegue. Burn bans y cocina bajo carpas: NO verificado → «check with your fire marshal». El '
          'contrato lleva fuerza mayor por burn ban con propane backup o nueva fecha (del ES: plan B de gas)'),
    (106, '§9 5/7: sales tax: en muchos estados grava TODA la factura de catering (comida, personal, alquileres) y el '
          'service charge según el estado (CA: cdtfa.ca.gov; NY: TB-ST-110; TX: excluido si ≤ 20 % separado y '
          'repartido) → el libro aplica {{sales_tax}} a toda la factura (conservador). IRS Rev. Rul. 2012-18: el '
          'service charge obligatorio es SALARIO, no propina; la gratuity voluntaria va aparte y es del personal. '
          'Sales tax permit del estado. Alcohol: el BBQ caterer no lo vende; si el cliente pone alcohol, que lo sirva '
          'un servicio con licencia y su propio seguro (liquor liability); sin cifras'),
    (107, '§9 6/7: empleo y seguros: event staff, pit cook y prep cook en nómina W-2 (servers y carvers de eventos son '
          'casi siempre empleados: FLSA; California AB5 presume empleo), nunca 1099 ni «freelance»; workers\' comp, '
          'I-9 / W-4 / new-hire reporting. Seguros ({{seguros_anual}} al año en el ejemplo): general liability / BOP, '
          'commercial auto QUE CUBRA EL REMOLQUE, workers\' comp, inland marine para el smoker y el equipo en tránsito '
          '(Insureon publica medias por póliza: insureon.com); COI y additional insured para los venues'),
    (108, '§9 7/7: el smoker trailer y la furgoneta: título, registro y placas en el DMV de tu estado (las reglas de los '
          'remolques varían: pregunta) y una póliza de auto que cubra el uso comercial y el remolque; una cargo van no '
          'necesita CDL (solo con GVWR ≥ 26,001 lb). Como ÚLTIMA frase o frases del párrafo, la nota UK: registrar el '
          'food business en el council «at least 28 days before trading», también desde una unidad móvil o un local '
          'temporal (gov.uk); Food Hygiene Rating 0-5 (FHIS en Escocia), plan HACCP, 14 alérgenos, VAT 20 % del '
          'catering de eventos, y permiso del evento y plan de fuego con el council y el venue'),
])
_NOTAS_SECCION = OrderedDict([
    (39, '§1 1/5: la oportunidad: BBQ catering en EE. UU. para empresas, fiestas y graduaciones, y bodas; demanda SOLO '
         'con research §2 (búsquedas mensuales US: «bbq catering» 9,900 y «bbq catering near me» 18,100, que hace el '
         'cliente que contrata; el emprendedor busca «bbq business plan», 70); sin tamaño de mercado inventado'),
    (40, '§1 2/5: el concepto (D99): full-service off-site BBQ caterer que ahúma en el patio de la commissary (brisket, '
         'pulled pork, ribs, chicken, sausage), mantiene en caliente en insulated food carriers / hot boxes y sirve en '
         'staffed buffet con carving station; el smoker trailer va al evento solo en bodas y eventos premium («live pit '
         'on site», add-on de pago); drop-off corporativo como segunda línea; live-fire premium (Argentine asado, Santa '
         'Maria tri-tip, whole hog / La Caja China). Del ES: el fuego y el corte delante del invitado, el punto con '
         'sonda'),
    (41, '§1 3/5: inversión y financiación SOLO con tokens: {{inversion_total}} = {{capex}} + {{fondo_maniobra}}; '
         '{{fondos_propios}} ({{aportacion_pct}}) + préstamo {{prestamo}} al {{tipo_prestamo}} a {{plazo_prestamo}} '
         'años (SBA 7(a): supera el tope de $50,000 del SBA Microloan); el tow vehicle es la pickup del dueño'),
    (42, '§1 4/5: proyecciones: {{eventos_a1}} eventos × {{invitados_evento}} invitados × {{precio_invitado}} → '
         '{{ventas_a1}} / {{ventas_a2}} / {{ventas_a3}}; EBITDA {{ebitda_pct_a1}}; equilibrio {{equilibrio_eventos}} '
         'eventos/año; DSCR mínimo {{dscr_min}}; y la frase honesta (D100): es el caso de un operador a tiempo completo '
         'con pit cook y presupuesto de marketing, no la media del primer año'),
    (43, '§1 5/5: el equipo: Owner / Pitmaster & Sales, pit cook / lead cook, event staff (servers, buffet attendants, '
         'carvers) y prep cook / driver, todos W-2 ({{plantilla_puestos}} personas, {{plantilla_jornadas}} FTE); sin '
         'inventar trayectoria'),
    (46, '§2 1/5: qué vende y a quién: empresas (drop-off de boxed BBQ lunches y buffets), familias (fiestas privadas, '
         'graduaciones), parejas (bodas) y clientes premium (live-fire); el cliente compra carne ahumada bien hecha, '
         'caliente y a tiempo, sin pensar en la logística'),
    (47, '§2 2/5: propuesta de valor: smoke (low and slow con post oak o hickory, bark y smoke ring) + live fire; el '
         'pitmaster delante del invitado en la carving station; estilos regionales; sonda y hot holding; degustación '
         'previa'),
    (48, '§2 3/5: modelo económico: precio por invitado {{precio_invitado}} sin sales tax con el personal y el service '
         'charge dentro ({{ventas_evento}} por evento de media); BBQ packages {{cuota_paquetes_pct}} de las ventas y el '
         'resto add-ons (live pit on site, postres, alquileres, travel fees); depósito del 50 % nonrefundable para '
         'bloquear la fecha (operadores leídos: eventective.com / Owen\'s BBQ, hutchinsbbq.com); service charge ≠ '
         'gratuity; guest minimum'),
    (49, '§2 4/5: posicionamiento frente a los BBQ restaurants que hacen catering, los caterers generalistas y las '
         'bandejas de supermercado; si nombras la venta callejera, «BBQ food trucks» (no es nuestro comprador); '
         'diferencial: live-fire premium y el pitmaster en la carving station'),
    (50, '§2 5/5: paquetes y menu styles: los 3 paquetes de la calculadora del kit (drop-off · full-service BBQ buffet · '
         'live-fire premium) + el interruptor «live pit on site»; las 10 experiencias del ES → menu styles: Texas · '
         'Carolina (whole hog) · Kansas City (burnt ends) · Memphis (dry-rub ribs) · Santa Maria (tri-tip over red '
         'oak) · Argentine asado · Brazilian churrasco · pig roast (La Caja China) · fire show (tomahawk) · corporate '
         'boxed lunch; guest minimum'),
    (53, '§3 1/6: el mercado US desde el lado del cliente: research §2 (búsquedas mensuales: «bbq catering» y «barbecue '
         'catering» 9,900 cada una, «bbq catering near me» 18,100; «bbq catering prices» y «bbq catering menu» al alza) '
         'sin tamaño de mercado inventado'),
    (54, '§3 2/6: bodas y fiestas: un operador Texas-style de Los Angeles cobra $40-58 por invitado en fiestas y $65-85 '
         'en bodas, con mínimo de 30 invitados (eventective.com, Owen\'s BBQ); temporada alta de bodas en mayo-junio y '
         'septiembre-octubre (sin porcentajes: la fuente es «resumen»)'),
    (55, '§3 3/6: empresas: drop-off desde $17.50 por persona y full-service con buffet atendido (q39kc.com, Kansas '
         'City); boxed BBQ lunches; marketplaces corporativos (comisión del libro: {{marketplace_comision}}); '
         'graduaciones en mayo-junio, 4 de julio y holiday parties en diciembre'),
    (56, '§3 4/6: mezcla del ejemplo (Kit estimate, research §8): 55 drop-off corporativos (40 invitados × $22), 45 '
         'fiestas y graduaciones (70 × $35), 22 eventos de empresa full-service (110 × $36), 20 bodas (130 × $52) y 8 '
         'live-fire (90 × $65): las bodas son el 13 % de los eventos y el 32 % de las ventas; estacionalidad: Month 1 = '
         'marzo, enero y febrero flojos'),
    (57, '§3 5/6: tendencias con cuidado: estilos regionales, live fire (Argentine asado, Santa Maria), bodas rústicas en '
         'barn venues y ranches; sin cifras sin fuente'),
    (58, '§3 6/6: riesgos de demanda y REALISMO (D100): temporada de bodas, cancelaciones, burn bans, presupuestos '
         'corporativos; 150 eventos al año son los de un operador a tiempo completo con pit cook y $10K de marketing, '
         'no la media del primer año (orden de magnitud: ≈ $300K el año 1, Kit estimate)'),
    (61, '§4 1/6: panorama competitivo local: BBQ restaurants con catering, BBQ caterers de fin de semana, caterers '
         'generalistas, bandejas de supermercado y «BBQ food trucks»'),
    (62, '§4 2/6: cinco fuerzas de Porter aplicadas al BBQ catering (estructura del ES [62])'),
    (63, '§4 3/6: competidores directos e indirectos y cómo compararse: precio por invitado, guest minimum, qué incluye '
         '(carnes, sides, personal, montaje), reseñas en The Knot, WeddingWire, Zola y Google'),
    (64, '§4 4/6: barreras de entrada: commissary con permiso (no desde casa), smoker trailer (desde $8,495 un offset en '
         'trailer: yodersmokers.com), seguros, permisos del condado y del fire marshal, y el oficio del pitmaster'),
    (65, '§4 5/6: factores críticos de éxito: puntualidad, carne caliente y segura (sonda, hot holding), un brisket '
         'constante, reseñas, relación con venues y wedding planners'),
    (66, '§4 6/6: DAFO del concepto (commissary + smoker trailer + live-fire premium; holgura justa)'),
    (69, '§5 1/7: estrategia: dos embudos (bodas: ciclo largo con degustación; empresas: drop-off recurrente) + fiestas '
         'privadas por referidos'),
    (70, '§5 2/7: presencia digital: web con paquetes y precios «desde» por invitado, formulario de presupuesto, Google '
         'Business Profile, Instagram con vídeo del pit y de la carving station'),
    (71, '§5 3/7: directorios y marketplaces: The Knot, WeddingWire, Zola, ezCater (comisión del libro: '
         '{{marketplace_comision}}) y Thumbtack'),
    (72, '§5 4/7: alianzas: venues (preferred vendor lists, barn venues), wedding planners, office managers; bridal shows'),
    (73, '§5 5/7: degustaciones para prospectos (su línea de coste en el P&L) y el proceso propuesta → contrato → '
         'depósito del 50 %'),
    (74, '§5 6/7: fidelización y referidos: empresas que repiten, fiestas de la misma familia, reseñas después de cada '
         'evento'),
    (75, '§5 7/7: presupuesto: {{marketing_anual}} al año en el ejemplo; medir el coste por evento ganado'),
    (78, '§6 1/5: la base: commissary compartida con permiso (horas de producción, almacén frío y seco, aparcamiento del '
         'smoker trailer donde se pueda ahumar: {{alquiler_mes}} al mes en el ejemplo; research: $15-$45 la hora, '
         'thefoodcorridor.com) y el commissary agreement por escrito; del ES: «es tuyo lo que viaja; lo que usas un día, '
         'lo alquilas»'),
    (79, '§6 2/5: el equipo: smoker trailer {{inv_vehiculo}} + upfit {{inv_adaptacion}}, live-fire rig {{inv_rig}}, '
         'furgoneta de carga usada {{inv_furgoneta}} + upfit {{inv_furgoneta_upfit}}, holding & service '
         '{{inv_holding}}; el tow vehicle es la pickup del dueño (si no la tienes: una pickup usada que remolque ≥ 3,000 '
         'lb, $25,000-$40,000, Kit estimate); orden de compra del equipo del ES (T8): primero lo que cocina, luego lo '
         'que mantiene en caliente, luego lo que sirve'),
    (80, '§6 3/5: la operativa de un evento en 6 fases con cocción nocturna: briefing 3 weeks out → visita al venue 2 '
         'weeks out → pedido de carne 5-7 días antes → rubs, trimming y porcionado en la commissary → cocción nocturna '
         'con sonda (el pit se enciende a la hora que da «Start the pit by» en la calculadora) → reposo, hot holding, '
         'carga, montaje 60-90 min y servicio con carving station → recogida, ceniza fría y cobro de extras. Nunca '
         '«D-21»'),
    (81, '§6 4/5: seguridad de las carnes ahumadas en la operativa: sonda calibrada; temperatura de CALIDAD (brisket ≈ '
         '203 °F: Kit estimate) frente al MÍNIMO SEGURO del Food Code (145 °F intactas, 155 °F inyectadas, picadas y '
         'sausage, 165 °F aves), diciendo siempre cuál es cuál; hot holding ≥ 135 °F; enfriado y recalentado; '
         'rendimiento ≈ 50 % del peso crudo en brisket y pork butt (fieryfoodscentral.com); alérgenos de rubs, salsas y '
         'sides'),
    (82, '§6 5/5: proveedores: carne de origen autorizado (USDA o inspección estatal), cash-and-carry tipo Restaurant '
         'Depot, leña (post oak, hickory, red oak) y carbón, sides; party rentals; mantenimiento del smoker, del '
         'trailer y de la furgoneta'),
    (85, '§7 1/6: estructura: Owner / Pitmaster & Sales, pit cook / lead cook (W-2), event staff (servers, buffet '
         'attendants, carvers; hourly W-2) y prep cook / driver (part-time W-2)'),
    (86, '§7 2/6: coste de personal: {{personal_a1}} el año 1 ({{personal_pct}} de las ventas), con el sueldo del dueño '
         'dentro; el del dueño y el del pit cook son fijos y el del event staff depende de las horas de evento (sin '
         'cifra propia: no hay token)'),
    (87, '§7 3/6: personal por evento: {{horas_evento}} horas por persona × {{personas_evento}} personas por evento, '
         'cobertura {{cobertura_horas}}; ≈ 1 server o buffet attendant por 25-30 invitados en buffet (Kit estimate); un '
         'pit cook vigila varias piezas a la vez; el libro reparte la nómina por igual en los 12 meses (conservador)'),
    (88, '§7 4/6: W-2 frente a 1099 (FLSA; California AB5), nunca «freelance»; cargas {{cargas_pct}}; mínimo federal y '
         'estatal; sueldos BLS OEWS mayo 2025 (bls.gov): cooks, restaurant media $18.62/h y p75 $21.45/h; food servers, '
         'nonrestaurant media $17.37/h y p75 $18.51/h (no escribas «chef» aquí: solo la tabla D19 nombra esa serie)'),
    (89, '§7 5/6: formación: ServSafe Manager (Certified Food Protection Manager), food handler cards, seguridad del '
         'fuego y del propano, el guion de la carving station y del live-fire, alérgenos'),
    (90, '§7 6/6: service charge frente a gratuity (IRS Rev. Rul. 2012-18): el service charge obligatorio es salario; la '
         'gratuity voluntaria es del personal'),
    (93, '§8 1/7: viabilidad: ventas del año 1 {{ventas_a1}}, margen bruto {{margen_bruto_pct}}, EBITDA {{ebitda_a1}} '
         '({{ebitda_pct_a1}}); {{ventas_evento}} por evento; precios dentro de las bandas leídas (drop-off $15-30 en '
         'q39kc.com; bodas por debajo de los $65-85 de Los Angeles)'),
    (94, '§8 2/7: inversión con tokens: {{inv_vehiculo}}, {{inv_adaptacion}}, {{inv_rig}}, {{inv_furgoneta}}, '
         '{{inv_furgoneta_upfit}}, {{inv_holding}}, {{inv_permisos}}, {{inv_lanzamiento}}, {{inv_stock}} → {{capex}} '
         '(con la contingencia del 10 % sobre el trailer, la furgoneta y sus upfits, calculada por fórmula); fondo de '
         'maniobra {{fondo_maniobra}}; total {{inversion_total}}; financiación SBA 7(a)'),
    (95, '§8 3/7: proyección a 3 años: {{ventas_a1}} / {{ventas_a2}} / {{ventas_a3}} (crecen los EVENTOS: '
         '{{crecimiento_a2}} y {{crecimiento_a3}}); resultado neto {{resultado_neto_a1}} / {{resultado_neto_a2}} / '
         '{{resultado_neto_a3}}; el {{impuesto_beneficios}} hace de impuesto sobre la renta: con una LLC pass-through lo '
         'paga el dueño en su declaración, así que la reserva se mantiene'),
    (96, '§8 4/7: costes: BBQ packages {{coste_paquetes_pct}} de sus ventas, mercancía total {{cogs_pct}}, desechables, '
         'leña y combustible de cocina {{consumibles_pct}}, personal {{personal_pct}}, commissary y parking '
         '{{ocupacion_pct}}; benchmarks: food cost de catering 28-35 % (galleysolutions.com), neto 7-8 % '
         '(itsacheckmate.com)'),
    (97, '§8 5/7: punto de equilibrio en EVENTOS al año: {{equilibrio_eventos}} (contable) y '
         '{{equilibrio_caja_eventos}} (caja) frente a {{eventos_a1}} del plan; holgura {{holgura_caja_pct}} (los eventos '
         'pueden caer {{caida_absorbible_pct}} antes de no cubrir la caja); si la holgura es justa, DECIRLO; el libro '
         'muestra la cifra exacta y el plan la redondea a eventos enteros'),
    (98, '§8 6/7: caja y retorno: cobras a {{cobro_dias}} días de media y pagas a los proveedores a {{pago_dias}} días '
         '(CADA TOKEN EN SU CELDA: el ES usa por error los días de cobro para los pagos, D113); las nóminas salen cada '
         'mes; saldo mínimo {{saldo_minimo}} en el mes {{mes_saldo_minimo}}, payback {{payback}}, DSCR {{dscr_min}}; el '
         'depósito del 50 % no se modela y mejora la caja real'),
    (99, '§8 7/7: escenarios: pesimista {{pesimista_eventos}} eventos × {{pesimista_precio}} × {{pesimista_invitados}} '
         'invitados → {{pesimista_ventas}}, resultado {{pesimista_resultado}} y caja estimada {{pesimista_caja}} (si es '
         'negativa, DECIRLO: «the cash runs out»); optimista {{optimista_eventos}} eventos → {{optimista_ventas}} y '
         '{{optimista_resultado}}; recordar que {{eventos_a1}} eventos no son la media del primer año'),
    (111, '§10 1/7: conclusión: por qué el modelo se sostiene (ahúma en la commissary, sin local, el pit en el evento '
          'como premium que se cobra aparte, dos motores de demanda) y la advertencia honesta (holgura justa; el '
          'pesimista agota la caja)'),
    (112, '§10 2/7: riesgos y mitigación: cancelación (depósito del 50 % nonrefundable y tramos), burn ban o lluvia '
          '(propane backup, nueva fecha, carpa con permiso), carne fuera de temperatura (sonda, hot holding, plan '
          'HACCP), avería del smoker trailer o de la furgoneta, subida del precio de la carne (revisa la calculadora con '
          'tus precios), falta de personal los sábados de temporada, inspecciones'),
    (113, '§10 3/7: fortalezas competitivas: el pitmaster y la carving station, el live-fire premium, los estilos '
          'regionales, commissary y permisos en regla'),
    (114, '§10 4/7: hoja de ruta en las 6 fases del checklist (Business Setup → Pits, Fire & Permits → Equipment → Staff '
          '→ Marketing → First 90 Days)'),
    (115, '§10 5/7: KPIs: eventos al mes, precio por invitado, libras crudas por invitado y yield real por corte, food '
          'cost, horas de personal por evento, conversión de propuestas, cancelaciones, reseñas'),
    (116, '§10 6/7: visión a 3 años: más empresas recurrentes, pit cook a tiempo completo o un segundo smoker trailer; '
          'local propio solo si los números lo piden'),
    (117, '§10 7/7: cierre: los siguientes pasos con el Excel, la calculadora de precios (con su «Meat Yield & Smoke '
          'Schedule» y su «Shopping List by Guest Count») y el checklist del kit'),
])


def _es22():
    """Párrafos ES 2.2 del parrillero por ranura (`parrillero-2_2/textos/par_es_{a,b}.json`: las mismas 61 ranuras que
    el EN, F1-inventario §0.5)."""
    out = {}
    for f in ('a', 'b'):
        p = os.path.join(PAR, 'textos', 'par_es_%s.json' % f)
        if os.path.exists(p):
            out.update({int(k): v for k, v in json.load(open(p, encoding='utf-8')).items()})
    return out


def _notas_docx():
    es = _es22()
    out = OrderedDict()
    for i, n in sorted(list(_NOTAS_SECCION.items()) + list(_N9.items())):
        if i in es:
            n += (' ‖ ES 2.2 DEL PARRILLERO EN ESTA RANURA (referencia de contenido; sus cifras, sus {TOKENS} en '
                  'mayúsculas y todo lo español NO se usan): «%s»' % es[i])
        out[i] = n
    return out


DOCX_NOTAS = OrderedDict([('bbq', _notas_docx())])

# ==========================================================================
# Pistas por celda (extraer_textos.py → textos_es.json → tandas)
# ==========================================================================
_CASO = ('D100: caso US = 150 eventos/año × 75 invitados × $38 por invitado (sin sales tax, con personal y service '
         'charge dentro, sin la gratuity voluntaria) = $427,500 (research §8; la calibración D15 puede subir B4 de 10 en '
         '10 hasta 170); drivers: B4 = eventos/año, B5 = precio por invitado, B6 = invitados por evento. Las notas '
         'describen el MÉTODO: sin cifras del caso (cambian al recalibrar)')
CELDA_PISTAS = OrderedDict([
    (('BBQP', _S, 'C4'), _CASO + '; los años 2-3 crecen en EVENTOS (B7/B8); compara con la capacidad del pit y del equipo '
                                 '(fila 51); el ejemplo es un operador a tiempo completo con pit cook, no la media del '
                                 'primer año'),
    (('BBQP', _S, 'C5'), _CASO + '; precio medio por invitado de la MEZCLA (drop-off, fiestas, empresa, bodas, live-fire) '
                                 'SIN sales tax, con el personal y el service charge dentro y SIN la gratuity voluntaria. '
                                 'Los operadores cotizan por paquete (drop-off $15-30 por persona en q39kc.com, staffed '
                                 'buffet, full-service): la calculadora del kit cotiza 3 paquetes por invitado y por libra '
                                 'cocinada; para pasar de ella a esta celda, pondera el precio de cada paquete por sus '
                                 'invitados del año (D105)'),
    (('BBQP', _S, 'C6'), _CASO + '; invitados medios por evento; la mezcla del ejemplo va de drop-off corporativos de 40 a '
                                 'bodas de 130 (guest minimums de los operadores leídos: 30 en eventective.com, 75 en '
                                 'hutchinsbbq.com)'),
    (('BBQP', _S, 'C7'), 'D100: crecimiento de EVENTOS 12 % en el año 2 (reseñas y bodas reservadas con meses; lo limita un '
                         'solo smoker trailer)'),
    (('BBQP', _S, 'C8'), 'D100: crecimiento de EVENTOS 8 % en el año 3, por la misma razón'),
    (('BBQP', _S, 'C11'), 'D103: cuota de BBQ PACKAGES (carnes ahumadas, sides, pan y salsas, personal) 88 %; el resto '
                          '(fila 12) son add-ons: live pit on site, postres, aperitivos, bebidas sin alcohol, alquileres, '
                          'travel fees. Es una ENTRADA'),
    (('BBQP', _S, 'C12'), 'D103: calculado como el resto: BBQ packages + add-ons = 100 %'),
    (('BBQP', _S, 'C13'), 'D100: coste de los BBQ packages 28 % = carne cruda (con la merma del ahumado: el rendimiento '
                          'del brisket y del pork butt ronda el 50 % del peso crudo), sides, pan y salsas, con un '
                          'colchón de sobreproducción (Kit estimate); el food cost de catering va del 28 al 35 % '
                          '(galleysolutions.com)'),
    (('BBQP', _S, 'C14'), 'D100: coste de los add-ons 35 % (Kit estimate: postres y aperitivos comprados, alquileres que '
                          'repercutes casi a coste; el live pit on site es casi todo margen)'),
    (('BBQP', _S, 'C15'), 'D103: desechables + leña, carbón, pellets y propane backup 3.5 % (Kit estimate: desechables '
                          '2.5 % + combustible de cocina 1 %, ≈ 60-100 lb de leña por cocción); escala con las libras y '
                          'los eventos; el combustible del VEHÍCULO va en la fila 27 del P&L'),
    (('BBQP', _S, 'C16'), 'D103: marketplaces de catering corporativo (p. ej. ezCater): 6 % de las ventas en el ejemplo '
                          '(parte del drop-off corporativo)'),
    (('BBQP', _S, 'C17'), 'D103: comisión del marketplace 15 % (ezCater cobra ~15 % sobre comida y entrega: Kit estimate)'),
    (('BBQP', _S, 'C18'), 'D100: tarjeta 3 %: los particulares pagan depósito y saldo con tarjeta; algunas empresas, por '
                          'ACH o cheque'),
    (('BBQP', _S, 'C24'), 'D103: commissary compartida con permiso: horas de producción + almacén frío y seco + '
                          'aparcamiento del smoker trailer DONDE SE PUEDA AHUMAR (en el patio de la commissary, si el '
                          'health department y el fire marshal lo permiten); research: $15-$45 la hora, el 42 % cobra '
                          '$20-$29 (thefoodcorridor.com); nunca «support kitchen»'),
    (('BBQP', _S, 'C25'), 'D103: meses de depósito de la commissary'),
    (('BBQP', _S, 'C26'), 'D103: agua, luz y teléfono que no cubre la commissary; SIN propano: la leña, el carbón y el '
                          'propane backup son variables (fila 15)'),
    (('BBQP', _S, 'C27'), 'D100: seguros al año = general liability / BOP + commercial auto que cubra el remolque + '
                          'workers\' comp + inland marine del smoker (Kit estimate por póliza; Insureon publica medias: GL '
                          '$45/mes, commercial auto $204/mes, insureon.com); los venues piden COI y additional insured; '
                          'liquor liability solo si el cliente pone alcohol y lo sirve tu personal'),
    (('BBQP', _S, 'C28'), 'D103: varios 3 % de las ventas: imprevistos de cada evento (carne extra, hielo, parking en el '
                          'venue); es VARIABLE. SIN combustible: el del vehículo y el remolque va en la fila 27 del P&L '
                          '(fijo) y el de cocina (leña, carbón, propano), en la fila 15'),
    (('BBQP', _S, 'C30'), 'D100: fondos propios del dueño (≈ un cuarto de la necesidad en el ejemplo)'),
    (('BBQP', _S, 'C31'), 'D100: préstamo que calibra el libro: supera el tope de $50,000 del SBA Microloan, así que el '
                          'ejemplo encaja en un SBA 7(a) o un préstamo bancario con garantía; el lender pide plan y '
                          'proyecciones'),
    (('BBQP', _S, 'C33'), 'D100: 7 años: el smoker trailer, la furgoneta y su equipo pierden valor antes que un local'),
    (('BBQP', _S, 'C44'), 'D102: 7 años: smoker trailer y su upfit, furgoneta usada y su upfit, e inspección del trailer '
                          '(la base de vida del vehículo, fila 31 de "Startup Costs")'),
    (('BBQP', _S, 'C45'), 'D102: 5 años: live-fire rig, commissary storage fit-out, software, smallwares & pit tools y '
                          'holding & service equipment'),
    (('BBQP', _S, 'C51'), 'D100: DATO INFORMATIVO (no entra en ningún cálculo): el techo de eventos al año que tu pit y tu '
                          'equipo pueden atender (un smoker trailer; los sábados de mayo-junio y octubre son el cuello de '
                          'botella); compáralo con la fila 4 y con el optimista'),
    (('BBQP', _S, 'C52'), 'D100: rampa 50 % → 8 meses: las bodas se reservan con meses de antelación y las empresas tardan '
                          'en repetir'),
    (('BBQP', _S, 'C54'), 'D100: 1 mes de commissary antes de abrir (test cooks, permisos y preventa en el primer bridal '
                          'show)'),
    (('BBQP', _S, 'C55'), 'D102: imprevistos 10 % sobre smoker trailer, su upfit, furgoneta, su upfit e inspección del '
                          'trailer (filas 7, 8, 11, 12 y 15 de "Startup Costs")'),
    (('BBQP', _S, 'C58'), 'D100: cobro medio 7 días: depósito del 50 % nonrefundable al reservar y saldo entre 72 horas y '
                          '14 días antes del evento; empresas a 30 días; el libro no modela anticipos (nota de la '
                          'Tesorería)'),
    (('BBQP', _S, 'C62'), 'D99/D100: alcohol 0 %: el BBQ caterer no vende alcohol; si el cliente lo pone, que lo sirva un '
                          'servicio con licencia y su propio seguro (docx §9); nunca «bartender» (gate)'),
    (('BBQP', _S, 'C63'), 'D100: solo si vendieras alcohol con licencia (0 % en este plan)'),
    # Startup Costs, notas de la columna D (D102; research §4, §8)
    (('BBQP', _I, 'D7'), 'D102: smoker trailer nuevo clase 500 gal (offset / reverse-flow; leña, carbón o pellets): Meadow '
                         'Creek TS500 $20,395 (webstaurantstore.com); Yoder Frontiersman $8,495-$16,295 + envío '
                         '(yodersmokers.com). El vehículo de arrastre es el del DUEÑO ($0 en el plan): si no lo tienes, '
                         'una pickup usada que remolque ≥ 5,000 lb, comprobado con el peso del trailer cargado (Kit estimate $25,000-$40,000). Nunca «truck»: di '
                         '«tow vehicle» o «pickup»'),
    (('BBQP', _I, 'D8'), 'D102: upfit del trailer: warming cabinet, lavamanos y depósitos de agua si tu condado lo exige '
                         '(cocinar en el evento puede convertirlo en mobile food unit), cajas de almacenaje y luces'),
    (('BBQP', _I, 'D9'), 'D102: live-fire rig para la línea premium: Santa Maria grill, Argentine parrilla, asado crosses '
                         'y La Caja China (pig roast); se amortiza con el equipo'),
    (('BBQP', _I, 'D10'), 'D102: almacén en la commissary: racks, meat lugs y envasadora al vacío'),
    (('BBQP', _I, 'D11'), 'D102: furgoneta de carga usada para drop-off y buffets: lleva las hot boxes; NO es frigorífica '
                          '(la carne cocinada viaja en hot holding ≥ 135 °F; la cruda va del proveedor a la commissary)'),
    (('BBQP', _I, 'D12'), 'D102: upfit de la furgoneta: estanterías, racks, sujeciones y rotulación (wrap)'),
    (('BBQP', _I, 'D13'), 'D102: LLC + contrato tipo revisado por un abogado (depósito del 50 % nonrefundable, tramos de '
                          'cancelación, fuerza mayor por burn ban)'),
    (('BBQP', _I, 'D14'), 'D102: permisos y certificaciones del año 1: catering / health permit del condado, mobile food '
                          'unit o temporary event permits, inspección del fire marshal, business license, sales tax '
                          'permit, ServSafe Manager, food handler cards; varía mucho por estado y condado'),
    (('BBQP', _I, 'D15'), 'D102: plan review / inspección del smoker trailer SOLO si tu condado lo exige (en Texas una '
                          'mobile food unit opera desde una central preparation facility: 25 TAC §228.221); si no, pon 0'),
    (('BBQP', _I, 'D16'), 'D102: software de catering (propuestas, contratos con firma electrónica, depósitos y saldos) + '
                          'lector de tarjetas + tablet'),
    (('BBQP', _I, 'D17'), 'D102: smallwares & pit tools: cuchillos, tablas, hotel pans, termómetros de sonda calibrados, '
                          'butcher paper y foil, guantes de calor; se amortizan'),
    (('BBQP', _I, 'D18'), 'D102: inventario inicial: carne para los test cooks, rubs, salsas, leña y desechables de los '
                          'primeros eventos'),
    (('BBQP', _I, 'D19'), 'D102: web, fotos de la carne y del smoker trailer, altas en The Knot / WeddingWire / Zola / '
                          'ezCater, Google Business Profile y el primer bridal show'),
    (('BBQP', _I, 'D20'), 'D102: holding & service: 6 insulated food carriers, 2 hot boxes, 10 chafing dishes, coolers, '
                          'mesas, carpa (canopy) y tabla de corte para la carving station; nunca «Cambro» (es marca)'),
    (('BBQP', _I, 'D27'), 'D102: lo que compras: smoker trailer, furgoneta y sus upfits, live-fire rig, equipo, '
                          'lanzamiento y constitución; el colchón de caja no es inversión'),
    # 3-Year P&L, notas (D103, D104)
    (('BBQP', _P, 'F10'), 'D103: ventas de BBQ packages por invitado: carnes ahumadas, sides, pan y salsas y el personal '
                          '(drop-off corporativo, fiestas, empresa, bodas, live-fire)'),
    (('BBQP', _P, 'F11'), 'D103: ventas de add-ons: live pit on site (el smoker trailer en el evento, extra de pago), '
                          'postres, aperitivos, bebidas sin alcohol, alquileres, travel fees'),
    (('BBQP', _P, 'F16'), 'D103: comisiones de los marketplaces de catering corporativo (p. ej. ezCater) sobre las ventas '
                          'de ese canal'),
    (('BBQP', _P, 'F22'), 'D103: el importe mensual se teclea en "0. Assumptions"; aquí × 12: commissary + aparcamiento '
                          'del smoker trailer'),
    (('BBQP', _P, 'F24'), 'D103: agua, luz y teléfono que no cubre la commissary; sin propano (va en la fila 15)'),
    (('BBQP', _P, 'F27'), 'D103: combustible, mantenimiento y registro de la furgoneta y del smoker trailer (y del tow '
                          'vehicle cuando arrastra para el negocio): FIJO en este libro'),
    (('BBQP', _P, 'F32'), 'D103: retirada de residuos, grasa y CENIZA con un hauler con licencia (a menudo lo gestiona la '
                          'commissary); la ceniza, fría y en contenedor metálico con tapa'),
    (('BBQP', _P, 'F33'), 'D103: reparación del smoker y del equipo (puertas, juntas, termómetros, ruedas y luces del '
                          'trailer)'),
    (('BBQP', _P, 'F34'), 'D103: ServSafe Manager (Certified Food Protection Manager) y food handler cards del equipo, y su '
                          'renovación'),
    (('BBQP', _P, 'F35'), 'D103: degustaciones para parejas, planners y empresas (carne, sides, horas de pit); muchos '
                          'operadores las descuentan si reservan'),
    (('BBQP', _P, 'F51'), 'D104: suelo del margen bruto del motor 58 % (kit benchmark, editable): el margen bruto del libro '
                          'resta también tarjeta, marketplace y varios'),
    (('BBQP', _P, 'F53'), 'D104: techo del coste de mercancía 35 % (kit benchmark, editable; food cost de catering 28-35 %, '
                          'galleysolutions.com)'),
    (('BBQP', _P, 'F54'), 'D104: techo de personal 38 % (kit benchmark, editable), con el sueldo del dueño dentro'),
    (('BBQP', _P, 'F55'), 'D104: techo de commissary y parking 7 % (kit benchmark, editable): no hay local'),
    (('BBQP', _P, 'F56'), 'D104: suelo del resultado neto 5 % (kit benchmark, editable; neto medio de catering 7-8 %, '
                          'itsacheckmate.com)'),
    # Staffing, notas (D103)
    (('BBQP', _R, 'J5'), 'D103: Owner / Pitmaster & Sales: vende, hace las degustaciones, lleva el pit y la carving station '
                         'en las bodas; el resto de su retribución sale del beneficio'),
    (('BBQP', _R, 'J6'), 'D103: pit cook / lead cook (W-2, 0.75 FTE): cocción nocturna con sonda y hot holding; un pit cook '
                         'vigila varias piezas a la vez; paga ≈ p75 de «cooks, restaurant» (BLS OEWS mayo 2025)'),
    (('BBQP', _R, 'J7'), 'D103: event staff por horas y en W-2 (servers, buffet attendants, carvers); su FTE es una '
                         'fracción; ≈ 1 por 25-30 invitados en buffet (Kit estimate); la gratuity voluntaria es suya'),
    (('BBQP', _R, 'J8'), 'D103: prep cook / driver part-time W-2: rubs y porcionado en la commissary, carga y conducción de '
                         'la furgoneta'),
    (('BBQP', _R, 'J18'), 'D100: horas por persona y evento: porcionado, cocción nocturna (repartida), carga, viaje, '
                          'montaje, 2-3 h de servicio y recogida'),
    (('BBQP', _R, 'J19'), 'D100 (M6 de REVISION-FINAL): personas por evento: drop-off 1.5 · buffet de 70 3 · empresa '
                          'full-service 5 · boda con live pit 7 (2 en el pit + 5 servers, como el ejemplo de la calculadora) · '
                          'live-fire 5 (Kit estimate); ponderado con la mezcla del docx, ≈ 3.4'),
    (('BBQP', _ES, 'E23'), 'D100: la MISMA plantilla en los tres escenarios; en el pesimista el coste real del event staff '
                           'baja con los eventos (pagas horas por evento), así que el resultado real sería algo mejor'),
    (('BBQP', _N, 'A5'), 'D99: «0. Assumptions» es la hoja de mando: eventos al año, precio por invitado sin sales tax, '
                         'invitados por evento, mezcla BBQ packages / add-ons, coste de mercancía; nunca «van» '
                         'frigorífica: smoker trailer + furgoneta de carga'),
    (('BBQP', _N, 'A12'), 'SPEC §4.1 línea 8 (I1): el Word del kit usa las MISMAS cifras de ejemplo que este libro; si '
                          'cambias el libro, actualiza las del Word. La calculadora de precios es otro fichero (con su '
                          'Meat Yield & Smoke Schedule y su Shopping List) y no lee este libro'),
])
_D18 = ('D18 (BBQ caterer): la propuesta es la del Catering EN publicado, que ya describe el MÉTODO del libro para un '
        'negocio de eventos con comida; reescribe SOLO lo que hable de van frigorífica, generador, quemadores, estaciones, '
        'chef o emplatado → smoker trailer + furgoneta de carga, commissary, pitmaster, carving station. Sin cifras del '
        'caso')
_D18_FILA = OrderedDict([
    (39, 'Fila del espacio: «Commissary kitchen and smoker trailer parking» (el coste del espacio, en "0. Assumptions")'),
    (42, 'Fila de seguros del vehículo: los del smoker trailer y la furgoneta (commercial auto que cubre el remolque, '
         'inland marine), una sola vez y como gasto anual'),
    (43, 'Fila de combustible de cocina (D103): «Wood, charcoal and propane backup»: va en la línea de desechables, leña '
         'y combustible de cocina (variable, % de ventas), no en utilities ni en una línea aparte'),
    (49, 'Fila «Fuel and miscellaneous» (D103; M6 del bar móvil): A «Miscellaneous event costs» · B «A miscellaneous line '
         'typed in among the fixed costs» · C «A percentage of sales, treated as a variable cost; vehicle and trailer '
         'fuel has its own fixed line» · D «Extra meat, ice and venue parking rise and fall with the number of events: '
         'among the fixed costs they would distort the break-even.»'),
])
for _f in range(35, 52):
    for _col in 'ABCD':
        CELDA_PISTAS[('BBQP', _N, '%s%d' % (_col, _f))] = _D18 + ('. ' + _D18_FILA[_f] if _f in _D18_FILA else '')
PISTA_D19_GENERICA = ('Celda a celda: escribe SOLO el texto de ESTA celda (una tabla o una tarea): mira su pista '
                      'propia')
_D19_BASE = ('D19/D104: tabla «US BBQ CATERING BENCHMARKS (sourced) AND KIT ESTIMATES» (Benchmark | Value | Source | '
             'Note). Value en formato US; Source = el DOMINIO de la fuente LEÍDA de research §4-§5, o «Kit estimate» si '
             'allí figura como «(resumen)». Esta fila: ')
_D19 = OrderedDict([
    (55, 'precio por persona según el servicio (Kansas City, 2023): drop-off «$15-$30 per person» (el del operador, desde '
         '$17.50) y full-service «up to $75» — q39kc.com'),
    (56, 'un operador Texas-style de Los Angeles: fiestas $40-58 y bodas $65-85 por invitado, mínimo 30 invitados, event '
         'fee $1,000-$1,200 — eventective.com (Owen\'s BBQ)'),
    (57, 'carne por invitado: «one-third to one-half pound of meat per guest» (hutchinsbbq.com); «6-8 oz» con 2-3 carnes '
         '(sonnybryans.com); ¼-⅓ lb cocinada como suelo (fieryfoodscentral.com, Dr. BBQ) — fuentes leídas'),
    (58, 'margen neto 7-8 % de media en catering — itsacheckmate.com [propuesta del catering: revisa que hable de '
         'catering en general y sirva para un BBQ caterer]'),
    (59, 'rendimiento del ahumado: «yield will be about 50% of the fresh weight» (brisket y pork butt); 300 invitados ≈ '
         '200 lb crudas — fieryfoodscentral.com'),
    (60, 'food cost de catering 28-35 % del precio — galleysolutions.com'),
    (61, 'smoker trailer: offset en trailer Yoder Frontiersman $8,495 / $11,295 / $16,295 + envío (yodersmokers.com); '
         'Meadow Creek TS500 de 500 gal $20,395 (webstaurantstore.com)'),
    (62, 'comisión de marketplace corporativo ~15 % (ezCater) — Kit estimate [propuesta del catering]'),
    (63, 'depósito: 50 % nonrefundable para reservar la fecha; saldo 72 h antes (fiestas) o 14 días antes (bodas) — '
         'eventective.com (Owen\'s BBQ) · hutchinsbbq.com [la propuesta del catering decía 25-50 %: cámbiala]'),
    (64, 'sueldos BLS OEWS mayo 2025: cooks, restaurant (35-2014) media $18.62/h, p75 $21.45; food servers, '
         'nonrestaurant (35-3041) media $17.37/h, p75 $18.51; chefs and head cooks (35-1011) mediana $30.03/h — bls.gov '
         '(ÚNICA celda del kit donde vale «chefs and head cooks»)'),
    (65, 'commissary compartida $15-$45 la hora (el 42 % cobra $20-$29) — thefoodcorridor.com (2023 Shared Kitchen '
         'Operator Survey) [propuesta del catering]'),
    (66, 'mínimos de invitados: 30 (eventective.com, Owen\'s BBQ), 75 en full catering y 20 en delivery '
         '(hutchinsbbq.com); comida desde $28 por persona con mínimo de $500 (zola.com, Heim BBQ)'),
    (67, 'seguros (Insureon, < 5 empleados): general liability $45/mes, BOP $96, workers\' comp $82, commercial auto $204 '
         '— insureon.com [propuesta del catering: añade workers\' comp y BOP si faltan; liquor liability solo si aplica]'),
    (68, 'leña y personal: ≈ 60-100 lb de leña por cocción; ≈ 1 server por 25-30 invitados en buffet — Kit estimate'),
])
for _f, _p in _D19.items():
    for _col in 'ABCD':
        CELDA_PISTAS[('BBQP', _N, '%s%d' % (_col, _f))] = _D19_BASE + _p

# Checklist (D107): una pista por FILA de tarea (columnas B tarea · C responsable · D plazo · E nota práctica). La
# propuesta EN es la tarea del catering en ESA celda: «[sobrevive]» = vale casi literal (L), «[sobrevive con ajuste]» =
# cambio de palabras (A), «[nueva]» = tarea distinta, la propuesta NO vale (N). F1-inventario §5
_CK = ('D107: escribe una TAREA de un BBQ caterer off-site (B tarea · C responsable · D plazo · E nota práctica, una celda '
       'cada vez) con el checklist ES del parrillero (fuente_es_bbq.json) + research §6 y el glosario §9; columna C: '
       '«Executive chef» → «Pitmaster»; plazos US («Week 1», «3 weeks out», nunca «D-21»); ' + REGLA_UNIDADES + '. '
       'Esta fila: ')
TAREAS_BBQ = OrderedDict([
    ('F1 - Constitución', [                                  # M2 y m9 de REVISION-FINAL: contador en la semana 1, préstamo en la fila 12
        'contador / bookkeeper y estimated taxes trimestrales (semana 1) [sobrevive]',
        'estructura: LLC, con o sin elección de S corp, con tu contador (ES: autónomo / SL) [sobrevive]',
        'registrar la LLC en el Secretary of State + registered agent + operating agreement [sobrevive]',
        'EIN gratis en el IRS para la LLC + alta estatal de nóminas y desempleo (vas a tener personal W-2) [sobrevive]',
        'cuenta bancaria del negocio y finanzas separadas [sobrevive]',
        'seller\'s permit / sales tax permit del estado: en muchos estados tributa toda la factura de catering (comida, '
        'personal, alquileres y, según el estado, el service charge) [sobrevive]',
        'business license de la ciudad o el condado (+ DBA si usas nombre comercial) [sobrevive]',
        'solicitar el préstamo a dos lenders (banco o SBA 7(a)) con el plan, el Excel y los presupuestos del trailer y la '
        'van; no firmar el trailer antes de la aprobación [nueva: el software pasa a P5 fila 14]',
        'contrato tipo con un abogado: depósito del 50 % nonrefundable, saldo entre 72 h y 14 días antes, tramos de '
        'cancelación sin huecos, variación de invitados y guest minimum, service charge frente a gratuity, fuerza mayor '
        'por burn ban (propane backup o nueva fecha), uso de fotos [sobrevive con ajuste del contenido]',
        'plan de seguridad alimentaria basado en HACCP para carnes ahumadas: cocinar a 145 °F (intactas), 155 °F '
        '(inyectadas, ablandadas o picadas, sausage incluida: inyectar un brisket lo vuelve non-intact) y 165 °F (aves); '
        'hot holding ≥ 135 °F; enfriado a 70 °F en 2 h y a 41 °F en 6 h en total; recalentado a 165 °F (FDA Food Code '
        '3-401.11, 3-501.16, 3-501.14, 3-403.11); la temperatura de calidad (brisket ≈ 203 °F) es otra cosa '
        '[sobrevive con ajuste]',
        'Certified Food Protection Manager (ServSafe Manager) del dueño / pitmaster [sobrevive]',
    ]),
    ('F2 - Vehículo', [
        'elegir una commissary compartida con permiso: horas, almacén frío y seco, aparcamiento del smoker trailer DONDE '
        'SE PUEDA AHUMAR y sitio para la leña (visita y precios); nunca cocina de casa: FDA Food Code 3-201.11(B), y el '
        'cottage food excluye la carne (Texas) [sobrevive con ajuste]',
        'commissary agreement por escrito (lo exige el health department) [sobrevive]',
        'catering / health permit del condado + pregunta si ahumar o servir desde el trailer en el evento lo convierte '
        'en mobile food unit (Texas, 25 TAC §228.221: opera desde una central preparation facility; Florida y North '
        'Carolina, parecido): «ask your county»; si no hay permiso, ahúma en la commissary y lleva la carne en hot boxes '
        '[sobrevive con ajuste]',
        'temporary food event permits para eventos comunitarios o públicos [sobrevive]',
        'fire marshal: solid fuel cooking (BBQ pits) con extintor Class K + 2A:10BC, 10 ft de separación, propano ≤ 200 '
        'lb (IFC 906.4.1 y 319.8.1, según los adopte tu ciudad); burn bans y cocina bajo carpas: «check with your fire '
        'marshal» (sin cifras no verificadas) [sobrevive con ajuste]',
        'comprar el smoker trailer (offset / reverse-flow, clase 500 gal, nuevo) y la furgoneta de carga usada, con '
        'inspección; el tow vehicle es tu pickup: comprueba que puede remolcar el trailer [nueva: la propuesta del '
        'catering habla de una van frigorífica]',
        'título y registro del trailer y de la furgoneta en el DMV + commercial auto que cubra el remolque + inland '
        'marine para el smoker y el equipo en tránsito [nueva]',
        'upfit: el trailer (warming cabinet, lavamanos y depósitos si el condado lo exige, cajas, luces) y la furgoneta '
        '(estanterías, sujeciones, wrap) [nueva]',
        'general liability o BOP; COI y «additional insured» que piden los venues [sobrevive]',
        'liquor liability SOLO si el cliente pone alcohol y lo sirve tu personal; lo normal es que el cliente contrate un '
        'servicio de bar con licencia y su propio seguro [sobrevive con ajuste]',
        'workers\' comp antes del primer empleado [sobrevive]',
        'residuos, grasa y CENIZA con un hauler con licencia (a menudo vía commissary); la ceniza, fría y en contenedor '
        'metálico con tapa [sobrevive con ajuste]',
        'control de plagas con empresa con licencia (vía commissary) y avisos obligatorios [sobrevive]',
    ]),
    ('F3 - Equipamiento', [
        'lista de equipo propio frente a alquilado (party rentals) por paquete: drop-off, staffed buffet y live-fire '
        'premium [sobrevive con ajuste]',
        'insulated food carriers, hot boxes y termómetros de sonda calibrados (nunca «Cambro» en el texto: es marca) '
        '[sobrevive con ajuste]',
        'el smoker del trailer, el live-fire rig (Santa Maria grill, Argentine parrilla, asado crosses, La Caja China) y '
        'el propane backup: prueba de temperatura de cada cámara [nueva]',
        'hotel pans, sheet pans y utensilios [sobrevive]',
        'proveedor de carne de origen autorizado (approved source: inspección USDA o estatal; el whole hog nunca custom '
        'exempt, que va marcado «not for sale») + cash-and-carry tipo Restaurant Depot; pedido 5-7 días antes '
        '[sobrevive con ajuste]',
        'carving station: tabla, cuchillos, guantes, lámpara de calor y el guion del corte delante del invitado [nueva]',
        'proveedor de leña (post oak, hickory; red oak para Santa Maria) y carbón: seca, por cord, guardada lejos del '
        'fuego [nueva]',
        'acuerdo con una empresa de party rentals (mesas, mantelería, vajilla) con tarifa pactada [sobrevive]',
        'desechables y envases para drop-off (butcher paper, foil, bandejas) [sobrevive]',
        'registros de temperatura en el transporte (data logger) [sobrevive]',
        'montar el espacio en la commissary: estanterías, etiquetado, FIFO [sobrevive]',
        'test cook completo con el equipo: cocción nocturna, hot holding, carving y un yield test (libras crudas frente '
        'a cocinadas por corte) para afinar la calculadora [sobrevive con ajuste]',
    ]),
    ('F4 - Personal', [
        'plan de personal por evento según el paquete: ≈ 1 server o buffet attendant por 25-30 invitados en buffet, '
        'pitmaster y carver en full-service (Kit estimate) [sobrevive con ajuste]',
        'pool de event staff en nómina W-2 (nunca 1099 ni «freelance»: FLSA; California AB5) [sobrevive]',
        'offer letters, I-9 y W-4; salario mínimo estatal [sobrevive]',
        'new-hire reporting al estado [sobrevive]',
        'proveedor de nóminas y workers\' comp en marcha [sobrevive]',
        'food handler cards de todo el equipo [sobrevive]',
        'seguridad del fuego: extintores (Class K y 2A:10BC), manejo del propano, apagado y ceniza, y quién vigila el pit '
        'durante el servicio [nueva: sustituye a la certificación de alcohol de los bartenders]',
        'OSHA basics: calor y humo, quemaduras, cargas pesadas (carne, leña) y conducción con remolque [sobrevive con '
        'ajuste]',
        'formación de servicio: guion de la carving station y del live-fire, uniforme, briefing y los 9 alérgenos '
        'mayores (rubs, salsas y sides) [sobrevive con ajuste]',
        'política de service charge y gratuity (IRS Rev. Rul. 2012-18: el service charge obligatorio es salario) '
        '[sobrevive]',
    ]),
    ('F5 - Marketing', [
        'marca, logo, menú por estilos regionales (Texas, Carolina, Kansas City, Memphis, Santa Maria, Argentine asado) '
        'y fotos profesionales de la carne y del smoker trailer [sobrevive con ajuste]',
        'web con paquetes, precios «desde» por invitado y formulario de presupuesto [sobrevive]',
        'Google Business Profile y reseñas [sobrevive]',
        'perfiles en The Knot, WeddingWire y Zola (ES: Bodas.net) [sobrevive con ajuste]',
        'ezCater para el drop-off corporativo (+ Thumbtack para fiestas privadas) [sobrevive con ajuste]',
        'prospección B2B: office managers, HR y event planners [sobrevive]',
        'acuerdos con venues y wedding planners (preferred vendor lists) [sobrevive]',
        'política de degustaciones para prospectos [sobrevive]',
        'Instagram y redes con fotos y vídeo del pit (ES: WhatsApp → texto / SMS) [sobrevive]',
        'plantilla de presupuesto con la calculadora del kit (libras por invitado, smoke schedule y shopping list), '
        'seguimiento en el CRM y software de catering que envía la propuesta, firma y cobra el depósito [sobrevive con '
        'ajuste]',
        'programa de referidos y reseñas después de cada evento [sobrevive]',
        'tasting / pop-up de lanzamiento para planners, venues y empresas + el primer bridal show local [nueva]',
    ]),
    ('F6 - 90 Días', [
        'llamada final de planificación con el cliente 3 semanas antes («3 weeks out»): invitados, paquete, estilo regional, alergias y hora '
        'de servicio [sobrevive con ajuste: fuera el calco «D-21»]',
        'visita o llamada técnica al venue 2 semanas antes: dónde va el smoker trailer o la carving station, acceso, '
        'suelo, agua y normas de fuego del venue [sobrevive con ajuste: fuera «D-14»]',
        'saldo cobrado antes del evento (entre 72 h y 14 días según el contrato) y factura de extras en 48 h; control de '
        'depósitos [sobrevive con ajuste]',
        'pedido de carne 5-7 días antes (libras crudas de la calculadora) y rubs, trimming y porcionado en la '
        'commissary 1-2 días antes, con el plan de ahumado («Start the pit by» de la calculadora) [sobrevive con ajuste: '
        'fuera «D-7 / D-1»]',
        'cocción con sonda, reposo, hot holding ≥ 135 °F en hot boxes y checklist de carga y transporte con '
        'temperaturas [sobrevive con ajuste]',
        'montaje 60-90 min antes, carving station y servicio; el pit en el evento solo si el permiso lo cubre '
        '[sobrevive con ajuste]',
        'recogida, limpieza, ceniza fría y devolución de alquileres [sobrevive]',
        'pedir reseña y fotos; seguimiento en el CRM [sobrevive]',
        'revisión semanal del yield real (libras crudas frente a cocinadas), el food cost y las horas de personal por '
        'evento frente a la calculadora [sobrevive con ajuste]',
        'revisión a los 90 días: precio por invitado, guest minimums y paquetes [sobrevive]',
    ]),
])
for _h, _ts in TAREAS_BBQ.items():
    for _k, _t in enumerate(_ts):
        for _col in 'BCDE':
            CELDA_PISTAS[('BBQC', _h, '%s%d' % (_col, 5 + _k))] = _CK + 'fase %s, tarea %d/%d: %s' % (
                _h[1], _k + 1, len(_ts), _t)

# Pistas por TEXTO propias del BBQ (se suman a las de extraer_textos.PISTAS)
PISTAS_EXTRA = [
    (r'^Días fuera de rango$|^Los días van de 1 a 365', 'D101: esta validación cubre a la vez B6 (INVITADOS por evento), '
                                                         'B58/B59 (días de cobro y de pago) y los invitados de '
                                                         'Escenarios: un texto que valga para todos'),
    (r'[Cc]lientes?|[Tt]icket|[Dd]ías de apertura|al día|por día',
     'D101: motor de eventos: «events per year» (B4), «price per guest» (B5), «guests per event» (B6); nunca «customers», '
     '«per day» ni «operating days» (gate)'),
    (r'[Vv]ehícul|[Ff]ood ?[Tt]ruck|[Cc]amión|[Rr]emolque', 'D99/D102: el smoker trailer (lo arrastra la pickup del dueño, '
                                                            '«tow vehicle») y la furgoneta de carga usada; nunca «truck» '
                                                            '(gate; «BBQ food trucks» solo para el competidor)'),
    (r'[Vv]entanilla|[Ff]estival|[Mm]ercados|[Aa]mbulante|[Cc]alle', 'D99: BBQ catering en el evento del cliente; sin '
                                                                     'ventanilla, festivales, mercados ni venta '
                                                                     'ambulante (gate)'),
    (r'[Aa]parcamiento|base del vehículo|comisar', 'Glosario: «commissary kitchen & smoker trailer parking»; nunca '
                                                   '«support kitchen»'),
    (r'[Gg]enerador|gas\b|propano', 'D103: el combustible de COCINA (leña, carbón, pellets, propane backup) es variable '
                                    '(fila 15); el del vehículo y el remolque, fijo (fila 27); el caso no tiene generador'),
    (r'[Dd]elivery|[Gg]lovo|[Uu]ber', 'D103: marketplaces de catering corporativo (p. ej. ezCater), no apps de delivery'),
    (r'[Cc]omida|[Cc]ocina|[Mm]enú|COMIDA', 'D99/D103: smoked meats, sides, BBQ packages y add-ons; «food» y «menu» valen; '
                                            'nunca «chef» (di pitmaster o pit cook), «plated» ni «stations» salvo '
                                            '«carving station» (gate)'),
    (r'm²|m2\b|\bkg\b|\bkm\b|[Ll]itros?\b|\b\d+ ?L\b|\bml\b|°C|ºC', REGLA_UNIDADES),
    (r'[Ee]ventos?|[Bb]odas?', 'Glosario §9: BBQ catering, pitmaster, drop-off, staffed buffet, full-service, live pit on '
                               'site, weddings, corporate events / holiday parties, private parties, graduation parties'),
]

# Glosario de research §9 (OBLIGATORIO: regla de jerga §0), entero. Se suma al de FT/CAF y al del financial-kit
GLOSARIO_BBQ = OrderedDict([
    ('empresa de parrilla para eventos', 'BBQ catering company / BBQ caterer («barbecue» solo como variante)'),
    ('maestro parrillero (dueño)', 'pitmaster («Owner / Pitmaster & Sales»; nunca «grill master»)'),
    ('BBQ pit con hogar lateral', 'offset smoker (offset firebox) · reverse-flow · stick burner (solo en prosa)'),
    ('remolque-parrilla', 'smoker trailer'),
    ('combustible', 'solid fuel (wood, charcoal, pellets) · pellet smoker'),
    ('leña de roble', 'post oak (TX) · hickory · red oak (Santa Maria)'),
    ('cocción lenta', 'low and slow'),
    ('pecho entero · punta · parte magra', 'packer brisket · point · flat'),
    ('puntas caramelizadas', 'burnt ends (Kansas City)'),
    ('paleta de cerdo desmigada', 'pulled pork (pork butt / shoulder)'),
    ('costillar', 'spare ribs · St. Louis style · baby backs'),
    ('adobo seco · corteza · anillo de humo', '(dry) rub · bark · smoke ring'),
    ('meseta · envolver', 'the stall · the wrap / Texas crutch (foil o butcher paper)'),
    ('reposo y mantenimiento', 'resting · holding en insulated food carriers / hot boxes («Cambro» es marca: no en '
                               'rótulos)'),
    ('mantener caliente (norma)', 'hot holding at 135 °F (Food Code 3-501.16)'),
    ('enfriar · recalentar', 'cooling (to 70 °F within 2 hours and to 41 °F within a total of 6 hours) · reheating for '
                             'hot holding (165 °F)'),
    ('merma / rendimiento', 'yield («about 50% of the fresh weight») · shrink'),
    ('gramos por invitado', 'pounds of meat per guest («one-third to one-half pound»); lb crudas en la calculadora'),
    ('precio por invitado · mínimo', 'per person / per guest · guest minimum'),
    ('entrega sin servicio', 'drop-off · Drop & Set · delivered ready to serve'),
    ('servicio completo', 'full-service (setup, service, cleanup)'),
    ('buffet con personal', '(staffed) buffet · tend the buffet'),
    ('corte al momento', 'carving station · carving to order'),
    ('parrilla en el evento', 'live pit on site · on-site pit (add-on premium, no la base)'),
    ('guarniciones', 'sides (mac and cheese, potato salad, coleslaw, collard greens, baked beans)'),
    ('bandejas', 'chafing dishes · buffet trays · boxed BBQ lunches'),
    ('señal · cargo del evento', 'deposit («50% nonrefundable») · event fee / service fee (≠ gratuity)'),
    ('cocina de apoyo', 'commissary / central preparation facility (nunca «support kitchen»)'),
    ('remolque que cocina en el evento', 'mobile food unit (TX) · mobile food dispensing vehicle (FL) · mobile food '
                                         'facility (CA), según el estado'),
    ('autorización puntual', 'temporary food establishment permit (CA: TFF)'),
    ('origen autorizado', 'approved source · USDA-inspected · «custom exempt… not for sale» (whole hog)'),
    ('extintor', 'Class K extinguisher (2.5 gallons para solid fuel) + 2A:10BC'),
    ('asado argentino', 'Argentine asado · parrilla · chimichurri'),
    ('parrilla de altura regulable', 'Santa Maria grill · tri-tip over red oak'),
    ('cochinillo / caja china', 'pig roast · whole hog · La Caja China · lechón'),
    ('estilos regionales', 'Texas · Kansas City · Memphis · Carolina («four types of BBQ»)'),
    # (e) no se traducen literalmente
    ('parrillero', 'pitmaster (persona) o BBQ caterer (negocio)'),
    ('asador', 'asado cross o spit roast; nunca «roaster» como negocio'),
    ('brasa', 'live fire / coals'),
    ('autónomo', 'single-member LLC'),
    ('fijo discontinuo / freelance', 'part-time hourly W-2 staff'),
    ('carnet de manipulador', 'food handler card'),
    ('APPCC', 'HACCP-based food safety plan'),
    ('plan B de gas', 'propane backup'),
    ('época de peligro', 'county burn ban'),
    ('chuletón', 'bone-in ribeye / tomahawk'),
    ('picaña', 'picanha'), ('entraña', 'skirt steak'), ('vacío', 'flank / bavette'),
    ('provoleta', 'grilled provolone'), ('finca', 'venue (ranch, barn venue)'), ('IVA', 'sales tax'),
    ('señal', 'deposit'), ('escandallo', 'cost per guest / food cost'),
    ('medidas (John, 13-oct)', 'US customary first, metric in parentheses: lb / oz (kg), °F (°C), gallons (liters), '
                               'miles, sq ft (sq m)'),
])


# ==========================================================================
# Caso de ejemplo US (D100; research §8 tal cual): celdas VERDES del FT. (corto, hoja ES, celda) → (valor, rótulo ES)
# ==========================================================================
def valores_bbq(M):
    v = OrderedDict()
    sup = [
        ('B4', 150, 'Clientes/día'), ('B5', 38, 'Ticket medio'), ('B6', 75, 'Días de apertura'),
        ('B7', 0.12, 'Crecimiento de volumen del año 2'), ('B8', 0.08, 'Crecimiento de volumen del año 3'),
        ('B11', 0.88, 'Ventas de COMIDA'), ('B13', 0.28, 'Coste de mercancía sobre las ventas de COMIDA'),
        ('B14', 0.35, 'Coste de mercancía sobre las ventas de BEBIDA'), ('B15', 0.035, 'Consumibles'),
        ('B16', 0.06, 'Ventas por delivery'), ('B17', 0.15, 'Comisión de la plataforma'),
        ('B18', 0.03, 'Comisión de los medios de pago'), ('B20', 0.10, 'Seguridad Social'),
        ('B21', 12, 'Número de pagas'), ('B22', 15080, 'SMI anual'), ('B24', 1800, 'Alquiler mensual'),
        ('B25', 1, 'Fianza'), ('B26', 150, 'Suministros'), ('B27', 6000, 'Seguros'), ('B28', 0.03, 'Varios'),
        ('B30', 35000, 'Recursos propios'), ('B31', M.CALIBRAR, 'Préstamo bancario'), ('B32', 0.10, 'Tipo de interés'),
        ('B33', 7, 'Plazo del préstamo'), ('B34', 0, 'Carencia'), ('B35', 3, 'Fondo de maniobra'),
        ('B37', 0.25, 'Impuesto de Sociedades, nueva'), ('B38', 0.25, 'Impuesto de Sociedades, tipo'),
        ('B39', 0.08, 'IVA repercutido de restauración'), ('B40', 0.08, 'IVA repercutido/soportado'),
        ('B41', 0, 'IVA soportado en compras'), ('B42', 0, 'Bases negativas'),
        ('B44', 7, 'Vida útil de obra'), ('B45', 5, 'Vida útil de maquinaria'), ('B48', 0, 'Subida anual'),
        ('B51', 220, 'Plazas de pie'), ('B52', 0.50, 'Actividad del mes 1'), ('B53', 8, 'Meses hasta alcanzar'),
        ('B54', 1, 'Meses de alquiler del aparcamiento'), ('B55', 0.10, 'Imprevistos sobre las partidas'),
        ('B58', 7, 'Días medios de cobro'), ('B59', 7, 'Días medios de pago'),
        ('B62', 0, 'Bebida ALCOHÓLICA'), ('B63', 0.08, 'IVA de la bebida ALCOHÓLICA'),
        ('B65', 1.15, 'DSCR mínimo'), ('B66', 1.25, 'DSCR objetivo'), ('B67', 0.15, 'Holgura mínima'),
        ('B68', None, 'Suelo salarial anual'),
    ]
    for c, val, rot in sup:
        v[('BBQP', _S, c)] = (val, rot)
    # Inversión (D102; orden del inventario §3, importes de research §8): filas 7-20 (rótulos ES del FT) = $75,200
    for k, (val, rot) in enumerate([
            (20000, 'Vehículo'), (3500, 'Adaptación'), (4500, 'Equipamiento cocina'), (1500, 'Generador'),
            (18000, 'Instalación gas'), (3000, 'Depósito de agua'), (1500, 'Constitución'), (2500, 'Licencias'),
            (500, 'Proyecto técnico'), (1200, 'TPV'), (3500, 'Menaje'), (4000, 'Stock'), (5000, 'Marketing'),
            (6500, 'Toldo')]):
        v[('BBQP', _I, 'B%d' % (7 + k))] = (val, rot)
    # P&L: fijos B26-B35 (research §8: $30,300) y umbrales D104 [kit benchmark]
    for k, (val, rot) in enumerate([
            (1200, 'Permisos'), (6000, 'Mantenimiento'), (10000, 'Marketing'), (3000, 'Gestoría'), (2400, 'Software'),
            (2400, 'Limpieza'), (1200, 'Gestión de residuos'), (1500, 'Desinsectación'), (600, 'Prevención'),
            (2000, 'Derechos de autor')]):
        v[('BBQP', _P, 'B%d' % (26 + k))] = (val, rot)
    for c, val, rot in [('E51', 0.58, 'Margen bruto'), ('E53', 0.35, 'Coste de mercancía /'),
                        ('E54', 0.38, 'Coste de personal'), ('E55', 0.07, 'Aparcamiento'), ('E56', 0.05, 'Resultado neto')]:
        v[('BBQP', _P, c)] = (val, rot)
    # Staffing (D103; research §8): personas (B), FTE por persona (C), bruto mes TOTAL de la fila (D) = $10,582/mes
    for f, (b, c, d) in zip(range(5, 9), [(1, 1.0, 4507), (1, 0.75, 2730), (6, 0.10, 1872), (1, 0.5, 1473)]):
        for col, val in zip('BCD', (b, c, d)):
            v[('BBQP', _R, '%s%d' % (col, f))] = (val, None)
    v.update([
        (('BBQP', _R, 'B11'), (5000, 'Coste anual')), (('BBQP', _R, 'B12'), (5000, 'Coste anual')),
        (('BBQP', _R, 'B16'), (40, 'Jornada completa')), (('BBQP', _R, 'B17'), (50, 'Semanas')),
        (('BBQP', _R, 'B18'), (10, 'Horas de servicio')), (('BBQP', _R, 'B19'), (3.4, 'Personas necesarias')),
    ])
    # Escenarios (research §8): −25 % / +25 % de eventos, −10 % / +10 % de precio e invitados
    v.update([
        (('BBQP', _ES, 'B5'), (113, 'Clientes/día')), (('BBQP', _ES, 'D5'), (188, 'Clientes/día')),
        (('BBQP', _ES, 'B6'), (34.2, 'Ticket')), (('BBQP', _ES, 'D6'), (41.8, 'Ticket')),
        (('BBQP', _ES, 'B7'), (68, 'Días')), (('BBQP', _ES, 'D7'), (83, 'Días')),
    ])
    # Estacionalidad (research §8, Kit estimate): apertura en MARZO → Month 1-12 (suma 100 %)
    for col, val in zip('BCDEFGHIJKLM', (0.065, 0.09, 0.12, 0.115, 0.09, 0.075, 0.10, 0.11, 0.07, 0.09, 0.035, 0.04)):
        v[('BBQP', _T, '%s5' % col)] = (val, 'Estacionalidad')
    return v


# Calibración D15 (SPEC D100): holgura ≥ 15 %; si no, B4 de 10 en 10 hasta 170; si la caja mínima ≤ 0 por la rampa,
# B35 3 → 4 antes de tocar el precio. Cada celda, citada en F2-NOTAS §3 (G7). Se rellena con el dry-run del paso 1
CALIBRACION_D15 = OrderedDict()


# ==========================================================================
# FORMULAS_EN: las del FT con la fila del Break-Even, las notas de las líneas de venta y las listas de la inversión
# ==========================================================================
_PE_BBQ = ('=IFERROR("With the average price per guest excl. sales tax above, you need "&TEXT(ROUNDUP(B15,0),"0")&" '
           'events a year at your average of "&TEXT(B11,"0")&" guests per event to avoid losing money (accounting '
           'break-even, depreciation included), and "&TEXT(ROUNDUP(B20,0),"0")&" for cash to hold (cash break-even: '
           'depreciation out, because it is not paid, and the year\'s loan payment in"&IF(B12=0,"; no principal is '
           'repaid this year (interest-only period or no loan)","")&"). The ""Revenue needed per year"" rows show the '
           'same figures in your currency.","")')
_C9_BBQ = ('=IFERROR("Price per guest excl. sales tax plus the weighted sales tax of your sales lines ("&TEXT('
           "SUMPRODUCT('3-Year P&L'!$E$10:$E$11,'3-Year P&L'!$G$10:$G$11)*100,\"0\")&\"%), rounded. In the US the "
           'quote adds sales tax on top, and many states tax the whole catering invoice (food, staff, rentals and the '
           'service charge); in the UK, VAT is included in the price.","")')
_F18_BBQ = ('=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$28,"0%")&" of sales: a cushion for unbudgeted event costs (extra '
            'meat, ice, venue parking). It is a VARIABLE cost: it moves with the number of events, so it cannot sit in '
            'fixed costs (vehicle and trailer fuel, maintenance and registration are in row 27; wood, charcoal and '
            'propane are in row 15)","")')
_F13_BBQ = ('=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$13,"0%")&" of BBQ PACKAGE sales (raw meat, sides, bread and '
            'sauces), not of total sales: add-ons have their own line","")')
_F14_BBQ = '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$14,"0%")&" of ADD-ON sales","")'


def formulas_bbq():
    sys.path.insert(0, BP)
    import formulas_en as F                                                    # noqa: E402
    out = OrderedDict()
    for h, d in F._COMUNES.items():
        for c, f in d.items():
            out[('BBQP', h, c)] = f
    out[('BBQP', _S, 'C9')] = _C9_BBQ
    out[('BBQP', _P, 'F18')] = _F18_BBQ
    out[('BBQP', _P, 'F13')] = _F13_BBQ
    out[('BBQP', _P, 'F14')] = _F14_BBQ
    o11 = out[('BBQP', _T, 'O11')]
    assert 'Food and beverage purchases, consumables' in o11
    out[('BBQP', _T, 'O11')] = o11.replace('Food and beverage purchases, consumables',
                                           'Meat, sides and add-on purchases, disposables and cooking fuel')
    out[('BBQP', _E, 'A26')] = _PE_BBQ
    for c, f in F._inversion('D21', 'D22', 'D23', 'D25', 'D26', 'D28', 'D31', 'D32', 'D33', 24, 26, 31, 32,
                             'smoker trailer, smoker trailer upfit, used cargo van, van upfit and the plan review / '
                             'trailer inspection',
                             'LLC formation and legal, first-year permits and certifications, opening inventory, '
                             'website, photos and launch, the commissary deposit, pre-opening commissary rent and the '
                             'working capital reserve').items():
        out[('BBQP', _I, c)] = (f.replace('when the lease ends', 'when the commissary agreement ends')
                                .replace(' of build-out and permits before opening', ' of test cooks, permits and '
                                         'pre-sales before opening'))
    return out


def _importes_research():
    """Importes en dólares ≥ 10,000 que cita la research del BBQ (smoker trailers, pickup de $25-40K, tope del cottage
    food…): son datos de mercado de este producto y no se vetan aunque coincidan con un importe de otro caso EN."""
    import re as _re
    p = os.path.join(AQUI, 'F1-research-us-delta.md')
    t = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    out = {int(x.replace(',', '')) for x in _re.findall(r'\$\s?(\d{1,3}(?:,\d{3})+)', t) if int(x.replace(',', '')) >= 10000}
    out |= {int(x) * 1000 for x in _re.findall(r'\$\s?(\d{2,3})K\b', t)}
    return out


def cifras_prohibidas(valores):
    """CIFRAS_PROHIBIDAS del conjunto (D110): ES del parrillero (importe y frase) + casos EN del catering, del bar móvil y
    del FT + vocabulario RX_BBQ_NO. Fuera las cifras que coinciden con un valor del propio caso (no son prohibidas aquí)."""
    propios = {int(round(x[0])) for x in valores.values() if isinstance(x[0], (int, float))}
    out = [(_num(n), 'cifra del ES del parrillero (D110)', None) for n in CIFRAS_ES if n not in propios]
    propios |= _importes_research()                     # solo para las listas de los otros casos EN
    out += [(rx, motivo, None) for rx, motivo in FRASES_ES]
    out += [(_num(n), 'cifra del caso del catering EN publicado (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(CAT, 'cifras_caso.json'), 'cat') if n not in propios]
    b4 = CALIBRACION_D15.get(('BBQP', _S, 'B4'), (valores.get(('BBQP', _S, 'B4'), (None,))[0],))[0]
    out += [(rx, motivo, None) for rx, motivo in FRASES_CAT if not (b4 == 180 and '180' in rx)]
    out += [(_num(n), 'cifra del caso del mobile bar EN publicado (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(MBAR, 'cifras_caso.json'), 'mbar') if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_MBAR if not (b4 == 160 and '160' in rx)]
    out += [(_num(n), 'cifra del caso FT EN publicado (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(BP, 'cifras_caso.json'), 'ft') if n not in propios]
    out += RX_BBQ_NO
    return out


def completar(M):
    fijos = OrderedDict((k, v) for k, v in M.FIJOS.items() if k not in FIJOS_FUERA)
    fijos.update(FIJOS_NUEVOS)
    M.FIJOS = fijos
    M.POR_CELDA = POR_CELDA
    M.TOKENS_DOCX = tokens_bbq(M.TOKENS_DOCX)
    M.PRODUCTOS_CIERRE = PRODUCTOS_CIERRE_BBQ
    M.DOCX_FIJOS = docx_fijos(M)
    M.DOCX_NOTAS = DOCX_NOTAS
    M.DOCX_NOTAS_PLAN = DOCX_NOTAS_PLAN
    M.FORMULAS_EN = formulas_bbq()
    M.VALORES_EN = valores_bbq(M)
    M.CALIBRACION_D15 = CALIBRACION_D15
    M.CELDA_PISTAS = CELDA_PISTAS
    M.PISTAS_EXTRA = PISTAS_EXTRA
    M.PISTA_D19 = PISTA_D19_GENERICA          # la pista D19 de verdad va por celda (filas 55-68); las tareas, también
    M.CIFRAS_PROHIBIDAS = cifras_prohibidas(M.VALORES_EN)
    M.RX_BBQ_NO = RX_BBQ_NO
    M.REGLA_UNIDADES = REGLA_UNIDADES
    glo = OrderedDict(M.GLOSARIO)
    for k in ('cliente/día', 'ticket medio sin IVA', 'PVP con IVA', 'aparcamiento y base del vehículo', 'venta ambulante'):
        glo.pop(k, None)                      # glosario del food truck que no vale aquí
    glo.update([('cliente/día → (motor)', 'events per year'), ('ticket medio sin IVA → (motor)',
                                                               'average price per guest (excl. sales tax, service '
                                                               'included)'),
                ('días de apertura → (motor)', 'average guests per event'),
                ('aparcamiento y base del vehículo', 'commissary kitchen & smoker trailer parking')])
    for k, val in GLOSARIO_BBQ.items():
        glo[k] = val                          # research §9 manda (regla de jerga §0)
    M.GLOSARIO = glo
