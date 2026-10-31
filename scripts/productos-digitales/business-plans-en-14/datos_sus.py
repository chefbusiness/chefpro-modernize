#!/usr/bin/env python3
"""
datos_sus.py — Sushi Restaurant Business Plan Kit (EN) · los datos ES→EN que dependen del contenido: rótulos fijados
(inversión 18 filas, fijos 9, plantilla de 7 filas), POR_CELDA, pistas, tokens del docx, fijos y notas del docx, caso US
(research US §8 con Mes 1 = enero, F1-camino §6), cifras ES prohibidas y RX_SUS_NO (F1-camino §7) y glosario (US §9). Lo
llama `mapas_sus.instalar()` con el módulo `mapas` YA cargado con los datos de FT/CAF (FIJOS comunes del motor 2.2,
TOKENS_DOCX). Clon de `../business-plans-en-13/datos_pol.py` (Rotisserie EN, el más reciente) con la REJILLA del Taco EN
(`../business-plans-en-12/datos_taq.py`: rotación encendida, `Break-Even!B25`, rótulos «Comensales…»). Sesión Claude
Code, 31-oct-2026 (F2-EN).
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
SUSES = os.path.join(PD, 'plan-sushi')                    # ES cerrado: F1-camino, research y cifras_caso_es.json

URL_SUS = 'aichef.pro/en/digital-products/sushi-restaurant-business-plan'
_I, _S, _P, _R, _N, _E, _ES, _T = ('Inversión Inicial', '0. Supuestos', 'PyG 3 Años', 'Personal', 'Instrucciones',
                                   'Punto Equilibrio', 'Escenarios', 'Tesorería 12 meses')
REGLA_UNIDADES = ('MEDIDAS US (John, 13-oct): principales lb y oz, °F, gallons / quarts / fl oz y sq ft; la métrica entre '
                  'paréntesis para UK: «0.5 oz (14 g)», «−4 °F (−20 °C)», «41 °F (5 °C)», «1,800 sq ft (167 sq m)», '
                  '«50 lb (23 kg)»; nada de kg, g, km, litros ni °C como unidad principal (gate). NUNCA la regla ES de '
                  'congelación «−20 °C 24 h» fuera de la nota UK: la US es −4 °F durante 7 días (168 h) o las dos de '
                  '−31 °F (Food Code 3-402.11)')

# ==========================================================================
# FIJOS (por TEXTO ES, en cualquier celda de los 2 libros). Parten de los de FT/CAF (los del motor 2.2)
# ==========================================================================
FIJOS_FUERA = ('Este fichero forma parte del producto «plan-negocio-food-truck» de AI Chef Pro.',
               'Este fichero forma parte del producto «plan-negocio-cafeteria» de AI Chef Pro.')
_TITULO_CHECK = 'SUSHI RESTAURANT STARTUP CHECKLIST'
FIJOS_NUEVOS = OrderedDict([
    # Instrucciones!A3 del checklist con el nombre comercial
    ('Este fichero forma parte del «Plan de Negocio: Sushi Bar» de AI Chef Pro.',
     'This file is part of the Sushi Restaurant Business Plan Kit by AI Chef Pro.'),
    # títulos: «sushi restaurant» en el nombre, «sushi bar» en descriptor y prosa; nunca «sushi-grade» como garantía ni
    # «authentic» (US §9)
    ('CHECKLIST DE APERTURA — SUSHI BAR', _TITULO_CHECK),
    ('INSTRUCCIONES DE USO — Plan financiero Sushi Bar',
     'HOW TO USE THIS WORKBOOK — Sushi Restaurant Financial Projections'),
    ('PLAN DE NEGOCIO: SUSHI BAR', 'SUSHI RESTAURANT BUSINESS PLAN: SUSHI BAR, TAKE-OUT & DELIVERY'),
    ('Inversión inicial estimada — sushi bar con barra a la vista, mesas, para llevar y a domicilio',
     'Estimated Startup Costs — sushi restaurant with a sushi bar counter, 40 seats, take-out and delivery'),
    ('Ajusta las cifras a tu proyecto: son las de un caso tipo en una ciudad media, sin traspaso. Pon tus presupuestos '
     'reales en las celdas de importe.', 'US kit example (2026) — replace with your own quotes.'),
    ('Escenario realista — sushi bar con barra a la vista, mesas, para llevar y a domicilio',
     'Base case — sushi restaurant: sushi bar and tables, take-out and delivery'),
    ('Punto de equilibrio mensual y diario — sushi bar con barra a la vista, mesas, para llevar y a domicilio',
     'Monthly and daily break-even — sushi restaurant with sushi bar, tables, take-out and delivery'),
    # cabecera de la tabla D19 y fases 2-3 del checklist con el nombre de su pestaña (US §9)
    ('DATOS DE REFERENCIA DEL SECTOR', 'US SUSHI RESTAURANT BENCHMARKS (sourced) AND KIT ESTIMATES'),
    ('FASE 2: LOCAL, EXTRACCIÓN, FRÍO Y LICENCIA (semanas 3-14)',
     'PHASE 2: SITE, HOOD, REFRIGERATION & PERMITS (weeks 3-14)'),
    ('FASE 3: PESCADO, ARROZ Y REGISTRO SANITARIO (semanas 6-14)',
     'PHASE 3: RAW FISH, SUSHI RICE & HEALTH PERMIT (weeks 6-14)'),
    # Inversión, filas 7-24: las 18 partidas de US §8 en las 18 filas con la CLASE de la fila ES (F1-camino §6): 7-11
    # obra (base de imprevistos), 12-21 equipo, 22-24 sin amortizar, y cada partida en la fila ES más parecida.
    # «Signage & facade» entra en la obra (8); «electrical, HVAC, plumbing & grease» se parte en 10 y 11; el freezer de
    # −4 °F va en la fila del congelador ES (14); fryer, range & griddle en la de la cocina caliente (15). Solo la fila 16
    # (campana ES: en EE. UU. va en la 9 con el Type I hood) cambia de objeto: walk-in (= Taco y Rotisserie EN)
    ('Proyecto técnico de actividad y de extracción, y dirección de obra',
     'Architect, MEP & hood drawings, plan review & permit fees'),
    ('Obra del local con barra de sushi a la vista, rótulo y fachada',
     'Build-out (second-generation space, 1,800 sq ft) with sushi bar counter, signage & facade'),
    ('Conducto de extracción exclusivo hasta cubierta', 'Type I hood (about 10 ft), UL 300 fire suppression & makeup air'),
    ('Instalación eléctrica, cuadro y boletín', 'Electrical service & panel'),
    ('Fontanería, separador de grasas y climatización', 'Plumbing, grease interceptor, HVAC & gas lines'),
    ('Vitrina refrigerada de sushi para la barra', 'Refrigerated sushi case (6 ft)'),
    ('Arroceras industriales, mantenedor de arroz y hangiri', 'Commercial gas rice cookers × 2 & rice warmers'),
    ('Armario congelador de -20 °C con registrador y arcón', 'Freezer (−4 °F or colder) with temperature logger'),
    ('Cocina caliente: inducción, freidora de tempura y plancha', 'Fryer, range & griddle (tempura, gyoza, miso)'),
    ('Campana extractora con motor y filtros', 'Walk-in cooler (6×8)'),
    ('Frío: armario de pescado, armarios de cocina, mesa refrigerada y nevera de bebida y sake',
     'Reach-in fish refrigerators (32-34 °F), prep tables, beverage & sake cooler, ice machine'),
    ('Lavavajillas de capota, fregaderos, lavamanos, mesas inox y estanterías',
     '3-comp sink, dish machine, hand sinks, shelving & stainless'),
    ('Utillaje: cuchillos japoneses, tablas por colores, sondas, básculas, pH-metro y etiquetadora',
     'Smallwares (Japanese knives, color-coded boards, hangiri, calibrated pH meter, probes, to-go station)'),
    ('Mobiliario de sala y barra', 'Furniture & sushi bar seating (40 seats)'),
    ('TPV con Veri*factu, datáfono, impresora de comandas y tablets', 'POS, online ordering, KDS & delivery tablets'),
    ('Constitución de la SL, licencia, tasas, registro sanitario y APPCC', 'LLC, legal & food safety plan'),
    ('Marca, web, fotos y lanzamiento', 'Branding, website, photos & launch'),
    ('Stock inicial: pescado, arroz, algas, salsas, cajas de pedidos y bebida',
     'Opening inventory (fish, rice, nori, sauces, disposables, beverage)'),
    # P&L (A10, A11, A25, fijos A26-A34 salvo marketing, que es GM). Fijos 9 = 9 (US §8, fila ES de la misma función):
    # las renovaciones de permisos (CFPM, HACCP plan / variance) van con la formación (fila 34 ES de PRL)
    ('Ventas de sushi y cocina (sala, para llevar y a domicilio)',
     'Food sales (sushi, rolls & kitchen: dine-in, take-out & delivery)'),
    ('Ventas de bebida (cerveza, sake, vino, refrescos, agua y té)', 'Beverage sales (beer, sake, wine, soft drinks & tea)'),
    ('Seguros (RC + multirriesgo)', 'Insurance (general + liquor liability + property + workers\' comp)'),
    ('Gestoría laboral, fiscal y contable', 'Accounting & bookkeeping'),
    ('Mantenimiento del frío, el congelador, la campana extractora y el pH-metro',
     'Maintenance (semiannual hood cleaning, refrigeration & freezer, rice cookers)'),
    ('Software, TPV, teléfono e internet', 'Software, POS & online ordering'),
    ('Limpieza, lavandería, EPI y análisis de autocontrol', 'Cleaning, linens & uniforms'),
    ('Gestión de residuos y del aceite usado de la freidora', 'Waste, grease & used-oil hauling'),
    ('Desinsectación, desratización y desinfección (DDD)', 'Pest control'),
    ('Derechos de autor por música ambiental (SGAE y AGEDI-AIE)', 'Music licensing (ASCAP/BMI/SESAC)'),
    ('Prevención de riesgos laborales, vigilancia de la salud y formación',
     'Training & permit renewals (CFPM, allergens, HACCP plan or variance, OSHA)'),
    # puestos de Staffing (A5:A11): servicio en mesa con servers W-2 y propinas aparte (US §8). Cada puesto en la fila ES
    # de su jornada: el encargado ES (1.0) → sushi chef; el camarero de cenas ES (0.75) → servers, host & to-go (4 × 0.75);
    # el refuerzo de fin de semana ES (0.5) → sushi chef part-time (0.6); las suplencias ES → dish & prep (1.0). En EE. UU.
    # el dueño es el GM y el head sushi chef (itamae) es un puesto contratado (US §8)
    ('Titular — itamae y gerente: compra y corte del pescado, carta y gestión', 'Owner / GM'),
    ('Sushiman o sushiwoman: shari, rolls y combinados', 'Head sushi chef (itamae)'),
    ('Cocinero/a de cocina caliente y arroz', 'Kitchen line cook (tempura, gyoza, rice)'),
    ('Encargado/a de sala y pedidos', 'Sushi chef'),
    ('Camarero/a de cenas y fines de semana', 'Servers, host & to-go packing (W-2, tips on top)'),
    ('Refuerzo de viernes a domingo: sala y empaquetado de pedidos', 'Sushi chef (part-time W-2, weekends & dinner peaks)'),
    ('Suplencias de vacaciones y descansos', 'Dish & prep'),
])

# Mismo ES con otro EN en ESTA celda (lección de BP2 §4.1: los arreglos de un libro no se heredan a ciegas)
POR_CELDA = OrderedDict([
    # E5: la columna H de la línea de bebida = parte gravada al tipo del alcohol de B40 (= Pizza, Taco y Rotisserie EN)
    (('SUSP', _P, 'H4'), 'Beverage share taxed at the alcohol rate in B40 (%)'),
    (('SUSP', _P, 'F11'), 'Dine-in beverages and the drinks that go out with orders (beer, sake, wine, soft drinks and '
                          'tea) · Column H is the share of beverage sales taxed at the alcohol rate in "0. Assumptions" '
                          'B40. With the example rates (B39 = B40 = 8%: state + local) it changes nothing. Some states '
                          'tax alcohol differently: type your alcohol rate in B40 and the alcohol share of beverage sales '
                          'here'),
    (('SUSP', _S, 'A62'), 'Alcohol share of beverage purchases (reference only: no input credit in the US)'),
    (('SUSP', _S, 'C62'), 'Reference only: in the US the sales tax you pay on purchases is a cost, not a credit (B41 = 0%), '
                          'so this share moves no figure in the workbook. The sales tax you COLLECT on beverages is set '
                          'by the beverage line of the P&L (column H)'),
    (('SUSP', _S, 'C63'), 'NO EFFECT in this workbook: the sales tax collected on beverages is set by the beverage line of '
                          'the P&L. With the example, beer, sake, wine, soft drinks and food all pay the same 8% (state + '
                          'local); if your state taxes alcohol at another rate, type it in B40 and the alcohol share in '
                          'column H of that line'),
    # Mes 1 = ENERO con los pesos de US §8 en el orden del calendario (VALORES_EN B5:M5), no los del ES (agosto abajo)
    (('SUSP', _T, 'O5'), 'Month 1 = JANUARY, in calendar order: January is the slowest month; February (Valentine\'s Day), '
                         'May (Mother\'s Day and graduations) and December (holiday parties and New Year\'s Eve platters) '
                         'are the peaks. Kit weights for a mid-size US city: replace them with your area\'s pattern; if '
                         'you open in another month, rotate the row. It must add up to 100%'),
    # E4: la nota de Staffing con servers W-2 y sus propinas (US §6.8): sin tip credit modelado
    (('SUSP', _R, 'A29'), 'The gross pay, employer payroll taxes, monthly cost and annual cost columns are TOTALS for the '
                          'row: for a position with several people they include all of them. "FTE" is the share of a '
                          'full-time week and is used to compare pay with the legal floor pro rata. The payroll tax rate '
                          'and the number of pay periods are in the "0. Assumptions" tab. Tips are not modeled: every '
                          'position, servers included, is budgeted at a base wage of at least $15/h, and the tips come on '
                          'top and belong to the staff, never to the owner or managers. Federal rules allow a $2.13/h cash '
                          'wage with a tip credit of up to $5.12 where the state permits it; CA, OR, WA, AK, MN, MT and NV '
                          'do not (DOL)'),
])


# ==========================================================================
# Cifras prohibidas (F1-camino §7): ES del sushi bar (importe y frase), casos EN publicados y RX_SUS_NO.
# Formato: (regex, motivo, excepción sobre el texto entero)
# ==========================================================================
def _num(n):
    """131000 → patrón que casa 131,000 · 131.000 · 131 000 · 131000 (y nada pegado a más dígitos)."""
    s = str(n)
    cab, cola = s[:-3], s[-3:]
    return r'(?<![\d.,])' + cab + r'[.,   ]?' + cola + r'(?![\d])'


def _cifras_es():
    """Importes ≥ 10.000 € del caso ES del sushi bar (`../plan-sushi/cifras_caso_es.json`, tokens con «€»: el ES está
    cerrado y manda). Los pequeños quedan cubiertos por la prohibición de «€»."""
    out = set()
    p = os.path.join(SUSES, 'cifras_caso_es.json')
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
        (r'(?i)\b79 (?:covers|guests|customers|diners|orders)\b', 'caso ES (79 comensales/día)'),
        (r'(?i)\b36 (?:seats|covers)\b', 'caso ES (36 plazas)'),
        (r'(?<![\d$])20[.,]00\b(?!\s?(?:lb|oz|%))', 'ticket ES (20,00 €)'),
        (r'(?i)\b300 (?:opening )?days\b', 'días del ES (300; el caso US abre 310)'),
        (r'(?i)\b14 (?:pay periods|payments|paychecks|salaries|monthly)', 'pagas del ES (14 pagas)'),
        (r'(?i)(?:payroll|social security|employer)[^.;]{0,60}?\b33\s?%', 'Seguridad Social del ES (33 %)'),
        (r'(?i)\b33\s?%[^.;]{0,40}?(?:payroll|social security|employer)', 'Seguridad Social del ES (33 %)'),
        (r'\b17[.,]094\b', 'SMI ES (17.094 €)'),
        (r'\b1[.,]221\b', 'SMI ES (1.221 €)'),
        # la plataforma ES (F1-camino §7): 24 % de las ventas al 30 %; el caso US es el 15 % al 25 %
        (r'(?i)\b24 ?% of (?:total )?sales\b', 'plataforma ES (24 % de ventas: el caso US es el 15 %)'),
        (r'(?i)\bRD 1(?:021|086|26|420)\b|\bRD 919\b|\bart\. ?(?:4\.1|8\.[12]|30(?:\.5)?)\b|Ley 1/2025|Ley 7/2022|'
         r'\bACSA\b|\bAESAN\b',
         'norma ES (RD 1021/2022, RD 1086/2020, RD 126/2015, RD 1420/2006, Leyes 1/2025 y 7/2022, AESAN)'),
        (r'\b6[03]\s?°C|\b75\s?°C', 'temperaturas ES (63 °C / 75 °C; en EE. UU. 135 °F y 165 °F)'),
        (r'\bv1\.[01]\b|\b[Vv]ersion 1\.[01]\b', 'historia de versiones (la EN nace en 2.2)'),
    ]


# casos EN publicados (frases). NO van «115 covers» (Taco EN), «95 covers» (Bar EN) ni «$36» (Pizza EN): coinciden con el
# caso del sushi (115 covers/día, pesimista de 95, comensal de sala de $36.00, US §8)
FRASES_OTROS = [(r'(?i)\b62 covers\b', 'caso de la Pizza EN («62 covers»)'),
                (r'(?i)\b165 customers\b', 'caso de la Ice Cream EN («165 customers»)'),
                (r'(?i)\b210 transactions\b', 'caso de la Bakery EN («210 transactions»)'),
                (r'\$27(?:\.00)?\b(?![.,]\d)', 'caso del Bar EN («$27»)'),
                (r'(?i)\b308 (?:opening )?days\b', 'caso del Taco EN («308 days»)'),
                (r'(?i)\b130 covers\b', 'caso del Rotisserie EN («130 covers»)'),
                (r'(?i)\b360 (?:opening )?days\b', 'caso del Rotisserie EN («360 days»)'),
                (r'\$17\.50\b', 'check del Taco y del Rotisserie EN («$17.50»)')]

_NO = r"(?i)\b(?:no|not|never|cannot|can't|don't|do not|without|isn't|is not|rather than|instead of)\b"
RX_SUS_NO = [
    # restos del Taco EN y del Rotisserie EN (F1-camino §7)
    (r'(?i)\btacos?\b|\btaquer', 'Taco EN («taco / taqueria»)', None),
    (r'(?i)trompo|al pastor', 'Taco EN («trompo / al pastor»)', None),
    (r'(?i)tortilla|masa harina', 'Taco EN («tortilla / masa harina»)', None),
    (r'(?i)salsa bar', 'Taco EN («salsa bar»)', None),
    (r'(?i)\bmezcal|\btequila', 'Taco EN / ES («mezcal / tequila»: el caso US es beer, sake & wine)',
     r'(?i)liquor license|full liquor'),
    (r'(?i)rotisserie|pollo a la brasa|\bspits?\b|family meals?|heated display|\byuca\b|huancaina|Inca Kola',
     'Rotisserie EN («rotisserie / spit / family meal / yuca»)', None),
    # restos de la Pizza EN y del Bar EN
    (r'(?i)\bpizz', 'Pizza EN («pizza»)', None),
    (r'(?i)Neapolitan|\bdough\b', 'Pizza EN («Neapolitan / dough»)', None),
    (r'\bVPN\b|\bAVPN\b', 'Pizza EN («VPN»)', None),
    (r'(?i)Margherita|mozzarella|San Marzano', 'Pizza EN (ingredientes)', None),
    (r'(?i)\btapas\b|\bsmall plates\b', 'Bar EN («tapas / small plates»)', None),
    (r'(?i)\bcocktails?\b', 'Bar EN («cocktails»: el sushi bar es beer, sake & wine)', None),
    (r'(?i)\bhappy hour\b|\blast call\b|\bbarbacks?\b|\bneighborhood bar\b', 'Bar EN', None),
    (r'(?i)\bspirits\b', 'Bar EN («spirits»: el sushi bar es beer, sake & wine)',
     r'(?i)liquor license|full liquor|' + _NO[4:]),
    # restos del ES (F1-camino §7)
    (r'\bIVA\b', 'ES («IVA»)', None),
    (r'(?i)\bconvenio\b', 'ES («convenio»)', None),
    (r'\bSMI\b', 'ES («SMI»)', None),
    (r'(?i)\baut[oó]nomo', 'ES («autónomo»)', None),
    (r'Veri\*?factu', 'ES («Veri*factu»)', None),
    (r'\bSGAE\b', 'ES («SGAE»)', None),
    (r'\bIAE\b', 'ES («IAE»)', None),
    (r'(?i)\bterrazas?\b', 'ES («terraza»)', None),
    (r'(?i)\bcomensal|\bpedidos?\b|\bcombinados?\b|\bvitrina|\bsushiman|\bsushiwoman',
     'ES («comensal / pedido / combinado / vitrina / sushiman» → covers, orders, platter, sushi case, sushi chef)', None),
    (r'\bEspaña\b|\bSpain\b|\bSpanish\b', 'ES («España/Spain»: la corriente española no cruza)', r'(?i)Spanish mackerel'),
    (r'\bVAT\b', 'ES («VAT» fuera de la nota UK)', r'\bUK\b|United Kingdom|HMRC'),
    (r'(?i)[−-]20\s?°C[^.;]{0,25}24 ?h(?:ours)?|24 ?h(?:ours)?[^.;]{0,25}[−-]20\s?°C',
     'regla ES de congelación («−20 °C 24 h»: la US es −4 °F 7 días o −31 °F; solo en la nota UK)',
     r'\bUK\b|United Kingdom|\bEU\b|853/2004'),
    # jerga trampa y claims (US §6.6 y §9)
    (r'(?i)\bsu(?:shi|shimi)[- ]grade|\bsashimi[- ]grade',
     'claim («sushi-grade / sashimi-grade»: sin definición legal; solo para negarlo)',
     r'(?i)no (?:legal|regulatory|federal|official) (?:definition|standard|meaning)|not (?:a )?(?:legal|regulated|defined)|'
     r'marketing (?:term|label)|' + _NO[4:]),
    (r'(?i)\bauthentic', 'claim («authentic»: US §9, nunca como promesa)', None),
    (r'(?i)gluten[- ]free', 'claim («gluten-free»: US §6.4, ni del arroz ni de la soja)',
     r"(?i)21 CFR|\bnot\b|\bnever\b|cannot|can't|don't|do not|\bno\b"),
    (r'(?i)\bsurimi\b', 'jerga: «imitation crab» («kani» o «krab» en carta), no «surimi» (US §9)', r'(?i)imitation crab'),
    (r'(?i)counter[- ]service', 'servicio en mesa con servers (US §1); counter service solo en la variante poke / hand roll',
     r'(?i)poke|hand[- ]roll'),
    (r'(?i)open (?:7|seven) days|(?:7|seven) days a week', 'el caso abre 6 días (cierra el lunes, US §8)',
     r'(?i)' + _NO[4:]),
    # unidades (REGLA_UNIDADES): kg, g, km, litros, °C y m² solo entre paréntesis
    (r'(?i)\d\s?(?:kg|km|°C|liters?|litres?|ml)\b(?![^()]*\))', 'unidades: métrica solo entre paréntesis (REGLA_UNIDADES)',
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
    """Importes en dólares ≥ 10,000 que cita la research US del sushi: son datos de este producto y no se vetan aunque
    coincidan con un importe de otro caso EN."""
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
    out = [(_num(n), 'cifra del caso ES del sushi bar', None) for n in sorted(_cifras_es()) if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in _frases_es()]
    propios |= _importes_research()
    for path, plan, nombre in [(os.path.join(POL, 'cifras_caso.json'), 'pol', 'del Rotisserie EN'),
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
    out += RX_SUS_NO
    return out


# ==========================================================================
# Tokens del docx: los de FT/CAF con los rótulos del sushi bar («Comensales…», = taquería) + partidas propias
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
    ('consumibles_pct', 'disposables (sushi trays, soy cups, chopsticks, bags), % of sales'),
])
_FUERA = ('inv_vehiculo', 'inv_adaptacion', 'inv_equipo_cocina', 'inv_generador', 'inv_permisos', 'inv_espresso',
          'inv_obra', 'inv_instalaciones', 'inv_mobiliario', 'inv_barra', 'inv_terraza', 'inv_lanzamiento',
          'inv_stock', 'aforo', 'rotaciones_dia')


def _inv(rot, desc):
    return ('usd', ('fila', _I, {'sus': rot}, 'B'), desc)


def _como_excel(v, decimales):
    """Redondeo que se VE en Excel: 15 cifras significativas y luego mitad hacia arriba (no al par como `format`)."""
    from decimal import Decimal, ROUND_HALF_UP
    return float(Decimal('%.15g' % v).quantize(Decimal(1).scaleb(-decimales), rounding=ROUND_HALF_UP))


TOKENS_PROPIOS = OrderedDict([
    ('inv_proyecto', _inv('Proyecto técnico de actividad y de extracción, y dirección de obra',
                          'architect, MEP & hood drawings, plan review and permit fees')),
    ('inv_obra', _inv('Obra del local con barra de sushi a la vista, rótulo y fachada',
                      'build-out of a second-generation space (1,800 sq ft) with the sushi bar counter, signage and '
                      'facade')),
    ('inv_campana', _inv('Conducto de extracción exclusivo hasta cubierta',
                         'Type I hood (about 10 ft), UL 300 fire suppression and makeup air')),
    ('inv_instalaciones', _inv('Instalación eléctrica, cuadro y boletín', 'electrical service and panel')),
    ('inv_fontaneria', _inv('Fontanería, separador de grasas y climatización',
                            'plumbing, grease interceptor, HVAC and gas lines')),
    ('inv_vitrina', _inv('Vitrina refrigerada de sushi para la barra', 'refrigerated sushi case (6 ft)')),
    ('inv_arroceras', _inv('Arroceras industriales, mantenedor de arroz y hangiri',
                           'two commercial gas rice cookers and rice warmers')),
    ('inv_congelador', _inv('Armario congelador de -20 °C con registrador y arcón',
                            'freezer (−4 °F or colder) with temperature logger')),
    ('inv_cocina', _inv('Cocina caliente: inducción, freidora de tempura y plancha',
                        'fryer, range and griddle (tempura, gyoza, miso)')),
    ('inv_camara', _inv('Campana extractora con motor y filtros', 'walk-in cooler (6×8)')),
    ('inv_frio', _inv('Frío: armario de pescado, armarios de cocina, mesa refrigerada y nevera de bebida y sake',
                      'reach-in fish refrigerators (32-34 °F), prep tables, beverage & sake cooler and ice machine')),
    ('inv_lavado', _inv('Lavavajillas de capota, fregaderos, lavamanos, mesas inox y estanterías',
                        '3-compartment sink, dish machine, hand sinks, shelving and stainless')),
    ('inv_utillaje', _inv('Utillaje: cuchillos japoneses, tablas por colores, sondas, básculas, pH-metro y etiquetadora',
                          'smallwares (Japanese knives, color-coded boards, hangiri, calibrated pH meter, probes, to-go '
                          'station)')),
    ('inv_mobiliario', _inv('Mobiliario de sala y barra', 'furniture and sushi bar seating (40 seats)')),
    ('inv_tpv', _inv('TPV con Veri*factu, datáfono, impresora de comandas y tablets',
                     'POS, online ordering, KDS and delivery tablets')),
    ('inv_constitucion', _inv('Constitución de la SL, licencia, tasas, registro sanitario y APPCC',
                              'LLC, legal and food safety plan')),
    ('inv_lanzamiento', _inv('Marca, web, fotos y lanzamiento', 'branding, website, photos and launch')),
    ('inv_stock', _inv('Stock inicial: pescado, arroz, algas, salsas, cajas de pedidos y bebida', 'opening inventory')),
    ('aforo', ('int', ('fila', _S, {'sus': 'Aforo del local (plazas sentadas, con la barra)'}, 'B'),
               'seats (10 at the sushi bar + 30 at tables)')),
    ('rotaciones_dia', ('dec1', ('fila', _S, {'sus': 'Rotaciones al día implícitas (calculado)'}, 'B'),
                        'implied seat turns per day (take-out and delivery covers included)')),
    ('comida_pct', ('pct0', ('fila', _S, {'sus': 'Ventas de COMIDA sobre el total'}, 'B'), 'food share of sales')),
    ('bebida_pct', ('pct0', ('fila', _S, {'sus': 'Ventas de BEBIDA sobre el total'}, 'B'), 'beverage share of sales')),
    ('plataforma_pct', ('pct0', ('fila', _S, {'sus': 'Ventas por delivery sobre el total'}, 'B'),
                        'share of sales through third-party delivery marketplaces')),
    ('comision_pct', ('pct0', ('fila', _S, {'sus': 'Comisión de la plataforma de delivery'}, 'B'),
                      'marketplace commission on those orders')),
    ('marketing_anual', ('usd', ('fila', _P, {'sus': 'Marketing y publicidad'}, 'B'), 'marketing budget per year')),
    ('prime_cost_pct', ('pct1', ('deriv', lambda c: c['cogs_pct'] + c['personal_pct']),
                        'prime cost year 1 (cost of goods + labor, % of sales)')),
    ('meses_alquiler_previo', ('int', ('fila', _S, {'sus': 'Meses de alquiler ANTES de abrir (obra y licencias)'}, 'B'),
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


def tokens_sus(base):
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
            src = ('fila', hoja, {'sus': rot}, col)
        if t == 'consumibles_pct':
            fmt = 'pct1'
        out[t] = (fmt, src, _DESC.get(t, desc))
    out.update(TOKENS_PROPIOS)
    return out


# ==========================================================================
# Docx: lo que escribe ensamblar_docx.py (índices del Word ES de 131 párrafos = Taco) y las notas por ranura
# ==========================================================================
# Productos del cierre: solo los que EXISTEN en la tienda EN (tienda.ts, 31-oct; lección M2 del Taco EN): no hay guía de
# restaurante japonés ni checklists de sushi en EN
PRODUCTOS_CIERRE_SUS = ['Food Cost Kit Pro', 'HACCP Food Safety Kit Pro', 'Restaurant Checklists Kit Pro',
                        'Food Cost + Menu Engineering Guide']


def docx_fijos(M):
    pc = PRODUCTOS_CIERRE_SUS
    d = OrderedDict([
        (6, 'BUSINESS PLAN'), (7, 'Sushi Restaurant'),
        (9, 'Complete financial plan, market analysis,\noperations strategy and startup checklist\nto open a sushi '
            'restaurant with a sushi bar, take-out and delivery in the United States'),
        (14, 'AI Chef Pro'), (15, 'aichef.pro'), (16, 'US edition with UK notes · 2026'),
        (18, 'LEGAL NOTICE'), (19, M.AVISO_DOCX_EN), (20, '© 2026 AI Chef Pro — aichef.pro'), (22, 'CONTENTS'),
        (35, 'Appendices: Sushi Restaurant Financial Projections (Excel) + Sushi Fish, Rice & Costing Calculator (Excel) + '
             'Sushi Restaurant Startup Checklist (Excel) + Equivalents Guide'),
        (123, 'AI Chef Pro'), (124, 'Templates and AI tools for food businesses'),
        (126, 'aichef.pro\ninfo@aichef.pro'),
        (127, '→ %s · %s' % tuple(pc[:2])), (128, '→ ' + pc[2]), (129, '→ ' + pc[3] + ' (cost per piece and menu mix)'),
        (130, '\n' + M.URL_TIENDA),
    ])
    return OrderedDict([('sus', d)])


DOCX_NOTAS_PLAN = OrderedDict([
    ('sus', 'Concepto (US §1): INDEPENDENT SUSHI RESTAURANT con SUSHI BAR en una ciudad media de EE. UU. (150-500 mil hab.), '
            '~1,800 sq ft, {{aforo}} plazas (10 en el sushi bar frente al sushi case, 30 en mesas), SERVICIO EN MESA con '
            'servers W-2 y propinas aparte, pickup propio (take-out) y marketplaces. Línea: el head sushi chef (itamae) a '
            'la vista en la barra; cocina caliente pequeña (tempura, gyoza, miso, teriyaki) bajo Type I hood; arroceras de '
            'gas; walk-in y freezer de −4 °F con registrador para el stock de pescado ya tratado. Carta: nigiri y sashimi, '
            'classic rolls (California, spicy tuna), specialty rolls, hand rolls, poke bowls, appetizers (edamame, gyoza, '
            'tempura) y beer, sake & wine (licencia como parámetro). ABRE 6 DÍAS (cierra el lunes; 310 días: cierra '
            'también Thanksgiving, Christmas Day y New Year\'s Day). En EE. UU. el dueño es el GM y el head sushi chef '
            'es un puesto contratado. Nombre: «sushi restaurant» en el título; «sushi bar» en la prosa; «itamae» glosado '
            'UNA vez (head sushi chef); «sushiman» NO (→ sushi chef); «vitrina» → sushi case; «combinado» → platter; '
            '«surimi» → imitation crab. NUNCA «sushi-grade» ni «sashimi-grade» como garantía (no tienen definición '
            'legal: solo para negarlo) ni «authentic» como promesa. El ES llama «comensal» a la unidad; el EN dice '
            '«covers» (1 order = 1.6 covers). Cada cifra del caso va con su token {{…}}; las de mercado solo si están en '
            'la research con fuente. Lo ES que NO cruza (IVA partido, RD 1021/2022 art. 8 y su −20 °C 24 h, RD 1086/2020 '
            'art. 30.5, RD 126/2015, ordenanza de humos, IAE, convenio, SMI, 14 pagas, Leyes 1/2025 y 7/2022, Veri*factu, '
            'agosto como mes flojo, menú del día al 10 %) se SUSTITUYE por US §6 o se quita. Omakase = variante (chef\'s '
            'counter de 10 plazas, 2 turnos); poke / hand roll bar = variante de counter service. Fuera: franquicias y '
            'quioscos de supermercado (son el grocery store sushi, otro negocio), kaiten (variante sin Excel), food truck. '
            'No cites productos que no estén en el cierre. Honestidad del margen: neto {{margen_neto_a1}}. Glosario US §9 '
            'obligatorio. El cierre (productos) lo escribe el ensamblador. ' + REGLA_UNIDADES),
])

_FORMA = ('FORMA: la sección §%d del Taco EN (business-plans-en-12/docx_en_taq_%s.json) da el registro y la longitud; '
          'su vocabulario de taquería (taco, trompo, tortilla, salsa bar, patio, counter service…) y sus cifras NO valen')
_SEC = OrderedDict([
    (1, ('a', 'Resumen ejecutivo: concepto (US §1), la oportunidad (US §2: «sushi restaurant» ≈ 201,000 búsquedas/mes y '
              '«sushi bar» 27,100 = demanda de CONSUMO; «sushi restaurant business plan» ≈ 20: no lo cites como '
              'mercado; IBISWorld: 17,301 sushi restaurants en EE. UU., ninguno con más del 5 %), inversión y financiación '
              'SOLO con tokens ({{inversion_total}}, {{capex}}, {{prestamo}} SBA 7(a) {{tipo_prestamo}} a '
              '{{plazo_prestamo}} años), ventas ({{ventas_a1}}, {{clientes_dia}} covers × {{ticket}} × {{dias}} días), '
              'neto {{margen_neto_a1}} y DSCR {{dscr_min}}')),
    (2, ('a', 'Concepto y propuesta (ES ¶46-¶47 adaptados): el formato elegido (sushi bar + mesas + take-out + delivery) '
              'frente a las variantes: omakase (chef\'s counter de 10 plazas, 2 turnos, precio fijo y reserva: menos '
              'CAPEX, pescado importado, otro modelo), poke / hand roll bar (counter service, sin sushi chef de barra), '
              'kaiten / conveyor (variante sin Excel); las franquicias y los quioscos de supermercado (grocery store '
              'sushi) son otro negocio; glosa itamae, neta, shari, saku, nigiri, sashimi, maki, uramaki / inside-out roll, '
              'hand roll (temaki) y platter la primera vez; sin «authentic»')),
    (3, ('a', 'Mercado y competencia: US §2, §5.1 y §5.2 (carta de ciudad media, Kit estimate de tres menús + 10-20 %: '
              'nigiri $5-7 el par, classic roll $7-9, specialty $13-18, sashimi $28-65; IBISWorld 17,301 negocios y '
              '$33.2-34.9 bn; ninguno > 5 %); el grocery store sushi y los quioscos franquiciados son el ancla de precio '
              'bajo del cliente (sin cifra de quioscos en el Word); se compite en frescura visible, el chef en la barra y '
              'la carta; sin datos de mercado sin fuente')),
    (4, ('a', 'Cliente y posicionamiento: parejas y grupos de cena, comida de oficina, fines de semana; el check de '
              '{{ticket}} por cover equivalente (US §8: comensal de sala ≈ $36.00 = comida $28.50 + bebida $7.50; take-out '
              '≈ $41.00 por pedido y marketplace ≈ $46.00 con la carta un 15 % más cara; 1 pedido = 1.6 covers; ≈ 70 de '
              'sala, ≈ 25 de take-out y ≈ 20 de marketplace al día); el pickup directo (0 % de comisión) frente a los '
              'marketplaces')),
    (5, ('a', 'Marketing y ventas: Google Business Profile, Yelp, Instagram (el corte en la barra vende en vídeo); fechas: '
              'Valentine\'s Day, Mother\'s Day y graduaciones, la noche del Super Bowl y New Year\'s Eve con party '
              'platters por encargo; marketplaces DoorDash / Uber Eats / Grubhub con sus tiers; el caso pone '
              '{{plataforma_pct}} de las ventas al {{comision_pct}}; viajan bien los rolls y los platters fríos, mal la '
              'tempura; la consumer advisory también en los listados de marketplace')),
    (6, ('b', 'Operaciones y equipo: sushi case ({{inv_vitrina}}), arroceras de gas ({{inv_arroceras}}), freezer de '
              '−4 °F con registrador ({{inv_congelador}}), fryer, range & griddle ({{inv_cocina}}), Type I hood + UL 300 + '
              'makeup air ({{inv_campana}}), walk-in ({{inv_camara}}) y reach-in de pescado a 32-34 °F ({{inv_frio}}); el '
              'sushi chef entra a las 9:30 (arroz, corte de saku); pescado comprado YA tratado (congelado según 3-402.11 '
              'con la carta del proveedor) o exento (atún, salmón de acuicultura con pienso, con declaración escrita); '
              '«EVERY SLICE COUNTS» (US §8): el margen está en los rolls y el precio en el pescado; regla del sushi case: '
              'cortar por servicio, nunca llenarlo «por si acaso»; merma objetivo ≤ 5 % del pescado comprado; mide el '
              'rendimiento y el coste por pieza con la calculadora del kit (sin inventar cifras: las da la calculadora)')),
    (7, ('b', 'Organización y personal: Owner / GM, head sushi chef (itamae), sushi chef, sushi chef part-time de fines de '
              'semana y cenas, kitchen line cook, servers, host & to-go packing (4 part-time W-2) y dish & prep '
              '({{plantilla_puestos}} personas = {{plantilla_jornadas_xl}} FTE); contrata al head sushi chef ANTES de la '
              'obra (diseña la barra y el flujo); ≥ $15/h, propinas de los servers aparte y para el equipo, sin tip '
              'credit modelado; employer payroll taxes {{cargas_pct}}; el dueño se paga por debajo de un manager: '
              '«owner\'s draw in addition from net profit»')),
    (8, ('b', 'Plan financiero: TODO con tokens (ventas años 1-3, mezcla {{comida_pct}}/{{bebida_pct}}, COGS '
              '{{cogs_pct_xl}}, personal {{personal_pct}}, prime cost {{prime_cost_pct}}, alquiler {{ocupacion_pct}}, '
              'EBITDA, neto, equilibrio {{equilibrio_clientes_dia}} / {{equilibrio_caja_clientes_dia}} covers/día, holgura '
              '{{holgura_caja_pct}}, DSCR {{dscr_min}}, saldo mínimo {{saldo_minimo}}, escenarios); el food cost del plan '
              'es el consumo real de TODA la carta con la merma del sushi case y las comidas del personal: el coste '
              'teórico por pieza de la calculadora sale más bajo (el puente, sin cifra inventada); el precio del pescado '
              'es volátil (salmón, atún) y lo pide la calculadora')),
    (9, ('b', 'Marco legal US (ver las notas propias de cada ranura de §9)')),
    (10, ('b', 'Hoja de ruta: el orden del checklist (80 tareas en 6 fases: setup; hood & permits; raw fish & health; '
               'staff & allergens; menu, brand & delivery; opening & 90 days); decide TPHC o variance para el sushi rice '
               'con tu health department ANTES de abrir; las cartas de los proveedores de pescado archivadas (90 días); '
               'la beer & wine license se pide al firmar el local; el head sushi chef contratado antes de la obra; cierre '
               'con el Excel, la calculadora del pescado, el arroz y el coste por pieza, y el checklist')),
])
_RANURAS = OrderedDict([(1, range(39, 44)), (2, range(46, 51)), (3, range(53, 59)), (4, range(61, 67)),
                        (5, range(69, 76)), (6, range(78, 83)), (7, range(85, 91)), (8, range(93, 100)),
                        (9, range(102, 109)), (10, range(111, 118))])
_N9 = OrderedDict([
    (102, '§9 1/7: el marco US por niveles (federal, estatal, condado, ciudad); LLC + EIN; sales tax permit; business '
          'license; zoning check ANTES de firmar; plan review (Food Code 8-201.11) + building permit → certificate of '
          'occupancy; fire marshal; sales tax {{sales_tax}} de ejemplo, un solo tipo («some states tax to-go food '
          'differently», sin cifra)'),
    (103, '§9 2/7: campana y fuego: Type I hood + supresión UL 300 sobre la freidora de tempura, el range y el griddle; '
          'makeup air; grease interceptor; limpieza de campana semestral (NFPA 96, Tabla 11.4: volumen moderado); '
          'pregunta al inspector mecánico si las arroceras de gas van bajo campana; walk-in, reach-in de pescado y '
          'freezer con registrador; health permit + inspección previa; Certified Food Protection Manager (2-102.12) + '
          'food handler cards según estado'),
    (104, '§9 3/7: pescado crudo: FDA Food Code 2022 (cada estado adopta su edición) 3-402.11 parasite destruction: −4 °F '
          'o menos durante 168 h (7 días), o −31 °F hasta sólido + 15 h, o −31 °F hasta sólido + −4 °F 24 h; EXENTOS el '
          'atún de las especies Thunnus (yellowfin, bigeye, bluefin, albacore…) y el pescado de acuicultura alimentado '
          'con pienso (como el salmón) con declaración escrita del proveedor; registros 3-402.12 guardados 90 días; el '
          'SOP del kit: comprar el pescado YA tratado con la carta del proveedor (supplier letter) y el freezer de −4 °F '
          'para el stock; «sushi-grade» no tiene definición legal (no lo prometas); scombrotoxin (histamina) en atún, '
          'yellowtail y caballa: recepción a ≤ 40 °F o se rechaza (FDA Fish and Fishery Products Hazards and Controls '
          'Guidance, cap. 7); cold holding ≤ 41 °F'),
    (105, '§9 4/7: sushi rice (TCS): dos vías: (a) TPHC 3-501.19, hasta 4 h con la hora marcada en cada tanda y '
          'procedimiento escrito para el inspector; a las 4 h se tira (no vuelve al frío ni se recalienta) = el caso por '
          'defecto; (b) variance + HACCP plan para el arroz acidificado (3-502.11(C); el anexo pone de ejemplo un límite '
          'crítico de pH < 4.2; cada condado fija el suyo, entre 4.0 y 4.6, con pH-metro calibrado y registro por '
          'tanda); el kit NO fija un pH «legal»: «ask your health department in writing»; consumer advisory 3-603.11: '
          'disclosure (asterisco en cada plato crudo) + reminder, en la carta, en la web y en los listados de '
          'marketplace'),
    (106, '§9 5/7: alérgenos: 9 mayores US incluido el sésamo (FASTER Act, desde 2023): fish, crustacean shellfish '
          '(shrimp, crab), soy y wheat (soy sauce; tamari solo si la etiqueta lo dice), sesame (semillas, aceite), egg '
          '(spicy mayo, tamago, rebozado de tempura), milk (cream cheese), wheat (tempura, panko; el imitation crab '
          'suele llevar almidón de trigo y clara de huevo: según etiqueta); los moluscos y la mostaza NO son major en '
          'EE. UU. (sí en UK); «gluten-free»: 21 CFR 101.91, NO se promete'),
    (107, '§9 6/7: beer & wine license (agencia estatal + aprobación local; el sake suele ir con la licencia de vino: «ask '
          'your state ABC»; «apply early», NO prometer licencia); liquor liability en el seguro ({{seguros_anual}} con '
          'general liability, product liability del pescado crudo, property y workers\' comp); personal: W-2 por horas '
          '(nada de 1099 para sushi chefs o servers), I-9, W-4, salario mínimo estatal (federal $7.25/h, DOL), propinas '
          'del equipo (los managers y el dueño nunca se quedan propinas); música ASCAP/BMI/SESAC; packaging ordinances '
          'locales (prohibiciones de poliestireno)'),
    (108, '§9 7/7: venta desde casa: las cottage food laws no cubren el pescado crudo ni el arroz (TCS): este plan es de '
          'local con permiso («check your state»); y, como ÚLTIMA frase o frases, la NOTA UK: registro del food business '
          'en el council 28 días antes, FHRS 0-5; parásitos: −20 °C (−4 °F) durante 24 h o −35 °C (−31 °F) durante 15 h, '
          'sin exención del atún (retained Regulation 853/2004, compruébalo con tu council); VAT 20 % en sala y en la '
          'comida caliente, el sushi frío para llevar suele ir al 0 % («check HMRC VAT Notice 709/1»); 14 alérgenos '
          '(moluscos, mostaza, apio, sulfitos, altramuces); premises + personal licence para el alcohol'),
])


def _notas_docx():
    out = OrderedDict()
    for s, filas in _RANURAS.items():
        tanda, nota = _SEC[s]
        for k, i in enumerate(filas, 1):
            n = _N9.get(i) or ('§%d %d/%d: %s' % (s, k, len(filas), nota))
            out[i] = n + ' ‖ ' + _FORMA % (s, tanda)
    return out


DOCX_NOTAS = OrderedDict([('sus', _notas_docx())])

# ==========================================================================
# Pistas por celda (extraer_textos.py → textos_es.json → tandas)
# ==========================================================================
_CASO = ('US §8: caso US = 115 covers/día equivalentes (≈ 70 en sala, 40 plazas: 10 en la barra y 30 en mesas; ≈ 25 de '
         'take-out/pickup = 15.6 pedidos; ≈ 20 de marketplace = 12.5 pedidos; 1 pedido = 1.6 covers) × $32.50 (sin sales '
         'tax ni propina) × 310 días (abre 6 días, cierra el lunes); servicio en mesa con servers; beer, sake & wine; sin '
         'cifras del ES ni historia de versiones')
CELDA_PISTAS = OrderedDict([
    (('SUSP', _S, 'A2'), 'D8: añade una vez que los importes van «in your currency» (sin símbolo)'),
    (('SUSP', _S, 'C4'), _CASO + '; media del año 1 con la rampa de apertura; compárala con tus reservas y con el paso de '
                                 'gente de tu calle'),
    (('SUSP', _S, 'C5'), _CASO + '; check de $32.50 por cover equivalente = sala 70 × $36.00 (comida $28.50 + bebida '
                                 '$7.50) + take-out 15.6 pedidos × $41.00 + marketplace 12.5 pedidos × $46.00 (carta un 15 % '
                                 'más cara y pedido algo mayor) = (2,520 + 640 + 575) ÷ 115 = $32.48 (Kit estimate, US §8); '
                                 'el precio con impuesto lo calcula la fila "Menu price incl. sales tax"'),
    (('SUSP', _S, 'C6'), _CASO + '; 310 días = 6 días a la semana (cierra el lunes) menos Thanksgiving, Christmas Day y New '
                                 'Year\'s Day'),
    (('SUSP', _S, 'C8'), 'Sobre el año 2. Conservador: el techo lo ponen la barra (10 plazas), las 40 plazas del viernes y '
                         'el sábado por la noche y lo que puede cortar el equipo de sushi'),
    (('SUSP', _S, 'C13'), 'US §5.2 y §8: food cost 32 % (Kit estimate; los blogs de consultoría dan 30-40 %): el coste '
                          'TEÓRICO por pieza de la calculadora del kit sale más bajo (la media de la carta, con el nigiri '
                          'de salmón y el California roll baratos y el spicy tuna caro); el 32 % es el consumo real de '
                          'TODA la carta con la merma del sushi case, los recortes, el arroz y el nori que se tiran, las '
                          'comidas del personal y las invitaciones; sin cifra de la calculadora inventada'),
    (('SUSP', _S, 'C14'), 'US §8: beverage cost 24 % (cerveza, sake y vino ≈ 70 % de la bebida; refrescos y té; Kit '
                          'estimate): pide el precio del sake por escrito a tu distribuidor'),
    (('SUSP', _S, 'C15'), 'US §8: disposables 3 % (bandejas de sushi, tarrinas de soja, palillos, bolsas y servilletas; '
                          'packaging ordinances locales)'),
    (('SUSP', _S, 'C16'), 'US §8: 15 % de las ventas por marketplaces (DoorDash, Uber Eats, Grubhub); el pickup directo '
                          'por teléfono o web no paga comisión: empújalo; los rolls y los platters viajan bien, la tempura '
                          'no'),
    (('SUSP', _S, 'C17'), 'PIZ-US §5.3: 25 % = plan Plus de DoorDash / Uber Eats (Basic 15 %, Premier 30 %; + 6-10 % en '
                          'pickup por la app); compruébalo en tu contrato'),
    (('SUSP', _S, 'C24'), 'US §8: $4,500/mes = 1,800 sq ft × ~$30/sq ft/año (Kit estimate, editable); local de segunda '
                          'generación que ya fue restaurante, con campana posible'),
    (('SUSP', _S, 'C26'), 'US §8: $1,700/mes (gas de las arroceras, la freidora y el range; walk-in, reach-in, freezer y '
                          'sushi case; campana y HVAC; Kit estimate): pide el histórico del local'),
    (('SUSP', _S, 'C27'), 'US §8: $8,000/año = general liability + product liability (pescado crudo) + liquor liability '
                          '(beer, sake & wine) + property + workers\' comp (Kit estimate)'),
    (('SUSP', _S, 'C31'), 'US §8: SBA 7(a) al 10 % a 10 años, sin interest-only; el préstamo lo calcula "Financing"'),
    (('SUSP', _S, 'C51'), 'US §1: 40 plazas: 10 en el sushi bar frente al sushi case y 30 en mesas (sin patio); quien se '
                          'lleva el pedido o lo recibe en casa no ocupa mesa'),
    (('SUSP', _S, 'C58'), 'Media ponderada: la sala y el pickup cobran al momento y los marketplaces liquidan cada semana lo '
                          'que venden (el 15 % de las ventas)'),
    (('SUSP', _S, 'C59'), 'Plazo de pago a los proveedores de pescado, arroz, nori y bebida (14 días en el caso): '
                          'negócialo por escrito; si el proveedor de pescado pide pago semanal o COD, baja la cifra'),
    (('SUSP', _N, 'A8'), 'SPEC §4.1 línea 4 (Bar): sin divisores 1,10/1,21 → «divide a menu price by 1 + your sales tax '
                         'rate»; P&L excl. sales tax, cash flow incl.; un solo tipo en el ejemplo (B39 = B40 = 8 %)'),
    (('SUSP', _N, 'A10'), 'F1-camino §6: Mes 1 = ENERO, en el orden del calendario (enero el más flojo; febrero, mayo y '
                          'diciembre, los picos); sin «agosto con cierre»'),
    (('SUSP', _N, 'A12'), 'El Word cita las cifras de este Excel (si cambias el libro, manda el Excel); la calculadora del '
                          'pescado, el arroz y el coste por pieza (Sushi Fish, Rice & Costing Calculator) va aparte y su '
                          'food cost por pieza NO se copia en "0. Assumptions" (allí va el food cost medio de toda la '
                          'carta, con la merma)'),
    (('SUSP', _P, 'F10'), 'US §8: sushi, rolls, sashimi, poke, appetizers (edamame, gyoza, tempura), miso y postres: ≈ 67 % '
                          'en sala, ≈ 17 % take-out y ≈ 15 % por marketplaces; un solo sales tax en el ejemplo'),
    (('SUSP', _E, 'E25'), 'US §8: 3 servicios completos por plaza y día (comida, cena y un segundo turno de cena el viernes '
                          'y el sábado; estancias de 45-60 min); techo físico, no objetivo; el equilibrio de caja pide '
                          'menos (fila 26)'),
])
for _f, _nota in [(7, 'US §8: plan review y permit fees ($14,000 con los planos MEP y de la campana; la tasa de plan '
                      'review de un HACCP plan del arroz, si eliges variance, puede pasar de $2,000 en algún condado, US '
                      '§6.2); sin licencia ni declaración responsable españolas'),
                  (8, 'US §8: local de segunda generación (ya fue restaurante) de 1,800 sq ft con la barra de sushi de '
                      'obra a la vista; incluye signage & facade ($5,000 de las 18 partidas de US §8)'),
                  (9, 'US §8: Type I hood de ≈ 10 ft + supresión UL 300 + makeup air ($18,000) sobre la freidora de '
                      'tempura, el range y el griddle; NADA de la ordenanza de Madrid ni del conducto a cubierta'),
                  (10, 'US §8: parte de «electrical, HVAC, plumbing & grease interceptor» ($26,000 en total): el servicio '
                       'eléctrico del frío, el sushi case y la campana; pregunta la potencia disponible ANTES de firmar'),
                  (11, 'US §8: la otra parte de los $26,000: fontanería, grease interceptor, HVAC y las líneas de gas de '
                       'las arroceras y la freidora'),
                  (12, 'US §4: sushi case refrigerado de 6 ft (Hoshizaki HNC-180BA-L-SL 70.9 in, $4,045; Mission 71 in '
                       '$4,020; webstaurantstore/howdybrewer, oct-2026); solo para la neta del servicio, no para guardar '
                       'pescado'),
                  (13, 'US §8: dos arroceras de gas comerciales y rice warmers ($2,500, Kit estimate: sin precio leído); el '
                       'hangiri va en el utillaje'),
                  (14, 'US §6.1: el freezer guarda el stock de pescado YA tratado a −4 °F o menos con registrador (los '
                       'registros de parásitos se guardan 90 días); congelar tú mismo (−4 °F × 7 días) ocupa mucho freezer: '
                       'el caso compra el pescado tratado o exento con la carta del proveedor; un ultracongelador de −31 °F '
                       'no tiene precio leído'),
                  (15, 'US §8: freidora (tempura), range (miso, caldos) y griddle (gyoza, teriyaki), todo bajo el Type I '
                       'hood ($6,000, Kit estimate)'),
                  (16, 'OJO: la nota ES habla de la campana, que en el caso US va en la fila 9: aquí escribe la del walk-in '
                       'cooler 6×8 (Norlake Kold Locker $12,808, webstaurantstore): la cámara del pescado, el arroz y la '
                       'verdura'),
                  (17, 'US §8: reach-in de pescado a 32-34 °F, mesas refrigeradas de trabajo de la barra, nevera de beer, '
                       'sake & wine y máquina de hielo ($11,000, Kit estimate); cold holding ≤ 41 °F'),
                  (18, 'US §8: 3-comp sink, lavavajillas, lavamanos de la barra y de la cocina, estanterías e inox'),
                  (19, 'US §8: cuchillos japoneses (yanagiba, deba), tablas por colores, hangiri, pH-metro calibrado (solo '
                       'si eliges variance), sondas, básculas en oz y la estación de empaquetado to-go ($6,000)'),
                  (20, 'US §1: 40 plazas: 10 taburetes en el sushi bar y 30 en mesas, sin patio'),
                  (21, 'US §8: POS con online ordering, KDS (pantalla de cocina y de barra) y las tablets de los '
                       'marketplaces; sin Veri*factu'),
                  (24, 'US §8: pescado (comprado ya tratado o exento, con su carta), arroz Calrose, nori, salsas, '
                       'envases to-go y bebida (beer, sake & wine)')]:
    CELDA_PISTAS[('SUSP', _I, 'D%d' % _f)] = _nota
for _f in range(7, 25):
    CELDA_PISTAS.setdefault(('SUSP', _I, 'D%d' % _f), 'Nota de la partida del ejemplo US (rótulo fijado de la col. A en '
                                                       '"fijos_en"); sin marcas ni normas españolas: solo rangos con '
                                                       'fuente de US §4 o ninguno')
# Staffing J5:J11: cada puesto US en la fila ES de su jornada (FIJOS): la nota describe el puesto US, no el ES
for _f, _nota in [(5, 'Owner / GM (1 × 1.0, $4,500/mes): compras, proveedores de pescado y sus cartas, sala, '
                      'marketplaces y gestión; en EE. UU. el dueño NO es el itamae (se contrata); cobra por debajo de un '
                      'manager: «owner\'s draw in addition from net profit»'),
                  (6, 'Head sushi chef / itamae (1 × 1.0, $5,199/mes ≈ $30/h, BLS 35-1011): compra y corta el pescado, '
                      'lleva la barra, firma la carta, el SOP del arroz y los registros de parásitos; contrátalo antes de la '
                      'obra'),
                  (7, 'Kitchen line cook (1 × 1.0, $3,119/mes ≈ $18/h): arroceras, tempura, gyoza, miso y teriyaki'),
                  (8, 'Sushi chef (1 × 1.0, $3,639/mes ≈ $21/h, Indeed $20.72): rolls, platters de los marketplaces y la '
                      'barra cuando el head sushi chef no está; con un solo cortador, una baja cierra la barra'),
                  (9, 'Servers, host & to-go packing (4 × 0.75, $7,798/mes en total ≈ $15/h de base): sala, reservas, '
                      'pickup y empaquetado; las propinas van aparte y son del equipo'),
                  (10, 'Sushi chef part-time W-2 (1 × 0.6, $2,080/mes ≈ $20/h): cenas del viernes y el sábado y los '
                       'platters por encargo; nunca como 1099'),
                  (11, 'Dish & prep (1 × 1.0, $2,773/mes ≈ $16/h): friegue, lavado del arroz y mise en place')]:
    CELDA_PISTAS[('SUSP', _R, 'J%d' % _f)] = _nota
for _f, _nota in [(21, 'US §8: 7.5 h de servicio al día (11:30-14:30 y 17:00-21:30; 22:00 viernes y sábado)'),
                  (22, 'US §8: 4.5 personas de media a la vez (barra, cocina caliente, sala y to-go); el viernes y el '
                       'sábado por la noche hacen falta más'),
                  (23, 'US §8: 3 h de producción (arroz, corte del saku, salsas, mise en place) antes de abrir'),
                  (24, 'US §8: 2 personas en producción (head sushi chef y line cook)')]:
    CELDA_PISTAS[('SUSP', _R, 'J%d' % _f)] = _nota
# Tabla D19 (Instrucciones 35-46, 12 filas como el ES): «US SUSHI RESTAURANT BENCHMARKS (sourced) AND KIT ESTIMATES»
# (Benchmark | Value | Source | Note). Cada fila sustituye a la ES de la misma fila; solo lo «leído» con fuente; lo
# «(resumen)» = Kit estimate
_D19 = OrderedDict([
    (35, 'fila → «Month 1 of the plan» · «January» · «Plan decision» · nota: orden del calendario; enero el más flojo; '
         'febrero, mayo y diciembre, los picos; si abres en otro mes, gira la fila de "12-Month Cash Flow"'),
    (36, 'fila (sustituye el sushi en el reparto de Just Eat) → «Consumer demand (US searches)» · «"sushi restaurant" about '
         '201,000 a month; "sushi bar" 27,100; "sushi takeout" 9,900» · «DataForSEO, US, Oct 2026» · nota: demanda de '
         'consumo, no de compradores del plan'),
    (37, 'fila → «Menu prices in mid-size cities» · «nigiri $5-7 a pair; classic roll $7-9; specialty roll $13-18» · «Kit '
         'estimate (three menus read Oct 2026, +10-20% to 2026 prices)» · nota: este plan, comensal de sala $36.00 '
         '(comida $28.50 + bebida $7.50)'),
    (38, 'fila → «Cost per piece» · «theoretical cost of each nigiri, roll and platter by channel» · «Kit estimate (Sushi '
         'Fish, Rice & Costing Calculator)» · nota: el 32 % del plan es el consumo real de toda la carta, con la merma '
         '(sin cifra de la calculadora: la pone el orquestador tras generarla)'),
    (39, 'fila → «Salmon yield» · «usable loin 45-60% of a whole fish; a fillet about 85%» · «Secondary sources (summary) '
         'and Kit estimate» · nota: mide el tuyo con 3 pescados en la hoja «Fish Yield» de la calculadora'),
    (40, 'fila → «Sushi rice (Calrose, 50 lb bag)» · «$51.99 ($1.04/lb)» · «webstaurantstore.com, read Oct 2026» · nota: '
         'el arroz es barato: el coste está en el pescado y en la mano del sushi chef'),
    (41, 'fila → «Delivery marketplace commission» · «DoorDash 15 / 25 / 30% + 6% pickup; Uber Eats 15-30%» · '
         '«merchants.ubereats.com; DoorDash tiers (Oct 2026)» · nota: este plan, 25 % sobre el 15 % de las ventas; el '
         'pickup directo no paga comisión'),
    (42, 'fila (sustituye el IVA del sushi) → «Sales tax» · «8% (example: state + local)» · «Kit example: look up your '
         'state and city rate» · nota: un solo tipo en el libro; algunos estados gravan distinto la comida para llevar'),
    (43, 'fila (sustituye el anisakis del RD 1021/2022) → «Fish served raw (parasite destruction)» · «−4 °F for 168 h (7 '
         'days), or −31 °F until solid + 15 h, or −31 °F + −4 °F for 24 h; tuna and feed-raised aquaculture fish exempt» '
         '· «FDA Food Code 2022 (3-402.11, 3-402.12)» · nota: compra el pescado ya tratado, con la carta del proveedor; '
         'guarda los registros 90 días'),
    (44, 'fila (sustituye el shari del art. 30.5) → «Sushi rice held at room temperature» · «TPHC: up to 4 h with the '
         'time marked and a written procedure, then discard; or a variance with a HACCP plan (example limit pH < 4.2)» · '
         '«FDA Food Code 2022 (3-501.19, 3-502.11)» · nota: tu condado decide: pídelo por escrito antes de abrir'),
    (45, 'fila (sustituye el SMI) → «Minimum wage» · «federal $7.25/h + your state» · «U.S. Department of Labor '
         '(dol.gov)» · nota: este plan presupuesta ≥ $15/h; teclea el suelo de tu estado en "0. Assumptions"'),
    (46, 'fila (sustituye el convenio) → «Labor cost / sales» · «about 30-35% with table service» · «Kit estimate» · nota: '
         'las propinas de los servers van aparte y no son coste del local; un head sushi chef bueno no es barato'),
])
for _f, _p in _D19.items():
    for _col in 'ABCD':
        CELDA_PISTAS[('SUSP', _N, '%s%d' % (_col, _f))] = _p

# Pistas por TEXTO propias del sushi bar (se suman a las de extraer_textos.PISTAS): US §6 y §9
PISTAS_EXTRA = [
    (r'[Cc]omensal|[Cc]ubierto', 'US §8: el caso cuenta «covers» (115 equivalentes; 1 order = 1.6 covers); «orders» para '
                                 'take-out y marketplace; nunca «customers» para el volumen diario'),
    (r'[Pp]edido', 'take-out order · pickup order · marketplace order (1 order = 1.6 covers)'),
    (r'[Ii]tamae|[Ss]ushiman|[Ss]ushiwoman', 'head sushi chef (itamae, glosado una vez) · sushi chef; NUNCA «sushiman»'),
    (r'[Vv]itrina', 'sushi case (refrigerated display): solo para la neta del servicio'),
    (r'\b[Nn]eta\b|[Ss]hari|sushi-zu|\b[Ss]aku\b|[Hh]angiri', 'neta (topping) · sushi rice (shari) · sushi vinegar '
                                                             '(sushi-zu) · saku block · hangiri'),
    (r'[Nn]igiri|[Ss]ashimi|[Hh]osomaki|[Uu]ramaki|[Tt]emaki|[Mm]aki', 'nigiri · sashimi · maki (thin roll) · inside-out '
                                                                        'roll · hand roll · classic roll · specialty roll'),
    (r'[Cc]ombinado|[Bb]andeja', 'sushi platter / combo · party platter (encargo)'),
    (r'[Ss]urimi|[Cc]angrejo', 'imitation crab («kani» o «krab» en carta)'),
    (r'[Aa]nisakis|[Cc]ongela|[Pp]ar[aá]sit|−20|-20', 'US §6.1: parasite destruction (Food Code 3-402.11): −4 °F 7 días o '
                                                      'las dos de −31 °F; atún y acuicultura con pienso exentos con '
                                                      'declaración; supplier letter; registros 90 días'),
    (r'[Aa]rroz|pH|[Aa]cidific', 'US §6.2: sushi rice = TCS: TPHC 4 h (3-501.19) por defecto o variance + HACCP plan '
                                 '(3-502.11; pH del condado); sin pH «legal»'),
    (r'[Hh]istamina|[Aa]t[uú]n', 'scombrotoxin (histamine): receiving ≤ 40 °F; tuna species exempt from freezing in the US'),
    (r'[Ss]almón', 'farmed Atlantic salmon (feed-raised aquaculture: exempt with a written supplier statement)'),
    (r'[Ss]ushi grade|[Ss]ashimi grade', '«sushi-grade» no tiene definición legal: solo para negarlo'),
    (r'[Ii]nformaci[oó]n al (?:cliente|consumidor)|[Cc]artel|art\. 8\.2', 'consumer advisory (3-603.11): disclosure + '
                                                                          'reminder, también en los listados online'),
    (r'\bSL\b|aut[oó]nomo|IAE|Seguridad Social|alta en', '«LLC vs S corp with your CPA» · «EIN + state payroll / '
                                                         'unemployment registration»'),
    (r'Veri\*?factu|TPV', '«POS that reports sales tax» (sin Veri*factu)'),
    (r'[Uu]rbanism|[Ll]icencia de (?:actividad|apertura|obra)|compatibilidad|declaraci[oó]n responsable',
     '«zoning check before signing» · «building permit + certificate of occupancy» · business license + sales tax permit'),
    (r'[Tt]erraza', 'el caso US no tiene patio (40 plazas en sala y barra)'),
    (r'alcohol|cerveza|vino|sake', 'US §6.7: «beer & wine license» (el sake suele ir con la de vino: «ask your state ABC»; '
                                   '«apply early», sin prometerla) · liquor liability'),
    (r'[Hh]umos|[Cc]ampana|extracci|[Cc]onducto', 'US §6.7: Type I hood + fire suppression (UL 300) + makeup air sobre la '
                                                  'freidora de tempura; «ask the fire marshal in writing»'),
    (r'[Rr]egistro sanitario|RGSEAA|APPCC|autocontrol', 'plan review (Food Code 8-201.11) + health permit + inspection; '
                                                        'written food safety plan (HACCP plan solo si hay variance)'),
    (r'[Ee]xtintor', 'Class K + 2-A extinguishers'),
    (r'[Gg]rasas|aceite usado', 'grease interceptor · used cooking oil pickup'),
    (r'°C', 'US: cold holding ≤ 41 °F; receiving de atún ≤ 40 °F; freezer −4 °F; hot holding ≥ 135 °F; la métrica solo '
            'entre paréntesis'),
    (r'irrellenable|Ley 1/2025|Ley 7/2022|desperdicio', 'sin equivalente US: packaging ordinances locales'),
    (r'[Rr]eclamaciones', 'required public notices (health permit, beer & wine license, labor law posters)'),
    (r'[Cc]onvenio|[Cc]ontrato|n[oó]mina|registro de jornada', 'offer letters, I-9, W-4, state minimum wage, W-2 por '
                                                               'horas (sin convenio; sin «digital obligatorio»)'),
    (r'PRL|[Pp]revenci[oó]n de riesgos|EPI', 'OSHA basics (cortes con los cuchillos, quemaduras de la freidora)'),
    (r'[Mm]anipulador|[Ff]ormaci[oó]n', 'Certified Food Protection Manager (2-102.12) + food handler cards (según estado)'),
    (r'[Aa]l[eé]rgen|s[eé]samo|soja|mostaza', 'US §6.4: 9 major allergens incl. sesame (UK 14); soy sauce = soy + wheat; '
                                              'spicy mayo = egg; cream cheese = milk; moluscos y mostaza NO son major en '
                                              'EE. UU.'),
    (r'[Gg]luten|cel[ií]ac', 'US §6.4: NO prometer «gluten-free» (21 CFR 101.91); tamari solo si la etiqueta lo dice'),
    (r'[Rr]ider|[Rr]epart', 'own drivers = W-2 + hired & non-owned auto insurance (check your state); el caso no tiene '
                            'reparto propio'),
    (r'[Pp]lataforma|Glovo|Just Eat|Uber|delivery', 'DoorDash / Uber Eats / Grubhub con sus tiers (PIZ-US §5.3)'),
    (r'[Ee]nvase|tarrina|bolsa|caja', 'sushi trays, soy cups, chopsticks, bags; local packaging ordinances'),
    (r'SGAE|AGEDI', '«Music licensing (ASCAP/BMI/SESAC)»'),
    (r'[Mm]en[uú] del d[ií]a|mediod[ií]a', 'lunch specials (bento or roll combos): el «menú del día» español no cruza'),
    (r'[Aa]gosto|vacaciones', 'el caso US no cierra en agosto: cierra el lunes y tres festivos'),
    (r'San Valent[ií]n|Nochebuena|Nochevieja', 'Valentine\'s Day · New Year\'s Eve party platters · holiday parties'),
    (r'[Tt]emporada', 'fish seasonality (ask your supplier): sin el calendario español'),
    (r'[Bb]arra\b', 'sushi bar / sushi counter (10 plazas) · chef\'s counter (solo omakase)'),
]

# Glosario del sushi bar (US §9, OBLIGATORIO; manda sobre el de FT/CAF)
GLOSARIO_SUS = OrderedDict([
    ('sushi bar (negocio)', 'sushi restaurant (título) · sushi bar (prosa)'),
    ('itamae · sushiman', 'head sushi chef · sushi chef; «itamae» glosado una vez; NUNCA «sushiman»'),
    ('barra de sushi · vitrina de neta', 'sushi bar / sushi counter · sushi case (refrigerated display) · «chef\'s '
                                         'counter» (omakase)'),
    ('neta · shari · sushi-zu · saku', 'neta (topping) · sushi rice (shari) · sushi vinegar (sushi-zu) · saku block'),
    ('nigiri · sashimi · hosomaki · uramaki · temaki · futomaki', 'nigiri · sashimi · maki (thin roll) · roll / inside-out '
                                                                 'roll · hand roll · futomaki; «classic roll», '
                                                                 '«specialty roll»'),
    ('combinado', 'sushi platter / combo · «party platter» (encargo)'),
    ('surimi', 'imitation crab («kani» o «krab» en carta)'),
    ('para llevar · plataforma', 'take-out / to-go / pickup · third-party delivery marketplace'),
    ('comensal equivalente · ticket', 'covers · average check (excl. sales tax and tip)'),
    ('escandallo', 'recipe costing · cost per piece / per roll'),
    ('congelación anti-anisakis', 'parasite destruction (freezing) · «frozen per Food Code 3-402.11» · supplier letter'),
    ('control por tiempo del arroz · validación', 'TPHC (time as a public health control) · variance · HACCP plan · pH log'),
    ('información al consumidor', 'consumer advisory (disclosure + reminder)'),
    ('histamina', 'scombrotoxin (histamine) · receiving temperature'),
    ('manipulador · APPCC', 'food handler card · CFPM · HACCP'),
    ('merma de vitrina', 'shrink · case waste'),
    ('−20 °C 24 h', '−4 °F for 7 days (or the −31 °F options)'),
    ('art. 30.5', 'TPHC or variance'),
    ('registro sanitario', 'health permit + plan review'),
    ('licencia de apertura', 'business license + certificate of occupancy'), ('convenio', 'state/local minimum wage'),
    ('IVA · fianza', 'sales tax · deposit'), ('autónomo / SL', 'LLC'),
    ('menú del día', 'lunch special'),
])


# ==========================================================================
# Caso de ejemplo US (research US §8; F1-camino §6): celdas VERDES. (corto, hoja ES, celda) → (valor, rótulo)
# ==========================================================================
# Mes 1 = ENERO (F1-camino §6): los pesos de US §8 en el orden del calendario, sin girar
ESTACIONALIDAD_US = (0.078, 0.086, 0.084, 0.082, 0.086, 0.084, 0.082, 0.080, 0.080, 0.084, 0.082, 0.092)   # ene → dic
assert abs(sum(ESTACIONALIDAD_US) - 1) < 1e-9


def valores_sus(M):
    v = OrderedDict()
    sup = [
        ('B4', 115, 'Comensales/día'), ('B5', 32.5, 'Ticket medio'), ('B6', 310, 'Días de apertura'),
        ('B7', 0.06, 'Crecimiento de volumen del año 2'), ('B8', 0.04, 'Crecimiento de volumen del año 3'),
        ('B11', 0.85, 'Ventas de COMIDA'), ('B13', 0.32, 'Coste de mercancía sobre las ventas de COMIDA'),
        ('B14', 0.24, 'Coste de mercancía sobre las ventas de BEBIDA'), ('B15', 0.03, 'Consumibles'),
        ('B16', 0.15, 'Ventas por delivery'), ('B17', 0.25, 'Comisión de la plataforma'),
        ('B18', 0.03, 'Comisión de los medios de pago'), ('B20', 0.10, 'Seguridad Social'),
        ('B21', 12, 'Número de pagas'), ('B22', 15080, 'SMI anual'), ('B24', 4500, 'Alquiler mensual'),
        ('B25', 2, 'Fianza'), ('B26', 1700, 'Suministros'), ('B27', 8000, 'Seguros'), ('B28', 0.01, 'Varios'),
        ('B30', 130000, 'Recursos propios'), ('B31', M.CALIBRAR, 'Préstamo bancario'), ('B32', 0.10, 'Tipo de interés'),
        ('B33', 10, 'Plazo del préstamo'), ('B34', 0, 'Carencia'), ('B35', 3, 'Fondo de maniobra'),
        ('B37', 0.25, 'Impuesto de Sociedades, nueva'), ('B38', 0.25, 'Impuesto de Sociedades, tipo'),
        ('B39', 0.08, 'IVA repercutido de restauración'), ('B40', 0.08, 'IVA repercutido/soportado'),
        ('B41', 0, 'IVA soportado en compras'), ('B42', 0, 'Bases negativas'),
        ('B44', 10, 'Vida útil de obra'), ('B45', 7, 'Vida útil de maquinaria'),
        ('B51', 40, 'Aforo'), ('B52', 0.75, 'Actividad del mes 1'), ('B53', 4, 'Meses hasta alcanzar'),
        ('B54', 2, 'Meses de alquiler ANTES'), ('B55', 0.10, 'Imprevistos sobre las partidas de OBRA'),
        ('B58', 2, 'Días medios de cobro'), ('B59', 14, 'Días medios de pago'),
        ('B62', 0.70, 'Bebida que compras al 21'), ('B63', 0.08, 'IVA de la bebida ALCOHÓLICA'),
        ('B65', 1.15, 'DSCR mínimo'), ('B66', 1.25, 'DSCR objetivo'), ('B67', 0.15, 'Holgura mínima'),
        ('B68', None, 'Suelo salarial anual'),
    ]
    for c, val, rot in sup:
        v[('SUSP', _S, c)] = (val, rot)
    # Inversión (US §8 en 18 filas, FIJOS): filas 7-24 = $223,800; los imprevistos (B27) van por fórmula (10 % de 7-11 =
    # $13,300: la base incluye arquitecto y rótulo, = Taco y Rotisserie EN; US §8 decía $12,800 sobre 2-5)
    for k, val in enumerate([14000, 75000, 18000, 11000, 15000, 4000, 2500, 3500, 6000, 12800, 11000, 11500, 6000,
                             14000, 4500, 2500, 5500, 7000]):
        v[('SUSP', _I, 'B%d' % (7 + k))] = (val, None)
    # P&L: fijos B26-B34 ($28,000, US §8), G13 (soportado de la bebida: valor en el ES) → 0, H11 → 70 % (beer, sake &
    # wine sobre la bebida, = B62), umbrales del semáforo (el margen «bruto» del libro descuenta TODOS los variables: con
    # 41.6 % de variables del caso, el suelo es 55 %; COGS 33 %; personal 36 %; alquiler 10 %; neto 5 %)
    for k, val in enumerate([4200, 3600, 7000, 3600, 2400, 1800, 900, 1000, 3500]):
        v[('SUSP', _P, 'B%d' % (26 + k))] = (val, None)
    v[('SUSP', _P, 'G13')] = (0, None)
    v[('SUSP', _P, 'H11')] = (0.70, None)
    for c, val, rot in [('E50', 0.55, 'Margen bruto'), ('E52', 0.33, 'Coste de mercancía /'),
                        ('E53', 0.36, 'Coste de personal'), ('E54', 0.10, 'Alquiler'), ('E55', 0.05, 'Resultado neto')]:
        v[('SUSP', _P, c)] = (val, rot)
    # Staffing (US §8, en la fila ES de su jornada): personas (B), FTE por persona (C), bruto mes TOTAL de la fila (D);
    # ≥ $15/h, 12 pagas, propinas aparte; servers, host & to-go = 4 personas en una fila (E4) → 8.6 FTE, $29,108/mes.
    # Cobertura: servicio 7.5 h × 4.5 + producción 3 h × 2 (US §8)
    for f, (b, c, d) in zip(range(5, 12), [(1, 1.0, 4500), (1, 1.0, 5199), (1, 1.0, 3119), (1, 1.0, 3639),
                                           (4, 0.75, 7798), (1, 0.6, 2080), (1, 1.0, 2773)]):
        for col, val in zip('BCD', (b, c, d)):
            v[('SUSP', _R, '%s%d' % (col, f))] = (val, None)
    v.update([(('SUSP', _R, 'B14'), (5000, 'Coste anual')), (('SUSP', _R, 'B15'), (5000, 'Coste anual')),
              (('SUSP', _R, 'B21'), (7.5, 'Horas de servicio')), (('SUSP', _R, 'B22'), (4.5, 'Personas necesarias')),
              (('SUSP', _R, 'B23'), (3, 'Horas de producción')), (('SUSP', _R, 'B24'), (2, 'Personas en el turno'))])
    # Break-Even!B25 (techo de rotaciones) = 3 (US §8 = ES): comida, cena y segundo turno de cena el viernes y el sábado.
    # El caso da 115 / 40 = 2.9 por plaza (con el take-out y el marketplace) y el equilibrio de caja pide ≈ 2.2: cabe
    v[('SUSP', _E, 'B25')] = (3, 'Rotaciones al día que da el local')
    # Escenarios (US §8): pesimista 95 · $30.50 · 305 / optimista 135 · $34.50 · 312
    v.update([
        (('SUSP', _ES, 'B5'), (95, 'Comensales/día')), (('SUSP', _ES, 'D5'), (135, 'Comensales/día')),
        (('SUSP', _ES, 'B6'), (30.5, 'Ticket')), (('SUSP', _ES, 'D6'), (34.5, 'Ticket')),
        (('SUSP', _ES, 'B7'), (305, 'Días')), (('SUSP', _ES, 'D7'), (312, 'Días')),
    ])
    # Estacionalidad (US §8, Mes 1 = ENERO sin girar: F1-camino §6) → Month 1-12
    for col, val in zip('BCDEFGHIJKLM', ESTACIONALIDAD_US):
        v[('SUSP', _T, '%s5' % col)] = (val, 'Estacionalidad')
    return v


# Calibración D15 (US §8: palancas en su orden; máx. 3 vueltas). Cada celda, citada en F2-NOTAS.md (G7)
CALIBRACION_D15 = OrderedDict()


def formulas_sus():
    p = os.path.join(AQUI, 'formulas_sus.json')
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
    M.TOKENS_DOCX = tokens_sus(M.TOKENS_DOCX)
    M.PRODUCTOS_CIERRE = PRODUCTOS_CIERRE_SUS
    M.DOCX_FIJOS = docx_fijos(M)
    M.DOCX_NOTAS = DOCX_NOTAS
    M.DOCX_NOTAS_PLAN = DOCX_NOTAS_PLAN
    M.FORMULAS_EN = formulas_sus()
    M.VALORES_EN = valores_sus(M)
    M.CALIBRACION_D15 = CALIBRACION_D15
    M.CELDA_PISTAS = CELDA_PISTAS
    M.PISTAS_EXTRA = PISTAS_EXTRA
    M.CIFRAS_PROHIBIDAS = cifras_prohibidas(M.VALORES_EN)
    M.RX_SUS_NO = RX_SUS_NO
    M.REGLA_UNIDADES = REGLA_UNIDADES
    glo = OrderedDict(M.GLOSARIO)
    for k, val in GLOSARIO_SUS.items():
        glo[k] = val                          # research §9 manda (regla de jerga §0)
    M.GLOSARIO = glo
