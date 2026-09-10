#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_checklist-equipamiento-y-proveedores.py — libro 7 de «Cómo Montar una
Pastelería» (SPEC §2.2 fila 7; decisiones D17, D21, D22 y D29).

Hojas: Instrucciones · Equipamiento · Variante del Formato · Proveedores ·
Contador.

QUÉ DECIDE ESTE LIBRO
---------------------
Qué compras, a quién, a qué precio real y CON QUÉ PLAZO. Las dos columnas que
no trae ningún checklist de equipamiento del mercado son las que deciden de
verdad: la base fiscal de cada precio (D17: sin ella el CAPEX sale un 21 %
desviado) y el plazo de entrega, que es lo que mueve la fecha de apertura.

LO QUE NO HACE, Y DÓNDE SE HACE
-------------------------------
* **No calcula el CAPEX.** Eso es la `calculadora-capex-pasteleria.xlsx`
  (libro 2). Aquí el CAPEX de equipamiento entra como CELDA VERDE que el lector
  copia del libro 2, con valor por defecto declarado como supuesto (D21): cero
  fórmulas entre libros, ni siquiera dentro del mismo producto.
* **No es el plan de producción del kit** (`kit-tareas-pasteleria`): el kit
  organiza el obrador que ya tienes; este libro decide el que vas a comprar.
* **No publica los 22 proveedores sin verificar** del research: sólo los 9 con
  URL comprobada el 10-09-2026 (SPEC §2.2 fila 7).

DECISIONES TÉCNICAS
-------------------
* Todos los datos salen de `datos_ejemplo.EQUIPAMIENTO` y `PROVEEDORES`: aquí
  no se teclea ni un precio ni una URL.
* **Estado del checklist en palabras, no en símbolos.** El molde B histórico usa
  `☐`/`✓`, que NO son WinAnsi (cp1252) y el gate de la familia los marca. Se usa
  el vocabulario que ya existe en el catálogo (`checklist-equipamiento-obra` de
  dark-kitchen): Pendiente · Presupuestado · Pedido · Recibido · Instalado ·
  N/A. El estado terminal es «Instalado».
* Cero constantes dentro de las fórmulas: el tipo de IVA, la horquilla del
  precio de referencia, el umbral de desviación, las semanas que faltan hasta
  la apertura y el margen de seguridad viven en celdas verdes del bloque de
  parámetros y se referencian con `$` absolutos.
* Los agregados condicionales van con `SUMPRODUCT(--(rango=celda), …)`, que
  tolera el vacío; `COUNTIF` sólo con criterio literal fijo.
* `MAX` no admite condición sin fórmula matricial: el plazo crítico se calcula
  sobre una columna auxiliar declarada («Aux · plazo de las líneas críticas»),
  no con `MAXIFS` (que pycel no evalúa) ni con `NETWORKDAYS` (prohibida).
* Sin `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA`, `RANK`
  ni `NETWORKDAYS`. `IFERROR(...,"")` en todo cociente; «sin dato» = `""`;
  semáforos con `ISNUMBER`; desplegables contra RANGO.
* Ninguna celda verde vacía (D21): todas nacen con su valor por defecto y la
  nota que dice que es un supuesto.

Salida fija: `build/checklist-equipamiento-y-proveedores.xlsx` + su mapa.
Via: Claude Code
"""
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
# Constantes de familia
# --------------------------------------------------------------------------
PID = 'guia-pasteleria-obrador'
PRODUCTO = 'Cómo Montar una Pastelería'
TITULO = 'Checklist de equipamiento y proveedores'
NOMBRE = 'checklist-equipamiento-y-proveedores'
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
FMT_DEC = '#,##0.0'

ORO = 'FFD700'
CABECERA = '2D2D2D'
CREMA = 'FFF6DC'
GRIS = 'F2F2F2'

H_EQ = 'Equipamiento'
H_VAR = 'Variante del Formato'
H_PROV = 'Proveedores'
H_CONT = 'Contador'

# Vocabulario del checklist (WinAnsi; terminal = «Instalado»).
ESTADOS = ('Pendiente', 'Presupuestado', 'Pedido', 'Recibido', 'Instalado',
           'N/A')
ESTADO_DEFECTO = 'Pendiente'
PRIORIDADES = ('Crítico', 'Opcional')
BASES_IVA = ('sin IVA', 'con IVA', 'no declarada')
PROV_PENDIENTE = 'Pendiente: pide tres presupuestos'
SI_NO = ('Sí', 'No')

# Valores por defecto de las celdas verdes que no salen de `datos_ejemplo`
# (D21: ninguna vacía, y todas declaradas como supuesto).
HORQUILLA_DEFECTO = 0.25
UMBRAL_DESVIACION = 0.10
SEMANAS_HASTA_APERTURA = 20
SEMANAS_MARGEN = 2
PEDIDO_MINIMO_DEFECTO = 300.0
PLAZO_PROVEEDOR_DEFECTO = 7

# Las siete variantes de formato con equipo distinto, de PS-01…PS-11. La
# columna de aplicabilidad es CRITERIO DE LA CASA, no norma, y así se dice en
# la propia hoja.
VARIANTES = (
    ('Obrador en casa', 'PS-01',
     'Venta directa al consumidor final desde vivienda particular (art. 13 del '
     'RD 1021/2022). Inversión publicada: 3.000-5.000 € mínimo viable.'),
    ('Obrador a puerta cerrada', 'PS-02',
     'Producción sin venta al público. Inversión publicada: 8.000-12.000 € '
     'mínimo viable, 15.000-20.000 € completo.'),
    ('Local con venta (caso base)', 'PS-03',
     'El caso de «La Clara»: obrador propio más despacho a calle. Inversión '
     'publicada: 15.000-25.000 € mínimo viable, 30.000-50.000 €+ completo.'),
    ('Cafetería-pastelería', 'PS-04',
     'Con degustación. Inversión publicada: 60.000-80.000 € mínimo viable. '
     'Cambia el IVA de lo consumido en sala y puede cambiar el convenio.'),
    ('Punto caliente', 'PS-06',
     'Regenera producto congelado y no fabrica: no puede usar la mención '
     '«ELABORACIÓN PROPIA». Inversión publicada: 60.000-100.000 €.'),
    ('Obrador B2B para hostelería', 'PS-09',
     'Producción a volumen con venta a otros negocios: entra el art. 3 del '
     'RD 1021/2022, que resuelve el libro 6.'),
    ('Sin salida de humos', 'PS-11',
     'Hornos 100 % eléctricos y campana de condensación. Se ahorra el conducto '
     'de extracción, y condiciona el surtido: sin fritos.'),
)

#: Aplicabilidad de cada línea de equipamiento por variante, en el orden de
#: `VARIANTES`. Vocabulario: Sí / No / Depende. Es criterio de la casa.
APLICA = {
    1:  ('No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí'),
    2:  ('No', 'Depende', 'Sí', 'Sí', 'Depende', 'Sí', 'Sí'),
    3:  ('No', 'No', 'Sí', 'Sí', 'Sí', 'No', 'Sí'),
    4:  ('No', 'No', 'Depende', 'Depende', 'Depende', 'No', 'Depende'),
    5:  ('No', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí'),
    6:  ('No', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí'),
    7:  ('Depende', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí'),
    8:  ('No', 'Depende', 'Depende', 'Depende', 'No', 'Depende', 'Depende'),
    9:  ('No', 'Depende', 'Depende', 'Depende', 'No', 'Sí', 'Depende'),
    10: ('No', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí'),
    11: ('No', 'Sí', 'Sí', 'Sí', 'Depende', 'Sí', 'No'),
    12: ('No', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí'),
    13: ('No', 'Sí', 'Sí', 'Sí', 'Depende', 'Sí', 'Sí'),
    14: ('Depende', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí'),
    15: ('No', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí'),
    16: ('Depende', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí'),
    17: ('Depende', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí'),
    18: ('No', 'No', 'Sí', 'Sí', 'Sí', 'No', 'Sí'),
    19: ('Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí'),
    20: ('No', 'No', 'Sí', 'Sí', 'Sí', 'No', 'Sí'),
    21: ('Depende', 'Sí', 'Sí', 'Sí', 'Depende', 'Sí', 'Sí'),
    22: ('Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí'),
}
VAR_BASE = 2                      # índice de «Local con venta (caso base)»

EQUIPOS = list(D.EQUIPAMIENTO)
N_EQ = len(EQUIPOS)
BLOQUES = []
for _e in EQUIPOS:
    if _e['bloque_capex'] not in BLOQUES:
        BLOQUES.append(_e['bloque_capex'])
CATEGORIAS = []
for _e in EQUIPOS:
    if _e['categoria'] not in CATEGORIAS:
        CATEGORIAS.append(_e['categoria'])

CAPEX2_DEFECTO = round(
    D.equipamiento_bloque_sin_iva('Equipamiento de obrador')
    + D.equipamiento_bloque_sin_iva('Tienda y vitrina'), 2)

# Gate legal ANTES de escribir una sola nota (SPEC §2.2).
IDS_LEGALES = ('PA-36', 'PA-37', 'PA-13', 'PA-12')
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
    ws.page_setup.paperSize = 9                       # A4
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
    """Desplegable contra un RANGO de la propia hoja (SPEC §2.2: nunca una
    lista de opciones separadas por comas)."""
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
    """Adjunta a la celda la nota legal «Verificado el … · norma · URL»."""
    global NOTAS_LEGALES
    texto = D.nota_legal(id_pa)
    if not texto:
        raise SystemExit('sin nota legal para ' + id_pa)
    if extra:
        texto = extra + ' — ' + texto
    ws[coord].comment = Comment(texto, 'AI Chef Pro', height=140, width=460)
    NOTAS_LEGALES += 1
    return texto


def pie(ws, fila, col_fin='F'):
    motor.val(ws, 'A%d' % fila, BIO)
    ws['A%d' % fila].font = Font(italic=True, size=9)
    motor.val(ws, 'A%d' % (fila + 1), VERSION_LINE)
    ws['A%d' % (fila + 1)].font = Font(size=8, italic=True)


# --------------------------------------------------------------------------
# Hoja «Instrucciones»
# --------------------------------------------------------------------------
PASOS = [
    '1. Hoja «Equipamiento»: la dotación completa de una pastelería con '
    'obrador, línea a línea. Empieza por el bloque verde de arriba: el tipo de '
    'IVA, la horquilla con la que quieres ver el precio de referencia, el '
    'CAPEX de equipamiento que te dio el libro 2, el umbral de desviación que '
    'te permites y las semanas que faltan hasta la apertura que tienes en la '
    'cabeza. Todo lo demás de la hoja se recalcula con eso.',
    '2. En cada línea escribe tres cosas: el precio real que te han '
    'presupuestado (SIN IVA), quién te lo vende y en cuántas semanas te lo '
    'entrega. Las tres vienen rellenas con un valor por defecto para que veas '
    'la hoja funcionando; los tres son supuestos y hay que sustituirlos.',
    '3. Marca el estado de cada línea (Pendiente, Presupuestado, Pedido, '
    'Recibido, Instalado o N/A). «N/A» es lo que tu formato no necesita, y no '
    'cuenta ni a favor ni en contra del avance.',
    '4. Hoja «Variante del Formato»: elige arriba qué vas a montar y la hoja te '
    'dice qué líneas de la dotación te sobran, cuáles te faltan y cuánto '
    'cuesta esa variante frente al caso base. Es la hoja que evita comprar el '
    'equipo de otro negocio.',
    '5. Hoja «Proveedores»: los nueve proveedores con URL comprobada el '
    '10-09-2026, con columnas verdes para tu contacto, tu pedido mínimo, tu '
    'plazo y tus condiciones de pago. Los 22 que el research recogió sin '
    'verificar no se publican: un directorio con un enlace roto vale menos que '
    'uno corto.',
    '6. Hoja «Contador»: el avance del checklist, el avance de lo CRÍTICO (que '
    'es el que decide si puedes abrir), el reparto por bloque de CAPEX y por '
    'categoría, y lo negociado contra lo de referencia.',
]

NOTAS_LIBRO = [
    'LA COLUMNA QUE MÁS DINERO MUEVE ES «¿Lleva IVA?». Unos distribuidores '
    'publican con IVA y otros sin él, y hay fichas que no lo dicen. Mezclarlos '
    'desvía la inversión un 21 %: sobre esta dotación son más de 14.000 € de '
    'diferencia entre hacerlo bien y hacerlo a ojo. Todas las cifras que suma '
    'este libro están llevadas a base imponible, y el IVA soportado se calcula '
    'aparte porque hay que ADELANTARLO aunque luego se recupere.',
    'EL PLAZO DE ENTREGA ES UNA DECISIÓN, NO UN DATO. Ningún distribuidor lo '
    'publica: los que trae la hoja son supuestos. Pero el plazo más largo de lo '
    'que no puedes dejar de comprar es el que fija tu fecha de apertura, y por '
    'eso la hoja lo calcula, dice qué línea lo marca y avisa si se te come el '
    'calendario. Se pide antes lo que tarda, no lo que ilusiona.',
    'EL PRECIO DE REFERENCIA NO ES TU PRECIO. Nueve líneas traen precio '
    'publicado por un distribuidor y trece traen un supuesto, porque en '
    'maquinaria de obrador se vende por presupuesto. La columna verde «precio '
    'real negociado» es la única que cuenta para tus totales: pide tres '
    'presupuestos por línea y escríbelos aquí.',
    'ESTE LIBRO NO CALCULA TU CAPEX. Eso lo hace la calculadora de CAPEX del '
    'libro 2, que además reparte la inversión por bloques, calcula el IVA '
    'soportado y compara traspaso contra obra nueva. Aquí sólo se compara: '
    'copia su total de equipamiento en la celda verde de arriba y esta hoja te '
    'dice cuánto te estás desviando. No hay ni una fórmula que apunte a otro '
    'fichero: un enlace entre libros se rompe en cuanto alguien mueve una '
    'carpeta, y entonces el libro miente sin avisar.',
    'LA ATEMPERADORA DE CHOCOLATE Y EL HORNO DE PISOS ESTÁN MARCADOS COMO '
    'OPCIONALES a propósito. Son las dos compras que más se discuten y las dos '
    'que más se compran de más: sólo entran si abres línea de bombonería o si '
    'tu volumen de pan y bollería lo justifica. Por eso quedan fuera del plazo '
    'crítico y del subtotal comparable.',
]


def hoja_instrucciones(wb):
    ws = wb.create_sheet('Instrucciones', 0)
    anchos(ws, {'A': 48, 'B': 48, 'C': 48})
    motor.val(ws, 'A1', TITULO)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', SUBTITULO)
    motor.val(ws, 'A3', 'Para qué sirve: decidir qué equipo compras, a quién, '
                        'a qué precio real y con qué plazo de entrega.')
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

    seccion(ws, 'A%d' % fila, 'Lo que conviene saber antes de empezar')
    fila += 1
    for texto in NOTAS_LIBRO:
        ws.merge_cells('A%d:C%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, texto, wrap=True)
        ws.row_dimensions[fila].height = 72
        fila += 1
    fila += 1

    seccion(ws, 'A%d' % fila, 'Cada cuánto se usa este libro')
    fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila,
              'Cadencia: TODAS LAS SEMANAS desde que decides el local hasta el '
              'día que abres, que es cuando el checklist se cierra. Después, '
              'una vez al año para las reposiciones y cuando cambies de '
              'proveedor. La hoja «Proveedores» sí se mantiene viva: cada vez '
              'que negocias condiciones nuevas, se anotan aquí.', wrap=True)
    ws.row_dimensions[fila].height = 44
    fila += 2

    seccion(ws, 'A%d' % fila, 'La frontera con el Kit de Tareas Pastelería '
                              '(12 €) y con el resto del pack')
    fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila,
              'El Kit de Tareas Pastelería organiza el obrador que YA tienes: '
              'plan de producción, encargos, alérgenos de vitrina y registro '
              'de temperaturas. Este libro decide el obrador que vas a '
              'comprar, y son dos preguntas distintas. Si ya tienes el kit, '
              'ninguna de sus quince plantillas se solapa con esta hoja. Y '
              'dentro de este mismo pack: el libro 1 dice si el local aguanta '
              'la producción, el libro 2 pone la inversión completa con su IVA '
              'y su tesorería, y el libro 6 encadena los plazos hasta la fecha '
              'de apertura. Éste es el que se lleva a la feria y al '
              'distribuidor.', wrap=True)
    ws.row_dimensions[fila].height = 72
    fila += 2

    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila, NOTA_DESPROTEGER, wrap=True)
    fila += 2
    pie(ws, fila, col_fin='C')
    pagina(ws, apaisado=False)
    return ws


# --------------------------------------------------------------------------
# Hoja «Equipamiento»
# --------------------------------------------------------------------------
P_IVA, P_HORQ, P_CAPEX2 = 7, 8, 9
P_UMBRAL, P_SEM, P_MARGEN = 10, 11, 12
EQ_SEC = 14
EQ_CAB = 15
EQ_INI = 16
EQ_FIN = EQ_INI + N_EQ - 1                       # 37
RES_SEC = EQ_FIN + 2                             # 39
R_LINEAS = RES_SEC + 1                           # 40
R_REF_CRIT = R_LINEAS + 1
R_REF_TODO = R_LINEAS + 2
R_REAL_CRIT = R_LINEAS + 3
R_REAL_TODO = R_LINEAS + 4
R_DIF_NEG = R_LINEAS + 5
R_IVA_SOP = R_LINEAS + 6
R_DESEMB = R_LINEAS + 7
R_CAPEX2 = R_LINEAS + 8
R_DESV_EUR = R_LINEAS + 9
R_DESV_PCT = R_LINEAS + 10
#: Fila añadida en la corrección del 2026-09-10 (hallazgo A2): explicita que la
#: desviación de I49/I50 son exactamente los opcionales, no un fallo de
#: negociación.
R_DIF_OPC = R_LINEAS + 11
R_VER_DESV = R_LINEAS + 12
R_PLAZO = R_LINEAS + 13
R_PLAZO_LIN = R_LINEAS + 14
R_MARGEN = R_LINEAS + 15
R_VER_PLAZO = R_LINEAS + 16
R_TARDE = R_LINEAS + 17                          # 57
LI_SEC = R_TARDE + 2                             # 59
LI_CAB = LI_SEC + 1                              # 60
LI_INI = LI_CAB + 1                              # 61
LI_FIN = LI_INI + len(ESTADOS) - 1               # 65
C_CRIT = '$C$%d' % LI_INI
C_OPC = '$C$%d' % (LI_INI + 1)
C_CONIVA = '$E$%d' % (LI_INI + 1)
C_INSTAL = '$A$%d' % (LI_INI + 4)
C_NA = '$A$%d' % (LI_INI + 5)
C_PROVPTE = '$G$%d' % LI_INI
EQ_NOTA = LI_FIN + 2
EQ_PIE = EQ_NOTA + 5

COLS_EQ = [
    ('A', 'Estado'), ('B', 'Nº'), ('C', 'Partida'), ('D', 'Marca'),
    ('E', 'Modelo'), ('F', 'Categoría'), ('G', 'Bloque de CAPEX'),
    ('H', 'Prioridad'), ('I', 'Precio de referencia (€)'),
    ('J', '¿Lleva IVA?'), ('K', 'Tipo de IVA (%)'),
    ('L', 'Precio de referencia SIN IVA (€)'), ('M', 'Mínimo estimado (€)'),
    ('N', 'Máximo estimado (€)'),
    ('O', 'Precio real negociado (€, sin IVA)'),
    ('P', 'Desviación sobre la referencia (%)'), ('Q', 'Proveedor'),
    ('R', 'Plazo de entrega (semanas)'),
    ('S', 'Margen hasta la apertura (semanas)'),
    ('T', 'Aux · plazo de las líneas críticas'),
    ('U', 'Aux · ¿el plazo se pasa? (1 = sí)'), ('V', 'Fuente del precio'),
    ('W', 'Nota'),
]


def hoja_equipamiento(wb):
    ws = wb.create_sheet(H_EQ)
    anchos(ws, {'A': 15, 'B': 5, 'C': 46, 'D': 14, 'E': 22, 'F': 20, 'G': 22,
                'H': 11, 'I': 15, 'J': 12, 'K': 11, 'L': 16, 'M': 14,
                'N': 14, 'O': 17, 'P': 13, 'Q': 26, 'R': 12, 'S': 14,
                'T': 12, 'U': 12, 'V': 30, 'W': 74})
    encabezar(ws, 'Equipamiento, línea a línea', col_fin='W',
              nota_txt='Los precios de referencia salen de fichas de '
                       'distribuidor leídas el 10-09-2026 (nueve líneas) o son '
                       'supuestos declarados (trece). Cada uno con SU base '
                       'fiscal: mezclarlas desvía la inversión un 21 %.')

    # --- parámetros ------------------------------------------------------
    seccion(ws, 'A5', 'Parámetros de esta hoja')
    cabecera(ws, 6, [('A', 'Parámetro'), ('C', 'Valor'), ('D', 'Nota')],
             altura=20)
    ws.merge_cells('A6:B6')
    ws.merge_cells('D6:W6')

    def par(fila, etiqueta, valor, fmt, nota):
        ws.merge_cells('A%d:B%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, etiqueta, bold=True)
        motor.val(ws, 'C%d' % fila, valor, fmt=fmt, verde_=True)
        ws.merge_cells('D%d:W%d' % (fila, fila))
        motor.val(ws, 'D%d' % fila, nota, wrap=True)
        ws['D%d' % fila].font = Font(italic=True, size=9)
        ws.row_dimensions[fila].height = 26

    par(P_IVA, 'Tipo de IVA general (%)', D.P('iva_equipamiento'), FMT_PCT,
        'Tipo general del art. 90.Uno de la Ley 37/1992. La maquinaria y el '
        'mobiliario van al 21 %: no hay tipo reducido para el equipamiento de '
        'un obrador. Cámbialo aquí y se recalcula toda la columna.')
    nota_celda(ws, 'C%d' % P_IVA, 'PA-36',
               'Tipo general del IVA sobre la maquinaria (21 %)')
    par(P_HORQ, 'Horquilla del precio de referencia (±%)', HORQUILLA_DEFECTO,
        FMT_PCT,
        'SUPUESTO. Con cuánta amplitud quieres ver el mínimo y el máximo '
        'alrededor del precio de referencia. El 25 % es la banda que se mueve '
        'entre lo que pide una ficha web y lo que se cierra con tres '
        'presupuestos; súbela si compras a un solo distribuidor.')
    par(P_CAPEX2, 'Total de CAPEX de equipamiento del libro 2 (€, sin IVA)',
        CAPEX2_DEFECTO, FMT_EUR,
        'CÓPIALO DE «calculadora-capex-pasteleria.xlsx» (libro 2), bloques '
        '«Equipamiento de obrador» y «Tienda y vitrina». Viene relleno con el '
        'valor del caso «La Clara» como SUPUESTO, para que la hoja funcione '
        'antes de que abras el libro 2. No hay ninguna fórmula entre libros: '
        'esto es una copia declarada, no un vínculo.')
    par(P_UMBRAL, 'Umbral de desviación admitida (%)', UMBRAL_DESVIACION,
        FMT_PCT,
        'SUPUESTO. Por encima de esta desviación contra el CAPEX del libro 2, '
        'la hoja lo marca en rojo: o has comprado de más, o el plan financiero '
        'del libro 5 está calculado con una inversión que ya no es la tuya.')
    par(P_SEM, 'Semanas que faltan hasta la apertura prevista',
        SEMANAS_HASTA_APERTURA, FMT_ENT,
        'SUPUESTO. Cuenta desde hoy hasta la fecha que tienes en la cabeza. El '
        'cronograma completo, con la ruta crítica de licencias y obra, lo '
        'calcula la hoja «Cronograma y Ruta Crítica» del libro 6.')
    par(P_MARGEN, 'Margen de seguridad entre la entrega y la apertura '
                  '(semanas)', SEMANAS_MARGEN, FMT_ENT,
        'SUPUESTO. Lo que necesitas entre que llega la máquina y que abres: '
        'montaje, conexión, puesta en marcha y las pruebas de producción. Con '
        'menos de dos semanas, la primera avería te pilla con la tienda '
        'abierta.')

    # --- tabla -----------------------------------------------------------
    seccion(ws, 'A%d' % EQ_SEC, 'La dotación completa, línea a línea')
    cabecera(ws, EQ_CAB, COLS_EQ, altura=46)
    verdes_estado, verdes_precio, verdes_prov, verdes_plazo = [], [], [], []
    for i, eq in enumerate(EQUIPOS):
        r = EQ_INI + i
        prioridad = PRIORIDADES[1] if eq['opcional'] else PRIORIDADES[0]
        ref = eq['valor_verificado'] if eq['valor_verificado'] is not None \
            else eq['supuesto_por_defecto']
        sin_iva = round(D.precio_equipamiento_sin_iva(eq), 2)
        motor.val(ws, 'A%d' % r, ESTADO_DEFECTO, verde_=True)
        verdes_estado.append('A%d' % r)
        motor.val(ws, 'B%d' % r, eq['n'], fmt=FMT_ENT)
        motor.val(ws, 'C%d' % r, eq['partida'], wrap=True)
        motor.val(ws, 'D%d' % r, eq['marca'] or '')
        motor.val(ws, 'E%d' % r, eq['modelo'] or '')
        motor.val(ws, 'F%d' % r, eq['categoria'])
        motor.val(ws, 'G%d' % r, eq['bloque_capex'])
        motor.val(ws, 'H%d' % r, prioridad)
        motor.val(ws, 'I%d' % r, ref, fmt=FMT_EUR)
        motor.val(ws, 'J%d' % r, eq['base_iva'])
        motor.f(ws, 'K%d' % r, '=$C$%d' % P_IVA, fmt=FMT_PCT)
        motor.f(ws, 'L%d' % r,
                '=IFERROR(IF($I{r}="","",IF($J{r}={ci},$I{r}/(1+$K{r}),'
                '$I{r})),"")'.format(r=r, ci=C_CONIVA), fmt=FMT_EUR)
        motor.f(ws, 'M%d' % r,
                '=IF($L{r}="","",$L{r}*(1-$C${h}))'.format(r=r, h=P_HORQ),
                fmt=FMT_EUR)
        motor.f(ws, 'N%d' % r,
                '=IF($L{r}="","",$L{r}*(1+$C${h}))'.format(r=r, h=P_HORQ),
                fmt=FMT_EUR)
        motor.val(ws, 'O%d' % r, sin_iva, fmt=FMT_EUR, verde_=True)
        verdes_precio.append('O%d' % r)
        motor.f(ws, 'P%d' % r,
                '=IFERROR(IF(OR($O{r}="",$L{r}=""),"",$O{r}/$L{r}-1),"")'
                .format(r=r), fmt=FMT_PCT)
        motor.val(ws, 'Q%d' % r, eq['marca'] or PROV_PENDIENTE, verde_=True)
        verdes_prov.append('Q%d' % r)
        motor.val(ws, 'R%d' % r, eq['plazo_semanas'], fmt=FMT_ENT, verde_=True)
        verdes_plazo.append('R%d' % r)
        motor.f(ws, 'S%d' % r,
                '=IFERROR(IF(OR($R{r}="",$C${s}="",$C${m}=""),"",'
                '$C${s}-$R{r}-$C${m}),"")'.format(r=r, s=P_SEM, m=P_MARGEN),
                fmt=FMT_ENT)
        motor.f(ws, 'T%d' % r,
                '=IF($H{r}={cr},$R{r},"")'.format(r=r, cr=C_CRIT),
                fmt=FMT_ENT)
        motor.f(ws, 'U%d' % r,
                '=IF($S{r}="","",IF($S{r}<0,1,0))'.format(r=r), fmt=FMT_ENT)
        motor.val(ws, 'V%d' % r, eq['fuente'])
        motor.val(ws, 'W%d' % r, eq['nota'] or '', wrap=True)
        ws.row_dimensions[r].height = 34
        if eq['n'] == 5:
            nota_celda(ws, 'C%d' % r, 'PA-13',
                       'El abatidor no es un capricho: el art. 5 exige llegar '
                       'a -18 °C en el centro con descenso ininterrumpido')
        if eq['n'] == 13:
            nota_celda(ws, 'C%d' % r, 'PA-12',
                       'La cámara es la que sostiene los 4 °C de lo relleno')
        if eq['n'] == 19:
            nota_celda(ws, 'C%d' % r, 'PA-37',
                       'El software que compres hoy ya tiene que estar '
                       'adaptado: la obligación del fabricante es anterior a '
                       'la tuya')

    # --- resumen ---------------------------------------------------------
    rng = lambda col: '${c}${a}:${c}${b}'.format(c=col, a=EQ_INI, b=EQ_FIN)

    def res(fila, etiqueta, formula, fmt, nota):
        ws.merge_cells('A%d:H%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, etiqueta, bold=True)
        motor.f(ws, 'I%d' % fila, formula, fmt=fmt, bold=True)
        ws['I%d' % fila].fill = PatternFill('solid', fgColor=CREMA)
        ws.merge_cells('K%d:W%d' % (fila, fila))
        motor.val(ws, 'K%d' % fila, nota, wrap=True)
        ws['K%d' % fila].font = Font(italic=True, size=9)
        ws.row_dimensions[fila].height = 24

    seccion(ws, 'A%d' % RES_SEC, 'Resumen de esta hoja')
    res(R_LINEAS, 'Líneas del checklist',
        '=COUNTIF(%s,"<>")' % rng('C'), FMT_ENT,
        'Las 22 líneas de la dotación tipo de una pastelería con obrador.')
    res(R_REF_CRIT, 'Total de referencia sin IVA, sólo líneas críticas (€)',
        '=SUMPRODUCT(--({h}={cr}),{l})'.format(h=rng('H'), cr=C_CRIT,
                                               l=rng('L')), FMT_EUR,
        'Lo que cuesta lo que no puedes dejar de comprar, a precio de '
        'referencia y en base imponible.')
    res(R_REF_TODO, 'Total de referencia sin IVA, todas las líneas (€)',
        '=SUM(%s)' % rng('L'), FMT_EUR,
        'Con la atemperadora de chocolate y el horno de pisos dentro, que son '
        'opcionales según el concepto.')
    res(R_REAL_CRIT, 'Total real negociado sin IVA, sólo líneas críticas (€)',
        '=SUMPRODUCT(--({h}={cr}),{o})'.format(h=rng('H'), cr=C_CRIT,
                                               o=rng('O')), FMT_EUR,
        'Lo mismo con TUS precios: es el número que se lleva al libro 2.')
    res(R_REAL_TODO, 'Total real negociado sin IVA, todas las líneas (€)',
        '=SUM(%s)' % rng('O'), FMT_EUR,
        'La base imponible de toda la compra de equipamiento.')
    res(R_DIF_NEG, 'Lo que has ganado (o perdido) negociando (€)',
        '=IFERROR($I${a}-$I${b},"")'.format(a=R_REAL_TODO, b=R_REF_TODO),
        FMT_EUR,
        'Negativo = has comprado por debajo del precio de referencia. Es el '
        'único sitio del pack donde se mide lo que vale pedir tres '
        'presupuestos.')
    res(R_IVA_SOP, 'IVA soportado sobre el precio real (€)',
        '=SUMPRODUCT({o},{k})'.format(o=rng('O'), k=rng('K')), FMT_EUR,
        'Se recupera vía declaraciones, pero hay que ADELANTARLO el día que '
        'pagas la máquina. La hoja «IVA y Tesorería» del libro 2 dice cuándo '
        'vuelve.')
    res(R_DESEMB, 'Desembolso real con IVA (€)',
        '=IFERROR($I${a}+$I${b},"")'.format(a=R_REAL_TODO, b=R_IVA_SOP),
        FMT_EUR, 'Lo que sale de la cuenta corriente.')
    res(R_CAPEX2, 'Total de CAPEX de equipamiento del libro 2 (€, sin IVA)',
        '=$C$%d' % P_CAPEX2, FMT_EUR,
        'Copia de la celda verde de arriba, que a su vez copias del libro 2.')
    # Hallazgo A2 (2026-09-10): C9/P_CAPEX2 se copia de los bloques del libro 2
    # que EXCLUYEN los tres opcionales (nota D9), así que la desviación tiene
    # que compararse contra R_REAL_CRIT (sólo líneas críticas), no contra
    # R_REAL_TODO (que sí las incluye). Con R_REAL_TODO, el ejemplo publicado
    # salía con +19.520,40 € / +29,1 % y un veredicto rojo falso: esos
    # 19.520,40 € son exactamente el precio de los tres opcionales, no una
    # desviación de negociación.
    res(R_DESV_EUR, 'Desviación contra el libro 2 (€)',
        '=IFERROR(IF($C${p}="","",$I${a}-$C${p}),"")'
        .format(p=P_CAPEX2, a=R_REAL_CRIT), FMT_EUR,
        'Positivo = estás comprando más equipo crítico del que había '
        'presupuestado el plan. No incluye los opcionales: mira la fila de '
        'abajo si quieres ese número.')
    res(R_DESV_PCT, 'Desviación contra el libro 2 (%)',
        '=IFERROR(IF($C${p}="","",$I${a}/$C${p}-1),"")'
        .format(p=P_CAPEX2, a=R_REAL_CRIT), FMT_PCT,
        'Se pinta en rojo si se pasa del umbral que has fijado arriba.')
    res(R_DIF_OPC, 'Diferencia por líneas opcionales (€)',
        '=IFERROR($I${a}-$I${b},"")'.format(a=R_REAL_TODO, b=R_REAL_CRIT),
        FMT_EUR,
        'Lo que cuestan la atemperadora, el horno de pisos y las puertas '
        'correderas si decides llevártelos: NO es un descuadre, es tu '
        'elección de ampliar el concepto.')
    res(R_VER_DESV, 'Veredicto de la desviación',
        '=IF($I${d}="","",IF(OR($I${d}>$C${u},$I${d}<-$C${u}),'
        '"Fuera del umbral: rehaz el CAPEX del libro 2 con estos precios",'
        '"En línea con el CAPEX del libro 2"))'
        .format(d=R_DESV_PCT, u=P_UMBRAL), None,
        'Compara sólo líneas críticas contra líneas críticas. El plan '
        'financiero del libro 5 se calcula sobre el CAPEX del libro 2: si '
        'esto se sale, hay que rehacer los dos, no cambiar este número.')
    res(R_PLAZO, 'Plazo crítico de entrega (semanas)',
        '=IFERROR(MAX(%s),"")' % rng('T'), FMT_ENT,
        'El plazo más largo de las líneas CRÍTICAS. Las opcionales no cuentan: '
        'si el horno de pisos tarda tres meses y no lo necesitas para abrir, no '
        'puede mover tu fecha.')
    res(R_PLAZO_LIN, 'Línea que marca el plazo crítico',
        '=IFERROR(INDEX({c},MATCH($I${p},{t},0)),"")'
        .format(c=rng('C'), p=R_PLAZO, t=rng('T')), None,
        'Ésta es la primera que hay que pedir, aunque sea la última que vayas '
        'a instalar.')
    res(R_MARGEN, 'Margen del plazo crítico (semanas)',
        '=IFERROR(IF(OR($C${s}="",$I${p}=""),"",$C${s}-$I${p}-$C${m}),"")'
        .format(s=P_SEM, p=R_PLAZO, m=P_MARGEN), FMT_ENT,
        'Semanas que te sobran entre pedir hoy el equipo de mayor plazo y '
        'abrir con el margen de seguridad dentro.')
    res(R_VER_PLAZO, 'Veredicto del plazo',
        '=IF($I${m}="","",IF($I${m}<0,'
        '"El equipo de mayor plazo mueve la apertura: pídelo hoy o retrasa la '
        'fecha","Llegas con margen, pero pide primero el de mayor plazo"))'
        .format(m=R_MARGEN), None,
        'Un obrador no abre porque falte una máquina, y la que falta casi '
        'siempre es la que se pidió la última.')
    res(R_TARDE, 'Líneas cuyo plazo se pasa de la apertura',
        '=IFERROR(SUM(%s),"")' % rng('U'), FMT_ENT,
        'Cuenta también las opcionales: si la pides, tiene que llegar.')

    # --- listas ----------------------------------------------------------
    seccion(ws, 'A%d' % LI_SEC, 'Listas (origen de los desplegables)')
    cabecera(ws, LI_CAB, [('A', 'Estado'), ('C', 'Prioridad'),
                          ('E', 'Base del precio'), ('G', 'Textos fijos')],
             altura=20)
    for i, est in enumerate(ESTADOS):
        motor.val(ws, 'A%d' % (LI_INI + i), est)
    for i, pri in enumerate(PRIORIDADES):
        motor.val(ws, 'C%d' % (LI_INI + i), pri)
    for i, base in enumerate(BASES_IVA):
        motor.val(ws, 'E%d' % (LI_INI + i), base)
    motor.val(ws, 'G%d' % LI_INI, PROV_PENDIENTE)

    parrafo(ws, EQ_NOTA,
            'CRÍTICO quiere decir «sin esto no abres», y es la lista que '
            'calcula el plazo crítico. OPCIONAL quiere decir «depende del '
            'concepto»: son la atemperadora de chocolate y el horno de pisos '
            'modular, más el accesorio de puertas de la vitrina. No hay un '
            'nivel intermedio a propósito: en una apertura, «recomendado» '
            'siempre acaba comprándose.', col_fin='W', alto=42)
    parrafo(ws, EQ_NOTA + 1,
            'Los plazos de entrega son SUPUESTOS: ningún distribuidor los '
            'publica. Sustitúyelos por el que te comprometan por escrito en el '
            'presupuesto, que es donde de verdad se negocia una apertura.',
            col_fin='W', alto=28)
    parrafo(ws, EQ_NOTA + 2,
            'La vitrina Docriluc lleva un descuento de campaña del 30 % sobre '
            'un PVP de 3.263,00 €: es un precio fechado el 10-09-2026 y puede '
            'caducar. La batidora Sammic no declara si su precio lleva IVA y '
            'se trata como base imponible: es exactamente el caso que obliga a '
            'tener la columna.', col_fin='W', alto=28)
    parrafo(ws, EQ_NOTA + 3,
            'Si ya tienes el Kit de Tareas Pastelería (12 €), ninguna de sus '
            'quince plantillas sustituye a esta hoja: el kit organiza el '
            'obrador montado, no la compra.', col_fin='W', alto=24)

    # --- validación, semáforos y formato ---------------------------------
    dv_rango(ws, verdes_estado, '${a}${i}:${a}${f}'
             .format(a='A', i=LI_INI, f=LI_FIN), 'Estado no válido',
             'Elige un estado de la lista de la propia hoja: Pendiente, '
             'Presupuestado, Pedido, Recibido, Instalado o N/A.')
    motor.dv_numerica(ws, verdes_precio, minimo=0, titulo='Precio negociado',
                      mensaje='Escribe el precio SIN IVA, en euros.')
    motor.dv_numerica(ws, verdes_plazo, minimo=0, maximo=104,
                      titulo='Plazo de entrega',
                      mensaje='Escribe el plazo en SEMANAS (0 a 104).')
    motor.dv_porcentaje(ws, ['C%d' % P_IVA, 'C%d' % P_HORQ,
                             'C%d' % P_UMBRAL])
    motor.dv_numerica(ws, ['C%d' % P_CAPEX2], minimo=0,
                      titulo='CAPEX del libro 2',
                      mensaje='Escribe el total SIN IVA, en euros.')
    motor.dv_numerica(ws, ['C%d' % P_SEM, 'C%d' % P_MARGEN], minimo=0,
                      maximo=104, titulo='Semanas',
                      mensaje='Escribe un número de semanas (0 a 104).')
    motor.semaforo_texto(ws, 'A%d:A%d' % (EQ_INI, EQ_FIN), motor.SEM_ESTADO)
    motor.semaforo_isnumber(ws, 'S%d:S%d' % (EQ_INI, EQ_FIN), '$S%d' % EQ_INI,
                            '<', '0')
    motor.regla_expresion(ws, 'P%d:P%d' % (EQ_INI, EQ_FIN),
                          '=AND(ISNUMBER($P{r}),$P{r}>$C${u})'
                          .format(r=EQ_INI, u=P_UMBRAL))
    motor.semaforo_isnumber(ws, 'I%d' % R_MARGEN, '$I$%d' % R_MARGEN, '<', '0')
    motor.regla_expresion(ws, 'I%d' % R_DESV_PCT,
                          '=AND(ISNUMBER($I${d}),OR($I${d}>$C${u},'
                          '$I${d}<-$C${u}))'.format(d=R_DESV_PCT, u=P_UMBRAL))
    pie(ws, EQ_PIE, col_fin='W')
    ws.freeze_panes = 'C%d' % EQ_INI
    pagina(ws, titulos='$%d:$%d' % (EQ_CAB, EQ_CAB),
           area='A1:W%d' % (EQ_PIE + 1))
    return ws


# --------------------------------------------------------------------------
# Hoja «Variante del Formato»
# --------------------------------------------------------------------------
V_ELIGE = 6
V_LINEAS = 7
V_INVER = 8
V_BASE = 9
V_DIF = 10
V_SOBRAN = 11
V_FALTAN = 12
V_TAB_SEC = 14
V_CAB = 15
V_INI = 16
V_FIN = V_INI + N_EQ - 1
V_TOT_LIN = V_FIN + 1
V_TOT_EUR = V_FIN + 2
V_LIST_SEC = V_TOT_EUR + 2
V_LIST_CAB = V_LIST_SEC + 1
V_LIST_INI = V_LIST_CAB + 1
V_LIST_FIN = V_LIST_INI + len(VARIANTES) - 1
V_NOTA = V_LIST_FIN + 2
V_PIE = V_NOTA + 4

COL_VAR = ('E', 'F', 'G', 'H', 'I', 'J', 'K')
COL_BASE = COL_VAR[VAR_BASE]


def hoja_variante(wb):
    ws = wb.create_sheet(H_VAR)
    anchos(ws, {'A': 5, 'B': 46, 'C': 16, 'D': 11, 'E': 15, 'F': 15, 'G': 15,
                'H': 15, 'I': 15, 'J': 15, 'K': 15, 'L': 16, 'M': 62})
    encabezar(ws, 'Qué equipo pide cada variante de formato', col_fin='M',
              nota_txt='La dotación completa es la del local con venta. Las '
                       'otras seis variantes se leen como desviaciones sobre '
                       'ella: qué línea te sobra y qué línea te falta.')

    seccion(ws, 'A5', 'Elige la variante que vas a montar')
    ws.merge_cells('A%d:B%d' % (V_ELIGE, V_ELIGE))
    motor.val(ws, 'A%d' % V_ELIGE, 'Variante que vas a montar', bold=True)
    motor.val(ws, 'C%d' % V_ELIGE, VARIANTES[VAR_BASE][0], verde_=True)
    ws.merge_cells('E%d:M%d' % (V_ELIGE, V_ELIGE))
    motor.val(ws, 'E%d' % V_ELIGE,
              'Desplegable contra la lista de más abajo. Viene con el caso '
              'base porque es el de «La Clara»; cámbialo por el tuyo.',
              wrap=True)
    ws['E%d' % V_ELIGE].font = Font(italic=True, size=9)

    def res(fila, etiqueta, formula, fmt, nota):
        ws.merge_cells('A%d:B%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, etiqueta, bold=True)
        motor.f(ws, 'C%d' % fila, formula, fmt=fmt, bold=True)
        ws['C%d' % fila].fill = PatternFill('solid', fgColor=CREMA)
        ws.merge_cells('E%d:M%d' % (fila, fila))
        motor.val(ws, 'E%d' % fila, nota, wrap=True)
        ws['E%d' % fila].font = Font(italic=True, size=9)
        ws.row_dimensions[fila].height = 24

    cab_var = '$E${c}:$K${c}'.format(c=V_CAB)
    res(V_LINEAS, 'Líneas de equipamiento que necesitas',
        '=IFERROR(INDEX($E${t}:$K${t},MATCH($C${e},{cv},0)),"")'
        .format(t=V_TOT_LIN, e=V_ELIGE, cv=cab_var), FMT_ENT,
        'Sólo las marcadas «Sí». Las «Depende» no se cuentan: son las que '
        'tienes que decidir tú.')
    res(V_INVER, 'Inversión de referencia de esa variante (€, sin IVA)',
        '=IFERROR(INDEX($E${t}:$K${t},MATCH($C${e},{cv},0)),"")'
        .format(t=V_TOT_EUR, e=V_ELIGE, cv=cab_var), FMT_EUR,
        'Suma del precio de referencia sin IVA de las líneas marcadas «Sí». No '
        'incluye obra, licencias ni fondo de maniobra: eso es el libro 2.')
    res(V_BASE, 'Inversión de referencia del caso base (€, sin IVA)',
        '=${c}${t}'.format(c=COL_BASE, t=V_TOT_EUR), FMT_EUR,
        'El local con venta, que es el caso de «La Clara».')
    res(V_DIF, 'Diferencia contra el caso base (€)',
        '=IFERROR(IF($C${i}="","",$C${i}-$C${b}),"")'
        .format(i=V_INVER, b=V_BASE), FMT_EUR,
        'Negativo = tu variante necesita menos equipo que el caso base.')
    res(V_SOBRAN, 'Líneas del caso base que a ti te sobran',
        '=SUMPRODUCT(--($L${a}:$L${b}<>$C${s}),--(${c}${a}:${c}${b}=$C${s}))'
        .format(a=V_INI, b=V_FIN, c=COL_BASE, s=V_LIST_INI), FMT_ENT,
        'Están en la dotación completa y tu formato no las pide.')
    res(V_FALTAN, 'Líneas que te faltan respecto del caso base',
        '=SUMPRODUCT(--($L${a}:$L${b}=$C${s}),--(${c}${a}:${c}${b}<>$C${s}))'
        .format(a=V_INI, b=V_FIN, c=COL_BASE, s=V_LIST_INI), FMT_ENT,
        'Las pide tu formato y no están en el caso base.')

    seccion(ws, 'A%d' % V_TAB_SEC, 'Qué pide cada variante, línea a línea')
    cols = [('A', 'Nº'), ('B', 'Partida'),
            ('C', 'Precio de referencia sin IVA (€)'), ('D', 'Prioridad')]
    for i, v in enumerate(VARIANTES):
        cols.append((COL_VAR[i], v[0]))
    cols.append(('L', '¿La necesitas tú?'))
    cols.append(('M', 'Por qué'))
    cabecera(ws, V_CAB, cols, altura=52)
    for i, eq in enumerate(EQUIPOS):
        r = V_INI + i
        motor.val(ws, 'A%d' % r, eq['n'], fmt=FMT_ENT)
        motor.val(ws, 'B%d' % r, eq['partida'], wrap=True)
        motor.f(ws, 'C%d' % r, "='{h}'!$L${r}".format(h=H_EQ, r=EQ_INI + i),
                fmt=FMT_EUR)
        motor.f(ws, 'D%d' % r, "='{h}'!$H${r}".format(h=H_EQ, r=EQ_INI + i))
        for j in range(len(VARIANTES)):
            motor.val(ws, '%s%d' % (COL_VAR[j], r), APLICA[eq['n']][j],
                      align='center')
        motor.f(ws, 'L%d' % r,
                '=IFERROR(INDEX($E{r}:$K{r},MATCH($C${e},{cv},0)),"")'
                .format(r=r, e=V_ELIGE, cv=cab_var), align='center')
        motor.val(ws, 'M%d' % r, eq['nota'] or '', wrap=True)
        ws.row_dimensions[r].height = 30
    ws.merge_cells('A%d:B%d' % (V_TOT_LIN, V_TOT_LIN))
    motor.val(ws, 'A%d' % V_TOT_LIN, 'Líneas marcadas «Sí»', bold=True)
    ws.merge_cells('A%d:B%d' % (V_TOT_EUR, V_TOT_EUR))
    motor.val(ws, 'A%d' % V_TOT_EUR,
              'Inversión de referencia sin IVA (€)', bold=True)
    for j in range(len(VARIANTES)):
        c = COL_VAR[j]
        motor.f(ws, '%s%d' % (c, V_TOT_LIN),
                '=SUMPRODUCT(--(${c}${a}:${c}${b}=$C${s}))'
                .format(c=c, a=V_INI, b=V_FIN, s=V_LIST_INI), fmt=FMT_ENT,
                bold=True)
        ws['%s%d' % (c, V_TOT_LIN)].fill = PatternFill('solid', fgColor=CREMA)
        motor.f(ws, '%s%d' % (c, V_TOT_EUR),
                '=SUMPRODUCT(--(${c}${a}:${c}${b}=$C${s}),$C${a}:$C${b})'
                .format(c=c, a=V_INI, b=V_FIN, s=V_LIST_INI), fmt=FMT_EUR,
                bold=True)
        ws['%s%d' % (c, V_TOT_EUR)].fill = PatternFill('solid', fgColor=CREMA)

    seccion(ws, 'A%d' % V_LIST_SEC,
            'Las siete variantes (lista del desplegable)')
    cabecera(ws, V_LIST_CAB, [('A', 'Nº'), ('B', 'Variante'),
                              ('C', 'Vocabulario'), ('D', 'Id'),
                              ('E', 'Qué cambia respecto del caso base')],
             altura=22)
    ws.merge_cells('E%d:M%d' % (V_LIST_CAB, V_LIST_CAB))
    for i, (nombre, idps, texto) in enumerate(VARIANTES):
        r = V_LIST_INI + i
        motor.val(ws, 'A%d' % r, i + 1, fmt=FMT_ENT)
        motor.val(ws, 'B%d' % r, nombre)
        motor.val(ws, 'C%d' % r, ('Sí', 'No', 'Depende')[i] if i < 3 else '')
        motor.val(ws, 'D%d' % r, idps)
        ws.merge_cells('E%d:M%d' % (r, r))
        motor.val(ws, 'E%d' % r, texto, wrap=True)
        ws.row_dimensions[r].height = 28

    parrafo(ws, V_NOTA,
            'La columna «Vocabulario» de las tres primeras filas es el origen '
            'de los valores Sí / No / Depende que usan las fórmulas de esta '
            'hoja. No la borres aunque no la leas.', col_fin='M', alto=24)
    parrafo(ws, V_NOTA + 1,
            'QUÉ ES CRITERIO Y QUÉ ES DATO: las inversiones publicadas de cada '
            'variante y sus ids PS son datos de terceros con fuente. El reparto '
            'de Sí / No / Depende línea a línea es CRITERIO DE LA CASA, no '
            'norma: describe qué equipo suele pedir cada formato, y hay '
            'obradores que lo resuelven de otra manera. Cámbialo si tu proyecto '
            'lo pide, desprotegiendo la hoja.', col_fin='M', alto=40)
    parrafo(ws, V_NOTA + 2,
            'Lo que NO cambia con la variante es lo legal: la vía de registro, '
            'el árbol del art. 3 y la ruta doméstica los resuelve el '
            '«checklist-legal-y-licencias.xlsx» (libro 6), y ahí sí hay '
            'diferencias grandes entre montar en casa y montar un obrador B2B.',
            col_fin='M', alto=28)

    dv_rango(ws, ['C%d' % V_ELIGE],
             '$B${a}:$B${b}'.format(a=V_LIST_INI, b=V_LIST_FIN),
             'Variante no válida',
             'Elige una de las siete variantes de la lista de esta hoja.')
    pie(ws, V_PIE, col_fin='M')
    ws.freeze_panes = 'C%d' % V_INI
    pagina(ws, titulos='$%d:$%d' % (V_CAB, V_CAB),
           area='A1:M%d' % (V_PIE + 1))
    return ws


# --------------------------------------------------------------------------
# Hoja «Proveedores»
# --------------------------------------------------------------------------
PR_CAB = 6
PR_INI = 7
PR_FIN = PR_INI + len(D.PROVEEDORES) - 1
PR_TOT = PR_FIN + 1
PR_TRAB = PR_FIN + 2
PR_MIN = PR_FIN + 3
PR_PLAZO = PR_FIN + 4
PR_LIST_SEC = PR_PLAZO + 2
PR_LIST_CAB = PR_LIST_SEC + 1
PR_LIST_INI = PR_LIST_CAB + 1
PR_LIST_FIN = PR_LIST_INI + 1
PR_NOTA = PR_LIST_FIN + 2
PR_PIE = PR_NOTA + 4


def hoja_proveedores(wb):
    ws = wb.create_sheet(H_PROV)
    anchos(ws, {'A': 5, 'B': 26, 'C': 40, 'D': 46, 'E': 8, 'F': 14, 'G': 28,
                'H': 15, 'I': 14, 'J': 34, 'K': 44, 'L': 46})
    encabezar(ws, 'Proveedores de materia prima', col_fin='L',
              nota_txt='Los nueve con URL comprobada el 10-09-2026. El '
                       'research recogió otros 22 sin verificar y no se '
                       'publican: un directorio con un enlace roto vale menos '
                       'que uno corto.')
    seccion(ws, 'A5', 'Los nueve proveedores verificados')
    cabecera(ws, PR_CAB, [
        ('A', 'Nº'), ('B', 'Proveedor'), ('C', 'Qué te vende'), ('D', 'URL'),
        ('E', 'Id'), ('F', '¿Trabajas con él?'), ('G', 'Contacto comercial'),
        ('H', 'Pedido mínimo (€)'), ('I', 'Plazo (días)'),
        ('J', 'Condiciones de pago'), ('K', 'Notas de la negociación'),
        ('L', 'Por qué está en la lista')], altura=40)
    v_si_no, v_texto, v_min, v_plazo = [], [], [], []
    for i, (nombre, cat, url, idps, nota) in enumerate(D.PROVEEDORES):
        r = PR_INI + i
        motor.val(ws, 'A%d' % r, i + 1, fmt=FMT_ENT)
        motor.val(ws, 'B%d' % r, nombre)
        motor.val(ws, 'C%d' % r, cat, wrap=True)
        motor.val(ws, 'D%d' % r, url)
        motor.val(ws, 'E%d' % r, idps)
        motor.val(ws, 'F%d' % r, SI_NO[1], verde_=True, align='center')
        v_si_no.append('F%d' % r)
        motor.val(ws, 'G%d' % r, 'Pendiente: pide el alta de cliente',
                  verde_=True)
        v_texto.append('G%d' % r)
        motor.val(ws, 'H%d' % r, PEDIDO_MINIMO_DEFECTO, fmt=FMT_EUR,
                  verde_=True)
        v_min.append('H%d' % r)
        motor.val(ws, 'I%d' % r, PLAZO_PROVEEDOR_DEFECTO, fmt=FMT_ENT,
                  verde_=True)
        v_plazo.append('I%d' % r)
        motor.val(ws, 'J%d' % r, 'Pendiente de negociar', verde_=True)
        motor.val(ws, 'K%d' % r, 'Pendiente de la primera visita comercial',
                  verde_=True)
        motor.val(ws, 'L%d' % r, nota or 'Fabricante o distribuidor con web '
                                         'propia comprobada el 10-09-2026.',
                  wrap=True)
        ws.row_dimensions[r].height = 28

    def res(fila, etiqueta, formula, fmt, nota):
        ws.merge_cells('A%d:E%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, etiqueta, bold=True)
        motor.f(ws, 'F%d' % fila, formula, fmt=fmt, bold=True)
        ws['F%d' % fila].fill = PatternFill('solid', fgColor=CREMA)
        ws.merge_cells('G%d:L%d' % (fila, fila))
        motor.val(ws, 'G%d' % fila, nota, wrap=True)
        ws['G%d' % fila].font = Font(italic=True, size=9)

    res(PR_TOT, 'Proveedores publicados en esta hoja',
        '=COUNTIF($B${a}:$B${b},"<>")'.format(a=PR_INI, b=PR_FIN), FMT_ENT,
        'Nueve verificados. Los 22 sin verificar del research no entran.')
    res(PR_TRAB, 'Proveedores con los que ya trabajas',
        '=SUMPRODUCT(--($F${a}:$F${b}=$B${s}))'
        .format(a=PR_INI, b=PR_FIN, s=PR_LIST_INI), FMT_ENT,
        'Empieza por dos o tres: abrir ficha en nueve proveedores a la vez es '
        'una semana de papeleo y ningún descuento.')
    res(PR_MIN, 'Pedido mínimo acumulado si pides a todos a la vez (€)',
        '=SUM($H${a}:$H${b})'.format(a=PR_INI, b=PR_FIN), FMT_EUR,
        'Es dinero parado en el almacén el día que menos caja tienes. Los '
        'pedidos mínimos son SUPUESTOS: te los confirma cada comercial.')
    res(PR_PLAZO, 'Plazo medio de entrega comprometido (días)',
        '=IFERROR(AVERAGE($I${a}:$I${b}),"")'.format(a=PR_INI, b=PR_FIN),
        FMT_DEC,
        'Con qué antelación tienes que pedir la materia prima de cada pico. '
        'La antelación de compra por campaña la calcula el '
        '«estacionalidad-y-picos.xlsx» (libro 3).')

    seccion(ws, 'A%d' % PR_LIST_SEC, 'Listas (origen de los desplegables)')
    cabecera(ws, PR_LIST_CAB, [('A', 'Nº'), ('B', '¿Trabajas con él?')],
             altura=20)
    for i, opt in enumerate(SI_NO):
        motor.val(ws, 'A%d' % (PR_LIST_INI + i), i + 1, fmt=FMT_ENT)
        motor.val(ws, 'B%d' % (PR_LIST_INI + i), opt)

    parrafo(ws, PR_NOTA, D.NOTA_PROVEEDORES, col_fin='L', alto=40)
    parrafo(ws, PR_NOTA + 1,
            'Directorio de proveedores del grupo (certificado comprobado el '
            '10-09-2026): ' + D.HOSPLY_URL, col_fin='L', alto=26)
    parrafo(ws, PR_NOTA + 2,
            'Los pedidos mínimos, los plazos y las condiciones de pago que '
            'vienen rellenos son SUPUESTOS para que la hoja funcione desde el '
            'primer minuto: no son las condiciones de estas empresas. Cada una '
            'te dará las suyas, y cambian con el volumen y con la provincia.',
            col_fin='L', alto=34)

    dv_rango(ws, v_si_no, '$B${a}:$B${b}'.format(a=PR_LIST_INI, b=PR_LIST_FIN),
             'Valor no válido', 'Elige Sí o No de la lista de esta hoja.')
    motor.dv_numerica(ws, v_min, minimo=0, titulo='Pedido mínimo',
                      mensaje='Escribe el pedido mínimo en euros, sin IVA.')
    motor.dv_numerica(ws, v_plazo, minimo=0, maximo=180, titulo='Plazo',
                      mensaje='Escribe el plazo de entrega en días (0 a 180).')
    pie(ws, PR_PIE, col_fin='L')
    ws.freeze_panes = 'C%d' % PR_INI
    pagina(ws, titulos='$%d:$%d' % (PR_CAB, PR_CAB),
           area='A1:L%d' % (PR_PIE + 1))
    return ws


# --------------------------------------------------------------------------
# Hoja «Contador»
# --------------------------------------------------------------------------
C_SEC1 = 5
C_CAB1 = 6
C_TOT = 7
C_NA_F = 8
C_ALCANCE = 9
C_INST = 10
C_RECIB = 11
C_PEDIDO = 12
C_PRESU = 13
C_PENDI = 14
C_AVANCE = 15
C_SEC2 = 17
C_CRIT_N = 18
C_CRIT_I = 19
C_CRIT_P = 20
C_VEREDICTO = 21
C_SEC3 = 23
C_CAB3 = 24
C_BLQ_INI = 25
C_BLQ_FIN = C_BLQ_INI + len(BLOQUES) - 1
C_BLQ_TOT = C_BLQ_FIN + 1
C_SEC4 = C_BLQ_TOT + 2
C_CAB4 = C_SEC4 + 1
C_CAT_INI = C_CAB4 + 1
C_CAT_FIN = C_CAT_INI + len(CATEGORIAS) - 1
C_SEC5 = C_CAT_FIN + 2
C_PROV_N = C_SEC5 + 1
C_PROV_T = C_SEC5 + 2
C_PROV_SIN = C_SEC5 + 3
C_NOTA = C_PROV_SIN + 2
C_PIE = C_NOTA + 3


def hoja_contador(wb):
    ws = wb.create_sheet(H_CONT)
    anchos(ws, {'A': 54, 'B': 16, 'C': 16, 'D': 16, 'E': 14, 'F': 72})
    encabezar(ws, 'Contador del checklist', col_fin='F',
              nota_txt='Todo lo de esta hoja se lee de «Equipamiento» y de '
                       '«Proveedores»: aquí no se teclea nada.')
    est_col = "'{h}'!$A${a}:$A${b}".format(h=H_EQ, a=EQ_INI, b=EQ_FIN)
    pri_col = "'{h}'!$H${a}:$H${b}".format(h=H_EQ, a=EQ_INI, b=EQ_FIN)
    par_col = "'{h}'!$C${a}:$C${b}".format(h=H_EQ, a=EQ_INI, b=EQ_FIN)
    blq_col = "'{h}'!$G${a}:$G${b}".format(h=H_EQ, a=EQ_INI, b=EQ_FIN)
    cat_col = "'{h}'!$F${a}:$F${b}".format(h=H_EQ, a=EQ_INI, b=EQ_FIN)
    ref_col = "'{h}'!$L${a}:$L${b}".format(h=H_EQ, a=EQ_INI, b=EQ_FIN)
    real_col = "'{h}'!$O${a}:$O${b}".format(h=H_EQ, a=EQ_INI, b=EQ_FIN)
    prov_col = "'{h}'!$Q${a}:$Q${b}".format(h=H_EQ, a=EQ_INI, b=EQ_FIN)
    crit_cel = "'{h}'!{c}".format(h=H_EQ, c=C_CRIT)
    inst_cel = "'{h}'!{c}".format(h=H_EQ, c=C_INSTAL)
    na_cel = "'{h}'!{c}".format(h=H_EQ, c=C_NA)
    pte_cel = "'{h}'!{c}".format(h=H_EQ, c=C_PROVPTE)

    def fila(r, etiqueta, formula, fmt, nota):
        motor.val(ws, 'A%d' % r, etiqueta)
        motor.f(ws, 'B%d' % r, formula, fmt=fmt, bold=True)
        ws['B%d' % r].fill = PatternFill('solid', fgColor=CREMA)
        ws.merge_cells('C%d:F%d' % (r, r))
        motor.val(ws, 'C%d' % r, nota, wrap=True)
        ws['C%d' % r].font = Font(italic=True, size=9)
        ws.row_dimensions[r].height = 22

    seccion(ws, 'A%d' % C_SEC1, 'Avance del checklist de equipamiento')
    cabecera(ws, C_CAB1, [('A', 'Concepto'), ('B', 'Valor'), ('C', 'Nota')],
             altura=20)
    ws.merge_cells('C%d:F%d' % (C_CAB1, C_CAB1))
    fila(C_TOT, 'Líneas del checklist', '=COUNTIF(%s,"<>")' % par_col,
         FMT_ENT, 'La dotación completa de una pastelería con obrador.')
    fila(C_NA_F, 'Líneas marcadas «N/A» (fuera de tu alcance)',
         '=SUMPRODUCT(--({e}={n}))'.format(e=est_col, n=na_cel), FMT_ENT,
         'Lo que tu formato no necesita. No cuenta ni a favor ni en contra.')
    fila(C_ALCANCE, 'Líneas dentro de tu alcance',
         '=$B${a}-$B${b}'.format(a=C_TOT, b=C_NA_F), FMT_ENT,
         'Es el denominador del avance.')
    fila(C_INST, 'Líneas instaladas',
         '=SUMPRODUCT(--({e}={i}))'.format(e=est_col, i=inst_cel), FMT_ENT,
         'Instalada quiere decir montada, conectada y probada; recibida no es '
         'instalada, y esa diferencia son días.')
    fila(C_RECIB, 'Líneas recibidas',
         '=COUNTIF({e},"Recibido")'.format(e=est_col), FMT_ENT,
         'Están en el local, en su caja.')
    fila(C_PEDIDO, 'Líneas pedidas',
         '=COUNTIF({e},"Pedido")'.format(e=est_col), FMT_ENT,
         'Pedidas y pagadas o con señal: el plazo ya corre.')
    fila(C_PRESU, 'Líneas presupuestadas',
         '=COUNTIF({e},"Presupuestado")'.format(e=est_col), FMT_ENT,
         'Tienes el precio, no has pedido.')
    fila(C_PENDI, 'Líneas pendientes',
         '=COUNTIF({e},"Pendiente")'.format(e=est_col), FMT_ENT,
         'Ni siquiera has pedido presupuesto.')
    fila(C_AVANCE, 'Avance del checklist (% instalado)',
         '=IFERROR(IF($B${a}=0,"",$B${i}/$B${a}),"")'
         .format(a=C_ALCANCE, i=C_INST), FMT_PCT,
         'Sobre lo que está dentro de tu alcance, no sobre las 22 líneas.')

    seccion(ws, 'A%d' % C_SEC2, 'Lo crítico, que es lo que decide si abres')
    fila(C_CRIT_N, 'Líneas críticas',
         '=SUMPRODUCT(--({p}={c}))'.format(p=pri_col, c=crit_cel), FMT_ENT,
         'Sin ellas no se abre. Las opcionales no entran aquí.')
    fila(C_CRIT_I, 'Líneas críticas instaladas',
         '=SUMPRODUCT(--({p}={c}),--({e}={i}))'
         .format(p=pri_col, c=crit_cel, e=est_col, i=inst_cel), FMT_ENT, '')
    fila(C_CRIT_P, 'Avance de lo crítico (%)',
         '=IFERROR(IF($B${n}=0,"",$B${i}/$B${n}),"")'
         .format(n=C_CRIT_N, i=C_CRIT_I), FMT_PCT,
         'Éste es el porcentaje que hay que mirar la semana antes de abrir.')
    motor.val(ws, 'A%d' % C_VEREDICTO, '¿Puedes abrir con lo que está '
                                       'instalado?', bold=True)
    motor.f(ws, 'B%d' % C_VEREDICTO,
            '=IF($B${n}=0,"",IF($B${i}=$B${n},'
            '"Sí: todo lo crítico está instalado",'
            'CONCATENATE("No: faltan ",$B${n}-$B${i}," líneas críticas")))'
            .format(n=C_CRIT_N, i=C_CRIT_I), bold=True)
    ws['B%d' % C_VEREDICTO].fill = PatternFill('solid', fgColor=CREMA)
    ws.merge_cells('C%d:F%d' % (C_VEREDICTO, C_VEREDICTO))
    motor.val(ws, 'C%d' % C_VEREDICTO,
              'La licencia y el registro sanitario van por su lado: eso lo '
              'contesta el libro 6.', wrap=True)
    ws['C%d' % C_VEREDICTO].font = Font(italic=True, size=9)

    seccion(ws, 'A%d' % C_SEC3, 'Por bloque de CAPEX')
    cabecera(ws, C_CAB3, [('A', 'Bloque'), ('B', 'Líneas'),
                          ('C', 'Referencia sin IVA (€)'),
                          ('D', 'Real negociado (€)'), ('E', 'Desviación (%)'),
                          ('F', 'Nota')], altura=30)
    for i, blq in enumerate(BLOQUES):
        r = C_BLQ_INI + i
        motor.val(ws, 'A%d' % r, blq)
        motor.f(ws, 'B%d' % r, '=SUMPRODUCT(--({b}=$A{r}))'
                .format(b=blq_col, r=r), fmt=FMT_ENT)
        motor.f(ws, 'C%d' % r, '=SUMPRODUCT(--({b}=$A{r}),{l})'
                .format(b=blq_col, r=r, l=ref_col), fmt=FMT_EUR)
        motor.f(ws, 'D%d' % r, '=SUMPRODUCT(--({b}=$A{r}),{o})'
                .format(b=blq_col, r=r, o=real_col), fmt=FMT_EUR)
        motor.f(ws, 'E%d' % r,
                '=IFERROR(IF($C{r}=0,"",$D{r}/$C{r}-1),"")'.format(r=r),
                fmt=FMT_PCT)
        motor.val(ws, 'F%d' % r,
                  'Es el bloque que el libro 2 lleva a su hoja «CAPEX por '
                  'Bloque» con este mismo nombre.', wrap=True)
    motor.val(ws, 'A%d' % C_BLQ_TOT, 'TOTAL', bold=True)
    # Hallazgo A3 (2026-09-10): `=SUM(B25:B26)` sobre dos SUMPRODUCT se
    # cacheaba como 0 (pycel no agrega bien un SUM sobre una columna de
    # SUMPRODUCT), justo debajo de sus dos sumandos correctos («17 + 5 = 0»).
    # C27/D27 sí cuadraban con SUM, pero se reescriben con el mismo
    # SUMPRODUCT directo sobre TODAS las líneas para no depender de que la
    # tabla de bloques tenga exactamente estas filas.
    motor.f(ws, 'B%d' % C_BLQ_TOT, '=SUMPRODUCT(--({b}<>""))'.format(b=blq_col),
            fmt=FMT_ENT, bold=True)
    motor.f(ws, 'C%d' % C_BLQ_TOT, '=SUMPRODUCT({r})'.format(r=ref_col),
            fmt=FMT_EUR, bold=True)
    motor.f(ws, 'D%d' % C_BLQ_TOT, '=SUMPRODUCT({r})'.format(r=real_col),
            fmt=FMT_EUR, bold=True)
    motor.f(ws, 'E%d' % C_BLQ_TOT,
            '=IFERROR(IF($C${t}=0,"",$D${t}/$C${t}-1),"")'.format(t=C_BLQ_TOT),
            fmt=FMT_PCT, bold=True)

    seccion(ws, 'A%d' % C_SEC4, 'Por categoría de equipo')
    cabecera(ws, C_CAB4, [('A', 'Categoría'), ('B', 'Líneas'),
                          ('C', 'Referencia sin IVA (€)'),
                          ('D', 'Real negociado (€)'),
                          ('E', 'Instaladas'), ('F', 'Nota')], altura=30)
    for i, cat in enumerate(CATEGORIAS):
        r = C_CAT_INI + i
        motor.val(ws, 'A%d' % r, cat)
        motor.f(ws, 'B%d' % r, '=SUMPRODUCT(--({c}=$A{r}))'
                .format(c=cat_col, r=r), fmt=FMT_ENT)
        motor.f(ws, 'C%d' % r, '=SUMPRODUCT(--({c}=$A{r}),{l})'
                .format(c=cat_col, r=r, l=ref_col), fmt=FMT_EUR)
        motor.f(ws, 'D%d' % r, '=SUMPRODUCT(--({c}=$A{r}),{o})'
                .format(c=cat_col, r=r, o=real_col), fmt=FMT_EUR)
        motor.f(ws, 'E%d' % r, '=SUMPRODUCT(--({c}=$A{r}),--({e}={i}))'
                .format(c=cat_col, r=r, e=est_col, i=inst_cel), fmt=FMT_ENT)
        motor.val(ws, 'F%d' % r, '', wrap=True)

    seccion(ws, 'A%d' % C_SEC5, 'Proveedores')
    fila(C_PROV_N, 'Proveedores verificados publicados',
         "='{h}'!$F${r}".format(h=H_PROV, r=PR_TOT), FMT_ENT,
         'Los nueve con URL comprobada el 10-09-2026.')
    fila(C_PROV_T, 'Proveedores con los que ya trabajas',
         "='{h}'!$F${r}".format(h=H_PROV, r=PR_TRAB), FMT_ENT, '')
    fila(C_PROV_SIN, 'Líneas de equipamiento sin proveedor asignado',
         '=SUMPRODUCT(--({q}={p}))'.format(q=prov_col, p=pte_cel), FMT_ENT,
         'Las que siguen con el texto «' + PROV_PENDIENTE + '». En maquinaria '
         'de obrador se vende por presupuesto: mientras no haya nombre, no hay '
         'precio.')

    parrafo(ws, C_NOTA,
            'Este contador NO dice si puedes abrir: dice si tienes el equipo. '
            'Lo otro -la comunicación al registro sanitario, la licencia, el '
            'plan de APPCC y la formación- lo cuenta el '
            '«checklist-legal-y-licencias.xlsx» (libro 6), que además encadena '
            'los plazos y calcula la fecha de apertura.', col_fin='F', alto=40)
    parrafo(ws, C_NOTA + 1,
            'Y no dice si el obrador rinde: cuántas piezas al día aguanta el '
            'equipo que estás comprando lo calcula el '
            '«capacidad-obrador-y-local.xlsx» (libro 1). Comprar el equipo '
            'completo no garantiza sacar la producción de Reyes.',
            col_fin='F', alto=32)
    pie(ws, C_PIE, col_fin='F')
    ws.freeze_panes = 'A%d' % (C_CAB1 + 1)     # hallazgo B12 (2026-09-10)
    pagina(ws, apaisado=False, area='A1:F%d' % (C_PIE + 1))
    return ws


# --------------------------------------------------------------------------
# Mapa de celdas citables
# --------------------------------------------------------------------------
def mapa_def():
    """(etiqueta, hoja, celda, tipo) de lo que el guion puede citar."""
    m = [
        ('Tipo de IVA general del equipamiento', H_EQ, 'C%d' % P_IVA,
         'parametro'),
        ('Horquilla del precio de referencia', H_EQ, 'C%d' % P_HORQ,
         'parametro'),
        ('CAPEX de equipamiento copiado del libro 2 (sin IVA)', H_EQ,
         'C%d' % P_CAPEX2, 'entrada'),
        ('Umbral de desviación admitida', H_EQ, 'C%d' % P_UMBRAL, 'parametro'),
        ('Semanas que faltan hasta la apertura prevista', H_EQ,
         'C%d' % P_SEM, 'entrada'),
        ('Margen de seguridad entre la entrega y la apertura (semanas)', H_EQ,
         'C%d' % P_MARGEN, 'entrada'),
        ('Líneas del checklist de equipamiento', H_EQ, 'I%d' % R_LINEAS,
         'salida'),
        ('Total de referencia sin IVA de las líneas críticas', H_EQ,
         'I%d' % R_REF_CRIT, 'salida'),
        ('Total de referencia sin IVA de toda la dotación', H_EQ,
         'I%d' % R_REF_TODO, 'salida'),
        ('Total real negociado sin IVA de las líneas críticas', H_EQ,
         'I%d' % R_REAL_CRIT, 'salida'),
        ('Total real negociado sin IVA de toda la dotación', H_EQ,
         'I%d' % R_REAL_TODO, 'salida'),
        ('Diferencia entre lo negociado y la referencia', H_EQ,
         'I%d' % R_DIF_NEG, 'salida'),
        ('IVA soportado sobre el equipamiento', H_EQ, 'I%d' % R_IVA_SOP,
         'salida'),
        ('Desembolso real del equipamiento con IVA', H_EQ, 'I%d' % R_DESEMB,
         'salida'),
        ('Desviación contra el CAPEX del libro 2 (euros)', H_EQ,
         'I%d' % R_DESV_EUR, 'salida'),
        ('Desviación contra el CAPEX del libro 2 (%)', H_EQ,
         'I%d' % R_DESV_PCT, 'salida'),
        ('Veredicto de la desviación de equipamiento', H_EQ,
         'I%d' % R_VER_DESV, 'salida'),
        ('Plazo crítico de entrega (semanas)', H_EQ, 'I%d' % R_PLAZO,
         'salida'),
        ('Línea que marca el plazo crítico', H_EQ, 'I%d' % R_PLAZO_LIN,
         'salida'),
        ('Margen del plazo crítico (semanas)', H_EQ, 'I%d' % R_MARGEN,
         'salida'),
        ('Veredicto del plazo de entrega', H_EQ, 'I%d' % R_VER_PLAZO,
         'salida'),
        ('Líneas cuyo plazo se pasa de la apertura', H_EQ, 'I%d' % R_TARDE,
         'salida'),
        ('Variante de formato elegida', H_VAR, 'C%d' % V_ELIGE, 'entrada'),
        ('Líneas de equipamiento que pide la variante elegida', H_VAR,
         'C%d' % V_LINEAS, 'salida'),
        ('Inversión de referencia de la variante elegida', H_VAR,
         'C%d' % V_INVER, 'salida'),
        ('Inversión de referencia del caso base (local con venta)', H_VAR,
         'C%d' % V_BASE, 'salida'),
        ('Diferencia de equipamiento contra el caso base', H_VAR,
         'C%d' % V_DIF, 'salida'),
        ('Líneas del caso base que sobran en la variante elegida', H_VAR,
         'C%d' % V_SOBRAN, 'salida'),
        ('Líneas que faltan respecto del caso base', H_VAR, 'C%d' % V_FALTAN,
         'salida'),
        ('Proveedores verificados publicados', H_PROV, 'F%d' % PR_TOT,
         'salida'),
        ('Proveedores con los que ya trabajas', H_PROV, 'F%d' % PR_TRAB,
         'salida'),
        ('Pedido mínimo acumulado de los nueve proveedores', H_PROV,
         'F%d' % PR_MIN, 'salida'),
        ('Plazo medio de entrega de los proveedores (días)', H_PROV,
         'F%d' % PR_PLAZO, 'salida'),
        ('Líneas dentro del alcance del checklist', H_CONT, 'B%d' % C_ALCANCE,
         'salida'),
        ('Avance del checklist de equipamiento (%)', H_CONT, 'B%d' % C_AVANCE,
         'salida'),
        ('Líneas críticas de equipamiento', H_CONT, 'B%d' % C_CRIT_N,
         'salida'),
        ('Avance de lo crítico (%)', H_CONT, 'B%d' % C_CRIT_P, 'salida'),
        ('Veredicto de si puedes abrir con lo instalado', H_CONT,
         'B%d' % C_VEREDICTO, 'salida'),
        ('Líneas de equipamiento sin proveedor asignado', H_CONT,
         'B%d' % C_PROV_SIN, 'salida'),
        ('Total de equipamiento por bloques (real negociado)', H_CONT,
         'D%d' % C_BLQ_TOT, 'salida'),
    ]
    for i, blq in enumerate(BLOQUES):
        m.append(('Inversión real negociada en «%s»' % blq, H_CONT,
                  'D%d' % (C_BLQ_INI + i), 'salida'))
    for j, v in enumerate(VARIANTES):
        m.append(('Inversión de referencia de la variante «%s»' % v[0], H_VAR,
                  '%s%d' % (COL_VAR[j], V_TOT_EUR), 'salida'))
    return m


# --------------------------------------------------------------------------
def construir():
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_equipamiento(wb)
    hoja_variante(wb)
    hoja_proveedores(wb)
    hoja_contador(wb)

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
    """`=SUM(rango)` recalculado a mano contra el caché (hallazgos A1/A3,
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

    Ojo con el «vacío»: `inject_cache.py` NO inyecta cache cuando el resultado
    es la cadena vacía (lo salta a propósito), así que una celda que en
    `data_only` sale `None` puede ser (a) una fórmula que no se pudo evaluar o
    (b) un «sin dato» legítimo de los que exige la SPEC («sin dato» = `""`,
    nunca 0). Las dos cosas se distinguen preguntándole a pycel: si devuelve
    `''`, la celda está vacía A PROPÓSITO; cualquier otra cosa es un fallo.
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
    """Cinco comportamientos probados con pycel sobre el fichero escrito."""
    from pycel import ExcelCompiler
    out = []

    def eval_(c, hoja, celda):
        return c.evaluate("'%s'!%s" % (hoja, celda))

    # 1. El total de referencia sin IVA suma las 22 líneas de datos_ejemplo.
    c = ExcelCompiler(ruta)
    esperado = round(sum(D.precio_equipamiento_sin_iva(e) for e in EQUIPOS), 2)
    total = eval_(c, H_EQ, 'I%d' % R_REF_TODO)
    ok1 = abs(total - esperado) < 0.05
    out.append(('el total de referencia sin IVA suma las %d líneas (%.2f €)'
                % (N_EQ, total), ok1))

    # 2. El plazo crítico IGNORA las líneas opcionales.
    plazo = eval_(c, H_EQ, 'I%d' % R_PLAZO)
    ok2 = (plazo == D.plazo_critico_semanas()
           and plazo < max(e['plazo_semanas'] for e in EQUIPOS))
    out.append(('el plazo crítico es %s semanas e ignora las opcionales '
                '(la más larga es %s)'
                % (plazo, max(e['plazo_semanas'] for e in EQUIPOS)), ok2))

    # 3. Un TEXTO en «precio real negociado» no rompe el semáforo ni el total.
    c3 = ExcelCompiler(ruta)
    eval_(c3, H_EQ, 'P%d' % EQ_INI)          # carga la celda y sus precedentes
    c3.set_value("'%s'!O%d" % (H_EQ, EQ_INI), 'sin presupuesto')
    desv = eval_(c3, H_EQ, 'P%d' % EQ_INI)
    ok3 = desv in ('', None) or isinstance(desv, str)
    out.append(('un texto en el precio negociado deja la desviación vacía '
                '(%r), no en rojo' % (desv,), ok3))

    # 4. Recortar las semanas hasta la apertura cambia el veredicto del plazo.
    c4 = ExcelCompiler(ruta)
    antes = eval_(c4, H_EQ, 'I%d' % R_VER_PLAZO)
    eval_(c4, H_EQ, 'C%d' % P_SEM)
    c4.set_value("'%s'!C%d" % (H_EQ, P_SEM), 4)
    despues = eval_(c4, H_EQ, 'I%d' % R_VER_PLAZO)
    ok4 = (antes != despues and 'mueve la apertura' in str(despues))
    out.append(('con 4 semanas hasta la apertura el veredicto pasa a «%s»'
                % str(despues)[:46], ok4))

    # 5. Bajar el precio negociado de una línea baja el total y la desviación.
    c5 = ExcelCompiler(ruta)
    t_antes = eval_(c5, H_EQ, 'I%d' % R_REAL_TODO)
    eval_(c5, H_EQ, 'O%d' % (EQ_INI + 4))
    c5.set_value("'%s'!O%d" % (H_EQ, EQ_INI + 4), 8000.0)
    t_despues = eval_(c5, H_EQ, 'I%d' % R_REAL_TODO)
    ok5 = t_despues < t_antes - 2000
    out.append(('negociar el abatidor a 8.000 € baja el total de %.2f a %.2f €'
                % (t_antes, t_despues), ok5))

    # 6. La variante «Obrador en casa» pide menos equipo que el caso base.
    c6 = ExcelCompiler(ruta)
    eval_(c6, H_VAR, 'C%d' % V_LINEAS)
    eval_(c6, H_VAR, 'C%d' % V_DIF)
    c6.set_value("'%s'!C%d" % (H_VAR, V_ELIGE), VARIANTES[0][0])
    lineas = eval_(c6, H_VAR, 'C%d' % V_LINEAS)
    dif = eval_(c6, H_VAR, 'C%d' % V_DIF)
    ok6 = lineas < 8 and dif < 0
    out.append(('la variante «Obrador en casa» pide %s líneas y %.2f € menos '
                'que el caso base' % (lineas, dif), ok6))
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
    total_verdes = sum(verdes.values())
    print('celdas verdes:', total_verdes)
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
