#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_banquetes-comidas-testigo.py — libro 6 de «Manual del Chef Ejecutivo»
(SPEC §2.2 fila 6).

Hojas: Instrucciones · Registro de Comidas Testigo · Producción y Ficha de
Banquete.

QUÉ DECIDE ESTE LIBRO
---------------------
Si un encargo dispara la obligación legal de guardar comidas testigo, y cómo se
produce el evento. Las dos cosas van juntas a propósito: la obligación se decide
con el número de comensales que el chef ya tiene delante cuando planifica la
producción, no en otro sitio y otro día.

DECISIONES TÉCNICAS
-------------------
* Los cinco parámetros legales (más de 40 comensales, 100 gramos, 7 días, 4 °C
  y -18 °C) son celdas verdes con su nota «Verificado el 06-09-2026 · norma ·
  URL» leída del JSON de research (id CE-11). Ninguna de esas cifras se teclea
  dentro de una fórmula.
* La obligación NO se decide solo por el número de comensales: el apartado 8
  del artículo 30 lista además los supuestos por tipo de servicio (residencias,
  hospitales, comedores escolares, comedores colectivos con menú común, medios
  de transporte y eventos cuando esa es la actividad principal). Van en una
  tabla con su casilla Sí/No y la alerta se enciende con CUALQUIERA de las dos
  vías. Decir «no llegas a 40, no te obliga» sería el error caro.
* La cuenta atrás de conservación se calcula con la fecha de recogida más los
  días del parámetro, y el estado sale de los días que faltan. Días naturales,
  nunca `NETWORKDAYS`.
* Este libro NO tiene hojas de desperdicio (SPEC D3 y D13): la jerarquía de la
  Ley 1/2025, el doggy bag y la exención de los 1.300 m2 son una tabla de una
  página del capítulo 16 del manual.
* Cero constantes dentro de una fórmula (salvo 0, 1 y los índices de
  INDEX/MATCH), `IFERROR(...,"")` en todo cociente, «sin dato» = `""` nunca 0,
  semáforos con `ISNUMBER`.
* Prohibidas `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA`,
  `RANK`, `NETWORKDAYS` y las referencias a otros ficheros: cero usos.
* Textos 100 % WinAnsi (cp1252): ni un carácter fuera.

Salida fija: build/banquetes-comidas-testigo.xlsx + su mapa de celdas.
"""
import datetime as dt
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
TITULO = 'Banquetes y comidas testigo'
NOMBRE = 'banquetes-comidas-testigo'

FMT_EUR = motor.FMT_EUR
FMT_PCT = motor.FMT_PCT
FMT_ENT = motor.FMT_ENT
FMT_FECHA = motor.FMT_FECHA
FMT_DEC = '#,##0.0'
FMT_DEC3 = '#,##0.000'

GRIS = 'F2F2F2'
CREMA = 'FFF6DC'
ORO = 'FFD700'
CABECERA = '2D2D2D'

FECHA_VERIF = '06-09-2026'
JSON_SECTOR = os.path.join(RAIZ, 'auditorias', 'guias-v2-research-sector.json')

CT = D.PARAMETROS_COMIDA_TESTIGO
EV = D.EVENTO_EJEMPLO


def sector(idd):
    """Entrada `CE-*`/`MM-*` del JSON de research consolidado."""
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


CE11 = verificado('CE-11')          # comidas testigo, art. 30.8, 30.9 y 30.10
CE10 = verificado('CE-10')          # temperaturas del art. 30
CE13 = verificado('CE-13')          # tres fechas al congelar

#: Fecha de referencia con la que se sirve el ejemplo: tres días después del
#: banquete, o sea DENTRO de la ventana de conservación, para que la cuenta
#: atrás se vea funcionando. Sale del propio juego de datos; borrando la celda
#: verde, el libro vuelve a `TODAY()`.
FECHA_EJEMPLO = D._fecha(EV['fecha']) + dt.timedelta(days=3)

SI_NO = ['Sí', 'No']
CONSERVACION = ['Refrigeración', 'Congelación']
MOMENTO_TOMA = ['Salida del obrador', 'En el servicio', 'Toma única']

# --- hoja «Registro de Comidas Testigo» ----------------------------------
R_UMBRAL, R_GRAMOS, R_DIAS = 7, 8, 9
R_TREF, R_TCON, R_SIM, R_HOY = 10, 11, 12, 13
R_EV_ID, R_EV_NOM, R_EV_FEC, R_EV_COM = 19, 20, 21, 22
R_EV_HORA, R_EV_RESP, R_EV_UBI, R_EV_ALERTA = 23, 24, 25, 26
#: B3 de la refutación xlsx (2026-09-06): art. 30.9 - catering en dos
#: establecimientos distintos exige DOS tomas, no una.
R_EV_DIST = 27
R_SUP_CAB = 29
R_SUP_INI = 30
R_SUP_FIN = R_SUP_INI + len(CT['supuestos_obligados']) - 1        # 34
R_SUP_TOT = R_SUP_FIN + 1                                        # 35
R_CAB = 38
R_INI = 39
R_FIN = R_INI + 12 - 1                                           # 50
R_RES = R_FIN + 2                                                # 52
R_RCAB = R_RES + 1                                               # 53
R_R1 = R_RCAB + 1                                                # 54 .. 59
#: Bloque de listas de los desplegables (A1 de la refutación xlsx): al final
#: de la hoja, fuera de la zona que se lee de un vistazo.
R_LSEC = 66
R_SN_CAB = 67
R_SN_INI = 68
R_SN_FIN = R_SN_INI + len(SI_NO) - 1                             # 69
R_CONS_CAB = 71
R_CONS_INI = 72
R_CONS_FIN = R_CONS_INI + len(CONSERVACION) - 1                  # 73
R_MOM_CAB = 75
R_MOM_INI = 76
R_MOM_FIN = R_MOM_INI + len(MOMENTO_TOMA) - 1                    # 78

# --- hoja «Producción y Ficha de Banquete» -------------------------------
B_EV_ID, B_EV_FEC, B_EV_COM, B_EV_ALERTA = 6, 7, 8, 9
B_MCAB = 12
B_MINI = 13
B_MFIN = B_MINI + 12 - 1                                         # 24
B_MTOT = B_MFIN + 1                                              # 25
B_PCAB = 28
B_PINI = 29
B_PFIN = B_PINI + len(D.PARTIDAS_PRODUCCION) - 1                 # 32
B_PTOT = B_PFIN + 1                                              # 33
B_TCAB = 36
B_TINI = 37
B_TFIN = B_TINI + 15 - 1                                         # 51
B_HCAB = 54
B_HINI = 55
B_HFIN = B_HINI + 9 - 1                                          # 63
B_HTOT = B_HFIN + 1                                              # 64
B_HCOM = B_HTOT + 1                                              # 65
#: Bloque de listas del desplegable de partida (A1 de la refutación xlsx):
#: celdas VERDES con nota «cópialas del libro 1» (copia declarada, D4).
B_LSEC = 72
B_PART_CAB = 73
B_PART_INI = 74
B_PART_FIN = B_PART_INI + len(D.ESTACIONES) - 1                  # 79

REF_SI_NO = "'Registro de Comidas Testigo'!$A$%d:$A$%d" % (R_SN_INI, R_SN_FIN)
REF_CONSERVACION = ("'Registro de Comidas Testigo'!$A$%d:$A$%d"
                    % (R_CONS_INI, R_CONS_FIN))
REF_MOMENTO_TOMA = ("'Registro de Comidas Testigo'!$A$%d:$A$%d"
                   % (R_MOM_INI, R_MOM_FIN))
REF_PARTIDAS_BANQUETE = ("'Producción y Ficha de Banquete'!$A$%d:$A$%d"
                        % (B_PART_INI, B_PART_FIN))

ALERTA_SI = 'COMIDA TESTIGO OBLIGATORIA'
ALERTA_NO = ('Por número de comensales no es obligatoria: revisa igualmente '
             'los supuestos de la tabla de abajo')
EST_CONS = 'En conservación: NO destruir'
EST_ULT = 'Último día de conservación'
EST_FIN = 'Ya se puede destruir'
GR_OK = 'Sí'
GR_MAL = 'NO: por debajo del mínimo'
TP_OK = 'Sí'
TP_MAL = 'NO: por encima del máximo'

REG = "'Registro de Comidas Testigo'"
PROD = "'Producción y Ficha de Banquete'"

NOMBRES = dict((p[0], p[1]) for p in D.PLANTILLA)


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


def pintar_cabecera(ws, fila, letras):
    for letra in letras:
        ws[letra + str(fila)].fill = PatternFill('solid', fgColor=CABECERA)


def seccion(ws, coord, texto):
    motor.val(ws, coord, texto, bold=True)
    ws[coord].font = Font(bold=True, size=12)


def fila_total(ws, fila, primera, ultima):
    for col in range(motor.column_index_from_string(primera),
                     motor.column_index_from_string(ultima) + 1):
        c = ws.cell(row=fila, column=col)
        c.fill = PatternFill('solid', fgColor=CREMA)
        c.font = Font(bold=True)


def pagina(ws, apaisado=True, titulos=None):
    ws.page_setup.paperSize = 9
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


def etiqueta(ws, fila, texto, hasta='C', bold=False):
    """Etiqueta de fila en A, combinada hasta `hasta` para que quepa."""
    motor.val(ws, 'A%d' % fila, texto, bold=bold)
    ws.merge_cells('A%d:%s%d' % (fila, hasta, fila))


def dv_rango(ws, coords, ref, titulo, mensaje):
    """Desplegable contra un RANGO (convención de familia: nunca lista con
    comas, que se rompe en cuanto una opción lleva una coma y tiene tope de
    255 caracteres). A1 de la refutación xlsx del 2026-09-06."""
    dv = DataValidation(type='list', formula1=ref, allow_blank=True,
                        showErrorMessage=True, errorTitle=titulo,
                        error=mensaje)
    ws.add_data_validation(dv)
    for c in coords:
        dv.add(c)
    return dv


# --------------------------------------------------------------------------
PASOS = [
    '1. Hoja «Registro de Comidas Testigo», bloque de arriba: los cinco '
    'parámetros legales vienen puestos (más de 40 comensales, 100 gramos, 7 '
    'días, 4 °C en refrigeración y -18 °C en congelación) con la norma y el '
    'enlace al lado. Son celdas verdes por si tu comunidad autónoma te exige '
    'más, nunca menos.',
    '2. Bloque «El evento»: escribe el id, la fecha, los comensales, la hora '
    'de servicio, quién toma las muestras y dónde se guardan. La casilla '
    '«Obligación de comida testigo» se enciende sola.',
    '3. Bloque «Supuestos»: la obligación NO va solo por el número de '
    'comensales. Marca Sí en los supuestos que se te apliquen (residencias, '
    'hospitales, comedores escolares, comedores colectivos con menú común, '
    'medios de transporte y eventos cuando esa sea tu actividad principal). '
    'Con uno solo marcado, la alerta ya se enciende.',
    '4. Tabla «Muestras tomadas»: una fila por elaboración servida, con su '
    'lote, la fecha y la hora de recogida, los gramos, dónde se guarda y a qué '
    'temperatura. El libro calcula la fecha de destrucción, los días que '
    'faltan, si los gramos llegan al mínimo y si la temperatura es la que '
    'toca.',
    '5. La columna «Estado» es la cuenta atrás: mientras queden días dice NO '
    'DESTRUIR; el último día lo avisa; después dice que ya se puede tirar. '
    'Son días naturales, no laborables.',
    '6. La celda verde «Fecha para simular» sirve para ver la cuenta atrás en '
    'cualquier día. En el ejemplo trae la fecha del banquete más tres días; '
    'bórrala y el libro usará la de hoy.',
    '7. Hoja «Producción y Ficha de Banquete»: el evento se lee solo de la '
    'hoja anterior. Escribe el menú, cuántas raciones sirve cada plato POR '
    'COMENSAL y cuántas raciones salen de cada unidad de producción (una olla, '
    'una placa, una bandeja).',
    '8. Las raciones a producir y las unidades de producción se calculan '
    'solas. Si el comercial cambia los comensales de 120 a 140, cambia UNA '
    'celda y toda la producción se recalcula: eso es lo que evita el pedido a '
    'ojo la víspera.',
    '9. El bloque «Producción por partida» reparte esas raciones entre las '
    'partidas de tu cocina, que es como se manda el trabajo. Debajo tienes el '
    'timing hora a hora y el personal asignado, con las horas totales y las '
    'horas por comensal.',
    '10. Cadencia: SÓLO SI HACES EVENTOS. No es una hoja de uso diario ni '
    'semanal: se abre cada vez que aceptas un encargo de más de 40 personas '
    'o de uno de los supuestos del art. 30.8.',
]

NOTAS_LIBRO = [
    'LA OBLIGACIÓN DE GUARDAR COMIDAS TESTIGO ES LA GRAN DESCONOCIDA. No es '
    'una recomendación de buenas prácticas: está en el artículo 30 del Real '
    'Decreto 1086/2020, y cualquier encargo para un grupo de más de 40 '
    'personas la dispara, lo haga un restaurante, un catering o un hotel. '
    + CE11,
    'Qué hay que guardar: una ración de cada elaboración servida, de 100 '
    'gramos como mínimo, identificada y fechada, durante al menos siete días, '
    'en refrigeración a 4 °C o congelada a -18 °C. Si hay un brote, esa muestra '
    'es lo único que puede demostrar que el plato salió bien de tu cocina.',
    'Los supuestos por tipo de servicio son independientes del número de '
    'comensales: residencias, hospitales y comedores escolares, comedores '
    'colectivos con menú común, medios de transporte, y los eventos cuando esa '
    'sea la actividad principal del establecimiento. Un comedor de empresa con '
    'menú común obliga aunque sirva a treinta personas.',
    'Al congelar una elaboración propia hay que poner TRES fechas: la de '
    'elaboración, la de congelación y la de caducidad o consumo preferente del '
    'producto ya congelado. ' + CE13,
    'Este libro NO lleva hojas de desperdicio. Qué se hace con el excedente de '
    'un banquete (la jerarquía de prioridades, la donación y el envase para '
    'que el cliente se lleve lo que no se ha comido) está resuelto en una '
    'página del capítulo 16 del manual, y en profundidad en el «Manual del '
    'Manager de Restaurante».',
    'Las raciones se calculan POR COMENSAL, no en absoluto. Es la única forma '
    'de que el libro sirva cuando el número de comensales cambia la víspera, '
    'que es lo que pasa siempre.',
]


def hoja_instrucciones(wb):
    ws = wb.create_sheet('Instrucciones', 0)
    anchos(ws, {'A': 110.0})
    motor.val(ws, 'A1', TITULO)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', SUBTITULO)
    motor.val(ws, 'A3', 'Para qué sirve: saber si este encargo te obliga a '
                        'guardar comidas testigo, y producir el evento sin '
                        'calcular nada a ojo.')
    ws['A3'].font = Font(italic=True, size=9)

    seccion(ws, 'A5', 'Instrucciones de uso')
    fila = 6
    for paso in PASOS:
        nota(ws, fila, paso, alto=48, wrap=True)
        fila += 1
    fila += 1
    motor.val(ws, 'A' + str(fila), motor.NOTA_VERDES)
    ws['A' + str(fila)].fill = PatternFill('solid', fgColor=motor.VERDE)
    fila += 2
    seccion(ws, 'A' + str(fila), 'Lo que conviene saber antes de empezar')
    fila += 1
    for texto in NOTAS_LIBRO:
        nota(ws, fila, texto, alto=62, wrap=True)
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
COLS_MUESTRAS = [
    ('A', 'Id de muestra', 'txt'),
    ('B', 'Id del plato', 'txt'),
    ('C', 'Elaboración', 'txt'),
    ('D', 'Lote', 'txt'),
    ('E', 'Fecha de recogida', 'fecha'),
    ('F', 'Hora', 'txt'),
    ('G', 'Gramos', 'ent'),
    ('H', 'Ubicación', 'txt'),
    ('I', 'Temperatura (°C)', 'ent'),
    ('J', 'Conservación', 'txt'),
    ('K', 'Fecha de destrucción prevista', 'fecha'),
    ('L', 'Días que faltan', 'ent'),
    ('M', 'Estado', 'txt'),
    ('N', 'Gramos suficientes', 'txt'),
    ('O', 'Temperatura conforme', 'txt'),
    ('P', 'Responsable', 'txt'),
    ('Q', 'Momento de la toma (art. 30.9)', 'txt'),
    ('R', 'Aviso', 'txt'),
]

PARAMETROS_LEGALES = [
    (R_UMBRAL, 'Comensales a partir de los que obliga (más de)',
     float(CT['umbral_comensales']), FMT_ENT, CE11),
    (R_GRAMOS, 'Gramos mínimos por elaboración guardada',
     float(CT['gramos_minimos']), FMT_ENT, CE11),
    (R_DIAS, 'Días de conservación de la muestra (mínimo)',
     float(CT['dias_conservacion']), FMT_ENT, CE11),
    (R_TREF, 'Temperatura máxima en refrigeración (°C)',
     float(CT['temp_refrigeracion_c']), FMT_ENT, CE11),
    (R_TCON, 'Temperatura máxima en congelación (°C)',
     float(CT['temp_congelacion_c']), FMT_ENT, CE11),
]


def hoja_registro(wb):
    ws = wb.create_sheet('Registro de Comidas Testigo')
    encabezar(ws, 'Registro de comidas testigo',
              nota='Si el encargo obliga, se decide arriba. Lo que hay que '
                   'guardar, cuánto y hasta cuándo, se calcula abajo.')
    anchos(ws, {'A': 18, 'B': 12, 'C': 46, 'D': 18, 'E': 16, 'F': 9,
                'G': 10, 'H': 30, 'I': 15, 'J': 16, 'K': 18, 'L': 14,
                'M': 30, 'N': 20, 'O': 22, 'P': 14, 'Q': 22, 'R': 46})

    # --- parámetros legales ---------------------------------------------
    seccion(ws, 'A5',
            'PARÁMETROS LEGALES DE LAS COMIDAS TESTIGO (celdas verdes)')
    cabecera(ws, 6, [('A', 'Parámetro'), ('D', 'Valor'),
                     ('E', 'Base legal, verificada el ' + FECHA_VERIF)],
             altura=32)
    pintar_cabecera(ws, 6, 'BC')
    ws.merge_cells('A6:C6')
    ws.merge_cells('E6:O6')
    for fila, texto, valor, fmt, base in PARAMETROS_LEGALES:
        etiqueta(ws, fila, texto)
        motor.val(ws, 'D%d' % fila, valor, fmt=fmt, verde_=True)
        motor.val(ws, 'E%d' % fila, base, wrap=True)
        ws.merge_cells('E%d:O%d' % (fila, fila))
        ws.row_dimensions[fila].height = 30
    motor.dv_numerica(ws, ['D%d' % R_UMBRAL, 'D%d' % R_GRAMOS,
                           'D%d' % R_DIAS], minimo=1,
                      titulo='Valor del parámetro')
    motor.dv_numerica(ws, ['D%d' % R_TREF, 'D%d' % R_TCON], minimo=-40,
                      maximo=20, titulo='Temperatura (°C)',
                      mensaje='Escribe la temperatura en grados centígrados, '
                              'entre -40 y 20.')

    etiqueta(ws, R_SIM, 'Fecha para simular (déjala vacía y se usa la de hoy)')
    motor.val(ws, 'D%d' % R_SIM, FECHA_EJEMPLO, fmt=FMT_FECHA, verde_=True)
    motor.dv_fecha(ws, ['D%d' % R_SIM])
    motor.val(ws, 'E%d' % R_SIM,
              'En el ejemplo trae la fecha del banquete más tres días, para '
              'que se vea la cuenta atrás. Bórrala y el libro usará la de hoy.')
    etiqueta(ws, R_HOY, 'Hoy (fecha de referencia de la cuenta atrás)',
             bold=True)
    motor.f(ws, 'D%d' % R_HOY,
            '=IFERROR(IF($D${s}="",TODAY(),$D${s}),"")'.format(s=R_SIM),
            fmt=FMT_FECHA, bold=True)
    gris(ws, 'D%d' % R_HOY)

    # --- el evento --------------------------------------------------------
    seccion(ws, 'A17', 'EL EVENTO')
    cabecera(ws, 18, [('A', 'Campo'), ('D', 'Valor')], altura=20)
    pintar_cabecera(ws, 18, 'BC')
    ws.merge_cells('A18:C18')
    campos = [
        (R_EV_ID, 'Id del evento', EV['id'], None),
        (R_EV_NOM, 'Nombre del evento', EV['nombre'], None),
        (R_EV_FEC, 'Fecha del evento', D._fecha(EV['fecha']), FMT_FECHA),
        (R_EV_COM, 'Comensales', float(EV['comensales']), FMT_ENT),
        (R_EV_HORA, 'Hora de servicio', EV['hora_servicio'], None),
        (R_EV_RESP, 'Responsable de tomar las muestras', EV['responsable'],
         None),
        (R_EV_UBI, 'Dónde se guardan las muestras', EV['ubicacion_muestras'],
         None),
        (R_EV_DIST, '¿Elaboración y servicio en establecimientos distintos?',
         EV['elaboracion_servicio_distintos'], None),
    ]
    for fila, texto, valor, fmt in campos:
        etiqueta(ws, fila, texto)
        motor.val(ws, 'D%d' % fila, valor, fmt=fmt, verde_=True)
        if fila in (R_EV_UBI, R_EV_NOM):
            ws.merge_cells('D%d:H%d' % (fila, fila))
    motor.dv_numerica(ws, ['D%d' % R_EV_COM], minimo=1, maximo=100000,
                      titulo='Comensales')
    motor.dv_fecha(ws, ['D%d' % R_EV_FEC])
    motor.val(ws, 'E%d' % R_EV_DIST,
              'Si es «Sí» (catering: se elabora en un obrador y se sirve en '
              'otro sitio), el art. 30.9 exige DOS tomas por elaboración: una '
              'a la salida del obrador y otra en el servicio. ' + CE11,
              wrap=True)
    ws.merge_cells('E%d:O%d' % (R_EV_DIST, R_EV_DIST))
    ws.row_dimensions[R_EV_DIST].height = 30

    etiqueta(ws, R_EV_ALERTA, 'OBLIGACIÓN DE COMIDA TESTIGO', bold=True)
    motor.f(ws, 'D%d' % R_EV_ALERTA,
            '=IF(OR(AND(ISNUMBER($D${c}),ISNUMBER($D${u}),$D${c}>$D${u}),'
            'AND(ISNUMBER($D${s}),$D${s}>0)),"{si}","{no}")'
            .format(c=R_EV_COM, u=R_UMBRAL, s=R_SUP_TOT, si=ALERTA_SI,
                    no=ALERTA_NO), bold=True)
    ws.merge_cells('D%d:O%d' % (R_EV_ALERTA, R_EV_ALERTA))
    ws.row_dimensions[R_EV_ALERTA].height = 26
    motor.semaforo_texto(ws, 'D%d' % R_EV_ALERTA,
                         ((ALERTA_SI, motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          (ALERTA_NO, motor.CF_AMBAR_BG,
                           motor.CF_AMBAR_FG)))

    # --- supuestos del art. 30.8 -----------------------------------------
    seccion(ws, 'A28',
            'SUPUESTOS DEL ARTÍCULO 30.8 — obligan por TIPO DE SERVICIO, sin '
            'mirar el número de comensales')
    cabecera(ws, R_SUP_CAB, [('A', 'Supuesto'), ('D', '¿Te aplica?')],
             altura=20)
    pintar_cabecera(ws, R_SUP_CAB, 'BC')
    ws.merge_cells('A%d:C%d' % (R_SUP_CAB, R_SUP_CAB))
    for i, texto in enumerate(CT['supuestos_obligados']):
        fila = R_SUP_INI + i
        etiqueta(ws, fila, texto)
        # el ejemplo es un banquete de encargo para 120 personas: el supuesto
        # que le aplica es el último de la lista de la norma
        marca = 'Sí' if i == len(CT['supuestos_obligados']) - 1 else 'No'
        motor.val(ws, 'D%d' % fila, marca, verde_=True, align='center')
    dv_rango(ws, ['D%d' % r for r in range(R_SUP_INI, R_SUP_FIN + 1)]
             + ['D%d' % R_EV_DIST], REF_SI_NO, '¿Te aplica?',
             'Elige Sí o No de la lista del final de esta hoja.')
    motor.semaforo_texto(ws, 'D%d:D%d' % (R_SUP_INI, R_SUP_FIN),
                         (('Sí', motor.CF_ROJO_BG, motor.CF_ROJO_FG),))
    etiqueta(ws, R_SUP_TOT, 'Supuestos marcados', bold=True)
    motor.f(ws, 'D%d' % R_SUP_TOT,
            '=COUNTIF($D${a}:$D${b},"Sí")'.format(a=R_SUP_INI, b=R_SUP_FIN),
            fmt=FMT_ENT, bold=True, align='center')
    gris(ws, 'D%d' % R_SUP_TOT)
    motor.val(ws, 'E%d' % R_SUP_TOT, CE11, wrap=True)
    ws.merge_cells('E%d:O%d' % (R_SUP_TOT, R_SUP_TOT))
    ws.row_dimensions[R_SUP_TOT].height = 30

    # --- muestras ---------------------------------------------------------
    seccion(ws, 'A37', 'MUESTRAS TOMADAS')
    cabecera(ws, R_CAB, [(c, t) for c, t, _ in COLS_MUESTRAS], altura=52)
    for i, fila in enumerate(D.COMIDAS_TESTIGO):
        r = R_INI + i
        (idm, idp, plato, lote, recogida, gramos, ubi, temp, _destr,
         resp, momento) = fila
        fecha, hora = recogida.split(' ')
        motor.val(ws, 'A%d' % r, idm, verde_=True)
        motor.val(ws, 'B%d' % r, idp, verde_=True)
        motor.val(ws, 'C%d' % r, plato, verde_=True, wrap=True)
        motor.val(ws, 'D%d' % r, lote, verde_=True)
        motor.val(ws, 'E%d' % r, D._fecha(fecha), fmt=FMT_FECHA, verde_=True)
        motor.val(ws, 'F%d' % r, hora, verde_=True, align='center')
        motor.val(ws, 'G%d' % r, float(gramos), fmt=FMT_ENT, verde_=True)
        motor.val(ws, 'H%d' % r, ubi, verde_=True)
        motor.val(ws, 'I%d' % r, float(temp), fmt=FMT_ENT, verde_=True)
        motor.val(ws, 'J%d' % r,
                  CONSERVACION[1] if temp < 0 else CONSERVACION[0],
                  verde_=True)
        motor.val(ws, 'P%d' % r, resp, verde_=True)
        motor.val(ws, 'Q%d' % r, momento, verde_=True)
        ws.row_dimensions[r].height = 28
    for r in range(R_INI, R_FIN + 1):
        motor.verde(ws, 'A%d:J%d' % (r, r))
        motor.verde(ws, 'P%d' % r)
        motor.verde(ws, 'Q%d' % r)
        motor.f(ws, 'K%d' % r,
                '=IFERROR(IF(OR(NOT(ISNUMBER($E{r})),NOT(ISNUMBER($D${d}))),'
                '"",$E{r}+$D${d}),"")'.format(r=r, d=R_DIAS), fmt=FMT_FECHA)
        motor.f(ws, 'L%d' % r,
                '=IFERROR(IF(OR(NOT(ISNUMBER($K{r})),NOT(ISNUMBER($D${h}))),'
                '"",$K{r}-$D${h}),"")'.format(r=r, h=R_HOY), fmt=FMT_ENT,
                align='center')
        motor.f(ws, 'M%d' % r,
                '=IF(NOT(ISNUMBER($L{r})),"",IF($L{r}>0,"{cons}",'
                'IF($L{r}=0,"{ult}","{fin}")))'
                .format(r=r, cons=EST_CONS, ult=EST_ULT, fin=EST_FIN))
        motor.f(ws, 'N%d' % r,
                '=IF(OR(NOT(ISNUMBER($G{r})),NOT(ISNUMBER($D${g}))),"",'
                'IF($G{r}>=$D${g},"{ok}","{mal}"))'
                .format(r=r, g=R_GRAMOS, ok=GR_OK, mal=GR_MAL))
        # A7 de la refutación xlsx: comparar contra las CELDAS de la lista
        # («Registro de Comidas Testigo»!$A$72:$A$73), no contra el literal.
        motor.f(ws, 'O%d' % r,
                '=IF(OR($J{r}="",NOT(ISNUMBER($I{r}))),"",'
                'IF($J{r}=$A${refr},IF($I{r}<=$D${tr},"{ok}","{mal}"),'
                'IF($J{r}=$A${cong},IF($I{r}<=$D${tc},"{ok}","{mal}"),"")))'
                .format(r=r, refr=R_CONS_INI, cong=R_CONS_INI + 1,
                        tr=R_TREF, tc=R_TCON, ok=TP_OK, mal=TP_MAL))
        # B3 de la refutación xlsx: si evento y servicio son establecimientos
        # distintos (art. 30.9), una elaboración con «Toma única» debe avisar.
        motor.f(ws, 'R%d' % r,
                '=IF(OR($Q{r}="",$D${dist}=""),"",'
                'IF(AND($D${dist}="Sí",$Q{r}=$A${unica}),'
                '"Revisar: art. 30.9 exige DOS tomas (salida del obrador y '
                'servicio) cuando elaboras y sirves en establecimientos '
                'distintos",""))'
                .format(r=r, dist=R_EV_DIST, unica=R_MOM_FIN))

    filas = list(range(R_INI, R_FIN + 1))
    motor.dv_fecha(ws, ['E%d' % r for r in filas])
    dv_rango(ws, ['J%d' % r for r in filas], REF_CONSERVACION, 'Conservación',
             'Elige Refrigeración o Congelación de la lista del final de '
             'esta hoja.')
    dv_rango(ws, ['Q%d' % r for r in filas], REF_MOMENTO_TOMA,
             'Momento de la toma',
             'Elige un momento de la lista del final de esta hoja.')
    motor.dv_numerica(ws, ['G%d' % r for r in filas], minimo=0,
                      titulo='Gramos')
    motor.dv_numerica(ws, ['I%d' % r for r in filas], minimo=-40, maximo=20,
                      titulo='Temperatura (°C)',
                      mensaje='Escribe la temperatura en grados centígrados, '
                              'entre -40 y 20.')
    motor.semaforo_texto(ws, 'M%d:M%d' % (R_INI, R_FIN),
                         ((EST_CONS, motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          (EST_ULT, motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          (EST_FIN, motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    for col, ok, mal in (('N', GR_OK, GR_MAL), ('O', TP_OK, TP_MAL)):
        motor.semaforo_texto(ws, '%s%d:%s%d' % (col, R_INI, col, R_FIN),
                             ((ok, motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                              (mal, motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    motor.regla_expresion(ws, 'R%d:R%d' % (R_INI, R_FIN),
                          '=LEN($R{a})>0'.format(a=R_INI))

    # --- resumen ----------------------------------------------------------
    seccion(ws, 'A%d' % R_RES, 'RESUMEN DEL REGISTRO')
    cabecera(ws, R_RCAB, [('A', 'Indicador'), ('D', 'Valor')], altura=20)
    pintar_cabecera(ws, R_RCAB, 'BC')
    ws.merge_cells('A%d:C%d' % (R_RCAB, R_RCAB))
    resumen = [
        ('Muestras registradas',
         '=COUNTIF($A${a}:$A${b},"<>")'.format(a=R_INI, b=R_FIN), FMT_ENT),
        ('Elaboraciones del menú del evento',
         '=COUNTIF({p}!$B${a}:$B${b},"<>")'.format(p=PROD, a=B_MINI,
                                                   b=B_MFIN), FMT_ENT),
        ('Muestras que faltan por tomar',
         '=IFERROR(IF(OR(NOT(ISNUMBER($D${a})),NOT(ISNUMBER($D${b}))),"",'
         '$D${b}-$D${a}),"")'.format(a=R_R1, b=R_R1 + 1), FMT_ENT),
        ('Muestras con los gramos por debajo del mínimo',
         '=COUNTIF($N${a}:$N${b},"{m}")'.format(a=R_INI, b=R_FIN, m=GR_MAL),
         FMT_ENT),
        ('Muestras con la temperatura fuera de rango',
         '=COUNTIF($O${a}:$O${b},"{m}")'.format(a=R_INI, b=R_FIN, m=TP_MAL),
         FMT_ENT),
        ('Muestras que ya se pueden destruir',
         '=COUNTIF($M${a}:$M${b},"{m}")'.format(a=R_INI, b=R_FIN, m=EST_FIN),
         FMT_ENT),
        ('Muestras con aviso de doble toma (art. 30.9)',
         '=COUNTIF($R${a}:$R${b},"<>")'.format(a=R_INI, b=R_FIN), FMT_ENT),
    ]
    for i, (texto, formula, fmt) in enumerate(resumen):
        r = R_R1 + i
        etiqueta(ws, r, texto)
        motor.f(ws, 'D%d' % r, formula, fmt=fmt, bold=True)
        gris(ws, 'D%d' % r)
    for r in (R_R1 + 2, R_R1 + 3, R_R1 + 4, R_R1 + 6):
        motor.semaforo_isnumber(ws, 'D%d' % r, '$D$%d' % r, operador='>',
                                umbral='0')

    fila = R_R1 + 7
    for texto in (
            'La comida testigo se guarda de CADA elaboración servida, no del '
            'plato montado: si el menú lleva seis elaboraciones, son seis '
            'muestras. ' + CE11,
            'Los siete días son un MÍNIMO legal. Si tu comunidad autónoma o el '
            'pliego del cliente te piden más, sube la celda verde: el libro '
            'recalcula la fecha de destrucción y la cuenta atrás.',
            'La muestra se identifica y se fecha. Una bolsa sin rotular no '
            'sirve de nada el día que hay que demostrar algo.',
            'Si el evento es de catering en dos establecimientos distintos '
            '(marca «Sí» en el bloque «El evento»), el art. 30.9 exige DOS '
            'tomas por elaboración: una a la salida del obrador y otra en el '
            'servicio. La columna «Momento de la toma» y el aviso de la '
            'columna «Aviso» son para eso. ' + CE11):
        nota(ws, fila, texto, alto=32, wrap=True)
        ws.merge_cells('A%d:O%d' % (fila, fila))
        fila += 1

    # --- listas de los desplegables (A1 de la refutación xlsx) ------------
    seccion(ws, 'A%d' % R_LSEC, 'LISTAS DE LOS DESPLEGABLES (no las borres)')
    cabecera(ws, R_SN_CAB, [('A', 'Sí / No')], altura=20)
    for i, texto in enumerate(SI_NO):
        motor.val(ws, 'A%d' % (R_SN_INI + i), texto)
    cabecera(ws, R_CONS_CAB, [('A', 'Conservación')], altura=20)
    for i, texto in enumerate(CONSERVACION):
        motor.val(ws, 'A%d' % (R_CONS_INI + i), texto)
    cabecera(ws, R_MOM_CAB, [('A', 'Momento de la toma (art. 30.9)')],
             altura=20)
    for i, texto in enumerate(MOMENTO_TOMA):
        motor.val(ws, 'A%d' % (R_MOM_INI + i), texto)
    nota(ws, R_MOM_FIN + 1,
         'Estas listas alimentan los desplegables de la hoja: no las borres '
         'ni las muevas.', wrap=True)

    ws.freeze_panes = 'C%d' % R_INI
    pagina(ws, titulos='$%d:$%d' % (R_CAB, R_CAB))
    return ws


# --------------------------------------------------------------------------
COLS_MENU = [
    ('A', 'Momento del menú', 'txt'),
    ('B', 'Id del plato', 'txt'),
    ('C', 'Elaboración', 'txt'),
    ('D', 'Partida', 'txt'),
    ('E', 'Raciones por comensal', 'dec'),
    ('F', 'Raciones a producir', 'ent'),
    ('G', 'Raciones por unidad de producción', 'ent'),
    ('H', 'Unidades de producción', 'ent'),
]

COLS_TIMING = [
    ('A', 'Fecha', 'fecha'),
    ('B', 'Hora', 'txt'),
    ('C', 'Hito', 'txt'),
    ('D', 'Partida o área', 'txt'),
    ('E', 'Responsable (id)', 'txt'),
    ('F', 'Nombre', 'txt'),
]

COLS_PERSONAL = [
    ('A', 'Id', 'txt'),
    ('B', 'Nombre', 'txt'),
    ('C', 'Puesto en el evento', 'txt'),
    ('D', 'Horas', 'dec'),
    ('E', 'Día', 'fecha'),
]


def hoja_banquete(wb):
    ws = wb.create_sheet('Producción y Ficha de Banquete')
    encabezar(ws, 'Producción y ficha de banquete',
              nota='Todo se calcula desde los comensales. Si cambian la '
                   'víspera, cambia una celda y se recalcula la producción '
                   'entera.')
    anchos(ws, {'A': 17, 'B': 12, 'C': 52, 'D': 21, 'E': 16, 'F': 16,
                'G': 18, 'H': 16, 'I': 40})

    # --- el evento (espejo) ----------------------------------------------
    seccion(ws, 'A5',
            'EL EVENTO — se lee de la hoja «Registro de Comidas Testigo»; '
            'cámbialo allí, no aquí')
    espejo = [
        (B_EV_ID, 'Id del evento', 'D$%d' % R_EV_ID, None),
        (B_EV_FEC, 'Fecha del evento', 'D$%d' % R_EV_FEC, FMT_FECHA),
        (B_EV_COM, 'Comensales', 'D$%d' % R_EV_COM, FMT_ENT),
    ]
    for fila, texto, origen, fmt in espejo:
        motor.val(ws, 'A%d' % fila, texto, bold=True)
        ws.merge_cells('A%d:B%d' % (fila, fila))
        motor.f(ws, 'C%d' % fila,
                '=IF({r}!${o}="","",{r}!${o})'.format(r=REG, o=origen),
                fmt=fmt, bold=True)
        gris(ws, 'C%d' % fila)
    motor.val(ws, 'A%d' % B_EV_ALERTA, 'Obligación de comida testigo',
              bold=True)
    ws.merge_cells('A%d:B%d' % (B_EV_ALERTA, B_EV_ALERTA))
    motor.f(ws, 'C%d' % B_EV_ALERTA,
            '=IF({r}!$D${o}="","",{r}!$D${o})'.format(r=REG, o=R_EV_ALERTA),
            bold=True)
    ws.merge_cells('C%d:I%d' % (B_EV_ALERTA, B_EV_ALERTA))
    motor.semaforo_texto(ws, 'C%d' % B_EV_ALERTA,
                         ((ALERTA_SI, motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          (ALERTA_NO, motor.CF_AMBAR_BG, motor.CF_AMBAR_FG)))

    # --- menú y producción por plato -------------------------------------
    seccion(ws, 'A11', 'MENÚ Y PRODUCCIÓN POR PLATO')
    cabecera(ws, B_MCAB, [(c, t) for c, t, _ in COLS_MENU], altura=48)
    comensales = float(EV['comensales'])
    for i, fila in enumerate(D.BANQUETE_MENU):
        r = B_MINI + i
        momento, idp, plato, partida, raciones, por_unidad, _uds = fila
        motor.val(ws, 'A%d' % r, momento, verde_=True)
        motor.val(ws, 'B%d' % r, idp, verde_=True)
        motor.val(ws, 'C%d' % r, plato, verde_=True, wrap=True)
        motor.val(ws, 'D%d' % r, partida, verde_=True)
        # raciones por comensal DERIVADO del menú, no tecleado
        motor.val(ws, 'E%d' % r, round(raciones / comensales, 4),
                  fmt=FMT_DEC3, verde_=True)
        motor.val(ws, 'G%d' % r, float(por_unidad), fmt=FMT_ENT, verde_=True)
        ws.row_dimensions[r].height = 28

    for r in range(B_MINI, B_MFIN + 1):
        motor.verde(ws, 'A%d:E%d' % (r, r))
        motor.verde(ws, 'G%d' % r)
        motor.f(ws, 'F%d' % r,
                '=IFERROR(IF(OR(NOT(ISNUMBER($E{r})),NOT(ISNUMBER($C${c}))),'
                '"",ROUND($C${c}*$E{r},0)),"")'.format(r=r, c=B_EV_COM),
                fmt=FMT_ENT, align='center')
        motor.f(ws, 'H%d' % r,
                '=IFERROR(IF(OR(NOT(ISNUMBER($F{r})),NOT(ISNUMBER($G{r})),'
                '$G{r}=0),"",ROUNDUP($F{r}/$G{r},0)),"")'.format(r=r),
                fmt=FMT_ENT, align='center')

    motor.val(ws, 'A%d' % B_MTOT, 'TOTAL', bold=True)
    ws.merge_cells('A%d:D%d' % (B_MTOT, B_MTOT))
    for col in 'EFH':
        fmt = FMT_DEC3 if col == 'E' else FMT_ENT
        motor.f(ws, '%s%d' % (col, B_MTOT),
                '=IF(COUNT({c}{a}:{c}{b})=0,"",SUM({c}{a}:{c}{b}))'
                .format(c=col, a=B_MINI, b=B_MFIN), fmt=fmt, bold=True)
    fila_total(ws, B_MTOT, 'A', 'H')

    filas = list(range(B_MINI, B_MFIN + 1))
    dv_rango(ws, ['D%d' % r for r in filas], REF_PARTIDAS_BANQUETE, 'Partida',
             'Elige una partida de la lista del final de esta hoja.')
    motor.dv_numerica(ws, ['E%d' % r for r in filas], minimo=0, maximo=20,
                      titulo='Raciones por comensal',
                      prompt='Cuántas raciones de este plato sirve CADA '
                             'comensal: 1 si lo toman todos, 0,4 si es uno de '
                             'los dos principales a elegir.')
    motor.dv_numerica(ws, ['G%d' % r for r in filas], minimo=1,
                      titulo='Raciones por unidad')

    # --- producción por partida ------------------------------------------
    seccion(ws, 'A27', 'PRODUCCIÓN POR PARTIDA — así se manda el trabajo')
    cabecera(ws, B_PCAB, [('A', 'Partida'), ('C', 'Raciones a producir'),
                          ('D', 'Unidades de producción'),
                          ('E', 'Porcentaje del total')], altura=32)
    pintar_cabecera(ws, B_PCAB, 'B')
    ws.merge_cells('A%d:B%d' % (B_PCAB, B_PCAB))
    for i, partida in enumerate(D.PARTIDAS_PRODUCCION):
        r = B_PINI + i
        motor.val(ws, 'A%d' % r, partida, bold=True)
        ws.merge_cells('A%d:B%d' % (r, r))
        for col, origen in (('C', 'F'), ('D', 'H')):
            motor.f(ws, '%s%d' % (col, r),
                    '=IFERROR(IF(COUNTIF($D${a}:$D${b},$A{r}&"")=0,"",'
                    'SUMIF($D${a}:$D${b},$A{r}&"",${o}${a}:${o}${b})),"")'
                    .format(a=B_MINI, b=B_MFIN, r=r, o=origen), fmt=FMT_ENT,
                    align='center')
        motor.f(ws, 'E%d' % r,
                '=IFERROR(IF(OR(NOT(ISNUMBER($C{r})),NOT(ISNUMBER($C${t})),'
                '$C${t}=0),"",$C{r}/$C${t}),"")'.format(r=r, t=B_PTOT),
                fmt=FMT_PCT)
    motor.val(ws, 'A%d' % B_PTOT, 'TOTAL', bold=True)
    ws.merge_cells('A%d:B%d' % (B_PTOT, B_PTOT))
    for col in 'CD':
        motor.f(ws, '%s%d' % (col, B_PTOT),
                '=IF(COUNT({c}{a}:{c}{b})=0,"",SUM({c}{a}:{c}{b}))'
                .format(c=col, a=B_PINI, b=B_PFIN), fmt=FMT_ENT, bold=True)
    motor.f(ws, 'E%d' % B_PTOT,
            '=IF(COUNT($E${a}:$E${b})=0,"",SUM($E${a}:$E${b}))'
            .format(a=B_PINI, b=B_PFIN), fmt=FMT_PCT, bold=True)
    fila_total(ws, B_PTOT, 'A', 'E')
    motor.val(ws, 'G%d' % B_PINI,
              'Las partidas que no producen nada en este evento se quedan en '
              'blanco, no en cero: en esta familia «sin dato» y «cero» no son '
              'lo mismo.')

    # --- timing -----------------------------------------------------------
    seccion(ws, 'A35', 'TIMING DEL EVENTO')
    cabecera(ws, B_TCAB, [(c, t) for c, t, _ in COLS_TIMING], altura=28)
    for i, fila in enumerate(D.BANQUETE_TIMING):
        r = B_TINI + i
        cuando, hito, area, resp = fila
        fecha, hora = cuando.split(' ')
        motor.val(ws, 'A%d' % r, D._fecha(fecha), fmt=FMT_FECHA, verde_=True)
        motor.val(ws, 'B%d' % r, hora, verde_=True, align='center')
        motor.val(ws, 'C%d' % r, hito, verde_=True, wrap=True)
        motor.val(ws, 'D%d' % r, area, verde_=True)
        motor.val(ws, 'E%d' % r, resp, verde_=True, align='center')
        motor.val(ws, 'F%d' % r, NOMBRES.get(resp, ''), verde_=True)
        ws.row_dimensions[r].height = 26
    for r in range(B_TINI, B_TFIN + 1):
        motor.verde(ws, 'A%d:F%d' % (r, r))
    motor.dv_fecha(ws, ['A%d' % r for r in range(B_TINI, B_TFIN + 1)])

    # --- personal ---------------------------------------------------------
    seccion(ws, 'A53', 'PERSONAL ASIGNADO AL EVENTO')
    cabecera(ws, B_HCAB, [(c, t) for c, t, _ in COLS_PERSONAL], altura=28)
    for i, fila in enumerate(D.BANQUETE_PERSONAL):
        r = B_HINI + i
        pid, puesto, horas, dia = fila
        motor.val(ws, 'A%d' % r, pid, verde_=True, align='center')
        motor.val(ws, 'B%d' % r, NOMBRES.get(pid, ''), verde_=True)
        motor.val(ws, 'C%d' % r, puesto, verde_=True)
        motor.val(ws, 'D%d' % r, float(horas), fmt=FMT_DEC, verde_=True)
        motor.val(ws, 'E%d' % r, D._fecha(dia), fmt=FMT_FECHA, verde_=True)
    for r in range(B_HINI, B_HFIN + 1):
        motor.verde(ws, 'A%d:E%d' % (r, r))
    motor.dv_numerica(ws, ['D%d' % r for r in range(B_HINI, B_HFIN + 1)],
                      minimo=0, maximo=24, titulo='Horas')
    motor.dv_fecha(ws, ['E%d' % r for r in range(B_HINI, B_HFIN + 1)])

    motor.val(ws, 'A%d' % B_HTOT, 'TOTAL de horas del evento', bold=True)
    ws.merge_cells('A%d:C%d' % (B_HTOT, B_HTOT))
    motor.f(ws, 'D%d' % B_HTOT,
            '=IF(COUNT($D${a}:$D${b})=0,"",SUM($D${a}:$D${b}))'
            .format(a=B_HINI, b=B_HFIN), fmt=FMT_DEC, bold=True)
    fila_total(ws, B_HTOT, 'A', 'E')
    motor.val(ws, 'A%d' % B_HCOM, 'Horas de cocina por comensal', bold=True)
    ws.merge_cells('A%d:C%d' % (B_HCOM, B_HCOM))
    motor.f(ws, 'D%d' % B_HCOM,
            '=IFERROR(IF(OR(NOT(ISNUMBER($D${t})),NOT(ISNUMBER($C${c})),'
            '$C${c}=0),"",$D${t}/$C${c}),"")'.format(t=B_HTOT, c=B_EV_COM),
            fmt=FMT_DEC3, bold=True)
    gris(ws, 'D%d' % B_HCOM)

    fila = B_HCOM + 2
    for texto in (
            'Las horas de este evento son EXTRA sobre la jornada ordinaria de '
            'la brigada, así que hay que sumarlas a las horas de cocina de la '
            'semana en el cuadro de mando (libro 1). Un banquete que no se '
            'apunta en las horas hace parecer que esa semana la cocina fue '
            'cara sin motivo.',
            'La toma de las comidas testigo está en el timing a propósito: es '
            'la única forma de que no se olvide justo el día en que hay 120 '
            'personas esperando. ' + CE11,
            'Las temperaturas de servicio del banquete son las mismas de '
            'siempre: lo que se mantiene en caliente, a 63 °C o más. ' + CE10):
        nota(ws, fila, texto, alto=44, wrap=True)
        ws.merge_cells('A%d:I%d' % (fila, fila))
        fila += 1

    # --- lista del desplegable de partida (A1 de la refutación xlsx) ------
    seccion(ws, 'A%d' % B_LSEC, 'LISTA DEL DESPLEGABLE (no la borres)')
    cabecera(ws, B_PART_CAB, [('A', 'Partidas de tu cocina')], altura=20)
    for i, partida in enumerate(D.ESTACIONES):
        motor.val(ws, 'A%d' % (B_PART_INI + i), partida, verde_=True)
    nota(ws, B_PART_FIN + 1,
         'Son las mismas partidas del cuadro de mando de cocina (libro 1). '
         'Cópialas de allí: este libro no lee ningún fichero ajeno.',
         wrap=True)

    ws.freeze_panes = 'C%d' % B_MINI
    pagina(ws, titulos='$%d:$%d' % (B_MCAB, B_MCAB))
    return ws


# --------------------------------------------------------------------------
def mapa():
    celdas_r = {
        'Comensales a partir de los que obliga': 'D%d' % R_UMBRAL,
        'Gramos mínimos por elaboración': 'D%d' % R_GRAMOS,
        'Días de conservación de la muestra': 'D%d' % R_DIAS,
        'Temperatura máxima en refrigeración': 'D%d' % R_TREF,
        'Temperatura máxima en congelación': 'D%d' % R_TCON,
        'Fecha para simular': 'D%d' % R_SIM,
        'Hoy (fecha de referencia)': 'D%d' % R_HOY,
        'Id del evento': 'D%d' % R_EV_ID,
        'Fecha del evento': 'D%d' % R_EV_FEC,
        'Comensales del evento': 'D%d' % R_EV_COM,
        '¿Elaboración y servicio en establecimientos distintos?':
            'D%d' % R_EV_DIST,
        'ALERTA de obligación de comida testigo': 'D%d' % R_EV_ALERTA,
        'Supuestos del art. 30.8 marcados': 'D%d' % R_SUP_TOT,
        'Muestras registradas': 'D%d' % R_R1,
        'Elaboraciones del menú del evento': 'D%d' % (R_R1 + 1),
        'Muestras que faltan por tomar': 'D%d' % (R_R1 + 2),
        'Muestras con los gramos por debajo del mínimo': 'D%d' % (R_R1 + 3),
        'Muestras con la temperatura fuera de rango': 'D%d' % (R_R1 + 4),
        'Muestras que ya se pueden destruir': 'D%d' % (R_R1 + 5),
        'Muestras con aviso de doble toma (art. 30.9)': 'D%d' % (R_R1 + 6),
    }
    for i, fila in enumerate(D.COMIDAS_TESTIGO):
        r = R_INI + i
        et = 'de la muestra ' + fila[0]
        celdas_r['Fecha de destrucción prevista ' + et] = 'K%d' % r
        celdas_r['Días que faltan ' + et] = 'L%d' % r
        celdas_r['Estado ' + et] = 'M%d' % r
        celdas_r['Gramos suficientes ' + et] = 'N%d' % r
        celdas_r['Temperatura conforme ' + et] = 'O%d' % r
        celdas_r['Momento de la toma ' + et] = 'Q%d' % r
        celdas_r['Aviso de doble toma ' + et] = 'R%d' % r

    celdas_b = {
        'Id del evento (espejo)': 'C%d' % B_EV_ID,
        'Fecha del evento (espejo)': 'C%d' % B_EV_FEC,
        'Comensales (espejo)': 'C%d' % B_EV_COM,
        'Obligación de comida testigo (espejo)': 'C%d' % B_EV_ALERTA,
        'Raciones por comensal del menú completo': 'E%d' % B_MTOT,
        'Raciones a producir en total': 'F%d' % B_MTOT,
        'Unidades de producción en total': 'H%d' % B_MTOT,
        'Raciones a producir de todas las partidas': 'C%d' % B_PTOT,
        'Unidades de producción de todas las partidas': 'D%d' % B_PTOT,
        'Horas totales del evento': 'D%d' % B_HTOT,
        'Horas de cocina por comensal': 'D%d' % B_HCOM,
    }
    for i, fila in enumerate(D.BANQUETE_MENU):
        r = B_MINI + i
        et = 'del plato ' + fila[1]
        celdas_b['Raciones a producir ' + et] = 'F%d' % r
        celdas_b['Unidades de producción ' + et] = 'H%d' % r
    for i, partida in enumerate(D.PARTIDAS_PRODUCCION):
        r = B_PINI + i
        celdas_b['Raciones de la partida ' + partida] = 'C%d' % r
        celdas_b['Unidades de producción de la partida ' + partida] = 'D%d' % r
        celdas_b['Porcentaje del total de la partida ' + partida] = 'E%d' % r

    tipo = {'eur': 'eur', 'pct': 'pct1', 'ent': 'num', 'dec': 'num',
            'fecha': 'txt', 'txt': 'txt'}
    return {
        'fichero': NOMBRE + '.xlsx',
        'producto': 'manual-chef-ejecutivo',
        'libro': 6,
        'que_decide': ('Si este encargo dispara la obligación de comidas '
                       'testigo y cómo se produce el evento'),
        'alerta_comida_testigo': {
            'celda': 'Registro de Comidas Testigo!D%d' % R_EV_ALERTA,
            'texto': ALERTA_SI,
            'celda_umbral': 'Registro de Comidas Testigo!D%d' % R_UMBRAL,
            'umbral_comensales': CT['umbral_comensales'],
            'id_research': CT['ce_id'],
            'norma': CT['norma'],
            'url': CT['url'],
            'tambien_por_supuesto': ('Registro de Comidas Testigo!D%d'
                                     % R_SUP_TOT),
        },
        'cuenta_atras': {
            'celda_dias': 'Registro de Comidas Testigo!D%d' % R_DIAS,
            'dias': CT['dias_conservacion'],
            'columna_dias_que_faltan': 'Registro de Comidas Testigo!L',
            'columna_estado': 'Registro de Comidas Testigo!M',
            'dias_naturales': True,
        },
        'sin_hojas_de_desperdicio': True,
        # A4 de la refutación xlsx (2026-09-06): «Barra y bebidas» no
        # interviene en el menú de este banquete, así que su fila queda a
        # propósito sin raciones ni unidades de producción.
        'vacias_a_proposito': [
            'Producción y Ficha de Banquete!C32',
            'Producción y Ficha de Banquete!D32',
            'Producción y Ficha de Banquete!E32',
        ],
        'hojas': {
            'Registro de Comidas Testigo': {
                'celdas': celdas_r,
                'tablas': [
                    {'titulo': 'Parámetros legales de las comidas testigo',
                     'cols': [['Parámetro', 'A', 'txt'],
                              ['Valor', 'D', 'num'],
                              ['Base legal', 'E', 'txt']],
                     'filas': [R_UMBRAL, R_TCON]},
                    {'titulo': 'Supuestos del artículo 30.8',
                     'cols': [['Supuesto', 'A', 'txt'],
                              ['¿Te aplica?', 'D', 'txt']],
                     'filas': [R_SUP_INI, R_SUP_FIN]},
                    {'titulo': 'Muestras tomadas',
                     'cols': [[t, c, tipo[k]] for c, t, k in COLS_MUESTRAS],
                     'filas': [R_INI, R_FIN]},
                    {'titulo': 'Resumen del registro',
                     'cols': [['Indicador', 'A', 'txt'],
                              ['Valor', 'D', 'num']],
                     'filas': [R_R1, R_R1 + 6]},
                ],
            },
            'Producción y Ficha de Banquete': {
                'celdas': celdas_b,
                'tablas': [
                    {'titulo': 'Menú y producción por plato',
                     'cols': [[t, c, tipo[k]] for c, t, k in COLS_MENU],
                     'filas': [B_MINI, B_MTOT]},
                    {'titulo': 'Producción por partida',
                     'cols': [['Partida', 'A', 'txt'],
                              ['Raciones a producir', 'C', 'num'],
                              ['Unidades de producción', 'D', 'num'],
                              ['Porcentaje del total', 'E', 'pct1']],
                     'filas': [B_PINI, B_PTOT]},
                    {'titulo': 'Timing del evento',
                     'cols': [[t, c, tipo[k]] for c, t, k in COLS_TIMING],
                     'filas': [B_TINI, B_TFIN]},
                    {'titulo': 'Personal asignado al evento',
                     'cols': [[t, c, tipo[k]] for c, t, k in COLS_PERSONAL],
                     'filas': [B_HINI, B_HTOT]},
                ],
            },
        },
    }


def main():
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_registro(wb)
    hoja_banquete(wb)

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
