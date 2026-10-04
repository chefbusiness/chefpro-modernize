#!/usr/bin/env python3
"""
mapas_rp.py — Restaurant Business Plan Kit + Bakery Business Plan Kit (EN) · datos ES→EN del conjunto «restpan».

SPEC: `SPEC-delta.md` (D30-D47, E1-E3) sobre `../business-plans-en/SPEC.md` (D1-D29), que manda en lo demás. Sesión
Claude Code, 4-oct-2026 (F2 tanda 1). NO se ejecuta solo: lo importa `../business-plans-en/mapas.py` cuando
`BP_CONJUNTO=restpan` y llama a `instalar(M)`, que SUSTITUYE en el módulo `mapas` los datos de food truck + cafetería
por los de restaurante + panadería. El código de los scripts (extraer, aplicar, gates, ensamblar, check, preparar) es
el mismo para los dos conjuntos; ver `F2-NOTAS.md` §1. Se usa con `bp2.py` (fija la variable y lanza el script):

    python3 bp2.py mapas            # autotest + cruce con censo_es.json de esta carpeta
    python3 bp2.py extraer_textos   # etc.

Claves con el nombre REAL de la pestaña ES («2. P&L 3 Años» en el restaurante). TOKENS_DOCX y el código usan el
nombre canónico del molde FT/CAF («PyG 3 Años»): `mapas.hoja_es()` lo resuelve libro a libro.
"""
import json
import os
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(os.path.dirname(AQUI), 'business-plans-en')

# ==========================================================================
# 0. Productos (D30-D32)
# ==========================================================================
PLANES = OrderedDict([
    ('rest', OrderedDict([
        ('slug', 'restaurant-business-plan'),
        ('producto', 'Restaurant Business Plan Kit'),
        ('slug_es', 'plan-negocio-bar-restaurante'),
        ('dir_es', 'astro-site/public/dl/plan-negocio-bar-restaurante'),
        ('env_stripe', 'VITE_STRIPE_PAYMENT_LINK_RESTAURANT_BUSINESS_PLAN'),
        ('keywords', 'restaurant business plan, restaurant business plan template, bar business plan, '
                     'restaurant startup costs, how to open a restaurant, AI Chef Pro'),
    ])),
    ('pan', OrderedDict([
        ('slug', 'bakery-business-plan'),
        ('producto', 'Bakery Business Plan Kit'),
        ('slug_es', 'plan-negocio-panaderia'),
        ('dir_es', 'astro-site/public/dl/plan-negocio-panaderia'),
        ('env_stripe', 'VITE_STRIPE_PAYMENT_LINK_BAKERY_BUSINESS_PLAN'),
        ('keywords', 'bakery business plan, bakery business plan template, how to start a bakery business, '
                     'bakery startup costs, AI Chef Pro'),
    ])),
])
for _p in PLANES.values():
    _p['url'] = 'aichef.pro/en/digital-products/' + _p['slug']
    _p['dir_en'] = 'astro-site/public/dl/' + _p['slug']

LIBROS = OrderedDict([
    ('RESTP', ('rest', 'plan-financiero-bar-restaurante.xlsx', 'restaurant-financial-projections.xlsx',
               'Restaurant Financial Projections: 3-Year P&L, Cash Flow & Financing')),
    ('RESTC', ('rest', 'checklist-apertura-bar-restaurante.xlsx', 'restaurant-opening-checklist.xlsx',
               'Restaurant Opening Checklist (64 Tasks)')),
    ('PANP', ('pan', 'plan-financiero-panaderia.xlsx', 'bakery-financial-projections.xlsx',
              'Bakery Financial Projections: 3-Year P&L, Cash Flow & Financing')),
    ('PANC', ('pan', 'checklist-apertura-panaderia.xlsx', 'bakery-opening-checklist.xlsx',
              'Bakery Opening Checklist (66 Tasks)')),
])
DOCX = OrderedDict([
    ('rest', ('plan-de-negocio-bar-restaurante.docx', 'restaurant-business-plan.docx',
              'Restaurant Business Plan (10 Sections)')),
    ('pan', ('plan-de-negocio-panaderia.docx', 'bakery-business-plan.docx', 'Bakery Business Plan (10 Sections)')),
])
TIPO_DE = {'RESTP': 'plan', 'RESTC': 'check', 'PANP': 'plan', 'PANC': 'check'}

# ==========================================================================
# 1. Pestañas (D33)
# ==========================================================================
_HOJAS_REST = OrderedDict([
    ('0. Supuestos', '0. Assumptions'), ('1. Inversión Inicial', '1. Startup Costs'),
    ('2. P&L 3 Años', '2. 3-Year P&L'), ('3. Punto Equilibrio', '3. Break-Even'), ('4. Escenarios', '4. Scenarios'),
    ('5. Personal', '5. Staffing'), ('Instrucciones', 'Instructions'), ('6. Tesorería 12 meses', '6. 12-Month Cash Flow'),
    ('7. Financiación', '7. Financing'),
])
_HOJAS_PAN = OrderedDict([
    ('0. Supuestos', '0. Assumptions'), ('Inversión Inicial', 'Startup Costs'), ('PyG 3 Años', '3-Year P&L'),
    ('Punto Equilibrio', 'Break-Even'), ('Escenarios', 'Scenarios'), ('Personal', 'Staffing'),
    ('Instrucciones', 'Instructions'), ('Tesorería 12 meses', '12-Month Cash Flow'), ('Financiación', 'Financing'),
])
HOJAS_POR_LIBRO = OrderedDict([
    ('RESTP', _HOJAS_REST),
    ('RESTC', OrderedDict([('Checklist Apertura', 'Opening Checklist'), ('Instrucciones', 'Instructions')])),
    ('PANP', _HOJAS_PAN),
    ('PANC', OrderedDict([('F1', 'Phase 1 - Business Setup'), ('F2', 'Phase 2 - Location & Permits'),
                          ('F3', 'Phase 3 - Equipment'), ('F4', 'Phase 4 - Staff'), ('F5', 'Phase 5 - Marketing'),
                          ('F6', 'Phase 6 - First 90 Days'), ('Instrucciones', 'Instructions')])),
])
HOJAS_ES_POR_LIBRO = OrderedDict((c, list(d)) for c, d in HOJAS_POR_LIBRO.items())
# D35: RESTC = una hoja, 7 fases como filas-cabecera fusionadas (A4, A15, A24, A33, A41, A50, A66), tareas hasta la 74
TAREAS_POR_FASE = OrderedDict([('RESTC', [10, 8, 8, 7, 8, 15, 8]), ('PANC', [11, 12, 12, 10, 11, 10])])
MOLDE_CHECK = OrderedDict([('RESTC', 'cabeceras'), ('PANC', 'hojas')])
COL_OK = OrderedDict([('RESTC', 5), ('PANC', 1)])
FASES_CABECERA = OrderedDict([('RESTC', ('Checklist Apertura', [4, 15, 24, 33, 41, 50, 66], 74))])

# ==========================================================================
# 2. Fórmulas: E2 (soportado de compras → B41) y E3 (PAN G10: el 4 % del pan común → 0, parte exenta)
# ==========================================================================
_E2_ALC = ("('0. Supuestos'!$B$62*'0. Supuestos'!$B$40+(1-'0. Supuestos'!$B$62)*'0. Supuestos'!$B$39)")
PARCHES_FORMULA = OrderedDict([
    (('RESTP', '2. P&L 3 Años', 'G14'), ("'0. Supuestos'!$B$39", "'0. Supuestos'!$B$41")),
    (('RESTP', '2. P&L 3 Años', 'G15'), (_E2_ALC, "'0. Supuestos'!$B$41")),
    (('PANP', 'PyG 3 Años', 'G10'), ('$H$10*0.04', '$H$10*0')),
    (('PANP', 'PyG 3 Años', 'G13'), ("$H$10*0.04+(1-$H$10)*'0. Supuestos'!$B$39", "'0. Supuestos'!$B$41")),
    (('PANP', 'PyG 3 Años', 'G14'), (_E2_ALC, "'0. Supuestos'!$B$41")),
])

# ==========================================================================
# 3. Instrucciones: versión D20 y aviso D21 (E1)
# ==========================================================================
FILA_VERSION = OrderedDict([('RESTP', 63), ('PANP', 72), ('RESTC', 11), ('PANC', 11)])
# tablas D18/D19 de Instrucciones: se localizan por sus cabeceras (SPEC delta §5: REST 34-45 / 49-58, PAN 35-51 / 55-67)
ZONAS_CELDA = OrderedDict([
    (('RESTP', 'Instrucciones'), [(None, None, 'ABCD', 'D18'), (None, None, 'ABCD', 'D19')]),
    (('PANP', 'Instrucciones'), [(None, None, 'ABCD', 'D18'), (None, None, 'ABCD', 'D19')]),
])
ZONAS_SPEC = OrderedDict([('RESTP', [(34, 45), (49, 58)]), ('PANP', [(35, 51), (55, 67)])])

# ==========================================================================
# 4. Docx (D43, D44)
# ==========================================================================
DOCX_N_PARRAFOS = OrderedDict([('rest', 148), ('pan', 131)])
DOCX_ENCABEZADOS = OrderedDict([('rest', [37, 45, 53, 61, 69, 78, 97, 104, 113, 123]),
                                ('pan', [37, 45, 52, 59, 68, 76, 84, 94, 104, 111])])
DOCX_INDICE = OrderedDict([('rest', list(range(24, 34))), ('pan', list(range(24, 34)))])
DOCX_ULTIMO_9 = OrderedDict([('rest', '122'), ('pan', '110')])
DOCX_TANDAS = OrderedDict([('rest_a', ('rest', [1, 2, 3, 4, 5])), ('rest_b', ('rest', [6, 7, 8, 9, 10])),
                           ('pan_a', ('pan', [1, 2, 3, 4, 5])), ('pan_b', ('pan', [6, 7, 8, 9, 10]))])
PRESTAMO_SEMILLA = OrderedDict([('rest', 250000), ('pan', 140000)])

# Autotest de gates_en.py (mismas mutaciones que FT/CAF, en estos libros)
AUTOTEST = OrderedDict([
    ('P1', 'RESTP'), ('P2', 'PANP'), ('C1', 'RESTC'), ('C2', 'PANC'),
    ('C1_hoja_papel', 'Checklist Apertura'), ('C1_titulo', 'Restaurant Opening Checklist (64 Tasks)'),
    ('C2_hoja_no_latino', 'F5'), ('P1_celda_texto', 'A3'), ('P1_celda_formula', 'B10'), ('P1_merge', 'A32:C32'),
])

GRUPOS = ('GM', 'GN', 'GREST', 'GPAN')
GRUPOS_TRADUCTORES = ('GN', 'GREST', 'GPAN')              # GM = reutilizado de FT/CAF (no va a los traductores)
GRUPOS_OVERRIDES = ('GREST', 'GPAN')
GRUPOS_DESC = OrderedDict([
    ('GM', 'REUTILIZADAS: idénticas a una cadena común de FT/CAF ya traducida (textos_en/GM.json de business-plans-en); '
           'preparar_tandas.py escribe su EN con los ids de este conjunto. No van a los traductores'),
    ('GN', 'Nuevas comunes a restaurante y panadería'),
    ('GREST', 'Solo restaurante (plan financiero + checklist de una hoja), incluidas las celdas de las tablas D18/D19'),
    ('GPAN', 'Solo panadería (plan financiero + checklist F1-F6), incluidas las celdas de las tablas D18/D19'),
    ('GX', 'NO se traduce: pestañas (mapas.HOJAS_POR_LIBRO), CLAVES, FIJOS, POR_CELDA, versión, pie y docProps'),
])


def grupo_de(planes, texto=None, tratamiento=None):
    r = REUSO.get(texto) if tratamiento == 'traducir' else None
    if r and r['grupo'] == 'GM':
        return 'GM'
    if planes == ['pan', 'rest']:
        return 'GN'
    return 'GREST' if planes == ['rest'] else 'GPAN'


# ==========================================================================
# 5. Reutilización (SPEC delta §5): cadenas idénticas a las YA traducidas para FT/CAF
# ==========================================================================
def _cargar_reuso():
    out = OrderedDict()
    te_p = os.path.join(BASE, 'textos_es.json')
    if not os.path.exists(te_p):
        return out
    te = json.load(open(te_p, encoding='utf-8'))
    en = {}
    for g in ('GM', 'GFT', 'GCAF'):
        p = os.path.join(BASE, 'textos_en', g + '.json')
        if os.path.exists(p):
            en.update(json.load(open(p, encoding='utf-8')))
    for c in te['cadenas']:
        if c['tratamiento'] != 'traducir' or c['grupo'] not in ('GM', 'GFT', 'GCAF') or c['id'] not in en:
            continue
        out[c['es']] = OrderedDict([('grupo', c['grupo']), ('id', c['id']), ('en', en[c['id']]),
                                    ('donde', ['%s %s!%s' % (d['f'], d.get('h', ''), d.get('c', ''))
                                               for d in c['donde'][:2]])])
    return out


REUSO = _cargar_reuso()


# ==========================================================================
# instalar
# ==========================================================================
def instalar(M):
    """Sustituye en el módulo `mapas` (M) los datos de FT/CAF por los de restaurante + panadería."""
    from datos_rp import completar                                         # el resto de los datos (§6-§9)
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
    M.grupo_de = grupo_de
    M.REUSO = REUSO
    M.FUENTES_CIFRAS = [os.path.join(BASE, 'F1-research-us.md'), os.path.join(BASE, 'SPEC.md'),
                        os.path.join(AQUI, 'F1-research-us-delta.md'), os.path.join(AQUI, 'SPEC-delta.md')]
    M.NOTAS_F2 = os.path.join(AQUI, 'F2-NOTAS.md')
    completar(M)
