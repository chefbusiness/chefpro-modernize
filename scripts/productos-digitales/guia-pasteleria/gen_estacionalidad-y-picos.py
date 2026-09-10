#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_estacionalidad-y-picos.py — libro 3 de «Cómo Montar una Pastelería»
(SPEC §2.2 fila 3; reglas R5 y D21).

Hojas: Instrucciones · Parámetros · Calendario de 6 Picos · Peso sobre el Año ·
Capacidad vs Demanda del Pico · Refuerzo y Tesorería.

QUÉ DECIDE ESTE LIBRO
---------------------
Si aguantas Reyes con el equipo que estás comprando, y cuánto dinero inmoviliza
cada campaña. No es un calendario: es la ECONOMÍA del pico.

FRONTERA R5 (SPEC §2.3), y va escrita en «Instrucciones»
--------------------------------------------------------
El `BONUS-02-calendario-anual-tareas.xlsx` del Kit de Tareas Pastelería (12 €)
pone las FECHAS y el qué hay que hacer. Este libro pone los EUROS y el «si
aguantas». No se repite el calendario: se le pone precio.

DECISIONES TÉCNICAS
-------------------
* **La capacidad del obrador es una celda VERDE con valor por defecto propio**
  (D21): el dato bueno sale de la hoja «Cuello de Botella» del libro 1
  (`capacidad-obrador-y-local.xlsx`), pero **no hay ni una fórmula entre
  libros** — se copia a mano y la nota lo dice. Igual con el resto de entradas
  que en el diseño original remitían al kit: ninguna queda vacía.
* El déficit del pico se resuelve por TRES palancas y en este orden, que es el
  del obrador de verdad: horas de máquina en campaña, producción adelantada y
  congelada (por eso el abatidor es la compra que más se discute) y refuerzo de
  personal. La hoja las separa para que se vea cuál falta.
* Cero constantes dentro de las fórmulas: piezas/hora, horas de turno, tipo de
  interés, pagas del convenio y SS viven en «Parámetros», en celda verde.
* `IFERROR(...,"")` en toda división; «sin dato» = `""`, nunca `0`; semáforos
  con `ISNUMBER`; DV contra RANGO. Prohibidas INDIRECT, COUNTA, PMT, OFFSET,
  XLOOKUP, LET, LAMBDA, RANK, NETWORKDAYS e IRR: cero usos.
* Nada de funciones de fecha para la ruta de compra: la antelación se cuenta en
  SEMANAS y en días, con aritmética.

Salida fija: build/estacionalidad-y-picos.xlsx + build/mapa-estacionalidad-y-picos.json
Uso: /usr/local/bin/python3 gen_estacionalidad-y-picos.py
Via: Claude Code
"""
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import _comun_libros_3_4 as C                                  # noqa: E402
import datos_ejemplo as D                                      # noqa: E402
import motor                                                   # noqa: E402

NOMBRE = 'estacionalidad-y-picos'
TITULO = 'Estacionalidad y Picos de Campaña'

H_INS = 'Instrucciones'
H_PAR = 'Parámetros'
H_CAL = 'Calendario de 6 Picos'
H_ANO = 'Peso sobre el Año'
H_CAP = 'Capacidad vs Demanda del Pico'
H_REF = 'Refuerzo y Tesorería'

QPAR = "'" + H_PAR + "'!"
QCAL = "'" + H_CAL + "'!"
QCAP = "'" + H_CAP + "'!"

NP = len(D.PICOS)                       # 6
CAL_INI = 6
CAL_FIN = CAL_INI + NP - 1              # 11
CAL_TOT = CAL_FIN + 2                   # 13

MES_INI = 6
MES_FIN = MES_INI + 11                  # 17
MES_TOT = MES_FIN + 1                   # 18

PIC_INI = 24
PIC_FIN = PIC_INI + NP - 1
PIC_TOT = PIC_FIN + 1

CAP_INI = 6
CAP_FIN = CAP_INI + NP - 1
CAP_TOT = CAP_FIN + 2

REF_INI = 6
REF_FIN = REF_INI + NP - 1
REF_TOT = REF_FIN + 2

# --- Parámetros: coordenadas -----------------------------------------------
P_VENTAS = 'B6'
P_PIEZAS = 'B7'
P_DIAS = 'B8'
P_CAPDIA = 'B9'
P_HTURNO = 'B10'
P_PZH = 'B11'
P_EXCED = 'B12'
P_HMAX = 'B13'
P_HPERS = 'B14'
P_BRUTO = 'B17'
P_PAGAS = 'B18'
P_SS = 'B19'
P_HANIO = 'B20'
P_CHORA = 'B21'
P_INT = 'B24'
P_IVAP = 'B25'
P_IVAPAN = 'B26'
P_UMBRAL = 'B27'

A = lambda coord: QPAR + '$' + coord[0] + '$' + coord[1:]      # noqa: E731


# --------------------------------------------------------------------------
# Datos derivados de `datos_ejemplo`
# --------------------------------------------------------------------------
def ref_de(nombre):
    for r in D.CARTA:
        if r['nombre'] == nombre:
            return r
    raise SystemExit('El producto estrella %r no está en la CARTA' % nombre)


ESTRELLA = [ref_de(p['producto_estrella']) for p in D.PICOS]

#: Horas de obrador al día EN CAMPAÑA. Supuesto por pico: Reyes y Todos los
#: Santos se hacen a dos turnos; San Valentín y el Día del Padre y de la Madre
#: son campañas de ticket, no de volumen, y no mueven el horario.
HORAS_CAMPANA = {'Reyes': 20.0, 'San Valentín': 10.0,
                 'Día del Padre y de la Madre': 10.0, 'Semana Santa': 14.0,
                 'Comuniones': 10.0, 'Todos los Santos': 16.0}

#: Días en los que puedes ADELANTAR producción y congelarla antes de que
#: empiece la campaña. Supuesto. Comuniones va a 0 a propósito: es una meseta
#: de dos meses y todo se entrega fresco por encargo.
DIAS_ADELANTO = {'Reyes': 15, 'San Valentín': 5,
                 'Día del Padre y de la Madre': 5, 'Semana Santa': 10,
                 'Comuniones': 0, 'Todos los Santos': 10}

#: Capacidad del obrador en piezas/día con la jornada normal. Valor por defecto
#: COPIADO de la hoja «Cuello de Botella» del libro 1
#: (`capacidad-obrador-y-local.xlsx`), donde el equipo que limita a La Clara es
#: el abatidor de 4 bandejas: 480 piezas/día contra las 476 que pide la
#: velocidad de crucero. Cuatro piezas de holgura, y por eso ninguna campaña
#: entra sin adelantar producción o reforzar. Se copia a mano: no hay ni una
#: fórmula entre libros (D21).
CAPACIDAD_DIA_DEFECTO = 480.0
HORAS_MAX_DIA = 24.0
UMBRAL_PICO_ANIO = 0.05


# --------------------------------------------------------------------------
# Hoja «Instrucciones»
# --------------------------------------------------------------------------
PASOS = [
    '1. Hoja «Parámetros»: lo primero es la capacidad de tu obrador en piezas '
    'por hora. Ese número sale de la hoja «Cuello de Botella» del libro '
    '«capacidad-obrador-y-local.xlsx» de este mismo pack: ábrelo, mira qué '
    'equipo te limita y copia aquí sus piezas por hora. Viene con un valor por '
    'defecto para que el libro funcione desde el primer minuto, pero es un '
    'SUPUESTO, no tu obrador.',
    '2. Hoja «Calendario de 6 Picos»: seis campañas con su producto estrella, '
    'sus días, su precio y las unidades que esperas vender al día dentro y '
    'fuera de campaña. Es la única hoja donde tecleas expectativas de venta.',
    '3. Hoja «Peso sobre el Año»: reparte tus ventas anuales entre los doce '
    'meses y verás qué porcentaje del año se juega en cada campaña. Es el '
    'número que decide si merece la pena montar la campaña o no.',
    '4. Hoja «Capacidad vs Demanda del Pico»: aquí está la pregunta del libro. '
    'La demanda del pico se calcula multiplicando tus piezas de un día normal '
    'por el factor de la campaña; la capacidad, con las horas que puedas tener '
    'el obrador en marcha. Si sale déficit, tienes tres palancas y en este '
    'orden: más horas de máquina, producción adelantada y congelada, y '
    'refuerzo de personal.',
    '5. Hoja «Refuerzo y Tesorería»: cuánto cuesta el refuerzo con el coste de '
    'empresa de verdad (bruto de convenio más Seguridad Social) y, sobre todo, '
    'cuánto dinero deja inmovilizado la compra de materia prima de la campaña '
    'y durante cuántos días. Ese dinero sale de tu caja semanas antes de que '
    'entre el primer euro de la campaña.',
    '6. Repite el ciclo cada año en enero, con las cifras reales de la campaña '
    'que acabas de cerrar: el libro sólo vale si le metes lo que pasó de '
    'verdad, no lo que esperabas que pasara.',
]

NOTAS_LIBRO = [
    'QUÉ HACE ESTE LIBRO Y QUÉ HACE EL KIT DE TAREAS PASTELERÍA. El '
    '«BONUS-02-calendario-anual-tareas.xlsx» del Kit de Tareas Pastelería '
    'pone las FECHAS y el qué hay que hacer en cada campaña; el '
    '«06-eventos-festivos.xlsx» lleva el detalle de cada evento. Este libro no '
    'repite ese calendario: le pone EUROS y responde a «si aguanto». Son dos '
    'piezas distintas del mismo problema, y se usan juntas.',
    'Aquí no hay ni una fórmula que apunte a otro fichero. Cuando un dato vive '
    'en otro libro del pack (la capacidad del obrador, por ejemplo) se COPIA a '
    'mano y la nota lo dice. Un enlace entre ficheros se rompe en cuanto '
    'alguien mueve una carpeta, y entonces el libro miente sin avisar.',
    'El factor de campaña multiplica las piezas del OBRADOR ENTERO, no las del '
    'producto estrella. En un obrador medido, la pastelería individual pasó de '
    '50-60 piezas al día a 500-600 en campaña con el mismo equipo. El 6,0 de '
    'Reyes que trae el ejemplo es el único que llega a esa zona; el resto se '
    'quedan entre 1,6 y 2,6 porque son campañas de dos, tres o cuatro días.',
    'El roscón relleno de nata arrastra los 4' + C.N + '°C de la fila 9 del '
    'art. 4.1 y las 24' + C.N + 'horas del art. 9.3 del RD 1021/2022 justo el '
    'día de más producción. Eso limita la campaña tanto como el horno: lo que '
    'no se puede adelantar y congelar hay que hacerlo el mismo día. La hoja de '
    'decisión de huevo y temperatura del libro '
    '«carta-de-apertura-y-escandallo.xlsx» te dice qué referencia entra en ese '
    'saco y cuál no.',
    'La producción adelantada tiene un techo físico que no está en esta hoja: '
    'los metros cúbicos de tu congelador y la capacidad de tu abatidor. Antes '
    'de dar por buena una cifra de piezas adelantadas, comprueba que te caben. '
    'Un armario de congelación conserva, pero NO congela: no sustituye al '
    'abatidor (art. 5 del RD 1021/2022).',
    'La tesorería de la campaña es el número que más sorprende. Pides la '
    'materia prima semanas antes, la pagas al contado o a 30 días, y cobras '
    'cuando vendes. Entre una cosa y otra hay un dinero parado que no está en '
    'ninguna cuenta de resultados y que sí está en tu banco.',
]

CADENCIA = ('Cada cuánto se usa este libro: los «Parámetros» y el «Calendario '
            'de 6 Picos», UNA VEZ AL AÑO, en enero, cuando cierras la campaña '
            'de Reyes y tienes los datos frescos. «Capacidad vs Demanda» y '
            '«Refuerzo y Tesorería», UNA VEZ POR CAMPAÑA, con la antelación de '
            'compra que diga la propia hoja: para Reyes, seis semanas antes, '
            'es decir a finales de noviembre.')


def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS, 0)
    ws.column_dimensions['A'].width = 90.0   # hallazgo A11b (2026-09-10): tope 90
    C.cabecera_hoja(ws, TITULO)
    motor.val(ws, 'A3', 'Para qué sirve: saber si aguantas Reyes antes de que '
                        'llegue, y cuánto dinero inmoviliza cada campaña.')
    ws['A3'].font = Font(italic=True, size=9)

    C.seccion(ws, 'A5', 'Instrucciones de uso')
    fila = 6
    for paso in PASOS:
        motor.val(ws, 'A%d' % fila, paso, wrap=True)
        ws.row_dimensions[fila].height = 58
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, C.LEYENDA_VERDE, verde_=True)
    C.VERDES.append((H_INS, 'A%d' % fila, 'Leyenda de celdas verdes',
                     C.LEYENDA_VERDE))
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Lo que conviene saber antes de empezar')
    fila += 1
    for nota in NOTAS_LIBRO:
        motor.val(ws, 'A%d' % fila, nota, wrap=True)
        ws.row_dimensions[fila].height = 62
        fila += 1
    fila += 1

    motor.val(ws, 'A%d' % fila, CADENCIA, wrap=True)
    ws.row_dimensions[fila].height = 46
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


# --------------------------------------------------------------------------
# Hoja «Parámetros»
# --------------------------------------------------------------------------
def par(ws, fila, etiqueta, valor, fmt, unidad, fuente, nota, verde=True,
        formula=None, bold=None):
    motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
    if formula is not None:
        cel = motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=True)
        C.crema(cel)
    else:
        cel = C.entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta=etiqueta,
                        bold=bold) if verde else motor.val(
                            ws, 'B%d' % fila, valor, fmt=fmt)
    motor.val(ws, 'C%d' % fila, unidad)
    motor.val(ws, 'D%d' % fila, fuente)
    ws['D%d' % fila].font = Font(size=8, color=C.GRIS)
    motor.val(ws, 'E%d' % fila, nota, wrap=True)
    ws['E%d' % fila].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[fila].height = 40
    return cel


def hoja_parametros(wb):
    ws = wb.create_sheet(H_PAR)
    C.cabecera_hoja(ws, 'Parámetros')
    for letra, ancho in (('A', 50), ('B', 15), ('C', 13), ('D', 20), ('E', 82)):
        ws.column_dimensions[letra].width = ancho
    C.encabezados(ws, 5, [('A', 'Parámetro', None), ('B', 'Valor', None),
                          ('C', 'Unidad', None), ('D', 'De dónde sale', None),
                          ('E', 'Nota', None)], alto=24)

    par(ws, 6, 'Ventas anuales sin IVA en velocidad de crucero',
        round(D.ventas_anuales_sin_iva(), 2), C.EUR, '€/año', 'supuesto',
        'Sale de la carta y del tráfico supuesto de La Clara: clientes al día '
        'por piezas por cliente por PVP medio ponderado. No es un dato del '
        'sector. Sustitúyelo por el de tu plan financiero.')
    par(ws, 7, 'Piezas al día en velocidad de crucero',
        round(D.piezas_dia_crucero()), C.ENT, 'piezas/día', 'supuesto',
        'Clientes al día por piezas por cliente. Es la base sobre la que el '
        'factor de cada campaña multiplica.')
    par(ws, 8, 'Días de apertura al año', D.NEGOCIO['dias_apertura_anio'],
        C.ENT, 'días', 'supuesto',
        D.NEGOCIO['nota_dias_apertura'])
    par(ws, 9, 'Capacidad del obrador en jornada normal',
        CAPACIDAD_DIA_DEFECTO, C.ENT, 'piezas/día', 'libro 1',
        'COPIA a mano el resultado de la hoja «Cuello de Botella» del libro '
        '«capacidad-obrador-y-local.xlsx» de este pack: la casilla «Piezas al '
        'día que permite el conjunto». En el ejemplo son 480 y el equipo que '
        'limita es el abatidor de 4 bandejas, contra 476 piezas de velocidad '
        'de crucero: cuatro piezas de holgura. No hay fórmula entre libros: '
        'si cambias de equipo, vuelve a copiarlo.')
    par(ws, 10, 'Horas de obrador al día en jornada normal',
        D.NEGOCIO['horas_turno'], C.DEC1, 'horas', 'supuesto',
        'Horas de reloj que el obrador está en marcha un día cualquiera, no '
        'horas de apertura de la tienda.')
    par(ws, 11, 'Piezas por hora de reloj del equipo que limita', None, C.DEC1,
        'piezas/hora', 'calculado',
        'Capacidad de la jornada normal dividida por sus horas. Va por hora de '
        'RELOJ, con las paradas ya dentro: el libro 1 ya descontó la parte de '
        'la jornada que no se pasa a pie de mesa.',
        formula='=IFERROR(%s/%s,"")' % (A(P_CAPDIA), A(P_HTURNO)))
    par(ws, 12, 'Excedente diario sobre la velocidad de crucero', None, C.ENT,
        'piezas/día', 'calculado',
        'Lo que te sobra un día normal. Es la munición para adelantar '
        'producción y congelarla antes de la campaña; si sale negativo, ya vas '
        'justo en crucero y el pico no lo arreglas adelantando.',
        formula='=IFERROR(%s-%s,"")' % (A(P_CAPDIA), A(P_PIEZAS)))
    par(ws, 13, 'Horas máximas de obrador al día que admites', HORAS_MAX_DIA,
        C.DEC1, 'horas', 'supuesto',
        'Techo que te pones tú. Por encima de este número la hoja se pone en '
        'rojo: no es un límite legal, es el aviso de que ese día no existe.')
    par(ws, 14, 'Horas por persona y día del refuerzo', 8.0, C.DEC1, 'horas',
        'supuesto',
        'Jornada del personal de refuerzo durante la campaña. Con ella se '
        'calcula cuántas personas hacen falta para cubrir las horas de máquina '
        'que faltan.')

    C.seccion(ws, 'A16', 'Coste del refuerzo (convenio de pastelería)')
    br = par(ws, 17, 'Bruto mensual del grupo de convenio del refuerzo',
             D.CONVENIO[4][2], C.EUR, '€/mes', D.FUENTE_CONVENIO,
             'Grupo 5, «%s», del convenio de la Comunidad de Madrid (código %s, '
             'revisión 2026 en el %s). Sustitúyelo por el de TU convenio '
             'provincial.'
             % (D.CONVENIO[4][1], D.CONVENIO_CODIGO, D.CONVENIO_PUBLICACION))
    C.nota_celda(ws, br.coordinate, 'PA-33')
    pg = par(ws, 18, 'Pagas del convenio al año', D.CONVENIO_PAGAS, C.ENT,
             'pagas', D.FUENTE_CONVENIO,
             'El convenio de Madrid paga 15, no 14: cambia el coste mes a mes.')
    C.nota_celda(ws, pg.coordinate, 'PA-33')
    par(ws, 19, 'Seguridad Social a cargo de la empresa', D.P('ss_empresa'),
        C.PCT, 'sobre bruto', 'motor.PARAMETROS',
        'Cotización empresarial aproximada sobre el bruto (contingencias '
        'comunes, desempleo, FOGASA y formación). Ajústala a tu convenio y a '
        'tus contratos.')
    par(ws, 20, 'Horas anuales de contrato', D.P('horas_anuales_contrato'),
        C.ENT, 'horas/año', 'supuesto',
        '40 horas por 52 semanas son 2.080, menos vacaciones y festivos del '
        'calendario laboral.')
    # Hallazgo B7 (2026-09-10): el pack publica tres costes por hora
    # distintos para la misma plantilla (13,36 € aquí, del grupo 5; 17,94 € en
    # el libro 4, obrador y sólo horas productivas; 14,89 € en el libro 8,
    # media pagada de toda la plantilla). El título deja el denominador
    # explícito.
    par(ws, 21, 'Coste por hora PAGADA del refuerzo (grupo 5)', None, C.EUR,
        '€/hora', 'calculado',
        'Bruto mensual por pagas por (1 más Seguridad Social), dividido por '
        'las horas anuales de contrato. Es el coste de verdad, no el bruto. '
        'NO es el «coste hora productiva de obrador» del libro 4 (17,94 €) ni '
        'el «coste medio por hora pagada de la plantilla» del libro 8 '
        '(14,89 €): las tres son correctas y miden un denominador distinto.',
        formula='=IFERROR(%s*%s*(1+%s)/%s,"")'
                % (A(P_BRUTO), A(P_PAGAS), A(P_SS), A(P_HANIO)))

    C.seccion(ws, 'A23', 'Dinero, IVA y umbrales')
    par(ws, 24, 'Tipo de interés anual del circulante', D.FINANCIACION['tipo_nominal'],
        C.PCT, 'anual', 'supuesto',
        'Coste del dinero que tienes parado en materia prima de campaña. Si '
        'financias la compra con póliza, pon el tipo de tu póliza; si la pagas '
        'de tu caja, pon lo que te costaría pedirla.')
    iv = par(ws, 25, 'IVA de pastelería, bollería y confitería',
             D.P('iva_producto'), C.PCT, 'sobre base', 'PA-36',
             'Regla general de alimentos del art. 91.Uno.1.1.º de la Ley '
             '37/1992: no porque un precepto los nombre, sino porque no están '
             'en la lista cerrada del 4' + C.N + '% ni excluidos del 10' + C.N + '%.')
    C.nota_celda(ws, iv.coordinate, 'PA-36')
    ivp = par(ws, 26, 'IVA del pan del RD 308/2019', D.P('iva_pan'), C.PCT,
              'sobre base', 'PA-36b',
              'Todos los productos del RD 308/2019 van al 4' + C.N + '% desde '
              'la Resolución vinculante de la DGT de 24-02-2025. El cruasán '
              'sigue al 10' + C.N + '%: el RD 308/2019 sólo regula el pan.')
    C.nota_celda(ws, ivp.coordinate, 'PA-36b')
    par(ws, 27, 'Umbral para marcar una campaña como grande',
        UMBRAL_PICO_ANIO, C.PCT, 'del año', 'supuesto',
        'Porcentaje de las ventas del año por encima del cual la hoja «Peso '
        'sobre el Año» resalta la campaña. Criterio de la casa, no del sector.')

    motor.val(ws, 'A29', C.VERSION_LINE)
    ws['A29'].font = Font(size=8, italic=True)
    C.setup(ws, landscape=True)
    return ws


# --------------------------------------------------------------------------
# Hoja «Calendario de 6 Picos»
# --------------------------------------------------------------------------
def hoja_calendario(wb):
    ws = wb.create_sheet(H_CAL)
    C.cabecera_hoja(ws, 'Calendario de 6 Picos')
    motor.val(ws, 'A3', 'Las FECHAS y el qué hacer están en el '
                        '«BONUS-02-calendario-anual-tareas.xlsx» del Kit de '
                        'Tareas Pastelería. Esta hoja pone los EUROS.')
    ws['A3'].font = Font(italic=True, size=9)

    cols = [
        ('A', '#', 4), ('B', 'Campaña', 24),
        ('C', 'Fechas de referencia', 30), ('D', 'Mes', 6),
        ('E', 'Días de campaña', 8), ('F', 'Producto estrella', 24),
        ('G', 'IVA', 7), ('H', 'PVP con IVA (€)', 10),
        ('I', 'PVP sin IVA (€)', 10),
        ('J', 'Uds/día fuera de campaña', 10),
        ('K', 'Uds/día en campaña', 10),
        ('L', 'Uds/día incrementales', 10),
        ('M', 'Uds de toda la campaña', 11),
        ('N', 'Facturación de la campaña sin IVA (€)', 13),
        ('O', 'Facturación incremental sin IVA (€)', 13),
        ('P', 'Factor sobre el obrador', 9),
        ('Q', 'Antelación de compra (semanas)', 10),
        ('R', 'Qué hay que saber de esta campaña', 92),
    ]
    C.encabezados(ws, 5, cols)

    for i, p in enumerate(D.PICOS):
        r = CAL_INI + i
        est = ESTRELLA[i]
        motor.val(ws, 'A%d' % r, i + 1)
        motor.val(ws, 'B%d' % r, p['nombre'], bold=True)
        motor.val(ws, 'C%d' % r, p['fechas'], wrap=True)
        C.entrada(ws, 'D%d' % r, p['mes'], fmt=C.ENT,
                  etiqueta='Mes de %s' % p['nombre'])
        C.entrada(ws, 'E%d' % r, p['dias_campana'], fmt=C.ENT,
                  etiqueta='Días de campaña de %s' % p['nombre'])
        motor.val(ws, 'F%d' % r, est['nombre'], wrap=True)
        cel = C.entrada(ws, 'G%d' % r, est['iva'], fmt=C.PCT,
                        etiqueta='IVA del producto estrella de %s' % p['nombre'])
        C.nota_celda(ws, cel.coordinate,
                     'PA-36b' if est['familia'] == 'Panes de acompañamiento'
                     else 'PA-36')
        C.entrada(ws, 'H%d' % r, est['pvp_con_iva'], fmt=C.EUR,
                  etiqueta='PVP con IVA del producto estrella de %s' % p['nombre'])
        motor.f(ws, 'I%d' % r, '=IFERROR(H{r}/(1+G{r}),"")'.format(r=r),
                fmt=C.EUR)
        C.entrada(ws, 'J%d' % r, p['uds_dia_normal'], fmt=C.ENT,
                  etiqueta='Uds/día fuera de campaña de %s' % p['nombre'])
        C.entrada(ws, 'K%d' % r, p['uds_dia_pico'], fmt=C.ENT,
                  etiqueta='Uds/día en campaña de %s' % p['nombre'])
        motor.f(ws, 'L%d' % r, '=IFERROR(K{r}-J{r},"")'.format(r=r), fmt=C.ENT)
        motor.f(ws, 'M%d' % r, '=IFERROR(K{r}*E{r},"")'.format(r=r), fmt=C.ENT)
        motor.f(ws, 'N%d' % r, '=IFERROR(M{r}*I{r},"")'.format(r=r), fmt=C.EUR)
        motor.f(ws, 'O%d' % r, '=IFERROR(L{r}*E{r}*I{r},"")'.format(r=r),
                fmt=C.EUR)
        C.entrada(ws, 'P%d' % r, p['factor_obrador'], fmt=C.DEC1,
                  etiqueta='Factor sobre el obrador de %s' % p['nombre'])
        C.entrada(ws, 'Q%d' % r, p['antelacion_compra_semanas'], fmt=C.ENT,
                  etiqueta='Antelación de compra de %s' % p['nombre'])
        motor.val(ws, 'R%d' % r, p['nota'], wrap=True)
        ws['R%d' % r].font = Font(size=8)
        ws.row_dimensions[r].height = 72

    motor.val(ws, 'B%d' % CAL_TOT, 'TOTAL DE LAS SEIS CAMPAÑAS', bold=True)
    for col, fmt in (('E', C.ENT), ('M', C.ENT), ('N', C.EUR), ('O', C.EUR)):
        C.crema(motor.f(ws, '%s%d' % (col, CAL_TOT),
                        '=SUM({c}{a}:{c}{b})'.format(c=col, a=CAL_INI, b=CAL_FIN),
                        fmt=fmt, bold=True))

    C.apunte(ws, 'A%d' % (CAL_TOT + 2),
             'El factor de campaña multiplica las piezas del OBRADOR ENTERO, no '
             'las del producto estrella: por eso Reyes lleva un 6,0 y San '
             'Valentín un 1,8 aunque las dos sean campañas. Las unidades del '
             'producto estrella son las de esta hoja; el obrador entero se '
             'trata en «Capacidad vs Demanda del Pico».')
    ws.merge_cells('A%d:R%d' % (CAL_TOT + 2, CAL_TOT + 2))
    ws.row_dimensions[CAL_TOT + 2].height = 32
    motor.val(ws, 'A%d' % (CAL_TOT + 4), C.VERSION_LINE)
    ws['A%d' % (CAL_TOT + 4)].font = Font(size=8, italic=True)

    motor.dv_numerica(ws, ['D%d' % r for r in range(CAL_INI, CAL_FIN + 1)],
                      minimo=1, maximo=12, titulo='Mes',
                      mensaje='El mes va de 1 a 12.')
    motor.dv_porcentaje(ws, ['G%d' % r for r in range(CAL_INI, CAL_FIN + 1)],
                        titulo='Tipo de IVA',
                        prompt='Se escribe en tanto por uno: 0,10 = 10 %.')
    ws.freeze_panes = 'D6'
    C.setup(ws)
    return ws


# --------------------------------------------------------------------------
# Hoja «Peso sobre el Año»
# --------------------------------------------------------------------------
def hoja_anio(wb):
    ws = wb.create_sheet(H_ANO)
    C.cabecera_hoja(ws, 'Peso sobre el Año')
    motor.val(ws, 'A3', 'Qué parte del año se juega en cada campaña. Es el '
                        'número que decide si merece la pena montarla.')
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, 5, [
        ('A', 'Mes', 16), ('B', 'Coeficiente sobre el mes medio', 12),
        ('C', 'Ventas del mes sin IVA (€)', 14),
        ('D', '% sobre el año', 11),
        ('E', 'Campañas que caen en el mes', 34),
        ('F', 'Por qué ese coeficiente', 74)], alto=42)

    picos_por_mes = {}
    for p in D.PICOS:
        picos_por_mes.setdefault(p['mes'], []).append(p['nombre'])
    razon = {
        1: 'Reyes. Es el mes más alto del año y el que decide la campaña.',
        2: 'San Valentín son dos días y febrero tiene 28: una campaña de esa '
           'longitud no levanta un mes entero.',
        3: 'El Día del Padre es un día. Mismo razonamiento que febrero.',
        4: 'Semana Santa y el arranque de las comuniones.',
        5: 'Día de la Madre y meseta de comuniones: dos meses de encargos.',
        6: 'Final de comuniones y caída del consumo con el calor.',
        7: 'Verano: baja el consumo de pastelería y sube el de helado, que no '
           'está en la carta de La Clara.',
        8: 'La Clara cierra dos semanas en agosto (los 300 días de apertura '
           'del año salen de ahí).',
        9: 'Vuelta al colegio y mes de apertura recomendado: fuera de pico y '
           'con tres meses y medio de rodaje antes de Reyes.',
        10: 'Mes de transición; Todos los Santos empieza el día 30.',
        11: 'Todos los Santos y arranque de la producción de Navidad.',
        12: 'Navidad: turrones, polvorones y el prólogo de Reyes.',
    }
    for i, mes in enumerate(D.MESES):
        r = MES_INI + i
        motor.val(ws, 'A%d' % r, mes)
        C.entrada(ws, 'B%d' % r, D.ESTACIONALIDAD_MENSUAL[i], fmt=C.DEC,
                  etiqueta='Coeficiente de estacionalidad de %s' % mes)
        motor.f(ws, 'C%d' % r,
                '=IFERROR({v}*B{r}/$B${t},"")'.format(v=A(P_VENTAS), r=r,
                                                      t=MES_TOT),
                fmt=C.EUR)
        motor.f(ws, 'D%d' % r,
                '=IFERROR(C{r}/{v},"")'.format(r=r, v=A(P_VENTAS)), fmt=C.PCT)
        motor.val(ws, 'E%d' % r, ', '.join(picos_por_mes.get(i + 1, [])) or '-',
                  wrap=True)
        motor.val(ws, 'F%d' % r, razon[i + 1], wrap=True)
        ws['F%d' % r].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[r].height = 30

    motor.val(ws, 'A%d' % MES_TOT, 'TOTAL AÑO', bold=True)
    C.crema(motor.f(ws, 'B%d' % MES_TOT,
                    '=SUM(B{a}:B{b})'.format(a=MES_INI, b=MES_FIN), fmt=C.DEC,
                    bold=True))
    C.crema(motor.f(ws, 'C%d' % MES_TOT,
                    '=SUM(C{a}:C{b})'.format(a=MES_INI, b=MES_FIN), fmt=C.EUR,
                    bold=True))
    C.crema(motor.f(ws, 'D%d' % MES_TOT,
                    '=SUM(D{a}:D{b})'.format(a=MES_INI, b=MES_FIN), fmt=C.PCT,
                    bold=True))
    C.apunte(ws, 'F%d' % MES_TOT,
             'Los doce coeficientes se reparten sobre el mes medio, así que su '
             'suma tiene que dar 12,00. Si cambias uno, el reparto se '
             'recalcula solo y las ventas del año no se mueven.')

    # --- bloque de picos --------------------------------------------------
    C.seccion(ws, 'A%d' % (PIC_INI - 3), 'Lo que pesa cada campaña')
    C.encabezados(ws, PIC_INI - 1, [
        ('A', 'Campaña', None), ('B', 'Días de campaña', None),
        ('C', 'Facturación de la campaña sin IVA (€)', None),
        ('D', '% sobre el año', None),
        ('E', 'Facturación incremental sin IVA (€)', None),
        ('F', '% incremental sobre el año', None),
        ('G', '€ por día de campaña', None),
        ('H', '€ por día medio del año', None),
        ('I', 'Cuántas veces un día normal', None)], alto=42)
    ws.column_dimensions['G'].width = 13
    ws.column_dimensions['H'].width = 13
    ws.column_dimensions['I'].width = 13

    for i, p in enumerate(D.PICOS):
        r = PIC_INI + i
        cr = CAL_INI + i
        motor.val(ws, 'A%d' % r, p['nombre'], bold=True)
        motor.f(ws, 'B%d' % r, '={q}E{c}'.format(q=QCAL, c=cr), fmt=C.ENT)
        motor.f(ws, 'C%d' % r, '={q}N{c}'.format(q=QCAL, c=cr), fmt=C.EUR)
        motor.f(ws, 'D%d' % r, '=IFERROR(C{r}/{v},"")'.format(r=r, v=A(P_VENTAS)),
                fmt=C.PCT)
        motor.f(ws, 'E%d' % r, '={q}O{c}'.format(q=QCAL, c=cr), fmt=C.EUR)
        motor.f(ws, 'F%d' % r, '=IFERROR(E{r}/{v},"")'.format(r=r, v=A(P_VENTAS)),
                fmt=C.PCT)
        motor.f(ws, 'G%d' % r, '=IFERROR(C{r}/B{r},"")'.format(r=r), fmt=C.EUR)
        motor.f(ws, 'H%d' % r, '=IFERROR({v}/{d},"")'.format(v=A(P_VENTAS),
                                                             d=A(P_DIAS)),
                fmt=C.EUR)
        motor.f(ws, 'I%d' % r, '=IFERROR(G{r}/H{r},"")'.format(r=r), fmt=C.DEC1)

    motor.val(ws, 'A%d' % PIC_TOT, 'TOTAL DE LAS SEIS CAMPAÑAS', bold=True)
    for col, fmt in (('B', C.ENT), ('C', C.EUR), ('D', C.PCT), ('E', C.EUR),
                     ('F', C.PCT)):
        C.crema(motor.f(ws, '%s%d' % (col, PIC_TOT),
                        '=SUM({c}{a}:{c}{b})'.format(c=col, a=PIC_INI, b=PIC_FIN),
                        fmt=fmt, bold=True))

    motor.semaforo_isnumber(ws, 'D%d:D%d' % (PIC_INI, PIC_FIN),
                            '$D%d' % PIC_INI, operador='>=',
                            umbral=A(P_UMBRAL), bg='FFF3C4', fg='7A5C00')
    motor.semaforo_isnumber(ws, 'I%d:I%d' % (PIC_INI, PIC_FIN),
                            '$I%d' % PIC_INI, operador='>=', umbral='2',
                            bg='FFF3C4', fg='7A5C00')

    C.apunte(ws, 'A%d' % (PIC_TOT + 2),
             'La «facturación de la campaña» cuenta TODAS las unidades del '
             'producto estrella que vendes esos días; la «incremental» sólo '
             'las que no habrías vendido de todas formas. Para decidir si '
             'montas la campaña manda la incremental. Para saber si aguantas, '
             'manda la total.')
    ws.merge_cells('A%d:I%d' % (PIC_TOT + 2, PIC_TOT + 2))
    ws.row_dimensions[PIC_TOT + 2].height = 32
    motor.val(ws, 'A%d' % (PIC_TOT + 4), C.VERSION_LINE)
    ws['A%d' % (PIC_TOT + 4)].font = Font(size=8, italic=True)
    ws.freeze_panes = 'A6'          # hallazgo B12 (2026-09-10)
    C.setup(ws)
    return ws


# --------------------------------------------------------------------------
# Hoja «Capacidad vs Demanda del Pico»
# --------------------------------------------------------------------------
def hoja_capacidad(wb):
    ws = wb.create_sheet(H_CAP)
    C.cabecera_hoja(ws, 'Capacidad vs Demanda del Pico')
    motor.val(ws, 'A3', 'La pregunta del libro: ¿aguantas Reyes con el equipo '
                        'que estás comprando?')
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, 5, [
        ('A', 'Campaña', 24), ('B', 'Días de campaña', 8),
        ('C', 'Factor sobre el crucero', 9),
        ('D', 'Demanda piezas/día', 10),
        ('E', 'Demanda de toda la campaña', 11),
        ('F', 'Horas de obrador al día en campaña', 10),
        ('G', 'Capacidad piezas/día en campaña', 10),
        ('H', 'Déficit diario', 10),
        ('I', 'Déficit de toda la campaña', 11),
        ('J', 'Días de producción adelantada', 10),
        ('K', 'Piezas que puedes adelantar', 11),
        ('L', 'Déficit tras adelantar', 11),
        ('M', 'Horas de obrador al día que harían falta', 11),
        ('N', '¿Aguantas?', 11),
        ('O', 'Horas de obrador que faltan', 11),
        ('P', 'Personas de refuerzo necesarias', 10),
        ('Q', 'Qué palanca te falta', 62)])

    for i, p in enumerate(D.PICOS):
        r = CAP_INI + i
        cr = CAL_INI + i
        motor.val(ws, 'A%d' % r, p['nombre'], bold=True)
        motor.f(ws, 'B%d' % r, '={q}E{c}'.format(q=QCAL, c=cr), fmt=C.ENT)
        motor.f(ws, 'C%d' % r, '={q}P{c}'.format(q=QCAL, c=cr), fmt=C.DEC1)
        motor.f(ws, 'D%d' % r, '=IFERROR({p}*C{r},"")'.format(p=A(P_PIEZAS), r=r),
                fmt=C.ENT)
        motor.f(ws, 'E%d' % r, '=IFERROR(D{r}*B{r},"")'.format(r=r), fmt=C.ENT)
        C.entrada(ws, 'F%d' % r, HORAS_CAMPANA[p['nombre']], fmt=C.DEC1,
                  etiqueta='Horas de obrador al día en campaña de %s' % p['nombre'])
        motor.f(ws, 'G%d' % r, '=IFERROR({h}*F{r},"")'.format(h=A(P_PZH), r=r),
                fmt=C.ENT)
        motor.f(ws, 'H%d' % r, '=IFERROR(MAX(0,D{r}-G{r}),"")'.format(r=r),
                fmt=C.ENT)
        motor.f(ws, 'I%d' % r, '=IFERROR(H{r}*B{r},"")'.format(r=r), fmt=C.ENT)
        C.entrada(ws, 'J%d' % r, DIAS_ADELANTO[p['nombre']], fmt=C.ENT,
                  etiqueta='Días de producción adelantada de %s' % p['nombre'])
        motor.f(ws, 'K%d' % r,
                '=IFERROR(MIN(I{r},MAX(0,{e})*J{r}),"")'.format(r=r, e=A(P_EXCED)),
                fmt=C.ENT)
        motor.f(ws, 'L%d' % r, '=IFERROR(MAX(0,I{r}-K{r}),"")'.format(r=r),
                fmt=C.ENT)
        motor.f(ws, 'M%d' % r,
                '=IFERROR((E{r}-K{r})/B{r}/{h},"")'.format(r=r, h=A(P_PZH)),
                fmt=C.DEC1)
        motor.f(ws, 'N%d' % r,
                '=IF(L{r}="","",IF(L{r}<=0,"Sí","No"))'.format(r=r))
        motor.f(ws, 'O%d' % r, '=IFERROR(L{r}/{h},"")'.format(r=r, h=A(P_PZH)),
                fmt=C.DEC1)
        motor.f(ws, 'P%d' % r,
                '=IFERROR(ROUNDUP(O{r}/(B{r}*{hp}),0),"")'.format(r=r,
                                                                  hp=A(P_HPERS)),
                fmt=C.ENT)
        motor.f(ws, 'Q%d' % r,
                '=IF(L{r}="","",IF(L{r}<=0,'
                '"Con estas horas y este adelanto, la campaña cabe.",'
                'IF(M{r}>{hm},'
                '"No cabe ni con el día entero: hay que adelantar y congelar más, '
                'o recortar el surtido de campaña.",'
                '"Cabe alargando el turno con refuerzo: mira la hoja Refuerzo y '
                'Tesorería.")))'.format(r=r, hm=A(P_HMAX)))
        ws['Q%d' % r].alignment = Alignment(wrap_text=True, vertical='top')
        ws.row_dimensions[r].height = 34

    motor.val(ws, 'A%d' % CAP_TOT, 'TOTAL DE LAS SEIS CAMPAÑAS', bold=True)
    for col in ('E', 'I', 'K', 'L'):
        C.crema(motor.f(ws, '%s%d' % (col, CAP_TOT),
                        '=SUM({c}{a}:{c}{b})'.format(c=col, a=CAP_INI, b=CAP_FIN),
                        fmt=C.ENT, bold=True))
    C.crema(motor.f(ws, 'N%d' % CAP_TOT,
                    '=COUNTIF(N{a}:N{b},"No")'.format(a=CAP_INI, b=CAP_FIN),
                    fmt=C.ENT, bold=True))
    motor.val(ws, 'O%d' % CAP_TOT, 'campañas que NO aguantas')
    ws['O%d' % CAP_TOT].font = Font(size=8, color=C.GRIS)

    motor.semaforo_texto(ws, 'N%d:N%d' % (CAP_INI, CAP_FIN),
                         ((('Sí'), 'C8E6C9', '1B5E20'),
                          (('No'), 'FFCDD2', 'B71C1C')))
    motor.semaforo_isnumber(ws, 'M%d:M%d' % (CAP_INI, CAP_FIN),
                            '$M%d' % CAP_INI, operador='>', umbral=A(P_HMAX))
    motor.semaforo_isnumber(ws, 'L%d:L%d' % (CAP_INI, CAP_FIN),
                            '$L%d' % CAP_INI, operador='>', umbral='0')

    fila = CAP_TOT + 2
    for texto in (
        'Cómo se lee: la demanda del pico sale de multiplicar tus piezas de un '
        'día normal por el factor de la campaña. La capacidad sale de las '
        'piezas por hora del equipo que te limita por las horas que tengas el '
        'obrador en marcha. La diferencia es el déficit, y se ataca en este '
        'orden: primero horas de máquina, después producción adelantada y '
        'congelada, y sólo al final refuerzo de personal, que es lo que cuesta '
        'dinero todos los días de la campaña.',
        'Las piezas que puedes adelantar están limitadas por el excedente de '
        'un día normal: si en crucero ya vas al límite, no tienes de dónde '
        'sacarlas. Y por lo que te quepa en el congelador, que esta hoja no '
        'sabe. Comprueba los metros cúbicos antes de dar por buena la cifra.',
        'Lo que NO se puede adelantar: todo lo que el art. 9.3 del RD 1021/2022 '
        'obliga a consumir en 24 horas desde su elaboración, y lo relleno no '
        'estable que va a 4' + C.N + '°C por la fila 9 del art. 4.1. El roscón '
        'relleno de nata es el caso de manual: se hace el mismo día. Los huesos '
        'de santo, que son estables a temperatura ambiente, sí se adelantan. '
        'Ese detalle legal ES la planificación de la campaña, y la hoja '
        '«Decisión de Huevo y Temperatura» del libro '
        '«carta-de-apertura-y-escandallo.xlsx» dice cuál es cuál.',
    ):
        motor.val(ws, 'A%d' % fila, texto, wrap=True)
        ws.merge_cells('A%d:Q%d' % (fila, fila))
        ws['A%d' % fila].font = Font(size=9)
        ws.row_dimensions[fila].height = 58
        fila += 1
    motor.val(ws, 'A%d' % (fila + 1), C.VERSION_LINE)
    ws['A%d' % (fila + 1)].font = Font(size=8, italic=True)

    motor.dv_numerica(ws, ['F%d' % r for r in range(CAP_INI, CAP_FIN + 1)],
                      minimo=0, maximo=24, titulo='Horas al día',
                      mensaje='Las horas de obrador al día van de 0 a 24.')
    motor.dv_numerica(ws, ['J%d' % r for r in range(CAP_INI, CAP_FIN + 1)],
                      minimo=0, maximo=120, titulo='Días de adelanto',
                      mensaje='Escribe los días de producción adelantada '
                              '(0 a 120).')
    ws.freeze_panes = 'B6'
    C.setup(ws)
    return ws


# --------------------------------------------------------------------------
# Hoja «Refuerzo y Tesorería»
# --------------------------------------------------------------------------
def hoja_refuerzo(wb):
    ws = wb.create_sheet(H_REF)
    C.cabecera_hoja(ws, 'Refuerzo y Tesorería')
    motor.val(ws, 'A3', 'Cuánto cuesta el refuerzo con la Seguridad Social '
                        'dentro, y cuánto dinero deja parado cada campaña.')
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, 5, [
        ('A', 'Campaña', 24),
        ('B', 'Personas de refuerzo', 9),
        ('C', 'Horas por persona en la campaña', 10),
        ('D', 'Horas totales de refuerzo', 10),
        ('E', 'Coste hora de empresa (€)', 10),
        ('F', 'Coste del refuerzo (€)', 11),
        ('G', 'Personas necesarias', 10),
        ('H', '¿Cubre el refuerzo?', 11),
        ('I', 'Coste de materia por unidad (€)', 11),
        ('J', 'Uds de toda la campaña', 10),
        ('K', 'Compra de materia de la campaña (€)', 12),
        ('L', 'Antelación de compra (semanas)', 10),
        ('M', 'Días con el dinero parado', 10),
        ('N', 'Coste financiero del inmovilizado (€)', 12),
        ('O', 'Materia de las uds incrementales (€)', 12),
        ('P', 'Facturación incremental sin IVA (€)', 12),
        ('Q', 'Resultado incremental de la campaña (€)', 12),
        ('R', 'Qué mirar en esta campaña', 74)])

    for i, p in enumerate(D.PICOS):
        r = REF_INI + i
        cr = CAL_INI + i
        cp = CAP_INI + i
        est = ESTRELLA[i]
        motor.val(ws, 'A%d' % r, p['nombre'], bold=True)
        C.entrada(ws, 'B%d' % r, p['refuerzo_personas'], fmt=C.ENT,
                  etiqueta='Personas de refuerzo de %s' % p['nombre'])
        C.entrada(ws, 'C%d' % r, p['refuerzo_horas_persona'], fmt=C.DEC1,
                  etiqueta='Horas por persona de refuerzo de %s' % p['nombre'])
        motor.f(ws, 'D%d' % r, '=IFERROR(B{r}*C{r},"")'.format(r=r), fmt=C.DEC1)
        motor.f(ws, 'E%d' % r, '={c}'.format(c=A(P_CHORA)), fmt=C.EUR)
        motor.f(ws, 'F%d' % r, '=IFERROR(D{r}*E{r},"")'.format(r=r), fmt=C.EUR)
        motor.f(ws, 'G%d' % r, '={q}P{c}'.format(q=QCAP, c=cp), fmt=C.ENT)
        motor.f(ws, 'H%d' % r,
                '=IF(G{r}="","",IF(B{r}>=G{r},"Sí","No"))'.format(r=r))
        C.entrada(ws, 'I%d' % r, round(D.coste_materia_unidad(est), 4),
                  fmt=C.EUR,
                  etiqueta='Coste de materia por unidad del producto estrella '
                           'de %s' % p['nombre'])
        motor.f(ws, 'J%d' % r, '={q}M{c}'.format(q=QCAL, c=cr), fmt=C.ENT)
        motor.f(ws, 'K%d' % r, '=IFERROR(I{r}*J{r},"")'.format(r=r), fmt=C.EUR)
        motor.f(ws, 'L%d' % r, '={q}Q{c}'.format(q=QCAL, c=cr), fmt=C.ENT)
        motor.f(ws, 'M%d' % r,
                '=IFERROR(L{r}*7+{q}E{c},"")'.format(r=r, q=QCAL, c=cr),
                fmt=C.ENT)
        motor.f(ws, 'N%d' % r,
                '=IFERROR(K{r}*{i}*M{r}/365,"")'.format(r=r, i=A(P_INT)),
                fmt=C.EUR)
        motor.f(ws, 'O%d' % r,
                '=IFERROR(I{r}*{q}L{c}*{q}E{c},"")'.format(r=r, q=QCAL, c=cr),
                fmt=C.EUR)
        motor.f(ws, 'P%d' % r, '={q}O{c}'.format(q=QCAL, c=cr), fmt=C.EUR)
        motor.f(ws, 'Q%d' % r,
                '=IFERROR(P{r}-O{r}-F{r}-N{r},"")'.format(r=r), fmt=C.EUR)
        motor.val(ws, 'R%d' % r, comentario_campana(p), wrap=True)
        ws['R%d' % r].font = Font(size=8)
        ws.row_dimensions[r].height = 62

    motor.val(ws, 'A%d' % REF_TOT, 'TOTAL DEL AÑO', bold=True)
    for col, fmt in (('D', C.DEC1), ('F', C.EUR), ('K', C.EUR), ('N', C.EUR),
                     ('O', C.EUR), ('P', C.EUR), ('Q', C.EUR)):
        C.crema(motor.f(ws, '%s%d' % (col, REF_TOT),
                        '=SUM({c}{a}:{c}{b})'.format(c=col, a=REF_INI, b=REF_FIN),
                        fmt=fmt, bold=True))
    C.crema(motor.f(ws, 'H%d' % REF_TOT,
                    '=COUNTIF(H{a}:H{b},"No")'.format(a=REF_INI, b=REF_FIN),
                    fmt=C.ENT, bold=True))
    motor.val(ws, 'I%d' % REF_TOT, 'campañas con refuerzo corto')
    ws['I%d' % REF_TOT].font = Font(size=8, color=C.GRIS)

    motor.semaforo_texto(ws, 'H%d:H%d' % (REF_INI, REF_FIN),
                         ((('Sí'), 'C8E6C9', '1B5E20'),
                          (('No'), 'FFCDD2', 'B71C1C')))
    motor.semaforo_isnumber(ws, 'Q%d:Q%d' % (REF_INI, REF_FIN),
                            '$Q%d' % REF_INI, operador='<', umbral='0')

    fila = REF_TOT + 2
    for texto in (
        'El coste hora de empresa no es el bruto: es el bruto por las pagas del '
        'convenio, más la Seguridad Social a cargo de la empresa, dividido por '
        'las horas anuales de contrato. Sale de la hoja «Parámetros» y en el '
        'ejemplo es casi un tercio más que el bruto. Contratar refuerzo por '
        'debajo de ese número es contratar a pérdida.',
        'La «compra de materia de la campaña» es el dinero que sale de tu caja '
        'ANTES de que entre el primero de la campaña. Multiplicado por los días '
        'que está parado y por el coste del dinero, tienes el coste financiero '
        'de la campaña, que casi nadie cuenta y que en Reyes es real.',
        'El «resultado incremental» descuenta sólo lo que la campaña añade: la '
        'materia de las unidades de más, el refuerzo y el coste financiero. No '
        'descuenta alquiler ni personal fijo, que los pagas igual. Si sale '
        'negativo, la campaña te está costando dinero.',
        'Frontera con el Kit de Tareas Pastelería (12 €): el '
        '«BONUS-02-calendario-anual-tareas.xlsx» te dice QUÉ hacer y CUÁNDO en '
        'cada campaña, y el «06-eventos-festivos.xlsx» lleva el detalle de cada '
        'evento. Este libro te dice CUÁNTO cuesta y SI aguantas. Si ya tienes '
        'el kit, sustituye las estimaciones de unidades por tus datos reales '
        'de producción del «10-plan-produccion-semanal.xlsx».',
    ):
        motor.val(ws, 'A%d' % fila, texto, wrap=True)
        ws.merge_cells('A%d:R%d' % (fila, fila))
        ws['A%d' % fila].font = Font(size=9)
        ws.row_dimensions[fila].height = 52
        fila += 1
    motor.val(ws, 'A%d' % (fila + 1), C.VERSION_LINE)
    ws['A%d' % (fila + 1)].font = Font(size=8, italic=True)

    motor.dv_numerica(ws, ['B%d' % r for r in range(REF_INI, REF_FIN + 1)],
                      minimo=0, maximo=50, titulo='Personas de refuerzo',
                      mensaje='Escribe cuántas personas de refuerzo contratas '
                              '(0 a 50).')
    motor.dv_numerica(ws, ['C%d' % r for r in range(REF_INI, REF_FIN + 1)],
                      minimo=0, maximo=400, titulo='Horas por persona',
                      mensaje='Horas de toda la campaña por persona (0 a 400).')
    ws.freeze_panes = 'B6'
    C.setup(ws)
    return ws


def comentario_campana(p):
    especiales = {
        'Reyes': 'La campaña que decide el año. Seis semanas de antelación de '
                 'compra: la almendra, la naranja confitada y el agua de azahar '
                 'se piden en noviembre. El roscón relleno no se puede '
                 'adelantar: 4' + C.N + '°C y 24 horas.',
        # Hallazgo B11 (2026-09-10): F7=0,00 € y H7=«No» son un cero REAL, no
        # un fallo -pero un capítulo que cite sólo F7 («el refuerzo cuesta
        # 0,00 €») suena a error si no la lee junto con esta nota. Explícito
        # aquí para que el guion cite las dos juntas o ninguna.
        'San Valentín': 'Dos días y ticket alto: se gana con cajas y '
                        'presentación, no con más horno. El refuerzo sale a '
                        'CERO personas y CERO euros a propósito -la persona '
                        'que hace falta ya está en la plantilla base-, y por '
                        'eso «¿Cubre el refuerzo?» dice «No»: no es un fallo, '
                        'es que aquí no se contrata refuerzo, se cubre con '
                        'plantilla.',
        'Día del Padre y de la Madre': 'Dos fechas con el mismo patrón de '
                                       'trabajo -tarta con dedicatoria, por '
                                       'encargo- y por eso van juntas como una '
                                       'sola campaña operativa.',
        'Semana Santa': 'Ocho días seguidos de producción extra, más agotador '
                        'que los cinco de Reyes aunque el pico sea menor. '
                        'Torrijas y monas a la vez: una pide freidora y frío, '
                        'la otra horno y chocolate.',
        'Comuniones': 'No es un pico, es una meseta de dos meses: se aguanta '
                      'con plantilla, no con horas extra, y por eso los días '
                      'de adelanto van a cero. Todo por encargo, con anticipo '
                      'y riesgo de anulación.',
        'Todos los Santos': 'Tres días con tres referencias que sólo se hacen '
                            'ahora. Los buñuelos van rellenos (4' + C.N + '°C y '
                            '24 horas) y los huesos de santo son estables a '
                            'temperatura ambiente: por eso éstos sí se '
                            'adelantan y aquéllos no.',
    }
    return especiales[p['nombre']]


# --------------------------------------------------------------------------
# Mapa de celdas citables
# --------------------------------------------------------------------------
def mapa_celdas():
    m = [
        ('Ventas anuales sin IVA en crucero', H_PAR, P_VENTAS, 'entrada'),
        ('Piezas al día en velocidad de crucero', H_PAR, P_PIEZAS, 'entrada'),
        ('Días de apertura al año', H_PAR, P_DIAS, 'entrada'),
        ('Capacidad del obrador en jornada normal', H_PAR, P_CAPDIA,
         'entrada'),
        ('Horas de obrador al día en jornada normal', H_PAR, P_HTURNO,
         'entrada'),
        ('Piezas por hora de reloj del equipo que limita', H_PAR, P_PZH,
         'salida'),
        ('Excedente diario sobre la velocidad de crucero', H_PAR, P_EXCED,
         'salida'),
        ('Bruto mensual del convenio del refuerzo', H_PAR, P_BRUTO, 'parametro'),
        ('Pagas del convenio al año', H_PAR, P_PAGAS, 'parametro'),
        ('Seguridad Social a cargo de la empresa', H_PAR, P_SS, 'parametro'),
        ('Coste por hora pagada del refuerzo (grupo 5)', H_PAR, P_CHORA, 'salida'),
        ('Tipo de interés anual del circulante', H_PAR, P_INT, 'parametro'),
        ('IVA de pastelería', H_PAR, P_IVAP, 'parametro'),
        ('IVA del pan', H_PAR, P_IVAPAN, 'parametro'),
        ('Facturación de las seis campañas sin IVA', H_CAL, 'N%d' % CAL_TOT,
         'salida'),
        ('Facturación incremental de las seis campañas sin IVA', H_CAL,
         'O%d' % CAL_TOT, 'salida'),
        ('Unidades de producto estrella de las seis campañas', H_CAL,
         'M%d' % CAL_TOT, 'salida'),
        ('Días de campaña al año', H_CAL, 'E%d' % CAL_TOT, 'salida'),
        ('Suma de los coeficientes de estacionalidad', H_ANO, 'B%d' % MES_TOT,
         'salida'),
        ('Ventas del mes más alto (enero)', H_ANO, 'C%d' % MES_INI, 'salida'),
        ('Ventas del mes más bajo (agosto)', H_ANO, 'C%d' % (MES_INI + 7),
         'salida'),
        ('Peso de enero sobre el año', H_ANO, 'D%d' % MES_INI, 'salida'),
        ('Peso de agosto sobre el año', H_ANO, 'D%d' % (MES_INI + 7), 'salida'),
        ('Peso de las seis campañas sobre el año', H_ANO, 'D%d' % PIC_TOT,
         'salida'),
        ('Peso incremental de las seis campañas sobre el año', H_ANO,
         'F%d' % PIC_TOT, 'salida'),
        ('Campañas que NO aguanta el obrador', H_CAP, 'N%d' % CAP_TOT,
         'salida'),
        ('Demanda de piezas de las seis campañas', H_CAP, 'E%d' % CAP_TOT,
         'salida'),
        ('Déficit de piezas de las seis campañas', H_CAP, 'I%d' % CAP_TOT,
         'salida'),
        ('Piezas adelantables en las seis campañas', H_CAP, 'K%d' % CAP_TOT,
         'salida'),
        ('Déficit tras adelantar de las seis campañas', H_CAP,
         'L%d' % CAP_TOT, 'salida'),
        ('Coste del refuerzo de todo el año', H_REF, 'F%d' % REF_TOT, 'salida'),
        ('Tesorería inmovilizada en materia de campaña', H_REF,
         'K%d' % REF_TOT, 'salida'),
        ('Coste financiero del inmovilizado de campaña', H_REF,
         'N%d' % REF_TOT, 'salida'),
        ('Resultado incremental de las seis campañas', H_REF, 'Q%d' % REF_TOT,
         'salida'),
        ('Campañas con refuerzo corto', H_REF, 'H%d' % REF_TOT, 'salida'),
    ]
    for i, p in enumerate(D.PICOS):
        cr, cp, rr = CAL_INI + i, CAP_INI + i, REF_INI + i
        pr = PIC_INI + i
        n = p['nombre']
        m += [
            ('Facturación sin IVA de la campaña de %s' % n, H_CAL,
             'N%d' % cr, 'salida'),
            ('Facturación incremental sin IVA de la campaña de %s' % n, H_CAL,
             'O%d' % cr, 'salida'),
            ('Peso de %s sobre las ventas del año' % n, H_ANO, 'D%d' % pr,
             'salida'),
            ('Cuántas veces un día normal factura un día de %s' % n, H_ANO,
             'I%d' % pr, 'salida'),
            ('Demanda de piezas al día en %s' % n, H_CAP, 'D%d' % cp, 'salida'),
            ('Déficit diario de piezas en %s' % n, H_CAP, 'H%d' % cp, 'salida'),
            ('Horas de obrador al día que harían falta en %s' % n, H_CAP,
             'M%d' % cp, 'salida'),
            ('¿Aguanta el obrador la campaña de %s?' % n, H_CAP, 'N%d' % cp,
             'salida'),
            ('Coste del refuerzo de %s' % n, H_REF, 'F%d' % rr, 'salida'),
            ('Tesorería inmovilizada en la campaña de %s' % n, H_REF,
             'K%d' % rr, 'salida'),
            ('Días con el dinero parado en %s' % n, H_REF, 'M%d' % rr,
             'salida'),
            ('Resultado incremental de la campaña de %s' % n, H_REF,
             'Q%d' % rr, 'salida'),
        ]
    return m


NOTAS_MAPA = (
    'Frontera R5: el BONUS-02-calendario-anual-tareas.xlsx del Kit de Tareas '
    'Pastelería pone las fechas; este libro pone los euros y el «si aguantas». '
    'La capacidad del obrador (Parámetros!' + P_CAPDIA + ') es una celda VERDE con '
    'valor por defecto declarado como supuesto (D21): el dato bueno se copia a '
    'mano de la hoja «Cuello de Botella» del libro 1 -480 piezas/día, el abatidor '
    'de 4 bandejas-, sin fórmula entre libros.'
)


# --------------------------------------------------------------------------
# Demostraciones con pycel
# --------------------------------------------------------------------------
def demo(ruta):
    """Prueba con pycel cinco comportamientos del libro."""
    from pycel import ExcelCompiler
    ok, fallos = [], []

    def prueba(nombre, cond, detalle=''):
        (ok if cond else fallos).append(nombre + (' — ' + detalle if detalle
                                                  else ''))

    exc = ExcelCompiler(ruta)

    def v(hoja, coord):
        return exc.evaluate("'%s'!%s" % (hoja, coord))

    # 1. El total de facturación de campañas es la suma de las seis filas.
    filas = [v(H_CAL, 'N%d' % (CAL_INI + i)) for i in range(NP)]
    total = v(H_CAL, 'N%d' % CAL_TOT)
    prueba('el total de facturación de campaña suma las seis filas',
           abs(sum(filas) - total) < 0.01,
           'suma %.2f frente a total %.2f' % (sum(filas), total))

    # 2. Los doce coeficientes reparten el año sin perder ni un euro.
    ventas = v(H_PAR, P_VENTAS)
    suma_meses = v(H_ANO, 'C%d' % MES_TOT)
    prueba('los doce meses suman las ventas del año',
           abs(suma_meses - ventas) < 0.5,
           '%.2f frente a %.2f' % (suma_meses, ventas))

    # 3. El semáforo «¿Aguantas?» no se enciende con texto: si el déficit
    #    llega vacío, la celda devuelve "" y no «No».
    exc2 = ExcelCompiler(ruta)
    exc2.evaluate("'%s'!N%d" % (H_CAP, CAP_INI))
    exc2.set_value("'%s'!%s" % (H_PAR, P_CAPDIA), '')
    n_reyes = exc2.evaluate("'%s'!N%d" % (H_CAP, CAP_INI))
    prueba('sin capacidad tecleada, el veredicto queda vacío y no dice «No»',
           n_reyes in ('', None), 'devuelve %r' % (n_reyes,))

    # 4. El veredicto CAMBIA al cambiar una entrada: con capacidad de sobra,
    #    Reyes pasa de «No» a «Sí».
    antes = v(H_CAP, 'N%d' % CAP_INI)
    exc3 = ExcelCompiler(ruta)
    exc3.evaluate("'%s'!N%d" % (H_CAP, CAP_INI))
    exc3.set_value("'%s'!%s" % (H_PAR, P_CAPDIA), 50000)
    despues = exc3.evaluate("'%s'!N%d" % (H_CAP, CAP_INI))
    prueba('el veredicto de Reyes cambia al subir la capacidad del obrador',
           antes == 'No' and despues == 'Sí',
           'antes %r, después %r' % (antes, despues))

    # 5. El coste hora del refuerzo es el bruto con pagas y SS, no el bruto.
    chora = v(H_PAR, P_CHORA)
    bruto = v(H_PAR, P_BRUTO)
    pagas = v(H_PAR, P_PAGAS)
    ss = v(H_PAR, P_SS)
    hanio = v(H_PAR, P_HANIO)
    prueba('el coste hora del refuerzo lleva pagas y Seguridad Social dentro',
           abs(chora - bruto * pagas * (1 + ss) / hanio) < 0.001
           and chora > bruto * pagas / hanio,
           '%.4f €/h' % chora)

    # 6. La tesorería inmovilizada del año es la suma de las seis campañas.
    k = [v(H_REF, 'K%d' % (REF_INI + i)) for i in range(NP)]
    ktot = v(H_REF, 'K%d' % REF_TOT)
    prueba('la tesorería inmovilizada del año suma las seis campañas',
           abs(sum(k) - ktot) < 0.01, '%.2f' % ktot)

    return ok, fallos


# --------------------------------------------------------------------------
def main():
    D.gate_legal()
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_parametros(wb)
    hoja_calendario(wb)
    hoja_anio(wb)
    hoja_capacidad(wb)
    hoja_refuerzo(wb)

    res = C.cerrar(wb, NOMBRE, TITULO, mapa_celdas(), NOTAS_MAPA)

    print('escrito: %s' % res['ruta'])
    print('hojas: %d · fórmulas: %d · celdas verdes: %d · verdes vacías: %d'
          % (res['hojas'], res['formulas'], res['verdes'],
             len(res['verdes_vacias'])))
    if res['verdes_vacias']:
        print('  VERDES VACÍAS: ' + ', '.join(res['verdes_vacias']))
    print('fórmulas que devuelven «sin dato» a propósito: %d' % res['sin_dato'])
    print('notas legales: %d · etiquetas en el mapa: %d'
          % (res['notas_legales'], res['mapa']))
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
