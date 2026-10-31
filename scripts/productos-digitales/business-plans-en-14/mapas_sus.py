#!/usr/bin/env python3
"""
mapas_sus.py — Sushi Restaurant Business Plan Kit (EN) · datos ES→EN del conjunto «sus» (estructura).

Fuente de verdad: `../plan-sushi/F1-camino.md` §6-§7 (EN delta) y `F1-research-us-delta.md` (US §n). Sesión Claude
Code, 31-oct-2026 (F2-EN). NO se ejecuta solo: lo importa `../business-plans-en/mapas.py` cuando `BP_CONJUNTO=sus` y
llama a `instalar(M)`. Clon de `../business-plans-en-13/mapas_pol.py` (Rotisserie EN, el circuito más reciente) con la
REJILLA del Taco EN (`../business-plans-en-12/mapas_taq.py`): el libro ES del sushi bar sale de la TAQUERÍA LIVE
(`../plan-sushi/semilla_sus.py`) con la `ROTACION` ENCENDIDA (medido el 31-oct: mismas celdas; solo 4 fórmulas de texto
distintas, C50, D27, D37 y F13), así que `Break-Even` NO se desplaza (al revés que el `pol`). Van los parches E2 (G14),
E4 (Staffing!C12) y E5 (G11), G13 → 0 y el DICCIONARIO en cadena, sin normalizar:

  0. EN del TACO EN en la MISMA celda (`../business-plans-en-12/textos_es.json` + `textos_en/{GM,GR,GRC,GTAQ-plan,
     GTAQ-check}.json` + `*.revision.json` + `datos_taq.POR_CELDA`); checklist casado por POSICIÓN de pestaña;
  1. EN del Taco EN por TEXTO; 2. EN del ROTISSERIE EN por texto (`../business-plans-en-13/`, mismo ES exacto);
  3. EN de la PIZZA EN por celda y por texto; 4. BAKERY EN; 5. BAR EN; 6. BP/BP2 (GM → REST → CAF → FT).

FUENTE ES: `FUENTE_ES` = `$SUS_FUENTE_ES` o, sin la variable, `astro-site/public/dl/plan-negocio-sushi-bar` (el ES FINAL
y revisado de la F2 ES, `51060183`: no hay paso 1c). Grupos:
  GM          motor común: mismo ES que una cadena GM (Taco EN, Rotisserie EN, Pizza EN, Bar EN o BP) con un EN limpio
              (RX_REESCRIBIR).
  GR · GRC    EN de GTAQ-* / GR / GRC del Taco EN, del Rotisserie EN, de la Pizza EN, de la Bakery, del Bar o de
              REST/CAF/FT: preparar_tandas lo escribe; GR (plan) lo revisa la tanda GSUS-plan (textos_en/GR.revision.json)
              y GRC (solo del checklist) la tanda GSUS-check (textos_en/GRC.revision.json).
  GSUS-plan   nuevas del plan (y las de reuso con vocabulario o caso de otro negocio, con propuesta) + las 12 filas
              D19 (una cadena por celda, sin propuesta).
  GSUS-check  nuevas del checklist (80 tareas). El checklist ES ya nace con la DV «✓,☐,N/A» (parche del 30-oct): sin la
              regla «—» → ☐ de los conjuntos taq/pol.

    python3 bp14.py mapas           # autotest + cruce con censo_es.json + verificar (incluye los sha256)
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

# ==========================================================================
# 0. Producto (F1-camino §6)
# ==========================================================================
FUENTE_ES = os.environ.get('SUS_FUENTE_ES') or 'astro-site/public/dl/plan-negocio-sushi-bar'
PLANES = OrderedDict([
    ('sus', OrderedDict([
        ('slug', 'sushi-restaurant-business-plan'),
        ('producto', 'Sushi Restaurant Business Plan Kit'),
        ('slug_es', 'plan-negocio-sushi-bar'),
        ('dir_es', FUENTE_ES),
        ('env_stripe', 'VITE_STRIPE_PAYMENT_LINK_SUSHI_RESTAURANT_BUSINESS_PLAN'),
        ('keywords', 'sushi restaurant business plan, sushi bar business plan, how to open a sushi restaurant, '
                     'sushi restaurant startup costs, sushi cost per roll, AI Chef Pro'),
    ])),
])
for _p in PLANES.values():
    _p['url'] = 'aichef.pro/en/digital-products/' + _p['slug']
    _p['dir_en'] = 'astro-site/public/dl/' + _p['slug']

LIBROS = OrderedDict([
    ('SUSP', ('sus', 'plan-financiero-sushi-bar.xlsx', 'sushi-restaurant-financial-projections.xlsx',
              'Sushi Restaurant Financial Projections: 3-Year P&L, Cash Flow & Financing')),
    ('SUSC', ('sus', 'checklist-apertura-sushi-bar.xlsx', 'sushi-restaurant-startup-checklist.xlsx',
              'Sushi Restaurant Startup Checklist (80 Tasks)')),
])
DOCX = OrderedDict([
    ('sus', ('plan-de-negocio-sushi-bar.docx', 'sushi-restaurant-business-plan.docx',
             'Sushi Restaurant Business Plan (10 Sections)')),
])
TIPO_DE = {'SUSP': 'plan', 'SUSC': 'check'}
A_TAQ = {'SUSP': 'TAQP', 'SUSC': 'TAQC'}                  # libro del Taco EN (diccionario por celda, nivel 0)
A_PIZ = {'SUSP': 'PIZP', 'SUSC': 'PIZC'}                  # libro de la Pizza EN (diccionario por celda, nivel 3)

# ==========================================================================
# 1. Pestañas: plan = las de la taquería (9, mismos nombres ES); checklist (todas ≤ 31 caracteres; F2 y F3 = US §9)
# ==========================================================================
_HOJAS_PLAN = OrderedDict([
    ('0. Supuestos', '0. Assumptions'), ('Inversión Inicial', 'Startup Costs'), ('PyG 3 Años', '3-Year P&L'),
    ('Punto Equilibrio', 'Break-Even'), ('Escenarios', 'Scenarios'), ('Personal', 'Staffing'),
    ('Instrucciones', 'Instructions'), ('Tesorería 12 meses', '12-Month Cash Flow'), ('Financiación', 'Financing'),
])
_HOJAS_CHECK = OrderedDict([
    ('F1 - Constitución', 'Phase 1 - Business Setup'), ('F2 - Local, frío y extracción', 'Phase 2 - Hood & Permits'),
    ('F3 - Pescado, arroz y sanidad', 'Phase 3 - Raw Fish & Health'),
    ('F4 - Personal y alérgenos', 'Phase 4 - Staff & Allergens'),
    ('F5 - Carta, marca y delivery', 'Phase 5 - Menu, Brand, Delivery'),
    ('F6 - Apertura y 90 días', 'Phase 6 - Opening & 90 Days'), ('Instrucciones', 'Instructions'),
])
assert all(len(v) <= 31 for v in _HOJAS_CHECK.values())
HOJAS_POR_LIBRO = OrderedDict([('SUSP', _HOJAS_PLAN), ('SUSC', _HOJAS_CHECK)])
HOJAS_ES_POR_LIBRO = OrderedDict((c, list(d)) for c, d in HOJAS_POR_LIBRO.items())
TAREAS_POR_FASE = OrderedDict([('SUSC', [12, 15, 14, 13, 13, 13])])          # 80 (F1-camino §4, mismas filas)
MOLDE_CHECK = OrderedDict([('SUSC', 'hojas')])
COL_OK = OrderedDict([('SUSC', 1)])
FASES_CABECERA = OrderedDict()

# Pestañas ES de la taquería y de la pizza en el MISMO orden (el checklist se casa por posición)
_HOJAS_TAQ = {
    'SUSP': list(_HOJAS_PLAN),
    'SUSC': ['F1 - Constitución', 'F2 - Local, humos y gas', 'F3 - Cocina, trompo y sanidad', 'F4 - Personal y alérgenos',
             'F5 - Carta, marca y delivery', 'F6 - Apertura y 90 días', 'Instrucciones'],
}
HOJA_TAQ = {c: dict(zip(HOJAS_ES_POR_LIBRO[c], _HOJAS_TAQ[c])) for c in HOJAS_ES_POR_LIBRO}
_HOJAS_PIZ = {
    'SUSP': list(_HOJAS_PLAN),
    'SUSC': ['F1 - Constitución', 'F2 - Local, humos y licencia', 'F3 - Cocina, horno y sanidad',
             'F4 - Personal y prevención', 'F5 - Carta, marca y delivery', 'F6 - Apertura y 90 días', 'Instrucciones'],
}
HOJA_PIZ = {c: dict(zip(HOJAS_ES_POR_LIBRO[c], _HOJAS_PIZ[c])) for c in HOJAS_ES_POR_LIBRO}

# ==========================================================================
# 2. Fórmulas (= Taco EN y Pizza EN, F1-camino §6): E2 solo G14 (G13 es VALOR en el ES → VALORES_EN 0), E4 (Staffing!C12 =
#    Σ personas × FTE: 4 servers en una fila) y E5 (el literal 0.21 de la línea de bebida → B40)
# ==========================================================================
_E2_ALC = ("('0. Supuestos'!$B$62*'0. Supuestos'!$B$40+(1-'0. Supuestos'!$B$62)*'0. Supuestos'!$B$39)")
PARCHES_FORMULA = OrderedDict([
    (('SUSP', 'PyG 3 Años', 'G14'), (_E2_ALC, "'0. Supuestos'!$B$41")),
    (('SUSP', 'Personal', 'C12'), ('SUM(C5:C11)', 'SUMPRODUCT(B5:B11,C5:C11)')),
    (('SUSP', 'PyG 3 Años', 'G11'), ('H11*0.21', "H11*'0. Supuestos'!$B$40")),
])

# ==========================================================================
# 3. Instrucciones: versión D20 y aviso D21 (E1: SUSP A52, SUSC A12; la tabla D19 del ES tiene 12 filas, 35-46, = la
#    taquería); zona D19 (sin D18) por cabecera
# ==========================================================================
FILA_VERSION = OrderedDict([('SUSP', 51), ('SUSC', 11)])
ZONAS_CELDA = OrderedDict([
    (('SUSP', 'Instrucciones'), [(None, None, 'ABCD', 'D19')]),
])

# ==========================================================================
# 4. Docx: las 131 ranuras del FT ES (= PIZ), H1 en 37·44·51·59·67·76·83·91·100·109; último de §9 = 108 (nota UK);
#    tandas sus_a (§1-5) y sus_b (§6-10), 61 ranuras desde el Word ES final (bp14.py extraer_docx)
# ==========================================================================
DOCX_N_PARRAFOS = OrderedDict([('sus', 131)])
DOCX_ENCABEZADOS = OrderedDict([('sus', [37, 44, 51, 59, 67, 76, 83, 91, 100, 109])])
DOCX_INDICE = OrderedDict([('sus', list(range(24, 34)))])
DOCX_ULTIMO_9 = OrderedDict([('sus', '108')])
DOCX_TANDAS = OrderedDict([('sus_a', ('sus', [1, 2, 3, 4, 5])), ('sus_b', ('sus', [6, 7, 8, 9, 10]))])
PRESTAMO_SEMILLA = OrderedDict([('sus', 248000)])                   # research US §8: ≈ $248,000 (punto fijo en F2)

AUTOTEST = OrderedDict([
    ('P1', 'SUSP'), ('P2', 'SUSP'), ('C1', 'SUSC'), ('C2', 'SUSC'),
    ('C1_hoja_papel', 'F2 - Local, frío y extracción'), ('C1_titulo', 'Sushi Restaurant Startup Checklist (80 Tasks)'),
    ('C2_hoja_no_latino', 'F5 - Carta, marca y delivery'), ('P1_celda_texto', 'A3'), ('P1_celda_formula', 'B9'),
    ('P1_merge', 'A30:C30'),
])

# ==========================================================================
# 5. Grupos (= heladería: GR del plan y GRC del checklist)
# ==========================================================================
GRUPOS = ('GM', 'GR', 'GRC', 'GSUS-plan', 'GSUS-check')
GRUPOS_TRADUCTORES = ('GSUS-plan', 'GSUS-check')
GRUPOS_OVERRIDES = ('GSUS-plan', 'GSUS-check')
REVISAR_EN_TANDA = OrderedDict([('GSUS-plan', ('GR',)), ('GSUS-check', ('GRC',))])
GRUPOS_DESC = OrderedDict([
    ('GM', 'REUTILIZADAS: motor común (mismo ES que una cadena GM del Taco EN, de la Pizza EN, del Bar EN o de BP) con un '
           'EN sin vocabulario ni caso de otro negocio. preparar_tandas escribe su EN. No van a los traductores'),
    ('GR', 'REUTILIZADAS con revisión (plan): EN de GTAQ-* / GR / GRC del Taco EN, de GPIZ-* de la Pizza EN, de la Bakery '
           'EN, del Bar EN o de REST/CAF/FT (y lo casado con «pedido» ↔ «comensal»). preparar_tandas escribe su EN; la '
           'tanda GSUS-plan las revisa en textos_en/GR.revision.json'),
    ('GRC', 'REUTILIZADAS con revisión (solo del checklist): EN del Taco EN o de la Pizza EN (plazos, responsables, '
            'cabeceras, tareas). preparar_tandas escribe su EN; la tanda GSUS-check las revisa en '
            'textos_en/GRC.revision.json'),
    ('GSUS-plan', 'Nuevas del plan financiero (SUSP) + las de reuso con vocabulario o caso de otro negocio (con '
                  'propuesta) + las 12 filas D19 de Instrucciones (una cadena por celda, sin propuesta)'),
    ('GSUS-check', 'Nuevas del checklist (SUSC): las 80 tareas, sus cabeceras y los mensajes de la DV (con propuesta '
                   'cuando el Taco EN o la Pizza EN tienen el mismo ES)'),
    ('GX', 'NO se traduce: pestañas (mapas.HOJAS_POR_LIBRO), CLAVES, FIJOS, POR_CELDA, versión, pie y docProps'),
])

# Vocabulario y caso del TACO, el ROTISSERIE, la PIZZA, la PANADERÍA y el BAR que NO vale para el sushi bar: clasifica las
# PROPUESTAS (no es el gate: ese es datos_sus.RX_SUS_NO). Una propuesta sucia va a los traductores con su EN como forma.
# «covers», «seat turns», «servers», «hood», «griddle», «beer & wine», «liquor liability», «pickup» y «closed Mondays» SÍ
# valen en el sushi bar (US §1 y §8: servicio en mesa, abre 6 días). «115 covers» y «40 seats» también: coinciden con el
# caso US del sushi (no se vetan aunque sean del Taco o del Rotisserie)
_CASO_OTROS = (r'669,600|709,776|738,167|242,550|329,274|86,724|217,300|39,275|\$36(?:\.00)?\b|\$38\.88|'
               r'619,850|657,041|683,323|176,000|197,600|275,612|\b308\b|\$2,800\b|\b1,200 sq ft\b|'
               r'819,000|868,140|902,866|216,000|237,832|335,708|\b130 covers\b|\b360\b|\$3,733\b|\b1,600 sq ft\b|'
               r'\$17\.50\b|\b62 covers\b|\b50 seats\b|\b30 seats\b|\b1,500 sq ft\b')
RX_REESCRIBIR = re.compile(
    r'(?i)\bpizz|\bdough\b|\bovens?\b|Neapolitan|\bVPN\b|firewood|wood-fired|\bflue\b|spark arrestor|\bpeels?\b|'
    r'hearth|mozzarella|San Marzano|Margherita|\b00 flour|\btapas\b|'
    r'small plates|\bcocktails?\b|\bspirits\b|\bbartend|happy hour|full liquor|\bbread\b|\bbakery\b|\bbakers?\b|'
    r'\bloa(?:f|ves)\b|pastr(?:y|ies)|croissant|transactions?(?:/day| per day| a day)|'
    r'\btacos?\b|taquer|trompo|al pastor|\bpastor\b|tortill|\bmasa\b|nixtamal|salsa bar|quesadilla|\bgringas?\b|'
    r'carnitas|birria|suadero|aguas? frescas?|horchata|jamaica|Cinco de Mayo|Mexican beer|\bcomal\b|'
    r'guac|pico de gallo|salsa macha|pork shoulder|vertical broiler|\bpatio\b|'
    r'rotisserie|chicken|\bbirds?\b|\bspits?\b|yuca|family meals?|pollo|Peruvian|\baji\b|huancaina|chicha|maduros|'
    r'salchipapa|heated display|marinade|counter service|no servers|without servers|\bkiosk|fried chicken|' + _CASO_OTROS)

# sha256 de los diccionarios del Taco EN (LIVE bf18ff72, con los textos corregidos en #186 554d962c), del Rotisserie EN
# (LIVE 26e618f8 + #186) y de la Pizza EN (+ #186), medidos el 31-oct sobre 51060183. Si cambian, hay que re-extraer y
# rehacer preparar_tandas (bp14.py verificar avisa)
SHA_TAQ = OrderedDict([
    ('textos_es.json', 'e0a469d45ad3668226661c97d5eea89000400e9eb42e40d0c02c20931a92d584'),
    ('textos_en/GM.json', '17bceb7b136363c3869b5e713fac64e6972bd87114bd45db58a993c08d23a877'),
    ('textos_en/GM.revision.json', 'bfc5dfa013ee8661d33e1181fcafdea1c291c8f2d23068dc1c1c967f72905d6e'),
    ('textos_en/GR.json', 'ead32eecbe8cd17532ce8e8a560d9ffc22aa91bd16a921e931792441fc0b5b27'),
    ('textos_en/GR.revision.json', 'b632ba77785bcebb14d96c666f4b91b8d3f2d12837ef1220cb30aec18f855682'),
    ('textos_en/GRC.json', 'e7ddfab10026b9c4f735338cab31f63c504f479661453f4bd79839052f81ebc1'),
    ('textos_en/GRC.revision.json', 'cda1d04f28213288b2ab41607b4415100005b3224c96f7aeb7416fa520f50f9b'),
    ('textos_en/GTAQ-plan.json', 'e2fdac65fca460a019411ea99c7c01c92bd4ec8af9cf8f3d8ed1c9eecab2a014'),
    ('textos_en/GTAQ-check.json', '33ab5e40c525f126e37f3ae67b51defa00631e3048ce51e945f61d313e4effd6'),
    ('formulas_taq.json', '32ebc9b30708271f45ec8c6534da31cef637b108f7e3228ecd52e4559fd05c10'),
    ('censo_es.json', '633aaaa18ef07b790e1b5791c919fc9269fa29044608661147abd2f37f69a8b9'),
    ('datos_taq.py', '0f0342a6eaf357eb8b97aba07c74a9f80548034b86bb48a30a6d7bdf877185ab'),
])
SHA_POL = OrderedDict([
    ('textos_es.json', 'f39efae33c6742303aefbf873ee81b6badef64d0b236ff4b0d94db971dd1fd5b'),
    ('textos_en/GM.json', '007679a592c311b2f11519c696ab3d52d1699b154d06252c2683f4159a3946ec'),
    ('textos_en/GR.json', '764fabde7a5f42a4091f0405bf4811c328cf840eeebe46b509d5853272a6c34e'),
    ('textos_en/GR.revision.json', '9141fde9272e0fa6d3a239f3b84020c5d47a4e927977ba307b24d27f6c02658b'),
    ('textos_en/GRC.json', 'ab0546ed982b4d69aa99064544c2c04f5bcccb495461fd82ce8ff36401094199'),
    ('textos_en/GRC.revision.json', 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356'),
    ('textos_en/GPOL-plan.json', '61814c88bd87215d9a341147816fbefbbd848e7fcefc20e0d90f79c27c1686bf'),
    ('textos_en/GPOL-check.json', 'f4b33e4997c124695850f19acc9d4b8943fd77e5e3bc23de7f9e5378f967fc58'),
])
SHA_PIZ = OrderedDict([
    ('textos_es.json', 'c477dc83a61609ec7de3ebe3d23937b27267c7e48000d389271e382ad630319b'),
    ('textos_en/GM.json', '0f6cd4198a3c533331cca1111dde7a5de26c87b173e0d2712abafac72e6c08ed'),
    ('textos_en/GR.json', 'ef088edc5b1709acd9ad28ab3f5d7023a6421f505fc0d0dfedb63a7f099e8151'),
    ('textos_en/GM.revision.json', 'b6d5e7768ba1fa4240dd3c055355db4fc17559b3eec0249f57978cbf574d7876'),
    ('textos_en/GR.revision.json', 'fc7cfb4e679c7f30c5571381cc72b9d4bec3094283172fdb5c30e508147941d0'),
    ('textos_en/GPIZ-plan.json', 'a52044a121fd9e28c7931534c3ee54adabe856a186c543c5f13e6aa08a7dc3b6'),
    ('textos_en/GPIZ-check.json', 'c3d62514b899edb9d0aa9a1c32fcaa3517a22229fe4121bd72d2b978d43556da'),
    ('formulas_piz.json', '286b3675b30e2eed71982781e209f4aa063fe4c8be2e7c616ebbd54877caebb2'),
    ('censo_es.json', '2c8a1f63f2b5de0db1d46794327831bc16405744f5fe6e8b0ddc68286708b933'),
    ('datos_piz.py', '44c178d7bb9ae94eb696f26d8f964ba98f510e275e4104ce5baece71e1d2158e'),
])
# sha256 del ES FINAL (F2 ES revisada y regenerada, 51060183 = plan-sushi/REVISION-FINAL.md; Mac = VPS el 31-oct): si el
# ES cambia, manda el ES nuevo (re-extraer y avisar)
SHA_ES = OrderedDict([
    ('plan-financiero-sushi-bar.xlsx', '9d6c2fdc314de00507180d30cb3bb68ff57c2c929b091849229c7c6e712c6f6c'),
    ('checklist-apertura-sushi-bar.xlsx', 'db87cd9e4c05c467840822ced9de33b73b4e70c93a6a5cdb192a9c1923ab7030'),
    ('plan-de-negocio-sushi-bar.docx', 'ac6a4994f526bff56a2ac0d35082467f6933a1e4bd123d627d684b2723d3b368'),
])


def _sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def diccionario_ok():
    """[] si los ficheros de los diccionarios del Taco EN, del Rotisserie EN y de la Pizza EN siguen con su sha256."""
    out = []
    for carpeta, nombre, shas in ((TAQ, 'business-plans-en-12', SHA_TAQ), (POL, 'business-plans-en-13', SHA_POL),
                                  (PIZ, 'business-plans-en-8', SHA_PIZ)):
        for rel, sha in shas.items():
            p = os.path.join(carpeta, rel)
            if not os.path.exists(p):
                out.append('%s/%s: falta' % (nombre, rel))
            elif _sha(p) != sha:
                out.append('%s/%s: sha256 distinto del fijado en mapas_sus' % (nombre, rel))
    return out


# ==========================================================================
# 6. Diccionario: Taco EN por celda → por texto → Rotisserie EN por texto → Pizza EN por celda → por texto → Bakery →
#    Bar → BP/BP2
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
    por_celda = _modulo('%s_ref_sus' % datos, os.path.join(carpeta, datos + '.py')).POR_CELDA
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


_ET_TAQ = 'business-plans-en-12 (Taco EN cerrada)'
_ET_PIZ = 'business-plans-en-8 (Pizza EN cerrada)'
_ET_POL = 'business-plans-en-13 (Rotisserie EN cerrada)'
TAQ_CELDA, TAQ_TEXTO = _cargar_celda(TAQ, ('GM', 'GR', 'GRC', 'GTAQ-plan', 'GTAQ-check'), 'datos_taq', _ET_TAQ)
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
_GM_ORIGEN = {(_ET_TAQ, 'GM'), (_ET_POL, 'GM'), (_ET_PIZ, 'GM'), ('business-plans-en-3 (Bar EN)', 'GM'),
              ('business-plans-en (GM)', 'GM')}


def _celdas(e):
    return [o for o in e['donde'] if o.get('t') == 'celda']


def _por_celda(dic, libros, hojas, celdas, es):
    gem = [dic.get((libros.get(o['f']), hojas.get(o['f'], {}).get(o['h']), o['c'])) for o in celdas]
    if celdas and all(x is not None and x['es'] == es for x in gem) and len({x['en'] for x in gem}) == 1:
        return OrderedDict(gem[0])
    return None


def propuesta_de(e):
    """(entrada de reuso, origen) de una cadena del sushi bar, o (None, None). origen: 'celda-taq', 'texto-taq',
    'texto-pol', 'celda-piz', 'texto-piz', 'texto-pan', 'texto-bar', 'texto-bp'."""
    es = e['es']
    celdas = _celdas(e)
    x = _por_celda(TAQ_CELDA, A_TAQ, HOJA_TAQ, celdas, es)
    if x:
        return x, 'celda-taq'
    if es in TAQ_TEXTO:
        return TAQ_TEXTO[es], 'texto-taq'
    if es in POL_TEXTO:
        return POL_TEXTO[es], 'texto-pol'
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
    destino = 'GSUS-check' if libros == {'SUSC'} else 'GSUS-plan'
    if any(o.get('det') == 'D19' for o in donde):
        return 'GSUS-plan'                                   # las 12 filas D19 cambian enteras
    if tratamiento != 'traducir':
        return destino
    prop, origen = propuesta_de({'es': texto, 'donde': donde})
    if not prop or not _limpia(prop['en']):
        return destino
    if (prop.get('conjunto'), prop['grupo']) in _GM_ORIGEN:
        return 'GM'
    return 'GRC' if libros == {'SUSC'} else 'GR'


def reuso_de(e):
    """EN del diccionario (GM / GR) o PROPUESTA para los traductores. D19: sin propuesta."""
    if any(o.get('det') == 'D19' for o in e['donde']) or e['tratamiento'] != 'traducir':
        return None
    prop, origen = propuesta_de(e)
    if not prop:
        return None
    libros = A_TAQ if origen.endswith('-taq') else A_PIZ
    hojas = HOJA_TAQ if origen.endswith('-taq') else HOJA_PIZ
    donde = prop.get('donde') or ['%s %s!%s' % (libros.get(o['f']), hojas.get(o['f'], {}).get(o.get('h'), ''),
                                                o.get('c', '')) for o in _celdas(e)[:2]]
    return OrderedDict([('grupo', prop['grupo']), ('id', prop['id']), ('en', prop['en']),
                        ('tratamiento_origen', prop['tratamiento_origen']),
                        ('conjunto', prop.get('conjunto', _ET_PIZ)), ('origen', origen), ('donde', donde)])


# ==========================================================================
# instalar
# ==========================================================================
def instalar(M):
    """Sustituye en el módulo `mapas` (M) los datos de FT/CAF por los del sushi bar."""
    from datos_sus import completar                                        # contenido (FIJOS, caso US, docx…)
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
    M.REUSO = OrderedDict()                     # el reuso es por CELDA del Taco EN y luego por texto (propuesta_de)
    M.FUENTES_CIFRAS = [os.path.join(BP, 'F1-research-us.md'), os.path.join(BP, 'SPEC.md'),
                        os.path.join(BP2, 'F1-research-us-delta.md'), os.path.join(BP2, 'SPEC-delta.md'),
                        os.path.join(PIZ, 'F1-research-us-delta.md'), os.path.join(PIZ, 'SPEC-delta.md'),
                        os.path.join(TAQ, 'F1-research-us-delta.md'), os.path.join(POL, 'F1-research-us-delta.md'),
                        os.path.join(AQUI, 'F1-research-us-delta.md'),
                        os.path.join(AQUI, 'cifras_calculadora.md')]      # caché de la calculadora EN (F2-NOTAS §3)
    M.NOTAS_F2 = os.path.join(AQUI, 'F2-NOTAS.md')
    # G4: el checklist ES del sushi bar ya nace con la DV "✓,☐,N/A" (parche del 30-oct en la semilla, medido el 31-oct) y
    # las 80 celdas OK en «☐»: el EN la copia tal cual; sin la clave «—» → ☐ de los conjuntos taq/pol (F1-camino §6).
    # Sin términos con artículos del español que retirar del detector de restos (la jerga japonesa no los lleva)
    completar(M)
