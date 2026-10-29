#!/usr/bin/env python3
"""
datos_pol.py — Rotisserie Chicken Restaurant Business Plan Kit (EN) · los datos ES→EN que dependen del contenido: rótulos
fijados (inversión 19 → 18 filas, fijos 10 → 9, plantilla de 7 filas), POR_CELDA, pistas, tokens del docx, fijos y notas
del docx, caso US (research US §8 con Mes 1 = enero, F1-camino §6), cifras ES prohibidas y RX_POL_NO (F1-camino §7) y
glosario (US §9). Lo llama `mapas_pol.instalar()` con el módulo `mapas` YA cargado con los datos de FT/CAF (FIJOS comunes
del motor 2.2, TOKENS_DOCX). Clon de `../business-plans-en-12/datos_taq.py` (Taco EN, LIVE hoy: misma semilla, misma
rejilla salvo la rotación apagada). Sesión Claude Code, 29-oct-2026 (F2-EN).
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
POLES = os.path.join(PD, 'plan-polleria')                 # ES cerrado: F1-camino, research y cifras_caso_es.json

URL_POL = 'aichef.pro/en/digital-products/rotisserie-chicken-restaurant-business-plan'
_I, _S, _P, _R, _N, _E, _ES, _T = ('Inversión Inicial', '0. Supuestos', 'PyG 3 Años', 'Personal', 'Instrucciones',
                                   'Punto Equilibrio', 'Escenarios', 'Tesorería 12 meses')
REGLA_UNIDADES = ('MEDIDAS US (John, 13-oct): principales lb y oz, °F, gallons / quarts y sq ft; la métrica entre '
                  'paréntesis para UK: «3.0 lb (1.4 kg)», «165 °F (74 °C)», «135 °F (57 °C)», «1,600 sq ft (149 sq m)», '
                  '«50 lb (23 kg)»; nada de kg, g, km, litros ni °C como unidad principal (gate). NUNCA «63 °C» ni «75 °C» '
                  '(reglas ES): las cifras US son 135 °F y 165 °F')

# ==========================================================================
# FIJOS (por TEXTO ES, en cualquier celda de los 2 libros). Parten de los de FT/CAF (los del motor 2.2)
# ==========================================================================
FIJOS_FUERA = ('Este fichero forma parte del producto «plan-negocio-food-truck» de AI Chef Pro.',
               'Este fichero forma parte del producto «plan-negocio-cafeteria» de AI Chef Pro.')
_TITULO_CHECK = 'ROTISSERIE CHICKEN RESTAURANT STARTUP CHECKLIST'
FIJOS_NUEVOS = OrderedDict([
    # Instrucciones!A3 del checklist con el nombre comercial
    ('Este fichero forma parte del «Plan de Negocio: Pollería y Asador de Pollos» de AI Chef Pro.',
     'This file is part of the Rotisserie Chicken Restaurant Business Plan Kit by AI Chef Pro.'),
    # títulos: «rotisserie chicken restaurant» en el nombre, «Peruvian-style» / «pollo a la brasa» en descriptor y prosa;
    # nunca «poultry shop», «roaster», «pollo asado» ni «authentic» (US §9)
    ('CHECKLIST DE APERTURA — POLLERÍA Y ASADOR DE POLLOS', _TITULO_CHECK),
    ('INSTRUCCIONES DE USO — Plan financiero Pollería y Asador de Pollos',
     'HOW TO USE THIS WORKBOOK — Rotisserie Chicken Restaurant Financial Projections'),
    ('PLAN DE NEGOCIO: POLLERÍA Y ASADOR DE POLLOS',
     'ROTISSERIE CHICKEN RESTAURANT BUSINESS PLAN: PERUVIAN-STYLE COUNTER SERVICE'),
    ('Inversión inicial estimada — pollería-asador de barrio con asador de gas, mostrador y 20 plazas',
     'Estimated Startup Costs — counter-service rotisserie chicken restaurant with two gas rotisseries and 40 seats'),
    ('Ajusta las cifras a tu proyecto: son las de un caso tipo en una ciudad media, sin traspaso. Pon tus presupuestos '
     'reales en las celdas de importe.', 'US kit example (2026) — replace with your own quotes.'),
    ('Escenario realista — pollería-asador con mostrador, encargos, plataforma y sala',
     'Base case — rotisserie chicken restaurant: counter, pickup & pre-orders, delivery and dine-in'),
    ('Punto de equilibrio mensual y diario — pollería-asador de barrio',
     'Monthly and daily break-even — neighborhood rotisserie chicken restaurant'),
    # cabecera de la tabla D19 y fases del checklist con el nombre de su pestaña (F1-camino §6)
    ('DATOS DE REFERENCIA DEL SECTOR', 'US ROTISSERIE CHICKEN BENCHMARKS (sourced) AND KIT ESTIMATES'),
    ('FASE 2: LOCAL, SALIDA DE HUMOS, GAS Y LICENCIA (semanas 3-14)', 'PHASE 2: SITE, HOOD, GAS & PERMITS (weeks 3-14)'),
    ('FASE 3: OBRADOR, ASADOR Y REGISTRO SANITARIO (semanas 6-14)',
     'PHASE 3: KITCHEN, ROTISSERIES & HEALTH PERMIT (weeks 6-14)'),
    ('FASE 5: CARTA, MARCA, ENCARGOS Y PROVEEDORES (semanas 8-16)',
     'PHASE 5: MENU, BRAND, PRE-ORDERS & SUPPLIERS (weeks 8-16)'),
    # Inversión, filas 7-24: las 19 partidas de US §8 en las 18 filas con la CLASE de la fila ES (F1-camino §6):
    # 7-11 obra (base de imprevistos), 12-21 equipo, 22-24 sin amortizar, y cada partida en la fila ES más parecida.
    # «Signage & facade» entra en la obra; «electrical, HVAC, plumbing, gas lines & grease» se parte en 10 y 11; freidoras
    # y fogones van juntos (= la fila 14 ES); la estación de salsas y las tinas de marinado, con el utillaje; la nevera de
    # bebida y la máquina de hielo salen de la línea de frío a la fila 19 (botellero ES). Solo la fila 15 (campana ES: en
    # EE. UU. va en la 9) cambia de objeto (= Taco EN)
    ('Proyecto técnico de actividad y de salida de humos, y dirección de obra',
     'Architect, MEP & hood drawings, plan review & permit fees'),
    ('Obra y acondicionamiento del local, rótulo y fachada',
     'Build-out (second-generation space, 1,600 sq ft), signage & facade'),
    ('Conducto de extracción exclusivo hasta cubierta', 'Type I hood (about 14 ft), UL 300 fire suppression & makeup air'),
    ('Instalación eléctrica trifásica, cuadro y boletín', 'Electrical service, panel & gas lines'),
    ('Fontanería, separador de grasas, climatización e instalación de gas', 'Plumbing, grease interceptor & HVAC'),
    ('Asador de pollos de gas de doce espadas y juego de espadas',
     'Commercial gas rotisseries × 2 (8 spits, 48 birds per load each)'),
    ('Vitrina caliente de mostrador y mantenedor de patatas', 'Heated display merchandiser, steam table & holding cabinet'),
    ('Freidora doble y fogón', 'Fryers × 2 (50 lb) & range with stock-pot burners'),
    ('Campana extractora con motor y filtros', 'Walk-in cooler (6×8)'),
    ('Frío: armarios de pollo crudo y adobado, congelador y vitrina refrigerada',
     'Refrigerated prep table & reach-in freezer'),
    ('Lavavajillas de capota, fregaderos, lavamanos y mesas inox de espetar',
     '3-comp sink, dish machine, hand & poultry prep sinks, shelving & stainless'),
    ('Utillaje: sondas, básculas, GN, tijeras de trinchar, etiquetadora y vajilla',
     'Smallwares & sauce station (spare spits, hotel pans, probes, blender, marinating tubs)'),
    ('Botellero y nevera de bebida para llevar', 'Beverage cooler & ice machine'),
    ('Mobiliario de sala', 'Furniture (40 seats)'),
    ('TPV con Veri*factu, datáfono, impresora y tablet de plataformas', 'POS, online ordering, kiosk & delivery tablets'),
    ('Constitución de la SL, licencia, tasas, registro sanitario y APPCC', 'LLC, legal & food safety plan'),
    ('Marca, web, fotos y lanzamiento', 'Branding, website, photos & launch'),
    ('Stock inicial: pollo, patata, aceite, envases y bebida', 'Opening inventory'),
    # P&L (A10, A11, A25, fijos A26-A34 salvo marketing, que es GM). Fijos 10 → 9: la fila ES de DDD lleva el pest
    # control de US §8 y las renovaciones de permisos van con residuos, aceite y grasa (fila 31 ES)
    ('Ventas de pollo asado y cocina (mostrador, encargos, plataforma y sala)',
     'Food sales (rotisserie chicken plates, family meals & sides: counter, pickup, pre-orders, delivery & dine-in)'),
    ('Ventas de bebida (refrescos, agua, cerveza y vino)', 'Beverage sales (sodas, chicha morada, beer & wine)'),
    ('Seguros (RC + multirriesgo)', 'Insurance (general + liquor liability + property + workers\' comp)'),
    ('Gestoría laboral, fiscal y contable', 'Accounting & bookkeeping'),
    ('Mantenimiento de la campana extractora, el gas, el asador y el frío',
     'Maintenance (quarterly hood cleaning, rotisserie service, refrigeration)'),
    ('Software, TPV, teléfono e internet', 'Software, POS & online ordering'),
    ('Limpieza, lavandería, EPI y análisis de autocontrol', 'Cleaning, linens & uniforms'),
    ('Gestión de residuos y del aceite y la grasa usados', 'Waste, grease & used-oil hauling + permit renewals'),
    ('Desinsectación, desratización y desinfección (DDD)', 'Pest control'),
    ('Derechos de autor por música ambiental (SGAE y AGEDI-AIE)', 'Music licensing (ASCAP/BMI/SESAC)'),
    ('Prevención de riesgos laborales, vigilancia de la salud y formación',
     'Food safety & staff training (CFPM, allergens, OSHA)'),
    # puestos de Staffing (A5:A11): counter service, sin servers, 7 días (US §8; cada puesto en la fila ES de su función:
    # el camarero ES → counter & expo; el refuerzo de fin de semana → fry & line; las suplencias → el segundo cocinero
    # de asador, que cubre los descansos con 7 días de apertura)
    ('Titular — maestro/a asador: compra del pollo, adobos, asador, encargos y gestión',
     'Owner / GM & head of rotisserie'),
    ('Asador/a-cocinero/a: espetar, freidora, guarniciones y croquetas', 'Rotisserie cook (spitting, loads, carving)'),
    ('Dependiente/a de mostrador y caja', 'Counter lead / cashier'),
    ('Camarero/a de sala', 'Counter, packing & expo (part-time W-2)'),
    ('Ayudante de cocina y friegue de fin de semana', 'Dish & prep (part-time W-2)'),
    ('Refuerzo de sábado, domingo y festivos', 'Fry & line cook (part-time W-2, weekends & peak days)'),
    ('Suplencias de vacaciones y descansos', 'Prep & relief rotisserie cook (marinades, sides, sauces; days off)'),
])

# Mismo ES con otro EN en ESTA celda (lección de BP2 §4.1: los arreglos de un libro no se heredan a ciegas)
POR_CELDA = OrderedDict([
    # E5: la columna H de la línea de bebida = parte gravada al tipo del alcohol de B40 (= Pizza EN y Taco EN)
    (('POLP', _P, 'H4'), 'Beverage share taxed at the alcohol rate in B40 (%)'),
    (('POLP', _P, 'F11'), 'Dine-in beverages and the drinks that go out with orders (sodas, chicha morada, '
                          'beer & wine) · Column H is the share of beverage sales taxed at the alcohol rate in "0. '
                          'Assumptions" B40. With the example rates (B39 = B40 = 8%: state + local) it changes nothing. '
                          'Some states tax alcohol differently: type your alcohol rate in B40 and the alcohol share of '
                          'beverage sales here'),
    (('POLP', _S, 'A62'), 'Alcohol share of beverage purchases (reference only: no input credit in the US)'),
    (('POLP', _S, 'C62'), 'Reference only: in the US the sales tax you pay on purchases is a cost, not a credit (B41 = 0%), '
                          'so this share moves no figure in the workbook. The sales tax you COLLECT on beverages is set '
                          'by the beverage line of the P&L (column H)'),
    (('POLP', _S, 'C63'), 'NO EFFECT in this workbook: the sales tax collected on beverages is set by the beverage line of '
                          'the P&L. With the example, beer, wine, sodas, chicha morada and food all pay the same 8% (state '
                          '+ local); if your state taxes alcohol at another rate, type it in B40 and the alcohol share in '
                          'column H of that line'),
    # Mes 1 = ENERO con los pesos de US §8 en el orden del calendario (VALORES_EN B5:M5), no los del ES
    (('POLP', _T, 'O5'), 'Month 1 = JANUARY, in calendar order: rotisserie chicken is an everyday meal, so the curve is '
                         'flat. January and February are the slowest months; May (Mother\'s Day), July (Pollo a la Brasa '
                         'Day in the Peruvian community and July 4 take-out) and December (holiday family meals and '
                         'pre-orders) are the peaks. Kit weights for a mid-size US city: replace them with your area\'s '
                         'pattern; if you open in another month, rotate the row. It must add up to 100%'),
    # E4: la nota de Staffing sin servers y con las propinas del mostrador (= Taco EN, US §6.6)
    (('POLP', _R, 'A29'), 'The gross pay, employer payroll taxes, monthly cost and annual cost columns are TOTALS for the '
                          'row: for a position with several people they include all of them. "FTE" is the share of a '
                          'full-time week and is used to compare pay with the legal floor pro rata. The payroll tax rate '
                          'and the number of pay periods are in the "0. Assumptions" tab. Tips are not modeled: this is '
                          'counter service, every position is budgeted at a base wage of at least $15/h, and counter tips '
                          '(tip jar or screen) belong to the staff, never to the owner or managers. Federal rules allow a '
                          '$2.13/h cash wage with a tip credit of up to $5.12 where the state permits it; CA, OR, WA, AK, '
                          'MN, MT and NV do not (DOL)'),
])


# ==========================================================================
# Cifras prohibidas (F1-camino §7): ES de la pollería (importe y frase), casos EN publicados y RX_POL_NO.
# Formato: (regex, motivo, excepción sobre el texto entero)
# ==========================================================================
def _num(n):
    """208500 → patrón que casa 208,500 · 208.500 · 208 500 · 208500 (y nada pegado a más dígitos)."""
    s = str(n)
    cab, cola = s[:-3], s[-3:]
    return r'(?<![\d.,])' + cab + r'[.,   ]?' + cola + r'(?![\d])'


def _cifras_es():
    """Importes ≥ 10.000 € del caso ES de la pollería (`../plan-polleria/cifras_caso_es.json`, tokens con «€»: el ES
    está cerrado y manda). Los pequeños quedan cubiertos por la prohibición de «€»."""
    out = set()
    p = os.path.join(POLES, 'cifras_caso_es.json')
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
        (r'(?i)\b77 (?:covers|guests|customers|diners|orders)\b', 'caso ES (77 pedidos/día)'),
        (r'(?<![\d$])15[.,]80\b', 'ticket ES (15,80 €)'),
        (r'(?i)\b300 (?:opening )?days\b', 'días del ES (300; el caso US abre 360)'),
        (r'(?i)\b14 (?:pay periods|payments|paychecks|salaries|monthly)', 'pagas del ES (14 pagas)'),
        (r'(?i)(?:payroll|social security|employer)[^.;]{0,60}?\b33\s?%', 'Seguridad Social del ES (33 %)'),
        (r'(?i)\b33\s?%[^.;]{0,40}?(?:payroll|social security|employer)', 'Seguridad Social del ES (33 %)'),
        (r'\b17[.,]094\b', 'SMI ES (17.094 €)'),
        (r'\b1[.,]221\b', 'SMI ES (1.221 €)'),
        # la plataforma ES (F1-camino §7): 11 % de las ventas al 30 % (y el 12 % de la taquería); el caso US es el 15 %
        (r'(?i)\b1[12] ?% of (?:total )?sales\b', 'plataforma ES (11-12 % de ventas: el caso US es el 15 %)'),
        (r'(?i)\bRD 1(?:021|086|26)\b|\bRD 919\b|\bart\. ?(?:4\.1|9|30)\b|Ley 1/2025|Ley 7/2022|\bACSA\b|\bAESAN\b',
         'norma ES (RD 1021/2022, RD 1086/2020, RD 126/2015, RD 919/2006, Leyes 1/2025 y 7/2022, ACSA, AESAN)'),
        (r'\b6[03]\s?°C|\b75\s?°C', 'temperaturas ES (63 °C / 75 °C; en EE. UU. 135 °F y 165 °F)'),
        (r'\bv1\.[01]\b|\b[Vv]ersion 1\.[01]\b', 'historia de versiones (la EN nace en 2.2)'),
    ]


# casos EN publicados (frases); «360 days» del Bar EN NO va: el caso de la pollería abre 360 días
FRASES_OTROS = [(r'(?i)\b62 covers\b', 'caso de la Pizza EN («62 covers»)'),
                (r'\$36(?:\.00)?\b(?![.,]\d)', 'caso de la Pizza EN («$36»)'),
                (r'(?i)\b165 customers\b', 'caso de la Ice Cream EN («165 customers»)'),
                (r'(?i)\b210 transactions\b', 'caso de la Bakery EN («210 transactions»)'),
                (r'(?i)\b95 covers\b', 'caso del Bar EN («95 covers»)'),
                (r'\$27(?:\.00)?\b(?![.,]\d)', 'caso del Bar EN («$27»; no $27,500 ni $27,945: revisión F2)'),
                (r'(?i)\b115 covers\b', 'caso del Taco EN («115 covers»)'),
                (r'(?i)\b308 (?:opening )?days\b', 'caso del Taco EN («308 days»)')]

_NO = r"(?i)\b(?:no|not|never|cannot|can't|don't|do not|without|isn't|is not|rather than|instead of)\b"
RX_POL_NO = [
    # restos del Taco EN (F1-camino §7)
    (r'(?i)\btacos?\b|\btaquer', 'Taco EN («taco / taqueria»)', None),
    (r'(?i)trompo|al pastor', 'Taco EN («trompo / al pastor»)', None),
    (r'(?i)tortilla|masa harina', 'Taco EN («tortilla / masa harina»)', None),
    (r'(?i)salsa bar', 'Taco EN («salsa bar»)', None),
    (r'(?i)\bmezcal|\btequila', 'Taco EN / ES («mezcal / tequila»: el caso US es beer & wine)', r'(?i)liquor license|full liquor'),
    # restos de la Pizza EN y del Bar EN
    (r'(?i)\bpizz', 'Pizza EN («pizza»)', None),
    (r'(?i)Neapolitan|\bdough\b', 'Pizza EN («Neapolitan / dough»)', None),
    (r'\bVPN\b|\bAVPN\b', 'Pizza EN («VPN»)', None),
    (r'(?i)Margherita|mozzarella|San Marzano', 'Pizza EN (ingredientes)', None),
    (r'(?i)\btapas\b|\bsmall plates\b', 'Bar EN («tapas / small plates»)', None),
    (r'(?i)\bcocktails?\b', 'Bar EN («cocktails»: la pollería es beer & wine)', None),
    (r'(?i)\bhappy hour\b|\blast call\b|\bbarbacks?\b|\bneighborhood bar\b', 'Bar EN', None),
    (r'(?i)\bspirits\b', 'Bar EN («spirits»: la pollería es beer & wine)', r'(?i)liquor license|full liquor|' + _NO[4:]),
    # restos del ES (F1-camino §7)
    (r'\bIVA\b', 'ES («IVA»)', None),
    (r'(?i)\bconvenio\b', 'ES («convenio»)', None),
    (r'\bSMI\b', 'ES («SMI»)', None),
    (r'(?i)\baut[oó]nomo', 'ES («autónomo»)', None),
    (r'Veri\*?factu', 'ES («Veri*factu»)', None),
    (r'\bSGAE\b', 'ES («SGAE»)', None),
    (r'\bIAE\b', 'ES («IAE»)', None),
    (r'(?i)\bterrazas?\b', 'ES («terraza»)', None),
    (r'(?i)\bcomensal|\bpedidos?\b', 'ES («comensal / pedido» → covers, orders)', None),
    (r'(?i)\bcroquet|ensaladilla|\balioli\b|al ast\b', 'ES (guarniciones y corriente españolas: la carta US es la de US §1)',
     None),
    (r'\bEspaña\b|\bSpain\b|\bSpanish\b', 'ES («España/Spain»: la corriente española no cruza)', None),
    (r'\bVAT\b', 'ES («VAT» fuera de la nota UK)', r'\bUK\b|United Kingdom|HMRC'),
    # jerga trampa (US §9 y §10)
    (r'(?i)pollo asado', 'jerga: «pollo asado» en EE. UU. = pollo mexicano a la parrilla (El Pollo Loco), no sinónimo',
     r'(?i)Mexican|grilled|El Pollo Loco|' + _NO[4:]),
    (r'(?i)poultry (?:shop|store)', 'jerga: «poultry shop/store» = venta de pollo crudo, otra actividad', r'(?i)raw|' + _NO[4:]),
    (r'(?i)\broasters?\b', 'jerga: «roaster» = pollo grande, no el asador ni el negocio',
     r'(?i)roasters? (?:chickens?|birds?)|(?:larger|bigger|heavier) birds?'),
    (r'(?i)\byucca\b', 'jerga: «yuca fries» (no «yucca»)', None),
    (r'PERi-PERi|PERI-PERI', 'marca: «peri-peri» genérico (US §6.9)', None),
    (r'(?i)Inca Kola', 'marca: «soda» / «Peruvian golden soda» (genérico, revisión F2)', None),
    (r'(?i)\bbroaster', 'marca: «pressure-fried chicken» (Broaster es marca, US §6.9)', r'(?i)brand|trademark'),
    (r'(?i)chicken shop', '«chicken shop» solo en la nota UK (US §9)', r'\bUK\b|United Kingdom|British'),
    (r'(?i)\bAustralia', 'Australia solo en la FAQ de la landing (F1-camino §6)', None),
    # claims (US §9 y §6.5)
    (r'(?i)\bauthentic', 'claim («authentic»: US §9, nunca como promesa)', None),
    (r'(?i)gluten[- ]free', 'claim («gluten-free»: US §6.5, ni del pollo ni de las yuca fries)',
     r"(?i)21 CFR|\bnot\b|\bnever\b|cannot|can't|don't|do not|\bno\b"),
    (r'(?i)\bservers?\b|\bwaitstaff\b|\bwaiters?\b', 'counter service (sin servers, US §8)',
     r'(?i)no servers|without servers|no table service|counter service'),
    # unidades (REGLA_UNIDADES): kg, g, km, litros, °C y m² solo entre paréntesis
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


def _importes_research():
    """Importes en dólares ≥ 10,000 que cita la research US de la pollería: son datos de este producto y no se vetan
    aunque coincidan con un importe de otro caso EN."""
    out = set()
    p = os.path.join(AQUI, 'F1-research-us-delta.md')
    t = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    for m in re.finditer(r'\$\s?(\d{1,3}(?:,\d{3})+)(?:\s?[-–]\s?\$?(\d{1,3}(?:,\d{3})+))?', t):
        out |= {int(x.replace(',', '')) for x in m.groups() if x and int(x.replace(',', '')) >= 10000}
    out |= {int(x) * 1000 for x in re.findall(r'\$\s?(\d{2,3})K\b', t)}
    return out


# Datos federales US que coinciden con un importe del caso ES: no se vetan (el límite de los SBA Microloans, $50,000, =
# los 50.000 € de recursos propios del ES; GM c0552 y GR c0055 lo citan)
HECHOS_US = {50000}
# Constantes físicas que coinciden con un importe de otro caso EN: se vetan salvo en su contexto (revisión F2: el
# «1 therm = 100,000 BTU» de la calculadora casaba con los $100,000 del Taco EN)
EXCEPCION_CIFRA = {100000: r'(?i)\bBTU\b|\btherms?\b'}


def cifras_prohibidas(valores):
    """CIFRAS_PROHIBIDAS del conjunto. Fuera las cifras que coinciden con un valor del propio caso US o un dato federal."""
    propios = {int(round(x[0])) for x in valores.values() if isinstance(x[0], (int, float))} | HECHOS_US
    out = [(_num(n), 'cifra del caso ES de la pollería', None) for n in sorted(_cifras_es()) if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in _frases_es()]
    propios |= _importes_research()
    for path, plan, nombre in [(os.path.join(TAQ, 'cifras_caso.json'), 'taq', 'del Taco EN'),
                               (os.path.join(PIZ, 'cifras_caso.json'), 'piz', 'de la Pizza EN'),
                               (os.path.join(ICE, 'cifras_caso.json'), 'ice', 'de la Ice Cream EN'),
                               (os.path.join(BP2, 'cifras_caso.json'), 'pan', 'de la Bakery EN'),
                               (os.path.join(BAR, 'cifras_caso.json'), 'bar', 'del Bar EN'),
                               (os.path.join(BP, 'cifras_caso.json'), 'ft', 'del FT EN'),
                               (os.path.join(BP2, 'cifras_caso.json'), 'rest', 'del Restaurant EN')]:
        out += [(_num(n), 'cifra del caso %s (no se reutiliza)' % nombre, EXCEPCION_CIFRA.get(n))
                for n in _cifras_caso(path, plan) if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_OTROS]
    out += RX_POL_NO
    return out


# ==========================================================================
# Tokens del docx: los de FT/CAF con los rótulos de la pollería («Pedidos…») + partidas propias
# ==========================================================================
_CLIENTES = OrderedDict([
    ('Clientes/día (media del año 1)', 'Pedidos/día (media del año 1)'),
    ('Clientes/día (media)', 'Pedidos/día (media)'),
    ('Clientes/día', 'Pedidos/día'),
    ('Clientes necesarios al día', 'Pedidos necesarios al día'),
    ('Clientes necesarios al día (caja)', 'Pedidos necesarios al día (caja)'),
])
_DESC = OrderedDict([
    ('clientes_dia', 'average covers per day, year 1: dine-in + take-out/pickup and pre-orders + delivery (a family meal '
                     'counts as 3.5 covers)'),
    ('clientes_a2', 'average covers per day, year 2'),
    ('clientes_a3', 'average covers per day, year 3'),
    ('equilibrio_clientes_dia', 'break-even covers per day (accounting)'),
    ('equilibrio_caja_clientes_dia', 'cash break-even covers per day (loan payments in, depreciation out)'),
    ('pesimista_clientes', 'pessimistic scenario: covers per day'),
    ('optimista_clientes', 'optimistic scenario: covers per day'),
    ('alquiler_mes', 'rent per month (base rent of the premises)'),
    ('vida_obra', 'useful life of build-out, years'),
    ('ocupacion_anual', 'rent per year (occupancy)'),
    ('consumibles_pct', 'disposables (family-meal boxes, foil bags, sauce cups, heated-display bags), % of sales'),
])
_FUERA = ('inv_vehiculo', 'inv_adaptacion', 'inv_equipo_cocina', 'inv_generador', 'inv_permisos', 'inv_espresso',
          'inv_obra', 'inv_instalaciones', 'inv_mobiliario', 'inv_barra', 'inv_terraza', 'inv_lanzamiento',
          'inv_stock', 'aforo', 'rotaciones_dia')


def _inv(rot, desc):
    return ('usd', ('fila', _I, {'pol': rot}, 'B'), desc)


def _como_excel(v, decimales):
    """Redondeo que se VE en Excel: 15 cifras significativas y luego mitad hacia arriba (no al par como `format`)."""
    from decimal import Decimal, ROUND_HALF_UP
    return float(Decimal('%.15g' % v).quantize(Decimal(1).scaleb(-decimales), rounding=ROUND_HALF_UP))


TOKENS_PROPIOS = OrderedDict([
    ('inv_proyecto', _inv('Proyecto técnico de actividad y de salida de humos, y dirección de obra',
                          'architect, MEP & hood drawings, plan review and permit fees')),
    ('inv_obra', _inv('Obra y acondicionamiento del local, rótulo y fachada',
                      'build-out of a second-generation space (1,600 sq ft), signage and facade')),
    ('inv_campana', _inv('Conducto de extracción exclusivo hasta cubierta',
                         'Type I hood (about 14 ft), UL 300 fire suppression and makeup air')),
    ('inv_instalaciones', _inv('Instalación eléctrica trifásica, cuadro y boletín', 'electrical service, panel and gas lines')),
    ('inv_fontaneria', _inv('Fontanería, separador de grasas, climatización e instalación de gas',
                            'plumbing, grease interceptor and HVAC')),
    ('inv_rotisseries', _inv('Asador de pollos de gas de doce espadas y juego de espadas',
                             'two commercial gas rotisseries (8 spits, 48 birds per load each)')),
    ('inv_display', _inv('Vitrina caliente de mostrador y mantenedor de patatas',
                         'heated display merchandiser, steam table and holding cabinet')),
    ('inv_freidora', _inv('Freidora doble y fogón', 'two 50 lb fryers and a range with stock-pot burners')),
    ('inv_camara', _inv('Campana extractora con motor y filtros', 'walk-in cooler (6×8)')),
    ('inv_frio', _inv('Frío: armarios de pollo crudo y adobado, congelador y vitrina refrigerada',
                      'refrigerated prep table and reach-in freezer')),
    ('inv_lavado', _inv('Lavavajillas de capota, fregaderos, lavamanos y mesas inox de espetar',
                        '3-compartment sink, dish machine, hand and poultry prep sinks, shelving and stainless')),
    ('inv_utillaje', _inv('Utillaje: sondas, básculas, GN, tijeras de trinchar, etiquetadora y vajilla',
                          'smallwares and sauce station (spare spits, hotel pans, probes, blender, marinating tubs)')),
    ('inv_bebida', _inv('Botellero y nevera de bebida para llevar', 'beverage cooler and ice machine')),
    ('inv_mobiliario', _inv('Mobiliario de sala', 'furniture (40 seats)')),
    ('inv_tpv', _inv('TPV con Veri*factu, datáfono, impresora y tablet de plataformas',
                     'POS, online ordering, kiosk and delivery tablets')),
    ('inv_constitucion', _inv('Constitución de la SL, licencia, tasas, registro sanitario y APPCC',
                              'LLC, legal and food safety plan')),
    ('inv_lanzamiento', _inv('Marca, web, fotos y lanzamiento', 'branding, website, photos and launch')),
    ('inv_stock', _inv('Stock inicial: pollo, patata, aceite, envases y bebida', 'opening inventory')),
    ('aforo', ('int', ('fila', _S, {'pol': 'Aforo de la sala (plazas sentadas)'}, 'B'), 'indoor seats')),
    ('comida_pct', ('pct0', ('fila', _S, {'pol': 'Ventas de COMIDA sobre el total'}, 'B'), 'food share of sales')),
    ('bebida_pct', ('pct0', ('fila', _S, {'pol': 'Ventas de BEBIDA sobre el total'}, 'B'), 'beverage share of sales')),
    ('plataforma_pct', ('pct0', ('fila', _S, {'pol': 'Ventas por delivery sobre el total'}, 'B'),
                        'share of sales through third-party delivery marketplaces')),
    ('comision_pct', ('pct0', ('fila', _S, {'pol': 'Comisión de la plataforma de delivery'}, 'B'),
                      'marketplace commission on those orders')),
    ('marketing_anual', ('usd', ('fila', _P, {'pol': 'Marketing y publicidad'}, 'B'), 'marketing budget per year')),
    ('prime_cost_pct', ('pct1', ('deriv', lambda c: c['cogs_pct'] + c['personal_pct']),
                        'prime cost year 1 (cost of goods + labor, % of sales)')),
    ('meses_alquiler_previo', ('int', ('fila', _S, {'pol': 'Meses de alquiler ANTES de abrir (obra y licencias)'}, 'B'),
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


def tokens_pol(base):
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
            src = ('fila', hoja, {'pol': rot}, col)
        if t == 'consumibles_pct':
            fmt = 'pct1'
        out[t] = (fmt, src, _DESC.get(t, desc))
    out.update(TOKENS_PROPIOS)
    return out


# ==========================================================================
# Docx: lo que escribe ensamblar_docx.py (índices del Word ES de 131 párrafos = Taco) y las notas por ranura
# ==========================================================================
# Productos del cierre: solo los que EXISTEN en la tienda EN (tienda.ts, 29-oct; lección M2 del Taco EN): no hay guía de
# restaurante peruano ni checklists de pollería en EN
PRODUCTOS_CIERRE_POL = ['Food Cost Kit Pro', 'HACCP Food Safety Kit Pro', 'Restaurant Checklists Kit Pro',
                        'Food Truck Business Plan Kit']


def docx_fijos(M):
    pc = PRODUCTOS_CIERRE_POL
    d = OrderedDict([
        (6, 'BUSINESS PLAN'), (7, 'Rotisserie Chicken Restaurant'),
        (9, 'Complete financial plan, market analysis,\noperations strategy and startup checklist\nto open a '
            'Peruvian-style rotisserie chicken restaurant in the United States'),
        (14, 'AI Chef Pro'), (15, 'aichef.pro'), (16, 'US edition with UK notes · 2026'),
        (18, 'LEGAL NOTICE'), (19, M.AVISO_DOCX_EN), (20, '© 2026 AI Chef Pro — aichef.pro'), (22, 'CONTENTS'),
        (35, 'Appendices: Rotisserie Chicken Restaurant Financial Projections (Excel) + Rotisserie Chicken Yield & Costing '
             'Calculator (Excel) + Rotisserie Chicken Restaurant Startup Checklist (Excel) + Equivalents Guide'),
        (123, 'AI Chef Pro'), (124, 'Templates and AI tools for food businesses'),
        (126, 'aichef.pro\ninfo@aichef.pro'),
        (127, '→ %s · %s' % tuple(pc[:2])), (128, '→ ' + pc[2]), (129, '→ ' + pc[3] + ' (for a rotisserie chicken truck)'),
        (130, '\n' + M.URL_TIENDA),
    ])
    return OrderedDict([('pol', d)])


DOCX_NOTAS_PLAN = OrderedDict([
    ('pol', 'Concepto (US §1): COUNTER-SERVICE ROTISSERIE CHICKEN RESTAURANT de barrio, estilo peruano (pollo a la brasa), '
            'en una ciudad media de EE. UU. (150-300 mil hab.), ~1,600 sq ft, {{aforo}} plazas, pedido en mostrador (sin '
            'servicio de mesa), pickup propio y family meals, pre-orders y party trays (cumpleaños, iglesias, oficinas), '
            'marketplaces; DOS commercial rotisseries de GAS de 8 espadas (48 pollos por carga cada una) a la vista desde '
            'la calle, 2 freidoras, fogones, heated display para los pollos enteros to-go y walk-in para el marinado de '
            '24-48 h. Carta: quarter (dark/white), half y whole chicken con 2 sides, family meal, sandwich/bowl de pollo '
            'deshilachado; sides yuca fries, fries, rice & beans, maduros, house salad, salchipapas; salsas aji verde, aji '
            'amarillo, huancaina; Inca Kola, chicha morada, sodas y beer & wine. ABRE 7 DÍAS (360; el domingo es el pico). '
            'El dueño es el GM y jefe de rotisserie. Nombre: «rotisserie chicken restaurant»; «Peruvian chicken» y «pollo '
            'a la brasa» en prosa; NUNCA «poultry shop/store» (es venta de pollo crudo), «roaster» (es un pollo grande), '
            '«PERi-PERi» ni «Broaster» (marcas: «peri-peri», «pressure-fried chicken»), ni «authentic» como promesa. '
            '«Pollo asado» en EE. UU. es el pollo MEXICANO a la parrilla (El Pollo Loco): solo para decir lo que este plan '
            'NO es, nunca como sinónimo. El ES llama «pedido» a la unidad de venta; el EN dice «covers» (una family meal = '
            '3.5 covers) y «orders» solo para pre-orders y pickup. Cada cifra del caso va con su token {{…}}; las de '
            'mercado solo si están en la research con fuente. Lo ES que NO cruza (IVA partido, RD 1021/2022 arts. 4.1 y 9, '
            'RD 1086/2020 art. 30, RD 126/2015, ordenanza de humos, IAE, convenio, SMI, 14 pagas, Leyes 1/2025 y 7/2022, '
            'Veri*factu, la corriente española del pollo al ast, las croquetas y la ensaladilla) se SUSTITUYE por US §6 o '
            'se quita. Gas en el caso; CARBÓN = variante (NFPA 96). Australia NO va en el Word (solo en la FAQ de la '
            'landing). No cites productos que no estén en el cierre (no hay guía de restaurante peruano en inglés). '
            'Honestidad del margen: neto {{margen_neto_a1}}. Fuera: food truck (→ Food Truck Business Plan Kit), '
            'franquicias (El Pollo Loco, Pollo Tropical), fried chicken / wings, venta de pollo crudo, kioscos de '
            'supermercado. Glosario US §9 obligatorio. El cierre (productos) lo escribe el ensamblador. ' + REGLA_UNIDADES),
])

_FORMA = ('FORMA: la sección §%d del Taco EN (business-plans-en-12/docx_en_taq_%s.json) da el registro y la longitud; '
          'su vocabulario de taquería (taco, trompo, tortilla, salsa bar, patio, «closed Mondays»…) y sus cifras NO valen')
_SEC = OrderedDict([
    (1, ('a', 'Resumen ejecutivo: concepto (US §1), la oportunidad (US §2-§3: «pollo a la brasa» y «peruvian chicken» '
              '≈ 40,500 búsquedas/mes cada una y «peruvian chicken restaurant» 2,900 = demanda de CONSUMO; las colas de '
              '«rotisserie chicken restaurant business plan» son pequeñas: no las cites como mercado), inversión y '
              'financiación SOLO con tokens ({{inversion_total}}, {{capex}}, {{prestamo}} SBA 7(a) {{tipo_prestamo}} a '
              '{{plazo_prestamo}} años), ventas ({{ventas_a1}}, {{clientes_dia}} covers × {{ticket}} × {{dias}} días), '
              'neto {{margen_neto_a1}} y DSCR {{dscr_min}}')),
    (2, ('a', 'Concepto y propuesta (ES ¶46-¶47 adaptados): el formato elegido frente a otros (solo-para-llevar de fin de '
              'semana; restaurante peruano de sala con horno de carbón = otro plan, SIN citar producto); las CINCO '
              'corrientes que el cliente US trae en la cabeza: (1) Peruvian pollo a la brasa = el caso (marinado de 24-48 h '
              'con soy sauce, cerveza, ajo, comino, aji panca, huacatay y vinagre; papas o yuca fries, ensalada y salsas '
              'aji verde / aji amarillo / huancaina; nació hacia 1950 en Lima); (2) peri-peri (chile africano a la '
              'portuguesa, en minúscula, sin marcas); (3) charcoal chicken (el mismo pollo sobre carbón vegetal: la '
              'identidad del asador limeño, aquí variante de combustible sólido); (4) la rotisserie francesa (poulet rôti '
              'en espadas horizontales, patatas en los jugos); (5) el pollo en brasa venezolano con guasacaca. «Pollo asado» '
              '= mexicano a la parrilla (El Pollo Loco), NO sinónimo. Sin «authentic»')),
    (3, ('a', 'Mercado y competencia: US §2, §5.1 y §7 (ciudad media: quarter + 2 sides $10-13, half + 2 $16-18, family '
              'meal $31-34 = Kit estimate de una lectura de menús; Mister Pio $59 el entero = outlier premium; cadenas como '
              'El Pollo Loco o Boston Market no son el modelo del comprador); el pollo asado del supermercado es el ancla '
              'de precio del cliente (sin cifra): se compite en marinado, salsas y sides; sin datos de mercado sin fuente')),
    (4, ('a', 'Cliente y posicionamiento: familias, comida y cena, pickup y pre-orders fuertes, domingo = pico (≈ 1.6-1.8 '
              '× un día laborable, Kit); el check de {{ticket}} por cover equivalente (platos + sides extra + salsas + '
              '0.65 bebidas, US §8; la family meal cuenta como 3.5 covers); el pickup directo (0 % de comisión) frente a '
              'los marketplaces')),
    (5, ('a', 'Marketing y ventas: Google Business Profile, Yelp, Instagram (las espadas girando venden en vídeo); fechas: '
              'Mother\'s Day, Super Bowl Sunday, Nochebuena y Nochevieja en las familias latinas, Pollo a la Brasa Day '
              '(tercer domingo de julio) y Fiestas Patrias (28 de julio) en la comunidad peruana; pre-orders con franja de '
              'recogida y depósito; marketplaces DoorDash / Uber Eats / Grubhub con sus tiers (US §5.2); el caso pone '
              '{{plataforma_pct}} de las ventas al {{comision_pct}}; el pollo viaja bien en envase ventilado, las fries '
              'no: radio corto')),
    (6, ('b', 'Operaciones y equipo: dos rotisseries de gas ({{inv_rotisseries}}), heated display ({{inv_display}}), '
              'freidoras y fogones ({{inv_freidora}}), Type I hood + UL 300 + makeup air ({{inv_campana}}), walk-in '
              '({{inv_camara}}) para el pollo crudo y el marinado; marinado la víspera, primera carga a las 9:00, 48 pollos '
              'por carga (8 espadas × 6) de 75-90 min (Kit); domingo 65-70 pollos y días punta 120-150 con pre-orders; '
              'cooked yield 70-75 % (Kit: mídelo con la calculadora). «EVERY BIRD COUNTS» (US §8): el pollo marinado '
              'cuesta $5.99; uno que pasa su ventana de 4 h y se tira cuesta $5.99, uno enfriado con registro para '
              'sandwich/bowl ($13.50, 5 oz) vale ≈ $2.70 de producto → cargar por franjas con el histórico del POS + '
              'pre-orders, nunca «llenar el asador por si acaso»; merma ≤ 5 % de los pollos cargados. Variantes: carbón '
              '(NFPA 96; rotisserie listada $27,500-35,950 + escape propio: +$45,000-60,000 de CAPEX) y ventless solo para '
              'la rotisserie (las freidoras siguen bajo Type I)')),
    (7, ('b', 'Organización y personal: Owner / GM & head of rotisserie, rotisserie cook, counter lead / cashier, counter, '
              'packing & expo part-time W-2 (4), dish & prep, fry & line cook de fin de semana y el prep & relief '
              'rotisserie cook que cubre los descansos ({{plantilla_puestos}} personas = {{plantilla_jornadas_xl}} FTE; 7 '
              'días piden más FTE que un local que cierra un día); ≥ $15/h, propinas del mostrador para el equipo (no para '
              'el dueño), sin tip credit modelado; employer payroll taxes {{cargas_pct}}; el dueño se paga por debajo de '
              'un manager: «draw in addition from net profit»')),
    (8, ('b', 'Plan financiero: TODO con tokens (ventas años 1-3, mezcla {{comida_pct}}/{{bebida_pct}}, COGS '
              '{{cogs_pct_xl}}, personal {{personal_pct}}, prime cost {{prime_cost_pct}}, alquiler {{ocupacion_pct}}, '
              'EBITDA, neto, equilibrio {{equilibrio_clientes_dia}} / {{equilibrio_caja_clientes_dia}} covers/día, holgura '
              '{{holgura_caja_pct}}, DSCR {{dscr_min}}, saldo mínimo {{saldo_minimo}}, escenarios); el precio del pollo es '
              'volátil (composite USDA, rango regional 88-149 ¢/lb, resumen) y la merma de display mueve el food cost: '
              'dilo sin cifra inventada; food & paper del caso frente al 24.5 % de una cadena con escala de compra (El '
              'Pollo Loco, resumen)')),
    (9, ('b', 'Marco legal US (ver las notas propias de cada ranura de §9)')),
    (10, ('b', 'Hoja de ruta: el orden del checklist (80 tareas en 6 fases: setup; hood, gas & permits; rotisseries & '
               'health; staff & allergens; menu & pre-orders; opening & 90 days); la beer & wine license se pide al firmar '
               'el local; las reglas de tu condado para el pollo y el hot holding por escrito ANTES de comprar el display; '
               'el holiday pre-order plan antes del primer Mother\'s Day; cierre con el Excel, la calculadora de '
               'rendimiento y coste del pollo y el checklist')),
])
_RANURAS = OrderedDict([(1, range(39, 44)), (2, range(46, 51)), (3, range(53, 59)), (4, range(61, 67)),
                        (5, range(69, 76)), (6, range(78, 83)), (7, range(85, 91)), (8, range(93, 100)),
                        (9, range(102, 109)), (10, range(111, 118))])
_N9 = OrderedDict([
    (102, '§9 1/7: el marco US por niveles (federal, estatal, condado, ciudad); LLC + EIN; sales tax permit; business '
          'license; zoning check ANTES de firmar; plan review (Food Code 8-201.11) + building permit → certificate of '
          'occupancy; fire marshal; sales tax {{sales_tax}} de ejemplo, un solo tipo («some states tax to-go food '
          'differently», sin cifra)'),
    (103, '§9 2/7: campana, gas y fuego: Type I hood + supresión UL 300 sobre rotisseries y freidoras; makeup air; grease '
          'interceptor; limpieza de campana trimestral (NFPA 96, Tabla 11.4: combustible sólido, mensual); dos '
          'rotisseries de ≈ 177,500 BTU + freidoras → acometida y regulador de gas dimensionados, con permiso; ventless '
          'solo con equipo listado con su campana; CARBÓN = combustible sólido (NFPA 96 cap. 14: escape propio, '
          'arrestachispas, ceniza mojada a diario en contenedor metálico, ≤ 1 día de combustible junto al aparato), '
          'aparato listado (UL/ETL) y NSF/ANSI 4; los asadores importados de Perú pueden no tener listing; reglas de '
          'calidad del aire: «ask your air district»'),
    (104, '§9 3/7: health permit + inspección previa; Certified Food Protection Manager (2-102.12) + food handler cards '
          'según estado; FDA Food Code 2022 (cada estado adopta su edición): aves a 165 °F (3-401.11); hot holding ≥ 135 '
          '°F (3-501.16); cooling 135 → 70 °F en 2 h y → 41 °F en 6 h en total (3-501.14); reheating para hot holding a '
          '165 °F (3-403.11); pollo con inspección USDA (approved source); pollo crudo abajo en el walk-in, tablas por '
          'color, no lavar el pollo crudo'),
    (105, '§9 4/7: el SOP del heated display: TPHC (3-501.19) hasta 4 h con la hora marcada y procedimiento escrito; a '
          'las 4 h o si baja de 135 °F, se enfría con registro para el sandwich/bowl del día siguiente o se tira; nunca '
          'vuelve al display sin pasar por 165 °F; pollos envasados en autoservicio: etiqueta (3-602.11); rice & beans = '
          'TCS (B. cereus): hot holding ≥ 135 °F; «keep a rotisserie chicken warm for 2 hours» → ≥ 135 °F o TPHC con SOP'),
    (106, '§9 5/7: alérgenos: 9 mayores US incluido el sésamo (FASTER Act); marinado = soy sauce (soy + wheat) + cerveza '
          '(wheat/barley); aji verde a menudo con mayonesa (egg) y queso fresco o cotija (milk), según receta; huancaina = '
          'queso fresco y leche evaporada (milk) + galletas saladas (wheat); pan del sandwich = wheat (sesame si lleva '
          'semillas); freidora compartida con empanados → contacto cruzado; «gluten-free»: 21 CFR 101.91, NO se promete '
          'ni del pollo ni de las yuca fries'),
    (107, '§9 6/7: beer & wine license (agencia estatal + aprobación local; coste y plazos muy distintos: «apply early», '
          'NO prometer licencia); liquor liability en el seguro ({{seguros_anual}} con general liability, property y '
          'workers\' comp); personal: W-2 por horas (nada de 1099 para cocineros o cajeros), I-9, W-4, salario mínimo '
          'estatal (federal $7.25/h, DOL), propinas del equipo; música ASCAP/BMI/SESAC; packaging ordinances locales; '
          'nombres: «peri-peri» genérico (nunca «PERi-PERi») y «pressure-fried chicken» («Broaster» es marca)'),
    (108, '§9 7/7: venta desde casa: las cottage food laws no cubren el pollo cocinado (TCS): este plan es de local con '
          'permiso («check your state»); y, como ÚLTIMA frase o frases, la NOTA UK: registro del food business en el '
          'council 28 días antes, FHRS 0-5, VAT 20 % en comida caliente (también para llevar), 14 alérgenos (apio y '
          'mostaza en los marinados, sulfitos, altramuces), premises + personal licence para el alcohol; «chicken shop» '
          'solo aquí. Sin Australia (va en la FAQ de la landing)'),
])


def _notas_docx():
    out = OrderedDict()
    for s, filas in _RANURAS.items():
        tanda, nota = _SEC[s]
        for k, i in enumerate(filas, 1):
            n = _N9.get(i) or ('§%d %d/%d: %s' % (s, k, len(filas), nota))
            out[i] = n + ' ‖ ' + _FORMA % (s, tanda)
    return out


DOCX_NOTAS = OrderedDict([('pol', _notas_docx())])

# ==========================================================================
# Pistas por celda (extraer_textos.py → textos_es.json → tandas)
# ==========================================================================
_CASO = ('US §8: caso US = 130 covers/día equivalentes (≈ 55 en sala, 40 plazas; ≈ 55 take-out/pickup y pre-orders; ≈ 20 '
         'por marketplace; una family meal = 3.5 covers) × $17.50 (sin sales tax ni propina) × 360 días (abre 7 días); '
         'counter service; beer & wine; sin cifras del ES ni historia de versiones')
CELDA_PISTAS = OrderedDict([
    (('POLP', _S, 'A2'), 'D8: añade una vez que los importes van «in your currency» (sin símbolo)'),
    (('POLP', _S, 'C4'), _CASO + '; media del año 1 con la rampa de apertura; compárala con el paso de gente de tu calle y '
                                 'con tus pre-orders de prueba'),
    (('POLP', _S, 'C5'), _CASO + '; check de $17.50 por cover = platos $12.79 (quarter + 2 sides $13.00 × 0.35, half + 2 '
                                 '$17.50 × 0.15, family meal $34 ÷ 3.5 × 0.30, sandwich/bowl $13.50 × 0.20) + sides '
                                 'extra $1.50 + postre $0.36 + salsas $0.30 + 0.65 bebidas × $3.84 (Kit estimate, US §8); '
                                 'el precio con impuesto lo calcula la fila "Menu price incl. sales tax"'),
    (('POLP', _S, 'C6'), _CASO + '; 360 días = abre 7 días; cierra Thanksgiving, Christmas Day y New Year\'s Day + 2 días de '
                                 'limpieza a fondo de la campana y las rotisseries'),
    (('POLP', _S, 'C13'), 'US §4: food cost 29 % (family meal 29.6 %, quarter + 2 sides 28.8 %, half + 2 sides 30.0 %, '
                          'sandwich/bowl ≈ 21 %; pollo de 3.0 lb a $1.75/lb + marinado + 5 % de merma de display = $5.99; '
                          'Kit estimate); la calculadora del kit da el coste de cada pollo y de cada plato'),
    (('POLP', _S, 'C14'), 'US §8: beverage cost 22 % (sodas, Inca Kola, chicha morada hecha en casa, beer & wine)'),
    (('POLP', _S, 'C15'), 'US §8: disposables 4 % (cajas de family meal, bolsas de aluminio, sauce cups, bolsas del heated '
                          'display; packaging ordinances locales)'),
    (('POLP', _S, 'C16'), 'US §8: 15 % de las ventas por marketplaces (DoorDash, Uber Eats, Grubhub); el pickup directo y '
                          'los pre-orders por teléfono o web no pagan comisión'),
    (('POLP', _S, 'C17'), 'US §5.2: 25 % = plan Plus de DoorDash / Uber Eats (Basic 15 %, Premier 30 %; + 6-10 % en pickup '
                          'por la app); compruébalo en tu contrato'),
    (('POLP', _S, 'C24'), 'US §8: $3,733/mes = 1,600 sq ft × ~$28/sq ft/año (Kit estimate, editable)'),
    (('POLP', _S, 'C26'), 'US §8: $1,800/mes (gas de las 2 rotisseries y las freidoras, walk-in, campana, HVAC; tarifa de '
                          'gas comercial sin fuente: Kit estimate)'),
    (('POLP', _S, 'C27'), 'US §8: $6,500/año = general liability + liquor liability (beer & wine) + property + workers\' '
                          'comp (Kit estimate)'),
    (('POLP', _S, 'C31'), 'US §8: SBA 7(a) al 10 % a 10 años, sin interest-only; el préstamo lo calcula "Financing"'),
    (('POLP', _S, 'C51'), 'US §1: 40 plazas en sala (sin patio)'),
    (('POLP', _N, 'A8'), 'SPEC §4.1 línea 4 (Bar): sin divisores 1,10/1,21 → «divide a menu price by 1 + your sales tax '
                         'rate»; P&L excl. sales tax, cash flow incl.; un solo tipo en el ejemplo (B39 = B40 = 8 %)'),
    (('POLP', _N, 'A10'), 'F1-camino §6: Mes 1 = ENERO, en el orden del calendario (curva plana; enero-febrero flojos; mayo, '
                          'julio y diciembre, los picos)'),
    (('POLP', _N, 'A12'), 'El Word cita las cifras de este Excel (si cambias el libro, manda el Excel); la calculadora de '
                          'rendimiento y coste del pollo va aparte y su food cost por pollo NO se copia en "0. '
                          'Assumptions" (allí va el food cost medio de toda la carta)'),
    (('POLP', _P, 'F10'), 'US §8: platos de pollo, family meals y sides: ≈ 42 % en sala, ≈ 42 % pickup y pre-orders y '
                          '≈ 15 % por marketplaces; un solo sales tax en el ejemplo'),
])
for _f, _nota in [(7, 'US §4: plan review y permit fees; la beer & wine license cambia mucho de un estado a otro '
                      '(pregunta a tu agencia estatal; sin cifra); sin licencia ni declaración responsable españolas'),
                  (8, 'US §8: local de segunda generación (ya fue restaurante) de 1,600 sq ft; incluye signage & facade '
                      '($5,000 de las 19 partidas de US §8: la rotisserie a la vista desde la calle)'),
                  (9, 'US §4: Type I hood de ≈ 14 ft + supresión UL 300 + makeup air (rango $5,000-28,000; el caso, '
                      '$26,000) sobre 2 rotisseries, 2 freidoras y fogones; NADA de la ordenanza de Madrid'),
                  (10, 'US §8: parte de «electrical, HVAC, plumbing, gas lines & grease interceptor» ($24,000 en total); '
                       'dos rotisseries de ≈ 177,500 BTU piden acometida y regulador de gas dimensionados (permiso de '
                       'gas); pregunta el servicio eléctrico disponible ANTES de firmar'),
                  (11, 'US §4: grease interceptor $3,500-7,500 (REST §3) + HVAC; la otra parte de los $24,000 de US §8'),
                  (12, 'US §4: dos rotisseries de gas de 8 espadas (Pegasus CR-8G, retail $6,011, 48 pollos por carga: '
                       'webstaurantstore, oct-2026); el caso pone $13,000 con flete e instalación; eléctrica (Alto-Shaam '
                       'AR-7E $11,912) y carbón (J&R $27,500-35,950) = variantes'),
                  (13, 'US §4: heated display (Avantco HDC-48 $599 … Alto-Shaam ED3-72 $11,207) + steam table + holding '
                       'cabinet; mantiene ≥ 135 °F; sin «mantenedor de patatas» como partida'),
                  (14, 'US §4: dos freidoras de 50 lb (Avantco FF50 $799 … Pitco 65C+S $1,848) para yuca fries y fries + '
                       'fogones para rice & beans, salsas y chicha morada'),
                  (15, 'OJO: la nota ES habla de la campana, que en el caso US va en la fila 9: aquí escribe la del '
                       'walk-in cooler 6×8 (Norlake Kold Locker $12,808, webstaurantstore): el pollo crudo y el marinado '
                       'de 24-48 h'),
                  (16, 'US §8: prep table refrigerada + congelador vertical (yuca congelada); sin vitrina refrigerada de '
                       'guarniciones (Kit estimate)'),
                  (17, 'US §8: 3-comp sink, lavavajillas, lavamanos y un fregadero aparte para preparar el pollo crudo, '
                       'estanterías e inox (el crudo, separado de lo que se sirve)'),
                  (18, 'US §8: espadas de recambio, hotel pans, sondas, tablas por color, estación de empaquetado + '
                       'estación de salsas (licuadora, biberones, portion cups) y tinas de marinado; sin etiquetadora '
                       'española'),
                  (19, 'OJO: la nota ES habla del botellero que cede la cervecera: aquí, beverage cooler y máquina de hielo '
                       '(Kit estimate; si el distribuidor presta la nevera, baja)'),
                  (20, 'US §1: 40 plazas en sala, sin patio ni barra'),
                  (24, 'US §8: pollo, yuca, aceite, marinado, salsas, bebida (beer & wine) y envases para llevar')]:
    CELDA_PISTAS[('POLP', _I, 'D%d' % _f)] = _nota
for _f in range(7, 25):
    CELDA_PISTAS.setdefault(('POLP', _I, 'D%d' % _f), 'Nota de la partida del ejemplo US (rótulo fijado de la col. A en '
                                                       '"fijos_en"); sin marcas ni normas españolas: solo rangos con '
                                                       'fuente de US §4 o ninguno')
# Tabla D19 (Instrucciones 35-46, 12 filas como el ES): «US ROTISSERIE CHICKEN BENCHMARKS (sourced) AND KIT ESTIMATES»
# (Benchmark | Value | Source | Note). Cada fila sustituye a la ES de la misma fila; solo lo «leído» con fuente; lo
# «(resumen)» = Kit estimate
_D19 = OrderedDict([
    (35, 'fila → «Month 1 of the plan» · «January» · «Plan decision» · nota: orden del calendario; curva plana (comida de '
         'diario); enero-febrero flojos; mayo, julio y diciembre, los picos; si abres en otro mes, gira la fila de '
         '"12-Month Cash Flow"'),
    (36, 'fila (sustituye el mercado español) → «Consumer demand (US searches)» · «"pollo a la brasa" and "peruvian '
         'chicken" about 40,500 a month each; "peruvian chicken restaurant" 2,900» · «DataForSEO, US, Oct 2026» · nota: '
         'demanda de consumo, no de compradores del plan'),
    (37, 'fila → «Family meal (whole chicken + 2 large sides)» · «$31-34 in mid-size cities (quarter + 2 sides $10-13; '
         'half + 2 sides $16-18)» · «Kit estimate (menu scan, Oct 2026)» · nota: este plan, quarter $13.00, half $17.50, '
         'family meal $34.00'),
    (38, 'fila → «Cost of a marinated bird» · «about $5.99 (3.0 lb at $1.75/lb + marinade + 5% holding shrink); family '
         'meal ≈ 30% of its price» · «Kit estimate (Rotisserie Chicken Yield & Costing Calculator)» · nota: pon el precio '
         'de tu distribuidor; el composite USDA de pollo entero varía por región'),
    (39, 'fila → «Cooked yield of a whole chicken» · «about 70-75%» · «Kit estimate (no manufacturer data)» · nota: mide '
         'el tuyo con la calculadora (peso crudo, peso asado)'),
    (40, 'fila → «Commercial gas rotisserie, 8 spits» · «$6,011 retail (48 birds per load); 5 spits $4,530» · '
         '«webstaurantstore.com (Pegasus CR-8G, CR-5G), read Oct 2026» · nota: el caso cuenta dos; de carbón, listada, '
         '$27,500-35,950 (J&R) = variante de combustible sólido (NFPA 96)'),
    (41, 'fila → «Delivery marketplace commission» · «DoorDash 15 / 25 / 30% + 6% pickup; Uber Eats 15-30%» · '
         '«merchants.ubereats.com; DoorDash tiers (Oct 2026)» · nota: este plan, 25 % sobre el 15 % de las ventas; el '
         'pickup directo y los pre-orders no pagan comisión'),
    (42, 'fila (sustituye el IVA del pollo asado) → «Sales tax» · «8% (example: state + local)» · «Kit example: look up '
         'your state and city rate» · nota: un solo tipo en el libro; algunos estados gravan distinto la comida para '
         'llevar'),
    (43, 'fila (sustituye la norma española de comidas preparadas) → «Cook, hold, cool and reheat» · «poultry 165 °F; hot '
         'holding ≥ 135 °F; cool 135 → 70 °F in 2 h and → 41 °F within 6 h; reheat for holding to 165 °F» · «FDA Food Code '
         '2022 (3-401.11, 3-501.16, 3-501.14, 3-403.11)» · nota: cada estado adopta su edición'),
    (44, 'fila (sustituye la mayonesa y las cremas) → «Time as a public health control (display)» · «up to 4 h with the '
         'time marked and a written procedure, then discard» · «FDA Food Code 2022 (3-501.19)» · nota: cada carga sale '
         'con su hora; lo que no se vende se enfría con registro o se tira'),
    (45, 'fila (sustituye el SMI) → «Minimum wage» · «federal $7.25/h + your state» · «U.S. Department of Labor '
         '(dol.gov)» · nota: este plan presupuesta ≥ $15/h; teclea el suelo de tu estado en "0. Assumptions"'),
    (46, 'fila (sustituye el convenio) → «Labor cost / sales» · «25-35% (a chicken chain: about 31%)» · «UpMenu '
         '(upmenu.com); El Pollo Loco Q2-2025 (summary)» · nota: 7 días de apertura lo suben; counter service lo baja'),
])
for _f, _p in _D19.items():
    for _col in 'ABCD':
        CELDA_PISTAS[('POLP', _N, '%s%d' % (_col, _f))] = _p

# Pistas por TEXTO propias de la pollería (se suman a las de extraer_textos.PISTAS): US §6 y §9
PISTAS_EXTRA = [
    (r'[Pp]edido|[Cc]omensal|[Cc]ubierto', 'US §8: el caso cuenta «covers» (130 equivalentes; una family meal = 3.5 '
                                           'covers); «orders» solo para pre-orders y pickup orders; nunca «customers» '
                                           'para el volumen diario'),
    (r'[Pp]oll(?:er[ií]a|o asado)|[Aa]sador', 'US §9: «rotisserie chicken restaurant» (negocio), «commercial rotisserie» '
                                              '(equipo), «rotisserie chicken» (producto); NUNCA «poultry shop», «roaster» '
                                              'ni «pollo asado» (en EE. UU. = pollo mexicano a la parrilla)'),
    (r'[Ee]spada|[Cc]arga|[Tt]anda|[Ee]spet', 'spit · load · spitting (8-spit rotisserie, 48 birds per load)'),
    (r'[Vv]itrina|[Mm]antenedor|63 ?°C|[Cc]aliente', 'heated display (merchandiser) · hot holding ≥ 135 °F · TPHC 4 h con '
                                                     'procedimiento escrito (US §6.1)'),
    (r'[Bb]rasa|[Cc]arb[oó]n|[Ll]eña', 'charcoal (lump/hardwood) · charcoal-fired · NFPA 96 solid fuel: variante, no el '
                                       'caso'),
    (r'[Ee]ncargo', 'pre-orders · party trays · catering orders (franja de recogida y depósito)'),
    (r'[Mm]en[uú] familiar|[Mm]edio pollo|[Cc]uarto|[Mm]uslo|[Pp]echuga', 'family meal (whole + 2 large sides) · half · '
                                                                           'quarter (dark = leg & thigh / white = breast '
                                                                           '& wing)'),
    (r'[Gg]uarnici|[Pp]atatas?|[Cc]roquet|[Ee]nsaladilla|[Pp]imientos', 'sides: yuca fries, fries, rice & beans, '
                                                                        'maduros, house salad, salchipapas (sin '
                                                                        'croquetas ni ensaladilla: carta US §1)'),
    (r'[Aa]lioli|[Mm]ayonesa|[Ss]alsas?|[Cc]remas?', 'aji verde · aji amarillo · huancaina · rocoto (sin tildes); '
                                                     'alérgenos egg / milk / wheat según receta'),
    (r'[Aa]dob|[Mm]acera|[Mm]arinad', 'marinade · marinated 24-48 hours (soy sauce, beer, garlic, cumin, aji panca, '
                                      'huacatay, vinegar): soy + wheat'),
    (r'[Rr]endimiento|[Mm]erma', 'cooked yield (70-75 %, Kit) · shrink / holding waste («Every bird counts»: ≤ 5 % de los '
                                 'pollos cargados)'),
    (r'[Mm]olleja|[Hh][ií]gado|[Mm]enudill', 'giblets: el caso compra WOG (without giblets)'),
    (r'[Pp]iri|[Cc]hurrasq|[Pp]ortugu', 'peri-peri (genérico, minúscula; nunca «PERi-PERi»)'),
    (r'[Vv]enezol|guasacaca', 'Venezuelan pollo en brasa · guasacaca'),
    (r'[Pp]eruan|[Ss]illao|[Hh]uacatay|[Aa]j[ií]', 'Peruvian pollo a la brasa · soy sauce (sillao) · aji panca · huacatay '
                                                   '(sin tildes)'),
    (r'[Ff]ranc[eé]s|r[ôo]tisserie', 'French rotisserie (poulet rôti on horizontal spits)'),
    (r'[Aa]l ast|[Cc]atal', 'el pollo al ast catalán NO cruza: en EE. UU. la quinta corriente es «charcoal chicken»'),
    (r'[Bb]roaster', 'pressure-fried chicken («Broaster» es marca)'),
    (r'\bSL\b|aut[oó]nomo|IAE|Seguridad Social|alta en', '«LLC vs S corp with your CPA» · «EIN + state payroll / '
                                                         'unemployment registration»'),
    (r'Veri\*?factu|TPV', '«POS that reports sales tax» (sin Veri*factu)'),
    (r'[Uu]rbanism|[Ll]icencia de (?:actividad|apertura|obra)|compatibilidad|declaraci[oó]n responsable',
     '«zoning check before signing» · «building permit + certificate of occupancy» · business license + sales tax permit'),
    (r'[Tt]erraza', 'el caso US no tiene patio (40 plazas en sala)'),
    (r'alcohol|cerveza|vino', 'US §6.7: «beer & wine license» (estado + local; «apply early», sin prometerla) · liquor '
                              'liability'),
    (r'[Hh]umos|[Cc]ampana|extracci|[Cc]onducto', 'US §6.2: Type I hood + fire suppression (UL 300) + makeup air sobre '
                                                  'rotisseries y freidoras; «ask the fire marshal in writing»'),
    (r'[Rr]egistro sanitario|RGSEAA|APPCC|autocontrol', 'US §6.4: plan review (Food Code 8-201.11) + health permit + '
                                                        'inspection; written food safety plan'),
    (r'\bgas\b|[Gg]as natural|butano|propano', 'licensed gas contractor; gas service and regulator sized for two '
                                               'rotisseries + fryers'),
    (r'[Ee]xtintor', 'Class K + 2-A extinguishers'),
    (r'[Gg]rasas|aceite usado', 'grease interceptor · used cooking oil pickup'),
    (r'°C', 'US §6.1: aves 165 °F; hot holding ≥ 135 °F; cooling 135 → 70 °F en 2 h y → 41 °F en 6 h; reheating 165 °F; '
            'la métrica solo entre paréntesis'),
    (r'irrellenable|Ley 1/2025|Ley 7/2022|desperdicio', 'sin equivalente US: packaging ordinances locales; TPHC y cold '
                                                        'holding ≤ 41 °F'),
    (r'[Rr]eclamaciones|[Cc]arteles?', 'required public notices (health permit, beer & wine license, labor law posters)'),
    (r'[Cc]onvenio|[Cc]ontrato|n[oó]mina|registro de jornada', 'offer letters, I-9, W-4, state minimum wage, W-2 por '
                                                               'horas (sin convenio; sin «digital obligatorio»)'),
    (r'PRL|[Pp]revenci[oó]n de riesgos|EPI', 'OSHA basics'),
    (r'[Mm]anipulador|[Ff]ormaci[oó]n', 'Certified Food Protection Manager (2-102.12) + food handler cards (según estado)'),
    (r'[Aa]l[eé]rgen|s[eé]samo|soja', 'US §6.5: 9 major allergens incl. sesame (UK 14); marinade = soy + wheat; aji verde '
                                      '= egg + milk; huancaina = milk + wheat'),
    (r'[Gg]luten|cel[ií]ac', 'US §6.5: NO prometer «gluten-free» (21 CFR 101.91), ni del pollo ni de las yuca fries'),
    (r'[Rr]ider|[Rr]epart', 'own drivers = W-2 + hired & non-owned auto insurance (check your state)'),
    (r'[Pp]lataforma|Glovo|Just Eat|Uber|delivery', 'DoorDash / Uber Eats / Grubhub con sus tiers (US §5.2)'),
    (r'[Ee]nvase|tarrina|bolsa', 'family-meal boxes, vented clamshells, foil bags, sauce cups; local packaging ordinances'),
    (r'SGAE|AGEDI', '«Music licensing (ASCAP/BMI/SESAC)»'),
    (r'[Bb]arra\b', 'Glosario: mostrador → «counter»; el caso US no tiene barra'),
]

# Glosario de la pollería (US §9, OBLIGATORIO; manda sobre el de FT/CAF)
GLOSARIO_POL = OrderedDict([
    ('pollería / asador de pollos (negocio)', 'rotisserie chicken restaurant · Peruvian chicken place/restaurant · '
                                              'chicken shop (solo UK); NUNCA «poultry shop/store» (pollo crudo) ni '
                                              '«roaster»'),
    ('pollo a la brasa', 'pollo a la brasa (sin traducir) · Peruvian rotisserie chicken · Peruvian chicken'),
    ('asador / horno de pollos (equipo)', 'commercial rotisserie (oven) · chicken rotisserie machine; el pollero peruano '
                                          '= charcoal rotisserie'),
    ('espada · cesta · carga / tanda', 'spit (8-spit rotisserie) · basket (basket rotisserie) · load'),
    ('pollo asado (España)', 'rotisserie chicken; «pollo asado» en EE. UU. = pollo mexicano a la parrilla (El Pollo '
                             'Loco): NO es sinónimo'),
    ('brasa / carbón vegetal', 'charcoal (lump/hardwood charcoal) · charcoal-fired'),
    ('pollo entero · medio · cuarto (muslo / pechuga)', 'whole · half · quarter chicken (dark = leg & thigh / white = '
                                                        'breast & wing)'),
    ('menú familiar', 'family meal (whole chicken + 2 large sides)'),
    ('guarniciones', 'sides (regular / large): yuca fries (no «yucca»), fries, rice & beans, maduros (sweet plantains), '
                     'house salad, coleslaw, salchipapas'),
    ('salsas / cremas', 'aji verde (Peruvian green sauce), aji amarillo, rocoto, huancaina, huacatay (sin tildes)'),
    ('bebidas peruanas', 'Inca Kola · chicha morada (purple corn drink)'),
    ('adobo / maceración', 'marinade · «marinated 24-48 hours»'),
    ('rendimiento · merma', 'cooked yield · shrink / holding waste'),
    ('vitrina caliente', 'heated display (merchandiser) · hot holding'),
    ('pollo de 1,2-1,4 kg', 'broiler/fryer (2.5-4.5 lb) · WOG (without giblets); «roaster» = pollo grande, no el asador'),
    ('encargos para fiestas', 'pre-orders · party trays · catering orders'),
    ('para llevar · plataforma', 'take-out / to-go / pickup · third-party delivery marketplace'),
    ('mostrador', 'counter service · fast casual · QSR'),
    ('cubierto equivalente · pedido · ticket medio', 'covers · average check (excl. sales tax and tip)'),
    ('escandallo', 'food cost per bird / per plate · recipe costing'),
    ('campana · carbón', 'Type I hood · fire suppression (UL 300) · solid-fuel cooking (NFPA 96) · spark arrester'),
    ('enfriar · recalentar · control por tiempo', 'cooling · reheating for hot holding · time as a public health control '
                                                  '(TPHC)'),
    ('manipulador de alimentos', 'food handler card · Certified Food Protection Manager (CFPM)'),
    ('pollo broaster', 'pressure-fried chicken («Broaster» es marca)'),
    ('piri-piri portugués', 'peri-peri (minúscula, genérico)'),
    ('agotado', '86\'d'),
    ('63 °C · 75 °C', '135 °F · 165 °F'),
    ('ordenanza de humos', 'Type I hood + local fire/mechanical code (+ air district)'),
    ('registro sanitario', 'health permit + plan review'),
    ('licencia de apertura', 'business license + certificate of occupancy'), ('convenio', 'state/local minimum wage'),
    ('IVA · fianza', 'sales tax · deposit'), ('autónomo / SL', 'LLC'),
])


# ==========================================================================
# Caso de ejemplo US (research US §8; F1-camino §6): celdas VERDES. (corto, hoja ES, celda) → (valor, rótulo)
# ==========================================================================
# Mes 1 = ENERO (F1-camino §6; US §8 decía marzo): los pesos de US §8 en el orden del calendario, sin girar
ESTACIONALIDAD_US = (0.078, 0.078, 0.084, 0.082, 0.088, 0.082, 0.086, 0.084, 0.082, 0.084, 0.082, 0.090)   # ene → dic
assert abs(sum(ESTACIONALIDAD_US) - 1) < 1e-9


def valores_pol(M):
    v = OrderedDict()
    sup = [
        ('B4', 130, 'Pedidos/día'), ('B5', 17.5, 'Ticket medio'), ('B6', 360, 'Días de apertura'),
        ('B7', 0.06, 'Crecimiento de volumen del año 2'), ('B8', 0.04, 'Crecimiento de volumen del año 3'),
        ('B11', 0.86, 'Ventas de COMIDA'), ('B13', 0.29, 'Coste de mercancía sobre las ventas de COMIDA'),
        ('B14', 0.22, 'Coste de mercancía sobre las ventas de BEBIDA'), ('B15', 0.04, 'Consumibles'),
        ('B16', 0.15, 'Ventas por delivery'), ('B17', 0.25, 'Comisión de la plataforma'),
        ('B18', 0.03, 'Comisión de los medios de pago'), ('B20', 0.10, 'Seguridad Social'),
        ('B21', 12, 'Número de pagas'), ('B22', 15080, 'SMI anual'), ('B24', 3733, 'Alquiler mensual'),
        ('B25', 2, 'Fianza'), ('B26', 1800, 'Suministros'), ('B27', 6500, 'Seguros'), ('B28', 0.01, 'Varios'),
        ('B30', 120000, 'Recursos propios'), ('B31', M.CALIBRAR, 'Préstamo bancario'), ('B32', 0.10, 'Tipo de interés'),
        ('B33', 10, 'Plazo del préstamo'), ('B34', 0, 'Carencia'), ('B35', 3, 'Fondo de maniobra'),
        ('B37', 0.25, 'Impuesto de Sociedades, nueva'), ('B38', 0.25, 'Impuesto de Sociedades, tipo'),
        ('B39', 0.08, 'IVA repercutido de restauración'), ('B40', 0.08, 'IVA repercutido/soportado'),
        ('B41', 0, 'IVA soportado en compras'), ('B42', 0, 'Bases negativas'),
        ('B44', 10, 'Vida útil de obra'), ('B45', 7, 'Vida útil de maquinaria'),
        ('B51', 40, 'Aforo'), ('B52', 0.75, 'Actividad del mes 1'), ('B53', 4, 'Meses hasta alcanzar'),
        ('B54', 2, 'Meses de alquiler ANTES'), ('B55', 0.10, 'Imprevistos sobre las partidas de OBRA'),
        ('B58', 2, 'Días medios de cobro'), ('B59', 14, 'Días medios de pago'),
        ('B62', 0.17, 'Bebida que compras al 21'), ('B63', 0.08, 'IVA de la bebida ALCOHÓLICA'),
        ('B65', 1.15, 'DSCR mínimo'), ('B66', 1.25, 'DSCR objetivo'), ('B67', 0.15, 'Holgura mínima'),
        ('B68', None, 'Suelo salarial anual'),
    ]
    for c, val, rot in sup:
        v[('POLP', _S, c)] = (val, rot)
    # Inversión (US §8 en 18 filas, FIJOS): filas 7-24 = $211,300; los imprevistos (B27) van por fórmula (10 % de 7-11 =
    # $11,600: la base incluye arquitecto y rótulo, = Taco EN)
    for k, val in enumerate([13000, 53000, 26000, 11000, 13000, 13000, 5500, 7000, 12800, 6500, 11500, 7500, 3000,
                             11000, 4500, 2500, 5500, 5000]):
        v[('POLP', _I, 'B%d' % (7 + k))] = (val, None)
    # P&L: fijos B26-B34 ($26,000), G13 (soportado de la bebida: valor en el ES) → 0, H11 → 17 % (beer & wine sobre la
    # bebida, = B62), umbrales del semáforo (el margen «bruto» del libro descuenta TODOS los variables: 60 %, = Taco)
    for k, val in enumerate([4200, 3600, 6400, 3600, 2000, 3500, 900, 1000, 800]):
        v[('POLP', _P, 'B%d' % (26 + k))] = (val, None)
    v[('POLP', _P, 'G13')] = (0, None)
    v[('POLP', _P, 'H11')] = (0.17, None)
    for c, val, rot in [('E50', 0.60, 'Margen bruto'), ('E52', 0.30, 'Coste de mercancía /'),
                        ('E53', 0.36, 'Coste de personal'), ('E54', 0.10, 'Alquiler'), ('E55', 0.05, 'Resultado neto')]:
        v[('POLP', _P, c)] = (val, rot)
    # Staffing (US §8, en la fila ES de su función): personas (B), FTE por persona (C), bruto mes TOTAL de la fila (D);
    # ≥ $15/h, 12 pagas, sin propinas; counter & expo = 4 personas en una fila (E4) → 6.6 FTE, $20,531/mes. Cobertura:
    # servicio 10.5 h × 2.75 + producción 3 h × 1.5 (US §8)
    for f, (b, c, d) in zip(range(5, 12), [(1, 1.0, 4500), (1, 1.0, 3293), (1, 1.0, 2773), (4, 0.4, 4159),
                                           (1, 0.5, 1300), (1, 0.5, 1473), (1, 1.0, 3033)]):
        for col, val in zip('BCD', (b, c, d)):
            v[('POLP', _R, '%s%d' % (col, f))] = (val, None)
    v.update([(('POLP', _R, 'B14'), (5000, 'Coste anual')), (('POLP', _R, 'B15'), (5000, 'Coste anual')),
              (('POLP', _R, 'B21'), (10.5, 'Horas de servicio')), (('POLP', _R, 'B22'), (2.75, 'Personas necesarias')),
              (('POLP', _R, 'B23'), (3, 'Horas de producción')), (('POLP', _R, 'B24'), (1.5, 'Personas en el turno'))])
    # Sin `Break-Even!B25` (techo de rotaciones): la rotación está APAGADA en el ES (F1-camino §6; = ES)
    # Escenarios (US §8): pesimista 110 · $16.50 · 355 / optimista 150 · $18.50 · 362
    v.update([
        (('POLP', _ES, 'B5'), (110, 'Pedidos/día')), (('POLP', _ES, 'D5'), (150, 'Pedidos/día')),
        (('POLP', _ES, 'B6'), (16.5, 'Ticket')), (('POLP', _ES, 'D6'), (18.5, 'Ticket')),
        (('POLP', _ES, 'B7'), (355, 'Días')), (('POLP', _ES, 'D7'), (362, 'Días')),
    ])
    # Estacionalidad (US §8, Mes 1 = ENERO sin girar: F1-camino §6) → Month 1-12
    for col, val in zip('BCDEFGHIJKLM', ESTACIONALIDAD_US):
        v[('POLP', _T, '%s5' % col)] = (val, 'Estacionalidad')
    return v


# Calibración D15 (US §8: palancas en su orden; máx. 3 vueltas). Cada celda, citada en F2-NOTAS.md (G7)
CALIBRACION_D15 = OrderedDict()


def formulas_pol():
    p = os.path.join(AQUI, 'formulas_pol.json')
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
    M.TOKENS_DOCX = tokens_pol(M.TOKENS_DOCX)
    M.PRODUCTOS_CIERRE = PRODUCTOS_CIERRE_POL
    M.DOCX_FIJOS = docx_fijos(M)
    M.DOCX_NOTAS = DOCX_NOTAS
    M.DOCX_NOTAS_PLAN = DOCX_NOTAS_PLAN
    M.FORMULAS_EN = formulas_pol()
    M.VALORES_EN = valores_pol(M)
    M.CALIBRACION_D15 = CALIBRACION_D15
    M.CELDA_PISTAS = CELDA_PISTAS
    M.PISTAS_EXTRA = PISTAS_EXTRA
    M.CIFRAS_PROHIBIDAS = cifras_prohibidas(M.VALORES_EN)
    M.RX_POL_NO = RX_POL_NO
    M.REGLA_UNIDADES = REGLA_UNIDADES
    glo = OrderedDict(M.GLOSARIO)
    for k, val in GLOSARIO_POL.items():
        glo[k] = val                          # research §9 manda (regla de jerga §0)
    M.GLOSARIO = glo
