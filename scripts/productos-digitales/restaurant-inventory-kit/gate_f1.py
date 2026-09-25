#!/usr/bin/env python3
"""
gate_f1.py — Restaurant Inventory Kit Pro (EN) · gate de salida de la F1.

Sale con código ≠ 0 salvo que:
  1. `censo_es.json` exista y cada uno de sus 9 libros tenga fila en la tabla de ficheros de SPEC §2.1
     (fichero ES y fichero EN entre comillas invertidas) y cada pestaña de cada libro tenga fila en §2.2
     (libro o «todos», pestaña ES, pestaña EN ≤ 31 caracteres y sin []:*?/\\).
  2. Los nombres EN de la SPEC coincidan con los de `mapas.py` (FICHEROS, HOJAS) y los títulos con TITULOS.
  3. Toda decisión `| Dn |` tenga estado DECIDIDA o PROPUESTA, numeración D1..Dn sin huecos ni duplicados.
  4. No quede TODO/TBD/XXX en SPEC.md (ni en F1-inventario-es.md).
  5. Estén el nombre, el slug y el precio (D1-D3) y coincidan con `mapas.py`.
  6. Las cifras de censo que cita la SPEC (hojas, fórmulas con hoja, DV, CF, merges, áreas, fechas, verdes)
     sean las de `censo_es.json`.
  7. `mapas.autotest()` y `mapas.cruzar_censo()` den 0 errores.
  8. SPEC.md tenga ≤ 300 líneas.

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


def corto(fichero):
    m = re.match(r'^(BONUS-)?(\d+)', fichero)
    return ('B' if m.group(1) else '') + m.group(2)


def seccion(texto, titulo):
    i = texto.find(titulo)
    if i < 0:
        return ''
    j = texto.find('\n### ', i + len(titulo))
    k = texto.find('\n## ', i + len(titulo))
    fin = min(x for x in (j, k, len(texto)) if x > 0)
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


def main():
    p_spec = os.path.join(AQUI, 'SPEC.md')
    p_censo = os.path.join(AQUI, 'censo_es.json')
    p_inv = os.path.join(AQUI, 'F1-inventario-es.md')
    for p in (p_spec, p_censo, p_inv):
        if not os.path.exists(p):
            err('falta ' + os.path.basename(p))
    if errores:
        return fin()
    spec = open(p_spec, encoding='utf-8').read()
    censo = json.load(open(p_censo, encoding='utf-8'))

    # 1-2. ficheros
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
        if not en.endswith('.xlsx') or en == libro:
            err('fichero EN inválido: ' + en)
    if len(set(v[0] for v in fich.values())) != len(fich):
        err('SPEC §2.1: ficheros EN duplicados')

    # 1-2. pestañas
    hojas = {}
    for f in filas_tabla(seccion(spec, '### 2.2 Pestañas')):
        if len(f) >= 3 and bt(f[1]) and bt(f[2]):
            hojas[(f[0], bt(f[1]))] = bt(f[2])
    n_hojas = 0
    for libro, info in censo['libros'].items():
        c = corto(libro)
        ens = []
        for h in info['hojas']:
            n_hojas += 1
            en = hojas.get((c, h)) or hojas.get(('todos', h))
            if not en:
                err('SPEC §2.2: falta la pestaña %s / %s' % (c, h))
                continue
            ens.append(en)
            if len(en) > 31 or set(en) & mapas.HOJA_PROHIBIDOS:
                err('pestaña EN inválida: ' + en)
            if mapas.HOJAS.get(h) != en:
                err('pestaña EN distinta de mapas.py: %s → %s (mapas: %s)' % (h, en, mapas.HOJAS.get(h)))
        if len(set(ens)) != len(ens):
            err('pestañas EN duplicadas en ' + libro)

    # 3. decisiones
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
    elif sorted(nums) != list(range(1, max(nums) + 1)) or len(nums) != len(set(nums)):
        err('numeración de decisiones con huecos o duplicados: %s' % sorted(nums))

    # 4. pendientes
    for nombre, texto in (('SPEC.md', spec), ('F1-inventario-es.md', open(p_inv, encoding='utf-8').read())):
        # TODO/XXX en mayúsculas («todo» es palabra española); TBD en cualquier caja
        for m in re.finditer(r'\bTODO\b|XXX|\b[Tt][Bb][Dd]\b', texto):
            err('%s: pendiente «%s» en la posición %d' % (nombre, m.group(0), m.start()))

    # 5. nombre, slug, precio
    for aguja in (mapas.PRODUCTO, mapas.SLUG, '$19', '/en/digital-products/' + mapas.SLUG):
        if aguja not in spec:
            err('SPEC: falta «%s»' % aguja)
    if not re.search(r'\|\s*D2\s*\|[^\n]*' + re.escape(mapas.PRODUCTO), spec):
        err('D2 no lleva el nombre ' + mapas.PRODUCTO)
    if not re.search(r'\|\s*D1\s*\|[^\n]*' + re.escape(mapas.SLUG), spec):
        err('D1 no lleva el slug ' + mapas.SLUG)
    if not re.search(r'\|\s*D3\s*\|[^\n]*\$19', spec):
        err('D3 no lleva el precio $19')

    # 6. cifras del censo citadas
    T = censo['totales']
    esperadas = [
        ('%d hojas' % T['hojas'], T['hojas'] == n_hojas),
        ('%d fórmulas con referencia a hoja' % T['formulas_con_hoja'], True),
        ('DV\n  (%d' % T['dv'], None), ('(%d, mismos sqref' % T['dv'], True),
        ('CF (%d' % T['cf'], True), ('%d merges' % T['merges'], True),
        ('%d áreas' % T['areas_impresion'], True), ('%d títulos de impresión' % T['titulos_impresion'], True),
        ('%d fechas' % T['fechas'], True),
        ('{:,}'.format(T['verdes']).replace(',', '.'), True),
        ('%d hojas que la llevan' % T['hojas_dv_unidades'], True),
    ]
    for aguja, cond in esperadas:
        if cond is None:
            continue
        if aguja not in spec:
            err('SPEC no cita la cifra del censo «%s»' % aguja.replace('\n', ' '))
        if cond is False:
            err('recuento de hojas incoherente')
    if T['graficos'] != 0 or T['imagenes'] != 0:
        err('el censo tiene gráficos/imágenes y la SPEC dice 0')

    # 7. mapas
    for e in mapas.autotest() + mapas.cruzar_censo(p_censo):
        err('mapas.py: ' + e)

    # 8. longitud
    n = spec.count('\n') + 1
    if n > 300:
        err('SPEC.md tiene %d líneas (> 300)' % n)
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
