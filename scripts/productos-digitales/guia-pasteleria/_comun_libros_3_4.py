# -*- coding: utf-8 -*-
"""
_comun_pasteleria.py — utillaje compartido por los generadores de los libros de
«Cómo Montar una Pastelería» (SPEC §2.2).

NO es un segundo motor: `guias-v2_0/motor.py` sigue siendo el motor de familia.
Aquí viven sólo las cuatro cosas que la SPEC pide a ESTE producto y que el motor
no trae:

  1. La línea de versión **1.0 · septiembre 2026** (el `motor.version_line()`
     devuelve «Versión 2.0 · agosto 2026», que es la de la familia v2.0).
  2. La bio anclada y la nota de desproteger, en el literal de la SPEC.
  3. `nota_celda()`: pone la nota legal de `datos_ejemplo.nota_legal(id)` como
     COMENTARIO de la celda y la cuenta, para que el resumen del generador
     pueda declarar cuántos datos legales llevan fuente.
  4. El cierre común: guardar, `inject_cache.py`, verificación `data_only` de
     TODAS las fórmulas registradas y escritura del `build/mapa-<libro>.json`
     en el formato que consume el guion (`etiqueta -> {ref, valor, tipo}`).

Via: Claude Code
"""
import json
import os
import subprocess
import sys

import openpyxl
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Font, PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..'))
sys.path.insert(0, os.path.join(RAIZ, 'guias-v2_0'))
sys.path.insert(0, AQUI)

import motor                                                   # noqa: E402
import datos_ejemplo as D                                      # noqa: E402

motor.CTX['producto'] = 'guia-pasteleria-obrador'

PID = 'guia-pasteleria-obrador'
PRODUCTO = 'Cómo Montar una Pastelería'
SUBTITULO = 'AI Chef Pro · aichef.pro — ' + PRODUCTO
SUBJECT = PRODUCTO + ' · Versión 1.0 · septiembre 2026'

VERSION_LINE = ('Versión 1.0 · septiembre 2026 · aichef.pro/' + PID
                + ' · info@aichef.pro')
BIO = ('Diseñado por John Guerrero — chef y consultor gastronómico desde 2010, '
       'en cocina desde los 17 años.')
DESPROTEGER = ('Para editar la estructura o una celda que no esté en verde, '
               'desprotege la hoja: Revisar > Desproteger hoja. La protección '
               'NO tiene contraseña; sólo evita pisar una fórmula sin querer.')
LEYENDA_VERDE = 'Celdas verdes = campos editables'
PIE = 'AI Chef Pro · aichef.pro · Página &P de &N'

N = motor.NARROW                 # espacio fino antes de la unidad

ORO = 'FFD700'
GRIS = '888888'
CAB_BG, CAB_FG = '2D2D2D', 'FFFFFF'
CREMA = 'FFF8E1'
AZUL = '1565C0'
VERDE_BG = motor.VERDE

EUR = motor.FMT_EUR
PCT = motor.FMT_PCT
PCT0 = '0%'
ENT = motor.FMT_ENT
DEC = '#,##0.00'
DEC1 = '#,##0.0'
FECHA = motor.FMT_FECHA

#: Contador de notas legales puestas por el generador en curso.
NOTAS_LEGALES = []
#: Celdas verdes declaradas por el generador: (hoja, coord, etiqueta, valor).
VERDES = []


# --------------------------------------------------------------------------
# Formato
# --------------------------------------------------------------------------
def cabecera_hoja(ws, titulo, sub=None):
    motor.val(ws, 'A1', titulo, bold=True)
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    motor.val(ws, 'A2', sub or SUBTITULO)
    ws['A2'].font = Font(size=10, color=GRIS)


def apunte(ws, coord, texto, ancho=None):
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


def seccion(ws, coord, texto):
    motor.val(ws, coord, texto, bold=True)
    ws[coord].font = Font(bold=True, size=12, color=ORO)


def crema(cel):
    cel.fill = PatternFill('solid', fgColor=CREMA)
    return cel


def setup(ws, landscape=True):
    ws.page_setup.paperSize = 9                        # A4
    ws.page_setup.orientation = 'landscape' if landscape else 'portrait'
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins.left = ws.page_margins.right = 0.39
    ws.page_margins.top = ws.page_margins.bottom = 0.59
    ws.oddFooter.center.text = PIE
    ws.oddFooter.center.size = 8


# --------------------------------------------------------------------------
# Entradas y notas
# --------------------------------------------------------------------------
def entrada(ws, coord, valor, fmt=None, etiqueta='', bold=None):
    """Celda VERDE de entrada. Registra su valor por defecto (D21)."""
    cel = motor.val(ws, coord, valor, fmt=fmt, verde_=True, bold=bold)
    VERDES.append((ws.title, coord, etiqueta, valor))
    return cel


def nota_celda(ws, coord, id_pa):
    """Nota legal de `id_pa` como comentario de la celda (SPEC §2.2)."""
    texto = D.nota_legal(id_pa)
    if not texto:
        raise SystemExit('nota_legal(%r) no devuelve nada: gate_legal debería '
                         'haber abortado antes' % id_pa)
    ws[coord].comment = Comment(texto, 'AI Chef Pro', height=110, width=440)
    NOTAS_LEGALES.append((ws.title, coord, id_pa))
    return texto


def dv_rango(ws, coords, ref, titulo, mensaje):
    """Desplegable cuyo origen es un RANGO de la propia hoja (SPEC §2.2)."""
    from openpyxl.worksheet.datavalidation import DataValidation
    if not coords:
        return None
    dv = DataValidation(type='list', formula1=ref, allow_blank=False,
                        showErrorMessage=True, errorTitle=titulo,
                        error=mensaje)
    ws.add_data_validation(dv)
    for c in coords:
        dv.add(c)
    return dv


# --------------------------------------------------------------------------
# Cierre: guardar, cachear, verificar y publicar el mapa
# --------------------------------------------------------------------------
def cerrar(wb, nombre, titulo, mapa_celdas, notas_mapa=None):
    """Guarda, inyecta caché, verifica `data_only` y escribe el mapa.

    `mapa_celdas` = [(etiqueta, hoja, coord, tipo), ...] con
    tipo en {'entrada', 'salida', 'parametro'}.
    Devuelve un dict con el resumen.
    """
    wb.properties.creator = 'AI Chef Pro'
    wb.properties.lastModifiedBy = 'AI Chef Pro'
    wb.properties.title = titulo
    wb.properties.subject = SUBJECT

    for ws in wb.worksheets:
        motor.retirar_verde_de_calculadas(ws)
        motor.proteger(ws)

    destino = os.path.join(AQUI, 'build')
    os.makedirs(destino, exist_ok=True)
    ruta = os.path.join(destino, nombre + '.xlsx')
    wb.save(ruta)

    # --- inject_cache ------------------------------------------------------
    res = subprocess.run([sys.executable, os.path.join(RAIZ, 'inject_cache.py'),
                          ruta], capture_output=True, text=True)
    salida_cache = (res.stdout or '') + (res.stderr or '')
    if res.returncode != 0:
        raise SystemExit('inject_cache falló:\n' + salida_cache)

    # --- verificación data_only -------------------------------------------
    # `inject_cache.py` NO cachea a propósito las fórmulas que devuelven la
    # cadena vacía (es el «sin dato» = "" de la familia, §7-bis.13): esas
    # celdas se quedan en `None` con data_only y NO son un fallo. Para no
    # confundirlas con una fórmula rota, cada `None` se vuelve a evaluar con
    # pycel y se exige que dé exactamente ''.
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
            if r == '' or r is None and formula.count('""'):
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

    # --- gate de totales: cada `=SUM(rango)` tiene que cachear lo que suma --
    # pycel cachea como 0 un `SUM` sobre una columna de `SUMPRODUCT`, y el
    # libro se publicaría con un total falso, sin error y sin aviso: el visor
    # que no recalcula enseñaría 0 y el guion citaría ese 0. Medido en el
    # libro 4 el 10-09-2026.
    import re
    rx = re.compile(r'^=SUM\(([A-Z]{1,2})(\d+):([A-Z]{1,2})(\d+)\)$')
    incoherentes = []
    for hoja, coord, formula in motor.REGISTRO:
        m = rx.match(formula)
        if not m or m.group(1) != m.group(3):
            continue
        col, a, b = m.group(1), int(m.group(2)), int(m.group(4))
        esperado = sum(v for v in (wbv[hoja]['%s%d' % (col, r)].value
                                   for r in range(a, b + 1))
                       if isinstance(v, (int, float)))
        real = wbv[hoja][coord].value
        if not isinstance(real, (int, float)) or abs(real - esperado) > 0.01:
            incoherentes.append('%s!%s  %s -> caché %r, suma real %r'
                                % (hoja, coord, formula, real, esperado))
    if incoherentes:
        raise SystemExit('TOTALES con caché incoherente en %s:\n  %s'
                         % (nombre, '\n  '.join(incoherentes)))

    # --- celdas verdes vacías (D21) ---------------------------------------
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
        if hasattr(v, 'isoformat'):        # fecha o fecha-hora cacheada
            v = v.isoformat()[:10]         # unifica con _comun_libros_5_6
        mapa[etiqueta] = {'ref': '%s.xlsx!%s!%s' % (nombre, hoja, coord),
                          'valor': v, 'tipo': tipo}
    if notas_mapa:
        # Hallazgo A9 (2026-09-10): `ref` sin `!Hoja!Celda` rompe cualquier
        # consumidor que haga `ref.split('!')` para resolver la celda (es lo
        # que hace `documentos.py`). Apunta a A1 de la primera hoja del propio
        # libro: no es un dato citable (`tipo` sigue siendo 'nota'), pero el
        # `ref` ya tiene la forma `libro.xlsx!Hoja!Celda` de todas las demás.
        mapa['_notas'] = {'ref': '%s.xlsx!%s!A1' % (nombre, wb.worksheets[0].title),
                          'valor': notas_mapa, 'tipo': 'nota'}
    with open(os.path.join(destino, 'mapa-' + nombre + '.json'), 'w',
              encoding='utf-8') as fh:
        json.dump(mapa, fh, ensure_ascii=False, indent=1)

    # --- funciones prohibidas ---------------------------------------------
    prohibidas = ('INDIRECT', 'COUNTA', 'PMT', 'OFFSET', 'XLOOKUP', 'LET(',
                  'LAMBDA', 'RANK', 'NETWORKDAYS', 'IRR')
    usos = []
    for hoja, coord, formula in motor.REGISTRO:
        arriba = formula.upper()
        for p in prohibidas:
            if p in arriba:
                usos.append('%s!%s usa %s' % (hoja, coord, p))
    if usos:
        raise SystemExit('Funciones PROHIBIDAS:\n  ' + '\n  '.join(usos))

    return {
        'ruta': ruta,
        'hojas': len(wbf.worksheets),
        'formulas': len(motor.REGISTRO),
        'sin_dato': len(sin_dato),
        'verdes': n_verdes,
        'verdes_vacias': verdes_vacias,
        'notas_legales': len(NOTAS_LEGALES),
        'mapa': len([k for k in mapa if k != '_notas']),
        'cache': salida_cache.strip().splitlines()[-1] if salida_cache.strip() else '',
    }
