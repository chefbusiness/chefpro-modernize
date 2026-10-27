#!/usr/bin/env python3
"""
datos_ice.py — Ice Cream Shop Business Plan Kit (EN) · los datos ES→EN que dependen del contenido: rótulos fijados
(D193-D195), POR_CELDA (D195, D193 fila 12), pistas (D191, D193, D196, D199), tokens del docx (D200), fijos y notas
del docx, caso US (D191; research §8), FORMULAS_EN (D197), cifras prohibidas y RX_ICE_NO (D202) y glosario (research
§9). Lo llama `mapas_ice.instalar()` con el módulo `mapas` YA cargado con los datos de FT/CAF (FIJOS comunes del motor
2.2, TOKENS_DOCX). Clon de `../business-plans-en-8/datos_piz.py` sin `REGLA_UNIDADES` de masa (D192). Sesión Claude
Code, 27-oct-2026 (F2-EN, paso 1a). Decisión de orquestador: D190 tal cual (base pasteurizada comprada a una central con
licencia; pasteurizar en el local = VARIANTE sin Excel).
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
HELES = os.path.join(PD, 'plan-heladeria')                 # ES cerrado: SPEC, research y cifras_caso_es.json

URL_ICE = 'aichef.pro/en/digital-products/ice-cream-shop-business-plan'
_I, _S, _P, _R, _N, _E, _ES, _T = ('Inversión Inicial', '0. Supuestos', 'PyG 3 Años', 'Personal', 'Instrucciones',
                                   'Punto Equilibrio', 'Escenarios', 'Tesorería 12 meses')
REGLA_UNIDADES = ('MEDIDAS US (John, 13-oct; SPEC §0 y D14): principales °F, sq ft, gallons / quarts / pints y lb; la '
                  'métrica entre paréntesis para UK y Australia: «0 °F (−18 °C)», «41 °F (5 °C)», «1,000 sq ft (93 sq '
                  'm)», «3 gallons (11 liters)», «20 qt (19 liters)»; la densidad legal del helado en lb por galón '
                  '(«4.5 lb per gallon»), nunca «430 g/l»; nada de kg, km, litros, m² ni °C como unidad principal (gate)')
REGLA_BASE = ('MODELO DE PRODUCCIÓN (D190, decisión SPEC): el caso COMPRA una base pasteurizada (ice cream mix / base, '
              '12-14 % butterfat) a una central láctea con licencia y la manteca en el local (aromatiza, batch-freeze, '
              'endurece). Regla de seguridad del caso: «after the dairy\'s pasteurization you add only flavorings and '
              'mix-ins: no raw eggs, no raw milk or cream; custard flavors need a custard base». Pasteurizar tu propia '
              'mezcla = VARIANTE sin Excel (batch pasteurizer ≈ $25,000-45,000, «get quotes», + licencia estatal de '
              'dairy plant / frozen dessert manufacturer + equipo 3-A); en la variante, grasas, yemas y emulsionantes '
              'ANTES de pasteurizar (mínimos estatales 155 °F 30 min / 175 °F 25 s, Ohio 901:11-3-05). La licencia '
              'SIEMPRE «depends on your state: ask your state department of agriculture» (Vermont, Georgia [leídas]; '
              'Arizona, Massachusetts, Pennsylvania en resumen); nunca «no license needed» ni una tarifa')

# ==========================================================================
# FIJOS (por TEXTO ES, en cualquier celda de los 2 libros). Parten de los de FT/CAF (los del motor 2.2)
# ==========================================================================
FIJOS_FUERA = ('Este fichero forma parte del producto «plan-negocio-food-truck» de AI Chef Pro.',
               'Este fichero forma parte del producto «plan-negocio-cafeteria» de AI Chef Pro.')
_TITULO_CHECK = 'ICE CREAM SHOP STARTUP CHECKLIST'
FIJOS_NUEVOS = OrderedDict([
    # Instrucciones!A3 del checklist con el nombre comercial (el ES trae el id interno, inv. §8)
    ('Este fichero forma parte del producto «plan-negocio-heladeria» de AI Chef Pro.',
     'This file is part of the Ice Cream Shop Business Plan Kit by AI Chef Pro.'),
    # títulos (D199 A1, D193 A1-A3); «gelato» nunca como nombre (§0)
    ('CHECKLIST DE APERTURA — HELADERÍA ARTESANAL', _TITULO_CHECK),
    ('INSTRUCCIONES DE USO — Plan financiero Heladería Artesanal',
     'HOW TO USE THIS WORKBOOK — Ice Cream Shop Financial Projections'),
    ('PLAN DE NEGOCIO: HELADERÍA ARTESANAL', 'ICE CREAM SHOP BUSINESS PLAN'),
    ('Inversión inicial estimada — heladería artesanal con obrador propio',
     'Startup costs — ice cream shop with on-site production'),
    ('Ajusta las cifras a tu proyecto.', 'US kit example (2026) — replace with your own quotes.'),
    ('Punto de equilibrio — heladería artesanal', 'Break-even — ice cream shop with on-site production'),
    # D196: cabecera de la tabla D19; rótulo nuevo de Supuestos (inv. rotulos_nuevos)
    ('DATOS DE REFERENCIA DEL SECTOR', 'US ICE CREAM SHOP BENCHMARKS (sourced) AND KIT ESTIMATES'),
    ('IVA de la bebida ALCOHÓLICA servida en el local', 'Sales tax rate on alcohol served on site'),
    # D193: partidas de la inversión, filas 7-25 (solo rótulo: ninguna fila se mueve; la clase de amortización la fija
    # la fila: 7-11 obra, 12-21 equipo, 22-25 no se amortizan)
    ('Proyecto técnico y dirección de obra', 'Architect, MEP drawings, plan review & permit fees'),
    ('Obra y acondicionamiento del obrador y la tienda',
     'Build-out of production room & shop (second-generation retail, ~1,000 sq ft)'),
    ('Instalación eléctrica trifásica, cuadro y boletín', 'Electrical service & panel (about 30 kW)'),
    ('Fontanería, desagües, climatización y ventilación',
     'Plumbing, floor sinks, hand sinks, HVAC & condenser ventilation'),
    ('Rótulo y escaparate', 'Signage & storefront'),
    ('Pasteurizador de 30 litros', 'Base refrigerator & flavor prep (41 °F or colder, stick blender, scales)'),
    ('Mantecadora horizontal de 6-12 litros por ciclo', 'Batch freezer (20 qt, horizontal)'),
    ('Abatidor de temperatura para cubetas', 'Hardening cabinet / blast freezer'),
    ('Armarios de conservación y de maduración', 'Storage freezers (0 °F or colder)'),
    ('Mesas inox, fregadero, básculas, refractómetro, sondas, cubetas y carapinas',
     'Prep tables, 3-compartment sink, hand sinks, scales, pans & smallwares'),
    ('Vitrina ventilada de 18 cubetas', 'Dipping cabinets (18 flavors)'),
    ('Mostrador, lavaporcionador, cafetera, crepera, gofrera y chocolatera',
     'Front counter, dipper wells, espresso, waffle cone irons & hot fudge warmers'),
    ('Mobiliario del local y de la terraza', 'Furniture (20 seats) & patio'),
    ('TPV con Veri*factu, datáfono y báscula', 'POS, card terminal & online ordering'),
    ('Menaje, uniformes y cartelería de alérgenos', 'Scoops, spades, cups, uniforms & allergen signage'),
    ('Formación técnica de heladería', 'Ice cream training course'),
    ('Marca, web, fotos y lanzamiento', 'Branding, website, photos & launch'),
    ('Constitución de la SL, licencia, tasas, registro sanitario y APPCC', 'LLC, legal, permits & food safety plan'),
    ('Stock inicial de materias primas y envases', 'Opening inventory (base, flavorings, cones, cups, pint containers)'),
    # D194: P&L (A2, A10, A11, seguros A25, fijos A26-A35)
    ('Escenario realista — heladería artesanal', 'Base case — ice cream shop with on-site production'),
    ('Ventas de helado y obrador (mostrador, para llevar, tartas, invierno y restaurantes)',
     'Ice cream sales (scoops, sundaes, pints & quarts to go, ice cream cakes, catering)'),
    ('Ventas de cafetería y bebidas (sin alcohol)', 'Coffee & beverages (espresso, hot chocolate, sodas, water)'),
    ('Seguros (RC + multirriesgo)', 'Insurance (general liability, property, equipment breakdown + food spoilage)'),
    ('Gestoría laboral, fiscal y contable', 'Accounting & bookkeeping'),
    ('Mantenimiento del frío (contrato con frigorista certificado)',
     'Refrigeration service contract (EPA 608-certified tech)'),
    ('Marketing y publicidad de temporada', 'Seasonal marketing'),
    ('Software, teléfono e internet', 'Software, POS & phone'),
    ('Limpieza, lavandería, EPI y análisis de autocontrol', 'Cleaning supplies, uniforms & laundry'),
    ('Tasa de terraza (pon la de tu ayuntamiento)', "Sidewalk café / patio permit (your city's fee)"),
    ('Gestión de residuos', 'Waste & recycling'),
    ('Desinsectación, desratización y desinfección (DDD)', 'Pest control'),
    ('Derechos de autor por música ambiental (SGAE y AGEDI-AIE)', 'Music licensing (ASCAP/BMI/SESAC)'),
    ('Prevención de riesgos laborales y vigilancia de la salud',
     'Food safety & OSHA training (CFPM, food handler cards, allergens)'),
    # D194: puestos de Staffing (A5:A10), 1 persona por fila
    ('Titular — maestro heladero, compras y gestión', 'Owner / ice cream maker & GM'),
    ('Dependiente/a y encargado/a de turno (todo el año)', 'Shift lead / counter (year-round)'),
    ('Dependiente/a de temporada (fijo discontinuo, abril-septiembre)', 'Seasonal scooper (part-time, April-September)'),
    ('Dependiente/a de verano (fijo discontinuo, junio-septiembre)', 'Summer scooper (part-time, June-August)'),
    ('Ayudante de obrador (fijo discontinuo, mayo-septiembre)', 'Production assistant (part-time, May-September)'),
    ('Suplencias de vacaciones y descansos', 'Relief cover (vacations and days off)'),
])

# Mismo ES con otro EN en ESTA celda (D193 fila 12, D194, D195; lección de BP2 §4.1: no se heredan a ciegas)
POR_CELDA = OrderedDict([
    # D193 / D190: la fila 12 del ES era el pasteurizador; en el caso US es la nevera de la base y la preparación
    (('HELP', _I, 'D12'), 'Base case: you buy pasteurized base from a licensed dairy, keep it at 41 °F (5 °C) or colder '
                          'and add only flavorings and mix-ins. Making your own mix adds a batch pasteurizer (about '
                          '$25,000-45,000: get quotes) and, in many states, a dairy or frozen dessert manufacturer '
                          'license: ask your state department of agriculture'),
    # D195: sin alcohol (B62 = 0 → G11 = B39) y sin crédito por compras
    (('HELP', _S, 'C62'), 'Set to ZERO: the beverage menu of this plan is coffee, hot chocolate, shakes, sodas and water, '
                          'with no alcohol. If you add alcohol, type its share of beverage sales here: it needs a state '
                          'liquor license, and its sales tax uses the cell below (on site) and B40 (to go)'),
    (('HELP', _S, 'C63'), 'NO EFFECT in this plan (the cell above is at 0). If you serve alcohol, type the sales tax rate '
                          'your state applies to alcohol served on site. With the example, everything pays the same 8% '
                          '(state + local)'),
    # D195: Mes 1 = marzo (pesos del ES sin tocar, inv. §2.8); trimestres del plan; liquidación del sales tax
    (('HELP', _T, 'O5'), 'Month 1 = MARCH: open in season so the first winter is paid by the first summer. July (Month 5, '
                         'National Ice Cream Month) is the peak; January (Month 11) the low point, with a three-week '
                         'closure. Kit weights for a mid-size US city: replace the weights with your area\'s pattern '
                         '(colder states: more weight June-August; Sun Belt: flatter). If you open in another month, '
                         'rotate the row. It must add up to 100%'),
    (('HELP', _T, 'A34'), 'The quarters in this sheet are plan quarters, not calendar quarters (March-May, June-August, '
                          'September-November and December-February): with Month 1 in March, the workbook remits the '
                          'sales tax of each plan quarter in the month after it. Your state sets the real filing '
                          'calendar (monthly, quarterly or annual): check it. Income tax for year 1 is paid in year 2. The '
                          'loan payment is split into twelve equal parts following the ANNUAL schedule in "Financing", and '
                          'payroll into twelve monthly installments'),
    (('HELP', _T, 'O20'), 'Cash only leaves when the quarter\'s result is positive. Months without a settlement are left '
                          'blank, not zero. The cell turns RED when the payment takes more cash than is left that month. '
                          'The model settles quarterly, in the month after each plan quarter (Months 4, 7 and 10: June, '
                          'September and December with Month 1 in March; the fourth quarter is remitted in Month 13): if '
                          'your state requires monthly filing, expect smaller payments every month instead'),
    # D194: la nota de Staffing de la Bakery/Pizza sin E4 (una persona por fila) y sin propinas modeladas
    (('HELP', _R, 'A28'), 'The gross pay, employer payroll taxes, monthly cost and annual cost columns are TOTALS for the '
                          'row: for a position with two people they include both. "FTE" is the share of a full-time week '
                          'and is used to compare pay with the legal floor pro rata. The payroll tax rate and the number '
                          'of pay periods are in the "0. Assumptions" tab. Tips are not modeled: the shift lead and the '
                          'scoopers are budgeted at a base wage of at least $15/h'),
])

# ==========================================================================
# Cifras prohibidas (D202): ES de la heladería (importe y frase), caso de la Pizza EN, de la Bakery EN, del Bar EN, FT
# y REST, y RX_ICE_NO. Formato: (regex, motivo, excepción sobre el texto entero)
# ==========================================================================
def _num(n):
    """162000 → patrón que casa 162,000 · 162.000 · 162 000 · 162000 (y nada pegado a más dígitos)."""
    s = str(n)
    cab, cola = s[:-3], s[-3:]
    return r'(?<![\d.,])' + cab + r'[.,   ]?' + cola + r'(?![\d])'


def _cifras_es():
    """Importes ≥ 10.000 € del caso ES de la heladería (`../plan-heladeria/cifras_caso_es.json`, tokens con «€»: el ES
    está cerrado y manda). Los pequeños quedan cubiertos por la prohibición de «€»."""
    out = set()
    p = os.path.join(HELES, 'cifras_caso_es.json')
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
        (r'(?i)\b143 (?:customers|guests|people|visitors|buyers)\b', 'caso ES (143 clientes/día)'),
        (r'(?<![\d$])4[.,]90\b', 'ticket ES (4,90 €)'),
        (r'(?i)\b14 (?:pay periods|payments|paychecks|salaries|monthly)', 'pagas del ES (14 pagas)'),
        (r'(?i)(?:payroll|social security|employer)[^.;]{0,60}?\b33\s?%', 'Seguridad Social del ES (33 %)'),
        (r'(?i)\b33\s?%[^.;]{0,40}?(?:payroll|social security|employer)', 'Seguridad Social del ES (33 %)'),
        (r'\b17[.,]094\b', 'SMI ES (17.094 €)'),
        (r'\b1[.,]221\b', 'SMI ES (1.221 €)'),
        (r'\b644\.4\b', 'IAE ES (644.4)'),
        (r'(?<![$\d.,])\b676\b(?![.,]\d)', 'IAE ES (676)'),
        (r'(?i)\b430 ?g\b', 'densidad ES (430 g/l: en EE. UU., 4.5 lb per gallon)'),
        (r'[−-]18 ?°C(?![^()]*\))', '−18 °C como regla (en EE. UU., 0 °F; la métrica solo entre paréntesis)'),
        (r'(?i)fijos? discontinuos?', 'ES («fijo discontinuo» → seasonal part-time W-2)'),
        # delivery ES = 3 % de las ventas; la TARJETA US también es el 3 % (B18): solo con contexto de delivery
        (r'(?i)(?:delivery|marketplace|DoorDash|Uber Eats|apps?)[^.;]{0,40}?\b3 ?% of (?:total |all )?sales|'
         r'\b3 ?% of (?:total |all )?sales (?:through|via|on|from|by) (?:the )?(?:delivery|marketplace|DoorDash|Uber|apps?)',
         'delivery ES (3 % de las ventas: el caso US es el 4 % de B16)'),
        (r'\bv1\.[01]\b|\b[Vv]ersion 1\.[01]\b', 'historia de versiones (la EN nace en 2.2)'),
    ]


FRASES_OTROS = [(r'(?i)\b62 covers\b', 'caso de la Pizza EN («62 covers»)'),
                (r'\$36(?:\.00)?\b', 'caso de la Pizza EN («$36»)'),
                (r'(?i)\b210 transactions\b', 'caso de la Bakery EN («210 transactions»)'),
                (r'(?i)\b95 covers\b', 'caso del Bar EN («95 covers»)'),
                (r'\$27(?:\.00)?\b', 'caso del Bar EN («$27»)'),
                (r'(?i)\b360 (?:opening )?days\b', 'caso del Bar EN («360 days»)')]
# «300 days» de la pizza NO se veta (D202 lo pedía): el pesimista de la heladería es de 300 días (D191)

# D202: restos de la pizza, de la panadería y del ES
_PASTEURIZ_OK = (r'(?i)licensed dairy|dairy|your own mix|own mix|make your own|making your own|variant|batch '
                 r'pasteurizer|licen[cs]e|155 ?°F|175 ?°F|pasteurized (?:base|mix|ice cream mix)|3-A')
_NEGACION = r"(?i)\b(?:no|not|never|cannot|can't|don't|do not|without)\b[^.;]{0,60}allergen-free"
RX_ICE_NO = [
    # Pizza EN
    (r'(?i)\bpizz', 'Pizza EN («pizza»)', None),
    (r'(?i)(?<!cookie )\bdough\b', 'Pizza EN («dough»; «cookie dough» como sabor vale)', None),
    (r'(?i)\bovens?\b', 'Pizza EN («oven»)', None),
    (r'(?i)\bNeapolitan\b', 'Pizza EN («Neapolitan»)', None),
    (r'\bVPN\b', 'Pizza EN («VPN»)', None),
    (r'(?i)\bfirewood\b|\bwood-fired\b', 'Pizza EN («firewood»)', None),
    (r'(?i)\bbeer (?:&|and) wine\b', 'Pizza EN («beer & wine»)', None),
    (r'(?i)\bequivalent covers\b|\bcovers?(?: per day|/day| a day)\b|\b\d+ covers\b', 'Pizza EN («covers»)', None),
    (r'(?i)\bflue\b|\bspark arrestor\b', 'Pizza EN («flue»)', None),
    # Bakery EN
    (r'(?i)\bbread\b', 'Bakery EN («bread»)', None),
    (r'(?i)\bbakery\b', 'Bakery EN («bakery»)', None),
    (r'(?i)\bbakers?\b', 'Bakery EN («baker»)', None),
    (r'(?i)\bloa(?:f|ves)\b', 'Bakery EN («loaf»)', None),
    (r'(?i)\btransactions? (?:per|a) day\b|\btransactions/day\b', 'Bakery EN («transactions per day»)', None),
    # Bar EN
    (r'(?i)\btapas\b|\bcocktails?\b|\bhappy hour\b|\bneighborhood bar\b', 'Bar EN', None),
    # ES
    (r'\bIVA\b', 'ES («IVA»)', None),
    (r'\bIAE\b', 'ES («IAE»)', None),
    (r'(?i)\baut[oó]nomo', 'ES («autónomo»)', None),
    (r'(?i)\bconvenio\b', 'ES («convenio»)', None),
    (r'\bSMI\b', 'ES («SMI»)', None),
    (r'Veri\*?factu', 'ES («Veri*factu»)', None),
    (r'\bRGSEAA\b', 'ES («RGSEAA»)', None),
    (r'\bSGAE\b', 'ES («SGAE»)', None),
    (r'(?i)\bterrazas?\b', 'ES («terraza» → patio)', None),
    (r'(?i)helader', 'ES («heladería» → ice cream shop)', None),
    (r'(?i)mantecad', 'ES («mantecado/mantecadora» → frozen custard / batch freezer)', None),
    (r'(?i)\bcarn[eé]t?\b', 'ES («carné de manipulador»)', None),
    (r'\b618/1998\b|\bRD 618\b', 'ES («RD 618/1998»)', None),
    (r'\b1021/2022\b', 'ES («RD 1021/2022»)', None),
    (r'(?i)\bcrepes?\b|\bcrêpes?\b', 'ES («crepes»: no cruzan, D200)', None),
    (r'(?i)\bturr[oó]n\b', 'ES («turrón» → holiday pies and cakes)', None),
    (r'(?i)\bcomuni[oó]n', 'ES («comunión» → birthdays and graduations)', None),
    (r'\bEspaña\b|\bSpain\b', 'ES («España/Spain»)', None),
    (r'\bVAT\b', 'ES («VAT» fuera de la nota UK)', r'\bUK\b|United Kingdom|HMRC'),
    # D190 / D202: el caso NO pasteuriza; «pasteuriz» solo con la base comprada o en la variante
    (r'(?i)\bpasteuri[sz]', '«pasteuriz» fuera de la base comprada / la variante (D190, D202)', _PASTEURIZ_OK),
    (r'(?i)\b85 ?°C|\b185 ?°F', 'temperatura de pasteurización del ES (85 °C): el caso compra la base (D190)', None),
    # §0 y research §9: «gelato» solo como estilo; nunca el nombre del negocio
    (r'(?i)\bgelato (?:shop|business|parlou?r|store)s?\b|\bgelateria\b|\bartisan gelato\b',
     '«gelato» como nombre del negocio (§0: solo como estilo)', None),
    # claims (D203): ni «no license needed» ni «allergen-free» prometido
    (r'(?i)\bno (?:dairy |state |special )?licen[cs]e (?:is )?(?:needed|required)\b|\blicen[cs]e-free\b',
     'claim («no license needed»: D190)', None),
    (r'(?i)\ballergen-free\b', 'claim («allergen-free»: scoops y dipper wells compartidos)', _NEGACION),
    # unidades (REGLA_UNIDADES): kg, km, litros, °C, m² y g/l solo entre paréntesis
    (r'(?i)\d\s?(?:kg|km|°C|liters?|litres?|m²|sq m|g/l)\b(?![^()]*\))',
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
    """Importes en dólares ≥ 10,000 que citan la research y la SPEC de la heladería: son datos de este producto y no se
    vetan aunque coincidan con un importe de otro caso EN."""
    out = set()
    for f in ('F1-research-us-delta.md', 'SPEC-delta.md'):
        p = os.path.join(AQUI, f)
        t = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
        for m in re.finditer(r'\$\s?(\d{1,3}(?:,\d{3})+)(?:\s?[-–]\s?\$?(\d{1,3}(?:,\d{3})+))?', t):  # «$25,000-45,000»
            out |= {int(x.replace(',', '')) for x in m.groups() if x and int(x.replace(',', '')) >= 10000}
        out |= {int(x) * 1000 for x in re.findall(r'\$\s?(\d{2,3})K\b', t)}
    return out


def cifras_prohibidas(valores):
    """CIFRAS_PROHIBIDAS del conjunto (D202). Fuera las cifras que coinciden con un valor del propio caso US."""
    propios = {int(round(x[0])) for x in valores.values() if isinstance(x[0], (int, float))}
    out = [(_num(n), 'cifra del caso ES de la heladería (D202)', None) for n in sorted(_cifras_es()) if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in _frases_es()]
    propios |= _importes_research()
    for path, plan, nombre in [(os.path.join(PIZ, 'cifras_caso.json'), 'piz', 'de la Pizza EN'),
                               (os.path.join(BP2, 'cifras_caso.json'), 'pan', 'de la Bakery EN'),
                               (os.path.join(BAR, 'cifras_caso.json'), 'bar', 'del Bar EN'),
                               (os.path.join(BP, 'cifras_caso.json'), 'ft', 'del FT EN'),
                               (os.path.join(BP2, 'cifras_caso.json'), 'rest', 'del Restaurant EN')]:
        out += [(_num(n), 'cifra del caso %s (no se reutiliza)' % nombre, None)
                for n in _cifras_caso(path, plan) if n not in propios]
    out += [(rx, motivo, None) for rx, motivo in FRASES_OTROS]
    out += RX_ICE_NO
    return out


# ==========================================================================
# Tokens del docx (D200): los de FT/CAF (la heladería dice «Clientes», como el FT) + las 19 partidas + propios
# ==========================================================================
_DESC = OrderedDict([
    ('clientes_dia', 'average customers per day, year 1 (each person who buys: counter, patio and to-go)'),
    ('clientes_a2', 'average customers per day, year 2'),
    ('clientes_a3', 'average customers per day, year 3'),
    ('equilibrio_clientes_dia', 'break-even customers per day (accounting)'),
    ('equilibrio_caja_clientes_dia', 'cash break-even customers per day (loan payments in, depreciation out)'),
    ('pesimista_clientes', 'pessimistic scenario: customers per day'),
    ('optimista_clientes', 'optimistic scenario: customers per day'),
    ('alquiler_mes', 'rent per month (base rent of the premises)'),
    ('vida_obra', 'useful life of build-out, years'),
    ('ocupacion_anual', 'rent per year (occupancy)'),
    ('consumibles_pct', 'disposables (cups, spoons, pint and quart containers, cake boxes), % of sales'),
    ('marketing_anual', 'seasonal marketing budget per year'),
])
_FUERA = ('inv_lanzamiento', 'inv_stock', 'inv_vehiculo', 'inv_adaptacion', 'inv_equipo_cocina', 'inv_generador',
          'inv_permisos', 'inv_obra', 'inv_instalaciones', 'inv_espresso', 'inv_mobiliario', 'inv_barra', 'inv_terraza',
          'aforo', 'rotaciones_dia')
_ROT_PROPIO = {'marketing_anual': 'Marketing y publicidad de temporada'}


def _inv(rot, desc):
    return ('usd', ('fila', _I, {'ice': rot}, 'B'), desc)


TOKENS_PROPIOS = OrderedDict([
    ('inv_proyecto', _inv('Proyecto técnico y dirección de obra', 'architect, MEP drawings, plan review and permit fees')),
    ('inv_obra', _inv('Obra y acondicionamiento del obrador y la tienda',
                      'build-out of the production room and shop (second-generation retail, ~1,000 sq ft)')),
    ('inv_electrica', _inv('Instalación eléctrica trifásica, cuadro y boletín', 'electrical service and panel (about 30 kW)')),
    ('inv_fontaneria', _inv('Fontanería, desagües, climatización y ventilación',
                            'plumbing, floor sinks, hand sinks, HVAC and condenser ventilation')),
    ('inv_rotulo', _inv('Rótulo y escaparate', 'signage and storefront')),
    ('inv_base_frio', _inv('Pasteurizador de 30 litros',
                           'base refrigerator and flavor prep (41 °F or colder, stick blender, scales): the case buys '
                           'pasteurized base, so there is NO pasteurizer in the budget')),
    ('inv_batch_freezer', _inv('Mantecadora horizontal de 6-12 litros por ciclo', 'batch freezer (20 qt, horizontal)')),
    ('inv_hardening', _inv('Abatidor de temperatura para cubetas', 'hardening cabinet / blast freezer')),
    ('inv_congeladores', _inv('Armarios de conservación y de maduración', 'storage freezers (0 °F or colder)')),
    ('inv_utillaje', _inv('Mesas inox, fregadero, básculas, refractómetro, sondas, cubetas y carapinas',
                          'prep tables, 3-compartment sink, hand sinks, scales, pans and smallwares')),
    ('inv_dipping', _inv('Vitrina ventilada de 18 cubetas', 'dipping cabinets (18 flavors)')),
    ('inv_mostrador', _inv('Mostrador, lavaporcionador, cafetera, crepera, gofrera y chocolatera',
                           'front counter, dipper wells, espresso, waffle cone irons and hot fudge warmers')),
    ('inv_mobiliario', _inv('Mobiliario del local y de la terraza', 'furniture (20 seats) and patio')),
    ('inv_tpv', _inv('TPV con Veri*factu, datáfono y báscula', 'POS, card terminal and online ordering')),
    ('inv_menaje', _inv('Menaje, uniformes y cartelería de alérgenos', 'scoops, spades, cups, uniforms and allergen signage')),
    ('inv_formacion', _inv('Formación técnica de heladería', 'ice cream training course')),
    ('inv_lanzamiento', _inv('Marca, web, fotos y lanzamiento', 'branding, website, photos and launch')),
    ('inv_constitucion', _inv('Constitución de la SL, licencia, tasas, registro sanitario y APPCC',
                              'LLC, legal, permits and food safety plan')),
    ('inv_stock', _inv('Stock inicial de materias primas y envases',
                       'opening inventory (base, flavorings, cones, cups, pint containers)')),
    ('aforo', ('int', ('fila', _S, {'ice': 'Aforo del local (plazas sentadas, sin la terraza)'}, 'B'),
               'indoor seats (patio not included)')),
    ('comida_pct', ('pct0', ('fila', _S, {'ice': 'Ventas de COMIDA sobre el total'}, 'B'),
                    'ice cream share of sales (scoops, sundaes, pints, cakes, catering)')),
    ('bebida_pct', ('pct0', ('fila', _S, {'ice': 'Ventas de BEBIDA sobre el total'}, 'B'),
                    'coffee & beverage share of sales')),
    ('delivery_pct', ('pct0', ('fila', _S, {'ice': 'Ventas por delivery sobre el total'}, 'B'),
                      'share of sales through third-party delivery marketplaces (pints and quarts)')),
    ('comision_pct', ('pct0', ('fila', _S, {'ice': 'Comisión de la plataforma de delivery'}, 'B'),
                      'marketplace commission on those orders')),
    ('produccion_horas', ('dec1', ('fila', _R, {'ice': 'Horas de producción al día ANTES de abrir'}, 'B'),
                          'production hours a day before opening (batch freezing and hardening; no pasteurizing)')),
    ('sabores', ('int', ('deriv', lambda c: 18),
                 'flavors in the dipping cabinets in season (10-12 in winter): fixed by the dipping cabinet line')),
    ('fijos_anual', ('usd', ('deriv', lambda c: c['costes_fijos_a1'] - c['ocupacion_anual'] - c['personal_a1'] -
                             12 * c['suministros_mes'] - c['seguros_anual'] - c['amortizacion_anual'] -
                             c['intereses_a1']),
                     'other fixed costs per year, year 1 (accounting, refrigeration service, marketing, software, '
                     'cleaning, patio permit, waste, pest control, music licensing, training)')),
    ('prime_cost_pct', ('pct1', ('deriv', lambda c: c['cogs_pct'] + c['personal_pct']),
                        'prime cost year 1 (cost of goods + labor, % of sales)')),
    ('meses_alquiler_previo', ('int', ('fila', _S, {'ice': 'Meses de alquiler ANTES de abrir (obra y licencias)'}, 'B'),
                               'months of rent paid before opening (build-out and permits)')),
    ('costes_variables_pct', ('pct1', ('deriv', lambda c: 1 - c['margen_bruto_pct']),
                              'all variable costs year 1 (cost of goods + disposables + marketplace + card fees + '
                              'contingency), % of sales')),
    ('otros_variables_pct', ('pct1', ('deriv', lambda c: 1 - c['margen_bruto_pct'] - c['cogs_pct']),
                             'disposables + marketplace + card fees + contingency, % of sales')),
    ('pesimista_perdida', ('usd', ('deriv', lambda c: -c['pesimista_resultado']),
                           'pessimistic scenario: pre-tax LOSS as a positive amount (only if it is a loss)')),
])


def tokens_ice(base):
    out = OrderedDict()
    for t, (fmt, src, desc) in base.items():
        if t in _FUERA:
            continue
        if src[0] == 'fila':
            _, hoja, rot, col = src
            if t in _ROT_PROPIO:
                rot = _ROT_PROPIO[t]
            elif isinstance(rot, dict):                   # ocupación: el rótulo de la cafetería es el del motor común
                rot = rot['caf']
            src = ('fila', hoja, {'ice': rot}, col)
        if t == 'consumibles_pct':
            fmt = 'pct1'
        out[t] = (fmt, src, _DESC.get(t, desc))
    out.update(TOKENS_PROPIOS)
    return out


# ==========================================================================
# Docx (D200): lo que escribe ensamblar_docx.py (índices del FT ES de 131 párrafos = PIZ) y las notas por ranura
# ==========================================================================
PRODUCTOS_CIERRE_ICE = ['Ice Cream Shop Checklists Kit Pro', 'Food Cost Kit Pro', 'HACCP Food Safety Kit Pro']


def docx_fijos(M):
    pc = PRODUCTOS_CIERRE_ICE
    d = OrderedDict([
        (6, 'BUSINESS PLAN'), (7, 'Ice Cream Shop'),
        (9, 'Complete financial plan, market analysis,\noperations strategy and startup checklist\nto open an ice cream '
            'shop that makes its own ice cream in the United States'),
        (14, 'AI Chef Pro'), (15, 'aichef.pro'), (16, 'US edition with UK notes · 2026'),
        (18, 'LEGAL NOTICE'), (19, M.AVISO_DOCX_EN), (20, '© 2026 AI Chef Pro — aichef.pro'), (22, 'CONTENTS'),
        (35, 'Appendices: Ice Cream Shop Financial Projections (Excel) + Ice Cream Shop Startup Checklist (Excel) + '
             'Equivalents Guide'),
        (123, 'AI Chef Pro'), (124, 'Templates and AI tools for food businesses'),
        (126, 'aichef.pro\ninfo@aichef.pro'),
        (127, '→ ' + pc[0]), (128, '→ ' + pc[1]), (129, '→ ' + pc[2]), (130, '\n' + M.URL_TIENDA),
    ])
    return OrderedDict([('ice', d)])


DOCX_NOTAS_PLAN = OrderedDict([
    ('ice', 'Concepto (D189): ICE CREAM SHOP de barrio que HACE su helado en el local (batch freezer a la vista), '
            'ciudad media de EE. UU. (150-300 mil hab.), ~1,000 sq ft (sala de producción ~250), dipping cabinets de '
            '{{sabores}} sabores (10-12 en invierno), {{aforo}} plazas + patio de 5 mesas en temporada; scoops, sundaes, '
            'pints y quarts hand-packed, ice cream cakes por encargo, café y chocolate caliente, catering. Abierto todo '
            'el año: cierra 3 semanas en enero, Thanksgiving, Christmas y los lunes de noviembre a febrero. El dueño es '
            'el ice cream maker y el GM. «Ice cream shop» en el nombre; «ice cream parlor», «scoop shop» y «creamery» '
            'como sinónimos en prosa; «gelato» SOLO como estilo (nunca el nombre); «homemade» / «made here in small '
            'batches» solo con lo que se hace en el local. Volumen = «customers» (cada persona que compra), nunca '
            '«covers» ni «transactions». Cada cifra del caso va con su token {{…}}; las de mercado solo si están en '
            'research/SPEC con fuente. Honestidad del margen: el caso da un neto de {{margen_neto_a1}} y el «10-25 %» '
            'de la SERP no se sostiene (IBISWorld ≈ 5.5 %, resumen). Fuera: soft serve / frozen yogurt, ice cream truck '
            '(→ Food Truck Business Plan Kit), franquicia, quiosco sin producción, venta desde casa. Nada de crepes ni '
            'de nada que pida campana o salida de humos. Glosario research §9 obligatorio. El cierre (productos) lo '
            'escribe el ensamblador. ' + REGLA_BASE + ' ' + REGLA_UNIDADES),
])

_FORMA = ('FORMA: la sección §%d de la Pizza EN (business-plans-en-8/docx_en_piz_%s.json) da el registro y la longitud; '
          'su vocabulario de pizzería (pizza, oven, dough, covers, beer & wine, Neapolitan…) y sus cifras NO valen')
_SEC = OrderedDict([
    (1, ('a', 'Resumen ejecutivo: concepto (D189), la oportunidad (research §2: «ice cream shop business plan» 320/mes; '
              'el hueco de la SERP: plan Word + Excel con estacionalidad + checklist), inversión y financiación SOLO con '
              'tokens ({{inversion_total}}, {{capex}}, {{fondos_propios}}, {{prestamo}} SBA 7(a) {{tipo_prestamo}} a '
              '{{plazo_prestamo}} años), ventas ({{ventas_a1}}: {{clientes_dia}} customers × {{ticket}} × {{dias}} '
              'días), neto {{margen_neto_a1}}, holgura {{holgura_caja_pct}} y DSCR {{dscr_min}}; el equipo (dueño ice '
              'cream maker + shift lead + seasonal scoopers)')),
    (2, ('a', 'Concepto y propuesta: los tipos de negocio (scoop shop que hace su helado vs franquicia, soft serve, '
              'quiosco) y por qué este; base comprada y batch freezer a la vista (D190); {{sabores}} sabores en verano y '
              '10-12 en invierno, sorbets sin lácteos; carta de ejemplo research §5.1 (single $5.25, double $7.00, '
              'kid\'s $4.25, waffle cone +$1.25, sundae $9.00, pint $11, quart $18, ice cream cake 8 in $45, espresso '
              '$3.50, hot chocolate $4.50: «Kit estimate (Oct 2026), excl. sales tax»); ticket por persona {{ticket}} '
              '(precio con impuesto {{precio_menu}}); invierno SIN crepes: ice cream cakes, holiday pies y pints, hot '
              'chocolate y catering')),
    (3, ('a', 'Mercado: demanda US (IDFA: julio = mes de más producción; National Ice Cream Month / Day, Presidential '
              'Proclamation 5219, 1984; DataForSEO US de research §2: «ice cream shop business plan» 320/mes, «homemade '
              'ice cream shop» 2,400/mes con pico en verano); estacionalidad del plan (Mes 1 = marzo, pico en julio); '
              'riesgos (verano frío y lluvioso, guerra de precios, helado del súper); sin datos sin fuente: las cifras '
              'MAPA y DataForSEO España NO cruzan')),
    (4, ('a', 'Competencia: el mapa (helado del súper, franquicias como Häagen-Dazs o Bruster\'s solo como «franchise» '
              'sin cifras salvo research §1, otros scoop shops, gelato como estilo, soft serve / froyo, cafés); Porter; '
              'barreras = licencia (D190, «depends on your state») + caja; DAFO con margen bruto {{margen_bruto_pct}}; '
              'las barreras ES (IAE 644.4, Ley 12/2012, 750 m²) NO cruzan')),
    (5, ('a', 'Marketing: por estaciones (Opening Day en marzo, peak season Memorial Day → Labor Day, National Ice Cream '
              'Day = 3rd Sunday of July), sabor del día en redes, Google Business Profile, samples con tasting spoons, '
              'colegios y vecindario; pints por DoorDash / Uber Eats ({{delivery_pct}} de las ventas a una comisión de '
              '{{comision_pct}}); presupuesto {{marketing_anual}} al año; reclamos honestos («made here in small '
              'batches»; «homemade» solo si es verdad)')),
    (6, ('b', 'Operaciones (D190, proceso con BASE COMPRADA): recibir la base a 41 °F o menos (lot codes) → aromatizar e '
              'incluir mix-ins → batch-freeze (draw a 16-19 °F) → endurecer a 0 °F o menos → dipping cabinet a 6-10 °F; '
              'dipper well de agua corriente (Food Code 3-304.12); {{produccion_horas}} h de producción al día antes de '
              'abrir; equipo con tokens ({{inv_batch_freezer}}, {{inv_hardening}}, {{inv_dipping}}, {{inv_congeladores}}, '
              '{{inv_base_frio}}); horario por temporada; sin pasteurizador en el caso')),
    (7, ('b', 'Organización y personal: Owner / ice cream maker & GM, shift lead / counter todo el año, seasonal scooper '
              '(abril-septiembre), summer scooper (junio-agosto), production assistant (mayo-septiembre), relief cover '
              '({{plantilla_puestos}} personas = {{plantilla_jornadas}} FTE); ≥ $15/h, sin propinas modeladas; employer '
              'payroll taxes {{cargas_pct}}; coste {{personal_a1}} ({{personal_pct}}); seasonal part-time W-2 '
              'recontratados cada primavera; scoopers de 14-15 años solo con el horario FLSA (29 CFR 570.35); el dueño '
              'cobra por debajo de un gerente: «draw in addition from net profit»; CFPM + food handler cards')),
    (8, ('b', 'Plan financiero: TODO con tokens (inversión, ventas años 1-3, mezcla {{comida_pct}}/{{bebida_pct}}, COGS '
              '{{cogs_pct}}, personal {{personal_pct}}, prime cost {{prime_cost_pct}}, alquiler {{ocupacion_pct}}, EBITDA, '
              'neto, equilibrio {{equilibrio_clientes_dia}} / {{equilibrio_caja_clientes_dia}} customers/día, holgura '
              '{{holgura_caja_pct}}, DSCR {{dscr_min}}, saldo mínimo {{saldo_minimo}} en el Mes {{mes_saldo_minimo}}, '
              'escenarios); Mes 1 = marzo; el neto real ≈ 5-6 % frente al «10-25 %» de la SERP: el Word dice la verdad')),
    (9, ('b', 'Marco legal US (ver las notas propias de cada ranura de §9)')),
    (10, ('b', 'Conclusiones y hoja de ruta: viable pero exigente; riesgos (abrir en otoño, la caja del invierno, el '
               'local equivocado: 30 kW / 3-phase, ventilación de condensadores, desagües; el clima: escenario '
               'pesimista; la licencia: decidir base comprada o mezcla propia ANTES de firmar); errores (reclamos, '
               'contratar tarde la temporada, no escandallar); el orden del checklist (80 tareas en 6 fases: business '
               'setup, site & permits, production & health, staff & food safety, brand & menu, opening & season); '
               'cierre con el Excel y el checklist')),
])
_RANURAS = OrderedDict([(1, range(39, 44)), (2, range(46, 51)), (3, range(53, 59)), (4, range(61, 67)),
                        (5, range(69, 76)), (6, range(78, 83)), (7, range(85, 91)), (8, range(93, 100)),
                        (9, range(102, 109)), (10, range(111, 118))])
# Notas de ranura (D200): las que SUSTITUYEN un bloque ES que no cruza o fijan el caso
_NR = OrderedDict([
    (47, '§2 2/5 (D190, D200): la propuesta con BASE COMPRADA: helado mantecado cada día en el local con la base de una '
         'central láctea con licencia, a la vista desde el mostrador; tras la pasteurización de la central solo se '
         'añaden aromas e inclusiones (no raw eggs, no raw milk or cream; los sabores custard piden una custard base); '
         '«frozen custard» solo si la receta cumple 21 CFR 135.110 (1.4 % egg yolk solids). Nada de «pasteurizar a '
         '85 °C»'),
    (50, '§2 5/5 (D200): el invierno SIN crepes ni salida de humos (no cruzan): ice cream cakes por encargo, holiday '
         'pies y pints de fiestas, hot chocolate, catering; cierre de 3 semanas en enero y lunes de noviembre a febrero'),
    (53, '§3 1/6 (D200): demanda US: IDFA (julio = mes de más producción) y National Ice Cream Month / Day (Proclamation '
         '5219, 1984); sin cifras de consumo de hogares (MAPA no cruza y no hay dato US leído equivalente)'),
    (54, '§3 2/6 (D200): estacionalidad US: verano hasta +40 % e invierno ≈ −30 % (7shifts, resumen: dilo como '
         '«industry estimates»); peak season Memorial Day → Labor Day; sin cifras de consumo fuera del hogar'),
    (55, '§3 3/6 (D200): búsquedas US (DataForSEO US, oct 2026, research §2): «ice cream shop business plan» 320/mes, '
         '«opening an ice cream shop» 320, «homemade ice cream shop» 2,400 con pico en verano, «ice cream shop '
         'equipment» 1,000; el comprador busca plan, coste y licencia'),
    (56, '§3 4/6 (D200): el reparto del plan con Mes 1 = marzo y el pico en julio (la Tesorería del Excel); sin el '
         '«81,6 %» del MAPA; describe el método y remite a la hoja «12-Month Cash Flow»'),
    (64, '§4 4/6 (D200): barreras de entrada US: la decisión de licencia (D190: base comprada = retail food establishment '
         'en la mayoría de estados; mezcla propia = licencia estatal de dairy / frozen dessert manufacturer + equipo '
         '3-A) y la caja; NO cruzan IAE 644.4/676, Ley 12/2012, declaración responsable ni 750 m²'),
    (73, '§5 5/7 (D200): encargos: ice cream cakes de cumpleaños todo el año, graduations en mayo-junio, Fourth of July, '
         'holiday pies y cakes en noviembre-diciembre (con señal / depósito); nada de comuniones ni turrón'),
    (78, '§6 1/5 (D190, D200): el día de producción con BASE COMPRADA, por orden de seguridad: recibir la base a 41 °F o '
         'menos y anotar el lot code → aromatizar e incluir (solo aromas e inclusiones tras la pasteurización de la '
         'central) → batch-freeze → endurecer a 0 °F o menos → dipping cabinet a 6-10 °F; date marking (3-501.17). '
         'Nada de pasteurizar, madurar a 4 °C ni «85 °C»'),
    (79, '§6 2/5 (D200): el equipo con los importes del caso SOLO por token: batch freezer {{inv_batch_freezer}} (un '
         'Carpigiani de 20 qt ronda $40,800 de lista: pide dos presupuestos; reacondicionados, menos), hardening '
         'cabinet {{inv_hardening}}, storage freezers {{inv_congeladores}}, dipping cabinets {{inv_dipping}}, nevera '
         'de base y preparación {{inv_base_frio}}, mostrador con dipper wells y waffle cone irons {{inv_mostrador}}'),
    (80, '§6 3/5 (D200): capacidad SIN cifra de producción (no hay token de galones: la frase va sin cifra): el batch '
         'freezer de 20 qt cubre el verano con {{produccion_horas}} h al día antes de abrir y algún turno extra en '
         'julio; el pico lo marca la Tesorería'),
    (82, '§6 5/5: contacto cruzado (una spade por tub, dipper well de agua corriente 3-304.12(D)); dipping cabinet a '
         '6-10 °F según el fabricante; almacén a 0 °F o menos; frío ≤ 41 °F; ninguna promesa «allergen-free»'),
    (87, '§7 3/6 (D200): la temporada = seasonal part-time W-2 recontratados cada primavera (sin figura de «fijo '
         'discontinuo»); unemployment insurance estatal; nada de art. 16 ET'),
    (88, '§7 4/6 (D200): salario mínimo federal $7.25/h + el de tu estado o ciudad (el caso presupuesta ≥ $15/h); '
         'jóvenes de 14-15 años con horario FLSA (29 CFR 570.35: hasta las 9 pm del 1 de junio al Labor Day); '
         'registro de horas; nada de convenio ni ALEH'),
    (99, '§8 7/7 (D200): DOS alternativas razonadas sin Excel: (1) la VARIANTE «make your own mix» (batch pasteurizer ≈ '
         '$25,000-45,000, «get quotes», licencia estatal de dairy plant / frozen dessert manufacturer, equipo 3-A, '
         'inspecciones; en la variante, grasas, yemas y emulsionantes ANTES de pasteurizar, 155 °F 30 min / 175 °F 25 s '
         'Ohio 901:11-3-05); (2) cerrar de noviembre a febrero (menos personal y suministros, pero el alquiler sigue)'),
    (113, '§10 3/7 (D200): el local equivocado: sin 3-phase / unos 30 kW («ask the utility about 3-phase service and '
          'amps before signing»), sin ventilación para los condensadores ni floor sinks; nada de salida de humos ni '
          'crepes'),
    (115, '§10 5/7: errores frecuentes: «homemade» o «small-batch» sin hacerlo en el local; «ice cream» o «frozen '
          'custard» sin cumplir 21 CFR 135.110; contratar tarde la temporada; firmar el local antes de decidir la '
          'licencia (D190)'),
])
_N9 = OrderedDict([
    (102, '§9 1/7 (D200): el marco US por niveles (federal, estatal, condado, ciudad); LLC (o S corp con tu CPA) + EIN; '
          'business license; sales tax permit ({{sales_tax}} de ejemplo, un solo tipo); registro estatal de payroll y '
          'unemployment'),
    (103, '§9 2/7 (D200): zoning check ANTES de firmar (retail food con producción en el local); plan review (Food Code '
          '8-201.11) con el layout del equipo + building permit → certificate of occupancy; sidewalk café / patio '
          'permit; signage permit; electrical inspection'),
    (104, '§9 3/7 (D190, D200): health permit + inspección; LA DECISIÓN DE LICENCIA: comprar la base pasteurizada a una '
          'central con licencia te mantiene como retail food establishment en la mayoría de estados; hacer tu mezcla '
          'suele añadir licencia estatal de dairy / frozen dessert manufacturer, equipo 3-A e inspecciones. Ejemplos '
          'LEÍDOS: Vermont (Agency of Agriculture: base pasteurizada → solo Frozen Dessert License, y tras la '
          'pasteurización solo aromas; mezclar tú → Milk Handler License) y Georgia (GAC 40-2-8-.01(3): el minorista '
          'que congela mezcla de una central con licencia no necesita Dairy Manufacturer\'s License); Arizona, '
          'Massachusetts y Pennsylvania lo tratan distinto («check»). «Ask your state department of agriculture in '
          'writing before you sign the lease». NUNCA «no license needed» ni una tarifa'),
    (105, '§9 4/7 (D200): Food Code: CFPM (2-102.12) + food handler cards según estado; dipper well de agua corriente '
          '(3-304.12); frío ≤ 41 °F, almacén a 0 °F, date marking (3-501.17), etiqueta de lo envasado en el local '
          '(3-602.11); sin huevo crudo en el caso (base comprada); nada de APPCC ni 70 °C'),
    (106, '§9 5/7 (D200): nombres: «ice cream» = ≥ 10 % milkfat y ≥ 4.5 lb per gallon; «frozen custard» = 1.4 % egg '
          'yolk solids (21 CFR 135.110); «gelato» no aparece en 135.110: si lo llamas ice cream, aplica el estándar '
          'federal (no afirmes que no hay estándar); reclamos honestos: «made here in small batches», «homemade» / '
          '«house-made» solo si es verdad; nada de RD 618 ni «artesano»'),
    (107, '§9 6/7 (D200): alérgenos: 9 mayores US con el sésamo (FASTER Act, 2023); scoops y dipper wells compartidos: '
          'ninguna promesa «allergen-free»; sales tax: el scoop para tomar es prepared food; el pint envasado y la '
          'tarta entera pueden ir como alimento exento en algunos estados (Texas Comptroller, ejemplo): «use your '
          'blended rate, check your state»'),
    (108, '§9 7/7 (D200): personal y riesgos: FLSA y jóvenes de 14-15 años (29 CFR 570.35), seasonal W-2, salario '
          'mínimo estatal; seguro con equipment breakdown + food spoilage; ASCAP/BMI/SESAC; refrigerante solo por un '
          'técnico EPA 608; y, como ÚLTIMA frase o frases, la NOTA UK: registro del food business en el council 28 '
          'días antes, FHRS 0-5 (FHIS en Escocia), VAT 20 % en lo que se toma en el local y en lo caliente (el helado '
          'para llevar suele ir a tipo cero: «check HMRC»), 14 alérgenos'),
])


def _notas_docx():
    out = OrderedDict()
    for s, filas in _RANURAS.items():
        tanda, nota = _SEC[s]
        for k, i in enumerate(filas, 1):
            n = _N9.get(i) or _NR.get(i) or ('§%d %d/%d: %s' % (s, k, len(filas), nota))
            out[i] = n + ' ‖ ' + _FORMA % (s, tanda)
    return out


DOCX_NOTAS = OrderedDict([('ice', _notas_docx())])

# ==========================================================================
# Pistas por celda (extraer_textos.py → textos_es.json → tandas)
# ==========================================================================
_CASO = ('D191: caso US = 165 customers/día (cada persona que compra: mostrador, patio y para llevar) × $7.50 por persona '
         '(sin sales tax) × 310 días; Mes 1 = marzo; sin alcohol; sin cifras del ES ni historia de versiones')
CELDA_PISTAS = OrderedDict([
    (('HELP', _S, 'C4'), _CASO + '; media del año con la apertura incluida (la Tesorería reparte la estacionalidad): un '
                                 'sábado de julio puede pasar de 400 y un martes de enero quedarse en 40 (Kit '
                                 'estimate); compáralo con el paso de gente de tu calle'),
    (('HELP', _S, 'C5'), _CASO + '; $7.50 por persona = 70 % doble en cup/cone ($7.00-8.25) + 15 % single/kid '
                                 '($4.25-5.25) + 10 % pint/quart repartido entre 2 personas + 5 % sundae/café (carta '
                                 'Kit estimate research §5.1); es por PERSONA, no por tique de caja; el precio con '
                                 'impuesto lo calcula la fila de abajo'),
    (('HELP', _S, 'C6'), _CASO + '; 310 días = cierra 3 semanas en enero (mantenimiento y vacaciones), Thanksgiving, '
                                 'Christmas y los lunes de noviembre a febrero'),
    (('HELP', _S, 'C7'), 'D191: +8 % el año 2 (clientela que repite el segundo verano, más ice cream cakes por encargo y '
                         'catering); sin cifras del ES'),
    (('HELP', _S, 'C13'), 'D191: food cost 22 % de las ventas de helado = base comprada + aromas e inclusiones, conos, '
                          'samples (tasting spoons) y merma (research §8); escandalla cada sabor cada temporada; sin '
                          'impuestos de compra (en EE. UU. no hay crédito)'),
    (('HELP', _S, 'C14'), 'D191: beverage cost 25 % (espresso, hot chocolate, shakes, sodas, agua); sin alcohol'),
    (('HELP', _S, 'C15'), 'D191: disposables 4.5 % (cups, spoons, napkins, pint/quart containers, cake boxes)'),
    (('HELP', _S, 'C16'), 'D191: 4 % de las ventas por DoorDash / Uber Eats: pints y quarts hand-packed en noches de '
                          'verano (el pint viaja bien; el scoop no); el pickup directo no paga comisión'),
    (('HELP', _S, 'C17'), 'D191: 25 % = plan medio de DoorDash / Uber Eats (Basic 15 %, Premier 30 %, research PIZ '
                          '§5.3); si repartes tú, pon 0; compruébalo en tu contrato'),
    (('HELP', _S, 'C24'), 'D191: $2,500/mes = ~1,000 sq ft × ~$30/sq ft/año (Kit estimate; media US pedida $24.69 + '
                          'NNN, TenantBase, resumen); calle comercial de barrio o junto a un parque o colegios, segunda '
                          'generación de retail; el peso sobre ventas lo calcula el P&L'),
    (('HELP', _S, 'C26'), 'D191: $1,300/mes (cabinets 24 h, batch freezer, hardening, AC: unos 30 kW contratados); el '
                          'verano dispara la luz'),
    (('HELP', _S, 'C27'), 'D191: $4,500/año = general liability + property + equipment breakdown con food spoilage + '
                          'workers\' comp'),
    (('HELP', _S, 'C25'), 'D191: 2 meses de fianza (forma: Pizza EN C25, «commercial leases commonly ask for one to '
                          'three… check it with your attorney»)'),
    (('HELP', _S, 'C27'), 'D191: sin el «300.000 €» del ES: general liability (límite habitual por siniestro, «ask '
                          'your broker») + equipment breakdown con food spoilage, que es el riesgo de una heladería'),
    (('HELP', _S, 'C32'), 'D191: SBA 7(a) al 10 % a 10 años (Prime + margen según tramo: «ask two lenders»); sin ICO'),
    (('HELP', _S, 'C34'), 'D191: B34 = 0 (SBA 7(a) amortiza desde el inicio; forma: Pizza EN C34); el ES pone un año '
                          'de carencia: aquí no'),
    (('HELP', _S, 'C35'), 'D191: 3 meses de costes fijos de caja: el colchón del primer invierno (noviembre-febrero)'),
    (('HELP', _S, 'C51'), 'D189: 20 plazas dentro; el patio de 5 mesas (en temporada) no cuenta en el aforo'),
    (('HELP', _S, 'C58'), 'D191: 2 días = media ponderada: el mostrador cobra al momento (tarjeta) y el catering a '
                          'unos días; sin «restaurantes»'),
    (('HELP', _S, 'C60'), 'D198: con 12 pagas no hay extras: solo cuenta si tecleas más de 12; «July is Month 5, because '
                          'Month 1 of the plan is March» (forma: Pizza EN C60)'),
    (('HELP', _S, 'C61'), 'D198: con 12 pagas no hay extras: solo cuenta si tecleas más de 12; «December is Month 10, '
                          'because Month 1 of the plan is March» (forma: Pizza EN C61)'),
    (('HELP', _S, 'C68'), 'D191: B68 vacío = state / local minimum wage anual (hourly × 2,080) si supera el federal '
                          '$7.25; sin convenio (forma: Pizza EN C68)'),
    (('HELP', _N, 'A8'), 'SPEC §4.1 línea 4 (Bar/PIZ): sin divisores 1,10/1,21 → «divide a menu price by 1 + your sales '
                         'tax rate»; P&L excl. sales tax, cash flow incl.; un solo tipo en el ejemplo (B39 = B40 = 8 %); '
                         'el pint envasado y la tarta entera pueden ir exentos en algunos estados (D195)'),
    (('HELP', _N, 'A10'), 'D195: Mes 1 = MARZO (abre en temporada para que el primer verano pague el primer invierno)'),
    (('HELP', _N, 'A12'), 'El Word del kit usa las cifras de este Excel: si cambias una celda verde, manda el Excel'),
    (('HELP', _P, 'F10'), 'D194: reparto del helado (Kit): scoops, cups/cones y sundaes en el local ≈ 65 %, pints y '
                          'quarts to go ≈ 15 %, ice cream cakes y holiday pies ≈ 10 %, catering ≈ 5 %, delivery '
                          'marketplaces 4 % (ver B16); un solo sales tax en el ejemplo; el pint envasado puede ir exento '
                          'en algunos estados'),
    (('HELP', _P, 'F11'), 'D194: espresso, hot chocolate, shakes, sodas y agua; sin alcohol'),
    (('HELP', _P, 'F26'), 'D194: accounting & bookkeeping, sales tax returns y payroll (incl. los seasonal W-2)'),
    (('HELP', _P, 'F31'), 'D194: sidewalk café / patio permit de 5 mesas en temporada; la tasa la pone tu ciudad'),
    (('HELP', _P, 'F35'), 'D194: CFPM, food handler cards, alérgenos y OSHA basics (frío, resbalones, cortes); sin Ley '
                          '31/1995'),
    (('HELP', _P, 'F53'), 'D196: techo del food cost sobre ventas (25 %); la base comprada lo sube frente a hacer tu '
                          'mezcla; Kit estimate'),
    (('HELP', _P, 'F54'), 'D196: techo del personal (35 %): la temporada obliga a reforzar el mostrador; Kit estimate'),
    (('HELP', _R, 'J5'), 'D194: owner / ice cream maker & GM: recetas, sabores, batch freezing, compras y gestión; NO '
                         'pasteuriza (base comprada); cobra por debajo de un gerente: «draw in addition from net '
                         'profit»; sin «administrador / autónomo»'),
    (('HELP', _R, 'J6'), 'D194: shift lead todo el año (≈ $17/h): mostrador, caja, dipping cabinets y cierre'),
    (('HELP', _R, 'J7'), 'D194: seasonal part-time W-2 (≈ 40 h/semana de abril a septiembre = 0.5 FTE en el año), '
                         'recontratado cada primavera; scoopers de 14-15 años solo con el horario FLSA (29 CFR 570.35)'),
    (('HELP', _R, 'J8'), 'D194: seasonal part-time W-2 de junio a agosto (tardes y noches del pico); nunca 1099 si '
                         'pones tú el horario (misclassification)'),
    (('HELP', _R, 'J9'), 'D194: production assistant de mayo a septiembre (batch freezing, pack-out, limpieza del '
                         'batch freezer y de los tubs); sin pasteurizador'),
    (('HELP', _R, 'J20'), 'D194: horas de la tienda por temporada (más en peak season, Memorial Day → Labor Day; menos '
                          'de noviembre a febrero); 9.5 h de media'),
    (('HELP', _R, 'J22'), 'D194: 2.0 h al día antes de abrir: aromatizar, batch-freeze y endurecer (SIN pasteurizar ni '
                          'madurar: la base viene pasteurizada); más en julio, menos en invierno'),
    (('HELP', _T, 'O13'), 'D194: 12 pagas (sin extras); el personal se reparte en 12 meses pero los seasonal solo cobran '
                          'en temporada: invierno más caro que la realidad (prudente)'),
])
for _f, _nota in [(7, 'D193: architect, MEP drawings, plan review (Food Code 8-201.11) y permit fees'),
                  (8, 'D193: build-out de un local de segunda generación de retail, ~1,000 sq ft con sala de '
                      'producción ~250 sq ft'),
                  (9, 'D193: unos 30 kW; «ask the utility about 3-phase service and amps before signing»'),
                  (10, 'D193: floor sinks, hand sinks, HVAC y ventilación para los condensadores'),
                  (13, 'D193: «a 20-qt Carpigiani lists at about $40,800; get two quotes; reconditioned units cost '
                       'less» (WebstaurantStore, resumen); Emery Thompson / Taylor: solo presupuesto'),
                  (14, 'D193: hardening cabinet / blast freezer ($10,000-30,000 según research §4, fuente débil: '
                       '«Kit estimate»)'),
                  (15, 'D193: storage freezers a 0 °F o menos'),
                  (17, 'D193: dipping cabinets: 12 sabores desde ≈ $1,700-2,500 (económicos) hasta ≈ $12,300 gama alta '
                       '(research §4, resumen); 18 sabores en verano, 10-12 en invierno; 6-10 °F según el fabricante'),
                  (18, 'D193: dipper wells de agua corriente (3-304.12), espresso, waffle cone irons y hot fudge '
                       'warmers; SIN crepera ni salida de humos'),
                  (20, 'D193: POS que reporta el sales tax (sin Veri*factu)'),
                  (22, 'D193: curso de ice cream making (p. ej. un short course universitario): «Kit estimate»'),
                  (24, 'D193: LLC, legal, permits y food safety plan; no se amortiza (E = «No»)'),
                  (25, 'D193: base, aromas, conos, cups y pint containers')]:
    CELDA_PISTAS[('HELP', _I, 'D%d' % _f)] = _nota
for _f in range(7, 26):
    if _f == 12:
        continue                                          # D12 es POR_CELDA (la nota de la variante, D193)
    CELDA_PISTAS.setdefault(('HELP', _I, 'D%d' % _f), 'D193: nota de la partida del ejemplo US (rótulo fijado de la col. '
                                                       'A en "fijos_en"); sin marcas ni normas españolas: solo rangos '
                                                       'con fuente de research §4 o ninguno')
# Tabla D19 (Instrucciones 35-47): «US ICE CREAM SHOP BENCHMARKS (sourced) AND KIT ESTIMATES» (Benchmark | Value | Source |
# Note). D196: 13 filas en el orden de las del ES; solo lo «[leída]» con fuente; lo «(resumen)» con «check» o como Kit
# estimate
_D19 = OrderedDict([
    (35, 'D196 fila → «Month 1 of the plan» · «March» · «Plan decision» · nota: abre en temporada; el primer verano paga '
         'el primer invierno'),
    (36, 'D196 fila (sustituye el consumo MAPA) → «Peak season» · «Memorial Day → Labor Day; July = National Ice Cream '
         'Month» · «Presidential Proclamation 5219 (1984); IDFA» · nota: julio es el mes de más producción; National Ice '
         'Cream Day = 3rd Sunday of July'),
    (37, 'D196 fila → «Ice cream cost (food cost)» · «about 22% of ice cream sales» · «Kit estimate» · nota: base '
         'comprada + aromas e inclusiones + conos + samples + merma; sustituye por las facturas de tu central y tu '
         'distribuidor'),
    (38, 'D196 fila → «Menu prices» · «single $5.25 · double $7.00 · pint $11 · quart $18 · 8-in cake $45» · «Kit '
         'estimate (Oct 2026), excl. sales tax» · nota: no hay una media US fiable del precio de la bola: usa los de tu '
         'zona'),
    (39, 'D196 fila (sustituye 430 g/l) → «"Ice cream" standard» · «≥ 10% milkfat and ≥ 4.5 lb per gallon; frozen '
         'custard: 1.4% egg yolk solids» · «21 CFR 135.110 (eCFR)» · nota: si lo llamas ice cream, aplica el estándar'),
    (40, 'D196 fila (sustituye −18 °C) → «Storage and serving temperature» · «0 °F (−18 °C) or colder in storage and '
         'hardening; dipping cabinet 6-10 °F» · «FDA Food Code + equipment manufacturer» · nota: cold holding de la '
         'base ≤ 41 °F'),
    (41, 'D196 fila (sustituye «huevo en la mezcla») → «Buy a base or make your own mix» · «buying pasteurized base: '
         'retail license in most states; own mix: state dairy / frozen dessert manufacturer license» · «Vermont Agency '
         'of Agriculture; Georgia Rules 40-2-8» · nota: «depends on your state: ask your state department of '
         'agriculture»; nunca «no license needed»'),
    (42, 'D196 fila → «Labor cost / sales» · «28-35%» · «Kit estimate» · nota: el dueño en nómina y la temporada lo '
         'llevan a la parte alta'),
    (43, 'D196 fila → «Rent / sales» · «≤ 10%» · «Kit estimate» · nota: el umbral del semáforo del P&L'),
    (44, 'D196 fila → «Production waste» · «5-8%» · «Kit estimate» · nota: sabores que no rotan, tubs abiertos, '
         'pruebas'),
    (45, 'D196 fila → «Electrical service» · «about 30 kW» · «Kit estimate» · nota: «ask the utility about 3-phase '
         'service and amps before signing»'),
    (46, 'D196 fila (sustituye «IVA del helado») → «Sales tax» · «scoops taxed as prepared food; packaged pints and '
         'whole cakes may be exempt as groceries» · «Texas Comptroller (example)» · nota: «check your state»; el libro '
         'usa un solo tipo de ejemplo (8 %)'),
    (47, 'D196 fila (sustituye «convenio») → «Minimum wage» · «federal $7.25/h + your state; teens 14-15: limited '
         'hours» · «U.S. Department of Labor (29 CFR 570.35)» · nota: este plan presupuesta ≥ $15/h; teclea el suelo '
         'de tu estado en "0. Assumptions"'),
])
for _f, _p in _D19.items():
    for _col in 'ABCD':
        CELDA_PISTAS[('HELP', _N, '%s%d' % (_col, _f))] = _p

# Pistas por TEXTO propias de la heladería (se suman a las de extraer_textos.PISTAS): D190, D199 + research §9
PISTAS_EXTRA = [
    (r'\b[Cc]lientes?\b', 'D191/§0: el volumen es «customers» (cada persona que compra); nunca «covers» ni '
                          '«transactions»'),
    (r'[Pp]asteuri|[Mm]ezcla|[Yy]ema|[Hh]uevo|85 ?°|[Mm]adur', 'D190: el caso COMPRA la base pasteurizada a una '
     'central con licencia: tras su pasteurización solo se añaden aromas e inclusiones (no raw eggs, no raw milk or '
     'cream; custard flavors need a custard base); pasteurizar tu mezcla = VARIANTE con licencia estatal (sin Excel)'),
    (r'[Mm]antec(?!ado)', 'Glosario: mantecadora → batch freezer · mantecar → batch-freeze / churn · extracción → draw'),
    (r'[Mm]antecado|[Hh]elado crema|[Ss]orbete|[Gg]ranizado|RD 618|430', 'research §6.2: nombres de 21 CFR 135.110 '
     '(«ice cream» ≥ 10 % milkfat y ≥ 4.5 lb/gal; «frozen custard» 1.4 % egg yolk solids); nada de RD 618'),
    (r'[Aa]batid|[Aa]batir', 'Glosario: abatidor → hardening cabinet / blast freezer · abatir → harden'),
    (r'[Vv]itrina|[Cc]ubeta', 'Glosario: vitrina → dipping cabinet · cubeta → tub (3 gal)'),
    (r'[Ll]avaporcionador|[Ee]sp[aá]tula', 'Glosario: dipper well (agua corriente, Food Code 3-304.12) · scoop · spade'),
    (r'[Tt]arrina', 'Glosario: tarrina para llevar → pint / quart (hand-packed) · envasar → pack-out'),
    (r'[Cc]ucurucho|[Bb]arquillo', 'Glosario: cone (waffle cone, sugar cone, cake cone) · waffle cone iron'),
    (r'\b[Cc]opas?\b', 'Glosario: copa → sundae · cup'),
    (r'[Tt]arta', 'Glosario: tarta helada → ice cream cake'),
    (r'[Aa]rtesan|[Ee]laboraci[oó]n propia', 'research §6.2: «made here in small batches»; «homemade» / «house-made» solo '
                                              'si es verdad (sin norma federal leída)'),
    (r'[Ff]ijo discontinuo|[Tt]emporada', 'D194: seasonal part-time W-2 recontratado cada primavera; scoopers de 14-15 '
                                          'años solo con horario FLSA (29 CFR 570.35); peak season Memorial Day → Labor '
                                          'Day'),
    (r'[Cc]repe|[Gg]ofre|[Hh]umos', 'D200: sin crepes ni salida de humos (no cruzan); waffle cone irons; el invierno = '
                                    'ice cream cakes, holiday pies y pints, hot chocolate y catering'),
    (r'[Tt]urr[oó]n|[Nn]avidad|[Cc]omuni[oó]n', 'research §9 (e): turrón helado → holiday pies and cakes · comuniones → '
                                                'birthdays and graduations'),
    (r'\bSL\b|aut[oó]nomo|IAE|Seguridad Social|alta en', 'D199: «LLC vs S corp with your CPA» · «EIN + state payroll / '
                                                         'unemployment registration»'),
    (r'Veri\*?factu|TPV', 'D199: «POS that reports sales tax» (sin Veri*factu)'),
    (r'[Uu]rbanism|[Ll]icencia de (?:actividad|apertura|obra)|[Dd]eclaraci[oó]n responsable|compatibilidad',
     'D199: «zoning check before signing» · «building permit + certificate of occupancy» · business license + sales tax '
     'permit'),
    (r'[Tt]erraza', 'D199: patio / sidewalk café permit (la tasa la pone tu ciudad)'),
    (r'[Rr]egistro sanitario|RGSEAA|APPCC|autocontrol', 'D199: plan review (Food Code 8-201.11) con el layout del equipo '
     '+ health permit + inspection; la decisión de licencia de D190 es una tarea propia («ask your state department of '
     'agriculture in writing»)'),
    (r'[Ff]rigorist|[Ff]r[ií]o|R290|gas', 'D194: refrigeration service contract con un técnico EPA 608 (el personal '
                                          'nunca recarga refrigerante)'),
    (r'PRL|[Pp]revenci[oó]n de riesgos|EPI', 'D199: OSHA basics (frío, resbalones, cortes)'),
    (r'[Mm]anipulador|[Ff]ormaci[oó]n', 'D199: Certified Food Protection Manager (2-102.12) + food handler cards (según '
                                        'estado)'),
    (r'[Aa]l[eé]rgen', 'D199: 9 major allergens incl. sesame (UK 14); ninguna promesa «allergen-free» (scoops y dipper '
                       'wells compartidos)'),
    (r'[Pp]lataforma|Glovo|Just Eat|Uber|delivery', 'D191: DoorDash / Uber Eats para pints y quarts'),
    (r'SGAE|AGEDI', 'D194: «Music licensing (ASCAP/BMI/SESAC)»'),
    (r'−18|-18 ?°|[Tt]emperatura', 'Unidades: 0 °F (−18 °C) o menos en almacén; dipping cabinet 6-10 °F; frío ≤ 41 °F '
                                   '(5 °C): °F principal y °C entre paréntesis'),
    (r'[Cc]onvenio|[Nn][oó]mina|[Cc]ontrato', 'D199: offer letters, I-9, W-4, state new-hire reporting, minimum wage '
                                              'posters (sin convenio)'),
    (r'[Tt]rif[aá]sic|kW|[Pp]otencia', 'D199: «ask the utility about 3-phase service and amps before signing»'),
    (r'm²|metros', 'Unidades: sq ft con los m² entre paréntesis («1,000 sq ft (93 sq m)»)'),
    (r'—', 'D199: la lista de la DV EN es «✓,☐,N/A»: ☐ = pendiente; el texto EN nunca dice «—»'),
]

# Glosario de la heladería (research §9, OBLIGATORIO; manda sobre el de FT/CAF)
GLOSARIO_ICE = OrderedDict([
    ('heladería artesanal', 'ice cream shop (nombre, H1, ficheros) · ice cream parlor · scoop shop · creamery (prosa)'),
    ('mantecadora · mantecar', 'batch freezer · batch-freeze / churn; extracción = draw (16-19 °F)'),
    ('mezcla base', 'ice cream base / mix · butterfat · «14% base»'),
    ('pasteurizador (variante)', 'batch pasteurizer · vat pasteurization (155 °F 30 min) · HTST'),
    ('maduración', 'aging the mix (36-39 °F)'), ('abatidor · abatir', 'hardening cabinet / blast freezer · harden'),
    ('vitrina de cubetas · cubeta', 'dipping cabinet (gelato: gelato case) · tub (3 gal) / pan (gelato)'),
    ('lavaporcionador', 'dipper well (running water, Food Code 3-304.12(D))'),
    ('porcionador · espátula', 'scoop (dipper) · spade'), ('rendimiento de aire', 'overrun'),
    ('tarrina para llevar', 'pint · quart · hand-packed · pack-out'),
    ('cucurucho · barquillo', 'cone (waffle cone, sugar cone, cake cone) · waffle cone iron / maker'),
    ('copa', 'sundae · cup'), ('inclusiones · variegato · virutas', 'mix-ins · swirl / ripple · sprinkles'),
    ('mantecado (≥ 4 % yema)', 'frozen custard (1.4% egg yolk solids, 21 CFR 135.110)'),
    ('tarta helada', 'ice cream cake'), ('sabor de prueba', 'sample (tasting spoon)'),
    ('dependiente/a', 'scooper / counter staff · shift lead'), ('maestro heladero', 'ice cream maker (owner/operator)'),
    ('fijo discontinuo de temporada', 'seasonal part-time (W-2)'),
    ('temporada alta · reapertura', 'peak season (Memorial Day → Labor Day) · Opening Day · off-season'),
    ('licencia de obrador', 'frozen dessert license / dairy plant or milk handler license (state) + health permit (local)'),
    ('elaboración propia / artesano', 'made here in small batches · homemade / house-made (only if true)'),
    ('seguro de mercancía por avería', 'equipment breakdown with food spoilage'),
    ('ticket medio', 'average check per person (excl. sales tax)'), ('IVA · terraza', 'sales tax · patio / sidewalk café'),
    ('helado crema / mantecado / sorbete (RD 618)', 'ice cream, frozen custard (21 CFR 135); sorbet sin estándar leído'),
    ('644.4/676, declaración responsable', 'business license + zoning + building permit / CO'),
    ('registro sanitario autonómico / RGSEAA', 'health permit + plan review / state frozen dessert license'),
    ('fijo discontinuo, convenio, SMI', 'seasonal W-2, state / local minimum wage'),
    ('−18 °C', '0 °F'), ('430 g/l', '4.5 lb per gallon'), ('autónomo / SL', 'LLC'),
    ('manipulador', 'food handler card + CFPM'),
    ('crepera / gofrera con salida de humos', 'waffle cone irons (sin humos; las crepes no cruzan)'),
    ('turrón helado de Navidad', 'holiday pies and cakes'), ('comuniones', 'birthdays and graduations'),
    ('cliente (volumen)', 'customer (cada persona que compra)'),
])


# ==========================================================================
# Caso de ejemplo US (D191, D193, D194, D196; research §8): celdas VERDES. (corto, hoja ES, celda) → (valor, rótulo)
# ==========================================================================
def valores_ice(M):
    v = OrderedDict()
    sup = [
        ('B4', 165, 'Clientes/día'), ('B5', 7.5, 'Ticket medio'), ('B6', 310, 'Días de apertura'),
        ('B7', 0.08, 'Crecimiento de volumen del año 2'), ('B8', 0.05, 'Crecimiento de volumen del año 3'),
        ('B11', 0.90, 'Ventas de COMIDA'), ('B13', 0.22, 'Coste de mercancía sobre las ventas de COMIDA'),
        ('B14', 0.25, 'Coste de mercancía sobre las ventas de BEBIDA'), ('B15', 0.045, 'Consumibles'),
        ('B16', 0.04, 'Ventas por delivery'), ('B17', 0.25, 'Comisión de la plataforma'),
        ('B18', 0.03, 'Comisión de los medios de pago'), ('B20', 0.10, 'Seguridad Social'),
        ('B21', 12, 'Número de pagas'), ('B22', 15080, 'SMI anual'), ('B24', 2500, 'Alquiler mensual'),
        ('B25', 2, 'Fianza'), ('B26', 1300, 'Suministros'), ('B27', 4500, 'Seguros'), ('B28', 0.01, 'Varios'),
        ('B30', 95000, 'Recursos propios'), ('B31', M.CALIBRAR, 'Préstamo bancario'), ('B32', 0.10, 'Tipo de interés'),
        ('B33', 10, 'Plazo del préstamo'), ('B34', 0, 'Carencia'), ('B35', 3, 'Fondo de maniobra'),
        ('B37', 0.25, 'Impuesto de Sociedades, nueva'), ('B38', 0.25, 'Impuesto de Sociedades, tipo'),
        ('B39', 0.08, 'IVA repercutido de restauración'), ('B40', 0.08, 'IVA repercutido/soportado'),
        ('B41', 0, 'IVA soportado en compras'), ('B42', 0, 'Bases negativas'),
        ('B44', 10, 'Vida útil de obra'), ('B45', 7, 'Vida útil de maquinaria'), ('B48', 0, 'Subida anual'),
        ('B51', 20, 'Aforo'), ('B52', 0.70, 'Actividad del mes 1'), ('B53', 4, 'Meses hasta alcanzar'),
        ('B54', 2, 'Meses de alquiler ANTES'), ('B55', 0.10, 'Imprevistos sobre las partidas de OBRA'),
        ('B58', 2, 'Días medios de cobro'), ('B59', 14, 'Días medios de pago'),
        ('B62', 0, 'Bebida ALCOHÓLICA'), ('B63', 0.08, 'IVA de la bebida ALCOHÓLICA'),
        ('B65', 1.15, 'DSCR mínimo'), ('B66', 1.25, 'DSCR objetivo'), ('B67', 0.15, 'Holgura mínima'),
        ('B68', None, 'Suelo salarial anual'),
    ]
    for c, val, rot in sup:
        v[('HELP', _S, c)] = (val, rot)
    # Inversión (D193): las 19 partidas tecleadas, filas 7-25 = $186,000; los imprevistos (B28) van por fórmula. B12 NUNCA
    # vacía: B37 = IF(B12="","",…) dejaría sin base la amortización del equipo (inv. §2.1)
    for k, val in enumerate([9000, 48000, 9000, 10000, 5000, 4500, 30000, 9000, 7000, 8500, 11000, 9000, 7000, 2500,
                             1500, 2500, 5000, 2500, 5000]):
        v[('HELP', _I, 'B%d' % (7 + k))] = (val, None)
    # P&L (D194, D195, D196): fijos B26-B35 ($16,600), G13 (soportado ponderado: valor en el ES) → 0, umbrales
    for k, val in enumerate([3000, 2400, 4500, 1800, 1500, 500, 1200, 600, 600, 500]):
        v[('HELP', _P, 'B%d' % (26 + k))] = (val, None)
    v[('HELP', _P, 'G13')] = (0, None)
    for c, val, rot in [('E51', 0.65, 'Margen bruto'), ('E53', 0.25, 'Coste de mercancía /'),
                        ('E54', 0.35, 'Coste de personal'), ('E55', 0.10, 'Alquiler'), ('E56', 0.05, 'Resultado neto')]:
        v[('HELP', _P, c)] = (val, rot)
    # Staffing (D194): personas (B), FTE por persona (C), bruto mes TOTAL de la fila (D); ≥ $15/h, 12 pagas, sin
    # propinas. Bruto = $/h × 173.3 × FTE (shift lead $17, seasonal $15, production $16). Cobertura = ES salvo B22 2.0 h
    for f, (b, c, d) in zip(range(5, 11), [(1, 1.0, 4000), (1, 1.0, 2946), (1, 0.5, 1300), (1, 0.25, 650),
                                           (1, 0.2, 555), (1, 0.1, 260)]):
        for col, val in zip('BCD', (b, c, d)):
            v[('HELP', _R, '%s%d' % (col, f))] = (val, None)
    v.update([(('HELP', _R, 'B13'), (8000, 'Coste anual')), (('HELP', _R, 'B14'), (8000, 'Coste anual')),
              (('HELP', _R, 'B22'), (2.0, 'Horas de producción'))])
    # Escenarios (D191): pesimista 140 · $7.00 · 300 (verano frío y lluvioso) / optimista 190 · $8.00 · 320
    v.update([
        (('HELP', _ES, 'B5'), (140, 'Clientes/día')), (('HELP', _ES, 'D5'), (190, 'Clientes/día')),
        (('HELP', _ES, 'B6'), (7.0, 'Ticket')), (('HELP', _ES, 'D6'), (8.0, 'Ticket')),
        (('HELP', _ES, 'B7'), (300, 'Días')), (('HELP', _ES, 'D7'), (320, 'Días')),
    ])
    return v


# Calibración D15 (D191: palancas en su orden; máx. 3 vueltas; la estacionalidad NO es palanca). Cada celda, citada en
# F2-NOTAS.md (G7). Se rellena tras el dry-run (F2-NOTAS §3)
CALIBRACION_D15 = OrderedDict()


def formulas_ice():
    p = os.path.join(AQUI, 'formulas_ice.json')
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
    M.TOKENS_DOCX = tokens_ice(M.TOKENS_DOCX)
    M.PRODUCTOS_CIERRE = PRODUCTOS_CIERRE_ICE
    M.DOCX_FIJOS = docx_fijos(M)
    M.DOCX_NOTAS = DOCX_NOTAS
    M.DOCX_NOTAS_PLAN = DOCX_NOTAS_PLAN
    M.FORMULAS_EN = formulas_ice()
    M.VALORES_EN = valores_ice(M)
    M.CALIBRACION_D15 = CALIBRACION_D15
    M.CELDA_PISTAS = CELDA_PISTAS
    M.PISTAS_EXTRA = PISTAS_EXTRA
    M.CIFRAS_PROHIBIDAS = cifras_prohibidas(M.VALORES_EN)
    M.RX_ICE_NO = RX_ICE_NO
    M.REGLA_UNIDADES = REGLA_UNIDADES
    glo = OrderedDict(M.GLOSARIO)
    for k, val in GLOSARIO_ICE.items():
        glo[k] = val                          # research §9 manda (regla de jerga §0)
    M.GLOSARIO = glo
