#!/usr/bin/env python3
"""
datos_pael.py — Paella Catering Business Plan Kit (EN) · los datos ES→EN que dependen del contenido: rótulos fijados
(D120-D121), POR_CELDA, pistas (D18/D19, notas del caso, las 68 tareas del checklist D125 con las columnas que cambian),
tokens del docx (D126), fijos y notas del docx (con la PROPUESTA EN DEL BBQ de cada ranura y el ES 2.2 del paellero), caso
US (D118; research §8), FORMULAS_EN, cifras prohibidas y vocabulario vetado RX_PAEL_NO (D128) y glosario de research §9
(regla de jerga §0). Lo llama `mapas_pael.instalar()` con el módulo `mapas` YA cargado con los datos de FT/CAF (motor 2.2),
de los que parte. La fuente ES del circuito es el FOOD TRUCK ES: los rótulos ES de abajo son los del FT; el EN de partida
de cada celda es el del BBQ cerrado (y, si no hay, el del Catering publicado): mapas_pael.propuesta_de. Estructura de
`../business-plans-en-6/datos_bbq.py` (D119). Sesión Claude Code, 24-oct-2026 (F2, paso 1).
"""
import json
import os
import sys
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
BP = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
CAT = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')
MBAR = os.path.join(os.path.dirname(AQUI), 'business-plans-en-5')
BBQ = os.path.join(os.path.dirname(AQUI), 'business-plans-en-6')
PAE = os.path.join(os.path.dirname(AQUI), 'paellero-2_2')

URL_PAEL = 'aichef.pro/en/digital-products/paella-catering-business-plan'
_I, _S, _P, _R, _N, _E, _ES, _T = ('Inversión Inicial', '0. Supuestos', 'PyG 3 Años', 'Personal', 'Instrucciones',
                                   'Punto Equilibrio', 'Escenarios', 'Tesorería 12 meses')
# Medidas (John, 13-oct; SPEC §0): sistema US como principal y la métrica entre paréntesis
REGLA_UNIDADES = ('MEDIDAS US (John, 13-oct; SPEC §0): principales lb y oz, °F, miles, gallons / quarts y sq ft; la '
                  'métrica entre paréntesis para UK y Australia: «3.25 oz (92 g)», «135 °F (57 °C)», «2 gallons (7.6 '
                  'liters)», «200 sq ft (19 sq m)» (el gate común no admite «m²»); las PAELLERAS en pulgadas con los cm '
                  'entre paréntesis: «36 in (90 cm)»; el AZAFRÁN en gramos (así se vende en EE. UU.; el gate no veta '
                  '«g»); nada de kg, km, litros ni °C como unidad principal (gate). El MÍNIMO del FDA Food Code (165 °F '
                  'aves · 145 °F 15 s pescado y marisco · 155 °F 17 s chorizo crudo mexicano · hot holding 135 °F o time '
                  'as a public health control de 4 h) se nombra SIEMPRE como tal')

# ==========================================================================
# FIJOS (por TEXTO ES del FT: valen en cualquier celda de los 2 libros) y POR_CELDA (solo esa celda)
# ==========================================================================
FIJOS_FUERA = ('Este fichero forma parte del producto «plan-negocio-cafeteria» de AI Chef Pro.',)
_TITULO_CHECK = 'PAELLA CATERING STARTUP CHECKLIST — LIVE PAELLA CATERER'
FIJOS_NUEVOS = OrderedDict([
    ('Este fichero forma parte del producto «plan-negocio-food-truck» de AI Chef Pro.',
     'This file is part of the Paella Catering Business Plan Kit by AI Chef Pro.'),
    # D125: título del checklist y de la fase 2 (el título de hoja no tiene el límite de 31 de la pestaña)
    ('CHECKLIST APERTURA — FOOD TRUCK', _TITULO_CHECK),
    ('FASE 2: VEHÍCULO Y PERMISOS', 'PHASE 2: COMMISSARY, PROPANE STATION, FIRE RULES & PERMITS'),
    ('INSTRUCCIONES DE USO — Plan financiero Food Truck',
     'HOW TO USE THIS WORKBOOK — Paella Catering Financial Projections'),
    ('PLAN DE NEGOCIO: FOOD TRUCK', 'BUSINESS PLAN: PAELLA CATERING COMPANY'),
    ('Ajusta las cifras a tu proyecto.', 'US kit example (2026) — replace with your own quotes.'),
    ('Escenario realista — Food Truck urbano', 'Base case — live paella caterer (cooked on site at events)'),
    ('Break-even — Food Truck', 'Break-even — Paella Catering'),
    # D122: cabecera de la tabla D19
    ('DATOS DE REFERENCIA DEL SECTOR', 'US PAELLA CATERING BENCHMARKS (sourced) AND KIT ESTIMATES'),
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
    # el canal de «delivery» del FT son los marketplaces de catering corporativo (B16/B17)
    ('Comisiones de delivery', 'Corporate catering marketplace fees'),
    # alcohol solo si algún día vendes con licencia (0 % en el caso)
    ('IVA repercutido/soportado general', 'Sales tax rate on alcohol sold (licensed only)'),
    # D121: las dos líneas de venta y su coste (los mismos textos ES salen en el P&L y en Escenarios)
    ('Coste de mercancía — comida', 'Cost of goods — paella packages (rice, seafood, meats, saffron, salad & bread)'),
    ('Coste de mercancía — bebida', 'Cost of goods — add-ons'),
    ('Consumibles y envases', 'Disposables & cooking fuel'),
])

POR_CELDA = OrderedDict([
    # 0. Supuestos (D118, D121): mezcla de ventas, canal, commissary
    (('PAEP', _S, 'A11'), 'PAELLA PACKAGES share of sales (live-cooked paella, salad & bread, paella chef & staff)'),
    (('PAEP', _S, 'A12'), 'ADD-ONS share of sales (tapas, desserts, non-alcoholic sangria & drinks, rentals, extra hours, '
                          'travel fees)'),
    (('PAEP', _S, 'A13'), 'Cost of goods on PAELLA PACKAGE sales (rice, seafood, meats, saffron, stock, salad, bread)'),
    (('PAEP', _S, 'A14'), 'Cost of goods on ADD-ON sales'),
    (('PAEP', _S, 'A15'), 'Disposables & cooking fuel as % of sales'),
    (('PAEP', _S, 'A16'), 'Corporate catering marketplace share of sales (e.g. ezCater)'),
    (('PAEP', _S, 'A17'), 'Marketplace commission on those sales'),
    (('PAEP', _S, 'A23'), 'COMMISSARY KITCHEN, EQUIPMENT STORAGE AND FIXED COSTS'),
    (('PAEP', _S, 'A24'), 'Commissary kitchen rent & equipment storage, per month'),
    (('PAEP', _S, 'A25'), 'Commissary deposit (months)'),
    (('PAEP', _S, 'A26'), 'Monthly utilities (water, power and phone not covered by the commissary)'),
    (('PAEP', _S, 'A44'), 'Useful life of the burners, pans, van and fit-outs (years)'),
    (('PAEP', _S, 'A45'), 'Useful life of the propane kit, commissary fit-out, setup & holding gear, paella tools and '
                          'software (years)'),
    (('PAEP', _S, 'A51'), 'Max events a year your paella crew can handle'),
    (('PAEP', _S, 'A54'), 'Months of commissary rent BEFORE opening'),
    (('PAEP', _S, 'A55'), 'Contingency on the burner, pan, van and fit-out lines (%)'),
    (('PAEP', _S, 'A62'), 'ALCOHOL as a share of add-on sales (0%: no liquor license; the client supplies any wine)'),
    # Startup Costs filas 7-23 y base de amortización (D120: huecos del BBQ; solo se mueven filas)
    (('PAEP', _I, 'A7'), 'Paella burners & stands (four 3-ring burners with legs, one rolling stand, wind guards)'),
    (('PAEP', _I, 'A8'), 'Paella pans: 2 × 36 in (90 cm), 3 × 32 in (80 cm), 3 × 26 in (65 cm)'),
    (('PAEP', _I, 'A9'), 'Propane & fire-safety kit (eight 20-lb cylinders, regulators, hoses, 2 extinguishers, fire '
                         'blanket)'),
    (('PAEP', _I, 'A10'), 'Commissary prep & storage fit-out (racks, sheet pans, labeled bins)'),
    (('PAEP', _I, 'A11'), 'Used cargo van'),
    (('PAEP', _I, 'A12'), 'Van upfit (shelving, upright cylinder racks, tie-downs, wrap)'),
    (('PAEP', _I, 'A13'), 'LLC formation, contracts and legal'),
    (('PAEP', _I, 'A14'), 'First-year permits and certifications (catering / health permit, temporary event permits, '
                          'ServSafe Manager, food handler cards)'),
    (('PAEP', _I, 'A15'), 'Fire / event permit & propane setup inspection (only if required)'),
    (('PAEP', _I, 'A16'), 'Catering software, card reader and tablet'),
    (('PAEP', _I, 'A17'), 'Smallwares & paella tools (paddles, ladles, knives, hotel pans, probe thermometers)'),
    (('PAEP', _I, 'A18'), 'Opening inventory (bomba rice, saffron, stock base, seafood for test cooks, disposables)'),
    (('PAEP', _I, 'A19'), 'Website, photos, launch and first bridal show'),
    (('PAEP', _I, 'A20'), 'Event setup & holding (canopy for the cooking station, tables, handwashing station, coolers, '
                          'chafing dishes, insulated carriers)'),
    (('PAEP', _I, 'A21'), 'Commissary deposit'),
    (('PAEP', _I, 'A22'), 'Commissary rent before opening'),
    (('PAEP', _I, 'A23'), 'Burner, pan, van and fit-out contingency'),
    (('PAEP', _I, 'A31'), 'Paella burners, pans, van and fit-outs (depreciated over the vehicle life)'),
    # 3-Year P&L (D121; research §8: fijos B26-B35 = 25,100)
    (('PAEP', _P, 'A10'), 'Paella package sales (live-cooked paella, salad & bread, paella chef & staff)'),
    (('PAEP', _P, 'A11'), 'Add-on sales (tapas, desserts, non-alcoholic sangria & drinks, rentals, extra hours, travel '
                          'fees)'),
    (('PAEP', _P, 'A22'), 'Commissary kitchen rent & equipment storage'),
    (('PAEP', _P, 'A24'), 'Utilities (water, power and phone not covered by the commissary)'),
    (('PAEP', _P, 'A25'), 'Insurance (general liability with open flame covered, commercial auto, workers\' comp, inland '
                          'marine)'),
    (('PAEP', _P, 'A26'), 'Annual permits and licenses (catering / health permit, temporary event and fire permits)'),
    (('PAEP', _P, 'A27'), 'Van fuel, maintenance and registration'),
    (('PAEP', _P, 'A30'), 'Software (catering / CRM, e-signature, POS, website)'),
    (('PAEP', _P, 'A31'), 'Linens, uniforms and cleaning'),
    (('PAEP', _P, 'A32'), 'Waste, used oil and shell disposal'),
    (('PAEP', _P, 'A33'), 'Pan, burner & hose replacement'),
    (('PAEP', _P, 'A34'), 'Food safety training (ServSafe Manager, food handler cards)'),
    (('PAEP', _P, 'A35'), 'Tastings for prospects'),
    (('PAEP', _P, 'A52'), 'Cost of goods sold (paella packages + add-ons)'),
    (('PAEP', _P, 'A55'), 'Commissary & storage / Sales'),
    (('PAEP', _N, 'A20'), 'Commissary & storage / Sales'),
    # Staffing (D121): 4 puestos W-2, cobertura por evento, nota W-2 / paella chef
    (('PAEP', _R, 'A5'), 'Owner / Paella Chef & Sales'),
    (('PAEP', _R, 'A6'), 'Lead cook / second paella chef (part-time W-2)'),
    (('PAEP', _R, 'A7'), 'Event staff (servers, buffet attendants; hourly W-2)'),
    (('PAEP', _R, 'A8'), 'Prep cook / driver (part-time W-2)'),
    (('PAEP', _R, 'A15'), 'COVERAGE OF EVENT HOURS'),
    (('PAEP', _R, 'A18'), 'Hours per person per event (prep, loading, travel, setup and cooking, service, breakdown)'),
    (('PAEP', _R, 'A19'), 'People per event (paella chefs and event staff, average)'),
    (('PAEP', _R, 'A20'), 'Event hours to cover per year'),
    (('PAEP', _R, 'A24'), 'Columns D-G are TOTALS for the row. Event staff (servers, buffet attendants) are hourly W-2 '
                          'employees with payroll taxes and workers\' comp: paying them as 1099 contractors is a '
                          'misclassification risk (FLSA; California AB5). One paella chef can run about three pans at '
                          'once.'),
    # 12-Month Cash Flow (D121): Month 1 = mes de apertura (marzo); el depósito no se modela
    (('PAEP', _T, 'O5'), 'Share of the year\'s events per month (100% in total). Month 1 = opening month (March in the '
                         'example). The booking deposit is not modeled: it improves real cash.'),
    # notas del motor (= BBQ)
    (('PAEP', _S, 'C20'), 'FICA (Social Security 6.2% + Medicare 1.45%) + federal and state unemployment taxes (FUTA / '
                          'SUTA). Workers\' comp is in the insurance line. The example uses a lean 10% with no benefits; '
                          'ask your payroll provider for your rate.'),
    (('PAEP', _S, 'A2'), 'Change the GREEN cells: the rest of the workbook recalculates on its own. Expense items are typed '
                         'on their own tab (also in green) and are not repeated here. Amounts are in US dollars (or your own '
                         'currency).'),
    (('PAEP', _S, 'C39'), 'Example rate: state + local sales tax combined, applied to the whole invoice (food, staffing, '
                          'rentals and the service charge). It varies widely by state and city: look up yours. UK: 20% VAT '
                          'applies to catering for events and functions (VAT Notice 709/1).'),
    (('PAEP', _S, 'C67'), 'Minimum cushion of the plan above break-even (plan ÷ break-even − 1). The drop you can absorb is '
                          '1 − break-even ÷ plan: a 15% cushion lets events fall by about 13% before costs stop being covered'),
    (('PAEP', _E, 'E24'), 'How far the plan sits above the cash break-even (plan ÷ break-even − 1); the drop you can absorb '
                          'is 1 − break-even ÷ plan. The required minimum is set in the "0. Assumptions" tab'),
])

# ==========================================================================
# Cifras prohibidas (D128): ES del paellero 2.2 (importe y frase), caso del BBQ, casos EN ajenos (catering, mobile bar,
# FT) y el vocabulario vetado RX_PAEL_NO (con su lista blanca). Formato: (regex, motivo, excepción sobre el texto entero)
# ==========================================================================
def _num(n):
    """190000 → patrón que casa 190,000 · 190.000 · 190 000 · 190000 (y nada pegado a más dígitos)."""
    s = str(n)
    cab, cola = s[:-3], s[-3:]
    return r'(?<![\d.,])' + cab + r'[.,   ]?' + cola + r'(?![\d])'


# F1-inventario §7: los importes ≥ 10.000 de `paellero-2_2/cifras_caso_es.json` (LIVE); 18.000 y 20.000 quedan fuera
# (chocan con la van y con importes US plausibles: decisión del paso 1)
CIFRAS_ES = (10800, 12392, 12417, 14579, 14829, 15794, 16803, 18582, 19772, 20425, 41777, 42686, 51600, 55097, 57893,
             63111, 71487, 85448, 100027, 108375, 128987, 134903, 152768, 157920, 173712, 184135, 212500)
_PEQ_ES = '1[.,]?504|1[.,]?750|2[.,]?100|2[.,]?400|3[.,]?354|3[.,]?747|4[.,]?000|6[.,]?130|8[.,]?376'
FRASES_ES = [
    # los pequeños del ES solo con € o EUR (como importe chocarían con importes US plausibles)
    (r'(?i)(?:€|\bEUR)\s?(?:%s)\b|\b(?:%s)\s?(?:€|EUR\b)' % (_PEQ_ES, _PEQ_ES), 'importe pequeño del ES con €'),
    (r'(?i)\b105 events\b', 'caso ES (105 eventos/año)'),
    (r'(?i)\b94 guests\b', 'caso ES (94 invitados por evento)'),
    (r'(?i)\b16\s?€|€\s?16\b', 'precio ES (16 €/invitado)'),
    (r'(?i)\b(?:90|86) events\b', 'equilibrio ES (90 / 86 eventos)'),
    (r'(?i)\b(?:81|77) guests\b', 'escenarios ES (81 / 77 invitados)'),
    (r'(?i)\b85 events\b', 'escenario ES (85 eventos)'),
    (r'\b22\.4\s?%', 'ratio ES (22,4 %)'),
    (r'(?i)\bDSCR (?:of )?1\.72\b', 'DSCR ES (1,72)'),
    (r'(?i)\b83 (?:tasks|steps|milestones)\b', 'recuento del checklist ES (83 tareas)'),
    (r'(?i)\b88 (?:validated )?suppliers\b', 'promesa ES (88 proveedores)'),
    (r'(?i)\b11 deliverables\b', 'recuento ES (11 entregables)'),
    (r'(?i)\bfiestas? populares?\b|\bcontrato menor\b', 'ES (fiestas populares / contrato menor)'),
    (r'\bv1\.1\b|\b[Vv]ersion 1\.1\b', 'historia de versiones (la EN nace en 2.2)'),
]
# lista blanca (D128): socarrat, sofrito, bomba rice, chorizo, aioli, tapas, patatas bravas, sangria, «paella food
# truck(s)», commissary, food handler, «cocktail hour», «burn ban», AI Chef Pro y la firma; «chef» solo como «paella chef»
# / «second paella chef» («chefs and head cooks» solo junto a OEWS / BLS / 35-1011); «Spain» solo junto al origen;
# «stations» solo «live paella station», «Serrano ham carving station» y las de montaje (cooking / handwashing station);
# VAT solo en la nota UK; «induction» y «wood-fire» valen (inducción en interiores; leña solo con permiso: D117)
_FIRMA = r'John Guerrero'
_OEWS = r'John Guerrero|\bchefs and head cooks\b[^.]*\b(?:OEWS|35-1011|BLS)\b|\b(?:OEWS|35-1011|BLS)\b[^.]*\bchefs and head cooks\b'
_ORIGEN_ES = (r'(?i)(?:saffron|bomba|rice|imported|origin|Valencia)[^.]{0,60}\bSpain\b|\bSpain\b[^.]{0,60}'
              r'(?:saffron|bomba|rice|imported|origin)')
RX_PAEL_NO = [
    # heredado del FT (D72)
    (r'(?i)\bper day\b', 'vocabulario FT («per day»)', None),
    (r'(?i)\boperating days?\b', 'vocabulario FT («operating days»)', None),
    (r'(?i)(?<!corporate )\bcustomers\b', 'vocabulario FT («customers» → clients / guests / hosts)',
     r'^Synthetic paragraph \d+ of the \w+ plan for the assembly test'),
    (r'(?i)(?<!paella food )\btrucks?\b(?! Business Plan Kit)', 'vocabulario FT («truck»: solo «paella food truck(s)» y el '
                                                               'nombre del kit)', None),
    (r'(?i)\bwindows?\b', 'vocabulario FT («window»)', None),
    (r'(?i)\bfestivals?\b', 'vocabulario FT («festival» → public or community event)', None),
    # del catering EN
    (r'(?i)\bplated\b', 'catering genérico («plated»)', None),
    (r'(?i)\b(?:chef-attended|themed|action|food) stations?\b', 'catering genérico («themed / action / food stations»)',
     None),
    (r'(?i)(?<!paella )(?<!carving )(?<!cooking )(?<!handwashing )(?<!handwash )(?<!propane )\bstations?\b',
     'catering genérico («stations»: solo live paella station, Serrano ham carving station, cooking / handwashing station)',
     None),
    (r'(?i)\bchef-attended\b', 'catering genérico («chef-attended»)', None),
    (r'(?i)(?<!AI )(?<!paella )\b(?:executive |sous )?chefs?\b', 'catering genérico («chef» → paella chef)', _OEWS),
    (r'(?i)\btaco bars?\b', 'catering genérico («taco bar»)', None),
    (r'(?i)\bpasta\b', 'catering genérico («pasta»)', None),
    (r'(?i)\b(?:12|twelve) (?:world )?cuisines\b', 'catering genérico («12 cuisines»)', None),
    (r'(?i)\brefrigerated (?:cargo )?vans?\b', 'catering genérico («refrigerated van»: la van no es frigorífica)', None),
    # del bar móvil
    (r'(?i)\bcocktails?\b(?! hour)', 'bar móvil («cocktails»; solo «cocktail hour»)', None),
    (r'(?i)\bbartend(?:er|ers|ing)\b', 'bar móvil («bartender»)', None),
    (r'(?i)\bdry hire\b', 'bar móvil («dry hire»)', None),
    (r'(?i)\bmobile bars?\b', 'bar móvil («mobile bar»)', None),
    (r'(?i)\bbarbacks?\b', 'bar móvil («barback»)', None),
    (r'(?i)\bmixers?\b', 'bar móvil («mixers»)', None),
    (r'(?i)\bspecialty bars?\b|\bcash bars?\b', 'bar móvil («specialty / cash bar»)', None),
    # del BBQ (D128; F1-inventario §7)
    (r'(?i)\bsmok(?:e|ed|er|ers|ing|y)\b(?! paprika)', 'BBQ («smoke / smoker / smoked»; solo «smoked paprika»)', None),
    (r'(?i)\bpitmasters?\b|\bpits?\b|\bpit (?:cook|crew)s?\b', 'BBQ («pitmaster / pit»)', None),
    (r'(?i)\bbrisket\b|\bpulled pork\b|\bpork butts?\b|\b(?:spare |baby back |St\. Louis )?ribs\b|\bbark\b|'
     r'\bsmoke ring\b|\bburnt ends\b', 'BBQ (cortes y jerga del ahumado)', None),
    (r'(?i)\blive[- ]fire\b|\blive pit\b', 'BBQ («live-fire / live pit»)', None),
    (r'(?i)(?<!ham )\bcarv(?:e|ed|ing|er|ers)\b', 'BBQ («carving»: solo «Serrano ham carving station»)', None),
    (r'(?i)\btrailers?\b|\btow vehicle\b|\bpickups?\b', 'BBQ («trailer / tow vehicle / pickup»)', None),
    (r'(?i)\bwhole hogs?\b|\bpig roasts?\b|\btri-tips?\b|\bpicanha\b|\basado\b|\bchurrasco\b|\bCaja China\b|'
     r'\bSanta Maria\b|\bparrilla\b', 'BBQ (live-fire premium)', None),
    (r'(?i)\bbutcher paper\b|\brubs?\b|\bpounds of meat\b|\bmeat (?:yield|lines?|prices?|per guest)\b|'
     r'\b(?:raw|cooked|smoked) meats?\b', 'BBQ (jerga de la carne)', None),
    (r'(?i)\bBBQ\b|\bbarbecue\b|(?<!Miami )\bgrill(?:s|ed|ing| masters?)?\b', 'BBQ («BBQ / barbecue / grill»)', None),
    # del ES del paellero
    (r'\bEspaña\b', 'ES («España»)', None),
    (r'\bSpain\b', 'ES («Spain» solo junto al origen: saffron, bomba, imported)', _ORIGEN_ES),
    (r'\bIVA\b', 'ES («IVA»)', None),
    (r'\bVAT\b', 'ES («VAT» fuera de la nota UK)', r'\bUK\b|United Kingdom|HMRC'),
    (r'(?i)\baut[oó]nomo\b|\bfijos? discontinuos?\b|\bETT\b', 'trámite ES (autónomo / fijo discontinuo / ETT)', None),
    (r'\bSL\b|\bIAE\b|\bAESAN\b|\bAPPCC\b|\bCCAA\b|\bRGSEAA\b|\bFACe\b|Veri\*?factu|\bADR\b', 'trámite / norma ES', None),
    (r'\bRD \d|Reglamento \(CE\)|Real Decreto|\bITC-ICG\b', 'norma ES (RD / Reglamento / ITC)', None),
    (r'Bodas\.net|Zankyou|Hosply|\bGGM\b|Garcima|Vaello|\bArcos\b|\bIDAE\b', 'proveedor / directorio ES', None),
    (r'(?i)\bpaeller[oa]s?\b|\bgarrof[oó]\b|\bferraura\b|\bbogavante\b|\bsenyoret\b|\bfincas?\b|\bfiestas? del pueblo\b|'
     r'\bFalles\b|\bFallas\b', 'ES del paellero (paellero / paellera / garrofó / bogavante / finca…)', None),
    (r'(?i:paella|valenciana?|vegetal|vegetable|rice)\s+D\.?O\.?(?!\w)|\bD\.O\.', '«DO» aplicado al plato (la DO ampara '
                                                                               'el arroz: deuda ES)', None),
    (r'\bEUR\b|€', 'moneda ES', None),
    (r'(?i)\bfree-?lance', 'jerga (§0): «freelance» → part-time hourly W-2 staff', None),
    # regla de jerga §0 (research §9)
    (r'(?i)\bsupport kitchen\b', 'jerga (§0): «support kitchen» → commissary', None),
    (r'(?i)\bshow cooking\b', 'jerga (§9e): «show cooking» → live paella / cooked live in front of your guests', None),
    (r'\bCambros?\b', 'jerga (§0): «Cambro» es marca → insulated food carriers', None),
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
# caso del BBQ (D128): la mezcla de la paella usa «75 guests at $38» para los eventos de empresa (research §8), así que
# las frases del BBQ se vetan solo como CASO («75 guests per event», «$38 per guest»)
FRASES_BBQ = [(r'(?i)\b150 events\b', 'caso del BBQ EN («150 events»)'),
              (r'(?i)\$38(?:\.00)? (?:per|a) guest\b|\$38\.00\b', 'caso del BBQ EN («$38 per guest»)'),
              (r'(?i)\b75 guests (?:per|an?|each) event\b|\baverage of 75 guests\b', 'caso del BBQ EN («75 guests per '
                                                                                      'event»)'),
              (r'(?i)\b220 events\b', 'caso del BBQ EN («220 events»)'),
              (r'(?i)\b128 events\b', 'equilibrio del BBQ EN («128 events»)'),
              (r'\$2,850\b', 'caso del BBQ EN ($2,850 por evento)')]


# ==========================================================================
# Tokens del docx (D126): los del motor con descripciones de paella + alias legibles + partidas propias. Cada token apunta
# a SU celda ([98]: {{cobro_dias}} y {{pago_dias}}, D113)
# ==========================================================================
_DESC = OrderedDict([
    ('clientes_dia', 'EVENTS per year, year 1 (alias heredado: usa {{eventos_a1}})'),
    ('clientes_a2', 'EVENTS per year, year 2 (alias: usa {{eventos_a2}})'),
    ('clientes_a3', 'EVENTS per year, year 3 (alias: usa {{eventos_a3}})'),
    ('ticket', 'average price per guest excl. sales tax (alias: usa {{precio_invitado}})'),
    ('precio_menu', 'price per guest incl. sales tax (alias: usa {{precio_invitado_con_tax}})'),
    ('dias', 'average guests per event (alias: usa {{invitados_evento}})'),
    ('crecimiento_a2', 'growth in EVENTS in year 2'), ('crecimiento_a3', 'growth in EVENTS in year 3'),
    ('consumibles_pct', 'disposables & cooking fuel (propane; wood only where a permit allows it), % of sales'),
    ('tarjeta_pct', 'card processing fees, % of sales (private clients pay deposits and balances by card)'),
    ('alquiler_mes', 'commissary kitchen rent & equipment storage, per month'),
    ('suministros_mes', 'utilities per month (water, power and phone not covered by the commissary)'),
    ('seguros_anual', 'insurance per year (general liability / BOP with open flame covered, commercial auto, workers\' '
                      'comp, inland marine)'),
    ('vida_obra', 'useful life of the burners, pans, van and fit-outs, years'),
    ('vida_equipo', 'useful life of the propane kit, commissary fit-out, setup & holding gear, paella tools and software, '
                    'years'),
    ('ocupacion_anual', 'commissary kitchen rent & equipment storage per year'),
    ('ocupacion_pct', 'commissary kitchen rent & equipment storage, % of sales'),
    ('cogs_pct', 'cost of goods (paella packages + add-ons), % of sales'),
    ('equilibrio_clientes_dia', 'break-even EVENTS per year, accounting (alias: usa {{equilibrio_eventos}})'),
    ('equilibrio_caja_clientes_dia', 'cash break-even EVENTS per year (alias: usa {{equilibrio_caja_eventos}})'),
    ('pesimista_clientes', 'pessimistic scenario: events per year (alias: usa {{pesimista_eventos}})'),
    ('optimista_clientes', 'optimistic scenario: events per year (alias: usa {{optimista_eventos}})'),
    ('pesimista_ticket', 'pessimistic scenario: price per guest (alias: usa {{pesimista_precio}})'),
    ('optimista_ticket', 'optimistic scenario: price per guest (alias: usa {{optimista_precio}})'),
    ('pesimista_dias', 'pessimistic scenario: guests per event (alias: usa {{pesimista_invitados}})'),
    ('optimista_dias', 'optimistic scenario: guests per event (alias: usa {{optimista_invitados}})'),
    ('inv_permisos', 'first-year permits and certifications (catering / health permit, temporary event permits, '
                     'ServSafe Manager, food handler cards)'),
    ('inv_lanzamiento', 'website, photos, launch and first bridal show'),
    ('inv_stock', 'opening inventory (bomba rice, saffron, stock base, seafood for test cooks, disposables)'),
    ('horas_semana', 'full-time hours per week'),
])
# fuera: ventas ÷ «días» no significa nada; las filas 7-10 del FT son aquí otras partidas (alias propios abajo: los
# heredados inv_vehiculo / inv_adaptacion confundirían «vehículo» con los quemadores); «food_cost_*» → alias neutros
_FUERA = ('ventas_dia', 'inv_vehiculo', 'inv_adaptacion', 'inv_equipo_cocina', 'inv_generador', 'food_cost_comida',
          'food_cost_bebida')
TOKENS_PROPIOS = OrderedDict([
    # alias legibles del motor (las mismas celdas que los tokens heredados)
    ('eventos_a1', ('int', ('fila', _S, 'Clientes/día (media del año 1)', 'B'), 'events per year, year 1')),
    ('eventos_a2', ('int', ('fila', _P, 'Clientes/día (media)', 'C'), 'events per year, year 2')),
    ('eventos_a3', ('int', ('fila', _P, 'Clientes/día (media)', 'D'), 'events per year, year 3')),
    ('precio_invitado', ('usd2', ('fila', _S, 'Ticket medio SIN IVA (€)', 'B'),
                         'average price per guest of the event mix, excl. sales tax, paella chef, staff and service '
                         'included')),
    ('precio_invitado_con_tax', ('usd2', ('fila', _S, 'PVP equivalente con IVA (calculado)', 'B'),
                                 'average price per guest incl. sales tax')),
    ('invitados_evento', ('int', ('fila', _S, 'Días de apertura al año', 'B'), 'average guests per event')),
    ('capacidad_eventos', ('int', ('fila', _S, {'pael': 'Plazas de pie y mesas altas junto al vehículo'}, 'B'),
                           'max events a year the paella crew can handle (information only)')),
    ('cuota_paquetes_pct', ('pct0', ('fila', _S, 'Ventas de COMIDA sobre el total', 'B'),
                            'paella packages, % of sales (the rest are add-ons)')),
    ('coste_paquetes_pct', ('pct0', ('fila', _S, 'Coste de mercancía sobre las ventas de COMIDA', 'B'),
                            'cost of goods on paella package sales (rice, seafood, meats, saffron, salad & bread)')),
    ('coste_extras_pct', ('pct0', ('fila', _S, 'Coste de mercancía sobre las ventas de BEBIDA', 'B'),
                          'cost of goods on add-on sales')),
    ('marketplace_pct', ('pct0', ('fila', _S, 'Ventas por delivery sobre el total', 'B'),
                         'share of sales through corporate catering marketplaces (e.g. ezCater)')),
    ('marketplace_comision', ('pct0', ('fila', _S, 'Comisión de la plataforma de delivery', 'B'),
                              'marketplace commission on those sales')),
    ('cobro_dias', ('int', ('fila', _S, 'Días medios de cobro', 'B'), 'average days to collect from clients')),
    ('pago_dias', ('int', ('fila', _S, 'Días medios de pago a proveedor', 'B'), 'average days to pay suppliers')),
    ('horas_evento', ('dec1', ('fila', _R, 'Horas de servicio al día que hay que cubrir', 'B'),
                      'hours per person per event (prep, loading, travel, setup and cooking, service, breakdown)')),
    ('personas_evento', ('dec1', ('fila', _R, 'Personas necesarias a la vez en cada franja', 'B'),
                         'people per event (paella chefs and event staff, average)')),
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
    # partidas de la inversión del paella caterer (D120: filas 7-20, huecos del BBQ; rótulos ES del FT)
    ('inv_quemadores', ('usd', ('fila', _I, {'pael': 'Vehículo food truck (nuevo o segunda mano)'}, 'B'),
                        'paella burners & stands (four 3-ring burners with legs, one rolling stand, wind guards)')),
    ('inv_paelleras', ('usd', ('fila', _I, {'pael': 'Adaptación y rotulación vehículo'}, 'B'),
                       'paella pans: 2 × 36 in (90 cm), 3 × 32 in (80 cm), 3 × 26 in (65 cm)')),
    ('inv_propano', ('usd', ('fila', _I, {'pael': 'Equipamiento cocina móvil'}, 'B'),
                     'propane & fire-safety kit (eight 20-lb cylinders, regulators, hoses, 2 extinguishers, fire blanket)')),
    ('inv_almacen', ('usd', ('fila', _I, {'pael': 'Generador eléctrico o conexión'}, 'B'),
                     'commissary prep & storage fit-out (racks, sheet pans, labeled bins)')),
    ('inv_furgoneta', ('usd', ('fila', _I, {'pael': 'Instalación gas (si aplica)'}, 'B'), 'used cargo van')),
    ('inv_furgoneta_upfit', ('usd', ('fila', _I, {'pael': 'Depósito de agua + aguas residuales'}, 'B'),
                             'van upfit (shelving, upright cylinder racks, tie-downs, wrap)')),
    ('inv_llc', ('usd', ('fila', _I, {'pael': 'Constitución SL + notaría + registro'}, 'B'),
                 'LLC formation, contracts and legal')),
    ('inv_inspeccion', ('usd', ('fila', _I, {'pael': 'Proyecto técnico sanitario'}, 'B'),
                        'fire / event permit & propane setup inspection (only if required)')),
    ('inv_software', ('usd', ('fila', _I, {'pael': 'TPV móvil + datáfono'}, 'B'), 'catering software, card reader and tablet')),
    ('inv_herramientas', ('usd', ('fila', _I, {'pael': 'Menaje, utensilios, packaging eco'}, 'B'),
                          'smallwares & paella tools (paddles, ladles, knives, hotel pans, probe thermometers)')),
    ('inv_montaje', ('usd', ('fila', _I, {'pael': 'Toldo, mobiliario exterior plegable'}, 'B'),
                     'event setup & holding (canopy for the cooking station, tables, handwashing station, coolers, '
                     'chafing dishes, insulated carriers)')),
    # derivadas
    ('ventas_evento', ('usd', ('deriv', lambda c: c['ventas_a1'] / c['clientes_dia']),
                       'average revenue per event, year 1 (excl. sales tax)')),
    ('invitados_a1', ('int', ('deriv', lambda c: c['clientes_dia'] * c['dias']), 'guests served in year 1')),
    ('caida_absorbible_pct', ('pct0', ('deriv', lambda c: c['holgura_caja_pct'] / (1 + c['holgura_caja_pct'])),
                              'drop in events the plan can absorb before cash stops covering costs (1 − break-even ÷ plan)')),
])


def tokens_pael(base):
    out = OrderedDict()
    for t, (fmt, src, desc) in base.items():
        if t in _FUERA:
            continue
        if src[0] == 'fila':
            _, hoja, rot, col = src
            if isinstance(rot, dict):
                if 'ft' not in rot:
                    continue                               # partidas de la cafetería
                src = ('fila', hoja, {'pael': rot['ft']}, col)
        if t == 'consumibles_pct':
            fmt = 'pct1'                               # M1 del BBQ: 3.5 %, no 4 %
        out[t] = (fmt, src, _DESC.get(t, desc))
    out.update(TOKENS_PROPIOS)
    return out


# ==========================================================================
# Docx (D126): lo que escribe ensamblar_docx.py y las notas para los redactores
# ==========================================================================
PRODUCTOS_CIERRE_PAEL = ['Catering Business Plan Kit', 'Food Truck Business Plan Kit', 'Food Cost Kit Pro',
                         'HACCP Food Safety Kit Pro']


def docx_fijos(M):
    pc = PRODUCTOS_CIERRE_PAEL
    d = OrderedDict([
        (6, 'BUSINESS PLAN'), (7, 'Paella Catering'),
        (9, 'Complete financial plan, market analysis,\noperations strategy and startup checklist\nto launch a live '
            'paella catering company in the United States'),
        (14, 'AI Chef Pro'), (15, 'aichef.pro'), (16, 'US edition with UK notes · 2026'),
        (18, 'LEGAL NOTICE'), (19, M.AVISO_DOCX_EN), (20, '© 2026 AI Chef Pro — aichef.pro'), (22, 'CONTENTS'),
        (35, 'Appendices: Paella Catering Financial Projections (Excel) + Paella Catering Pricing Calculator (Excel) + '
             'Paella Catering Startup Checklist (Excel)'),
        (123, 'AI Chef Pro'), (124, 'Templates and AI tools for food businesses'),
        (126, 'aichef.pro\ninfo@aichef.pro'),
        (127, '→ %s · %s' % tuple(pc[:2])), (128, '→ ' + pc[2]), (129, '→ ' + pc[3]), (130, '\n' + M.URL_TIENDA),
    ])
    return OrderedDict([('pael', d)])


DOCX_NOTAS_PLAN = OrderedDict([
    ('pael', 'REDACTAS, NO TRADUCES (D126). Cada párrafo trae en su nota: (1) el NIVEL de la ranura (casi literal · '
             'adaptar · nueva, F1-inventario §6); (2) la PISTA de lo que va en esa ranura para un LIVE PAELLA CATERER '
             '(D117): la paella cocinada en vivo en el evento ES el producto (paelleras de 26-36 in sobre quemadores de '
             'propano de 3 aros, con ensalada y pan), sofrito, caldo, verdura y marisco limpio salen de la commissary, '
             'drop-off como línea menor, premium de marisco y tapas; (3) la PROPUESTA EN DEL BBQ de esa misma ranura '
             '(../business-plans-en-6/docx_en_bbq_a.json / _b.json, sha256 fijados): da la FORMA (estructura, tono, '
             'longitud, tokens, fuentes comunes); (4) en las ranuras «adaptar» y «nueva», el párrafo ES 2.2 DEL '
             'PAELLERO de la misma ranura (contenido de referencia: sus cifras, sus {TOKENS} en mayúsculas y todo lo '
             'español NO se usan). LA PISTA MANDA; CERO VOCABULARIO BBQ (smoker, smoked salvo «smoked paprika», '
             'pitmaster, pit, brisket, pulled pork, ribs, bark, live-fire, live pit, carving salvo «Serrano ham '
             'carving station», trailer, tow vehicle, pickup, whole hog, tri-tip, asado, rub, BBQ, barbecue, grill, '
             '«pounds of meat», «meat per guest»). El «es» de cada párrafo es la RANURA del plan de FOOD TRUCK: solo '
             'da el papel y la longitud (±30 %). Fuentes: research §1, §5, §6, §8 y §9 (glosario OBLIGATORIO, regla '
             'de jerga §0) de business-plans-en-7/F1-research-us-delta.md. Cifras del caso SOLO con tokens {{…}}; de '
             'mercado, solo las de research «leída» con su fuente. Prohibido además (gate RX_PAEL_NO y check_textos): '
             '«paellero» y «paellera» (di paella chef / paella caterer / paella pan), «chef» suelto (solo «paella '
             'chef» o «second paella chef»), «Spain» y «Valencia» (check_textos los rechaza: di «Spanish», «imported '
             'Spanish saffron», «Valencian paella»), «stations» salvo «live paella station», «Serrano ham carving '
             'station» y «cooking / handwashing station», «show cooking» (di «live paella», «cooked live in front of '
             'your guests»), «DO» aplicado al plato, «truck» salvo «paella food truck», «per day», «operating days», '
             '«customers», «window», «festival» (di «public or community event»), «plated», «refrigerated van», '
             '«cocktails» (sí «cocktail hour»), «bartender», «mixers», «support kitchen», «Cambro», «freelance», '
             '«D-21» y similares, kg / °C / litros fuera de paréntesis, las cifras del ES del paellero (157.920, «105 '
             'eventos», «94 invitados», «16 €»…), las del CASO DEL BBQ ($427,500, «150 events», «$38 per guest», «75 '
             'guests per event», $101,000…) y las de los casos del catering y del bar móvil, «España», «ChefBusiness». '
             + REGLA_UNIDADES + '. Lo no verificado por la research va como «check your county / state rules» o '
             '«check with your fire marshal», nunca como cifra. El cierre (productos) lo escribe el ensamblador'),
])
# §9 = el núcleo legal (D126); research §6
_N9 = OrderedDict([
    (102, '§9 1/7 (NUEVA; = BBQ en lo común): commissary OBLIGATORIA y nada de cocina de casa: FDA Food Code 2022 '
          '§3-201.11(B) «FOOD prepared in a private home may not be used» (fda.gov) y (A) «obtained from sources that '
          'comply with LAW»; la paella con marisco, pollo o arroz cocido necesita control de tiempo y temperatura y las '
          'leyes de cottage food no la cubren («check your state rules»). Por eso sofrito, caldo y marisco limpio se '
          'preparan en una commissary con permiso y con un commissary agreement por escrito, antes del health permit'),
    (103, '§9 2/7 (NUEVA): permisos y personas: catering / health permit del condado + Certified Food Protection Manager '
          '(ServSafe Manager) + food handler cards según el estado + plan de seguridad alimentaria basado en HACCP '
          'para la paella: el ARROZ COCIDO es TCS (vegetal tratado por calor, Food Code 1-201.10) y el Anexo 3 avisa: '
          '«B. cereus is found commonly in outbreaks attributed to inadequate hot holding of starchy foods like '
          'rice»; servir a ≥ 135 °F (3-501.16) o con time as a public health control de 4 h (3-501.19: SOP escrito, '
          'hora marcada, descarte a las 4 h; pregunta si tu condado lo admite); cocinar el pollo a 165 °F, pescado y '
          'marisco a 145 °F 15 s (3-401.11; «fish» incluye crustáceos y moluscos), chorizo crudo mexicano a 155 °F '
          '17 s (el curado español es listo para comer); las sobras NO se enfrían para reutilizarlas: a la basura; '
          'approved source (3-201.11) y shellstock tags de mejillones y almejas guardadas 90 días (3-203.12). 9 '
          'alérgenos mayores US: entre ellos «fish» y «crustacean shellfish such as crab, lobster, or shrimp»'),
    (104, '§9 3/7 (NUEVA): cocinar en el evento: el Food Code incluye en «food establishment» la «catering operation if '
          'the operation provides FOOD directly to a CONSUMER» (1-201.10); como EJEMPLO, San Diego County (CalRFC '
          '§113818): todo se prepara en la commissary y se permite «Limited Food Preparation» en eventos privados con '
          'catering (invitados, horario y cantidades predeterminados), lavamanos de 5 gal, aseos a ≤ 200 ft, el fuego '
          'separado del público con barrera o cuerda y nunca desde un vehículo, registros 90 días y sobras a la '
          'basura (sandiegocounty.gov) → «ask your county» si cocinar el arroz en el evento cabe en su regla. Un '
          'evento público abierto (no un festival: palabra vetada) es otra figura, el temporary food establishment '
          '(«no more than 14 consecutive days»), y no es el caso del plan'),
    (105, '§9 4/7 (NUEVA): propano y carpas: como EJEMPLO, Virginia (13VAC5-52-360, law.lis.virginia.gov): «cooking '
          'tents shall be separated from other tents… by not less than 20 feet» (3107.12.5) y los envases de LP-gas '
          'fuera de la carpa (3107.13.2); regla del plan: la estación de cocina al aire libre o bajo su propio toldo, '
          'lejos de la carpa de invitados, con extintor y el permiso que pida el fire code local → «check with your '
          'fire marshal» (sin cifras nacionales). Leña solo con permiso y nunca con burn ban; inducción para '
          'interiores. El contrato lleva plan B por viento, lluvia o fuego no autorizado (del ES: plan B)'),
    (106, '§9 5/7 (adaptar): sales tax: en muchos estados grava TODA la factura de catering (comida, personal, '
          'alquileres) y el service charge según el estado (CA: cdtfa.ca.gov; NY: TB-ST-110; TX: excluido si ≤ 20 % '
          'separado y repartido) → el libro aplica {{sales_tax}} a toda la factura (conservador). IRS Rev. Rul. '
          '2012-18: el service charge obligatorio es SALARIO; la gratuity voluntaria va aparte. Sales tax permit. '
          'SANGRÍA: sin licencia no se vende alcohol: sangría sin alcohol como add-on, o hecha con el vino QUE COMPRA '
          'EL CLIENTE, sin margen ni barra de pago; el corkage fee puede contar como venta según el estado y no se '
          'modela; liquor liability solo si tu personal sirve el alcohol del cliente'),
    (107, '§9 6/7 (adaptar): empleo y seguros: event staff, second paella chef y prep cook en nómina W-2 (FLSA; '
          'California AB5), nunca 1099 ni «freelance»; workers\' comp (opcional en Texas, pero venues y lenders lo '
          'piden), I-9 / W-4 / new-hire reporting. Seguros ({{seguros_anual}} al año en el ejemplo): general liability '
          '/ BOP que NO excluya la llama abierta en eventos (pregúntalo por escrito: Kit), commercial auto de la van, '
          'workers\' comp, inland marine para paelleras, quemadores y equipo en tránsito (Insureon publica medias: '
          'insureon.com); COI y additional insured para los venues'),
    (108, '§9 7/7 (adaptar): la van: título, registro y placas en el DMV a nombre del negocio y una póliza de auto '
          'comercial; una cargo van no necesita CDL (solo con GVWR ≥ 26,001 lb); los cilindros viajan de pie, sujetos '
          'y con ventilación. Como ÚLTIMA frase o frases del párrafo, la nota UK: registrar el food business en el '
          'council «at least 28 days before trading» (gov.uk); Food Hygiene Rating 0-5 (FHIS en Escocia), plan HACCP, '
          '14 alérgenos (suma molluscs, celery y sulphites a los US), VAT 20 % del catering de eventos (once you are '
          'VAT-registered), y el gas del evento con el council y el venue (sin cifras)'),
])
# Nivel de cada ranura (F1-inventario §6): L = casi literal (propuesta del BBQ + tokens) · A = adaptar · N = nueva
_NIVEL = {}
for _i in (42, 56, 61, 65, 69, 70, 71, 72, 73, 74, 75, 86, 88, 90, 93, 95, 97, 98, 99, 115, 116, 117):
    _NIVEL[_i] = 'L'
for _i in (39, 41, 43, 48, 49, 53, 54, 55, 57, 58, 62, 63, 64, 66, 82, 85, 87, 89, 94, 96, 106, 107, 108, 111, 112, 113,
           114):
    _NIVEL[_i] = 'A'
for _i in (40, 46, 47, 50, 78, 79, 80, 81, 102, 103, 104, 105):
    _NIVEL[_i] = 'N'
_NIVEL_TXT = {'L': 'CASI LITERAL: parte de la propuesta del BBQ y cambia SOLO lo que dice la pista (vocabulario BBQ, '
                   'cifras del caso por tokens, fuentes de la paella)',
              'A': 'ADAPTAR: la propuesta del BBQ da la forma; el contenido cambia según la pista y el ES 2.2 del '
                   'paellero',
              'N': 'NUEVA (núcleo paella): escribe desde la pista, el ES 2.2 del paellero y research; la propuesta del '
                   'BBQ solo da el tono y la longitud'}
_NOTAS_SECCION = OrderedDict([
    (39, '§1 1/5: la oportunidad: paella catering y Spanish catering en EE. UU.; demanda SOLO con research §2 (búsquedas '
         'mensuales US del lado del cliente: «spanish catering» 2,900, «paella catering» 720, «paella caterer» 720, '
         '«paella party» 320; el emprendedor apenas busca «paella business», 10); sin tamaño de mercado inventado'),
    (40, '§1 2/5: el concepto (D117): live paella caterer: la paella cocinada en vivo delante de los invitados ES el '
         'producto (paelleras de 26-36 in sobre quemadores de propano de 3 aros, con ensalada y pan); sofrito, caldo, '
         'verdura y marisco limpio salen de la commissary la víspera; el drop-off (paella cocinada en la commissary y '
         'entregada en caliente) es la línea menor; premium de marisco y tapas. Gas = base; leña solo con permiso; '
         'inducción en interiores. No es el paella food truck ni el restaurante. Del ES: «la paella se cocina en el '
         'evento; caldos y sofritos, en la cocina de apoyo»'),
    (41, '§1 3/5: inversión y financiación SOLO con tokens: {{inversion_total}} = {{capex}} + {{fondo_maniobra}}; '
         '{{fondos_propios}} ({{aportacion_pct}}) + préstamo {{prestamo}} al {{tipo_prestamo}} a {{plazo_prestamo}} '
         'años (SBA 7(a): supera el tope de $50,000 del SBA Microloan); el equipo de cocción (paelleras y quemadores) '
         'es pequeño: la van es la partida grande'),
    (42, '§1 4/5: proyecciones: {{eventos_a1}} eventos × {{invitados_evento}} invitados × {{precio_invitado}} → '
         '{{ventas_a1}} / {{ventas_a2}} / {{ventas_a3}}; EBITDA {{ebitda_pct_a1}}; equilibrio {{equilibrio_eventos}} '
         'eventos/año; DSCR mínimo {{dscr_min}}; y la frase honesta (D118): es el caso de un dueño-paella chef a tiempo '
         'completo con un segundo cocinero los fines de semana, no la media del primer año (orden de magnitud: ≈ $225K '
         'el año 1, Kit estimate)'),
    (43, '§1 5/5: el equipo: Owner / Paella Chef & Sales, lead cook / second paella chef, event staff (servers, buffet '
         'attendants) y prep cook / driver, todos W-2 ({{plantilla_puestos}} personas, {{plantilla_jornadas}} FTE); sin '
         'inventar trayectoria'),
    (46, '§2 1/5: qué vende y a quién: familias (backyard paella parties, cumpleaños, first communions, baptisms, '
         'quinceañeras), parejas (bodas, rehearsal dinners), empresas (live cooking corporativo y drop-off) y clientes '
         'premium (marisco y tapas); compran el espectáculo de la paella cocinada en vivo, el socarrat, y que llegue '
         'caliente y a tiempo, sin pensar en la logística'),
    (47, '§2 2/5: propuesta de valor: la paella «cooked live in front of your guests in a giant traditional pan» '
         '(zola.com, Viton Paella); el socarrat reveal; arroz bomba y azafrán; sofrito y caldo hechos la víspera; el '
         'paella chef en la estación; degustación previa. El precio INCLUYE al paella chef y al personal (otros los '
         'cobran aparte: cafesevilla.com)'),
    (48, '§2 3/5: modelo económico: precio por invitado {{precio_invitado}} sin sales tax con el paella chef, el '
         'personal y el service charge dentro ({{ventas_evento}} por evento de media); paella packages '
         '{{cuota_paquetes_pct}} de las ventas y el resto add-ons (tapas hour, postres, sangría sin alcohol y bebidas, '
         'alquileres, horas extra, travel fees); depósito para bloquear la fecha (los caterers US piden entre el 25 y '
         'el 50 %: Kit estimate; la calculadora propone 50 %); service charge ≠ gratuity; guest minimum de 20-30 '
         '(tasteofpaella.com, zola.com)'),
    (49, '§2 4/5: posicionamiento frente a los restaurantes españoles que hacen catering, los caterers generalistas y '
         'otros paella caterers; si nombras la venta callejera, «paella food trucks» (no es nuestro comprador); '
         'diferencial: cocinada en vivo, el precio incluye al paella chef, marisco de origen autorizado'),
    (50, '§2 5/5: paquetes, menu styles y tipos de evento: los 3 paquetes de la calculadora del kit (drop-off paella · '
         'live paella party · full-service live paella) + el interruptor «tapas hour»; 8 menu styles: seafood · '
         'chicken & seafood · chicken & chorizo · Valencian (rabbit on request) · farm vegetable (vegan) · paella negra '
         '· lobster & seafood (premium) · easy-eat peeled seafood; «fideua (noodle paella)» como nota de menú; tipos de '
         'evento: backyard paella party, boda con tapas hour, live cooking corporativo, rehearsal dinner, first '
         'communion / baptism / quinceañera, cumpleaños, drop-off corporativo, premium de marisco y tapas, vegano; '
         'guest minimum'),
    (53, '§3 1/6: el mercado US desde el lado del cliente: research §2 (búsquedas: «spanish catering» 2,900, «paella '
         'catering» 720, «paella party» 320, «tapas catering» 140; relacionadas: paella catering cost, menu, near me) '
         'sin tamaño de mercado inventado'),
    (54, '§3 2/6: bodas y fiestas: la paella en vivo con ensalada y pan va de $12-13 por plato (zola.com, Viton Paella) '
         'a $26-31 por persona y $45 la de langosta (tasteofpaella.com); en bodas, «couples usually spend $50» '
         '(weddingwire.com, Paella Time); en Florida la temporada alta es invierno-primavera (peak season con mínimo de '
         '25: tasteofpaella.com); sin porcentajes sin fuente'),
    (55, '§3 3/6: empresas: live cooking corporativo y drop-off entregado en caliente; menú español completo con '
         'personal $44-65 por persona (zola.com, Señor Pepe\'s; miamigrillcatering.com, que dobla el mínimo en las '
         'fiestas de fin de año); marketplaces corporativos (comisión del libro: {{marketplace_comision}}); holiday '
         'parties en diciembre'),
    (56, '§3 4/6: mezcla del ejemplo (Kit estimate, research §8): 25 drop-offs (30 invitados a $22), 60 backyard paella '
         'parties (45 a $34), 25 eventos de empresa (75 a $38: escribe «75 guests at $38», NUNCA «75 guests per event» '
         'ni «$38 per guest», que son el caso del BBQ y el gate los veta), 18 bodas y rehearsal dinners (110 a $52) y '
         '7 premium de marisco y tapas (70 a $65) = {{eventos_a1}} eventos; las bodas son el 13 % de los eventos y el '
         '33 % de las ventas; estacionalidad: Month 1 = marzo, picos en mayo, junio y octubre, enero y febrero flojos'),
    (57, '§3 5/6: tendencias con cuidado: comida española y tapas, cocina en vivo en bodas, sangria bars (weddingwire.com, '
         'Paella Time), flamenco y guitarra española; operadores que diversifican (alquileres, otras estaciones); sin '
         'cifras sin fuente'),
    (58, '§3 6/6: riesgos de demanda y REALISMO (D118): temporada de bodas, cancelaciones, viento y lluvia, burn bans '
         'para la leña, presupuestos corporativos, precio volátil del marisco; {{eventos_a1}} eventos al año son los de '
         'un dueño-paella chef a tiempo completo con segundo cocinero los fines de semana, no la media del primer año '
         '(≈ $225K el año 1, Kit estimate); el escenario pesimista agota la caja'),
    (61, '§4 1/6: panorama competitivo local: otros paella caterers (Taste of Paella, Señor Pepe\'s, Qué Paella como '
         'ejemplos leídos), restaurantes españoles que hacen catering (Café Sevilla), caterers generalistas, bandejas '
         'de supermercado y «paella food trucks»'),
    (62, '§4 2/6: cinco fuerzas de Porter aplicadas al paella catering (estructura del ES [62]): proveedores de marisco '
         'y arroz bomba, sustitutos (catering genérico, food trucks), clientes que comparan por persona, entrada fácil '
         'pero difícil de hacer bien a 40 invitados por paellera'),
    (63, '§4 3/6: competidores directos e indirectos y cómo compararse: precio por persona, guest minimum, qué incluye '
         '(paella chef, personal, dishes & flatware, travel fee: «included up to 20 mile radius» en cafesevilla.com), '
         'reseñas en The Knot, WeddingWire, Zola y Google; algunos cobran aparte al paella chef ($300 por 2 h en '
         'cafesevilla.com)'),
    (64, '§4 4/6: barreras de entrada: commissary con permiso (no desde casa), paelleras y quemadores (una paellera de 36 '
         'in ≈ $349 y un quemador de 3 aros ≈ $549: Kit estimate con precios de tienda.com), seguros con llama '
         'abierta, permisos del condado y del fire marshal, y el oficio del paella chef (el socarrat para 40 '
         'invitados)'),
    (65, '§4 5/6: factores críticos de éxito: puntualidad, paella caliente y segura (≥ 135 °F o time as a public health '
         'control), socarrat constante, reseñas, relación con venues y wedding planners'),
    (66, '§4 6/6: DAFO del concepto (commissary + paelleras y quemadores + espectáculo en vivo; inversión pequeña; '
         'holgura justa; marisco volátil; viento y lluvia)'),
    (69, '§5 1/7: estrategia: dos embudos (bodas: ciclo largo con degustación; empresas: live cooking y drop-off '
         'recurrente) + backyard parties por referidos'),
    (70, '§5 2/7: presencia digital: web con paquetes y precios «desde» por persona, formulario de presupuesto, Google '
         'Business Profile, Instagram con vídeo de la paella cocinada en vivo y del socarrat reveal'),
    (71, '§5 3/7: directorios y marketplaces: The Knot, WeddingWire, Zola, ezCater (comisión del libro: '
         '{{marketplace_comision}}) y Thumbtack'),
    (72, '§5 4/7: alianzas: venues (preferred vendor lists), wedding planners, office managers, la comunidad hispana '
         '(first communions, quinceañeras); bridal shows'),
    (73, '§5 5/7: degustaciones para prospectos (su línea de coste en el P&L: una paella pequeña cocinada en vivo) y el '
         'proceso propuesta → contrato → depósito'),
    (74, '§5 6/7: fidelización y referidos: empresas que repiten, familias que vuelven para la próxima celebración, '
         'reseñas después de cada evento'),
    (75, '§5 7/7: presupuesto: {{marketing_anual}} al año en el ejemplo; medir el coste por evento ganado'),
    (78, '§6 1/5: la base: commissary compartida con permiso (horas de producción para sofrito, caldo y marisco limpio, '
         'almacén frío y seco, sitio para paelleras y quemadores; pregunta si admite cilindros de propano: Kit): '
         '{{alquiler_mes}} al mes en el ejemplo; research: $15-$45 la hora (thefoodcorridor.com); commissary agreement '
         'por escrito; del ES: «es tuyo lo que viaja; lo que usas un día, lo alquilas»'),
    (79, '§6 2/5: el equipo y su orden de compra: paella burners & stands {{inv_quemadores}}, paelleras por tamaño '
         '{{inv_paelleras}} (36 in ≈ 40 invitados, 32 in ≈ 30, 26 in ≈ 18: Kit estimate), propane & fire-safety kit '
         '{{inv_propano}}, montaje y holding {{inv_montaje}} (carpa de la estación, mesas, lavamanos, coolers, '
         'chafing dishes, insulated carriers), van de carga usada {{inv_furgoneta}} + upfit {{inv_furgoneta_upfit}} '
         '(racks verticales para los cilindros); orden: primero lo que cocina (paelleras, quemadores, propano), luego '
         'lo que protege (carpa, extintores), luego lo que sirve'),
    (80, '§6 3/5: la operativa de un evento en fases: briefing 3 weeks out → visita al venue 2 weeks out → pedidos '
         '(marisco 1-2 días antes con sus etiquetas) → la víspera en la commissary: sofrito, caldo y marisco limpio, '
         'etiquetados → el día: llegada 2-3 h antes, montaje de la estación fuera de la carpa de invitados, encendido, '
         '≈ 1 h de cocción, ≈ 2 h de servicio y 1 h de recogida (miamigrillcatering.com), 1 persona del equipo por 25 '
         'invitados → limpieza y aceitado de las paelleras, cilindros cerrados. Nunca «D-1»'),
    (81, '§6 4/5: seguridad del arroz y del marisco en la operativa: el arroz cocido es TCS y el B. cereus aparece en '
         'brotes por mal hot holding de arroz (Food Code, Anexo 3): servir a ≥ 135 °F o con time as a public health '
         'control de 4 h con SOP escrito; las sobras, a la basura; el MÍNIMO del Food Code: pollo 165 °F, pescado y '
         'marisco 145 °F 15 s, chorizo crudo mexicano 155 °F 17 s (el curado español es listo para comer); marisco '
         'crudo en coolers a ≤ 41 °F; shellstock tags; alérgenos (crustáceos y pescado entre los 9 mayores; los '
         'moluscos se declaran igual; huevo del alioli, trigo, sulfitos de la gamba congelada)'),
    (82, '§6 5/5: proveedores: marisco de origen autorizado (mejillones y almejas con la etiqueta del dealer), pollo y '
         'verdura, arroz bomba y azafrán de un importador de productos españoles, cash-and-carry tipo Restaurant Depot, '
         'propano (intercambio o recarga), party rentals; mantenimiento de la van y repuesto de paelleras, quemadores y '
         'mangueras'),
    (85, '§7 1/6: estructura: Owner / Paella Chef & Sales, lead cook / second paella chef (part-time W-2), event staff '
         '(servers, buffet attendants; hourly W-2) y prep cook / driver (part-time W-2)'),
    (86, '§7 2/6: coste de personal: {{personal_a1}} el año 1 ({{personal_pct}} de las ventas), con el sueldo del dueño '
         'dentro; el del dueño y el del segundo paella chef son fijos y el del event staff depende de las horas de '
         'evento (sin cifra propia: no hay token)'),
    (87, '§7 3/6: personal por evento: {{horas_evento}} horas por persona × {{personas_evento}} personas por evento, '
         'cobertura {{cobertura_horas}}; ≈ 1 persona del equipo por 25 invitados (miamigrillcatering.com); un paella '
         'chef lleva unas 3 paelleras y hace falta un ayudante desde 4 paelleras u 80 invitados (Kit estimate); el '
         'libro reparte la nómina por igual en los 12 meses (conservador)'),
    (88, '§7 4/6: W-2 frente a 1099 (FLSA; California AB5), nunca «freelance»; cargas {{cargas_pct}}; mínimo federal y '
         'estatal; sueldos BLS OEWS mayo 2025 (bls.gov): cooks, restaurant media $18.62/h y p75 $21.45/h; food servers, '
         'nonrestaurant media $17.37/h y p75 $18.51/h (no escribas «chef» suelto: solo la tabla D19 nombra esa serie); '
         'workers\' comp opcional en Texas'),
    (89, '§7 5/6: formación: ServSafe Manager (Certified Food Protection Manager), food handler cards, seguridad del '
         'propano y del fuego, el guion del espectáculo (el socarrat reveal), alérgenos (crustáceos y pescado entre '
         'los 9 mayores US)'),
    (90, '§7 6/6: service charge frente a gratuity (IRS Rev. Rul. 2012-18): el service charge obligatorio es salario; la '
         'gratuity voluntaria es del personal'),
    (93, '§8 1/7: viabilidad: ventas del año 1 {{ventas_a1}}, margen bruto {{margen_bruto_pct}}, EBITDA {{ebitda_a1}} '
         '({{ebitda_pct_a1}}); {{ventas_evento}} por evento; precios dentro de las bandas leídas (paella en vivo $12-31 '
         'por persona; menú español con personal $44-65)'),
    (94, '§8 2/7: inversión con tokens: {{inv_quemadores}}, {{inv_paelleras}}, {{inv_propano}}, {{inv_furgoneta}}, '
         '{{inv_furgoneta_upfit}}, {{inv_montaje}}, {{inv_permisos}}, {{inv_lanzamiento}}, {{inv_stock}} → {{capex}} '
         '(con la contingencia del 10 % sobre quemadores, paelleras, la van, su upfit y la inspección, calculada por '
         'fórmula); fondo de maniobra {{fondo_maniobra}}; total {{inversion_total}}; financiación SBA 7(a)'),
    (95, '§8 3/7: proyección a 3 años: {{ventas_a1}} / {{ventas_a2}} / {{ventas_a3}} (crecen los EVENTOS: '
         '{{crecimiento_a2}} y {{crecimiento_a3}}); resultado neto {{resultado_neto_a1}} / {{resultado_neto_a2}} / '
         '{{resultado_neto_a3}}; el {{impuesto_beneficios}} hace de impuesto sobre la renta: con una LLC pass-through lo '
         'paga el dueño en su declaración, así que la reserva se mantiene'),
    (96, '§8 4/7: costes: paella packages {{coste_paquetes_pct}} de sus ventas, mercancía total {{cogs_pct}}, '
         'desechables y combustible de cocina {{consumibles_pct}} (el propano), personal {{personal_pct}}, commissary y '
         'almacén {{ocupacion_pct}}; benchmarks: food cost de catering 28-35 % (galleysolutions.com), neto 7-8 % '
         '(itsacheckmate.com)'),
    (97, '§8 5/7: punto de equilibrio en EVENTOS al año: {{equilibrio_eventos}} (contable) y '
         '{{equilibrio_caja_eventos}} (caja) frente a {{eventos_a1}} del plan; holgura {{holgura_caja_pct}} (los eventos '
         'pueden caer {{caida_absorbible_pct}} antes de no cubrir la caja); si la holgura es justa, DECIRLO; el libro '
         'muestra la cifra exacta y el plan la redondea a eventos enteros'),
    (98, '§8 6/7: caja y retorno: cobras a {{cobro_dias}} días de media y pagas a los proveedores a {{pago_dias}} días '
         '(CADA TOKEN EN SU CELDA, D113); las nóminas salen cada mes; saldo mínimo {{saldo_minimo}} en el mes '
         '{{mes_saldo_minimo}}, payback {{payback}}, DSCR {{dscr_min}}; el depósito no se modela y mejora la caja real'),
    (99, '§8 7/7: escenarios: pesimista {{pesimista_eventos}} eventos × {{pesimista_precio}} × {{pesimista_invitados}} '
         'invitados → {{pesimista_ventas}}, resultado {{pesimista_resultado}} y caja estimada {{pesimista_caja}} (si es '
         'negativa, DECIRLO: «the cash runs out»); optimista {{optimista_eventos}} eventos → {{optimista_ventas}} y '
         '{{optimista_resultado}}; recordar que {{eventos_a1}} eventos no son la media del primer año'),
    (111, '§10 1/7: conclusión: por qué el modelo se sostiene (cocinar en vivo ES el producto, sin local, inversión '
          'pequeña, dos motores de demanda: celebraciones privadas y empresas) y la advertencia honesta (holgura justa; '
          'el pesimista agota la caja)'),
    (112, '§10 2/7: riesgos y mitigación: cancelación (depósito y tramos), viento, lluvia o fuego no autorizado (carpa '
          'de la estación, inducción en interiores, cocinar en la commissary y servir en caliente, nueva fecha), arroz '
          'fuera de temperatura (≥ 135 °F o time as a public health control, sobras a la basura), subida del marisco '
          '(revisa la calculadora con tus precios), incidente con el propano (prueba de fugas, extintores), falta de '
          'personal los sábados de temporada, inspecciones'),
    (113, '§10 3/7: fortalezas competitivas: el paella chef y el espectáculo en vivo, el precio que incluye al chef y al '
          'personal, los 8 menu styles, commissary y permisos en regla'),
    (114, '§10 4/7: hoja de ruta en las 6 fases del checklist (Business Setup → Propane & Permits → Equipment → Staff → '
          'Marketing → First 90 Days): la van y los permisos del fire marshal en la Phase 2; las fases se solapan; '
          'ningún evento pagado con permisos abiertos'),
    (115, '§10 5/7: KPIs: eventos al mes, precio por invitado, arroz (oz) por invitado e invitados reales por paellera, '
          'food cost, propano por evento, horas de personal por evento, conversión de propuestas, cancelaciones, '
          'reseñas'),
    (116, '§10 6/7: visión a 3 años: más empresas recurrentes, segundo paella chef a tiempo completo o una segunda '
          'estación con otra van; local propio solo si los números lo piden'),
    (117, '§10 7/7: cierre: los siguientes pasos con el Excel, la calculadora de precios (con su «Paella Yield & Pan '
          'Sizing» y su «Shopping List by Guest Count») y el checklist del kit'),
])


def _json_ranuras(base, patron):
    out = {}
    for f in ('a', 'b'):
        p = os.path.join(base, patron % f)
        if os.path.exists(p):
            out.update({int(k): v for k, v in json.load(open(p, encoding='utf-8')).items()})
    return out


def _notas_docx():
    """Nota de cada ranura: nivel + pista + PROPUESTA EN DEL BBQ (misma ranura) + ES 2.2 del paellero (adaptar / nueva)."""
    es = _json_ranuras(os.path.join(PAE, 'textos'), 'pae_es_%s.json')
    bbq = _json_ranuras(BBQ, 'docx_en_bbq_%s.json')
    out = OrderedDict()
    for i, n in sorted(list(_NOTAS_SECCION.items()) + list(_N9.items())):
        nivel = _NIVEL.get(i, 'A')
        n = '[%s] %s' % (_NIVEL_TXT[nivel], n)
        if i in bbq:
            n += ' ‖ PROPUESTA EN DEL BBQ EN ESTA RANURA (la forma; cero vocabulario BBQ): «%s»' % bbq[i]
        if i in es and nivel != 'L':
            n += (' ‖ ES 2.2 DEL PAELLERO EN ESTA RANURA (referencia de contenido; sus cifras, sus {TOKENS} en '
                  'mayúsculas y todo lo español NO se usan): «%s»' % es[i])
        out[i] = n
    return out


DOCX_NOTAS = OrderedDict([('pael', _notas_docx())])

# ==========================================================================
# Pistas por celda (extraer_textos.py → textos_es.json → tandas)
# ==========================================================================
_CASO = ('D118: caso US = 135 eventos/año × 58 invitados × $40 por invitado (sin sales tax, con el paella chef, el '
         'personal y el service charge dentro, sin la gratuity voluntaria) ≈ $313,200 (research §8; la calibración D15 '
         'puede subir B4 de 5 en 5 hasta 150); drivers: B4 = eventos/año, B5 = precio por invitado, B6 = invitados por '
         'evento. Las notas describen el MÉTODO: sin cifras del caso (cambian al recalibrar). La propuesta EN es la del '
         'BBQ en esta celda: cambia lo que hable de smoker trailer, pit, carne, leña o del caso del BBQ')
CELDA_PISTAS = OrderedDict([
    (('PAEP', _S, 'C4'), _CASO + '; los años 2-3 crecen en EVENTOS (B7/B8); compara con la capacidad del equipo (fila '
                                 '51); el ejemplo es un dueño-paella chef a tiempo completo con segundo cocinero los fines '
                                 'de semana, no la media del primer año'),
    (('PAEP', _S, 'C5'), _CASO + '; precio medio por invitado de la MEZCLA (drop-off, backyard parties, empresa, bodas, '
                                 'premium) SIN sales tax, con el paella chef, el personal y el service charge dentro y SIN '
                                 'la gratuity voluntaria. Los operadores cotizan por persona (paella en vivo con ensalada y '
                                 'pan $12-31 en tasteofpaella.com y zola.com; menú español con personal $44-65 en '
                                 'miamigrillcatering.com y zola.com): la calculadora del kit cotiza 3 paquetes por '
                                 'invitado; para pasar de ella a esta celda, pondera el precio de cada paquete por sus '
                                 'invitados del año (D123)'),
    (('PAEP', _S, 'C6'), _CASO + '; invitados medios por evento; la mezcla del ejemplo va de drop-offs de 30 a bodas de '
                                 '110 (guest minimums de los operadores leídos: 20 en tasteofpaella.com, 30 en zola.com)'),
    (('PAEP', _S, 'C7'), 'D118: crecimiento de EVENTOS 10 % en el año 2 (reseñas y bodas reservadas con meses; lo limita '
                         'un dueño-paella chef con una van)'),
    (('PAEP', _S, 'C8'), 'D118: crecimiento de EVENTOS 6 % en el año 3, por la misma razón'),
    (('PAEP', _S, 'C11'), 'D121: cuota de PAELLA PACKAGES (paella cocinada en vivo, ensalada y pan, paella chef y personal) '
                          '88 %; el resto (fila 12) son add-ons: tapas, postres, sangría sin alcohol y bebidas, '
                          'alquileres, horas extra, travel fees. Es una ENTRADA'),
    (('PAEP', _S, 'C12'), 'D121: calculado como el resto: paella packages + add-ons = 100 %'),
    (('PAEP', _S, 'C13'), 'D118: coste de los paella packages 28 % = arroz, marisco, pollo y chorizo, azafrán, caldo, '
                          'ensalada y pan, con un colchón por sobreproducción y por el precio volátil del marisco (Kit '
                          'estimate); el food cost de catering va del 28 al 35 % (galleysolutions.com)'),
    (('PAEP', _S, 'C14'), 'D118: coste de los add-ons 35 % (Kit estimate: tapas y postres, alquileres que repercutes casi '
                          'a coste)'),
    (('PAEP', _S, 'C15'), 'D121: desechables y combustible de cocina 3.5 % (Kit estimate: propano ≈ 6-8 lb por evento de '
                          '60 invitados, $10-15, + desechables ≈ $0.75 por invitado; cubre la leña donde un permiso la '
                          'admita); escala con las paelleras y los eventos; el combustible del VEHÍCULO va en la fila 27 '
                          'del P&L'),
    (('PAEP', _S, 'C16'), 'D118: marketplaces de catering corporativo (p. ej. ezCater): 5 % de las ventas en el ejemplo '
                          '(parte del drop-off corporativo)'),
    (('PAEP', _S, 'C17'), 'D118: comisión del marketplace 15 % (ezCater cobra ~15 %: Kit estimate)'),
    (('PAEP', _S, 'C18'), 'D118: tarjeta 3 %: los particulares pagan depósito y saldo con tarjeta; algunas empresas, por '
                          'ACH o cheque'),
    (('PAEP', _S, 'C24'), 'D121: commissary compartida con permiso: horas de producción (sofrito, caldo, marisco limpio) + '
                          'almacén frío y seco + sitio para paelleras y quemadores (pregunta si admite cilindros de '
                          'propano); research: ≈ 30 h × $22 + almacén, Kit estimate; $15-$45 la hora, el 42 % cobra '
                          '$20-$29 (thefoodcorridor.com); nunca «support kitchen»'),
    (('PAEP', _S, 'C25'), 'D121: meses de depósito de la commissary'),
    (('PAEP', _S, 'C26'), 'D121: agua, luz y teléfono que no cubre la commissary; SIN propano: el combustible de cocina es '
                          'variable (fila 15)'),
    (('PAEP', _S, 'C27'), 'D121: seguros al año = general liability / BOP que NO excluya la llama abierta en eventos + '
                          'commercial auto + workers\' comp + inland marine para paelleras y quemadores (Kit estimate por '
                          'póliza; Insureon publica medias: GL $45/mes, commercial auto $204/mes, insureon.com); los '
                          'venues piden COI y additional insured; liquor liability solo si tu personal sirve el alcohol '
                          'del cliente'),
    (('PAEP', _S, 'C28'), 'D121: varios 3 % de las ventas: imprevistos de cada evento (marisco extra, hielo, limones, '
                          'parking en el venue); es VARIABLE. SIN combustible: el de la van va en la fila 27 del P&L '
                          '(fijo) y el propano, en la fila 15'),
    (('PAEP', _S, 'C30'), 'D118: fondos propios del dueño (≈ 30 % de la necesidad en el ejemplo)'),
    (('PAEP', _S, 'C31'), 'D118: préstamo que calibra el libro: supera el tope de $50,000 del SBA Microloan, así que el '
                          'ejemplo encaja en un SBA 7(a) o un préstamo bancario; el lender pide plan y proyecciones'),
    (('PAEP', _S, 'C33'), 'D118: 7 años: la van, los quemadores y las paelleras pierden valor antes que un local'),
    (('PAEP', _S, 'C44'), 'D120: 7 años: quemadores y soportes, paelleras, la van usada y su upfit, y la inspección del '
                          'fire marshal / del propano (la base de vida del vehículo, fila 31 de "Startup Costs")'),
    (('PAEP', _S, 'C45'), 'D120: 5 años: kit de propano y seguridad, fit-out de la commissary, software, smallwares y '
                          'utensilios de paella, montaje y holding'),
    (('PAEP', _S, 'C51'), 'D118: DATO INFORMATIVO (no entra en ningún cálculo): el techo de eventos al año que tu equipo '
                          'puede atender (una van; dos eventos el mismo sábado con el segundo paella chef; los sábados de '
                          'mayo, junio y octubre son el cuello de botella); compáralo con la fila 4 y con el optimista'),
    (('PAEP', _S, 'C52'), 'D118: rampa 50 % → 8 meses: las bodas se reservan con meses de antelación y las empresas tardan '
                          'en repetir'),
    (('PAEP', _S, 'C54'), 'D118: 1 mes de commissary antes de abrir (pruebas por tamaño de paellera, permisos y preventa '
                          'en el primer bridal show)'),
    (('PAEP', _S, 'C55'), 'D120: imprevistos 10 % sobre quemadores, paelleras, la van, su upfit y la inspección (filas 7, '
                          '8, 11, 12 y 15 de "Startup Costs")'),
    (('PAEP', _S, 'C58'), 'D118: cobro medio 7 días: depósito al reservar la fecha (los caterers US piden entre el 25 y el '
                          '50 %: Kit estimate; la calculadora propone 50 %) y saldo antes del evento; empresas a 30 días; '
                          'el libro no modela anticipos (nota de la Tesorería)'),
    (('PAEP', _S, 'C62'), 'D117/D118: alcohol 0 %: sin licencia no vendes alcohol; la sangría va sin alcohol o con el vino '
                          'que compra el cliente, sin margen (docx §9); nunca «bartender» (gate)'),
    (('PAEP', _S, 'C63'), 'D118: solo si vendieras alcohol con licencia (0 % en este plan)'),
    # Startup Costs, notas de la columna D (D120; research §5, §8)
    (('PAEP', _I, 'D7'), 'D120: cuatro quemadores de paella de 3 aros con patas (un quemador XL de 3 aros con trípode y '
                         'regulador para paelleras de hasta 36 in ronda los $549: Kit estimate con precios de tienda.com), '
                         'un rolling stand ($399 el de 2 aros) y wind guards'),
    (('PAEP', _I, 'D8'), 'D120: paelleras por tamaño: 2 de 36 in (90 cm) ≈ 40 invitados cada una, 3 de 32 in (80 cm) ≈ '
                         '30 y 3 de 26 in (65 cm) ≈ 18 (Kit estimate); una de 36 in ronda los $349 (tienda.com, Kit '
                         'estimate); acero al carbono o esmaltadas'),
    (('PAEP', _I, 'D9'), 'D120: kit de propano y seguridad: ocho cilindros de 20 lb (≈ 4.7 gal cada uno), reguladores, '
                         'mangueras en fecha, 2 extintores (el fire marshal dice cuáles) y manta ignífuga'),
    (('PAEP', _I, 'D10'), 'D120: fit-out de la commissary: estanterías, sheet pans, cubetas etiquetadas para sofrito y '
                          'caldo'),
    (('PAEP', _I, 'D11'), 'D120: van de carga usada: lleva paelleras, quemadores, cilindros (de pie, sujetos y con '
                          'ventilación) y coolers; NO es frigorífica: el marisco crudo viaja en coolers con hielo a ≤ 41 '
                          '°F y la paella del drop-off en insulated carriers a ≥ 135 °F'),
    (('PAEP', _I, 'D12'), 'D120: upfit de la van: estanterías, racks verticales para los cilindros, sujeciones y '
                          'rotulación (wrap); comprueba que tu seguro lo cubre'),
    (('PAEP', _I, 'D13'), 'D120: LLC + contrato tipo revisado por un abogado (depósito, tramos de cancelación, recuento '
                          'final, plan B por viento y lluvia, cláusula de fuego no autorizado)'),
    (('PAEP', _I, 'D14'), 'D120: permisos y certificaciones del año 1: catering / health permit del condado, temporary '
                          'event permits, business license, sales tax permit, ServSafe Manager, food handler cards; varía '
                          'mucho por estado y condado'),
    (('PAEP', _I, 'D15'), 'D120: permiso del fire marshal o del evento e inspección del montaje de propano SOLO si tu '
                          'ciudad o el venue lo exigen; si no, pon 0'),
    (('PAEP', _I, 'D16'), 'D120: software de catering (propuestas, contratos con firma electrónica, depósitos y saldos) + '
                          'lector de tarjetas + tablet'),
    (('PAEP', _I, 'D17'), 'D120: smallwares y utensilios de paella: paletas, cucharones, cuchillos, tablas de colores, '
                          'hotel pans, termómetros de sonda calibrados, guantes de calor; se amortizan'),
    (('PAEP', _I, 'D18'), 'D120: inventario inicial: arroz bomba, azafrán, base de caldo, marisco y pollo para las '
                          'pruebas, desechables de los primeros eventos'),
    (('PAEP', _I, 'D19'), 'D120: web, fotos y vídeo de la paella cocinada en vivo, altas en The Knot / WeddingWire / Zola '
                          '/ ezCater, Google Business Profile y el primer bridal show'),
    (('PAEP', _I, 'D20'), 'D120: montaje y holding: carpa para la estación de cocina (fuera de la carpa de invitados), '
                          'mesas plegables, lavamanos (San Diego County pide uno de 5 gal: sandiegocounty.gov), coolers '
                          'para el marisco, 6 chafing dishes para las tapas, insulated carriers para el drop-off; nunca '
                          '«Cambro» (es marca)'),
    (('PAEP', _I, 'D27'), 'D120: lo que compras: quemadores, paelleras, la van y su upfit, el kit de propano, el montaje, '
                          'el lanzamiento y la constitución; el colchón de caja no es inversión'),
    # 3-Year P&L, notas (D121, D122)
    (('PAEP', _P, 'F10'), 'D121: ventas de paella packages por invitado: la paella cocinada en vivo con ensalada y pan, el '
                          'paella chef y el personal (drop-off, backyard parties, empresa, bodas, premium)'),
    (('PAEP', _P, 'F11'), 'D121: ventas de add-ons: tapas hour, postres, sangría sin alcohol y bebidas, alquileres, horas '
                          'extra, travel fees'),
    (('PAEP', _P, 'F16'), 'D121: comisiones de los marketplaces de catering corporativo (p. ej. ezCater) sobre las ventas '
                          'de ese canal'),
    (('PAEP', _P, 'F22'), 'D121: el importe mensual se teclea en "0. Assumptions"; aquí × 12: commissary + almacén de '
                          'paelleras y quemadores'),
    (('PAEP', _P, 'F24'), 'D121: agua, luz y teléfono que no cubre la commissary; sin propano (va en la fila 15)'),
    (('PAEP', _P, 'F27'), 'D121: combustible, mantenimiento y registro de la van: FIJO en este libro'),
    (('PAEP', _P, 'F32'), 'D121: retirada de residuos, aceite usado y conchas con un hauler con licencia (a menudo lo '
                          'gestiona la commissary)'),
    (('PAEP', _P, 'F33'), 'D121: repuesto de paelleras (se deforman), quemadores (aros obstruidos) y mangueras (caducan)'),
    (('PAEP', _P, 'F34'), 'D121: ServSafe Manager (Certified Food Protection Manager) y food handler cards del equipo, y su '
                          'renovación'),
    (('PAEP', _P, 'F35'), 'D121: degustaciones para parejas, planners y empresas (una paella pequeña cocinada en vivo); '
                          'muchos operadores las descuentan si reservan'),
    (('PAEP', _P, 'F51'), 'D122: suelo del margen bruto del motor 58 % (kit benchmark, editable): el margen bruto del libro '
                          'resta también tarjeta, marketplace y varios'),
    (('PAEP', _P, 'F53'), 'D122: techo del coste de mercancía 35 % (kit benchmark, editable; food cost de catering 28-35 %, '
                          'galleysolutions.com)'),
    (('PAEP', _P, 'F54'), 'D122: techo de personal 38 % (kit benchmark, editable), con el sueldo del dueño dentro'),
    (('PAEP', _P, 'F55'), 'D122: techo de commissary y almacén 7 % (kit benchmark, editable): no hay local'),
    (('PAEP', _P, 'F56'), 'D122: suelo del resultado neto 5 % (kit benchmark, editable; neto medio de catering 7-8 %, '
                          'itsacheckmate.com)'),
    # Staffing, notas (D121)
    (('PAEP', _R, 'J5'), 'D121: Owner / Paella Chef & Sales: vende, hace las degustaciones y cocina la paella en los '
                         'eventos; el resto de su retribución sale del beneficio'),
    (('PAEP', _R, 'J6'), 'D121: lead cook / second paella chef (part-time W-2, 0.4 FTE): lleva la segunda estación en los '
                         'eventos grandes y el segundo evento del sábado; paga entre la media y el p75 de «cooks, '
                         'restaurant» (BLS OEWS mayo 2025: $18.62 y $21.45)'),
    (('PAEP', _R, 'J7'), 'D121: event staff por horas y en W-2 (servers, buffet attendants); su FTE es una fracción; ≈ 1 '
                         'persona del equipo por 25 invitados (miamigrillcatering.com); la gratuity voluntaria es suya'),
    (('PAEP', _R, 'J8'), 'D121: prep cook / driver part-time W-2: sofrito, caldo y marisco limpio en la commissary, carga '
                         'y conducción de la van'),
    (('PAEP', _R, 'J18'), 'D118: horas por persona y evento: preparación, carga, viaje, llegada 2-3 h antes, montaje y ≈ 1 '
                          'h de cocción, ≈ 2 h de servicio y recogida'),
    (('PAEP', _R, 'J19'), 'D118: personas por evento: drop-off 1 · backyard party 2 · empresa 3 · boda 4.5 · premium 4 '
                          '(Kit estimate); ponderado con la mezcla del docx, ≈ 2.5'),
    (('PAEP', _ES, 'E23'), 'D118: la MISMA plantilla en los tres escenarios; en el pesimista el coste real del event staff '
                           'baja con los eventos (pagas horas por evento), así que el resultado real sería algo mejor'),
    (('PAEP', _N, 'A5'), 'D117: «0. Assumptions» es la hoja de mando: eventos al año, precio por invitado sin sales tax, '
                         'invitados por evento, mezcla paella packages / add-ons, coste de mercancía; la van es de carga, '
                         'no frigorífica'),
    (('PAEP', _N, 'A12'), 'SPEC §4.1 línea 8 (I1): el Word del kit usa las MISMAS cifras de ejemplo que este libro; si '
                          'cambias el libro, actualiza las del Word. La calculadora de precios es otro fichero (con su '
                          'Paella Yield & Pan Sizing y su Shopping List) y no lee este libro'),
])
_D18 = ('D18 (paella caterer): la propuesta es la del BBQ EN (o del Catering) en esa celda, que ya describe el MÉTODO del '
        'libro para un negocio de eventos con comida; reescribe SOLO lo que hable de smoker trailer, pit, leña, carne o '
        'BBQ → quemadores y paelleras, la van de carga, el propano (combustible de cocina), la commissary, el paella '
        'chef. Sin cifras del caso')
_D18_FILA = OrderedDict([
    (39, 'Fila del espacio: «Commissary kitchen and equipment storage» (el coste del espacio, en "0. Assumptions")'),
    (42, 'Fila de seguros del vehículo: los de la van (commercial auto) y el inland marine de paelleras y quemadores, una '
         'sola vez y como gasto anual'),
    (43, 'Fila de combustible de cocina (D121): «Propane (and wood where a permit allows it)»: va en la línea de '
         'desechables y combustible de cocina (variable, % de ventas), no en utilities ni en una línea aparte'),
    (49, 'Fila «Fuel and miscellaneous»: A «Miscellaneous event costs» · B «A miscellaneous line typed in among the fixed '
         'costs» · C «A percentage of sales, treated as a variable cost; van fuel has its own fixed line» · D «Extra '
         'seafood, ice, lemons and venue parking rise and fall with the number of events: among the fixed costs they '
         'would distort the break-even.»'),
])
for _f in range(35, 52):
    for _col in 'ABCD':
        CELDA_PISTAS[('PAEP', _N, '%s%d' % (_col, _f))] = _D18 + ('. ' + _D18_FILA[_f] if _f in _D18_FILA else '')
PISTA_D19_GENERICA = ('Celda a celda: escribe SOLO el texto de ESTA celda (una tabla o una tarea): mira su pista '
                      'propia')
_D19_BASE = ('D19/D122: tabla «US PAELLA CATERING BENCHMARKS (sourced) AND KIT ESTIMATES» (Benchmark | Value | Source | '
             'Note). Value en formato US; Source = el DOMINIO de la fuente LEÍDA de research §1 y §5, o «Kit estimate» si '
             'allí figura como «(resumen)». Esta fila: ')
_D19 = OrderedDict([
    (55, 'precio por persona de la paella cocinada en vivo con ensalada y pan: $12-13 por plato (zola.com, Viton Paella) '
         'a $26-31 por persona y $45 la de langosta (tasteofpaella.com) [NUEVA]'),
    (56, 'menú español completo con personal: $44-65 por persona (zola.com, Señor Pepe\'s desde $44; '
         'miamigrillcatering.com $65 → $53 según tramo); en bodas «couples usually spend $50» (weddingwire.com, Paella '
         'Time) [NUEVA]'),
    (57, 'arroz por invitado: 80-100 g (3-3.5 oz) de arroz crudo; +10-15 % en grupos; caldo 2-3 veces el volumen de '
         'arroz — Kit estimate (las fuentes solo se leyeron en resumen) [NUEVA]'),
    (58, 'margen neto 7-8 % de media en catering — itsacheckmate.com [propuesta del BBQ: vale si habla de catering en '
         'general]'),
    (59, 'invitados por paellera: 36 in (90 cm) ≈ 40 · 32 in (80 cm) ≈ 30 · 26 in (65 cm) ≈ 18 — Kit estimate [NUEVA]'),
    (60, 'food cost de catering 28-35 % del precio — galleysolutions.com [propuesta del BBQ]'),
    (61, 'paelleras y quemadores: paellera de 36 in ≈ $349 · quemador XL de 3 aros con trípode y regulador ≈ $549 · '
         'rolling stand de 2 aros $399 · alquiler de una de 36 in $39.90 — Kit estimate (precios de tienda en resumen) '
         '[NUEVA]'),
    (62, 'comisión de marketplace corporativo ~15 % (ezCater) — Kit estimate [propuesta del BBQ]'),
    (63, 'paella chef y attendant cobrados aparte: «Paella chef (required)» $300 por 2 h (+$85 la hora extra), buffet '
         'attendant $190 por 2 h, vajilla $5-10 por persona, mínimo $1,250 — cafesevilla.com [NUEVA: la fila 63 del BBQ '
         'citaba operadores BBQ y no vale]'),
    (64, 'sueldos BLS OEWS mayo 2025: cooks, restaurant (35-2014) media $18.62/h, p75 $21.45; food servers, '
         'nonrestaurant (35-3041) media $17.37/h, p75 $18.51; chefs and head cooks (35-1011) mediana $30.03/h — bls.gov '
         '(ÚNICA celda del kit donde vale «chefs and head cooks») [propuesta del BBQ]'),
    (65, 'commissary compartida $15-$45 la hora (el 42 % cobra $20-$29) — thefoodcorridor.com (2023 Shared Kitchen '
         'Operator Survey) [propuesta del BBQ]'),
    (66, 'mínimos: 20-30 invitados (tasteofpaella.com: 20, 25 en peak season; zola.com, Viton Paella: 30 en vivo) y '
         '$500-1,600 (zola.com: Qué Paella $500, Señor Pepe\'s $1,600) [NUEVA]'),
    (67, 'seguros (Insureon, < 5 empleados): general liability $45/mes, BOP $96, workers\' comp $82, commercial auto $204 '
         '— insureon.com [propuesta del BBQ; nota: confirma que la GL no excluye la llama abierta en eventos]'),
    (68, 'propano y desechables por evento: 6-8 lb de propano (≈ $10-15) en un evento de 60 invitados + desechables ≈ '
         '$0.75 por invitado — Kit estimate; personal: 1 persona del equipo por 25 invitados (miamigrillcatering.com) '
         '[NUEVA]'),
])
for _f, _p in _D19.items():
    for _col in 'ABCD':
        CELDA_PISTAS[('PAEP', _N, '%s%d' % (_col, _f))] = _D19_BASE + _p

# Checklist (D125): una pista por FILA de tarea (columnas B tarea · C responsable · D plazo · E nota práctica). La
# propuesta EN es la tarea del BBQ en ESA celda (columna C ya con «Paella chef»). Cada fila: (columnas que CAMBIAN,
# pista). '' = la tarea sobrevive tal cual (sus celdas limpias entran directas: GLB-check); 'E', 'BE'… = esas columnas
# van a la tanda; 'BCDE' = tarea nueva. Toda celda con vocabulario BBQ va a la tanda aunque su columna no esté marcada
_CK = ('D125: escribe una TAREA de un live paella caterer (B tarea · C responsable · D plazo · E nota práctica, una celda '
       'cada vez) con el checklist ES del paellero (fuente_es_pael.json) + research §6 y el glosario §9; columna C: '
       '«Paella chef» (nunca «Pitmaster» ni «chef» suelto); plazos US («Week 1», «3 weeks out», nunca «D-21»); '
       + REGLA_UNIDADES + '. Esta fila: ')
TAREAS_PAEL = OrderedDict([
    ('F1 - Constitución', [
        ('', 'contador / bookkeeper y estimated taxes trimestrales (semana 1) [sobrevive]'),
        ('E', 'estructura: LLC, con o sin elección de S corp; en E, la responsabilidad importa porque cocinas con llama '
              'abierta (propano) en eventos ajenos, no «tow a smoker» [sobrevive con ajuste: E]'),
        ('', 'registrar la LLC en el Secretary of State + registered agent + operating agreement [sobrevive]'),
        ('', 'EIN + alta estatal de nóminas y desempleo [sobrevive]'),
        ('', 'cuenta bancaria del negocio y finanzas separadas [sobrevive]'),
        ('E', 'seller\'s permit / sales tax permit: en muchos estados tributa toda la factura de catering (la paella, el '
              'personal, los alquileres y, según el estado, el service charge); sin «smoked meats» [sobrevive con '
              'ajuste: E]'),
        ('', 'business license de la ciudad o el condado (+ DBA) [sobrevive]'),
        ('E', 'solicitar el préstamo a dos lenders (banco o SBA 7(a)) con el plan, el Excel y presupuestos escritos de la '
              'van, las paelleras y los quemadores; no firmar la van antes de la aprobación [sobrevive con ajuste: E]'),
        ('BE', 'contrato tipo de paella catering con un abogado: depósito para bloquear la fecha (los caterers US piden '
               '25-50 %; la calculadora del kit propone 50 %), saldo antes del evento, tramos de cancelación sin huecos, '
               'recuento final y guest minimum, service charge frente a gratuity, PLAN B de viento y lluvia (carpa de la '
               'estación, interior con inducción o nueva fecha), cláusula por si el venue o un burn ban no permiten el '
               'fuego (paella cocinada en la commissary y servida en caliente), el vino de la sangría lo compra el '
               'cliente, uso de fotos [sobrevive con ajuste: B y E]'),
        ('BE', 'plan de seguridad alimentaria basado en HACCP para paella: el arroz cocido es TCS (B. cereus); servir a ≥ '
               '135 °F (57 °C) o con time as a public health control de 4 h con SOP escrito, hora marcada y descarte '
               '(3-501.19, si tu condado lo admite); MÍNIMOS del Food Code: pollo 165 °F (74 °C), pescado y marisco '
               '145 °F (63 °C) 15 s, chorizo crudo mexicano 155 °F (68 °C) 17 s (el curado español es listo para comer); '
               'sobras a la basura, nunca enfriadas para reutilizar; marisco de approved source y shellstock tags '
               'guardadas 90 días (3-203.12) [sobrevive con ajuste: B y E]'),
        ('', 'Certified Food Protection Manager (ServSafe Manager) del dueño / paella chef [sobrevive]'),
    ]),
    ('F2 - Vehículo', [
        ('BE', 'elegir una commissary compartida con permiso: horas para sofrito, caldo y marisco limpio, almacén frío y '
               'seco, sitio para paelleras y quemadores; pregunta si admite cilindros de propano; nunca cocina de casa '
               '(Food Code 3-201.11(B)) [sobrevive con ajuste: B y E]'),
        ('E', 'commissary agreement por escrito: horas, zonas de almacén (paelleras, quemadores, cilindros si los admite) '
              'y limpieza [sobrevive con ajuste: E]'),
        ('BE', 'catering / health permit del condado + pregunta si cocinar el arroz en el evento cabe en su regla (en '
               'California, «limited food preparation» en eventos privados con catering: CalRFC §113818, San Diego '
               'County): «ask your county»; si no, se cocina en la commissary y la paella viaja en caliente [sobrevive '
               'con ajuste: B y E]'),
        ('', 'temporary food event permits para eventos públicos o comunitarios [sobrevive]'),
        ('BE', 'fire marshal: la estación de propano al aire libre o bajo su propio toldo de cocina, lejos de la carpa de '
               'invitados (Virginia, solo como ejemplo: cooking tents a ≥ 20 ft de otras carpas y cilindros de LP-gas '
               'fuera, 13VAC5-52-360), extintores y permiso según el fire code local; leña solo con permiso y nunca con '
               'burn ban: «check with your fire marshal» [sobrevive con ajuste: B y E]'),
        ('BE', 'comprar la van de carga usada con inspección mecánica (kilometraje, mantenimiento, carga útil); no es '
               'frigorífica: el marisco crudo va en coolers con hielo [sobrevive con ajuste: B y E]'),
        ('BE', 'título y registro de la van en el DMV a nombre del negocio + commercial auto + inland marine para '
               'paelleras, quemadores y equipo en tránsito; una cargo van no necesita CDL (solo con GVWR ≥ 26,001 lb) '
               '[sobrevive con ajuste: B y E]'),
        ('BE', 'upfit de la van: estanterías, racks verticales para los cilindros (de pie, sujetos y con ventilación), '
               'sujeciones y rotulación; comprueba que el seguro lo cubre [sobrevive con ajuste: B y E]'),
        ('E', 'general liability o BOP que NO excluya la llama abierta en eventos (pídelo por escrito); COI y additional '
              'insured para los venues [sobrevive con ajuste: E]'),
        ('E', 'liquor liability SOLO si tu personal sirve alcohol que compra el cliente (p. ej. su vino en la sangría); '
              'sin licencia no vendes alcohol [sobrevive con ajuste: E]'),
        ('', 'workers\' comp antes del primer empleado (opcional en Texas) [sobrevive]'),
        ('BE', 'residuos, aceite usado y conchas con un hauler con licencia (a menudo vía commissary); sin ceniza '
               '[sobrevive con ajuste: B y E]'),
        ('', 'control de plagas con empresa con licencia (vía commissary) [sobrevive]'),
    ]),
    ('F3 - Equipamiento', [
        ('E', 'lista de equipo propio frente a alquilado por paquete: drop-off paella, live paella party y full-service '
              'live paella [sobrevive con ajuste: E]'),
        ('BE', 'insulated food carriers para el drop-off (la paella a ≥ 135 °F o bajo time as a public health control), '
               'coolers con hielo para el marisco crudo (≤ 41 °F) y termómetros de sonda calibrados; nunca «Cambro» ni '
               '«hot box» [sobrevive con ajuste: B y E]'),
        ('BCDE', 'paelleras por tamaño (36 / 32 / 26 in con los cm entre paréntesis) y quemadores de 3 aros con patas: '
                 'prueba cada aro, el regulador y las mangueras antes del primer evento [nueva]'),
        ('', 'hotel pans, sheet pans y utensilios [sobrevive]'),
        ('BE', 'proveedor de marisco de approved source: mejillones y almejas con la etiqueta del dealer (shellstock '
               'tags, 90 días); pollo y verdura; cash-and-carry tipo Restaurant Depot; comparar mínimos y precios '
               '[sobrevive con ajuste: B y E]'),
        ('BCDE', 'kit de la estación de paella: paletas y cucharones, wind guards, mesa de trabajo, toldo de la '
                 'estación, protector de suelo, extintor a mano [nueva]'),
        ('BCDE', 'arroz bomba, azafrán (en gramos) y despensa española (smoked paprika, aceite de oliva, base de caldo) '
                 'de un importador: precio por trimestre y stock de reserva [nueva]'),
        ('', 'acuerdo con party rentals (mesas, mantelería, vajilla) [sobrevive]'),
        ('E', 'desechables para el drop-off (bandejas y tapas que aguanten el calor, platos y cubiertos de bambú o '
              'plástico); etiqueta con la hora de salida del hot holding y descarte a las 4 h, o chafing dishes (time as '
              'a public health control, 3-501.19: «ask your county»); sin butcher paper [sobrevive con ajuste: E]'),
        ('E', 'registro de temperaturas en el transporte (data logger en cada insulated carrier y en la van) [sobrevive '
              'con ajuste: E, sin «hot box»]'),
        ('', 'montar el espacio en la commissary: estanterías, etiquetado, FIFO [sobrevive]'),
        ('BE', 'prueba completa por tamaño de paellera con el equipo: arroz, caldo y propano reales, tiempos y raciones, '
               'para afinar la calculadora [sobrevive con ajuste: B y E]'),
    ]),
    ('F4 - Personal', [
        ('E', 'plan de personal por evento: ≈ 1 persona del equipo por 25 invitados (miamigrillcatering.com); un paella '
              'chef por ≈ 3 paelleras y un ayudante desde 4 paelleras u 80 invitados (Kit estimate) [sobrevive con '
              'ajuste: E]'),
        ('', 'pool de event staff en nómina W-2 (nunca 1099 ni «freelance») [sobrevive]'),
        ('', 'offer letters, I-9 y W-4; salario mínimo estatal [sobrevive]'),
        ('', 'new-hire reporting al estado [sobrevive]'),
        ('', 'proveedor de nóminas y workers\' comp en marcha [sobrevive]'),
        ('', 'food handler cards de todo el equipo [sobrevive]'),
        ('BE', 'seguridad del propano y del fuego: prueba de fugas con agua jabonosa, extintores, manta ignífuga, cierre '
               'de los cilindros y quién vigila los quemadores en el servicio [sobrevive con ajuste: B y E]'),
        ('BE', 'OSHA basics: quemaduras, calor, levantar paelleras llenas y cilindros entre dos, conducción de la van '
               '[sobrevive con ajuste: B y E]'),
        ('BE', 'guion del espectáculo (el socarrat reveal), uniforme, briefing y alérgenos: entre los 9 mayores de EE. UU. '
               'están el pescado y los crustáceos (crab, lobster, shrimp); los moluscos (mejillones, almejas) se '
               'declaran igual; huevo del alioli, trigo del pan y de la fideua, sulfitos de la gamba congelada, contacto '
               'cruzado por paletas y paelleras [sobrevive con ajuste: B y E]'),
        ('', 'política de service charge y gratuity [sobrevive]'),
    ]),
    ('F5 - Marketing', [
        ('BE', 'marca, logo, los 8 menu styles de paella (seafood, chicken & seafood, chicken & chorizo, Valencian, farm '
               'vegetable, paella negra, lobster & seafood, easy-eat peeled seafood) y fotos profesionales de la paella '
               'cocinada en vivo [sobrevive con ajuste: B y E]'),
        ('', 'web con paquetes, precios «desde» por invitado y formulario [sobrevive]'),
        ('', 'Google Business Profile y reseñas [sobrevive]'),
        ('', 'The Knot, WeddingWire y Zola [sobrevive]'),
        ('', 'ezCater + Thumbtack [sobrevive]'),
        ('', 'prospección B2B [sobrevive]'),
        ('', 'venues y wedding planners [sobrevive]'),
        ('', 'política de degustaciones [sobrevive]'),
        ('BE', 'Instagram y redes con fotos y vídeo de la paella cocinada en vivo y del socarrat (con permiso del '
               'cliente); seguimiento por texto / SMS [sobrevive con ajuste: B y E]'),
        ('E', 'plantilla de presupuesto con la calculadora del kit (paelleras por tamaño, arroz por invitado, shopping '
              'list) + CRM + software que envía la propuesta, firma y cobra el depósito [sobrevive con ajuste: E]'),
        ('', 'referidos y reseñas [sobrevive]'),
        ('E', 'tasting de lanzamiento: una paella cocinada en vivo para planners, venues y empresas + el primer bridal '
              'show local [sobrevive con ajuste: E]'),
    ]),
    ('F6 - 90 Días', [
        ('', 'llamada final 3 semanas antes: invitados, paquete, menu style, alergias, horario [sobrevive]'),
        ('BE', 'visita o llamada técnica al venue 2 semanas antes: suelo llano para los quemadores, viento y sombra, '
               'distancia a la carpa de invitados, agua para el lavamanos, acceso de la van y normas de fuego del venue '
               'por escrito [sobrevive con ajuste: B y E]'),
        ('', 'saldo antes del evento y extras en 48 h [sobrevive]'),
        ('BDE', 'pedidos: arroz y despensa con margen, marisco 1-2 días antes con sus etiquetas; sofrito, caldo y '
                'marisco limpio la víspera en la commissary, etiquetados; D = «3-5 days out, then the day before» '
                '[sobrevive con ajuste: B, D y E]'),
        ('BE', 'carga de la van con la lista (paelleras, quemadores, cilindros de pie y sujetos, coolers a ≤ 41 °F con el '
               'marisco) y registro de temperaturas al cargar y al llegar [sobrevive con ajuste: B y E]'),
        ('BE', 'llegar 2-3 h antes, montar la estación fuera de la carpa de invitados, encender, ≈ 1 h de cocción '
               '(pollo a 165 °F, marisco a 145 °F) y servir a ≥ 135 °F o bajo time as a public health control; las '
               'sobras, a la basura [sobrevive con ajuste: B y E]'),
        ('BE', 'recogida: limpiar y aceitar las paelleras, cerrar y revisar los cilindros, devolver los alquileres '
               '[sobrevive con ajuste: B y E]'),
        ('', 'pedir reseña y fotos; CRM [sobrevive]'),
        ('BE', 'revisión semanal: arroz por invitado, invitados por paellera, propano por evento, food cost y horas por '
               'evento frente a la calculadora [sobrevive con ajuste: B y E]'),
        ('', 'revisión a los 90 días: precio por invitado, guest minimums y paquetes [sobrevive]'),
    ]),
])
COLS_CAMBIAN = OrderedDict()
for _h, _ts in TAREAS_PAEL.items():
    for _k, (_cols, _t) in enumerate(_ts):
        COLS_CAMBIAN[(_h, 5 + _k)] = _cols
        for _col in 'BCDE':
            CELDA_PISTAS[('PAEC', _h, '%s%d' % (_col, 5 + _k))] = _CK + 'fase %s, tarea %d/%d: %s' % (
                _h[1], _k + 1, len(_ts), _t)

# Pistas por TEXTO propias de la paella (se suman a las de extraer_textos.PISTAS)
PISTAS_EXTRA = [
    (r'^Días fuera de rango$|^Los días van de 1 a 365', 'D119: esta validación cubre a la vez B6 (INVITADOS por evento), '
                                                         'B58/B59 (días de cobro y de pago) y los invitados de '
                                                         'Escenarios: un texto que valga para todos'),
    (r'[Cc]lientes?|[Tt]icket|[Dd]ías de apertura|al día|por día',
     'D119: motor de eventos: «events per year» (B4), «price per guest» (B5), «guests per event» (B6); nunca «customers», '
     '«per day» ni «operating days» (gate)'),
    (r'[Vv]ehícul|[Ff]ood ?[Tt]ruck|[Cc]amión|[Rr]emolque', 'D117/D120: la van de carga usada (paelleras, quemadores, '
                                                            'cilindros y coolers); nunca «truck» ni «trailer» (gate; '
                                                            '«paella food trucks» solo para el no-comprador)'),
    (r'[Vv]entanilla|[Ff]estival|[Mm]ercados|[Aa]mbulante|[Cc]alle', 'D117: paella catering en el evento del cliente; sin '
                                                                     'ventanilla, festivales, mercados ni venta '
                                                                     'ambulante (gate)'),
    (r'[Aa]parcamiento|base del vehículo|comisar', 'Glosario: «commissary kitchen & equipment storage»; nunca «support '
                                                   'kitchen»'),
    (r'[Gg]enerador|gas\b|propano', 'D121: el combustible de COCINA (propano; leña solo con permiso) es variable (fila '
                                    '15); el de la van, fijo (fila 27); el caso no tiene generador'),
    (r'[Dd]elivery|[Gg]lovo|[Uu]ber', 'D121: marketplaces de catering corporativo (p. ej. ezCater), no apps de delivery'),
    (r'[Cc]omida|[Cc]ocina|[Mm]enú|COMIDA', 'D117/D121: paella packages y add-ons; «food» y «menu» valen; nunca «chef» '
                                            'suelto (di paella chef), «plated» ni «stations» salvo «live paella station» '
                                            '(gate)'),
    (r'm²|m2\b|\bkg\b|\bkm\b|[Ll]itros?\b|\b\d+ ?L\b|\bml\b|°C|ºC', REGLA_UNIDADES),
    (r'[Ee]ventos?|[Bb]odas?', 'Glosario §9: paella catering, paella chef, live paella, backyard paella party, drop-off, '
                               'full-service, tapas hour, weddings, corporate events / holiday parties, first '
                               'communions, quinceañeras'),
]

# Glosario de research §9 (OBLIGATORIO: regla de jerga §0), entero. Se suma al de FT/CAF y al del financial-kit
GLOSARIO_PAEL = OrderedDict([
    ('empresa de paellas para eventos · show cooking', 'paella catering (nombre, H1, ficheros) · live paella · «cooked '
                                                       'live in front of your guests» · «prepared on site»; «Spanish '
                                                       'catering» como variante con tapas'),
    ('fiesta de paellas en casa', 'backyard paella party'),
    ('paellero (persona) · paellera', 'paella chef («Paella chef (required)») · paella pan («giant traditional pan»); '
                                      'el negocio: paella caterer'),
    ('paellero de gas (quemador)', 'paella burner (3-ring) with legs / stand + regulator'),
    ('socarrat · arroz · azafrán', 'socarrat («golden socarrat reveal») · bomba rice / Spanish rice · saffron (en gramos)'),
    ('sofrito · caldo · fumet', 'sofrito · stock · fish stock'),
    ('marinera · mixta · campera', 'seafood paella / paella marinera · chicken & seafood · chicken & chorizo'),
    ('valenciana · huerta · negra · bogavante', 'Valencian paella (rabbit on request) · farm vegetable · paella negra · '
                                                'lobster & seafood'),
    ('entrantes · alioli · jamón', 'tapas (patatas bravas, Spanish tortilla, cheese & cold cuts) · garlic aioli · Serrano '
                                   'ham carving station (sin tilde: «jamón» lo rechaza el detector)'),
    ('sangría · descorche', 'sangria bar (sin alcohol, o con el vino que compra el cliente) · non-alcoholic options · '
                            'corkage fee (no se modela)'),
    ('animación', 'flamenco · Spanish guitarist'),
    ('precio y mínimo', 'per person · «a minimum of 20 guests is required for on-site cooking» · overall minimum'),
    ('temporada alta', 'peak season · holiday season'),
    ('personal y formato', 'buffet attendant · serving staff · buffet · family-style (solo como formato de servicio del '
                           'operador; el gate no lo veta, pero no es un paquete del kit)'),
    ('para llevar', 'delivery orders · «pick up & delivery» · drop-off'),
    ('desplazamiento · menaje', 'travel fee («included up to 20 mile radius») · dishes & flatware (bamboo / plastic)'),
    ('botella · carpa de cocina', '20-lb propane cylinder / LP-gas container · cooking tent'),
    ('normas', 'limited food preparation (CA) · shellstock tags · time as a public health control'),
    ('cocina de apoyo', 'commissary (nunca «support kitchen»)'),
    ('isotermo', 'insulated food carriers (nunca «Cambro»: es marca)'),
    # (e) no se traducen literalmente
    ('paellero', 'paella chef (persona) o paella caterer (negocio); nunca «paellero» ni «chef» suelto'),
    ('trípode de leña', 'wood-fire setup (solo con permiso)'),
    ('ración', 'serving / per person'),
    ('show cooking', 'live paella'),
    ('fiesta popular', 'fuera del caso (temporary food establishment)'),
    ('comunión, bautizo', 'first communion, baptism, quinceañera'),
    ('finca', 'venue / backyard'),
    ('garrofó', 'lima beans'), ('ferraura', 'flat green beans'), ('bogavante', 'lobster'),
    ('fideuà', 'fideua (noodle paella), sin tilde'), ('pimentón', 'smoked paprika'),
    ('regla de los 15 kg', 'no aplica (fire code local)'), ('época de peligro', 'burn ban'),
    ('APPCC', 'HACCP-based food safety plan + TPHC SOP'), ('manipulador', 'food handler card'),
    ('anticipo', 'deposit'), ('IVA', 'sales tax'), ('escandallo', 'cost per guest / food cost'),
    ('autónomo', 'single-member LLC'), ('fijo discontinuo / freelance', 'part-time hourly W-2 staff'),
    ('medidas (John, 13-oct)', 'US customary first, metric in parentheses: lb / oz (g), °F (°C), gallons / quarts '
                               '(liters), miles, sq ft (sq m); pans in inches with cm in parentheses; saffron in grams'),
])


# ==========================================================================
# Caso de ejemplo US (D118; research §8): celdas VERDES del FT. (corto, hoja ES, celda) → (valor, rótulo ES)
# ==========================================================================
def valores_pael(M):
    v = OrderedDict()
    sup = [
        ('B4', 135, 'Clientes/día'), ('B5', 40, 'Ticket medio'), ('B6', 58, 'Días de apertura'),
        ('B7', 0.10, 'Crecimiento de volumen del año 2'), ('B8', 0.06, 'Crecimiento de volumen del año 3'),
        ('B11', 0.88, 'Ventas de COMIDA'), ('B13', 0.28, 'Coste de mercancía sobre las ventas de COMIDA'),
        ('B14', 0.35, 'Coste de mercancía sobre las ventas de BEBIDA'), ('B15', 0.035, 'Consumibles'),
        ('B16', 0.05, 'Ventas por delivery'), ('B17', 0.15, 'Comisión de la plataforma'),
        ('B18', 0.03, 'Comisión de los medios de pago'), ('B20', 0.10, 'Seguridad Social'),
        ('B21', 12, 'Número de pagas'), ('B22', 15080, 'SMI anual'), ('B24', 1100, 'Alquiler mensual'),
        ('B25', 1, 'Fianza'), ('B26', 150, 'Suministros'), ('B27', 5500, 'Seguros'), ('B28', 0.03, 'Varios'),
        ('B30', 25000, 'Recursos propios'), ('B31', M.CALIBRAR, 'Préstamo bancario'), ('B32', 0.10, 'Tipo de interés'),
        ('B33', 7, 'Plazo del préstamo'), ('B34', 0, 'Carencia'), ('B35', 3, 'Fondo de maniobra'),
        ('B37', 0.25, 'Impuesto de Sociedades, nueva'), ('B38', 0.25, 'Impuesto de Sociedades, tipo'),
        ('B39', 0.08, 'IVA repercutido de restauración'), ('B40', 0.08, 'IVA repercutido/soportado'),
        ('B41', 0, 'IVA soportado en compras'), ('B42', 0, 'Bases negativas'),
        ('B44', 7, 'Vida útil de obra'), ('B45', 5, 'Vida útil de maquinaria'), ('B48', 0, 'Subida anual'),
        ('B51', 200, 'Plazas de pie'), ('B52', 0.50, 'Actividad del mes 1'), ('B53', 8, 'Meses hasta alcanzar'),
        ('B54', 1, 'Meses de alquiler del aparcamiento'), ('B55', 0.10, 'Imprevistos sobre las partidas'),
        ('B58', 7, 'Días medios de cobro'), ('B59', 7, 'Días medios de pago'),
        ('B62', 0, 'Bebida ALCOHÓLICA'), ('B63', 0.08, 'IVA de la bebida ALCOHÓLICA'),
        ('B65', 1.15, 'DSCR mínimo'), ('B66', 1.25, 'DSCR objetivo'), ('B67', 0.15, 'Holgura mínima'),
        ('B68', None, 'Suelo salarial anual'),
    ]
    for c, val, rot in sup:
        v[('PAEP', _S, c)] = (val, rot)
    # Inversión (D120; huecos del BBQ, importes de research §8): filas 7-20 (rótulos ES del FT) = $44,700
    for k, (val, rot) in enumerate([
            (2500, 'Vehículo'), (1800, 'Adaptación'), (900, 'Equipamiento cocina'), (1500, 'Generador'),
            (18000, 'Instalación gas'), (3000, 'Depósito de agua'), (1500, 'Constitución'), (2000, 'Licencias'),
            (500, 'Proyecto técnico'), (1200, 'TPV'), (1800, 'Menaje'), (2500, 'Stock'), (4500, 'Marketing'),
            (3000, 'Toldo')]):
        v[('PAEP', _I, 'B%d' % (7 + k))] = (val, rot)
    # P&L: fijos B26-B35 (research §8: $25,100) y umbrales D122 [kit benchmark] = BBQ
    for k, (val, rot) in enumerate([
            (1200, 'Permisos'), (5000, 'Mantenimiento'), (8000, 'Marketing'), (3000, 'Gestoría'), (2400, 'Software'),
            (1800, 'Limpieza'), (600, 'Gestión de residuos'), (1000, 'Desinsectación'), (600, 'Prevención'),
            (1500, 'Derechos de autor')]):
        v[('PAEP', _P, 'B%d' % (26 + k))] = (val, rot)
    for c, val, rot in [('E51', 0.58, 'Margen bruto'), ('E53', 0.35, 'Coste de mercancía /'),
                        ('E54', 0.38, 'Coste de personal'), ('E55', 0.07, 'Aparcamiento'), ('E56', 0.05, 'Resultado neto')]:
        v[('PAEP', _P, c)] = (val, rot)
    # Staffing (D121; research §8): personas (B), FTE por persona (C), bruto mes TOTAL de la fila (D) = $8,026/mes
    for f, (b, c, d) in zip(range(5, 9), [(1, 1.0, 4507), (1, 0.4, 1387), (4, 0.10, 1248), (1, 0.3, 884)]):
        for col, val in zip('BCD', (b, c, d)):
            v[('PAEP', _R, '%s%d' % (col, f))] = (val, None)
    v.update([
        (('PAEP', _R, 'B11'), (4000, 'Coste anual')), (('PAEP', _R, 'B12'), (4000, 'Coste anual')),
        (('PAEP', _R, 'B16'), (40, 'Jornada completa')), (('PAEP', _R, 'B17'), (50, 'Semanas')),
        (('PAEP', _R, 'B18'), (9, 'Horas de servicio')), (('PAEP', _R, 'B19'), (2.5, 'Personas necesarias')),
    ])
    # Escenarios (research §8): −25 % / +25 % de eventos, −10 % / +10 % de precio e invitados
    v.update([
        (('PAEP', _ES, 'B5'), (101, 'Clientes/día')), (('PAEP', _ES, 'D5'), (169, 'Clientes/día')),
        (('PAEP', _ES, 'B6'), (36.0, 'Ticket')), (('PAEP', _ES, 'D6'), (44.0, 'Ticket')),
        (('PAEP', _ES, 'B7'), (52, 'Días')), (('PAEP', _ES, 'D7'), (64, 'Días')),
    ])
    # Estacionalidad (research §8, Kit estimate): apertura en MARZO → Month 1-12 (suma 100 %)
    for col, val in zip('BCDEFGHIJKLM', (0.07, 0.09, 0.115, 0.11, 0.08, 0.07, 0.095, 0.11, 0.075, 0.10, 0.04, 0.045)):
        v[('PAEP', _T, '%s5' % col)] = (val, 'Estacionalidad')
    return v


# Calibración D15 (SPEC D118): holgura ≥ 15 %; si no, B4 de 5 en 5 hasta 150; si la caja mínima ≤ 0 por la rampa,
# B35 3 → 4 antes de tocar el precio. Cada celda, citada en F2-NOTAS §3 (G7). Se rellena con el dry-run del paso 1
CALIBRACION_D15 = OrderedDict()


# ==========================================================================
# FORMULAS_EN: las del FT con la fila del Break-Even, las notas de las líneas de venta y las listas de la inversión
# ==========================================================================
_PE_PAEL = ('=IFERROR("With the average price per guest excl. sales tax above, you need "&TEXT(ROUNDUP(B15,0),"0")&" '
            'events a year at your average of "&TEXT(B11,"0")&" guests per event to avoid losing money (accounting '
            'break-even, depreciation included), and "&TEXT(ROUNDUP(B20,0),"0")&" for cash to hold (cash break-even: '
            'depreciation out, because it is not paid, and the year\'s loan payment in"&IF(B12=0,"; no principal is '
            'repaid this year (interest-only period or no loan)","")&"). The ""Revenue needed per year"" rows show the '
            'same figures in your currency.","")')
_C9_PAEL = ('=IFERROR("Price per guest excl. sales tax plus the weighted sales tax of your sales lines ("&TEXT('
            "SUMPRODUCT('3-Year P&L'!$E$10:$E$11,'3-Year P&L'!$G$10:$G$11)*100,\"0\")&\"%), rounded. In the US the "
            'quote adds sales tax on top, and many states tax the whole catering invoice (food, staff, rentals and the '
            'service charge); in the UK, VAT is included in the price.","")')
_F18_PAEL = ('=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$28,"0%")&" of sales: a cushion for unbudgeted event costs '
             '(extra seafood, ice, lemons, venue parking). It is a VARIABLE cost: it moves with the number of events, so '
             'it cannot sit in fixed costs (van fuel, maintenance and registration are in row 27; propane is in row '
             '15)","")')
_F13_PAEL = ('=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$13,"0%")&" of PAELLA PACKAGE sales (rice, seafood, meats, '
             'saffron, stock, salad and bread), not of total sales: add-ons have their own line","")')
_F14_PAEL = '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$14,"0%")&" of ADD-ON sales","")'


def formulas_pael():
    sys.path.insert(0, BP)
    import formulas_en as F                                                    # noqa: E402
    out = OrderedDict()
    for h, d in F._COMUNES.items():
        for c, f in d.items():
            out[('PAEP', h, c)] = f
    out[('PAEP', _S, 'C9')] = _C9_PAEL
    out[('PAEP', _P, 'F18')] = _F18_PAEL
    out[('PAEP', _P, 'F13')] = _F13_PAEL
    out[('PAEP', _P, 'F14')] = _F14_PAEL
    o11 = out[('PAEP', _T, 'O11')]
    assert 'Food and beverage purchases, consumables' in o11
    out[('PAEP', _T, 'O11')] = o11.replace('Food and beverage purchases, consumables',
                                           'Paella ingredient and add-on purchases, disposables and cooking fuel')
    out[('PAEP', _E, 'A26')] = _PE_PAEL
    for c, f in F._inversion('D21', 'D22', 'D23', 'D25', 'D26', 'D28', 'D31', 'D32', 'D33', 24, 26, 31, 32,
                             'paella burners and stands, paella pans, used cargo van, van upfit and the fire / propane '
                             'setup inspection',
                             'LLC formation and legal, first-year permits and certifications, opening inventory, '
                             'website, photos and launch, the commissary deposit, pre-opening commissary rent and the '
                             'working capital reserve').items():
        out[('PAEP', _I, c)] = (f.replace('when the lease ends', 'when the commissary agreement ends')
                                .replace(' of build-out and permits before opening', ' of test cooks, permits and '
                                         'pre-sales before opening'))
    return out


def _importes_research():
    """Importes en dólares ≥ 10,000 que cita la research de la paella (lean $12-20K, caso, BBQ $430K…): son datos de
    este producto y no se vetan aunque coincidan con un importe de otro caso EN."""
    import re as _re
    p = os.path.join(AQUI, 'F1-research-us-delta.md')
    t = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    out = {int(x.replace(',', '')) for x in _re.findall(r'\$\s?(\d{1,3}(?:,\d{3})+)', t) if int(x.replace(',', '')) >= 10000}
    out |= {int(x) * 1000 for x in _re.findall(r'\$\s?(\d{2,3})K\b', t)}
    return out


def cifras_prohibidas(valores):
    """CIFRAS_PROHIBIDAS del conjunto (D128): ES del paellero (importe y frase) + caso del BBQ + casos EN del catering, del
    bar móvil y del FT + vocabulario RX_PAEL_NO. Fuera las cifras que coinciden con un valor del propio caso."""
    propios = {int(round(x[0])) for x in valores.values() if isinstance(x[0], (int, float))}
    out = [(_num(n), 'cifra del ES del paellero (D128)', None) for n in CIFRAS_ES if n not in propios]
    propios |= _importes_research()                     # solo para las listas de los otros casos EN
    out += [(rx, motivo, None) for rx, motivo in FRASES_ES]
    b4 = CALIBRACION_D15.get(('PAEP', _S, 'B4'), (valores.get(('PAEP', _S, 'B4'), (None,))[0],))[0]
    out += [(_num(n), 'cifra del caso del BBQ EN (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(BBQ, 'cifras_caso.json'), 'bbq') if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_BBQ if not (b4 == 150 and '150' in rx)]
    out += [(_num(n), 'cifra del caso del catering EN publicado (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(CAT, 'cifras_caso.json'), 'cat') if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_CAT]
    out += [(_num(n), 'cifra del caso del mobile bar EN publicado (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(MBAR, 'cifras_caso.json'), 'mbar') if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_MBAR]
    out += [(_num(n), 'cifra del caso FT EN publicado (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(BP, 'cifras_caso.json'), 'ft') if n not in propios]
    out += RX_PAEL_NO
    return out


def completar(M):
    fijos = OrderedDict((k, v) for k, v in M.FIJOS.items() if k not in FIJOS_FUERA)
    fijos.update(FIJOS_NUEVOS)
    M.FIJOS = fijos
    M.POR_CELDA = POR_CELDA
    M.TOKENS_DOCX = tokens_pael(M.TOKENS_DOCX)
    M.PRODUCTOS_CIERRE = PRODUCTOS_CIERRE_PAEL
    M.DOCX_FIJOS = docx_fijos(M)
    M.DOCX_NOTAS = DOCX_NOTAS
    M.DOCX_NOTAS_PLAN = DOCX_NOTAS_PLAN
    M.FORMULAS_EN = formulas_pael()
    M.VALORES_EN = valores_pael(M)
    M.CALIBRACION_D15 = CALIBRACION_D15
    M.CELDA_PISTAS = CELDA_PISTAS
    M.PISTAS_EXTRA = PISTAS_EXTRA
    M.PISTA_D19 = PISTA_D19_GENERICA          # la pista D19 de verdad va por celda (filas 55-68); las tareas, también
    M.CIFRAS_PROHIBIDAS = cifras_prohibidas(M.VALORES_EN)
    M.RX_PAEL_NO = RX_PAEL_NO
    M.REGLA_UNIDADES = REGLA_UNIDADES
    glo = OrderedDict(M.GLOSARIO)
    for k in ('cliente/día', 'ticket medio sin IVA', 'PVP con IVA', 'aparcamiento y base del vehículo', 'venta ambulante'):
        glo.pop(k, None)                      # glosario del food truck que no vale aquí
    glo.update([('cliente/día → (motor)', 'events per year'), ('ticket medio sin IVA → (motor)',
                                                               'average price per guest (excl. sales tax, service '
                                                               'included)'),
                ('días de apertura → (motor)', 'average guests per event'),
                ('aparcamiento y base del vehículo', 'commissary kitchen & equipment storage')])
    for k, val in GLOSARIO_PAEL.items():
        glo[k] = val                          # research §9 manda (regla de jerga §0)
    M.GLOSARIO = glo
