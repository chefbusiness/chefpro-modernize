#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_comun_libros_4_6.py — utillaje del constructor C3 (libros 4 y 6 de «Cómo Montar
una Chocolatería»: carta y escandallo, y campañas y valle del año).

Misma arquitectura de DOS CAPAS que la hermana Pastelería, que publica
`_comun_pasteleria.py` (formatos, `dv_rango`, barrido WinAnsi) **y**
`_comun_libros_3_4.py` (entradas verdes contadas, notas legales y el CIERRE
común). Aquí la primera capa es `_comun_chocolateria.py` —la escribió otro
constructor y NO se toca— y esta es la segunda:

  1. `entrada()`  — celda VERDE con su valor por defecto REGISTRADO (regla 2 de
     §2.3: ninguna celda verde vacía, y el gate lo comprueba sobre el mapa).
  2. `nota_celda()` — pone la nota legal de `datos_ejemplo.nota_legal(id)` como
     COMENTARIO de la celda y la cuenta.
  3. `nota_sector()` — lo mismo para un id `CHS-*`, que no vive en la
     verificación legal sino en el JSON común: «Fuente: <tema> · <url>».
  4. `cerrar()` — guarda, corre `inject_cache.py`, verifica `data_only` de TODAS
     las fórmulas registradas (con pycel para distinguir la que devuelve `""` a
     propósito de la que está rota), gate de `=SUM(rango)`, barrido WinAnsi,
     censo de verdes vacías, funciones prohibidas, **cero fórmulas que nombren
     otro fichero** (D32) y escritura de `build/mapa-<libro>.json`.

Via: Claude Code
"""
import json
import os
import re
import subprocess
import sys

import openpyxl
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Font, PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..'))
if os.path.join(RAIZ, 'guias-v2_0') not in sys.path:
    sys.path.insert(0, os.path.join(RAIZ, 'guias-v2_0'))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import motor                                                   # noqa: E402
import datos_ejemplo as D                                      # noqa: E402
import _comun_chocolateria as CC                               # noqa: E402

motor.CTX['producto'] = CC.PID

PID = CC.PID
PRODUCTO = CC.PRODUCTO
SUBTITULO = CC.SUBTITULO
SUBJECT = PRODUCTO + ' · Versión 1.0 · septiembre 2026'
VERSION_LINE = CC.VERSION_LINE
BIO = CC.BIO
DESPROTEGER = CC.NOTA_DESPROTEGER
LEYENDA_VERDE = motor.NOTA_VERDES
PIE = 'AI Chef Pro · aichef.pro · Página &P de &N'

#: WinAnsi ESTRICTO (SPEC §2.3 y docstring de `datos_ejemplo`): ni espacio fino
#: (U+202F) ni guion no separable (U+2011). Donde Pastelería escribía
#: `100` + espacio fino + `%`, aquí va un espacio normal.
N = ' '

ORO = 'FFD700'
GRIS = '888888'
CAB_BG, CAB_FG = '2D2D2D', 'FFFFFF'
CREMA = 'FFF8E1'
AZUL = '1565C0'

EUR = motor.FMT_EUR
EUR4 = '#,##0.0000 €'
PCT = motor.FMT_PCT
PCT0 = '0%'
ENT = motor.FMT_ENT
DEC = '#,##0.00'
DEC1 = '#,##0.0'
DEC3 = '#,##0.000'
FECHA = motor.FMT_FECHA

#: Notas legales puestas por el generador en curso: (hoja, coord, id).
NOTAS_LEGALES = []
#: Celdas verdes declaradas: (hoja, coord, etiqueta, valor por defecto).
VERDES = []

#: Etiqueta LITERAL de las celdas verdes que traen una cifra de otro libro
#: (D32). El gate de `cerrar()` exige que cada una tenga su fila de CUADRE en
#: la misma hoja.
ETIQUETA_TRAE = 'trae aquí la cifra de '
ETIQUETA_CUADRE = 'CUADRE'


# --------------------------------------------------------------------------
# Formato
# --------------------------------------------------------------------------
def cabecera_hoja(ws, titulo, sub=None):
    motor.val(ws, 'A1', CC.titulo_hoja(titulo), bold=True)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    motor.val(ws, 'A2', sub or SUBTITULO)
    ws['A2'].font = Font(size=10, color=GRIS)


def seccion(ws, coord, texto):
    motor.val(ws, coord, texto, bold=True)
    ws[coord].font = Font(bold=True, size=12, color=ORO)


def apunte(ws, coord, texto):
    motor.val(ws, coord, texto, wrap=True)
    ws[coord].font = Font(size=9, color=GRIS)
    return ws[coord]


def encabezados(ws, fila, cols, alto=42):
    """`cols` = [(letra, texto, ancho|None), ...]."""
    for letra, texto, ancho in cols:
        cel = ws[letra + str(fila)]
        cel.value = texto
        cel.font = Font(bold=True, color=CAB_FG, size=9)
        cel.fill = PatternFill('solid', fgColor=CAB_BG)
        cel.alignment = Alignment(horizontal='center', vertical='center',
                                  wrap_text=True)
        if ancho is not None:
            ws.column_dimensions[letra].width = ancho
    ws.row_dimensions[fila].height = alto


def crema(cel):
    cel.fill = PatternFill('solid', fgColor=CREMA)
    return cel


def setup(ws, landscape=True, titulos=None):
    ws.page_setup.paperSize = 9                        # A4
    ws.page_setup.orientation = 'landscape' if landscape else 'portrait'
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins.left = ws.page_margins.right = 0.39
    ws.page_margins.top = ws.page_margins.bottom = 0.59
    ws.oddFooter.center.text = PIE
    ws.oddFooter.center.size = 8
    if titulos:
        ws.print_title_rows = titulos


# --------------------------------------------------------------------------
# Entradas y notas
# --------------------------------------------------------------------------
def entrada(ws, coord, valor, fmt=None, etiqueta='', bold=None):
    """Celda VERDE de entrada, con su valor por defecto REGISTRADO.

    Regla 2 de §2.3: ninguna celda verde queda vacía. `valor` nunca puede ser
    `None` ni cadena vacía: si no hay dato publicado, se siembra el supuesto
    declarado.
    """
    if valor is None or (isinstance(valor, str) and not valor.strip()):
        raise SystemExit('entrada(%s!%s, «%s») sin valor por defecto: la regla '
                         '2 de §2.3 no admite una celda verde vacía'
                         % (ws.title, coord, etiqueta))
    cel = motor.val(ws, coord, valor, fmt=fmt, verde_=True, bold=bold)
    VERDES.append((ws.title, coord, etiqueta, valor))
    return cel


def nota_celda(ws, coord, id_chn):
    """Nota legal de `id_chn` como comentario de la celda (regla 1 de §2.3)."""
    texto = D.nota_legal(id_chn)
    if not texto:
        raise SystemExit('nota_legal(%r) no devuelve nada: gate_legal debería '
                         'haber abortado antes' % id_chn)
    ws[coord].comment = Comment(texto, 'AI Chef Pro', height=120, width=460)
    NOTAS_LEGALES.append((ws.title, coord, id_chn))
    return texto


def nota_sector(ws, coord, id_chs):
    """Nota de procedencia para un id `CHS-*` del JSON común. No es una nota
    legal y no se cuenta como tal: un dato de sector no es una norma."""
    f = D.ficha(id_chs)
    if not f:
        raise SystemExit('El id de sector %r no existe en el JSON común '
                         '(D44: hay familias que sólo existen con sufijo)'
                         % id_chs)
    tema = str(f.get('tema') or '').strip()
    url = str(f.get('url') or '').strip()
    fiab = str(f.get('fiabilidad') or '').strip()
    texto = '%s: %s%s%s' % (id_chs, tema,
                            ' · fiabilidad ' + fiab if fiab else '',
                            ' · ' + url if url else '')
    ws[coord].comment = Comment(texto, 'AI Chef Pro', height=110, width=440)
    return texto


def dv_rango(ws, coords, ref, titulo, mensaje, prompt=None):
    return CC.dv_rango(ws, coords, ref, titulo, mensaje, prompt=prompt)


def bloque_listas(ws, fila, listas, col='A'):
    return CC.bloque_listas(ws, fila, listas, col=col)


# --------------------------------------------------------------------------
# Cierre: guardar, cachear, verificar y publicar el mapa
# --------------------------------------------------------------------------
_PROHIBIDAS = ('INDIRECT', 'COUNTA', 'PMT(', 'OFFSET', 'XLOOKUP', 'LET(',
               'LAMBDA', 'RANK(', 'NETWORKDAYS', 'IRR(')

#: Los nueve ficheros del paquete. Ninguna fórmula puede nombrar a otro (D32).
_LIBROS = ('capacidad-obrador-y-clima', 'calculadora-capex-chocolateria',
           'sensibilidad-al-precio-del-cacao',
           'carta-de-apertura-y-escandallo-chocolate',
           'vida-util-rellenos-y-rotacion', 'campanas-y-valle-del-ano',
           'plan-financiero-3-anos-chocolateria',
           'checklist-legal-licencias-y-cacao',
           'checklist-equipamiento-y-proveedores-cacao')


def _gate_cruces(wbf, nombre):
    """D32: cada celda verde etiquetada «trae aquí la cifra de …» tiene su fila
    de CUADRE EN LA MISMA HOJA. Comprobar las fórmulas no detecta una fila de
    cuadre ausente, así que se cuentan las dos cosas por hoja."""
    trae, cuadre = {}, {}
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if not isinstance(c.value, str):
                    continue
                if ETIQUETA_TRAE in c.value:
                    trae.setdefault(ws.title, []).append(c.coordinate)
                if c.value.startswith(ETIQUETA_CUADRE):
                    cuadre.setdefault(ws.title, []).append(c.coordinate)
    fallos = []
    for hoja in trae:
        if hoja not in cuadre:
            fallos.append('la hoja «%s» trae una cifra de otro libro y no '
                          'tiene fila de CUADRE' % hoja)
    if fallos:
        raise SystemExit('GATE DE CRUCES (D32) en %s:\n  %s'
                         % (nombre, '\n  '.join(fallos)))
    return sum(len(v) for v in trae.values()), sum(len(v) for v in cuadre.values())


def _gate_sin_referencias_externas(nombre):
    """Cero fórmulas que nombren OTRO fichero del paquete (D32)."""
    usos = []
    for hoja, coord, formula in motor.REGISTRO:
        bajo = formula.lower()
        for libro in _LIBROS:
            if libro != nombre and libro in bajo:
                usos.append('%s!%s nombra %s.xlsx' % (hoja, coord, libro))
        if '.xlsx' in bajo or '[' in formula:
            usos.append('%s!%s parece referencia externa: %s'
                        % (hoja, coord, formula[:70]))
    if usos:
        raise SystemExit('REFERENCIAS ENTRE LIBROS (prohibidas, D32):\n  '
                         + '\n  '.join(sorted(set(usos))))


def cerrar(wb, nombre, titulo, mapa_celdas, notas_mapa=None):
    """Guarda, inyecta caché, verifica `data_only` y escribe el mapa.

    `mapa_celdas` = [(etiqueta, hoja, coord, tipo), ...] con
    tipo en {'entrada', 'salida', 'parametro'}.
    """
    wb.properties.creator = 'AI Chef Pro'
    wb.properties.lastModifiedBy = 'AI Chef Pro'
    wb.properties.title = titulo
    wb.properties.subject = SUBJECT

    CC.barrer_cp1252(wb)
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and (motor.NARROW in c.value
                                                 or motor.NOBRK in c.value):
                    raise SystemExit('%s!%s lleva espacio fino o guion no '
                                     'separable: la SPEC de este producto los '
                                     'prohíbe' % (ws.title, c.coordinate))

    for ws in wb.worksheets:
        motor.retirar_verde_de_calculadas(ws)
        motor.proteger(ws)

    destino = os.path.join(AQUI, 'build')
    if not os.path.isdir(destino):
        os.makedirs(destino)
    ruta = os.path.join(destino, nombre + '.xlsx')
    wb.save(ruta)

    _gate_sin_referencias_externas(nombre)

    # --- inject_cache ------------------------------------------------------
    res = subprocess.run([sys.executable,
                          os.path.join(RAIZ, 'inject_cache.py'), ruta],
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    salida_cache = res.stdout.decode('utf-8', 'replace')
    if res.returncode != 0:
        raise SystemExit('inject_cache falló:\n' + salida_cache)

    # --- verificación data_only -------------------------------------------
    # `inject_cache.py` NO cachea las fórmulas que devuelven la cadena vacía
    # (el «sin dato» = "" de la familia): esas celdas se quedan en `None` con
    # data_only y NO son un fallo. Para no confundirlas con una fórmula rota,
    # cada `None` se vuelve a evaluar con pycel y se exige que dé ''.
    wbf = openpyxl.load_workbook(ruta)
    wbv = openpyxl.load_workbook(ruta, data_only=True)
    sin_valor, con_error, sin_dato = [], [], []
    pendientes = []
    for hoja, coord, formula in motor.REGISTRO:
        v = wbv[hoja][coord].value
        if v is None:
            pendientes.append((hoja, coord, formula))
        elif isinstance(v, str) and v.startswith('#'):
            con_error.append('%s!%s  %s -> %s' % (hoja, coord, formula[:60], v))
    if pendientes:
        from pycel import ExcelCompiler
        xl = ExcelCompiler(ruta)
        for hoja, coord, formula in pendientes:
            try:
                r = xl.evaluate("'%s'!%s" % (hoja, coord))
            except Exception as e:                            # noqa: BLE001
                sin_valor.append('%s!%s  %s -> pycel: %s'
                                 % (hoja, coord, formula[:60], e))
                continue
            if r == '' or (r is None and formula.count('""')):
                sin_dato.append('%s!%s' % (hoja, coord))
            else:
                sin_valor.append('%s!%s  %s -> %r'
                                 % (hoja, coord, formula[:60], r))
    if sin_valor or con_error:
        raise SystemExit(
            'VERIFICACIÓN data_only FALLIDA en %s\n  sin valor (%d):\n   %s\n'
            '  con error (%d):\n   %s'
            % (nombre, len(sin_valor), '\n   '.join(sin_valor[:40]),
               len(con_error), '\n   '.join(con_error[:40])))

    # --- gate de totales: cada `=SUM(rango)` cachea lo que suma -------------
    incoherentes = CC.gate_sum_rango(wbv)
    if incoherentes:
        raise SystemExit('TOTALES con caché incoherente en %s:\n  %s'
                         % (nombre, '\n  '.join(incoherentes)))

    # --- celdas verdes vacías (regla 2 de §2.3) ---------------------------
    verdes_vacias = []
    n_verdes = 0
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                if motor.es_verde(c):
                    n_verdes += 1
                    if c.value is None or (isinstance(c.value, str)
                                           and not c.value.strip()):
                        verdes_vacias.append('%s!%s' % (ws.title, c.coordinate))
    if verdes_vacias:
        raise SystemExit('CELDAS VERDES VACÍAS en %s (regla 2 de §2.3):\n  %s'
                         % (nombre, ', '.join(verdes_vacias)))

    n_trae, n_cuadre = _gate_cruces(wbf, nombre)

    # --- funciones prohibidas ---------------------------------------------
    usos = []
    for hoja, coord, formula in motor.REGISTRO:
        arriba = formula.upper()
        for p in _PROHIBIDAS:
            if p in arriba:
                usos.append('%s!%s usa %s' % (hoja, coord, p))
    if usos:
        raise SystemExit('Funciones PROHIBIDAS:\n  ' + '\n  '.join(usos))

    # --- divisiones sin IFERROR -------------------------------------------
    sin_guarda = []
    for hoja, coord, formula in motor.REGISTRO:
        if '/' in formula and 'IFERROR' not in formula.upper():
            sin_guarda.append('%s!%s  %s' % (hoja, coord, formula[:70]))
    if sin_guarda:
        raise SystemExit('DIVISIONES sin IFERROR:\n  '
                         + '\n  '.join(sin_guarda[:30]))

    # --- mapa --------------------------------------------------------------
    mapa = {}
    for etiqueta, hoja, coord, tipo in mapa_celdas:
        if hoja not in wbv.sheetnames:
            raise SystemExit('El mapa cita la hoja inexistente %r' % hoja)
        v = wbv[hoja][coord].value
        if v is None:
            raise SystemExit('El mapa cita %s!%s («%s») y está VACÍA'
                             % (hoja, coord, etiqueta))
        if etiqueta in mapa:
            raise SystemExit('Etiqueta de mapa repetida: %r' % etiqueta)
        if hasattr(v, 'isoformat'):
            v = v.isoformat()[:10]
        mapa[etiqueta] = {'ref': '%s.xlsx!%s!%s' % (nombre, hoja, coord),
                          'valor': v, 'tipo': tipo}
    if notas_mapa:
        mapa['_notas'] = {'ref': '%s.xlsx!%s!A1'
                                 % (nombre, wb.worksheets[0].title),
                          'valor': notas_mapa, 'tipo': 'nota'}
    with open(os.path.join(destino, 'mapa-' + nombre + '.json'), 'w') as fh:
        fh.write(json.dumps(mapa, ensure_ascii=False, indent=1))

    return {
        'ruta': ruta,
        'hojas': len(wbf.worksheets),
        'formulas': len(motor.REGISTRO),
        'sin_dato': len(sin_dato),
        'verdes': n_verdes,
        'verdes_vacias': verdes_vacias,
        'notas_legales': len(NOTAS_LEGALES),
        'trae': n_trae,
        'cuadre': n_cuadre,
        'mapa': len([k for k in mapa if k != '_notas']),
        'cache': (salida_cache.strip().splitlines() or [''])[-1],
    }
