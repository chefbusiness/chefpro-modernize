#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_campanas-y-valle-del-ano.py — libro 6 de «Cómo Montar una Chocolatería»
(SPEC §2.2 fila 6; decisiones D32, D35 y D36).

Hojas: Instrucciones · Parámetros · Calendario de Campañas · Peso sobre el Año ·
Capacidad vs Demanda del Pico · Refuerzo y Tesorería · El Valle de Agosto.

QUÉ DECIDE ESTE LIBRO
---------------------
Si aguantas Navidad con el obrador que estás montando, y de qué vives en julio y
en agosto. No es un calendario: es la ECONOMÍA del pico y del valle.

FRONTERA K2 (SPEC §2.2), y va escrita en «Instrucciones»
--------------------------------------------------------
El `BONUS-02-calendario-anual-tareas.xlsx` del Kit de Tareas Chocolatería (12 €)
pone las FECHAS y el qué hay que hacer. Este libro pone los EUROS y el «si
aguantas». Las doce filas bajan aquí como ETIQUETAS declaradas —copia de
`BONUS-02-calendario-anual-tareas.xlsx!Calendario`— y sus «Acciones clave» y sus
«Productos destacados» se citan literales y NO se reescriben.

DECISIONES TÉCNICAS
-------------------
* **D35, las DOCE filas del kit, con COMUNIONES dentro.** Siete meses «Alta»
  (feb, mar, abr, may, oct, nov, dic), cuatro «Media» (ene, jun, jul, sep) y UNO
  «Baja» (ago). Las comuniones son campaña PROPIA —lo que las distingue de
  Pascua es la antelación de pedido y el detalle de mesa personalizado— y
  sostienen abril, mayo y junio. El generador ABORTA si falta un mes.
* **D36, el valle es AGOSTO y lo que para es el OBRADOR, no la caja.** Un mes
  «Baja» de doce. La tienda abre para el turista aunque el obrador pare; los
  envíos se paran de junio a septiembre, y eso es canal ONLINE, no mostrador.
  La hoja calcula la caída del margen al cambiar el mix y los gastos fijos
  contra una facturación MENOR PERO NO NULA. Prohibidos «valle de junio-agosto»,
  «un valle de tres meses» y «fijos que siguen corriendo con la caja parada».
* **D32, cruce 6 ← 1, sin una sola fórmula entre ficheros.** La capacidad diaria
  del obrador es una celda VERDE «trae aquí la cifra de
  `capacidad-obrador-y-clima.xlsx!Cuello de Botella!<Celda>`» con su valor por
  defecto declarado, más una **fila de CUADRE** con semáforo.
* **Todo se cuenta en BOMBONES DE OBRADOR, no en tickets.** Una caja de 35
  bombones es UNA venta y TREINTA Y SEIS bombones de obrador (los 35 bombones más
  el montaje de la caja). Medir el pico en unidades vendidas es lo que hace
  creer que Navidad cabe.
* Cero constantes dentro de fórmulas —los días de la semana y los del año viven
  en «Parámetros»—; `IFERROR(...,"")` en toda división; «sin dato» = `""`;
  semáforos con `ISNUMBER`; DV contra RANGO. Prohibidas INDIRECT, COUNTA, PMT,
  OFFSET, XLOOKUP, LET, LAMBDA, RANK, NETWORKDAYS e IRR.

Salida fija: build/campanas-y-valle-del-ano.xlsx + su mapa.
Uso: /usr/local/bin/python3 gen_campanas-y-valle-del-ano.py
Via: Claude Code
"""
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Font

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import _comun_libros_4_6 as C                                  # noqa: E402
import datos_ejemplo as D                                      # noqa: E402
import motor                                                   # noqa: E402

NOMBRE = 'campanas-y-valle-del-ano'
TITULO = 'Campañas y Valle del Año'

H_INS = 'Instrucciones'
H_PAR = 'Parámetros'
H_CAL = 'Calendario de Campañas'
H_ANO = 'Peso sobre el Año'
H_CAP = 'Capacidad vs Demanda del Pico'
H_REF = 'Refuerzo y Tesorería'
H_VAL = 'El Valle de Agosto'

QPAR = "'" + H_PAR + "'!"
QCAL = "'" + H_CAL + "'!"
QANO = "'" + H_ANO + "'!"
QCAP = "'" + H_CAP + "'!"
QREF = "'" + H_REF + "'!"

CAMPANAS = sorted(D.CAMPANAS, key=lambda c: c['mes'])
NM = len(CAMPANAS)                                  # 12
MES_VALLE = D.VALLE['mes']                          # 8

#: BOMBONES de obrador que produce una unidad del producto estrella. Un bombón
#: suelto es uno; una caja son los bombones que lleva MÁS el montaje de la caja.
#: Supuesto declarado, derivado de la composición de cada caja en el libro 4.
#: Se cuenta en BOMBONES AL DÍA porque es la unidad en la que el libro 1 publica
#: la capacidad («Bombones al día que permite el conjunto»): comparar dos
#: magnitudes que se llaman igual y miden cosas distintas es el defecto que la
#: fila de CUADRE viene a cerrar.
def piezas_obrador_por_unidad(rid):
    r = D.ref(rid)
    if D.es_caja(r):
        return sum(n for _i, n in r['composicion_caja']) + 1
    return 1


#: Días de adelanto que admite el producto estrella de cada campaña. Supuesto
#: declarado, y no es una cifra libre: lo que se puede adelantar y congelar o
#: guardar en cámara lo manda la vida útil que publica el kit (10-15 días la
#: ganache fresca, 12-18 meses la tableta). Por eso una caja de bombones de
#: ganache admite mucho menos adelanto que una figura o una tableta.
DIAS_ADELANTO = {1: 20, 2: 8, 3: 8, 4: 20, 5: 8, 6: 8,
                 7: 20, 8: 20, 9: 8, 10: 20, 11: 3, 12: 8}

#: Inversión de temporada por campaña, en euros y como CIFRA DE CAMPAÑA, no como
#: «tantos moldes por tanto cada uno»: los moldes de policarbonato valen entre
#: 24,20 y 42,83 EUR/ud (`CHS-45a`) y publicar un número de moldes por un precio
#: elegido es la aritmética que la SPEC prohíbe (D23a). Supuestos declarados.
INVERSION_TEMPORADA = {1: (0.0, 120.0), 2: (280.0, 420.0), 3: (0.0, 180.0),
                       4: (520.0, 380.0), 5: (240.0, 560.0), 6: (0.0, 260.0),
                       7: (0.0, 220.0), 8: (0.0, 0.0), 9: (0.0, 340.0),
                       10: (180.0, 200.0), 11: (140.0, 380.0),
                       12: (450.0, 980.0)}

#: Personas de refuerzo y horas por persona: las publica `datos_ejemplo` fila a
#: fila (`refuerzo_personas`, `refuerzo_horas_persona`), y son supuestos.

# ---------------------------------------------------------------- Parámetros
SEC_VOL = 5
PAR_CAB = 6
P_VENTAS = 'B7'
P_CLI = 'B8'
P_PZVTA = 'B9'
P_DIAS = 'B10'
P_TICKET = 'B11'
P_PZOBR = 'B12'
P_HTURNO = 'B13'
P_MBANO = 'B14'
P_MBVER = 'B15'
P_IVA = 'B16'

SEC_REF = 18
P_BRUTO = 'B19'
P_PAGAS = 'B20'
P_SS = 'B21'
P_HANIO = 'B22'
P_CHORA = 'B23'

SEC_DIN = 25
P_INT = 'B26'
P_FIJOS = 'B27'
P_UMB = 'B28'
P_TOL = 'B29'
P_DSEM = 'B30'
P_DANO = 'B31'
PAR_PIE = 33


def A(coord):
    return QPAR + '$' + coord[0] + '$' + coord[1:]


# ------------------------------------------------------- Filas de doce meses
FIL_CAB = 6
FIL_INI = 7
FIL_FIN = FIL_INI + NM - 1
FIL_TOT = FIL_FIN + 1
FILA_MES = dict((c['mes'], FIL_INI + i) for i, c in enumerate(CAMPANAS))
FILA_VALLE = FILA_MES[MES_VALLE]

# --------------------------------------------------- Peso sobre el Año: pico
PIC_SEC = FIL_TOT + 2
PIC_CAB = PIC_SEC + 1
PIC_INI = PIC_CAB + 1
PIC_FIN = PIC_INI + NM - 1
PIC_TOT = PIC_FIN + 1
PIC_CONTR = PIC_TOT + 2

# --------------------------------------------- Capacidad: el cruce, arriba
CAP_SECC = 5
CAP_TRAE = 'B6'
CAP_ORIG = 'B7'
CAP_DESV = 'B8'
CAP_CUAD = 'B9'
CAP_CAB = 11
CAP_INI = 12
CAP_FIN = CAP_INI + NM - 1
CAP_TOT = CAP_FIN + 1
CAP_NOAG = CAP_TOT + 2

#: Valor por defecto de la capacidad, declarado como supuesto. Sale de las horas
#: PRODUCTIVAS del obrador de La Almendra (2 jornadas de obrador por 8 horas por
#: el 85 % de horas a pie de mesa = 816 minutos al día) y de los minutos por
#: pieza de obrador que publica el libro 4 ponderados por el mix (1,75 minutos).
#: El dato BUENO lo calcula la hoja «Cuello de Botella» del libro 1 por EQUIPO
#: -kg/hora de la atemperadora, moldes y piezas por molde- y hay que copiarlo.
#: 512, leído en `build/mapa-capacidad-obrador-y-clima.json` el 12-09-2026:
#: «Bombones al día que permite el conjunto», `Cuello de Botella!B7`, con el
#: puesto de envasado y montaje de cajas como equipo que limita.
CAPACIDAD_DEFECTO = 512
CELDA_ORIGEN_CAPACIDAD = 'capacidad-obrador-y-clima.xlsx!Cuello de Botella!B7'
#: 472 bombones al día en velocidad de crucero: es la misma magnitud que el
#: libro 1 publica como «Bombones al día objetivo» (`Cuello de Botella!B6`,
#: 471,81). Aquí es celda VERDE y supuesto declarado, no un cruce: el cruce
#: declarado entre estos dos libros es UNO, el de la capacidad.
PIEZAS_OBRADOR_DIA = 472

# --------------------------------------------------------------- El Valle
VAL_INI = 6
V_MES = VAL_INI
V_MESES_BAJA = VAL_INI + 1
V_PARA_OBR = VAL_INI + 2
V_PARA_ENV = VAL_INI + 3
V_MESES_ENV = VAL_INI + 4
V_VTA_AGO = VAL_INI + 5
V_VTA_MED = VAL_INI + 6
V_RATIO = VAL_INI + 7
V_MB_ANO = VAL_INI + 8
V_MB_VER = VAL_INI + 9
V_CAIDA = VAL_INI + 10
V_MBE_AGO = VAL_INI + 11
V_MBE_MED = VAL_INI + 12
V_FIJOS = VAL_INI + 13
V_RES_AGO = VAL_INI + 14
V_RES_MED = VAL_INI + 15
V_DIF = VAL_INI + 16
V_VER = VAL_INI + 17

VC_SEC = V_VER + 2
VC_CAMP = VC_SEC + 1
VC_ANO = VC_SEC + 2
VC_PCT = VC_SEC + 3
VC_VER = VC_SEC + 4
VAL_NOTA = VC_VER + 2
VAL_LISTAS = VAL_NOTA + 6

SI_NO = ('Sí', 'No')


# ==========================================================================
# Hoja «Instrucciones»
# ==========================================================================
PASOS = [
    '1. Hoja «Parámetros». Lo primero son las ventas del año y las piezas de '
    'OBRADOR que salen un día normal, que no son lo mismo que las ventas: una '
    'caja de 35 bombones es UNA venta y treinta y seis bombones de obrador. '
    'Después, el coste por hora del refuerzo, que se calcula con el bruto de '
    'tu convenio, las pagas y la Seguridad Social.',
    '2. Hoja «Calendario de Campañas». Las doce filas son las del '
    'BONUS-02-calendario-anual-tareas.xlsx del Kit de Tareas Chocolatería: las '
    'fechas, las acciones clave y los productos destacados están copiados de '
    'ahí y no se tocan. Lo que rellenas tú son las unidades del producto '
    'estrella un día normal y un día de pico, su PVP y los días que dura la '
    'campaña. De ahí salen los euros.',
    '3. Hoja «Peso sobre el Año». Doce coeficientes que reparten las ventas del '
    'año, más el peso de cada campaña. Los coeficientes son supuestos y su '
    'forma la dicta el calendario del kit: diciembre arriba, agosto abajo y '
    'siete meses «Alta». Sustitúyelos por los tuyos en cuanto tengas un año de '
    'TPV.',
    '4. Hoja «Capacidad vs Demanda del Pico». Arriba va la capacidad diaria del '
    'obrador, que se COPIA a mano de la hoja «Cuello de Botella» del libro 1: '
    'no hay ninguna fórmula entre ficheros, y por eso hay una fila de CUADRE '
    'que avisa si las dos cifras se separan. Debajo, mes a mes, si aguantas.',
    '5. Hoja «Refuerzo y Tesorería». Personas de refuerzo, horas, antelación de '
    'compra de moldes y de packaging, y el dinero que eso deja parado. El '
    'resultado incremental de cada campaña es lo que de verdad te deja, ya '
    'descontado el refuerzo y el coste de tener el dinero quieto.',
    '6. Hoja «El Valle de Agosto». Un mes «Baja» de doce. Lo que para es el '
    'obrador, no la caja: la tienda abre para el turista. La hoja calcula la '
    'caída del margen al cambiar el mix -menos ganache fresca, más tableta y '
    'producto estable- y pone los gastos fijos contra una facturación menor '
    'pero NO nula.',
]

NOTAS_LIBRO = [
    'EL CALENDARIO NO ES DE ESTE LIBRO, Y NO SE REESCRIBE. Las fechas, las '
    'acciones clave y los productos destacados de los doce meses son los del '
    'BONUS-02-calendario-anual-tareas.xlsx del Kit de Tareas Chocolatería '
    '(12 €). Aquí están copiados para que las filas tengan nombre y para que '
    'los euros cuelguen de algo, no para sustituirlo: si tienes el kit, '
    'trabaja con él al lado.',
    'LAS COMUNIONES SON CAMPAÑA PROPIA, NO LA COLA DE PASCUA. Lo que las '
    'distingue no es el producto: es que el cliente encarga con seis semanas '
    'de antelación un detalle de mesa personalizado, así que el obrador '
    'trabaja contra pedido firme y con señal -merma cero y tesorería a '
    'favor-. Y es la única campaña que reparte su carga en TRES meses (abril, '
    'mayo y junio) en vez de concentrarla en una semana.',
    'EL VALLE ES AGOSTO, Y ES UN MES DE DOCE. El calendario del kit tiene '
    'SIETE meses «Alta», CUATRO «Media» y UNO «Baja», y el único «Baja» es '
    'agosto. Junio y julio son «Media»: en junio empieza a cambiar el '
    'catálogo y en julio entra el turista. Contar un «valle de tres meses» '
    'contradice al calendario que la propia casa publica y te hace '
    'presupuestar un agujero que no existe.',
    'Y LO QUE PARA EN AGOSTO ES EL OBRADOR, NO LA CAJA. El literal del kit es '
    '«la tienda abre para el turista aunque el obrador pare». Se para por tres '
    'motivos que el propio kit nombra: mantenimiento profundo, vacaciones '
    'escalonadas y el cierre del pedido de coberturas de Navidad. La '
    'facturación de agosto es MENOR, no nula, y por eso la hoja pone los '
    'gastos fijos contra lo que sí entra.',
    'LOS ENVÍOS SON OTRA COSA, Y SE PARAN DE JUNIO A SEPTIEMBRE. Esa parada es '
    'de CANAL ONLINE: el chocolate no viaja en verano sin cadena de frío, y '
    'los operadores del sector apagan los envíos a mediados de junio. El '
    'mostrador sigue vivo los cuatro meses, y en julio y agosto con turista. '
    'Meter los dos en el mismo saco es lo que produce el falso valle largo.',
    'EL PICO SE MIDE EN BOMBONES DE OBRADOR, NO EN TICKETS. Una caja de 35 '
    'bombones es UNA venta y TREINTA Y SEIS bombones de obrador: los 35 bombones '
    'más el montaje de la caja. Si mides Navidad en unidades vendidas, el pico '
    'parece pequeño y cabe; medido en bombones de obrador, normalmente no cabe, '
    'y ésa es justo la decisión que hay que tomar en octubre y no en '
    'diciembre.',
    'LO QUE SE PUEDE ADELANTAR LO MANDA LA VIDA ÚTIL, NO LAS GANAS. La tableta '
    'y la figura aguantan meses; una caja de bombones de ganache fresca, entre '
    'diez y quince días según el propio kit. Por eso cada campaña tiene su '
    'columna de días de adelanto y no un número único: adelantar producción de '
    'ganache es tirar dinero con una semana de diferencia.',
    'LA CAPACIDAD DEL OBRADOR SE COPIA A MANO DEL LIBRO 1, Y ESO ES A '
    'PROPÓSITO. Ningún libro de este pack tiene una fórmula que apunte a otro '
    'fichero: si el otro no está abierto, o le cambias el nombre, o lo mueves '
    'de carpeta, la fórmula se rompe y el número desaparece sin avisar. Lo que '
    'sí hay es una fila de CUADRE que compara lo que has traído con lo que '
    'aquel libro publica y avisa si se han separado.',
]

CADENCIA = ('Cada cuánto se usa este libro: el «Calendario de Campañas» y el '
            '«Peso sobre el Año», UNA VEZ AL AÑO, en enero, cuando cierras '
            'Reyes y tienes los números frescos. «Capacidad vs Demanda» y '
            '«Refuerzo y Tesorería», UNA VEZ POR CAMPAÑA y con la antelación '
            'que diga la propia hoja: para Navidad, doce semanas antes de los '
            'moldes y catorce de packaging, es decir en septiembre. «El Valle '
            'de Agosto», en mayo, que es cuando todavía se puede decidir qué '
            'se produce y qué se compra hecho.')


def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS, 0)
    ws.column_dimensions['A'].width = 90.0
    C.cabecera_hoja(ws, TITULO)
    motor.val(ws, 'A3', 'Para qué sirve: saber si aguantas Navidad antes de que '
                        'llegue, y de qué vives en julio y en agosto.')
    ws['A3'].font = Font(italic=True, size=9)

    C.seccion(ws, 'A5', 'Instrucciones de uso')
    fila = 6
    for paso in PASOS:
        motor.val(ws, 'A%d' % fila, paso, wrap=True)
        ws.row_dimensions[fila].height = 72
        fila += 1
    fila += 1
    C.entrada(ws, 'A%d' % fila, C.LEYENDA_VERDE,
              etiqueta='Leyenda de celdas verdes')
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Lo que conviene saber antes de empezar')
    fila += 1
    for nota in NOTAS_LIBRO:
        motor.val(ws, 'A%d' % fila, nota, wrap=True)
        ws.row_dimensions[fila].height = 86
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, CADENCIA, wrap=True)
    ws.row_dimensions[fila].height = 62
    fila += 2
    motor.val(ws, 'A%d' % fila, C.DESPROTEGER, wrap=True)
    ws.row_dimensions[fila].height = 30
    fila += 2
    motor.val(ws, 'A%d' % fila, C.BIO, wrap=True)
    fila += 1
    motor.val(ws, 'A%d' % fila, C.VERSION_LINE)
    ws['A%d' % fila].font = Font(size=8, italic=True)
    C.setup(ws, landscape=False)
    return ws


# ==========================================================================
# Hoja «Parámetros»
# ==========================================================================
def par(ws, fila, etiqueta, valor, fmt, unidad, fuente, nota, formula=None,
        id_chn=None):
    motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
    if formula is not None:
        cel = motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=True)
        C.crema(cel)
    else:
        cel = C.entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
    motor.val(ws, 'C%d' % fila, unidad)
    motor.val(ws, 'D%d' % fila, fuente)
    ws['D%d' % fila].font = Font(size=8, color=C.GRIS)
    motor.val(ws, 'E%d' % fila, nota, wrap=True)
    ws['E%d' % fila].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[fila].height = 44
    if id_chn:
        C.nota_celda(ws, cel.coordinate, id_chn)
    return cel


def hoja_parametros(wb):
    ws = wb.create_sheet(H_PAR)
    C.cabecera_hoja(ws, 'Parámetros')
    motor.val(ws, 'A3', 'Ninguna fórmula de este libro lleva un número dentro: '
                        'ni los días de la semana, ni los del año, ni el tipo '
                        'de interés. Todo está aquí y todo se puede cambiar.')
    ws['A3'].font = Font(italic=True, size=9)
    for letra, ancho in (('A', 54), ('B', 16), ('C', 16), ('D', 22), ('E', 88)):
        ws.column_dimensions[letra].width = ancho

    C.seccion(ws, 'A%d' % SEC_VOL, 'Volumen, precio y margen')
    C.encabezados(ws, PAR_CAB, [
        ('A', 'Parámetro', None), ('B', 'Valor', None), ('C', 'Unidad', None),
        ('D', 'De dónde sale', None), ('E', 'Nota', None)], alto=26)
    par(ws, 7, 'Ventas anuales sin IVA en velocidad de crucero',
        round(D.ventas_anuales_sin_iva(), 2), C.EUR, 'EUR/año', 'supuesto',
        'Sale de la carta y del tráfico supuesto de La Almendra: clientes al '
        'día por piezas por ticket por PVP medio ponderado. NO es un dato del '
        'sector -no existe ticket medio publicado de chocolatería- y se '
        'sustituye por el de tu plan financiero.')
    par(ws, 8, 'Clientes al día en velocidad de crucero',
        D.P('tickets_dia_crucero'), C.ENT, 'clientes/día', 'supuesto',
        'Mídelo con tu TPV en dos semanas y cámbialo.')
    par(ws, 9, 'Piezas de VENTA al día en velocidad de crucero',
        round(D.piezas_dia_crucero(), 1), C.DEC1, 'ventas/día', 'supuesto',
        'Clientes al día por piezas por ticket. Una caja cuenta como UNA.')
    par(ws, 10, 'Días de apertura al año', D.NEGOCIO['dias_apertura_anio'],
        C.ENT, 'días', 'supuesto', D.NEGOCIO['nota_dias_apertura'])
    par(ws, 11, 'Ticket medio sin IVA', None, C.EUR, 'EUR/ticket', 'calculado',
        'Ventas del año entre clientes al día por días de apertura. No se '
        'teclea: si lo tecleas y encima pones las ventas, se pueden '
        'contradecir.',
        formula='=IFERROR(%s/(%s*%s),"")' % (A(P_VENTAS), A(P_CLI), A(P_DIAS)))
    par(ws, 12, 'Bombones al día que salen del obrador en velocidad de crucero',
        PIEZAS_OBRADOR_DIA, C.ENT, 'piezas/día', 'supuesto',
        'NO es lo mismo que las ventas: una caja de 35 bombones es UNA venta y '
        'treinta y seis bombones de obrador. Es la MISMA magnitud que el libro '
        '1 publica como «Bombones al día objetivo» (471,81), y por eso se mide '
        'en bombones y no en tickets: comparar la capacidad con los tickets es '
        'lo que hace creer que Navidad cabe.')
    par(ws, 13, 'Horas de obrador al día en jornada normal',
        D.NEGOCIO['horas_turno'], C.DEC1, 'horas', 'supuesto',
        'Horas de reloj que el obrador está en marcha un día cualquiera, no '
        'horas de apertura de la tienda.')
    par(ws, 14, 'Margen bruto medio con el mix de todo el año',
        round(1.0 - D.food_cost_carta(), 4), C.PCT, 'sobre ventas', 'supuesto',
        'En el ejemplo sale de la carta de La Almendra (libro 4, hoja «Mix y '
        'Ticket Medio»), y aquí es una celda verde: este libro no tiene la '
        'carta dentro y no puede recalcularlo.')
    par(ws, 15, 'Margen bruto medio con el mix de julio y agosto',
        round(1.0 - D.food_cost_carta(True), 4), C.PCT, 'sobre ventas',
        'supuesto',
        'Menos ganache fresca y más tableta y producto estable -literal del '
        'kit-. El margen NO sube por vender tableta: la tableta lleva más '
        'chocolate por pieza y menos manos, y en este ejemplo el mix de verano '
        'deja algo MENOS de margen. Comprueba el tuyo antes de darlo por '
        'bueno.')
    iv = par(ws, 16, 'IVA del chocolate', D.P('iva_producto'), C.PCT,
             'sobre base', 'CHN-71',
             'El chocolate va al 10 % POR EXCLUSIÓN: la lista del 4 % es '
             'cerrada y no lo nombra, y tampoco está entre las dos exclusiones '
             'del 10 %. Se usa aquí para pasar la facturación de campaña, que '
             'se escribe CON IVA porque es precio de mostrador, a base '
             'imponible.', id_chn='CHN-71')
    del iv

    C.seccion(ws, 'A%d' % SEC_REF,
              'Coste del refuerzo (convenio de Madrid, marcado EJEMPLO)')
    br = par(ws, 19, 'Bruto mensual del grupo de convenio del refuerzo',
             D.CONVENIO[4][2], C.EUR, 'EUR/mes', 'CHN-65b',
             'Grupo 5, «%s», del convenio de la Comunidad de Madrid (código '
             '%s, denominación oficial en REGCON «%s»). Es un EJEMPLO: '
             'sustitúyelo por el de TU convenio. Y ojo: está PROBADO que no '
             'existe un convenio estatal del chocolate.'
             % (D.CONVENIO[4][1], D.CONVENIO_CODIGO, D.CONVENIO_DENOMINACION),
             id_chn='CHN-65b')
    del br
    par(ws, 20, 'Pagas del convenio al año', D.P('pagas_convenio'), C.ENT,
        'pagas', 'CHN-65b',
        'El convenio de Madrid paga 15, no 14: cambia el coste mes a mes.',
        id_chn='CHN-65b')
    par(ws, 21, 'Seguridad Social a cargo de la empresa', D.P('ss_empresa'),
        C.PCT, 'sobre bruto', 'motor.PARAMETROS',
        'Contingencias comunes, desempleo, FOGASA y formación. Un refuerzo de '
        'campaña cuesta un tercio más de lo que pone su nómina.')
    par(ws, 22, 'Horas anuales de contrato a jornada completa',
        D.P('horas_anuales_contrato'), C.ENT, 'horas/año', 'supuesto',
        '40 horas por 52 semanas son 2.080, menos vacaciones y festivos.')
    par(ws, 23, 'Coste por hora PAGADA del refuerzo', None, C.EUR, 'EUR/hora',
        'calculado',
        'Bruto mensual por pagas por (1 más Seguridad Social), entre las horas '
        'anuales de contrato. NO es el «coste de la hora de obrador» del libro '
        '4, que se calcula sobre horas PRODUCTIVAS y sobre otros grupos: las '
        'dos son correctas y miden denominadores distintos.',
        formula='=IFERROR(%s*%s*(1+%s)/%s,"")'
                % (A(P_BRUTO), A(P_PAGAS), A(P_SS), A(P_HANIO)))

    C.seccion(ws, 'A%d' % SEC_DIN, 'Dinero, umbrales y calendario')
    par(ws, 26, 'Tipo de interés anual del circulante',
        D.FINANCIACION['tipo_nominal'], C.PCT, 'anual', 'supuesto',
        'Coste del dinero parado en moldes y packaging de temporada. Si '
        'financias la compra con póliza, pon el tipo de tu póliza; si la pagas '
        'de tu caja, pon lo que te costaría pedirla.')
    par(ws, 27, 'Gastos fijos mensuales', round(D.gastos_fijos_mensuales(), 2),
        C.EUR, 'EUR/mes', 'supuesto',
        'Los del año de crucero, con personal, autónomos, alquiler, '
        'suministros, amortización y financieros dentro. Es la cifra contra la '
        'que se mide agosto, y por eso es una celda verde: el que manda es tu '
        'plan financiero.')
    par(ws, 28, 'Umbral para marcar una campaña como grande', 0.08, C.PCT,
        'de las ventas del año', 'supuesto',
        'Criterio de la casa, no del sector. Por encima de este peso, la '
        'campaña deja de ser una fecha y pasa a ser una decisión de compra, de '
        'personal y de tesorería.')
    par(ws, 29, 'Tolerancia de las filas de CUADRE', 0.02, C.PCT, 'desviación',
        'supuesto',
        'Por encima de esta desviación, la fila de CUADRE avisa de que lo que '
        'has traído de otro libro ya no es lo que aquel publica.')
    par(ws, 30, 'Días por semana', 7, C.ENT, 'días', 'calendario',
        'Vive aquí porque las antelaciones de compra se cuentan en SEMANAS y '
        'el coste financiero en días: ninguna fórmula del libro lleva un '
        'número dentro.')
    par(ws, 31, 'Días del año para el coste financiero', 365, C.ENT, 'días',
        'convención',
        'Base de cálculo del interés del circulante. Tu banco puede usar 360: '
        'cámbialo aquí y todo el libro se recalcula.')

    motor.val(ws, 'A%d' % PAR_PIE, C.VERSION_LINE)
    ws['A%d' % PAR_PIE].font = Font(size=8, italic=True)
    C.setup(ws, landscape=True)
    return ws


# ==========================================================================
# Hoja «Calendario de Campañas» (D35)
# ==========================================================================
def hoja_calendario(wb):
    ws = wb.create_sheet(H_CAL)
    C.cabecera_hoja(ws, 'Calendario de Campañas')
    motor.val(ws, 'A3', 'Las FECHAS, las acciones clave y los productos '
                        'destacados son del BONUS-02-calendario-anual-tareas.xlsx '
                        'del Kit de Tareas Chocolatería, copiados fila a fila y '
                        'SIN reescribir. Esta hoja pone los EUROS.')
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, FIL_CAB, [
        ('A', 'Mes', 12), ('B', 'Temporada que declara el kit', 13),
        ('C', 'Campaña', 30), ('D', '¿Campaña propia?', 12),
        ('E', 'Producto estrella', 40),
        ('F', 'Bombones de obrador por unidad', 13),
        ('G', 'Unidades al día fuera de campaña', 13),
        ('H', 'Unidades al día en el pico', 13),
        ('I', 'PVP de campaña con IVA (EUR)', 13),
        ('J', 'Días de campaña', 12), ('K', 'Factor del pico', 11),
        ('L', 'Unidades incrementales de la campaña', 14),
        ('M', 'Facturación de la campaña con IVA (EUR)', 14),
        ('N', 'Facturación de la campaña sin IVA (EUR)', 14),
        ('O', 'Facturación INCREMENTAL sin IVA (EUR)', 14),
        ('P', 'Días de adelanto que admite', 13),
        ('Q', 'Acciones clave que publica el kit', 72),
        ('R', 'Productos destacados que publica el kit', 40),
        ('S', 'Nota', 66)], alto=74)
    for i, c in enumerate(CAMPANAS):
        fila = FIL_INI + i
        estrella = D.ref(c['producto_estrella'])
        motor.val(ws, 'A%d' % fila, c['nombre_mes'])
        motor.val(ws, 'B%d' % fila, c['temporada'])
        motor.val(ws, 'C%d' % fila, c['campana'], wrap=True)
        motor.val(ws, 'D%d' % fila, 'Sí' if c['campana_propia'] else 'No')
        motor.val(ws, 'E%d' % fila,
                  '%s - %s' % (estrella['id'], estrella['nombre']), wrap=True)
        C.entrada(ws, 'F%d' % fila,
                  piezas_obrador_por_unidad(c['producto_estrella']), fmt=C.ENT,
                  etiqueta='Bombones de obrador por unidad en %s' % c['nombre_mes'])
        C.entrada(ws, 'G%d' % fila, c['uds_dia_normal'], fmt=C.ENT,
                  etiqueta='Unidades al día fuera de campaña en %s' % c['nombre_mes'])
        C.entrada(ws, 'H%d' % fila, c['uds_dia_pico'], fmt=C.ENT,
                  etiqueta='Unidades al día en el pico de %s' % c['nombre_mes'])
        C.entrada(ws, 'I%d' % fila, c['pvp_campana'], fmt=C.EUR,
                  etiqueta='PVP de campaña de %s' % c['nombre_mes'])
        C.entrada(ws, 'J%d' % fila, c['dias_campana'], fmt=C.ENT,
                  etiqueta='Días de campaña de %s' % c['nombre_mes'])
        motor.f(ws, 'K%d' % fila, '=IFERROR(H%d/G%d,"")' % (fila, fila),
                fmt=C.DEC1)
        motor.f(ws, 'L%d' % fila, '=IFERROR((H%d-G%d)*J%d,"")'
                % (fila, fila, fila), fmt=C.ENT)
        motor.f(ws, 'M%d' % fila, '=IFERROR(H%d*J%d*I%d,"")'
                % (fila, fila, fila), fmt=C.EUR)
        motor.f(ws, 'N%d' % fila, '=IFERROR(M%d/(1+%s),"")'
                % (fila, A(P_IVA)), fmt=C.EUR)
        motor.f(ws, 'O%d' % fila, '=IFERROR(L%d*I%d/(1+%s),"")'
                % (fila, fila, A(P_IVA)), fmt=C.EUR)
        C.entrada(ws, 'P%d' % fila, DIAS_ADELANTO[c['mes']], fmt=C.ENT,
                  etiqueta='Días de adelanto de %s' % c['nombre_mes'])
        motor.val(ws, 'Q%d' % fila, c['acciones_kit'], wrap=True)
        ws['Q%d' % fila].font = Font(size=8)
        motor.val(ws, 'R%d' % fila, c['productos_kit'], wrap=True)
        ws['R%d' % fila].font = Font(size=8)
        motor.val(ws, 'S%d' % fila, c['nota'], wrap=True)
        ws['S%d' % fila].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[fila].height = 78
    motor.val(ws, 'A%d' % FIL_TOT, 'TOTAL del año', bold=True)
    for col, fmt in (('J', C.ENT), ('L', C.ENT), ('M', C.EUR), ('N', C.EUR),
                     ('O', C.EUR)):
        motor.f(ws, '%s%d' % (col, FIL_TOT),
                '=SUM(%s%d:%s%d)' % (col, FIL_INI, col, FIL_FIN), fmt=fmt,
                bold=True)

    fila = FIL_TOT + 2
    motor.val(ws, 'A%d' % fila,
              'La campaña de COMUNIONES (abril, mayo y junio) es la única que '
              'reparte su carga en tres meses en vez de concentrarla en una '
              'semana, y es campaña PROPIA, no la cola de Pascua: lo que la '
              'distingue es que se encarga con seis semanas de antelación un '
              'detalle de mesa personalizado, con señal. El obrador trabaja '
              'contra pedido firme: merma cero y tesorería a favor.', wrap=True)
    ws['A%d' % fila].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[fila].height = 58
    motor.val(ws, 'A%d' % (fila + 2), C.VERSION_LINE)
    ws['A%d' % (fila + 2)].font = Font(size=8, italic=True)
    C.setup(ws, landscape=True, titulos='%d:%d' % (FIL_CAB, FIL_CAB))
    return ws


# ==========================================================================
# Hoja «Peso sobre el Año»
# ==========================================================================
def hoja_anio(wb):
    ws = wb.create_sheet(H_ANO)
    C.cabecera_hoja(ws, 'Peso sobre el Año')
    motor.val(ws, 'A3', 'Doce coeficientes que reparten las ventas del año. Son '
                        'SUPUESTOS -no existe reparto mensual publicado de '
                        'chocolatería- y su forma la dicta el calendario del '
                        'kit: diciembre arriba, agosto abajo.')
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, FIL_CAB, [
        ('A', 'Mes', 14), ('B', 'Temporada que declara el kit', 14),
        ('C', 'Coeficiente de estacionalidad', 14),
        ('D', 'Días de apertura del mes', 13),
        ('E', 'Ventas del mes sin IVA (EUR)', 15),
        ('F', 'Peso sobre el año', 12),
        ('G', 'Ventas por día de apertura (EUR)', 14),
        ('H', 'Veces un día medio', 12), ('I', 'Nota', 76)], alto=48)
    for i, c in enumerate(CAMPANAS):
        fila = FIL_INI + i
        motor.val(ws, 'A%d' % fila, c['nombre_mes'])
        motor.val(ws, 'B%d' % fila, c['temporada'])
        C.entrada(ws, 'C%d' % fila, D.ESTACIONALIDAD_MENSUAL[c['mes'] - 1],
                  fmt=C.DEC, etiqueta='Coeficiente de %s' % c['nombre_mes'])
        C.entrada(ws, 'D%d' % fila, D.DIAS_APERTURA_MES[c['mes'] - 1],
                  fmt=C.ENT, etiqueta='Días de apertura de %s' % c['nombre_mes'])
        motor.f(ws, 'E%d' % fila, '=IFERROR(%s*C%d/12,"")'
                % (A(P_VENTAS), fila), fmt=C.EUR)
        motor.f(ws, 'F%d' % fila, '=IFERROR(E%d/%s,"")' % (fila, A(P_VENTAS)),
                fmt=C.PCT)
        motor.f(ws, 'G%d' % fila, '=IFERROR(E%d/D%d,"")' % (fila, fila),
                fmt=C.EUR)
        motor.f(ws, 'H%d' % fila, '=IFERROR(G%d*%s/%s,"")'
                % (fila, A(P_DIAS), A(P_VENTAS)), fmt=C.DEC)
        ws.row_dimensions[fila].height = 22
    motor.val(ws, 'I%d' % FILA_VALLE,
              'El único mes «Baja» de los doce. Agosto NO vale cero: la tienda '
              'abre para el turista y lo que para es el obrador.', wrap=True)
    ws['I%d' % FILA_VALLE].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[FILA_VALLE].height = 34
    motor.val(ws, 'A%d' % FIL_TOT, 'TOTAL del año', bold=True)
    for col, fmt in (('C', C.DEC), ('D', C.ENT), ('E', C.EUR), ('F', C.PCT)):
        motor.f(ws, '%s%d' % (col, FIL_TOT),
                '=SUM(%s%d:%s%d)' % (col, FIL_INI, col, FIL_FIN), fmt=fmt,
                bold=True)

    # --- peso de cada campaña ---------------------------------------------
    C.seccion(ws, 'A%d' % PIC_SEC, 'Lo que pesa cada campaña sobre el año')
    C.encabezados(ws, PIC_CAB, [
        ('A', 'Campaña', None), ('B', 'Mes', None),
        ('C', 'Facturación de la campaña sin IVA (EUR)', None),
        ('D', 'Peso sobre las ventas del año', None),
        ('E', 'Facturación INCREMENTAL sin IVA (EUR)', None),
        ('F', 'Peso incremental sobre el año', None),
        ('G', '¿Campaña grande?', None), ('H', 'Nota', None)], alto=44)
    for i, c in enumerate(CAMPANAS):
        fila = PIC_INI + i
        origen = FIL_INI + i
        motor.val(ws, 'A%d' % fila, c['campana'], wrap=True)
        motor.val(ws, 'B%d' % fila, c['nombre_mes'])
        motor.f(ws, 'C%d' % fila, '=%sN%d' % (QCAL, origen), fmt=C.EUR)
        motor.f(ws, 'D%d' % fila, '=IFERROR(C%d/%s,"")' % (fila, A(P_VENTAS)),
                fmt=C.PCT)
        motor.f(ws, 'E%d' % fila, '=%sO%d' % (QCAL, origen), fmt=C.EUR)
        motor.f(ws, 'F%d' % fila, '=IFERROR(E%d/%s,"")' % (fila, A(P_VENTAS)),
                fmt=C.PCT)
        motor.f(ws, 'G%d' % fila,
                '=IF(NOT(ISNUMBER(D%d)),"",IF(D%d>=%s,"Sí","No"))'
                % (fila, fila, A(P_UMB)))
        ws.row_dimensions[fila].height = 24
    motor.val(ws, 'A%d' % PIC_TOT, 'TOTAL de las doce campañas', bold=True)
    for col, fmt in (('C', C.EUR), ('D', C.PCT), ('E', C.EUR), ('F', C.PCT)):
        motor.f(ws, '%s%d' % (col, PIC_TOT),
                '=SUM(%s%d:%s%d)' % (col, PIC_INI, col, PIC_FIN), fmt=fmt,
                bold=True)

    motor.val(ws, 'A%d' % PIC_CONTR,
              'Contraste publicado: hasta el 10 % de la venta anual en un solo '
              'evento', wrap=True)
    cel = motor.val(ws, 'B%d' % PIC_CONTR, 0.10, fmt=C.PCT)
    C.nota_sector(ws, cel.coordinate, 'CHS-34')
    motor.val(ws, 'C%d' % PIC_CONTR,
              'Es el caso EXTREMO de una compañía concreta, no una regla del '
              'sector: la fuente dice que las ventas de chocolates y dulces '
              'pueden llegar a duplicar el promedio anual en San Valentín y que '
              'hay compañías que hacen en ese solo evento hasta el 10 % de su '
              'venta anual. Sirve para saber si tu reparto es plausible, no '
              'para copiarlo.', wrap=True)
    ws['C%d' % PIC_CONTR].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[PIC_CONTR].height = 58

    fila = PIC_CONTR + 2
    motor.val(ws, 'A%d' % fila,
              'La suma de las doce campañas NO tiene que dar el 100 % del año: '
              'una campaña es lo que se vende del producto estrella en sus '
              'días, y el resto del año se vende carta. Lo que sí tiene que '
              'cuadrar es que las unidades de campaña quepan dentro de las '
              'unidades del año, y eso lo comprueba la hoja «El Valle de '
              'Agosto».', wrap=True)
    ws['A%d' % fila].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[fila].height = 50
    ws.column_dimensions['A'].width = 34
    motor.val(ws, 'A%d' % (fila + 2), C.VERSION_LINE)
    ws['A%d' % (fila + 2)].font = Font(size=8, italic=True)
    C.setup(ws, landscape=True, titulos='%d:%d' % (FIL_CAB, FIL_CAB))
    return ws


# ==========================================================================
# Hoja «Capacidad vs Demanda del Pico» (cruce 6 <- 1, D32)
# ==========================================================================
def hoja_capacidad(wb):
    ws = wb.create_sheet(H_CAP)
    C.cabecera_hoja(ws, 'Capacidad vs Demanda del Pico')
    motor.val(ws, 'A3', 'Todo se mide en BOMBONES DE OBRADOR: una caja de 35 '
                        'bombones es una venta y treinta y seis piezas de '
                        'obrador. Medir el pico en tickets es lo que hace creer '
                        'que Navidad cabe.')
    ws['A3'].font = Font(italic=True, size=9)
    for letra, ancho in (('A', 30), ('B', 16), ('C', 16), ('D', 22), ('E', 90)):
        ws.column_dimensions[letra].width = ancho

    C.seccion(ws, 'A%d' % CAP_SECC,
              'Capacidad diaria del obrador: trae aquí la cifra de '
              + CELDA_ORIGEN_CAPACIDAD)
    ws.row_dimensions[CAP_SECC].height = 30
    motor.val(ws, 'A%d' % 6,
              'Capacidad del obrador en jornada normal (bombones de obrador/día)',
              wrap=True)
    cap = C.entrada(ws, CAP_TRAE, CAPACIDAD_DEFECTO, fmt=C.ENT,
                    etiqueta='Capacidad del obrador traída del libro 1')
    motor.val(ws, 'C6', 'piezas/día')
    motor.val(ws, 'D6', 'libro 1')
    ws['D6'].font = Font(size=8, color=C.GRIS)
    motor.val(ws, 'E6',
              'COPIA a mano el resultado de la hoja «Cuello de Botella» del '
              'libro «capacidad-obrador-y-clima.xlsx» de este mismo pack: la '
              'casilla de piezas al día que permite el equipo que limita. NO '
              'hay ninguna fórmula entre ficheros -si la hubiera, se rompería '
              'al mover o renombrar el otro libro-. El valor por defecto son '
              'los 512 bombones al día que ese libro publica hoy en «Bombones '
              'al día que permite el conjunto», con el puesto de envasado y '
              'montaje de cajas como equipo que limita. Si cambias de '
              'atemperadora, de moldes o de puesto de envasado, vuelve a '
              'copiarlo.', wrap=True)
    ws['E6'].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[6].height = 78
    del cap
    motor.val(ws, 'A7',
              'Cifra que publica hoy esa hoja del libro 1', wrap=True)
    C.entrada(ws, CAP_ORIG, CAPACIDAD_DEFECTO, fmt=C.ENT,
              etiqueta='Capacidad que publica el libro 1')
    motor.val(ws, 'C7', 'piezas/día')
    motor.val(ws, 'E7',
              'Anota aquí lo que ves en el libro 1 la última vez que lo '
              'abriste. Si arriba tecleas otra cosa -porque has comprado otra '
              'máquina, o porque te lo dijo el instalador-, la fila de CUADRE '
              'te avisa en vez de dejar las dos cifras separadas en silencio.',
              wrap=True)
    ws['E7'].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[7].height = 48
    motor.val(ws, 'A8', 'Desviación entre las dos')
    motor.f(ws, CAP_DESV,
            '=IFERROR(ABS(%s-%s)/%s,"")' % (CAP_TRAE, CAP_ORIG, CAP_ORIG),
            fmt=C.PCT)
    motor.val(ws, 'A%d' % 9,
              'CUADRE: la capacidad que usas frente a la que publica el libro 1',
              bold=True)
    motor.f(ws, CAP_CUAD,
            '=IF(NOT(ISNUMBER(%s)),"",IF(%s<=%s,"CUADRA","REVISA: la capacidad '
            'que estás usando no es la que calcula el libro 1"))'
            % (CAP_DESV, CAP_DESV, A(P_TOL)), bold=True)
    motor.semaforo_isnumber(ws, CAP_DESV, '$%s' % CAP_DESV, '>', A(P_TOL))

    C.encabezados(ws, CAP_CAB, [
        ('A', 'Mes', 14), ('B', 'Campaña', 30),
        ('C', 'Bombones de obrador de base al día', 14),
        ('D', 'Unidades extra del producto estrella al día', 14),
        ('E', 'Bombones de obrador extra al día', 14),
        ('F', 'DEMANDA de bombones de obrador al día', 14),
        ('G', 'Capacidad al día', 13), ('H', 'Déficit diario', 13),
        ('I', '¿Aguanta el obrador?', 12),
        ('J', 'Horas de obrador que harían falta', 13),
        ('K', 'Excedente de un día normal', 13),
        ('L', 'Piezas adelantables antes de la campaña', 14),
        ('M', 'Déficit de la campaña tras adelantar', 14),
        ('N', 'Bombones de obrador extra en toda la campaña', 14),
        ('O', 'Nota', 70)], alto=76)
    for i, c in enumerate(CAMPANAS):
        fila = CAP_INI + i
        cal = FIL_INI + i
        ano = FIL_INI + i
        motor.val(ws, 'A%d' % fila, c['nombre_mes'])
        motor.val(ws, 'B%d' % fila, c['campana'], wrap=True)
        motor.f(ws, 'C%d' % fila, '=IFERROR(%s*%sC%d,"")'
                % (A(P_PZOBR), QANO, ano), fmt=C.ENT)
        motor.f(ws, 'D%d' % fila, '=IFERROR(%sH%d-%sG%d,"")'
                % (QCAL, cal, QCAL, cal), fmt=C.ENT)
        motor.f(ws, 'E%d' % fila, '=IFERROR(D%d*%sF%d,"")' % (fila, QCAL, cal),
                fmt=C.ENT)
        motor.f(ws, 'F%d' % fila, '=IFERROR(C%d+E%d,"")' % (fila, fila),
                fmt=C.ENT, bold=True)
        motor.f(ws, 'G%d' % fila, '=%s' % CAP_TRAE, fmt=C.ENT)
        motor.f(ws, 'H%d' % fila,
                '=IF(OR(NOT(ISNUMBER(F%d)),NOT(ISNUMBER(G%d))),"",'
                'MAX(0,F%d-G%d))' % (fila, fila, fila, fila), fmt=C.ENT)
        motor.f(ws, 'I%d' % fila,
                '=IF(NOT(ISNUMBER(H%d)),"",IF(H%d<=0,"Sí","No"))'
                % (fila, fila), bold=True)
        motor.f(ws, 'J%d' % fila, '=IFERROR(F%d*%s/G%d,"")'
                % (fila, A(P_HTURNO), fila), fmt=C.DEC1)
        motor.f(ws, 'K%d' % fila,
                '=IF(OR(NOT(ISNUMBER(G%d)),NOT(ISNUMBER(C%d))),"",'
                'MAX(0,G%d-C%d))' % (fila, fila, fila, fila), fmt=C.ENT)
        motor.f(ws, 'L%d' % fila, '=IFERROR(K%d*%sP%d,"")' % (fila, QCAL, cal),
                fmt=C.ENT)
        motor.f(ws, 'M%d' % fila,
                '=IF(OR(NOT(ISNUMBER(H%d)),NOT(ISNUMBER(L%d))),"",'
                'MAX(0,H%d*%sJ%d-L%d))' % (fila, fila, fila, QCAL, cal, fila),
                fmt=C.ENT, bold=True)
        motor.f(ws, 'N%d' % fila, '=IFERROR(E%d*%sJ%d,"")' % (fila, QCAL, cal),
                fmt=C.ENT)
        ws.row_dimensions[fila].height = 26
    motor.val(ws, 'O%d' % CAP_INI,
              'Las tres palancas, y van en este orden: adelantar producción de '
              'lo que aguanta, alargar la jornada de máquina y, sólo después, '
              'contratar refuerzo. La columna de piezas adelantables usa los '
              'días de adelanto que admite el producto estrella de cada '
              'campaña, que los manda la vida útil, no las ganas.', wrap=True)
    ws['O%d' % CAP_INI].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[CAP_INI].height = 58
    motor.val(ws, 'A%d' % CAP_TOT, 'TOTAL del año', bold=True)
    motor.f(ws, 'N%d' % CAP_TOT,
            '=SUM(N%d:N%d)' % (CAP_INI, CAP_FIN), fmt=C.ENT, bold=True)
    motor.semaforo_texto(ws, 'I%d:I%d' % (CAP_INI, CAP_FIN),
                         (('No', 'FFC7CE', '9C0006'),
                          ('Sí', 'C6EFCE', '006100')))
    motor.val(ws, 'A%d' % CAP_NOAG, 'Campañas que NO aguanta el obrador')
    motor.f(ws, 'B%d' % CAP_NOAG,
            '=COUNTIF(I%d:I%d,"No")' % (CAP_INI, CAP_FIN), fmt=C.ENT,
            bold=True)
    motor.val(ws, 'A%d' % (CAP_NOAG + 1),
              'Campañas con déficit incluso después de adelantar')
    motor.f(ws, 'B%d' % (CAP_NOAG + 1),
            '=COUNTIF(M%d:M%d,">0")' % (CAP_INI, CAP_FIN), fmt=C.ENT,
            bold=True)

    fila = CAP_NOAG + 3
    motor.val(ws, 'A%d' % fila,
              'Un «No» aquí no significa que no puedas hacer la campaña: '
              'significa que ese día, con ese equipo y esa plantilla, no cabe. '
              'Mira la columna de al lado -piezas adelantables- antes de '
              'contratar a nadie: adelantar tableta y figura es gratis y '
              'contratar no lo es.', wrap=True)
    ws['A%d' % fila].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[fila].height = 50
    motor.val(ws, 'A%d' % (fila + 2), C.VERSION_LINE)
    ws['A%d' % (fila + 2)].font = Font(size=8, italic=True)
    C.setup(ws, landscape=True, titulos='%d:%d' % (CAP_CAB, CAP_CAB))
    return ws


# ==========================================================================
# Hoja «Refuerzo y Tesorería»
# ==========================================================================
def hoja_refuerzo(wb):
    ws = wb.create_sheet(H_REF)
    C.cabecera_hoja(ws, 'Refuerzo y Tesorería')
    motor.val(ws, 'A3', 'Una campaña no cuesta sólo las horas del refuerzo: '
                        'cuesta también el dinero que dejas parado en moldes y '
                        'en packaging semanas antes de vender nada.')
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, FIL_CAB, [
        ('A', 'Mes', 14), ('B', 'Campaña', 30),
        ('C', 'Personas de refuerzo', 12),
        ('D', 'Horas por persona', 12),
        ('E', 'Coste del refuerzo (EUR)', 13),
        ('F', 'Antelación de los moldes (semanas)', 13),
        ('G', 'Inversión en moldes de temporada (EUR)', 14),
        ('H', 'Antelación del packaging (semanas)', 13),
        ('I', 'Inversión en packaging de temporada (EUR)', 14),
        ('J', 'Tesorería inmovilizada (EUR)', 14),
        ('K', 'Días con el dinero parado', 13),
        ('L', 'Coste financiero del inmovilizado (EUR)', 14),
        ('M', 'Margen bruto de la facturación incremental (EUR)', 15),
        ('N', 'RESULTADO INCREMENTAL (EUR)', 15),
        ('O', 'Veredicto', 26), ('P', 'Nota', 66)], alto=76)
    for i, c in enumerate(CAMPANAS):
        fila = FIL_INI + i
        cal = FIL_INI + i
        moldes, packaging = INVERSION_TEMPORADA[c['mes']]
        motor.val(ws, 'A%d' % fila, c['nombre_mes'])
        motor.val(ws, 'B%d' % fila, c['campana'], wrap=True)
        C.entrada(ws, 'C%d' % fila, c['refuerzo_personas'], fmt=C.ENT,
                  etiqueta='Personas de refuerzo en %s' % c['nombre_mes'])
        C.entrada(ws, 'D%d' % fila, c['refuerzo_horas_persona'], fmt=C.ENT,
                  etiqueta='Horas por persona en %s' % c['nombre_mes'])
        motor.f(ws, 'E%d' % fila, '=IFERROR(C%d*D%d*%s,"")'
                % (fila, fila, A(P_CHORA)), fmt=C.EUR)
        C.entrada(ws, 'F%d' % fila, c['antelacion_moldes_semanas'], fmt=C.ENT,
                  etiqueta='Antelación de moldes en %s' % c['nombre_mes'])
        C.entrada(ws, 'G%d' % fila, moldes, fmt=C.EUR,
                  etiqueta='Inversión en moldes de %s' % c['nombre_mes'])
        C.entrada(ws, 'H%d' % fila, c['antelacion_packaging_semanas'],
                  fmt=C.ENT,
                  etiqueta='Antelación de packaging en %s' % c['nombre_mes'])
        C.entrada(ws, 'I%d' % fila, packaging, fmt=C.EUR,
                  etiqueta='Inversión en packaging de %s' % c['nombre_mes'])
        motor.f(ws, 'J%d' % fila, '=IFERROR(G%d+I%d,"")' % (fila, fila),
                fmt=C.EUR)
        motor.f(ws, 'K%d' % fila,
                '=IF(OR(NOT(ISNUMBER(F%d)),NOT(ISNUMBER(H%d))),"",'
                'MAX(F%d,H%d)*%s)' % (fila, fila, fila, fila, A(P_DSEM)),
                fmt=C.ENT)
        motor.f(ws, 'L%d' % fila, '=IFERROR(J%d*%s*K%d/%s,"")'
                % (fila, A(P_INT), fila, A(P_DANO)), fmt=C.EUR)
        motor.f(ws, 'M%d' % fila, '=IFERROR(%sO%d*%s,"")'
                % (QCAL, cal, A(P_MBANO)), fmt=C.EUR)
        motor.f(ws, 'N%d' % fila, '=IFERROR(M%d-E%d-L%d,"")'
                % (fila, fila, fila), fmt=C.EUR, bold=True)
        motor.f(ws, 'O%d' % fila,
                '=IF(NOT(ISNUMBER(N%d)),"",IF(N%d>=0,"La campaña deja dinero",'
                '"La campaña cuesta más de lo que deja"))' % (fila, fila))
        motor.val(ws, 'P%d' % fila,
                  'Las inversiones en moldes y en packaging son CIFRAS DE '
                  'CAMPAÑA y supuestos declarados, no un número de moldes por '
                  'un precio: un molde de policarbonato vale entre 24,20 y '
                  '42,83 EUR y elegir un punto de ese rango para multiplicarlo '
                  'es inventarse un presupuesto.' if c['mes'] == 12 else
                  'Cero personas de refuerzo y cero euros es un cero REAL: esa '
                  'campaña se cubre con la plantilla que ya tienes.'
                  if not c['refuerzo_personas'] else
                  'Con refuerzo contratado: recuerda que el coste de empresa '
                  'es un tercio más que el bruto de la nómina.', wrap=True)
        ws['P%d' % fila].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[fila].height = 46
    motor.val(ws, 'A%d' % FIL_TOT, 'TOTAL del año', bold=True)
    for col in ('E', 'G', 'I', 'J', 'L', 'M', 'N'):
        motor.f(ws, '%s%d' % (col, FIL_TOT),
                '=SUM(%s%d:%s%d)' % (col, FIL_INI, col, FIL_FIN), fmt=C.EUR,
                bold=True)
    motor.semaforo_isnumber(ws, 'N%d:N%d' % (FIL_INI, FIL_FIN),
                            '$N%d' % FIL_INI, '<', '0')

    fila = FIL_TOT + 2
    motor.val(ws, 'A%d' % fila,
              'El resultado incremental es lo que la campaña te deja POR ENCIMA '
              'de lo que habrías vendido igual: por eso se calcula sobre la '
              'facturación incremental y no sobre la total. Una campaña que '
              'sale negativa no es siempre una campaña que retirar -Navidad '
              'trae clientes que vuelven en enero-, pero sí es una campaña que '
              'hay que rehacer: menos referencias, menos moldes nuevos o más '
              'precio.', wrap=True)
    ws['A%d' % fila].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[fila].height = 58
    motor.val(ws, 'A%d' % (fila + 2), C.VERSION_LINE)
    ws['A%d' % (fila + 2)].font = Font(size=8, italic=True)
    C.setup(ws, landscape=True, titulos='%d:%d' % (FIL_CAB, FIL_CAB))
    return ws


# ==========================================================================
# Hoja «El Valle de Agosto» (D36)
# ==========================================================================
def hoja_valle(wb):
    ws = wb.create_sheet(H_VAL)
    C.cabecera_hoja(ws, 'El Valle de Agosto')
    motor.val(ws, 'A3', 'Un mes «Baja» de doce, y lo que para es el OBRADOR, no '
                        'la caja: literal del kit, «la tienda abre para el '
                        'turista aunque el obrador pare».')
    ws['A3'].font = Font(italic=True, size=9)
    for letra, ancho in (('A', 56), ('B', 18), ('C', 16), ('D', 20), ('E', 92)):
        ws.column_dimensions[letra].width = ancho

    C.encabezados(ws, 5, [
        ('A', 'Concepto', None), ('B', 'Valor', None), ('C', 'Unidad', None),
        ('D', 'De dónde sale', None), ('E', 'Nota', None)], alto=26)

    def linea(fila, etiqueta, unidad, fuente, nota, valor=None, formula=None,
              fmt=None, verde=False, bold=None):
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
        if formula is not None:
            cel = C.crema(motor.f(ws, 'B%d' % fila, formula, fmt=fmt,
                                  bold=True))
        elif verde:
            cel = C.entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
        else:
            cel = motor.val(ws, 'B%d' % fila, valor, fmt=fmt, bold=bold)
        motor.val(ws, 'C%d' % fila, unidad)
        motor.val(ws, 'D%d' % fila, fuente)
        ws['D%d' % fila].font = Font(size=8, color=C.GRIS)
        motor.val(ws, 'E%d' % fila, nota, wrap=True)
        ws['E%d' % fila].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[fila].height = 42
        return cel

    linea(V_MES, 'Mes del valle según el calendario del kit', 'mes',
          'BONUS-02!Calendario',
          'Es AGOSTO, y es uno de los doce. Junio y julio son «Media»: en '
          'junio empieza a cambiar el catálogo y en julio entra el turista.',
          valor=D.VALLE['nombre_mes'])
    linea(V_MESES_BAJA, 'Meses en temporada «Baja» de los doce', 'meses',
          'BONUS-02!Calendario',
          'Siete «Alta», cuatro «Media» y UNO «Baja». Hablar de un valle de '
          'tres meses contradice el calendario que la propia casa publica.',
          valor=1, fmt=C.ENT)
    linea(V_PARA_OBR, '¿Paras el obrador en agosto?', 'sí/no', 'decisión tuya',
          'En el ejemplo, sí: mantenimiento profundo, vacaciones escalonadas y '
          'cierre del pedido de coberturas de Navidad, que son los tres '
          'motivos que nombra el propio kit.', valor='Sí', verde=True)
    linea(V_PARA_ENV, '¿Paras los envíos?', 'sí/no', 'decisión tuya',
          'Es una decisión de CANAL ONLINE, no de mostrador: el chocolate no '
          'viaja en verano sin cadena de frío.', valor='Sí', verde=True)
    linea(V_MESES_ENV, 'Meses con los envíos parados', 'meses',
          'supuesto sobre dato de canal online',
          'De junio a septiembre. El mostrador sigue vivo los cuatro meses, y '
          'en julio y agosto con turista.', valor='de junio a septiembre')
    linea(V_VTA_AGO, 'Ventas de agosto sin IVA', 'EUR', 'calculado',
          'Sale del coeficiente de estacionalidad de agosto. NO es cero: la '
          'tienda abre.', formula='=%sE%d' % (QANO, FILA_VALLE), fmt=C.EUR)
    linea(V_VTA_MED, 'Ventas de un mes medio sin IVA', 'EUR', 'calculado',
          'Las ventas del año entre doce.',
          formula='=IFERROR(%s/12,"")' % A(P_VENTAS), fmt=C.EUR)
    linea(V_RATIO, 'Agosto frente a un mes medio', 'veces', 'calculado',
          'Cuánto factura agosto por cada euro de un mes normal.',
          formula='=IFERROR(B%d/B%d,"")' % (V_VTA_AGO, V_VTA_MED), fmt=C.DEC)
    linea(V_MB_ANO, 'Margen bruto con el mix de todo el año', 'sobre ventas',
          'Parámetros', 'El de la carta completa.',
          formula='=%s' % A(P_MBANO), fmt=C.PCT)
    linea(V_MB_VER, 'Margen bruto con el mix de julio y agosto',
          'sobre ventas', 'Parámetros',
          'Menos ganache fresca, más tableta y producto estable: literal del '
          'kit para junio.', formula='=%s' % A(P_MBVER), fmt=C.PCT)
    linea(V_CAIDA, 'Caída del margen al cambiar el mix', 'puntos',
          'calculado',
          'Sale en NEGATIVO si el mix de verano deja menos margen, que es lo '
          'que pasa en este ejemplo: la tableta lleva más chocolate por pieza '
          'y menos manos. Vender producto estable en agosto es una decisión de '
          'CADUCIDAD, no de margen, y conviene saberlo antes de tomarla.',
          formula='=IFERROR(B%d-B%d,"")' % (V_MB_VER, V_MB_ANO), fmt=C.PCT)
    linea(V_MBE_AGO, 'Margen bruto de agosto en euros', 'EUR', 'calculado',
          'Ventas de agosto por el margen del mix de verano.',
          formula='=IFERROR(B%d*B%d,"")' % (V_VTA_AGO, V_MB_VER), fmt=C.EUR)
    linea(V_MBE_MED, 'Margen bruto de un mes medio en euros', 'EUR',
          'calculado', 'Ventas de un mes medio por el margen del año.',
          formula='=IFERROR(B%d*B%d,"")' % (V_VTA_MED, V_MB_ANO), fmt=C.EUR)
    linea(V_FIJOS, 'Gastos fijos del mes', 'EUR', 'Parámetros',
          'Siguen corriendo enteros: el alquiler, el préstamo, los seguros y '
          'los tres equipos de frío, que en agosto trabajan más que nunca.',
          formula='=%s' % A(P_FIJOS), fmt=C.EUR)
    linea(V_RES_AGO, 'RESULTADO DE AGOSTO', 'EUR', 'calculado',
          'Margen bruto de agosto menos los gastos fijos del mes. Es la cifra '
          'que hay que mirar en mayo, no en agosto.',
          formula='=IFERROR(B%d-B%d,"")' % (V_MBE_AGO, V_FIJOS), fmt=C.EUR)
    linea(V_RES_MED, 'Resultado de un mes medio', 'EUR', 'calculado',
          'Para comparar.',
          formula='=IFERROR(B%d-B%d,"")' % (V_MBE_MED, V_FIJOS), fmt=C.EUR)
    linea(V_DIF, 'Lo que te cuesta agosto frente a un mes medio', 'EUR',
          'calculado',
          'Ésta es la cifra que hay que tener provisionada, y es la razón por '
          'la que el ejemplo abre el 1 de junio: así el valle cae dentro del '
          'arranque, cuando todavía sale barato.',
          formula='=IFERROR(B%d-B%d,"")' % (V_RES_AGO, V_RES_MED), fmt=C.EUR)
    linea(V_VER, 'Veredicto de agosto', '', 'calculado',
          'Un agosto en negativo NO es un motivo para cerrar: es un motivo '
          'para provisionarlo. Cerrar la tienda en el mes en el que el turista '
          'pasa por delante sería cambiar una pérdida pequeña por una grande.',
          formula='=IF(NOT(ISNUMBER(B%d)),"",IF(B%d>=0,"Agosto se paga solo",'
                  '"Agosto da pérdida: provisiónala, no cierres la tienda"))'
                  % (V_RES_AGO, V_RES_AGO))

    # --- cuadre interno ----------------------------------------------------
    # El rótulo de la sección NO empieza por «CUADRE» a propósito: la única
    # fila que lo hace en este libro además del cruce 6 <- 1 es la del cuadre
    # interno, y va marcada como tal para que un gate que cuente los OCHO
    # cruces del pack no confunda una comprobación interna con un cruce.
    C.seccion(ws, 'A%d' % VC_SEC,
              'Comprobación interna: las unidades de campaña frente a las del '
              'año')
    linea(VC_CAMP, 'Bombones de obrador extra que suman las doce campañas',
          'piezas/año', 'Capacidad vs Demanda',
          'Son las bombones de obrador que las campañas añaden a lo que se '
          'produce un día normal.',
          formula='=%sN%d' % (QCAP, CAP_TOT), fmt=C.ENT)
    linea(VC_ANO, 'Bombones de obrador al año en velocidad de crucero',
          'piezas/año', 'Parámetros',
          'Bombones de obrador al día por días de apertura.',
          formula='=IFERROR(%s*%s,"")' % (A(P_PZOBR), A(P_DIAS)), fmt=C.ENT)
    linea(VC_PCT, 'Las campañas sobre la producción del año', 'sobre el año',
          'calculado', 'Cuánto añaden las campañas a un año de producción.',
          formula='=IFERROR(B%d/B%d,"")' % (VC_CAMP, VC_ANO), fmt=C.PCT)
    linea(VC_VER,
          'CUADRE INTERNO (no es un cruce entre libros): ¿caben las campañas '
          'dentro del año?', '', 'calculado',
          'Si las campañas añaden más producción que la de un año entero, o el '
          'calendario está inflado o las unidades de pico están mal medidas. '
          'No es un cruce con otro fichero: es una comprobación de este libro '
          'consigo mismo.',
          formula='=IF(NOT(ISNUMBER(B%d)),"",IF(B%d<=1,"CUADRA: las campañas '
                  'caben dentro del año","REVISA: las campañas suman más '
                  'producción que todo un año"))' % (VC_PCT, VC_PCT))
    motor.semaforo_isnumber(ws, 'B%d' % VC_PCT, '$B$%d' % VC_PCT, '>', '1')

    motor.val(ws, 'A%d' % VAL_NOTA,
              'Lo que el kit dice, literal, de los tres meses de verano: junio, '
              '«adaptar catálogo (menos ganache fresca, más tableta y producto '
              'estable)»; julio, «temporada turística: packs souvenir y '
              'colaboraciones locales»; agosto, «la tienda abre para el turista '
              'aunque el obrador pare». Tres meses, tres cosas distintas, y '
              'sólo uno de ellos es «Baja».', wrap=True)
    ws['A%d' % VAL_NOTA].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[VAL_NOTA].height = 62
    motor.val(ws, 'A%d' % (VAL_NOTA + 2),
              'Y la línea que sí funciona en agosto son los TALLERES: no '
              'dependen del precio del cacao, no necesitan obrador y ocupan la '
              'sala en el mes en el que la sala está vacía. Su economía -euros '
              'por hora de sala dando taller frente a euros por hora de la '
              'misma sala vendiendo- la calcula el plan financiero del pack, '
              'no este libro.', wrap=True)
    ws['A%d' % (VAL_NOTA + 2)].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[VAL_NOTA + 2].height = 58

    refs, fin = C.bloque_listas(ws, VAL_LISTAS, (('Sí o no', SI_NO),))
    C.dv_rango(ws, ['B%d' % V_PARA_OBR, 'B%d' % V_PARA_ENV], refs['Sí o no'],
               'Responde sí o no',
               'Escribe «Sí» o «No», que es lo que entiende la hoja.')
    motor.val(ws, 'A%d' % (fin + 1), C.VERSION_LINE)
    ws['A%d' % (fin + 1)].font = Font(size=8, italic=True)
    C.setup(ws, landscape=True)
    return ws


# ==========================================================================
# Mapa de celdas citables
# ==========================================================================
def mapa_celdas():
    m = [
        ('Ventas anuales sin IVA en crucero', H_PAR, P_VENTAS, 'entrada'),
        ('Ticket medio sin IVA', H_PAR, P_TICKET, 'salida'),
        ('Bombones de obrador al dia en crucero', H_PAR, P_PZOBR, 'entrada'),
        ('Dias de apertura al ano', H_PAR, P_DIAS, 'entrada'),
        ('Margen bruto medio con el mix del ano', H_PAR, P_MBANO, 'entrada'),
        ('Margen bruto medio con el mix de julio y agosto', H_PAR, P_MBVER,
         'entrada'),
        ('Coste por hora pagada del refuerzo', H_PAR, P_CHORA, 'salida'),
        ('Gastos fijos mensuales', H_PAR, P_FIJOS, 'entrada'),
        ('Tipo de interes anual del circulante', H_PAR, P_INT, 'parametro'),
        ('Dias de campana al ano', H_CAL, 'J%d' % FIL_TOT, 'salida'),
        ('Unidades incrementales de las doce campanas', H_CAL,
         'L%d' % FIL_TOT, 'salida'),
        ('Facturacion de las doce campanas con IVA', H_CAL, 'M%d' % FIL_TOT,
         'salida'),
        ('Facturacion de las doce campanas sin IVA', H_CAL, 'N%d' % FIL_TOT,
         'salida'),
        ('Facturacion incremental de las doce campanas sin IVA', H_CAL,
         'O%d' % FIL_TOT, 'salida'),
        ('Suma de los coeficientes de estacionalidad', H_ANO,
         'C%d' % FIL_TOT, 'salida'),
        ('Ventas repartidas en los doce meses', H_ANO, 'E%d' % FIL_TOT,
         'salida'),
        ('Ventas de diciembre sin IVA', H_ANO, 'E%d' % FILA_MES[12], 'salida'),
        ('Ventas de agosto sin IVA', H_ANO, 'E%d' % FILA_VALLE, 'salida'),
        ('Peso de diciembre sobre el ano', H_ANO, 'F%d' % FILA_MES[12],
         'salida'),
        ('Peso de agosto sobre el ano', H_ANO, 'F%d' % FILA_VALLE, 'salida'),
        ('Veces un dia medio que factura un dia de diciembre', H_ANO,
         'H%d' % FILA_MES[12], 'salida'),
        ('Peso de las doce campanas sobre el ano', H_ANO, 'D%d' % PIC_TOT,
         'salida'),
        ('Peso incremental de las doce campanas sobre el ano', H_ANO,
         'F%d' % PIC_TOT, 'salida'),
        ('Capacidad diaria del obrador traida del libro 1', H_CAP, CAP_TRAE,
         'entrada'),
        ('Desviacion del cuadre de capacidad', H_CAP, CAP_DESV, 'salida'),
        ('Veredicto del cuadre de capacidad', H_CAP, CAP_CUAD, 'salida'),
        ('Campanas que no aguanta el obrador', H_CAP, 'B%d' % CAP_NOAG,
         'salida'),
        ('Campanas con deficit despues de adelantar', H_CAP,
         'B%d' % (CAP_NOAG + 1), 'salida'),
        ('Bombones de obrador extra de las doce campanas', H_CAP,
         'N%d' % CAP_TOT, 'salida'),
        ('Coste del refuerzo de todo el ano', H_REF, 'E%d' % FIL_TOT,
         'salida'),
        ('Inversion en moldes de temporada del ano', H_REF, 'G%d' % FIL_TOT,
         'salida'),
        ('Inversion en packaging de temporada del ano', H_REF,
         'I%d' % FIL_TOT, 'salida'),
        ('Tesoreria inmovilizada en campanas', H_REF, 'J%d' % FIL_TOT,
         'salida'),
        ('Coste financiero del inmovilizado de campana', H_REF,
         'L%d' % FIL_TOT, 'salida'),
        ('Resultado incremental de las doce campanas', H_REF, 'N%d' % FIL_TOT,
         'salida'),
        ('Ventas de agosto frente a un mes medio', H_VAL, 'B%d' % V_RATIO,
         'salida'),
        ('Caida del margen al cambiar el mix en verano', H_VAL,
         'B%d' % V_CAIDA, 'salida'),
        ('Resultado de agosto', H_VAL, 'B%d' % V_RES_AGO, 'salida'),
        ('Resultado de un mes medio', H_VAL, 'B%d' % V_RES_MED, 'salida'),
        ('Lo que cuesta agosto frente a un mes medio', H_VAL, 'B%d' % V_DIF,
         'salida'),
        ('Veredicto de agosto', H_VAL, 'B%d' % V_VER, 'salida'),
        ('Bombones de obrador al ano en crucero', H_VAL, 'B%d' % VC_ANO,
         'salida'),
        ('Las campanas sobre la produccion del ano', H_VAL, 'B%d' % VC_PCT,
         'salida'),
        ('Cuadre interno de unidades de campana', H_VAL, 'B%d' % VC_VER,
         'salida'),
    ]
    for i, c in enumerate(CAMPANAS):
        cal = FIL_INI + i
        cap = CAP_INI + i
        ref = FIL_INI + i
        nom = c['campana']
        m += [
            ('Facturacion sin IVA de la campana de %s' % nom, H_CAL,
             'N%d' % cal, 'salida'),
            ('Demanda de bombones de obrador al dia en %s' % nom, H_CAP,
             'F%d' % cap, 'salida'),
            ('Aguanta el obrador la campana de %s' % nom, H_CAP, 'I%d' % cap,
             'salida'),
            ('Resultado incremental de la campana de %s' % nom, H_REF,
             'N%d' % ref, 'salida'),
        ]
    return m


NOTAS_MAPA = (
    'Libro 6 del pack. Frontera K2: el BONUS-02-calendario-anual-tareas.xlsx '
    'del Kit de Tareas Chocolatería (12 €) pone las fechas y el qué; este libro '
    'pone los euros y el «si aguantas». Las doce filas del calendario bajan '
    'como copia declarada y sus acciones y productos se citan literales. D35: '
    'siete meses «Alta», cuatro «Media» y UNO «Baja», con las COMUNIONES '
    '(abril-junio) como campaña propia. D36: el valle es AGOSTO -un mes de '
    'doce- y lo que para es el OBRADOR, no la caja: la tienda abre para el '
    'turista y los envíos se paran de junio a septiembre, que es canal online. '
    'Cruce 6 <- 1 (D32): la capacidad diaria es una celda VERDE que trae la '
    'cifra de capacidad-obrador-y-clima.xlsx!Cuello de Botella, con valor por '
    'defecto declarado y fila de CUADRE; no hay ni una fórmula entre ficheros. '
    'Todo se cuenta en BOMBONES DE OBRADOR: una caja de 35 bombones es una venta '
    'y treinta y seis bombones de obrador.'
)


# ==========================================================================
# Demostraciones con pycel
# ==========================================================================
def demo(ruta):
    from pycel import ExcelCompiler
    ok, fallos = [], []

    def prueba(nombre, cond, detalle=''):
        (ok if cond else fallos).append(nombre + (' - ' + detalle if detalle
                                                  else ''))

    exc = ExcelCompiler(ruta)

    def v(hoja, coord):
        return exc.evaluate("'%s'!%s" % (hoja, coord))

    # 1. Los doce coeficientes reparten el año sin perder ni un euro.
    ventas = v(H_PAR, P_VENTAS)
    suma = v(H_ANO, 'E%d' % FIL_TOT)
    prueba('los doce meses suman las ventas del año',
           abs(suma - ventas) < 0.5, '%.2f frente a %.2f' % (suma, ventas))

    # 2. Agosto es el mes más bajo, y NO es cero: la tienda abre.
    agosto = v(H_ANO, 'E%d' % FILA_VALLE)
    meses = [v(H_ANO, 'E%d' % (FIL_INI + i)) for i in range(NM)]
    prueba('agosto es el mes más bajo de los doce y no vale cero',
           abs(agosto - min(meses)) < 0.01 and agosto > 0,
           '%.2f EUR frente a %.2f del mes más alto' % (agosto, max(meses)))

    # 3. El pico se mide en BOMBONES DE OBRADOR: una caja pesa lo que lleva
    #    dentro. Navidad, con cajas de 35, no cabe en el obrador del ejemplo.
    fila_dic = CAP_INI + [c['mes'] for c in CAMPANAS].index(12)
    demanda = v(H_CAP, 'F%d' % fila_dic)
    capacidad = v(H_CAP, 'G%d' % fila_dic)
    aguanta = v(H_CAP, 'I%d' % fila_dic)
    prueba('el pico de Navidad se mide en bombones de obrador y no cabe en la '
           'jornada normal', demanda > capacidad and aguanta == 'No',
           '%d piezas/día de demanda frente a %d de capacidad'
           % (demanda, capacidad))

    # 4. La fila de CUADRE avisa si la capacidad se aleja de la del libro 1.
    exc2 = ExcelCompiler(ruta)
    cuadra = exc2.evaluate("'%s'!%s" % (H_CAP, CAP_CUAD))
    exc2.set_value("'%s'!%s" % (H_CAP, CAP_TRAE), 900)
    revisa = exc2.evaluate("'%s'!%s" % (H_CAP, CAP_CUAD))
    prueba('la fila de CUADRE avisa si la capacidad se separa de la del libro 1',
           cuadra == 'CUADRA' and revisa.startswith('REVISA'),
           'antes %r, después %r' % (cuadra, revisa))

    # 5. Subir la capacidad cambia el veredicto de Navidad.
    exc3 = ExcelCompiler(ruta)
    antes = exc3.evaluate("'%s'!I%d" % (H_CAP, fila_dic))
    exc3.set_value("'%s'!%s" % (H_CAP, CAP_TRAE), 5000)
    despues = exc3.evaluate("'%s'!I%d" % (H_CAP, fila_dic))
    prueba('el veredicto de Navidad cambia al subir la capacidad del obrador',
           antes == 'No' and despues == 'Sí',
           'antes %r, después %r' % (antes, despues))

    # 6. Agosto: la facturación es MENOR pero no nula, y los fijos corren.
    res_ago = v(H_VAL, 'B%d' % V_RES_AGO)
    res_med = v(H_VAL, 'B%d' % V_RES_MED)
    fijos = v(H_VAL, 'B%d' % V_FIJOS)
    prueba('agosto da menos resultado que un mes medio y los fijos siguen '
           'corriendo enteros', res_ago < res_med and fijos > 0,
           'agosto %.2f EUR frente a %.2f EUR de un mes medio'
           % (res_ago, res_med))

    # 7. El CUADRE INTERNO dice que las campañas caben dentro del año.
    ver = v(H_VAL, 'B%d' % VC_VER)
    prueba('el cuadre interno confirma que las campañas caben dentro del año',
           ver.startswith('CUADRA'), 'devuelve %r' % (ver,))

    return ok, fallos


# ==========================================================================
def main():
    D.gate_legal()
    # D35: el generador ABORTA si falta un mes del calendario del kit.
    meses = sorted(c['mes'] for c in CAMPANAS)
    if meses != list(range(1, 13)):
        raise SystemExit('El calendario del kit tiene que traer los DOCE meses '
                         '(D35) y trae: %r' % meses)
    temporadas = {}
    for c in CAMPANAS:
        temporadas[c['temporada']] = temporadas.get(c['temporada'], 0) + 1
    if temporadas != {'Alta': 7, 'Media': 4, 'Baja': 1}:
        raise SystemExit('El calendario del kit declara 7 «Alta», 4 «Media» y 1 '
                         '«Baja» (D35/D36) y aquí salen: %r' % temporadas)
    if D.VALLE['mes'] != 8 or D.VALLE['para_la_tienda']:
        raise SystemExit('D36: el valle es AGOSTO y lo que para es el OBRADOR, '
                         'no la tienda.')

    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_parametros(wb)
    hoja_calendario(wb)
    hoja_anio(wb)
    hoja_capacidad(wb)
    hoja_refuerzo(wb)
    hoja_valle(wb)

    res = C.cerrar(wb, NOMBRE, TITULO, mapa_celdas(), NOTAS_MAPA)

    print('escrito: %s' % res['ruta'])
    print('hojas: %d · fórmulas: %d · celdas verdes: %d · verdes vacías: %d'
          % (res['hojas'], res['formulas'], res['verdes'],
             len(res['verdes_vacias'])))
    print('fórmulas que devuelven «sin dato» a propósito: %d' % res['sin_dato'])
    print('notas legales: %d · etiquetas en el mapa: %d'
          % (res['notas_legales'], res['mapa']))
    print('celdas «trae aquí la cifra de»: %d · filas de CUADRE: %d'
          % (res['trae'], res['cuadre']))
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
