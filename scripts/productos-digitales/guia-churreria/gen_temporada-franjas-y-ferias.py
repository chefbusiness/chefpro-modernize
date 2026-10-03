#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_temporada-franjas-y-ferias.py - libro 5 de «Cómo Montar una
Churrería-Chocolatería» (producto 51, `guia-churreria-chocolateria`; SPEC
`scripts/productos-digitales/guia-churreria-SPEC.md`, §2.1 fila 5, §2.2, §3.2, §3.5 y §5).

Molde H+N. Se calca de `guia-chocolateria/gen_campanas-y-valle-del-ano.py` la idea de
«Peso sobre el Año» (doce coeficientes supuestos que reparten el año), de «Capacidad vs
Demanda del Pico» (demanda del mes frente a la capacidad que se copia del libro 1) y de
«Refuerzo» y «Valle» (aquí, «El Verano (Tres Salidas)»). Es nuevo: «Franjas del Día»
(fuente ÚNICA de la franja en todo el paquete), «Cola del Domingo», «Punto Muerto por
Evento» y «Calendario de Ferias». El cierre (inject_cache + data_only + contrato de
cruces + lista negra + mapa + demo con pycel) es el de los libros 3 y 4 de este mismo
producto.

Hojas (`datos_ejemplo.HOJAS[5]`): Instrucciones · Parámetros · Peso sobre el Año ·
Franjas del Día · Capacidad contra el Pico · Cola del Domingo · Refuerzo por Pico ·
El Verano (Tres Salidas) · Punto Muerto por Evento · Calendario de Ferias.

CRUCES (D16, `datos_ejemplo.CRUCES`)
------------------------------------
Recibe X4 (del libro 1: raciones del día tipo y del día punta, capacidad en raciones por
hora) y X5 (del libro 3: ticket sin IVA y materia por ración en verano, materia por ración
para llevar y coste hora de mano de obra). Cada una es una celda VERDE de «Parámetros»
con su valor por defecto y el rótulo «cópialo del libro N: <fichero>!<Hoja>!<Celda>»,
más UNA FILA DE CUADRE con semáforo: al lado, otra verde «lo que publica hoy esa celda»
(el patrón del libro 1 y de la hermana) y la fila dice CUADRA o REVISA según la
desviación. Nunca una fórmula entre ficheros.

Es ORIGEN de X7 (horas por franja y horas de refuerzo, al 8), X13 (raciones del año y doce
coeficientes, al 6), X14 (resultado anual de ferias, al 6) y X16 (contribución de julio y
agosto de la salida elegida, al 6). Rótulo en K y valor en L desde la fila 5 de cada hoja
de origen, como fija `CRUCES`.

DECISIONES QUE MATERIALIZA
--------------------------
* D14 / A3 / SR-03: el verano tiene TRES salidas (cerrar, carta de verano, ferias) y se
  comparan por CONTRIBUCIÓN en euros. Lo que pagas igual en las tres no entra: lo resta
  el libro 6. Ninguna celda lleva el rótulo de ese concepto ni el del local alquilado
  (gate propio, además del de `gate_libros.py`). Ninguna reducción del IAE.
* D10: el semáforo «antes de las 8:00, sólo como cafetería o bar en el ejemplo de
  Madrid» vive en «Franjas del Día», con la hora mínima legal en celda verde y la nota
  de CUN-34. El libro 7 cita la norma y remite aquí.
* C2: la demanda base nace en el libro 1; el reparto por mes y por franja, aquí; la
  «Cola del Domingo» también, que es donde están a la vez la franja y la capacidad.
* SR-19: el orden de los eventos se calcula con COUNTIF, nunca con RANK.
* Para no contar dos veces las ferias de julio y agosto (van en la salida «Ferias» del
  verano, cruce X16), el resultado anual de ferias que copia el libro 6 (X14) deja fuera
  las de esos dos meses. Supuesto de construcción declarado en «Calendario de Ferias».

Salida: build/temporada-franjas-y-ferias.xlsx + build/mapa-temporada-franjas-y-ferias.json.
Uso: /usr/local/bin/python3 gen_temporada-franjas-y-ferias.py
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

LIBRO = 5
FICHERO = D.LIBROS[LIBRO]
NOMBRE = os.path.splitext(FICHERO)[0]
TITULO = 'Temporada, Franjas y Ferias'
SUBJECT = CC.PRODUCTO + ' · Versión 1.0 · octubre 2026'

(H_INS, H_PAR, H_ANO, H_FRA, H_CAP, H_COL, H_REF, H_VER, H_PME, H_CAL) = D.HOJAS[LIBRO]
assert NOMBRE == 'temporada-franjas-y-ferias'


def Q(hoja):
    return "'" + hoja + "'!"


def ABS_(hoja, coord):
    """Referencia absoluta a otra hoja del MISMO libro."""
    m = re.match(r'([A-Z]+)(\d+)$', coord)
    return Q(hoja) + '$' + m.group(1) + '$' + m.group(2)


def RNG(hoja, a, b):
    """Rango absoluto a otra hoja del MISMO libro."""
    ma = re.match(r'([A-Z]+)(\d+)$', a)
    mb = re.match(r'([A-Z]+)(\d+)$', b)
    return Q(hoja) + '$%s$%s:$%s$%s' % (ma.group(1), ma.group(2), mb.group(1), mb.group(2))


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
HORA = '0.00'

NOTAS_LEGALES = []
VERDES = []
CRUCE_VERDES = []        # (hoja, coord, x, concepto)
CRUCE_CUADRES = []       # (hoja, coord, x, concepto)


def cabecera_hoja(ws, titulo, nota_txt=None):
    # Los nombres de pestaña de la SPEC ya vienen en Title Case («Capacidad contra el
    # Pico»): el A1 los repite literales para que coincidan con la pestaña.
    a1 = titulo if titulo in D.HOJAS[LIBRO] else CC.titulo_hoja(titulo)
    motor.val(ws, 'A1', a1, bold=True)
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


def encabezados(ws, fila, cols, alto=42, congelar=False):
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
    """Comentario de procedencia de un dato de SECTOR (CUS-*, CHS-*, FC-IVA-*): id,
    fiabilidad y URL de la ficha del JSON común."""
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
        ws.row_dimensions[fila].height = max(ws.row_dimensions[fila].height or 15, 28)
    ws.column_dimensions['K'].width = max(ws.column_dimensions['K'].width or 0, 40)
    ws.column_dimensions['L'].width = max(ws.column_dimensions['L'].width or 0, 14)
    ws.column_dimensions['M'].width = max(ws.column_dimensions['M'].width or 0, 44)


# ==========================================================================
# Datos que el libro necesita (todos de `datos_ejemplo`)
# ==========================================================================
CRUCES_IN = [c for c in D.CRUCES if c['receptor'] == LIBRO]
CRUCES_OUT = [c for c in D.CRUCES if c['origen'] == LIBRO]
assert [c['x'] for c in CRUCES_IN] == ['X4'] * 3 + ['X5'] * 4, [c['x'] for c in CRUCES_IN]
assert sorted(set(c['x'] for c in CRUCES_OUT)) == ['X13', 'X14', 'X16', 'X16 bis', 'X16 ter', 'X7'], \
    sorted(set(c['x'] for c in CRUCES_OUT))
assert all(c['hoja_receptor'] == 'Parámetros' for c in CRUCES_IN)

ETIQUETA_CRUCE = {
    '_raciones_tipo': ('Raciones de un día tipo (lunes a viernes)', 'raciones', ENT),
    '_raciones_punta': ('Raciones de un día punta (sábado, domingo y festivo)', 'raciones', ENT),
    'capacidad_raciones_h': ('Capacidad de la línea, en raciones por hora', 'raciones/h', DEC1),
    '_ticket_verano': ('Ticket sin IVA por ración en julio y agosto (carta de verano)',
                       'EUR/ración', EUR4),
    '_materia_verano': ('Coste de materia por ración en julio y agosto (aceite absorbido '
                        'incluido)', 'EUR/ración', EUR4),
    '_materia_llevar': ('Coste de materia por ración para llevar (aceite absorbido incluido)',
                        'EUR/ración', EUR4),
    'coste_hora_mano_obra': ('Coste hora de mano de obra', 'EUR/h', EUR),
}
NOTA_CRUCE = {
    '_raciones_tipo': 'La demanda base nace en el libro 1; aquí se reparte por mes y por franja.',
    '_raciones_punta': 'Sábados, domingos y festivos. Nace en el libro 1.',
    'capacidad_raciones_h': ('Lo que aguanta el conjunto (el equipo que manda) con tu masa por '
                             'ración. Si compras otra máquina, vuelve a copiarla.'),
    '_ticket_verano': ('Con el mix de julio y agosto del libro 3 (la carta de verano). Es la '
                       'base imponible media de una ración de la carta.'),
    '_materia_verano': 'El coste de materia de esa misma ración media de verano.',
    '_materia_llevar': ('El coste de materia de una ración para llevar: es el que se usa en '
                        'las ferias.'),
    'coste_hora_mano_obra': ('Valora el refuerzo y el personal de las ferias sin una segunda '
                             'fuente del salario: es el mismo que usa el escandallo.'),
}

# --- Parámetros: filas ------------------------------------------------------
P_CAB = 5
P_SEC1 = 6
P_SEC3 = 10
CRUCE_ROW = {}
_f1, _f3 = P_SEC1 + 1, P_SEC3 + 1
for _c in CRUCES_IN:
    if _c['origen'] == 1:
        CRUCE_ROW[_c['calcula']] = _f1
        _f1 += 1
    else:
        CRUCE_ROW[_c['calcula']] = _f3
        _f3 += 1
assert _f1 == P_SEC3 and _f3 == 15, (_f1, _f3)

P_SEC_CAL = 16
P_DANIO, P_DCIERRE, P_FINDE, P_FEST, P_MES1, P_MES2, P_DVER = range(17, 24)
P_SEC_HORA = 25
P_FACTOR, P_MIN, P_HCHOC, P_HCAFE = range(26, 30)
P_SEC_TEMP = 31
P_UALTA, P_UVALLE, P_IVAF, P_TOL, P_UREF = range(32, 37)
P_SEC_CUA = 38
P_CUA_CAB = 38
P_CUA_INI = 39
CUADRE_ROW = dict((c['calcula'], P_CUA_INI + i) for i, c in enumerate(CRUCES_IN))
P_CUA_FIN = P_CUA_INI + len(CRUCES_IN) - 1


def PB(fila):
    return ABS_(H_PAR, 'B%d' % fila)


def XB(clave):
    """Celda verde del cruce `clave` (nombre de la función de `datos_ejemplo`)."""
    return PB(CRUCE_ROW[clave])


#: Calendario del año: supuestos declarados (los del juego de datos).
SABADOS_Y_DOMINGOS = 104          # 52 semanas x 2: el mismo reparto que raciones_anio()
DIAS_ANIO = 365
DIAS_JULIO_AGOSTO = 31 + 31
MINUTOS_HORA = 60
assert (DIAS_ANIO - D.dato(D.NEGOCIO, 'dias_cierre_anio')) == D.dias_apertura_anio()
_punta = SABADOS_Y_DOMINGOS + D.dato(D.NEGOCIO, 'festivos_entre_semana')
assert ((D.dias_apertura_anio() - _punta) * D.dato(D.PRODUCCION, 'raciones_dia_tipo')
        + _punta * D.dato(D.PRODUCCION, 'raciones_dia_punta')) == D.raciones_anio()
UMBRAL_ALTA = 1.10                # supuesto: los seis meses de pico de MESES_PICO
UMBRAL_VALLE = 0.60               # supuesto: julio y agosto
assert all(D.COEFICIENTES_MES[m - 1] >= UMBRAL_ALTA - 1e-9 for m in D.MESES_PICO)
assert all(D.COEFICIENTES_MES[m - 1] <= UMBRAL_VALLE for m in D.MESES_VERANO)
assert not any(D.COEFICIENTES_MES[m - 1] >= UMBRAL_ALTA - 1e-9 for m in range(1, 13)
               if m not in D.MESES_PICO)
TOLERANCIA = 0.02                 # la del libro 1: «heredado: guia-chocolateria»
UMBRAL_REFUERZO = 0.25            # supuesto: lo que cubren masa preparada y una persona más (R-03)

# --- Peso sobre el Año --------------------------------------------------------
W_DANIO, W_DCIERRE, W_DPUNTA, W_DTIPO, W_DAPER, W_RTIPO, W_RPUNTA, W_RANIO, W_MESES, \
    W_SUMC, W_CHK = range(5, 16)
W_CAB = 17
W_INI = 18
W_FIN = W_INI + 11
W_TOT = W_FIN + 1
W_SEC_VER = W_TOT + 2
W_C1, W_C2, W_RVER = W_SEC_VER + 1, W_SEC_VER + 2, W_SEC_VER + 3

# --- Franjas del Día ------------------------------------------------------------
NOMBRE_DIA = dict((d, D.NOMBRE_DIA[d][:1].upper() + D.NOMBRE_DIA[d][1:]) for d in D.DIAS)
FRANJAS = D.FRANJAS
NF = len(FRANJAS)
F_DCAB = 5
F_DINI = 6
F_DFIN = F_DINI + len(D.DIAS) - 1
F_PT, F_PP, F_ANTES, F_ANTES2, F_REP = range(F_DFIN + 2, F_DFIN + 7)
F_SEC_FR = F_REP + 2
F_LCAB = F_SEC_FR + 1
F_LINI = F_LCAB + 1
F_LFIN = F_LINI + len(D.DIAS) * NF - 1
F_SEC_SEM = F_LFIN + 2
F_SCAB = F_SEC_SEM + 1
F_SINI = F_SCAB + 1
F_SFIN = F_SINI + NF - 1
F_STOT = F_SFIN + 1
F_LEGAL = F_STOT + 2
F_LISTAS = F_LEGAL + 3
TIPOS_DIA = ('Tipo', 'Punta')
TIPO_DE = dict((d, 'Punta' if d in ('S', 'D') else 'Tipo') for d in D.DIAS)
TXT_OK_CHOC = 'Cabe también como chocolatería'
TXT_SOLO_CAFE = 'Antes de la hora de chocolatería: sólo como cafetería o bar (ejemplo de Madrid)'
TXT_ANTES_TODO = 'Antes de la hora mínima también como cafetería o bar'


def fila_dia(d):
    return F_DINI + D.DIAS.index(d)


def fila_franja_dia(d, k):
    """Tabla larga, día a día: cada día ocupa NF filas seguidas (una por franja)."""
    return F_LINI + D.DIAS.index(d) * NF + k


def tramo(franja, d):
    """Inicio y fin de la franja ese día, o una franja vacía (inicio = fin) si no abre."""
    if d in franja['tramos']:
        return franja['tramos'][d]
    fin = FRANJAS[2]['tramos'][d][1]
    return (fin, fin)


# --- Capacidad, Cola, Refuerzo ---------------------------------------------------
C_CAB = 6
C_INI = 7
C_FIN = C_INI + 11
C_S1, C_S2, C_S3, C_S4 = C_FIN + 2, C_FIN + 3, C_FIN + 4, C_FIN + 5
assert C_S4 == 23        # el libro 1 («Cuello de Botella») cita esta fila: E23
TXT_UNA = 'Una basta: la línea aguanta la hora punta todos los meses'
TXT_UNA_REF = 'Una, con refuerzo en el pico: masa preparada antes de abrir y una persona más'
TXT_DOS = ('Necesitas más línea: activa la segunda freidora en el libro 1 y vuelve a copiar la '
           'capacidad (X4)')

K_CAB = 6
K_INI = 7
K_FIN = K_INI + 11
K_S1, K_S2, K_S3 = K_FIN + 2, K_FIN + 3, K_FIN + 4

R_DIAS, R_HORAS, R_COSTEH, R_HTOT, R_COSTE, R_COLA, R_VERED = range(5, 12)
R_CAB = 13
R_INI = 14
R_FIN = R_INI + 11

# --- El Verano ----------------------------------------------------------------
SALIDAS = [s[:1].upper() + s[1:] for s in D.SALIDAS_VERANO]          # Cerrar, Carta..., Ferias
SALIDA_ELEGIDA = D.SALIDA_VERANO_ELEGIDA[:1].upper() + D.SALIDA_VERANO_ELEGIDA[1:]
assert SALIDA_ELEGIDA in SALIDAS
COLS_SAL = ('B', 'C', 'D')
#: Lo que hace cada salida, como bandera (1 sí, 0 no): abrir el local y salir a las
#: ferias de julio y agosto. Es la definición de D14, en celda verde.
ABRE_LOCAL = {'Cerrar': 0, 'Carta de verano': 1, 'Ferias': 0}
VA_FERIAS = {'Cerrar': 0, 'Carta de verano': 0, 'Ferias': 1}
HORAS_EXTRA_LOCAL = {'Cerrar': 0, 'Carta de verano': 0, 'Ferias': 0}
V_CAB = 6
V_NOM, V_LOCAL, V_FER, V_HEXT, V_RAC, V_VEN, V_MAT, V_PERS, V_FERC, V_CONT, V_MAX = range(7, 18)
V_SEC_DEC = 19
V_ELIGE, V_CELEG, V_GANA, V_AVISO, V_UMBRAL = range(20, 25)
TXT_ELIGE_OK = 'Eliges la que más deja en julio y agosto'
TXT_ELIGE_KO = 'REVISA: hay otra salida que deja más en julio y agosto'

# --- Punto Muerto por Evento ------------------------------------------------------
EVENTOS = D.FERIAS
COLS_EV = ('B', 'C', 'D', 'E')
assert len(EVENTOS) == len(COLS_EV)
E_CAB = 5
#: (clave, etiqueta, unidad, formato, tipo de validación)
CAMPOS_EVENTO = [
    ('evento', 'Evento', '', None, 'texto'),
    ('mes', 'Mes del evento (1 = enero ... 12 = diciembre)', 'mes', ENT, 'mes'),
    ('dias', 'Días que dura', 'días', ENT, 'num'),
    ('horas_dia', 'Horas abiertas al día', 'h/día', DEC1, 'num'),
    ('tasa_fija', 'Tasa fija por todo el evento (base imponible)', 'EUR', EUR, 'num'),
    ('tasa_m2_dia', 'Tasa por m² y día', 'EUR/m²·día', EUR, 'num'),
    ('m2', 'Metros cuadrados del puesto', 'm²', DEC1, 'num'),
    ('desplazamiento', 'Desplazamiento (ida y vuelta, carga incluida)', 'EUR', EUR, 'num'),
    ('montaje', 'Montaje y desmontaje del puesto', 'EUR', EUR, 'num'),
    ('personas', 'Personas en el puesto a la vez', 'personas', ENT, 'num'),
    ('horas_personal_extra', 'Horas de personal que contratas sólo para el evento', 'h', DEC1, 'num'),
    ('afluencia_h', 'Personas que pasan por delante del puesto en una hora', 'personas/h', ENT, 'num'),
    ('conversion', 'De ellas, las que compran', '%', PCT, 'pct'),
    ('raciones_por_compra', 'Raciones por compra', 'raciones', DEC1, 'num'),
    ('ticket_feria', 'PVP medio de una ración en la feria (con IVA)', 'EUR/ración', EUR, 'num'),
    ('va', '¿Vas? (cuenta para el año)', '', None, 'sino'),
]
E_ROW = dict((k, E_CAB + 1 + i) for i, (k, _e, _u, _f, _t) in enumerate(CAMPOS_EVENTO))
E_SEC = E_ROW['va'] + 2
(E_HPUESTO, E_RAC, E_VEN, E_MAT, E_CRAC, E_TASA, E_PERS, E_COSTE, E_PM, E_PMH, E_SEG, E_RES,
 E_CUBRE, E_ORDEN) = range(E_SEC + 1, E_SEC + 15)
E_FVER = E_ORDEN + 2
E_NCUB = E_FVER + 1
E_NOTAS = E_NCUB + 2
E_LISTAS = E_NOTAS + 4
SI_NO = ('Sí', 'No')

# --- Calendario de Ferias ---------------------------------------------------------
L_CAB = 6
L_INI = 7
L_FIN = L_INI + 11
L_TOT = L_FIN + 1
L_SEC_REF = L_TOT + 2
L_REF1, L_REF2 = L_SEC_REF + 1, L_SEC_REF + 2


# ==========================================================================
# Hoja «Instrucciones»
# ==========================================================================
def _orden_relleno():
    partes = ['%d (%s)' % (n, D.LIBROS[n]) for n in D.ORDEN_RELLENO if n != 7]
    return ('Orden de relleno del paquete: ' + ', luego '.join(partes)
            + '. El libro 7 (%s) no depende de ninguno: rellénalo cuando quieras. '
              'Este es el libro 5: rellénalo DESPUÉS del 3 y del 1, que le pasan sus cifras, '
              'y ANTES del 8 y del 6, que copian sus horas de refuerzo, su año y su verano.' % D.LIBROS[7])


def _cruces_texto():
    lineas = []
    for c in CRUCES_IN:
        lineas.append('Parámetros!B%d - %s. Viene del libro %d: %s!%s!%s.' % (
            CRUCE_ROW[c['calcula']], c['concepto'], c['origen'], c['fichero_origen'],
            c['hoja_origen'], c['celda_origen']))
    vistos = set()
    for c in CRUCES_OUT:
        clave = (c['hoja_origen'], c['x'])
        if clave in vistos:
            continue
        vistos.add(clave)
        celdas = [x['celda_origen'] for x in CRUCES_OUT if (x['hoja_origen'], x['x']) == clave]
        rango = celdas[0] if len(celdas) == 1 else '%s a %s' % (celdas[0], celdas[-1])
        lineas.append('%s!%s - %s. Lo copia: libro %d (%s, %s).' % (
            c['hoja_origen'], rango, 'doce coeficientes y raciones del año' if c['x'] == 'X13'
            else ('horas de refuerzo' if c['x'] == 'X7' else c['concepto']),
            c['receptor'], c['fichero_receptor'], c['x']))
    return lineas


PASOS = [
    '1. Hoja «Parámetros». Arriba, siete celdas verdes que copias a mano de los libros 1 y 3 '
    '(cada una dice de qué celda exacta). Debajo, el calendario del año, la hora punta, la '
    'hora mínima de apertura del ejemplo de Madrid y la tolerancia. Al pie, el CUADRE: anota lo '
    'que publica hoy cada celda de origen y, si lo que usas se separa, la fila se pone en rojo.',
    '2. Hoja «Peso sobre el Año». Las raciones de un año normal y doce coeficientes que las '
    'reparten por meses (suman 12). Es lo que copia el libro 6 para su tesorería.',
    '3. Hoja «Franjas del Día». La ÚNICA fuente de las franjas de todo el paquete: a qué hora '
    'empieza y acaba cada franja cada día y qué parte de las raciones del día se lleva. De aquí '
    'salen la hora punta, el semáforo de la hora de apertura y las horas por franja de la '
    'semana tipo (a la derecha, como dato de referencia).',
    '4. Hojas «Capacidad contra el Pico» y «Cola del Domingo». Mes a mes, si la línea aguanta la '
    'hora punta de un día tipo y de un día punta, y cuántas raciones por hora se quedan en cola '
    'el domingo. Diciembre y enero son Navidad y Reyes. Al pie de la primera sale el veredicto '
    '«¿Una churrera o dos?».',
    '5. Hoja «Refuerzo por Pico». Las horas de refuerzo de Navidad y Reyes y lo que cuestan. Las '
    'copia el libro 8.',
    '6. Hoja «El Verano (Tres Salidas)». Cerrar, abrir con carta de verano o salir de ferias, '
    'comparadas por lo que dejan en euros en julio y agosto. Eliges una y su contribución la '
    'copia el libro 6.',
    '7. Hojas «Punto Muerto por Evento» y «Calendario de Ferias». Cada feria con sus días, su tasa '
    'y su afluencia: las raciones que necesitas para cubrirla, lo que deja y su orden. Las que '
    'marcas con «Sí» van al calendario y su resultado del año lo copia el libro 6.',
]

NOTAS_LIBRO = [
    'LA FRANJA DEL DÍA VIVE SÓLO AQUÍ. Ningún otro libro del paquete pide horarios ni '
    'porcentajes por franja: el libro 8 trabaja con sus propios mínimos de cobertura y el '
    'libro 7 cita la norma de horarios y remite a esta hoja, donde pones tu hora de apertura.',
    'EL VERANO SE COMPARA POR CONTRIBUCIÓN. Lo que pagas igual abras o cierres en julio y '
    'agosto (el local, la plantilla fija, los seguros, las cuotas) es lo mismo en las tres '
    'salidas y no entra en este libro: lo resta el libro 6, que enseña cada salida con todo '
    'pagado en su hoja «Escenarios». Por eso aquí cerrar deja cero, no un número negativo.',
    'LAS FERIAS SON MÉTODO, NO CASO. El Molinete no va a ninguna (elige la carta de verano). Los '
    'cuatro eventos de la hoja son ejemplos para enseñar el cálculo: pon los tuyos. Si vas a '
    'montar un puesto que viva de las ferias, el Plan de Negocio Food Truck y el Kit de Tareas '
    'Food Truck de aichef.pro son el sitio; lo legal de la venta ambulante está en el libro 7.',
    'LA HORA MÍNIMA DE APERTURA ES LA DEL EJEMPLO DE MADRID. Allí una chocolatería no abre antes '
    'de las 8:00 y una cafetería o bar puede desde las 6:00: abrir a las 6:00 o a las 7:00 '
    'obliga a clasificarse como cafetería o bar. Otras comunidades tienen su propia norma: '
    'cambia las dos celdas verdes por las de la tuya.',
    'LOS SUPUESTOS NO SON DATOS DEL SECTOR. Los coeficientes de cada mes, el reparto por '
    'franjas, el factor de la hora punta, los días de refuerzo y todos los datos de las ferias '
    'son supuestos declarados de El Molinete, sin fuente pública. Pon los tuyos.',
]

CADENCIA = ('Cada cuánto se usa este libro: los coeficientes y las franjas, al cerrar el primer '
            'año con tus ventas reales de cada mes y de cada franja (el TPV las da); el verano, '
            'cada primavera; las ferias, cuando te llegue cada convocatoria. Si cambia alguna '
            'cifra del bloque «Lo que Copian Otros Libros», cópiala de nuevo en el libro 8 o en '
            'el 6.')


def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS, 0)
    ws.column_dimensions['A'].width = 100.0
    cabecera_hoja(ws, TITULO)
    motor.val(ws, 'A3', 'Para qué sirve: repartir tus raciones por meses y por franjas, saber si '
                        'la línea aguanta la hora punta (y la cola del domingo), cuánto refuerzo '
                        'te toca en Navidad, qué haces en verano y a qué ferias te compensa ir.')
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
              'y una fila de CUADRE que avisa si se separa de lo que publica el origen. Lo que '
              'este libro pasa a otro está en el bloque «Lo que Copian Otros Libros» de cada '
              'hoja (rótulo en la columna K, valor en la L).', wrap=True)
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
    for txt in NOTAS_LIBRO:
        motor.val(ws, 'A%d' % fila, txt, wrap=True)
        ws.row_dimensions[fila].height = 72
        if txt.startswith('LA HORA MÍNIMA'):
            nota_legal(ws, 'A%d' % fila, 'CUN-34')
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
               minimo=0, maximo=None, legal=None, fuente_sector=None):
    motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
    if form is not None:
        cel = formula(ws, 'B%d' % fila, form, fmt=fmt, bold=True, destacar=True)
    else:
        cel = entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
        if pct:
            motor.dv_porcentaje(ws, [cel.coordinate], maximo=maximo)
        else:
            motor.dv_numerica(ws, [cel.coordinate], minimo=minimo, maximo=maximo)
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


def hoja_parametros(wb):
    ws = wb.create_sheet(H_PAR)
    cabecera_hoja(ws, H_PAR, 'Todo lo que el resto de hojas da por sabido vive aquí. Ninguna '
                             'fórmula de este libro lleva dentro un umbral, una hora ni un '
                             'número de días.')
    for letra, ancho in (('A', 56), ('B', 16), ('C', 15), ('D', 46), ('E', 66)):
        ws.column_dimensions[letra].width = ancho
    encabezados(ws, P_CAB, [('A', 'Parámetro', None), ('B', 'Valor', None),
                            ('C', 'Unidad', None), ('D', 'De dónde sale', None),
                            ('E', 'Nota', None)], alto=24, congelar=True)

    seccion(ws, 'A%d' % P_SEC1, 'Lo que Copias del Libro 1 (Producción y Local)')
    seccion(ws, 'A%d' % P_SEC3, 'Lo que Copias del Libro 3 (Carta y Escandallo)')
    for c in CRUCES_IN:
        clave = c['calcula']
        etq, uni, fmt = ETIQUETA_CRUCE[clave]
        fila = CRUCE_ROW[clave]
        valor = c['valor_defecto']
        if fmt == ENT:
            valor = int(round(valor))
        cel = fila_param(ws, fila, etq, valor, fmt, uni, D.rotulo_cruce(c), NOTA_CRUCE[clave])
        CRUCE_VERDES.append((ws.title, cel.coordinate, c['x'], c['concepto']))

    seccion(ws, 'A%d' % P_SEC_CAL, 'Calendario del Año')
    fila_param(ws, P_DANIO, 'Días del año', DIAS_ANIO, ENT, 'días', 'calendario',
               'Un año normal.', minimo=1)
    v, fuente, _n = D.NEGOCIO['dias_cierre_anio']
    fila_param(ws, P_DCIERRE, 'Días al año con el local cerrado', v, ENT, 'días',
               texto_fuente(fuente), 'Cinco días seguidos para la limpieza a fondo y la puesta a '
                                     'punto de la línea. Se restan de los días tipo.')
    fila_param(ws, P_FINDE, 'Sábados y domingos del año', SABADOS_Y_DOMINGOS, ENT, 'días',
               'calendario (52 semanas)', 'Son días punta. Si cierras un día de la semana, '
                                          'réstalo aquí o en los días tipo.')
    v, fuente, _n = D.NEGOCIO['festivos_entre_semana']
    fila_param(ws, P_FEST, 'Festivos de lunes a viernes que abres como un domingo', v, ENT,
               'días', texto_fuente(fuente),
               'Cambian cada año y en cada municipio. Se trabajan como un día punta.')
    fila_param(ws, P_MES1, 'Primer mes del verano (número del mes)', D.MESES_VERANO[0], ENT, 'mes',
               'supuesto declarado de El Molinete',
               'El valle: julio. Si tu valle es otro, cambia los dos meses.', minimo=1, maximo=12)
    fila_param(ws, P_MES2, 'Segundo mes del verano (número del mes)', D.MESES_VERANO[1], ENT, 'mes',
               'supuesto declarado de El Molinete', 'Agosto.', minimo=1, maximo=12)
    fila_param(ws, P_DVER, 'Días de esos dos meses', DIAS_JULIO_AGOSTO, ENT, 'días', 'calendario',
               'Julio y agosto: 31 + 31. Sirve para pasar la contribución del verano a raciones al '
               'día en «El Verano (Tres Salidas)».', minimo=1)

    seccion(ws, 'A%d' % P_SEC_HORA, 'Hora Punta y Hora Mínima de Apertura')
    v, fuente, nota_ = D.PARAMS['factor_hora_punta']
    fila_param(ws, P_FACTOR, 'Factor de la hora punta (la hora más cargada frente a la media de su '
                             'franja)', v, DEC, 'veces', texto_fuente(fuente),
               nota_ + ' Míralo en tu TPV: las ventas de la peor hora entre las de la franja.',
               minimo=1)
    fila_param(ws, P_MIN, 'Minutos de una hora', MINUTOS_HORA, ENT, 'min', 'calendario',
               'Para pasar la cola a minutos de espera.', minimo=1)
    v, fuente, nota_ = D.HORA_MINIMA_APERTURA_MADRID['chocolateria']
    fila_param(ws, P_HCHOC, 'Hora mínima de apertura como chocolatería (ejemplo de Madrid)', v,
               HORA, 'hora', fuente,
               nota_ + ' Si tu comunidad tiene otra norma, pon su hora.', minimo=0, maximo=24,
               legal='CUN-34')
    v, fuente, nota_ = D.HORA_MINIMA_APERTURA_MADRID['cafeteria_bar']
    fila_param(ws, P_HCAFE, 'Hora mínima de apertura como cafetería o bar (ejemplo de Madrid)', v,
               HORA, 'hora', fuente, nota_ + ' Abrir antes de las 8:00 obliga a clasificarse así.',
               minimo=0, maximo=24, legal='CUN-34')

    seccion(ws, 'A%d' % P_SEC_TEMP, 'Temporada, IVA de Feria y Tolerancia')
    fila_param(ws, P_UALTA, 'Coeficiente desde el que un mes es temporada alta', UMBRAL_ALTA, DEC,
               'veces', 'supuesto declarado de El Molinete',
               'Con los coeficientes del ejemplo marca de octubre a marzo, la forma que describen '
               'las fuentes del sector: el churro vive de octubre a marzo con Navidad arriba.',
               minimo=0)
    nota_fuente(ws, 'B%d' % P_UALTA, 'CUS-29 CUS-V17',
                extra='Forma cualitativa de la temporada; el umbral es supuesto.')
    fila_param(ws, P_UVALLE, 'Coeficiente hasta el que un mes es valle', UMBRAL_VALLE, DEC, 'veces',
               'supuesto declarado de El Molinete', 'Con el ejemplo marca julio y agosto.', minimo=0)
    v, fuente, nota_ = D.PARAMS['iva_llevar_comida']
    fila_param(ws, P_IVAF, 'IVA de lo que vendes en una feria (churros para llevar)', v, PCT, '',
               fuente, nota_ + ' El PVP de feria se teclea con IVA y aquí se le quita.', pct=True,
               fuente_sector=fuente)
    fila_param(ws, P_TOL, 'Tolerancia de las filas de CUADRE y de los repartos', TOLERANCIA, PCT, '',
               'heredado: guia-chocolateria (Tolerancia de las filas de CUADRE)',
               'Por encima de esta desviación, la fila de CUADRE avisa de que lo que has copiado '
               'no es lo que publica el libro de origen.', pct=True)

    fila_param(ws, P_UREF, 'Déficit que cubren la masa preparada antes de abrir y una persona más '
                           'en la línea (en % de la capacidad)', UMBRAL_REFUERZO, PCT, '',
               'supuesto declarado de El Molinete',
               'Con un déficit de hora punta por debajo de esta parte de la capacidad, el veredicto '
               '«¿Una churrera o dos?» de «Capacidad contra el Pico» dice que una basta con '
               'refuerzo en el pico. Mide cuánto adelantas con masa preparada y una segunda '
               'persona, y pon tu cifra.', pct=True)

    # --- CUADRE ------------------------------------------------------------------
    seccion(ws, 'A%d' % P_SEC_CUA, 'Cuadre de lo que Has Copiado')
    encabezados(ws, P_CUA_CAB, [('A', 'Cuadre', None),
                                ('B', 'Lo que publica hoy la celda de origen (anótalo)', None),
                                ('C', 'Desviación', None), ('D', 'Veredicto', None),
                                ('E', 'Si no cuadra', None)], alto=36)
    t = PB(P_TOL)
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
                      % (fila, fila, t, ko), bold=True)
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
    setup(ws, apaisado=True, titulos='%d:%d' % (P_CAB, P_CAB))
    return ws


# ==========================================================================
# Hoja «Peso sobre el Año» (origen de X13)
# ==========================================================================
COEF = 'B'          # columna de los coeficientes (verdes)


def coef_mes(m):
    return ABS_(H_ANO, '%s%d' % (COEF, W_INI + m - 1))


def hoja_anio(wb):
    ws = wb.create_sheet(H_ANO)
    cabecera_hoja(ws, H_ANO, 'Las raciones de un año normal y doce coeficientes que las reparten '
                             'por meses. Los coeficientes son SUPUESTOS: no hay reparto mensual '
                             'publicado de churrería.')
    for letra, ancho in (('A', 46), ('B', 15), ('C', 18), ('D', 16), ('E', 13), ('F', 16),
                         ('G', 16), ('H', 16), ('I', 56)):
        ws.column_dimensions[letra].width = ancho
    seccion(ws, 'A4', 'Las Raciones del Año')
    filas = (
        (W_DANIO, 'Días del año', '=%s' % PB(P_DANIO), ENT, 'días'),
        (W_DCIERRE, 'Días con el local cerrado', '=%s' % PB(P_DCIERRE), ENT, 'días'),
        (W_DPUNTA, 'Días punta: sábados, domingos y festivos que abres', '=%s+%s'
         % (PB(P_FINDE), PB(P_FEST)), ENT, 'días'),
        (W_DTIPO, 'Días tipo: el resto de días abiertos', '=B%d-B%d-B%d' % (W_DANIO, W_DCIERRE, W_DPUNTA),
         ENT, 'días'),
        (W_DAPER, 'Días de apertura del año', '=B%d-B%d' % (W_DANIO, W_DCIERRE), ENT, 'días'),
        (W_RTIPO, 'Raciones de un día tipo (copiadas del libro 1)', '=%s' % XB('_raciones_tipo'), ENT,
         'raciones'),
        (W_RPUNTA, 'Raciones de un día punta (copiadas del libro 1)', '=%s' % XB('_raciones_punta'), ENT,
         'raciones'),
        (W_RANIO, 'RACIONES DEL AÑO', '=B%d*B%d+B%d*B%d' % (W_DTIPO, W_RTIPO, W_DPUNTA, W_RPUNTA), ENT,
         'raciones'),
        (W_MESES, 'Meses con coeficiente', '=COUNT(%s%d:%s%d)' % (COEF, W_INI, COEF, W_FIN), ENT, 'meses'),
        (W_SUMC, 'Suma de los doce coeficientes', '=SUM(%s%d:%s%d)' % (COEF, W_INI, COEF, W_FIN), DEC,
         'tiene que dar 12'),
    )
    for fila, etq, form, fmt, uni in filas:
        motor.val(ws, 'A%d' % fila, etq, bold=fila == W_RANIO)
        formula(ws, 'B%d' % fila, form, fmt=fmt, bold=fila == W_RANIO, destacar=fila == W_RANIO)
        motor.val(ws, 'C%d' % fila, uni)
    ko = 'REVISA: los doce coeficientes no suman 12 y los meses no suman el año'
    motor.val(ws, 'A%d' % W_CHK, '¿Los coeficientes reparten el año entero?', bold=True)
    cel = formula(ws, 'B%d' % W_CHK, '=IF(NOT(ISNUMBER(B%d)),"",IF(ABS(B%d-B%d)<=%s*B%d,"CUADRA","%s"))'
                  % (W_SUMC, W_SUMC, W_MESES, PB(P_TOL), W_MESES, ko), bold=True)
    cel.alignment = Alignment(wrap_text=True, vertical='top')
    ws.merge_cells('B%d:D%d' % (W_CHK, W_CHK))
    ws.row_dimensions[W_CHK].height = 30
    motor.semaforo_texto(ws, 'B%d' % W_CHK, (('CUADRA', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                                            (ko, motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    gris(ws, 'D%d' % W_RANIO, 'Lo copia el libro 6 (bloque de la derecha, celda L5).')

    encabezados(ws, W_CAB, [
        ('A', 'Mes', None), ('B', 'Coeficiente (1 = un mes medio)', None),
        ('C', 'Temporada', None), ('D', 'Raciones del mes', None),
        ('E', 'Peso sobre el año', None), ('F', 'Raciones de un día medio del mes', None),
        ('G', 'Raciones de un día tipo del mes', None),
        ('H', 'Raciones de un día punta del mes', None), ('I', 'Nota', None)], alto=48)
    for m in range(1, 13):
        fila = W_INI + m - 1
        motor.val(ws, 'A%d' % fila, D.MESES[m - 1])
        cel = entrada(ws, '%s%d' % (COEF, fila), D.COEFICIENTES_MES[m - 1], fmt=DEC,
                      etiqueta='Coeficiente de %s' % D.MESES[m - 1].lower())
        motor.dv_numerica(ws, [cel.coordinate], minimo=0, maximo=5)
        formula(ws, 'C%d' % fila, '=IF(NOT(ISNUMBER(B{f})),"",IF(B{f}>={a},"Temporada alta",'
                                  'IF(B{f}<={v},"Valle","Media")))'.format(f=fila, a=PB(P_UALTA),
                                                                         v=PB(P_UVALLE)))
        formula(ws, 'D%d' % fila, '=IFERROR($B$%d*B%d/$B$%d,"")' % (W_RANIO, fila, W_MESES), fmt=ENT)
        formula(ws, 'E%d' % fila, '=IFERROR(D%d/$B$%d,"")' % (fila, W_RANIO), fmt=PCT)
        formula(ws, 'F%d' % fila, '=IFERROR(D%d/($B$%d/$B$%d),"")' % (fila, W_DAPER, W_MESES), fmt=ENT)
        formula(ws, 'G%d' % fila, '=IFERROR($B$%d*B%d,"")' % (W_RTIPO, fila), fmt=ENT)
        formula(ws, 'H%d' % fila, '=IFERROR($B$%d*B%d,"")' % (W_RPUNTA, fila), fmt=ENT)
    motor.semaforo_texto(ws, 'C%d:C%d' % (W_INI, W_FIN), (
        ('Temporada alta', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
        ('Valle', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG)))
    gris(ws, 'I%d' % W_INI, 'Supuestos declarados con la forma que describen las fuentes del sector: '
                            'pico de octubre a marzo con Navidad arriba y valle en julio y agosto. '
                            'La serie de búsquedas en internet no vale como reparto de ventas. Al '
                            'cerrar tu primer año, pon los tuyos (ventas del mes entre la media).',
         alto=60)
    ws.merge_cells('I%d:I%d' % (W_INI, W_INI + 2))
    nota_fuente(ws, 'I%d' % W_INI, 'CUS-29 CUS-V17', extra='Forma cualitativa; los valores son supuesto.')
    gris(ws, 'I%d' % (W_FIN - 1), 'Diciembre es Navidad y Reyes: mira la cola del domingo y el '
                                  'refuerzo.', alto=30)
    motor.val(ws, 'A%d' % W_TOT, 'TOTAL del año', bold=True)
    for col, fmt in (('B', DEC), ('D', ENT), ('E', PCT)):
        formula(ws, '%s%d' % (col, W_TOT), '=SUM(%s%d:%s%d)' % (col, W_INI, col, W_FIN), fmt=fmt, bold=True)

    seccion(ws, 'A%d' % W_SEC_VER, 'Julio y Agosto (los Dos Meses del Verano)')
    for fila, etq, mes_p in ((W_C1, 'Coeficiente del primer mes del verano', P_MES1),
                             (W_C2, 'Coeficiente del segundo mes del verano', P_MES2)):
        motor.val(ws, 'A%d' % fila, etq)
        formula(ws, 'B%d' % fila, '=IFERROR(INDEX($B$%d:$B$%d,%s),"")' % (W_INI, W_FIN, PB(mes_p)),
                fmt=DEC)
    motor.val(ws, 'A%d' % W_RVER, 'Raciones que vendería el local en julio y agosto', bold=True)
    formula(ws, 'B%d' % W_RVER, '=IFERROR((B%d+B%d)*$B$%d/$B$%d,"")' % (W_C1, W_C2, W_RANIO, W_MESES),
            fmt=ENT, bold=True, destacar=True)
    gris(ws, 'C%d' % W_RVER, 'Si abre con carta de verano. Lo usa la hoja «El Verano (Tres Salidas)».')
    ws.merge_cells('C%d:F%d' % (W_RVER, W_RVER))

    filas_c = [(5, 'Raciones del año', '=B%d' % W_RANIO, ENT)]
    for m in range(1, 13):
        filas_c.append((5 + m, 'Coeficiente de %s' % D.MESES[m - 1].lower(),
                        '=%s%d' % (COEF, W_INI + m - 1), DEC))
    bloque_contrato(ws, filas_c)
    version_al_pie(ws, W_RVER + 2)
    setup(ws, apaisado=True)
    return ws


# ==========================================================================
# Hoja «Franjas del Día» (fuente ÚNICA de la franja; origen de X7)
# ==========================================================================
def hoja_franjas(wb):
    ws = wb.create_sheet(H_FRA)
    cabecera_hoja(ws, H_FRA, 'La franja del día vive SÓLO aquí. Horario y reparto de las raciones '
                             'de cada día, la hora punta y el semáforo de la hora de apertura.')
    for letra, ancho in (('A', 26), ('B', 13), ('C', 13), ('D', 13), ('E', 30), ('F', 14),
                         ('G', 14), ('H', 15), ('I', 15), ('J', 15)):
        ws.column_dimensions[letra].width = ancho
    cap = XB('capacidad_raciones_h')
    factor = PB(P_FACTOR)
    seccion(ws, 'A4', 'Los Siete Días')
    encabezados(ws, F_DCAB, [
        ('A', 'Día', None), ('B', 'Tipo de día', None),
        ('C', 'Raciones del día (mes medio)', None), ('D', 'Hora de apertura', None),
        ('E', 'Hora de apertura frente a la mínima legal (ejemplo de Madrid)', None),
        ('F', 'Horas abiertas', None), ('G', 'Reparto de las raciones (tiene que dar 100 %)', None),
        ('H', 'Hora punta del día (raciones/h)', None),
        ('I', 'Hora punta si es día tipo', None), ('J', 'Hora punta si es día punta', None)], alto=58)
    lista_tipo = '=$A$%d:$A$%d' % (F_LISTAS + 2, F_LISTAS + 1 + len(TIPOS_DIA))
    coords_tipo = []
    for d in D.DIAS:
        fila = fila_dia(d)
        primera = fila_franja_dia(d, 0)
        ultima = fila_franja_dia(d, NF - 1)
        motor.val(ws, 'A%d' % fila, NOMBRE_DIA[d], bold=True)
        cel = entrada(ws, 'B%d' % fila, TIPO_DE[d], etiqueta='Tipo de día del %s' % D.NOMBRE_DIA[d])
        coords_tipo.append(cel.coordinate)
        formula(ws, 'C%d' % fila, '=IF(B{f}="Punta",{p},IF(B{f}="Tipo",{t},""))'.format(
            f=fila, p=XB('_raciones_punta'), t=XB('_raciones_tipo')), fmt=ENT)
        formula(ws, 'D%d' % fila, '=C%d' % primera, fmt=HORA)
        cel = formula(ws, 'E%d' % fila, '=IF(NOT(ISNUMBER(D{f})),"",IF(D{f}<{cafe},"{todo}",'
                                        'IF(D{f}<{choc},"{solo}","{ok}")))'.format(
                                            f=fila, cafe=PB(P_HCAFE), choc=PB(P_HCHOC),
                                            todo=TXT_ANTES_TODO, solo=TXT_SOLO_CAFE, ok=TXT_OK_CHOC),
                      bold=True)
        cel.alignment = Alignment(wrap_text=True, vertical='top')
        formula(ws, 'F%d' % fila, '=SUMIF($B$%d:$B$%d,A%d,$E$%d:$E$%d)'
                % (F_LINI, F_LFIN, fila, F_LINI, F_LFIN), fmt=DEC1)
        formula(ws, 'G%d' % fila, '=SUMIF($B$%d:$B$%d,A%d,$F$%d:$F$%d)'
                % (F_LINI, F_LFIN, fila, F_LINI, F_LFIN), fmt=PCT)
        formula(ws, 'H%d' % fila, '=MAX(I%d:I%d)' % (primera, ultima), fmt=DEC1, bold=True)
        formula(ws, 'I%d' % fila, '=IF(B%d="Tipo",H%d,"")' % (fila, fila), fmt=DEC1)
        formula(ws, 'J%d' % fila, '=IF(B%d="Punta",H%d,"")' % (fila, fila), fmt=DEC1)
        ws.row_dimensions[fila].height = 34
    motor.semaforo_texto(ws, 'E%d:E%d' % (F_DINI, F_DFIN), (
        (TXT_OK_CHOC, motor.CF_VERDE_BG, motor.CF_VERDE_FG),
        (TXT_SOLO_CAFE, motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
        (TXT_ANTES_TODO, motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    nota_legal(ws, 'E%d' % F_DCAB, 'CUN-34')

    resumen = (
        (F_PT, 'Hora punta de un día tipo (la más alta de los días tipo), mes medio',
         '=MAX(I%d:I%d)' % (F_DINI, F_DFIN), DEC1, 'raciones/h'),
        (F_PP, 'Hora punta de un día punta (la más alta de los días punta), mes medio',
         '=MAX(J%d:J%d)' % (F_DINI, F_DFIN), DEC1, 'raciones/h'),
        (F_ANTES, 'Días que abres antes de la hora mínima de chocolatería',
         '=COUNTIF(E%d:E%d,"%s")+COUNTIF(E%d:E%d,"%s")' % (F_DINI, F_DFIN, TXT_SOLO_CAFE, F_DINI, F_DFIN,
                                                          TXT_ANTES_TODO), ENT, 'días'),
        (F_ANTES2, 'De ellos, días que abres antes de la hora mínima incluso como cafetería o bar',
         '=COUNTIF(E%d:E%d,"%s")' % (F_DINI, F_DFIN, TXT_ANTES_TODO), ENT, 'días'),
        (F_REP, 'Días cuyo reparto de raciones no suma el 100 %',
         '=COUNTIF(G{a}:G{b},"<"&(1-{t}))+COUNTIF(G{a}:G{b},">"&(1+{t}))'.format(
             a=F_DINI, b=F_DFIN, t=PB(P_TOL)), ENT, 'días'),
    )
    for fila, etq, form, fmt, uni in resumen:
        motor.val(ws, 'A%d' % fila, etq, wrap=True)
        ws.merge_cells('A%d:D%d' % (fila, fila))
        formula(ws, 'E%d' % fila, form, fmt=fmt, bold=True, destacar=fila in (F_PT, F_PP))
        motor.val(ws, 'F%d' % fila, uni)
        ws.row_dimensions[fila].height = 22
    motor.semaforo_isnumber(ws, 'E%d' % F_ANTES2, '$E$%d' % F_ANTES2, '>', '0')
    motor.semaforo_isnumber(ws, 'E%d' % F_REP, '$E$%d' % F_REP, '>', '0')
    gris(ws, 'G%d' % F_ANTES, 'El Molinete abre a las 6:00 y a las 7:00: en el ejemplo de Madrid '
                              'se clasifica como cafetería o bar (decisión 8). El libro 7 cita la '
                              'norma y remite aquí.', alto=44)
    ws.merge_cells('G%d:J%d' % (F_ANTES, F_ANTES))

    seccion(ws, 'A%d' % F_SEC_FR, 'Las Franjas, Día a Día')
    encabezados(ws, F_LCAB, [
        ('A', 'Franja', None), ('B', 'Día', None),
        ('C', 'Empieza (hora: 16,5 = 16:30)', None), ('D', 'Acaba (25 = la 1:00 del día siguiente)', None),
        ('E', 'Horas', None), ('F', 'Parte de las raciones del día', None),
        ('G', 'Raciones de la franja (mes medio)', None), ('H', 'Raciones por hora (media)', None),
        ('I', 'Raciones por hora en su hora punta', None),
        ('J', '¿Aguanta la línea? (mes medio)', None)], alto=58)
    coords_hora, coords_pct = [], []
    for d in D.DIAS:
        for k, fr in enumerate(FRANJAS):
            fila = fila_franja_dia(d, k)
            a, b = tramo(fr, d)
            motor.val(ws, 'A%d' % fila, fr['nombre'])
            motor.val(ws, 'B%d' % fila, NOMBRE_DIA[d])
            coords_hora.append(entrada(ws, 'C%d' % fila, a, fmt=HORA,
                                       etiqueta='%s del %s: empieza' % (fr['nombre'], D.NOMBRE_DIA[d])).coordinate)
            coords_hora.append(entrada(ws, 'D%d' % fila, b, fmt=HORA,
                                       etiqueta='%s del %s: acaba' % (fr['nombre'], D.NOMBRE_DIA[d])).coordinate)
            formula(ws, 'E%d' % fila, '=IF(AND(ISNUMBER(C{f}),ISNUMBER(D{f})),MAX(0,D{f}-C{f}),"")'
                    .format(f=fila), fmt=DEC1)
            coords_pct.append(entrada(ws, 'F%d' % fila, D.pct_franja(fr, d) / 100.0, fmt=PCT,
                                      etiqueta='%s del %s: parte de las raciones'
                                      % (fr['nombre'], D.NOMBRE_DIA[d])).coordinate)
            formula(ws, 'G%d' % fila, '=IFERROR($C$%d*F%d,"")' % (fila_dia(d), fila), fmt=DEC1)
            formula(ws, 'H%d' % fila, '=IFERROR(G%d/E%d,"")' % (fila, fila), fmt=DEC1)
            formula(ws, 'I%d' % fila, '=IFERROR(H%d*%s,"")' % (fila, factor), fmt=DEC1)
            formula(ws, 'J%d' % fila, '=IF(NOT(ISNUMBER(I%d)),"",IF(I%d<=%s,"Sí","No"))'
                    % (fila, fila, cap))
            if k == 0:
                for col in 'ABCDEFGHIJ':
                    ws['%s%d' % (col, fila)].border = openpyxl.styles.Border(
                        top=openpyxl.styles.Side(style='thin', color='999999'))
    motor.dv_numerica(ws, coords_hora, minimo=0, maximo=30, titulo='Hora no válida',
                      mensaje='Escribe la hora en horas decimales, entre 0 y 30 (16,5 = 16:30; '
                              '25 = la 1:00 del día siguiente).')
    motor.dv_porcentaje(ws, coords_pct)
    motor.semaforo_texto(ws, 'J%d:J%d' % (F_LINI, F_LFIN), (
        ('Sí', motor.CF_VERDE_BG, motor.CF_VERDE_FG), ('No', motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    gris(ws, 'K%d' % F_LINI, 'Si un día no abres una franja, pon la misma hora de inicio y de fin y '
                             'un 0 % de las raciones. El 100 % de cada día se reparte entre sus '
                             'franjas: el resumen de arriba cuenta los días que no cuadran.', alto=30)
    ws.merge_cells('K%d:M%d' % (F_LINI, F_LINI + 2))

    seccion(ws, 'A%d' % F_SEC_SEM, 'Cada Franja en la Semana (lo que Copia el Libro 8)')
    encabezados(ws, F_SCAB, [('A', 'Franja', None), ('B', 'Horas a la semana', None),
                             ('C', 'Raciones a la semana (mes medio)', None),
                             ('D', 'Parte de las raciones de la semana', None)], alto=44)
    for k, fr in enumerate(FRANJAS):
        fila = F_SINI + k
        motor.val(ws, 'A%d' % fila, fr['nombre'], bold=True)
        formula(ws, 'B%d' % fila, '=SUMIF($A$%d:$A$%d,A%d,$E$%d:$E$%d)'
                % (F_LINI, F_LFIN, fila, F_LINI, F_LFIN), fmt=DEC1, bold=True)
        formula(ws, 'C%d' % fila, '=SUMIF($A$%d:$A$%d,A%d,$G$%d:$G$%d)'
                % (F_LINI, F_LFIN, fila, F_LINI, F_LFIN), fmt=ENT)
        formula(ws, 'D%d' % fila, '=IFERROR(C%d/$C$%d,"")' % (fila, F_STOT), fmt=PCT)
    motor.val(ws, 'A%d' % F_STOT, 'TOTAL de la semana', bold=True)
    for col, fmt in (('B', DEC1), ('C', ENT), ('D', PCT)):
        formula(ws, '%s%d' % (col, F_STOT), '=SUM(%s%d:%s%d)' % (col, F_SINI, col, F_SFIN), fmt=fmt, bold=True)

    texto(ws, 'A%d' % F_LEGAL, 'La hora mínima de apertura es la del ejemplo de Madrid (celdas verdes de '
                               '«Parámetros», con su nota). Una chocolatería allí no abre antes de las '
                               '8:00; una cafetería o bar, desde las 6:00. No se extrapola a otras '
                               'comunidades: pon la norma de la tuya.', alto=44, merge_hasta='J',
          italica=True)
    nota_legal(ws, 'A%d' % F_LEGAL, 'CUN-34')

    refs, _fin = CC.bloque_listas(ws, F_LISTAS, (('Tipo de día', TIPOS_DIA),))
    assert refs['Tipo de día'] == lista_tipo, (refs, lista_tipo)
    CC.dv_rango(ws, coords_tipo, refs['Tipo de día'], 'Tipo de día',
                'Elige «Tipo» (las raciones del día tipo) o «Punta» (las del día punta).')

    # R-15: las horas por franja ya NO viajan al libro 8 (sólo alimentaban una suma de control);
    # se publican como dato de referencia, para citarlas en el mapa.
    filas_c = [(5 + k, 'Horas a la semana: %s' % FRANJAS[k]['nombre'].lower(), '=B%d' % (F_SINI + k), DEC1)
               for k in range(NF)]
    assert [f for f, _r, _x, _m in filas_c] == [5, 6, 7, 8]
    bloque_contrato(ws, filas_c, titulo='Horas por Franja de la Semana Tipo (Dato de Referencia)')
    version_al_pie(ws, _fin + 1)
    setup(ws, apaisado=True, titulos='%d:%d' % (F_LCAB, F_LCAB))
    return ws


# ==========================================================================
# Hoja «Capacidad contra el Pico»
# ==========================================================================
def hoja_capacidad(wb):
    ws = wb.create_sheet(H_CAP)
    cabecera_hoja(ws, H_CAP, 'Mes a mes, la hora punta de un día tipo y de un día punta frente a lo '
                             'que saca la línea en una hora. Se mide en raciones, no en tickets.')
    for letra, ancho in (('A', 14), ('B', 13), ('C', 15), ('D', 15), ('E', 16), ('F', 16),
                         ('G', 14), ('H', 15), ('I', 15), ('J', 30), ('K', 50)):
        ws.column_dimensions[letra].width = ancho
    encabezados(ws, C_CAB, [
        ('A', 'Mes', None), ('B', 'Coeficiente', None),
        ('C', 'Raciones de un día tipo', None), ('D', 'Raciones de un día punta', None),
        ('E', 'Hora punta de un día tipo (raciones/h)', None),
        ('F', 'Hora punta de un día punta (raciones/h)', None),
        ('G', 'Capacidad de la línea (raciones/h)', None),
        ('H', 'Déficit en un día tipo (raciones/h)', None),
        ('I', 'Déficit en un día punta (raciones/h)', None),
        ('J', '¿Aguanta la línea?', None)], alto=58, congelar=True)
    pt = ABS_(H_FRA, 'E%d' % F_PT)
    pp = ABS_(H_FRA, 'E%d' % F_PP)
    for m in range(1, 13):
        fila = C_INI + m - 1
        ano = W_INI + m - 1
        motor.val(ws, 'A%d' % fila, D.MESES[m - 1])
        formula(ws, 'B%d' % fila, '=%s' % coef_mes(m), fmt=DEC)
        formula(ws, 'C%d' % fila, '=%sG%d' % (Q(H_ANO), ano), fmt=ENT)
        formula(ws, 'D%d' % fila, '=%sH%d' % (Q(H_ANO), ano), fmt=ENT)
        formula(ws, 'E%d' % fila, '=IFERROR(%s*B%d,"")' % (pt, fila), fmt=DEC1)
        formula(ws, 'F%d' % fila, '=IFERROR(%s*B%d,"")' % (pp, fila), fmt=DEC1)
        formula(ws, 'G%d' % fila, '=%s' % XB('capacidad_raciones_h'), fmt=DEC1)
        for col, dem in (('H', 'E'), ('I', 'F')):
            formula(ws, '%s%d' % (col, fila), '=IF(AND(ISNUMBER({d}{f}),ISNUMBER(G{f})),MAX(0,{d}{f}-G{f}),"")'
                    .format(d=dem, f=fila), fmt=DEC1)
        cel = formula(ws, 'J%d' % fila, '=IF(NOT(AND(ISNUMBER(H{f}),ISNUMBER(I{f}))),"",IF(H{f}>0,'
                                        '"No, tampoco entre semana",IF(I{f}>0,"No en los días punta",'
                                        '"Sí")))'.format(f=fila), bold=True)
        cel.alignment = Alignment(wrap_text=True)
    motor.semaforo_texto(ws, 'J%d:J%d' % (C_INI, C_FIN), (
        ('Sí', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
        ('No en los días punta', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
        ('No, tampoco entre semana', motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    gris(ws, 'K%d' % C_INI, 'La hora punta de cada mes es la de un mes medio (hoja «Franjas del '
                            'Día») por el coeficiente del mes. La capacidad es la del conjunto, la '
                            'que manda el equipo más lento (libro 1, «Cuello de Botella»).', alto=48)
    ws.merge_cells('K%d:K%d' % (C_INI, C_INI + 2))
    for fila, etq, form, fmt in (
            (C_S1, 'Meses que no aguanta en los días punta', '=COUNTIF(I%d:I%d,">0")' % (C_INI, C_FIN), ENT),
            (C_S2, 'Meses que no aguanta ni entre semana', '=COUNTIF(H%d:H%d,">0")' % (C_INI, C_FIN), ENT),
            (C_S3, 'Peor déficit de un día punta (raciones/h)', '=MAX(I%d:I%d)' % (C_INI, C_FIN), DEC1)):
        motor.val(ws, 'A%d' % fila, etq, bold=True)
        ws.merge_cells('A%d:D%d' % (fila, fila))
        formula(ws, 'E%d' % fila, form, fmt=fmt, bold=True, destacar=True)
    motor.semaforo_isnumber(ws, 'E%d' % C_S2, '$E$%d' % C_S2, '>', '0')
    # R-03: el veredicto de «¿una churrera o dos?» vive AQUÍ, donde se cruzan la capacidad y las franjas
    motor.val(ws, 'A%d' % C_S4, '¿UNA CHURRERA O DOS?', bold=True)
    ws.merge_cells('A%d:D%d' % (C_S4, C_S4))
    cap = XB('capacidad_raciones_h')
    cel = formula(ws, 'E%d' % C_S4,
                  '=IF(OR(NOT(ISNUMBER(E{a})),NOT(ISNUMBER(E{b})),NOT(ISNUMBER(E{c})),NOT(ISNUMBER({cap}))),"",'
                  'IF(E{a}=0,"{una}",IF(AND(E{b}=0,E{c}<={u}*{cap}),"{ref}","{dos}")))'
                  .format(a=C_S1, b=C_S2, c=C_S3, cap=cap, u=PB(P_UREF), una=TXT_UNA, ref=TXT_UNA_REF,
                          dos=TXT_DOS), bold=True, destacar=True)
    cel.alignment = Alignment(wrap_text=True, vertical='top')
    ws.merge_cells('E%d:J%d' % (C_S4, C_S4))
    ws.row_dimensions[C_S4].height = 34
    motor.semaforo_texto(ws, 'E%d' % C_S4, ((TXT_UNA, motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                                            (TXT_UNA_REF, motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                                            (TXT_DOS, motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    texto(ws, 'A%d' % (C_S4 + 2), 'Un «No» no quiere decir que no puedas abrir ese mes: quiere decir '
                                  'que en la peor hora se te forma cola. Las palancas, en este orden: '
                                  'masa preparada antes de abrir, una segunda persona en la línea '
                                  '(hoja «Refuerzo por Pico») y, si no basta, más línea: el '
                                  'veredicto de arriba te dice cuándo.',
          alto=44, merge_hasta='J', italica=True)
    version_al_pie(ws, C_S4 + 4)
    setup(ws, apaisado=True, titulos='%d:%d' % (C_CAB, C_CAB))
    return ws


# ==========================================================================
# Hoja «Cola del Domingo»
# ==========================================================================
def hoja_cola(wb):
    ws = wb.create_sheet(H_COL)
    cabecera_hoja(ws, H_COL, 'El domingo por la mañana es el día punta del día punta. Mes a mes, '
                             'las raciones por hora que la línea no llega a servir en esa hora.')
    for letra, ancho in (('A', 14), ('B', 13), ('C', 15), ('D', 16), ('E', 14), ('F', 17),
                         ('G', 12), ('H', 16), ('I', 52)):
        ws.column_dimensions[letra].width = ancho
    encabezados(ws, K_CAB, [
        ('A', 'Mes', None), ('B', 'Coeficiente', None), ('C', 'Raciones del domingo', None),
        ('D', 'Hora punta del domingo (raciones/h)', None),
        ('E', 'Capacidad de la línea (raciones/h)', None),
        ('F', 'COLA: raciones por hora que no llegas a servir', None),
        ('G', '¿Hay cola?', None), ('H', 'Espera al final de la hora punta (minutos)', None),
        ('I', 'Nota', None)], alto=58, congelar=True)
    dom = fila_dia('D')
    for m in range(1, 13):
        fila = K_INI + m - 1
        motor.val(ws, 'A%d' % fila, D.MESES[m - 1])
        formula(ws, 'B%d' % fila, '=%s' % coef_mes(m), fmt=DEC)
        formula(ws, 'C%d' % fila, '=IFERROR(%s*B%d,"")' % (ABS_(H_FRA, 'C%d' % dom), fila), fmt=ENT)
        formula(ws, 'D%d' % fila, '=IFERROR(%s*B%d,"")' % (ABS_(H_FRA, 'H%d' % dom), fila), fmt=DEC1)
        formula(ws, 'E%d' % fila, '=%s' % XB('capacidad_raciones_h'), fmt=DEC1)
        formula(ws, 'F%d' % fila, '=IF(AND(ISNUMBER(D{f}),ISNUMBER(E{f})),MAX(0,D{f}-E{f}),"")'
                .format(f=fila), fmt=DEC1, bold=True)
        formula(ws, 'G%d' % fila, '=IF(NOT(ISNUMBER(F%d)),"",IF(F%d>0,"Sí","No"))' % (fila, fila), bold=True)
        formula(ws, 'H%d' % fila, '=IFERROR(F%d/E%d*%s,"")' % (fila, fila, PB(P_MIN)), fmt=DEC1)
    motor.semaforo_texto(ws, 'G%d:G%d' % (K_INI, K_FIN), (
        ('Sí', motor.CF_ROJO_BG, motor.CF_ROJO_FG), ('No', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    gris(ws, 'I%d' % K_INI, 'Diciembre y enero son Navidad y Reyes: los domingos y festivos de esas '
                            'semanas son los de más cola del año.', alto=34)
    gris(ws, 'I%d' % (K_INI + 3), 'La cola sale de la franja más cargada del domingo (hoja «Franjas del '
                                  'Día», fila del domingo) por el coeficiente del mes, frente a la '
                                  'capacidad de la línea copiada del libro 1.', alto=46)
    for fila, etq, form, fmt in (
            (K_S1, 'Meses con cola el domingo', '=COUNTIF(G%d:G%d,"Sí")' % (K_INI, K_FIN), ENT),
            (K_S2, 'Peor cola del año (raciones/h)', '=MAX(F%d:F%d)' % (K_INI, K_FIN), DEC1),
            (K_S3, 'Mes de la peor cola', '=IF(NOT(ISNUMBER(E%d)),"",IF(E%d>0,INDEX(A%d:A%d,MATCH(E%d,F%d:F%d,0)),'
                                          '"Ninguno"))' % (K_S2, K_S2, K_INI, K_FIN, K_S2, K_INI, K_FIN), None)):
        motor.val(ws, 'A%d' % fila, etq, bold=True)
        ws.merge_cells('A%d:D%d' % (fila, fila))
        formula(ws, 'E%d' % fila, form, fmt=fmt, bold=True, destacar=True)
    texto(ws, 'A%d' % (K_S3 + 2), 'La cola no se arregla subiendo el precio: se arregla con masa '
                                  'preparada antes de abrir y con una segunda persona en la línea en '
                                  'esas mañanas. Las horas de ese refuerzo están en la hoja «Refuerzo '
                                  'por Pico».', alto=44, merge_hasta='H', italica=True)
    version_al_pie(ws, K_S3 + 4)
    setup(ws, apaisado=True, titulos='%d:%d' % (K_CAB, K_CAB))
    return ws


# ==========================================================================
# Hoja «Refuerzo por Pico» (origen de X7, horas de refuerzo)
# ==========================================================================
def hoja_refuerzo(wb):
    ws = wb.create_sheet(H_REF)
    cabecera_hoja(ws, H_REF, 'Las horas de refuerzo de Navidad y Reyes, por encima del medio '
                             'refuerzo fijo de los fines de semana (que está en la plantilla del '
                             'libro 8), y lo que cuestan.')
    for letra, ancho in (('A', 52), ('B', 16), ('C', 14), ('D', 14), ('E', 56)):
        ws.column_dimensions[letra].width = ancho
    seccion(ws, 'A4', 'El Refuerzo de Navidad y Reyes')
    v, fuente, nota_ = D.PARAMS['dias_refuerzo_navidad_reyes']
    motor.val(ws, 'A%d' % R_DIAS, 'Días punta de Navidad y Reyes con una persona más por la mañana',
              wrap=True)
    cel = entrada(ws, 'B%d' % R_DIAS, v, fmt=ENT, etiqueta='Días de refuerzo de Navidad y Reyes')
    motor.dv_numerica(ws, [cel.coordinate], minimo=0, maximo=60)
    motor.val(ws, 'C%d' % R_DIAS, 'días')
    gris(ws, 'E%d' % R_DIAS, texto_fuente(fuente) + '. ' + nota_)
    v, fuente, nota_ = D.PARAMS['horas_refuerzo_dia']
    motor.val(ws, 'A%d' % R_HORAS, 'Horas de refuerzo cada uno de esos días')
    cel = entrada(ws, 'B%d' % R_HORAS, v, fmt=DEC1, etiqueta='Horas de refuerzo al día')
    motor.dv_numerica(ws, [cel.coordinate], minimo=0, maximo=14)
    motor.val(ws, 'C%d' % R_HORAS, 'h/día')
    gris(ws, 'E%d' % R_HORAS, texto_fuente(fuente) + '. ' + nota_)
    motor.val(ws, 'A%d' % R_COSTEH, 'Coste hora de mano de obra (copiado del libro 3)')
    formula(ws, 'B%d' % R_COSTEH, '=%s' % XB('coste_hora_mano_obra'), fmt=EUR)
    motor.val(ws, 'C%d' % R_COSTEH, 'EUR/h')
    motor.val(ws, 'A%d' % R_HTOT, 'HORAS DE REFUERZO AL AÑO', bold=True)
    formula(ws, 'B%d' % R_HTOT, '=IFERROR(B%d*B%d,"")' % (R_DIAS, R_HORAS), fmt=DEC1, bold=True, destacar=True)
    motor.val(ws, 'C%d' % R_HTOT, 'h/año')
    gris(ws, 'E%d' % R_HTOT, 'Las copia el libro 8 (bloque de la derecha) para el coste de la plantilla.')
    motor.val(ws, 'A%d' % R_COSTE, 'Lo que cuesta ese refuerzo al año', bold=True)
    formula(ws, 'B%d' % R_COSTE, '=IFERROR(B%d*B%d,"")' % (R_HTOT, R_COSTEH), fmt=EUR, bold=True)
    motor.val(ws, 'C%d' % R_COSTE, 'EUR/año')
    motor.val(ws, 'A%d' % R_COLA, 'Peor cola del domingo del año (hoja «Cola del Domingo»)')
    formula(ws, 'B%d' % R_COLA, '=%s' % ABS_(H_COL, 'E%d' % K_S2), fmt=DEC1)
    motor.val(ws, 'C%d' % R_COLA, 'raciones/h')
    si = 'Hay cola en algún domingo: el refuerzo tiene sentido'
    no = 'No hay cola en ningún domingo: revisa si necesitas el refuerzo'
    motor.val(ws, 'A%d' % R_VERED, '¿Lo pide la cola?', bold=True)
    cel = formula(ws, 'B%d' % R_VERED, '=IF(NOT(ISNUMBER(B%d)),"",IF(B%d>0,"%s","%s"))'
                  % (R_COLA, R_COLA, si, no), bold=True)
    cel.alignment = Alignment(wrap_text=True, vertical='top')
    ws.merge_cells('B%d:D%d' % (R_VERED, R_VERED))
    ws.row_dimensions[R_VERED].height = 30
    motor.semaforo_texto(ws, 'B%d' % R_VERED, ((si, motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                                              (no, motor.CF_AMBAR_BG, motor.CF_AMBAR_FG)))

    encabezados(ws, R_CAB, [('A', 'Mes', None), ('B', 'Cola del domingo (raciones/h)', None),
                            ('C', '¿Hay cola?', None), ('D', 'Temporada', None),
                            ('E', 'Qué hacer', None)], alto=44)
    for m in range(1, 13):
        fila = R_INI + m - 1
        motor.val(ws, 'A%d' % fila, D.MESES[m - 1])
        formula(ws, 'B%d' % fila, '=%sF%d' % (Q(H_COL), K_INI + m - 1), fmt=DEC1)
        formula(ws, 'C%d' % fila, '=%sG%d' % (Q(H_COL), K_INI + m - 1))
        formula(ws, 'D%d' % fila, '=%sC%d' % (Q(H_ANO), W_INI + m - 1))
        formula(ws, 'E%d' % fila, '=IF(C{f}="Sí","Una persona más en la línea los domingos y festivos '
                                  'por la mañana",IF(D{f}="Temporada alta","Vigila la cola: estás '
                                  'cerca","Sin refuerzo"))'.format(f=fila))
    motor.semaforo_texto(ws, 'C%d:C%d' % (R_INI, R_FIN), (
        ('Sí', motor.CF_ROJO_BG, motor.CF_ROJO_FG), ('No', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    texto(ws, 'A%d' % (R_FIN + 2), 'El medio refuerzo fijo de los sábados y domingos ya está en la '
                                   'plantilla de El Molinete (libro 8). Aquí sólo van las horas de más '
                                   'de Navidad y Reyes. El coste hora es el del escandallo del libro 3: '
                                   'si el libro 8 te da otro, cuadra los dos.', alto=44, merge_hasta='E',
          italica=True)
    bloque_contrato(ws, [(5, 'Horas de refuerzo de Navidad y Reyes al año', '=B%d' % R_HTOT, DEC1)])
    version_al_pie(ws, R_FIN + 4)
    setup(ws, apaisado=True, titulos='%d:%d' % (R_CAB, R_CAB))
    return ws


# ==========================================================================
# Hoja «El Verano (Tres Salidas)» (origen de X16)
# ==========================================================================
def hoja_verano(wb):
    ws = wb.create_sheet(H_VER)
    cabecera_hoja(ws, H_VER, 'Julio y agosto: cerrar, abrir con carta de verano o salir de ferias. '
                             'Se comparan por lo que DEJAN en euros; lo que pagas igual en las tres '
                             'lo resta el libro 6.')
    for letra, ancho in (('A', 58), ('B', 18), ('C', 18), ('D', 18), ('E', 54)):
        ws.column_dimensions[letra].width = ancho
    encabezados(ws, V_CAB, [('A', 'Concepto', None), ('B', 'Salida 1', None),
                            ('C', 'Salida 2', None), ('D', 'Salida 3', None),
                            ('E', 'Nota', None)], alto=24)
    rver = ABS_(H_ANO, 'B%d' % W_RVER)
    ticket, materia = XB('_ticket_verano'), XB('_materia_verano')
    coste_h = XB('coste_hora_mano_obra')
    fver = ABS_(H_PME, 'B%d' % E_FVER)
    flags = []
    for col, sal in zip(COLS_SAL, SALIDAS):
        motor.val(ws, '%s%d' % (col, V_NOM), sal, bold=True)
        ws['%s%d' % (col, V_NOM)].alignment = Alignment(horizontal='center')
        flags.append(entrada(ws, '%s%d' % (col, V_LOCAL), ABRE_LOCAL[sal], fmt=ENT,
                             etiqueta='%s: ¿abre el local?' % sal).coordinate)
        flags.append(entrada(ws, '%s%d' % (col, V_FER), VA_FERIAS[sal], fmt=ENT,
                             etiqueta='%s: ¿va a las ferias?' % sal).coordinate)
        cel = entrada(ws, '%s%d' % (col, V_HEXT), HORAS_EXTRA_LOCAL[sal], fmt=DEC1,
                      etiqueta='%s: horas de personal extra del local' % sal)
        motor.dv_numerica(ws, [cel.coordinate], minimo=0)
        formula(ws, '%s%d' % (col, V_RAC), '=IFERROR(%s%d*%s,"")' % (col, V_LOCAL, rver), fmt=ENT)
        formula(ws, '%s%d' % (col, V_VEN), '=IFERROR(%s%d*%s,"")' % (col, V_RAC, ticket), fmt=EUR)
        formula(ws, '%s%d' % (col, V_MAT), '=IFERROR(%s%d*%s,"")' % (col, V_RAC, materia), fmt=EUR)
        formula(ws, '%s%d' % (col, V_PERS), '=IFERROR(%s%d*%s,"")' % (col, V_HEXT, coste_h), fmt=EUR)
        formula(ws, '%s%d' % (col, V_FERC), '=IFERROR(%s%d*%s,"")' % (col, V_FER, fver), fmt=EUR)
        formula(ws, '%s%d' % (col, V_CONT), '=IFERROR({c}{v}-{c}{m}-{c}{p}+{c}{f},"")'.format(
            c=col, v=V_VEN, m=V_MAT, p=V_PERS, f=V_FERC), fmt=EUR, bold=True, destacar=True)
        formula(ws, '%s%d' % (col, V_MAX), '=IF(NOT(ISNUMBER({c}{r})),"",IF({c}{r}=MAX($B${r}:$D${r}),'
                                           '"La que más deja",""))'.format(c=col, r=V_CONT), bold=True)
    motor.dv_numerica(ws, flags, minimo=0, maximo=1, titulo='1 o 0',
                      mensaje='Escribe 1 (sí) o 0 (no).')
    motor.semaforo_texto(ws, 'B%d:D%d' % (V_MAX, V_MAX), (('La que más deja', motor.CF_VERDE_BG,
                                                           motor.CF_VERDE_FG),))
    nota_fuente(ws, 'C%d' % V_NOM, 'CUS-11', extra='Carta de verano de una chocolatería real '
                                                   '(granizado, horchata, batido): sólo el formato; '
                                                   'los precios de El Molinete están en el libro 3.')
    filas = (
        (V_LOCAL, '¿Abre el local en julio y agosto? (1 sí, 0 no)',
         'Cerrar y salir de ferias dejan el local cerrado; la carta de verano lo abre.'),
        (V_FER, '¿Sale a las ferias de julio y agosto? (1 sí, 0 no)',
         'Las de la hoja «Punto Muerto por Evento» cuyo mes es uno de los dos del verano.'),
        (V_HEXT, 'Horas de personal extra del local en julio y agosto',
         'Si la carta de verano necesita a alguien más (heladería, terraza). En El Molinete, ninguna.'),
        (V_RAC, 'Raciones que vende el local', 'Las de julio y agosto de «Peso sobre el Año».'),
        (V_VEN, 'Ventas del local sin IVA', 'Raciones por el ticket de verano del libro 3.'),
        (V_MAT, 'Materia de esas raciones (aceite absorbido incluido)', 'Raciones por la materia de verano del libro 3.'),
        (V_PERS, 'Personal extra del local', 'Horas extra por el coste hora del libro 3.'),
        (V_FERC, 'Lo que dejan las ferias de julio y agosto',
         'Ya descontadas su materia, sus tasas, el desplazamiento, el montaje y su personal.'),
        (V_CONT, 'CONTRIBUCIÓN DE JULIO Y AGOSTO',
         'Ventas menos materia menos personal extra, más lo que dejan las ferias. Cerrar deja cero: '
         'lo que pagas aun cerrado lo resta el libro 6.'),
        (V_MAX, '¿La que más deja?', ''),
    )
    motor.val(ws, 'A%d' % V_NOM, 'Salida', bold=True)
    for fila, etq, nota_ in filas:
        motor.val(ws, 'A%d' % fila, etq, wrap=True, bold=fila in (V_CONT, V_MAX))
        if nota_:
            gris(ws, 'E%d' % fila, nota_)
        ws.row_dimensions[fila].height = 32

    seccion(ws, 'A%d' % V_SEC_DEC, 'La Salida que Eliges (lo que Copia el Libro 6)')
    motor.val(ws, 'A%d' % V_ELIGE, 'La salida que eliges', bold=True)
    cel = entrada(ws, 'B%d' % V_ELIGE, SALIDA_ELEGIDA, etiqueta='La salida del verano que eliges')
    CC.dv_rango(ws, [cel.coordinate], '=$B$%d:$D$%d' % (V_NOM, V_NOM), 'Salida del verano',
                'Elige una de las tres salidas de la fila %d.' % V_NOM)
    gris(ws, 'E%d' % V_ELIGE, 'El Molinete elige la carta de verano (decisión 9).')
    rng_nom = '$B$%d:$D$%d' % (V_NOM, V_NOM)
    rng_con = '$B$%d:$D$%d' % (V_CONT, V_CONT)
    motor.val(ws, 'A%d' % V_CELEG, 'CONTRIBUCIÓN DE JULIO Y AGOSTO DE LA SALIDA QUE ELIGES', bold=True)
    formula(ws, 'B%d' % V_CELEG, '=IFERROR(INDEX(%s,MATCH(B%d,%s,0)),"")' % (rng_con, V_ELIGE, rng_nom),
            fmt=EUR, bold=True, destacar=True)
    gris(ws, 'E%d' % V_CELEG, 'La copia el libro 6 (bloque de la derecha, L5): la resta de dos '
                              'meses de lo que pagas igual la hace él, en «Escenarios».')
    motor.val(ws, 'A%d' % V_GANA, 'La salida que más deja')
    formula(ws, 'B%d' % V_GANA, '=IFERROR(INDEX(%s,MATCH(MAX(%s),%s,0)),"")' % (rng_nom, rng_con, rng_con))
    motor.val(ws, 'A%d' % V_AVISO, '¿Eliges la que más deja?', bold=True)
    cel = formula(ws, 'B%d' % V_AVISO, '=IF(OR(B%d="",B%d=""),"",IF(B%d=B%d,"%s","%s"))'
                  % (V_ELIGE, V_GANA, V_ELIGE, V_GANA, TXT_ELIGE_OK, TXT_ELIGE_KO), bold=True)
    cel.alignment = Alignment(wrap_text=True, vertical='top')
    ws.merge_cells('B%d:D%d' % (V_AVISO, V_AVISO))
    ws.row_dimensions[V_AVISO].height = 30
    motor.semaforo_texto(ws, 'B%d' % V_AVISO, ((TXT_ELIGE_OK, motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                                              (TXT_ELIGE_KO, motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    motor.val(ws, 'A%d' % V_UMBRAL, 'Raciones al día del local por debajo de las cuales la carta de '
                                    'verano deja menos que salir de ferias', wrap=True)
    formula(ws, 'B%d' % V_UMBRAL, '=IFERROR(D%d/(%s-%s)/%s,"")' % (V_CONT, ticket, materia, PB(P_DVER)),
            fmt=DEC1, bold=True)
    motor.val(ws, 'C%d' % V_UMBRAL, 'raciones/día')
    gris(ws, 'E%d' % V_UMBRAL, 'Lo que dejan las ferias del verano entre lo que deja una ración de '
                               'carta de verano, repartido entre los días de julio y agosto.')
    ws.row_dimensions[V_UMBRAL].height = 34
    texto(ws, 'A%d' % (V_UMBRAL + 2), 'Por qué cerrar deja cero y no un número negativo: lo que pagas '
                                      'igual abras o cierres (el local, la plantilla fija, los seguros, '
                                      'las cuotas) es lo mismo en las tres salidas, así que no cambia '
                                      'cuál gana. El libro 6 enseña cada salida con todo eso restado, '
                                      'en su hoja «Escenarios».', alto=46, merge_hasta='E', italica=True)
    rng_ven = '$B$%d:$D$%d' % (V_VEN, V_VEN)
    bloque_contrato(ws, [
        (5, 'Contribución de julio y agosto de la salida que eliges', '=B%d' % V_CELEG, EUR),
        (6, 'Contribución de julio y agosto si cierras', '=B%d' % V_CONT, EUR),
        (7, 'Contribución de julio y agosto con carta de verano', '=C%d' % V_CONT, EUR),
        (8, 'Contribución de julio y agosto con ferias', '=D%d' % V_CONT, EUR),
        (9, 'Ventas sin IVA de julio y agosto de la salida que eliges',
         '=IFERROR(INDEX(%s,MATCH(B%d,%s,0)),"")' % (rng_ven, V_ELIGE, rng_nom), EUR),
    ])
    version_al_pie(ws, V_UMBRAL + 4)
    setup(ws, apaisado=True)
    return ws


# ==========================================================================
# Hoja «Punto Muerto por Evento»
# ==========================================================================
def EV(clave, col):
    return '%s%d' % (col, E_ROW[clave])


def hoja_punto_muerto(wb):
    ws = wb.create_sheet(H_PME)
    cabecera_hoja(ws, H_PME, 'Cada feria con sus días, su tasa y su gente: cuántas raciones '
                             'necesitas para cubrirla y cuánto deja. Los cuatro eventos son '
                             'EJEMPLOS para enseñar el cálculo, no un caso: pon los tuyos.')
    for letra, ancho in (('A', 54), ('B', 17), ('C', 17), ('D', 17), ('E', 17), ('F', 13), ('G', 52)):
        ws.column_dimensions[letra].width = ancho
    encabezados(ws, E_CAB, [('A', 'Concepto', None)] + [(col, e['id'], None) for col, e in
                                                         zip(COLS_EV, EVENTOS)]
                + [('F', 'Unidad', None), ('G', 'Nota', None)], alto=24, congelar=True)
    iva = PB(P_IVAF)
    materia = XB('_materia_llevar')
    coste_h = XB('coste_hora_mano_obra')
    coords = {'num': [], 'pct': [], 'mes': [], 'sino': []}
    for clave, etq, uni, fmt, tipo in CAMPOS_EVENTO:
        fila = E_ROW[clave]
        motor.val(ws, 'A%d' % fila, etq, wrap=True, bold=clave in ('evento', 'va'))
        motor.val(ws, 'F%d' % fila, uni)
        for col, e in zip(COLS_EV, EVENTOS):
            v = e[clave]
            if clave == 'va':
                v = 'Sí' if v else 'No'
            cel = entrada(ws, '%s%d' % (col, fila), v, fmt=fmt, etiqueta='%s: %s' % (e['id'], etq))
            if tipo in coords:
                coords[tipo].append(cel.coordinate)
            if clave == 'evento':
                cel.alignment = Alignment(wrap_text=True, vertical='top')
        ws.row_dimensions[fila].height = 30 if clave != 'evento' else 44
    motor.dv_numerica(ws, coords['num'], minimo=0)
    motor.dv_porcentaje(ws, coords['pct'])
    motor.dv_numerica(ws, coords['mes'], minimo=1, maximo=12, titulo='Mes no válido',
                      mensaje='Escribe el número del mes, de 1 (enero) a 12 (diciembre).')
    nota_fuente(ws, 'B%d' % E_ROW['evento'], '', extra='Eventos de ejemplo: supuesto declarado, todo. '
                                                       'Son método, no caso (D2).')
    gris(ws, 'G%d' % E_ROW['tasa_fija'], 'La de tu ayuntamiento o la de la comisión de fiestas. Unas '
                                         'cobran por toda la feria y otras por metro y día: rellena la '
                                         'que te toque y deja la otra a cero.', alto=44)
    gris(ws, 'G%d' % E_ROW['afluencia_h'], 'Cuéntala tú: una hora, un día normal de la feria, la gente '
                                           'que pasa por delante del sitio que te dan.', alto=30)
    gris(ws, 'G%d' % E_ROW['ticket_feria'], 'Otra carta y otro precio que en la barra del local. Se '
                                            'teclea con IVA, como lo pones en el cartel.', alto=30)
    gris(ws, 'G%d' % E_ROW['va'], '«Sí» lo lleva al «Calendario de Ferias» y a la cuenta del año del '
                                  'libro 6 (salvo julio y agosto, que van en «El Verano»).', alto=30)

    seccion(ws, 'A%d' % E_SEC, 'Lo que Sale de Cada Evento')
    for col in COLS_EV:
        r = lambda k: EV(k, col)                                              # noqa: E731
        formula(ws, '%s%d' % (col, E_HPUESTO), '=IFERROR(%s*%s*%s,"")' % (r('personas'), r('dias'),
                                                                          r('horas_dia')), fmt=DEC1)
        formula(ws, '%s%d' % (col, E_RAC), '=IFERROR(%s*%s*%s*%s*%s,"")' % (
            r('afluencia_h'), r('horas_dia'), r('dias'), r('conversion'), r('raciones_por_compra')), fmt=ENT)
        formula(ws, '%s%d' % (col, E_VEN), '=IFERROR(%s%d*%s/(1+%s),"")' % (col, E_RAC, r('ticket_feria'), iva),
                fmt=EUR)
        formula(ws, '%s%d' % (col, E_MAT), '=IFERROR(%s%d*%s,"")' % (col, E_RAC, materia), fmt=EUR)
        formula(ws, '%s%d' % (col, E_CRAC), '=IFERROR(%s/(1+%s)-%s,"")' % (r('ticket_feria'), iva, materia),
                fmt=EUR4)
        formula(ws, '%s%d' % (col, E_TASA), '=IFERROR(%s+%s*%s*%s,"")' % (r('tasa_fija'), r('tasa_m2_dia'),
                                                                          r('m2'), r('dias')), fmt=EUR)
        formula(ws, '%s%d' % (col, E_PERS), '=IFERROR(%s*%s,"")' % (r('horas_personal_extra'), coste_h), fmt=EUR)
        formula(ws, '%s%d' % (col, E_COSTE), '=IFERROR({c}{t}+{d}+{m}+{c}{p},"")'.format(
            c=col, t=E_TASA, d=r('desplazamiento'), m=r('montaje'), p=E_PERS), fmt=EUR, bold=True)
        formula(ws, '%s%d' % (col, E_PM), '=IFERROR(%s%d/%s%d,"")' % (col, E_COSTE, col, E_CRAC), fmt=ENT,
                bold=True, destacar=True)
        formula(ws, '%s%d' % (col, E_PMH), '=IFERROR(%s%d/(%s*%s),"")' % (col, E_PM, r('dias'), r('horas_dia')),
                fmt=DEC1)
        formula(ws, '%s%d' % (col, E_SEG), '=IFERROR(%s%d/%s%d-1,"")' % (col, E_RAC, col, E_PM), fmt=PCT)
        formula(ws, '%s%d' % (col, E_RES), '=IFERROR({c}{v}-{c}{m}-{c}{k},"")'.format(
            c=col, v=E_VEN, m=E_MAT, k=E_COSTE), fmt=EUR, bold=True, destacar=True)
        formula(ws, '%s%d' % (col, E_CUBRE), '=IF(NOT(ISNUMBER({c}{r})),"",IF({c}{r}>=0,"Sí","No"))'
                .format(c=col, r=E_RES), bold=True)
        formula(ws, '%s%d' % (col, E_ORDEN), '=IF(NOT(ISNUMBER({c}{r})),"",COUNTIF($B${r}:$E${r},">"&{c}{r})+1)'
                .format(c=col, r=E_RES), fmt=ENT, bold=True)
    for fila, etq, uni in (
            (E_HPUESTO, 'Horas de puesto (personas x días x horas)', 'h'),
            (E_RAC, 'Raciones que esperas vender', 'raciones'),
            (E_VEN, 'Ventas sin IVA', 'EUR'),
            (E_MAT, 'Materia de esas raciones (la de una ración para llevar, libro 3)', 'EUR'),
            (E_CRAC, 'Lo que deja cada ración (PVP sin IVA menos materia)', 'EUR/ración'),
            (E_TASA, 'Tasa total del puesto', 'EUR'),
            (E_PERS, 'Personal contratado para el evento (al coste hora del libro 3)', 'EUR'),
            (E_COSTE, 'Lo que cuesta el evento sin la materia', 'EUR'),
            (E_PM, 'RACIONES PARA CUBRIR EL EVENTO (punto muerto)', 'raciones'),
            (E_PMH, 'Raciones por hora para cubrirlo', 'raciones/h'),
            (E_SEG, 'Margen de seguridad (lo que esperas sobre el punto muerto)', ''),
            (E_RES, 'LO QUE DEJA EL EVENTO', 'EUR'),
            (E_CUBRE, '¿Cubre el evento?', ''),
            (E_ORDEN, 'Orden (1 = el que más deja)', '')):
        motor.val(ws, 'A%d' % fila, etq, wrap=True, bold=fila in (E_PM, E_RES, E_CUBRE, E_ORDEN))
        motor.val(ws, 'F%d' % fila, uni)
        ws.row_dimensions[fila].height = 28
    motor.semaforo_texto(ws, 'B%d:E%d' % (E_CUBRE, E_CUBRE), (
        ('Sí', motor.CF_VERDE_BG, motor.CF_VERDE_FG), ('No', motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    gris(ws, 'G%d' % E_PM, 'Lo que cuesta el evento (sin la materia) entre lo que deja cada ración. Si '
                           'esperas vender menos, el evento no se paga.', alto=34)
    gris(ws, 'G%d' % E_ORDEN, 'Se ordena contando cuántos eventos dejan más que este (COUNTIF): si '
                              'dos empatan, comparten número.', alto=30)
    gris(ws, 'G%d' % E_PERS, 'Sólo el personal que contratas para el evento. Si va gente de la '
                             'plantilla, su coste ya está en el libro 6, pero esas horas faltan en el '
                             'local.', alto=44)
    mes1, mes2 = PB(P_MES1), PB(P_MES2)
    rng_mes = '$B$%d:$E$%d' % (E_ROW['mes'], E_ROW['mes'])
    rng_res = '$B$%d:$E$%d' % (E_RES, E_RES)
    motor.val(ws, 'A%d' % E_FVER, 'Lo que dejan los eventos de julio y agosto (salida «Ferias» del verano)',
              bold=True, wrap=True)
    formula(ws, 'B%d' % E_FVER, '=SUMIF(%s,%s,%s)+SUMIF(%s,%s,%s)' % (rng_mes, mes1, rng_res, rng_mes, mes2,
                                                                      rng_res), fmt=EUR, bold=True, destacar=True)
    gris(ws, 'G%d' % E_FVER, 'Todos los de esos dos meses, marques «Sí» o no: es la salida «Ferias» '
                             'de «El Verano (Tres Salidas)».', alto=30)
    motor.val(ws, 'A%d' % E_NCUB, 'Eventos que se cubren')
    formula(ws, 'B%d' % E_NCUB, '=COUNTIF(B%d:E%d,"Sí")' % (E_CUBRE, E_CUBRE), fmt=ENT, bold=True)
    texto(ws, 'A%d' % E_NOTAS, 'Lo legal de una feria (autorización municipal, venta ambulante, gas de '
                               'la caseta y requisitos higiénicos) está en el libro 7, hoja «Ferias y '
                               'Venta Ambulante». Si vas a vivir de las ferias, el Plan de Negocio Food '
                               'Truck y el Kit de Tareas Food Truck de aichef.pro son el sitio.',
          alto=46, merge_hasta='G', italica=True)
    texto(ws, 'A%d' % (E_NOTAS + 1), 'La tasa de una feria cambia de un pueblo a otro y de un año a otro: '
                                     'la del «Calendario de Ferias» es el ejemplo de un pueblo pequeño, '
                                     'nunca un orden de magnitud. Pide la tuya por escrito.', alto=34,
          merge_hasta='G', italica=True)
    refs, _fin = CC.bloque_listas(ws, E_LISTAS, (('Sí o no', SI_NO),))
    CC.dv_rango(ws, coords['sino'], refs['Sí o no'], '¿Vas?', 'Elige «Sí» o «No».')
    version_al_pie(ws, _fin + 1)
    setup(ws, apaisado=True, titulos='%d:%d' % (E_CAB, E_CAB))
    return ws


# ==========================================================================
# Hoja «Calendario de Ferias» (origen de X14)
# ==========================================================================
def hoja_calendario(wb):
    ws = wb.create_sheet(H_CAL)
    cabecera_hoja(ws, H_CAL, 'Las ferias a las que vas (las marcadas con «Sí»), mes a mes, frente a '
                             'la temporada del local. Lo que dejan fuera de julio y agosto es la línea '
                             'de ferias del libro 6.')
    for letra, ancho in (('A', 9), ('B', 14), ('C', 13), ('D', 13), ('E', 16), ('F', 12),
                         ('G', 17), ('H', 34)):
        ws.column_dimensions[letra].width = ancho
    encabezados(ws, L_CAB, [
        ('A', 'Nº de mes', None), ('B', 'Mes', None), ('C', 'Coeficiente del local', None),
        ('D', 'Eventos a los que vas', None), ('E', 'Lo que dejan (EUR)', None),
        ('F', '¿Mes de verano?', None), ('G', 'Cuenta para el libro 6 (EUR)', None),
        ('H', '¿Choca con la temporada alta del local?', None)], alto=58, congelar=True)
    rng_mes = Q(H_PME) + '$B$%d:$E$%d' % (E_ROW['mes'], E_ROW['mes'])
    rng_va = Q(H_PME) + '$B$%d:$E$%d' % (E_ROW['va'], E_ROW['va'])
    rng_res = Q(H_PME) + '$B$%d:$E$%d' % (E_RES, E_RES)
    choca = 'Sí: el local también va a tope'
    for m in range(1, 13):
        fila = L_INI + m - 1
        motor.val(ws, 'A%d' % fila, m)
        motor.val(ws, 'B%d' % fila, D.MESES[m - 1])
        formula(ws, 'C%d' % fila, '=%s' % coef_mes(m), fmt=DEC)
        formula(ws, 'D%d' % fila, '=COUNTIFS(%s,A%d,%s,"Sí")' % (rng_mes, fila, rng_va), fmt=ENT)
        formula(ws, 'E%d' % fila, '=SUMIFS(%s,%s,A%d,%s,"Sí")' % (rng_res, rng_mes, fila, rng_va), fmt=EUR)
        formula(ws, 'F%d' % fila, '=IF(OR(A%d=%s,A%d=%s),"Sí","No")' % (fila, PB(P_MES1), fila, PB(P_MES2)))
        formula(ws, 'G%d' % fila, '=IF(F%d="Sí","",E%d)' % (fila, fila), fmt=EUR)
        formula(ws, 'H%d' % fila, '=IF(NOT(ISNUMBER(D{f})),"",IF(D{f}=0,"",IF(C{f}>={a},"{s}","No")))'
                .format(f=fila, a=PB(P_UALTA), s=choca))
    motor.semaforo_texto(ws, 'H%d:H%d' % (L_INI, L_FIN), ((choca, motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),))
    motor.val(ws, 'B%d' % L_TOT, 'TOTAL', bold=True)
    for col, fmt in (('D', ENT), ('E', EUR), ('G', EUR)):
        formula(ws, '%s%d' % (col, L_TOT), '=SUM(%s%d:%s%d)' % (col, L_INI, col, L_FIN), fmt=fmt, bold=True,
                destacar=col == 'G')
    seccion(ws, 'A%d' % L_SEC_REF, 'Dos Referencias Reales, para Leer el Orden de las Cosas')
    for fila, ref in ((L_REF1, D.FERIAS_REFERENCIAS[0]), (L_REF2, D.FERIAS_REFERENCIAS[1])):
        texto(ws, 'A%d' % fila, '%s: %s.' % (ref['que'], ref['dato']), alto=34, merge_hasta='H')
        if ref['fuente'].startswith('CUN-'):
            nota_legal(ws, 'A%d' % fila, ref['fuente'])
        else:
            nota_fuente(ws, 'A%d' % fila, ref['fuente'])
    texto(ws, 'A%d' % (L_REF2 + 2), 'Por qué julio y agosto no cuentan aquí para el libro 6: esos dos '
                                    'meses se valoran en «El Verano (Tres Salidas)», y si eliges salir de '
                                    'ferias su contribución viaja al libro 6 por otra celda. Contarlas '
                                    'también aquí las sumaría dos veces.', alto=46, merge_hasta='H',
          italica=True)
    texto(ws, 'A%d' % (L_REF2 + 3), 'Una feria que cae en temporada alta saca a gente del local justo '
                                    'cuando más vende: la columna H lo avisa. El Molinete no va a '
                                    'ninguna.', alto=34, merge_hasta='H', italica=True)
    bloque_contrato(ws, [(5, 'Lo que dejan las ferias del año fuera de julio y agosto',
                          '=G%d' % L_TOT, EUR)])
    version_al_pie(ws, L_REF2 + 5)
    setup(ws, apaisado=True, titulos='%d:%d' % (L_CAB, L_CAB))
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
    for c in CRUCES_OUT:
        m.append(('%s (origen de %s)' % (c['concepto'], c['x']), c['hoja_origen'], c['celda_origen'], 'salida'))
    for k in range(NF):
        m.append(('Horas a la semana de la franja %s (dato de referencia)' % FRANJAS[k]['nombre'].lower(),
                  H_FRA, 'L%d' % (5 + k), 'salida'))
    m += [
        ('Veredicto «¿Una churrera o dos?»', H_CAP, 'E%d' % C_S4, 'salida'),
        ('Déficit que cubren masa preparada y una persona más (% de la capacidad)', H_PAR,
         'B%d' % P_UREF, 'parametro'),
        ('Días al año con el local cerrado', H_PAR, 'B%d' % P_DCIERRE, 'entrada'),
        ('Festivos de lunes a viernes que se abren como un domingo', H_PAR, 'B%d' % P_FEST, 'entrada'),
        ('Factor de la hora punta', H_PAR, 'B%d' % P_FACTOR, 'parametro'),
        ('Hora mínima de apertura como chocolatería (ejemplo de Madrid)', H_PAR, 'B%d' % P_HCHOC, 'parametro'),
        ('Hora mínima de apertura como cafetería o bar (ejemplo de Madrid)', H_PAR, 'B%d' % P_HCAFE, 'parametro'),
        ('Coeficiente desde el que un mes es temporada alta', H_PAR, 'B%d' % P_UALTA, 'parametro'),
        ('IVA de lo que se vende en una feria', H_PAR, 'B%d' % P_IVAF, 'parametro'),
        ('Tolerancia de las filas de CUADRE', H_PAR, 'B%d' % P_TOL, 'parametro'),
        ('Cuadre de la capacidad de la línea (veredicto)', H_PAR,
         'D%d' % CUADRE_ROW['capacidad_raciones_h'], 'salida'),
        ('Días tipo del año', H_ANO, 'B%d' % W_DTIPO, 'salida'),
        ('Días punta del año', H_ANO, 'B%d' % W_DPUNTA, 'salida'),
        ('Días de apertura del año', H_ANO, 'B%d' % W_DAPER, 'salida'),
        ('Raciones de diciembre', H_ANO, 'D%d' % (W_INI + 11), 'salida'),
        ('Raciones de agosto', H_ANO, 'D%d' % (W_INI + 7), 'salida'),
        ('Peso de diciembre sobre el año', H_ANO, 'E%d' % (W_INI + 11), 'salida'),
        ('Raciones de un día medio de diciembre', H_ANO, 'F%d' % (W_INI + 11), 'salida'),
        ('Raciones del local en julio y agosto con carta de verano', H_ANO, 'B%d' % W_RVER, 'salida'),
        ('Hora de apertura del sábado', H_FRA, 'D%d' % fila_dia('S'), 'salida'),
        ('Hora de apertura del lunes', H_FRA, 'D%d' % fila_dia('L'), 'salida'),
        ('Semáforo de la hora de apertura del sábado', H_FRA, 'E%d' % fila_dia('S'), 'salida'),
        ('Días que se abre antes de la hora mínima de chocolatería', H_FRA, 'E%d' % F_ANTES, 'salida'),
        ('Hora punta de un día tipo, mes medio (raciones/h)', H_FRA, 'E%d' % F_PT, 'salida'),
        ('Hora punta de un día punta, mes medio (raciones/h)', H_FRA, 'E%d' % F_PP, 'salida'),
        ('Inicio del desayuno del sábado', H_FRA, 'C%d' % fila_franja_dia('S', 0), 'entrada'),
        ('Parte de las raciones del desayuno del domingo', H_FRA, 'F%d' % fila_franja_dia('D', 0), 'entrada'),
        ('Parte de las raciones de la semana que se lleva el desayuno', H_FRA, 'D%d' % F_SINI, 'salida'),
        ('Parte de las raciones de la semana que se lleva la merienda', H_FRA, 'D%d' % (F_SINI + 2), 'salida'),
        ('Raciones de la semana (mes medio)', H_FRA, 'C%d' % F_STOT, 'salida'),
        ('Hora punta de un día punta de diciembre (raciones/h)', H_CAP, 'F%d' % (C_INI + 11), 'salida'),
        ('Déficit de un día punta de diciembre (raciones/h)', H_CAP, 'I%d' % (C_INI + 11), 'salida'),
        ('Meses que la línea no aguanta en los días punta', H_CAP, 'E%d' % C_S1, 'salida'),
        ('Cola del domingo de diciembre (raciones/h)', H_COL, 'F%d' % (K_INI + 11), 'salida'),
        ('Espera al final de la hora punta del domingo de diciembre (min)', H_COL, 'H%d' % (K_INI + 11), 'salida'),
        ('Meses con cola el domingo', H_COL, 'E%d' % K_S1, 'salida'),
        ('Mes de la peor cola del domingo', H_COL, 'E%d' % K_S3, 'salida'),
        ('Días de refuerzo de Navidad y Reyes', H_REF, 'B%d' % R_DIAS, 'entrada'),
        ('Horas de refuerzo al día', H_REF, 'B%d' % R_HORAS, 'entrada'),
        ('Coste del refuerzo de Navidad y Reyes al año', H_REF, 'B%d' % R_COSTE, 'salida'),
        ('Contribución de julio y agosto si se cierra', H_VER, 'B%d' % V_CONT, 'salida'),
        ('Contribución de julio y agosto con carta de verano', H_VER, 'C%d' % V_CONT, 'salida'),
        ('Contribución de julio y agosto saliendo de ferias', H_VER, 'D%d' % V_CONT, 'salida'),
        ('Ventas sin IVA del local en julio y agosto con carta de verano', H_VER, 'C%d' % V_VEN, 'salida'),
        ('Salida del verano que se elige', H_VER, 'B%d' % V_ELIGE, 'entrada'),
        ('Salida del verano que más deja', H_VER, 'B%d' % V_GANA, 'salida'),
        ('Raciones al día por debajo de las cuales la carta de verano deja menos que las ferias',
         H_VER, 'B%d' % V_UMBRAL, 'salida'),
        ('Lo que dejan los eventos de julio y agosto', H_PME, 'B%d' % E_FVER, 'salida'),
    ]
    for col, e in zip(COLS_EV, EVENTOS):
        m.append(('Raciones para cubrir el evento %s (punto muerto)' % e['id'], H_PME, '%s%d' % (col, E_PM), 'salida'))
        m.append(('Lo que deja el evento %s' % e['id'], H_PME, '%s%d' % (col, E_RES), 'salida'))
        m.append(('Orden del evento %s' % e['id'], H_PME, '%s%d' % (col, E_ORDEN), 'salida'))
    m += [
        ('Eventos a los que se va en el año', H_CAL, 'D%d' % L_TOT, 'salida'),
        ('Lo que dejan todos los eventos a los que se va', H_CAL, 'E%d' % L_TOT, 'salida'),
    ]
    return m


# ==========================================================================
# Cierre: guardar, cachear, verificar, cruces, lista negra y mapa
# ==========================================================================
_PROHIBIDAS = ('INDIRECT', 'COUNTA', 'PMT(', 'OFFSET', 'XLOOKUP', 'LET(', 'LAMBDA', 'RANK(',
               'NETWORKDAYS', 'IRR(')
RX_CONST_DEC = re.compile(r'[*/]\s*\d{1,3}[.,]\d{1,4}(?!\d)')
#: Enteros que pueden ir en una fórmula: el cero y el uno («uno menos», «más uno»).
#: Cualquier otro número tecleado aborta: los doce meses salen de COUNT, los minutos y
#: las horas de «Parámetros».
_ENTEROS_OK = {'0', '1'}
_RX_NUM = re.compile(r'(?<![A-Z$0-9.])(\d+(?:\.\d+)?)(?![0-9]*[(!])')
#: Rótulos que no pueden aparecer en el libro 5 (SR-03, D14): viven en el libro 6.
_RX_VETADOS_5 = (re.compile(r'gastos\s+fijos', re.I), re.compile(r'\brenta\b', re.I),
                 re.compile(r'\brentab', re.I), re.compile(r'\b676\b'), re.compile(r'\bcanon\b', re.I),
                 re.compile(r'posici[oó]n\s+1\b', re.I), re.compile(r'\bRANK\b'))


def _textos(wbf):
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                if isinstance(c.value, str):
                    yield '%s!%s' % (ws.title, c.coordinate), c.value, c.data_type == 'f'
                if c.comment is not None:
                    yield '%s!%s (nota)' % (ws.title, c.coordinate), c.comment.text, False


def _gate_lista_negra(wbf):
    fallos = []
    rotulos = set(D.rotulo_cruce(c) for c in CRUCES_IN)
    for donde, txt, es_formula in _textos(wbf):
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
        if not es_formula and '(nota)' not in donde:
            for rx in _RX_VETADOS_5:
                if rx.search(txt):
                    fallos.append('%s: rótulo vetado en el libro 5 (%s): %s' % (donde, rx.pattern, txt[:70]))
        elif '(nota)' in donde:
            for rx in _RX_VETADOS_5[:2] + _RX_VETADOS_5[3:4]:
                if rx.search(txt):
                    fallos.append('%s: rótulo vetado en una nota del libro 5 (%s)' % (donde, rx.pattern))
        if 'trae aquí la cifra de' in bajo:
            fallos.append('%s: rótulo de cruce con la fórmula de la hermana' % donde)
        if 'cópialo del libro' in bajo and txt.strip() not in rotulos:
            fallos.append('%s: rótulo de cruce que no está en CRUCES: %s' % (donde, txt[:80]))
    if fallos:
        raise SystemExit('LISTA NEGRA / IDS PROHIBIDOS en %s:\n  %s' % (NOMBRE, '\n  '.join(fallos[:40])))


def _gate_cruces(wbf, wbv):
    """Receptor: cada cruce con receptor 5 tiene su verde en «Parámetros» con el rótulo
    exacto y el `valor_defecto`, y su fila de CUADRE en verde. Origen: cada celda de X7,
    X13, X14 y X16 tiene rótulo en K y el valor de `datos_ejemplo`."""
    if D._ERROR_CRUCES:
        raise SystemExit('datos_ejemplo no pudo calcular los cruces: %s' % D._ERROR_CRUCES)
    fallos, filas = [], []
    if len(CRUCE_VERDES) != len(CRUCES_IN) or len(CRUCE_CUADRES) != len(CRUCES_IN):
        fallos.append('%d cruces, %d verdes de cruce y %d filas de CUADRE'
                      % (len(CRUCES_IN), len(CRUCE_VERDES), len(CRUCE_CUADRES)))
    for c in CRUCES_IN:
        fila = CRUCE_ROW[c['calcula']]
        cel_v = wbf[H_PAR]['B%d' % fila]
        if not motor.es_verde(cel_v) or cel_v.protection.locked:
            fallos.append('%s: Parámetros!B%d no es verde y editable' % (c['x'], fila))
        if wbf[H_PAR]['D%d' % fila].value != D.rotulo_cruce(c):
            fallos.append('%s: Parámetros!D%d no lleva el rótulo %r' % (c['x'], fila, D.rotulo_cruce(c)))
        v = wbv[H_PAR]['B%d' % fila].value
        esperado = c['valor_defecto']
        if ETIQUETA_CRUCE[c['calcula']][2] == ENT:
            esperado = int(round(esperado))
        if not isinstance(v, (int, float)) or abs(v - esperado) > max(1e-9, abs(esperado) * 1e-9):
            fallos.append('%s: Parámetros!B%d = %r y datos_ejemplo dice %r' % (c['x'], fila, v, esperado))
        fc = CUADRE_ROW[c['calcula']]
        rot = wbf[H_PAR]['A%d' % fc].value
        if not (isinstance(rot, str) and rot.startswith('CUADRE')):
            fallos.append('%s: Parámetros!A%d no es una fila de CUADRE' % (c['x'], fc))
        if wbv[H_PAR]['D%d' % fc].value != 'CUADRA':
            fallos.append('%s: con los datos de El Molinete el CUADRE de la fila %d dice %r'
                          % (c['x'], fc, wbv[H_PAR]['D%d' % fc].value))
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
    """Las salidas principales, contra `datos_ejemplo`."""
    pares = [
        ('raciones del año', wbv[H_ANO]['B%d' % W_RANIO].value, D.raciones_anio()),
        ('raciones de julio y agosto', wbv[H_ANO]['B%d' % W_RVER].value, D.raciones_verano()),
        ('días de apertura', wbv[H_ANO]['B%d' % W_DAPER].value, D.dias_apertura_anio()),
        ('horas de refuerzo', wbv[H_REF]['B%d' % R_HTOT].value, D.horas_refuerzo_pico()),
        ('resultado anual de ferias', wbv[H_CAL]['G%d' % L_TOT].value, D.resultado_anual_ferias()),
        ('ferias de julio y agosto', wbv[H_PME]['B%d' % E_FVER].value, D.contribucion_verano('ferias')),
    ]
    for col, s in zip(COLS_SAL, D.SALIDAS_VERANO):
        pares.append(('contribución del verano: %s' % s, wbv[H_VER]['%s%d' % (col, V_CONT)].value,
                      D.contribucion_verano(s)))
    for m in range(1, 13):
        pares.append(('raciones de %s' % D.MESES[m - 1].lower(), wbv[H_ANO]['D%d' % (W_INI + m - 1)].value,
                      D.raciones_mes(m)))
        pares.append(('hora punta del domingo de %s' % D.MESES[m - 1].lower(),
                      wbv[H_COL]['D%d' % (K_INI + m - 1)].value, D.demanda_hora_punta_domingo(m)))
        pares.append(('cola del domingo de %s' % D.MESES[m - 1].lower(),
                      wbv[H_COL]['F%d' % (K_INI + m - 1)].value, D.cola_del_domingo(m)))
    for col, e in zip(COLS_EV, EVENTOS):
        pares.append(('raciones del evento %s' % e['id'], wbv[H_PME]['%s%d' % (col, E_RAC)].value,
                      D.raciones_evento(e)))
        pares.append(('resultado del evento %s' % e['id'], wbv[H_PME]['%s%d' % (col, E_RES)].value,
                      D.resultado_evento(e)))
    for k, fr in enumerate(FRANJAS):
        pares.append(('horas de la franja %s' % fr['clave'], wbv[H_FRA]['B%d' % (F_SINI + k)].value,
                      D.horas_semana_franja(fr['clave'])))
    fallos = ['%s: libro %r, datos_ejemplo %r' % (n, v, e) for n, v, e in pares
              if not isinstance(v, (int, float)) or abs(v - e) > max(1e-9, abs(e) * 1e-9)]
    orden = sorted(((wbv[H_PME]['%s%d' % (col, E_ORDEN)].value, e['id']) for col, e in zip(COLS_EV, EVENTOS)))
    if [i for _o, i in orden] != D.orden_eventos():
        fallos.append('orden de eventos %r frente a datos_ejemplo %r' % (orden, D.orden_eventos()))
    if wbv[H_VER]['B%d' % V_GANA].value != SALIDA_ELEGIDA:
        fallos.append('la salida que más deja es %r y El Molinete elige %r'
                      % (wbv[H_VER]['B%d' % V_GANA].value, SALIDA_ELEGIDA))
    if wbv[H_FRA]['E%d' % F_REP].value != 0:
        fallos.append('hay días cuyo reparto de franjas no suma el 100 %')
    if wbv[H_ANO]['B%d' % W_CHK].value != 'CUADRA':
        fallos.append('los coeficientes no reparten el año')
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

    sin_dv = []
    for ws in wbf.worksheets:
        cubiertas = set()
        for dv in ws.data_validations.dataValidation:
            if not dv.showErrorMessage:
                sin_dv.append('%s: DV sin showErrorMessage (%s)' % (ws.title, dv.sqref))
            if dv.type == 'list' and dv.formula1 and not str(dv.formula1).startswith('$') \
                    and '!' not in str(dv.formula1) and ':' not in str(dv.formula1):
                sin_dv.append('%s: DV de lista que no apunta a un rango (%s)' % (ws.title, dv.formula1))
            for rng in str(dv.sqref).split():
                for fila in ws[rng] if ':' in rng else [[ws[rng]]]:
                    for cel in fila:
                        cubiertas.add(cel.coordinate)
        for row in ws.iter_rows():
            for c in row:
                if (c.__class__.__name__ != 'MergedCell' and motor.es_verde(c)
                        and c.coordinate not in cubiertas
                        and (isinstance(c.value, (int, float)) or c.value in SI_NO + TIPOS_DIA
                             or c.value in SALIDAS)):
                    sin_dv.append('%s!%s verde sin validación' % (ws.title, c.coordinate))
    if sin_dv:
        raise SystemExit('VALIDACIÓN DE DATOS:\n  ' + '\n  '.join(sin_dv))

    _gate_lista_negra(wbf)
    contrato = _gate_cruces(wbf, wbv)
    contra_datos = _gate_contra_datos(wbv)

    requeridos = [i for i, (_t, libros) in D.IDS_LEGALES_REQUERIDOS.items() if LIBRO in libros]
    puestos = set(pid for _h, _c, pid in NOTAS_LEGALES)
    faltan = [i for i in requeridos if i not in puestos]
    if faltan:
        raise SystemExit('Faltan notas legales del libro 5: %s' % ', '.join(faltan))

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

    dic_col = 'F%d' % (K_INI + 11)

    # 1. Más raciones en el día punta (X4, del libro 1): suben las raciones del año (X13) y la
    #    cola del domingo de diciembre, en la proporción que dicta la franja.
    xl = nuevo()
    a0, c0 = ev(xl, H_ANO, 'L5'), ev(xl, H_COL, dic_col)
    pon(xl, H_PAR, 'B%d' % CRUCE_ROW['_raciones_punta'], 480)
    a1, c1 = ev(xl, H_ANO, 'L5'), ev(xl, H_COL, dic_col)
    dpunta = ev(xl, H_ANO, 'B%d' % W_DPUNTA)
    esperado_c1 = 480 * D.COEFICIENTES_MES[11] * 0.5 / 4.0 * D.P('factor_hora_punta') - D.capacidad_raciones_h()
    prueba('480 raciones en el día punta: el año sube %d raciones x 80 y la cola del domingo de '
           'diciembre pasa de %.1f a %.1f raciones/h' % (dpunta, c0, c1),
           abs(a1 - a0 - dpunta * 80) < 1e-6 and abs(c1 - esperado_c1) < 1e-9 and c1 > c0,
           'año %d -> %d' % (a0, a1))

    # 2. Abrir el sábado a las 8:30 en vez de a las 6:00: el semáforo del sábado pasa a
    #    «Cabe también como chocolatería» y la franja de desayuno pierde 2,5 h (X7).
    xl = nuevo()
    s0 = ev(xl, H_FRA, 'E%d' % fila_dia('S'))
    h0 = ev(xl, H_FRA, 'L5')
    n0 = ev(xl, H_FRA, 'E%d' % F_ANTES)
    pon(xl, H_FRA, 'C%d' % fila_franja_dia('S', 0), 8.5)
    s1 = ev(xl, H_FRA, 'E%d' % fila_dia('S'))
    h1 = ev(xl, H_FRA, 'L5')
    n1 = ev(xl, H_FRA, 'E%d' % F_ANTES)
    prueba('abrir el sábado a las 8:30: el semáforo cambia y el desayuno pierde 2,5 h a la semana',
           s0 == TXT_SOLO_CAFE and s1 == TXT_OK_CHOC and abs(h0 - h1 - 2.5) < 1e-9 and n1 == n0 - 1,
           '%r -> %r · %.1f h -> %.1f h · días antes de las 8: %d -> %d' % (s0[:22], s1[:22], h0, h1, n0, n1))

    # 3. Si la carta de verano no abriera el local, deja cero y la que más deja pasa a ser
    #    «Ferias»: el aviso salta y la celda que copia el libro 6 (X16) cae a cero.
    xl = nuevo()
    w0, x0 = ev(xl, H_VER, 'B%d' % V_GANA), ev(xl, H_VER, 'L5')
    ev(xl, H_VER, 'B%d' % V_AVISO)       # pycel sólo recalcula lo que ya está en su mapa
    pon(xl, H_VER, 'C%d' % V_LOCAL, 0)
    w1, x1, av = ev(xl, H_VER, 'B%d' % V_GANA), ev(xl, H_VER, 'L5'), ev(xl, H_VER, 'B%d' % V_AVISO)
    prueba('la carta de verano con el local cerrado: gana «Ferias», el aviso salta y X16 cae a 0',
           w0 == 'Carta de verano' and w1 == 'Ferias' and av == TXT_ELIGE_KO and abs(x0 - D._contribucion_verano_elegida()) < 1e-6
           and abs(x1) < 1e-9, '%r -> %r · X16 %.2f -> %.2f' % (w0, w1, x0, x1))

    # 4. Marcar «Sí» en el mercado navideño (diciembre) lo lleva al año del libro 6 (X14);
    #    marcarlo en la feria de agosto no, porque agosto va en «El Verano».
    xl = nuevo()
    y0 = ev(xl, H_CAL, 'L5')
    col3 = COLS_EV[[e['id'] for e in EVENTOS].index('E3')]
    col1 = COLS_EV[[e['id'] for e in EVENTOS].index('E1')]
    pon(xl, H_PME, '%s%d' % (col1, E_ROW['va']), 'Sí')
    y1 = ev(xl, H_CAL, 'L5')
    pon(xl, H_PME, '%s%d' % (col3, E_ROW['va']), 'Sí')
    y2 = ev(xl, H_CAL, 'L5')
    e3 = [e for e in EVENTOS if e['id'] == 'E3'][0]
    prueba('«Sí» en la feria de agosto no toca X14; «Sí» en el mercado navideño suma lo que deja',
           y0 == 0 and abs(y1) < 1e-9 and abs(y2 - D.resultado_evento(e3)) < 1e-6,
           'X14 %.2f -> %.2f -> %.2f' % (y0, y1, y2))

    # 5. Copiar una capacidad nueva del libro 1 sin anotar lo que publica: el CUADRE avisa, y
    #    con un 10 % más de capacidad la cola de diciembre se cierra.
    xl = nuevo()
    fc = CUADRE_ROW['capacidad_raciones_h']
    q0 = ev(xl, H_PAR, 'D%d' % fc)
    ev(xl, H_COL, dic_col)               # pycel sólo recalcula lo que ya está en su mapa
    pon(xl, H_PAR, 'B%d' % CRUCE_ROW['capacidad_raciones_h'], D.capacidad_raciones_h() * 1.1)
    q1 = ev(xl, H_PAR, 'D%d' % fc)
    c2 = ev(xl, H_COL, dic_col)
    prueba('una capacidad copiada un 10 % más alta: el CUADRE dice REVISA y la cola de diciembre '
           'desaparece', q0 == 'CUADRA' and q1.startswith('REVISA') and c2 == 0,
           '%r -> %r · cola %.2f' % (q0, q1[:12], c2))

    # 6. R-03: el veredicto «¿Una churrera o dos?» sale de la capacidad copiada del libro 1.
    xl = nuevo()
    v0 = ev(xl, H_CAP, 'E%d' % C_S4)
    pon(xl, H_PAR, 'B%d' % CRUCE_ROW['capacidad_raciones_h'], D.capacidad_raciones_h() * 1.2)
    v1 = ev(xl, H_CAP, 'E%d' % C_S4)
    xl = nuevo()
    ev(xl, H_CAP, 'E%d' % C_S4)
    pon(xl, H_PAR, 'B%d' % CRUCE_ROW['capacidad_raciones_h'], D.capacidad_raciones_h() * 0.6)
    v2 = ev(xl, H_CAP, 'E%d' % C_S4)
    prueba('el veredicto «¿Una churrera o dos?»: con la capacidad del ejemplo, una con refuerzo; con '
           'un 20 % más, una basta; con un 40 % menos, más línea',
           v0 == TXT_UNA_REF and v1 == TXT_UNA and v2 == TXT_DOS,
           '%r -> %r · %r' % (v0[:20], v1[:20], v2[:20]))
    return ok, fallos


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
    hoja_anio(wb)
    hoja_franjas(wb)
    hoja_capacidad(wb)
    hoja_cola(wb)
    hoja_refuerzo(wb)
    hoja_verano(wb)
    hoja_punto_muerto(wb)
    hoja_calendario(wb)
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
        print('  origen %-4s %s!%s = %.6f (datos_ejemplo %.6f)' % (x, hoja, celda, v, e))
    print('  contra datos_ejemplo: %d comprobaciones al céntimo, todas en verde' % len(res['contra_datos']))
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
