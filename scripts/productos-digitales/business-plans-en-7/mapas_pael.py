#!/usr/bin/env python3
"""
mapas_pael.py — Paella Catering Business Plan Kit (EN) · datos ES→EN del conjunto «pael» (estructura).

SPEC: `SPEC-delta.md` (D114-D132) sobre las heredadas (`../business-plans-en-6/SPEC-delta.md` D96-D113, `-5/` D81-D95,
`-4/` D66-D80, `-3/` D48-D65, `-2/` D30-D47, `../business-plans-en/SPEC.md` D1-D29). Sesión Claude Code, 24-oct-2026
(F2, paso 1). NO se ejecuta solo: lo importa `../business-plans-en/mapas.py` cuando `BP_CONJUNTO=pael` y llama a
`instalar(M)`. Clon de `../business-plans-en-6/mapas_bbq.py` (D119).

Como el BBQ: la FUENTE ES DEL CIRCUITO es el FOOD TRUCK ES (ranuras de celdas y párrafos) y el motor es el de eventos
(B4 = eventos/año, B5 = precio por invitado, B6 = invitados por evento; los 7 parches, con el Break-Even en ±$3 / +$6).
El DICCIONARIO DE REUSO POR CELDA va EN CADENA (D119): primero el EN del BBQ en ESA celda (`../business-plans-en-6/
textos_es.json` + `textos_en/{GM,GRC-plan,GBQ-plan,GBQ-check}.json` con `GRC-plan.revision.json` encima; 8 sha256 en
SHA_BBQ) y, si el BBQ no tiene EN en esa celda, el EN publicado del catering (los mismos 8 sha256 de mapas_bbq): 16 en
total, que `bp7.py verificar` comprueba (D132: si el BBQ deriva, avisa y hay que rehacer preparar_tandas).

    python3 bp7.py mapas            # autotest + cruce con censo_es.json + verificar (incluye los 16 sha256)

Grupos (D119 + «solo lo que de verdad cambia», orden del orquestador del paso 1):
  GM          motor común cuyo EN (BBQ = catering) no trae vocabulario que no valga para la paella: no va a nadie.
  GRB-plan    EN del BBQ (o del catering) reutilizable con revisión (notas del plan, tabla D18, las filas D19 con
              propuesta limpia): preparar_tandas escribe su EN; la tanda GPA-plan las revisa (GRB-plan.revision.json).
  GPA-plan    se escriben para la paella: las del plan cuyo EN del BBQ trae vocabulario o caso BBQ (RX_REESCRIBIR), las
              51 forzadas (notas del caso), las sin EN y las celdas D19 sin propuesta o con propuesta sucia.
  GLB-check   checklist: celdas cuya propuesta del BBQ vale tal cual (tareas «L» y las columnas que no cambian de las
              «A»; la columna C con «Pitmaster» → «Paella chef», transformación mecánica de D125): no van a nadie.
  GPA-check   checklist: las celdas que cambian (vocabulario BBQ, columnas marcadas de las tareas «A» y las 4 de las «N»).
"""
import hashlib
import json
import os
import re
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
BP = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
CAT = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')
BBQ = os.path.join(os.path.dirname(AQUI), 'business-plans-en-6')

# ==========================================================================
# 0. Producto (D114-D116). dir_es = FUENTE DEL CIRCUITO (food truck ES); slug_es = gemelo ES para hreflang (D114)
# ==========================================================================
PLANES = OrderedDict([
    ('pael', OrderedDict([
        ('slug', 'paella-catering-business-plan'),
        ('producto', 'Paella Catering Business Plan Kit'),
        ('slug_es', 'plan-negocio-paellero-eventos'),
        ('dir_es', 'astro-site/public/dl/plan-negocio-food-truck'),
        ('env_stripe', 'VITE_STRIPE_PAYMENT_LINK_PAELLA_CATERING_BUSINESS_PLAN'),
        ('keywords', 'paella catering business plan, paella business plan, how to start a paella catering business, '
                     'spanish catering business plan, paella catering prices, paella party, AI Chef Pro'),
    ])),
])
for _p in PLANES.values():
    _p['url'] = 'aichef.pro/en/digital-products/' + _p['slug']
    _p['dir_en'] = 'astro-site/public/dl/' + _p['slug']

LIBROS = OrderedDict([
    ('PAEP', ('pael', 'plan-financiero-food-truck.xlsx', 'paella-catering-financial-projections.xlsx',
              'Paella Catering Financial Projections: 3-Year P&L, Cash Flow & Financing')),
    ('PAEC', ('pael', 'checklist-apertura-food-truck.xlsx', 'paella-catering-startup-checklist.xlsx',
              'Paella Catering Startup Checklist (68 Tasks)')),
])
DOCX = OrderedDict([
    ('pael', ('plan-de-negocio-food-truck.docx', 'paella-catering-business-plan.docx',
              'Paella Catering Business Plan (10 Sections)')),
])
TIPO_DE = {'PAEP': 'plan', 'PAEC': 'check'}
A_BBQ = {'PAEP': 'BBQP', 'PAEC': 'BBQC'}                  # libro del BBQ que hace de diccionario (1.º de la cadena)
A_CAT = {'PAEP': 'CATP', 'PAEC': 'CATC'}                  # libro del catering (2.º de la cadena)

# ==========================================================================
# 1. Pestañas: plan = FT; checklist = FT con la fase 2 «Propane & Permits» (D125: 27 caracteres ≤ 31; el título de la
#    hoja, sin límite, es «PHASE 2: COMMISSARY, PROPANE STATION, FIRE RULES & PERMITS»)
# ==========================================================================
_HOJAS_PLAN = OrderedDict([
    ('0. Supuestos', '0. Assumptions'), ('Inversión Inicial', 'Startup Costs'), ('PyG 3 Años', '3-Year P&L'),
    ('Punto Equilibrio', 'Break-Even'), ('Escenarios', 'Scenarios'), ('Personal', 'Staffing'),
    ('Instrucciones', 'Instructions'), ('Tesorería 12 meses', '12-Month Cash Flow'), ('Financiación', 'Financing'),
])
HOJA_F2_EN = 'Phase 2 - Propane & Permits'
assert len(HOJA_F2_EN) <= 31
_HOJAS_CHECK = OrderedDict([
    ('F1 - Constitución', 'Phase 1 - Business Setup'), ('F2 - Vehículo', HOJA_F2_EN),
    ('F3 - Equipamiento', 'Phase 3 - Equipment'), ('F4 - Personal', 'Phase 4 - Staff'),
    ('F5 - Marketing', 'Phase 5 - Marketing'), ('F6 - 90 Días', 'Phase 6 - First 90 Days'),
    ('Instrucciones', 'Instructions'),
])
HOJAS_POR_LIBRO = OrderedDict([('PAEP', _HOJAS_PLAN), ('PAEC', _HOJAS_CHECK)])
HOJAS_ES_POR_LIBRO = OrderedDict((c, list(d)) for c, d in HOJAS_POR_LIBRO.items())
TAREAS_POR_FASE = OrderedDict([('PAEC', [11, 13, 12, 10, 12, 10])])          # 68 (D125 = rejilla del BBQ)
MOLDE_CHECK = OrderedDict([('PAEC', 'hojas')])
COL_OK = OrderedDict([('PAEC', 1)])
FASES_CABECERA = OrderedDict()
FILAS_TAREA = OrderedDict([('F1 - Constitución', (5, 15)), ('F2 - Vehículo', (5, 17)), ('F3 - Equipamiento', (5, 16)),
                           ('F4 - Personal', (5, 14)), ('F5 - Marketing', (5, 16)), ('F6 - 90 Días', (5, 14))])

# ==========================================================================
# 2. Fórmulas: los 7 parches del BBQ sin cambios (D119: Break-Even ±$3 / +$6; B5 = $40)
# ==========================================================================
_E2_ALC = ("('0. Supuestos'!$B$62*'0. Supuestos'!$B$40+(1-'0. Supuestos'!$B$62)*'0. Supuestos'!$B$39)")
PARCHES_FORMULA = OrderedDict([
    (('PAEP', 'PyG 3 Años', 'G13'), ("'0. Supuestos'!$B$39", "'0. Supuestos'!$B$41")),
    (('PAEP', 'PyG 3 Años', 'G14'), (_E2_ALC, "'0. Supuestos'!$B$41")),
    (('PAEP', 'Personal', 'B20'), ("'0. Supuestos'!$B$6", "'0. Supuestos'!$B$4")),
    (('PAEP', 'Personal', 'C9'), ('SUM(C5:C8)', 'SUMPRODUCT(B5:B8,C5:C8)')),
    (('PAEP', 'Punto Equilibrio', 'B31'), ('$B$8-2', '$B$8-3')),
    (('PAEP', 'Punto Equilibrio', 'D31'), ('$B$8+2', '$B$8+3')),
    (('PAEP', 'Punto Equilibrio', 'E31'), ('$B$8+4', '$B$8+6')),
])

# ==========================================================================
# 3. Instrucciones: versión D20 y aviso D21; zonas celda a celda: D18 (35-51), D19 (55-68) y las 68 tareas (B-E)
# ==========================================================================
FILA_VERSION = OrderedDict([('PAEP', 73), ('PAEC', 11)])
ZONAS_CELDA = OrderedDict([(('PAEP', 'Instrucciones'), [(35, 51, 'ABCD', 'D18'), (55, 68, 'ABCD', 'D19')])])
for _h, (_f1, _f2) in FILAS_TAREA.items():
    ZONAS_CELDA[('PAEC', _h)] = [(_f1, _f2, 'BCDE', 'TAREA')]

# ==========================================================================
# 4. Docx (D126): las 131 ranuras del FT ES, H1 en 37·44·51·59·67·76·83·91·100·109; último de §9 = 108 (nota UK)
# ==========================================================================
DOCX_N_PARRAFOS = OrderedDict([('pael', 131)])
DOCX_ENCABEZADOS = OrderedDict([('pael', [37, 44, 51, 59, 67, 76, 83, 91, 100, 109])])
DOCX_INDICE = OrderedDict([('pael', list(range(24, 34)))])
DOCX_ULTIMO_9 = OrderedDict([('pael', '108')])
DOCX_TANDAS = OrderedDict([('pael_a', ('pael', [1, 2, 3, 4, 5])), ('pael_b', ('pael', [6, 7, 8, 9, 10]))])
PRESTAMO_SEMILLA = OrderedDict([('pael', 64000)])                   # punto fijo del dry-run (research §8: ≈ $62,400)

AUTOTEST = OrderedDict([
    ('P1', 'PAEP'), ('P2', 'PAEP'), ('C1', 'PAEC'), ('C2', 'PAEC'),
    ('C1_hoja_papel', 'F2 - Vehículo'), ('C1_titulo', 'Paella Catering Startup Checklist (68 Tasks)'),
    ('C2_hoja_no_latino', 'F5 - Marketing'), ('P1_celda_texto', 'A3'), ('P1_celda_formula', 'B9'),
    ('P1_merge', 'A30:C30'),
])

# ==========================================================================
# 5. Grupos (D119 + «solo lo que cambia»)
# ==========================================================================
GRUPOS = ('GM', 'GRB-plan', 'GLB-check', 'GPA-plan', 'GPA-check')
GRUPOS_TRADUCTORES = ('GPA-plan', 'GPA-check')
GRUPOS_OVERRIDES = ('GPA-plan', 'GPA-check')
REVISAR_EN_TANDA = OrderedDict([('GPA-plan', ('GRB-plan',))])
GRUPOS_DESC = OrderedDict([
    ('GM', 'REUTILIZADAS: motor común cuyo EN (el del BBQ, que es el del Catering publicado) no trae vocabulario ni caso '
           'del BBQ. preparar_tandas escribe su EN. No van a los redactores'),
    ('GRB-plan', 'REUTILIZADAS con revisión: EN del BBQ (o del Catering) en ESA celda que vale para un paella caterer '
                 'salvo matices (notas del plan, método D18, filas D19 con propuesta limpia). preparar_tandas escribe su '
                 'EN; la tanda GPA-plan las revisa en textos_en/GRB-plan.revision.json (solo las que cambian)'),
    ('GLB-check', 'REUTILIZADAS tal cual: celdas del checklist cuya propuesta del BBQ vale para la paella (tareas que '
                  'sobreviven y columnas que no cambian; «Pitmaster» → «Paella chef» en la columna C). No van a nadie'),
    ('GPA-plan', 'Plan financiero (PAEP) que se ESCRIBE para el paella caterer: celdas cuyo EN del BBQ trae vocabulario '
                 'o caso BBQ (propuesta = ese EN), las 51 forzadas (notas del caso), las sin EN y las celdas D19 sin '
                 'propuesta (8 filas nuevas) o con propuesta sucia'),
    ('GPA-check', 'Checklist (PAEC): las celdas que CAMBIAN de las 68 tareas (columnas marcadas de las tareas que se '
                  'ajustan, las 4 de las 3 nuevas y toda celda con vocabulario BBQ), con la propuesta del BBQ'),
    ('GX', 'NO se traduce: pestañas (mapas.HOJAS_POR_LIBRO), CLAVES, FIJOS, POR_CELDA, versión, pie y docProps'),
])

# Vocabulario y caso del BBQ (y lo que sigue vetado del catering) que NO vale para un paella caterer (F1-inventario §1).
# Clasifica las PROPUESTAS, no es el gate (RX_PAEL_NO de datos_pael). Salen frente al BBQ: burners, stations y «chef»
# precedido de «paella»; la van (usada, de carga) sí vale
_CASO_BBQ = (r'427,500|478,800|517,104|135,671|101,000|83,300|52,371|29,816|60,367|\b150 events\b|\$38(?:\.00)?\b|'
             r'\b75 guests\b|\b128 events\b|\b220 events\b|\$2,850')
RX_REESCRIBIR = re.compile(
    r'(?i)\bsmok|\bpitmasters?\b|\bpits?\b|brisket|pulled pork|\bribs?\b|\bbark\b|live[- ]fire|\bmeats?\b|'
    r'\bcarv(?:e|ed|ing|er|ers)\b|\btrailers?\b|tow vehicle|\bpickup\b|whole hog|pig roast|tri-tip|picanha|\basado\b|'
    r'churrasco|butcher paper|\brubs?\b|\bBBQ\b|barbecue|\bgrill|\bwood\b|charcoal|pellet|sausage|\bsides\b|'
    r'Santa Maria|parrilla|Caja China|Texas|burnt ends|\bhot ?box|'
    r'\bplated\b|family-style|chef-attended|\bthemed\b|(?<!AI )(?<!paella )\bchefs?\b|\bsous\b|owner-chef|induction|'
    r'\bovens?\b|reach-in|\btaco|\bpasta\b|cuisine|\bcoffee\b|refrigerat|generator|' + _CASO_BBQ)

# sha256 del diccionario en cadena (D119/D132): 8 del BBQ cerrado (`../business-plans-en-6/`, fijados el 24-oct-2026
# sobre 4610f8da) + los 8 del catering publicado (`../business-plans-en-4/`, los mismos que mapas_bbq)
SHA_BBQ = OrderedDict([
    ('textos_es.json', '7c9c8ce0afb478dc48076740d3b5dad7094162cf7dfba2d6cef50e263d4f0d88'),
    ('textos_en/GM.json', 'd9a2a597eccff769d34461c2a797f25973d569c1f96bff2ea20db7e6dbaa6943'),
    ('textos_en/GRC-plan.json', '123034ac4137fe8b266bca8873012f86d421d40d6dfca8a527b649568a4f60e5'),
    ('textos_en/GRC-plan.revision.json', '7bd6735fe4a6fd5a3c02c4cb30bfec482728cdee852e4eb3dad54bab75a11081'),
    ('textos_en/GBQ-plan.json', '65a13976b21ff44ff0f593cef5565378e382295cbb09c5ceb1d5f7089798f49c'),
    ('textos_en/GBQ-check.json', 'ebdf155fde86faaa48b5b5f439dcdfcadee296b6aeda19ac2b44f0f1b318e26b'),
    ('docx_en_bbq_a.json', '25c0a2155029938ef385e310d39eaf8e73b1b261e9781f2aa56c8c36579e4287'),
    ('docx_en_bbq_b.json', '102f7417b4b1a8440acab3c9642842c59e17d5391b273a0dfe77fc87cc512e67'),
])
SHA_DICCIONARIO = OrderedDict([
    ('textos_es.json', '9d02ffbeb6c088ae84f5f1ad80364a7f0e1bcb1ad264d8c57a16739b64f574f1'),
    ('textos_en/GM.json', 'b05fd56a3ed3eb562b7eb1dcc114e751f14d525ec0feefc7151388ede96c35d1'),
    ('textos_en/GR.json', '7e2e0f23be5f1d6f9e2e8cc5d60def04fd15030a7d1ea6d677ea7f8942b883ea'),
    ('textos_en/GR.revision.json', '976190192b0c069cad212a5c7e40a5dc2761917cc5a920edfd6f8fff3097b13e'),
    ('textos_en/GCAT-plan.json', '849c96d84281bd39825fac07cae8668b9f8a61d7549f2030e6d2e3725d2b569e'),
    ('textos_en/GCAT-check.json', '56399ef7fc4ecc9ab667b0f719243062c605d100a54025f4dfc247226af61104'),
    ('docx_en_cat_a.json', '2afccc350b8046f5567e0d990245a054f2530dfb2914fccb51d6d4213a3d7252'),
    ('docx_en_cat_b.json', '858fcf7d3119a7d87be2bf550c3c7fc9753a020d2c83f7a6d8d9183da7873728'),
])
_GRUPOS_BBQ = ('GM', 'GRC-plan', 'GBQ-plan', 'GBQ-check')
_GRUPOS_CAT = ('GM', 'GR', 'GCAT-plan', 'GCAT-check')


def _sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def diccionario_ok():
    """[] si los 16 ficheros del diccionario en cadena (8 del BBQ + 8 del catering) siguen con el sha256 fijado; si no,
    la lista de los que cambiaron (hay que re-extraer y rehacer preparar_tandas antes de los redactores, D132)."""
    out = []
    for base, tabla, nombre in ((BBQ, SHA_BBQ, 'SHA_BBQ'), (CAT, SHA_DICCIONARIO, 'SHA_DICCIONARIO')):
        for rel, sha in tabla.items():
            p = os.path.join(base, rel)
            if not os.path.exists(p):
                out.append('%s/%s: falta' % (os.path.basename(base), rel))
            elif _sha(p) != sha:
                out.append('%s/%s: sha256 distinto del fijado en mapas_pael.%s' % (os.path.basename(base), rel, nombre))
    return out


def _en_de(base, grupos, revision):
    en = OrderedDict()
    for g in grupos:
        p = os.path.join(base, 'textos_en', g + '.json')
        if os.path.exists(p):
            en.update(json.load(open(p, encoding='utf-8')))
    rev = os.path.join(base, 'textos_en', revision)
    if os.path.exists(rev):
        en.update(json.load(open(rev, encoding='utf-8')))             # ya va dentro del .json; idempotente
    return en


# Transformación mecánica de la columna C del checklist (D125): «Pitmaster» → «Paella chef»
RX_COL_C = re.compile(r'[A-Z]+')


def _mecanica(f, c, en):
    if f == 'BBQC' and RX_COL_C.match(c or '') and RX_COL_C.match(c).group(0) == 'C':
        return en.replace('Pitmaster', 'Paella chef')
    return en


def _cargar(base, grupos, revision, libros, plan_etq):
    te_p = os.path.join(base, 'textos_es.json')
    celda, texto = OrderedDict(), OrderedDict()
    if not os.path.exists(te_p):
        return celda, texto
    en = _en_de(base, grupos, revision)
    for c in json.load(open(te_p, encoding='utf-8'))['cadenas']:
        if c['grupo'] not in grupos or c['id'] not in en:
            continue
        for d in c['donde']:
            if d.get('t') != 'celda' or d['f'] not in libros:
                continue
            celda[(d['f'], d['h'], d['c'])] = (_mecanica(d['f'], d['c'], en[c['id']]), c['grupo'], c['id'],
                                               c['tratamiento'])
        if plan_etq in c.get('planes', []):
            texto.setdefault(c['es'], (en[c['id']], c['grupo'], c['id'], c['tratamiento']))
    return celda, texto


BBQ_CELDA, BBQ_TEXTO = _cargar(BBQ, _GRUPOS_BBQ, 'GRC-plan.revision.json', ('BBQP', 'BBQC'), 'bbq')
CAT_CELDA, CAT_TEXTO = _cargar(CAT, _GRUPOS_CAT, 'GR.revision.json', ('CATP', 'CATC'), 'cat')
_ORIGEN = {'bbq': 'business-plans-en-6 (BBQ EN cerrado)', 'cat': 'business-plans-en-4 (Catering EN publicado)'}

# celdas que van a los redactores aunque su EN del BBQ parezca limpio: las 51 de mapas_bbq.FORZAR_TRADUCTORES (notas
# del caso: C4-C8, C11-C15, C18, C24-C27, C44-C62, Startup D7:D20, P&L F10-F55, Staffing J), D119
_S, _I, _P, _R = '0. Supuestos', 'Inversión Inicial', 'PyG 3 Años', 'Personal'
FORZAR_TRADUCTORES = set(
    [('PAEP', _S, c) for c in ('C4', 'C5', 'C6', 'C7', 'C8', 'C11', 'C12', 'C13', 'C15', 'C18', 'C24', 'C26', 'C27',
                               'C44', 'C45', 'C51', 'C52', 'C54', 'C55', 'C58', 'C62')] +
    [('PAEP', _I, 'D%d' % f) for f in range(7, 21)] +
    [('PAEP', _P, c) for c in ('F10', 'F11', 'F24', 'F32', 'F33', 'F34', 'F35', 'F53', 'F54', 'F55')] +
    [('PAEP', _R, c) for c in ('J5', 'J6', 'J7', 'J8', 'J18', 'J19')])
# D122: filas de la tabla D19 que heredan la PROPUESTA del BBQ (misma fila): neto 7-8 % (58), food cost 28-35 % (60),
# marketplace ~15 % (62), OEWS (64), shared kitchen (65), seguros Insureon (67). Las otras 8 son nuevas (research §5)
D19_CON_PROPUESTA = (58, 60, 62, 64, 65, 67)


def propuesta_de(donde, es=None):
    """[(EN, grupo, id, tratamiento, origen)] por aparición en celda: primero el BBQ en esa celda, si no el catering;
    si la cadena no tiene ninguna aparición en celda (mensaje de DV…), el EN del mismo texto ES (BBQ, luego catering)."""
    out = []
    for o in donde or []:
        if o.get('t') != 'celda':
            continue
        k = (A_BBQ.get(o['f']), o.get('h'), o.get('c'))
        if k in BBQ_CELDA:
            out.append(BBQ_CELDA[k] + ('bbq',))
            continue
        k = (A_CAT.get(o['f']), o.get('h'), o.get('c'))
        if k in CAT_CELDA:
            out.append(CAT_CELDA[k] + ('cat',))
    if not out and not any(o.get('t') == 'celda' for o in donde or []):
        if es in BBQ_TEXTO:
            out.append(BBQ_TEXTO[es] + ('bbq',))
        elif es in CAT_TEXTO:
            out.append(CAT_TEXTO[es] + ('cat',))
    return out


def _fila(o):
    m = re.fullmatch(r'[A-Z]+(\d+)', o.get('c') or '')
    return int(m.group(1)) if m else None


def _col(o):
    m = re.fullmatch(r'([A-Z]+)\d+', o.get('c') or '')
    return m.group(1) if m else None


def _cambia_tarea(o):
    """Columnas que la pista marca como «cambia» en esa fila de tarea (datos_pael.TAREAS_PAEL)."""
    from datos_pael import COLS_CAMBIAN                                     # noqa: E402 (import perezoso)
    return _col(o) in COLS_CAMBIAN.get((o['h'], _fila(o)), '')


def grupo_de(planes, texto=None, tratamiento=None, donde=None):
    donde = donde or []
    libros = {o['f'] for o in donde}
    prop = propuesta_de(donde, texto)
    limpia = bool(prop) and len({x[0] for x in prop}) == 1 and not RX_REESCRIBIR.search(prop[0][0])
    tarea = [o for o in donde if o.get('det') == 'TAREA']
    if tarea:                                          # las 68 tareas × 4 columnas
        return 'GLB-check' if limpia and not any(_cambia_tarea(o) for o in tarea) else 'GPA-check'
    d19 = [o for o in donde if o.get('det') == 'D19']
    if d19:                                            # tabla de research §5 (D122)
        return 'GRB-plan' if limpia and all(_fila(o) in D19_CON_PROPUESTA for o in d19) else 'GPA-plan'
    destino = 'GPA-check' if libros == {'PAEC'} else 'GPA-plan'
    if any((o['f'], o.get('h'), o.get('c')) in FORZAR_TRADUCTORES for o in donde):
        return destino
    if not limpia:
        return destino                                 # sin EN, con EN distinto por celda o con vocabulario BBQ
    if prop[0][1] == 'GM' and tratamiento == 'traducir':
        return 'GM'
    return 'GLB-check' if libros == {'PAEC'} else 'GRB-plan'


def reuso_de(e):
    """EN de la PRIMERA celda de la cadena en la cadena BBQ → catering: el EN de GM / GRB-plan / GLB-check o la
    PROPUESTA de los redactores. D19: solo las 6 filas de D19_CON_PROPUESTA (D122); las otras 8, sin propuesta."""
    d19 = [o for o in e['donde'] if o.get('det') == 'D19']
    if d19 and not all(_fila(o) in D19_CON_PROPUESTA for o in d19):
        return None
    prop = propuesta_de(e['donde'], e['es'])
    if not prop:
        return None
    en, g, ident, tr, origen = prop[0]
    libro = A_BBQ if origen == 'bbq' else A_CAT
    return OrderedDict([('grupo', g), ('id', ident), ('en', en), ('tratamiento_origen', tr),
                        ('conjunto', _ORIGEN[origen]),
                        ('donde', ['%s %s!%s' % (libro.get(o['f']), o.get('h', ''), o.get('c', ''))
                                   for o in e['donde'][:2]])])


# ==========================================================================
# instalar
# ==========================================================================
def instalar(M):
    """Sustituye en el módulo `mapas` (M) los datos de FT/CAF por los del paella caterer."""
    from datos_pael import completar                                       # contenido (FIJOS, caso US, docx…)
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
    M.REUSO = OrderedDict()                     # el reuso es por CELDA (BBQ_CELDA → CAT_CELDA), no por texto
    M.FUENTES_CIFRAS = [os.path.join(BP, 'F1-research-us.md'), os.path.join(BP, 'SPEC.md'),
                        os.path.join(CAT, 'F1-research-us-delta.md'), os.path.join(BBQ, 'F1-research-us-delta.md'),
                        os.path.join(AQUI, 'F1-research-us-delta.md'), os.path.join(AQUI, 'SPEC-delta.md')]
    M.NOTAS_F2 = os.path.join(AQUI, 'F2-NOTAS.md')
    completar(M)
