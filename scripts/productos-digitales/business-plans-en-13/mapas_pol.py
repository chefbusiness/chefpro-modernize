#!/usr/bin/env python3
"""
mapas_pol.py — Rotisserie Chicken Restaurant Business Plan Kit (EN) · datos ES→EN del conjunto «pol» (estructura).

Fuente de verdad: `../plan-polleria/F1-camino.md` §6-§7 (EN delta) y `F1-research-us-delta.md` (US §n). Sesión Claude
Code, 29-oct-2026 (F2-EN). NO se ejecuta solo: lo importa `../business-plans-en/mapas.py` cuando `BP_CONJUNTO=pol` y
llama a `instalar(M)`. Clon de `../business-plans-en-12/mapas_taq.py` (Taco EN, LIVE hoy): el libro ES de la pollería sale
de la TAQUERÍA LIVE (`semilla_pol.py`) con `ROTACION` apagada: `0. Supuestos!A50:C50` vacías y `Punto Equilibrio` sin las
filas 25-26 de la rotación (las de abajo suben 2). Van los parches E2 (G14), E4 (Staffing!C12) y E5 (G11), G13 → 0 y el
DICCIONARIO en cadena, sin normalizar (el «por celda» exige el MISMO ES en la misma celda: en `Break-Even` ≥ 25 cae solo a
«por texto»):

  0. EN del TACO EN en la MISMA celda (`../business-plans-en-12/textos_es.json` + `textos_en/{GM,GR,GRC,GTAQ-plan,
     GTAQ-check}.json` + `*.revision.json` + `datos_taq.POR_CELDA`); checklist casado por POSICIÓN de pestaña;
  1. EN del Taco EN por TEXTO (y con «pedido» ↔ «comensal»: la pollería ES cuenta pedidos, el caso US covers);
  2. EN de la PIZZA EN por celda y por texto; 3. BAKERY EN; 4. BAR EN; 5. BP/BP2 (GM → REST → CAF → FT).

FUENTE ES: `FUENTE_ES` = `$POL_FUENTE_ES` o, sin la variable, `astro-site/public/dl/plan-negocio-polleria` (el ES FINAL
y revisado de la F2 ES, `8c34fa09`: no hay paso 1c). Grupos:
  GM          motor común: mismo ES que una cadena GM (Taco EN, Pizza EN, Bar EN o BP) con un EN limpio (RX_REESCRIBIR).
  GR · GRC    EN de GTAQ-* / GR / GRC del Taco EN, de la Pizza EN, de la Bakery, del Bar o de REST/CAF/FT (y TODO lo
              casado por «pedido» ↔ «comensal»): preparar_tandas lo escribe; GR (plan) lo revisa la tanda GPOL-plan
              (textos_en/GR.revision.json) y GRC (solo del checklist) la tanda GPOL-check (textos_en/GRC.revision.json).
  GPOL-plan   nuevas del plan (y las de reuso con vocabulario o caso de otro negocio, con propuesta) + las 12 filas
              D19 (una cadena por celda, sin propuesta).
  GPOL-check  nuevas del checklist (80 tareas) + los mensajes de la DV con «—» (la DV EN es ✓,☐,N/A).

    python3 bp13.py mapas           # autotest + cruce con censo_es.json + verificar (incluye los sha256)
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

# ==========================================================================
# 0. Producto (F1-camino §6)
# ==========================================================================
FUENTE_ES = os.environ.get('POL_FUENTE_ES') or 'astro-site/public/dl/plan-negocio-polleria'
PLANES = OrderedDict([
    ('pol', OrderedDict([
        ('slug', 'rotisserie-chicken-restaurant-business-plan'),
        ('producto', 'Rotisserie Chicken Restaurant Business Plan Kit'),
        ('slug_es', 'plan-negocio-polleria'),
        ('dir_es', FUENTE_ES),
        ('env_stripe', 'VITE_STRIPE_PAYMENT_LINK_ROTISSERIE_CHICKEN_RESTAURANT_BUSINESS_PLAN'),
        ('keywords', 'rotisserie chicken restaurant business plan, chicken restaurant business plan, how to open a '
                     'rotisserie chicken restaurant, Peruvian chicken restaurant, pollo a la brasa, AI Chef Pro'),
    ])),
])
for _p in PLANES.values():
    _p['url'] = 'aichef.pro/en/digital-products/' + _p['slug']
    _p['dir_en'] = 'astro-site/public/dl/' + _p['slug']

LIBROS = OrderedDict([
    ('POLP', ('pol', 'plan-financiero-polleria.xlsx', 'rotisserie-chicken-restaurant-financial-projections.xlsx',
              'Rotisserie Chicken Restaurant Financial Projections: 3-Year P&L, Cash Flow & Financing')),
    ('POLC', ('pol', 'checklist-apertura-polleria.xlsx', 'rotisserie-chicken-restaurant-startup-checklist.xlsx',
              'Rotisserie Chicken Restaurant Startup Checklist (80 Tasks)')),
])
DOCX = OrderedDict([
    ('pol', ('plan-de-negocio-polleria.docx', 'rotisserie-chicken-restaurant-business-plan.docx',
             'Rotisserie Chicken Restaurant Business Plan (10 Sections)')),
])
TIPO_DE = {'POLP': 'plan', 'POLC': 'check'}
A_TAQ = {'POLP': 'TAQP', 'POLC': 'TAQC'}                  # libro del Taco EN (diccionario por celda, nivel 0)
A_PIZ = {'POLP': 'PIZP', 'POLC': 'PIZC'}                  # libro de la Pizza EN (diccionario por celda, nivel 2)

# ==========================================================================
# 1. Pestañas: plan = las de la taquería (9, mismos nombres ES); checklist (todas ≤ 31 caracteres; F2 y F3 = F1-camino §6)
# ==========================================================================
_HOJAS_PLAN = OrderedDict([
    ('0. Supuestos', '0. Assumptions'), ('Inversión Inicial', 'Startup Costs'), ('PyG 3 Años', '3-Year P&L'),
    ('Punto Equilibrio', 'Break-Even'), ('Escenarios', 'Scenarios'), ('Personal', 'Staffing'),
    ('Instrucciones', 'Instructions'), ('Tesorería 12 meses', '12-Month Cash Flow'), ('Financiación', 'Financing'),
])
_HOJAS_CHECK = OrderedDict([
    ('F1 - Constitución', 'Phase 1 - Business Setup'), ('F2 - Local, humos y gas', 'Phase 2 - Hood, Gas & Permits'),
    ('F3 - Cocina, asador y sanidad', 'Phase 3 - Rotisserie & Health'),
    ('F4 - Personal y alérgenos', 'Phase 4 - Staff & Allergens'),
    ('F5 - Carta, marca y encargos', 'Phase 5 - Menu & Pre-Orders'),
    ('F6 - Apertura y 90 días', 'Phase 6 - Opening & 90 Days'), ('Instrucciones', 'Instructions'),
])
assert all(len(v) <= 31 for v in _HOJAS_CHECK.values())
HOJAS_POR_LIBRO = OrderedDict([('POLP', _HOJAS_PLAN), ('POLC', _HOJAS_CHECK)])
HOJAS_ES_POR_LIBRO = OrderedDict((c, list(d)) for c, d in HOJAS_POR_LIBRO.items())
TAREAS_POR_FASE = OrderedDict([('POLC', [12, 15, 14, 13, 13, 13])])          # 80 (F1-camino §4, mismas filas)
MOLDE_CHECK = OrderedDict([('POLC', 'hojas')])
COL_OK = OrderedDict([('POLC', 1)])
FASES_CABECERA = OrderedDict()

# Pestañas ES de la taquería y de la pizza en el MISMO orden (el checklist se casa por posición)
_HOJAS_TAQ = {
    'POLP': list(_HOJAS_PLAN),
    'POLC': ['F1 - Constitución', 'F2 - Local, humos y gas', 'F3 - Cocina, trompo y sanidad', 'F4 - Personal y alérgenos',
             'F5 - Carta, marca y delivery', 'F6 - Apertura y 90 días', 'Instrucciones'],
}
HOJA_TAQ = {c: dict(zip(HOJAS_ES_POR_LIBRO[c], _HOJAS_TAQ[c])) for c in HOJAS_ES_POR_LIBRO}
_HOJAS_PIZ = {
    'POLP': list(_HOJAS_PLAN),
    'POLC': ['F1 - Constitución', 'F2 - Local, humos y licencia', 'F3 - Cocina, horno y sanidad',
             'F4 - Personal y prevención', 'F5 - Carta, marca y delivery', 'F6 - Apertura y 90 días', 'Instrucciones'],
}
HOJA_PIZ = {c: dict(zip(HOJAS_ES_POR_LIBRO[c], _HOJAS_PIZ[c])) for c in HOJAS_ES_POR_LIBRO}

# ==========================================================================
# 2. Fórmulas (= Taco EN y Pizza EN, F1-camino §6): E2 solo G14 (G13 es VALOR en el ES → VALORES_EN 0), E4 (Staffing!C12 =
#    Σ personas × FTE: 2 personas de counter en una fila) y E5 (el literal 0.21 de la línea de bebida → B40)
# ==========================================================================
_E2_ALC = ("('0. Supuestos'!$B$62*'0. Supuestos'!$B$40+(1-'0. Supuestos'!$B$62)*'0. Supuestos'!$B$39)")
PARCHES_FORMULA = OrderedDict([
    (('POLP', 'PyG 3 Años', 'G14'), (_E2_ALC, "'0. Supuestos'!$B$41")),
    (('POLP', 'Personal', 'C12'), ('SUM(C5:C11)', 'SUMPRODUCT(B5:B11,C5:C11)')),
    (('POLP', 'PyG 3 Años', 'G11'), ('H11*0.21', "H11*'0. Supuestos'!$B$40")),
])

# ==========================================================================
# 3. Instrucciones: versión D20 y aviso D21 (E1: POLP A52, POLC A12; la tabla D19 del ES tiene 12 filas, 35-46, = la
#    taquería); zona D19 (sin D18) por cabecera
# ==========================================================================
FILA_VERSION = OrderedDict([('POLP', 51), ('POLC', 11)])
ZONAS_CELDA = OrderedDict([
    (('POLP', 'Instrucciones'), [(None, None, 'ABCD', 'D19')]),
])

# ==========================================================================
# 4. Docx: las 131 ranuras del FT ES (= PIZ), H1 en 37·44·51·59·67·76·83·91·100·109; último de §9 = 108 (nota UK);
#    tandas pol_a (§1-5) y pol_b (§6-10), 61 ranuras desde el Word ES final (bp13.py extraer_docx)
# ==========================================================================
DOCX_N_PARRAFOS = OrderedDict([('pol', 131)])
DOCX_ENCABEZADOS = OrderedDict([('pol', [37, 44, 51, 59, 67, 76, 83, 91, 100, 109])])
DOCX_INDICE = OrderedDict([('pol', list(range(24, 34)))])
DOCX_ULTIMO_9 = OrderedDict([('pol', '108')])
DOCX_TANDAS = OrderedDict([('pol_a', ('pol', [1, 2, 3, 4, 5])), ('pol_b', ('pol', [6, 7, 8, 9, 10]))])
PRESTAMO_SEMILLA = OrderedDict([('pol', 208500)])                   # research US §8: ≈ $208,500 (punto fijo en F2)

AUTOTEST = OrderedDict([
    ('P1', 'POLP'), ('P2', 'POLP'), ('C1', 'POLC'), ('C2', 'POLC'),
    ('C1_hoja_papel', 'F2 - Local, humos y gas'), ('C1_titulo', 'Rotisserie Chicken Restaurant Startup Checklist (80 Tasks)'),
    ('C2_hoja_no_latino', 'F5 - Carta, marca y encargos'), ('P1_celda_texto', 'A3'), ('P1_celda_formula', 'B9'),
    ('P1_merge', 'A30:C30'),
])

# ==========================================================================
# 5. Grupos (= heladería: GR del plan y GRC del checklist)
# ==========================================================================
GRUPOS = ('GM', 'GR', 'GRC', 'GPOL-plan', 'GPOL-check')
GRUPOS_TRADUCTORES = ('GPOL-plan', 'GPOL-check')
GRUPOS_OVERRIDES = ('GPOL-plan', 'GPOL-check')
REVISAR_EN_TANDA = OrderedDict([('GPOL-plan', ('GR',)), ('GPOL-check', ('GRC',))])
GRUPOS_DESC = OrderedDict([
    ('GM', 'REUTILIZADAS: motor común (mismo ES que una cadena GM del Taco EN, de la Pizza EN, del Bar EN o de BP) con un '
           'EN sin vocabulario ni caso de otro negocio. preparar_tandas escribe su EN. No van a los traductores'),
    ('GR', 'REUTILIZADAS con revisión (plan): EN de GTAQ-* / GR / GRC del Taco EN, de GPIZ-* de la Pizza EN, de la Bakery '
           'EN, del Bar EN o de REST/CAF/FT (y lo casado con «pedido» ↔ «comensal»). preparar_tandas escribe su EN; la '
           'tanda GPOL-plan las revisa en textos_en/GR.revision.json'),
    ('GRC', 'REUTILIZADAS con revisión (solo del checklist): EN del Taco EN o de la Pizza EN (plazos, responsables, '
            'cabeceras, tareas). preparar_tandas escribe su EN; la tanda GPOL-check las revisa en '
            'textos_en/GRC.revision.json'),
    ('GPOL-plan', 'Nuevas del plan financiero (POLP) + las de reuso con vocabulario o caso de otro negocio (con '
                  'propuesta) + las 12 filas D19 de Instrucciones (una cadena por celda, sin propuesta)'),
    ('GPOL-check', 'Nuevas del checklist (POLC): las 80 tareas, sus cabeceras y los mensajes de la DV (con propuesta '
                   'cuando el Taco EN o la Pizza EN tienen el mismo ES)'),
    ('GX', 'NO se traduce: pestañas (mapas.HOJAS_POR_LIBRO), CLAVES, FIJOS, POR_CELDA, versión, pie y docProps'),
])

# Vocabulario y caso del TACO, la PIZZA, la PANADERÍA y el BAR que NO vale para la pollería: clasifica las PROPUESTAS
# (no es el gate: ese es datos_pol.RX_POL_NO). Una propuesta sucia va a los traductores con su EN como forma. «covers»,
# «hood», «beer & wine», «liquor liability», «counter service» y «pickup» SÍ valen en la pollería
_CASO_OTROS = (r'669,600|709,776|738,167|242,550|329,274|86,724|217,300|39,275|\$36(?:\.00)?\b|\$38\.88|'
               r'619,850|657,041|683,323|176,000|197,600|275,612|\b115 covers\b|\b308\b|\$2,800\b|\b1,200 sq ft\b|'
               r'\b62 covers\b|\b50 seats\b|\b30 seats\b|\b1,500 sq ft\b|closed (?:on )?Mondays|\bMondays?\b')
RX_REESCRIBIR = re.compile(
    r'(?i)\bpizz|\bdough\b|\bovens?\b|Neapolitan|\bVPN\b|firewood|wood-fired|\bflue\b|spark arrestor|\bpeels?\b|'
    r'hearth|mozzarella|San Marzano|Margherita|\b00 flour|\bservers?\b|\bwaitstaff|table service|\btapas\b|'
    r'small plates|\bcocktails?\b|\bspirits\b|\bbartend|happy hour|full liquor|\bbread\b|\bbakery\b|\bbakers?\b|'
    r'\bloa(?:f|ves)\b|pastr(?:y|ies)|croissant|transactions?(?:/day| per day| a day)|'
    r'\btacos?\b|taquer|trompo|al pastor|\bpastor\b|tortill|\bmasa\b|nixtamal|salsa bar|quesadilla|\bgringas?\b|'
    r'carnitas|birria|suadero|aguas? frescas?|horchata|jamaica|Cinco de Mayo|Mexican beer|\bcomal\b|griddle|'
    r'guac|pico de gallo|salsa macha|pork shoulder|vertical broiler|seat turns?|\bpatio\b|' + _CASO_OTROS)

# «pedido» (ES de la pollería) ↔ «comensal» (ES de la taquería): mismo rótulo con otra unidad. El caso US cuenta covers
# (US §8: 130 covers equivalentes; la family meal = 3.5 covers): el EN del Taco vale como PROPUESTA revisada (GR/GRC)
# Jerga peruana y nombres propios US con artículos del español (US §9): el detector de restos no los cuenta (instalar)
TERMINOS_PE = ('D[ií]a del Pollo a la Brasa', 'El Pollo Loco', 'pollo a la brasa', 'papa a la huancaina')

_ALIAS = (('Pedidos', 'Comensales'), ('pedidos', 'comensales'), ('Pedido', 'Comensal'), ('pedido', 'comensal'))


def _alias(es):
    out = es
    for a, b in _ALIAS:
        out = re.sub(r'\b%s\b' % a, b, out)
    return out if out != es else None


# sha256 del diccionario del Taco EN (cerrado y LIVE, bf18ff72; medidos el 29-oct sobre 8c34fa09) y de la Pizza EN
# (= mapas_taq.SHA_PIZ). Si cambian, hay que re-extraer y rehacer preparar_tandas (bp13.py verificar avisa)
SHA_TAQ = OrderedDict([
    ('textos_es.json', '6ea5f29803fe74e6013738f7896931c473b4bb143cca529dd3c850d49725874c'),
    ('textos_en/GM.json', '17bceb7b136363c3869b5e713fac64e6972bd87114bd45db58a993c08d23a877'),
    ('textos_en/GM.revision.json', 'bfc5dfa013ee8661d33e1181fcafdea1c291c8f2d23068dc1c1c967f72905d6e'),
    ('textos_en/GR.json', 'ead32eecbe8cd17532ce8e8a560d9ffc22aa91bd16a921e931792441fc0b5b27'),
    ('textos_en/GR.revision.json', 'b632ba77785bcebb14d96c666f4b91b8d3f2d12837ef1220cb30aec18f855682'),
    ('textos_en/GRC.json', 'e7ddfab10026b9c4f735338cab31f63c504f479661453f4bd79839052f81ebc1'),
    ('textos_en/GRC.revision.json', 'cda1d04f28213288b2ab41607b4415100005b3224c96f7aeb7416fa520f50f9b'),
    ('textos_en/GTAQ-plan.json', 'e2fdac65fca460a019411ea99c7c01c92bd4ec8af9cf8f3d8ed1c9eecab2a014'),
    ('textos_en/GTAQ-check.json', '33ab5e40c525f126e37f3ae67b51defa00631e3048ce51e945f61d313e4effd6'),
    ('formulas_taq.json', '32ebc9b30708271f45ec8c6534da31cef637b108f7e3228ecd52e4559fd05c10'),
    ('censo_es.json', '0626cb6d3731262445961ff212bbbbad6c6492558c21a6339f4e85dd036aff68'),
    ('datos_taq.py', '0f0342a6eaf357eb8b97aba07c74a9f80548034b86bb48a30a6d7bdf877185ab'),
])
SHA_PIZ = OrderedDict([
    ('textos_es.json', '7f504ed3ffc1ec12e95b36888dbf4e92711b7d1cc4319cb6128251deea817986'),
    ('textos_en/GM.json', '0f6cd4198a3c533331cca1111dde7a5de26c87b173e0d2712abafac72e6c08ed'),
    ('textos_en/GR.json', 'ef088edc5b1709acd9ad28ab3f5d7023a6421f505fc0d0dfedb63a7f099e8151'),
    ('textos_en/GM.revision.json', 'b6d5e7768ba1fa4240dd3c055355db4fc17559b3eec0249f57978cbf574d7876'),
    ('textos_en/GR.revision.json', 'fc7cfb4e679c7f30c5571381cc72b9d4bec3094283172fdb5c30e508147941d0'),
    ('textos_en/GPIZ-plan.json', 'a52044a121fd9e28c7931534c3ee54adabe856a186c543c5f13e6aa08a7dc3b6'),
    ('textos_en/GPIZ-check.json', 'c3d62514b899edb9d0aa9a1c32fcaa3517a22229fe4121bd72d2b978d43556da'),
    ('formulas_piz.json', '286b3675b30e2eed71982781e209f4aa063fe4c8be2e7c616ebbd54877caebb2'),
    ('censo_es.json', '442b610642a4a11ea781c1790d02a74bf5c41b4e9da5fa790b8ab2c3fe1bf53b'),
    ('datos_piz.py', '44c178d7bb9ae94eb696f26d8f964ba98f510e275e4104ce5baece71e1d2158e'),
])
# sha256 del ES FINAL (F2 ES revisada, 8c34fa09 = plan-polleria/REVISION-FINAL.md): si el ES cambia, manda el ES nuevo
# (re-extraer y avisar)
SHA_ES = OrderedDict([
    ('plan-financiero-polleria.xlsx', '5080ac3bb261dc8883cb8ed23045b9cb1d603098f637eb195f9f4f1557efdcaf'),
    ('checklist-apertura-polleria.xlsx', '0fdb65f57d7a2dc07aa297a49829c0a9210be671b36e2af89b8b1b591a11c724'),
    ('plan-de-negocio-polleria.docx', 'cd12837f309dbeea59b92f6de2dfe9e04286c650f244ff5a82822eb0b4447fa4'),
])


def _sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def diccionario_ok():
    """[] si los ficheros de los diccionarios del Taco EN y de la Pizza EN siguen con el sha256 fijado."""
    out = []
    for carpeta, nombre, shas in ((TAQ, 'business-plans-en-12', SHA_TAQ), (PIZ, 'business-plans-en-8', SHA_PIZ)):
        for rel, sha in shas.items():
            p = os.path.join(carpeta, rel)
            if not os.path.exists(p):
                out.append('%s/%s: falta' % (nombre, rel))
            elif _sha(p) != sha:
                out.append('%s/%s: sha256 distinto del fijado en mapas_pol' % (nombre, rel))
    return out


# ==========================================================================
# 6. Diccionario: Taco EN por celda → por texto (+ alias) → Pizza EN por celda → por texto → Bakery → Bar → BP/BP2
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
    por_celda = _modulo('%s_ref_pol' % datos, os.path.join(carpeta, datos + '.py')).POR_CELDA
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
TAQ_CELDA, TAQ_TEXTO = _cargar_celda(TAQ, ('GM', 'GR', 'GRC', 'GTAQ-plan', 'GTAQ-check'), 'datos_taq', _ET_TAQ)
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
_GM_ORIGEN = {(_ET_TAQ, 'GM'), (_ET_PIZ, 'GM'), ('business-plans-en-3 (Bar EN)', 'GM'), ('business-plans-en (GM)', 'GM')}


def _celdas(e):
    return [o for o in e['donde'] if o.get('t') == 'celda']


def _por_celda(dic, libros, hojas, celdas, es):
    gem = [dic.get((libros.get(o['f']), hojas.get(o['f'], {}).get(o['h']), o['c'])) for o in celdas]
    if celdas and all(x is not None and x['es'] == es for x in gem) and len({x['en'] for x in gem}) == 1:
        return OrderedDict(gem[0])
    return None


def propuesta_de(e):
    """(entrada de reuso, origen) de una cadena de la pollería, o (None, None). origen: 'celda-taq', 'texto-taq',
    'alias-taq' (mismo ES con «pedido» → «comensal»), 'celda-piz', 'texto-piz', 'texto-pan', 'texto-bar', 'texto-bp'."""
    es = e['es']
    celdas = _celdas(e)
    x = _por_celda(TAQ_CELDA, A_TAQ, HOJA_TAQ, celdas, es)
    if x:
        return x, 'celda-taq'
    if es in TAQ_TEXTO:
        return TAQ_TEXTO[es], 'texto-taq'
    al = _alias(es)
    if al and al in TAQ_TEXTO:
        return TAQ_TEXTO[al], 'alias-taq'
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


_DV_MSG = ('dv-error', 'dv-prompt', 'dv-error-titulo', 'dv-prompt-titulo')


def grupo_de(planes, texto=None, tratamiento=None, donde=None):
    donde = donde or []
    libros = {o['f'] for o in donde}
    destino = 'GPOL-check' if libros == {'POLC'} else 'GPOL-plan'
    if any(o.get('det') == 'D19' for o in donde):
        return 'GPOL-plan'                                   # las 12 filas D19 cambian enteras
    if texto and '—' in texto and any(o.get('t') in _DV_MSG for o in donde):
        return 'GPOL-check'                                  # la DV EN es ✓,☐,N/A; su texto dice ☐, no «—»
    if tratamiento != 'traducir':
        return destino
    prop, origen = propuesta_de({'es': texto, 'donde': donde})
    if not prop or not _limpia(prop['en']):
        return destino
    if origen != 'alias-taq' and (prop.get('conjunto'), prop['grupo']) in _GM_ORIGEN:
        return 'GM'
    return 'GRC' if libros == {'POLC'} else 'GR'


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
    """Sustituye en el módulo `mapas` (M) los datos de FT/CAF por los de la pollería."""
    from datos_pol import completar                                        # contenido (FIJOS, caso US, docx…)
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
                        os.path.join(TAQ, 'F1-research-us-delta.md'), os.path.join(AQUI, 'F1-research-us-delta.md')]
    M.NOTAS_F2 = os.path.join(AQUI, 'F2-NOTAS.md')
    # G4 (heredado de la pizza y el taco, F2-NOTAS PIZ §5.1 y §7): el checklist ES de la pollería (semilla = taquería)
    # trae la DV "✓,—,N/A" con las 80 celdas OK en «☐». En el EN la lista pasa a "✓,☐,N/A". «—» no tiene letras y `necesita_clave` lo
    # dejaba fuera de CLAVES: solo en este conjunto se le da clave. «—» no es literal de ninguna fórmula ni CF del ES.
    M.CLAVES['—'] = '☐'
    # Jerga peruana y nombres que el inglés US usa tal cual (US §9): «Día del Pollo a la Brasa», «El Pollo Loco»…
    # llevan artículos del español que el detector de restos (mapas.restos_espanol) marcaría. Como los topónimos US,
    # se retiran del texto ANTES de buscar restos; solo en este conjunto (cero código común). Sin tildes en EN (aji,
    # huancaina): la lista blanca no cambia
    M.RX_LUGARES_US = re.compile(M.RX_LUGARES_US.pattern + r'|(?i:\b(?:' + '|'.join(TERMINOS_PE) + r')\b)')
    _nc = M.necesita_clave
    M.necesita_clave = lambda lit, _nc=_nc: lit == '—' or _nc(lit)
    completar(M)
