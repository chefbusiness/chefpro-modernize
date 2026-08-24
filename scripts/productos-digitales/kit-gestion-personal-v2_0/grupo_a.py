#!/usr/bin/env python3
"""
grupo_a.py — Grupo A del Kit de Gestión de Personal y Turnos v2.0:
**el tiempo de trabajo**. Cubre el §2 de `kit-gestion-personal-v2-SPEC.md`:

  · `01-cuadrante-turnos-semanal.xlsx`  — hoja nueva `Turnos`, el bloque
    auxiliar oculto `P:AP` y las **4 alertas legales** del cuadrante semanal
    (DOM-05/DOM-25/TEC-05/COM-01), más la reconstrucción del `Cuadrante
    Mensual`, que hoy es una rejilla muerta (DOM-17/TEC-23/COM-12).
  · `02-control-horas-extras.xlsx`      — cruce de medianoche y turno partido
    (DOM-03/DOM-21/TEC-01/COM-07), guarda de «H. Contratadas» vacía
    (DOM-11/TEC-09), `Resumen Mensual` que AGREGA por `SUMIF` con el recargo
    como parámetro y el contador de las 80 h/año (DOM-07/TEC-06/TEC-08/
    COM-02/COM-14) y la cita legal correcta (DOM-12/COM-19).
  · `BONUS-01-briefing-cambio-turno.xlsx` — bloques de CAJA y de TEMPERATURAS
    (DOM-29) y `wrap_text` en las observaciones (TEC-24).

Interfaz que espera `main.py` (`procesar()`): `FICHEROS`, `pre(wb, fname,
cambios)`, `post(wb, fname, cambios, registro_grupo)` y `demos(carpeta,
origen)`. NO se declara `PROPIOS`: los tres ficheros pasan por el motor §1.

REGLA DE ORO del pipeline (main.py): las COLUMNAS se insertan en `pre()`
—antes de que el motor fije rangos— y las FILAS se añaden en `post()`.

IDEMPOTENCIA. Todo lo que este módulo escribe es o bien escritura ABSOLUTA
sobre una celda, o bien una reconstrucción completa de la hoja (`Turnos` y
`Cuadrante Mensual` se borran y se vuelven a crear). Los objetos ACUMULABLES
—validaciones y formato condicional— se limpian por marca antes de
reescribirse: sin eso, la 2.ª pasada duplica cada DV y cada regla, y la
diferencia no se ve en el contenido pero sí en el fichero.

⚠ Dos cosas que el motor NO puede hacer por este grupo, y por eso van aquí:
  1. `motor.DV_LISTA['02-…']` busca «Tipo Extra» en la **columna H**. La v2.0
     mete «Pausa (h)» en E y el Tipo se va a la I, así que ese centinela ya no
     casa nunca: la DV de las 4 modalidades de hora extra (art. 35.2) la pone
     este módulo, con marca propia `grupoA` para que `motor._limpiar_dv` —que
     barre por el prefijo `kitgp-v2`— no se la lleve por delante.
  2. `motor.CF_COLUMNA['BONUS-01…']` apunta a `Briefing!D` con centinela
     «Conforme», que sólo existe en el bloque de temperaturas que crea este
     módulo y que NO está en `motor.BLOQUES`. El semáforo de ese bloque se
     pinta aquí.

Python 3.7 / openpyxl 3.1.3: sin walrus ni f-strings de depuración.
"""
import copy
import os
import re
import sys

from openpyxl.styles import Alignment, Font, PatternFill, Protection
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

import motor

# ==========================================================================
# Identidad del grupo
# ==========================================================================
FICHEROS = [
    '01-cuadrante-turnos-semanal.xlsx',
    '02-control-horas-extras.xlsx',
    'BONUS-01-briefing-cambio-turno.xlsx',
]

F01, F02, FB1 = FICHEROS

#: Marca de MIS validaciones. Deliberadamente NO empieza por `kitgp-v2`:
#: `motor._limpiar_dv` borra todo lo que case con ese prefijo, y una DV mía
#: barrida por el motor desaparecería sin que ningún gate lo notara (el motor
#: sólo re-escribe LAS SUYAS).
MARCA_A = 'grupoA-v2'
#: El prefijo que sí usa el motor, para poder limpiar las DV informativas que
#: `motor.parametro()` deja en las hojas que el motor luego no barre (Resumen
#: Mensual y Turnos no están en `motor.DV_LISTA`, así que nadie las limpiaría
#: y se DUPLICARÍAN en cada pasada).
MARCA_MOTOR = motor.MARCA_DV + ' · '

#: §1.3 — 30 empleados en toda hoja indexada por empleado.
CAP = motor.CAPACIDAD                       # 30
FILAS_REG = motor.FILAS_REGISTRO            # 300

#: Bloque auxiliar OCULTO del cuadrante semanal (§2). 7 + 7 + 7 + 6 = 27
#: columnas, de la P a la AP. No llevan cabecera en la fila 5 A PROPÓSITO: el
#: motor deduce formato y verde por el texto de esa fila, y una cabecera aquí
#: metería 27 columnas auxiliares en `aplicar_verde`. La etiqueta va en la
#: fila 4, que el motor no mira, para quien las muestre.
AUX_HORAS = 16      # P..V  · horas de cada día
AUX_INI = 23        # W..AC · hora de inicio
AUX_FIN = 30        # AD..AJ· hora de fin
AUX_TRANS = 37      # AK..AP· las 6 transiciones entre jornadas
AUX_ULT = 42        # AP

DIAS = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado',
        'Domingo')

#: Rango de la tabla de turnos, tal cual lo referencian todas las fórmulas.
TURNOS_TABLA = 'Turnos!$A$5:$E$12'
TURNOS_JORNADA_MAX = 'Turnos!$B$2'
TURNOS_DESCANSO = 'Turnos!$B$3'

BLANCO = Font(color='FFFFFF', bold=True, size=10)
NEGRITA = Font(bold=True)
CENTRO = Alignment(horizontal='center', vertical='center')


# ==========================================================================
# Utilidades locales
# ==========================================================================
def _f(ws, coord, formula):
    """Escribe una fórmula y la REGISTRA para que `main.py` verifique con
    `data_only` que quedó con valor cacheado (o que pycel confirma que vale la
    cadena vacía)."""
    ws[coord] = motor._reg(ws, coord, formula)
    return formula


def _cab(ws, fila, textos, col0=1):
    """Fila de cabecera con el estilo oscuro del kit."""
    for i, t in enumerate(textos):
        cel = ws.cell(row=fila, column=col0 + i)
        cel.value = t
        cel.fill = PatternFill('solid', fgColor=motor.CAB)
        cel.font = BLANCO
        cel.alignment = Alignment(horizontal='center', vertical='center',
                                  wrap_text=True)
    ws.row_dimensions[fila].height = 30


def _titulo_bloque(ws, fila, texto, ultima_col):
    """Banda de título de un bloque, combinada de A a `ultima_col`."""
    ref = 'A{f}:{c}{f}'.format(f=fila, c=get_column_letter(ultima_col))
    if ref not in [str(m) for m in ws.merged_cells.ranges]:
        ws.merge_cells(ref)
    cel = ws.cell(row=fila, column=1)
    cel.value = texto
    cel.font = Font(bold=True, size=11)
    cel.fill = PatternFill('solid', fgColor='EEEEEE')
    cel.alignment = Alignment(horizontal='left', vertical='center')
    ws.row_dimensions[fila].height = 20


def _fila_con(ws, col, texto, desde=1):
    """Primera fila >= `desde` cuya columna `col` contiene `texto`."""
    for r in range(desde, ws.max_row + 1):
        v = ws.cell(row=r, column=col).value
        if isinstance(v, str) and texto.lower() in v.lower():
            return r
    return None


def _cola(ws, r_ult):
    """Filas de COLA de un bloque: todo lo que tiene contenido por debajo de la
    última fila de datos (totales, notas, pie). `motor.expandir_filas` las baja
    en bloque y ESTIRA las referencias a la última fila."""
    fuera = []
    for r in range(r_ult + 1, ws.max_row + 1):
        if any(ws.cell(row=r, column=c).value is not None
               for c in range(1, ws.max_column + 1)):
            fuera.append(r)
    return tuple(fuera)


def _limpiar_mis_dv(ws, rangos=()):
    """Quita MIS validaciones (marca `grupoA-v2`), las informativas que deja
    `motor.parametro` (marca `kitgp-v2 · `) y las HEREDADAS de la v1.1 que
    pisen los rangos que voy a reescribir.

    Sin esto la 2.ª pasada acumula: `motor.parametro` añade un `DataValidation`
    nuevo en cada llamada y el motor sólo barre las hojas que él mismo gobierna
    (`Resumen Mensual` y `Turnos` no están en `motor.DV_LISTA`, así que nadie
    las limpiaría). Las heredadas hay que quitarlas porque Excel aplica la
    PRIMERA validación que encuentra: la lista vieja «Voluntaria,Obligatoria»
    seguiría ganando sobre las 4 modalidades del art. 35.2.
    """
    objetivo = set()
    for r in rangos:
        objetivo |= motor._celdas_sqref(r)
    vivas, quitadas = [], 0
    for dv in ws.data_validations.dataValidation:
        pt = getattr(dv, 'promptTitle', None) or ''
        if pt.startswith(MARCA_A) or pt.startswith(MARCA_MOTOR):
            quitadas += 1
            continue
        if objetivo and (motor._celdas_sqref(dv.sqref) & objetivo):
            quitadas += 1
            continue
        vivas.append(dv)
    ws.data_validations.dataValidation = vivas
    return quitadas


def _dv(ws, ref, valores, titulo, prompt, error, tipo='list', **extra):
    """Validación con marca propia. `showErrorMessage=True` (§ convenciones)."""
    if tipo == 'list':
        formula1 = '"{}"'.format(','.join(valores))
        if len(formula1) > 255:
            raise ValueError('DV inline de {} caracteres: {}'
                             .format(len(formula1), titulo))
        dv = DataValidation(type='list', formula1=formula1, allow_blank=True,
                            showErrorMessage=True, errorTitle=titulo,
                            error=error, errorStyle='stop',
                            showInputMessage=True,
                            promptTitle='{} · {}'.format(MARCA_A, titulo),
                            prompt=prompt)
    else:
        dv = DataValidation(type=tipo, allow_blank=True,
                            showErrorMessage=True, errorTitle=titulo,
                            error=error, errorStyle='stop',
                            showInputMessage=True,
                            promptTitle='{} · {}'.format(MARCA_A, titulo),
                            prompt=prompt, **extra)
    ws.add_data_validation(dv)
    dv.add(ref)
    return dv


def _nota_parametro(ws, fila, clave, col_rotulo=1, col_valor=2, alto=None):
    """`motor.parametro` + legibilidad: el rótulo del catálogo §1.4 es largo
    («Recargo de la hora extra (× la ordinaria) — según tu convenio») y la
    columna que lo aloja mide 16-22 caracteres, así que sin `wrap_text` se ve
    cortado y el cliente no sabe qué está editando. Se conserva el literal del
    motor —es el que explica de dónde sale el número— y se le da altura."""
    coord = motor.parametro(ws, fila, clave, col_rotulo, col_valor)
    cel = ws.cell(row=fila, column=col_rotulo)
    cel.alignment = Alignment(wrap_text=True, vertical='center')
    cel.font = NEGRITA
    if alto:
        ws.row_dimensions[fila].height = max(alto,
                                             ws.row_dimensions[fila].height
                                             or 0)
    return coord


def _instrucciones(ws, lineas):
    """Reescribe el CUERPO de `Instrucciones` entero y de forma determinista.

    `motor.linea_instrucciones` sustituye la línea que case con un patrón y, si
    no casa ninguna, la AÑADE en `max_row + 2`. Eso no es idempotente en este
    kit: el bloque de bio y versión de `motor.bio_y_version` se ancla en la
    línea de versión —que en la v1.1 es la ÚLTIMA— y pisa lo que se haya
    añadido debajo. Medido el 2026-08-24: la 1.ª pasada perdía una línea de
    cada fichero y la 2.ª la volvía a escribir dos filas más abajo → 6
    diferencias de idempotencia, una por línea nueva y otra por el `print_area`
    que crecía con ella.

    Reescribiendo el cuerpo entero no hay líneas «añadidas»: hay una lista. Las
    tres últimas son las del motor (nota de desprotección, bio y versión), que
    `bio_y_version` reconoce por su literal y reescribe EN SU SITIO.
    """
    col = motor.col_instrucciones(ws)
    estilos = {}
    for r in range(4, min(ws.max_row, 30) + 1):
        v = ws.cell(row=r, column=col).value
        if not isinstance(v, str):
            continue
        clave = 'texto' if v.startswith('▸') else 'titulo'
        if clave not in estilos:
            estilos[clave] = copy.copy(ws.cell(row=r, column=col)._style)
    for r in range(3, ws.max_row + 1):
        ws.cell(row=r, column=col).value = None
    fila = 4
    for texto in list(lineas) + [None, motor.NOTA_DESPROTEGER, motor.BIO,
                                 motor.VERSION_LINE]:
        if texto is None:
            fila += 1
            continue
        cel = ws.cell(row=fila, column=col)
        cel.value = texto
        est = estilos.get('texto' if texto.startswith('▸') else 'titulo')
        if est is not None:
            cel._style = copy.copy(est)
        cel.alignment = Alignment(wrap_text=True, vertical='top')
        fila += 1
    return fila - 1


#: Las dos líneas que `motor.escribir_leyenda` reescribe en el 01 (§1.1). Se
#: toman del motor —no se copian— para que el cuerpo que escribe este módulo
#: contenga ya su literal exacto: si no estuvieran, `linea_instrucciones` las
#: añadiría DESPUÉS del bloque de bio y versión.
def _lineas_leyenda(fname):
    return [t for f, _rx, t in motor.LINEAS_LEYENDA if f == fname]


# ==========================================================================
# 01 — hoja nueva `Turnos` (§2, DOM-05/TEC-05)
# ==========================================================================
def _hoja_turnos(wb, cambios):
    """La tabla de la que salen TODAS las horas y las cuatro alertas.

    Hoy los horarios viven dentro de la fórmula monstruo de `01!Cuadrante
    Semanal!I6` —siete `IF` anidados de 700 caracteres con el 8 y el 9
    escritos dentro— y en cinco líneas de texto de `Instrucciones!B16:B20`.
    Un restaurante que abra la mañana a las 8:00 no tiene dónde decirlo.

    Las horas van como NÚMERO de 0 a 24, no como hora de Excel: las fórmulas de
    transición hacen aritmética (`24-$AD6+$X6`) y, sobre todo, pycel devuelve un
    `datetime.time` al leer una celda con formato de hora y la multiplicación
    reventaría en `inject_cache` — la celda de resultado se quedaría en blanco
    en el visor del móvil, que es justo lo que ese script existe para evitar.
    """
    idx = wb.sheetnames.index('Instrucciones') + 1 \
        if 'Instrucciones' in wb.sheetnames else 0
    if 'Turnos' in wb.sheetnames:
        idx = wb.sheetnames.index('Turnos')
        wb.remove(wb['Turnos'])
    ws = wb.create_sheet('Turnos', idx)

    for letra, ancho in (('A', 30), ('B', 34), ('C', 14), ('D', 14),
                         ('E', 10)):
        ws.column_dimensions[letra].width = ancho

    ws.merge_cells('A1:E1')
    ws['A1'] = 'Turnos y límites legales — edítalos aquí, valen para todo el kit'
    ws['A1'].font = Font(bold=True, size=13)
    ws.row_dimensions[1].height = 22

    _nota_parametro(ws, 2, 'jornada_diaria_max', 1, 2, alto=30)
    _nota_parametro(ws, 3, 'descanso_min', 1, 2, alto=30)
    ws['C2'] = 'Art. 34.3 ET'
    ws['C3'] = 'Art. 34.3 ET'
    for coord in ('C2', 'C3'):
        ws[coord].font = Font(italic=True, size=9, color='666666')

    _cab(ws, 4, ['Código', 'Descripción', 'Hora inicio (h)', 'Hora fin (h)',
                 'Horas'])
    for i, cod in enumerate(motor.CODIGOS_JORNADA):
        fila = 5 + i
        ini = int(cod[2].split(':')[0])
        fin = int(cod[3].split(':')[0])
        ws.cell(row=fila, column=1, value=cod[0]).alignment = CENTRO
        ws.cell(row=fila, column=1).font = NEGRITA
        ws.cell(row=fila, column=1).fill = PatternFill('solid',
                                                       fgColor=cod[-1])
        ws.cell(row=fila, column=2, value=cod[1])
        for col, valor in ((3, ini), (4, fin), (5, cod[4])):
            cel = ws.cell(row=fila, column=col, value=valor)
            cel.number_format = motor.FMT_DEC2
            cel.alignment = CENTRO
    motor.marcar_verde(ws, 'B5:E12')

    ws['B13'] = ('El PARTIDO son 10:00-15:00 y 19:00-23:00: 13 h entre '
                 'extremos y 9 h efectivas. La columna «Horas» es la que '
                 'cuenta para la jornada; el inicio y el fin son los que '
                 'miden el descanso entre jornadas.')
    ws['B14'] = ('El DOBLE (D) es el turno de 16 h que dispara la alerta de '
                 'jornada diaria. Existe para poder MARCARLO y que salte, no '
                 'para planificarlo.')
    ws['B15'] = ('Escribe las horas como número: 7 son las 07:00 y 15,5 las '
                 '15:30. La columna A no se edita: esas 8 letras son las del '
                 'desplegable del cuadrante y las del calendario del 05.')
    for r in (13, 14, 15):
        ws.cell(row=r, column=2).alignment = Alignment(wrap_text=True,
                                                       vertical='top')
        ws.row_dimensions[r].height = 32
        ws.merge_cells('B{0}:E{0}'.format(r))

    cambios.append('{}:Turnos!A5:E12: tabla de los 8 turnos (horas, inicio y '
                   'fin) + parámetros B2 (jornada diaria máx. {} h) y B3 '
                   '(descanso mínimo {} h, art. 34.3 ET) — §2'
                   .format(F01, motor.PARAMETROS['jornada_diaria_max'][1],
                           motor.PARAMETROS['descanso_min'][1]))
    return ws


# ==========================================================================
# 01 — cuadrante semanal: bloque auxiliar + las 4 alertas
# ==========================================================================
def _aux_formulas(fila):
    """Las 27 fórmulas del bloque auxiliar de una fila (§2).

    ⚠ TODAS devuelven la cadena vacía cuando el día no tiene turno, y las
    alertas que las leen neutralizan ese vacío con `IF(x="",neutro,x)` en vez
    de comparar contra él. No es estilo: es lo único que hace MEDIBLE la
    batería §5 de `main.py`, y se descubrió midiendo, el 2026-08-24:

      · **pycel devuelve el valor CACHEADO de una celda de fórmula si el libro
        lo trae**, y `main.py` corre `inject_cache` (paso 3) ANTES de las
        demostraciones (paso 7). Con el auxiliar devolviendo `0`/`24` en la
        hoja vacía, `inject_cache` graba esos ceros y `demo_descanso` —que
        planifica `B6='T'`, `C6='M'` y lee `K6`— seguía leyendo el 24 cacheado:
        el gate daba «sin alerta» con la alerta perfectamente escrita. Medido:
        con cache, `P6` vale 0,0 con `B6='M'`; sobre el MISMO libro re-guardado
        sin cache, vale 8.
      · Como la cadena vacía no se cachea (`inject_cache` la salta), la cadena
        `B6 → P6 → AK6 → K6` queda entera sin cache y pycel la recalcula. El
        efecto secundario es además el que pide §1.5: la hoja recién descargada
        enseña las columnas auxiliares y el total EN BLANCO, no una pared de
        ceros.
      · Y el mismo motivo obliga a que ninguna alerta lea un RANGO de celdas de
        fórmula: pycel tampoco propaga `set_value` a través de un nodo rango
        (`K6=IF(COUNTIF($AK6:$AP6,…))` nunca recalculaba). Por eso las seis
        transiciones se comparan una a una.

    Ojo con el 0: un día marcado L, V o B SÍ tiene horas (0), así que la
    transición tiene que excluirlo explícitamente o un día libre seguido de una
    mañana daría «7 h de descanso» y una alerta falsa.
    """
    fuera = []
    for j in range(7):
        dia = get_column_letter(2 + j)
        for base, col_tabla in ((AUX_HORAS, 5), (AUX_INI, 3), (AUX_FIN, 4)):
            coord = '{}{}'.format(get_column_letter(base + j), fila)
            fuera.append((coord,
                          '=IF(${d}{f}="","",'
                          'IFERROR(VLOOKUP(${d}{f},{t},{c},FALSE),0))'
                          .format(d=dia, f=fila, t=TURNOS_TABLA, c=col_tabla)))
    for j in range(6):
        h1 = get_column_letter(AUX_HORAS + j)
        h2 = get_column_letter(AUX_HORAS + j + 1)
        ini1 = get_column_letter(AUX_INI + j)
        ini2 = get_column_letter(AUX_INI + j + 1)
        fin1 = get_column_letter(AUX_FIN + j)
        coord = '{}{}'.format(get_column_letter(AUX_TRANS + j), fila)
        fuera.append((coord,
                      '=IF(OR(${h1}{f}="",${h2}{f}="",${h1}{f}=0,${h2}{f}=0),'
                      '"",IF(${fin1}{f}<=${ini1}{f},${ini2}{f}-${fin1}{f},'
                      '24-${fin1}{f}+${ini2}{f}))'
                      .format(h1=h1, h2=h2, ini1=ini1, ini2=ini2, fin1=fin1,
                              f=fila)))
    return fuera


def _alertas_semanal(fila):
    """Las CUATRO alertas que la landing vende desde el día uno y que el
    fichero no tenía (COM-01). Cada una cita su artículo.

    Sin guarda de `$A6=""`: no hace falta y estorba. No hace falta porque una
    fila recién descargada deja el bloque auxiliar en blanco y las cuatro
    salen vacías por su propia aritmética (§1.5, y así lo mide el gate). Y
    estorba porque condicionaría la alerta a haber TECLEADO EL NOMBRE: quien
    planifica reparte turnos antes de escribir nada en la columna A, que es
    justo cuando la alerta tiene que estar viva — y es lo que hace la batería
    §5 de `main.py`, que planifica `B6`/`C6` y no toca `A6`.
    """
    p = [get_column_letter(AUX_HORAS + j) for j in range(7)]
    tr = [get_column_letter(AUX_TRANS + j) for j in range(6)]
    d, m = TURNOS_DESCANSO, TURNOS_JORNADA_MAX
    dias = '+'.join('IF(${c}{f}="",0,IF(${c}{f}>0,1,0))'.format(c=c, f=fila)
                    for c in p)
    return [
        # el total se calla con la fila vacía en vez de enseñar 30 ceros
        ('I{}'.format(fila),
         '=IF(COUNT(${a}{f}:${b}{f})=0,"",ROUND(SUM(${a}{f}:${b}{f}),2))'
         .format(a=p[0], b=p[-1], f=fila)),
        # «neutro = el propio umbral»: sin encadenamiento, d<d es FALSO sea
        # cual sea el convenio. Un literal (24, 99) mentiría con un umbral alto.
        ('K{}'.format(fila),
         '=IF(OR({o}),"⛔ <"&{d}&" h","")'
         .format(o=','.join('IF(${c}{f}="",{d},${c}{f})<{d}'
                            .format(c=c, f=fila, d=d) for c in tr), d=d)),
        ('L{}'.format(fila),
         '=IF(7-({c})=0,"⛔ 0 días",IF(7-({c})=1,'
         '"⚠ 1 día (el ET pide 1,5, acumulable en 14 días — art. 37.1)",""))'
         .format(c=dias)),
        ('M{}'.format(fila),
         '=IF(OR($I{f}="",$J{f}=""),"",IF($I{f}>$J{f},'
         '"⛔ +"&TEXT($I{f}-$J{f},"0")&" h",""))'.format(f=fila)),
        ('N{}'.format(fila),
         '=IF(OR({o}),"⛔ jornada > "&{m}&" h","")'
         .format(o=','.join('IF(${c}{f}="",0,${c}{f})>{m}'
                            .format(c=c, f=fila, m=m) for c in p), m=m)),
    ]


def _cuadrante_semanal(ws, cambios):
    r0, r1_hoy, r1 = 6, 20, 5 + CAP
    delta = motor.expandir_filas(ws, r1_hoy, r1, cola=_cola(ws, r1_hoy))
    if delta:
        cambios.append('{}:Cuadrante Semanal: bloque 6..{} → 6..{} '
                       '({} empleados, §1.3) y la cola bajada {} filas'
                       .format(F01, r1_hoy, r1, CAP, delta))

    _cab(ws, 5, ['Empleado'] + list(DIAS)
         + ['Total Horas', 'H. contratadas/semana',
            'Descanso entre jornadas', 'Descanso semanal', 'Jornada semanal',
            'Jornada diaria'])
    for letra, ancho in (('I', 13), ('J', 15), ('K', 20), ('L', 26),
                         ('M', 18), ('N', 22)):
        ws.column_dimensions[letra].width = ancho

    # etiquetas del bloque auxiliar en la fila 4 (el motor sólo mira la 5)
    for col, texto in ((AUX_HORAS, 'AUXILIAR — no editar · horas por día'),
                       (AUX_INI, 'hora de inicio'),
                       (AUX_FIN, 'hora de fin'),
                       (AUX_TRANS, 'descanso entre jornadas (h)')):
        cel = ws.cell(row=4, column=col, value=texto)
        cel.font = Font(italic=True, size=8, color='999999')

    n = 0
    for fila in range(r0, r1 + 1):
        for coord, formula in _aux_formulas(fila) + _alertas_semanal(fila):
            _f(ws, coord, formula)
            n += 1
        cel = ws.cell(row=fila, column=10)         # J · h. contratadas
        cel.value = motor.PARAMETROS['jornada_semanal'][1]
        cel.number_format = motor.FMT_DEC2
        cel.alignment = CENTRO
    for col in range(AUX_HORAS, AUX_ULT + 1):
        ws.column_dimensions[get_column_letter(col)].hidden = True

    # el TOTAL del equipo lo estira `expandir_filas`; la fila de PROMEDIO es
    # nueva y va justo debajo, con la guarda de rango vacío del §1.5.
    fila_total = _fila_con(ws, 1, 'TOTAL HORAS EQUIPO', r1 + 1)
    if fila_total:
        ws.cell(row=fila_total, column=11).value = None
        _f(ws, 'K{}'.format(fila_total),
           motor.guarda_media('$I${}:$I${}'.format(r0, r1)))
        ws.cell(row=fila_total, column=10,
                value='Media por empleado →').font = NEGRITA
        ws.cell(row=fila_total, column=10).alignment = Alignment(
            horizontal='right')
        n += 1

    cambios.append('{}:Cuadrante Semanal!I{}:N{}: {} fórmulas — bloque '
                   'auxiliar oculto {}:{} (horas, inicio, fin y las 6 '
                   'transiciones) y las 4 alertas legales: descanso entre '
                   'jornadas (art. 34.3 ET, {} h), descanso semanal '
                   '(art. 37.1), jornada semanal contra las horas '
                   'CONTRATADAS de cada uno (J, verde, {} por defecto) y '
                   'jornada diaria / turno doble (art. 34.3, {} h) — '
                   'DOM-05/DOM-25/TEC-05/COM-01'
                   .format(F01, r0, r1, n, get_column_letter(AUX_HORAS),
                           get_column_letter(AUX_ULT),
                           motor.PARAMETROS['descanso_min'][1],
                           motor.PARAMETROS['jornada_semanal'][1],
                           motor.PARAMETROS['jornada_diaria_max'][1]))
    return r0, r1


# ==========================================================================
# 01 — `Cuadrante Mensual` (DOM-17/TEC-23/COM-12)
# ==========================================================================
def _horas_mes(fila):
    """Horas de la semana en la hoja mensual. El bloque auxiliar del semanal
    no se puede replicar cinco veces (serían 135 columnas), así que los siete
    `VLOOKUP` van inline: es la MISMA tabla `Turnos`, así que las dos hojas no
    pueden discrepar."""
    trozos = []
    for j in range(7):
        trozos.append('IFERROR(VLOOKUP(${d}{f},{t},5,FALSE),0)'
                      .format(d=get_column_letter(2 + j), f=fila,
                              t=TURNOS_TABLA))
    return ('=IF($A{f}="","",ROUND({s},2))'
            .format(f=fila, s='+'.join(trozos)))


def _cuadrante_mensual(wb, cambios, r0_sem):
    """Cinco semanas VIVAS + el total del mes por empleado.

    Se borra y se vuelve a crear entera: hoy son 30 rótulos y CERO fórmulas,
    CERO validación y CERO alertas para 28 días (`01-cuadrante-turnos-semanal
    .xlsx:Cuadrante Mensual:A3..A61`), así que no hay nada que conservar y una
    reconstrucción completa es lo único idempotente de verdad.

    Los nombres NO se teclean: salen del cuadrante semanal (`=IF('Cuadrante
    Semanal'!$A6="","",…)`), que es lo que evita mantener la plantilla en cinco
    sitios. La fila 3 la ocupa la leyenda única que escribe el motor (§1.1) y
    por eso «SEMANA 1» va en `A3`: la fila 4 tiene que ser la de CABECERA,
    que es la que `motor.PRESENTACION` inmoviliza (`A5`) y repite al imprimir
    (`$4:$4`) — y esa cabecera es idéntica en los cinco bloques.
    """
    idx = wb.sheetnames.index('Cuadrante Mensual') \
        if 'Cuadrante Mensual' in wb.sheetnames else len(wb.sheetnames)
    if 'Cuadrante Mensual' in wb.sheetnames:
        wb.remove(wb['Cuadrante Mensual'])
    ws = wb.create_sheet('Cuadrante Mensual', idx)

    ws.column_dimensions['A'].width = 22
    for j in range(7):
        ws.column_dimensions[get_column_letter(2 + j)].width = 12
    ws.column_dimensions['I'].width = 13
    ws.column_dimensions['J'].width = 26

    ws.merge_cells('A1:J1')
    ws['A1'] = 'Cuadrante Mensual — Mes: _______________'
    ws['A1'].font = Font(bold=True, size=13)
    ws.merge_cells('A2:J2')
    ws['A2'] = 'AI Chef Pro · aichef.pro — Kit Gestión de Personal y Turnos'
    ws['A2'].font = Font(size=9, color='666666')

    cabecera = ['Empleado'] + list(DIAS) + ['Total Horas', 'Alerta semanal']
    semanas, n = [], 0
    fila = 3
    for semana in range(1, 6):
        if semana == 1:
            ws['A3'] = 'SEMANA 1'
            ws['A3'].font = Font(bold=True, size=11)
            hdr = 4
        else:
            _titulo_bloque(ws, fila, 'SEMANA {}'.format(semana), 10)
            hdr = fila + 1
        _cab(ws, hdr, cabecera)
        d0 = hdr + 1
        d1 = hdr + CAP
        semanas.append((d0, d1))
        for k in range(CAP):
            f = d0 + k
            sem = r0_sem + k                     # fila gemela del semanal
            _f(ws, 'A{}'.format(f),
               '=IF(\'Cuadrante Semanal\'!$A{s}="","",'
               '\'Cuadrante Semanal\'!$A{s})'.format(s=sem))
            _f(ws, 'I{}'.format(f), _horas_mes(f))
            _f(ws, 'J{}'.format(f),
               '=IF($A{f}="","",IF($I{f}>\'Cuadrante Semanal\'!$J{s},'
               '"⛔ +"&TEXT($I{f}-\'Cuadrante Semanal\'!$J{s},"0")&" h",""))'
               .format(f=f, s=sem))
            n += 3
            for j in range(7):
                cel = ws.cell(row=f, column=2 + j)
                cel.alignment = CENTRO
        motor.marcar_verde(ws, 'B{}:H{}'.format(d0, d1))
        _dv(ws, 'B{}:H{}'.format(d0, d1),
            motor.DV_JORNADA.split(','), 'Código de turno no válido',
            motor.LEYENDA_JORNADA + '.',
            'Usa uno de los 8 códigos del kit: son los mismos que en el '
            '«Cuadrante Semanal» y de ellos salen las horas y las alertas.')
        motor._limpiar_cf(ws, set(['J{}:J{}'.format(d0, d1)]))
        motor.semaforo(ws, 'J{}:J{}'.format(d0, d1), motor.VOC_ALERTA)
        fila = d1 + 2

    # ---- total del mes por empleado + fila de promedio -------------------
    _titulo_bloque(ws, fila, 'TOTAL DEL MES POR EMPLEADO', 10)
    hdr = fila + 1
    _cab(ws, hdr, ['Empleado', 'Semana 1', 'Semana 2', 'Semana 3', 'Semana 4',
                   'Semana 5', 'Total del mes', 'Media semanal',
                   'H. contratadas/semana', 'Alerta del cómputo'])
    t0, t1 = hdr + 1, hdr + CAP
    for k in range(CAP):
        f = t0 + k
        sem = r0_sem + k
        _f(ws, 'A{}'.format(f),
           '=IF(\'Cuadrante Semanal\'!$A{s}="","",'
           '\'Cuadrante Semanal\'!$A{s})'.format(s=sem))
        for w, par in enumerate(semanas):
            _f(ws, '{}{}'.format(get_column_letter(2 + w), f),
               '=IF($A{f}="","",$I{g})'.format(f=f, g=par[0] + k))
        _f(ws, 'G{}'.format(f),
           '=IF($A{f}="","",ROUND(SUM($B{f}:$F{f}),2))'.format(f=f))
        _f(ws, 'H{}'.format(f),
           motor.guarda_media('$B{f}:$F{f}'.format(f=f)))
        _f(ws, 'I{}'.format(f),
           '=IF(\'Cuadrante Semanal\'!$A{s}="","",'
           '\'Cuadrante Semanal\'!$J{s})'.format(s=sem))
        _f(ws, 'J{}'.format(f),
           '=IF(OR($H{f}="",$I{f}=""),"",IF($H{f}>$I{f},'
           '"⛔ media +"&TEXT($H{f}-$I{f},"0")&" h/semana",""))'.format(f=f))
        n += 5 + len(semanas)
    motor._limpiar_cf(ws, set(['J{}:J{}'.format(t0, t1)]))
    motor.semaforo(ws, 'J{}:J{}'.format(t0, t1), motor.VOC_ALERTA)

    prom = t1 + 1
    ws.cell(row=prom, column=1, value='PROMEDIO DEL EQUIPO').font = NEGRITA
    for col in ('B', 'C', 'D', 'E', 'F', 'G', 'H'):
        _f(ws, '{}{}'.format(col, prom),
           motor.guarda_media('${c}${a}:${c}${b}'.format(c=col, a=t0, b=t1)))
        n += 1
    for c in range(1, 11):
        ws.cell(row=prom, column=c).fill = PatternFill('solid',
                                                       fgColor='EEEEEE')
        ws.cell(row=prom, column=c).font = NEGRITA

    pie = prom + 2
    ws.merge_cells('A{0}:J{0}'.format(pie))
    ws.cell(row=pie, column=1, value=motor.PIE).font = Font(size=9,
                                                            color='666666')
    for f in range(4, prom + 1):
        for c in range(9, 11):
            ws.cell(row=f, column=c).number_format = motor.FMT_DEC2

    cambios.append('{}:Cuadrante Mensual: hoja reconstruida — 5 semanas × {} '
                   'empleados con DV de los 8 códigos, horas por VLOOKUP a '
                   '«Turnos», alerta semanal contra las horas contratadas, '
                   'nombres ENLAZADOS al cuadrante semanal, total del mes por '
                   'empleado (G{}:G{}), media semanal y fila de promedio '
                   '({} fórmulas). Antes: 30 rótulos y cero fórmulas para 28 '
                   'días — DOM-17/TEC-23/COM-12'
                   .format(F01, CAP, t0, t1, n))
    return ws


def _instrucciones_01(wb, cambios):
    ley = _lineas_leyenda(F01)
    lineas = [
        'Cómo usar esta plantilla:',
        '▸ Escribe los nombres de tu equipo UNA sola vez, en la columna A de '
        'esta hoja: el \'Cuadrante Mensual\' los arrastra solo y no hay que '
        'teclearlos cinco veces.',
        ley[0] if ley else None,
        '▸ Las horas NO están escritas dentro de la fórmula: salen de la hoja '
        '\'Turnos\'. Si tu mañana empieza a las 8:00, cámbialo allí y se '
        'recalcula el kit entero.',
        ley[1] if len(ley) > 1 else None,
        '▸ La hoja \'Cuadrante Mensual\' repite la rejilla cinco semanas '
        '(los meses de 31 días no caben en cuatro), hereda los nombres del '
        '\'Cuadrante Semanal\', suma el total del mes por empleado y saca la '
        'media semanal, que es lo que se compara con el contrato cuando '
        'distribuyes la jornada de forma irregular.',
        None,
        'Las 4 alertas del cuadrante (columnas K a N):',
        '▸ K · Descanso entre jornadas: compara la hora de FIN de cada día con '
        'la de INICIO del siguiente, contando el turno que cruza la '
        'medianoche. Salta por debajo de las 12 h del art. 34.3 ET; el umbral '
        'es la celda Turnos!B3.',
        '▸ L · Descanso semanal: art. 37.1 ET, día y medio ininterrumpido, '
        'acumulable en periodos de hasta 14 días. Con cero días libres en la '
        'semana la alerta es roja; con uno, ámbar.',
        '▸ M · Jornada semanal: compara con las horas CONTRATADAS de esa '
        'persona (columna J, verde, {jor} por defecto), no con un 40 fijo: a '
        'un contrato de 20 h las alertas le saltan a las 20.',
        '▸ N · Jornada diaria: art. 34.3 ET, máximo {max} h ordinarias al día '
        'salvo distribución irregular pactada (umbral en Turnos!B2). Es la que '
        'caza el turno doble.',
        None,
        'La tabla de turnos vive en la hoja \'Turnos\':',
        '▸ Cada código lleva su hora de inicio, su hora de fin y sus horas '
        'efectivas. Las horas se escriben como número: 7 = 07:00 y 15,5 = '
        '15:30.',
        '▸ El PARTIDO (P) son 9 h efectivas entre las 10:00 y las 23:00; el '
        'DOBLE (D) son 16 h y existe para que la alerta de jornada diaria '
        'tenga algo que cazar.',
        '▸ V (vacaciones) y B (baja) se marcan aquí con las mismas letras que '
        'en el 05 y cuentan 0 h. El permiso es PE y sólo existe en el 05: en '
        'este cuadrante la P es el turno Partido.',
        '▸ Una letra que no esté en la tabla cuenta 0 h: por eso las celdas de '
        'turno llevan desplegable.',
        '▸ Las columnas P a AP están OCULTAS: son el cálculo auxiliar (horas, '
        'hora de inicio, hora de fin y las 6 transiciones entre jornadas). '
        'Muéstralas si quieres '
        'auditar una alerta.',
    ]
    lineas = [x.format(jor=motor.PARAMETROS['jornada_semanal'][1],
                       max=motor.PARAMETROS['jornada_diaria_max'][1])
              if isinstance(x, str) and '{' in x else x for x in lineas]
    _instrucciones(wb['Instrucciones'], lineas)
    cambios.append('{}:Instrucciones: cuerpo reescrito — las 4 alertas '
                   'descritas una a una con su artículo, el descanso pasa a '
                   '12 h (art. 34.3 ET) y aparecen por fin la hoja '
                   '\'Turnos\' y el \'Cuadrante Mensual\', hoy no '
                   'mencionado ni una vez (TEC-23)'.format(F01))


# ==========================================================================
# 02 — registro de horas
# ==========================================================================
CAB_REGISTRO = ['Empleado', 'Fecha', 'Entrada', 'Salida', 'Pausa (h)',
                'Horas trabajadas', 'H. contratadas', 'Horas extra', 'Tipo']

TIPOS_EXTRA = ['Voluntaria', 'Obligatoria', 'Fuerza mayor',
               'Compensada con descanso']


def _pre_02(wb, cambios):
    """La columna «Pausa (h)» se inserta en `pre()`, ANTES de que el motor fije
    rangos (regla del pipeline). Es lo que hace registrable el turno partido,
    que hoy no cabe en un solo par entrada/salida: 10:00→23:00 da 13 h y 5 h
    extra falsas, y partido en dos filas contra 8 h contratadas cada una da
    CERO extras cuando la realidad es 1 h (DOM-21)."""
    ws = wb['Registro Horas']
    if isinstance(ws['E4'].value, str) and 'pausa' in ws['E4'].value.lower():
        return 0                                   # ya insertada (2.ª pasada)
    motor.insertar_columna(ws, 5)
    cambios.append('{}:Registro Horas!E: columna «Pausa (h)» insertada; el '
                   'Tipo de hora extra se desplaza a la I — DOM-21'
                   .format(F02))
    return 1


def _registro_horas(ws, cambios):
    r0, r1_hoy, r1 = 5, 54, 4 + FILAS_REG
    delta = motor.expandir_filas(ws, r1_hoy, r1, cola=_cola(ws, r1_hoy))
    if delta:
        cambios.append('{}:Registro Horas: {} → {} filas de registro '
                       '(§1.3/COM-18)'.format(F02, r1_hoy - r0 + 1, FILAS_REG))
    _cab(ws, 4, CAB_REGISTRO)
    ws.column_dimensions['E'].width = 12
    ws.column_dimensions['I'].width = 22

    for fila in range(r0, r1 + 1):
        _f(ws, 'F{}'.format(fila), motor.horas_mod('C', 'D', fila, 'E'))
        _f(ws, 'H{}'.format(fila),
           motor.guarda_resta('$F{}'.format(fila), '$G{}'.format(fila),
                              'MAX(0,$F{f}-$G{f})'.format(f=fila)))
        cel = ws.cell(row=fila, column=7)          # G · H. contratadas
        cel.value = 8
        cel.number_format = motor.FMT_DEC2

    _limpiar_mis_dv(ws, ('G{}:G{}'.format(r0, r1), 'I{}:I{}'.format(r0, r1)))
    _dv(ws, 'G{}:G{}'.format(r0, r1), None, 'Jornada diaria no válida',
        'Jornada CONTRATADA de ese día, en horas. Viene precargada a 8. Si la '
        'dejas vacía, la columna «Horas extra» se queda en blanco a propósito: '
        'sin saber lo contratado no se puede decir qué es extra.',
        'Escribe un número de horas entre 1 y 12.',
        tipo='decimal', operator='between', formula1='1', formula2='12')
    _dv(ws, 'I{}:I{}'.format(r0, r1), TIPOS_EXTRA,
        'Tipo de hora extra no válido',
        'Art. 35.2 ET: las de FUERZA MAYOR y las COMPENSADAS CON DESCANSO '
        'dentro de los 4 meses siguientes NO computan en el tope de 80 h/año. '
        'El «Resumen Mensual» las descuenta buscando este texto exacto.',
        'Elige un valor de la lista: las fórmulas de agregación buscan este '
        'texto exacto.')
    cambios.append('{}:Registro Horas!F{}:I{}: horas con MOD (cruce de '
                   'medianoche: 23:00→07:00 son 8,00 h, no −16) menos la '
                   'pausa, y la hora extra con GUARDA de «H. contratadas» '
                   'vacía. G precargada a 8 con DV 1-12; el Tipo pasa a las 4 '
                   'modalidades del art. 35.2 — DOM-03/DOM-11/DOM-21/TEC-01/'
                   'TEC-09/COM-07'.format(F02, r0, r1))
    return r0, r1


def _resumen_mensual(ws, cambios, reg0, reg1):
    r0, r1_hoy, r1 = 6, 20, 5 + CAP
    delta = motor.expandir_filas(ws, r1_hoy, r1, cola=_cola(ws, r1_hoy))
    if delta:
        cambios.append('{}:Resumen Mensual: 15 → {} empleados (§1.3)'
                       .format(F02, CAP))

    ws.column_dimensions['C'].width = 20
    ws.column_dimensions['E'].width = 20
    _limpiar_mis_dv(ws)
    _nota_parametro(ws, 3, 'tarifa_hora', 1, 2)
    _nota_parametro(ws, 3, 'recargo_extra', 3, 4)
    _nota_parametro(ws, 3, 'limite_extra_anual', 5, 6, alto=58)

    # ⚠ La columna E era «Coste ×1.75» y traía fórmula en E6:E20. Ahora es la
    # casilla VERDE del acumulado del año: si no se vacía, la hoja conserva un
    # coste calculado con el multiplicador que esta versión retira, `aplicar_
    # verde` la ve «calculada» y no la pinta, y el cliente no puede escribir en
    # ella. Lo mismo la F, que era «Coste ×2.0».
    for f in range(r0, r1 + 1):
        ws.cell(row=f, column=5).value = None
        ws.cell(row=f, column=5).number_format = motor.FMT_DEC2

    _cab(ws, 5, ['Empleado', 'Total H. Extra del mes',
                 'H. extra no computables (art. 35.2)',
                 'H. extra computables', 'H. extra acumuladas en el año',
                 'Límite anual de horas extra',
                 'Coste de las horas extra (€)'])

    reg = "'Registro Horas'"
    emp = '{r}!$A${a}:$A${b}'.format(r=reg, a=reg0, b=reg1)
    ext = '{r}!$H${a}:$H${b}'.format(r=reg, a=reg0, b=reg1)
    tip = '{r}!$I${a}:$I${b}'.format(r=reg, a=reg0, b=reg1)
    n = 0
    for f in range(r0, r1 + 1):
        _f(ws, 'B{}'.format(f),
           '=IF($A{f}="","",ROUND(SUMIF({e},$A{f}&"",{x}),2))'
           .format(f=f, e=emp, x=ext))
        _f(ws, 'C{}'.format(f),
           '=IF($A{f}="","",ROUND(SUMIFS({x},{e},$A{f}&"",{t},"Fuerza mayor")'
           '+SUMIFS({x},{e},$A{f}&"",{t},"Compensada con descanso"),2))'
           .format(f=f, e=emp, x=ext, t=tip))
        _f(ws, 'D{}'.format(f),
           '=IF($A{f}="","",ROUND($B{f}-$C{f},2))'.format(f=f))
        _f(ws, 'F{}'.format(f),
           '=IF($E{f}="","",IF($E{f}>$F$3,'
           '"⛔ EXCEDE ("&TEXT($E{f}-$F$3,"0")&" h)",'
           'IF($E{f}>$F$3*0.8,"⚠ cerca del límite","✓ dentro")))'.format(f=f))
        _f(ws, 'G{}'.format(f),
           '=IF($B{f}="","",ROUND($B{f}*$B$3*$D$3,2))'.format(f=f))
        n += 5

    fila_tot = _fila_con(ws, 1, 'TOTALES', r1 + 1)
    if fila_tot:
        for col in ('B', 'C', 'D', 'G'):
            _f(ws, '{}{}'.format(col, fila_tot),
               '=ROUND(SUM({c}{a}:{c}{b}),2)'.format(c=col, a=r0, b=r1))
            n += 1
        for col in ('E', 'F'):
            ws['{}{}'.format(col, fila_tot)] = None
    cambios.append('{}:Resumen Mensual!B{}:G{}: {} fórmulas — B agrega por '
                   'SUMIF desde «Registro Horas» (hoy es transcripción '
                   'manual), C descuenta fuerza mayor y compensadas con '
                   'descanso (art. 35.2), F vigila el límite anual de B/F3 '
                   'con semáforo y G usa el recargo de D3 como PARÁMETRO. '
                   'Desaparecen las cabeceras «Coste ×1.75» y «Coste ×2.0», '
                   'que presentaban como ley lo que fija el convenio — '
                   'DOM-07/DOM-12/TEC-06/TEC-08/COM-02/COM-14/COM-19'
                   .format(F02, r0, r1, n))


def _instrucciones_02(wb, cambios):
    lineas = [
        'Cómo usar esta plantilla:',
        '▸ Registra entrada, salida y PAUSA. La pausa es lo que hace '
        'registrable el turno partido: 10:00 → 23:00 con 4 h de pausa son 9 h '
        'trabajadas, no 13.',
        '▸ El turno de NOCHE se registra igual: 23:00 → 07:00 son 8 h. La '
        'fórmula contempla el cruce de medianoche.',
        '▸ El \'Resumen Mensual\' agrega por empleado con SUMIF: no hay que '
        'transcribir nada a mano.',
        motor.AVISO_REGISTRO,
        None,
        'Lo que dice el Estatuto de los Trabajadores:',
        '▸ Art. 35.2: máximo 80 horas extra al año por trabajador. NO computan '
        'en ese tope las compensadas con descanso dentro de los 4 meses '
        'siguientes ni las de fuerza mayor: por eso el registro pide el tipo y '
        'el resumen las descuenta.',
        '▸ Art. 35.1: la hora extra no puede valer MENOS que la ordinaria. La '
        'cuantía exacta la fija tu convenio o tu contrato, y puede compensarse '
        'con descanso en vez de pagarse.',
        '▸ Por eso el recargo es una celda verde (D3) y no un número dentro de '
        'la fórmula. El 1,25 que trae de fábrica es un punto de partida, no '
        'una cifra legal: sustitúyelo por el de tu convenio provincial de '
        'hostelería antes de usar la columna de coste.',
        '▸ Las horas extra son voluntarias salvo pacto en convenio o contrato '
        '(art. 35.4 ET).',
        None,
        'Columnas del registro:',
        '▸ Horas trabajadas = salida − entrada − pausa. Escribe las horas en '
        'formato hh:mm (9:00, no 9).',
        '▸ H. Contratadas = jornada CONTRATADA de ese día, precargada a 8. Si '
        'la borras, la hora extra se queda en blanco a propósito: sin saber lo '
        'contratado no hay forma de decir qué sobra.',
        '▸ Tipo: Voluntaria · Obligatoria · Fuerza mayor · Compensada con '
        'descanso. Las dos últimas no suman al tope de 80 h.',
        '▸ En el \'Resumen Mensual\', «H. extra acumuladas en el año» es '
        'verde y la llevas tú de mes en mes: suma el acumulado anterior y las '
        'computables de este mes. Es la que vigila el límite.',
        '▸ Antes de usar la tarifa de B3, sácala de la columna «Coste/hora» '
        'del 03: es el coste real por hora, no el bruto del convenio.',
    ]
    _instrucciones(wb['Instrucciones'], lineas)
    cambios.append('{}:Instrucciones: cuerpo reescrito — ×1,75 y ×2,0 dejan '
                   'de presentarse como «Legislación española» (art. 35.1: '
                   'sólo se exige que no valga menos que la ordinaria) y '
                   'entran las dos excepciones del art. 35.2 — DOM-12/COM-19'
                   .format(F02))


# ==========================================================================
# BONUS-01 — caja y temperaturas (DOM-29) + observaciones (TEC-24)
# ==========================================================================
FILAS_BONUS = 14           # 46..59, justo antes de OBSERVACIONES GENERALES
LIMITES_TEMP = [('Cámara de refrigeración', 4),
                ('Congelador', -18),
                ('Expositor / vitrina', 4)]


def _bonus01(wb, cambios):
    ws = wb['Briefing']
    ws.column_dimensions['A'].width = 20      # 5 era ilegible hasta para
    ws.column_dimensions['B'].width = 34      # «Producto» y «Empleado»
    ws.column_dimensions['C'].width = 20
    ws.column_dimensions['D'].width = 26

    fila_obs = _fila_con(ws, 1, 'OBSERVACIONES GENERALES')
    if fila_obs is None:
        return
    if _fila_con(ws, 1, 'CAJA') is None:
        for _ in range(FILAS_BONUS):
            motor.insertar_fila(ws, fila_obs)
        cambios.append('{}:Briefing!{}:{}: {} filas insertadas para los dos '
                       'bloques que faltaban en un traspaso real — DOM-29'
                       .format(FB1, fila_obs, fila_obs + FILAS_BONUS - 1,
                               FILAS_BONUS))
    c0 = _fila_con(ws, 1, 'CAJA')
    if c0 is None:
        c0 = fila_obs

    # ---- CAJA ------------------------------------------------------------
    _titulo_bloque(ws, c0, '💶 CAJA: FONDO, RECAUDACIÓN Y DIFERENCIA', 4)
    _cab(ws, c0 + 1, ['Caja', 'Fondo inicial (€)', 'Recaudación (€)',
                      'Diferencia (€)'])
    for k, nombre in enumerate(('Sala', 'Barra')):
        f = c0 + 2 + k
        ws.cell(row=f, column=1, value=nombre)
        _f(ws, 'D{}'.format(f),
           '=IF(OR($B{f}="",$C{f}=""),"",ROUND($C{f}-$B{f},2))'.format(f=f))
        for col in ('B', 'C', 'D'):
            ws['{}{}'.format(col, f)].number_format = motor.FMT_EUR
    motor.marcar_verde(ws, 'A{}:C{}'.format(c0 + 2, c0 + 3))
    ftot = c0 + 4
    ws.cell(row=ftot, column=1, value='TOTAL').font = NEGRITA
    for col in ('B', 'C'):
        _f(ws, '{}{}'.format(col, ftot),
           '=IF(COUNT({c}{a}:{c}{b})=0,"",ROUND(SUM({c}{a}:{c}{b}),2))'
           .format(c=col, a=c0 + 2, b=c0 + 3))
    _f(ws, 'D{}'.format(ftot),
       '=IF(OR($B{f}="",$C{f}=""),"",ROUND($C{f}-$B{f},2))'.format(f=ftot))
    for col in ('B', 'C', 'D'):
        cel = ws['{}{}'.format(col, ftot)]
        cel.number_format = motor.FMT_EUR
        cel.font = NEGRITA
    ffirma = c0 + 5
    ws.merge_cells('A{0}:D{0}'.format(ffirma))
    ws.cell(row=ffirma, column=1,
            value='Arqueo hecho por: _____________________     ·     '
                  'Conforme turno entrante: _____________________')

    # ---- TEMPERATURAS ----------------------------------------------------
    t0 = c0 + 7
    _titulo_bloque(ws, t0, '🌡️ TEMPERATURAS AL CAMBIO DE TURNO (APPCC)', 4)
    _cab(ws, t0 + 1, ['Equipo', 'Temperatura (°C)', 'Límite (°C)', 'Conforme'])
    for k, par in enumerate(LIMITES_TEMP):
        f = t0 + 2 + k
        ws.cell(row=f, column=1, value=par[0])
        cel = ws.cell(row=f, column=3, value=par[1])
        cel.number_format = motor.FMT_DEC1
        cel.alignment = CENTRO
        ws.cell(row=f, column=2).number_format = motor.FMT_DEC1
        ws.cell(row=f, column=2).alignment = CENTRO
        _f(ws, 'D{}'.format(f),
           '=IF(OR($B{f}="",$C{f}=""),"",IF($B{f}<=$C{f},"✓ CONFORME",'
           '"⛔ FUERA DE RANGO"))'.format(f=f))
    motor.marcar_verde(ws, 'B{}:C{}'.format(t0 + 2, t0 + 4))
    ref_cf = 'D{}:D{}'.format(t0 + 2, t0 + 4)
    motor._limpiar_cf(ws, set([ref_cf]))
    motor.semaforo(ws, ref_cf, motor.VOC_CONFORME)
    fnota = t0 + 5
    ws.merge_cells('A{0}:D{0}'.format(fnota))
    cel = ws.cell(row=fnota, column=1,
                  value='Quien entrega toma la temperatura DELANTE de quien '
                        'recibe: es el punto en que el APPCC cambia de '
                        'responsable. Fuera de rango, anótalo arriba como '
                        'incidencia y avisa antes de irte.')
    cel.alignment = Alignment(wrap_text=True, vertical='top')
    ws.row_dimensions[fnota].height = 28

    # ---- observaciones: wrap_text y alto (TEC-24) ------------------------
    obs = _fila_con(ws, 1, 'OBSERVACIONES GENERALES')
    for f in range(obs, obs + 4):
        for c in range(1, 5):
            ws.cell(row=f, column=c).alignment = Alignment(wrap_text=True,
                                                            vertical='top')
        if f > obs:
            ws.row_dimensions[f].height = 30
    motor.marcar_verde(ws, 'A{}:D{}'.format(obs + 1, obs + 3))

    _instrucciones(wb['Instrucciones'], [
        'Cómo usar esta plantilla:',
        '▸ El turno saliente completa este briefing ANTES de irse.',
        '▸ El turno entrante lo revisa y firma al llegar.',
        '▸ Imprime una copia diaria o úsalo en la tablet.',
        '▸ Archiva los briefings: son la trazabilidad del traspaso, y las '
        'temperaturas de abajo son además registro de autocontrol APPCC.',
        None,
        'Secciones incluidas:',
        '▸ Reservas pendientes y VIPs del siguiente turno.',
        '▸ Incidencias: averías, falta de stock, quejas. La gravedad va con '
        'desplegable (Alta · Media · Baja): sin escala fija cada encargado '
        'escribe una cosa y el archivo deja de ser comparable.',
        '▸ Tareas pendientes que no se completaron, con prioridad (Urgente · '
        'Alta · Normal).',
        '▸ Stock bajo que necesita pedido urgente.',
        '▸ Personal: ausencias y cambios de último momento.',
        '▸ CAJA: fondo inicial, recaudación y diferencia, con la firma de '
        'quien entrega y de quien recibe. Es lo que convierte el traspaso en '
        'un arqueo.',
        '▸ TEMPERATURAS al cambio de turno (cámara, congelador y expositor): '
        'es el punto exacto en que el APPCC cambia de responsable. El límite '
        'viene precargado y la columna «Conforme» se pinta sola.',
        '▸ Observaciones generales: las tres líneas admiten texto largo (van '
        'con ajuste de línea y alto de fila, para que no se corten al '
        'imprimir).',
    ])
    cambios.append('{}:Briefing!A{}:D{}: bloque de CAJA (fondo · recaudación '
                   '· diferencia · firma) y bloque de TEMPERATURAS (cámara '
                   '≤ 4 °C, congelador ≤ −18 °C, expositor ≤ 4 °C) con '
                   'semáforo CONFORME / FUERA DE RANGO; observaciones con '
                   'wrap_text y alto de fila — DOM-29/TEC-24'
                   .format(FB1, c0, obs + 3))


# ==========================================================================
# Interfaz del pipeline
# ==========================================================================
def pre(wb, fname, cambios):
    if fname == F02:
        _pre_02(wb, cambios)


def post(wb, fname, cambios, registro_grupo):
    if fname == F01:
        _hoja_turnos(wb, cambios)
        r0, _r1 = _cuadrante_semanal(wb['Cuadrante Semanal'], cambios)
        _cuadrante_mensual(wb, cambios, r0)
        _instrucciones_01(wb, cambios)
    elif fname == F02:
        reg0, reg1 = _registro_horas(wb['Registro Horas'], cambios)
        _resumen_mensual(wb['Resumen Mensual'], cambios, reg0, reg1)
        _instrucciones_02(wb, cambios)
    elif fname == FB1:
        _bonus01(wb, cambios)


# ==========================================================================
# Demostraciones con pycel (SPEC §5)
# ==========================================================================
def _pycel_helpers():
    """Reutiliza los helpers de `main.py` cuando el módulo corre dentro del
    orquestador (que es siempre); el respaldo local sólo existe para poder
    importar este módulo suelto."""
    m = sys.modules.get('__main__')
    if m is not None and all(hasattr(m, k) for k in ('_ev', '_set', '_pycel',
                                                     'hora')):
        return m._pycel, m._ev, m._set, m.hora
    import contextlib

    def _pycel(path):
        from pycel import ExcelCompiler
        return ExcelCompiler(filename=path)

    def _ev(xl, ref):
        with open(os.devnull, 'w') as dn, contextlib.redirect_stderr(dn):
            try:
                return xl.evaluate(ref)
            except Exception:                              # noqa: BLE001
                return 'ERR'

    def _set(xl, ref, valor):
        with open(os.devnull, 'w') as dn, contextlib.redirect_stderr(dn):
            try:
                xl.evaluate(ref)
                xl.set_value(ref, valor)
                return True
            except Exception:                              # noqa: BLE001
                return False

    def hora(hh, mm=0):
        return (hh * 60.0 + mm) / 1440.0
    return _pycel, _ev, _set, hora


def demos(carpeta, origen):
    """Cada bloque CAMBIA una entrada y comprueba la DIRECCIÓN del resultado.
    Un valor correcto con la hoja vacía no demuestra nada.

    Cada escenario usa un compilador de pycel **limpio** (`ExcelCompiler`
    cuesta 0,16 s sobre el 01, medido). No es celo: pycel **no propaga la
    invalidación de `set_value` a través de un nodo RANGO**, así que reutilizar
    un compilador para escenarios encadenados devuelve valores de la ronda
    anterior — en la primera ejecución de esta batería, `Resumen Mensual!F6`
    llegó a informar «⛔ EXCEDE (25 h)» con la celda de acumulado VACÍA. Un
    gate que arrastra estado no es un gate.
    """
    _pyc, _ev, _set, _hora = _pycel_helpers()

    def esc(path, sets, lecturas):
        """Compilador limpio → aplica las entradas → lee las salidas."""
        xl = _pyc(path)
        for ref, val in sets:
            _set(xl, ref, val)
        return dict((k, _ev(xl, r)) for k, r in lecturas)

    fuera = {}
    p01 = os.path.join(carpeta, F01)
    p02 = os.path.join(carpeta, F02)
    pb1 = os.path.join(carpeta, FB1)
    cs = "'Cuadrante Semanal'!"

    # ---- 01 · las 4 alertas ---------------------------------------------
    if os.path.isfile(p01):
        def plan(codigos, contratadas=40, nombre='Demo'):
            sets = [(cs + '{}6'.format(get_column_letter(2 + j)), c)
                    for j, c in enumerate(codigos)]
            return sets + [(cs + 'J6', contratadas), (cs + 'A6', nombre)]

        L = ('I', 'K', 'L', 'M', 'N')
        lect = [(c, cs + '{}6'.format(c)) for c in L]
        vacia = esc(p01, [], lect)
        tm = esc(p01, plan(['T', 'M', 'L', 'L', 'L', 'L', 'L']), lect)
        mm = esc(p01, plan(['M', 'M', 'L', 'L', 'L', 'L', 'L']), lect)
        nt = esc(p01, plan(['N', 'T', 'L', 'L', 'L', 'L', 'L']), lect)
        siete = esc(p01, plan(['M'] * 7), lect)
        seis = esc(p01, plan(['M'] * 6 + ['L']), lect)
        cinco = esc(p01, plan(['M'] * 5 + ['L', 'L']), lect)
        parcial = esc(p01, plan(['M'] * 4 + ['L', 'L', 'L'], contratadas=20),
                      lect)
        doble = esc(p01, plan(['D', 'L', 'L', 'L', 'L', 'L', 'L']), lect)
        partido = esc(p01, plan(['P', 'L', 'L', 'L', 'L', 'L', 'L']), lect)

        pruebas = [
            {'alerta': 'K · descanso entre jornadas (art. 34.3 ET, 12 h)',
             'ref': '{}:Cuadrante Semanal:K6'.format(F01),
             'hoja recién descargada': vacia['K'],
             'T→M · 8 h de descanso': tm['K'],
             'M→M · 16 h de descanso': mm['K'],
             'N→T · el turno cruza la medianoche, 8 h': nt['K'],
             'ok': (vacia['K'] in ('', None) and bool(tm['K'])
                    and mm['K'] in ('', None) and bool(nt['K']))},
            {'alerta': 'L · descanso semanal (art. 37.1 ET)',
             'ref': '{}:Cuadrante Semanal:L6'.format(F01),
             'hoja recién descargada': vacia['L'],
             '7 días con turno': siete['L'], '1 día libre': seis['L'],
             '2 días libres': cinco['L'],
             'ok': (vacia['L'] in ('', None) and '0 días' in str(siete['L'])
                    and '1 día' in str(seis['L'])
                    and cinco['L'] in ('', None))},
            {'alerta': 'M · jornada semanal contra lo CONTRATADO (DOM-25)',
             'ref': '{}:Cuadrante Semanal:M6'.format(F01),
             'hoja recién descargada': vacia['M'],
             '40 h planificadas / 40 contratadas': cinco['M'],
             'horas de esa semana (I6)': cinco['I'],
             '32 h planificadas / 20 contratadas': parcial['M'],
             'ok': (vacia['M'] in ('', None) and cinco['M'] in ('', None)
                    and cinco['I'] == 40 and '+12' in str(parcial['M'])
                    and parcial['I'] == 32)},
            {'alerta': 'N · jornada diaria (art. 34.3 ET, 9 h)',
             'ref': '{}:Cuadrante Semanal:N6'.format(F01),
             'hoja recién descargada': vacia['N'],
             'turno DOBLE de 16 h': doble['N'],
             'turno PARTIDO de 9 h': partido['N'],
             'ok': (vacia['N'] in ('', None) and bool(doble['N'])
                    and partido['N'] in ('', None))},
        ]
        fuera['grupo_a_4_alertas_01'] = {
            'ref': '{}:Cuadrante Semanal:K6:N6'.format(F01),
            'pruebas': pruebas, 'ok': all(p['ok'] for p in pruebas),
            'nota': 'las cuatro alertas que la landing vende desde la v1.0 y '
                    'que el fichero no tenía: la única era «>40 h» con el 40 '
                    'escrito dentro de la fórmula (COM-01/DOM-25)'}

        # el umbral es un PARÁMETRO, no un literal (§1.4)
        base = plan(['M', 'M', 'L', 'L', 'L', 'L', 'L'])
        con12 = esc(p01, base, [('K', cs + 'K6')])
        con18 = esc(p01, base + [('Turnos!B3', 18)], [('K', cs + 'K6')])
        fuera['grupo_a_parametro_descanso_01'] = {
            'ref': '{}:Turnos:B3 → Cuadrante Semanal:K6'.format(F01),
            'M→M con el mínimo legal de 12 h': con12['K'],
            'M→M con un convenio que exija 18 h': con18['K'],
            'ok': con12['K'] in ('', None) and bool(con18['K']),
            'nota': 'M→M deja 16 h de descanso: cumple las 12 del art. 34.3 y '
                    'no cumpliría un convenio de 18. El umbral vive en celda, '
                    'no dentro de la fórmula (§1.4)'}

        # la tabla `Turnos` manda sobre las horas (DOM-05)
        uno = plan(['M', 'L', 'L', 'L', 'L', 'L', 'L'])
        h8 = esc(p01, uno, [('I', cs + 'I6'), ('N', cs + 'N6')])
        h6 = esc(p01, uno + [('Turnos!E5', 6)], [('I', cs + 'I6')])
        h11 = esc(p01, uno + [('Turnos!E5', 11)],
                  [('I', cs + 'I6'), ('N', cs + 'N6')])
        fuera['grupo_a_turnos_manda_01'] = {
            'ref': '{}:Turnos:E5 → Cuadrante Semanal:I6/N6'.format(F01),
            'M = 8 h (tabla de fábrica)': h8['I'],
            'alerta de jornada diaria con 8 h': h8['N'],
            'M reconfigurado a 6 h': h6['I'],
            'M reconfigurado a 11 h': h11['I'],
            'alerta de jornada diaria con 11 h': h11['N'],
            'ok': (h8['I'] == 8 and h6['I'] == 6 and h11['I'] == 11
                   and h8['N'] in ('', None) and bool(h11['N'])),
            'nota': 'las horas salen de la tabla, no de los siete IF anidados '
                    'de 700 caracteres de `Cuadrante Semanal!I6` de la v1.1 '
                    '(DOM-05)'}

        # la hoja mensual bebe del semanal y calcula (DOM-17/COM-12)
        men = esc(p01, [(cs + 'A7', 'Marta Ibáñez'), (cs + 'J7', 40),
                        ("'Cuadrante Mensual'!B6", 'M'),
                        ("'Cuadrante Mensual'!C6", 'D'),
                        ("'Cuadrante Mensual'!D6", 'D')],
                  [('nombre', "'Cuadrante Mensual'!A6"),
                   ('horas', "'Cuadrante Mensual'!I6"),
                   ('alerta', "'Cuadrante Mensual'!J6"),
                   ('sem1_del_total', "'Cuadrante Mensual'!B171"),
                   ('total_mes', "'Cuadrante Mensual'!G171")])
        fuera['grupo_a_mensual_vivo_01'] = {
            'ref': '{}:Cuadrante Mensual:A6/I6/J6 y G171'.format(F01),
            'nombre heredado de Cuadrante Semanal!A7': men['nombre'],
            'M + D + D = 8 + 16 + 16': men['horas'],
            'alerta contra las 40 h contratadas': men['alerta'],
            'esa semana en el total del mes': men['sem1_del_total'],
            'total del mes': men['total_mes'],
            'ok': (men['nombre'] == 'Marta Ibáñez' and men['horas'] == 40
                   and men['alerta'] in ('', None)
                   and men['sem1_del_total'] == 40
                   and men['total_mes'] == 40),
            'nota': 'la hoja mensual tenía 30 rótulos, CERO fórmulas, CERO '
                    'validación y 28 días (DOM-17/TEC-23/COM-12)'}

    # ---- 02 · medianoche, pausa, guarda y límite -------------------------
    if os.path.isfile(p02):
        rh = "'Registro Horas'!"
        casos = []
        for etiqueta, ent, sal, pausa, contratadas, esperado in (
                ('turno de noche 23:00 → 07:00', (23, 0), (7, 0), 0, 8, 8.0),
                ('cierre 19:00 → 01:30', (19, 0), (1, 30), 0, 8, 6.5),
                ('partido 10:00 → 23:00 con 4 h de pausa', (10, 0), (23, 0), 4,
                 8, 9.0)):
            r = esc(p02, [(rh + 'C5', _hora(*ent)), (rh + 'D5', _hora(*sal)),
                          (rh + 'E5', pausa), (rh + 'G5', contratadas)],
                    [('horas', rh + 'F5'), ('extra', rh + 'H5')])
            casos.append({'caso': etiqueta, 'esperado_horas': esperado,
                          'horas': r['horas'], 'extra': r['extra'],
                          'ok': isinstance(r['horas'], (int, float))
                          and abs(r['horas'] - esperado) < 0.005})
        jornada = [(rh + 'C5', _hora(9)), (rh + 'D5', _hora(17)),
                   (rh + 'E5', 0)]
        sin_g = esc(p02, jornada + [(rh + 'G5', '')],
                    [('extra', rh + 'H5'), ('horas', rh + 'F5')])
        con_g = esc(p02, jornada + [(rh + 'G5', 6)], [('extra', rh + 'H5')])
        igual = esc(p02, jornada + [(rh + 'G5', 8)], [('extra', rh + 'H5')])
        casos.append({'caso': 'H. contratadas VACÍA con 8 h trabajadas',
                      'horas': sin_g['horas'], 'extra': sin_g['extra'],
                      'ok': sin_g['extra'] in ('', None)
                      and sin_g['horas'] == 8})
        casos.append({'caso': '8 h trabajadas contra 6 contratadas',
                      'extra': con_g['extra'],
                      'ok': isinstance(con_g['extra'], (int, float))
                      and abs(con_g['extra'] - 2) < 0.005})
        casos.append({'caso': '8 h trabajadas contra 8 contratadas',
                      'extra': igual['extra'],
                      'ok': isinstance(igual['extra'], (int, float))
                      and abs(igual['extra']) < 0.005})
        fuera['grupo_a_horas_y_guarda_02'] = {
            'ref': '{}:Registro Horas:F5/H5'.format(F02),
            'pruebas': casos, 'ok': all(c['ok'] for c in casos),
            'nota': 'la v1.1 hacía (D5−C5)*24 y el turno de noche fichaba '
                    '−16 h; y con la columna de contratadas vacía declaraba '
                    'extra la jornada ENTERA — 8 h × 12 € × 1,25 = 120 € por '
                    'día y empleado que el cliente no debe '
                    '(DOM-03/DOM-11/DOM-21/TEC-01/TEC-09/COM-07)'}

        # el resumen AGREGA, descuenta el art. 35.2 y usa el recargo en celda
        registros = [
            (rh + 'A5', 'Ana Prieto'), (rh + 'C5', _hora(9)),
            (rh + 'D5', _hora(17)), (rh + 'E5', 0), (rh + 'G5', 6),
            (rh + 'I5', 'Voluntaria'),
            (rh + 'A6', 'Ana Prieto'), (rh + 'C6', _hora(9)),
            (rh + 'D6', _hora(20)), (rh + 'E6', 0), (rh + 'G6', 8),
            (rh + 'I6', 'Fuerza mayor'),
            (rh + 'A7', 'Luis Cabo'), (rh + 'C7', _hora(9)),
            (rh + 'D7', _hora(19)), (rh + 'E7', 0), (rh + 'G7', 8),
            (rh + 'I7', 'Voluntaria'),
            ("'Resumen Mensual'!A6", 'Ana Prieto'),
            ("'Resumen Mensual'!A7", 'Luis Cabo')]
        lect = [('B', "'Resumen Mensual'!B6"), ('C', "'Resumen Mensual'!C6"),
                ('D', "'Resumen Mensual'!D6"), ('G', "'Resumen Mensual'!G6"),
                ('otro', "'Resumen Mensual'!B7")]
        r125 = esc(p02, registros, lect)
        r150 = esc(p02, registros + [("'Resumen Mensual'!D3", 1.5)], lect)
        r20 = esc(p02, registros + [("'Resumen Mensual'!B3", 20.0)], lect)
        fuera['grupo_a_resumen_agrega_02'] = {
            'ref': '{}:Resumen Mensual:B6/C6/D6/G6'.format(F02),
            'extra de Ana en el mes (2 h + 3 h)': r125['B'],
            'de las que NO computan (fuerza mayor, art. 35.2)': r125['C'],
            'computables en el tope de 80 h': r125['D'],
            'no mezcla empleados: extra de Luis (2 h)': r125['otro'],
            'coste con recargo 1,25 y tarifa 12 €': r125['G'],
            'coste subiendo el recargo a 1,50': r150['G'],
            'coste subiendo la tarifa a 20 €': r20['G'],
            'ok': (r125['B'] == 5 and r125['C'] == 3 and r125['D'] == 2
                   and r125['otro'] == 2
                   and abs(r125['G'] - 75) < 0.01
                   and abs(r150['G'] - 90) < 0.01
                   and abs(r20['G'] - 125) < 0.01),
            'nota': 'la columna B era transcripción MANUAL (COM-14) y el '
                    '×1,75 / ×2,0 estaba escrito dentro de 30 fórmulas '
                    '(TEC-06); ahora los dos son celda verde'}

        # el contador del límite anual, con el tope en celda
        def lim(acum, tope=None):
            sets = [("'Resumen Mensual'!E6", acum)]
            if tope is not None:
                sets.append(("'Resumen Mensual'!F3", tope))
            return esc(p02, sets, [('F', "'Resumen Mensual'!F6")])['F']
        v_vacio, v40, v70, v95, v95_120 = (lim(''), lim(40), lim(70), lim(95),
                                           lim(95, 120))
        fuera['grupo_a_limite_80h_02'] = {
            'ref': '{}:Resumen Mensual:F6 (tope en F3)'.format(F02),
            'recién descargado, sin acumulado': v_vacio,
            'acumuladas 40 h': v40, 'acumuladas 70 h': v70,
            'acumuladas 95 h': v95,
            'acumuladas 95 h con el tope subido a 120': v95_120,
            'ok': (v_vacio in ('', None) and 'dentro' in str(v40)
                   and 'cerca' in str(v70) and 'EXCEDE' in str(v95)
                   and 'dentro' in str(v95_120)),
            'nota': 'art. 35.2 ET: 80 h/año. El tope es celda verde porque se '
                    'prorratea en los contratos parciales y en los de '
                    'duración inferior al año'}

    # ---- BONUS-01 · caja y temperaturas ---------------------------------
    if os.path.isfile(pb1):
        import openpyxl
        wsb = openpyxl.load_workbook(pb1)['Briefing']
        fc = _fila_con(wsb, 1, 'CAJA')
        ft = _fila_con(wsb, 1, 'TEMPERATURAS')
        if fc and ft:
            b, t = fc + 2, ft + 2
            bri = "'Briefing'!"
            caja = esc(pb1, [(bri + 'B{}'.format(b), 200),
                             (bri + 'C{}'.format(b), 1450.5),
                             (bri + 'B{}'.format(b + 1), 150),
                             (bri + 'C{}'.format(b + 1), 620.25)],
                       [('dif', bri + 'D{}'.format(b)),
                        ('total_fondo', bri + 'B{}'.format(fc + 4)),
                        ('total_dif', bri + 'D{}'.format(fc + 4))])
            frio = esc(pb1, [(bri + 'B{}'.format(t), 3),
                             (bri + 'B{}'.format(t + 1), -22),
                             (bri + 'B{}'.format(t + 2), 4)],
                       [('camara', bri + 'D{}'.format(t)),
                        ('congelador', bri + 'D{}'.format(t + 1)),
                        ('expositor', bri + 'D{}'.format(t + 2))])
            malo = esc(pb1, [(bri + 'B{}'.format(t), 8),
                             (bri + 'B{}'.format(t + 1), -12)],
                       [('camara', bri + 'D{}'.format(t)),
                        ('congelador', bri + 'D{}'.format(t + 1))])
            vacio = esc(pb1, [], [('camara', bri + 'D{}'.format(t)),
                                  ('dif', bri + 'D{}'.format(b))])
            fuera['grupo_a_caja_y_temperaturas_bonus01'] = {
                'ref': '{}:Briefing:D{} (caja) y D{} (temperaturas)'
                       .format(FB1, b, t),
                'recién descargado · conforme': vacio['camara'],
                'recién descargado · diferencia': vacio['dif'],
                'diferencia 1450,50 − 200': caja['dif'],
                'fondo total de las dos cajas': caja['total_fondo'],
                'diferencia total': caja['total_dif'],
                'cámara a 3 °C (límite 4)': frio['camara'],
                'congelador a −22 °C (límite −18)': frio['congelador'],
                'expositor a 4 °C (límite 4)': frio['expositor'],
                'cámara a 8 °C': malo['camara'],
                'congelador a −12 °C': malo['congelador'],
                'ok': (vacio['camara'] in ('', None)
                       and vacio['dif'] in ('', None)
                       and abs(caja['dif'] - 1250.5) < 0.01
                       and caja['total_fondo'] == 350
                       and abs(caja['total_dif'] - 1720.75) < 0.01
                       and 'CONFORME' in str(frio['camara'])
                       and 'CONFORME' in str(frio['congelador'])
                       and 'CONFORME' in str(frio['expositor'])
                       and 'FUERA' in str(malo['camara'])
                       and 'FUERA' in str(malo['congelador'])),
                'nota': 'el signo importa: con −18 de límite, «conforme» es '
                        '≤ −18, así que −12 °C tiene que fallar y −22 °C '
                        'pasar. Y el límite en el borde (4 °C contra 4) es '
                        'conforme, no incumplimiento (DOM-29)'}
    return fuera
