# -*- coding: utf-8 -*-
"""
_comun_libro_7.py — cierre común del libro 7 de «Cómo Montar una Chocolatería»
(SPEC §2.2, fila 7; constructor C4, que va solo).

`_comun_chocolateria.py` (de C1) trae el FORMATO de la familia: cabeceras, A4,
Title Case, `dv_rango()`, `bloque_listas()`, `barrer_cp1252()`, `gate_sum_rango()`
y la línea de versión 1.0 de ESTE producto. Lo que no trae —y es lo que la SPEC
pide a cada generador al terminar— vive aquí, calcado de
`guia-pasteleria/_comun_libros_5_6.py` (el módulo del molde del libro 7) y de
`_comun_libros_3_5.py` (el de C2 en este mismo producto):

  1. `entrada()`: celda VERDE con su valor por defecto REGISTRADO (regla 2 de
     §2.3: ninguna celda verde vacía).
  2. `nota_celda()`: la nota legal de `datos_ejemplo.nota_legal(id)` como
     comentario de celda (regla 1 de §2.3).
  3. `nota_fuente()`: lo mismo para un id de SECTOR (`CHS-*`), que no es una
     norma y por eso NO se cuenta como nota legal. Aborta si el id no existe
     LITERALMENTE en el JSON común (D44: hay ids bare que sólo existen con
     sufijo).
  4. `cerrar()`: guardar, gate de funciones prohibidas y de referencias entre
     ficheros, `inject_cache.py`, verificación `data_only` de TODAS las fórmulas
     registradas (distinguiendo con pycel las que devuelven `""` a propósito),
     gate de totales `=SUM(rango)`, gate de verdes vacías, barrido WinAnsi y
     `build/mapa-<libro>.json` con un mínimo de 25 etiquetas.

No es un segundo motor: `guias-v2_0/motor.py` sigue siendo el motor de familia.

Via: Claude Code
"""
import json
import os
import re
import subprocess
import sys

import openpyxl
from openpyxl.comments import Comment
from openpyxl.styles import Font, PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..'))
if os.path.join(RAIZ, 'guias-v2_0') not in sys.path:
    sys.path.insert(0, os.path.join(RAIZ, 'guias-v2_0'))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import motor                                                   # noqa: E402
import datos_ejemplo as D                                      # noqa: E402
import _comun_chocolateria as CP                               # noqa: E402

motor.CTX['producto'] = CP.PID

PID = CP.PID
PRODUCTO = CP.PRODUCTO
SUBTITULO = CP.SUBTITULO
SUBJECT = PRODUCTO + ' · Versión 1.0 · septiembre 2026'
VERSION_LINE = CP.VERSION_LINE
BIO = CP.BIO
NOTA_VERDES = CP.NOTA_VERDES
NOTA_DESPROTEGER = CP.NOTA_DESPROTEGER

# --- formatos -------------------------------------------------------------
EUR = motor.FMT_EUR
PCT = motor.FMT_PCT
PCT2 = '0.00%'
PCT4 = '0.0000%'
ENT = motor.FMT_ENT
FECHA = motor.FMT_FECHA
DEC = '#,##0.00'
DEC1 = '#,##0.0'

ORO = CP.ORO
GRIS = CP.GRIS
GRIS_TXT = '808080'
CREMA = CP.CREMA
CABECERA = CP.CABECERA
AZUL = CP.AZUL

# --- formato: lo que ya vive en `_comun_chocolateria` ---------------------
anchos = CP.anchos
cabecera = CP.cabecera
nota = CP.nota
parrafo = CP.parrafo
pagina = CP.pagina
encabezar = CP.encabezar
dv_rango = CP.dv_rango
bloque_listas = CP.bloque_listas
pie = CP.pie
destacado = CP.destacado
titulo_hoja = CP.titulo_hoja

#: Contadores del generador en curso.
NOTAS_LEGALES = []
NOTAS_SECTOR = []
VERDES = []


def seccion(ws, coord, texto):
    """Fila de sección: texto dorado sobre fondo negro (molde del libro 7)."""
    motor.val(ws, coord, texto)
    ws[coord].font = Font(bold=True, size=11, color=ORO)
    ws[coord].fill = PatternFill('solid', fgColor=CABECERA)
    return ws[coord]


def banda(ws, fila, letras, texto):
    """Sección que ocupa toda la anchura de la tabla."""
    seccion(ws, 'A%d' % fila, texto)
    for letra in letras:
        if letra == 'A':
            continue
        motor.val(ws, letra + str(fila), '')
        ws[letra + str(fila)].fill = PatternFill('solid', fgColor=CABECERA)


def total_fila(ws, fila, letras):
    for letra in letras:
        c = ws[letra + str(fila)]
        c.font = Font(bold=True, size=c.font.size)
        c.fill = PatternFill('solid', fgColor=CREMA)


# --------------------------------------------------------------------------
# Entradas y notas
# --------------------------------------------------------------------------
def entrada(ws, coord, valor, fmt=None, etiqueta='', bold=None, align=None):
    """Celda VERDE de entrada, con su valor por defecto declarado (regla 2 de
    §2.3: ninguna celda verde vacía, y ninguna que dependa de un producto que
    el comprador no tiene)."""
    if valor is None or (isinstance(valor, str) and not valor.strip()):
        raise SystemExit('entrada(%s!%s) sin valor por defecto: la regla 2 de '
                         '§2.3 prohíbe una celda verde vacía'
                         % (ws.title, coord))
    cel = motor.val(ws, coord, valor, fmt=fmt, verde_=True, bold=bold,
                    align=align)
    VERDES.append((ws.title, coord, etiqueta, valor))
    return cel


def _winansi(texto):
    """Los comentarios no los barre `barrer_cp1252` (sólo mira valores de
    celda) y las fichas del JSON traen comillas tipográficas y emojis."""
    out = []
    for ch in texto:
        if ch == '\n':
            out.append(' ')
            continue
        try:
            ch.encode('cp1252')
        except UnicodeEncodeError:
            continue
        out.append(ch)
    return re.sub(r'\s+', ' ', ''.join(out)).strip()


def nota_celda(ws, coord, id_chn, extra=None):
    """Nota LEGAL como comentario de celda (regla 1 de §2.3):
    «Verificado el 12-09-2026 · norma y artículo · URL»."""
    texto = D.nota_legal(id_chn)
    if not texto:
        raise SystemExit('nota_legal(%r) no devuelve nada: gate_legal() '
                         'tendría que haber abortado antes.' % id_chn)
    if extra:
        texto = texto + ' · ' + extra
    ws[coord].comment = Comment(_winansi(texto), 'AI Chef Pro', height=130,
                                width=470)
    NOTAS_LEGALES.append((ws.title, coord, id_chn))
    return texto


def nota_fuente(ws, coord, id_chs, extra=None):
    """Procedencia de un dato de SECTOR (`CHS-*`). No es una nota legal y no se
    cuenta como tal. Aborta si el id no existe LITERALMENTE en el JSON común:
    es lo que hace cumplir D44 («`CHS-28` no existe; `CHS-28a` sí»)."""
    f = D.ficha(id_chs)
    if not f:
        raise SystemExit('ficha(%r): ese id NO existe en el JSON común. D44: '
                         'cita la variante CON SUFIJO.' % id_chs)
    partes = ['%s (%s)' % (f.get('tema') or id_chs, id_chs)]
    if f.get('fuente_titulo'):
        partes.append('Fuente: %s' % f['fuente_titulo'])
    if f.get('fecha_publicacion'):
        partes.append('Consultada el %s' % f['fecha_publicacion'])
    if f.get('url'):
        partes.append(f['url'])
    if extra:
        partes.append(extra)
    texto = _winansi((' ' + chr(183) + ' ').join(partes))
    ws[coord].comment = Comment(texto, 'AI Chef Pro', height=130, width=470)
    NOTAS_SECTOR.append((ws.title, coord, id_chs))
    return texto


def comentario(ws, coord, texto):
    """Comentario NO legal (criterio propio, supuesto declarado)."""
    ws[coord].comment = Comment(_winansi(texto), 'AI Chef Pro', height=115,
                                width=450)


# --------------------------------------------------------------------------
# Cierre
# --------------------------------------------------------------------------
PROHIBIDAS = ('INDIRECT(', 'COUNTA(', 'PMT(', 'OFFSET(', 'XLOOKUP(', 'LET(',
              'LAMBDA(', 'RANK(', 'NETWORKDAYS(', 'IRR(')

_RX_SUM = re.compile(r'^=SUM\(([A-Z]{1,2})(\d+):([A-Z]{1,2})(\d+)\)$')


def cerrar(wb, nombre, titulo, mapa_celdas, notas_mapa=None):
    """Guarda, inyecta caché, verifica `data_only` y escribe el mapa.

    `mapa_celdas` = [(etiqueta, hoja, coord, tipo), …] con tipo en
    {'entrada', 'salida', 'parametro'}. Devuelve el resumen como dict.
    """
    wb.properties.creator = 'AI Chef Pro'
    wb.properties.lastModifiedBy = 'AI Chef Pro'
    wb.properties.title = titulo
    wb.properties.subject = SUBJECT

    CP.barrer_cp1252(wb)

    for ws in wb.worksheets:
        motor.retirar_verde_de_calculadas(ws)
        motor.proteger(ws)

    destino = CP.BUILD_DIR
    if not os.path.isdir(destino):
        os.makedirs(destino)
    ruta = os.path.join(destino, nombre + '.xlsx')
    wb.save(ruta)

    # --- funciones prohibidas y referencias entre ficheros ----------------
    usos = []
    for hoja, coord, formula in motor.REGISTRO:
        arriba = formula.upper().replace(' ', '')
        for p in PROHIBIDAS:
            if p in arriba:
                usos.append('%s!%s usa %s' % (hoja, coord, p[:-1]))
        if '.XLSX' in arriba or '[' in formula:
            usos.append('%s!%s NOMBRA OTRO FICHERO: %s'
                        % (hoja, coord, formula[:90]))
    if usos:
        raise SystemExit('Funciones PROHIBIDAS o referencia externa:\n  '
                         + '\n  '.join(usos))

    # --- inject_cache ------------------------------------------------------
    res = subprocess.run(
        [sys.executable, os.path.join(RAIZ, 'inject_cache.py'), ruta],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    salida_cache = res.stdout.decode('utf-8', 'replace')
    if res.returncode != 0:
        raise SystemExit('inject_cache falló:\n' + salida_cache)

    # --- verificación data_only de TODAS las fórmulas registradas ---------
    # `inject_cache.py` NO cachea las fórmulas que devuelven la cadena vacía
    # (el «sin dato» = "" de la familia): con `data_only` se leen como `None` y
    # NO son un fallo. Cada `None` se vuelve a evaluar con pycel y se exige que
    # dé exactamente ''.
    wbf = openpyxl.load_workbook(ruta)
    wbv = openpyxl.load_workbook(ruta, data_only=True)
    sin_valor, con_error, sin_dato, pendientes = [], [], [], []
    for hoja, coord, formula in motor.REGISTRO:
        v = wbv[hoja][coord].value
        if v is None:
            pendientes.append((hoja, coord, formula))
        elif isinstance(v, str) and v.startswith('#'):
            con_error.append('%s!%s  %s -> %s' % (hoja, coord, formula[:70], v))
    if pendientes:
        xl = compilador(ruta)
        for hoja, coord, formula in pendientes:
            try:
                r = xl.evaluate("'%s'!%s" % (hoja, coord))
            except Exception as e:                            # noqa: BLE001
                sin_valor.append('%s!%s  %s -> pycel: %s'
                                 % (hoja, coord, formula[:70], e))
                continue
            if r == '' or (r is None and formula.count('""')):
                sin_dato.append('%s!%s' % (hoja, coord))
            else:
                sin_valor.append('%s!%s  %s -> %r'
                                 % (hoja, coord, formula[:70], r))
    if sin_valor or con_error:
        raise SystemExit(
            'VERIFICACIÓN data_only FALLIDA en %s\n  sin valor (%d):\n   %s\n'
            '  con error (%d):\n   %s'
            % (nombre, len(sin_valor), '\n   '.join(sin_valor[:40]),
               len(con_error), '\n   '.join(con_error[:40])))

    # --- gate de totales: cada `=SUM(rango)` cachea lo que suma ------------
    incoherentes = []
    for hoja, coord, formula in motor.REGISTRO:
        m = _RX_SUM.match(formula)
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

    # --- celdas verdes vacías (regla 2 de §2.3) ---------------------------
    verdes_vacias, n_verdes = [], 0
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                if motor.es_verde(c):
                    n_verdes += 1
                    if c.value is None or (isinstance(c.value, str)
                                           and not c.value.strip()):
                        verdes_vacias.append('%s!%s'
                                             % (ws.title, c.coordinate))
    if verdes_vacias:
        raise SystemExit('CELDAS VERDES VACÍAS en %s (regla 2 de §2.3):\n  %s'
                         % (nombre, '\n  '.join(verdes_vacias[:40])))

    # --- mapa de celdas citables ------------------------------------------
    mapa = {}
    for etiqueta, hoja, coord, tipo in mapa_celdas:
        if hoja not in wbv.sheetnames:
            raise SystemExit('El mapa cita la hoja inexistente %r' % hoja)
        v = wbv[hoja][coord].value
        if v is None or (isinstance(v, str) and not v.strip()):
            raise SystemExit('El mapa cita %s!%s («%s») y está VACÍA'
                             % (hoja, coord, etiqueta))
        if etiqueta in mapa:
            raise SystemExit('Etiqueta de mapa repetida: %r' % etiqueta)
        if hasattr(v, 'isoformat'):
            v = v.isoformat()[:10]
        mapa[etiqueta] = {'ref': '%s.xlsx!%s!%s' % (nombre, hoja, coord),
                          'valor': v, 'tipo': tipo}
    if len(mapa) < 25:
        raise SystemExit('El mapa de %s tiene %d etiquetas: el mínimo son 25'
                         % (nombre, len(mapa)))
    # A8 (refutación 2026-09-12): antes se publicaba aquí una entrada
    # `_notas` con `tipo: 'nota'`, que no es uno de los tres tipos válidos
    # del mapa (`entrada|salida|parametro`) y cuyo `valor` no era el de
    # ninguna celda. `notas_mapa` sigue entrando como parámetro pero ya no
    # se escribe en el JSON.
    with open(os.path.join(destino, 'mapa-' + nombre + '.json'), 'w',
              encoding='utf-8') as fh:
        json.dump(mapa, fh, ensure_ascii=False, indent=1)

    return {
        'ruta': ruta,
        'hojas': len(wbf.worksheets),
        'formulas': len(motor.REGISTRO),
        'sin_dato': len(sin_dato),
        'verdes': n_verdes,
        'verdes_vacias': verdes_vacias,
        'notas_legales': len(NOTAS_LEGALES),
        'notas_sector': len(NOTAS_SECTOR),
        'mapa': len([k for k in mapa if not k.startswith('_')]),
        'cache': (salida_cache.strip().splitlines() or [''])[-1],
    }


def compilador(ruta):
    """`pycel.ExcelCompiler` sobre el fichero ya escrito, para los `demo()`."""
    import logging
    logging.disable(logging.CRITICAL)
    from pycel import ExcelCompiler
    return ExcelCompiler(ruta)


def resumen(nombre, res, demos):
    ok = all(d[1] for d in demos)
    print('')
    print('=== %s ===' % nombre)
    print('  fichero          : %s' % res['ruta'])
    print('  hojas            : %d' % res['hojas'])
    print('  fórmulas         : %d  (todas con valor cacheado y sin #error)'
          % res['formulas'])
    print('  de ellas «sin dato» a propósito (""): %d' % res['sin_dato'])
    print('  celdas verdes    : %d  · vacías: %d'
          % (res['verdes'], len(res['verdes_vacias'])))
    print('  notas legales    : %d · notas de fuente sectorial: %d'
          % (res['notas_legales'], res['notas_sector']))
    print('  mapa             : %d etiquetas' % res['mapa'])
    print('  inject_cache     : %s' % res['cache'])
    print('  demos            : %s' % ('OK' if ok else 'FALLAN'))
    for nombre_d, bien, detalle in demos:
        print('    [%s] %s — %s' % ('ok' if bien else 'NO', nombre_d, detalle))
    if not ok:
        raise SystemExit('Algún demo del libro no pasa.')
    return ok
