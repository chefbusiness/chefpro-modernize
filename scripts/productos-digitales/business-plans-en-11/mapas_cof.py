#!/usr/bin/env python3
"""
mapas_cof.py — Coffee Cart Business Plan Kit (EN) · datos ES→EN del conjunto «cof» (estructura).

SPEC: `SPEC-delta.md` (D216-D235) sobre las heredadas (`../business-plans-en-7/SPEC-delta.md` D114-D132 = PAELLA, `-6/`
D96-D113, `-5/` D81-D95, `-4/` D66-D80, `-3/` D48-D65, `-2/` D30-D47, `../business-plans-en/SPEC.md` D1-D29; contrato de
`-9/` D171, bloque Escandallo de `-8/`). Sesión Claude Code, 28-oct-2026 (F1 + paso 1a). NO se ejecuta solo: lo importa
`../business-plans-en/mapas.py` cuando `BP_CONJUNTO=cof` y llama a `instalar(M)`. Clon de `../business-plans-en-7/
mapas_pael.py` (D221).

Como la paella y el BBQ: la FUENTE ES DEL CIRCUITO es el FOOD TRUCK ES (ranuras de celdas y párrafos) y el motor es el de
eventos (B4 = eventos/año, B5 = precio por invitado, B6 = invitados por evento; los 7 parches, con el Break-Even en ±$1 /
+$2: el precio medio del café es $12.60, D220). El DICCIONARIO DE REUSO POR CELDA va EN CADENA (D221): primero el EN de la
PAELLA cerrada y LIVE en ESA celda (`../business-plans-en-7/textos_es.json` + `textos_en/{GM,GRB-plan,GLB-check,GPA-plan,
GPA-check}.json` con sus `.revision.json` encima; 10 sha256 en SHA_PAEL) y, si la paella no tiene EN en esa celda, el EN
publicado del catering (los mismos 8 sha256 de siempre): 18 en total, que `bp11.py verificar` comprueba. El contenido de
café sale de las pistas, de `fuente_es_cof.json` (cafetería móvil ES 1.0, en construcción el 28-oct: paso 1c) y de research.

    python3 bp11.py mapas           # autotest + cruce con censo_es.json + verificar (incluye los 18 sha256)

Grupos (D221; mismo esquema que la paella, «solo lo que de verdad cambia»):
  GM          motor común cuyo EN (paella = BBQ = catering) no trae vocabulario que no valga para el café: no va a nadie.
  GRP-plan    EN de la paella (o del catering) reutilizable con revisión (notas del motor, tabla D18, filas D19 con
              propuesta limpia): preparar_tandas escribe su EN; la tanda GCF-plan las revisa (GRP-plan.revision.json).
  GCF-plan    se escriben para el coffee caterer: las del plan cuyo EN de la paella trae vocabulario o caso de paella
              (RX_REESCRIBIR), las 51 forzadas (notas del caso), las sin EN y las celdas D19 sin propuesta o sucias.
  GLP-check   checklist: celdas cuya propuesta de la paella vale tal cual (tareas «L» y columnas que no cambian de las
              «A»; columna C con «Paella chef» → «Lead barista», transformación mecánica de D228): no van a nadie.
  GCF-check   checklist: las celdas que cambian (vocabulario de paella, columnas marcadas y las 4 de las tareas nuevas).
"""
import hashlib
import json
import os
import re
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
BP = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
CAT = os.path.join(os.path.dirname(AQUI), 'business-plans-en-4')
PAEL = os.path.join(os.path.dirname(AQUI), 'business-plans-en-7')

# ==========================================================================
# 0. Producto (D216-D218). dir_es = FUENTE DEL CIRCUITO (food truck ES); slug_es = gemelo ES para hreflang (D216)
# ==========================================================================
PLANES = OrderedDict([
    ('cof', OrderedDict([
        ('slug', 'coffee-cart-business-plan'),
        ('producto', 'Coffee Cart Business Plan Kit'),
        ('slug_es', 'plan-negocio-cafeteria-movil-eventos'),
        ('dir_es', 'astro-site/public/dl/plan-negocio-food-truck'),
        ('env_stripe', 'VITE_STRIPE_PAYMENT_LINK_COFFEE_CART_BUSINESS_PLAN'),
        ('keywords', 'coffee cart business plan, coffee truck business plan, mobile coffee business plan, coffee '
                     'trailer business plan, how to start a coffee cart business, coffee catering, AI Chef Pro'),
    ])),
])
for _p in PLANES.values():
    _p['url'] = 'aichef.pro/en/digital-products/' + _p['slug']
    _p['dir_en'] = 'astro-site/public/dl/' + _p['slug']

LIBROS = OrderedDict([
    ('COFP', ('cof', 'plan-financiero-food-truck.xlsx', 'coffee-cart-financial-projections.xlsx',
              'Coffee Cart Financial Projections: 3-Year P&L, Cash Flow & Financing')),
    ('COFC', ('cof', 'checklist-apertura-food-truck.xlsx', 'coffee-cart-startup-checklist.xlsx',
              'Coffee Cart Startup Checklist (68 Tasks)')),
])
DOCX = OrderedDict([
    ('cof', ('plan-de-negocio-food-truck.docx', 'coffee-cart-business-plan.docx',
             'Coffee Cart Business Plan (10 Sections)')),
])
TIPO_DE = {'COFP': 'plan', 'COFC': 'check'}
A_PAEL = {'COFP': 'PAEP', 'COFC': 'PAEC'}                 # libro de la paella que hace de diccionario (1.º de la cadena)
A_CAT = {'COFP': 'CATP', 'COFC': 'CATC'}                  # libro del catering (2.º de la cadena)

# ==========================================================================
# 1. Pestañas: plan = FT; checklist = FT con la fase 2 «Permits & Commissary» (D228: 30 caracteres ≤ 31; research §9
#    proponía «Phase 2 - Cart, Permits & Commissary», que tiene 36; el título de la hoja, sin límite, es «PHASE 2:
#    COMMISSARY, CART & TRAILER, HEALTH PERMIT & INSURANCE»)
# ==========================================================================
_HOJAS_PLAN = OrderedDict([
    ('0. Supuestos', '0. Assumptions'), ('Inversión Inicial', 'Startup Costs'), ('PyG 3 Años', '3-Year P&L'),
    ('Punto Equilibrio', 'Break-Even'), ('Escenarios', 'Scenarios'), ('Personal', 'Staffing'),
    ('Instrucciones', 'Instructions'), ('Tesorería 12 meses', '12-Month Cash Flow'), ('Financiación', 'Financing'),
])
HOJA_F2_EN = 'Phase 2 - Permits & Commissary'
assert len(HOJA_F2_EN) <= 31
_HOJAS_CHECK = OrderedDict([
    ('F1 - Constitución', 'Phase 1 - Business Setup'), ('F2 - Vehículo', HOJA_F2_EN),
    ('F3 - Equipamiento', 'Phase 3 - Equipment'), ('F4 - Personal', 'Phase 4 - Staff'),
    ('F5 - Marketing', 'Phase 5 - Marketing'), ('F6 - 90 Días', 'Phase 6 - First 90 Days'),
    ('Instrucciones', 'Instructions'),
])
HOJAS_POR_LIBRO = OrderedDict([('COFP', _HOJAS_PLAN), ('COFC', _HOJAS_CHECK)])
HOJAS_ES_POR_LIBRO = OrderedDict((c, list(d)) for c, d in HOJAS_POR_LIBRO.items())
TAREAS_POR_FASE = OrderedDict([('COFC', [11, 13, 12, 10, 12, 10])])          # 68 (D228 = rejilla de la paella)
MOLDE_CHECK = OrderedDict([('COFC', 'hojas')])
COL_OK = OrderedDict([('COFC', 1)])
FASES_CABECERA = OrderedDict()
FILAS_TAREA = OrderedDict([('F1 - Constitución', (5, 15)), ('F2 - Vehículo', (5, 17)), ('F3 - Equipamiento', (5, 16)),
                           ('F4 - Personal', (5, 14)), ('F5 - Marketing', (5, 16)), ('F6 - 90 Días', (5, 14))])

# ==========================================================================
# 2. Fórmulas: los 7 parches de la paella con los escalones del Break-Even en ±$1 / +$2 por invitado (D220: el precio
#    medio del café es $12.60; ±$3 sería un 24 % del precio)
# ==========================================================================
_E2_ALC = ("('0. Supuestos'!$B$62*'0. Supuestos'!$B$40+(1-'0. Supuestos'!$B$62)*'0. Supuestos'!$B$39)")
PARCHES_FORMULA = OrderedDict([
    (('COFP', 'PyG 3 Años', 'G13'), ("'0. Supuestos'!$B$39", "'0. Supuestos'!$B$41")),
    (('COFP', 'PyG 3 Años', 'G14'), (_E2_ALC, "'0. Supuestos'!$B$41")),
    (('COFP', 'Personal', 'B20'), ("'0. Supuestos'!$B$6", "'0. Supuestos'!$B$4")),
    (('COFP', 'Personal', 'C9'), ('SUM(C5:C8)', 'SUMPRODUCT(B5:B8,C5:C8)')),
    (('COFP', 'Punto Equilibrio', 'B31'), ('$B$8-2', '$B$8-1')),
    (('COFP', 'Punto Equilibrio', 'D31'), ('$B$8+2', '$B$8+1')),
    (('COFP', 'Punto Equilibrio', 'E31'), ('$B$8+4', '$B$8+2')),
])

# ==========================================================================
# 3. Instrucciones: versión D20 y aviso D21; zonas celda a celda: D18 (35-51), D19 (55-68) y las 68 tareas (B-E)
# ==========================================================================
FILA_VERSION = OrderedDict([('COFP', 73), ('COFC', 11)])
ZONAS_CELDA = OrderedDict([(('COFP', 'Instrucciones'), [(35, 51, 'ABCD', 'D18'), (55, 68, 'ABCD', 'D19')])])
for _h, (_f1, _f2) in FILAS_TAREA.items():
    ZONAS_CELDA[('COFC', _h)] = [(_f1, _f2, 'BCDE', 'TAREA')]

# ==========================================================================
# 4. Docx (D229): las 131 ranuras del FT ES, H1 en 37·44·51·59·67·76·83·91·100·109; último de §9 = 108 (nota UK)
# ==========================================================================
DOCX_N_PARRAFOS = OrderedDict([('cof', 131)])
DOCX_ENCABEZADOS = OrderedDict([('cof', [37, 44, 51, 59, 67, 76, 83, 91, 100, 109])])
DOCX_INDICE = OrderedDict([('cof', list(range(24, 34)))])
DOCX_ULTIMO_9 = OrderedDict([('cof', '108')])
DOCX_TANDAS = OrderedDict([('cof_a', ('cof', [1, 2, 3, 4, 5])), ('cof_b', ('cof', [6, 7, 8, 9, 10]))])
PRESTAMO_SEMILLA = OrderedDict([('cof', 71000)])                    # punto fijo del dry-run del paso 1a (68,000 → 71,000 → 71,000)

AUTOTEST = OrderedDict([
    ('P1', 'COFP'), ('P2', 'COFP'), ('C1', 'COFC'), ('C2', 'COFC'),
    ('C1_hoja_papel', 'F2 - Vehículo'), ('C1_titulo', 'Coffee Cart Startup Checklist (68 Tasks)'),
    ('C2_hoja_no_latino', 'F5 - Marketing'), ('P1_celda_texto', 'A3'), ('P1_celda_formula', 'B9'),
    ('P1_merge', 'A30:C30'),
])

# ==========================================================================
# 5. Grupos (D221 + «solo lo que cambia»)
# ==========================================================================
GRUPOS = ('GM', 'GRP-plan', 'GLP-check', 'GCF-plan', 'GCF-check')
GRUPOS_TRADUCTORES = ('GCF-plan', 'GCF-check')
GRUPOS_OVERRIDES = ('GCF-plan', 'GCF-check')
REVISAR_EN_TANDA = OrderedDict([('GCF-plan', ('GRP-plan',))])
GRUPOS_DESC = OrderedDict([
    ('GM', 'REUTILIZADAS: motor común cuyo EN (el de la Paella, que es el del BBQ y el del Catering publicado) no trae '
           'vocabulario ni caso de la paella. preparar_tandas escribe su EN. No van a los redactores'),
    ('GRP-plan', 'REUTILIZADAS con revisión: EN de la Paella (o del Catering) en ESA celda que vale para un coffee '
                 'caterer salvo matices (notas del plan, método D18, filas D19 con propuesta limpia). preparar_tandas '
                 'escribe su EN; la tanda GCF-plan las revisa en textos_en/GRP-plan.revision.json (solo las que cambian)'),
    ('GLP-check', 'REUTILIZADAS tal cual: celdas del checklist cuya propuesta de la Paella vale para el café (tareas que '
                  'sobreviven y columnas que no cambian; «Paella chef» → «Lead barista» en la columna C). No van a nadie'),
    ('GCF-plan', 'Plan financiero (COFP) que se ESCRIBE para el coffee caterer: celdas cuyo EN de la Paella trae '
                 'vocabulario o caso de paella (propuesta = ese EN), las 51 forzadas (notas del caso), las sin EN y las '
                 'celdas D19 sin propuesta (12 filas nuevas) o con propuesta sucia'),
    ('GCF-check', 'Checklist (COFC): las celdas que CAMBIAN de las 68 tareas (columnas marcadas de las tareas que se '
                  'ajustan, las 4 de las tareas nuevas y toda celda con vocabulario de paella), con la propuesta de la '
                  'Paella'),
    ('GX', 'NO se traduce: pestañas (mapas.HOJAS_POR_LIBRO), CLAVES, FIJOS, POR_CELDA, versión, pie y docProps'),
])

# Vocabulario y caso de la PAELLA (y lo que sigue vetado del catering y del BBQ) que NO vale para un coffee caterer
# (F1-inventario §3). Clasifica las PROPUESTAS, no es el gate (RX_COF_NO de datos_cof). Frente a la paella: «stations»,
# «trailer» y «festival» SÍ valen aquí (dos estaciones de espresso, remolque cerrado, mercados y festivales guest-pay)
_CASO_PAEL = (r'313,200|344,520|365,191|49,480|88,966|64,000|44,700|39,227|20,319|\b135 events\b|\$40(?:\.00)?\b|'
              r'\b58 guests\b|\b116 events\b|\b200 events\b|\$2,320|\b101 events\b|\b169 events\b')
RX_REESCRIBIR = re.compile(
    r'(?i)\bpaellas?\b|socarrat|sofrito|saffron|\bbomba\b|\brice\b|seafood|shellfish|shellstock|mussels?|clams?|'
    r'\bpans?\b|\bburners?\b|propane|cylinders?|\btapas\b|sangria|Valencian?|\bSpanish\b|chorizo|aioli|fideua|'
    r'\bvans?\b|upfit|\bcooking (?:station|tent|canopy|fuel)|open flame|wind guards?|fish stock|B\. cereus|'
    r'\bchicken\b|lobster|\bTPHC\b|time as a public health control|\bburn bans?\b|wood-fire|'
    r'\bsmok|\bpitmasters?\b|\bpits?\b|brisket|\bmeats?\b|\bcarv(?:e|ed|ing|er|ers)\b|\bBBQ\b|barbecue|\bgrill|'
    r'\bplated\b|family-style|chef-attended|\bthemed\b|(?<!AI )\bchefs?\b|\bsous\b|induction|\bovens?\b|reach-in|'
    r'\btaco|\bpasta\b|cuisine|refrigerat|ezCater|\bbuffets?\b|insulated (?:food )?carriers|hotel pans?|chafing|'
    r'\bservers?\b|buffet attendants?|drop-off|marketplace|' + _CASO_PAEL)

# sha256 del diccionario en cadena (D221): 10 de la Paella cerrada y LIVE (`../business-plans-en-7/`, fijados el
# 28-oct-2026 sobre d8984ffd) + los 8 del catering publicado (`../business-plans-en-4/`, los mismos de mapas_pael)
SHA_PAEL = OrderedDict([
    ('textos_es.json', '30b07f0339d7e02a9e9e5c61f2926c841f8aa17df89fcaaaf082e2d9cce25927'),
    ('textos_en/GM.json', 'd9a2a597eccff769d34461c2a797f25973d569c1f96bff2ea20db7e6dbaa6943'),
    ('textos_en/GRB-plan.json', '95cafd3ec2348249b46ceef838801b3b886743412d70ae9bebb0953cb7401252'),
    ('textos_en/GRB-plan.revision.json', '11963df99a2c562db91eec31a5faf06d7ab92b0260574e5dffb2725684b61e09'),
    ('textos_en/GLB-check.json', 'd48e825a10eeb8972ac285898bb1fd46997684c505baafe40384a56f997f5cfb'),
    ('textos_en/GLB-check.revision.json', 'a37f1cd3fb714767fc88dad9899cce1171a971ee93845cfcac7d3e1a30ebb9e7'),
    ('textos_en/GPA-plan.json', 'eff91d03ab6507c8bd0eebea27e6999f4f33d7ab1088d4691d75ae75e774ff0e'),
    ('textos_en/GPA-check.json', '4a69a98fd4393c8362a0928d6ab67353fb7cd983ee80cdaea9b79dd7237e3348'),
    ('docx_en_pael_a.json', '1b3708f01beb1c08fa3b00cdc00178c1173f78b3782aec846ec6e93156d67415'),
    ('docx_en_pael_b.json', '90d2a3cacd48b3f9347af88290c7d1256814ab521616b21ae718e5e8872b7436'),
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
_GRUPOS_PAEL = ('GM', 'GRB-plan', 'GLB-check', 'GPA-plan', 'GPA-check')
_REV_PAEL = ('GRB-plan.revision.json', 'GLB-check.revision.json')
_GRUPOS_CAT = ('GM', 'GR', 'GCAT-plan', 'GCAT-check')


def _sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def diccionario_ok():
    """[] si los 18 ficheros del diccionario en cadena (10 de la paella + 8 del catering) siguen con el sha256 fijado; si
    no, la lista de los que cambiaron (hay que re-extraer y rehacer preparar_tandas antes de los redactores)."""
    out = []
    for base, tabla, nombre in ((PAEL, SHA_PAEL, 'SHA_PAEL'), (CAT, SHA_DICCIONARIO, 'SHA_DICCIONARIO')):
        for rel, sha in tabla.items():
            p = os.path.join(base, rel)
            if not os.path.exists(p):
                out.append('%s/%s: falta' % (os.path.basename(base), rel))
            elif _sha(p) != sha:
                out.append('%s/%s: sha256 distinto del fijado en mapas_cof.%s' % (os.path.basename(base), rel, nombre))
    return out


def _en_de(base, grupos, revisiones):
    en = OrderedDict()
    for g in grupos:
        p = os.path.join(base, 'textos_en', g + '.json')
        if os.path.exists(p):
            en.update(json.load(open(p, encoding='utf-8')))
    for r in revisiones:
        rev = os.path.join(base, 'textos_en', r)
        if os.path.exists(rev):
            en.update(json.load(open(rev, encoding='utf-8')))         # ya va dentro del .json; idempotente
    return en


# Transformación mecánica de la columna C del checklist (D228): los papeles de la paella → los del café
RX_COL_C = re.compile(r'[A-Z]+')
_ROLES_C = (('Paella chef / Event captain', 'Lead barista'), ('Event captain / Event staff', 'Lead barista / Event '
            'baristas'), ('Paella chef / Driver', 'Lead barista / Driver'), ('Owner / Event captain', 'Owner / Lead '
            'barista'), ('Paella chef', 'Lead barista'), ('Event captain', 'Lead barista'), ('Event staff', 'Event '
            'baristas'))


def _mecanica(f, c, en):
    if f == 'PAEC' and RX_COL_C.match(c or '') and RX_COL_C.match(c).group(0) == 'C':
        for a, b in _ROLES_C:
            en = en.replace(a, b)
        return en.replace('Owner / Lead barista / Lead barista', 'Owner / Lead barista')
    return en


def _cargar(base, grupos, revisiones, libros, plan_etq):
    te_p = os.path.join(base, 'textos_es.json')
    celda, texto = OrderedDict(), OrderedDict()
    if not os.path.exists(te_p):
        return celda, texto
    en = _en_de(base, grupos, revisiones)
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


PAEL_CELDA, PAEL_TEXTO = _cargar(PAEL, _GRUPOS_PAEL, _REV_PAEL, ('PAEP', 'PAEC'), 'pael')
CAT_CELDA, CAT_TEXTO = _cargar(CAT, _GRUPOS_CAT, ('GR.revision.json',), ('CATP', 'CATC'), 'cat')
_ORIGEN = {'pael': 'business-plans-en-7 (Paella EN cerrada y LIVE)', 'cat': 'business-plans-en-4 (Catering EN publicado)'}

# celdas que van a los redactores aunque su EN de la paella parezca limpio: las 51 de mapas_pael.FORZAR_TRADUCTORES
# (notas del caso: C4-C8, C11-C15, C18, C24-C27, C44-C62, Startup D7:D20, P&L F10-F55, Staffing J), D221, + 36 del café
_S, _I, _P, _R = '0. Supuestos', 'Inversión Inicial', 'PyG 3 Años', 'Personal'
FORZAR_TRADUCTORES = set(
    [('COFP', _S, c) for c in ('C4', 'C5', 'C6', 'C7', 'C8', 'C11', 'C12', 'C13', 'C15', 'C18', 'C24', 'C26', 'C27',
                               'C44', 'C45', 'C51', 'C52', 'C54', 'C55', 'C58', 'C62')] +
    [('COFP', _I, 'D%d' % f) for f in range(7, 21)] +
    [('COFP', _P, c) for c in ('F10', 'F11', 'F24', 'F32', 'F33', 'F34', 'F35', 'F53', 'F54', 'F55')] +
    [('COFP', _R, c) for c in ('J5', 'J6', 'J7', 'J8', 'J18', 'J19')] +
    # paso 1a: las celdas con pista propia del café cuya propuesta de la paella parecía limpia (irían a GRP-plan, y la
    # lista de revisión de preparar_tandas no lleva pistas): canal de festivales, umbrales, escenarios, Word y método D18
    [('COFP', _S, c) for c in ('C25', 'C30', 'C63')] +
    [('COFP', _P, c) for c in ('F16', 'F51', 'F56')] +
    [('COFP', 'Escenarios', 'E23'), ('COFP', 'Instrucciones', 'A12')] +
    [('COFP', 'Instrucciones', '%s%d' % (c, f)) for f in (39, 41, 42, 43, 44, 49, 50) for c in 'ABCD'])
# D225: filas de la tabla D19 que heredan la PROPUESTA de la paella (misma fila): shared kitchen (65) y seguros
# Insureon (67). Las otras 12 son nuevas (research §4-§6)
D19_CON_PROPUESTA = (65, 67)


def propuesta_de(donde, es=None):
    """[(EN, grupo, id, tratamiento, origen)] por aparición en celda: primero la paella en esa celda, si no el catering;
    si la cadena no tiene ninguna aparición en celda (mensaje de DV…), el EN del mismo texto ES (paella, luego catering)."""
    out = []
    for o in donde or []:
        if o.get('t') != 'celda':
            continue
        k = (A_PAEL.get(o['f']), o.get('h'), o.get('c'))
        if k in PAEL_CELDA:
            out.append(PAEL_CELDA[k] + ('pael',))
            continue
        k = (A_CAT.get(o['f']), o.get('h'), o.get('c'))
        if k in CAT_CELDA:
            out.append(CAT_CELDA[k] + ('cat',))
    if not out and not any(o.get('t') == 'celda' for o in donde or []):
        if es in PAEL_TEXTO:
            out.append(PAEL_TEXTO[es] + ('pael',))
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
    """Columnas que la pista marca como «cambia» en esa fila de tarea (datos_cof.TAREAS_COF)."""
    from datos_cof import COLS_CAMBIAN                                      # noqa: E402 (import perezoso)
    return _col(o) in COLS_CAMBIAN.get((o['h'], _fila(o)), '')


def grupo_de(planes, texto=None, tratamiento=None, donde=None):
    donde = donde or []
    libros = {o['f'] for o in donde}
    prop = propuesta_de(donde, texto)
    limpia = bool(prop) and len({x[0] for x in prop}) == 1 and not RX_REESCRIBIR.search(prop[0][0])
    tarea = [o for o in donde if o.get('det') == 'TAREA']
    if tarea:                                          # las 68 tareas × 4 columnas
        return 'GLP-check' if limpia and not any(_cambia_tarea(o) for o in tarea) else 'GCF-check'
    d19 = [o for o in donde if o.get('det') == 'D19']
    if d19:                                            # tabla de research (D225)
        return 'GRP-plan' if limpia and all(_fila(o) in D19_CON_PROPUESTA for o in d19) else 'GCF-plan'
    destino = 'GCF-check' if libros == {'COFC'} else 'GCF-plan'
    if any((o['f'], o.get('h'), o.get('c')) in FORZAR_TRADUCTORES for o in donde):
        return destino
    if not limpia:
        return destino                                 # sin EN, con EN distinto por celda o con vocabulario de paella
    if prop[0][1] == 'GM' and tratamiento == 'traducir':
        return 'GM'
    return 'GLP-check' if libros == {'COFC'} else 'GRP-plan'


def reuso_de(e):
    """EN de la PRIMERA celda de la cadena en la cadena paella → catering: el EN de GM / GRP-plan / GLP-check o la
    PROPUESTA de los redactores. D19: solo las 2 filas de D19_CON_PROPUESTA (D225); las otras 12, sin propuesta."""
    d19 = [o for o in e['donde'] if o.get('det') == 'D19']
    if d19 and not all(_fila(o) in D19_CON_PROPUESTA for o in d19):
        return None
    prop = propuesta_de(e['donde'], e['es'])
    if not prop:
        return None
    en, g, ident, tr, origen = prop[0]
    libro = A_PAEL if origen == 'pael' else A_CAT
    return OrderedDict([('grupo', g), ('id', ident), ('en', en), ('tratamiento_origen', tr),
                        ('conjunto', _ORIGEN[origen]),
                        ('donde', ['%s %s!%s' % (libro.get(o['f']), o.get('h', ''), o.get('c', ''))
                                   for o in e['donde'][:2]])])


# ==========================================================================
# instalar
# ==========================================================================
def instalar(M):
    """Sustituye en el módulo `mapas` (M) los datos de FT/CAF por los del coffee caterer."""
    from datos_cof import completar                                        # contenido (FIJOS, caso US, docx…)
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
    M.REUSO = OrderedDict()                     # el reuso es por CELDA (PAEL_CELDA → CAT_CELDA), no por texto
    M.FUENTES_CIFRAS = [os.path.join(BP, 'F1-research-us.md'), os.path.join(BP, 'SPEC.md'),
                        os.path.join(CAT, 'F1-research-us-delta.md'), os.path.join(PAEL, 'F1-research-us-delta.md'),
                        os.path.join(os.path.dirname(AQUI), 'business-plans-en-5', 'F1-research-us-delta.md'),
                        os.path.join(AQUI, 'F1-research-us-delta.md'), os.path.join(AQUI, 'SPEC-delta.md')]
    M.NOTAS_F2 = os.path.join(AQUI, 'F2-NOTAS.md')
    completar(M)
