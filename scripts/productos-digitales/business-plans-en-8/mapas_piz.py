#!/usr/bin/env python3
"""
mapas_piz.py — Pizza Shop Business Plan Kit (EN) · datos ES→EN del conjunto «piz» (estructura).

SPEC: `SPEC-delta.md` (D133-D155) sobre las heredadas (`../business-plans-en-3/SPEC-delta.md` D48-D65 = BAR, y las
demás hasta D132). Sesión Claude Code, 25-oct-2026 (F2-EN, paso 1a). NO se ejecuta solo: lo importa
`../business-plans-en/mapas.py` cuando `BP_CONJUNTO=piz` y llama a `instalar(M)`. Clon de
`../business-plans-en-3/mapas_bar.py` (D138): el libro de la pizzería es GEMELO del tapas bar ES (731/741 fórmulas
idénticas), así que el molde es el del Bar (plan `_HOJAS_PLAN`, checklist de 6 hojas + Instrucciones, `COL_OK 1`, E2/E4)
y el docx, el del FT ES (131 ranuras, config de PAEL).

FUENTE ES (una sola variable): `FUENTE_ES` = `$PIZ_FUENTE_ES` o, si no está, `astro-site/public/dl/plan-negocio-pizzeria`
(el ES FINAL). El paso 1a corre sobre el dry-run ES copiado a `/root/tmp-pizen/fuente-es/plan-negocio-pizzeria`; el 1c,
sin la variable (F2-NOTAS §6).

DICCIONARIO (D138): primero el EN del BAR EN cerrado en ESA celda (`../business-plans-en-3/textos_es.json` +
`textos_en/{GM,GR,GBAR-plan,GBAR-check}.json` con `GR.revision.json` encima + `datos_bar.POR_CELDA`), luego el EN del Bar
por TEXTO y luego BP/BP2 (la cadena de `mapas_bar._FUENTES_REUSO`). Antes de buscar, el ES de la pizzería se normaliza
«comensal(es)» → «cubierto(s)» (el tapas bar dice «cubiertos»). Grupos:
  GM          mismo ES que el Bar EN en la MISMA celda (sin normalizar) o cadena GM del Bar (motor común), con un EN
              limpio (sin vocabulario ni caso del bar, RX_REESCRIBIR): no va a nadie.
  GR          EN reutilizado de OTRA celda del Bar, de BP/BP2 o casado solo tras la normalización: preparar_tandas lo
              escribe y la tanda GPIZ-plan lo revisa (textos_en/GR.revision.json).
  GPIZ-plan   nuevas del plan (y las del Bar con vocabulario o caso de bar, con propuesta) + las 13 filas D19 (sin
              propuesta: D142 las cambia todas).
  GPIZ-check  nuevas del checklist (80 tareas, casi todo texto nuevo).

    python3 bp8.py mapas            # autotest + cruce con censo_es.json + verificar (incluye los sha256 del Bar EN)
"""
import hashlib
import importlib.util
import json
import os
import re
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
BP = os.path.join(os.path.dirname(AQUI), 'business-plans-en')
BP2 = os.path.join(os.path.dirname(AQUI), 'business-plans-en-2')
BAR = os.path.join(os.path.dirname(AQUI), 'business-plans-en-3')

# ==========================================================================
# 0. Producto (D133-D135). FUENTE_ES: la ÚNICA ruta que cambia entre el paso 1a (dry-run ES) y el 1c (ES final)
# ==========================================================================
FUENTE_ES = os.environ.get('PIZ_FUENTE_ES') or 'astro-site/public/dl/plan-negocio-pizzeria'
PLANES = OrderedDict([
    ('piz', OrderedDict([
        ('slug', 'pizza-shop-business-plan'),
        ('producto', 'Pizza Shop Business Plan Kit'),
        ('slug_es', 'plan-negocio-pizzeria'),
        ('dir_es', FUENTE_ES),
        ('env_stripe', 'VITE_STRIPE_PAYMENT_LINK_PIZZA_SHOP_BUSINESS_PLAN'),
        ('keywords', 'pizza shop business plan, pizzeria business plan, how to open a pizza shop, pizza shop startup '
                     'costs, wood fired pizza oven cost, AI Chef Pro'),
    ])),
])
for _p in PLANES.values():
    _p['url'] = 'aichef.pro/en/digital-products/' + _p['slug']
    _p['dir_en'] = 'astro-site/public/dl/' + _p['slug']

LIBROS = OrderedDict([
    ('PIZP', ('piz', 'plan-financiero-pizzeria.xlsx', 'pizza-shop-financial-projections.xlsx',
              'Pizza Shop Financial Projections: 3-Year P&L, Cash Flow & Financing')),
    ('PIZC', ('piz', 'checklist-apertura-pizzeria.xlsx', 'pizza-shop-startup-checklist.xlsx',
              'Pizza Shop Startup Checklist (80 Tasks)')),
])
DOCX = OrderedDict([
    ('piz', ('plan-de-negocio-pizzeria.docx', 'pizza-shop-business-plan.docx', 'Pizza Shop Business Plan (10 Sections)')),
])
TIPO_DE = {'PIZP': 'plan', 'PIZC': 'check'}
A_BAR = {'PIZP': 'BARP', 'PIZC': 'BARC'}                  # libro gemelo del Bar EN (diccionario por celda)

# ==========================================================================
# 1. Pestañas: plan = las del Bar (FT/CAF); checklist D146 (todas ≤ 31 caracteres)
# ==========================================================================
_HOJAS_PLAN = OrderedDict([
    ('0. Supuestos', '0. Assumptions'), ('Inversión Inicial', 'Startup Costs'), ('PyG 3 Años', '3-Year P&L'),
    ('Punto Equilibrio', 'Break-Even'), ('Escenarios', 'Scenarios'), ('Personal', 'Staffing'),
    ('Instrucciones', 'Instructions'), ('Tesorería 12 meses', '12-Month Cash Flow'), ('Financiación', 'Financing'),
])
_HOJAS_CHECK = OrderedDict([
    ('F1 - Constitución', 'Phase 1 - Business Setup'), ('F2 - Local, humos y licencia', 'Phase 2 - Site, Hood & Permits'),
    ('F3 - Cocina, horno y sanidad', 'Phase 3 - Kitchen, Oven, Health'),
    ('F4 - Personal y prevención', 'Phase 4 - Staff & Safety'),
    ('F5 - Carta, marca y delivery', 'Phase 5 - Menu, Brand, Delivery'),
    ('F6 - Apertura y 90 días', 'Phase 6 - Opening & 90 Days'), ('Instrucciones', 'Instructions'),
])
assert all(len(v) <= 31 for v in _HOJAS_CHECK.values())
HOJAS_POR_LIBRO = OrderedDict([('PIZP', _HOJAS_PLAN), ('PIZC', _HOJAS_CHECK)])
HOJAS_ES_POR_LIBRO = OrderedDict((c, list(d)) for c, d in HOJAS_POR_LIBRO.items())
TAREAS_POR_FASE = OrderedDict([('PIZC', [12, 15, 14, 13, 13, 13])])          # 80 (D146, inv. §4)
MOLDE_CHECK = OrderedDict([('PIZC', 'hojas')])
COL_OK = OrderedDict([('PIZC', 1)])
FASES_CABECERA = OrderedDict()

# ==========================================================================
# 2. Fórmulas (D141, D143): E2 solo G14 (G13 es VALOR en el ES → VALORES_EN 0), E4 (FTE = Σ personas × FTE) y E5
#    (el literal 0.21 de la línea de bebida → B40, mecanismo E3 de la Bakery EN)
# ==========================================================================
_E2_ALC = ("('0. Supuestos'!$B$62*'0. Supuestos'!$B$40+(1-'0. Supuestos'!$B$62)*'0. Supuestos'!$B$39)")
PARCHES_FORMULA = OrderedDict([
    (('PIZP', 'PyG 3 Años', 'G14'), (_E2_ALC, "'0. Supuestos'!$B$41")),
    (('PIZP', 'Personal', 'C12'), ('SUM(C5:C11)', 'SUMPRODUCT(B5:B11,C5:C11)')),
    (('PIZP', 'PyG 3 Años', 'G11'), ('H11*0.21', "H11*'0. Supuestos'!$B$40")),
])

# ==========================================================================
# 3. Instrucciones: versión D20 y aviso D21 (E1: PIZP A53, PIZC A12); zona D19 (sin D18) por cabecera (filas 35-47)
# ==========================================================================
FILA_VERSION = OrderedDict([('PIZP', 52), ('PIZC', 11)])
ZONAS_CELDA = OrderedDict([
    (('PIZP', 'Instrucciones'), [(None, None, 'ABCD', 'D19')]),
])

# ==========================================================================
# 4. Docx (D147): las 131 ranuras del FT ES (= PAEL), H1 en 37·44·51·59·67·76·83·91·100·109; último de §9 = 108
#    (nota UK); tandas piz_a (§1-5) y piz_b (§6-10). El Word ES aún no existe: docx_es_piz.json es un marcador
#    «pendiente» hasta el paso 1c (`bp8.py extraer_docx`)
# ==========================================================================
DOCX_N_PARRAFOS = OrderedDict([('piz', 131)])
DOCX_ENCABEZADOS = OrderedDict([('piz', [37, 44, 51, 59, 67, 76, 83, 91, 100, 109])])
DOCX_INDICE = OrderedDict([('piz', list(range(24, 34)))])
DOCX_ULTIMO_9 = OrderedDict([('piz', '108')])
DOCX_TANDAS = OrderedDict([('piz_a', ('piz', [1, 2, 3, 4, 5])), ('piz_b', ('piz', [6, 7, 8, 9, 10]))])
PRESTAMO_SEMILLA = OrderedDict([('piz', 200000)])                   # punto fijo del dry-run (research §8: ≈ $192,400)

AUTOTEST = OrderedDict([
    ('P1', 'PIZP'), ('P2', 'PIZP'), ('C1', 'PIZC'), ('C2', 'PIZC'),
    ('C1_hoja_papel', 'F2 - Local, humos y licencia'), ('C1_titulo', 'Pizza Shop Startup Checklist (80 Tasks)'),
    ('C2_hoja_no_latino', 'F5 - Carta, marca y delivery'), ('P1_celda_texto', 'A3'), ('P1_celda_formula', 'B9'),
    ('P1_merge', 'A30:C30'),
])

# ==========================================================================
# 5. Grupos (D138)
# ==========================================================================
GRUPOS = ('GM', 'GR', 'GPIZ-plan', 'GPIZ-check')
GRUPOS_TRADUCTORES = ('GPIZ-plan', 'GPIZ-check')
GRUPOS_OVERRIDES = ('GPIZ-plan', 'GPIZ-check')
REVISAR_EN_TANDA = OrderedDict([('GPIZ-plan', ('GR',))])
GRUPOS_DESC = OrderedDict([
    ('GM', 'REUTILIZADAS: mismo ES que el Bar EN en la MISMA celda (o cadena común del motor, GM del Bar) y EN sin '
           'vocabulario ni caso del bar. preparar_tandas escribe su EN. No van a los traductores'),
    ('GR', 'REUTILIZADAS con revisión: EN del Bar de OTRA celda, de BP/BP2, o casado solo tras normalizar «comensal» → '
           '«cubierto». preparar_tandas escribe su EN; la tanda GPIZ-plan las revisa en textos_en/GR.revision.json'),
    ('GPIZ-plan', 'Nuevas del plan financiero (PIZP) + las del Bar con vocabulario o caso de bar (con propuesta) + las '
                  '13 filas D19 de Instrucciones (una cadena por celda, sin propuesta: D142)'),
    ('GPIZ-check', 'Nuevas del checklist (PIZC): las 80 tareas y sus cabeceras (con propuesta cuando el Bar tiene el '
                   'mismo ES)'),
    ('GX', 'NO se traduce: pestañas (mapas.HOJAS_POR_LIBRO), CLAVES, FIJOS, POR_CELDA, versión, pie y docProps'),
])

# Vocabulario y caso del BAR EN (y lo vetado del ES) que NO vale para la pizzería: clasifica las PROPUESTAS (no es el
# gate: ese es datos_piz.RX_PIZ_NO). Una propuesta sucia va a los traductores con su EN como forma
_CASO_BAR = (r'923,400|1,061,910|1,168,101|488,932|361,700|127,232|369,000|171,583|75,358|60,053|\b95 covers\b|'
             r'\$27(?:\.00)?\b|\$29\.16\b|\b360 days\b|\b60 seats\b|\b14 at the bar\b|\b65 ?%')
RX_REESCRIBIR = re.compile(
    r'(?i)\btapas\b|small plates|\bcocktails?\b|\bspirits\b|neighborhood bar|\bbarbacks?\b|\bbartend|last call|'
    r'happy hour|draft beer|draft system|draft lines|pour cost|\bliquor license|full liquor|vermouth|mixed beverage|'
    r'\bnightclub|\bDJ\b|three-tier|\bbar stools?\b|high-tops?|underbar|back-bar coolers|' + _CASO_BAR)

# sha256 del diccionario del Bar EN (cerrado y publicado; fijados el 25-oct-2026 sobre 8beee70e). Si cambian, hay que
# re-extraer y rehacer preparar_tandas antes de los traductores (bp8.py verificar avisa)
SHA_BAR = OrderedDict([
    ('textos_es.json', '7ff7c653499cf1c2599bdcd756d9635b4c91072d9cdec8e42c79eb15ed1d602b'),
    ('textos_en/GM.json', '0e55128a45b2383ffe4857a168e4a5c42b9dabfb8f18a7838e20eef10893a097'),
    ('textos_en/GR.json', '3de14dffc6cd9c752c68864655b4dd9714758f49d39cef6fcd9bdf356d6eb3a3'),
    ('textos_en/GR.revision.json', '05f108dafaf1715c6055e1cc3f8981c3521085bdd9641771797e3d20480eb611'),
    ('textos_en/GBAR-plan.json', 'dfd6769997098ed659f72820e7a4d3ba1703b87f6cefa9a32854a45499fef523'),
    ('textos_en/GBAR-check.json', '1cd062007913b8801c3130d6e2689e1a8647685407beedfd5ef63e0d3a25828e'),
    ('formulas_bar.json', '91d1ad137be39960453cf4feb861cd31ab4d0aaa2c19787f70a0e21b66c390d8'),
    ('censo_es.json', '16ebea870d07e443cc23c4563f3229b6cce0858bce4029ae0ab9298e6ba553ab'),
    ('datos_bar.py', 'bdff86b942fa78cf71209a7460a0e1e6aa066fbcd3618b94a160ba056a907bac'),
])


def _sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def diccionario_ok():
    """[] si los ficheros del diccionario del Bar EN siguen con el sha256 fijado; si no, los que cambiaron."""
    out = []
    for rel, sha in SHA_BAR.items():
        p = os.path.join(BAR, rel)
        if not os.path.exists(p):
            out.append('business-plans-en-3/%s: falta' % rel)
        elif _sha(p) != sha:
            out.append('business-plans-en-3/%s: sha256 distinto del fijado en mapas_piz.SHA_BAR' % rel)
    return out


# ==========================================================================
# 6. Diccionario: Bar EN por celda → Bar EN por texto → BP/BP2 por texto (con «comensal» → «cubierto»)
# ==========================================================================
_NORM = [(r'COMENSALES', 'CUBIERTOS'), (r'Comensales', 'Cubiertos'), (r'comensales', 'cubiertos'),
         (r'COMENSAL', 'CUBIERTO'), (r'Comensal', 'Cubierto'), (r'comensal', 'cubierto')]


def normalizar(t):
    for a, b in _NORM:
        t = t.replace(a, b)
    return t


def _datos_bar():
    """datos_bar.py del Bar cargado con otro nombre (sin chocar con el import de mapas_bar)."""
    spec = importlib.util.spec_from_file_location('datos_bar_ref_piz', os.path.join(BAR, 'datos_bar.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _cargar_bar():
    celda, texto = OrderedDict(), OrderedDict()
    te_p = os.path.join(BAR, 'textos_es.json')
    if not os.path.exists(te_p):
        return celda, texto
    en = OrderedDict()
    for g in ('GM', 'GR', 'GBAR-plan', 'GBAR-check'):
        p = os.path.join(BAR, 'textos_en', g + '.json')
        if os.path.exists(p):
            en.update(json.load(open(p, encoding='utf-8')))
    rev = os.path.join(BAR, 'textos_en', 'GR.revision.json')
    if os.path.exists(rev):
        en.update(json.load(open(rev, encoding='utf-8')))                 # ya va dentro de GR.json; idempotente
    por_celda = _datos_bar().POR_CELDA
    for c in json.load(open(te_p, encoding='utf-8'))['cadenas']:
        for d in c['donde']:
            if d.get('t') != 'celda':
                continue
            k = (d['f'], d['h'], d['c'])
            if k in por_celda:                                             # override del Bar en esa celda
                celda[k] = OrderedDict([('es', c['es']), ('en', por_celda[k]), ('grupo', 'POR_CELDA'),
                                        ('id', c['id']), ('tratamiento_origen', 'traducir')])
            elif c['id'] in en and c['tratamiento'] in ('traducir', 'localizar'):
                celda[k] = OrderedDict([('es', c['es']), ('en', en[c['id']]), ('grupo', c['grupo']), ('id', c['id']),
                                        ('tratamiento_origen', c['tratamiento'])])
        if c['id'] in en and c['tratamiento'] == 'traducir':
            texto.setdefault(c['es'], OrderedDict([('es', c['es']), ('en', en[c['id']]), ('grupo', c['grupo']),
                                                   ('id', c['id']), ('tratamiento_origen', 'traducir'),
                                                   ('donde', ['%s %s!%s' % (d['f'], d.get('h', ''), d.get('c', ''))
                                                              for d in c['donde'][:2]])]))
    return celda, texto


# BP/BP2: la cadena del Bar (`mapas_bar._FUENTES_REUSO`, prioridad GM → REST → CAF → PAN → FT), solo «traducir»
_FUENTES_BP = [(BP, ('GM',)), (BP2, ('GREST', 'GN')), (BP, ('GCAF',)), (BP2, ('GPAN',)), (BP, ('GFT',))]


def _cargar_bp():
    out = OrderedDict()
    cache = {}
    for carpeta, grupos in _FUENTES_BP:
        te_p = os.path.join(carpeta, 'textos_es.json')
        if not os.path.exists(te_p):
            continue
        if te_p not in cache:
            cache[te_p] = json.load(open(te_p, encoding='utf-8'))
        for g in grupos:
            p = os.path.join(carpeta, 'textos_en', g + '.json')
            if not os.path.exists(p):
                continue
            en = json.load(open(p, encoding='utf-8'))
            for go in (('GREST',) if carpeta == BP2 else ()):
                po = os.path.join(carpeta, 'textos_en', 'overrides_%s.json' % go)
                if os.path.exists(po):
                    for ident, o in json.load(open(po, encoding='utf-8')).items():
                        if ident in en:
                            en[ident] = o['texto']
            for c in cache[te_p]['cadenas']:
                if c['grupo'] != g or c['id'] not in en or c['tratamiento'] != 'traducir' or c['es'] in out:
                    continue
                out[c['es']] = OrderedDict([
                    ('es', c['es']), ('en', en[c['id']]), ('grupo', g), ('id', c['id']),
                    ('tratamiento_origen', 'traducir'), ('conjunto', os.path.basename(carpeta)),
                    ('donde', ['%s %s!%s' % (d['f'], d.get('h', ''), d.get('c', '')) for d in c['donde'][:2]])])
    return out


BAR_CELDA, BAR_TEXTO = _cargar_bar()
BP_TEXTO = _cargar_bp()


def propuesta_de(e):
    """(EN de reuso, origen) de una cadena de la pizzería, o (None, None). origen: 'celda' (mismo ES en la misma celda
    del Bar), 'celda-norm' (ídem tras normalizar), 'texto-bar-GM' / 'texto-bar' / 'texto-bar-norm' (mismo ES en otra
    celda del Bar), 'texto-bp' / 'texto-bp-norm' (BP/BP2)."""
    es = e['es']
    n = normalizar(es)
    celdas = [o for o in e['donde'] if o.get('t') == 'celda']
    gem = [BAR_CELDA.get((A_BAR.get(o['f']), o['h'], o['c'])) for o in celdas]
    if celdas and all(x is not None and x['es'] in (es, n) for x in gem) and len({x['en'] for x in gem}) == 1:
        return gem[0], ('celda' if all(x['es'] == es for x in gem) else 'celda-norm')
    for t, suf in ((es, ''), (n, '-norm')):
        if t in BAR_TEXTO:
            x = BAR_TEXTO[t]
            return x, 'texto-bar' + ('-GM' if (x['grupo'] == 'GM' and not suf) else suf)
    for t, suf in ((es, ''), (n, '-norm')):
        if t in BP_TEXTO:
            return BP_TEXTO[t], 'texto-bp' + suf
    return None, None


def _limpia(en):
    return not RX_REESCRIBIR.search(en or '')


def grupo_de(planes, texto=None, tratamiento=None, donde=None):
    donde = donde or []
    libros = {o['f'] for o in donde}
    destino = 'GPIZ-check' if libros == {'PIZC'} else 'GPIZ-plan'
    if any(o.get('det') == 'D19' for o in donde):
        return 'GPIZ-plan'                                   # D142: las 13 filas cambian enteras
    if tratamiento != 'traducir':
        return destino
    prop, origen = propuesta_de({'es': texto, 'donde': donde})
    if not prop or not _limpia(prop['en']):
        return destino
    if origen in ('celda', 'texto-bar-GM') and prop['grupo'] in ('GM', 'GR', 'GBAR-plan', 'GBAR-check', 'POR_CELDA'):
        return 'GM'
    return 'GR'


def reuso_de(e):
    """EN del diccionario (GM / GR) o PROPUESTA para los traductores. D19: sin propuesta (D142)."""
    if any(o.get('det') == 'D19' for o in e['donde']) or e['tratamiento'] != 'traducir':
        return None
    prop, origen = propuesta_de(e)
    if not prop:
        return None
    donde = prop.get('donde') or ['%s %s!%s' % (A_BAR.get(o['f']), o.get('h', ''), o.get('c', ''))
                                  for o in e['donde'][:2]]
    return OrderedDict([('grupo', prop['grupo']), ('id', prop['id']), ('en', prop['en']),
                        ('tratamiento_origen', prop['tratamiento_origen']),
                        ('conjunto', prop.get('conjunto', 'business-plans-en-3 (Bar EN cerrado)')),
                        ('origen', origen), ('donde', donde)])


# ==========================================================================
# instalar
# ==========================================================================
def instalar(M):
    """Sustituye en el módulo `mapas` (M) los datos de FT/CAF por los de la pizzería."""
    from datos_piz import completar                                        # contenido (FIJOS, caso US, docx…)
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
    M.REUSO = OrderedDict()                     # el reuso es por CELDA del Bar y luego por texto (propuesta_de)
    M.FUENTES_CIFRAS = [os.path.join(BP, 'F1-research-us.md'), os.path.join(BP, 'SPEC.md'),
                        os.path.join(BP2, 'F1-research-us-delta.md'), os.path.join(BP2, 'SPEC-delta.md'),
                        os.path.join(BAR, 'F1-research-us-delta.md'), os.path.join(BAR, 'SPEC-delta.md'),
                        os.path.join(AQUI, 'F1-research-us-delta.md'), os.path.join(AQUI, 'SPEC-delta.md')]
    M.NOTAS_F2 = os.path.join(AQUI, 'F2-NOTAS.md')
    completar(M)
