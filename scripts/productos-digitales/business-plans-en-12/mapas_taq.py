#!/usr/bin/env python3
"""
mapas_taq.py — Taco Shop Business Plan Kit (EN) · datos ES→EN del conjunto «taq» (estructura).

Fuente de verdad: `../plan-taqueria/F1-camino.md` §6-§7 (EN delta) y `F1-research-us-delta.md` (US §n). Sesión Claude
Code, 29-oct-2026 (F2-EN). NO se ejecuta solo: lo importa `../business-plans-en/mapas.py` cuando `BP_CONJUNTO=taq` y
llama a `instalar(M)`. Clon de `../business-plans-en-10/mapas_taq.py` (circuito refinado: FUENTE_ES fija con SHA_ES,
sin paso 1c, GR/GRC, check_revision, canon, regresión versionada) con el CÓDIGO de la pizza
(`../business-plans-en-8/mapas_piz.py`): el libro ES de la taquería sale de la MISMA semilla que el de la pizzería
(misma rejilla; medido el 29-oct: solo 4 fórmulas de texto distintas, C50, D27, D37 y F13), así que van los parches
E2 (G14), E4 (Staffing!C12) y E5 (G11) de la Pizza EN, G13 → 0 y el DICCIONARIO en cadena, sin normalizar:

  1. EN de la PIZZA EN en la MISMA celda (`../business-plans-en-8/textos_es.json` + `textos_en/{GM,GR,GPIZ-plan,
     GPIZ-check}.json` + `*.revision.json` + `datos_piz.POR_CELDA`); el checklist se casa por POSICIÓN de pestaña
     (las fases 2-4 se renombran);
  2. EN de la Pizza EN por TEXTO;
  3. BAKERY EN por texto (`../business-plans-en-2/`, GPAN/GN con sus `overrides_` de la misma celda);
  4. BAR EN por texto (`../business-plans-en-3/`);
  5. BP/BP2 por texto (GM → REST → CAF → FT).

FUENTE ES: `FUENTE_ES` = `$TAQ_FUENTE_ES` o, sin la variable, `astro-site/public/dl/plan-negocio-taqueria` (el ES FINAL
y revisado de la F2 ES, `f5c5b269`: no hay paso 1c). Grupos:
  GM          motor común: mismo ES que una cadena GM (Pizza EN, Bar EN o BP) con un EN limpio (RX_REESCRIBIR).
  GR · GRC    EN de GPIZ-plan / GPIZ-check / GR de la pizza, de la Bakery, del Bar o de REST/CAF/FT: preparar_tandas lo
              escribe; GR (plan) lo revisa la tanda GTAQ-plan (textos_en/GR.revision.json) y GRC (solo del checklist)
              la tanda GTAQ-check (textos_en/GRC.revision.json).
  GTAQ-plan   nuevas del plan (y las de reuso con vocabulario o caso de otro negocio, con propuesta) + las 13 filas
              D19 (una cadena por celda, sin propuesta).
  GTAQ-check  nuevas del checklist (80 tareas) + los mensajes de la DV con «—» (la DV EN es ✓,☐,N/A).

    python3 bp12.py mapas           # autotest + cruce con censo_es.json + verificar (incluye los sha256)
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

# ==========================================================================
# 0. Producto (F1-camino §6)
# ==========================================================================
FUENTE_ES = os.environ.get('TAQ_FUENTE_ES') or 'astro-site/public/dl/plan-negocio-taqueria'
PLANES = OrderedDict([
    ('taq', OrderedDict([
        ('slug', 'taco-shop-business-plan'),
        ('producto', 'Taco Shop Business Plan Kit'),
        ('slug_es', 'plan-negocio-taqueria'),
        ('dir_es', FUENTE_ES),
        ('env_stripe', 'VITE_STRIPE_PAYMENT_LINK_TACO_SHOP_BUSINESS_PLAN'),
        ('keywords', 'taco shop business plan, taqueria business plan, how to open a taco shop, '
                     'taco shop startup costs, trompo yield, AI Chef Pro'),
    ])),
])
for _p in PLANES.values():
    _p['url'] = 'aichef.pro/en/digital-products/' + _p['slug']
    _p['dir_en'] = 'astro-site/public/dl/' + _p['slug']

LIBROS = OrderedDict([
    ('TAQP', ('taq', 'plan-financiero-taqueria.xlsx', 'taco-shop-financial-projections.xlsx',
              'Taco Shop Financial Projections: 3-Year P&L, Cash Flow & Financing')),
    ('TAQC', ('taq', 'checklist-apertura-taqueria.xlsx', 'taco-shop-startup-checklist.xlsx',
              'Taco Shop Startup Checklist (80 Tasks)')),
])
DOCX = OrderedDict([
    ('taq', ('plan-de-negocio-taqueria.docx', 'taco-shop-business-plan.docx',
             'Taco Shop Business Plan (10 Sections)')),
])
TIPO_DE = {'TAQP': 'plan', 'TAQC': 'check'}
A_PIZ = {'TAQP': 'PIZP', 'TAQC': 'PIZC'}                  # libro de la Pizza EN (diccionario por celda)

# ==========================================================================
# 1. Pestañas: plan = las de la pizza (9, mismos nombres ES); checklist (todas ≤ 31 caracteres; F2 = US §9)
# ==========================================================================
_HOJAS_PLAN = OrderedDict([
    ('0. Supuestos', '0. Assumptions'), ('Inversión Inicial', 'Startup Costs'), ('PyG 3 Años', '3-Year P&L'),
    ('Punto Equilibrio', 'Break-Even'), ('Escenarios', 'Scenarios'), ('Personal', 'Staffing'),
    ('Instrucciones', 'Instructions'), ('Tesorería 12 meses', '12-Month Cash Flow'), ('Financiación', 'Financing'),
])
_HOJAS_CHECK = OrderedDict([
    ('F1 - Constitución', 'Phase 1 - Business Setup'), ('F2 - Local, humos y gas', 'Phase 2 - Hood, Gas & Permits'),
    ('F3 - Cocina, trompo y sanidad', 'Phase 3 - Kitchen & Health'),
    ('F4 - Personal y alérgenos', 'Phase 4 - Staff & Allergens'),
    ('F5 - Carta, marca y delivery', 'Phase 5 - Menu, Brand, Delivery'),
    ('F6 - Apertura y 90 días', 'Phase 6 - Opening & 90 Days'), ('Instrucciones', 'Instructions'),
])
assert all(len(v) <= 31 for v in _HOJAS_CHECK.values())
HOJAS_POR_LIBRO = OrderedDict([('TAQP', _HOJAS_PLAN), ('TAQC', _HOJAS_CHECK)])
HOJAS_ES_POR_LIBRO = OrderedDict((c, list(d)) for c, d in HOJAS_POR_LIBRO.items())
TAREAS_POR_FASE = OrderedDict([('TAQC', [12, 15, 14, 13, 13, 13])])          # 80 (F1-camino §4, mismas filas)
MOLDE_CHECK = OrderedDict([('TAQC', 'hojas')])
COL_OK = OrderedDict([('TAQC', 1)])
FASES_CABECERA = OrderedDict()

# Pestañas ES de la pizza en el MISMO orden (el checklist de la taquería renombra las fases 2-4: se casa por posición)
_HOJAS_PIZ = {
    'TAQP': list(_HOJAS_PLAN),
    'TAQC': ['F1 - Constitución', 'F2 - Local, humos y licencia', 'F3 - Cocina, horno y sanidad',
             'F4 - Personal y prevención', 'F5 - Carta, marca y delivery', 'F6 - Apertura y 90 días', 'Instrucciones'],
}
HOJA_PIZ = {c: dict(zip(HOJAS_ES_POR_LIBRO[c], _HOJAS_PIZ[c])) for c in HOJAS_ES_POR_LIBRO}

# ==========================================================================
# 2. Fórmulas (= Pizza EN, F1-camino §6): E2 solo G14 (G13 es VALOR en el ES → VALORES_EN 0), E4 (Staffing!C12 =
#    Σ personas × FTE: 2 personas de counter en una fila) y E5 (el literal 0.21 de la línea de bebida → B40)
# ==========================================================================
_E2_ALC = ("('0. Supuestos'!$B$62*'0. Supuestos'!$B$40+(1-'0. Supuestos'!$B$62)*'0. Supuestos'!$B$39)")
PARCHES_FORMULA = OrderedDict([
    (('TAQP', 'PyG 3 Años', 'G14'), (_E2_ALC, "'0. Supuestos'!$B$41")),
    (('TAQP', 'Personal', 'C12'), ('SUM(C5:C11)', 'SUMPRODUCT(B5:B11,C5:C11)')),
    (('TAQP', 'PyG 3 Años', 'G11'), ('H11*0.21', "H11*'0. Supuestos'!$B$40")),
])

# ==========================================================================
# 3. Instrucciones: versión D20 y aviso D21 (E1: TAQP A52, TAQC A12; la tabla D19 del ES tiene 12 filas, 35-46, una
#    menos que la pizza); zona D19 (sin D18) por cabecera
# ==========================================================================
FILA_VERSION = OrderedDict([('TAQP', 51), ('TAQC', 11)])
ZONAS_CELDA = OrderedDict([
    (('TAQP', 'Instrucciones'), [(None, None, 'ABCD', 'D19')]),
])

# ==========================================================================
# 4. Docx: las 131 ranuras del FT ES (= PIZ), H1 en 37·44·51·59·67·76·83·91·100·109; último de §9 = 108 (nota UK);
#    tandas taq_a (§1-5) y taq_b (§6-10), 61 ranuras desde el Word ES final (bp12.py extraer_docx)
# ==========================================================================
DOCX_N_PARRAFOS = OrderedDict([('taq', 131)])
DOCX_ENCABEZADOS = OrderedDict([('taq', [37, 44, 51, 59, 67, 76, 83, 91, 100, 109])])
DOCX_INDICE = OrderedDict([('taq', list(range(24, 34)))])
DOCX_ULTIMO_9 = OrderedDict([('taq', '108')])
DOCX_TANDAS = OrderedDict([('taq_a', ('taq', [1, 2, 3, 4, 5])), ('taq_b', ('taq', [6, 7, 8, 9, 10]))])
PRESTAMO_SEMILLA = OrderedDict([('taq', 170000)])                   # research US §8: ≈ $168,700 (punto fijo en F2)

AUTOTEST = OrderedDict([
    ('P1', 'TAQP'), ('P2', 'TAQP'), ('C1', 'TAQC'), ('C2', 'TAQC'),
    ('C1_hoja_papel', 'F2 - Local, humos y gas'), ('C1_titulo', 'Taco Shop Startup Checklist (80 Tasks)'),
    ('C2_hoja_no_latino', 'F5 - Carta, marca y delivery'), ('P1_celda_texto', 'A3'), ('P1_celda_formula', 'B9'),
    ('P1_merge', 'A30:C30'),
])

# ==========================================================================
# 5. Grupos (= heladería: GR del plan y GRC del checklist)
# ==========================================================================
GRUPOS = ('GM', 'GR', 'GRC', 'GTAQ-plan', 'GTAQ-check')
GRUPOS_TRADUCTORES = ('GTAQ-plan', 'GTAQ-check')
GRUPOS_OVERRIDES = ('GTAQ-plan', 'GTAQ-check')
REVISAR_EN_TANDA = OrderedDict([('GTAQ-plan', ('GR',)), ('GTAQ-check', ('GRC',))])
GRUPOS_DESC = OrderedDict([
    ('GM', 'REUTILIZADAS: motor común (mismo ES que una cadena GM de la Pizza EN, del Bar EN o de BP) con un EN sin '
           'vocabulario ni caso de otro negocio. preparar_tandas escribe su EN. No van a los traductores'),
    ('GR', 'REUTILIZADAS con revisión (plan): EN de GPIZ-plan / GPIZ-check / GR de la Pizza EN, de la Bakery EN, del Bar '
           'EN o de REST/CAF/FT. preparar_tandas escribe su EN; la tanda GTAQ-plan las revisa en textos_en/GR.revision.json'),
    ('GRC', 'REUTILIZADAS con revisión (solo del checklist): EN de la Pizza EN (plazos, responsables, cabeceras, tareas). '
            'preparar_tandas escribe su EN; la tanda GTAQ-check las revisa en textos_en/GRC.revision.json'),
    ('GTAQ-plan', 'Nuevas del plan financiero (TAQP) + las de reuso con vocabulario o caso de otro negocio (con '
                  'propuesta) + las 13 filas D19 de Instrucciones (una cadena por celda, sin propuesta)'),
    ('GTAQ-check', 'Nuevas del checklist (TAQC): las 80 tareas, sus cabeceras y los mensajes de la DV (con propuesta '
                   'cuando la Pizza EN tiene el mismo ES)'),
    ('GX', 'NO se traduce: pestañas (mapas.HOJAS_POR_LIBRO), CLAVES, FIJOS, POR_CELDA, versión, pie y docProps'),
])

# Vocabulario y caso de la PIZZA, la PANADERÍA y el BAR que NO vale para la taquería: clasifica las PROPUESTAS (no es
# el gate: ese es datos_taq.RX_TAQ_NO). Una propuesta sucia va a los traductores con su EN como forma. A diferencia de
# la heladería, «covers», «seat turns», «hood», «beer & wine» y «liquor liability» SÍ valen en la taquería
_CASO_PIZ = (r'669,600|709,776|738,167|242,550|329,274|86,724|217,300|39,275|\$36(?:\.00)?\b|\$38\.88|'
             r'\b62 covers\b|\b50 seats\b|\b1,500 sq ft\b')
RX_REESCRIBIR = re.compile(
    r'(?i)\bpizz|\bdough\b|\bovens?\b|Neapolitan|\bVPN\b|firewood|wood-fired|\bflue\b|spark arrestor|\bpeels?\b|'
    r'hearth|mozzarella|San Marzano|Margherita|\b00 flour|\bservers?\b|\bwaitstaff|table service|\btapas\b|'
    r'small plates|\bcocktails?\b|\bspirits\b|\bbartend|happy hour|full liquor|\bbread\b|\bbakery\b|\bbakers?\b|'
    r'\bloa(?:f|ves)\b|pastr(?:y|ies)|croissant|transactions?(?:/day| per day| a day)|' + _CASO_PIZ)

# Términos mexicanos del oficio US con «de/al/con» del español (US §9): el detector de restos no los cuenta (instalar)
TERMINOS_MX = ('al pastor', 'pico de gallo', 'Cinco de Mayo', 'chiles? de [aá]rbol', 'tacos? de (?:lengua|cabeza|canasta)',
               'agua de jamaica', 'carne asada')

# sha256 del diccionario de la Pizza EN (cerrada y publicada; fijados el 27-oct-2026 sobre db6c741b y re-medidos el
# 29-oct en f5c5b269: iguales). Si cambian, hay que re-extraer y rehacer preparar_tandas (bp12.py verificar avisa)
SHA_PIZ = OrderedDict([
    ('textos_es.json', 'c477dc83a61609ec7de3ebe3d23937b27267c7e48000d389271e382ad630319b'),
    ('textos_en/GM.json', '93b2451ebd54ce5584ca4714679b6faa529695c7bfa2fbd843d3508b6482e5de'),
    ('textos_en/GR.json', '5392e3689a7a511fab85a2401afc74f6bf9a9fc4ff522f45348ca250f9ccf0b8'),
    ('textos_en/GM.revision.json', 'b6d5e7768ba1fa4240dd3c055355db4fc17559b3eec0249f57978cbf574d7876'),
    ('textos_en/GR.revision.json', 'fc7cfb4e679c7f30c5571381cc72b9d4bec3094283172fdb5c30e508147941d0'),
    ('textos_en/GPIZ-plan.json', 'a52044a121fd9e28c7931534c3ee54adabe856a186c543c5f13e6aa08a7dc3b6'),
    ('textos_en/GPIZ-check.json', 'c3d62514b899edb9d0aa9a1c32fcaa3517a22229fe4121bd72d2b978d43556da'),
    ('formulas_piz.json', '286b3675b30e2eed71982781e209f4aa063fe4c8be2e7c616ebbd54877caebb2'),
    ('censo_es.json', '2c8a1f63f2b5de0db1d46794327831bc16405744f5fe6e8b0ddc68286708b933'),
    ('datos_piz.py', '44c178d7bb9ae94eb696f26d8f964ba98f510e275e4104ce5baece71e1d2158e'),
])
# sha256 del ES FINAL (F2 ES revisada, f5c5b269 = plan-taqueria/REVISION-FINAL.md): si el ES cambia, manda el ES nuevo
# (re-extraer y avisar)
SHA_ES = OrderedDict([
    ('plan-financiero-taqueria.xlsx', '5778011f9bd918657c364488d145e62163d38996c18eae7e6f280147c21c0ad6'),
    ('checklist-apertura-taqueria.xlsx', '27b6962cdb60e38fa86eb53dca7f411c662ec82134a683d2e4bdd50aa4f4d339'),
    ('plan-de-negocio-taqueria.docx', 'c028c2bb753df9b09b9f023e376e633d6f098468300dbb62424e962ed40d63d5'),
])


def _sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def diccionario_ok():
    """[] si los ficheros del diccionario de la Pizza EN siguen con el sha256 fijado; si no, los que cambiaron."""
    out = []
    for rel, sha in SHA_PIZ.items():
        p = os.path.join(PIZ, rel)
        if not os.path.exists(p):
            out.append('business-plans-en-8/%s: falta' % rel)
        elif _sha(p) != sha:
            out.append('business-plans-en-8/%s: sha256 distinto del fijado en mapas_taq.SHA_PIZ' % rel)
    return out


# ==========================================================================
# 6. Diccionario: Pizza EN por celda → Pizza EN por texto → Bakery → Bar → BP/BP2 (sin normalizar, inv. §6)
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


def _cargar_piz():
    """(por celda {(corto PIZ, hoja ES, celda): entrada}, por texto {es: entrada}) de la Pizza EN cerrada."""
    celda, texto = OrderedDict(), OrderedDict()
    te_p = os.path.join(PIZ, 'textos_es.json')
    if not os.path.exists(te_p):
        return celda, texto
    en = _en_de(PIZ, ('GM', 'GR', 'GPIZ-plan', 'GPIZ-check'))
    por_celda = _modulo('datos_piz_ref_taq', os.path.join(PIZ, 'datos_piz.py')).POR_CELDA
    for c in json.load(open(te_p, encoding='utf-8'))['cadenas']:
        for d in c['donde']:
            if d.get('t') != 'celda':
                continue
            k = (d['f'], d['h'], d['c'])
            if k in por_celda:                                             # override de la pizza en esa celda
                celda[k] = OrderedDict([('es', c['es']), ('en', por_celda[k]), ('grupo', 'POR_CELDA'),
                                        ('id', c['id']), ('tratamiento_origen', 'traducir')])
            elif c['id'] in en and c['tratamiento'] in ('traducir', 'localizar'):
                celda[k] = OrderedDict([('es', c['es']), ('en', en[c['id']]), ('grupo', c['grupo']), ('id', c['id']),
                                        ('tratamiento_origen', c['tratamiento'])])
        if c['id'] in en and c['tratamiento'] == 'traducir':
            texto.setdefault(c['es'], OrderedDict([('es', c['es']), ('en', en[c['id']]), ('grupo', c['grupo']),
                                                   ('id', c['id']), ('tratamiento_origen', 'traducir'),
                                                   ('conjunto', 'business-plans-en-8 (Pizza EN cerrada)'),
                                                   ('donde', _donde(c))]))
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


PIZ_CELDA, PIZ_TEXTO = _cargar_piz()
# Bakery (GPAN/GN, con overrides de GPAN), Bar, y la cadena BP de la pizza (GM → REST → CAF → FT)
PAN_TEXTO = _cargar_texto(BP2, ('GPAN', 'GN'), 'business-plans-en-2 (Bakery EN)', overrides=('GPAN',))
BAR_TEXTO = _cargar_texto(BAR, ('GM', 'GR', 'GBAR-plan', 'GBAR-check'), 'business-plans-en-3 (Bar EN)')
BP_TEXTO = OrderedDict()
for _carpeta, _gs, _et in [(BP, ('GM',), 'business-plans-en (GM)'), (BP2, ('GREST',), 'business-plans-en-2 (REST)'),
                           (BP, ('GCAF',), 'business-plans-en (CAF)'), (BP, ('GFT',), 'business-plans-en (FT)')]:
    for _k, _v in _cargar_texto(_carpeta, _gs, _et, overrides=('GREST',)).items():
        BP_TEXTO.setdefault(_k, _v)
# grupos de ORIGEN que son motor común (GM): su EN por texto no va a nadie si está limpio
_GM_ORIGEN = {('business-plans-en-8 (Pizza EN cerrada)', 'GM'), ('business-plans-en-3 (Bar EN)', 'GM'),
              ('business-plans-en (GM)', 'GM')}


def _celdas(e):
    return [o for o in e['donde'] if o.get('t') == 'celda']


def propuesta_de(e):
    """(entrada de reuso, origen) de una cadena de la taquería, o (None, None). origen: 'celda-piz' (mismo ES en la
    misma celda de la Pizza EN), 'texto-piz', 'texto-pan', 'texto-bar', 'texto-bp'."""
    es = e['es']
    celdas = _celdas(e)
    gem = [PIZ_CELDA.get((A_PIZ.get(o['f']), HOJA_PIZ.get(o['f'], {}).get(o['h']), o['c'])) for o in celdas]
    if celdas and all(x is not None and x['es'] == es for x in gem) and len({x['en'] for x in gem}) == 1:
        x = OrderedDict(gem[0])
        x.setdefault('conjunto', 'business-plans-en-8 (Pizza EN cerrada)')
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


_DV_MSG = ('dv-error', 'dv-prompt', 'dv-error-titulo', 'dv-prompt-titulo')


def grupo_de(planes, texto=None, tratamiento=None, donde=None):
    donde = donde or []
    libros = {o['f'] for o in donde}
    destino = 'GTAQ-check' if libros == {'TAQC'} else 'GTAQ-plan'
    if any(o.get('det') == 'D19' for o in donde):
        return 'GTAQ-plan'                                   # las 13 filas D19 cambian enteras
    if texto and '—' in texto and any(o.get('t') in _DV_MSG for o in donde):
        return 'GTAQ-check'                                  # la DV EN es ✓,☐,N/A; su texto dice ☐, no «—»
    if tratamiento != 'traducir':
        return destino
    prop, origen = propuesta_de({'es': texto, 'donde': donde})
    if not prop or not _limpia(prop['en']):
        return destino
    if (prop.get('conjunto'), prop['grupo']) in _GM_ORIGEN:
        return 'GM'
    return 'GRC' if libros == {'TAQC'} else 'GR'


def reuso_de(e):
    """EN del diccionario (GM / GR) o PROPUESTA para los traductores. D19: sin propuesta."""
    if any(o.get('det') == 'D19' for o in e['donde']) or e['tratamiento'] != 'traducir':
        return None
    prop, origen = propuesta_de(e)
    if not prop:
        return None
    donde = prop.get('donde') or ['%s %s!%s' % (A_PIZ.get(o['f']), HOJA_PIZ.get(o['f'], {}).get(o.get('h'), ''),
                                                o.get('c', '')) for o in _celdas(e)[:2]]
    return OrderedDict([('grupo', prop['grupo']), ('id', prop['id']), ('en', prop['en']),
                        ('tratamiento_origen', prop['tratamiento_origen']),
                        ('conjunto', prop.get('conjunto', 'business-plans-en-8 (Pizza EN cerrada)')),
                        ('origen', origen), ('donde', donde)])


# ==========================================================================
# instalar
# ==========================================================================
def instalar(M):
    """Sustituye en el módulo `mapas` (M) los datos de FT/CAF por los de la taquería."""
    from datos_taq import completar                                        # contenido (FIJOS, caso US, docx…)
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
    M.REUSO = OrderedDict()                     # el reuso es por CELDA de la pizza y luego por texto (propuesta_de)
    M.FUENTES_CIFRAS = [os.path.join(BP, 'F1-research-us.md'), os.path.join(BP, 'SPEC.md'),
                        os.path.join(BP2, 'F1-research-us-delta.md'), os.path.join(BP2, 'SPEC-delta.md'),
                        os.path.join(PIZ, 'F1-research-us-delta.md'), os.path.join(PIZ, 'SPEC-delta.md'),
                        os.path.join(AQUI, 'F1-research-us-delta.md')]
    M.NOTAS_F2 = os.path.join(AQUI, 'F2-NOTAS.md')
    # G4 (heredado de la pizza, F2-NOTAS PIZ §5.1 y §7): el checklist ES de la taquería trae la DV "✓,—,N/A" con las 80
    # celdas OK en «☐» (medido el 29-oct). En el EN la lista pasa a "✓,☐,N/A". «—» no tiene letras y `necesita_clave` lo
    # dejaba fuera de CLAVES: solo en este conjunto se le da clave. «—» no es literal de ninguna fórmula ni CF del ES.
    M.CLAVES['—'] = '☐'
    # Jerga mexicana que el inglés US usa tal cual (US §9): «al pastor», «pico de gallo», «Cinco de Mayo»… llevan
    # artículos o preposiciones del español que el detector de restos (mapas.restos_espanol) marcaría. Como los
    # topónimos US, se retiran del texto ANTES de buscar restos; solo en este conjunto (cero código común)
    M.RX_LUGARES_US = re.compile(M.RX_LUGARES_US.pattern + r'|(?i:\b(?:' + '|'.join(TERMINOS_MX) + r')\b)')
    M.LISTA_BLANCA_TILDE |= {'consomé'}
    _nc = M.necesita_clave
    M.necesita_clave = lambda lit, _nc=_nc: lit == '—' or _nc(lit)
    completar(M)
