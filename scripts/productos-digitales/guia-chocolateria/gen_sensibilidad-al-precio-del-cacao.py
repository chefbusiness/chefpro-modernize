#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_sensibilidad-al-precio-del-cacao.py — libro 3 de «Cómo Montar una
Chocolatería» (SPEC §2.2, fila 3; constructor C2).

Hojas: Instrucciones · Parámetros · Coste de Cobertura · Escenarios de Precio ·
Repercusión al PVP · Stock y Cobertura de Compra.

QUÉ DECIDE ESTE LIBRO
---------------------
Qué haces cuando el cacao sube un 40 %: subes precio, cambias gramaje, cambias
cobertura o aceptas menos margen. Y, antes de eso, cuál de tus 28 referencias
se rompe la primera.

LA CELDA MÁS CRÍTICA DEL PAQUETE (§3.3, regla «un concepto, una fuente»)
-----------------------------------------------------------------------
El precio de la cobertura vive SÓLO aquí. `CHS-28a` lo publica CON IVA
(25,02 €/kg, bloque de 5 kg a 125,08 €), y un escandallo se calcula con precios
SIN IVA porque el soportado es deducible: con la base equivocada el food cost
sale un 9 % alto. Por eso la hoja «Coste de Cobertura» publica el precio en LAS
DOS BASES y **lo que copian el libro 4 y el libro 7 es la de BASE IMPONIBLE**
(regla 3 de §2.3, ampliada a la materia prima por A-2).

Los cruces 4 <- 3 y 7 <- 3 se materializan en el libro RECEPTOR (celda verde
«trae aquí la cifra de …» + fila de CUADRE, D32): aquí lo que toca es PUBLICAR
la celda en `build/mapa-sensibilidad-al-precio-del-cacao.json` para que C3 y C4
puedan montarlas. **Cero fórmulas que nombren otro fichero.**

DECISIONES TÉCNICAS
-------------------
* Cero constantes dentro de las fórmulas: IVA, food cost objetivo, food cost
  máximo, semanas del año, tipo de interés y volumen viven en «Parámetros», en
  celda verde.
* `IFERROR(...,"")` en toda división; «sin dato» = `""`, nunca `0`; semáforos
  con `ISNUMBER`; DV contra RANGO. Prohibidas INDIRECT, COUNTA, PMT, OFFSET,
  XLOOKUP, LET, LAMBDA, RANK, NETWORKDAYS e IRR: cero usos.
* El porcentaje de cobertura sobre el peso de la pieza de este libro **NO es el
  25 % legal del ap. 1.13** (`CHN-10`): aquél lo calcula el libro 4 con el
  chocolate de la cáscara sobre el peso total. Aquí se mide la EXPOSICIÓN al
  precio del cacao, e incluye la cobertura que va dentro del relleno.
* Las cuatro cajas surtidas no tienen gramaje propio: se COMPONEN de lo que
  llevan dentro. Se prorratean a su cobertura dominante y la diferencia queda
  en «demás materias», de modo que su coste de materia total es el exacto.

Salida fija: build/sensibilidad-al-precio-del-cacao.xlsx
             + build/mapa-sensibilidad-al-precio-del-cacao.json
Uso: /usr/local/bin/python3 gen_sensibilidad-al-precio-del-cacao.py
Via: Claude Code
"""
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Font

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import _comun_chocolateria as C                                # noqa: E402
import _comun_libros_3_5 as X                                  # noqa: E402
import datos_ejemplo as D                                      # noqa: E402
import motor                                                   # noqa: E402

NOMBRE = 'sensibilidad-al-precio-del-cacao'
TITULO = 'Sensibilidad al Precio del Cacao'

H_INS = 'Instrucciones'
H_PAR = 'Parámetros'
H_COB = 'Coste de Cobertura'
H_ESC = 'Escenarios de Precio'
H_REP = 'Repercusión al PVP'
H_STK = 'Stock y Cobertura de Compra'

QPAR = "'" + H_PAR + "'!"
QCOB = "'" + H_COB + "'!"
QESC = "'" + H_ESC + "'!"

N = motor.NARROW

# --- Parámetros: coordenadas ----------------------------------------------
P_IVACOB = 'B6'
P_IVAPVP = 'B7'
P_FC = 'B8'
P_MB = 'B9'
P_FCMAX = 'B10'
P_TICK = 'B11'
P_PZT = 'B12'
P_DIAS = 'B13'
P_PZANO = 'B14'
P_SEM = 'B15'
P_STKSEM = 'B16'
P_PLAZO = 'B17'
P_SEG = 'B18'
P_INT = 'B19'
P_ANTIC = 'B20'

A = lambda coord: QPAR + '$' + coord[0] + '$' + coord[1:]      # noqa: E731

# --- Filas ----------------------------------------------------------------
COB_INI = 7                      # bloque de las cuatro coberturas
COBS = ('negra', 'origen', 'leche', 'blanca')
COB_FIN = COB_INI + len(COBS) - 1

REF_CAB = 15                     # fila de cabecera de la tabla de referencias
REF_INI = 16
REF_FIN = REF_INI + len(D.CARTA) - 1            # 43
REF_TOT = REF_FIN + 1                           # 44

ESC_CAB = 6
ESC_INI = 7
ESCENARIOS = (
    ('Precio de hoy', 0.0,
     'La tarifa que tienes hoy delante. Es el punto de partida, no un '
     'escenario: si tu proveedor te ha pasado tarifa nueva, cámbiala arriba.'),
    ('Subida moderada', 0.20,
     'Una subida que el mercado del cacao se ha comido varias veces sin que '
     'nadie cambie la carta. Se absorbe con gramaje o con margen.'),
    ('Subida fuerte', 0.40,
     'El escenario de trabajo de esta hoja: el que obliga a decidir. A partir '
     'de aquí no hay una sola palanca que lo arregle.'),
    ('Crisis del cacao', 0.60,
     'El peor caso razonable. Sirve para saber qué referencias tendrías que '
     'retirar del surtido, no para poner precios.'),
    ('Tu escenario', 0.35,
     'Escribe aquí la subida que te ha comunicado TU proveedor. Es la celda '
     'que vas a usar de verdad.'),
)
ESC_FIN = ESC_INI + len(ESCENARIOS) - 1

STK_CAB = 6
STK_INI = 7
STK_FIN = STK_INI + len(COBS) - 1
STK_TOT = STK_FIN + 1

#: Fila donde arranca el bloque de vocabulario de los desplegables de la hoja
#: «Coste de Cobertura»: por debajo de TODO lo demás de esa hoja.
LISTAS_FILA = 60

IDS_LEGALES = ('CHN-71', 'CHN-71c', 'CHN-10')

#: Formato de compra por defecto de cada cobertura (kg por bloque o saco).
#: SUPUESTO declarado salvo los dos que trae la ficha del proveedor.
FORMATO_KG = {'negra': 5.0, 'origen': 0.4, 'leche': 10.0, 'blanca': 10.0}
FORMATO_FUENTE = {'negra': 'CHS-28a', 'origen': 'CHS-28c',
                  'leche': 'supuesto', 'blanca': 'supuesto'}

SEMANAS_ANO = 52
SEMANAS_STOCK = 3
PLAZO_ENTREGA = 2
STOCK_SEGURIDAD = 1
INTERES = 0.06
SEMANAS_ANTICIPO = 8
FC_MAXIMO = 0.35


# --------------------------------------------------------------------------
# Datos derivados de `datos_ejemplo`
# --------------------------------------------------------------------------
def kg_cobertura(r):
    """Kilos de cobertura por pieza vendible, DESGLOSADOS por cobertura. Suma
    la cáscara y la que va dentro del relleno; una caja se compone de lo que
    lleva dentro."""
    out = {}
    if D.es_caja(r):
        for i, n in r['composicion_caja']:
            for k, v in kg_cobertura(D.ref(i)).items():
                out[k] = out.get(k, 0.0) + v * n
        return out
    out[r['cobertura']] = out.get(r['cobertura'], 0.0) + r['g_chocolate'] / 1000.0
    if r['relleno']:
        for ing, cantidad in D.RELLENOS[r['relleno']]['lineas']:
            if ing in D.COBERTURA_DE_INGREDIENTE:
                k = D.COBERTURA_DE_INGREDIENTE[ing]
                out[k] = out.get(k, 0.0) + r['g_relleno'] / 1000.0 * cantidad
    return out


def perfil(r):
    """Lo que necesita una fila de la tabla de referencias."""
    kc = kg_cobertura(r)
    g_total = sum(kc.values()) * 1000.0
    if D.es_caja(r):
        clave = max(kc.items(), key=lambda kv: kv[1])[0] if kc else r['cobertura']
        g_cascara, g_relleno = g_total, 0.0
    else:
        clave = r['cobertura']
        g_cascara = r['g_chocolate']
        g_relleno = g_total - g_cascara
    precio = D.precio_cobertura_base_imponible(clave)
    cob_eur = g_total / 1000.0 * precio
    otras = D.coste_materia_unidad(r) - cob_eur
    return {'r': r, 'clave': clave, 'g_cascara': round(g_cascara, 3),
            'g_relleno': round(g_relleno, 3), 'g_total': g_total,
            'peso': D.peso_total_g(r), 'otras': round(max(otras, 0.0), 4)}


PERFILES = [perfil(r) for r in D.CARTA]


# --------------------------------------------------------------------------
# Hoja «Instrucciones»
# --------------------------------------------------------------------------
def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS)
    C.anchos(ws, {'A': 26, 'B': 34, 'C': 62})
    C.encabezar(ws, TITULO, C.NOTA_VERDES, col_fin='C')
    C.pagina(ws, apaisado=False)

    fila = 5
    C.seccion(ws, 'A%d' % fila, 'Qué Decide Este Libro')
    fila += 1
    C.parrafo(ws, fila,
              'Qué haces cuando el cacao sube: subir el precio, bajar el '
              'gramaje, cambiar de cobertura o aceptar menos margen. El libro '
              'no elige por ti: pone las cuatro salidas en euros y te dice '
              'cuál de tus referencias se rompe la primera.',
              col_fin='C', alto=46)
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'La Celda Más Importante del Paquete')
    fila += 1
    C.parrafo(ws, fila,
              'El precio de cada cobertura vive SÓLO en este libro, en la hoja '
              '«' + H_COB + '». El libro 4 (carta y escandallo) y el libro 7 '
              '(plan financiero) lo COPIAN a mano en una celda verde y lo '
              'cuadran: no hay ni una fórmula entre ficheros. Si cambias aquí '
              'el precio, cámbialo también allí -las dos hojas te avisan si no '
              'cuadran-.',
              col_fin='C', alto=58)
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'El IVA: por Qué el Precio Sale en Dos Bases')
    fila += 1
    C.parrafo(ws, fila,
              'La tarifa del distribuidor puede venir con IVA o sin él, y casi '
              'nunca lo dice en la misma línea. Un escandallo se calcula '
              'SIEMPRE con precios sin IVA: el que soportas al comprar te lo '
              'deduces. Por eso escribes el precio tal y como te lo pasan, '
              'marcas en qué base viene, y la hoja te devuelve la base '
              'imponible. Mezclar las dos bases infla el food cost alrededor '
              'de un 9 %, que es justo el margen que creías tener.',
              col_fin='C', alto=70)
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Las Hojas, y Qué Hace Cada Una')
    fila += 1
    for hoja, texto in (
        (H_PAR, 'Los números que gobiernan todo el libro: IVA, food cost '
                'objetivo, food cost máximo, volumen de venta y condiciones de '
                'compra. Nada de esto está escrito dentro de una fórmula.'),
        (H_COB, 'El precio de las cuatro coberturas en las dos bases, y el '
                'coste de cobertura de cada una de las 28 referencias de la '
                'carta. De aquí sale todo lo demás.'),
        (H_ESC, 'Cinco escenarios de subida -hoy, +20 %, +40 %, +60 % y el '
                'tuyo- con el coste de materia y el food cost de cada '
                'referencia en cada uno.'),
        (H_REP, 'Las cuatro salidas, referencia a referencia: subir el PVP, '
                'bajar el gramaje, cambiar de cobertura o aguantar. Y la '
                'referencia que primero se rompe.'),
        (H_STK, 'Cuánta cobertura tienes que tener parada, qué dinero es eso, '
                'cuándo hay que volver a pedir y qué te cuesta comprar por '
                'delante para una campaña.'),
    ):
        motor.val(ws, 'A%d' % fila, hoja, bold=True)
        ws.merge_cells('B%d:C%d' % (fila, fila))
        motor.val(ws, 'B%d' % fila, texto, wrap=True)
        ws['B%d' % fila].font = Font(size=9)
        ws.row_dimensions[fila].height = 42
        fila += 1
    fila += 1

    C.seccion(ws, 'A%d' % fila, 'Cada Cuánto Se Usa')
    fila += 1
    C.parrafo(ws, fila,
              'Cada vez que tu proveedor te pase tarifa nueva, y como mínimo '
              'una vez por trimestre. Son diez minutos: cambias los precios de '
              'la hoja «' + H_COB + '», miras la hoja «' + H_REP + '» y '
              'decides. Antes de Navidad, míralo también con la compra '
              'anticipada de la hoja «' + H_STK + '».',
              col_fin='C', alto=46)
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Frontera con el Kit de Tareas Chocolatería')
    fila += 1
    C.parrafo(ws, fila,
              'El Kit de Tareas Chocolatería (12 €) no costea nada: publica '
              'las curvas de templado, las fichas de moldeado y los plazos de '
              'vida útil. Este libro no repite ninguna de esas tablas; lo que '
              'hace es ponerle precio al kilo de cobertura que se va en cada '
              'pieza. Si tienes el kit, los porcentajes de cacao de las tres '
              'coberturas son los suyos: cobertura negra 55-70 %, con leche '
              '35-40 % y blanca 28-33 % (02-partidas-produccion.xlsx, hoja '
              'Templado).',
              col_fin='C', alto=70)
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'De Dónde Salen los Números del Ejemplo')
    fila += 1
    C.parrafo(ws, fila,
              'Todo lo que ves relleno es la bombonería «La Almendra», el caso '
              'de ejemplo de la guía: 75 m2, obrador y tienda, 28 referencias. '
              'Los precios de las coberturas negra y de origen están '
              'verificados con su tienda y su fecha; los de leche y blanca son '
              'supuestos declarados, porque no hay precio público verificado. '
              'Todos los gramajes, el mix y el volumen son supuestos: '
              'sustitúyelos por los tuyos en cuanto tengas dos semanas de TPV.',
              col_fin='C', alto=70)
    fila += 2

    C.parrafo(ws, fila, C.NOTA_DESPROTEGER, col_fin='C', alto=30)
    fila += 2
    C.pie(ws, fila, col='A', col_fin='C')
    return ws


# --------------------------------------------------------------------------
# Hoja «Parámetros»
# --------------------------------------------------------------------------
def par(ws, fila, etiqueta, valor, fmt, unidad, origen, nota, formula=None):
    motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
    if formula is None:
        cel = X.entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
    else:
        cel = motor.f(ws, 'B%d' % fila, formula, fmt=fmt)
    motor.val(ws, 'C%d' % fila, unidad)
    motor.val(ws, 'D%d' % fila, origen)
    motor.val(ws, 'E%d' % fila, nota, wrap=True)
    ws['E%d' % fila].font = Font(size=9)
    ws.row_dimensions[fila].height = 34
    return cel


def hoja_parametros(wb):
    ws = wb.create_sheet(H_PAR)
    C.anchos(ws, {'A': 48, 'B': 14, 'C': 15, 'D': 20, 'E': 78})
    C.encabezar(ws, H_PAR,
                'Ninguna de estas cifras está escrita dentro de una fórmula: '
                'se cambian aquí y el libro entero se mueve.', col_fin='E')
    C.pagina(ws, apaisado=True)
    C.cabecera(ws, 5, (('A', 'Parámetro'), ('B', 'Valor'), ('C', 'Unidad'),
                       ('D', 'De dónde sale'), ('E', 'Nota')), altura=24)
    C.inmovilizar(ws, 5)

    c = par(ws, 6, 'IVA de la cobertura y del chocolate', D.IVA_COBERTURA,
            C.FMT_PCT, 'sobre la base', 'CHN-71',
            D.PARAMS['iva_producto'][2])
    X.nota_celda(ws, c.coordinate, 'CHN-71')
    c = par(ws, 7, 'IVA del producto que vendes en mostrador',
            D.P('iva_producto'), C.FMT_PCT, 'sobre la base', 'CHN-71',
            'El mismo tipo, y por la misma razón. La taza SERVIDA EN SALA va '
            'al 10 % por otra vía -es prestación de servicio de hostelería, '
            'no entrega de un bien-, y por eso la nota de esta celda cita las '
            'dos.')
    X.nota_celda(ws, c.coordinate, 'CHN-71c')
    par(ws, 8, 'Food cost objetivo (sobre PVP sin IVA)',
        D.P('food_cost_objetivo'), C.FMT_PCT, 'sobre PVP', 'supuesto',
        D.PARAMS['food_cost_objetivo'][2])
    par(ws, 9, 'Margen bruto objetivo sobre PVP', None, C.FMT_PCT,
        'sobre PVP', 'calculado',
        'Es el food cost objetivo dicho al revés. Son la misma regla, no dos: '
        'por eso sólo se teclea una y la otra se calcula.',
        formula='=IFERROR(1-%s,"")' % A(P_FC))
    par(ws, 10, 'Food cost máximo antes de dar la referencia por rota',
        FC_MAXIMO, C.FMT_PCT, 'sobre PVP', 'supuesto',
        'El techo que te pones tú. Por encima de él la hoja «' + H_REP + '» '
        'marca la referencia como ROTA. No es un límite del sector: es tu '
        'línea roja, y con ella se calcula «la subida máxima que aguanta».')
    par(ws, 11, 'Clientes al día en velocidad de crucero',
        D.P('tickets_dia_crucero'), C.FMT_ENT, 'tickets/día', 'supuesto',
        D.PARAMS['tickets_dia_crucero'][2])
    par(ws, 12, 'Piezas por ticket', D.P('piezas_por_ticket'), C.FMT_DEC1,
        'piezas/ticket', 'supuesto', D.PARAMS['piezas_por_ticket'][2])
    par(ws, 13, 'Días de apertura al año', D.NEGOCIO['dias_apertura_anio'],
        C.FMT_ENT, 'días/año', 'supuesto', D.NEGOCIO['nota_dias_apertura'])
    par(ws, 14, 'Piezas vendibles al año', None, C.FMT_ENT, 'piezas/año',
        'calculado',
        'Clientes al día por piezas por ticket por días de apertura. Es la '
        'base sobre la que el mix de cada referencia reparte las unidades. Una '
        'caja surtida cuenta como UNA pieza vendible: la unidad de venta de '
        'una bombonería es la caja, no el bombón.',
        formula='=IFERROR(%s*%s*%s,"")' % (A(P_TICK), A(P_PZT), A(P_DIAS)))
    par(ws, 15, 'Semanas al año', SEMANAS_ANO, C.FMT_ENT, 'semanas',
        'supuesto',
        'Se usa para pasar el consumo anual de cobertura a consumo semanal y '
        'para prorratear el coste financiero de la compra anticipada.')
    par(ws, 16, 'Semanas de stock de cobertura que quieres tener',
        SEMANAS_STOCK, C.FMT_ENT, 'semanas', 'supuesto',
        'Cuánta cobertura quieres tener parada en el almacén. Tres semanas es '
        'el supuesto de partida de La Almendra; súbelo si tu proveedor sirve '
        'mal o si entras en campaña.')
    par(ws, 17, 'Plazo de entrega de tu proveedor', PLAZO_ENTREGA, C.FMT_ENT,
        'semanas', 'supuesto',
        'Desde que haces el pedido hasta que lo tienes en el almacén. Es el '
        'número que de verdad fija el punto de recompra: pídeselo por escrito '
        'a tu comercial, y anótalo también en el libro 9.')
    par(ws, 18, 'Stock de seguridad', STOCK_SEGURIDAD, C.FMT_ENT, 'semanas',
        'supuesto',
        'El colchón por encima del plazo de entrega. Sin él, cualquier retraso '
        'del proveedor te para el obrador.')
    par(ws, 19, 'Tipo de interés anual del circulante', INTERES, C.FMT_PCT,
        'anual', 'supuesto',
        'Lo que te cuesta el dinero que tienes parado en existencias. Si tiras '
        'de póliza, es el tipo de tu póliza; si tiras de caja, es lo que dejas '
        'de ganar con ese dinero.')
    par(ws, 20, 'Semanas de compra anticipada para campaña', SEMANAS_ANTICIPO,
        C.FMT_ENT, 'semanas', 'supuesto',
        'Cuántas semanas de consumo compras por delante cuando llega Navidad. '
        'Es la compra que más tesorería inmoviliza del año, y la hoja «'
        + H_STK + '» le pone precio.')
    return ws


# --------------------------------------------------------------------------
# Hoja «Coste de Cobertura»
# --------------------------------------------------------------------------
def hoja_cobertura(wb):
    ws = wb.create_sheet(H_COB)
    C.anchos(ws, {'A': 9, 'B': 46, 'C': 26, 'D': 11, 'E': 12, 'F': 12,
                  'G': 12, 'H': 12, 'I': 13, 'J': 13, 'K': 13, 'L': 13,
                  'M': 13, 'N': 10, 'O': 12, 'P': 13, 'Q': 14, 'R': 12,
                  'S': 9, 'T': 12, 'U': 12})
    C.encabezar(ws, 'Coste de Cobertura por Referencia',
                'El precio de la cobertura vive SÓLO en esta hoja. Lo que '
                'copian el libro 4 y el libro 7 es la columna de BASE '
                'IMPONIBLE, nunca la de «como lo trae la fuente».', col_fin='U')
    C.pagina(ws, apaisado=True)

    # --- bloque de vocabulario para las DV (al pie de la hoja) -------------
    # Va por debajo de TODO lo demás de la hoja, incluido el bloque de consumo
    # por cobertura: si se solapara, el desplegable leería importes.
    listas, _fl = C.bloque_listas(
        ws, LISTAS_FILA,
        (('Base de IVA declarada', ('con IVA', 'sin IVA', 'no declarada')),),
        col='A')
    ref_base = listas['Base de IVA declarada']
    # La primera opción del bloque es «con IVA»: es la celda contra la que se
    # compara para decidir si hay que quitarle el impuesto al precio.
    celda_con_iva = '$A$%d' % (LISTAS_FILA + 2)

    # --- bloque A: las cuatro coberturas ----------------------------------
    C.seccion(ws, 'A5', 'La Celda Única: el Precio de Cada Cobertura en las Dos Bases')
    C.cabecera(ws, 6, (
        ('A', 'Clave'), ('B', 'Cobertura'), ('C', 'Formato de compra'),
        ('D', 'Precio como lo trae la fuente (€/kg)'),
        ('E', 'Base declarada por la fuente'), ('F', 'Tipo de IVA'),
        ('G', 'Precio en BASE IMPONIBLE (€/kg)'), ('H', 'Fuente'),
        ('I', '% de cacao (rango del kit)'), ('J', 'Nota')), altura=46)

    for i, clave in enumerate(COBS):
        fila = COB_INI + i
        c = D.COBERTURAS[clave]
        motor.val(ws, 'A%d' % fila, clave)
        motor.val(ws, 'B%d' % fila, c['nombre'], wrap=True)
        motor.val(ws, 'C%d' % fila, c['formato'], wrap=True)
        X.entrada(ws, 'D%d' % fila, c['precio_fuente'], fmt=C.FMT_DEC,
                  etiqueta='Precio de la cobertura ' + clave)
        X.entrada(ws, 'E%d' % fila, c['base_iva'],
                  etiqueta='Base de IVA de la cobertura ' + clave)
        X.entrada(ws, 'F%d' % fila, c['tipo_iva'], fmt=C.FMT_PCT,
                  etiqueta='Tipo de IVA de la cobertura ' + clave)
        motor.f(ws, 'G%d' % fila,
                '=IFERROR(IF($E{f}={ci},$D{f}/(1+$F{f}),$D{f}),"")'.format(
                    f=fila, ci=celda_con_iva), fmt=C.FMT_DEC)
        motor.val(ws, 'H%d' % fila, c['fuente_precio'])
        motor.val(ws, 'I%d' % fila, '%g-%g %%' % (c['cacao_min_pct'],
                                                  c['cacao_max_pct']))
        motor.val(ws, 'J%d' % fila, c['nota'], wrap=True)
        ws.merge_cells('J%d:U%d' % (fila, fila))
        ws['J%d' % fila].font = Font(size=9)
        ws.row_dimensions[fila].height = 46
        if c['fuente_precio'].startswith('CHS-'):
            X.nota_fuente(ws, 'D%d' % fila, c['fuente_precio'])
        X.nota_celda(ws, 'F%d' % fila, 'CHN-71')

    C.dv_rango(ws, ['E%d' % (COB_INI + i) for i in range(len(COBS))],
               ref_base, 'Base de IVA no válida',
               'Elige una de las tres: con IVA, sin IVA o no declarada. Si tu '
               'proveedor no lo dice, marca «no declarada» y pídeselo por '
               'escrito.')
    C.destacado(ws, 'G%d' % COB_INI)
    motor.val(ws, 'A%d' % (COB_FIN + 1),
              'ESTA es la celda que copian el libro 4 y el libro 7: '
              + H_COB + '!G' + str(COB_INI) + ', la de BASE IMPONIBLE. La de '
              'la izquierda (D' + str(COB_INI) + ') viene CON IVA declarado '
              'por la ficha, y un escandallo hecho con ella sale un 9 % alto.',
              wrap=True)
    ws.merge_cells('A%d:J%d' % (COB_FIN + 1, COB_FIN + 1))
    ws['A%d' % (COB_FIN + 1)].font = Font(italic=True, size=9)
    ws.row_dimensions[COB_FIN + 1].height = 30

    # --- bloque B: las referencias ----------------------------------------
    C.seccion(ws, 'A13', 'Coste de Chocolate por Referencia')
    motor.val(ws, 'A14',
              'Los gramos son los mismos que tecleas en el libro 4 (carta y '
              'escandallo); aquí sirven para medir cuánto te expone cada '
              'referencia al precio del cacao, e incluyen la cobertura que va '
              'DENTRO del relleno. Las cuatro cajas surtidas no tienen gramaje '
              'propio: se componen de lo que llevan dentro, se prorratean a su '
              'cobertura dominante y la diferencia queda en «demás materias», '
              'así que su coste de materia total es el exacto.', wrap=True)
    ws.merge_cells('A14:U14')
    ws['A14'].font = Font(italic=True, size=9)
    ws.row_dimensions[14].height = 40

    C.cabecera(ws, REF_CAB, (
        ('A', 'Id'), ('B', 'Referencia'), ('C', 'Familia'), ('D', 'Cobertura'),
        ('E', 'Gramos de cobertura en la cáscara'),
        ('F', 'Gramos de cobertura dentro del relleno'),
        ('G', 'Gramos de cobertura por pieza'),
        ('H', 'Peso total de la pieza (g)'),
        ('I', '% del peso que es cobertura'),
        ('J', 'Precio de su cobertura (€/kg)'),
        ('K', 'Coste de cobertura por pieza (€)'),
        ('L', 'Coste de las demás materias (€)'),
        ('M', 'Coste de materia por pieza (€)'),
        ('N', 'Mix (% de unidades)'), ('O', 'Unidades al año'),
        ('P', 'Kg de cobertura al año'), ('Q', '€ de cobertura al año'),
        ('R', 'PVP con IVA (€)'), ('S', 'IVA'), ('T', 'PVP sin IVA (€)'),
        ('U', 'Food cost de materia')), altura=58)
    C.inmovilizar(ws, REF_CAB, col='C')
    X.nota_celda(ws, 'I%d' % REF_CAB, 'CHN-10')

    for i, p in enumerate(PERFILES):
        fila = REF_INI + i
        r = p['r']
        motor.val(ws, 'A%d' % fila, r['id'])
        motor.val(ws, 'B%d' % fila, r['nombre'], wrap=True)
        motor.val(ws, 'C%d' % fila, r['familia'])
        X.entrada(ws, 'D%d' % fila, p['clave'],
                  etiqueta='Cobertura de ' + r['id'])
        X.entrada(ws, 'E%d' % fila, p['g_cascara'], fmt=C.FMT_DEC1,
                  etiqueta='Gramos de cobertura en la cáscara de ' + r['id'])
        X.entrada(ws, 'F%d' % fila, p['g_relleno'], fmt=C.FMT_DEC1,
                  etiqueta='Gramos de cobertura en el relleno de ' + r['id'])
        motor.f(ws, 'G%d' % fila, '=$E%d+$F%d' % (fila, fila), fmt=C.FMT_DEC1)
        X.entrada(ws, 'H%d' % fila, p['peso'], fmt=C.FMT_DEC1,
                  etiqueta='Peso total de ' + r['id'])
        motor.f(ws, 'I%d' % fila, '=IFERROR($G%d/$H%d,"")' % (fila, fila),
                fmt=C.FMT_PCT)
        motor.f(ws, 'J%d' % fila,
                '=IFERROR(INDEX($G$%d:$G$%d,MATCH($D%d,$A$%d:$A$%d,0)),"")'
                % (COB_INI, COB_FIN, fila, COB_INI, COB_FIN), fmt=C.FMT_DEC)
        motor.f(ws, 'K%d' % fila, '=IFERROR($G%d/1000*$J%d,"")' % (fila, fila),
                fmt=C.FMT_DEC)
        X.entrada(ws, 'L%d' % fila, p['otras'], fmt=C.FMT_DEC,
                  etiqueta='Demás materias de ' + r['id'])
        motor.f(ws, 'M%d' % fila, '=IFERROR($K%d+$L%d,"")' % (fila, fila),
                fmt=C.FMT_DEC)
        X.entrada(ws, 'N%d' % fila, r['mix_pct'], fmt=C.FMT_DEC1,
                  etiqueta='Mix de ' + r['id'])
        motor.f(ws, 'O%d' % fila, '=IFERROR(%s*$N%d/100,"")' % (A(P_PZANO), fila),
                fmt=C.FMT_ENT)
        motor.f(ws, 'P%d' % fila, '=IFERROR($G%d/1000*$O%d,"")' % (fila, fila),
                fmt=C.FMT_DEC1)
        motor.f(ws, 'Q%d' % fila, '=IFERROR($K%d*$O%d,"")' % (fila, fila),
                fmt=C.FMT_EUR)
        X.entrada(ws, 'R%d' % fila, r['pvp_con_iva'], fmt=C.FMT_DEC,
                  etiqueta='PVP con IVA de ' + r['id'])
        X.entrada(ws, 'S%d' % fila, r['iva'], fmt=C.FMT_PCT,
                  etiqueta='IVA de ' + r['id'])
        motor.f(ws, 'T%d' % fila, '=IFERROR($R%d/(1+$S%d),"")' % (fila, fila),
                fmt=C.FMT_DEC)
        motor.f(ws, 'U%d' % fila, '=IFERROR($M%d/$T%d,"")' % (fila, fila),
                fmt=C.FMT_PCT)
        ws.row_dimensions[fila].height = 26

    C.dv_rango(ws, ['D%d' % (REF_INI + i) for i in range(len(PERFILES))],
               '=$A$%d:$A$%d' % (COB_INI, COB_FIN), 'Cobertura no válida',
               'Elige una de las cuatro coberturas del bloque de arriba.')

    motor.val(ws, 'A%d' % REF_TOT, 'TOTAL', bold=True)
    motor.val(ws, 'B%d' % REF_TOT, 'Las %d referencias de la carta'
              % len(D.CARTA), bold=True)
    motor.f(ws, 'N%d' % REF_TOT, '=SUM(N%d:N%d)' % (REF_INI, REF_FIN),
            fmt=C.FMT_DEC1, bold=True)
    motor.f(ws, 'O%d' % REF_TOT, '=SUM(O%d:O%d)' % (REF_INI, REF_FIN),
            fmt=C.FMT_ENT, bold=True)
    motor.f(ws, 'P%d' % REF_TOT, '=SUM(P%d:P%d)' % (REF_INI, REF_FIN),
            fmt=C.FMT_DEC1, bold=True)
    motor.f(ws, 'Q%d' % REF_TOT, '=SUM(Q%d:Q%d)' % (REF_INI, REF_FIN),
            fmt=C.FMT_EUR, bold=True)

    fila = REF_TOT + 2
    motor.val(ws, 'A%d' % fila, 'Coste de materia de todo el año (€)',
              wrap=True)
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.f(ws, 'D%d' % fila,
            '=IFERROR(SUMPRODUCT($M$%d:$M$%d,$O$%d:$O$%d),"")'
            % (REF_INI, REF_FIN, REF_INI, REF_FIN), fmt=C.FMT_EUR)
    motor.val(ws, 'F%d' % fila,
              'Suma del coste de materia de cada referencia por sus unidades. '
              'Es la cifra contra la que se mide lo que pesa la cobertura.',
              wrap=True)
    ws.merge_cells('F%d:U%d' % (fila, fila))
    ws['F%d' % fila].font = Font(italic=True, size=9)

    fila += 1
    motor.val(ws, 'A%d' % fila,
              'Parte del coste de materia que es cobertura', wrap=True)
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.f(ws, 'D%d' % fila, '=IFERROR($Q$%d/$D$%d,"")' % (REF_TOT, fila - 1),
            fmt=C.FMT_PCT)
    motor.val(ws, 'F%d' % fila,
              'Cuanto más alto sea este número, más te mueve el precio del '
              'cacao. Por encima del 80 % no hay escandallo que te salve de '
              'una subida: la decisión es de carta, no de coste.', wrap=True)
    ws.merge_cells('F%d:U%d' % (fila, fila))
    ws['F%d' % fila].font = Font(italic=True, size=9)

    fila += 2
    C.seccion(ws, 'A%d' % fila, 'Consumo por Cobertura')
    C.cabecera(ws, fila + 1, (('A', 'Clave'), ('B', 'Cobertura'),
                              ('C', 'Kg al año'), ('D', '€ al año'),
                              ('E', 'Referencias que la llevan')), altura=24)
    global CONS_INI
    CONS_INI = fila + 2
    for i, clave in enumerate(COBS):
        f2 = CONS_INI + i
        motor.val(ws, 'A%d' % f2, clave)
        motor.val(ws, 'B%d' % f2, D.COBERTURAS[clave]['nombre'], wrap=True)
        motor.f(ws, 'C%d' % f2,
                '=IFERROR(SUMIF($D$%d:$D$%d,$A%d,$P$%d:$P$%d),"")'
                % (REF_INI, REF_FIN, f2, REF_INI, REF_FIN), fmt=C.FMT_DEC1)
        motor.f(ws, 'D%d' % f2,
                '=IFERROR(SUMIF($D$%d:$D$%d,$A%d,$Q$%d:$Q$%d),"")'
                % (REF_INI, REF_FIN, f2, REF_INI, REF_FIN), fmt=C.FMT_EUR)
        motor.f(ws, 'E%d' % f2,
                '=COUNTIF($D$%d:$D$%d,$A%d)' % (REF_INI, REF_FIN, f2),
                fmt=C.FMT_ENT)
    return ws


# --------------------------------------------------------------------------
# Hoja «Escenarios de Precio»
# --------------------------------------------------------------------------
def hoja_escenarios(wb):
    ws = wb.create_sheet(H_ESC)
    C.anchos(ws, {'A': 9, 'B': 42, 'C': 14, 'D': 14, 'E': 13, 'F': 13,
                  'G': 12, 'H': 13, 'I': 12, 'J': 13, 'K': 12, 'L': 13,
                  'M': 12, 'N': 13, 'O': 12, 'P': 14, 'Q': 40})
    C.encabezar(ws, H_ESC,
                'Cinco escenarios sobre el MISMO precio de partida. Lo único '
                'que se teclea es el porcentaje de subida: los precios y los '
                'food cost salen solos.', col_fin='Q')
    C.pagina(ws, apaisado=True)

    C.cabecera(ws, ESC_CAB, (
        ('A', 'Escenario'), ('B', 'Qué es'),
        ('C', 'Subida sobre el precio de hoy'), ('D', 'Factor'),
        ('E', 'Cobertura negra (€/kg)'), ('F', 'Cobertura de origen (€/kg)'),
        ('G', 'Cobertura con leche (€/kg)'),
        ('H', 'Cobertura blanca (€/kg)')), altura=46)

    for i, (nombre, subida, nota) in enumerate(ESCENARIOS):
        fila = ESC_INI + i
        motor.val(ws, 'A%d' % fila, nombre, bold=True)
        motor.val(ws, 'B%d' % fila, nota, wrap=True)
        X.entrada(ws, 'C%d' % fila, subida, fmt=C.FMT_PCT,
                  etiqueta='Subida del escenario ' + nombre)
        motor.f(ws, 'D%d' % fila, '=1+$C%d' % fila, fmt=C.FMT_DEC)
        for j, letra in enumerate('EFGH'):
            motor.f(ws, '%s%d' % (letra, fila),
                    '=IFERROR(%s$G$%d*$D%d,"")' % (QCOB, COB_INI + j, fila),
                    fmt=C.FMT_DEC)
        ws.row_dimensions[fila].height = 40

    C.seccion(ws, 'A13', 'Coste de Materia y Food Cost, Referencia a Referencia')
    motor.val(ws, 'A14',
              'Lo que sube en cada escenario es SÓLO la parte de cobertura: '
              'las demás materias se quedan donde estaban. Por eso una tableta '
              'de origen -que es cobertura y poco más- se mueve mucho más que '
              'un bombón de praliné.', wrap=True)
    ws.merge_cells('A14:Q14')
    ws['A14'].font = Font(italic=True, size=9)
    ws.row_dimensions[14].height = 28

    cols = []
    for i, (nombre, _s, _n) in enumerate(ESCENARIOS):
        cols.append((chr(ord('F') + i * 2), chr(ord('G') + i * 2), nombre))

    cab = [('A', 'Id'), ('B', 'Referencia'),
           ('C', 'Coste de cobertura hoy (€)'),
           ('D', 'Coste de las demás materias (€)'), ('E', 'PVP sin IVA (€)')]
    for c1, c2, nombre in cols:
        cab.append((c1, 'Coste de materia CON merma · ' + nombre + ' (€)'))
        cab.append((c2, 'Food cost · ' + nombre))
    cab.append(('P', 'Subida máxima que aguanta'))
    cab.append(('Q', 'Veredicto'))
    # B3 (refutación 2026-09-12): «Coste de materia» comparaba sin merma
    # contra el mismo food cost del libro 4, que SÍ aplica la merma no
    # recuperable -y con eso, TB4 pasaba por debajo del techo aquí y por
    # encima allí-. Se añade la merma de cada referencia (columna R, el
    # mismo dato que siembra el libro 5) para que las dos hojas midan lo
    # mismo: «un concepto, una fuente».
    cab.append(('R', 'Merma no recuperable (%)'))
    C.cabecera(ws, REF_CAB, cab, altura=58)
    C.inmovilizar(ws, REF_CAB, col='C')

    for i, p in enumerate(PERFILES):
        fila = REF_INI + i
        r = p['r']
        motor.val(ws, 'A%d' % fila, r['id'])
        motor.val(ws, 'B%d' % fila, r['nombre'], wrap=True)
        motor.f(ws, 'C%d' % fila, '=%sK%d' % (QCOB, fila), fmt=C.FMT_DEC)
        motor.f(ws, 'D%d' % fila, '=%sL%d' % (QCOB, fila), fmt=C.FMT_DEC)
        motor.f(ws, 'E%d' % fila, '=%sT%d' % (QCOB, fila), fmt=C.FMT_DEC)
        motor.val(ws, 'R%d' % fila, r['merma_no_recuperable_pct'],
                  fmt=C.FMT_PCT)
        for j, (c1, c2, _n) in enumerate(cols):
            motor.f(ws, '%s%d' % (c1, fila),
                    '=IFERROR(($D%d+$C%d*$D$%d)/(1-$R%d),"")'
                    % (fila, fila, ESC_INI + j, fila), fmt=C.FMT_DEC)
            motor.f(ws, '%s%d' % (c2, fila),
                    '=IFERROR(%s%d/$E%d,"")' % (c1, fila, fila), fmt=C.FMT_PCT)
        motor.f(ws, 'P%d' % fila,
                '=IFERROR(($E%d*%s*(1-$R%d)-$D%d)/$C%d-1,"")'
                % (fila, A(P_FCMAX), fila, fila, fila), fmt=C.FMT_PCT)
        motor.f(ws, 'Q%d' % fila,
                '=IF(ISNUMBER($P%d),IF($P%d<0,"Ya está por encima de tu food '
                'cost máximo","Aguanta esa subida sin pasar de tu food cost '
                'máximo"),"")' % (fila, fila))
        ws.row_dimensions[fila].height = 26

    motor.semaforo_isnumber(ws, 'P%d:P%d' % (REF_INI, REF_FIN),
                            '$P%d' % REF_INI, operador='<', umbral='0')

    motor.val(ws, 'A%d' % REF_TOT, 'ROTAS', bold=True)
    motor.val(ws, 'B%d' % REF_TOT,
              'Referencias que en ese escenario pasan de tu food cost máximo',
              bold=True, wrap=True)
    for c1, c2, _n in cols:
        motor.f(ws, '%s%d' % (c2, REF_TOT),
                '=COUNTIF(%s%d:%s%d,">"&%s)'
                % (c2, REF_INI, c2, REF_FIN, A(P_FCMAX)), fmt=C.FMT_ENT,
                bold=True)
    return ws


# --------------------------------------------------------------------------
# Hoja «Repercusión al PVP»
# --------------------------------------------------------------------------
def hoja_repercusion(wb):
    ws = wb.create_sheet(H_REP)
    C.anchos(ws, {'A': 9, 'B': 42, 'C': 12, 'D': 12, 'E': 13, 'F': 11,
                  'G': 14, 'H': 12, 'I': 14, 'J': 14, 'K': 12, 'L': 12,
                  'M': 14, 'N': 13, 'O': 15, 'P': 34, 'Q': 13, 'R': 34})
    C.encabezar(ws, H_REP,
                'Las cuatro salidas cuando sube el cacao: subir el PVP, bajar '
                'el gramaje, cambiar de cobertura o aguantar. Elige arriba el '
                'escenario y la hoja entera se recalcula.', col_fin='R')
    C.pagina(ws, apaisado=True)

    listas, _f = C.bloque_listas(
        ws, REF_TOT + 8,
        (('Escenarios', tuple(n for n, _s, _x in ESCENARIOS)),), col='A')

    C.seccion(ws, 'A5', 'El Escenario con el que Trabajas')
    motor.val(ws, 'A6', 'Escenario elegido')
    ws.merge_cells('A6:B6')
    X.entrada(ws, 'C6', ESCENARIOS[2][0], etiqueta='Escenario elegido')
    C.dv_rango(ws, ['C6'], listas['Escenarios'], 'Escenario no válido',
               'Elige uno de los cinco escenarios de la hoja «' + H_ESC + '».')
    motor.val(ws, 'A7', 'Subida que supone')
    ws.merge_cells('A7:B7')
    motor.f(ws, 'C7',
            '=IFERROR(INDEX(%sC$%d:C$%d,MATCH($C$6,%sA$%d:A$%d,0)),"")'
            % (QESC, ESC_INI, ESC_FIN, QESC, ESC_INI, ESC_FIN), fmt=C.FMT_PCT)
    motor.val(ws, 'A8', 'Factor sobre el precio de hoy')
    ws.merge_cells('A8:B8')
    motor.f(ws, 'C8',
            '=IFERROR(INDEX(%sD$%d:D$%d,MATCH($C$6,%sA$%d:A$%d,0)),"")'
            % (QESC, ESC_INI, ESC_FIN, QESC, ESC_INI, ESC_FIN), fmt=C.FMT_DEC)
    motor.val(ws, 'E6',
              'Cambia sólo esta celda: el escenario elegido gobierna las 28 '
              'filas de abajo. Si quieres trabajar con la subida que te ha '
              'pasado tu proveedor, ponla en «Tu escenario» en la hoja «'
              + H_ESC + '» y elígelo aquí.', wrap=True)
    ws.merge_cells('E6:R8')
    ws['E6'].font = Font(italic=True, size=9)

    C.seccion(ws, 'A13', 'Qué Haces con Cada Referencia')
    motor.val(ws, 'A14',
              'Las columnas I a L suben el precio; las M y N bajan el gramaje; '
              'las O y P cambian de cobertura. La columna Q dice cuánto '
              'aguanta la referencia antes de romper tu food cost máximo, y es '
              'la que ordena la lista: la que menos aguante es la primera que '
              'se te rompe.', wrap=True)
    ws.merge_cells('A14:R14')
    ws['A14'].font = Font(italic=True, size=9)
    ws.row_dimensions[14].height = 28

    C.cabecera(ws, REF_CAB, (
        ('A', 'Id'), ('B', 'Referencia'), ('C', 'PVP con IVA hoy (€)'),
        ('D', 'PVP sin IVA hoy (€)'), ('E', 'Coste de materia hoy (€)'),
        ('F', 'Food cost hoy'),
        ('G', 'Coste de materia en el escenario (€)'),
        ('H', 'Food cost en el escenario'),
        ('I', 'PVP sin IVA necesario (€)'), ('J', 'PVP con IVA necesario (€)'),
        ('K', 'Subida de PVP (€)'), ('L', 'Subida de PVP (%)'),
        ('M', 'Gramos de cobertura admisibles con el PVP de hoy'),
        ('N', 'Recorte de gramaje necesario (negativo: te sobra margen)'),
        ('O', 'Precio máximo de cobertura que aguanta (€/kg)'),
        ('P', '¿Qué cobertura te vale a ese precio?'),
        ('Q', 'Subida máxima que aguanta'), ('R', 'Veredicto')), altura=58)
    C.inmovilizar(ws, REF_CAB, col='C')

    for i, p in enumerate(PERFILES):
        fila = REF_INI + i
        r = p['r']
        motor.val(ws, 'A%d' % fila, r['id'])
        motor.val(ws, 'B%d' % fila, r['nombre'], wrap=True)
        motor.f(ws, 'C%d' % fila, '=%sR%d' % (QCOB, fila), fmt=C.FMT_DEC)
        motor.f(ws, 'D%d' % fila, '=%sT%d' % (QCOB, fila), fmt=C.FMT_DEC)
        motor.f(ws, 'E%d' % fila, '=%sM%d' % (QCOB, fila), fmt=C.FMT_DEC)
        motor.f(ws, 'F%d' % fila, '=%sU%d' % (QCOB, fila), fmt=C.FMT_PCT)
        motor.f(ws, 'G%d' % fila,
                '=IFERROR(%sD%d+%sC%d*$C$8,"")' % (QESC, fila, QESC, fila),
                fmt=C.FMT_DEC)
        motor.f(ws, 'H%d' % fila, '=IFERROR($G%d/$D%d,"")' % (fila, fila),
                fmt=C.FMT_PCT)
        motor.f(ws, 'I%d' % fila, '=IFERROR($G%d/%s,"")' % (fila, A(P_FC)),
                fmt=C.FMT_DEC)
        motor.f(ws, 'J%d' % fila,
                '=IFERROR($I%d*(1+%sS%d),"")' % (fila, QCOB, fila),
                fmt=C.FMT_DEC)
        motor.f(ws, 'K%d' % fila, '=IFERROR($J%d-$C%d,"")' % (fila, fila),
                fmt=C.FMT_DEC)
        motor.f(ws, 'L%d' % fila, '=IFERROR($J%d/$C%d-1,"")' % (fila, fila),
                fmt=C.FMT_PCT)
        motor.f(ws, 'M%d' % fila,
                '=IFERROR(($D%d*%s-%sD%d)/(%sJ%d*$C$8)*1000,"")'
                % (fila, A(P_FC), QESC, fila, QCOB, fila), fmt=C.FMT_DEC1)
        motor.f(ws, 'N%d' % fila,
                '=IFERROR(1-$M%d/%sG%d,"")' % (fila, QCOB, fila), fmt=C.FMT_PCT)
        motor.f(ws, 'O%d' % fila,
                '=IFERROR(($D%d*%s-%sD%d)/(%sG%d/1000),"")'
                % (fila, A(P_FC), QESC, fila, QCOB, fila), fmt=C.FMT_DEC)
        motor.f(ws, 'P%d' % fila,
                '=IF(ISNUMBER($O%d),IF($O%d>=MAX(%sG$%d:G$%d),"Cualquiera de '
                'las cuatro, incluida la que usas",IF($O%d>=MIN(%sG$%d:G$%d),'
                '"Sólo alguna de las más baratas: compáralas arriba",'
                '"Ninguna: el gramaje o el PVP tienen que moverse")),"")'
                % (fila, fila, QCOB, COB_INI, COB_FIN, fila, QCOB, COB_INI,
                   COB_FIN))
        motor.f(ws, 'Q%d' % fila, '=%sP%d' % (QESC, fila), fmt=C.FMT_PCT)
        motor.f(ws, 'R%d' % fila,
                '=IF(ISNUMBER($H%d),IF($H%d>%s,"ROTA: por encima de tu food '
                'cost máximo",IF($H%d>%s,"Avisa: por encima del objetivo",'
                '"Aguanta")),"")'
                % (fila, fila, A(P_FCMAX), fila, A(P_FC)))
        ws.row_dimensions[fila].height = 26

    motor.semaforo_isnumber(ws, 'Q%d:Q%d' % (REF_INI, REF_FIN),
                            '$Q%d' % REF_INI, operador='<', umbral='0')

    fila = REF_TOT + 1
    C.seccion(ws, 'A%d' % fila, 'La Referencia que Primero se Rompe')
    fila += 1
    motor.val(ws, 'A%d' % fila, 'Referencia', bold=True)
    ws.merge_cells('A%d:B%d' % (fila, fila))
    motor.f(ws, 'C%d' % fila,
            '=IFERROR(INDEX($B$%d:$B$%d,MATCH(MIN($Q$%d:$Q$%d),$Q$%d:$Q$%d,0)),"")'
            % (REF_INI, REF_FIN, REF_INI, REF_FIN, REF_INI, REF_FIN))
    ws.merge_cells('C%d:H%d' % (fila, fila))
    motor.val(ws, 'I%d' % fila,
              'Es la que menos subida aguanta antes de pasar de tu food cost '
              'máximo. No es la más cara ni la que más vendes: es la que peor '
              'reparte el precio del cacao.', wrap=True)
    ws.merge_cells('I%d:R%d' % (fila, fila))
    ws['I%d' % fila].font = Font(italic=True, size=9)

    fila += 1
    motor.val(ws, 'A%d' % fila, 'Subida que la rompe', bold=True)
    ws.merge_cells('A%d:B%d' % (fila, fila))
    motor.f(ws, 'C%d' % fila, '=IFERROR(MIN($Q$%d:$Q$%d),"")'
            % (REF_INI, REF_FIN), fmt=C.FMT_PCT)
    motor.f(ws, 'I%d' % fila,
            '=IF(ISNUMBER($C%d),IF($C%d<0,"En NEGATIVO: esa referencia ya '
            'está por encima de tu food cost máximo con el precio de hoy, y '
            'lo que mide es cuánto tendría que BAJAR el cacao para que '
            'entrase","Es la subida a partir de la cual tu carta empieza a '
            'romperse"),"")' % (fila, fila))
    ws.merge_cells('I%d:R%d' % (fila, fila))
    ws['I%d' % fila].font = Font(italic=True, size=9)

    fila += 1
    motor.val(ws, 'A%d' % fila,
              'Referencias rotas en el escenario elegido', bold=True)
    ws.merge_cells('A%d:B%d' % (fila, fila))
    motor.f(ws, 'C%d' % fila,
            '=COUNTIF($H$%d:$H$%d,">"&%s)' % (REF_INI, REF_FIN, A(P_FCMAX)),
            fmt=C.FMT_ENT)

    fila += 1
    motor.val(ws, 'A%d' % fila,
              'Subida media de PVP que haría falta', bold=True)
    ws.merge_cells('A%d:B%d' % (fila, fila))
    motor.f(ws, 'C%d' % fila,
            '=IFERROR(SUMPRODUCT($L$%d:$L$%d,%sN$%d:N$%d)/SUM(%sN$%d:N$%d),"")'
            % (REF_INI, REF_FIN, QCOB, REF_INI, REF_FIN, QCOB, REF_INI,
               REF_FIN), fmt=C.FMT_PCT)
    motor.val(ws, 'I%d' % fila,
              'Ponderada por el mix: es la subida media de carta, no la media '
              'de las 28 subidas. Si sale por encima del 10 %, no es una '
              'subida de precios: es un cambio de carta.', wrap=True)
    ws.merge_cells('I%d:R%d' % (fila, fila))
    ws['I%d' % fila].font = Font(italic=True, size=9)
    return ws


# --------------------------------------------------------------------------
# Hoja «Stock y Cobertura de Compra»
# --------------------------------------------------------------------------
def hoja_stock(wb):
    ws = wb.create_sheet(H_STK)
    C.anchos(ws, {'A': 9, 'B': 44, 'C': 13, 'D': 13, 'E': 12, 'F': 13,
                  'G': 13, 'H': 15, 'I': 14, 'J': 13, 'K': 12, 'L': 12,
                  'M': 14, 'N': 40, 'O': 14, 'P': 16, 'Q': 15})
    C.encabezar(ws, H_STK,
                'Cuánta cobertura tienes parada, qué dinero es eso, cuándo hay '
                'que volver a pedir y qué te cuesta comprar por delante para '
                'Navidad.', col_fin='Q')
    C.pagina(ws, apaisado=True)

    C.cabecera(ws, STK_CAB, (
        ('A', 'Clave'), ('B', 'Cobertura'), ('C', 'Consumo al año (kg)'),
        ('D', 'Consumo a la semana (kg)'),
        ('E', 'Semanas de stock objetivo'), ('F', 'Stock objetivo (kg)'),
        ('G', 'Precio en base imponible (€/kg)'),
        ('H', '€ parados en el almacén'), ('I', 'Formato de compra (kg)'),
        ('J', 'Bloques que hay que pedir'), ('K', 'Plazo de entrega (semanas)'),
        ('L', 'Stock de seguridad (semanas)'),
        ('M', 'Punto de recompra (kg)'),
        ('N', '¿Tu stock objetivo cubre el plazo?'),
        ('O', 'Semanas de compra anticipada'),
        ('P', '€ parados en la compra anticipada'),
        ('Q', 'Coste financiero del adelanto (€)')), altura=58)
    C.inmovilizar(ws, STK_CAB, col='C')

    for i, clave in enumerate(COBS):
        fila = STK_INI + i
        motor.val(ws, 'A%d' % fila, clave)
        motor.val(ws, 'B%d' % fila, D.COBERTURAS[clave]['nombre'], wrap=True)
        motor.f(ws, 'C%d' % fila,
                '=IFERROR(SUMIF(%s$D$%d:$D$%d,$A%d,%s$P$%d:$P$%d),"")'
                % (QCOB, REF_INI, REF_FIN, fila, QCOB, REF_INI, REF_FIN),
                fmt=C.FMT_DEC1)
        motor.f(ws, 'D%d' % fila, '=IFERROR($C%d/%s,"")' % (fila, A(P_SEM)),
                fmt=C.FMT_DEC1)
        X.entrada(ws, 'E%d' % fila, SEMANAS_STOCK, fmt=C.FMT_ENT,
                  etiqueta='Semanas de stock de la cobertura ' + clave)
        motor.f(ws, 'F%d' % fila, '=IFERROR($D%d*$E%d,"")' % (fila, fila),
                fmt=C.FMT_DEC1)
        motor.f(ws, 'G%d' % fila, '=%sG%d' % (QCOB, COB_INI + i),
                fmt=C.FMT_DEC)
        motor.f(ws, 'H%d' % fila, '=IFERROR($F%d*$G%d,"")' % (fila, fila),
                fmt=C.FMT_EUR)
        e = X.entrada(ws, 'I%d' % fila, FORMATO_KG[clave], fmt=C.FMT_DEC1,
                      etiqueta='Formato de compra de la cobertura ' + clave)
        if FORMATO_FUENTE[clave].startswith('CHS-'):
            X.nota_fuente(ws, e.coordinate, FORMATO_FUENTE[clave])
        motor.f(ws, 'J%d' % fila, '=IFERROR(ROUNDUP($F%d/$I%d,0),"")'
                % (fila, fila), fmt=C.FMT_ENT)
        X.entrada(ws, 'K%d' % fila, PLAZO_ENTREGA, fmt=C.FMT_ENT,
                  etiqueta='Plazo de entrega de la cobertura ' + clave)
        X.entrada(ws, 'L%d' % fila, STOCK_SEGURIDAD, fmt=C.FMT_ENT,
                  etiqueta='Stock de seguridad de la cobertura ' + clave)
        motor.f(ws, 'M%d' % fila, '=IFERROR($D%d*($K%d+$L%d),"")'
                % (fila, fila, fila), fmt=C.FMT_DEC1)
        motor.f(ws, 'N%d' % fila,
                '=IF(AND(ISNUMBER($F%d),ISNUMBER($M%d)),IF($F%d>=$M%d,"Sí",'
                '"No: te quedas sin cobertura antes de que llegue el pedido"),'
                '"")' % (fila, fila, fila, fila))
        X.entrada(ws, 'O%d' % fila, SEMANAS_ANTICIPO, fmt=C.FMT_ENT,
                  etiqueta='Semanas de compra anticipada de ' + clave)
        motor.f(ws, 'P%d' % fila, '=IFERROR($D%d*$O%d*$G%d,"")'
                % (fila, fila, fila), fmt=C.FMT_EUR)
        motor.f(ws, 'Q%d' % fila, '=IFERROR($P%d*%s*$O%d/%s,"")'
                % (fila, A(P_INT), fila, A(P_SEM)), fmt=C.FMT_EUR)
        ws.row_dimensions[fila].height = 28

    motor.val(ws, 'A%d' % STK_TOT, 'TOTAL', bold=True)
    motor.val(ws, 'B%d' % STK_TOT, 'Las cuatro coberturas', bold=True)
    for letra, fmt in (('C', C.FMT_DEC1), ('F', C.FMT_DEC1), ('H', C.FMT_EUR),
                       ('P', C.FMT_EUR), ('Q', C.FMT_EUR)):
        motor.f(ws, '%s%d' % (letra, STK_TOT),
                '=SUM(%s%d:%s%d)' % (letra, STK_INI, letra, STK_FIN), fmt=fmt,
                bold=True)

    fila = STK_TOT + 2
    motor.val(ws, 'A%d' % fila,
              'El dinero parado en cobertura no está en tu cuenta de '
              'resultados: está en tu tesorería. Por eso esta hoja va aparte '
              'del food cost, y por eso la compra anticipada de Navidad -que '
              'nadie discute- tiene su propia columna. Si el coste financiero '
              'del adelanto te parece pequeño, míralo al lado del margen de '
              'las semanas que estás financiando.', wrap=True)
    ws.merge_cells('A%d:Q%d' % (fila, fila))
    ws['A%d' % fila].font = Font(italic=True, size=9)
    ws.row_dimensions[fila].height = 40
    return ws


# --------------------------------------------------------------------------
# Mapa de celdas citables
# --------------------------------------------------------------------------
def mapa_celdas():
    m = [
        ('Precio de la cobertura negra como lo trae la fuente (con IVA)',
         H_COB, 'D%d' % COB_INI, 'entrada'),
        ('PRECIO DE LA COBERTURA NEGRA EN BASE IMPONIBLE (la celda que copian '
         'el libro 4 y el libro 7)', H_COB, 'G%d' % COB_INI, 'salida'),
        ('Precio de la cobertura de origen en base imponible', H_COB,
         'G%d' % (COB_INI + 1), 'salida'),
        ('Precio de la cobertura con leche en base imponible', H_COB,
         'G%d' % (COB_INI + 2), 'salida'),
        ('Precio de la cobertura blanca en base imponible', H_COB,
         'G%d' % (COB_INI + 3), 'salida'),
        ('IVA de la cobertura', H_PAR, P_IVACOB, 'parametro'),
        ('Food cost objetivo', H_PAR, P_FC, 'parametro'),
        ('Margen bruto objetivo sobre PVP', H_PAR, P_MB, 'salida'),
        ('Food cost máximo antes de dar la referencia por rota', H_PAR,
         P_FCMAX, 'parametro'),
        ('Piezas vendibles al año', H_PAR, P_PZANO, 'salida'),
        ('Semanas de stock objetivo', H_PAR, P_STKSEM, 'parametro'),
        ('Tipo de interés anual del circulante', H_PAR, P_INT, 'parametro'),
        ('Unidades vendidas al año en toda la carta', H_COB, 'O%d' % REF_TOT,
         'salida'),
        ('Kilos de cobertura que se van al año', H_COB, 'P%d' % REF_TOT,
         'salida'),
        ('Coste de la cobertura de todo el año', H_COB, 'Q%d' % REF_TOT,
         'salida'),
        ('Coste de materia de todo el año', H_COB, 'D%d' % (REF_TOT + 2),
         'salida'),
        ('Parte del coste de materia que es cobertura', H_COB,
         'D%d' % (REF_TOT + 3), 'salida'),
        ('Precio de la cobertura negra con una subida del 40 %', H_ESC,
         'E%d' % (ESC_INI + 2), 'salida'),
        ('Precio de la cobertura negra en el peor escenario', H_ESC,
         'E%d' % (ESC_INI + 3), 'salida'),
        ('Referencias que ya están por encima del food cost máximo con el '
         'precio de hoy', H_ESC, 'G%d' % REF_TOT, 'salida'),
        ('Food cost de materia de la tableta de origen, la referencia más '
         'expuesta', H_COB, 'U26', 'salida'),
        ('Referencias rotas con una subida del 20 %', H_ESC,
         'I%d' % REF_TOT, 'salida'),
        ('Referencias rotas con una subida del 40 %', H_ESC,
         'K%d' % REF_TOT, 'salida'),
        ('Referencias rotas con una subida del 60 %', H_ESC,
         'M%d' % REF_TOT, 'salida'),
        ('Escenario elegido en la hoja de repercusión', H_REP, 'C6', 'entrada'),
        ('Subida del escenario elegido', H_REP, 'C7', 'salida'),
        ('La referencia que primero se rompe', H_REP, 'C%d' % (REF_TOT + 2),
         'salida'),
        ('Subida que rompe la primera referencia', H_REP,
         'C%d' % (REF_TOT + 3), 'salida'),
        ('Referencias rotas en el escenario elegido', H_REP,
         'C%d' % (REF_TOT + 4), 'salida'),
        ('Subida media de PVP que haría falta en el escenario elegido', H_REP,
         'C%d' % (REF_TOT + 5), 'salida'),
        ('Kilos de cobertura negra que se consumen al año', H_STK,
         'C%d' % STK_INI, 'salida'),
        ('Euros parados en el almacén de cobertura', H_STK, 'H%d' % STK_TOT,
         'salida'),
        ('Euros parados en la compra anticipada de campaña', H_STK,
         'P%d' % STK_TOT, 'salida'),
        ('Coste financiero de la compra anticipada', H_STK, 'Q%d' % STK_TOT,
         'salida'),
        ('Punto de recompra de la cobertura negra', H_STK, 'M%d' % STK_INI,
         'salida'),
    ]
    # Las cuatro referencias que el texto cita una y otra vez.
    for rid in ('BC1', 'BC3', 'TB1', 'CJ1'):
        i = [p['r']['id'] for p in PERFILES].index(rid)
        fila = REF_INI + i
        nombre = D.ref(rid)['nombre']
        m += [
            ('Coste de cobertura por pieza de %s' % nombre, H_COB,
             'K%d' % fila, 'salida'),
            ('Food cost de materia de %s' % nombre, H_COB, 'U%d' % fila,
             'salida'),
            ('Coste de materia de %s con una subida del 40 %%' % nombre, H_ESC,
             'J%d' % fila, 'salida'),
            ('Subida máxima que aguanta %s' % nombre, H_ESC, 'P%d' % fila,
             'salida'),
            ('PVP con IVA que necesitaría %s en el escenario elegido' % nombre,
             H_REP, 'J%d' % fila, 'salida'),
            ('Recorte de gramaje que evitaría subir el PVP de %s' % nombre,
             H_REP, 'N%d' % fila, 'salida'),
        ]
    return m


NOTAS_MAPA = (
    'El precio de la cobertura vive SÓLO en este libro (regla «un concepto, '
    'una fuente», §3.3). La celda que copian el libro 4 (cruce 4 <- 3) y el '
    'libro 7 (cruce 7 <- 3) es ' + H_COB + '!G' + str(COB_INI) + ', la de '
    'BASE IMPONIBLE: `CHS-28a` publica 25,02 €/kg CON IVA y un escandallo '
    'hecho con esa base sale un 9 % alto (A-2). Los dos libros receptores la '
    'traen por celda verde con valor por defecto declarado más fila de CUADRE '
    '(D32); aquí no hay ni una fórmula que nombre otro fichero. El porcentaje '
    'de cobertura sobre el peso de la pieza de la hoja «' + H_COB + '» NO es '
    'el 25 % legal del ap. 1.13 del RD 1055/2003: aquél lo calcula el libro 4 '
    'con el chocolate de la cáscara sobre el peso total (`CHN-10`).'
)


# --------------------------------------------------------------------------
# Demostraciones con pycel
# --------------------------------------------------------------------------
def demo(ruta):
    from pycel import ExcelCompiler
    ok, fallos = [], []

    def prueba(nombre, cond, detalle=''):
        (ok if cond else fallos).append(
            nombre + (' — ' + detalle if detalle else ''))

    exc = ExcelCompiler(ruta)

    def v(hoja, coord):
        return exc.evaluate("'%s'!%s" % (hoja, coord))

    # 1. La base imponible de la cobertura negra es la de la fuente sin el IVA,
    #    y es MENOR que la de la fuente: es el defecto que A-2 vino a cerrar.
    fuente = v(H_COB, 'D%d' % COB_INI)
    base = v(H_COB, 'G%d' % COB_INI)
    iva = v(H_COB, 'F%d' % COB_INI)
    prueba('el precio en base imponible es el de la fuente sin el IVA',
           abs(base - fuente / (1 + iva)) < 0.0001 and base < fuente,
           '%.4f frente a %.2f' % (base, fuente))

    # 2. Si la base declarada pasa a «sin IVA», el precio ya no se toca.
    exc2 = ExcelCompiler(ruta)
    exc2.evaluate("'%s'!G%d" % (H_COB, COB_INI))
    exc2.set_value("'%s'!E%d" % (H_COB, COB_INI), 'sin IVA')
    base2 = exc2.evaluate("'%s'!G%d" % (H_COB, COB_INI))
    prueba('marcando la base como «sin IVA» el precio se queda como está',
           abs(base2 - fuente) < 0.0001, '%.4f' % base2)

    # 3. Una subida del 40 % sube el coste de materia SÓLO en la parte de
    #    cobertura: las demás materias no se mueven. B3 (refutación
    #    2026-09-12): el coste de materia lleva la merma no recuperable de
    #    la propia referencia (columna R), igual que el food cost del libro
    #    4, así que el esperado también la aplica.
    fila = REF_INI + [p['r']['id'] for p in PERFILES].index('BC1')
    cob = v(H_ESC, 'C%d' % fila)
    otras = v(H_ESC, 'D%d' % fila)
    merma = v(H_ESC, 'R%d' % fila)
    esc40 = v(H_ESC, 'J%d' % fila)
    esperado = (otras + cob * 1.40) / (1 - merma)
    prueba('una subida del 40 % sólo mueve la parte de cobertura',
           abs(esc40 - esperado) < 0.0001,
           '%.4f frente a %.4f' % (esc40, esperado))

    # 4. El veredicto CAMBIA al cambiar el escenario elegido: es una hoja viva.
    exc3 = ExcelCompiler(ruta)
    antes = exc3.evaluate("'%s'!C%d" % (H_REP, REF_TOT + 4))
    exc3.set_value("'%s'!C6" % H_REP, ESCENARIOS[3][0])
    despues = exc3.evaluate("'%s'!C%d" % (H_REP, REF_TOT + 4))
    prueba('al pasar a «Crisis del cacao» se rompen más referencias que en el '
           'escenario de trabajo', despues >= antes,
           'de %r a %r referencias rotas' % (antes, despues))

    # 5. El total de kilos de cobertura del año es la suma de las 28 filas.
    kilos = [v(H_COB, 'P%d' % (REF_INI + i)) for i in range(len(PERFILES))]
    total = v(H_COB, 'P%d' % REF_TOT)
    prueba('los kilos de cobertura del año suman las 28 referencias',
           abs(sum(kilos) - total) < 0.01,
           '%.1f frente a %.1f' % (sum(kilos), total))

    # 6. El consumo por cobertura reparte el total sin perder un kilo.
    por_cob = [v(H_COB, 'C%d' % (CONS_INI + i)) for i in range(len(COBS))]
    prueba('el consumo desglosado por cobertura suma el total del año',
           abs(sum(por_cob) - total) < 0.01, '%.1f' % sum(por_cob))

    return ok, fallos


# --------------------------------------------------------------------------
def main():
    D.gate_legal(IDS_LEGALES)
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_parametros(wb)
    hoja_cobertura(wb)
    hoja_escenarios(wb)
    hoja_repercusion(wb)
    hoja_stock(wb)

    res = X.cerrar(wb, NOMBRE, TITULO, mapa_celdas(), NOTAS_MAPA)

    print('escrito: %s' % res['ruta'])
    print('hojas: %d · fórmulas: %d · celdas verdes: %d · verdes vacías: %d'
          % (res['hojas'], res['formulas'], res['verdes'],
             len(res['verdes_vacias'])))
    print('fórmulas que devuelven «sin dato» a propósito: %d' % res['sin_dato'])
    print('notas legales: %d · notas de fuente sectorial: %d · etiquetas en el '
          'mapa: %d' % (res['notas_legales'], res['notas_sector'], res['mapa']))
    print('inject_cache: %s' % res['cache'])
    ok, fallos = demo(res['ruta'])
    for t in ok:
        print('  demo OK  · %s' % t)
    for t in fallos:
        print('  demo FALLA · %s' % t)
    if fallos:
        raise SystemExit('demos con fallos: %d' % len(fallos))


if __name__ == '__main__':
    main()
