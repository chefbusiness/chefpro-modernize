# -*- coding: utf-8 -*-
"""
_comun_libros_8_9.py — cierre común de los libros 8 y 9 de «Cómo Montar una
Chocolatería» (SPEC §2.2, filas 8 y 9; constructor C5).

`_comun_chocolateria.py` (de otro constructor) trae el FORMATO de la familia:
cabeceras, A4, Title Case, `dv_rango()`, `bloque_listas()`, `barrer_cp1252()` y
la línea de versión 1.0. Lo que NO trae —y es lo que la SPEC pide a cada
generador al terminar— vive aquí, calcado de
`guia-pasteleria/_comun_libros_5_6.py` y `_comun_libros_3_5.py`:

  1. `entrada()`: celda VERDE con su valor por defecto REGISTRADO (regla 2 de
     §2.3: ninguna celda verde vacía).
  2. `nota_celda()`: la nota legal de `datos_ejemplo.nota_legal(id)` como
     comentario de la celda, contada para el resumen.
  3. `nota_fuente()`: lo mismo para un id de SECTOR (`CHS-*`), que no está en la
     verificación legal sino en el JSON común, y por eso NO se cuenta como nota
     legal: es procedencia de un dato de mercado, no de una norma.
  4. `cerrar()`: guardar, `inject_cache.py`, verificación `data_only` de TODAS
     las fórmulas registradas (distinguiendo con pycel las que devuelven `""` a
     propósito), gate de totales `=SUM(rango)`, gate de verdes vacías, gate de
     funciones prohibidas, barrido WinAnsi y `build/mapa-<libro>.json`.

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

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..'))
if os.path.join(RAIZ, 'guias-v2_0') not in sys.path:
    sys.path.insert(0, os.path.join(RAIZ, 'guias-v2_0'))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import motor                                                   # noqa: E402
import datos_ejemplo as D                                      # noqa: E402
import _comun_chocolateria as C                                # noqa: E402

motor.CTX['producto'] = C.PID

SUBJECT = C.PRODUCTO + ' · Versión 1.0 · septiembre 2026'

#: Alias cortos de formato, para que los generadores de este constructor no
#: escriban `C.FMT_*` cincuenta veces.
EUR = C.FMT_EUR
PCT = C.FMT_PCT
PCT2 = '0.00%'
ENT = C.FMT_ENT
FECHA = C.FMT_FECHA
DEC = C.FMT_DEC
DEC1 = C.FMT_DEC1

#: Contador de notas legales puestas por el generador en curso.
NOTAS_LEGALES = []
#: Notas de procedencia de datos de SECTOR (`CHS-*`): no son notas legales.
NOTAS_SECTOR = []
#: Celdas verdes declaradas por el generador: (hoja, coord, etiqueta, valor).
VERDES = []


# --------------------------------------------------------------------------
# Entradas y notas
# --------------------------------------------------------------------------
def entrada(ws, coord, valor, fmt=None, etiqueta='', bold=None, align=None,
            wrap=None):
    """Celda VERDE de entrada, con su valor por defecto declarado (regla 2)."""
    if valor is None or (isinstance(valor, str) and not valor.strip()):
        raise SystemExit('entrada(%s!%s) sin valor por defecto: la regla 2 de '
                         '§2.3 prohíbe una celda verde vacía' % (ws.title, coord))
    cel = motor.val(ws, coord, valor, fmt=fmt, verde_=True, bold=bold,
                    align=align, wrap=wrap)
    VERDES.append((ws.title, coord, etiqueta, valor))
    return cel


def total_fila(ws, fila, letras, fondo=None):
    """Resalta una fila de total (negrita + fondo crema de la familia)."""
    from openpyxl.styles import Font, PatternFill
    for letra in letras:
        c = ws[letra + str(fila)]
        c.font = Font(bold=True, size=c.font.size)
        c.fill = PatternFill('solid', fgColor=fondo or C.CREMA)


#: Filas de CUADRE declaradas por el generador en curso (D32): una por cada
#: celda verde «trae aquí la cifra de <fichero>.xlsx!<Hoja>». `cerrar()` exige
#: que salgan tantas como celdas «trae aquí» se hayan escrito.
CRUCES_VERDES = []
CRUCES_CUADRE = []


def cruce_verde(ws, coord, valor, fmt=None, etiqueta=''):
    """Celda verde de un CRUCE entre libros (D32). Se contabiliza aparte para
    que `cerrar()` compruebe que tiene su fila de CUADRE en la misma hoja."""
    cel = entrada(ws, coord, valor, fmt=fmt, etiqueta=etiqueta)
    CRUCES_VERDES.append((ws.title, coord, etiqueta))
    return cel


def cruce_cuadre(ws, coord, formula, bold=True):
    """Fila de CUADRE de un cruce: fórmula de veredicto + semáforo de texto."""
    cel = motor.f(ws, coord, formula, bold=bold)
    CRUCES_CUADRE.append((ws.title, coord))
    return cel


def nota_celda(ws, coord, id_chn):
    """Nota LEGAL de `id_chn` como comentario de la celda (regla 1 de §2.3):
    «Verificado el 12-09-2026 · norma y artículo · URL»."""
    texto = D.nota_legal(id_chn)
    if not texto:
        raise SystemExit('nota_legal(%r) no devuelve nada: gate_legal debería '
                         'haber abortado antes' % id_chn)
    ws[coord].comment = Comment(_winansi(texto), 'AI Chef Pro', height=120,
                                width=460)
    NOTAS_LEGALES.append((ws.title, coord, id_chn))
    return texto


def nota_fuente(ws, coord, id_chs, extra=None):
    """Procedencia de un dato de SECTOR (`CHS-*`) como comentario. No es una
    nota legal y no se cuenta como tal: la regla 1 de §2.3 habla de datos
    legales. Aborta si el id no existe LITERALMENTE en el JSON común (D44: hay
    ids bare que sólo existen con sufijo)."""
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
    ws[coord].comment = Comment(texto, 'AI Chef Pro', height=120, width=460)
    NOTAS_SECTOR.append((ws.title, coord, id_chs))
    return texto


def cita_legal(id_chn):
    """La `cita_literal` de la verificación legal del 12-09-2026, que es la
    fuente de verdad de lo legal (SPEC §2.3, regla 1) y MANDA sobre la síntesis.

    Existe porque `datos_ejemplo.py` publica algunos entrecomillados con los
    acentos quitados —p. ej. `NOTA_644_5` dice «la fabricacion de bombones…»
    donde el BOE dice «La fabricación de bombones…»—, y un texto entre comillas
    que no coincide con la norma deja de ser una cita. Devuelve `None` si el id
    no trae cita literal, para que el llamante decida.
    """
    fila = D._carga_verificacion_legal()['entradas'].get(str(id_chn).strip())
    if not fila:
        return None
    cita = fila.get('cita_literal')
    return cita.strip() if isinstance(cita, str) and cita.strip() else None


def _winansi(texto):
    """Los comentarios no los barre `barrer_cp1252` (sólo mira valores de
    celda), y las fichas del JSON traen emojis. Se limpian aquí."""
    out = []
    for ch in texto:
        try:
            ch.encode('cp1252')
        except UnicodeEncodeError:
            continue
        out.append(ch)
    return re.sub(r'\s+', ' ', ''.join(out)).strip()


# --------------------------------------------------------------------------
# Cierre
# --------------------------------------------------------------------------
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

    C.barrer_cp1252(wb)

    for ws in wb.worksheets:
        motor.retirar_verde_de_calculadas(ws)
        motor.proteger(ws)

    destino = os.path.join(AQUI, 'build')
    os.makedirs(destino, exist_ok=True)
    ruta = os.path.join(destino, nombre + '.xlsx')
    wb.save(ruta)

    # --- inject_cache ------------------------------------------------------
    res = subprocess.run([sys.executable,
                          os.path.join(RAIZ, 'inject_cache.py'), ruta],
                         capture_output=True, text=True)
    salida_cache = (res.stdout or '') + (res.stderr or '')
    if res.returncode != 0:
        raise SystemExit('inject_cache falló:\n' + salida_cache)

    # --- verificación data_only -------------------------------------------
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
        from pycel import ExcelCompiler
        xl = ExcelCompiler(ruta)
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

    # --- gate de totales: cada `=SUM(rango)` cachea lo que suma -------------
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

    # --- celdas verdes vacías (regla 2 de §2.3) ----------------------------
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
                        verdes_vacias.append('%s!%s' % (ws.title, c.coordinate))
    if verdes_vacias:
        raise SystemExit('CELDAS VERDES VACÍAS en %s (regla 2 de §2.3):\n  %s'
                         % (nombre, '\n  '.join(verdes_vacias[:40])))

    # --- funciones prohibidas y referencias entre libros -------------------
    prohibidas = ('INDIRECT', 'COUNTA', 'PMT(', 'OFFSET', 'XLOOKUP', 'LET(',
                  'LAMBDA', 'RANK(', 'NETWORKDAYS', 'IRR(')
    usos = []
    for hoja, coord, formula in motor.REGISTRO:
        arriba = formula.upper()
        for p in prohibidas:
            if p in arriba:
                usos.append('%s!%s usa %s' % (hoja, coord, p.rstrip('(')))
        if '.XLSX' in arriba or '[' in formula:
            usos.append('%s!%s NOMBRA OTRO FICHERO: %s' % (hoja, coord, formula))
    if usos:
        raise SystemExit('Funciones PROHIBIDAS o referencia externa:\n  '
                         + '\n  '.join(usos))

    # --- cruces (D32): cada verde «trae aquí» con su fila de CUADRE --------
    if len(CRUCES_VERDES) != len(CRUCES_CUADRE):
        raise SystemExit(
            'CRUCES descuadrados en %s: %d celdas verdes «trae aquí» y %d '
            'filas de CUADRE.\n  verdes: %r\n  cuadres: %r'
            % (nombre, len(CRUCES_VERDES), len(CRUCES_CUADRE),
               CRUCES_VERDES, CRUCES_CUADRE))
    for (hv, cv, et), (hc, cc) in zip(CRUCES_VERDES, CRUCES_CUADRE):
        if hv != hc:
            raise SystemExit('El cruce «%s» tiene la verde en %r y el CUADRE '
                             'en %r: deben ir en la MISMA hoja' % (et, hv, hc))

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
    if len(mapa) < 25:
        raise SystemExit('El mapa de %s tiene %d etiquetas: el mínimo son 25'
                         % (nombre, len(mapa)))
    if notas_mapa:
        mapa['_notas'] = {'ref': '%s.xlsx!%s!A1'
                                 % (nombre, wb.worksheets[0].title),
                          'valor': notas_mapa, 'tipo': 'nota'}
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
        'mapa': len([k for k in mapa if k != '_notas']),
        'cruces': len(CRUCES_VERDES),
        'cache': (salida_cache.strip().splitlines()[-1]
                  if salida_cache.strip() else ''),
    }
