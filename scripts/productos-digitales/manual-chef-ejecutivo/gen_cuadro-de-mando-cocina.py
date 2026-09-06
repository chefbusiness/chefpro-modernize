#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_cuadro-de-mando-cocina.py — libro 1 de «Manual del Chef Ejecutivo»
(SPEC §2.2 fila 1; decisiones D4, D6, D7, D8, D9 y D10).

Hojas: Instrucciones · Parámetros · Semana (52 filas ISO) · KPI y Definiciones ·
Comparativa entre Unidades.

QUÉ MIDE Y POR QUÉ NO DUPLICA AL CUADRO DEL MANUAL DEL MANAGER
--------------------------------------------------------------
`manual-manager-restaurante/cuadro-de-mando-semanal-manager.xlsx` mide el
DINERO de la semana (ventas, food cost, labor cost, prime cost). Éste mide la
COCINA de la misma semana: merma por partida, producción, tiempo de pase,
incidencias de alérgenos, horas de cocina y platos devueltos. Por eso este libro
NO tiene ni una sola columna financiera (SPEC §2.2, regla de no-solape): cuando
el prime cost se sale de objetivo, el del Manager dice CUÁNTO y éste dice EN QUÉ
PARTIDA.

DECISIONES TÉCNICAS
-------------------
* D7 — «Partidas activas (3-8)»: una celda verde de `Parámetros` gobierna los
  encabezados de las 8 columnas de partida por `INDEX` sobre la lista, NUNCA por
  `INDIRECT` (prohibida). Las columnas de las partidas que no existen se quedan
  sin encabezado y sin dato, y el semáforo las ignora por `ISNUMBER`.
* D10 — el semáforo NO se enciende sin objetivo propio: las reglas llevan
  `ISNUMBER` sobre el valor **y sobre el objetivo**, y la primera regla (gris)
  se queda con la celda mientras el objetivo esté vacío. Este producto no
  publica ningún benchmark de merma, de pase ni de horas: los KPI se miden.
* D6 — «Comparativa entre Unidades»: la fila de la unidad de referencia se
  CALCULA desde la hoja «Semana» filtrando por el mes cerrado (`SUMIF` sobre la
  columna «Mes»); las otras cinco se teclean copiando del libro de cada cocina.
  Cero fórmulas entre ficheros (D4).
* D8 — el contrato con el Manual del Manager va escrito en «Instrucciones»:
  qué se copia de dónde y qué NO hay que volver a teclear.
* Cero constantes dentro de una fórmula: hasta la base de las tasas («por cada
  1.000 cubiertos») es una celda verde de `Parámetros`.
* Prohibidas `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA`,
  `RANK` y `NETWORKDAYS`: cero usos. El ranking se hace con `SUMPRODUCT`.
* `IFERROR(...,"")` en todo cociente, «sin dato» = `""` nunca 0, textos 100 %
  WinAnsi (cp1252): ni «≤», ni «≥», ni el espacio fino U+202F.

Salida fija: build/cuadro-de-mando-cocina.xlsx + build/mapa-cuadro-de-mando-cocina.json
"""
import json
import os
import sys

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
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
TITULO = 'Cuadro de mando de cocina'
NOMBRE = 'cuadro-de-mando-cocina'
PID = 'manual-chef-ejecutivo'

FMT_PCT = motor.FMT_PCT
FMT_ENT = motor.FMT_ENT
FMT_FECHA = motor.FMT_FECHA
FMT_DEC1 = '#,##0.0'          # minutos de pase, tasas por mil
FMT_DEC2 = '#,##0.00'         # kg de merma
FMT_DEC3 = '#,##0.000'        # horas de cocina por cubierto
FMT_PCT1 = '0.0%'

GRIS = 'F2F2F2'
CREMA = 'FFF6DC'
ORO = 'FFD700'
CABECERA = '2D2D2D'

FECHA_VERIF = '06-09-2026'


# --------------------------------------------------------------------------
def sector(idd):
    """Devuelve la entrada del id `CE-*` / `CS-*` / `MM-*` del JSON de research.

    Regla de familia: ninguna cifra ni ninguna norma se teclea en el generador.
    Se lee del JSON, que lleva fuente, URL y fiabilidad.
    """
    ruta = os.path.join(RAIZ, 'auditorias', 'guias-v2-research-sector.json')
    with open(ruta, encoding='utf-8') as fh:
        datos = json.load(fh)['datos']
    for it in datos:
        if it.get('id') == idd:
            return it
    raise KeyError('id de research inexistente: ' + idd)


def verificado(idd):
    """Nota de familia: «Verificado el <fecha> · norma · URL» (SPEC §2.2)."""
    it = sector(idd)
    return ('Verificado el ' + FECHA_VERIF + ' · ' + it['fuente_titulo']
            + ' · ' + it['url'])


CE06 = sector('CE-06')      # alérgenos: declaración obligatoria
CE01 = sector('CE-01')      # alérgenos: contaminación cruzada (punto 9, Cap. IX)
JORN02 = sector('JORN-02')  # registro de jornada: art. 34.9 ET

OBJ = D.PARAMETROS_COCINA['objetivos']
KGR = D.PARAMETROS_COCINA['kg_racion']

#: Ranuras de partida del libro (SPEC D7: de 3 a 8). El caso modelado declara
#: SEIS; las dos últimas quedan vacías para quien tenga más.
N_RANURAS = 8
PARTIDAS_ACTIVAS = D.PARAMETROS_COCINA['partidas_activas']
BASE_TASAS = 1000.0

# --- filas de la hoja «Parámetros» ---------------------------------------
P_NOMBRE = 5
P_CARTA = 6
P_ACT = 7
P_BASE = 8
P_SEC_PART = 13
P_PCAB = 14
P_PINI = 15
P_PFIN = P_PINI + N_RANURAS - 1                 # 22
P_SEC_OBJ = 27
P_OCAB = 28
P_O_PASE_E = 29
P_O_PASE_P = 30
P_O_PASE_D = 31
P_O_INCID = 32
P_O_HORAS = 33
P_O_DEVUE = 34
P_O_RETRA = 35
P_O_SUMA = 36
P_SEC_LIS = 42
P_LCAB = 43
P_LINI = 44
P_LFIN = P_LINI + len(D.PARAMETROS_COCINA['tipos_carta_lista']) - 1   # 48
P_SNCAB = 50
P_SNINI = 51
P_SNFIN = 52

REF_PARTIDAS = "'Parámetros'!$A$%d:$A$%d" % (P_PINI, P_PFIN)
IDX_NOMBRE = 'Parámetros!$A$%d:$A$%d' % (P_PINI, P_PFIN)
IDX_KG = 'Parámetros!$C$%d:$C$%d' % (P_PINI, P_PFIN)
IDX_OBJ = 'Parámetros!$D$%d:$D$%d' % (P_PINI, P_PFIN)
REF_CARTA = "'Parámetros'!$A$%d:$A$%d" % (P_LINI, P_LFIN)
REF_SINO = "'Parámetros'!$A$%d:$A$%d" % (P_SNINI, P_SNFIN)

# --- filas de la hoja «Semana» -------------------------------------------
S_CAB, S_INI = 4, 5
S_FIN = S_INI + len(D.SEMANA_COCINA) - 1        # 56
S_TOT = S_FIN + 1                               # 57
E_TIT = S_TOT + 3                               # 60
E_NOM = E_TIT + 1                               # 61 · nombre de cada partida
E_KG = E_TIT + 2                                # 62 · kg por ración
E_OBJ = E_TIT + 3                               # 63 · objetivos de la casa
E_BASE = E_TIT + 4                              # 64 · base de las tasas
E_ACT = E_TIT + 5                               # 65 · partidas activas

# --- filas de la hoja «KPI y Definiciones» -------------------------------
K_CAB, K_INI = 4, 5
K_FIN = K_INI + len(D.KPI_COCINA) - 1

# --- filas de la hoja «Comparativa entre Unidades» -----------------------
N_UNIDADES = 6
C_MES = 5
C_ANIO = 6
C_BASE = 7
C_SEC_EST = 10
C_ECAB = 11
C_EST = 12                                       # fila del estándar del grupo
C_SEC_UNI = 15
C_UCAB = 16
C_UINI = 17
C_UFIN = C_UINI + N_UNIDADES - 1                 # 22


# --------------------------------------------------------------------------
# Columnas de la hoja «Semana»
# --------------------------------------------------------------------------
def _letras(inicio, cuantas):
    return [get_column_letter(inicio + i) for i in range(cuantas)]


COL_SEM = 'A'
COL_LUNES = 'B'
COL_MES = 'C'
COL_CUB = 'D'
COLS_PROD = _letras(5, N_RANURAS)                # E..L
COL_RACIONES = get_column_letter(5 + N_RANURAS)  # M
COLS_MERMA = _letras(6 + N_RANURAS, N_RANURAS)   # N..U
COL_MERMA_TOT = get_column_letter(6 + 2 * N_RANURAS)          # V
COLS_PCT = _letras(7 + 2 * N_RANURAS, N_RANURAS)              # W..AD
_sig = 7 + 3 * N_RANURAS                                       # 31 -> AE
COL_KG_PROD = get_column_letter(_sig)            # AE
COL_MERMA_GLB = get_column_letter(_sig + 1)      # AF
COL_PASE_E = get_column_letter(_sig + 2)         # AG
COL_PASE_P = get_column_letter(_sig + 3)         # AH
COL_PASE_D = get_column_letter(_sig + 4)         # AI
COL_INCID = get_column_letter(_sig + 5)          # AJ
COL_GRAV = get_column_letter(_sig + 6)           # AK
COL_INCID_T = get_column_letter(_sig + 7)        # AL
COL_HORAS = get_column_letter(_sig + 8)          # AM
COL_HORAS_C = get_column_letter(_sig + 9)        # AN
COL_DEVUE = get_column_letter(_sig + 10)         # AO
COL_RETRA = get_column_letter(_sig + 11)         # AP
COL_DR_T = get_column_letter(_sig + 12)          # AQ
COL_NFUERA = get_column_letter(_sig + 13)        # AR
COL_LECTURA = get_column_letter(_sig + 14)       # AS
COL_ULTIMA = COL_LECTURA
COL_ESPEJO = COL_RACIONES     # columna de los espejos escalares (M)


# --------------------------------------------------------------------------
# Utilidades de formato (mismo molde que el libro 1 del Manual del Manager)
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


def estilo_cabecera(ws, fila, letras, altura=44):
    """Pinta de cabecera unas columnas cuyo valor ya está escrito (fórmula)."""
    for letra in letras:
        c = ws[letra + str(fila)]
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


def semaforo_con_objetivo(ws, rango, col_valor, fila_ini, col_obj, fila_obj):
    """Semáforo de la SPEC D10, en tres reglas y por este orden:

    1. GRIS  si hay valor pero NO hay objetivo (la casa todavía no lo ha
       fijado): el libro no dice «bien» ni «mal» sin que alguien decida qué es
       bien y qué es mal.
    2. ROJO  si el valor supera el objetivo.
    3. VERDE si lo cumple.

    Las tres llevan `ISNUMBER` sobre el valor Y sobre el objetivo: sin esa
    guarda, Excel lee `""` como texto, que ordena por encima de cualquier
    número, y pintaría de rojo justo la celda que dice que no hay dato.
    """
    v = '%s%d' % (col_valor, fila_ini)
    o = '%s$%d' % (col_obj, fila_obj)
    cf_expresion(ws, rango,
                 '=AND(ISNUMBER(%s),NOT(ISNUMBER(%s)))' % (v, o),
                 motor.CF_GRIS_BG, motor.CF_GRIS_FG)
    cf_expresion(ws, rango,
                 '=AND(ISNUMBER(%s),ISNUMBER(%s),%s>%s)' % (v, o, v, o),
                 motor.CF_ROJO_BG, motor.CF_ROJO_FG)
    cf_expresion(ws, rango,
                 '=AND(ISNUMBER(%s),ISNUMBER(%s),%s<=%s)' % (v, o, v, o),
                 motor.CF_VERDE_BG, motor.CF_VERDE_FG)


def pagina(ws, apaisado=True, titulos=None, area=None):
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
    """Nota al pie de una sección; sin `wrap` se derrama sobre las celdas
    vacías de la derecha, que es como se leen en las hojas anchas."""
    motor.val(ws, col + str(fila), texto, wrap=wrap)
    if alto:
        ws.row_dimensions[fila].height = alto


def dv_rango(ws, coords, ref, titulo, mensaje):
    """Desplegable contra un RANGO (convención de familia: nunca lista con
    comas, que se rompe en cuanto una opción lleva una coma y tiene tope de
    255 caracteres)."""
    dv = DataValidation(type='list', formula1=ref, allow_blank=True,
                        showErrorMessage=True, errorTitle=titulo,
                        error=mensaje)
    ws.add_data_validation(dv)
    for c in coords:
        dv.add(c)
    return dv


def mirar(ref, fmt_cero=False):
    """Espejo de una celda de otra hoja del MISMO fichero, con «sin dato» = "".

    (El formato condicional no puede referirse a otra hoja, así que los
    objetivos se espejan en la propia hoja «Semana».)
    """
    if fmt_cero:
        return '=IF({r}="","",IF({r}=0,"",{r}))'.format(r=ref)
    return '=IF({r}="","",{r})'.format(r=ref)


# --------------------------------------------------------------------------
# Hoja «Instrucciones»
# --------------------------------------------------------------------------
PASOS = [
    '1. Hoja «Parámetros»: escribe el nombre de tu cocina, elige el tipo de '
    'carta y di cuántas partidas (estaciones, en el vocabulario de la matriz '
    'de polivalencia del Manual del Manager) tienes activas. Ese número, de '
    '3 a 8, es el que enciende las columnas de la hoja «Semana»: si pones 4, '
    'las columnas 5 a 8 se quedan sin encabezado y dejan de avisarte, aunque '
    'los totales siguen sumando lo que quede escrito en ellas.',
    '2. En la misma hoja, escribe el nombre de cada partida, si produce '
    'raciones, cuántos kilos de materia prima neta lleva una ración media de '
    'esa partida y el objetivo de merma que TÚ te pones. Los kilos por ración '
    'son lo que convierte la merma (en kg) y la producción (en raciones) en un '
    'porcentaje comparable entre partidas.',
    '3. Debajo están los demás objetivos de la casa: tiempos de pase, '
    'incidencias de alérgenos, horas de cocina por cubierto y platos '
    'devueltos y retrabajados. Son celdas verdes y son OBLIGATORIAS: mientras '
    'una esté vacía, su semáforo se queda GRIS. Este libro no trae ningún '
    'objetivo de referencia del sector porque no existe ninguno publicado.',
    '4. Hoja «Semana»: una fila por semana ISO. Rellena las celdas verdes con '
    'lo que registres en cocina: cubiertos, raciones producidas por partida, '
    'kilos de merma por partida, tiempos de pase muestreados, incidencias de '
    'alérgenos, horas de cocina trabajadas y platos devueltos y retrabajados.',
    '5. Las columnas grises las calcula el libro: la merma de cada partida en '
    'porcentaje, la merma global, las tasas por cubiertos y el recuento de '
    'indicadores fuera de objetivo. La última columna te lo dice con palabras.',
    '6. Hoja «KPI y Definiciones»: qué mide cada indicador, cómo se calcula, '
    'con qué cadencia y cuál es el error típico. Es la hoja que se consulta '
    'cuando dos personas dan dos números distintos para lo mismo.',
    '7. Hoja «Comparativa entre Unidades»: si diriges varias cocinas, elige el '
    'mes cerrado que quieres comparar. La primera fila es TU cocina y la '
    'calcula el libro desde la hoja «Semana»; las otras cinco las tecleas tú '
    'copiando de la hoja «Semana» del libro de cada unidad.',
    '8. Cadencia de uso: este libro se rellena UNA VEZ POR SEMANA, al cerrar la '
    'semana, y se lee en la reunión de cocina de la semana siguiente. La '
    'comparativa entre unidades, una vez al mes.',
]

NOTAS_LIBRO = [
    'ESTE LIBRO NO LLEVA NI UNA COLUMNA DE DINERO, y es a propósito. Las '
    'ventas, el food cost, el labor cost y el prime cost de la misma semana '
    'están en el cuadro de mando semanal del «Manual del Manager de '
    'Restaurante». Aquel dice CUÁNTO se ha ido; éste dice EN QUÉ PARTIDA.',
    'La merma que se mide aquí es la merma AGREGADA de cada partida contra lo '
    'que esa partida ha producido. El rendimiento de un ingrediente concreto '
    '(cuánto queda de un lomo después de limpiarlo) vive en la «Guía Food Cost '
    '+ Ingeniería de Menú», y la merma por producto y la recepción, en el «Kit '
    'de Inventario». No son lo mismo y no se suman.',
    'Los objetivos de este libro son TUYOS. No existe un estándar publicado de '
    'KPI de cocina en español: ésta es nuestra lista de indicadores y el '
    'porqué de cada uno, pero el número contra el que te mides lo pones tú, '
    'con tu carta, tu equipo y tu temporada. Mientras la celda del objetivo '
    'esté vacía, el semáforo se queda gris.',
    'La semana ISO empieza en lunes y la semana 1 del año es la que contiene el '
    'primer jueves de enero. Por eso la semana 1 de 2026 arranca el lunes 29 de '
    'diciembre de 2025: es la convención, no una errata.',
    'La columna «Mes» sirve para cerrar el mes en la comparativa entre '
    'unidades. La convención es asignar la semana al mes de su JUEVES, que es '
    'la que usa la norma ISO; por eso la semana 14 de 2026 (lunes 30 de marzo) '
    'cuenta como abril.',
    'Un dato que falta se deja EN BLANCO, nunca a cero: un cero es una medida '
    '(«esta semana no hubo ninguna incidencia») y un blanco es la ausencia de '
    'medida. El libro los trata distinto y los semáforos ignoran los blancos.',
]


def hoja_instrucciones(wb):
    ws = wb.create_sheet('Instrucciones', 0)
    anchos(ws, {'A': 38, 'B': 52, 'C': 52})
    motor.val(ws, 'A1', TITULO)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', SUBTITULO)
    motor.val(ws, 'A3', 'Para qué sirve: saber qué partida se está comiendo el '
                        'margen mientras todavía puedes hacer algo con ella.')
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

    # --- contrato con el Manual del Manager (SPEC D8) ---------------------
    seccion(ws, 'A%d' % fila,
            'Qué se copia de dónde (y qué NO hay que volver a teclear)')
    fila += 1
    cabecera(ws, fila, [('A', 'Producto'), ('B', 'Qué te da'),
                        ('C', 'Qué no hay que volver a teclear')], altura=32)
    fila += 1
    for producto, da, no_teclear in D.CONTRATO_ENTRE_MANUALES:
        motor.val(ws, 'A%d' % fila, producto, bold=True, wrap=True)
        motor.val(ws, 'B%d' % fila, da, wrap=True)
        motor.val(ws, 'C%d' % fila, no_teclear, wrap=True)
        ws.row_dimensions[fila].height = 58
        fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    nota(ws, fila,
         'Es una COPIA declarada, no un vínculo: ningún libro de este pack lee '
         'una celda de otro fichero. Si mañana mueves un fichero de carpeta, '
         'nada se rompe.', alto=30, wrap=True)
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
# Hoja «Parámetros»
# --------------------------------------------------------------------------
def hoja_parametros(wb):
    ws = wb.create_sheet('Parámetros')
    anchos(ws, {'A': 38, 'B': 20, 'C': 24, 'D': 26, 'E': 58, 'F': 76})
    encabezar(ws, 'Parámetros del cuadro de mando de cocina',
              nota_='Todas las celdas verdes son tuyas. Los objetivos son '
                    'criterio de la casa, no un estándar del sector.')

    seccion(ws, 'A4', 'IDENTIFICACIÓN Y ESCALA')
    motor.val(ws, 'A%d' % P_NOMBRE, 'Nombre de la cocina o unidad', bold=True)
    motor.val(ws, 'B%d' % P_NOMBRE, D.RESTAURANTE['nombre'], verde_=True)
    motor.val(ws, 'A%d' % P_CARTA, 'Tipo de carta', bold=True)
    motor.val(ws, 'B%d' % P_CARTA, D.PARAMETROS_COCINA['tipo_carta'],
              verde_=True)
    motor.val(ws, 'A%d' % P_ACT, 'Partidas activas (de 3 a 8)', bold=True)
    motor.val(ws, 'B%d' % P_ACT, PARTIDAS_ACTIVAS, fmt=FMT_ENT, verde_=True)
    motor.val(ws, 'A%d' % P_BASE,
              'Base de las tasas por cubiertos', bold=True)
    motor.val(ws, 'B%d' % P_BASE, BASE_TASAS, fmt=FMT_ENT, verde_=True)

    nota(ws, 9,
         'Las partidas activas gobiernan los encabezados de la hoja «Semana»: '
         'si escribes 4, las columnas de la 5.ª a la 8.ª partida se quedan sin '
         'encabezado y sin semáforo. La lista de abajo es la que da el nombre '
         'a cada columna.')
    nota(ws, 10,
         'La base de las tasas es el número de cubiertos sobre el que se '
         'expresan las incidencias de alérgenos y los platos devueltos y '
         'retrabajados. Viene en 1.000 cubiertos; si tu cocina es pequeña y '
         'prefieres leerlo por cada 100, cámbialo aquí y se recalcula toda la '
         'hoja «Semana». Los objetivos de más abajo van en esta misma base.')
    nota(ws, 11,
         'El nombre de la cocina es el que aparece como unidad de referencia '
         'en la hoja «Comparativa entre Unidades».')

    # --- las partidas ------------------------------------------------------
    seccion(ws, 'A%d' % P_SEC_PART, 'LAS PARTIDAS DE TU COCINA')
    cabecera(ws, P_PCAB,
             [('A', 'Partida'), ('B', '¿Produce raciones?'),
              ('C', 'Kg de materia prima neta por ración'),
              ('D', 'Objetivo de merma (%)'),
              ('E', 'Qué produce')], altura=46)
    for i in range(N_RANURAS):
        r = P_PINI + i
        if i < len(D.PARTIDAS):
            nombre, produce, que, _equiv = D.PARTIDAS[i]
            motor.val(ws, 'A%d' % r, nombre, verde_=True)
            motor.val(ws, 'B%d' % r, 'Sí' if produce else 'No', verde_=True,
                      align='center')
            if produce:
                motor.val(ws, 'C%d' % r, KGR[nombre], fmt=FMT_DEC2,
                          verde_=True)
                motor.val(ws, 'D%d' % r, OBJ['merma_' + nombre], fmt=FMT_PCT1,
                          verde_=True)
            else:
                motor.verde(ws, 'C%d' % r)
                motor.verde(ws, 'D%d' % r)
                ws['C%d' % r].number_format = FMT_DEC2
                ws['D%d' % r].number_format = FMT_PCT1
            motor.val(ws, 'E%d' % r, que, verde_=True, wrap=True)
            ws.row_dimensions[r].height = 30
        else:
            for letra, fmt in (('A', None), ('B', None), ('C', FMT_DEC2),
                               ('D', FMT_PCT1), ('E', None)):
                motor.verde(ws, letra + str(r))
                if fmt:
                    ws[letra + str(r)].number_format = fmt

    nota(ws, P_PFIN + 1,
         'Las dos últimas filas están libres: son las ranuras 7 y 8, para '
         'cocinas con más partidas. Escribe el nombre y sube «partidas '
         'activas» a 7 u 8.')
    nota(ws, P_PFIN + 2,
         'Una partida que no produce raciones (sala, caja, barra sin '
         'elaboración) se deja con «No» y sin kilos por ración: su columna de '
         'la hoja «Semana» se queda en blanco y el semáforo la ignora. '
         'Existe en la lista porque es una partida de tu organigrama, aunque '
         'no produzca.')
    nota(ws, P_PFIN + 3,
         'Los kilos por ración son de MATERIA PRIMA NETA y son una media de la '
         'partida, no de un plato. Se miden una vez, pesando lo que entra en '
         'una ración media de esa partida, y se revisan al cambiar la carta.')

    # --- objetivos de la casa ---------------------------------------------
    seccion(ws, 'A%d' % P_SEC_OBJ, 'OBJETIVOS DE LA CASA (los demás indicadores)')
    cabecera(ws, P_OCAB, [('A', 'Indicador'), ('B', 'Objetivo'),
                          ('C', 'Unidad'), ('D', 'Cómo se lee')], altura=32)
    ws.merge_cells('D%d:E%d' % (P_OCAB, P_OCAB))
    objetivos = [
        (P_O_PASE_E, 'Tiempo de pase de entrantes',
         OBJ['pase_entrantes_min'], FMT_DEC1, 'minutos',
         'Media de los muestreos de la semana, de la comanda a la salida.'),
        (P_O_PASE_P, 'Tiempo de pase de principales',
         OBJ['pase_principales_min'], FMT_DEC1, 'minutos',
         'Un arroz y un postre no compiten en la misma liga: por eso hay tres '
         'objetivos y no una media de carta.'),
        (P_O_PASE_D, 'Tiempo de pase de postres',
         OBJ['pase_postres_min'], FMT_DEC1, 'minutos',
         'Se mide igual que los otros dos, y casi siempre es el que más se '
         'descuida.'),
        (P_O_INCID, 'Incidencias de alérgenos por base de cubiertos',
         OBJ['incidencias_alergenos_1000'], FMT_DEC1, 'incidencias',
         'Cuenta también la que se detecta en el pase y no llega al cliente: '
         'ésa es la que te enseña dónde falla el proceso.'),
        (P_O_HORAS, 'Horas de cocina por cubierto',
         OBJ['horas_cocina_cubierto'], FMT_DEC3, 'horas',
         'Horas del registro de jornada de la brigada, no las del contrato, y '
         'sin meter dentro las de sala.'),
        (P_O_DEVUE, 'Platos devueltos por base de cubiertos',
         OBJ['devueltos_1000'], FMT_DEC1, 'platos',
         'El plato que vuelve de la mesa.'),
        (P_O_RETRA, 'Platos retrabajados por base de cubiertos',
         OBJ['retrabajados_1000'], FMT_DEC1, 'platos',
         'El plato que se rehace ANTES de salir. No se ve en ninguna cuenta y '
         'suele ser el que más dinero cuesta.'),
    ]
    for r, etiqueta, valor, fmt, unidad, lectura in objetivos:
        motor.val(ws, 'A%d' % r, etiqueta, bold=True, wrap=True)
        motor.val(ws, 'B%d' % r, valor, fmt=fmt, verde_=True)
        motor.val(ws, 'C%d' % r, unidad, align='center')
        ws.merge_cells('D%d:E%d' % (r, r))
        motor.val(ws, 'D%d' % r, lectura, wrap=True)
        ws.row_dimensions[r].height = 32
    motor.val(ws, 'A%d' % P_O_SUMA,
              'Platos devueltos y retrabajados (objetivo conjunto)', bold=True,
              wrap=True)
    motor.f(ws, 'B%d' % P_O_SUMA,
            '=IFERROR(IF(OR($B${a}="",$B${b}=""),"",$B${a}+$B${b}),"")'
            .format(a=P_O_DEVUE, b=P_O_RETRA), fmt=FMT_DEC1)
    ws['B%d' % P_O_SUMA].fill = PatternFill('solid', fgColor=GRIS)
    motor.val(ws, 'C%d' % P_O_SUMA, 'platos', align='center')
    ws.merge_cells('D%d:E%d' % (P_O_SUMA, P_O_SUMA))
    motor.val(ws, 'D%d' % P_O_SUMA,
              'Lo calcula el libro sumando los dos de arriba: es el que '
              'gobierna el semáforo de la hoja «Semana».', wrap=True)
    ws.row_dimensions[P_O_SUMA].height = 32

    nota(ws, P_O_SUMA + 1,
         'ESTOS OBJETIVOS SON DE LA CASA. No existe un estándar publicado de '
         'KPI de cocina en español, y este producto no cita ninguno: los '
         'números que ves son los del restaurante de ejemplo con el que está '
         'montado el pack. Cámbialos por los tuyos antes de leer un solo '
         'semáforo.')
    nota(ws, P_O_SUMA + 2,
         'Si borras un objetivo, su semáforo se queda GRIS en vez de verde o '
         'rojo. Es deliberado: el libro no dice «bien» ni «mal» mientras nadie '
         'haya decidido qué es bien y qué es mal en esta casa.')
    nota(ws, P_O_SUMA + 3,
         'Qué cuenta como incidencia de alérgenos: cualquier fallo en la '
         'declaración al cliente o en la separación de un alérgeno del Anexo '
         'II del Reglamento 1169/2011, se haya servido el plato o no. El '
         'cartel de «consulte al personal» no basta por sí solo: hace falta '
         'soporte escrito o electrónico accesible. ' + verificado('CE-06'))
    nota(ws, P_O_SUMA + 4,
         'Y también cuenta el utensilio o el recipiente que se ha usado con un '
         'alérgeno y se reutiliza sin limpieza comprobada: no es un capítulo '
         'propio de alérgenos, es el punto 9 del Capítulo IX del Anexo II del '
         'Reglamento 852/2004. ' + verificado('CE-01'))
    nota(ws, P_O_SUMA + 5,
         'Las horas de cocina salen del registro diario de jornada, que es '
         'obligatorio para toda la plantilla y se conserva cuatro años. '
         + verificado('JORN-02'))

    # --- listas de los desplegables ---------------------------------------
    seccion(ws, 'A%d' % P_SEC_LIS,
            'LISTAS DE LOS DESPLEGABLES (no borres estas celdas)')
    cabecera(ws, P_LCAB, [('A', 'Tipos de carta')], altura=20)
    for i, tipo in enumerate(D.PARAMETROS_COCINA['tipos_carta_lista']):
        motor.val(ws, 'A%d' % (P_LINI + i), tipo)
    cabecera(ws, P_SNCAB, [('A', 'Sí / No')], altura=20)
    motor.val(ws, 'A%d' % P_SNINI, 'Sí')
    motor.val(ws, 'A%d' % P_SNFIN, 'No')
    nota(ws, P_SNFIN + 2,
         'Los desplegables de este libro leen estas dos listas. Puedes '
         'ampliarlas: si añades un tipo de carta, amplía también el rango del '
         'desplegable (Datos > Validación de datos).')

    # --- validaciones ------------------------------------------------------
    dv_rango(ws, ['B%d' % P_CARTA], REF_CARTA, 'Tipo de carta',
             'Elige un tipo de carta de la lista de la parte de abajo de esta '
             'hoja.')
    dv_rango(ws, ['B%d' % r for r in range(P_PINI, P_PFIN + 1)], REF_SINO,
             '¿Produce raciones?',
             'Escribe Sí o No (la lista está en la parte de abajo de esta '
             'hoja).')
    motor.dv_numerica(ws, ['B%d' % P_ACT], minimo=3, maximo=N_RANURAS,
                      titulo='Partidas activas',
                      mensaje='Un número entre 3 y 8.')
    motor.dv_numerica(ws, ['B%d' % P_BASE], minimo=1, maximo=100000,
                      titulo='Base de las tasas',
                      mensaje='Número de cubiertos sobre el que se expresan '
                              'las tasas (por ejemplo 1.000).')
    motor.dv_numerica(ws, ['C%d' % r for r in range(P_PINI, P_PFIN + 1)],
                      minimo=0, maximo=10, titulo='Kg por ración',
                      mensaje='Kilos de materia prima neta de una ración '
                              'media de esa partida.')
    motor.dv_porcentaje(ws, ['D%d' % r for r in range(P_PINI, P_PFIN + 1)],
                        titulo='Objetivo de merma',
                        prompt='Se escribe en tanto por uno: 0,055 = 5,5 %.')
    motor.dv_numerica(ws, ['B%d' % r for r in (P_O_PASE_E, P_O_PASE_P,
                                               P_O_PASE_D)],
                      minimo=0, maximo=240, titulo='Minutos',
                      mensaje='Minutos desde la comanda hasta la salida.')
    motor.dv_numerica(ws, ['B%d' % r for r in (P_O_INCID, P_O_DEVUE,
                                               P_O_RETRA)],
                      minimo=0, maximo=100000, titulo='Tasa por cubiertos',
                      mensaje='En la misma base de cubiertos que has fijado '
                              'arriba.')
    motor.dv_numerica(ws, ['B%d' % P_O_HORAS], minimo=0, maximo=24,
                      titulo='Horas por cubierto',
                      mensaje='Horas de cocina por cada cubierto servido.')
    pagina(ws, apaisado=False)
    return ws


# --------------------------------------------------------------------------
# Hoja «Semana»
# --------------------------------------------------------------------------
def _cols_semana():
    """(letra, encabezado, tipo) de las 45 columnas, en orden."""
    cols = [(COL_SEM, 'Semana ISO', 'ent'),
            (COL_LUNES, 'Lunes de la semana', 'fecha'),
            (COL_MES, 'Mes', 'ent'),
            (COL_CUB, 'Cubiertos servidos', 'ent')]
    for i, letra in enumerate(COLS_PROD):
        cols.append((letra, 'Producción partida %d (raciones)' % (i + 1),
                     'ent'))
    cols.append((COL_RACIONES, 'Raciones producidas (total)', 'ent'))
    for i, letra in enumerate(COLS_MERMA):
        cols.append((letra, 'Merma partida %d (kg)' % (i + 1), 'dec2'))
    cols.append((COL_MERMA_TOT, 'Merma total (kg)', 'dec2'))
    for i, letra in enumerate(COLS_PCT):
        cols.append((letra, 'Merma partida %d (%%)' % (i + 1), 'pct'))
    cols += [
        (COL_KG_PROD, 'Materia prima producida (kg)', 'dec2'),
        (COL_MERMA_GLB, 'Merma global de la cocina (%)', 'pct'),
        (COL_PASE_E, 'Pase de entrantes (min)', 'dec1'),
        (COL_PASE_P, 'Pase de principales (min)', 'dec1'),
        (COL_PASE_D, 'Pase de postres (min)', 'dec1'),
        (COL_INCID, 'Incidencias de alérgenos', 'ent'),
        (COL_GRAV, 'Gravedad máxima (0 a 3)', 'ent'),
        (COL_INCID_T, 'Incidencias por base de cubiertos', 'dec1'),
        (COL_HORAS, 'Horas de cocina trabajadas', 'ent'),
        (COL_HORAS_C, 'Horas de cocina por cubierto', 'dec3'),
        (COL_DEVUE, 'Platos devueltos', 'ent'),
        (COL_RETRA, 'Platos retrabajados', 'ent'),
        (COL_DR_T, 'Devueltos y retrabajados por base', 'dec1'),
        (COL_NFUERA, 'Indicadores fuera de objetivo', 'ent'),
        (COL_LECTURA, 'Lectura de la semana', 'txt'),
    ]
    return cols


FORMATO = {'pct': FMT_PCT1, 'ent': FMT_ENT, 'fecha': FMT_FECHA,
           'dec1': FMT_DEC1, 'dec2': FMT_DEC2, 'dec3': FMT_DEC3, 'txt': None}

#: columnas de ENTRADA (celda verde) de la hoja «Semana»
VERDES_SEMANA = ([COL_SEM, COL_LUNES, COL_MES, COL_CUB] + COLS_PROD
                 + COLS_MERMA + [COL_PASE_E, COL_PASE_P, COL_PASE_D,
                                 COL_INCID, COL_GRAV, COL_HORAS, COL_DEVUE,
                                 COL_RETRA])
#: columnas que se SUMAN en la fila de totales
SUMABLES = ([COL_CUB] + COLS_PROD + [COL_RACIONES] + COLS_MERMA
            + [COL_MERMA_TOT, COL_KG_PROD, COL_INCID, COL_HORAS, COL_DEVUE,
               COL_RETRA])


def _f_merma_pct(r, i):
    """Merma de la partida i en la fila r, en % del peso que ha producido."""
    prod, merma, kg = COLS_PROD[i], COLS_MERMA[i], COLS_PROD[i]
    return ('=IFERROR(IF(OR(${m}{r}="",${p}{r}="",${p}{r}=0,{k}${kf}="",'
            '{k}${kf}=0),"",${m}{r}/(${p}{r}*{k}${kf})),"")'
            .format(m=merma, p=prod, k=kg, kf=E_KG, r=r))


def _f_kg_producidos(r):
    return ('=IF(SUMPRODUCT(${a}{r}:${b}{r},${a}${kf}:${b}${kf})=0,"",'
            'SUMPRODUCT(${a}{r}:${b}{r},${a}${kf}:${b}${kf}))'
            .format(a=COLS_PROD[0], b=COLS_PROD[-1], kf=E_KG, r=r))


def _f_n_fuera(r):
    """Cuántos indicadores de la fila se salen de su objetivo.

    La merma se cuenta con `SUMPRODUCT` sobre las ocho columnas a la vez (con
    `ISNUMBER` sobre el valor y sobre el objetivo, para que una partida sin
    objetivo no cuente); los otros seis, uno a uno.
    """
    partes = ['SUMPRODUCT(--(ISNUMBER(${a}{r}:${b}{r})),'
              '--(ISNUMBER(${a}${o}:${b}${o})),'
              '--(${a}{r}:${b}{r}>${a}${o}:${b}${o}))'
              .format(a=COLS_PCT[0], b=COLS_PCT[-1], o=E_OBJ, r=r)]
    for col in (COL_PASE_E, COL_PASE_P, COL_PASE_D, COL_INCID_T, COL_HORAS_C,
                COL_DR_T):
        partes.append('IF(AND(ISNUMBER(${c}{r}),ISNUMBER(${c}${o}),'
                      '${c}{r}>${c}${o}),1,0)'.format(c=col, o=E_OBJ, r=r))
    return ('=IF(NOT(ISNUMBER(${cu}{r})),"",' + '+'.join(partes) + ')') \
        .format(cu=COL_CUB, r=r)


def hoja_semana(wb):
    ws = wb.create_sheet('Semana')
    cols = _cols_semana()
    encabezar(ws, 'Las 52 semanas ISO de la cocina',
              nota_='Aquí no hay ni una cifra de dinero: eso es el cuadro de '
                    'mando del Manual del Manager. Aquí está la partida.')

    # --- encabezados: los de las partidas los escribe una fórmula (D7) ----
    for letra, texto, _tipo in cols:
        if letra in COLS_PROD + COLS_MERMA + COLS_PCT:
            continue
        motor.val(ws, letra + str(S_CAB), texto)
    for i, letra in enumerate(COLS_PROD):
        motor.f(ws, letra + str(S_CAB),
                '=IF(${n}${f}="","","Producción · "&${n}${f}&" (raciones)")'
                .format(n=COLS_PROD[i], f=E_NOM))
    for i, letra in enumerate(COLS_MERMA):
        motor.f(ws, letra + str(S_CAB),
                '=IF(${n}${f}="","","Merma · "&${n}${f}&" (kg)")'
                .format(n=COLS_PROD[i], f=E_NOM))
    for i, letra in enumerate(COLS_PCT):
        motor.f(ws, letra + str(S_CAB),
                '=IF(${n}${f}="","","Merma · "&${n}${f}&" (%)")'
                .format(n=COLS_PROD[i], f=E_NOM))
    estilo_cabecera(ws, S_CAB, [c[0] for c in cols], altura=74)

    ancho = {COL_SEM: 9, COL_LUNES: 13, COL_MES: 7, COL_CUB: 11,
             COL_RACIONES: 14, COL_MERMA_TOT: 12, COL_KG_PROD: 15,
             COL_MERMA_GLB: 13, COL_PASE_E: 12, COL_PASE_P: 12,
             COL_PASE_D: 12, COL_INCID: 13, COL_GRAV: 12, COL_INCID_T: 14,
             COL_HORAS: 13, COL_HORAS_C: 14, COL_DEVUE: 11, COL_RETRA: 12,
             COL_DR_T: 15, COL_NFUERA: 14, COL_LECTURA: 40}
    for letra in COLS_PROD:
        ancho[letra] = 13
    for letra in COLS_MERMA + COLS_PCT:
        ancho[letra] = 12
    anchos(ws, ancho)

    # --- las 52 filas ------------------------------------------------------
    for j, fila in enumerate(D.SEMANA_COCINA):
        r = S_INI + j
        (sem, mes, cub, prod, merma, pase, inc, grav, horas, dev, ret) = fila
        motor.val(ws, COL_SEM + str(r), sem, fmt=FMT_ENT, verde_=True)
        motor.val(ws, COL_LUNES + str(r), D._lunes_iso(2026, sem),
                  fmt=FMT_FECHA, verde_=True)
        motor.val(ws, COL_MES + str(r), mes, fmt=FMT_ENT, verde_=True)
        motor.val(ws, COL_CUB + str(r), cub, fmt=FMT_ENT, verde_=True)
        for i in range(N_RANURAS):
            v = prod[i] if i < len(prod) else None
            if v is None:
                motor.verde(ws, COLS_PROD[i] + str(r))
                ws[COLS_PROD[i] + str(r)].number_format = FMT_ENT
            else:
                motor.val(ws, COLS_PROD[i] + str(r), v, fmt=FMT_ENT,
                          verde_=True)
            m = merma[i] if i < len(merma) else None
            if m is None:
                motor.verde(ws, COLS_MERMA[i] + str(r))
                ws[COLS_MERMA[i] + str(r)].number_format = FMT_DEC2
            else:
                motor.val(ws, COLS_MERMA[i] + str(r), float(m), fmt=FMT_DEC2,
                          verde_=True)
            motor.f(ws, COLS_PCT[i] + str(r), _f_merma_pct(r, i), fmt=FMT_PCT1)
        motor.f(ws, COL_RACIONES + str(r),
                '=IF(COUNT(${a}{r}:${b}{r})=0,"",SUM(${a}{r}:${b}{r}))'
                .format(a=COLS_PROD[0], b=COLS_PROD[-1], r=r), fmt=FMT_ENT)
        motor.f(ws, COL_MERMA_TOT + str(r),
                '=IF(COUNT(${a}{r}:${b}{r})=0,"",SUM(${a}{r}:${b}{r}))'
                .format(a=COLS_MERMA[0], b=COLS_MERMA[-1], r=r), fmt=FMT_DEC2)
        motor.f(ws, COL_KG_PROD + str(r), _f_kg_producidos(r), fmt=FMT_DEC2)
        motor.f(ws, COL_MERMA_GLB + str(r),
                '=IFERROR(IF(OR(${m}{r}="",${k}{r}="",${k}{r}=0),"",'
                '${m}{r}/${k}{r}),"")'
                .format(m=COL_MERMA_TOT, k=COL_KG_PROD, r=r), fmt=FMT_PCT1)
        motor.val(ws, COL_PASE_E + str(r), float(pase[0]), fmt=FMT_DEC1,
                  verde_=True)
        motor.val(ws, COL_PASE_P + str(r), float(pase[1]), fmt=FMT_DEC1,
                  verde_=True)
        motor.val(ws, COL_PASE_D + str(r), float(pase[2]), fmt=FMT_DEC1,
                  verde_=True)
        motor.val(ws, COL_INCID + str(r), inc, fmt=FMT_ENT, verde_=True)
        motor.val(ws, COL_GRAV + str(r), grav, fmt=FMT_ENT, verde_=True)
        motor.f(ws, COL_INCID_T + str(r),
                '=IFERROR(IF(OR(${i}{r}="",${c}{r}="",${c}{r}=0,'
                '${cu}${b}=""),"",${i}{r}/${c}{r}*${cu}${b}),"")'
                .format(i=COL_INCID, c=COL_CUB, cu=COL_ESPEJO, b=E_BASE, r=r),
                fmt=FMT_DEC1)
        motor.val(ws, COL_HORAS + str(r), horas, fmt=FMT_ENT, verde_=True)
        motor.f(ws, COL_HORAS_C + str(r),
                '=IFERROR(IF(OR(${h}{r}="",${c}{r}="",${c}{r}=0),"",'
                '${h}{r}/${c}{r}),"")'
                .format(h=COL_HORAS, c=COL_CUB, r=r), fmt=FMT_DEC3)
        motor.val(ws, COL_DEVUE + str(r), dev, fmt=FMT_ENT, verde_=True)
        motor.val(ws, COL_RETRA + str(r), ret, fmt=FMT_ENT, verde_=True)
        motor.f(ws, COL_DR_T + str(r),
                '=IFERROR(IF(OR(${d}{r}="",${e}{r}="",${c}{r}="",${c}{r}=0,'
                '${cu}${b}=""),"",(${d}{r}+${e}{r})/${c}{r}*${cu}${b}),"")'
                .format(d=COL_DEVUE, e=COL_RETRA, c=COL_CUB, cu=COL_ESPEJO,
                        b=E_BASE, r=r), fmt=FMT_DEC1)
        motor.f(ws, COL_NFUERA + str(r), _f_n_fuera(r), fmt=FMT_ENT)
        motor.f(ws, COL_LECTURA + str(r),
                '=IF(NOT(ISNUMBER(${n}{r})),"",IF(${n}{r}=0,'
                '"Semana en objetivo",IF(${n}{r}=1,'
                '"1 indicador fuera de objetivo",'
                '${n}{r}&" indicadores fuera de objetivo")))'
                .format(n=COL_NFUERA, r=r))

    # --- fila TOTAL / MEDIA ------------------------------------------------
    motor.val(ws, COL_SEM + str(S_TOT), 'TOTAL / MEDIA', bold=True)
    for letra in SUMABLES:
        tipo = dict((c[0], c[2]) for c in cols)[letra]
        motor.f(ws, letra + str(S_TOT),
                '=IF(COUNT({c}{a}:{c}{b})=0,"",SUM({c}{a}:{c}{b}))'
                .format(c=letra, a=S_INI, b=S_FIN), fmt=FORMATO[tipo],
                bold=True)
    for i in range(N_RANURAS):
        motor.f(ws, COLS_PCT[i] + str(S_TOT), _f_merma_pct(S_TOT, i),
                fmt=FMT_PCT1, bold=True)
    motor.f(ws, COL_MERMA_GLB + str(S_TOT),
            '=IFERROR(IF(OR(${m}${t}="",${k}${t}="",${k}${t}=0),"",'
            '${m}${t}/${k}${t}),"")'
            .format(m=COL_MERMA_TOT, k=COL_KG_PROD, t=S_TOT), fmt=FMT_PCT1,
            bold=True)
    for letra in (COL_PASE_E, COL_PASE_P, COL_PASE_D):
        motor.f(ws, letra + str(S_TOT),
                '=IF(COUNT({c}{a}:{c}{b})=0,"",AVERAGE({c}{a}:{c}{b}))'
                .format(c=letra, a=S_INI, b=S_FIN), fmt=FMT_DEC1, bold=True)
    motor.f(ws, COL_GRAV + str(S_TOT),
            '=IF(COUNT({c}{a}:{c}{b})=0,"",MAX({c}{a}:{c}{b}))'
            .format(c=COL_GRAV, a=S_INI, b=S_FIN), fmt=FMT_ENT, bold=True)
    motor.f(ws, COL_INCID_T + str(S_TOT),
            '=IFERROR(IF(OR(${i}${t}="",${c}${t}="",${c}${t}=0,'
            '${cu}${b}=""),"",${i}${t}/${c}${t}*${cu}${b}),"")'
            .format(i=COL_INCID, c=COL_CUB, cu=COL_ESPEJO, b=E_BASE, t=S_TOT),
            fmt=FMT_DEC1, bold=True)
    motor.f(ws, COL_HORAS_C + str(S_TOT),
            '=IFERROR(IF(OR(${h}${t}="",${c}${t}="",${c}${t}=0),"",'
            '${h}${t}/${c}${t}),"")'
            .format(h=COL_HORAS, c=COL_CUB, t=S_TOT), fmt=FMT_DEC3, bold=True)
    motor.f(ws, COL_DR_T + str(S_TOT),
            '=IFERROR(IF(OR(${d}${t}="",${e}${t}="",${c}${t}="",${c}${t}=0,'
            '${cu}${b}=""),"",(${d}${t}+${e}${t})/${c}${t}*${cu}${b}),"")'
            .format(d=COL_DEVUE, e=COL_RETRA, c=COL_CUB, cu=COL_ESPEJO, b=E_BASE,
                    t=S_TOT), fmt=FMT_DEC1, bold=True)
    motor.f(ws, COL_NFUERA + str(S_TOT), _f_n_fuera(S_TOT), fmt=FMT_ENT,
            bold=True)
    motor.f(ws, COL_LECTURA + str(S_TOT),
            '=IF(NOT(ISNUMBER(${n}${t})),"",IF(${n}${t}=0,'
            '"Año en objetivo",IF(${n}${t}=1,'
            '"1 indicador fuera de objetivo en el año",'
            '${n}${t}&" indicadores fuera de objetivo en el año")))'
            .format(n=COL_NFUERA, t=S_TOT), bold=True)
    fila_total(ws, S_TOT, COL_SEM, COL_ULTIMA)

    nota(ws, S_TOT + 2,
         'Y ojo con leer sólo esta fila: el año puede cerrar en objetivo con '
         'semanas malas dentro. En el restaurante de ejemplo el año entero '
         'entra en objetivo y aun así hay cuatro semanas fuera (la 7, por el '
         'pase, y la 33, la 34 y la 35, por la merma de la partida de fríos). '
         'Por eso este libro se mira por semanas y no por medias del año.')
    nota(ws, S_TOT + 1,
         'En la fila TOTAL los porcentajes NO son la media de los 52 '
         'porcentajes: la merma del año es la merma en kilos del año dividida '
         'entre los kilos producidos del año, que es la media ponderada y la '
         'única correcta. Los tiempos de pase sí son una media simple de las '
         'semanas medidas, porque cada semana aporta su propio muestreo.')

    # --- espejo de parámetros (el formato condicional no cruza de hoja) ---
    seccion(ws, COL_SEM + str(E_TIT),
            'PARÁMETROS EN VIGOR — se leen de la hoja «Parámetros»; cámbialos '
            'allí, no aquí')
    motor.val(ws, COL_SEM + str(E_NOM), 'Partida activa')
    motor.val(ws, COL_SEM + str(E_KG), 'Kg de materia prima por ración')
    motor.val(ws, COL_SEM + str(E_OBJ), 'Objetivo de la casa')
    motor.val(ws, COL_SEM + str(E_BASE), 'Base de las tasas por cubiertos')
    motor.val(ws, COL_SEM + str(E_ACT), 'Partidas activas')
    for i in range(N_RANURAS):
        motor.f(ws, COLS_PROD[i] + str(E_NOM),
                '=IFERROR(IF({k}>Parámetros!$B${a},"",'
                'IF(INDEX({rp},{k})=0,"",INDEX({rp},{k}))),"")'
                .format(k=i + 1, a=P_ACT, rp=IDX_NOMBRE))
        motor.f(ws, COLS_PROD[i] + str(E_KG),
                '=IFERROR(IF({k}>Parámetros!$B${a},"",'
                'IF(INDEX({rk},{k})=0,"",INDEX({rk},{k}))),"")'
                .format(k=i + 1, a=P_ACT, rk=IDX_KG),
                fmt=FMT_DEC2)
        motor.f(ws, COLS_PCT[i] + str(E_OBJ),
                '=IFERROR(IF({k}>Parámetros!$B${a},"",'
                'IF(INDEX({ro},{k})=0,"",INDEX({ro},{k}))),"")'
                .format(k=i + 1, a=P_ACT, ro=IDX_OBJ),
                fmt=FMT_PCT1)
    for letra, fila_p, fmt in ((COL_PASE_E, P_O_PASE_E, FMT_DEC1),
                               (COL_PASE_P, P_O_PASE_P, FMT_DEC1),
                               (COL_PASE_D, P_O_PASE_D, FMT_DEC1),
                               (COL_INCID_T, P_O_INCID, FMT_DEC1),
                               (COL_HORAS_C, P_O_HORAS, FMT_DEC3),
                               (COL_DR_T, P_O_SUMA, FMT_DEC1)):
        motor.f(ws, letra + str(E_OBJ),
                mirar('Parámetros!$B$%d' % fila_p), fmt=fmt)
    motor.f(ws, COL_ESPEJO + str(E_BASE), mirar('Parámetros!$B$%d' % P_BASE),
            fmt=FMT_ENT)
    motor.f(ws, COL_ESPEJO + str(E_ACT), mirar('Parámetros!$B$%d' % P_ACT),
            fmt=FMT_ENT)
    for r in (E_NOM, E_KG, E_OBJ, E_BASE, E_ACT):
        for letra in COLS_PROD + COLS_PCT + [COL_ESPEJO, COL_PASE_E, COL_PASE_P,
                                             COL_PASE_D, COL_INCID_T,
                                             COL_HORAS_C, COL_DR_T]:
            c = ws[letra + str(r)]
            if c.value is not None:
                c.fill = PatternFill('solid', fgColor=GRIS)
    nota(ws, E_ACT + 2,
         'Este bloque es un espejo de la hoja «Parámetros». Está aquí porque '
         'el formato condicional no puede leer otra hoja sin usar INDIRECT, '
         'que esta familia de libros tiene prohibida por frágil.')

    # --- semáforos ---------------------------------------------------------
    semaforo_con_objetivo(
        ws, '{a}{i}:{b}{t}'.format(a=COLS_PCT[0], b=COLS_PCT[-1], i=S_INI,
                                   t=S_TOT),
        COLS_PCT[0], S_INI, COLS_PCT[0], E_OBJ)
    semaforo_con_objetivo(
        ws, '{a}{i}:{b}{t}'.format(a=COL_PASE_E, b=COL_PASE_D, i=S_INI,
                                   t=S_TOT),
        COL_PASE_E, S_INI, COL_PASE_E, E_OBJ)
    for letra in (COL_INCID_T, COL_HORAS_C, COL_DR_T):
        semaforo_con_objetivo(
            ws, '{c}{i}:{c}{t}'.format(c=letra, i=S_INI, t=S_TOT),
            letra, S_INI, letra, E_OBJ)
    rango_n = '{c}{i}:{c}{t}'.format(c=COL_NFUERA, i=S_INI, t=S_TOT)
    cf_expresion(ws, rango_n,
                 '=AND(ISNUMBER(${c}{i}),${c}{i}>0)'.format(c=COL_NFUERA,
                                                            i=S_INI),
                 motor.CF_ROJO_BG, motor.CF_ROJO_FG)
    cf_expresion(ws, rango_n,
                 '=AND(ISNUMBER(${c}{i}),${c}{i}=0)'.format(c=COL_NFUERA,
                                                            i=S_INI),
                 motor.CF_VERDE_BG, motor.CF_VERDE_FG)
    rango_l = '{c}{i}:{c}{t}'.format(c=COL_LECTURA, i=S_INI, t=S_TOT)
    cf_expresion(ws, rango_l,
                 '=AND(ISNUMBER(${n}{i}),${n}{i}>0)'.format(n=COL_NFUERA,
                                                            i=S_INI),
                 motor.CF_ROJO_BG, motor.CF_ROJO_FG)
    cf_expresion(ws, rango_l,
                 '=AND(ISNUMBER(${n}{i}),${n}{i}=0)'.format(n=COL_NFUERA,
                                                            i=S_INI),
                 motor.CF_VERDE_BG, motor.CF_VERDE_FG)
    cf_expresion(ws, '{c}{i}:{c}{t}'.format(c=COL_GRAV, i=S_INI, t=S_TOT),
                 '=AND(ISNUMBER(${c}{i}),${c}{i}>0)'.format(c=COL_GRAV,
                                                            i=S_INI),
                 motor.CF_AMBAR_BG, motor.CF_AMBAR_FG)

    # --- validaciones ------------------------------------------------------
    filas = list(range(S_INI, S_FIN + 1))
    motor.dv_numerica(ws, [COL_SEM + str(r) for r in filas], minimo=1,
                      maximo=53, titulo='Semana ISO',
                      mensaje='La semana ISO va de 1 a 53.')
    motor.dv_fecha(ws, [COL_LUNES + str(r) for r in filas])
    motor.dv_numerica(ws, [COL_MES + str(r) for r in filas], minimo=1,
                      maximo=12, titulo='Mes',
                      mensaje='El mes al que asignas la semana (1 a 12). La '
                              'convención ISO es el mes de su jueves.')
    motor.dv_numerica(ws, [c + str(r) for c in [COL_CUB] + COLS_PROD
                           + [COL_INCID, COL_HORAS, COL_DEVUE, COL_RETRA]
                           for r in filas],
                      minimo=0, titulo='Recuento',
                      mensaje='Escribe un número entero mayor o igual que 0.')
    motor.dv_numerica(ws, [c + str(r) for c in COLS_MERMA for r in filas],
                      minimo=0, titulo='Merma (kg)',
                      mensaje='Kilos de merma de esa partida en la semana.')
    motor.dv_numerica(ws, [c + str(r) for c in (COL_PASE_E, COL_PASE_P,
                                                COL_PASE_D) for r in filas],
                      minimo=0, maximo=240, titulo='Minutos',
                      mensaje='Minutos desde la comanda hasta la salida.')
    motor.dv_numerica(ws, [COL_GRAV + str(r) for r in filas], minimo=0,
                      maximo=3, titulo='Gravedad',
                      mensaje='De 0 (ninguna) a 3 (llegó al cliente con '
                              'consecuencias).')

    ws.freeze_panes = COLS_PROD[0] + str(S_INI)
    pagina(ws, titulos='$%d:$%d' % (S_CAB, S_CAB))
    return ws


# --------------------------------------------------------------------------
# Hoja «KPI y Definiciones»
# --------------------------------------------------------------------------
#: Objetivo y columna de la hoja «Semana» de cada uno de los 7 KPI, en el mismo
#: orden que `datos_ejemplo.KPI_COCINA`. La rotación de la brigada no se mide
#: en este libro (es trimestral y sale del Manual del Manager): por eso no
#: tiene ni objetivo ni columna.
KPI_ENLACE = [
    (None, 'Semana, columnas «Merma · <partida> (%)»'),
    (None, 'Semana, columnas «Pase de entrantes / principales / postres»'),
    (P_O_INCID, 'Semana, columna «Incidencias por base de cubiertos»'),
    (P_O_HORAS, 'Semana, columna «Horas de cocina por cubierto»'),
    (None, 'No se mide aquí: hoja «Control de Calidad del Pase» del libro de '
           'desarrollo de carta'),
    (P_O_SUMA, 'Semana, columna «Devueltos y retrabajados por base»'),
    (None, 'No se mide aquí: cuadro de mando del Manual del Manager, con '
           'cadencia trimestral'),
]


def hoja_kpi(wb):
    ws = wb.create_sheet('KPI y Definiciones')
    encabezar(ws, 'Los siete KPI de cocina',
              nota_='No existe un estándar publicado de KPI de cocina en '
                    'español. Ésta es nuestra lista: por qué cada uno y cuál '
                    'es su error típico. El objetivo lo pones tú.')
    cabecera(ws, K_CAB, [('A', 'Indicador'), ('B', 'Cómo se calcula'),
                         ('C', 'Unidad'), ('D', 'Error típico'),
                         ('E', 'Cadencia'), ('F', 'Objetivo de la casa'),
                         ('G', 'De dónde sale el dato')], altura=32)
    anchos(ws, {'A': 30, 'B': 54, 'C': 16, 'D': 62, 'E': 14, 'F': 18, 'G': 46})
    for i, (kpi, formula, unidad, error, cadencia) in enumerate(D.KPI_COCINA):
        r = K_INI + i
        motor.val(ws, 'A%d' % r, kpi, bold=True, wrap=True)
        motor.val(ws, 'B%d' % r, formula, wrap=True)
        motor.val(ws, 'C%d' % r, unidad, align='center')
        motor.val(ws, 'D%d' % r, error, wrap=True)
        motor.val(ws, 'E%d' % r, cadencia, align='center')
        fila_obj, origen = KPI_ENLACE[i]
        if fila_obj is None:
            motor.val(ws, 'F%d' % r, 'Uno por partida'
                      if i == 0 else ('Tres, uno por familia' if i == 1
                                      else 'No se mide en este libro'),
                      align='center', wrap=True)
        else:
            fmt = FMT_DEC3 if fila_obj == P_O_HORAS else FMT_DEC1
            motor.f(ws, 'F%d' % r, mirar('Parámetros!$B$%d' % fila_obj),
                    fmt=fmt, align='center')
            ws['F%d' % r].fill = PatternFill('solid', fgColor=GRIS)
        motor.val(ws, 'G%d' % r, origen, wrap=True)
        ws.row_dimensions[r].height = 52
    nota(ws, K_FIN + 2,
         'La columna «Error típico» es la que evita las discusiones: casi '
         'siempre que dos personas dan dos números distintos para lo mismo, '
         'una de las dos está cometiendo el error de esa columna.')
    nota(ws, K_FIN + 3,
         'Ninguno de estos siete indicadores se compara con el de otra cocina '
         'sin mirar antes qué carta tiene, cuántos servicios hace y con qué '
         'brigada: para eso está la hoja «Comparativa entre Unidades», que '
         'compara contra el estándar que fija tu grupo, no contra el sector.')
    nota(ws, K_FIN + 4,
         'Ninguna cifra de este libro es un benchmark de mercado. Este '
         'producto no publica ni uno solo de merma, de tiempo de pase ni de '
         'horas de formación, porque no existe ninguno verificado en español.')
    ws.freeze_panes = 'A%d' % K_INI
    pagina(ws)
    return ws


# --------------------------------------------------------------------------
# Hoja «Comparativa entre Unidades» (SPEC D6)
# --------------------------------------------------------------------------
#: (letra, encabezado, formato, clave de ESTANDAR_GRUPO, columna de «Semana»)
KPI_UNIDAD = [
    ('C', 'Merma global (%)', FMT_PCT1, 'merma_global'),
    ('D', 'Pase de principales (min)', FMT_DEC1, 'pase_principales_min'),
    ('E', 'Incidencias de alérgenos por base', FMT_DEC1,
     'incidencias_alergenos_1000'),
    ('F', 'Horas de cocina por cubierto', FMT_DEC3, 'horas_cocina_cubierto'),
    ('G', 'Platos devueltos por base', FMT_DEC1, 'devueltos_1000'),
]
COLS_DESV = ['I', 'J', 'K', 'L', 'M']
COL_DENTRO = 'N'
COL_POS = 'O'


def hoja_comparativa(wb):
    ws = wb.create_sheet('Comparativa entre Unidades')
    anchos(ws, {'A': 34, 'B': 14, 'C': 14, 'D': 16, 'E': 18, 'F': 16,
                'G': 16, 'H': 3, 'I': 14, 'J': 14, 'K': 14, 'L': 14,
                'M': 14, 'N': 16, 'O': 12})
    encabezar(ws, 'Comparativa entre unidades',
              nota_='Una cocina, con las herramientas para comparar varias. La '
                    'primera fila la calcula el libro desde tu hoja «Semana»; '
                    'las otras cinco las tecleas copiando del libro de cada '
                    'unidad.')

    seccion(ws, 'A4', 'MES CERRADO QUE SE COMPARA')
    motor.val(ws, 'A%d' % C_MES, 'Mes (1 a 12)', bold=True)
    motor.val(ws, 'B%d' % C_MES, D.UNIDADES_MES['mes'], fmt=FMT_ENT,
              verde_=True)
    motor.val(ws, 'A%d' % C_ANIO, 'Año', bold=True)
    motor.val(ws, 'B%d' % C_ANIO, D.UNIDADES_MES['anio'], fmt='0',
              verde_=True)
    motor.val(ws, 'A%d' % C_BASE, 'Base de las tasas por cubiertos', bold=True)
    motor.f(ws, 'B%d' % C_BASE, mirar('Parámetros!$B$%d' % P_BASE),
            fmt=FMT_ENT)
    ws['B%d' % C_BASE].fill = PatternFill('solid', fgColor=GRIS)
    nota(ws, C_BASE + 1,
         'El mes se busca en la columna «Mes» de la hoja «Semana». El año no '
         'entra en el cálculo: este libro cubre un año, y está aquí para que '
         'la comparativa quede fechada cuando la imprimas o la copies.')

    # --- estándar del grupo ------------------------------------------------
    seccion(ws, 'A%d' % C_SEC_EST, 'ESTÁNDAR DEL GRUPO')
    cabecera(ws, C_ECAB,
             [('A', 'Estándar contra el que se comparan las unidades')]
             + [(letra, texto) for letra, texto, _f, _k in KPI_UNIDAD],
             altura=46)
    motor.val(ws, 'A%d' % C_EST, 'Objetivo del grupo', bold=True)
    for letra, _texto, fmt, clave in KPI_UNIDAD:
        motor.val(ws, letra + str(C_EST), D.ESTANDAR_GRUPO[clave], fmt=fmt,
                  verde_=True)
    nota(ws, C_EST + 1,
         'Este estándar es del GRUPO, no del sector: no hay ninguno publicado. '
         'Viene igualado a los objetivos de la hoja «Parámetros» del '
         'restaurante de ejemplo; si tu grupo fija otros, cámbialos aquí y la '
         'comparativa se recalcula.')
    nota(ws, C_EST + 2,
         'Los cinco indicadores van en el mismo sentido: cuanto MÁS BAJO, '
         'mejor. Por eso una desviación positiva es siempre peor que el '
         'estándar, y se pinta en rojo.')

    # --- las unidades ------------------------------------------------------
    seccion(ws, 'A%d' % C_SEC_UNI, 'UNIDADES')
    cabecera(ws, C_UCAB,
             [('A', 'Unidad'), ('B', 'Cubiertos del mes')]
             + [(letra, texto) for letra, texto, _f, _k in KPI_UNIDAD]
             + [('H', '')]
             + [(COLS_DESV[i], 'Desviación · ' + KPI_UNIDAD[i][1])
                for i in range(len(KPI_UNIDAD))]
             + [(COL_DENTRO, 'Indicadores dentro del estándar (de 5)'),
                (COL_POS, 'Posición')], altura=74)

    mes = '$B$%d' % C_MES
    base = '$B$%d' % C_BASE
    smes = "Semana!${c}${a}:${c}${b}".format(c=COL_MES, a=S_INI, b=S_FIN)

    def scol(letra):
        return "Semana!${c}${a}:${c}${b}".format(c=letra, a=S_INI, b=S_FIN)

    # fila 1: la unidad de referencia, calculada desde la hoja «Semana». A2 de
    # la refutación xlsx (2026-09-06): antes era un literal que no se
    # enteraba de que cambiaras el nombre de tu cocina en «Parámetros».
    r = C_UINI
    motor.f(ws, 'A%d' % r,
            '=IF(Parámetros!$B$%d="","",Parámetros!$B$%d&" (unidad de '
            'referencia)")' % (P_NOMBRE, P_NOMBRE))
    ws['A%d' % r].alignment = Alignment(wrap_text=True, vertical='top')
    ws['A%d' % r].fill = PatternFill('solid', fgColor=GRIS)
    motor.f(ws, 'B%d' % r,
            '=IFERROR(IF(SUMIF({m},{mes},{cub})=0,"",SUMIF({m},{mes},{cub})),'
            '"")'.format(m=smes, mes=mes, cub=scol(COL_CUB)), fmt=FMT_ENT)
    motor.f(ws, 'C%d' % r,
            '=IFERROR(SUMIF({m},{mes},{mk})/SUMIF({m},{mes},{kg}),"")'
            .format(m=smes, mes=mes, mk=scol(COL_MERMA_TOT),
                    kg=scol(COL_KG_PROD)), fmt=FMT_PCT1)
    motor.f(ws, 'D%d' % r,
            '=IFERROR(AVERAGEIF({m},{mes},{p}),"")'
            .format(m=smes, mes=mes, p=scol(COL_PASE_P)), fmt=FMT_DEC1)
    motor.f(ws, 'E%d' % r,
            '=IFERROR(SUMIF({m},{mes},{i})/SUMIF({m},{mes},{cub})*{b},"")'
            .format(m=smes, mes=mes, i=scol(COL_INCID), cub=scol(COL_CUB),
                    b=base), fmt=FMT_DEC1)
    motor.f(ws, 'F%d' % r,
            '=IFERROR(SUMIF({m},{mes},{h})/SUMIF({m},{mes},{cub}),"")'
            .format(m=smes, mes=mes, h=scol(COL_HORAS), cub=scol(COL_CUB)),
            fmt=FMT_DEC3)
    motor.f(ws, 'G%d' % r,
            '=IFERROR(SUMIF({m},{mes},{d})/SUMIF({m},{mes},{cub})*{b},"")'
            .format(m=smes, mes=mes, d=scol(COL_DEVUE), cub=scol(COL_CUB),
                    b=base), fmt=FMT_DEC1)
    for letra in ['B'] + [k[0] for k in KPI_UNIDAD]:
        ws[letra + str(r)].fill = PatternFill('solid', fgColor=GRIS)

    # filas 2 a 6: se teclean
    for i in range(1, N_UNIDADES):
        r = C_UINI + i
        if i < len(D.UNIDADES):
            nombre, cub, merma, pase, incid, horas, devue = D.UNIDADES[i]
            motor.val(ws, 'A%d' % r, nombre, verde_=True, wrap=True)
            motor.val(ws, 'B%d' % r, cub, fmt=FMT_ENT, verde_=True)
            for letra, valor, fmt in (('C', merma, FMT_PCT1),
                                      ('D', pase, FMT_DEC1),
                                      ('E', incid, FMT_DEC1),
                                      ('F', horas, FMT_DEC3),
                                      ('G', devue, FMT_DEC1)):
                motor.val(ws, letra + str(r), valor, fmt=fmt, verde_=True)
        else:
            motor.verde(ws, 'A%d' % r)
            motor.verde(ws, 'B%d' % r)
            ws['B%d' % r].number_format = FMT_ENT
            for letra, _t, fmt, _k in KPI_UNIDAD:
                motor.verde(ws, letra + str(r))
                ws[letra + str(r)].number_format = fmt

    # desviaciones, recuento y posición (todas las filas)
    for i in range(N_UNIDADES):
        r = C_UINI + i
        for j, (letra, _t, _f, _k) in enumerate(KPI_UNIDAD):
            motor.f(ws, COLS_DESV[j] + str(r),
                    '=IFERROR(IF(OR(NOT(ISNUMBER(${c}{r})),'
                    'NOT(ISNUMBER(${c}${e})),${c}${e}=0),"",'
                    '(${c}{r}-${c}${e})/${c}${e}),"")'
                    .format(c=letra, r=r, e=C_EST), fmt=FMT_PCT1)
        partes = ['IF(AND(ISNUMBER(${c}{r}),ISNUMBER(${c}${e}),'
                  '${c}{r}<=${c}${e}),1,0)'.format(c=k[0], r=r, e=C_EST)
                  for k in KPI_UNIDAD]
        motor.f(ws, COL_DENTRO + str(r),
                '=IF(NOT(ISNUMBER($B{r})),"",{s})'
                .format(r=r, s='+'.join(partes)), fmt=FMT_ENT)
        motor.f(ws, COL_POS + str(r),
                '=IF(NOT(ISNUMBER(${d}{r})),"",'
                'SUMPRODUCT(--(ISNUMBER(${d}${a}:${d}${b})),'
                '--(${d}${a}:${d}${b}>${d}{r}))+1)'
                .format(d=COL_DENTRO, a=C_UINI, b=C_UFIN, r=r), fmt=FMT_ENT)

    nota(ws, C_UFIN + 2,
         'La fila de la unidad de referencia NO se teclea: el nombre lo trae '
         'de la hoja «Parámetros» (cámbialo allí, no aquí) y las cifras '
         'salen de tu hoja «Semana», sumando las semanas cuyo mes coincide '
         'con el de arriba.')
    nota(ws, C_UFIN + 3,
         'Las otras cinco filas se rellenan a mano copiando la fila TOTAL del '
         'mes de la hoja «Semana» del libro de cada unidad. Es copia, no '
         'vínculo: ningún libro de este pack lee un fichero ajeno.')
    nota(ws, C_UFIN + 4,
         'La posición ordena por cuántos indicadores están dentro del '
         'estándar, no por una media de magnitudes distintas (no se puede '
         'promediar un minuto con un kilo). Dos unidades con el mismo '
         'recuento comparten posición.')
    nota(ws, C_UFIN + 5,
         'Antes de sacar una conclusión de esta hoja: dos cocinas del mismo '
         'grupo no son comparables sin mirar la carta, los servicios y la '
         'brigada de cada una. Esta tabla dice DÓNDE mirar, no quién lo hace '
         'mal.')

    # semáforos de las desviaciones
    for j in range(len(KPI_UNIDAD)):
        letra = COLS_DESV[j]
        rango = '{c}{a}:{c}{b}'.format(c=letra, a=C_UINI, b=C_UFIN)
        cf_expresion(ws, rango,
                     '=AND(ISNUMBER(${c}{a}),${c}{a}>0)'.format(c=letra,
                                                                a=C_UINI),
                     motor.CF_ROJO_BG, motor.CF_ROJO_FG)
        cf_expresion(ws, rango,
                     '=AND(ISNUMBER(${c}{a}),${c}{a}<=0)'.format(c=letra,
                                                                 a=C_UINI),
                     motor.CF_VERDE_BG, motor.CF_VERDE_FG)

    motor.dv_numerica(ws, ['B%d' % C_MES], minimo=1, maximo=12, titulo='Mes',
                      mensaje='Un número del 1 al 12.')
    motor.dv_numerica(ws, ['B%d' % C_ANIO], minimo=2020, maximo=2040,
                      titulo='Año', mensaje='Un año entre 2020 y 2040.')
    motor.dv_porcentaje(ws, ['C%d' % C_EST]
                        + ['C%d' % r for r in range(C_UINI + 1, C_UFIN + 1)],
                        titulo='Merma global',
                        prompt='Se escribe en tanto por uno: 0,040 = 4,0 %.')
    motor.dv_numerica(ws, ['D%d' % C_EST]
                      + ['D%d' % r for r in range(C_UINI + 1, C_UFIN + 1)],
                      minimo=0, maximo=240, titulo='Minutos',
                      mensaje='Minutos de pase de principales.')
    motor.dv_numerica(ws, [c + str(C_EST) for c in ('E', 'G')]
                      + [c + str(r) for c in ('E', 'G')
                         for r in range(C_UINI + 1, C_UFIN + 1)],
                      minimo=0, maximo=100000, titulo='Tasa por cubiertos',
                      mensaje='En la misma base de cubiertos de la hoja '
                              '«Parámetros».')
    motor.dv_numerica(ws, ['F%d' % C_EST]
                      + ['F%d' % r for r in range(C_UINI + 1, C_UFIN + 1)],
                      minimo=0, maximo=24, titulo='Horas por cubierto',
                      mensaje='Horas de cocina por cada cubierto servido.')
    motor.dv_numerica(ws, ['B%d' % r for r in range(C_UINI + 1, C_UFIN + 1)],
                      minimo=0, titulo='Cubiertos',
                      mensaje='Cubiertos servidos por esa unidad en el mes.')
    pagina(ws)
    return ws


# --------------------------------------------------------------------------
def mapa():
    """Contrato del guion: qué celda tiene qué (SPEC §7).

    Sólo se registran celdas con VALOR: las ranuras de partida vacías y las
    columnas de las partidas que no producen raciones devuelven «sin dato»
    («») a propósito y no se citan en el manual.
    """
    celdas_p = {
        'Nombre de la cocina de ejemplo': 'B%d' % P_NOMBRE,
        'Tipo de carta del caso': 'B%d' % P_CARTA,
        'Partidas activas del caso': 'B%d' % P_ACT,
        'Base de las tasas por cubiertos': 'B%d' % P_BASE,
        'Objetivo de tiempo de pase de entrantes': 'B%d' % P_O_PASE_E,
        'Objetivo de tiempo de pase de principales': 'B%d' % P_O_PASE_P,
        'Objetivo de tiempo de pase de postres': 'B%d' % P_O_PASE_D,
        'Objetivo de incidencias de alérgenos por base': 'B%d' % P_O_INCID,
        'Objetivo de horas de cocina por cubierto': 'B%d' % P_O_HORAS,
        'Objetivo de platos devueltos por base': 'B%d' % P_O_DEVUE,
        'Objetivo de platos retrabajados por base': 'B%d' % P_O_RETRA,
        'Objetivo conjunto de devueltos y retrabajados': 'B%d' % P_O_SUMA,
    }
    for i, (nombre, produce, _q, _e) in enumerate(D.PARTIDAS):
        r = P_PINI + i
        celdas_p['Nombre de la partida %d' % (i + 1)] = 'A%d' % r
        if produce:
            celdas_p['Kg por ración de ' + nombre] = 'C%d' % r
            celdas_p['Objetivo de merma de ' + nombre] = 'D%d' % r

    celdas_s = {
        'Cubiertos del año': COL_CUB + str(S_TOT),
        'Raciones producidas en el año': COL_RACIONES + str(S_TOT),
        'Merma total del año (kg)': COL_MERMA_TOT + str(S_TOT),
        'Materia prima producida en el año (kg)': COL_KG_PROD + str(S_TOT),
        'Merma global del año (%)': COL_MERMA_GLB + str(S_TOT),
        'Tiempo medio de pase de entrantes del año':
            COL_PASE_E + str(S_TOT),
        'Tiempo medio de pase de principales del año':
            COL_PASE_P + str(S_TOT),
        'Tiempo medio de pase de postres del año': COL_PASE_D + str(S_TOT),
        'Incidencias de alérgenos del año': COL_INCID + str(S_TOT),
        'Gravedad máxima de alérgenos del año': COL_GRAV + str(S_TOT),
        'Incidencias de alérgenos por base del año': COL_INCID_T + str(S_TOT),
        'Horas de cocina del año': COL_HORAS + str(S_TOT),
        'Horas de cocina por cubierto del año': COL_HORAS_C + str(S_TOT),
        'Platos devueltos del año': COL_DEVUE + str(S_TOT),
        'Platos retrabajados del año': COL_RETRA + str(S_TOT),
        'Devueltos y retrabajados por base del año': COL_DR_T + str(S_TOT),
        'Indicadores fuera de objetivo en el año': COL_NFUERA + str(S_TOT),
        'Lectura del año': COL_LECTURA + str(S_TOT),
    }
    for i, (nombre, produce, _q, _e) in enumerate(D.PARTIDAS):
        if not produce:
            continue
        celdas_s['Producción del año de ' + nombre] = COLS_PROD[i] + str(S_TOT)
        celdas_s['Merma del año de ' + nombre + ' (kg)'] = \
            COLS_MERMA[i] + str(S_TOT)
        celdas_s['Merma del año de ' + nombre + ' (%)'] = \
            COLS_PCT[i] + str(S_TOT)
    for j, fila in enumerate(D.SEMANA_COCINA):
        sem = fila[0]
        r = S_INI + j
        if sem not in D.SEMANAS_MALAS_COCINA and sem != D.SEMANA_TIPO_PREVISION:
            continue
        etq = 'semana %d' % sem
        celdas_s['Cubiertos de la ' + etq] = COL_CUB + str(r)
        celdas_s['Merma global de la ' + etq] = COL_MERMA_GLB + str(r)
        celdas_s['Pase de principales de la ' + etq] = COL_PASE_P + str(r)
        celdas_s['Horas de cocina por cubierto de la ' + etq] = \
            COL_HORAS_C + str(r)
        celdas_s['Devueltos y retrabajados por base de la ' + etq] = \
            COL_DR_T + str(r)
        celdas_s['Indicadores fuera de objetivo de la ' + etq] = \
            COL_NFUERA + str(r)
        celdas_s['Lectura de la ' + etq] = COL_LECTURA + str(r)
        for i, (nombre, produce, _q, _e) in enumerate(D.PARTIDAS):
            if produce:
                celdas_s['Merma de ' + nombre + ' en la ' + etq] = \
                    COLS_PCT[i] + str(r)

    celdas_c = {'Mes cerrado que se compara': 'B%d' % C_MES,
                'Año de la comparativa': 'B%d' % C_ANIO}
    for letra, texto, _f, clave in KPI_UNIDAD:
        celdas_c['Estándar del grupo: ' + texto] = letra + str(C_EST)
    for i in range(min(len(D.UNIDADES), N_UNIDADES)):
        r = C_UINI + i
        nombre = D.UNIDADES[i][0]
        celdas_c['Cubiertos del mes de ' + nombre] = 'B%d' % r
        for letra, texto, _f, _k in KPI_UNIDAD:
            celdas_c[texto + ' de ' + nombre] = letra + str(r)
        celdas_c['Indicadores dentro del estándar de ' + nombre] = \
            COL_DENTRO + str(r)
        celdas_c['Posición de ' + nombre] = COL_POS + str(r)

    hojas = {
        'Parámetros': {
            'celdas': celdas_p,
            'tablas': [
                {'titulo': 'Las partidas de la cocina',
                 'cols': [['Partida', 'A', 'txt'],
                          ['¿Produce raciones?', 'B', 'txt'],
                          ['Kg de materia prima neta por ración', 'C', 'num'],
                          ['Objetivo de merma (%)', 'D', 'pct1'],
                          ['Qué produce', 'E', 'txt']],
                 'filas': [P_PINI, P_PINI + len(D.PARTIDAS) - 1]},
                {'titulo': 'Objetivos de la casa',
                 'cols': [['Indicador', 'A', 'txt'],
                          ['Objetivo', 'B', 'num'],
                          ['Unidad', 'C', 'txt'],
                          ['Cómo se lee', 'D', 'txt']],
                 'filas': [P_O_PASE_E, P_O_SUMA]},
            ],
        },
        'Semana': {
            'celdas': celdas_s,
            'tablas': [
                {'titulo': 'Las 52 semanas ISO de la cocina',
                 'cols': [[t, c, {'ent': 'num', 'dec1': 'num', 'dec2': 'num',
                                  'dec3': 'num', 'pct': 'pct1',
                                  'fecha': 'txt', 'txt': 'txt'}[k]]
                          for c, t, k in _cols_semana()],
                 'filas': [S_INI, S_TOT]},
            ],
        },
        'KPI y Definiciones': {
            'celdas': {},
            'tablas': [
                {'titulo': 'Los siete KPI de cocina',
                 'cols': [['Indicador', 'A', 'txt'],
                          ['Cómo se calcula', 'B', 'txt'],
                          ['Unidad', 'C', 'txt'],
                          ['Error típico', 'D', 'txt'],
                          ['Cadencia', 'E', 'txt'],
                          ['Objetivo de la casa', 'F', 'txt'],
                          ['De dónde sale el dato', 'G', 'txt']],
                 'filas': [K_INI, K_FIN]},
            ],
        },
        'Comparativa entre Unidades': {
            'celdas': celdas_c,
            'tablas': [
                {'titulo': 'Comparativa entre unidades del mes cerrado',
                 'cols': [['Unidad', 'A', 'txt'],
                          ['Cubiertos del mes', 'B', 'num'],
                          ['Merma global (%)', 'C', 'pct1'],
                          ['Pase de principales (min)', 'D', 'num'],
                          ['Incidencias de alérgenos por base', 'E', 'num'],
                          ['Horas de cocina por cubierto', 'F', 'num'],
                          ['Platos devueltos por base', 'G', 'num'],
                          ['Indicadores dentro del estándar', 'N', 'num'],
                          ['Posición', 'O', 'num']],
                 'filas': [C_UINI, C_UINI + len(D.UNIDADES) - 1]},
            ],
        },
    }
    referencias = {}
    for hoja, cont in hojas.items():
        for desc, coord in cont['celdas'].items():
            referencias[desc] = hoja + '!' + coord
    return {
        'fichero': NOMBRE + '.xlsx',
        'producto': PID,
        'semanas_malas': list(D.SEMANAS_MALAS_COCINA),
        'mes_comparativa': D.UNIDADES_MES,
        'hojas': hojas,
        'referencias': referencias,
    }


def main():
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_parametros(wb)
    hoja_semana(wb)
    hoja_kpi(wb)
    hoja_comparativa(wb)

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
