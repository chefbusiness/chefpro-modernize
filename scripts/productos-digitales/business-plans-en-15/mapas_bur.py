#!/usr/bin/env python3
"""
mapas_bur.py — Burger Restaurant Business Plan Kit (EN) · datos ES→EN del conjunto «bur» (estructura).

Fuente de verdad: `../plan-hamburgueseria/F1-camino.md` §6-§7 (EN delta) y `F1-research-us-delta.md` (US §n). Sesión Claude
Code, 31-oct-2026 (F2-EN). NO se ejecuta solo: lo importa `../business-plans-en/mapas.py` cuando `BP_CONJUNTO=bur` y
llama a `instalar(M)`. Clon de `../business-plans-en-14/mapas_sus.py` (Sushi Restaurant EN, LIVE el 31-oct): el libro ES de
la hamburguesería sale del SUSHI BAR LIVE (`../plan-hamburgueseria/semilla_ham.py`) con la `ROTACION` ENCENDIDA (medido el
31-oct: mismas celdas y pestañas; solo 4 fórmulas de texto distintas, C50, D27, D37 y F13), así que `Break-Even` NO se
desplaza. Van los parches E2 (G14), E4 (Staffing!C12) y E5 (G11), G13 → 0 y el DICCIONARIO en cadena, sin normalizar:

  0. EN del SUSHI EN en la MISMA celda (`../business-plans-en-14/textos_es.json` + `textos_en/{GM,GR,GRC,GSUS-plan,
     GSUS-check}.json` + `*.revision.json` + `datos_sus.POR_CELDA`); checklist casado por POSICIÓN de pestaña;
  1. EN del TACO EN por TEXTO (`../business-plans-en-12/`: el mostrador); 2. EN del ROTISSERIE EN por texto
     (`../business-plans-en-13/`); 3. EN del SUSHI EN por texto; 4. EN de la PIZZA EN por celda y por texto; 5. BAKERY EN;
     6. BAR EN; 7. BP/BP2 (GM → REST → CAF → FT).

FUENTE ES: `FUENTE_ES` = `$BUR_FUENTE_ES` o, sin la variable, `astro-site/public/dl/plan-negocio-hamburgueseria` (el ES
FINAL y revisado de la F2 ES, `17117feb`: no hay paso 1c). Grupos:
  GM          motor común: mismo ES que una cadena GM (Sushi EN, Taco EN, Rotisserie EN, Pizza EN, Bar EN o BP) con un EN
              limpio (RX_REESCRIBIR).
  GR · GRC    EN de GSUS-* / GR / GRC del Sushi EN, del Taco EN, del Rotisserie EN, de la Pizza EN, de la Bakery, del Bar o
              de REST/CAF/FT: preparar_tandas lo escribe; GR (plan) lo revisa la tanda GBUR-plan (textos_en/GR.revision.json)
              y GRC (solo del checklist) la tanda GBUR-check (textos_en/GRC.revision.json).
  GBUR-plan   nuevas del plan (y las de reuso con vocabulario o caso de otro negocio, con propuesta) + las 12 filas
              D19 (una cadena por celda, sin propuesta).
  GBUR-check  nuevas del checklist (80 tareas). El checklist ES ya nace con la DV «✓,☐,N/A» (la del Sushi Bar): sin la
              regla «—» → ☐ de los conjuntos taq/pol.

    python3 bp15.py mapas           # autotest + cruce con censo_es.json + verificar (incluye los sha256)
"""
import hashlib
import importlib.util
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
TAQ = os.path.join(PD, 'business-plans-en-12')
POL = os.path.join(PD, 'business-plans-en-13')
SUS = os.path.join(PD, 'business-plans-en-14')

# ==========================================================================
# 0. Producto (F1-camino §6)
# ==========================================================================
FUENTE_ES = os.environ.get('BUR_FUENTE_ES') or 'astro-site/public/dl/plan-negocio-hamburgueseria'
PLANES = OrderedDict([
    ('bur', OrderedDict([
        ('slug', 'burger-restaurant-business-plan'),
        ('producto', 'Burger Restaurant Business Plan Kit'),
        ('slug_es', 'plan-negocio-hamburgueseria'),
        ('dir_es', FUENTE_ES),
        ('env_stripe', 'VITE_STRIPE_PAYMENT_LINK_BURGER_RESTAURANT_BUSINESS_PLAN'),
        ('keywords', 'burger restaurant business plan, smash burger business plan, how to open a burger restaurant, '
                     'burger restaurant startup costs, cost per burger, AI Chef Pro'),
    ])),
])
for _p in PLANES.values():
    _p['url'] = 'aichef.pro/en/digital-products/' + _p['slug']
    _p['dir_en'] = 'astro-site/public/dl/' + _p['slug']

LIBROS = OrderedDict([
    ('BURP', ('bur', 'plan-financiero-hamburgueseria.xlsx', 'burger-restaurant-financial-projections.xlsx',
              'Burger Restaurant Financial Projections: 3-Year P&L, Cash Flow & Financing')),
    ('BURC', ('bur', 'checklist-apertura-hamburgueseria.xlsx', 'burger-restaurant-startup-checklist.xlsx',
              'Burger Restaurant Startup Checklist (80 Tasks)')),
])
DOCX = OrderedDict([
    ('bur', ('plan-de-negocio-hamburgueseria.docx', 'burger-restaurant-business-plan.docx',
             'Burger Restaurant Business Plan (10 Sections)')),
])
TIPO_DE = {'BURP': 'plan', 'BURC': 'check'}
A_SUS = {'BURP': 'SUSP', 'BURC': 'SUSC'}                  # libro del Sushi EN (diccionario por celda, nivel 0)
A_TAQ = {'BURP': 'TAQP', 'BURC': 'TAQC'}                  # libro del Taco EN (por texto; la celda solo para el «donde»)
A_PIZ = {'BURP': 'PIZP', 'BURC': 'PIZC'}                  # libro de la Pizza EN (diccionario por celda, nivel 4)

# ==========================================================================
# 1. Pestañas: plan = las de la taquería (9, mismos nombres ES); checklist (todas ≤ 31 caracteres; F2 y F3 = US §9)
# ==========================================================================
_HOJAS_PLAN = OrderedDict([
    ('0. Supuestos', '0. Assumptions'), ('Inversión Inicial', 'Startup Costs'), ('PyG 3 Años', '3-Year P&L'),
    ('Punto Equilibrio', 'Break-Even'), ('Escenarios', 'Scenarios'), ('Personal', 'Staffing'),
    ('Instrucciones', 'Instructions'), ('Tesorería 12 meses', '12-Month Cash Flow'), ('Financiación', 'Financing'),
])
_HOJAS_CHECK = OrderedDict([
    ('F1 - Constitución', 'Phase 1 - Business Setup'), ('F2 - Local, humos y gas', 'Phase 2 - Hood & Permits'),
    ('F3 - Carne, fritura y sanidad', 'Phase 3 - Beef & Health'),
    ('F4 - Personal y alérgenos', 'Phase 4 - Staff & Allergens'),
    ('F5 - Carta, marca y delivery', 'Phase 5 - Menu, Brand, Delivery'),
    ('F6 - Apertura y 90 días', 'Phase 6 - Opening & 90 Days'), ('Instrucciones', 'Instructions'),
])
assert all(len(v) <= 31 for v in _HOJAS_CHECK.values())
HOJAS_POR_LIBRO = OrderedDict([('BURP', _HOJAS_PLAN), ('BURC', _HOJAS_CHECK)])
HOJAS_ES_POR_LIBRO = OrderedDict((c, list(d)) for c, d in HOJAS_POR_LIBRO.items())
TAREAS_POR_FASE = OrderedDict([('BURC', [12, 15, 14, 13, 13, 13])])          # 80 (F1-camino §4, mismas filas)
MOLDE_CHECK = OrderedDict([('BURC', 'hojas')])
COL_OK = OrderedDict([('BURC', 1)])
FASES_CABECERA = OrderedDict()

# Pestañas ES del sushi bar, de la taquería y de la pizza en el MISMO orden (el checklist se casa por posición)
_HOJAS_SUS = {
    'BURP': list(_HOJAS_PLAN),
    'BURC': ['F1 - Constitución', 'F2 - Local, frío y extracción', 'F3 - Pescado, arroz y sanidad',
             'F4 - Personal y alérgenos', 'F5 - Carta, marca y delivery', 'F6 - Apertura y 90 días', 'Instrucciones'],
}
HOJA_SUS = {c: dict(zip(HOJAS_ES_POR_LIBRO[c], _HOJAS_SUS[c])) for c in HOJAS_ES_POR_LIBRO}
_HOJAS_TAQ = {
    'BURP': list(_HOJAS_PLAN),
    'BURC': ['F1 - Constitución', 'F2 - Local, humos y gas', 'F3 - Cocina, trompo y sanidad', 'F4 - Personal y alérgenos',
             'F5 - Carta, marca y delivery', 'F6 - Apertura y 90 días', 'Instrucciones'],
}
HOJA_TAQ = {c: dict(zip(HOJAS_ES_POR_LIBRO[c], _HOJAS_TAQ[c])) for c in HOJAS_ES_POR_LIBRO}
_HOJAS_PIZ = {
    'BURP': list(_HOJAS_PLAN),
    'BURC': ['F1 - Constitución', 'F2 - Local, humos y licencia', 'F3 - Cocina, horno y sanidad',
             'F4 - Personal y prevención', 'F5 - Carta, marca y delivery', 'F6 - Apertura y 90 días', 'Instrucciones'],
}
HOJA_PIZ = {c: dict(zip(HOJAS_ES_POR_LIBRO[c], _HOJAS_PIZ[c])) for c in HOJAS_ES_POR_LIBRO}

# ==========================================================================
# 2. Fórmulas (= Sushi EN, Taco EN y Pizza EN, F1-camino §6): E2 solo G14 (G13 es VALOR en el ES → VALORES_EN 0), E4
#    (Staffing!C12 = Σ personas × FTE: 2 grill cooks, 3 counter crew y 3 weekend crew en una fila) y E5 (el literal 0.21 de la línea de bebida → B40)
# ==========================================================================
_E2_ALC = ("('0. Supuestos'!$B$62*'0. Supuestos'!$B$40+(1-'0. Supuestos'!$B$62)*'0. Supuestos'!$B$39)")
PARCHES_FORMULA = OrderedDict([
    (('BURP', 'PyG 3 Años', 'G14'), (_E2_ALC, "'0. Supuestos'!$B$41")),
    (('BURP', 'Personal', 'C12'), ('SUM(C5:C11)', 'SUMPRODUCT(B5:B11,C5:C11)')),
    (('BURP', 'PyG 3 Años', 'G11'), ('H11*0.21', "H11*'0. Supuestos'!$B$40")),
])

# ==========================================================================
# 3. Instrucciones: versión D20 y aviso D21 (E1: BURP A52, BURC A12; la tabla D19 del ES tiene 12 filas, 35-46, = el
#    sushi bar); zona D19 (sin D18) por cabecera
# ==========================================================================
FILA_VERSION = OrderedDict([('BURP', 51), ('BURC', 11)])
ZONAS_CELDA = OrderedDict([
    (('BURP', 'Instrucciones'), [(None, None, 'ABCD', 'D19')]),
])

# ==========================================================================
# 4. Docx: las 131 ranuras del FT ES (= PIZ = SUS), H1 en 37·44·51·59·67·76·83·91·100·109; último de §9 = 108 (nota UK);
#    tandas bur_a (§1-5) y bur_b (§6-10), 61 ranuras desde el Word ES final (bp15.py extraer_docx)
# ==========================================================================
DOCX_N_PARRAFOS = OrderedDict([('bur', 131)])
DOCX_ENCABEZADOS = OrderedDict([('bur', [37, 44, 51, 59, 67, 76, 83, 91, 100, 109])])
DOCX_INDICE = OrderedDict([('bur', list(range(24, 34)))])
DOCX_ULTIMO_9 = OrderedDict([('bur', '108')])
DOCX_TANDAS = OrderedDict([('bur_a', ('bur', [1, 2, 3, 4, 5])), ('bur_b', ('bur', [6, 7, 8, 9, 10]))])
PRESTAMO_SEMILLA = OrderedDict([('bur', 247000)])                   # research US §8: ≈ $247,000 (punto fijo en F2)

AUTOTEST = OrderedDict([
    ('P1', 'BURP'), ('P2', 'BURP'), ('C1', 'BURC'), ('C2', 'BURC'),
    ('C1_hoja_papel', 'F2 - Local, humos y gas'), ('C1_titulo', 'Burger Restaurant Startup Checklist (80 Tasks)'),
    ('C2_hoja_no_latino', 'F5 - Carta, marca y delivery'), ('P1_celda_texto', 'A3'), ('P1_celda_formula', 'B9'),
    ('P1_merge', 'A30:C30'),
])

# ==========================================================================
# 5. Grupos (= heladería: GR del plan y GRC del checklist)
# ==========================================================================
GRUPOS = ('GM', 'GR', 'GRC', 'GBUR-plan', 'GBUR-check')
GRUPOS_TRADUCTORES = ('GBUR-plan', 'GBUR-check')
GRUPOS_OVERRIDES = ('GBUR-plan', 'GBUR-check')
REVISAR_EN_TANDA = OrderedDict([('GBUR-plan', ('GR',)), ('GBUR-check', ('GRC',))])
GRUPOS_DESC = OrderedDict([
    ('GM', 'REUTILIZADAS: motor común (mismo ES que una cadena GM del Sushi EN, del Taco EN, de la Pizza EN, del Bar EN o de BP) con un '
           'EN sin vocabulario ni caso de otro negocio. preparar_tandas escribe su EN. No van a los traductores'),
    ('GR', 'REUTILIZADAS con revisión (plan): EN de GSUS-* / GTAQ-* / GR / GRC del Sushi EN o del Taco EN, de GPIZ-* de la Pizza EN, de la Bakery '
           'EN, del Bar EN o de REST/CAF/FT. preparar_tandas escribe su EN; la '
           'tanda GBUR-plan las revisa en textos_en/GR.revision.json'),
    ('GRC', 'REUTILIZADAS con revisión (solo del checklist): EN del Sushi EN, del Taco EN o de la Pizza EN (plazos, responsables, '
            'cabeceras, tareas). preparar_tandas escribe su EN; la tanda GBUR-check las revisa en '
            'textos_en/GRC.revision.json'),
    ('GBUR-plan', 'Nuevas del plan financiero (BURP) + las de reuso con vocabulario o caso de otro negocio (con '
                  'propuesta) + las 12 filas D19 de Instrucciones (una cadena por celda, sin propuesta)'),
    ('GBUR-check', 'Nuevas del checklist (BURC): las 80 tareas, sus cabeceras y los mensajes de la DV (con propuesta '
                   'cuando el Sushi EN, el Taco EN o la Pizza EN tienen el mismo ES)'),
    ('GX', 'NO se traduce: pestañas (mapas.HOJAS_POR_LIBRO), CLAVES, FIJOS, POR_CELDA, versión, pie y docProps'),
])

# Vocabulario y caso del SUSHI, el TACO, el ROTISSERIE, la PIZZA, la PANADERÍA y el BAR que NO vale para la hamburguesería:
# clasifica las PROPUESTAS (no es el gate: ese es datos_bur.RX_BUR_NO). Una propuesta sucia va a los traductores con su EN
# como forma. «covers», «seat turns», «counter service», «kiosk», «hood», «griddle», «fryer», «beer», «pickup» y «open 7
# days» SÍ valen en la hamburguesería (US §1 y §8: counter service, abre 7 días, 360 días); NO valen «servers», «table
# service», «closed Mondays» ni el caso del sushi (115 covers, $32.50, 310 días, 40 plazas, 1,800 sq ft). «360» y «$17.50»
# (Rotisserie y Taco EN) son del caso burger (360 días, optimista de $17.50): no van aquí
_CASO_OTROS = (r'669,600|709,776|738,167|242,550|329,274|86,724|217,300|39,275|\$36(?:\.00)?\b|\$38\.88|'
               r'619,850|657,041|683,323|176,000|197,600|275,612|\b308\b|\$2,800\b|\b1,200 sq ft\b|'
               r'819,000|868,140|902,866|216,000|237,832|335,708|\b130 covers\b|\$3,733\b|\b1,600 sq ft\b|'
               r'\b62 covers\b|\b50 seats\b|\b30 seats\b|\b1,500 sq ft\b|'
               r'1,158,625|1,228,142|1,277,268|256,000|385,156|255,100|223,800|130,056|41,663|182,591|140,937|'
               r'\$32\.50\b|\b115 covers\b|\b310\b|\b40 seats\b|\b1,800 sq ft\b|\$41(?:\.00)?\b|\$46(?:\.00)?\b')
RX_REESCRIBIR = re.compile(
    r'(?i)\bpizz|\bdough\b|\bovens?\b|Neapolitan|\bVPN\b|firewood|wood-fired|\bflue\b|spark arrestor|\bpeels?\b|'
    r'hearth|mozzarella|San Marzano|Margherita|\b00 flour|\btapas\b|'
    r'small plates|\bcocktails?\b|\bspirits\b|\bbartend|happy hour|full liquor|\bbread\b|\bbakery\b|\bbakers?\b|'
    r'\bloa(?:f|ves)\b|pastr(?:y|ies)|croissant|transactions?(?:/day| per day| a day)|'
    r'\btacos?\b|taquer|trompo|al pastor|\bpastor\b|tortill|\bmasa\b|nixtamal|salsa bar|quesadilla|\bgringas?\b|'
    r'carnitas|birria|suadero|aguas? frescas?|horchata|jamaica|Cinco de Mayo|Mexican beer|\bcomal\b|'
    r'guac|pico de gallo|salsa macha|pork shoulder|vertical broiler|\bpatio\b|'
    r'rotisserie|chicken|\bbirds?\b|\bspits?\b|yuca|family meals?|pollo|Peruvian|\baji\b|huancaina|chicha|maduros|'
    r'salchipapa|heated display|marinade|'
    r'sushi|nigiri|sashimi|\bmaki\b|\brolls?\b|itamae|\bsake\b|raw fish|parasit|platters?|omakase|rice cookers?|'
    r'\bnori\b|imitation crab|wasabi|\bpoke\b|tempura|gyoza|\bmiso\b|teriyaki|\bneta\b|\bshari\b|\bsaku\b|'
    r'hangiri|\bfish\b|seafood|histamine|scombro|\bservers?\b|table service|tips? on top|closed Mondays|Mondays|'
    r'six days|6 days a week|' + _CASO_OTROS)

# sha256 de los diccionarios del Sushi EN (LIVE 07e7513a, con el resync tras #191), del Taco EN (LIVE bf18ff72 + #186), del
# Rotisserie EN (LIVE 26e618f8 + #186) y de la Pizza EN (+ #186), medidos el 31-oct sobre 17117feb. Si cambian, hay que
# re-extraer y rehacer preparar_tandas (bp15.py verificar avisa)
SHA_SUS = OrderedDict([
    ('textos_es.json', '158dc547d78a3b481b64f929e3f6f1498e6ca4549c1328cb6e9433ab28bdb286'),
    ('textos_en/GM.json', 'defe93056b5d6e4d34e585a97eb34cb89a211ba94a85d5dc6dd75ff8ac98ff72'),
    ('textos_en/GM.revision.json', '40f4cf8d363cc8d6390a0b9855c88e075301cb6df6e4d64cfe1945942e075bbc'),
    ('textos_en/GR.json', '52068bcd92bbdcbfbb0561b10532657ae79d7a3566170a4ca9da9d673e7e2e98'),
    ('textos_en/GR.revision.json', '4e1aa37fb8592fc36dd3f1c81d4b3e3486abd0c64678e33cd4b5274aef1bab82'),
    ('textos_en/GRC.json', 'f3ab2057bc030ea5d87f64ae79635492a0aef4f035a0fadda2645944974edef6'),
    ('textos_en/GRC.revision.json', '9dc659e2bf41b547c81839a806f1b533eafdef90320227ef2b39ba29c551420c'),
    ('textos_en/GSUS-plan.json', 'faf64a1d8c0075fe7a09aea9309f3a97ad1b3b31006b6d618cb6b55d1513cb8a'),
    ('textos_en/GSUS-check.json', '9c7d6433b2c8f358a8cbe4ec25ad166a4afb1d9a227e3ac75aaf30523a4e0021'),
    ('formulas_sus.json', 'ede84f6cf983db3e473dafb08f037aed1653086028fd966fc033d7c3d13d5409'),
    ('censo_es.json', '12382f3c6d9d2a96536fe1484e9fb8adc13d239597d8e07e3599fbd1b1e498c1'),
    ('datos_sus.py', '30198e54e55beb56fd58479aac7d47c4d76a182f9e4e588667e569e0627027ce'),
])
SHA_TAQ = OrderedDict([
    ('textos_es.json', '6ea5f29803fe74e6013738f7896931c473b4bb143cca529dd3c850d49725874c'),
    ('textos_en/GM.json', '17bceb7b136363c3869b5e713fac64e6972bd87114bd45db58a993c08d23a877'),
    ('textos_en/GM.revision.json', 'bfc5dfa013ee8661d33e1181fcafdea1c291c8f2d23068dc1c1c967f72905d6e'),
    ('textos_en/GR.json', 'ead32eecbe8cd17532ce8e8a560d9ffc22aa91bd16a921e931792441fc0b5b27'),
    ('textos_en/GR.revision.json', 'b632ba77785bcebb14d96c666f4b91b8d3f2d12837ef1220cb30aec18f855682'),
    ('textos_en/GRC.json', 'e7ddfab10026b9c4f735338cab31f63c504f479661453f4bd79839052f81ebc1'),
    ('textos_en/GRC.revision.json', 'cda1d04f28213288b2ab41607b4415100005b3224c96f7aeb7416fa520f50f9b'),
    ('textos_en/GTAQ-plan.json', 'e2fdac65fca460a019411ea99c7c01c92bd4ec8af9cf8f3d8ed1c9eecab2a014'),
    ('textos_en/GTAQ-check.json', '33ab5e40c525f126e37f3ae67b51defa00631e3048ce51e945f61d313e4effd6'),
    ('formulas_taq.json', '32ebc9b30708271f45ec8c6534da31cef637b108f7e3228ecd52e4559fd05c10'),
    ('censo_es.json', '0626cb6d3731262445961ff212bbbbad6c6492558c21a6339f4e85dd036aff68'),
    ('datos_taq.py', '0f0342a6eaf357eb8b97aba07c74a9f80548034b86bb48a30a6d7bdf877185ab'),
])
SHA_POL = OrderedDict([
    ('textos_es.json', '587ef9920989718002a1ab7071c0bedf12d24faa2ef5919e64d4aad1aa2d6ea7'),
    ('textos_en/GM.json', '007679a592c311b2f11519c696ab3d52d1699b154d06252c2683f4159a3946ec'),
    ('textos_en/GR.json', '764fabde7a5f42a4091f0405bf4811c328cf840eeebe46b509d5853272a6c34e'),
    ('textos_en/GR.revision.json', '9141fde9272e0fa6d3a239f3b84020c5d47a4e927977ba307b24d27f6c02658b'),
    ('textos_en/GRC.json', 'ab0546ed982b4d69aa99064544c2c04f5bcccb495461fd82ce8ff36401094199'),
    ('textos_en/GRC.revision.json', 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356'),
    ('textos_en/GPOL-plan.json', '61814c88bd87215d9a341147816fbefbbd848e7fcefc20e0d90f79c27c1686bf'),
    ('textos_en/GPOL-check.json', 'f4b33e4997c124695850f19acc9d4b8943fd77e5e3bc23de7f9e5378f967fc58'),
])
SHA_PIZ = OrderedDict([
    ('textos_es.json', '7f504ed3ffc1ec12e95b36888dbf4e92711b7d1cc4319cb6128251deea817986'),
    ('textos_en/GM.json', '0f6cd4198a3c533331cca1111dde7a5de26c87b173e0d2712abafac72e6c08ed'),
    ('textos_en/GR.json', 'ef088edc5b1709acd9ad28ab3f5d7023a6421f505fc0d0dfedb63a7f099e8151'),
    ('textos_en/GM.revision.json', 'b6d5e7768ba1fa4240dd3c055355db4fc17559b3eec0249f57978cbf574d7876'),
    ('textos_en/GR.revision.json', 'fc7cfb4e679c7f30c5571381cc72b9d4bec3094283172fdb5c30e508147941d0'),
    ('textos_en/GPIZ-plan.json', 'a52044a121fd9e28c7931534c3ee54adabe856a186c543c5f13e6aa08a7dc3b6'),
    ('textos_en/GPIZ-check.json', 'c3d62514b899edb9d0aa9a1c32fcaa3517a22229fe4121bd72d2b978d43556da'),
    ('formulas_piz.json', '286b3675b30e2eed71982781e209f4aa063fe4c8be2e7c616ebbd54877caebb2'),
    ('censo_es.json', '442b610642a4a11ea781c1790d02a74bf5c41b4e9da5fa790b8ab2c3fe1bf53b'),
    ('datos_piz.py', '44c178d7bb9ae94eb696f26d8f964ba98f510e275e4104ce5baece71e1d2158e'),
])
# sha256 del ES FINAL (F2 ES revisada, 17117feb = plan-hamburgueseria/REVISION-FINAL.md; Mac = VPS el 31-oct): si el ES
# cambia (la F3 ES retoca frases legales españolas que no cruzan), manda el ES nuevo: resync_es.py --solo business-plans-en-15
SHA_ES = OrderedDict([
    ('plan-financiero-hamburgueseria.xlsx', '05eb9365960653a325f6c60a20db116c62edf66e2c62d68f95e334bba601aa7f'),
    ('checklist-apertura-hamburgueseria.xlsx', 'f997c9a68c08bcd1d7a78af92856c252469d22f25340d3352f9677637a683ee0'),
    ('plan-de-negocio-hamburgueseria.docx', '0ea51bd9777f91fe2fe0b66e068b39194e9f18847e1ec222ce03d0546104920f'),
])


def _sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def diccionario_ok():
    """[] si los ficheros de los diccionarios del Sushi EN, del Taco EN, del Rotisserie EN y de la Pizza EN siguen con su
    sha256."""
    out = []
    for carpeta, nombre, shas in ((SUS, 'business-plans-en-14', SHA_SUS), (TAQ, 'business-plans-en-12', SHA_TAQ), (POL, 'business-plans-en-13', SHA_POL),
                                  (PIZ, 'business-plans-en-8', SHA_PIZ)):
        for rel, sha in shas.items():
            p = os.path.join(carpeta, rel)
            if not os.path.exists(p):
                out.append('%s/%s: falta' % (nombre, rel))
            elif _sha(p) != sha:
                out.append('%s/%s: sha256 distinto del fijado en mapas_bur' % (nombre, rel))
    return out


# ==========================================================================
# 6. Diccionario: Sushi EN por celda → Taco EN por texto → Rotisserie EN por texto → Sushi EN por texto → Pizza EN por
#    celda → por texto → Bakery → Bar → BP/BP2
# ==========================================================================
def _modulo(nombre, ruta):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _en_de(carpeta, grupos):
    """EN de los grupos de un conjunto, con sus *.revision.json encima (idempotente si ya van dentro)."""
    en = OrderedDict()
    for g in grupos:
        p = os.path.join(carpeta, 'textos_en', g + '.json')
        if os.path.exists(p):
            en.update(json.load(open(p, encoding='utf-8')))
        r = os.path.join(carpeta, 'textos_en', g + '.revision.json')
        if os.path.exists(r):
            en.update(json.load(open(r, encoding='utf-8')))
    return en


def _donde(c):
    return ['%s %s!%s' % (d['f'], d.get('h', ''), d.get('c', '')) for d in c['donde'][:2]]


def _cargar_celda(carpeta, grupos, datos, etiqueta):
    """(por celda {(corto, hoja ES, celda): entrada}, por texto {es: entrada}) de un conjunto EN cerrado."""
    celda, texto = OrderedDict(), OrderedDict()
    te_p = os.path.join(carpeta, 'textos_es.json')
    if not os.path.exists(te_p):
        return celda, texto
    en = _en_de(carpeta, grupos)
    por_celda = _modulo('%s_ref_bur' % datos, os.path.join(carpeta, datos + '.py')).POR_CELDA
    for c in json.load(open(te_p, encoding='utf-8'))['cadenas']:
        for d in c['donde']:
            if d.get('t') != 'celda':
                continue
            k = (d['f'], d['h'], d['c'])
            if k in por_celda:                                             # override de ese conjunto en esa celda
                celda[k] = OrderedDict([('es', c['es']), ('en', por_celda[k]), ('grupo', 'POR_CELDA'),
                                        ('id', c['id']), ('tratamiento_origen', 'traducir'), ('conjunto', etiqueta)])
            elif c['id'] in en and c['tratamiento'] in ('traducir', 'localizar'):
                celda[k] = OrderedDict([('es', c['es']), ('en', en[c['id']]), ('grupo', c['grupo']), ('id', c['id']),
                                        ('tratamiento_origen', c['tratamiento']), ('conjunto', etiqueta)])
        if c['id'] in en and c['tratamiento'] == 'traducir':
            texto.setdefault(c['es'], OrderedDict([('es', c['es']), ('en', en[c['id']]), ('grupo', c['grupo']),
                                                   ('id', c['id']), ('tratamiento_origen', 'traducir'),
                                                   ('conjunto', etiqueta), ('donde', _donde(c))]))
    return celda, texto


def _cargar_texto(carpeta, grupos, etiqueta, overrides=()):
    """{es: entrada} por TEXTO de un conjunto (solo «traducir»). `overrides`: grupos con overrides_<g>.json por celda
    (Bakery): la entrada guarda el EN de cada celda sobreescrita en `por_celda` {(hoja, celda): EN}."""
    out = OrderedDict()
    te_p = os.path.join(carpeta, 'textos_es.json')
    if not os.path.exists(te_p):
        return out
    te = json.load(open(te_p, encoding='utf-8'))
    for g in grupos:
        en = _en_de(carpeta, (g,))
        ov = {}
        if g in overrides:
            po = os.path.join(carpeta, 'textos_en', 'overrides_%s.json' % g)
            if os.path.exists(po):
                ov = json.load(open(po, encoding='utf-8'))
        for c in te['cadenas']:
            if c['grupo'] != g or c['id'] not in en or c['tratamiento'] != 'traducir' or c['es'] in out:
                continue
            x = OrderedDict([('es', c['es']), ('en', en[c['id']]), ('grupo', g), ('id', c['id']),
                             ('tratamiento_origen', 'traducir'), ('conjunto', etiqueta), ('donde', _donde(c))])
            if c['id'] in ov:
                o = ov[c['id']]
                x['por_celda'] = {(o['hoja'], o['celda']): o['texto']}
            out[c['es']] = x
    return out


_ET_SUS = 'business-plans-en-14 (Sushi EN cerrada)'
_ET_TAQ = 'business-plans-en-12 (Taco EN cerrada)'
_ET_PIZ = 'business-plans-en-8 (Pizza EN cerrada)'
_ET_POL = 'business-plans-en-13 (Rotisserie EN cerrada)'
SUS_CELDA, SUS_TEXTO = _cargar_celda(SUS, ('GM', 'GR', 'GRC', 'GSUS-plan', 'GSUS-check'), 'datos_sus', _ET_SUS)
_TAQ_CELDA, TAQ_TEXTO = _cargar_celda(TAQ, ('GM', 'GR', 'GRC', 'GTAQ-plan', 'GTAQ-check'), 'datos_taq', _ET_TAQ)
_POL_CELDA, POL_TEXTO = _cargar_celda(POL, ('GM', 'GR', 'GRC', 'GPOL-plan', 'GPOL-check'), 'datos_pol', _ET_POL)
PIZ_CELDA, PIZ_TEXTO = _cargar_celda(PIZ, ('GM', 'GR', 'GPIZ-plan', 'GPIZ-check'), 'datos_piz', _ET_PIZ)
# Bakery (GPAN/GN, con overrides de GPAN), Bar, y la cadena BP de la pizza (GM → REST → CAF → FT)
PAN_TEXTO = _cargar_texto(BP2, ('GPAN', 'GN'), 'business-plans-en-2 (Bakery EN)', overrides=('GPAN',))
BAR_TEXTO = _cargar_texto(BAR, ('GM', 'GR', 'GBAR-plan', 'GBAR-check'), 'business-plans-en-3 (Bar EN)')
BP_TEXTO = OrderedDict()
for _carpeta, _gs, _et in [(BP, ('GM',), 'business-plans-en (GM)'), (BP2, ('GREST',), 'business-plans-en-2 (REST)'),
                           (BP, ('GCAF',), 'business-plans-en (CAF)'), (BP, ('GFT',), 'business-plans-en (FT)')]:
    for _k, _v in _cargar_texto(_carpeta, _gs, _et, overrides=('GREST',)).items():
        BP_TEXTO.setdefault(_k, _v)
# grupos de ORIGEN que son motor común (GM): su EN por texto no va a nadie si está limpio
_GM_ORIGEN = {(_ET_SUS, 'GM'), (_ET_TAQ, 'GM'), (_ET_POL, 'GM'), (_ET_PIZ, 'GM'), ('business-plans-en-3 (Bar EN)', 'GM'),
              ('business-plans-en (GM)', 'GM')}


def _celdas(e):
    return [o for o in e['donde'] if o.get('t') == 'celda']


def _por_celda(dic, libros, hojas, celdas, es):
    gem = [dic.get((libros.get(o['f']), hojas.get(o['f'], {}).get(o['h']), o['c'])) for o in celdas]
    if celdas and all(x is not None and x['es'] == es for x in gem) and len({x['en'] for x in gem}) == 1:
        return OrderedDict(gem[0])
    return None


def propuesta_de(e):
    """(entrada de reuso, origen) de una cadena de la hamburguesería, o (None, None). origen: 'celda-sus', 'texto-taq',
    'texto-pol', 'texto-sus', 'celda-piz', 'texto-piz', 'texto-pan', 'texto-bar', 'texto-bp'."""
    es = e['es']
    celdas = _celdas(e)
    x = _por_celda(SUS_CELDA, A_SUS, HOJA_SUS, celdas, es)
    if x:
        return x, 'celda-sus'
    if es in TAQ_TEXTO:
        return TAQ_TEXTO[es], 'texto-taq'
    if es in POL_TEXTO:
        return POL_TEXTO[es], 'texto-pol'
    if es in SUS_TEXTO:
        return SUS_TEXTO[es], 'texto-sus'
    x = _por_celda(PIZ_CELDA, A_PIZ, HOJA_PIZ, celdas, es)
    if x:
        return x, 'celda-piz'
    if es in PIZ_TEXTO:
        return PIZ_TEXTO[es], 'texto-piz'
    if es in PAN_TEXTO:
        x = PAN_TEXTO[es]
        ov = x.get('por_celda') or {}
        en_ov = {ov[(o['h'], o['c'])] for o in celdas if (o['h'], o['c']) in ov}
        if en_ov and len(en_ov) == 1:                                     # override de la Bakery en ESA celda
            x = OrderedDict(x)
            x['en'] = en_ov.pop()
        return x, 'texto-pan'
    if es in BAR_TEXTO:
        return BAR_TEXTO[es], 'texto-bar'
    if es in BP_TEXTO:
        return BP_TEXTO[es], 'texto-bp'
    return None, None


def _limpia(en):
    return not RX_REESCRIBIR.search(en or '')


def grupo_de(planes, texto=None, tratamiento=None, donde=None):
    donde = donde or []
    libros = {o['f'] for o in donde}
    destino = 'GBUR-check' if libros == {'BURC'} else 'GBUR-plan'
    if any(o.get('det') == 'D19' for o in donde):
        return 'GBUR-plan'                                   # las 12 filas D19 cambian enteras
    if tratamiento != 'traducir':
        return destino
    prop, origen = propuesta_de({'es': texto, 'donde': donde})
    if not prop or not _limpia(prop['en']):
        return destino
    if (prop.get('conjunto'), prop['grupo']) in _GM_ORIGEN:
        return 'GM'
    return 'GRC' if libros == {'BURC'} else 'GR'


def reuso_de(e):
    """EN del diccionario (GM / GR) o PROPUESTA para los traductores. D19: sin propuesta."""
    if any(o.get('det') == 'D19' for o in e['donde']) or e['tratamiento'] != 'traducir':
        return None
    prop, origen = propuesta_de(e)
    if not prop:
        return None
    libros, hojas = ((A_SUS, HOJA_SUS) if origen.endswith('-sus') else (A_TAQ, HOJA_TAQ) if origen.endswith('-taq')
                     else (A_PIZ, HOJA_PIZ))
    donde = prop.get('donde') or ['%s %s!%s' % (libros.get(o['f']), hojas.get(o['f'], {}).get(o.get('h'), ''),
                                                o.get('c', '')) for o in _celdas(e)[:2]]
    return OrderedDict([('grupo', prop['grupo']), ('id', prop['id']), ('en', prop['en']),
                        ('tratamiento_origen', prop['tratamiento_origen']),
                        ('conjunto', prop.get('conjunto', _ET_PIZ)), ('origen', origen), ('donde', donde)])


# ==========================================================================
# instalar
# ==========================================================================
def instalar(M):
    """Sustituye en el módulo `mapas` (M) los datos de FT/CAF por los de la hamburguesería."""
    from datos_bur import completar                                        # contenido (FIJOS, caso US, docx…)
    M.DATOS = AQUI
    M.PLANES, M.LIBROS, M.DOCX, M.TIPO_DE = PLANES, LIBROS, DOCX, TIPO_DE
    M.FICHEROS = OrderedDict((v[1], v[2]) for v in LIBROS.values())
    M.FICHEROS.update((v[0], v[1]) for v in DOCX.values())
    M.TITULOS = OrderedDict((v[2], v[3]) for v in LIBROS.values())
    M.TITULOS.update((v[1], v[2]) for v in DOCX.values())
    M.LIBROS_ES = [v[1] for v in LIBROS.values()]
    M.CORTO_DE = {v[1]: k for k, v in LIBROS.items()}
    M.PLAN_DE = {k: v[0] for k, v in LIBROS.items()}
    M.HOJAS_POR_LIBRO, M.HOJAS_ES_POR_LIBRO = HOJAS_POR_LIBRO, HOJAS_ES_POR_LIBRO
    M.TAREAS_POR_FASE, M.MOLDE_CHECK, M.COL_OK, M.FASES_CABECERA = TAREAS_POR_FASE, MOLDE_CHECK, COL_OK, FASES_CABECERA
    M.PARCHES_FORMULA = PARCHES_FORMULA
    M.FILA_VERSION = FILA_VERSION
    M.TEXTOS_NUEVOS = OrderedDict()
    for c, f in FILA_VERSION.items():
        t = M.AVISO_EN if TIPO_DE[c] == 'plan' else M.AVISO_EN + ' ' + M.AVISO_CHECK_EN
        M.TEXTOS_NUEVOS[(c, 'Instrucciones', 'A%d' % (f + 1))] = (t, 'A%d' % f)
    M.ZONAS_CELDA = ZONAS_CELDA
    M.DOCX_N_PARRAFOS, M.DOCX_ENCABEZADOS, M.DOCX_INDICE = DOCX_N_PARRAFOS, DOCX_ENCABEZADOS, DOCX_INDICE
    M.DOCX_ULTIMO_9, M.DOCX_TANDAS = DOCX_ULTIMO_9, DOCX_TANDAS
    M.DOCX_MOVER, M.DOCX_RPR_DE, M.DOCX_RESUMEN_TOKENS = OrderedDict(), OrderedDict(), OrderedDict()
    M.PRESTAMO_SEMILLA, M.AUTOTEST = PRESTAMO_SEMILLA, AUTOTEST
    M.GRUPOS, M.GRUPOS_TRADUCTORES, M.GRUPOS_OVERRIDES, M.GRUPOS_DESC = (GRUPOS, GRUPOS_TRADUCTORES,
                                                                         GRUPOS_OVERRIDES, GRUPOS_DESC)
    M.REVISAR_EN_TANDA = REVISAR_EN_TANDA
    M.grupo_de = grupo_de
    M.reuso_de = reuso_de
    M.REUSO = OrderedDict()                     # el reuso es por CELDA del Sushi EN y luego por texto (propuesta_de)
    M.FUENTES_CIFRAS = [os.path.join(BP, 'F1-research-us.md'), os.path.join(BP, 'SPEC.md'),
                        os.path.join(BP2, 'F1-research-us-delta.md'), os.path.join(BP2, 'SPEC-delta.md'),
                        os.path.join(PIZ, 'F1-research-us-delta.md'), os.path.join(PIZ, 'SPEC-delta.md'),
                        os.path.join(TAQ, 'F1-research-us-delta.md'), os.path.join(POL, 'F1-research-us-delta.md'),
                        os.path.join(AQUI, 'F1-research-us-delta.md'),
                        os.path.join(AQUI, 'cifras_calculadora.md')]      # caché de la calculadora EN (F2-NOTAS §3)
    M.NOTAS_F2 = os.path.join(AQUI, 'F2-NOTAS.md')
    # G4: el checklist ES de la hamburguesería ya nace con la DV "✓,☐,N/A" (la del Sushi Bar, su semilla) y las 80 celdas OK
    # en «☐»: el EN la copia tal cual; sin la clave «—» → ☐ de los conjuntos taq/pol (F1-camino §6). «bur» no es palabra
    # española: el autotest de ensamblar_docx no necesita el arreglo del «sus»
    completar(M)
