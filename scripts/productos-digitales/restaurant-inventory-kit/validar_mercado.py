#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validar_mercado.py — gate de mercado_en.json (Restaurant Inventory Kit Pro, F2-EN).

SPEC: D8, D9, D11, D13-D15, D20, D24, D25 y §8 G7 («Identidades de D14»). Sesión Claude Code, 25-sep-2026.
Modelo: recipe-costing-kit/validar_mercado.py. Recalcula todo desde las celdas de «libros», sin fiarse de los
resúmenes de generar_mercado.py («identidades» solo se compara al final). No abre ningún xlsx: la cobertura del ES
sale de textos_es.json (quién es producto y en qué celda del 01 vive).

Comprueba
  A. Fuentes: cada precio con fuente del piloto, [derivado] con cálculo o [estimado] con razonamiento; los que citan
     el piloto sin cambio de formato valen exactamente lo que el catálogo del piloto.
  B. Tabla maestra: 50 productos del 01 (misma hoja y fila) + cod; B08 = mismos 50, mismo orden; 10 categorías D8;
     unidades en la lista D9; par < par max.
  C. Mismo producto ⇒ mismo precio, unidad y categoría en TODAS las celdas de los 9 libros.
  D. BONUS-09: consumo × (lead + cobertura) = par del 01 y stock máx. = par max; EOQ, tope y sugerida recalculados.
  E. Importes = cantidad × precio (03 pedido e historial, 04 incidencias, 07 Top 20), 02 comparativa (mejor precio
     normalizado = precio maestro), 02 «Free over $X» = pedido mínimo, 05 compras = total de enero del 07, Top 20 por
     categoría ≤ gasto de la categoría, food cost 28-32 %, coste por cubierto y variación dentro del objetivo.
  F. Estados: historia del 04 (ACCEPT / REJECT too warm / ACCEPT / N/A) con mapas.FAMILIAS; 06 con los 5 estados
     hoy (fechas D25); 02 cotizaciones.
  G. D25: 19 celdas, fórmula = desfase contra la fecha ES. D20: las 13 celdas de la lista, con las cifras EN.
  H. localizar: los 246 ids GL-mercado, mismos textos ES, EN coherente con la tabla maestra y los proveedores.
  I. D15: teléfonos 555-01xx, correos .example, Tax ID 00-000000n. Texto: cero €/EUR, cero no latinos, cero restos
     de español en todo valor EN.

Uso:  python3 validar_mercado.py [--json RUTA]   → código 1 si algo falla.
"""
from __future__ import print_function

import datetime as dt
import json
import math
import os
import re
import sys
from collections import OrderedDict, defaultdict
from decimal import Decimal, ROUND_HALF_UP

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import mapas  # noqa: E402

_JSON = sys.argv[sys.argv.index('--json') + 1] if '--json' in sys.argv else os.path.join(AQUI, 'mercado_en.json')
M = json.load(open(_JSON, encoding='utf-8'))
T = json.load(open(os.path.join(AQUI, 'textos_es.json'), encoding='utf-8'))
PIL = json.load(open(os.path.join(AQUI, '..', 'recipe-costing-kit', 'mercado_en.json'), encoding='utf-8'))['catalogo']
D9 = set(mapas.UNIDADES_EN)
D8 = list(mapas.CATEGORIAS.values())
VERBOSE = '--verbose' in sys.argv
FALLOS, OKS = [], []
TOL = 0.005


def fallo(msg):
    FALLOS.append(msg)


def ok(msg):
    OKS.append(msg)


def xround(x, n=0):
    return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-n), rounding=ROUND_HALF_UP))


def eq(a, b, tol=TOL):
    return abs(float(a) - float(b)) <= tol


PROD = OrderedDict((p['id'], p) for p in M['productos'])
EXTRA = OrderedDict((p['id'], p) for p in M['productos_extra_historial'])
NOMBRE = {p['en']: p for p in M['productos']}
PROV = M['proveedores']
PROV_EN = {p['en']: p for p in PROV}

# celdas: libro → hoja_es → celda → valor
C = defaultdict(lambda: defaultdict(dict))
for libro, lst in M['libros'].items():
    for c in lst:
        if c['hoja_en'] != mapas.HOJAS[c['hoja_es']]:
            fallo('%s %s!%s: hoja EN %r ≠ mapas %r' % (libro, c['hoja_es'], c['celda'], c['hoja_en'],
                                                      mapas.HOJAS[c['hoja_es']]))
        if c['celda'] in C[libro][c['hoja_es']]:
            fallo('%s %s!%s duplicada' % (libro, c['hoja_es'], c['celda']))
        C[libro][c['hoja_es']][c['celda']] = c['valor']


def v(libro, hoja, ref):
    return C[libro][hoja].get(ref)


def producto_de(texto):
    """Nombre de celda → registro maestro (quita « (sample)» y el formato de la línea de harina del 04)."""
    if not isinstance(texto, str):
        return None
    t = re.sub(r' \(sample\)$', '', texto)
    t = re.sub(r', 50 lb bags$', '', t)
    if t in NOMBRE:
        return NOMBRE[t]
    # nombre corto en los ejemplos: «Beef tenderloin» = «Beef tenderloin (PSMO)» si es el único que casa
    cand = [p for n, p in NOMBRE.items() if re.sub(r' \([^)]*\)$', '', n) == t]
    return cand[0] if len(cand) == 1 else None


# ---------------------------------------------------------------- A. fuentes
TIPOS = {'BLS', 'USDA AMS', 'distribuidor', 'fuente secundaria (resumen de buscador)', '[estimado]', '[derivado]'}
for p in list(PROD.values()) + list(EXTRA.values()):
    f = p['fuente']
    t = f.get('tipo') if isinstance(f, dict) else None
    if t not in TIPOS:
        fallo('A %s: fuente sin tipo válido (%r)' % (p['id'], t))
        continue
    if t == '[estimado]' and len(f.get('razonamiento', '')) < 30:
        fallo('A %s: [estimado] sin razonamiento' % p['id'])
    if t == '[derivado]':
        b = f.get('base_piloto', {})
        if not f.get('calculo') or b.get('id') not in PIL or not eq(b['precio'], PIL[b['id']]['precio'], 1e-9):
            fallo('A %s: [derivado] sin cálculo o sin base del piloto coherente' % p['id'])
    if t not in ('[estimado]', '[derivado]'):
        pid = p.get('id_piloto')
        if pid not in PIL or not eq(p['precio'], round(PIL[pid]['precio'], 2)) or \
                PIL[pid]['ud_compra'] != p['unidad']:
            fallo('A %s: dice fuente del piloto pero precio/unidad no casan (%s %s vs %s %s)' % (
                p['id'], p['precio'], p['unidad'], PIL.get(pid, {}).get('precio'), PIL.get(pid, {}).get('ud_compra')))
    if not (isinstance(p['precio'], (int, float)) and p['precio'] > 0):
        fallo('A %s: precio no positivo' % p['id'])
if not any(F for F in FALLOS if F.startswith('A ')):
    n = {}
    for p in PROD.values():
        n[p['fuente']['tipo']] = n.get(p['fuente']['tipo'], 0) + 1
    ok('A fuentes: %d productos + %d extra · %s' % (len(PROD), len(EXTRA), ', '.join(
        '%s %d' % kv for kv in sorted(n.items()))))

# ---------------------------------------------------------------- B. tabla maestra
es01 = {}
for c in T['cadenas']:
    for w in c['donde']:
        if w.get('f') == '01' and w.get('h') in ('Cocina', 'Barra', 'Almacén') and 'producto' in w.get('det', ''):
            es01[c['es']] = (w['h'], int(re.sub(r'\D', '', w['c'])))
nb = len([F for F in FALLOS if F.startswith('B ')])
if len(es01) != 50:
    fallo('B el ES tiene %d productos en el 01 (esperados 50)' % len(es01))
con01 = [p for p in PROD.values() if p.get('libro01')]
if len(con01) != 50 or len(PROD) != 51:
    fallo('B tabla maestra: %d productos, %d en el 01 (esperados 51 / 50)' % (len(PROD), len(con01)))
for p in con01:
    pos = es01.get(p['es'])
    if pos != (p['libro01']['hoja_es'], p['libro01']['fila']):
        fallo('B %s: posición %r ≠ ES %r' % (p['id'], (p['libro01']['hoja_es'], p['libro01']['fila']), pos))
    if p['b08_fila'] != con01.index(p) + 5:
        fallo('B %s: fila B08 %s ≠ %s' % (p['id'], p['b08_fila'], con01.index(p) + 5))
for p in PROD.values():
    if p['categoria_en'] not in D8:
        fallo('B %s: categoría %r fuera de D8' % (p['id'], p['categoria_en']))
    if p['unidad'] not in D9:
        fallo('B %s: unidad %r fuera de D9' % (p['id'], p['unidad']))
    if p.get('libro01') and not (0 < p['par'] < p['par_max']):
        fallo('B %s: par %s / par max %s' % (p['id'], p['par'], p['par_max']))
if len(set(p['en'] for p in PROD.values())) != len(PROD):
    fallo('B nombres EN repetidos en la tabla maestra')
if M['categorias_d8'] != D8 or M['unidades_d9'] != mapas.UNIDADES_EN:
    fallo('B categorias_d8 / unidades_d9 ≠ mapas.py')
cats_usadas = set(p['categoria_en'] for p in PROD.values())
if len([F for F in FALLOS if F.startswith('B ')]) == nb:
    ok('B tabla maestra: 51 productos (50 del 01 en su hoja y fila + cod), B08 en el mismo orden, %d/10 categorías '
       'D8 en uso, unidades ⊂ D9' % len(cats_usadas))

# ---------------------------------------------------------------- C. mismo producto, mismo precio en todos los libros
# (libro, hoja): (columna nombre, columna precio, columna unidad, columna categoría)
COLS = {('01', 'Cocina'): ('B', 'J', 'D', 'C'), ('01', 'Barra'): ('B', 'J', 'D', 'C'),
        ('01', 'Almacén'): ('B', 'J', 'D', 'C'), ('B08', 'Conteo Rápido'): ('B', 'E', 'D', 'C'),
        ('02', 'Comparativa Precios'): ('B', None, 'C', None), ('03', 'Pedido Actual'): ('B', 'F', 'D', 'C'),
        ('04', 'Control Recepción'): ('D', 'L', None, 'E'), ('05', 'Registro Diario Mermas'): ('B', 'F', 'E', 'C'),
        ('06', 'Control FIFO'): ('B', 'P', 'O', 'C'), ('07', 'Top 20 Productos'): ('B', 'I', 'D', 'C'),
        ('B09', 'Calculadora'): ('B', 'I', None, 'C')}
nc = len(FALLOS)
apariciones = defaultdict(set)
nceldas = 0
for (libro, hoja), (cn, cp, cu, cc) in COLS.items():
    for ref, val in C[libro][hoja].items():
        mt = re.match(r'([A-Z]+)(\d+)$', ref)
        if mt.group(1) != cn:
            continue
        fila = mt.group(2)
        p = producto_de(val)
        if p is None:
            fallo('C %s %s!%s: %r no es un producto de la tabla maestra' % (libro, hoja, ref, val))
            continue
        apariciones[p['id']].add(libro)
        nceldas += 1
        if cp and not eq(v(libro, hoja, cp + fila), p['precio']):
            fallo('C %s %s!%s%s: precio %r ≠ maestro %s (%s)' % (libro, hoja, cp, fila, v(libro, hoja, cp + fila),
                                                                 p['precio'], p['id']))
        if cu and v(libro, hoja, cu + fila) != p['unidad']:
            fallo('C %s %s!%s%s: unidad %r ≠ %s' % (libro, hoja, cu, fila, v(libro, hoja, cu + fila), p['unidad']))
        if cc and v(libro, hoja, cc + fila) != p['categoria_en']:
            fallo('C %s %s!%s%s: categoría %r ≠ %s' % (libro, hoja, cc, fila, v(libro, hoja, cc + fila),
                                                       p['categoria_en']))
for libro, hoja in (('01', 'Cocina'), ('01', 'Barra'), ('01', 'Almacén')):
    for ref, val in C[libro][hoja].items():
        if ref.startswith('E') or ref.startswith('F'):
            p = producto_de(v(libro, hoja, 'B' + ref[1:]))
            if p and val != (p['par'] if ref[0] == 'E' else p['par_max']):
                fallo('C %s %s!%s: par %r ≠ maestro' % (libro, hoja, ref, val))
# todas las unidades y categorías escritas en celdas de producto están en D9 / D8
for libro in C:
    for hoja in C[libro]:
        for ref, val in C[libro][hoja].items():
            k = COLS.get((libro, hoja))
            if k and k[2] and ref.startswith(k[2]) and re.match(r'[A-Z]+\d+$', ref) and \
                    re.match(r'([A-Z]+)', ref).group(1) == k[2] and val not in D9:
                fallo('C %s %s!%s: unidad %r fuera de D9' % (libro, hoja, ref, val))
for ref, val in C['05']['Plan de Acción'].items():
    if ref.startswith('B') and val not in D8:
        fallo('C 05 Plan!%s: categoría %r fuera de D8' % (ref, val))
for i in range(6):
    if v('02', 'Directorio Proveedores', 'C%d' % (4 + i)) not in D8:
        fallo('C 02 Directorio!C%d fuera de D8' % (4 + i))
if len(FALLOS) == nc:
    ok('C mismo precio/unidad/categoría: %d celdas de producto en %d libros; productos en ≥ 2 libros: %d; par levels '
       'del 01 = maestro' % (nceldas, len(set(b for s in apariciones.values() for b in s)),
                             sum(1 for s in apariciones.values() if len(s) >= 2)))

# ---------------------------------------------------------------- D. BONUS-09
nd = len(FALLOS)
par = M['parametros_b09']
for f in range(4, 12):
    p = producto_de(v('B09', 'Calculadora', 'B%d' % f))
    d, e, fc = (v('B09', 'Calculadora', c + str(f)) for c in 'DEF')
    vida, kmax, precio = v('B09', 'Calculadora', 'J%d' % f), v('B09', 'Calculadora', 'K%d' % f), \
        v('B09', 'Calculadora', 'I%d' % f)
    rop = d * e + d * fc
    if not eq(rop, p['par'], 1e-6):
        fallo('D B09 fila %d (%s): consumo × (lead + cobertura) = %s ≠ par del 01 %s' % (f, p['id'], rop, p['par']))
    if kmax != p['par_max']:
        fallo('D B09 fila %d (%s): stock máx. %s ≠ par max %s' % (f, p['id'], kmax, p['par_max']))
    eoq = xround(math.sqrt(2 * d * 365 * par['coste_pedido'] / (precio * par['almacenamiento_anual'])), 0)
    cap = xround(d * vida * par['factor_vida_util'], 0)
    sug = min(eoq, cap, kmax)
    r = next(x for x in M['b09'] if x['fila'] == f)
    if (r['eoq'], r['tope_vida_util'], r['sugerida']) != (eoq, cap, sug):
        fallo('D B09 fila %d: EOQ/tope/sugerida %s ≠ recalculado %s' % (
            f, (r['eoq'], r['tope_vida_util'], r['sugerida']), (eoq, cap, sug)))
    if f == 7:
        leche = (d, vida, kmax, eoq, cap, sug)
if (par['coste_pedido'], par['almacenamiento_anual'], par['factor_vida_util']) != (3, 0.25, 0.7):
    fallo('D parámetros ≠ D24 (3 / 0.25 / 0.7)')
if len(FALLOS) == nd:
    ok('D BONUS-09: 8/8 filas con ROP = par del 01 y stock máx. = par max; EOQ/tope/sugerida recalculados; leche '
       '%s gal/día, vida %s, máx. %s → EOQ %d, tope %d, sugerida %d' % leche)

# ---------------------------------------------------------------- E. importes y agregados
ne = len(FALLOS)
precio_de = lambda pid: PROD[pid]['precio'] if pid in PROD else EXTRA[pid]['precio']  # noqa: E731
# 03 pedido actual
sub = sum(v('03', 'Pedido Actual', 'E%d' % f) * v('03', 'Pedido Actual', 'F%d' % f) for f in (9, 10, 11))
prov03 = PROV_EN[v('03', 'Pedido Actual', 'C3')]
if sub < prov03['pedido_minimo']:
    fallo('E 03 pedido de ejemplo %.2f por debajo del mínimo %s (el ES lo supera)' % (sub, prov03['pedido_minimo']))
# 03 historial: subtotal = Σ líneas; total = subtotal + tax; «n lines»
for h in M['identidades']['historial_03']:
    f = h['fila']
    s = round(sum(l['qty'] * precio_de(l['id']) for l in h['lineas']), 2)
    for l in h['lineas']:
        if not eq(l['precio'], precio_de(l['id'])):
            fallo('E 03 historial fila %d: precio de %s ≠ maestro' % (f, l['id']))
    E_, F_, G_ = (v('03', 'Historial Pedidos', c + str(f)) for c in 'EFG')
    if not eq(E_, s) or not eq(G_, E_ + F_):
        fallo('E 03 historial fila %d: E %s ≠ Σ %s o G %s ≠ E + F' % (f, E_, s, G_))
    if v('03', 'Historial Pedidos', 'D%d' % f) != '%d lines' % len(h['lineas']):
        fallo('E 03 historial fila %d: «n lines» no cuadra' % f)
    if F_ != 0:
        fallo('E 03 historial fila %d: impuesto %s ≠ 0 (Tax Rates al 0 %%, D11)' % (f, F_))
# 04 incidencias
L4 = lambda c, f: v('04', 'Control Recepción', '%s%d' % (c, f))  # noqa: E731
I4 = lambda c, f: v('04', 'Registro Incidencias', '%s%d' % (c, f))  # noqa: E731
if not eq(I4('I', 4), (L4('I', 4) - L4('J', 4)) * L4('L', 4)):
    fallo('E 04 incidencia 4: reclamado ≠ faltante × precio')
if not eq(I4('I', 5), L4('J', 5) * L4('L', 5)) or not eq(I4('J', 5), I4('I', 5)):
    fallo('E 04 incidencia 5: partida devuelta ≠ recibido × precio o abono ≠ reclamado')
m6 = re.search(r'Two (\d+) lb cases', I4('F', 6))
if not m6 or not eq(I4('I', 6), 2 * int(m6.group(1)) * L4('L', 6)):
    fallo('E 04 incidencia 6: reclamado ≠ 2 cajas × lb × precio')
for f in (4, 5, 6):
    if I4('B', f) != L4('C', f) or I4('C', f) != L4('B', f) or I4('D', f) != L4('D', f):
        fallo('E 04 incidencia %d: albarán/proveedor/producto ≠ recepción' % f)
m4 = re.match(r'(\d+) lb short of the (\d+) lb', L4('T', 4))
if not m4 or int(m4.group(1)) != L4('I', 4) - L4('J', 4) or int(m4.group(2)) != L4('I', 4):
    fallo('E 04 T4: el texto no cuadra con pedido/recibido')
# 07 Top 20
gasto_cat = OrderedDict((D8[i], v('07', 'Coste por Categoría', 'B%d' % (4 + i))) for i in range(10))
top_cat = defaultdict(float)
for t in M['identidades']['top20_07']:
    f = t['fila']
    p = producto_de(v('07', 'Top 20 Productos', 'B%d' % f))
    if not eq(v('07', 'Top 20 Productos', 'E%d' % f), t['qty_mes'] * p['precio']):
        fallo('E 07 Top 20 fila %d: gasto ≠ cantidad × precio' % f)
    top_cat[p['categoria_en']] += v('07', 'Top 20 Productos', 'E%d' % f)
for cat, g in top_cat.items():
    if g > gasto_cat[cat] + TOL:
        fallo('E 07: Top 20 de %s (%.2f) supera el gasto de la categoría (%s)' % (cat, g, gasto_cat[cat]))
gastos = [v('07', 'Top 20 Productos', 'E%d' % f) for f in range(4, 12)]
if len(set(gastos)) != len(gastos):
    fallo('E 07 Top 20 con gastos repetidos (dispararía el defecto I5)')
subidas = sum(1 for f in range(4, 12)
              if v('07', 'Top 20 Productos', 'I%d' % f) / v('07', 'Top 20 Productos', 'H%d' % f) - 1 > 0.05)
compras = sum(gasto_cat.values())
if v('05', 'Dashboard Mermas', 'B10') != compras:
    fallo('E 05 compras del mes %s ≠ total de enero del 07 %s' % (v('05', 'Dashboard Mermas', 'B10'), compras))
k = {r: v('07', 'Dashboard KPIs', r) for r in ('B12', 'B13', 'B14', 'B15', 'B16', 'B17')}
fc = (k['B14'] + compras - k['B15']) / float(k['B12'])
cpc = (k['B14'] + compras - k['B15'] - gasto_cat['Paper & Cleaning'] - gasto_cat['Other']) / float(k['B13'])
var = compras / float(k['B16']) - 1
if not (0.28 <= fc <= 0.32):
    fallo('E 07 food cost %.2f %% fuera de 28-32 %%' % (100 * fc))
if cpc > 0.3 * k['B17']:
    fallo('E 07 coste por cubierto %.2f > 30 %% del ticket medio' % cpc)
if abs(var) > 0.05:
    fallo('E 07 variación %.2f %% > 5 %%' % (100 * var))
if not eq(k['B17'], k['B12'] / float(k['B13'])):
    fallo('E 07 ticket medio ≠ ventas / cubiertos')
# 05 mermas y objetivo
merm = sum(v('05', 'Registro Diario Mermas', 'D%d' % f) * v('05', 'Registro Diario Mermas', 'F%d' % f)
           for f in (4, 5, 6))
if merm > 0.03 * compras:
    fallo('E 05 mermas de ejemplo %.2f por encima del 3 %% de las compras' % merm)
# 02 comparativa: mejor precio normalizado = precio maestro y es el mínimo
for f in range(4, 14):
    p = producto_de(v('02', 'Comparativa Precios', 'B%d' % f))
    cont = v('02', 'Comparativa Precios', 'E%d' % f)
    packs = [v('02', 'Comparativa Precios', c + str(f)) for c in 'FGHIJ']
    packs = [x for x in packs if x is not None]
    if packs and not eq(min(packs) / float(cont), p['precio']):
        fallo('E 02 comparativa fila %d: mejor %.4f ≠ maestro %s' % (f, min(packs) / float(cont), p['precio']))
# 02 condiciones: «Free over $X» = pedido mínimo del directorio
for i, pv in enumerate(PROV):
    t = v('02', 'Condiciones Comerciales', 'F%d' % (4 + i))
    mm = re.match(r'Free over \$([\d,]+)$', t)
    if mm and int(mm.group(1).replace(',', '')) != pv['pedido_minimo']:
        fallo('E 02 condiciones F%d: %r ≠ mínimo %s' % (4 + i, t, pv['pedido_minimo']))
    if v('02', 'Directorio Proveedores', 'N%d' % (4 + i)) != pv['pedido_minimo'] or \
            v('03', 'Proveedores', 'E%d' % (4 + i)) != pv['pedido_minimo']:
        fallo('E pedido mínimo del proveedor %d distinto entre 02 y 03' % (i + 1))
# evaluación del proveedor 6 = «Grade D (2.2/5)»
if 'Grade D (2.2/5)' not in PROV[5]['notas_directorio']:
    fallo('E ProClean: la nota D (2.2/5) no coincide con su evaluación (2,3,2,2,2)')
if len(FALLOS) == ne:
    ok('E importes: pedido 03 %.2f ≥ mínimo %s; historial 3/3 = Σ líneas (tax 0); incidencias 04 %s / %s / %s; Top 20 = '
       'qty × precio y ≤ su categoría; compras enero %s = 05 B10; food cost %.2f %%, coste/cubierto %.2f ≤ %.2f, '
       'variación %.2f %%, %d subidas > 5 %%; mermas %.2f (%.2f %% < 3 %%); comparativa 3/3 y «Free over» 4/4' % (
           sub, prov03['pedido_minimo'], I4('I', 4), I4('I', 5), I4('I', 6), compras, 100 * fc, cpc, 0.3 * k['B17'],
           100 * var, subidas, merm, 100 * merm / compras))

# ---------------------------------------------------------------- F. estados
nf = len(FALLOS)
FAM = {x[0]: x for x in mapas.FAMILIAS.values()}
esperado04 = ['✓ ACCEPT', '✗ REJECT (too warm)', '✓ ACCEPT', 'N/A']
for f, exp in zip((4, 5, 6, 7), esperado04):
    fam = L4('G', f)
    if fam not in FAM:
        fallo('F 04 fila %d: familia %r no está en mapas.FAMILIAS' % (f, fam))
        continue
    _, mn, mx, _, _ = FAM[fam]
    t = L4('O', f)
    got = 'N/A' if mx == 'N/A' else ('✗ REJECT (too cold)' if t < mn else ('✓ ACCEPT' if t <= mx else
                                                                            '✗ REJECT (too warm)'))
    if got != exp:
        fallo('F 04 fila %d: %s a %s °F da %s (esperado %s)' % (f, fam, t, got, exp))
    cat = L4('E', f)
    if f < 7 and mapas.FAMILIA_POR_CATEGORIA[cat] != fam:
        fallo('F 04 fila %d: familia %r ≠ la sugerida por la categoría' % (f, fam))
OFF = {(x['hoja_es'], x['celda']): x['desfase'] for x in M['fechas_hoy']}
est06 = []
for f in range(5, 11):
    g = OFF[('Control FIFO', 'G%d' % f)]
    h = OFF.get(('Control FIFO', 'H%d' % f))
    i = v('06', 'Control FIFO', 'I%d' % f)
    lim = g if h is None or i is None else min(g, h + i)
    tipo = v('06', 'Control FIFO', 'F%d' % f)
    if lim < 0:
        est06.append('CHECK' if tipo == 'Best-by' else 'EXPIRED')
    else:
        est06.append('URGENT' if lim <= 2 else ('SOON' if lim <= 7 else 'OK'))
if set(est06) != {'EXPIRED', 'CHECK', 'URGENT', 'SOON', 'OK'}:
    fallo('F 06: estados hoy %s (faltan de los 5)' % est06)
if tipo not in dict(mapas.DV_LISTAS['tipo_fecha']).values():
    fallo('F 06: tipo de fecha fuera de la DV')
for f in range(5, 11):
    if v('06', 'Control FIFO', 'R%d' % f) not in mapas.ZONAS.values():
        fallo('F 06 R%d: zona fuera de mapas.ZONAS' % f)
est02 = ['EXPIRED' if OFF[('Comparativa Precios', 'O%d' % f)] < 0 else
         ('this week' if OFF[('Comparativa Precios', 'O%d' % f)] <= 7 else 'current') for f in (4, 7, 8)]
if len(FALLOS) == nf:
    ok('F estados: 04 = ACCEPT / REJECT (too warm) / ACCEPT / N/A; 06 hoy = %s; 02 cotizaciones = %s' % (
        ' · '.join(est06), ' · '.join(est02)))

# ---------------------------------------------------------------- G. D25 y D20
ng = len(FALLOS)
ESPERADAS = {('06', 'Control FIFO', c) for c in
             ['E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'H9']} | \
            {('02', 'Comparativa Precios', c) for c in ['N4', 'O4', 'N7', 'O7', 'N8', 'O8']}
got = {(x['libro'], x['hoja_es'], x['celda']) for x in M['fechas_hoy']}
if got != ESPERADAS or len(M['fechas_hoy']) != 19:
    fallo('G D25: celdas %s ≠ las 19 de la SPEC' % sorted(got ^ ESPERADAS))
REF = dt.date(2026, 8, 24)
for x in M['fechas_hoy']:
    k_ = (dt.date(*map(int, x['fecha_es'].split('-'))) - REF).days
    if x['desfase'] != k_ or x['formula'] != ('=TODAY()%+d' % k_ if k_ else '=TODAY()') or x['numFmtId'] != 14:
        fallo('G D25 %s!%s: fórmula %s ≠ desfase %d' % (x['hoja_en'], x['celda'], x['formula'], k_))
D20 = {('01', 'Instructions', 'A20'), ('03', 'Instructions', 'A10'), ('04', 'Instructions', 'A7'),
       ('04', 'Instructions', 'A8'), ('04', 'Receiving Temps', 'G15'), ('05', 'Instructions', 'A8'),
       ('05', 'Instructions', 'A10'), ('05', 'Waste Dashboard', 'A13'), ('07', 'Instructions', 'A7'),
       ('07', 'KPI Dashboard', 'A19'), ('B08', 'Instructions', 'A14'), ('B09', 'Instructions', 'A19'),
       ('B09', 'Instructions', 'A21')}
tcd = {(x['book'], x['sheet'], x['cell']): x for x in M['textos_cifra_derivada']}
if set(tcd) != D20:
    fallo('G D20: celdas %s ≠ lista de la SPEC' % sorted(set(tcd) ^ D20))
for key, x in tcd.items():
    if not x.get('calc') or not x.get('en'):
        fallo('G D20 %s: sin en o sin calc' % (key,))
need = {('07', 'KPI Dashboard', 'A19'): ['{:,}'.format(compras), '{:,}'.format(k['B12']), '{:,}'.format(k['B13']),
                                          '%.1f%%' % (100 * fc)],
        ('B09', 'Instructions', 'A19'): ['%s gal a day' % leche[0], '%s-day' % leche[1], '%s gal.' % leche[5],
                                         'at %d gal' % leche[3], 'to %d gal' % leche[4]],
        ('03', 'Instructions', 'A10'): ['rows 40 to 42', 'row 43', 'Rows 45 to 48', '0%, 5% and 20%'],
        ('01', 'Instructions', 'A20'): ['row 44', 'row 34'], ('B08', 'Instructions', 'A14'): ['row 84'],
        ('05', 'Instructions', 'A10'): ['3%'], ('05', 'Instructions', 'A8'): ['3%'],
        ('04', 'Instructions', 'A8'): ['ACCEPT', 'REJECT (too warm)', 'REJECT (too cold)', 'NO LIMIT FOR THIS FAMILY']}
for key, frags in need.items():
    for fr in frags:
        if key in tcd and fr not in tcd[key]['en']:
            fallo('G D20 %s: falta «%s»' % (key, fr))
if len(FALLOS) == ng:
    ok('G D25: 19/19 celdas =TODAY()±k (ref. 24-ago-2026, numFmtId 14); D20: 13/13 celdas con cifra EN y cálculo')

# ---------------------------------------------------------------- H. localizar
nh = len(FALLOS)
gl = OrderedDict((c['id'], c['es']) for c in T['cadenas'] if c.get('tratamiento') == 'localizar')
loc = OrderedDict((x['id'], x) for x in M['localizar'])
if list(gl) != list(loc):
    fallo('H localizar: ids %s' % sorted(set(gl) ^ set(loc)))
for i, x in loc.items():
    if gl.get(i) != x['es']:
        fallo('H %s: ES distinto de textos_es.json' % i)
    if not x['en'].strip():
        fallo('H %s: EN vacío' % i)
for p in PROD.values():
    for x in loc.values():
        if x['es'] == p['es'] and x['en'] != p['en']:
            fallo('H %s: EN %r ≠ tabla maestra %r' % (x['id'], x['en'], p['en']))
for pv in PROV:
    x = [y for y in loc.values() if y['es'] == pv['es']]
    if not x or x[0]['en'] != pv['en']:
        fallo('H proveedor %r sin EN coherente' % pv['es'])
# cada producto «(ejemplo)» se localiza como el producto de la tabla + « (sample)»
for x in loc.values():
    if x['es'].endswith('(ejemplo)') and not x['en'].endswith('(sample)'):
        fallo('H %s: «(ejemplo)» sin «(sample)»' % x['id'])
    if x['es'].endswith('(ejemplo)'):
        base = x['es'][:-len(' (ejemplo)')]
        p = next((q for q in PROD.values() if q['es'] == base), None)
        if p and producto_de(x['en']) is not p:
            fallo('H %s: %r no casa con la tabla maestra (%s)' % (x['id'], x['en'], p['en']))
if len(FALLOS) == nh:
    ok('H localizar: %d/%d cadenas GL-mercado, mismos ids y ES; productos y proveedores = tabla maestra' % (
        len(loc), len(gl)))

# ---------------------------------------------------------------- I. D15 y limpieza de texto
ni = len(FALLOS)
for i, pv in enumerate(PROV):
    if not re.match(r'^\(555\) 555-01\d\d$', pv['telefono']):
        fallo('I proveedor %d: teléfono %r' % (i + 1, pv['telefono']))
    for t in (pv['email'], pv['contacto_incidencias']):
        for mail in re.findall(r'[\w.+-]+@[\w.-]+', t):
            if not mail.endswith('.example'):
                fallo('I proveedor %d: correo %r fuera de .example' % (i + 1, mail))
        for tel in re.findall(r'\(\d{3}\) \d{3}-\d{4}', t):
            if not re.match(r'\(555\) 555-01\d\d', tel):
                fallo('I proveedor %d: teléfono %r' % (i + 1, tel))
    if not re.match(r'^00-000000%d$' % (i + 1), pv['tax_id']):
        fallo('I proveedor %d: Tax ID %r' % (i + 1, pv['tax_id']))
    if 'Anytown' not in pv['direccion'] or not pv['en'].endswith('(sample)'):
        fallo('I proveedor %d: dirección sin Anytown o nombre sin «(sample)»' % (i + 1))
if [p['condiciones_pago'] for p in PROV][:3] != ['Net 30', 'Net 15', 'COD']:
    fallo('I condiciones de pago ≠ Net 30 / Net 15 / COD')

NO_LATINO = re.compile(r'[Ѐ-ӿ֐-׿؀-ۿ฀-๿ᄀ-ᇿ぀-ヿ㐀-鿿가-힯]')
ES_CAR = re.compile(r'[ñÑáéíóúÁÉÍÓÚ¿¡]')
_PAL = ['de', 'del', 'la', 'las', 'los', 'el', 'con', 'para', 'por', 'sin', 'una', 'uno', 'caja', 'saco', 'ejemplo',
        'proveedor', 'precio', 'merma', 'albarán', 'pedido', 'cámara', 'lote', 'según', 'también', 'más', 'días',
        'fecha', 'factura']
# sensible a mayúsculas: «y» minúscula es español; «Y» es el ítem EN de la DV Approved (Y/N/Pending)
ES_PAL = re.compile(r'\b(' + '|'.join(_PAL + [w.capitalize() for w in _PAL]) + r'|y|IVA|APPCC)\b')
MONEDA = re.compile(r'€|\bEUR\b')
textos_en = []
for lst in M['libros'].values():
    textos_en += [('libros %s!%s' % (c['hoja_en'], c['celda']), c['valor']) for c in lst if isinstance(c['valor'], str)]
textos_en += [('localizar ' + x['id'], x['en']) for x in M['localizar']]
textos_en += [('d20 %s %s' % (x['sheet'], x['cell']), x['en']) for x in M['textos_cifra_derivada']]
textos_en += [('producto ' + p['id'], p['en']) for p in list(PROD.values()) + list(EXTRA.values())]
textos_en += [('producto ' + p['id'], p['formato_compra']) for p in PROD.values()]
for pv in PROV:
    textos_en += [('proveedor %s' % k_, pv[k_]) for k_ in pv if k_ != 'es' and isinstance(pv[k_], str)]
BLANCA = re.compile(r'(?i)parmesan|arborio')
for donde, t in textos_en:
    limpio = BLANCA.sub('', t)
    if MONEDA.search(t):
        fallo('I %s: moneda € / EUR en %r' % (donde, t))
    if NO_LATINO.search(t):
        fallo('I %s: carácter no latino en %r' % (donde, t))
    if ES_CAR.search(limpio) or ES_PAL.search(limpio):
        fallo('I %s: resto de español en %r' % (donde, t))
if len(FALLOS) == ni:
    ok('I D15: 6 proveedores con (555) 555-01xx, correos .example, Tax ID 00-000000n, Anytown; texto EN: %d valores sin '
       '€/EUR, sin no latinos y sin restos de español' % len(textos_en))

# ---------------------------------------------------------------- resumen
for o in OKS:
    print('OK   ' + o)
for f_ in FALLOS:
    print('FALLO ' + f_)
print('validar_mercado.py: %d comprobaciones en verde · %d fallos' % (len(OKS), len(FALLOS)))
sys.exit(1 if FALLOS else 0)
