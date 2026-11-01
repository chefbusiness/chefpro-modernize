#!/usr/bin/env python3
"""
datos_bur.py — Burger Restaurant Business Plan Kit (EN) · los datos ES→EN que dependen del contenido: rótulos fijados
(inversión 18 filas, fijos 9, plantilla de 7 filas), POR_CELDA, pistas, tokens del docx, fijos y notas del docx, caso US
(research US §8 con Mes 1 = enero, F1-camino §6), cifras ES prohibidas y RX_BUR_NO (F1-camino §7) y glosario (US §9). Lo
llama `mapas_bur.instalar()` con el módulo `mapas` YA cargado con los datos de FT/CAF (FIJOS comunes del motor 2.2,
TOKENS_DOCX). Clon de `../business-plans-en-14/datos_sus.py` (Sushi Restaurant EN, LIVE el 31-oct: misma rejilla, rotación
encendida, `Break-Even!B25`, rótulos «Comensales…»). Sesión Claude Code, 31-oct-2026 (F2-EN).
"""
import json
import os
import re
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
PD = os.path.dirname(AQUI)
BP = os.path.join(PD, 'business-plans-en')
BP2 = os.path.join(PD, 'business-plans-en-2')
BAR = os.path.join(PD, 'business-plans-en-3')
PIZ = os.path.join(PD, 'business-plans-en-8')
ICE = os.path.join(PD, 'business-plans-en-10')
TAQ = os.path.join(PD, 'business-plans-en-12')
POL = os.path.join(PD, 'business-plans-en-13')
SUS = os.path.join(PD, 'business-plans-en-14')
HAMES = os.path.join(PD, 'plan-hamburgueseria')       # ES cerrado: F1-camino, research y cifras_caso_es.json

URL_BUR = 'aichef.pro/en/digital-products/burger-restaurant-business-plan'
CALC_EN = 'Smash Burger Patty, Fries & Costing Calculator'
_I, _S, _P, _R, _N, _E, _ES, _T = ('Inversión Inicial', '0. Supuestos', 'PyG 3 Años', 'Personal', 'Instrucciones',
                                   'Punto Equilibrio', 'Escenarios', 'Tesorería 12 meses')
REGLA_UNIDADES = ('MEDIDAS US (John, 13-oct): principales lb y oz, °F, gallons / quarts / fl oz y sq ft; la métrica entre '
                  'paréntesis para UK: «3 oz (85 g)», «155 °F (68 °C)», «41 °F (5 °C)», «1,700 sq ft (158 sq m)», «35 lb '
                  '(16 kg)»; nada de kg, g, km, litros ni °C como unidad principal (gate). NUNCA las temperaturas españolas '
                  'de la carne o de la fritura («70 °C 2 min», «75 °C», «175 °C», «−18 °C», «2 °C»): la regla US de la carne '
                  'picada es 155 °F (68 °C) durante 17 segundos (Food Code 3-401.11(A)(2)) y el frío 41 °F (5 °C) o menos')

# ==========================================================================
# FIJOS (por TEXTO ES, en cualquier celda de los 2 libros). Parten de los de FT/CAF (los del motor 2.2)
# ==========================================================================
FIJOS_FUERA = ('Este fichero forma parte del producto «plan-negocio-food-truck» de AI Chef Pro.',
               'Este fichero forma parte del producto «plan-negocio-cafeteria» de AI Chef Pro.')
_TITULO_CHECK = 'BURGER RESTAURANT STARTUP CHECKLIST'
FIJOS_NUEVOS = OrderedDict([
    # Instrucciones!A3 del checklist con el nombre comercial
    ('Este fichero forma parte del «Plan de Negocio: Hamburguesería Smash» de AI Chef Pro.',
     'This file is part of the Burger Restaurant Business Plan Kit by AI Chef Pro.'),
    # títulos: «burger restaurant» en el nombre, «smash burger» en descriptor y prosa; nunca «gourmet» ni «authentic» (US §9)
    ('CHECKLIST DE APERTURA — HAMBURGUESERÍA SMASH', _TITULO_CHECK),
    ('INSTRUCCIONES DE USO — Plan financiero Hamburguesería Smash',
     'HOW TO USE THIS WORKBOOK — Burger Restaurant Financial Projections'),
    ('PLAN DE NEGOCIO: HAMBURGUESERÍA SMASH', 'BURGER RESTAURANT BUSINESS PLAN: SMASH BURGERS, TAKE-OUT & DELIVERY'),
    ('Inversión inicial estimada — hamburguesería de smash burgers con sala, para llevar y a domicilio',
     'Estimated Startup Costs — smash burger restaurant with counter service, 44 seats, take-out and delivery'),
    ('Ajusta las cifras a tu proyecto: son las de un caso tipo en una ciudad media, sin traspaso. Pon tus presupuestos '
     'reales en las celdas de importe.', 'US kit example (2026) — replace with your own quotes.'),
    ('Escenario realista — hamburguesería de smash burgers con sala, para llevar y a domicilio',
     'Base case — smash burger restaurant: counter service, take-out and delivery'),
    ('Punto de equilibrio mensual y diario — hamburguesería de smash burgers con sala, para llevar y a domicilio',
     'Monthly and daily break-even — smash burger restaurant with counter service, take-out and delivery'),
    # cabecera de la tabla D19 y fases 2-3 del checklist con el nombre de su pestaña (US §9)
    ('DATOS DE REFERENCIA DEL SECTOR', 'US BURGER RESTAURANT BENCHMARKS (sourced) AND KIT ESTIMATES'),
    ('FASE 2: LOCAL, HUMOS, GAS Y LICENCIA (semanas 3-14)', 'PHASE 2: SITE, HOOD, GAS & PERMITS (weeks 3-14)'),
    ('FASE 3: CARNE, FRITURA Y REGISTRO SANITARIO (semanas 6-14)', 'PHASE 3: BEEF, FRYERS & HEALTH PERMIT (weeks 6-14)'),
    # Inversión, filas 7-24: las 18 partidas de F1-camino §6 en las 18 filas con la CLASE de la fila ES: 7-11 obra (base de
    # imprevistos), 12-21 equipo, 22-24 sin amortizar. El hood va partido como en el ES: el conducto a cubierta con el
    # makeup air en la obra (9) y la campana Type I con la supresión UL 300 en el equipo (14)
    ('Proyecto técnico de actividad y de extracción, y dirección de obra',
     'Architect, MEP & hood drawings, plan review & permit fees'),
    ('Obra del local con mostrador de pedidos y cocina a la vista, rótulo y fachada',
     'Build-out (second-generation space, 1,700 sq ft) with order counter, signage & facade'),
    ('Conducto de extracción exclusivo hasta cubierta', 'Hood exhaust duct to the roof & makeup air'),
    ('Instalación eléctrica, cuadro y boletín', 'Electrical service, panel & HVAC'),
    ('Fontanería, separador de grasas, climatización e instalación de gas', 'Plumbing, gas lines & grease interceptor'),
    ('Plancha fry-top de acero a gas y tostador de pan',
     'Two 48" gas flat-tops, bun toaster, smash presses & scrapers'),
    ('Dos freidoras eléctricas de doble cuba y mantenedor de patatas', 'Three gas fryers with filtration & fry station'),
    ('Campana extractora con motor y filtros', 'Type I hood with UL 300 fire suppression'),
    ('Mesa refrigerada de montaje y bajo plancha refrigerado para las bolas',
     'Make-line unit, refrigerated chef base & cheese/holding station'),
    ('Frío: armario de carne, armarios de cocina, congelador de patatas y nevera de bebidas',
     'Walk-in cooler, reach-ins, freezer & ice machine'),
    ('Barra: batidora de batidos, arcón de helado, tirador de cerveza y botellero',
     'Shake machine, blenders & beverage station'),
    ('Lavavajillas de capota, fregaderos, lavamanos, mesas inox y estanterías',
     '3-comp sink, dish machine, hand sinks, shelving & stainless'),
    ('Utillaje: smashers, espátulas, básculas, sondas, medidor de compuestos polares y etiquetadora',
     'Smallwares (portion scale, ball portioner, probe thermometers, TPM tester, labels, to-go station)'),
    ('Mobiliario de sala, barra de ventana y mostrador', 'Furniture & seating (44 seats) and order counter'),
    ('TPV con Veri*factu, pantalla de turnos, datáfono, impresora de comandas e integrador de plataformas',
     'POS, self-order kiosk, KDS, online ordering & delivery tablets'),
    ('Constitución de la SL, licencia, tasas, registro sanitario y APPCC',
     'LLC, legal, licenses, food safety plan & pre-opening training'),
    ('Marca, web, fotos y vídeo de lanzamiento', 'Branding, website, photos & launch video'),
    ('Stock inicial: carne, pan, patatas, aceite, salsas, envases y bebida',
     'Opening inventory (beef, buns, cheese, fries, oil, disposables, beverage)'),
    # P&L (A10, A11, A25, fijos A26-A34 salvo marketing, que es GM). Fijos 9 = 9 ($26,000, F1-camino §6, fila ES de la
    # misma función): las renovaciones de permisos (CFPM, food handler cards) van con la formación (fila 34 ES de PRL)
    ('Ventas de hamburguesas y cocina (sala, para llevar y a domicilio)',
     'Food sales (burgers, chicken, fries & sides: dine-in, take-out & delivery)'),
    ('Ventas de bebida (refrescos, cerveza, batidos y agua)', 'Beverage sales (soft drinks, shakes & beer)'),
    ('Seguros (RC + multirriesgo)', 'Insurance (general + liquor liability + property + workers\' comp)'),
    ('Gestoría laboral, fiscal y contable', 'Accounting & bookkeeping'),
    ('Mantenimiento de la campana extractora y el conducto, la plancha y el gas, las freidoras y el frío',
     'Maintenance (quarterly hood cleaning, fryers, flat-tops, refrigeration)'),
    ('Software, TPV, integrador de plataformas, teléfono e internet', 'Software, POS, kiosk & online ordering'),
    ('Limpieza, lavandería, EPI y análisis de autocontrol', 'Cleaning, linens & uniforms'),
    ('Gestión de residuos y del aceite usado de las freidoras', 'Waste, grease & used-oil pickup'),
    ('Desinsectación, desratización y desinfección (DDD)', 'Pest control'),
    ('Derechos de autor por música ambiental (SGAE y AGEDI-AIE)', 'Music licensing (ASCAP/BMI/SESAC)'),
    ('Prevención de riesgos laborales, vigilancia de la salud y formación',
     'Training & permit renewals (CFPM, food handler cards, allergens, OSHA)'),
    # puestos de Staffing (A5:A11): counter service, sin servers ni propinas modeladas (US §8). Cada puesto en la fila ES
    # de su jornada (F1-camino §6): titular (1.0) → Owner / GM; plancha (1.0) → grill cooks (2 × 1.0); montaje y freidora
    # (1.0) → fry & prep cook; encargado de mostrador (1.0) → shift lead; auxiliar (0.75) → counter crew (3 × 0.75);
    # refuerzo de fin de semana (0.5) → weekend crew (3 × 0.4); suplencias → dish & prep (1 × 0.6)
    ('Titular — gerente y jefe/a de plancha: compra de la carne, carta y gestión', 'Owner / GM'),
    ('Cocinero/a de plancha: smash, costra y tiempos', 'Grill cooks (smash station)'),
    ('Cocinero/a de montaje y freidora', 'Fry & prep cook'),
    ('Encargado/a de mostrador y pedidos', 'Shift lead'),
    ('Auxiliar de sala y empaquetado', 'Counter crew (cashier, expo, to-go packing)'),
    ('Refuerzo de viernes a domingo: segunda plancha y empaquetado', 'Weekend crew (part-time W-2)'),
    ('Suplencias de vacaciones y descansos', 'Dish & prep'),
])

# Mismo ES con otro EN en ESTA celda (lección de BP2 §4.1: los arreglos de un libro no se heredan a ciegas)
POR_CELDA = OrderedDict([
    # E5: la columna H de la línea de bebida = parte gravada al tipo del alcohol de B40 (= Pizza, Taco y Sushi EN)
    (('BURP', _P, 'H4'), 'Beverage share taxed at the alcohol rate in B40 (%)'),
    (('BURP', _P, 'F11'), 'Dine-in beverages and the drinks that go out with orders (soft drinks, shakes and beer) · '
                          'Column H is the share of beverage sales taxed at the alcohol rate in "0. Assumptions" B40. '
                          'With the example rates (B39 = B40 = 8%: state + local) it changes nothing. Some states tax '
                          'alcohol differently: type your alcohol rate in B40 and the alcohol share of beverage sales '
                          'here'),
    (('BURP', _S, 'A62'), 'Alcohol share of beverage purchases (reference only: no input credit in the US)'),
    (('BURP', _S, 'C62'), 'Reference only: in the US the sales tax you pay on purchases is a cost, not a credit (B41 = 0%), '
                          'so this share moves no figure in the workbook. The sales tax you COLLECT on beverages is set '
                          'by the beverage line of the P&L (column H)'),
    (('BURP', _S, 'C63'), 'NO EFFECT in this workbook: the sales tax collected on beverages is set by the beverage line of '
                          'the P&L. With the example, beer, soft drinks, shakes and food all pay the same 8% (state + '
                          'local); if your state taxes alcohol at another rate, type it in B40 and the alcohol share in '
                          'column H of that line'),
    # Mes 1 = ENERO con los pesos de US §8 en el orden del calendario (VALORES_EN B5:M5), no los del ES
    (('BURP', _T, 'O5'), 'Month 1 = JANUARY, in calendar order: February is the slowest month, with January and November '
                         'close behind; May (National Burger Month and graduations), June, July and August are the peaks. '
                         'Kit weights for a mid-size US city: replace them with your area\'s pattern; if you open in another '
                         'month, rotate the row. It must add up to 100%'),
    # E4: la nota de Staffing con counter service (US §8): sin servers ni tip credit
    (('BURP', _R, 'A29'), 'The gross pay, employer payroll taxes, monthly cost and annual cost columns are TOTALS for the '
                          'row: for a position with several people they include all of them. "FTE" is the share of a '
                          'full-time week and is used to compare pay with the legal floor pro rata. The payroll tax rate '
                          'and the number of pay periods are in the "0. Assumptions" tab. Tips are not modeled: with '
                          'counter service there are no servers, every position is budgeted at a base wage of at least '
                          '$15/h, and any tips from a tip jar or the POS belong to the crew, never to the owner or '
                          'managers'),
])


# ==========================================================================
# Cifras prohibidas (F1-camino §7): ES de la hamburguesería (importe y frase), casos EN publicados y RX_BUR_NO.
# Formato: (regex, motivo, excepción sobre el texto entero)
# ==========================================================================
def _num(n):
    """131000 → patrón que casa 131,000 · 131.000 · 131 000 · 131000 (y nada pegado a más dígitos)."""
    s = str(n)
    cab, cola = s[:-3], s[-3:]
    return r'(?<![\d.,])' + cab + r'[.,   ]?' + cola + r'(?![\d])'


def _cifras_es():
    """Importes ≥ 10.000 € del caso ES de la hamburguesería (`../plan-hamburgueseria/cifras_caso_es.json`, tokens con «€»:
    el ES está cerrado y manda). Los pequeños quedan cubiertos por la prohibición de «€»."""
    out = set()
    p = os.path.join(HAMES, 'cifras_caso_es.json')
    if not os.path.exists(p):
        return out
    for s in json.load(open(p, encoding='utf-8')).get('tokens', {}).values():
        if not isinstance(s, str) or '€' not in s:
            continue
        n = s.replace('€', '').replace('−', '-').replace(' ', '').replace(' ', '').strip()
        n = n.replace('.', '').replace(',', '.')
        try:
            x = float(n)
        except ValueError:
            continue
        if abs(x) >= 10000:
            out.add(int(round(abs(x))))
    return out


def _frases_es():
    return [
        (r'(?i)€|\bEUR\b', 'moneda ES'),
        # «195 covers» es el caso US: lookbehind contra el dígito (F1-camino §7)
        (r'(?i)(?<![\d.,])95 (?:covers|guests|customers|diners|orders)\b', 'caso ES (95 comensales/día)'),
        (r'(?i)\b36 (?:seats|covers)\b', 'caso ES (36 plazas)'),
        (r'(?i)(?:check|ticket)[^.;$]{0,20}(?<![\d$])16[.,]00\b|(?<![\d$])16[.,]00\s?(?:€|EUR|per (?:cover|guest|diner))',
         'ticket ES (16,00 €)'),
        (r'(?i)\b300 (?:opening )?days\b', 'días del ES (300; el caso US abre 360)'),
        (r'(?i)\b1[.,]7 (?:covers|guests|diners)\b', 'equivalencia del ES (1 pedido = 1,7; el caso US usa 1.6)'),
        (r'(?i)\b14 (?:pay periods|payments|paychecks|salaries|monthly)', 'pagas del ES (14 pagas)'),
        (r'(?i)(?:payroll|social security|employer)[^.;]{0,60}?\b33\s?%', 'Seguridad Social del ES (33 %)'),
        (r'(?i)\b33\s?%[^.;]{0,40}?(?:payroll|social security|employer)', 'Seguridad Social del ES (33 %)'),
        (r'\b17[.,]094\b', 'SMI ES (17.094 €)'),
        (r'\b1[.,]221\b', 'SMI ES (1.221 €)'),
        # la plataforma ES (F1-camino §7): 24 % de las ventas al 30 %; el caso US es el 19 % al 25 %
        (r'(?i)\b24 ?% of (?:total )?sales\b|\b24 ?% (?:through|via|by) (?:the )?(?:delivery|marketplace)',
         'plataforma ES (24 % de ventas: el caso US es el 19 %)'),
        (r'(?i)\bRD 1(?:021|086|26|420)\b|\bRD 919\b|\bart\. ?(?:4\.1|7\.[23]|30(?:\.5)?)\b|Ley 1/2025|Ley 7/2022|'
         r'Ley 37/1992|\bACSA\b|\bAESAN\b|Inf26008|Orden de 1989|Order of 26 January 1989|2017/2158|ROESB|RGSEAA',
         'norma ES (RD 1021/2022, RD 1086/2020, RD 919/2006, Orden de 1989, Rgto. 2017/2158, Inf26008, AESAN…)'),
        (r'\bv1\.[01]\b|\b[Vv]ersion 1\.[01]\b', 'historia de versiones (la EN nace en 2.2)'),
    ]


# casos EN publicados (frases). NO van «360 days» (Rotisserie EN) ni «$17.50» (Taco y Rotisserie EN): coinciden con el caso
# burger (360 días, optimista de $17.50, US §8)
FRASES_OTROS = [(r'(?i)\b62 covers\b', 'caso de la Pizza EN («62 covers»)'),
                (r'(?i)\b165 customers\b', 'caso de la Ice Cream EN («165 customers»)'),
                (r'(?i)\b210 transactions\b', 'caso de la Bakery EN («210 transactions»)'),
                (r'\$27(?:\.00)?\b(?![.,]\d)', 'caso del Bar EN («$27»)'),
                (r'(?i)\b308 (?:opening )?days\b', 'caso del Taco EN («308 days»)'),
                (r'(?i)\b130 covers\b', 'caso del Rotisserie EN («130 covers»)'),
                (r'(?i)\b115 covers\b', 'caso del Sushi y del Taco EN («115 covers»)'),
                (r'(?i)\b310 (?:opening )?days\b', 'caso del Sushi EN («310 days»)'),
                (r'\$32\.50\b', 'check del Sushi EN («$32.50»)'),
                (r'(?i)\b40 seats\b', 'caso del Sushi EN («40 seats»)'),
                (r'(?i)\b1,800 sq ft\b', 'caso del Sushi EN («1,800 sq ft»)')]

_NO = r"(?i)\b(?:no|not|never|cannot|can't|don't|do not|without|isn't|is not|rather than|instead of)\b"
RX_BUR_NO = [
    # restos del Sushi EN (F1-camino §7)
    (r'(?i)sushi|nigiri|sashimi|\bmaki\b|itamae|\bsake\b|raw fish|parasit|omakase|\bnori\b|wasabi|imitation crab|'
     r'\bpoke\b|tempura|gyoza|teriyaki|rice cookers?',
     'Sushi EN («sushi / nigiri / sake / raw fish / parasite / tempura…»)', None),
    (r'(?i)\brolls?\b', 'Sushi EN («roll»: en la hamburguesería, «bun»)', r"(?i)potato rolls?|Martin's"),
    (r'(?i)\bplatters?\b', 'Sushi EN («platter»: en la hamburguesería, «combo» o «party pack»)', None),
    # restos del Taco EN y del Rotisserie EN
    (r'(?i)\btacos?\b|\btaquer', 'Taco EN («taco / taqueria»)', None),
    (r'(?i)trompo|al pastor', 'Taco EN («trompo / al pastor»)', None),
    (r'(?i)tortilla|masa harina', 'Taco EN («tortilla / masa harina»)', None),
    (r'(?i)salsa bar', 'Taco EN («salsa bar»)', None),
    (r'(?i)\bmezcal|\btequila', 'Taco EN / ES («mezcal / tequila»: el caso US es beer)', r'(?i)liquor license|full liquor'),
    (r'(?i)rotisserie|pollo a la brasa|\bspits?\b|family meals?|heated display|\byuca\b|huancaina|Inca Kola',
     'Rotisserie EN («rotisserie / spit / family meal / yuca»)', None),
    # restos de la Pizza EN y del Bar EN
    (r'(?i)\bpizz', 'Pizza EN («pizza»)', None),
    (r'(?i)Neapolitan|\bdough\b', 'Pizza EN («Neapolitan / dough»)', None),
    (r'\bVPN\b|\bAVPN\b', 'Pizza EN («VPN»)', None),
    (r'(?i)Margherita|mozzarella|San Marzano', 'Pizza EN (ingredientes)', None),
    (r'(?i)\btapas\b|\bsmall plates\b', 'Bar EN («tapas / small plates»)', None),
    (r'(?i)\bcocktails?\b', 'Bar EN («cocktails»: la hamburguesería sirve beer)', None),
    (r'(?i)\bhappy hour\b|\blast call\b|\bbarbacks?\b|\bneighborhood bar\b', 'Bar EN', None),
    (r'(?i)\bspirits\b', 'Bar EN («spirits»: la hamburguesería sirve beer)', r'(?i)liquor license|full liquor|' + _NO[4:]),
    # restos del ES (F1-camino §7)
    (r'\bIVA\b', 'ES («IVA»)', None),
    (r'(?i)\bconvenio\b', 'ES («convenio»)', None),
    (r'\bSMI\b', 'ES («SMI»)', None),
    (r'(?i)\baut[oó]nomo', 'ES («autónomo»)', None),
    (r'Veri\*?factu', 'ES («Veri*factu»)', None),
    (r'\bSGAE\b', 'ES («SGAE»)', None),
    (r'\bIAE\b', 'ES («IAE»)', None),
    (r'(?i)\bterrazas?\b', 'ES («terraza»)', None),
    (r'(?i)\bcomensal|\bpedidos?\b|\bhamburgueser|\bbolas?\b|\bbatidos?\b|\bmen[uú] del d[ií]a',
     'ES («comensal / pedido / hamburguesería / bola / batido» → covers, orders, burger restaurant, ball, shake)', None),
    (r'(?i)fry[- ]?tops?', 'jerga ES («fry-top» → flat-top, US §9)', None),
    (r'(?i)\bvalue meals?\b', 'jerga («value meal» NO: «combo», US §9)', None),
    (r'(?i)\bsmashed burgers?\b', 'jerga («smash burger», nunca «smashed burger»; «smashed on the flat-top» sí)', None),
    (r'\bEspaña\b|\bSpain\b|\bSpanish\b', 'ES («España/Spain»: la corriente española no cruza)', None),
    (r'\bVAT\b', 'ES («VAT» fuera de la nota UK)', r'\bUK\b|United Kingdom|HMRC'),
    # temperaturas ES de la carne y de la fritura (F1-camino §7 y §9: «75 °C» es FALSO para España; el EN usa 155 °F 17 s).
    # La nota UK va sin cifras de cocción: sin excepción UK. Las conversiones del Food Code entre paréntesis sí valen
    (r'(?<![\d.,])75\s?°C|[−-]18\s?°C', 'temperaturas ES («75 °C», «−18 °C»)', None),
    (r'(?<![\d.,])70\s?°C', 'temperatura ES («70 °C 2 min» de la AESAN)', r'158\s?°F\s?\(70\s?°C\)'),
    (r'(?<![\d.,])175\s?°C', 'temperatura ES («175 °C» de la acrilamida, Rgto. 2017/2158)', None),
    (r'(?<![\d.,])63\s?°C', 'temperatura ES («63 °C»; en EE. UU. hot holding 135 °F)', r'145\s?°F\s?\(63\s?°C\)'),
    (r'(?<![\d.,−-])2\s?°C', 'temperatura ES («2 °C» de la carne picada; en EE. UU. 41 °F)', None),
    (r'(?i)\b25\s?%[^.;]{0,30}polar|polar[^.;]{0,40}\b25\s?%', 'límite ES de polares (25 %: sin límite federal en EE. UU.)',
     None),
    # jerga trampa y claims (US §6 y §9)
    (r'(?i)\bauthentic', 'claim («authentic»: US §9, nunca como promesa)', None),
    (r'(?i)\bgourmet\b', 'claim («gourmet»: solo la variante «gourmet burger bar» con servers)', r'(?i)gourmet burger bar'),
    (r'(?i)gluten[- ]free', 'claim («gluten-free»: US §6.9, ni del bun ni de las fries)',
     r"(?i)21 CFR|\bnot\b|\bnever\b|cannot|can't|don't|do not|\bno\b"),
    (r'(?i)medium[- ]rare|\brare\b|\bpink (?:in the )?(?:middle|center)',
     'cocción: el caso sirve todas las smash cocidas a 155 °F 17 s; poco hecha solo con consumer advisory (US §6.2)',
     r'(?i)consumer advisory|3-603\.11|3-401\.11\s?\(D\)|' + _NO[4:]),
    (r'(?i)(?:required|mandatory|must|have to|obligat)[^.;]{0,40}grind(?:ing)? logs?|grind(?:ing)? logs?[^.;]{0,30}'
     r'(?:are|is) (?:required|mandatory|compulsory)',
     'grinding logs: el kit no afirma que sean obligatorios (US §6.5)',
     r"(?i)whether|does not (?:say|claim)|doesn't (?:say|claim)|ask your|if (?:they|it) (?:are|is) required"),
    (r'(?i)\bservers?\b|table service', 'counter service sin servers (US §1); servers solo en la variante burger bar',
     r'(?i)burger bar|no servers|without servers|not .{0,25}servers|instead of servers|server-free'),
    (r'(?i)closed (?:on )?Mondays?|(?:six|6) days a week|open (?:six|6) days', 'el caso abre 7 días (360 días, US §8)',
     None),
    (r'(?i)\b(?:fish|seafood)[- ]grade', 'claim de otro negocio', None),
    # unidades (REGLA_UNIDADES): kg, g, km, litros, °C y m² solo entre paréntesis
    (r'(?i)\d\s?(?:kg|km|°C|liters?|litres?|ml)\b(?![^()]*\))', 'unidades: métrica solo entre paréntesis (REGLA_UNIDADES)',
     None),
    (r'(?<![\w.])\d+(?:[.,]\d+)?\s?g\b(?![^()]*\))', 'unidades: gramos solo entre paréntesis (REGLA_UNIDADES)', None),
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
    """Importes en dólares ≥ 10,000 que cita la research US de la hamburguesería: son datos de este producto y no se vetan
    aunque coincidan con un importe de otro caso EN."""
    out = set()
    p = os.path.join(AQUI, 'F1-research-us-delta.md')
    t = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    for m in re.finditer(r'\$\s?(\d{1,3}(?:,\d{3})+)(?:\s?[-–]\s?\$?(\d{1,3}(?:,\d{3})+))?', t):
        out |= {int(x.replace(',', '')) for x in m.groups() if x and int(x.replace(',', '')) >= 10000}
    out |= {int(x) * 1000 for x in re.findall(r'\$\s?(\d{2,3})K\b', t)}
    return out


# Datos federales US que coinciden con un importe del caso ES: no se vetan (el límite de los SBA Microloans, $50,000)
HECHOS_US = {50000}
# Constantes físicas que coinciden con un importe de otro caso EN: se vetan salvo en su contexto
EXCEPCION_CIFRA = {100000: r'(?i)\bBTU\b|\btherms?\b'}


def cifras_prohibidas(valores):
    """CIFRAS_PROHIBIDAS del conjunto. Fuera las cifras que coinciden con un valor del propio caso US o un dato federal."""
    propios = {int(round(x[0])) for x in valores.values() if isinstance(x[0], (int, float))} | HECHOS_US
    out = [(_num(n), 'cifra del caso ES de la hamburguesería', None) for n in sorted(_cifras_es()) if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in _frases_es()]
    propios |= _importes_research()
    for path, plan, nombre in [(os.path.join(SUS, 'cifras_caso.json'), 'sus', 'del Sushi EN'),
                               (os.path.join(POL, 'cifras_caso.json'), 'pol', 'del Rotisserie EN'),
                               (os.path.join(TAQ, 'cifras_caso.json'), 'taq', 'del Taco EN'),
                               (os.path.join(PIZ, 'cifras_caso.json'), 'piz', 'de la Pizza EN'),
                               (os.path.join(ICE, 'cifras_caso.json'), 'ice', 'de la Ice Cream EN'),
                               (os.path.join(BP2, 'cifras_caso.json'), 'pan', 'de la Bakery EN'),
                               (os.path.join(BAR, 'cifras_caso.json'), 'bar', 'del Bar EN'),
                               (os.path.join(BP, 'cifras_caso.json'), 'ft', 'del FT EN'),
                               (os.path.join(BP2, 'cifras_caso.json'), 'rest', 'del Restaurant EN')]:
        out += [(_num(n), 'cifra del caso %s (no se reutiliza)' % nombre, EXCEPCION_CIFRA.get(n))
                for n in _cifras_caso(path, plan) if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_OTROS]
    out += RX_BUR_NO
    return out


# ==========================================================================
# Tokens del docx: los de FT/CAF con los rótulos de la hamburguesería («Comensales…», = sushi bar) + partidas propias
# ==========================================================================
_CLIENTES = OrderedDict([
    ('Clientes/día (media del año 1)', 'Comensales/día (media del año 1)'),
    ('Clientes/día (media)', 'Comensales/día (media)'),
    ('Clientes/día', 'Comensales/día'),
    ('Clientes necesarios al día', 'Comensales necesarios al día'),
    ('Clientes necesarios al día (caja)', 'Comensales necesarios al día (caja)'),
])
_DESC = OrderedDict([
    ('clientes_dia', 'average covers per day, year 1: dine-in + take-out/pickup and delivery equivalents (1 order = 1.6 '
                     'covers)'),
    ('clientes_a2', 'average covers per day, year 2'),
    ('clientes_a3', 'average covers per day, year 3'),
    ('equilibrio_clientes_dia', 'break-even covers per day (accounting)'),
    ('equilibrio_caja_clientes_dia', 'cash break-even covers per day (loan payments in, depreciation out)'),
    ('pesimista_clientes', 'pessimistic scenario: covers per day'),
    ('optimista_clientes', 'optimistic scenario: covers per day'),
    ('alquiler_mes', 'rent per month (base rent of the premises)'),
    ('vida_obra', 'useful life of build-out, years'),
    ('ocupacion_anual', 'rent per year (occupancy)'),
    ('consumibles_pct', 'disposables (wrappers, burger boxes, fry cups, sauce cups, bags), % of sales'),
])
_FUERA = ('inv_vehiculo', 'inv_adaptacion', 'inv_equipo_cocina', 'inv_generador', 'inv_permisos', 'inv_espresso',
          'inv_obra', 'inv_instalaciones', 'inv_mobiliario', 'inv_barra', 'inv_terraza', 'inv_lanzamiento',
          'inv_stock', 'aforo', 'rotaciones_dia')


def _inv(rot, desc):
    return ('usd', ('fila', _I, {'bur': rot}, 'B'), desc)


def _como_excel(v, decimales):
    """Redondeo que se VE en Excel: 15 cifras significativas y luego mitad hacia arriba (no al par como `format`)."""
    from decimal import Decimal, ROUND_HALF_UP
    return float(Decimal('%.15g' % v).quantize(Decimal(1).scaleb(-decimales), rounding=ROUND_HALF_UP))


TOKENS_PROPIOS = OrderedDict([
    ('inv_proyecto', _inv('Proyecto técnico de actividad y de extracción, y dirección de obra',
                          'architect, MEP & hood drawings, plan review and permit fees')),
    ('inv_obra', _inv('Obra del local con mostrador de pedidos y cocina a la vista, rótulo y fachada',
                      'build-out of a second-generation space (1,700 sq ft) with the order counter, signage and facade')),
    ('inv_conducto', _inv('Conducto de extracción exclusivo hasta cubierta', 'hood exhaust duct to the roof and makeup air')),
    ('inv_instalaciones', _inv('Instalación eléctrica, cuadro y boletín', 'electrical service, panel and HVAC')),
    ('inv_fontaneria', _inv('Fontanería, separador de grasas, climatización e instalación de gas',
                            'plumbing, gas lines and grease interceptor')),
    ('inv_plancha', _inv('Plancha fry-top de acero a gas y tostador de pan',
                         'two 48" gas flat-tops, bun toaster, smash presses and scrapers')),
    ('inv_freidoras', _inv('Dos freidoras eléctricas de doble cuba y mantenedor de patatas',
                           'three gas fryers with filtration and the fry station')),
    ('inv_campana', _inv('Campana extractora con motor y filtros', 'Type I hood with UL 300 fire suppression')),
    ('inv_montaje', _inv('Mesa refrigerada de montaje y bajo plancha refrigerado para las bolas',
                         'make-line unit, refrigerated chef base and cheese/holding station')),
    ('inv_frio', _inv('Frío: armario de carne, armarios de cocina, congelador de patatas y nevera de bebidas',
                      'walk-in cooler, reach-ins, freezer and ice machine')),
    ('inv_batidos', _inv('Barra: batidora de batidos, arcón de helado, tirador de cerveza y botellero',
                         'shake machine, blenders and beverage station')),
    ('inv_lavado', _inv('Lavavajillas de capota, fregaderos, lavamanos, mesas inox y estanterías',
                        '3-compartment sink, dish machine, hand sinks, shelving and stainless')),
    ('inv_utillaje', _inv('Utillaje: smashers, espátulas, básculas, sondas, medidor de compuestos polares y etiquetadora',
                          'smallwares (portion scale, ball portioner, probe thermometers, TPM tester, labels, to-go '
                          'station)')),
    ('inv_mobiliario', _inv('Mobiliario de sala, barra de ventana y mostrador',
                            'furniture and seating (44 seats) and the order counter')),
    ('inv_tpv', _inv('TPV con Veri*factu, pantalla de turnos, datáfono, impresora de comandas e integrador de plataformas',
                     'POS, self-order kiosk, KDS, online ordering and delivery tablets')),
    ('inv_constitucion', _inv('Constitución de la SL, licencia, tasas, registro sanitario y APPCC',
                              'LLC, legal, licenses, food safety plan and pre-opening training')),
    ('inv_lanzamiento', _inv('Marca, web, fotos y vídeo de lanzamiento', 'branding, website, photos and launch video')),
    ('inv_stock', _inv('Stock inicial: carne, pan, patatas, aceite, salsas, envases y bebida', 'opening inventory')),
    ('aforo', ('int', ('fila', _S, {'bur': 'Aforo del local (plazas sentadas, con la barra de ventana)'}, 'B'),
               'seats (tables and a window counter; counter service)')),
    ('rotaciones_dia', ('dec1', ('fila', _S, {'bur': 'Rotaciones al día implícitas (calculado)'}, 'B'),
                        'implied seat turns per day (take-out and delivery covers included)')),
    ('comida_pct', ('pct0', ('fila', _S, {'bur': 'Ventas de COMIDA sobre el total'}, 'B'), 'food share of sales')),
    ('bebida_pct', ('pct0', ('fila', _S, {'bur': 'Ventas de BEBIDA sobre el total'}, 'B'), 'beverage share of sales')),
    ('plataforma_pct', ('pct0', ('fila', _S, {'bur': 'Ventas por delivery sobre el total'}, 'B'),
                        'share of sales through third-party delivery marketplaces')),
    ('comision_pct', ('pct0', ('fila', _S, {'bur': 'Comisión de la plataforma de delivery'}, 'B'),
                      'marketplace commission on those orders')),
    ('marketing_anual', ('usd', ('fila', _P, {'bur': 'Marketing y publicidad'}, 'B'), 'marketing budget per year')),
    ('prime_cost_pct', ('pct1', ('deriv', lambda c: c['cogs_pct'] + c['personal_pct']),
                        'prime cost year 1 (cost of goods + labor, % of sales)')),
    ('meses_alquiler_previo', ('int', ('fila', _S, {'bur': 'Meses de alquiler ANTES de abrir (obra y licencias)'}, 'B'),
                               'months of rent paid before opening (build-out and permits)')),
    ('costes_variables_pct', ('pct1', ('deriv', lambda c: 1 - c['margen_bruto_pct']),
                              'all variable costs year 1 (cost of goods + disposables + marketplace + card fees + '
                              'contingency), % of sales')),
    ('otros_variables_pct', ('pct1', ('deriv', lambda c: 1 - c['margen_bruto_pct'] - c['cogs_pct']),
                             'disposables + marketplace + card fees + contingency, % of sales')),
    ('pesimista_perdida', ('usd', ('deriv', lambda c: -c['pesimista_resultado']),
                           'pessimistic scenario: pre-tax LOSS as a positive amount (only if it is a loss)')),
    # Taco EN, revisión F2 (M5): `formatear` redondea al par y Excel muestra mitad arriba: el Word cita lo que se VE
    ('cogs_pct_xl', ('pct1', ('deriv', lambda c: _como_excel(c['cogs_pct'], 3)),
                     'cost of goods, % of sales, rounded as Excel shows it (P&L B52)')),
    ('plantilla_jornadas_xl', ('dec2', ('deriv', lambda c: _como_excel(c['plantilla_jornadas'], 2)),
                               'staff in FTE, rounded as Excel shows it (Staffing C12)')),
])


def tokens_bur(base):
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
            src = ('fila', hoja, {'bur': rot}, col)
        if t == 'consumibles_pct':
            fmt = 'pct1'
        out[t] = (fmt, src, _DESC.get(t, desc))
    out.update(TOKENS_PROPIOS)
    return out


# ==========================================================================
# Docx: lo que escribe ensamblar_docx.py (índices del Word ES de 131 párrafos = Sushi) y las notas por ranura
# ==========================================================================
# Productos del cierre: solo los que EXISTEN en la tienda EN (tienda.ts, 31-oct; lección M2 del Taco EN): el Burger Joint
# Checklists Kit Pro es el hermano de tareas (F1-camino §6)
PRODUCTOS_CIERRE_BUR = ['Burger Joint Checklists Kit Pro', 'Food Cost Kit Pro', 'HACCP Food Safety Kit Pro',
                        'Food Cost + Menu Engineering Guide']


def docx_fijos(M):
    pc = PRODUCTOS_CIERRE_BUR
    d = OrderedDict([
        (6, 'BUSINESS PLAN'), (7, 'Burger Restaurant'),
        (9, 'Complete financial plan, market analysis,\noperations strategy and startup checklist\nto open a smash burger '
            'restaurant with counter service, take-out and delivery in the United States'),
        (14, 'AI Chef Pro'), (15, 'aichef.pro'), (16, 'US edition with UK notes · 2026'),
        (18, 'LEGAL NOTICE'), (19, M.AVISO_DOCX_EN), (20, '© 2026 AI Chef Pro — aichef.pro'), (22, 'CONTENTS'),
        (35, 'Appendices: Burger Restaurant Financial Projections (Excel) + %s (Excel) + Burger Restaurant Startup '
             'Checklist (Excel) + Equivalents Guide' % CALC_EN),
        (123, 'AI Chef Pro'), (124, 'Templates and AI tools for food businesses'),
        (126, 'aichef.pro\ninfo@aichef.pro'),
        (127, '→ %s · %s' % tuple(pc[:2])), (128, '→ ' + pc[2]), (129, '→ ' + pc[3] + ' (cost per burger and menu mix)'),
        (130, '\n' + M.URL_TIENDA),
    ])
    return OrderedDict([('bur', d)])


DOCX_NOTAS_PLAN = OrderedDict([
    ('bur', 'Concepto (US §1): INDEPENDENT SMASH BURGER RESTAURANT (fast casual, COUNTER SERVICE) en una ciudad media de '
            'EE. UU. (150-500 mil hab.), ~1,700 sq ft, {{aforo}} plazas (mesas y una window counter), se pide en el '
            'counter o en el self-order kiosk y la comida sale en bandeja desde el expo: SIN servers y sin propinas '
            'modeladas; pickup propio (take-out) y marketplaces. Línea: smash burgers (balls de 3 oz aplastadas en el '
            'flat-top para la crust), single / double / triple, combos con fries, chicken sandwich, fries, shakes, soft '
            'drinks y beer (licencia como parámetro). Cocina: dos flat-tops de gas de 48", tres fryers de gas con '
            'filtrado bajo Type I hood + UL 300, walk-in y reach-ins a 41 °F. ABRE 7 DÍAS, 11:00-22:00 (23:00 viernes y '
            'sábado; 360 días: cierra Thanksgiving, Christmas Day, New Year\'s Day y 2 días de mantenimiento). El dueño '
            'es el GM. Nombre: «burger restaurant» en el título; «smash burger» en la prosa; «burger joint / burger '
            'shop» solo como sinónimo coloquial; NUNCA «gourmet» como promesa, «authentic», «smashed burger», «value '
            'meal» ni «fry-top». El ES llama «comensal» a la unidad; el EN dice «covers» (1 order = 1.6 covers). Cada '
            'cifra del caso va con su token {{…}}; las de mercado solo si están en la research con fuente. Lo ES que '
            'NO cruza (IVA partido, RD 1021/2022 y sus 2 °C, la picada del día, la carne madurada, AESAN y sus 70 °C, '
            'Rgto. 853/2004, el Rgto. 2017/2158 y sus 175 °C, los polares < 25 % de la Orden de 1989, RD 919/2006, la '
            'ordenanza de Madrid, IAE, convenio, SMI, 14 pagas, Leyes 1/2025 y 7/2022, Veri*factu, las franquicias '
            'españolas) se SUSTITUYE por US §6 o se quita. Variantes (texto, sin Excel): gourmet burger bar con servers '
            '(propinas aparte), ghost kitchen / delivery-only; fuera: franquicias y drive-thru (solo comparación de '
            'inversión), burger truck (→ Food Truck Business Plan Kit). No cites productos que no estén en el cierre. '
            'Honestidad del margen: neto {{margen_neto_a1}}. Glosario US §9 obligatorio. El cierre (productos) lo '
            'escribe el ensamblador. ' + REGLA_UNIDADES),
])

_FORMA = ('FORMA: la sección §%d del Sushi EN (business-plans-en-14/docx_en_sus_%s.json, el mismo esqueleto de párrafos) da '
          'el registro y la longitud; su vocabulario de sushi (sushi bar, nigiri, rolls, sake, raw fish, servers, closed '
          'Mondays…) y sus cifras NO valen')
_SEC = OrderedDict([
    (1, ('a', 'Resumen ejecutivo: concepto (US §1), la oportunidad (US §2: «smash burger» ≈ 673,000 búsquedas/mes y '
              '«burger restaurant» 110,000 = demanda de CONSUMO; «how to start a burger business» ≈ 20: no lo cites como '
              'mercado), inversión y financiación SOLO con tokens ({{inversion_total}}, {{capex}}, {{prestamo}} SBA 7(a) '
              '{{tipo_prestamo}} a {{plazo_prestamo}} años), ventas ({{ventas_a1}}, {{clientes_dia}} covers × {{ticket}} '
              '× {{dias}} días), neto {{margen_neto_a1}} y DSCR {{dscr_min}}')),
    (2, ('a', 'Concepto y propuesta: el formato elegido (smash burgers con counter service + take-out + delivery) frente a '
              'las variantes: gourmet burger bar con servers (más ticket, más personal, propinas aparte), ghost kitchen '
              '/ delivery-only (sin sala, todo marketplace) y burger truck (otro kit); la carta corta (single, double, '
              'triple, combo, chicken sandwich, fries, shakes); glosa smash burger, ball / puck / patty, flat-top, crust '
              'y lacy edges, smash press, potato bun y make line la primera vez; sin «authentic» ni «gourmet»')),
    (3, ('a', 'Mercado y competencia: US §2 y §5 (carta del caso: single $8.49 · double $10.99 · triple $13.49 · combo '
              '$15.99 · chicken sandwich $10.49 · fries $3.99-4.99 · shake $6.49, Kit estimate; Shake Shack como '
              'referencia de precio nacional solo con «secondary source»); las franquicias (Smashburger $1,239,500-'
              '$2,255,500 y Freddy\'s $785,936-$2,753,566 de Item 7, «reported by third-party franchise directories; '
              'check the FDD») como comparación de inversión, nunca como caso; el AI Overview de «$30,000 to $130,000» '
              'es de un pop-up sin hood; se compite en la crust, la velocidad y el precio del double; sin datos de '
              'mercado sin fuente')),
    (4, ('a', 'Cliente y posicionamiento: comida rápida de calidad para oficinas, familias, estudiantes y fines de semana; '
              'el check de {{ticket}} por cover equivalente (US §8: cover de sala ≈ $15.00 = comida $12.00 + bebida $3.00; '
              'take-out ≈ $28.00 por pedido y marketplace ≈ $32.00 con la carta un 15 % más cara; 1 pedido = 1.6 covers; '
              '≈ 107 de sala, ≈ 36 pedidos de take-out y ≈ 19 de marketplace al día); el pickup directo (0 % de comisión) '
              'frente a los marketplaces; sin propina (counter service)')),
    (5, ('a', 'Marketing y ventas: Google Business Profile, Yelp, Instagram y TikTok (el smash en la plancha vende en '
              'vídeo); fechas: National Burger Month (mayo), Super Bowl Sunday y March Madness (take-out de multi-packs), '
              'graduaciones y verano; marketplaces DoorDash / Uber Eats / Grubhub con sus tiers; el caso pone '
              '{{plataforma_pct}} de las ventas al {{comision_pct}}; la smash llega peor que otras comidas (la crust se '
              'ablanda en unos 15 minutos: fries en envase ventilado y carta del marketplace un 15 % más cara); el '
              'consumer advisory también en los listados de marketplace si ofreces cooked to order')),
    (6, ('b', 'Operaciones y equipo: dos flat-tops de 48" con bun toaster y smash presses ({{inv_plancha}}), tres fryers con '
              'filtrado ({{inv_freidoras}}), Type I hood + UL 300 ({{inv_campana}}) y el duct con makeup air '
              '({{inv_conducto}}), make line ({{inv_montaje}}), walk-in y reach-ins ({{inv_frio}}), shake machine '
              '({{inv_batidos}}); la apertura a las 8:30 (balls, cortes, salsas); «THE BALL IS THE BUSINESS» (US §8): cada '
              'onza cuenta, pesar las balls con báscula (nunca a ojo), no mezclar lotes en el flat-top, merma objetivo ≤ '
              '4 % de la carne comprada; carne comprada ya picada o en balls con el establishment number del proveedor; '
              'aceite filtrado cada noche y cambiado por TPM; mide la merma de plancha, las balls por lb y el coste por '
              'burger con la calculadora del kit (sin inventar cifras: las da la calculadora)')),
    (7, ('b', 'Organización y personal: Owner / GM, shift lead, grill cooks (2, smash station), fry & prep cook, counter '
              'crew (3 part-time W-2: cashier, expo, to-go packing), weekend crew (3 part-time W-2) y dish & prep '
              '({{plantilla_puestos}} personas = {{plantilla_jornadas_xl}} FTE); contrata al grill cook líder ANTES de '
              'la obra (diseña la línea); ≥ $15/h, counter service sin servers ni tip credit, las propinas del tip jar o '
              'del POS son del equipo; employer payroll taxes {{cargas_pct}}; el dueño se paga por debajo de un manager '
              'de cadena: «owner\'s draw in addition from net profit»')),
    (8, ('b', 'Plan financiero: TODO con tokens (ventas años 1-3, mezcla {{comida_pct}}/{{bebida_pct}}, COGS '
              '{{cogs_pct_xl}}, personal {{personal_pct}}, prime cost {{prime_cost_pct}}, alquiler {{ocupacion_pct}}, '
              'EBITDA, neto, equilibrio {{equilibrio_clientes_dia}} / {{equilibrio_caja_clientes_dia}} covers/día, holgura '
              '{{holgura_caja_pct}}, DSCR {{dscr_min}}, saldo mínimo {{saldo_minimo}}, escenarios); el food cost del plan '
              'es el consumo real de TODA la carta con la merma, los comps, el pollo, el bacon y los shakes: el coste '
              'teórico por burger de la calculadora sale más bajo (el puente, con las cifras de la calculadora que diga '
              'cifras_calculadora.md o sin cifra); el precio de la carne es el riesgo del caso: +$0.75/lb ≈ +$0.28 por '
              'double; revisar el precio cada 4 semanas')),
    (9, ('b', 'Marco legal US (ver las notas propias de cada ranura de §9)')),
    (10, ('b', 'Hoja de ruta: el orden del checklist (80 tareas en 6 fases: setup; hood & permits; beef & health; staff & '
               'allergens; menu, brand & delivery; opening & 90 days); decide ANTES de abrir si ofreces cooked to order '
               '(si sí, consumer advisory en carta, web y marketplaces); el establishment number y los lotes de cada '
               'proveedor de carne archivados; la beer & wine license se pide al firmar el local; el grill cook líder '
               'contratado antes de la obra; cierre con el Excel, la calculadora de la carne, las fries y el coste por '
               'burger, y el checklist')),
])
_RANURAS = OrderedDict([(1, range(39, 44)), (2, range(46, 51)), (3, range(53, 59)), (4, range(61, 67)),
                        (5, range(69, 76)), (6, range(78, 83)), (7, range(85, 91)), (8, range(93, 100)),
                        (9, range(102, 109)), (10, range(111, 118))])
_N9 = OrderedDict([
    (102, '§9 1/7: el marco US por niveles (federal, estatal, condado, ciudad); LLC + EIN; sales tax permit; business '
          'license; zoning check ANTES de firmar; plan review (Food Code 8-201.11) + building permit → certificate of '
          'occupancy; fire marshal; sales tax {{sales_tax}} de ejemplo, un solo tipo («some states tax to-go food '
          'differently», sin cifra)'),
    (103, '§9 2/7: campana y fuego: Type I hood + supresión UL 300 sobre los flat-tops y las fryers; makeup air; limpieza de '
          'campana y conductos según NFPA 96 (trimestral con volumen alto de grasa, semestral si es moderado: pregúntalo '
          'al fire marshal); Class K + extintores; grease interceptor (lo dimensiona el condado en el plan review); '
          'aceite: filtrado cada noche, cambio por TPM o por el fabricante (SIN límite federal de polares) y el usado a un '
          'renderer autorizado; health permit + inspección previa; Certified Food Protection Manager (2-102.12) + food '
          'handler cards según estado'),
    (104, '§9 3/7: carne picada: FDA Food Code 2022 (cada estado adopta su edición) 3-401.11(A)(2): 155 °F (68 °C) durante '
          '17 segundos para la carne picada (comminuted), o 145 °F 3 min · 150 °F 1 min · 158 °F instantáneo; SOP del kit: '
          'TODAS las smash a ≥ 155 °F 17 s con sonda de punta fina a una muestra por tanda (el color y la crust no '
          'certifican la temperatura); cold holding ≤ 41 °F (3-501.16) y la carne cruda separada por debajo de lo listo '
          'para comer y por especie (3-302.11); carne comprada ya picada o en balls con el establishment number del '
          'proveedor y lotes; grinding logs: el kit NO afirma que sean obligatorios para un restaurante (la regla de FSIS '
          'de 2015 es para «retail stores and official establishments that grind raw beef»): si picas en casa, lleva un '
          'house-grind log (lotes, establishment numbers, hora de cada picada y de la limpieza) y pregunta a tu health '
          'department; poultry 165 °F'),
    (105, '§9 4/7: consumer advisory 3-603.11: solo si ofreces la burger «cooked to order» (poco hecha a petición del '
          'cliente, 3-401.11(D)): disclosure («hamburgers (can be cooked to order)» o asterisco) + reminder («Consuming '
          'raw or undercooked meats, poultry, seafood, shellfish, or eggs may increase your risk of foodborne illness»), '
          'en la carta, en la web y en los listados de marketplace; NUNCA en el menú infantil ni para highly susceptible '
          'populations (3-801.11: catering a residencias o colegios, cocción completa); el caso sirve todo cocido y no '
          'necesita advisory; acrilamida: SIN límite federal para restaurantes; en California, Prop 65 (el estado '
          'demandó en 2005 a las cadenas por las fries; KFC acordó en 2007 avisar y pagar $208,000 + $133,000): «if you '
          'open in California, ask your attorney about the Prop 65 warning for fried potatoes»'),
    (106, '§9 5/7: alérgenos: 9 mayores US incluido el sésamo (FASTER Act, desde 2023): el bun (wheat; milk, egg y soy '
          'según la receta; sesame en las semillas y a veces en el aceite), el American cheese (milk), las salsas (mayo '
          '= egg), los shakes (milk; mix-ins con peanuts o tree nuts), el chicken sandwich rebozado (wheat, egg, milk) y '
          'el aceite de freír compartido (cross-contact); el flat-top compartido pasa wheat y sesame del bun a la carne '
          'si se tuesta en él; la mostaza NO es major en EE. UU. (sí en UK); «gluten-free»: 21 CFR 101.91, NO se promete; '
          'allergen matrix'),
    (107, '§9 6/7: beer license o beer & wine license (agencia estatal + aprobación local; «apply early», NO prometer '
          'licencia); liquor liability en el seguro ({{seguros_anual}} con general liability, product liability, '
          'property y workers\' comp); personal: W-2 por horas (nada de 1099 para grill cooks o counter crew), I-9, W-4, '
          'salario mínimo estatal (federal $7.25/h, DOL); sin servers y sin tip credit: las propinas del tip jar son del '
          'equipo (los managers y el dueño nunca se quedan propinas); OSHA (quemaduras del flat-top y de las fryers); '
          'música ASCAP/BMI/SESAC; packaging ordinances locales (prohibiciones de poliestireno)'),
    (108, '§9 7/7: venta desde casa: las cottage food laws no cubren la carne (TCS): este plan es de local con permiso '
          '(«check your state»); y, como ÚLTIMA frase o frases, las notas UK y Australia SIN cifras de cocción: UK: '
          'registro del food business en el council 28 días antes, FHRS 0-5; la FSA espera las burgers de carne picada '
          'bien hechas salvo controles validados («ask your local authority»); VAT 20 % en sala y en la comida caliente '
          'para llevar («check HMRC VAT Notice 709/1»); 14 alérgenos (mostaza, apio, sulfitos, altramuces, moluscos); '
          'premises + personal licence para el alcohol; Australia en una línea: Food Safety Supervisor y GST 10 %'),
])


def _notas_docx():
    out = OrderedDict()
    for s, filas in _RANURAS.items():
        tanda, nota = _SEC[s]
        for k, i in enumerate(filas, 1):
            n = _N9.get(i) or ('§%d %d/%d: %s' % (s, k, len(filas), nota))
            out[i] = n + ' ‖ ' + _FORMA % (s, tanda)
    return out


DOCX_NOTAS = OrderedDict([('bur', _notas_docx())])

# ==========================================================================
# Pistas por celda (extraer_textos.py → textos_es.json → tandas)
# ==========================================================================
_CASO = ('US §8: caso US = 195 covers/día equivalentes (≈ 107 en sala, 44 plazas, counter service; ≈ 36 pedidos de '
         'take-out/pickup = 57.6 covers; ≈ 19 pedidos de marketplace = 30.4 covers; 1 pedido = 1.6 covers) × $16.50 (sin '
         'sales tax; counter service, sin propina) × 360 días (abre 7 días); beer; sin cifras del ES ni historia de '
         'versiones')
CELDA_PISTAS = OrderedDict([
    (('BURP', _S, 'A2'), 'D8: añade una vez que los importes van «in your currency» (sin símbolo)'),
    (('BURP', _S, 'C4'), _CASO + '; media del año 1 con la rampa de apertura; compárala con el paso de gente de tu calle y '
                                 'con los pedidos que caben en una hora punta'),
    (('BURP', _S, 'C5'), _CASO + '; check de $16.50 por cover equivalente = sala 107 × $15.00 (comida $12.00 + bebida $3.00) '
                                 '+ take-out 36 pedidos × $28.00 + marketplace 19 pedidos × $32.00 (carta un 15 % más cara) '
                                 '= (1,605 + 1,008 + 608) ÷ 195 = $16.52 (Kit estimate, US §8); el precio con impuesto lo '
                                 'calcula la fila "Menu price incl. sales tax"'),
    (('BURP', _S, 'C6'), _CASO + '; 360 días = abre 7 días a la semana; cierra Thanksgiving, Christmas Day, New Year\'s Day '
                                 'y 2 días de mantenimiento de la campana y las fryers'),
    (('BURP', _S, 'C7'), 'Clientela que repite y más pedidos de pickup el año 2; se aplica a los covers con el mismo check; '
                         'el personal NO sube con este porcentaje (va en Staffing)'),
    (('BURP', _S, 'C8'), 'Sobre el año 2. Conservador: el techo lo ponen los dos flat-tops, las 44 plazas del viernes y el '
                         'sábado y los pedidos que caben en una hora punta'),
    (('BURP', _S, 'C13'), 'US §5.2 y §8: food cost 34 % (Kit estimate): el coste TEÓRICO por burger de la calculadora del kit '
                          'sale más bajo (el double con fries, a $5.25/lb, ronda un cuarto del precio de carta); el 34 % es el '
                          'consumo real de TODA la carta con la merma, los comps, el pollo, el bacon, los shakes y la carne '
                          'al alza; sin cifra de la calculadora inventada'),
    (('BURP', _S, 'C14'), 'US §8: beverage cost 20 % (soft drinks de fountain, shakes y beer ≈ 25 % de la bebida; Kit '
                          'estimate)'),
    (('BURP', _S, 'C15'), 'US §8: disposables 4.5 % (wrappers, burger boxes, fry cups, tarrinas de salsa, bolsas, vasos; '
                          'packaging ordinances locales)'),
    (('BURP', _S, 'C16'), 'US §8: 19 % de las ventas por marketplaces (DoorDash, Uber Eats, Grubhub, ≈ 19 pedidos al día); el '
                          'pickup directo por teléfono, web o kiosk no paga comisión: empújalo; la smash llega peor que la '
                          'pizza (la crust se ablanda): fries en envase ventilado'),
    (('BURP', _S, 'C17'), 'PIZ-US §5.3: 25 % = plan Plus de DoorDash / Uber Eats (Basic 15 %, Premier 30 %; + 6-10 % en '
                          'pickup por la app); compruébalo en tu contrato'),
    (('BURP', _S, 'C24'), 'US §8: $4,500/mes = 1,700 sq ft × ~$32/sq ft/año (Kit estimate, editable); local de segunda '
                          'generación que ya fue restaurante, con ruta posible para la campana'),
    (('BURP', _S, 'C26'), 'US §8: $1,900/mes (gas de los flat-tops y las fryers, electricidad del walk-in, los reach-ins y '
                          'la campana con su makeup air, agua; Kit estimate): pide el histórico del local'),
    (('BURP', _S, 'C27'), 'US §8: $7,500/año = general liability + product liability + liquor liability (beer) + property '
                          '+ workers\' comp (Kit estimate)'),
    (('BURP', _S, 'C31'), 'US §8: SBA 7(a) al 10 % a 10 años, sin interest-only; el préstamo lo calcula "Financing"'),
    (('BURP', _S, 'C51'), 'US §1: 44 plazas en mesas y una window counter (sin patio); counter service: se pide en el '
                          'counter o el kiosk; quien se lleva el pedido o lo recibe en casa no ocupa mesa'),
    (('BURP', _S, 'C58'), 'Media ponderada: la sala y el pickup cobran al momento y los marketplaces liquidan cada semana lo '
                          'que venden (el 19 % de las ventas)'),
    (('BURP', _S, 'C59'), 'Plazo de pago a los proveedores de carne, buns, fries y bebida (14 días en el caso): negócialo '
                          'por escrito; si el proveedor de carne pide pago semanal o COD, baja la cifra'),
    (('BURP', _N, 'A8'), 'SPEC §4.1 línea 4 (Bar): sin divisores 1,10/1,21 → «divide a menu price by 1 + your sales tax '
                         'rate»; P&L excl. sales tax, cash flow incl.; un solo tipo en el ejemplo (B39 = B40 = 8 %)'),
    (('BURP', _N, 'A10'), 'F1-camino §6: Mes 1 = ENERO, en el orden del calendario (febrero el más flojo, enero y noviembre '
                          'detrás; mayo y el verano, los picos); sin el cierre de enero ni el agosto español'),
    (('BURP', _N, 'A12'), 'El Word cita las cifras de este Excel (si cambias el libro, manda el Excel); la calculadora de la '
                          'carne, las fries y el coste por burger (' + CALC_EN + ') va aparte y su food cost por burger NO '
                          'se copia en "0. Assumptions" (allí va el food cost medio de toda la carta, con la merma)'),
    (('BURP', _P, 'F10'), 'US §8: burgers, chicken sandwich, fries y sides: ≈ 50 % de las ventas en sala, ≈ 31 % take-out y '
                          '≈ 19 % por marketplaces; un solo sales tax en el ejemplo'),
    (('BURP', _P, 'F50'), 'Suelo del margen tras TODOS los variables: con el 44.5 % de variables del caso (comida y bebida, '
                          'disposables, marketplace, tarjeta y varios) el suelo es 52 %; si los marketplaces suben, baja'),
    (('BURP', _P, 'F52'), 'Techo de la mercancía sobre ventas: la carne es más de la mitad de la compra de comida y su precio '
                          'manda (Kit estimate)'),
    (('BURP', _P, 'F53'), 'Techo del personal sobre ventas con counter service, dos flat-tops y 7 días (Kit estimate)'),
    (('BURP', _P, 'F55'), 'Suelo de resultado neto a régimen para que el plan se sostenga (Kit estimate; sin la cifra '
                          'española del 8-10 %)'),
    (('BURP', _E, 'E25'), 'US §8 y F1-camino §6: 5 servicios completos por plaza y día (11 h abiertas, pedido en el counter y '
                          'estancias de 20-30 min); techo físico, no objetivo; solo la sala da ≈ 2.4; el equilibrio de caja '
                          'pide menos (fila 26)'),
])
for _f, _nota in [(7, 'F1-camino §6: arquitecto, planos MEP y de la campana, plan review y permit fees ($12,000, Kit '
                      'estimate); sin licencia ni declaración responsable españolas'),
                  (8, 'F1-camino §6: local de segunda generación (ya fue restaurante) de 1,700 sq ft con el order counter, '
                      'la cocina a la vista, signage & facade ($67,500, Kit estimate)'),
                  (9, 'F1-camino §6: el duct de la campana hasta la cubierta y el makeup air ($8,000; la campana Type I con la '
                      'supresión va en la fila 14); NADA de la ordenanza de Madrid'),
                  (10, 'F1-camino §6: servicio eléctrico y panel (walk-in, reach-ins, shake machine, kiosk, makeup air) y el '
                       'HVAC ($12,000): pregunta la potencia disponible ANTES de firmar'),
                  (11, 'F1-camino §6: fontanería, líneas de gas de los flat-tops y las fryers y el grease interceptor que '
                       'dimensiona el condado ($12,000)'),
                  (12, 'US §4: flat-top de gas de 36" de $589 (Avantco) a $4,858 (Imperial, plancha de 1"), '
                       'webstaurantstore oct-2026; el de 48" sin precio leído: el caso cuenta dos de 48" con bun toaster, '
                       'smash presses ($10.49-25.99 cada una) y scrapers ($10,000, Kit estimate)'),
                  (13, 'F1-camino §6: tres fryers de gas con filtrado (fries aparte del pollo rebozado por cross-contact) y la '
                       'fry station ($9,000, Kit estimate, sin precio leído)'),
                  (14, 'F1-camino §6: campana Type I con supresión UL 300 sobre los flat-tops y las fryers ($12,000, Kit '
                       'estimate); limpieza según NFPA 96'),
                  (15, 'F1-camino §6: make-line unit, chef base refrigerada bajo el flat-top para las balls a 41 °F y la '
                       'estación de queso y holding ($6,500, Kit estimate)'),
                  (16, 'US §4 y F1-camino §6: walk-in 6×8 (≈ $12,800, webstaurantstore) + reach-ins, freezer de fries y '
                       'máquina de hielo ($20,800 en total); cold holding ≤ 41 °F'),
                  (17, 'F1-camino §6: shake machine, blenders y estación de bebida (fountain, beer) ($4,000, Kit estimate)'),
                  (18, 'US §8: 3-comp sink, dish machine, hand sinks de la línea y de la cocina, estanterías e inox'),
                  (19, 'US §8: báscula de porciones en oz, ball portioner, termómetros de sonda de punta fina, tester de TPM '
                       'o tiras, etiquetas y la estación to-go ($4,000)'),
                  (20, 'US §1: 44 plazas en mesas y una window counter, y el order counter; sin patio'),
                  (21, 'US §8: POS con self-order kiosk, KDS, online ordering y las tablets de los marketplaces; sin '
                       'Veri*factu'),
                  (22, 'F1-camino §6: LLC, abogado, licencias, food safety plan y la formación de pre-apertura de 2 semanas '
                       '($10,500)'),
                  (23, 'US §8: marca, web con carta y alérgenos, fotos y el vídeo de lanzamiento (el smash vende en vídeo)'),
                  (24, 'US §8: carne (ya picada o en balls, con establishment number), potato buns, American cheese, fries '
                       'congeladas, aceite, salsas, disposables y bebida')]:
    CELDA_PISTAS[('BURP', _I, 'D%d' % _f)] = _nota
for _f in range(7, 25):
    CELDA_PISTAS.setdefault(('BURP', _I, 'D%d' % _f), 'Nota de la partida del ejemplo US (rótulo fijado de la col. A en '
                                                       '"fijos_en"); sin marcas ni normas españolas: solo rangos con '
                                                       'fuente de US §4 o ninguno')
# Staffing J5:J11: cada puesto US en la fila ES de su jornada (FIJOS): la nota describe el puesto US, no el ES
for _f, _nota in [(5, 'Owner / GM (1 × 1.0, $4,500/mes): compra de la carne y sus proveedores, carta, marketplaces y '
                      'gestión; cubre los picos en la línea; cobra por debajo de un manager de cadena: «owner\'s draw in '
                      'addition from net profit»'),
                  (6, 'Grill cooks (2 × 1.0, $5,892/mes en total ≈ $17/h, BLS 35-2014 mediana ≈ $17.98): la smash station '
                      'en el flat-top: aplastar, la crust, los tiempos y la sonda por tanda; con un solo grill cook, una '
                      'baja cierra la línea'),
                  (7, 'Fry & prep cook (1 × 1.0, $2,773/mes ≈ $16/h): fryers, fries, el filtrado del aceite, salsas, balls '
                      'porcionadas y mise en place'),
                  (8, 'Shift lead (1 × 1.0, $3,639/mes ≈ $21/h): abre o cierra, caja, kiosk, marketplaces, el registro de '
                      'temperaturas y la información de alérgenos'),
                  (9, 'Counter crew (3 × 0.75, $6,044/mes en total ≈ $15.50/h): cashier, expo y to-go packing; sin '
                      'propinas modeladas (las del tip jar son del equipo)'),
                  (10, 'Weekend crew (3 × 0.4, $3,223/mes en total ≈ $15.50/h, part-time W-2): viernes a domingo, segundo '
                       'flat-top y empaquetado; nunca como 1099'),
                  (11, 'Dish & prep (1 × 0.6, $1,612/mes ≈ $15.50/h): friegue, limpieza del flat-top y de la línea, '
                       'reposición')]:
    CELDA_PISTAS[('BURP', _R, 'J%d' % _f)] = _nota
for _f, _nota in [(21, 'US §8: 11 h de servicio al día (11:00-22:00; 23:00 viernes y sábado), sin cierre de tarde'),
                  (22, 'US §8: 3.5 personas de media a la vez (flat-top, fryer, counter y expo); el viernes y el sábado por '
                       'la noche hacen falta más (entra el weekend crew)'),
                  (23, 'US §8: 2.5 h de producción (balls porcionadas, cortes, salsas, reponer la línea) antes de abrir, '
                       'desde las 8:30'),
                  (24, 'US §8: 2 personas en producción (un grill cook y el fry & prep cook)')]:
    CELDA_PISTAS[('BURP', _R, 'J%d' % _f)] = _nota
# Tabla D19 (Instructions 35-46, 12 filas como el ES): «US BURGER RESTAURANT BENCHMARKS (sourced) AND KIT ESTIMATES»
# (Benchmark | Value | Source | Note). Cada fila sustituye a la ES de la misma fila; solo lo «leído» con fuente; lo
# «(resumen)» = Kit estimate
_D19 = OrderedDict([
    (35, 'fila → «Month 1 of the plan» · «January» · «Plan decision» · nota: orden del calendario; febrero el más flojo, '
         'enero y noviembre detrás; mayo y el verano, los picos; si abres en otro mes, gira la fila de "12-Month Cash Flow"'),
    (36, 'fila (sustituye la hamburguesa en el reparto español) → «Consumer demand (US searches)» · «"smash burger" about '
         '673,000 a month; "burger restaurant" 110,000; "smash burger restaurant" 4,400» · «DataForSEO, US, Oct 2026» · '
         'nota: demanda de consumo, no de compradores del plan'),
    (37, 'fila → «Menu prices (this plan)» · «single $8.49 · double $10.99 · triple $13.49 · combo $15.99 · shake $6.49» · '
         '«Kit estimate (Oct 2026)» · nota: dine-in cover $15.00 (food $12.00 + beverage $3.00); marketplace menu about 15% '
         'higher'),
    (38, 'fila → «Ball (raw) for a smash burger» · «3 oz (85 g); 2-4 oz» · «Kit estimate» · nota: el double lleva dos balls '
         '(6 oz crudas); el coste se calcula sobre el peso CRUDO'),
    (39, 'fila → «Burgers per pound of beef» · «about 5 balls of 3 oz (16 oz ÷ 3 = 5.3)» · «' + CALC_EN + '» · nota: pesa '
         'tus balls y mide la merma de plancha en la hoja "Beef & Patty"'),
    (40, 'fila → «Delivery marketplace commission» · «DoorDash 15 / 25 / 30% + 6% pickup; Uber Eats 15-30%» · '
         '«merchants.ubereats.com; DoorDash tiers (Oct 2026)» · nota: este plan, 25 % sobre el 19 % de las ventas; el '
         'pickup directo no paga comisión'),
    (41, 'fila (sustituye el IVA de la hamburguesería) → «Sales tax» · «8% (example: state + local)» · «Kit example: look '
         'up your state and city rate» · nota: un solo tipo en el libro; algunos estados gravan distinto la comida para '
         'llevar'),
    (42, 'fila (sustituye la carne picada del RD 1021/2022) → «Ground beef (cooking)» · «155 °F (68 °C) for 17 seconds» · '
         '«FDA Food Code 2022, 3-401.11(A)(2)» · nota: todas las smash cocidas; sonda en una por tanda; cooked to order '
         'solo a petición y con consumer advisory (3-603.11)'),
    (43, 'fila (sustituye los 175 °C de la acrilamida) → «Ground beef (cold holding)» · «41 °F (5 °C) or below; raw beef '
         'below ready-to-eat food» · «FDA Food Code 2022 (3-501.16, 3-302.11)» · nota: compra la carne ya picada o en balls '
         'con el establishment number del proveedor; house-grind log si picas tú'),
    (44, 'fila (sustituye los polares de la Orden de 1989) → «Frying oil» · «no federal limit on total polar materials '
         '(TPM)» · «Kit summary» · nota: filtra cada noche y cambia por la lectura de TPM o por el fabricante; el usado, a '
         'un renderer autorizado'),
    (45, 'fila (sustituye el SMI) → «Minimum wage» · «federal $7.25/h + your state» · «U.S. Department of Labor '
         '(dol.gov)» · nota: este plan presupuesta ≥ $15/h; teclea el suelo de tu estado en "0. Assumptions"'),
    (46, 'fila (sustituye el convenio) → «Labor cost / sales» · «about 30-32% with counter service» · «Kit estimate» · '
         'nota: sin servers ni propinas modeladas; el sueldo del dueño va en la fila del GM'),
])
for _f, _p in _D19.items():
    for _col in 'ABCD':
        CELDA_PISTAS[('BURP', _N, '%s%d' % (_col, _f))] = _p

# Pistas por TEXTO propias de la hamburguesería (se suman a las de extraer_textos.PISTAS): US §6 y §9
PISTAS_EXTRA = [
    (r'[Cc]omensal|[Cc]ubierto', 'US §8: el caso cuenta «covers» (195 equivalentes; 1 order = 1.6 covers); «orders» para '
                                 'take-out y marketplace; nunca «customers» para el volumen diario'),
    (r'[Pp]edido', 'take-out order · pickup order · marketplace order (1 order = 1.6 covers)'),
    (r'[Hh]amburgueser', 'burger restaurant (título) · burger joint / burger shop (prosa coloquial)'),
    (r'[Ss]mash|[Aa]plast', 'smash burger (nunca «smashed burger») · «smashed on the flat-top» · smash press / smasher'),
    (r'\b[Bb]olas?\b', 'ball (la bola cruda, 3 oz) · puck · patty (el disco cocinado)'),
    (r'[Pp]lancha|fry-top', 'flat-top (la plancha de gas); NUNCA «fry-top»'),
    (r'[Cc]ostra', 'crust · lacy edges'),
    (r'\b[Pp]an\b|brioche', 'bun · potato bun · brioche bun'),
    (r'[Mm]en[uú]\b', 'combo (burger + fries + drink); nunca «value meal»'),
    (r'[Bb]atido', 'shake'),
    (r'[Cc]arne picada|[Pp]icad|[Bb]lend', 'ground beef (80/20) · ground chuck · blend (chuck, brisket, short rib)'),
    (r'[Mm]adurad', 'la regla española de la carne madurada NO cruza; el caso no ofrece dry-aged'),
    (r'[Cc]occi[oó]n|[Ss]onda|°C', 'US §6.1: 155 °F (68 °C) 17 s (Food Code 3-401.11(A)(2)); sonda de punta fina por tanda; '
                                  'cold holding ≤ 41 °F; hot holding ≥ 135 °F; la métrica solo entre paréntesis'),
    (r'[Pp]olares|[Aa]ceite', 'US §6.7: TPM (total polar materials), SIN límite federal; filtrado nocturno; used oil a '
                              'renderer'),
    (r'[Aa]crilamida', 'US §6.8: sin límite federal para restaurantes; Prop 65 en California («ask your attorney»)'),
    (r'[Ff]reidora', 'fryer (de gas, con filtrado)'),
    (r'[Pp]atata', 'fries (frozen 3/8" crinkle o fresh-cut)'),
    (r'[Qq]ueso|cheddar', 'American cheese (en lonchas)'),
    (r'[Ll][ií]nea de montaje|[Pp]ase', 'make line · expo'),
    (r'[Mm]ostrador|[Bb]arra de ventana', 'order counter · window counter'),
    (r'[Ii]nformaci[oó]n al (?:cliente|consumidor)|[Pp]oco hecha', 'consumer advisory (3-603.11): disclosure + reminder, '
                                                                   'solo si ofreces cooked to order'),
    (r'\bSL\b|aut[oó]nomo|IAE|Seguridad Social|alta en', '«LLC vs S corp with your CPA» · «EIN + state payroll / '
                                                         'unemployment registration»'),
    (r'Veri\*?factu|TPV', '«POS that reports sales tax» (sin Veri*factu)'),
    (r'[Uu]rbanism|[Ll]icencia de (?:actividad|apertura|obra)|compatibilidad|declaraci[oó]n responsable',
     '«zoning check before signing» · «building permit + certificate of occupancy» · business license + sales tax permit'),
    (r'[Tt]erraza', 'el caso US no tiene patio (44 plazas en sala y window counter)'),
    (r'alcohol|cerveza|vino', 'US §6.6: «beer license» o «beer & wine license» («apply early», sin prometerla) · liquor '
                              'liability'),
    (r'[Hh]umos|[Cc]ampana|extracci|[Cc]onducto', 'US §6.6: Type I hood + fire suppression (UL 300) + makeup air sobre los '
                                                  'flat-tops y las fryers; NFPA 96; «ask the fire marshal in writing»'),
    (r'[Gg]as\b|RD 919', 'gas lines por un plumber o gas fitter licenciado con su permiso (sin RD 919/2006)'),
    (r'[Rr]egistro sanitario|RGSEAA|APPCC|autocontrol', 'plan review (Food Code 8-201.11) + health permit + inspection; '
                                                        'written food safety plan'),
    (r'[Ee]xtintor', 'Class K + 2-A extinguishers'),
    (r'[Gg]rasas|aceite usado', 'grease interceptor · used cooking oil pickup (renderer)'),
    (r'irrellenable|Ley 1/2025|Ley 7/2022|desperdicio|[Ee]nvase', 'sin equivalente US: packaging ordinances locales '
                                                                  '(wrappers, burger boxes, fry cups)'),
    (r'[Rr]eclamaciones', 'required public notices (health permit, beer license, labor law posters)'),
    (r'[Cc]onvenio|[Cc]ontrato|n[oó]mina|registro de jornada', 'offer letters, I-9, W-4, state minimum wage, W-2 por '
                                                               'horas (sin convenio; sin «digital obligatorio»)'),
    (r'PRL|[Pp]revenci[oó]n de riesgos|EPI', 'OSHA basics (quemaduras del flat-top y de las fryers, resbalones con la '
                                             'grasa)'),
    (r'[Mm]anipulador|[Ff]ormaci[oó]n', 'Certified Food Protection Manager (2-102.12) + food handler cards (según estado)'),
    (r'[Aa]l[eé]rgen|s[eé]samo|soja|mostaza', 'US §6.9: 9 major allergens incl. sesame (UK 14); bun = wheat (+ milk, egg, '
                                              'soy, sesame según receta); American cheese = milk; mayo = egg; la mostaza NO '
                                              'es major en EE. UU.'),
    (r'[Gg]luten|cel[ií]ac', 'US §6.9: NO prometer «gluten-free» (21 CFR 101.91): bun de trigo, fryer y flat-top compartidos'),
    (r'[Rr]ider|[Rr]epart', 'own drivers = W-2 + hired & non-owned auto insurance (check your state); el caso no tiene '
                            'reparto propio'),
    (r'[Pp]lataforma|Glovo|Just Eat|Uber|delivery', 'DoorDash / Uber Eats / Grubhub con sus tiers (PIZ-US §5.3)'),
    (r'SGAE|AGEDI', '«Music licensing (ASCAP/BMI/SESAC)»'),
    (r'[Mm]en[uú] del d[ií]a|mediod[ií]a', 'lunch combo: el «menú del día» español no cruza'),
    (r'[Aa]gosto|vacaciones|[Ee]nero', 'el caso US no cierra en enero ni en agosto: abre 7 días (360)'),
    (r'San Valent[ií]n|Navidad|Reyes', 'National Burger Month (mayo) · Super Bowl Sunday · March Madness · graduaciones'),
    (r'[Ff]ranquici|Goiko|La Pepita', 'franquicias US solo como comparación de inversión (Smashburger, Freddy\'s: «reported '
                                      'by third-party franchise directories; check the FDD»)'),
]

# Glosario de la hamburguesería (US §9, OBLIGATORIO; manda sobre el de FT/CAF)
GLOSARIO_BUR = OrderedDict([
    ('hamburguesería (negocio)', 'burger restaurant (título) · burger joint / burger shop (prosa)'),
    ('smash burger · hamburguesa aplastada', 'smash burger (nunca «smashed burger») · «smashed on the flat-top»'),
    ('bola de carne', 'ball (cruda, 3 oz) · puck · patty (el disco cocinado)'),
    ('plancha · fry-top', 'flat-top · griddle; NUNCA «fry-top»'),
    ('smasher · espátula', 'smash press / smasher · burger scraper / spatula'),
    ('costra · bordes', 'crust · lacy edges'),
    ('pan de patata', 'potato bun'),
    ('simple · doble · triple', 'single · double · triple'),
    ('menú · combinado', 'combo; nunca «value meal»'),
    ('batido', 'shake'),
    ('línea de montaje · pase', 'make line · expo'),
    ('cocinero de plancha · de freidora', 'grill cook · fry cook · line cook · shift lead'),
    ('para llevar · plataforma', 'take-out / to-go / pickup · third-party delivery marketplace'),
    ('comensal equivalente · ticket', 'covers · average check (excl. sales tax)'),
    ('escandallo', 'recipe costing · cost per burger · plate cost'),
    ('carne picada 80/20', 'ground beef (80/20) · ground chuck · blend: chuck, brisket, short rib'),
    ('aviso al consumidor', 'consumer advisory (disclosure + reminder)'),
    ('contaminación cruzada', 'cross-contact (alérgenos) · cross-contamination (patógenos)'),
    ('merma de plancha', 'cook loss / shrink'),
    ('compuestos polares', 'TPM (total polar materials)'),
    ('75 °C · temperatura de cocción', '155 °F (68 °C) for 17 seconds (Food Code 3-401.11(A)(2))'),
    ('14 alérgenos', '9 major allergens (US; UK 14)'),
    ('registro sanitario', 'health permit + plan review'),
    ('licencia de apertura', 'business license + certificate of occupancy'), ('convenio', 'state/local minimum wage'),
    ('IVA · fianza', 'sales tax · deposit'), ('autónomo / SL', 'LLC'),
    ('menú del día', 'lunch combo'),
])


# ==========================================================================
# Caso de ejemplo US (research US §8; F1-camino §6): celdas VERDES. (corto, hoja ES, celda) → (valor, rótulo)
# ==========================================================================
# Mes 1 = ENERO (F1-camino §6): los pesos de US §8 en el orden del calendario, sin girar
ESTACIONALIDAD_US = (0.078, 0.076, 0.082, 0.084, 0.088, 0.090, 0.090, 0.088, 0.082, 0.082, 0.078, 0.082)   # ene → dic
assert abs(sum(ESTACIONALIDAD_US) - 1) < 1e-9


def valores_bur(M):
    v = OrderedDict()
    sup = [
        ('B4', 195, 'Comensales/día'), ('B5', 16.5, 'Ticket medio'), ('B6', 360, 'Días de apertura'),
        ('B7', 0.06, 'Crecimiento de volumen del año 2'), ('B8', 0.04, 'Crecimiento de volumen del año 3'),
        ('B11', 0.80, 'Ventas de COMIDA'), ('B13', 0.34, 'Coste de mercancía sobre las ventas de COMIDA'),
        ('B14', 0.20, 'Coste de mercancía sobre las ventas de BEBIDA'), ('B15', 0.045, 'Consumibles'),
        ('B16', 0.19, 'Ventas por delivery'), ('B17', 0.25, 'Comisión de la plataforma'),
        ('B18', 0.03, 'Comisión de los medios de pago'), ('B20', 0.10, 'Seguridad Social'),
        ('B21', 12, 'Número de pagas'), ('B22', 15080, 'SMI anual'), ('B24', 4500, 'Alquiler mensual'),
        ('B25', 2, 'Fianza'), ('B26', 1900, 'Suministros'), ('B27', 7500, 'Seguros'), ('B28', 0.01, 'Varios'),
        ('B30', 130000, 'Recursos propios'), ('B31', M.CALIBRAR, 'Préstamo bancario'), ('B32', 0.10, 'Tipo de interés'),
        ('B33', 10, 'Plazo del préstamo'), ('B34', 0, 'Carencia'), ('B35', 3, 'Fondo de maniobra'),
        ('B37', 0.25, 'Impuesto de Sociedades, nueva'), ('B38', 0.25, 'Impuesto de Sociedades, tipo'),
        ('B39', 0.08, 'IVA repercutido de restauración'), ('B40', 0.08, 'IVA repercutido/soportado'),
        ('B41', 0, 'IVA soportado en compras'), ('B42', 0, 'Bases negativas'),
        ('B44', 10, 'Vida útil de obra'), ('B45', 7, 'Vida útil de maquinaria'),
        ('B51', 44, 'Aforo'), ('B52', 0.75, 'Actividad del mes 1'), ('B53', 4, 'Meses hasta alcanzar'),
        ('B54', 2, 'Meses de alquiler ANTES'), ('B55', 0.10, 'Imprevistos sobre las partidas de OBRA'),
        ('B58', 2, 'Días medios de cobro'), ('B59', 14, 'Días medios de pago'),
        ('B62', 0.25, 'Bebida que compras al 21'), ('B63', 0.08, 'IVA de la bebida ALCOHÓLICA'),
        ('B65', 1.15, 'DSCR mínimo'), ('B66', 1.25, 'DSCR objetivo'), ('B67', 0.15, 'Holgura mínima'),
        ('B68', None, 'Suelo salarial anual'),
    ]
    for c, val, rot in sup:
        v[('BURP', _S, c)] = (val, rot)
    # Inversión (F1-camino §6 en 18 filas, FIJOS): filas 7-24 = $228,300; los imprevistos (B27) van por fórmula (10 % de 7-11
    # = $11,150: arquitecto, obra con rótulo, duct, eléctrico + HVAC y fontanería con gas y grease interceptor)
    for k, val in enumerate([12000, 67500, 8000, 12000, 12000, 10000, 9000, 12000, 6500, 20800, 4000, 10500, 4000,
                             11000, 7000, 10500, 5500, 6000]):
        v[('BURP', _I, 'B%d' % (7 + k))] = (val, None)
    # P&L: fijos B26-B34 ($26,000, F1-camino §6), G13 (soportado de la bebida: valor en el ES) → 0, H11 → 25 % (beer sobre
    # la bebida, = B62), umbrales del semáforo (el margen «bruto» del libro descuenta TODOS los variables: con 44.5 % de
    # variables del caso, el suelo es 52 %; COGS 33 %; personal 36 %; alquiler 10 %; neto 5 %)
    for k, val in enumerate([3600, 4000, 6500, 3300, 2200, 2400, 900, 1000, 2100]):
        v[('BURP', _P, 'B%d' % (26 + k))] = (val, None)
    v[('BURP', _P, 'G13')] = (0, None)
    v[('BURP', _P, 'H11')] = (0.25, None)
    for c, val, rot in [('E50', 0.52, 'Margen bruto'), ('E52', 0.33, 'Coste de mercancía /'),
                        ('E53', 0.36, 'Coste de personal'), ('E54', 0.10, 'Alquiler'), ('E55', 0.05, 'Resultado neto')]:
        v[('BURP', _P, c)] = (val, rot)
    # Staffing (US §8, en la fila ES de su jornada): personas (B), FTE por persona (C), bruto mes TOTAL de la fila (D);
    # ≥ $15/h, 12 pagas, sin propinas; 2 grill cooks, 3 counter crew y 3 weekend crew en su fila (E4) → 9.05 FTE,
    # $27,683/mes. Cobertura: servicio 11 h × 3.5 + producción 2.5 h × 2 (US §8)
    for f, (b, c, d) in zip(range(5, 12), [(1, 1.0, 4500), (2, 1.0, 5892), (1, 1.0, 2773), (1, 1.0, 3639),
                                           (3, 0.75, 6044), (3, 0.4, 3223), (1, 0.6, 1612)]):
        for col, val in zip('BCD', (b, c, d)):
            v[('BURP', _R, '%s%d' % (col, f))] = (val, None)
    v.update([(('BURP', _R, 'B14'), (5000, 'Coste anual')), (('BURP', _R, 'B15'), (5000, 'Coste anual')),
              (('BURP', _R, 'B21'), (11, 'Horas de servicio')), (('BURP', _R, 'B22'), (3.5, 'Personas necesarias')),
              (('BURP', _R, 'B23'), (2.5, 'Horas de producción')), (('BURP', _R, 'B24'), (2, 'Personas en el turno'))])
    # Break-Even!B25 (techo de rotaciones) = 5 (F1-camino §6, no el 3 de US §8): 11 h abiertas, pedido en el counter y
    # estancias de 20-30 min. El caso da 195 / 44 = 4.4 por plaza (con el take-out y el marketplace) y el equilibrio de caja
    # pide ≈ 3.4: con 3, el semáforo saldría rojo
    v[('BURP', _E, 'B25')] = (5, 'Rotaciones al día que da el local')
    # Escenarios (US §8): pesimista 180 · $15.50 · 355 / optimista 215 · $17.50 · 362
    v.update([
        (('BURP', _ES, 'B5'), (180, 'Comensales/día')), (('BURP', _ES, 'D5'), (215, 'Comensales/día')),
        (('BURP', _ES, 'B6'), (15.5, 'Ticket')), (('BURP', _ES, 'D6'), (17.5, 'Ticket')),
        (('BURP', _ES, 'B7'), (355, 'Días')), (('BURP', _ES, 'D7'), (362, 'Días')),
    ])
    # Estacionalidad (US §8, Mes 1 = ENERO sin girar: F1-camino §6) → Month 1-12
    for col, val in zip('BCDEFGHIJKLM', ESTACIONALIDAD_US):
        v[('BURP', _T, '%s5' % col)] = (val, 'Estacionalidad')
    return v


# Calibración D15 (US §8: palancas en su orden; máx. 3 vueltas). Cada celda, citada en F2-NOTAS.md (G7)
CALIBRACION_D15 = OrderedDict()


def formulas_bur():
    p = os.path.join(AQUI, 'formulas_bur.json')
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
    M.TOKENS_DOCX = tokens_bur(M.TOKENS_DOCX)
    M.PRODUCTOS_CIERRE = PRODUCTOS_CIERRE_BUR
    M.DOCX_FIJOS = docx_fijos(M)
    M.DOCX_NOTAS = DOCX_NOTAS
    M.DOCX_NOTAS_PLAN = DOCX_NOTAS_PLAN
    M.FORMULAS_EN = formulas_bur()
    M.VALORES_EN = valores_bur(M)
    M.CALIBRACION_D15 = CALIBRACION_D15
    M.CELDA_PISTAS = CELDA_PISTAS
    M.PISTAS_EXTRA = PISTAS_EXTRA
    M.CIFRAS_PROHIBIDAS = cifras_prohibidas(M.VALORES_EN)
    M.RX_BUR_NO = RX_BUR_NO
    M.REGLA_UNIDADES = REGLA_UNIDADES
    glo = OrderedDict(M.GLOSARIO)
    for k, val in GLOSARIO_BUR.items():
        glo[k] = val                          # research §9 manda (regla de jerga §0)
    M.GLOSARIO = glo
