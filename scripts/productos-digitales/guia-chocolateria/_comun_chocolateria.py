#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_comun_chocolateria.py — utilidades de formato compartidas por los constructores
de los libros de «Cómo Montar una Chocolatería».

No es un motor paralelo: `motor.py` sigue siendo el que pone las verdes, las
fórmulas registradas, los semáforos, las validaciones y la protección. Aquí
sólo vive lo que la familia repite en CADA generador (cabeceras, A4, notas al
pie) más las dos cosas que este producto necesita y `motor.py` no puede dar:

* **`VERSION_LINE` propio.** `motor.version_line()` devuelve literalmente
  «Versión 2.0 · agosto 2026 · …» (motor.py:203-215): es la línea de la familia
  `guias-v2_0`, que va por su versión 2.0. Este producto NACE en 1.0 y en
  septiembre de 2026, así que la línea se escribe aquí, con el mismo formato y
  la misma regex de la familia (`motor.RX_VERSION`).
* **`dv_rango()`.** `motor.dv_lista()` construye la validación con una cadena
  de opciones separadas por comas, y la SPEC §2.2 exige que TODA lista vaya
  contra un RANGO de la propia hoja. Se escribe el vocabulario en un bloque
  «Listas de validación» al pie de la hoja y se apunta ahí.

Calcado de `guia-pasteleria/_comun_pasteleria.py` (SPEC §2.4): mismas dos
razones para existir —`VERSION_LINE` propio del producto y `dv_rango()` contra
rango— y los mismos gates (`barrer_cp1252`, `gate_sum_rango`).

Via: Claude Code
"""
import os
import sys

from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.page import PageMargins
from openpyxl.worksheet.properties import PageSetupProperties

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..'))
if os.path.join(RAIZ, 'guias-v2_0') not in sys.path:
    sys.path.insert(0, os.path.join(RAIZ, 'guias-v2_0'))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import motor                                                   # noqa: E402

#: Directorio de salida de los 9 libros. Overridable con `GUIA_BUILD_DIR`
#: (fixer de segunda pasada, 2026-09-12: probar los generadores en un
#: directorio temporal ANTES de escribir sobre `build/`, que otro agente está
#: leyendo para el guion). Sin la variable, el comportamiento no cambia.
BUILD_DIR = os.environ.get('GUIA_BUILD_DIR') or os.path.join(AQUI, 'build')

PID = 'guia-chocolateria-obrador'
PRODUCTO = 'Cómo Montar una Chocolatería'
SUBTITULO = 'AI Chef Pro · aichef.pro — ' + PRODUCTO

#: La línea de versión de ESTE producto (ver el docstring: `motor.version_line`
#: es la de la familia 2.0). Cumple `motor.RX_VERSION`.
VERSION_LINE = ('Versión 1.0 · septiembre 2026 · aichef.pro/' + PID
                + ' · info@aichef.pro')
#: `motor.BIO_LINE` lleva el sufijo « · johnguerrero.es» de la familia
#: `guias-v2_0`. El literal de la SPEC de ESTE producto termina en punto, sin
#: sufijo (auditoría 2026-09-10, hallazgo A4): se declara aquí en vez de tomar
#: la de `motor` para que los ocho libros publiquen la misma frase.
BIO = ('Diseñado por John Guerrero — chef y consultor gastronómico desde 2010, '
       'en cocina desde los 17 años.')
assert motor.RX_BIO.search(BIO)
#: `motor.NOTA_DESPROTEGER` lleva una FLECHA (U+2192) que no cabe en cp1252 y
#: rompe la regla WinAnsi de la SPEC. Misma frase, mismo significado y misma
#: regex de la familia (`motor.RX_DESPROTEGER`), con «>» en vez de flecha.
NOTA_DESPROTEGER = ('Para editar la estructura o una celda que no esté en '
                    'verde: Revisar > Desproteger hoja (no tiene contraseña).')
assert motor.RX_DESPROTEGER.match(NOTA_DESPROTEGER)
NOTA_DESPROTEGER.encode('cp1252')
NOTA_VERDES = motor.NOTA_VERDES

FMT_EUR = motor.FMT_EUR
FMT_PCT = motor.FMT_PCT
FMT_ENT = motor.FMT_ENT
FMT_FECHA = motor.FMT_FECHA
FMT_DEC = '#,##0.00'
FMT_DEC1 = '#,##0.0'
FMT_M2 = '#,##0.0 "m2"'
FMT_EURM2 = '#,##0 "EUR/m2"'

GRIS = 'F2F2F2'
CREMA = 'FFF6DC'
ORO = 'FFD700'
CABECERA = '2D2D2D'
AZUL = 'DCE6F1'

ETIQUETA_LISTAS = 'Listas de validación (no las borres: las usan los desplegables)'

#: Conectores cortos que van en minúscula en Title Case español, salvo si son
#: la primera palabra del título o van justo después de dos puntos
#: (refutación 2026-09-12, hallazgo A9: faltaban «por», «vs», «que» y «se» —
#: de ahí «CAPEX Por Bloque», «Capacidad Vs Demanda» y «... Que Viene» mal—).
#: Verificación 2026-09-12 (segunda pasada): seguía faltando «sobre», de ahí
#: `campanas-y-valle-del-ano.xlsx!Peso sobre el Año!A1` = «Peso Sobre el
#: Año» -la propia PESTAÑA ya lo llevaba bien-. Se añaden también «tras»,
#: «según» y «desde», del mismo grupo gramatical (preposiciones cortas), y
#: la ampliación se simuló contra los 55 títulos de hoja del pack ANTES de
#: aplicarse: sólo cambia «Peso sobre el Año», ningún otro título se mueve.
#: OJO: «qué» interrogativo (con tilde) NO entra aquí a propósito: se queda
#: en mayúscula («Qué Fecha te Corre»).
_MENORES_TC = {'y', 'e', 'o', 'u', 'de', 'del', 'la', 'el', 'los', 'las',
              'en', 'a', 'al', 'para', 'con', 'su', 'sus', 'un', 'una',
              'por', 'vs', 'que', 'se', 'te', 'sobre', 'tras', 'según',
              'desde'}


def titulo_hoja(texto):
    """Title Case español (SPEC §2.2): significativas en mayúscula inicial,
    conectores cortos en minúscula salvo en primera posición o justo tras
    ':' (que reabre mayúscula, como el principio del título). Se aplica al A1
    de cada hoja para que coincida con la pestaña (que ya nace en Title Case).
    """
    palabras = texto.split(' ')
    out = []
    forzar_mayus = True
    for p in palabras:
        limpio = p.lower().strip(':,;.()')
        if not forzar_mayus and limpio in _MENORES_TC:
            out.append(p.lower())
        else:
            out.append(p[:1].upper() + p[1:] if p else p)
        forzar_mayus = p.endswith(':')
    return ' '.join(out)


#: Caracteres fuera de cp1252 tolerados a propósito (espacio fino de unidad:
#: precedente en `guia-food-cost` ya publicado). Cualquier otro no-WinAnsi
#: aborta el cierre del libro (hallazgo A5).
_CP1252_TOLERADOS = {motor.NARROW}


def barrer_cp1252(wb):
    """Recorre todas las celdas de texto del libro y aborta si hay algún
    carácter fuera de WinAnsi (cp1252) que no esté en la lista de tolerados."""
    fallos = []
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell' or not isinstance(c.value, str):
                    continue
                for ch in c.value:
                    if ch in _CP1252_TOLERADOS:
                        continue
                    try:
                        ch.encode('cp1252')
                    except UnicodeEncodeError:
                        fallos.append('%s!%s: %r (U+%04X)'
                                      % (ws.title, c.coordinate, ch, ord(ch)))
    if fallos:
        raise SystemExit('Caracteres fuera de WinAnsi (cp1252):\n  '
                         + '\n  '.join(fallos[:40]))


def inmovilizar(ws, fila_cabecera=1, col='A'):
    """`freeze_panes` justo debajo de la fila de cabecera (hallazgo B12)."""
    ws.freeze_panes = '%s%d' % (col, fila_cabecera + 1)


import re as _re
_RX_SUM_RANGO = _re.compile(r'^=SUM\(([A-Z]{1,2})(\d+):([A-Z]{1,2})(\d+)\)$')


def gate_sum_rango(wbv):
    """Recalcula a mano todo `=SUM(rango)` de `motor.REGISTRO` contra la suma
    real de su rango en el libro `data_only`. `pycel` cachea como `0` un `SUM`
    que agrega una fila de `SUMPRODUCT` (medido el 10-09-2026 en
    `Turnos Semanales!E24/E25` y `Contador!B27`, hallazgos A1 y A3): el `SUM`
    en sí no es una fórmula prohibida, pero un total mal agregado se publica
    sin error y sin aviso. Devuelve la lista de incoherencias (vacía si OK)."""
    incoherentes = []
    for hoja, coord, formula in motor.REGISTRO:
        m = _RX_SUM_RANGO.match(formula)
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
    return incoherentes


# --------------------------------------------------------------------------
def anchos(ws, mapa):
    for letra, ancho in mapa.items():
        ws.column_dimensions[letra].width = ancho


def cabecera(ws, fila, columnas, altura=30):
    """`columnas` = ((letra, texto), …). Fila de cabecera negra con texto blanco.

    Congela los paneles justo debajo de esta fila por defecto (refutación
    2026-09-12, hallazgo A10: los libros 1, 2, 3, 4 y 6 no llevaban
    `freeze_panes` en NINGUNA hoja, y en una tabla de 28-44 filas se pierde la
    cabecera al primer scroll). Una llamada posterior a `inmovilizar()` con
    otra columna (para fijar además unas columnas de identificación) pisa
    este valor por defecto sin problema."""
    for letra, texto in columnas:
        c = ws[letra + str(fila)]
        c.value = texto
        c.fill = PatternFill('solid', fgColor=CABECERA)
        c.font = Font(bold=True, color='FFFFFF', size=10)
        c.alignment = Alignment(horizontal='center', vertical='center',
                                wrap_text=True)
    ws.row_dimensions[fila].height = altura
    ws.freeze_panes = 'A%d' % (fila + 1)


def seccion(ws, coord, texto):
    motor.val(ws, coord, texto, bold=True)
    ws[coord].font = Font(bold=True, size=12)


def nota(ws, coord, texto, italica=True, tam=9):
    motor.val(ws, coord, texto, wrap=True)
    ws[coord].font = Font(italic=italica, size=tam)


def parrafo(ws, fila, texto, col_ini='A', col_fin='F', alto=30, tam=9):
    ws.merge_cells('%s%d:%s%d' % (col_ini, fila, col_fin, fila))
    motor.val(ws, '%s%d' % (col_ini, fila), texto, wrap=True)
    ws['%s%d' % (col_ini, fila)].font = Font(italic=True, size=tam)
    ws.row_dimensions[fila].height = alto


def destacado(ws, coord, fondo=CREMA):
    ws[coord].fill = PatternFill('solid', fgColor=fondo)
    ws[coord].font = Font(bold=True, size=11)


def pagina(ws, apaisado=True, titulos=None, area=None):
    ws.page_setup.paperSize = 9                      # A4
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
    motor.val(ws, 'A1', titulo_hoja(titulo))
    ws['A1'].font = Font(bold=True, size=16, color=ORO)
    ws.row_dimensions[1].height = 28
    motor.val(ws, 'A2', SUBTITULO)
    if nota_txt:
        ws.merge_cells('A3:%s3' % col_fin)
        motor.val(ws, 'A3', nota_txt, wrap=True)
        ws['A3'].font = Font(italic=True, size=9)
        ws.row_dimensions[3].height = 26


def dv_rango(ws, coords, ref, titulo, mensaje, prompt=None):
    """Desplegable contra un RANGO de la propia hoja (SPEC §2.2: nunca una
    lista de opciones separadas por comas)."""
    if not coords:
        return None
    dv = DataValidation(type='list', formula1=ref, allow_blank=False,
                        showErrorMessage=True, errorTitle=titulo,
                        error=mensaje)
    if prompt:
        dv.showInputMessage = True
        dv.promptTitle = titulo
        dv.prompt = prompt
    ws.add_data_validation(dv)
    for c in coords:
        dv.add(c)
    return dv


def bloque_listas(ws, fila, listas, col='A'):
    """Escribe el vocabulario de los desplegables al pie de la hoja y devuelve
    `{nombre: referencia absoluta al rango}`. `listas` = ((nombre, (op, …)), …).
    """
    seccion(ws, col + str(fila), ETIQUETA_LISTAS)
    fila += 1
    refs = {}
    letra = col
    from openpyxl.utils import column_index_from_string, get_column_letter
    base = column_index_from_string(col)
    for i, (nombre, opciones) in enumerate(listas):
        letra = get_column_letter(base + i)
        motor.val(ws, letra + str(fila), nombre, bold=True)
        for j, op in enumerate(opciones):
            motor.val(ws, letra + str(fila + 1 + j), op)
        refs[nombre] = ('=$%s$%d:$%s$%d'
                        % (letra, fila + 1, letra, fila + len(opciones)))
    alto = max(len(o) for _n, o in listas)
    return refs, fila + alto + 2


def pie(ws, fila, col='A', col_fin='C'):
    """Bio anclada + línea de versión al pie de la hoja de Instrucciones."""
    ws.merge_cells('%s%d:%s%d' % (col, fila, col_fin, fila))
    motor.val(ws, '%s%d' % (col, fila), BIO, wrap=True)
    fila += 1
    ws.merge_cells('%s%d:%s%d' % (col, fila, col_fin, fila))
    motor.val(ws, '%s%d' % (col, fila), VERSION_LINE, wrap=True)
    return fila + 1
