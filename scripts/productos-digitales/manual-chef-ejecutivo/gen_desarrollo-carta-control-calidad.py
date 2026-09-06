#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_desarrollo-carta-control-calidad.py — libro 5 de «Manual del Chef
Ejecutivo» (SPEC §2.2 fila 5).

Hojas: Instrucciones · Calendario de Temporada · Registro de Pruebas de Plato ·
Control de Calidad del Pase.

QUÉ DECIDE ESTE LIBRO
---------------------
Renovar la carta con método y comprobar que lo que sale por el pase es lo que
dice la ficha. Son las dos mitades del mismo problema: el plato se prueba, se
costea, se documenta, se forma y se lanza (hoja «Calendario de Temporada»), y a
partir de ahí lo único que importa es si el pase lo respeta (hoja «Control de
Calidad del Pase»).

DECISIONES TÉCNICAS
-------------------
* La alerta del calendario cuenta DÍAS NATURALES, nunca `NETWORKDAYS` (que
  además pycel no evalúa): una ficha que lleva 40 días sin cerrar lleva 40 días,
  se abra o no la cocina. El límite es una celda verde (30 días en el ejemplo).
* Fecha de referencia con el patrón de la familia: una celda verde «fecha para
  simular» y, debajo, `IF(simular="",TODAY(),simular)`. `TODAY()` aparece UNA
  sola vez en todo el libro.
* La temperatura de emplatado se registra pero NO enciende ningún semáforo
  automático: `datos_ejemplo.py` no dice qué platos se mantienen en caliente, y
  un umbral de 63 °C aplicado a ciegas marcaría en rojo la ensalada servida a
  9 °C y la torrija a 57 °C, que son filas conformes. El umbral vive en celda
  verde con su nota legal (CE-10) y las dos temperaturas extremas del muestreo
  se calculan, para que el chef lea la columna con criterio.
* Los tres tiempos medios de pase y el % de cumplimiento de ficha son lo que
  alimenta la hoja «Semana» del cuadro de mando de cocina (libro 1). Se copian
  a mano: cero fórmulas entre ficheros (SPEC D4).
* Cero constantes dentro de una fórmula (salvo 0, 1 y los índices de
  INDEX/MATCH), `IFERROR(...,"")` en todo cociente, «sin dato» = `""` nunca 0,
  semáforos con `ISNUMBER`.
* Prohibidas `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA`,
  `RANK`, `NETWORKDAYS` y las referencias a otros ficheros: cero usos.
* Textos 100 % WinAnsi (cp1252): ni un carácter fuera. Nada de flechas ni de
  los signos «mayor o igual» / «menor o igual», que no están en cp1252.

Salida fija: build/desarrollo-carta-control-calidad.xlsx + su mapa de celdas.
"""
import json
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.page import PageMargins
from openpyxl.worksheet.properties import PageSetupProperties

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..'))
sys.path.insert(0, os.path.join(RAIZ, 'guias-v2_0'))
sys.path.insert(0, AQUI)

import motor                                                   # noqa: E402
import datos_ejemplo as D                                      # noqa: E402

motor.CTX['producto'] = 'manual-chef-ejecutivo'

PRODUCTO = 'Manual del Chef Ejecutivo'
SUBTITULO = 'AI Chef Pro · aichef.pro — ' + PRODUCTO
TITULO = 'Desarrollo de carta y control de calidad del pase'
NOMBRE = 'desarrollo-carta-control-calidad'

FMT_EUR = motor.FMT_EUR
FMT_PCT = motor.FMT_PCT
FMT_ENT = motor.FMT_ENT
FMT_FECHA = motor.FMT_FECHA
FMT_DEC = '#,##0.0'

GRIS = 'F2F2F2'
ORO = 'FFD700'
CABECERA = '2D2D2D'

FECHA_VERIF = '06-09-2026'
JSON_SECTOR = os.path.join(RAIZ, 'auditorias', 'guias-v2-research-sector.json')


def sector(idd):
    """Devuelve la entrada `CE-*`/`MM-*` del JSON de research consolidado.

    Regla de familia: ninguna cifra ni norma se teclea en el generador; sale del
    JSON, que lleva fuente, URL y fiabilidad.
    """
    with open(JSON_SECTOR, encoding='utf-8') as fh:
        datos = json.load(fh)['datos']
    for it in datos:
        if it.get('id') == idd:
            return it
    raise KeyError('id de research inexistente: ' + idd)


def verificado(idd):
    """Nota literal de la familia: «Verificado el <fecha> · norma · URL»."""
    it = sector(idd)
    return ('Verificado el ' + FECHA_VERIF + ' · ' + it['fuente_titulo']
            + ' · ' + it['url'])


CE10 = verificado('CE-10')          # temperaturas del art. 30 del RD 1086/2020
CE04 = verificado('CE-04')          # formación por puesto

#: Fecha de referencia con la que se sirve el ejemplo: la de la ÚLTIMA prueba
#: registrada. No es una fecha inventada, sale del juego de datos; y va en la
#: celda verde de simulación para que las cinco filas del calendario enseñen su
#: cuenta de días. Borrando esa celda, el libro vuelve a `TODAY()`.
FECHA_EJEMPLO = max(D._fecha(p[0]) for p in D.PRUEBAS_PLATO)

# --- hoja «Calendario de Temporada» --------------------------------------
C_SIM, C_HOY, C_DIAS = 6, 7, 8
C_CAB, C_INI = 12, 13
C_FIN = C_INI + 12 - 1                                   # 24 (5 platos + 7)
C_RES = 26                                               # sección del resumen
C_RCAB = C_RES + 1                                       # 27
C_R1 = C_RCAB + 1                                        # 28 .. 33

# --- hoja «Registro de Pruebas de Plato» ---------------------------------
P_CAB, P_INI = 5, 6
P_FIN = P_INI + 30 - 1                                   # 35 (8 pruebas + 22)
P_RES = P_FIN + 2                                        # 37
P_RCAB = P_RES + 1                                       # 38
P_R1 = P_RCAB + 1                                        # 39 .. 44

# --- hoja «Control de Calidad del Pase» ----------------------------------
M_CAB, M_INI = 5, 6
M_FIN = M_INI + 40 - 1                                   # 45 (30 muestras +10)
M_RES = M_FIN + 2                                        # 47
M_RCAB = M_RES + 1                                       # 48
M_R1 = M_RCAB + 1                                        # 49

ESTADOS_PLATO = ['Planificado', 'En prueba', 'En curso', 'Lanzado',
                 'Descartado']
SI_NO = ['Sí', 'No']
DECISIONES = ['Repetir', 'Aprobar', 'Descartar']
SERVICIOS = ['Comida', 'Cena']
FAMILIAS = ['Entrantes', 'Principales', 'Postres']

# --- A1 de la refutación xlsx (2026-09-06): bloques de listas al final de
# cada hoja, con las DV apuntando a un RANGO, nunca a una lista con comas.
# Bloque de «Calendario de Temporada» (partidas en celdas verdes, «cópialas
# del libro 1» — D4; los otros dos NO son del caso, son universales).
CL_SEC = C_R1 + 11                                       # 39
CL_PART_CAB = CL_SEC + 1                                 # 40
CL_PART_INI = CL_PART_CAB + 1                            # 41
CL_PART_FIN = CL_PART_INI + len(D.ESTACIONES) - 1        # 46
CL_PART_NOTA = CL_PART_FIN + 1                           # 47
CL_EST_CAB = CL_PART_NOTA + 2                            # 49
CL_EST_INI = CL_EST_CAB + 1                              # 50
CL_EST_FIN = CL_EST_INI + len(ESTADOS_PLATO) - 1         # 54
CL_SI_CAB = CL_EST_FIN + 2                               # 56
CL_SI_INI = CL_SI_CAB + 1                                # 57
CL_SI_FIN = CL_SI_INI + len(SI_NO) - 1                   # 58

# Bloque de «Registro de Pruebas de Plato» (la partida reutiliza el bloque de
# arriba, mismo fichero: D4 no prohíbe la referencia entre HOJAS, sólo entre
# FICHEROS).
PP_SEC = P_R1 + 9                                        # 48
PP_DEC_CAB = PP_SEC + 1                                  # 49
PP_DEC_INI = PP_DEC_CAB + 1                              # 50
PP_DEC_FIN = PP_DEC_INI + len(DECISIONES) - 1            # 52

REF_PARTIDAS_CAL = ("'Calendario de Temporada'!$A$%d:$A$%d"
                    % (CL_PART_INI, CL_PART_FIN))
REF_ESTADOS_PLATO = ("'Calendario de Temporada'!$A$%d:$A$%d"
                     % (CL_EST_INI, CL_EST_FIN))
REF_SI_NO_CAL = "'Calendario de Temporada'!$A$%d:$A$%d" % (CL_SI_INI, CL_SI_FIN)
REF_DECISIONES = ("'Registro de Pruebas de Plato'!$A$%d:$A$%d"
                  % (PP_DEC_INI, PP_DEC_FIN))

# Bloque de «Control de Calidad del Pase» (fila 64 es la última nota tras
# F_TEMP=58; el bloque va después, con margen).
M_LSEC = 67
M_SERV_CAB = 68
M_SERV_INI = 69
M_SERV_FIN = M_SERV_INI + len(SERVICIOS) - 1              # 70
M_FAM_CAB = 72
M_FAM_INI = 73
M_FAM_FIN = M_FAM_INI + len(FAMILIAS) - 1                 # 75
M_SI_CAB = 77
M_SI_INI = 78
M_SI_FIN = M_SI_INI + len(SI_NO) - 1                      # 79

REF_SERVICIOS = ("'Control de Calidad del Pase'!$A$%d:$A$%d"
                 % (M_SERV_INI, M_SERV_FIN))
REF_FAMILIAS = "'Control de Calidad del Pase'!$A$%d:$A$%d" % (M_FAM_INI, M_FAM_FIN)
REF_SI_NO_PASE = "'Control de Calidad del Pase'!$A$%d:$A$%d" % (M_SI_INI, M_SI_FIN)


# --------------------------------------------------------------------------
def cabecera(ws, fila, columnas, altura=44):
    for letra, texto in columnas:
        c = ws[letra + str(fila)]
        c.value = texto
        c.fill = PatternFill('solid', fgColor=CABECERA)
        c.font = Font(bold=True, color='FFFFFF')
        c.alignment = Alignment(horizontal='center', vertical='center',
                                wrap_text=True)
    ws.row_dimensions[fila].height = altura


def seccion(ws, coord, texto):
    motor.val(ws, coord, texto, bold=True)
    ws[coord].font = Font(bold=True, size=12)


def pagina(ws, apaisado=True, titulos=None):
    ws.page_setup.paperSize = 9                      # A4
    ws.page_setup.orientation = 'landscape' if apaisado else 'portrait'
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    if ws.sheet_properties.pageSetUpPr is None:
        ws.sheet_properties.pageSetUpPr = PageSetupProperties()
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins = PageMargins(left=0.59, right=0.59, top=0.59,
                                  bottom=0.59, header=0.3, footer=0.3)
    ws.oddFooter.center.text = 'AI Chef Pro · aichef.pro · Página &P de &N'
    ws.oddFooter.center.size = 8
    if titulos:
        ws.print_title_rows = titulos


def encabezar(ws, titulo, nota=None):
    motor.val(ws, 'A1', titulo)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', SUBTITULO)
    if nota:
        motor.val(ws, 'A3', nota)
        ws['A3'].font = Font(italic=True, size=9)


def anchos(ws, mapa):
    for letra, ancho in mapa.items():
        ws.column_dimensions[letra].width = ancho


def nota(ws, fila, texto, alto=None, col='A', wrap=False):
    motor.val(ws, col + str(fila), texto, wrap=wrap)
    if alto:
        ws.row_dimensions[fila].height = alto


def gris(ws, coord):
    ws[coord].fill = PatternFill('solid', fgColor=GRIS)


def dv_rango(ws, coords, ref, titulo, mensaje):
    """Desplegable contra un RANGO (convención de familia: nunca lista con
    comas). A1 de la refutación xlsx del 2026-09-06."""
    dv = DataValidation(type='list', formula1=ref, allow_blank=True,
                        showErrorMessage=True, errorTitle=titulo,
                        error=mensaje)
    ws.add_data_validation(dv)
    for c in coords:
        dv.add(c)
    return dv


# --------------------------------------------------------------------------
PASOS = [
    '1. Hoja «Calendario de Temporada»: una fila por plato nuevo. Escribe las '
    'cinco fechas de sus cinco hitos (probar, costear, documentar la ficha, '
    'formar a la brigada y lanzar), el estado y si la ficha técnica ya está '
    'cerrada. Lo demás lo calcula el libro.',
    '2. Arriba de esa hoja tienes dos celdas verdes: la fecha para simular '
    '(déjala vacía y el libro usa la de hoy) y los días máximos que aceptas '
    'que un plato esté en prueba sin ficha cerrada. Vienen a 30 días; es un '
    'criterio de la casa, no una cifra de nadie.',
    '3. La columna «Aviso» se enciende sola. Si un plato lleva más días en '
    'prueba de los que has puesto y su ficha sigue abierta, se pone en rojo y '
    'lo dice con palabras. Se cuentan días NATURALES: una ficha que lleva 40 '
    'días sin cerrar lleva 40 días, abra la cocina o no.',
    '4. Hoja «Registro de Pruebas de Plato»: una fila por prueba, con su '
    'resultado de 1 a 5, el coste estimado por ración de esa prueba y la '
    'decisión (repetir, aprobar o descartar). El nombre del plato lo trae solo '
    'desde el calendario en cuanto escribes el id.',
    '5. Las cinco últimas columnas del calendario resumen ese registro plato a '
    'plato: cuántas pruebas lleva, qué nota media saca, cuánto cuesta de media '
    'la ración, cuántas veces se aprobó y cuántas se descartó. No hay que '
    'escribir nada ahí.',
    '6. El coste por ración de la prueba es ESTIMADO y sirve para descartar '
    'pronto lo que no cabe en la carta. El coste bueno sale de tu escandallo '
    '(Kit de Escandallos o Guía Food Cost + Ingeniería de Menú) y es el que se '
    'copia a la ficha técnica de proceso, en el libro 3 de este pack.',
    '7. Hoja «Control de Calidad del Pase»: muestrea el servicio. Una fila por '
    'plato muestreado, con la hora, la familia, la temperatura de emplatado, '
    'los minutos entre comanda y salida, si salió conforme a la ficha y si el '
    'cliente lo devolvió.',
    '8. Al final de esa hoja tienes los objetivos de la casa en celdas verdes '
    '(tiempo de pase por familia y % de cumplimiento de ficha) y el resumen '
    'del muestreo al lado. Mientras un objetivo esté vacío su semáforo no se '
    'enciende: es a propósito.',
    '9. Los tres tiempos medios de pase y el porcentaje de cumplimiento de '
    'ficha son los que se copian a la hoja «Semana» del cuadro de mando de '
    'cocina (libro 1 de este pack). Se copian a mano: en este pack no hay ni '
    'una fórmula que salte de un fichero a otro.',
    '10. Cadencia: el calendario de temporada se abre y se revisa AL ABRIR '
    'TEMPORADA, cada vez que cambias la carta; el registro de pruebas, cada '
    'vez que pruebas un plato nuevo; el control de calidad del pase, con un '
    'muestreo SEMANAL del servicio.',
]

NOTAS_LIBRO = [
    'ESTE LIBRO NO HACE INGENIERÍA DE MENÚ. Aquí se decide si el plato está '
    'listo para entrar en carta y si el pase lo respeta. Qué plato deja más '
    'margen, cuál es vaca y cuál perro, y qué se retira de la carta se decide '
    'en la «Guía Food Cost + Ingeniería de Menú», que es otro producto.',
    'Los cinco hitos son a propósito los mismos siempre: probar, costear, '
    'documentar, formar y lanzar. El que casi todo el mundo se salta es '
    '«formar»: un plato lanzado sin que la partida sepa hacerlo vuelve al pase '
    'en forma de tiempo y de devoluciones, que es justo lo que mide la tercera '
    'hoja.',
    'El plato de ejemplo que dispara la alerta lleva desde julio en prueba, '
    'tres pruebas hechas, dos repeticiones y un descarte final. Es el caso '
    'normal: no se rompe nada, simplemente el plato se queda a medias y nadie '
    'lo cierra hasta que alguien lo mira escrito.',
    'La temperatura de emplatado se registra pero el libro NO la puntúa solo. '
    'El motivo es honesto: el mantenimiento en caliente obliga a partir de '
    '63 °C, pero una ensalada se sirve a 9 °C y una torrija templada a 57 °C '
    'sin incumplir nada. Quien decide qué elaboración se mantiene en caliente '
    'es la ficha de cada plato, no una fórmula. ' + CE10,
    'Los objetivos de tiempo de pase y de cumplimiento de ficha son de la casa '
    'y van en celdas verdes. No existe un estándar publicado de tiempos de '
    'pase en español, así que aquí no se cita ninguno: se miden los tuyos y se '
    'comparan contigo mismo semana a semana.',
    'Formar a la brigada en el plato nuevo antes de lanzarlo no es solo '
    'sentido común: la formación en higiene tiene que darse por puesto y '
    'según la actividad de cada uno. ' + CE04,
]


def hoja_instrucciones(wb):
    ws = wb.create_sheet('Instrucciones', 0)
    anchos(ws, {'A': 110.0})
    motor.val(ws, 'A1', TITULO)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', SUBTITULO)
    motor.val(ws, 'A3', 'Para qué sirve: meter un plato en carta con método, y '
                        'comprobar que lo que sale por el pase es lo que dice '
                        'su ficha.')
    ws['A3'].font = Font(italic=True, size=9)

    seccion(ws, 'A5', 'Instrucciones de uso')
    fila = 6
    for paso in PASOS:
        nota(ws, fila, paso, alto=44, wrap=True)
        fila += 1
    fila += 1
    motor.val(ws, 'A' + str(fila), motor.NOTA_VERDES)
    ws['A' + str(fila)].fill = PatternFill('solid', fgColor=motor.VERDE)
    fila += 2
    seccion(ws, 'A' + str(fila), 'Lo que conviene saber antes de empezar')
    fila += 1
    for texto in NOTAS_LIBRO:
        nota(ws, fila, texto, alto=58, wrap=True)
        fila += 1
    fila += 1
    motor.val(ws, 'A' + str(fila), D.NOTA_DESPROTEGER)
    fila += 1
    motor.val(ws, 'A' + str(fila),
              'Ruta en Excel: Revisar > Desproteger hoja. La protección no '
              'tiene contraseña; sirve para no pisar una fórmula sin querer.')
    fila += 2
    motor.val(ws, 'A' + str(fila), D.BIO)
    fila += 1
    motor.val(ws, 'A' + str(fila), D.VERSION_LINE)
    pagina(ws, apaisado=False)
    return ws


# --------------------------------------------------------------------------
COLS_CAL = [
    ('A', 'Id', 'txt'),
    ('B', 'Plato', 'txt'),
    ('C', 'Partida', 'txt'),
    ('D', 'Probar (fecha)', 'fecha'),
    ('E', 'Costear (fecha)', 'fecha'),
    ('F', 'Documentar la ficha (fecha)', 'fecha'),
    ('G', 'Formar a la brigada (fecha)', 'fecha'),
    ('H', 'Lanzar (fecha)', 'fecha'),
    ('I', 'Estado', 'txt'),
    ('J', 'Ficha técnica cerrada', 'txt'),
    ('K', 'Días naturales desde la primera prueba', 'ent'),
    ('L', 'Hitos con fecha puesta (de 5)', 'ent'),
    ('M', 'Aviso', 'txt'),
    ('N', 'Pruebas hechas', 'ent'),
    ('O', 'Resultado medio (1-5)', 'dec'),
    ('P', 'Coste medio estimado por ración', 'eur'),
    ('Q', 'Veces aprobado', 'ent'),
    ('R', 'Veces descartado', 'ent'),
]

AVISO_ROJO = 'REVISAR: demasiados días en prueba sin ficha cerrada'
AVISO_AMBAR = 'Ficha pendiente'
AVISO_VERDE = 'Ficha cerrada'

PR = "'Registro de Pruebas de Plato'"


def hoja_calendario(wb):
    ws = wb.create_sheet('Calendario de Temporada')
    encabezar(ws, 'Calendario de temporada: de la prueba a la carta',
              nota='Cinco hitos por plato. La columna «Aviso» se enciende sola '
                   'cuando un plato lleva demasiado tiempo en prueba con la '
                   'ficha abierta.')
    anchos(ws, {'A': 8, 'B': 52, 'C': 21, 'D': 13, 'E': 13, 'F': 15, 'G': 15,
                'H': 13, 'I': 14, 'J': 14, 'K': 15, 'L': 14, 'M': 46,
                'N': 12, 'O': 13, 'P': 17, 'Q': 12, 'R': 13})

    seccion(ws, 'B5', 'PARÁMETROS DE ESTA HOJA')
    motor.val(ws, 'B%d' % C_SIM,
              'Fecha para simular (déjala vacía y se usa la de hoy)')
    motor.val(ws, 'C%d' % C_SIM, FECHA_EJEMPLO, fmt=FMT_FECHA, verde_=True)
    motor.dv_fecha(ws, ['C%d' % C_SIM])
    motor.val(ws, 'D%d' % C_SIM,
              'En el ejemplo trae la fecha de la última prueba registrada, '
              'para que se vea el cálculo. Bórrala y el libro usará la de hoy.')

    motor.val(ws, 'B%d' % C_HOY, 'Hoy (fecha de referencia)', bold=True)
    motor.f(ws, 'C%d' % C_HOY,
            '=IFERROR(IF($C${s}="",TODAY(),$C${s}),"")'.format(s=C_SIM),
            fmt=FMT_FECHA, bold=True)
    gris(ws, 'C%d' % C_HOY)

    motor.val(ws, 'B%d' % C_DIAS,
              'Días máximos en prueba sin ficha técnica cerrada')
    motor.val(ws, 'C%d' % C_DIAS,
              float(D.PARAMETROS_COCINA['dias_max_en_prueba_sin_ficha']),
              fmt=FMT_ENT, verde_=True)
    motor.dv_numerica(ws, ['C%d' % C_DIAS], minimo=1, maximo=365,
                      titulo='Días máximos',
                      mensaje='Escribe un número de días entre 1 y 365.')
    motor.val(ws, 'D%d' % C_DIAS,
              'Criterio de la casa, no una cifra publicada por nadie. Son días '
              'NATURALES: no se descuentan los cierres ni los festivos.')

    nota(ws, 10,
         'Los cinco hitos son: ' + ', '.join(D.HITOS_TEMPORADA).lower()
         + '. El que más se salta es «formar»: un plato que llega al pase sin '
           'que la partida sepa hacerlo se paga en tiempo y en devoluciones.',
         col='B')

    cabecera(ws, C_CAB, [(c, t) for c, t, _ in COLS_CAL], altura=62)

    for i, fila in enumerate(D.CALENDARIO_TEMPORADA):
        r = C_INI + i
        (idp, plato, partida, f_pro, f_cos, f_doc, f_for, f_lan,
         estado, ficha) = fila
        motor.val(ws, 'A%d' % r, idp, verde_=True)
        motor.val(ws, 'B%d' % r, plato, verde_=True, wrap=True)
        motor.val(ws, 'C%d' % r, partida, verde_=True)
        for letra, texto in (('D', f_pro), ('E', f_cos), ('F', f_doc),
                             ('G', f_for), ('H', f_lan)):
            motor.val(ws, '%s%d' % (letra, r),
                      D._fecha(texto) if texto else None,
                      fmt=FMT_FECHA, verde_=True)
        motor.val(ws, 'I%d' % r, estado, verde_=True)
        motor.val(ws, 'J%d' % r, ficha, verde_=True)
        ws.row_dimensions[r].height = 30

    for r in range(C_INI, C_FIN + 1):
        # las filas sin datos también son editables: el libro es una plantilla
        motor.verde(ws, 'A%d:J%d' % (r, r))
        motor.f(ws, 'K%d' % r,
                '=IFERROR(IF(OR($D{r}="",$C${h}=""),"",'
                'IF($C${h}<$D{r},"",$C${h}-$D{r})),"")'.format(r=r, h=C_HOY),
                fmt=FMT_ENT, align='center')
        motor.f(ws, 'L%d' % r, '=COUNT($D{r}:$H{r})'.format(r=r),
                fmt=FMT_ENT, align='center')
        # A7 de la refutación xlsx (2026-09-06): comparar contra la CELDA de
        # la lista ($A$58 = «No»), no contra el literal.
        motor.f(ws, 'M%d' % r,
                '=IF($J{r}="","",IF(AND($J{r}=$A${no},ISNUMBER($K{r}),'
                'ISNUMBER($C${d}),$K{r}>$C${d}),"{rojo}",'
                'IF($J{r}=$A${no},"{ambar}","{verde}")))'
                .format(r=r, d=C_DIAS, no=CL_SI_INI + 1, rojo=AVISO_ROJO,
                        ambar=AVISO_AMBAR, verde=AVISO_VERDE), align='left')
        motor.f(ws, 'N%d' % r,
                '=IF($A{r}="","",COUNTIF({p}!$B${a}:$B${b},$A{r}&""))'
                .format(r=r, p=PR, a=P_INI, b=P_FIN), fmt=FMT_ENT,
                align='center')
        motor.f(ws, 'O%d' % r,
                '=IFERROR(IF(OR($N{r}="",$N{r}=0),"",'
                'SUMIF({p}!$B${a}:$B${b},$A{r}&"",{p}!$F${a}:$F${b})/$N{r}),"")'
                .format(r=r, p=PR, a=P_INI, b=P_FIN), fmt=FMT_DEC)
        motor.f(ws, 'P%d' % r,
                '=IFERROR(IF(OR($N{r}="",$N{r}=0),"",'
                'SUMIF({p}!$B${a}:$B${b},$A{r}&"",{p}!$G${a}:$G${b})/$N{r}),"")'
                .format(r=r, p=PR, a=P_INI, b=P_FIN), fmt=FMT_EUR)
        motor.f(ws, 'Q%d' % r,
                '=IF($A{r}="","",SUMIF({p}!$B${a}:$B${b},$A{r}&"",'
                '{p}!$J${a}:$J${b}))'.format(r=r, p=PR, a=P_INI, b=P_FIN),
                fmt=FMT_ENT, align='center')
        motor.f(ws, 'R%d' % r,
                '=IF($A{r}="","",SUMIF({p}!$B${a}:$B${b},$A{r}&"",'
                '{p}!$K${a}:$K${b}))'.format(r=r, p=PR, a=P_INI, b=P_FIN),
                fmt=FMT_ENT, align='center')

    filas = list(range(C_INI, C_FIN + 1))
    dv_rango(ws, ['I%d' % r for r in filas], REF_ESTADOS_PLATO,
             'Estado del plato',
             'Elige un estado de la lista del final de esta hoja.')
    dv_rango(ws, ['J%d' % r for r in filas], REF_SI_NO_CAL, 'Ficha cerrada',
             'Elige Sí o No de la lista del final de esta hoja.')
    dv_rango(ws, ['C%d' % r for r in filas], REF_PARTIDAS_CAL, 'Partida',
             'Elige una partida de la lista del final de esta hoja.')
    motor.dv_fecha(ws, ['%s%d' % (c, r) for c in 'DEFGH' for r in filas])

    motor.semaforo_texto(ws, 'M{a}:M{b}'.format(a=C_INI, b=C_FIN),
                         ((AVISO_ROJO, motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          (AVISO_AMBAR, motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          (AVISO_VERDE, motor.CF_VERDE_BG,
                           motor.CF_VERDE_FG)))
    motor.regla_expresion(
        ws, 'K{a}:K{b}'.format(a=C_INI, b=C_FIN),
        '=AND(ISNUMBER($K{a}),ISNUMBER($C${d}),$K{a}>$C${d},$J{a}="No")'
        .format(a=C_INI, d=C_DIAS))

    # --- resumen ---------------------------------------------------------
    seccion(ws, 'B%d' % C_RES, 'RESUMEN DEL DESARROLLO DE CARTA')
    cabecera(ws, C_RCAB, [('B', 'Indicador'), ('C', 'Valor')], altura=20)
    resumen = [
        ('Platos en desarrollo',
         '=COUNTIF($A${a}:$A${b},"<>")'.format(a=C_INI, b=C_FIN), FMT_ENT),
        ('Platos con ficha técnica cerrada',
         '=COUNTIF($J${a}:$J${b},"Sí")'.format(a=C_INI, b=C_FIN), FMT_ENT),
        ('Porcentaje de platos con ficha cerrada',
         '=IFERROR(IF($C${p}=0,"",$C${q}/$C${p}),"")'
         .format(p=C_R1, q=C_R1 + 1), FMT_PCT),
        ('Platos que superan los días máximos en prueba',
         '=COUNTIFS($J${a}:$J${b},"No",$K${a}:$K${b},">"&$C${d})'
         .format(a=C_INI, b=C_FIN, d=C_DIAS), FMT_ENT),
        ('Platos ya lanzados',
         '=COUNTIF($I${a}:$I${b},"Lanzado")'.format(a=C_INI, b=C_FIN),
         FMT_ENT),
        ('Pruebas registradas en total',
         '=SUM($N${a}:$N${b})'.format(a=C_INI, b=C_FIN), FMT_ENT),
    ]
    for i, (etiqueta, formula, fmt) in enumerate(resumen):
        r = C_R1 + i
        motor.val(ws, 'B%d' % r, etiqueta)
        motor.f(ws, 'C%d' % r, formula, fmt=fmt, bold=True)
        gris(ws, 'C%d' % r)
    motor.semaforo_isnumber(ws, 'C%d' % (C_R1 + 3), '$C$%d' % (C_R1 + 3),
                            operador='>', umbral='0')

    nota(ws, C_R1 + 7,
         'La columna «Coste medio estimado por ración» es de las PRUEBAS: '
         'sirve para descartar pronto un plato que no cabe en la carta. El '
         'coste bueno sale del escandallo y es el que se copia a la ficha '
         'técnica de proceso (libro 3). Este pack no lo recalcula.', col='B')
    nota(ws, C_R1 + 8,
         'Qué plato deja más margen y cuál sale de la carta es ingeniería de '
         'menú, y vive en la «Guía Food Cost + Ingeniería de Menú». Aquí solo '
         'se decide si el plato está listo.', col='B')

    # --- listas de los desplegables (A1 de la refutación xlsx) ------------
    seccion(ws, 'B%d' % CL_SEC, 'LISTAS DE LOS DESPLEGABLES (no las borres)')
    cabecera(ws, CL_PART_CAB, [('A', 'Partidas de tu cocina')], altura=20)
    for i, partida in enumerate(D.ESTACIONES):
        motor.val(ws, 'A%d' % (CL_PART_INI + i), partida, verde_=True)
    nota(ws, CL_PART_NOTA,
         'Son las mismas partidas del cuadro de mando de cocina (libro 1). '
         'Cópialas de allí: este libro no lee ningún fichero ajeno.')
    cabecera(ws, CL_EST_CAB, [('A', 'Estado del plato')], altura=20)
    for i, estado in enumerate(ESTADOS_PLATO):
        motor.val(ws, 'A%d' % (CL_EST_INI + i), estado)
    cabecera(ws, CL_SI_CAB, [('A', 'Ficha técnica cerrada')], altura=20)
    for i, texto in enumerate(SI_NO):
        motor.val(ws, 'A%d' % (CL_SI_INI + i), texto)

    ws.freeze_panes = 'C%d' % C_INI
    pagina(ws, titulos='$%d:$%d' % (C_CAB, C_CAB))
    return ws


# --------------------------------------------------------------------------
COLS_PRUEBAS = [
    ('A', 'Fecha', 'fecha'),
    ('B', 'Id del plato', 'txt'),
    ('C', 'Plato (lo trae el calendario)', 'txt'),
    ('D', 'Número de prueba', 'ent'),
    ('E', 'Partida', 'txt'),
    ('F', 'Resultado (1 a 5)', 'ent'),
    ('G', 'Coste estimado por ración', 'eur'),
    ('H', 'Decisión', 'txt'),
    ('I', 'Observación', 'txt'),
    ('J', 'Aprobada (1 o 0)', 'ent'),
    ('K', 'Descartada (1 o 0)', 'ent'),
]

CAL = "'Calendario de Temporada'"


def hoja_pruebas(wb):
    ws = wb.create_sheet('Registro de Pruebas de Plato')
    encabezar(ws, 'Registro de pruebas de plato',
              nota='Una fila por prueba. El nombre del plato lo trae el '
                   'calendario en cuanto escribes su id.')
    anchos(ws, {'A': 13, 'B': 12, 'C': 50, 'D': 12, 'E': 21, 'F': 12,
                'G': 16, 'H': 14, 'I': 58, 'J': 12, 'K': 12})
    cabecera(ws, P_CAB, [(c, t) for c, t, _ in COLS_PRUEBAS], altura=48)

    for i, fila in enumerate(D.PRUEBAS_PLATO):
        r = P_INI + i
        fecha, idp, num, partida, res, coste, obs, decision = fila
        motor.val(ws, 'A%d' % r, D._fecha(fecha), fmt=FMT_FECHA, verde_=True)
        motor.val(ws, 'B%d' % r, idp, verde_=True)
        motor.val(ws, 'D%d' % r, num, fmt=FMT_ENT, verde_=True)
        motor.val(ws, 'E%d' % r, partida, verde_=True)
        motor.val(ws, 'F%d' % r, res, fmt=FMT_ENT, verde_=True)
        motor.val(ws, 'G%d' % r, float(coste), fmt=FMT_EUR, verde_=True)
        motor.val(ws, 'I%d' % r, obs, verde_=True, wrap=True)
        motor.val(ws, 'H%d' % r, decision, verde_=True)
        ws.row_dimensions[r].height = 28

    for r in range(P_INI, P_FIN + 1):
        motor.verde(ws, 'A%d:B%d' % (r, r))
        motor.verde(ws, 'D%d:I%d' % (r, r))
        motor.f(ws, 'C%d' % r,
                '=IFERROR(IF($B{r}="","",INDEX({c}!$B${a}:$B${b},'
                'MATCH($B{r}&"",{c}!$A${a}:$A${b},0))),"")'
                .format(r=r, c=CAL, a=C_INI, b=C_FIN), align='left')
        motor.f(ws, 'J%d' % r,
                '=IF($H{r}="","",IF($H{r}="Aprobar",1,0))'.format(r=r),
                fmt=FMT_ENT, align='center')
        motor.f(ws, 'K%d' % r,
                '=IF($H{r}="","",IF($H{r}="Descartar",1,0))'.format(r=r),
                fmt=FMT_ENT, align='center')

    filas = list(range(P_INI, P_FIN + 1))
    motor.dv_fecha(ws, ['A%d' % r for r in filas])
    dv_rango(ws, ['E%d' % r for r in filas], REF_PARTIDAS_CAL, 'Partida',
             'Elige una partida de la lista del final de la hoja «Calendario '
             'de Temporada».')
    dv_rango(ws, ['H%d' % r for r in filas], REF_DECISIONES, 'Decisión',
             'Elige una decisión de la lista del final de esta hoja.')
    motor.dv_numerica(ws, ['F%d' % r for r in filas], minimo=1, maximo=5,
                      titulo='Resultado',
                      mensaje='Puntúa la prueba de 1 a 5.')
    motor.dv_numerica(ws, ['D%d' % r for r in filas], minimo=1, maximo=99,
                      titulo='Número de prueba')
    motor.dv_numerica(ws, ['G%d' % r for r in filas], minimo=0,
                      titulo='Importe (€)')

    motor.semaforo_texto(ws, 'H{a}:H{b}'.format(a=P_INI, b=P_FIN),
                         (('Aprobar', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                          ('Repetir', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          ('Descartar', motor.CF_ROJO_BG, motor.CF_ROJO_FG)))

    seccion(ws, 'A%d' % P_RES, 'RESUMEN DEL REGISTRO')
    cabecera(ws, P_RCAB, [('A', 'Indicador'), ('B', 'Valor')], altura=20)
    ws.merge_cells('A%d:B%d' % (P_RCAB, P_RCAB))
    resumen = [
        ('Pruebas registradas',
         '=COUNTIF($B${a}:$B${b},"<>")'.format(a=P_INI, b=P_FIN), FMT_ENT),
        ('Resultado medio de todas las pruebas (1 a 5)',
         '=IFERROR(IF(COUNT($F${a}:$F${b})=0,"",SUM($F${a}:$F${b})'
         '/COUNT($F${a}:$F${b})),"")'.format(a=P_INI, b=P_FIN), FMT_DEC),
        ('Coste estimado medio por ración',
         '=IFERROR(IF(COUNT($G${a}:$G${b})=0,"",SUM($G${a}:$G${b})'
         '/COUNT($G${a}:$G${b})),"")'.format(a=P_INI, b=P_FIN), FMT_EUR),
        ('Pruebas aprobadas', '=SUM($J${a}:$J${b})'.format(a=P_INI, b=P_FIN),
         FMT_ENT),
        ('Pruebas descartadas',
         '=SUM($K${a}:$K${b})'.format(a=P_INI, b=P_FIN), FMT_ENT),
        ('Pruebas que hubo que repetir',
         '=COUNTIF($H${a}:$H${b},"Repetir")'.format(a=P_INI, b=P_FIN),
         FMT_ENT),
    ]
    for i, (etiqueta, formula, fmt) in enumerate(resumen):
        r = P_R1 + i
        motor.val(ws, 'A%d' % r, etiqueta)
        ws.merge_cells('A%d:B%d' % (r, r))
        motor.f(ws, 'C%d' % r, formula, fmt=fmt, bold=True)
        gris(ws, 'C%d' % r)

    nota(ws, P_R1 + 7,
         'Las columnas «Aprobada» y «Descartada» valen 1 o 0 y están para que '
         'el calendario pueda contarlas por plato sin fórmulas raras. No hay '
         'que tocarlas.')

    # --- lista del desplegable de decisión (A1 de la refutación xlsx) ------
    seccion(ws, 'A%d' % PP_SEC, 'LISTA DEL DESPLEGABLE (no la borres)')
    cabecera(ws, PP_DEC_CAB, [('A', 'Decisión')], altura=20)
    for i, texto in enumerate(DECISIONES):
        motor.val(ws, 'A%d' % (PP_DEC_INI + i), texto)

    ws.freeze_panes = 'C%d' % P_INI
    pagina(ws, titulos='$%d:$%d' % (P_CAB, P_CAB))
    return ws


# --------------------------------------------------------------------------
COLS_PASE = [
    ('A', 'Fecha', 'fecha'),
    ('B', 'Servicio', 'txt'),
    ('C', 'Id del plato', 'txt'),
    ('D', 'Familia', 'txt'),
    ('E', 'Temperatura de emplatado (°C)', 'ent'),
    ('F', 'Tiempo de pase (min)', 'dec'),
    ('G', 'Conforme a la ficha', 'txt'),
    ('H', 'Devuelto por el cliente', 'txt'),
    ('I', 'Observación', 'txt'),
    ('J', 'Conforme (1 o 0)', 'ent'),
    ('K', 'Devuelto (1 o 0)', 'ent'),
    ('L', '¿Se mantiene en caliente? (Sí/No)', 'txt'),
]

#: (etiqueta del objetivo, clave en PARAMETROS_COCINA['objetivos'], familia)
OBJETIVOS_PASE = [
    ('Tiempo de pase objetivo en entrantes (min)', 'pase_entrantes_min',
     'Entrantes'),
    ('Tiempo de pase objetivo en principales (min)', 'pase_principales_min',
     'Principales'),
    ('Tiempo de pase objetivo en postres (min)', 'pase_postres_min',
     'Postres'),
]

LECTURA_OK = 'En objetivo'
LECTURA_MAL = 'Por encima del objetivo'


def hoja_pase(wb):
    ws = wb.create_sheet('Control de Calidad del Pase')
    encabezar(ws, 'Control de calidad del pase',
              nota='Muestreo del servicio. De aquí salen los tiempos de pase y '
                   'el cumplimiento de ficha que se copian al cuadro de mando '
                   'de cocina.')
    anchos(ws, {'A': 13, 'B': 12, 'C': 12, 'D': 16, 'E': 17, 'F': 15,
                'G': 16, 'H': 16, 'I': 52, 'J': 12, 'K': 12, 'L': 20})
    cabecera(ws, M_CAB, [(c, t) for c, t, _ in COLS_PASE], altura=52)

    for i, fila in enumerate(D.CONTROL_PASE):
        r = M_INI + i
        (fecha, servicio, idp, familia, temp, tiempo, conforme, dev, obs,
         caliente) = fila
        motor.val(ws, 'A%d' % r, D._fecha(fecha), fmt=FMT_FECHA, verde_=True)
        motor.val(ws, 'B%d' % r, servicio, verde_=True)
        motor.val(ws, 'C%d' % r, idp, verde_=True)
        motor.val(ws, 'D%d' % r, familia, verde_=True)
        motor.val(ws, 'E%d' % r, temp, fmt=FMT_ENT, verde_=True)
        motor.val(ws, 'F%d' % r, float(tiempo), fmt=FMT_DEC, verde_=True)
        motor.val(ws, 'G%d' % r, conforme, verde_=True)
        motor.val(ws, 'H%d' % r, dev, verde_=True)
        if obs:
            motor.val(ws, 'I%d' % r, obs, verde_=True, wrap=True)
        motor.val(ws, 'L%d' % r, caliente, verde_=True)

    for r in range(M_INI, M_FIN + 1):
        motor.verde(ws, 'A%d:I%d' % (r, r))
        motor.verde(ws, 'L%d' % r)
        # A7 de la refutación xlsx (2026-09-06): comparar contra la CELDA de
        # la lista ($A$78 = «Sí»), no contra el literal.
        motor.f(ws, 'J%d' % r,
                '=IF($G{r}="","",IF($G{r}=$A${si},1,0))'
                .format(r=r, si=M_SI_INI), fmt=FMT_ENT, align='center')
        motor.f(ws, 'K%d' % r,
                '=IF($H{r}="","",IF($H{r}=$A${si},1,0))'
                .format(r=r, si=M_SI_INI), fmt=FMT_ENT, align='center')

    filas = list(range(M_INI, M_FIN + 1))
    motor.dv_fecha(ws, ['A%d' % r for r in filas])
    dv_rango(ws, ['B%d' % r for r in filas], REF_SERVICIOS, 'Servicio',
             'Elige un servicio de la lista del final de esta hoja.')
    dv_rango(ws, ['D%d' % r for r in filas], REF_FAMILIAS, 'Familia',
             'Elige una familia de la lista del final de esta hoja.')
    dv_rango(ws, ['G%d' % r for r in filas], REF_SI_NO_PASE,
             'Conforme a la ficha',
             'Elige Sí o No de la lista del final de esta hoja.')
    dv_rango(ws, ['H%d' % r for r in filas], REF_SI_NO_PASE, 'Devuelto',
             'Elige Sí o No de la lista del final de esta hoja.')
    dv_rango(ws, ['L%d' % r for r in filas], REF_SI_NO_PASE,
             '¿Se mantiene en caliente?',
             'Elige Sí o No de la lista del final de esta hoja.')
    motor.dv_numerica(ws, ['E%d' % r for r in filas], minimo=-30, maximo=120,
                      titulo='Temperatura (°C)',
                      mensaje='Escribe la temperatura en grados centígrados, '
                              'entre -30 y 120.')
    motor.dv_numerica(ws, ['F%d' % r for r in filas], minimo=0, maximo=240,
                      titulo='Minutos de pase')

    motor.semaforo_texto(ws, 'G{a}:G{b}'.format(a=M_INI, b=M_FIN),
                         (('Sí', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                          ('No', motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    motor.semaforo_texto(ws, 'H{a}:H{b}'.format(a=M_INI, b=M_FIN),
                         (('Sí', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('No', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))

    # --- resumen y objetivos ---------------------------------------------
    seccion(ws, 'A%d' % M_RES,
            'RESUMEN DEL MUESTREO Y OBJETIVOS DE LA CASA')
    cabecera(ws, M_RCAB, [('A', 'Indicador'), ('D', 'Medido'),
                          ('E', 'Objetivo de la casa'), ('F', 'Lectura'),
                          ('H', 'Muestreos de la familia')], altura=32)
    for letra in 'BCG':
        ws[letra + str(M_RCAB)].fill = PatternFill('solid', fgColor=CABECERA)
    ws.merge_cells('A%d:C%d' % (M_RCAB, M_RCAB))

    r = M_R1
    obj_filas = {}
    for etiqueta, clave, familia in OBJETIVOS_PASE:
        motor.val(ws, 'A%d' % r, 'Tiempo medio de pase - ' + familia + ' (min)')
        ws.merge_cells('A%d:C%d' % (r, r))
        motor.f(ws, 'D%d' % r,
                '=IFERROR(IF(COUNTIF($D${a}:$D${b},"{f}")=0,"",'
                'SUMIF($D${a}:$D${b},"{f}",$F${a}:$F${b})'
                '/COUNTIF($D${a}:$D${b},"{f}")),"")'
                .format(a=M_INI, b=M_FIN, f=familia), fmt=FMT_DEC, bold=True)
        gris(ws, 'D%d' % r)
        motor.val(ws, 'E%d' % r,
                  float(D.PARAMETROS_COCINA['objetivos'][clave]), fmt=FMT_DEC,
                  verde_=True)
        motor.f(ws, 'F%d' % r,
                '=IF(OR(NOT(ISNUMBER($D{r})),NOT(ISNUMBER($E{r}))),"",'
                'IF($D{r}<=$E{r},"{ok}","{mal}"))'
                .format(r=r, ok=LECTURA_OK, mal=LECTURA_MAL))
        motor.f(ws, 'H%d' % r,
                '=COUNTIF($D${a}:$D${b},"{f}")'.format(a=M_INI, b=M_FIN,
                                                       f=familia),
                fmt=FMT_ENT)
        gris(ws, 'H%d' % r)
        obj_filas[familia] = r
        r += 1

    F_CUMP = r
    motor.val(ws, 'A%d' % r, 'Cumplimiento de ficha técnica en el pase')
    ws.merge_cells('A%d:C%d' % (r, r))
    motor.f(ws, 'D%d' % r,
            '=IFERROR(IF(COUNT($J${a}:$J${b})=0,"",SUM($J${a}:$J${b})'
            '/COUNT($J${a}:$J${b})),"")'.format(a=M_INI, b=M_FIN),
            fmt=FMT_PCT, bold=True)
    gris(ws, 'D%d' % r)
    motor.val(ws, 'E%d' % r,
              float(D.PARAMETROS_COCINA['objetivos']['cumplimiento_ficha']),
              fmt=FMT_PCT, verde_=True)
    motor.f(ws, 'F%d' % r,
            '=IF(OR(NOT(ISNUMBER($D{r})),NOT(ISNUMBER($E{r}))),"",'
            'IF($D{r}>=$E{r},"{ok}","{mal}"))'
            .format(r=r, ok=LECTURA_OK, mal='Por debajo del objetivo'))
    r += 1

    otros = [
        ('Muestreos hechos',
         '=COUNT($F${a}:$F${b})'.format(a=M_INI, b=M_FIN), FMT_ENT),
        ('Muestreos NO conformes con la ficha',
         '=COUNTIF($G${a}:$G${b},"No")'.format(a=M_INI, b=M_FIN), FMT_ENT),
        ('Platos devueltos por el cliente',
         '=COUNTIF($H${a}:$H${b},"Sí")'.format(a=M_INI, b=M_FIN), FMT_ENT),
        ('Temperatura de emplatado más baja del muestreo (°C)',
         '=IFERROR(IF(COUNT($E${a}:$E${b})=0,"",MIN($E${a}:$E${b})),"")'
         .format(a=M_INI, b=M_FIN), FMT_ENT),
        ('Temperatura de emplatado más alta del muestreo (°C)',
         '=IFERROR(IF(COUNT($E${a}:$E${b})=0,"",MAX($E${a}:$E${b})),"")'
         .format(a=M_INI, b=M_FIN), FMT_ENT),
    ]
    F_OTROS = r
    for etiqueta, formula, fmt in otros:
        motor.val(ws, 'A%d' % r, etiqueta)
        ws.merge_cells('A%d:C%d' % (r, r))
        motor.f(ws, 'D%d' % r, formula, fmt=fmt, bold=True)
        gris(ws, 'D%d' % r)
        r += 1

    F_TEMP = r
    motor.val(ws, 'A%d' % r,
              'Temperatura mínima de mantenimiento en caliente (°C)')
    ws.merge_cells('A%d:C%d' % (r, r))
    motor.val(ws, 'D%d' % r, 63, fmt=FMT_ENT, verde_=True)
    r += 1

    # --- B6 de la refutación xlsx: el muestreo no distinguía qué se mantiene
    # en caliente, así que el mínimo de temperatura no se podía puntuar bien.
    F_CALIENTE = r
    motor.val(ws, 'A%d' % r,
              'Muestras de elaboraciones que se mantienen en caliente')
    ws.merge_cells('A%d:C%d' % (r, r))
    motor.f(ws, 'D%d' % r,
            '=COUNTIF($L${a}:$L${b},"Sí")'.format(a=M_INI, b=M_FIN),
            fmt=FMT_ENT, bold=True)
    gris(ws, 'D%d' % r)
    r += 1
    F_CALIENTE_MAL = r
    motor.val(ws, 'A%d' % r,
              'De ellas, por debajo del mínimo de D%d' % F_TEMP)
    ws.merge_cells('A%d:C%d' % (r, r))
    motor.f(ws, 'D%d' % r,
            '=COUNTIFS($L${a}:$L${b},"Sí",$E${a}:$E${b},"<"&$D${t})'
            .format(a=M_INI, b=M_FIN, t=F_TEMP),
            fmt=FMT_ENT, bold=True)
    gris(ws, 'D%d' % r)
    r += 1
    motor.semaforo_isnumber(ws, 'D%d' % F_CALIENTE_MAL,
                            '$D$%d' % F_CALIENTE_MAL, operador='>',
                            umbral='0')

    nota(ws, r, CE10, alto=30, wrap=True)
    ws.merge_cells('A%d:I%d' % (r, r))
    r += 2

    for texto in (
            'Este umbral es el del mantenimiento en caliente y va en la ficha '
            'de cada plato que se mantenga o se regenere. El libro NO lo '
            'aplica solo a la columna de temperatura, y es a propósito: una '
            'ensalada se sirve a 9 °C y una torrija templada a 57 °C sin '
            'incumplir nada. Quien dice qué elaboración se mantiene en '
            'caliente es su ficha, no una fórmula.',
            'Los tres tiempos medios de pase y el porcentaje de cumplimiento '
            'de ficha son los que se copian a la hoja «Semana» del cuadro de '
            'mando de cocina (libro 1 de este pack). Se copian a mano: en este '
            'pack no hay ni una fórmula que salte de un fichero a otro.',
            'Mientras un objetivo esté vacío, su semáforo no se enciende. No '
            'existe un estándar publicado de tiempos de pase en español: la '
            'referencia eres tú mismo, semana a semana.'):
        nota(ws, r, texto, alto=42, wrap=True)
        ws.merge_cells('A%d:I%d' % (r, r))
        r += 1

    for familia, fila in obj_filas.items():
        motor.regla_expresion(
            ws, 'D%d' % fila,
            '=AND(ISNUMBER($D${r}),ISNUMBER($E${r}),$D${r}>$E${r})'
            .format(r=fila))
    motor.regla_expresion(
        ws, 'D%d' % F_CUMP,
        '=AND(ISNUMBER($D${r}),ISNUMBER($E${r}),$D${r}<$E${r})'
        .format(r=F_CUMP))
    motor.semaforo_texto(ws, 'F{a}:F{b}'.format(a=M_R1, b=F_CUMP),
                         ((LECTURA_OK, motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                          (LECTURA_MAL, motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('Por debajo del objetivo', motor.CF_ROJO_BG,
                           motor.CF_ROJO_FG)))

    motor.dv_numerica(ws, ['E%d' % f for f in obj_filas.values()], minimo=0,
                      maximo=240, titulo='Minutos de pase')
    motor.dv_porcentaje(ws, ['E%d' % F_CUMP], titulo='Cumplimiento (%)')
    motor.dv_numerica(ws, ['D%d' % F_TEMP], minimo=0, maximo=120,
                      titulo='Temperatura (°C)')

    # --- listas de los desplegables (A1 de la refutación xlsx) ------------
    seccion(ws, 'A%d' % M_LSEC, 'LISTAS DE LOS DESPLEGABLES (no las borres)')
    cabecera(ws, M_SERV_CAB, [('A', 'Servicio')], altura=20)
    for i, texto in enumerate(SERVICIOS):
        motor.val(ws, 'A%d' % (M_SERV_INI + i), texto)
    cabecera(ws, M_FAM_CAB, [('A', 'Familia')], altura=20)
    for i, texto in enumerate(FAMILIAS):
        motor.val(ws, 'A%d' % (M_FAM_INI + i), texto)
    cabecera(ws, M_SI_CAB, [('A', 'Sí / No')], altura=20)
    for i, texto in enumerate(SI_NO):
        motor.val(ws, 'A%d' % (M_SI_INI + i), texto)

    ws.freeze_panes = 'C%d' % M_INI
    pagina(ws, titulos='$%d:$%d' % (M_CAB, M_CAB))
    return ws, obj_filas, F_CUMP, F_OTROS, F_TEMP, F_CALIENTE, F_CALIENTE_MAL


# --------------------------------------------------------------------------
def mapa(obj_filas, f_cump, f_otros, f_temp, f_caliente, f_caliente_mal):
    celdas_c = {
        'Fecha para simular': 'C%d' % C_SIM,
        'Hoy (fecha de referencia)': 'C%d' % C_HOY,
        'Días máximos en prueba sin ficha cerrada': 'C%d' % C_DIAS,
        'Platos en desarrollo': 'C%d' % C_R1,
        'Platos con ficha técnica cerrada': 'C%d' % (C_R1 + 1),
        'Porcentaje de platos con ficha cerrada': 'C%d' % (C_R1 + 2),
        'Platos que superan los días máximos en prueba': 'C%d' % (C_R1 + 3),
        'Platos ya lanzados': 'C%d' % (C_R1 + 4),
        'Pruebas registradas en total': 'C%d' % (C_R1 + 5),
    }
    for i, fila in enumerate(D.CALENDARIO_TEMPORADA):
        r = C_INI + i
        et = 'del plato ' + fila[0]
        celdas_c['Días naturales desde la primera prueba ' + et] = 'K%d' % r
        celdas_c['Hitos con fecha puesta ' + et] = 'L%d' % r
        celdas_c['Aviso ' + et] = 'M%d' % r
        celdas_c['Pruebas hechas ' + et] = 'N%d' % r
        celdas_c['Resultado medio ' + et] = 'O%d' % r
        celdas_c['Coste medio estimado por ración ' + et] = 'P%d' % r
        celdas_c['Veces aprobado ' + et] = 'Q%d' % r
        celdas_c['Veces descartado ' + et] = 'R%d' % r

    celdas_p = {
        'Pruebas registradas': 'C%d' % P_R1,
        'Resultado medio de todas las pruebas': 'C%d' % (P_R1 + 1),
        'Coste estimado medio por ración': 'C%d' % (P_R1 + 2),
        'Pruebas aprobadas': 'C%d' % (P_R1 + 3),
        'Pruebas descartadas': 'C%d' % (P_R1 + 4),
        'Pruebas que hubo que repetir': 'C%d' % (P_R1 + 5),
    }
    for i, fila in enumerate(D.PRUEBAS_PLATO):
        r = P_INI + i
        et = 'de la prueba %d de %s' % (fila[2], fila[1])
        celdas_p['Nombre del plato ' + et] = 'C%d' % r
        celdas_p['Aprobada (1 o 0) ' + et] = 'J%d' % r
        celdas_p['Descartada (1 o 0) ' + et] = 'K%d' % r

    celdas_m = {
        'Cumplimiento de ficha técnica en el pase (medido)': 'D%d' % f_cump,
        'Cumplimiento de ficha técnica (objetivo de la casa)': 'E%d' % f_cump,
        'Lectura del cumplimiento de ficha': 'F%d' % f_cump,
        'Muestreos hechos': 'D%d' % f_otros,
        'Muestreos NO conformes con la ficha': 'D%d' % (f_otros + 1),
        'Platos devueltos por el cliente': 'D%d' % (f_otros + 2),
        'Temperatura de emplatado más baja del muestreo': 'D%d' % (f_otros + 3),
        'Temperatura de emplatado más alta del muestreo': 'D%d' % (f_otros + 4),
        'Temperatura mínima de mantenimiento en caliente (CE-10)':
            'D%d' % f_temp,
        'Muestras de elaboraciones que se mantienen en caliente':
            'D%d' % f_caliente,
        'De ellas, por debajo del mínimo de mantenimiento en caliente':
            'D%d' % f_caliente_mal,
    }
    for familia, fila in obj_filas.items():
        celdas_m['Tiempo medio de pase medido en ' + familia] = 'D%d' % fila
        celdas_m['Tiempo de pase objetivo en ' + familia] = 'E%d' % fila
        celdas_m['Lectura del tiempo de pase en ' + familia] = 'F%d' % fila
        celdas_m['Muestreos de la familia ' + familia] = 'H%d' % fila

    tipo = {'eur': 'eur', 'pct': 'pct1', 'ent': 'num', 'dec': 'num',
            'fecha': 'txt', 'txt': 'txt'}
    return {
        'fichero': NOMBRE + '.xlsx',
        'producto': 'manual-chef-ejecutivo',
        'libro': 5,
        'que_decide': ('Renovar la carta con método y comprobar que lo que '
                       'sale por el pase es lo que dice la ficha'),
        'alerta_dias_en_prueba': {
            'celda_limite': "Calendario de Temporada!C%d" % C_DIAS,
            'dias': D.PARAMETROS_COCINA['dias_max_en_prueba_sin_ficha'],
            'texto': AVISO_ROJO,
            'plato_que_la_dispara': D.CALENDARIO_TEMPORADA[2][0],
            'dias_naturales': True,
        },
        'alimenta_libro_1': {
            'tiempos_de_pase': ['Control de Calidad del Pase!D%d' % f
                                for f in obj_filas.values()],
            'cumplimiento_ficha': 'Control de Calidad del Pase!D%d' % f_cump,
            'como': 'copia manual: cero fórmulas entre ficheros (SPEC D4)',
        },
        # A4 de la refutación xlsx (2026-09-06): celdas del mapa que
        # resuelven a "" A PROPÓSITO (N4 y N5 aún no tienen pruebas
        # registradas). El guion no debe citarlas como si tuvieran valor.
        'vacias_a_proposito': [
            'Calendario de Temporada!O16', 'Calendario de Temporada!P16',
            'Calendario de Temporada!O17', 'Calendario de Temporada!P17',
        ],
        'hojas': {
            'Calendario de Temporada': {
                'celdas': celdas_c,
                'tablas': [
                    {'titulo': 'Calendario de temporada plato a plato',
                     'cols': [[t, c, tipo[k]] for c, t, k in COLS_CAL],
                     'filas': [C_INI, C_FIN]},
                    {'titulo': 'Resumen del desarrollo de carta',
                     'cols': [['Indicador', 'B', 'txt'],
                              ['Valor', 'C', 'num']],
                     'filas': [C_R1, C_R1 + 5]},
                ],
            },
            'Registro de Pruebas de Plato': {
                'celdas': celdas_p,
                'tablas': [
                    {'titulo': 'Registro de pruebas de plato',
                     'cols': [[t, c, tipo[k]] for c, t, k in COLS_PRUEBAS],
                     'filas': [P_INI, P_FIN]},
                    {'titulo': 'Resumen del registro de pruebas',
                     'cols': [['Indicador', 'A', 'txt'],
                              ['Valor', 'C', 'num']],
                     'filas': [P_R1, P_R1 + 5]},
                ],
            },
            'Control de Calidad del Pase': {
                'celdas': celdas_m,
                'tablas': [
                    {'titulo': 'Muestreo del pase',
                     'cols': [[t, c, tipo[k]] for c, t, k in COLS_PASE],
                     'filas': [M_INI, M_FIN]},
                    {'titulo': 'Resumen del muestreo y objetivos de la casa',
                     'cols': [['Indicador', 'A', 'txt'],
                              ['Medido', 'D', 'num'],
                              ['Objetivo de la casa', 'E', 'num'],
                              ['Lectura', 'F', 'txt']],
                     'filas': [M_R1, f_caliente_mal]},
                ],
            },
        },
    }


def main():
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_calendario(wb)
    hoja_pruebas(wb)
    (_ws, obj_filas, f_cump, f_otros, f_temp, f_caliente,
     f_caliente_mal) = hoja_pase(wb)

    wb.properties.creator = 'AI Chef Pro'
    wb.properties.lastModifiedBy = 'AI Chef Pro'
    wb.properties.title = TITULO
    wb.properties.subject = PRODUCTO + ' · v1.0'

    for ws in wb.worksheets:
        motor.retirar_verde_de_calculadas(ws)
        motor.proteger(ws)

    destino = os.path.join(AQUI, 'build')
    os.makedirs(destino, exist_ok=True)
    ruta = os.path.join(destino, NOMBRE + '.xlsx')
    wb.save(ruta)
    with open(os.path.join(destino, 'mapa-' + NOMBRE + '.json'), 'w',
              encoding='utf-8') as fh:
        json.dump(mapa(obj_filas, f_cump, f_otros, f_temp, f_caliente,
                       f_caliente_mal), fh,
                  ensure_ascii=False, indent=1)
    print('escrito:', ruta)
    print('formulas registradas:', len(motor.REGISTRO))


if __name__ == '__main__':
    main()
