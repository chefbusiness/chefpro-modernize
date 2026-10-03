#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_aceite-de-fritura-coste-y-cambio.py - libro 4 de «Cómo Montar una
Churrería-Chocolatería» (producto 51, `guia-churreria-chocolateria`; SPEC
`scripts/productos-digitales/guia-churreria-SPEC.md`, §2.1 fila 4, §2.2, §3.5 y §5).

Molde N: sin generador hermano que calcar. Se toma la ESTRUCTURA de Parámetros y
Escenarios de `guia-chocolateria/gen_sensibilidad-al-precio-del-cacao.py` (parámetros
con unidad, origen y nota por fila; escenarios en los que sólo se teclea el % de
subida) y el cierre de `gen_carta-de-apertura-y-escandallo-churro.py` (libro 3 de
este mismo producto): inject_cache + verificación data_only + contrato de cruces +
lista negra + mapa + demo con pycel.

Hojas (`datos_ejemplo.HOJAS[4]`): Instrucciones · Parámetros · Consumo y Reposición ·
Punto Económico de Cambio · Escenarios de Precio del Aceite · Gestor de Aceite Usado.

CRUCES (D16, `datos_ejemplo.CRUCES`)
------------------------------------
Recibe X2 y X2 bis (del libro 3: precio del aceite, absorción, densidad, kg de masa
por ración y aceite absorbido por ración) y X3 y X3 bis (del libro 1: kg fritos del
día tipo y punta, litros de cuba y raciones del día tipo y punta). Cada una es una
celda VERDE de «Parámetros» con su valor por defecto (`valor_defecto`) y el rótulo
«cópialo del libro N: <fichero>!<Hoja>!<Celda>», más UNA FILA DE CUADRE con semáforo
en la misma hoja. Nunca una fórmula entre ficheros.

Los cuadres no comparan contra el origen (no hay vínculo): comparan las cifras
copiadas ENTRE SÍ, porque todas salen de los mismos supuestos y una copia vieja rompe
la identidad. Cuatro comprobaciones:
  A  aceite absorbido por ración (3) = kg fritos del día tipo (1) / raciones del día
     tipo (1) x absorción / densidad x precio (3). Se cumple exacta con El Molinete.
  B  kg fritos punta / kg fritos tipo = raciones punta / raciones tipo (misma masa
     por ración en los dos días).
  C  los kg fritos por kg de masa que implican las copias no pueden pasar de
     1 / (1 - absorción): la pieza frita pierde agua y gana aceite.
  D  la reposición que pide un día punta según la absorción no puede pasar de una
     cuba entera.

Es ORIGEN de X12 (renovación de aceite por ración, `Consumo y Reposición`!L5, al
libro 6). La renovación (el descarte al cambiar la cuba) es distinta del aceite
absorbido, que ya va en el escandallo del libro 3; la fila de contraste «aceite
absorbido (3) + renovación (4) = aceite total por ración» enseña las dos.

FRONTERAS
---------
No es registro APPCC: cita `pack-appcc/09-control-aceite-fritura.xlsx` (días entre
cambios y litros retirados se toman del registro del lector). Sin comparativa de
marcas ni tipos de aceite (C5). Sin temperatura de fritura del churro (V-02, rama
B); de la acrilamida, sólo la remisión a la parte A si además se fríen patatas
(CUN-05), sin cifra. El medidor de mano ayuda a decidir el cambio; el 25 % de
compuestos polares se prueba en laboratorio (A12, CUN-02). El gestor del aceite usado,
Ley 7/2022 (CUN-27).

Salida: build/aceite-de-fritura-coste-y-cambio.xlsx + build/mapa-...json.
Uso: /usr/local/bin/python3 gen_aceite-de-fritura-coste-y-cambio.py
Via: Claude Code
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

import openpyxl
from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Font, PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..'))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import _comun_churreria as CC                                  # noqa: E402
import motor                                                   # noqa: E402


def _importar_datos():
    spec = importlib.util.spec_from_file_location(
        'datos_ejemplo_churreria', os.path.join(AQUI, 'datos_ejemplo.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


D = _importar_datos()
import enmiendas_churreria                                     # noqa: E402
enmiendas_churreria.aplicar(D)      # R-04/05/06/13/14/15: el contrato de cruces enmendado
motor.CTX['producto'] = CC.PID

LIBRO = 4
FICHERO = D.LIBROS[LIBRO]
NOMBRE = os.path.splitext(FICHERO)[0]
TITULO = 'Aceite de Fritura: Coste y Cambio'
SUBJECT = CC.PRODUCTO + ' · Versión 1.0 · octubre 2026'

(H_INS, H_PAR, H_CON, H_PEC, H_ESC, H_GES) = D.HOJAS[LIBRO]
assert NOMBRE == 'aceite-de-fritura-coste-y-cambio'


def Q(hoja):
    return "'" + hoja + "'!"


def ABS_(hoja, coord):
    """Referencia absoluta a otra hoja del MISMO libro."""
    m = re.match(r'([A-Z]+)(\d+)$', coord)
    return Q(hoja) + '$' + m.group(1) + '$' + m.group(2)


# --------------------------------------------------------------------------
# Formato y utilidades (segunda capa; la primera es `_comun_churreria.py`)
# --------------------------------------------------------------------------
ORO = 'FFD700'
GRIS = '888888'
CAB_BG, CAB_FG = '2D2D2D', 'FFFFFF'
CREMA = 'FFF8E1'
EUR = motor.FMT_EUR
EUR4 = '#,##0.0000 €'
PCT = motor.FMT_PCT
ENT = motor.FMT_ENT
DEC = '#,##0.00'
DEC1 = '#,##0.0'
DEC4 = '#,##0.0000'

NOTAS_LEGALES = []
VERDES = []
CRUCE_VERDES = []        # (hoja, coord, x, concepto)
CRUCE_CUADRES = []       # (hoja, coord, x, concepto)
CONTRASTES = []          # (hoja, coord) de las cuatro identidades


def cabecera_hoja(ws, titulo, nota_txt=None):
    motor.val(ws, 'A1', CC.titulo_hoja(titulo), bold=True)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    motor.val(ws, 'A2', CC.SUBTITULO)
    ws['A2'].font = Font(size=10, color=GRIS)
    if nota_txt:
        motor.val(ws, 'A3', nota_txt)
        ws['A3'].font = Font(italic=True, size=9)


def seccion(ws, coord, texto):
    motor.val(ws, coord, texto, bold=True)
    ws[coord].font = Font(bold=True, size=12, color=ORO)


def gris(ws, coord, texto, alto=None):
    motor.val(ws, coord, texto, wrap=True)
    ws[coord].font = Font(size=8, color=GRIS)
    if alto:
        ws.row_dimensions[int(re.sub(r'[A-Z]', '', coord))].height = alto
    return ws[coord]


def texto(ws, coord, txt, alto=None, merge_hasta=None, tam=9, italica=False, negrita=False):
    if merge_hasta:
        fila = int(re.sub(r'[A-Z]', '', coord))
        ws.merge_cells('%s:%s%d' % (coord, merge_hasta, fila))
    motor.val(ws, coord, txt, wrap=True)
    ws[coord].font = Font(size=tam, italic=italica, bold=negrita)
    if alto:
        ws.row_dimensions[int(re.sub(r'[A-Z]', '', coord))].height = alto
    return ws[coord]


def encabezados(ws, fila, cols, alto=42, congelar=True):
    """`cols` = [(letra, texto, ancho|None), ...]."""
    for letra, txt, ancho in cols:
        cel = ws[letra + str(fila)]
        cel.value = txt
        cel.font = Font(bold=True, color=CAB_FG, size=9)
        cel.fill = PatternFill('solid', fgColor=CAB_BG)
        cel.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        if ancho is not None:
            ws.column_dimensions[letra].width = ancho
    ws.row_dimensions[fila].height = alto
    if congelar:
        ws.freeze_panes = 'A%d' % (fila + 1)


def crema(cel):
    cel.fill = PatternFill('solid', fgColor=CREMA)
    return cel


def entrada(ws, coord, valor, fmt=None, etiqueta=''):
    """Celda VERDE con su valor por defecto. Ninguna verde vacía."""
    if valor is None or (isinstance(valor, str) and not valor.strip()):
        raise SystemExit('entrada(%s!%s, «%s») sin valor por defecto: ninguna celda '
                         'verde puede quedar vacía' % (ws.title, coord, etiqueta))
    cel = motor.val(ws, coord, valor, fmt=fmt, verde_=True)
    VERDES.append((ws.title, coord, etiqueta, valor))
    return cel


def formula(ws, coord, txt, fmt=None, bold=None, destacar=False):
    cel = motor.f(ws, coord, txt, fmt=fmt, bold=bold)
    if destacar:
        crema(cel)
    return cel


def nota_legal(ws, coord, pid):
    txt = D.nota_legal(pid)
    if not txt:
        raise SystemExit('nota_legal(%r) vacía: gate_legal() debería haber abortado' % pid)
    ws[coord].comment = Comment(txt, 'AI Chef Pro', height=130, width=470)
    NOTAS_LEGALES.append((ws.title, coord, pid))
    return txt


RX_ID = D.RX_ID


def nota_fuente(ws, coord, fuente, extra=None):
    """Comentario de procedencia de un dato de SECTOR (CUS-*, CHS-*): id, fiabilidad y
    URL de la ficha del JSON común. No copia el «tema» de la ficha."""
    partes = []
    for pid in RX_ID.findall(fuente or ''):
        if pid in D.IDS_PROHIBIDOS:
            raise SystemExit('El id %s está PROHIBIDO (SPEC §5.1) y no puede ser fuente' % pid)
        if pid.startswith('CUN-') or pid.startswith('CHN-'):
            continue
        f = D.ficha_comun(pid)
        if not f:
            raise SystemExit('El id %s no existe en el JSON común' % pid)
        url = str(f.get('url') or '').strip()
        fiab = str(f.get('fiabilidad') or '').strip()
        partes.append('%s%s%s' % (pid, ' · fiabilidad ' + fiab if fiab else '',
                                  ' · ' + url if url else ''))
    if extra:
        partes.append(extra)
    if not partes:
        return None
    ws[coord].comment = Comment('Fuente: ' + ' | '.join(partes), 'AI Chef Pro',
                                height=110, width=440)
    return partes


def texto_fuente(fuente):
    if not fuente:
        return ''
    if fuente.startswith('supuesto'):
        return 'supuesto declarado de El Molinete' + fuente[len('supuesto'):]
    if fuente.startswith('heredado'):
        return 'heredado de la hermana o del motor'
    return fuente


def setup(ws, apaisado=True, titulos=None):
    CC.pagina(ws, apaisado=apaisado, titulos=titulos)


def version_al_pie(ws, fila, col='A'):
    motor.val(ws, '%s%d' % (col, fila), CC.VERSION_LINE)
    ws['%s%d' % (col, fila)].font = Font(size=8, italic=True)


def bloque_contrato(ws, filas, titulo='Lo que Copian Otros Libros (No Muevas Estas Celdas)'):
    """El CONTRATO de `datos_ejemplo.CRUCES`: rótulo en K y valor en L desde la fila 5."""
    seccion(ws, 'K4', titulo)
    for fila, rotulo, form, fmt in filas:
        motor.val(ws, 'K%d' % fila, rotulo, wrap=True)
        ws['K%d' % fila].font = Font(bold=True, size=9)
        formula(ws, 'L%d' % fila, form, fmt=fmt, bold=True, destacar=True)
        destinos = []
        for c in D.CRUCES:
            if (c['origen'] == LIBRO and c['hoja_origen'] == ws.title
                    and c['celda_origen'] == 'L%d' % fila):
                destinos.append('libro %d (%s, hoja %s, %s)' % (
                    c['receptor'], c['fichero_receptor'], c['hoja_receptor'], c['x']))
        if destinos:
            gris(ws, 'M%d' % fila, 'Lo copia: ' + '; '.join(sorted(set(destinos))))
        ws.row_dimensions[fila].height = max(ws.row_dimensions[fila].height or 15, 30)
    ws.column_dimensions['K'].width = max(ws.column_dimensions['K'].width or 0, 40)
    ws.column_dimensions['L'].width = max(ws.column_dimensions['L'].width or 0, 14)
    ws.column_dimensions['M'].width = max(ws.column_dimensions['M'].width or 0, 48)


# ==========================================================================
# Datos que el libro necesita (todos de `datos_ejemplo`)
# ==========================================================================
#: Los diez cruces que recibe este libro, en el orden de `CRUCES`.
CRUCES_IN = [c for c in D.CRUCES if c['receptor'] == LIBRO]
CRUCES_OUT = [c for c in D.CRUCES if c['origen'] == LIBRO]
assert len(CRUCES_IN) == 10, len(CRUCES_IN)
assert [c['origen'] for c in CRUCES_IN] == [3] * 5 + [1] * 5
assert [c['calcula'] for c in CRUCES_OUT] == ['renovacion_por_racion']
assert (CRUCES_OUT[0]['hoja_origen'], CRUCES_OUT[0]['celda_origen']) == (H_CON, 'L5')

#: Qué comprobación cuadra cada celda cruzada (ver el docstring).
IDENTIDAD = {
    'precio_aceite_eur_l': 'A', '_absorcion': 'A', '_densidad': 'A',
    'kg_masa_por_racion_media': 'C', 'aceite_absorbido_por_racion': 'A',
    '_kg_fritos_tipo': 'A', '_kg_fritos_punta': 'B', '_litros_cuba': 'D',
    '_raciones_tipo': 'A', '_raciones_punta': 'B',
}
ETIQUETA_CRUCE = {
    'precio_aceite_eur_l': ('Precio del aceite (base imponible)', 'EUR/L', EUR4),
    '_absorcion': ('Absorción de aceite, en % del peso frito', 'del peso frito', PCT),
    '_densidad': ('Densidad del aceite', 'kg/L', DEC),
    'kg_masa_por_racion_media': ('Kilos de masa por ración media (merma incluida)', 'kg/ración', DEC4),
    'aceite_absorbido_por_racion': ('Aceite absorbido por ración media', 'EUR/ración', EUR4),
    '_kg_fritos_tipo': ('Kilos fritos en un día tipo', 'kg/día', DEC1),
    '_kg_fritos_punta': ('Kilos fritos en un día punta', 'kg/día', DEC1),
    '_litros_cuba': ('Litros totales de cuba (todas las freidoras)', 'L', DEC1),
    '_raciones_tipo': ('Raciones de un día tipo (lunes a viernes)', 'raciones', ENT),
    '_raciones_punta': ('Raciones de un día punta (sábado, domingo y festivo)', 'raciones', ENT),
}
NOTA_CRUCE = {
    'precio_aceite_eur_l': ('El precio del aceite vive en UNA celda de todo el paquete, en el '
                            'libro 3. Aquí se copia; no se vuelve a pedir.'),
    '_absorcion': 'Supuesto de El Molinete en el libro 3, sin fuente pública: copia el tuyo.',
    '_densidad': ('Supuesto de El Molinete en el libro 3: hace falta porque la absorción va en '
                  'peso y el aceite se compra por litros.'),
    'kg_masa_por_racion_media': ('Con la merma: es la masa que se fríe por cada ración media '
                                 'de la carta.'),
    'aceite_absorbido_por_racion': ('Lo que se lleva la masa. Ya está dentro del coste de '
                                    'materia del libro 3; aquí sirve para el contraste con la '
                                    'renovación.'),
    '_kg_fritos_tipo': 'Lo que sale de la freidora un día de lunes a viernes.',
    '_kg_fritos_punta': 'Lo que sale de la freidora un sábado, domingo o festivo.',
    '_litros_cuba': ('Si tienes dos freidoras, la suma de las dos cubas: es lo que tiras en '
                     'cada cambio.'),
    '_raciones_tipo': 'La demanda base nace en el libro 1.',
    '_raciones_punta': 'La demanda base nace en el libro 1.',
}

# --- Parámetros: filas ------------------------------------------------------
P_CAB = 5
P_SEC3 = 6
P_SEC1 = 13
CRUCE_ROW = {}
for _i, _c in enumerate(CRUCES_IN):
    CRUCE_ROW[_c['calcula']] = (P_SEC3 + 1 + _i) if _i < 5 else (P_SEC1 + 1 + _i - 5)
assert CRUCE_ROW['aceite_absorbido_por_racion'] == 11 and CRUCE_ROW['_raciones_punta'] == 18

P_SEC_TUS = 20
P_DIAS = 21
P_REPO_T = 22
P_REPO_P = 23
P_GESTOR = 24
P_POLARES = 25
P_RETIRADOS = 26
P_SEC_CAL = 28
P_DT = 29
P_DP = 30
P_ANIO = 31
P_MES = 32
P_TOL = 33          # tolerancia de los CONTRASTES (identidades entre tus copias): 5 %
P_TOLC = 34         # tolerancia de las filas de CUADRE contra el origen: 2 %, la de la familia
P_SEC_CON = 36      # «Contraste entre tus Copias»: las cuatro identidades (R-01)
P_A_RECALC = 37
P_A_DEV = 38
P_B_KG = 39
P_B_RAC = 40
P_B_DEV = 41
P_C_RATIO = 42
P_C_MAX = 43
P_D_REPO = 44
P_CON_CAB = 45
P_CON_INI = 46      # A, B, C, D: 46..49
P_SEC_CUA = 51      # «Cuadre de lo que Has Copiado»: UNA fila por celda cruzada
P_CUA_CAB = 52
P_CUA_INI = 53
CUADRE_ROW = dict((c['calcula'], P_CUA_INI + i) for i, c in enumerate(CRUCES_IN))
P_CUA_FIN = P_CUA_INI + len(CRUCES_IN) - 1


def PB(fila):
    return ABS_(H_PAR, 'B%d' % fila)


def XB(clave):
    """Celda verde del cruce `clave` (nombre de la función de `datos_ejemplo`)."""
    return PB(CRUCE_ROW[clave])


#: Días tipo y punta de la semana: de lunes a viernes y de sábado a domingo, el
#: reparto de `datos_ejemplo.raciones_dia_medio_semana()` (horario de El Molinete).
DIAS_TIPO_SEMANA = 5
DIAS_PUNTA_SEMANA = 2
assert abs((DIAS_TIPO_SEMANA * D.dato(D.PRODUCCION, 'raciones_dia_tipo')
            + DIAS_PUNTA_SEMANA * D.dato(D.PRODUCCION, 'raciones_dia_punta'))
           / float(DIAS_TIPO_SEMANA + DIAS_PUNTA_SEMANA) - D.raciones_dia_medio_semana()) < 1e-9
#: Días naturales del año: la renovación cuenta días de calendario entre cambios
#: (como el registro del Pack APPCC, que va por fechas), igual que
#: `datos_ejemplo.litros_al_gestor_mes()`.
DIAS_ANIO = 365
assert abs(D.renovacion_litros_dia() * DIAS_ANIO / 12.0 - D.litros_al_gestor_mes()) < 1e-9
#: Tolerancia de cuadres y contrastes: supuesto declarado de este libro.
TOLERANCIA = 0.05            # de los contrastes (la reposición que mides frente a la absorción)
TOLERANCIA_CUADRE = 0.02     # la de la familia («heredado», como en los libros 1, 2, 5 y 6)

# --- Consumo y Reposición ---------------------------------------------------
C_CUBA, C_DIAS, C_LDIA, C_PRECIO, C_EDIA, C_RACMED, C_RENRAC, C_DMES, C_EMES = range(5, 14)
C_SEC_REP = 15
C_REP_CAB = 16
C_KGF, C_REPO, C_REPO_ABS, C_DEV, C_VERED, C_REPO_EUR, C_REPO_RAC = range(17, 24)
C_SEC_COM = 25
C_COM_CAB = 26
C_COM_L, C_COM_E = 27, 28
C_SEC_CON = 30
C_ABS3, C_REN4, C_TOTAL, C_PARTE, C_REPRAC, C_DIF = range(31, 37)
C_KGM, C_ABSKG, C_RENKG, C_TOTKG = range(37, 41)       # R-15: litros y euros POR KILO DE MASA
C_LEG = 42

# --- Punto Económico de Cambio ----------------------------------------------
PE_CAB = 6
PE_DIAS = (3, 4, 5, 6, 7, 8, 9, 10)
PE_INI = 7
PE_FIN = PE_INI + len(PE_DIAS) - 1
PE_SEC = PE_FIN + 2
PE_CICLO, PE_RENMES, PE_ANTES, PE_DESPUES, PE_EQUI, PE_VERED, PE_LIMITE = range(PE_SEC + 1, PE_SEC + 8)
assert D.dato(D.ACEITE, 'dias_entre_cambios') in PE_DIAS

# --- Escenarios ---------------------------------------------------------------
E_CAB = 6
E_HOY = 7
E_INI = 8
SUBIDAS = D.dato(D.ACEITE, 'subidas_de_precio')
E_FIN = E_INI + len(SUBIDAS) - 1

# --- Gestor ---------------------------------------------------------------------
G_LDIA, G_DMES, G_LMES, G_LANIO, G_CMES, G_CANIO, G_CRAC = range(5, 12)
G_SEC_REG = 13
G_RET, G_DEV, G_VERED = 14, 15, 16
G_SEC_LEG = 18


# ==========================================================================
# Hoja «Instrucciones»
# ==========================================================================
def _orden_relleno():
    partes = ['%d (%s)' % (n, D.LIBROS[n]) for n in D.ORDEN_RELLENO if n != 7]
    return ('Orden de relleno del paquete: ' + ', luego '.join(partes)
            + '. El libro 7 (%s) no depende de ninguno: rellénalo cuando quieras. '
              'Este es el libro 4: rellénalo DESPUÉS del 3 y del 1, que le pasan sus cifras, '
              'y ANTES del 6, que copia la renovación por ración.' % D.LIBROS[7])


def _cruces_texto():
    lineas = []
    for c in CRUCES_IN:
        lineas.append('Parámetros!B%d - %s. Viene del libro %d: %s!%s!%s.' % (
            CRUCE_ROW[c['calcula']], c['concepto'], c['origen'], c['fichero_origen'],
            c['hoja_origen'], c['celda_origen']))
    for c in CRUCES_OUT:
        lineas.append('%s!%s - %s. Lo copia: libro %d (%s, %s).' % (
            c['hoja_origen'], c['celda_origen'], c['concepto'], c['receptor'],
            c['fichero_receptor'], c['x']))
    return lineas


PASOS = [
    '1. Hoja «Parámetros». Arriba, diez celdas verdes que copias a mano de los libros 3 y 1 '
    '(cada una dice de qué celda exacta). Debajo, tus datos del aceite: cada cuántos días '
    'cambias la cuba, cuánto repones al día y lo que te cobra el gestor. Al pie, primero el '
    'CONTRASTE (si tus copias son coherentes entre sí) y después el CUADRE: anota lo que '
    'publica hoy la celda de origen de cada cifra y, si lo que usas se separa, su fila se '
    'pone en rojo.',
    '2. Hoja «Consumo y Reposición». Lo que tiras al cambiar la cuba (la renovación), lo que '
    'añades cada día para que no baje (la reposición) y lo que compras al mes. Aquí sale la '
    'renovación por ración que copia el libro 6, y la fila de contraste: aceite absorbido '
    '(libro 3) más renovación (este libro) igual a aceite total por ración.',
    '3. Hoja «Punto Económico de Cambio». Cuánto cuesta cada ciclo de cambio, de 3 a 10 días '
    '(los días de la tabla se pueden cambiar), lo que te cuesta adelantar un día y lo que '
    'ahorras alargando uno. El límite no lo pone el dinero: lo pone el medidor.',
    '4. Hoja «Escenarios de Precio del Aceite». Tres subidas del precio del aceite (sólo se '
    'teclea el porcentaje) y el margen que pierdes por ración, al mes y al año si no tocas '
    'el PVP.',
    '5. Hoja «Gestor de Aceite Usado». Los litros que se lleva el gestor al mes y al año, lo '
    'que cuesta, el contraste con tu registro de retiradas y los papeles que tienes que '
    'guardar.',
]

NOTAS_LIBRO = [
    'ESTE LIBRO NO ES UN REGISTRO APPCC. El registro del aceite (lecturas del medidor, '
    'cambios y retiradas) es el del Pack APPCC, fichero 09-control-aceite-fritura.xlsx: '
    'aquí se cita, no se copia. Si lo tienes, los días entre cambios salen de contar los días '
    'entre dos filas con «cambio de aceite» en su hoja «Control Aceite», y los litros que se '
    'llevó el gestor, de su hoja «Retirada de aceite usado».',
    'DOS ACEITES DISTINTOS POR RACIÓN. El que se lleva la masa (aceite absorbido) ya está en '
    'el coste de materia del libro 3. El que tiras al cambiar la cuba (renovación) lo calcula '
    'este libro. El plan financiero del libro 6 suma los dos, cada uno con su fuente: si '
    'metieras la renovación también en el libro 3, la contarías dos veces.',
    'NO COMPARA MARCAS NI TIPOS DE ACEITE. Trabaja con TU aceite, TU precio y TU ciclo de '
    'cambio. Lo que dure tu aceite lo dicen tu medidor y tu registro, no una ficha comercial.',
    'EL MEDIDOR DE MANO TE DICE CUÁNDO CAMBIAR; EL 25 % LEGAL SE PRUEBA EN LABORATORIO. La '
    'norma fija los compuestos polares por debajo del 25 %, medidos con el método de su '
    'anexo 1 (cromatografía en columna). El medidor es una ayuda para decidir, no la prueba.',
    'SIN TEMPERATURA DE FRITURA DEL CHURRO. No hay una fuente primaria que la fije y este '
    'paquete no da ninguna. Si además fríes patatas frescas, te toca la parte A del '
    'reglamento de la acrilamida (su temperatura máxima de fritura es para las PATATAS, no '
    'para el churro): mira la nota de esta celda y la hoja de alérgenos y acrilamida del '
    'libro 7.',
    'LOS SUPUESTOS NO SON DATOS DEL SECTOR. Los días entre cambios, la reposición diaria, la '
    'tolerancia de los cuadres y los días de la tabla de ciclos son supuestos declarados de '
    'El Molinete, sin fuente pública. Pon los tuyos.',
]

CADENCIA = ('Cada cuánto se usa este libro: los días entre cambios y la reposición, al mes de '
            'abrir con tu registro y cada vez que cambies de aceite o de freidora. El precio, '
            'cada vez que te suba el proveedor (lo cambias en el libro 3 y lo copias aquí). Si '
            'cambia la renovación por ración del bloque «Lo que Copian Otros Libros», cópiala '
            'de nuevo en el libro 6.')


def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS, 0)
    ws.column_dimensions['A'].width = 100.0
    cabecera_hoja(ws, TITULO)
    motor.val(ws, 'A3', 'Para qué sirve: saber cuánto te cuesta el aceite por ración y al mes, '
                        'cada cuántos días te sale a cuenta cambiar la cuba, qué te hace una '
                        'subida del precio y cuánto aceite usado sale hacia el gestor.')
    ws['A3'].font = Font(italic=True, size=9)
    fila = 5
    seccion(ws, 'A%d' % fila, 'Instrucciones de Uso')
    fila += 1
    entrada(ws, 'A%d' % fila, motor.NOTA_VERDES, etiqueta='Leyenda de celdas verdes')
    fila += 1
    motor.val(ws, 'A%d' % fila, 'Las celdas en crema son resultados que el libro calcula; las '
                                'blancas con fórmula, también. No escribas encima.', wrap=True)
    fila += 2
    for paso in PASOS:
        motor.val(ws, 'A%d' % fila, paso, wrap=True)
        ws.row_dimensions[fila].height = 58
        fila += 1
    fila += 1
    seccion(ws, 'A%d' % fila, 'Orden de Relleno y Cifras que Viajan')
    fila += 1
    motor.val(ws, 'A%d' % fila, _orden_relleno(), wrap=True)
    ws.row_dimensions[fila].height = 58
    fila += 1
    motor.val(ws, 'A%d' % fila,
              'Ningún libro se vincula con otro por fórmula. Lo que viene de otro libro tiene en '
              '«Parámetros» una celda verde para copiarlo a mano, con la celda exacta de origen, '
              'y una fila de CUADRE que avisa si se ha quedado vieja frente a las demás. Lo que '
              'este libro pasa a otro está en el bloque «Lo que Copian Otros Libros» (rótulo en '
              'la columna K, valor en la L).', wrap=True)
    ws.row_dimensions[fila].height = 58
    fila += 1
    for linea in _cruces_texto():
        motor.val(ws, 'A%d' % fila, linea, wrap=True)
        ws['A%d' % fila].font = Font(size=9)
        ws.row_dimensions[fila].height = 28
        fila += 1
    fila += 1
    seccion(ws, 'A%d' % fila, 'Lo que Conviene Saber Antes de Empezar')
    fila += 1
    for i, txt in enumerate(NOTAS_LIBRO):
        motor.val(ws, 'A%d' % fila, txt, wrap=True)
        ws.row_dimensions[fila].height = 72
        if txt.startswith('ESTE LIBRO NO ES'):
            nota_fuente(ws, 'A%d' % fila, '', extra='Registro del lector: %s y %s'
                        % D.REGISTRO_DEL_LECTOR)
        if txt.startswith('SIN TEMPERATURA'):
            nota_legal(ws, 'A%d' % fila, 'CUN-05')
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, CADENCIA, wrap=True)
    ws.row_dimensions[fila].height = 58
    fila += 2
    motor.val(ws, 'A%d' % fila, CC.NOTA_DESPROTEGER, wrap=True)
    fila += 2
    motor.val(ws, 'A%d' % fila, CC.BIO, wrap=True)
    fila += 1
    version_al_pie(ws, fila)
    setup(ws, apaisado=False)
    return ws


# ==========================================================================
# Hoja «Parámetros»
# ==========================================================================
def fila_param(ws, fila, etiqueta, valor, fmt, unidad, origen, nota, pct=False, form=None,
               minimo=0, legal=None, fuente_sector=None):
    motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
    if form is not None:
        cel = formula(ws, 'B%d' % fila, form, fmt=fmt, bold=True, destacar=True)
    else:
        cel = entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
        if pct:
            motor.dv_porcentaje(ws, [cel.coordinate])
        else:
            motor.dv_numerica(ws, [cel.coordinate], minimo=minimo)
    motor.val(ws, 'C%d' % fila, unidad)
    motor.val(ws, 'D%d' % fila, origen, wrap=True)
    ws['D%d' % fila].font = Font(size=8, color=GRIS)
    gris(ws, 'E%d' % fila, nota)
    ws.row_dimensions[fila].height = 44
    if legal:
        nota_legal(ws, cel.coordinate, legal)
    elif fuente_sector:
        nota_fuente(ws, cel.coordinate, fuente_sector)
    return cel


def _veredicto(cond_ko, guardas, ko):
    """«COHERENTE» / «INCOHERENTE: ...» / "" si falta algún dato (ISNUMBER)."""
    return '=IF(AND(%s),IF(%s,"%s","COHERENTE"),"")' % (
        ','.join('ISNUMBER(%s)' % g for g in guardas), cond_ko, ko)


KO = {
    'A': ('INCOHERENTE: el aceite absorbido, el precio, la absorción, la densidad, los kilos '
          'fritos y las raciones del día tipo no salen de la misma versión de los libros 3 y '
          '1; vuelve a copiarlos'),
    'B': ('INCOHERENTE: los kilos fritos y las raciones del día punta no guardan la proporción '
          'del día tipo; vuelve a copiar el libro 1'),
    'C': ('INCOHERENTE: con esta masa por ración no salen los kilos fritos del libro 1; vuelve a '
          'copiar la masa por ración del libro 3'),
    'D': ('INCOHERENTE: repondrías más de una cuba entera en un día punta; revisa los litros de '
          'cuba y los kilos fritos del libro 1'),
}
QUE_COMPARA_CORTO = {
    'A': 'aceite absorbido por ración',
    'B': 'proporción punta/tipo',
    'C': 'masa por ración y kilos fritos',
    'D': 'reposición del día punta frente a la cuba',
}
QUE_COMPARA = {
    'A': 'Aceite absorbido copiado del libro 3 frente al que sale de recalcularlo con las demás '
         'cifras copiadas (filas %d y %d)' % (P_A_RECALC, P_A_DEV),
    'B': 'Proporción punta/tipo de los kilos fritos frente a la de las raciones (filas %d a %d)'
         % (P_B_KG, P_B_DEV),
    'C': 'Kilos fritos por kilo de masa que implican tus copias frente al máximo físico con tu '
         'absorción (filas %d y %d)' % (P_C_RATIO, P_C_MAX),
    'D': 'Reposición que pide un día punta según tu absorción frente a los litros de cuba '
         '(fila %d)' % P_D_REPO,
}


def hoja_parametros(wb):
    ws = wb.create_sheet(H_PAR)
    cabecera_hoja(ws, H_PAR, 'Todo lo que el resto de hojas da por sabido vive aquí. Ninguna '
                             'fórmula de este libro lleva dentro un precio, un umbral ni un '
                             'número de días.')
    for letra, ancho in (('A', 54), ('B', 16), ('C', 15), ('D', 46), ('E', 66)):
        ws.column_dimensions[letra].width = ancho
    encabezados(ws, P_CAB, [('A', 'Parámetro', None), ('B', 'Valor', None),
                            ('C', 'Unidad', None), ('D', 'De dónde sale', None),
                            ('E', 'Nota', None)], alto=24)

    seccion(ws, 'A%d' % P_SEC3, 'Lo que Copias del Libro 3 (Carta y Escandallo)')
    seccion(ws, 'A%d' % P_SEC1, 'Lo que Copias del Libro 1 (Producción y Local)')
    for c in CRUCES_IN:
        clave = c['calcula']
        etq, uni, fmt = ETIQUETA_CRUCE[clave]
        fila = CRUCE_ROW[clave]
        valor = c['valor_defecto']
        if fmt == ENT:
            valor = int(round(valor))
        cel = fila_param(ws, fila, etq, valor, fmt, uni, D.rotulo_cruce(c), NOTA_CRUCE[clave],
                         pct=(fmt == PCT), minimo=0)
        CRUCE_VERDES.append((ws.title, cel.coordinate, c['x'], c['concepto']))
        if clave == 'precio_aceite_eur_l':
            nota_fuente(ws, cel.coordinate, D.INSUMOS['aceite']['fuente'],
                        extra='Se copia del libro 3, donde vive la celda única del precio.')

    seccion(ws, 'A%d' % P_SEC_TUS, 'Tus Datos del Aceite')
    v, fuente, _n = D.ACEITE['dias_entre_cambios']
    fila_param(ws, P_DIAS, 'Días entre cambios de aceite (cada cuántos días vacías la cuba)',
               v, ENT, 'días', texto_fuente(fuente),
               'Supuesto declarado de El Molinete. Si tienes el Pack APPCC, usa tu registro: '
               'cuenta los días entre dos filas con «cambio de aceite» en su hoja «Control '
               'Aceite» (09-control-aceite-fritura.xlsx).', minimo=1)
    fila_param(ws, P_REPO_T, 'Aceite que repones en un día tipo', round(D.reposicion_litros_dia('tipo'), 2),
               DEC, 'L/día', 'supuesto declarado de El Molinete (calculado con su absorción)',
               'El aceite nuevo que añades para que la cuba no baje. Mídelo una semana: los '
               'litros que entran en la freidora sin contar los cambios. La hoja «Consumo y '
               'Reposición» lo contrasta con la absorción del libro 3.')
    fila_param(ws, P_REPO_P, 'Aceite que repones en un día punta', round(D.reposicion_litros_dia('punta'), 2),
               DEC, 'L/día', 'supuesto declarado de El Molinete (calculado con su absorción)',
               'Lo mismo un sábado, domingo o festivo.')
    v, fuente, _n = D.ACEITE['coste_gestor_mes']
    fila_param(ws, P_GESTOR, 'Lo que te cobra el gestor de aceite usado al mes (base imponible)',
               v, EUR, 'EUR/mes', texto_fuente(fuente),
               'En el ejemplo el gestor recoge a cambio de obsequios, servicios gratuitos o '
               'valoración económica: la recogida no cuesta. Si el tuyo cobra, pon aquí su '
               'importe sin IVA.', fuente_sector='CUS-44h')
    v, fuente, _n = D.ACEITE['compuestos_polares_max_pct']
    fila_param(ws, P_POLARES, 'Compuestos polares: el aceite tiene que estar por debajo de',
               v / 100.0, PCT, 'del aceite', fuente,
               'Límite legal, medido con el método del anexo 1 de la norma (cromatografía en '
               'columna, en laboratorio). El medidor de mano te dice cuándo cambiar; el 25 % '
               'legal se prueba en laboratorio.', pct=True, legal='CUN-02')
    fila_param(ws, P_RETIRADOS, 'Litros que retiró tu gestor el último mes (de tu registro)',
               round(D.litros_al_gestor_mes(), 1), DEC1, 'L/mes',
               'supuesto declarado de El Molinete (lo que calcula este libro)',
               'Anótalo de la hoja «Retirada de aceite usado» del Pack APPCC 09. La hoja «Gestor '
               'de Aceite Usado» lo contrasta con lo que renuevas.')

    seccion(ws, 'A%d' % P_SEC_CAL, 'Calendario y Tolerancia')
    fila_param(ws, P_DT, 'Días tipo a la semana', DIAS_TIPO_SEMANA, ENT, 'días',
               'supuesto declarado de El Molinete (horario: de lunes a viernes)',
               'Los días con las raciones del día tipo. Pesan en la ración media de la semana.',
               minimo=0)
    fila_param(ws, P_DP, 'Días punta a la semana', DIAS_PUNTA_SEMANA, ENT, 'días',
               'supuesto declarado de El Molinete (horario: sábado y domingo)',
               'Los días con las raciones del día punta. Si cierras un día, réstalo de su grupo.',
               minimo=0)
    fila_param(ws, P_ANIO, 'Días naturales del año', DIAS_ANIO, ENT, 'días', 'calendario',
               'Los cambios de aceite se cuentan en días de calendario, como en el registro, '
               'que va por fechas.', minimo=1)
    fila_param(ws, P_MES, 'Días naturales por mes (media)', None, DEC, 'días', 'calculado',
               'Días del año entre los doce meses.', form='=IFERROR(%s/12,"")' % PB(P_ANIO))
    fila_param(ws, P_TOL, 'Tolerancia de los contrastes', TOLERANCIA, PCT, '',
               'supuesto declarado de este libro',
               'Cuánto pueden separarse dos cifras que deberían coincidir (lo que repones frente '
               'a lo que dice la absorción, las proporciones punta/tipo) antes de que la hoja '
               'avise.', pct=True)
    fila_param(ws, P_TOLC, 'Tolerancia de las filas de CUADRE', TOLERANCIA_CUADRE, PCT, '',
               'heredado de la Guía de la Chocolatería (tolerancia de las filas de CUADRE)',
               'Por encima de esta desviación, la fila de CUADRE avisa de que lo que has copiado '
               'no es lo que publica el libro de origen.', pct=True)

    # --- CONTRASTE entre tus copias (las identidades) ------------------------------
    seccion(ws, 'A%d' % P_SEC_CON, 'Contraste entre tus Copias')
    t = PB(P_TOL)
    comprob = (
        (P_A_RECALC, 'Aceite absorbido por ración, recalculado con tus copias (kg fritos del día '
                     'tipo / raciones del día tipo x absorción / densidad x precio)',
         '=IFERROR(%s/%s*%s/%s*%s,"")' % (XB('_kg_fritos_tipo'), XB('_raciones_tipo'),
                                          XB('_absorcion'), XB('_densidad'),
                                          XB('precio_aceite_eur_l')), EUR4, 'EUR/ración'),
        (P_A_DEV, 'Separación entre el aceite absorbido copiado y el recalculado',
         '=IFERROR(ABS(B%d/%s-1),"")' % (P_A_RECALC, XB('aceite_absorbido_por_racion')), PCT, ''),
        (P_B_KG, 'Kilos fritos del día punta entre los del día tipo',
         '=IFERROR(%s/%s,"")' % (XB('_kg_fritos_punta'), XB('_kg_fritos_tipo')), DEC4, 'veces'),
        (P_B_RAC, 'Raciones del día punta entre las del día tipo',
         '=IFERROR(%s/%s,"")' % (XB('_raciones_punta'), XB('_raciones_tipo')), DEC4, 'veces'),
        (P_B_DEV, 'Separación entre las dos proporciones',
         '=IFERROR(ABS(B%d/B%d-1),"")' % (P_B_KG, P_B_RAC), PCT, ''),
        (P_C_RATIO, 'Kilos fritos por kilo de masa que implican tus copias',
         '=IFERROR(%s/(%s*%s),"")' % (XB('_kg_fritos_tipo'), XB('_raciones_tipo'),
                                      XB('kg_masa_por_racion_media')), DEC4, 'kg/kg'),
        (P_C_MAX, 'Máximo físico con tu absorción: 1 / (1 - absorción)',
         '=IFERROR(1/(1-%s),"")' % XB('_absorcion'), DEC4, 'kg/kg'),
        (P_D_REPO, 'Litros que repondrías en un día punta según tu absorción',
         '=IFERROR(%s*%s/%s,"")' % (XB('_kg_fritos_punta'), XB('_absorcion'), XB('_densidad')),
         DEC, 'L/día'),
    )
    for fila, etq, form, fmt, uni in comprob:
        motor.val(ws, 'A%d' % fila, etq, wrap=True)
        ws['A%d' % fila].font = Font(size=9)
        formula(ws, 'B%d' % fila, form, fmt=fmt)
        motor.val(ws, 'C%d' % fila, uni)
        ws.row_dimensions[fila].height = 30
    gris(ws, 'D%d' % P_A_RECALC, 'Con las cifras de El Molinete coinciden al céntimo: salen de '
                                 'los mismos supuestos. Si una se ha copiado de una versión '
                                 'vieja, se separan.')
    gris(ws, 'D%d' % P_C_MAX, 'La pieza frita pierde agua y gana aceite: por cada kilo de masa '
                              'no puede salir más de esto.')

    encabezados(ws, P_CON_CAB, [('A', 'Contraste', None), ('B', 'Veredicto', None),
                                ('C', 'Celdas que compara', None), ('D', 'Qué compara', None),
                                ('E', 'Si no es coherente', None)], alto=24, congelar=False)
    celdas_de = {
        'A': ('aceite_absorbido_por_racion', 'precio_aceite_eur_l', '_absorcion', '_densidad',
              '_kg_fritos_tipo', '_raciones_tipo'),
        'B': ('_kg_fritos_punta', '_kg_fritos_tipo', '_raciones_punta', '_raciones_tipo'),
        'C': ('_kg_fritos_tipo', '_raciones_tipo', 'kg_masa_por_racion_media', '_absorcion'),
        'D': ('_kg_fritos_punta', '_absorcion', '_densidad', '_litros_cuba'),
    }
    for k, ident in enumerate('ABCD'):
        fila = P_CON_INI + k
        motor.val(ws, 'A%d' % fila, 'Contraste %s · %s' % (ident, QUE_COMPARA_CORTO[ident]), wrap=True)
        ws['A%d' % fila].font = Font(bold=True, size=9)
        if ident == 'A':
            form = _veredicto('B%d>%s' % (P_A_DEV, t), ['B%d' % P_A_DEV], KO['A'])
        elif ident == 'B':
            form = _veredicto('B%d>%s' % (P_B_DEV, t), ['B%d' % P_B_DEV], KO['B'])
        elif ident == 'C':
            form = _veredicto('B%d>B%d' % (P_C_RATIO, P_C_MAX),
                              ['B%d' % P_C_RATIO, 'B%d' % P_C_MAX], KO['C'])
        else:
            form = _veredicto('B%d>%s' % (P_D_REPO, XB('_litros_cuba')),
                              ['B%d' % P_D_REPO, XB('_litros_cuba')], KO['D'])
        cel = formula(ws, 'B%d' % fila, form, bold=True)
        cel.alignment = Alignment(wrap_text=True, vertical='top')
        motor.semaforo_texto(ws, 'B%d' % fila, (
            ('COHERENTE', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
            (KO[ident], motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
        motor.val(ws, 'C%d' % fila, ', '.join('B%d' % CRUCE_ROW[x] for x in celdas_de[ident]))
        gris(ws, 'D%d' % fila, QUE_COMPARA[ident])
        gris(ws, 'E%d' % fila, 'Vuelve a copiar las cifras del libro 3 y del libro 1: alguna es de '
                               'otra versión.')
        ws.row_dimensions[fila].height = 48
    CONTRASTES.extend((H_PAR, 'B%d' % (P_CON_INI + k)) for k in range(4))

    # --- CUADRE: UNA fila por celda cruzada, contra lo que publica el origen (R-01) -------
    seccion(ws, 'A%d' % P_SEC_CUA, 'Cuadre de lo que Has Copiado')
    encabezados(ws, P_CUA_CAB, [('A', 'Cuadre', None),
                                ('B', 'Lo que publica hoy la celda de origen (anótalo)', None),
                                ('C', 'Desviación', None), ('D', 'Veredicto', None),
                                ('E', 'Si no cuadra', None)], alto=36, congelar=False)
    tc = PB(P_TOLC)
    for c in CRUCES_IN:
        clave = c['calcula']
        fila = CUADRE_ROW[clave]
        etq, _uni, fmt = ETIQUETA_CRUCE[clave]
        motor.val(ws, 'A%d' % fila, 'CUADRE · %s (%s)' % (etq, c['x']), wrap=True)
        ws['A%d' % fila].font = Font(bold=True, size=9)
        valor = c['valor_defecto']
        if fmt == ENT:
            valor = int(round(valor))
        cel = entrada(ws, 'B%d' % fila, valor, fmt=fmt,
                      etiqueta='%s: lo que publica el libro %d' % (c['x'], c['origen']))
        motor.dv_numerica(ws, [cel.coordinate], minimo=0)
        formula(ws, 'C%d' % fila, '=IFERROR(ABS(%s-B%d)/B%d,"")' % (XB(clave), fila, fila), fmt=PCT)
        ko = 'REVISA: no es lo que publica el libro %d' % c['origen']
        cel = formula(ws, 'D%d' % fila, '=IF(NOT(ISNUMBER(C%d)),"",IF(C%d<=%s,"CUADRA","%s"))'
                      % (fila, fila, tc, ko), bold=True)
        cel.alignment = Alignment(wrap_text=True, vertical='top')
        motor.semaforo_texto(ws, 'D%d' % fila, (
            ('CUADRA', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
            (ko, motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
        gris(ws, 'E%d' % fila, 'Vuelve a copiar la cifra de su celda de origen (libro %d, %s!%s!%s) '
                               'en la fila %d, o anota aquí lo que publica hoy.'
             % (c['origen'], c['fichero_origen'], c['hoja_origen'], c['celda_origen'],
                CRUCE_ROW[clave]))
        ws.row_dimensions[fila].height = 40
        CRUCE_CUADRES.append((ws.title, 'D%d' % fila, c['x'], c['concepto']))
    version_al_pie(ws, P_CUA_FIN + 2)
    setup(ws, apaisado=True)
    return ws


# ==========================================================================
# Hoja «Consumo y Reposición»
# ==========================================================================
def hoja_consumo(wb):
    ws = wb.create_sheet(H_CON)
    cabecera_hoja(ws, H_CON, 'Lo que tiras al cambiar la cuba, lo que añades cada día y lo que '
                             'compras. El aceite que se lleva la masa (absorbido) está en el '
                             'libro 3.')
    for letra, ancho in (('A', 58), ('B', 16), ('C', 16), ('D', 17), ('E', 16), ('F', 4),
                         ('G', 44)):
        ws.column_dimensions[letra].width = ancho
    dt, dp = PB(P_DT), PB(P_DP)
    rt, rp = XB('_raciones_tipo'), XB('_raciones_punta')
    precio = XB('precio_aceite_eur_l')

    seccion(ws, 'A4', 'Renovación: el Aceite que Tiras al Cambiar la Cuba')
    filas = (
        (C_CUBA, 'Litros de cuba (todas las freidoras)', '=%s' % XB('_litros_cuba'), DEC1, 'L'),
        (C_DIAS, 'Días entre cambios', '=%s' % PB(P_DIAS), ENT, 'días'),
        (C_LDIA, 'Litros renovados por día', '=IFERROR(B%d/B%d,"")' % (C_CUBA, C_DIAS), DEC, 'L/día'),
        (C_PRECIO, 'Precio del aceite (base imponible)', '=%s' % precio, EUR4, 'EUR/L'),
        (C_EDIA, 'Renovación en euros por día', '=IFERROR(B%d*B%d,"")' % (C_LDIA, C_PRECIO), EUR, 'EUR/día'),
        (C_RACMED, 'Raciones de un día medio de la semana',
         '=IFERROR((%s*%s+%s*%s)/(%s+%s),"")' % (dt, rt, dp, rp, dt, dp), DEC1, 'raciones/día'),
        (C_RENRAC, 'RENOVACIÓN POR RACIÓN', '=IFERROR(B%d/B%d,"")' % (C_EDIA, C_RACMED), EUR4,
         'EUR/ración'),
        (C_DMES, 'Días naturales por mes (media)', '=%s' % PB(P_MES), DEC, 'días'),
        (C_EMES, 'Renovación en euros al mes', '=IFERROR(B%d*B%d,"")' % (C_EDIA, C_DMES), EUR, 'EUR/mes'),
    )
    for fila, etq, form, fmt, uni in filas:
        motor.val(ws, 'A%d' % fila, etq, bold=fila == C_RENRAC)
        formula(ws, 'B%d' % fila, form, fmt=fmt, bold=fila in (C_RENRAC, C_EMES),
                destacar=fila in (C_RENRAC, C_EMES))
        motor.val(ws, 'C%d' % fila, uni)
    gris(ws, 'D%d' % C_RENRAC, 'La copia el libro 6 (bloque de la derecha). Va sobre la ración '
                               'media de la semana: cinco días tipo y dos punta, sin festivos ni '
                               'días cerrados. El libro 6 la multiplica por las raciones del año, '
                               'que sí los cuentan: por eso su cifra anual y la de este libro '
                               'pueden separarse en torno a un 0,5 %.', alto=64)
    ws.merge_cells('D%d:G%d' % (C_RENRAC, C_RENRAC))

    # --- reposición -------------------------------------------------------------
    seccion(ws, 'A%d' % C_SEC_REP, 'Reposición: el Aceite que Añades para que la Cuba no Baje')
    encabezados(ws, C_REP_CAB, [('A', 'Concepto', None), ('B', 'Día tipo', None),
                                ('C', 'Día punta', None), ('D', 'Media de la semana', None),
                                ('E', 'Unidad', None)], alto=30, congelar=False)
    tol = PB(P_TOL)
    ok_txt = 'Tu reposición cuadra con la absorción del libro 3'
    mas_txt = ('Repones más de lo que dice la absorción del libro 3: revísala, o busca '
               'derrames y fugas')
    menos_txt = 'Repones menos de lo que dice la absorción del libro 3: revísala'
    fuentes = {'B': (XB('_kg_fritos_tipo'), PB(P_REPO_T)), 'C': (XB('_kg_fritos_punta'), PB(P_REPO_P))}
    for col, (kgf, repo) in fuentes.items():
        formula(ws, '%s%d' % (col, C_KGF), '=%s' % kgf, fmt=DEC1)
        formula(ws, '%s%d' % (col, C_REPO), '=%s' % repo, fmt=DEC)
        formula(ws, '%s%d' % (col, C_REPO_ABS), '=IFERROR(%s%d*%s/%s,"")'
                % (col, C_KGF, XB('_absorcion'), XB('_densidad')), fmt=DEC)
        formula(ws, '%s%d' % (col, C_REPO_EUR), '=IFERROR(%s%d*%s,"")' % (col, C_REPO, precio), fmt=EUR)
        racs = rt if col == 'B' else rp
        formula(ws, '%s%d' % (col, C_REPO_RAC), '=IFERROR(%s%d/%s,"")' % (col, C_REPO_EUR, racs), fmt=EUR4)
    media = lambda f: '=IFERROR((%s*B%d+%s*C%d)/(%s+%s),"")' % (dt, f, dp, f, dt, dp)  # noqa: E731
    for fila, fmt in ((C_KGF, DEC1), (C_REPO, DEC), (C_REPO_ABS, DEC), (C_REPO_EUR, EUR)):
        formula(ws, 'D%d' % fila, media(fila), fmt=fmt)
    formula(ws, 'D%d' % C_REPO_RAC, '=IFERROR((%s*B%d+%s*C%d)/(%s*%s+%s*%s),"")'
            % (dt, C_REPO_EUR, dp, C_REPO_EUR, dt, rt, dp, rp), fmt=EUR4)
    for col in 'BCD':
        formula(ws, '%s%d' % (col, C_DEV), '=IFERROR(%s%d/%s%d-1,"")' % (col, C_REPO, col, C_REPO_ABS),
                fmt=PCT)
        cel = formula(ws, '%s%d' % (col, C_VERED),
                      '=IF(ISNUMBER({c}{d}),IF({c}{d}>{t},"{mas}",IF({c}{d}<-{t},"{menos}","{ok}")),"")'
                      .format(c=col, d=C_DEV, t=tol, mas=mas_txt, menos=menos_txt, ok=ok_txt),
                      bold=True)
        cel.alignment = Alignment(wrap_text=True, vertical='top')
    motor.semaforo_texto(ws, 'B%d:D%d' % (C_VERED, C_VERED), (
        (ok_txt, motor.CF_VERDE_BG, motor.CF_VERDE_FG),
        (mas_txt, motor.CF_ROJO_BG, motor.CF_ROJO_FG),
        (menos_txt, motor.CF_AMBAR_BG, motor.CF_AMBAR_FG)))
    ws.row_dimensions[C_VERED].height = 58
    for fila, etq, uni in (
            (C_KGF, 'Kilos fritos (copiados del libro 1)', 'kg/día'),
            (C_REPO, 'Reposición que mides (Parámetros)', 'L/día'),
            (C_REPO_ABS, 'Reposición que sale de la absorción del libro 3 (kg fritos x absorción / '
                         'densidad)', 'L/día'),
            (C_DEV, 'Lo que repones de más (+) o de menos (-) frente a la absorción', ''),
            (C_VERED, 'Contraste', ''),
            (C_REPO_EUR, 'Reposición en euros', 'EUR/día'),
            (C_REPO_RAC, 'Reposición en euros por ración', 'EUR/ración')):
        motor.val(ws, 'A%d' % fila, etq, wrap=True, bold=fila == C_VERED)
        motor.val(ws, 'E%d' % fila, uni)
        ws.row_dimensions[fila].height = max(ws.row_dimensions[fila].height or 15, 30)
    texto(ws, 'G%d' % C_REPO, 'Reponer es una decisión de cocina, no un permiso de la norma: el '
                              'aceite se cambia cuando el medidor se acerca al límite de '
                              'compuestos polares. Varios artículos de la norma de aceites '
                              'calentados están derogados; el que sigue vivo prohíbe añadir al '
                              'aceite sustancias extrañas y vender el usado para uso '
                              'alimentario.', alto=96)
    ws.merge_cells('G%d:G%d' % (C_REPO, C_REPO_ABS))
    nota_legal(ws, 'G%d' % C_REPO, 'CUN-03')

    # --- compras -------------------------------------------------------------------
    seccion(ws, 'A%d' % C_SEC_COM, 'Lo que Compras de Aceite')
    encabezados(ws, C_COM_CAB, [('A', 'Concepto', None), ('B', 'Día tipo', None),
                                ('C', 'Día punta', None), ('D', 'Media de la semana', None),
                                ('E', 'Al mes', None)], alto=30, congelar=False)
    motor.val(ws, 'A%d' % C_COM_L, 'Litros que compras (renovación + reposición)')
    motor.val(ws, 'A%d' % C_COM_E, 'Euros de aceite que compras (base imponible)', bold=True)
    for col in 'BC':
        formula(ws, '%s%d' % (col, C_COM_L), '=IFERROR($B$%d+%s%d,"")' % (C_LDIA, col, C_REPO), fmt=DEC)
        formula(ws, '%s%d' % (col, C_COM_E), '=IFERROR(%s%d*%s,"")' % (col, C_COM_L, precio), fmt=EUR)
    formula(ws, 'D%d' % C_COM_L, media(C_COM_L), fmt=DEC)
    formula(ws, 'D%d' % C_COM_E, media(C_COM_E), fmt=EUR)
    formula(ws, 'E%d' % C_COM_L, '=IFERROR(D%d*$B$%d,"")' % (C_COM_L, C_DMES), fmt=DEC1, bold=True,
            destacar=True)
    formula(ws, 'E%d' % C_COM_E, '=IFERROR(D%d*$B$%d,"")' % (C_COM_E, C_DMES), fmt=EUR, bold=True,
            destacar=True)

    # --- contraste -----------------------------------------------------------------
    seccion(ws, 'A%d' % C_SEC_CON, 'Fila de Contraste: Aceite Absorbido (3) + Renovación (4) = '
                                   'Aceite Total por Ración')
    filas = (
        (C_ABS3, 'Aceite absorbido por ración (libro 3, copiado en Parámetros)',
         '=%s' % XB('aceite_absorbido_por_racion'), EUR4),
        (C_REN4, 'Renovación por ración (este libro)', '=B%d' % C_RENRAC, EUR4),
        (C_TOTAL, 'ACEITE TOTAL POR RACIÓN', '=IFERROR(B%d+B%d,"")' % (C_ABS3, C_REN4), EUR4),
        (C_PARTE, 'Parte del aceite total que es renovación', '=IFERROR(B%d/B%d,"")' % (C_REN4, C_TOTAL), PCT),
        (C_REPRAC, 'Reposición que mides, por ración (media de la semana)', '=D%d' % C_REPO_RAC, EUR4),
        (C_DIF, 'Reposición por ración menos aceite absorbido por ración',
         '=IFERROR(B%d-B%d,"")' % (C_REPRAC, C_ABS3), EUR4),
    )
    for fila, etq, form, fmt in filas:
        motor.val(ws, 'A%d' % fila, etq, bold=fila == C_TOTAL, wrap=True)
        formula(ws, 'B%d' % fila, form, fmt=fmt, bold=fila == C_TOTAL, destacar=fila == C_TOTAL)
        motor.val(ws, 'C%d' % fila, '' if fmt == PCT else 'EUR/ración')
    gris(ws, 'D%d' % C_TOTAL, 'El libro 6 suma las dos partes, cada una con su fuente: la '
                              'absorbida dentro del coste de materia del libro 3 y la '
                              'renovación con la celda de la derecha. Así no se cuenta dos '
                              'veces.', alto=48)
    ws.merge_cells('D%d:G%d' % (C_TOTAL, C_TOTAL))
    gris(ws, 'D%d' % C_DIF, 'Cerca de cero si tu absorción del libro 3 es realista: lo que '
                            'repones es, sobre todo, lo que se lleva la masa.', alto=36)
    ws.merge_cells('D%d:G%d' % (C_DIF, C_DIF))
    # R-15: la masa por ración (X2 bis) sirve para dar el aceite POR KILO DE MASA
    filas_kg = (
        (C_KGM, 'Kilos de masa por ración media (libro 3, copiado en Parámetros)',
         '=%s' % XB('kg_masa_por_racion_media'), DEC4, 'kg/ración'),
        (C_ABSKG, 'Aceite absorbido por kilo de masa', '=IFERROR(B%d/B%d,"")' % (C_ABS3, C_KGM),
         EUR4, 'EUR/kg de masa'),
        (C_RENKG, 'Renovación por kilo de masa', '=IFERROR(B%d/B%d,"")' % (C_REN4, C_KGM),
         EUR4, 'EUR/kg de masa'),
        (C_TOTKG, 'ACEITE TOTAL POR KILO DE MASA', '=IFERROR(B%d+B%d,"")' % (C_ABSKG, C_RENKG),
         EUR4, 'EUR/kg de masa'),
    )
    for fila, etq, form, fmt, uni in filas_kg:
        motor.val(ws, 'A%d' % fila, etq, bold=fila == C_TOTKG, wrap=True)
        formula(ws, 'B%d' % fila, form, fmt=fmt, bold=fila == C_TOTKG, destacar=fila == C_TOTKG)
        motor.val(ws, 'C%d' % fila, uni)
    gris(ws, 'D%d' % C_TOTKG, 'Lo que te cuesta el aceite por cada kilo de masa que fríes: lo '
                              'que se lleva la pieza y lo que tiras al cambiar la cuba. Sirve '
                              'para comparar con el precio por kilo de tu preparado o de tu mix.',
         alto=48)
    ws.merge_cells('D%d:G%d' % (C_TOTKG, C_TOTKG))

    texto(ws, 'A%d' % C_LEG, 'La norma de calidad de los aceites y grasas calentados alcanza a '
                             'la churrería, sea permanente o de temporada: la nota de esta '
                             'celda dice dónde.', alto=36, merge_hasta='E', italica=True)
    nota_legal(ws, 'A%d' % C_LEG, 'CUN-01')

    bloque_contrato(ws, [(5, 'Renovación de aceite por ración (EUR)', '=B%d' % C_RENRAC, EUR4)])
    version_al_pie(ws, C_LEG + 2)
    setup(ws, apaisado=True)
    return ws


# ==========================================================================
# Hoja «Punto Económico de Cambio»
# ==========================================================================
def hoja_punto(wb):
    ws = wb.create_sheet(H_PEC)
    cabecera_hoja(ws, H_PEC, 'Cuánto cuesta cada ciclo de cambio de la cuba. El dinero te dice '
                             'cuánto ahorras alargando; el medidor te dice hasta dónde puedes.')
    for letra, ancho in (('A', 16), ('B', 15), ('C', 15), ('D', 16), ('E', 18), ('F', 16),
                         ('G', 16), ('H', 18), ('I', 14)):
        ws.column_dimensions[letra].width = ancho
    seccion(ws, 'A4', 'Cuánto Te Cuesta Cada Ciclo de Cambio')
    encabezados(ws, PE_CAB, [
        ('A', 'Días entre cambios (cámbialos)', None),
        ('B', 'Litros renovados por día', None),
        ('C', 'Renovación en euros por día', None),
        ('D', 'Renovación por ración (EUR)', None),
        ('E', 'Aceite total por ración: absorbido + renovación (EUR)', None),
        ('F', 'Renovación al mes (EUR)', None),
        ('G', 'Litros al gestor al mes', None),
        ('H', 'Diferencia al mes frente a tu ciclo (EUR)', None),
        ('I', '¿Es tu ciclo?', None)], alto=58)
    cuba = ABS_(H_CON, 'B%d' % C_CUBA)
    prec = ABS_(H_CON, 'B%d' % C_PRECIO)
    racmed = ABS_(H_CON, 'B%d' % C_RACMED)
    dmes = ABS_(H_CON, 'B%d' % C_DMES)
    absorb = XB('aceite_absorbido_por_racion')
    ciclo = PB(P_DIAS)
    for i, d in enumerate(PE_DIAS):
        fila = PE_INI + i
        cel = entrada(ws, 'A%d' % fila, d, fmt=ENT, etiqueta='Días del ciclo %d' % (i + 1))
        motor.dv_numerica(ws, [cel.coordinate], minimo=1)
        formula(ws, 'B%d' % fila, '=IFERROR(%s/A%d,"")' % (cuba, fila), fmt=DEC)
        formula(ws, 'C%d' % fila, '=IFERROR(B%d*%s,"")' % (fila, prec), fmt=EUR)
        formula(ws, 'D%d' % fila, '=IFERROR(C%d/%s,"")' % (fila, racmed), fmt=EUR4)
        formula(ws, 'E%d' % fila, '=IFERROR(D%d+%s,"")' % (fila, absorb), fmt=EUR4)
        formula(ws, 'F%d' % fila, '=IFERROR(C%d*%s,"")' % (fila, dmes), fmt=EUR)
        formula(ws, 'G%d' % fila, '=IFERROR(B%d*%s,"")' % (fila, dmes), fmt=DEC1)
        formula(ws, 'H%d' % fila, '=IFERROR(F%d-%s,"")' % (fila, ABS_(H_CON, 'B%d' % C_EMES)), fmt=EUR)
        formula(ws, 'I%d' % fila, '=IF(A%d=%s,"Tu ciclo","")' % (fila, ciclo))
    motor.semaforo_isnumber(ws, 'H%d:H%d' % (PE_INI, PE_FIN), '$H%d' % PE_INI, '>', '0')
    motor.semaforo_texto(ws, 'I%d:I%d' % (PE_INI, PE_FIN),
                         (('Tu ciclo', motor.CF_VERDE_BG, motor.CF_VERDE_FG),))

    seccion(ws, 'A%d' % PE_SEC, 'Tu Ciclo y el Punto Económico')
    ws.column_dimensions['A'].width = 16
    rows = (
        (PE_CICLO, 'Tu ciclo actual (días entre cambios)', '=%s' % ciclo, ENT, 'días'),
        (PE_RENMES, 'Renovación al mes con tu ciclo', '=%s' % ABS_(H_CON, 'B%d' % C_EMES), EUR, 'EUR/mes'),
        (PE_ANTES, 'Lo que te cuesta cambiar un día antes',
         '=IFERROR(%s*%s*%s*(1/(F{c}-1)-1/F{c}),"")'.replace('{c}', str(PE_CICLO))
         % (cuba, prec, dmes), EUR, 'EUR/mes más'),
        (PE_DESPUES, 'Lo que ahorras alargando un día (si el medidor te deja)',
         '=IFERROR(%s*%s*%s*(1/F{c}-1/(F{c}+1)),"")'.replace('{c}', str(PE_CICLO))
         % (cuba, prec, dmes), EUR, 'EUR/mes menos'),
        (PE_EQUI, 'Días a partir de los cuales lo que tiras al cambiar cuesta menos por ración '
                  'que lo que se lleva la masa',
         '=IFERROR(%s*%s/(%s*%s),"")' % (cuba, prec, racmed, absorb), DEC1, 'días'),
    )
    for fila, etq, form, fmt, uni in rows:
        ws.merge_cells('A%d:E%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, etq, wrap=True)
        formula(ws, 'F%d' % fila, form, fmt=fmt, bold=True, destacar=fila in (PE_ANTES, PE_DESPUES, PE_EQUI))
        motor.val(ws, 'G%d' % fila, uni)
        ws.row_dimensions[fila].height = 30
    caro = ('Con tu ciclo, el aceite que tiras al cambiar cuesta más por ración que el que se '
            'lleva la masa: cada día que alargues, sin pasar del límite del medidor, se nota')
    barato = ('Con tu ciclo, lo que tiras al cambiar ya cuesta menos por ración que lo que se '
              'lleva la masa: alargar más ahorra poco')
    ws.merge_cells('A%d:E%d' % (PE_VERED, PE_VERED))
    motor.val(ws, 'A%d' % PE_VERED, 'Veredicto', bold=True)
    ws.merge_cells('F%d:I%d' % (PE_VERED, PE_VERED))
    cel = formula(ws, 'F%d' % PE_VERED,
                  '=IF(AND(ISNUMBER(F{c}),ISNUMBER(F{e})),IF(F{c}<F{e},"{caro}","{barato}"),"")'
                  .format(c=PE_CICLO, e=PE_EQUI, caro=caro, barato=barato), bold=True)
    cel.alignment = Alignment(wrap_text=True, vertical='top')
    ws.row_dimensions[PE_VERED].height = 48
    motor.semaforo_texto(ws, 'F%d' % PE_VERED, ((caro, motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                                                (barato, motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    ws.merge_cells('A%d:E%d' % (PE_LIMITE, PE_LIMITE))
    motor.val(ws, 'A%d' % PE_LIMITE, 'El límite que no se negocia: compuestos polares por debajo de',
              wrap=True)
    formula(ws, 'F%d' % PE_LIMITE, '=%s' % PB(P_POLARES), fmt=PCT, bold=True)
    ws.row_dimensions[PE_LIMITE].height = 30
    fila = PE_LIMITE + 2
    texto(ws, 'A%d' % fila, 'El día del cambio lo decide la lectura del medidor de mano, no '
                            'esta tabla: anótala en tu registro del Pack APPCC (hoja «Control '
                            'Aceite») y cambia antes de llegar al límite. El medidor es una '
                            'ayuda para decidir; el 25 % legal se prueba en laboratorio, con el '
                            'método del anexo 1 de la norma. Esta tabla sólo te dice cuánto '
                            'dinero hay en juego en cada día que ganes o pierdas.',
          alto=60, merge_hasta='I', italica=True)
    nota_fuente(ws, 'A%d' % fila, 'CUS-38', extra='Medidor de compuestos polares de mano (el '
                                                  'del ejemplo está en el libro 2).')
    version_al_pie(ws, fila + 2)
    setup(ws, apaisado=True)
    return ws


# ==========================================================================
# Hoja «Escenarios de Precio del Aceite»
# ==========================================================================
def hoja_escenarios(wb):
    ws = wb.create_sheet(H_ESC)
    cabecera_hoja(ws, H_ESC, 'Tres subidas sobre el precio de hoy. Sólo se teclea el porcentaje: '
                             'lo demás sale solo.')
    for letra, ancho in (('A', 22), ('B', 14), ('C', 14), ('D', 16), ('E', 16), ('F', 16),
                         ('G', 17), ('H', 17), ('I', 17), ('J', 17)):
        ws.column_dimensions[letra].width = ancho
    seccion(ws, 'A4', 'Lo que Te Hace una Subida del Aceite')
    encabezados(ws, E_CAB, [
        ('A', 'Escenario', None), ('B', 'Subida sobre el precio de hoy', None),
        ('C', 'Precio del aceite (EUR/L)', None),
        ('D', 'Aceite absorbido por ración (EUR)', None),
        ('E', 'Renovación por ración (EUR)', None),
        ('F', 'Aceite total por ración (EUR)', None),
        ('G', 'Aceite que compras al mes (EUR)', None),
        ('H', 'Margen que pierdes por ración (EUR)', None),
        ('I', 'Margen que pierdes al mes (EUR)', None),
        ('J', 'Margen que pierdes al año (EUR)', None)], alto=58)
    ldia = ABS_(H_CON, 'B%d' % C_LDIA)
    racmed = ABS_(H_CON, 'B%d' % C_RACMED)
    lmes = ABS_(H_CON, 'E%d' % C_COM_L)
    motor.val(ws, 'A%d' % E_HOY, 'Hoy', bold=True)
    motor.val(ws, 'B%d' % E_HOY, 'precio de hoy')
    formula(ws, 'C%d' % E_HOY, '=%s' % XB('precio_aceite_eur_l'), fmt=EUR4)
    for i, s in enumerate(SUBIDAS):
        fila = E_INI + i
        motor.val(ws, 'A%d' % fila, 'Subida %d' % (i + 1), bold=True)
        cel = entrada(ws, 'B%d' % fila, s, fmt=PCT, etiqueta='Subida del escenario %d' % (i + 1))
        motor.dv_porcentaje(ws, [cel.coordinate], maximo=5)
        formula(ws, 'C%d' % fila, '=IFERROR($C$%d*(1+B%d),"")' % (E_HOY, fila), fmt=EUR4)
    nota_fuente(ws, 'B%d' % E_INI, '', extra='Subidas: supuesto declarado de El Molinete. Pon las '
                                             'que temas.')
    for fila in range(E_HOY, E_FIN + 1):
        formula(ws, 'D%d' % fila, '=IFERROR(%s*C%d/$C$%d,"")' % (XB('aceite_absorbido_por_racion'),
                                                                 fila, E_HOY), fmt=EUR4)
        formula(ws, 'E%d' % fila, '=IFERROR(%s*C%d/%s,"")' % (ldia, fila, racmed), fmt=EUR4)
        formula(ws, 'F%d' % fila, '=IFERROR(D%d+E%d,"")' % (fila, fila), fmt=EUR4, bold=True)
        formula(ws, 'G%d' % fila, '=IFERROR(%s*C%d,"")' % (lmes, fila), fmt=EUR)
        formula(ws, 'H%d' % fila, '=IFERROR(F%d-$F$%d,"")' % (fila, E_HOY), fmt=EUR4)
        formula(ws, 'I%d' % fila, '=IFERROR(G%d-$G$%d,"")' % (fila, E_HOY), fmt=EUR, bold=True)
        formula(ws, 'J%d' % fila, '=IFERROR(I%d*12,"")' % fila, fmt=EUR, destacar=fila > E_HOY)
    motor.semaforo_isnumber(ws, 'I%d:I%d' % (E_INI, E_FIN), '$I%d' % E_INI, '>', '0')
    fila = E_FIN + 2
    seccion(ws, 'A%d' % fila, 'Cómo Leerlo')
    texto(ws, 'A%d' % (fila + 1), 'Lo que sube por ración es lo que baja tu margen por ración si no '
                                  'tocas el PVP: para no perderlo, el PVP sin IVA tendría que subir '
                                  'esa misma cantidad. Sólo se mueve el aceite (el que se lleva la '
                                  'masa y el que tiras al cambiar); el resto del escandallo se queda '
                                  'donde estaba.', alto=48, merge_hasta='J')
    texto(ws, 'A%d' % (fila + 2), 'El margen que pierdes al mes sale del aceite que COMPRAS (la '
                                  'renovación más tu reposición medida), no de las raciones: es lo '
                                  'que de verdad sale de la caja. Si cambias el precio de la garrafa, '
                                  'hazlo en el libro 3 (allí se recalcula todo el coste de materia) y '
                                  'cópialo aquí.', alto=48, merge_hasta='J')
    version_al_pie(ws, fila + 4)
    setup(ws, apaisado=True)
    return ws


# ==========================================================================
# Hoja «Gestor de Aceite Usado»
# ==========================================================================
def hoja_gestor(wb):
    ws = wb.create_sheet(H_GES)
    cabecera_hoja(ws, H_GES, 'El aceite que tiras al cambiar la cuba sale por la puerta de atrás '
                             'hacia un gestor autorizado. Aquí, cuánto, cuánto cuesta y qué papeles '
                             'guardas.')
    for letra, ancho in (('A', 62), ('B', 16), ('C', 14), ('D', 60)):
        ws.column_dimensions[letra].width = ancho
    seccion(ws, 'A4', 'Lo que Se Lleva el Gestor')
    filas = (
        (G_LDIA, 'Litros renovados por día', '=%s' % ABS_(H_CON, 'B%d' % C_LDIA), DEC, 'L/día'),
        (G_DMES, 'Días naturales por mes (media)', '=%s' % PB(P_MES), DEC, 'días'),
        (G_LMES, 'LITROS AL GESTOR AL MES', '=IFERROR(B%d*B%d,"")' % (G_LDIA, G_DMES), DEC1, 'L/mes'),
        (G_LANIO, 'Litros al gestor al año', '=IFERROR(B%d*%s,"")' % (G_LDIA, PB(P_ANIO)), ENT, 'L/año'),
        (G_CMES, 'Lo que te cobra el gestor al mes (base imponible)', '=%s' % PB(P_GESTOR), EUR, 'EUR/mes'),
        (G_CANIO, 'Lo que te cobra el gestor al año', '=IFERROR(B%d*12,"")' % G_CMES, EUR, 'EUR/año'),
        (G_CRAC, 'Coste del gestor por ración', '=IFERROR(B%d/(%s*B%d),"")'
         % (G_CMES, ABS_(H_CON, 'B%d' % C_RACMED), G_DMES), EUR4, 'EUR/ración'),
    )
    for fila, etq, form, fmt, uni in filas:
        motor.val(ws, 'A%d' % fila, etq, bold=fila == G_LMES)
        formula(ws, 'B%d' % fila, form, fmt=fmt, bold=fila == G_LMES, destacar=fila == G_LMES)
        motor.val(ws, 'C%d' % fila, uni)
    gris(ws, 'D%d' % G_LMES, 'Sólo el aceite de los cambios de cuba: la reposición se la lleva la '
                             'masa.', alto=30)
    gris(ws, 'D%d' % G_CRAC, 'Con un gestor que recoge sin cobrar, cero. Lo que no puede faltar '
                             'es el justificante de cada retirada.', alto=30)

    seccion(ws, 'A%d' % G_SEC_REG, 'Contraste con tu Registro de Retiradas')
    ok_txt = 'Cuadra con tu registro de retiradas'
    menos_txt = 'El gestor se lleva menos aceite del que renuevas: averigua a dónde va el resto'
    mas_txt = ('El gestor se lleva más aceite del que calcula este libro: revisa los días entre '
               'cambios y los litros de cuba')
    filas = (
        (G_RET, 'Litros que retiró tu gestor el último mes (Parámetros)', '=%s' % PB(P_RETIRADOS), DEC1),
        (G_DEV, 'Diferencia frente a los litros que calcula este libro',
         '=IFERROR(B%d/B%d-1,"")' % (G_RET, G_LMES), PCT),
    )
    for fila, etq, form, fmt in filas:
        motor.val(ws, 'A%d' % fila, etq, wrap=True)
        formula(ws, 'B%d' % fila, form, fmt=fmt)
    motor.val(ws, 'A%d' % G_VERED, 'Contraste', bold=True)
    ws.merge_cells('B%d:D%d' % (G_VERED, G_VERED))
    cel = formula(ws, 'B%d' % G_VERED,
                  '=IF(ISNUMBER(B{d}),IF(B{d}<-{t},"{menos}",IF(B{d}>{t},"{mas}","{ok}")),"")'
                  .format(d=G_DEV, t=PB(P_TOL), menos=menos_txt, mas=mas_txt, ok=ok_txt), bold=True)
    cel.alignment = Alignment(wrap_text=True, vertical='top')
    ws.row_dimensions[G_VERED].height = 34
    motor.semaforo_texto(ws, 'B%d' % G_VERED, ((ok_txt, motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                                               (menos_txt, motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                                               (mas_txt, motor.CF_AMBAR_BG, motor.CF_AMBAR_FG)))

    seccion(ws, 'A%d' % G_SEC_LEG, 'Obligaciones y Papeles que Guardas')
    fila = G_SEC_LEG + 1
    c = texto(ws, 'A%d' % fila, 'El aceite de cocina usado de la hostelería tiene recogida separada '
                                'obligatoria desde el 30 de junio de 2022: contrato con un gestor '
                                'autorizado y archivo de los justificantes de cada retirada.',
              alto=40, merge_hasta='D')
    nota_legal(ws, c.coordinate, 'CUN-27')
    fila += 1
    c = texto(ws, 'A%d' % fila, 'Cada retirada se anota en el registro del Pack APPCC, fichero '
                                '09-control-aceite-fritura.xlsx, hoja «Retirada de aceite usado» '
                                '(fecha, litros, gestor, número de documento y firma). Este libro '
                                'no lo duplica: sólo contrasta los litros del mes.',
              alto=40, merge_hasta='D')
    nota_fuente(ws, c.coordinate, '', extra='Registro del lector: %s' % D.F_PACK_APPCC_09_RETIRADA)
    fila += 1
    texto(ws, 'A%d' % fila, 'La prohibición de verter el aceite por el desagüe la fijan las '
                            'ordenanzas municipales: mira la de tu ayuntamiento.',
          alto=30, merge_hasta='D')
    fila += 1
    nombre, ofrece, url, fuente, nota_p = [p for p in D.PROVEEDORES if p[3] == 'CUS-44h'][0]
    c = texto(ws, 'A%d' % fila, 'Ejemplo de gestor para Madrid, sin relación comercial: %s. %s. %s '
                                'El de El Molinete recoge sin coste a cambio de obsequios, servicios '
                                'gratuitos o valoración económica; pide el tuyo en tu ciudad.'
              % (nombre, ofrece, nota_p), alto=58, merge_hasta='D')
    nota_fuente(ws, c.coordinate, fuente)
    version_al_pie(ws, fila + 2)
    setup(ws, apaisado=False)
    return ws


# ==========================================================================
# Mapa de celdas
# ==========================================================================
def mapa_celdas():
    m = []
    for c in CRUCES_IN:
        clave = c['calcula']
        m.append(('%s (copiado del libro %d, %s)' % (ETIQUETA_CRUCE[clave][0], c['origen'], c['x']),
                  H_PAR, 'B%d' % CRUCE_ROW[clave], 'entrada'))
    m += [
        ('Renovación de aceite por ración (origen de X12)', H_CON, 'L5', 'salida'),
        ('Días entre cambios de aceite', H_PAR, 'B%d' % P_DIAS, 'entrada'),
        ('Aceite que repones en un día tipo', H_PAR, 'B%d' % P_REPO_T, 'entrada'),
        ('Aceite que repones en un día punta', H_PAR, 'B%d' % P_REPO_P, 'entrada'),
        ('Coste del gestor de aceite usado al mes', H_PAR, 'B%d' % P_GESTOR, 'entrada'),
        ('Límite legal de compuestos polares', H_PAR, 'B%d' % P_POLARES, 'parametro'),
        ('Litros que retiró el gestor el último mes', H_PAR, 'B%d' % P_RETIRADOS, 'entrada'),
        ('Tolerancia de los contrastes', H_PAR, 'B%d' % P_TOL, 'parametro'),
        ('Tolerancia de las filas de CUADRE', H_PAR, 'B%d' % P_TOLC, 'parametro'),
        ('Días naturales por mes', H_PAR, 'B%d' % P_MES, 'parametro'),
        ('Cuadre del aceite absorbido (veredicto)', H_PAR,
         'D%d' % CUADRE_ROW['aceite_absorbido_por_racion'], 'salida'),
        ('Contraste A: aceite absorbido recalculado (veredicto)', H_PAR, 'B%d' % P_CON_INI, 'salida'),
        ('Aceite absorbido por ración recalculado con las copias', H_PAR, 'B%d' % P_A_RECALC, 'salida'),
        ('Kilos fritos por kilo de masa que implican las copias', H_PAR, 'B%d' % P_C_RATIO, 'salida'),
        ('Litros renovados por día', H_CON, 'B%d' % C_LDIA, 'salida'),
        ('Renovación en euros por día', H_CON, 'B%d' % C_EDIA, 'salida'),
        ('Raciones de un día medio de la semana', H_CON, 'B%d' % C_RACMED, 'salida'),
        ('Renovación por ración', H_CON, 'B%d' % C_RENRAC, 'salida'),
        ('Renovación en euros al mes', H_CON, 'B%d' % C_EMES, 'salida'),
        ('Reposición que sale de la absorción en un día tipo', H_CON, 'B%d' % C_REPO_ABS, 'salida'),
        ('Contraste de la reposición con la absorción (media de la semana)', H_CON,
         'D%d' % C_VERED, 'salida'),
        ('Reposición por ración (media de la semana)', H_CON, 'D%d' % C_REPO_RAC, 'salida'),
        ('Litros de aceite que compras al mes', H_CON, 'E%d' % C_COM_L, 'salida'),
        ('Euros de aceite que compras al mes', H_CON, 'E%d' % C_COM_E, 'salida'),
        ('Aceite total por ración (absorbido del libro 3 más renovación)', H_CON, 'B%d' % C_TOTAL, 'salida'),
        ('Aceite absorbido por kilo de masa', H_CON, 'B%d' % C_ABSKG, 'salida'),
        ('Renovación de aceite por kilo de masa', H_CON, 'B%d' % C_RENKG, 'salida'),
        ('Aceite total por kilo de masa', H_CON, 'B%d' % C_TOTKG, 'salida'),
        ('Parte del aceite total por ración que es renovación', H_CON, 'B%d' % C_PARTE, 'salida'),
        ('Coste de cambiar un día antes al mes', H_PEC, 'F%d' % PE_ANTES, 'salida'),
        ('Ahorro de alargar un día al mes', H_PEC, 'F%d' % PE_DESPUES, 'salida'),
        ('Días en que la renovación por ración iguala al aceite absorbido', H_PEC, 'F%d' % PE_EQUI, 'salida'),
        ('Veredicto del punto económico de cambio', H_PEC, 'F%d' % PE_VERED, 'salida'),
    ]
    for i, d in enumerate(PE_DIAS):
        if d in (4, 8):
            m.append(('Renovación por ración con un ciclo de %d días' % d, H_PEC, 'D%d' % (PE_INI + i), 'salida'))
    for i, s in enumerate(SUBIDAS):
        fila = E_INI + i
        pct = int(round(s * 100))
        m.append(('Subida del aceite del escenario %d' % (i + 1), H_ESC, 'B%d' % fila, 'entrada'))
        m.append(('Margen que pierdes al mes con el aceite un %d %% más caro' % pct, H_ESC,
                  'I%d' % fila, 'salida'))
        m.append(('Margen que pierdes al año con el aceite un %d %% más caro' % pct, H_ESC,
                  'J%d' % fila, 'salida'))
    m += [
        ('Litros al gestor al mes', H_GES, 'B%d' % G_LMES, 'salida'),
        ('Litros al gestor al año', H_GES, 'B%d' % G_LANIO, 'salida'),
        ('Coste del gestor al año', H_GES, 'B%d' % G_CANIO, 'salida'),
        ('Contraste con el registro de retiradas', H_GES, 'B%d' % G_VERED, 'salida'),
    ]
    return m


# ==========================================================================
# Cierre: guardar, cachear, verificar, cruces, lista negra y mapa
# ==========================================================================
_PROHIBIDAS = ('INDIRECT', 'COUNTA', 'PMT(', 'OFFSET', 'XLOOKUP', 'LET(', 'LAMBDA', 'RANK(',
               'NETWORKDAYS', 'IRR(')
RX_CONST_DEC = re.compile(r'[*/]\s*\d{1,3}[.,]\d{1,4}(?!\d)')
#: Enteros que pueden ir en una fórmula: conversiones de unidad y de calendario (1 de
#: «uno menos», 12 meses al año). Cualquier otro número tecleado aborta.
_ENTEROS_OK = {'1', '12'}
_RX_NUM = re.compile(r'(?<![A-Z$0-9.])(\d+(?:\.\d+)?)(?![0-9]*[(!])')


def _textos(wbf):
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                if isinstance(c.value, str):
                    yield '%s!%s' % (ws.title, c.coordinate), c.value
                if c.comment is not None:
                    yield '%s!%s (nota)' % (ws.title, c.coordinate), c.comment.text


def _gate_lista_negra(wbf):
    fallos = []
    rotulos = set(D.rotulo_cruce(c) for c in CRUCES_IN)
    for donde, txt in _textos(wbf):
        bajo = txt.lower()
        for aguja, motivo in D.LISTA_NEGRA:
            if aguja.startswith('re:'):
                if re.search(aguja[3:], bajo):
                    fallos.append('%s: /%s/ (%s)' % (donde, aguja[3:], motivo))
            elif aguja.lower() in bajo:
                fallos.append('%s: «%s» (%s)' % (donde, aguja, motivo))
        for pid in RX_ID.findall(txt):
            if pid in D.IDS_PROHIBIDOS:
                fallos.append('%s: id prohibido %s' % (donde, pid))
        if 'trae aquí la cifra de' in bajo:
            fallos.append('%s: rótulo de cruce con la fórmula de la hermana' % donde)
        if 'cópialo del libro' in bajo and txt.strip() not in rotulos:
            fallos.append('%s: rótulo de cruce que no está en CRUCES: %s' % (donde, txt[:80]))
        if 'comparativa' in bajo and 'aceite' in bajo:
            fallos.append('%s: comparativa de aceites (C5)' % donde)
    if fallos:
        raise SystemExit('LISTA NEGRA / IDS PROHIBIDOS en %s:\n  %s' % (NOMBRE, '\n  '.join(fallos[:40])))


def _gate_cruces(wbf, wbv):
    """Receptor: cada cruce de `CRUCES` con receptor 4 tiene su celda verde en
    «Parámetros» con el rótulo exacto y el `valor_defecto`, y su fila de CUADRE.
    Origen: cada celda de X12 tiene rótulo en K y el valor de `datos_ejemplo`."""
    if D._ERROR_CRUCES:
        raise SystemExit('datos_ejemplo no pudo calcular los cruces: %s' % D._ERROR_CRUCES)
    fallos, filas = [], []
    if len(CRUCE_VERDES) != len(CRUCES_IN) or len(CRUCE_CUADRES) != len(CRUCES_IN):
        fallos.append('%d cruces, %d verdes de cruce y %d filas de CUADRE'
                      % (len(CRUCES_IN), len(CRUCE_VERDES), len(CRUCE_CUADRES)))
    for c in CRUCES_IN:
        if c['hoja_receptor'] != H_PAR:
            fallos.append('%s: la hoja receptora es %s y no «Parámetros»' % (c['x'], c['hoja_receptor']))
        fila = CRUCE_ROW[c['calcula']]
        cel_v = wbf[H_PAR]['B%d' % fila]
        if not motor.es_verde(cel_v) or cel_v.protection.locked:
            fallos.append('%s: Parámetros!B%d no es verde y editable' % (c['x'], fila))
        if wbf[H_PAR]['D%d' % fila].value != D.rotulo_cruce(c):
            fallos.append('%s: Parámetros!D%d no lleva el rótulo %r' % (c['x'], fila, D.rotulo_cruce(c)))
        v = wbv[H_PAR]['B%d' % fila].value
        esperado = c['valor_defecto']
        if not isinstance(v, (int, float)) or abs(v - esperado) > max(1e-9, abs(esperado) * 1e-9):
            fallos.append('%s: Parámetros!B%d = %r y datos_ejemplo dice %r' % (c['x'], fila, v, esperado))
        fc = CUADRE_ROW[c['calcula']]
        rot = wbf[H_PAR]['A%d' % fc].value
        if not (isinstance(rot, str) and rot.startswith('CUADRE')):
            fallos.append('%s: Parámetros!A%d no es una fila de CUADRE' % (c['x'], fc))
        if wbv[H_PAR]['D%d' % fc].value != 'CUADRA':
            fallos.append('%s: con los datos de El Molinete el CUADRE de la fila %d dice %r'
                          % (c['x'], fc, wbv[H_PAR]['D%d' % fc].value))
        if not motor.es_verde(wbf[H_PAR]['B%d' % fc]):
            fallos.append('%s: la celda «lo que publica hoy el origen» de la fila %d no es verde' % (c['x'], fc))
    for _h, coord in CONTRASTES:
        if wbv[H_PAR][coord].value != 'COHERENTE':
            fallos.append('el contraste %s dice %r con los datos de El Molinete'
                          % (coord, wbv[H_PAR][coord].value))
    for c in CRUCES_OUT:
        hoja, celda = c['hoja_origen'], c['celda_origen']
        rot = wbf[hoja]['K' + celda[1:]].value
        if not isinstance(rot, str) or not rot.strip():
            fallos.append('%s: %s!K%s sin rótulo' % (c['x'], hoja, celda[1:]))
        v = wbv[hoja][celda].value
        esperado = c['valor_defecto']
        if not isinstance(v, (int, float)) or abs(v - esperado) > max(1e-9, abs(esperado) * 1e-9):
            fallos.append('%s: %s!%s = %r y datos_ejemplo dice %r' % (c['x'], hoja, celda, v, esperado))
        filas.append((c['x'], hoja, celda, v, esperado))
    # El libro no puede escribir ninguna celda de origen de otro libro con la frase de
    # recepción fuera de «Parámetros».
    for ws in wbf.worksheets:
        if ws.title == H_PAR:
            continue
        for row in ws.iter_rows():
            for cel in row:
                if isinstance(cel.value, str) and 'cópialo del libro' in cel.value:
                    fallos.append('%s!%s: rótulo de cruce fuera de «Parámetros»' % (ws.title, cel.coordinate))
    if fallos:
        raise SystemExit('CRUCES ROTOS en %s:\n  %s' % (NOMBRE, '\n  '.join(fallos)))
    return filas


def _gate_contra_datos(wbv):
    """Las salidas principales, al céntimo contra `datos_ejemplo`."""
    pares = [
        ('renovación por ración', wbv[H_CON]['B%d' % C_RENRAC].value, D.renovacion_por_racion()),
        ('litros renovados por día', wbv[H_CON]['B%d' % C_LDIA].value, D.renovacion_litros_dia()),
        ('litros al gestor al mes', wbv[H_GES]['B%d' % G_LMES].value, D.litros_al_gestor_mes()),
        ('reposición del día tipo por absorción', wbv[H_CON]['B%d' % C_REPO_ABS].value,
         D.reposicion_litros_dia('tipo')),
        ('reposición del día punta por absorción', wbv[H_CON]['C%d' % C_REPO_ABS].value,
         D.reposicion_litros_dia('punta')),
        ('raciones del día medio', wbv[H_CON]['B%d' % C_RACMED].value, D.raciones_dia_medio_semana()),
        ('aceite total por ración', wbv[H_CON]['B%d' % C_TOTAL].value,
         D.aceite_absorbido_por_racion() + D.renovacion_por_racion()),
        ('consumo del día tipo', wbv[H_CON]['B%d' % C_COM_L].value,
         D.renovacion_litros_dia() + round(D.reposicion_litros_dia('tipo'), 2)),
    ]
    fallos = ['%s: libro %r, datos_ejemplo %r' % (n, v, e) for n, v, e in pares
              if not isinstance(v, (int, float)) or abs(v - e) > max(1e-9, abs(e) * 1e-9)]
    if fallos:
        raise SystemExit('SALIDAS que no cuadran con datos_ejemplo:\n  ' + '\n  '.join(fallos))
    return pares


def cerrar(wb, mapa_celdas_):
    wb.properties.creator = 'AI Chef Pro'
    wb.properties.lastModifiedBy = 'AI Chef Pro'
    wb.properties.title = TITULO
    wb.properties.subject = SUBJECT

    enmiendas_churreria.sanear_libro(wb)       # R-09: sin texto interno de la fábrica
    CC.barrer_cp1252(wb)
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and (motor.NARROW in c.value or motor.NOBRK in c.value):
                    raise SystemExit('%s!%s lleva espacio fino o guion no separable' % (ws.title, c.coordinate))
                if c.comment is not None:
                    try:
                        c.comment.text.encode('cp1252')
                    except UnicodeEncodeError:
                        raise SystemExit('%s!%s: la nota no cabe en WinAnsi' % (ws.title, c.coordinate))
    for ws in wb.worksheets:
        motor.retirar_verde_de_calculadas(ws)
        motor.proteger(ws)

    if wb.sheetnames[0] != H_INS:
        raise SystemExit('La primera hoja no es «Instrucciones»')
    if tuple(wb.sheetnames) != tuple(D.HOJAS[LIBRO]):
        raise SystemExit('Hojas %r frente a las de datos_ejemplo %r' % (wb.sheetnames, D.HOJAS[LIBRO]))

    destino = CC.BUILD_DIR
    if not os.path.isdir(destino):
        os.makedirs(destino)
    ruta = os.path.join(destino, NOMBRE + '.xlsx')
    wb.save(ruta)

    otros = [os.path.splitext(f)[0] for n, f in D.LIBROS.items() if n != LIBRO]
    problemas = []
    for hoja, coord, form in motor.REGISTRO:
        arriba = form.upper()
        for p in _PROHIBIDAS:
            if p in arriba:
                problemas.append('%s!%s usa %s' % (hoja, coord, p))
        bajo = form.lower()
        if '.xlsx' in bajo or '[' in form or any(o in bajo for o in otros):
            problemas.append('%s!%s parece referencia a otro libro: %s' % (hoja, coord, form[:70]))
        sin_texto = re.sub(r'"[^"]*"', '', form)
        sin_refs = re.sub(r"'[^']*'!", '', sin_texto)
        for m in RX_CONST_DEC.finditer(sin_refs):
            problemas.append('%s!%s constante tecleada %s en %s' % (hoja, coord, m.group(0), form[:70]))
        for m in _RX_NUM.finditer(re.sub(r'\$?[A-Z]{1,2}\$?\d+', '', sin_refs)):
            if m.group(1) not in _ENTEROS_OK:
                problemas.append('%s!%s número tecleado %s en %s' % (hoja, coord, m.group(1), form[:70]))
        if '/' in sin_texto and 'IFERROR' not in arriba:
            problemas.append('%s!%s división sin IFERROR: %s' % (hoja, coord, form[:70]))
    if problemas:
        raise SystemExit('FÓRMULAS con problemas en %s:\n  %s' % (NOMBRE, '\n  '.join(problemas[:40])))

    res = subprocess.run([sys.executable, os.path.join(RAIZ, 'inject_cache.py'), ruta],
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    salida_cache = res.stdout.decode('utf-8', 'replace')
    if res.returncode != 0:
        raise SystemExit('inject_cache falló:\n' + salida_cache)

    wbf = openpyxl.load_workbook(ruta)
    wbv = openpyxl.load_workbook(ruta, data_only=True)
    sin_valor, con_error, sin_dato, pendientes = [], [], [], []
    for hoja, coord, form in motor.REGISTRO:
        v = wbv[hoja][coord].value
        if v is None:
            pendientes.append((hoja, coord, form))
        elif isinstance(v, str) and v.startswith('#'):
            con_error.append('%s!%s  %s -> %s' % (hoja, coord, form[:60], v))
    if pendientes:
        from pycel import ExcelCompiler
        xl = ExcelCompiler(ruta)
        for hoja, coord, form in pendientes:
            try:
                r = xl.evaluate("'%s'!%s" % (hoja, coord))
            except Exception as e:                            # noqa: BLE001
                sin_valor.append('%s!%s  %s -> pycel: %s' % (hoja, coord, form[:60], e))
                continue
            if r == '' or (r is None and '""' in form):
                sin_dato.append('%s!%s' % (hoja, coord))
            else:
                sin_valor.append('%s!%s  %s -> %r' % (hoja, coord, form[:60], r))
    if sin_valor or con_error:
        raise SystemExit('VERIFICACIÓN data_only FALLIDA en %s\n  sin valor (%d):\n   %s\n  con error '
                         '(%d):\n   %s' % (NOMBRE, len(sin_valor), '\n   '.join(sin_valor[:40]),
                                           len(con_error), '\n   '.join(con_error[:40])))
    incoherentes = CC.gate_sum_rango(wbv)
    if incoherentes:
        raise SystemExit('TOTALES con caché incoherente:\n  ' + '\n  '.join(incoherentes))

    verdes_vacias, n_verdes = [], 0
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                if motor.es_verde(c):
                    n_verdes += 1
                    if c.protection.locked:
                        verdes_vacias.append('%s!%s bloqueada' % (ws.title, c.coordinate))
                    if c.value is None or (isinstance(c.value, str) and not c.value.strip()):
                        verdes_vacias.append('%s!%s' % (ws.title, c.coordinate))
                    if c.data_type == 'f':
                        verdes_vacias.append('%s!%s verde con fórmula' % (ws.title, c.coordinate))
    if verdes_vacias:
        raise SystemExit('CELDAS VERDES VACÍAS, BLOQUEADAS O CON FÓRMULA:\n  ' + ', '.join(verdes_vacias))

    # DV en cada verde numérica, con mensaje de error.
    sin_dv = []
    for ws in wbf.worksheets:
        cubiertas = set()
        for dv in ws.data_validations.dataValidation:
            if not dv.showErrorMessage:
                sin_dv.append('%s: DV sin showErrorMessage (%s)' % (ws.title, dv.sqref))
            for rng in str(dv.sqref).split():
                for fila in ws[rng] if ':' in rng else [[ws[rng]]]:
                    for cel in fila:
                        cubiertas.add(cel.coordinate)
        for row in ws.iter_rows():
            for c in row:
                if (c.__class__.__name__ != 'MergedCell' and motor.es_verde(c)
                        and isinstance(c.value, (int, float)) and c.coordinate not in cubiertas):
                    sin_dv.append('%s!%s verde numérica sin validación' % (ws.title, c.coordinate))
    if sin_dv:
        raise SystemExit('VALIDACIÓN DE DATOS:\n  ' + '\n  '.join(sin_dv))

    _gate_lista_negra(wbf)
    contrato = _gate_cruces(wbf, wbv)
    contra_datos = _gate_contra_datos(wbv)

    requeridos = [i for i, (_t, libros) in D.IDS_LEGALES_REQUERIDOS.items() if LIBRO in libros]
    puestos = set(pid for _h, _c, pid in NOTAS_LEGALES)
    faltan = [i for i in requeridos if i not in puestos]
    if faltan:
        raise SystemExit('Faltan notas legales del libro 4: %s' % ', '.join(faltan))

    mapa = {}
    for etiqueta, hoja, coord, tipo in mapa_celdas_:
        if tipo not in ('entrada', 'salida', 'parametro'):
            raise SystemExit('Tipo de mapa no válido: %r' % tipo)
        v = wbv[hoja][coord].value
        if v is None:
            raise SystemExit('El mapa cita %s!%s («%s») y está VACÍA' % (hoja, coord, etiqueta))
        if etiqueta in mapa:
            raise SystemExit('Etiqueta de mapa repetida: %r' % etiqueta)
        mapa[etiqueta] = {'ref': '%s!%s!%s' % (FICHERO, hoja, coord), 'valor': v, 'tipo': tipo}
    if len(mapa) < 25:
        raise SystemExit('El mapa tiene %d etiquetas y el mínimo es 25' % len(mapa))
    for x, hoja, celda, _v, _e in contrato:
        if not any(d['ref'] == '%s!%s!%s' % (FICHERO, hoja, celda) for d in mapa.values()):
            raise SystemExit('El mapa no cita la celda de origen %s!%s (%s)' % (hoja, celda, x))
    with open(os.path.join(destino, 'mapa-' + NOMBRE + '.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(mapa, ensure_ascii=False, indent=1))

    return {'ruta': ruta, 'hojas': len(wbf.worksheets), 'formulas': len(motor.REGISTRO),
            'sin_dato': len(sin_dato), 'verdes': n_verdes, 'verdes_vacias': verdes_vacias,
            'notas_legales': len(NOTAS_LEGALES), 'mapa': len(mapa), 'contrato': contrato,
            'contra_datos': contra_datos, 'cruces_in': len(CRUCE_VERDES),
            'cuadres': len(CRUCE_CUADRES),
            'cache': (salida_cache.strip().splitlines() or [''])[-1]}


# ==========================================================================
# Demostraciones con pycel
# ==========================================================================
def demo(ruta):
    from pycel import ExcelCompiler
    ok, fallos = [], []

    def prueba(nombre, cond, detalle=''):
        (ok if cond else fallos).append(nombre + (' - ' + detalle if detalle else ''))

    def nuevo():
        return ExcelCompiler(ruta)

    def ev(xl, hoja, coord):
        return xl.evaluate("'%s'!%s" % (hoja, coord))

    def pon(xl, hoja, coord, v):
        xl.set_value("'%s'!%s" % (hoja, coord), v)

    # 1. La renovación por ración (X12) es la de datos_ejemplo, y alargar el ciclo de 6 a 8
    #    días la baja en la proporción 6/8, igual que los litros al gestor.
    xl = nuevo()
    r0 = ev(xl, H_CON, 'L5')
    g0 = ev(xl, H_GES, 'B%d' % G_LMES)
    pon(xl, H_PAR, 'B%d' % P_DIAS, 8)
    r1 = ev(xl, H_CON, 'L5')
    g1 = ev(xl, H_GES, 'B%d' % G_LMES)
    prueba('X12 = datos_ejemplo, y cambiar cada 8 días en vez de 6 baja la renovación por '
           'ración y los litros al gestor a 6/8',
           abs(r0 - D.renovacion_por_racion()) < 1e-12 and abs(r1 / r0 - 6.0 / 8.0) < 1e-9
           and abs(g1 / g0 - 6.0 / 8.0) < 1e-9,
           'EUR/ración %.5f -> %.5f · L/mes al gestor %.1f -> %.1f' % (r0, r1, g0, g1))

    # 2. Si el aceite absorbido copiado del libro 3 se queda viejo (un 20 % por encima), su fila de
    #    CUADRE (contra lo que publica el origen) y el contraste A se ponen en rojo; los demás no.
    xl = nuevo()
    fAbs = CUADRE_ROW['aceite_absorbido_por_racion']
    fB = CUADRE_ROW['_raciones_punta']
    cA, cB = P_CON_INI, P_CON_INI + 1
    a0, b0 = ev(xl, H_PAR, 'D%d' % fAbs), ev(xl, H_PAR, 'D%d' % fB)
    ca0, cb0 = ev(xl, H_PAR, 'B%d' % cA), ev(xl, H_PAR, 'B%d' % cB)
    pon(xl, H_PAR, 'B%d' % CRUCE_ROW['aceite_absorbido_por_racion'],
        D.aceite_absorbido_por_racion() * 1.2)
    a1, b1 = ev(xl, H_PAR, 'D%d' % fAbs), ev(xl, H_PAR, 'D%d' % fB)
    ca1, cb1 = ev(xl, H_PAR, 'B%d' % cA), ev(xl, H_PAR, 'B%d' % cB)
    prueba('un aceite absorbido copiado de una versión vieja del libro 3 pone en rojo su CUADRE '
           'y el contraste A, y deja en verde el de la proporción punta/tipo',
           a0 == 'CUADRA' and a1.startswith('REVISA') and b0 == 'CUADRA' and b1 == 'CUADRA'
           and ca0 == 'COHERENTE' and ca1 == KO['A'] and cb0 == 'COHERENTE' and cb1 == 'COHERENTE',
           '%r -> %r · %r -> %r' % (a0, a1[:12], ca0, ca1[:12]))

    # 3. Copiar las raciones del día punta sin actualizar sus kilos fritos rompe el contraste B y
    #    su CUADRE.
    xl = nuevo()
    ev(xl, H_PAR, 'D%d' % fB)
    ev(xl, H_PAR, 'B%d' % cB)
    pon(xl, H_PAR, 'B%d' % CRUCE_ROW['_raciones_punta'], 480)
    b2 = ev(xl, H_PAR, 'B%d' % cB)
    q2 = ev(xl, H_PAR, 'D%d' % fB)
    prueba('raciones del día punta copiadas sin sus kilos fritos: contraste B INCOHERENTE y su '
           'CUADRE en REVISA', b2 == KO['B'] and q2.startswith('REVISA'), repr(b2[:30]))

    # 3 bis. R-01: una copia mal hecha que las identidades no cazan (los litros de cuba al doble)
    #        la caza la fila de CUADRE contra el origen; antes decía «CUADRA» y la renovación se
    #        duplicaba en silencio hacia el libro 6 (X12).
    xl = nuevo()
    fCuba = CUADRE_ROW['_litros_cuba']
    d0 = ev(xl, H_PAR, 'D%d' % fCuba)
    r0 = ev(xl, H_CON, 'L5')
    pon(xl, H_PAR, 'B%d' % CRUCE_ROW['_litros_cuba'], D.dato(D.PRODUCCION, 'litros_freidora') * 2)
    d1 = ev(xl, H_PAR, 'D%d' % fCuba)
    r1 = ev(xl, H_CON, 'L5')
    prueba('litros de cuba copiados al doble: la renovación (X12) se duplica Y el CUADRE de la cuba '
           'dice REVISA', d0 == 'CUADRA' and d1.startswith('REVISA') and abs(r1 / r0 - 2.0) < 1e-9,
           'X12 %.5f -> %.5f · %r -> %r' % (r0, r1, d0, d1[:12]))
    xl = nuevo()
    fMasa = CUADRE_ROW['kg_masa_por_racion_media']
    m0 = ev(xl, H_PAR, 'D%d' % fMasa)
    k0 = ev(xl, H_CON, 'B%d' % C_ABSKG)
    pon(xl, H_PAR, 'B%d' % CRUCE_ROW['kg_masa_por_racion_media'], 0.2)
    m1 = ev(xl, H_PAR, 'D%d' % fMasa)
    k1 = ev(xl, H_CON, 'B%d' % C_ABSKG)
    prueba('masa por ración copiada mal (0,2 kg): el CUADRE avisa y el aceite por kilo de masa '
           '(R-15) se mueve', m0 == 'CUADRA' and m1.startswith('REVISA') and k1 < k0,
           '%r -> %r · EUR/kg %.4f -> %.4f' % (m0, m1[:12], k0, k1))

    # 4. Una subida del 30 % del aceite: el margen perdido al mes es el 30 % de lo que compras,
    #    y subir el precio copiado del libro 3 mueve todos los escenarios.
    xl = nuevo()
    fila = E_INI + len(SUBIDAS) - 1
    i0 = ev(xl, H_ESC, 'I%d' % fila)
    compra = ev(xl, H_CON, 'E%d' % C_COM_E)
    pon(xl, H_PAR, 'B%d' % CRUCE_ROW['precio_aceite_eur_l'], D.precio_aceite_eur_l() * 1.5)
    i1 = ev(xl, H_ESC, 'I%d' % fila)
    prueba('subida del %d %%: margen perdido al mes = esa parte de la compra de aceite, y crece '
           'con el precio copiado' % int(round(SUBIDAS[-1] * 100)),
           abs(i0 - compra * SUBIDAS[-1]) < 1e-9 and abs(i1 / i0 - 1.5) < 1e-9,
           'EUR/mes %.2f -> %.2f (compra %.2f)' % (i0, i1, compra))

    # 5. Reponer un 50 % más de lo que dice la absorción: el contraste avisa.
    xl = nuevo()
    v0 = ev(xl, H_CON, 'B%d' % C_VERED)
    pon(xl, H_PAR, 'B%d' % P_REPO_T, round(D.reposicion_litros_dia('tipo'), 2) * 1.5)
    v1 = ev(xl, H_CON, 'B%d' % C_VERED)
    prueba('reponer un 50 % más de lo que dice la absorción del libro 3 dispara el contraste',
           v0.startswith('Tu reposición cuadra') and v1.startswith('Repones más'),
           '%r -> %r' % (v0[:30], v1[:30]))

    # 6. El punto económico: con 6 días la renovación pesa más que lo absorbido; con un
    #    ciclo más largo que el punto de equilibrio, el veredicto cambia.
    xl = nuevo()
    equi = ev(xl, H_PEC, 'F%d' % PE_EQUI)
    w0 = ev(xl, H_PEC, 'F%d' % PE_VERED)
    pon(xl, H_PAR, 'B%d' % P_DIAS, int(equi) + 2)
    w1 = ev(xl, H_PEC, 'F%d' % PE_VERED)
    esperado = (dato_cuba() * D.precio_aceite_eur_l()
                / (D.raciones_dia_medio_semana() * D.aceite_absorbido_por_racion()))
    prueba('punto económico en %.1f días; con 6 días «cuesta más», con %d días «ahorra poco»'
           % (equi, int(equi) + 2),
           abs(equi - esperado) < 1e-9 and w0.startswith('Con tu ciclo, el aceite que tiras')
           and w1.startswith('Con tu ciclo, lo que tiras'), '%.3f' % equi)
    return ok, fallos


def dato_cuba():
    return D.dato(D.PRODUCCION, 'litros_freidora')


# ==========================================================================
def main():
    requeridos = [i for i, (_t, libros) in D.IDS_LEGALES_REQUERIDOS.items() if LIBRO in libros]
    D.gate_legal(requeridos)
    for c in CRUCES_IN + CRUCES_OUT:
        if (c['origen'], c['receptor']) not in D.ARISTAS_SPEC:
            raise SystemExit('%s: arista %s no está en la SPEC' % (c['x'], (c['origen'], c['receptor'])))
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_parametros(wb)
    hoja_consumo(wb)
    hoja_punto(wb)
    hoja_escenarios(wb)
    hoja_gestor(wb)
    orden = list(D.HOJAS[LIBRO])
    wb._sheets.sort(key=lambda ws: orden.index(ws.title))

    res = cerrar(wb, mapa_celdas())
    print('escrito: %s' % res['ruta'])
    print('hojas: %d · fórmulas: %d · celdas verdes: %d · verdes vacías: %d'
          % (res['hojas'], res['formulas'], res['verdes'], len(res['verdes_vacias'])))
    print('fórmulas que devuelven «sin dato» a propósito: %d' % res['sin_dato'])
    print('notas legales: %d · etiquetas en el mapa: %d' % (res['notas_legales'], res['mapa']))
    print('cruces recibidos: %d (con %d filas de CUADRE) · cruces de origen: %d'
          % (res['cruces_in'], res['cuadres'], len(res['contrato'])))
    print('inject_cache: %s' % res['cache'])
    for x, hoja, celda, v, e in res['contrato']:
        print('  origen %-5s %s!%s = %.6f (datos_ejemplo %.6f)' % (x, hoja, celda, v, e))
    for n, v, e in res['contra_datos']:
        print('  contra datos_ejemplo · %s = %.6f' % (n, v))
    ok, fallos = demo(res['ruta'])
    for t in ok:
        print('  demo OK    · %s' % t)
    for t in fallos:
        print('  demo FALLA · %s' % t)
    if fallos:
        raise SystemExit('demos con fallos: %d' % len(fallos))
    return res, len(ok), len(fallos)


if __name__ == '__main__':
    main()
