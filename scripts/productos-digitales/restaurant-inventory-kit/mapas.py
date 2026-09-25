#!/usr/bin/env python3
"""
mapas.py — Restaurant Inventory Kit Pro (EN) · mapas ES→EN del Kit de Inventario v2.0.

SPEC: `scripts/productos-digitales/restaurant-inventory-kit/SPEC.md` (D1-D24).
Importable SIN efectos (solo constantes y funciones). Ejecutado como script corre el autotest
(nombres de pestaña ≤ 31 caracteres y sin caracteres prohibidos, listas de DV ≤ 255 caracteres y
sin comas dentro de un ítem, tokens de CF sin colisiones) y, si existe `censo_es.json` al lado,
comprueba que TODAS las pestañas, listas de DV y literales del censo tienen su EN.

    python3 mapas.py

Contenido:
  · PRODUCTO / SLUG / URL_PRODUCTO / VERSION_ES        (D1, D2, D21)
  · FICHEROS, TITULOS                                   nombres de fichero y título interior (D5)
  · HOJAS, HOJAS_ES_POR_LIBRO                           pestañas ES→EN (D6)
  · CATEGORIAS, UNIDADES, LISTA_UNIDADES_EN             claves-dato (D8, D9)
  · DV_LISTAS                                           resto de listas literales de DV (D8)
  · FAMILIAS                                            las 15 familias de recepción → FDA Food Code (D12)
  · ZONAS                                               las 11 zonas del Mapa Almacén (D12)
  · MESES_CORTOS / MESES_LARGOS / PERIODO_ANIO          07 (D8)
  · LITERALES / LITERALES_SIN_CAMBIO                    literales de fórmula (D10)
  · TOKENS_CF                                           cadenas que buscan las CF containsText (D10)
"""
import json
import os
import re
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))

# ==========================================================================
# 0. Producto (D1, D2, D21)
# ==========================================================================
PRODUCTO = 'Restaurant Inventory Kit Pro'
SLUG = 'restaurant-inventory-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
VERSION_ES = '2.0'

# ==========================================================================
# 1. Ficheros y títulos (D5: intención de búsqueda, no traducción literal)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-inventario-stock-diario.xlsx', '01-kitchen-bar-inventory-par-sheet.xlsx'),
    ('02-fichas-proveedores.xlsx', '02-vendor-list-price-comparison.xlsx'),
    ('03-pedidos-compra.xlsx', '03-purchase-order-template.xlsx'),
    ('04-recepcion-mercancias.xlsx', '04-receiving-log.xlsx'),
    ('05-control-mermas.xlsx', '05-food-waste-log.xlsx'),
    ('06-fifo-caducidades.xlsx', '06-fifo-expiration-date-tracker.xlsx'),
    ('07-analisis-costes-compras.xlsx', '07-purchasing-cost-analysis.xlsx'),
    ('BONUS-08-inventario-rapido-mensual.xlsx', 'BONUS-08-month-end-inventory-count.xlsx'),
    ('BONUS-09-calculadora-punto-pedido.xlsx', 'BONUS-09-reorder-point-calculator.xlsx'),
])
LIBROS_ES = list(FICHEROS)

TITULOS = OrderedDict([
    ('01-kitchen-bar-inventory-par-sheet.xlsx', 'Kitchen & Bar Inventory Sheet with Par Levels'),
    ('02-vendor-list-price-comparison.xlsx', 'Vendor List, Price Comparison & Scorecard'),
    ('03-purchase-order-template.xlsx', 'Purchase Order Template & Order Log'),
    ('04-receiving-log.xlsx', 'Receiving Log (Temperatures & Credit Requests)'),
    ('05-food-waste-log.xlsx', 'Food Waste Log & Action Plan'),
    ('06-fifo-expiration-date-tracker.xlsx', 'FIFO & Expiration Date Tracker'),
    ('07-purchasing-cost-analysis.xlsx', 'Purchasing Cost Analysis & Food Cost KPIs'),
    ('BONUS-08-month-end-inventory-count.xlsx', 'BONUS: Month-End Inventory Count'),
    ('BONUS-09-reorder-point-calculator.xlsx', 'BONUS: Reorder Point & Order Quantity Calculator'),
])

# ==========================================================================
# 2. Pestañas (D6). Clave = nombre ES exacto; valor = nombre EN (≤ 31, sin []:*?/\)
# ==========================================================================
HOJAS = OrderedDict([
    ('Instrucciones', 'Instructions'),
    # 01
    ('Cocina', 'Kitchen'),
    ('Barra', 'Bar'),
    ('Almacén', 'Storeroom'),
    ('Resumen Dashboard', 'Summary Dashboard'),
    # 02
    ('Directorio Proveedores', 'Vendor Directory'),
    ('Comparativa Precios', 'Price Comparison'),
    ('Evaluación Proveedores', 'Vendor Scorecard'),
    ('Condiciones Comerciales', 'Vendor Terms'),
    # 03
    ('Pedido Actual', 'Current Order'),
    ('Proveedores', 'Vendors'),
    ('Historial Pedidos', 'Order Log'),
    ('Listas', 'Tax Rates'),
    # 04
    ('Control Recepción', 'Receiving Log'),
    ('Registro Incidencias', 'Discrepancy Log'),
    ('Verificación Temperaturas', 'Receiving Temps'),
    # 05
    ('Registro Diario Mermas', 'Daily Waste Log'),
    ('Análisis por Categoría', 'Waste by Category'),
    ('Dashboard Mermas', 'Waste Dashboard'),
    ('Plan de Acción', 'Action Plan'),
    # 06
    ('Control FIFO', 'FIFO Tracker'),
    ('Alertas Caducidad', 'Expiration Alerts'),
    ('Mapa Almacén', 'Storage Map'),
    # 07
    ('Coste por Categoría', 'Spend by Category'),
    ('Evolución Mensual', 'Monthly Trend'),
    ('Top 20 Productos', 'Top 20 Items'),
    ('Dashboard KPIs', 'KPI Dashboard'),
    # BONUS-08
    ('Conteo Rápido', 'Quick Count'),
    # BONUS-09
    ('Calculadora', 'Reorder Calculator'),
    ('Parámetros', 'Parameters'),
])

HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01-inventario-stock-diario.xlsx', ['Instrucciones', 'Cocina', 'Barra', 'Almacén', 'Resumen Dashboard']),
    ('02-fichas-proveedores.xlsx', ['Instrucciones', 'Directorio Proveedores', 'Comparativa Precios',
                                    'Evaluación Proveedores', 'Condiciones Comerciales']),
    ('03-pedidos-compra.xlsx', ['Instrucciones', 'Pedido Actual', 'Proveedores', 'Historial Pedidos', 'Listas']),
    ('04-recepcion-mercancias.xlsx', ['Instrucciones', 'Control Recepción', 'Registro Incidencias',
                                      'Verificación Temperaturas']),
    ('05-control-mermas.xlsx', ['Instrucciones', 'Registro Diario Mermas', 'Análisis por Categoría',
                                'Dashboard Mermas', 'Plan de Acción']),
    ('06-fifo-caducidades.xlsx', ['Instrucciones', 'Control FIFO', 'Alertas Caducidad', 'Mapa Almacén']),
    ('07-analisis-costes-compras.xlsx', ['Instrucciones', 'Coste por Categoría', 'Evolución Mensual',
                                         'Top 20 Productos', 'Dashboard KPIs']),
    ('BONUS-08-inventario-rapido-mensual.xlsx', ['Instrucciones', 'Conteo Rápido']),
    ('BONUS-09-calculadora-punto-pedido.xlsx', ['Instrucciones', 'Calculadora', 'Parámetros']),
])
HOJA_PROHIBIDOS = set('[]:*?/\\')

# ==========================================================================
# 3. Claves-dato (D8, D9). Un ítem de lista de DV NUNCA lleva coma.
# ==========================================================================
CATEGORIAS = OrderedDict([
    ('Cárnicos', 'Meat & Poultry'),
    ('Pescados', 'Seafood'),
    ('Lácteos', 'Dairy & Eggs'),
    ('Verduras/Frutas', 'Produce'),
    ('Secos/Granos', 'Dry Goods'),
    ('Congelados', 'Frozen'),
    ('Bebidas Alcohólicas', 'Alcoholic Beverages'),
    ('Bebidas No Alcohólicas', 'Non-Alcoholic Beverages'),
    ('Limpieza', 'Paper & Cleaning'),
    ('Otros', 'Other'),
])

# Unidad ES → unidad EN POR DEFECTO de la traducción literal. Los datos de ejemplo NO usan este mapa:
# cada producto lleva su unidad US en la tabla maestra (D9, D14). Sirve para textos y validaciones.
UNIDADES = OrderedDict([
    ('kg', 'kg'), ('L', 'L'), ('ud', 'each'), ('docena', 'dozen'), ('caja', 'case'),
    ('bandeja', 'tray'), ('barril', 'keg'), ('saco', 'bag'), ('rollo', 'roll'), ('paquete', 'pack'),
])
LISTA_UNIDADES_EN = 'lb,oz,kg,gal,qt,L,each,dozen,case,tray,keg,bag,roll,pack,bottle,can'
UNIDADES_EN = LISTA_UNIDADES_EN.split(',')

DV_LISTAS = OrderedDict([
    ('homologado', OrderedDict([('S', 'Y'), ('N', 'N'), ('Pendiente', 'Pending')])),
    ('estado_pedido', OrderedDict([
        ('Borrador', 'Draft'), ('Enviado', 'Sent'), ('Confirmado', 'Confirmed'), ('Recibido', 'Received'),
        ('Recibido con incidencia', 'Received with issues'), ('Facturado', 'Invoiced')])),
    ('marca', OrderedDict([('✓', '✓'), ('✗', '✗'), ('—', '—')])),
    ('tipo_incidencia', OrderedDict([
        ('Cantidad incorrecta', 'Wrong quantity'),
        ('Temperatura fuera de rango', 'Temperature out of range'),
        ('Producto en mal estado', 'Poor condition'),
        ('Caducidad demasiado corta', 'Short shelf life'),
        ('Producto no solicitado', 'Not ordered'),
        ('Precio distinto al pactado', 'Price differs from quote'),
        ('Falta el lote o el albarán', 'Missing lot no. or invoice')])),
    ('estado_incidencia', OrderedDict([
        ('Abierta', 'Open'), ('Reclamada', 'Claimed'), ('Abono recibido', 'Credit received'),
        ('Cerrada sin abono', 'Closed without credit'), ('Cerrada', 'Closed')])),
    ('motivo_merma', OrderedDict([
        ('Caducidad superada', 'Past use-by date'),
        ('Mal estado en recepción', 'Poor condition on arrival'),
        ('Rotura o derrame', 'Breakage or spill'),
        ('Error de elaboración', 'Prep error'),
        ('Sobreproducción', 'Overproduction'),
        ('Devolución de cliente', 'Customer return'),
        ('Cadena de frío rota', 'Cold chain failure'),
        ('Merma de despiece', 'Butchery trim loss'),
        ('Plato cambiado o rechazado', 'Dish sent back'),
        ('Descuadre sin justificar', 'Unexplained variance')])),
    ('prioridad', OrderedDict([('Alta', 'High'), ('Media', 'Medium'), ('Baja', 'Low')])),
    ('estado_plan', OrderedDict([
        ('Pendiente', 'Pending'), ('En curso', 'In progress'), ('Implantada', 'Implemented'),
        ('Verificada', 'Verified'), ('Descartada', 'Dropped')])),
    ('tipo_fecha', OrderedDict([('Caducidad', 'Use-by'), ('Consumo preferente', 'Best-by')])),
])

# 04 · las 15 filas de 'Verificación Temperaturas'!A4:A18 (el rango de la DV y del VLOOKUP no cambia).
# OJO: es una REESCRITURA POR FILA (la fila n del ES pasa a ser la familia n del EN), no una traducción:
# las familias de la UE (7/3/4/2 °C) se funden en el Food Code (41 °F para casi todo) y entran familias
# que el ES no tiene (shellstock, comida recibida en caliente). Donde una celda de ejemplo del ES cite
# una familia por su nombre, vale el mapa (p. ej. «Pescado fresco y marisco» → «Fresh fish & …»).
# (familia EN, mín °F, máx °F, texto «ideal», base normativa). 'N/A' = no se controla por temperatura.
# Etiquetas: [fuente] FDA Food Code 2022 · [estimado] práctica del sector (ver SPEC D12).
FAMILIAS = OrderedDict([
    ('Canal y despiece de ungulados domésticos',
     ('Raw beef, pork & lamb', 30, 41, '41 °F (5 °C) or below', 'FDA Food Code 2022 §3-202.11(A) [fuente]; min [estimado]')),
    ('Despojos comestibles',
     ('Ground & variety meats', 30, 41, '41 °F (5 °C) or below', 'FDA Food Code 2022 §3-202.11(A) [fuente]')),
    ('Aves y lagomorfos',
     ('Raw poultry', 30, 41, '41 °F (5 °C) or below', 'FDA Food Code 2022 §3-202.11(A) [fuente]')),
    ('Preparados de carne',
     ('Marinated & processed raw meat', 30, 41, '41 °F (5 °C) or below', 'FDA Food Code 2022 §3-202.11(A) [fuente]')),
    ('Carne picada',
     ('Live shellfish (shellstock)', 32, 45, '45 °F (7 °C) air temp or below', 'FDA Food Code 2022 §3-202.11(B); NSSP [fuente]')),
    ('Pescado fresco y marisco',
     ('Fresh fish & shucked shellfish', 30, 41, '41 °F (5 °C) or below, on ice', 'FDA Food Code 2022 §3-202.11(A) [fuente]')),
    ('Congelados',
     ('Frozen food', -40, 0, 'Frozen solid, 0 °F (-18 °C) or below', 'FDA Food Code 2022 §3-202.11(E) «received frozen» [fuente]; 0 °F [estimado]')),
    ('Comidas preparadas refrigeradas (más de 24 h)',
     ('Cold ready-to-eat TCS food', 30, 41, '41 °F (5 °C) or below', 'FDA Food Code 2022 §3-202.11(A) [fuente]')),
    ('Comidas preparadas refrigeradas (menos de 24 h)',
     ('Hot TCS food (received hot)', 135, 212, '135 °F (57 °C) or above', 'FDA Food Code 2022 §3-202.11(D) [fuente]; max = límite físico')),
    ('Lácteos y otros refrigerados',
     ('Dairy & other refrigerated TCS', 30, 41, '41 °F (5 °C) or below; fluid milk up to 45 °F', 'FDA Food Code 2022 §3-202.11(A)-(B) [fuente]')),
    ('Frutas y verduras',
     ('Whole produce', 32, 54, '32-54 °F (0-12 °C), per item', 'No legal limit; industry practice [estimado]')),
    ('Huevos',
     ('Shell eggs', 30, 45, '45 °F (7 °C) air temp or below', 'FDA Food Code 2022 §3-202.11(C); 21 CFR 118.4(e) [fuente]')),
    ('Secos y economato (ambiente)',
     ('Dry & canned goods (ambient)', 'N/A', 'N/A', 'Cool and dry, 50-70 °F (10-21 °C)', 'FDA Food Code 2022 §3-202.15 package integrity [fuente]; range [estimado]')),
    ('Bebidas y conservas (ambiente)',
     ('Beverages (ambient)', 'N/A', 'N/A', 'Cool and dry; draft beer kegs 34-38 °F (1-3 °C)', 'No legal limit; follow the manufacturer [estimado]')),
    ('No alimentario (limpieza, menaje y desechables)',
     ('Non-food (cleaning & disposables)', 'N/A', 'N/A', 'Ambient, stored away from food', 'FDA Food Code 2022 §7-201.11 [fuente]')),
])

# 04 · 'Verificación Temperaturas'!G4:H13 · categoría → familia por defecto (EN)
FAMILIA_POR_CATEGORIA = OrderedDict([
    ('Meat & Poultry', 'Raw beef, pork & lamb'),
    ('Seafood', 'Fresh fish & shucked shellfish'),
    ('Dairy & Eggs', 'Dairy & other refrigerated TCS'),
    ('Produce', 'Whole produce'),
    ('Dry Goods', 'Dry & canned goods (ambient)'),
    ('Frozen', 'Frozen food'),
    ('Alcoholic Beverages', 'Beverages (ambient)'),
    ('Non-Alcoholic Beverages', 'Beverages (ambient)'),
    ('Paper & Cleaning', 'Non-food (cleaning & disposables)'),
    ('Other', 'Dry & canned goods (ambient)'),
])

# 06 · zonas de 'Mapa Almacén'!A4:A14 (= lista de la DV R5:R54)
ZONAS = OrderedDict([
    ('Cámara crudos', 'Raw meat cooler'),
    ('Cámara pescado', 'Seafood cooler'),
    ('Cámara elaborados', 'Prepared foods cooler'),
    ('Cámara verduras', 'Produce cooler'),
    ('Congelador', 'Walk-in freezer'),
    ('Descongelación', 'Thawing shelf'),
    ('Economato seco', 'Dry storage'),
    ('Bodega', 'Wine & liquor storage'),
    ('Residuos', 'Trash & recycling'),
    ('Huevera', 'Dairy & egg cooler'),
    ('Almacén de químicos', 'Chemical storage'),
])

MESES_CORTOS = OrderedDict(zip('Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic'.split(),
                               'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()))
MESES_LARGOS = OrderedDict(zip(
    'Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre Octubre Noviembre Diciembre'.split(),
    'January February March April May June July August September October November December'.split()))
PERIODO_ANIO = ('Año completo', 'Full year')


def dv_lista(valores):
    return '"' + ','.join(valores) + '"'


# ==========================================================================
# 4. Literales de fórmula (D10). Se traducen IGUAL en fórmulas, CF y DV.
# ==========================================================================
LITERALES = OrderedDict([
    # 01
    ('🔴 PEDIR', '🔴 REORDER'), ('\U0001f7e1 BAJO', '\U0001f7e1 LOW'), ('*BAJO*', '*LOW*'), ('*PEDIR*', '*REORDER*'),
    # 02
    ('Prov. 1', 'Vendor 1'), ('Prov. 2', 'Vendor 2'), ('Prov. 3', 'Vendor 3'), ('Prov. 4', 'Vendor 4'),
    ('Prov. 5', 'Vendor 5'),
    ('⚠ falta contenido', '⚠ missing pack size'),
    ('⛔ COTIZACIÓN VENCIDA', '⛔ QUOTE EXPIRED'),
    ('\U0001f7e1 vence esta semana', '\U0001f7e1 expires this week'),
    ('\U0001f7e2 vigente', '\U0001f7e2 current'),
    ('A — Preferente', 'A — Preferred'), ('B — Válido', 'B — Approved'), ('C — Vigilar', 'C — Monitor'),
    ('D — Sustituir', 'D — Replace'),
    ('S', 'Y'),
    ('⚠ nota D y sigue homologado: revísalo', '⚠ D grade but still approved: review it'),
    ('\U0001f7e1 nota C: vigílalo, sigue homologado', '\U0001f7e1 C grade: monitor it, still approved'),
    ('✓ coherente', '✓ consistent'),
    # 03, 05, BONUS-08
    ('⚠ falta coste', '⚠ missing cost'),
    ('✓ El pedido supera el mínimo de este proveedor', "✓ This order meets the vendor's minimum"),
    ('⚠ POR DEBAJO DEL PEDIDO MÍNIMO: pueden cobrarte portes',
     '⚠ BELOW THE ORDER MINIMUM: you may be charged a delivery fee'),
    (' líneas', ' lines'),
    ('⚠ faltan compras', '⚠ missing purchases'),
    # 04
    ('⚠ FAMILIA SIN LÍMITE', '⚠ NO LIMIT FOR THIS GROUP'),
    ('✗ RECHAZAR (frío)', '✗ REJECT (too cold)'),
    ('✗ RECHAZAR (calor)', '✗ REJECT (too warm)'),
    ('✓ CONFORME', '✓ ACCEPT'),
    ('*RECHAZAR*', '*REJECT*'),
    # 05, 07
    ('🔴 ALERTA', '🔴 ALERT'), ('\U0001f7e1 REVISAR', '\U0001f7e1 REVIEW'),
    ('— sin mermas registradas —', '— no waste logged —'), (' veces', ' times'),
    # 06
    ('Consumo preferente', 'Best-by'),
    ('⚠ REVISAR (consumo preferente)', '⚠ CHECK (best-by passed)'),
    ('⛔ CADUCADO — RETIRAR', '⛔ EXPIRED — DISCARD'),
    ('🔴 URGENTE', '🔴 URGENT'),
    ('\U0001f7e1 PRÓXIMO', '\U0001f7e1 USE SOON'),
    ('*CADUCADO*', '*EXPIRED*'), ('*REVISAR*', '*CHECK*'), ('*URGENTE*', '*URGENT*'), ('*PRÓXIMO*', '*SOON*'),
    # 07
    ('Año completo', 'Full year'),
])
LITERALES_SIN_CAMBIO = {'', '<>', '—', 'D', 'C', 'N/A', '\U0001f7e2 OK', '*OK*', '>0.05', ' · '}

# CF containsText: token ES → token EN. Cada token EN debe aparecer SOLO en su estado (D10, gate G-CF).
TOKENS_CF = OrderedDict([
    ('PEDIR', 'REORDER'), ('BAJO', 'LOW'), ('OK', 'OK'),
    ('VENCIDA', 'EXPIRED'), ('vence', 'expires'), ('vigente', 'current'),
    ('POR DEBAJO', 'BELOW'), ('supera', 'meets'),
    ('RECHAZAR', 'REJECT'), ('SIN LÍMITE', 'NO LIMIT'), ('CONFORME', 'ACCEPT'),
    ('ALERTA', 'ALERT'), ('REVISAR', 'REVIEW'),
    ('CADUCADO', 'EXPIRED'), ('URGENTE', 'URGENT'), ('PRÓXIMO', 'SOON'),
])
# En 06 el token ES «REVISAR» busca «⚠ REVISAR (consumo preferente)» → en EN «CHECK» (no «REVIEW»).
TOKENS_CF_POR_LIBRO = {'06': {'REVISAR': 'CHECK'}}

# Grupos de estados que comparten una CF (o un COUNTIF) sobre el mismo rango: para el gate de colisiones.
ESTADOS_POR_RANGO = OrderedDict([
    ('01 H', ['🔴 REORDER', '\U0001f7e1 LOW', '\U0001f7e2 OK']),
    ('02 U', ['⛔ QUOTE EXPIRED', '\U0001f7e1 expires this week', '\U0001f7e2 current']),
    ('03 A43', ["✓ This order meets the vendor's minimum",
                '⚠ BELOW THE ORDER MINIMUM: you may be charged a delivery fee']),
    ('04 R', ['⚠ NO LIMIT FOR THIS GROUP', '✗ REJECT (too cold)', '✗ REJECT (too warm)', '✓ ACCEPT', 'N/A']),
    ('05 D', ['\U0001f7e2 OK', '🔴 ALERT', '\U0001f7e1 REVIEW']),
    ('06 L', ['⛔ EXPIRED — DISCARD', '⚠ CHECK (best-by passed)', '🔴 URGENT', '\U0001f7e1 USE SOON',
              '\U0001f7e2 OK']),
    ('07 E', ['\U0001f7e2 OK', '\U0001f7e1 REVIEW', '🔴 ALERT']),
])
TOKENS_EN_POR_RANGO = OrderedDict([
    ('01 H', ['REORDER', 'LOW', 'OK']), ('02 U', ['EXPIRED', 'expires', 'current']),
    ('03 A43', ['BELOW', 'meets']), ('04 R', ['REJECT', 'NO LIMIT', 'ACCEPT']),
    ('05 D', ['ALERT', 'REVIEW', 'OK']), ('06 L', ['EXPIRED', 'URGENT', 'CHECK', 'SOON', 'OK']),
    ('07 E', ['ALERT', 'REVIEW', 'OK']),
])


# ==========================================================================
# 5. Autotest
# ==========================================================================
def todas_las_claves():
    """{texto ES: (tipo, EN)} de todas las claves-dato (para el extractor)."""
    out = OrderedDict()
    for es, en in CATEGORIAS.items():
        out[es] = ('categoria', en)
    for es, en in UNIDADES.items():
        out.setdefault(es, ('unidad', en))
    for nombre, tabla in DV_LISTAS.items():
        for es, en in tabla.items():
            out.setdefault(es, (nombre, en))
    for es, v in FAMILIAS.items():
        out.setdefault(es, ('familia', v[0]))
    for es, en in ZONAS.items():
        out.setdefault(es, ('zona', en))
    for es, en in MESES_CORTOS.items():
        out.setdefault(es, ('mes', en))
    for es, en in MESES_LARGOS.items():
        out.setdefault(es, ('mes', en))
    out.setdefault(PERIODO_ANIO[0], ('periodo', PERIODO_ANIO[1]))
    return out


def autotest():
    err = []
    for es, en in HOJAS.items():
        if len(en) > 31 or set(en) & HOJA_PROHIBIDOS or en.startswith("'"):
            err.append('pestaña inválida: ' + en)
    for f, hs in HOJAS_ES_POR_LIBRO.items():
        ens = [HOJAS[h] for h in hs]
        if len(set(ens)) != len(ens):
            err.append('pestañas EN duplicadas en ' + f)
    listas = [list(CATEGORIAS.values()), UNIDADES_EN, list(ZONAS.values()),
              [PERIODO_ANIO[1]] + list(MESES_CORTOS.values())] + [list(t.values()) for t in DV_LISTAS.values()]
    for lst in listas:
        if any(',' in x for x in lst):
            err.append('coma dentro de un ítem de DV: %r' % lst)
        if len(dv_lista(lst)) > 255:
            err.append('lista DV > 255: %r' % lst)
        if len(set(lst)) != len(lst):
            err.append('ítems duplicados: %r' % lst)
    if len(FAMILIAS) != 15:
        err.append('FAMILIAS debe tener 15 filas (A4:A18)')
    for es, (en, mn, mx, _, _) in FAMILIAS.items():
        if len(en) > 60:
            err.append('familia larga: ' + en)
        if (mn == 'N/A') != (mx == 'N/A') or (mn != 'N/A' and not mn < mx):
            err.append('límites incoherentes: ' + en)
    if set(FAMILIA_POR_CATEGORIA) != set(CATEGORIAS.values()):
        err.append('FAMILIA_POR_CATEGORIA no cubre las 10 categorías')
    fam_en = {v[0] for v in FAMILIAS.values()}
    for c, f in FAMILIA_POR_CATEGORIA.items():
        if f not in fam_en:
            err.append('familia por defecto inexistente: ' + f)
    # colisiones de tokens de CF: cada token casa (SEARCH, sin mayúsculas) solo con su estado
    for rng, estados in ESTADOS_POR_RANGO.items():
        for tok in TOKENS_EN_POR_RANGO[rng]:
            casan = [e for e in estados if tok.lower() in e.lower()]
            if len(casan) != 1 and not (tok == 'REJECT' and len(casan) == 2):
                err.append('token CF %r casa con %r en %s' % (tok, casan, rng))
    return err


def cruzar_censo(p):
    censo = json.load(open(p, encoding='utf-8'))
    err = []
    claves = todas_las_claves()
    for f, info in censo['libros'].items():
        if f not in FICHEROS:
            err.append('libro sin nombre EN: ' + f)
        for h in info['hojas']:
            if h not in HOJAS:
                err.append('pestaña sin EN: %s / %s' % (f, h))
        for h, hd in info['hojas_detalle'].items():
            for dv in hd['dv']:
                f1 = dv['formula1'] or ''
                if f1.startswith('"'):
                    for it in f1.strip('"').split(','):
                        if it not in claves and not re.fullmatch(r'\d+', it):
                            err.append('ítem de DV sin EN: %s / %s / %r' % (f, h, it))
            for lit in list(hd['literales']) + list(hd['literales_cf']):
                if lit not in LITERALES and lit not in LITERALES_SIN_CAMBIO and lit not in TOKENS_CF:
                    err.append('literal sin EN: %s / %s / %r' % (f, h, lit))
    return err


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
    for x in e:
        print('ERROR', x)
    print('mapas.py: {} pestañas · {} categorías · {} unidades EN · {} familias · {} literales · {} errores'.format(
        len(HOJAS), len(CATEGORIAS), len(UNIDADES_EN), len(FAMILIAS), len(LITERALES), len(e)))
    raise SystemExit(1 if e else 0)
