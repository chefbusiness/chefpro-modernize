#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_brigada-puestos-y-evaluacion.py — libro 4 de «Manual del Chef Ejecutivo»
(SPEC §2.2 fila 4, y las decisiones D3, D7, D8, D9 y D11).

Hojas: Instrucciones · Organigrama · Fichas de Puesto · Matriz RACI ·
Rúbrica de Competencias · Prueba Práctica · Plan de Desarrollo Individual ·
Histórico.

QUÉ DECIDE ESTE LIBRO
---------------------
A quién promocionar, a quién formar en qué y quién decide qué. Los cuatro
libros que la SPEC fundió aquí (organigrama, fichas de puesto, RACI y
evaluación técnica) responden a la misma pregunta desde cuatro sitios, y
separarlos obligaba a teclear la brigada cuatro veces.

LO QUE NO HACE, Y DÓNDE SE HACE (reglas de no-solape de la SPEC)
---------------------------------------------------------------
* **No pregunta «¿puede cubrir esta partida?»**. Eso es la matriz de
  polivalencia del «Manual del Manager de Restaurante», y aquí sólo se COPIA su
  resultado en una columna, para poder contrastarlo con la nota técnica. Es
  literalmente el capítulo 18: cobertura no es competencia. Quien cubre el pase
  un viernes no necesariamente domina el pase.
* **No es la evaluación genérica del Kit de Gestión de Personal**: ésta es
  técnica, se puntúa POR PRUEBA PRÁCTICA y sólo evalúa a quien pisa cocina. Las
  cuatro personas de sala pura salen con sus siete casillas en N/A, y N/A no es
  un cero: sale de la media, no la baja.
* **El Plan de Desarrollo Individual REMITE por texto al Plan de Cross-Training
  del Manager** (SPEC D4: cero fórmulas entre ficheros). No lo repite y no lo
  enlaza: lo cita, con la fila.

DECISIONES TÉCNICAS
-------------------
* Las funciones de los diez puestos son las LITERALES del art. 17.B del ALEH VI
  (`datos_ejemplo.PUESTOS_ALEH`), con su fuente y su fecha de verificación. La
  columna de al lado es verde: ahí va lo que en TU casa hace ese puesto y el
  convenio no dice. No se toca el literal.
* **La media ponderada ignora los N/A** y se calcula a la vista: siete columnas
  de «peso aplicado» (INDEX/MATCH sobre la tabla de pesos por puesto, vacías
  cuando la competencia es N/A) y siete de «puntos ponderados». La media es la
  división de las dos sumas, no un `SUMPRODUCT` que nadie puede auditar.
* **Todas las listas desplegables van contra un RANGO** de la propia hoja, nunca
  contra una cadena de opciones separadas por comas.
* «Partidas activas» (3-8) gobierna el alcance del organigrama (SPEC D7): las
  filas de más se marcan «Fuera del alcance» y el semáforo las ignora.
* Cero constantes dentro de las fórmulas de cálculo; `IFERROR(...,"")` en todo
  cociente; «sin dato» = `""`; semáforos con `ISNUMBER`; prohibidas `INDIRECT`,
  `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA`, `RANK` y
  `NETWORKDAYS`: cero usos. Textos 100 % WinAnsi (cp1252).
* Término único «partida» (SPEC D9); la glosa «(estación)» se escribe UNA vez,
  en el primer paso de «Instrucciones», y la nota de equivalencia con la matriz
  del Manager acompaña a «próxima partida a aprender».

Salida fija: build/brigada-puestos-y-evaluacion.xlsx + su mapa de celdas.
Via: Claude Code
"""
import json
import os
import sys

from openpyxl import Workbook
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
TITULO = 'Brigada, puestos y evaluación técnica'
NOMBRE = 'brigada-puestos-y-evaluacion'

FMT_EUR = motor.FMT_EUR
FMT_PCT = motor.FMT_PCT
FMT_ENT = motor.FMT_ENT
FMT_FECHA = motor.FMT_FECHA
FMT_DEC = '#,##0.00'

GRIS = 'F2F2F2'
CREMA = 'FFF6DC'
ORO = 'FFD700'
CABECERA = '2D2D2D'

FECHA_VERIF = '06-09-2026'

H_ORG = 'Organigrama'
H_PUESTOS = 'Fichas de Puesto'
H_RACI = 'Matriz RACI'
#: El nombre de la SPEC («Rúbrica de Competencias Técnicas») tiene 32
#: caracteres y Excel corta las pestañas en 31. Se acorta aquí y el mapa lo
#: declara, para que el guion cite la hoja que existe de verdad.
H_RUBRICA = 'Rúbrica de Competencias'
H_PRUEBA = 'Prueba Práctica'
H_PDI = 'Plan de Desarrollo Individual'
H_HIST = 'Histórico'


# --------------------------------------------------------------------------
def sector(idd):
    """Entrada `CE-*`/`MM-*`/`CS-*` del JSON de research (norma, URL, cifra)."""
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


MM14 = sector('MM-14')      # áreas funcionales y grupos profesionales
CE04 = sector('CE-04')      # formación de higiene por puesto
CE27 = sector('CE-27')      # formación PRL: coste nunca del trabajador


# --------------------------------------------------------------------------
# Vocabulario y derivaciones (todo sale de `datos_ejemplo`)
# --------------------------------------------------------------------------
PARTIDAS = [p[0] for p in D.PARTIDAS]
SI_NO = ['Sí', 'No']
LETRAS_RACI = (
    ('R', 'Hace el trabajo. Puede haber varios.'),
    ('A', 'Responde del resultado. Uno y sólo uno por decisión.'),
    ('C', 'Se le consulta ANTES de decidir.'),
    ('I', 'Se le informa DESPUÉS de decidir.'),
)
ESTADOS_PDI = ['Planificado', 'En curso', 'Cerrado']
LECTURAS = ['Coherente', 'Cubre por encima de lo que domina',
            'Domina más de lo que cubre']
NO_EVALUADO = 'No evaluado en la rúbrica de cocina'

ORDEN_GRUPO = {'Grupo I': 1, 'Grupo II': 2, 'Grupo III': 3}


def titular_de(partida):
    """Titular de una partida: quien la tiene como principal y está en el grupo
    profesional más alto; a igualdad, quien lleva más tiempo en la casa.

    Se DERIVA de `PLANTILLA`, no se teclea: si mañana cambia la plantilla,
    cambia el organigrama.
    """
    candidatos = [p for p in D.PLANTILLA if p[9] == partida]
    if not candidatos:
        return ''
    candidatos.sort(key=lambda p: (ORDEN_GRUPO.get(p[4], 9), p[8]))
    p = candidatos[0]
    return '%s (%s)' % (p[1], p[0])


def puesto_convenio(pid):
    """Puesto del ALEH VI que ocupa esa persona, según `PUESTOS_ALEH`."""
    for puesto, _g, _f, _n, ocupantes in D.PUESTOS_ALEH:
        if pid in [x.strip() for x in ocupantes.split(',') if x.strip()]:
            return puesto
    return ''


def delegacion_de(puesto):
    for p, _g, _f, nivel, _o in D.PUESTOS_ALEH:
        if p == puesto:
            return nivel
    return ''


def proxima_partida(pid):
    """Próxima partida a aprender: la del Plan de Cross-Training del Manual del
    Manager para esa persona (SPEC D9). Copia declarada, no vínculo."""
    for idp, estacion, _na, _no, _resp, _fecha, _estado in D.PLAN_CROSS_TRAINING:
        if idp == pid:
            return estacion
    return ''


PLANTILLA_N = len(D.PLANTILLA)
N_ORG_PARTIDAS = 8                    # la SPEC D7 permite de 3 a 8
N_ORG_BRIGADA = PLANTILLA_N + 4
N_RACI = len(D.RACI) + 5
N_PDI = len(D.PDI) + 6
EVALUADOS = [e for e in D.EVALUACIONES if e[2]]
N_HIST = len(EVALUADOS) + 12


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
    for fila in ws[rango]:
        for c in fila:
            c.fill = PatternFill('solid', fgColor=CABECERA)


def seccion(ws, coord, texto):
    motor.val(ws, coord, texto, bold=True)
    ws[coord].font = Font(bold=True, size=12)


def nota(ws, fila, texto, col='A', alto=None, wrap=False):
    motor.val(ws, col + str(fila), texto, wrap=wrap)
    ws[col + str(fila)].font = Font(italic=True, size=9)
    if alto:
        ws.row_dimensions[fila].height = alto


def parrafo(ws, fila, texto, col_ini='A', col_fin='F', alto=30):
    ws.merge_cells('%s%d:%s%d' % (col_ini, fila, col_fin, fila))
    motor.val(ws, '%s%d' % (col_ini, fila), texto, wrap=True)
    ws['%s%d' % (col_ini, fila)].font = Font(italic=True, size=9)
    ws.row_dimensions[fila].height = alto


def anchos(ws, mapa):
    for letra, ancho in mapa.items():
        ws.column_dimensions[letra].width = ancho


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


def encabezar(ws, titulo, nota_txt=None, col_fin='F'):
    motor.val(ws, 'A1', titulo)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', SUBTITULO)
    if nota_txt:
        ws.merge_cells('A3:%s3' % col_fin)
        motor.val(ws, 'A3', nota_txt, wrap=True)
        ws['A3'].font = Font(italic=True, size=9)
        ws.row_dimensions[3].height = 26


def dv_rango(ws, coords, ref, titulo, mensaje):
    """Desplegable cuyo origen es un RANGO de la propia hoja (SPEC §2.2)."""
    if not coords:
        return None
    dv = DataValidation(type='list', formula1=ref, allow_blank=True,
                        showErrorMessage=True, errorTitle=titulo,
                        error=mensaje)
    ws.add_data_validation(dv)
    for c in coords:
        dv.add(c)
    return dv


# --------------------------------------------------------------------------
# Hoja «Instrucciones»
# --------------------------------------------------------------------------
PASOS = [
    '1. Hoja «Organigrama»: declara cuántas partidas (estaciones, en el '
    'vocabulario de la matriz de polivalencia del Manual del Manager) tiene tu '
    'cocina, ponles nombre y di quién es el titular de cada una. Debajo va la '
    'brigada: una fila por persona, con su puesto del convenio y su partida '
    'principal. Es la hoja que alimenta a todas las demás.',
    '2. Hoja «Fichas de Puesto»: los diez puestos de cocina del convenio con '
    'sus funciones LITERALES. Esa columna no se toca: es lo que pone el ALEH '
    'VI, y es lo que un inspector o un abogado va a leer. Lo que sí escribes '
    'es la columna verde de al lado, con lo que en TU casa hace ese puesto y '
    'el convenio no dice: cerrar la cámara, pasar el pedido del pescado, '
    'llevar el registro de temperaturas.',
    '3. Hoja «Matriz RACI»: quince decisiones que cruzan cocina, sala y '
    'dirección. Para cada una, marca quién hace (R), quién responde (A), a '
    'quién se consulta antes (C) y a quién se informa después (I). La hoja te '
    'avisa si una decisión se ha quedado sin A o con dos: es el fallo que hace '
    'que un plato se retire de la carta dos veces y ninguna.',
    '4. Hoja «Rúbrica de Competencias»: siete competencias técnicas con los '
    'cinco niveles descritos, los pesos de cada una POR PUESTO y la evaluación '
    'de tu gente. Puntúa de 1 a 5 y deja en blanco lo que no aplique. La media '
    'ponderada ignora los blancos: un ayudante que no hace fondos no baja nota '
    'por no hacerlos.',
    '5. Hoja «Prueba Práctica»: el guion de la prueba, una por competencia, con '
    'lo que es un 5 y lo que es un 1. Sin esto, la rúbrica es una opinión; con '
    'esto, es una nota que se puede defender delante de quien la recibe.',
    '6. Hoja «Plan de Desarrollo Individual»: qué va a trabajar cada persona, '
    'con quién, para cuándo y en qué estado está. La columna «próxima partida a '
    'aprender» es la que enlaza con el plan de cross-training del Manual del '
    'Manager: no se repite aquí, se cita.',
    '7. Hoja «Histórico»: una línea por evaluación y por persona. La primera '
    'ronda no dice nada; la segunda es la que enseña quién ha crecido y quién '
    'lleva año y medio en el mismo sitio.',
]

NOTAS_LIBRO = [
    'COBERTURA NO ES COMPETENCIA, y es la confusión que más caro sale. La '
    'matriz de polivalencia del «Manual del Manager de Restaurante» responde a '
    '«¿puede sostener esta partida en un servicio?». Esta rúbrica responde a '
    '«¿con qué nivel técnico?». La columna «nivel en cocina» de la hoja '
    '«Rúbrica de Competencias» es una COPIA de aquella matriz, puesta ahí para '
    'poder contrastarlas: quien cubre el pase un viernes no necesariamente lo '
    'domina.',
    'N/A NO ES CERO. Una competencia que no aplica a un puesto se deja en '
    'blanco y sale de la media; un cero dice que se hizo la prueba y salió mal. '
    'Las cuatro personas de sala pura del ejemplo tienen las siete casillas en '
    'blanco: su evaluación genérica vive en el Kit de Gestión de Personal, no '
    'aquí.',
    'Las funciones de los diez puestos son las del convenio, palabra por '
    'palabra. «Chef ejecutivo», «chef corporativo» y «sous chef» NO son '
    'categorías del ALEH VI: son denominaciones de uso, y quien las lleva se '
    'clasifica por las funciones que hace. La tabla de equivalencias está en la '
    'hoja «Fichas de Puesto».',
    'La evaluación se puntúa POR PRUEBA PRÁCTICA, nunca por impresión ni por '
    'autoevaluación. Si no ha habido prueba, la casilla se queda en blanco: una '
    'nota sin prueba detrás no se sostiene el día que hay que explicar por qué '
    'asciende uno y no otro.',
    'Este libro no calcula nóminas, ni cuadrantes, ni coste laboral: eso es el '
    'Kit de Gestión de Personal y el cuadro de mando del Manual del Manager. '
    'Aquí se decide quién hace qué, con qué nivel y qué le falta.',
]


def hoja_instrucciones(wb):
    ws = wb.create_sheet('Instrucciones', 0)
    anchos(ws, {'A': 46, 'B': 46, 'C': 46})
    motor.val(ws, 'A1', TITULO)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', SUBTITULO)
    motor.val(ws, 'A3', 'Para qué sirve: decidir a quién promocionar, a quién '
                        'formar en qué y quién decide qué.')
    ws['A3'].font = Font(italic=True, size=9)

    seccion(ws, 'A5', 'Instrucciones de uso')
    fila = 6
    for paso in PASOS:
        ws.merge_cells('A%d:C%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, paso, wrap=True)
        ws.row_dimensions[fila].height = 58
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, motor.NOTA_VERDES)
    ws['A%d' % fila].fill = PatternFill('solid', fgColor=motor.VERDE)
    fila += 2

    # --- contrato entre manuales (SPEC D8) -------------------------------
    seccion(ws, 'A%d' % fila,
            'QUÉ SE COPIA DE DÓNDE Y QUÉ NO HAY QUE VOLVER A TECLEAR')
    fila += 1
    cabecera(ws, fila, [('A', 'Producto'), ('B', 'Qué aporta'),
                        ('C', 'Qué NO hay que volver a teclear')], altura=26)
    fila += 1
    for producto, aporta, no_teclear in D.CONTRATO_ENTRE_MANUALES:
        motor.val(ws, 'A%d' % fila, producto, bold=True, wrap=True)
        motor.val(ws, 'B%d' % fila, aporta, wrap=True)
        motor.val(ws, 'C%d' % fila, no_teclear, wrap=True)
        ws.row_dimensions[fila].height = 58
        fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila,
              'Es COPIA declarada, no vínculo: en todo este pack no hay ni una '
              'fórmula que apunte a otro fichero. Un enlace entre libros se '
              'rompe en cuanto alguien mueve una carpeta o renombra un '
              'fichero, y entonces el libro miente sin avisar de nada.',
              wrap=True)
    ws['A%d' % fila].font = Font(italic=True, size=9)
    ws.row_dimensions[fila].height = 40
    fila += 2

    seccion(ws, 'A%d' % fila, 'Lo que conviene saber antes de empezar')
    fila += 1
    for texto in NOTAS_LIBRO:
        ws.merge_cells('A%d:C%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, texto, wrap=True)
        ws.row_dimensions[fila].height = 58
        fila += 1
    fila += 1

    seccion(ws, 'A%d' % fila, 'Cada cuánto se usa este libro')
    fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila,
              'Cadencia: el organigrama y las fichas de puesto, AL ABRIR '
              'TEMPORADA o cuando entra o sale alguien. La rúbrica y la prueba '
              'práctica, DOS VECES AL AÑO. El plan de desarrollo individual se '
              'repasa cada mes. La matriz RACI se escribe UNA VEZ y se toca '
              'cuando cambia la estructura.', wrap=True)
    ws.row_dimensions[fila].height = 40
    fila += 2

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
# Hoja «Organigrama»
# --------------------------------------------------------------------------
O_ACTIVAS = 5
O_AREA = 6
O_PAR_SEC = 8
O_PAR_CAB = 9
O_PAR_INI = 10
O_PAR_FIN = O_PAR_INI + N_ORG_PARTIDAS - 1           # 17
O_PAR_N1 = O_PAR_FIN + 1
O_PAR_N2 = O_PAR_FIN + 2
O_BRI_SEC = O_PAR_FIN + 4                            # 21
O_BRI_CAB = O_BRI_SEC + 1                            # 22
O_BRI_INI = O_BRI_CAB + 1                            # 23
O_BRI_FIN = O_BRI_INI + N_ORG_BRIGADA - 1            # 38
O_TOT_PERS = O_BRI_FIN + 1
O_TOT_HORAS = O_BRI_FIN + 2
O_BRI_N1 = O_BRI_FIN + 4
O_BRI_N2 = O_BRI_FIN + 5
O_BRI_N3 = O_BRI_FIN + 6
O_LIST_SEC = O_BRI_N3 + 2
O_LIST_CAB = O_LIST_SEC + 1
O_LIST_INI = O_LIST_CAB + 1
O_LIST_FIN = O_LIST_INI + max(len(PARTIDAS), len(D.PUESTOS_ALEH),
                              len(SI_NO)) - 1


def hoja_organigrama(wb):
    ws = wb.create_sheet(H_ORG)
    anchos(ws, {'A': 6, 'B': 24, 'C': 13, 'D': 46, 'E': 24, 'F': 24, 'G': 12,
                'H': 17, 'I': 26, 'J': 14})
    encabezar(ws, 'Organigrama de cocina', col_fin='J',
              nota_txt='Las partidas de arriba y la brigada de abajo son la '
                       'misma cocina vista de dos maneras. Todo lo demás en '
                       'este libro se lee de aquí.')

    motor.val(ws, 'A%d' % O_ACTIVAS, 'Partidas activas (de 3 a 8)', bold=True)
    ws.merge_cells('A%d:B%d' % (O_ACTIVAS, O_ACTIVAS))
    motor.val(ws, 'C%d' % O_ACTIVAS,
              float(D.PARAMETROS_COCINA['partidas_activas']), fmt=FMT_ENT)
    motor.verde(ws, 'C%d' % O_ACTIVAS)
    ws.merge_cells('D%d:J%d' % (O_ACTIVAS, O_ACTIVAS))
    motor.val(ws, 'D%d' % O_ACTIVAS,
              'La tabla trae ocho filas fijas. Las que pases de este número se '
              'marcan «Fuera del alcance» y dejan de avisarte: una cocina de '
              'tres partidas usa este libro igual que una de ocho.', wrap=True)
    ws['D%d' % O_ACTIVAS].font = Font(italic=True, size=9)
    ws.row_dimensions[O_ACTIVAS].height = 26

    motor.val(ws, 'A%d' % O_AREA, 'Área funcional de la brigada de cocina',
              bold=True)
    ws.merge_cells('A%d:B%d' % (O_AREA, O_AREA))
    motor.val(ws, 'C%d' % O_AREA, D.AREA_COCINA)
    motor.verde(ws, 'C%d' % O_AREA)
    ws.merge_cells('D%d:J%d' % (O_AREA, O_AREA))
    motor.val(ws, 'D%d' % O_AREA,
              'El ALEH VI tipifica seis áreas funcionales y tres grupos '
              'profesionales; cocina y economato son la segunda. '
              + verificado('MM-14'), wrap=True)
    ws['D%d' % O_AREA].font = Font(italic=True, size=9)
    ws.row_dimensions[O_AREA].height = 30

    # --- las partidas ----------------------------------------------------
    seccion(ws, 'A%d' % O_PAR_SEC, 'LAS PARTIDAS DE TU COCINA')
    cabecera(ws, O_PAR_CAB,
             [('A', 'Nº'), ('B', 'Partida'), ('C', '¿Produce raciones?'),
              ('D', 'Qué produce'), ('E', 'Responsable (titular)'),
              ('F', 'Quién la cubre si falta'), ('G', 'Personas asignadas'),
              ('H', 'Alcance'), ('I', 'Aviso')], altura=44)
    v_produce, v_partida = [], []
    for i in range(N_ORG_PARTIDAS):
        r = O_PAR_INI + i
        dato = D.PARTIDAS[i] if i < len(D.PARTIDAS) else None
        motor.val(ws, 'A%d' % r, i + 1, fmt=FMT_ENT, align='center')
        motor.val(ws, 'B%d' % r, dato[0] if dato else '', wrap=True)
        motor.val(ws, 'C%d' % r,
                  (SI_NO[0] if dato[1] else SI_NO[1]) if dato else '',
                  align='center')
        motor.val(ws, 'D%d' % r, dato[2] if dato else '', wrap=True)
        motor.val(ws, 'E%d' % r, titular_de(dato[0]) if dato else '',
                  wrap=True)
        motor.val(ws, 'F%d' % r, '', wrap=True)
        motor.verde(ws, 'B%d:F%d' % (r, r))
        # El `&""` no es adorno: sin el, la celda de partida vacia deja el
        # criterio de COUNTIF a nulo y el evaluador que rellena la cache de
        # formulas (pycel) revienta -> la fila se quedaria sin valor cacheado.
        # En Excel la guarda exterior ya devuelve "" y el COUNTIF ni se
        # evalua, asi que el resultado visible es el mismo.
        motor.f(ws, 'G%d' % r,
                '=IFERROR(IF($B{r}="","",COUNTIF($H${a}:$H${b},$B{r}&"")),"")'
                .format(r=r, a=O_BRI_INI, b=O_BRI_FIN), fmt=FMT_ENT)
        motor.f(ws, 'H%d' % r,
                '=IF($B{r}="","",IF(OR(NOT(ISNUMBER($C${act})),$A{r}<=$C${act}),'
                '"Activa","Fuera del alcance"))'.format(r=r, act=O_ACTIVAS))
        motor.f(ws, 'I%d' % r,
                '=IF(OR($B{r}="",$H{r}<>"Activa"),"",'
                'IF($E{r}="","FALTA RESPONSABLE",'
                'IF(AND(ISNUMBER($G{r}),$G{r}=0),"SIN PERSONAL ASIGNADO",'
                '"Correcto")))'.format(r=r))
        ws.row_dimensions[r].height = 32
        v_produce.append('C%d' % r)
        v_partida.append('B%d' % r)
    parrafo(ws, O_PAR_N1,
            'La columna «quién la cubre si falta» se deja en blanco a '
            'propósito: quién puede sostener una partida en un servicio no se '
            'decide aquí, se mide en la matriz de polivalencia del «Manual del '
            'Manager de Restaurante». Escribe aquí el nombre que salga de allí.',
            col_fin='J', alto=32)
    parrafo(ws, O_PAR_N2,
            'Dos partidas del ejemplo no producen raciones (sala y caja): '
            'existen en el negocio y en la matriz del Manager, pero no entran '
            'en la producción ni en la merma del cuadro de mando de cocina.',
            col_fin='J', alto=26)

    # --- la brigada ------------------------------------------------------
    seccion(ws, 'A%d' % O_BRI_SEC, 'LA BRIGADA: QUIÉN ESTÁ HOY EN CADA PARTIDA')
    cabecera(ws, O_BRI_CAB,
             [('A', 'Id'), ('B', 'Nombre'), ('C', 'Grupo'),
              ('D', 'Puesto en tu organigrama'),
              ('E', 'Puesto del convenio (ALEH VI)'),
              ('F', 'Área funcional'), ('G', 'Nivel de delegación'),
              ('H', 'Partida principal'), ('I', 'Contrato y jornada'),
              ('J', 'Nivel en cocina')], altura=44)
    v_puesto_conv, v_part_princ = [], []
    for i in range(N_ORG_BRIGADA):
        r = O_BRI_INI + i
        p = D.PLANTILLA[i] if i < PLANTILLA_N else None
        pc = puesto_convenio(p[0]) if p else ''
        motor.val(ws, 'A%d' % r, p[0] if p else '')
        motor.val(ws, 'B%d' % r, p[1] if p else '')
        motor.val(ws, 'C%d' % r, p[4] if p else '', align='center')
        motor.val(ws, 'D%d' % r, p[2] if p else '', wrap=True)
        motor.val(ws, 'E%d' % r, pc, wrap=True)
        motor.val(ws, 'F%d' % r, p[3] if p else '', align='center')
        motor.val(ws, 'G%d' % r, delegacion_de(pc), wrap=True)
        motor.val(ws, 'H%d' % r, p[9] if p else '', wrap=True)
        motor.val(ws, 'I%d' % r,
                  ('%s · %d h/semana' % (p[5], p[6])) if p else '', wrap=True)
        nc = D.nivel_cocina(p[0]) if p else None
        motor.val(ws, 'J%d' % r, float(nc) if nc is not None else '',
                  fmt=FMT_ENT, align='center')
        motor.verde(ws, 'A%d:J%d' % (r, r))
        ws.row_dimensions[r].height = 30
        v_puesto_conv.append('E%d' % r)
        v_part_princ.append('H%d' % r)

    motor.val(ws, 'A%d' % O_TOT_PERS, 'Personas de la brigada de cocina',
              bold=True)
    ws.merge_cells('A%d:E%d' % (O_TOT_PERS, O_TOT_PERS))
    motor.f(ws, 'F%d' % O_TOT_PERS,
            '=IFERROR(COUNTIF($F${a}:$F${b},$C${ar}),"")'
            .format(a=O_BRI_INI, b=O_BRI_FIN, ar=O_AREA), fmt=FMT_ENT,
            bold=True)
    ws['F%d' % O_TOT_PERS].fill = PatternFill('solid', fgColor=CREMA)
    motor.val(ws, 'A%d' % O_TOT_HORAS,
              'Personas de la casa dadas de alta en esta hoja', bold=True)
    ws.merge_cells('A%d:E%d' % (O_TOT_HORAS, O_TOT_HORAS))
    motor.f(ws, 'F%d' % O_TOT_HORAS,
            '=IF(COUNT($J${a}:$J${b})=0,"",COUNT($J${a}:$J${b}))'
            .format(a=O_BRI_INI, b=O_BRI_FIN), fmt=FMT_ENT, bold=True)
    ws['F%d' % O_TOT_HORAS].fill = PatternFill('solid', fgColor=CREMA)

    parrafo(ws, O_BRI_N1,
            'La columna «nivel en cocina» es el nivel MÁXIMO de polivalencia de '
            'esa persona en las tres partidas de cocina, copiado de la matriz '
            'del «Manual del Manager de Restaurante». Está aquí para poder '
            'contrastarlo con la nota técnica de la hoja «Rúbrica de '
            'Competencias»: son dos preguntas distintas y a menudo dan '
            'respuestas distintas.', col_fin='J', alto=40)
    parrafo(ws, O_BRI_N2,
            'El puesto del convenio sólo se rellena para el área funcional de '
            'cocina y economato: quien está en sala o en administración se '
            'clasifica en otra área del mismo convenio, y sus funciones no son '
            'las del artículo 17.B.', col_fin='J', alto=32)
    parrafo(ws, O_BRI_N3,
            'Ojo con los fijos-discontinuos: en el ejemplo, una de las seis '
            'personas de cocina sólo está de campaña, así que las horas '
            'contratadas de la brigada no son las mismas en febrero que en '
            'agosto.', col_fin='J', alto=32)

    # --- listas de referencia -------------------------------------------
    seccion(ws, 'A%d' % O_LIST_SEC,
            'LISTAS DE REFERENCIA DE LOS DESPLEGABLES (fuera del área de '
            'impresión)')
    cabecera(ws, O_LIST_CAB, [('A', 'Sí / No'), ('B', 'Partidas'),
                              ('C', 'Puestos del convenio')], altura=20)
    for i in range(O_LIST_FIN - O_LIST_INI + 1):
        r = O_LIST_INI + i
        if i < len(SI_NO):
            motor.val(ws, 'A%d' % r, SI_NO[i])
        if i < len(PARTIDAS):
            motor.val(ws, 'B%d' % r, PARTIDAS[i])
        if i < len(D.PUESTOS_ALEH):
            motor.val(ws, 'C%d' % r, D.PUESTOS_ALEH[i][0])
    dv_rango(ws, v_produce,
             "'%s'!$A$%d:$A$%d" % (H_ORG, O_LIST_INI,
                                   O_LIST_INI + len(SI_NO) - 1),
             'Sí o No', 'Marca Sí si esa partida produce raciones de comida.')
    dv_rango(ws, v_part_princ,
             "'%s'!$B$%d:$B$%d" % (H_ORG, O_LIST_INI,
                                   O_LIST_INI + len(PARTIDAS) - 1),
             'Partida', 'Elige una de las partidas declaradas arriba.')
    dv_rango(ws, v_puesto_conv,
             "'%s'!$C$%d:$C$%d" % (H_ORG, O_LIST_INI,
                                   O_LIST_INI + len(D.PUESTOS_ALEH) - 1),
             'Puesto del convenio',
             'Elige uno de los diez puestos del área de cocina y economato del '
             'ALEH VI. Déjalo vacío para el personal de otra área.')
    motor.dv_numerica(ws, ['C%d' % O_ACTIVAS], minimo=3, maximo=8,
                      titulo='Partidas activas',
                      mensaje='Escribe cuántas partidas tiene tu cocina, de 3 '
                              'a 8.')
    motor.dv_numerica(ws, ['J%d' % r for r in range(O_BRI_INI, O_BRI_FIN + 1)],
                      minimo=0, maximo=3, titulo='Nivel de polivalencia',
                      mensaje='De 0 a 3, copiado de la matriz de polivalencia '
                              'del Manual del Manager.')
    motor.semaforo_texto(ws, 'I%d:I%d' % (O_PAR_INI, O_PAR_FIN),
                         (('Correcto', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                          ('FALTA RESPONSABLE', motor.CF_ROJO_BG,
                           motor.CF_ROJO_FG),
                          ('SIN PERSONAL ASIGNADO', motor.CF_ROJO_BG,
                           motor.CF_ROJO_FG)))
    motor.semaforo_texto(ws, 'H%d:H%d' % (O_PAR_INI, O_PAR_FIN),
                         (('Fuera del alcance', motor.CF_GRIS_BG,
                           motor.CF_GRIS_FG),))
    ws.freeze_panes = 'B10'
    pagina(ws, titulos='$%d:$%d' % (O_PAR_CAB, O_PAR_CAB),
           area='A1:J%d' % O_BRI_N3)
    return ws


# --------------------------------------------------------------------------
# Hoja «Fichas de Puesto»
# --------------------------------------------------------------------------
P_CAB = 5
P_INI = 6
P_FIN = P_INI + len(D.PUESTOS_ALEH) - 1
P_TOT = P_FIN + 1
P_N1 = P_TOT + 2
P_N2 = P_TOT + 3
#: B4 de la refutación xlsx (2026-09-06): la columna A no es la lista literal
#: del art. 15, es una denominación de trabajo basada en las funciones.
P_N3 = P_TOT + 4
P_DEL_SEC = P_TOT + 5
P_DEL_CAB = P_DEL_SEC + 1
P_DEL_INI = P_DEL_CAB + 1
P_DEL_FIN = P_DEL_INI + len(D.NIVELES_DELEGACION) - 1
P_USO_SEC = P_DEL_FIN + 2
P_USO_CAB = P_USO_SEC + 1
P_USO_INI = P_USO_CAB + 1
P_USO_FIN = P_USO_INI + len(D.DENOMINACIONES_USO) - 1
P_USO_N = P_USO_FIN + 1
P_FOR_SEC = P_USO_N + 2
P_FOR_1 = P_FOR_SEC + 1
P_FOR_2 = P_FOR_SEC + 2
P_PIE = P_FOR_2 + 2


def hoja_puestos(wb):
    ws = wb.create_sheet(H_PUESTOS)
    anchos(ws, {'A': 26, 'B': 12, 'C': 78, 'D': 46, 'E': 26, 'F': 20,
                'G': 12})
    encabezar(ws, 'Fichas de puesto de cocina', col_fin='G',
              nota_txt='La columna de funciones del convenio es LITERAL: es lo '
                       'que pone el ALEH VI. Lo que escribes tú es la columna '
                       'verde de al lado.')
    cabecera(ws, P_CAB,
             [('A', 'Puesto (denominación del art. 17.B)'), ('B', 'Grupo'),
              ('C', 'Funciones del convenio (literal, art. 17.B)'),
              ('D', 'Funciones propias de tu casa'),
              ('E', 'Nivel de delegación'), ('F', 'Quién lo ocupa hoy'),
              ('G', 'Personas')], altura=44)
    for i, (puesto, grupo, funciones, nivel, ocupantes) in enumerate(
            D.PUESTOS_ALEH):
        r = P_INI + i
        motor.val(ws, 'A%d' % r, puesto, bold=True, wrap=True)
        motor.val(ws, 'B%d' % r, grupo, align='center')
        motor.val(ws, 'C%d' % r, funciones, wrap=True)
        motor.val(ws, 'D%d' % r, '', wrap=True)
        motor.verde(ws, 'D%d' % r)
        motor.val(ws, 'E%d' % r, nivel, wrap=True)
        motor.val(ws, 'F%d' % r, ocupantes, wrap=True)
        motor.verde(ws, 'F%d' % r)
        motor.f(ws, 'G%d' % r,
                '=IFERROR(COUNTIF(\'{h}\'!$E${a}:$E${b},$A{r}),"")'
                .format(h=H_ORG, a=O_BRI_INI, b=O_BRI_FIN, r=r), fmt=FMT_ENT)
        ws.row_dimensions[r].height = 96
    motor.val(ws, 'A%d' % P_TOT, 'TOTAL de personas encuadradas', bold=True)
    motor.f(ws, 'G%d' % P_TOT,
            '=IF(COUNT($G${a}:$G${b})=0,"",SUM($G${a}:$G${b}))'
            .format(a=P_INI, b=P_FIN), fmt=FMT_ENT, bold=True)
    ws['G%d' % P_TOT].fill = PatternFill('solid', fgColor=CREMA)

    parrafo(ws, P_N1, D.FUENTE_ALEH_ART17, col_fin='G', alto=26)
    parrafo(ws, P_N2,
            'La columna «Personas» cuenta cuántas filas de la hoja '
            '«Organigrama» tienen ese puesto del convenio. Si el total no '
            'cuadra con tu plantilla de cocina, es que alguien está sin '
            'encuadrar: el grupo profesional y la ocupación tienen que constar '
            'en el contrato y en el recibo de salario. ' + verificado('MM-14'),
            col_fin='G', alto=40)
    parrafo(ws, P_N3,
            'La columna A es una denominación de TRABAJO, no la lista '
            'literal del art. 15: la Resolución de 25-08-2026 solo cambió el '
            'nombre de 5 de los 10 puestos (invirtiendo el orden de género) '
            'y dejó los otros cuatro como en 2023, y el propio BOE es '
            'incoherente con «Ayudante/a economato» (sin cambiar en el art. '
            '15, «Ayudanta/e economato» en los arts. 16 y 17). Lo literal es '
            'la columna C.',
            col_fin='G', alto=44)

    seccion(ws, 'A%d' % P_DEL_SEC,
            'LOS TRES NIVELES DE DELEGACIÓN QUE YA ESTÁN EN EL CONVENIO')
    cabecera(ws, P_DEL_CAB,
             [('A', 'Nivel'), ('C', 'Puestos'),
              ('E', 'Cómo se manda en ese nivel')], altura=26)
    ws.merge_cells('A%d:B%d' % (P_DEL_CAB, P_DEL_CAB))
    ws.merge_cells('C%d:D%d' % (P_DEL_CAB, P_DEL_CAB))
    ws.merge_cells('E%d:G%d' % (P_DEL_CAB, P_DEL_CAB))
    pintar_cabecera(ws, 'A%d:G%d' % (P_DEL_CAB, P_DEL_CAB))
    for i, (nivel, puestos, como) in enumerate(D.NIVELES_DELEGACION):
        r = P_DEL_INI + i
        ws.merge_cells('A%d:B%d' % (r, r))
        motor.val(ws, 'A%d' % r, nivel, bold=True, wrap=True)
        ws.merge_cells('C%d:D%d' % (r, r))
        motor.val(ws, 'C%d' % r, puestos, wrap=True)
        ws.merge_cells('E%d:G%d' % (r, r))
        motor.val(ws, 'E%d' % r, como, wrap=True)
        ws.row_dimensions[r].height = 40

    seccion(ws, 'A%d' % P_USO_SEC,
            'DENOMINACIONES DE USO Y SU EQUIVALENCIA EN EL CONVENIO')
    cabecera(ws, P_USO_CAB,
             [('A', 'Denominación de uso'), ('B', '¿Está en el ALEH VI?'),
              ('C', 'Puesto equivalente por las funciones que hace')],
             altura=26)
    ws.merge_cells('C%d:G%d' % (P_USO_CAB, P_USO_CAB))
    pintar_cabecera(ws, 'C%d:G%d' % (P_USO_CAB, P_USO_CAB))
    for i, (denom, esta, equivalente) in enumerate(D.DENOMINACIONES_USO):
        r = P_USO_INI + i
        motor.val(ws, 'A%d' % r, denom, bold=True)
        motor.val(ws, 'B%d' % r, SI_NO[0] if esta else SI_NO[1],
                  align='center')
        ws.merge_cells('C%d:G%d' % (r, r))
        motor.val(ws, 'C%d' % r, equivalente, wrap=True)
        ws.row_dimensions[r].height = 32
    parrafo(ws, P_USO_N,
            'Esto no es una discusión de nombres: el grupo profesional decide '
            'el salario del convenio, el periodo de prueba y la clasificación '
            'que consta en el contrato. Llamarse «chef ejecutivo» no cambia '
            'ninguna de las tres.', col_fin='G', alto=26)

    seccion(ws, 'A%d' % P_FOR_SEC, 'FORMACIÓN: LO QUE OBLIGA, POR PUESTO')
    parrafo(ws, P_FOR_1,
            'La formación en higiene se da de acuerdo con la actividad laboral '
            'de CADA PUESTO, no de forma genérica para toda la casa. '
            + verificado('CE-04'), col_fin='G', alto=26)
    parrafo(ws, P_FOR_2,
            'Y la formación en prevención es teórica y práctica, suficiente y '
            'adecuada al puesto, dentro de la jornada, y su coste no puede '
            'recaer nunca sobre el trabajador. ' + verificado('CE-27'),
            col_fin='G', alto=26)

    motor.val(ws, 'A%d' % P_PIE, D.VERSION_LINE)
    ws['A%d' % P_PIE].font = Font(size=8, italic=True)
    ws.freeze_panes = 'A6'
    pagina(ws, titulos='$%d:$%d' % (P_CAB, P_CAB), area='A1:G%d' % P_PIE)
    return ws


# --------------------------------------------------------------------------
# Hoja «Matriz RACI»
# --------------------------------------------------------------------------
COLS_RACI = [get_column_letter(2 + i) for i in range(len(D.ROLES_RACI))]  # B..G
C_NA, C_NR, C_CHK = 'H', 'I', 'J'

R_LEY_CAB = 5
R_LEY_INI = 6
R_LEY_FIN = R_LEY_INI + len(LETRAS_RACI) - 1         # 9
R_CAB = 12
R_INI = 13
R_FIN = R_INI + N_RACI - 1                           # 32
R_N1 = R_FIN + 2
R_N2 = R_FIN + 3
R_N3 = R_FIN + 4
R_PIE = R_FIN + 6


def hoja_raci(wb):
    ws = wb.create_sheet(H_RACI)
    anchos(ws, dict([('A', 66)] + [(c, 14) for c in COLS_RACI]
                    + [(C_NA, 10), (C_NR, 10), (C_CHK, 24)]))
    encabezar(ws, 'Matriz RACI: cocina, sala y dirección', col_fin=C_CHK,
              nota_txt='Quince decisiones que cruzan los tres. La hoja no '
                       'opina sobre quién debe decidir: comprueba que alguien '
                       'lo haga, y sólo uno.')

    cabecera(ws, R_LEY_CAB, [('A', 'Letra'), ('B', 'Qué quiere decir')],
             altura=20)
    ws.merge_cells('B%d:%s%d' % (R_LEY_CAB, C_CHK, R_LEY_CAB))
    pintar_cabecera(ws, 'B%d:%s%d' % (R_LEY_CAB, C_CHK, R_LEY_CAB))
    for i, (letra, glosa) in enumerate(LETRAS_RACI):
        r = R_LEY_INI + i
        motor.val(ws, 'A%d' % r, letra, bold=True, align='center')
        ws.merge_cells('B%d:%s%d' % (r, C_CHK, r))
        motor.val(ws, 'B%d' % r, glosa, wrap=True)
        ws.row_dimensions[r].height = 20

    cabecera(ws, R_CAB,
             [('A', 'Decisión')] + list(zip(COLS_RACI, D.ROLES_RACI))
             + [(C_NA, 'Nº de A'), (C_NR, 'Nº de R'),
                (C_CHK, 'Comprobación')], altura=44)
    verdes = []
    for i in range(N_RACI):
        r = R_INI + i
        dato = D.RACI[i] if i < len(D.RACI) else None
        motor.val(ws, 'A%d' % r, dato[0] if dato else '', wrap=True)
        motor.verde(ws, 'A%d' % r)
        for j, col in enumerate(COLS_RACI):
            motor.val(ws, '%s%d' % (col, r), dato[1][j] if dato else '',
                      align='center')
            motor.verde(ws, '%s%d' % (col, r))
            verdes.append('%s%d' % (col, r))
        motor.f(ws, '%s%d' % (C_NA, r),
                '=IFERROR(IF($A{r}="","",COUNTIF(${c0}{r}:${c1}{r},$A${la})),"")'
                .format(r=r, c0=COLS_RACI[0], c1=COLS_RACI[-1],
                        la=R_LEY_INI + 1), fmt=FMT_ENT)
        motor.f(ws, '%s%d' % (C_NR, r),
                '=IFERROR(IF($A{r}="","",COUNTIF(${c0}{r}:${c1}{r},$A${lr})),"")'
                .format(r=r, c0=COLS_RACI[0], c1=COLS_RACI[-1],
                        lr=R_LEY_INI), fmt=FMT_ENT)
        motor.f(ws, '%s%d' % (C_CHK, r),
                '=IF($A{r}="","",IF(${na}{r}=0,"Falta la A",'
                'IF(${na}{r}>1,"Más de una A",'
                'IF(${nr}{r}=0,"Falta la R","Correcta"))))'
                .format(r=r, na=C_NA, nr=C_NR))
        ws.row_dimensions[r].height = 30

    dv_rango(ws, verdes,
             "'%s'!$A$%d:$A$%d" % (H_RACI, R_LEY_INI, R_LEY_FIN),
             'Letra RACI',
             'Escribe R, A, C o I. Deja la celda vacía si ese rol no '
             'interviene en la decisión.')
    motor.semaforo_texto(ws, '%s%d:%s%d' % (C_CHK, R_INI, C_CHK, R_FIN),
                         (('Correcta', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                          ('Falta la A', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('Más de una A', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('Falta la R', motor.CF_AMBAR_BG,
                           motor.CF_AMBAR_FG)))

    parrafo(ws, R_N1,
            'Una sola A por decisión. Dos personas que responden de lo mismo es '
            'la forma más fiable de que un plato se retire de la carta dos '
            'veces y ninguna, y de que la incidencia de un alérgeno se quede '
            'esperando a que la coja alguien.', col_fin=C_CHK, alto=30)
    parrafo(ws, R_N2,
            'Esta matriz dice QUIÉN decide. Cómo se lleva una discusión entre '
            'cocina y sala sin que acabe en el pase está en el capítulo 18 del '
            '«Manual del Manager de Restaurante»; y cómo se lleva una propuesta '
            'al gerente con la cifra de la semana delante, en el capítulo 19 de '
            'este manual.', col_fin=C_CHK, alto=32)
    parrafo(ws, R_N3,
            'Las filas son un punto de partida, no un dogma: en una casa con '
            'propiedad presente, el PVP puede ser A de propiedad; en un grupo '
            'con dirección de operaciones, no. Cámbialas. Lo que no se cambia '
            'es la regla de la A única.', col_fin=C_CHK, alto=30)

    motor.val(ws, 'A%d' % R_PIE, D.VERSION_LINE)
    ws['A%d' % R_PIE].font = Font(size=8, italic=True)
    ws.freeze_panes = 'B13'
    pagina(ws, titulos='$%d:$%d' % (R_CAB, R_CAB), area='A1:%s%d' % (C_CHK,
                                                                     R_PIE))
    return ws


# --------------------------------------------------------------------------
# Hoja «Rúbrica de Competencias»
# --------------------------------------------------------------------------
N_COMP = len(D.COMPETENCIAS_TECNICAS)
U_DESC_CAB = 5
U_DESC_INI = 6
U_DESC_FIN = U_DESC_INI + N_COMP - 1                 # 12
U_PES_SEC = U_DESC_FIN + 2                           # 14
U_PES_CAB = U_PES_SEC + 1                            # 15
U_PES_INI = U_PES_CAB + 1                            # 16
U_PES_FIN = U_PES_INI + len(D.PESOS_COMPETENCIA_PUESTO)  # +1 fila «no evaluado»
U_PES_N = U_PES_FIN + 1
U_BAN_SEC = U_PES_N + 2
U_BAN_CAB = U_BAN_SEC + 1
U_BAN_INI = U_BAN_CAB + 1
U_BAN_FIN = U_BAN_INI + len(D.BANDAS_NIVEL_COMPETENCIA) - 1
U_EV_SEC = U_BAN_FIN + 2
U_EV_CAB = U_EV_SEC + 1
U_EV_INI = U_EV_CAB + 1
U_EV_FIN = U_EV_INI + PLANTILLA_N - 1
U_EV_RES = U_EV_FIN + 1
U_EV_MED = U_EV_FIN + 2
U_N1 = U_EV_MED + 2
U_N2 = U_EV_MED + 3
U_N3 = U_EV_MED + 4
U_LEC_CAB = U_N3 + 2
U_LEC_INI = U_LEC_CAB + 1
U_LEC_FIN = U_LEC_INI + len(LECTURAS) - 1
U_PIE = U_LEC_FIN + 2

# columnas de la tabla de evaluación
E_ID, E_NOM, E_PUE, E_FEC, E_EVA = 'A', 'B', 'C', 'D', 'E'
E_C0 = 6                                   # F = primera competencia
E_COMP = [get_column_letter(E_C0 + i) for i in range(N_COMP)]     # F..L
E_MED = get_column_letter(E_C0 + N_COMP)                          # M
E_NIV = get_column_letter(E_C0 + N_COMP + 1)                      # N
E_POL = get_column_letter(E_C0 + N_COMP + 2)                      # O
E_LEC = get_column_letter(E_C0 + N_COMP + 3)                      # P
# bloque de cálculo, a la derecha y separado
E_W0 = E_C0 + N_COMP + 5                                          # R
E_PESO = [get_column_letter(E_W0 + i) for i in range(N_COMP)]      # R..X
E_PTS = [get_column_letter(E_W0 + N_COMP + i) for i in range(N_COMP)]  # Y..AE
# columnas de pesos por puesto (bloque 2)
W_COMP = [get_column_letter(2 + i) for i in range(N_COMP)]         # B..H


def hoja_rubrica(wb):
    ws = wb.create_sheet(H_RUBRICA)
    anchos(ws, dict([('A', 30), ('B', 30), ('C', 26), ('D', 13), ('E', 13)]
                    + [(c, 8) for c in E_COMP]
                    + [(E_MED, 11), (E_NIV, 10), (E_POL, 10), (E_LEC, 30)]
                    + [(c, 9) for c in E_PESO] + [(c, 9) for c in E_PTS]))
    encabezar(ws, 'Rúbrica de competencias técnicas', col_fin=E_LEC,
              nota_txt='Siete competencias, cinco niveles descritos y pesos '
                       'por puesto. Se puntúa por prueba práctica; lo que no '
                       'aplica se deja en blanco y sale de la media.')

    # --- descriptores -----------------------------------------------------
    cabecera(ws, U_DESC_CAB,
             [('A', 'Competencia')] + [(get_column_letter(2 + i),
                                        'Nivel %d' % (i + 1))
                                       for i in range(5)], altura=22)
    for i, (comp, niveles) in enumerate(D.COMPETENCIAS_TECNICAS):
        r = U_DESC_INI + i
        motor.val(ws, 'A%d' % r, comp, bold=True, wrap=True)
        for j, texto in enumerate(niveles):
            motor.val(ws, '%s%d' % (get_column_letter(2 + j), r), texto,
                      wrap=True)
        ws.row_dimensions[r].height = 46
    for j in range(5):
        ws.column_dimensions[get_column_letter(2 + j)].width = 34

    # --- pesos por puesto -------------------------------------------------
    seccion(ws, 'A%d' % U_PES_SEC, 'PESO DE CADA COMPETENCIA POR PUESTO (0 a 3)')
    cabecera(ws, U_PES_CAB,
             [('A', 'Puesto')] + [(W_COMP[i], D.COMPETENCIAS_TECNICAS[i][0])
                                  for i in range(N_COMP)], altura=58)
    for i, (puesto, pesos) in enumerate(D.PESOS_COMPETENCIA_PUESTO):
        r = U_PES_INI + i
        motor.val(ws, 'A%d' % r, puesto, bold=True, wrap=True)
        for j, peso in enumerate(pesos):
            motor.val(ws, '%s%d' % (W_COMP[j], r), float(peso), fmt=FMT_ENT,
                      align='center')
            motor.verde(ws, '%s%d' % (W_COMP[j], r))
        ws.row_dimensions[r].height = 26
    motor.val(ws, 'A%d' % U_PES_FIN, NO_EVALUADO, bold=True, wrap=True)
    ws.row_dimensions[U_PES_FIN].height = 26
    parrafo(ws, U_PES_N,
            'Un peso 0 quiere decir que esa competencia no cuenta para ese '
            'puesto y sale de la media. La última fila no tiene pesos a '
            'propósito: es la que se elige para quien no pisa cocina, y deja '
            'toda su evaluación en blanco.', col_fin=E_LEC, alto=30)

    # --- bandas -----------------------------------------------------------
    seccion(ws, 'A%d' % U_BAN_SEC,
            'BANDAS: DE LA MEDIA PONDERADA AL NIVEL TÉCNICO')
    cabecera(ws, U_BAN_CAB, [('A', 'Nivel técnico'), ('B', 'Media desde'),
                             ('C', 'Media hasta')], altura=20)
    for i, nivel in enumerate(sorted(D.BANDAS_NIVEL_COMPETENCIA, reverse=True)):
        r = U_BAN_INI + i
        minimo, maximo = D.BANDAS_NIVEL_COMPETENCIA[nivel]
        motor.val(ws, 'A%d' % r, float(nivel), fmt=FMT_ENT, align='center')
        motor.val(ws, 'B%d' % r, float(minimo), fmt=FMT_DEC)
        motor.val(ws, 'C%d' % r, float(maximo), fmt=FMT_DEC)
        motor.verde(ws, 'B%d:C%d' % (r, r))

    # --- evaluación -------------------------------------------------------
    seccion(ws, 'A%d' % U_EV_SEC, 'EVALUACIÓN TÉCNICA DE LA BRIGADA')
    cabecera(ws, U_EV_CAB,
             [(E_ID, 'Id'), (E_NOM, 'Nombre'), (E_PUE, 'Puesto de la rúbrica'),
              (E_FEC, 'Fecha'), (E_EVA, 'Evaluador')]
             + [(E_COMP[i], D.COMPETENCIAS_TECNICAS[i][0])
                for i in range(N_COMP)]
             + [(E_MED, 'Media ponderada'), (E_NIV, 'Nivel técnico'),
                (E_POL, 'Nivel en cocina'), (E_LEC, 'Lectura')], altura=76)
    cabecera(ws, U_EV_CAB,
             [(E_PESO[i], 'Peso aplicado ' + str(i + 1))
              for i in range(N_COMP)]
             + [(E_PTS[i], 'Puntos ' + str(i + 1)) for i in range(N_COMP)],
             altura=76)
    nombres = dict((p[0], p[1]) for p in D.PLANTILLA)
    v_puesto, v_fecha, v_punt = [], [], []
    for i, (pid, puesto, fecha, evaluador, punt) in enumerate(D.EVALUACIONES):
        r = U_EV_INI + i
        motor.val(ws, '%s%d' % (E_ID, r), pid)
        motor.val(ws, '%s%d' % (E_NOM, r), nombres.get(pid, ''))
        motor.val(ws, '%s%d' % (E_PUE, r), puesto, wrap=True)
        motor.val(ws, '%s%d' % (E_FEC, r),
                  D._fecha(fecha) if fecha else '', fmt=FMT_FECHA)
        motor.val(ws, '%s%d' % (E_EVA, r), evaluador, align='center')
        motor.verde(ws, '%s%d:%s%d' % (E_ID, r, E_EVA, r))
        v_puesto.append('%s%d' % (E_PUE, r))
        v_fecha.append('%s%d' % (E_FEC, r))
        for j in range(N_COMP):
            coord = '%s%d' % (E_COMP[j], r)
            motor.val(ws, coord, float(punt[j]) if punt[j] is not None else '',
                      fmt=FMT_ENT, align='center')
            motor.verde(ws, coord)
            v_punt.append(coord)
            # peso aplicado: vacío cuando la competencia va en blanco (N/A)
            motor.f(ws, '%s%d' % (E_PESO[j], r),
                    '=IFERROR(IF(NOT(ISNUMBER(${c}{r})),"",'
                    'INDEX(${w0}${pi}:${w1}${pf},'
                    'MATCH(${pu}{r},$A${pi}:$A${pf},0),{idx})),"")'
                    .format(c=E_COMP[j], r=r, w0=W_COMP[0], w1=W_COMP[-1],
                            pi=U_PES_INI, pf=U_PES_FIN, pu=E_PUE,
                            idx=j + 1), fmt=FMT_ENT)
            motor.f(ws, '%s%d' % (E_PTS[j], r),
                    '=IFERROR(IF(NOT(ISNUMBER(${p}{r})),"",${c}{r}*${p}{r}),"")'
                    .format(p=E_PESO[j], c=E_COMP[j], r=r), fmt=FMT_ENT)
        motor.f(ws, '%s%d' % (E_MED, r),
                '=IFERROR(IF(SUM(${w0}{r}:${w1}{r})=0,"",'
                'SUM(${t0}{r}:${t1}{r})/SUM(${w0}{r}:${w1}{r})),"")'
                .format(r=r, w0=E_PESO[0], w1=E_PESO[-1], t0=E_PTS[0],
                        t1=E_PTS[-1]), fmt=FMT_DEC)
        motor.f(ws, '%s%d' % (E_NIV, r),
                '=IF(NOT(ISNUMBER(${m}{r})),"",'
                'IF(${m}{r}>=$B${b3},$A${b3},'
                'IF(${m}{r}>=$B${b2},$A${b2},'
                'IF(${m}{r}>=$B${b1},$A${b1},""))))'
                .format(m=E_MED, r=r, b3=U_BAN_INI, b2=U_BAN_INI + 1,
                        b1=U_BAN_INI + 2), fmt=FMT_ENT)
        nc = D.nivel_cocina(pid)
        motor.val(ws, '%s%d' % (E_POL, r),
                  float(nc) if nc is not None else '', fmt=FMT_ENT,
                  align='center')
        motor.verde(ws, '%s%d' % (E_POL, r))
        motor.f(ws, '%s%d' % (E_LEC, r),
                '=IF(OR(NOT(ISNUMBER(${n}{r})),NOT(ISNUMBER(${p}{r}))),"",'
                'IF(${n}{r}>${p}{r},$A${l3},'
                'IF(${n}{r}=${p}{r},$A${l1},$A${l2})))'
                .format(n=E_NIV, p=E_POL, r=r, l1=U_LEC_INI,
                        l2=U_LEC_INI + 1, l3=U_LEC_INI + 2))
        ws.row_dimensions[r].height = 22

    motor.val(ws, '%s%d' % (E_ID, U_EV_RES), 'Personas evaluadas', bold=True)
    ws.merge_cells('%s%d:%s%d' % (E_ID, U_EV_RES, E_EVA, U_EV_RES))
    motor.f(ws, '%s%d' % (E_MED, U_EV_RES),
            '=IF(COUNT(${m}${a}:${m}${b})=0,"",COUNT(${m}${a}:${m}${b}))'
            .format(m=E_MED, a=U_EV_INI, b=U_EV_FIN), fmt=FMT_ENT, bold=True)
    ws['%s%d' % (E_MED, U_EV_RES)].fill = PatternFill('solid', fgColor=CREMA)
    motor.val(ws, '%s%d' % (E_ID, U_EV_MED),
              'Media ponderada de la brigada evaluada', bold=True)
    ws.merge_cells('%s%d:%s%d' % (E_ID, U_EV_MED, E_EVA, U_EV_MED))
    motor.f(ws, '%s%d' % (E_MED, U_EV_MED),
            '=IFERROR(IF(COUNT(${m}${a}:${m}${b})=0,"",'
            'AVERAGE(${m}${a}:${m}${b})),"")'
            .format(m=E_MED, a=U_EV_INI, b=U_EV_FIN), fmt=FMT_DEC, bold=True)
    ws['%s%d' % (E_MED, U_EV_MED)].fill = PatternFill('solid', fgColor=CREMA)

    parrafo(ws, U_N1,
            'Las columnas de la derecha («peso aplicado» y «puntos») son el '
            'cálculo a la vista: el peso sólo entra cuando la competencia se ha '
            'puntuado, y la media es la división de las dos sumas. Están ahí '
            'para que una nota se pueda explicar delante de quien la recibe, no '
            'para tocarlas.', col_fin=E_LEC, alto=32)
    parrafo(ws, U_N2,
            'La columna «nivel en cocina» es una COPIA de la matriz de '
            'polivalencia del «Manual del Manager de Restaurante» (nivel máximo '
            'en las tres partidas de cocina). La matriz completa vive allí y no '
            'se duplica aquí.',
            col_fin=E_LEC, alto=32)
    parrafo(ws, U_N3,
            'Y ésa es la lectura del capítulo 18: cobertura no es competencia. '
            'Que alguien pueda sostener una partida en un servicio no quiere '
            'decir que la domine, y al revés: la mejor técnica de la casa puede '
            'estar cubriendo una sola partida.', col_fin=E_LEC, alto=30)

    cabecera(ws, U_LEC_CAB, [('A', 'Lectura'), ('B', 'Qué quiere decir')],
             altura=20)
    glosas = (
        'El nivel técnico y el de cobertura coinciden.',
        'Sostiene la partida en un servicio con más soltura de la que le da la '
        'prueba técnica: mírale la nota antes de darle una partida nueva.',
        'Tiene más nivel técnico del que la matriz le reconoce en cobertura: es '
        'un candidato a ampliar partida, y probablemente a promocionar.')
    for i, lectura in enumerate(LECTURAS):
        r = U_LEC_INI + i
        motor.val(ws, 'A%d' % r, lectura, bold=True, wrap=True)
        ws.merge_cells('B%d:%s%d' % (r, E_LEC, r))
        motor.val(ws, 'B%d' % r, glosas[i], wrap=True)
        ws.row_dimensions[r].height = 26

    motor.val(ws, 'A%d' % U_PIE, D.VERSION_LINE)
    ws['A%d' % U_PIE].font = Font(size=8, italic=True)

    dv_rango(ws, v_puesto,
             "'%s'!$A$%d:$A$%d" % (H_RUBRICA, U_PES_INI, U_PES_FIN),
             'Puesto de la rúbrica',
             'Elige el puesto por el que se le evalúa (el que hace en la '
             'partida, no el del contrato).')
    motor.dv_numerica(ws, v_punt, minimo=1, maximo=5, titulo='Puntuación',
                      mensaje='Puntúa de 1 a 5 con la prueba práctica '
                              'delante. Deja la celda vacía si la competencia '
                              'no aplica: en blanco no es un cero.')
    motor.dv_numerica(ws, ['%s%d' % (E_POL, r)
                           for r in range(U_EV_INI, U_EV_FIN + 1)],
                      minimo=0, maximo=3, titulo='Nivel de polivalencia',
                      mensaje='De 0 a 3, copiado de la matriz de polivalencia '
                              'del Manual del Manager.')
    motor.dv_numerica(ws, ['%s%d' % (c, r) for c in W_COMP
                           for r in range(U_PES_INI, U_PES_FIN)],
                      minimo=0, maximo=3, titulo='Peso',
                      mensaje='De 0 a 3. Un 0 saca la competencia de la media '
                              'de ese puesto.')
    motor.dv_numerica(ws, ['%s%d' % (c, r) for c in 'BC'
                           for r in range(U_BAN_INI, U_BAN_FIN + 1)],
                      minimo=0, maximo=5, titulo='Media',
                      mensaje='La media va de 1 a 5.')
    motor.dv_fecha(ws, v_fecha)
    motor.semaforo_texto(
        ws, '%s%d:%s%d' % (E_LEC, U_EV_INI, E_LEC, U_EV_FIN),
        ((LECTURAS[0], motor.CF_VERDE_BG, motor.CF_VERDE_FG),
         (LECTURAS[1], motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
         (LECTURAS[2], motor.CF_GRIS_BG, motor.CF_GRIS_FG)))
    ws.freeze_panes = 'B%d' % U_EV_INI
    pagina(ws, titulos='$%d:$%d' % (U_EV_CAB, U_EV_CAB),
           area='A1:%s%d' % (E_LEC, U_PIE))
    return ws


# --------------------------------------------------------------------------
# Hoja «Prueba Práctica»
# --------------------------------------------------------------------------
B_PERS = 5
B_FECHA = 6
B_EVAL = 7
B_CAB = 10
B_INI = 11
B_FIN = B_INI + len(D.PRUEBA_PRACTICA) - 1
B_TOT = B_FIN + 1
B_MED = B_FIN + 2
B_N1 = B_MED + 2
B_N2 = B_MED + 3
B_PIE = B_N2 + 2


def hoja_prueba(wb):
    ws = wb.create_sheet(H_PRUEBA)
    anchos(ws, {'A': 30, 'B': 54, 'C': 11, 'D': 32, 'E': 46, 'F': 46,
                'G': 12, 'H': 34})
    encabezar(ws, 'Prueba práctica de competencias', col_fin='H',
              nota_txt='El guion de la prueba: una por competencia, con lo que '
                       'es un 5 y lo que es un 1. Sin esto, la rúbrica es una '
                       'opinión.')
    motor.val(ws, 'A%d' % B_PERS, 'Persona evaluada', bold=True)
    motor.val(ws, 'B%d' % B_PERS, '')
    motor.verde(ws, 'B%d' % B_PERS)
    motor.val(ws, 'A%d' % B_FECHA, 'Fecha de la prueba', bold=True)
    motor.val(ws, 'B%d' % B_FECHA, '', fmt=FMT_FECHA)
    motor.verde(ws, 'B%d' % B_FECHA)
    motor.val(ws, 'A%d' % B_EVAL, 'Evaluador', bold=True)
    motor.val(ws, 'B%d' % B_EVAL, '')
    motor.verde(ws, 'B%d' % B_EVAL)
    nota(ws, B_PERS, 'Imprime una copia por persona: la prueba se apunta '
                     'mientras se hace, no después.', col='D', wrap=True)

    cabecera(ws, B_CAB,
             [('A', 'Competencia'), ('B', 'Prueba'), ('C', 'Minutos'),
              ('D', 'Material'), ('E', 'Qué es un 5'), ('F', 'Qué es un 1'),
              ('G', 'Puntuación'), ('H', 'Observaciones')], altura=32)
    v_punt = []
    for i, (comp, prueba, minutos, material, cinco, uno) in enumerate(
            D.PRUEBA_PRACTICA):
        r = B_INI + i
        motor.val(ws, 'A%d' % r, comp, bold=True, wrap=True)
        motor.val(ws, 'B%d' % r, prueba, wrap=True)
        motor.val(ws, 'C%d' % r, float(minutos), fmt=FMT_ENT, align='center')
        motor.val(ws, 'D%d' % r, material, wrap=True)
        motor.val(ws, 'E%d' % r, cinco, wrap=True)
        motor.val(ws, 'F%d' % r, uno, wrap=True)
        motor.val(ws, 'G%d' % r, '', fmt=FMT_ENT, align='center')
        motor.verde(ws, 'G%d' % r)
        motor.val(ws, 'H%d' % r, '', wrap=True)
        motor.verde(ws, 'H%d' % r)
        ws.row_dimensions[r].height = 58
        v_punt.append('G%d' % r)
    motor.val(ws, 'A%d' % B_TOT, 'Duración total de la prueba (minutos)',
              bold=True)
    motor.f(ws, 'C%d' % B_TOT,
            '=IF(COUNT($C${a}:$C${b})=0,"",SUM($C${a}:$C${b}))'
            .format(a=B_INI, b=B_FIN), fmt=FMT_ENT, bold=True)
    ws['C%d' % B_TOT].fill = PatternFill('solid', fgColor=CREMA)
    motor.val(ws, 'A%d' % B_MED, 'Media SIMPLE de la prueba (sin pesos)',
              bold=True)
    motor.f(ws, 'G%d' % B_MED,
            '=IFERROR(IF(COUNT($G${a}:$G${b})=0,"",AVERAGE($G${a}:$G${b})),"")'
            .format(a=B_INI, b=B_FIN), fmt=FMT_DEC, bold=True)
    ws['G%d' % B_MED].fill = PatternFill('solid', fgColor=CREMA)

    parrafo(ws, B_N1,
            'Esta media es SIMPLE y sólo sirve para verla de un vistazo al '
            'terminar. La nota que cuenta es la ponderada de la hoja «Rúbrica '
            'de Competencias», que pesa cada competencia según el puesto: para '
            'un ayudante, los cortes pesan más que las salsas.',
            col_fin='H', alto=30)
    parrafo(ws, B_N2,
            'Las puntuaciones de esta hoja se pasan A MANO a la hoja de '
            'evaluación. Es a propósito: la prueba se hace con una persona '
            'delante y la evaluación se cierra después, revisando lo que se '
            'apuntó.', col_fin='H', alto=30)

    motor.val(ws, 'A%d' % B_PIE, D.VERSION_LINE)
    ws['A%d' % B_PIE].font = Font(size=8, italic=True)
    motor.dv_numerica(ws, v_punt, minimo=1, maximo=5, titulo='Puntuación',
                      mensaje='Puntúa de 1 a 5. Deja la celda vacía si la '
                              'competencia no aplica.')
    motor.dv_fecha(ws, ['B%d' % B_FECHA])
    ws.freeze_panes = 'A11'
    pagina(ws, titulos='$%d:$%d' % (B_CAB, B_CAB), area='A1:H%d' % B_PIE)
    return ws


# --------------------------------------------------------------------------
# Hoja «Plan de Desarrollo Individual»
# --------------------------------------------------------------------------
D_CTRL = 5
D_CAB = 8
D_INI = 9
D_FIN = D_INI + N_PDI - 1
D_LEY_CAB = D_FIN + 2
D_LEY_INI = D_LEY_CAB + 1
D_LEY_FIN = D_LEY_INI + len(ESTADOS_PDI) - 1
D_RES_INI = D_LEY_FIN + 2
D_RES_FIN = D_RES_INI + len(ESTADOS_PDI) - 1
D_N1 = D_RES_FIN + 2
D_N2 = D_RES_FIN + 3
D_PIE = D_N2 + 2


def hoja_pdi(wb):
    ws = wb.create_sheet(H_PDI)
    anchos(ws, {'A': 8, 'B': 16, 'C': 46, 'D': 40, 'E': 54, 'F': 14,
                'G': 15, 'H': 14, 'I': 13, 'J': 24, 'K': 46})
    encabezar(ws, 'Plan de desarrollo individual', col_fin='K',
              nota_txt='Qué va a trabajar cada persona, con quién y para '
                       'cuándo. Sale de la evaluación técnica, no de una '
                       'conversación de pasillo.')
    motor.val(ws, 'A%d' % D_CTRL, 'Fecha de control', bold=True)
    ws.merge_cells('A%d:B%d' % (D_CTRL, D_CTRL))
    motor.val(ws, 'C%d' % D_CTRL,
              D._fecha(D.PARAMETROS_COCINA['fecha_corte_normativa']),
              fmt=FMT_FECHA)
    motor.verde(ws, 'C%d' % D_CTRL)
    ws.merge_cells('D%d:K%d' % (D_CTRL, D_CTRL))
    motor.val(ws, 'D%d' % D_CTRL,
              'Cámbiala y se recalculan los días que quedan para cada fecha '
              'objetivo.', wrap=True)
    ws['D%d' % D_CTRL].font = Font(italic=True, size=9)

    cabecera(ws, D_CAB,
             [('A', 'Id'), ('B', 'Persona'), ('C', 'Objetivo'),
              ('D', 'Competencias a trabajar'), ('E', 'Acciones'),
              ('F', 'Responsable'), ('G', 'Fecha objetivo'), ('H', 'Estado'),
              ('I', 'Días restantes'), ('J', 'Próxima partida a aprender'),
              ('K', 'Remite a')], altura=44)
    nombres = dict((p[0], p[1]) for p in D.PLANTILLA)
    v_estado, v_fecha = [], []
    for i in range(N_PDI):
        r = D_INI + i
        p = D.PDI[i] if i < len(D.PDI) else None
        if p:
            pid, objetivo, comps, acciones, resp, fecha, estado, remite = p
            comp_txt = '; '.join(D.COMPETENCIAS_TECNICAS[j][0] for j in comps)
        else:
            pid = objetivo = acciones = resp = fecha = estado = remite = ''
            comp_txt = ''
        motor.val(ws, 'A%d' % r, pid)
        motor.val(ws, 'B%d' % r, nombres.get(pid, ''))
        motor.val(ws, 'C%d' % r, objetivo, wrap=True)
        motor.val(ws, 'D%d' % r, comp_txt, wrap=True)
        motor.val(ws, 'E%d' % r, acciones, wrap=True)
        motor.val(ws, 'F%d' % r, resp, align='center')
        motor.val(ws, 'G%d' % r, D._fecha(fecha) if fecha else '',
                  fmt=FMT_FECHA)
        motor.val(ws, 'H%d' % r, estado, align='center')
        motor.val(ws, 'J%d' % r, proxima_partida(pid) if pid else '',
                  wrap=True)
        motor.val(ws, 'K%d' % r, remite, wrap=True)
        motor.verde(ws, 'A%d:H%d' % (r, r))
        motor.verde(ws, 'J%d:K%d' % (r, r))
        motor.f(ws, 'I%d' % r,
                '=IFERROR(IF(OR($G{r}="",$C${c}=""),"",$G{r}-$C${c}),"")'
                .format(r=r, c=D_CTRL), fmt=FMT_ENT)
        ws.row_dimensions[r].height = 54
        v_estado.append('H%d' % r)
        v_fecha.append('G%d' % r)

    cabecera(ws, D_LEY_CAB, [('A', 'Estado'), ('C', 'Cuándo se marca')],
             altura=20)
    ws.merge_cells('A%d:B%d' % (D_LEY_CAB, D_LEY_CAB))
    ws.merge_cells('C%d:K%d' % (D_LEY_CAB, D_LEY_CAB))
    pintar_cabecera(ws, 'A%d:K%d' % (D_LEY_CAB, D_LEY_CAB))
    glosas = ('Está escrito y tiene fecha, pero todavía no ha empezado.',
              'Ya se está trabajando: hay rotaciones hechas o formación en '
              'marcha.',
              'Se ha alcanzado el objetivo y hay una prueba práctica que lo '
              'respalda.')
    for i, estado in enumerate(ESTADOS_PDI):
        r = D_LEY_INI + i
        ws.merge_cells('A%d:B%d' % (r, r))
        motor.val(ws, 'A%d' % r, estado, bold=True)
        ws.merge_cells('C%d:K%d' % (r, r))
        motor.val(ws, 'C%d' % r, glosas[i], wrap=True)
        ws.row_dimensions[r].height = 22
    dv_rango(ws, v_estado,
             "'%s'!$A$%d:$A$%d" % (H_PDI, D_LEY_INI, D_LEY_FIN),
             'Estado del plan', 'Elige un estado de la lista.')

    for i, estado in enumerate(ESTADOS_PDI):
        r = D_RES_INI + i
        ws.merge_cells('A%d:B%d' % (r, r))
        motor.val(ws, 'A%d' % r, 'Planes en estado «' + estado + '»',
                  bold=(i == 0))
        motor.f(ws, 'C%d' % r,
                '=IFERROR(COUNTIF($H${a}:$H${b},$A${l}),"")'
                .format(a=D_INI, b=D_FIN, l=D_LEY_INI + i), fmt=FMT_ENT)
        ws['C%d' % r].fill = PatternFill('solid', fgColor=GRIS)

    parrafo(ws, D_N1,
            'La columna «Remite a» es texto a propósito: este libro NO enlaza '
            'con el Plan de Cross-Training del «Manual del Manager de '
            'Restaurante», lo cita con su fila. Un enlace entre ficheros se '
            'rompe en cuanto alguien mueve una carpeta, y entonces el plan '
            'miente sin avisar.', col_fin='K', alto=32)
    parrafo(ws, D_N2,
            '«Próxima partida a aprender» es la partida que esa persona tiene '
            'en marcha en el plan de cross-training. Si la celda va vacía es '
            'que esa persona no tiene ninguna rotación abierta, no que no '
            'pueda aprender.', col_fin='K', alto=32)

    motor.val(ws, 'A%d' % D_PIE, D.VERSION_LINE)
    ws['A%d' % D_PIE].font = Font(size=8, italic=True)
    motor.dv_fecha(ws, v_fecha + ['C%d' % D_CTRL])
    motor.semaforo_isnumber(ws, 'I%d:I%d' % (D_INI, D_FIN), '$I%d' % D_INI,
                            operador='<', umbral='0')
    ws.freeze_panes = 'C9'
    pagina(ws, titulos='$%d:$%d' % (D_CAB, D_CAB), area='A1:K%d' % D_PIE)
    return ws


# --------------------------------------------------------------------------
# Hoja «Histórico»
# --------------------------------------------------------------------------
T_CAB = 5
T_INI = 6
T_FIN = T_INI + N_HIST - 1
T_RES = T_FIN + 1
T_MED = T_FIN + 2
T_N1 = T_MED + 2
T_N2 = T_MED + 3
T_PIE = T_N2 + 2


def hoja_historico(wb):
    ws = wb.create_sheet(H_HIST)
    anchos(ws, {'A': 15, 'B': 8, 'C': 16, 'D': 30, 'E': 15, 'F': 12,
                'G': 14, 'H': 54})
    encabezar(ws, 'Histórico de evaluaciones', col_fin='H',
              nota_txt='Una línea por evaluación y por persona. La primera '
                       'ronda no dice nada; la segunda enseña quién ha crecido '
                       'y quién lleva año y medio en el mismo sitio.')
    cabecera(ws, T_CAB,
             [('A', 'Fecha'), ('B', 'Id'), ('C', 'Persona'),
              ('D', 'Puesto de la rúbrica'), ('E', 'Media ponderada'),
              ('F', 'Nivel técnico'), ('G', 'Evaluador'),
              ('H', 'Qué se acordó')], altura=32)
    nombres = dict((p[0], p[1]) for p in D.PLANTILLA)
    filas_ev = dict((e[0], U_EV_INI + i)
                    for i, e in enumerate(D.EVALUACIONES))
    v_fecha = []
    for i in range(N_HIST):
        r = T_INI + i
        e = EVALUADOS[i] if i < len(EVALUADOS) else None
        if e:
            pid, puesto, fecha, evaluador, _p = e
            fila = filas_ev[pid]
            motor.val(ws, 'A%d' % r, D._fecha(fecha), fmt=FMT_FECHA)
            motor.val(ws, 'B%d' % r, pid, align='center')
            motor.val(ws, 'C%d' % r, nombres.get(pid, ''))
            motor.val(ws, 'D%d' % r, puesto, wrap=True)
            motor.f(ws, 'E%d' % r,
                    '=IFERROR(IF(\'{h}\'!${m}{f}="","",\'{h}\'!${m}{f}),"")'
                    .format(h=H_RUBRICA, m=E_MED, f=fila), fmt=FMT_DEC)
            motor.f(ws, 'F%d' % r,
                    '=IFERROR(IF(\'{h}\'!${n}{f}="","",\'{h}\'!${n}{f}),"")'
                    .format(h=H_RUBRICA, n=E_NIV, f=fila), fmt=FMT_ENT)
            motor.val(ws, 'G%d' % r, evaluador, align='center')
        else:
            motor.val(ws, 'A%d' % r, '', fmt=FMT_FECHA)
            motor.val(ws, 'B%d' % r, '')
            motor.val(ws, 'C%d' % r, '')
            motor.val(ws, 'D%d' % r, '', wrap=True)
            motor.val(ws, 'E%d' % r, '', fmt=FMT_DEC)
            motor.val(ws, 'F%d' % r, '', fmt=FMT_ENT)
            motor.val(ws, 'G%d' % r, '')
            motor.verde(ws, 'E%d:F%d' % (r, r))
        motor.val(ws, 'H%d' % r, '', wrap=True)
        motor.verde(ws, 'A%d:D%d' % (r, r))
        motor.verde(ws, 'G%d:H%d' % (r, r))
        ws.row_dimensions[r].height = 26
        v_fecha.append('A%d' % r)

    motor.val(ws, 'A%d' % T_RES, 'Evaluaciones registradas', bold=True)
    ws.merge_cells('A%d:D%d' % (T_RES, T_RES))
    motor.f(ws, 'E%d' % T_RES,
            '=IF(COUNT($E${a}:$E${b})=0,"",COUNT($E${a}:$E${b}))'
            .format(a=T_INI, b=T_FIN), fmt=FMT_ENT, bold=True)
    ws['E%d' % T_RES].fill = PatternFill('solid', fgColor=CREMA)
    motor.val(ws, 'A%d' % T_MED, 'Media ponderada de la ronda', bold=True)
    ws.merge_cells('A%d:D%d' % (T_MED, T_MED))
    motor.f(ws, 'E%d' % T_MED,
            '=IFERROR(IF(COUNT($E${a}:$E${b})=0,"",AVERAGE($E${a}:$E${b})),"")'
            .format(a=T_INI, b=T_FIN), fmt=FMT_DEC, bold=True)
    ws['E%d' % T_MED].fill = PatternFill('solid', fgColor=CREMA)

    parrafo(ws, T_N1,
            'Las filas de la primera ronda leen la media y el nivel de la hoja '
            '«Rúbrica de Competencias» de este mismo libro: si corriges una '
            'puntuación allí, aquí cambia sola. Las filas vacías de abajo son '
            'para las rondas siguientes, y ahí la media se escribe a mano '
            'cuando cierres la ronda y quieras conservar la anterior.',
            col_fin='H', alto=40)
    parrafo(ws, T_N2,
            'Guarda también lo que se acordó en la conversación: sin eso, la '
            'evaluación siguiente empieza discutiendo qué se dijo en la '
            'anterior.', col_fin='H', alto=26)

    motor.val(ws, 'A%d' % T_PIE, D.VERSION_LINE)
    ws['A%d' % T_PIE].font = Font(size=8, italic=True)
    motor.dv_fecha(ws, v_fecha)
    motor.dv_numerica(ws, ['E%d' % r for r in range(T_INI + len(EVALUADOS),
                                                    T_FIN + 1)],
                      minimo=0, maximo=5, titulo='Media',
                      mensaje='La media ponderada va de 1 a 5.')
    motor.dv_numerica(ws, ['F%d' % r for r in range(T_INI + len(EVALUADOS),
                                                    T_FIN + 1)],
                      minimo=1, maximo=3, titulo='Nivel técnico',
                      mensaje='El nivel técnico va de 1 a 3.')
    ws.freeze_panes = 'A6'
    pagina(ws, titulos='$%d:$%d' % (T_CAB, T_CAB), area='A1:H%d' % T_PIE)
    return ws


# --------------------------------------------------------------------------
def mapa():
    celdas_org = {
        'Partidas activas declaradas': 'C%d' % O_ACTIVAS,
        'Área funcional de la brigada de cocina': 'C%d' % O_AREA,
        'Personas de la brigada de cocina': 'F%d' % O_TOT_PERS,
        'Personas dadas de alta en el organigrama': 'F%d' % O_TOT_HORAS,
    }
    for i, p in enumerate(D.PARTIDAS):
        r = O_PAR_INI + i
        celdas_org['Responsable de la partida «%s»' % p[0]] = 'E%d' % r
        celdas_org['Personas asignadas a la partida «%s»' % p[0]] = 'G%d' % r
        celdas_org['Alcance de la partida «%s»' % p[0]] = 'H%d' % r
    celdas_pue = {
        'Total de personas encuadradas en los puestos del convenio':
            'G%d' % P_TOT,
    }
    for i, (puesto, _g, _f, _n, _o) in enumerate(D.PUESTOS_ALEH):
        celdas_pue['Personas en el puesto «%s»' % puesto] = 'G%d' % (P_INI + i)
    celdas_raci = {}
    for i, (decision, _r) in enumerate(D.RACI):
        r = R_INI + i
        celdas_raci['Comprobación de la decisión «%s»' % decision[:52]] = \
            '%s%d' % (C_CHK, r)
    celdas_rub = {
        'Personas evaluadas en la rúbrica': '%s%d' % (E_MED, U_EV_RES),
        'Media ponderada de la brigada evaluada': '%s%d' % (E_MED, U_EV_MED),
    }
    for i, e in enumerate(D.EVALUACIONES):
        r = U_EV_INI + i
        if D.media_ponderada_evaluacion(e[0]) is None:
            continue
        celdas_rub['Media ponderada de %s' % e[0]] = '%s%d' % (E_MED, r)
        celdas_rub['Nivel técnico de %s' % e[0]] = '%s%d' % (E_NIV, r)
        celdas_rub['Lectura de cobertura y competencia de %s' % e[0]] = \
            '%s%d' % (E_LEC, r)
    celdas_pru = {
        'Duración total de la prueba práctica (minutos)': 'C%d' % B_TOT,
    }
    celdas_pdi = {
        'Fecha de control del plan de desarrollo': 'C%d' % D_CTRL,
    }
    for i, p in enumerate(D.PDI):
        celdas_pdi['Días restantes del plan de %s' % p[0]] = \
            'I%d' % (D_INI + i)
    for i, estado in enumerate(ESTADOS_PDI):
        celdas_pdi['Planes en estado «%s»' % estado] = 'C%d' % (D_RES_INI + i)
    celdas_hist = {
        'Evaluaciones registradas en el histórico': 'E%d' % T_RES,
        'Media ponderada de la ronda de septiembre de 2026': 'E%d' % T_MED,
    }
    for i, e in enumerate(EVALUADOS):
        celdas_hist['Media ponderada de %s en el histórico' % e[0]] = \
            'E%d' % (T_INI + i)
    return {
        'fichero': NOMBRE + '.xlsx',
        'producto': 'manual-chef-ejecutivo',
        'libro': 4,
        'nota': ('La hoja que la SPEC llama «Rúbrica de Competencias Técnicas» '
                 'se llama «' + H_RUBRICA + '» en el fichero: Excel corta los '
                 'nombres de pestaña en 31 caracteres y el de la SPEC tiene 32.'),
        'hojas': {
            H_ORG: {
                'celdas': celdas_org,
                'tablas': [
                    {'titulo': 'Las partidas de la cocina',
                     'cols': [['Nº', 'A', 'num'], ['Partida', 'B', 'txt'],
                              ['¿Produce raciones?', 'C', 'txt'],
                              ['Qué produce', 'D', 'txt'],
                              ['Responsable (titular)', 'E', 'txt'],
                              ['Personas asignadas', 'G', 'num'],
                              ['Alcance', 'H', 'txt']],
                     'filas': [O_PAR_INI, O_PAR_INI + len(D.PARTIDAS) - 1]},
                    {'titulo': 'La brigada, persona a persona',
                     'cols': [['Id', 'A', 'txt'], ['Nombre', 'B', 'txt'],
                              ['Grupo', 'C', 'txt'],
                              ['Puesto en tu organigrama', 'D', 'txt'],
                              ['Puesto del convenio (ALEH VI)', 'E', 'txt'],
                              ['Área funcional', 'F', 'txt'],
                              ['Nivel de delegación', 'G', 'txt'],
                              ['Partida principal', 'H', 'txt'],
                              ['Nivel en cocina', 'J', 'num']],
                     'filas': [O_BRI_INI, O_BRI_INI + PLANTILLA_N - 1]},
                ],
            },
            H_PUESTOS: {
                'celdas': celdas_pue,
                'tablas': [
                    {'titulo': 'Los diez puestos de cocina del ALEH VI',
                     'cols': [['Puesto (ALEH VI)', 'A', 'txt'],
                              ['Grupo', 'B', 'txt'],
                              ['Funciones del convenio (literal, art. 17.B)',
                               'C', 'txt'],
                              ['Nivel de delegación', 'E', 'txt'],
                              ['Personas', 'G', 'num']],
                     'filas': [P_INI, P_FIN]},
                    {'titulo': 'Los tres niveles de delegación del convenio',
                     'cols': [['Nivel', 'A', 'txt'], ['Puestos', 'C', 'txt'],
                              ['Cómo se manda en ese nivel', 'E', 'txt']],
                     'filas': [P_DEL_INI, P_DEL_FIN]},
                    {'titulo': 'Denominaciones de uso y su equivalencia',
                     'cols': [['Denominación de uso', 'A', 'txt'],
                              ['¿Está en el ALEH VI?', 'B', 'txt'],
                              ['Puesto equivalente por las funciones que hace',
                               'C', 'txt']],
                     'filas': [P_USO_INI, P_USO_FIN]},
                ],
            },
            H_RACI: {
                'celdas': celdas_raci,
                'tablas': [
                    {'titulo': 'Matriz RACI de cocina, sala y dirección',
                     'cols': ([['Decisión', 'A', 'txt']]
                              + [[D.ROLES_RACI[i], COLS_RACI[i], 'txt']
                                 for i in range(len(D.ROLES_RACI))]
                              + [['Comprobación', C_CHK, 'txt']]),
                     'filas': [R_INI, R_INI + len(D.RACI) - 1]},
                    {'titulo': 'Qué quiere decir cada letra',
                     'cols': [['Letra', 'A', 'txt'],
                              ['Qué quiere decir', 'B', 'txt']],
                     'filas': [R_LEY_INI, R_LEY_FIN]},
                ],
            },
            H_RUBRICA: {
                'celdas': celdas_rub,
                'tablas': [
                    {'titulo': 'Las siete competencias técnicas y sus niveles',
                     'cols': [['Competencia', 'A', 'txt'],
                              ['Nivel 1', 'B', 'txt'], ['Nivel 2', 'C', 'txt'],
                              ['Nivel 3', 'D', 'txt'], ['Nivel 4', 'E', 'txt'],
                              ['Nivel 5', 'F', 'txt']],
                     'filas': [U_DESC_INI, U_DESC_FIN]},
                    {'titulo': 'Peso de cada competencia por puesto',
                     'cols': ([['Puesto', 'A', 'txt']]
                              + [[D.COMPETENCIAS_TECNICAS[i][0], W_COMP[i],
                                  'num'] for i in range(N_COMP)]),
                     'filas': [U_PES_INI, U_PES_INI
                               + len(D.PESOS_COMPETENCIA_PUESTO) - 1]},
                    {'titulo': 'Evaluación técnica de la brigada',
                     'sin_dato': ('Las cuatro personas de sala pura (P08 a '
                                  'P11) no hacen la prueba de cocina: su '
                                  'media, su nivel técnico y su lectura van '
                                  'VACÍAS a propósito. N/A no es cero.'),
                     'cols': ([['Id', E_ID, 'txt'], ['Nombre', E_NOM, 'txt'],
                               ['Puesto de la rúbrica', E_PUE, 'txt']]
                              + [[D.COMPETENCIAS_TECNICAS[i][0], E_COMP[i],
                                  'num'] for i in range(N_COMP)]
                              + [['Media ponderada', E_MED, 'num'],
                                 ['Nivel técnico', E_NIV, 'num'],
                                 ['Nivel en cocina', E_POL, 'num'],
                                 ['Lectura', E_LEC, 'txt']]),
                     'filas': [U_EV_INI, U_EV_FIN]},
                ],
            },
            H_PRUEBA: {
                'celdas': celdas_pru,
                'tablas': [
                    {'titulo': 'Guion de la prueba práctica',
                     'cols': [['Competencia', 'A', 'txt'],
                              ['Prueba', 'B', 'txt'],
                              ['Minutos', 'C', 'num'],
                              ['Material', 'D', 'txt'],
                              ['Qué es un 5', 'E', 'txt'],
                              ['Qué es un 1', 'F', 'txt']],
                     'filas': [B_INI, B_FIN]},
                ],
            },
            H_PDI: {
                'celdas': celdas_pdi,
                'tablas': [
                    {'titulo': 'Planes de desarrollo individual abiertos',
                     'cols': [['Id', 'A', 'txt'], ['Persona', 'B', 'txt'],
                              ['Objetivo', 'C', 'txt'],
                              ['Competencias a trabajar', 'D', 'txt'],
                              ['Acciones', 'E', 'txt'],
                              ['Responsable', 'F', 'txt'],
                              ['Fecha objetivo', 'G', 'txt'],
                              ['Estado', 'H', 'txt'],
                              ['Próxima partida a aprender', 'J', 'txt'],
                              ['Remite a', 'K', 'txt']],
                     'filas': [D_INI, D_INI + len(D.PDI) - 1]},
                ],
            },
            H_HIST: {
                'celdas': celdas_hist,
                'tablas': [
                    {'titulo': 'Histórico de evaluaciones técnicas',
                     'cols': [['Fecha', 'A', 'txt'], ['Id', 'B', 'txt'],
                              ['Persona', 'C', 'txt'],
                              ['Puesto de la rúbrica', 'D', 'txt'],
                              ['Media ponderada', 'E', 'num'],
                              ['Nivel técnico', 'F', 'num']],
                     'filas': [T_INI, T_INI + len(EVALUADOS) - 1]},
                ],
            },
        },
    }


def main():
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_organigrama(wb)
    hoja_puestos(wb)
    hoja_raci(wb)
    hoja_rubrica(wb)
    hoja_prueba(wb)
    hoja_pdi(wb)
    hoja_historico(wb)

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
