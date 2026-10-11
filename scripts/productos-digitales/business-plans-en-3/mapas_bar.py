#!/usr/bin/env python3
"""
mapas_bar.py — Bar Business Plan Kit (EN) · datos ES→EN del conjunto «bar» (estructura).

SPEC: `SPEC-delta.md` (D48-D65) sobre `../business-plans-en-2/SPEC-delta.md` (D30-D47) y
`../business-plans-en/SPEC.md` (D1-D29), que mandan en lo demás. Sesión Claude Code, 11-oct-2026 (F2, paso 1). NO se
ejecuta solo: lo importa `../business-plans-en/mapas.py` cuando `BP_CONJUNTO=bar` y llama a `instalar(M)`, que
SUSTITUYE en el módulo `mapas` los datos de food truck + cafetería por los del bar. Por estructura el bar es gemelo de
la CAFETERÍA (F1-inventario-delta §0): molde FT/CAF (pestañas sin numerar, checklist de 6 hojas con OK en la col. A),
sin el resolutor de pestañas numeradas ni el molde de una hoja del restaurante. Del restaurante se reutiliza el
CONTENIDO (alcohol, cubiertos, propinas, licencia de alcohol) por el diccionario de reutilización (`REUSO`).

    python3 bp3.py mapas            # autotest + cruce con censo_es.json de esta carpeta

Contenido (el resto, en `datos_bar.py`): productos D48-D50 · pestañas D53 · E2/E4 · versión D20/D21 · zonas D18/D19 ·
docx D61 · grupos (GM, GR, GBAR-plan, GBAR-check) · reutilización (BP + BP2).
"""
import json
import os
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
BP = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
BP2 = os.path.join(os.path.dirname(AQUI), 'business-plans-en-2')

# ==========================================================================
# 0. Producto (D48-D50)
# ==========================================================================
PLANES = OrderedDict([
    ('bar', OrderedDict([
        ('slug', 'bar-business-plan'),
        ('producto', 'Bar Business Plan Kit'),
        ('slug_es', 'plan-negocio-tapas-bar'),
        ('dir_es', 'astro-site/public/dl/plan-negocio-tapas-bar'),
        ('env_stripe', 'VITE_STRIPE_PAYMENT_LINK_BAR_BUSINESS_PLAN'),
        ('keywords', 'bar business plan, bar business plan template, how to open a bar, bar startup costs, '
                     'liquor license, AI Chef Pro'),
    ])),
])
for _p in PLANES.values():
    _p['url'] = 'aichef.pro/en/digital-products/' + _p['slug']
    _p['dir_en'] = 'astro-site/public/dl/' + _p['slug']

LIBROS = OrderedDict([
    ('BARP', ('bar', 'plan-financiero-tapas-bar.xlsx', 'bar-financial-projections.xlsx',
              'Bar Financial Projections: 3-Year P&L, Cash Flow & Financing')),
    ('BARC', ('bar', 'checklist-apertura-tapas-bar.xlsx', 'bar-opening-checklist.xlsx',
              'Bar Opening Checklist (73 Tasks)')),
])
DOCX = OrderedDict([
    ('bar', ('plan-de-negocio-tapas-bar.docx', 'bar-business-plan.docx', 'Bar Business Plan (10 Sections)')),
])
TIPO_DE = {'BARP': 'plan', 'BARC': 'check'}

# ==========================================================================
# 1. Pestañas (D53): plan = las de FT/CAF; checklist = CAFC salvo «F2 - Local» → «Phase 2 - Location & Licenses»
# ==========================================================================
_HOJAS_PLAN = OrderedDict([
    ('0. Supuestos', '0. Assumptions'), ('Inversión Inicial', 'Startup Costs'), ('PyG 3 Años', '3-Year P&L'),
    ('Punto Equilibrio', 'Break-Even'), ('Escenarios', 'Scenarios'), ('Personal', 'Staffing'),
    ('Instrucciones', 'Instructions'), ('Tesorería 12 meses', '12-Month Cash Flow'), ('Financiación', 'Financing'),
])
_HOJAS_CHECK = OrderedDict([
    ('F1 - Constitución', 'Phase 1 - Business Setup'), ('F2 - Local', 'Phase 2 - Location & Licenses'),
    ('F3 - Equipamiento', 'Phase 3 - Build-Out & Equipment'), ('F4 - Personal', 'Phase 4 - Staff'),
    ('F5 - Marketing', 'Phase 5 - Marketing'), ('F6 - 90 Días', 'Phase 6 - First 90 Days'),
    ('Instrucciones', 'Instructions'),
])
HOJAS_POR_LIBRO = OrderedDict([('BARP', _HOJAS_PLAN), ('BARC', _HOJAS_CHECK)])
HOJAS_ES_POR_LIBRO = OrderedDict((c, list(d)) for c, d in HOJAS_POR_LIBRO.items())
TAREAS_POR_FASE = OrderedDict([('BARC', [11, 13, 13, 12, 14, 10])])          # 73 (D24, F1 §1)
MOLDE_CHECK = OrderedDict([('BARC', 'hojas')])
COL_OK = OrderedDict([('BARC', 1)])
FASES_CABECERA = OrderedDict()

# ==========================================================================
# 2. Fórmulas: E2 (soportado de compras → B41, las mismas celdas que la CAF) y E4 (FTE = Σ personas × FTE)
# ==========================================================================
_E2_ALC = ("('0. Supuestos'!$B$62*'0. Supuestos'!$B$40+(1-'0. Supuestos'!$B$62)*'0. Supuestos'!$B$39)")
PARCHES_FORMULA = OrderedDict([
    (('BARP', 'PyG 3 Años', 'G13'), ("'0. Supuestos'!$B$39", "'0. Supuestos'!$B$41")),
    (('BARP', 'PyG 3 Años', 'G14'), (_E2_ALC, "'0. Supuestos'!$B$41")),
    (('BARP', 'Personal', 'C12'), ('SUM(C5:C11)', 'SUMPRODUCT(B5:B11,C5:C11)')),
])

# ==========================================================================
# 3. Instrucciones: versión D20 y aviso D21 (E1: BARP A75, BARC A12); zonas D18 (34-50) / D19 (53-69) por cabecera
# ==========================================================================
FILA_VERSION = OrderedDict([('BARP', 74), ('BARC', 11)])
ZONAS_CELDA = OrderedDict([
    (('BARP', 'Instrucciones'), [(None, None, 'ABCD', 'D18'), (None, None, 'ABCD', 'D19')]),
])

# ==========================================================================
# 4. Docx (D61): 133 párrafos, 10 Heading 1; último de §9 = 110 (nota UK); tandas bar_a (§1-5) y bar_b (§6-10)
# ==========================================================================
DOCX_N_PARRAFOS = OrderedDict([('bar', 133)])
DOCX_ENCABEZADOS = OrderedDict([('bar', [37, 45, 52, 60, 69, 79, 86, 96, 104, 111])])
DOCX_INDICE = OrderedDict([('bar', list(range(24, 34)))])
DOCX_ULTIMO_9 = OrderedDict([('bar', '110')])
DOCX_TANDAS = OrderedDict([('bar_a', ('bar', [1, 2, 3, 4, 5])), ('bar_b', ('bar', [6, 7, 8, 9, 10]))])
PRESTAMO_SEMILLA = OrderedDict([('bar', 369000)])                   # research §8 (CALIBRAR por punto fijo)

# Autotest de gates_en.py: un solo plan → P1 = P2 y C1 = C2 (cada mutación va en su propia copia)
AUTOTEST = OrderedDict([
    ('P1', 'BARP'), ('P2', 'BARP'), ('C1', 'BARC'), ('C2', 'BARC'),
    ('C1_hoja_papel', 'F2 - Local'), ('C1_titulo', 'Bar Opening Checklist (73 Tasks)'),
    ('C2_hoja_no_latino', 'F5 - Marketing'), ('P1_celda_texto', 'A3'), ('P1_celda_formula', 'B9'),
    ('P1_merge', 'A30:C30'),
])

# ==========================================================================
# 5. Grupos (D53). GM y GR NO van a los traductores: su EN sale del diccionario de reutilización. GR se revisa
#    en la tanda GBAR-check (lista «revisar_reutilizadas»; correcciones en textos_en/GR.revision.json).
# ==========================================================================
GRUPOS = ('GM', 'GR', 'GBAR-plan', 'GBAR-check')
GRUPOS_TRADUCTORES = ('GBAR-plan', 'GBAR-check')
GRUPOS_OVERRIDES = ('GBAR-plan', 'GBAR-check')
REVISAR_EN_TANDA = OrderedDict([('GBAR-check', ('GR',))])
GRUPOS_DESC = OrderedDict([
    ('GM', 'REUTILIZADAS: idénticas a una cadena común de FT/CAF ya traducida (../business-plans-en/textos_en/GM.json); '
           'preparar_tandas escribe su EN con los ids de este conjunto. No van a los traductores'),
    ('GR', 'REUTILIZADAS con marca «revisar contexto»: idénticas a una cadena de REST/PAN/CAF/FT ya traducida '
           '(GN/GREST/GPAN de business-plans-en-2, GCAF/GFT de business-plans-en). preparar_tandas escribe su EN; '
           'la tanda GBAR-check las revisa y corrige en textos_en/GR.revision.json'),
    ('GBAR-plan', 'Nuevas del plan financiero (BARP), incluidas TODAS las celdas de las tablas D18/D19 de Instrucciones '
                  '(una por celda; con propuesta cuando la celda existe en otro libro)'),
    ('GBAR-check', 'Nuevas del checklist (BARC) + revisión de las reutilizadas GR'),
    ('GX', 'NO se traduce: pestañas (mapas.HOJAS_POR_LIBRO), CLAVES, FIJOS, POR_CELDA, versión, pie y docProps'),
])


def grupo_de(planes, texto=None, tratamiento=None, donde=None):
    """GM / GR si la cadena (de «traducir») ya está traducida en otro conjunto; si no, por libro: GBAR-check solo si
    TODAS sus apariciones son del checklist (la cadena de los dos libros va al plan)."""
    if tratamiento == 'traducir':
        r = REUSO.get(texto)
        if r and r.get('tratamiento_origen') == 'traducir':
            return 'GM' if r['grupo'] == 'GM' else 'GR'
    libros = {o['f'] for o in (donde or [])}
    return 'GBAR-check' if libros == {'BARC'} else 'GBAR-plan'


def reuso_de(e):
    """«traducir»: solo EN de cadenas que en su conjunto también eran de «traducir» (valen para cualquier celda).
    «localizar» de la tabla D18: cualquier EN del mismo ES, como PROPUESTA (el EN de una tabla vale solo para su
    celda de origen: el traductor la revisa). D19 sin propuesta: sus filas las fija D58 por pista."""
    r = REUSO.get(e['es'])
    if not r:
        return None
    if e['tratamiento'] == 'traducir':
        return r if r.get('tratamiento_origen') == 'traducir' else None
    if e['tratamiento'] != 'localizar' or any(o.get('det') == 'D19' for o in e['donde']):
        return None                     # D19: TODAS sus filas cambian por las de D58 (una propuesta despistaría)
    return r


# ==========================================================================
# 6. Reutilización (D53; F1-inventario-delta §2). Prioridad GM → REST → CAF → PAN → FT (la del inventario)
# ==========================================================================
_FUENTES_REUSO = [
    # (carpeta, grupos de textos_en, orden de prioridad del grupo)
    (BP, ('GM',)), (BP2, ('GREST', 'GN')), (BP, ('GCAF',)), (BP2, ('GPAN',)), (BP, ('GFT',)),
]


def _cargar_reuso():
    out = OrderedDict()
    cache = {}
    for carpeta, grupos in _FUENTES_REUSO:
        te_p = os.path.join(carpeta, 'textos_es.json')
        if not os.path.exists(te_p):
            continue
        if te_p not in cache:
            cache[te_p] = json.load(open(te_p, encoding='utf-8'))
        te = cache[te_p]
        for g in grupos:
            p = os.path.join(carpeta, 'textos_en', g + '.json')
            if not os.path.exists(p):
                continue
            en = json.load(open(p, encoding='utf-8'))
            # overrides por celda del RESTAURANTE (ronda de arreglos de BP2: la nota E4 de Staffing, que el bar
            # también lleva; la de SBA Microloan): el EN corregido manda. Los de FT (commissary) y CAF (avisos de
            # la fase 2) son propios de su libro y NO se heredan
            for go in (('GREST',) if carpeta == BP2 else ()):
                po = os.path.join(carpeta, 'textos_en', 'overrides_%s.json' % go)
                if os.path.exists(po):
                    for ident, o in json.load(open(po, encoding='utf-8')).items():
                        if ident in en:
                            en[ident] = o['texto']
            for c in te['cadenas']:
                if c['grupo'] != g or c['id'] not in en or c['tratamiento'] not in ('traducir', 'localizar'):
                    continue
                previo = out.get(c['es'])
                # una cadena de «traducir» manda sobre una de tabla (por celda) del mismo ES
                if previo and not (previo['tratamiento_origen'] == 'localizar' and c['tratamiento'] == 'traducir'):
                    continue
                out[c['es']] = OrderedDict([
                    ('grupo', g), ('id', c['id']), ('en', en[c['id']]), ('tratamiento_origen', c['tratamiento']),
                    ('conjunto', os.path.basename(carpeta)),
                    ('donde', ['%s %s!%s' % (d['f'], d.get('h', ''), d.get('c', '')) for d in c['donde'][:2]])])
    return out


REUSO = _cargar_reuso()


# ==========================================================================
# instalar
# ==========================================================================
def instalar(M):
    """Sustituye en el módulo `mapas` (M) los datos de FT/CAF por los del bar."""
    from datos_bar import completar                                        # contenido (FIJOS, caso US, docx…)
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
    M.REUSO = REUSO
    M.FUENTES_CIFRAS = [os.path.join(BP, 'F1-research-us.md'), os.path.join(BP, 'SPEC.md'),
                        os.path.join(BP2, 'F1-research-us-delta.md'), os.path.join(BP2, 'SPEC-delta.md'),
                        os.path.join(AQUI, 'F1-research-us-delta.md'), os.path.join(AQUI, 'SPEC-delta.md')]
    M.NOTAS_F2 = os.path.join(AQUI, 'F2-NOTAS.md')
    completar(M)
