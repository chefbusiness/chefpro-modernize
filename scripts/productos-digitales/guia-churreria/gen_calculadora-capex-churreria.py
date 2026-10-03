#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_calculadora-capex-churreria.py - libro 2 de «Cómo Montar una
Churrería-Chocolatería» (producto 51, `guia-churreria-chocolateria`; SPEC
`scripts/productos-digitales/guia-churreria-SPEC.md`, §2.1 fila 2, §2.2, §3.1, §3.4 y §3.6).

Molde H: se calca de `guia-chocolateria/gen_calculadora-capex-chocolateria.py` la
estructura de CAPEX por Bloque, Variante del Formato, Traspaso vs Obra Nueva, IVA y
Tesorería y Resumen (SIN la fila del fondo de maniobra y SIN el cruce 2 <- 7 de la
hermana), y de `gen_checklist-equipamiento-y-proveedores-cacao.py` la tabla de
Equipamiento y la de Proveedores (SIN EUDR, cadmio, clientes ni plazo de entrega). Es
NUEVO: Franquicia o Independiente, y los bloques de extracción, fritura y sala. El cierre
(inject_cache + data_only + contrato + mapa + demo con pycel) se calca del libro 1 de
este mismo producto.

Hojas (`datos_ejemplo.HOJAS[2]`): Instrucciones · Parámetros · CAPEX por Bloque ·
Equipamiento Línea a Línea · Variante del Formato · Franquicia o Independiente ·
Traspaso vs Obra Nueva · IVA y Tesorería · Proveedores · Resumen.

CRUCES (D16)
------------
* RECIBE X9 (del libro 1: ¿extinción automática?, 1/0) y X17 (del libro 3: precio del
  aceite €/L y del mix €/kg, base imponible). Tres celdas verdes en «Parámetros», cada
  una con el rótulo literal de `datos_ejemplo.rotulo_cruce()`, su `valor_defecto` y su
  fila de CUADRE con semáforo. Ninguna fórmula entre ficheros.
* ES ORIGEN de X10 (Resumen!L5: CAPEX SIN el fondo de maniobra, que sólo calcula el
  libro 6) y de X18 (Parámetros!L5: la renta mensual, que nace aquí). `cerrar()`
  comprueba que cada una devuelve, a la precisión de la máquina, el `valor_defecto` que
  calcula `datos_ejemplo`.

Lo que NO hay aquí, a propósito: ninguna fila ni bloque del fondo de maniobra de los
primeros meses (D16: vive sólo en el libro 6), ningún plazo de entrega de maquinaria
(sólo en el 7), la rellenadora sin cifra (importe del lector, SR-06), Maestro Churrero
sólo con la inversión de CUS-M14 (SR-20) y el traspaso con sala con el techo de CUS-02
(D15).

Salida: build/calculadora-capex-churreria.xlsx + build/mapa-calculadora-capex-churreria.json.
Uso: /usr/local/bin/python3 gen_calculadora-capex-churreria.py
Via: Claude Code
"""
import datetime
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

LIBRO = 2
FICHERO = D.LIBROS[LIBRO]
NOMBRE = os.path.splitext(FICHERO)[0]
TITULO = 'Calculadora de CAPEX de la Churrería-Chocolatería'
SUBJECT = CC.PRODUCTO + ' · Versión 1.0 · octubre 2026'
assert NOMBRE == 'calculadora-capex-churreria'

(H_INS, H_PAR, H_CAP, H_EQ, H_VAR, H_FRA, H_TRA, H_IVA, H_PRO, H_RES) = D.HOJAS[LIBRO]


def Q(hoja):
    return "'" + hoja + "'!"


def ABS_(hoja, coord):
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
PCT = motor.FMT_PCT
ENT = motor.FMT_ENT
FEC = motor.FMT_FECHA
DEC = '#,##0.00'
DEC1 = '#,##0.0'
DEC3 = '#,##0.000'
M2 = CC.FMT_M2

NOTAS_LEGALES = []
VERDES = []
RECEPTORAS = []      # (hoja, coord del valor, rótulo, cruce)
CUADRES = []         # (hoja, coord)

SI = 'Sí'
NO = 'No'
SI_NO = (SI, NO)
PRESUPUESTO = ('Sí', 'No', 'Por pedir')
UNO_CERO = (1, 0)
CON_IVA_FICHA = 'con IVA en la ficha'
SIN_FUENTE = 'supuesto, sin fecha'


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


def encabezados(ws, fila, cols, alto=42, congelar=True):
    for letra, texto, ancho in cols:
        cel = ws[letra + str(fila)]
        cel.value = texto
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
        raise SystemExit('entrada(%s!%s, «%s») sin valor por defecto' % (ws.title, coord, etiqueta))
    cel = motor.val(ws, coord, valor, fmt=fmt, verde_=True)
    VERDES.append((ws.title, coord, etiqueta, valor))
    return cel


def formula(ws, coord, texto, fmt=None, bold=None, destacar=False):
    cel = motor.f(ws, coord, texto, fmt=fmt, bold=bold)
    if destacar:
        crema(cel)
    return cel


RX_ID = D.RX_ID


def _partes_fuente(fuente):
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
        if url == 'None':
            url = ''
        fiab = str(f.get('fiabilidad') or '').strip()
        partes.append('%s%s%s' % (pid, ' · fiabilidad ' + fiab if fiab else '',
                                  ' · ' + url if url else ''))
    return partes


def comentar(ws, coord, legales=(), fuente=None, extra=None):
    """Una sola nota por celda: la verificación legal de cada id CUN/CHN (`nota_legal`)
    y la procedencia de los ids de sector (CUS/CHS: id, fiabilidad y URL)."""
    if isinstance(legales, str):
        legales = (legales,)
    textos = []
    for pid in legales:
        t = D.nota_legal(pid)
        if not t:
            raise SystemExit('nota_legal(%r) vacía: gate_legal() debería haber abortado' % pid)
        textos.append(t)
        NOTAS_LEGALES.append((ws.title, coord, pid))
    partes = _partes_fuente(fuente)
    if partes:
        textos.append('Fuente: ' + ' | '.join(partes))
    if extra:
        textos.append(extra)
    if not textos:
        return None
    alto = 120 + 60 * len(legales)
    ws[coord].comment = Comment(' || '.join(textos), 'AI Chef Pro', height=alto, width=520)
    return textos


def texto_fuente(fuente):
    if not fuente:
        return ''
    if fuente == 'supuesto':
        return 'supuesto declarado'
    if fuente.startswith('heredado'):
        return 'heredado de la hermana'
    return fuente


def fecha_ficha(fuente):
    """Fecha de consulta de la ficha del primer id CUS de la fuente, o None."""
    for pid in RX_ID.findall(fuente or ''):
        f = D.ficha_comun(pid)
        if f and f.get('fecha_publicacion'):
            try:
                return datetime.datetime.strptime(str(f['fecha_publicacion'])[:10], '%Y-%m-%d')
            except ValueError:
                return None
    return None


def setup(ws, apaisado=True, titulos=None):
    CC.pagina(ws, apaisado=apaisado, titulos=titulos)


def bloque_contrato(ws, filas, titulo='Lo que Copian Otros Libros (No Muevas Estas Celdas)'):
    """El CONTRATO de `datos_ejemplo.CRUCES`: rótulo en K y valor en L desde la fila 5."""
    seccion(ws, 'K4', titulo)
    for fila, rotulo, form, fmt in filas:
        motor.val(ws, 'K%d' % fila, rotulo, wrap=True)
        ws['K%d' % fila].font = Font(bold=True, size=9)
        formula(ws, 'L%d' % fila, form, fmt=fmt, bold=True, destacar=True)
        destinos = []
        for c in D.CRUCES:
            if c['origen'] == LIBRO and c['hoja_origen'] == ws.title and c['celda_origen'] == 'L%d' % fila:
                destinos.append('libro %d (%s, hoja %s, %s)' % (c['receptor'], c['fichero_receptor'],
                                                               c['hoja_receptor'], c['x']))
        if destinos:
            gris(ws, 'M%d' % fila, 'Lo copia: ' + '; '.join(sorted(set(destinos))))
        ws.row_dimensions[fila].height = max(ws.row_dimensions[fila].height or 15, 30)
    ws.column_dimensions['K'].width = max(ws.column_dimensions['K'].width or 0, 40)
    ws.column_dimensions['L'].width = max(ws.column_dimensions['L'].width or 0, 15)
    ws.column_dimensions['M'].width = max(ws.column_dimensions['M'].width or 0, 48)


def listas(ws, fila, defs, col='A'):
    return CC.bloque_listas(ws, fila, defs, col=col)


def dv_si_no(ws, coords, refs, clave, titulo):
    CC.dv_rango(ws, coords, refs[clave], titulo, 'Elige una opción de la lista.')


# ==========================================================================
# Posiciones
# ==========================================================================
# ---- Parámetros ----------------------------------------------------------------
P = {'iva_general': 6, 'iva_compra_alimentos': 7, 'iva_no_lleva': 8,
     'm2_total': 10, 'obra_eur_m2': 11, 'renta_mensual': 12, 'meses_fianza': 13,
     'meses_anio': 15, 'tolerancia_cuadre': 16, 'umbral_desviacion': 17}
P_SEC_IVA, P_SEC_LOCAL, P_SEC_CTRL, P_SEC_CRU = 5, 9, 14, 18
CRUCES_RECIBIDOS = [c for c in D.CRUCES if c['receptor'] == LIBRO]
RX = {}
_r = P_SEC_CRU + 1
for _c in CRUCES_RECIBIDOS:
    RX[_c['n']] = dict(rec=_r, orig=_r + 1, desv=_r + 2, cuad=_r + 3)
    _r += 4
P_LISTAS = _r + 2
_X9 = [c for c in CRUCES_RECIBIDOS if c['x'] == 'X9'][0]
_X17_ACEITE = [c for c in CRUCES_RECIBIDOS if c['x'] == 'X17' and c['calcula'] == 'precio_aceite_eur_l'][0]
_X17_MIX = [c for c in CRUCES_RECIBIDOS if c['x'] == 'X17' and c['calcula'] == 'precio_mix_eur_kg'][0]
_X9B = [c for c in CRUCES_RECIBIDOS if c['x'] == 'X9 bis'][0]       # R-05c: superficie útil (libro 1)
#: R-05b: el precio de cada uno de los otros 12 insumos del stock llega del libro 3.
_X17_INS = dict((c['calcula'][len('_precio_insumo_'):], c) for c in CRUCES_RECIBIDOS
                if c['calcula'].startswith('_precio_insumo_'))
assert sorted(_X17_INS) == sorted(enmiendas_churreria.INSUMOS_STOCK_X17), sorted(_X17_INS)


def PB(clave):
    return ABS_(H_PAR, 'B%d' % P[clave])


X9_CELDA = ABS_(H_PAR, 'B%d' % RX[_X9['n']]['rec'])
ACEITE_CELDA = ABS_(H_PAR, 'B%d' % RX[_X17_ACEITE['n']]['rec'])
MIX_CELDA = ABS_(H_PAR, 'B%d' % RX[_X17_MIX['n']]['rec'])
M2_CELDA = ABS_(H_PAR, 'B%d' % RX[_X9B['n']]['rec'])
INS_CELDA = dict((k, ABS_(H_PAR, 'B%d' % RX[c['n']]['rec'])) for k, c in _X17_INS.items())

# ---- Equipamiento Línea a Línea --------------------------------------------------
EQUIPOS = list(D.EQUIPAMIENTO)
EQ_CAB = 5
EQ_INI = 6
EQ_FIN = EQ_INI + len(EQUIPOS) - 1
EQ_TOT = EQ_FIN + 2
EQ_NUC = EQ_TOT + 1
EQ_DESV = EQ_TOT + 2
EQ_VER = EQ_TOT + 3
EQ_LISTAS = EQ_VER + 3
EQ_ROW = dict((e['clave'], EQ_INI + i) for i, e in enumerate(EQUIPOS))

# ---- CAPEX por Bloque ----------------------------------------------------------
PARTIDAS = list(D.CAPEX_PARTIDAS)
X_CAB = 5
X_INI = 6
X_FIN = X_INI + len(PARTIDAS) - 1
S_SEC = X_FIN + 2
S_CAB = S_SEC + 1
S_INI = S_CAB + 1
S_FIN = S_INI + len(D.STOCK_INICIAL) - 1
S_TOT = S_FIN + 1
B_SEC = S_TOT + 2
B_CAB = B_SEC + 1
B_INI = B_CAB + 1
B_FIN = B_INI + len(D.BLOQUES_CAPEX) - 1
B_TOT = B_FIN + 1
X_LISTAS = B_TOT + 4
BLOQUE_FILA = dict((n, B_INI + i) for i, n in enumerate(sorted(D.BLOQUES_CAPEX)))
CAPEX_TOTAL = ABS_(H_CAP, 'E%d' % B_TOT)


def _fila_partida(prefijo):
    for i, p in enumerate(PARTIDAS):
        if p[1].startswith(prefijo):
            return X_INI + i
    raise KeyError(prefijo)


F_OBRA = _fila_partida('Obra y acondicionamiento')
F_EXT = _fila_partida('Sistema automático de extinción')
F_FIANZA = _fila_partida('Fianza')
F_STOCK = _fila_partida('Stock inicial')

# ---- Variante del Formato ---------------------------------------------------------
V_CAB = 5
V_ORDEN = ('local_con_sala', 'despacho', 'caseta', 'franquicia')
V_ROW = dict((k, V_CAB + 1 + i) for i, k in enumerate(V_ORDEN))
V_SEC_CAS = V_CAB + len(V_ORDEN) + 2
V_ELIGE = V_SEC_CAS + 1
V_CAS_CAB = V_ELIGE + 1
V_CAS_INI = V_CAS_CAB + 1
V_CAS_FIN = V_CAS_INI + len(D.VARIANTES['caseta']['equipos']) - 1
V_SEC_FUERA = V_CAS_FIN + 2
V_FUERA_INI = V_SEC_FUERA + 1
V_LISTAS = V_FUERA_INI + len(D.VARIANTES_FUERA) + 2

# ---- Franquicia o Independiente ---------------------------------------------------
FR_CAB = 5
FR_INI = 6
FR_FIN = FR_INI + len(D.FRANQUICIAS) - 1
FR = dict(capex=FR_FIN + 2, minimo=FR_FIN + 3, maximo=FR_FIN + 4, mediana=FR_FIN + 5,
          debajo=FR_FIN + 6, encima=FR_FIN + 7)

# ---- Traspaso vs Obra Nueva -------------------------------------------------------
T = dict(sec_t=4, cab=5, pedido=6, adapt=7, renta_t=8, parado_t=9, sec_o=10, capex_o=11,
         renta_o=12, meses_o=13, horiz=14, sec_inv=15, inv_t=16, inv_o=17, umbral=18,
         ver_inv=19, sec_h=20, coste_t=21, coste_o=22, dif=23, ver_h=24, sec_tab=26,
         tab_cab=27)
T['tab_ini'] = T['tab_cab'] + 1
T['tab_fin'] = T['tab_ini'] + len(D.TRASPASOS) - 1
T['res'] = T['tab_fin'] + 2
TR_ROW = dict((t['fuente'], T['tab_ini'] + i) for i, t in enumerate(D.TRASPASOS))
MESES_OBRA_NUEVA = (D.ruta_critica()[0] - sum(h[2] for h in D.GANTT if h[0] in ('H1', 'H2')))

# ---- IVA y Tesorería ----------------------------------------------------------
I_CAB = 5
I_INI = 6
I_FIN = I_INI + len(D.BLOQUES_CAPEX) - 1
I_TOT = I_FIN + 1
I = dict(sec_tipo=I_TOT + 2, red=I_TOT + 3, gen=I_TOT + 4, sin=I_TOT + 5,
         sec_caja=I_TOT + 7, base=I_TOT + 8, iva=I_TOT + 9, des=I_TOT + 10, peso=I_TOT + 11)

# ---- Proveedores ----------------------------------------------------------------
PR_CAB = 5
PR_INI = 6
PR_FIN = PR_INI + len(D.PROVEEDORES) - 1
PR_TRABAJA = PR_FIN + 2
PR_PRESUP = PR_FIN + 3
PR_LISTAS = PR_FIN + 7

# ---- Resumen ------------------------------------------------------------------
R_CAB = 5
R_INI = 6


# ==========================================================================
# Hoja «Instrucciones»
# ==========================================================================
PASOS = [
    '1. Hoja «Parámetros». Los tipos de IVA, los metros del local, el coste de obra por '
    'metro, la RENTA MENSUAL (nace aquí: el libro 6 la copia) y los meses de fianza. Abajo, '
    'las celdas verdes que copias de otros libros, cada una con su fila de CUADRE: si '
    'necesitas extinción automática y la superficie útil (del libro 1) y los precios del '
    'aceite, del mix y de los demás insumos del stock (del libro 3).',
    '2. Hoja «Equipamiento Línea a Línea». Cada máquina con su precio de referencia, su '
    'fuente y la fecha en que se leyó. Pon tu mínimo, tu máximo y TU importe, y di si ese '
    'importe lleva IVA: el libro lo pasa a base imponible antes de sumar. «¿La compras?» '
    'decide si entra en el CAPEX.',
    '3. Hoja «CAPEX por Bloque». Lo que no es máquina: la obra, el proyecto, la licencia y '
    'las tasas, la extinción automática si te toca, la fianza, el stock inicial y el '
    'marketing de apertura. Y abajo, los once bloques sumados: equipamiento más partidas.',
    '4. Hoja «Variante del Formato». Local con sala, despacho para llevar, caseta de feria '
    'o franquicia: la dotación con fuente de cada una y lo que cambia frente al local con sala.',
    '5. Hoja «Franquicia o Independiente». Lo que publican las enseñas, fechado y como orden '
    'de magnitud, frente a tu CAPEX. No es una recomendación de marca.',
    '6. Hoja «Traspaso vs Obra Nueva». El precio que te piden por un traspaso y lo que te '
    'costaría adaptarlo, frente a la obra nueva, primero en inversión y después en el '
    'horizonte con la renta.',
    '7. Hoja «IVA y Tesorería». El IVA que adelantas el día que pagas, de qué tipo es y el '
    'desembolso total con IVA.',
    '8. Hoja «Proveedores». Los proveedores con URL comprobada, para pedir presupuestos por '
    'escrito.',
    '9. Hoja «Resumen». Las cifras que llevas al banco y al libro 6. Aquí no se teclea nada.',
]

NOTAS_LIBRO = [
    'ESTE LIBRO SUMA LO QUE CUESTA ABRIR, NO LO QUE CUESTA AGUANTAR. El fondo de maniobra de '
    'los primeros meses no es una partida de este libro: lo calcula el libro 6 con sus '
    'gastos fijos y sus meses de colchón, y le suma este CAPEX. Si lo metieras aquí, el '
    'mismo negocio aparecería con dos inversiones distintas.',
    'TODO SE SUMA EN BASE IMPONIBLE. Unas fichas publican el precio sin IVA y otras con IVA '
    '(el medidor de compuestos polares, por ejemplo). La columna «¿Tu importe lleva IVA?» '
    'existe para que el total no se desvíe un 21 %. El IVA que adelantas va aparte, en «IVA '
    'y Tesorería».',
    'LOS PRECIOS DE MÁQUINA SON DE TIENDA, CON DESCUENTO Y CON FECHA. Los de la tienda de '
    'hostelería llevaban un descuento vigente el día de la lectura: pueden haber cambiado. '
    'La columna de fecha dice cuándo se leyó cada uno. Pide siempre presupuesto por escrito.',
    'LO QUE NO TIENE PRECIO CON FUENTE VA COMO SUPUESTO DECLARADO, Y SE DICE. El conducto a '
    'cubierta, la cafetera, la barra, el mobiliario o la obra por metro son importes de '
    'ejemplo de El Molinete: el que vale es el de tu presupuesto. La rellenadora no tiene '
    'precio con fuente: su importe es el tuyo y El Molinete no la compra (rellena con manga).',
    'UNA REFERENCIA DE CONTRASTE, Y SÓLO UNA. El traspaso de Vallecas de 74 m² (CUS-02) '
    'declara unos 50.000 € de equipos incluidos (freidora, dosificadores, calientachocolates, '
    'cafetera, campana, frío y TPV). Es una declaración del anunciante, con la base de IVA '
    'sin declarar: sirve para ver el orden de magnitud de tus bloques 2 a 7, no para '
    'restarla de nada.',
    'DÓNDE NO ESTÁ LO QUE AQUÍ NO ESTÁ. El plazo de entrega de la maquinaria crítica vive en '
    'el libro 7 (checklist legal y cronograma); el riesgo de incendio y los kW de la cocina, '
    'en el 1; el precio del aceite y del mix, en el 3; los gastos fijos, el fondo de maniobra, '
    'la financiación y el P&L, en el 6. Las franquicias van como orden de magnitud fechado; '
    'los traspasos, como precio PEDIDO, nunca como precio pagado.',
]

CADENCIA = ('Cada cuánto se usa este libro: una vez al preparar el plan, con presupuestos de '
            'verdad, y otra cada vez que firmes un pedido (pon el importe real en «Tu importe» '
            'y mira la desviación). Cuando cambie el CAPEX o la renta del bloque «Lo que Copian '
            'Otros Libros», cópialos de nuevo en el libro 6.')


def _orden_relleno():
    partes = ['%d (%s)' % (n, D.LIBROS[n]) for n in D.ORDEN_RELLENO if n != 7]
    return ('Orden de relleno del paquete: ' + ', luego '.join(partes)
            + '. El libro 7 (%s) no depende de ninguno: rellénalo cuando quieras. Este es el '
              'libro 2 y va el SEXTO: antes, el libro 1 (si necesitas extinción automática) y '
              'el 3 (precio del aceite y del mix); después, el 6, que copia de aquí el CAPEX y '
              'la renta.' % D.LIBROS[7])


def _destinos_texto():
    por_celda = {}
    for c in D.CRUCES:
        if c['origen'] != LIBRO:
            continue
        clave = (c['hoja_origen'], c['celda_origen'])
        por_celda.setdefault(clave, {'concepto': c['concepto'], 'destinos': []})
        por_celda[clave]['destinos'].append('libro %d (%s)' % (c['receptor'], c['x']))
    lineas = []
    for (hoja, celda), d in sorted(por_celda.items(),
                                    key=lambda kv: (D.HOJAS[LIBRO].index(kv[0][0]), int(kv[0][1][1:]))):
        concepto = d['concepto'].replace('SIN fondo de maniobra', 'sin el fondo de maniobra')
        lineas.append('%s!%s - %s. Lo copia: %s.' % (hoja, celda, concepto,
                                                    ', '.join(sorted(set(d['destinos'])))))
    return lineas


def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS, 0)
    ws.column_dimensions['A'].width = 100.0
    cabecera_hoja(ws, TITULO)
    motor.val(ws, 'A3', 'Para qué sirve: saber cuánto necesitas para abrir y en qué formato, '
                        'línea a línea y en base imponible, con el IVA que adelantas aparte. '
                        'Responde a una pregunta: ¿cuánto necesito y en qué formato?')
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
        ws.row_dimensions[fila].height = 46
        fila += 1
    fila += 1
    seccion(ws, 'A%d' % fila, 'Orden de Relleno y Lo que Este Libro Pasa a los Demás')
    fila += 1
    motor.val(ws, 'A%d' % fila, _orden_relleno(), wrap=True)
    ws.row_dimensions[fila].height = 70
    fila += 1
    motor.val(ws, 'A%d' % fila,
              'Ningún libro se vincula con otro por fórmula. Lo que este libro necesita del 1 y '
              'del 3 se copia a mano en las celdas verdes de «Parámetros», y una fila de CUADRE '
              'avisa si se ha quedado vieja. Lo que este libro pasa a los demás está en el '
              'bloque «Lo que Copian Otros Libros» (rótulo en la columna K, valor en la L):',
              wrap=True)
    ws.row_dimensions[fila].height = 44
    fila += 1
    for linea in _destinos_texto():
        motor.val(ws, 'A%d' % fila, linea, wrap=True)
        ws['A%d' % fila].font = Font(size=9)
        ws.row_dimensions[fila].height = 28
        fila += 1
    fila += 1
    seccion(ws, 'A%d' % fila, 'Lo que Conviene Saber Antes de Empezar')
    fila += 1
    for txt in NOTAS_LIBRO:
        motor.val(ws, 'A%d' % fila, txt, wrap=True)
        ws.row_dimensions[fila].height = 62
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, CADENCIA, wrap=True)
    ws.row_dimensions[fila].height = 46
    fila += 2
    motor.val(ws, 'A%d' % fila,
              'Los valores marcados «supuesto declarado» son los de la churrería-chocolatería de '
              'ejemplo «El Molinete» (75 m² con sala, terraza y despacho a calle, obra nueva en '
              'un local sin salida de humos). NO son datos de sector: son un punto de partida '
              'coherente para que veas el libro funcionando antes de meter los tuyos.', wrap=True)
    ws.row_dimensions[fila].height = 46
    fila += 2
    motor.val(ws, 'A%d' % fila, CC.NOTA_DESPROTEGER, wrap=True)
    fila += 2
    motor.val(ws, 'A%d' % fila, CC.BIO, wrap=True)
    fila += 1
    motor.val(ws, 'A%d' % fila, CC.VERSION_LINE)
    ws['A%d' % fila].font = Font(size=8, italic=True)
    setup(ws, apaisado=False)
    return ws


# ==========================================================================
# Hoja «Parámetros»
# ==========================================================================
def fila_param(ws, fila, etiqueta, valor, fmt, unidad, fuente, nota, ids_legales=(),
               pct=False, verde=True):
    motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
    if verde:
        cel = entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
        if pct:
            motor.dv_porcentaje(ws, [cel.coordinate])
        elif isinstance(valor, (int, float)) and not isinstance(valor, bool):
            motor.dv_numerica(ws, [cel.coordinate], minimo=0)
    else:
        cel = motor.val(ws, 'B%d' % fila, valor, fmt=fmt)
    motor.val(ws, 'C%d' % fila, unidad)
    motor.val(ws, 'D%d' % fila, texto_fuente(fuente), wrap=True)
    ws['D%d' % fila].font = Font(size=8, color=GRIS)
    gris(ws, 'E%d' % fila, nota)
    ws.row_dimensions[fila].height = 44
    comentar(ws, cel.coordinate, legales=ids_legales, fuente=fuente)
    return cel


def _bloque_receptor(ws, c, filas, fmt, desc, absoluto=False):
    rot = D.rotulo_cruce(c)
    r = filas['rec']
    motor.val(ws, 'A%d' % r, rot, wrap=True)
    ws['A%d' % r].font = Font(bold=True, size=9)
    entrada(ws, 'B%d' % r, c['valor_defecto'], fmt=fmt, etiqueta='%s %s' % (c['x'], c['concepto']))
    motor.val(ws, 'C%d' % r, c['unidad'])
    motor.val(ws, 'D%d' % r, 'cruce %s (libro %d)' % (c['x'], c['origen']))
    ws['D%d' % r].font = Font(size=8, color=GRIS)
    gris(ws, 'E%d' % r, desc)
    ws.row_dimensions[r].height = 58
    RECEPTORAS.append((H_PAR, 'B%d' % r, rot, c))

    o = filas['orig']
    motor.val(ws, 'A%d' % o, 'Lo que publica hoy esa celda del libro %d (anótalo cada vez que '
                             'lo abras)' % c['origen'], wrap=True)
    entrada(ws, 'B%d' % o, c['valor_defecto'], fmt=fmt,
            etiqueta='%s lo que publica el libro %d' % (c['x'], c['origen']))
    motor.val(ws, 'C%d' % o, c['unidad'])
    gris(ws, 'E%d' % o, 'Si arriba usas otra cifra, la fila de CUADRE te avisa en vez de dejar '
                        'las dos separadas en silencio.')
    ws.row_dimensions[o].height = 36
    d = filas['desv']
    if absoluto:
        motor.val(ws, 'A%d' % d, 'Diferencia entre las dos')
        formula(ws, 'B%d' % d, '=IF(AND(ISNUMBER(B%d),ISNUMBER(B%d)),ABS(B%d-B%d),"")'
                % (r, o, r, o), fmt=ENT)
        cond = 'B%d=0' % d
    else:
        motor.val(ws, 'A%d' % d, 'Desviación entre las dos')
        formula(ws, 'B%d' % d, '=IFERROR(ABS(B%d-B%d)/B%d,"")' % (r, o, o), fmt=PCT)
        motor.semaforo_isnumber(ws, 'B%d' % d, '$B$%d' % d, '>', PB('tolerancia_cuadre'))
        cond = 'B%d<=%s' % (d, PB('tolerancia_cuadre'))
    q = filas['cuad']
    aviso = 'REVISA: no es lo que publica el libro %d' % c['origen']
    motor.val(ws, 'A%d' % q, 'CUADRE: lo que usas frente a lo que publica el libro %d (%s)'
              % (c['origen'], c['concepto'].lower()), wrap=True)
    ws['A%d' % q].font = Font(bold=True)
    formula(ws, 'B%d' % q, '=IF(NOT(ISNUMBER(B%d)),"",IF(%s,"CUADRA","%s"))' % (d, cond, aviso),
            bold=True, destacar=True)
    motor.semaforo_texto(ws, 'B%d' % q, (('CUADRA', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                                         (aviso, motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    ws.row_dimensions[q].height = 34
    CUADRES.append((H_PAR, 'B%d' % q))


def hoja_parametros(wb):
    ws = wb.create_sheet(H_PAR)
    cabecera_hoja(ws, H_PAR, 'Lo que vale para todo el libro. Ninguna fórmula lleva un número '
                             'dentro: los tipos de IVA, los metros, la renta y los umbrales viven aquí.')
    encabezados(ws, 4, [('A', 'Parámetro', 50), ('B', 'Valor', 16), ('C', 'Unidad', 12),
                        ('D', 'Procedencia', 22), ('E', 'Nota', 78)])
    seccion(ws, 'A%d' % P_SEC_IVA, 'El IVA')
    fila_param(ws, P['iva_general'], 'Tipo de IVA general (maquinaria, obra, servicios y envases)',
               D.P('iva_general'), PCT, '%', 'CHN-71c',
               'El equipamiento, la obra, el proyecto y los envases van al tipo general. Lo que '
               'vendes en la carta va a otros tipos: se explica en el capítulo 3 de la guía y lo '
               'aplica el libro 3.', ids_legales=('CHN-71c',), pct=True)
    fila_param(ws, P['iva_compra_alimentos'], 'Tipo de IVA de los alimentos del stock inicial (mix, '
               'aceite, preparado, leche, café...)', D.P('iva_compra_alimentos'), PCT, '%',
               D.PARAMS['iva_compra_alimentos'][1], D.PARAMS['iva_compra_alimentos'][2], pct=True)
    fila_param(ws, P['iva_no_lleva'], 'Tipo de las partidas que no llevan IVA (tasas municipales '
               'y fianza)', 0.0, PCT, '%', 'supuesto',
               'Las tasas del ayuntamiento y la fianza del arrendamiento no llevan IVA: la fianza '
               'es un depósito que se recupera, no una compra.', pct=True)

    seccion(ws, 'A%d' % P_SEC_LOCAL, 'El Local, la Renta y la Obra')
    N = D.NEGOCIO
    fila_param(ws, P['m2_total'], 'Superficie útil del local (copiada del libro 1, más abajo)',
               D.dato(N, 'm2_total'), DEC1, 'm²', N['m2_total'][1],
               'La que copias del libro 1 en la sección «Lo que Copias de Otros Libros» (cruce '
               'X9 bis): la superficie tiene una sola fuente. Aquí sólo sirve para el coste de la '
               'obra por metro.', verde=False)
    formula(ws, 'B%d' % P['m2_total'], '=%s' % M2_CELDA, fmt=DEC1, destacar=True)
    fila_param(ws, P['obra_eur_m2'], 'Coste de obra y acondicionamiento por m² (local en bruto)',
               D.OBRA_EUR_M2[0], EUR, '€/m²', D.OBRA_EUR_M2[1],
               D.OBRA_EUR_M2[2] + ' Supuesto de El Molinete: ninguna ficha publica un coste de '
               'obra por m² de churrería. El conducto a cubierta va en su propia línea.')
    fila_param(ws, P['renta_mensual'], 'Renta mensual del local (nace aquí)',
               D.dato(N, 'renta_mensual'), EUR, '€/mes', N['renta_mensual'][1],
               'La renta del local de 74 m² del traspaso de Vallecas (CUS-02). De aquí sale la '
               'fianza y la copia el libro 6 para sus gastos fijos (bloque de la derecha).')
    fila_param(ws, P['meses_fianza'], 'Meses de fianza y garantía', D.dato(N, 'meses_fianza'),
               ENT, 'meses', N['meses_fianza'][1], N['meses_fianza'][2])

    seccion(ws, 'A%d' % P_SEC_CTRL, 'Controles y Conversiones')
    fila_param(ws, P['meses_anio'], 'Meses que tiene un año', 12, ENT, 'meses', 'conversión',
               'Conversión de unidades. Vive aquí para que ninguna fórmula lleve un número dentro.',
               verde=False)
    fila_param(ws, P['tolerancia_cuadre'], 'Tolerancia de las filas de CUADRE', 0.02, PCT,
               'desviación', 'heredado: guia-chocolateria (Tolerancia de las filas de CUADRE)',
               'Por encima de esta desviación, la fila de CUADRE avisa de que lo que has copiado '
               'ya no es lo que publica el libro de origen.', pct=True)
    fila_param(ws, P['umbral_desviacion'], 'Desviación admitida de tus importes contra la referencia',
               0.10, PCT, 'desviación',
               'heredado: guia-chocolateria/gen_checklist-equipamiento-y-proveedores-cacao.py UMBRAL_DESVIACION',
               'Por encima, la hoja «Equipamiento Línea a Línea» y el «Resumen» avisan: o has '
               'comprado más caro, o has elegido otro equipo. No es un error: es una pregunta.',
               pct=True)

    seccion(ws, 'A%d' % P_SEC_CRU, 'Lo que Copias de Otros Libros')
    _bloque_receptor(ws, _X9, RX[_X9['n']], ENT,
                     '1 si tu cocina pasa de 50 kW computables y la extinción automática es '
                     'obligatoria; 0 si no. El umbral se aplica UNA vez, en el libro 1. Con 1, la '
                     'línea de extinción automática de «CAPEX por Bloque» suma su importe.',
                     absoluto=True)
    _bloque_receptor(ws, _X17_ACEITE, RX[_X17_ACEITE['n']], DEC3,
                     'Precio del aceite de fritura en base imponible. Vive en el libro 3 (celda '
                     'única del paquete): aquí sólo sirve para valorar el stock inicial.')
    _bloque_receptor(ws, _X17_MIX, RX[_X17_MIX['n']], DEC3,
                     'Precio del preparado para masa de churro en base imponible, del libro 3. '
                     'Aquí sólo valora el stock inicial.')
    _bloque_receptor(ws, _X9B, RX[_X9B['n']], DEC1,
                     'La superficie útil del local, del libro 1 (hoja «Zonas y m²»). Mide el '
                     'coste de la obra: obra por metro por metros.')
    for k in enmiendas_churreria.INSUMOS_STOCK_X17:
        c = _X17_INS[k]
        _bloque_receptor(ws, c, RX[c['n']], DEC3,
                         'Precio de «%s» sin IVA, por unidad, del libro 3 (tabla de insumos de su '
                         'hoja «Parámetros»). Aquí sólo valora el stock inicial.'
                         % D.INSUMOS[k]['nombre'])
    refs, _sig = listas(ws, P_LISTAS, [('1 o 0', UNO_CERO)], col='A')
    CC.dv_rango(ws, ['B%d' % RX[_X9['n']]['rec'], 'B%d' % RX[_X9['n']]['orig']], refs['1 o 0'],
                'Extinción automática', 'Escribe 1 (sí) o 0 (no).')
    for c in [_X17_ACEITE, _X17_MIX, _X9B] + [_X17_INS[k] for k in enmiendas_churreria.INSUMOS_STOCK_X17]:
        motor.dv_numerica(ws, ['B%d' % RX[c['n']]['rec'], 'B%d' % RX[c['n']]['orig']], minimo=0)

    bloque_contrato(ws, [(5, 'Renta mensual del local (nace aquí; la copia el libro 6)',
                          '=B%d' % P['renta_mensual'], EUR)])
    setup(ws, titulos='4:4')
    return ws


# ==========================================================================
# Hoja «Equipamiento Línea a Línea»
# ==========================================================================
def hoja_equipamiento(wb):
    ws = wb.create_sheet(H_EQ)
    cabecera_hoja(ws, H_EQ, 'Cada máquina con su fuente, su fecha y su base de IVA. Tu importe se '
                            'pasa a base imponible antes de sumar. Sin plazo de entrega: vive en el libro 7.')
    encabezados(ws, EQ_CAB, [
        ('A', 'Nº', 5), ('B', 'Bloque', 22), ('C', 'Partida', 40), ('D', 'Procedencia', 14),
        ('E', 'Cómo publica la fuente el precio', 18), ('F', 'Fecha del precio', 12),
        ('G', '¿La compras?', 10), ('H', 'Uds', 7), ('I', 'Precio de referencia (ud)', 12),
        ('J', 'Mínimo (ud)', 12), ('K', 'Máximo (ud)', 12), ('L', 'Tu importe (ud)', 12),
        ('M', '¿Tu importe lleva IVA?', 10), ('N', 'Tipo de IVA', 8),
        ('O', 'Base sin IVA', 13), ('P', 'IVA soportado', 12), ('Q', 'Total con IVA', 13),
        ('R', 'Referencia sin IVA (ud)', 12), ('S', 'Referencia de la línea', 13),
        ('T', 'Desviación contra la referencia', 11), ('U', '¿Dentro de tu horquilla?', 13),
        ('V', 'Uds en el local con sala', 9), ('W', 'Uds en el despacho', 9),
        ('X', 'Dotación del local con sala', 12), ('Y', 'Dotación del despacho', 12),
        ('Z', 'Nota', 60)], alto=58)
    v_compra, v_lleva, v_num = [], [], []
    for i, e in enumerate(EQUIPOS):
        r = EQ_INI + i
        motor.val(ws, 'A%d' % r, i + 1, fmt=ENT)
        motor.val(ws, 'B%d' % r, D.BLOQUES_CAPEX[e['bloque']], wrap=True)
        motor.val(ws, 'C%d' % r, e['partida'], wrap=True)
        motor.val(ws, 'D%d' % r, texto_fuente(e['fuente']), wrap=True)
        ws['D%d' % r].font = Font(size=8, color=GRIS)
        base_txt = e['base_iva'] + (' (precio «desde»)' if e['es_desde'] else '')
        motor.val(ws, 'E%d' % r, base_txt, wrap=True)
        fch = fecha_ficha(e['fuente'])
        if fch is not None:
            motor.val(ws, 'F%d' % r, fch, fmt=FEC)
        else:
            motor.val(ws, 'F%d' % r, SIN_FUENTE if e['fuente'] == 'supuesto' else 'sin fecha', wrap=True)
        compra = SI if (e['en_capex'] and e['clave'] != 'rellenadora') else NO
        entrada(ws, 'G%d' % r, compra, etiqueta='¿La compras? ' + e['partida'])
        v_compra.append('G%d' % r)
        entrada(ws, 'H%d' % r, e['uds'], fmt=ENT, etiqueta='Uds ' + e['partida'])
        motor.val(ws, 'I%d' % r, e['precio_fuente'], fmt=EUR)
        for col in ('J', 'K', 'L'):
            entrada(ws, '%s%d' % (col, r), e['precio_fuente'], fmt=EUR,
                    etiqueta='%s %s' % (col, e['partida']))
        v_num += ['H%d' % r, 'J%d' % r, 'K%d' % r, 'L%d' % r]
        lleva = SI if e['base_iva'] == CON_IVA_FICHA else NO
        entrada(ws, 'M%d' % r, lleva, etiqueta='¿Lleva IVA? ' + e['partida'])
        v_lleva.append('M%d' % r)
        formula(ws, 'N%d' % r, '=%s' % PB('iva_general'), fmt=PCT)
        formula(ws, 'O%d' % r, '=IF(G{r}="No","",IFERROR(ROUND(IF(M{r}="Sí",L{r}/(1+N{r}),L{r}),2)*H{r},""))'
                .format(r=r), fmt=EUR)
        formula(ws, 'P%d' % r, '=IF(O{r}="","",O{r}*N{r})'.format(r=r), fmt=EUR)
        formula(ws, 'Q%d' % r, '=IF(O{r}="","",O{r}+P{r})'.format(r=r), fmt=EUR)
        formula(ws, 'R%d' % r, '=IFERROR(ROUND(IF(E{r}="{c}",I{r}/(1+N{r}),I{r}),2),"")'
                .format(r=r, c=CON_IVA_FICHA), fmt=EUR)
        formula(ws, 'S%d' % r, '=IF(OR(G{r}="No",NOT(ISNUMBER(R{r}))),"",R{r}*H{r})'.format(r=r), fmt=EUR)
        formula(ws, 'T%d' % r, '=IF(OR(O{r}="",S{r}=""),"",IF(S{r}=0,"",IFERROR(O{r}/S{r}-1,"")))'
                .format(r=r), fmt=PCT)
        formula(ws, 'U%d' % r, '=IF(G{r}="No","",IF(AND(L{r}>=J{r},L{r}<=K{r}),"Dentro",'
                '"Fuera de tu horquilla"))'.format(r=r))
        motor.val(ws, 'V%d' % r, 1 * e['uds'] if e['en_b'] else 0, fmt=ENT)
        uds_a = (1 if e['clave'] == 'chocolatera_mch5' else e['uds']) if e['en_a'] else 0
        motor.val(ws, 'W%d' % r, uds_a, fmt=ENT)
        formula(ws, 'X%d' % r, '=IF(ISNUMBER(R{r}),R{r}*V{r},"")'.format(r=r), fmt=EUR)
        formula(ws, 'Y%d' % r, '=IF(ISNUMBER(R{r}),R{r}*W{r},"")'.format(r=r), fmt=EUR)
        motor.val(ws, 'Z%d' % r, e['nota'], wrap=True)
        ws.row_dimensions[r].height = 44
        legales = ()
        if e['clave'] == 'extintor_clase_f':
            legales = ('CUN-38',)
        elif e['clave'] == 'conducto_cubierta':
            legales = ('CUN-35',)
        elif e['clave'] == 'freidora_gas_25l':
            legales = ('CUN-26',)
        if e['fuente'] != 'supuesto' or legales:
            comentar(ws, 'Z%d' % r if legales else 'I%d' % r, legales=legales,
                     fuente=None if legales else e['fuente'])
            if legales and e['fuente'] != 'supuesto':
                comentar(ws, 'I%d' % r, fuente=e['fuente'])
    motor.regla_expresion(ws, 'T%d:T%d' % (EQ_INI, EQ_FIN),
                          '=AND(ISNUMBER($T%d),ABS($T%d)>%s)' % (EQ_INI, EQ_INI, PB('umbral_desviacion')),
                          bg=motor.CF_AMBAR_BG, fg=motor.CF_AMBAR_FG)
    motor.semaforo_texto(ws, 'U%d:U%d' % (EQ_INI, EQ_FIN),
                         (('Fuera de tu horquilla', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          ('Dentro', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    motor.dv_numerica(ws, v_num, minimo=0)

    motor.val(ws, 'C%d' % EQ_TOT, 'TOTAL del equipamiento que compras', bold=True)
    for col in ('O', 'P', 'Q', 'S', 'X', 'Y'):
        formula(ws, '%s%d' % (col, EQ_TOT), '=SUM(%s%d:%s%d)' % (col, EQ_INI, col, EQ_FIN),
                fmt=EUR, bold=True, destacar=True)
    motor.val(ws, 'C%d' % EQ_NUC, 'Núcleo con precio de ficha del local con sala, sin el medidor '
                                  'de polares (el que suman las siete líneas de CUS-59)', wrap=True)
    formula(ws, 'X%d' % EQ_NUC, '=IFERROR(X%d-X%d,"")' % (EQ_TOT, EQ_ROW['testo_270']), fmt=EUR, bold=True)
    formula(ws, 'Y%d' % EQ_NUC, '=IFERROR(Y%d-Y%d,"")' % (EQ_TOT, EQ_ROW['testo_270']), fmt=EUR, bold=True)
    ws.row_dimensions[EQ_NUC].height = 34
    motor.val(ws, 'C%d' % EQ_DESV, 'Desviación de tus importes contra la referencia (líneas que compras)',
              wrap=True)
    formula(ws, 'T%d' % EQ_DESV, '=IF(OR(NOT(ISNUMBER(S%d)),S%d=0),"",IFERROR(O%d/S%d-1,""))'
            % (EQ_TOT, EQ_TOT, EQ_TOT, EQ_TOT), fmt=PCT, bold=True)
    motor.val(ws, 'C%d' % EQ_VER, 'VEREDICTO DE LA DESVIACIÓN', bold=True)
    formula(ws, 'T%d' % EQ_VER, '=IF(NOT(ISNUMBER(T%d)),"",IF(ABS(T%d)>%s,"REVISA: te desvías más de '
            'lo admitido","Dentro de lo admitido"))' % (EQ_DESV, EQ_DESV, PB('umbral_desviacion')),
            bold=True, destacar=True)
    motor.semaforo_texto(ws, 'T%d' % EQ_VER,
                         (('REVISA: te desvías más de lo admitido', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          ('Dentro de lo admitido', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    refs, _sig = listas(ws, EQ_LISTAS, [('Sí o No', SI_NO)], col='C')
    dv_si_no(ws, v_compra + v_lleva, refs, 'Sí o No', 'Sí o No')
    CC.parrafo(ws, EQ_LISTAS - 1,
               'Precios de la ficha el 03-10-2026: los descuentos de las tiendas caducan, así que '
               'confirma el precio vigente antes de presupuestar y pon el tuyo en «Tu importe». '
               'La columna «Referencia» es el precio que publica la fuente el día de la fecha, en '
               'base imponible; «Tu importe» es el de TU presupuesto. Las líneas que El Molinete '
               'no compra (el despacho, la freidora eléctrica de la decisión 4, la rellenadora) '
               'están para que cambies «¿La compras?» y veas qué pasa con el CAPEX.',
               col_ini='C', col_fin='Z', alto=40)
    setup(ws, titulos='%d:%d' % (EQ_CAB, EQ_CAB))
    return ws


# ==========================================================================
# Hoja «CAPEX por Bloque»
# ==========================================================================
def hoja_capex(wb):
    ws = wb.create_sheet(H_CAP)
    cabecera_hoja(ws, H_CAP, 'Lo que no es máquina, el stock inicial y los once bloques sumados. '
                             'Sin fondo de maniobra: lo calcula el libro 6.')
    encabezados(ws, X_CAB, [
        ('A', 'Nº', 5), ('B', 'Bloque', 24), ('C', 'Partida', 42), ('D', 'Procedencia', 14),
        ('E', '¿La incluyes?', 10), ('F', 'Mínimo', 13), ('G', 'Máximo', 13),
        ('H', 'Tu importe', 13), ('I', '¿Tu importe lleva IVA?', 10), ('J', 'Tipo de IVA', 9),
        ('K', 'Base sin IVA', 13), ('L', 'IVA soportado', 12), ('M', 'Total con IVA', 13),
        ('N', '¿Se amortiza?', 10), ('O', 'Base amortizable', 13), ('P', 'Nota', 70)], alto=52)
    v_incl, v_lleva, v_num = [], [], []
    for i, p in enumerate(PARTIDAS):
        r = X_INI + i
        bloque, partida, importe, tipo, fuente, amortiza, notatxt = p
        motor.val(ws, 'A%d' % r, i + 1, fmt=ENT)
        motor.val(ws, 'B%d' % r, D.BLOQUES_CAPEX[bloque], wrap=True)
        motor.val(ws, 'C%d' % r, partida, wrap=True)
        motor.val(ws, 'D%d' % r, texto_fuente(fuente), wrap=True)
        ws['D%d' % r].font = Font(size=8, color=GRIS)
        entrada(ws, 'E%d' % r, SI, etiqueta='¿La incluyes? ' + partida)
        v_incl.append('E%d' % r)
        if r == F_OBRA:
            for col in ('F', 'G', 'H'):
                formula(ws, '%s%d' % (col, r), '=%s*%s' % (PB('m2_total'), PB('obra_eur_m2')), fmt=EUR)
        elif r == F_FIANZA:
            for col in ('F', 'G', 'H'):
                formula(ws, '%s%d' % (col, r), '=%s*%s' % (PB('meses_fianza'), PB('renta_mensual')), fmt=EUR)
        elif r == F_STOCK:
            for col in ('F', 'G', 'H'):
                formula(ws, '%s%d' % (col, r), '=I%d' % S_TOT, fmt=EUR)
        else:
            for col in ('F', 'G', 'H'):
                entrada(ws, '%s%d' % (col, r), importe, fmt=EUR, etiqueta='%s %s' % (col, partida))
                v_num.append('%s%d' % (col, r))
        if r == F_STOCK:
            motor.val(ws, 'I%d' % r, 'Por línea, abajo', wrap=True)
            formula(ws, 'J%d' % r, '=IFERROR(J%d/I%d,"")' % (S_TOT, S_TOT), fmt=PCT)
            formula(ws, 'K%d' % r, '=IF(E{r}="No","",H{r})'.format(r=r), fmt=EUR)
            formula(ws, 'L%d' % r, '=IF(K{r}="","",J{s})'.format(r=r, s=S_TOT), fmt=EUR)
        else:
            entrada(ws, 'I%d' % r, NO, etiqueta='¿Lleva IVA? ' + partida)
            v_lleva.append('I%d' % r)
            formula(ws, 'J%d' % r, '=%s' % PB('iva_general' if tipo else 'iva_no_lleva'), fmt=PCT)
            base = 'IFERROR(IF(I{r}="Sí",H{r}/(1+J{r}),H{r}),"")'.format(r=r)
            if r == F_EXT:
                formula(ws, 'K%d' % r, '=IF(E{r}="No","",IF({x}=1,{b},0))'.format(r=r, x=X9_CELDA, b=base),
                        fmt=EUR)
            else:
                formula(ws, 'K%d' % r, '=IF(E{r}="No","",{b})'.format(r=r, b=base), fmt=EUR)
            formula(ws, 'L%d' % r, '=IF(K{r}="","",K{r}*J{r})'.format(r=r), fmt=EUR)
        formula(ws, 'M%d' % r, '=IF(K{r}="","",K{r}+L{r})'.format(r=r), fmt=EUR)
        motor.val(ws, 'N%d' % r, SI if amortiza else NO)
        formula(ws, 'O%d' % r, '=IF(AND(N{r}="Sí",ISNUMBER(K{r})),K{r},"")'.format(r=r), fmt=EUR)
        motor.val(ws, 'P%d' % r, notatxt, wrap=True)
        ws.row_dimensions[r].height = 48
        if r == F_EXT:
            comentar(ws, 'P%d' % r, extra='Suma su importe sólo si la celda del libro 1 copiada en '
                                         '«Parámetros» (cruce X9) vale 1.')
        if r == F_OBRA or partida.startswith('Licencia de obra'):
            comentar(ws, 'C%d' % r, legales=('CUN-35',))
    motor.dv_numerica(ws, v_num, minimo=0)

    # ---- stock inicial ----------------------------------------------------------
    seccion(ws, 'A%d' % S_SEC, 'Stock Inicial y Envase (Bloque 10), Línea a Línea')
    encabezados(ws, S_CAB, [('A', 'Nº', None), ('B', 'Insumo', None), ('C', 'Procedencia del precio', None),
                            ('D', 'Cantidad', None), ('E', 'Unidad', None),
                            ('F', 'Precio por unidad, como lo copias', None),
                            ('G', '¿Lleva IVA?', None), ('H', 'Tipo de IVA', None),
                            ('I', 'Base sin IVA', None), ('J', 'IVA soportado', None),
                            ('K', 'Total con IVA', None), ('L', 'Nota', None)], alto=44, congelar=False)
    for i, (clave, cant) in enumerate(D.STOCK_INICIAL):
        r = S_INI + i
        ins = D.INSUMOS[clave]
        motor.val(ws, 'A%d' % r, i + 1, fmt=ENT)
        motor.val(ws, 'B%d' % r, ins['nombre'], wrap=True)
        entrada(ws, 'D%d' % r, cant, fmt=DEC1, etiqueta='Cantidad de stock ' + ins['nombre'])
        v_num.append('D%d' % r)
        motor.val(ws, 'E%d' % r, ins['unidad'])
        if clave == 'aceite':
            formula(ws, 'F%d' % r, '=%s' % ACEITE_CELDA, fmt=DEC3)
            motor.val(ws, 'C%d' % r, 'cruce X17 (libro 3, celda única del precio del aceite)', wrap=True)
            nota_txt = 'El precio llega del libro 3 por la celda verde de «Parámetros»: no se teclea aquí.'
        elif clave == 'mix_churros':
            formula(ws, 'F%d' % r, '=%s' % MIX_CELDA, fmt=DEC3)
            motor.val(ws, 'C%d' % r, 'cruce X17 (libro 3)', wrap=True)
            nota_txt = 'El precio llega del libro 3 por la celda verde de «Parámetros»: no se teclea aquí.'
        else:
            # R-05b: el precio nace en el libro 3 y llega por su celda verde de «Parámetros»
            formula(ws, 'F%d' % r, '=%s' % INS_CELDA[clave], fmt=DEC3)
            motor.val(ws, 'C%d' % r, 'cruce X17 (libro 3)', wrap=True)
            nota_txt = ('El precio llega del libro 3 por la celda verde de «Parámetros»: no se teclea '
                        'aquí. Base de la fuente: %s.' % ins['base_iva'])
            if ins['nota']:
                nota_txt += ' ' + ins['nota']
        ws['C%d' % r].font = Font(size=8, color=GRIS)
        entrada(ws, 'G%d' % r, NO, etiqueta='¿Lleva IVA? stock ' + ins['nombre'])
        v_lleva.append('G%d' % r)
        tipo = 'iva_compra_alimentos' if clave in D.INSUMOS_ALIMENTO else 'iva_general'
        formula(ws, 'H%d' % r, '=%s' % PB(tipo), fmt=PCT)
        formula(ws, 'I%d' % r, '=IFERROR(IF(G{r}="Sí",D{r}*F{r}/(1+H{r}),D{r}*F{r}),"")'.format(r=r), fmt=EUR)
        formula(ws, 'J%d' % r, '=IF(I{r}="","",I{r}*H{r})'.format(r=r), fmt=EUR)
        formula(ws, 'K%d' % r, '=IF(I{r}="","",I{r}+J{r})'.format(r=r), fmt=EUR)
        motor.val(ws, 'L%d' % r, nota_txt, wrap=True)
        ws.row_dimensions[r].height = 34
        if clave == 'vaso_llevar':
            comentar(ws, 'L%d' % r, legales=('CUN-41',))
        elif ins['fuente'] != 'supuesto':
            comentar(ws, 'F%d' % r, fuente=ins['fuente'])
    motor.val(ws, 'B%d' % S_TOT, 'TOTAL del stock inicial', bold=True)
    for col in ('I', 'J', 'K'):
        formula(ws, '%s%d' % (col, S_TOT), '=SUM(%s%d:%s%d)' % (col, S_INI, col, S_FIN), fmt=EUR,
                bold=True, destacar=True)
    motor.dv_numerica(ws, v_num, minimo=0)

    # ---- resumen por bloque ------------------------------------------------------
    seccion(ws, 'A%d' % B_SEC, 'Los Once Bloques, Equipamiento y Partidas')
    encabezados(ws, B_CAB, [('A', 'Nº', None), ('B', 'Bloque', None), ('C', 'Equipamiento sin IVA', None),
                            ('D', 'Otras partidas sin IVA', None), ('E', 'Base sin IVA', None),
                            ('F', 'IVA soportado', None), ('G', 'Total con IVA', None),
                            ('H', '% del CAPEX', None), ('I', 'Inmovilizado amortizable', None),
                            ('J', 'Procedencia', None)], alto=44, congelar=False)
    eqB = '%s$B$%d:$B$%d' % (Q(H_EQ), EQ_INI, EQ_FIN)
    eqO = '%s$O$%d:$O$%d' % (Q(H_EQ), EQ_INI, EQ_FIN)
    eqP = '%s$P$%d:$P$%d' % (Q(H_EQ), EQ_INI, EQ_FIN)
    procedencia = {
        1: 'supuesto (obra por m²)', 2: 'CUS-36a + supuesto (conducto, CUS-36b sin fuente)',
        3: 'CUS-33a, CUS-34c, CUS-35a, CUS-39', 4: 'CUS-37a + supuesto (cafetera, CUS-43)',
        5: 'supuesto (CUS-43: sin precio con fuente)', 6: 'CUS-38, CUS-41 + supuesto',
        7: 'supuesto', 8: 'supuesto (nunca la horquilla de nuestro post)',
        9: 'meses de fianza por la renta (CUS-02)', 10: 'precios del libro 3 y de las fichas',
        11: 'supuesto'}
    for n in sorted(D.BLOQUES_CAPEX):
        r = BLOQUE_FILA[n]
        motor.val(ws, 'A%d' % r, n, fmt=ENT)
        motor.val(ws, 'B%d' % r, D.BLOQUES_CAPEX[n], wrap=True)
        formula(ws, 'C%d' % r, '=SUMIF(%s,B%d,%s)' % (eqB, r, eqO), fmt=EUR)
        formula(ws, 'D%d' % r, '=SUMIF($B$%d:$B$%d,B%d,$K$%d:$K$%d)' % (X_INI, X_FIN, r, X_INI, X_FIN), fmt=EUR)
        formula(ws, 'E%d' % r, '=C%d+D%d' % (r, r), fmt=EUR, bold=True)
        formula(ws, 'F%d' % r, '=SUMIF(%s,B%d,%s)+SUMIF($B$%d:$B$%d,B%d,$L$%d:$L$%d)'
                % (eqB, r, eqP, X_INI, X_FIN, r, X_INI, X_FIN), fmt=EUR)
        formula(ws, 'G%d' % r, '=E%d+F%d' % (r, r), fmt=EUR)
        formula(ws, 'H%d' % r, '=IFERROR(E%d/$E$%d,"")' % (r, B_TOT), fmt=PCT)
        formula(ws, 'I%d' % r, '=C%d+SUMIF($B$%d:$B$%d,B%d,$O$%d:$O$%d)' % (r, X_INI, X_FIN, r, X_INI, X_FIN),
                fmt=EUR)
        motor.val(ws, 'J%d' % r, procedencia[n], wrap=True)
        ws['J%d' % r].font = Font(size=8, color=GRIS)
        ws.row_dimensions[r].height = 30
    motor.val(ws, 'B%d' % B_TOT, 'CAPEX TOTAL, sin fondo de maniobra', bold=True)
    for col in ('C', 'D', 'E', 'F', 'G', 'H', 'I'):
        formula(ws, '%s%d' % (col, B_TOT), '=SUM(%s%d:%s%d)' % (col, B_INI, col, B_FIN),
                fmt=PCT if col == 'H' else EUR, bold=True, destacar=True)
    motor.val(ws, 'J%d' % B_TOT, 'Viaja al libro 6 desde «Resumen» (L5). El libro 6 le suma el '
                                 'fondo de maniobra de los primeros meses: aquí no está.', wrap=True)
    ws.row_dimensions[B_TOT].height = 44

    refs, _sig = listas(ws, X_LISTAS, [('Sí o No', SI_NO)], col='C')
    dv_si_no(ws, v_incl + v_lleva, refs, 'Sí o No', 'Sí o No')
    CC.parrafo(ws, X_LISTAS - 2,
               'Los importes de obra, proyecto, licencia, tasas y marketing son supuestos de El '
               'Molinete: ninguna ficha publica esas cifras para una churrería, y la horquilla de '
               'licencias que circula por internet no vale para tu ayuntamiento. Pide presupuesto. '
               'La extinción automática suma cero mientras el libro 1 diga que no la necesitas.',
               col_ini='B', col_fin='P', alto=44)
    setup(ws, titulos='%d:%d' % (X_CAB, X_CAB))
    return ws


# ==========================================================================
# Hoja «Variante del Formato»
# ==========================================================================
def hoja_variante(wb):
    ws = wb.create_sheet(H_VAR)
    cabecera_hoja(ws, H_VAR, 'Local con sala, despacho para llevar, caseta de feria o franquicia. Sólo '
                             'el local con sala es caso cifrado; la caseta remite al food truck.')
    encabezados(ws, V_CAB, [('A', 'Variante', 34), ('B', 'm²', 12),
                            ('C', 'Dotación con fuente, sin IVA', 15),
                            ('D', 'Diferencia frente al local con sala', 15),
                            ('E', 'Régimen de apertura', 60), ('F', 'Procedencia', 22),
                            ('G', '¿Caso cifrado?', 10), ('H', 'Remite a', 28), ('I', 'Nota', 50)],
                alto=46)
    sala = V_ROW['local_con_sala']
    for clave in V_ORDEN:
        v = D.VARIANTES[clave]
        r = V_ROW[clave]
        motor.val(ws, 'A%d' % r, v['nombre'], wrap=True)
        motor.val(ws, 'B%d' % r, v['m2'])
        if clave == 'local_con_sala':
            formula(ws, 'C%d' % r, '=%s' % ABS_(H_EQ, 'X%d' % EQ_TOT), fmt=EUR, bold=True)
            formula(ws, 'D%d' % r, '=C%d-$C$%d' % (r, sala), fmt=EUR)
            notatxt = ('Las ocho líneas con precio de ficha (CUS-59) más el medidor de polares. '
                       'Sin la rellenadora, que no tiene cifra con fuente. Es la dotación con '
                       'fuente, no el CAPEX: el CAPEX entero está en «CAPEX por Bloque».')
            legales = ('CHN-49c',)
        elif clave == 'despacho':
            formula(ws, 'C%d' % r, '=%s' % ABS_(H_EQ, 'Y%d' % EQ_TOT), fmt=EUR, bold=True)
            formula(ws, 'D%d' % r, '=C%d-$C$%d' % (r, sala), fmt=EUR)
            notatxt = ('La dotación A (CUS-58): equipo completo Mundigas, caldero, pala, '
                       'escurridor, una chocolatera, campana, balanza y medidor de polares. Sin sala '
                       'te ahorras mobiliario y vajilla, y pierdes la parte de la venta que se '
                       'consume en el local.')
            legales = ('CUN-35', 'CUN-09')
        elif clave == 'caseta':
            formula(ws, 'C%d' % r, '=INDEX($F$%d:$F$%d,$B$%d)' % (V_CAS_INI, V_CAS_FIN, V_ELIGE),
                    fmt=EUR, bold=True)
            formula(ws, 'D%d' % r, '=C%d-$C$%d' % (r, sala), fmt=EUR)
            notatxt = ('El equipo de feria que elijas abajo. Sin caso cifrado (D2): el capítulo y el '
                       'checklist del libro 7 te dicen qué papeles hacen falta; las cuentas de un '
                       'puesto móvil, el plan de negocio del food truck.')
            legales = ('CUN-28', 'CUN-11')
        else:
            motor.val(ws, 'C%d' % r, 'No es una dotación', wrap=True)
            motor.val(ws, 'D%d' % r, 'Ver «Franquicia o Independiente»', wrap=True)
            notatxt = ('La inversión de una franquicia incluye canon, obra y lo que diga cada '
                       'enseña: no se compara con una dotación de máquinas. Va en su hoja, fechada '
                       'y como orden de magnitud.')
            legales = ()
        motor.val(ws, 'E%d' % r, v['regimen'], wrap=True)
        motor.val(ws, 'F%d' % r, v['fuente'], wrap=True)
        ws['F%d' % r].font = Font(size=8, color=GRIS)
        motor.val(ws, 'G%d' % r, SI if v['caso_cifrado'] else NO)
        remite = v.get('remite_a') or ()
        motor.val(ws, 'H%d' % r, ', '.join(remite) if remite else 'esta guía', wrap=True)
        motor.val(ws, 'I%d' % r, notatxt, wrap=True)
        ws.row_dimensions[r].height = 80
        if legales:
            comentar(ws, 'E%d' % r, legales=legales)
        fu = v['fuente']
        if _partes_fuente(fu):
            comentar(ws, 'F%d' % r, fuente=fu)
    comentar(ws, 'A%d' % V_ROW['caseta'], legales=('CUN-13',))

    seccion(ws, 'A%d' % V_SEC_CAS, 'Equipos de Feria (Variante Caseta)')
    motor.val(ws, 'A%d' % V_ELIGE, 'Equipo de feria que miras (1, 2 o 3, por su número de abajo)', wrap=True)
    entrada(ws, 'B%d' % V_ELIGE, 1, fmt=ENT, etiqueta='Equipo de feria elegido')
    encabezados(ws, V_CAS_CAB, [('A', 'Equipo', None), ('B', 'Nº', None), ('C', 'Precio publicado', None),
                                ('D', '¿Lleva IVA?', None), ('E', 'Tipo de IVA', None),
                                ('F', 'Base sin IVA', None), ('G', 'Fecha del precio', None),
                                ('H', 'Procedencia', None)], alto=34, congelar=False)
    v_lleva, v_num = [], []
    fch = fecha_ficha('CUS-42')
    for i, (nombre, precio) in enumerate(D.VARIANTES['caseta']['equipos']):
        r = V_CAS_INI + i
        motor.val(ws, 'A%d' % r, nombre, wrap=True)
        motor.val(ws, 'B%d' % r, i + 1, fmt=ENT)
        entrada(ws, 'C%d' % r, precio, fmt=EUR, etiqueta='Precio ' + nombre)
        v_num.append('C%d' % r)
        entrada(ws, 'D%d' % r, NO, etiqueta='¿Lleva IVA? ' + nombre)
        v_lleva.append('D%d' % r)
        formula(ws, 'E%d' % r, '=%s' % PB('iva_general'), fmt=PCT)
        formula(ws, 'F%d' % r, '=IFERROR(IF(D{r}="Sí",C{r}/(1+E{r}),C{r}),"")'.format(r=r), fmt=EUR)
        if fch is not None:
            motor.val(ws, 'G%d' % r, fch, fmt=FEC)
        motor.val(ws, 'H%d' % r, 'CUS-42 (la tienda publica «Impuestos excluidos»)', wrap=True)
        comentar(ws, 'C%d' % r, fuente='CUS-42')
        ws.row_dimensions[r].height = 30
    motor.dv_numerica(ws, v_num, minimo=0)

    seccion(ws, 'A%d' % V_SEC_FUERA, 'Lo que Queda Fuera del Comparador')
    for i, (formato, texto, remite) in enumerate(D.VARIANTES_FUERA):
        r = V_FUERA_INI + i
        motor.val(ws, 'A%d' % r, formato, wrap=True)
        motor.val(ws, 'E%d' % r, texto, wrap=True)
        motor.val(ws, 'H%d' % r, remite or 'fuera del producto', wrap=True)
        ws.row_dimensions[r].height = 40
        if 'CUN-12' in texto:
            comentar(ws, 'E%d' % r, legales=('CUN-12', 'CUN-30'))

    refs, _sig = listas(ws, V_LISTAS, [('Sí o No', SI_NO), ('Equipo de feria', (1, 2, 3))], col='A')
    dv_si_no(ws, v_lleva, refs, 'Sí o No', 'Sí o No')
    CC.dv_rango(ws, ['B%d' % V_ELIGE], refs['Equipo de feria'], 'Equipo de feria',
                'Escribe 1, 2 o 3.')
    setup(ws, titulos='%d:%d' % (V_CAB, V_CAB))
    return ws


# ==========================================================================
# Hoja «Franquicia o Independiente»
# ==========================================================================
def _base_comparable(f):
    """R-11: ¿la inversión que publica la enseña es total, con obra y equipamiento, y sin IVA aparte?"""
    t = (f['que_incluye'] or '').lower()
    return not any(x in t for x in ('desde', 'más iva', 'sin iva', 'sin la obra', 'existencias'))


def hoja_franquicia(wb):
    ws = wb.create_sheet(H_FRA)
    cabecera_hoja(ws, H_FRA, D.ETIQUETA_FRANQUICIAS)
    encabezados(ws, FR_CAB, [('A', 'Enseña', 24), ('B', 'Inversión publicada', 14),
                             ('C', 'Qué incluye, según la enseña', 46), ('D', 'Canon de entrada', 13),
                             ('E', 'Royalty sobre ventas', 11), ('F', 'Locales', 16),
                             ('G', 'Fuente', 18), ('H', 'Consultado el', 12),
                             ('I', '¿Base comparable con tu CAPEX?', 15),
                             ('J', 'Diferencia frente a tu CAPEX', 15), ('K', 'Nota', 54)], alto=58)
    fch = datetime.datetime.strptime(D.FECHA_DATOS, '%d-%m-%Y')
    comparables = []
    for i, f in enumerate(D.FRANQUICIAS):
        r = FR_INI + i
        motor.val(ws, 'A%d' % r, f['marca'], wrap=True)
        motor.val(ws, 'B%d' % r, f['inversion'], fmt=EUR)
        motor.val(ws, 'C%d' % r, f['que_incluye'], wrap=True)
        if f['canon'] is not None:
            motor.val(ws, 'D%d' % r, f['canon'], fmt=EUR)
        else:
            motor.val(ws, 'D%d' % r, 'no publicado')
        if f['royalty_pct'] is not None:
            motor.val(ws, 'E%d' % r, f['royalty_pct'] / 100.0, fmt=PCT)
        else:
            motor.val(ws, 'E%d' % r, 'no publicado')
        motor.val(ws, 'F%d' % r, f['locales'] or 'no publicado', wrap=True)
        motor.val(ws, 'G%d' % r, f['fuente'], wrap=True)
        motor.val(ws, 'H%d' % r, fch, fmt=FEC)
        # R-11: sólo se resta y se cuenta cuando la enseña publica una inversión TOTAL con obra y
        # equipamiento; «desde», «más IVA», «sin la obra» o «sin fianzas ni existencias» no son
        # la misma base que el CAPEX de la hoja anterior.
        comparables.append(entrada(ws, 'I%d' % r, SI if _base_comparable(f) else NO,
                                   etiqueta='¿Base comparable con tu CAPEX? ' + f['marca']).coordinate)
        formula(ws, 'J%d' % r, '=IF(I%d="%s",IFERROR(B%d-$B$%d,""),"")' % (r, SI, r, FR['capex']), fmt=EUR)
        motor.val(ws, 'K%d' % r, f.get('nota', ''), wrap=True)
        comentar(ws, 'B%d' % r, fuente=f['fuente'])
        ws.row_dimensions[r].height = 34
    filas = [
        (FR['capex'], 'Tu CAPEX, sin fondo de maniobra (de «CAPEX por Bloque»)', '=%s' % CAPEX_TOTAL, EUR),
        (FR['minimo'], 'Inversión publicada más baja', '=IFERROR(MIN(B%d:B%d),"")' % (FR_INI, FR_FIN), EUR),
        (FR['maximo'], 'Inversión publicada más alta', '=IFERROR(MAX(B%d:B%d),"")' % (FR_INI, FR_FIN), EUR),
        (FR['mediana'], 'Enseñas con inversión publicada en la tabla', '=COUNT(B%d:B%d)' % (FR_INI, FR_FIN), ENT),
        (FR['debajo'], 'Enseñas de base comparable que publican una inversión por debajo de tu CAPEX',
         '=SUMPRODUCT(--(I%d:I%d="%s"),--(B%d:B%d<B%d))' % (FR_INI, FR_FIN, SI, FR_INI, FR_FIN,
                                                               FR['capex']), ENT),
        (FR['encima'], 'Enseñas de base comparable que publican una inversión igual o por encima de tu CAPEX',
         '=SUMPRODUCT(--(I%d:I%d="%s"),--(B%d:B%d>=B%d))' % (FR_INI, FR_FIN, SI, FR_INI, FR_FIN,
                                                                FR['capex']), ENT),
    ]
    for r, etq, form, fmt in filas:
        motor.val(ws, 'A%d' % r, etq, wrap=True, bold=True)
        formula(ws, 'B%d' % r, form, fmt=fmt, bold=True, destacar=True)
        ws.row_dimensions[r].height = 30
    CC.parrafo(ws, FR['encima'] + 2,
               'CÓMO LEER ESTA HOJA. Cada enseña dice «inversión» de una manera: con obra o sin '
               'ella, con IVA o sin él, «desde» o total, con el canon dentro o aparte. Por eso no se '
               'suman, no se promedian como si fueran lo mismo y no se recomienda ninguna: son el '
               'orden de magnitud que publica el franquiciador, consultado en la fecha de la columna '
               'H. Tu CAPEX va sin fondo de maniobra y con la obra. Por eso la columna «¿Base comparable '
               'con tu CAPEX?» sólo dice «Sí» donde la enseña publica una inversión total con obra y '
               'equipamiento, y sólo ahí se calcula la diferencia y se cuentan las enseñas por debajo o '
               'por encima; en las «desde», con IVA aparte o sin obra, la comparación sería mezclar '
               'bases. Lo '
               'que la franquicia te da a cambio del canon y del royalty (marca, proveedor, formación '
               'y central de compras) no sale en esta tabla: pregúntalo por escrito y pide el '
               'documento de información precontractual.', col_ini='A', col_fin='K', alto=110)
    CC.parrafo(ws, FR['encima'] + 3,
               'El royalty se paga sobre las ventas de cada mes, también en verano. Con las ventas de '
               'tu libro 6 y el porcentaje de esta tabla sabrás cuánto es al año antes de firmar.',
               col_ini='A', col_fin='K', alto=36)
    refs, _sig = listas(ws, FR['encima'] + 5, [('Sí o No', SI_NO)], col='A')
    dv_si_no(ws, comparables, refs, 'Sí o No', 'Sí o No')
    setup(ws, titulos='%d:%d' % (FR_CAB, FR_CAB))
    return ws


# ==========================================================================
# Hoja «Traspaso vs Obra Nueva»
# ==========================================================================
def hoja_traspaso(wb):
    ws = wb.create_sheet(H_TRA)
    cabecera_hoja(ws, H_TRA, 'El precio de un traspaso es lo que te PIDEN, no lo que se paga. Primero la '
                             'inversión; después, el horizonte con la renta.')
    encabezados(ws, T['cab'], [('A', 'Concepto', 54), ('B', 'Valor', 16), ('C', 'Unidad', 10),
                               ('D', 'Procedencia', 20), ('E', 'Nota', 80)], alto=30)
    seccion(ws, 'A%d' % T['sec_t'], 'El Local que Estás Mirando (Traspaso)')
    vallecas = [t for t in D.TRASPASOS if t['fuente'] == 'CUS-02'][0]
    TA = D.TRASPASO_ALTERNATIVA
    entradas = [
        (T['pedido'], 'Precio de traspaso que te piden', vallecas['precio_pedido'], EUR, '€', 'CUS-02',
         'Sembrado con el traspaso con sala de Vallecas: 74 m², precio PEDIDO y negociable, con '
         'los equipos dentro. Es el techo de los anuncios leídos para un local con sala. Lectura '
         'del 3-oct no reabierta por el captcha: se comprueba antes de publicar la guía.'),
        (T['adapt'], 'Inversión de adaptación que aún tendrías que hacer', D.dato(TA, 'adaptacion'),
         EUR, '€', TA['adaptacion'][1], TA['adaptacion'][2] + ' Supuesto de El Molinete. Pasa el '
         'local por la «Ficha de Visita a Local» del libro 1 antes de fiarte de esta cifra.'),
        (T['renta_t'], 'Renta mensual del local traspasado', D.dato(D.NEGOCIO, 'renta_mensual'), EUR,
         '€/mes', 'CUS-02', 'La del anuncio de Vallecas, la misma que la de El Molinete: por eso, en '
         'este ejemplo, la renta pesa igual en los dos lados.'),
        (T['parado_t'], 'Meses pagando renta sin facturar con el traspaso', D.dato(TA, 'meses_hasta_abrir'),
         ENT, 'meses', TA['meses_hasta_abrir'][1], TA['meses_hasta_abrir'][2]),
        (T['meses_o'], 'Meses pagando renta sin facturar con la obra nueva', MESES_OBRA_NUEVA, DEC1,
         'meses', 'supuesto',
         'De la firma del arrendamiento a la apertura en el cronograma de El Molinete (proyecto, '
         'licencia de obra, obra y conducto, gas, montaje y pruebas). El tuyo sale de la hoja '
         '«Cronograma y Ruta Crítica» del libro 7.'),
        (T['horiz'], 'Horizonte de la comparación', D.P('horizonte_traspaso_anios'), ENT, 'años',
         D.PARAMS['horizonte_traspaso_anios'][1], D.PARAMS['horizonte_traspaso_anios'][2]),
    ]
    v_num = []
    for fila, etq, valor, fmt, unidad, fuente, notatxt in entradas:
        motor.val(ws, 'A%d' % fila, etq, wrap=True)
        cel = entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta=etq)
        v_num.append(cel.coordinate)
        motor.val(ws, 'C%d' % fila, unidad)
        motor.val(ws, 'D%d' % fila, texto_fuente(fuente), wrap=True)
        ws['D%d' % fila].font = Font(size=8, color=GRIS)
        gris(ws, 'E%d' % fila, notatxt)
        ws.row_dimensions[fila].height = 46
        if _partes_fuente(fuente):
            comentar(ws, cel.coordinate, fuente=fuente)
    motor.dv_numerica(ws, v_num, minimo=0)

    seccion(ws, 'A%d' % T['sec_o'], 'La Obra Nueva (El Caso de El Molinete)')
    motor.val(ws, 'A%d' % T['capex_o'], 'CAPEX comparable de la obra nueva (bloques 1 a 8 de «CAPEX por '
                                        'Bloque»)', wrap=True)
    formula(ws, 'B%d' % T['capex_o'], '=SUM(%s$E$%d:$E$%d)' % (Q(H_CAP), BLOQUE_FILA[1], BLOQUE_FILA[8]),
            fmt=EUR, bold=True)
    gris(ws, 'E%d' % T['capex_o'], 'Obra, extracción, maquinaria, barra y sala, control, TPV y '
                                   'licencias. Fuera quedan la fianza, el stock y el marketing, que '
                                   'pagarías igual con un traspaso: sumarlos a un solo lado falsearía '
                                   'la comparación.', alto=46)
    motor.val(ws, 'A%d' % T['renta_o'], 'Renta mensual del local de obra nueva (de «Parámetros»)')
    formula(ws, 'B%d' % T['renta_o'], '=%s' % PB('renta_mensual'), fmt=EUR)

    seccion(ws, 'A%d' % T['sec_inv'], 'La Inversión (Decisión 2)')
    motor.val(ws, 'A%d' % T['inv_t'], 'Traspaso: precio pedido más adaptación')
    formula(ws, 'B%d' % T['inv_t'], '=B%d+B%d' % (T['pedido'], T['adapt']), fmt=EUR, bold=True)
    motor.val(ws, 'A%d' % T['inv_o'], 'Obra nueva: CAPEX comparable')
    formula(ws, 'B%d' % T['inv_o'], '=B%d' % T['capex_o'], fmt=EUR, bold=True)
    motor.val(ws, 'A%d' % T['umbral'], 'Precio de traspaso por debajo del cual gana el traspaso', wrap=True)
    formula(ws, 'B%d' % T['umbral'], '=B%d-B%d' % (T['capex_o'], T['adapt']), fmt=EUR, bold=True, destacar=True)
    gris(ws, 'E%d' % T['umbral'], 'Es la cifra a la que hay que negociar: si el traspaso se cierra por '
                                  'debajo, la inversión sale mejor que la obra nueva.', alto=30)
    motor.val(ws, 'A%d' % T['ver_inv'], 'VEREDICTO DE LA INVERSIÓN', bold=True)
    formula(ws, 'B%d' % T['ver_inv'], '=IF(OR(NOT(ISNUMBER(B%d)),NOT(ISNUMBER(B%d))),"",IF(B%d<B%d,'
            '"Sale mejor el TRASPASO","Sale mejor la OBRA NUEVA"))'
            % (T['inv_t'], T['inv_o'], T['inv_t'], T['inv_o']), bold=True, destacar=True)
    ver_vocab = (('Sale mejor el TRASPASO', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                 ('Sale mejor la OBRA NUEVA', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG))
    motor.semaforo_texto(ws, 'B%d' % T['ver_inv'], ver_vocab)

    seccion(ws, 'A%d' % T['sec_h'], 'En el Horizonte, con la Renta')
    mes = PB('meses_anio')
    filas = [
        (T['coste_t'], 'Coste del traspaso en el horizonte (precio, adaptación, renta y meses parado)',
         '=IFERROR(B{p}+B{a}+B{rt}*{m}*B{h}+B{rt}*B{pt},"")'.format(p=T['pedido'], a=T['adapt'],
                                                                   rt=T['renta_t'], m=mes, h=T['horiz'],
                                                                   pt=T['parado_t'])),
        (T['coste_o'], 'Coste de la obra nueva en el horizonte (CAPEX comparable, renta y meses de obra)',
         '=IFERROR(B{c}+B{ro}*{m}*B{h}+B{ro}*B{mo},"")'.format(c=T['capex_o'], ro=T['renta_o'], m=mes,
                                                              h=T['horiz'], mo=T['meses_o'])),
        (T['dif'], 'Diferencia (traspaso menos obra nueva)',
         '=IFERROR(B%d-B%d,"")' % (T['coste_t'], T['coste_o'])),
    ]
    for r, etq, form in filas:
        motor.val(ws, 'A%d' % r, etq, wrap=True)
        formula(ws, 'B%d' % r, form, fmt=EUR, bold=True)
        ws.row_dimensions[r].height = 30
    motor.val(ws, 'A%d' % T['ver_h'], 'VEREDICTO EN EL HORIZONTE', bold=True)
    formula(ws, 'B%d' % T['ver_h'], '=IF(NOT(ISNUMBER(B%d)),"",IF(B%d<0,"Sale mejor el TRASPASO",'
            '"Sale mejor la OBRA NUEVA"))' % (T['dif'], T['dif']), bold=True, destacar=True)
    motor.semaforo_texto(ws, 'B%d' % T['ver_h'], ver_vocab)
    gris(ws, 'E%d' % T['ver_h'], 'Compara dinero. Un traspaso te da clientela y un local que ya '
                                 'funcionó, y te ata a una distribución que igual no admite el '
                                 'conducto ni la freidora que quieres. Pide los modelos 303 y 390 de '
                                 'los tres últimos años: un traspaso se valora por lo que gana el '
                                 'negocio, no por lo que pide el anuncio.', alto=58)

    seccion(ws, 'A%d' % T['sec_tab'], 'Traspasos Publicados: Precios Pedidos, No Pagados')
    encabezados(ws, T['tab_cab'], [('A', 'Zona', None), ('B', 'Tipo de negocio', None), ('C', 'm²', None),
                                   ('D', 'Precio pedido', None), ('E', 'Nota', None),
                                   ('F', '€ por m²', 12), ('G', 'Fuente', 12), ('H', 'Fiabilidad', 10)],
                alto=30, congelar=False)
    for t in D.TRASPASOS:
        r = TR_ROW[t['fuente']]
        motor.val(ws, 'A%d' % r, t['zona'], wrap=True)
        motor.val(ws, 'B%d' % r, t['tipo'], wrap=True)
        motor.val(ws, 'C%d' % r, t['m2'], fmt=ENT)
        motor.val(ws, 'D%d' % r, t['precio_pedido'], fmt=EUR)
        nota_t = t['nota']
        if t['fuente'] == 'CUS-02':
            nota_t = ('Precio pedido y negociable, con unos 50.000 € de equipos declarados dentro y '
                      'la misma renta que El Molinete. Lectura del 3-oct no reabierta por el captcha: '
                      'se comprueba antes de publicar la guía.')
        motor.val(ws, 'E%d' % r, nota_t, wrap=True)
        formula(ws, 'F%d' % r, '=IFERROR(D%d/C%d,"")' % (r, r), fmt=EUR)
        motor.val(ws, 'G%d' % r, t['fuente'])
        motor.val(ws, 'H%d' % r, t['fiabilidad'])
        comentar(ws, 'D%d' % r, fuente=t['fuente'])
        ws.row_dimensions[r].height = 36

    def celdas(fuentes):
        return ','.join('D%d' % TR_ROW[f] for f in fuentes)
    barrio = ('CUS-31a', 'CUS-31b')
    cafe = ('CUS-31c', 'CUS-31d', 'CUS-31g')
    res = [
        ('Churrería de barrio: precio pedido más bajo', '=MIN(%s)' % celdas(barrio)),
        ('Churrería de barrio: precio pedido más alto', '=MAX(%s)' % celdas(barrio)),
        ('Cafetería-churrería: precio pedido más bajo', '=MIN(%s)' % celdas(cafe)),
        ('Cafetería-churrería: precio pedido más alto', '=MAX(%s)' % celdas(cafe)),
        ('Churrería-chocolatería con sala: techo de los anuncios leídos', '=D%d' % TR_ROW['CUS-02']),
    ]
    T['res_filas'] = {}
    for i, (etq, form) in enumerate(res):
        r = T['res'] + i
        motor.val(ws, 'A%d' % r, etq, bold=True)
        formula(ws, 'D%d' % r, form, fmt=EUR, bold=True, destacar=True)
        T['res_filas'][etq] = r
    CC.parrafo(ws, T['res'] + len(res) + 1,
               'Son precios PEDIDOS en anuncios, no precios pagados: un traspaso se negocia, y '
               'algunos llevan meses sin venderse. Los anuncios que se reeditan durante años no '
               'entran en ningún rango. El techo con sala es el del anuncio de Vallecas, precio '
               'pedido y negociable, con los equipos dentro.',
               col_ini='A', col_fin='H', alto=46)
    setup(ws, titulos='%d:%d' % (T['cab'], T['cab']))
    return ws


# ==========================================================================
# Hoja «IVA y Tesorería»
# ==========================================================================
def hoja_iva(wb):
    ws = wb.create_sheet(H_IVA)
    cabecera_hoja(ws, H_IVA, 'El IVA de la inversión sale de tu bolsillo el día que pagas y vuelve '
                             'después, al ritmo al que factures.')
    encabezados(ws, I_CAB, [('A', 'Bloque', 46), ('B', 'Base sin IVA', 15), ('C', 'IVA soportado', 15),
                            ('D', 'Total con IVA', 15), ('E', 'Nota', 80)], alto=30)
    for n in sorted(D.BLOQUES_CAPEX):
        r = I_INI + n - 1
        b = BLOQUE_FILA[n]
        motor.val(ws, 'A%d' % r, D.BLOQUES_CAPEX[n])
        formula(ws, 'B%d' % r, '=%s' % ABS_(H_CAP, 'E%d' % b), fmt=EUR)
        formula(ws, 'C%d' % r, '=%s' % ABS_(H_CAP, 'F%d' % b), fmt=EUR)
        formula(ws, 'D%d' % r, '=%s' % ABS_(H_CAP, 'G%d' % b), fmt=EUR)
    motor.val(ws, 'A%d' % I_TOT, 'TOTAL', bold=True)
    for col in ('B', 'C', 'D'):
        formula(ws, '%s%d' % (col, I_TOT), '=SUM(%s%d:%s%d)' % (col, I_INI, col, I_FIN), fmt=EUR,
                bold=True, destacar=True)

    seccion(ws, 'A%d' % I['sec_tipo'], 'De Qué Tipo Es el IVA que Adelantas')
    sH = '%s$H$%d:$H$%d' % (Q(H_CAP), S_INI, S_FIN)
    sJ = '%s$J$%d:$J$%d' % (Q(H_CAP), S_INI, S_FIN)
    xJ = '%s$J$%d:$J$%d' % (Q(H_CAP), X_INI, X_FIN)
    xK = '%s$K$%d:$K$%d' % (Q(H_CAP), X_INI, X_FIN)
    motor.val(ws, 'A%d' % I['red'], 'IVA al tipo de los alimentos (el stock de mix, aceite, preparado...)',
              wrap=True)
    formula(ws, 'C%d' % I['red'], '=SUMIF(%s,%s,%s)' % (sH, PB('iva_compra_alimentos'), sJ), fmt=EUR)
    motor.val(ws, 'A%d' % I['gen'], 'IVA al tipo general (maquinaria, obra, servicios y envases)', wrap=True)
    formula(ws, 'C%d' % I['gen'], '=C%d-C%d' % (I_TOT, I['red']), fmt=EUR)
    motor.val(ws, 'A%d' % I['sin'], 'Partidas que no llevan IVA (tasas y fianza), base', wrap=True)
    formula(ws, 'B%d' % I['sin'], '=SUMIF(%s,%s,%s)' % (xJ, PB('iva_no_lleva'), xK), fmt=EUR)
    gris(ws, 'E%d' % I['gen'], 'Casi todo el IVA que adelantas es del tipo general, y lo que vendes '
                               'en la carta va a tipos más bajos: la compensación tarda más de lo que '
                               'parece. Si te inscribes en el registro de devolución mensual, la '
                               'espera se acorta; pregúntaselo a tu asesor.', alto=58)
    comentar(ws, 'A%d' % I['gen'], legales=('CHN-71c',))

    seccion(ws, 'A%d' % I['sec_caja'], 'La Caja del Día que Pagas')
    filas = [
        (I['base'], 'CAPEX sin IVA (los once bloques)', '=B%d' % I_TOT),
        (I['iva'], 'IVA que tienes que adelantar', '=C%d' % I_TOT),
        (I['des'], 'Desembolso total con IVA', '=D%d' % I_TOT),
        (I['peso'], 'Peso del IVA sobre el desembolso', '=IFERROR(C%d/D%d,"")' % (I_TOT, I_TOT)),
    ]
    for r, etq, form in filas:
        motor.val(ws, 'A%d' % r, etq, bold=True)
        formula(ws, 'B%d' % r, form, fmt=PCT if r == I['peso'] else EUR, bold=True, destacar=True)
    gris(ws, 'E%d' % I['des'], 'Lo que sale de la cuenta para abrir, sin contar el fondo de maniobra '
                               'de los primeros meses: ese lo calcula el libro 6 con sus gastos '
                               'fijos, junto con la financiación y la aportación propia.', alto=44)
    setup(ws, apaisado=False, titulos='%d:%d' % (I_CAB, I_CAB))
    return ws


# ==========================================================================
# Hoja «Proveedores»
# ==========================================================================
def hoja_proveedores(wb):
    ws = wb.create_sheet(H_PRO)
    cabecera_hoja(ws, H_PRO, 'Sólo proveedores con URL comprobada. Sin relación comercial: están para '
                             'que pidas presupuesto por escrito.')
    encabezados(ws, PR_CAB, [('A', 'Nº', 5), ('B', 'Proveedor', 32), ('C', 'Qué ofrece', 40),
                             ('D', 'URL', 44), ('E', 'Id', 9), ('F', '¿Trabajas con él?', 11),
                             ('G', '¿Te ha dado presupuesto por escrito?', 13), ('H', 'Nota', 60)], alto=46)
    v_si, v_pres = [], []
    for i, (nombre, que, url, idf, notatxt) in enumerate(D.PROVEEDORES):
        r = PR_INI + i
        motor.val(ws, 'A%d' % r, i + 1, fmt=ENT)
        motor.val(ws, 'B%d' % r, nombre, wrap=True)
        motor.val(ws, 'C%d' % r, que, wrap=True)
        motor.val(ws, 'D%d' % r, url, wrap=True)
        motor.val(ws, 'E%d' % r, idf)
        entrada(ws, 'F%d' % r, NO, etiqueta='¿Trabajas con ' + nombre + '?')
        v_si.append('F%d' % r)
        entrada(ws, 'G%d' % r, 'Por pedir', etiqueta='Presupuesto de ' + nombre)
        v_pres.append('G%d' % r)
        motor.val(ws, 'H%d' % r, notatxt, wrap=True)
        comentar(ws, 'E%d' % r, fuente=idf)
        ws.row_dimensions[r].height = 46
    motor.val(ws, 'B%d' % PR_TRABAJA, 'Proveedores con los que trabajas', bold=True)
    formula(ws, 'F%d' % PR_TRABAJA, '=COUNTIF(F%d:F%d,"Sí")' % (PR_INI, PR_FIN), fmt=ENT, bold=True,
            destacar=True)
    motor.val(ws, 'B%d' % PR_PRESUP, 'Presupuestos por escrito recibidos', bold=True)
    formula(ws, 'G%d' % PR_PRESUP, '=COUNTIF(G%d:G%d,"Sí")' % (PR_INI, PR_FIN), fmt=ENT, bold=True,
            destacar=True)
    CC.parrafo(ws, PR_PRESUP + 2, D.NOTA_PROVEEDORES + ' Para la maquinaria, pide al menos dos '
               'presupuestos por escrito con la base de IVA declarada, y apunta el importe en '
               '«Equipamiento Línea a Línea». El plazo de entrega se anota en el libro 7.',
               col_ini='B', col_fin='H', alto=46)
    refs, _sig = listas(ws, PR_LISTAS, [('Sí o No', SI_NO), ('Presupuesto', PRESUPUESTO)], col='B')
    dv_si_no(ws, v_si, refs, 'Sí o No', '¿Trabajas con él?')
    CC.dv_rango(ws, v_pres, refs['Presupuesto'], 'Presupuesto', 'Elige Sí, No o Por pedir.')
    setup(ws, titulos='%d:%d' % (PR_CAB, PR_CAB))
    return ws


# ==========================================================================
# Hoja «Resumen»
# ==========================================================================
R_FILAS = {}


def hoja_resumen(wb):
    ws = wb.create_sheet(H_RES)
    cabecera_hoja(ws, H_RES, 'Las cifras que llevas al banco y al libro 6. Todas calculadas; aquí no '
                             'se teclea nada.')
    encabezados(ws, R_CAB, [('A', 'Cifra', 56), ('B', 'Valor', 16), ('C', 'De dónde sale', 24),
                            ('D', 'Qué dice', 70)], alto=30)
    filas = []
    for n in sorted(D.BLOQUES_CAPEX):
        filas.append(('Bloque %d. %s' % (n, D.BLOQUES_CAPEX[n]), '=%s' % ABS_(H_CAP, 'E%d' % BLOQUE_FILA[n]),
                      EUR, H_CAP, 'Base sin IVA del bloque.'))
    filas += [
        ('CAPEX TOTAL, sin fondo de maniobra', '=%s' % CAPEX_TOTAL, EUR, H_CAP,
         'LA CIFRA QUE VIAJA AL LIBRO 6 (columna L de esta hoja). El libro 6 le suma el colchón '
         'de caja de los primeros meses, que se calcula allí y sólo allí.'),
        ('IVA soportado que adelantas', '=%s' % ABS_(H_CAP, 'F%d' % B_TOT), EUR, H_CAP,
         'Vuelve al ritmo al que factures, no en una fecha.'),
        ('Desembolso total con IVA', '=%s' % ABS_(H_CAP, 'G%d' % B_TOT), EUR, H_CAP,
         'Lo que sale de la cuenta para abrir.'),
        ('Inmovilizado amortizable', '=%s' % ABS_(H_CAP, 'I%d' % B_TOT), EUR, H_CAP,
         'Máquinas, obra, proyecto y licencias. La fianza (se recupera), el stock (existencias) y '
         'el marketing (gasto del primer año) no se amortizan.'),
        ('No amortizable (fianza, stock inicial y marketing)',
         '=%s-%s' % (CAPEX_TOTAL, ABS_(H_CAP, 'I%d' % B_TOT)), EUR, H_CAP, ''),
        ('Equipamiento y mobiliario (bloques 2 a 7)',
         '=SUM(%s$E$%d:$E$%d)' % (Q(H_CAP), BLOQUE_FILA[2], BLOQUE_FILA[7]), EUR, H_CAP,
         'Lo que se puede poner al lado de los ~50.000 € de equipos que declara el traspaso de '
         'Vallecas, sólo como orden de magnitud (base de IVA sin declarar).'),
        ('Dotación con fuente del local con sala (con el medidor de polares)',
         '=%s' % ABS_(H_EQ, 'X%d' % EQ_TOT), EUR, H_EQ,
         'Las ocho líneas con precio de ficha, sin la rellenadora.'),
        ('Dotación con fuente del despacho (con el medidor de polares)',
         '=%s' % ABS_(H_EQ, 'Y%d' % EQ_TOT), EUR, H_EQ, 'La variante (b), sin sala.'),
        ('Desviación de tus importes contra la referencia', '=%s' % ABS_(H_EQ, 'T%d' % EQ_DESV), PCT, H_EQ,
         'Cero mientras uses los precios de referencia. Cuando metas tus presupuestos, te dice '
         'cuánto te has movido.'),
        ('Veredicto de la desviación', '=%s' % ABS_(H_EQ, 'T%d' % EQ_VER), None, H_EQ, ''),
        ('¿Necesitas extinción automática? (1 sí, 0 no; del libro 1)', '=%s' % X9_CELDA, ENT, H_PAR,
         'Con 1, la línea de extinción automática suma su importe en el bloque 8.'),
        ('Traspaso u obra nueva: veredicto de la inversión', '=%s' % ABS_(H_TRA, 'B%d' % T['ver_inv']),
         None, H_TRA, 'Compara dinero; la clientela y la distribución del local no salen en esta celda.'),
        ('Precio de traspaso por debajo del cual gana el traspaso', '=%s' % ABS_(H_TRA, 'B%d' % T['umbral']),
         EUR, H_TRA, 'La cifra a la que hay que negociar.'),
        ('Despacho frente al local con sala: diferencia de dotación',
         '=%s' % ABS_(H_VAR, 'D%d' % V_ROW['despacho']), EUR, H_VAR, ''),
        ('Franquicias de base comparable que publican una inversión por debajo de tu CAPEX',
         '=%s' % ABS_(H_FRA, 'B%d' % FR['debajo']), ENT, H_FRA, 'Orden de magnitud, no recomendación.'),
    ]
    for c in CRUCES_RECIBIDOS:
        filas.append(('Cuadre del cruce %s (%s)' % (c['x'], c['concepto'].lower()),
                      '=%s' % ABS_(H_PAR, 'B%d' % RX[c['n']]['cuad']), None, H_PAR,
                      'Si no dice CUADRA, has copiado una cifra que el libro %d ya no publica.' % c['origen']))
    fila = R_INI
    for etq, form, fmt, hoja, notatxt in filas:
        R_FILAS[etq] = fila
        motor.val(ws, 'A%d' % fila, etq, wrap=True)
        formula(ws, 'B%d' % fila, form, fmt=fmt)
        motor.val(ws, 'C%d' % fila, hoja)
        motor.val(ws, 'D%d' % fila, notatxt, wrap=True)
        ws.row_dimensions[fila].height = 30
        fila += 1
    crema(ws['B%d' % R_FILAS['CAPEX TOTAL, sin fondo de maniobra']])
    ws['A%d' % R_FILAS['CAPEX TOTAL, sin fondo de maniobra']].font = Font(bold=True)
    CC.parrafo(ws, fila + 1,
               'Si alguna de estas cifras no te cuadra, no la cambies aquí: esta hoja no tiene ni una '
               'celda editable. Vuelve a la hoja donde nace y cambia el importe o el parámetro.',
               col_ini='A', col_fin='D', alto=34)
    bloque_contrato(ws, [
        (5, 'CAPEX de apertura, sin el fondo de maniobra (lo suma el libro 6)', '=%s' % CAPEX_TOTAL, EUR),
        (6, 'CAPEX que no se amortiza (fianza, stock inicial y marketing)',
         '=%s-%s' % (CAPEX_TOTAL, ABS_(H_CAP, 'I%d' % B_TOT)), EUR),
    ])
    setup(ws, apaisado=False, titulos='%d:%d' % (R_CAB, R_CAB))
    return ws


# ==========================================================================
# Mapa de celdas
# ==========================================================================
def mapa_celdas():
    m = [
        # --- las celdas del contrato (origen de X10 y X18)
        ('CAPEX de apertura sin fondo de maniobra (origen de X10)', H_RES, 'L5', 'salida'),
        ('CAPEX que no se amortiza: fianza, stock inicial y marketing (origen de X10 bis)', H_RES, 'L6', 'salida'),
        ('Renta mensual del local (origen de X18)', H_PAR, 'L5', 'salida'),
        # --- cruces recibidos
        ('¿Necesitas extinción automática? copiado del libro 1 (X9)', H_PAR, 'B%d' % RX[_X9['n']]['rec'], 'entrada'),
        ('Cuadre de la extinción automática con el libro 1', H_PAR, 'B%d' % RX[_X9['n']]['cuad'], 'salida'),
        ('Precio del aceite copiado del libro 3 (X17)', H_PAR, 'B%d' % RX[_X17_ACEITE['n']]['rec'], 'entrada'),
        ('Cuadre del precio del aceite con el libro 3', H_PAR, 'B%d' % RX[_X17_ACEITE['n']]['cuad'], 'salida'),
        ('Precio del mix copiado del libro 3 (X17)', H_PAR, 'B%d' % RX[_X17_MIX['n']]['rec'], 'entrada'),
        ('Cuadre del precio del mix con el libro 3', H_PAR, 'B%d' % RX[_X17_MIX['n']]['cuad'], 'salida'),
        # --- parámetros
        ('Tipo de IVA general', H_PAR, 'B%d' % P['iva_general'], 'parametro'),
        ('Tipo de IVA de los alimentos del stock', H_PAR, 'B%d' % P['iva_compra_alimentos'], 'parametro'),
        ('Superficie útil del local', H_PAR, 'B%d' % P['m2_total'], 'parametro'),
        ('Coste de obra por m²', H_PAR, 'B%d' % P['obra_eur_m2'], 'parametro'),
        ('Renta mensual del local', H_PAR, 'B%d' % P['renta_mensual'], 'parametro'),
        ('Meses de fianza', H_PAR, 'B%d' % P['meses_fianza'], 'parametro'),
        ('Desviación admitida contra la referencia', H_PAR, 'B%d' % P['umbral_desviacion'], 'parametro'),
        # --- CAPEX
        ('CAPEX total sin fondo de maniobra', H_CAP, 'E%d' % B_TOT, 'salida'),
        ('IVA soportado del CAPEX', H_CAP, 'F%d' % B_TOT, 'salida'),
        ('Desembolso total con IVA', H_CAP, 'G%d' % B_TOT, 'salida'),
        ('Inmovilizado amortizable', H_CAP, 'I%d' % B_TOT, 'salida'),
        ('Stock inicial sin IVA', H_CAP, 'I%d' % S_TOT, 'salida'),
        ('Obra y acondicionamiento del local', H_CAP, 'K%d' % F_OBRA, 'salida'),
        ('Fianza y garantías', H_CAP, 'K%d' % F_FIANZA, 'salida'),
        ('Sistema automático de extinción (sólo si X9 = 1)', H_CAP, 'K%d' % F_EXT, 'salida'),
        ('Importe de la extinción automática si te toca', H_CAP, 'H%d' % F_EXT, 'entrada'),
    ]
    for n in sorted(D.BLOQUES_CAPEX):
        m.append(('Bloque %d: %s' % (n, D.BLOQUES_CAPEX[n]), H_CAP, 'E%d' % BLOQUE_FILA[n], 'salida'))
    m += [
        # --- equipamiento
        ('Dotación con fuente del local con sala, con el medidor de polares', H_EQ, 'X%d' % EQ_TOT, 'salida'),
        ('Núcleo con precio de ficha del local con sala', H_EQ, 'X%d' % EQ_NUC, 'salida'),
        ('Dotación con fuente del despacho, con el medidor de polares', H_EQ, 'Y%d' % EQ_TOT, 'salida'),
        ('Núcleo con precio de ficha del despacho', H_EQ, 'Y%d' % EQ_NUC, 'salida'),
        ('Freidora de gas de 25 L, tu importe', H_EQ, 'L%d' % EQ_ROW['freidora_gas_25l'], 'entrada'),
        ('Medidor de polares, base sin IVA', H_EQ, 'O%d' % EQ_ROW['testo_270'], 'salida'),
        ('Freidora eléctrica de 25 L, referencia sin IVA', H_EQ, 'R%d' % EQ_ROW['freidora_electrica_25l'], 'salida'),
        ('Rellenadora, importe del lector', H_EQ, 'L%d' % EQ_ROW['rellenadora'], 'entrada'),
        ('Conducto a cubierta, obra y proyecto', H_EQ, 'L%d' % EQ_ROW['conducto_cubierta'], 'entrada'),
        ('Desviación de tus importes contra la referencia', H_EQ, 'T%d' % EQ_DESV, 'salida'),
        # --- variante
        ('Diferencia de dotación del despacho frente al local con sala', H_VAR, 'D%d' % V_ROW['despacho'], 'salida'),
        ('Dotación de la caseta (equipo de feria elegido)', H_VAR, 'C%d' % V_ROW['caseta'], 'salida'),
        # --- franquicia
        ('Inversión publicada de Maestro Churrero (CUS-M14)', H_FRA,
         'B%d' % (FR_INI + [f['marca'] for f in D.FRANQUICIAS].index('Maestro Churrero')), 'salida'),
        ('Franquicias: inversión publicada más baja', H_FRA, 'B%d' % FR['minimo'], 'salida'),
        ('Franquicias: inversión publicada más alta', H_FRA, 'B%d' % FR['maximo'], 'salida'),
        ('Franquicias: enseñas con inversión publicada', H_FRA, 'B%d' % FR['mediana'], 'salida'),
        ('Franquicias de base comparable por debajo de tu CAPEX', H_FRA, 'B%d' % FR['debajo'], 'salida'),
        # --- traspaso
        ('Precio de traspaso pedido (techo con sala, CUS-02)', H_TRA, 'B%d' % T['pedido'], 'entrada'),
        ('Inversión del traspaso (precio más adaptación)', H_TRA, 'B%d' % T['inv_t'], 'salida'),
        ('CAPEX comparable de la obra nueva (bloques 1 a 8)', H_TRA, 'B%d' % T['capex_o'], 'salida'),
        ('Precio de traspaso por debajo del cual gana el traspaso', H_TRA, 'B%d' % T['umbral'], 'salida'),
        ('Veredicto de la inversión: traspaso u obra nueva', H_TRA, 'B%d' % T['ver_inv'], 'salida'),
        ('Coste del traspaso en el horizonte', H_TRA, 'B%d' % T['coste_t'], 'salida'),
        ('Coste de la obra nueva en el horizonte', H_TRA, 'B%d' % T['coste_o'], 'salida'),
        ('Veredicto en el horizonte', H_TRA, 'B%d' % T['ver_h'], 'salida'),
        ('Traspasos de barrio: más bajo', H_TRA, 'D%d' % T['res_filas']['Churrería de barrio: precio pedido más bajo'], 'salida'),
        ('Traspasos de barrio: más alto', H_TRA, 'D%d' % T['res_filas']['Churrería de barrio: precio pedido más alto'], 'salida'),
        ('Traspasos de cafetería-churrería: más bajo', H_TRA, 'D%d' % T['res_filas']['Cafetería-churrería: precio pedido más bajo'], 'salida'),
        ('Traspasos de cafetería-churrería: más alto', H_TRA, 'D%d' % T['res_filas']['Cafetería-churrería: precio pedido más alto'], 'salida'),
        # --- IVA
        ('IVA al tipo de los alimentos (stock)', H_IVA, 'C%d' % I['red'], 'salida'),
        ('IVA al tipo general', H_IVA, 'C%d' % I['gen'], 'salida'),
        ('Peso del IVA sobre el desembolso', H_IVA, 'B%d' % I['peso'], 'salida'),
    ]
    return m


# ==========================================================================
# Cierre
# ==========================================================================
_PROHIBIDAS = ('INDIRECT', 'COUNTA', 'PMT(', 'OFFSET', 'XLOOKUP', 'LET(', 'LAMBDA', 'RANK(',
               'NETWORKDAYS', 'IRR(')
RX_CONST_DEC = re.compile(r'[*/]\s*\d{1,3}[.,]\d{1,4}(?!\d)')
RX_CONST_ENT = re.compile(r'[*/+\-<>=]\s*(\d+)(?![\d.,]*["!])')


def _textos(wbf):
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                if isinstance(c.value, str):
                    yield ws.title, c.coordinate, c.value
                if c.comment is not None:
                    yield ws.title, c.coordinate + ' (nota)', c.comment.text


def _gate_lista_negra(wbf):
    fallos = []
    rotulos_ok = set((h, 'A' + c[1:]) for h, c, _r, _x in RECEPTORAS)
    for hoja, coord, texto in _textos(wbf):
        donde = '%s!%s' % (hoja, coord)
        bajo = texto.lower()
        for aguja, motivo in D.LISTA_NEGRA:
            if aguja.startswith('re:'):
                if re.search(aguja[3:], bajo):
                    fallos.append('%s: /%s/ (%s)' % (donde, aguja[3:], motivo))
            elif aguja.lower() in bajo:
                fallos.append('%s: «%s» (%s)' % (donde, aguja, motivo))
        for pid in RX_ID.findall(texto):
            if pid in D.IDS_PROHIBIDOS:
                fallos.append('%s: id prohibido %s' % (donde, pid))
        for frase in ('cópialo del libro', 'trae aquí la cifra de'):
            if frase in bajo and (hoja, coord) not in rotulos_ok:
                fallos.append('%s: «%s» fuera de las celdas declaradas en CRUCES' % (donde, frase))
        if '0,50 m' in texto and '1,20 m' not in texto:
            fallos.append('%s: filtros a 0,50 m sin los 1,20 m de gas o parrilla (A5)' % donde)
        if re.search(r'\bpor declaración responsable\b', bajo) and 'obra' not in bajo:
            fallos.append('%s: declaración responsable sin la condición de obra (A4)' % donde)
        # Libro 2: ninguna fila ni bloque del fondo de maniobra (D16), sin plazo de entrega,
        # traspasos sólo con el techo de CUS-02, Maestro Churrero sólo con CUS-M14.
        # R-22: lo que se veta son las FILAS y los BLOQUES que lo calculan (un rótulo que EMPIEZA por
        # «fondo de maniobra»); decir que lo suma el libro 6 es lo que hay que decir.
        if re.match(r'\s*fondo de maniobra', bajo) and not coord.endswith('(nota)'):
            fallos.append('%s: una fila o bloque «fondo de maniobra» en el libro 2 (vive sólo en el 6, D16)' % donde)
        if re.search(r'plazo de entrega', bajo) and 'libro 7' not in bajo:
            fallos.append('%s: plazo de entrega fuera del libro 7' % donde)
    if fallos:
        raise SystemExit('LISTA NEGRA en %s:\n  %s' % (NOMBRE, '\n  '.join(fallos[:40])))


def _gate_numeros_vetados(wbv):
    """Ningún NÚMERO de traspaso vetado (D15) y ningún 75.000 junto a Maestro Churrero."""
    fallos = []
    for ws in wbv.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, (int, float)) and not isinstance(c.value, bool):
                    if c.value in (95000, 107000, 120000):
                        fallos.append('%s!%s = %r (D15)' % (ws.title, c.coordinate, c.value))
    hoja = wbv[H_FRA]
    for r in range(FR_INI, FR_FIN + 1):
        if hoja['A%d' % r].value == 'Maestro Churrero' and hoja['B%d' % r].value != 115000:
            fallos.append('Maestro Churrero con %r: sólo los 115.000 € de CUS-M14' % hoja['B%d' % r].value)
    if fallos:
        raise SystemExit('NÚMEROS VETADOS en %s:\n  %s' % (NOMBRE, '\n  '.join(fallos)))


def _gate_contrato(wbv):
    if D._ERROR_CRUCES:
        raise SystemExit('datos_ejemplo no pudo calcular los cruces: %s' % D._ERROR_CRUCES)
    fallos, filas = [], []
    for c in D.CRUCES:
        if c['origen'] != LIBRO:
            continue
        hoja, celda = c['hoja_origen'], c['celda_origen']
        if not re.match(r'^L\d+$', celda) or int(celda[1:]) < 5:
            fallos.append('%s: la celda de origen %s no está en la L desde la fila 5' % (c['x'], celda))
            continue
        rot = wbv[hoja]['K' + celda[1:]].value
        if not isinstance(rot, str) or not rot.strip():
            fallos.append('%s: %s!K%s sin rótulo' % (c['x'], hoja, celda[1:]))
        v = wbv[hoja][celda].value
        e = c['valor_defecto']
        if not isinstance(v, (int, float)) or abs(v - e) > max(1e-9, abs(e) * 1e-9):
            fallos.append('%s: %s!%s = %r y datos_ejemplo dice %r (%s)' % (c['x'], hoja, celda, v, e,
                                                                        c['concepto']))
        filas.append((c['x'], hoja, celda, v, e))
    if fallos:
        raise SystemExit('CONTRATO DE CRUCES ROTO en %s:\n  %s' % (NOMBRE, '\n  '.join(fallos)))
    return filas


def _gate_receptor(wbf, wbv):
    esperados = [c for c in D.CRUCES if c['receptor'] == LIBRO]
    if len(RECEPTORAS) != len(esperados) or len(CUADRES) != len(esperados):
        raise SystemExit('Receptoras %d, CUADRES %d y CRUCES con receptor 2: %d'
                         % (len(RECEPTORAS), len(CUADRES), len(esperados)))
    n_rot = 0
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and 'cópialo del libro' in c.value.lower():
                    n_rot += 1
    if n_rot != len(esperados):
        raise SystemExit('Rótulos «cópialo del libro» en el libro: %d; CRUCES declara %d' % (n_rot, len(esperados)))
    for (hoja, coord, rot, c), (hc, cc) in zip(RECEPTORAS, CUADRES):
        cel = wbf[hoja][coord]
        if not motor.es_verde(cel) or cel.protection.locked:
            raise SystemExit('%s!%s (cruce %s) no es verde editable' % (hoja, coord, c['x']))
        if wbf[hoja]['A' + coord[1:]].value != D.rotulo_cruce(c):
            raise SystemExit('%s!A%s no lleva el rótulo literal de CRUCES' % (hoja, coord[1:]))
        if abs(wbv[hoja][coord].value - c['valor_defecto']) > 1e-12:
            raise SystemExit('%s!%s no nace con el valor_defecto de CRUCES' % (hoja, coord))
        if hc != hoja or not str(wbf[hoja]['A' + cc[1:]].value).startswith('CUADRE'):
            raise SystemExit('El cruce %s no tiene su fila de CUADRE en %s' % (c['x'], hoja))
        if wbv[hc][cc].value != 'CUADRA':
            raise SystemExit('La fila de CUADRE %s!%s no cuadra con los valores por defecto' % (hc, cc))


def _cerca(a, b, tol=1e-6):
    return isinstance(a, (int, float)) and abs(a - b) <= max(tol, abs(b) * 1e-9)


def cerrar(wb):
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
    ruta = os.path.join(destino, FICHERO)
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
        sin_ref = re.sub(r"'[^']*'!", '', sin_texto)
        sin_ref = re.sub(r'\$?[A-Z]{1,2}\$?\d+', '', sin_ref)
        for m in RX_CONST_DEC.finditer(sin_ref):
            problemas.append('%s!%s constante tecleada %s' % (hoja, coord, m.group(0)))
        for m in RX_CONST_ENT.finditer(sin_ref):
            if m.group(1) not in ('0', '1', '2'):
                problemas.append('%s!%s constante entera %s en %s' % (hoja, coord, m.group(1), form[:80]))
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
    if verdes_vacias:
        raise SystemExit('CELDAS VERDES VACÍAS O BLOQUEADAS:\n  ' + ', '.join(verdes_vacias))

    _gate_lista_negra(wbf)
    _gate_numeros_vetados(wbv)
    contrato = _gate_contrato(wbv)
    _gate_receptor(wbf, wbv)

    requeridos = [i for i, (_t, libros) in D.IDS_LEGALES_REQUERIDOS.items() if LIBRO in libros]
    puestos = set(pid for _h, _c, pid in NOTAS_LEGALES)
    faltan = [i for i in requeridos if i not in puestos]
    if faltan:
        raise SystemExit('Faltan notas legales del libro 2: %s' % ', '.join(faltan))

    # Comprobaciones del caso contra datos_ejemplo (no sólo el contrato).
    vc = wbv[H_CAP]
    chequeos = [('CAPEX total', vc['E%d' % B_TOT].value, D.capex_total()),
                ('IVA soportado', vc['F%d' % B_TOT].value, D.iva_soportado_capex()),
                ('inmovilizado amortizable', vc['I%d' % B_TOT].value, D.capex_amortizable()),
                ('stock inicial', vc['I%d' % S_TOT].value, D.stock_inicial_sin_iva()),
                ('dotación B con Testo', wbv[H_EQ]['X%d' % EQ_TOT].value, D.dotacion_b_con_testo()),
                ('dotación B núcleo', wbv[H_EQ]['X%d' % EQ_NUC].value, D.dotacion_b_nucleo()),
                ('dotación A con Testo', wbv[H_EQ]['Y%d' % EQ_TOT].value, D.dotacion_a_con_testo()),
                ('dotación A núcleo', wbv[H_EQ]['Y%d' % EQ_NUC].value, D.dotacion_a_nucleo()),
                ('equipamiento y mobiliario', wbv[H_RES]['B%d' % R_FILAS['Equipamiento y mobiliario (bloques 2 a 7)']].value,
                 D.equipamiento_y_mobiliario()),
                ('obra nueva bloques 1 a 8', wbv[H_TRA]['B%d' % T['capex_o']].value,
                 sum(D.capex_bloque(n) for n in range(1, 9)))]
    for n in sorted(D.BLOQUES_CAPEX):
        chequeos.append(('bloque %d' % n, vc['E%d' % BLOQUE_FILA[n]].value, D.capex_bloque(n)))
    for etq, v, e in chequeos:
        if not _cerca(v, e):
            raise SystemExit('%s: el libro da %r y datos_ejemplo %r' % (etq, v, e))
    if abs(D.dotacion_b_nucleo() - 8618.35) > 0.005 or abs(D.dotacion_b_con_testo() - 9117.35) > 0.005:
        raise SystemExit('Las sumas de control de §3.4 no cuadran al céntimo')

    mapa = {}
    for etiqueta, hoja, coord, tipo in mapa_celdas():
        if tipo not in ('entrada', 'salida', 'parametro'):
            raise SystemExit('Tipo de mapa no válido: %r' % tipo)
        v = wbv[hoja][coord].value
        if v is None:
            raise SystemExit('El mapa cita %s!%s («%s») y está VACÍA' % (hoja, coord, etiqueta))
        if etiqueta in mapa:
            raise SystemExit('Etiqueta de mapa repetida: %r' % etiqueta)
        if isinstance(v, datetime.datetime):
            v = v.strftime('%d/%m/%Y')
        mapa[etiqueta] = {'ref': '%s!%s!%s' % (FICHERO, hoja, coord), 'valor': v, 'tipo': tipo}
    for x, hoja, celda, _v, _e in contrato:
        if not any(d['ref'] == '%s!%s!%s' % (FICHERO, hoja, celda) for d in mapa.values()):
            raise SystemExit('El mapa no cita la celda de origen %s!%s (%s)' % (hoja, celda, x))
    with open(os.path.join(destino, 'mapa-' + NOMBRE + '.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(mapa, ensure_ascii=False, indent=1))

    return {'ruta': ruta, 'hojas': len(wbf.worksheets), 'formulas': len(motor.REGISTRO),
            'sin_dato': len(sin_dato), 'verdes': n_verdes, 'verdes_vacias': verdes_vacias,
            'notas_legales': len(NOTAS_LEGALES), 'mapa': len(mapa), 'contrato': contrato,
            'cache': (salida_cache.strip().splitlines() or [''])[-1],
            'capex': vc['E%d' % B_TOT].value, 'iva': vc['F%d' % B_TOT].value,
            'ver_inv': wbv[H_TRA]['B%d' % T['ver_inv']].value,
            'umbral': wbv[H_TRA]['B%d' % T['umbral']].value}


# ==========================================================================
# Demostraciones con pycel
# ==========================================================================
def demo(ruta):
    from pycel import ExcelCompiler
    ok, fallos = [], []

    def prueba(nombre, cond, detalle=''):
        (ok if cond else fallos).append(nombre + (' - ' + detalle if detalle else ''))

    def ev(xl, hoja, coord):
        return xl.evaluate("'%s'!%s" % (hoja, coord))

    def sv(xl, hoja, coord, v):
        xl.set_value("'%s'!%s" % (hoja, coord), v)

    rx9 = RX[_X9['n']]
    rac = RX[_X17_ACEITE['n']]

    # 1. X9 = 1 (el libro 1 dice que necesitas extinción automática): el bloque 8 y el
    #    CAPEX que viaja al 6 suben el importe de la extinción; el CUADRE avisa.
    xl = ExcelCompiler(ruta)
    c0 = ev(xl, H_RES, 'L5')
    b0 = ev(xl, H_CAP, 'E%d' % BLOQUE_FILA[8])
    ev(xl, H_PAR, 'B%d' % rx9['cuad'])
    imp = ev(xl, H_CAP, 'H%d' % F_EXT)
    sv(xl, H_PAR, 'B%d' % rx9['rec'], 1)
    c1 = ev(xl, H_RES, 'L5')
    b1 = ev(xl, H_CAP, 'E%d' % BLOQUE_FILA[8])
    cu = ev(xl, H_PAR, 'B%d' % rx9['cuad'])
    prueba('con extinción automática (X9 = 1) el CAPEX sube su importe y el CUADRE avisa',
           abs((c1 - c0) - imp) < 1e-6 and abs((b1 - b0) - imp) < 1e-6 and str(cu).startswith('REVISA'),
           'CAPEX %.2f -> %.2f (+%.2f) · %s' % (c0, c1, c1 - c0, cu))

    # 2. X17: si el aceite cuesta el doble, el stock inicial sube 75 L por su precio.
    xl = ExcelCompiler(ruta)
    s0 = ev(xl, H_CAP, 'I%d' % S_TOT)
    ev(xl, H_RES, 'L5')
    ev(xl, H_PAR, 'B%d' % rac['cuad'])
    p0 = _X17_ACEITE['valor_defecto']
    litros = dict(D.STOCK_INICIAL)['aceite']
    sv(xl, H_PAR, 'B%d' % rac['rec'], p0 * 2)
    s1 = ev(xl, H_CAP, 'I%d' % S_TOT)
    cu = ev(xl, H_PAR, 'B%d' % rac['cuad'])
    prueba('el aceite al doble (X17) sube el stock inicial en litros x precio y el CUADRE avisa',
           abs((s1 - s0) - litros * p0) < 1e-6 and str(cu).startswith('REVISA'),
           'stock %.2f -> %.2f · %s' % (s0, s1, cu))

    # 3. La renta nace aquí (X18): subirla mueve Parámetros!L5 y la fianza del bloque 9.
    xl = ExcelCompiler(ruta)
    r0, f0, k0 = ev(xl, H_PAR, 'L5'), ev(xl, H_CAP, 'E%d' % BLOQUE_FILA[9]), ev(xl, H_RES, 'L5')
    sv(xl, H_PAR, 'B%d' % P['renta_mensual'], D.dato(D.NEGOCIO, 'renta_mensual') + 100)
    r1, f1, k1 = ev(xl, H_PAR, 'L5'), ev(xl, H_CAP, 'E%d' % BLOQUE_FILA[9]), ev(xl, H_RES, 'L5')
    meses = D.dato(D.NEGOCIO, 'meses_fianza')
    prueba('100 € más de renta: X18 sube 100 y la fianza y el CAPEX suben 100 por los meses de fianza',
           abs(r1 - r0 - 100) < 1e-9 and abs(f1 - f0 - 100 * meses) < 1e-9 and abs(k1 - k0 - 100 * meses) < 1e-9,
           'renta %.0f -> %.0f · fianza %.0f -> %.0f' % (r0, r1, f0, f1))

    # 4. Un traspaso cerrado por debajo del umbral cambia el veredicto.
    xl = ExcelCompiler(ruta)
    v0 = ev(xl, H_TRA, 'B%d' % T['ver_inv'])
    um = ev(xl, H_TRA, 'B%d' % T['umbral'])
    sv(xl, H_TRA, 'B%d' % T['pedido'], um - 1000)
    v1 = ev(xl, H_TRA, 'B%d' % T['ver_inv'])
    prueba('un traspaso cerrado 1.000 € por debajo del umbral pasa el veredicto al traspaso',
           v0 == 'Sale mejor la OBRA NUEVA' and v1 == 'Sale mejor el TRASPASO',
           'umbral %.2f · %s -> %s' % (um, v0, v1))

    # 5. Comprar la freidora eléctrica en vez de la de gas (decisión 4) mueve el bloque 3.
    xl = ExcelCompiler(ruta)
    q0 = ev(xl, H_CAP, 'E%d' % BLOQUE_FILA[3])
    ev(xl, H_EQ, 'T%d' % EQ_DESV)
    sv(xl, H_EQ, 'G%d' % EQ_ROW['freidora_gas_25l'], 'No')
    sv(xl, H_EQ, 'G%d' % EQ_ROW['freidora_electrica_25l'], 'Sí')
    q1 = ev(xl, H_CAP, 'E%d' % BLOQUE_FILA[3])
    dif = (D.importe_sin_iva(D.equipo('freidora_electrica_25l')) - D.importe_sin_iva(D.equipo('freidora_gas_25l')))
    prueba('cambiar la freidora de gas por la eléctrica sube el bloque 3 lo que cuesta de más',
           abs((q1 - q0) - dif) < 1e-6, 'bloque 3 %.2f -> %.2f (+%.2f)' % (q0, q1, q1 - q0))

    # 6. El medidor de polares tecleado SIN marcar que lleva IVA desvía la línea un 21 %.
    xl = ExcelCompiler(ruta)
    t0 = ev(xl, H_EQ, 'O%d' % EQ_ROW['testo_270'])
    ev(xl, H_EQ, 'T%d' % EQ_ROW['testo_270'])
    sv(xl, H_EQ, 'M%d' % EQ_ROW['testo_270'], 'No')
    t1 = ev(xl, H_EQ, 'O%d' % EQ_ROW['testo_270'])
    dv = ev(xl, H_EQ, 'T%d' % EQ_ROW['testo_270'])
    prueba('el medidor de polares sin marcar «lleva IVA» desvía su base un 21 %',
           abs(t0 - 499.0) < 0.005 and abs(dv - D.P('iva_general')) < 1e-3,
           'base %.2f -> %.2f · desviación %.4f' % (t0, t1, dv))

    # 7. R-05c: la superficie viene del libro 1 (X9 bis). Más metros, más obra; y el CUADRE avisa.
    xl = ExcelCompiler(ruta)
    rm = RX[_X9B['n']]
    o0 = ev(xl, H_CAP, 'H%d' % F_OBRA)
    ev(xl, H_PAR, 'B%d' % rm['cuad'])
    sv(xl, H_PAR, 'B%d' % rm['rec'], 100)
    o1 = ev(xl, H_CAP, 'H%d' % F_OBRA)
    cm = ev(xl, H_PAR, 'B%d' % rm['cuad'])
    prueba('100 m² en vez de 75 (X9 bis): la obra sube 25 m² por el coste por metro y el CUADRE avisa',
           abs((o1 - o0) - 25 * D.OBRA_EUR_M2[0]) < 1e-6 and str(cm).startswith('REVISA'),
           'obra %.0f -> %.0f · %s' % (o0, o1, cm))

    # 8. R-05b: el precio de un insumo del stock llega del libro 3 (X17): al doble, sube el stock.
    xl = ExcelCompiler(ruta)
    ck = _X17_INS['cobertura']
    rk = RX[ck['n']]
    s0 = ev(xl, H_CAP, 'I%d' % S_TOT)
    ev(xl, H_PAR, 'B%d' % rk['cuad'])
    sv(xl, H_PAR, 'B%d' % rk['rec'], ck['valor_defecto'] * 2)
    s1 = ev(xl, H_CAP, 'I%d' % S_TOT)
    ccu = ev(xl, H_PAR, 'B%d' % rk['cuad'])
    q_cob = dict(D.STOCK_INICIAL)['cobertura']
    prueba('la cobertura al doble (X17) sube el stock inicial en kilos x precio y el CUADRE avisa',
           abs((s1 - s0) - q_cob * ck['valor_defecto']) < 1e-6 and str(ccu).startswith('REVISA'),
           'stock %.2f -> %.2f · %s' % (s0, s1, ccu))

    # 9. R-04: el CAPEX que no se amortiza (X10 bis) sube con la fianza (meses de fianza x renta).
    xl = ExcelCompiler(ruta)
    n0 = ev(xl, H_RES, 'L6')
    sv(xl, H_PAR, 'B%d' % P['renta_mensual'], D.dato(D.NEGOCIO, 'renta_mensual') + 100)
    n1 = ev(xl, H_RES, 'L6')
    prueba('100 € más de renta suben el CAPEX que no se amortiza (X10 bis) 100 x meses de fianza',
           abs(n0 - D._capex_no_amortizable()) < 1e-6
           and abs((n1 - n0) - 100 * D.dato(D.NEGOCIO, 'meses_fianza')) < 1e-6,
           '%.2f -> %.2f' % (n0, n1))

    # 10. R-11: sólo las enseñas de base comparable entran en el recuento contra tu CAPEX.
    xl = ExcelCompiler(ruta)
    d0 = ev(xl, H_FRA, 'B%d' % FR['debajo'])
    ev(xl, H_FRA, 'B%d' % FR['encima'])
    i_king = FR_INI + [f['marca'] for f in D.FRANQUICIAS].index('King Churro')
    sv(xl, H_FRA, 'I%d' % i_king, 'Sí')
    d1 = ev(xl, H_FRA, 'B%d' % FR['debajo'])
    prueba('marcar como comparable una enseña de 20.000 € («desde») la suma al recuento de las que '
           'están por debajo de tu CAPEX (2 -> 3)', d0 == 2 and d1 == 3, '%s -> %s' % (d0, d1))
    return ok, fallos


# ==========================================================================
def main():
    ids = sorted(set([i for i, (_t, libros) in D.IDS_LEGALES_REQUERIDOS.items() if LIBRO in libros]
                     + ['CUN-26', 'CUN-41', 'CUN-09', 'CUN-11', 'CUN-12', 'CUN-13', 'CUN-28',
                        'CUN-30', 'CHN-49c']))
    D.gate_legal(ids)
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_parametros(wb)
    hoja_equipamiento(wb)
    hoja_capex(wb)
    hoja_variante(wb)
    hoja_franquicia(wb)
    hoja_traspaso(wb)
    hoja_iva(wb)
    hoja_proveedores(wb)
    hoja_resumen(wb)
    orden = list(D.HOJAS[LIBRO])
    wb._sheets.sort(key=lambda ws: orden.index(ws.title))

    res = cerrar(wb)
    print('escrito: %s' % res['ruta'])
    print('hojas: %d · fórmulas: %d · celdas verdes: %d · verdes vacías: %d'
          % (res['hojas'], res['formulas'], res['verdes'], len(res['verdes_vacias'])))
    print('fórmulas que devuelven «sin dato» a propósito: %d' % res['sin_dato'])
    print('notas legales: %d · etiquetas en el mapa: %d' % (res['notas_legales'], res['mapa']))
    print('cruces recibidos: %d (X9, X9 bis y X17 x14, cada uno con su CUADRE) · celdas de origen: %d'
          % (len(RECEPTORAS), len(res['contrato'])))
    print('inject_cache: %s' % res['cache'])
    print('CAPEX sin fondo de maniobra: %.2f € · IVA soportado %.2f €' % (res['capex'], res['iva']))
    print('traspaso: umbral %.2f € · %s' % (res['umbral'], res['ver_inv']))
    print('contrato (celdas de origen = valor de datos_ejemplo):')
    for x, hoja, celda, v, e in res['contrato']:
        print('  %-7s %s!%s = %.6f (datos_ejemplo %.6f)' % (x, hoja, celda, v, e))
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
