#!/usr/bin/env python3
"""
mapas_ice.py — Ice Cream Shop Business Plan Kit (EN) · datos ES→EN del conjunto «ice» (estructura).

SPEC: `SPEC-delta.md` (D186-D208) sobre las heredadas (`../business-plans-en-8/SPEC-delta.md` D133-D155 = PIZZA, y las
demás). Sesión Claude Code, 27-oct-2026 (F2-EN, paso 1a). NO se ejecuta solo: lo importa
`../business-plans-en/mapas.py` cuando `BP_CONJUNTO=ice` y llama a `instalar(M)`. Clon de
`../business-plans-en-8/mapas_piz.py` (D192): el libro de la heladería es GEMELO de la panadería ES 2.2 (727/736
fórmulas), pero ninguna cadena nueva sale del EN de la Bakery por celda (inv. §0), así que el CÓDIGO es el de la pizza
(plan `_HOJAS_PLAN`, checklist C2 de 6 fases + Instrucciones, `COL_OK 1`, G4 de la DV, versión A52/A11, zona D19 por
cabecera, docx de 131 ranuras) y el DICCIONARIO va en cadena, sin normalizar (inv. §6):

  1. EN de la PIZZA EN en la MISMA celda (`../business-plans-en-8/textos_es.json` + `textos_en/{GM,GR,GPIZ-plan,
     GPIZ-check}.json` + `*.revision.json` + `datos_piz.POR_CELDA`); el checklist se casa por POSICIÓN de pestaña
     (las 6 fases se renombran, inv. §0);
  2. EN de la Pizza EN por TEXTO;
  3. BAKERY EN por texto (`../business-plans-en-2/`, GPAN/GN con sus `overrides_` de la misma celda);
  4. BAR EN por texto (`../business-plans-en-3/`);
  5. BP/BP2 por texto (GM → REST → CAF → FT).

FUENTE ES: `FUENTE_ES` = `$ICE_FUENTE_ES` o, sin la variable, `astro-site/public/dl/plan-negocio-heladeria` (el ES
FINAL y LIVE: aquí no hay paso 1c, el ES ya está cerrado). Grupos:
  GM          motor común: mismo ES que una cadena GM (Pizza EN, Bar EN o BP) con un EN limpio (RX_REESCRIBIR).
  GR · GRC    EN de GPIZ-plan / GPIZ-check / GR de la pizza, de la Bakery, del Bar o de REST/CAF/FT: preparar_tandas lo
              escribe; GR (plan) lo revisa la tanda GICE-plan (textos_en/GR.revision.json) y GRC (solo del checklist:
              plazos, responsables, cabeceras y tareas de la Pizza EN) la tanda GICE-check (textos_en/GRC.revision.json).
              Desdoble frente a la pizza: aquí 73 de las 87 reutilizadas con revisión son del checklist (F2-NOTAS §1).
  GICE-plan   nuevas del plan (y las de reuso con vocabulario o caso de otro negocio, con propuesta) + las 13 filas
              D19 (una cadena por celda, sin propuesta: D196).
  GICE-check  nuevas del checklist (80 tareas, casi todo texto nuevo) + los mensajes de la DV con «—» (D199: ☐).

    python3 bp10.py mapas           # autotest + cruce con censo_es.json + verificar (incluye los sha256 de la pizza)
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
# 0. Producto (D186-D188)
# ==========================================================================
FUENTE_ES = os.environ.get('ICE_FUENTE_ES') or 'astro-site/public/dl/plan-negocio-heladeria'
PLANES = OrderedDict([
    ('ice', OrderedDict([
        ('slug', 'ice-cream-shop-business-plan'),
        ('producto', 'Ice Cream Shop Business Plan Kit'),
        ('slug_es', 'plan-negocio-heladeria'),
        ('dir_es', FUENTE_ES),
        ('env_stripe', 'VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_BUSINESS_PLAN'),
        ('keywords', 'ice cream shop business plan, ice cream parlor business plan, how to open an ice cream shop, '
                     'ice cream shop startup costs, batch freezer, AI Chef Pro'),
    ])),
])
for _p in PLANES.values():
    _p['url'] = 'aichef.pro/en/digital-products/' + _p['slug']
    _p['dir_en'] = 'astro-site/public/dl/' + _p['slug']

LIBROS = OrderedDict([
    ('HELP', ('ice', 'plan-financiero-heladeria.xlsx', 'ice-cream-shop-financial-projections.xlsx',
              'Ice Cream Shop Financial Projections: 3-Year P&L, Cash Flow & Financing')),
    ('HELC', ('ice', 'checklist-apertura-heladeria.xlsx', 'ice-cream-shop-startup-checklist.xlsx',
              'Ice Cream Shop Startup Checklist (80 Tasks)')),
])
DOCX = OrderedDict([
    ('ice', ('plan-de-negocio-heladeria.docx', 'ice-cream-shop-business-plan.docx',
             'Ice Cream Shop Business Plan (10 Sections)')),
])
TIPO_DE = {'HELP': 'plan', 'HELC': 'check'}
A_PIZ = {'HELP': 'PIZP', 'HELC': 'PIZC'}                  # libro de la Pizza EN (diccionario por celda)

# ==========================================================================
# 1. Pestañas: plan = las de la pizza (9, mismos nombres ES); checklist D199 (todas ≤ 31 caracteres)
# ==========================================================================
_HOJAS_PLAN = OrderedDict([
    ('0. Supuestos', '0. Assumptions'), ('Inversión Inicial', 'Startup Costs'), ('PyG 3 Años', '3-Year P&L'),
    ('Punto Equilibrio', 'Break-Even'), ('Escenarios', 'Scenarios'), ('Personal', 'Staffing'),
    ('Instrucciones', 'Instructions'), ('Tesorería 12 meses', '12-Month Cash Flow'), ('Financiación', 'Financing'),
])
_HOJAS_CHECK = OrderedDict([
    ('F1 - Constitución', 'Phase 1 - Business Setup'), ('F2 - Local y licencia', 'Phase 2 - Site & Permits'),
    ('F3 - Obrador y sanidad', 'Phase 3 - Production & Health'),
    ('F4 - Personal y APPCC', 'Phase 4 - Staff & Food Safety'),
    ('F5 - Marca y carta', 'Phase 5 - Brand & Menu'),
    ('F6 - Apertura y temporada', 'Phase 6 - Opening & Season'), ('Instrucciones', 'Instructions'),
])
assert all(len(v) <= 31 for v in _HOJAS_CHECK.values())
HOJAS_POR_LIBRO = OrderedDict([('HELP', _HOJAS_PLAN), ('HELC', _HOJAS_CHECK)])
HOJAS_ES_POR_LIBRO = OrderedDict((c, list(d)) for c, d in HOJAS_POR_LIBRO.items())
TAREAS_POR_FASE = OrderedDict([('HELC', [12, 15, 15, 12, 13, 13])])          # 80 (D199, inv. §4)
MOLDE_CHECK = OrderedDict([('HELC', 'hojas')])
COL_OK = OrderedDict([('HELC', 1)])
FASES_CABECERA = OrderedDict()

# Pestañas ES de la pizza en el MISMO orden (el checklist de la heladería renombra las 6 fases: se casa por posición)
_HOJAS_PIZ = {
    'HELP': list(_HOJAS_PLAN),
    'HELC': ['F1 - Constitución', 'F2 - Local, humos y licencia', 'F3 - Cocina, horno y sanidad',
             'F4 - Personal y prevención', 'F5 - Carta, marca y delivery', 'F6 - Apertura y 90 días', 'Instrucciones'],
}
HOJA_PIZ = {c: dict(zip(HOJAS_ES_POR_LIBRO[c], _HOJAS_PIZ[c])) for c in HOJAS_ES_POR_LIBRO}

# ==========================================================================
# 2. Fórmulas (D197): SOLO E2 en G14. G13 es VALOR en el ES (→ VALORES_EN 0), G11 con B62 = 0 da B39 (neutra) y la
#    columna H está vacía: sin E3 ni E5. Una persona por fila en Staffing (C11 = SUM(C5:C10)): sin E4 (inv. §2.6:
#    el E4 de la pizza apunta a C12, que aquí es la cabecera «CRECIMIENTO DE LA PLANTILLA»)
# ==========================================================================
_E2_ALC = ("('0. Supuestos'!$B$62*'0. Supuestos'!$B$40+(1-'0. Supuestos'!$B$62)*'0. Supuestos'!$B$39)")
PARCHES_FORMULA = OrderedDict([
    (('HELP', 'PyG 3 Años', 'G14'), (_E2_ALC, "'0. Supuestos'!$B$41")),
])

# ==========================================================================
# 3. Instrucciones: versión D20 y aviso D21 (E1: HELP A53, HELC A12); zona D19 (sin D18) por cabecera (filas 35-47)
# ==========================================================================
FILA_VERSION = OrderedDict([('HELP', 52), ('HELC', 11)])
ZONAS_CELDA = OrderedDict([
    (('HELP', 'Instrucciones'), [(None, None, 'ABCD', 'D19')]),
])

# ==========================================================================
# 4. Docx (D200): las 131 ranuras del FT ES (= PIZ), H1 en 37·44·51·59·67·76·83·91·100·109; último de §9 = 108
#    (nota UK); tandas ice_a (§1-5) e ice_b (§6-10). El Word ES ya es FINAL (bp10.py extraer_docx)
# ==========================================================================
DOCX_N_PARRAFOS = OrderedDict([('ice', 131)])
DOCX_ENCABEZADOS = OrderedDict([('ice', [37, 44, 51, 59, 67, 76, 83, 91, 100, 109])])
DOCX_INDICE = OrderedDict([('ice', list(range(24, 34)))])
DOCX_ULTIMO_9 = OrderedDict([('ice', '108')])
DOCX_TANDAS = OrderedDict([('ice_a', ('ice', [1, 2, 3, 4, 5])), ('ice_b', ('ice', [6, 7, 8, 9, 10]))])
PRESTAMO_SEMILLA = OrderedDict([('ice', 162000)])                   # research §8: ≈ $162,000 (punto fijo en F2)

AUTOTEST = OrderedDict([
    ('P1', 'HELP'), ('P2', 'HELP'), ('C1', 'HELC'), ('C2', 'HELC'),
    ('C1_hoja_papel', 'F2 - Local y licencia'), ('C1_titulo', 'Ice Cream Shop Startup Checklist (80 Tasks)'),
    ('C2_hoja_no_latino', 'F5 - Marca y carta'), ('P1_celda_texto', 'A3'), ('P1_celda_formula', 'B9'),
    ('P1_merge', 'A30:C30'),
])

# ==========================================================================
# 5. Grupos (D192)
# ==========================================================================
GRUPOS = ('GM', 'GR', 'GRC', 'GICE-plan', 'GICE-check')
GRUPOS_TRADUCTORES = ('GICE-plan', 'GICE-check')
GRUPOS_OVERRIDES = ('GICE-plan', 'GICE-check')
REVISAR_EN_TANDA = OrderedDict([('GICE-plan', ('GR',)), ('GICE-check', ('GRC',))])
GRUPOS_DESC = OrderedDict([
    ('GM', 'REUTILIZADAS: motor común (mismo ES que una cadena GM de la Pizza EN, del Bar EN o de BP) con un EN sin '
           'vocabulario ni caso de otro negocio. preparar_tandas escribe su EN. No van a los traductores'),
    ('GR', 'REUTILIZADAS con revisión (plan): EN de GPIZ-plan / GPIZ-check / GR de la Pizza EN, de la Bakery EN, del Bar '
           'EN o de REST/CAF/FT. preparar_tandas escribe su EN; la tanda GICE-plan las revisa en textos_en/GR.revision.json'),
    ('GRC', 'REUTILIZADAS con revisión (solo del checklist): EN de la Pizza EN (plazos, responsables, cabeceras, tareas). '
            'preparar_tandas escribe su EN; la tanda GICE-check las revisa en textos_en/GRC.revision.json'),
    ('GICE-plan', 'Nuevas del plan financiero (HELP) + las de reuso con vocabulario o caso de otro negocio (con '
                  'propuesta) + las 13 filas D19 de Instrucciones (una cadena por celda, sin propuesta: D196)'),
    ('GICE-check', 'Nuevas del checklist (HELC): las 80 tareas, sus cabeceras y los mensajes de la DV (con propuesta '
                   'cuando la Pizza EN tiene el mismo ES)'),
    ('GX', 'NO se traduce: pestañas (mapas.HOJAS_POR_LIBRO), CLAVES, FIJOS, POR_CELDA, versión, pie y docProps'),
])

# Vocabulario y caso de la PIZZA, la PANADERÍA y el BAR que NO vale para la heladería: clasifica las PROPUESTAS (no es
# el gate: ese es datos_ice.RX_ICE_NO). Una propuesta sucia va a los traductores con su EN como forma
_CASO_PIZ = (r'669,600|709,776|738,167|242,550|329,274|86,724|217,300|39,275|\$36(?:\.00)?\b|\$38\.88|'
             r'\b62 covers\b|\b50 seats\b|\b1,500 sq ft\b')
RX_REESCRIBIR = re.compile(
    r'(?i)\bpizz|(?<!cookie )\bdough\b|\bovens?\b|Neapolitan|\bVPN\b|firewood|wood-fired|beer (?:&|and) wine|'
    r'\bcovers?(?:/day| per day| a day| needed)|\d+ covers\b|equivalent covers|seat turns|\bflue\b|spark arrestor|'
    r'\bhood\b|mozzarella|San Marzano|Margherita|\btapas\b|small plates|\bcocktails?\b|\bspirits\b|\bbartend|'
    r'happy hour|liquor|\bbread\b|\bbakery\b|\bbakers?\b|\bloa(?:f|ves)\b|pastr(?:y|ies)|croissant|'
    r'transactions?(?:/day| per day| a day)|' + _CASO_PIZ)

# sha256 del diccionario de la Pizza EN (cerrada y publicada; fijados el 27-oct-2026 sobre db6c741b). Si cambian, hay
# que re-extraer y rehacer preparar_tandas antes de los traductores (bp10.py verificar avisa)
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
# sha256 del ES FINAL medido en F1 (inv. cabecera): si el ES cambia, manda el ES nuevo (re-medir y avisar)
SHA_ES = OrderedDict([
    ('plan-financiero-heladeria.xlsx', 'a99b1686751b25ced5d71b6f66585ba199355ee75c8f07bb3ffb76031d378ba7'),
    ('checklist-apertura-heladeria.xlsx', 'd8ec6c6fa3910f8234d7aa4074897ad7ebdf0e8e371d296c8b08d511475113bc'),
    ('plan-de-negocio-heladeria.docx', '04739dfec3f0dbef3b1bf9b221adbd2fecf9c6f3fadcfdfde0bc8881b02ee74b'),
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
            out.append('business-plans-en-8/%s: sha256 distinto del fijado en mapas_ice.SHA_PIZ' % rel)
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
    por_celda = _modulo('datos_piz_ref_ice', os.path.join(PIZ, 'datos_piz.py')).POR_CELDA
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
    """(entrada de reuso, origen) de una cadena de la heladería, o (None, None). origen: 'celda-piz' (mismo ES en la
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
    destino = 'GICE-check' if libros == {'HELC'} else 'GICE-plan'
    if any(o.get('det') == 'D19' for o in donde):
        return 'GICE-plan'                                   # D196: las 13 filas cambian enteras
    if texto and '—' in texto and any(o.get('t') in _DV_MSG for o in donde):
        return 'GICE-check'                                  # D199: la DV EN es ✓,☐,N/A; su texto dice ☐, no «—»
    if tratamiento != 'traducir':
        return destino
    prop, origen = propuesta_de({'es': texto, 'donde': donde})
    if not prop or not _limpia(prop['en']):
        return destino
    if (prop.get('conjunto'), prop['grupo']) in _GM_ORIGEN:
        return 'GM'
    return 'GRC' if libros == {'HELC'} else 'GR'


def reuso_de(e):
    """EN del diccionario (GM / GR) o PROPUESTA para los traductores. D19: sin propuesta (D196)."""
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
    """Sustituye en el módulo `mapas` (M) los datos de FT/CAF por los de la heladería."""
    from datos_ice import completar                                        # contenido (FIJOS, caso US, docx…)
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
                        os.path.join(AQUI, 'F1-research-us-delta.md'), os.path.join(AQUI, 'SPEC-delta.md')]
    M.NOTAS_F2 = os.path.join(AQUI, 'F2-NOTAS.md')
    # D199 · G4 (heredado de la pizza, F2-NOTAS PIZ §5.1 y §7): el checklist ES LIVE trae la DV "✓,—,N/A" con las 80
    # celdas OK en «☐» (inv. §4 y §8). En el EN la lista pasa a "✓,☐,N/A". «—» no tiene letras y `necesita_clave` lo
    # dejaba fuera de CLAVES: solo en este conjunto se le da clave. «—» no es literal de ninguna fórmula ni CF del ES.
    M.CLAVES['—'] = '☐'
    _nc = M.necesita_clave
    M.necesita_clave = lambda lit, _nc=_nc: lit == '—' or _nc(lit)
    completar(M)
