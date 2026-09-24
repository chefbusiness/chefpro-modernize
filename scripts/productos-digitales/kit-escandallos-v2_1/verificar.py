#!/usr/bin/env python3
"""
verificar.py — Verificación del Kit de Escandallos Pro v2.1 (después de main.py).

    python3 verificar.py [--carpeta <dry-run>] [--json salida.json]

Todo en SERIE (una sola instancia de pycel cada vez). No escribe en la carpeta
verificada: las pruebas que modifican celdas trabajan sobre copias en `_pruebas/`.

  1. pycel: ningún #REF!/#VALUE!/#DIV/0!/#N/A/#NAME?/#NUM! en los 14 libros (ni en la
     evaluación ni en la caché inyectada).
  2. 12: rendimiento en (0,1), factor ≥ 1, merma = 1 − 1/factor; coste por porción del 12 =
     coste de la fila 5 de la 01 con la merma equivalente (0,5 %), en el 01 v2.1 y en una
     copia del 01 PUBLICADO alimentada con esa merma; cocción coherente con la ficha 08.
  3. 13: la alerta salta con variación > umbral y NO con ≤ (incluido el 5 % exacto);
     resumen; para cada ingrediente de una ficha, precio del formato ÷ contenido = precio
     de la ficha ÷ factor.
  4. Rango libre de «Conversiones»: una pareja nueva en la fila 38 (y en la 67) la resuelve
     una fila del escandallo; en la 68 no; en el 01 publicado, ni la 38.
  5. `censo-entregables.py --only <carpeta> --fail`.
  6. Paridad 01-08: fórmulas idénticas a las publicadas salvo el rango de Conversiones;
     ningún otro cambio de estructura; lista de cambios de texto.
  7. Forma: A4, ajuste a 1 página de ancho, pie, fechas numFmtId 14, protección, metadatos,
     línea de versión y subject en los 14, autofiltro, gráficos de 09 y 11 intactos.
"""
import argparse
import contextlib
import json
import logging
import os
import re
import shutil
import subprocess
import sys
import zipfile

AQUI = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(SCRIPTS, 'kit-escandallos-v2_0'))
sys.path.insert(0, AQUI)

import openpyxl                                                # noqa: E402

import main as build                                           # noqa: E402
import motor                                                   # noqa: E402
import nuevas                                                  # noqa: E402

logging.disable(logging.CRITICAL)

ORIGEN = build.ORIGEN          # `--publicados` lo cambia (p. ej., al respaldo tras --real)
ERRORES = ('#REF!', '#VALUE!', '#DIV/0!', '#N/A', '#NAME?', '#NUM!', '#NULL!')
TOL = 0.005


def log(m):
    print(m, flush=True)


def xl(path):
    from pycel import ExcelCompiler
    return ExcelCompiler(filename=path)


def ev(c, ref):
    with open(os.devnull, 'w') as dn, contextlib.redirect_stderr(dn):
        try:
            v = c.evaluate(ref)
        except Exception as e:                                   # noqa: BLE001
            return f'EXC:{type(e).__name__}'
    try:
        import numpy as np
        if isinstance(v, np.generic):
            v = v.item()
    except ImportError:
        pass
    return v


def es_error(v):
    return isinstance(v, str) and (v.startswith(ERRORES) or v.startswith('EXC:'))


def rel(a, b):
    return abs(a - b) / max(abs(b), 1e-12)


# ==========================================================================
def v_errores(carpeta):
    fuera = {}
    for n in build.LIBROS:
        p = os.path.join(carpeta, n)
        wb = openpyxl.load_workbook(p)
        wbv = openpyxl.load_workbook(p, data_only=True)
        c = xl(p)
        malos, total, na_diseno = [], 0, 0
        for ws in wb.worksheets:
            for row in ws.iter_rows():
                for cel in row:
                    if cel.data_type == 'f' and isinstance(cel.value, str):
                        total += 1
                        ref = f"'{ws.title}'!{cel.coordinate}"
                        v = ev(c, ref)
                        cache = wbv[ws.title][cel.coordinate].value
                        # 09 y 11 (v2.0): =IF(x=0,NA(),…) deja #N/A A PROPÓSITO en las
                        # semanas/meses vacíos para que la línea del gráfico no caiga a 0.
                        if (v == '#N/A' and 'NA()' in cel.value.upper()
                                and cache in ('#N/A', None)):
                            na_diseno += 1
                            continue
                        if es_error(v) or es_error(cache):
                            malos.append(f'{ws.title}!{cel.coordinate}: {v!r} / cache {cache!r}')
        fuera[n] = {'formulas': total, 'errores': malos, 'na_por_diseno_grafico': na_diseno}
        log(f'  {n}: {total} fórmulas, {len(malos)} errores'
            + (f' ({na_diseno} #N/A de NA() para el gráfico, por diseño)' if na_diseno else ''))
    return fuera


# ==========================================================================
def v_12(carpeta, pruebas):
    p12 = os.path.join(carpeta, nuevas.F12)
    c = xl(p12)
    D, C = nuevas.DESP, nuevas.COC
    g = lambda ref: ev(c, f"'Test de despiece'!{ref}")        # noqa: E731
    k = lambda ref: ev(c, f"'Test de cocción'!{ref}")          # noqa: E731
    r = {
        'coste_ap': g(D['coste_ap']), 'peso_util': g(D['peso_util']),
        'valor_sub': g(D['valor_sub']), 'neto': g(D['neto']),
        'rendimiento': g(D['rend']), 'coste_kg_util': g(D['coste_kg_util']),
        'factor': g(D['factor']), 'merma': g(D['merma']),
        'porcion_g': g(D['porcion']), 'coste_porcion': g(D['coste_porcion']),
        'perdida_corte_kg': g(f"C{D['perdida']}"),
        'coccion': {'perdida': k(C['perdida']), 'coste_kg_coc': k(C['coste_kg_coc']),
                    'coste_porcion': k(C['coste_porcion']),
                    'merma_comb': k(C['merma_comb'])},
    }
    fallos = []
    if not 0 < r['rendimiento'] < 1:
        fallos.append(f"rendimiento fuera de (0,1): {r['rendimiento']}")
    if not r['factor'] >= 1:
        fallos.append(f"factor < 1: {r['factor']}")
    if abs(r['merma'] - (1 - 1 / r['factor'])) > 1e-12:
        fallos.append('merma ≠ 1 − 1/factor')

    # 01 v2.1 (la de la carpeta): fila 5 con la merma del 12
    p01 = os.path.join(carpeta, motor.FICHEROS[0])
    c01 = xl(p01)
    j5 = ev(c01, "'Escandallo'!J5")
    h5 = ev(c01, "'Escandallo'!H5")
    wbv = openpyxl.load_workbook(p01, data_only=True)
    j5_cache = wbv['Escandallo']['J5'].value
    r['ficha01_v21'] = {'H5': h5, 'J5_pycel': j5, 'J5_cache': j5_cache,
                        'desviacion': rel(j5, r['coste_porcion'])}
    if rel(j5, r['coste_porcion']) > TOL or rel(j5_cache, r['coste_porcion']) > TOL:
        fallos.append(f"01 v2.1 J5 {j5} vs 12 {r['coste_porcion']}")

    # 01 PUBLICADO alimentado con la merma sin redondear (control independiente)
    cp = os.path.join(pruebas, '01-publicado-con-merma-12.xlsx')
    shutil.copy2(os.path.join(ORIGEN, motor.FICHEROS[0]), cp)
    cpub = xl(cp)
    antes = ev(cpub, "'Escandallo'!J5")
    cpub.set_value("'Escandallo'!H5", r['merma'])
    despues = ev(cpub, "'Escandallo'!J5")
    r['ficha01_publicada'] = {'J5_con_merma_20': antes, 'J5_con_merma_12': despues,
                              'desviacion': rel(despues, r['coste_porcion'])}
    if rel(despues, r['coste_porcion']) > TOL:
        fallos.append(f'01 publicado + merma: {despues} vs {r["coste_porcion"]}')

    # cocción ↔ ficha 08: la porción cocinada con la merma combinada cuesta lo mismo
    q = k(C['porcion']) / k(C['unidades'])
    precio = k(C['coste_kg'])
    ficha = q / (1 - r['coccion']['merma_comb']) * precio
    r['coccion']['fila_ficha_equivalente'] = ficha
    if rel(ficha, r['coccion']['coste_porcion']) > TOL:
        fallos.append('cocción: la ficha con la merma combinada no da el coste del test')
    if abs(r['coccion']['merma_comb'] - (1 - (1 - k(C['merma_desp'])) *
                                         (1 - r['coccion']['perdida']))) > 1e-12:
        fallos.append('merma combinada mal calculada')

    # R1 CH-04: con una merma de despiece ≠ 0 (el solomillo del despiece, a precio
    # de factura) el coste por porción cocinada sigue cuadrando con la ficha.
    cp12 = os.path.join(pruebas, '12-coccion-con-despiece.xlsx')
    shutil.copy2(p12, cp12)
    c2 = xl(cp12)
    hoja = "'Test de cocción'!"
    # pycel sólo recalcula tras set_value las fórmulas que YA estaban en su grafo:
    # hay que evaluar entradas y resultados antes (si no, C17/C18 salen viejos).
    for ref in ('C7', 'C8', 'C9', 'C10', 'C12', 'C15', 'C16', 'C17', 'C18'):
        ev(c2, hoja + ref)
    for ref, v in (('C7', 1), ('C8', g(D['precio'])),
                   ('C9', 0.74), ('C10', r['merma']), ('C12', 148)):
        c2.set_value(hoja + ref, v)
    cp_test = ev(c2, hoja + 'C17')
    comb = ev(c2, hoja + 'C18')
    ficha_sol = 0.148 / (1 - comb) * ev(c2, hoja + 'C8')
    r['coccion']['caso_solomillo'] = {'C17_test': cp_test, 'C18': comb,
                                      'ficha_merma_combinada': ficha_sol}
    if rel(cp_test, ficha_sol) > 1e-9:
        fallos.append(f'cocción con despiece: test {cp_test} ≠ ficha {ficha_sol}')

    # R1 CH-01: la merma del ejemplo cabe en la horquilla de «Carne roja» del kit.
    _, mn, mx = [m for m in motor.MERMAS if m[0] == 'Carne roja'][0][1:]
    r['merma_en_horquilla_carne_roja'] = [mn, mx]
    if not mn <= r['merma'] <= mx:
        fallos.append(f"merma del solomillo {r['merma']:.4f} fuera de Carne roja {mn}-{mx}")

    # R1 CH-03/T2: la ficha 08 (picada en crudo, merma 0 %) = test de cocción.
    p08 = os.path.join(carpeta, '08-food-truck.xlsx')
    c08 = xl(p08)
    j5_08, h5_08 = ev(c08, "'Smash Burger'!J5"), ev(c08, "'Smash Burger'!H5")
    r['ficha08'] = {'H5': h5_08, 'J5': j5_08, 'test_C17': r['coccion']['coste_porcion']}
    if h5_08 != 0 or rel(j5_08, r['coccion']['coste_porcion']) > TOL:
        fallos.append(f"08 Smash Burger H5={h5_08} J5={j5_08} vs test "
                      f"{r['coccion']['coste_porcion']}")
    r['fallos'] = fallos
    return r


# ==========================================================================
def v_13(carpeta, pruebas):
    L = nuevas.LISTA
    p13 = os.path.join(carpeta, nuevas.F13)
    wb = openpyxl.load_workbook(p13)
    wbv = openpyxl.load_workbook(p13, data_only=True)
    ws, wsv = wb['Lista de precios'], wbv['Lista de precios']
    d0 = L['d0']
    d1 = d0
    while ws.cell(row=d1 + 1, column=8).value:
        d1 += 1
    filas = {}
    for r in range(d0, d1 + 1):
        nombre = ws.cell(row=r, column=1).value
        if nombre:
            filas[nombre] = r
    n_ing = len(filas)
    fallos = []
    res = {'filas_tabla': d1 - d0 + 1, 'ingredientes': n_ing,
           'resumen_cache': {'n': wsv[L['resumen_n']].value,
                             'alertas': wsv[L['alertas']].value,
                             'mayor': wsv[L['mayor']].value}}
    if wsv[L['resumen_n']].value != n_ing:
        fallos.append(f"resumen nº ingredientes {wsv[L['resumen_n']].value} ≠ {n_ing}")

    # --- alerta: > umbral salta; ≤ no -------------------------------------
    cp = os.path.join(pruebas, '13-alertas.xlsx')
    shutil.copy2(p13, cp)
    c = xl(cp)
    hoja = "'Lista de precios'!"
    r0 = d1 - 1                       # una fila vacía del final
    casos = []
    for col in 'EGIJK':                 # pycel exige evaluar antes de set_value
        ev(c, f'{hoja}{col}{r0}')
    ev(c, hoja + L['alertas'])
    ev(c, hoja + L['umbral'])
    for etiqueta, g_, i_, esperado in (
            ('+6 %', 21.2, 20, 'ALERTA'), ('+5 % exacto', 21, 20, 'OK'),
            ('+4,9 %', 20.98, 20, 'OK'), ('−10 %', 18, 20, 'OK'),
            ('+5,01 %', 21.002, 20, 'ALERTA')):
        c.set_value(f'{hoja}E{r0}', 1)
        c.set_value(f'{hoja}G{r0}', g_)
        c.set_value(f'{hoja}I{r0}', i_)
        j, kk = ev(c, f'{hoja}J{r0}'), ev(c, f'{hoja}K{r0}')
        casos.append({'caso': etiqueta, 'variacion': j, 'estado': kk, 'esperado': esperado})
        if kk != esperado:
            fallos.append(f'alerta {etiqueta}: {kk} (esperado {esperado})')
    alertas_con = ev(c, hoja + L['alertas'])
    # umbral: la fila de demostración del AOVE (+10,29 %) con umbral 10 % y 11 %
    aove = filas.get('Aceite de oliva virgen extra (AOVE)')
    c.set_value(hoja + L['umbral'], 0.10)
    e10 = ev(c, f'{hoja}K{aove}')
    c.set_value(hoja + L['umbral'], 0.11)
    e11 = ev(c, f'{hoja}K{aove}')
    casos.append({'caso': 'AOVE +10,29 % con umbral 10 % / 11 %', 'estado': [e10, e11],
                  'esperado': ['ALERTA', 'OK']})
    if [e10, e11] != ['ALERTA', 'OK']:
        fallos.append(f'umbral editable: {e10}/{e11}')
    res['alertas'] = casos
    res['resumen_con_prueba'] = {'alertas': alertas_con}
    res['demos_cache'] = {n: {'J': wsv.cell(row=filas[n], column=10).value,
                              'K': wsv.cell(row=filas[n], column=11).value}
                          for n in ('Aceite de oliva virgen extra (AOVE)',
                                    'Solomillo de ternera')}

    # --- precio del formato ÷ contenido = precio de la ficha ÷ factor --------
    datos = nuevas.cargar_datos()
    alias = datos['lista_precios']['alias']
    excluir = datos['lista_precios'].get('excluir', {})
    conv = nuevas.conversiones(ORIGEN)
    fichas = nuevas.leer_fichas(ORIGEN, datos)
    ok, malos, excluidas = 0, [], []
    for f in fichas:
        canon = alias.get(f['nombre'], f['nombre'])
        if f['nombre'] in excluir:
            excluidas.append(f"{f['fichero'][:2]} {f['hoja']}!A{f['fila']} {f['nombre']}")
            if canon in filas:
                fallos.append(f'{canon}: excluido pero con fila en el 13')
            continue
        r = filas.get(canon)
        if r is None:
            malos.append((canon, f"{f['fichero']}:{f['hoja']}:{f['fila']} {f['nombre']}: sin fila"))
            continue
        e = ws.cell(row=r, column=5).value
        ub = ws.cell(row=r, column=6).value
        g_ = ws.cell(row=r, column=7).value
        h_cache = wsv.cell(row=r, column=8).value
        factor = float(conv[f"{f['ud']}→{ub}"])
        esperado = round(f['precio'] / factor, 4)
        lista = round(g_ / e, 4)
        if abs(lista - esperado) < 1e-9 and abs(h_cache - esperado) < 1e-9:
            ok += 1
        else:
            malos.append((canon, f"{f['fichero'][:2]} {f['hoja']}!D{f['fila']} {f['nombre']}"
                                 f" (→ {canon}): ficha {f['precio']} €/{f['ud']} ÷ "
                                 f"{factor:g} = {esperado} · lista {g_} ÷ {e} = {lista} ({ub})"))
    res['precios_fichas'] = {'filas_ficha': len(fichas), 'coinciden': ok,
                             'difieren': [m for _, m in malos], 'excluidas': excluidas}
    # Las únicas diferencias admitidas: los ingredientes que el propio kit usa con dos
    # precios (lo avisa la Nota de SU fila: «La plantilla NN lo usa a … (otro proveedor)»).
    notas_dos_precios = [n for n, r in filas.items()
                         if (ws.cell(row=r, column=13).value or '').find('otro proveedor') >= 0]
    res['ingredientes_con_dos_precios'] = notas_dos_precios
    for canon, m in malos:
        if canon not in notas_dos_precios:
            fallos.append('precio no cuadra: ' + m)
    if len(excluidas) != sum(1 for f in fichas if f['nombre'] in excluir) or \
            any(k not in {f['nombre'] for f in fichas} for k in excluir):
        fallos.append('exclusiones del 13 sin uso o mal contadas')

    # R1 CH-06: «Se usa en: …» en la Nota de cada ingrediente, con TODAS sus fichas.
    usos = {}
    for f in fichas:
        if f['nombre'] in excluir:
            continue
        usos.setdefault(alias.get(f['nombre'], f['nombre']), set()).add(
            (f['plantilla'], f['hoja']))
    sin_uso = []
    for nombre, r in filas.items():
        nota = ws.cell(row=r, column=13).value or ''
        if not nota.startswith('Se usa en: '):
            sin_uso.append(nombre)
            continue
        for plant, hoja_ in usos.get(nombre, ()):
            if f'{plant} «' not in nota or f'«{hoja_}»' not in nota:
                sin_uso.append(f'{nombre}: falta {plant} {hoja_}')
    res['notas_se_usa_en'] = {'filas': len(filas), 'fallan': sin_uso}
    if sin_uso:
        fallos.append(f'«Se usa en» incompleto: {sin_uso[:5]}')

    # --- forma de la tabla -----------------------------------------------
    res['autofiltro'] = ws.auto_filter.ref
    res['area_impresion'] = str(ws.print_area)
    res['proteccion'] = {'sheet': ws.protection.sheet, 'password': ws.protection.password,
                         'sort_permitido': ws.protection.sort is False,
                         'autofiltro_permitido': ws.protection.autoFilter is False}
    if not ws.auto_filter.ref:
        fallos.append('sin autofiltro')
    # R1 CH-02: filtrar SÍ con la hoja protegida; ordenar NO (hay fórmulas bloqueadas).
    if not (ws.protection.sheet and ws.protection.sort is not False
            and ws.protection.autoFilter is False and not ws.protection.password):
        fallos.append('protección del 13 no es la de R1 (autofiltro sí, ordenar no, '
                      'sin contraseña)')
    # R1 CH-02: fórmulas (H, J, K) bloqueadas; el resto de la tabla, editable.
    mal_bloqueo = [ws.cell(row=r, column=col).coordinate for r in range(d0, d1 + 1)
                   for col in range(1, 14)
                   if ws.cell(row=r, column=col).protection.locked != (col in (8, 10, 11))]
    res['celdas_bloqueo_incorrecto'] = mal_bloqueo[:10]
    if mal_bloqueo:
        fallos.append(f'{len(mal_bloqueo)} celdas de la tabla con el bloqueo al revés')
    # R1 CH-08: se imprime sin Notas.
    if not str(ws.print_area).endswith(f'$L${d1}'):
        fallos.append(f'área de impresión del 13: {ws.print_area}')
    res['fallos'] = fallos
    return res


# ==========================================================================
def v_rango_libre(carpeta, pruebas):
    fuera, fallos = {}, []

    def prueba(origen, nombre, fila_conv):
        cp = os.path.join(pruebas, nombre)
        shutil.copy2(origen, cp)
        wb = openpyxl.load_workbook(cp)
        co = wb['Conversiones']
        co.cell(row=fila_conv, column=1, value='lata→g')
        co.cell(row=fila_conv, column=2, value=400)
        co.cell(row=fila_conv, column=3, value='lata de conserva de 400 g (prueba)')
        es = wb['Escandallo']
        for col, v in zip('ABCDEF', ['Tomate triturado (prueba)', 'Conservas/encurtidos',
                                     'lata', 1.2, 150, 'g']):
            es[f'{col}15'] = v
        wb.save(cp)
        c = xl(cp)
        return {'G15': ev(c, "'Escandallo'!G15"), 'J15': ev(c, "'Escandallo'!J15"),
                'J26_total': ev(c, "'Escandallo'!J26")}

    v21 = os.path.join(carpeta, motor.FICHEROS[0])
    pub = os.path.join(ORIGEN, motor.FICHEROS[0])
    fuera['v21_fila38'] = prueba(v21, 'rango-v21-38.xlsx', 38)
    fuera['v21_fila67'] = prueba(v21, 'rango-v21-67.xlsx', 67)
    fuera['v21_fila68'] = prueba(v21, 'rango-v21-68.xlsx', 68)
    fuera['publicado_fila38'] = prueba(pub, 'rango-pub-38.xlsx', 38)
    esperado = 150 / (1 - 0.08) * 1.2 / 400
    fuera['coste_esperado_J15'] = esperado
    if fuera['v21_fila38']['G15'] != 400 or rel(fuera['v21_fila38']['J15'], esperado) > 1e-9:
        fallos.append(f"v2.1 fila 38 no resuelve: {fuera['v21_fila38']}")
    if fuera['v21_fila67']['G15'] != 400:
        fallos.append(f"v2.1 fila 67 no resuelve: {fuera['v21_fila67']}")
    if fuera['v21_fila68']['G15'] != '?':
        fallos.append(f"v2.1 fila 68 debería quedar fuera: {fuera['v21_fila68']}")
    if fuera['publicado_fila38']['G15'] != '?':
        fallos.append('control: el publicado ya resolvía la fila 38 (la prueba no prueba)')
    fuera['fallos'] = fallos
    return fuera


# ==========================================================================
def v_censo(carpeta, pruebas):
    out = os.path.join(pruebas, 'censo.json')
    r = subprocess.run([sys.executable, '-W', 'ignore',
                        os.path.join(SCRIPTS, 'censo-entregables.py'),
                        '--only', carpeta, '--fail', '--json', out],
                       capture_output=True, text=True)
    datos = json.load(open(out, encoding='utf-8')) if os.path.isfile(out) else []
    campos = ('nocache_real', 'box_colA_muerta', 'noprint', 'nonlat', 'empty_str')
    por_fichero = {}
    for d in datos:
        n = os.path.basename(d.get('f') or '?')
        por_fichero[n] = {k: d.get(k) for k in campos + ('creator', 'bio_vieja',
                                                         'version_line', 'form')}
    return {'exit': r.returncode, 'resumen': r.stdout.strip().splitlines()[-8:],
            'ficheros': por_fichero, 'n': len(datos)}


# ==========================================================================
def _cf(ws):
    return sorted((str(r.sqref), tuple((x.type, x.operator, tuple(x.formula or ()))
                                       for x in r.rules))
                  for r in ws.conditional_formatting)


# R1: cambios de valor, estilo y estructura PREVISTOS en 01-08, además de
# Mermas!A3 y Conversiones!A2 (en todos) y de las correcciones de texto CH-10.
VALORES_R1 = {'01': {'Escandallo!H5'}, '08': {'Smash Burger!H5'},
              '03': {'Rotación Semanal!J3', 'Rotación Semanal!K3'}}
ESTILOS_R1 = {'03': {'Rotación Semanal!J3', 'Rotación Semanal!K3'}}
CF_R1 = {'03': {'Rotación Semanal'}}
# Hojas cuyos RESULTADOS (caché de fórmulas) pueden cambiar: las que dependen de
# 01!H5 y 08!H5, y la K3 nueva del 03.
RESULTADOS_R1 = {'01': {'Escandallo'}, '08': {'Smash Burger', 'Punto de Equilibrio'},
                 '03': {'Rotación Semanal'}}


def _correccion_prevista(va, vb, col, fila_a, cf):
    """¿Es va → vb una corrección de texto de CH-10 (nombre en A o categoría en B)?"""
    if col == 1:
        return cf.get('renombrar', {}).get(va) == vb
    if col == 2:
        nombre = cf.get('renombrar', {}).get(fila_a, fila_a)
        return cf.get('categoria', {}).get(nombre) == vb
    return False


def v_paridad(carpeta):
    fuera, fallos = {}, []
    patron = re.compile(r"Conversiones!\$A\$5:\$B\$67")
    cf_textos = nuevas.cargar_datos().get('correcciones_fichas', {})
    for n in motor.FICHEROS:
        a = openpyxl.load_workbook(os.path.join(ORIGEN, n))
        b = openpyxl.load_workbook(os.path.join(carpeta, n))
        av = openpyxl.load_workbook(os.path.join(ORIGEN, n), data_only=True)
        bv = openpyxl.load_workbook(os.path.join(carpeta, n), data_only=True)
        pref = n[:2]
        rep = {'hojas_iguales': a.sheetnames == b.sheetnames, 'formulas_distintas': [],
               'valores_distintos': [], 'estilo_distinto': [], 'estructura': [],
               'instrucciones_nuevas': [], 'formulas_comparadas': 0,
               'correcciones_texto': [], 'resultados_cambiados': []}
        for t in a.sheetnames:
            wa, wb_ = a[t], b[t]
            if t == 'Instrucciones':
                ta = [c.value for c in wa['B'] if c.value is not None]
                tb = [c.value for c in wb_['B'] if c.value is not None]
                ta2 = [x for x in ta if not motor.RX_VERSION.match(str(x))]
                tb2 = [x for x in tb if not motor.RX_VERSION.match(str(x))]
                nuevas_l = [x for x in tb2 if x not in ta2]
                quitadas = [x for x in ta2 if x not in tb2]
                orden = [x for x in tb2 if x in ta2] == ta2
                rep['instrucciones_nuevas'] = nuevas_l
                if quitadas or not orden:
                    fallos.append(f'{n}: Instrucciones pierde o reordena líneas')
                continue
            for k, fa, fb in (('merges', sorted(map(str, wa.merged_cells.ranges)),
                               sorted(map(str, wb_.merged_cells.ranges))),
                              ('dv', sorted(f'{d.type}:{d.formula1}:{d.sqref}' for d in
                                            wa.data_validations.dataValidation),
                               sorted(f'{d.type}:{d.formula1}:{d.sqref}' for d in
                                      wb_.data_validations.dataValidation)),
                              ('cf', _cf(wa), _cf(wb_)),
                              ('proteccion', (wa.protection.sheet, wa.protection.password),
                               (wb_.protection.sheet, wb_.protection.password)),
                              ('dimensiones', wa.max_column, wb_.max_column),
                              ('anchos', {k2: v.width for k2, v in wa.column_dimensions.items()},
                               {k2: v.width for k2, v in wb_.column_dimensions.items()}),
                              ('area', str(wa.print_area), str(wb_.print_area)),
                              ('freeze', wa.freeze_panes, wb_.freeze_panes)):
                if fa != fb:
                    rep['estructura'].append(f'{t}: {k} {fa} → {fb}')
            filas = max(wa.max_row, wb_.max_row)
            cols = max(wa.max_column, wb_.max_column)
            for r in range(1, filas + 1):
                for col in range(1, cols + 1):
                    ca, cb = wa.cell(row=r, column=col), wb_.cell(row=r, column=col)
                    va, vb = ca.value, cb.value
                    if isinstance(va, str) and va.startswith('='):
                        rep['formulas_comparadas'] += 1
                        if patron.sub('Conversiones!$A$5:$B$37', vb or '') != va:
                            rep['formulas_distintas'].append(f'{t}!{ca.coordinate}')
                        ra, rb = av[t][ca.coordinate].value, bv[t][ca.coordinate].value
                        distinto = (abs(ra - rb) > 1e-9
                                    if isinstance(ra, (int, float)) and isinstance(rb, (int, float))
                                    and not isinstance(ra, bool) else ra != rb)
                        if distinto:
                            rep['resultados_cambiados'].append((f'{t}!{ca.coordinate}', ra, rb))
                    elif va != vb:
                        if _correccion_prevista(va, vb, col, wa.cell(row=r, column=1).value,
                                                cf_textos):
                            rep['correcciones_texto'].append(f'{t}!{ca.coordinate}: {va!r} → {vb!r}')
                        else:
                            rep['valores_distintos'].append(
                                f'{t}!{ca.coordinate}: {va!r} → {vb!r}')
                    if (ca.number_format != cb.number_format
                            or ca.fill.fgColor.rgb != cb.fill.fgColor.rgb
                            or ca.protection.locked != cb.protection.locked):
                        rep['estilo_distinto'].append(f'{t}!{ca.coordinate}')
        estructura_inesperada = [e for e in rep['estructura']
                                 if not e.startswith('Conversiones: area')
                                 and not any(e.startswith(f'{h}: cf ')
                                             for h in CF_R1.get(pref, ()))]
        if estructura_inesperada:
            fallos.append(f'{n}: cambios de estructura {estructura_inesperada}')
        if rep['formulas_distintas']:
            fallos.append(f"{n}: {len(rep['formulas_distintas'])} fórmulas distintas")
        vals_esperados = {'Mermas!A3', 'Conversiones!A2'} | VALORES_R1.get(pref, set())
        inesperados = [v for v in rep['valores_distintos']
                       if v.split(':')[0] not in vals_esperados]
        if inesperados:
            fallos.append(f'{n}: valores cambiados sin estar previstos: {inesperados[:5]}')
        rep['estilo_distinto_inesperado'] = [
            e for e in rep['estilo_distinto']
            if e not in {'Mermas!A3'} | ESTILOS_R1.get(pref, set())]
        if rep['estilo_distinto_inesperado']:
            fallos.append(f"{n}: estilos distintos {rep['estilo_distinto_inesperado'][:5]}")
        # R1: sólo cambian resultados en las hojas que dependen de lo que se ha tocado
        res_inesperados = [x for x in rep['resultados_cambiados']
                           if x[0].split('!')[0] not in RESULTADOS_R1.get(pref, set())]
        if res_inesperados:
            fallos.append(f'{n}: resultados cambiados sin estar previstos: {res_inesperados[:5]}')
        fuera[n] = rep
        log(f"  {n}: {rep['formulas_comparadas']} fórmulas, "
            f"{len(rep['formulas_distintas'])} distintas · valores cambiados "
            f"{[v.split(':')[0] for v in rep['valores_distintos']]} · correcciones CH-10 "
            f"{len(rep['correcciones_texto'])} · resultados cambiados "
            f"{len(rep['resultados_cambiados'])} · estructura {rep['estructura']}")
    fuera['fallos'] = fallos
    return fuera


# ==========================================================================
def v_forma(carpeta):
    fuera, fallos = {}, []
    version = nuevas.version_line()
    for n in build.LIBROS:
        p = os.path.join(carpeta, n)
        wb = openpyxl.load_workbook(p)
        pr = wb.properties
        rep = {'subject': pr.subject, 'creator': pr.creator, 'title': pr.title,
               'category': pr.category, 'description': pr.description,
               'keywords': pr.keywords}
        lineas = [c.value for c in wb['Instrucciones']['B'] if isinstance(c.value, str)]
        rep['version'] = [x for x in lineas if motor.RX_VERSION.match(x)]
        if rep['version'] != [version]:
            fallos.append(f'{n}: línea de versión {rep["version"]}')
        if pr.subject != nuevas.SUBJECT:
            fallos.append(f'{n}: subject {pr.subject!r}')
        if n in build.NUEVOS:
            for k, v in (('creator', 'AI Chef Pro'), ('description', 'aichef.pro/kit-escandallos'),
                         ('keywords', 'kit escandallos, AI Chef Pro'),
                         ('category', 'AI Chef Pro · Productos digitales')):
                if getattr(pr, k) != v:
                    fallos.append(f'{n}: {k} = {getattr(pr, k)!r}')
            hojas = {}
            for ws in wb.worksheets:
                ps = ws.page_setup
                h = {'papel': ps.paperSize, 'fitToWidth': ps.fitToWidth,
                     'fitToHeight': ps.fitToHeight,
                     'fitToPage': ws.sheet_properties.pageSetUpPr.fitToPage,
                     'pie': ws.oddFooter.center.text, 'area': ws.print_area,
                     'protegida': ws.protection.sheet,
                     'password': ws.protection.password}
                if ps.paperSize != 9 or ps.fitToWidth != 1 or ps.fitToHeight != 0:
                    fallos.append(f'{n}:{ws.title}: impresión {h}')
                h['orientacion'] = ps.orientation
                if n == nuevas.F12 and ps.orientation != 'portrait':      # R1 CH-07
                    fallos.append(f'{n}:{ws.title}: no está en vertical')
                if ws.oddFooter.center.text != 'AI Chef Pro · aichef.pro · Página &P de &N':
                    fallos.append(f'{n}:{ws.title}: pie')
                if ws.title != 'Instrucciones':
                    if not ws.protection.sheet or ws.protection.password:
                        fallos.append(f'{n}:{ws.title}: protección')
                    verdes_bloq = [c.coordinate for row in ws.iter_rows() for c in row
                                   if motor._es_verde(c) and c.protection.locked]
                    if verdes_bloq:
                        fallos.append(f'{n}:{ws.title}: verdes bloqueadas {verdes_bloq[:5]}')
                    fechas = [c.coordinate for row in ws.iter_rows() for c in row
                              if c.number_format == nuevas.FMT_FECHA]
                    h['celdas_fecha'] = len(fechas)
                    formulas = [c.value for row in ws.iter_rows() for c in row
                                if c.data_type == 'f' and isinstance(c.value, str)]
                    if any('COUNTA' in f.upper() for f in formulas):
                        fallos.append(f'{n}:{ws.title}: usa COUNTA')
                    sin_iferror = [f for f in formulas if '/' in f and 'IFERROR' not in f]
                    if sin_iferror:
                        fallos.append(f'{n}:{ws.title}: división sin IFERROR {sin_iferror[:2]}')
                hojas[ws.title] = h
            rep['hojas'] = hojas
            # numFmtId 14 de verdad en el XML
            with zipfile.ZipFile(p) as z:
                styles = z.read('xl/styles.xml').decode('utf-8')
            rep['numFmtId14_en_estilos'] = 'numFmtId="14"' in styles
            if not rep['numFmtId14_en_estilos']:
                fallos.append(f'{n}: ningún estilo con numFmtId 14')
        fuera[n] = rep
    for n in ('09-control-mermas.xlsx', '11-dashboard-food-cost-mensual.xlsx'):
        with zipfile.ZipFile(os.path.join(carpeta, n)) as z:
            ok = 'xl/charts/chart1.xml' in z.namelist()
        fuera[n]['grafico'] = ok
        if not ok:
            fallos.append(f'{n}: ha perdido el gráfico')
    # 01-08: área de impresión de Conversiones
    for n in motor.FICHEROS:
        wb = openpyxl.load_workbook(os.path.join(carpeta, n))
        fuera[n]['area_conversiones'] = wb['Conversiones'].print_area
        if not str(wb['Conversiones'].print_area).endswith('$J$67'):
            fallos.append(f'{n}: área de Conversiones {wb["Conversiones"].print_area}')
    fuera['fallos'] = fallos
    return fuera


# ==========================================================================
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--carpeta', default=build.DRYRUN)
    ap.add_argument('--json', default=None)
    ap.add_argument('--publicados', default=build.ORIGEN,
                    help='carpeta con los 12 xlsx v2.0 de referencia (tras --real: el respaldo)')
    args = ap.parse_args()
    global ORIGEN
    ORIGEN = args.publicados
    carpeta = args.carpeta
    pruebas = os.path.join(os.path.dirname(carpeta), 'v2_1-pruebas')
    if os.path.isdir(pruebas):
        shutil.rmtree(pruebas)
    os.makedirs(pruebas)

    res = {'carpeta': carpeta}
    log('== 1/7 · pycel: errores en los 14 ==')
    res['errores'] = v_errores(carpeta)
    log('== 2/7 · 12: rendimiento, factor y coste por porción vs 01 ==')
    res['libro12'] = v_12(carpeta, pruebas)
    log(json.dumps({k: v for k, v in res['libro12'].items() if k != 'fallos'},
                   ensure_ascii=False, default=str)[:900])
    log('== 3/7 · 13: alertas y precios vs fichas ==')
    res['libro13'] = v_13(carpeta, pruebas)
    log(f"  {res['libro13']['precios_fichas']['coinciden']}/"
        f"{res['libro13']['precios_fichas']['filas_ficha']} filas de ficha cuadran; "
        f"difieren {len(res['libro13']['precios_fichas']['difieren'])}")
    for m in res['libro13']['precios_fichas']['difieren']:
        log('    ' + m)
    for ccc in res['libro13']['alertas']:
        log(f'    alerta {ccc}')
    log('== 4/7 · rango libre de Conversiones ==')
    res['rango_libre'] = v_rango_libre(carpeta, pruebas)
    log(json.dumps(res['rango_libre'], ensure_ascii=False, default=str))
    log('== 5/7 · censo-entregables --fail ==')
    res['censo'] = v_censo(carpeta, pruebas)
    log('\n'.join(res['censo']['resumen']))
    log('== 6/7 · paridad 01-08 vs publicados ==')
    res['paridad'] = v_paridad(carpeta)
    log('== 7/7 · forma ==')
    res['forma'] = v_forma(carpeta)

    fallos = []
    for n, r in res['errores'].items():
        fallos += [f'{n}: {e}' for e in r['errores']]
    for k in ('libro12', 'libro13', 'rango_libre', 'paridad', 'forma'):
        fallos += [f'{k}: {f}' for f in res[k]['fallos']]
    if res['censo']['exit'] != 0:
        fallos.append(f"censo --fail exit {res['censo']['exit']}")
    res['fallos'] = fallos
    if args.json:
        with open(args.json, 'w', encoding='utf-8') as fh:
            json.dump(res, fh, ensure_ascii=False, indent=1, default=str)
        log(f'informe → {args.json}')
    log('\n' + ('FALLOS:\n  ' + '\n  '.join(fallos) if fallos else 'VERIFICACIÓN OK'))
    return 1 if fallos else 0


if __name__ == '__main__':
    sys.exit(main())
