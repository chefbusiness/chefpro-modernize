#!/usr/bin/env python3
"""
inventario_delta.py — Restaurant + Bakery Business Plan Kit (EN) · F1 (sesión Claude Code, 4-oct-2026).

Inventario DELTA de los 6 ficheros ES PUBLICADOS de `plan-negocio-bar-restaurante` y `plan-negocio-panaderia`
frente a lo que ya existe para food truck / cafetería en `../business-plans-en/` (SOLO LECTURA):

  · cada cadena de texto (celdas, DV, pestañas, pie, docProps) se clasifica contra `textos_es.json` de FT/CAF:
      GM          ya está en el grupo común (traducido en textos_en/GM.json)
      GFT/GCAF    idéntica a una cadena propia de FT o CAF → su EN se reutiliza (revisar si el contexto cambia)
      GX          no se traduce (pestaña, clave, fijo, versión, pie, docProps)
      GN          nueva y COMÚN a restaurante y panadería
      GREST/GPAN  nueva y propia de uno
  · estructura por libro (hojas, rangos, fórmulas, DV, CF, merges, verdes, papel, tareas por fase) y diferencias
    de rótulos de la col. A frente a FT y CAF hoja a hoja;
  · fórmulas con literales de texto (candidatas a FORMULAS_EN) y literales fuera de mapas.CLAVES;
  · resolución de mapas.TOKENS_DOCX en los dos planes (con valor ES en caché);
  · docx: párrafos, runs, estilos, secciones con palabras, defectos (pendiente, rojo, inglés, sin tildes, € del
    texto frente a la caché del Excel).

    python3 inventario_delta.py [--repo DIR] [--salida inventario_delta.json]

No traduce nada. Térmica: un proceso, en serie, 8 libros + 2 docx, < 15 s. Correr en el VPS (D27).
"""
import argparse
import collections
import json
import os
import re
import sys

import docx
import openpyxl
from openpyxl.utils import get_column_letter

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(AQUI, '..', 'business-plans-en')
sys.path.insert(0, BASE)
import mapas                                                     # noqa: E402

LIBROS = collections.OrderedDict([
    ('RESTP', ('rest', 'plan-negocio-bar-restaurante', 'plan-financiero-bar-restaurante.xlsx')),
    ('RESTC', ('rest', 'plan-negocio-bar-restaurante', 'checklist-apertura-bar-restaurante.xlsx')),
    ('PANP', ('pan', 'plan-negocio-panaderia', 'plan-financiero-panaderia.xlsx')),
    ('PANC', ('pan', 'plan-negocio-panaderia', 'checklist-apertura-panaderia.xlsx')),
])
REF = collections.OrderedDict([
    ('FTP', ('plan-negocio-food-truck', 'plan-financiero-food-truck.xlsx')),
    ('CAFP', ('plan-negocio-cafeteria', 'plan-financiero-cafeteria-brunch.xlsx')),
    ('FTC', ('plan-negocio-food-truck', 'checklist-apertura-food-truck.xlsx')),
    ('CAFC', ('plan-negocio-cafeteria', 'checklist-apertura-cafeteria-brunch.xlsx')),
])
DOCX = collections.OrderedDict([
    ('rest', ('plan-negocio-bar-restaurante', 'plan-de-negocio-bar-restaurante.docx')),
    ('pan', ('plan-negocio-panaderia', 'plan-de-negocio-panaderia.docx')),
])
VERDE = 'E8F5E9'
RX_LIT = re.compile(r'"((?:[^"]|"")*)"')
RX_LETRA = re.compile(r'[A-Za-zÁÉÍÓÚáéíóúÑñÜü]')
RX_PAL = re.compile(r"[A-Za-zÀ-ÿ0-9]+(?:[.,'’-][A-Za-zÀ-ÿ0-9]+)*")
RX_EUR = re.compile(r'(\d{1,3}(?:\.\d{3})+|\d+)(?:,\d+)?\s*(?:€|euros?\b|EUR\b)', re.I)
RX_INGLES = re.compile(r'\b(?:the|and|with|which|ranging|from|of the|gap|fill|cash flow|break-even|'
                       r'flujosconstants|affluencia|determinantepara|brutoss|recuperase|fixa|spectacles)\b', re.I)
SIN_TILDE = ['Analisis', 'Captacion', 'Espana', 'Gastronomica', 'Consultoria', 'Ejecucion', 'Estrategico',
             'Organizacion', 'Informacion', 'Financiacion', 'Inversion', 'Operacion', 'Produccion', 'Panaderia',
             'Indice', 'Conclusion', 'Proposicion', 'Promocion', 'Gestion']


def norm_hoja(h):
    """Pestaña del molde v2.0 del bar-restaurante («1. Inversión Inicial», «2. P&L 3 Años») → nombre FT/CAF."""
    if h == '0. Supuestos':
        return h
    h = re.sub(r'^\d+\. ', '', h)
    return {'P&L 3 Años': 'PyG 3 Años'}.get(h, h)


def palabras(s):
    return len(RX_PAL.findall(s or ''))


def literales(f):
    return [m.group(1).replace('""', '"') for m in RX_LIT.finditer(f or '')]


def abrir(repo, d, f, data_only=False):
    return openpyxl.load_workbook(os.path.join(repo, 'astro-site/public/dl', d, f), data_only=data_only)


def ocurrencias(wb):
    """(texto, dónde) de todo lo traducible del libro, como extraer_textos.py (sin clasificar)."""
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
    return out


def estructura(wb, corto):
    hojas = collections.OrderedDict()
    lits_fuera = collections.defaultdict(list)
    fx_texto = []
    for ws in wb.worksheets:
        n_txt = n_fx = n_ref = 0
        verdes = desbl = 0
        for row in ws.iter_rows():
            for c in row:
                v = c.value
                rgb = c.fill.fgColor.rgb if c.fill is not None and c.fill.fgColor is not None else None
                if isinstance(rgb, str) and rgb[-6:].upper() == VERDE:      # también verdes vacías (RESTC col. E)
                    verdes += 1
                    if c.protection is not None and c.protection.locked is False:
                        desbl += 1
                if v is None:
                    continue
                if c.data_type == 'f' or (isinstance(v, str) and v.startswith('=')):
                    n_fx += 1
                    if '!' in v:
                        n_ref += 1
                    lt = [x for x in literales(v) if RX_LETRA.search(x)]
                    fuera = [x for x in lt if x not in mapas.CLAVES]
                    for x in fuera:
                        lits_fuera[x].append('%s!%s' % (ws.title, c.coordinate))
                    if fuera:
                        fx_texto.append('%s!%s' % (ws.title, c.coordinate))
                elif isinstance(v, str):
                    n_txt += 1
        cf = sum(len(r) for r in ws.conditional_formatting._cf_rules.values())
        h = collections.OrderedDict([
            ('rango', ws.dimensions), ('textos', n_txt), ('formulas', n_fx), ('fx_con_hoja', n_ref),
            ('dv', len(ws.data_validations.dataValidation)), ('cf', cf), ('merges', len(ws.merged_cells.ranges)),
            ('verdes', verdes), ('verdes_desbloqueadas', desbl), ('papel', ws.page_setup.paperSize),
            ('protegida', bool(ws.protection.sheet)), ('password', bool(ws.protection.password)),
            ('paneles', ws.freeze_panes)])
        tareas = sorted({r for dv in ws.data_validations.dataValidation if (dv.formula1 or '').startswith('"✓')
                         for rng in str(dv.sqref).split() for r in _filas(rng)})
        if tareas:
            h['tareas'] = len(tareas)
            h['tareas_con_texto'] = sum(1 for r in tareas if isinstance(ws.cell(r, 2).value, str))
        hojas[ws.title] = h
    return hojas, dict(lits_fuera), fx_texto


def _filas(rng):
    from openpyxl.utils import range_boundaries
    c1, r1, c2, r2 = range_boundaries(rng)
    return range(r1, r2 + 1)


def rotulos(wb):
    """hoja → [(fila, rótulo col. A)] para comparar estructura."""
    out = {}
    for ws in wb.worksheets:
        out[norm_hoja(ws.title)] = [(c.row, c.value.strip()) for c in ws['A'] if isinstance(c.value, str) and c.value.strip()]
    return out


def resolver_tokens(wb_v, plan):
    """mapas.TOKENS_DOCX → (hoja, celda, valor ES) en este plan; deriv aparte."""
    res, faltan = collections.OrderedDict(), []
    for tok, (fmt, fuente, _desc) in mapas.TOKENS_DOCX.items():
        if fuente[0] != 'fila':
            continue
        _, hoja, rot, col = fuente
        if isinstance(rot, dict):                  # rótulo por plan: el de la cafetería es el del motor común
            rot = rot.get(plan) or rot.get('caf')
            if rot is None:
                continue                           # token propio de FT (vehículo, generador…): no aplica
        sust = {'rest': ('Clientes', 'Cubiertos'), 'pan': ('Clientes', 'Transacciones')}[plan]
        reales = {norm_hoja(n): n for n in wb_v.sheetnames}
        if hoja not in reales:
            faltan.append(tok)
            continue
        ws = wb_v[reales[hoja]]
        fila = next((c.row for c in ws['A'] if isinstance(c.value, str) and c.value.strip() in
                     (rot, rot.replace(*sust))), None)
        if fila is None:
            faltan.append(tok)
            continue
        res[tok] = (hoja, '%s%d' % (col, fila), ws['%s%d' % (col, fila)].value)
    return res, faltan


def analizar_docx(repo, d, f):
    doc = docx.Document(os.path.join(repo, 'astro-site/public/dl', d, f))
    ps = doc.paragraphs
    est = collections.Counter(p.style.name for p in ps)
    multi, rojos, pend, ingles, sin_tilde, eur = [], [], [], [], [], []
    secciones, sec, encab = collections.OrderedDict(), 0, []
    con_texto = 0
    for i, p in enumerate(ps):
        t = p.text
        if t.strip():
            con_texto += 1
        runs = [r for r in p.runs]
        if len(runs) > 1 and len({(r.bold, r.italic, r.font.size, str(r.font.color.rgb if r.font.color and
                                    r.font.color.type else None)) for r in runs}) > 1:
            multi.append(i)
        for r in runs:
            if r.font.color is not None and r.font.color.type is not None and str(r.font.color.rgb).upper() in (
                    'FF0000', 'C00000', 'E74C3C'):
                rojos.append(i)
                break
        if 'pendiente' in t.lower() or '[contenido' in t.lower():
            pend.append(i)
        m = RX_INGLES.findall(t)
        if m and p.style.name != 'Heading 1':
            ingles.append((i, sorted(set(x.lower() for x in m))[:6]))
        for w in SIN_TILDE:
            if re.search(r'\b%s\b' % w, t):
                sin_tilde.append((i, w))
        for mm in RX_EUR.finditer(t):
            eur.append((i, mm.group(0)))
        if p.style.name == 'Heading 1':
            sec += 1
            encab.append((i, t))
        secciones.setdefault(sec, [0, 0])
        secciones[sec][0] += 1 if t.strip() else 0
        secciones[sec][1] += palabras(t)
    s = doc.sections[0]
    return collections.OrderedDict([
        ('parrafos', len(ps)), ('con_texto', con_texto), ('estilos', dict(est)),
        ('palabras', sum(palabras(p.text) for p in ps)), ('multi_run_formato_distinto', multi),
        ('runs_rojos', rojos), ('pendiente', pend), ('ingles_sospechoso', ingles[:40]),
        ('sin_tilde', sin_tilde[:40]), ('importes_eur', eur), ('encabezados', encab),
        ('secciones', {k: {'parrafos_texto': v[0], 'palabras': v[1]} for k, v in secciones.items()}),
        ('tablas', len(doc.tables)), ('imagenes', len(doc.inline_shapes)),
        ('pagina_emu', [s.page_width, s.page_height]),
        ('core', {'title': doc.core_properties.title, 'author': doc.core_properties.author,
                  'subject': doc.core_properties.subject}),
        ('texto', {i: p.text for i, p in enumerate(ps) if p.text.strip()}),
    ])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=os.path.abspath(os.path.join(AQUI, '..', '..', '..')))
    ap.add_argument('--salida', default=os.path.join(AQUI, 'inventario_delta.json'))
    a = ap.parse_args()

    base = json.load(open(os.path.join(BASE, 'textos_es.json')))
    grupo_de = {c['es']: c['grupo'] for c in base['cadenas']}
    # textos de los docx FT/CAF (para medir párrafos idénticos)
    docx_base = set()
    for p in ('ft', 'caf'):
        dj = json.load(open(os.path.join(BASE, 'docx_es_%s.json' % p)))
        docx_base.update(x['texto'] for x in dj['parrafos'].values() if x['texto'].strip())

    out = collections.OrderedDict()
    occ = collections.OrderedDict()
    estr = collections.OrderedDict()
    rots = {}
    for corto, (plan, d, f) in LIBROS.items():
        wb = abrir(a.repo, d, f)
        occ[corto] = ocurrencias(wb)
        hojas, lits, fxt = estructura(wb, corto)
        props = wb.properties
        estr[corto] = {'hojas': hojas, 'literales_fuera_de_CLAVES': lits, 'formulas_con_texto': fxt,
                       'docprops': {'title': props.title, 'subject': props.subject, 'creator': props.creator,
                                    'keywords': props.keywords, 'description': props.description}}
        rots[corto] = rotulos(wb)
    for corto, (d, f) in REF.items():
        rots[corto] = rotulos(abrir(a.repo, d, f))

    # ---- clasificación de cadenas
    planes_de = collections.defaultdict(set)
    donde = collections.defaultdict(list)
    for corto, lst in occ.items():
        for t, w in lst:
            planes_de[t].add(LIBROS[corto][0])
            donde[t].append('%s:%s!%s' % (corto, w[0], w[1]))
    tabla = collections.OrderedDict()
    resumen = collections.defaultdict(lambda: collections.Counter())
    for t in planes_de:
        if not RX_LETRA.search(t) or t in ('✓', '☐', 'OK', 'N/A', 'AI Chef Pro'):
            g = 'SIN-LETRAS'
        elif t in grupo_de:
            g = grupo_de[t]
        elif t in mapas.CLAVES:
            g = 'GX'
        elif planes_de[t] == {'rest', 'pan'}:
            g = 'GN'
        else:
            g = 'GREST' if 'rest' in planes_de[t] else 'GPAN'
        tipo = 'check' if all(':' in x and x.split(':')[0].endswith('C') for x in donde[t]) else (
            'plan' if all(x.split(':')[0].endswith('P') for x in donde[t]) else 'ambos')
        tabla[t] = {'grupo': g, 'planes': sorted(planes_de[t]), 'tipo': tipo, 'palabras': palabras(t),
                    'n': len(donde[t]), 'donde': donde[t][:6]}
        for p in planes_de[t]:
            resumen[p][g] += 1
        resumen['_palabras'][g] += palabras(t)
        resumen['_cadenas'][g] += 1
        resumen['_' + tipo][g] += 1
    out['clasificacion'] = {k: dict(v) for k, v in resumen.items()}
    out['cadenas'] = tabla
    out['estructura'] = estr

    # ---- rótulos de la col. A: nuevos y ausentes frente a FT y CAF
    difs = collections.OrderedDict()
    for corto in LIBROS:
        refs = ('FTP', 'CAFP') if corto.endswith('P') else ('FTC', 'CAFC')
        dh = collections.OrderedDict()
        for hoja, lst in rots[corto].items():
            ref_set = set()
            for r in refs:
                ref_set.update(x[1] for x in rots[r].get(hoja, []))
            nuevos = [(f, x) for f, x in lst if x not in ref_set]
            mios = {x for _, x in lst}
            ausentes_ft = [x for _, x in rots[refs[0]].get(hoja, []) if x not in mios]
            ausentes_caf = [x for _, x in rots[refs[1]].get(hoja, []) if x not in mios]
            dh[hoja] = {'n_rotulos': len(lst), 'nuevos': nuevos[:80], 'n_nuevos': len(nuevos),
                        'ausentes_vs_FT': len(ausentes_ft), 'ausentes_vs_CAF': len(ausentes_caf)}
        difs[corto] = dh
    out['rotulos_delta'] = difs

    # ---- tokens del docx y valores del caso ES
    tok = collections.OrderedDict()
    caso = collections.OrderedDict()
    for corto in ('RESTP', 'PANP'):
        plan, d, f = LIBROS[corto]
        wbv = abrir(a.repo, d, f, data_only=True)
        res, faltan = resolver_tokens(wbv, plan)
        tok[plan] = {'resueltos': len(res), 'faltan': faltan, 'valores': {k: v for k, v in res.items()}}
        ws = wbv['0. Supuestos']
        caso[plan] = [(c.row, c.value, ws.cell(c.row, 2).value) for c in ws['A']
                      if isinstance(c.value, str) and c.row > 2]
    out['tokens_docx'] = tok
    out['supuestos_es'] = caso

    # ---- docx
    dd = collections.OrderedDict()
    for plan, (d, f) in DOCX.items():
        r = analizar_docx(a.repo, d, f)
        r['parrafos_identicos_a_ft_caf'] = sum(1 for t in r['texto'].values() if t in docx_base)
        dd[plan] = r
    out['docx'] = dd

    with open(a.salida, 'w') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1, default=str)

    # ---- resumen
    print('== clasificación (cadenas únicas) ==')
    for k, v in out['clasificacion'].items():
        print(' ', k, dict(sorted(v.items())))
    print('== estructura ==')
    for corto, e in estr.items():
        tot = collections.Counter()
        for h in e['hojas'].values():
            for kk in ('textos', 'formulas', 'fx_con_hoja', 'dv', 'cf', 'merges', 'verdes', 'verdes_desbloqueadas',
                       'tareas'):
                tot[kk] += h.get(kk, 0) or 0
        print(' ', corto, len(e['hojas']), 'hojas', dict(tot), 'papel', {h['papel'] for h in e['hojas'].values()},
              'sin pass', all(h['protegida'] and not h['password'] for h in e['hojas'].values()))
        print('    hojas:', [(n, h['rango'], h.get('tareas')) for n, h in e['hojas'].items()])
        print('    fx con texto fuera de CLAVES:', len(e['formulas_con_texto']), 'literales:', len(e['literales_fuera_de_CLAVES']))
        print('    docprops:', e['docprops'])
    print('== rótulos nuevos frente a FT+CAF ==')
    for corto, dh in difs.items():
        print(' ', corto, {h: (x['n_rotulos'], x['n_nuevos']) for h, x in dh.items()})
    print('== tokens docx ==')
    for p, t in tok.items():
        print(' ', p, 'resueltos', t['resueltos'], 'faltan', t['faltan'])
    print('== docx ==')
    for p, r in dd.items():
        print(' ', p, {k: r[k] for k in ('parrafos', 'con_texto', 'estilos', 'palabras', 'tablas', 'imagenes',
                                       'pagina_emu', 'parrafos_identicos_a_ft_caf')})
        print('    multi-run≠', r['multi_run_formato_distinto'], 'rojos', r['runs_rojos'], 'pendiente', r['pendiente'])
        print('    encabezados', r['encabezados'])
        print('    secciones', r['secciones'])
        print('    sin tilde', r['sin_tilde'][:15])
        print('    inglés?', r['ingles_sospechoso'][:15])
        print('    € en texto', r['importes_eur'][:40])
        print('    core', r['core'])


if __name__ == '__main__':
    main()
