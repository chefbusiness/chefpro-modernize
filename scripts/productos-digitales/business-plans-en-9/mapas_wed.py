#!/usr/bin/env python3
"""
mapas_wed.py — Wedding Venue Business Plan Kit (EN) · datos ES→EN del conjunto «wed» (estructura).

SPEC: `SPEC-delta.md` (D156-D180) sobre las heredadas (`../business-plans-en-8/SPEC-delta.md` D133-D155 = PIZZA, código y
método; `../business-plans-en-2/` = BAKERY, estructura del libro). Sesión Claude Code, 27-oct-2026 (F2-EN, paso 1a). NO se
ejecuta solo: lo importa `../business-plans-en/mapas.py` cuando `BP_CONJUNTO=wed` y llama a `instalar(M)`. Clon de
`../business-plans-en-8/mapas_piz.py` (D161): el libro de la finca ES es GEMELO de la PANADERÍA ES (724/734 fórmulas
idénticas, inv. §0), estructura que ya pasó por el código común con el Bakery EN; el docx es el del FT ES (131 ranuras,
config de PAEL/PIZ).

FUENTE ES (una sola variable): `FUENTE_ES` = `$WED_FUENTE_ES` o, si no está, `astro-site/public/dl/
plan-negocio-finca-eventos-bodas` (el ES LIVE, ya revisado: inv. §0).

DICCIONARIO POR TEXTO (D161, decisión SPEC frente al «por celda» del Bar en la pizza: ningún EN es gemelo de celda de la
finca, inv. §0.2). Fuentes en este orden: PIZZA EN (GM, GR, GPIZ-plan, GPIZ-check) → Bakery/BP (GM de BP2, GPAN, GREST,
GN; GM, GCAF, GFT de BP) → BBQ (GM, GRC-plan, GBQ-*) → PAEL (GM, GRB-plan, GPA-*, GLB-check). Primero el ES exacto y luego
el ES NORMALIZADO con el VOCABULARIO de la finca invertido (invitado → cubierto, evento → día, finca → local, espacio y
servicios → comida, canon → bebida…: `normalizadores()`, copia de `inventario_delta.py`). Grupos:
  GM          ES exacto de una cadena GM (motor común) de la pizza o de BP/BP2, con EN limpio (sin RX_REESCRIBIR).
  GR          EN reutilizado de una cadena NO GM, de otro conjunto o casado solo tras normalizar, con EN limpio (solo
              del plan): preparar_tandas lo escribe y la tanda GWED-plan lo revisa (textos_en/GR.revision.json).
  GWED-plan   nuevas del plan + las reutilizables con vocabulario o caso de restaurante (RX_REESCRIBIR, con propuesta)
              + las 14 filas D19 (sin propuesta: D165 las cambia todas).
  GWED-check  nuevas del checklist (84 tareas: casi todo texto nuevo) + las reutilizables no GM del checklist, con
              propuesta (cada fila lleva la tarea US de D169 como pista: la propuesta de otro kit no basta).

    python3 bp9.py mapas            # autotest + cruce con censo_es.json + verificar (incluye los sha256 de las fuentes)
"""
import ast
import hashlib
import json
import os
import re
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
PD = os.path.dirname(AQUI)
BP = os.path.join(PD, 'business-plans-en')
BP2 = os.path.join(PD, 'business-plans-en-2')
BBQ = os.path.join(PD, 'business-plans-en-6')
PAEL = os.path.join(PD, 'business-plans-en-7')
PIZ = os.path.join(PD, 'business-plans-en-8')
A_FINCA = os.path.join(PD, 'planes-v2_0', 'contenido_plan_negocio_finca_eventos_bodas', 'a.py')

# ==========================================================================
# 0. Producto (D156-D158). FUENTE_ES: la ÚNICA ruta del ES (el LIVE de main)
# ==========================================================================
FUENTE_ES = os.environ.get('WED_FUENTE_ES') or 'astro-site/public/dl/plan-negocio-finca-eventos-bodas'
PLANES = OrderedDict([
    ('wed', OrderedDict([
        ('slug', 'wedding-venue-business-plan'),
        ('producto', 'Wedding Venue Business Plan Kit'),
        ('slug_es', 'plan-negocio-finca-eventos-bodas'),
        ('dir_es', FUENTE_ES),
        ('env_stripe', 'VITE_STRIPE_PAYMENT_LINK_WEDDING_VENUE_BUSINESS_PLAN'),
        ('keywords', 'wedding venue business plan, event venue business plan, how to start a wedding venue, wedding '
                     'venue startup costs, venue rental agreement, AI Chef Pro'),
    ])),
])
for _p in PLANES.values():
    _p['url'] = 'aichef.pro/en/digital-products/' + _p['slug']
    _p['dir_en'] = 'astro-site/public/dl/' + _p['slug']

LIBROS = OrderedDict([
    ('WEDP', ('wed', 'plan-financiero-finca-eventos-bodas.xlsx', 'wedding-venue-financial-projections.xlsx',
              'Wedding Venue Financial Projections: 3-Year P&L, Cash Flow & Financing')),
    ('WEDC', ('wed', 'checklist-apertura-finca-eventos-bodas.xlsx', 'wedding-venue-startup-checklist.xlsx',
              'Wedding Venue Startup Checklist (84 Tasks)')),
])
DOCX = OrderedDict([
    ('wed', ('plan-de-negocio-finca-eventos-bodas.docx', 'wedding-venue-business-plan.docx',
             'Wedding Venue Business Plan (10 Sections)')),
])
TIPO_DE = {'WEDP': 'plan', 'WEDC': 'check'}

# ==========================================================================
# 1. Pestañas: plan = las de la pizza (mismas 9); checklist D169 (todas ≤ 31 caracteres)
# ==========================================================================
_HOJAS_PLAN = OrderedDict([
    ('0. Supuestos', '0. Assumptions'), ('Inversión Inicial', 'Startup Costs'), ('PyG 3 Años', '3-Year P&L'),
    ('Punto Equilibrio', 'Break-Even'), ('Escenarios', 'Scenarios'), ('Personal', 'Staffing'),
    ('Instrucciones', 'Instructions'), ('Tesorería 12 meses', '12-Month Cash Flow'), ('Financiación', 'Financing'),
])
_HOJAS_CHECK = OrderedDict([
    ('F1 - Constitución', 'Phase 1 - Business Setup'), ('F2 - Finca y licencia', 'Phase 2 - Zoning & Permits'),
    ('F3 - Obra y equipamiento', 'Phase 3 - Build-Out & Equipment'), ('F4 - Personal y catering', 'Phase 4 - Staff & Caterer'),
    ('F5 - Marca y reservas', 'Phase 5 - Brand & Bookings'), ('F6 - Temporada y eventos', 'Phase 6 - Season & Events'),
    ('Instrucciones', 'Instructions'),
])
assert all(len(v) <= 31 for v in _HOJAS_CHECK.values())
HOJAS_POR_LIBRO = OrderedDict([('WEDP', _HOJAS_PLAN), ('WEDC', _HOJAS_CHECK)])
HOJAS_ES_POR_LIBRO = OrderedDict((c, list(d)) for c, d in HOJAS_POR_LIBRO.items())
TAREAS_POR_FASE = OrderedDict([('WEDC', [12, 16, 15, 13, 14, 14])])          # 84 (D169, inv. §1)
MOLDE_CHECK = OrderedDict([('WEDC', 'hojas')])
COL_OK = OrderedDict([('WEDC', 1)])
FASES_CABECERA = OrderedDict()

# ==========================================================================
# 2. Fórmulas (D164, D166): E2 solo G14 (G13 es VALOR en el ES → VALORES_EN 0) y E4 (FTE = Σ personas × FTE). Sin E3
#    ni E5: la columna H del P&L va vacía en la finca (inv. §2.3)
# ==========================================================================
_E2_ALC = ("('0. Supuestos'!$B$62*'0. Supuestos'!$B$40+(1-'0. Supuestos'!$B$62)*'0. Supuestos'!$B$39)")
PARCHES_FORMULA = OrderedDict([
    (('WEDP', 'PyG 3 Años', 'G14'), (_E2_ALC, "'0. Supuestos'!$B$41")),
    (('WEDP', 'Personal', 'C11'), ('SUM(C5:C10)', 'SUMPRODUCT(B5:B10,C5:C10)')),
])

# ==========================================================================
# 3. Instrucciones: versión D20 y aviso D21 (E1: WEDP A54, WEDC A12); zona D19 (sin D18) por cabecera (filas 35-48)
# ==========================================================================
FILA_VERSION = OrderedDict([('WEDP', 53), ('WEDC', 11)])
ZONAS_CELDA = OrderedDict([
    (('WEDP', 'Instrucciones'), [(None, None, 'ABCD', 'D19')]),
])

# ==========================================================================
# 4. Docx (D170): las 131 ranuras del FT ES (= PAEL/PIZ), H1 en 37·44·51·59·67·76·83·91·100·109; último de §9 = 108
#    (nota UK); tandas wed_a (§1-5) y wed_b (§6-10)
# ==========================================================================
DOCX_N_PARRAFOS = OrderedDict([('wed', 131)])
DOCX_ENCABEZADOS = OrderedDict([('wed', [37, 44, 51, 59, 67, 76, 83, 91, 100, 109])])
DOCX_INDICE = OrderedDict([('wed', list(range(24, 34)))])
DOCX_ULTIMO_9 = OrderedDict([('wed', '108')])
DOCX_TANDAS = OrderedDict([('wed_a', ('wed', [1, 2, 3, 4, 5])), ('wed_b', ('wed', [6, 7, 8, 9, 10]))])
PRESTAMO_SEMILLA = OrderedDict([('wed', 460000)])                   # research §8: ≈ $458,000 (punto fijo)

AUTOTEST = OrderedDict([
    ('P1', 'WEDP'), ('P2', 'WEDP'), ('C1', 'WEDC'), ('C2', 'WEDC'),
    ('C1_hoja_papel', 'F2 - Finca y licencia'), ('C1_titulo', 'Wedding Venue Startup Checklist (84 Tasks)'),
    ('C2_hoja_no_latino', 'F5 - Marca y reservas'), ('P1_celda_texto', 'A3'), ('P1_celda_formula', 'B9'),
    ('P1_merge', 'A31:C31'),
])

# ==========================================================================
# 5. Grupos (D161)
# ==========================================================================
GRUPOS = ('GM', 'GR', 'GWED-plan', 'GWED-check')
GRUPOS_TRADUCTORES = ('GWED-plan', 'GWED-check')
GRUPOS_OVERRIDES = ('GWED-plan', 'GWED-check')
REVISAR_EN_TANDA = OrderedDict([('GWED-plan', ('GR',))])
GRUPOS_DESC = OrderedDict([
    ('GM', 'REUTILIZADAS: mismo ES exacto que una cadena GM (motor común) de la Pizza EN o de BP/BP2, con EN sin '
           'vocabulario de restaurante (RX_REESCRIBIR). preparar_tandas escribe su EN. No van a los traductores'),
    ('GR', 'REUTILIZADAS con revisión: EN de una cadena no GM de la Pizza, de BP/BP2, BBQ o PAEL, o casado solo tras '
           'normalizar el vocabulario de la finca. preparar_tandas escribe su EN; la tanda GWED-plan las revisa en '
           'textos_en/GR.revision.json'),
    ('GWED-plan', 'Nuevas del plan financiero (WEDP) + las reutilizables con vocabulario o caso de restaurante (con '
                  'propuesta) + las 14 filas D19 de Instrucciones (una cadena por celda, sin propuesta: D165)'),
    ('GWED-check', 'Nuevas del checklist (WEDC): las 84 tareas y sus cabeceras (con propuesta si existe)'),
    ('GX', 'NO se traduce: pestañas (mapas.HOJAS_POR_LIBRO), CLAVES, FIJOS, POR_CELDA, versión, pie y docProps'),
])

# Vocabulario y caso de restaurante (pizza, bar, panadería, cafetería, food truck) que NO vale para un venue: clasifica las
# PROPUESTAS (no es el gate: ese es datos_wed.RX_WED_NO). Una propuesta sucia va a los traductores con su EN como forma
_CASO_PIZ = (r'669,600|709,776|738,167|242,550|329,274|217,300|\b62 covers\b|\$36(?:\.00)?\b|\b300 days\b|'
             r'\b50 seats\b')
RX_REESCRIBIR = re.compile(
    r'(?i)\bcovers?\b|\bpizz|\bdough|\boven\b|wood-fired|seat turns?|\bseats?\b|\bdine-in\b|take-out|to-go|\bpickup\b|'
    r'\bdelivery\b|marketplace|average check|\bmenu\b|\bfood\b|\bbeverages?\b|\bdrinks?\b|food cost|cost of goods|'
    r'\bCOGS\b|prime cost|\bshifts?\b|opening days?|\bper day\b|\ba day\b|\bdaily\b|\bdays? a year\b|\bcustomers?\b|'
    r'\bFOH\b|\bBOH\b|\bservers?\b|\btips?\b|restaurant|\bbakery|\bbread\b|croissant|pastr|coffee|espresso|\bcafe\b|'
    r'\bcafé\b|food truck|\btruck\b|\btapas\b|cocktail|\bbar\b|beer|wine|liquor license|patio|firewood|Neapolitan|'
    r'\bkitchen\b|\bcook|\bchef\b|\bdining room\b|\bpremises\b|' + _CASO_PIZ)

# ==========================================================================
# 6. Diccionario por TEXTO (D161)
# ==========================================================================
# (carpeta, grupos con EN, etiqueta). Orden = prioridad. Los GM de la pizza y de BP/BP2 son «motor común»
FUENTES = [
    (PIZ, ('GM', 'GR', 'GPIZ-plan', 'GPIZ-check'), 'business-plans-en-8 (Pizza EN)'),
    (BP2, ('GM', 'GPAN', 'GREST', 'GN'), 'business-plans-en-2 (Bakery/Restaurant EN)'),
    (BP, ('GM', 'GCAF', 'GFT'), 'business-plans-en (FT/CAF EN)'),
    (BBQ, ('GM', 'GRC-plan', 'GBQ-plan', 'GBQ-check'), 'business-plans-en-6 (BBQ EN)'),
    (PAEL, ('GM', 'GRB-plan', 'GPA-plan', 'GPA-check', 'GLB-check'), 'business-plans-en-7 (Paella EN)'),
]
GM_MOTOR = {(PIZ, 'GM'), (BP2, 'GM'), (BP, 'GM')}

# sha256 del diccionario de la Pizza EN (cerrada y publicada; fijados el 27-oct-2026 sobre e2da040e). Si cambian, hay que
# re-extraer y rehacer preparar_tandas antes de los traductores (bp9.py verificar avisa)
SHA_PIZ = OrderedDict([
    ('textos_es.json', None), ('textos_en/GM.json', None), ('textos_en/GR.json', None),
    ('textos_en/GPIZ-plan.json', None), ('textos_en/GPIZ-check.json', None), ('formulas_piz.json', None),
    ('censo_es.json', None), ('cifras_caso.json', None),
])
_SHA_FIJADOS = os.path.join(AQUI, 'sha_piz.json')
if os.path.exists(_SHA_FIJADOS):
    SHA_PIZ.update(json.load(open(_SHA_FIJADOS, encoding='utf-8')))


def _sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def diccionario_ok():
    """[] si los ficheros del diccionario de la Pizza EN siguen con el sha256 fijado (sha_piz.json); si no, los que
    cambiaron."""
    out = []
    for rel, sha in SHA_PIZ.items():
        p = os.path.join(PIZ, rel)
        if not os.path.exists(p):
            out.append('business-plans-en-8/%s: falta' % rel)
        elif sha is None:
            out.append('business-plans-en-8/%s: sin sha256 fijado (bp9.py verificar --fijar)' % rel)
        elif _sha(p) != sha:
            out.append('business-plans-en-8/%s: sha256 distinto del fijado en sha_piz.json' % rel)
    return out


def fijar_sha():
    d = OrderedDict((rel, _sha(os.path.join(PIZ, rel))) for rel in SHA_PIZ)
    json.dump(d, open(_SHA_FIJADOS, 'w', encoding='utf-8'), indent=1)
    return d


def vocabulario_finca():
    """VOCABULARIO de la finca (a.py del motor ES) por ast, sin importar el motor."""
    if not os.path.exists(A_FINCA):
        return {}
    arbol = ast.parse(open(A_FINCA, encoding='utf-8').read())
    for nodo in arbol.body:
        if isinstance(nodo, ast.Assign) and any(getattr(t, 'id', '') == 'VOCABULARIO' for t in nodo.targets):
            return ast.literal_eval(nodo.value)
    return {}


def normalizadores():
    """Dos variantes de la inversa (invitado → cubierto / → comensal), la clave más larga primero (inventario_delta)."""
    voc = vocabulario_finca()
    out = []
    for preferida in ('cubiert', 'comensal'):
        inv = {}
        for k, v in voc.items():
            if len(v) > 140 or len(k) > 140:
                continue
            if v in inv and not k.startswith(preferida):
                continue
            inv[v] = k
        if not inv:
            continue
        claves = sorted(inv, key=len, reverse=True)
        rx = re.compile('|'.join(r'(?<![\wáéíóúñ])%s(?![\wáéíóúñ])' % re.escape(c) for c in claves))
        out.append((rx, inv))
    return out


NORMS = normalizadores()


def normalizar(t):
    """Variantes normalizadas del ES (sin repetir el original)."""
    out = []
    for rx, inv in NORMS:
        n = rx.sub(lambda m: inv[m.group(0)], t)
        if n != t and n not in out:
            out.append(n)
    return out


def _cargar():
    """es → registro con el EN de la PRIMERA fuente (orden de FUENTES), solo cadenas «traducir»."""
    out = OrderedDict()
    for carpeta, grupos, et in FUENTES:
        te_p = os.path.join(carpeta, 'textos_es.json')
        if not os.path.exists(te_p):
            continue
        te = json.load(open(te_p, encoding='utf-8'))
        en = {}
        for g in grupos:
            p = os.path.join(carpeta, 'textos_en', g + '.json')
            if os.path.exists(p):
                d = json.load(open(p, encoding='utf-8'))
                rev = os.path.join(carpeta, 'textos_en', g + '.revision.json')
                if os.path.exists(rev):
                    d.update(json.load(open(rev, encoding='utf-8')))
                po = os.path.join(carpeta, 'textos_en', 'overrides_%s.json' % g)
                if os.path.exists(po):
                    for ident, o in json.load(open(po, encoding='utf-8')).items():
                        if ident in d and isinstance(o, dict) and 'texto' in o:
                            d[ident] = o['texto']
                en[g] = d
        for c in te['cadenas']:
            g = c['grupo']
            if g not in en or c['id'] not in en[g] or c['tratamiento'] != 'traducir' or c['es'] in out:
                continue
            out[c['es']] = OrderedDict([
                ('es', c['es']), ('en', en[g][c['id']]), ('grupo', g), ('id', c['id']),
                ('tratamiento_origen', 'traducir'), ('conjunto', et), ('motor', (carpeta, g) in GM_MOTOR),
                ('donde', ['%s %s!%s' % (d['f'], d.get('h', ''), d.get('c', '')) for d in c['donde'][:2]])])
    return out


TEXTO = _cargar()


def propuesta_de(e):
    """(registro, origen) del EN reutilizable de una cadena de la finca, o (None, None). origen: 'texto' (ES exacto) o
    'texto-norm' (ES casado tras normalizar el vocabulario de la finca)."""
    es = e['es']
    if es in TEXTO:
        return TEXTO[es], 'texto'
    for n in normalizar(es):
        if n in TEXTO:
            return TEXTO[n], 'texto-norm'
    return None, None


def _limpia(en):
    return not RX_REESCRIBIR.search(en or '')


def grupo_de(planes, texto=None, tratamiento=None, donde=None):
    donde = donde or []
    libros = {o['f'] for o in donde}
    destino = 'GWED-check' if libros == {'WEDC'} else 'GWED-plan'
    if any(o.get('det') == 'D19' for o in donde):
        return 'GWED-plan'                                   # D165: las 14 filas cambian enteras
    if tratamiento != 'traducir':
        return destino
    prop, origen = propuesta_de({'es': texto, 'donde': donde})
    if not prop or not _limpia(prop['en']):
        return destino
    if origen == 'texto' and prop['motor']:
        return 'GM'
    if destino == 'GWED-check':
        return 'GWED-check'                                  # checklist: con propuesta y la tarea US de D169 (pista)
    return 'GR'


def reuso_de(e):
    """EN del diccionario (GM / GR) o PROPUESTA para los traductores. D19: sin propuesta (D165)."""
    if any(o.get('det') == 'D19' for o in e['donde']) or e['tratamiento'] != 'traducir':
        return None
    prop, origen = propuesta_de(e)
    if not prop:
        return None
    return OrderedDict([('grupo', prop['grupo']), ('id', prop['id']), ('en', prop['en']),
                        ('tratamiento_origen', prop['tratamiento_origen']), ('conjunto', prop['conjunto']),
                        ('origen', origen), ('donde', prop['donde'])])


# ==========================================================================
# instalar
# ==========================================================================
def instalar(M):
    """Sustituye en el módulo `mapas` (M) los datos de FT/CAF por los de la finca (wedding venue)."""
    from datos_wed import completar                                        # contenido (FIJOS, caso US, docx…)
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
    M.REUSO = OrderedDict()                     # el reuso es por TEXTO (propuesta_de)
    M.FUENTES_CIFRAS = [os.path.join(BP, 'F1-research-us.md'), os.path.join(BP, 'SPEC.md'),
                        os.path.join(BP2, 'F1-research-us-delta.md'), os.path.join(BP2, 'SPEC-delta.md'),
                        os.path.join(PIZ, 'F1-research-us-delta.md'), os.path.join(PIZ, 'SPEC-delta.md'),
                        os.path.join(AQUI, 'F1-research-us-delta.md'), os.path.join(AQUI, 'SPEC-delta.md')]
    M.NOTAS_F2 = os.path.join(AQUI, 'F2-NOTAS.md')
    # G4 (pizza F2-NOTAS §5.1 y §7): el checklist ES trae la DV "✓,—,N/A" con las celdas OK en «☐» (defecto sistémico
    # del motor ES nuevo, también en la finca). En el EN la lista pasa a "✓,☐,N/A" (la del Bar EN), coherente con
    # Instrucciones. «—» no tiene letras y `necesita_clave` lo dejaba fuera de CLAVES: solo en este conjunto se le da clave.
    M.CLAVES['—'] = '☐'
    _nc = M.necesita_clave
    M.necesita_clave = lambda lit, _nc=_nc: lit == '—' or _nc(lit)
    completar(M)
