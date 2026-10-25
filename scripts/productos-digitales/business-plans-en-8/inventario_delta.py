#!/usr/bin/env python3
"""
inventario_delta.py — Pizza Shop Business Plan Kit (EN) · re-medición del paso 1c (sesión Claude Code, 25-oct-2026).
Clon de `../business-plans-en-3/inventario_delta.py` (Bar EN, F1) con: los 2 libros ES de la PIZZERÍA en la fuente de
`mapas_piz.FUENTE_ES` (variable PIZ_FUENTE_ES o, sin ella, `astro-site/public/dl/plan-negocio-pizzeria`), el docx ES si ya
existe, las referencias + el TAPAS BAR ES (BARP/BARC, la semilla) y el EN del BAR EN como primera fuente de reutilización
(GM, GR, GBAR-plan, GBAR-check de `../business-plans-en-3/`) antes de BP/BP2. Solo lectura; salida inventario_delta.json.

    PIZ_FUENTE_ES=… /root/venv-guias/bin/python inventario_delta.py [--repo DIR] [--salida inventario_delta.json]

Mide: clasificación de cadenas por la primera fuente con EN (BAR-* → GM → REST → CAF → PAN → FT → GX → PIZ), estructura,
parecido celda a celda con las referencias (el tapas bar ES es la gemela), fórmulas con texto con o sin gemela, caso ES
(Supuestos, inversión, fijos, personal, tokens) y docx (párrafos, encabezados, € en el texto). No traduce nada.
"""
import argparse
import collections
import json
import os
import re
import sys

import docx
import openpyxl
from openpyxl.utils import range_boundaries

AQUI = os.path.dirname(os.path.abspath(__file__))
BP = os.path.join(AQUI, '..', 'business-plans-en')
BP2 = os.path.join(AQUI, '..', 'business-plans-en-2')
BAR = os.path.join(AQUI, '..', 'business-plans-en-3')
FUENTE = os.environ.get('PIZ_FUENTE_ES') or 'plan-negocio-pizzeria'      # absoluta = dry-run; si no, dl/ del repo
sys.path.insert(0, BP)
os.environ.setdefault('BP_CONJUNTO', 'ftcaf')
import mapas                                                     # noqa: E402  (CLAVES, TOKENS_DOCX del molde FT/CAF)

DL = 'astro-site/public/dl'
LIBROS = collections.OrderedDict([
    ('PIZP', (FUENTE, 'plan-financiero-pizzeria.xlsx')),
    ('PIZC', (FUENTE, 'checklist-apertura-pizzeria.xlsx')),
])
DOCX_BAR = (FUENTE, 'plan-de-negocio-pizzeria.docx')
REF = collections.OrderedDict([          # libros ES de las tandas anteriores (estructura y fórmulas); el tapas bar, 1.º
    ('BARP', ('plan-negocio-tapas-bar', 'plan-financiero-tapas-bar.xlsx')),
    ('BARC', ('plan-negocio-tapas-bar', 'checklist-apertura-tapas-bar.xlsx')),
    ('FTP', ('plan-negocio-food-truck', 'plan-financiero-food-truck.xlsx')),
    ('CAFP', ('plan-negocio-cafeteria', 'plan-financiero-cafeteria-brunch.xlsx')),
    ('RESTP', ('plan-negocio-bar-restaurante', 'plan-financiero-bar-restaurante.xlsx')),
    ('PANP', ('plan-negocio-panaderia', 'plan-financiero-panaderia.xlsx')),
    ('FTC', ('plan-negocio-food-truck', 'checklist-apertura-food-truck.xlsx')),
    ('CAFC', ('plan-negocio-cafeteria', 'checklist-apertura-cafeteria-brunch.xlsx')),
    ('RESTC', ('plan-negocio-bar-restaurante', 'checklist-apertura-bar-restaurante.xlsx')),
    ('PANC', ('plan-negocio-panaderia', 'checklist-apertura-panaderia.xlsx')),
])
# fuentes de EN ya escrito: (carpeta, grupo) → etiqueta del inventario. Orden = prioridad de reutilización.
FUENTES = [
    (BAR, 'GM', 'BAR-GM'), (BAR, 'GR', 'BAR-GR'), (BAR, 'GBAR-plan', 'BAR'), (BAR, 'GBAR-check', 'BAR'),
    (BP, 'GM', 'GM'),
    (BP2, 'GREST', 'REST'), (BP2, 'GN', 'REST'),
    (BP, 'GCAF', 'CAF'),
    (BP2, 'GPAN', 'PAN'),
    (BP, 'GFT', 'FT'),
]
DOCX_REF = [(BP, 'ft'), (BP, 'caf'), (BP2, 'rest'), (BP2, 'pan'), (BAR, 'bar')]
VERDE = 'E8F5E9'
INVARIABLES = ('✓', '☐', 'OK', 'N/A', '—', 'AI Chef Pro', 'Break-even', 'DSCR', 'EBITDA', 'Marketing')
RX_LIT = re.compile(r'"((?:[^"]|"")*)"')
RX_LETRA = re.compile(r'[A-Za-zÁÉÍÓÚáéíóúÑñÜü]')
RX_PAL = re.compile(r"[A-Za-zÀ-ÿ0-9]+(?:[.,'’-][A-Za-zÀ-ÿ0-9]+)*")
RX_EUR = re.compile(r'(\d{1,3}(?:\.\d{3})+|\d+)(?:,\d+)?\s*(?:€|euros?\b|EUR\b|K\s*€|K\s*EUR)', re.I)
RX_HOJA_REF = re.compile(r"'([^']+)'!|\b([A-Za-zÁÉÍÓÚáéíóúñÑ0-9_.]+)!")
SIN_TILDE = ['Analisis', 'Captacion', 'Espana', 'Gastronomica', 'Consultoria', 'Ejecucion', 'Estrategico',
             'Organizacion', 'Informacion', 'Financiacion', 'Inversion', 'Operacion', 'Produccion', 'Indice',
             'Conclusion', 'Proposicion', 'Promocion', 'Gestion', 'Analisis', 'Tecnica', 'Ubicacion']


def norm_hoja(h):
    """Pestaña → nombre del molde FT/CAF (quita «N. » del molde numerado del restaurante)."""
    if h == '0. Supuestos':
        return h
    h = re.sub(r'^\d+\. ', '', h)
    return {'P&L 3 Años': 'PyG 3 Años'}.get(h, h)


def norm_formula(f):
    """Fórmula con los nombres de hoja normalizados (para comparar BAR con REST, que numera las pestañas)."""
    def rep(m):
        h = m.group(1) or m.group(2)
        n = norm_hoja(h)
        return "'%s'!" % n
    return RX_HOJA_REF.sub(rep, f or '')


def palabras(s):
    return len(RX_PAL.findall(s or ''))


def literales(f):
    return [m.group(1).replace('""', '"') for m in RX_LIT.finditer(f or '')]


def abrir(repo, d, f, data_only=False):
    return openpyxl.load_workbook(os.path.join(repo, DL, d, f), data_only=data_only)


def es_verde(c):
    rgb = c.fill.fgColor.rgb if c.fill is not None and c.fill.fgColor is not None else None
    return isinstance(rgb, str) and rgb[-6:].upper() == VERDE


# ------------------------------------------------------------------ diccionario de reutilización
def cargar_reuso():
    """es → [(etiqueta, grupo, id, en, por_celda, donde_origen)] con el EN ya escrito de BP y BP2."""
    reuso = collections.defaultdict(list)
    gx = set()
    for carpeta in (BAR, BP, BP2):
        tes = json.load(open(os.path.join(carpeta, 'textos_es.json')))
        en_por_grupo = {}
        for g in ('GM', 'GR', 'GBAR-plan', 'GBAR-check', 'GFT', 'GCAF', 'GN', 'GREST', 'GPAN'):
            p = os.path.join(carpeta, 'textos_en', g + '.json')
            if os.path.exists(p):
                en_por_grupo[g] = json.load(open(p))
            po = os.path.join(carpeta, 'textos_en', 'overrides_%s.json' % g)
            if os.path.exists(po):
                en_por_grupo['ov_' + g] = json.load(open(po))
        for c in tes['cadenas']:
            g = c['grupo']
            if g == 'GX':
                gx.add(c['es'])
                continue
            en = (en_por_grupo.get(g) or {}).get(c['id'])
            if en is None and c.get('reuso'):
                en = c['reuso'].get('en')
            if en is None:
                continue
            etiqueta = next((e for (cp, gg, e) in FUENTES if cp == carpeta and gg == g), None)
            if etiqueta is None:
                continue
            ov = (en_por_grupo.get('ov_' + g) or {}).get(c['id'])
            por_celda = bool(c.get('por_celda')) or ov is not None
            donde = ['%s %s!%s' % (d['f'], d['h'], d['c']) for d in c.get('donde', [])][:4]
            reuso[c['es']].append((etiqueta, g, c['id'], en, por_celda, donde))
    prio = {e: i for i, (_c, _g, e) in enumerate(FUENTES)}
    for k in reuso:
        reuso[k].sort(key=lambda x: prio[x[0]])
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
    c1, r1, c2, r2 = range_boundaries(rng)
    return range(r1, r2 + 1)


def mapa_formulas(wb):
    """(hoja normalizada, celda) → fórmula normalizada."""
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
    lits_fuera = collections.defaultdict(list)
    fx_texto = collections.OrderedDict()
    for ws in wb.worksheets:
        n_txt = n_fx = n_ref = verdes = desbl = 0
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
                    if '!' in str(v):
                        n_ref += 1
                    lt = [x for x in literales(str(v)) if RX_LETRA.search(x)]
                    fuera = [x for x in lt if x not in mapas.CLAVES]
                    for x in fuera:
                        lits_fuera[x].append('%s!%s' % (ws.title, c.coordinate))
                    if fuera:
                        fx_texto['%s!%s' % (ws.title, c.coordinate)] = str(v)
                elif isinstance(v, str):
                    n_txt += 1
        cf = sum(len(r) for r in ws.conditional_formatting._cf_rules.values())
        cf_rangos = sorted(str(k.sqref) for k in ws.conditional_formatting._cf_rules)
        dvs = [(dv.type, dv.formula1, str(dv.sqref)) for dv in ws.data_validations.dataValidation]
        h = collections.OrderedDict([
            ('rango', ws.dimensions), ('textos', n_txt), ('formulas', n_fx), ('fx_con_hoja', n_ref),
            ('dv', len(dvs)), ('dv_detalle', dvs), ('cf', cf), ('cf_rangos', cf_rangos),
            ('merges', len(ws.merged_cells.ranges)), ('merges_detalle', sorted(str(m) for m in ws.merged_cells.ranges)),
            ('verdes', verdes), ('verdes_desbloqueadas', desbl), ('papel', ws.page_setup.paperSize),
            ('protegida', bool(ws.protection.sheet)), ('password', bool(ws.protection.password)),
            ('paneles', ws.freeze_panes)])
        tareas = sorted({r for dv in ws.data_validations.dataValidation if (dv.formula1 or '').startswith('"✓')
                         for rng in str(dv.sqref).split() for r in _filas(rng)})
        if tareas:
            h['tareas'] = len(tareas)
            h['tareas_con_texto'] = sum(1 for r in tareas if isinstance(ws.cell(r, 2).value, str))
            h['dv_ok'] = sorted({dv.formula1 for dv in ws.data_validations.dataValidation
                                 if (dv.formula1 or '').startswith('"✓')})
        hojas[ws.title] = h
    return hojas, dict(lits_fuera), fx_texto


def rotulos(wb):
    out = {}
    for ws in wb.worksheets:
        out[norm_hoja(ws.title)] = [(c.row, c.value.strip()) for c in ws['A']
                                    if isinstance(c.value, str) and c.value.strip()]
    return out


def resolver_tokens(wb_v):
    """mapas.TOKENS_DOCX con el rótulo de la cafetería (molde de este libro) → (hoja, celda, valor ES)."""
    res, faltan = collections.OrderedDict(), []
    reales = {norm_hoja(n): n for n in wb_v.sheetnames}
    for tok, (fmt, fuente, _desc) in mapas.TOKENS_DOCX.items():
        if fuente[0] != 'fila':
            continue
        _, hoja, rot, col = fuente
        if isinstance(rot, dict):
            rot = rot.get('caf')
            if rot is None:
                continue                      # token propio del food truck
        if hoja not in reales:
            faltan.append(tok)
            continue
        ws = wb_v[reales[hoja]]
        fila = next((c.row for c in ws['A'] if isinstance(c.value, str) and c.value.strip() == rot), None)
        if fila is None:
            faltan.append(tok)
            continue
        res[tok] = (hoja, '%s%d' % (col, fila), ws['%s%d' % (col, fila)].value)
    return res, faltan


# ------------------------------------------------------------------ docx
def analizar_docx(repo, d, f):
    doc = docx.Document(os.path.join(repo, DL, d, f))
    ps = doc.paragraphs
    est = collections.Counter(p.style.name for p in ps)
    multi, rojos, pend, sin_tilde, eur = [], [], [], [], []
    secciones, sec, encab = collections.OrderedDict(), 0, []
    con_texto = 0
    for i, p in enumerate(ps):
        t = p.text
        if t.strip():
            con_texto += 1
        runs = list(p.runs)
        if len(runs) > 1 and len({(r.bold, r.italic, r.font.size) for r in runs}) > 1:
            multi.append(i)
        for r in runs:
            if r.font.color is not None and r.font.color.type is not None and str(r.font.color.rgb).upper() in (
                    'FF0000', 'C00000', 'E74C3C'):
                rojos.append(i)
                break
        tl = t.lower()
        if re.search(r'\bpendiente\b', tl) or '[contenido' in tl:
            pend.append(i)
        for w in SIN_TILDE:
            if re.search(r'\b%s\b' % w, t):
                sin_tilde.append((i, w))
        for mm in RX_EUR.finditer(t):
            eur.append((i, mm.group(0)))
        if p.style.name.startswith('Heading'):
            if p.style.name == 'Heading 1':
                sec += 1
            encab.append((i, p.style.name, t))
        secciones.setdefault(sec, [0, 0])
        secciones[sec][0] += 1 if t.strip() else 0
        secciones[sec][1] += palabras(t)
    s = doc.sections[0]
    return collections.OrderedDict([
        ('parrafos', len(ps)), ('con_texto', con_texto), ('estilos', dict(est)),
        ('palabras', sum(palabras(p.text) for p in ps)), ('multi_run_formato_distinto', multi),
        ('runs_rojos', rojos), ('pendiente', pend), ('sin_tilde', sin_tilde), ('importes_eur', eur),
        ('encabezados', encab), ('tablas', len(doc.tables)), ('imagenes', len(doc.inline_shapes)),
        ('secciones', {k: {'parrafos_texto': v[0], 'palabras': v[1]} for k, v in secciones.items()}),
        ('pagina_emu', [s.page_width, s.page_height]),
        ('core', {'title': doc.core_properties.title, 'author': doc.core_properties.author,
                  'subject': doc.core_properties.subject, 'keywords': doc.core_properties.keywords}),
        ('texto', {i: p.text for i, p in enumerate(ps) if p.text.strip()}),
    ])


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=os.path.abspath(os.path.join(AQUI, '..', '..', '..')))
    ap.add_argument('--salida', default=os.path.join(AQUI, 'inventario_delta.json'))
    a = ap.parse_args()

    reuso, gx_prev = cargar_reuso()
    tabs_conocidas = set()
    for d in mapas.HOJAS_POR_LIBRO.values():
        tabs_conocidas.update(d)

    out = collections.OrderedDict()
    occ, estr, rots, fx = collections.OrderedDict(), collections.OrderedDict(), {}, {}
    for corto, (d, f) in LIBROS.items():
        wb = abrir(a.repo, d, f)
        occ[corto] = ocurrencias(wb)
        hojas, lits, fxt = estructura(wb)
        p = wb.properties
        estr[corto] = {'hojas': hojas, 'literales_fuera_de_CLAVES': lits, 'formulas_con_texto': fxt,
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
            _h, _l, ref_fxt[corto] = estructura(wb)

    # ---- 1. clasificación de cadenas
    donde = collections.defaultdict(list)
    for corto, lst in occ.items():
        for t, w in lst:
            donde[t].append('%s:%s!%s' % (corto, w[0], w[1]))
    tabla = collections.OrderedDict()
    resumen = collections.defaultdict(collections.Counter)
    for t, ds in donde.items():
        revisar = False
        fuente = None
        if not RX_LETRA.search(t) or t in INVARIABLES:
            g = 'SIN-LETRAS'
        elif t in reuso:
            fuente = reuso[t][0]
            g = fuente[0]
            revisar = fuente[4]
        elif t in mapas.CLAVES or t in tabs_conocidas or t in gx_prev or any(':docProps!' in x for x in ds) \
                or any('!pestaña' in x for x in ds):
            g = 'GX'
        else:
            g = 'PIZ'
        libros = sorted({x.split(':')[0] for x in ds})
        tipo = 'check' if libros == ['PIZC'] else ('plan' if libros == ['PIZP'] else 'ambos')
        tabla[t] = collections.OrderedDict([
            ('grupo', g), ('tipo', tipo), ('palabras', palabras(t)), ('n', len(ds)), ('donde', ds[:6]),
            ('revisar', revisar)])
        if fuente:
            tabla[t]['reuso'] = {'de': fuente[1], 'id': fuente[2], 'en': fuente[3], 'origen': fuente[5],
                                 'otras_fuentes': [x[0] for x in reuso[t][1:]]}
        resumen['_cadenas'][g] += 1
        resumen['_palabras'][g] += palabras(t)
        resumen['_' + tipo][g] += 1
        if revisar:
            resumen['_revisar'][g] += 1
    out['clasificacion'] = {k: dict(v) for k, v in resumen.items()}
    out['cadenas'] = tabla

    # ---- 2. estructura y parecido con los libros de referencia
    out['estructura'] = estr
    parecido = collections.OrderedDict()
    for corto in LIBROS:
        refs = [r for r in REF if r[-1] == corto[-1]]
        pc = collections.OrderedDict()
        for r in refs:
            tabs_b = [norm_hoja(h) for h in rots[corto]]
            tabs_r = [norm_hoja(h) for h in rots[r]]
            mismas_tabs = [h for h in tabs_b if h in tabs_r]
            # fórmulas idénticas en la misma celda (hojas normalizadas)
            fb, fr = fx[corto], fx[r]
            ident = sum(1 for k, v in fb.items() if fr.get(k) == v)
            por_hoja = collections.OrderedDict()
            for h in dict.fromkeys(k[0] for k in fb):
                ks = [k for k in fb if k[0] == h]
                por_hoja[h] = '%d/%d' % (sum(1 for k in ks if fr.get(k) == fb[k]), len(ks))
            # rótulos col. A idénticos (texto y fila)
            rb = {(h, f_, x) for h, lst in rots[corto].items() for f_, x in lst}
            rr = {(h, f_, x) for h, lst in rots[r].items() for f_, x in lst}
            rot_txt_b = {(h, x) for h, _f, x in rb}
            rot_txt_r = {(h, x) for h, _f, x in rr}
            pc[r] = collections.OrderedDict([
                ('pestanas_comunes', '%d/%d' % (len(mismas_tabs), len(tabs_b))),
                ('formulas_identicas', '%d/%d' % (ident, len(fb))), ('formulas_por_hoja', por_hoja),
                ('rotulos_misma_fila', '%d/%d' % (len(rb & rr), len(rb))),
                ('rotulos_mismo_texto', '%d/%d' % (len(rot_txt_b & rot_txt_r), len(rot_txt_b)))])
        parecido[corto] = pc
    out['parecido'] = parecido

    # rótulos de la col. A del BAR que no tiene NINGÚN libro de referencia del mismo tipo (por hoja)
    nuevos_rot = collections.OrderedDict()
    for corto in LIBROS:
        refs = [r for r in REF if r[-1] == corto[-1]]
        dh = collections.OrderedDict()
        for hoja, lst in rots[corto].items():
            ref_set = set()
            for r in refs:
                for hh, l2 in rots[r].items():
                    if corto.endswith('C') or hh == hoja:
                        ref_set.update(x for _f, x in l2)
            nuevos = [(f_, x) for f_, x in lst if x not in ref_set]
            dh[hoja] = {'n_rotulos': len(lst), 'n_nuevos': len(nuevos), 'nuevos': nuevos}
        nuevos_rot[corto] = dh
    out['rotulos_nuevos'] = nuevos_rot

    # ---- 3. fórmulas con texto: ¿ya tienen gemela (mismos literales) en un libro de referencia?
    lits_ref = collections.defaultdict(list)
    for r, fxt in ref_fxt.items():
        for celda, f in fxt.items():
            lits_ref[tuple(literales(f))].append('%s!%s' % (r, celda))
    fxt_bar = collections.OrderedDict()
    for celda, f in estr['PIZP']['formulas_con_texto'].items():
        k = tuple(literales(f))
        fxt_bar[celda] = {'gemelas': lits_ref.get(k, [])[:4],
                          'literales_nuevos': [x for x in k if RX_LETRA.search(x) and x not in mapas.CLAVES and
                                               not any(x in kk for kk in lits_ref)]}
    out['formulas_con_texto'] = fxt_bar

    # fórmulas del BAR que no tiene ningún libro de referencia en la misma celda (posibles cambios de molde)
    distintas = collections.OrderedDict()
    for corto in LIBROS:
        refs = [r for r in REF if r[-1] == corto[-1]]
        lst = [('%s!%s' % k, v) for k, v in fx[corto].items() if not any(fx[r].get(k) == v for r in refs)]
        distintas[corto] = {'n': len(lst), 'muestra': lst[:60]}
    out['formulas_sin_gemela'] = distintas

    # ---- 4. caso ES
    wbv = abrir(a.repo, *LIBROS['PIZP'], data_only=True)
    wbf = abrir(a.repo, *LIBROS['PIZP'])
    ws, wsf = wbv['0. Supuestos'], wbf['0. Supuestos']
    out['supuestos_es'] = [(c.row, c.value, wsf.cell(c.row, 2).value, ws.cell(c.row, 2).value)
                           for c in ws['A'] if isinstance(c.value, str) and c.row > 2]
    res, faltan = resolver_tokens(wbv)
    out['tokens_docx'] = {'resueltos': len(res), 'faltan': faltan, 'valores': res}
    # inversión y fijos del P&L (rótulo + valor)
    for hoja in ('Inversión Inicial', 'PyG 3 Años', 'Personal'):
        wsv = wbv[hoja]
        out['filas_' + hoja] = [(c.row, c.value, wsv.cell(c.row, 2).value, wsv.cell(c.row, 3).value)
                                for c in wsv['A'] if isinstance(c.value, str)]

    # ---- 5. docx (el Word ES de la pizzería puede no existir aún: paso 1c)
    if not os.path.exists(os.path.join(a.repo, DL, *DOCX_BAR)):
        out['docx'] = 'pendiente: no existe %s' % os.path.join(a.repo, DL, *DOCX_BAR)
        with open(a.salida, 'w') as fh:
            json.dump(out, fh, ensure_ascii=False, indent=1, default=str)
        print('== docx ES: pendiente (aún no existe) ==')
        r = None
    else:
        r = analizar_docx(a.repo, *DOCX_BAR)
    if r is None:
        print('== clasificación ==', {k: dict(sorted(v.items())) for k, v in out['clasificacion'].items()})
        return
    
    ident = collections.Counter()
    for carpeta, plan in DOCX_REF:
        dj = json.load(open(os.path.join(carpeta, 'docx_es_%s.json' % plan)))
        txt = {x['texto'] for x in dj['parrafos'].values() if x['texto'].strip()}
        ident[plan] = sum(1 for t in r['texto'].values() if t in txt)
    r['parrafos_identicos'] = dict(ident)
    out['docx'] = r

    with open(a.salida, 'w') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1, default=str)

    # ---- resumen por pantalla
    print('== clasificación (cadenas únicas · palabras) ==')
    for k in ('_cadenas', '_palabras', '_plan', '_check', '_ambos', '_revisar'):
        print('  %-9s %s' % (k, dict(sorted(out['clasificacion'].get(k, {}).items()))))
    print('== estructura ==')
    for corto, e in estr.items():
        tot = collections.Counter()
        for h in e['hojas'].values():
            for kk in ('textos', 'formulas', 'fx_con_hoja', 'dv', 'cf', 'merges', 'verdes', 'verdes_desbloqueadas',
                       'tareas'):
                tot[kk] += h.get(kk, 0) or 0
        print(' ', corto, len(e['hojas']), 'hojas', dict(tot), 'papel', {h['papel'] for h in e['hojas'].values()},
              'protegidas sin pass', all(h['protegida'] and not h['password'] for h in e['hojas'].values()))
        print('    hojas:', [(n, h['rango'], h.get('tareas')) for n, h in e['hojas'].items()])
        print('    fx con texto fuera de CLAVES:', len(e['formulas_con_texto']))
        print('    docprops:', e['docprops'])
    print('== parecido con las referencias ==')
    for corto, pc in parecido.items():
        for rr_, v in pc.items():
            print('  %s vs %-5s tabs %s · fx idénticas %s · rótulos misma fila %s · mismo texto %s' % (
                corto, rr_, v['pestanas_comunes'], v['formulas_identicas'], v['rotulos_misma_fila'],
                v['rotulos_mismo_texto']))
    print('== fórmulas sin gemela en la misma celda ==', {k: v['n'] for k, v in distintas.items()})
    print('== fórmulas con texto: con gemela', sum(1 for v in fxt_bar.values() if v['gemelas']), 'de', len(fxt_bar))
    print('== rótulos nuevos ==')
    for corto, dh in nuevos_rot.items():
        print(' ', corto, {h: (x['n_rotulos'], x['n_nuevos']) for h, x in dh.items()})
    print('== tokens docx: resueltos', len(res), 'faltan', faltan)
    print('== docx ==', {k: r[k] for k in ('parrafos', 'con_texto', 'estilos', 'palabras', 'tablas', 'imagenes',
                                         'pagina_emu', 'parrafos_identicos')})
    print('   encabezados', [(i, t[:40]) for i, _s, t in r['encabezados']])
    print('   secciones', r['secciones'])
    print('   pendiente', r['pendiente'], 'rojos', r['runs_rojos'], 'sin tilde', r['sin_tilde'][:12])
    print('   € en texto', r['importes_eur'][:50])


if __name__ == '__main__':
    main()
