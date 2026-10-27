#!/usr/bin/env python3
"""
inventario_delta.py — Wedding Venue Business Plan Kit (EN) · inventario de F1 (sesión Claude Code, 27-oct-2026).
Clon de `../business-plans-en-8/inventario_delta.py` (Pizza Shop EN) con: los 3 xlsx + 2 docx ES de la FINCA
(`dl/plan-negocio-finca-eventos-bodas/`, ES 1.0 LIVE), las referencias ES de su semilla (PANADERÍA 2.2) y de sus
hermanas de motor (HELADERÍA = misma semilla; PARRILLERO = mismo contenido de eventos; PIZZERÍA = motor 2.2 más reciente)
y el EN ya escrito de los 8 conjuntos (piz, bbq, pael, bar, cat, restpan, ftcaf) como fuentes de reutilización.
Solo lectura; salida inventario_delta.json (+ resumen por pantalla).

    VPS:  cd /root/wt-wedding/scripts/productos-digitales/business-plans-en-9 && /root/venv-guias/bin/python inventario_delta.py

Mide: (1) clasificación de cadenas por la 1.ª fuente con EN, exacta y tras NORMALIZAR la finca al motor genérico
(VOCABULARIO de la finca invertido: invitado → cubierto, evento → día, finca → local…); (2) estructura y parecido celda
a celda (fórmulas y rótulos) con cada referencia; (3) fórmulas con texto y su gemela; (4) caso ES (Supuestos, inversión,
fijos, personal, columna de IVA, verdes); (5) Word, contrato y calculadora. No traduce nada.
"""
import argparse
import ast
import collections
import json
import os
import re
import sys

import docx
import openpyxl
from openpyxl.utils import range_boundaries

AQUI = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
PD = os.path.dirname(AQUI)
BP = os.path.join(PD, 'business-plans-en')
BP2 = os.path.join(PD, 'business-plans-en-2')
BAR = os.path.join(PD, 'business-plans-en-3')
CAT = os.path.join(PD, 'business-plans-en-4')
BBQ = os.path.join(PD, 'business-plans-en-6')
PAEL = os.path.join(PD, 'business-plans-en-7')
PIZ = os.path.join(PD, 'business-plans-en-8')
A_FINCA = os.path.join(PD, 'planes-v2_0', 'contenido_plan_negocio_finca_eventos_bodas', 'a.py')
sys.path.insert(0, BP)
os.environ.setdefault('BP_CONJUNTO', 'ftcaf')
import mapas                                                     # noqa: E402  (CLAVES del molde FT/CAF)

DL = 'astro-site/public/dl'
FIN = 'plan-negocio-finca-eventos-bodas'
LIBROS = collections.OrderedDict([
    ('WEDP', (FIN, 'plan-financiero-finca-eventos-bodas.xlsx')),
    ('WEDC', (FIN, 'checklist-apertura-finca-eventos-bodas.xlsx')),
])
CALC = (FIN, 'calculadora-presupuesto-boda-evento-finca.xlsx')
DOCX_PLAN = (FIN, 'plan-de-negocio-finca-eventos-bodas.docx')
DOCX_CONTRATO = (FIN, 'modelo-contrato-reserva-finca-eventos.docx')
REF = collections.OrderedDict([          # libros ES (estructura y fórmulas); la semilla (panadería), 1.º
    ('PANP', ('plan-negocio-panaderia', 'plan-financiero-panaderia.xlsx')),
    ('HELP', ('plan-negocio-heladeria', 'plan-financiero-heladeria.xlsx')),
    ('PARP', ('plan-negocio-parrillero-asador-eventos', 'plan-financiero-parrillero-asador-eventos.xlsx')),
    ('PIZP', ('plan-negocio-pizzeria', 'plan-financiero-pizzeria.xlsx')),
    ('BARP', ('plan-negocio-tapas-bar', 'plan-financiero-tapas-bar.xlsx')),
    ('FTP', ('plan-negocio-food-truck', 'plan-financiero-food-truck.xlsx')),
    ('PANC', ('plan-negocio-panaderia', 'checklist-apertura-panaderia.xlsx')),
    ('HELC', ('plan-negocio-heladeria', 'checklist-apertura-heladeria.xlsx')),
    ('PARC', ('plan-negocio-parrillero-asador-eventos', 'checklist-apertura-parrillero-asador-eventos.xlsx')),
    ('PIZC', ('plan-negocio-pizzeria', 'checklist-apertura-pizzeria.xlsx')),
])
# fuentes de EN ya escrito: (carpeta, grupo, etiqueta). Orden = prioridad de reutilización (la más reciente primero).
FUENTES = [
    (PIZ, 'GM', 'PIZ-GM'), (PIZ, 'GR', 'PIZ-GR'), (PIZ, 'GPIZ-plan', 'PIZ'), (PIZ, 'GPIZ-check', 'PIZ'),
    (BBQ, 'GM', 'BBQ-GM'), (BBQ, 'GRC-plan', 'BBQ'), (BBQ, 'GBQ-plan', 'BBQ'), (BBQ, 'GBQ-check', 'BBQ'),
    (PAEL, 'GM', 'PAEL-GM'), (PAEL, 'GRB-plan', 'PAEL'), (PAEL, 'GPA-plan', 'PAEL'), (PAEL, 'GPA-check', 'PAEL'),
    (PAEL, 'GLB-check', 'PAEL'),
    (BAR, 'GM', 'BAR-GM'), (BAR, 'GR', 'BAR'), (BAR, 'GBAR-plan', 'BAR'), (BAR, 'GBAR-check', 'BAR'),
    (BP2, 'GM', 'PAN-GM'), (BP2, 'GPAN', 'PAN'), (BP2, 'GREST', 'REST'), (BP2, 'GN', 'REST'),
    (BP, 'GM', 'GM'), (BP, 'GCAF', 'CAF'), (BP, 'GFT', 'FT'),
    (CAT, 'GM', 'CAT-GM'), (CAT, 'GR', 'CAT'), (CAT, 'GCAT-plan', 'CAT'), (CAT, 'GCAT-check', 'CAT'),
]
DOCX_REF = [(BP, 'ft'), (BP, 'caf'), (BP2, 'rest'), (BP2, 'pan'), (BAR, 'bar'), (CAT, 'cat'), (BBQ, 'bbq'),
            (PAEL, 'pael'), (PIZ, 'piz')]
VERDE = 'E8F5E9'
INVARIABLES = ('✓', '☐', 'OK', 'N/A', '—', 'AI Chef Pro', 'Break-even', 'DSCR', 'EBITDA', 'Marketing')
RX_LIT = re.compile(r'"((?:[^"]|"")*)"')
RX_LETRA = re.compile(r'[A-Za-zÁÉÍÓÚáéíóúÑñÜü]')
RX_PAL = re.compile(r"[A-Za-zÀ-ÿ0-9]+(?:[.,'’-][A-Za-zÀ-ÿ0-9]+)*")
RX_EUR = re.compile(r'(\d{1,3}(?:\.\d{3})+|\d+)(?:,\d+)?\s*(?:€|euros?\b|EUR\b|K\s*€|K\s*EUR)', re.I)
RX_HOJA_REF = re.compile(r"'([^']+)'!|\b([A-Za-zÁÉÍÓÚáéíóúñÑ0-9_.]+)!")


def norm_hoja(h):
    if h == '0. Supuestos':
        return h
    h = re.sub(r'^\d+\. ', '', h)
    return {'P&L 3 Años': 'PyG 3 Años'}.get(h, h)


def norm_formula(f):
    return RX_HOJA_REF.sub(lambda m: "'%s'!" % norm_hoja(m.group(1) or m.group(2)), f or '')


def palabras(s):
    return len(RX_PAL.findall(s or ''))


def literales(f):
    return [m.group(1).replace('""', '"') for m in RX_LIT.finditer(f or '')]


def abrir(repo, d, f, data_only=False):
    return openpyxl.load_workbook(os.path.join(repo, DL, d, f), data_only=data_only)


def es_verde(c):
    rgb = c.fill.fgColor.rgb if c.fill is not None and c.fill.fgColor is not None else None
    return isinstance(rgb, str) and rgb[-6:].upper() == VERDE


# ------------------------------------------------------------------ normalización finca → motor genérico
def vocabulario_finca():
    """VOCABULARIO de la finca (a.py) por ast, sin importar el motor."""
    arbol = ast.parse(open(A_FINCA, encoding='utf-8').read())
    for nodo in arbol.body:
        if isinstance(nodo, ast.Assign) and any(getattr(t, 'id', '') == 'VOCABULARIO' for t in nodo.targets):
            return ast.literal_eval(nodo.value)
    return {}


def normalizadores():
    """Dos variantes de la inversa (invitado → cubierto / → comensal), la clave más larga primero."""
    voc = vocabulario_finca()
    out = []
    for preferida in ('cubiert', 'comensal'):
        inv = {}
        for k, v in voc.items():
            if len(v) > 140 or len(k) > 140:
                continue                           # frases largas: no son vocabulario, son notas reescritas
            if v in inv and not k.startswith(preferida):
                continue
            inv[v] = k
        claves = sorted(inv, key=len, reverse=True)
        rx = re.compile('|'.join(r'(?<![\wáéíóúñ])%s(?![\wáéíóúñ])' % re.escape(c) for c in claves))
        out.append((rx, inv))
    return out


def normalizar(t, norms):
    return [rx.sub(lambda m: inv[m.group(0)], t) for rx, inv in norms]


# ------------------------------------------------------------------ diccionario de reutilización
def cargar_reuso():
    """es → [(etiqueta, grupo, id, en, por_celda)] con el EN ya escrito de los conjuntos anteriores."""
    reuso = collections.defaultdict(list)
    gx = set()
    prio = {}
    for i, (carpeta, g, et) in enumerate(FUENTES):
        prio.setdefault((carpeta, g), (i, et))
    carpetas = list(dict.fromkeys(c for c, _g, _e in FUENTES))
    for carpeta in carpetas:
        tes = json.load(open(os.path.join(carpeta, 'textos_es.json')))
        en_g = {}
        for (cp, g, _e) in FUENTES:
            if cp != carpeta:
                continue
            p = os.path.join(carpeta, 'textos_en', g + '.json')
            if os.path.exists(p):
                en_g[g] = json.load(open(p))
            po = os.path.join(carpeta, 'textos_en', 'overrides_%s.json' % g)
            if os.path.exists(po):
                en_g['ov_' + g] = json.load(open(po))
        for c in tes['cadenas']:
            g = c['grupo']
            if g == 'GX':
                gx.add(c['es'])
                continue
            if (carpeta, g) not in prio:
                continue
            en = (en_g.get(g) or {}).get(c['id'])
            if en is None and c.get('reuso'):
                en = c['reuso'].get('en')
            if en is None:
                continue
            ov = (en_g.get('ov_' + g) or {}).get(c['id'])
            por_celda = bool(c.get('por_celda')) or ov is not None
            reuso[c['es']].append((prio[(carpeta, g)][0], prio[(carpeta, g)][1], g, c['id'], en, por_celda))
    for k in reuso:
        reuso[k].sort()
    return reuso, gx


# ------------------------------------------------------------------ xlsx
def ocurrencias(wb):
    out = []
    for ws in wb.worksheets:
        out.append((ws.title, (ws.title, 'pestaña')))
        for row in ws.iter_rows():
            for c in row:
                v = c.value
                if isinstance(v, str) and c.data_type != 'f' and not v.startswith('='):
                    out.append((v, (ws.title, c.coordinate)))
        for dv in ws.data_validations.dataValidation:
            for campo in ('errorTitle', 'error', 'promptTitle', 'prompt'):
                t = getattr(dv, campo)
                if t:
                    out.append((t, (ws.title, 'dv-' + campo)))
        for nombre in ('oddFooter', 'oddHeader'):
            obj = getattr(ws, nombre)
            for parte in ('left', 'center', 'right'):
                t = getattr(obj, parte).text
                if t:
                    out.append((t, (ws.title, 'pie')))
    p = wb.properties
    for campo in ('title', 'subject', 'keywords', 'description'):
        t = getattr(p, campo)
        if t:
            out.append((t, ('docProps', campo)))
    return out


def _filas(rng):
    _c1, r1, _c2, r2 = range_boundaries(rng)
    return range(r1, r2 + 1)


def mapa_formulas(wb):
    out = {}
    for ws in wb.worksheets:
        h = norm_hoja(ws.title)
        for row in ws.iter_rows():
            for c in row:
                if c.data_type == 'f' or (isinstance(c.value, str) and c.value.startswith('=')):
                    out[(h, c.coordinate)] = norm_formula(str(c.value))
    return out


def estructura(wb):
    hojas = collections.OrderedDict()
    fx_texto = collections.OrderedDict()
    for ws in wb.worksheets:
        n_txt = n_fx = verdes = desbl = pal = 0
        for row in ws.iter_rows():
            for c in row:
                v = c.value
                if es_verde(c):
                    verdes += 1
                    if c.protection is not None and c.protection.locked is False:
                        desbl += 1
                if v is None:
                    continue
                if c.data_type == 'f' or (isinstance(v, str) and v.startswith('=')):
                    n_fx += 1
                    lt = [x for x in literales(str(v)) if RX_LETRA.search(x)]
                    if [x for x in lt if x not in mapas.CLAVES]:
                        fx_texto['%s!%s' % (ws.title, c.coordinate)] = str(v)
                elif isinstance(v, str):
                    n_txt += 1
                    pal += palabras(v)
        cf = sum(len(r) for r in ws.conditional_formatting._cf_rules.values())
        dvs = [(dv.type, dv.formula1, str(dv.sqref)) for dv in ws.data_validations.dataValidation]
        h = collections.OrderedDict([
            ('rango', ws.dimensions), ('textos', n_txt), ('palabras', pal), ('formulas', n_fx), ('dv', len(dvs)),
            ('dv_detalle', dvs), ('cf', cf), ('merges', len(ws.merged_cells.ranges)), ('verdes', verdes),
            ('verdes_desbloqueadas', desbl), ('papel', ws.page_setup.paperSize),
            ('protegida', bool(ws.protection.sheet)), ('password', bool(ws.protection.password))])
        tareas = sorted({r for dv in ws.data_validations.dataValidation if (dv.formula1 or '').startswith('"✓')
                         for rng in str(dv.sqref).split() for r in _filas(rng)})
        if tareas:
            h['tareas'] = len(tareas)
            h['filas_tareas'] = '%d-%d' % (tareas[0], tareas[-1])
            h['cabecera'] = [ws.cell(tareas[0] - 1, k).value for k in range(1, 6)]
            h['A1'], h['A2'] = ws['A1'].value, ws['A2'].value
        hojas[ws.title] = h
    return hojas, fx_texto


def rotulos(wb):
    return {norm_hoja(ws.title): [(c.row, c.value.strip()) for c in ws['A']
                                  if isinstance(c.value, str) and c.value.strip()] for ws in wb.worksheets}


def verdes_de(wbf, wbv, hojas):
    out = collections.OrderedDict()
    for h in hojas:
        if h not in wbf.sheetnames:
            continue
        ws, wv = wbf[h], wbv[h]
        lst = []
        for row in ws.iter_rows():
            for c in row:
                if es_verde(c) and c.value is not None:
                    rot = ws.cell(c.row, 1).value
                    lst.append((c.coordinate, (rot or '')[:70] if isinstance(rot, str) else rot, c.value,
                                wv[c.coordinate].value))
        out[h] = lst
    return out


# ------------------------------------------------------------------ docx
def analizar_docx(ruta):
    doc = docx.Document(ruta)
    ps = doc.paragraphs
    est = collections.Counter(p.style.name for p in ps)
    encab, eur = [], []
    secciones, sec = collections.OrderedDict(), 0
    for i, p in enumerate(ps):
        t = p.text
        for mm in RX_EUR.finditer(t):
            eur.append((i, mm.group(0)))
        if p.style.name.startswith('Heading') or p.style.name in ('H1', 'H2', 'Title'):
            if p.style.name in ('Heading 1', 'H1'):
                sec += 1
            encab.append((i, p.style.name, t[:90]))
        secciones.setdefault(sec, [0, 0])
        secciones[sec][0] += 1 if t.strip() else 0
        secciones[sec][1] += palabras(t)
    s = doc.sections[0]
    return collections.OrderedDict([
        ('parrafos', len(ps)), ('con_texto', sum(1 for p in ps if p.text.strip())), ('estilos', dict(est)),
        ('palabras', sum(palabras(p.text) for p in ps)), ('encabezados', encab), ('tablas', len(doc.tables)),
        ('tabla_celdas', [[c.text[:40] for c in r.cells] for t in doc.tables for r in t.rows][:30]),
        ('imagenes', len(doc.inline_shapes)), ('importes_eur', eur[:80]),
        ('secciones', {k: {'parrafos_texto': v[0], 'palabras': v[1]} for k, v in secciones.items()}),
        ('pagina_emu', [s.page_width, s.page_height]),
        ('core', {'title': doc.core_properties.title, 'author': doc.core_properties.author,
                  'subject': doc.core_properties.subject, 'keywords': doc.core_properties.keywords,
                  'comments': doc.core_properties.comments}),
        ('texto', {i: p.text for i, p in enumerate(ps) if p.text.strip()}),
        ('estilo_idx', {i: p.style.name for i, p in enumerate(ps)}),
    ])


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=os.path.abspath(os.path.join(PD, '..', '..')))
    ap.add_argument('--salida', default=os.path.join(AQUI, 'inventario_delta.json'))
    a = ap.parse_args()

    reuso, gx_prev = cargar_reuso()
    norms = normalizadores()
    tabs_conocidas = set()
    for d in mapas.HOJAS_POR_LIBRO.values():
        tabs_conocidas.update(d)

    out = collections.OrderedDict()
    occ, estr, rots, fx = collections.OrderedDict(), collections.OrderedDict(), {}, {}
    for corto, (d, f) in LIBROS.items():
        wb = abrir(a.repo, d, f)
        occ[corto] = ocurrencias(wb)
        hojas, fxt = estructura(wb)
        p = wb.properties
        estr[corto] = {'hojas': hojas, 'formulas_con_texto': fxt,
                       'docprops': {'title': p.title, 'subject': p.subject, 'creator': p.creator,
                                    'keywords': p.keywords, 'description': p.description}}
        rots[corto] = rotulos(wb)
        fx[corto] = mapa_formulas(wb)
    ref_fxt = {}
    for corto, (d, f) in REF.items():
        wb = abrir(a.repo, d, f)
        rots[corto] = rotulos(wb)
        fx[corto] = mapa_formulas(wb)
        if corto.endswith('P'):
            _h, ref_fxt[corto] = estructura(wb)
            estr['ref_' + corto] = {'hojas': {k: {kk: v[kk] for kk in ('rango', 'textos', 'formulas', 'verdes')}
                                              for k, v in _h.items()}}

    # ---- 1. clasificación de cadenas (exacta y normalizada)
    donde = collections.defaultdict(list)
    for corto, lst in occ.items():
        for t, w in lst:
            donde[t].append('%s:%s!%s' % (corto, w[0], w[1]))
    tabla = collections.OrderedDict()
    resumen = collections.defaultdict(collections.Counter)
    for t, ds in donde.items():
        fuente, via = None, None
        if not RX_LETRA.search(t) or t in INVARIABLES:
            g = 'SIN-LETRAS'
        elif t in reuso:
            fuente, via = reuso[t][0], 'exacta'
            g = fuente[1]
        else:
            for tn in normalizar(t, norms):
                if tn != t and tn in reuso:
                    fuente, via = reuso[tn][0], 'normalizada'
                    break
            if fuente:
                g = 'N-' + fuente[1]
            elif t in mapas.CLAVES or t in tabs_conocidas or t in gx_prev or any(':docProps!' in x for x in ds) \
                    or any('!pestaña' in x for x in ds):
                g = 'GX'
            else:
                g = 'WED'
        libros = sorted({x.split(':')[0] for x in ds})
        tipo = 'check' if libros == ['WEDC'] else ('plan' if libros == ['WEDP'] else 'ambos')
        tabla[t] = collections.OrderedDict([('grupo', g), ('tipo', tipo), ('palabras', palabras(t)), ('n', len(ds)),
                                            ('donde', ds[:6])])
        if fuente:
            tabla[t]['reuso'] = {'via': via, 'de': fuente[2], 'id': fuente[3], 'en': fuente[4],
                                 'por_celda': fuente[5],
                                 'otras': sorted({x[1] for x in reuso.get(t, [])[1:]})}
        resumen['_cadenas'][g] += 1
        resumen['_palabras'][g] += palabras(t)
        resumen['_' + tipo][g] += 1
    out['clasificacion'] = {k: dict(v) for k, v in resumen.items()}
    out['cadenas'] = tabla

    # ---- 2. parecido con las referencias
    out['estructura'] = estr
    parecido = collections.OrderedDict()
    for corto in LIBROS:
        pc = collections.OrderedDict()
        for r in [r for r in REF if r[-1] == corto[-1]]:
            fb, fr = fx[corto], fx[r]
            por_hoja = collections.OrderedDict()
            for h in dict.fromkeys(k[0] for k in fb):
                ks = [k for k in fb if k[0] == h]
                por_hoja[h] = '%d/%d' % (sum(1 for k in ks if fr.get(k) == fb[k]), len(ks))
            rb = {(h, f_, x) for h, lst in rots[corto].items() for f_, x in lst}
            rr = {(h, f_, x) for h, lst in rots[r].items() for f_, x in lst}
            pc[r] = collections.OrderedDict([
                ('pestanas', [h for h in rots[corto] if h in rots[r]]),
                ('formulas_identicas', '%d/%d' % (sum(1 for k, v in fb.items() if fr.get(k) == v), len(fb))),
                ('formulas_por_hoja', por_hoja),
                ('rotulos_misma_fila', '%d/%d' % (len(rb & rr), len(rb)))])
        parecido[corto] = pc
    out['parecido'] = parecido
    distintas = collections.OrderedDict()
    for corto in LIBROS:
        refs = [r for r in REF if r[-1] == corto[-1]]
        lst = [('%s!%s' % k, v) for k, v in fx[corto].items() if not any(fx[r].get(k) == v for r in refs)]
        distintas[corto] = {'n': len(lst), 'muestra': lst[:60]}
        if corto == 'WEDP':
            distintas['WEDP_vs_PANP'] = [('%s!%s' % k, v, fx['PANP'].get(k)) for k, v in fx[corto].items()
                                         if fx['PANP'].get(k) != v][:80]
    out['formulas_sin_gemela'] = distintas

    # ---- 3. fórmulas con texto y su gemela por literales
    lits_ref = collections.defaultdict(list)
    for r, fxt in ref_fxt.items():
        for celda, f in fxt.items():
            lits_ref[tuple(literales(f))].append('%s!%s' % (r, celda))
    out['formulas_con_texto'] = {celda: {'formula': f[:300], 'gemelas': lits_ref.get(tuple(literales(f)), [])[:4]}
                                 for celda, f in estr['WEDP']['formulas_con_texto'].items()}

    # ---- 4. caso ES
    wbv = abrir(a.repo, *LIBROS['WEDP'], data_only=True)
    wbf = abrir(a.repo, *LIBROS['WEDP'])
    ws, wsf = wbv['0. Supuestos'], wbf['0. Supuestos']
    out['supuestos_es'] = [(c.row, c.value[:110], wsf.cell(c.row, 2).value, ws.cell(c.row, 2).value)
                           for c in ws['A'] if isinstance(c.value, str) and c.row > 2]
    for hoja in wbf.sheetnames:
        if hoja in ('0. Supuestos', 'Instrucciones'):
            continue
        wsv = wbv[hoja]
        out['filas_' + hoja] = [(c.row, c.value[:90], wsv.cell(c.row, 2).value, wsv.cell(c.row, 3).value)
                                for c in wsv['A'] if isinstance(c.value, str)]
    pyg = next(h for h in wbf.sheetnames if h.startswith('PyG') or h.startswith('P&L'))
    out['pyg_GH'] = [(r, wbf[pyg].cell(r, 1).value, wbf[pyg].cell(r, 7).value, wbv[pyg].cell(r, 7).value,
                      wbf[pyg].cell(r, 8).value) for r in range(1, 60)
                     if wbf[pyg].cell(r, 7).value is not None or wbf[pyg].cell(r, 8).value is not None]
    out['instrucciones_es'] = [(c.coordinate, str(c.value)[:160]) for row in wbf['Instrucciones'].iter_rows()
                               for c in row if c.value is not None]
    tes = next(h for h in wbf.sheetnames if h.startswith('Tesor'))
    out['tesoreria_notas'] = [(c.coordinate, str(c.value)[:200]) for row in wbf[tes].iter_rows()
                              for c in row if isinstance(c.value, str) and c.column >= 14]
    out['verdes'] = verdes_de(wbf, wbv, [h for h in wbf.sheetnames if h != 'Instrucciones'])

    # ---- 5. calculadora, Word y contrato
    wbc = abrir(a.repo, *CALC)
    hc, fxc = estructura(wbc)
    out['calculadora'] = {'hojas': hc, 'formulas_con_texto': len(fxc),
                          'textos': [(ws.title, c.coordinate, str(c.value)[:120]) for ws in wbc.worksheets
                                     for row in ws.iter_rows() for c in row
                                     if isinstance(c.value, str) and not c.value.startswith('=')][:400],
                          'docprops': {'title': wbc.properties.title, 'keywords': wbc.properties.keywords}}
    r = analizar_docx(os.path.join(a.repo, DL, *DOCX_PLAN))
    ident = collections.Counter()
    for carpeta, plan in DOCX_REF:
        pj = os.path.join(carpeta, 'docx_es_%s.json' % plan)
        if not os.path.exists(pj):
            continue
        dj = json.load(open(pj))
        txt = {x['texto'] for x in dj['parrafos'].values() if x['texto'].strip()}
        ident[plan] = sum(1 for t in r['texto'].values() if t in txt)
        if plan == 'pael':      # mismo molde de 131 párrafos: estilos índice a índice
            r['estilos_igual_pael'] = '%d/%d' % (sum(1 for i, x in dj['parrafos'].items()
                                                     if r['estilo_idx'].get(int(i)) == x['estilo']), len(dj['parrafos']))
    r['parrafos_identicos'] = dict(ident)
    out['docx'] = r
    out['contrato'] = analizar_docx(os.path.join(a.repo, DL, *DOCX_CONTRATO))

    with open(a.salida, 'w') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1, default=str)

    # ---- resumen
    print('== clasificación (cadenas únicas · palabras) ==')
    for k in ('_cadenas', '_palabras', '_plan', '_check', '_ambos'):
        print('  %-9s %s' % (k, dict(sorted(out['clasificacion'].get(k, {}).items()))))
    print('== estructura ==')
    for corto, e in estr.items():
        if corto.startswith('ref_'):
            print(' ', corto, {h: (v['rango'], v['textos'], v['formulas']) for h, v in e['hojas'].items()})
            continue
        tot = collections.Counter()
        for h in e['hojas'].values():
            for kk in ('textos', 'palabras', 'formulas', 'dv', 'cf', 'merges', 'verdes', 'verdes_desbloqueadas',
                       'tareas'):
                tot[kk] += h.get(kk, 0) or 0
        print(' ', corto, len(e['hojas']), 'hojas', dict(tot), 'papel', {h['papel'] for h in e['hojas'].values()})
        print('    hojas:', [(n, h['rango'], h.get('tareas'), h.get('filas_tareas')) for n, h in e['hojas'].items()])
        print('    fx con texto fuera de CLAVES:', len(e['formulas_con_texto']), '· docprops:', e['docprops'])
    print('== parecido ==')
    for corto, pc in parecido.items():
        for rr_, v in pc.items():
            print('  %s vs %s tabs %d · fx idénticas %s · rótulos misma fila %s · por hoja %s' % (
                corto, rr_, len(v['pestanas']), v['formulas_identicas'], v['rotulos_misma_fila'],
                dict(v['formulas_por_hoja'])))
    print('== fórmulas sin gemela en ninguna ref ==', {k: v['n'] for k, v in distintas.items() if isinstance(v, dict)})
    print('== fórmulas WEDP distintas de PANP ==', len(distintas['WEDP_vs_PANP']))
    print('== fórmulas con texto con gemela', sum(1 for v in out['formulas_con_texto'].values() if v['gemelas']),
          'de', len(out['formulas_con_texto']))
    print('== calculadora ==', {h: (v['rango'], v['textos'], v['palabras'], v['formulas'], v['dv'], v['verdes'])
                                for h, v in hc.items()}, out['calculadora']['docprops'])
    for nombre in ('docx', 'contrato'):
        d = out[nombre]
        print('== %s ==' % nombre, {k: d[k] for k in ('parrafos', 'con_texto', 'estilos', 'palabras', 'tablas',
                                                      'imagenes', 'pagina_emu', 'core')})
        print('   secciones', d['secciones'])
        print('   € en texto', len(d['importes_eur']))
    print('   docx idénticos con', out['docx']['parrafos_identicos'])


if __name__ == '__main__':
    main()
