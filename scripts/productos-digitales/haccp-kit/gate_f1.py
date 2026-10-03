#!/usr/bin/env python3
"""
gate_f1.py — HACCP Food Safety Kit Pro (EN) · gate de salida de la F1 (copia adaptada del inventario).

Sale con código ≠ 0 salvo que:
  1. `censo_es.json` exista y cada uno de sus 21 libros tenga fila en SPEC §2.1 (fichero ES y EN entre comillas
     invertidas) con el mismo fichero EN y título que `mapas.py`, y cada pestaña del censo tenga fila en §2.2
     (libro o «todos») con el mismo EN que `mapas.HOJAS` (≤ 31 caracteres, sin []:*?/\\).
  2. Toda decisión `| Dn |` tenga estado DECIDIDA o PROPUESTA [(ES)], numeración D1..Dn sin huecos ni duplicados.
  3. No quede TODO/TBD/XXX en SPEC.md ni en F1-inventario-es.md.
  4. D1-D3 lleven slug, nombre y precio de `mapas.py`.
  5. Las cifras del censo que cita la SPEC (hojas, fórmulas, fórmulas con hoja, DV, CF, merges, áreas, títulos,
     paneles, fechas, fechas de texto, verdes, patrones EN) sean las de `censo_es.json`, y los recuentos de grupos
     de §7 los de `textos_es.json`.
  6. La tabla §0 de F1-inventario-es.md sea exactamente la que genera el censo (`extraer_textos.tabla_md`).
  7. Cada fila de la tabla §3 (límites) tenga fuente, cada entrada de `mapas.LIMITES_F` y `LIMITES_02` también, y
     toda cifra NUEVA de `mapas.FORMULAS_EN` (respecto a su patrón ES) esté declarada en `LIMITES_F`.
     Cada celda de `mapas.POR_CELDA` existe en el ES y no va a un grupo de traducción.
  8. `mapas.autotest()` y `mapas.cruzar_censo()` den 0 errores.
  9. SPEC.md tenga ≤ 230 líneas.

    python3 gate_f1.py
"""
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import mapas                                                     # noqa: E402
import extraer_textos                                            # noqa: E402

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


def bt(celda):
    m = re.fullmatch(r'`([^`]+)`', celda)
    return m.group(1) if m else None


def numeros(s):
    return {float(x) for x in re.findall(r'(?<![\w$.])-?\d+(?:\.\d+)?', re.sub(r'"(?:[^"]|"")*"', '""', s))}


def main():
    p_spec = os.path.join(AQUI, 'SPEC.md')
    p_censo = os.path.join(AQUI, 'censo_es.json')
    p_textos = os.path.join(AQUI, 'textos_es.json')
    p_inv = os.path.join(AQUI, 'F1-inventario-es.md')
    for p in (p_spec, p_censo, p_textos, p_inv):
        if not os.path.exists(p):
            err('falta ' + os.path.basename(p))
    if errores:
        return fin()
    spec = open(p_spec, encoding='utf-8').read()
    inv = open(p_inv, encoding='utf-8').read()
    censo = json.load(open(p_censo, encoding='utf-8'))
    textos = json.load(open(p_textos, encoding='utf-8'))
    T = censo['totales']

    # 1. ficheros
    fich = {}
    for f in filas_tabla(seccion(spec, '### 2.1 Ficheros')):
        if len(f) >= 4 and bt(f[1]) and bt(f[2]):
            fich[bt(f[1])] = (bt(f[2]), f[3])
    for libro in censo['libros']:
        if libro not in fich:
            err('SPEC §2.1: falta el fichero ' + libro)
            continue
        en, titulo = fich[libro]
        if mapas.FICHEROS.get(libro) != en:
            err('fichero EN distinto de mapas.py: %s → %s (mapas: %s)' % (libro, en, mapas.FICHEROS.get(libro)))
        if mapas.TITULOS.get(en) != titulo:
            err('título distinto de mapas.TITULOS: %s → %r (mapas: %r)' % (en, titulo, mapas.TITULOS.get(en)))
    if len(set(v[0] for v in fich.values())) != len(fich):
        err('SPEC §2.1: ficheros EN duplicados')

    # 1. pestañas (filas de 3 o de 6 columnas: dos tríos por fila)
    hojas = {}
    for f in filas_tabla(seccion(spec, '### 2.2 Pestañas')):
        for k in range(0, len(f) - 2, 3):
            if bt(f[k + 1]) and bt(f[k + 2]):
                hojas[(f[k], bt(f[k + 1]))] = bt(f[k + 2])
    n_hojas = 0
    for libro, info in censo['libros'].items():
        c = info['corto']
        for h in info['hojas']:
            n_hojas += 1
            en = hojas.get((c, h)) or hojas.get(('todos', h))
            if not en:
                err('SPEC §2.2: falta la pestaña %s / %s' % (c, h))
                continue
            if len(en) > 31 or set(en) & mapas.HOJA_PROHIBIDOS:
                err('pestaña EN inválida: ' + en)
            if mapas.HOJAS.get(h) != en:
                err('pestaña EN distinta de mapas.py: %s → %s (mapas: %s)' % (h, en, mapas.HOJAS.get(h)))

    # 2. decisiones
    nums = []
    for ln in spec.splitlines():
        m = re.match(r'^\|\s*D(\d+)\s*\|', ln)
        if m:
            nums.append(int(m.group(1)))
            estado = ln.strip().strip('|').split('|')[-1].strip()
            if not re.fullmatch(r'(DECIDIDA|PROPUESTA)( \(ES\))?', estado):
                err('D%s sin estado DECIDIDA/PROPUESTA (%r)' % (m.group(1), estado))
    if not nums:
        err('no hay decisiones D en la SPEC')
    elif sorted(nums) != list(range(1, max(nums) + 1)):
        err('numeración de decisiones con huecos o duplicados: %s' % sorted(nums))

    # 3. pendientes
    for nombre, texto in (('SPEC.md', spec), ('F1-inventario-es.md', inv)):
        for m in re.finditer(r'\bTODO\b|XXX|\b[Tt][Bb][Dd]\b', texto):
            err('%s: pendiente «%s» en la posición %d' % (nombre, m.group(0), m.start()))

    # 4. nombre, slug, precio
    for d, aguja in (('D1', mapas.SLUG), ('D2', mapas.PRODUCTO), ('D3', '$19')):
        if not re.search(r'\|\s*' + d + r'\s*\|[^\n]*' + re.escape(aguja), spec):
            err('%s no lleva «%s»' % (d, aguja))
    if '/en/digital-products/' + mapas.SLUG not in spec:
        err('SPEC sin la URL /en/digital-products/' + mapas.SLUG)

    # 5. cifras del censo y de los grupos
    def miles(n):
        return '{:,}'.format(n).replace(',', '.')
    citas = [
        ('%d hojas' % T['hojas'], T['hojas'] == n_hojas),
        ('%s fórmulas' % miles(T['celdas_formula']), True),
        ('%d fórmulas con hoja' % T['formulas_con_hoja'], True),
        ('%d DV' % T['dv'], True), ('%d CF' % T['cf'], True), ('%d merges' % T['merges'], True),
        ('%d áreas' % T['areas_impresion'], True), ('%d títulos de impresión' % T['titulos_impresion'], True),
        ('%d paneles' % T['paneles'], True), ('%d fechas' % T['fechas'], True),
        ('%d fechas de texto' % T['fechas_texto'], True), ('%s verdes' % miles(T['verdes']), True),
        ('%d patrones' % len(mapas.FORMULAS_EN), True),
    ]
    for aguja, cond in citas:
        if aguja not in spec:
            err('SPEC no cita la cifra del censo «%s»' % aguja)
        if not cond:
            err('recuento de hojas incoherente')
    for g in textos['meta']['grupos']:
        if g['id'] != 'GM' and '**%s** %d' % (g['id'], g['n_cadenas']) not in spec:
            err('SPEC §7 no cita el grupo %s con %d cadenas' % (g['id'], g['n_cadenas']))
        if g['id'] == 'GM' and 'GM %d' % g['n_cadenas'] not in spec:
            err('SPEC §7 no cita GM %d' % g['n_cadenas'])
    if '%s cadenas' % miles(textos['meta']['n_cadenas']) not in spec:
        err('SPEC §7 no cita %s cadenas' % miles(textos['meta']['n_cadenas']))
    if T['graficos'] or T['imagenes'] or T['hojas_protegidas']:
        err('el censo tiene gráficos/imágenes/protección y la SPEC dice que no')

    # 6. tabla §0 del inventario = censo
    if extraer_textos.tabla_md(censo) not in inv:
        err('F1-inventario-es.md §0 no coincide con el censo (regenerar con extraer_textos.py --md)')

    # 7. límites con fuente
    for f in filas_tabla(seccion(spec, '## 3. Límites'))[1:]:
        if len(f) < 4 or not f[3]:
            err('SPEC §3: fila sin fuente: %r' % f[:1])
    for k, v in mapas.LIMITES_F.items():
        if not v[2]:
            err('LIMITES_F sin fuente: ' + k)
    for fam, mx, base in mapas.LIMITES_02:
        if not base:
            err('LIMITES_02 sin base: ' + fam)
    declarados = set()
    for v in mapas.LIMITES_F.values():
        declarados.update(float(x) for x in v[:2] if x is not None)
    auxiliares = {1.0, 3.0, 6.0}                         # MID/FIND/LEFT del 16 (lectura del rótulo)
    for es, en in mapas.FORMULAS_EN.items():
        nuevos = numeros(en) - numeros(es) - auxiliares
        if nuevos - declarados:
            err('FORMULAS_EN con cifras no declaradas en LIMITES_F %s: %s' % (sorted(nuevos - declarados), en[:80]))

    # 7b. cada celda de POR_CELDA / EJEMPLOS_NUM (texto) existe en el ES y sale de la traducción (regenerar)
    donde = {}
    for e in textos['cadenas']:
        for o in e['donde']:
            if o.get('t') == 'celda':
                donde[(o['f'], o['h'], o['c'])] = (e['es'], o['tr'])
    for k in mapas.POR_CELDA:
        if k not in donde:
            err('POR_CELDA cita una celda sin texto en el ES: %r' % (k,))
        elif donde[k][1] not in ('regenerar', 'localizar'):
            err('POR_CELDA %r está en un grupo de traducción (%s)' % (k, donde[k][1]))
    for k, v in mapas.EJEMPLOS_NUM.items():
        if isinstance(v, str) and not v.startswith('+') and k in donde and donde[k][1] != 'regenerar':
            err('EJEMPLOS_NUM %r (texto) no está marcado regenerar' % (k,))

    # 8. mapas
    for e in mapas.autotest() + mapas.cruzar_censo(p_censo):
        err('mapas.py: ' + e)

    # 9. longitud
    n = spec.count('\n') + 1
    if n > 230:
        err('SPEC.md tiene %d líneas (> 230)' % n)
    return fin(len(censo['libros']), n_hojas, len(nums), n)


def fin(*info):
    for e in errores:
        print('FALLO', e)
    if info:
        print('gate_f1: {} libros · {} pestañas en el censo · {} decisiones · SPEC {} líneas'.format(*info))
    print('gate_f1: {}'.format('VERDE' if not errores else 'ROJO ({} fallos)'.format(len(errores))))
    return 1 if errores else 0


if __name__ == '__main__':
    sys.exit(main())
