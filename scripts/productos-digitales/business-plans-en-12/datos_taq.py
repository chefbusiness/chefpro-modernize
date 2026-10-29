#!/usr/bin/env python3
"""
datos_taq.py — Taco Shop Business Plan Kit (EN) · los datos ES→EN que dependen del contenido: rótulos fijados
(inversión 19 → 18 filas, fijos 10 → 9, plantilla 6 + suplencias), POR_CELDA, pistas, tokens del docx, fijos y notas del
docx, caso US (research US §8, Mes 1 = enero), cifras ES prohibidas y RX_TAQ_NO (F1-camino §7) y glosario (US §9). Lo
llama `mapas_taq.instalar()` con el módulo `mapas` YA cargado con los datos de FT/CAF (FIJOS comunes del motor 2.2,
TOKENS_DOCX). Clon de `../business-plans-en-8/datos_piz.py` (misma rejilla: las celdas son las de la pizza) con las
cifras prohibidas en cadena de `../business-plans-en-10/datos_ice.py`. Sesión Claude Code, 29-oct-2026 (F2-EN).
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
TAQES = os.path.join(PD, 'plan-taqueria')                 # ES cerrado: F1-camino, research y cifras_caso_es.json

URL_TAQ = 'aichef.pro/en/digital-products/taco-shop-business-plan'
_I, _S, _P, _R, _N, _E, _ES, _T = ('Inversión Inicial', '0. Supuestos', 'PyG 3 Años', 'Personal', 'Instrucciones',
                                   'Punto Equilibrio', 'Escenarios', 'Tesorería 12 meses')
REGLA_UNIDADES = ('MEDIDAS US (John, 13-oct): principales lb y oz, °F, gallons / quarts y sq ft; la métrica entre '
                  'paréntesis para UK y Australia: «1.5 oz (43 g)», «145 °F (63 °C)», «1,200 sq ft (111 sq m)», '
                  '«30 lb (13.6 kg)»; tortillas en pulgadas «6 in (15 cm)»; nada de kg, g, km, litros ni °C como unidad '
                  'principal (gate)')

# ==========================================================================
# FIJOS (por TEXTO ES, en cualquier celda de los 2 libros). Parten de los de FT/CAF (los del motor 2.2)
# ==========================================================================
FIJOS_FUERA = ('Este fichero forma parte del producto «plan-negocio-food-truck» de AI Chef Pro.',
               'Este fichero forma parte del producto «plan-negocio-cafeteria» de AI Chef Pro.')
_TITULO_CHECK = 'TACO SHOP STARTUP CHECKLIST'
FIJOS_NUEVOS = OrderedDict([
    # Instrucciones!A3 del checklist con el nombre comercial
    ('Este fichero forma parte del «Plan de Negocio: Taquería» de AI Chef Pro.',
     'This file is part of the Taco Shop Business Plan Kit by AI Chef Pro.'),
    # títulos: «taco shop» en el nombre, «taqueria» en prosa; nunca «authentic» ni «Tex-Mex» (US §9)
    ('CHECKLIST DE APERTURA — TAQUERÍA', _TITULO_CHECK),
    ('INSTRUCCIONES DE USO — Plan financiero Taquería',
     'HOW TO USE THIS WORKBOOK — Taco Shop Financial Projections'),
    ('PLAN DE NEGOCIO: TAQUERÍA', 'TACO SHOP BUSINESS PLAN: COUNTER-SERVICE TAQUERIA'),
    ('Inversión inicial estimada — taquería con trompo, barra de salsas, 32 plazas y terraza',
     'Estimated Startup Costs — counter-service taco shop with trompo and salsa bar, 30 seats + patio'),
    ('Ajusta las cifras a tu proyecto: son las de un caso tipo en una ciudad media, sin traspaso. Pon tus presupuestos '
     'reales en las celdas de importe.', 'US kit example (2026) — replace with your own quotes.'),
    ('Escenario realista — taquería con trompo, barra de salsas y para llevar',
     'Base case — counter-service taco shop with trompo, salsa bar and take-out'),
    ('Punto de equilibrio mensual y diario — taquería con trompo',
     'Monthly and daily break-even — taco shop with trompo'),
    # cabecera de la tabla D19 y fase 2 del checklist con el nombre de su pestaña (US §9)
    ('DATOS DE REFERENCIA DEL SECTOR', 'US TAQUERIA BENCHMARKS (sourced) AND KIT ESTIMATES'),
    ('FASE 2: LOCAL, SALIDA DE HUMOS, GAS, LICENCIA Y TERRAZA (semanas 3-14)',
     'PHASE 2: SITE, HOOD, GAS, PERMITS & PATIO (weeks 3-14)'),
    # Inversión, filas 7-24: las 19 partidas de US §8 en las 18 filas con la CLASE de la fila ES (F1-camino §6):
    # 7-11 obra (base de imprevistos), 12-21 equipo, 22-24 sin amortizar, y cada partida en la fila ES más parecida.
    # «Signage & facade» entra en la obra; «electrical, HVAC, plumbing, gas & grease» se parte en 10 y 11; freidora,
    # fogón y steam table van juntos (= la fila 14 ES); las prensas, con el utillaje; el beer cooler sale de la línea de
    # la salsa bar a la fila 19 (la barra ES). Solo la fila 15 (campana ES: en EE. UU. va en la 9) cambia de objeto
    ('Proyecto técnico de actividad y de salida de humos, y dirección de obra',
     'Architect, MEP & hood drawings, plan review & permit fees'),
    ('Obra y acondicionamiento del local, rótulo y fachada',
     'Build-out (second-generation space, 1,200 sq ft), signage & facade'),
    ('Conducto de extracción exclusivo hasta cubierta', 'Type I hood, UL 300 fire suppression & makeup air'),
    ('Instalación eléctrica, cuadro y boletín', 'Electrical service, panel & gas lines'),
    ('Fontanería, separador de grasas, climatización e instalación de gas', 'Plumbing, grease interceptor & HVAC'),
    ('Trompo: asador vertical de gas de cuatro quemadores', 'Vertical broilers (trompos) × 2'),
    ('Plancha de acero a gas y comal', 'Flat-top griddle (36 in) & comal'),
    ('Freidora, fogón de carnitas, baño maría y mantenedor de tortillas',
     'Fryer, stock-pot range, steam table & tortilla warmers'),
    ('Campana extractora con motor y filtros', 'Walk-in cooler (6×8)'),
    ('Frío: armarios, congelador y mesa refrigerada de salsas', 'Refrigerated prep table, salsa bar & freezer'),
    ('Lavavajillas de capota, fregaderos, lavamanos, mesas inox y estanterías',
     '3-comp sink, dish machine, hand sinks, shelving & stainless'),
    ('Utillaje y menaje: licuadora, molcajetes, sondas y prensa de tortillas',
     'Smallwares & tortilla presses (hotel pans, blenders, probe thermometers, scales)'),
    ('Barra: botellero frío, tirador de cerveza y cafetera', 'Beverage station (beer cooler, agua fresca dispensers)'),
    ('Mobiliario de sala, barra y terraza', 'Furniture (30 seats) & patio (12)'),
    ('TPV con Veri*factu, datáfonos, impresora de comandas y tablet', 'POS, online ordering, kiosk & delivery tablets'),
    ('Constitución de la SL, licencia, tasas, registro sanitario y APPCC', 'LLC, legal & food safety plan'),
    ('Marca, web, fotos y lanzamiento', 'Branding, website, photos & launch'),
    ('Stock inicial: carnes, chiles, tortillas, bebida y envases', 'Opening inventory'),
    # P&L (A10, A11, A25, fijos A26-A34 salvo marketing, que es GM). Fijos 10 → 9: la fila ES de DDD lleva el pest
    # control de US §8 y las renovaciones de permisos van con residuos (la fila ES de terraza y residuos)
    ('Ventas de taquería y cocina (sala, para llevar y a domicilio)',
     'Food sales (tacos, quesadillas, plates & sides: dine-in, take-out & delivery)'),
    ('Ventas de bebida (aguas frescas, cerveza, mezcal y tequila, refrescos y agua)',
     'Beverage sales (aguas frescas, sodas, Mexican beer & wine)'),
    ('Seguros (RC + multirriesgo)', 'Insurance (general + liquor liability + property + workers\' comp)'),
    ('Gestoría laboral, fiscal y contable', 'Accounting & bookkeeping'),
    ('Mantenimiento de la campana extractora, el gas y el frío',
     'Maintenance (hood cleaning, broilers, refrigeration)'),
    ('Software, TPV, teléfono e internet', 'Software, POS & online ordering'),
    ('Limpieza, lavandería, EPI y análisis de autocontrol', 'Cleaning, linens & uniforms'),
    ('Tasa de terraza y gestión de residuos (pon las de tu ayuntamiento)',
     'Waste, grease & used-oil hauling + permit renewals'),
    ('Desinsectación, desratización y desinfección (DDD)', 'Pest control'),
    ('Derechos de autor por música ambiental (SGAE y AGEDI-AIE)', 'Music licensing (ASCAP/BMI/SESAC)'),
    ('Prevención de riesgos laborales, vigilancia de la salud y formación',
     'Food safety & staff training (CFPM, allergens, OSHA)'),
    # puestos de Staffing (A5:A11): counter service, sin servers (US §8)
    ('Titular — taquero/a jefe: marinado, trompo, compras y gestión', 'Owner / head taquero & GM'),
    ('Taquero/a de trompo, plancha y comal', 'Taquero / line cook (trompo & griddle)'),
    ('Cocinero/a de producción y salsas', 'Prep cook (marinades, carnitas, salsas, aguas frescas)'),
    ('Encargado/a de sala, barra y mostrador', 'Counter lead / cashier'),
    ('Camarero/a de cenas y fines de semana', 'Counter & expo (part-time W-2)'),
    ('Refuerzo de viernes a domingo: barra, terraza y recogidas', 'Dish & prep (part-time W-2)'),
    ('Suplencias de vacaciones y descansos', 'Relief cover (vacations + days off)'),
])

# Mismo ES con otro EN en ESTA celda (lección de BP2 §4.1: los arreglos de un libro no se heredan a ciegas)
POR_CELDA = OrderedDict([
    # E5: la columna H de la línea de bebida = parte gravada al tipo del alcohol de B40 (= Pizza EN)
    (('TAQP', _P, 'H4'), 'Beverage share taxed at the alcohol rate in B40 (%)'),
    (('TAQP', _P, 'F11'), 'Dine-in beverages and the drinks that go out with orders (aguas frescas, sodas, Mexican beer '
                          '& wine) · Column H is the share of beverage sales taxed at the alcohol rate in "0. '
                          'Assumptions" B40. With the example rates (B39 = B40 = 8%: state + local) it changes nothing. '
                          'Some states tax alcohol differently: type your alcohol rate in B40 and the alcohol share of '
                          'beverage sales here'),
    (('TAQP', _S, 'A62'), 'Alcohol share of beverage purchases (reference only: no input credit in the US)'),
    (('TAQP', _S, 'C62'), 'Reference only: in the US the sales tax you pay on purchases is a cost, not a credit (B41 = 0%), '
                          'so this share moves no figure in the workbook. The sales tax you COLLECT on beverages is set '
                          'by the beverage line of the P&L (column H)'),
    (('TAQP', _S, 'C63'), 'NO EFFECT in this workbook: the sales tax collected on beverages is set by the beverage line of '
                          'the P&L. With the example, beer, wine, aguas frescas and food all pay the same 8% (state + '
                          'local); if your state taxes alcohol at another rate, type it in B40 and the alcohol share in '
                          'column H of that line'),
    # Mes 1 = ENERO con los pesos de US §8 (VALORES_EN B5:M5), no los del ES
    (('TAQP', _T, 'O5'), 'Month 1 = JANUARY, in calendar order: January and February are the slowest months, May is the '
                         'peak (Cinco de Mayo, celebrated mostly in the US, plus the start of patio season) and the summer '
                         'stays strong with the patio. Kit weights for a mid-size US city: replace them with your area\'s '
                         'pattern; if you open in another month, rotate the row. It must add up to 100%'),
    # D19: el rótulo ES de A39 es el de la partida 12 (FIJO): aquí, el nombre de la fila de referencia
    (('TAQP', _N, 'A39'), 'Vertical broiler (trompo)'),
    # E4: la nota de Staffing sin servers y con las propinas del mostrador (US §6.6)
    (('TAQP', _R, 'A29'), 'The gross pay, employer payroll taxes, monthly cost and annual cost columns are TOTALS for the '
                          'row: for a position with two people they include both. "FTE" is the share of a full-time week '
                          'and is used to compare pay with the legal floor pro rata. The payroll tax rate and the number '
                          'of pay periods are in the "0. Assumptions" tab. Tips are not modeled: this is counter service, '
                          'every position is budgeted at a base wage of at least $15/h, and counter tips (tip jar or '
                          'screen) belong to the staff, never to the owner or managers. Federal rules allow a $2.13/h cash '
                          'wage with a tip credit of up to $5.12 where the state permits it; CA, OR, WA, AK, MN, MT and NV '
                          'do not (DOL)'),
])

# ==========================================================================
# Cifras prohibidas (F1-camino §7): ES de la taquería (importe y frase), casos EN publicados y RX_TAQ_NO.
# Formato: (regex, motivo, excepción sobre el texto entero)
# ==========================================================================
def _num(n):
    """168700 → patrón que casa 168,700 · 168.700 · 168 700 · 168700 (y nada pegado a más dígitos)."""
    s = str(n)
    cab, cola = s[:-3], s[-3:]
    return r'(?<![\d.,])' + cab + r'[.,   ]?' + cola + r'(?![\d])'


def _cifras_es():
    """Importes ≥ 10.000 € del caso ES de la taquería (`../plan-taqueria/cifras_caso_es.json`, tokens con «€»: el ES
    está cerrado y manda). Los pequeños quedan cubiertos por la prohibición de «€»."""
    out = set()
    p = os.path.join(TAQES, 'cifras_caso_es.json')
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
        (r'(?i)\b77 (?:covers|guests|customers|diners)\b', 'caso ES (77 comensales/día)'),
        (r'(?<![\d$])15[.,]50\b', 'ticket ES (15,50 €)'),
        (r'(?i)\b300 (?:opening )?days\b', 'días del ES (300; el caso US abre 308)'),
        (r'(?i)\b14 (?:pay periods|payments|paychecks|salaries|monthly)', 'pagas del ES (14 pagas)'),
        (r'(?i)(?:payroll|social security|employer)[^.;]{0,60}?\b33\s?%', 'Seguridad Social del ES (33 %)'),
        (r'(?i)\b33\s?%[^.;]{0,40}?(?:payroll|social security|employer)', 'Seguridad Social del ES (33 %)'),
        (r'\b17[.,]094\b', 'SMI ES (17.094 €)'),
        (r'\b1[.,]221\b', 'SMI ES (1.221 €)'),
        (r'(?i)net[^.;]{0,40}?\b9[.,][19]\s?%', 'margen neto ES (9,1 % del caso; 9,9 % de la research)'),
        # la cuota de plataforma ES (F1-camino §7; = B4 Pizza EN): el caso US es el 15 % de B16
        (r'(?i)\b12 ?% of sales\b', 'plataforma ES (12 % de ventas: el caso US es el 15 %)'),
        (r'(?i)\bRD 10(?:21|86)\b|\bart\. ?(?:4\.1|30)\b|Ley 1/2025|Ley 7/2022|\bACSA\b|\bAESAN\b',
         'norma ES (RD 1021/2022, RD 1086/2020, Leyes 1/2025 y 7/2022, ACSA, AESAN)'),
        (r'\bv1\.[01]\b|\b[Vv]ersion 1\.[01]\b', 'historia de versiones (la EN nace en 2.2)'),
    ]


FRASES_OTROS = [(r'(?i)\b62 covers\b', 'caso de la Pizza EN («62 covers»)'),
                (r'\$36(?:\.00)?\b', 'caso de la Pizza EN («$36»)'),
                (r'(?i)\b165 customers\b', 'caso de la Ice Cream EN («165 customers»)'),
                (r'(?i)\b210 transactions\b', 'caso de la Bakery EN («210 transactions»)'),
                (r'(?i)\b95 covers\b', 'caso del Bar EN («95 covers»)'),
                (r'\$27(?:\.00)?\b', 'caso del Bar EN («$27»)'),
                (r'(?i)\b360 (?:opening )?days\b', 'caso del Bar EN («360 days»)')]

_NO = r"(?i)\b(?:no|not|never|cannot|can't|don't|do not|without|isn't|is not|rather than|instead of)\b"
RX_TAQ_NO = [
    # restos de la Pizza EN (F1-camino §7)
    (r'(?i)\bpizz', 'Pizza EN («pizza»)', None),
    (r'(?i)Neapolitan', 'Pizza EN («Neapolitan»)', None),
    (r'(?i)\bdough\b', 'Pizza EN («dough»: en la taquería, «masa»)', None),
    (r'(?i)wood-fired|firewood', 'Pizza EN («wood-fired / firewood»)', None),
    (r'\bVPN\b|\bAVPN\b', 'Pizza EN («VPN»)', None),
    (r'(?i)Margherita|mozzarella|San Marzano', 'Pizza EN (ingredientes)', None),
    # restos del Bar EN
    (r'(?i)\btapas\b|\bsmall plates\b', 'Bar EN («tapas / small plates»)', None),
    (r'(?i)\bcocktails?\b', 'Bar EN («cocktails»: la taquería es beer & wine)', None),
    (r'(?i)\bhappy hour\b|\blast call\b|\bbarbacks?\b|\bneighborhood bar\b', 'Bar EN', None),
    (r'(?i)\bspirits\b', 'Bar EN («spirits»: la taquería es beer & wine)', r'(?i)liquor license|full liquor|' + _NO[4:]),
    (r'(?i)\bmezcal|\btequila', 'ES («mezcal / tequila»: el caso US es beer & wine)', r'(?i)liquor license|full liquor'),
    # restos del ES (F1-camino §7)
    (r'\bIVA\b', 'ES («IVA»)', None),
    (r'(?i)\bconvenio\b', 'ES («convenio»)', None),
    (r'\bSMI\b', 'ES («SMI»)', None),
    (r'(?i)\baut[oó]nomo', 'ES («autónomo»)', None),
    (r'Veri\*?factu', 'ES («Veri*factu»)', None),
    (r'\bSGAE\b', 'ES («SGAE»)', None),
    (r'\bIAE\b', 'ES («IAE»)', None),
    (r'(?i)\bterrazas?\b', 'ES («terraza» → patio)', None),
    (r'(?i)\bcomensal', 'ES («comensal» → covers)', None),
    (r'\bEspaña\b|\bSpain\b', 'ES («España/Spain»)', None),
    (r'\bVAT\b', 'ES («VAT» fuera de la nota UK)', r'\bUK\b|United Kingdom|HMRC'),
    # claims (US §9 y §6.5)
    (r'(?i)\bauthentic', 'claim («authentic»: US §9, nunca como promesa)', None),
    (r'(?i)\bTex-Mex\b', 'claim («Tex-Mex» no es sinónimo, US §9)', _NO),
    (r'(?i)gluten[- ]free', 'claim («gluten-free»: US §6.5, comal y freidora compartidos)',
     r"(?i)naturally gluten-free|21 CFR|\bnot\b|\bnever\b|cannot|can't|don't|do not|\bno\b"),
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
    """Importes en dólares ≥ 10,000 que cita la research US de la taquería: son datos de este producto y no se vetan
    aunque coincidan con un importe de otro caso EN."""
    out = set()
    p = os.path.join(AQUI, 'F1-research-us-delta.md')
    t = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    for m in re.finditer(r'\$\s?(\d{1,3}(?:,\d{3})+)(?:\s?[-–]\s?\$?(\d{1,3}(?:,\d{3})+))?', t):
        out |= {int(x.replace(',', '')) for x in m.groups() if x and int(x.replace(',', '')) >= 10000}
    out |= {int(x) * 1000 for x in re.findall(r'\$\s?(\d{2,3})K\b', t)}
    return out


def cifras_prohibidas(valores):
    """CIFRAS_PROHIBIDAS del conjunto. Fuera las cifras que coinciden con un valor del propio caso US."""
    propios = {int(round(x[0])) for x in valores.values() if isinstance(x[0], (int, float))}
    out = [(_num(n), 'cifra del caso ES de la taquería', None) for n in sorted(_cifras_es()) if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in _frases_es()]
    propios |= _importes_research()
    for path, plan, nombre in [(os.path.join(PIZ, 'cifras_caso.json'), 'piz', 'de la Pizza EN'),
                               (os.path.join(ICE, 'cifras_caso.json'), 'ice', 'de la Ice Cream EN'),
                               (os.path.join(BP2, 'cifras_caso.json'), 'pan', 'de la Bakery EN'),
                               (os.path.join(BAR, 'cifras_caso.json'), 'bar', 'del Bar EN'),
                               (os.path.join(BP, 'cifras_caso.json'), 'ft', 'del FT EN'),
                               (os.path.join(BP2, 'cifras_caso.json'), 'rest', 'del Restaurant EN')]:
        out += [(_num(n), 'cifra del caso %s (no se reutiliza)' % nombre, None)
                for n in _cifras_caso(path, plan) if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_OTROS]
    out += RX_TAQ_NO
    return out


# ==========================================================================
# Tokens del docx: los de FT/CAF con los rótulos de la taquería («Comensales…», = pizza) + partidas propias
# ==========================================================================
_CLIENTES = OrderedDict([
    ('Clientes/día (media del año 1)', 'Comensales/día (media del año 1)'),
    ('Clientes/día (media)', 'Comensales/día (media)'),
    ('Clientes/día', 'Comensales/día'),
    ('Clientes necesarios al día', 'Comensales necesarios al día'),
    ('Clientes necesarios al día (caja)', 'Comensales necesarios al día (caja)'),
])
_DESC = OrderedDict([
    ('clientes_dia', 'average covers per day, year 1: dine-in + take-out/pickup and delivery equivalents'),
    ('clientes_a2', 'average covers per day, year 2'),
    ('clientes_a3', 'average covers per day, year 3'),
    ('equilibrio_clientes_dia', 'break-even covers per day (accounting)'),
    ('equilibrio_caja_clientes_dia', 'cash break-even covers per day (loan payments in, depreciation out)'),
    ('pesimista_clientes', 'pessimistic scenario: covers per day'),
    ('optimista_clientes', 'optimistic scenario: covers per day'),
    ('alquiler_mes', 'rent per month (base rent of the premises)'),
    ('vida_obra', 'useful life of build-out, years'),
    ('ocupacion_anual', 'rent per year (occupancy)'),
    ('consumibles_pct', 'disposables (clamshells, foil, salsa cups, bags), % of sales'),
])
_FUERA = ('inv_vehiculo', 'inv_adaptacion', 'inv_equipo_cocina', 'inv_generador', 'inv_permisos', 'inv_espresso',
          'inv_obra', 'inv_instalaciones', 'inv_mobiliario', 'inv_barra', 'inv_terraza', 'inv_lanzamiento',
          'inv_stock', 'aforo', 'rotaciones_dia')


def _inv(rot, desc):
    return ('usd', ('fila', _I, {'taq': rot}, 'B'), desc)


def _como_excel(v, decimales):
    """Redondeo que se VE en Excel: 15 cifras significativas y luego mitad hacia arriba (no al par como `format`)."""
    from decimal import Decimal, ROUND_HALF_UP
    return float(Decimal('%.15g' % v).quantize(Decimal(1).scaleb(-decimales), rounding=ROUND_HALF_UP))


TOKENS_PROPIOS = OrderedDict([
    ('inv_proyecto', _inv('Proyecto técnico de actividad y de salida de humos, y dirección de obra',
                          'architect, MEP & hood drawings, plan review and permit fees')),
    ('inv_obra', _inv('Obra y acondicionamiento del local, rótulo y fachada',
                      'build-out of a second-generation space (1,200 sq ft), signage and facade')),
    ('inv_campana', _inv('Conducto de extracción exclusivo hasta cubierta',
                         'Type I hood, UL 300 fire suppression and makeup air')),
    ('inv_instalaciones', _inv('Instalación eléctrica, cuadro y boletín', 'electrical service, panel and gas lines')),
    ('inv_fontaneria', _inv('Fontanería, separador de grasas, climatización e instalación de gas',
                            'plumbing, grease interceptor and HVAC')),
    ('inv_trompo', _inv('Trompo: asador vertical de gas de cuatro quemadores', 'two gas vertical broilers (trompos)')),
    ('inv_plancha', _inv('Plancha de acero a gas y comal', 'flat-top griddle (36 in) and comal')),
    ('inv_freidora', _inv('Freidora, fogón de carnitas, baño maría y mantenedor de tortillas',
                          'fryer, stock-pot range (carnitas, guisados), steam table and tortilla warmers')),
    ('inv_camara', _inv('Campana extractora con motor y filtros', 'walk-in cooler (6×8)')),
    ('inv_frio', _inv('Frío: armarios, congelador y mesa refrigerada de salsas',
                      'refrigerated prep table, salsa bar and freezer')),
    ('inv_lavado', _inv('Lavavajillas de capota, fregaderos, lavamanos, mesas inox y estanterías',
                        '3-compartment sink, dish machine, hand sinks, shelving and stainless')),
    ('inv_utillaje', _inv('Utillaje y menaje: licuadora, molcajetes, sondas y prensa de tortillas',
                          'smallwares and tortilla presses')),
    ('inv_bebida', _inv('Barra: botellero frío, tirador de cerveza y cafetera',
                        'beverage station (beer cooler, agua fresca dispensers)')),
    ('inv_mobiliario', _inv('Mobiliario de sala, barra y terraza', 'furniture (30 seats) and patio (12)')),
    ('inv_tpv', _inv('TPV con Veri*factu, datáfonos, impresora de comandas y tablet',
                     'POS, online ordering, kiosk and delivery tablets')),
    ('inv_constitucion', _inv('Constitución de la SL, licencia, tasas, registro sanitario y APPCC',
                              'LLC, legal and food safety plan')),
    ('inv_lanzamiento', _inv('Marca, web, fotos y lanzamiento', 'branding, website, photos and launch')),
    ('inv_stock', _inv('Stock inicial: carnes, chiles, tortillas, bebida y envases', 'opening inventory')),
    ('aforo', ('int', ('fila', _S, {'taq': 'Aforo del local (plazas sentadas, sin la terraza)'}, 'B'),
               'indoor seats (patio not included)')),
    ('rotaciones_dia', ('dec1', ('fila', _S, {'taq': 'Rotaciones al día implícitas (calculado)'}, 'B'),
                        'implied seat turns per day (take-out and delivery included)')),
    ('comida_pct', ('pct0', ('fila', _S, {'taq': 'Ventas de COMIDA sobre el total'}, 'B'), 'food share of sales')),
    ('bebida_pct', ('pct0', ('fila', _S, {'taq': 'Ventas de BEBIDA sobre el total'}, 'B'), 'beverage share of sales')),
    ('plataforma_pct', ('pct0', ('fila', _S, {'taq': 'Ventas por delivery sobre el total'}, 'B'),
                        'share of sales through third-party delivery marketplaces')),
    ('comision_pct', ('pct0', ('fila', _S, {'taq': 'Comisión de la plataforma de delivery'}, 'B'),
                      'marketplace commission on those orders')),
    ('marketing_anual', ('usd', ('fila', _P, {'taq': 'Marketing y publicidad'}, 'B'), 'marketing budget per year')),
    ('prime_cost_pct', ('pct1', ('deriv', lambda c: c['cogs_pct'] + c['personal_pct']),
                        'prime cost year 1 (cost of goods + labor, % of sales)')),
    ('meses_alquiler_previo', ('int', ('fila', _S, {'taq': 'Meses de alquiler ANTES de abrir (obra y licencias)'}, 'B'),
                               'months of rent paid before opening (build-out and permits)')),
    ('costes_variables_pct', ('pct1', ('deriv', lambda c: 1 - c['margen_bruto_pct']),
                              'all variable costs year 1 (cost of goods + disposables + marketplace + card fees + '
                              'contingency), % of sales')),
    ('otros_variables_pct', ('pct1', ('deriv', lambda c: 1 - c['margen_bruto_pct'] - c['cogs_pct']),
                             'disposables + marketplace + card fees + contingency, % of sales')),
    ('pesimista_perdida', ('usd', ('deriv', lambda c: -c['pesimista_resultado']),
                           'pessimistic scenario: pre-tax LOSS as a positive amount (only if it is a loss)')),
    # Revisión F2 (29-oct): `formatear` redondea al par (0.2625 → «26.2%», 5.025 → «5.02») y Excel/LibreOffice muestran
    # 26.3% y 5.03 en PyG!B52 y Personal!C12: el Word cita lo que se VE en el libro (redondeo de Excel a 15 cifras)
    ('cogs_pct_xl', ('pct1', ('deriv', lambda c: _como_excel(c['cogs_pct'], 3)),
                     'cost of goods, % of sales, rounded as Excel shows it (P&L B52)')),
    ('plantilla_jornadas_xl', ('dec2', ('deriv', lambda c: _como_excel(c['plantilla_jornadas'], 2)),
                               'staff in FTE, rounded as Excel shows it (Staffing C12)')),
])


def tokens_taq(base):
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
            src = ('fila', hoja, {'taq': rot}, col)
        if t == 'consumibles_pct':
            fmt = 'pct1'
        out[t] = (fmt, src, _DESC.get(t, desc))
    out.update(TOKENS_PROPIOS)
    return out


# ==========================================================================
# Docx: lo que escribe ensamblar_docx.py (índices del FT ES de 131 párrafos = PIZ) y las notas por ranura
# ==========================================================================
PRODUCTOS_CIERRE_TAQ = ['Food Cost Kit Pro', 'HACCP Food Safety Kit Pro', 'Restaurant Checklists Kit Pro',
                        'Food Truck Business Plan Kit']


def docx_fijos(M):
    pc = PRODUCTOS_CIERRE_TAQ
    d = OrderedDict([
        (6, 'BUSINESS PLAN'), (7, 'Taco Shop'),
        (9, 'Complete financial plan, market analysis,\noperations strategy and startup checklist\nto open a '
            'counter-service taco shop in the United States'),
        (14, 'AI Chef Pro'), (15, 'aichef.pro'), (16, 'US edition with UK notes · 2026'),
        (18, 'LEGAL NOTICE'), (19, M.AVISO_DOCX_EN), (20, '© 2026 AI Chef Pro — aichef.pro'), (22, 'CONTENTS'),
        (35, 'Appendices: Taco Shop Financial Projections (Excel) + Taco Cost & Trompo Yield Calculator (Excel) + Taco '
             'Shop Startup Checklist (Excel) + Equivalents Guide'),
        (123, 'AI Chef Pro'), (124, 'Templates and AI tools for food businesses'),
        (126, 'aichef.pro\ninfo@aichef.pro'),
        (127, '→ %s · %s' % tuple(pc[:2])), (128, '→ ' + pc[2]), (129, '→ ' + pc[3] + ' (for a taco truck)'),
        (130, '\n' + M.URL_TIENDA),
    ])
    return OrderedDict([('taq', d)])


DOCX_NOTAS_PLAN = OrderedDict([
    ('taq', 'Concepto (US §1): COUNTER-SERVICE TACO SHOP de barrio en una ciudad media de EE. UU. (150-300 mil hab.), '
            '~1,200 sq ft, {{aforo}} plazas + patio de 12 (abril-octubre), pedido en mostrador (sin servicio de mesa), '
            'take-out/pickup propio y marketplaces; trompo de gas para el al pastor (vertical broiler), flat-top griddle '
            'y comal, freidora para chips, fogón para carnitas y guisados, steam table y salsa bar refrigerada; carta de '
            '8-10 street tacos en doble tortilla de maíz de 6 in, quesadillas y gringas, plates (3 tacos + rice & '
            'beans), chips & guac, aguas frescas, refrescos y beer & wine (Mexican beer; sin full liquor: nada de '
            'mezcal ni tequila en el caso); cierra los lunes; el dueño es el head taquero y el GM. «Taco shop» en el '
            'nombre, «taqueria» (sin tilde) en prosa; nunca «Tex-Mex» como sinónimo ni «authentic» como promesa; volumen '
            '= «covers». Cada cifra del caso va con su token {{…}}; las de mercado solo si están en research con fuente. '
            'Lo ES que NO cruza (IVA partido 10/21 %, RD 1021/2022 art. 4.1, RD 1086/2020 art. 30, ordenanza de humos, '
            'ACSA/AESAN, convenio, SMI, 14 pagas, Leyes 1/2025 y 7/2022, Veri*factu, IAE) se SUSTITUYE por US §6. La '
            'temperatura del pastor la pone el condado (145 °F o 155 °F; 165 °F el pollo): NUNCA una cifra única como '
            'regla. Tortilla: comprada al abrir; la propia (masa harina + prensa) se paga a ≈ 660 al día y el caso gasta '
            '≈ 650. Honestidad del margen: neto {{margen_neto_a1}}. Fuera: taco truck (→ Food Truck Business Plan Kit), '
            'franquicia, restaurante mexicano de mesa con bar completo, venta desde casa. Glosario US §9 obligatorio. El '
            'cierre (productos) lo escribe el ensamblador. ' + REGLA_UNIDADES),
])

_FORMA = ('FORMA: la sección §%d de la Pizza EN (business-plans-en-8/docx_en_piz_%s.json) da el registro y la longitud; '
          'su vocabulario de pizza (oven, dough, Neapolitan, servers…) y sus cifras NO valen')
_SEC = OrderedDict([
    (1, ('a', 'Resumen ejecutivo: concepto (US §1), la oportunidad (US §2-§3: «trompo» 27,100/mes y «street tacos» '
              '74,000 de demanda de consumo; las colas de «taco shop business plan» son pequeñas: no las cites como '
              'mercado), inversión y financiación SOLO con tokens ({{inversion_total}}, {{capex}}, {{prestamo}} SBA 7(a) '
              '{{tipo_prestamo}} a {{plazo_prestamo}} años), ventas ({{ventas_a1}}, {{clientes_dia}} covers × {{ticket}} × '
              '{{dias}} días), neto {{margen_neto_a1}} y DSCR {{dscr_min}}')),
    (2, ('a', 'Concepto y propuesta: counter service, trompo a la vista (al pastor con piña), street tacos en doble '
              'tortilla de maíz de 6 in «with everything» (onion & cilantro), order of 3 / plate, gringa y quesadilla, '
              'birria los fines de semana como opción, salsa bar, aguas frescas (horchata, jamaica), beer & wine; tortilla '
              'comprada al abrir y la propia como palanca cuando pase de ~700 al día; sin «authentic» ni «Tex-Mex»')),
    (3, ('a', 'Mercado y competencia: US §2, §5.1 y §7 (precio del street taco $3.00-3.75 en ciudad media y ≈ $5 en '
              'gran ciudad = Kit estimate; franquicias como Del Taco no son el comprador); el cliente US entre taco truck, '
              'cadena fast casual y taqueria de barrio; sin datos de mercado sin fuente')),
    (4, ('a', 'Cliente y posicionamiento: comida y cena, take-out/pickup fuerte; el check de {{ticket}} (2.6 tacos + '
              'quesadilla o sides + 0.85 bebidas); el pickup directo (0 % de comisión) frente a marketplaces')),
    (5, ('a', 'Marketing y ventas: Google Business Profile, Yelp, Instagram (el trompo vende en vídeo), fechas (Cinco de '
              'Mayo, fiesta sobre todo estadounidense; Taco Tuesday); marketplaces DoorDash/Uber Eats/Grubhub con sus tiers '
              '(US §5.2); el caso pone {{plataforma_pct}} de las ventas al {{comision_pct}}; los tacos viajan mal: '
              'tortillas aparte, radio corto')),
    (6, ('b', 'Operaciones y equipo: trompos ({{inv_trompo}}), griddle y comal ({{inv_plancha}}), freidora y fogón '
              '({{inv_freidora}}), Type I hood + UL 300 + makeup air ({{inv_campana}}), walk-in ({{inv_camara}}), salsa bar '
              '({{inv_frio}}); el cono: marinado, montaje, cocción y corte (rendimiento ≈ 65 %, ≈ 6.9 tacos por lb cruda: '
              'Kit estimate, mídelo con la calculadora); salsa bar con TPHC y procedimiento escrito; tortilla comprada vs '
              'propia (equilibrio ≈ 660 al día); trompo de carbón = variante de combustible sólido (NFPA 96)')),
    (7, ('b', 'Organización y personal: Owner / head taquero & GM, taquero (trompo & griddle), prep cook, counter lead / '
              'cashier, counter & expo part-time W-2, dish & prep, relief cover ({{plantilla_puestos}} personas = '
              '{{plantilla_jornadas}} FTE); ≥ $15/h, propinas del mostrador para el equipo (no para el dueño), sin tip '
              'credit modelado; employer payroll taxes {{cargas_pct}}; el dueño se paga por debajo de un manager: «draw '
              'in addition from net profit»')),
    (8, ('b', 'Plan financiero: TODO con tokens (ventas años 1-3, mezcla {{comida_pct}}/{{bebida_pct}}, COGS {{cogs_pct}}, '
              'personal {{personal_pct}}, prime cost {{prime_cost_pct}}, alquiler {{ocupacion_pct}}, EBITDA, neto, '
              'equilibrio {{equilibrio_clientes_dia}} / {{equilibrio_caja_clientes_dia}} covers/día, holgura '
              '{{holgura_caja_pct}}, DSCR {{dscr_min}}, saldo mínimo {{saldo_minimo}}, escenarios); el food cost del '
              'caso y su sensibilidad (cada punto de food cost mueve el resultado: dilo sin cifra inventada)')),
    (9, ('b', 'Marco legal US (ver las notas propias de cada ranura de §9)')),
    (10, ('b', 'Hoja de ruta: el orden del checklist (80 tareas en 6 fases: setup, hood/gas/permits, kitchen & health, '
               'staff & allergens, menu/brand/delivery, opening & 90 days); la beer & wine license se pide al firmar el '
               'local; las reglas del trompo de tu condado por escrito ANTES de comprar; cierre con el Excel, la '
               'calculadora de coste por taco y rendimiento del trompo y el checklist')),
])
_RANURAS = OrderedDict([(1, range(39, 44)), (2, range(46, 51)), (3, range(53, 59)), (4, range(61, 67)),
                        (5, range(69, 76)), (6, range(78, 83)), (7, range(85, 91)), (8, range(93, 100)),
                        (9, range(102, 109)), (10, range(111, 118))])
_N9 = OrderedDict([
    (102, '§9 1/7: el marco US por niveles (federal, estatal, condado, ciudad); LLC + EIN; sales tax permit; business '
          'license; zoning check ANTES de firmar; plan review (Food Code 8-201.11) + building permit → certificate of '
          'occupancy; fire marshal; sales tax {{sales_tax}} de ejemplo, un solo tipo («some states tax to-go food '
          'differently», sin cifra)'),
    (103, '§9 2/7: campana y fuego: Type I hood + fire suppression (UL 300) sobre griddle, freidora y vertical broilers '
          'de gas; makeup air; grease interceptor; trompo o parrilla de carbón = combustible sólido (NFPA 96: escape '
          'separado, arrestachispas, ceniza diaria) → variante, no el caso; «ask the fire marshal in writing»'),
    (104, '§9 3/7: health permit + inspección previa; Certified Food Protection Manager (2-102.12) + food handler cards '
          'según estado; FDA Food Code 2022 (cada estado adopta su edición): frío ≤ 41 °F, caliente ≥ 135 °F (carnitas, '
          'birria y guisados en el steam table); TPHC (3-501.19: 4 h / 6 h) con procedimiento escrito para la salsa bar; '
          'pico de gallo y salsas con tomate cortado = TCS; guacamole: «treat it as TCS; ask your regulator»'),
    (105, '§9 4/7: al pastor en el trompo: la temperatura de cocción y el tiempo máximo en el broiler los pone el '
          'CONDADO (guías de condado: 145 °F en unas, 155 °F en otras; pollo 165 °F; cortar solo lo que ha llegado a '
          'temperatura; sonda de respuesta rápida); el plan NO da una cifra única: «get your health department\'s '
          'vertical broiler rules in writing (cook temp, max time on the broiler, leftover cone)»; reheating a 165 °F'),
    (106, '§9 5/7: alérgenos: 9 mayores US incluido el sésamo (FASTER Act); salsa macha = peanuts + sesame; moles = tree '
          'nuts, peanuts, sesame; flour tortillas = wheat; queso y crema = milk; cerveza = wheat/barley; etiquetas en la '
          'salsa bar; «gluten-free»: 21 CFR 101.91 (< 20 ppm); comal y freidora compartidos con la de harina impiden '
          'prometerlo: «corn tortillas are naturally gluten-free; ask about our fryer and griddle»'),
    (107, '§9 6/7: beer & wine license (agencia estatal + aprobación local; coste y plazos muy distintos: «apply early», '
          'NO prometer licencia); liquor liability en el seguro ({{seguros_anual}} con general liability, property y '
          'workers\' comp); personal: W-2 por horas (nada de 1099 para taqueros o cajeros), I-9, W-4, salario mínimo '
          'estatal (federal $7.25/h, DOL), propinas del equipo; música ASCAP/BMI/SESAC; packaging ordinances locales'),
    (108, '§9 7/7: venta desde casa: las cottage food laws cubren productos de bajo riesgo según estado; la carne y las '
          'salsas frescas son TCS: este plan es de local con permiso («check your state»); y, como ÚLTIMA frase o frases, '
          'la NOTA UK: registro del food business en el council 28 días antes, FHRS 0-5, VAT 20 % en comida caliente y '
          'en sala (los tacos calientes para llevar también), 14 alérgenos (cacahuete y sésamo en la macha; apio y '
          'mostaza según receta; sulfitos), premises + personal licence para el alcohol'),
])


def _notas_docx():
    out = OrderedDict()
    for s, filas in _RANURAS.items():
        tanda, nota = _SEC[s]
        for k, i in enumerate(filas, 1):
            n = _N9.get(i) or ('§%d %d/%d: %s' % (s, k, len(filas), nota))
            out[i] = n + ' ‖ ' + _FORMA % (s, tanda)
    return out


DOCX_NOTAS = OrderedDict([('taq', _notas_docx())])

# ==========================================================================
# Pistas por celda (extraer_textos.py → textos_es.json → tandas)
# ==========================================================================
_CASO = ('US §8: caso US = 115 covers/día (≈ 60 en sala, 30 plazas + patio de 12 abr-oct, + ≈ 38 take-out/pickup + ≈ 17 '
         'equivalentes de marketplace) × $17.50 (sin sales tax ni propina) × 308 días; counter service; beer & wine; sin '
         'cifras del ES ni historia de versiones')
CELDA_PISTAS = OrderedDict([
    (('TAQP', _S, 'A2'), 'D8: añade una vez que los importes van «in your currency» (sin símbolo)'),
    (('TAQP', _S, 'C4'), _CASO + '; media del año 1 con la rampa de apertura; compáralo con el paso de gente de tu calle y '
                                 'con tus pedidos de prueba'),
    (('TAQP', _S, 'C5'), _CASO + '; check de $17.50 = 2.6 tacos × $4.00 + 0.2 quesadilla/gringa × $11.50 + 0.25 chips & '
                                 'guac/sides × $7.00 + 0.85 bebidas × $3.60 (Kit estimate, US §8); street taco $3.00-3.75 '
                                 'en ciudad media; el precio con impuesto lo calcula la fila "Menu price incl. sales tax"'),
    (('TAQP', _S, 'C6'), _CASO + '; 308 días = cierra los lunes (52) + Thanksgiving, Christmas, New Year\'s Day, July 4 y un '
                                 'día de inventario'),
    (('TAQP', _S, 'C13'), 'US §5.2: food cost 27 % (taco 25 %, quesadilla 25 %, chips & guac 28 %, birria 30 %, + 1.5 puntos '
                          'de merma; Kit estimate); la calculadora del kit da el coste de cada taco y el rendimiento del '
                          'trompo'),
    (('TAQP', _S, 'C14'), 'US §8: beverage cost 22 % (aguas frescas hechas en casa, refrescos, Mexican beer & wine)'),
    (('TAQP', _S, 'C15'), 'US §8: disposables 4 % (clamshells, foil, salsa cups, bags; packaging ordinances locales)'),
    (('TAQP', _S, 'C16'), 'US §8: 15 % de las ventas por marketplaces (DoorDash, Uber Eats, Grubhub); el pickup directo por '
                          'teléfono o web no paga comisión'),
    (('TAQP', _S, 'C17'), 'US §5.2: 25 % = plan Plus de DoorDash / Uber Eats (Basic 15 %, Premier 30 %; + 6-10 % en pickup '
                          'por la app); compruébalo en tu contrato'),
    (('TAQP', _S, 'C24'), 'US §8: $2,800/mes = 1,200 sq ft × ~$28/sq ft/año (Kit estimate, editable)'),
    (('TAQP', _S, 'C26'), 'US §8: $1,300/mes (gas de los broilers y la plancha, frío y campana)'),
    (('TAQP', _S, 'C27'), 'US §8: $6,000/año = general liability + liquor liability (beer & wine) + property + workers\' '
                          'comp (Kit estimate)'),
    (('TAQP', _S, 'C31'), 'US §8: SBA 7(a) al 10 % a 10 años, sin interest-only; el préstamo lo calcula "Financing"'),
    (('TAQP', _S, 'C51'), 'US §1: 30 plazas en sala; el patio de 12 (abril-octubre) no cuenta en el aforo'),
    (('TAQP', _N, 'A8'), 'SPEC §4.1 línea 4 (Bar): sin divisores 1,10/1,21 → «divide a menu price by 1 + your sales tax '
                         'rate»; P&L excl. sales tax, cash flow incl.; un solo tipo en el ejemplo (B39 = B40 = 8 %)'),
    (('TAQP', _N, 'A10'), 'F1-camino §6: Mes 1 = ENERO, en el orden del calendario (enero-febrero flojos; mayo, el pico, '
                          'con Cinco de Mayo y el patio)'),
    (('TAQP', _N, 'A12'), 'El Word cita las cifras de este Excel (si cambias el libro, manda el Excel); la calculadora de '
                          'coste por taco y rendimiento del trompo va aparte y su food cost por taco NO se copia en '
                          '"0. Assumptions" (allí va el food cost medio de toda la carta)'),
    (('TAQP', _E, 'E25'), 'US: el techo (B25 = 5) incluye a quien se lleva los tacos o los recibe a domicilio, que no '
                          'ocupa plaza (casi la mitad de los covers del caso): ≈ 3 rotaciones de sala en counter service '
                          '(comida y cena, estancias de 20-30 min) + ≈ 2 de take-out/delivery por plaza. Es el techo '
                          'físico del local, no un objetivo'),
    (('TAQP', _P, 'F10'), 'US §8: tacos, quesadillas, plates y sides: ≈ 52 % en sala, ≈ 33 % pickup propio y 15 % por '
                          'marketplaces; un solo sales tax en el ejemplo'),
])
for _f, _nota in [(7, 'US §4: plan review y permit fees; la beer & wine license cambia mucho de un estado a otro '
                      '(pregunta a tu agencia estatal; sin cifra); sin licencia ni declaración responsable españolas'),
                  (8, 'US §8: local de segunda generación (ya fue restaurante) de 1,200 sq ft; incluye signage & facade '
                      '($4,000 de las 19 partidas de US §8)'),
                  (9, 'US §4: Type I hood de 10-12 ft + supresión UL 300 + makeup air (rango $5,000-$25,000; el caso, '
                      '$22,000) sobre griddle, freidora y vertical broilers de gas; NADA de la ordenanza de Madrid'),
                  (10, 'US §8: parte de «electrical, HVAC, plumbing, gas lines & grease interceptor» ($20,000 en total); '
                       'pregunta el servicio eléctrico disponible ANTES de firmar'),
                  (11, 'US §4: grease interceptor $3,500-$7,500 (REST §3) + HVAC; la otra parte de los $20,000 de US §8'),
                  (12, 'US §4: dos trompos de gas (pastor + segundo cono o reserva): Avantco VB203 $999, Visvardis DG8A '
                       '$2,844 (webstaurantstore); conos de unas 30 lb; carbón = variante de combustible sólido'),
                  (13, 'US §4: flat-top griddle 36 in mid-range (Vulcan VCRG36-M1 $2,501; Star 636MF $2,129) + comal'),
                  (14, 'US §4: freidora para los chips, fogón para carnitas y guisados, steam table de 4 pozos (ServIt '
                       'EST-4WS ≈ $1,119, resumen) y tortilla warmers'),
                  (15, 'OJO: la nota ES habla de la campana, que en el caso US va en la fila 9: aquí escribe la del '
                       'walk-in cooler 6×8 (Norlake Kold Locker $12,808, webstaurantstore): la carne marinada en volumen'),
                  (16, 'US §4: prep table refrigerada + salsa bar + congelador (salsa bar sin precio leído: Kit estimate)'),
                  (18, 'US §4: hotel pans, licuadoras, sondas, básculas + prensas manuales de tortilla (Choice 7½ in '
                       '$17.49); sin molcajetes como partida'),
                  (19, 'OJO: la nota ES habla de tirador de cerveza y cafetera: aquí, beer cooler y dispensadores de '
                       'aguas frescas (Kit estimate); sin cafetera'),
                  (20, 'US §1: 30 plazas en sala y el patio de 12 de temporada (sin plazas de barra)'),
                  (24, 'US §8: carnes, chiles, tortillas, bebida (beer & wine: sin mezcal) y envases para llevar')]:
    CELDA_PISTAS[('TAQP', _I, 'D%d' % _f)] = _nota
for _f in range(7, 25):
    CELDA_PISTAS.setdefault(('TAQP', _I, 'D%d' % _f), 'Nota de la partida del ejemplo US (rótulo fijado de la col. A en '
                                                       '"fijos_en"); sin marcas ni normas españolas: solo rangos con '
                                                       'fuente de US §4 o ninguno')
# Tabla D19 (Instrucciones 35-46, 12 filas como el ES): «US TAQUERIA BENCHMARKS (sourced) AND KIT ESTIMATES»
# (Benchmark | Value | Source | Note). Cada fila sustituye a la ES de la misma fila; solo lo «leída» con fuente; lo
# «(resumen)» = Kit estimate. A39 (el rótulo ES = el de la partida 12) va por POR_CELDA
_D19 = OrderedDict([
    (35, 'fila → «Month 1 of the plan» · «January» · «Plan decision» · nota: orden del calendario; enero-febrero flojos, '
         'mayo el pico (Cinco de Mayo y el patio); si abres en otro mes, gira la fila de "12-Month Cash Flow"'),
    (36, 'fila → «Street taco on the menu» · «$3.00-3.75 in mid-size cities; about $5 in big cities» · «Kit estimate '
         '(menu scan, Oct 2026)» · nota: este plan lo pone a $4.00 (plate de 3 tacos + rice & beans ≈ $14)'),
    (37, 'fila → «Al pastor taco food cost» · el % que da la calculadora del kit para el taco al pastor (si no, «about '
         '25% of its price excl. sales tax») · «Kit estimate (Taco Cost & Trompo Yield Calculator)» · nota: 2 tortillas '
         'de 6 in + 1.5 oz servidas + guarnición + salsa + 5 % de merma; carne y tortilla con precios estimados por el '
         'kit: pon los de tu distribuidor'),
    (38, 'fila → «Trompo yield» · «about 7 tacos per raw lb (30 lb cone ≈ 208 tacos)» · «Kit estimate (65% yield, '
         '1.5 oz served)» · nota: mide el tuyo con la calculadora del kit (cono crudo, sobrante, servido)'),
    (39, 'fila → (A39 fijado: «Vertical broiler (trompo)») · «$999-$2,844 each» · «webstaurantstore.com (Avantco VB203, '
         'Visvardis DG8A), read Oct 2026» · nota: el caso cuenta dos trompos de gas; de carbón = variante de combustible '
         'sólido (NFPA 96)'),
    (40, 'fila → «Delivery marketplace commission» · «DoorDash 15 / 25 / 30% + 6% pickup; Uber Eats 15-30%» · '
         '«merchants.ubereats.com; DoorDash tiers (Oct 2026)» · nota: este plan, 25 % sobre el 15 % de las ventas; el '
         'pickup directo no paga comisión'),
    (41, 'fila (sustituye el IVA de los tacos) → «Sales tax» · «8% (example: state + local)» · «Kit example: look up your '
         'state and city rate» · nota: un solo tipo en el libro; algunos estados gravan distinto la comida para llevar'),
    (42, 'fila (sustituye el RD español) → «Hot and cold holding» · «≥ 135 °F hot, ≤ 41 °F cold; reheat to 165 °F within '
         '2 h; TPHC up to 4 h with a written procedure» · «FDA Food Code 2022 (3-501.16, 3-403.11, 3-501.19)» · nota: '
         'cada estado adopta su edición; la salsa bar con TPHC necesita el procedimiento escrito'),
    (43, 'fila (sustituye el SMI) → «Minimum wage» · «federal $7.25/h + your state» · «U.S. Department of Labor '
         '(dol.gov)» · nota: este plan presupuesta ≥ $15/h; teclea el suelo de tu estado en "0. Assumptions"'),
    (44, 'fila → «Labor cost / sales» · «25-35%» · «UpMenu (upmenu.com)» · nota: counter service lo deja en la parte '
         'baja; dos taqueros (el dueño y un segundo) son seguridad, no un lujo'),
    (45, 'fila → «Rent / sales» · «≤ 10%» · «Kit estimate» · nota: el umbral del semáforo del P&L; un local con Type I '
         'hood ya instalado ahorra obra'),
    (46, 'fila (sustituye el convenio) → «Al pastor cook temperature» · «set by your county: 145 °F in some, 155 °F in '
         'others (165 °F for chicken)» · «County vertical broiler guidance (summaries)» · nota: pídela por escrito a tu '
         'health department con el tiempo máximo en el broiler y qué hacer con el cono sobrante; nunca una cifra única'),
])
for _f, _p in _D19.items():
    for _col in 'ABCD':
        CELDA_PISTAS[('TAQP', _N, '%s%d' % (_col, _f))] = _p

# Pistas por TEXTO propias de la taquería (se suman a las de extraer_textos.PISTAS): US §6 y §9
PISTAS_EXTRA = [
    (r'[Cc]omensal|[Cc]ubiertos?|rotaci', 'US §9: el libro dice «covers» y «seat turns»; nunca «customers» para el '
                                          'volumen diario'),
    (r'[Tt]rompo|[Pp]astor|asador vertical|cono', 'US §6.2/§9: «trompo» en carta y prosa, «vertical broiler» en equipo; '
                                                  'la temperatura de cocción la pone el CONDADO (145 o 155 °F; pollo 165 '
                                                  '°F): nunca una cifra única; «get your county\'s vertical broiler rules '
                                                  'in writing»'),
    (r'[Cc]arb[oó]n', 'US §6.3: trompo o parrilla de carbón = combustible sólido (NFPA 96: escape separado, '
                      'arrestachispas, ceniza diaria): variante, no el caso'),
    (r'\bSL\b|aut[oó]nomo|IAE|Seguridad Social|alta en', '«LLC vs S corp with your CPA» · «EIN + state payroll / '
                                                         'unemployment registration»'),
    (r'Veri\*?factu|TPV', '«POS that reports sales tax» (sin Veri*factu)'),
    (r'[Uu]rbanism|[Ll]icencia de (?:actividad|apertura|obra)|compatibilidad|declaraci[oó]n responsable',
     '«zoning check before signing» · «building permit + certificate of occupancy» · business license + sales tax permit'),
    (r'[Tt]erraza', 'patio (permiso de patio/sidewalk café de la ciudad)'),
    (r'alcohol|cerveza|mezcal|tequila|vino', 'US §6.7: «beer & wine license» (estado + local; «apply early», sin '
                                             'prometerla) · liquor liability · el caso US NO vende mezcal ni tequila'),
    (r'[Hh]umos|[Cc]ampana|extracci|[Cc]onducto', 'US §6.3: Type I hood + fire suppression (UL 300) + makeup air sobre '
                                                  'griddle, freidora y vertical broilers; «ask the fire marshal in '
                                                  'writing»'),
    (r'[Rr]egistro sanitario|RGSEAA|APPCC|autocontrol', 'US §6.4: plan review (Food Code 8-201.11) + health permit + '
                                                        'inspection; written food safety plan'),
    (r'\bgas\b|[Gg]as natural|butano|propano', 'licensed gas contractor; gas lines in the build-out'),
    (r'[Ee]xtintor', 'Class K + 2-A extinguishers'),
    (r'[Gg]rasas|aceite usado', 'grease interceptor · used cooking oil pickup'),
    (r'°C', 'US §6.1: frío ≤ 41 °F, caliente ≥ 135 °F, recalentado 165 °F en 2 h; TPHC 4 h / 6 h con '
                             'procedimiento escrito (la métrica solo entre paréntesis)'),
    (r'[Ss]alsas?|barra de salsas|guacamole|pico', 'US §6.1: salsa bar; tomate cortado = TCS (pico de gallo, salsas '
                                                   'frescas); guacamole «treat it as TCS; ask your regulator»; TPHC con '
                                                   'SOP escrito'),
    (r'irrellenable|Ley 1/2025|Ley 7/2022|desperdicio', 'sin equivalente US: packaging ordinances locales; TPHC y cold '
                                                        'holding ≤ 41 °F'),
    (r'[Rr]eclamaciones|[Cc]arteles?', 'required public notices (health permit, beer & wine license, labor law posters)'),
    (r'[Cc]onvenio|[Cc]ontrato|n[oó]mina|registro de jornada', 'offer letters, I-9, W-4, state minimum wage, W-2 por '
                                                               'horas (sin convenio; sin «digital obligatorio»)'),
    (r'PRL|[Pp]revenci[oó]n de riesgos|EPI', 'OSHA basics'),
    (r'[Mm]anipulador|[Ff]ormaci[oó]n', 'Certified Food Protection Manager (2-102.12) + food handler cards (según estado)'),
    (r'[Aa]l[eé]rgen|macha|cacahuete|s[eé]samo', 'US §6.5: 9 major allergens incl. sesame (UK 14); salsa macha = peanuts '
                                                 '+ sesame; flour tortillas = wheat'),
    (r'[Gg]luten|cel[ií]ac', 'US §6.5: NO prometer «gluten-free» (21 CFR 101.91; comal y freidora compartidos): «corn '
                             'tortillas are naturally gluten-free; ask about our fryer and griddle»'),
    (r'[Rr]ider|[Rr]epart', 'own drivers = W-2 + hired & non-owned auto insurance (check your state)'),
    (r'[Pp]lataforma|Glovo|Just Eat|Uber|delivery', 'DoorDash / Uber Eats / Grubhub con sus tiers (US §5.2)'),
    (r'[Ee]nvase|tarrina', 'clamshells, foil, salsa cups; local packaging ordinances'),
    (r'SGAE|AGEDI', '«Music licensing (ASCAP/BMI/SESAC)»'),
    (r'[Bb]arra\b', 'Glosario: barra de salsas → «salsa bar»; mostrador → «counter»'),
    (r'[Tt]ortill|nixtamal|[Mm]asa|harina', 'US §8/§9: tortillas de maíz de 6 in compradas (360 por caja); la propia con '
                                            'masa harina se paga a ≈ 660 al día; nixtamal = variante; «masa», nunca '
                                            '«dough»'),
    (r'[Aa]guas? frescas?|horchata|jamaica', 'US §9: aguas frescas · horchata · jamaica (hibiscus)'),
    (r'[Gg]ringa|[Cc]ampechano|[Ss]uadero|[Cc]arnitas|[Bb]irria|[Cc]ochinita|orden de', 'US §9: gringa · campechano · '
                                                                                        'suadero · carnitas · birria · '
                                                                                        'cochinita pibil · order of 3 / '
                                                                                        'plate'),
]

# Glosario de la taquería (US §9, OBLIGATORIO; manda sobre el de FT/CAF)
GLOSARIO_TAQ = OrderedDict([
    ('taquería', 'taco shop (nombre, H1, ficheros) · taqueria (sin tilde; prosa y subtítulo)'),
    ('trompo / asador vertical', 'trompo (carta y prosa) · vertical broiler (equipo) · vertical spit; «cone» o «stack» '
                                 'para la carne'),
    ('taco al pastor', 'al pastor (tacos al pastor; «pastor» solo en jerga de cocina)'),
    ('taquero/a', 'taquero (head taquero); en la plantilla «line cook (trompo & griddle)»'),
    ('taco de calle, doble tortilla', 'street tacos (small corn tortillas, onion & cilantro)'),
    ('con todo', 'with everything / onion and cilantro'),
    ('orden de 3', 'order of 3 tacos · plate / combo plate (with rice & beans)'),
    ('gringa · quesadilla', 'gringa (flour tortilla, al pastor & cheese) · quesadilla'),
    ('carnitas · suadero · campechano · cochinita · barbacoa · birria', 'carnitas · suadero · campechano · cochinita '
                                                                       'pibil · barbacoa · birria, quesabirria, consomé'),
    ('barra de salsas', 'salsa bar'),
    ('agua fresca · horchata · jamaica', 'aguas frescas · horchata · jamaica (hibiscus) · tamarindo'),
    ('salsa macha', 'salsa macha (chile oil with peanuts/sesame) — siempre con el alérgeno'),
    ('nixtamal · masa · harina de maíz nixtamalizado', 'nixtamal / nixtamalization · masa · masa harina'),
    ('comal · plancha', 'comal · flat-top griddle («plancha» no)'),
    ('tortilladora · prensa', 'tortilla machine · tortilla press (manual/electric)'),
    ('tortillería', 'tortilleria (sin tilde)'),
    ('totopos', 'tortilla chips · chips & guac · chips & salsa'),
    ('mostrador / sin servicio de mesa', 'counter service · fast casual · QSR'),
    ('cubierto / comensal · ticket medio', 'covers · average check (excl. sales tax and tip)'),
    ('escandallo por taco · rendimiento', 'taco costing / food cost per taco · yield (trompo yield, tacos per pound)'),
    ('plataforma · para llevar', 'third-party delivery marketplace · take-out / to-go / pickup'),
    ('manipulador de alimentos', 'food handler card · Certified Food Protection Manager (CFPM)'),
    ('campana · supresión', 'Type I hood · fire suppression system (UL 300)'),
    ('control por tiempo', 'time as a public health control (TPHC)'),
    ('agotado', '86\'d'),
    ('cerveza mexicana, michelada', 'Mexican beer · michelada (solo con beer & wine license)'),
    ('preparado de carne ≤ 4 °C · 63 °C · 74 °C', 'cold holding ≤ 41 °F · 135 °F · 165 °F'),
    ('ordenanza de humos', 'Type I hood + local fire/mechanical code'), ('registro sanitario', 'health permit + plan review'),
    ('licencia de apertura', 'business license + certificate of occupancy'), ('convenio', 'state/local minimum wage'),
    ('IVA · fianza', 'sales tax · deposit'), ('autónomo / SL', 'LLC'), ('terraza', 'patio'),
])


# ==========================================================================
# Caso de ejemplo US (research US §8; F1-camino §6): celdas VERDES. (corto, hoja ES, celda) → (valor, rótulo)
# ==========================================================================
ESTACIONALIDAD_US = (0.074, 0.076, 0.084, 0.086, 0.092, 0.088, 0.088, 0.086, 0.084, 0.084, 0.078, 0.080)   # ene → dic
assert abs(sum(ESTACIONALIDAD_US) - 1) < 1e-9


def valores_taq(M):
    v = OrderedDict()
    sup = [
        ('B4', 115, 'Comensales/día'), ('B5', 17.5, 'Ticket medio'), ('B6', 308, 'Días de apertura'),
        ('B7', 0.06, 'Crecimiento de volumen del año 2'), ('B8', 0.04, 'Crecimiento de volumen del año 3'),
        ('B11', 0.85, 'Ventas de COMIDA'), ('B13', 0.27, 'Coste de mercancía sobre las ventas de COMIDA'),
        ('B14', 0.22, 'Coste de mercancía sobre las ventas de BEBIDA'), ('B15', 0.04, 'Consumibles'),
        ('B16', 0.15, 'Ventas por delivery'), ('B17', 0.25, 'Comisión de la plataforma'),
        ('B18', 0.03, 'Comisión de los medios de pago'), ('B20', 0.10, 'Seguridad Social'),
        ('B21', 12, 'Número de pagas'), ('B22', 15080, 'SMI anual'), ('B24', 2800, 'Alquiler mensual'),
        ('B25', 2, 'Fianza'), ('B26', 1300, 'Suministros'), ('B27', 6000, 'Seguros'), ('B28', 0.01, 'Varios'),
        ('B30', 100000, 'Recursos propios'), ('B31', M.CALIBRAR, 'Préstamo bancario'), ('B32', 0.10, 'Tipo de interés'),
        ('B33', 10, 'Plazo del préstamo'), ('B34', 0, 'Carencia'), ('B35', 3, 'Fondo de maniobra'),
        ('B37', 0.25, 'Impuesto de Sociedades, nueva'), ('B38', 0.25, 'Impuesto de Sociedades, tipo'),
        ('B39', 0.08, 'IVA repercutido de restauración'), ('B40', 0.08, 'IVA repercutido/soportado'),
        ('B41', 0, 'IVA soportado en compras'), ('B42', 0, 'Bases negativas'),
        ('B44', 10, 'Vida útil de obra'), ('B45', 7, 'Vida útil de maquinaria'),
        ('B51', 30, 'Aforo'), ('B52', 0.75, 'Actividad del mes 1'), ('B53', 4, 'Meses hasta alcanzar'),
        ('B54', 2, 'Meses de alquiler ANTES'), ('B55', 0.10, 'Imprevistos sobre las partidas de OBRA'),
        ('B58', 2, 'Días medios de cobro'), ('B59', 14, 'Días medios de pago'),
        ('B62', 0.30, 'Bebida que compras al 21'), ('B63', 0.08, 'IVA de la bebida ALCOHÓLICA'),
        ('B65', 1.15, 'DSCR mínimo'), ('B66', 1.25, 'DSCR objetivo'), ('B67', 0.15, 'Holgura mínima'),
        ('B68', None, 'Suelo salarial anual'),
    ]
    for c, val, rot in sup:
        v[('TAQP', _S, c)] = (val, rot)
    # Inversión (US §8 en 18 filas, FIJOS): filas 7-24 = $176,800; los imprevistos (B27) van por fórmula (10 % de 7-11)
    for k, val in enumerate([12000, 42000, 22000, 9000, 11000, 4000, 4000, 6500, 12800, 6500, 11000, 6500, 2000,
                             10000, 4500, 2500, 5500, 5000]):
        v[('TAQP', _I, 'B%d' % (7 + k))] = (val, None)
    # P&L: fijos B26-B34 ($25,000), G13 (soportado de la bebida: valor en el ES) → 0, H11 → 30 % (beer & wine sobre la
    # bebida), umbrales del semáforo (el margen «bruto» del libro descuenta TODOS los variables: 60 %, = ES)
    for k, val in enumerate([4200, 3000, 6000, 3600, 2000, 3500, 900, 1000, 800]):
        v[('TAQP', _P, 'B%d' % (26 + k))] = (val, None)
    v[('TAQP', _P, 'G13')] = (0, None)
    v[('TAQP', _P, 'H11')] = (0.30, None)
    for c, val, rot in [('E50', 0.60, 'Margen bruto'), ('E52', 0.30, 'Coste de mercancía /'),
                        ('E53', 0.36, 'Coste de personal'), ('E54', 0.10, 'Alquiler'), ('E55', 0.05, 'Resultado neto')]:
        v[('TAQP', _P, c)] = (val, rot)
    # Staffing (US §8): personas (B), FTE por persona (C), bruto mes TOTAL de la fila (D); ≥ $15/h, 12 pagas, sin
    # propinas; counter & expo = 2 personas en una fila (E4). Cobertura: servicio 10.5 h × 2.5 + producción 2.5 h × 1.5
    for f, (b, c, d) in zip(range(5, 12), [(1, 1.0, 4500), (1, 1.0, 3293), (1, 0.75, 2340), (1, 1.0, 2773),
                                           (2, 0.4, 2080), (1, 0.375, 975), (1, 0.1, 270)]):
        for col, val in zip('BCD', (b, c, d)):
            v[('TAQP', _R, '%s%d' % (col, f))] = (val, None)
    v.update([(('TAQP', _R, 'B14'), (5000, 'Coste anual')), (('TAQP', _R, 'B15'), (5000, 'Coste anual')),
              (('TAQP', _R, 'B21'), (10.5, 'Horas de servicio')), (('TAQP', _R, 'B22'), (2.5, 'Personas necesarias')),
              (('TAQP', _R, 'B23'), (2.5, 'Horas de producción')), (('TAQP', _R, 'B24'), (1.5, 'Personas en el turno'))])
    # Break-Even!B25 (techo de rotaciones): US §8 decía 3, pero el caso ya vende 3.8 covers por plaza (115 / 30: casi la
    # mitad son take-out y delivery, que no ocupan plaza) y el equilibrio de caja pide 3.2 → con 3 el libro diría que el
    # equilibrio no cabe en el local. Counter service: ≈ 3 rotaciones de sala (comida y cena, estancias de 20-30 min) +
    # ≈ 2 de take-out/delivery por plaza = 5 (Kit estimate; F2-NOTAS §3)
    v[('TAQP', _E, 'B25')] = (5, 'Rotaciones al día que da el local')
    # Escenarios (US §8): pesimista 100 · $16.50 · 303 / optimista 130 · $18.50 · 312
    v.update([
        (('TAQP', _ES, 'B5'), (100, 'Comensales/día')), (('TAQP', _ES, 'D5'), (130, 'Comensales/día')),
        (('TAQP', _ES, 'B6'), (16.5, 'Ticket')), (('TAQP', _ES, 'D6'), (18.5, 'Ticket')),
        (('TAQP', _ES, 'B7'), (303, 'Días')), (('TAQP', _ES, 'D7'), (312, 'Días')),
    ])
    # Estacionalidad (US §8, Mes 1 = ENERO sin girar: F1-camino §6) → Month 1-12
    for col, val in zip('BCDEFGHIJKLM', ESTACIONALIDAD_US):
        v[('TAQP', _T, '%s5' % col)] = (val, 'Estacionalidad')
    return v


# Calibración D15 (US §8: palancas en su orden; máx. 3 vueltas). Cada celda, citada en F2-NOTAS.md (G7)
CALIBRACION_D15 = OrderedDict()


def formulas_taq():
    p = os.path.join(AQUI, 'formulas_taq.json')
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
    M.TOKENS_DOCX = tokens_taq(M.TOKENS_DOCX)
    M.PRODUCTOS_CIERRE = PRODUCTOS_CIERRE_TAQ
    M.DOCX_FIJOS = docx_fijos(M)
    M.DOCX_NOTAS = DOCX_NOTAS
    M.DOCX_NOTAS_PLAN = DOCX_NOTAS_PLAN
    M.FORMULAS_EN = formulas_taq()
    M.VALORES_EN = valores_taq(M)
    M.CALIBRACION_D15 = CALIBRACION_D15
    M.CELDA_PISTAS = CELDA_PISTAS
    M.PISTAS_EXTRA = PISTAS_EXTRA
    M.CIFRAS_PROHIBIDAS = cifras_prohibidas(M.VALORES_EN)
    M.RX_TAQ_NO = RX_TAQ_NO
    M.REGLA_UNIDADES = REGLA_UNIDADES
    glo = OrderedDict(M.GLOSARIO)
    for k, val in GLOSARIO_TAQ.items():
        glo[k] = val                          # research §9 manda (regla de jerga §0)
    M.GLOSARIO = glo
