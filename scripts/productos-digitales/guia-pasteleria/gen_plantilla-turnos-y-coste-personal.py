#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_plantilla-turnos-y-coste-personal.py — libro 8 de «Cómo Montar una
Pastelería» (SPEC §2.2 fila 8; decisiones D21 y D22, y la regla de no-solape
R6 de la §2.3).

Hojas: Instrucciones · Parámetros · Turnos Semanales · Horas y Coste ·
Plan de Contratación.

QUÉ DECIDE ESTE LIBRO
---------------------
Cuánta gente, de qué perfil, en qué turno y CUÁNTO CUESTA DE VERDAD con la
Seguridad Social dentro. El molde de la guía de panadería
(`plantilla-turnos-brigada.xlsx`) tiene CERO fórmulas: no suma horas, no
calcula coste y no sabe que el convenio de pastelería paga 15 pagas. Ese olvido
-la SS a cargo de la empresa, un 33 % sobre el bruto- es el que hunde el P&L de
un plan de negocio de apertura.

LO QUE NO HACE, Y DÓNDE SE HACE (regla R6)
------------------------------------------
* **No rehace las fichas de tarea del kit.** `kit-tareas-pasteleria/
  04-tareas-perfiles.xlsx` dice QUÉ hace cada perfil (Jefe Pastelero,
  Pastelero, Ayudante, Dependiente Vitrina). Este libro dice CUÁNTOS necesitas
  de cada uno, en qué turno y cuánto cuestan. Los cuatro nombres son los
  LITERALES del kit (D22): «oficial» no existe en el kit y está prohibido.
* **No proyecta el P&L**: el coste de personal mes a mes, con la rampa y la
  estacionalidad, lo hace `plan-financiero-3-anos-pasteleria.xlsx` (libro 5).
  Aquí se calcula el dimensionado que aquél consume, y se copia a mano: cero
  fórmulas entre libros.

DECISIONES TÉCNICAS
-------------------
* Los seis grupos del convenio de pastelería de Madrid (PA-33, revisión 2026,
  BOCM núm. 50) van EN CELDA VERDE, con su nota legal en la celda: el lector
  los sustituye por los de su convenio provincial. 15 pagas, no 14.
* El SMI (PA-32) se publica como referencia y con el aviso de que **en
  pastelería manda el convenio**: el grupo más bajo de Madrid (17.886,30 €/año)
  ya lo supera. El aviso es una fórmula, no una frase: si el lector teclea un
  convenio más bajo, salta.
* **Aritmética de meses, no funciones de calendario**: `NETWORKDAYS` está
  prohibida en la familia. El mes de alta sale de `MONTH()` sobre la fecha
  verde y todo lo demás son índices de mes.
* Cero constantes dentro de las fórmulas: pagas, SS, horas de jornada completa,
  horas anuales de contrato, mes de apertura y días de apertura viven en celdas
  verdes de «Parámetros».
* Sin `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA`, `RANK`
  ni `NETWORKDAYS`. `IFERROR(...,"")` en toda división; «sin dato» = `""`;
  semáforos con `ISNUMBER`; desplegables contra RANGO.
* Ninguna celda verde vacía (D21).

Salida fija: `build/plantilla-turnos-y-coste-personal.xlsx` + su mapa.
Via: Claude Code
"""
import datetime
import importlib.util
import json
import os
import subprocess
import sys

import openpyxl
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.page import PageMargins
from openpyxl.worksheet.properties import PageSetupProperties

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..'))
sys.path.insert(0, os.path.join(RAIZ, 'guias-v2_0'))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)
import motor                                                    # noqa: E402
import _comun_pasteleria as CP                                  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    'datos_ejemplo_pasteleria', os.path.join(AQUI, 'datos_ejemplo.py'))
D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(D)

motor.CTX['producto'] = 'guia-pasteleria-obrador'

# --------------------------------------------------------------------------
PID = 'guia-pasteleria-obrador'
PRODUCTO = 'Cómo Montar una Pastelería'
TITULO = 'Plantilla, turnos y coste de personal'
NOMBRE = 'plantilla-turnos-y-coste-personal'
SUBTITULO = 'AI Chef Pro · aichef.pro — ' + PRODUCTO
VERSION_LINE = ('Versión 1.0 · septiembre 2026 · aichef.pro/' + PID
                + ' · info@aichef.pro')
BIO = ('Diseñado por John Guerrero — chef y consultor gastronómico desde 2010, '
       'en cocina desde los 17 años.')
NOTA_DESPROTEGER = ('Para editar la estructura o una celda que no esté en '
                    'verde: Revisar > Desproteger hoja (no tiene contraseña).')

FMT_EUR = motor.FMT_EUR
FMT_PCT = motor.FMT_PCT
FMT_ENT = motor.FMT_ENT
FMT_FECHA = motor.FMT_FECHA
FMT_DEC = '#,##0.00'
FMT_DEC1 = '#,##0.0'

ORO = 'FFD700'
CABECERA = '2D2D2D'
CREMA = 'FFF6DC'

H_PAR = 'Parámetros'
H_TUR = 'Turnos Semanales'
H_COS = 'Horas y Coste'
H_PLA = 'Plan de Contratación'

DIAS = (('L', 'Lunes'), ('M', 'Martes'), ('X', 'Miércoles'), ('J', 'Jueves'),
        ('V', 'Viernes'), ('S', 'Sábado'), ('D', 'Domingo'))
COL_DIA = ('E', 'F', 'G', 'H', 'I', 'J', 'K')
SI_NO = ('Sí', 'No')

#: Reparto de horas por persona y día. SUPUESTO declarado: cuadra las horas
#: contratadas de cada uno (40/40/20/20/20) con los 6 días que abre el
#: despacho, sin dejar ningún día abierto sin nadie en el mostrador.
TURNOS = {
    'P1': (0, 8, 8, 8, 8, 8, 0),
    'P2': (8, 8, 8, 8, 8, 0, 0),
    'P3': (4, 4, 4, 4, 4, 0, 0),
    'P4': (4, 4, 4, 4, 4, 0, 0),
    'P5': (0, 4, 4, 4, 4, 4, 0),
}
ABRE = ('Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No')

#: Fechas de alta por defecto (SUPUESTO): el obrador entra ANTES de abrir para
#: ensayar las tandas, el despacho de mañana el mismo día, y el turno de tarde
#: tres meses después, cuando la venta de tarde lo justifica y justo antes de
#: la campaña de Navidad. Escalonar el alta del quinto es lo que hace que el
#: año 1 no cueste lo mismo que el año de crucero.
ANIO_PLAN = 2027
ALTAS = {
    'P1': datetime.date(ANIO_PLAN, 8, 2),
    'P2': datetime.date(ANIO_PLAN, 8, 16),
    'P3': datetime.date(ANIO_PLAN, 9, 1),
    'P4': datetime.date(ANIO_PLAN, 9, 1),
    'P5': datetime.date(ANIO_PLAN, 12, 1),
}
GRUPO_REFUERZO = 5              # «Personal de apoyo» del convenio de Madrid

PLANTILLA = list(D.PLANTILLA)
N_PERS = len(PLANTILLA)
N_GRUPOS = len(D.CONVENIO)
PICOS = list(D.PICOS)
N_PICOS = len(PICOS)

# Gate legal ANTES de escribir una sola nota (SPEC §2.2).
IDS_LEGALES = ('PA-32', 'PA-33', 'PA-39')
D.gate_legal(IDS_LEGALES)
NOTAS_LEGALES = 0


# --------------------------------------------------------------------------
# Utilidades de formato
# --------------------------------------------------------------------------
def anchos(ws, mapa):
    for letra, ancho in mapa.items():
        ws.column_dimensions[letra].width = ancho


def cabecera(ws, fila, columnas, altura=30):
    for letra, texto in columnas:
        c = ws[letra + str(fila)]
        c.value = texto
        c.fill = PatternFill('solid', fgColor=CABECERA)
        c.font = Font(bold=True, color='FFFFFF', size=9)
        c.alignment = Alignment(horizontal='center', vertical='center',
                                wrap_text=True)
    ws.row_dimensions[fila].height = altura


def seccion(ws, coord, texto):
    motor.val(ws, coord, texto, bold=True)
    ws[coord].font = Font(bold=True, size=12)


def parrafo(ws, fila, texto, col_ini='A', col_fin='F', alto=30):
    ws.merge_cells('%s%d:%s%d' % (col_ini, fila, col_fin, fila))
    motor.val(ws, '%s%d' % (col_ini, fila), texto, wrap=True)
    ws['%s%d' % (col_ini, fila)].font = Font(italic=True, size=9)
    ws.row_dimensions[fila].height = alto


def pagina(ws, apaisado=True, titulos=None, area=None):
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
    if area:
        ws.print_area = area


def encabezar(ws, titulo, nota_txt=None, col_fin='F'):
    motor.val(ws, 'A1', CP.titulo_hoja(titulo))
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', SUBTITULO)
    if nota_txt:
        ws.merge_cells('A3:%s3' % col_fin)
        motor.val(ws, 'A3', nota_txt, wrap=True)
        ws['A3'].font = Font(italic=True, size=9)
        ws.row_dimensions[3].height = 28


def dv_rango(ws, coords, ref, titulo, mensaje):
    if not coords:
        return None
    dv = DataValidation(type='list', formula1=ref, allow_blank=False,
                        showErrorMessage=True, errorTitle=titulo,
                        error=mensaje)
    ws.add_data_validation(dv)
    for c in coords:
        dv.add(c)
    return dv


def nota_celda(ws, coord, id_pa, extra=None):
    global NOTAS_LEGALES
    texto = D.nota_legal(id_pa)
    if not texto:
        raise SystemExit('sin nota legal para ' + id_pa)
    if extra:
        texto = extra + ' — ' + texto
    ws[coord].comment = Comment(texto, 'AI Chef Pro', height=140, width=460)
    NOTAS_LEGALES += 1
    return texto


def pie(ws, fila):
    motor.val(ws, 'A%d' % fila, BIO)
    ws['A%d' % fila].font = Font(italic=True, size=9)
    motor.val(ws, 'A%d' % (fila + 1), VERSION_LINE)
    ws['A%d' % (fila + 1)].font = Font(size=8, italic=True)


# --------------------------------------------------------------------------
# Hoja «Instrucciones»
# --------------------------------------------------------------------------
PASOS = [
    '1. Hoja «Parámetros»: los seis grupos del convenio de pastelería de '
    'Madrid de 2026, las pagas, la Seguridad Social a cargo de la empresa, la '
    'jornada completa y el mes en el que piensas abrir. Todo en verde: si tu '
    'provincia tiene convenio propio -y casi todas lo tienen-, sustituye los '
    'seis brutos por los tuyos y el libro entero se recalcula.',
    '2. Hoja «Turnos Semanales»: cuántas horas hace cada persona cada día. '
    'Viene rellena con la plantilla del caso «La Clara»: cinco personas y 3,5 '
    'jornadas. La hoja suma las horas por persona y por día, separa obrador de '
    'despacho y avisa si algún día que abres se queda sin nadie en el '
    'mostrador.',
    '3. Hoja «Horas y Coste»: asigna a cada persona su grupo de convenio y la '
    'hoja calcula el bruto ajustado a su jornada, el bruto anual con las 15 '
    'pagas, el coste de empresa con la Seguridad Social dentro y el coste por '
    'hora. Avisa si alguien pasa de la jornada completa y si un grupo se te '
    'queda por debajo del SMI.',
    '4. Hoja «Plan de Contratación»: cuándo das de alta a cada uno y cuánto '
    'cuesta el primer año, que NO es el año de crucero porque nadie entra el '
    'día 1. Debajo, el refuerzo de las seis campañas: personas, horas y coste '
    'de cada pico.',
    '5. Lleva al libro 5 (plan financiero) sólo dos números: el coste de '
    'personal del año de crucero y el del primer año. Se copian a mano, a '
    'propósito: en todo este pack no hay ni una fórmula que apunte a otro '
    'fichero.',
]

NOTAS_LIBRO = [
    'DEL BRUTO AL COSTE DE EMPRESA HAY UN 33 %, Y ESE ES EL NÚMERO QUE HUNDE '
    'LOS PLANES. Un ayudante de 1.192,42 € al mes no cuesta 1.192,42 €: con 15 '
    'pagas y la Seguridad Social a cargo de la empresa cuesta casi 24.000 € al '
    'año a jornada completa. La plantilla del caso «La Clara» -cinco personas, '
    '3,5 jornadas- sale por encima de los 92.000 € anuales. Ese es el número '
    'que se lleva al plan financiero.',
    'EN PASTELERÍA MANDA EL CONVENIO, NO EL SMI. El grupo más bajo del '
    'convenio de Madrid está en 17.886,30 € al año, por encima de la '
    'referencia anual del SMI de 2026 (17.094 €). Por eso el SMI aparece aquí '
    'sólo como aviso: si tecleas un convenio cuyo grupo más bajo se queda por '
    'debajo, la hoja lo marca. Y ojo con la fecha: la tabla de Madrid caduca el '
    '31-12-2026 y el convenio entra en renegociación.',
    'LAS 15 PAGAS NO SON UN DETALLE. El convenio de pastelería de Madrid paga '
    'quince, no catorce. Sobre el grupo 2 son 1.427,89 € más al año por '
    'persona respecto de calcularlo con catorce: en una plantilla de 3,5 '
    'jornadas, más de 4.000 € que no estaban en el plan.',
    'ESTE LIBRO NO REHACE LAS FICHAS DE PUESTO. Lo que hace cada perfil -Jefe '
    'Pastelero, Pastelero, Ayudante y Dependiente Vitrina- está en el '
    '04-tareas-perfiles.xlsx del Kit de Tareas Pastelería (12 €), con sus '
    'tareas por turno. Aquí se decide cuántas personas de cada perfil hacen '
    'falta, en qué horario y cuánto cuestan. Son dos preguntas distintas y no '
    'se pisan.',
    'EL REFUERZO DE CAMPAÑA NO ES PLANTILLA. Reyes multiplica por seis la '
    'producción del obrador con el mismo equipo y la misma gente: o refuerzas, '
    'o no sales. El coste de ese refuerzo se calcula abajo con el coste por '
    'hora del convenio, y hay que meterlo en la tesorería del mes ANTES de la '
    'campaña, porque se paga a mes vencido y se cobra en la campaña.',
]


def hoja_instrucciones(wb):
    ws = wb.create_sheet('Instrucciones', 0)
    anchos(ws, {'A': 48, 'B': 48, 'C': 48})
    motor.val(ws, 'A1', TITULO)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', SUBTITULO)
    motor.val(ws, 'A3', 'Para qué sirve: decidir cuánta gente necesitas, de '
                        'qué perfil, en qué turno y cuánto cuesta de verdad '
                        'con la Seguridad Social dentro.')
    ws['A3'].font = Font(italic=True, size=9)

    seccion(ws, 'A5', 'Instrucciones de uso')
    fila = 6
    for paso in PASOS:
        ws.merge_cells('A%d:C%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, paso, wrap=True)
        ws.row_dimensions[fila].height = 62
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, motor.NOTA_VERDES)
    ws['A%d' % fila].fill = PatternFill('solid', fgColor=motor.VERDE)
    fila += 2

    seccion(ws, 'A%d' % fila, 'Lo que conviene saber antes de empezar')
    fila += 1
    for texto in NOTAS_LIBRO:
        ws.merge_cells('A%d:C%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, texto, wrap=True)
        ws.row_dimensions[fila].height = 76
        fila += 1
    fila += 1

    seccion(ws, 'A%d' % fila, 'Cada cuánto se usa este libro')
    fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila,
              'Cadencia: UNA VEZ al dimensionar la plantilla, antes de firmar '
              'nada; OTRA VEZ antes de cada una de las seis campañas, para '
              'decidir el refuerzo; y una revisión ANUAL cuando se publique la '
              'revisión salarial del convenio, que en Madrid sale en el BOCM '
              'de febrero. Los turnos del día a día no se llevan aquí: se '
              'llevan en el cuadrante del obrador.', wrap=True)
    ws.row_dimensions[fila].height = 52
    fila += 2

    seccion(ws, 'A%d' % fila,
            'La frontera con el Kit de Tareas Pastelería (12 €)')
    fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila,
              'El kit tiene el 04-tareas-perfiles.xlsx con una pestaña por '
              'perfil: Jefe Pastelero, Pastelero, Ayudante y Dependiente '
              'Vitrina, con lo que hace cada uno en cada turno. Este libro NO '
              'lo repite y no lo sustituye: construye el dimensionado (cuántas '
              'personas de cada perfil, con su bruto de convenio y su '
              'Seguridad Social) y el plan de contratación con sus fechas. Si '
              'tienes los dos productos, el kit te dice qué hace cada uno y '
              'este libro cuánto te cuesta.', wrap=True)
    ws.row_dimensions[fila].height = 76
    fila += 2

    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila, NOTA_DESPROTEGER, wrap=True)
    fila += 2
    pie(ws, fila)
    pagina(ws, apaisado=False)
    return ws


# --------------------------------------------------------------------------
# Hoja «Parámetros»
# --------------------------------------------------------------------------
G_CAB = 7
G_INI = 8
G_FIN = G_INI + N_GRUPOS - 1                    # 13
P_PAGAS = G_FIN + 2                             # 15
P_MINCONV = G_FIN + 3
P_SMI = G_FIN + 4
P_AVISO_SMI = G_FIN + 5
P_SEC2 = P_AVISO_SMI + 2                        # 20
P_SS = P_SEC2 + 1
P_JORNADA = P_SEC2 + 2
P_HORAS_ANIO = P_SEC2 + 3
P_DIAS = P_SEC2 + 4
P_MES_AP = P_SEC2 + 5
P_NOTA = P_MES_AP + 2
P_PIE = P_NOTA + 4


def hoja_parametros(wb):
    ws = wb.create_sheet(H_PAR)
    anchos(ws, {'A': 8, 'B': 42, 'C': 16, 'D': 16, 'E': 30, 'F': 46, 'G': 60})
    encabezar(ws, 'Parámetros: convenio, cotización y jornada', col_fin='G',
              nota_txt='Todo lo verde de esta hoja gobierna las otras tres. '
                       'Los seis brutos son los del convenio de pastelería de '
                       'Madrid de 2026: sustitúyelos por los de tu convenio '
                       'provincial.')
    seccion(ws, 'A5', 'Los seis grupos del convenio de referencia')
    ws.merge_cells('A6:G6')
    motor.val(ws, 'A6',
              'Convenio del Sector de Comercio e Industria de Confitería, '
              'Pastelería, Bollería, Repostería, Heladería y Platos Cocinados '
              'de la Comunidad de Madrid, código ' + D.CONVENIO_CODIGO
              + '. Revisión salarial 2026 publicada en el '
              + D.CONVENIO_PUBLICACION + ', vigencia ' + D.CONVENIO_VIGENCIA
              + '. Tablas a ' + str(D.CONVENIO_PAGAS) + ' pagas.', wrap=True)
    ws['A6'].font = Font(italic=True, size=9)
    ws.row_dimensions[6].height = 30
    cabecera(ws, G_CAB, [('A', 'Grupo'), ('B', 'Descripción funcional'),
                         ('C', 'Bruto mensual (€)'),
                         ('D', 'Bruto anual publicado (€)'),
                         ('E', 'Áreas funcionales'),
                         ('F', 'Puestos que cita el convenio'),
                         ('G', 'Nota')], altura=34)
    verdes_bruto = []
    for i, (n, desc, mes, anio, areas, puestos) in enumerate(D.CONVENIO):
        r = G_INI + i
        motor.val(ws, 'A%d' % r, n, fmt=FMT_ENT, align='center')
        motor.val(ws, 'B%d' % r, desc)
        motor.val(ws, 'C%d' % r, mes, fmt=FMT_EUR, verde_=True)
        verdes_bruto.append('C%d' % r)
        motor.val(ws, 'D%d' % r, anio, fmt=FMT_EUR)
        motor.val(ws, 'E%d' % r, ' · '.join(areas))
        motor.val(ws, 'F%d' % r, puestos or '', wrap=True)
        motor.val(ws, 'G%d' % r,
                  'Bruto de tabla, sin antigüedad, plus de nocturnidad ni '
                  'horas extra. El obrador entra de madrugada: mira el plus de '
                  'nocturnidad de tu convenio antes de cerrar el número.',
                  wrap=True)
        nota_celda(ws, 'C%d' % r, 'PA-33',
                   'Bruto mensual del grupo %d a %d pagas'
                   % (n, D.CONVENIO_PAGAS))
        ws.row_dimensions[r].height = 26

    def par(fila, etiqueta, valor, fmt, nota, verde=True, formula=None):
        motor.val(ws, 'A%d' % fila, etiqueta, bold=True)
        ws.merge_cells('A%d:B%d' % (fila, fila))
        if formula:
            motor.f(ws, 'C%d' % fila, formula, fmt=fmt, bold=True)
            ws['C%d' % fila].fill = PatternFill('solid', fgColor=CREMA)
        else:
            motor.val(ws, 'C%d' % fila, valor, fmt=fmt, verde_=verde)
        ws.merge_cells('E%d:G%d' % (fila, fila))
        motor.val(ws, 'E%d' % fila, nota, wrap=True)
        ws['E%d' % fila].font = Font(italic=True, size=9)
        ws.row_dimensions[fila].height = 28

    par(P_PAGAS, 'Pagas del convenio', D.P('pagas_convenio'), FMT_ENT,
        'El convenio de Madrid paga 15, no 14, y eso cambia el coste todos los '
        'meses. Si tu convenio prorratea las extras, sigue siendo 15: lo que '
        'cambia es cuándo se pagan, no cuánto.')
    nota_celda(ws, 'C%d' % P_PAGAS, 'PA-33', 'Las tablas de Madrid son a 15 '
                                             'pagas')
    par(P_MINCONV, 'Bruto anual del grupo más bajo (€)', None, FMT_EUR,
        'Se calcula con los brutos de arriba y las pagas: es el número que se '
        'compara con el SMI.',
        formula='=IFERROR(MIN($C${a}:$C${b})*$C${p},"")'
                .format(a=G_INI, b=G_FIN, p=P_PAGAS))
    par(P_SMI, 'Referencia anual del SMI (€)', D.P('smi_anual'), FMT_EUR,
        'Cuantía ANUAL de referencia del art. 3.1 del RD 126/2026, en cómputo '
        'global: no es un mínimo por concepto ni el resultado de multiplicar '
        'por catorce. CADUCA el 31-12-2026.')
    nota_celda(ws, 'C%d' % P_SMI, 'PA-32',
               'SMI 2026: 1.221 €/mes y referencia anual de 17.094 €')
    motor.val(ws, 'A%d' % P_AVISO_SMI, '¿Manda el convenio o el SMI?',
              bold=True)
    ws.merge_cells('A%d:B%d' % (P_AVISO_SMI, P_AVISO_SMI))
    motor.f(ws, 'C%d' % P_AVISO_SMI,
            '=IF($C${m}="","",IF($C${m}>=$C${s},'
            '"Manda el convenio: el grupo más bajo supera el SMI",'
            '"OJO: el grupo más bajo se queda por debajo del SMI anual"))'
            .format(m=P_MINCONV, s=P_SMI), bold=True)
    ws['C%d' % P_AVISO_SMI].fill = PatternFill('solid', fgColor=CREMA)
    ws.merge_cells('E%d:G%d' % (P_AVISO_SMI, P_AVISO_SMI))
    motor.val(ws, 'E%d' % P_AVISO_SMI,
              'En pastelería manda el convenio. Este aviso existe por si '
              'tecleas el de otra provincia: ningún grupo puede quedar por '
              'debajo del SMI en cómputo anual.', wrap=True)
    ws['E%d' % P_AVISO_SMI].font = Font(italic=True, size=9)

    seccion(ws, 'A%d' % P_SEC2, 'Cotización, jornada y calendario')
    motor.escribir_parametro(ws, P_SS, 'A', 'C', 'ss_empresa', col_nota='E')
    ws.merge_cells('A%d:B%d' % (P_SS, P_SS))
    ws.merge_cells('E%d:G%d' % (P_SS, P_SS))
    ws['E%d' % P_SS].font = Font(italic=True, size=9)
    ws['A%d' % P_SS].font = Font(bold=True)
    ws.row_dimensions[P_SS].height = 30
    par(P_JORNADA, 'Horas semanales de jornada completa',
        D.P('horas_semana_jornada_completa'), FMT_ENT,
        'SUPUESTO: la jornada anual del convenio de Madrid no está verificada. '
        'Cámbiala por la de tu convenio; es la que decide si alguien se pasa '
        'de jornada y cuántas jornadas equivalentes tienes.')
    par(P_HORAS_ANIO, 'Horas anuales de contrato',
        D.P('horas_anuales_contrato'), FMT_ENT,
        'SUPUESTO: 40 h × 52 semanas = 2.080, menos 30 días naturales de '
        'vacaciones y los festivos. Es el divisor del coste por hora, y por '
        'eso el coste por hora sale más caro de lo que la gente espera.')
    par(P_DIAS, 'Días de apertura a la semana',
        D.NEGOCIO['dias_apertura_semana'], FMT_ENT,
        'SUPUESTO. La pastelería tiene libertad horaria por ley estatal cuando '
        'es su actividad principal, así que abrir en domingo o en festivo es '
        'una decisión tuya, no un permiso que se pida.')
    nota_celda(ws, 'C%d' % P_DIAS, 'PA-39',
               'Libertad horaria de la pastelería')
    par(P_MES_AP, 'Mes de apertura previsto (1 a 12)',
        D.NEGOCIO['mes_apertura_recomendado'], FMT_ENT,
        'SUPUESTO: septiembre. No es ninguno de los seis picos y deja tres '
        'meses y medio de rodaje antes de Reyes, que es la campaña que decide '
        'el año. La fecha realista la calcula la ruta crítica del libro 6.')

    parrafo(ws, P_NOTA,
            'Los seis brutos y las pagas son datos verificados contra el BOCM '
            'el 10-09-2026 (pasa el ratón por encima de cada celda para ver la '
            'fuente). Todo lo demás de esta hoja es SUPUESTO y se dice en cada '
            'nota. Un convenio provincial distinto no cambia ninguna fórmula '
            'de este libro: cambia seis números.', col_fin='G', alto=40)
    parrafo(ws, P_NOTA + 1,
            'Lo que esta hoja NO trae, a propósito: antigüedad, plus de '
            'nocturnidad, horas extra, pluses de transporte y bonificaciones a '
            'la contratación. Son reales y cambian el coste, pero dependen de '
            'tu convenio y de cada contrato: cuando los tengas, súmalos al '
            'bruto mensual de cada grupo.', col_fin='G', alto=34)

    motor.dv_numerica(ws, verdes_bruto, minimo=0, titulo='Bruto de convenio',
                      mensaje='Escribe el bruto MENSUAL de tabla, en euros.')
    motor.dv_numerica(ws, ['C%d' % P_PAGAS], minimo=12, maximo=16,
                      titulo='Pagas', mensaje='Entre 12 y 16 pagas.')
    motor.dv_numerica(ws, ['C%d' % P_SMI], minimo=0, titulo='SMI anual',
                      mensaje='Referencia anual del SMI, en euros.')
    motor.dv_porcentaje(ws, ['C%d' % P_SS])
    motor.dv_numerica(ws, ['C%d' % P_JORNADA], minimo=1, maximo=48,
                      titulo='Jornada completa',
                      mensaje='Horas semanales de jornada completa (1 a 48).')
    motor.dv_numerica(ws, ['C%d' % P_HORAS_ANIO], minimo=1, maximo=2200,
                      titulo='Horas anuales',
                      mensaje='Horas anuales de contrato (1 a 2.200).')
    motor.dv_numerica(ws, ['C%d' % P_DIAS], minimo=1, maximo=7,
                      titulo='Días de apertura',
                      mensaje='Días de apertura a la semana (1 a 7).')
    motor.dv_numerica(ws, ['C%d' % P_MES_AP], minimo=1, maximo=12,
                      titulo='Mes de apertura',
                      mensaje='Mes de apertura previsto (1 = enero).')
    pie(ws, P_PIE)
    pagina(ws, titulos='$%d:$%d' % (G_CAB, G_CAB), area='A1:G%d' % (P_PIE + 1))
    return ws


# --------------------------------------------------------------------------
# Hoja «Turnos Semanales»
# --------------------------------------------------------------------------
T_ABRE_CAB = 6
T_ABRE = 7
T_SEC2 = 9
T_CAB = 10
T_INI = 11
T_FIN = T_INI + N_PERS - 1                      # 15
T_TOT = T_FIN + 1                               # 16
T_OBR = T_FIN + 2
T_DES = T_FIN + 3
T_COBER = T_FIN + 4
T_RES = T_FIN + 6
T_TOT_SEM = T_RES + 1
T_TOT_JOR = T_RES + 2
T_TOT_OBR = T_RES + 3
T_TOT_DES = T_RES + 4
T_HUECOS = T_RES + 5
T_LIST_SEC = T_HUECOS + 2
T_LIST_CAB = T_LIST_SEC + 1
T_LIST_INI = T_LIST_CAB + 1
T_LIST_FIN = T_LIST_INI + len(SI_NO) - 1
T_NOTA = T_LIST_FIN + 2
T_PIE = T_NOTA + 4


def hoja_turnos(wb):
    ws = wb.create_sheet(H_TUR)
    anchos(ws, {'A': 6, 'B': 24, 'C': 13, 'D': 26, 'E': 7, 'F': 7, 'G': 7,
                'H': 7, 'I': 7, 'J': 7, 'K': 7, 'L': 15, 'M': 15, 'N': 14,
                'O': 58})
    encabezar(ws, 'Turnos semanales', col_fin='O',
              nota_txt='Cinco personas y 3,5 jornadas: el dimensionado del '
                       'caso «La Clara». Los cuatro perfiles son los '
                       'literales del 04-tareas-perfiles.xlsx del kit, con dos '
                       'personas en Dependiente Vitrina.')

    seccion(ws, 'A5', '¿Qué días abre el despacho?')
    cols_dia = [(COL_DIA[i], DIAS[i][0]) for i in range(7)]
    cabecera(ws, T_ABRE_CAB, [('A', 'Día')] + cols_dia, altura=20)
    ws.merge_cells('A%d:D%d' % (T_ABRE_CAB, T_ABRE_CAB))
    motor.val(ws, 'A%d' % T_ABRE, '¿Abre el despacho?', bold=True)
    ws.merge_cells('A%d:D%d' % (T_ABRE, T_ABRE))
    verdes_abre = []
    for i in range(7):
        motor.val(ws, '%s%d' % (COL_DIA[i], T_ABRE), ABRE[i], verde_=True,
                  align='center')
        verdes_abre.append('%s%d' % (COL_DIA[i], T_ABRE))
    ws.merge_cells('L%d:O%d' % (T_ABRE, T_ABRE))
    motor.val(ws, 'L%d' % T_ABRE,
              'SUPUESTO: seis días, con el domingo cerrado. Es una decisión '
              'tuya, no un permiso: la pastelería tiene libertad horaria.',
              wrap=True)
    ws['L%d' % T_ABRE].font = Font(italic=True, size=9)

    seccion(ws, 'A%d' % T_SEC2, 'Horas por persona y día')
    cabecera(ws, T_CAB,
             [('A', 'Id'), ('B', 'Persona (perfil del kit)'), ('C', 'Área'),
              ('D', 'Turno')] + cols_dia
             + [('L', 'Horas planificadas / semana'),
                ('M', 'Horas contratadas / semana'),
                ('N', 'Diferencia (h)'), ('O', 'Nota')], altura=40)
    verdes_horas, verdes_contrato = [], []
    for i, (pid, perfil, jornada, grupo, area, horas, turno) in \
            enumerate(PLANTILLA):
        r = T_INI + i
        motor.val(ws, 'A%d' % r, pid, align='center')
        motor.val(ws, 'B%d' % r, perfil)
        motor.val(ws, 'C%d' % r, area)
        motor.val(ws, 'D%d' % r, turno)
        for j in range(7):
            motor.val(ws, '%s%d' % (COL_DIA[j], r), TURNOS[pid][j],
                      fmt=FMT_ENT, verde_=True, align='center')
            verdes_horas.append('%s%d' % (COL_DIA[j], r))
        motor.f(ws, 'L%d' % r, '=SUM($E{r}:$K{r})'.format(r=r), fmt=FMT_ENT,
                bold=True)
        motor.val(ws, 'M%d' % r, horas, fmt=FMT_ENT, verde_=True)
        verdes_contrato.append('M%d' % r)
        motor.f(ws, 'N%d' % r,
                '=IFERROR(IF(OR($L{r}="",$M{r}=""),"",$L{r}-$M{r}),"")'
                .format(r=r), fmt=FMT_ENT)
        motor.val(ws, 'O%d' % r,
                  'Jornada contratada: %s. Las horas del reparto son un '
                  'SUPUESTO que cuadra con esa jornada.'
                  % ('completa' if jornada >= 1 else ('%.0f %%' % (jornada * 100))),
                  wrap=True)
        ws.row_dimensions[r].height = 24

    motor.val(ws, 'A%d' % T_TOT, 'TOTAL de la plantilla', bold=True)
    ws.merge_cells('A%d:D%d' % (T_TOT, T_TOT))
    for j in range(7):
        c = COL_DIA[j]
        motor.f(ws, '%s%d' % (c, T_TOT),
                '=SUM(${c}${a}:${c}${b})'.format(c=c, a=T_INI, b=T_FIN),
                fmt=FMT_ENT, bold=True)
        ws['%s%d' % (c, T_TOT)].fill = PatternFill('solid', fgColor=CREMA)
    motor.f(ws, 'L%d' % T_TOT, '=SUM($L${a}:$L${b})'.format(a=T_INI, b=T_FIN),
            fmt=FMT_ENT, bold=True)
    ws['L%d' % T_TOT].fill = PatternFill('solid', fgColor=CREMA)
    motor.f(ws, 'M%d' % T_TOT, '=SUM($M${a}:$M${b})'.format(a=T_INI, b=T_FIN),
            fmt=FMT_ENT, bold=True)

    motor.val(ws, 'A%d' % T_OBR, 'Horas de OBRADOR por día', bold=True)
    ws.merge_cells('A%d:D%d' % (T_OBR, T_OBR))
    motor.val(ws, 'A%d' % T_DES, 'Horas de DESPACHO por día', bold=True)
    ws.merge_cells('A%d:D%d' % (T_DES, T_DES))
    motor.val(ws, 'A%d' % T_COBER, 'Cobertura del despacho', bold=True)
    ws.merge_cells('A%d:D%d' % (T_COBER, T_COBER))
    for j in range(7):
        c = COL_DIA[j]
        motor.f(ws, '%s%d' % (c, T_OBR),
                '=SUMPRODUCT(--($C${a}:$C${b}="OBRADOR"),${c}${a}:${c}${b})'
                .format(a=T_INI, b=T_FIN, c=c), fmt=FMT_ENT)
        motor.f(ws, '%s%d' % (c, T_DES),
                '=SUMPRODUCT(--($C${a}:$C${b}="COMERCIO"),${c}${a}:${c}${b})'
                .format(a=T_INI, b=T_FIN, c=c), fmt=FMT_ENT)
        motor.f(ws, '%s%d' % (c, T_COBER),
                '=IF(${c}${ab}<>"Sí","Cerrado",IF(${c}${d}=0,"SIN NADIE",'
                '"Cubierto"))'.format(c=c, ab=T_ABRE, d=T_DES), align='center')
    motor.semaforo_texto(ws, '%s%d:%s%d' % (COL_DIA[0], T_COBER, COL_DIA[6],
                                            T_COBER),
                         (('Cubierto', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                          ('SIN NADIE', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('Cerrado', motor.CF_GRIS_BG, motor.CF_GRIS_FG)))

    def res(fila, etiqueta, formula, fmt, nota):
        motor.val(ws, 'A%d' % fila, etiqueta, bold=True)
        ws.merge_cells('A%d:D%d' % (fila, fila))
        motor.f(ws, 'E%d' % fila, formula, fmt=fmt, bold=True)
        ws.merge_cells('E%d:F%d' % (fila, fila))
        ws['E%d' % fila].fill = PatternFill('solid', fgColor=CREMA)
        ws.merge_cells('H%d:O%d' % (fila, fila))
        motor.val(ws, 'H%d' % fila, nota, wrap=True)
        ws['H%d' % fila].font = Font(italic=True, size=9)
        ws.row_dimensions[fila].height = 24

    seccion(ws, 'A%d' % T_RES, 'Resumen de la semana')
    res(T_TOT_SEM, 'Horas planificadas a la semana',
        '=$L${t}'.format(t=T_TOT), FMT_ENT,
        'Es la semana tipo de velocidad de crucero, sin campañas.')
    res(T_TOT_JOR, 'Jornadas equivalentes',
        "=IFERROR($L${t}/'{p}'!$C${j},\"\")".format(t=T_TOT, p=H_PAR,
                                                    j=P_JORNADA), FMT_DEC1,
        'Horas planificadas divididas por la jornada completa. El caso «La '
        'Clara» son 3,5 jornadas repartidas en cinco personas.')
    # Hallazgo A1 (2026-09-10): `=SUM(E17:K17)`/`=SUM(E18:K18)` sobre una fila
    # de SUMPRODUCT se cacheaba como 0 (100 h y 40 h reales) y las dos
    # etiquetas están en el mapa que cita el guion. Se agrega directo sobre la
    # tabla de turnos, sumando cada columna de día por separado dentro de LA
    # MISMA fórmula (un SUMPRODUCT de un rango C×1 contra uno E:K de 7
    # columnas da #VALUE!: las dimensiones no casan) — así se evita también
    # la fila intermedia que causaba el bug original.
    _sp_obrador = '+'.join('SUMPRODUCT(--($C${a}:$C${b}="OBRADOR"),${c}${a}:'
                           '${c}${b})'.format(a=T_INI, b=T_FIN, c=c)
                           for c in COL_DIA)
    _sp_comercio = '+'.join('SUMPRODUCT(--($C${a}:$C${b}="COMERCIO"),${c}${a}:'
                            '${c}${b})'.format(a=T_INI, b=T_FIN, c=c)
                            for c in COL_DIA)
    res(T_TOT_OBR, 'Horas de obrador a la semana', '=' + _sp_obrador, FMT_ENT,
        'Son las que tienen que dar de sí para la producción que calcula el '
        'libro 1. Si no llegan, el problema no es el horno.')
    res(T_TOT_DES, 'Horas de despacho a la semana', '=' + _sp_comercio,
        FMT_ENT,
        'Mostrador y atención. En una pastelería de barrio la venta se '
        'concentra en dos franjas y en el sábado.')
    res(T_HUECOS, 'Días abiertos sin nadie en el mostrador',
        '=COUNTIF(${a}${c}:${b}${c},"SIN NADIE")'
        .format(a=COL_DIA[0], b=COL_DIA[6], c=T_COBER), FMT_ENT,
        'Tiene que ser cero antes de firmar los contratos. Es el fallo de '
        'dimensionado más caro y el más fácil de ver.')

    seccion(ws, 'A%d' % T_LIST_SEC, 'Lista (origen del desplegable)')
    cabecera(ws, T_LIST_CAB, [('A', 'Nº'), ('B', '¿Abre el despacho?')],
             altura=20)
    for i, opt in enumerate(SI_NO):
        motor.val(ws, 'A%d' % (T_LIST_INI + i), i + 1, fmt=FMT_ENT)
        motor.val(ws, 'B%d' % (T_LIST_INI + i), opt)

    parrafo(ws, T_NOTA,
            'El reparto de horas por día es un SUPUESTO que cuadra las horas '
            'contratadas de cada persona con los seis días de apertura. Tu '
            'reparto real depende de a qué hora entra el obrador (aquí, entre '
            'las 04:30 y las 05:00) y de dónde tengas los picos de venta. Lo '
            'que no cambia es la aritmética: si planificas más horas de las '
            'que contratas, la columna «Diferencia» lo dice.', col_fin='O',
            alto=40)
    parrafo(ws, T_NOTA + 1,
            'Esta hoja no es el cuadrante del día a día ni el registro de '
            'jornada, que es obligatorio y se lleva aparte. Es el dimensionado '
            'con el que se firman los contratos y se calcula el coste.',
            col_fin='O', alto=26)
    parrafo(ws, T_NOTA + 2,
            'Qué hace cada perfil en su turno está en el '
            '04-tareas-perfiles.xlsx del Kit de Tareas Pastelería (12 €): este '
            'libro no lo repite (regla R6 de la SPEC).', col_fin='O', alto=24)

    motor.dv_numerica(ws, verdes_horas, minimo=0, maximo=12,
                      titulo='Horas del día',
                      mensaje='Horas que hace esa persona ese día (0 a 12).')
    motor.dv_numerica(ws, verdes_contrato, minimo=0, maximo=48,
                      titulo='Horas contratadas',
                      mensaje='Horas semanales del contrato (0 a 48).')
    dv_rango(ws, verdes_abre,
             '$B${a}:$B${b}'.format(a=T_LIST_INI, b=T_LIST_FIN),
             'Sí o No', 'Elige Sí o No de la lista de esta hoja.')
    motor.regla_expresion(ws, 'N%d:N%d' % (T_INI, T_FIN),
                          '=AND(ISNUMBER($N{r}),$N{r}>0)'.format(r=T_INI))
    pie(ws, T_PIE)
    ws.freeze_panes = 'E%d' % T_INI
    pagina(ws, titulos='$%d:$%d' % (T_CAB, T_CAB), area='A1:O%d' % (T_PIE + 1))
    return ws


# --------------------------------------------------------------------------
# Hoja «Horas y Coste»
# --------------------------------------------------------------------------
C_CAB = 6
C_INI = 7
C_FIN = C_INI + N_PERS - 1                      # 11
C_TOT = C_FIN + 1                               # 12
C_RES = C_TOT + 2                               # 14
C_MES = C_RES + 1
C_ANIO = C_RES + 2
C_JORN = C_RES + 3
C_HORA = C_RES + 4
C_SS_EUR = C_RES + 5
C_BRUTO = C_RES + 6
C_LIST_SEC = C_BRUTO + 2
C_LIST_CAB = C_LIST_SEC + 1
C_LIST_INI = C_LIST_CAB + 1
C_LIST_FIN = C_LIST_INI + N_GRUPOS - 1
C_NOTA = C_LIST_FIN + 2
C_PIE = C_NOTA + 4


def hoja_coste(wb):
    ws = wb.create_sheet(H_COS)
    anchos(ws, {'A': 6, 'B': 24, 'C': 13, 'D': 34, 'E': 15, 'F': 13, 'G': 14,
                'H': 16, 'I': 15, 'J': 16, 'K': 16, 'L': 13, 'M': 30,
                'N': 34})
    encabezar(ws, 'Horas y coste de personal', col_fin='N',
              nota_txt='Del bruto de tabla al coste de empresa hay un 33 %: '
                       'quince pagas y la Seguridad Social a cargo de la '
                       'empresa. Es el número que se lleva al plan financiero, '
                       'no el bruto.')
    seccion(ws, 'A5', 'Coste persona a persona')
    cabecera(ws, C_CAB, [
        ('A', 'Id'), ('B', 'Persona (perfil del kit)'), ('C', 'Área'),
        ('D', 'Grupo de convenio'), ('E', 'Bruto mensual del grupo (€)'),
        ('F', 'Jornada equivalente'), ('G', 'Horas / semana'),
        ('H', 'Bruto mensual ajustado (€)'), ('I', 'Bruto anual (€)'),
        ('J', 'Coste empresa mes (€)'), ('K', 'Coste empresa año (€)'),
        ('L', 'Coste por hora (€)'), ('M', 'Aviso de jornada'),
        ('N', 'Aviso de SMI')], altura=44)
    verdes_grupo = []
    ss = "'{p}'!$C${r}".format(p=H_PAR, r=P_SS)
    pagas = "'{p}'!$C${r}".format(p=H_PAR, r=P_PAGAS)
    jornada_h = "'{p}'!$C${r}".format(p=H_PAR, r=P_JORNADA)
    horas_anio = "'{p}'!$C${r}".format(p=H_PAR, r=P_HORAS_ANIO)
    smi = "'{p}'!$C${r}".format(p=H_PAR, r=P_SMI)
    grupos_desc = "'{p}'!$B${a}:$B${b}".format(p=H_PAR, a=G_INI, b=G_FIN)
    grupos_bruto = "'{p}'!$C${a}:$C${b}".format(p=H_PAR, a=G_INI, b=G_FIN)
    for i, (pid, perfil, jornada, grupo, area, horas, turno) in \
            enumerate(PLANTILLA):
        r = C_INI + i
        motor.val(ws, 'A%d' % r, pid, align='center')
        motor.val(ws, 'B%d' % r, perfil)
        motor.val(ws, 'C%d' % r, area)
        motor.val(ws, 'D%d' % r, D.CONVENIO[grupo - 1][1], verde_=True)
        verdes_grupo.append('D%d' % r)
        motor.f(ws, 'E%d' % r,
                '=IFERROR(INDEX({gb},MATCH($D{r},{gd},0)),"")'
                .format(gb=grupos_bruto, gd=grupos_desc, r=r), fmt=FMT_EUR)
        motor.f(ws, 'G%d' % r, "='{t}'!$L${tr}".format(t=H_TUR,
                                                       tr=T_INI + i),
                fmt=FMT_ENT)
        motor.f(ws, 'F%d' % r,
                '=IFERROR(IF($G{r}="","",$G{r}/{j}),"")'.format(r=r,
                                                                j=jornada_h),
                fmt=FMT_DEC)
        motor.f(ws, 'H%d' % r,
                '=IFERROR(IF(OR($E{r}="",$F{r}=""),"",$E{r}*$F{r}),"")'
                .format(r=r), fmt=FMT_EUR)
        motor.f(ws, 'I%d' % r,
                '=IFERROR(IF($H{r}="","",$H{r}*{p}),"")'.format(r=r, p=pagas),
                fmt=FMT_EUR)
        motor.f(ws, 'K%d' % r,
                '=IFERROR(IF($I{r}="","",$I{r}*(1+{s})),"")'.format(r=r, s=ss),
                fmt=FMT_EUR)
        motor.f(ws, 'J%d' % r,
                '=IFERROR(IF($K{r}="","",$K{r}/12),"")'.format(r=r),
                fmt=FMT_EUR)
        motor.f(ws, 'L%d' % r,
                '=IFERROR(IF(OR($K{r}="",$F{r}=""),"",$K{r}/({h}*$F{r})),"")'
                .format(r=r, h=horas_anio), fmt=FMT_EUR)
        motor.f(ws, 'M%d' % r,
                '=IF($G{r}="","",IF($G{r}>{j},'
                '"Se pasa de la jornada completa",""))'.format(r=r,
                                                               j=jornada_h))
        motor.f(ws, 'N%d' % r,
                '=IFERROR(IF($E{r}="","",IF($E{r}*{p}<{s},'
                '"El grupo queda por debajo del SMI anual","")),"")'
                .format(r=r, p=pagas, s=smi))
        ws.row_dimensions[r].height = 24
    motor.val(ws, 'A%d' % C_TOT, 'TOTAL de la plantilla', bold=True)
    ws.merge_cells('A%d:D%d' % (C_TOT, C_TOT))
    for col, fmt in (('F', FMT_DEC), ('G', FMT_ENT), ('H', FMT_EUR),
                     ('I', FMT_EUR), ('J', FMT_EUR), ('K', FMT_EUR)):
        motor.f(ws, '%s%d' % (col, C_TOT),
                '=SUM(${c}${a}:${c}${b})'.format(c=col, a=C_INI, b=C_FIN),
                fmt=fmt, bold=True)
        ws['%s%d' % (col, C_TOT)].fill = PatternFill('solid', fgColor=CREMA)

    def res(fila, etiqueta, formula, fmt, nota):
        motor.val(ws, 'A%d' % fila, etiqueta, bold=True)
        ws.merge_cells('A%d:D%d' % (fila, fila))
        motor.f(ws, 'E%d' % fila, formula, fmt=fmt, bold=True)
        ws['E%d' % fila].fill = PatternFill('solid', fgColor=CREMA)
        ws.merge_cells('G%d:N%d' % (fila, fila))
        motor.val(ws, 'G%d' % fila, nota, wrap=True)
        ws['G%d' % fila].font = Font(italic=True, size=9)
        ws.row_dimensions[fila].height = 26

    seccion(ws, 'A%d' % C_RES, 'Lo que se lleva al plan financiero')
    res(C_MES, 'Coste de personal al mes (€)', '=$J${t}'.format(t=C_TOT),
        FMT_EUR,
        'Coste de empresa, con la Seguridad Social dentro. Es una de las dos '
        'partidas grandes de los gastos fijos del libro 5.')
    res(C_ANIO, 'Coste de personal al año (€)', '=$K${t}'.format(t=C_TOT),
        FMT_EUR,
        'El año de crucero completo. El primer año cuesta menos porque nadie '
        'entra el día 1: eso lo calcula la hoja «Plan de Contratación».')
    res(C_JORN, 'Jornadas equivalentes', '=$F${t}'.format(t=C_TOT), FMT_DEC1,
        'Cinco personas, 3,5 jornadas. Contar personas en vez de jornadas es '
        'el error que hace que un plan parezca sobredimensionado.')
    # Hallazgo B7 (2026-09-10): el pack publica tres costes por hora
    # distintos para la misma plantilla (14,89 € aquí; 17,94 € en el libro 4;
    # 13,36 € en el libro 3), los tres bien calculados pero con un
    # denominador distinto. El título deja claro que ÉSTE es PAGADO y medio de
    # TODA la plantilla, no el productivo de obrador del libro 4.
    res(C_HORA, 'Coste medio por hora PAGADA de la plantilla (€)',
        '=IFERROR(IF($F${t}=0,"",$K${t}/({h}*$F${t})),"")'
        .format(t=C_TOT, h=horas_anio), FMT_EUR,
        'Media de TODA la plantilla (obrador + despacho), sobre horas '
        'PAGADAS. NO es el «coste hora productiva de obrador» del libro 4 '
        '(17,94 €, carta-de-apertura-y-escandallo.xlsx, sólo obrador y sólo '
        'horas productivas) ni el «coste por hora PAGADA del refuerzo» del '
        'libro 3 (13,36 €, estacionalidad-y-picos.xlsx, sólo el grupo 5): las '
        'tres son correctas y miden un denominador distinto.')
    res(C_SS_EUR, 'Lo que cuesta la Seguridad Social al año (€)',
        '=IFERROR($K${t}-$I${t},"")'.format(t=C_TOT), FMT_EUR,
        'La diferencia entre lo que cobran y lo que pagas. No es negociable y '
        'no se puede olvidar.')
    res(C_BRUTO, 'Suma de los brutos anuales (€)', '=$I${t}'.format(t=C_TOT),
        FMT_EUR, 'Lo que perciben las cinco personas, antes de cotizaciones.')

    seccion(ws, 'A%d' % C_LIST_SEC,
            'Lista de grupos (origen del desplegable)')
    cabecera(ws, C_LIST_CAB, [('A', 'Grupo'), ('B', 'Descripción funcional')],
             altura=20)
    for i in range(N_GRUPOS):
        r = C_LIST_INI + i
        motor.f(ws, 'A%d' % r, "='{p}'!$A${g}".format(p=H_PAR, g=G_INI + i),
                fmt=FMT_ENT)
        motor.f(ws, 'B%d' % r, "='{p}'!$B${g}".format(p=H_PAR, g=G_INI + i))

    parrafo(ws, C_NOTA,
            'Las horas de la columna G se leen de la hoja «Turnos Semanales»: '
            'si cambias un turno, aquí cambia el coste. La jornada equivalente '
            'es horas planificadas partido por jornada completa, así que un '
            'contrato de 20 horas cuesta la mitad que uno de 40 del mismo '
            'grupo. Lo que no se prorratea es lo que no depende de la jornada: '
            'ropa de trabajo, formación y reconocimiento médico cuestan casi '
            'lo mismo para media jornada que para una completa.', col_fin='N',
            alto=44)
    parrafo(ws, C_NOTA + 1,
            'La Seguridad Social del 33 % es una aproximación de la cotización '
            'empresarial (contingencias comunes, desempleo, FOGASA y '
            'formación). Tu tipo real depende del contrato, de la actividad y '
            'de las bonificaciones que te apliquen: cámbialo en «Parámetros» y '
            'todo el libro se recalcula.', col_fin='N', alto=34)
    parrafo(ws, C_NOTA + 2,
            'Este libro no calcula nóminas ni cotizaciones exactas, y no '
            'sustituye a tu gestoría: calcula el DIMENSIONADO y su coste, que '
            'es lo que hay que saber antes de firmar el arrendamiento.',
            col_fin='N', alto=26)

    dv_rango(ws, verdes_grupo,
             '$B${a}:$B${b}'.format(a=C_LIST_INI, b=C_LIST_FIN),
             'Grupo de convenio',
             'Elige uno de los seis grupos de la lista de esta hoja.')
    motor.semaforo_texto(ws, 'M%d:M%d' % (C_INI, C_FIN),
                         (('Se pasa de la jornada completa', motor.CF_ROJO_BG,
                           motor.CF_ROJO_FG),))
    motor.semaforo_texto(ws, 'N%d:N%d' % (C_INI, C_FIN),
                         (('El grupo queda por debajo del SMI anual',
                           motor.CF_ROJO_BG, motor.CF_ROJO_FG),))
    pie(ws, C_PIE)
    ws.freeze_panes = 'E%d' % C_INI
    pagina(ws, titulos='$%d:$%d' % (C_CAB, C_CAB), area='A1:N%d' % (C_PIE + 1))
    return ws


# --------------------------------------------------------------------------
# Hoja «Plan de Contratación»
# --------------------------------------------------------------------------
A_CAB = 6
A_INI = 7
A_FIN = A_INI + N_PERS - 1                      # 11
A_TOT = A_FIN + 1                               # 12
R_SEC = A_TOT + 2                               # 14
R_CAB = R_SEC + 1
R_INI = R_CAB + 1
R_FIN = R_INI + N_PICOS - 1
R_TOT = R_FIN + 1
F_SEC = R_TOT + 2
F_ANIO1 = F_SEC + 1
F_REF = F_SEC + 2
F_TOTAL1 = F_SEC + 3
F_CRUCERO = F_SEC + 4
F_DIF = F_SEC + 5
F_VER = F_SEC + 6
A_LIST_SEC = F_VER + 2
A_LIST_CAB = A_LIST_SEC + 1
A_LIST_INI = A_LIST_CAB + 1
A_LIST_FIN = A_LIST_INI + N_GRUPOS - 1
A_NOTA = A_LIST_FIN + 2
A_PIE = A_NOTA + 4


def hoja_plan(wb):
    ws = wb.create_sheet(H_PLA)
    anchos(ws, {'A': 6, 'B': 26, 'C': 17, 'D': 11, 'E': 15, 'F': 18,
                'G': 17, 'H': 16, 'I': 14, 'J': 34, 'K': 52})
    encabezar(ws, 'Plan de contratación y refuerzo de campañas', col_fin='K',
              nota_txt='El primer año no cuesta lo que el año de crucero: '
                       'nadie entra el día 1 y las campañas se refuerzan. '
                       'Éstos son los dos números que van al plan financiero.')
    mes_ap = "'{p}'!$C${r}".format(p=H_PAR, r=P_MES_AP)
    horas_anio = "'{p}'!$C${r}".format(p=H_PAR, r=P_HORAS_ANIO)
    pagas = "'{p}'!$C${r}".format(p=H_PAR, r=P_PAGAS)
    ss = "'{p}'!$C${r}".format(p=H_PAR, r=P_SS)
    grupos_desc = "'{p}'!$B${a}:$B${b}".format(p=H_PAR, a=G_INI, b=G_FIN)
    grupos_bruto = "'{p}'!$C${a}:$C${b}".format(p=H_PAR, a=G_INI, b=G_FIN)

    seccion(ws, 'A5', 'Altas de la plantilla')
    cabecera(ws, A_CAB, [
        ('A', 'Id'), ('B', 'Persona (perfil del kit)'),
        ('C', 'Fecha de alta prevista'), ('D', 'Mes de alta'),
        ('E', 'Meses en el año 1'), ('F', 'Coste empresa mes (€)'),
        ('G', 'Coste del año 1 (€)'), ('H', 'Coste del año de crucero (€)'),
        ('I', 'Ahorro del año 1 (€)'), ('J', 'Por qué entra cuando entra'),
        ('K', 'Nota')], altura=40)
    verdes_fecha = []
    motivos = {
        'P1': 'Un mes antes de abrir: cierra la carta de apertura, hace las '
              'pruebas de producción y recibe la maquinaria.',
        'P2': 'Dos semanas antes: entra cuando ya hay obrador montado y hay '
              'que ensayar las tandas de verdad.',
        'P3': 'El día de la apertura: hasta que no hay producción diaria no '
              'hay nada que ayudar.',
        'P4': 'El día de la apertura, turno de mañana.',
        'P5': 'Tres meses después de abrir: el turno de tarde se abre cuando '
              'la venta de tarde lo justifica, y llega a tiempo para la '
              'campaña de Navidad.',
    }
    for i, (pid, perfil, jornada, grupo, area, horas, turno) in \
            enumerate(PLANTILLA):
        r = A_INI + i
        motor.val(ws, 'A%d' % r, pid, align='center')
        motor.val(ws, 'B%d' % r, perfil)
        motor.val(ws, 'C%d' % r, ALTAS[pid], fmt=motor.FMT_FECHA, verde_=True)
        verdes_fecha.append('C%d' % r)
        motor.f(ws, 'D%d' % r,
                '=IFERROR(IF($C{r}="","",MONTH($C{r})),"")'.format(r=r),
                fmt=FMT_ENT)
        motor.f(ws, 'E%d' % r,
                '=IFERROR(IF($D{r}="","",MIN(12,MAX(0,12-($D{r}-{m})))),"")'
                .format(r=r, m=mes_ap), fmt=FMT_ENT)
        motor.f(ws, 'F%d' % r, "='{c}'!$J${cr}".format(c=H_COS, cr=C_INI + i),
                fmt=FMT_EUR)
        motor.f(ws, 'G%d' % r,
                '=IFERROR(IF(OR($E{r}="",$F{r}=""),"",$E{r}*$F{r}),"")'
                .format(r=r), fmt=FMT_EUR)
        motor.f(ws, 'H%d' % r, "='{c}'!$K${cr}".format(c=H_COS, cr=C_INI + i),
                fmt=FMT_EUR)
        motor.f(ws, 'I%d' % r,
                '=IFERROR(IF(OR($G{r}="",$H{r}=""),"",$H{r}-$G{r}),"")'
                .format(r=r), fmt=FMT_EUR)
        motor.val(ws, 'J%d' % r, motivos[pid], wrap=True)
        motor.val(ws, 'K%d' % r,
                  'El alta en la Seguridad Social es PREVIA al inicio de la '
                  'prestación de servicios: se comunica antes de que la '
                  'persona empiece, no el mismo día.', wrap=True)
        ws.row_dimensions[r].height = 32
    motor.val(ws, 'A%d' % A_TOT, 'TOTAL de la plantilla', bold=True)
    ws.merge_cells('A%d:E%d' % (A_TOT, A_TOT))
    for col in ('F', 'G', 'H', 'I'):
        motor.f(ws, '%s%d' % (col, A_TOT),
                '=SUM(${c}${a}:${c}${b})'.format(c=col, a=A_INI, b=A_FIN),
                fmt=FMT_EUR, bold=True)
        ws['%s%d' % (col, A_TOT)].fill = PatternFill('solid', fgColor=CREMA)

    seccion(ws, 'A%d' % R_SEC, 'Refuerzo de las seis campañas')
    cabecera(ws, R_CAB, [
        ('A', 'Nº'), ('B', 'Campaña'), ('C', 'Fechas'), ('D', 'Mes'),
        ('E', 'Personas de refuerzo'), ('F', 'Horas por persona'),
        ('G', 'Grupo de convenio'), ('H', 'Coste por hora (€)'),
        ('I', 'Coste del refuerzo (€)'), ('J', 'Antelación de compra'),
        ('K', 'Nota')], altura=40)
    verdes_pers, verdes_horas_ref, verdes_grupo_ref = [], [], []
    for i, pico in enumerate(PICOS):
        r = R_INI + i
        motor.val(ws, 'A%d' % r, i + 1, fmt=FMT_ENT, align='center')
        motor.val(ws, 'B%d' % r, pico['nombre'])
        motor.val(ws, 'C%d' % r, pico['fechas'])
        motor.val(ws, 'D%d' % r, pico['mes'], fmt=FMT_ENT, align='center')
        motor.val(ws, 'E%d' % r, pico['refuerzo_personas'], fmt=FMT_ENT,
                  verde_=True, align='center')
        verdes_pers.append('E%d' % r)
        motor.val(ws, 'F%d' % r, pico['refuerzo_horas_persona'], fmt=FMT_ENT,
                  verde_=True, align='center')
        verdes_horas_ref.append('F%d' % r)
        motor.val(ws, 'G%d' % r, D.CONVENIO[GRUPO_REFUERZO - 1][1],
                  verde_=True)
        verdes_grupo_ref.append('G%d' % r)
        motor.f(ws, 'H%d' % r,
                '=IFERROR(INDEX({gb},MATCH($G{r},{gd},0))*{p}*(1+{s})/{h},"")'
                .format(gb=grupos_bruto, gd=grupos_desc, r=r, p=pagas, s=ss,
                        h=horas_anio), fmt=FMT_EUR)
        motor.f(ws, 'I%d' % r,
                '=IFERROR(IF(OR($E{r}="",$F{r}="",$H{r}=""),"",'
                '$E{r}*$F{r}*$H{r}),"")'.format(r=r), fmt=FMT_EUR)
        motor.val(ws, 'J%d' % r,
                  '%d semanas antes' % pico['antelacion_compra_semanas'])
        motor.val(ws, 'K%d' % r, pico['nota'][:300], wrap=True)
        ws.row_dimensions[r].height = 44
    motor.val(ws, 'A%d' % R_TOT, 'TOTAL del refuerzo de campañas', bold=True)
    ws.merge_cells('A%d:D%d' % (R_TOT, R_TOT))
    for col, fmt in (('E', FMT_ENT), ('F', FMT_ENT), ('I', FMT_EUR)):
        motor.f(ws, '%s%d' % (col, R_TOT),
                '=SUM(${c}${a}:${c}${b})'.format(c=col, a=R_INI, b=R_FIN),
                fmt=fmt, bold=True)
        ws['%s%d' % (col, R_TOT)].fill = PatternFill('solid', fgColor=CREMA)

    def res(fila, etiqueta, formula, fmt, nota):
        motor.val(ws, 'A%d' % fila, etiqueta, bold=True)
        ws.merge_cells('A%d:E%d' % (fila, fila))
        motor.f(ws, 'F%d' % fila, formula, fmt=fmt, bold=True)
        ws['F%d' % fila].fill = PatternFill('solid', fgColor=CREMA)
        ws.merge_cells('H%d:K%d' % (fila, fila))
        motor.val(ws, 'H%d' % fila, nota, wrap=True)
        ws['H%d' % fila].font = Font(italic=True, size=9)
        ws.row_dimensions[fila].height = 26

    seccion(ws, 'A%d' % F_SEC, 'Los dos números que van al plan financiero')
    res(F_ANIO1, 'Coste de la plantilla en el año 1 (€)',
        '=$G${t}'.format(t=A_TOT), FMT_EUR,
        'Sólo los meses que cada uno está de alta desde la apertura.')
    res(F_REF, 'Coste del refuerzo de campañas en un año (€)',
        '=$I${t}'.format(t=R_TOT), FMT_EUR,
        'Las seis campañas juntas. Se paga en el mes de la campaña o al '
        'siguiente: mira la tesorería del libro 5 justo ahí.')
    res(F_TOTAL1, 'Coste de personal acumulado del primer año (€)',
        '=IFERROR($F${a}+$F${b},"")'.format(a=F_ANIO1, b=F_REF), FMT_EUR,
        'Éste es el número del año 1. Es el que hay que meter en el plan, no '
        'el de crucero.')
    res(F_CRUCERO, 'Coste de personal del año de crucero (€)',
        "='{c}'!$E${r}".format(c=H_COS, r=C_ANIO), FMT_EUR,
        'Doce meses con toda la plantilla, sin refuerzo. Es el que se usa a '
        'partir del año 2.')
    res(F_DIF, 'Diferencia entre el año 1 y el de crucero (€)',
        '=IFERROR($F${a}-$F${b},"")'.format(a=F_TOTAL1, b=F_CRUCERO), FMT_EUR,
        'Negativo = el primer año cuesta menos porque no está todo el mundo '
        'los doce meses.')
    motor.val(ws, 'A%d' % F_VER, 'Veredicto del arranque', bold=True)
    ws.merge_cells('A%d:E%d' % (F_VER, F_VER))
    motor.f(ws, 'F%d' % F_VER,
            '=IF($F${d}="","",IF($F${d}<0,'
            '"El primer año ahorra en personal: no lo confundas con que el '
            'negocio vaya bien","El refuerzo se come el ahorro del arranque: '
            'revisa las campañas"))'.format(d=F_DIF), bold=True)
    ws['F%d' % F_VER].fill = PatternFill('solid', fgColor=CREMA)
    ws.merge_cells('H%d:K%d' % (F_VER, F_VER))
    motor.val(ws, 'H%d' % F_VER,
              'En el año 1 el ahorro de personal coincide con los meses en los '
              'que tampoco hay ventas: la rampa de arranque del libro 5 lo '
              'pone en su sitio.', wrap=True)
    ws['H%d' % F_VER].font = Font(italic=True, size=9)

    seccion(ws, 'A%d' % A_LIST_SEC,
            'Lista de grupos (origen del desplegable)')
    cabecera(ws, A_LIST_CAB,
             [('A', 'Grupo'), ('B', 'Descripción funcional')], altura=20)
    for i in range(N_GRUPOS):
        r = A_LIST_INI + i
        motor.f(ws, 'A%d' % r, "='{p}'!$A${g}".format(p=H_PAR, g=G_INI + i),
                fmt=FMT_ENT)
        motor.f(ws, 'B%d' % r, "='{p}'!$B${g}".format(p=H_PAR, g=G_INI + i))

    parrafo(ws, A_NOTA,
            'Las fechas de alta que vienen puestas son SUPUESTOS coherentes '
            'con el mes de apertura de «Parámetros»: el obrador entra antes '
            'porque hay que ensayar las tandas, y el despacho el mismo día. '
            'El cálculo de meses del año 1 cuenta desde el mes de apertura, '
            'con aritmética de meses y sin funciones de calendario.',
            col_fin='K', alto=40)
    parrafo(ws, A_NOTA + 1,
            'El refuerzo de campaña se calcula con el coste por hora del '
            'grupo que elijas, que ya lleva las quince pagas y la Seguridad '
            'Social dentro. San Valentín viene con cero personas de refuerzo a '
            'propósito: son dos días de ticket alto y poco volumen, y se '
            'aguanta con la plantilla. Reyes viene con tres, que es lo que '
            'pide multiplicar por seis la producción del obrador durante cinco '
            'días.', col_fin='K', alto=44)
    parrafo(ws, A_NOTA + 2,
            'Lo que este libro no decide: el TIPO de contrato del refuerzo. '
            'Eso depende de la causa que puedas acreditar y de tu convenio, y '
            'lo tiene que ver tu gestoría antes de la primera campaña, no '
            'durante.', col_fin='K', alto=30)

    motor.dv_fecha(ws, verdes_fecha)
    motor.dv_numerica(ws, verdes_pers, minimo=0, maximo=20,
                      titulo='Personas de refuerzo',
                      mensaje='Cuántas personas extra contratas (0 a 20).')
    motor.dv_numerica(ws, verdes_horas_ref, minimo=0, maximo=200,
                      titulo='Horas por persona',
                      mensaje='Horas de cada refuerzo en la campaña (0 a 200).')
    dv_rango(ws, verdes_grupo_ref,
             '$B${a}:$B${b}'.format(a=A_LIST_INI, b=A_LIST_FIN),
             'Grupo de convenio',
             'Elige uno de los seis grupos de la lista de esta hoja.')
    pie(ws, A_PIE)
    ws.freeze_panes = 'C%d' % A_INI
    pagina(ws, titulos='$%d:$%d' % (A_CAB, A_CAB), area='A1:K%d' % (A_PIE + 1))
    return ws


# --------------------------------------------------------------------------
def mapa_def():
    m = [
        ('Pagas del convenio de pastelería', H_PAR, 'C%d' % P_PAGAS,
         'parametro'),
        ('Bruto anual del grupo más bajo del convenio', H_PAR,
         'C%d' % P_MINCONV, 'salida'),
        ('Referencia anual del SMI', H_PAR, 'C%d' % P_SMI, 'parametro'),
        ('Veredicto de si manda el convenio o el SMI', H_PAR,
         'C%d' % P_AVISO_SMI, 'salida'),
        ('Seguridad Social a cargo de la empresa', H_PAR, 'C%d' % P_SS,
         'parametro'),
        ('Horas semanales de jornada completa', H_PAR, 'C%d' % P_JORNADA,
         'parametro'),
        ('Horas anuales de contrato', H_PAR, 'C%d' % P_HORAS_ANIO,
         'parametro'),
        ('Días de apertura a la semana', H_PAR, 'C%d' % P_DIAS, 'entrada'),
        ('Mes de apertura previsto', H_PAR, 'C%d' % P_MES_AP, 'entrada'),
        ('Horas planificadas a la semana', H_TUR, 'E%d' % T_TOT_SEM, 'salida'),
        ('Jornadas equivalentes de la plantilla', H_TUR, 'E%d' % T_TOT_JOR,
         'salida'),
        ('Horas de obrador a la semana', H_TUR, 'E%d' % T_TOT_OBR, 'salida'),
        ('Horas de despacho a la semana', H_TUR, 'E%d' % T_TOT_DES, 'salida'),
        ('Días abiertos sin nadie en el mostrador', H_TUR, 'E%d' % T_HUECOS,
         'salida'),
        ('Coste de personal al mes', H_COS, 'E%d' % C_MES, 'salida'),
        ('Coste de personal al año (crucero)', H_COS, 'E%d' % C_ANIO,
         'salida'),
        ('Jornadas equivalentes contabilizadas en el coste', H_COS,
         'E%d' % C_JORN, 'salida'),
        ('Coste medio por hora PAGADA de la plantilla', H_COS, 'E%d' % C_HORA,
         'salida'),
        ('Lo que cuesta la Seguridad Social al año', H_COS, 'E%d' % C_SS_EUR,
         'salida'),
        ('Suma de los brutos anuales de la plantilla', H_COS,
         'E%d' % C_BRUTO, 'salida'),
        ('Coste de la plantilla en el año 1', H_PLA, 'F%d' % F_ANIO1,
         'salida'),
        ('Coste del refuerzo de las seis campañas', H_PLA, 'F%d' % F_REF,
         'salida'),
        ('Coste de personal acumulado del primer año', H_PLA,
         'F%d' % F_TOTAL1, 'salida'),
        ('Coste de personal del año de crucero', H_PLA, 'F%d' % F_CRUCERO,
         'salida'),
        ('Diferencia entre el año 1 y el de crucero', H_PLA, 'F%d' % F_DIF,
         'salida'),
        ('Veredicto del arranque de personal', H_PLA, 'F%d' % F_VER, 'salida'),
        ('Personas de refuerzo en todo el año', H_PLA, 'E%d' % R_TOT,
         'salida'),
        ('Horas de refuerzo en todo el año', H_PLA, 'F%d' % R_TOT, 'salida'),
    ]
    for i, (n, desc, mes, anio, areas, puestos) in enumerate(D.CONVENIO):
        m.append(('Bruto mensual del grupo %d del convenio (%s)' % (n, desc),
                  H_PAR, 'C%d' % (G_INI + i), 'entrada'))
    for i, (pid, perfil, jornada, grupo, area, horas, turno) in \
            enumerate(PLANTILLA):
        m.append(('Coste de empresa al año de %s (%s)' % (perfil, pid), H_COS,
                  'K%d' % (C_INI + i), 'salida'))
        m.append(('Horas semanales planificadas de %s (%s)' % (perfil, pid),
                  H_TUR, 'L%d' % (T_INI + i), 'salida'))
    for i, pico in enumerate(PICOS):
        m.append(('Coste del refuerzo de %s' % pico['nombre'], H_PLA,
                  'I%d' % (R_INI + i), 'salida'))
    return m


# --------------------------------------------------------------------------
def construir():
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_parametros(wb)
    hoja_turnos(wb)
    hoja_coste(wb)
    hoja_plan(wb)

    verdes = {}
    for ws in wb.worksheets:
        motor.retirar_verde_de_calculadas(ws)
        verdes[ws.title] = motor.proteger(ws)

    wb.properties.creator = 'AI Chef Pro'
    wb.properties.lastModifiedBy = 'AI Chef Pro'
    wb.properties.title = TITULO
    wb.properties.subject = PRODUCTO + ' · Versión 1.0 · septiembre 2026'
    wb.calculation.fullCalcOnLoad = True

    destino = os.path.join(AQUI, 'build')
    if not os.path.isdir(destino):
        os.makedirs(destino)
    ruta = os.path.join(destino, NOMBRE + '.xlsx')
    wb.save(ruta)
    CP.barrer_cp1252(wb)
    return ruta, verdes


def gate_totales(ruta):
    """`=SUM(rango)` recalculado a mano contra el caché (hallazgo A1,
    2026-09-10): `pycel` cachea como 0 un `SUM` sobre una columna de
    `SUMPRODUCT`. Se llama DESPUÉS de `inject_cache.py`."""
    wbv = openpyxl.load_workbook(ruta, data_only=True)
    incoherentes = CP.gate_sum_rango(wbv)
    wbv.close()
    if incoherentes:
        raise SystemExit('TOTALES con caché incoherente:\n  '
                         + '\n  '.join(incoherentes))


def verificar(ruta):
    """`inject_cache.py` + comprobación `data_only` de TODAS las fórmulas.

    `inject_cache.py` NO inyecta cache cuando el resultado es la cadena vacía,
    así que un `None` en `data_only` puede ser un fallo o un «sin dato» legítimo
    (la SPEC exige «sin dato» = `""`, nunca 0). Se distinguen preguntándole a
    pycel: `''` es vacío A PROPÓSITO; cualquier otra cosa es un fallo.
    """
    from pycel import ExcelCompiler
    inject = os.path.join(RAIZ, 'inject_cache.py')
    salida = subprocess.check_output([sys.executable, inject, ruta])
    wb = openpyxl.load_workbook(ruta, data_only=True)
    sospechosas, errores = [], []
    for hoja, coord, formula in motor.REGISTRO:
        v = wb[hoja][coord].value
        if v is None:
            sospechosas.append((hoja, coord, formula))
        elif isinstance(v, str) and v.startswith('#'):
            errores.append('%s!%s  %s' % (hoja, coord, v))
    wb.close()
    vacias, a_proposito = [], []
    if sospechosas:
        c = ExcelCompiler(ruta)
        for hoja, coord, formula in sospechosas:
            try:
                v = c.evaluate("'%s'!%s" % (hoja, coord))
            except Exception as e:                            # noqa: BLE001
                v = 'ERROR ' + type(e).__name__ + ': ' + str(e)[:60]
            if isinstance(v, str) and v == '':
                a_proposito.append('%s!%s  %s' % (hoja, coord, formula[:60]))
            else:
                vacias.append('%s!%s  %s  -> %r'
                              % (hoja, coord, formula[:50], v))
    return salida.decode('utf-8', 'replace'), vacias, errores, a_proposito


def escribir_mapa(ruta):
    wb = openpyxl.load_workbook(ruta, data_only=True)
    mapa = {}
    for etiqueta, hoja, celda, tipo in mapa_def():
        v = wb[hoja][celda].value
        if hasattr(v, 'isoformat'):
            v = v.isoformat()
        mapa[etiqueta] = {'ref': '%s.xlsx!%s!%s' % (NOMBRE, hoja, celda),
                          'valor': v, 'tipo': tipo}
    wb.close()
    destino = os.path.join(AQUI, 'build', 'mapa-' + NOMBRE + '.json')
    with open(destino, 'w') as fh:
        json.dump(mapa, fh, ensure_ascii=False, indent=1)
    return mapa, destino


def demo(ruta):
    from pycel import ExcelCompiler
    out = []

    def eval_(c, hoja, celda):
        return c.evaluate("'%s'!%s" % (hoja, celda))

    # 1. El coste anual con SS coincide con datos_ejemplo.
    c = ExcelCompiler(ruta)
    anio = eval_(c, H_COS, 'E%d' % C_ANIO)
    ok1 = abs(anio - D.coste_personal_anual()) < 1.0
    out.append(('el coste de personal del año de crucero es %.2f € y cuadra '
                'con datos_ejemplo (%.2f €)' % (anio, D.coste_personal_anual()),
                ok1))

    # 2. La Seguridad Social está DENTRO: ponerla a cero baja el coste al bruto.
    c2 = ExcelCompiler(ruta)
    eval_(c2, H_COS, 'E%d' % C_ANIO)
    bruto = eval_(c2, H_COS, 'E%d' % C_BRUTO)
    eval_(c2, H_PAR, 'C%d' % P_SS)
    c2.set_value("'%s'!C%d" % (H_PAR, P_SS), 0)
    sin_ss = eval_(c2, H_COS, 'E%d' % C_ANIO)
    ok2 = abs(sin_ss - bruto) < 1.0
    out.append(('con la SS al 0 %% el coste anual baja de %.2f a %.2f €, que es '
                'la suma de los brutos' % (anio, sin_ss), ok2))

    # 3. Un TEXTO en una celda de horas no enciende el aviso de jornada.
    c3 = ExcelCompiler(ruta)
    eval_(c3, H_COS, 'M%d' % C_INI)
    c3.set_value("'%s'!E%d" % (H_TUR, T_INI), 'libre')
    aviso = eval_(c3, H_COS, 'M%d' % C_INI)
    ok3 = 'pasa de la jornada' not in str(aviso)
    out.append(('un texto en una casilla de horas deja el aviso de jornada en '
                '%r, no en rojo' % (aviso,), ok3))

    # 4. Pasar de jornada SÍ enciende el aviso.
    c4 = ExcelCompiler(ruta)
    eval_(c4, H_COS, 'M%d' % C_INI)
    c4.set_value("'%s'!E%d" % (H_TUR, T_INI), 12)
    c4.set_value("'%s'!F%d" % (H_TUR, T_INI), 12)
    c4.set_value("'%s'!G%d" % (H_TUR, T_INI), 12)
    c4.set_value("'%s'!H%d" % (H_TUR, T_INI), 12)
    aviso4 = eval_(c4, H_COS, 'M%d' % C_INI)
    ok4 = 'pasa de la jornada' in str(aviso4)
    out.append(('con 48 horas planificadas el aviso pasa a «%s»'
                % str(aviso4)[:40], ok4))

    # 5. El aviso de SMI no salta con Madrid y sí al bajar el grupo más bajo.
    c5 = ExcelCompiler(ruta)
    antes = eval_(c5, H_PAR, 'C%d' % P_AVISO_SMI)
    eval_(c5, H_PAR, 'C%d' % G_FIN)
    c5.set_value("'%s'!C%d" % (H_PAR, G_FIN), 900.0)
    despues = eval_(c5, H_PAR, 'C%d' % P_AVISO_SMI)
    ok5 = ('Manda el convenio' in str(antes)) and ('OJO' in str(despues))
    out.append(('el aviso del SMI pasa de «%s» a «%s» al bajar el grupo 6 a '
                '900 €' % (str(antes)[:28], str(despues)[:28]), ok5))

    # 6. El coste del refuerzo de Reyes reacciona a las personas de refuerzo.
    c6 = ExcelCompiler(ruta)
    reyes_antes = eval_(c6, H_PLA, 'I%d' % R_INI)
    eval_(c6, H_PLA, 'E%d' % R_INI)
    c6.set_value("'%s'!E%d" % (H_PLA, R_INI), 6)
    reyes_despues = eval_(c6, H_PLA, 'I%d' % R_INI)
    ok6 = reyes_despues > reyes_antes * 1.9
    out.append(('doblar el refuerzo de Reyes sube su coste de %.2f a %.2f €'
                % (reyes_antes, reyes_despues), ok6))
    return out


def main():
    ruta, verdes = construir()
    salida, vacias, errores, a_proposito = verificar(ruta)
    gate_totales(ruta)
    mapa, destino_mapa = escribir_mapa(ruta)
    pruebas = demo(ruta)

    print('escrito:', ruta)
    print(salida.strip())
    print('formulas registradas:', len(motor.REGISTRO))
    print('formulas vacías A PROPÓSITO («sin dato» = ""):', len(a_proposito))
    for v in a_proposito[:12]:
        print('   ', v)
    print('formulas sin valor cacheado:', len(vacias))
    for v in vacias[:12]:
        print('   ', v)
    print('formulas con error:', len(errores))
    for e in errores[:12]:
        print('   ', e)
    print('celdas verdes:', sum(verdes.values()))
    for hoja, n in verdes.items():
        print('   %-24s %d' % (hoja, n))
    print('notas legales:', NOTAS_LEGALES)
    print('mapa:', destino_mapa, '(%d etiquetas)' % len(mapa))
    print('demos:')
    for texto, ok in pruebas:
        print('   [%s] %s' % ('OK' if ok else 'FALLA', texto))
    if vacias or errores or not all(ok for _t, ok in pruebas):
        raise SystemExit('VERIFICACIÓN FALLIDA')


if __name__ == '__main__':
    main()
