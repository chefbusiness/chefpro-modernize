#!/usr/bin/env python3
"""
gate_f1.py — Restaurant Checklists Kit Pro (EN) · gate de salida de la F1 (copia adaptada del staff-kit).

Sale con código ≠ 0 salvo que:
  1. `censo_es.json` exista y cada uno de sus 11 libros tenga fila en SPEC §2.1 (fichero ES y EN entre comillas
     invertidas) con el mismo fichero EN y título que `mapas.py`, y cada pestaña del censo tenga fila en §2.2
     (libro o «todos») con el mismo EN que `mapas.HOJAS`.
  2. Toda decisión `| Dn |` tenga estado DECIDIDA o PROPUESTA [(ES)], numeración D1..Dn sin huecos ni duplicados.
  3. No quede TODO/TBD/XXX en SPEC.md ni en F1-inventario-es.md.
  4. D1-D4 lleven slug, variable de Stripe, nombre, title SEO, precio y la fórmula sin anclas; la SPEC, la URL del
     producto; y ninguna ancla de precio viva (`priceOld: '…'`, «-NN%», «worth $», «launch price»).
  5. Las cifras del censo que cita la SPEC sean las de `censo_es.json` y los grupos de §7 los de `textos_es.json`.
  6. Las tablas §0 y §1 de F1-inventario-es.md sean exactamente las que genera el censo (`extraer_textos.tabla_md`
     y `tabla_dependencias_md`), y el inventario tenga la sección «Jerga profesional».
  7. Cada fila de la tabla §3 (reglas) tenga fuente; cada `mapas.REGLAS_US` también; cada celda de `POR_CELDA`
     vaya a «regenerar» y cada celda de `ADAPTAR` a un grupo de traducción (G1/G2); cada aparición de una clave de
     `GLOSARIO` en celda sea «mapa-glosario» o «regenerar».
  8. `mapas.autotest()` y `mapas.cruzar_censo()` den 0 errores (incluye denominaciones, horas y «ningún literal EN
     cambia de color»).
  9. SPEC.md tenga ≤ 220 líneas y GLOSARIO-JERGA-ES-EN.md la sección de este kit.

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


def miles(n):
    return '{:,}'.format(n).replace(',', '.')


def main():
    p_spec = os.path.join(AQUI, 'SPEC.md')
    p_censo = os.path.join(AQUI, 'censo_es.json')
    p_textos = os.path.join(AQUI, 'textos_es.json')
    p_inv = os.path.join(AQUI, 'F1-inventario-es.md')
    p_glos = os.path.join(AQUI, '..', 'GLOSARIO-JERGA-ES-EN.md')
    for p in (p_spec, p_censo, p_textos, p_inv, p_glos):
        if not os.path.exists(p):
            err('falta ' + os.path.basename(p))
    if errores:
        return fin()
    spec = open(p_spec, encoding='utf-8').read()
    inv = open(p_inv, encoding='utf-8').read()
    glos = open(p_glos, encoding='utf-8').read()
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

    # 1. pestañas (filas de 3 o de 6 columnas)
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
            elif mapas.HOJAS.get(h) != en:
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

    # 4. nombre, slug, precio, Stripe, sin anclas
    for d, aguja in (('D1', mapas.SLUG), ('D1', mapas.ENV_STRIPE), ('D1', mapas.JWT), ('D2', mapas.PRODUCTO),
                     ('D2', mapas.TITULO_SEO), ('D3', '$19'),
                     ('D4', 'One-time payment · lifetime access · updates included')):
        if not re.search(r'\|\s*' + d + r'\s*\|[^\n]*' + re.escape(aguja), spec):
            err('%s no lleva «%s»' % (d, aguja))
    if '/en/digital-products/' + mapas.SLUG not in spec:
        err('SPEC sin la URL /en/digital-products/' + mapas.SLUG)
    for rx in (r"priceOld\s*:\s*['\"]", r'(?<![\w.])-\d{2}%', r'(?<!«)\bworth \$', r'(?<!ni «)launch price(?!»)'):
        for m in re.finditer(rx, spec):
            err('SPEC con un ancla de precio viva: %r' % spec[max(0, m.start() - 20):m.end() + 20])

    # 5. cifras del censo y de los grupos
    citas = [
        '%d hojas' % T['hojas'], '%d fórmulas' % T['celdas_formula'],
        '%d con referencia a hoja' % T['formulas_con_hoja'], '%d DV' % T['dv'], '%d CF' % T['cf'],
        '%d merges' % T['merges'], '%d áreas' % T['areas_impresion'],
        '%d títulos de impresión' % T['titulos_impresion'], '%d paneles' % T['paneles'],
        '%d hojas protegidas' % T['hojas_protegidas'], '%s celdas verdes' % miles(T['verdes']),
        '%d tareas' % T['tareas'], '%d formatos con €' % T['formatos_euro'],
        '%d horas de 24 h' % T['horas_24h'], '%d fórmulas por celda' % len(mapas.FORMULAS_POR_CELDA),
        '%d celdas con °C' % T['textos_celsius'],
    ]
    if T['hojas'] != n_hojas:
        err('recuento de hojas incoherente')
    for aguja in citas:
        if aguja not in spec:
            err('SPEC no cita la cifra del censo «%s»' % aguja)
    for g in textos['meta']['grupos']:
        if g['id'] != 'GM' and '**%s** %d' % (g['id'], g['n_cadenas']) not in spec:
            err('SPEC §7 no cita el grupo %s con %d cadenas' % (g['id'], g['n_cadenas']))
        if g['id'] == 'GM' and 'GM %d' % g['n_cadenas'] not in spec:
            err('SPEC §7 no cita GM %d' % g['n_cadenas'])
    if '%s cadenas' % miles(textos['meta']['n_cadenas']) not in spec:
        err('SPEC §7 no cita %s cadenas' % miles(textos['meta']['n_cadenas']))
    if T['graficos'] or T['imagenes'] or T['hojas_con_password'] or T['comentarios']:
        err('el censo tiene gráficos/imágenes/comentarios/contraseñas y el inventario dice que no')
    if '%d celdas de puesto/zona' % censo['dependencias']['puestos']['apariciones'] not in spec:
        err('SPEC D8 no cita las celdas de puesto/zona del censo')

    # 6. tablas del inventario = censo
    if extraer_textos.tabla_md(censo) not in inv:
        err('F1-inventario-es.md §0 no coincide con el censo (regenerar con extraer_textos.py --md)')
    if extraer_textos.tabla_dependencias_md(censo) not in inv:
        err('F1-inventario-es.md §1 no coincide con el censo (regenerar con extraer_textos.py --md)')
    if '## 4. Jerga profesional' not in inv:
        err('F1-inventario-es.md sin la sección «Jerga profesional»')

    # 7. reglas con fuente; celdas de mapas.py con su tratamiento
    for f in filas_tabla(seccion(spec, '## 3. Reglas'))[1:]:
        if len(f) < 4 or not f[3]:
            err('SPEC §3: fila sin fuente: %r' % f[:1])
    for k, (val, fuente) in mapas.REGLAS_US.items():
        if not fuente:
            err('REGLAS_US sin fuente: ' + k)
    tr_celda, grupo_celda = {}, {}
    for e in textos['cadenas']:
        for o in e['donde']:
            if o.get('t') == 'celda':
                tr_celda[(o['f'], o['h'], o['c'])] = o['tr']
                grupo_celda[(o['f'], o['h'], o['c'])] = e['grupo']
                if e['es'] in mapas.GLOSARIO and o['tr'] not in ('mapa-glosario', 'regenerar'):
                    err('celda del GLOSARIO con tratamiento %s: %s:%s!%s' % (o['tr'], o['f'], o['h'], o['c']))
    for k in mapas.POR_CELDA:
        if tr_celda.get(k) != 'regenerar':
            err('POR_CELDA %r no va a «regenerar» (%s)' % (k, tr_celda.get(k)))
    for k in mapas.ADAPTAR:
        if tr_celda.get(k) != 'traducir' or grupo_celda.get(k) not in ('G1', 'G2'):
            err('ADAPTAR %r no llega a un traductor (%s / %s)' % (k, tr_celda.get(k), grupo_celda.get(k)))

    # 8. mapas
    for e in mapas.autotest() + mapas.cruzar_censo(p_censo):
        err('mapas.py: ' + e)

    # 9. longitud y glosario vivo
    n = spec.count('\n') + 1
    if n > 220:
        err('SPEC.md tiene %d líneas (> 220)' % n)
    if 'Restaurant Checklists Kit Pro' not in glos:
        err('GLOSARIO-JERGA-ES-EN.md sin la sección de este kit')
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
