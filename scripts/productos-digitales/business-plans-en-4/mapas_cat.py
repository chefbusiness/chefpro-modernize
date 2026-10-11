#!/usr/bin/env python3
"""
mapas_cat.py — Catering Business Plan Kit (EN) · datos ES→EN del conjunto «cat» (estructura).

SPEC: `SPEC-delta.md` (D66-D80) sobre `../business-plans-en-3/SPEC-delta.md` (D48-D65),
`../business-plans-en-2/SPEC-delta.md` (D30-D47) y `../business-plans-en/SPEC.md` (D1-D29). Sesión Claude Code,
11-oct-2026 (F2, paso 1). NO se ejecuta solo: lo importa `../business-plans-en/mapas.py` cuando `BP_CONJUNTO=cat` y
llama a `instalar(M)`, que SUSTITUYE en el módulo `mapas` los datos de food truck + cafetería por los del catering.

La FUENTE ES DEL CIRCUITO es el FOOD TRUCK ES (`plan-negocio-food-truck`: plan, checklist y docx), no el catering ES de
línea B (sus cifras y fórmulas no se reutilizan: F1-inventario-delta §0). El motor se reinterpreta solo con rótulos
(D72): B4 = eventos/año, B5 = precio por invitado, B6 = invitados por evento. El contenido de catering (concepto,
tareas, política comercial) lo escriben los redactores desde `fuente_es_cat.json` (catering ES) y research.

    python3 bp4.py mapas            # autotest + cruce con censo_es.json de esta carpeta

Grupos (D71):
  GM          motor común FT/CAF cuyo EN publicado (food truck) vale tal cual: no va a los traductores.
  GR          reutilizada con marca «revisar contexto» (EN del food truck que nombra local, alquiler, menú…):
              preparar_tandas escribe su EN; la tanda GCAT-check la revisa (textos_en/GR.revision.json).
  GCAT-plan   nuevas del plan: las cadenas PROPIAS del FT (se escriben para catering), las del motor que hablan de
              clientes/día, días, camión, ventanilla, festivales… y las celdas de las tablas D18/D19. Con propuesta
              (el EN del food truck de ESA celda) salvo D19.
  GCAT-check  checklist: las 272 celdas de las 68 tareas (una por celda: zona «TAREA») + los textos con vocabulario
              del food truck.
"""
import json
import os
import re
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
BP = os.path.join(os.path.dirname(AQUI), 'business-plans-en')

# ==========================================================================
# 0. Producto (D66-D68). dir_es = FUENTE DEL CIRCUITO (food truck ES); slug_es = gemelo ES para hreflang (D66)
# ==========================================================================
PLANES = OrderedDict([
    ('cat', OrderedDict([
        ('slug', 'catering-business-plan'),
        ('producto', 'Catering Business Plan Kit'),
        ('slug_es', 'plan-catering-tematico-eventos'),
        ('dir_es', 'astro-site/public/dl/plan-negocio-food-truck'),
        ('env_stripe', 'VITE_STRIPE_PAYMENT_LINK_CATERING_BUSINESS_PLAN'),
        ('keywords', 'catering business plan, catering business plan template, how to start a catering business, '
                     'catering startup costs, catering pricing per person, AI Chef Pro'),
    ])),
])
for _p in PLANES.values():
    _p['url'] = 'aichef.pro/en/digital-products/' + _p['slug']
    _p['dir_en'] = 'astro-site/public/dl/' + _p['slug']

LIBROS = OrderedDict([
    ('CATP', ('cat', 'plan-financiero-food-truck.xlsx', 'catering-financial-projections.xlsx',
              'Catering Financial Projections: 3-Year P&L, Cash Flow & Financing')),
    ('CATC', ('cat', 'checklist-apertura-food-truck.xlsx', 'catering-startup-checklist.xlsx',
              'Catering Startup Checklist (68 Tasks)')),
])
DOCX = OrderedDict([
    ('cat', ('plan-de-negocio-food-truck.docx', 'catering-business-plan.docx', 'Catering Business Plan (10 Sections)')),
])
TIPO_DE = {'CATP': 'plan', 'CATC': 'check'}
A_FT = {'CATP': 'FTP', 'CATC': 'FTC'}                       # libro del food truck del que sale cada libro

# ==========================================================================
# 1. Pestañas: plan = FT; checklist = FT con la fase 2 «Kitchen, Van & Permits» (D77). Excel admite 31 caracteres:
#    «Phase 2 - Kitchen, Van & Permits» tiene 32 → «Phase 2 - Kitchen, Van, Permits» (31; el título de la hoja,
#    que no tiene límite, conserva el «&»: «PHASE 2: KITCHEN, VAN & PERMITS»)
# ==========================================================================
_HOJAS_PLAN = OrderedDict([
    ('0. Supuestos', '0. Assumptions'), ('Inversión Inicial', 'Startup Costs'), ('PyG 3 Años', '3-Year P&L'),
    ('Punto Equilibrio', 'Break-Even'), ('Escenarios', 'Scenarios'), ('Personal', 'Staffing'),
    ('Instrucciones', 'Instructions'), ('Tesorería 12 meses', '12-Month Cash Flow'), ('Financiación', 'Financing'),
])
HOJA_F2_EN = 'Phase 2 - Kitchen, Van, Permits'
_HOJAS_CHECK = OrderedDict([
    ('F1 - Constitución', 'Phase 1 - Business Setup'), ('F2 - Vehículo', HOJA_F2_EN),
    ('F3 - Equipamiento', 'Phase 3 - Equipment'), ('F4 - Personal', 'Phase 4 - Staff'),
    ('F5 - Marketing', 'Phase 5 - Marketing'), ('F6 - 90 Días', 'Phase 6 - First 90 Days'),
    ('Instrucciones', 'Instructions'),
])
HOJAS_POR_LIBRO = OrderedDict([('CATP', _HOJAS_PLAN), ('CATC', _HOJAS_CHECK)])
HOJAS_ES_POR_LIBRO = OrderedDict((c, list(d)) for c, d in HOJAS_POR_LIBRO.items())
TAREAS_POR_FASE = OrderedDict([('CATC', [11, 13, 12, 10, 12, 10])])          # 68 (D77 = molde FT)
MOLDE_CHECK = OrderedDict([('CATC', 'hojas')])
COL_OK = OrderedDict([('CATC', 1)])
FASES_CABECERA = OrderedDict()
# filas de tarea de cada fase en el FT ES (censo: tareas_filas) → zona celda a celda «TAREA» (columnas B-E)
FILAS_TAREA = OrderedDict([('F1 - Constitución', (5, 15)), ('F2 - Vehículo', (5, 17)), ('F3 - Equipamiento', (5, 16)),
                           ('F4 - Personal', (5, 14)), ('F5 - Marketing', (5, 16)), ('F6 - 90 Días', (5, 14))])

# ==========================================================================
# 2. Fórmulas (D72): E2 del FT + Staffing!B20 (horas × personas × EVENTOS) + E4 (FTE = Σ personas × FTE) +
#    escalones de precio del Break-Even ±$10 / +$20 (el ±2 / +4 del FT estaba pensado para un ticket de $14)
# ==========================================================================
_E2_ALC = ("('0. Supuestos'!$B$62*'0. Supuestos'!$B$40+(1-'0. Supuestos'!$B$62)*'0. Supuestos'!$B$39)")
PARCHES_FORMULA = OrderedDict([
    (('CATP', 'PyG 3 Años', 'G13'), ("'0. Supuestos'!$B$39", "'0. Supuestos'!$B$41")),
    (('CATP', 'PyG 3 Años', 'G14'), (_E2_ALC, "'0. Supuestos'!$B$41")),
    (('CATP', 'Personal', 'B20'), ("'0. Supuestos'!$B$6", "'0. Supuestos'!$B$4")),
    (('CATP', 'Personal', 'C9'), ('SUM(C5:C8)', 'SUMPRODUCT(B5:B8,C5:C8)')),
    (('CATP', 'Punto Equilibrio', 'B31'), ('$B$8-2', '$B$8-10')),
    (('CATP', 'Punto Equilibrio', 'D31'), ('$B$8+2', '$B$8+10')),
    (('CATP', 'Punto Equilibrio', 'E31'), ('$B$8+4', '$B$8+20')),
])

# ==========================================================================
# 3. Instrucciones: versión D20 y aviso D21 (E1: CATP A74, CATC A12); zonas celda a celda: D18 (35-51) y D19 (55-68)
#    del plan como el FT, y las 68 tareas del checklist (B-E), cada celda con su id
# ==========================================================================
FILA_VERSION = OrderedDict([('CATP', 73), ('CATC', 11)])
ZONAS_CELDA = OrderedDict([(('CATP', 'Instrucciones'), [(35, 51, 'ABCD', 'D18'), (55, 68, 'ABCD', 'D19')])])
for _h, (_f1, _f2) in FILAS_TAREA.items():
    ZONAS_CELDA[('CATC', _h)] = [(_f1, _f2, 'BCDE', 'TAREA')]

# ==========================================================================
# 4. Docx (D78): las 131 ranuras del FT ES, H1 en 37·44·51·59·67·76·83·91·100·109; último de §9 = 108 (nota UK)
# ==========================================================================
DOCX_N_PARRAFOS = OrderedDict([('cat', 131)])
DOCX_ENCABEZADOS = OrderedDict([('cat', [37, 44, 51, 59, 67, 76, 83, 91, 100, 109])])
DOCX_INDICE = OrderedDict([('cat', list(range(24, 34)))])
DOCX_ULTIMO_9 = OrderedDict([('cat', '108')])
DOCX_TANDAS = OrderedDict([('cat_a', ('cat', [1, 2, 3, 4, 5])), ('cat_b', ('cat', [6, 7, 8, 9, 10]))])
PRESTAMO_SEMILLA = OrderedDict([('cat', 146000)])                   # punto fijo del dry-run (research §8: ≈ 140,000)

AUTOTEST = OrderedDict([
    ('P1', 'CATP'), ('P2', 'CATP'), ('C1', 'CATC'), ('C2', 'CATC'),
    ('C1_hoja_papel', 'F2 - Vehículo'), ('C1_titulo', 'Catering Startup Checklist (68 Tasks)'),
    ('C2_hoja_no_latino', 'F5 - Marketing'), ('P1_celda_texto', 'A3'), ('P1_celda_formula', 'B9'),
    ('P1_merge', 'A30:C30'),
])

# ==========================================================================
# 5. Grupos (D71)
# ==========================================================================
GRUPOS = ('GM', 'GR', 'GCAT-plan', 'GCAT-check')
GRUPOS_TRADUCTORES = ('GCAT-plan', 'GCAT-check')
GRUPOS_OVERRIDES = ('GCAT-plan', 'GCAT-check')
REVISAR_EN_TANDA = OrderedDict([('GCAT-check', ('GR',))])
GRUPOS_DESC = OrderedDict([
    ('GM', 'REUTILIZADAS: cadenas del motor común FT/CAF cuyo EN del Food Truck publicado vale para catering (sin '
           'vocabulario de food truck ni de local). preparar_tandas escribe su EN. No van a los traductores'),
    ('GR', 'REUTILIZADAS con marca «revisar contexto»: EN del Food Truck que nombra alquiler, local, menú, reparto, '
           'vehículo o comisaria. preparar_tandas escribe su EN; la tanda GCAT-check las revisa y corrige en '
           'textos_en/GR.revision.json'),
    ('GCAT-plan', 'Plan financiero (CATP): las cadenas propias del FT (se escriben NUEVAS para catering), las del motor '
                  'que hablan de clientes/día, días, ticket, camión, ventanilla o festivales, y TODAS las celdas de las '
                  'tablas D18/D19 de Instrucciones (una por celda). Propuesta = EN del Food Truck de esa celda (salvo D19)'),
    ('GCAT-check', 'Checklist (CATC): las 68 tareas × 4 columnas (una por celda; contenido del catering ES + research §6) '
                   'y los textos del checklist con vocabulario de food truck; + revisión de las reutilizadas GR'),
    ('GX', 'NO se traduce: pestañas (mapas.HOJAS_POR_LIBRO), CLAVES, FIJOS, POR_CELDA, versión, pie y docProps'),
])

# Vocabulario que NO se reutiliza (D71/D72): se busca en el ES del FT y en su EN publicado
RX_ACTIVIDAD_ES = re.compile(r'[Cc]lientes?\b|[Dd]ías de (?:apertura|servicio)|\bal día\b|/día\b|por día|[Dd]iari|'
                             r'[Vv]ehícul|[Ff]ood ?[Tt]ruck|[Cc]amión|[Vv]entanilla|[Ff]estival|[Aa]mbulante|'
                             r'[Gg]enerador|[Rr]emolque|[Tt]icket|\b[Cc]alle\b|[Mm]ercados\b')
RX_ACTIVIDAD_EN = re.compile(r'(?i)\bcustomers?\b|\bper day\b|\ba day\b|\bdaily\b|\b(?:operating|opening|service) '
                             r'days?\b|\btrucks?\b|\bwindows?\b|\bfestivals?\b|\bvending\b|\bgenerators?\b|\bpropane\b|'
                             r'\btrailers?\b|\baverage check\b|\bstreet\b|\bmarkets\b|\bwalk-?up\b|\blunch rush\b')
# EN reutilizable pero con contexto de local / vehículo → GR (revisar contexto)
RX_REVISAR_EN = re.compile(r'(?i)\b(?:rent|premises|menu|seats?|seating|dining|location|delivery|lease|landlord|'
                           r'build-?out|shop|store|restaurant|caf[eé]|commissary|parking|vehicle|van|counter)\b')


# --------------------------------------------------------------------------
# EN publicado del Food Truck, celda a celda (../business-plans-en: textos_es.json + GM/GFT + overrides_GFT)
# --------------------------------------------------------------------------
def _cargar_ft():
    te_p = os.path.join(BP, 'textos_es.json')
    out = OrderedDict()
    if not os.path.exists(te_p):
        return out
    te = json.load(open(te_p, encoding='utf-8'))
    en = {}
    for g in ('GM', 'GFT'):
        p = os.path.join(BP, 'textos_en', g + '.json')
        if os.path.exists(p):
            en.update(json.load(open(p, encoding='utf-8')))
    po = os.path.join(BP, 'textos_en', 'overrides_GFT.json')
    ov = json.load(open(po, encoding='utf-8')) if os.path.exists(po) else {}
    for c in te['cadenas']:
        if c['grupo'] not in ('GM', 'GFT') or c['id'] not in en:
            continue
        for d in c['donde']:
            if d.get('t') != 'celda' or d['f'] not in ('FTP', 'FTC'):
                continue
            t = en[c['id']]
            o = ov.get(c['id'])
            if o and (o['libro'], o['hoja'], o['celda']) == (d['f'], d['h'], d['c']):
                t = o['texto']                       # el EN publicado de ESA celda (ronda de arreglos del FT)
            out[(d['f'], d['h'], d['c'])] = (t, c['grupo'], c['id'], c['tratamiento'])
    return out


def _cargar_ft_texto():
    """ES → (EN, grupo, id, tratamiento) del FT para las apariciones que NO son celda (mensajes de DV, cabeceras):
    mismo texto ES = mismo EN."""
    out = OrderedDict()
    te_p = os.path.join(BP, 'textos_es.json')
    if not os.path.exists(te_p):
        return out
    en = {}
    for g in ('GM', 'GFT'):
        p = os.path.join(BP, 'textos_en', g + '.json')
        if os.path.exists(p):
            en.update(json.load(open(p, encoding='utf-8')))
    for c in json.load(open(te_p, encoding='utf-8'))['cadenas']:
        if c['grupo'] in ('GM', 'GFT') and c['id'] in en and 'ft' in c.get('planes', []):
            out.setdefault(c['es'], (en[c['id']], c['grupo'], c['id'], c['tratamiento']))
    return out


FT_CELDA = _cargar_ft()
FT_TEXTO = _cargar_ft_texto()
# celdas que van a los traductores aunque su EN del FT valga en general: llevan una nota propia del catering (D73)
FORZAR_TRADUCTORES = {('CATP', 'Escenarios', 'E23')}
# mensajes de DV compartidos por B6 (ahora INVITADOS por evento), B58/B59 (días) y los invitados de Escenarios
FORZAR_TEXTOS = {'Días fuera de rango', 'Los días van de 1 a 365.'}


def ft_de(donde, es=None):
    """[(EN publicado del FT, grupo, id FT, tratamiento FT)] de las apariciones en celda de una cadena del catering;
    si no tiene ninguna en celda (mensaje de DV…), el EN del mismo texto ES en el FT."""
    out = []
    for o in donde or []:
        if o.get('t') != 'celda':
            continue
        k = (A_FT.get(o['f']), o.get('h'), o.get('c'))
        if k in FT_CELDA:
            out.append(FT_CELDA[k])
    if not out and es in FT_TEXTO and not any(o.get('t') == 'celda' for o in donde or []):
        out.append(FT_TEXTO[es])
    return out


def grupo_de(planes, texto=None, tratamiento=None, donde=None):
    libros = {o['f'] for o in (donde or [])}
    destino = 'GCAT-check' if libros == {'CATC'} else 'GCAT-plan'
    if tratamiento != 'traducir':
        return destino                                 # localizar: tablas D18/D19 y celdas de tarea del checklist
    if texto in FORZAR_TEXTOS or any((o['f'], o.get('h'), o.get('c')) in FORZAR_TRADUCTORES for o in donde or []):
        return destino
    ft = ft_de(donde, texto)
    if not ft or len({x[0] for x in ft}) > 1 or ft[0][3] != 'traducir':
        return destino                                 # sin EN del FT, o con EN distinto por celda
    en, g = ft[0][0], ft[0][1]
    if RX_ACTIVIDAD_ES.search(texto or '') or RX_ACTIVIDAD_EN.search(en):
        return destino
    if g == 'GFT' and 'CATP' in libros:
        return destino                                 # D71: lo propio del FT en el plan se escribe para catering
    if g == 'GM' and not RX_REVISAR_EN.search(en):
        return 'GM'
    return 'GR'


def reuso_de(e):
    """EN del Food Truck de la PRIMERA celda de la cadena: el EN de GM/GR o la PROPUESTA de los traductores (que la
    revisan, el contexto cambia). D19 sin propuesta: sus filas cambian enteras por los benchmarks de catering (D75)."""
    if any(o.get('det') == 'D19' for o in e['donde']):
        return None
    ft = ft_de(e['donde'], e['es'])
    if not ft:
        return None
    en, g, ident, tr = ft[0]
    return OrderedDict([('grupo', g), ('id', ident), ('en', en), ('tratamiento_origen', tr),
                        ('conjunto', 'business-plans-en (Food Truck EN publicado)'),
                        ('donde', ['%s %s!%s' % (A_FT.get(o['f']), o.get('h', ''), o.get('c', ''))
                                   for o in e['donde'][:2]])])


# ==========================================================================
# instalar
# ==========================================================================
def instalar(M):
    """Sustituye en el módulo `mapas` (M) los datos de FT/CAF por los del catering."""
    from datos_cat import completar                                        # contenido (FIJOS, caso US, docx…)
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
    M.REUSO = OrderedDict()                     # el reuso del catering es por CELDA (FT_CELDA), no por texto
    M.FUENTES_CIFRAS = [os.path.join(BP, 'F1-research-us.md'), os.path.join(BP, 'SPEC.md'),
                        os.path.join(AQUI, 'F1-research-us-delta.md'), os.path.join(AQUI, 'SPEC-delta.md')]
    M.NOTAS_F2 = os.path.join(AQUI, 'F2-NOTAS.md')
    completar(M)
