#!/usr/bin/env python3
"""
datos_cof.py — Coffee Cart Business Plan Kit (EN) · los datos ES→EN que dependen del contenido: rótulos fijados
(D222-D224), POR_CELDA, pistas (D18/D19, notas del caso, las 68 tareas del checklist D228 con las columnas que cambian),
tokens del docx (D229), fijos y notas del docx (con la PROPUESTA EN DE LA PAELLA de cada ranura y el ES 1.0 de la cafetería
móvil cuando exista), caso US (D220; research §8), FORMULAS_EN, cifras prohibidas y vocabulario vetado RX_COF_NO (D231) y
glosario de research §9 (regla de jerga §0). Lo llama `mapas_cof.instalar()` con el módulo `mapas` YA cargado con los datos
de FT/CAF (motor 2.2), de los que parte. La fuente ES del circuito es el FOOD TRUCK ES: los rótulos ES de abajo son los del
FT; el EN de partida de cada celda es el de la Paella cerrada (y, si no hay, el del Catering publicado):
mapas_cof.propuesta_de. Estructura de `../business-plans-en-7/datos_pael.py` (D221). Sesión Claude Code, 28-oct-2026
(F1 + paso 1a).
"""
import json
import math
import os
import re
import sys
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
BP = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
CAT = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')
MBAR = os.path.join(os.path.dirname(AQUI), 'business-plans-en-5')
BBQ = os.path.join(os.path.dirname(AQUI), 'business-plans-en-6')
PAEL = os.path.join(os.path.dirname(AQUI), 'business-plans-en-7')
# ES gemelo (cafetería móvil para eventos 1.0, en F2 el 28-oct): por defecto la carpeta del repo; COF_FUENTE_ES apunta a
# otra (p. ej. el worktree del implementador ES en el VPS, SOLO LECTURA) para el paso 1c
CAF = os.environ.get('COF_FUENTE_ES') or os.path.join(os.path.dirname(AQUI), 'plan-cafeteria-movil')

URL_COF = 'aichef.pro/en/digital-products/coffee-cart-business-plan'
_I, _S, _P, _R, _N, _E, _ES, _T = ('Inversión Inicial', '0. Supuestos', 'PyG 3 Años', 'Personal', 'Instrucciones',
                                   'Punto Equilibrio', 'Escenarios', 'Tesorería 12 meses')
# Medidas (John, 13-oct; SPEC §0): sistema US como principal y la métrica entre paréntesis
REGLA_UNIDADES = ('MEDIDAS US (John, 13-oct; SPEC §0): principales lb y oz, °F, gallons / quarts, miles y sq ft; la '
                  'métrica entre paréntesis para UK y Australia: «8 oz (240 ml)», «41 °F (5 °C)», «5 gallons (19 '
                  'liters)», «12 ft (3.7 m)»; el café se compra por lb; la DOSIS de espresso en gramos con su oz «18 g '
                  '(0.63 oz)» (así trabaja el barista; el gate no veta «g»); la leche en oz por bebida y en gallons por '
                  'evento; la electricidad en V, A y W («110V / 220V», «NEMA 6-20», «5,500 W»); nada de kg, km, litros ni '
                  '°C como unidad principal (gate). La leche es TCS: «cold holding at 41 °F (5 °C) or below (FDA Food '
                  'Code)», nombrado SIEMPRE como mínimo del Food Code')

# ==========================================================================
# FIJOS (por TEXTO ES del FT: valen en cualquier celda de los 2 libros) y POR_CELDA (solo esa celda)
# ==========================================================================
FIJOS_FUERA = ('Este fichero forma parte del producto «plan-negocio-cafeteria» de AI Chef Pro.',)
_TITULO_CHECK = 'COFFEE CART STARTUP CHECKLIST — MOBILE ESPRESSO BAR & COFFEE CATERING'
FIJOS_NUEVOS = OrderedDict([
    ('Este fichero forma parte del producto «plan-negocio-food-truck» de AI Chef Pro.',
     'This file is part of the Coffee Cart Business Plan Kit by AI Chef Pro.'),
    # D228: título del checklist y de la fase 2 (el título de hoja no tiene el límite de 31 de la pestaña)
    ('CHECKLIST APERTURA — FOOD TRUCK', _TITULO_CHECK),
    ('FASE 2: VEHÍCULO Y PERMISOS', 'PHASE 2: COMMISSARY, CART & TRAILER, HEALTH PERMIT & INSURANCE'),
    ('INSTRUCCIONES DE USO — Plan financiero Food Truck',
     'HOW TO USE THIS WORKBOOK — Coffee Cart Financial Projections'),
    ('PLAN DE NEGOCIO: FOOD TRUCK', 'BUSINESS PLAN: COFFEE CART & COFFEE CATERING COMPANY'),
    ('Ajusta las cifras a tu proyecto.', 'US kit example (2026) — replace with your own quotes.'),
    ('Escenario realista — Food Truck urbano', 'Base case — coffee catering company with two espresso stations'),
    ('Break-even — Food Truck', 'Break-even — Coffee Cart'),
    # D225: cabecera de la tabla D19
    ('DATOS DE REFERENCIA DEL SECTOR', 'US COFFEE CART & COFFEE CATERING BENCHMARKS (sourced) AND KIT ESTIMATES'),
    # motor de eventos (B4 = eventos/año, B5 = precio por invitado, B6 = invitados por evento) en todas las hojas
    ('Ticket medio SIN IVA (€)', 'Average price per guest (excl. sales tax, baristas included)'),
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
    # D224 (decisión SPEC, = ES D5): el canal de «delivery» del FT son los FESTIVALES Y MERCADOS guest-pay (B16/B17)
    ('Comisiones de delivery', 'Festival & market organizer fees'),
    # alcohol solo si algún día vendes con licencia (0 % en el caso)
    ('IVA repercutido/soportado general', 'Sales tax rate on alcohol (not used: no alcohol in this plan)'),
    # D223: las dos líneas de venta y su coste (los mismos textos ES salen en el P&L y en Escenarios)
    ('Coste de mercancía — comida', 'Cost of goods — coffee bar packages (beans, milks, syrups, cold brew)'),
    ('Coste de mercancía — bebida', 'Cost of goods — add-ons'),
    ('Consumibles y envases', 'Compostable cups, lids, sleeves & napkins'),
])

POR_CELDA = OrderedDict([
    # 0. Supuestos (D220, D223, D224): mezcla de ventas, canal de festivales, commissary
    (('COFP', _S, 'A11'), 'COFFEE BAR PACKAGES share of sales (baristas, espresso drinks, batch & cold brew, milks, syrups, '
                          'cups)'),
    (('COFP', _S, 'A12'), 'ADD-ONS share of sales (extra hours, branded cups & latte printing, pastries from a licensed '
                          'bakery, travel fees)'),
    (('COFP', _S, 'A13'), 'Cost of goods on COFFEE BAR PACKAGE sales (beans, milks incl. oat milk, syrups, cold brew)'),
    (('COFP', _S, 'A14'), 'Cost of goods on ADD-ON sales (pastries, branded cups, printing)'),
    (('COFP', _S, 'A15'), 'Compostable cups, lids, sleeves & napkins as % of sales'),
    (('COFP', _S, 'A16'), 'FESTIVALS & FARMERS MARKETS share of sales (guest-pay pop-ups)'),
    (('COFP', _S, 'A17'), 'Organizer / vendor fee on those sales (booth fees converted to %)'),
    (('COFP', _S, 'A23'), 'COMMISSARY, CART STORAGE AND FIXED COSTS'),
    (('COFP', _S, 'A24'), 'Commissary, cart storage & trailer parking, per month'),
    (('COFP', _S, 'A25'), 'Commissary deposit (months)'),
    (('COFP', _S, 'A26'), 'Monthly utilities (generator fuel, water and ice not covered by the commissary)'),
    (('COFP', _S, 'A44'), 'Useful life of the espresso cart, portable bar, trailer and fit-outs (years)'),
    (('COFP', _S, 'A45'), 'Useful life of the espresso machines, grinders, brewing gear, POS and generator (years)'),
    (('COFP', _S, 'A51'), 'Max events a year your stations and baristas can handle'),
    (('COFP', _S, 'A54'), 'Months of commissary rent BEFORE opening'),
    (('COFP', _S, 'A55'), 'Contingency on the cart, portable bar, trailer, wrap and plan review lines (%)'),
    (('COFP', _S, 'A62'), 'ALCOHOL as a share of add-on sales (0%: no liquor license; espresso martinis go to a licensed '
                          'mobile bar)'),
    # Startup Costs filas 7-23 y base de amortización (D222: las bases de las fórmulas mandan; solo se mueven filas)
    (('COFP', _I, 'A7'), 'Espresso cart (NSF, hand sink, fresh & gray water tanks, pump & filtration, undercounter fridge)'),
    (('COFP', _I, 'A8'), 'Portable espresso bar for the second station (with undercounter fridge)'),
    (('COFP', _I, 'A9'), 'Espresso machines: 2-group volumetric (220V) + compact 2-group'),
    (('COFP', _I, 'A10'), 'Espresso grinders ×4 (house + decaf at each station)'),
    (('COFP', _I, 'A11'), 'Enclosed cargo trailer (6×12 ft, ramp door)'),
    (('COFP', _I, 'A12'), 'Trailer wrap, hitch, tie-downs & cart loading ramps'),
    (('COFP', _I, 'A13'), 'LLC formation, contracts and legal'),
    (('COFP', _I, 'A14'), 'First-year permits and certifications (health permit, food handler cards, CFPM, fire / '
                          'generator)'),
    (('COFP', _I, 'A15'), 'Mobile food unit plan review & cart inspection'),
    (('COFP', _I, 'A16'), 'POS, card readers & booking software'),
    (('COFP', _I, 'A17'), 'Batch brewer, airpots, cold brew system, smallwares & commissary storage racks'),
    (('COFP', _I, 'A18'), 'Opening inventory (beans, milks, syrups, compostable cups)'),
    (('COFP', _I, 'A19'), 'Website, photos, tastings & launch (corporate open house, bridal show)'),
    (('COFP', _I, 'A20'), 'Power: inverter generator (5,500 W), cords & power distribution'),
    (('COFP', _I, 'A21'), 'Commissary deposit'),
    (('COFP', _I, 'A22'), 'Commissary rent before opening'),
    (('COFP', _I, 'A23'), 'Cart, bar, trailer and plan review contingency'),
    (('COFP', _I, 'A31'), 'Espresso cart, portable bar, trailer, wrap and plan review (depreciated over the cart life)'),
    # 3-Year P&L (D223; fijos B26-B35 = $21,000)
    (('COFP', _P, 'A10'), 'Coffee bar package sales (baristas, espresso drinks, batch & cold brew, milks, syrups, cups)'),
    (('COFP', _P, 'A11'), 'Add-on sales (extra hours, branded cups & latte printing, pastries, travel fees)'),
    (('COFP', _P, 'A22'), 'Commissary, cart storage & trailer parking'),
    (('COFP', _P, 'A24'), 'Utilities (generator fuel, water and ice not covered by the commissary)'),
    (('COFP', _P, 'A25'), 'Insurance (general liability, commercial auto with the trailer, workers\' comp, equipment)'),
    (('COFP', _P, 'A26'), 'Annual permits and licenses (health permit renewal, temporary event and fire / generator '
                          'permits)'),
    (('COFP', _P, 'A27'), 'Tow vehicle & trailer fuel, maintenance and registration'),
    (('COFP', _P, 'A30'), 'Software (quotes / booking / CRM, POS, e-signature, website)'),
    (('COFP', _P, 'A31'), 'Linens, signage, aprons and smallwares replacement'),
    (('COFP', _P, 'A32'), 'Phone, internet & card-reader data plans'),
    (('COFP', _P, 'A33'), 'Espresso machine service, water filters & grinder burrs'),
    (('COFP', _P, 'A34'), 'Food safety & barista training (CFPM, food handler cards)'),
    (('COFP', _P, 'A35'), 'Tastings for prospects (corporate open house, couples)'),
    (('COFP', _P, 'A52'), 'Cost of goods sold (coffee bar packages + add-ons)'),
    (('COFP', _P, 'A55'), 'Commissary & cart storage / Sales'),
    (('COFP', _N, 'A20'), 'Commissary & cart storage / Sales'),
    # Staffing (D223): 4 puestos W-2, cobertura por evento, nota W-2 / bebidas por hora
    (('COFP', _R, 'A5'), 'Owner / Lead Barista & Sales'),
    (('COFP', _R, 'A6'), 'Lead barista (part-time W-2)'),
    (('COFP', _R, 'A7'), 'Event baristas (hourly W-2)'),
    (('COFP', _R, 'A8'), 'On-call barista / driver (hourly W-2, peak months)'),
    (('COFP', _R, 'A15'), 'COVERAGE OF EVENT HOURS'),
    (('COFP', _R, 'A18'), 'Hours per person per event (loading at the commissary, travel, setup, service, breakdown, '
                          'cleaning)'),
    (('COFP', _R, 'A19'), 'Baristas per event (average)'),
    (('COFP', _R, 'A20'), 'Event hours to cover per year'),
    (('COFP', _R, 'A24'), 'Columns D-G are TOTALS for the row. Event baristas are hourly W-2 employees with payroll taxes '
                          'and workers\' comp: paying them as 1099 contractors is a misclassification risk (FLSA; '
                          'California AB5). One barista serves about 50-65 drinks an hour.'),
    # 12-Month Cash Flow (D226): Month 1 = marzo; el retainer no se modela; trimestres del PLAN (deuda O20 de la pizza)
    (('COFP', _T, 'O5'), 'Share of the year\'s events per month (100% in total). Month 1 = opening month (March in the '
                         'example); July is the slowest month for coffee carts. The retainer is not modeled: it improves '
                         'real cash.'),
    (('COFP', _T, 'O20'), 'Cash only leaves when the quarter\'s result is positive. Months without a settlement are left '
                          'blank, not zero. The cell turns RED when the payment takes more cash than is left that month. '
                          'The model settles in the month after each plan quarter (Months 4, 7 and 10: June, September '
                          'and December with Month 1 in March; the fourth quarter is remitted in Month 13): if your state '
                          'requires monthly filing, expect smaller payments every month instead'),
    (('COFP', _T, 'A34'), 'The fourth plan quarter\'s sales tax is settled in Month 13 (March of the following year with '
                          'Month 1 in March), so it does not appear in this table. The model pays year-1 income tax in '
                          'year 2 (a simplification: estimated tax payments are usually quarterly). The loan payment is '
                          'spread in twelve equal parts following the ANNUAL schedule in the Financing tab, and payroll in '
                          'twelve monthly installments (plus extra pay periods in their month, only if pay periods > 12).'),
    # notas del motor (= Paella, con la corrección de la holgura heredada)
    (('COFP', _S, 'C20'), 'FICA (Social Security 6.2% + Medicare 1.45%) + federal and state unemployment taxes (FUTA / '
                          'SUTA). Workers\' comp is in the insurance line. The example uses a lean 10% with no benefits; '
                          'ask your payroll provider for your rate.'),
    (('COFP', _S, 'A2'), 'Change the GREEN cells: the rest of the workbook recalculates on its own. Expense items are typed '
                         'on their own tab (also in green) and are not repeated here. Amounts are in US dollars (or your own '
                         'currency).'),
    (('COFP', _S, 'C39'), 'Example rate: state + local sales tax combined, applied to the whole invoice (coffee service, '
                          'baristas and add-ons, and in some states the travel fee). Hosted events are usually taxed as catering; at festivals and '
                          'markets you collect it drink by drink and may need a permit where you sell. Rates and rules vary '
                          'widely by state and city: look up yours. UK: 20% VAT applies to catering for events and '
                          'functions (VAT Notice 709/1).'),
    (('COFP', _S, 'C67'), 'Minimum cushion of the plan above break-even (plan ÷ break-even − 1). The drop you can absorb is '
                          '1 − break-even ÷ plan: a 15% cushion lets events fall by about 13% before costs stop being covered'),
    (('COFP', _E, 'E24'), 'How far the plan sits above the cash break-even (plan ÷ break-even − 1); the drop you can absorb '
                          'is 1 − break-even ÷ plan. The required minimum is set in the "0. Assumptions" tab'),
])

# ==========================================================================
# Cifras prohibidas (D231): ES de la cafetería móvil (provisionales hasta su cifras_caso_es.json: paso 1c), caso de la
# Paella, casos EN ajenos (BBQ, catering, mobile bar, FT) y el vocabulario vetado RX_COF_NO (con su lista blanca).
# Formato: (regex, motivo, excepción sobre el texto entero)
# ==========================================================================
def _num(n):
    """190000 → patrón que casa 190,000 · 190.000 · 190 000 · 190000 (y nada pegado a más dígitos)."""
    s = str(n)
    cab, cola = s[:-3], s[-3:]
    return r'(?<![\d.,])' + cab + r'[.,   ]?' + cola + r'(?![\d])'


def _cifras_es_caf():
    """Importes ≥ 10.000 del caso ES de la cafetería móvil: los de `../plan-cafeteria-movil/cifras_caso_es.json` cuando
    exista (paso 1c); mientras, los de su SPEC 1.0 antes de calibrar (D5, D8, D9: 107.055 € de ventas, 42.000 € de
    inversión, ≈ 41.000 € de préstamo; 25.000 € de propios queda fuera: choca con importes US plausibles)."""
    p = os.environ.get('COF_CIFRAS_ES') or os.path.join(CAF, 'cifras_caso_es.json')     # en el VPS, durante la F2 ES:
    out = {107055, 42000, 41000}                                                        # /root/tmp-caf-f2/cifras_caso_es.json
    if os.path.exists(p):                     # formato de los ES 2.2 / 1.0: {fuente, tokens: {T: '12.345 €'}, valores}
        d = json.load(open(p, encoding='utf-8'))
        tok, val = d.get('tokens', {}), d.get('valores', {})
        for t, v in val.items():
            if isinstance(v, (int, float)) and abs(v) >= 10000 and '€' in str(tok.get(t, '')):
                out.add(int(round(abs(v))))
    return tuple(sorted(out))


CIFRAS_ES = _cifras_es_caf()
FRASES_ES = [
    (r'(?i)€|\bEUR\b', 'moneda ES'),
    (r'(?i)\b130 events\b', 'caso ES (130 eventos/año)'),
    (r'(?i)\b135 guests\b', 'caso ES (135 invitados por evento)'),
    (r'(?i)\b6[.,][12]0\s?(?:€|EUR)|(?:€|EUR)\s?6[.,][12]0\b|\$6\.[12]0\b', 'precio ES (6,10-6,20 €/invitado)'),
    (r'(?i)\b83 (?:tasks|steps|milestones)\b|\b8[0-9] tasks\b', 'recuento del checklist ES (~80 tareas; el EN tiene 68)'),
    (r'(?i)\bferia\b|\bfiestas? populares?\b|\bcontrato menor\b', 'ES (feria / fiestas populares / contrato menor)'),
    (r'\bv1\.[01]\b|\b[Vv]ersion 1\.[01]\b', 'versión del ES (1.0): la familia EN va en 2.2'),
]
_FIRMA = r'John Guerrero'
RX_COF_NO = [
    # heredado del FT (D72), con los matices del café
    (r'(?i)\bper day\b', 'vocabulario FT («per day»)', None),
    (r'(?i)\boperating days?\b', 'vocabulario FT («operating days»)', None),
    (r'(?i)(?<!corporate )\bcustomers\b', 'vocabulario FT («customers» → clients / hosts / guests)',
     r'^Synthetic paragraph \d+ of the \w+ plan for the assembly test'),
    (r'(?i)(?<!coffee )(?<!food )(?<!pickup )\btrucks?\b(?! Business Plan Kit)',
     'vocabulario FT («truck»: solo «coffee truck» como FORMATO, «food truck» y el nombre del kit)', None),
    (r'(?i)(?<!service )\bwindows?\b', 'vocabulario FT («window»: solo «service window»)', None),
    # del catering EN y de la paella (las propuestas)
    (r'(?i)\bplated\b|\bfamily-style\b|\bchef-attended\b', 'catering genérico («plated / family-style / chef-attended»)',
     None),
    (r'(?i)\b(?:themed|action|food|carving) stations?\b', 'catering genérico («themed / action / food stations»)', None),
    (r'(?i)(?<!AI )\b(?:executive |sous |paella )?chefs?\b', 'catering / paella («chef»: aquí, barista o lead barista)',
     _FIRMA),
    (r'(?i)\btaco bars?\b|\bpasta\b|\b(?:12|twelve) (?:world )?cuisines\b|\bbuffets?\b|\bchafing\b',
     'catering genérico (taco bar / pasta / cuisines / buffet / chafing)', None),
    (r'(?i)\brefrigerated (?:cargo )?vans?\b|\bcargo vans?\b|\bvan upfit\b', 'catering / paella («van»: el caso lleva un '
                                                                             'remolque cerrado y el vehículo del dueño)',
     None),
    (r'(?i)\bpaellas?\b|\bsocarrat\b|\bsofrito\b|\bsaffron\b|\bbomba\b|\bshellstock\b|\bsangria\b|\btapas\b|'
     r'\bpaella pans?\b|\b3-ring burners?\b|\bpropane cylinders?\b|\bwind guards?\b|\bTPHC\b',
     'paella (vocabulario de la propuesta)', None),
    (r'(?i)\bseafood\b|\bshellfish\b|\bmussels?\b|\bclams?\b|\blobster\b|\bchorizo\b|\baioli\b|\bfideua\b',
     'paella (ingredientes)', None),
    (r'(?i)\bezCater\b', 'catering corporativo («ezCater»: el café usa GigSalad, Thumbtack, The Bash y Zola)', None),
    # del bar móvil
    (r'(?i)(?<!espresso )\bcocktails?\b(?! hour)', 'bar móvil («cocktails»; solo «cocktail hour» y «espresso martini»)',
     None),
    (r'(?i)\bbartend(?:er|ers|ing)\b|\bbarbacks?\b|\bdry hire\b|\bmixers?\b|\bcash bars?\b|\bspecialty bars?\b',
     'bar móvil (bartender / barback / dry hire / mixers / cash bar)', None),
    (r'(?i)\bmobile bars?\b(?! Business Plan Kit)', 'bar móvil («mobile bar»: solo «licensed mobile bar» y el nombre del '
                                                    'kit)', r'(?i)licensed mobile bar'),
    # del BBQ
    (r'(?i)\bsmok(?:e|ed|er|ers|ing|y)\b|\bpitmasters?\b|\bpits?\b|\bbrisket\b|\bpulled pork\b|\bribs\b|\blive[- ]fire\b|'
     r'\bcarv(?:e|ed|ing|er|ers)\b|\bBBQ\b|\bbarbecue\b|\bgrill(?:s|ed|ing)?\b|\brubs?\b|\bwhole hogs?\b|\bmeats?\b',
     'BBQ (vocabulario)', None),
    # del ES de la cafetería móvil (falsos amigos y trámites)
    (r'(?i)\bcafeterias?\b', 'falso amigo («cafetería» ≠ cafeteria: di coffee cart / mobile espresso bar)', None),
    (r'(?i)\bmobile caf[eé]\b', 'calco («mobile café»: di coffee cart / mobile espresso bar)', None),
    (r'\bEspaña\b|\bSpain\b|\bSpanish\b', 'ES (España / Spain / Spanish)', None),
    (r'\bIVA\b', 'ES («IVA»)', None),
    (r'\bVAT\b', 'ES («VAT» fuera de la nota UK)', r'\bUK\b|United Kingdom|HMRC'),
    (r'(?i)\baut[oó]nomo\b|\bfijos? discontinuos?\b|\bETT\b|\bconvenio\b|\bSMI\b', 'trámite ES (autónomo / fijo '
                                                                                   'discontinuo / convenio / SMI)', None),
    (r'\bSL\b|\bIAE\b|\bAESAN\b|\bAPPCC\b|\bCCAA\b|\bRGSEAA\b|\bFACe\b|Veri\*?factu|\bITV\b|\bRGV\b',
     'trámite / norma ES', None),
    (r'\bRD \d|Reglamento \(CE\)|Real Decreto|\bLey \d', 'norma ES (RD / Reglamento / Ley)', None),
    (r'(?i)\bPiaggio\b|\bApe 50\b|\bfurgoneta\b|\bboller[ií]a\b|\bcomida testigo\b|\bBizum\b|'
     r'Bodas\.net|Zankyou', 'ES de la cafetería móvil (Piaggio / furgoneta / bollería / Bizum…; «cortado» vale: carta US)',
     None),
    (r'(?i)\bfree-?lance', 'jerga (§0): «freelance» → W-2 event barista', None),
    # regla de jerga §0 (research §9)
    (r'(?i)\brecipe costing\b|\bescandallo\b', 'jerga (§9 #17): «cost per drink» (nunca «recipe costing» ni '
                                               '«escandallo»)', None),
    (r'(?i)\bsupport kitchen\b', 'jerga (§0): «support kitchen» → commissary', None),
    (r'\bCambros?\b', 'jerga (§0): «Cambro» es marca → insulated carriers / airpots', None),
    (r'\bD\s?[-–+]\s?\d{1,2}\b', 'calco ES «D-21 / D-14 / D-1» → «3 weeks out / 2 weeks out / day before»', None),
    (r'(?i)\bgrowing demand\b|\bdemand is (?:growing|rising)\b|\brising demand\b',
     'research §0: la demanda es estacional (pico en enero), no creciente', None),
    # unidades (REGLA_UNIDADES): kg, km, litros, °C y m² solo entre paréntesis
    (r'(?i)\d\s?(?:kg|km|°C|liters?|litres?|ml)\b(?![^()]*\))', 'unidades: métrica solo entre paréntesis '
                                                                '(REGLA_UNIDADES)', None),
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
# BBQ: «128 events» NO se veta aquí (es el escenario pesimista del café: 170 × 0.75)
FRASES_BBQ = [(r'(?i)\b150 events\b', 'caso del BBQ EN («150 events»)'),
              (r'(?i)\$38(?:\.00)? (?:per|a) guest\b|\$38\.00\b', 'caso del BBQ EN («$38 per guest»)'),
              (r'(?i)\b220 events\b', 'caso del BBQ EN («220 events»)'),
              (r'\$2,850\b', 'caso del BBQ EN ($2,850 por evento)')]
FRASES_PAEL = [(r'(?i)\b135 events\b', 'caso de la Paella EN («135 events»)'),
               (r'(?i)\$40(?:\.00)? (?:per|a) guest\b', 'caso de la Paella EN («$40 per guest»)'),
               (r'(?i)\b58 guests\b', 'caso de la Paella EN («58 guests»)'),
               (r'(?i)\b116 events\b', 'equilibrio de la Paella EN («116 events»)'),
               (r'\$2,320\b', 'caso de la Paella EN ($2,320 por evento)')]


# ==========================================================================
# Tokens del docx (D229): los del motor con descripciones de café + alias legibles + partidas propias. Cada token apunta
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
    ('consumibles_pct', 'compostable cups, lids, sleeves & napkins, % of sales'),
    ('tarjeta_pct', 'card processing fees, % of sales (hosts pay retainers and balances by card; festival sales by card)'),
    ('alquiler_mes', 'commissary, cart storage & trailer parking, per month'),
    ('suministros_mes', 'utilities per month (generator fuel, water and ice not covered by the commissary)'),
    ('seguros_anual', 'insurance per year (general liability, commercial auto with the trailer, workers\' comp, equipment)'),
    ('vida_obra', 'useful life of the espresso cart, portable bar, trailer and fit-outs, years'),
    ('vida_equipo', 'useful life of the espresso machines, grinders, brewing gear, POS and generator, years'),
    ('ocupacion_anual', 'commissary, cart storage & trailer parking per year'),
    ('ocupacion_pct', 'commissary, cart storage & trailer parking, % of sales'),
    ('cogs_pct', 'cost of goods (coffee bar packages + add-ons), % of sales'),
    ('equilibrio_clientes_dia', 'break-even EVENTS per year, accounting (alias: usa {{equilibrio_eventos}})'),
    ('equilibrio_caja_clientes_dia', 'cash break-even EVENTS per year (alias: usa {{equilibrio_caja_eventos}})'),
    ('pesimista_clientes', 'pessimistic scenario: events per year (alias: usa {{pesimista_eventos}})'),
    ('optimista_clientes', 'optimistic scenario: events per year (alias: usa {{optimista_eventos}})'),
    ('pesimista_ticket', 'pessimistic scenario: price per guest (alias: usa {{pesimista_precio}})'),
    ('optimista_ticket', 'optimistic scenario: price per guest (alias: usa {{optimista_precio}})'),
    ('pesimista_dias', 'pessimistic scenario: guests per event (alias: usa {{pesimista_invitados}})'),
    ('optimista_dias', 'optimistic scenario: guests per event (alias: usa {{optimista_invitados}})'),
    ('inv_permisos', 'first-year permits and certifications (health permit, food handler cards, CFPM, fire / generator)'),
    ('inv_lanzamiento', 'website, photos, tastings & launch (corporate open house, bridal show)'),
    ('inv_stock', 'opening inventory (beans, milks, syrups, compostable cups)'),
    ('horas_semana', 'full-time hours per week'),
])
# fuera: ventas ÷ «días» no significa nada; las filas 7-20 del FT son aquí otras partidas (alias propios abajo)
_FUERA = ('ventas_dia', 'inv_vehiculo', 'inv_adaptacion', 'inv_equipo_cocina', 'inv_generador', 'food_cost_comida',
          'food_cost_bebida')
TOKENS_PROPIOS = OrderedDict([
    # alias legibles del motor (las mismas celdas que los tokens heredados)
    ('eventos_a1', ('int', ('fila', _S, 'Clientes/día (media del año 1)', 'B'), 'events per year, year 1')),
    # M3 de la paella: redondeo al entero más cercano, como el libro (187.0 → 187); el «int» común trunca
    ('eventos_a2', ('int', ('deriv', lambda c: math.floor(c['clientes_a2'] + 0.5)), 'events per year, year 2 (rounded)')),
    ('eventos_a3', ('int', ('deriv', lambda c: math.floor(c['clientes_a3'] + 0.5)), 'events per year, year 3 (rounded)')),
    ('precio_invitado', ('usd2', ('fila', _S, 'Ticket medio SIN IVA (€)', 'B'),
                         'average price per guest of the event mix, excl. sales tax, baristas and travel included')),
    ('precio_invitado_con_tax', ('usd2', ('fila', _S, 'PVP equivalente con IVA (calculado)', 'B'),
                                 'average price per guest incl. sales tax')),
    ('invitados_evento', ('int', ('fila', _S, 'Días de apertura al año', 'B'), 'average guests per event')),
    ('capacidad_eventos', ('int', ('fila', _S, {'cof': 'Plazas de pie y mesas altas junto al vehículo'}, 'B'),
                           'max events a year the two stations and the baristas can handle (information only)')),
    ('cuota_paquetes_pct', ('pct0', ('fila', _S, 'Ventas de COMIDA sobre el total', 'B'),
                            'coffee bar packages, % of sales (the rest are add-ons)')),
    ('coste_paquetes_pct', ('pct0', ('fila', _S, 'Coste de mercancía sobre las ventas de COMIDA', 'B'),
                            'cost of goods on coffee bar package sales (beans, milks, syrups, cold brew)')),
    ('coste_extras_pct', ('pct0', ('fila', _S, 'Coste de mercancía sobre las ventas de BEBIDA', 'B'),
                          'cost of goods on add-on sales')),
    ('festivales_pct', ('pct0', ('fila', _S, 'Ventas por delivery sobre el total', 'B'),
                        'share of sales from festivals & farmers markets (guest-pay pop-ups)')),
    ('festivales_comision', ('pct0', ('fila', _S, 'Comisión de la plataforma de delivery', 'B'),
                             'organizer / vendor fee on festival & market sales')),
    ('cobro_dias', ('int', ('fila', _S, 'Días medios de cobro', 'B'), 'average days to collect from clients')),
    ('pago_dias', ('int', ('fila', _S, 'Días medios de pago a proveedor', 'B'), 'average days to pay suppliers')),
    ('horas_evento', ('dec1', ('fila', _R, 'Horas de servicio al día que hay que cubrir', 'B'),
                      'hours per person per event (loading, travel, setup, service, breakdown, cleaning)')),
    ('personas_evento', ('dec1', ('fila', _R, 'Personas necesarias a la vez en cada franja', 'B'),
                         'baristas per event (average)')),
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
    # partidas de la inversión del coffee caterer (D222: filas 7-20; rótulos ES del FT)
    ('inv_carro', ('usd', ('fila', _I, {'cof': 'Vehículo food truck (nuevo o segunda mano)'}, 'B'),
                   'espresso cart (NSF, hand sink, fresh & gray water tanks, pump & filtration, undercounter fridge)')),
    ('inv_barra', ('usd', ('fila', _I, {'cof': 'Adaptación y rotulación vehículo'}, 'B'),
                   'portable espresso bar for the second station (with undercounter fridge)')),
    ('inv_espresso', ('usd', ('fila', _I, {'cof': 'Equipamiento cocina móvil'}, 'B'),
                      'espresso machines: 2-group volumetric (220V) + compact 2-group')),
    ('inv_molinos', ('usd', ('fila', _I, {'cof': 'Generador eléctrico o conexión'}, 'B'),
                     'espresso grinders ×4 (house + decaf at each station)')),
    ('inv_remolque', ('usd', ('fila', _I, {'cof': 'Instalación gas (si aplica)'}, 'B'), 'enclosed cargo trailer (6×12 ft)')),
    ('inv_remolque_wrap', ('usd', ('fila', _I, {'cof': 'Depósito de agua + aguas residuales'}, 'B'),
                           'trailer wrap, hitch, tie-downs & cart loading ramps')),
    ('inv_llc', ('usd', ('fila', _I, {'cof': 'Constitución SL + notaría + registro'}, 'B'),
                 'LLC formation, contracts and legal')),
    ('inv_plan_review', ('usd', ('fila', _I, {'cof': 'Proyecto técnico sanitario'}, 'B'),
                         'mobile food unit plan review & cart inspection')),
    ('inv_software', ('usd', ('fila', _I, {'cof': 'TPV móvil + datáfono'}, 'B'), 'POS, card readers & booking software')),
    ('inv_brew', ('usd', ('fila', _I, {'cof': 'Menaje, utensilios, packaging eco'}, 'B'),
                  'batch brewer, airpots, cold brew system, smallwares & commissary storage racks')),
    ('inv_energia', ('usd', ('fila', _I, {'cof': 'Toldo, mobiliario exterior plegable'}, 'B'),
                     'power: inverter generator (5,500 W), cords & power distribution')),
    # derivadas
    ('ventas_evento', ('usd', ('deriv', lambda c: c['ventas_a1'] / c['clientes_dia']),
                       'average revenue per event, year 1 (excl. sales tax)')),
    ('invitados_a1', ('int', ('deriv', lambda c: c['clientes_dia'] * c['dias']), 'guests served in year 1')),
    ('caida_absorbible_pct', ('pct0', ('deriv', lambda c: c['holgura_caja_pct'] / (1 + c['holgura_caja_pct'])),
                              'drop in events the plan can absorb before cash stops covering costs (1 − break-even ÷ plan)')),
])


def tokens_cof(base):
    out = OrderedDict()
    for t, (fmt, src, desc) in base.items():
        if t in _FUERA:
            continue
        if src[0] == 'fila':
            _, hoja, rot, col = src
            if isinstance(rot, dict):
                if 'ft' not in rot:
                    continue                               # partidas de la cafetería
                src = ('fila', hoja, {'cof': rot['ft']}, col)
        if t == 'consumibles_pct':
            fmt = 'pct1'                               # M1 del BBQ: 3.5 %, no 4 % (aquí 4.0 %)
        out[t] = (fmt, src, _DESC.get(t, desc))
    out.update(TOKENS_PROPIOS)
    return out


# ==========================================================================
# Docx (D229): lo que escribe ensamblar_docx.py y las notas para los redactores
# ==========================================================================
PRODUCTOS_CIERRE_COF = ['Coffee Shop Business Plan Kit', 'Mobile Bar Business Plan Kit',
                        'Coffee Shop Checklists Kit Pro', 'HACCP Food Safety Kit Pro']


def docx_fijos(M):
    pc = PRODUCTOS_CIERRE_COF
    d = OrderedDict([
        (6, 'BUSINESS PLAN'), (7, 'Coffee Cart'),
        (9, 'Complete financial plan, market analysis,\noperations strategy and startup checklist\nto launch a coffee cart '
            'and coffee catering company in the United States'),
        (14, 'AI Chef Pro'), (15, 'aichef.pro'), (16, 'US edition with UK notes · Version 2.2 · October 2026'),
        (18, 'LEGAL NOTICE'), (19, M.AVISO_DOCX_EN), (20, '© 2026 AI Chef Pro — aichef.pro'), (22, 'CONTENTS'),
        (35, 'Appendices: Coffee Cart Financial Projections (Excel) + Coffee Cart Pricing Calculator (Excel) + Coffee Cart '
             'Startup Checklist (Excel) + Coffee Catering Service Agreement Template (Word)'),
        (123, 'AI Chef Pro'), (124, 'Templates and AI tools for food businesses'),
        (126, 'aichef.pro\ninfo@aichef.pro'),
        (127, '→ %s · %s' % tuple(pc[:2])), (128, '→ ' + pc[2]), (129, '→ ' + pc[3]), (130, '\n' + M.URL_TIENDA),
    ])
    return OrderedDict([('cof', d)])


DOCX_NOTAS_PLAN = OrderedDict([
    ('cof', 'REDACTAS, NO TRADUCES (D229). Cada párrafo trae en su nota: (1) el NIVEL de la ranura (casi literal · '
            'adaptar · nueva, F1-inventario §6); (2) la PISTA de lo que va en esa ranura para un COFFEE CATERER (D219): '
            'empresa de café de especialidad para eventos con DOS estaciones (un espresso cart con lavamanos, depósitos '
            'y nevera + un portable espresso bar) que viajan en un remolque cerrado arrastrado por el vehículo del dueño; '
            'servicio hosted (paga el anfitrión) con baristas W-2, espresso, batch brew, cold brew, leches, siropes y '
            'vasos compostables; tres motores: empresa entre semana (el volumen), bodas (el ticket) y fiestas privadas; '
            'festivales y farmers markets guest-pay como complemento; base en una commissary; (3) la PROPUESTA EN DE LA '
            'PAELLA de esa misma ranura (../business-plans-en-7/docx_en_pael_a.json / _b.json, sha256 fijados): da la '
            'FORMA (estructura, tono, longitud, tokens, fuentes comunes); (4) en las ranuras «adaptar» y «nueva», el '
            'párrafo ES 1.0 FINAL DE LA CAFETERÍA MÓVIL de la misma ranura (contenido de referencia: sus cifras, sus '
            '{TOKENS} en mayúsculas y todo lo español NO se usan; el §9 EN mantiene su mapa: commissary [102] y permisos '
            '[103] van en la sección 9, como promete la landing). LA PISTA MANDA; CERO VOCABULARIO DE PAELLA (paella, '
            'paella chef, pans, burners, propane cylinders, socarrat, saffron, seafood, shellstock, tapas, sangria, '
            'cargo van, cooking station, TPHC) y cero «chef» suelto. El «es» de cada párrafo es la RANURA del plan de '
            'FOOD TRUCK: solo da el papel y la longitud (±30 %). Fuentes: research §1-§9 (glosario OBLIGATORIO, regla '
            'de jerga §0) de business-plans-en-11/F1-research-us-delta.md. Cifras del caso SOLO con tokens {{…}}; de '
            'mercado, solo las de research «leída» con su fuente (Flashquotes, GrindKit, operadores de Zola, BLS…). '
            'Prohibido además (gate RX_COF_NO y check_textos): «cafeteria» y «mobile café» (falsos amigos: di coffee '
            'cart / mobile espresso bar / coffee catering), «coffee truck» como NOMBRE del negocio (solo como formato), '
            '«truck» suelto, «per day», «operating days», «customers» (di clients, hosts, guests), «window» salvo '
            '«service window», «recipe costing» / «escandallo» (di cost per drink), «bartender», «cocktails» salvo '
            '«cocktail hour» y «espresso martini», «mobile bar» salvo «licensed mobile bar» y el nombre del kit, '
            '«freelance», «Spain / Spanish», «D-21» y similares, «growing demand» (la demanda es estacional, research '
            '§0), kg / °C / litros / ml fuera de paréntesis, las cifras del ES de la cafetería (107.055, «130 eventos», '
            '«135 invitados», «6,10 €»…), las del CASO DE LA PAELLA ($313,200, «135 events», «$40 per guest», «58 '
            'guests»…) y las de los casos del BBQ, del catering y del bar móvil, «ChefBusiness». ' + REGLA_UNIDADES +
            '. Lo no verificado por la research va como «check with your county / state» o «ask your fire marshal», '
            'nunca como cifra. El cierre (productos) lo escribe el ensamblador'),
])
# §9 = el núcleo legal (D229); research §6
_N9 = OrderedDict([
    (102, '§9 1/7 (NUEVA): commissary y nada de casa: un carro es «mobile food unit» (WA, IN) o «mobile food facility» '
          '(CA), el mismo trámite que un food truck; el FDA Food Code deja la decisión a la autoridad local; en '
          'California las MFF «shall operate in conjunction with» una commissary (Health & Safety Code §114295, '
          'resumen); en Washington «all mobile units must have a commissary kitchen» salvo la exención de RCW 43.20.148, '
          'con acuerdo anual y commissary log a bordo (Snohomish County, leída). Respuesta a la PAA: «usually yes; some '
          'counties exempt self-contained units: ask yours in writing before you buy the cart». Allí se llenan los '
          'depósitos de agua potable, se vacían las aguas grises, se guarda la leche en frío y se aparca el remolque'),
    (103, '§9 2/7 (NUEVA): permiso sanitario: mobile food unit permit + plan review del condado ANTES de comprar el '
          'carro (como ejemplo leído, Snohomish County: plan review $1,100, permiso anual $500 / $745 / $1,025 según '
          'riesgo y aprobación eléctrica previa de L&I); business license, sales tax permit, food handler cards de todo '
          'el equipo y, según el condado, un Certified Food Protection Manager; temporary event permit por cada festival '
          'o mercado. La LECHE es TCS: cold holding a 41 °F (5 °C) o menos (FDA Food Code) en una nevera aprobada a '
          'bordo; lavamanos con agua caliente y depósitos según el condado (sin cifras: «check your county»)'),
    (104, '§9 3/7 (NUEVA): electricidad y bomberos: una máquina de 2 grupos a 220V / 3,400 W pide un circuito dedicado '
          '(NEMA 6-20, 15-17 A) y la checklist pregunta a cada sala «110V or 220V, how many amps, how far»; si no hay, '
          'generador inverter de ~5.5 kW. Sin vapores grasos no hace falta campana tipo I ni el permiso IFC de mobile '
          'food preparation vehicles (resumen), pero el GENERADOR y el propano sí: como ejemplo (resumen), generador no '
          'montado a ≥ 12 ft (3.7 m) de la unidad (NFPA 96 §17.6.2), a 10 ft de edificios, con extintor; New Jersey pide '
          'un Fire Safety Permit con generador en cada montaje → «ask your fire marshal», nunca «no fire permit needed»'),
    (105, '§9 4/7 (NUEVA): lo que se sirve: bollería solo de un obrador con licencia (la cottage food se vende directa '
          'del productor al consumidor; la reventa por un establecimiento suele quedar fuera: «check your state») '
          'y nada de «cottage food pastries are fine»; vasos: el kit presupuesta compostables y lo marca como regla LOCAL '
          '(Seattle exige single-use compostable onsite y prohíbe el foam desde 2009: seattle.gov, resumen); alcohol '
          'fuera: el espresso martini exige licencia → «partner with a licensed mobile bar»; alérgenos US (9 mayores con '
          'sésamo): leche, soja, frutos de cáscara (almendra, coco) y, en la bollería, trigo y huevo; la avena solo '
          '«certified gluten-free» si lo está'),
    (106, '§9 5/7 (adaptar): sales tax: el servicio HOSTED es catering y en muchos estados tributa toda la factura (CA y '
          'NY: ✅ catering EN); en festivales y mercados guest-pay se cobra bebida a bebida y puede exigir registro '
          'donde se vende → el libro aplica {{sales_tax}} a toda la factura (ejemplo editable) con la nota «rate and '
          'taxability depend on your state and on who pays»; nunca la regla de un estado como general. IRS Rev. Rul. '
          '2012-18: el service charge obligatorio es SALARIO; la gratuity y el tip jar (si el anfitrión lo acepta) son '
          'voluntarios y del equipo. Sales tax permit'),
    (107, '§9 6/7 (adaptar): empleo y seguros: baristas de evento en nómina W-2 por horas (FLSA; California AB5), nunca '
          '1099 ni «freelance»; workers\' comp (opcional en Texas, pero salas y lenders lo piden), I-9 / W-4 / new-hire '
          'reporting; salario mínimo estatal; sueldos: BLS OEWS mayo 2025 no tiene ocupación «barista» propia (va '
          'dentro de 35-3023, mediana $15.00/h, p90 $20.51) y el barista de eventos cobra más (Flashquotes modela $25/h). '
          'Seguros ({{seguros_anual}} al año en el ejemplo): general liability $1M/$2M con additional insureds '
          'ilimitados, commercial auto que cubra el remolque, workers\' comp y equipo en tránsito; COI con la sala como '
          'additional insured; sin liquor liability (no hay alcohol). Arizona limita que las ciudades lo exijan (A.R.S. '
          '9-485.02, resumen)'),
    (108, '§9 7/7 (adaptar): el remolque: título, registro y placas en el DMV a nombre del negocio, comprobar la '
          'capacidad de arrastre y el enganche del vehículo; si no hay vehículo propio, una furgoneta usada ≈ $18,000 '
          '(no está en el presupuesto). Como ÚLTIMA frase o frases del párrafo, la nota UK: registrar el food business '
          'en el council 28 días antes de operar (FSA, «check»), street trading licence o consent para vender en la '
          'calle, Food Hygiene Rating, 14 alérgenos, VAT del catering de eventos (once you are VAT-registered); la guía '
          'NCASS del café móvil; sin cifras'),
])
# Nivel de cada ranura (F1-inventario §6): L = casi literal (propuesta de la paella + tokens) · A = adaptar · N = nueva
_NIVEL = {}
for _i in (42, 61, 65, 69, 70, 71, 72, 73, 74, 75, 86, 88, 90, 93, 95, 97, 98, 99, 115, 116, 117):
    _NIVEL[_i] = 'L'
for _i in (39, 41, 43, 48, 49, 53, 54, 55, 56, 57, 58, 62, 63, 64, 66, 82, 85, 87, 89, 94, 96, 106, 107, 108, 111, 112,
           113, 114):
    _NIVEL[_i] = 'A'
for _i in (40, 46, 47, 50, 78, 79, 80, 81, 102, 103, 104, 105):
    _NIVEL[_i] = 'N'
_NIVEL_TXT = {'L': 'CASI LITERAL: parte de la propuesta de la paella y cambia SOLO lo que dice la pista (vocabulario de '
                   'paella, cifras del caso por tokens, fuentes del café)',
              'A': 'ADAPTAR: la propuesta de la paella da la forma; el contenido cambia según la pista y el ES 1.0 de la '
                   'cafetería móvil',
              'N': 'NUEVA (núcleo café): escribe desde la pista, el ES 1.0 de la cafetería móvil y research; la propuesta '
                   'de la paella solo da el tono y la longitud'}
_NOTAS_SECCION = OrderedDict([
    (39, '§1 1/5: la oportunidad: coffee catering en EE. UU.; demanda SOLO con research §2 (búsquedas US del cliente: '
         '«coffee catering» 2,900, «coffee cart for events» 720, «coffee bar for wedding» 720, «coffee cart catering» '
         '590; del emprendedor: «coffee truck business plan» 720, «coffee cart business plan» 320, con pico en enero: '
         'NUNCA «growing demand»); sin tamaño de mercado inventado'),
    (40, '§1 2/5: el concepto (D219): coffee catering company con dos estaciones de espresso (espresso cart + portable '
         'espresso bar) en un remolque cerrado que arrastra el vehículo del dueño; servicio hosted con baristas W-2; '
         'empresa entre semana (el volumen: 69.3 % de las reservas reales son corporativas entre semana, Flashquotes), '
         'bodas (el ticket) y fiestas privadas; festivales y farmers markets guest-pay con minimum sales guarantee; base '
         'en una commissary. No es el coffee shop con local, ni el food truck de ruta diaria, ni un bar de espresso '
         'martinis (licencia)'),
    (41, '§1 3/5: inversión y financiación SOLO con tokens: {{inversion_total}} = {{capex}} + {{fondo_maniobra}}; '
         '{{fondos_propios}} ({{aportacion_pct}}) + préstamo {{prestamo}} al {{tipo_prestamo}} a {{plazo_prestamo}} '
         'años (SBA 7(a): supera el tope de $50,000 del SBA Microloan); lo caro son las máquinas de espresso '
         '({{inv_espresso}}) y el carro ({{inv_carro}}); un solo carro con máquina usada y enchufe de sala cuesta '
         '$16,600-24,000 (cart-king.com)'),
    (42, '§1 4/5: proyecciones: {{eventos_a1}} eventos × {{invitados_evento}} invitados × {{precio_invitado}} → '
         '{{ventas_a1}} / {{ventas_a2}} / {{ventas_a3}}; EBITDA {{ebitda_pct_a1}}; equilibrio {{equilibrio_eventos}} '
         'eventos/año; DSCR mínimo {{dscr_min}}; y la frase honesta: es el caso de un dueño-barista a tiempo completo con '
         'venta corporativa activa y dos estaciones, no la media del primer año'),
    (43, '§1 5/5: el equipo: Owner / Lead Barista & Sales, lead barista a tiempo parcial, event baristas y un on-call '
         'barista / driver, todos W-2 ({{plantilla_puestos}} personas, {{plantilla_jornadas}} FTE); sin inventar '
         'trayectoria'),
    (46, '§2 1/5: qué vende y a quién: empresas (oficinas, conferencias, trade shows, brand activations: entre semana), '
         'parejas (bodas, la cocktail hour o el postre), familias (cumpleaños, baby y bridal showers, graduaciones) y '
         'organizadores de festivales y farmers markets; compran café de especialidad hecho al momento, sin colas y sin '
         'ocuparse de nada'),
    (47, '§2 2/5: propuesta de valor: «unlimited made-to-order espresso drinks during your booked service window» '
         '(iconcoffeecart.com); leche de avena incluida (Houston Coffee Cart en zola.com); signature y seasonal drinks, '
         'house-made syrups; branded cups y latte printing para empresas; montaje en ~1 h (coffeecartboys.com); cero '
         'tomas de agua: el carro es self-contained'),
    (48, '§2 3/5: modelo económico: precio por invitado {{precio_invitado}} sin sales tax con los baristas dentro '
         '({{ventas_evento}} por evento de media, entre la mediana de $1,040 y el P75 de $1,697 de Flashquotes); coffee '
         'bar packages {{cuota_paquetes_pct}} de las ventas y el resto add-ons (horas extra, branded cups y latte '
         'printing, bollería de obrador, travel fees); retainer del 30-50 % para bloquear la fecha y saldo 14 días antes '
         '(grindkit.app); travel fee fuera de un radio gratis; service charge ≠ gratuity'),
    (49, '§2 4/5: posicionamiento frente a otros coffee carts, coffee trucks, cafeterías de barrio que hacen catering y '
         'el café de los caterers generalistas; diferencial: dos estaciones (100 bebidas por hora con 2 baristas), '
         'leches vegetales incluidas, empresa entre semana; no competir por debajo de $612 por reserva (el P10 de '
         'Flashquotes: mano de obra mal cobrada)'),
    (50, '§2 5/5: paquetes y formatos: full-service espresso bar (baristas, 2 h estándar: el 55.3 % de las reservas), '
         'self-serve coffee station / drop-off de cold brew, guest-pay pop-up con minimum sales guarantee; carta '
         'corta: espresso, americano, latte, cappuccino, flat white, mocha, chai latte, hot chocolate, cold brew, '
         'batch brew, signature drink; add-ons; los 3 formatos y la calculadora del kit (precio por invitado, por hora '
         'de servicio y por bebida)'),
    (53, '§3 1/6: el mercado US desde el lado del cliente: research §2 (coffee catering 2,900; mobile coffee bar 880; '
         'coffee cart for events 720; «cart» gana a «truck» ×3-4 en eventos) sin tamaño de mercado inventado'),
    (54, '§3 2/6: precios de referencia: Flashquotes (25,860 reservas de 578 operadores): mediana $1,040, el 50 % '
         'central entre $764 y $1,697, evento típico de 100 invitados; por tamaño: $38 por invitado por debajo de 50, '
         '$18 entre 50 y 99, $13 entre 100 y 249; GrindKit: $700 para 50 invitados y $950 para 100 (2 h hosted); '
         'operadores leídos: $400-1,800 (Big Dipper, Icon desde $850, Houston $1,000-1,500)'),
    (55, '§3 3/6: empresas y bodas: el 69.3 % de las reservas son corporativas entre semana (oficinas, conferencias, '
         'trade shows, brand activations) y ≈ 31 % fines de semana (bodas y privadas) (Flashquotes); boda premium o '
         'brand activation $1,697-3,000; contratos corporativos de varios días $3,000-10,000; en bodas, carro con '
         'barista $700-1,800 (guía de bodas 2026)'),
    (56, '§3 4/6: mezcla del ejemplo (Kit estimate, research §8): 110 eventos de empresa (90 invitados a $12), 30 bodas '
         '(130 a $15), 20 fiestas privadas y showers (45 a $20) y 10 festivales o farmers markets guest-pay (≈ 150 '
         'bebidas a $6.50 con minimum sales guarantee) = {{eventos_a1}} eventos; la empresa es el 65 % de los eventos y '
         'el 58 % de las ventas; estacionalidad Flashquotes con Month 1 = marzo: picos en marzo, mayo y diciembre, '
         'JULIO vende la tercera parte de diciembre'),
    (57, '§3 5/6: tendencias con cuidado: leches vegetales (la avena ya se da incluida), cold brew y bebidas de '
         'temporada, branded cups y latte printing para marcas, estaciones de café en bodas además de la barra de '
         'postres; sin cifras sin fuente'),
    (58, '§3 6/6: riesgos de demanda y REALISMO: concentración corporativa (≈ 65 % de eventos), valle de verano '
         '(julio 3.8 % de las reservas), presupuestos corporativos, conversión de presupuestos del 20-30 % (Flashquotes); '
         '{{eventos_a1}} eventos al año son los de un operador a tiempo completo con venta corporativa activa; '
         'Flashquotes da ≈ 15 reservas por operador y año SOLO en su plataforma (no es el total del operador); el '
         'primer año es más lento (rampa)'),
    (61, '§4 1/6: panorama competitivo local: otros coffee carts y mobile espresso bars (Coffee Cart Boys, Icon, Big '
         'Dipper, Houston Coffee Cart como ejemplos leídos), coffee trucks y trailers, coffee shops que hacen catering, '
         'el café de los caterers y el self-serve de los hoteles'),
    (62, '§4 2/6: cinco fuerzas de Porter aplicadas al coffee catering (estructura del ES [62]): proveedores (tostadores, '
         'lácteos), sustitutos (café de termo del caterer, coffee shop con entrega), clientes corporativos que comparan '
         'por reserva, entrada barata con un carro pero difícil a 100 bebidas por hora'),
    (63, '§4 3/6: competidores directos e indirectos y cómo compararse: precio por reserva y por invitado, horas '
         'incluidas, leches vegetales incluidas o con suplemento ($50 en Sweet Carolinas, zola.com), radio de '
         'desplazamiento gratis, generador incluido o no («no hidden generator or setup fees», coffeecartboys.com), '
         'reseñas en Google, The Knot, Zola y GigSalad'),
    (64, '§4 4/6: barreras de entrada: permiso de unidad móvil con plan review y commissary, máquina de 2 grupos '
         '(≈ $8,500) y la energía (220V o generador), seguros con COI, y el oficio del barista a 50-65 bebidas por hora'),
    (65, '§4 5/6: factores críticos de éxito: velocidad y consistencia, leche fría y segura (41 °F), puntualidad en el '
         'montaje, reseñas, relación con office managers, event planners y salas'),
    (66, '§4 6/6: DAFO del concepto (dos estaciones + remolque + empresa entre semana; margen bruto alto; valle de '
         'verano; dependencia del enchufe de la sala; concentración corporativa)'),
    (69, '§5 1/7: estrategia: dos embudos (empresas: venta activa, reservas recurrentes entre semana; bodas: ciclo largo '
         'con degustación) + fiestas privadas por referidos y marketplaces'),
    (70, '§5 2/7: presencia digital: web con paquetes y precios «desde», formulario de presupuesto (fecha, sala, '
         'invitados, horas), Google Business Profile, Instagram con latte art y el carro en eventos reales'),
    (71, '§5 3/7: directorios y marketplaces: The Knot, WeddingWire y Zola (bodas), GigSalad, Thumbtack y The Bash '
         '(fiestas privadas); mide el coste por reserva ganada'),
    (72, '§5 4/7: alianzas: salas y hoteles (preferred vendor lists), event planners, office managers y coworkings, '
         'organizadores de festivales y farmers markets'),
    (73, '§5 5/7: degustaciones para prospectos (su línea de coste en el P&L: un open house corporativo o una cata para '
         'parejas) y el proceso presupuesto → contrato → retainer'),
    (74, '§5 6/7: fidelización y referidos: empresas que repiten cada trimestre, planners que recomiendan, reseñas '
         'después de cada evento'),
    (75, '§5 7/7: presupuesto: {{marketing_anual}} al año en el ejemplo; medir el coste por evento ganado'),
    (78, '§6 1/5: la base: commissary con permiso (llenado de agua potable y vaciado de grises, nevera para la leche, '
         'almacén seco, aparcamiento del remolque y del carro): {{alquiler_mes}} al mes en el ejemplo; commissary '
         'agreement por escrito y commissary log donde lo pidan'),
    (79, '§6 2/5: el equipo y su orden de compra: espresso cart {{inv_carro}}, portable espresso bar {{inv_barra}}, '
         'máquinas {{inv_espresso}}, molinos {{inv_molinos}}, energía (generador, cables) {{inv_energia}}, batch '
         'brewer y cold brew {{inv_brew}}, remolque cerrado {{inv_remolque}} + {{inv_remolque_wrap}}; primero el plan '
         'review del condado y la potencia (110V / 220V), luego el carro; una máquina de 2 grupos a 220V / 3,400 W pide '
         'circuito dedicado'),
    (80, '§6 3/5: la operativa de un evento: llamada final 3 weeks out (recuento final 10 días antes) → comprobación '
         'de la sala 2 weeks out (enchufe, metros, acceso, aparcamiento del remolque) → la víspera en la commissary: '
         'cold brew, siropes, agua y leche en frío → el día: carga, viaje, montaje ~1 h, calentar y ajustar la molienda, '
         '2-2.5 h de servicio (el 55.3 % de las reservas son de 2 h), recogida y limpieza; un evento de 2 h ocupa 7-9 h '
         'de turno (grindkit.app); 1 barista por 50-65 bebidas por hora (Flashquotes). Nunca «D-1»'),
    (81, '§6 4/5: calidad y seguridad en la operativa: dosis de 18 g (0.63 oz) por doble y ratio 1:2 (1 lb rinde ≈ 23 '
         'dobles netos, Kit estimate), bebidas por invitado 1.0-1.5 según horas y +20-30 % por la mañana (grindkit.app), '
         'leche a 41 °F (5 °C) o menos en nevera y coolers, jarras separadas por tipo de leche, lavamanos primero, '
         'limpieza de lanceta y portafiltros'),
    (82, '§6 5/5: proveedores: tostador de especialidad al por mayor (≈ $14/lb en el ejemplo, entre el retail de BLS '
         '$9.33/lb y el especialidad ≈ $18/lb), leche ($4.11/gal BLS) y avena por distribuidor o cash-and-carry, '
         'vasos compostables, bollería de obrador con licencia, servicio técnico de la espresso y filtros de agua'),
    (85, '§7 1/6: estructura: Owner / Lead Barista & Sales, lead barista (part-time W-2), event baristas (hourly W-2) y '
         'on-call barista / driver (hourly W-2, meses punta)'),
    (86, '§7 2/6: coste de personal: {{personal_a1}} el año 1 ({{personal_pct}} de las ventas), con el sueldo del dueño '
         'dentro; el del dueño y el del lead barista son fijos y el de los event baristas depende de las horas de evento'),
    (87, '§7 3/6: personal por evento: {{horas_evento}} horas por persona × {{personas_evento}} baristas por evento, '
         'cobertura {{cobertura_horas}}; 1 carro con 1 barista sirve 50-65 bebidas por hora y 2 + 2 ≈ 100 (Flashquotes); '
         'las bodas y la empresa grande llevan 2; el libro reparte la nómina en 12 meses (prudente con el valle de verano)'),
    (88, '§7 4/6: W-2 frente a 1099 (FLSA; California AB5), nunca «freelance»; cargas {{cargas_pct}}; mínimo federal y '
         'estatal; BLS OEWS mayo 2025: «barista» va dentro de 35-3023 (mediana $15.00/h, p75 $17.34, p90 $20.51); el '
         'barista de eventos cobra más: $20-35/h en grindkit.app, $25/h en el modelo de Flashquotes; propinas aparte'),
    (89, '§7 5/6: formación: Certified Food Protection Manager, food handler cards, estándares de bebida (dosis, ratio, '
         'leche, latte art), velocidad en la cola, quemaduras de vapor, generador y cables, alérgenos (leche, soja, '
         'frutos de cáscara)'),
    (90, '§7 6/6: service charge frente a gratuity (IRS Rev. Rul. 2012-18): el service charge obligatorio es salario; la '
         'gratuity y el tip jar son voluntarios y del equipo'),
    (93, '§8 1/7: viabilidad: ventas del año 1 {{ventas_a1}}, margen bruto {{margen_bruto_pct}}, EBITDA {{ebitda_a1}} '
         '({{ebitda_pct_a1}}); {{ventas_evento}} por evento, dentro de la banda de Flashquotes (mediana $1,040)'),
    (94, '§8 2/7: inversión con tokens: {{inv_carro}}, {{inv_barra}}, {{inv_espresso}}, {{inv_molinos}}, {{inv_remolque}}, '
         '{{inv_energia}}, {{inv_permisos}}, {{inv_plan_review}}, {{inv_lanzamiento}}, {{inv_stock}} → {{capex}} (con la '
         'contingencia del 10 % sobre el carro, la barra portátil, el remolque, su equipamiento y el plan review, '
         'calculada por fórmula); fondo de maniobra {{fondo_maniobra}}; total {{inversion_total}}; financiación SBA 7(a); '
         'el vehículo de arrastre es el del dueño ($0)'),
    (95, '§8 3/7: proyección a 3 años: {{ventas_a1}} / {{ventas_a2}} / {{ventas_a3}} (crecen los EVENTOS: '
         '{{crecimiento_a2}} y {{crecimiento_a3}}); resultado neto {{resultado_neto_a1}} / {{resultado_neto_a2}} / '
         '{{resultado_neto_a3}}; el {{impuesto_beneficios}} hace de impuesto sobre la renta: con una LLC pass-through lo '
         'paga el dueño en su declaración, así que la reserva se mantiene'),
    (96, '§8 4/7: costes: coffee bar packages {{coste_paquetes_pct}} de sus ventas, mercancía total {{cogs_pct}}, vasos '
         'compostables {{consumibles_pct}}, personal {{personal_pct}}, commissary {{ocupacion_pct}}; benchmarks: coste por '
         'bebida $0.75-1.50 todo incluido y COGS del 20-30 % (grindkit.app); margen bruto del operador 50-70 % '
         '(Flashquotes)'),
    (97, '§8 5/7: punto de equilibrio en EVENTOS al año: {{equilibrio_eventos}} (contable) y {{equilibrio_caja_eventos}} '
         '(caja) frente a {{eventos_a1}} del plan; holgura {{holgura_caja_pct}} (los eventos pueden caer '
         '{{caida_absorbible_pct}} antes de no cubrir la caja); si es justa, DECIRLO; el libro muestra la cifra exacta y el '
         'plan la redondea a eventos enteros'),
    (98, '§8 6/7: caja y retorno: cobras a {{cobro_dias}} días de media y pagas a los proveedores a {{pago_dias}} días '
         '(CADA TOKEN EN SU CELDA, D113); las nóminas salen cada mes; saldo mínimo {{saldo_minimo}} en el mes '
         '{{mes_saldo_minimo}} (con Month 1 = marzo: septiembre, tras el valle de julio y agosto y el primer pago '
         'trimestral del sales tax), payback {{payback}}, DSCR {{dscr_min}}; el retainer no se modela y mejora la caja '
         'real'),
    (99, '§8 7/7: escenarios: pesimista {{pesimista_eventos}} eventos × {{pesimista_precio}} × {{pesimista_invitados}} '
         'invitados → {{pesimista_ventas}}, resultado {{pesimista_resultado}} y caja estimada {{pesimista_caja}} (si es '
         'negativa, DECIRLO: «the cash runs out»); optimista {{optimista_eventos}} eventos → {{optimista_ventas}} y '
         '{{optimista_resultado}}; recordar que {{eventos_a1}} eventos no son la media del primer año'),
    (111, '§10 1/7: conclusión: por qué el modelo se sostiene (sin local, coste de bebida bajo y margen bruto alto, dos '
          'estaciones, la empresa entre semana llena el calendario que las bodas dejan libre) y la advertencia honesta '
          '(valle de julio, concentración corporativa)'),
    (112, '§10 2/7: riesgos y mitigación: cancelación (retainer y tramos), sala sin enchufe de 220V (máquina compacta o '
          'generador), lluvia en exterior (carpa o interior), leche fuera de temperatura (nevera, coolers, termómetro), '
          'avería de la máquina (segunda estación, servicio técnico), julio flojo (mercados y festivales, caja de 3 '
          'meses), falta de baristas en temporada'),
    (113, '§10 3/7: fortalezas competitivas: dos estaciones y 100 bebidas por hora, leches vegetales incluidas, '
          'branded cups para empresas, commissary y permisos en regla, contrato y COI listos'),
    (114, '§10 4/7: hoja de ruta en las 6 fases del checklist (Business Setup → Permits & Commissary → Equipment → Staff '
          '→ Marketing → First 90 Days): plan review y carro en la Phase 2; las fases se solapan; ningún evento pagado con '
          'permisos abiertos'),
    (115, '§10 5/7: KPIs: eventos al mes, precio por invitado, bebidas por invitado y por hora de barista, coste por '
          'bebida, horas de personal por evento, conversión de presupuestos (20-30 %), cancelaciones, reseñas'),
    (116, '§10 6/7: visión a 3 años: más contratos corporativos recurrentes, una tercera estación o un segundo remolque, '
          'local propio solo si los números lo piden (Coffee Shop Business Plan Kit)'),
    (117, '§10 7/7: cierre: los siguientes pasos con el Excel, la calculadora de precios (coste por bebida, precio por '
          'invitado y por hora, baristas y energía por evento), el contrato tipo y el checklist del kit'),
])


def _json_ranuras(base, patron):
    out = {}
    for f in ('a', 'b'):
        p = os.path.join(base, patron % f)
        if os.path.exists(p):
            out.update({int(k): v for k, v in json.load(open(p, encoding='utf-8')).items()})
    return out


def _notas_docx():
    """Nota de cada ranura: nivel + pista + PROPUESTA EN DE LA PAELLA (misma ranura) + ES 1.0 de la cafetería móvil
    (adaptar / nueva) si ya existe (`../plan-cafeteria-movil/textos/caf_es_{a,b}.json`; paso 1c si no)."""
    es = _json_ranuras(os.path.join(CAF, 'textos'), 'caf_es_%s.json')
    pael = _json_ranuras(PAEL, 'docx_en_pael_%s.json')
    out = OrderedDict()
    for i, n in sorted(list(_NOTAS_SECCION.items()) + list(_N9.items())):
        nivel = _NIVEL.get(i, 'A')
        n = '[%s] %s' % (_NIVEL_TXT[nivel], n)
        if i in pael:
            n += ' ‖ PROPUESTA EN DE LA PAELLA EN ESTA RANURA (la forma; cero vocabulario de paella): «%s»' % pael[i]
        if i in es and nivel != 'L':
            n += (' ‖ ES 1.0 FINAL DE LA CAFETERÍA MÓVIL EN ESTA RANURA (referencia de contenido de la MISMA sección; si '
                  'trata otro subtema que la pista, manda la pista; sus cifras, sus {TOKENS} en mayúsculas y todo lo español '
                  '—normas, IVA, autónomo, comunidades, Bizum, furgoneta, «feria»— NO se usan): «%s»' % es[i])
        out[i] = n
    return out


DOCX_NOTAS = OrderedDict([('cof', _notas_docx())])

# ==========================================================================
# Pistas por celda (extraer_textos.py → textos_es.json → tandas)
# ==========================================================================
_CASO = ('D220: caso US = 170 eventos/año × 95 invitados × $12.60 por invitado (sin sales tax, con los baristas, los '
         'desplazamientos y los extras dentro, sin la gratuity voluntaria) ≈ $203,490 (research §8); drivers: B4 = '
         'eventos/año, B5 = precio por invitado, B6 = invitados por evento. Las notas describen el MÉTODO: sin cifras del '
         'caso (cambian al recalibrar). La propuesta EN es la de la PAELLA en esta celda: cambia lo que hable de paella, '
         'paelleras, quemadores, propano, marisco, van o del caso de la paella')
CELDA_PISTAS = OrderedDict([
    (('COFP', _S, 'C4'), _CASO + '; los años 2-3 crecen en EVENTOS (B7/B8); compara con la capacidad de las dos '
                                 'estaciones (fila 51); el ejemplo es un operador a tiempo completo con venta corporativa '
                                 'activa, no la media del primer año; Flashquotes da ≈ 15 reservas por operador y año SOLO '
                                 'en su plataforma'),
    (('COFP', _S, 'C5'), _CASO + '; precio medio por invitado de la MEZCLA (empresa, bodas, fiestas privadas, festivales '
                                 'guest-pay) SIN sales tax, con los baristas, el desplazamiento y los extras dentro y SIN la '
                                 'gratuity. Los operadores cotizan por reserva y por hora (base $300-500 + $150-200 por hora '
                                 'de servicio, Flashquotes; $700 para 50 invitados y $950 para 100 en grindkit.app): la '
                                 'calculadora del kit cotiza por invitado, por hora y por bebida; para pasar de ella a esta '
                                 'celda, divide lo facturado en el año entre los invitados del año (D227)'),
    (('COFP', _S, 'C6'), _CASO + '; invitados medios por evento; la mezcla del ejemplo va de fiestas de 45 a bodas de 130; '
                                 'en un festival cada bebida vendida cuenta como un invitado; el evento típico de '
                                 'Flashquotes es de 100 invitados'),
    (('COFP', _S, 'C7'), 'D220: crecimiento de EVENTOS 10 % en el año 2 (empresas que repiten y bodas reservadas con meses; '
                         'lo limitan dos estaciones y los baristas)'),
    (('COFP', _S, 'C8'), 'D220: crecimiento de EVENTOS 6 % en el año 3, por la misma razón'),
    (('COFP', _S, 'C11'), 'D223: cuota de COFFEE BAR PACKAGES (baristas, bebidas de espresso, batch y cold brew, leches, '
                          'siropes y vasos) 85 %; el resto (fila 12) son add-ons: horas extra, branded cups y latte '
                          'printing, bollería de un obrador con licencia, travel fees. Es una ENTRADA'),
    (('COFP', _S, 'C12'), 'D223: calculado como el resto: coffee bar packages + add-ons = 100 %'),
    (('COFP', _S, 'C13'), 'D220: coste de los coffee bar packages 12 % = café (≈ $14/lb, 18 g por doble), leche y avena, '
                          'siropes y cold brew con un 10 % de merma (purga, dial-in, leche sobrante): Kit estimate a partir '
                          'del coste por bebida de $0.75-1.50 todo incluido (grindkit.app); el coste de UNA bebida de la '
                          'calculadora no se copia aquí: esta celda es la media de la mezcla'),
    (('COFP', _S, 'C14'), 'D220: coste de los add-ons 25 % (Kit estimate: bollería comprada a un obrador, branded cups y '
                          'tinta de impresión; las horas extra y el travel fee casi no tienen coste de mercancía)'),
    (('COFP', _S, 'C15'), 'D223: vasos compostables, tapas, fundas, removedores de madera y servilletas 4 % (Kit estimate: '
                          '≈ $0.30 por bebida); compostable porque varias ciudades lo exigen (Seattle, como ejemplo); escala '
                          'con las bebidas'),
    (('COFP', _S, 'C16'), 'D224: FESTIVALES y FARMERS MARKETS guest-pay (pop-ups donde cada invitado paga su bebida, a '
                          'menudo con minimum sales guarantee del organizador): 5 % de las ventas en el ejemplo; pon 0 si '
                          'solo trabajas eventos hosted'),
    (('COFP', _S, 'C17'), 'D224: cuota u honorario del organizador sobre lo vendido en el festival o el mercado (Kit '
                          'estimate 15 %; si te cobran una cuota fija por puesto, conviértela en % de lo que esperas '
                          'vender); sin efecto si la fila 16 es 0'),
    (('COFP', _S, 'C18'), 'D220: tarjeta 3 %: los anfitriones pagan retainer y saldo con tarjeta; en festivales casi todo '
                          'es tarjeta; algunas empresas pagan por ACH'),
    (('COFP', _S, 'C24'), 'D223: commissary con permiso: llenado de agua potable y vaciado de grises, nevera para la leche, '
                          'almacén seco, aparcamiento del carro y del remolque ($200-600 al mes en cart-king.com + '
                          'almacén: Kit estimate); nunca «support kitchen»'),
    (('COFP', _S, 'C25'), 'D223: meses de depósito de la commissary'),
    (('COFP', _S, 'C26'), 'D223: combustible del generador (solo en eventos al aire libre: casi todas las salas dan '
                          'enchufe), agua y hielo que no cubre la commissary; fijo y pequeño'),
    (('COFP', _S, 'C27'), 'D223: seguros al año = general liability $1M/$2M con additional insureds ilimitados (≈ $750 en '
                          'coffee shops, resumen: Kit estimate) + commercial auto que cubra el remolque + workers\' comp + '
                          'equipo en tránsito; las salas piden COI y additional insured; sin liquor liability (no hay '
                          'alcohol)'),
    (('COFP', _S, 'C28'), 'D223: varios 3 % de las ventas: imprevistos de cada evento (leche extra, hielo, parking en la '
                          'sala, cables); es VARIABLE. El combustible del vehículo va en la fila 27 del P&L (fijo)'),
    (('COFP', _S, 'C30'), 'D220: fondos propios del dueño (≈ 30 % de la necesidad en el ejemplo)'),
    (('COFP', _S, 'C31'), 'D220: préstamo que calibra el libro: supera el tope de $50,000 del SBA Microloan, así que el '
                          'ejemplo encaja en un SBA 7(a) o un préstamo bancario (o en un Microloan con más fondos propios); '
                          'el lender pide plan y proyecciones'),
    (('COFP', _S, 'C33'), 'D220: 7 años: el carro, la barra portátil y el remolque pierden valor antes que un local'),
    (('COFP', _S, 'C44'), 'D222: 7 años: espresso cart, portable espresso bar, remolque cerrado y su equipamiento, y el plan '
                          'review (la base de vida del vehículo, fila 31 de "Startup Costs")'),
    (('COFP', _S, 'C45'), 'D222: 5 años: máquinas de espresso, molinos, generador y cables, batch brewer y cold brew, '
                          'smallwares, TPV y software (las muelas y las juntas se cambian antes: van en el mantenimiento)'),
    (('COFP', _S, 'C51'), 'D220: DATO INFORMATIVO (no entra en ningún cálculo): el techo de eventos al año que tus dos '
                          'estaciones y tus baristas pueden atender (entre semana hay capacidad: la empresa la llena); '
                          'compáralo con la fila 4 y con el optimista'),
    (('COFP', _S, 'C52'), 'D220: rampa 45 % → 9 meses: las empresas tardan en repetir y las bodas se reservan con meses '
                          '(mediana de 41 días de antelación, Flashquotes)'),
    (('COFP', _S, 'C54'), 'D220: 1 mes de commissary antes de abrir (plan review, pruebas de las dos estaciones, open house '
                          'corporativo)'),
    (('COFP', _S, 'C55'), 'D222: imprevistos 10 % sobre el carro, la barra portátil, el remolque, su equipamiento y el plan '
                          'review (filas 7, 8, 11, 12 y 15 de "Startup Costs")'),
    (('COFP', _S, 'C58'), 'D220: cobro medio 14 días: retainer del 30-50 % al reservar (grindkit.app) y saldo 14 días antes '
                          'en bodas y fiestas; las empresas pagan a 15-30 días; el libro no modela anticipos (nota de la '
                          'Tesorería)'),
    (('COFP', _S, 'C62'), 'D219: alcohol 0 %: sin licencia no vendes alcohol; los espresso martinis, con un licensed mobile '
                          'bar (Mobile Bar Business Plan Kit); nunca «bartender» (gate)'),
    (('COFP', _S, 'C63'), 'D220: solo si vendieras alcohol con licencia (0 % en este plan)'),
    # Startup Costs, notas de la columna D (D222; research §4)
    (('COFP', _I, 'D7'), 'D222: espresso cart con certificación NSF, lavamanos, depósitos de agua potable y grises (el '
                         'volumen lo fija tu condado), bomba y filtro, nevera bajo barra: carro nuevo básico $4,000-10,000 '
                         'y custom premium $15,000-25,000 (cart-king.com); pide al condado la checklist del plan review '
                         'ANTES de comprarlo'),
    (('COFP', _I, 'D8'), 'D222: portable espresso bar para la segunda estación y los salones interiores, con nevera bajo '
                         'barra (Kit estimate)'),
    (('COFP', _I, 'D9'), 'D222: una máquina volumétrica de 2 grupos a 220V / 3,400 W (≈ $8,500-9,000, NEMA 6-20, 15-17 A, '
                         'circuito dedicado) + una compacta de 2 grupos (≈ $7,200, 14 A) para la segunda estación; '
                         'precios de tienda (resumen): pide dos presupuestos'),
    (('COFP', _I, 'D10'), 'D222: cuatro molinos de espresso (casa + descafeinado en cada estación); $300-3,000 cada uno '
                          '(cart-king.com)'),
    (('COFP', _I, 'D11'), 'D222: remolque cerrado de 6×12 ft con rampa: transporta el carro, la barra y el equipo; lo '
                          'arrastra el vehículo del dueño ($0 en el ejemplo); si no tienes, una furgoneta usada ronda los '
                          '$18,000 (no está en el presupuesto)'),
    (('COFP', _I, 'D12'), 'D222: rotulación (wrap), enganche, anclajes en E-track y rampas para subir el carro; comprueba '
                          'la capacidad de arrastre de tu vehículo'),
    (('COFP', _I, 'D13'), 'D222: LLC + contrato tipo revisado por un abogado de tu estado (parte del contrato del kit): '
                          'retainer, tramos de cancelación, recuento final, horas de servicio, enchufe o generador, plan '
                          'de lluvia'),
    (('COFP', _I, 'D14'), 'D222: permisos y certificaciones del año 1: health permit de la unidad móvil, food handler cards, '
                          'Certified Food Protection Manager, business license, sales tax permit, permiso del fire marshal '
                          'para el generador donde lo pidan; varía mucho por estado y condado'),
    (('COFP', _I, 'D15'), 'D222: plan review de la unidad móvil e inspección del carro (como ejemplo leído, Snohomish '
                          'County: plan review $1,100) + la aprobación eléctrica que pida tu estado'),
    (('COFP', _I, 'D16'), 'D222: TPV con lectores de tarjeta (también para los festivales) y software de reservas, '
                          'presupuestos y firma electrónica'),
    (('COFP', _I, 'D17'), 'D222: batch brewer, airpots, sistema de cold brew, jarras de leche, básculas, tampers, '
                          'knock boxes, cubos de sanitizante y estanterías de la commissary; se amortizan'),
    (('COFP', _I, 'D18'), 'D222: inventario inicial: café para las pruebas y los primeros eventos, leches, siropes, vasos '
                          'compostables'),
    (('COFP', _I, 'D19'), 'D222: web, fotos en eventos reales, catas, un open house corporativo y el primer bridal show; '
                          'altas en The Knot, Zola y GigSalad'),
    (('COFP', _I, 'D20'), 'D222: generador inverter de 5,500 W continuos (silencioso, para salas sin enchufe y eventos al '
                          'aire libre), cables de calibre adecuado, regleta de distribución con GFCI; el fire marshal puede '
                          'pedir distancia y extintor'),
    (('COFP', _I, 'D27'), 'D222: lo que compras: el carro, la barra portátil, las máquinas y los molinos, el remolque, la '
                          'energía, el lanzamiento y la constitución; el colchón de caja no es inversión'),
    # 3-Year P&L, notas (D223, D225)
    (('COFP', _P, 'F10'), 'D223: ventas de coffee bar packages por invitado: barra de espresso con baristas, batch y cold '
                          'brew, leches y siropes, vasos (empresa, bodas, fiestas privadas y festivales)'),
    (('COFP', _P, 'F11'), 'D223: ventas de add-ons: horas extra, branded cups y latte printing, bollería de obrador, travel '
                          'fees'),
    (('COFP', _P, 'F16'), 'D224: cuotas de los organizadores de festivales y farmers markets sobre las ventas de ese canal'),
    (('COFP', _P, 'F22'), 'D223: el importe mensual se teclea en "0. Assumptions"; aquí × 12: commissary, almacén del carro '
                          'y aparcamiento del remolque'),
    (('COFP', _P, 'F24'), 'D223: combustible del generador, agua y hielo que no cubre la commissary'),
    (('COFP', _P, 'F27'), 'D223: combustible, mantenimiento y registro del vehículo de arrastre y del remolque: FIJO en este '
                          'libro'),
    (('COFP', _P, 'F32'), 'D223: teléfono, internet y datos de los lectores de tarjeta'),
    (('COFP', _P, 'F33'), 'D223: servicio técnico de la espresso, filtros de agua y muelas de los molinos (las juntas y las '
                          'muelas se gastan antes que la máquina)'),
    (('COFP', _P, 'F34'), 'D223: Certified Food Protection Manager, food handler cards del equipo y formación de baristas'),
    (('COFP', _P, 'F35'), 'D223: catas para parejas y open houses para empresas; muchos operadores las descuentan si '
                          'reservan'),
    (('COFP', _P, 'F51'), 'D225: suelo del margen bruto del motor 72 % (kit benchmark, editable): el margen bruto del libro '
                          'resta también vasos, tarjeta, cuotas de festival y varios'),
    (('COFP', _P, 'F53'), 'D225: techo del coste de mercancía 20 % (kit benchmark, editable; COGS de 20-30 % del ingreso por '
                          'bebida en grindkit.app)'),
    (('COFP', _P, 'F54'), 'D225: techo de personal 40 % (kit benchmark, editable), con el sueldo del dueño dentro'),
    (('COFP', _P, 'F55'), 'D225: techo de commissary 6 % (kit benchmark, editable): no hay local'),
    (('COFP', _P, 'F56'), 'D225: suelo del resultado neto 5 % (kit benchmark, editable)'),
    # Staffing, notas (D223)
    (('COFP', _R, 'J5'), 'D223: Owner / Lead Barista & Sales: vende a empresas y parejas, hace las catas y lleva la barra '
                         'en los eventos; el resto de su retribución sale del beneficio'),
    (('COFP', _R, 'J6'), 'D223: lead barista (part-time W-2, 0.3 FTE): lleva la segunda estación y el segundo evento del '
                         'día; paga por encima del p90 de 35-3023 (BLS OEWS mayo 2025: $20.51) porque el barista de eventos '
                         'cobra más ($20-35/h, grindkit.app)'),
    (('COFP', _R, 'J7'), 'D223: event baristas por horas y en W-2; su FTE es una fracción; 1 barista por 50-65 bebidas por '
                         'hora (Flashquotes); las propinas voluntarias son suyas'),
    (('COFP', _R, 'J8'), 'D223: on-call barista / driver por horas y en W-2: refuerza en marzo-mayo y diciembre, carga y '
                         'arrastra el remolque'),
    (('COFP', _R, 'J18'), 'D220: horas por persona y evento: carga en la commissary, viaje, montaje ~1 h, 2-2.5 h de '
                          'servicio, recogida y limpieza (un evento de 2 h ocupa 7-9 h de turno: grindkit.app)'),
    (('COFP', _R, 'J19'), 'D220: baristas por evento: 1 en fiestas pequeñas y festivales tranquilos, 2 en bodas y en la '
                          'empresa grande (Kit estimate a partir de 50-65 bebidas por barista y hora); ponderado ≈ 1.6'),
    (('COFP', _ES, 'E23'), 'D220: la MISMA plantilla en los tres escenarios; en el pesimista el coste real de los event '
                           'baristas baja con los eventos (pagas horas por evento), así que el resultado real sería algo '
                           'mejor'),
    (('COFP', _N, 'A5'), 'D219: «0. Assumptions» es la hoja de mando: eventos al año, precio por invitado sin sales tax, '
                         'invitados por evento, mezcla coffee bar packages / add-ons, coste de mercancía; el carro y la barra '
                         'viajan en un remolque cerrado'),
    (('COFP', _N, 'A12'), 'SPEC §4.1 línea 8 (I1): el Word del kit usa las MISMAS cifras de ejemplo que este libro; si '
                          'cambias el libro, actualiza las del Word. La calculadora de precios (coste por bebida, precio por '
                          'invitado y por hora) y el contrato son otros ficheros y no leen este libro'),
])
_D18 = ('D18 (coffee caterer): la propuesta es la de la PAELLA EN (o del Catering) en esa celda, que ya describe el MÉTODO '
        'del libro para un negocio de eventos con comida; reescribe SOLO lo que hable de paelleras, quemadores, propano, '
        'marisco, la van o la paella → el carro y la barra portátil, el remolque, el generador, la leche y el café, la '
        'commissary, los baristas. Sin cifras del caso')
_D18_FILA = OrderedDict([
    (39, 'Fila del espacio: «Commissary, cart storage and trailer parking» (el coste del espacio, en "0. Assumptions"): '
         'el café se prepara en el carro, pero el agua, la leche y el carro duermen en una commissary con permiso'),
    (41, 'Fila de la amortización: dos vidas: el carro, la barra portátil, el remolque y su equipamiento en una, y las '
         'máquinas de espresso, los molinos, el generador y el resto del equipo en otra'),
    (42, 'Fila de seguros del vehículo: el commercial auto que cubre el remolque y el seguro del equipo en tránsito, una '
         'sola vez y como gasto anual'),
    (43, 'Fila del combustible (= FT): «Generator fuel»: va DENTRO de la celda de suministros (casi todas las salas dan '
         'enchufe; el generador solo trabaja al aire libre), no en una línea aparte'),
    (44, 'Fila de la contingencia: un porcentaje calculado sobre el carro, la barra portátil, el remolque y el plan review'),
    (49, 'Fila «Fuel and miscellaneous»: A «Miscellaneous event costs» · B «A miscellaneous line typed in among the fixed '
         'costs» · C «A percentage of sales, treated as a variable cost; tow vehicle fuel has its own fixed line» · D «Extra '
         'milk, ice, cables and venue parking rise and fall with the number of events: among the fixed costs they would '
         'distort the break-even.»'),
    (50, 'Fila del coste de mercancía: coffee bar packages y add-ons, cada uno con su porcentaje'),
])
for _f in range(35, 52):
    for _col in 'ABCD':
        CELDA_PISTAS[('COFP', _N, '%s%d' % (_col, _f))] = _D18 + ('. ' + _D18_FILA[_f] if _f in _D18_FILA else '')
PISTA_D19_GENERICA = ('Celda a celda: escribe SOLO el texto de ESTA celda (una tabla o una tarea): mira su pista '
                      'propia')
_D19_BASE = ('D19/D225: tabla «US COFFEE CART & COFFEE CATERING BENCHMARKS (sourced) AND KIT ESTIMATES» (Benchmark | '
             'Value | Source | Note). Value en formato US; Source = el DOMINIO de la fuente LEÍDA de research §4-§6, o «Kit '
             'estimate» si allí figura como «(resumen)». Esta fila: ')
_D19 = OrderedDict([
    (55, 'precio por reserva de coffee cart: mediana $1,040 · P25 $764 · P75 $1,697 (P10 $612, P90 $3,000); evento típico '
         '100 invitados — flashquotes.com (25,860 reservas de 578 operadores, abr-2023 → abr-2026) [NUEVA]'),
    (56, 'precio por invitado según tamaño: < 50 invitados ≈ $38 · 50-99 ≈ $18 · 100-249 ≈ $13 · 250-499 ≈ $11 — '
         'flashquotes.com; GrindKit: $5-11 por invitado a 100 invitados es «sano», < $5 = pérdida (grindkit.app) [NUEVA]'),
    (57, 'bebidas por invitado: ≤ 2 h 1.0 · 2-4 h 1.3-1.5 · 4-6 h 1.5-1.8 · 6+ h 2.0-2.5; por la mañana +20-30 % — '
         'grindkit.app [NUEVA]'),
    (58, 'permiso de unidad móvil (ejemplo de un condado): plan review $1,100 · permiso anual $500 / $745 / $1,025 según '
         'riesgo · aprobación eléctrica previa — snohd.org (Snohomish County, WA); varía por condado [NUEVA]'),
    (59, 'bebidas por hora: 1 carro + 1 barista 50-65 · 2 + 2 ≈ 100; 2-3 baristas para ~250 invitados — flashquotes.com; '
         '«50 cups per hour» (coffeecartboys.com) [NUEVA]'),
    (60, 'coste por bebida todo incluido $0.75-1.50 (doble $0.25-0.45 · leche $0.20-0.40 · avena $0.60-1.10 · vaso y tapa '
         '$0.20-0.45); COGS 20-30 % del ingreso por bebida — grindkit.app [NUEVA: la fila 60 de la paella era food cost '
         'de catering]'),
    (61, 'coste de arranque: un carro $5,000-25,000 (Kit estimate: resumen de búsqueda); carro típico $24,000 y premium '
         '$49,000 (cart-king.com); máquina de 2 grupos ≈ $8,500 (precio de tienda, Kit estimate) [NUEVA]'),
    (62, 'precios de insumos: café molido $9.33/lb y leche entera $4.11/gal (medias nacionales, septiembre de 2026) — '
         'bls.gov (APU0000717311, APU0000709112); el café de especialidad mayorista ronda los $18/lb (Kit estimate) '
         '[NUEVA: la fila 62 de la paella era el marketplace]'),
    (63, 'estructura de precio: base $300-500 + $150-200 por hora de servicio; desplazamiento $1.25 por milla ida y '
         'vuelta — flashquotes.com; retainer del 30-50 % no reembolsable y saldo 14 días antes — grindkit.app [NUEVA]'),
    (64, 'sueldos BLS OEWS mayo 2025: no hay ocupación «barista» propia: va dentro de 35-3023 Fast Food and Counter Workers, '
         'mediana $15.00/h · p75 $17.34 · p90 $20.51 — bls.gov; el barista de eventos cobra más ($20-35/h en '
         'grindkit.app) [NUEVA]'),
    (65, 'commissary compartida $15-$45 la hora (el 42 % cobra $20-$29) — thefoodcorridor.com (2023 Shared Kitchen '
         'Operator Survey); un carro paga sobre todo almacén y agua: $200-600 al mes (cart-king.com) [propuesta de la '
         'paella + nota del café]'),
    (66, 'estacionalidad de las reservas: diciembre 11.7 % · marzo 11.2 % · mayo 10.9 % · julio 3.8 % (el mínimo) — '
         'flashquotes.com [NUEVA]'),
    (67, 'seguros (Insureon, < 5 empleados): general liability $45/mes, BOP $96, workers\' comp $82, commercial auto $204 — '
         'insureon.com [propuesta de la paella; nota: sin la llama abierta de la paella; pide additional insureds '
         'ilimitados para las salas]'),
    (68, 'tasa de cierre y antelación: 20-30 % de los presupuestos se convierten en reservas (> 30 % = demasiado barato); '
         'mediana de 41 días de antelación — flashquotes.com [NUEVA]'),
])
for _f, _p in _D19.items():
    for _col in 'ABCD':
        CELDA_PISTAS[('COFP', _N, '%s%d' % (_col, _f))] = _D19_BASE + _p

# Checklist (D228): una pista por FILA de tarea (columnas B tarea · C responsable · D plazo · E nota práctica). La
# propuesta EN es la tarea de la PAELLA en ESA celda (columna C ya con «Lead barista»). Cada fila: (columnas que CAMBIAN,
# pista). '' = la tarea sobrevive tal cual (sus celdas limpias entran directas: GLP-check); 'E', 'BE'… = esas columnas
# van a la tanda; 'BCDE' = tarea nueva. Toda celda con vocabulario de paella va a la tanda aunque su columna no esté marcada
_CK = ('D228: escribe una TAREA de un coffee caterer (B tarea · C responsable · D plazo · E nota práctica, una celda cada '
       'vez) con el checklist ES de la cafetería móvil (fuente_es_cof.json, cuando exista) + research §6 y el glosario §9; '
       'columna C: «Owner», «Lead barista», «Event baristas» (nunca «Paella chef» ni «chef»); plazos US («Week 1», «3 '
       'weeks out», nunca «D-21»); ' + REGLA_UNIDADES + '. Esta fila: ')
TAREAS_COF = OrderedDict([
    ('F1 - Constitución', [
        ('', 'contador / bookkeeper y estimated taxes trimestrales (semana 1) [sobrevive]'),
        ('E', 'estructura: LLC, con o sin elección de S corp; en E, la responsabilidad importa porque sirves bebidas '
              'calientes y llevas un generador a eventos ajenos (no «open flame») [sobrevive con ajuste: E]'),
        ('', 'registrar la LLC en el Secretary of State + registered agent + operating agreement [sobrevive]'),
        ('', 'EIN + alta estatal de nóminas y desempleo [sobrevive]'),
        ('', 'cuenta bancaria del negocio y finanzas separadas [sobrevive]'),
        ('E', 'seller\'s permit / sales tax permit: el servicio hosted suele tributar como catering (toda la factura: '
              'café, baristas, extras y desplazamiento); en festivales y mercados se cobra bebida a bebida y puede hacer '
              'falta registrarse donde vendes; «check your state» [sobrevive con ajuste: E]'),
        ('', 'business license de la ciudad o el condado (+ DBA) [sobrevive]'),
        ('E', 'solicitar el préstamo a dos lenders (banco o SBA 7(a)) con el plan, el Excel y presupuestos escritos del '
              'carro, las máquinas de espresso, los molinos y el remolque; no comprar el carro antes del plan review ni de '
              'la aprobación [sobrevive con ajuste: E]'),
        ('BE', 'contrato tipo de coffee catering con un abogado de tu estado, partiendo del modelo del kit: retainer del '
               '30-50 % para bloquear la fecha (grindkit.app), saldo 14 días antes, recuento final 10 días antes, tramos '
               'de cancelación sin huecos, horas de servicio y hora extra, ENCHUFE (110V o 220V a X ft) o suplemento de '
               'generador, travel fee fuera del radio gratis, leches vegetales, plan de lluvia, COI para la sala [sobrevive '
               'con ajuste: B y E]'),
        ('BE', 'plan de seguridad alimentaria del carro: la leche es TCS → cold holding a 41 °F (5 °C) o menos (mínimo del '
               'FDA Food Code) en nevera y coolers, fecha en la leche abierta, agua potable de approved source en depósitos '
               'de grado alimentario, lavamanos primero, limpieza de lanceta y jarras, alérgenos (leche, soja, frutos de '
               'cáscara; trigo y huevo en la bollería), bollería solo de obrador con licencia [sobrevive con ajuste: B y E]'),
        ('', 'Certified Food Protection Manager (ServSafe Manager) del dueño / lead barista [sobrevive]'),
    ]),
    ('F2 - Vehículo', [
        ('BE', 'elegir una commissary con permiso: llenado de agua potable y vaciado de aguas grises, nevera para la '
               'leche, almacén seco, aparcamiento o almacén del carro y del remolque; «Do you need a commissary for a '
               'coffee cart? Usually yes» (CA Health & Safety Code §114295, resumen; WA salvo la exención de RCW '
               '43.20.148, Snohomish County); nunca desde casa [sobrevive con ajuste: B y E]'),
        ('E', 'commissary agreement por escrito: horas, llenado y vaciado de agua, almacén del carro y del remolque, '
              'limpieza; commissary log a bordo donde lo pidan (Washington) [sobrevive con ajuste: E]'),
        ('BE', 'mobile food unit permit + plan review del condado ANTES de comprar el carro: fichas NSF, volumen de los '
               'depósitos, lavamanos, nevera, plano eléctrico (Snohomish, como ejemplo: plan review $1,100, permiso anual '
               '$500-1,025, aprobación eléctrica de L&I); pregunta si un carro en eventos privados con catering cuenta '
               'como unidad móvil o como caterer [sobrevive con ajuste: B y E]'),
        ('E', 'temporary food event permits para eventos públicos o comunitarios (festivales, farmers markets): en E, '
              'el permiso de la unidad móvil no siempre cubre un festival; pregunta al condado y al organizador con '
              'cuánta antelación (no «catering permit») [sobrevive con ajuste: E]'),
        ('BE', 'fire marshal: el generador y, si lo hubiera, el propano: sin vapores grasos no hace falta campana, pero el '
               'generador sí tiene reglas (como ejemplo, a ≥ 12 ft (3.7 m) de la unidad y a 10 ft de edificios, con '
               'extintor: NFPA 96, resumen; New Jersey pide permiso con generador en cada montaje): «ask your fire marshal» '
               '[sobrevive con ajuste: B y E]'),
        ('BE', 'comprar el espresso cart (NSF, lavamanos, depósitos de agua potable y grises del volumen que pida el '
               'condado, nevera bajo barra) con la checklist del plan review en la mano; nuevo o de segunda mano con '
               'inspección [sobrevive con ajuste: B y E]'),
        ('BE', 'título y registro del remolque en el DMV a nombre del negocio + commercial auto que cubra el arrastre + '
               'seguro del equipo en tránsito (carro, máquinas, molinos); comprueba la capacidad de arrastre y el enganche '
               'del vehículo [sobrevive con ajuste: B y E]'),
        ('BE', 'comprar y equipar el remolque cerrado: rampa, anclajes E-track, calzos para el carro, estanterías, '
               'rotulación (wrap); el carro y la barra viajan sujetos [sobrevive con ajuste: B y E]'),
        ('E', 'general liability $1M/$2M con additional insureds ilimitados; las salas y los planners piden COI con ellos '
              'como additional insured (pídelo por escrito); sin «open flame» [sobrevive con ajuste: E]'),
        ('BE', 'política de alcohol: sin licencia no hay espresso martinis ni licores en tus bebidas: deriva a un licensed '
               'mobile bar; confirma con tu corredor que la GL no cubre alcohol que no vendes [sobrevive con ajuste: B y E]'),
        ('', 'workers\' comp antes del primer empleado (opcional en Texas) [sobrevive]'),
        ('BE', 'aguas grises solo en la commissary (nunca en la sala ni en un desagüe pluvial), posos de café a compost, '
               'reciclaje de envases de leche [sobrevive con ajuste: B y E]'),
        ('', 'control de plagas con empresa con licencia (vía commissary) [sobrevive]'),
    ]),
    ('F3 - Equipamiento', [
        ('E', 'lista de equipo propio frente a alquilado por formato: full-service espresso bar, self-serve coffee station '
              '/ drop-off de cold brew y pop-up guest-pay [sobrevive con ajuste: E]'),
        ('BE', 'cadena de frío de la leche: neveras bajo barra en las dos estaciones, coolers con placas de hielo para la '
               'reserva a 41 °F (5 °C) o menos, termómetros calibrados; airpots para el batch brew [sobrevive con ajuste: '
               'B y E]'),
        ('BE', 'cuentas de proveedores: tostador de especialidad al por mayor (≈ $14/lb en el ejemplo; tueste de 1-3 '
               'semanas), leche y avena por distribuidor o cash-and-carry, vasos compostables [sobrevive con ajuste: B y '
               'E]'),
        ('BCDE', 'comprar las máquinas de espresso (2 grupos a 220V + compacta de 2 grupos) y los molinos, instalarlas y '
                 'ajustarlas (dial in); confirma amperios y enchufe (NEMA 6-20 para la de 220V) antes del primer evento '
                 '[nueva]'),
        ('BE', 'smallwares: jarras de leche de varios tamaños, básculas, tampers, knock boxes, vasitos de shot, paños, '
               'cubos de sanitizante y tiras de prueba [sobrevive con ajuste: B y E]'),
        ('BCDE', 'siropes, salsas, leches vegetales y té: receta y etiqueta de los house-made syrups, avena, almendra y '
                 'soja, chai; lista de alérgenos por bebida [nueva]'),
        ('BCDE', 'montar la segunda estación: portable espresso bar, menú y cartelería, expositor de vasos, estación de '
                 'condimentos; cables y regleta con GFCI (y el generador para exterior) [nueva]'),
        ('BCDE', 'agua para la espresso: depósitos de grado alimentario, bomba, filtro o descalcificador según la dureza '
                 'del agua; plan de llenado y vaciado en la commissary [nueva]'),
        ('E', 'vasos y desechables: vasos compostables de 8 / 12 / 16 oz, tapas, fundas, removedores de madera, '
              'servilletas, vasos fríos; compostables donde tu ciudad lo exija (Seattle, como ejemplo); sin foam '
              '[sobrevive con ajuste: E]'),
        ('BE', 'registro de temperaturas de la leche en cada estación (termómetro de nevera y anotación al cargar, al '
               'montar y a mitad de servicio) [sobrevive con ajuste: B y E]'),
        ('', 'montar el espacio en la commissary: estanterías, etiquetado, FIFO [sobrevive]'),
        ('BE', 'evento de prueba completo: las dos estaciones a tope con una cola simulada; cuenta bebidas por hora y '
               'barista, café, leche y vasos usados, para afinar la calculadora [sobrevive con ajuste: B y E]'),
    ]),
    ('F4 - Personal', [
        ('BE', 'plan de baristas por evento: 1 barista por 50-65 bebidas por hora; 2 + 2 ≈ 100 bebidas por hora; 2-3 '
               'baristas para ~250 invitados (Flashquotes) [sobrevive con ajuste: B y E]'),
        ('E', 'pool de event baristas en nómina W-2 por horas (nunca 1099 ni «freelance») [sobrevive con ajuste: E]'),
        ('', 'offer letters, I-9 y W-4; salario mínimo estatal [sobrevive]'),
        ('', 'new-hire reporting al estado [sobrevive]'),
        ('', 'proveedor de nóminas y workers\' comp en marcha [sobrevive]'),
        ('E', 'política de service charge, gratuity y tip jar (solo si el anfitrión lo acepta; las propinas son del '
              'equipo) [sobrevive con ajuste: E]'),
        ('', 'food handler cards de todo el equipo [sobrevive]'),
        ('BE', 'seguridad del barista: quemaduras de vapor y agua caliente, repostar el generador en frío y lejos de los '
               'invitados, cables y tropiezos, regletas con GFCI [sobrevive con ajuste: B y E]'),
        ('BE', 'OSHA basics: quemaduras, levantar el carro y las máquinas entre dos y por la rampa, arrastrar el remolque, '
               'suelos mojados [sobrevive con ajuste: B y E]'),
        ('BE', 'protocolo de servicio del barista: carta, estándares (doble de 18 g (0.63 oz) a 36 g, leche de 8 oz), latte '
               'art, saludo, gestión de la cola, alérgenos (leche, soja, frutos de cáscara; trigo y huevo en la bollería; '
               'la avena solo «certified gluten-free» si lo está) [sobrevive con ajuste: B y E]'),
    ]),
    ('F5 - Marketing', [
        ('BE', 'marca, logo, una carta corta (clásicos de espresso, signature y seasonal drinks, cold brew, chai, hot '
               'chocolate, avena incluida) y fotos del carro en eventos reales [sobrevive con ajuste: B y E]'),
        ('', 'web con paquetes, precios «desde» y formulario [sobrevive]'),
        ('', 'Google Business Profile y reseñas [sobrevive]'),
        ('', 'The Knot, WeddingWire y Zola [sobrevive]'),
        ('BE', 'GigSalad, Thumbtack y The Bash para fiestas privadas: comisión o coste por lead dentro del precio; mide el '
               'coste por reserva [sobrevive con ajuste: B y E]'),
        ('', 'política de degustaciones [sobrevive]'),
        ('E', 'plantilla de presupuesto con la calculadora del kit (coste por bebida, precio por invitado y por hora, '
              'baristas y potencia) + CRM [sobrevive con ajuste: E]'),
        ('E', 'prospección B2B: office managers, HR, event planners y coworkings; ofrece una hora de barra gratis en un '
              'open house; el 69.3 % de las reservas son corporativas entre semana (Flashquotes) [sobrevive con ajuste: E]'),
        ('BE', 'Instagram y redes con latte art y el carro en eventos (con permiso del cliente); seguimiento por texto / '
               'SMS [sobrevive con ajuste: B y E]'),
        ('', 'salas y wedding planners (preferred vendor lists) [sobrevive]'),
        ('', 'referidos y reseñas [sobrevive]'),
        ('E', 'open house corporativo de lanzamiento con barra de café para planners, salas y empresas + el primer bridal '
              'show local [sobrevive con ajuste: E]'),
    ]),
    ('F6 - 90 Días', [
        ('E', 'llamada final 3 semanas antes: invitados, horas de servicio, carta y leches, alergias, enchufe; recuento '
              'final 10 días antes [sobrevive con ajuste: E]'),
        ('BE', 'comprobación de la sala 2 semanas antes: 110V o 220V, amperios y distancia al enchufe, suelo nivelado, '
               'interior o exterior, acceso y ascensor para el carro, aparcamiento del remolque, normas de la sala por '
               'escrito [sobrevive con ajuste: B y E]'),
        ('', 'saldo antes del evento y extras en 48 h [sobrevive]'),
        ('BDE', 'pedidos: café (tueste de 1-3 semanas) y leches con margen, vasos; cold brew (12-24 h) y siropes la víspera '
                'en la commissary; D = «1 week out, then the day before» [sobrevive con ajuste: B, D y E]'),
        ('BE', 'carga del remolque con la lista: carro y barra sujetos, máquinas, molinos, cables y generador, leche en '
               'coolers a 41 °F (5 °C) o menos, depósitos llenos en la commissary, vasos; anota la temperatura de la leche '
               '[sobrevive con ajuste: B y E]'),
        ('BE', 'llegar 1-1.5 h antes: lavamanos primero, montaje ~1 h, calentar las máquinas y ajustar la molienda, servir '
               'en la service window; cuenta las bebidas servidas [sobrevive con ajuste: B y E]'),
        ('BE', 'recogida: backflush y limpieza de máquinas, lancetas y molinos; aguas grises solo en la commissary; la leche '
               'abierta que pasó tiempo fuera de temperatura, a la basura [sobrevive con ajuste: B y E]'),
        ('', 'pedir reseña y fotos; CRM [sobrevive]'),
        ('BE', 'revisión semanal: bebidas por invitado, bebidas por hora y barista, café y leche usados, coste por bebida y '
               'horas por evento frente a la calculadora [sobrevive con ajuste: B y E]'),
        ('', 'revisión a los 90 días: precio por invitado, mínimos y paquetes [sobrevive]'),
    ]),
])
COLS_CAMBIAN = OrderedDict()
for _h, _ts in TAREAS_COF.items():
    for _k, (_cols, _t) in enumerate(_ts):
        COLS_CAMBIAN[(_h, 5 + _k)] = _cols
        for _col in 'BCDE':
            CELDA_PISTAS[('COFC', _h, '%s%d' % (_col, 5 + _k))] = _CK + 'fase %s, tarea %d/%d: %s' % (
                _h[1], _k + 1, len(_ts), _t)

# Pistas por TEXTO propias del café (se suman a las de extraer_textos.PISTAS)
PISTAS_EXTRA = [
    (r'^Días fuera de rango$|^Los días van de 1 a 365', 'D221: esta validación cubre a la vez B6 (INVITADOS por evento), '
                                                         'B58/B59 (días de cobro y de pago) y los invitados de '
                                                         'Escenarios: un texto que valga para todos'),
    (r'[Cc]lientes?|[Tt]icket|[Dd]ías de apertura|al día|por día',
     'D221: motor de eventos: «events per year» (B4), «price per guest» (B5), «guests per event» (B6); nunca «customers», '
     '«per day» ni «operating days» (gate)'),
    (r'[Vv]ehícul|[Ff]ood ?[Tt]ruck|[Cc]amión|[Rr]emolque', 'D219/D222: el espresso cart y el portable espresso bar viajan '
                                                            'en un remolque cerrado que arrastra el vehículo del dueño; '
                                                            '«coffee truck» solo como FORMATO; nunca «truck» suelto'),
    (r'[Vv]entanilla', 'D219: no hay ventanilla: barra de espresso en el evento; «service window» = horas contratadas'),
    (r'[Ff]estival|[Mm]ercados|[Aa]mbulante|[Cc]alle', 'D224: festivales y farmers markets guest-pay SÍ (complemento, con '
                                                        'temporary event permit y, a menudo, minimum sales guarantee); '
                                                        'nunca venta callejera diaria (eso es el Food Truck Kit)'),
    (r'[Aa]parcamiento|base del vehículo|comisar', 'Glosario: «commissary, cart storage & trailer parking»; nunca «support '
                                                   'kitchen»'),
    (r'[Gg]enerador|gas\b|propano', 'D223: el combustible del generador va en suministros (= FT); el del vehículo, fijo '
                                    '(fila 27); el caso no cocina con propano'),
    (r'[Dd]elivery|[Gg]lovo|[Uu]ber', 'D224: el canal es FESTIVALES Y FARMERS MARKETS guest-pay con cuota del '
                                      'organizador, no apps de delivery ni marketplaces'),
    (r'[Cc]omida|[Cc]ocina|[Mm]enú|COMIDA', 'D219/D223: coffee bar packages y add-ons; «menu» vale; nunca «chef», «plated» '
                                            'ni «buffet» (gate)'),
    (r'm²|m2\b|\bkg\b|\bkm\b|[Ll]itros?\b|\b\d+ ?L\b|\bml\b|°C|ºC', REGLA_UNIDADES),
    (r'[Ee]ventos?|[Bb]odas?', 'Glosario §9: coffee catering, coffee cart, mobile espresso bar, full-service espresso bar, '
                               'self-serve coffee station, hosted / guest-pay, service window, corporate events, weddings, '
                               'brand activations, trade shows'),
]

# Glosario de research §9 (OBLIGATORIO: regla de jerga §0), entero. Se suma al de FT/CAF y al del financial-kit
GLOSARIO_COF = OrderedDict([
    ('cafetería móvil para eventos (nombre)', 'coffee cart (nombre, slug, H1, ficheros) · coffee catering y mobile espresso '
                                              'bar (subtítulo y cuerpo) · coffee truck / coffee trailer solo como FORMATO; '
                                              'NUNCA «mobile cafeteria» (cafeteria = comedor) ni «mobile café»'),
    ('servicio de café para eventos', 'coffee catering · coffee cart catering'),
    ('barra con baristas · estación sin barista', 'full-service espresso bar · self-serve coffee station / drop-off (cold '
                                                  'brew)'),
    ('carro · remolque · camión · bici · furgoneta', 'espresso cart / coffee cart · coffee trailer · coffee truck · coffee '
                                                     'bike · coffee van'),
    ('barra portátil · barista jefe · de evento', 'portable espresso bar · lead barista · event barista'),
    ('bebidas sin límite', '«unlimited made-to-order espresso drinks during your booked service window»'),
    ('horas de servicio · hora extra · tarifa base', 'service hours / service window · additional hour / extra time · base '
                                                     'fee + hourly rate'),
    ('precio por invitado · paquete', 'per person (pp) / per guest · package («100 Guest Package»)'),
    ('paga el anfitrión · pagan los invitados · mínimo', 'hosted («host-paid, all-inclusive») · guest-pay / pop-up · '
                                                         'minimum sales guarantee'),
    ('leche vegetal', 'alt milk / plant-based milk · oat milk («additional alternative milk», o incluida)'),
    ('filtro por lotes · frío · nitro', 'batch brew · drip coffee · cold brew · nitro cold brew'),
    ('bebida de autor · temporada · siropes caseros', 'signature drinks · seasonal drinks · house-made syrups'),
    ('vasos personalizados · activación de marca', 'branded cups · custom cup sleeves · latte printing / latte logo '
                                                   'printing · brand activation · trade show'),
    ('montaje, servicio y desmontaje', 'setup, service & breakdown · load-in'),
    ('enchufe · circuito propio · sin toma de agua', 'standard 110V outlet · dedicated circuit · «No plumbing connection is '
                                                     'required» (self-contained)'),
    ('ajustar molienda · sacar un café · doble', 'dial in · pull a shot · double shot (18 g in / 36 g out)'),
    ('capacidad · consumo', 'drinks per hour (50-65 por barista) · drinks per guest'),
    ('escandallo de bebida', 'cost per drink («all-in cost per drink») · COGS % (NUNCA «escandallo» ni «recipe costing»)'),
    ('señal · saldo · recuento final · desplazamiento', 'retainer (30-50 %) · balance due 14 days before · final guest '
                                                        'count · travel fee ($/mile, free radius)'),
    ('tasa de cierre', 'booking rate (quotes → bookings)'),
    ('cocina base · permiso · revisión de planos', 'commissary (+ agreement, log) · mobile food unit / facility permit · '
                                                   'plan review'),
    ('manipulador · seguro y certificado', 'food handler card · CFPM · general liability $1M/$2M · COI · additional insured'),
    ('vasos compostables', 'compostable cups (single-use, onsite)'),
    # (e) no se traducen literalmente
    ('cafetería móvil', 'coffee cart / mobile espresso bar (nunca «mobile cafeteria»)'),
    ('café de especialidad', 'specialty coffee'), ('barra de café', 'espresso bar / coffee bar'),
    ('carrito', 'cart'), ('tueste / tostador', 'roast / roaster'), ('leche de avena', 'oat milk'),
    ('feria', 'festival / farmers market / fair'), ('evento de empresa', 'corporate event'),
    ('barista autónomo / fijo discontinuo / freelance', 'W-2 event barista (hourly)'), ('IVA', 'sales tax'),
    ('licencia de actividad', 'business license'), ('registro sanitario', 'health permit + plan review'),
    ('señal', 'retainer / deposit'), ('manipulador', 'food handler'), ('bollería', 'pastries (from a licensed bakery)'),
    ('comida testigo', 'no aplica en EE. UU.'), ('canon de feria', 'organizer / vendor fee (booth fee)'),
    ('medidas (John, 13-oct)', 'US customary first, metric in parentheses: lb / oz (g), °F (°C), gallons / quarts '
                               '(liters), miles, sq ft (sq m); espresso dose in grams with its oz'),
])


# ==========================================================================
# Caso de ejemplo US (D220; research §8): celdas VERDES del FT. (corto, hoja ES, celda) → (valor, rótulo ES)
# ==========================================================================
def valores_cof(M):
    v = OrderedDict()
    sup = [
        ('B4', 170, 'Clientes/día'), ('B5', 12.60, 'Ticket medio'), ('B6', 95, 'Días de apertura'),
        ('B7', 0.10, 'Crecimiento de volumen del año 2'), ('B8', 0.06, 'Crecimiento de volumen del año 3'),
        ('B11', 0.85, 'Ventas de COMIDA'), ('B13', 0.12, 'Coste de mercancía sobre las ventas de COMIDA'),
        ('B14', 0.25, 'Coste de mercancía sobre las ventas de BEBIDA'), ('B15', 0.04, 'Consumibles'),
        ('B16', 0.05, 'Ventas por delivery'), ('B17', 0.15, 'Comisión de la plataforma'),
        ('B18', 0.03, 'Comisión de los medios de pago'), ('B20', 0.10, 'Seguridad Social'),
        ('B21', 12, 'Número de pagas'), ('B22', 15080, 'SMI anual'), ('B24', 700, 'Alquiler mensual'),
        ('B25', 1, 'Fianza'), ('B26', 100, 'Suministros'), ('B27', 3800, 'Seguros'), ('B28', 0.03, 'Varios'),
        ('B30', 30000, 'Recursos propios'), ('B31', M.CALIBRAR, 'Préstamo bancario'), ('B32', 0.10, 'Tipo de interés'),
        ('B33', 7, 'Plazo del préstamo'), ('B34', 0, 'Carencia'), ('B35', 3, 'Fondo de maniobra'),
        ('B37', 0.25, 'Impuesto de Sociedades, nueva'), ('B38', 0.25, 'Impuesto de Sociedades, tipo'),
        ('B39', 0.08, 'IVA repercutido de restauración'), ('B40', 0.08, 'IVA repercutido/soportado'),
        ('B41', 0, 'IVA soportado en compras'), ('B42', 0, 'Bases negativas'),
        ('B44', 7, 'Vida útil de obra'), ('B45', 5, 'Vida útil de maquinaria'), ('B48', 0, 'Subida anual'),
        ('B51', 350, 'Plazas de pie'), ('B52', 0.45, 'Actividad del mes 1'), ('B53', 9, 'Meses hasta alcanzar'),
        ('B54', 1, 'Meses de alquiler del aparcamiento'), ('B55', 0.10, 'Imprevistos sobre las partidas'),
        ('B58', 14, 'Días medios de cobro'), ('B59', 7, 'Días medios de pago'),
        ('B62', 0, 'Bebida ALCOHÓLICA'), ('B63', 0.08, 'IVA de la bebida ALCOHÓLICA'),
        ('B65', 1.15, 'DSCR mínimo'), ('B66', 1.25, 'DSCR objetivo'), ('B67', 0.15, 'Holgura mínima'),
        ('B68', None, 'Suelo salarial anual'),
    ]
    for c, val, rot in sup:
        v[('COFP', _S, c)] = (val, rot)
    # Inversión (D222; las bases de las fórmulas mandan): filas 7-20 (rótulos ES del FT) = $67,100
    for k, (val, rot) in enumerate([
            (13400, 'Vehículo'), (5400, 'Adaptación'), (15700, 'Equipamiento cocina'), (4800, 'Generador'),
            (6500, 'Instalación gas'), (1500, 'Depósito de agua'), (1500, 'Constitución'), (1400, 'Licencias'),
            (1100, 'Proyecto técnico'), (1000, 'TPV'), (3300, 'Menaje'), (1500, 'Stock'), (5000, 'Marketing'),
            (5000, 'Toldo')]):
        v[('COFP', _I, 'B%d' % (7 + k))] = (val, rot)
    # P&L: fijos B26-B35 (research §8: $21,000, con la fila libre repartida) y umbrales D225 [kit benchmark]
    for k, (val, rot) in enumerate([
            (1500, 'Permisos'), (3500, 'Mantenimiento'), (8000, 'Marketing'), (2400, 'Gestoría'), (1500, 'Software'),
            (600, 'Limpieza'), (900, 'Gestión de residuos'), (1800, 'Desinsectación'), (400, 'Prevención'),
            (400, 'Derechos de autor')]):
        v[('COFP', _P, 'B%d' % (26 + k))] = (val, rot)
    for c, val, rot in [('E51', 0.72, 'Margen bruto'), ('E53', 0.20, 'Coste de mercancía /'),
                        ('E54', 0.40, 'Coste de personal'), ('E55', 0.06, 'Aparcamiento'), ('E56', 0.05, 'Resultado neto')]:
        v[('COFP', _P, c)] = (val, rot)
    # Staffing (D223; research §8): personas (B), FTE por persona (C), bruto mes TOTAL de la fila (D) = $5,644/mes
    # (D = personas × FTE × 173.33 h × $/h: $22 · $20 · $19 · $19)
    for f, (b, c, d) in zip(range(5, 9), [(1, 1.0, 3813), (1, 0.3, 1040), (2, 0.08, 527), (1, 0.08, 264)]):
        for col, val in zip('BCD', (b, c, d)):
            v[('COFP', _R, '%s%d' % (col, f))] = (val, None)
    v.update([
        (('COFP', _R, 'B11'), (3000, 'Coste anual')), (('COFP', _R, 'B12'), (3000, 'Coste anual')),
        (('COFP', _R, 'B16'), (40, 'Jornada completa')), (('COFP', _R, 'B17'), (50, 'Semanas')),
        (('COFP', _R, 'B18'), (7, 'Horas de servicio')), (('COFP', _R, 'B19'), (1.6, 'Personas necesarias')),
    ])
    # Escenarios (research §8): −25 % / +25 % de eventos, −10 % / +10 % de precio e invitados
    v.update([
        (('COFP', _ES, 'B5'), (128, 'Clientes/día')), (('COFP', _ES, 'D5'), (212, 'Clientes/día')),
        (('COFP', _ES, 'B6'), (11.34, 'Ticket')), (('COFP', _ES, 'D6'), (13.86, 'Ticket')),
        (('COFP', _ES, 'B7'), (86, 'Días')), (('COFP', _ES, 'D7'), (105, 'Días')),
    ])
    # Estacionalidad (research §8 = Flashquotes, marzo 11.2 → 11.1 para sumar 100): apertura en MARZO → Month 1-12
    pesos = (0.111, 0.108, 0.109, 0.059, 0.038, 0.053, 0.073, 0.095, 0.079, 0.117, 0.070, 0.088)
    assert abs(sum(pesos) - 1.0) < 1e-9
    for col, val in zip('BCDEFGHIJKLM', pesos):
        v[('COFP', _T, '%s5' % col)] = (val, 'Estacionalidad')
    return v


# Calibración D15 (SPEC D220): holgura ≥ 15 %; si no, B4 de 10 en 10 hasta 190; si la caja mínima ≤ 0 en el valle de
# julio, B35 3 → 4 antes de tocar el precio. Cada celda, citada en F2-NOTAS §3 (G7). Se rellena con el dry-run del paso 1a
CALIBRACION_D15 = OrderedDict()


# ==========================================================================
# FORMULAS_EN: las del FT con la fila del Break-Even, las notas de las líneas de venta y las listas de la inversión
# ==========================================================================
_PE_COF = ('=IFERROR("With the average price per guest excl. sales tax above, you need "&TEXT(ROUNDUP(B15,0),"0")&" '
           'events a year at your average of "&TEXT(B11,"0")&" guests per event to avoid losing money (accounting '
           'break-even, depreciation included), and "&TEXT(ROUNDUP(B20,0),"0")&" for cash to hold (cash break-even: '
           'depreciation out, because it is not paid, and the year\'s loan payment in"&IF(B12=0,"; no principal is '
           'repaid this year (interest-only period or no loan)","")&"). The ""Revenue needed per year"" rows show the '
           'same figures in your currency.","")')
_C9_COF = ('=IFERROR("Price per guest excl. sales tax plus the weighted sales tax of your sales lines ("&TEXT('
           "SUMPRODUCT('3-Year P&L'!$E$10:$E$11,'3-Year P&L'!$G$10:$G$11)*100,\"0\")&\"%), rounded. In the US the "
           'quote adds sales tax on top, and many states tax the whole catering invoice (coffee service, baristas and '
           'add-ons; in some states, travel too); in the UK, VAT is included in the price.","")')
_F18_COF = ('=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$28,"0%")&" of sales: a cushion for unbudgeted event costs '
            '(extra milk, ice, cables, venue parking). It is a VARIABLE cost: it moves with the number of events, so '
            'it cannot sit in fixed costs (tow vehicle and trailer fuel, maintenance and registration are in row 27; '
            'generator fuel is in utilities)","")')
_F13_COF = ('=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$13,"0%")&" of COFFEE BAR PACKAGE sales (beans, milks, syrups '
            'and cold brew, with waste), not of total sales: add-ons have their own line","")')
_F14_COF = '=IFERROR("At "&TEXT(\'0. Assumptions\'!$B$14,"0%")&" of ADD-ON sales","")'


def formulas_cof():
    sys.path.insert(0, BP)
    import formulas_en as F                                                    # noqa: E402
    out = OrderedDict()
    for h, d in F._COMUNES.items():
        for c, f in d.items():
            out[('COFP', h, c)] = f
    out[('COFP', _S, 'C9')] = _C9_COF
    out[('COFP', _P, 'F18')] = _F18_COF
    out[('COFP', _P, 'F13')] = _F13_COF
    out[('COFP', _P, 'F14')] = _F14_COF
    o11 = out[('COFP', _T, 'O11')]
    assert 'Food and beverage purchases, consumables' in o11
    out[('COFP', _T, 'O11')] = o11.replace('Food and beverage purchases, consumables',
                                           'Coffee, milk and add-on purchases, compostable cups')
    out[('COFP', _E, 'A26')] = _PE_COF
    for c, f in F._inversion('D21', 'D22', 'D23', 'D25', 'D26', 'D28', 'D31', 'D32', 'D33', 24, 26, 31, 32,
                             'espresso cart, portable espresso bar, enclosed cargo trailer, trailer wrap and hitch, and '
                             'the mobile food unit plan review',
                             'LLC formation and legal, first-year permits and certifications, opening inventory, '
                             'website, photos and launch, the commissary deposit, pre-opening commissary rent and the '
                             'working capital reserve').items():
        out[('COFP', _I, c)] = (f.replace('when the lease ends', 'when the commissary agreement ends')
                                .replace(' of build-out and permits before opening', ' of plan review, test events and '
                                         'pre-sales before opening'))
    return out


def _importes_research():
    """Importes en dólares ≥ 10,000 que cita la research del café (carros, remolques, máquinas, caso…): son datos de
    este producto y no se vetan aunque coincidan con un importe de otro caso EN."""
    p = os.path.join(AQUI, 'F1-research-us-delta.md')
    t = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    out = {int(x.replace(',', '')) for x in re.findall(r'\$\s?(\d{1,3}(?:,\d{3})+)', t) if int(x.replace(',', '')) >= 10000}
    out |= {int(x) * 1000 for x in re.findall(r'\$\s?(\d{2,3})K\b', t)}
    return out


def cifras_prohibidas(valores):
    """CIFRAS_PROHIBIDAS del conjunto (D231): ES de la cafetería móvil (importe y frase) + caso de la Paella + casos EN del
    BBQ, catering, bar móvil y FT + vocabulario RX_COF_NO. Fuera las cifras que coinciden con un valor del propio caso."""
    propios = {int(round(x[0])) for x in valores.values() if isinstance(x[0], (int, float))}
    research = _importes_research()
    # del ES no se vetan los importes que la research del café cita ($5,000-25,000 por carro, $50,000 del Microloan…) ni
    # los múltiplos redondos de 5,000 hasta 50,000: en un texto US son plausibles por sí mismos (paso 1a)
    out = [(_num(n), 'cifra del ES de la cafetería móvil (D231)', None) for n in CIFRAS_ES
           if n not in propios and n not in research and not (n <= 50000 and n % 5000 == 0)]
    propios |= research                                 # solo para las listas de los otros casos EN
    out += [(rx, motivo, None) for rx, motivo in FRASES_ES]
    b4 = CALIBRACION_D15.get(('COFP', _S, 'B4'), (valores.get(('COFP', _S, 'B4'), (None,))[0],))[0]
    out += [(_num(n), 'cifra del caso de la Paella EN (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(PAEL, 'cifras_caso.json'), 'pael') if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_PAEL]
    out += [(_num(n), 'cifra del caso del BBQ EN (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(BBQ, 'cifras_caso.json'), 'bbq') if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_BBQ]
    out += [(_num(n), 'cifra del caso del catering EN publicado (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(CAT, 'cifras_caso.json'), 'cat') if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_CAT if not (b4 == 180 and '180' in rx)]
    out += [(_num(n), 'cifra del caso del mobile bar EN publicado (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(MBAR, 'cifras_caso.json'), 'mbar') if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_MBAR]
    out += [(_num(n), 'cifra del caso FT EN publicado (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(BP, 'cifras_caso.json'), 'ft') if n not in propios]
    out += RX_COF_NO
    return out


def completar(M):
    fijos = OrderedDict((k, v) for k, v in M.FIJOS.items() if k not in FIJOS_FUERA)
    fijos.update(FIJOS_NUEVOS)
    M.FIJOS = fijos
    M.POR_CELDA = POR_CELDA
    M.TOKENS_DOCX = tokens_cof(M.TOKENS_DOCX)
    M.PRODUCTOS_CIERRE = PRODUCTOS_CIERRE_COF
    M.DOCX_FIJOS = docx_fijos(M)
    M.DOCX_NOTAS = DOCX_NOTAS
    M.DOCX_NOTAS_PLAN = DOCX_NOTAS_PLAN
    M.FORMULAS_EN = formulas_cof()
    M.VALORES_EN = valores_cof(M)
    M.CALIBRACION_D15 = CALIBRACION_D15
    M.CELDA_PISTAS = CELDA_PISTAS
    M.PISTAS_EXTRA = PISTAS_EXTRA
    M.PISTA_D19 = PISTA_D19_GENERICA          # la pista D19 de verdad va por celda (filas 55-68); las tareas, también
    M.CIFRAS_PROHIBIDAS = cifras_prohibidas(M.VALORES_EN)
    M.RX_COF_NO = RX_COF_NO
    M.REGLA_UNIDADES = REGLA_UNIDADES
    glo = OrderedDict(M.GLOSARIO)
    for k in ('cliente/día', 'ticket medio sin IVA', 'PVP con IVA', 'aparcamiento y base del vehículo', 'venta ambulante'):
        glo.pop(k, None)                      # glosario del food truck que no vale aquí
    glo.update([('cliente/día → (motor)', 'events per year'), ('ticket medio sin IVA → (motor)',
                                                               'average price per guest (excl. sales tax, baristas '
                                                               'included)'),
                ('días de apertura → (motor)', 'average guests per event'),
                ('aparcamiento y base del vehículo', 'commissary, cart storage & trailer parking')])
    for k, val in GLOSARIO_COF.items():
        glo[k] = val                          # research §9 manda (regla de jerga §0)
    M.GLOSARIO = glo
