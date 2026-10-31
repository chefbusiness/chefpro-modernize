#!/usr/bin/env python3
"""
mapas_mbar.py — Mobile Bar Business Plan Kit (EN) · datos ES→EN del conjunto «mbar» (estructura).

SPEC: `SPEC-delta.md` (D81-D95) sobre las heredadas (`../business-plans-en-4/SPEC-delta.md` D66-D80, `-3/` D48-D65,
`-2/` D30-D47, `../business-plans-en/SPEC.md` D1-D29). Sesión Claude Code, 13-oct-2026 (F2, paso 1). NO se ejecuta
solo: lo importa `../business-plans-en/mapas.py` cuando `BP_CONJUNTO=mbar` y llama a `instalar(M)`.

Como el catering: la FUENTE ES DEL CIRCUITO es el FOOD TRUCK ES (ranuras de celdas y párrafos) y el motor es el de
eventos (B4 = eventos/año, B5 = precio por invitado, B6 = invitados por evento; los 7 parches de `mapas_cat.py`, con
los escalones del Break-Even en ±$1 / +$2, D88). Lo NUEVO (D86): el DICCIONARIO DE REUSO POR CELDA es el EN PUBLICADO
DEL CATERING (`../business-plans-en-4/textos_es.json` + `textos_en/{GM,GR,GCAT-plan,GCAT-check}.json` con
`GR.revision.json` encima), con sus sha256 fijados abajo: si el catering cambia, `diccionario_ok()` lo dice y hay que
re-extraer. El contenido de bar móvil sale de las pistas, de `fuente_es_mbar.json` (coctelería ES) y de research.

    python3 bp5.py mapas            # autotest + cruce con censo_es.json + verificar (incluye los sha256)

Grupos (D86):
  GM          motor común cuyo EN publicado del catering (= el del FT) no habla de comida: no va a los redactores.
  GRC-plan    EN del catering reutilizable con revisión (notas del plan, tabla D18 «método»): preparar_tandas escribe
              su EN; la tanda GMB-plan las revisa (textos_en/GRC-plan.revision.json, solo las que cambian).
  GMB-plan    se escriben para el bar móvil: las del plan cuyo EN del catering habla de comida, cocina, comisaria,
              furgoneta, catering… (RX_REESCRIBIR), las sin EN del catering y las 56 celdas de la tabla D19.
  GMB-check   checklist: las 68 tareas × 4 columnas (una por celda: zona «TAREA») + los textos del checklist que no
              son motor limpio; propuesta = el EN del catering en ESA celda (si la ranura sobrevive, F1 §5).
"""
import hashlib
import json
import os
import re
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
BP = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
CAT = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')

# ==========================================================================
# 0. Producto (D81-D83). dir_es = FUENTE DEL CIRCUITO (food truck ES); slug_es = gemelo ES para hreflang (D81)
# ==========================================================================
PLANES = OrderedDict([
    ('mbar', OrderedDict([
        ('slug', 'mobile-bar-business-plan'),
        ('producto', 'Mobile Bar Business Plan Kit'),
        ('slug_es', 'plan-negocio-cocteleria-eventos'),
        ('dir_es', 'astro-site/public/dl/plan-negocio-food-truck'),
        ('env_stripe', 'VITE_STRIPE_PAYMENT_LINK_MOBILE_BAR_BUSINESS_PLAN'),
        ('keywords', 'mobile bar business plan, mobile bartending business plan, mobile bar business plan template, '
                     'how to start a mobile bar business, dry hire mobile bar, mobile bar pricing, mobile bar license, '
                     'AI Chef Pro'),
    ])),
])
for _p in PLANES.values():
    _p['url'] = 'aichef.pro/en/digital-products/' + _p['slug']
    _p['dir_en'] = 'astro-site/public/dl/' + _p['slug']

LIBROS = OrderedDict([
    ('MBP', ('mbar', 'plan-financiero-food-truck.xlsx', 'mobile-bar-financial-projections.xlsx',
             'Mobile Bar Financial Projections: 3-Year P&L, Cash Flow & Financing')),
    ('MBC', ('mbar', 'checklist-apertura-food-truck.xlsx', 'mobile-bar-startup-checklist.xlsx',
             'Mobile Bar Startup Checklist (68 Tasks)')),
])
DOCX = OrderedDict([
    ('mbar', ('plan-de-negocio-food-truck.docx', 'mobile-bar-business-plan.docx', 'Mobile Bar Business Plan (10 Sections)')),
])
TIPO_DE = {'MBP': 'plan', 'MBC': 'check'}
A_CAT = {'MBP': 'CATP', 'MBC': 'CATC'}                    # libro del catering que hace de diccionario de cada libro

# ==========================================================================
# 1. Pestañas: plan = FT; checklist = FT con la fase 2 «Trailer & Permits» (D83/D91: 27 caracteres ≤ 31; el título
#    de la hoja, sin límite, es «PHASE 2: TRAILER, LIQUOR RULES, PERMITS & INSURANCE»)
# ==========================================================================
_HOJAS_PLAN = OrderedDict([
    ('0. Supuestos', '0. Assumptions'), ('Inversión Inicial', 'Startup Costs'), ('PyG 3 Años', '3-Year P&L'),
    ('Punto Equilibrio', 'Break-Even'), ('Escenarios', 'Scenarios'), ('Personal', 'Staffing'),
    ('Instrucciones', 'Instructions'), ('Tesorería 12 meses', '12-Month Cash Flow'), ('Financiación', 'Financing'),
])
HOJA_F2_EN = 'Phase 2 - Trailer & Permits'
_HOJAS_CHECK = OrderedDict([
    ('F1 - Constitución', 'Phase 1 - Business Setup'), ('F2 - Vehículo', HOJA_F2_EN),
    ('F3 - Equipamiento', 'Phase 3 - Equipment'), ('F4 - Personal', 'Phase 4 - Staff'),
    ('F5 - Marketing', 'Phase 5 - Marketing'), ('F6 - 90 Días', 'Phase 6 - First 90 Days'),
    ('Instrucciones', 'Instructions'),
])
HOJAS_POR_LIBRO = OrderedDict([('MBP', _HOJAS_PLAN), ('MBC', _HOJAS_CHECK)])
HOJAS_ES_POR_LIBRO = OrderedDict((c, list(d)) for c, d in HOJAS_POR_LIBRO.items())
TAREAS_POR_FASE = OrderedDict([('MBC', [11, 13, 12, 10, 12, 10])])           # 68 (D91 = rejilla del FT)
MOLDE_CHECK = OrderedDict([('MBC', 'hojas')])
COL_OK = OrderedDict([('MBC', 1)])
FASES_CABECERA = OrderedDict()
FILAS_TAREA = OrderedDict([('F1 - Constitución', (5, 15)), ('F2 - Vehículo', (5, 17)), ('F3 - Equipamiento', (5, 16)),
                           ('F4 - Personal', (5, 14)), ('F5 - Marketing', (5, 16)), ('F6 - 90 Días', (5, 14))])

# ==========================================================================
# 2. Fórmulas: los 7 parches del catering (E2 ×2, Staffing!B20 → eventos, Staffing!C9 → SUMPRODUCT) con los escalones
#    del Break-Even en ±$1 / +$2 por invitado (D88: el precio medio del caso es ≈ $14)
# ==========================================================================
_E2_ALC = ("('0. Supuestos'!$B$62*'0. Supuestos'!$B$40+(1-'0. Supuestos'!$B$62)*'0. Supuestos'!$B$39)")
PARCHES_FORMULA = OrderedDict([
    (('MBP', 'PyG 3 Años', 'G13'), ("'0. Supuestos'!$B$39", "'0. Supuestos'!$B$41")),
    (('MBP', 'PyG 3 Años', 'G14'), (_E2_ALC, "'0. Supuestos'!$B$41")),
    (('MBP', 'Personal', 'B20'), ("'0. Supuestos'!$B$6", "'0. Supuestos'!$B$4")),
    (('MBP', 'Personal', 'C9'), ('SUM(C5:C8)', 'SUMPRODUCT(B5:B8,C5:C8)')),
    (('MBP', 'Punto Equilibrio', 'B31'), ('$B$8-2', '$B$8-1')),
    (('MBP', 'Punto Equilibrio', 'D31'), ('$B$8+2', '$B$8+1')),
    (('MBP', 'Punto Equilibrio', 'E31'), ('$B$8+4', '$B$8+2')),
])

# ==========================================================================
# 3. Instrucciones: versión D20 y aviso D21; zonas celda a celda: D18 (35-51), D19 (55-68) y las 68 tareas (B-E)
# ==========================================================================
FILA_VERSION = OrderedDict([('MBP', 73), ('MBC', 11)])
ZONAS_CELDA = OrderedDict([(('MBP', 'Instrucciones'), [(35, 51, 'ABCD', 'D18'), (55, 68, 'ABCD', 'D19')])])
for _h, (_f1, _f2) in FILAS_TAREA.items():
    ZONAS_CELDA[('MBC', _h)] = [(_f1, _f2, 'BCDE', 'TAREA')]

# ==========================================================================
# 4. Docx (D92): las 131 ranuras del FT ES, H1 en 37·44·51·59·67·76·83·91·100·109; último de §9 = 108 (nota UK)
# ==========================================================================
DOCX_N_PARRAFOS = OrderedDict([('mbar', 131)])
DOCX_ENCABEZADOS = OrderedDict([('mbar', [37, 44, 51, 59, 67, 76, 83, 91, 100, 109])])
DOCX_INDICE = OrderedDict([('mbar', list(range(24, 34)))])
DOCX_ULTIMO_9 = OrderedDict([('mbar', '108')])
DOCX_TANDAS = OrderedDict([('mbar_a', ('mbar', [1, 2, 3, 4, 5])), ('mbar_b', ('mbar', [6, 7, 8, 9, 10]))])
PRESTAMO_SEMILLA = OrderedDict([('mbar', 49000)])                   # punto fijo del dry-run (research §8: ≈ $50,000)

AUTOTEST = OrderedDict([
    ('P1', 'MBP'), ('P2', 'MBP'), ('C1', 'MBC'), ('C2', 'MBC'),
    ('C1_hoja_papel', 'F2 - Vehículo'), ('C1_titulo', 'Mobile Bar Startup Checklist (68 Tasks)'),
    ('C2_hoja_no_latino', 'F5 - Marketing'), ('P1_celda_texto', 'A3'), ('P1_celda_formula', 'B9'),
    ('P1_merge', 'A30:C30'),
])

# ==========================================================================
# 5. Grupos (D86)
# ==========================================================================
GRUPOS = ('GM', 'GRC-plan', 'GMB-plan', 'GMB-check')
GRUPOS_TRADUCTORES = ('GMB-plan', 'GMB-check')
GRUPOS_OVERRIDES = ('GMB-plan', 'GMB-check')
REVISAR_EN_TANDA = OrderedDict([('GMB-plan', ('GRC-plan',))])
GRUPOS_DESC = OrderedDict([
    ('GM', 'REUTILIZADAS: motor común cuyo EN publicado del Catering (= el del Food Truck) no habla de comida, cocina, '
           'comisaria, furgoneta ni catering. preparar_tandas escribe su EN. No van a los redactores'),
    ('GRC-plan', 'REUTILIZADAS con revisión: EN publicado del Catering en ESA celda que vale para un bar móvil salvo '
                 'matices (notas del plan, método D18). preparar_tandas escribe su EN; la tanda GMB-plan las revisa en '
                 'textos_en/GRC-plan.revision.json (solo las que cambian)'),
    ('GMB-plan', 'Plan financiero (MBP) que se ESCRIBE para el bar móvil: celdas cuyo EN del Catering habla de comida, '
                 'cocina, comisaria, furgoneta o catering (propuesta = ese EN), las que no tienen EN del Catering y las '
                 '56 celdas de la tabla D19 (sin propuesta)'),
    ('GMB-check', 'Checklist (MBC): las 68 tareas × 4 columnas (una por celda; ranuras del Catering que sobreviven, '
                  'F1-inventario §5) y los textos del checklist que no son motor limpio'),
    ('GX', 'NO se traduce: pestañas (mapas.HOJAS_POR_LIBRO), CLAVES, FIJOS, POR_CELDA, versión, pie y docProps'),
])

# Vocabulario del catering de comida / furgoneta que NO vale para un bar móvil: se busca en el EN del catering de la
# celda (F1-inventario §1). Es más amplio que el gate (RX_BAR_NO de datos_mbar): incluye «catering», «van», «menu»…
RX_REESCRIBIR = re.compile(
    r'(?i)\bfood\b|kitchen|commissar|(?<!AI )\bchefs?\b|\bsous\b|prep cook|\bplated\b|buffet|drop-?off|family-style|'
    r'\bstations?\b|chafing|\b(?:hotel|sheet) pans?\b|recipe|boxed lunch|ezcater|broadline|haccp|servsafe|'
    r'food protection|(?<!alcohol )\bservers?\b|grease|\bpests?\b|per plate|\bmenus?\b|\bmeals?\b|\bdish(?:es)?\b|'
    r'cuisine|\bcater|\bvans?\b|refrigerat|upfit|dietar|allergen|smallwares|insulated|cooking|burners?\b|'
    r'\bovens?\b|\bhot box|\bcold holding|\b41\s?°F')

# sha256 del diccionario (EN publicado del catering, `../business-plans-en-4/`) — D86/D93: no puede derivar
SHA_DICCIONARIO = OrderedDict([
    ('textos_es.json', '942033c95c5e11323cd49c556f0e019a888e55aad420187098b842c34eae2555'),
    ('textos_en/GM.json', 'a65dbc65e834e73376ed99d32243cd5512a6b96af8b40521f91db3d25a35503c'),
    ('textos_en/GR.json', '7e2e0f23be5f1d6f9e2e8cc5d60def04fd15030a7d1ea6d677ea7f8942b883ea'),
    ('textos_en/GR.revision.json', '976190192b0c069cad212a5c7e40a5dc2761917cc5a920edfd6f8fff3097b13e'),
    ('textos_en/GCAT-plan.json', '849c96d84281bd39825fac07cae8668b9f8a61d7549f2030e6d2e3725d2b569e'),
    ('textos_en/GCAT-check.json', '56399ef7fc4ecc9ab667b0f719243062c605d100a54025f4dfc247226af61104'),
    ('docx_en_cat_a.json', '2afccc350b8046f5567e0d990245a054f2530dfb2914fccb51d6d4213a3d7252'),
    ('docx_en_cat_b.json', '858fcf7d3119a7d87be2bf550c3c7fc9753a020d2c83f7a6d8d9183da7873728'),
])
_GRUPOS_CAT = ('GM', 'GR', 'GCAT-plan', 'GCAT-check')


def diccionario_ok():
    """[] si los 8 ficheros del diccionario del catering siguen con el sha256 fijado; si no, la lista de los que
    cambiaron (hay que re-extraer y revisar las propuestas)."""
    out = []
    for rel, sha in SHA_DICCIONARIO.items():
        p = os.path.join(CAT, rel)
        if not os.path.exists(p):
            out.append('%s: falta' % rel)
        elif hashlib.sha256(open(p, 'rb').read()).hexdigest() != sha:
            out.append('%s: sha256 distinto del fijado en mapas_mbar.SHA_DICCIONARIO' % rel)
    return out


def _en_cat():
    en = OrderedDict()
    for g in _GRUPOS_CAT:
        p = os.path.join(CAT, 'textos_en', g + '.json')
        if os.path.exists(p):
            en.update(json.load(open(p, encoding='utf-8')))
    rev = os.path.join(CAT, 'textos_en', 'GR.revision.json')
    if os.path.exists(rev):
        en.update(json.load(open(rev, encoding='utf-8')))             # ya va dentro de GR.json; idempotente
    return en


# --------------------------------------------------------------------------
# EN publicado del Catering, celda a celda (D86)
# --------------------------------------------------------------------------
def _cargar_cat():
    te_p = os.path.join(CAT, 'textos_es.json')
    out = OrderedDict()
    if not os.path.exists(te_p):
        return out
    en = _en_cat()
    for c in json.load(open(te_p, encoding='utf-8'))['cadenas']:
        if c['grupo'] not in _GRUPOS_CAT or c['id'] not in en:
            continue
        for d in c['donde']:
            if d.get('t') != 'celda' or d['f'] not in ('CATP', 'CATC'):
                continue
            out[(d['f'], d['h'], d['c'])] = (en[c['id']], c['grupo'], c['id'], c['tratamiento'])
    return out


def _cargar_cat_texto():
    """ES → (EN, grupo, id, tratamiento) del catering para las apariciones que NO son celda (mensajes de DV,
    cabeceras): mismo texto ES = mismo EN."""
    out = OrderedDict()
    te_p = os.path.join(CAT, 'textos_es.json')
    if not os.path.exists(te_p):
        return out
    en = _en_cat()
    for c in json.load(open(te_p, encoding='utf-8'))['cadenas']:
        if c['grupo'] in _GRUPOS_CAT and c['id'] in en and 'cat' in c.get('planes', []):
            out.setdefault(c['es'], (en[c['id']], c['grupo'], c['id'], c['tratamiento']))
    return out


CAT_CELDA = _cargar_cat()
CAT_TEXTO = _cargar_cat_texto()
# celdas que van a los redactores aunque su EN del catering parezca limpio: llevan una nota propia del bar móvil
FORZAR_TRADUCTORES = {('MBP', 'Escenarios', 'E23'), ('MBP', '0. Supuestos', 'C4'), ('MBP', '0. Supuestos', 'C5'),
                      ('MBP', '0. Supuestos', 'C6'), ('MBP', '0. Supuestos', 'C27'), ('MBP', '0. Supuestos', 'C52'),
                      ('MBP', '0. Supuestos', 'C58'), ('MBP', '0. Supuestos', 'C62')}


def cat_de(donde, es=None):
    """[(EN publicado del catering, grupo, id, tratamiento)] de las apariciones en celda; si la cadena no tiene ninguna
    en celda (mensaje de DV…), el EN del mismo texto ES en el catering."""
    out = []
    for o in donde or []:
        if o.get('t') != 'celda':
            continue
        k = (A_CAT.get(o['f']), o.get('h'), o.get('c'))
        if k in CAT_CELDA:
            out.append(CAT_CELDA[k])
    if not out and es in CAT_TEXTO and not any(o.get('t') == 'celda' for o in donde or []):
        out.append(CAT_TEXTO[es])
    return out


def grupo_de(planes, texto=None, tratamiento=None, donde=None):
    donde = donde or []
    libros = {o['f'] for o in donde}
    if any(o.get('det') == 'TAREA' for o in donde):
        return 'GMB-check'                             # las 68 tareas × 4 columnas
    if any(o.get('det') == 'D19' for o in donde):
        return 'GMB-plan'                              # tabla nueva desde research §5 (D88)
    destino = 'GMB-check' if libros == {'MBC'} else 'GMB-plan'
    if any((o['f'], o.get('h'), o.get('c')) in FORZAR_TRADUCTORES for o in donde):
        return destino
    cat = cat_de(donde, texto)
    if not cat or len({x[0] for x in cat}) > 1:
        return destino                                 # sin EN del catering, o con EN distinto por celda
    en, g = cat[0][0], cat[0][1]
    if RX_REESCRIBIR.search(en):
        return destino
    if g == 'GM' and tratamiento == 'traducir':
        return 'GM'
    return destino if libros == {'MBC'} else 'GRC-plan'


def reuso_de(e):
    """EN del Catering de la PRIMERA celda de la cadena: el EN de GM/GRC-plan o la PROPUESTA de los redactores. D19 sin
    propuesta: sus filas cambian enteras por los benchmarks del bar móvil (D88)."""
    if any(o.get('det') == 'D19' for o in e['donde']):
        return None
    cat = cat_de(e['donde'], e['es'])
    if not cat:
        return None
    en, g, ident, tr = cat[0]
    return OrderedDict([('grupo', g), ('id', ident), ('en', en), ('tratamiento_origen', tr),
                        ('conjunto', 'business-plans-en-4 (Catering EN publicado)'),
                        ('donde', ['%s %s!%s' % (A_CAT.get(o['f']), o.get('h', ''), o.get('c', ''))
                                   for o in e['donde'][:2]])])


# ==========================================================================
# instalar
# ==========================================================================
def instalar(M):
    """Sustituye en el módulo `mapas` (M) los datos de FT/CAF por los del bar móvil."""
    from datos_mbar import completar                                       # contenido (FIJOS, caso US, docx…)
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
    M.REUSO = OrderedDict()                     # el reuso es por CELDA (CAT_CELDA), no por texto
    M.FUENTES_CIFRAS = [os.path.join(BP, 'F1-research-us.md'), os.path.join(BP, 'SPEC.md'),
                        os.path.join(CAT, 'F1-research-us-delta.md'),
                        os.path.join(AQUI, 'F1-research-us-delta.md'), os.path.join(AQUI, 'SPEC-delta.md')]
    M.NOTAS_F2 = os.path.join(AQUI, 'F2-NOTAS.md')
    completar(M)
