#!/usr/bin/env python3
"""
datos_piz.py — Pizza Shop Business Plan Kit (EN) · los datos ES→EN que dependen del contenido: rótulos fijados
(D139-D140), POR_CELDA (D141, D144), pistas (D137, D142, D146), tokens del docx (D147), fijos y notas del docx, caso US
(D137; research §8), FORMULAS_EN (D143), cifras ES prohibidas y RX_PIZ_NO (D149) y glosario (research §9). Lo llama
`mapas_piz.instalar()` con el módulo `mapas` YA cargado con los datos de FT/CAF (FIJOS comunes del motor 2.2,
TOKENS_DOCX). Clon de `../business-plans-en-3/datos_bar.py` + `cifras_prohibidas()` de `../business-plans-en-7/
datos_pael.py`. Sesión Claude Code, 25-oct-2026 (F2-EN, paso 1a).
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
PIZES = os.path.join(PD, 'plan-pizzeria')                 # ES: SPEC, research y (al cerrar) cifras_caso_es.json

URL_PIZ = 'aichef.pro/en/digital-products/pizza-shop-business-plan'
_I, _S, _P, _R, _N, _E, _ES, _T = ('Inversión Inicial', '0. Supuestos', 'PyG 3 Años', 'Personal', 'Instrucciones',
                                   'Punto Equilibrio', 'Escenarios', 'Tesorería 12 meses')
REGLA_UNIDADES = ('MEDIDAS US (John, 13-oct; SPEC §0): principales lb y oz, °F, gallons / quarts y sq ft; la métrica entre '
                  'paréntesis para UK y Australia: «3.25 oz (92 g)», «900 °F (480 °C)», «2 gallons (7.6 liters)», «1,500 '
                  'sq ft (139 sq m)»; el horno en pulgadas con los cm entre paréntesis: «47-51 in (120-130 cm)»; la MASA en '
                  'gramos y % panadero (así trabaja el oficio US, D145) con la onza entre paréntesis si ayuda; nada de kg, '
                  'km, litros ni °C como unidad principal (gate)')

# ==========================================================================
# FIJOS (por TEXTO ES, en cualquier celda de los 2 libros). Parten de los de FT/CAF (los del motor 2.2)
# ==========================================================================
FIJOS_FUERA = ('Este fichero forma parte del producto «plan-negocio-food-truck» de AI Chef Pro.',
               'Este fichero forma parte del producto «plan-negocio-cafeteria» de AI Chef Pro.')
_TITULO_CHECK = 'PIZZA SHOP STARTUP CHECKLIST'
FIJOS_NUEVOS = OrderedDict([
    # Instrucciones!A3 del checklist con el nombre comercial (defecto I5 del Bar, inv. §4)
    ('Este fichero forma parte del producto «plan-negocio-pizzeria» de AI Chef Pro.',
     'This file is part of the Pizza Shop Business Plan Kit by AI Chef Pro.'),
    # títulos (D146 A1, D139 A1-A3): «Neapolitan-style», nunca «authentic» ni «VPN-certified»
    ('CHECKLIST DE APERTURA — PIZZERÍA NAPOLITANA', _TITULO_CHECK),
    ('INSTRUCCIONES DE USO — Plan financiero Pizzería Napolitana',
     'HOW TO USE THIS WORKBOOK — Pizza Shop Financial Projections'),
    ('PLAN DE NEGOCIO: PIZZERÍA NAPOLITANA', 'PIZZA SHOP BUSINESS PLAN: NEAPOLITAN-STYLE PIZZERIA'),
    ('Inversión inicial estimada — pizzería con horno de leña, 50 plazas y terraza',
     'Estimated Startup Costs — Neapolitan-style pizza shop, wood-fired oven, 50 seats + patio'),
    ('Ajusta las cifras a tu proyecto: son las de un caso tipo en una ciudad media, sin traspaso. Pon tus presupuestos '
     'reales en las celdas de importe.', 'US kit example (2026) — replace with your own quotes.'),
    # D142: cabecera de la tabla D19; D146: la fase 2 del checklist se llama como su pestaña
    ('DATOS DE REFERENCIA DEL SECTOR', 'US PIZZA SHOP BENCHMARKS (sourced) AND KIT ESTIMATES'),
    ('FASE 2: LOCAL, SALIDA DE HUMOS, LICENCIA Y TERRAZA (semanas 3-14)',
     'PHASE 2: SITE, HOOD, FLUE, PERMITS & PATIO (weeks 3-14)'),
    # D139: partidas de la inversión, filas 7-24 (solo rótulo: ninguna fila se mueve)
    ('Proyecto técnico de actividad y de salida de humos, y dirección de obra',
     'Architect, MEP, hood & flue drawings, plan review & permit fees (incl. beer & wine license, non-quota state)'),
    ('Obra y acondicionamiento del local, rótulo y fachada', 'Build-out (second-generation space), signage & facade'),
    ('Chimenea de doble pared hasta cubierta, filtro de partículas y bancada del horno',
     'Flue/chimney, spark arrestor & insulated hearth pad'),
    ('Instalación eléctrica trifásica, cuadro y boletín', 'Electrical service & panel'),
    ('Fontanería, separador de grasas, climatización y extracción',
     'Plumbing, grease interceptor, HVAC & makeup air'),
    ('Horno de leña de cúpula baja de 120-130 cm de diámetro',
     'Neapolitan wood-fired dome oven (47-51 in, UL 2162-listed)'),
    ('Amasadora de espiral profesional', 'Spiral mixer (60 qt)'),
    ('Mesa fría de pizza con encimera de granito y vitrina', 'Pizza prep table (67-71 in)'),
    ('Armarios refrigerados para las cajas de bolas y arcón congelador',
     'Walk-in (6×8), reach-ins, dough-ball cabinets & freezer'),
    ('Campana extractora con motor, freidora y fogón de apoyo', 'Type I hood & support line (fryer, range)'),
    ('Lavavajillas de capota, fregaderos, lavamanos, mesas inox y estanterías',
     '3-comp sink, dish machine, hand sinks & stainless'),
    ('Utillaje y menaje: palas, cajas de bolas, básculas, vajilla y uniformes',
     'Peels, dough boxes, scales & smallwares'),
    ('Barra: cafetera y molino, botellero frío y equipo de cerveza', 'Beer & wine bar (taps, back bar, espresso)'),
    ('Mobiliario de sala y terraza', 'Furniture (50 seats) & patio'),
    ('TPV con Veri*factu, datáfonos, impresora de comandas y tablet', 'POS, online ordering & delivery tablets'),
    ('Constitución de la SL, licencia, tasas, registro sanitario y APPCC', 'LLC, legal & food safety plan'),
    ('Marca, web, fotos, formación de pizzaiolo y lanzamiento', 'Branding, website, training & launch'),
    ('Stock inicial de harina, tomate, quesos, bebida, leña y cajas', 'Opening inventory'),
    # D140: P&L (A2, A10, A11, fijos A26-A34 salvo marketing, que es GM)
    ('Escenario realista — pizzería con horno de leña, 50 plazas y terraza',
     'Base case — Neapolitan-style pizza shop, 50 seats + patio'),
    ('Ventas de pizzería y cocina (sala, para llevar y a domicilio)',
     'Food sales (pizza, starters & desserts: dine-in, take-out & delivery)'),
    ('Ventas de bebida (cerveza, vino, refrescos, agua y café)', 'Beverage sales (beer, wine, soft drinks & coffee)'),
    ('Seguros (RC + multirriesgo)', 'Insurance (general + liquor liability + property)'),
    ('Gestoría laboral, fiscal y contable', 'Accounting & bookkeeping'),
    ('Mantenimiento del horno, la campana extractora y el frío',
     'Maintenance (oven, hood & flue cleaning, refrigeration)'),
    ('Software, TPV, teléfono e internet', 'Software, POS & online ordering'),
    ('Limpieza, lavandería, EPI, DDD y análisis de autocontrol', 'Cleaning, linens, uniforms & pest control'),
    ('Leña para el horno', 'Firewood'),
    ('Tasa de terraza y gestión de residuos (pon las de tu ayuntamiento)', 'Waste, grease & ash hauling'),
    ('Derechos de autor por música ambiental (SGAE y AGEDI-AIE)', 'Music licensing (ASCAP/BMI/SESAC)'),
    ('Prevención de riesgos laborales y vigilancia de la salud', 'Food safety & staff training (CFPM, allergens, OSHA)'),
    # D140: puestos de Staffing (A5:A11)
    ('Titular — pizzaiolo jefe, masa, compras y gestión', 'Owner / head pizzaiolo & GM'),
    ('Pizzaiolo/a de horno y estirado', 'Pizzaiolo (stretching & oven)'),
    ('Ayudante de cocina y masa', 'Prep & dough cook'),
    ('Camarero/a encargado/a de sala y barra', 'FOH lead / bar'),
    ('Camarero/a de cenas y fines de semana', 'Servers (dinner & weekends, part-time W-2)'),
    ('Refuerzo de viernes a domingo: sala, terraza y recogida', 'Weekend runner / counter & pickup'),
    ('Suplencias de vacaciones y descansos', 'Relief cover (vacations + days off)'),
])

# Mismo ES con otro EN en ESTA celda (D141, D144; lección de BP2 §4.1: los arreglos de un libro no se heredan a ciegas)
POR_CELDA = OrderedDict([
    # D141: la columna H de la línea de bebida = parte gravada al tipo del alcohol de B40 (E5)
    (('PIZP', _P, 'H4'), 'Beverage share taxed at the alcohol rate in B40 (%)'),
    (('PIZP', _P, 'F11'), 'Dine-in beverages and the drinks that go out with orders · Column H is the share of beverage '
                          'sales taxed at the alcohol rate in "0. Assumptions" B40. With the example rates (B39 = B40 = '
                          '8%: state + local) it changes nothing. Some states tax alcohol differently (e.g. Texas: bars '
                          'with a mixed beverage permit pay a separate gross receipts tax): type your alcohol rate in B40 '
                          'and the alcohol share of beverage sales here'),
    (('PIZP', _S, 'A62'), 'Alcohol share of beverage purchases (reference only: no input credit in the US)'),
    (('PIZP', _S, 'C62'), 'Reference only: in the US the sales tax you pay on purchases is a cost, not a credit (B41 = 0%), '
                          'so this share moves no figure in the workbook. The sales tax you COLLECT on beverages is set '
                          'by the beverage line of the P&L (column H)'),
    (('PIZP', _S, 'C63'), 'NO EFFECT in this workbook: the sales tax collected on beverages is set by the beverage line of '
                          'the P&L. With the example, beer, wine and food all pay the same 8% (state + local); if your '
                          'state taxes alcohol at another rate, type it in B40 and the alcohol share in column H of that '
                          'line'),
    # D144: Mes 1 = septiembre (pesos del ES sin tocar)
    (('PIZP', _T, 'O5'), 'Month 1 = SEPTEMBER: the plan opens after the summer to reach the holidays with regulars and '
                         'January-February (Months 5 and 6, the slowest) with the reserve intact. December (Month 4) is the '
                         'peak; January (Month 5) the low point, with a short closure. Kit weights for a mid-size US city: '
                         'replace the weights with your area\'s pattern; if you open in another month, rotate the row. It '
                         'must add up to 100%'),
    (('PIZP', _T, 'A34'), 'The quarters in this sheet are plan quarters, not calendar quarters (September-November, '
                          'December-February, March-May and June-August): with Month 1 in September, the workbook remits '
                          'the sales tax of each plan quarter in the month after it. Your state sets the real filing '
                          'calendar (monthly, quarterly or annual): check it. Income tax for year 1 is paid in year 2. The '
                          'loan payment is split into twelve equal parts following the ANNUAL schedule in "Financing", and '
                          'payroll into twelve monthly installments'),
    # E4 + D38: la nota de Staffing del Bar (override c0422 del restaurante) sin barra de cócteles
    (('PIZP', _R, 'A29'), 'The gross pay, employer payroll taxes, monthly cost and annual cost columns are TOTALS for the '
                          'row: for a position with two people they include both. "FTE" is the share of a full-time week '
                          'and is used to compare pay with the legal floor pro rata. The payroll tax rate and the number '
                          'of pay periods are in the "0. Assumptions" tab. Tips are not modeled: servers and the counter / '
                          'pickup runner are budgeted at a base wage of at least $15/h. Federal rules allow a $2.13/h cash '
                          'wage with a tip credit of up to $5.12 where the state permits it; CA, OR, WA, AK, MN, MT and NV '
                          'do not (DOL)'),
])

# ==========================================================================
# Cifras prohibidas (D149): ES de la pizzería (importe y frase), caso del Bar EN, casos EN de FT y REST y RX_PIZ_NO.
# Formato: (regex, motivo, excepción sobre el texto entero)
# ==========================================================================
def _num(n):
    """192400 → patrón que casa 192,400 · 192.400 · 192 400 · 192400 (y nada pegado a más dígitos)."""
    s = str(n)
    cab, cola = s[:-3], s[-3:]
    return r'(?<![\d.,])' + cab + r'[.,   ]?' + cola + r'(?![\d])'


def _importes(obj, out, minimo=10000):
    """Recorre un JSON de cifras y junta los importes (fmt usd/eur, o claves de importe) ≥ minimo."""
    if isinstance(obj, dict):
        v, fmt = obj.get('valor', obj.get('valor_es')), obj.get('fmt')
        if isinstance(v, (int, float)) and fmt in ('usd', 'eur', 'usd2', 'eur2') and abs(v) >= minimo:
            out.add(int(round(abs(v))))
        for x in obj.values():
            if isinstance(x, (dict, list)):
                _importes(x, out, minimo)
    elif isinstance(obj, list):
        for x in obj:
            _importes(x, out, minimo)
    return out


def _cifras_es():
    """Importes ≥ 10.000 del caso ES: `../plan-pizzeria/cifras_caso_es.json` (ES cerrado, manda) o, si aún no existe,
    los valores ES en caché de los tokens del censo de ESTA fuente (censo_es.json: paso 1a sobre el dry-run) + las 18
    partidas de la inversión ES. Al re-extraer en el paso 1c se recalculan solas."""
    out = set()
    p = os.path.join(PIZES, 'cifras_caso_es.json')
    if os.path.exists(p):
        _importes(json.load(open(p, encoding='utf-8')), out)
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        cen = json.load(open(pc, encoding='utf-8'))
        _importes(cen.get('tokens_docx', {}), out)
        for t in cen.get('tokens_docx', {}).get('piz', {}).values():
            v = t.get('valor_es')
            if t.get('fmt') == 'usd' and isinstance(v, (int, float)) and abs(v) >= 10000:
                out.add(int(round(abs(v))))
    return out


def _es_caso():
    """B4 y B5 del ES (para las frases «66 covers» y «19,50»), del censo de esta fuente; por defecto, los del dry-run."""
    b4, b5 = 66, 19.5
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        tk = json.load(open(pc, encoding='utf-8')).get('tokens_docx', {}).get('piz', {})
        b4 = tk.get('clientes_dia', {}).get('valor_es', b4)
        b5 = tk.get('ticket', {}).get('valor_es', b5)
    return b4, b5


def _frases_es():
    b4, b5 = _es_caso()
    ent, dec = int(b5), int(round((b5 - int(b5)) * 100))
    return [
        (r'(?i)€|\bEUR\b', 'moneda ES'),
        (r'(?i)\b%d (?:covers|guests|customers|diners)\b' % int(round(b4)), 'caso ES (%d comensales/día)' % b4),
        (r'(?<![\d$])%d[.,]%02d\b' % (ent, dec), 'ticket ES (%s €)' % b5),
        (r'(?i)\b14 (?:pay periods|payments|paychecks|salaries|monthly)', 'pagas del ES (14 pagas)'),
        (r'(?i)(?:payroll|social security|employer)[^.;]{0,60}?\b33\s?%', 'Seguridad Social del ES (33 %)'),
        (r'(?i)\b33\s?%[^.;]{0,40}?(?:payroll|social security|employer)', 'Seguridad Social del ES (33 %)'),
        (r'\b1[.,]221\b', 'SMI ES (1.221 €)'),
        (r'\b9[.,]3\s?%', 'margen neto ES (9,3 %)'),
        (r'(?i)(?:delivery|marketplace|platform)s? (?:share|sales)[^.;]{0,30}\b10\s?%|\b10\s?% of (?:total )?sales '
         r'(?:through|via|on|from) (?:the )?(?:delivery|marketplace|platform)', 'plataforma ES (10 % de ventas)'),
        # REVISION-FINAL B4: «in this plan, 10% of sales» se colaba (el caso US es el 12 % de B16). Ningún uso legítimo
        # del conjunto dice «10% of sales» (renta «≤ 10%», cargas del 10 % e interés del 10 % no casan)
        (r'(?i)\b10 ?% of sales\b', 'plataforma ES (10 % de ventas: el caso US es el 12 %)'),
        (r'\bv1\.[01]\b|\b[Vv]ersion 1\.[01]\b', 'historia de versiones (la EN nace en 2.2)'),
    ]


FRASES_BAR = [(r'(?i)\b95 covers\b', 'caso del Bar EN («95 covers»)'),
              (r'\$27(?:\.00)?\b', 'caso del Bar EN («$27»)'),
              (r'(?i)\b360 (?:opening )?days\b', 'caso del Bar EN («360 days»)')]

# D149: restos del Bar + del ES; «97/2010», «TSG» y «Napoletana» solo en contexto UE/AVPN (fila D19 del nombre, su
# ranura del Word y «Verace Pizza Napoletana»)
_UE = r'Verace Pizza Napoletana|\bEU\b|European|AVPN'
RX_PIZ_NO = [
    (r'(?i)\btapas\b', 'Bar EN («tapas»)', None),
    (r'(?i)\bsmall plates\b', 'Bar EN («small plates»)', None),
    (r'(?i)\bcocktails?\b', 'Bar EN («cocktails»: la pizzería es beer & wine)', None),
    (r'(?i)\bspirits\b', 'Bar EN («spirits»)', None),
    (r'(?i)\bneighborhood bar\b', 'Bar EN («neighborhood bar»)', None),
    (r'(?i)\bbarbacks?\b', 'Bar EN («barback»)', None),
    (r'(?i)\blast call\b', 'Bar EN («last call»)', None),
    (r'(?i)\bhappy hour\b', 'Bar EN («happy hour»)', None),
    (r'(?i)\bdraft beer system\b', 'Bar EN («draft beer system»)', None),
    (r'\bETG\b', 'ES («ETG»)', None),
    (r'(?i)\bpliego\b', 'ES («pliego»)', None),
    (r'(?i)\bconvenio\b', 'ES («convenio»)', None),
    (r'\bSMI\b', 'ES («SMI»)', None),
    (r'(?i)\baut[oó]nomo', 'ES («autónomo»)', None),
    (r'Veri\*?factu', 'ES («Veri*factu»)', None),
    (r'\bIVA\b', 'ES («IVA»)', None),
    (r'\bSGAE\b', 'ES («SGAE»)', None),
    (r'\bIAE\b', 'ES («IAE»)', None),
    (r'(?i)\bterrazas?\b', 'ES («terraza» → patio)', None),
    (r'(?i)\bcomensal', 'ES («comensal» → covers)', None),
    (r'\b97/2010\b', 'norma UE (Reg. 97/2010) fuera de su contexto', _UE),
    (r'\bTSG\b', 'norma UE (TSG) fuera de su contexto', _UE),
    (r'(?i)\bNapoletana\b', '«Napoletana» fuera de su contexto (D149)', _UE),
    (r'(?i)\bauthentic Neapolitan\b', 'claim («authentic Neapolitan»: §0, solo «Neapolitan-style»)', None),
    (r'(?i)\bverace\b', 'claim («verace»: §0)', r'Verace Pizza Napoletana'),
    (r'\bEspaña\b|\bSpain\b', 'ES («España/Spain»)', None),
    (r'\bVAT\b', 'ES («VAT» fuera de la nota UK)', r'\bUK\b|United Kingdom|HMRC'),
    # unidades (REGLA_UNIDADES): kg, km, litros, °C y m² solo entre paréntesis (los gramos de la masa valen)
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
    """Importes en dólares ≥ 10,000 que cita la research de la pizzería: son datos de este producto y no se vetan
    aunque coincidan con un importe de otro caso EN."""
    p = os.path.join(AQUI, 'F1-research-us-delta.md')
    t = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    out = {int(x.replace(',', '')) for x in re.findall(r'\$\s?(\d{1,3}(?:,\d{3})+)', t) if int(x.replace(',', '')) >= 10000}
    out |= {int(x) * 1000 for x in re.findall(r'\$\s?(\d{2,3})K\b', t)}
    return out


def cifras_prohibidas(valores):
    """CIFRAS_PROHIBIDAS del conjunto (D149). Fuera las cifras que coinciden con un valor del propio caso US."""
    propios = {int(round(x[0])) for x in valores.values() if isinstance(x[0], (int, float))}
    out = [(_num(n), 'cifra del caso ES de la pizzería (D149)', None) for n in sorted(_cifras_es()) if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in _frases_es()]
    propios |= _importes_research()
    out += [(_num(n), 'cifra del caso del Bar EN (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(BAR, 'cifras_caso.json'), 'bar') if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_BAR]
    out += [(_num(n), 'cifra del caso FT EN publicado (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(BP, 'cifras_caso.json'), 'ft') if n not in propios]
    out += [(_num(n), 'cifra del caso del Restaurant EN publicado (no se reutiliza)', None)
            for n in _cifras_caso(os.path.join(BP2, 'cifras_caso.json'), 'rest') if n not in propios]
    out += RX_PIZ_NO
    return out


# ==========================================================================
# Tokens del docx (D147): los de FT/CAF con los rótulos de la pizzería («Comensales…») + partidas propias
# ==========================================================================
_CLIENTES = OrderedDict([
    ('Clientes/día (media del año 1)', 'Comensales/día (media del año 1)'),
    ('Clientes/día (media)', 'Comensales/día (media)'),
    ('Clientes/día', 'Comensales/día'),
    ('Clientes necesarios al día', 'Comensales necesarios al día'),
    ('Clientes necesarios al día (caja)', 'Comensales necesarios al día (caja)'),
])
_DESC = OrderedDict([
    ('clientes_dia', 'average covers (guests) per day, year 1: dine-in + take-out/delivery equivalents'),
    ('clientes_a2', 'average covers per day, year 2'),
    ('clientes_a3', 'average covers per day, year 3'),
    ('equilibrio_clientes_dia', 'break-even covers per day (accounting)'),
    ('equilibrio_caja_clientes_dia', 'cash break-even covers per day (loan payments in, depreciation out)'),
    ('pesimista_clientes', 'pessimistic scenario: covers per day'),
    ('optimista_clientes', 'optimistic scenario: covers per day'),
    ('alquiler_mes', 'rent per month (base rent of the premises)'),
    ('vida_obra', 'useful life of build-out, years'),
    ('ocupacion_anual', 'rent per year (occupancy)'),
    ('consumibles_pct', 'disposables (pizza boxes, paper, take-home containers), % of sales'),
])
_FUERA = ('inv_vehiculo', 'inv_adaptacion', 'inv_equipo_cocina', 'inv_generador', 'inv_permisos', 'inv_espresso',
          'inv_obra', 'inv_instalaciones', 'inv_mobiliario', 'inv_barra', 'inv_terraza', 'inv_lanzamiento',
          'inv_stock', 'aforo', 'rotaciones_dia')


def _inv(rot, desc):
    return ('usd', ('fila', _I, {'piz': rot}, 'B'), desc)


TOKENS_PROPIOS = OrderedDict([
    ('inv_proyecto', _inv('Proyecto técnico de actividad y de salida de humos, y dirección de obra',
                          'architect, MEP, hood & flue drawings, plan review and permit fees (beer & wine license '
                          'included, non-quota state)')),
    ('inv_obra', _inv('Obra y acondicionamiento del local, rótulo y fachada',
                      'build-out of a second-generation space, signage and facade')),
    ('inv_chimenea', _inv('Chimenea de doble pared hasta cubierta, filtro de partículas y bancada del horno',
                          'flue/chimney, spark arrestor and insulated hearth pad (solid fuel)')),
    ('inv_instalaciones', _inv('Instalación eléctrica trifásica, cuadro y boletín', 'electrical service and panel')),
    ('inv_fontaneria', _inv('Fontanería, separador de grasas, climatización y extracción',
                            'plumbing, grease interceptor, HVAC and makeup air')),
    ('inv_horno', _inv('Horno de leña de cúpula baja de 120-130 cm de diámetro',
                       'Neapolitan wood-fired dome oven, 47-51 in, UL 2162-listed')),
    ('inv_amasadora', _inv('Amasadora de espiral profesional', 'spiral mixer (60 qt)')),
    ('inv_mesa_fria', _inv('Mesa fría de pizza con encimera de granito y vitrina', 'pizza prep table (67-71 in)')),
    ('inv_frio', _inv('Armarios refrigerados para las cajas de bolas y arcón congelador',
                      'walk-in, reach-ins, dough-ball cabinets and freezer')),
    ('inv_campana', _inv('Campana extractora con motor, freidora y fogón de apoyo',
                         'Type I hood and support line (fryer, range)')),
    ('inv_lavado', _inv('Lavavajillas de capota, fregaderos, lavamanos, mesas inox y estanterías',
                        '3-compartment sink, dish machine, hand sinks and stainless')),
    ('inv_utillaje', _inv('Utillaje y menaje: palas, cajas de bolas, básculas, vajilla y uniformes',
                          'peels, dough boxes, scales and smallwares')),
    ('inv_barra', _inv('Barra: cafetera y molino, botellero frío y equipo de cerveza',
                       'beer & wine bar (taps, back bar, espresso)')),
    ('inv_mobiliario', _inv('Mobiliario de sala y terraza', 'furniture (50 seats) and patio')),
    ('inv_tpv', _inv('TPV con Veri*factu, datáfonos, impresora de comandas y tablet',
                     'POS, online ordering and delivery tablets')),
    ('inv_constitucion', _inv('Constitución de la SL, licencia, tasas, registro sanitario y APPCC',
                              'LLC, legal and food safety plan')),
    ('inv_lanzamiento', _inv('Marca, web, fotos, formación de pizzaiolo y lanzamiento',
                             'branding, website, training and launch')),
    ('inv_stock', _inv('Stock inicial de harina, tomate, quesos, bebida, leña y cajas', 'opening inventory')),
    ('aforo', ('int', ('fila', _S, {'piz': 'Aforo del local (plazas sentadas, sin la terraza)'}, 'B'),
               'indoor seats (patio not included)')),
    ('rotaciones_dia', ('dec1', ('fila', _S, {'piz': 'Rotaciones al día implícitas (calculado)'}, 'B'),
                        'implied seat turns per day (take-out and delivery included)')),
    ('comida_pct', ('pct0', ('fila', _S, {'piz': 'Ventas de COMIDA sobre el total'}, 'B'), 'food share of sales')),
    ('bebida_pct', ('pct0', ('fila', _S, {'piz': 'Ventas de BEBIDA sobre el total'}, 'B'), 'beverage share of sales')),
    ('plataforma_pct', ('pct0', ('fila', _S, {'piz': 'Ventas por delivery sobre el total'}, 'B'),
                        'share of sales through third-party delivery marketplaces')),
    ('comision_pct', ('pct0', ('fila', _S, {'piz': 'Comisión de la plataforma de delivery'}, 'B'),
                      'marketplace commission on those orders')),
    ('lena_ano', ('usd', ('fila', _P, {'piz': 'Leña para el horno'}, 'B'), 'firewood per year')),
    ('prime_cost_pct', ('pct1', ('deriv', lambda c: c['cogs_pct'] + c['personal_pct']),
                        'prime cost year 1 (cost of goods + labor, % of sales)')),
    ('meses_alquiler_previo', ('int', ('fila', _S, {'piz': 'Meses de alquiler ANTES de abrir (obra y licencias)'}, 'B'),
                               'months of rent paid before opening (build-out and permits)')),
    ('costes_variables_pct', ('pct1', ('deriv', lambda c: 1 - c['margen_bruto_pct']),
                              'all variable costs year 1 (cost of goods + disposables + marketplace + card fees + '
                              'contingency), % of sales')),
    ('otros_variables_pct', ('pct1', ('deriv', lambda c: 1 - c['margen_bruto_pct'] - c['cogs_pct']),
                             'disposables + marketplace + card fees + contingency, % of sales')),
    ('pesimista_perdida', ('usd', ('deriv', lambda c: -c['pesimista_resultado']),
                           'pessimistic scenario: pre-tax LOSS as a positive amount (only if it is a loss)')),
])


def tokens_piz(base):
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
            src = ('fila', hoja, {'piz': rot}, col)
        if t == 'consumibles_pct':
            fmt = 'pct1'
        out[t] = (fmt, src, _DESC.get(t, desc))
    out.update(TOKENS_PROPIOS)
    return out


# ==========================================================================
# Docx (D147): lo que escribe ensamblar_docx.py (índices del FT ES de 131 párrafos = PAEL) y las notas por ranura
# ==========================================================================
PRODUCTOS_CIERRE_PIZ = ['Pizza Shop Checklists Kit Pro', 'Food Cost Kit Pro', 'HACCP Food Safety Kit Pro',
                        'Restaurant Business Plan Kit']


def docx_fijos(M):
    pc = PRODUCTOS_CIERRE_PIZ
    d = OrderedDict([
        (6, 'BUSINESS PLAN'), (7, 'Neapolitan-Style Pizza Shop'),
        (9, 'Complete financial plan, market analysis,\noperations strategy and startup checklist\nto open a '
            'Neapolitan-style pizza shop in the United States'),
        (14, 'AI Chef Pro'), (15, 'aichef.pro'), (16, 'US edition with UK notes · 2026'),
        (18, 'LEGAL NOTICE'), (19, M.AVISO_DOCX_EN), (20, '© 2026 AI Chef Pro — aichef.pro'), (22, 'CONTENTS'),
        (35, 'Appendices: Pizza Shop Financial Projections (Excel) + Pizza Dough & Food Cost Calculator (Excel) + Pizza '
             'Shop Startup Checklist (Excel) + Equivalents Guide'),
        (123, 'AI Chef Pro'), (124, 'Templates and AI tools for food businesses'),
        (126, 'aichef.pro\ninfo@aichef.pro'),
        (127, '→ %s · %s' % tuple(pc[:2])), (128, '→ ' + pc[2]), (129, '→ ' + pc[3]), (130, '\n' + M.URL_TIENDA),
    ])
    return OrderedDict([('piz', d)])


DOCX_NOTAS_PLAN = OrderedDict([
    ('piz', 'Concepto (D136): NEAPOLITAN-STYLE PIZZA SHOP de barrio en una ciudad media de EE. UU. (150-300 mil hab.), '
            '~1,500 sq ft, {{aforo}} plazas + patio de 24 (abril-octubre), mesa + take-out/delivery, horno de leña de '
            'cúpula de 47-51 in listado UL 2162 (gas/eléctrico = variante, y no cumplen VPN), beer & wine (sin full '
            'liquor), cierra los lunes; el dueño es el head pizzaiolo y el GM. «Pizza shop» en el nombre y «pizzeria» '
            'como sinónimo en prosa; «Neapolitan-style» SIEMPRE (nunca «authentic», «verace» ni «VPN-certified» como '
            'promesa); volumen = «covers». Cada cifra del caso va con su token {{…}}; las de mercado solo si están en '
            'research/SPEC con fuente. El bloque ES de la ETG y sus 3 reglamentos NO cruza: en su sitio, «Neapolitan-'
            'style vs VPN-certified: what you can put on your menu» (research §6.9). Honestidad del margen: el caso da '
            'un neto de {{margen_neto_a1}} y el «15-25 %» de la SERP no se sostiene (PMQ 2026: 2-3 %). Fuera: slice '
            'shop NY, franquicia, food truck, ghost kitchen, venta desde casa. Glosario research §9 obligatorio. El '
            'cierre (productos) lo escribe el ensamblador. ' + REGLA_UNIDADES),
])

_FORMA_BAR = ('FORMA: la sección §%d del Bar EN (business-plans-en-3/docx_en_bar_%s.json) da el registro y la longitud; '
              'su vocabulario de bar (cocktails, spirits, small plates, happy hour…) y sus cifras NO valen')
_SEC = OrderedDict([
    (1, ('a', 'Resumen ejecutivo: concepto (D136), la oportunidad (research §2: «pizza shop business plan» 320/mes x6,5; '
              'mercado ≈ 75,000 pizzerías, indies > 50 %, PMQ), inversión y financiación SOLO con tokens '
              '({{inversion_total}}, {{capex}}, {{prestamo}} SBA 7(a) {{tipo_prestamo}} a {{plazo_prestamo}} años), '
              'ventas ({{ventas_a1}}, {{clientes_dia}} covers × {{ticket}} × {{dias}} días), neto {{margen_neto_a1}} y '
              'DSCR {{dscr_min}}')),
    (2, ('a', 'Concepto y propuesta: Neapolitan-style (60-90 s a ~900 °F, cornicione, leopard spotting, 00 flour, fior di '
              'latte, San Marzano DOP), carta de 14-16 pizzas + 5 starters + 3 postres, beer & wine; la ranura del NOMBRE '
              'PROTEGIDO del ES (ETG, Reg. 97/2010, 2022/2313, 2024/1143) se SUSTITUYE por «Neapolitan-style vs '
              'VPN-certified: what you can put on your menu» (research §6.9: sin norma federal; AVPN privada $2,500 + '
              '$300 + $400/año; exige local abierto y horno de leña de cúpula)')),
    (3, ('a', 'Mercado y competencia: research §2-§5 (PMQ Pizza Power Report 2026, Slice indies $561K-$658K, Margherita '
              '$18 en Bufalina, Antico y via Marina); el comprador US entre slice shop NY, franquicia y Neapolitan-style; '
              'sin datos de mercado sin fuente')),
    (4, ('a', 'Cliente y posicionamiento: mesa + take-out/delivery; el check de {{ticket}} (½ starter + pizza + 1.2 '
              'bebidas + postre/café); el pickup directo (0 % de comisión) frente a marketplaces')),
    (5, ('a', 'Marketing y ventas: Google, Yelp, Instagram; marketplaces DoorDash/Uber Eats/Grubhub con sus tiers '
              '(research §5.3: 15/25/30 % + 6-10 % pickup); el caso pone {{plataforma_pct}} de las ventas al '
              '{{comision_pct}}; la pizza Neapolitan viaja mal (radio corto, caja ventilada)')),
    (6, ('b', 'Operaciones y equipo: horno UL 2162 ({{inv_horno}}), chimenea + arrestachispas ({{inv_chimenea}}), Type '
              'I hood solo para la línea de apoyo ({{inv_campana}}), spiral mixer ({{inv_amasadora}}), prep table '
              '({{inv_mesa_fria}}); masa (biga/poolish, cold ferment, dough balls), TPHC 3-501.19; leña {{lena_ano}} al '
              'año; nunca prometer que sobra la campana (NFPA 96 / AHJ)')),
    (7, ('b', 'Organización y personal: Owner / head pizzaiolo & GM, pizzaiolo, prep & dough cook, FOH lead / bar, '
              'servers part-time W-2, weekend runner, relief cover ({{plantilla_puestos}} personas = '
              '{{plantilla_jornadas}} FTE); ≥ $15/h, sin tip credit modelado; employer payroll taxes {{cargas_pct}}; el '
              'dueño se paga por debajo del OEWS de Food Service Managers ($33.36/h): «draw in addition from net '
              'profit»')),
    (8, ('b', 'Plan financiero: TODO con tokens (ventas años 1-3, mezcla {{comida_pct}}/{{bebida_pct}}, COGS {{cogs_pct}}, '
              'personal {{personal_pct}}, prime cost {{prime_cost_pct}}, alquiler {{ocupacion_pct}}, EBITDA, neto, '
              'equilibrio {{equilibrio_clientes_dia}} / {{equilibrio_caja_clientes_dia}} covers/día, holgura '
              '{{holgura_caja_pct}}, DSCR {{dscr_min}}, saldo mínimo {{saldo_minimo}}, escenarios); neto ≈ 5 % frente al '
              '«15-25 %» de la SERP (PMQ 2-3 %): el Word dice la verdad')),
    (9, ('b', 'Marco legal US (ver las notas propias de cada ranura de §9)')),
    (10, ('b', 'Hoja de ruta: el orden del checklist (80 tareas en 6 fases: setup, site/hood/permits, kitchen/oven/health, '
               'staff & safety, menu/brand/delivery, opening & 90 days); la licencia beer & wine se pide al firmar el '
               'local (3-12 meses); cierre con el Excel, la calculadora de masa y food cost y el checklist')),
])
_RANURAS = OrderedDict([(1, range(39, 44)), (2, range(46, 51)), (3, range(53, 59)), (4, range(61, 67)),
                        (5, range(69, 76)), (6, range(78, 83)), (7, range(85, 91)), (8, range(93, 100)),
                        (9, range(102, 109)), (10, range(111, 118))])
_N9 = OrderedDict([
    (102, '§9 1/7: el marco US por niveles (federal, estatal, condado, ciudad); LLC + EIN; sales tax permit; business '
          'license; zoning check ANTES de firmar; plan review (Food Code 8-201.11) + building permit → certificate of '
          'occupancy; sales tax {{sales_tax}} de ejemplo, un solo tipo'),
    (103, '§9 2/7: horno de leña: NFPA 96 cap. 14 (escape dedicado, arrestachispas, ceniza fuera a diario, combustible '
          'lejos del horno), horno listado UL 2162; Oregon 15-01 como ejemplo de AHJ que no exige Type I con horno '
          'listado (vinculante solo allí): «ask the fire marshal in writing: hood? suppression? UL 2162 file number?»; '
          'nunca prometer que sobra la campana'),
    (104, '§9 3/7: health permit + inspección; Certified Food Protection Manager (Food Code 2-102.12) + food handler '
          'cards según estado; TPHC con procedimiento escrito (3-501.19: 4 h / 6 h); cold holding ≤ 41 °F; mozzarella y '
          'tomate cortado son TCS; la masa: «ask your regulator» (Tabla B = product assessment)'),
    (105, '§9 4/7: alérgenos: 9 mayores US incluido el sésamo (FASTER Act, 2023); trigo y leche siempre; contacto '
          'cruzado por palas y mesa; «gluten-free»: 21 CFR 101.91 (< 20 ppm) y la harina en el aire lo hacen inviable '
          'sin protocolo y análisis: el plan NO lo promete («gluten-friendly / ask» con aviso)'),
    (106, '§9 5/7: beer & wine license (agencia estatal ABC + aprobación local; estado sin cupo ≈ $3,000 dentro de '
          '{{inv_proyecto}}; con cupo, mucho más: pregunta a tu ABC); a menudo 3-12 meses: contingencia en el lease; '
          'liquor liability en el seguro ({{seguros_anual}} con general liability, property con llama abierta y '
          'workers\' comp); servicio responsable'),
    (107, '§9 6/7: personal y reparto: offer letters, I-9, W-4, salario mínimo estatal (federal $7.25/h, DOL); OSHA '
          'basics; repartidores propios = W-2 + hired & non-owned auto (check your state); marketplaces con contrato; '
          'música ASCAP/BMI/SESAC; packaging ordinances locales; «Neapolitan-style» en carta, «VPN-certified» solo con '
          'certificado AVPN'),
    (108, '§9 7/7: venta desde casa: no hay regla federal y las cottage food laws cubren productos de bajo riesgo según '
          'estado; la pizza con queso es TCS: este plan es de local con permiso («check your state»); y, como ÚLTIMA '
          'frase o frases, la NOTA UK: registro del food business en el council 28 días antes, FHRS 0-5 (FHIS en '
          'Escocia), VAT 20 % en comida caliente y en sala, 14 alérgenos, horno de leña: smoke control area / '
          'Environmental Health, premises + personal licence para el alcohol'),
])


def _notas_docx():
    out = OrderedDict()
    for s, filas in _RANURAS.items():
        tanda, nota = _SEC[s]
        for k, i in enumerate(filas, 1):
            n = _N9.get(i) or ('§%d %d/%d: %s' % (s, k, len(filas), nota))
            out[i] = n + ' ‖ ' + _FORMA_BAR % (s, tanda)
    return out


DOCX_NOTAS = OrderedDict([('piz', _notas_docx())])

# ==========================================================================
# Pistas por celda (extraer_textos.py → textos_es.json → tandas)
# ==========================================================================
_CASO = ('D137: caso US = 62 covers/día (≈ 47 en sala, 50 plazas + patio de 24 abr-oct, + ≈ 15 equivalentes de take-out '
         'y delivery) × $35 (sin sales tax ni propina) × 300 días; beer & wine; sin cifras del ES ni historia de '
         'versiones')
CELDA_PISTAS = OrderedDict([
    (('PIZP', _S, 'A2'), 'D8: añade una vez que los importes van «in your currency» (sin símbolo)'),
    (('PIZP', _S, 'C4'), _CASO + '; take-out/delivery ≈ 10 pedidos/día de ≈ $52 (2 pizzas + starter + bebida) ÷ el '
                                 'check; un sábado ≈ 110, un martes ≈ 45 (Kit estimate); compáralo con el paso de gente '
                                 'de tu calle'),
    (('PIZP', _S, 'C5'), _CASO + '; check de $35 = ½ starter ($5) + pizza (~$20: Margherita $18, especialidades $20-24) '
                                 '+ 1.2 bebidas ($6.60) + postre/café (~$3); Margherita $18 = mediana de Bufalina '
                                 '(Austin), Antico (Atlanta) y via Marina (Des Moines), research §5.1; el precio con '
                                 'impuesto lo calcula la fila "Menu price incl. sales tax"'),
    (('PIZP', _S, 'C6'), _CASO + '; 300 días = cierra los lunes (52) + Thanksgiving, Christmas, New Year, July 4 + una '
                                 'semana de enero (mantenimiento del horno y vacaciones)'),
    (('PIZP', _S, 'C13'), 'D137: food cost 26 % (pizza ≈ 21 % de su precio, starters 28 %, postres 25 %, merma 1.5 '
                          'puntos); la calculadora del kit da el coste de cada pizza'),
    (('PIZP', _S, 'C14'), 'D137: beverage cost 26 % (beer & wine, refrescos y café)'),
    (('PIZP', _S, 'C15'), 'D137: disposables 3.5 % (pizza boxes, papel, envases de take-out)'),
    (('PIZP', _S, 'C16'), 'D137: 12 % de las ventas por marketplaces (DoorDash, Uber Eats, Grubhub; research §5.3); el '
                          'pickup directo por teléfono o web no paga comisión'),
    (('PIZP', _S, 'C17'), 'D137: 25 % = plan Plus de DoorDash / Uber Eats (Basic 15 % con poca visibilidad, Premier 30 %; '
                          '+ 6-10 % en pickup por la app); compruébalo en tu contrato'),
    (('PIZP', _S, 'C24'), 'D137: $4,000/mes = 1,500 sq ft × ~$32/sq ft/año (Kit estimate); un local con salida de humos '
                          'a cubierta cuesta más encontrarlo'),
    (('PIZP', _S, 'C26'), 'D137: $1,800/mes (≈ 25 kW, agua y el gas de la línea de apoyo); con horno de gas o '
                          'eléctrico, la leña pasa aquí'),
    (('PIZP', _S, 'C27'), 'D137: $7,500/año = general liability + liquor liability (beer & wine) + property con llama '
                          'abierta + workers\' comp (research §6.8)'),
    (('PIZP', _S, 'C31'), 'D137: SBA 7(a) al 10 % a 10 años, sin interest-only; el préstamo lo calcula "Financing"'),
    (('PIZP', _S, 'C51'), 'D136: 50 plazas en sala; el patio de 24 (abril-octubre) no cuenta en el aforo'),
    (('PIZP', _N, 'A8'), 'SPEC §4.1 línea 4 (Bar): sin divisores 1,10/1,21 → «divide a menu price by 1 + your sales tax '
                         'rate»; P&L excl. sales tax, cash flow incl.; un solo tipo en el ejemplo (B39 = B40 = 8 %)'),
    (('PIZP', _N, 'A10'), 'D144: Mes 1 = SEPTIEMBRE (abre tras el verano, llega a las fiestas con clientela y a '
                          'enero-febrero con el fondo intacto)'),
    (('PIZP', _N, 'A12'), 'El Word cita las cifras de este Excel (si cambias el libro, manda el Excel); la calculadora '
                          'de masa y food cost del kit va aparte y su coste por pizza es el que llevas al food cost de '
                          '"0. Assumptions"'),
    (('PIZP', _P, 'F10'), 'D140: pizza, starters y postres: ≈ 76 % en mesa, ≈ 12 % pickup propio y 12 % por '
                          'marketplaces (research §8); un solo sales tax en el ejemplo'),
])
for _f, _nota in [(7, 'D139: incluye la beer & wine license de un estado sin cupo (≈ $3,000; con cupo, mucho más: '
                      'pregunta a tu ABC) y el plan review'),
                  (9, 'D139: NFPA 96 cap. 14 (escape dedicado, arrestachispas, solera aislada); pide el presupuesto al '
                      'instalador del horno'),
                  (12, 'D139: horno de cúpula de leña listado UL 2162 (Forno Bravo Modena120 $12,950; Marra Forni, '
                       'Acunto, Ferrara: sin precio publicado; rango $12,950-$25,000+); gas/eléctrico = variante'),
                  (16, 'D139: el Type I hood es para la línea de apoyo (freidora, fogón); el horno listado con su '
                       'chimenea puede no necesitarlo si lo acepta tu AHJ: pregunta al fire marshal por escrito'),
                  (24, 'D139: harina 00, tomate, quesos, bebida, leña y pizza boxes')]:
    CELDA_PISTAS[('PIZP', _I, 'D%d' % _f)] = _nota
for _f in range(7, 25):
    CELDA_PISTAS.setdefault(('PIZP', _I, 'D%d' % _f), 'D139: nota de la partida del ejemplo US (rótulo fijado de la col. '
                                                       'A en "fijos_en"); sin marcas ni normas españolas: solo rangos '
                                                       'con fuente de research §4 o ninguno')
# Tabla D19 (Instrucciones 35-47): «US PIZZA SHOP BENCHMARKS (sourced) AND KIT ESTIMATES» (Benchmark | Value | Source |
# Note). D142: 13 filas; solo lo «leída» con fuente; lo «(resumen)» = Kit estimate
_D19 = OrderedDict([
    (35, 'D142 fila → «Month 1 of the plan» · «September» · «Plan decision» · nota: abre tras el verano; llega a las '
         'fiestas con clientela y a enero-febrero con el fondo intacto'),
    (36, 'D142 fila → «Margherita food cost» · el % que da la calculadora del kit para la Margherita (si no, «about '
         '20% of its price excl. sales tax») · «Kit estimate (Pizza Dough & Food Cost Calculator)» · nota: 00 flour, fior '
         'di latte, San Marzano y aceite con merma; sustituye por el precio de tu distribuidor'),
    (37, 'D142 fila → «Margherita on the menu» · «$18 (median)» · «Bufalina (Austin), Antico Pizza Napoletana (Atlanta), '
         'via Marina (Des Moines): menus read Oct 2026» · nota: rango $15-24; especialidades $20-24'),
    (38, 'D142 fila → «Traditional Neapolitan dough ratios» · los gramajes del pliego en unidades US con la métrica entre '
         'paréntesis (1 quart (1 liter) of water per ~4 lb (1.8 kg) of flour, 50-55 g of salt, 3 g of fresh yeast; ≈ 56 % '
         'hydration; dough balls 6.3-8.8 oz (180-250 g)) · «EU TSG "Pizza Napoletana" spec (Reg. (EU) 97/2010), also used '
         'by the AVPN» · nota: «a reference, not a US rule»'),
    (39, 'D142 fila → «Bake» · «60-90 seconds at about 900 °F (480 °C)» · «Kit estimate (EU TSG spec and AVPN)» · nota: '
         'wood-fired dome oven; gas or electric is a variant and does not qualify for VPN'),
    (40, 'D142 fila → «"Neapolitan-style" vs "VPN-certified"» · «"Neapolitan-style": no US rule; "VPN-certified": only '
         'after AVPN certification» · «AVPN Americas (americas.pizzanapoletana.org)» · nota: $2,500 certification + $300 '
         'inspection + $400 a year (USA/Canada); needs an open location and a wood-fired dome oven'),
    (41, 'D142 fila → «Delivery marketplace commission» · «DoorDash 15 / 25 / 30% + 6% pickup; Uber Eats 15-30%» · '
         '«merchants.ubereats.com; DoorDash tiers via duck-hub.com (Oct 2026)» · nota: este plan, 25 % sobre el 12 % de '
         'las ventas; el pickup directo no paga comisión'),
    (42, 'D142 fila (sustituye «IVA de la pizza») → «Sales tax» · «8% (example: state + local)» · «Kit example: look up '
         'your state and city rate» · nota: un solo tipo en el libro; algunos estados gravan distinto la comida para '
         'llevar'),
    (43, 'D142 fila (sustituye «SMI») → «Minimum wage» · «federal $7.25/h + your state» · «U.S. Department of Labor '
         '(dol.gov)» · nota: este plan presupuesta ≥ $15/h; teclea el suelo de tu estado en "0. Assumptions"'),
    (44, 'D142 fila → «Labor cost / sales» · «25-35%» · «UpMenu (upmenu.com)» · nota: el dueño en nómina y el servicio '
         'en mesa lo llevan a la parte alta'),
    (45, 'D142 fila → «Rent / sales» · «≤ 10%» · «Kit estimate» · nota: el umbral del semáforo del P&L; un local con '
         'salida de humos a cubierta cuesta más encontrarlo'),
    (46, 'D142 fila → «Firewood» · «about $5,500 a year» · «Kit estimate» · nota: ~18 US tons (16.5 t) a year; pide el '
         'precio entregado a tu proveedor; con gas o eléctrico, va a utilities'),
    (47, 'D142 fila (sustituye «convenio») → «Prime cost (food + labor)» · «≤ 60% of sales» · «Restaurant365 '
         '(restaurant365.com)» · nota: los buenos operadores rondan el 55 %'),
])
for _f, _p in _D19.items():
    for _col in 'ABCD':
        CELDA_PISTAS[('PIZP', _N, '%s%d' % (_col, _f))] = _p

# Pistas por TEXTO propias de la pizzería (se suman a las de extraer_textos.PISTAS): D146 + research §9
PISTAS_EXTRA = [
    (r'[Cc]omensal|[Cc]ubiertos?|rotaci', 'D55/§0: el libro dice «covers» y «seat turns»; nunca «customers» para el '
                                          'volumen diario'),
    (r'napolitan|[Nn]apoletana|ETG|pliego|97/2010|2022/2313|2024/1143|AVPN', 'D149/research §6.9: «Neapolitan-style» '
                                                                         'se puede escribir; «VPN-certified» solo con '
                                                                         'certificado AVPN; el pliego/ETG es derecho UE '
                                                                         '(no aplica en EE. UU.)'),
    (r'\bSL\b|aut[oó]nomo|IAE|Seguridad Social|alta en', 'D146: «LLC vs S corp with your CPA» · «EIN + state payroll / '
                                                         'unemployment registration»'),
    (r'Veri\*?factu|TPV', 'D146: «POS that reports sales tax» (sin Veri*factu)'),
    (r'[Uu]rbanism|[Ll]icencia de (?:actividad|apertura|obra)|compatibilidad',
     'D146: «zoning check before signing» · «building permit + certificate of occupancy» · business license + sales tax '
     'permit'),
    (r'[Tt]erraza', 'D146: patio (permiso de patio/sidewalk café de la ciudad)'),
    (r'alcohol|cerveza|vino', 'D146: «beer & wine license» (state ABC + local; a menudo 3-12 meses: contingencia en el '
                              'lease) · liquor liability'),
    (r'[Hh]umos|[Cc]himenea|[Ll]eña|[Cc]ampana|extracci', 'D146/research §6.2: NFPA 96 ch. 14 (dedicated exhaust, spark '
                                                          'arrestor, UL 2162-listed oven, ash out daily, fuel away from '
                                                          'the oven) + «ask the fire marshal in writing: hood? '
                                                          'suppression? UL 2162 file number?»'),
    (r'[Rr]egistro sanitario|RGSEAA|APPCC|autocontrol', 'D146: plan review (Food Code 8-201.11) + health permit + '
                                                        'inspection; written food safety plan'),
    (r'\bgas\b|[Gg]as natural|butano|propano', 'D146: licensed gas contractor'),
    (r'[Ee]xtintor', 'D146: Class K + 2-A extinguishers'),
    (r'[Gg]rasas', 'D146: grease interceptor'),
    (r'irrellenable|Ley 1/2025|desperdicio', 'D146: sin equivalente US: TPHC written procedure (Food Code 3-501.19) y '
                                              'cold holding ≤ 41 °F'),
    (r'[Rr]eclamaciones|[Cc]arteles?', 'D146: required public notices (health permit, beer & wine license, labor law '
                                       'posters)'),
    (r'[Cc]onvenio|[Cc]ontrato|n[oó]mina', 'D146: offer letters, I-9, W-4, state minimum wage (sin convenio)'),
    (r'PRL|[Pp]revenci[oó]n de riesgos|EPI', 'D146: OSHA basics'),
    (r'[Mm]anipulador|[Ff]ormaci[oó]n', 'D146: Certified Food Protection Manager (2-102.12) + food handler cards (según '
                                        'estado)'),
    (r'[Aa]l[eé]rgen', 'D146: 9 major allergens incl. sesame (UK 14)'),
    (r'[Gg]luten|cel[ií]ac', 'D146/research §6.7: NO prometer «gluten-free» (21 CFR 101.91, < 20 ppm; harina en el '
                             'aire): «gluten-friendly / ask» con aviso'),
    (r'[Rr]ider|[Rr]epart', 'D146: own drivers = W-2 + hired & non-owned auto insurance (check your state)'),
    (r'[Pp]lataforma|Glovo|Just Eat|Uber|delivery', 'D146: DoorDash / Uber Eats / Grubhub con sus tiers (research §5.3)'),
    (r'[Ee]nvase|caja', 'D146: pizza boxes; local packaging ordinances'),
    (r'SGAE|AGEDI', 'D140: «Music licensing (ASCAP/BMI/SESAC)»'),
    (r'[Bb]arra\b', 'Glosario: barra → «bar (beer & wine)»'),
    (r'[Pp]izzaiol|[Mm]asa|bolas?|[Pp]alas?|[Cc]ornicione|leopard', 'Glosario research §9: pizzaiolo · dough ball(s) · '
                                                                    'peel · cornicione · leopard spotting'),
]

# Glosario de la pizzería (research §9, OBLIGATORIO; manda sobre el de FT/CAF)
GLOSARIO_PIZ = OrderedDict([
    ('pizzaiolo', 'pizzaiolo (head pizzaiolo; «pizza chef» en menús)'), ('bola de masa', 'dough ball / dough balls'),
    ('cornicione', 'cornicione (crust rim, edge)'), ('manchas de leopardo', 'leopard spotting (char blistering)'),
    ('harina «00» · tipo 1', '00 flour (Caputo-type) · "1" flour'),
    ('fior di latte · búfala', 'fior di latte (fresh cow\'s milk mozzarella) · mozzarella di bufala (DOP)'),
    ('tomate San Marzano DOP', 'San Marzano tomatoes (DOP)'), ('prefermento', 'biga · poolish · preferment'),
    ('pala', 'peel (wood/aluminum; turning peel)'), ('horno de cúpula · solera', 'dome oven · deck («deck» ≠ «dome»)'),
    ('pizza napolitana vs americana', 'Neapolitan-style · New York-style · Detroit-style'),
    ('pizzería', 'pizza shop (nombre, H1, ficheros) · pizzeria (prosa)'), ('cocina / sala', 'BOH / FOH'),
    ('agotado', '86\'d'), ('cubierto / comensal', 'covers'), ('ticket medio', 'average check (excl. sales tax and tip)'),
    ('coste de mercancía', 'food cost % · prime cost (food + labor)'),
    ('para llevar', 'take-out · to-go · pickup · delivery'),
    ('plataforma', 'third-party delivery marketplace (DoorDash, Uber Eats, Grubhub)'),
    ('escandallo', 'plate costing / recipe costing / food cost per pizza'),
    ('manipulador de alimentos', 'food handler card · Certified Food Protection Manager (CFPM)'),
    ('nombre protegido', '«Neapolitan-style» (libre) vs «VPN-certified» (solo con certificado)'),
    ('campana / chimenea', 'Type I hood · flue / chimney · spark arrestor · UL 2162-listed'),
    ('control por tiempo', 'time as a public health control (TPHC)'), ('hidratación · reposo', 'hydration · cold ferment / proof'),
    ('fianza · IVA', 'deposit · sales tax'),
    ('napolitana (carta)', 'Neapolitan-style'), ('ETG / pliego', 'no aplica en EE. UU. (solo nota)'),
    ('ordenanza de humos', 'NFPA 96 + local fire/mechanical code'), ('registro sanitario', 'health permit + plan review'),
    ('licencia de apertura', 'business license + certificate of occupancy'), ('convenio', 'state/local minimum wage'),
    ('autónomo / SL', 'LLC'), ('terraza', 'patio'), ('barra', 'bar (beer & wine)'),
])


# ==========================================================================
# Caso de ejemplo US (D137, D139, D140; research §8): celdas VERDES. (corto, hoja ES, celda) → (valor, rótulo)
# ==========================================================================
def valores_piz(M):
    v = OrderedDict()
    sup = [
        ('B4', 62, 'Comensales/día'), ('B5', 35, 'Ticket medio'), ('B6', 300, 'Días de apertura'),
        ('B7', 0.06, 'Crecimiento de volumen del año 2'), ('B8', 0.04, 'Crecimiento de volumen del año 3'),
        ('B11', 0.82, 'Ventas de COMIDA'), ('B13', 0.26, 'Coste de mercancía sobre las ventas de COMIDA'),
        ('B14', 0.26, 'Coste de mercancía sobre las ventas de BEBIDA'), ('B15', 0.035, 'Consumibles'),
        ('B16', 0.12, 'Ventas por delivery'), ('B17', 0.25, 'Comisión de la plataforma'),
        ('B18', 0.03, 'Comisión de los medios de pago'), ('B20', 0.10, 'Seguridad Social'),
        ('B21', 12, 'Número de pagas'), ('B22', 15080, 'SMI anual'), ('B24', 4000, 'Alquiler mensual'),
        ('B25', 2, 'Fianza'), ('B26', 1800, 'Suministros'), ('B27', 7500, 'Seguros'), ('B28', 0.01, 'Varios'),
        ('B30', 130000, 'Recursos propios'), ('B31', M.CALIBRAR, 'Préstamo bancario'), ('B32', 0.10, 'Tipo de interés'),
        ('B33', 10, 'Plazo del préstamo'), ('B34', 0, 'Carencia'), ('B35', 3, 'Fondo de maniobra'),
        ('B37', 0.25, 'Impuesto de Sociedades, nueva'), ('B38', 0.25, 'Impuesto de Sociedades, tipo'),
        ('B39', 0.08, 'IVA repercutido de restauración'), ('B40', 0.08, 'IVA repercutido/soportado'),
        ('B41', 0, 'IVA soportado en compras'), ('B42', 0, 'Bases negativas'),
        ('B44', 10, 'Vida útil de obra'), ('B45', 7, 'Vida útil de maquinaria'),
        ('B51', 50, 'Aforo'), ('B52', 0.75, 'Actividad del mes 1'), ('B53', 4, 'Meses hasta alcanzar'),
        ('B54', 2, 'Meses de alquiler ANTES'), ('B55', 0.10, 'Imprevistos sobre las partidas de OBRA'),
        ('B58', 2, 'Días medios de cobro'), ('B59', 14, 'Días medios de pago'),
        ('B62', 0.50, 'Bebida que compras al 21'), ('B63', 0.08, 'IVA de la bebida ALCOHÓLICA'),
        ('B65', 1.15, 'DSCR mínimo'), ('B66', 1.25, 'DSCR objetivo'), ('B67', 0.15, 'Holgura mínima'),
        ('B68', None, 'Suelo salarial anual'),
    ]
    for c, val, rot in sup:
        v[('PIZP', _S, c)] = (val, rot)
    # Inversión (D139): las 18 partidas tecleadas, filas 7-24 = $217,300; los imprevistos (B27) van por fórmula
    for k, val in enumerate([14000, 46500, 12000, 8000, 12000, 22000, 8000, 6500, 19800, 9000, 12000, 5500, 7000,
                             16000, 4500, 2500, 6500, 5500]):
        v[('PIZP', _I, 'B%d' % (7 + k))] = (val, None)
    # P&L (D140, D141, D142): fijos B26-B34 ($30,400), G13 (soportado de la bebida: valor en el ES) → 0, H11 → 50 %,
    # umbrales del semáforo
    for k, val in enumerate([4200, 3600, 6000, 3600, 3300, 5500, 2400, 1000, 800]):
        v[('PIZP', _P, 'B%d' % (26 + k))] = (val, None)
    v[('PIZP', _P, 'G13')] = (0, None)
    v[('PIZP', _P, 'H11')] = (0.50, None)
    for c, val, rot in [('E50', 0.62, 'Margen bruto'), ('E52', 0.28, 'Coste de mercancía /'),
                        ('E53', 0.36, 'Coste de personal'), ('E54', 0.10, 'Alquiler'), ('E55', 0.05, 'Resultado neto')]:
        v[('PIZP', _P, c)] = (val, rot)
    # Staffing (D140): personas (B), FTE por persona (C), bruto mes TOTAL de la fila (D); ≥ $15/h, 12 pagas, sin
    # propinas. Cobertura B19-B24 = ES (D140)
    for f, (b, c, d) in zip(range(5, 12), [(1, 1.0, 4500), (1, 1.0, 3900), (1, 0.75, 2340), (1, 1.0, 3293),
                                           (2, 0.25, 1343), (1, 0.375, 975), (1, 0.1, 270)]):
        for col, val in zip('BCD', (b, c, d)):
            v[('PIZP', _R, '%s%d' % (col, f))] = (val, None)
    v.update([(('PIZP', _R, 'B14'), (5000, 'Coste anual')), (('PIZP', _R, 'B15'), (5000, 'Coste anual'))])
    # Escenarios (D137): pesimista 54 · $32.50 · 295 / optimista 70 · $37.50 · 305
    v.update([
        (('PIZP', _ES, 'B5'), (54, 'Comensales/día')), (('PIZP', _ES, 'D5'), (70, 'Comensales/día')),
        (('PIZP', _ES, 'B6'), (32.5, 'Ticket')), (('PIZP', _ES, 'D6'), (37.5, 'Ticket')),
        (('PIZP', _ES, 'B7'), (295, 'Días')), (('PIZP', _ES, 'D7'), (305, 'Días')),
    ])
    return v


# Calibración D15 (D137: palancas en su orden; máx. 3 vueltas). Cada celda, citada en F2-NOTAS.md (G7). Vuelta 1
# (dry-run ES aad4cabe): research §8 tal cual da holgura 15.01 % (justa) y neto año 1 4.7 % (ámbar en D142, E55 5 %)
# → 1.ª palanca de D137, la opción «B5 $36» (la de «B30 +$10,000» solo sube el neto ≈ 0.1 punto)
CALIBRACION_D15 = OrderedDict([
    (('PIZP', _S, 'B5'), (36, 'D137 palanca 1: holgura 15.0 % y neto año 1 4.7 % < E55 → ticket $35 → $36')),
    # los tickets de los escenarios siguen al base con la lógica de D137 (∓$2.50): $32.50 / $37.50 → $33.50 / $38.50
    (('PIZP', _ES, 'B6'), (33.5, 'sigue a B5 = $36 (pesimista = base − $2.50, D137)')),
    (('PIZP', _ES, 'D6'), (38.5, 'sigue a B5 = $36 (optimista = base + $2.50, D137)')),
])


def formulas_piz():
    p = os.path.join(AQUI, 'formulas_piz.json')
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
    M.TOKENS_DOCX = tokens_piz(M.TOKENS_DOCX)
    M.PRODUCTOS_CIERRE = PRODUCTOS_CIERRE_PIZ
    M.DOCX_FIJOS = docx_fijos(M)
    M.DOCX_NOTAS = DOCX_NOTAS
    M.DOCX_NOTAS_PLAN = DOCX_NOTAS_PLAN
    M.FORMULAS_EN = formulas_piz()
    M.VALORES_EN = valores_piz(M)
    M.CALIBRACION_D15 = CALIBRACION_D15
    M.CELDA_PISTAS = CELDA_PISTAS
    M.PISTAS_EXTRA = PISTAS_EXTRA
    M.CIFRAS_PROHIBIDAS = cifras_prohibidas(M.VALORES_EN)
    M.RX_PIZ_NO = RX_PIZ_NO
    M.REGLA_UNIDADES = REGLA_UNIDADES
    glo = OrderedDict(M.GLOSARIO)
    for k, val in GLOSARIO_PIZ.items():
        glo[k] = val                          # research §9 manda (regla de jerga §0)
    M.GLOSARIO = glo
