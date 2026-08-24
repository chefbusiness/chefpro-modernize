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
import datetime
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


def _instr(ws, texto, patron):
    return motor.linea_instrucciones(ws, texto, re.compile(patron))


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
    """Las 27 fórmulas del bloque auxiliar de una fila (§2)."""
    fuera = []
    for j in range(7):
        dia = get_column_letter(2 + j)
        for base, col_tabla in ((AUX_HORAS, 5), (AUX_INI, 3), (AUX_FIN, 4)):
            coord = '{}{}'.format(get_column_letter(base + j), fila)
            fuera.append((coord,
                          '=IFERROR(VLOOKUP(${d}{f},{t},{c},FALSE),0)'
                          .format(d=dia, f=fila, t=TURNOS_TABLA, c=col_tabla)))
    for j in range(6):
        h1 = get_column_letter(AUX_HORAS + j)
        h2 = get_column_letter(AUX_HORAS + j + 1)
        ini1 = get_column_letter(AUX_INI + j)
        ini2 = get_column_letter(AUX_INI + j + 1)
        fin1 = get_column_letter(AUX_FIN + j)
        coord = '{}{}'.format(get_column_letter(AUX_TRANS + j), fila)
        fuera.append((coord,
                      '=IF(OR(${h1}{f}=0,${h2}{f}=0),"",'
                      'IF(${fin1}{f}<=${ini1}{f},${ini2}{f}-${fin1}{f},'
                      '24-${fin1}{f}+${ini2}{f}))'
                      .format(h1=h1, h2=h2, ini1=ini1, ini2=ini2, fin1=fin1,
                              f=fila)))
    return fuera


def _alertas_semanal(fila):
    """Las CUATRO alertas que la landing vende desde el día uno y que el
    fichero no tenía (COM-01). Cada una cita su artículo."""
    ak = get_column_letter(AUX_TRANS)
    ap = get_column_letter(AUX_TRANS + 5)
    p = get_column_letter(AUX_HORAS)
    v = get_column_letter(AUX_HORAS + 6)
    return [
        ('I{}'.format(fila),
         '=SUM(${p}{f}:${v}{f})'.format(p=p, v=v, f=fila)),
        ('K{}'.format(fila),
         '=IF($A{f}="","",IF(COUNTIF(${ak}{f}:${ap}{f},"<"&{d})>0,'
         '"⛔ <"&{d}&" h",""))'.format(f=fila, ak=ak, ap=ap,
                                      d=TURNOS_DESCANSO)),
        ('L{}'.format(fila),
         '=IF($A{f}="","",IF(7-COUNTIF(${p}{f}:${v}{f},">0")=0,"⛔ 0 días",'
         'IF(7-COUNTIF(${p}{f}:${v}{f},">0")=1,'
         '"⚠ 1 día (el ET pide 1,5, acumulable en 14 días — art. 37.1)","")))'
         .format(f=fila, p=p, v=v)),
        ('M{}'.format(fila),
         '=IF($A{f}="","",IF($I{f}>$J{f},"⛔ +"&TEXT($I{f}-$J{f},"0")&" h",""))'
         .format(f=fila)),
        ('N{}'.format(fila),
         '=IF($A{f}="","",IF(COUNTIF(${p}{f}:${v}{f},">"&{m})>0,'
         '"⛔ jornada > "&{m}&" h",""))'.format(f=fila, p=p, v=v,
                                               m=TURNOS_JORNADA_MAX)),
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
    ws = wb['Instrucciones']
    _instr(ws, '▸ Escribe los nombres de tu equipo UNA sola vez, en la '
               'columna A de esta hoja: el \'Cuadrante Mensual\' los arrastra '
               'solo y no hay que teclearlos cinco veces.',
           r'^▸ Introduce los nombres')
    _instr(ws, '▸ Las horas NO están escritas dentro de la fórmula: salen de '
               'la hoja \'Turnos\'. Si tu mañana empieza a las 8:00, cámbialo '
               'allí y se recalcula el kit entero.',
           r'^▸ Las horas se calculan')
    _instr(ws, '▸ La hoja \'Cuadrante Mensual\' repite la rejilla cinco '
               'semanas (los meses de 31 días no caben en cuatro), suma el '
               'total del mes por empleado y saca la media semanal, que es lo '
               'que se compara con el contrato cuando distribuyes la jornada '
               'de forma irregular.',
           r'^▸ La hoja .Cuadrante Mensual.')
    _instr(ws, 'Las 4 alertas del cuadrante (columnas K a N):',
           r'^Alertas autom')
    _instr(ws, '▸ K · Descanso entre jornadas: compara la hora de FIN de cada '
               'día con la de INICIO del siguiente, contando el turno que '
               'cruza la medianoche. Salta por debajo de las 12 h del art. '
               '34.3 ET (el umbral está en Turnos!B3).',
           r'^▸ La columna .Alertas.')
    _instr(ws, '▸ L · Descanso semanal: art. 37.1 ET, día y medio '
               'ininterrumpido, acumulable en periodos de hasta 14 días. Con '
               'cero días libres en la semana la alerta es roja.',
           r'^▸ Recuerda: m.nimo')
    _instr(ws, '▸ M · Jornada semanal: compara con las horas CONTRATADAS de '
               'esa persona (columna J, verde, 40 por defecto), no con un 40 '
               'fijo: a un contrato de 20 h se le disparan las alertas a las '
               '20, no a las 40.',
           r'^▸ M · Jornada semanal')
    _instr(ws, '▸ N · Jornada diaria: art. 34.3 ET, máximo 9 h ordinarias al '
               'día salvo distribución irregular pactada (umbral en '
               'Turnos!B2). Es la que caza el turno doble.',
           r'^▸ M.ximo 9h de jornada')
    _instr(ws, 'La tabla de turnos vive en la hoja \'Turnos\':',
           r'^Turnos est')
    _instr(ws, '▸ Cada código lleva su hora de inicio, su hora de fin y sus '
               'horas efectivas. Las horas se escriben como número: 7 = 07:00 '
               'y 15,5 = 15:30.',
           r'^▸ M = Ma.ana')
    _instr(ws, '▸ El PARTIDO (P) son 9 h efectivas entre las 10:00 y las '
               '23:00; el DOBLE (D) son 16 h y existe para que la alerta de '
               'jornada diaria tenga algo que cazar.',
           r'^▸ T = Tarde')
    _instr(ws, '▸ Las columnas P a AP están OCULTAS: son el cálculo auxiliar '
               '(horas, hora de inicio, hora de fin y las 6 transiciones '
               'entre jornadas). Muéstralas si quieres auditar una alerta.',
           r'^▸ N = Noche')
    _instr(ws, '▸ V (vacaciones) y B (baja) se marcan aquí igual que en el '
               '05, con las mismas letras, y cuentan 0 h.',
           r'^▸ P = Partido')
    _instr(ws, '▸ Una letra que no esté en la tabla cuenta 0 h: por eso las '
               'celdas de turno llevan desplegable.',
           r'^▸ L = Libre')
    cambios.append('{}:Instrucciones: 14 líneas reescritas — las 4 alertas '
                   'descritas una a una con su artículo, el descanso pasa a '
                   '12 h (art. 34.3 ET; las de la Directiva 2003/88/CE son '
                   'otra cosa) y aparecen por fin la hoja \'Turnos\' y el '
                   '\'Cuadrante Mensual\', hoy no mencionado ni una vez '
                   '(TEC-23)'.format(F01))


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
           '=IF($A{f}="","",ROUND(SUMIF({e},$A{f},{x}),2))'
           .format(f=f, e=emp, x=ext))
        _f(ws, 'C{}'.format(f),
           '=IF($A{f}="","",ROUND(SUMIFS({x},{e},$A{f},{t},"Fuerza mayor")'
           '+SUMIFS({x},{e},$A{f},{t},"Compensada con descanso"),2))'
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
    ws = wb['Instrucciones']
    _instr(ws, '▸ Registra entrada, salida y PAUSA. La pausa es lo que hace '
               'registrable el turno partido: 10:00 → 23:00 con 4 h de pausa '
               'son 9 h trabajadas, no 13.',
           r'^▸ Registra cada d.a')
    _instr(ws, '▸ El turno de NOCHE se registra igual: 23:00 → 07:00 son 8 h. '
               'La fórmula contempla el cruce de medianoche.',
           r'^▸ Las horas trabajadas y las horas extra')
    _instr(ws, motor.AVISO_REGISTRO, r'^▸ Esta hoja trae ')
    _instr(ws, 'Lo que dice el Estatuto de los Trabajadores:',
           r'^Legislaci.n espa.ola')
    _instr(ws, '▸ Art. 35.2: máximo 80 horas extra al año por trabajador. NO '
               'computan en ese tope las compensadas con descanso dentro de '
               'los 4 meses siguientes ni las de fuerza mayor: por eso el '
               'registro pide el tipo y el resumen las descuenta.',
           r'^▸ M.ximo 80 horas extra')
    _instr(ws, '▸ Art. 35.1: la hora extra no puede valer MENOS que la '
               'ordinaria. La cuantía exacta la fija tu convenio o tu '
               'contrato, y puede compensarse con descanso en vez de pagarse. '
               'Por eso el recargo es una celda verde (D3), no un número '
               'dentro de la fórmula.',
           r'^▸ Las primeras 80h')
    _instr(ws, '▸ El 1,25 que trae D3 es un valor de partida, no una cifra '
               'legal: sustitúyelo por el de tu convenio provincial de '
               'hostelería antes de usar la columna de coste.',
           r'^▸ Horas por encima de 80')
    _instr(ws, '▸ Horas trabajadas = salida − entrada − pausa. Escribe las '
               'horas en formato hh:mm (9:00, no 9).',
           r'^▸ Horas Contratadas =')
    _instr(ws, '▸ H. Contratadas = jornada CONTRATADA de ese día, precargada '
               'a 8. Si la borras, la hora extra se queda en blanco: sin '
               'saber lo contratado no hay forma de decir qué sobra.',
           r'^▸ Horas Extra = max')
    _instr(ws, '▸ Tipo: Voluntaria · Obligatoria · Fuerza mayor · Compensada '
               'con descanso. Las dos últimas no suman al tope de 80 h.',
           r'^▸ Tipo: Voluntaria')
    _instr(ws, '▸ La columna «H. extra acumuladas en el año» del resumen es '
               'verde y la llevas tú de mes en mes: suma el acumulado '
               'anterior y las computables de este mes (columna D). Es la que '
               'vigila el límite.',
           r'^▸ La columna .H. extra acumuladas')
    cambios.append('{}:Instrucciones: bloque legal reescrito — ×1,75 y ×2,0 '
                   'dejan de presentarse como «Legislación española» (art. '
                   '35.1: sólo se exige que no valga menos que la ordinaria) '
                   'y entran las dos excepciones del art. 35.2 — '
                   'DOM-12/COM-19'.format(F02))


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

    ws2 = wb['Instrucciones']
    _instr(ws2, '▸ Caja: fondo inicial, recaudación y diferencia, con la '
                'firma de quien entrega y de quien recibe.',
           r'^▸ Caja: fondo inicial')
    _instr(ws2, '▸ Temperaturas de cámara, congelador y expositor al cambio '
                'de turno: es el punto donde el APPCC cambia de responsable.',
           r'^▸ Temperaturas de c.mara')
    _instr(ws2, '▸ Gravedad de la incidencia y prioridad de la tarea van con '
                'desplegable: sin escala fija, cada encargado escribe una '
                'cosa y el archivo no es comparable de un día para otro.',
           r'^▸ Gravedad de la incidencia')
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
    Un valor correcto con la hoja vacía no demuestra nada: lo que se mide es
    que la fórmula reacciona, y en el sentido que dice la SPEC."""
    _pyc, _ev, _set, _hora = _pycel_helpers()
    fuera = {}
    p01 = os.path.join(carpeta, F01)
    p02 = os.path.join(carpeta, F02)
    pb1 = os.path.join(carpeta, FB1)

    # ---- 01 · las 4 alertas ---------------------------------------------
    if os.path.isfile(p01):
        xl = _pyc(p01)
        cs = "'Cuadrante Semanal'"
        pruebas = []

        def _plan(codigos, contratadas=40):
            for j, cod in enumerate(codigos):
                _set(xl, '{}!{}6'.format(cs, get_column_letter(2 + j)), cod)
            _set(xl, '{}!J6'.format(cs), contratadas)
            _set(xl, '{}!A6'.format(cs), 'Demo')

        # K · descanso entre jornadas (art. 34.3 ET, 12 h)
        _plan(['T', 'M', 'L', 'L', 'L', 'L', 'L'])
        k_mal = _ev(xl, '{}!K6'.format(cs))
        _plan(['M', 'M', 'L', 'L', 'L', 'L', 'L'])
        k_bien = _ev(xl, '{}!K6'.format(cs))
        _plan(['N', 'T', 'L', 'L', 'L', 'L', 'L'])
        k_noche = _ev(xl, '{}!K6'.format(cs))
        pruebas.append({
            'alerta': 'K · descanso entre jornadas',
            'ref': '{}:Cuadrante Semanal:K6'.format(F01),
            'T→M (8 h de descanso)': k_mal,
            'M→M (16 h de descanso)': k_bien,
            'N→T (cruza medianoche: 8 h)': k_noche,
            'ok': bool(k_mal) and not k_bien and bool(k_noche)})

        # L · descanso semanal (art. 37.1)
        _plan(['M'] * 7)
        l_cero = _ev(xl, '{}!L6'.format(cs))
        _plan(['M'] * 6 + ['L'])
        l_uno = _ev(xl, '{}!L6'.format(cs))
        _plan(['M'] * 5 + ['L', 'L'])
        l_dos = _ev(xl, '{}!L6'.format(cs))
        pruebas.append({
            'alerta': 'L · descanso semanal',
            'ref': '{}:Cuadrante Semanal:L6'.format(F01),
            '7 días trabajados': l_cero, '1 día libre': l_uno,
            '2 días libres': l_dos,
            'ok': '0 días' in str(l_cero) and '1 día' in str(l_uno)
            and not l_dos})

        # M · jornada semanal contra las horas CONTRATADAS (DOM-25)
        _plan(['M'] * 5 + ['L', 'L'], contratadas=40)
        m_completa = _ev(xl, '{}!M6'.format(cs))
        i_completa = _ev(xl, '{}!I6'.format(cs))
        _plan(['M'] * 4 + ['L', 'L', 'L'], contratadas=20)
        m_parcial = _ev(xl, '{}!M6'.format(cs))
        pruebas.append({
            'alerta': 'M · jornada semanal',
            'ref': '{}:Cuadrante Semanal:M6'.format(F01),
            '40 h planificadas / 40 contratadas': m_completa,
            'horas de esa semana': i_completa,
            '32 h planificadas / 20 contratadas (parcial)': m_parcial,
            'ok': not m_completa and '+12' in str(m_parcial)
            and i_completa == 40})

        # N · jornada diaria / turno doble
        _plan(['D', 'L', 'L', 'L', 'L', 'L', 'L'])
        n_doble = _ev(xl, '{}!N6'.format(cs))
        _plan(['P', 'L', 'L', 'L', 'L', 'L', 'L'])
        n_partido = _ev(xl, '{}!N6'.format(cs))
        pruebas.append({
            'alerta': 'N · jornada diaria (art. 34.3 ET)',
            'ref': '{}:Cuadrante Semanal:N6'.format(F01),
            'turno DOBLE de 16 h': n_doble,
            'turno PARTIDO de 9 h': n_partido,
            'ok': bool(n_doble) and not n_partido})
        fuera['grupo_a_4_alertas_01'] = {
            'ref': '{}:Cuadrante Semanal:K6:N6'.format(F01),
            'pruebas': pruebas, 'ok': all(p['ok'] for p in pruebas),
            'nota': 'las cuatro alertas que la landing vende desde la v1.0 y '
                    'que el fichero no tenía: sólo existía «>40 h» (COM-01)'}

        # el parámetro MANDA: subir Turnos!B3 a 14 h hace saltar M→M
        _plan(['M', 'M', 'L', 'L', 'L', 'L', 'L'])
        antes = _ev(xl, '{}!K6'.format(cs))
        _set(xl, 'Turnos!B3', 14)
        despues = _ev(xl, '{}!K6'.format(cs))
        _set(xl, 'Turnos!B3', 12)
        fuera['grupo_a_parametro_descanso_01'] = {
            'ref': '{}:Turnos:B3 → Cuadrante Semanal:K6'.format(F01),
            'con 12 h (art. 34.3 ET)': antes, 'con 14 h': despues,
            'ok': (not antes) and bool(despues),
            'nota': 'el umbral está en celda, no dentro de la fórmula (§1.4): '
                    'M→M deja 16 h de descanso, así que sólo salta cuando el '
                    'convenio exige más de 16'}

        # la tabla Turnos manda sobre las horas
        _plan(['M', 'L', 'L', 'L', 'L', 'L', 'L'])
        h8 = _ev(xl, '{}!I6'.format(cs))
        _set(xl, 'Turnos!E5', 6)
        h6 = _ev(xl, '{}!I6'.format(cs))
        _set(xl, 'Turnos!E5', 8)
        fuera['grupo_a_turnos_manda_01'] = {
            'ref': '{}:Turnos:E5 → Cuadrante Semanal:I6'.format(F01),
            'M = 8 h': h8, 'M reconfigurado a 6 h': h6,
            'ok': h8 == 8 and h6 == 6,
            'nota': 'las horas salen de la tabla, no de los siete IF anidados '
                    'de 700 caracteres de la v1.1 (DOM-05)'}

        # la hoja mensual bebe del semanal
        _set(xl, "'Cuadrante Semanal'!A7", 'Marta Ibáñez')
        nombre = _ev(xl, "'Cuadrante Mensual'!A6")
        _set(xl, "'Cuadrante Mensual'!B6", 'M')
        _set(xl, "'Cuadrante Mensual'!C6", 'D')
        horas_mes = _ev(xl, "'Cuadrante Mensual'!I6")
        fuera['grupo_a_mensual_vivo_01'] = {
            'ref': '{}:Cuadrante Mensual:A6/I6'.format(F01),
            'nombre heredado de Cuadrante Semanal!A7': nombre,
            'M + D = 24 h': horas_mes,
            'ok': nombre == 'Marta Ibáñez' and horas_mes == 24,
            'nota': 'la hoja mensual tenía CERO fórmulas y CERO validación '
                    '(DOM-17/COM-12); ahora hereda los nombres y calcula'}

    # ---- 02 · medianoche, pausa, guarda y límite -------------------------
    if os.path.isfile(p02):
        xl = _pyc(p02)
        rh = "'Registro Horas'"
        casos = []
        for etiqueta, ent, sal, pausa, contratadas, esperado_h in (
                ('turno de noche 23:00 → 07:00', 23, 7, 0, 8, 8.0),
                ('cierre 19:00 → 01:30', 19, 1.5, 0, 8, 6.5),
                ('partido 10:00 → 23:00 con 4 h de pausa', 10, 23, 4, 8, 9.0)):
            _set(xl, '{}!C5'.format(rh), _hora(int(ent), int(round((ent % 1)
                                                                   * 60))))
            _set(xl, '{}!D5'.format(rh), _hora(int(sal), int(round((sal % 1)
                                                                   * 60))))
            _set(xl, '{}!E5'.format(rh), pausa)
            _set(xl, '{}!G5'.format(rh), contratadas)
            h = _ev(xl, '{}!F5'.format(rh))
            x = _ev(xl, '{}!H5'.format(rh))
            casos.append({'caso': etiqueta, 'esperado_horas': esperado_h,
                          'horas': h, 'extra': x,
                          'ok': isinstance(h, (int, float))
                          and abs(h - esperado_h) < 0.005})
        # guarda: sin «H. contratadas» la extra se calla
        _set(xl, '{}!C5'.format(rh), _hora(9))
        _set(xl, '{}!D5'.format(rh), _hora(17))
        _set(xl, '{}!E5'.format(rh), 0)
        _set(xl, '{}!G5'.format(rh), None)
        x_vacia = _ev(xl, '{}!H5'.format(rh))
        _set(xl, '{}!G5'.format(rh), 6)
        x_seis = _ev(xl, '{}!H5'.format(rh))
        casos.append({'caso': 'H. contratadas VACÍA (8 h trabajadas)',
                      'extra': x_vacia, 'ok': x_vacia in ('', None)})
        casos.append({'caso': '8 h trabajadas contra 6 contratadas',
                      'extra': x_seis, 'ok': isinstance(x_seis, (int, float))
                      and abs(x_seis - 2) < 0.005})
        fuera['grupo_a_horas_y_guarda_02'] = {
            'ref': '{}:Registro Horas:F5/H5'.format(F02),
            'pruebas': casos, 'ok': all(c['ok'] for c in casos),
            'nota': 'la v1.1 hacía (D5−C5)*24 y el turno de noche fichaba '
                    '−16 h; y con la columna de contratadas vacía declaraba '
                    'extra la jornada ENTERA (DOM-03/DOM-11/DOM-21)'}

        # Resumen: agrega, descuenta el art. 35.2 y usa el recargo en celda
        _set(xl, '{}!A5'.format(rh), 'Ana Prieto')
        _set(xl, '{}!G5'.format(rh), 6)
        _set(xl, '{}!I5'.format(rh), 'Voluntaria')
        _set(xl, '{}!A6'.format(rh), 'Ana Prieto')
        _set(xl, '{}!C6'.format(rh), _hora(9))
        _set(xl, '{}!D6'.format(rh), _hora(20))
        _set(xl, '{}!E6'.format(rh), 0)
        _set(xl, '{}!G6'.format(rh), 8)
        _set(xl, '{}!I6'.format(rh), 'Fuerza mayor')
        _set(xl, "'Resumen Mensual'!A6", 'Ana Prieto')
        total = _ev(xl, "'Resumen Mensual'!B6")
        nocomp = _ev(xl, "'Resumen Mensual'!C6")
        comp = _ev(xl, "'Resumen Mensual'!D6")
        coste125 = _ev(xl, "'Resumen Mensual'!G6")
        _set(xl, "'Resumen Mensual'!D3", 1.5)
        coste150 = _ev(xl, "'Resumen Mensual'!G6")
        _set(xl, "'Resumen Mensual'!D3", 1.25)
        fuera['grupo_a_resumen_agrega_02'] = {
            'ref': '{}:Resumen Mensual:B6/C6/D6/G6'.format(F02),
            'extra del mes (2+3 h)': total,
            'no computables (fuerza mayor, art. 35.2)': nocomp,
            'computables': comp,
            'coste con recargo 1,25': coste125,
            'coste con recargo 1,50': coste150,
            'ok': (isinstance(total, (int, float)) and abs(total - 5) < 0.005
                   and isinstance(nocomp, (int, float))
                   and abs(nocomp - 3) < 0.005
                   and isinstance(comp, (int, float)) and abs(comp - 2) < 0.005
                   and isinstance(coste125, (int, float))
                   and abs(coste125 - 75) < 0.01
                   and isinstance(coste150, (int, float))
                   and abs(coste150 - 90) < 0.01),
            'nota': 'B era transcripción MANUAL (COM-14) y el ×1,75/×2,0 '
                    'estaba escrito dentro de 30 fórmulas (TEC-06)'}

        # límite anual con el tope en celda
        _set(xl, "'Resumen Mensual'!E6", 40)
        v40 = _ev(xl, "'Resumen Mensual'!F6")
        _set(xl, "'Resumen Mensual'!E6", 70)
        v70 = _ev(xl, "'Resumen Mensual'!F6")
        _set(xl, "'Resumen Mensual'!E6", 95)
        v95 = _ev(xl, "'Resumen Mensual'!F6")
        _set(xl, "'Resumen Mensual'!F3", 120)
        v95_120 = _ev(xl, "'Resumen Mensual'!F6")
        _set(xl, "'Resumen Mensual'!F3", 80)
        _set(xl, "'Resumen Mensual'!E6", None)
        vacio = _ev(xl, "'Resumen Mensual'!F6")
        fuera['grupo_a_limite_80h_02'] = {
            'ref': '{}:Resumen Mensual:F6 (tope en F3)'.format(F02),
            'acumuladas 40 h': v40, 'acumuladas 70 h': v70,
            'acumuladas 95 h': v95,
            'acumuladas 95 h con el tope subido a 120': v95_120,
            'sin acumulado (recién descargado)': vacio,
            'ok': ('dentro' in str(v40) and 'cerca' in str(v70)
                   and 'EXCEDE' in str(v95) and 'dentro' in str(v95_120)
                   and vacio in ('', None)),
            'nota': 'art. 35.2 ET: 80 h/año. El tope es celda verde porque '
                    'el cómputo se prorratea en los contratos parciales y de '
                    'duración inferior al año'}

    # ---- BONUS-01 · caja y temperaturas ---------------------------------
    if os.path.isfile(pb1):
        import openpyxl
        wsb = openpyxl.load_workbook(pb1)['Briefing']
        fila_caja = _fila_con(wsb, 1, 'CAJA')
        fila_temp = _fila_con(wsb, 1, 'TEMPERATURAS')
        if fila_caja and fila_temp:
            xl = _pyc(pb1)
            b = fila_caja + 2
            _set(xl, "'Briefing'!B{}".format(b), 200)
            _set(xl, "'Briefing'!C{}".format(b), 1450.5)
            dif = _ev(xl, "'Briefing'!D{}".format(b))
            t = fila_temp + 2
            _set(xl, "'Briefing'!B{}".format(t), 3)
            ok_frio = _ev(xl, "'Briefing'!D{}".format(t))
            _set(xl, "'Briefing'!B{}".format(t), 8)
            mal_frio = _ev(xl, "'Briefing'!D{}".format(t))
            _set(xl, "'Briefing'!B{}".format(t + 1), -22)
            ok_cong = _ev(xl, "'Briefing'!D{}".format(t + 1))
            _set(xl, "'Briefing'!B{}".format(t + 1), -12)
            mal_cong = _ev(xl, "'Briefing'!D{}".format(t + 1))
            fuera['grupo_a_caja_y_temperaturas_bonus01'] = {
                'ref': '{}:Briefing:D{} y D{}'.format(FB1, b, t),
                'diferencia 1450,50 − 200': dif,
                'cámara a 3 °C (límite 4)': ok_frio,
                'cámara a 8 °C': mal_frio,
                'congelador a −22 °C (límite −18)': ok_cong,
                'congelador a −12 °C': mal_cong,
                'ok': (isinstance(dif, (int, float))
                       and abs(dif - 1250.5) < 0.01
                       and 'CONFORME' in str(ok_frio)
                       and 'FUERA' in str(mal_frio)
                       and 'CONFORME' in str(ok_cong)
                       and 'FUERA' in str(mal_cong)),
                'nota': 'el signo importa: con −18 de límite, «conforme» es '
                        '≤ −18, así que −12 tiene que fallar y −22 pasar '
                        '(DOM-29)'}
    return fuera
