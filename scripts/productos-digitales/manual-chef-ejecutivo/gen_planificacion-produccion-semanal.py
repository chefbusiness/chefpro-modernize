#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_planificacion-produccion-semanal.py — libro 2 de «Manual del Chef Ejecutivo»
(SPEC §2.2 fila 2; decisiones D4, D7, D9 y D18).

Hojas: Instrucciones · Previsión de Cubiertos · Producción por Partida ·
Lista de Producción Diaria (imprimible en A4) · Ajuste por Desviación.

QUÉ DECIDE Y QUÉ NO REPITE
--------------------------
Decide CUÁNTO produce hoy cada partida, con la única cuenta que importa:

    cantidad a producir = cubiertos previstos x mix de venta - stock elaborado

Y avisa cuando esa resta sale negativa, que es la definición de
sobreproducción: hay más elaborado en cámara que demanda prevista para toda la
semana. NO repite el checklist de tareas de los «Kit de Tareas» (aquéllos
preguntan «¿se hizo?»; éste dice «cuánto»), ni la merma por partida (eso es el
cuadro de mando de cocina, libro 1), ni el escandallo (Guía Food Cost).

DECISIONES TÉCNICAS
-------------------
* La «Lista de Producción Diaria» es el CHECKLIST del manual (SPEC D18): se
  imprime en A4 vertical, se rellena a mano en el pase y sus cantidades salen
  por fórmula de la hoja «Producción por Partida», repartidas por el peso de
  los cubiertos de ese día sobre los de la semana. Las listas de sus
  desplegables viven FUERA de la zona de impresión.
* D7 — «Partidas activas (de 3 a 8)» gobierna el resumen por partida con
  `INDEX` sobre la lista; `INDIRECT` está prohibida.
* Cero constantes dentro de una fórmula: hasta los días que cubre la semana
  son una celda verde, porque hay cocinas que planifican de martes a domingo.
* La hoja «Ajuste por Desviación» se entrega VACÍA en sus columnas de entrada
  a propósito: se rellena al CERRAR la semana, con lo que pasó de verdad. Un
  dato de ejemplo ahí sería un dato inventado.
* Prohibidas `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA`,
  `RANK` y `NETWORKDAYS`: cero usos.
* `IFERROR(...,"")` en todo cociente, «sin dato» = `""` nunca 0, semáforos con
  `ISNUMBER`, textos 100 % WinAnsi (cp1252).

Salida fija: build/planificacion-produccion-semanal.xlsx
             + build/mapa-planificacion-produccion-semanal.json
"""
import json
import os
import sys

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
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
TITULO = 'Planificación de producción semanal'
NOMBRE = 'planificacion-produccion-semanal'
PID = 'manual-chef-ejecutivo'

FMT_PCT1 = '0.0%'
FMT_ENT = motor.FMT_ENT
FMT_FECHA = motor.FMT_FECHA
FMT_DEC1 = '#,##0.0'

GRIS = 'F2F2F2'
CREMA = 'FFF6DC'
ORO = 'FFD700'
CABECERA = '2D2D2D'

FECHA_VERIF = '06-09-2026'

H_PREV = "'Previsión de Cubiertos'"
H_PROD = "'Producción por Partida'"
H_LISTA = "'Lista de Producción Diaria'"
H_AJUSTE = "'Ajuste por Desviación'"

#: Las dos alertas de la hoja «Producción por Partida». El texto vive en una
#: constante porque lo usan la fórmula QUE lo escribe y el semáforo que lo
#: pinta: si se separan, el semáforo deja de encontrarlo y nadie se entera.
ALERTA_SOBRE = ('Sobreproducción: el stock ya cubre toda la semana, no '
                'produzcas')
ALERTA_CADUCA = ('El stock caduca antes de consumirse al ritmo previsto: '
                 'prográmalo en los primeros días')


def sector(idd):
    """Entrada del id `CE-*` del JSON de research (fuente, URL, fiabilidad)."""
    ruta = os.path.join(RAIZ, 'auditorias', 'guias-v2-research-sector.json')
    with open(ruta, encoding='utf-8') as fh:
        datos = json.load(fh)['datos']
    for it in datos:
        if it.get('id') == idd:
            return it
    raise KeyError('id de research inexistente: ' + idd)


def verificado(idd):
    it = sector(idd)
    return ('Verificado el ' + FECHA_VERIF + ' · ' + it['fuente_titulo']
            + ' · ' + it['url'])


# --------------------------------------------------------------------------
# Datos del caso, resueltos una sola vez
# --------------------------------------------------------------------------
N_RANURAS = 8
N_PLATOS = 20                     # 12 del caso + 8 ranuras libres
DIAS = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado',
        'Domingo')
SERVICIOS = ('Comida', 'Cena')


def _sin_tildes(t):
    for a, b in (('á', 'a'), ('é', 'e'), ('í', 'i'), ('ó', 'o'), ('ú', 'u')):
        t = t.replace(a, b).replace(a.upper(), b.upper())
    return t.lower()


#: (día, servicio) -> (reservas, histórico, previsión) del caso modelado.
PREVISION = dict(((_sin_tildes(d), s), (r, h, p))
                 for d, s, r, h, p in D.PREVISION_CUBIERTOS)
#: id de plato -> fila de STOCK_ELABORADO
STOCK = dict((f[0], f) for f in D.STOCK_ELABORADO)

DIAS_SEMANA = 7
SEMANA = D.SEMANA_TIPO_PREVISION
LUNES = D._lunes_iso(2026, SEMANA)

# --- filas de «Previsión de Cubiertos» -----------------------------------
V_SEM = 6
V_LUNES = 7
V_DIAS = 8
V_ULT = 9
V_SEC2 = 13
V_CAB = 14
V_INI = 15
V_FIN = V_INI + len(DIAS) * len(SERVICIOS) - 1        # 28
V_TOT = V_FIN + 1                                     # 29

# --- filas de «Producción por Partida» -----------------------------------
Q_CUB = 6
Q_ACT = 7
Q_LCAB = 11
Q_LINI = 12
Q_LFIN = Q_LINI + N_RANURAS - 1                       # 19
Q_SEC2 = 22
Q_PCAB = 23
Q_PINI = 24
Q_PFIN = Q_PINI + N_PLATOS - 1                        # 43
Q_PTOT = Q_PFIN + 1                                   # 44
Q_SEC3 = 48
Q_RCAB = 49
Q_RINI = 50
Q_RFIN = Q_RINI + N_RANURAS - 1                       # 57
Q_RTOT = Q_RFIN + 1                                   # 58

# --- filas de «Lista de Producción Diaria» -------------------------------
L_SEM = 5
L_DIA = 6
L_FECHA = 7
L_CUBD = 8
L_CUBS = 9
L_CAB = 13
L_INI = 14
L_FIN = L_INI + N_PLATOS - 1                          # 33
L_TOT = L_FIN + 1                                     # 34
L_FIRMA = L_TOT + 2                                   # 36
L_NOTA = L_FIRMA + 2                                  # 38
L_LCAB = 44
L_DIAS_INI = 45
L_DIAS_FIN = L_DIAS_INI + len(DIAS) - 1               # 51
L_CONS_CAB = 53
L_CONS_INI = 54
L_EST_CAB = 61
L_EST_INI = 62

CONSERVACION = [
    'Refrigeración a 4 °C o menos (vida útil de más de 24 horas)',
    'Refrigeración a 8 °C o menos (vida útil de menos de 24 horas)',
    'Congelación a -18 °C o menos',
    'Mantenimiento en caliente a 63 °C o más',
    'Consumo inmediato en el mismo servicio',
]
L_CONS_FIN = L_CONS_INI + len(CONSERVACION) - 1       # 58
ESTADOS = ['Producido', 'Pendiente', 'No se produce hoy']
L_EST_FIN = L_EST_INI + len(ESTADOS) - 1              # 64

# --- filas de «Ajuste por Desviación» ------------------------------------
A_TOL = 6
A_CAB = 9
A_INI = 10
A_FIN = A_INI + len(DIAS) * len(SERVICIOS) - 1        # 23
A_TOT = A_FIN + 1                                     # 24
A_SEC2 = 29
A_PCAB = 30
A_PINI = 31
A_PFIN = A_PINI + N_PLATOS - 1                        # 50
A_PTOT = A_PFIN + 1                                   # 51

# Todos los desplegables y el INDEX del resumen apuntan a un rango de SU MISMA
# hoja, así que van sin prefijo: un nombre de hoja con espacios («Producción
# por Partida») hay que entrecomillarlo, y sin comillas Excel lo lee como un
# nombre definido inexistente. Cazado con pycel: una sola fórmula así tumbaba
# la evaluación de 378 celdas.
REF_PARTIDAS = "$A$%d:$A$%d" % (Q_LINI, Q_LFIN)
IDX_PARTIDAS = REF_PARTIDAS
REF_DIAS = "$A$%d:$A$%d" % (L_DIAS_INI, L_DIAS_FIN)
REF_CONS = "$A$%d:$A$%d" % (L_CONS_INI, L_CONS_FIN)
REF_EST = "$A$%d:$A$%d" % (L_EST_INI, L_EST_FIN)


# --------------------------------------------------------------------------
# Utilidades de formato (mismo molde que el resto de la familia)
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


def fila_total(ws, fila, primera, ultima):
    for col in range(motor.column_index_from_string(primera),
                     motor.column_index_from_string(ultima) + 1):
        c = ws.cell(row=fila, column=col)
        c.fill = PatternFill('solid', fgColor=CREMA)
        c.font = Font(bold=True)


def cf_expresion(ws, rango, formula, bg, fg):
    ws.conditional_formatting.add(
        rango, FormulaRule(formula=[formula], stopIfTrue=True,
                           font=Font(color=fg, bold=True),
                           fill=PatternFill(start_color=bg, end_color=bg,
                                            fill_type='solid')))


def pagina(ws, apaisado=True, titulos=None, area=None, alto=0):
    ws.page_setup.paperSize = 9                      # A4
    ws.page_setup.orientation = 'landscape' if apaisado else 'portrait'
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = alto
    if ws.sheet_properties.pageSetUpPr is None:
        ws.sheet_properties.pageSetUpPr = PageSetupProperties()
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins = PageMargins(left=0.59, right=0.59, top=0.59,
                                  bottom=0.59, header=0.3, footer=0.3)
    ws.oddFooter.center.text = 'AI Chef Pro · aichef.pro · Página &P de &N'
    ws.oddFooter.center.size = 8
    if titulos:
        ws.print_title_rows = titulos
    if area:
        ws.print_area = area


def encabezar(ws, titulo, nota_=None):
    motor.val(ws, 'A1', titulo)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', SUBTITULO)
    if nota_:
        motor.val(ws, 'A3', nota_)
        ws['A3'].font = Font(italic=True, size=9)


def anchos(ws, mapa):
    for letra, ancho in mapa.items():
        ws.column_dimensions[letra].width = ancho


def nota(ws, fila, texto, alto=None, col='A', wrap=False):
    motor.val(ws, col + str(fila), texto, wrap=wrap)
    if alto:
        ws.row_dimensions[fila].height = alto


def dv_rango(ws, coords, ref, titulo, mensaje):
    """Desplegable contra un RANGO (convención de familia: nunca lista con
    comas, que se parte en cuanto una opción lleva una coma dentro)."""
    dv = DataValidation(type='list', formula1=ref, allow_blank=True,
                        showErrorMessage=True, errorTitle=titulo,
                        error=mensaje)
    ws.add_data_validation(dv)
    for c in coords:
        dv.add(c)
    return dv


def mirar(ref):
    return '=IF({r}="","",{r})'.format(r=ref)


# --------------------------------------------------------------------------
# Hoja «Instrucciones»
# --------------------------------------------------------------------------
PASOS = [
    '1. Hoja «Previsión de Cubiertos»: pon la semana ISO, el lunes que la abre '
    'y cuántos días abres. Después, por cada día y servicio, las reservas '
    'confirmadas y el histórico de ese mismo servicio (la media de las cuatro '
    'semanas anteriores). El libro te sugiere una previsión; la que manda es '
    'la que escribas tú en la columna verde.',
    '2. Hoja «Producción por Partida»: escribe tus partidas (estaciones, en '
    'el vocabulario de la matriz de polivalencia del Manual del Manager) y '
    'cuántas tienes activas. Después, plato a plato: la partida que lo '
    'produce, la unidad de ración, el mix de venta y lo que ya tienes '
    'elaborado en cámara.',
    '3. Esa hoja hace la única cuenta que importa: cantidad a producir = '
    'cubiertos previstos x mix de venta - stock ya elaborado. Si te sale cero, '
    'no produces; si el stock supera la demanda de toda la semana, la columna '
    '«Alerta» te lo dice con todas las letras.',
    '4. El bloque «Resumen por partida» del final te dice cuántas raciones le '
    'tocan esta semana a cada partida. Es lo que se lee en la reunión de los '
    'lunes y lo que decide si hace falta una mano más en fríos.',
    '5. Hoja «Lista de Producción Diaria»: elige el día y IMPRÍMELA. Sale en '
    'A4 vertical con las cantidades del día ya calculadas, y con las columnas '
    'en blanco para que el equipo anote lo producido, la hora, la '
    'conservación y quién lo hizo. Es el checklist de este manual.',
    '6. Hoja «Ajuste por Desviación»: se rellena al CERRAR la semana, no '
    'antes. Se apuntan los cubiertos reales y lo que de verdad se produjo y se '
    'vendió, y la hoja te dice de cuánto te has desviado y qué histórico '
    'llevarte a la semana siguiente. Viene vacía a propósito.',
    '7. Cadencia de uso: la previsión y la producción, UNA VEZ POR SEMANA (el '
    'viernes o el sábado, para la semana siguiente). La lista diaria, todos '
    'los días. El ajuste, al cerrar la semana.',
]

NOTAS_LIBRO = [
    'ESTE LIBRO NO ES UN CHECKLIST DE TAREAS. Los «Kit de Tareas» preguntan '
    '«¿se hizo la tarea de apertura?»; éste responde «cuántas raciones hay que '
    'producir hoy en cada partida». La «Lista de Producción Diaria» es la '
    'única hoja que se imprime y se firma, y lo que registra son cantidades, '
    'no tareas.',
    'La merma NO se mide aquí. Lo que esta hoja mide al cerrar la semana es el '
    'SOBRANTE: raciones producidas menos raciones vendidas. La merma por '
    'partida (kilos que se van a la basura sobre kilos producidos) se registra '
    'en el cuadro de mando de cocina, que es el libro 1 de este pack. No son '
    'lo mismo y no se suman.',
    'El coste de una ración no se calcula aquí: se copia del escandallo. Este '
    'pack no recalcula ningún coste, y por eso ninguna hoja lleva una columna '
    'de euros. El escandallo vive en el «Kit de Escandallos» y en la «Guía '
    'Food Cost + Ingeniería de Menú».',
    'El mix de venta es el porcentaje de cubiertos que pide cada plato: si de '
    'cada 100 comensales 11 piden croquetas, el mix de las croquetas es el '
    '11 %. Sale del TPV, del histórico de la carta o de la ingeniería de menú, '
    'y se revisa cuando cambia la carta.',
    'La previsión sugerida es el MAYOR entre las reservas confirmadas y el '
    'histórico, redondeado hacia arriba. Es una sugerencia mecánica: el que '
    'sabe que el sábado hay partido, o que llueve toda la semana, eres tú.',
    'Un dato que falta se deja EN BLANCO, nunca a cero. Un cero es una medida '
    '(«no hay stock de este plato») y un blanco es la ausencia de medida: el '
    'libro los trata distinto.',
]


def hoja_instrucciones(wb):
    ws = wb.create_sheet('Instrucciones', 0)
    anchos(ws, {'A': 38, 'B': 52, 'C': 52})
    motor.val(ws, 'A1', TITULO)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', SUBTITULO)
    motor.val(ws, 'A3', 'Para qué sirve: producir lo que se va a vender, ni una '
                        'ración más.')
    ws['A3'].font = Font(italic=True, size=9)

    fila = 5
    seccion(ws, 'A%d' % fila, 'Instrucciones de uso')
    fila += 1
    for paso in PASOS:
        ws.merge_cells('A%d:C%d' % (fila, fila))
        nota(ws, fila, paso, alto=44, wrap=True)
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, motor.NOTA_VERDES)
    ws['A%d' % fila].fill = PatternFill('solid', fgColor=motor.VERDE)
    fila += 2

    seccion(ws, 'A%d' % fila, 'De dónde sale cada dato')
    fila += 1
    cabecera(ws, fila, [('A', 'Dato'), ('B', 'De dónde sale'),
                        ('C', 'Qué no hay que volver a teclear')], altura=32)
    fila += 1
    contrato = [
        ('Cubiertos previstos por día y servicio',
         'Del histórico de tu TPV y de las reservas confirmadas. Si tienes el '
         'Manual del Manager, la columna de cubiertos de su cuadro de mando '
         'semanal ya lleva el histórico de las 52 semanas',
         'El histórico: cópialo de una semana a otra con la última columna de '
         'la hoja «Ajuste por Desviación»'),
        ('Mix de venta de cada plato',
         'Del TPV o de la ingeniería de menú de la «Guía Food Cost + '
         'Ingeniería de Menú»',
         'El mix se teclea una vez por temporada, no cada semana'),
        ('Partidas de la cocina',
         'Las mismas del cuadro de mando de cocina (libro 1 de este pack)',
         'Cópialas del libro 1: son copia declarada, no vínculo'),
    ]
    for dato, de_donde, no_teclear in contrato:
        motor.val(ws, 'A%d' % fila, dato, bold=True, wrap=True)
        motor.val(ws, 'B%d' % fila, de_donde, wrap=True)
        motor.val(ws, 'C%d' % fila, no_teclear, wrap=True)
        ws.row_dimensions[fila].height = 62
        fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    nota(ws, fila,
         'Ninguna hoja de este libro lee una celda de otro fichero: es copia '
         'declarada. Si mueves un fichero de carpeta, nada se rompe.',
         alto=30, wrap=True)
    fila += 2

    seccion(ws, 'A%d' % fila, 'Lo que conviene saber antes de empezar')
    fila += 1
    for texto in NOTAS_LIBRO:
        ws.merge_cells('A%d:C%d' % (fila, fila))
        nota(ws, fila, texto, alto=58, wrap=True)
        fila += 1
    fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila, D.NOTA_DESPROTEGER, wrap=True)
    fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila,
              'Ruta en Excel: Revisar > Desproteger hoja. La protección no '
              'tiene contraseña; sirve para no pisar una fórmula sin querer.',
              wrap=True)
    fila += 2
    motor.val(ws, 'A%d' % fila, D.BIO)
    fila += 1
    motor.val(ws, 'A%d' % fila, D.VERSION_LINE)
    pagina(ws, apaisado=False)
    return ws


# --------------------------------------------------------------------------
# Hoja «Previsión de Cubiertos»
# --------------------------------------------------------------------------
def hoja_prevision(wb):
    ws = wb.create_sheet('Previsión de Cubiertos')
    anchos(ws, {'A': 16, 'B': 14, 'C': 22, 'D': 26, 'E': 20, 'F': 22,
                'G': 24, 'H': 60})
    encabezar(ws, 'Previsión de cubiertos de la semana',
              nota_='La previsión que manda es la tuya. La sugerida es una '
                    'cuenta mecánica sobre reservas e histórico.')

    seccion(ws, 'A5', 'LA SEMANA QUE SE PLANIFICA')
    motor.val(ws, 'A%d' % V_SEM, 'Semana ISO', bold=True)
    motor.val(ws, 'B%d' % V_SEM, SEMANA, fmt=FMT_ENT, verde_=True)
    motor.val(ws, 'A%d' % V_LUNES, 'Lunes de la semana', bold=True)
    motor.val(ws, 'B%d' % V_LUNES, LUNES, fmt=FMT_FECHA, verde_=True)
    motor.val(ws, 'A%d' % V_DIAS, 'Días que cubre la planificación', bold=True)
    motor.val(ws, 'B%d' % V_DIAS, DIAS_SEMANA, fmt=FMT_ENT, verde_=True)
    motor.val(ws, 'A%d' % V_ULT, 'Último día de la semana', bold=True)
    motor.f(ws, 'B%d' % V_ULT,
            '=IF(OR($B${l}="",$B${d}=""),"",$B${l}+$B${d}-1)'
            .format(l=V_LUNES, d=V_DIAS), fmt=FMT_FECHA)
    ws['B%d' % V_ULT].fill = PatternFill('solid', fgColor=GRIS)

    nota(ws, V_ULT + 1,
         'La semana ISO empieza en lunes y la semana 1 del año es la que '
         'contiene el primer jueves de enero. Los días que cubre la '
         'planificación son SIETE aunque cierres uno o dos: los días de cierre '
         'se dejan en blanco y no suman.')
    nota(ws, V_ULT + 2,
         'El último día de la semana lo calcula el libro y es el que usa la '
         'hoja «Producción por Partida» para avisar de un stock que caduca '
         'antes de consumirse.')

    seccion(ws, 'A%d' % V_SEC2, 'PREVISIÓN POR DÍA Y SERVICIO')
    cabecera(ws, V_CAB,
             [('A', 'Día'), ('B', 'Servicio'),
              ('C', 'Reservas confirmadas'),
              ('D', 'Histórico del mismo servicio (media de 4 semanas)'),
              ('E', 'Previsión sugerida'),
              ('F', 'Previsión de cubiertos (la tuya)'),
              ('G', 'Diferencia con la sugerida')], altura=60)
    fila = V_INI
    for dia in DIAS:
        for servicio in SERVICIOS:
            motor.val(ws, 'A%d' % fila, dia, bold=True)
            motor.val(ws, 'B%d' % fila, servicio)
            datos = PREVISION.get((_sin_tildes(dia), servicio))
            if datos:
                reservas, historico, prevision = datos
                motor.val(ws, 'C%d' % fila, reservas, fmt=FMT_ENT, verde_=True)
                motor.val(ws, 'D%d' % fila, float(historico), fmt=FMT_DEC1,
                          verde_=True)
            else:
                prevision = None
                motor.verde(ws, 'C%d' % fila)
                motor.verde(ws, 'D%d' % fila)
                ws['C%d' % fila].number_format = FMT_ENT
                ws['D%d' % fila].number_format = FMT_DEC1
            motor.f(ws, 'E%d' % fila,
                    '=IFERROR(IF(AND($C{r}="",$D{r}=""),"",'
                    'ROUNDUP(MAX(IF($C{r}="",0,$C{r}),IF($D{r}="",0,$D{r})),'
                    '0)),"")'.format(r=fila), fmt=FMT_ENT)
            if prevision is None:
                motor.verde(ws, 'F%d' % fila)
                ws['F%d' % fila].number_format = FMT_ENT
            else:
                motor.val(ws, 'F%d' % fila, prevision, fmt=FMT_ENT,
                          verde_=True)
            motor.f(ws, 'G%d' % fila,
                    '=IFERROR(IF(OR(NOT(ISNUMBER($F{r})),NOT(ISNUMBER($E{r})),'
                    '$E{r}=0),"",($F{r}-$E{r})/$E{r}),"")'.format(r=fila),
                    fmt=FMT_PCT1)
            fila += 1

    motor.val(ws, 'A%d' % V_TOT, 'TOTAL DE LA SEMANA', bold=True)
    for letra, fmt in (('C', FMT_ENT), ('D', FMT_DEC1), ('E', FMT_ENT),
                       ('F', FMT_ENT)):
        motor.f(ws, letra + str(V_TOT),
                '=IF(COUNT({c}{a}:{c}{b})=0,"",SUM({c}{a}:{c}{b}))'
                .format(c=letra, a=V_INI, b=V_FIN), fmt=fmt, bold=True)
    motor.f(ws, 'G%d' % V_TOT,
            '=IFERROR(IF(OR(NOT(ISNUMBER($F${t})),NOT(ISNUMBER($E${t})),'
            '$E${t}=0),"",($F${t}-$E${t})/$E${t}),"")'.format(t=V_TOT),
            fmt=FMT_PCT1, bold=True)
    fila_total(ws, V_TOT, 'A', 'G')

    nota(ws, V_TOT + 2,
         'El total de la columna «Previsión de cubiertos (la tuya)» es el que '
         'alimenta la hoja «Producción por Partida». Si cambias un solo día, '
         'la producción de toda la semana se recalcula sola.')
    nota(ws, V_TOT + 3,
         'En el restaurante de ejemplo el lunes está cerrado: sus dos filas '
         'van en blanco y no suman. Si tú abres los lunes, rellénalas.')
    nota(ws, V_TOT + 4,
         'La diferencia con la sugerida no es un error: es tu criterio. Lo que '
         'sí conviene mirar es si SIEMPRE vas por encima o SIEMPRE por debajo, '
         'porque entonces el que está mal calibrado es el histórico.')

    filas = list(range(V_INI, V_FIN + 1))
    motor.dv_numerica(ws, ['C%d' % r for r in filas] + ['F%d' % r
                                                        for r in filas],
                      minimo=0, maximo=10000, titulo='Cubiertos',
                      mensaje='Número de comensales de ese servicio.')
    motor.dv_numerica(ws, ['D%d' % r for r in filas], minimo=0, maximo=10000,
                      titulo='Histórico',
                      mensaje='Media de cubiertos de ese mismo servicio en las '
                              'cuatro semanas anteriores.')
    motor.dv_numerica(ws, ['B%d' % V_SEM], minimo=1, maximo=53,
                      titulo='Semana ISO', mensaje='La semana ISO va de 1 a 53.')
    motor.dv_numerica(ws, ['B%d' % V_DIAS], minimo=1, maximo=7,
                      titulo='Días de la semana',
                      mensaje='Cuántos días cubre la planificación (1 a 7).')
    motor.dv_fecha(ws, ['B%d' % V_LUNES])
    ws.freeze_panes = 'C%d' % V_INI
    pagina(ws, apaisado=False, titulos='$%d:$%d' % (V_CAB, V_CAB))
    return ws


# --------------------------------------------------------------------------
# Hoja «Producción por Partida»
# --------------------------------------------------------------------------
COLS_PROD = [
    ('A', 'Id', 8),
    ('B', 'Plato', 34),
    ('C', 'Elaboración previa (mise en place)', 38),
    ('D', 'Partida', 22),
    ('E', 'Unidad de ración', 26),
    ('F', 'Mix de venta (% de los cubiertos)', 13),
    ('G', 'Raciones previstas en la semana', 14),
    ('H', 'Stock ya elaborado (raciones)', 13),
    ('I', 'Conservación del stock', 26),
    ('J', 'Fecha de elaboración del stock', 14),
    ('K', 'Vida útil (días)', 11),
    ('L', 'Consumir antes del', 15),
    ('M', 'Cantidad a producir (raciones)', 14),
    ('N', 'Alerta', 46),
]


def hoja_produccion(wb):
    ws = wb.create_sheet('Producción por Partida')
    anchos(ws, dict((letra, ancho) for letra, _t, ancho in COLS_PROD))
    encabezar(ws, 'Producción de la semana, partida por partida',
              nota_='Cantidad a producir = cubiertos previstos x mix de venta '
                    '- stock ya elaborado.')

    seccion(ws, 'A5', 'PARÁMETROS DE LA SEMANA')
    motor.val(ws, 'A%d' % Q_CUB, 'Cubiertos previstos de la semana', bold=True)
    motor.f(ws, 'B%d' % Q_CUB, mirar('%s!$F$%d' % (H_PREV, V_TOT)),
            fmt=FMT_ENT)
    ws['B%d' % Q_CUB].fill = PatternFill('solid', fgColor=GRIS)
    motor.val(ws, 'A%d' % Q_ACT, 'Partidas activas (de 3 a 8)', bold=True)
    motor.val(ws, 'B%d' % Q_ACT, D.PARAMETROS_COCINA['partidas_activas'],
              fmt=FMT_ENT, verde_=True)
    nota(ws, Q_ACT + 1,
         'Los cubiertos de la semana los trae la hoja «Previsión de '
         'Cubiertos»: no se teclean aquí.')
    nota(ws, Q_ACT + 2,
         'Las partidas activas gobiernan el «Resumen por partida» del final de '
         'la hoja: si pones 4, las ranuras 5 a 8 se quedan en blanco.')

    cabecera(ws, Q_LCAB, [('A', 'Partidas de tu cocina')],
             altura=24)
    for i in range(N_RANURAS):
        r = Q_LINI + i
        if i < len(D.PARTIDAS):
            motor.val(ws, 'A%d' % r, D.PARTIDAS[i][0], verde_=True)
        else:
            motor.verde(ws, 'A%d' % r)
    nota(ws, Q_LFIN + 1,
         'Son las mismas partidas del cuadro de mando de cocina (libro 1). '
         'Cópialas de allí: este libro no lee ningún fichero ajeno. Las dos '
         'últimas ranuras están libres para cocinas con más partidas.')

    # --- los platos --------------------------------------------------------
    seccion(ws, 'A%d' % Q_SEC2, 'PLATOS DE LA CARTA')
    cabecera(ws, Q_PCAB, [(letra, texto) for letra, texto, _a in COLS_PROD],
             altura=60)
    cub = '$B$%d' % Q_CUB
    ult = '%s!$B$%d' % (H_PREV, V_ULT)
    lun = '%s!$B$%d' % (H_PREV, V_LUNES)
    dias = '%s!$B$%d' % (H_PREV, V_DIAS)
    for i in range(N_PLATOS):
        r = Q_PINI + i
        if i < len(D.MIX_VENTA):
            p = D.MIX_VENTA[i]
            st = STOCK.get(p['id'])
            motor.val(ws, 'A%d' % r, p['id'], verde_=True, align='center')
            motor.val(ws, 'B%d' % r, p['plato'], verde_=True, wrap=True)
            elab = st[1] if st else ''
            if elab.startswith('Sin stock'):
                elab = ''          # se monta a la comanda: no hay mise en place
            motor.val(ws, 'C%d' % r, elab, verde_=True, wrap=True)
            motor.val(ws, 'D%d' % r, p['partida'], verde_=True, wrap=True)
            motor.val(ws, 'E%d' % r, p['unidad_racion'], verde_=True,
                      wrap=True)
            motor.val(ws, 'F%d' % r, p['mix'], fmt=FMT_PCT1, verde_=True)
            if st and st[3]:
                motor.val(ws, 'H%d' % r, st[3], fmt=FMT_ENT, verde_=True)
                motor.val(ws, 'I%d' % r, st[6], verde_=True, wrap=True)
                motor.val(ws, 'J%d' % r, D._fecha(st[4]), fmt=FMT_FECHA,
                          verde_=True)
                motor.val(ws, 'K%d' % r, st[5], fmt=FMT_ENT, verde_=True)
            else:
                motor.val(ws, 'H%d' % r, 0, fmt=FMT_ENT, verde_=True)
                motor.val(ws, 'I%d' % r, st[6] if st else '', verde_=True,
                          wrap=True)
                motor.verde(ws, 'J%d' % r)
                motor.verde(ws, 'K%d' % r)
                ws['J%d' % r].number_format = FMT_FECHA
                ws['K%d' % r].number_format = FMT_ENT
            ws.row_dimensions[r].height = 30
        else:
            for letra in 'ABCDEFHIJK':
                motor.verde(ws, letra + str(r))
            ws['F%d' % r].number_format = FMT_PCT1
            for letra in ('H', 'K'):
                ws[letra + str(r)].number_format = FMT_ENT
            ws['J%d' % r].number_format = FMT_FECHA
        motor.f(ws, 'G%d' % r,
                '=IFERROR(IF(OR(NOT(ISNUMBER($F{r})),NOT(ISNUMBER({c}))),"",'
                'ROUNDUP($F{r}*{c},0)),"")'.format(r=r, c=cub), fmt=FMT_ENT)
        motor.f(ws, 'L%d' % r,
                '=IF(OR(NOT(ISNUMBER($J{r})),NOT(ISNUMBER($K{r}))),"",'
                '$J{r}+$K{r})'.format(r=r), fmt=FMT_FECHA)
        motor.f(ws, 'M%d' % r,
                '=IFERROR(IF($G{r}="","",MAX(0,$G{r}-IF($H{r}="",0,$H{r}))),'
                '"")'.format(r=r), fmt=FMT_ENT)
        # A3 de la refutación xlsx (2026-09-06): las dos alertas eran
        # excluyentes (la de caducidad iba en el ELSE de la sobreproducción)
        # y el propio caso de ejemplo probaba que se perdía un aviso real.
        # Ahora se comprueban por separado y se concatenan.
        sobre_cond = 'AND(ISNUMBER($H{r}),$H{r}>$G{r})'.format(r=r)
        caduca_cond = ('AND(ISNUMBER($L{r}),ISNUMBER($H{r}),$H{r}>0,'
                       'ISNUMBER({l}),ISNUMBER({d}),$G{r}>0,'
                       '$L{r}<{l}+$H{r}*{d}/$G{r})'
                       ).format(r=r, l=lun, d=dias)
        motor.f(ws, 'N%d' % r,
                ('=IFERROR(IF($G{r}="","",TRIM('
                 'IF({sc},"{sobre}","")'
                 '&IF(AND({sc},{cc}),". ","")'
                 '&IF({cc},"{caduca}","")'
                 ')),"")')
                .format(r=r, sc=sobre_cond, cc=caduca_cond,
                        sobre=ALERTA_SOBRE, caduca=ALERTA_CADUCA))

    motor.val(ws, 'A%d' % Q_PTOT, 'TOTAL', bold=True)
    for letra in ('G', 'H', 'M'):
        motor.f(ws, letra + str(Q_PTOT),
                '=IF(COUNT({c}{a}:{c}{b})=0,"",SUM({c}{a}:{c}{b}))'
                .format(c=letra, a=Q_PINI, b=Q_PFIN), fmt=FMT_ENT, bold=True)
    motor.f(ws, 'F%d' % Q_PTOT,
            '=IF(COUNT($F{a}:$F{b})=0,"",SUM($F{a}:$F{b}))'
            .format(a=Q_PINI, b=Q_PFIN), fmt=FMT_PCT1, bold=True)
    fila_total(ws, Q_PTOT, 'A', 'N')

    nota(ws, Q_PTOT + 1,
         'El total del mix no tiene por qué sumar 100 %: mide cuántas raciones '
         'de estos platos se venden por cada 100 cubiertos, y un comensal '
         'puede pedir entrante y principal, o sólo un plato del menú.')
    nota(ws, Q_PTOT + 2,
         'La fecha de «consumir antes del» es la de elaboración más la vida '
         'útil que TÚ le has dado. No existe ninguna tabla legal de días: la '
         'ley sólo exige un estudio de vida útil documentado cuando el '
         'producto favorece el crecimiento de Listeria monocytogenes, y cada '
         'establecimiento fija y documenta su criterio dentro del APPCC. '
         # CE-37 sostiene la afirmación, pero su «fuente» es una síntesis
         # interna: la nota cita la norma de verdad, que es la de CE-08.
         + verificado('CE-08') +
         ' El aviso de caducidad reparte el stock entre los días que cubre '
         'la planificación (celda verde de «Previsión de Cubiertos»): son '
         'DÍAS NATURALES, no días de servicio (A6 de la refutación xlsx), '
         'así que si cierras alguno, revisa a ojo lo que caduca en tu '
         'primer día de apertura.')
    nota(ws, Q_PTOT + 3,
         'Si congelas una elaboración de la casa, la etiqueta lleva TRES '
         'fechas: la de elaboración, la de congelación y la de caducidad o '
         'consumo preferente del congelado, con registro de descripción y '
         'cantidad. ' + verificado('CE-13'))

    # --- resumen por partida ----------------------------------------------
    seccion(ws, 'A%d' % Q_SEC3, 'RESUMEN POR PARTIDA')
    cabecera(ws, Q_RCAB,
             [('A', 'Partida'), ('B', 'Raciones previstas'),
              ('C', 'Stock ya elaborado'), ('D', 'Raciones a producir'),
              ('E', 'Peso sobre lo que hay que producir')], altura=44)
    for i in range(N_RANURAS):
        r = Q_RINI + i
        motor.f(ws, 'A%d' % r,
                '=IFERROR(IF({k}>$B${a},"",IF(INDEX({rp},{k})=0,"",'
                'INDEX({rp},{k}))),"")'
                .format(k=i + 1, a=Q_ACT, rp=IDX_PARTIDAS))
        for letra, origen, fmt in (('B', 'G', FMT_ENT), ('C', 'H', FMT_ENT),
                                   ('D', 'M', FMT_ENT)):
            motor.f(ws, letra + str(r),
                    '=IF($A{r}="","",SUMIF($D${a}:$D${b},$A{r},'
                    '${o}${a}:${o}${b}))'
                    .format(r=r, a=Q_PINI, b=Q_PFIN, o=origen), fmt=fmt)
        motor.f(ws, 'E%d' % r,
                '=IFERROR(IF(OR($A{r}="",NOT(ISNUMBER($D{r})),'
                'NOT(ISNUMBER($D${t})),$D${t}=0),"",$D{r}/$D${t}),"")'
                .format(r=r, t=Q_RTOT), fmt=FMT_PCT1)
    motor.val(ws, 'A%d' % Q_RTOT, 'TOTAL', bold=True)
    for letra in ('B', 'C', 'D'):
        motor.f(ws, letra + str(Q_RTOT),
                '=IF(COUNT({c}{a}:{c}{b})=0,"",SUM({c}{a}:{c}{b}))'
                .format(c=letra, a=Q_RINI, b=Q_RFIN), fmt=FMT_ENT, bold=True)
    motor.f(ws, 'E%d' % Q_RTOT,
            '=IFERROR(IF(OR(NOT(ISNUMBER($D${t})),$D${t}=0),"",'
            '$D${t}/$D${t}),"")'.format(t=Q_RTOT), fmt=FMT_PCT1, bold=True)
    fila_total(ws, Q_RTOT, 'A', 'E')
    nota(ws, Q_RTOT + 2,
         'Este bloque es el que se lee en la reunión de cocina: dice qué '
         'partida carga con la producción de la semana. Si una partida se '
         'lleva la mitad de las raciones y la sostiene una sola persona, ahí '
         'tienes un punto único de fallo, y la matriz de polivalencia del '
         'Manual del Manager te dice a quién formar.')
    nota(ws, Q_RTOT + 4,
         'Una partida que no produce raciones (sala, caja) sale con cero: no '
         'es un error, sigue siendo una partida de tu organigrama y está en la '
         'lista para que las seis coincidan con las del cuadro de mando de '
         'cocina y con la matriz de polivalencia del Manual del Manager.')
    nota(ws, Q_RTOT + 3,
         'Las raciones previstas del resumen pueden no cuadrar con el total de '
         'la tabla de platos si algún plato se ha quedado sin partida: '
         'compruébalo mirando que las dos filas TOTAL coincidan.')

    # --- semáforos y validaciones -----------------------------------------
    cf_expresion(ws, 'H%d:H%d' % (Q_PINI, Q_PFIN),
                 '=AND(ISNUMBER($H{a}),ISNUMBER($G{a}),$H{a}>$G{a})'
                 .format(a=Q_PINI), motor.CF_ROJO_BG, motor.CF_ROJO_FG)
    cf_expresion(ws, 'M%d:M%d' % (Q_PINI, Q_PFIN),
                 '=AND(ISNUMBER($M{a}),ISNUMBER($G{a}),$M{a}=0)'
                 .format(a=Q_PINI), motor.CF_AMBAR_BG, motor.CF_AMBAR_FG)
    # Dos severidades: la sobreproducción es ROJA (has producido de más y ya
    # está pagado) y la caducidad corta es ÁMBAR (no es un error, es un orden
    # de trabajo: ese stock va en los primeros días de la semana).
    # LEFT/LEN, no igualdad exacta: N puede llevar las dos alertas
    # concatenadas (A3 de la refutación xlsx) y el caso de sobreproducción
    # sigue siendo el más grave aunque también caduque.
    cf_expresion(ws, 'N%d:N%d' % (Q_PINI, Q_PFIN),
                 '=AND(ISNUMBER($G{a}),LEFT($N{a},LEN("{t}"))="{t}")'
                 .format(a=Q_PINI, t=ALERTA_SOBRE),
                 motor.CF_ROJO_BG, motor.CF_ROJO_FG)
    cf_expresion(ws, 'N%d:N%d' % (Q_PINI, Q_PFIN),
                 '=AND(ISNUMBER($G{a}),LEN($N{a})>0)'.format(a=Q_PINI),
                 motor.CF_AMBAR_BG, motor.CF_AMBAR_FG)

    filas = list(range(Q_PINI, Q_PFIN + 1))
    dv_rango(ws, ['D%d' % r for r in filas], REF_PARTIDAS, 'Partida',
             'Elige una de las partidas de la lista de la parte de arriba de '
             'esta hoja.')
    motor.dv_porcentaje(ws, ['F%d' % r for r in filas], titulo='Mix de venta',
                        prompt='Se escribe en tanto por uno: 0,11 = 11 % de '
                               'los cubiertos.')
    motor.dv_numerica(ws, ['H%d' % r for r in filas], minimo=0, maximo=100000,
                      titulo='Stock elaborado',
                      mensaje='Raciones ya elaboradas que tienes en cámara.')
    motor.dv_numerica(ws, ['K%d' % r for r in filas], minimo=0, maximo=3650,
                      titulo='Vida útil',
                      mensaje='Días de vida útil que TÚ has documentado para '
                              'esa elaboración.')
    motor.dv_fecha(ws, ['J%d' % r for r in filas])
    motor.dv_numerica(ws, ['B%d' % Q_ACT], minimo=3, maximo=N_RANURAS,
                      titulo='Partidas activas',
                      mensaje='Un número entre 3 y 8.')
    ws.freeze_panes = 'C%d' % Q_PINI
    pagina(ws, titulos='$%d:$%d' % (Q_PCAB, Q_PCAB))
    return ws


# --------------------------------------------------------------------------
# Hoja «Lista de Producción Diaria» (imprimible en A4 vertical)
# --------------------------------------------------------------------------
COLS_LISTA = [
    ('A', 'Partida', 20),
    ('B', 'Elaboración', 36),
    ('C', 'Unidad de ración', 20),
    ('D', 'Raciones para hoy', 12),
    ('E', 'Producido (raciones)', 12),
    ('F', 'Hora de fin', 11),
    ('G', 'Conservación', 30),
    ('H', 'Responsable', 18),
    ('I', 'Estado', 16),
]


def hoja_lista(wb):
    ws = wb.create_sheet('Lista de Producción Diaria')
    anchos(ws, dict((letra, ancho) for letra, _t, ancho in COLS_LISTA))
    encabezar(ws, 'Lista de producción diaria',
              nota_='Elige el día, imprime y cuélgala en la cocina. Las cuatro '
                    'columnas de la derecha se rellenan a mano.')

    motor.val(ws, 'A%d' % L_SEM, 'Semana ISO', bold=True)
    motor.f(ws, 'B%d' % L_SEM, mirar('%s!$B$%d' % (H_PREV, V_SEM)),
            fmt=FMT_ENT)
    motor.val(ws, 'A%d' % L_DIA, 'Día de la lista', bold=True)
    motor.val(ws, 'B%d' % L_DIA, DIAS[4], verde_=True)
    motor.val(ws, 'A%d' % L_FECHA, 'Fecha', bold=True)
    motor.f(ws, 'B%d' % L_FECHA,
            '=IFERROR(IF(OR($B${d}="",{lun}=""),"",'
            '{lun}+MATCH($B${d},$A${di}:$A${df},0)-1),"")'
            .format(d=L_DIA, lun='%s!$B$%d' % (H_PREV, V_LUNES),
                    di=L_DIAS_INI, df=L_DIAS_FIN), fmt=FMT_FECHA)
    motor.val(ws, 'A%d' % L_CUBD, 'Cubiertos previstos del día', bold=True)
    motor.f(ws, 'B%d' % L_CUBD,
            '=IFERROR(IF($B${d}="","",SUMIF({dia},$B${d},{prev})),"")'
            .format(d=L_DIA,
                    dia='%s!$A$%d:$A$%d' % (H_PREV, V_INI, V_FIN),
                    prev='%s!$F$%d:$F$%d' % (H_PREV, V_INI, V_FIN)),
            fmt=FMT_ENT)
    motor.val(ws, 'A%d' % L_CUBS, 'Cubiertos previstos de la semana',
              bold=True)
    motor.f(ws, 'B%d' % L_CUBS, mirar('%s!$F$%d' % (H_PREV, V_TOT)),
            fmt=FMT_ENT)
    for r in (L_SEM, L_FECHA, L_CUBD, L_CUBS):
        ws['B%d' % r].fill = PatternFill('solid', fgColor=GRIS)

    nota(ws, L_CUBD + 2,
         'Las raciones de hoy salen de la producción de la semana repartida '
         'por el peso de los cubiertos de este día: cantidad semanal x '
         'cubiertos del día / cubiertos de la semana, redondeada hacia arriba.')
    nota(ws, L_CUBD + 3,
         'Si un día concreto pide otra cosa (un menú de grupo, una fiesta '
         'local), corrige la cantidad a mano sobre el papel: esta hoja es un '
         'punto de partida, no una orden.')

    cabecera(ws, L_CAB, [(letra, texto) for letra, texto, _a in COLS_LISTA],
             altura=44)
    for i in range(N_PLATOS):
        r = L_INI + i
        pr = Q_PINI + i
        motor.f(ws, 'A%d' % r, mirar('%s!$D$%d' % (H_PROD, pr)))
        motor.f(ws, 'B%d' % r,
                '=IF({prod}!$B${p}="","",IF({prod}!$C${p}="",'
                '{prod}!$B${p},{prod}!$C${p}))'
                .format(prod=H_PROD, p=pr))
        motor.f(ws, 'C%d' % r, mirar('%s!$E$%d' % (H_PROD, pr)))
        motor.f(ws, 'D%d' % r,
                '=IFERROR(IF(OR({prod}!$M${p}="",NOT(ISNUMBER($B${cd})),'
                'NOT(ISNUMBER($B${cs})),$B${cs}=0),"",'
                'ROUNDUP({prod}!$M${p}*$B${cd}/$B${cs},0)),"")'
                .format(prod=H_PROD, p=pr, cd=L_CUBD, cs=L_CUBS), fmt=FMT_ENT)
        for letra in 'EFGHI':
            motor.verde(ws, letra + str(r))
        ws['E%d' % r].number_format = FMT_ENT
        ws.row_dimensions[r].height = 26
    motor.val(ws, 'A%d' % L_TOT, 'TOTAL DEL DÍA', bold=True)
    for letra in ('D', 'E'):
        motor.f(ws, letra + str(L_TOT),
                '=IF(COUNT({c}{a}:{c}{b})=0,"",SUM({c}{a}:{c}{b}))'
                .format(c=letra, a=L_INI, b=L_FIN), fmt=FMT_ENT, bold=True)
    fila_total(ws, L_TOT, 'A', 'I')

    motor.val(ws, 'A%d' % L_FIRMA,
              'Responsable de cocina del día (nombre y firma):', bold=True)
    for letra in ('C', 'D', 'E', 'F'):
        motor.verde(ws, letra + str(L_FIRMA))
    motor.val(ws, 'A%d' % (L_FIRMA + 1),
              'Incidencias del día:', bold=True)
    for letra in ('C', 'D', 'E', 'F', 'G', 'H', 'I'):
        motor.verde(ws, letra + str(L_FIRMA + 1))

    nota(ws, L_NOTA,
         'Temperaturas de la columna «Conservación»: mantener en caliente a '
         '63 °C o más; refrigerar a 4 °C o menos si la vida útil pasa de 24 '
         'horas y a 8 °C o menos si no llega; congelar a -18 °C o menos; y al '
         'enfriar, bajar de 60 °C a 10 °C en menos de dos horas. La norma '
         'admite otras temperaturas si el operador demuestra ante la autoridad '
         'competente que son seguras. ' + verificado('CE-10'))
    nota(ws, L_NOTA + 1,
         'Esta hoja NO sustituye a los registros del APPCC ni a la matriz de '
         'alérgenos por plato: ésos van en el «Pack APPCC». Aquí se registra '
         'cuánto se produjo y cómo se conservó.')
    nota(ws, L_NOTA + 2,
         'Se imprime en A4 vertical. Las listas de los desplegables están '
         'debajo, fuera de la zona de impresión: no las borres.')

    # --- listas de los desplegables (fuera de la zona de impresión) -------
    cabecera(ws, L_LCAB, [('A', 'Días de la semana')], altura=20)
    for i, dia in enumerate(DIAS):
        motor.val(ws, 'A%d' % (L_DIAS_INI + i), dia)
    cabecera(ws, L_CONS_CAB, [('A', 'Conservación')], altura=20)
    for i, texto in enumerate(CONSERVACION):
        motor.val(ws, 'A%d' % (L_CONS_INI + i), texto)
    cabecera(ws, L_EST_CAB, [('A', 'Estado')], altura=20)
    for i, texto in enumerate(ESTADOS):
        motor.val(ws, 'A%d' % (L_EST_INI + i), texto)

    filas = list(range(L_INI, L_FIN + 1))
    dv_rango(ws, ['B%d' % L_DIA], REF_DIAS, 'Día de la lista',
             'Elige un día de la semana de la lista que hay al final de esta '
             'hoja.')
    dv_rango(ws, ['G%d' % r for r in filas], REF_CONS, 'Conservación',
             'Elige una de las cinco formas de conservación de la lista del '
             'final de esta hoja.')
    dv_rango(ws, ['I%d' % r for r in filas], REF_EST, 'Estado',
             'Elige Producido, Pendiente o No se produce hoy.')
    motor.dv_numerica(ws, ['E%d' % r for r in filas], minimo=0, maximo=100000,
                      titulo='Raciones producidas',
                      mensaje='Raciones que se han producido de verdad.')

    ws.freeze_panes = 'A%d' % L_INI
    pagina(ws, apaisado=False, area='A1:I%d' % (L_NOTA + 2), alto=1)
    return ws


# --------------------------------------------------------------------------
# Hoja «Ajuste por Desviación»
# --------------------------------------------------------------------------
def hoja_ajuste(wb):
    ws = wb.create_sheet('Ajuste por Desviación')
    anchos(ws, {'A': 16, 'B': 14, 'C': 16, 'D': 16, 'E': 16, 'F': 16,
                'G': 30, 'H': 30, 'I': 30})
    encabezar(ws, 'Ajuste por desviación',
              nota_='Se rellena al CERRAR la semana, con lo que pasó de '
                    'verdad. Por eso viene vacía.')

    seccion(ws, 'A5', 'DESVIACIÓN DE CUBIERTOS')
    motor.val(ws, 'A%d' % A_TOL, 'Tolerancia de desviación (%)', bold=True)
    motor.verde(ws, 'B%d' % A_TOL)
    ws['B%d' % A_TOL].number_format = FMT_PCT1
    nota(ws, A_TOL + 1,
         'La tolerancia viene VACÍA y es obligatoria: mientras no escribas la '
         'tuya, la columna de desviación se queda gris. No existe ningún '
         'estándar publicado de cuánto puede desviarse una previsión de '
         'cubiertos, y este producto no se inventa ninguno: empieza mirando '
         'tus cuatro últimas semanas y ponte el número que puedas sostener.')

    cabecera(ws, A_CAB,
             [('A', 'Día'), ('B', 'Servicio'), ('C', 'Previsión'),
              ('D', 'Cubiertos reales'), ('E', 'Desviación (cubiertos)'),
              ('F', 'Desviación (%)'), ('G', 'Lectura'),
              ('H', 'Histórico para la semana que viene')], altura=44)
    for i in range(len(DIAS) * len(SERVICIOS)):
        r = A_INI + i
        pr = V_INI + i
        motor.f(ws, 'A%d' % r, mirar('%s!$A$%d' % (H_PREV, pr)))
        motor.f(ws, 'B%d' % r, mirar('%s!$B$%d' % (H_PREV, pr)))
        motor.f(ws, 'C%d' % r, mirar('%s!$F$%d' % (H_PREV, pr)), fmt=FMT_ENT)
        motor.verde(ws, 'D%d' % r)
        ws['D%d' % r].number_format = FMT_ENT
        motor.f(ws, 'E%d' % r,
                '=IF(OR(NOT(ISNUMBER($C{r})),NOT(ISNUMBER($D{r}))),"",'
                '$D{r}-$C{r})'.format(r=r), fmt=FMT_ENT)
        motor.f(ws, 'F%d' % r,
                '=IFERROR(IF(OR(NOT(ISNUMBER($E{r})),NOT(ISNUMBER($C{r})),'
                '$C{r}=0),"",$E{r}/$C{r}),"")'.format(r=r), fmt=FMT_PCT1)
        motor.f(ws, 'G%d' % r,
                '=IF(NOT(ISNUMBER($E{r})),"",IF($E{r}>0,'
                '"Por encima de lo previsto",IF($E{r}<0,'
                '"Por debajo de lo previsto","Justo en la previsión")))'
                .format(r=r))
        motor.f(ws, 'H%d' % r, mirar('$D%d' % r), fmt=FMT_ENT)
    motor.val(ws, 'A%d' % A_TOT, 'TOTAL DE LA SEMANA', bold=True)
    for letra in ('C', 'D', 'E'):
        motor.f(ws, letra + str(A_TOT),
                '=IF(COUNT({c}{a}:{c}{b})=0,"",SUM({c}{a}:{c}{b}))'
                .format(c=letra, a=A_INI, b=A_FIN), fmt=FMT_ENT, bold=True)
    motor.f(ws, 'F%d' % A_TOT,
            '=IFERROR(IF(OR(NOT(ISNUMBER($E${t})),NOT(ISNUMBER($C${t})),'
            '$C${t}=0),"",$E${t}/$C${t}),"")'.format(t=A_TOT), fmt=FMT_PCT1,
            bold=True)
    motor.f(ws, 'G%d' % A_TOT,
            '=IF(NOT(ISNUMBER($E${t})),"",IF($E${t}>0,'
            '"Por encima de lo previsto",IF($E${t}<0,'
            '"Por debajo de lo previsto","Justo en la previsión")))'
            .format(t=A_TOT), bold=True)
    fila_total(ws, A_TOT, 'A', 'H')

    nota(ws, A_TOT + 2,
         'La última columna es la que cierra el círculo: esos cubiertos reales '
         'son el histórico de la semana que viene. Cópialos a la columna '
         '«Histórico del mismo servicio» de la hoja «Previsión de Cubiertos» '
         'antes de planificar.')
    nota(ws, A_TOT + 3,
         'Una desviación aislada no dice nada. Lo que hay que mirar es el '
         'signo repetido: cuatro semanas seguidas por debajo significan que '
         'estás produciendo de más todas las semanas.')

    seccion(ws, 'A%d' % A_SEC2, 'SOBRANTE DE PRODUCCIÓN')
    cabecera(ws, A_PCAB,
             [('A', 'Id'), ('B', 'Plato'), ('C', 'Partida'),
              ('D', 'Raciones a producir previstas'),
              ('E', 'Raciones producidas'), ('F', 'Raciones vendidas'),
              ('G', 'Sobrante (raciones)'),
              ('H', 'Sobrante sobre lo producido'), ('I', 'Lectura')],
             altura=44)
    for i in range(N_PLATOS):
        r = A_PINI + i
        pr = Q_PINI + i
        motor.f(ws, 'A%d' % r, mirar('%s!$A$%d' % (H_PROD, pr)))
        motor.f(ws, 'B%d' % r, mirar('%s!$B$%d' % (H_PROD, pr)))
        motor.f(ws, 'C%d' % r, mirar('%s!$D$%d' % (H_PROD, pr)))
        motor.f(ws, 'D%d' % r, mirar('%s!$M$%d' % (H_PROD, pr)), fmt=FMT_ENT)
        for letra in ('E', 'F'):
            motor.verde(ws, letra + str(r))
            ws[letra + str(r)].number_format = FMT_ENT
        motor.f(ws, 'G%d' % r,
                '=IF(OR(NOT(ISNUMBER($E{r})),NOT(ISNUMBER($F{r}))),"",'
                '$E{r}-$F{r})'.format(r=r), fmt=FMT_ENT)
        motor.f(ws, 'H%d' % r,
                '=IFERROR(IF(OR(NOT(ISNUMBER($G{r})),NOT(ISNUMBER($E{r})),'
                '$E{r}=0),"",$G{r}/$E{r}),"")'.format(r=r), fmt=FMT_PCT1)
        motor.f(ws, 'I%d' % r,
                '=IF(NOT(ISNUMBER($G{r})),"",IF($G{r}>0,'
                '"Sobra: baja la producción de este plato",IF($G{r}<0,'
                '"Faltó: sube la producción de este plato","Ajustado")))'
                .format(r=r))
    motor.val(ws, 'A%d' % A_PTOT, 'TOTAL', bold=True)
    for letra in ('D', 'E', 'F', 'G'):
        motor.f(ws, letra + str(A_PTOT),
                '=IF(COUNT({c}{a}:{c}{b})=0,"",SUM({c}{a}:{c}{b}))'
                .format(c=letra, a=A_PINI, b=A_PFIN), fmt=FMT_ENT, bold=True)
    motor.f(ws, 'H%d' % A_PTOT,
            '=IFERROR(IF(OR(NOT(ISNUMBER($G${t})),NOT(ISNUMBER($E${t})),'
            '$E${t}=0),"",$G${t}/$E${t}),"")'.format(t=A_PTOT), fmt=FMT_PCT1,
            bold=True)
    fila_total(ws, A_PTOT, 'A', 'I')

    nota(ws, A_PTOT + 2,
         'SOBRANTE NO ES MERMA. Aquí se mide si produjiste de más; la merma '
         '(lo que se tira, en kilos, sobre lo que se produjo) se registra por '
         'partida en el cuadro de mando de cocina, que es el libro 1 de este '
         'pack. Sumar las dos cosas es contar el mismo problema dos veces.')
    nota(ws, A_PTOT + 3,
         'Antes de tirar un excedente: el orden legal de prioridades es '
         'prevenir primero y donar o redistribuir para consumo humano después, '
         'antes que destinarlo a alimentación animal o a residuo. '
         + verificado('CE-31'))
    nota(ws, A_PTOT + 4,
         'Qué hacer con cada excedente de cocina y qué se puede donar y qué no '
         'está en el capítulo de comidas testigo y banquetes del manual, y el '
         'plan de prevención del desperdicio, en el Manual del Manager.')

    # --- semáforos ---------------------------------------------------------
    rango_f = 'F%d:F%d' % (A_INI, A_TOT)
    cf_expresion(ws, rango_f,
                 '=AND(ISNUMBER($F{a}),NOT(ISNUMBER($B${t})))'
                 .format(a=A_INI, t=A_TOL), motor.CF_GRIS_BG,
                 motor.CF_GRIS_FG)
    cf_expresion(ws, rango_f,
                 '=AND(ISNUMBER($F{a}),ISNUMBER($B${t}),ABS($F{a})>$B${t})'
                 .format(a=A_INI, t=A_TOL), motor.CF_ROJO_BG,
                 motor.CF_ROJO_FG)
    cf_expresion(ws, rango_f,
                 '=AND(ISNUMBER($F{a}),ISNUMBER($B${t}),ABS($F{a})<=$B${t})'
                 .format(a=A_INI, t=A_TOL), motor.CF_VERDE_BG,
                 motor.CF_VERDE_FG)
    cf_expresion(ws, 'G%d:G%d' % (A_PINI, A_PTOT),
                 '=AND(ISNUMBER($G{a}),$G{a}>0)'.format(a=A_PINI),
                 motor.CF_ROJO_BG, motor.CF_ROJO_FG)
    cf_expresion(ws, 'G%d:G%d' % (A_PINI, A_PTOT),
                 '=AND(ISNUMBER($G{a}),$G{a}<=0)'.format(a=A_PINI),
                 motor.CF_VERDE_BG, motor.CF_VERDE_FG)

    motor.dv_porcentaje(ws, ['B%d' % A_TOL], titulo='Tolerancia',
                        prompt='Se escribe en tanto por uno: 0,10 = 10 %.')
    motor.dv_numerica(ws, ['D%d' % r for r in range(A_INI, A_FIN + 1)],
                      minimo=0, maximo=10000, titulo='Cubiertos reales',
                      mensaje='Cubiertos que se sirvieron de verdad.')
    motor.dv_numerica(ws, [c + str(r) for c in ('E', 'F')
                           for r in range(A_PINI, A_PFIN + 1)],
                      minimo=0, maximo=100000, titulo='Raciones',
                      mensaje='Raciones producidas o vendidas de ese plato.')
    ws.freeze_panes = 'C%d' % A_INI
    pagina(ws, titulos='$%d:$%d' % (A_CAB, A_CAB))
    return ws


# --------------------------------------------------------------------------
def mapa():
    """Contrato del guion: sólo celdas con VALOR.

    La hoja «Ajuste por Desviación» se entrega vacía en sus columnas de
    entrada (se rellena al cerrar la semana), así que de ella sólo se citan las
    columnas que sí traen dato: día, servicio, previsión y cantidad prevista.
    """
    celdas_v = {
        'Semana ISO que se planifica': 'B%d' % V_SEM,
        'Lunes de la semana': 'B%d' % V_LUNES,
        'Días que cubre la planificación': 'B%d' % V_DIAS,
        'Último día de la semana': 'B%d' % V_ULT,
        'Reservas confirmadas de la semana': 'C%d' % V_TOT,
        'Histórico de cubiertos de la semana': 'D%d' % V_TOT,
        'Previsión sugerida de la semana': 'E%d' % V_TOT,
        'Cubiertos previstos de la semana': 'F%d' % V_TOT,
    }
    for i, dia in enumerate(DIAS):
        for j, servicio in enumerate(SERVICIOS):
            r = V_INI + i * len(SERVICIOS) + j
            if (_sin_tildes(dia), servicio) not in PREVISION:
                continue
            etq = dia.lower() + ' · ' + servicio.lower()
            celdas_v['Reservas confirmadas del ' + etq] = 'C%d' % r
            celdas_v['Previsión de cubiertos del ' + etq] = 'F%d' % r

    celdas_q = {
        'Cubiertos previstos de la semana': 'B%d' % Q_CUB,
        'Partidas activas': 'B%d' % Q_ACT,
        'Raciones previstas de la semana (todas las partidas)':
            'G%d' % Q_PTOT,
        'Stock ya elaborado (total)': 'H%d' % Q_PTOT,
        'Raciones a producir en la semana (total)': 'M%d' % Q_PTOT,
        'Mix de venta acumulado de los platos': 'F%d' % Q_PTOT,
    }
    for i, p in enumerate(D.MIX_VENTA):
        r = Q_PINI + i
        celdas_q['Raciones previstas de ' + p['plato']] = 'G%d' % r
        celdas_q['Stock elaborado de ' + p['plato']] = 'H%d' % r
        celdas_q['Cantidad a producir de ' + p['plato']] = 'M%d' % r
    for i, (nombre, _pr, _q, _e) in enumerate(D.PARTIDAS):
        r = Q_RINI + i
        celdas_q['Raciones previstas de la partida ' + nombre] = 'B%d' % r
        celdas_q['Raciones a producir de la partida ' + nombre] = 'D%d' % r
        celdas_q['Peso de la partida ' + nombre + ' en la producción'] = \
            'E%d' % r

    celdas_l = {
        'Día de la lista de ejemplo': 'B%d' % L_DIA,
        'Fecha de la lista de ejemplo': 'B%d' % L_FECHA,
        'Cubiertos previstos del día de la lista': 'B%d' % L_CUBD,
        'Cubiertos previstos de la semana': 'B%d' % L_CUBS,
        'Raciones a producir en el día de la lista': 'D%d' % L_TOT,
    }
    for i, p in enumerate(D.MIX_VENTA):
        celdas_l['Raciones para hoy de ' + p['plato']] = 'D%d' % (L_INI + i)

    celdas_a = {
        'Previsión de cubiertos de la semana (hoja de ajuste)':
            'C%d' % A_TOT,
        'Raciones a producir previstas (hoja de ajuste)': 'D%d' % A_PTOT,
    }

    hojas = {
        'Previsión de Cubiertos': {
            'celdas': celdas_v,
            'tablas': [
                {'titulo': 'Previsión por día y servicio',
                 'cols': [['Día', 'A', 'txt'], ['Servicio', 'B', 'txt'],
                          ['Reservas confirmadas', 'C', 'num'],
                          ['Histórico del mismo servicio', 'D', 'num'],
                          ['Previsión sugerida', 'E', 'num'],
                          ['Previsión de cubiertos', 'F', 'num']],
                 'filas': [V_INI, V_TOT]},
            ],
        },
        'Producción por Partida': {
            'celdas': celdas_q,
            'tablas': [
                {'titulo': 'Producción de la semana, plato a plato',
                 'cols': [['Id', 'A', 'txt'], ['Plato', 'B', 'txt'],
                          ['Elaboración previa (mise en place)', 'C', 'txt'],
                          ['Partida', 'D', 'txt'],
                          ['Unidad de ración', 'E', 'txt'],
                          ['Mix de venta (%)', 'F', 'pct1'],
                          ['Raciones previstas', 'G', 'num'],
                          ['Stock ya elaborado', 'H', 'num'],
                          ['Cantidad a producir', 'M', 'num'],
                          ['Alerta', 'N', 'txt']],
                 'filas': [Q_PINI, Q_PINI + len(D.MIX_VENTA) - 1]},
                {'titulo': 'Resumen por partida',
                 'cols': [['Partida', 'A', 'txt'],
                          ['Raciones previstas', 'B', 'num'],
                          ['Stock ya elaborado', 'C', 'num'],
                          ['Raciones a producir', 'D', 'num'],
                          ['Peso sobre lo que hay que producir', 'E', 'pct1']],
                 'filas': [Q_RINI, Q_RTOT]},
            ],
        },
        'Lista de Producción Diaria': {
            'celdas': celdas_l,
            'tablas': [
                {'titulo': 'Lista de producción diaria (imprimible)',
                 'cols': [['Partida', 'A', 'txt'],
                          ['Elaboración', 'B', 'txt'],
                          ['Unidad de ración', 'C', 'txt'],
                          ['Raciones para hoy', 'D', 'num']],
                 'filas': [L_INI, L_INI + len(D.MIX_VENTA) - 1]},
            ],
        },
        'Ajuste por Desviación': {
            'celdas': celdas_a,
            'tablas': [],
        },
    }
    referencias = {}
    for hoja, cont in hojas.items():
        for desc, coord in cont['celdas'].items():
            referencias[hoja + ' · ' + desc] = hoja + '!' + coord
    return {
        'fichero': NOMBRE + '.xlsx',
        'producto': PID,
        'semana_tipo': SEMANA,
        'lunes_semana_tipo': LUNES.isoformat(),
        'hojas': hojas,
        'referencias': referencias,
    }


def main():
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_prevision(wb)
    hoja_produccion(wb)
    hoja_lista(wb)
    hoja_ajuste(wb)

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
        json.dump(mapa(), fh, ensure_ascii=False, indent=1)
    print('escrito:', ruta)
    print('formulas registradas:', len(motor.REGISTRO))


if __name__ == '__main__':
    main()
