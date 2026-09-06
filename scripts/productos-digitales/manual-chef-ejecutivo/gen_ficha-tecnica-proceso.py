#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_ficha-tecnica-proceso.py — libro 3 de «Manual del Chef Ejecutivo»
(SPEC §2.2 fila 3).

Hojas: Instrucciones · Ficha (plantilla) · Ficha (ejemplo) · Índice de Fichas.

QUÉ DECIDE ESTE LIBRO
---------------------
Que el plato salga igual lo haga quien lo haga. No es un escandallo y no es una
matriz de alérgenos de carta: es el PROCESO de una elaboración, escrito para que
otra persona lo repita.

LAS TRES REGLAS QUE LO SEPARAN DEL RESTO DEL CATÁLOGO
-----------------------------------------------------
* **El coste NO se calcula aquí (SPEC D4).** «Coste por ración copiado del
  escandallo» es una celda VERDE sin fórmula, con su nota y el enlace de texto
  al Kit de Escandallos / Guía Food Cost. Cero fórmulas entre ficheros en todo
  el pack: si mañana sube el precio de compra, se actualiza allí y se vuelve a
  copiar aquí. Lo único que este libro hace con ese número es multiplicarlo por
  las raciones que se venden al mes, para que el chef vea qué le cuesta el plato
  al mes en materia prima.
* **Alérgenos DE PROCESO (SPEC D5).** Esta tabla dice dónde entra cada alérgeno
  en ESTA elaboración, si es traza, si es utensilio compartido y si se puede
  sustituir. La declaración de carta —los 14 alérgenos por plato, la que lee el
  cliente— vive en `pack-appcc/08-matriz-alergenos.xlsx` y aquí sólo se remite a
  ella. Nunca las dos declaraciones completas.
* **El «Índice de Fichas» es MANUAL (SPEC D4).** Excel sólo podría leer el
  nombre de otra hoja con `INDIRECT`, que está prohibida en la familia porque la
  rompen Google Sheets y los visores móviles. Se escribe a mano, lo dice la hoja
  «Instrucciones» en voz alta, y a cambio el índice hace lo único que de verdad
  hace falta: contar cuántos platos de la carta NO tienen ficha.

DECISIONES TÉCNICAS
-------------------
* La ficha se construye DOS VECES con la misma función (`hoja_ficha`): una vacía
  (plantilla, para imprimir y rellenar) y otra con el plato P1 del caso modelado.
  Así no pueden desincronizarse, que es lo que pasa cuando se copian a mano.
* Ninguna lista desplegable se arma con comas dentro de una cadena: todas van
  contra un RANGO de la propia hoja (bloque «Listas de referencia»), que además
  documenta el vocabulario cerrado del libro.
* La temperatura mínima de mantenimiento en caliente es una celda verde con su
  nota legal (CE-10, art. 30.2 del RD 1086/2020): el semáforo compara contra esa
  celda, nunca contra un 63 escrito dentro de una fórmula.
* «Sin dato» = `""`, nunca 0. La antigüedad de una ficha sin fecha no es «hoy».
* Cero constantes dentro de las fórmulas de cálculo; `IFERROR(...,"")` en todo
  cociente; semáforos con `ISNUMBER`; prohibidas `INDIRECT`, `COUNTA`, `PMT`,
  `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA`, `RANK` y `NETWORKDAYS`: cero usos.
* Textos 100 % WinAnsi (cp1252): ni un carácter fuera.
* Término único «partida» (SPEC D9); la glosa «(estación)» se escribe UNA vez,
  en el primer paso de «Instrucciones».

Salida fija: build/ficha-tecnica-proceso.xlsx + build/mapa-ficha-tecnica-proceso.json
Via: Claude Code
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
TITULO = 'Ficha técnica de proceso'
NOMBRE = 'ficha-tecnica-proceso'

FMT_EUR = motor.FMT_EUR
FMT_PCT = motor.FMT_PCT
FMT_ENT = motor.FMT_ENT
FMT_FECHA = motor.FMT_FECHA
FMT_DEC = '#,##0.0'

GRIS = 'F2F2F2'
CREMA = 'FFF6DC'
ORO = 'FFD700'
CABECERA = '2D2D2D'

FECHA_VERIF = '06-09-2026'

H_PLANTILLA = 'Ficha (plantilla)'
H_EJEMPLO = 'Ficha (ejemplo)'
H_INDICE = 'Índice de Fichas'


# --------------------------------------------------------------------------
def sector(idd):
    """Devuelve la entrada `CE-*`/`MM-*`/`CS-*` del JSON de research.

    Regla de familia: ninguna cifra legal ni de sector se teclea en el
    generador. Se lee del JSON, que lleva norma, URL y fiabilidad.
    """
    ruta = os.path.join(RAIZ, 'auditorias', 'guias-v2-research-sector.json')
    with open(ruta, encoding='utf-8') as fh:
        datos = json.load(fh)['datos']
    for it in datos:
        if it.get('id') == idd:
            return it
    raise KeyError('id de research inexistente: ' + idd)


def verificado(idd):
    """Nota legal de familia: «Verificado el <fecha> · <norma> · <URL>»."""
    it = sector(idd)
    return ('Verificado el ' + FECHA_VERIF + ' · ' + it['fuente_titulo']
            + ' · ' + it['url'])


CE01 = sector('CE-01')      # contaminación cruzada: equipo y utensilio
CE06 = sector('CE-06')      # 14 alérgenos, el cartel no basta
CE08 = sector('CE-08')      # estudio de vida útil (Listeria)
CE10 = sector('CE-10')      # temperaturas
CE13 = sector('CE-13')      # tres fechas al congelar
CE35 = sector('CE-35')      # V gama < 4 °C
CE37 = sector('CE-37')      # no hay cifra legal de días de vida útil
MM31 = sector('MM-31')      # soporte escrito de la información de alérgenos


# --------------------------------------------------------------------------
# Vocabulario cerrado del libro (todo sale de `datos_ejemplo`)
# --------------------------------------------------------------------------
F = D.FICHA_TECNICA_EJEMPLO

PARTIDAS = [p[0] for p in D.PARTIDAS]
FAMILIAS = sorted(set(p[2] for p in D.PLATOS))
#: Estados de la tabla de alérgenos DE PROCESO (SPEC D5).
ESTADOS_ALERGENO = ['Presente', 'Traza en esta elaboración',
                    'Utensilio o superficie compartidos', 'No interviene']
SI_NO = ['Sí', 'No']
ESTADOS_FICHA = ['Cerrada', 'Pendiente de cerrar', 'Toca revisarla',
                 'Sin ficha']

#: El plato de la ficha de ejemplo, tal y como lo ve la carta de la Guía Food
#: Cost: de ahí salen las unidades al mes (no se teclean).
MIX_P1 = [m for m in D.MIX_VENTA if m['id'] == F['id_plato']][0]
#: Fecha de elaboración del lote del ejemplo: la del stock elaborado de ese
#: mismo plato (libro 2). Ni una fecha inventada.
LOTE_P1 = [s for s in D.STOCK_ELABORADO if s[0] == F['id_plato']][0]
FECHA_LOTE = D._fecha(LOTE_P1[4])
FECHA_CONTROL = D._fecha(D.PARAMETROS_COCINA['fecha_corte_normativa'])

N_PASOS = 12
N_ALERGENOS = 12
N_CONSERVA = 8
N_INDICE = 30


# --------------------------------------------------------------------------
# Utilidades de formato (mismo molde que el libro 1 del Manual del Manager)
# --------------------------------------------------------------------------
def cabecera(ws, fila, columnas, altura=32):
    for letra, texto in columnas:
        c = ws[letra + str(fila)]
        c.value = texto
        c.fill = PatternFill('solid', fgColor=CABECERA)
        c.font = Font(bold=True, color='FFFFFF')
        c.alignment = Alignment(horizontal='center', vertical='center',
                                wrap_text=True)
    ws.row_dimensions[fila].height = altura


def pintar_cabecera(ws, rango):
    """Extiende el fondo de cabecera a las celdas combinadas de la derecha."""
    for fila in ws[rango]:
        for c in fila:
            c.fill = PatternFill('solid', fgColor=CABECERA)


def seccion(ws, coord, texto):
    motor.val(ws, coord, texto, bold=True)
    ws[coord].font = Font(bold=True, size=12)


def parrafo(ws, fila, texto, col_fin='F', alto=30, cursiva=True):
    """Nota a lo ancho de la ficha, combinada y con altura fija."""
    ws.merge_cells('A%d:%s%d' % (fila, col_fin, fila))
    motor.val(ws, 'A%d' % fila, texto, wrap=True)
    if cursiva:
        ws['A%d' % fila].font = Font(italic=True, size=9)
    ws.row_dimensions[fila].height = alto


def anchos(ws, mapa):
    for letra, ancho in mapa.items():
        ws.column_dimensions[letra].width = ancho


def pagina(ws, apaisado=False, titulos=None, area=None):
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


def encabezar(ws, titulo, nota=None):
    motor.val(ws, 'A1', titulo)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', SUBTITULO)
    if nota:
        ws.merge_cells('A3:F3')
        motor.val(ws, 'A3', nota, wrap=True)
        ws['A3'].font = Font(italic=True, size=9)
        ws.row_dimensions[3].height = 26


def dv_rango(ws, coords, ref, titulo, mensaje):
    """Desplegable cuyo origen es un RANGO de la propia hoja (SPEC §2.2).

    `motor.dv_lista` une las opciones con comas dentro de una cadena; el pack
    exige rango, que además deja el vocabulario a la vista del que rellena.
    """
    dv = DataValidation(type='list', formula1=ref, allow_blank=True,
                        showErrorMessage=True, errorTitle=titulo,
                        error=mensaje)
    ws.add_data_validation(dv)
    for c in coords:
        dv.add(c)
    return dv


def campo(ws, fila, etiqueta, valor=None, fmt=None, col_valor='B',
          col_fin=None, nota=None):
    """Etiqueta en A y celda VERDE de entrada a su derecha."""
    motor.val(ws, 'A%d' % fila, etiqueta, bold=True, wrap=True)
    coord = '%s%d' % (col_valor, fila)
    if col_fin:
        ws.merge_cells('%s%d:%s%d' % (col_valor, fila, col_fin, fila))
    motor.val(ws, coord, valor if valor is not None else '', fmt=fmt,
              wrap=True)
    motor.verde(ws, coord)
    if nota:
        motor.val(ws, 'E%d' % fila, nota, wrap=True)
        ws['E%d' % fila].font = Font(italic=True, size=9)
    return coord


# --------------------------------------------------------------------------
# Hoja «Instrucciones»
# --------------------------------------------------------------------------
PASOS = [
    '1. Este libro tiene DOS fichas iguales: «Ficha (plantilla)», vacía, para '
    'imprimir o duplicar por cada plato, y «Ficha (ejemplo)», rellena con un '
    'plato del restaurante de ejemplo para que veas hasta dónde llega el '
    'detalle. Copia la plantilla una vez por plato y cámbiale el nombre a la '
    'pestaña. Todo lo que este libro llama partida (estación, en el vocabulario '
    'de la matriz de polivalencia del Manual del Manager) es la unidad de '
    'trabajo de tu cocina: pase, fríos, postres, barra.',
    '2. Rellena primero la identificación: código, nombre, familia, partida que '
    'lo produce, cuántas raciones rinde la ficha, versión y fecha de revisión. '
    'La versión y la fecha no son burocracia: son lo que te deja saber si el '
    'cocinero está mirando la ficha buena o una impresión de hace ocho meses.',
    '3. El COSTE por ración se COPIA de tu escandallo; esta hoja no calcula '
    'costes y no está enlazada con ningún otro fichero. Está así a propósito: '
    'un enlace entre ficheros se rompe en cuanto alguien mueve una carpeta, y '
    'entonces la ficha miente sin avisar. Si cambia el precio de compra, se '
    'actualiza en el escandallo y se vuelve a copiar aquí.',
    '4. Escribe los pasos como se los dirías a alguien que entra hoy: una '
    'operación por línea, con el gramaje, el tiempo y la temperatura dentro de '
    'la frase. La columna «Punto de control» es para lo que hay que COMPROBAR '
    'en ese paso (temperatura en el centro, textura, peso de la ración).',
    '5. Temperaturas: la celda «temperatura mínima de mantenimiento en '
    'caliente» viene con el mínimo legal y su norma al lado. Si el plato se '
    'mantiene en caliente antes de servirse, escribe la temperatura que mides '
    'de verdad en la celda de al lado y la ficha te dice si estás por debajo. '
    'Si el plato sale directo del fuego al pase, deja esa casilla vacía.',
    '6. La tabla de ALÉRGENOS de esta ficha es de PROCESO: dice dónde entra '
    'cada alérgeno en ESTA elaboración, si es traza, si viene de un utensilio o '
    'una superficie compartidos, y si se puede sustituir. La declaración de '
    'carta —los 14 alérgenos por plato, la que se le enseña al cliente— se hace '
    'en la matriz de alérgenos del Pack APPCC; aquí no se duplica.',
    '7. Conservación y vida útil: escribe cada elaboración intermedia con su '
    'conservación y sus días. Pon la fecha del lote arriba y la hoja te calcula '
    'el consumo preferente de cada una. Los días los fijas tú y los documentas: '
    'no existe una tabla legal que diga cuánto dura una salsa.',
    '8. Hoja «Índice de Fichas»: se escribe A MANO, una línea por plato de tu '
    'carta. Es lo único que te dice cuántos platos vendes sin ficha, que es el '
    'número que de verdad importa el día que falta el jefe de partida.',
]

NOTAS_LIBRO = [
    'ESTA FICHA NO ES UN ESCANDALLO. El escandallo dice cuánto cuesta un plato; '
    'la ficha técnica de proceso dice cómo se hace para que salga igual. Se '
    'usan a la vez y cada una vive en su sitio: el coste, en el Kit de '
    'Escandallos o en la Guía Food Cost + Ingeniería de Menú; el proceso, aquí.',
    'ESTA FICHA NO ES LA DECLARACIÓN DE ALÉRGENOS DE LA CARTA. La declaración '
    'por plato, con los 14 alérgenos de declaración obligatoria, se hace en la '
    'matriz de alérgenos del Pack APPCC. Aquí van los alérgenos de PROCESO de '
    'una sola elaboración. Duplicar las dos declaraciones es la forma más '
    'rápida de que un día digan cosas distintas.',
    'Por qué el índice es manual: para rellenarse solo, Excel tendría que leer '
    'el nombre de cada pestaña con INDIRECT, una función que Google Sheets y '
    'los visores del móvil no resuelven igual. Antes que un índice que a veces '
    'funciona, un índice que se escribe a mano y siempre dice la verdad.',
    'La ficha se cierra cuando alguien que no la escribió ejecuta el plato con '
    'ella delante y sale igual. Hasta entonces está en borrador, aunque esté '
    'escrita: eso es lo que mide la columna «ficha cerrada» del índice.',
    'Cambiar el gramaje o el proceso de un plato que ya está en carta obliga a '
    'subir la versión y la fecha de revisión, y a decírselo a la partida. Una '
    'ficha nueva con la versión de la anterior es peor que no tener ficha.',
]


def hoja_instrucciones(wb):
    ws = wb.create_sheet('Instrucciones', 0)
    anchos(ws, {'A': 110.0})
    motor.val(ws, 'A1', TITULO)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', SUBTITULO)
    motor.val(ws, 'A3', 'Para qué sirve: que el plato salga igual lo haga quien '
                        'lo haga.')
    ws['A3'].font = Font(italic=True, size=9)

    seccion(ws, 'A5', 'Instrucciones de uso')
    fila = 6
    for paso in PASOS:
        motor.val(ws, 'A%d' % fila, paso, wrap=True)
        ws.row_dimensions[fila].height = 44
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, motor.NOTA_VERDES)
    ws['A%d' % fila].fill = PatternFill('solid', fgColor=motor.VERDE)
    fila += 2

    seccion(ws, 'A%d' % fila, 'Lo que conviene saber antes de empezar')
    fila += 1
    for texto in NOTAS_LIBRO:
        motor.val(ws, 'A%d' % fila, texto, wrap=True)
        ws.row_dimensions[fila].height = 44
        fila += 1
    fila += 1

    seccion(ws, 'A%d' % fila, 'Cada cuánto se usa este libro')
    fila += 1
    motor.val(ws, 'A%d' % fila,
              'Cadencia: UNA VEZ por plato, y cada vez que cambie el proceso o '
              'el gramaje. El índice se repasa al cerrar cada carta de '
              'temporada.', wrap=True)
    ws.row_dimensions[fila].height = 30
    fila += 2

    seccion(ws, 'A%d' % fila, 'Lo que este libro NO hace (y dónde se hace)')
    fila += 1
    for texto in (
            'Coste por ración, escandallo y rendimiento: Kit de Escandallos y '
            'Guía Food Cost + Ingeniería de Menú.',
            'Declaración de alérgenos por plato para el cliente (14 columnas): '
            'Pack APPCC, matriz de alérgenos.',
            'Registros de temperaturas, limpieza y plagas: Pack APPCC.',
            'Cuánto hay que producir hoy de cada partida: libro 2 de este mismo '
            'manual, planificación de producción semanal.',
            'Quién puede cubrir una partida: matriz de polivalencia del Manual '
            'del Manager de Restaurante.'):
        motor.val(ws, 'A%d' % fila, texto, wrap=True)
        ws.row_dimensions[fila].height = 30
        fila += 1
    fila += 1

    motor.val(ws, 'A%d' % fila, D.NOTA_DESPROTEGER)
    fila += 1
    motor.val(ws, 'A%d' % fila,
              'Ruta en Excel: Revisar > Desproteger hoja. La protección no '
              'tiene contraseña; sirve para no pisar una fórmula sin querer.')
    fila += 2
    motor.val(ws, 'A%d' % fila, D.BIO)
    fila += 1
    motor.val(ws, 'A%d' % fila, D.VERSION_LINE)
    pagina(ws)
    return ws


# --------------------------------------------------------------------------
# Hojas «Ficha (plantilla)» y «Ficha (ejemplo)»
# --------------------------------------------------------------------------
#: Coordenadas de la ficha. Las dos hojas se construyen con la MISMA función,
#: así que estas filas valen para las dos y son el contrato del guion.
R_ID = 5
R_COD, R_NOM, R_FAM, R_PAR = 6, 7, 8, 9
R_RAC, R_VER, R_FEC, R_REV = 10, 11, 12, 13
R_COSTE_SEC = 15
R_COSTE, R_UDS, R_COSTE_MES = 16, 17, 18
R_COSTE_N1, R_COSTE_N2 = 19, 20
R_PASOS_SEC = 22
R_PASOS_CAB = 23
R_PASOS_INI = 24
R_PASOS_FIN = R_PASOS_INI + N_PASOS - 1              # 35
R_TECNICAS = R_PASOS_FIN + 2                         # 37
R_TIEMPOS_SEC = R_TECNICAS + 2                       # 39
R_MEP, R_PASE, R_REPOSO, R_TIEMPO = (R_TIEMPOS_SEC + 1, R_TIEMPOS_SEC + 2,
                                     R_TIEMPOS_SEC + 3, R_TIEMPOS_SEC + 4)
R_TEMP_SEC = R_TIEMPO + 2                            # 46
R_PUNTO = R_TEMP_SEC + 1                             # 47
R_TMIN = R_TEMP_SEC + 2                              # 48
R_TMIN_N = R_TEMP_SEC + 3                            # 49
R_TSERV = R_TEMP_SEC + 4                             # 50
R_TLECT = R_TEMP_SEC + 5                             # 51
R_TEMP_N = R_TEMP_SEC + 6                            # 52
R_MONTAJE_SEC = R_TEMP_N + 2                         # 54
R_MONTAJE = R_MONTAJE_SEC + 1                        # 55
R_MONTAJE_N = R_MONTAJE_SEC + 2                      # 56
R_ALE_SEC = R_MONTAJE_N + 2                          # 58
R_ALE_N1 = R_ALE_SEC + 1                             # 59
R_ALE_CAB = R_ALE_SEC + 2                            # 60
R_ALE_INI = R_ALE_CAB + 1                            # 61
R_ALE_FIN = R_ALE_INI + N_ALERGENOS - 1              # 72
R_LEY_CAB = R_ALE_FIN + 2                            # 74
R_LEY_INI = R_LEY_CAB + 1                            # 75
R_LEY_FIN = R_LEY_INI + len(ESTADOS_ALERGENO) - 1    # 78
R_CNT_INI = R_LEY_FIN + 2                            # 80
R_ALE_N2 = R_CNT_INI + 3                             # 83
R_ALE_N3 = R_CNT_INI + 4                             # 84
R_CON_SEC = R_ALE_N3 + 2                             # 86
R_LOTE = R_CON_SEC + 1                               # 87
R_CON_CAB = R_CON_SEC + 2                            # 88
R_CON_INI = R_CON_CAB + 1                            # 89
R_CON_FIN = R_CON_INI + N_CONSERVA - 1               # 96
R_CON_N1 = R_CON_FIN + 1                             # 97
R_CON_N2 = R_CON_FIN + 2                             # 98
R_CON_N3 = R_CON_FIN + 3                             # 99
R_PIE = R_CON_N3 + 2                                 # 101
R_LIST_SEC = R_PIE + 3                               # 104
R_LIST_CAB = R_LIST_SEC + 1                          # 105
R_LIST_INI = R_LIST_CAB + 1                          # 106
R_LIST_FIN = R_LIST_INI + max(len(PARTIDAS),
                              len(FAMILIAS)) - 1     # 111


def hoja_ficha(wb, titulo_hoja, relleno):
    """Construye una ficha. `relleno=False` deja todas las celdas verdes vacías.

    Las dos hojas del libro salen de aquí: la plantilla y el ejemplo no pueden
    desincronizarse porque no se copian, se generan.
    """
    ws = wb.create_sheet(titulo_hoja)
    anchos(ws, {'A': 36, 'B': 22, 'C': 22, 'D': 26, 'E': 34, 'F': 26})
    encabezar(ws, 'Ficha técnica de proceso'
              + (' — ejemplo relleno' if relleno else ' — plantilla'),
              nota=('Ejemplo del restaurante modelado del manual: un plato real '
                    'de la carta, con su proceso completo. Cambia lo que quieras: '
                    'todas las celdas verdes son tuyas.') if relleno else
                   ('Duplica esta hoja una vez por plato. Todas las celdas '
                    'verdes son editables; el resto se calcula o es texto fijo.'))

    # ---------------- identificación -------------------------------------
    seccion(ws, 'A%d' % R_ID, 'IDENTIFICACIÓN DE LA FICHA')
    campo(ws, R_COD, 'Código del plato', F['id_plato'] if relleno else '')
    campo(ws, R_NOM, 'Nombre del plato', F['plato'] if relleno else '',
          col_fin='D')
    campo(ws, R_FAM, 'Familia', F['familia'] if relleno else '')
    campo(ws, R_PAR, 'Partida que lo produce', F['partida'] if relleno else '')
    campo(ws, R_RAC, 'Raciones que rinde la ficha',
          float(F['raciones_ficha']) if relleno else '', fmt=FMT_ENT)
    campo(ws, R_VER, 'Versión de la ficha', F['version'] if relleno else '')
    campo(ws, R_FEC, 'Fecha de revisión',
          D._fecha(F['fecha_revision']) if relleno else '', fmt=FMT_FECHA)
    campo(ws, R_REV, 'Revisada por', F['revisada_por'] if relleno else '',
          col_fin='D')
    motor.val(ws, 'E%d' % R_VER,
              'Sube la versión cada vez que cambies gramaje, proceso o '
              'montaje.', wrap=True)
    ws['E%d' % R_VER].font = Font(italic=True, size=9)

    # ---------------- coste (SPEC D4) ------------------------------------
    seccion(ws, 'A%d' % R_COSTE_SEC,
            'COSTE — SE COPIA DEL ESCANDALLO; ESTA HOJA NO LO CALCULA')
    campo(ws, R_COSTE, 'Coste por ración copiado del escandallo (€)',
          float(F['coste_racion_copiado']) if relleno else '', fmt=FMT_EUR)
    campo(ws, R_UDS, 'Raciones vendidas al mes (referencia de la carta)',
          float(MIX_P1['uds_mes']) if relleno else '', fmt=FMT_ENT)
    motor.val(ws, 'A%d' % R_COSTE_MES,
              'Coste de materia prima al mes de este plato (€)', bold=True,
              wrap=True)
    motor.f(ws, 'B%d' % R_COSTE_MES,
            '=IFERROR(IF(OR($B${c}="",$B${u}=""),"",$B${c}*$B${u}),"")'
            .format(c=R_COSTE, u=R_UDS), fmt=FMT_EUR, bold=True)
    ws['B%d' % R_COSTE_MES].fill = PatternFill('solid', fgColor=CREMA)
    parrafo(ws, R_COSTE_N1, F['nota_coste'], alto=30)
    parrafo(ws, R_COSTE_N2,
            'Es coste de MATERIA PRIMA, nada más: ni personal, ni energía, ni '
            'la merma de la partida. Sirve para saber qué plato mueve de '
            'verdad tu compra, no para fijar el precio de venta.', alto=26)

    # ---------------- proceso --------------------------------------------
    seccion(ws, 'A%d' % R_PASOS_SEC, 'PROCESO: PASOS DE ELABORACIÓN')
    cabecera(ws, R_PASOS_CAB, [('A', 'Nº'), ('B', 'Operación'),
                               ('F', 'Punto de control')], altura=22)
    ws.merge_cells('B%d:E%d' % (R_PASOS_CAB, R_PASOS_CAB))
    pintar_cabecera(ws, 'B%d:E%d' % (R_PASOS_CAB, R_PASOS_CAB))
    pasos = dict((n, t) for n, t in F['pasos']) if relleno else {}
    puntos_control = dict((n, t) for n, t in F['puntos_control']) if relleno else {}
    for i in range(N_PASOS):
        r = R_PASOS_INI + i
        motor.val(ws, 'A%d' % r, i + 1, fmt=FMT_ENT, align='center')
        ws.merge_cells('B%d:E%d' % (r, r))
        motor.val(ws, 'B%d' % r, pasos.get(i + 1, ''), wrap=True)
        motor.verde(ws, 'B%d' % r)
        motor.val(ws, 'F%d' % r, puntos_control.get(i + 1, ''), wrap=True)
        motor.verde(ws, 'F%d' % r)
        ws.row_dimensions[r].height = 30
    motor.val(ws, 'A%d' % R_TECNICAS, 'Técnicas empleadas', bold=True)
    ws.merge_cells('B%d:F%d' % (R_TECNICAS, R_TECNICAS))
    motor.val(ws, 'B%d' % R_TECNICAS, F['tecnicas'] if relleno else '',
              wrap=True)
    motor.verde(ws, 'B%d' % R_TECNICAS)

    # ---------------- tiempos --------------------------------------------
    seccion(ws, 'A%d' % R_TIEMPOS_SEC, 'TIEMPOS')
    t = F['tiempos']
    campo(ws, R_MEP, 'Mise en place (minutos)',
          float(t['mise_en_place_min']) if relleno else '', fmt=FMT_ENT)
    campo(ws, R_PASE, 'Tiempo de pase, de la comanda al pase (minutos)',
          float(t['pase_min']) if relleno else '', fmt=FMT_ENT)
    campo(ws, R_REPOSO, 'Reposo (minutos)',
          float(t['reposo_min']) if relleno else '', fmt=FMT_ENT)
    motor.val(ws, 'A%d' % R_TIEMPO, 'Tiempo total de la elaboración (minutos)',
              bold=True, wrap=True)
    motor.f(ws, 'B%d' % R_TIEMPO,
            '=IF(COUNT($B${a}:$B${b})=0,"",SUM($B${a}:$B${b}))'
            .format(a=R_MEP, b=R_REPOSO), fmt=FMT_ENT, bold=True)
    ws['B%d' % R_TIEMPO].fill = PatternFill('solid', fgColor=CREMA)
    motor.val(ws, 'E%d' % R_PASE,
              'El tiempo de pase de esta ficha es el que alimenta el control de '
              'calidad del pase (libro 5).', wrap=True)
    ws['E%d' % R_PASE].font = Font(italic=True, size=9)

    # ---------------- punto y temperaturas -------------------------------
    seccion(ws, 'A%d' % R_TEMP_SEC, 'PUNTO Y TEMPERATURAS')
    campo(ws, R_PUNTO, 'Punto de cocción y temperatura en el centro',
          F['punto'] if relleno else '', col_fin='F')
    campo(ws, R_TMIN,
          'Temperatura mínima de mantenimiento en caliente (°C)',
          float(F['temperatura_servicio_c']), fmt=FMT_ENT)
    parrafo(ws, R_TMIN_N,
            'Si el plato o alguno de sus componentes se mantiene en caliente '
            'antes de servirse, la temperatura no puede bajar de esa cifra. La '
            'norma admite otra temperatura si demuestras ante la autoridad que '
            'es segura (art. 30.5) y otro recalentamiento si documentas su '
            'equivalencia (art. 30.7). ' + verificado('CE-10'), alto=42)
    campo(ws, R_TSERV, 'Temperatura de servicio medida (°C)', '', fmt=FMT_ENT)
    motor.val(ws, 'A%d' % R_TLECT, 'Lectura de la temperatura de servicio',
              bold=True, wrap=True)
    ws.merge_cells('B%d:D%d' % (R_TLECT, R_TLECT))
    motor.f(ws, 'B%d' % R_TLECT,
            '=IF(OR(NOT(ISNUMBER($B${s})),NOT(ISNUMBER($B${m}))),"",'
            'IF($B${s}>=$B${m},"Correcta","POR DEBAJO DEL MÍNIMO"))'
            .format(s=R_TSERV, m=R_TMIN), bold=True)
    parrafo(ws, R_TEMP_N,
            'Si el plato sale del fuego directo al pase, deja vacía la casilla '
            'de temperatura medida: la lectura se queda en blanco, que es lo '
            'que quiere decir «aquí no aplica». Vacío no es cero.', alto=30)

    # ---------------- montaje --------------------------------------------
    seccion(ws, 'A%d' % R_MONTAJE_SEC, 'MONTAJE Y PRESENTACIÓN')
    ws.merge_cells('A%d:F%d' % (R_MONTAJE, R_MONTAJE))
    motor.val(ws, 'A%d' % R_MONTAJE, F['montaje'] if relleno else '',
              wrap=True)
    motor.verde(ws, 'A%d' % R_MONTAJE)
    ws.row_dimensions[R_MONTAJE].height = 54
    parrafo(ws, R_MONTAJE_N,
            'Pega aquí la foto del montaje bueno, el que sale cuando lo hace '
            'quien mejor lo hace. Una ficha sin foto se interpreta, y una ficha '
            'que se interpreta no es un estándar.', alto=26)

    # ---------------- alérgenos de proceso (SPEC D5) ---------------------
    seccion(ws, 'A%d' % R_ALE_SEC, 'ALÉRGENOS DE PROCESO DE ESTA ELABORACIÓN')
    parrafo(ws, R_ALE_N1, F['nota_alergenos'], alto=42)
    cabecera(ws, R_ALE_CAB, [('A', 'Alérgeno'),
                             ('B', 'Estado en esta elaboración'),
                             ('C', 'Dónde entra en ESTA elaboración'),
                             ('E', 'Sustitución posible')], altura=32)
    ws.merge_cells('C%d:D%d' % (R_ALE_CAB, R_ALE_CAB))
    ws.merge_cells('E%d:F%d' % (R_ALE_CAB, R_ALE_CAB))
    pintar_cabecera(ws, 'C%d:F%d' % (R_ALE_CAB, R_ALE_CAB))
    filas_ale = F['alergenos_proceso'] if relleno else []
    v_estado = []
    for i in range(N_ALERGENOS):
        r = R_ALE_INI + i
        dato = filas_ale[i] if i < len(filas_ale) else ('', '', '', '')
        motor.val(ws, 'A%d' % r, dato[0], wrap=True)
        motor.verde(ws, 'A%d' % r)
        motor.val(ws, 'B%d' % r, dato[1], wrap=True)
        motor.verde(ws, 'B%d' % r)
        ws.merge_cells('C%d:D%d' % (r, r))
        motor.val(ws, 'C%d' % r, dato[2], wrap=True)
        motor.verde(ws, 'C%d' % r)
        ws.merge_cells('E%d:F%d' % (r, r))
        motor.val(ws, 'E%d' % r, dato[3], wrap=True)
        motor.verde(ws, 'E%d' % r)
        ws.row_dimensions[r].height = 32
        v_estado.append('B%d' % r)

    cabecera(ws, R_LEY_CAB, [('A', 'Estado'), ('B', 'Qué quiere decir')],
             altura=20)
    ws.merge_cells('B%d:F%d' % (R_LEY_CAB, R_LEY_CAB))
    pintar_cabecera(ws, 'B%d:F%d' % (R_LEY_CAB, R_LEY_CAB))
    glosas = (
        'El alérgeno es un ingrediente de esta elaboración.',
        'No es ingrediente, pero puede llegar por una materia prima de '
        'proveedor: hay que comprobar su ficha.',
        'No es ingrediente ni traza de la materia prima: entra por un utensilio '
        'o una superficie que se comparten con otra elaboración.',
        'Ni ingrediente, ni traza, ni contacto: en esta elaboración no aparece.')
    for i, estado in enumerate(ESTADOS_ALERGENO):
        r = R_LEY_INI + i
        motor.val(ws, 'A%d' % r, estado, bold=True, wrap=True)
        ws.merge_cells('B%d:F%d' % (r, r))
        motor.val(ws, 'B%d' % r, glosas[i], wrap=True)
        ws.row_dimensions[r].height = 26
    dv_rango(ws, v_estado,
             "'%s'!$A$%d:$A$%d" % (titulo_hoja, R_LEY_INI, R_LEY_FIN),
             'Estado del alérgeno',
             'Elige uno de los cuatro estados de la leyenda de abajo.')

    etiquetas_cnt = (
        ('Alérgenos presentes como ingrediente', R_LEY_INI),
        ('Alérgenos por traza en esta elaboración', R_LEY_INI + 1),
        ('Alérgenos por utensilio o superficie compartidos', R_LEY_INI + 2))
    for i, (etiqueta, fila_ley) in enumerate(etiquetas_cnt):
        r = R_CNT_INI + i
        motor.val(ws, 'A%d' % r, etiqueta, bold=True, wrap=True)
        motor.f(ws, 'B%d' % r,
                '=IFERROR(COUNTIF($B${a}:$B${b},$A${l}),"")'
                .format(a=R_ALE_INI, b=R_ALE_FIN, l=fila_ley), fmt=FMT_ENT,
                bold=True)
        ws['B%d' % r].fill = PatternFill('solid', fgColor=CREMA)
    parrafo(ws, R_ALE_N2,
            'El utensilio y la superficie compartidos no son una manía: el '
            'equipo o el recipiente que ha tocado un alérgeno no se puede '
            'reutilizar para un alimento sin ese alérgeno salvo limpieza y '
            'comprobación de que no quedan restos visibles. ' + verificado('CE-01'),
            alto=42)
    parrafo(ws, R_ALE_N3,
            'Y el cartel de «consulte al personal» no basta por sí solo: la '
            'información oral sólo vale si además está escrita y accesible al '
            'personal, a la autoridad de control y a quien la pida. '
            + verificado('MM-31'), alto=42)

    # ---------------- conservación y vida útil ---------------------------
    seccion(ws, 'A%d' % R_CON_SEC, 'CONSERVACIÓN Y VIDA ÚTIL')
    campo(ws, R_LOTE, 'Fecha de elaboración del lote',
          FECHA_LOTE if relleno else '', fmt=FMT_FECHA)
    motor.val(ws, 'E%d' % R_LOTE,
              'Cámbiala y se recalculan todos los consumos preferentes de '
              'abajo.', wrap=True)
    ws['E%d' % R_LOTE].font = Font(italic=True, size=9)
    cabecera(ws, R_CON_CAB, [('A', 'Elaboración'), ('B', 'Conservación'),
                             ('D', 'Vida útil (días)'),
                             ('E', 'Consumo preferente'),
                             ('F', 'Comprobación')], altura=32)
    ws.merge_cells('B%d:C%d' % (R_CON_CAB, R_CON_CAB))
    pintar_cabecera(ws, 'B%d:C%d' % (R_CON_CAB, R_CON_CAB))
    filas_con = F['conservacion'] if relleno else []
    for i in range(N_CONSERVA):
        r = R_CON_INI + i
        dato = filas_con[i] if i < len(filas_con) else ('', '', '')
        motor.val(ws, 'A%d' % r, dato[0], wrap=True)
        motor.verde(ws, 'A%d' % r)
        ws.merge_cells('B%d:C%d' % (r, r))
        motor.val(ws, 'B%d' % r, dato[1], wrap=True)
        motor.verde(ws, 'B%d' % r)
        motor.val(ws, 'D%d' % r, float(dato[2]) if dato[2] else '',
                  fmt=FMT_ENT)
        motor.verde(ws, 'D%d' % r)
        motor.f(ws, 'E%d' % r,
                '=IFERROR(IF(OR($B${l}="",$D{r}=""),"",$B${l}+$D{r}),"")'
                .format(r=r, l=R_LOTE), fmt=FMT_FECHA)
        motor.val(ws, 'F%d' % r, '', wrap=True)
        motor.verde(ws, 'F%d' % r)
        ws.row_dimensions[r].height = 26
    parrafo(ws, R_CON_N1,
            F['vida_util_nota'] + ' ' + verificado('CE-37'), alto=42)
    parrafo(ws, R_CON_N2,
            'Si el plato es un listo para consumo que favorece el crecimiento '
            'de Listeria monocytogenes, los días no los pones a ojo: hace falta '
            'un estudio de vida útil documentado. ' + verificado('CE-08'),
            alto=42)
    parrafo(ws, R_CON_N3,
            'Al congelar una elaboración propia hacen falta TRES fechas: '
            'elaboración, congelación y caducidad del congelado. '
            + verificado('CE-13') + '. Y si envasas al vacío, la recomendación '
            'de la AESAN para la V gama es conservar por debajo de 4 °C. '
            + verificado('CE-35'), alto=54)

    motor.val(ws, 'A%d' % R_PIE, D.VERSION_LINE)
    ws['A%d' % R_PIE].font = Font(size=8, italic=True)

    # ---------------- listas de referencia (origen de los desplegables) --
    seccion(ws, 'A%d' % R_LIST_SEC,
            'LISTAS DE REFERENCIA DE LOS DESPLEGABLES (fuera del área de '
            'impresión)')
    cabecera(ws, R_LIST_CAB, [('A', 'Partidas'), ('B', 'Familias de carta')],
             altura=20)
    for i in range(R_LIST_FIN - R_LIST_INI + 1):
        r = R_LIST_INI + i
        if i < len(PARTIDAS):
            motor.val(ws, 'A%d' % r, PARTIDAS[i])
        if i < len(FAMILIAS):
            motor.val(ws, 'B%d' % r, FAMILIAS[i])
    dv_rango(ws, ['B%d' % R_PAR],
             "'%s'!$A$%d:$A$%d" % (titulo_hoja, R_LIST_INI,
                                   R_LIST_INI + len(PARTIDAS) - 1),
             'Partida', 'Elige una de las partidas de tu cocina.')
    dv_rango(ws, ['B%d' % R_FAM],
             "'%s'!$B$%d:$B$%d" % (titulo_hoja, R_LIST_INI,
                                   R_LIST_INI + len(FAMILIAS) - 1),
             'Familia de carta', 'Elige una familia de la carta.')

    # ---------------- validaciones y semáforos ---------------------------
    motor.dv_numerica(ws, ['B%d' % R_RAC, 'B%d' % R_UDS, 'B%d' % R_MEP,
                           'B%d' % R_PASE, 'B%d' % R_REPOSO]
                      + ['D%d' % r for r in range(R_CON_INI, R_CON_FIN + 1)],
                      minimo=0, titulo='Recuento')
    motor.dv_numerica(ws, ['B%d' % R_COSTE], minimo=0, titulo='Importe (€)')
    motor.dv_numerica(ws, ['B%d' % R_TMIN, 'B%d' % R_TSERV], minimo=-40,
                      maximo=300, titulo='Temperatura (°C)',
                      mensaje='Escribe la temperatura en grados centígrados.')
    motor.dv_fecha(ws, ['B%d' % R_FEC, 'B%d' % R_LOTE])
    motor.semaforo_texto(ws, 'B%d:D%d' % (R_TLECT, R_TLECT),
                         (('Correcta', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                          ('POR DEBAJO DEL MÍNIMO', motor.CF_ROJO_BG,
                           motor.CF_ROJO_FG)))
    motor.semaforo_texto(
        ws, 'B%d:B%d' % (R_ALE_INI, R_ALE_FIN),
        ((ESTADOS_ALERGENO[0], motor.CF_ROJO_BG, motor.CF_ROJO_FG),
         (ESTADOS_ALERGENO[1], motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
         (ESTADOS_ALERGENO[2], motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
         (ESTADOS_ALERGENO[3], motor.CF_GRIS_BG, motor.CF_GRIS_FG)))

    pagina(ws, area='A1:F%d' % R_PIE)
    ws.freeze_panes = 'A5'
    return ws


# --------------------------------------------------------------------------
# Hoja «Índice de Fichas» (MANUAL, SPEC D4)
# --------------------------------------------------------------------------
I_CTRL = 5           # fecha de control
I_AVISO = 6          # avisar si la ficha supera (días)
I_CAB = 9
I_INI = 10
I_FIN = I_INI + N_INDICE - 1                 # 39
I_LEY_CAB = I_FIN + 2                        # 41
I_LEY_INI = I_LEY_CAB + 1                    # 42
I_LEY_FIN = I_LEY_INI + len(ESTADOS_FICHA) - 1
I_SN_CAB = I_LEY_FIN + 2
I_SN_INI = I_SN_CAB + 1
I_SN_FIN = I_SN_INI + len(SI_NO) - 1
I_RES_CAB = I_SN_FIN + 2
I_RES_INI = I_RES_CAB + 1                    # 4 estados
I_RES_FIN = I_RES_INI + len(ESTADOS_FICHA) - 1
I_TOT = I_RES_FIN + 1
I_PCT = I_TOT + 1
I_NOTA = I_PCT + 2

COLS_INDICE = [
    ('A', 'Código', 12),
    ('B', 'Plato', 40),
    ('C', 'Partida que lo produce', 22),
    ('D', 'Familia', 16),
    ('E', 'Versión', 11),
    ('F', 'Fecha de revisión', 15),
    ('G', 'Revisada por', 20),
    ('H', '¿Ficha cerrada?', 14),
    ('I', 'Antigüedad de la ficha (días)', 15),
    ('J', 'Estado', 22),
]


def hoja_indice(wb):
    ws = wb.create_sheet(H_INDICE)
    anchos(ws, dict((c, a) for c, _t, a in COLS_INDICE))
    encabezar(ws, 'Índice de fichas técnicas',
              nota='Este índice se escribe A MANO, una línea por plato de tu '
                   'carta. Es lo único que te dice cuántos platos vendes sin '
                   'ficha.')

    motor.val(ws, 'A%d' % I_CTRL, 'Fecha de control', bold=True)
    motor.val(ws, 'C%d' % I_CTRL, FECHA_CONTROL, fmt=FMT_FECHA)
    motor.verde(ws, 'C%d' % I_CTRL)
    motor.val(ws, 'D%d' % I_CTRL,
              'Cámbiala para ver cómo envejecen tus fichas.', wrap=True)
    ws['D%d' % I_CTRL].font = Font(italic=True, size=9)
    motor.val(ws, 'A%d' % I_AVISO, 'Avisar si la ficha supera (días)',
              bold=True, wrap=True)
    motor.val(ws, 'C%d' % I_AVISO, '', fmt=FMT_ENT)
    motor.verde(ws, 'C%d' % I_AVISO)
    ws.merge_cells('D%d:G%d' % (I_AVISO, I_AVISO))
    motor.val(ws, 'D%d' % I_AVISO,
              'Vacía a propósito: el plazo de revisión lo pones tú. Mientras '
              'esté vacía no se enciende ningún aviso de antigüedad, y una '
              'ficha cerrada seguirá leyéndose como cerrada.', wrap=True)
    ws['D%d' % I_AVISO].font = Font(italic=True, size=9)
    ws.row_dimensions[I_AVISO].height = 26

    cabecera(ws, I_CAB, [(c, t) for c, t, _a in COLS_INDICE], altura=44)

    seed = dict((m['id'], m) for m in D.MIX_VENTA)
    orden = [m['id'] for m in D.MIX_VENTA]
    # B9(a) de la refutación xlsx (2026-09-06): los platos de la carta de
    # temporada que YA tienen la ficha cerrada («Calendario de Temporada»,
    # columna «Ficha técnica cerrada» = «Sí») entran también en este índice,
    # con su versión y su fecha. Si no, el flujo «documentar la ficha -> entra
    # en el índice» no queda demostrado de punta a punta (N1 y N2 del libro 5;
    # N3, N4 y N5 siguen sin ficha cerrada y no entran).
    nuevos_con_ficha = [c for c in D.CALENDARIO_TEMPORADA if c[9] == 'Sí']
    familia_de_partida = {D.ESTACIONES[D.IDX_FRIOS]: 'Entrantes',
                          D.ESTACIONES[D.IDX_PASE]: 'Principales',
                          D.ESTACIONES[D.IDX_POSTRES]: 'Postres'}
    orden_todos = orden + [c[0] for c in nuevos_con_ficha]
    v_cerrada, v_fecha = [], []
    for i in range(N_INDICE):
        r = I_INI + i
        idp = orden_todos[i] if i < len(orden_todos) else None
        m = seed.get(idp) if idp else None
        nuevo = None
        if m is None and idp:
            nuevo = next(c for c in nuevos_con_ficha if c[0] == idp)
        if m:
            motor.val(ws, 'A%d' % r, m['id'])
            motor.val(ws, 'B%d' % r, m['plato'], wrap=True)
            motor.val(ws, 'C%d' % r, m['partida'], wrap=True)
            motor.val(ws, 'D%d' % r, m['familia'])
        elif nuevo:
            _idn, plato, partida = nuevo[0], nuevo[1], nuevo[2]
            motor.val(ws, 'A%d' % r, _idn)
            motor.val(ws, 'B%d' % r, plato, wrap=True)
            motor.val(ws, 'C%d' % r, partida, wrap=True)
            motor.val(ws, 'D%d' % r, familia_de_partida.get(partida, ''))
        else:
            motor.val(ws, 'A%d' % r, '')
            motor.val(ws, 'B%d' % r, '', wrap=True)
            motor.val(ws, 'C%d' % r, '', wrap=True)
            motor.val(ws, 'D%d' % r, '')
        es_p1 = bool(m) and m['id'] == F['id_plato']
        motor.val(ws, 'E%d' % r, F['version'] if es_p1 else
                  ('1.0' if nuevo else ''))
        # el 5. de los cinco hitos del calendario (nuevo[5]) es «documentar la
        # ficha (fecha)»: la fecha de revisión de una ficha recién cerrada.
        if es_p1:
            fecha_rev = D._fecha(F['fecha_revision'])
        elif nuevo:
            fecha_rev = D._fecha(nuevo[5])
        else:
            fecha_rev = ''
        motor.val(ws, 'F%d' % r, fecha_rev, fmt=FMT_FECHA)
        motor.val(ws, 'G%d' % r, F['revisada_por'] if es_p1 else
                  ('P02 (jefe de cocina)' if nuevo else ''), wrap=True)
        motor.val(ws, 'H%d' % r, SI_NO[0] if (es_p1 or nuevo) else '')
        motor.verde(ws, 'A%d:H%d' % (r, r))
        motor.f(ws, 'I%d' % r,
                '=IFERROR(IF(OR($F{r}="",$C${c}=""),"",$C${c}-$F{r}),"")'
                .format(r=r, c=I_CTRL), fmt=FMT_ENT)
        motor.f(ws, 'J%d' % r,
                '=IF($B{r}="","",IF($H{r}="",$A${sf},'
                'IF($H{r}=$A${no},$A${pc},'
                'IF(OR($I{r}="",$C${av}=""),$A${ce},'
                'IF($I{r}>$C${av},$A${tr},$A${ce})))))'
                .format(r=r, sf=I_LEY_INI + 3, no=I_SN_INI + 1,
                        pc=I_LEY_INI + 1, ce=I_LEY_INI,
                        tr=I_LEY_INI + 2, av=I_AVISO))
        ws.row_dimensions[r].height = 26
        v_cerrada.append('H%d' % r)
        v_fecha.append('F%d' % r)

    # --- leyendas (origen de las listas y de los COUNTIF) ----------------
    cabecera(ws, I_LEY_CAB, [('A', 'Estado de la ficha'),
                             ('B', 'Qué quiere decir')], altura=20)
    glosas = (
        'La ficha existe, está escrita y alguien que no la escribió ya ha '
        'ejecutado el plato con ella delante.',
        'La ficha existe pero todavía no la ha validado nadie ejecutándola.',
        'La ficha está cerrada, pero lleva más días de los que has puesto '
        'arriba sin revisarse.',
        'El plato está en la carta y no tiene ficha. Es la fila que cuesta '
        'dinero.')
    for i, estado in enumerate(ESTADOS_FICHA):
        r = I_LEY_INI + i
        motor.val(ws, 'A%d' % r, estado, bold=True)
        ws.merge_cells('B%d:G%d' % (r, r))
        motor.val(ws, 'B%d' % r, glosas[i], wrap=True)
        ws.row_dimensions[r].height = 26

    cabecera(ws, I_SN_CAB, [('A', '¿Ficha cerrada?'),
                            ('B', 'Cuándo se marca')], altura=20)
    for i, texto in enumerate(SI_NO):
        r = I_SN_INI + i
        motor.val(ws, 'A%d' % r, texto, bold=True)
        ws.merge_cells('B%d:G%d' % (r, r))
        motor.val(ws, 'B%d' % r,
                  ('Ya la ha ejecutado alguien que no la escribió y salió '
                   'igual.' if i == 0 else
                   'Está escrita pero sin validar. Déjala en blanco si ni '
                   'siquiera está escrita.'), wrap=True)
        ws.row_dimensions[r].height = 26
    dv_rango(ws, v_cerrada,
             "'%s'!$A$%d:$A$%d" % (H_INDICE, I_SN_INI, I_SN_FIN),
             'Sí o No', 'Marca Sí sólo si la ficha ya se ha validado '
                        'ejecutándola. Déjala vacía si no hay ficha.')

    # --- resumen ---------------------------------------------------------
    cabecera(ws, I_RES_CAB, [('A', 'Resumen del índice'), ('C', 'Platos')],
             altura=20)
    ws.merge_cells('A%d:B%d' % (I_RES_CAB, I_RES_CAB))
    pintar_cabecera(ws, 'A%d:B%d' % (I_RES_CAB, I_RES_CAB))
    for i, estado in enumerate(ESTADOS_FICHA):
        r = I_RES_INI + i
        ws.merge_cells('A%d:B%d' % (r, r))
        motor.val(ws, 'A%d' % r, 'Platos en estado «' + estado + '»')
        motor.f(ws, 'C%d' % r,
                '=IFERROR(COUNTIF($J${a}:$J${b},$A${l}),"")'
                .format(a=I_INI, b=I_FIN, l=I_LEY_INI + i), fmt=FMT_ENT)
        ws['C%d' % r].fill = PatternFill('solid', fgColor=GRIS)
    ws.merge_cells('A%d:B%d' % (I_TOT, I_TOT))
    motor.val(ws, 'A%d' % I_TOT, 'Platos registrados en el índice', bold=True)
    motor.f(ws, 'C%d' % I_TOT,
            '=IF(COUNT($C${a}:$C${b})=0,"",SUM($C${a}:$C${b}))'
            .format(a=I_RES_INI, b=I_RES_FIN), fmt=FMT_ENT, bold=True)
    ws['C%d' % I_TOT].fill = PatternFill('solid', fgColor=CREMA)
    ws.merge_cells('A%d:B%d' % (I_PCT, I_PCT))
    motor.val(ws, 'A%d' % I_PCT, 'Platos de la carta con la ficha cerrada (%)',
              bold=True)
    motor.f(ws, 'C%d' % I_PCT,
            '=IFERROR(IF(OR($C${t}="",$C${t}=0),"",$C${c}/$C${t}),"")'
            .format(t=I_TOT, c=I_RES_INI), fmt=FMT_PCT, bold=True)
    ws['C%d' % I_PCT].fill = PatternFill('solid', fgColor=CREMA)

    ws.merge_cells('A%d:J%d' % (I_NOTA, I_NOTA))
    motor.val(ws, 'A%d' % I_NOTA,
              'El porcentaje se calcula sobre los platos REGISTRADOS en el '
              'índice, no sobre los que tienen algo escrito en la columna de '
              'ficha cerrada: una fila en blanco cuenta como «Sin ficha», que '
              'es exactamente lo que es. En el ejemplo hay 12 platos de la '
              'carta y una sola ficha cerrada, y ése es el número con el que '
              'se empieza a trabajar.', wrap=True)
    ws['A%d' % I_NOTA].font = Font(italic=True, size=9)
    ws.row_dimensions[I_NOTA].height = 44

    ws.merge_cells('A%d:J%d' % (I_NOTA + 2, I_NOTA + 2))
    motor.val(ws, 'A%d' % (I_NOTA + 2),
              'Por qué es manual: para rellenarse solo, la hoja tendría que '
              'leer el nombre de cada pestaña con INDIRECT, que Google Sheets '
              'y los visores del móvil no resuelven igual. Antes un índice que '
              'se escribe a mano y siempre dice la verdad que uno que a veces '
              'funciona.', wrap=True)
    ws['A%d' % (I_NOTA + 2)].font = Font(italic=True, size=9)
    ws.row_dimensions[I_NOTA + 2].height = 40

    motor.val(ws, 'A%d' % (I_NOTA + 4), D.VERSION_LINE)
    ws['A%d' % (I_NOTA + 4)].font = Font(size=8, italic=True)

    motor.dv_fecha(ws, v_fecha + ['C%d' % I_CTRL])
    motor.dv_numerica(ws, ['C%d' % I_AVISO], minimo=0, maximo=3650,
                      titulo='Días',
                      mensaje='Escribe cada cuántos días quieres revisar una '
                              'ficha cerrada. Déjala vacía si no quieres aviso.')
    motor.semaforo_texto(
        ws, 'J%d:J%d' % (I_INI, I_FIN),
        ((ESTADOS_FICHA[0], motor.CF_VERDE_BG, motor.CF_VERDE_FG),
         (ESTADOS_FICHA[1], motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
         (ESTADOS_FICHA[2], motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
         (ESTADOS_FICHA[3], motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    ws.freeze_panes = 'B10'
    pagina(ws, apaisado=True, titulos='$%d:$%d' % (I_CAB, I_CAB))
    return ws


# --------------------------------------------------------------------------
def mapa():
    """Contrato del guion: celdas clave con `hoja!celda` y descripción."""
    celdas_ej = {
        'Código del plato de la ficha de ejemplo': 'B%d' % R_COD,
        'Nombre del plato de la ficha de ejemplo': 'B%d' % R_NOM,
        'Partida que produce el plato de ejemplo': 'B%d' % R_PAR,
        'Versión de la ficha de ejemplo': 'B%d' % R_VER,
        'Fecha de revisión de la ficha de ejemplo': 'B%d' % R_FEC,
        'Coste por ración copiado del escandallo': 'B%d' % R_COSTE,
        'Raciones vendidas al mes del plato de ejemplo': 'B%d' % R_UDS,
        'Coste de materia prima al mes del plato de ejemplo':
            'B%d' % R_COSTE_MES,
        'Mise en place de la ficha de ejemplo (min)': 'B%d' % R_MEP,
        'Tiempo de pase de la ficha de ejemplo (min)': 'B%d' % R_PASE,
        'Tiempo total de la elaboración de ejemplo (min)': 'B%d' % R_TIEMPO,
        'Temperatura mínima de mantenimiento en caliente (°C)': 'B%d' % R_TMIN,
        'Punto de cocción de la ficha de ejemplo': 'B%d' % R_PUNTO,
        'Alérgenos presentes como ingrediente en la ficha de ejemplo':
            'B%d' % R_CNT_INI,
        'Alérgenos por traza en la ficha de ejemplo': 'B%d' % (R_CNT_INI + 1),
        'Alérgenos por utensilio compartido en la ficha de ejemplo':
            'B%d' % (R_CNT_INI + 2),
        'Fecha de elaboración del lote de ejemplo': 'B%d' % R_LOTE,
    }
    for i in range(len(F['conservacion'])):
        r = R_CON_INI + i
        celdas_ej['Consumo preferente de «%s»' % F['conservacion'][i][0]] = \
            'E%d' % r
    # La fila del plato de la ficha de ejemplo NO es la primera del índice: el
    # índice se siembra en el orden del mix de venta y P1 es el quinto.
    fila_p1 = I_INI + [m['id'] for m in D.MIX_VENTA].index(F['id_plato'])
    celdas_idx = {
        'Fecha de control del índice': 'C%d' % I_CTRL,
        'Aviso de antigüedad de ficha (días)': 'C%d' % I_AVISO,
        'Antigüedad de la ficha del plato de ejemplo': 'I%d' % fila_p1,
        'Estado de la ficha del plato de ejemplo': 'J%d' % fila_p1,
        'Platos con la ficha cerrada': 'C%d' % I_RES_INI,
        'Platos con ficha pendiente de cerrar': 'C%d' % (I_RES_INI + 1),
        'Platos con ficha que toca revisar': 'C%d' % (I_RES_INI + 2),
        'Platos sin ficha': 'C%d' % (I_RES_INI + 3),
        'Platos registrados en el índice': 'C%d' % I_TOT,
        'Platos de la carta con la ficha cerrada (%)': 'C%d' % I_PCT,
    }
    for i, m in enumerate(D.MIX_VENTA):
        celdas_idx['Estado de la ficha de «%s»' % m['plato']] = \
            'J%d' % (I_INI + i)
    return {
        'fichero': NOMBRE + '.xlsx',
        'producto': 'manual-chef-ejecutivo',
        'libro': 3,
        'nota': ('«Ficha (plantilla)» tiene la MISMA estructura de filas que '
                 '«Ficha (ejemplo)», con todas las celdas verdes vacías: '
                 'cualquier celda de esta lista existe también allí, en blanco.'),
        # A4 de la refutación xlsx (2026-09-06): vacía a propósito, lo dice
        # la propia nota de «Índice de Fichas»!D6 - el plazo de revisión lo
        # pone el comprador.
        'vacias_a_proposito': ['Índice de Fichas!C6'],
        'hojas': {
            H_EJEMPLO: {
                'celdas': celdas_ej,
                'tablas': [
                    {'titulo': 'Pasos de elaboración de la ficha de ejemplo',
                     'cols': [['Nº', 'A', 'num'], ['Operación', 'B', 'txt'],
                              ['Punto de control', 'F', 'txt']],
                     'filas': [R_PASOS_INI, R_PASOS_INI
                               + len(F['pasos']) - 1]},
                    {'titulo': 'Alérgenos de proceso de la ficha de ejemplo',
                     'cols': [['Alérgeno', 'A', 'txt'],
                              ['Estado en esta elaboración', 'B', 'txt'],
                              ['Dónde entra en ESTA elaboración', 'C', 'txt'],
                              ['Sustitución posible', 'E', 'txt']],
                     'filas': [R_ALE_INI, R_ALE_INI
                               + len(F['alergenos_proceso']) - 1]},
                    {'titulo': 'Conservación y vida útil de la ficha de ejemplo',
                     'cols': [['Elaboración', 'A', 'txt'],
                              ['Conservación', 'B', 'txt'],
                              ['Vida útil (días)', 'D', 'num'],
                              ['Consumo preferente', 'E', 'txt']],
                     'filas': [R_CON_INI, R_CON_INI
                               + len(F['conservacion']) - 1]},
                    {'titulo': 'Estados de la tabla de alérgenos de proceso',
                     'cols': [['Estado', 'A', 'txt'],
                              ['Qué quiere decir', 'B', 'txt']],
                     'filas': [R_LEY_INI, R_LEY_FIN]},
                ],
            },
            H_PLANTILLA: {'celdas': {}, 'tablas': []},
            H_INDICE: {
                'celdas': celdas_idx,
                'tablas': [
                    {'titulo': 'Índice de fichas técnicas de la carta',
                     'cols': [['Código', 'A', 'txt'], ['Plato', 'B', 'txt'],
                              ['Partida que lo produce', 'C', 'txt'],
                              ['Familia', 'D', 'txt'],
                              ['Versión', 'E', 'txt'],
                              ['¿Ficha cerrada?', 'H', 'txt'],
                              ['Estado', 'J', 'txt']],
                     'filas': [I_INI, I_INI + len(D.MIX_VENTA) - 1]},
                    {'titulo': 'Resumen del índice de fichas',
                     'cols': [['Resumen del índice', 'A', 'txt'],
                              ['Platos', 'C', 'num']],
                     'filas': [I_RES_INI, I_PCT]},
                ],
            },
        },
    }


def main():
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_ficha(wb, H_PLANTILLA, relleno=False)
    hoja_ficha(wb, H_EJEMPLO, relleno=True)
    hoja_indice(wb)

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
