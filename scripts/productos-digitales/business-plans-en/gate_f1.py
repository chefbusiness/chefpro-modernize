#!/usr/bin/env python3
"""
gate_f1.py — Food Truck + Coffee Shop Business Plan Kit (EN) · gate de los cimientos (censo + mapas + docx).

Copia adaptada de `financial-kit/gate_f1.py`. Solo lee JSON y Markdown (corre en el Mac sin openpyxl). Sale con
código ≠ 0 salvo que:
  1. existan SPEC.md, F1-inventario-es.md, F1-research-us.md, censo_es.json, textos_es.json, docx_es_ft.json y
     docx_es_caf.json;
  2. SPEC §2.1 (6 ficheros: ES, EN y título) = mapas.LIBROS + mapas.DOCX; §2.2 (pestañas) = mapas.HOJAS_POR_LIBRO;
  3. decisiones D1..Dn sin huecos; ni TODO/TBD/XXX en SPEC ni inventario; D1-D3 con slugs, variables de Stripe,
     nombres y precio de mapas;
  4. la tabla §0 de F1-inventario-es.md (hojas, texto, fórmulas, fx→hoja, DV, CF, merges, verdes = desbloqueadas)
     y las cifras que cita la SPEC (722 / 742 fórmulas, 419 / 423 referencias, 68 / 75 tareas, tareas por fase D24,
     131 / 167 párrafos) sean las del censo;
  5. mapas.autotest() y mapas.cruzar_censo() den 0 errores (pestañas, claves, literales de fórmula cubiertos,
     CF que no cambian de color, PARCHES E2 que casan, VALORES_EN sobre celdas verdes con su rótulo, tokens);
  6. textos_es.json: GM, GFT y GCAF no vacíos; todo lo de GX es mapa/regenerar con su EN; ninguna cadena traducible
     sin `donde`; DV con max_len; cada FIJO existe en el ES y va a GX; mapa-clave ∈ CLAVES;
  7. E1: la celda del aviso (mapas.TEXTOS_NUEVOS) está vacía en el ES y justo debajo de la línea de versión;
  8. docx: nº de párrafos de la SPEC, 0 multi-run, 0 «sin-asignar», 4 tandas no vacías, tokens de DOCX_NOTAS válidos;
  9. el caso US reproduce el CAPEX de research §7 (FT ≈ $114,000; CAF ≈ $190,000; ±3 %) con VALORES_EN.

    python3 gate_f1.py
"""
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import mapas                                                     # noqa: E402

errores = []


def err(msg):
    errores.append(msg)


def seccion(texto, titulo):
    i = texto.find(titulo)
    if i < 0:
        return ''
    cands = [texto.find(m, i + len(titulo)) for m in ('\n### ', '\n## ')]
    fin = min([x for x in cands if x > 0] + [len(texto)])
    return texto[i:fin]


def filas_tabla(bloque):
    out = []
    for ln in bloque.splitlines():
        if ln.startswith('|') and not re.match(r'^\|[\s\-|]+\|$', ln):
            out.append([c.strip() for c in ln.strip().strip('|').split('|')])
    return out


def bts(celda):
    return re.findall(r'`([^`]+)`', celda)


def num(s):
    m = re.search(r'\d[\d.]*', s)
    return int(m.group(0).replace('.', '')) if m else None


def main():
    rutas = {n: os.path.join(AQUI, n) for n in ('SPEC.md', 'F1-inventario-es.md', 'F1-research-us.md', 'censo_es.json',
                                               'textos_es.json', 'docx_es_ft.json', 'docx_es_caf.json')}
    for n, p in rutas.items():
        if not os.path.exists(p):
            err('falta ' + n)
    if errores:
        return fin()
    spec = open(rutas['SPEC.md'], encoding='utf-8').read()
    inv = open(rutas['F1-inventario-es.md'], encoding='utf-8').read()
    censo = json.load(open(rutas['censo_es.json'], encoding='utf-8'))
    textos = json.load(open(rutas['textos_es.json'], encoding='utf-8'))
    dx = {p: json.load(open(rutas['docx_es_%s.json' % p], encoding='utf-8')) for p in mapas.PLANES}
    por_corto = {i['corto']: i for i in censo['libros'].values()}

    # 2. ficheros §2.1
    esperado = {}
    for c, (plan, fes, fen, tit) in mapas.LIBROS.items():
        esperado[fes] = (fen, tit)
    for plan, (fes, fen, tit) in mapas.DOCX.items():
        esperado[fes] = (fen, tit)
    vistos = set()
    for f in filas_tabla(seccion(spec, '### 2.1 Ficheros')):
        b = bts(f[1]) + bts(f[2]) if len(f) >= 4 else []
        if len(b) == 2:
            vistos.add(b[0])
            if b[0] not in esperado:
                err('SPEC §2.1: fichero ES desconocido para mapas: ' + b[0])
            elif esperado[b[0]] != (b[1], f[3]):
                err('SPEC §2.1 ≠ mapas: %s → %s / %r (mapas: %s)' % (b[0], b[1], f[3], esperado[b[0]]))
    for fes in esperado:
        if fes not in vistos:
            err('SPEC §2.1 no tiene el fichero ' + fes)
    # 2. pestañas §2.2
    pares = {}
    for f in filas_tabla(seccion(spec, '### 2.2 Pestañas')):
        for k in range(0, len(f) - 1, 2):
            es, en = bts(f[k]), bts(f[k + 1])
            if not es or not en:
                continue
            caf = re.search(r'\(CAF `([^`]+)`\)', f[k + 1])
            ambito = 'FT' if '(FT)' in f[k] else ('CAF' if '(CAF)' in f[k] else 'todos')
            pares[(ambito, es[0])] = en[0]
            if caf:
                pares[('CAF', es[0])] = caf.group(1)
                pares[('FT', es[0])] = en[0]
    for c, d in mapas.HOJAS_POR_LIBRO.items():
        amb = 'FT' if c.startswith('FT') else 'CAF'
        for es, en in d.items():
            sp = pares.get((amb, es)) or pares.get(('todos', es))
            if sp is None:
                err('SPEC §2.2 no tiene la pestaña %s / %s' % (c, es))
            elif sp != en:
                err('pestaña %s / %s: SPEC %r ≠ mapas %r' % (c, es, sp, en))

    # 3. decisiones, pendientes, D1-D3
    nums = [int(m.group(1)) for m in re.finditer(r'^\|\s*D(\d+)\s*\|', spec, re.M)]
    if not nums or sorted(nums) != list(range(1, max(nums) + 1)):
        err('decisiones D con huecos o duplicadas: %s' % sorted(nums))
    for nombre, t in (('SPEC.md', spec), ('F1-inventario-es.md', inv)):
        for m in re.finditer(r'\bTODO\b|XXX|\bTBD\b', t):
            err('%s: pendiente «%s»' % (nombre, m.group(0)))
    for p in mapas.PLANES.values():
        for d, aguja in (('D1', p['slug']), ('D1', p['env_stripe']), ('D2', p['producto']), ('D3', mapas.PRECIO)):
            if not re.search(r'\|\s*' + d + r'\s*\|[^\n]*' + re.escape(aguja), spec):
                err('%s no lleva «%s»' % (d, aguja))

    # 4. inventario §0 y cifras de la SPEC
    for f in filas_tabla(seccion(inv, '## 0. Totales')):
        m = re.search(r'`([^`]+\.xlsx)`', f[0])
        if not m:
            continue
        fes = m.group(1)
        info = censo['libros'].get(fes)
        if not info:
            err('inventario §0: %s no está en el censo' % fes)
            continue
        T = info['totales']
        cols = [('hojas', 1), ('celdas_texto', 2), ('celdas_formula', 3), ('formulas_con_hoja', 4), ('dv', 5),
                ('cf', 6), ('merges', 7), ('verdes', 8)]
        for k, j in cols:
            if num(f[j]) != T[k]:
                err('inventario §0 %s %s = %s; censo %s' % (fes, k, f[j], T[k]))
        if T['verdes'] != T['desbloqueadas']:
            err('%s: verdes %d ≠ desbloqueadas %d' % (fes, T['verdes'], T['desbloqueadas']))
    for aguja, valor in (('722 / 742', '%d / %d' % (por_corto['FTP']['totales']['celdas_formula'],
                                                    por_corto['CAFP']['totales']['celdas_formula'])),
                         ('419 / 423', '%d / %d' % (por_corto['FTP']['totales']['formulas_con_hoja'],
                                                    por_corto['CAFP']['totales']['formulas_con_hoja'])),
                         ('68 / 75', '%d / %d' % (por_corto['FTC']['totales']['tareas'],
                                                  por_corto['CAFC']['totales']['tareas'])),
                         ('131 / 167', '%d / %d' % (dx['ft']['meta']['n_parrafos'], dx['caf']['meta']['n_parrafos']))):
        if aguja not in spec:
            err('la SPEC ya no cita «%s»' % aguja)
        elif aguja != valor:
            err('la SPEC cita «%s» y el censo dice %s' % (aguja, valor))
    for c in ('FTC', 'CAFC'):
        real = [por_corto[c]['hojas_detalle'][h].get('tareas') for h in mapas.HOJAS_ES_POR_LIBRO[c][:6]]
        if real != mapas.TAREAS_POR_FASE[c]:
            err('tareas por fase %s: censo %s ≠ mapas %s' % (c, real, mapas.TAREAS_POR_FASE[c]))
        cita = '/'.join(str(x) for x in mapas.TAREAS_POR_FASE[c])
        if cita not in spec:
            err('D24 no cita %s' % cita)
        for h in mapas.HOJAS_ES_POR_LIBRO[c][:6]:
            hd = por_corto[c]['hojas_detalle'][h]
            if hd.get('tareas') != hd.get('tareas_con_texto'):
                err('%s / %s: filas de tarea sin texto' % (c, h))

    # 5. mapas
    for e in mapas.autotest() + mapas.cruzar_censo(rutas['censo_es.json']):
        err('mapas.py: ' + e)

    # 6. textos
    grupos = {g['id']: g for g in textos['meta']['grupos']}
    for g in ('GM', 'GFT', 'GCAF'):
        if not grupos.get(g, {}).get('n_cadenas'):
            err('grupo %s vacío' % g)
    trat_de = {}
    for e in textos['cadenas']:
        trat_de.setdefault(e['es'], set()).add(e['grupo'])
        if e['grupo'] == 'GX':
            if e['tratamiento'] in ('traducir', 'localizar'):
                err('%s traducible en GX' % e['id'])
            if e['tratamiento'] in ('mapa-hoja', 'mapa-clave') and not e.get('en_mapa'):
                err('%s (%s) sin en_mapa' % (e['id'], e['tratamiento']))
            if e['tratamiento'] == 'mapa-clave' and e['es'] not in mapas.CLAVES:
                err('%s mapa-clave fuera de CLAVES: %r' % (e['id'], e['es']))
        else:
            if not e.get('donde'):
                err('%s sin donde' % e['id'])
            if any(o['t'].startswith('dv-') for o in e['donde']) and 'max_len' not in e:
                err('%s: texto de DV sin max_len' % e['id'])
    for k in mapas.FIJOS:
        if k not in trat_de:
            err('FIJOS cita una cadena que no está en el ES: %r' % k[:60])
        elif trat_de[k] != {'GX'}:
            err('FIJOS %r va a %s' % (k[:50], trat_de[k]))

    # 7. E1
    for (c, h, celda), (t, estilo) in mapas.TEXTOS_NUEVOS.items():
        hd = por_corto[c]['hojas_detalle'][h]
        fila = int(celda[1:])
        if str(fila) in hd['etiquetas']:
            err('E1 %s: la celda %s no está vacía en el ES' % (c, celda))
        if not re.match(r'^Versi[óo]n 2\.2 · ', hd['etiquetas'].get(str(fila - 1), '')):
            err('E1 %s: la fila %d no es la línea de versión' % (c, fila - 1))

    # 8. docx
    for plan, d in dx.items():
        m = d['meta']
        if m['multi_run']:
            err('docx %s: %d párrafos con varios runs (F2-NOTAS §4)' % (plan, len(m['multi_run'])))
        if 'sin-asignar' in m['roles']:
            err('docx %s: párrafos sin asignar' % plan)
        for t, v in m['tandas'].items():
            if not v['parrafos']:
                err('docx %s: tanda %s vacía' % (plan, t))
        for i, nota in mapas.DOCX_NOTAS.get(plan, {}).items():
            for tok in mapas.RX_TOKEN.findall(nota):
                if tok not in mapas.tokens_de(plan):
                    err('DOCX_NOTAS %s[%d] cita un token inválido: %s' % (plan, i, tok))
            if not d['parrafos'][str(i)].get('traducir'):
                err('DOCX_NOTAS %s[%d] sobre un párrafo que no se traduce' % (plan, i))
        res = censo['tokens_docx'][plan]
        if set(res) != {t for t, v in mapas.tokens_de(plan).items() if v[1][0] == 'fila'}:
            err('tokens_docx %s incompleto' % plan)

    # 9. CAPEX del caso US (research §7: FT ≈ 114,000; CAF ≈ 190,000)
    for c, objetivo, filas_obra in (('FTP', 114000, [7, 8, 11, 12, 15]), ('CAFP', 190000, [9, 10, 11, 12, 24, 25])):
        v = {k[2]: val for k, (val, _r) in mapas.VALORES_EN.items() if k[0] == c and k[1] == '0. Supuestos'}
        partidas = sum(val for k, (val, _r) in mapas.VALORES_EN.items() if k[0] == c and k[1] == 'Inversión Inicial')
        renta = v['B24']
        meses_previos = 2 if c == 'FTP' else 1             # Supuestos!B54 del ES (se conserva)
        imprev = 0.08 if c == 'FTP' else 0.10              # Supuestos!B55 del ES (se conserva)
        obra = sum(mapas.VALORES_EN[(c, 'Inversión Inicial', 'B%d' % r)][0] for r in filas_obra)
        capex = partidas + renta * v['B25'] + renta * meses_previos + round(obra * imprev)
        if abs(capex - objetivo) / objetivo > 0.03:
            err('CAPEX del caso US %s = %s (research §7 ≈ %s)' % (c, capex, objetivo))
        print('gate_f1: CAPEX del caso US %s = %s (research §7 ≈ %s)' % (c, '{:,}'.format(capex), '{:,}'.format(objetivo)))

    g = {k: v['n_cadenas'] for k, v in grupos.items()}
    return fin(len(censo['libros']), sum(len(i['hojas']) for i in censo['libros'].values()), len(nums), g,
               dx['ft']['meta']['n_traducir'] + dx['caf']['meta']['n_traducir'])


def fin(*info):
    for e in errores:
        print('FALLO', e)
    if info:
        print('gate_f1: {} libros · {} pestañas · {} decisiones · grupos {} · {} párrafos docx traducibles'.format(*info))
    print('gate_f1: {}'.format('VERDE' if not errores else 'ROJO ({} fallos)'.format(len(errores))))
    return 1 if errores else 0


if __name__ == '__main__':
    sys.exit(main())
