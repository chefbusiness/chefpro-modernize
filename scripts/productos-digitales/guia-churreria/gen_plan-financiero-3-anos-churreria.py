#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_plan-financiero-3-anos-churreria.py - libro 6 de «Cómo Montar una
Churrería-Chocolatería» (producto 51, `guia-churreria-chocolateria`; SPEC
`scripts/productos-digitales/guia-churreria-SPEC.md`, §2.1 fila 6, §2.2, §3.5, §3.6 y §5).

Molde H: se calca `guia-chocolateria/gen_plan-financiero-3-anos-chocolateria.py` (motor
`planes-v2_0` 2.2: P&L a tres años con el año 2 como crucero, cuadro de amortización
mensual escrito como anualidad algebraica, fondo de maniobra por meses de colchón,
principal del préstamo como punto fijo). Fuera: «Talleres y Regalo Corporativo». El
cierre (inject_cache + data_only + contrato de cruces + lista negra + mapa + demo con
pycel) es el de los libros 3, 4 y 5 de este mismo producto.

Hojas (`datos_ejemplo.HOJAS[6]`, con «Instrucciones» delante por la regla de familia):
Instrucciones · 0. Supuestos · Inversión Inicial · PyG 3 Años · Punto de Equilibrio ·
Escenarios · Personal · Tesorería 12 meses · Financiación · Canales y Punto Muerto.

CIERRA EL GRAFO (D16, `datos_ejemplo.CRUCES`)
---------------------------------------------
Recibe X10 y X18 (libro 2: CAPEX sin fondo y renta), X11 (libro 3: materia y ticket por
canal y mix de canales), X12 (libro 4: renovación del aceite), X13, X14 y X16 (libro 5:
raciones del año, doce coeficientes, ferias y contribución del verano) y X15 (libro 8:
plantilla). Cada uno es una celda VERDE de «0. Supuestos» con el rótulo «cópialo del
libro N: <fichero>!<Hoja>!<Celda>» y su valor por defecto, más UNA FILA DE CUADRE con
semáforo. No es origen de ningún cruce. Nunca una fórmula entre ficheros.

DECISIONES QUE MATERIALIZA
--------------------------
* Los GASTOS FIJOS MENSUALES nacen sólo aquí (`datos_ejemplo.GASTOS_FIJOS_MENSUALES`);
  la renta llega por X18 y la plantilla por X15.
* El FONDO DE MANIOBRA se calcula sólo aquí: meses de colchón por los fijos de caja del
  mes (plantilla, renta, fijos e intereses del año de crucero). Inversión total = CAPEX
  (sin fondo, X10) + fondo.
* El principal del préstamo es un PUNTO FIJO, igual que la hermana: celda verde con el
  valor de `principal_prestamo()` y una comprobación que dice si coincide con lo que pide
  la estructura (60 % de la inversión, redondeado). Sin referencia circular.
* Veredictos en EUROS, nunca por ratio: el DSCR se enseña como información y la lectura
  «¿aguanta el banco?» es la holgura en euros del peor año.
* El verano entra por contribución (X16). «Verano: resultado con fijos» en «Escenarios».
* Año 2 = año de crucero: reproduce al céntimo `datos_ejemplo.cuenta_resultados_crucero()`.

Salida: build/plan-financiero-3-anos-churreria.xlsx + build/mapa-plan-financiero-3-anos-churreria.json
Uso: /usr/local/bin/python3 gen_plan-financiero-3-anos-churreria.py
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

LIBRO = 6
FICHERO = D.LIBROS[LIBRO]
NOMBRE = os.path.splitext(FICHERO)[0]
TITULO = 'Plan Financiero a 3 Años'
SUBJECT = CC.PRODUCTO + ' · Versión 1.0 · octubre 2026'
assert NOMBRE == 'plan-financiero-3-anos-churreria'

(H_SUP, H_INV, H_PYG, H_PEQ, H_ESC, H_PER, H_TES, H_FIN, H_CAN, H_INS) = D.HOJAS[LIBRO]
assert H_INS == 'Instrucciones'
#: Orden de las pestañas: «Instrucciones» PRIMERO (regla de familia) y el resto en el orden
#: de `datos_ejemplo.HOJAS[6]`, que la pone al final porque copia la fila de §2.1.
ORDEN_HOJAS = (H_INS,) + tuple(h for h in D.HOJAS[LIBRO] if h != H_INS)


def Q(hoja):
    return "'" + hoja + "'!"


def ABS_(hoja, coord):
    m = re.match(r'([A-Z]+)(\d+)$', coord)
    return Q(hoja) + '$' + m.group(1) + '$' + m.group(2)


def RNG(hoja, a, b):
    ma = re.match(r'([A-Z]+)(\d+)$', a)
    mb = re.match(r'([A-Z]+)(\d+)$', b)
    return Q(hoja) + '$%s$%s:$%s$%s' % (ma.group(1), ma.group(2), mb.group(1), mb.group(2))


def ie(expr, alterna=''):
    return motor.iferror(expr, alterna)


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
PCT2 = '0.00%'
PCT4 = '0.0000%'
ENT = motor.FMT_ENT
DEC = '#,##0.00'
DEC1 = '#,##0.0'

NOTAS_LEGALES = []
NOTAS_SECTOR = []
VERDES = []
CRUCE_VERDES = []        # (hoja, coord, x, concepto)
CRUCE_CUADRES = []       # (hoja, coord, x, concepto)


def cabecera_hoja(ws, titulo, nota_txt=None, merge_hasta=None):
    motor.val(ws, 'A1', CC.titulo_hoja(titulo), bold=True)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    motor.val(ws, 'A2', CC.SUBTITULO)
    ws['A2'].font = Font(size=10, color=GRIS)
    if nota_txt:
        if merge_hasta:
            ws.merge_cells('A3:%s3' % merge_hasta)
        motor.val(ws, 'A3', nota_txt, wrap=True)
        ws['A3'].font = Font(italic=True, size=9)
        ws.row_dimensions[3].height = 40


def seccion(ws, coord, texto):
    motor.val(ws, coord, texto, bold=True)
    ws[coord].font = Font(bold=True, size=12, color=ORO)


def gris(ws, coord, texto, alto=None):
    motor.val(ws, coord, texto, wrap=True)
    ws[coord].font = Font(size=8, color=GRIS)
    if alto:
        ws.row_dimensions[int(re.sub(r'[A-Z]', '', coord))].height = alto
    return ws[coord]


def etiqueta(ws, coord, texto, negrita=False):
    motor.val(ws, coord, texto, wrap=True)
    ws[coord].font = Font(size=10, bold=negrita)
    return ws[coord]


def encabezados(ws, fila, cols, alto=40, congelar=False):
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


def total(ws, fila, letras):
    for letra in letras:
        c = ws[letra + str(fila)]
        c.font = Font(bold=True, size=10)
        crema(c)


def entrada(ws, coord, valor, fmt=None, etiqueta_=''):
    """Celda VERDE con su valor por defecto. Ninguna verde vacía."""
    if valor is None or (isinstance(valor, str) and not valor.strip()):
        raise SystemExit('entrada(%s!%s, «%s») sin valor por defecto: ninguna celda '
                         'verde puede quedar vacía' % (ws.title, coord, etiqueta_))
    cel = motor.val(ws, coord, valor, fmt=fmt, verde_=True)
    VERDES.append((ws.title, coord, etiqueta_, valor))
    return cel


def formula(ws, coord, txt, fmt=None, bold=None, destacar=False):
    cel = motor.f(ws, coord, txt, fmt=fmt, bold=bold)
    if destacar:
        crema(cel)
    return cel


def nota_legal(ws, coord, pid, extra=None):
    txt = D.nota_legal(pid)
    if not txt:
        raise SystemExit('nota_legal(%r) vacía: gate_legal() debería haber abortado' % pid)
    if extra:
        txt = txt + ' · ' + extra
    ws[coord].comment = Comment(txt, 'AI Chef Pro', height=130, width=470)
    NOTAS_LEGALES.append((ws.title, coord, pid))
    return txt


RX_ID = D.RX_ID


def nota_fuente(ws, coord, fuente, extra=None):
    """Procedencia de un dato de SECTOR (CUS-*, CHS-*, FC-IVA-*): id, fiabilidad y URL."""
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
    NOTAS_SECTOR.append((ws.title, coord, fuente))
    return partes


def comentario(ws, coord, texto):
    ws[coord].comment = Comment(texto, 'AI Chef Pro', height=110, width=440)


def texto_fuente(fuente):
    if not fuente:
        return ''
    if fuente.startswith('supuesto'):
        return 'supuesto declarado de El Molinete' + fuente[len('supuesto'):]
    return fuente


def setup(ws, apaisado=True, titulos=None, area=None):
    CC.pagina(ws, apaisado=apaisado, titulos=titulos, area=area)


def version_al_pie(ws, fila, col='A'):
    motor.val(ws, '%s%d' % (col, fila), CC.VERSION_LINE)
    ws['%s%d' % (col, fila)].font = Font(size=8, italic=True)


# ==========================================================================
# Los cruces que recibe este libro (todos de `datos_ejemplo.CRUCES`)
# ==========================================================================
CRUCES_IN = [c for c in D.CRUCES if c['receptor'] == LIBRO]
CRUCES_OUT = [c for c in D.CRUCES if c['origen'] == LIBRO]
assert not CRUCES_OUT, 'El libro 6 cierra el grafo: no es origen de ningún cruce'
assert sorted(set(c['x'] for c in CRUCES_IN)) == sorted(
    ['X10', 'X10 bis', 'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X16 bis', 'X16 ter', 'X18']), \
    [c['x'] for c in CRUCES_IN]
assert all(c['hoja_receptor'] == H_SUP for c in CRUCES_IN)
assert len(set(c['calcula'] for c in CRUCES_IN)) == len(CRUCES_IN)

ETIQUETA_CRUCE = {
    'capex_total': ('CAPEX de apertura SIN fondo de maniobra (base imponible)', '€', EUR),
    '_renta': ('Renta mensual del local (sin IVA)', '€/mes', EUR),
    '_materia_sala': ('Coste de materia por ración en sala (invierno, aceite absorbido incluido)',
                      '€/ración', EUR4),
    '_materia_llevar': ('Coste de materia por ración para llevar (invierno, aceite absorbido '
                        'incluido)', '€/ración', EUR4),
    '_ticket_sala': ('Ticket sin IVA por ración en sala (invierno)', '€/ración', EUR4),
    '_ticket_llevar': ('Ticket sin IVA por ración para llevar (invierno)', '€/ración', EUR4),
    '_pct_sala_fraccion': ('Raciones que se consumen en sala (el resto, para llevar)', '%', PCT),
    '_capex_no_amortizable': ('Partidas del CAPEX que no se amortizan (fianza, stock inicial y '
                              'marketing de apertura)', '€', EUR),
    '_contribucion_verano_cerrar': ('Contribución de julio y agosto si cierras', '€', EUR),
    '_contribucion_verano_carta': ('Contribución de julio y agosto con carta de verano', '€', EUR),
    '_contribucion_verano_ferias': ('Contribución de julio y agosto con ferias', '€', EUR),
    '_ventas_verano_elegida': ('Ventas sin IVA del local en julio y agosto de la salida que eliges',
                               '€', EUR),
    'renovacion_por_racion': ('Renovación del aceite por ración (el aceite que se tira al '
                              'cambiar la cuba)', '€/ración', EUR4),
    'raciones_anio': ('Raciones de un año normal', 'raciones', ENT),
    'resultado_anual_ferias': ('Resultado anual de ferias (las de fuera de julio y agosto)', '€', EUR),
    '_contribucion_verano_elegida': ('Contribución de julio y agosto de la salida que eliges', '€',
                                     EUR),
    'coste_plantilla_anual': ('Coste anual de la plantilla (Seguridad Social, refuerzos y '
                              'sustituciones incluidos)', '€/año', EUR),
}
for _i in range(12):
    ETIQUETA_CRUCE['_coef_%02d' % (_i + 1)] = ('Coeficiente de ' + D.MESES[_i].lower(),
                                               'coeficiente', DEC)

NOTA_CRUCE = {
    'capex_total': ('El total de los once bloques del libro 2, SIN fondo de maniobra: el fondo se '
                    'calcula aquí y sólo aquí. Si copias un total que ya lo lleve, lo contarías '
                    'dos veces.'),
    '_renta': 'Nace en el libro 2 (con el traspaso y la fianza). Aquí entra en los fijos.',
    '_materia_sala': 'Materia prima más el aceite que se queda en la masa. Sale del escandallo.',
    '_materia_llevar': 'Con el envase de llevar dentro. Sale del escandallo.',
    '_ticket_sala': 'Base imponible media de una ración de la carta en sala.',
    '_ticket_llevar': 'Base imponible media para llevar, con el vaso cobrado aparte.',
    '_pct_sala_fraccion': ('Se copia tal cual, con el formato de porcentaje (0,70 es el 70 %). Con '
                           'él se mezclan el ticket y la materia de los dos canales.'),
    '_capex_no_amortizable': ('Son los bloques 9, 10 y 11 de tu CAPEX: la fianza se recupera, el '
                              'stock se vende y el marketing es gasto del primer año. Nace en el '
                              'libro 2: si tu CAPEX cambia, cópiala de nuevo.'),
    '_contribucion_verano_cerrar': ('Cerrar deja cero por definición, salvo que cambies las '
                                    'banderas de la salida en el libro 5. Aquí se enseña con los '
                                    'fijos dentro, en «Escenarios».'),
    '_contribucion_verano_carta': ('Ventas menos materia de julio y agosto con la carta de verano. '
                                   'Con ella y las dos de al lado, «Escenarios» enseña el verano '
                                   'con fijos de las tres salidas.'),
    '_contribucion_verano_ferias': ('Lo que dejan las ferias de julio y agosto, ya con su materia, '
                                    'tasas, desplazamiento, montaje y personal.'),
    '_ventas_verano_elegida': ('Las ventas del local de julio y agosto con el ticket de la salida '
                               'que eliges (carta de verano, cero si cierras o sales de ferias). '
                               'Valoran el verano de las ventas del año.'),
    'renovacion_por_racion': ('Distinto del aceite absorbido, que ya va en la materia: es el '
                              'descarte al cambiar el aceite.'),
    'raciones_anio': ('Días tipo y días punta por su demanda base. Es un año normal: la rampa '
                      'del primer año la pone este libro.'),
    'resultado_anual_ferias': ('Una línea de canal. El punto muerto de cada evento vive en el libro '
                               '5; las ferias de julio y agosto van en la salida del verano.'),
    '_contribucion_verano_elegida': ('Ventas sin IVA menos materia de julio y agosto de la salida '
                                     'que eliges. Lo que pagas igual en las tres salidas lo resta '
                                     'este libro.'),
    'coste_plantilla_anual': ('Con el suelo del SMI y el plus de nocturnidad ya aplicados en el '
                              'libro 8. El titular va dentro como un puesto más; su cuota de '
                              'autónomos, en los gastos fijos.'),
}
for _i in range(12):
    NOTA_CRUCE['_coef_%02d' % (_i + 1)] = ('Reparte las raciones del año: los doce suman 12.'
                                           if _i == 0 else '')

GRUPOS = [
    (2, 'Lo que Copias del Libro 2 (CAPEX y Renta)'),
    (3, 'Lo que Copias del Libro 3 (Carta y Escandallo)'),
    (4, 'Lo que Copias del Libro 4 (Aceite de Fritura)'),
    (5, 'Lo que Copias del Libro 5 (Temporada, Verano y Ferias)'),
    (8, 'Lo que Copias del Libro 8 (Plantilla)'),
]

# ==========================================================================
# Filas de «0. Supuestos»
# ==========================================================================
S = {}
SECCIONES_SUP = []
CRUCE_ROW = {}
_FILA = [6]


def _sec(titulo):
    SECCIONES_SUP.append((_FILA[0], titulo))
    _FILA[0] += 1


def _row(clave):
    S[clave] = _FILA[0]
    _FILA[0] += 1


for _o, _t in GRUPOS:
    _sec(_t)
    for _c in CRUCES_IN:
        if _c['origen'] == _o:
            CRUCE_ROW[_c['calcula']] = _FILA[0]
            _FILA[0] += 1
assert len(CRUCE_ROW) == len(CRUCES_IN)
S['no_amort'] = CRUCE_ROW['_capex_no_amortizable']      # R-04: ya no es una verde propia sin cruce
COEF_INI, COEF_FIN = CRUCE_ROW['_coef_01'], CRUCE_ROW['_coef_12']
assert COEF_FIN - COEF_INI == 11

_FILA[0] += 1
_sec('Calendario, Arranque y Crecimiento')
for _k in ('dias_anio', 'dias_cierre', 'meses', 'mes_apertura', 'mes_ver1', 'mes_ver2', 'rampa1',
           'rampa_meses', 'crec3'):
    _row(_k)
assert S['mes_ver2'] == S['mes_ver1'] + 1
_FILA[0] += 1
_sec('Fondo de Maniobra, Amortización e Inversión')
for _k in ('colchon', 'anios_amort', 'anio_crucero'):
    _row(_k)
_FILA[0] += 1
_sec('Financiación')
for _k in ('pct_prestamo', 'pct_propios', 'tipo', 'plazo', 'carencia', 'principal', 'redondeo',
           'tol_cuadro'):
    _row(_k)
_FILA[0] += 1
_sec('Gastos Fijos Mensuales (Nacen Sólo Aquí, sin IVA)')
GF = D.GASTOS_FIJOS_MENSUALES
for _i in range(len(GF)):
    _row('gf_%02d' % _i)
_row('gf_total')
I_AUTONOMOS = [i for i, g in enumerate(GF) if g[0].startswith('Cuota de autónomos')][0]
_FILA[0] += 1
_sec('Escenarios')
for _k in ('var_pes', 'var_opt', 'ahorro_desp'):
    _row(_k)
_FILA[0] += 1
_sec('Tolerancia de las Filas de CUADRE')
_row('tol')
_FILA[0] += 1
S_SEC_CUA = _FILA[0]
S_CUA_CAB = S_SEC_CUA + 1
S_CUA_INI = S_CUA_CAB + 1
CUADRE_ROW = dict((c['calcula'], S_CUA_INI + i) for i, c in enumerate(CRUCES_IN))
S_CUA_FIN = S_CUA_INI + len(CRUCES_IN) - 1


def SB(clave):
    return ABS_(H_SUP, 'B%d' % S[clave])


def XB(calcula):
    return ABS_(H_SUP, 'B%d' % CRUCE_ROW[calcula])


COEFS = RNG(H_SUP, 'B%d' % COEF_INI, 'B%d' % COEF_FIN)
MESES_ = SB('meses')
DIAS_APERTURA = '(%s-%s)' % (SB('dias_anio'), SB('dias_cierre'))

#: Supuestos de ESTE libro que no están en `datos_ejemplo.py` (no hay dato que copiar):
#: palancas de escenario, sin crecimiento en el año 3 y el redondeo del préstamo. Se
#: declaran en la propia hoja y en las dudas del constructor.
VAR_PESIMISTA = -0.15
VAR_OPTIMISTA = 0.10
CRECIMIENTO_ANIO_3 = 0.0
AHORRO_DESPACHO = 0.0
REDONDEO_PRESTAMO = 100.0          # `principal_prestamo()` redondea a centenas
TOLERANCIA = 0.02                  # la de los libros 1 y 5: heredada de la hermana
TOLERANCIA_CUADRO = 0.01           # heredada de la hermana (cierre del cuadro)
DIAS_ANIO = 365
assert DIAS_ANIO - D.dato(D.NEGOCIO, 'dias_cierre_anio') == D.dias_apertura_anio()

# ==========================================================================
# Filas de las demás hojas
# ==========================================================================
IV = {'sec_capex': 5, 'capex': 6, 'no_amort': 7, 'amortizable': 8, 'anios': 9, 'amort': 10,
      'sec_fondo': 12, 'plantilla_mes': 13, 'renta': 14, 'gf': 15, 'int_mes': 16, 'fijos_caja': 17,
      'colchon': 18, 'fondo': 19,
      'sec_total': 21, 'capex2': 22, 'fondo2': 23, 'inversion': 24, 'prestamo': 25, 'propios': 26,
      'nota': 28}

P = {'cab': 5, 'sec_ing': 6, 'raciones': 7, 'rac_inv': 8, 'ventas_inv': 9, 'materia_inv': 10,
     'cont_carta': 11, 'cont_verano': 12, 'renov': 13, 'ferias': 14, 'contribucion': 15,
     'sec_fijos': 16, 'plantilla': 17, 'renta': 18, 'gf': 19, 'amort': 20, 'intereses': 21,
     'tot_fijos': 22, 'resultado': 23, 'lectura': 24,
     'sec_ventas': 26, 'ventas_ver': 27, 'ventas': 28, 'margen_neto': 29, 'cont_racion': 30,
     'res_racion': 31, 'caja': 32, 'nota': 34}

E = {'sec_base': 5, 'fijos': 6, 'contribucion': 7, 'raciones': 8, 'cont_racion': 9, 'dias': 10,
     'pe_anio': 11, 'pe_dia': 12, 'prev_dia': 13, 'seg_dia': 14, 'seg_eur': 15, 'veredicto': 16,
     'pm_mes': 17, 'ventas_pe_mes': 18, 'pe_caja_dia': 19,
     'sec_mes': 21, 'cab_mes': 22, 'mes_ini': 23}
E['mes_fin'] = E['mes_ini'] + 11
E['mes_tot'] = E['mes_fin'] + 1
E['meses_neg'] = E['mes_tot'] + 1
E['nota'] = E['meses_neg'] + 2

X = {'cab': 5, 'var': 6, 'raciones': 7, 'cont_var': 8, 'ferias': 9, 'contribucion': 10,
     'fijos': 11, 'resultado': 12, 'lectura': 13, 'pe_dia': 14, 'prev_dia': 15, 'seg_dia': 16,
     'sec_ver': 18, 'cab_ver': 19, 'meses_ver': 20, 'fijos_ver': 21, 'cerrar': 22, 'carta': 23,
     'ferias': 24, 'elegida': 25, 'dif_ver': 26, 'nota_ver': 27,
     'sec_fmt': 29, 'cab_fmt': 30, 'f_pct': 31, 'f_rac': 32, 'f_carta': 33, 'f_verano': 34,
     'f_renov': 35, 'f_ferias': 36, 'f_cont': 37, 'f_fijos': 38, 'f_res': 39, 'f_lectura': 40,
     'f_ahorro': 41, 'nota': 43}

R = {'sec': 5, 'plantilla': 6, 'autonomos': 7, 'personas': 8, 'mes': 9, 'racion': 10,
     'sobre_ventas': 11, 'sobre_cont': 12, 'rac_dia': 13, 'sec_frontera': 15, 'frontera': 16}

T = {'cab': 5, 'mes': 6, 'nombre': 7, 'coef': 8, 'verano': 9, 'rampa': 10, 'raciones': 11,
     'sec_cont': 12, 'ventas_inv': 13, 'ventas_ver': 14, 'materia': 15, 'cont_carta': 16,
     'cont_verano': 17, 'renov': 18, 'ferias': 19, 'cont_neta': 20,
     'sec_pagos': 21, 'plantilla': 22, 'renta': 23, 'gf': 24, 'intereses': 25, 'principal': 26,
     'pagos': 27, 'flujo': 28, 'saldo': 29,
     'sec_valle': 31, 'saldo_ini': 32, 'fondo': 33, 'valle': 34, 'mes_valle': 35, 'veredicto': 36,
     'consumo': 37, 'nota': 38,
     'sec_cal': 40, 'cab_cal': 41, 'cal_ini': 42}
T['cal_fin'] = T['cal_ini'] + 11
MESES_COL = ('B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M')
COL_TOT = 'N'

F = {'sec_origen': 5, 'propios': 6, 'prestamo': 7, 'tot_origen': 8, 'pct_real': 9,
     'sec_usos': 10, 'inversion': 11, 'propios_est': 12, 'dif_propios': 13,
     'sec_pf': 14, 'pide': 15, 'punto_fijo': 16,
     'sec_cond': 17, 'principal': 18, 'tipo': 19, 'tipo_mes': 20, 'plazo': 21, 'carencia': 22,
     'meses_am': 23, 'cuota': 24, 'nota_cuota': 25, 'cab': 27}
F_MESES = 84
F_MES_INI = F['cab'] + 1
F_MES_FIN = F_MES_INI + F_MESES - 1
F_PENDIENTE = F_MES_FIN + 1
F_CIERRA = F_MES_FIN + 2
F_SEC_ANIO = F_MES_FIN + 4
F_ANIO_CAB = F_SEC_ANIO + 1
F_ANIO_INI = F_ANIO_CAB + 1
F_ANIOS = 7
F_ANIO_FIN = F_ANIO_INI + F_ANIOS - 1
F_PEOR = F_ANIO_FIN + 1
F_AGUANTA = F_ANIO_FIN + 2
F_ANIO_PEOR = F_ANIO_FIN + 3
F_DSCR_MIN = F_ANIO_FIN + 4
F_NOTA = F_ANIO_FIN + 6
assert D.dato(D.FINANCIACION, 'plazo_meses') <= F_MESES

K = {'cab': 5, 'sala': 6, 'llevar': 7, 'mix': 8, 'verano': 9, 'ferias': 10, 'renov': 11,
     'total': 12, 'sec_fijos': 14, 'fijos': 15, 'cab_fijos': 16, 'f_sala': 17, 'f_llevar': 18,
     'f_juntas': 19, 'f_todo': 20, 'quien': 21, 'nota': 23}

#: Interés del año de crucero, del resumen anual de «Financiación».
INT_ANIOS = RNG(H_FIN, 'B%d' % F_ANIO_INI, 'B%d' % F_ANIO_FIN)


def int_crucero():
    return 'INDEX(%s,%s)' % (INT_ANIOS, SB('anio_crucero'))


# ==========================================================================
# Hoja «Instrucciones»
# ==========================================================================
def _orden_relleno():
    partes = ['%d (%s)' % (n, D.LIBROS[n]) for n in D.ORDEN_RELLENO if n != 7]
    return ('Orden de relleno del paquete: ' + ', luego '.join(partes)
            + '. El libro 7 (%s) no depende de ninguno: rellénalo cuando quieras. Este es el '
              'libro 6 y va el ÚLTIMO de la cadena: rellénalo cuando tengas los otros seis, '
              'porque copia sus cifras.' % D.LIBROS[7])


def _cruces_texto():
    lineas = []
    for o, _t in GRUPOS:
        for c in CRUCES_IN:
            if c['origen'] != o or (c['calcula'].startswith('_coef_') and c['calcula'] != '_coef_01'):
                continue
            if c['calcula'] == '_coef_01':
                lineas.append('0. Supuestos!B%d a B%d - los doce coeficientes del año. Vienen del '
                              'libro 5: %s!%s!L6 a L17.' % (COEF_INI, COEF_FIN, c['fichero_origen'],
                                                           c['hoja_origen']))
                continue
            lineas.append('0. Supuestos!B%d - %s. Viene del libro %d: %s!%s!%s.' % (
                CRUCE_ROW[c['calcula']], c['concepto'], c['origen'], c['fichero_origen'],
                c['hoja_origen'], c['celda_origen']))
    return lineas


PASOS = [
    '1. Hoja «0. Supuestos». Arriba, las cifras que copias a mano de los libros 2, 3, 4, 5 y 8 '
    '(cada celda verde dice de qué celda exacta). Debajo, el calendario, la rampa de arranque, '
    'el fondo de maniobra, la financiación, los GASTOS FIJOS de cada mes (nacen aquí) y los '
    'escenarios. Al pie, el CUADRE: anota lo que publica hoy cada celda de origen y, si lo que '
    'usas se separa, la fila se pone en rojo.',
    '2. Hoja «Inversión Inicial». El CAPEX del libro 2 más el fondo de maniobra, que se calcula '
    'aquí con los meses de colchón: es la inversión total que le enseñas al banco.',
    '3. Hoja «PyG 3 Años». La cuenta de resultados: el año 1 con la rampa de arranque, el año 2 '
    'de crucero y el año 3. La primera pregunta es si el año 2 gana dinero, en euros.',
    '4. Hoja «Punto de Equilibrio». Cuántas raciones al día pagan los fijos y qué meses del año '
    'no llegan.',
    '5. Hoja «Escenarios». Tres escenarios de raciones, el verano con los fijos dentro (las '
    'tres salidas del libro 5: cerrar, carta de verano y ferias) y el local con sala frente a '
    'sólo despacho.',
    '6. Hojas «Personal» y «Canales y Punto Muerto». Lo que pesa la plantilla y qué canal (sala, '
    'para llevar, ferias) paga los fijos.',
    '7. Hojas «Tesorería 12 meses» y «Financiación». El primer año mes a mes con su valle, el '
    'cuadro del préstamo y si el negocio genera la cuota todos los años.',
]

NOTAS_LIBRO = [
    'ESTE LIBRO CIERRA EL PAQUETE. No recalcula tu escandallo (libro 3), tu plantilla (libro 8), '
    'tu temporada (libro 5) ni tu CAPEX (libro 2): los copia. Lo que es SUYO son los gastos fijos '
    'de cada mes, el fondo de maniobra, la rampa del primer año y la deuda.',
    'EL FONDO DE MANIOBRA SE CALCULA AQUÍ Y SÓLO AQUÍ. El CAPEX que copias del libro 2 no lo '
    'lleva: inversión total = CAPEX + fondo. Si copiaras un total que ya lo incluyera, lo '
    'contarías dos veces.',
    'LOS VEREDICTOS VAN EN EUROS. «¿Gana dinero?», «¿aguanta el fondo el valle?», «¿aguanta el '
    'banco?» y «¿qué canal paga los fijos?» se contestan con euros que sobran o que faltan. El '
    'DSCR del préstamo se enseña porque te lo van a pedir, pero no decide nada solo.',
    'EL PRÉSTAMO ES UN PUNTO FIJO. Su importe depende del fondo de maniobra, y el fondo depende '
    'de los intereses del préstamo. Para no crear una referencia circular, el préstamo es una '
    'celda verde: la hoja «Financiación» te dice cuánto pide la estructura y, si no coincide, '
    'copias esa cifra en el préstamo y listo.',
    'TODO VA SIN IVA. Las ventas, la materia, los fijos y la caja son bases imponibles. El IVA '
    'que adelantas al comprar el equipo lo calcula el libro 2 (hoja «IVA y Tesorería») y no '
    'entra aquí. Este libro tampoco calcula el impuesto sobre el beneficio (Sociedades o IRPF): '
    'depende de tu forma jurídica; el resultado es ANTES de impuestos.',
    'LAS VENTAS DE JULIO Y AGOSTO SON LAS DE LA SALIDA QUE ELIGES. Del verano viajan del libro 5 '
    'la CONTRIBUCIÓN de las tres salidas (para el resultado y para «Escenarios») y las ventas '
    'sin IVA de la que eliges (para las ventas del año). Si cierras o sales de ferias, el '
    'local no vende en esos dos meses y sus ventas son cero.',
    'LOS SUPUESTOS NO SON DATOS DEL SECTOR. Los gastos fijos, la rampa, los meses de colchón, la '
    'financiación y los escenarios son supuestos declarados de El Molinete (o heredados de la '
    'guía hermana), sin fuente pública. Pon los tuyos.',
]

CADENCIA = ('Cada cuánto se usa este libro: antes de firmar el local y antes de ir al banco; '
            'luego, al cerrar cada trimestre con tus cifras reales (tu TPV y tu gestoría las dan). '
            'Si cambia alguna cifra de otro libro, vuelve a copiarla en «0. Supuestos» y mira el '
            'CUADRE.')


def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS)
    ws.column_dimensions['A'].width = 100.0
    cabecera_hoja(ws, TITULO)
    motor.val(ws, 'A3', 'Para qué sirve: saber si el negocio gana dinero en un año normal, '
                        'cuánto tienes que poner el día que abres (con el fondo de maniobra), si '
                        'aguanta el valle del primer año, si aguanta el banco y qué canal paga '
                        'los fijos.', wrap=True)
    ws['A3'].font = Font(italic=True, size=9)
    fila = 5
    seccion(ws, 'A%d' % fila, 'Instrucciones de Uso')
    fila += 1
    entrada(ws, 'A%d' % fila, motor.NOTA_VERDES, etiqueta_='Leyenda de celdas verdes')
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
              '«0. Supuestos» una celda verde para copiarlo a mano, con la celda exacta de origen, '
              'y una fila de CUADRE que avisa si se separa de lo que publica el origen. Este libro '
              'no pasa ninguna cifra a otro: es el último de la cadena.', wrap=True)
    ws.row_dimensions[fila].height = 44
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
        ws.row_dimensions[fila].height = 60
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, CADENCIA, wrap=True)
    ws.row_dimensions[fila].height = 44
    fila += 2
    motor.val(ws, 'A%d' % fila, CC.NOTA_DESPROTEGER, wrap=True)
    fila += 2
    motor.val(ws, 'A%d' % fila, CC.BIO, wrap=True)
    fila += 1
    version_al_pie(ws, fila)
    setup(ws, apaisado=False)
    return ws


# ==========================================================================
# Hoja «0. Supuestos»
# ==========================================================================
def fila_sup(ws, clave, etq, valor, fmt, unidad, origen, nota, pct=False, form=None, minimo=0,
             maximo=None, legal=None, fuente_sector=None):
    fila = S[clave]
    etiqueta(ws, 'A%d' % fila, etq)
    if form is not None:
        cel = formula(ws, 'B%d' % fila, form, fmt=fmt, bold=True, destacar=True)
    else:
        cel = entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta_=etq)
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
    if fuente_sector:
        nota_fuente(ws, cel.coordinate, fuente_sector)
    return cel


def hoja_supuestos(wb):
    ws = wb.create_sheet(H_SUP)
    cabecera_hoja(ws, 'Supuestos del Plan Financiero',
                  'Todo lo que el resto de hojas da por sabido vive aquí. Ninguna fórmula de este '
                  'libro lleva dentro un tipo, un porcentaje, un número de meses ni un umbral.',
                  merge_hasta='E')
    for letra, ancho in (('A', 56), ('B', 17), ('C', 13), ('D', 50), ('E', 66)):
        ws.column_dimensions[letra].width = ancho
    encabezados(ws, 5, [('A', 'Supuesto', None), ('B', 'Valor', None), ('C', 'Unidad', None),
                        ('D', 'De dónde sale', None), ('E', 'Nota', None)], alto=24, congelar=True)
    for fila, titulo in SECCIONES_SUP:
        seccion(ws, 'A%d' % fila, titulo)

    # --- cruces ----------------------------------------------------------------
    for c in CRUCES_IN:
        clave = c['calcula']
        etq, uni, fmt = ETIQUETA_CRUCE[clave]
        fila = CRUCE_ROW[clave]
        valor = c['valor_defecto']
        if fmt == ENT:
            valor = int(round(valor))
        etiqueta(ws, 'A%d' % fila, etq)
        cel = entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta_=etq)
        if clave in ('resultado_anual_ferias', '_contribucion_verano_elegida', '_contribucion_verano_cerrar',
                     '_contribucion_verano_carta', '_contribucion_verano_ferias'):
            motor.dv_numerica(ws, [cel.coordinate], minimo=-10 ** 9,
                              mensaje='Escribe un importe: puede ser negativo si pierde dinero.')
        elif clave == '_pct_sala_fraccion':
            motor.dv_porcentaje(ws, [cel.coordinate])
        else:
            motor.dv_numerica(ws, [cel.coordinate], minimo=0)
        motor.val(ws, 'C%d' % fila, uni)
        motor.val(ws, 'D%d' % fila, D.rotulo_cruce(c), wrap=True)
        ws['D%d' % fila].font = Font(size=8, color=GRIS)
        gris(ws, 'E%d' % fila, NOTA_CRUCE[clave])
        ws.row_dimensions[fila].height = 40 if not clave.startswith('_coef_') else 30
        if clave == '_renta':
            nota_fuente(ws, cel.coordinate, 'CUS-02',
                        extra='La renta del local de referencia de 74 m². Nace en el libro 2.')
        CRUCE_VERDES.append((ws.title, cel.coordinate, c['x'], c['concepto']))

    # --- calendario, arranque y crecimiento --------------------------------------
    fila_sup(ws, 'dias_anio', 'Días del año', DIAS_ANIO, ENT, 'días', 'calendario',
             'Un año normal.', minimo=1, maximo=366)
    v, fuente, nota_ = D.NEGOCIO['dias_cierre_anio']
    fila_sup(ws, 'dias_cierre', 'Días al año con el local cerrado', v, ENT, 'días',
             texto_fuente(fuente), nota_ + ' Los mismos que pones en «Parámetros» del libro 5.',
             minimo=0, maximo=365)
    fila_sup(ws, 'meses', 'Meses del año (los cuenta la hoja: son los coeficientes)', None, ENT,
             'meses', 'calculado', 'Cuenta los doce coeficientes de arriba. Sirve para pasar de '
             'año a mes sin escribir un 12 dentro de ninguna fórmula.',
             form='=COUNT(%s)' % COEFS)
    v, fuente, nota_ = D.NEGOCIO['mes_apertura']
    fila_sup(ws, 'mes_apertura', 'Mes de apertura (número del mes)', v, ENT, 'mes',
             texto_fuente(fuente), nota_ + ' El año 1 de este libro son los doce meses que '
             'empiezan aquí.', minimo=1, maximo=12)
    fila_sup(ws, 'mes_ver1', 'Primer mes del verano (número del mes)', D.MESES_VERANO[0], ENT, 'mes',
             texto_fuente(D.FUENTE_COEFICIENTES),
             'El valle: julio. Son los meses de la contribución del verano (X16) y los mismos que '
             'pones en el libro 5.', minimo=1, maximo=12)
    fila_sup(ws, 'mes_ver2', 'Segundo mes del verano (número del mes)', D.MESES_VERANO[1], ENT, 'mes',
             texto_fuente(D.FUENTE_COEFICIENTES), 'Agosto.', minimo=1, maximo=12)
    v, fuente, _n = D.RAMPA['mes1']
    fila_sup(ws, 'rampa1', 'Ventas del primer mes sobre las de un mes normal (rampa)', v, PCT, '',
             fuente, 'El primer mes vendes el 55 % de lo que venderás cuando el barrio te conozca.',
             pct=True)
    v, fuente, _n = D.RAMPA['meses']
    fila_sup(ws, 'rampa_meses', 'Meses hasta vender como un mes normal', v, ENT, 'meses', fuente,
             'La rampa sube en línea recta desde el primer mes hasta este.', minimo=1, maximo=12)
    fila_sup(ws, 'crec3', 'Crecimiento de las raciones en el año 3 sobre el año 2', CRECIMIENTO_ANIO_3,
             PCT, '', 'supuesto declarado de este libro (sin crecimiento)',
             'A cero: el año 3 repite el año de crucero y sólo cambian los intereses. Si subes '
             'precios o ganas clientela, ponlo aquí; si lo hace tu competencia, en negativo.',
             minimo=-1, maximo=1)
    # --- fondo, amortización e inversión ------------------------------------------
    v, fuente, nota_ = D.PARAMS['meses_colchon']
    fila_sup(ws, 'colchon', 'Meses de colchón (fondo de maniobra)', v, ENT, 'meses', fuente, nota_,
             minimo=0, maximo=24)
    v, fuente, nota_ = D.PARAMS['anios_amortizacion']
    fila_sup(ws, 'anios_amort', 'Años de amortización del inmovilizado', v, ENT, 'años', fuente, nota_,
             minimo=1, maximo=50)
    v, fuente, nota_ = D.PARAMS['anio_crucero']
    fila_sup(ws, 'anio_crucero', 'Año de crucero (el que da los intereses del fondo)', v, ENT, 'año',
             fuente, nota_, minimo=1, maximo=F_ANIOS)

    # --- financiación ----------------------------------------------------------
    v, fuente, _n = D.FINANCIACION['pct_prestamo']
    fila_sup(ws, 'pct_prestamo', 'Parte de la inversión total que pides al banco', v, PCT, '', fuente,
             'La estructura heredada de la hermana: 40 % de fondos propios y 60 % de préstamo.',
             pct=True)
    v, fuente, _n = D.FINANCIACION['pct_recursos_propios']
    fila_sup(ws, 'pct_propios', 'Parte que pones tú (recursos propios)', None, PCT, '', fuente,
             'Lo que no pides al banco. Se calcula: un solo dato para la estructura.',
             form='=1-%s' % SB('pct_prestamo'))
    v, fuente, _n = D.FINANCIACION['tipo_nominal']
    fila_sup(ws, 'tipo', 'Tipo de interés nominal anual', v, PCT2, '', fuente,
             'Pide la oferta por escrito: con la TAE delante, no sólo el nominal.', pct=True)
    v, fuente, _n = D.FINANCIACION['plazo_meses']
    fila_sup(ws, 'plazo', 'Plazo del préstamo (meses)', v, ENT, 'meses', fuente,
             'El cuadro de «Financiación» tiene 84 filas: más plazo no cabe.', minimo=1,
             maximo=F_MESES)
    v, fuente, _n = D.FINANCIACION['carencia_meses']
    fila_sup(ws, 'carencia', 'Carencia de principal (meses en que sólo pagas intereses)', v, ENT,
             'meses', fuente, 'Es lo que hace que la cuota no se coma la caja en la rampa del '
             'primer año. Es lo primero que hay que negociar.', minimo=0, maximo=F_MESES)
    fila_sup(ws, 'principal', 'Préstamo bancario que pides (punto fijo)', D.principal_prestamo(), EUR,
             '€', 'calculado en datos_ejemplo: principal_prestamo()',
             'El 60 % de la inversión total, redondeado. Como la inversión lleva el fondo y el '
             'fondo lleva los intereses, la hoja «Financiación» te dice si esta cifra sigue siendo '
             'la que pide la estructura; si no, copia la suya aquí.', minimo=0)
    fila_sup(ws, 'redondeo', 'Redondeo del préstamo (múltiplo de)', REDONDEO_PRESTAMO, EUR, '€',
             'heredado: datos_ejemplo.principal_prestamo() (centenas)',
             'Los bancos conceden cifras redondas.', minimo=1)
    fila_sup(ws, 'tol_cuadro', 'Tolerancia del cierre del cuadro y del punto fijo', TOLERANCIA_CUADRO,
             EUR, '€', 'heredado: guia-chocolateria (Tolerancia de cierre del cuadro)',
             'Por debajo de esta diferencia, dos importes se dan por iguales.', minimo=0)

    # --- gastos fijos mensuales -------------------------------------------------------
    for i, (concepto, importe, fuente, nota_) in enumerate(GF):
        clave = 'gf_%02d' % i
        legal = None
        sector = None
        if 'CHN-75' in fuente:
            legal = 'CHN-75'
        elif 'CHN-48' in fuente:
            legal = 'CHN-48'
        elif 'CUN-23' in fuente:
            legal = 'CUN-23'
        if 'CUS-44h' in fuente:
            sector = 'CUS-44h'
        origen = texto_fuente(fuente) if fuente.startswith('supuesto') else fuente
        fila_sup(ws, clave, concepto, importe, EUR, '€/mes', origen,
                 nota_ or 'Supuesto, sin fuente pública; pon el tuyo.', minimo=0, legal=legal,
                 fuente_sector=sector)
    fila_sup(ws, 'gf_total', 'TOTAL GASTOS FIJOS DEL MES (sin renta ni plantilla)', None, EUR, '€/mes',
             'calculado', 'La renta llega del libro 2 y la plantilla del libro 8: no están aquí.',
             form='=SUM(B%d:B%d)' % (S['gf_00'], S['gf_%02d' % (len(GF) - 1)]))
    total(ws, S['gf_total'], 'AB')

    # --- escenarios ----------------------------------------------------------------
    fila_sup(ws, 'var_pes', 'Escenario pesimista: raciones sobre el año normal', VAR_PESIMISTA, PCT, '',
             'supuesto declarado de este libro',
             'Un año entero yendo mal (un invierno templado, una obra en la calle), no un mal día.',
             minimo=-1, maximo=1)
    fila_sup(ws, 'var_opt', 'Escenario optimista: raciones sobre el año normal', VAR_OPTIMISTA, PCT, '',
             'supuesto declarado de este libro', 'Más clientela con la misma plantilla.',
             minimo=-1, maximo=1)
    fila_sup(ws, 'ahorro_desp', 'Ahorro de fijos al año si montas sólo despacho (sin sala)',
             AHORRO_DESPACHO, EUR, '€/año', 'supuesto declarado de este libro',
             'A cero, «Escenarios» enseña lo que pierdes si el mismo local vende sólo para llevar. '
             'Sin sala te ahorras parte de la plantilla, de la renta y de la limpieza: pon aquí ese '
             'ahorro.', minimo=0)

    # --- tolerancia --------------------------------------------------------------
    fila_sup(ws, 'tol', 'Tolerancia de las filas de CUADRE', TOLERANCIA, PCT, '',
             'heredado: guia-chocolateria (Tolerancia de las filas de CUADRE)',
             'Por encima de esta desviación, la fila de CUADRE avisa de que lo que has copiado no '
             'es lo que publica el libro de origen.', pct=True)

    # --- CUADRE ----------------------------------------------------------------------
    seccion(ws, 'A%d' % S_SEC_CUA, 'Cuadre de lo que Has Copiado')
    encabezados(ws, S_CUA_CAB, [('A', 'Cuadre', None),
                                ('B', 'Lo que publica hoy la celda de origen (anótalo)', None),
                                ('C', 'Desviación', None), ('D', 'Veredicto', None),
                                ('E', 'Si no cuadra', None)], alto=36)
    t = SB('tol')
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
                      etiqueta_='%s: lo que publica el libro %d' % (c['x'], c['origen']))
        motor.dv_numerica(ws, [cel.coordinate], minimo=-10 ** 9)
        formula(ws, 'C%d' % fila, ie('IF(B{f}=0,ABS({x}-B{f}),ABS({x}-B{f})/ABS(B{f}))'
                                     .format(f=fila, x=XB(clave))), fmt=PCT)
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
    version_al_pie(ws, S_CUA_FIN + 2)
    setup(ws, apaisado=True, titulos='5:5')
    return ws


# ==========================================================================
# Hoja «Inversión Inicial»
# ==========================================================================
def linea(ws, fila, etq, form=None, fmt=EUR, nota_txt=None, negrita=False, col='B', col_nota='C'):
    etiqueta(ws, 'A%d' % fila, etq, negrita=negrita)
    cel = None
    if form is not None:
        cel = formula(ws, '%s%d' % (col, fila), form, fmt=fmt, bold=negrita or None)
    if nota_txt:
        gris(ws, '%s%d' % (col_nota, fila), nota_txt)
    ws.row_dimensions[fila].height = max(ws.row_dimensions[fila].height or 15, 30)
    return cel


def hoja_inversion(wb):
    ws = wb.create_sheet(H_INV)
    cabecera_hoja(ws, 'Inversión Inicial: CAPEX y Fondo de Maniobra',
                  'El CAPEX llega del libro 2 SIN fondo de maniobra; el fondo se calcula aquí, con '
                  'los fijos de caja de un mes y los meses de colchón. Inversión total = CAPEX + '
                  'fondo. Todo sin IVA.', merge_hasta='C')
    for letra, ancho in (('A', 60), ('B', 18), ('C', 80)):
        ws.column_dimensions[letra].width = ancho

    seccion(ws, 'A%d' % IV['sec_capex'], 'CAPEX (del Libro 2, sin Fondo de Maniobra)')
    linea(ws, IV['capex'], 'CAPEX de apertura (copiado del libro 2)', '=%s' % XB('capex_total'),
          nota_txt='Los once bloques del libro 2: obra, extracción, fritura, chocolate, barra, control, '
                   'TPV, licencias, fianza, stock y marketing.')
    linea(ws, IV['no_amort'], 'De él, lo que no se amortiza (fianza, stock y marketing)',
          '=%s' % SB('no_amort'), nota_txt='Se pone en «0. Supuestos».')
    linea(ws, IV['amortizable'], 'CAPEX que se amortiza',
          '=B%d-B%d' % (IV['capex'], IV['no_amort']))
    linea(ws, IV['anios'], 'Años de amortización', '=%s' % SB('anios_amort'), fmt=ENT)
    linea(ws, IV['amort'], 'Amortización anual', ie('B%d/B%d' % (IV['amortizable'], IV['anios'])),
          negrita=True, nota_txt='Es un coste del P&L pero no sale de la caja.')
    total(ws, IV['amort'], 'AB')

    seccion(ws, 'A%d' % IV['sec_fondo'], 'Fondo de Maniobra (Se Calcula Aquí y Sólo Aquí)')
    linea(ws, IV['plantilla_mes'], 'Plantilla de un mes', ie('%s/%s' % (XB('coste_plantilla_anual'), MESES_)),
          nota_txt='El coste anual del libro 8 entre los meses del año.')
    linea(ws, IV['renta'], 'Renta del mes', '=%s' % XB('_renta'))
    linea(ws, IV['gf'], 'Gastos fijos del mes', '=%s' % SB('gf_total'))
    linea(ws, IV['int_mes'], 'Intereses de un mes del año de crucero',
          ie('%s/%s' % (int_crucero(), MESES_)),
          nota_txt='Los del año de crucero de «Financiación», no los de la carencia: con los del año 1 '
                   'el fondo saldría distinto según cuándo lo mires.')
    linea(ws, IV['fijos_caja'], 'Fijos de caja de un mes', '=SUM(B%d:B%d)' % (IV['plantilla_mes'], IV['int_mes']),
          negrita=True, nota_txt='La amortización no está: no es caja.')
    total(ws, IV['fijos_caja'], 'AB')
    linea(ws, IV['colchon'], 'Meses de colchón', '=%s' % SB('colchon'), fmt=ENT)
    linea(ws, IV['fondo'], 'FONDO DE MANIOBRA', '=B%d*B%d' % (IV['fijos_caja'], IV['colchon']),
          negrita=True, nota_txt='Lo que tiene que haber en la cuenta el día que abres para pagar los '
                                'fijos mientras el negocio arranca y en el valle del verano.')
    total(ws, IV['fondo'], 'AB')

    seccion(ws, 'A%d' % IV['sec_total'], 'Inversión Total')
    linea(ws, IV['capex2'], 'CAPEX sin fondo', '=B%d' % IV['capex'])
    linea(ws, IV['fondo2'], 'Fondo de maniobra', '=B%d' % IV['fondo'])
    linea(ws, IV['inversion'], 'INVERSIÓN TOTAL (CAPEX + fondo)', '=B%d+B%d' % (IV['capex2'], IV['fondo2']),
          negrita=True, nota_txt='Es la cifra que le enseñas al banco.')
    total(ws, IV['inversion'], 'AB')
    linea(ws, IV['prestamo'], 'De ella, préstamo bancario', '=%s' % SB('principal'))
    linea(ws, IV['propios'], 'De ella, lo que pones tú', '=B%d-B%d' % (IV['inversion'], IV['prestamo']))
    motor.semaforo_isnumber(ws, 'B%d' % IV['propios'], '$B$%d' % IV['propios'], operador='<', umbral='0')
    CC.parrafo(ws, IV['nota'],
               'El IVA que adelantas al comprar el equipo y pagar la obra NO está aquí: lo calcula el '
               'libro 2 en su hoja «IVA y Tesorería» y Hacienda te lo devuelve después. Cuéntalo con tu '
               'banco aparte, porque el día que abres sí sale de la cuenta.', col_ini='A', col_fin='C',
               alto=44)
    ws.freeze_panes = 'A5'
    setup(ws, apaisado=False)
    return ws


# ==========================================================================
# Hoja «Canales y Punto Muerto»
# ==========================================================================
def hoja_canales(wb):
    ws = wb.create_sheet(H_CAN)
    cabecera_hoja(ws, 'Canales y Punto Muerto: Sala, para Llevar y Ferias',
                  'Lo que deja cada canal en el año de crucero y si alguno paga los fijos él solo. '
                  'Las raciones de la carta de invierno son las de los meses fuera de julio y agosto; '
                  'el verano entra con su contribución (libro 5).', merge_hasta='H')
    encabezados(ws, K['cab'], [
        ('A', 'Canal', 44), ('B', 'Parte de las raciones', 13),
        ('C', 'Raciones de la carta de invierno (año de crucero)', 16),
        ('D', 'Ticket sin IVA por ración', 14), ('E', 'Materia por ración (aceite absorbido incluido)', 16),
        ('F', 'Contribución por ración', 14), ('G', 'Contribución del año', 16),
        ('H', 'Peso sobre la contribución', 13)], alto=48, congelar=True)
    rac_inv = ABS_(H_PYG, 'C%d' % P['rac_inv'])
    filas = ((K['sala'], 'Sala (barra, mesas y terraza)', '=%s' % XB('_pct_sala_fraccion'),
              XB('_ticket_sala'), XB('_materia_sala')),
             (K['llevar'], 'Para llevar (despacho a calle)', '=1-B%d' % K['sala'],
              XB('_ticket_llevar'), XB('_materia_llevar')))
    for fila, nombre, f_pct, tick, mat in filas:
        etiqueta(ws, 'A%d' % fila, nombre)
        formula(ws, 'B%d' % fila, f_pct, fmt=PCT)
        formula(ws, 'C%d' % fila, '=%s*B%d' % (rac_inv, fila), fmt=ENT)
        formula(ws, 'D%d' % fila, '=%s' % tick, fmt=EUR4)
        formula(ws, 'E%d' % fila, '=%s' % mat, fmt=EUR4)
        formula(ws, 'F%d' % fila, '=D%d-E%d' % (fila, fila), fmt=EUR4)
        formula(ws, 'G%d' % fila, '=C%d*F%d' % (fila, fila), fmt=EUR)
    fm = K['mix']
    etiqueta(ws, 'A%d' % fm, 'Carta de invierno: los dos canales juntos (la mezcla)', negrita=True)
    formula(ws, 'B%d' % fm, '=B%d+B%d' % (K['sala'], K['llevar']), fmt=PCT)
    formula(ws, 'C%d' % fm, '=C%d+C%d' % (K['sala'], K['llevar']), fmt=ENT)
    formula(ws, 'D%d' % fm, '=B%d*D%d+B%d*D%d' % (K['sala'], K['sala'], K['llevar'], K['llevar']), fmt=EUR4)
    formula(ws, 'E%d' % fm, '=B%d*E%d+B%d*E%d' % (K['sala'], K['sala'], K['llevar'], K['llevar']), fmt=EUR4)
    formula(ws, 'F%d' % fm, '=D%d-E%d' % (fm, fm), fmt=EUR4)
    formula(ws, 'G%d' % fm, '=G%d+G%d' % (K['sala'], K['llevar']), fmt=EUR)
    total(ws, fm, 'ABCDEFGH')
    etiqueta(ws, 'A%d' % K['verano'], 'Julio y agosto: la salida que eliges en el libro 5')
    formula(ws, 'G%d' % K['verano'], '=%s' % XB('_contribucion_verano_elegida'), fmt=EUR)
    etiqueta(ws, 'A%d' % K['ferias'], 'Ferias (resultado del año, libro 5)')
    formula(ws, 'G%d' % K['ferias'], '=%s' % XB('resultado_anual_ferias'), fmt=EUR)
    etiqueta(ws, 'A%d' % K['renov'], 'Renovación del aceite (todas las raciones del año, en negativo)')
    formula(ws, 'G%d' % K['renov'], '=-%s*%s' % (XB('raciones_anio'), XB('renovacion_por_racion')), fmt=EUR)
    etiqueta(ws, 'A%d' % K['total'], 'CONTRIBUCIÓN DEL AÑO DE CRUCERO', negrita=True)
    formula(ws, 'G%d' % K['total'], '=SUM(G%d:G%d)' % (K['mix'], K['renov']), fmt=EUR, bold=True)
    total(ws, K['total'], 'AG')
    for fila in (K['sala'], K['llevar'], K['mix'], K['verano'], K['ferias'], K['renov']):
        formula(ws, 'H%d' % fila, ie('G%d/$G$%d' % (fila, K['total'])), fmt=PCT)

    seccion(ws, 'A%d' % K['sec_fijos'], '¿Qué Canal Paga los Fijos?')
    etiqueta(ws, 'A%d' % K['fijos'], 'Fijos del año de crucero (los del P&L)')
    formula(ws, 'B%d' % K['fijos'], '=%s' % ABS_(H_PYG, 'C%d' % P['tot_fijos']), fmt=EUR, bold=True)
    encabezados(ws, K['cab_fijos'], [
        ('A', 'Si sólo tuvieras...', None), ('B', 'Contribución del año', None),
        ('C', 'Menos los fijos del año', None), ('D', 'Lectura en euros', None),
        ('E', 'Raciones al día de equilibrio si todas fueran de este canal', None)], alto=48)
    dias = ABS_(H_PEQ, 'B%d' % E['dias'])
    renov = XB('renovacion_por_racion')
    filas_f = ((K['f_sala'], 'La sala', 'G%d' % K['sala'], 'F%d' % K['sala']),
               (K['f_llevar'], 'El para llevar', 'G%d' % K['llevar'], 'F%d' % K['llevar']),
               (K['f_juntas'], 'Sala y para llevar (la carta de invierno entera)', 'G%d' % K['mix'],
                'F%d' % K['mix']),
               (K['f_todo'], 'Todo el negocio (con el verano, las ferias y el aceite)', 'G%d' % K['total'],
                None))
    for fila, nombre, g, fcol in filas_f:
        etiqueta(ws, 'A%d' % fila, nombre)
        formula(ws, 'B%d' % fila, '=%s' % g, fmt=EUR)
        formula(ws, 'C%d' % fila, '=B%d-$B$%d' % (fila, K['fijos']), fmt=EUR, bold=True)
        motor.semaforo_isnumber(ws, 'C%d' % fila, '$C$%d' % fila, operador='<', umbral='0')
        formula(ws, 'D%d' % fila, '=IF(NOT(ISNUMBER(C%d)),"",IF(C%d>=0,"Paga los fijos","No llega a los fijos"))'
                % (fila, fila))
        motor.semaforo_texto(ws, 'D%d' % fila, (
            ('Paga los fijos', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
            ('No llega a los fijos', motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
        if fcol:
            formula(ws, 'E%d' % fila, ie('IF(%s-%s<=0,"",$B$%d/(%s-%s)/%s)' % (fcol, renov, K['fijos'], fcol,
                                                                                renov, dias)), fmt=DEC1)
        else:
            formula(ws, 'E%d' % fila, '=%s' % ABS_(H_PEQ, 'B%d' % E['pe_dia']), fmt=DEC1)
        ws.row_dimensions[fila].height = 30
    etiqueta(ws, 'A%d' % K['quien'], 'El canal que más deja')
    formula(ws, 'B%d' % K['quien'], '=IF(G%d>=G%d,A%d,A%d)' % (K['sala'], K['llevar'], K['sala'], K['llevar']),
            bold=True)
    CC.parrafo(ws, K['nota'],
               'Las ferias tienen su propio punto muerto, evento a evento, en el libro 5 (hoja «Punto '
               'Muerto por Evento»): aquí entra sólo su resultado del año. Las raciones al día de '
               'equilibrio de un canal suponen que todas tus raciones fueran de ese canal, con la '
               'renovación del aceite descontada.', col_ini='A', col_fin='H', alto=44)
    setup(ws, apaisado=True, titulos='%d:%d' % (K['cab'], K['cab']))
    return ws


# ==========================================================================
# Hoja «Tesorería 12 meses»
# ==========================================================================
def hoja_tesoreria(wb):
    ws = wb.create_sheet(H_TES)
    cabecera_hoja(ws, 'Tesorería del Primer Año, Mes a Mes',
                  'Los doce meses que empiezan el mes de apertura, con la rampa de arranque. Flujos '
                  'sin IVA. El valle es el saldo más bajo: si baja de cero, el fondo de maniobra no '
                  'aguanta.', merge_hasta='N')
    ws.column_dimensions['A'].width = 52
    for col in MESES_COL:
        ws.column_dimensions[col].width = 12.5
    ws.column_dimensions[COL_TOT].width = 15
    encabezados(ws, T['cab'], [('A', 'Mes de explotación', None)] + [(c, '', None) for c in MESES_COL]
                + [(COL_TOT, 'Año 1', None)], alto=24)
    for k, col in enumerate(MESES_COL, 1):
        ws['%s%d' % (col, T['cab'])].value = k
        ws['%s%d' % (col, T['cab'])].number_format = ENT
    cal_n = RNG(H_TES, 'B%d' % T['cal_ini'], 'B%d' % T['cal_fin'])
    cal_c = RNG(H_TES, 'C%d' % T['cal_ini'], 'C%d' % T['cal_fin'])
    c1 = 'INDEX(%s,%s)' % (COEFS, SB('mes_ver1'))
    c2 = 'INDEX(%s,%s)' % (COEFS, SB('mes_ver2'))
    tmix = ABS_(H_CAN, 'D%d' % K['mix'])
    mmix = ABS_(H_CAN, 'E%d' % K['mix'])
    fin_int = RNG(H_FIN, 'C%d' % F_MES_INI, 'C%d' % F_MES_FIN)
    fin_am = RNG(H_FIN, 'D%d' % F_MES_INI, 'D%d' % F_MES_FIN)

    etiquetas = [
        (T['mes'], 'Mes del calendario (número)'), (T['nombre'], 'Mes'), (T['coef'], 'Coeficiente del mes'),
        (T['verano'], '¿Julio o agosto? (1 sí, 0 no)'), (T['rampa'], 'Rampa de arranque'),
        (T['raciones'], 'Raciones del mes'),
        (T['ventas_inv'], 'Ventas sin IVA de la carta de invierno'),
        (T['ventas_ver'], 'Ventas sin IVA de julio y agosto (salida elegida, libro 5)'),
        (T['materia'], 'Materia de la carta de invierno'),
        (T['cont_carta'], 'Contribución de la carta de invierno'),
        (T['cont_verano'], 'Contribución de julio y agosto (salida elegida, libro 5)'),
        (T['renov'], 'Renovación del aceite'), (T['ferias'], 'Ferias (resultado del año repartido)'),
        (T['cont_neta'], 'CONTRIBUCIÓN DEL MES'),
        (T['plantilla'], 'Plantilla'), (T['renta'], 'Renta'), (T['gf'], 'Gastos fijos'),
        (T['intereses'], 'Intereses del préstamo'), (T['principal'], 'Devolución de principal'),
        (T['pagos'], 'TOTAL PAGOS FIJOS'), (T['flujo'], 'FLUJO DEL MES'),
        (T['saldo'], 'SALDO DE CAJA AL CIERRE DEL MES')]
    for fila, txt in etiquetas:
        etiqueta(ws, 'A%d' % fila, txt, negrita=txt.isupper() or txt.startswith('CONTRIB'))
    seccion(ws, 'A%d' % T['sec_cont'], 'Lo que Entra: Contribución')
    seccion(ws, 'A%d' % T['sec_pagos'], 'Lo que Sale: Fijos y Deuda')

    for k, col in enumerate(MESES_COL):
        def c(clave, col=col):
            return '%s%d' % (col, T[clave])
        formula(ws, c('mes'), '=MOD(%s+%s%d-1-1,%s)+1' % (SB('mes_apertura'), col, T['cab'], MESES_), fmt=ENT)
        formula(ws, c('nombre'), '=INDEX(%s,%s)' % (cal_n, c('mes')))
        formula(ws, c('coef'), '=INDEX(%s,%s)' % (cal_c, c('mes')), fmt=DEC)
        formula(ws, c('verano'), '=IF(OR(%s=%s,%s=%s),1,0)' % (c('mes'), SB('mes_ver1'), c('mes'), SB('mes_ver2')),
                fmt=ENT)
        formula(ws, c('rampa'), ie('MIN(1,{r1}+(1-{r1})*({col}{cab}-1)/({rn}-1))'.format(
            r1=SB('rampa1'), col=col, cab=T['cab'], rn=SB('rampa_meses')), '1').replace(',"1")', ',1)'),
            fmt=PCT)
        formula(ws, c('raciones'), ie('%s*%s/%s*%s' % (XB('raciones_anio'), c('coef'), MESES_, c('rampa'))),
                fmt=ENT)
        formula(ws, c('ventas_inv'), '=IF(%s=1,0,%s*%s)' % (c('verano'), c('raciones'), tmix), fmt=EUR)
        formula(ws, c('ventas_ver'), ie('IF(%s=1,IF(%s+%s>0,%s*%s/(%s+%s)*%s,0),0)' % (
            c('verano'), c1, c2, XB('_ventas_verano_elegida'), c('coef'), c1, c2, c('rampa'))), fmt=EUR)
        formula(ws, c('materia'), '=IF(%s=1,0,%s*%s)' % (c('verano'), c('raciones'), mmix), fmt=EUR)
        formula(ws, c('cont_carta'), '=%s-%s' % (c('ventas_inv'), c('materia')), fmt=EUR)
        formula(ws, c('cont_verano'), ie('IF(%s=1,IF(%s+%s>0,%s*%s/(%s+%s)*%s,0),0)' % (
            c('verano'), c1, c2, XB('_contribucion_verano_elegida'), c('coef'), c1, c2, c('rampa'))),
            fmt=EUR)
        formula(ws, c('renov'), '=%s*%s' % (c('raciones'), XB('renovacion_por_racion')), fmt=EUR)
        formula(ws, c('ferias'), ie('%s/%s' % (XB('resultado_anual_ferias'), MESES_)), fmt=EUR)
        formula(ws, c('cont_neta'), '=%s+%s-%s+%s' % (c('cont_carta'), c('cont_verano'), c('renov'),
                                                      c('ferias')), fmt=EUR, bold=True)
        formula(ws, c('plantilla'), ie('%s/%s' % (XB('coste_plantilla_anual'), MESES_)), fmt=EUR)
        formula(ws, c('renta'), '=%s' % XB('_renta'), fmt=EUR)
        formula(ws, c('gf'), '=%s' % SB('gf_total'), fmt=EUR)
        formula(ws, c('intereses'), '=INDEX(%s,%s%d)' % (fin_int, col, T['cab']), fmt=EUR)
        formula(ws, c('principal'), '=INDEX(%s,%s%d)' % (fin_am, col, T['cab']), fmt=EUR)
        formula(ws, c('pagos'), '=SUM(%s:%s)' % (c('plantilla'), c('principal')), fmt=EUR, bold=True)
        formula(ws, c('flujo'), '=%s-%s' % (c('cont_neta'), c('pagos')), fmt=EUR, bold=True)
        prev = '$B$%d' % T['saldo_ini'] if k == 0 else '%s%d' % (MESES_COL[k - 1], T['saldo'])
        formula(ws, c('saldo'), '=%s+%s' % (prev, c('flujo')), fmt=EUR, bold=True)
    for clave in ('raciones', 'ventas_inv', 'ventas_ver', 'materia', 'cont_carta', 'cont_verano', 'renov',
                  'ferias', 'cont_neta', 'plantilla', 'renta', 'gf', 'intereses', 'principal', 'pagos',
                  'flujo'):
        fila = T[clave]
        formula(ws, '%s%d' % (COL_TOT, fila), '=SUM(B%d:M%d)' % (fila, fila),
                fmt=ENT if clave == 'raciones' else EUR, bold=True)
        crema(ws['%s%d' % (COL_TOT, fila)])
    for clave in ('cont_neta', 'pagos', 'flujo', 'saldo'):
        total(ws, T[clave], ['A'])
    motor.semaforo_isnumber(ws, 'B%d:M%d' % (T['saldo'], T['saldo']), 'B%d' % T['saldo'], operador='<',
                            umbral='0')

    seccion(ws, 'A%d' % T['sec_valle'], 'El Valle y el Fondo de Maniobra')
    etiqueta(ws, 'A%d' % T['saldo_ini'], 'Saldo el día que abres (lo que pones tú + préstamo - CAPEX)')
    formula(ws, 'B%d' % T['saldo_ini'], '=%s+%s-%s' % (ABS_(H_FIN, 'B%d' % F['propios']),
                                                      ABS_(H_FIN, 'B%d' % F['prestamo']), XB('capex_total')),
            fmt=EUR, bold=True)
    etiqueta(ws, 'A%d' % T['fondo'], 'De él, fondo de maniobra (hoja «Inversión Inicial»)')
    formula(ws, 'B%d' % T['fondo'], '=%s' % ABS_(H_INV, 'B%d' % IV['fondo']), fmt=EUR)
    etiqueta(ws, 'A%d' % T['valle'], 'Saldo más bajo del año (el valle)', negrita=True)
    formula(ws, 'B%d' % T['valle'], '=MIN(B%d:M%d)' % (T['saldo'], T['saldo']), fmt=EUR, bold=True)
    crema(ws['B%d' % T['valle']])
    etiqueta(ws, 'A%d' % T['mes_valle'], 'Mes del valle')
    formula(ws, 'B%d' % T['mes_valle'], ie('INDEX(B%d:M%d,MATCH(B%d,B%d:M%d,0))' % (
        T['nombre'], T['nombre'], T['valle'], T['saldo'], T['saldo'])))
    etiqueta(ws, 'A%d' % T['veredicto'], '¿Aguanta el fondo el valle?', negrita=True)
    formula(ws, 'B%d' % T['veredicto'], '=IF(NOT(ISNUMBER(B%d)),"",IF(B%d>=0,"Aguanta: el saldo no baja de '
                                        'cero","No aguanta: el saldo se pone en negativo"))'
            % (T['valle'], T['valle']), bold=True)
    motor.semaforo_texto(ws, 'B%d' % T['veredicto'], (
        ('Aguanta: el saldo no baja de cero', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
        ('No aguanta: el saldo se pone en negativo', motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    etiqueta(ws, 'A%d' % T['consumo'], 'Caja que se come el arranque hasta el valle')
    formula(ws, 'B%d' % T['consumo'], '=B%d-B%d' % (T['saldo_ini'], T['valle']), fmt=EUR)
    CC.parrafo(ws, T['nota'],
               'En negativo, el valle dice cuántos euros te faltan en el peor mes: sube los meses de '
               'colchón, negocia más carencia o abre en otro mes. Ningún cobro se aplaza: en una '
               'churrería se cobra al momento. El IVA de la explotación se liquida cada trimestre y no '
               'está aquí.', col_ini='A', col_fin='N', alto=44)

    seccion(ws, 'A%d' % T['sec_cal'], 'Calendario (lo Usan las Filas de Arriba)')
    encabezados(ws, T['cab_cal'], [('A', 'Número del mes', None), ('B', 'Mes', None),
                                   ('C', 'Coeficiente (de «0. Supuestos»)', None)], alto=30)
    for m in range(12):
        fila = T['cal_ini'] + m
        motor.val(ws, 'A%d' % fila, m + 1, fmt=ENT)
        motor.val(ws, 'B%d' % fila, D.MESES[m])
        formula(ws, 'C%d' % fila, '=%s' % ABS_(H_SUP, 'B%d' % (COEF_INI + m)), fmt=DEC)
    ws.freeze_panes = 'B%d' % (T['cab'] + 1)
    setup(ws, apaisado=True, titulos='%d:%d' % (T['cab'], T['cab']))
    return ws


# ==========================================================================
# Hoja «Financiación»
# ==========================================================================
def hoja_financiacion(wb):
    ws = wb.create_sheet(H_FIN)
    for letra, ancho in (('A', 56), ('B', 17), ('C', 15), ('D', 17), ('E', 17), ('F', 17), ('G', 12),
                         ('H', 70)):
        ws.column_dimensions[letra].width = ancho
    cabecera_hoja(ws, 'Financiación: de Dónde Sale y Cuánto Cuesta Devolverlo',
                  'El cuadro de amortización es MENSUAL (84 filas) porque la carencia son seis '
                  'meses. La cuota es la anualidad del sistema francés escrita a mano: la función PMT '
                  'está prohibida en esta familia. La lectura de si aguanta el banco va en euros.',
                  merge_hasta='H')

    def lin(clave, etq, form, fmt=EUR, nota_txt=None, negrita=False):
        cel = linea(ws, F[clave], etq, form, fmt=fmt, nota_txt=nota_txt, negrita=negrita, col_nota='H')
        return cel

    seccion(ws, 'A%d' % F['sec_origen'], 'Origen de los Fondos')
    lin('propios', 'Lo que pones tú (recursos propios)', '=B%d-B%d' % (F['inversion'], F['prestamo']),
        nota_txt='La inversión total menos el préstamo. Un banco quiere verte arriesgar lo tuyo.')
    lin('prestamo', 'Préstamo bancario', '=%s' % SB('principal'))
    lin('tot_origen', 'TOTAL ORIGEN DE LOS FONDOS', '=B%d+B%d' % (F['propios'], F['prestamo']), negrita=True)
    total(ws, F['tot_origen'], 'AB')
    lin('pct_real', 'Parte que pones tú, en %', ie('B%d/B%d' % (F['propios'], F['tot_origen'])), fmt=PCT)

    seccion(ws, 'A%d' % F['sec_usos'], 'Usos')
    lin('inversion', 'Inversión total (CAPEX + fondo de maniobra)', '=%s' % ABS_(H_INV, 'B%d' % IV['inversion']))
    lin('propios_est', 'Lo que pondrías tú con la estructura de «0. Supuestos»',
        '=B%d*%s' % (F['inversion'], SB('pct_propios')))
    lin('dif_propios', 'Diferencia (lo que pones tú de verdad menos lo de la estructura)',
        '=B%d-B%d' % (F['propios'], F['propios_est']),
        nota_txt='Sale de redondear el préstamo: unos cientos de euros arriba o abajo.')

    seccion(ws, 'A%d' % F['sec_pf'], 'El Préstamo como Punto Fijo')
    lin('pide', 'Préstamo que pide la estructura (redondeado)',
        ie('ROUND(%s*B%d/%s,0)*%s' % (SB('pct_prestamo'), F['inversion'], SB('redondeo'), SB('redondeo'))),
        nota_txt='El porcentaje de préstamo por la inversión total, redondeado. La inversión lleva el '
                 'fondo, y el fondo los intereses de este mismo préstamo: por eso el préstamo es una '
                 'celda verde y aquí se comprueba.')
    ok_pf = 'Cerrado: el préstamo es el que pide la estructura'
    ko_pf = 'REVISA: copia la cifra de la fila %d en el préstamo de «0. Supuestos»' % F['pide']
    lin('punto_fijo', 'Comprobación del punto fijo',
        '=IF(NOT(ISNUMBER(B{p})),"",IF(ABS(B{p}-B{q})<={t},"{ok}","{ko}"))'.format(
            p=F['pide'], q=F['prestamo'], t=SB('tol_cuadro'), ok=ok_pf, ko=ko_pf), fmt=None, negrita=True,
        nota_txt='Si cambias el CAPEX, los fijos o los meses de colchón, el préstamo que pide la '
                 'estructura cambia: copia la cifra nueva y esta fila vuelve a decir «Cerrado». A la '
                 'segunda vez se queda quieta.')
    ws['B%d' % F['punto_fijo']].alignment = Alignment(wrap_text=True, vertical='top')
    motor.semaforo_texto(ws, 'B%d' % F['punto_fijo'], (
        (ok_pf, motor.CF_VERDE_BG, motor.CF_VERDE_FG), (ko_pf, motor.CF_ROJO_BG, motor.CF_ROJO_FG)))

    seccion(ws, 'A%d' % F['sec_cond'], 'Condiciones del Préstamo')
    lin('principal', 'Importe del principal', '=IF(%s=0,"",%s)' % (SB('principal'), SB('principal')))
    lin('tipo', 'Tipo de interés nominal anual', '=%s' % SB('tipo'), fmt=PCT2)
    lin('tipo_mes', 'Tipo mensual', ie('B%d/%s' % (F['tipo'], MESES_)), fmt=PCT4)
    lin('plazo', 'Plazo total (meses)', '=%s' % SB('plazo'), fmt=ENT)
    lin('carencia', 'Carencia de principal aplicada (meses)',
        '=IF(%s>=%s,%s-1,%s)' % (SB('carencia'), SB('plazo'), SB('plazo'), SB('carencia')), fmt=ENT,
        nota_txt='Una carencia igual o mayor que el plazo no existe: la hoja la recorta.')
    lin('meses_am', 'Meses de amortización', '=B%d-B%d' % (F['plazo'], F['carencia']), fmt=ENT)
    lin('cuota', 'Cuota mensual durante la amortización',
        ie('IF(B{n}<=0,"",IF(B{i}=0,B{p}/B{n},B{p}*B{i}/(1-(1+B{i})^(-B{n}))))'.format(
            n=F['meses_am'], i=F['tipo_mes'], p=F['principal'])), negrita=True)
    total(ws, F['cuota'], 'AB')
    CC.parrafo(ws, F['nota_cuota'],
               'Sistema francés: capital por tipo mensual dividido entre uno menos (uno más el tipo) '
               'elevado a menos el número de cuotas. Con el tipo a cero es el principal entre los '
               'meses de amortización.', col_ini='A', col_fin='H', alto=30)

    encabezados(ws, F['cab'], [('A', 'Mes', None), ('B', 'Capital pendiente', None), ('C', 'Intereses', None),
                               ('D', 'Devolución de principal', None), ('E', 'Cuota total', None),
                               ('F', 'Capital al cierre', None), ('G', '', None), ('H', 'Notas', None)], alto=30)
    for i in range(F_MESES):
        fila = F_MES_INI + i
        motor.val(ws, 'A%d' % fila, i + 1, fmt=ENT, align='center')
        if i == 0:
            formula(ws, 'B%d' % fila, '=IF($B$%d="","",$B$%d)' % (F['principal'], F['principal']), fmt=EUR)
        else:
            formula(ws, 'B%d' % fila, '=IF(OR(A{0}>$B${1},F{2}=""),"",F{2})'.format(fila, F['plazo'], fila - 1),
                    fmt=EUR)
        formula(ws, 'C%d' % fila, '=IF(OR(A{0}>$B${1},B{0}=""),"",B{0}*$B${2})'.format(
            fila, F['plazo'], F['tipo_mes']), fmt=EUR)
        formula(ws, 'D%d' % fila, '=IF(OR(A{0}>$B${1},B{0}=""),"",IF(A{0}<=$B${2},0,MIN(B{0},$B${3}-C{0})))'
                .format(fila, F['plazo'], F['carencia'], F['cuota']), fmt=EUR)
        formula(ws, 'E%d' % fila, '=IF(C{0}="","",C{0}+D{0})'.format(fila), fmt=EUR)
        formula(ws, 'F%d' % fila, '=IF(D{0}="","",B{0}-D{0})'.format(fila), fmt=EUR)
    gris(ws, 'H%d' % F_MES_INI, 'Durante la carencia la devolución de principal vale cero y sólo se pagan '
                                'intereses.')
    etiqueta(ws, 'A%d' % F_PENDIENTE, 'Capital pendiente al vencimiento')
    formula(ws, 'B%d' % F_PENDIENTE, '=IF($B${0}="","",ROUND($B${0}-SUM(D{1}:D{2}),2))'.format(
        F['principal'], F_MES_INI, F_MES_FIN), fmt=EUR)
    etiqueta(ws, 'A%d' % F_CIERRA, '¿Cierra el cuadro de amortización?')
    formula(ws, 'B%d' % F_CIERRA, '=IF(B{0}="","",IF(ABS(B{0})<={1},"Sí","No: revisa el plazo"))'.format(
        F_PENDIENTE, SB('tol_cuadro')))

    seccion(ws, 'A%d' % F_SEC_ANIO, 'Resumen por Año: ¿Genera el Negocio la Cuota?')
    encabezados(ws, F_ANIO_CAB, [('A', 'Año', None), ('B', 'Intereses', None), ('C', 'Devolución de principal', None),
                                 ('D', 'Servicio de la deuda (cuota)', None),
                                 ('E', 'Caja que deja el negocio antes de la deuda', None),
                                 ('F', 'Lo que sobra (o falta) tras pagar al banco', None), ('G', 'DSCR', None),
                                 ('H', 'Notas', None)], alto=48)
    for k in range(F_ANIOS):
        fila = F_ANIO_INI + k
        ini = F_MES_INI + k * 12
        fin = ini + 11
        motor.val(ws, 'A%d' % fila, k + 1, fmt=ENT, align='center')
        formula(ws, 'B%d' % fila, '=SUM(C%d:C%d)' % (ini, fin), fmt=EUR)
        formula(ws, 'C%d' % fila, '=SUM(D%d:D%d)' % (ini, fin), fmt=EUR)
        formula(ws, 'D%d' % fila, '=B%d+C%d' % (fila, fila), fmt=EUR)
        col_pyg = 'BCD'[k] if k < 3 else 'D'
        formula(ws, 'E%d' % fila, '={q}{c}{r}+{q}{c}{a}+{q}{c}{i}'.format(
            q=Q(H_PYG), c=col_pyg, r=P['resultado'], a=P['amort'], i=P['intereses']), fmt=EUR)
        formula(ws, 'F%d' % fila, '=E%d-D%d' % (fila, fila), fmt=EUR, bold=True)
        formula(ws, 'G%d' % fila, ie('IF(D{0}=0,"",E{0}/D{0})'.format(fila)), fmt=DEC)
    motor.semaforo_isnumber(ws, 'F%d:F%d' % (F_ANIO_INI, F_ANIO_FIN), 'F%d' % F_ANIO_INI, operador='<',
                            umbral='0')
    gris(ws, 'H%d' % F_ANIO_INI, 'La caja que deja el negocio es el resultado antes de impuestos más la '
                                 'amortización (que no se paga) y más los intereses (que son parte de la '
                                 'cuota). Del año 4 en adelante se repite el año 3: este libro no '
                                 'proyecta más lejos.', alto=60)
    etiqueta(ws, 'A%d' % F_PEOR, 'Lo que sobra en el peor año del préstamo', negrita=True)
    formula(ws, 'B%d' % F_PEOR, '=MIN(F%d:F%d)' % (F_ANIO_INI, F_ANIO_FIN), fmt=EUR, bold=True)
    crema(ws['B%d' % F_PEOR])
    motor.semaforo_isnumber(ws, 'B%d' % F_PEOR, '$B$%d' % F_PEOR, operador='<', umbral='0')
    etiqueta(ws, 'A%d' % F_AGUANTA, '¿Aguanta el banco?', negrita=True)
    ok_b = 'Aguanta: en el peor año te sobra dinero después de pagar la cuota'
    ko_b = 'No aguanta: hay un año en que el negocio no genera la cuota'
    formula(ws, 'B%d' % F_AGUANTA, '=IF(NOT(ISNUMBER(B%d)),"",IF(B%d>=0,"%s","%s"))'
            % (F_PEOR, F_PEOR, ok_b, ko_b), bold=True)
    motor.semaforo_texto(ws, 'B%d' % F_AGUANTA, (
        (ok_b, motor.CF_VERDE_BG, motor.CF_VERDE_FG), (ko_b, motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    etiqueta(ws, 'A%d' % F_ANIO_PEOR, 'Año del peor margen')
    formula(ws, 'B%d' % F_ANIO_PEOR, ie('MATCH(B%d,F%d:F%d,0)' % (F_PEOR, F_ANIO_INI, F_ANIO_FIN)), fmt=ENT)
    etiqueta(ws, 'A%d' % F_DSCR_MIN, 'DSCR más bajo (información para el banco)')
    formula(ws, 'B%d' % F_DSCR_MIN, '=IF(COUNT(G{0}:G{1})=0,"",MIN(G{0}:G{1}))'.format(F_ANIO_INI, F_ANIO_FIN),
            fmt=DEC)
    gris(ws, 'H%d' % F_DSCR_MIN, 'Caja antes de la deuda entre la cuota. Te lo van a pedir, pero la lectura '
                                 'que decide es la de los euros: un ratio alto sobre una cuota pequeña '
                                 'puede seguir dejando pocos euros.')
    CC.parrafo(ws, F_NOTA,
               'El año de la carencia sale holgado porque casi no devuelves principal. Mira el año 2 y el '
               'año 3, con la cuota completa.', col_ini='A', col_fin='H', alto=30)
    ws.freeze_panes = 'A%d' % (F['cab'] + 1)
    setup(ws, apaisado=True, titulos='%d:%d' % (F['cab'], F['cab']))
    return ws


# ==========================================================================
# Hoja «PyG 3 Años»
# ==========================================================================
def hoja_pyg(wb):
    ws = wb.create_sheet(H_PYG)
    cabecera_hoja(ws, 'Cuenta de Resultados a 3 Años',
                  'Año 1 con la rampa de arranque (suma la hoja de Tesorería), año 2 de crucero (un año '
                  'normal) y año 3. Formato de contribución: lo que deja cada ración menos los fijos. '
                  'Sin IVA y antes de impuestos.', merge_hasta='E')
    encabezados(ws, P['cab'], [('A', 'Concepto', 62), ('B', 'Año 1 (con rampa)', 16),
                               ('C', 'Año 2 (crucero)', 16), ('D', 'Año 3', 16), ('E', 'Notas', 70)],
                alto=30, congelar=True)
    tes = lambda clave: ABS_(H_TES, '%s%d' % (COL_TOT, T[clave]))     # noqa: E731
    crec = SB('crec3')
    c1 = 'INDEX(%s,%s)' % (COEFS, SB('mes_ver1'))
    c2 = 'INDEX(%s,%s)' % (COEFS, SB('mes_ver2'))
    tmix = ABS_(H_CAN, 'D%d' % K['mix'])
    mmix = ABS_(H_CAN, 'E%d' % K['mix'])

    def fila(clave, etq, b, c, d, fmt=EUR, nota_txt=None, negrita=False):
        f = P[clave]
        etiqueta(ws, 'A%d' % f, etq, negrita=negrita)
        for col, form in (('B', b), ('C', c), ('D', d)):
            formula(ws, '%s%d' % (col, f), form, fmt=fmt, bold=negrita or None)
        if nota_txt:
            gris(ws, 'E%d' % f, nota_txt)
        ws.row_dimensions[f].height = 30
        if negrita:
            total(ws, f, 'ABCD')

    seccion(ws, 'A%d' % P['sec_ing'], 'Raciones y Contribución')
    fila('raciones', 'Raciones del año', '=%s' % tes('raciones'), '=%s' % XB('raciones_anio'),
         '=C%d*(1+%s)' % (P['raciones'], crec), fmt=ENT,
         nota_txt='Año 2: las del libro 5. Año 1: con la rampa. Año 3: con el crecimiento de «0. Supuestos».')
    fila('rac_inv', 'De ellas, raciones de la carta de invierno (fuera de julio y agosto)',
         '=SUMIF(%s,0,%s)' % (RNG(H_TES, 'B%d' % T['verano'], 'M%d' % T['verano']),
                              RNG(H_TES, 'B%d' % T['raciones'], 'M%d' % T['raciones'])),
         ie('%s*(SUM(%s)-%s-%s)/%s' % (XB('raciones_anio'), COEFS, c1, c2, MESES_)),
         '=C%d*(1+%s)' % (P['rac_inv'], crec), fmt=ENT)
    fila('ventas_inv', 'Ventas sin IVA de la carta de invierno', '=%s' % tes('ventas_inv'),
         '=C%d*%s' % (P['rac_inv'], tmix), '=D%d*%s' % (P['rac_inv'], tmix),
         nota_txt='Raciones por el ticket medio de la mezcla sala / para llevar (hoja «Canales»).')
    fila('materia_inv', 'Materia de la carta de invierno (aceite absorbido incluido)',
         '=%s' % tes('materia'), '=C%d*%s' % (P['rac_inv'], mmix), '=D%d*%s' % (P['rac_inv'], mmix),
         nota_txt='El margen sale del escandallo del libro 3, nunca de un porcentaje del sector.')
    fila('cont_carta', 'Contribución de la carta de invierno', '=B%d-B%d' % (P['ventas_inv'], P['materia_inv']),
         '=C%d-C%d' % (P['ventas_inv'], P['materia_inv']), '=D%d-D%d' % (P['ventas_inv'], P['materia_inv']))
    fila('cont_verano', 'Contribución de julio y agosto (la salida que eliges en el libro 5)',
         '=%s' % tes('cont_verano'), '=%s' % XB('_contribucion_verano_elegida'),
         '=C%d*(1+%s)' % (P['cont_verano'], crec),
         nota_txt='Si cierras en verano, es cero: los fijos de esos dos meses se pagan igual (hoja «Escenarios»).')
    fila('renov', 'Renovación del aceite (se resta)', '=%s' % tes('renov'),
         '=C%d*%s' % (P['raciones'], XB('renovacion_por_racion')),
         '=D%d*%s' % (P['raciones'], XB('renovacion_por_racion')),
         nota_txt='El aceite que se tira al cambiar la cuba (libro 4). El absorbido ya va en la materia.')
    fila('ferias', 'Ferias (resultado del año, libro 5)', '=%s' % tes('ferias'),
         '=%s' % XB('resultado_anual_ferias'), '=%s' % XB('resultado_anual_ferias'))
    fila('contribucion', 'CONTRIBUCIÓN DEL AÑO',
         '=B{a}+B{b}-B{c}+B{d}'.format(a=P['cont_carta'], b=P['cont_verano'], c=P['renov'], d=P['ferias']),
         '=C{a}+C{b}-C{c}+C{d}'.format(a=P['cont_carta'], b=P['cont_verano'], c=P['renov'], d=P['ferias']),
         '=D{a}+D{b}-D{c}+D{d}'.format(a=P['cont_carta'], b=P['cont_verano'], c=P['renov'], d=P['ferias']),
         negrita=True)

    seccion(ws, 'A%d' % P['sec_fijos'], 'Costes Fijos')
    pl = '=%s' % XB('coste_plantilla_anual')
    fila('plantilla', 'Plantilla (libro 8)', pl, pl, pl,
         nota_txt='La misma los tres años: se contrata desde el primer día.')
    rt = '=%s*%s' % (XB('_renta'), MESES_)
    fila('renta', 'Renta del local (libro 2)', rt, rt, rt)
    gf = '=%s*%s' % (SB('gf_total'), MESES_)
    fila('gf', 'Gastos fijos (suministros, seguros, asesoría, TPV, cuota de autónomos...)', gf, gf, gf,
         nota_txt='Los de «0. Supuestos», que nacen en este libro.')
    am = '=%s' % ABS_(H_INV, 'B%d' % IV['amort'])
    fila('amort', 'Amortización del inmovilizado', am, am, am, nota_txt='No sale de la caja.')
    fila('intereses', 'Intereses del préstamo', '=%s' % ABS_(H_FIN, 'B%d' % F_ANIO_INI),
         '=%s' % ABS_(H_FIN, 'B%d' % (F_ANIO_INI + 1)), '=%s' % ABS_(H_FIN, 'B%d' % (F_ANIO_INI + 2)),
         nota_txt='Los de cada año del cuadro de «Financiación».')
    fila('tot_fijos', 'TOTAL COSTES FIJOS', '=SUM(B%d:B%d)' % (P['plantilla'], P['intereses']),
         '=SUM(C%d:C%d)' % (P['plantilla'], P['intereses']), '=SUM(D%d:D%d)' % (P['plantilla'], P['intereses']),
         negrita=True)
    fila('resultado', 'RESULTADO ANTES DE IMPUESTOS', '=B%d-B%d' % (P['contribucion'], P['tot_fijos']),
         '=C%d-C%d' % (P['contribucion'], P['tot_fijos']), '=D%d-D%d' % (P['contribucion'], P['tot_fijos']),
         negrita=True, nota_txt='En euros. Sin Impuesto de Sociedades ni IRPF: dependen de tu forma jurídica.')
    motor.semaforo_isnumber(ws, 'B%d:D%d' % (P['resultado'], P['resultado']), 'B%d' % P['resultado'],
                            operador='<', umbral='0')
    etiqueta(ws, 'A%d' % P['lectura'], '¿Gana dinero?', negrita=True)
    for col in 'BCD':
        formula(ws, '%s%d' % (col, P['lectura']), '=IF(NOT(ISNUMBER({c}{r})),"",IF({c}{r}>=0,"Gana dinero",'
                '"Pierde dinero"))'.format(c=col, r=P['resultado']), bold=True)
    motor.semaforo_texto(ws, 'B%d:D%d' % (P['lectura'], P['lectura']), (
        ('Gana dinero', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
        ('Pierde dinero', motor.CF_ROJO_BG, motor.CF_ROJO_FG)))

    seccion(ws, 'A%d' % P['sec_ventas'], 'Ventas y Lecturas por Ración')
    fila('ventas_ver', 'Ventas sin IVA de julio y agosto (la salida que eliges en el libro 5)',
         '=%s' % tes('ventas_ver'), '=%s' % XB('_ventas_verano_elegida'),
         '=C%d*(1+%s)' % (P['ventas_ver'], crec),
         nota_txt='Con el ticket de la salida elegida (libro 5, X16 ter): cero si cierras o sales de '
                  'ferias, cuyas ventas están en su contribución. El resultado cuenta con la '
                  'contribución, no con estas ventas.')
    fila('ventas', 'VENTAS SIN IVA DEL AÑO (con el verano de la salida elegida)', '=B%d+B%d' % (P['ventas_inv'], P['ventas_ver']),
         '=C%d+C%d' % (P['ventas_inv'], P['ventas_ver']), '=D%d+D%d' % (P['ventas_inv'], P['ventas_ver']),
         negrita=True)
    fila('margen_neto', 'Resultado sobre ventas', ie('B%d/B%d' % (P['resultado'], P['ventas'])),
         ie('C%d/C%d' % (P['resultado'], P['ventas'])), ie('D%d/D%d' % (P['resultado'], P['ventas'])), fmt=PCT,
         nota_txt='Información, no veredicto: el veredicto es el resultado en euros.')
    fila('cont_racion', 'Contribución por ración', ie('B%d/B%d' % (P['contribucion'], P['raciones'])),
         ie('C%d/C%d' % (P['contribucion'], P['raciones'])), ie('D%d/D%d' % (P['contribucion'], P['raciones'])),
         fmt=EUR4)
    fila('res_racion', 'Resultado por ración', ie('B%d/B%d' % (P['resultado'], P['raciones'])),
         ie('C%d/C%d' % (P['resultado'], P['raciones'])), ie('D%d/D%d' % (P['resultado'], P['raciones'])),
         fmt=EUR4)
    fila('caja', 'Caja que genera el negocio antes de la deuda (resultado + amortización + intereses)',
         '=B{r}+B{a}+B{i}'.format(r=P['resultado'], a=P['amort'], i=P['intereses']),
         '=C{r}+C{a}+C{i}'.format(r=P['resultado'], a=P['amort'], i=P['intereses']),
         '=D{r}+D{a}+D{i}'.format(r=P['resultado'], a=P['amort'], i=P['intereses']),
         nota_txt='Con ella se paga la cuota del préstamo (hoja «Financiación»).')
    CC.parrafo(ws, P['nota'],
               'El año 2 es el de crucero: un año entero sin la rampa del arranque. Es el que se cita en '
               'el resumen del plan de negocio y el que decide si el negocio funciona. El año 1 suele '
               'salir peor por la rampa y por la carencia; el año 3 repite el 2 salvo que pongas '
               'crecimiento.', col_ini='A', col_fin='E', alto=44)
    setup(ws, apaisado=True, titulos='%d:%d' % (P['cab'], P['cab']))
    return ws


# ==========================================================================
# Hoja «Punto de Equilibrio»
# ==========================================================================
def hoja_equilibrio(wb):
    ws = wb.create_sheet(H_PEQ)
    cabecera_hoja(ws, 'Punto de Equilibrio en Raciones al Día',
                  'Cuántas raciones al día pagan los fijos del año de crucero, con la contribución media '
                  'por ración de tu carta, y qué meses no llegan.', merge_hasta='I')
    for letra, ancho in (('A', 58), ('B', 16), ('C', 14), ('D', 14), ('E', 14), ('F', 16), ('G', 15),
                         ('H', 16), ('I', 16)):
        ws.column_dimensions[letra].width = ancho
    pyg = lambda clave: ABS_(H_PYG, 'C%d' % P[clave])     # noqa: E731

    def lin(clave, etq, form, fmt=EUR, nota_txt=None, negrita=False):
        return linea(ws, E[clave], etq, form, fmt=fmt, nota_txt=nota_txt, negrita=negrita, col_nota='C')

    seccion(ws, 'A%d' % E['sec_base'], 'Año de Crucero')
    lin('fijos', 'Fijos del año (con amortización e intereses)', '=%s' % pyg('tot_fijos'))
    lin('contribucion', 'Contribución del año', '=%s' % pyg('contribucion'))
    lin('raciones', 'Raciones del año', '=%s' % pyg('raciones'), fmt=ENT)
    lin('cont_racion', 'Contribución media por ración', ie('B%d/B%d' % (E['contribucion'], E['raciones'])),
        fmt=EUR4, nota_txt='Mezcla la carta de invierno, el verano, las ferias y el aceite.')
    lin('dias', 'Días de apertura al año', '=%s' % DIAS_APERTURA, fmt=ENT)
    lin('pe_anio', 'Raciones al año que pagan los fijos', ie('B%d/B%d' % (E['fijos'], E['cont_racion'])),
        fmt=ENT)
    lin('pe_dia', 'PUNTO DE EQUILIBRIO: raciones al día', ie('B%d/B%d' % (E['pe_anio'], E['dias'])), fmt=DEC1,
        negrita=True)
    total(ws, E['pe_dia'], 'AB')
    lin('prev_dia', 'Raciones al día que prevés vender (media del año)', ie('B%d/B%d' % (E['raciones'], E['dias'])),
        fmt=DEC1)
    lin('seg_dia', 'Margen de seguridad (raciones al día por encima del equilibrio)',
        '=B%d-B%d' % (E['prev_dia'], E['pe_dia']), fmt=DEC1)
    motor.semaforo_isnumber(ws, 'B%d' % E['seg_dia'], '$B$%d' % E['seg_dia'], operador='<', umbral='0')
    lin('seg_eur', 'Lo que te sobra (o falta) al año, en euros', '=B%d-B%d' % (E['contribucion'], E['fijos']),
        negrita=True, nota_txt='Es el resultado antes de impuestos del año de crucero.')
    motor.semaforo_isnumber(ws, 'B%d' % E['seg_eur'], '$B$%d' % E['seg_eur'], operador='<', umbral='0')
    ok_e, ko_e = 'Por encima del punto de equilibrio', 'Por debajo del punto de equilibrio'
    lin('veredicto', 'Veredicto', '=IF(NOT(ISNUMBER(B%d)),"",IF(B%d>=0,"%s","%s"))'
        % (E['seg_eur'], E['seg_eur'], ok_e, ko_e), fmt=None, negrita=True)
    motor.semaforo_texto(ws, 'B%d' % E['veredicto'], ((ok_e, motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                                                      (ko_e, motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    lin('pm_mes', 'Contribución que necesitas cada mes para pagar los fijos', ie('B%d/%s' % (E['fijos'], MESES_)))
    lin('ventas_pe_mes', 'Ventas sin IVA al mes en el punto de equilibrio (estimación)',
        ie('B%d/%s*%s/%s' % (E['pe_anio'], MESES_, pyg('ventas'), pyg('raciones'))),
        nota_txt='Con las ventas del año de «PyG 3 Años», que estiman julio y agosto con el ticket de invierno.')
    lin('pe_caja_dia', 'Punto de equilibrio de caja: raciones al día (sin la amortización)',
        ie('(B%d-%s)/B%d/B%d' % (E['fijos'], pyg('amort'), E['cont_racion'], E['dias'])), fmt=DEC1,
        nota_txt='Lo que necesitas para no perder caja, aunque contablemente pierdas dinero.')

    seccion(ws, 'A%d' % E['sec_mes'], 'Mes a Mes del Año de Crucero')
    encabezados(ws, E['cab_mes'], [('A', 'Mes', None), ('B', 'Número del mes', None), ('C', 'Coeficiente', None),
                                   ('D', 'Raciones del mes', None), ('E', 'Raciones al día', None),
                                   ('F', 'Contribución del mes', None), ('G', 'Fijos del mes', None),
                                   ('H', 'Resultado del mes', None), ('I', '¿Paga sus fijos?', None)], alto=36)
    c1 = 'INDEX(%s,%s)' % (COEFS, SB('mes_ver1'))
    c2 = 'INDEX(%s,%s)' % (COEFS, SB('mes_ver2'))
    tmix = ABS_(H_CAN, 'D%d' % K['mix'])
    mmix = ABS_(H_CAN, 'E%d' % K['mix'])
    for m in range(12):
        f = E['mes_ini'] + m
        motor.val(ws, 'A%d' % f, D.MESES[m])
        motor.val(ws, 'B%d' % f, m + 1, fmt=ENT)
        formula(ws, 'C%d' % f, '=%s' % ABS_(H_SUP, 'B%d' % (COEF_INI + m)), fmt=DEC)
        formula(ws, 'D%d' % f, ie('%s*C%d/%s' % (XB('raciones_anio'), f, MESES_)), fmt=ENT)
        formula(ws, 'E%d' % f, ie('D%d/($B$%d/%s)' % (f, E['dias'], MESES_)), fmt=DEC1)
        formula(ws, 'F%d' % f, ie('IF(OR(B{f}={v1},B{f}={v2}),IF({c1}+{c2}>0,{x16}*C{f}/({c1}+{c2}),0),'
                                  'D{f}*({t}-{m}))-D{f}*{rn}+{fe}/{ms}'.format(
                                      f=f, v1=SB('mes_ver1'), v2=SB('mes_ver2'), c1=c1, c2=c2,
                                      x16=XB('_contribucion_verano_elegida'), t=tmix, m=mmix,
                                      rn=XB('renovacion_por_racion'), fe=XB('resultado_anual_ferias'),
                                      ms=MESES_)), fmt=EUR)
        formula(ws, 'G%d' % f, ie('$B$%d/%s' % (E['fijos'], MESES_)), fmt=EUR)
        formula(ws, 'H%d' % f, '=F%d-G%d' % (f, f), fmt=EUR, bold=True)
        formula(ws, 'I%d' % f, '=IF(NOT(ISNUMBER(H%d)),"",IF(H%d>=0,"Sí","No"))' % (f, f))
    motor.semaforo_isnumber(ws, 'H%d:H%d' % (E['mes_ini'], E['mes_fin']), 'H%d' % E['mes_ini'], operador='<',
                            umbral='0')
    motor.semaforo_texto(ws, 'I%d:I%d' % (E['mes_ini'], E['mes_fin']), (
        ('Sí', motor.CF_VERDE_BG, motor.CF_VERDE_FG), ('No', motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    ft = E['mes_tot']
    etiqueta(ws, 'A%d' % ft, 'TOTAL DEL AÑO', negrita=True)
    for col in 'DFGH':
        formula(ws, '%s%d' % (col, ft), '=SUM(%s%d:%s%d)' % (col, E['mes_ini'], col, E['mes_fin']),
                fmt=ENT if col == 'D' else EUR, bold=True)
    total(ws, ft, 'ABCDEFGHI')
    etiqueta(ws, 'A%d' % E['meses_neg'], 'Meses que no pagan sus fijos')
    formula(ws, 'B%d' % E['meses_neg'], '=COUNTIF(H%d:H%d,"<0")' % (E['mes_ini'], E['mes_fin']), fmt=ENT,
            bold=True)
    CC.parrafo(ws, E['nota'],
               'Los meses que no pagan sus fijos los pagan los meses buenos: por eso el fondo de maniobra '
               'tiene que llegar vivo al primer verano. El punto de equilibrio en raciones al día usa la '
               'contribución media de todo el año; en un mes concreto, mira su fila.', col_ini='A',
               col_fin='I', alto=44)
    setup(ws, apaisado=True)
    return ws


# ==========================================================================
# Hoja «Escenarios»
# ==========================================================================
def hoja_escenarios(wb):
    ws = wb.create_sheet(H_ESC)
    cabecera_hoja(ws, 'Escenarios: Raciones, Verano y Formato',
                  'Tres escenarios de raciones sobre el año de crucero, el verano con sus fijos dentro y el '
                  'mismo local con sala o sólo despacho. Todo en euros.', merge_hasta='E')
    for letra, ancho in (('A', 58), ('B', 17), ('C', 17), ('D', 17), ('E', 70)):
        ws.column_dimensions[letra].width = ancho
    pyg = lambda clave: ABS_(H_PYG, 'C%d' % P[clave])     # noqa: E731
    dias = ABS_(H_PEQ, 'B%d' % E['dias'])
    encabezados(ws, X['cab'], [('A', 'Métrica', None), ('B', 'Pesimista', None),
                               ('C', 'Base (año de crucero)', None), ('D', 'Optimista', None),
                               ('E', 'Notas', None)], alto=30)

    def lin(clave, etq, plantilla, fmt=EUR, nota_txt=None, negrita=False):
        f = X[clave]
        etiqueta(ws, 'A%d' % f, etq, negrita=negrita)
        for col in 'BCD':
            formula(ws, '%s%d' % (col, f), plantilla(col), fmt=fmt, bold=negrita or None)
        if nota_txt:
            gris(ws, 'E%d' % f, nota_txt)
        ws.row_dimensions[f].height = 30
        if negrita:
            total(ws, f, 'ABCD')

    etiqueta(ws, 'A%d' % X['var'], 'Raciones sobre el año normal')
    formula(ws, 'B%d' % X['var'], '=%s' % SB('var_pes'), fmt=PCT)
    motor.val(ws, 'C%d' % X['var'], 0, fmt=PCT)
    formula(ws, 'D%d' % X['var'], '=%s' % SB('var_opt'), fmt=PCT)
    gris(ws, 'E%d' % X['var'], 'Se cambian en «0. Supuestos». La base no se mueve: es el año de crucero.')
    lin('raciones', 'Raciones del año', lambda c: '=%s*(1+%s%d)' % (pyg('raciones'), c, X['var']), fmt=ENT)
    lin('cont_var', 'Contribución que depende de las raciones',
        lambda c: '=(%s-%s)*(1+%s%d)' % (pyg('contribucion'), pyg('ferias'), c, X['var']),
        nota_txt='Carta, verano y aceite se mueven con las raciones; las ferias, no.')
    lin('ferias', 'Ferias', lambda c: '=%s' % pyg('ferias'))
    lin('contribucion', 'CONTRIBUCIÓN DEL AÑO', lambda c: '=%s%d+%s%d' % (c, X['cont_var'], c, X['ferias']),
        negrita=True)
    lin('fijos', 'Fijos del año (los mismos en los tres)', lambda c: '=%s' % pyg('tot_fijos'),
        nota_txt='Si en el pesimista no aguantas, el ajuste es la plantilla o la renta, no las raciones.')
    lin('resultado', 'RESULTADO ANTES DE IMPUESTOS', lambda c: '=%s%d-%s%d' % (c, X['contribucion'], c, X['fijos']),
        negrita=True)
    motor.semaforo_isnumber(ws, 'B%d:D%d' % (X['resultado'], X['resultado']), 'B%d' % X['resultado'],
                            operador='<', umbral='0')
    lin('lectura', '¿Gana dinero?', lambda c: '=IF(NOT(ISNUMBER({c}{r})),"",IF({c}{r}>=0,"Gana dinero",'
        '"Pierde dinero"))'.format(c=c, r=X['resultado']), fmt=None, negrita=True)
    motor.semaforo_texto(ws, 'B%d:D%d' % (X['lectura'], X['lectura']), (
        ('Gana dinero', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
        ('Pierde dinero', motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    lin('pe_dia', 'Raciones al día que pagan los fijos',
        lambda c: ie('IF({c}{k}<=0,"",{c}{f}/({c}{k}/{c}{r})/{d})'.format(
            c=c, k=X['contribucion'], f=X['fijos'], r=X['raciones'], d=dias)), fmt=DEC1)
    lin('prev_dia', 'Raciones al día que vendes', lambda c: ie('%s%d/%s' % (c, X['raciones'], dias)), fmt=DEC1)
    lin('seg_dia', 'Margen de seguridad (raciones al día)',
        lambda c: ie('%s%d-%s%d' % (c, X['prev_dia'], c, X['pe_dia'])), fmt=DEC1)

    # --- verano con fijos ----------------------------------------------------------
    seccion(ws, 'A%d' % X['sec_ver'], 'El Verano con los Fijos Dentro (Julio y Agosto)')
    encabezados(ws, X['cab_ver'], [('A', 'Salida del verano', None),
                                   ('B', 'Contribución de julio y agosto', None),
                                   ('C', 'Fijos de esos dos meses', None), ('D', 'Resultado con fijos', None),
                                   ('E', 'Notas', None)], alto=36)
    etiqueta(ws, 'A%d' % X['meses_ver'], 'Meses del verano')
    formula(ws, 'B%d' % X['meses_ver'], '=COUNT(%s:%s)' % (SB('mes_ver1'), SB('mes_ver2').split('!')[1]), fmt=ENT)
    etiqueta(ws, 'A%d' % X['fijos_ver'], 'Fijos de esos meses (los mismos en las tres salidas)')
    formula(ws, 'B%d' % X['fijos_ver'], ie('%s*B%d/%s' % (pyg('tot_fijos'), X['meses_ver'], MESES_)), fmt=EUR,
            bold=True)
    gris(ws, 'E%d' % X['fijos_ver'], 'Plantilla, renta, gastos fijos, amortización e intereses de dos meses '
                                     'del año de crucero. Se pagan abras o cierres.')
    filas_v = ((X['cerrar'], 'Cerrar en julio y agosto', '=%s' % XB('_contribucion_verano_cerrar'),
                'Contribución cero por definición: no vendes, pero pagas los fijos.'),
               (X['carta'], 'Abrir con la carta de verano', '=%s' % XB('_contribucion_verano_carta'),
                'Ventas menos materia de julio y agosto, del libro 5.'),
               (X['ferias'], 'Salir de ferias en julio y agosto', '=%s' % XB('_contribucion_verano_ferias'),
                'Lo que dejan las ferias de esos dos meses, del libro 5.'),
               (X['elegida'], 'La salida que eliges en el libro 5 (su contribución, X16)',
                '=%s' % XB('_contribucion_verano_elegida'),
                'En El Molinete, la carta de verano. Es una de las tres de arriba.'))
    for f, etq, form_b, nota_txt in filas_v:
        etiqueta(ws, 'A%d' % f, etq)
        formula(ws, 'B%d' % f, form_b, fmt=EUR)
        formula(ws, 'C%d' % f, '=$B$%d' % X['fijos_ver'], fmt=EUR)
        formula(ws, 'D%d' % f, '=B%d-C%d' % (f, f), fmt=EUR, bold=True)
        gris(ws, 'E%d' % f, nota_txt)
        ws.row_dimensions[f].height = 30
    motor.semaforo_isnumber(ws, 'D%d:D%d' % (X['cerrar'], X['elegida']), 'D%d' % X['cerrar'], operador='<',
                            umbral='0')
    ws.row_dimensions[X['elegida']].height = 30
    etiqueta(ws, 'A%d' % X['dif_ver'], 'Lo que te deja la salida elegida frente a cerrar', negrita=True)
    formula(ws, 'B%d' % X['dif_ver'], '=D%d-D%d' % (X['elegida'], X['cerrar']), fmt=EUR, bold=True)
    crema(ws['B%d' % X['dif_ver']])
    CC.parrafo(ws, X['nota_ver'],
               'Un verano con resultado negativo es lo normal en una churrería: lo que decide es cuánto '
               'menos negativo es abrir que cerrar. Las tres salidas se enseñan aquí con la misma regla: su '
               'contribución (la copias del libro 5) menos los «Fijos de esos meses». El libro 5, en «El '
               'Verano (Tres Salidas)», compara las tres sin fijos y elige la que más deja.',
               col_ini='A', col_fin='E', alto=44)

    # --- local con sala o sólo despacho ------------------------------------------------
    seccion(ws, 'A%d' % X['sec_fmt'], 'Local con Sala o Sólo Despacho para Llevar')
    encabezados(ws, X['cab_fmt'], [('A', 'Métrica', None), ('B', 'Local con sala (el caso)', None),
                                   ('C', 'Sólo despacho para llevar', None), ('D', '', None),
                                   ('E', 'Notas', None)], alto=36)
    llevar = ABS_(H_CAN, 'B%d' % K['llevar'])
    filas_f = [
        ('f_pct', 'Parte de las raciones que conservas', '=%s+%s' % (ABS_(H_CAN, 'B%d' % K['sala']), llevar),
         '=%s' % llevar, PCT, 'Sin sala, el mismo local vende sólo la parte que ya se llevaban.'),
        ('f_rac', 'Raciones del año', '=%s' % pyg('raciones'), '=%s*%s' % (pyg('raciones'), llevar), ENT, None),
        ('f_carta', 'Contribución de la carta de invierno', '=%s' % ABS_(H_CAN, 'G%d' % K['mix']),
         '=%s' % ABS_(H_CAN, 'G%d' % K['llevar']), EUR, None),
        ('f_verano', 'Contribución de julio y agosto', '=%s' % pyg('cont_verano'),
         '=%s*%s' % (pyg('cont_verano'), llevar), EUR, 'En el despacho, la parte para llevar del verano.'),
        ('f_renov', 'Renovación del aceite (se resta)', '=%s' % pyg('renov'), '=%s*%s' % (pyg('renov'), llevar),
         EUR, None),
        ('f_ferias', 'Ferias', '=%s' % pyg('ferias'), '=%s' % pyg('ferias'), EUR,
         'Las ferias no dependen de tener sala.'),
    ]
    for clave, etq, fb, fc, fmt, nota_txt in filas_f:
        f = X[clave]
        etiqueta(ws, 'A%d' % f, etq)
        formula(ws, 'B%d' % f, fb, fmt=fmt)
        formula(ws, 'C%d' % f, fc, fmt=fmt)
        if nota_txt:
            gris(ws, 'E%d' % f, nota_txt)
    f = X['f_cont']
    etiqueta(ws, 'A%d' % f, 'CONTRIBUCIÓN DEL AÑO', negrita=True)
    for col in 'BC':
        formula(ws, '%s%d' % (col, f), '={c}{a}+{c}{b}-{c}{r}+{c}{e}'.format(
            c=col, a=X['f_carta'], b=X['f_verano'], r=X['f_renov'], e=X['f_ferias']), fmt=EUR, bold=True)
    total(ws, f, 'ABC')
    f = X['f_fijos']
    etiqueta(ws, 'A%d' % f, 'Fijos del año')
    formula(ws, 'B%d' % f, '=%s' % pyg('tot_fijos'), fmt=EUR)
    formula(ws, 'C%d' % f, '=%s-%s' % (pyg('tot_fijos'), SB('ahorro_desp')), fmt=EUR)
    gris(ws, 'E%d' % f, 'El despacho resta el ahorro que pongas en «0. Supuestos» (a cero, los mismos fijos).')
    f = X['f_res']
    etiqueta(ws, 'A%d' % f, 'RESULTADO ANTES DE IMPUESTOS', negrita=True)
    for col in 'BC':
        formula(ws, '%s%d' % (col, f), '=%s%d-%s%d' % (col, X['f_cont'], col, X['f_fijos']), fmt=EUR, bold=True)
    total(ws, f, 'ABC')
    motor.semaforo_isnumber(ws, 'B%d:C%d' % (f, f), 'B%d' % f, operador='<', umbral='0')
    f = X['f_lectura']
    etiqueta(ws, 'A%d' % f, '¿Gana dinero?', negrita=True)
    for col in 'BC':
        formula(ws, '%s%d' % (col, f), '=IF(NOT(ISNUMBER({c}{r})),"",IF({c}{r}>=0,"Gana dinero",'
                '"Pierde dinero"))'.format(c=col, r=X['f_res']), bold=True)
    motor.semaforo_texto(ws, 'B%d:C%d' % (f, f), (
        ('Gana dinero', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
        ('Pierde dinero', motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
    f = X['f_ahorro']
    etiqueta(ws, 'A%d' % f, 'Ahorro de fijos al año que necesitaría el despacho para no perder dinero')
    formula(ws, 'C%d' % f, '=MAX(0,C%d-C%d)' % (X['f_fijos'], X['f_cont']), fmt=EUR, bold=True)
    crema(ws['C%d' % f])
    gris(ws, 'E%d' % f, 'Si un despacho más pequeño (menos renta, menos plantilla) no consigue ahorrarte esto, '
                        'la sala es la que paga el negocio.')
    CC.parrafo(ws, X['nota'],
               'El despacho de esta hoja es el MISMO local vendiendo sólo para llevar. Un despacho de verdad '
               'es otro local, con otra renta y otro CAPEX (libro 2, «Variante del Formato»): para '
               'estudiarlo, haz una copia de este libro con sus cifras.', col_ini='A', col_fin='E', alto=44)
    setup(ws, apaisado=True)
    return ws


# ==========================================================================
# Hoja «Personal»
# ==========================================================================
def hoja_personal(wb):
    ws = wb.create_sheet(H_PER)
    cabecera_hoja(ws, 'Personal: lo que Pesa la Plantilla',
                  'El coste de la plantilla llega del libro 8, que es donde viven el convenio, el suelo '
                  'del SMI y las dos figuras de nocturnidad. Aquí sólo se mide lo que pesa en el negocio.',
                  merge_hasta='C')
    for letra, ancho in (('A', 62), ('B', 18), ('C', 76)):
        ws.column_dimensions[letra].width = ancho
    pyg = lambda clave: ABS_(H_PYG, 'C%d' % P[clave])     # noqa: E731

    def lin(clave, etq, form, fmt=EUR, nota_txt=None, negrita=False):
        return linea(ws, R[clave], etq, form, fmt=fmt, nota_txt=nota_txt, negrita=negrita, col_nota='C')

    seccion(ws, 'A%d' % R['sec'], 'Año de Crucero')
    cel = lin('plantilla', 'Coste anual de la plantilla (libro 8)', '=%s' % XB('coste_plantilla_anual'),
              nota_txt='Con la Seguridad Social de empresa, el refuerzo de Navidad y Reyes y las '
                       'sustituciones de vacaciones. Coste por puesto = el mayor entre su salario y el SMI.')
    nota_legal(ws, cel.coordinate, 'CHN-67', extra='El suelo del SMI se aplica en el libro 8.')
    lin('autonomos', 'Cuota de autónomos del titular (de los gastos fijos)',
        '=%s*%s' % (SB('gf_%02d' % I_AUTONOMOS), MESES_),
        nota_txt='El titular está en la plantilla como un puesto más: aquí sólo va su cuota.')
    lin('personas', 'COSTE TOTAL DE LAS PERSONAS', '=B%d+B%d' % (R['plantilla'], R['autonomos']), negrita=True)
    total(ws, R['personas'], 'AB')
    lin('mes', 'Al mes', ie('B%d/%s' % (R['personas'], MESES_)))
    lin('racion', 'Por ración vendida', ie('B%d/%s' % (R['personas'], pyg('raciones'))), fmt=EUR4)
    lin('sobre_ventas', 'Sobre las ventas del año (estimación)', ie('B%d/%s' % (R['personas'], pyg('ventas'))),
        fmt=PCT, nota_txt='Información, no veredicto.')
    lin('sobre_cont', 'Sobre la contribución del año', ie('B%d/%s' % (R['personas'], pyg('contribucion'))),
        fmt=PCT, nota_txt='Qué parte de lo que deja la carta se va en personas.')
    lin('rac_dia', 'Raciones al día que hacen falta sólo para pagar a las personas',
        ie('B%d/%s/%s' % (R['personas'], ABS_(H_PEQ, 'B%d' % E['cont_racion']), ABS_(H_PEQ, 'B%d' % E['dias']))),
        fmt=DEC1, negrita=True)
    seccion(ws, 'A%d' % R['sec_frontera'], 'Lo que Este Libro No Hace')
    CC.parrafo(ws, R['frontera'],
               'No reproduce el cuadrante semanal por empleado ni las nóminas: el libro 8 calcula las horas '
               'por franja, las dos figuras de nocturnidad (el trabajador nocturno del Estatuto y el plus '
               'del convenio) y el coste anual por puesto. Para el cuadrante semana a semana, el Kit de '
               'Gestión de Personal de aichef.pro.', col_ini='A', col_fin='C', alto=58)
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
                  H_SUP, 'B%d' % CRUCE_ROW[clave], 'entrada'))
    m += [
        ('Gastos fijos del mes, sin renta ni plantilla', H_SUP, 'B%d' % S['gf_total'], 'salida'),
        ('Meses de colchón del fondo de maniobra', H_SUP, 'B%d' % S['colchon'], 'parametro'),
        ('Préstamo bancario que se pide', H_SUP, 'B%d' % S['principal'], 'entrada'),
        ('Tipo de interés nominal anual', H_SUP, 'B%d' % S['tipo'], 'parametro'),
        ('Plazo del préstamo en meses', H_SUP, 'B%d' % S['plazo'], 'parametro'),
        ('Carencia del préstamo en meses', H_SUP, 'B%d' % S['carencia'], 'parametro'),
        ('Ventas del primer mes sobre un mes normal (rampa)', H_SUP, 'B%d' % S['rampa1'], 'parametro'),
        ('Cuota de autónomos del titular al mes', H_SUP, 'B%d' % S['gf_%02d' % I_AUTONOMOS], 'entrada'),
        ('Amortización anual', H_INV, 'B%d' % IV['amort'], 'salida'),
        ('Fijos de caja de un mes', H_INV, 'B%d' % IV['fijos_caja'], 'salida'),
        ('Fondo de maniobra', H_INV, 'B%d' % IV['fondo'], 'salida'),
        ('Inversión total (CAPEX más fondo de maniobra)', H_INV, 'B%d' % IV['inversion'], 'salida'),
        ('Recursos propios que pone el promotor', H_INV, 'B%d' % IV['propios'], 'salida'),
        ('Raciones del año 1 (con rampa)', H_PYG, 'B%d' % P['raciones'], 'salida'),
        ('Contribución del año 1', H_PYG, 'B%d' % P['contribucion'], 'salida'),
        ('Resultado antes de impuestos del año 1', H_PYG, 'B%d' % P['resultado'], 'salida'),
        ('Ventas sin IVA de la carta de invierno, año de crucero', H_PYG, 'C%d' % P['ventas_inv'], 'salida'),
        ('Contribución de la carta de invierno, año de crucero', H_PYG, 'C%d' % P['cont_carta'], 'salida'),
        ('Contribución del año de crucero', H_PYG, 'C%d' % P['contribucion'], 'salida'),
        ('Costes fijos del año de crucero', H_PYG, 'C%d' % P['tot_fijos'], 'salida'),
        ('Intereses del año de crucero', H_PYG, 'C%d' % P['intereses'], 'salida'),
        ('Resultado antes de impuestos del año de crucero', H_PYG, 'C%d' % P['resultado'], 'salida'),
        ('Lectura del año de crucero (gana o pierde)', H_PYG, 'C%d' % P['lectura'], 'salida'),
        ('Ventas sin IVA del año de crucero (verano estimado)', H_PYG, 'C%d' % P['ventas'], 'salida'),
        ('Resultado sobre ventas del año de crucero', H_PYG, 'C%d' % P['margen_neto'], 'salida'),
        ('Contribución por ración, año de crucero', H_PYG, 'C%d' % P['cont_racion'], 'salida'),
        ('Resultado antes de impuestos del año 3', H_PYG, 'D%d' % P['resultado'], 'salida'),
        ('Punto de equilibrio en raciones al año', H_PEQ, 'B%d' % E['pe_anio'], 'salida'),
        ('Punto de equilibrio en raciones al día', H_PEQ, 'B%d' % E['pe_dia'], 'salida'),
        ('Raciones al día previstas (media del año)', H_PEQ, 'B%d' % E['prev_dia'], 'salida'),
        ('Margen de seguridad en raciones al día', H_PEQ, 'B%d' % E['seg_dia'], 'salida'),
        ('Contribución mensual que pagan los fijos', H_PEQ, 'B%d' % E['pm_mes'], 'salida'),
        ('Punto de equilibrio de caja en raciones al día', H_PEQ, 'B%d' % E['pe_caja_dia'], 'salida'),
        ('Meses del año de crucero que no pagan sus fijos', H_PEQ, 'B%d' % E['meses_neg'], 'salida'),
        ('Resultado de agosto en el año de crucero', H_PEQ, 'H%d' % (E['mes_ini'] + 7), 'salida'),
        ('Resultado del escenario pesimista', H_ESC, 'B%d' % X['resultado'], 'salida'),
        ('Resultado del escenario optimista', H_ESC, 'D%d' % X['resultado'], 'salida'),
        ('Fijos de julio y agosto', H_ESC, 'B%d' % X['fijos_ver'], 'salida'),
        ('Verano con fijos si se cierra', H_ESC, 'D%d' % X['cerrar'], 'salida'),
        ('Verano con fijos con la carta de verano', H_ESC, 'D%d' % X['carta'], 'salida'),
        ('Verano con fijos saliendo de ferias', H_ESC, 'D%d' % X['ferias'], 'salida'),
        ('Verano con fijos de la salida elegida', H_ESC, 'D%d' % X['elegida'], 'salida'),
        ('Lo que deja la salida elegida frente a cerrar', H_ESC, 'B%d' % X['dif_ver'], 'salida'),
        ('Resultado del mismo local sólo como despacho', H_ESC, 'C%d' % X['f_res'], 'salida'),
        ('Ahorro de fijos que necesitaría el despacho para no perder', H_ESC, 'C%d' % X['f_ahorro'], 'salida'),
        ('Coste total de las personas', H_PER, 'B%d' % R['personas'], 'salida'),
        ('Raciones al día sólo para pagar a las personas', H_PER, 'B%d' % R['rac_dia'], 'salida'),
        ('Saldo de caja el día que se abre', H_TES, 'B%d' % T['saldo_ini'], 'salida'),
        ('Valle de tesorería del año 1', H_TES, 'B%d' % T['valle'], 'salida'),
        ('Mes del valle de tesorería', H_TES, 'B%d' % T['mes_valle'], 'salida'),
        ('Lectura del valle (aguanta o no el fondo)', H_TES, 'B%d' % T['veredicto'], 'salida'),
        ('Saldo de caja al cierre del año 1', H_TES, 'M%d' % T['saldo'], 'salida'),
        ('Préstamo que pide la estructura', H_FIN, 'B%d' % F['pide'], 'salida'),
        ('Comprobación del punto fijo del préstamo', H_FIN, 'B%d' % F['punto_fijo'], 'salida'),
        ('Cuota mensual del préstamo', H_FIN, 'B%d' % F['cuota'], 'salida'),
        ('Servicio de la deuda del año 2', H_FIN, 'D%d' % (F_ANIO_INI + 1), 'salida'),
        ('Lo que sobra en el peor año del préstamo', H_FIN, 'B%d' % F_PEOR, 'salida'),
        ('Lectura del banco (aguanta o no)', H_FIN, 'B%d' % F_AGUANTA, 'salida'),
        ('DSCR más bajo', H_FIN, 'B%d' % F_DSCR_MIN, 'salida'),
        ('Ticket medio sin IVA de la carta de invierno', H_CAN, 'D%d' % K['mix'], 'salida'),
        ('Materia media por ración de la carta de invierno', H_CAN, 'E%d' % K['mix'], 'salida'),
        ('Contribución de la sala en el año de crucero', H_CAN, 'G%d' % K['sala'], 'salida'),
        ('Contribución del para llevar en el año de crucero', H_CAN, 'G%d' % K['llevar'], 'salida'),
        ('La sala menos los fijos del año', H_CAN, 'C%d' % K['f_sala'], 'salida'),
        ('Lectura de la sala frente a los fijos', H_CAN, 'D%d' % K['f_sala'], 'salida'),
        ('Canal que más deja', H_CAN, 'B%d' % K['quien'], 'salida'),
    ]
    return m


# ==========================================================================
# Cierre: guardar, cachear, verificar, cruces, lista negra y mapa
# ==========================================================================
_PROHIBIDAS = ('INDIRECT', 'COUNTA', 'PMT(', 'OFFSET', 'XLOOKUP', 'LET(', 'LAMBDA', 'RANK(',
               'NETWORKDAYS', 'IRR(')
RX_CONST_DEC = re.compile(r'[*/]\s*\d{1,3}[.,]\d{1,4}(?!\d)')
#: Enteros que pueden ir en una fórmula: el cero y el uno («uno menos», «más uno») y el
#: dos de ROUND(x,2) en el cierre del cuadro (redondeo al céntimo). Cualquier otro número
#: tecleado aborta: los doce meses salen de COUNT y todo lo demás de «0. Supuestos».
_ENTEROS_OK = {'0', '1'}
_RX_NUM = re.compile(r'(?<![A-Z$0-9.])(\d+(?:\.\d+)?)(?![0-9]*[(!])')
_RX_ROUND_CENT = re.compile(r',2\)\)$')


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
    for donde, txt, _es_formula in _textos(wbf):
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
    if fallos:
        raise SystemExit('LISTA NEGRA / IDS PROHIBIDOS en %s:\n  %s' % (NOMBRE, '\n  '.join(fallos[:40])))


def _gate_cruces(wbf, wbv):
    if D._ERROR_CRUCES:
        raise SystemExit('datos_ejemplo no pudo calcular los cruces: %s' % D._ERROR_CRUCES)
    fallos = []
    if len(CRUCE_VERDES) != len(CRUCES_IN) or len(CRUCE_CUADRES) != len(CRUCES_IN):
        fallos.append('%d cruces, %d verdes de cruce y %d filas de CUADRE'
                      % (len(CRUCES_IN), len(CRUCE_VERDES), len(CRUCE_CUADRES)))
    n_cuadre = sum(1 for r in wbf[H_SUP].iter_rows(min_col=1, max_col=1)
                   for c in r if isinstance(c.value, str) and c.value.startswith('CUADRE'))
    if n_cuadre != len(CRUCES_IN):
        fallos.append('%d filas que empiezan por CUADRE y %d celdas cruzadas' % (n_cuadre, len(CRUCES_IN)))
    for c in CRUCES_IN:
        fila = CRUCE_ROW[c['calcula']]
        cel_v = wbf[H_SUP]['B%d' % fila]
        if not motor.es_verde(cel_v) or cel_v.protection.locked:
            fallos.append('%s: 0. Supuestos!B%d no es verde y editable' % (c['x'], fila))
        if wbf[H_SUP]['D%d' % fila].value != D.rotulo_cruce(c):
            fallos.append('%s: 0. Supuestos!D%d no lleva el rótulo %r' % (c['x'], fila, D.rotulo_cruce(c)))
        v = wbv[H_SUP]['B%d' % fila].value
        esperado = c['valor_defecto']
        if ETIQUETA_CRUCE[c['calcula']][2] == ENT:
            esperado = int(round(esperado))
        if not isinstance(v, (int, float)) or abs(v - esperado) > max(1e-9, abs(esperado) * 1e-9):
            fallos.append('%s: 0. Supuestos!B%d = %r y datos_ejemplo dice %r' % (c['x'], fila, v, esperado))
        fc = CUADRE_ROW[c['calcula']]
        if wbv[H_SUP]['D%d' % fc].value != 'CUADRA':
            fallos.append('%s: con los datos de El Molinete el CUADRE de la fila %d dice %r'
                          % (c['x'], fc, wbv[H_SUP]['D%d' % fc].value))
    for ws in wbf.worksheets:
        if ws.title == H_SUP:
            continue
        for row in ws.iter_rows():
            for cel in row:
                if isinstance(cel.value, str) and 'cópialo del libro' in cel.value:
                    fallos.append('%s!%s: rótulo de cruce fuera de «0. Supuestos»' % (ws.title, cel.coordinate))
    if fallos:
        raise SystemExit('CRUCES ROTOS en %s:\n  %s' % (NOMBRE, '\n  '.join(fallos)))
    return len(CRUCES_IN)


def _python_anio1():
    """Espejo en Python de la hoja de Tesorería (año 1), para el gate contra datos."""
    R_ = D.raciones_anio()
    coef = D.COEFICIENTES_MES
    rampa = D.rampa_mensual()
    pct = D._pct_sala() / 100.0
    tmix = pct * D._ticket_sala() + (1 - pct) * D._ticket_llevar()
    mmix = pct * D._materia_sala() + (1 - pct) * D._materia_llevar()
    v1, v2 = D.MESES_VERANO
    x16 = D._contribucion_verano_elegida()
    x14 = D.resultado_anual_ferias()
    cuadro = D.cuadro_frances()
    fijos_mes = D.coste_plantilla_anual() / 12.0 + D._renta() + D.gastos_fijos_mes()
    saldo = (D.inversion_total() - D.principal_prestamo()) + D.principal_prestamo() - D.capex_total()
    raciones = contribucion = 0.0
    saldos = []
    for k in range(12):
        mes = (D.dato(D.NEGOCIO, 'mes_apertura') - 1 + k) % 12 + 1
        c = coef[mes - 1]
        rac = R_ * c / 12.0 * rampa[k]
        ver = mes in (v1, v2)
        cont = (0.0 if ver else rac * (tmix - mmix))
        cont += (x16 * c / (coef[v1 - 1] + coef[v2 - 1]) * rampa[k]) if ver else 0.0
        cont += -rac * D.renovacion_por_racion() + x14 / 12.0
        raciones += rac
        contribucion += cont
        _m, _s, interes, amort, _q = cuadro[k]
        saldo += cont - fijos_mes - interes - amort
        saldos.append(saldo)
    return {'raciones': raciones, 'contribucion': contribucion, 'valle': min(saldos),
            'saldo_12': saldos[-1], 'tmix': tmix, 'mmix': mmix}


def _gate_contra_datos(wbv):
    pyg = D.cuenta_resultados_crucero()
    a1 = _python_anio1()
    rac_inv = sum(D.raciones_mes(m) for m in range(1, 13) if m not in D.MESES_VERANO)
    pares = [
        ('CAPEX', wbv[H_INV]['B%d' % IV['capex']].value, D.capex_total()),
        ('CAPEX amortizable', wbv[H_INV]['B%d' % IV['amortizable']].value, D.capex_amortizable()),
        ('amortización anual', wbv[H_INV]['B%d' % IV['amort']].value, D.amortizacion_anual()),
        ('fondo de maniobra', wbv[H_INV]['B%d' % IV['fondo']].value, D.fondo_maniobra()),
        ('inversión total', wbv[H_INV]['B%d' % IV['inversion']].value, D.inversion_total()),
        ('préstamo que pide la estructura', wbv[H_FIN]['B%d' % F['pide']].value, D.principal_prestamo()),
        ('gastos fijos del mes', wbv[H_SUP]['B%d' % S['gf_total']].value, D.gastos_fijos_mes()),
        ('contribución del crucero', wbv[H_PYG]['C%d' % P['contribucion']].value, pyg['contribucion']),
        ('fijos del crucero', wbv[H_PYG]['C%d' % P['tot_fijos']].value, pyg['fijos']),
        ('resultado del crucero', wbv[H_PYG]['C%d' % P['resultado']].value, pyg['beneficio']),
        ('raciones de la carta de invierno', wbv[H_PYG]['C%d' % P['rac_inv']].value, rac_inv),
        ('ventas de la carta de invierno', wbv[H_PYG]['C%d' % P['ventas_inv']].value,
         rac_inv * D.ticket_sin_iva('invierno')),
        ('punto de equilibrio (raciones al día)', wbv[H_PEQ]['B%d' % E['pe_dia']].value,
         D.punto_equilibrio_raciones_dia()),
        ('resultado mes a mes (suma)', wbv[H_PEQ]['H%d' % E['mes_tot']].value, pyg['beneficio']),
        ('contribución por canales', wbv[H_CAN]['G%d' % K['total']].value, pyg['contribucion']),
        ('ticket medio de invierno', wbv[H_CAN]['D%d' % K['mix']].value, D.ticket_sin_iva('invierno')),
        ('materia media de invierno', wbv[H_CAN]['E%d' % K['mix']].value, D.materia_por_racion('invierno')),
        ('verano con fijos: cerrar', wbv[H_ESC]['D%d' % X['cerrar']].value, D.verano_con_fijos('cerrar')),
        ('verano con fijos: salida elegida', wbv[H_ESC]['D%d' % X['elegida']].value,
         D.verano_con_fijos(D.SALIDA_VERANO_ELEGIDA)),
        ('verano con fijos: carta de verano', wbv[H_ESC]['D%d' % X['carta']].value,
         D.verano_con_fijos('carta de verano')),
        ('verano con fijos: ferias', wbv[H_ESC]['D%d' % X['ferias']].value, D.verano_con_fijos('ferias')),
        ('ventas sin IVA del año de crucero (R-13: el verano con su ticket)',
         wbv[H_PYG]['C%d' % P['ventas']].value, pyg['ventas']),

        ('raciones del año 1', wbv[H_PYG]['B%d' % P['raciones']].value, a1['raciones']),
        ('contribución del año 1', wbv[H_PYG]['B%d' % P['contribucion']].value, a1['contribucion']),
        ('valle del año 1', wbv[H_TES]['B%d' % T['valle']].value, a1['valle']),
        ('saldo al cierre del año 1', wbv[H_TES]['M%d' % T['saldo']].value, a1['saldo_12']),
    ]
    for k in (1, 2, 3):
        pares.append(('intereses del año %d' % k, wbv[H_FIN]['B%d' % (F_ANIO_INI + k - 1)].value,
                      D.intereses_anio(k)))
    fallos = ['%s: libro %r, datos_ejemplo %r' % (n, v, e) for n, v, e in pares
              if not isinstance(v, (int, float)) or abs(v - e) > max(0.005, abs(e) * 1e-9)]
    if not str(wbv[H_FIN]['B%d' % F['punto_fijo']].value or '').startswith('Cerrado'):
        fallos.append('el punto fijo del préstamo dice %r' % wbv[H_FIN]['B%d' % F['punto_fijo']].value)
    if wbv[H_FIN]['B%d' % F_CIERRA].value != 'Sí':
        fallos.append('el cuadro de amortización no cierra')
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
    if set(wb.sheetnames) != set(D.HOJAS[LIBRO]) or len(wb.sheetnames) != len(D.HOJAS[LIBRO]):
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
        limpio = re.sub(r'\$?[A-Z]{1,2}\$?\d+', '', sin_refs)
        if _RX_ROUND_CENT.search(limpio) and 'ROUND(' in limpio:
            limpio = _RX_ROUND_CENT.sub('))', limpio)
        for m in _RX_NUM.finditer(limpio):
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
        import logging
        logging.disable(logging.CRITICAL)
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
            if dv.type == 'list':
                sin_dv.append('%s: DV de lista en el libro 6 (%s)' % (ws.title, dv.formula1))
            for rng in str(dv.sqref).split():
                for fila in ws[rng] if ':' in rng else [[ws[rng]]]:
                    for cel in fila:
                        cubiertas.add(cel.coordinate)
        for row in ws.iter_rows():
            for c in row:
                if (c.__class__.__name__ != 'MergedCell' and motor.es_verde(c)
                        and c.coordinate not in cubiertas and isinstance(c.value, (int, float))):
                    sin_dv.append('%s!%s verde sin validación' % (ws.title, c.coordinate))
    if sin_dv:
        raise SystemExit('VALIDACIÓN DE DATOS:\n  ' + '\n  '.join(sin_dv))

    _gate_lista_negra(wbf)
    n_cruces = _gate_cruces(wbf, wbv)
    contra_datos = _gate_contra_datos(wbv)

    requeridos = [i for i, (_t, libros) in D.IDS_LEGALES_REQUERIDOS.items() if LIBRO in libros]
    puestos = set(pid for _h, _c, pid in NOTAS_LEGALES)
    faltan = [i for i in requeridos if i not in puestos]
    if faltan:
        raise SystemExit('Faltan notas legales del libro 6: %s' % ', '.join(faltan))

    mapa = {}
    for etq, hoja, coord, tipo in mapa_celdas_:
        if tipo not in ('entrada', 'salida', 'parametro'):
            raise SystemExit('Tipo de mapa no válido: %r' % tipo)
        v = wbv[hoja][coord].value
        if v is None or (isinstance(v, str) and not v.strip()):
            raise SystemExit('El mapa cita %s!%s («%s») y está VACÍA' % (hoja, coord, etq))
        if etq in mapa:
            raise SystemExit('Etiqueta de mapa repetida: %r' % etq)
        mapa[etq] = {'ref': '%s!%s!%s' % (FICHERO, hoja, coord), 'valor': v, 'tipo': tipo}
    if len(mapa) < 25:
        raise SystemExit('El mapa tiene %d etiquetas y el mínimo es 25' % len(mapa))
    for c in CRUCES_IN:
        ref = '%s!%s!B%d' % (FICHERO, H_SUP, CRUCE_ROW[c['calcula']])
        if not any(d['ref'] == ref for d in mapa.values()):
            raise SystemExit('El mapa no cita la celda receptora del cruce %s (%s)' % (c['x'], ref))
    with open(os.path.join(destino, 'mapa-' + NOMBRE + '.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(mapa, ensure_ascii=False, indent=1))

    return {'ruta': ruta, 'hojas': len(wbf.worksheets), 'formulas': len(motor.REGISTRO),
            'sin_dato': len(sin_dato), 'verdes': n_verdes, 'verdes_vacias': verdes_vacias,
            'notas_legales': len(NOTAS_LEGALES), 'notas_sector': len(NOTAS_SECTOR), 'mapa': len(mapa),
            'contra_datos': contra_datos, 'cruces_in': n_cruces, 'cuadres': len(CRUCE_CUADRES),
            'cache': (salida_cache.strip().splitlines() or [''])[-1]}


# ==========================================================================
# Demostraciones con pycel
# ==========================================================================
def demo(ruta):
    import logging
    logging.disable(logging.CRITICAL)
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

    res_c = 'C%d' % P['resultado']
    pe = 'B%d' % E['pe_dia']

    # 1. Subir la renta (X18, del libro 2) de 910 a 1.200 €/mes: el resultado del crucero
    #    baja 12 x 290 €, el punto de equilibrio sube y el CUADRE de la renta avisa.
    xl = nuevo()
    r0, p0 = ev(xl, H_PYG, res_c), ev(xl, H_PEQ, pe)
    fc = CUADRE_ROW['_renta']
    q0 = ev(xl, H_SUP, 'D%d' % fc)
    f0 = ev(xl, H_INV, 'B%d' % IV['fondo'])
    pon(xl, H_SUP, 'B%d' % CRUCE_ROW['_renta'], 1200.0)
    r1, p1, q1 = ev(xl, H_PYG, res_c), ev(xl, H_PEQ, pe), ev(xl, H_SUP, 'D%d' % fc)
    f1 = ev(xl, H_INV, 'B%d' % IV['fondo'])
    prueba('renta de 910 a 1.200 €/mes: el resultado baja 3.480 €, el equilibrio sube, el fondo sube '
           '6 x 290 € y el CUADRE de la renta dice REVISA',
           abs((r0 - r1) - 12 * 290.0) < 1e-6 and p1 > p0 and abs((f1 - f0) - 6 * 290.0) < 1e-6
           and q0 == 'CUADRA' and str(q1).startswith('REVISA'),
           'resultado %.2f -> %.2f · equilibrio %.1f -> %.1f raciones/día' % (r0, r1, p0, p1))

    # 2. Cerrar en verano (X16 = 0): el resultado del crucero cae exactamente lo que dejaba la
    #    carta de verano y la salida elegida queda igual que «cerrar» en «Escenarios».
    xl = nuevo()
    r0 = ev(xl, H_PYG, res_c)
    e0, c0 = ev(xl, H_ESC, 'D%d' % X['elegida']), ev(xl, H_ESC, 'D%d' % X['cerrar'])
    pon(xl, H_SUP, 'B%d' % CRUCE_ROW['_contribucion_verano_elegida'], 0.0)
    r1 = ev(xl, H_PYG, res_c)
    e1 = ev(xl, H_ESC, 'D%d' % X['elegida'])
    x16 = D._contribucion_verano_elegida()
    prueba('X16 a cero (cerrar en verano): el resultado cae %.2f € y la salida elegida iguala a cerrar' % x16,
           abs((r0 - r1) - x16) < 1e-6 and abs(e1 - c0) < 1e-9 and e0 > c0,
           'resultado %.2f -> %.2f · verano con fijos %.2f -> %.2f' % (r0, r1, e0, e1))

    # 3. Bajar los meses de colchón de 6 a 3: el fondo se queda en la mitad y el préstamo que
    #    pide la estructura baja; la comprobación del punto fijo avisa.
    xl = nuevo()
    f0 = ev(xl, H_INV, 'B%d' % IV['fondo'])
    pf0 = ev(xl, H_FIN, 'B%d' % F['punto_fijo'])
    pide0 = ev(xl, H_FIN, 'B%d' % F['pide'])
    pon(xl, H_SUP, 'B%d' % S['colchon'], 3)
    f1 = ev(xl, H_INV, 'B%d' % IV['fondo'])
    pf1 = ev(xl, H_FIN, 'B%d' % F['punto_fijo'])
    pide1 = ev(xl, H_FIN, 'B%d' % F['pide'])
    prueba('3 meses de colchón en vez de 6: el fondo se parte por la mitad, el préstamo que pide la '
           'estructura baja y el punto fijo pide que lo copies',
           abs(f1 - f0 / 2.0) < 1e-6 and pide1 < pide0 and str(pf0).startswith('Cerrado')
           and str(pf1).startswith('REVISA'),
           'fondo %.2f -> %.2f · préstamo %.0f -> %.0f' % (f0, f1, pide0, pide1))

    # 4. Un 10 % menos de raciones del año (X13): la contribución que depende de las raciones
    #    baja un 10 % y el margen de seguridad en raciones al día se estrecha.
    xl = nuevo()
    k0 = ev(xl, H_PYG, 'C%d' % P['contribucion'])
    fe = ev(xl, H_PYG, 'C%d' % P['ferias'])
    s0 = ev(xl, H_PEQ, 'B%d' % E['seg_dia'])
    pon(xl, H_SUP, 'B%d' % CRUCE_ROW['raciones_anio'], int(round(D.raciones_anio() * 0.9)))
    k1 = ev(xl, H_PYG, 'C%d' % P['contribucion'])
    s1 = ev(xl, H_PEQ, 'B%d' % E['seg_dia'])
    prueba('un 10 % menos de raciones: la carta de invierno y el aceite se mueven un 10 % y el margen de '
           'seguridad baja',
           abs((k1 - fe) - ((k0 - fe) - 0.1 * (k0 - fe - D._contribucion_verano_elegida()))) < 1e-6 and s1 < s0,
           'contribución %.2f -> %.2f · margen %.1f -> %.1f raciones/día' % (k0, k1, s0, s1))

    # 5. Despacho: un ahorro de fijos igual al que pide la hoja deja el despacho a cero.
    xl = nuevo()
    a0 = ev(xl, H_ESC, 'C%d' % X['f_ahorro'])
    d0 = ev(xl, H_ESC, 'C%d' % X['f_res'])
    pon(xl, H_SUP, 'B%d' % S['ahorro_desp'], a0)
    d1 = ev(xl, H_ESC, 'C%d' % X['f_res'])
    a1 = ev(xl, H_ESC, 'C%d' % X['f_ahorro'])
    prueba('sólo despacho: si te ahorras los %.0f € que pide la hoja, el resultado del despacho queda en cero'
           % a0, d0 < 0 and abs(d1) < 1e-6 and abs(a1) < 1e-6, 'resultado %.2f -> %.2f' % (d0, d1))

    # 7. R-04 (X10 bis): las partidas no amortizables viajan del libro 2 con su CUADRE. Si el
    #    lector copia 0 en vez de 4.668,30 €, la amortización sube y el CUADRE avisa.
    xl = nuevo()
    fna = CUADRE_ROW['_capex_no_amortizable']
    am0 = ev(xl, H_INV, 'B%d' % IV['amort'])
    na0 = ev(xl, H_SUP, 'D%d' % fna)
    pon(xl, H_SUP, 'B%d' % CRUCE_ROW['_capex_no_amortizable'], 0.0)
    am1 = ev(xl, H_INV, 'B%d' % IV['amort'])
    na1 = ev(xl, H_SUP, 'D%d' % fna)
    prueba('el CAPEX no amortizable copiado a cero sube la amortización anual y su CUADRE (X10 bis) '
           'dice REVISA', am1 > am0 and na0 == 'CUADRA' and str(na1).startswith('REVISA'),
           'amortización %.2f -> %.2f · %r -> %r' % (am0, am1, na0, str(na1)[:12]))

    # 8. R-06 (X16 bis): «Escenarios» enseña el verano con fijos de las TRES salidas; cambiar la
    #    contribución de las ferias mueve sólo su fila.
    xl = nuevo()
    ev(xl, H_ESC, 'D%d' % X['carta'])
    v0 = ev(xl, H_ESC, 'D%d' % X['ferias'])
    pon(xl, H_SUP, 'B%d' % CRUCE_ROW['_contribucion_verano_ferias'], 10000.0)
    v1 = ev(xl, H_ESC, 'D%d' % X['ferias'])
    carta = ev(xl, H_ESC, 'D%d' % X['carta'])
    prueba('la contribución de las ferias (X16 bis) mueve su fila del verano con fijos y no la de la '
           'carta de verano', abs((v1 - v0) - (10000.0 - D._contribucion_verano_ferias())) < 1e-6
           and abs(carta - D.verano_con_fijos('carta de verano')) < 1e-6,
           'ferias %.2f -> %.2f · carta %.2f' % (v0, v1, carta))

    # 9. R-13 (X16 ter): las ventas del verano son las de la salida elegida, no el ticket de invierno.
    xl = nuevo()
    vv0 = ev(xl, H_PYG, 'C%d' % P['ventas'])
    pon(xl, H_SUP, 'B%d' % CRUCE_ROW['_ventas_verano_elegida'], 0.0)
    vv1 = ev(xl, H_PYG, 'C%d' % P['ventas'])
    prueba('sin ventas de verano (X16 ter a cero) las ventas del año bajan exactamente esas ventas',
           abs((vv0 - vv1) - D._ventas_verano_elegida()) < 1e-6,
           'ventas %.2f -> %.2f' % (vv0, vv1))

    # 10. R-14: el % de sala viaja como fracción (0,70). Un 0,50 mueve el resultado y avisa.
    xl = nuevo()
    fp = CUADRE_ROW['_pct_sala_fraccion']
    z0 = ev(xl, H_PYG, res_c)
    c_0 = ev(xl, H_SUP, 'D%d' % fp)
    pon(xl, H_SUP, 'B%d' % CRUCE_ROW['_pct_sala_fraccion'], 0.5)
    z1 = ev(xl, H_PYG, res_c)
    c_1 = ev(xl, H_SUP, 'D%d' % fp)
    prueba('el % de sala copiado como 0,50 (fracción) mueve el resultado del crucero y su CUADRE avisa',
           z1 != z0 and c_0 == 'CUADRA' and str(c_1).startswith('REVISA'),
           'resultado %.2f -> %.2f · %r -> %r' % (z0, z1, c_0, str(c_1)[:12]))
    return ok, fallos


# ==========================================================================
def main():
    ids_usados = ['CHN-75', 'CHN-48', 'CUN-23', 'CHN-67']
    requeridos = [i for i, (_t, libros) in D.IDS_LEGALES_REQUERIDOS.items() if LIBRO in libros]
    D.gate_legal(sorted(set(requeridos + ids_usados)))
    for c in CRUCES_IN:
        if (c['origen'], c['receptor']) not in D.ARISTAS_SPEC:
            raise SystemExit('%s: arista %s no está en la SPEC' % (c['x'], (c['origen'], c['receptor'])))
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_supuestos(wb)
    hoja_inversion(wb)
    hoja_pyg(wb)
    hoja_equilibrio(wb)
    hoja_escenarios(wb)
    hoja_personal(wb)
    hoja_tesoreria(wb)
    hoja_financiacion(wb)
    hoja_canales(wb)
    orden = list(ORDEN_HOJAS)
    wb._sheets.sort(key=lambda ws: orden.index(ws.title))

    res = cerrar(wb, mapa_celdas())
    print('escrito: %s' % res['ruta'])
    print('hojas: %d · fórmulas: %d · celdas verdes: %d · verdes vacías: %d'
          % (res['hojas'], res['formulas'], res['verdes'], len(res['verdes_vacias'])))
    print('fórmulas que devuelven «sin dato» a propósito (sin caché): %d' % res['sin_dato'])
    print('notas legales: %d · notas de fuente sectorial: %d · etiquetas en el mapa: %d'
          % (res['notas_legales'], res['notas_sector'], res['mapa']))
    print('cruces recibidos: %d (con %d filas de CUADRE) · cruces de origen: 0'
          % (res['cruces_in'], res['cuadres']))
    print('inject_cache: %s' % res['cache'])
    print('  contra datos_ejemplo: %d comprobaciones al céntimo, todas en verde' % len(res['contra_datos']))
    for n, v, e in res['contra_datos']:
        print('    %-42s %16.4f  (datos_ejemplo %16.4f)' % (n, v, e))
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
