#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
grupo_b.py — Kit de Gestión de Personal y Turnos v2.0

Reparto del orquestador (2026-08-24): este grupo construye TRES ficheros —

  · `03-coste-laboral-mensual.xlsx`   (SPEC §3)
  · `04-onboarding-nuevo-empleado.xlsx` (SPEC §4, bloque «04»)
  · `05-planificacion-vacaciones.xlsx`  (SPEC §4, bloque «05»)

`BONUS-02-calculadora-plantilla-optima.xlsx`, que la SPEC empareja con el 03
dentro del §3, NO está en este reparto: lo construye otro grupo. Aquí se deja
el 03 dando **7 FTE** con los datos por defecto y el modelo entero escrito en
celdas visibles (§3), que es lo que `main.demo_fte` compara contra el bonus.

Contrato con `main.py`: se exponen `FICHEROS`, `pre(wb, fname, cambios)` y
`demos(carpeta, origen)`. Todo el trabajo va en `pre()` —antes de
`motor.aplicar` y, por tanto, mucho antes de `motor.cerrar`— por dos razones
medidas:

  1. `motor.colores_seccion_04` corre dentro de `motor.aplicar`, es decir ENTRE
     `pre` y `post`, y detecta los cinco tramos del 04 con `secciones_04()`. Si
     las tres tareas nuevas (DOM-15) se insertaran en `post`, el motor habría
     pintado los tramos VIEJOS y las filas nuevas se quedarían sin color.
  2. `motor.cerrar` fija formatos, verde, DV, formato condicional, área de
     impresión y protección sobre el layout FINAL. Cuanto antes esté ese layout,
     menos casos especiales.

Idempotencia (2.ª pasada = 0 diferencias): las hojas que cambian de GEOMETRÍA
—el calendario del 05 pasa de 12 columnas a 55— se **reconstruyen enteras**
(`wb.remove` + `create_sheet` en el mismo índice) en vez de parchearse; las que
sólo cambian de contenido se sobrescriben celda a celda. Las DV propias se
borran antes de reescribirse (una `DataValidation` añadida dos veces son dos
entradas distintas en el `digest` de `main.py`), y lo mismo con el formato
condicional propio.
"""

import copy
import datetime

from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

import motor

FICHEROS = [
    '03-coste-laboral-mensual.xlsx',
    '04-onboarding-nuevo-empleado.xlsx',
    '05-planificacion-vacaciones.xlsx',
]

#: Marca de las DV que escribe ESTE grupo. Empieza por `motor.MARCA_DV` a
#: propósito: así `motor._limpiar_dv(ws)` —que reconoce las suyas por ese
#: prefijo— también se lleva las mías cuando limpia una hoja, y no quedan dos
#: validaciones sobre la misma celda (Excel aplica la primera que encuentra).
MARCA_B = motor.MARCA_DV + 'b'

# ==========================================================================
# Utilidades locales
# ==========================================================================


def _merges(ws, deseadas):
    """Fija EXACTAMENTE las combinaciones de la hoja. Idempotente por
    construcción: deshace todas y rehace la lista pedida."""
    for m in [str(r) for r in ws.merged_cells.ranges]:
        ws.unmerge_cells(m)
    for m in deseadas:
        ws.merge_cells(m)


def _anchos(ws, mapa):
    for letra, ancho in mapa.items():
        ws.column_dimensions[letra].width = ancho


def _rotulo(ws, fila, texto, col=1, negrita=False):
    cel = ws.cell(row=fila, column=col, value=texto)
    if negrita:
        cel.font = Font(bold=True)
    return cel


def _formula(ws, coord, formula, fmt=None):
    """Escribe una fórmula y la REGISTRA para que `main.py` compruebe que
    quedó con valor cacheado (`verificar_cache`)."""
    cel = ws[coord]
    cel.value = formula
    if fmt:
        cel.number_format = fmt
    motor._reg(ws, coord, formula)
    return cel


def _verde(ws, coord, valor=None, fmt=None):
    cel = ws[coord]
    if valor is not None:
        cel.value = valor
    if fmt:
        cel.number_format = fmt
    motor.marcar_verde(ws, coord)
    return cel


def _dv(ws, rango, valores, titulo, prompt, error, marca=MARCA_B):
    """DV de lista inline, marcada para poder retirarla en la 2.ª pasada."""
    dv = DataValidation(
        type='list', formula1='"{}"'.format(','.join(valores)),
        allow_blank=True, showErrorMessage=True, errorTitle=titulo,
        error=error, errorStyle='stop', showInputMessage=True,
        promptTitle='{} · {}'.format(marca, titulo), prompt=prompt)
    ws.add_data_validation(dv)
    dv.add(rango)
    return dv


def _cf(ws, rango, vocabulario):
    """Semáforo propio, limpiando antes el rango: `motor.aplicar_cf` sólo
    limpia los rangos que gobierna ÉL, así que una regla del grupo escrita dos
    veces se duplicaría en cada pasada."""
    motor._limpiar_cf(ws, {rango})
    return motor.semaforo(ws, rango, vocabulario)


def _instrucciones(ws, lineas, zona=32):
    """Reescribe el cuerpo de `Instrucciones` (columna B en este kit).

    Se limpia una ZONA fija y se escribe desde la fila 2, dejando SIEMPRE
    contenido en la última fila escrita: el bloque de bio + versión que añade
    `motor.bio_y_version` se ancla en sí mismo, así que mientras mi zona no lo
    pise, la 2.ª pasada lo reescribe en su sitio y no se desplaza.
    """
    col = motor.col_instrucciones(ws)
    for r in range(2, zona + 1):
        ws.cell(row=r, column=col).value = None
    fila = 2
    for texto in lineas:
        if texto is None:
            fila += 1
            continue
        cel = ws.cell(row=fila, column=col, value=texto)
        cel.alignment = Alignment(wrap_text=True, vertical='top')
        if fila == 2:
            cel.font = Font(bold=True, size=13)
        fila += 1
    return fila - 1


def _cabecera(ws, fila, textos, col0=1):
    """Cabecera oscura, del mismo estilo que ya usa la v1.1."""
    for i, txt in enumerate(textos):
        cel = ws.cell(row=fila, column=col0 + i, value=txt)
        cel.fill = PatternFill('solid', fgColor=motor.CAB)
        cel.font = Font(bold=True, color='FFFFFF', size=10)
        cel.alignment = Alignment(horizontal='center', vertical='center',
                                  wrap_text=True)


def _seccion(ws, fila, texto, ancho, color='ECEFF1'):
    cel = ws.cell(row=fila, column=1, value=texto)
    cel.font = Font(bold=True, size=11)
    cel.fill = PatternFill('solid', fgColor=color)
    for c in range(2, ancho + 1):
        ws.cell(row=fila, column=c).fill = PatternFill('solid', fgColor=color)


def _pie(ws, fila, ancho):
    cel = ws.cell(row=fila, column=1, value=motor.PIE)
    cel.font = Font(size=8, color='888888')
    cel.alignment = Alignment(horizontal='center')
    return '{}{}:{}{}'.format('A', fila, get_column_letter(ancho), fila)


# ==========================================================================
# 03 · COSTE LABORAL MENSUAL  (SPEC §3)
# ==========================================================================
#: Los 6 tipos de negocio de la tabla de referencia del propio fichero
#: (`03-coste-laboral-mensual.xlsx:Ratio Coste Laboral:A14:A19`), con sus dos
#: columnas NUMÉRICAS nuevas (objetivo / máximo aceptable). No son cifras
#: inventadas: son el extremo superior de los rangos que la hoja ya imprime en
#: texto desde la v1.1 —«25-28 %» → 0,28 objetivo; «22-30 %» → 0,30 aceptable—,
#: así que el semáforo y la tabla dejan de contradecirse (COM-11).
TIPOS_NEGOCIO = [
    ('Fast Casual / Comida Rápida', '25-28%', '22-30%', 0.28, 0.30),
    ('Restaurante Casual',          '28-33%', '25-35%', 0.33, 0.35),
    ('Fine Dining / Alta Cocina',   '35-40%', '33-42%', 0.40, 0.42),
    ('Catering / Eventos',          '30-35%', '28-38%', 0.35, 0.38),
    ('Cafetería / Brunch',          '28-32%', '25-35%', 0.32, 0.35),
    ('Bar / Cocktails',             '25-30%', '22-33%', 0.30, 0.33),
]

FILA_TOT_03 = 4 + motor.CAPACIDAD + 1          # 35 · TOTALES de Nóminas


def _n03_nominas(wb, cambios):
    """§3 · DOM-08/DOM-31/TEC-14/TEC-26.

    Lo que había: `D5='=IF(C5<>"",C5*0.30,"")'` repetido en 20 filas, con el
    tipo de cotización ESCRITO DENTRO de la fórmula (21 veces contando la
    cabecera `D4='SS Empresa (30%)'`), sin pagas extra y con una columna
    «Horas Contratadas» que no alimentaba nada.
    """
    ws = wb['Nóminas']
    sub = ws['A2'].value if isinstance(ws['A2'].value, str) else None

    # 1) 20 → 30 empleados. La cola (TOTALES en 25, pie en 27) baja 10 filas y
    #    `=SUM(C5:C24)` se ESTIRA a `C34` (lo hace `motor._corre_cola`).
    delta = motor.expandir_filas(ws, 24, 4 + motor.CAPACIDAD, cola=(25, 27))
    if delta:
        cambios.append('03:Nóminas!5:34: bloque de empleados 20 → {} '
                       '(§1.3, DOM-32)'.format(motor.CAPACIDAD))

    _merges(ws, ['A1:I1', 'A3:I3',
                 'A{0}:I{0}'.format(FILA_TOT_03 + 2)])
    ws['A1'] = 'Nóminas — Mes: _______________'
    ws['A3'] = sub or ('AI Chef Pro · aichef.pro — Kit Gestión de Personal '
                       'y Turnos')
    ws['A2'] = None
    ws['B2'] = None
    ws['C2'] = None

    # 2) el 0,30 sale de las 21 fórmulas y pasa a UNA celda verde (§1.4)
    motor._limpiar_dv(ws)
    coord = motor.parametro(ws, 2, 'ss_empresa', col_rotulo=1, col_valor=3)
    _formula(ws, 'D2', '="El coste total de cada empleado incluye un "'
                       '&TEXT($C$2,"0%")&" de cotización empresarial sobre el '
                       'bruto ya prorrateado"')
    cambios.append('03:Nóminas!{}: tipo de cotización empresarial en celda '
                   'verde (33 %) — antes iba dentro de 20 fórmulas y de la '
                   'cabecera D4 (DOM-08/TEC-14)'.format(coord))

    # 3) cabecera de 6 → 9 columnas
    _cabecera(ws, 4, ['Empleado', 'Puesto', 'Salario Bruto Mes (€)',
                      'Nº de pagas/año', 'Bruto prorrateado/mes (€)',
                      'Cotización SS empresa (€)', 'Coste total/mes (€)',
                      'Horas contratadas/semana', 'Coste/hora (€)'])
    _anchos(ws, {'A': 24, 'B': 18, 'C': 18, 'D': 14, 'E': 20, 'F': 20,
                 'G': 18, 'H': 20, 'I': 14})

    for f in range(5, 4 + motor.CAPACIDAD + 1):
        ws['C{}'.format(f)].value = None
        ws['D{}'.format(f)].value = 14          # §3 · por defecto 14 pagas
        ws['H{}'.format(f)].value = None
        _formula(ws, 'E{}'.format(f),
                 '=IF(OR($C{f}="",$D{f}=""),"",ROUND($C{f}*$D{f}/12,2))'
                 .format(f=f))
        _formula(ws, 'F{}'.format(f),
                 '=IF($E{f}="","",ROUND($E{f}*$C$2,2))'.format(f=f))
        _formula(ws, 'G{}'.format(f),
                 '=IF($E{f}="","",ROUND($E{f}+$F{f},2))'.format(f=f))
        # 52/12 = las semanas que tiene un mes. Se deja a la vista dentro de la
        # fórmula en vez de escribir «4,33», que es el mismo número redondeado
        # y no se entiende al leerlo.
        _formula(ws, 'I{}'.format(f),
                 '=IFERROR(IF(OR($G{f}="",$H{f}="",$H{f}=0),"",'
                 'ROUND($G{f}/($H{f}*52/12),2)),"")'.format(f=f))

    # 4) TOTALES coherentes con las columnas nuevas
    t = FILA_TOT_03
    ws['A{}'.format(t)] = 'TOTALES'
    ws['A{}'.format(t)].font = Font(bold=True)
    ws['B{}'.format(t)].value = None
    ws['D{}'.format(t)].value = None
    for col in ('C', 'E', 'F', 'G', 'H'):
        _formula(ws, '{}{}'.format(col, t),
                 '=SUM(${c}$5:${c}${u})'.format(c=col, u=t - 1),
                 motor.FMT_EUR if col in ('C', 'E', 'F', 'G')
                 else motor.FMT_DEC2)
    _formula(ws, 'I{}'.format(t),
             '=IFERROR(IF(OR($G${t}="",$H${t}=0),"",'
             'ROUND($G${t}/($H${t}*52/12),2)),"")'.format(t=t),
             motor.FMT_EUR)
    for col in 'ACDEFGHI':
        ws['{}{}'.format(col, t)].fill = PatternFill('solid', fgColor='ECEFF1')

    _dv(ws, 'D5:D{}'.format(t - 1), ['12', '14', '15'],
        'Número de pagas no válido',
        'Doce pagas = extras prorrateadas mes a mes. Catorce (lo habitual en '
        'hostelería) o quince = las extras se pagan aparte, pero el coste '
        'mensual REAL sigue siendo el prorrateado: es lo que calcula la '
        'columna E.',
        '12, 14 o 15. La columna E prorratea el bruto anual a doce meses.')
    _pie(ws, t + 2, 9)
    cambios.append('03:Nóminas!D4:I{}: pagas prorrateadas, cotización por '
                   'parámetro y coste/hora — la columna «Horas Contratadas» '
                   'deja de estar muerta (DOM-31/TEC-26)'.format(t))


def _n03_ratio(wb, cambios):
    """§3 · DOM-16/TEC-10/TEC-11/COM-11/COM-17 — el semáforo deja de felicitar
    al que no ha medido nada y de suspender a la alta cocina.

    Lo que había: `B7='=IF(B4>0,B5/B4*100,0)'` (con la hoja vacía daba 0) y
    `B9='=IF(B7<30,"🟢 EXCELENTE…"…)'`, así que un fichero recién descargado
    abría en verde EXCELENTE; y un fine dining al 38 % —que su propia tabla de
    la fila 16 declara correcto— salía en rojo.
    """
    ws = wb['Ratio Coste Laboral']
    motor._limpiar_dv(ws)
    _merges(ws, ['A1:E1', 'A2:E2', 'A22:E22', 'B9:E9'])
    _anchos(ws, {'A': 34, 'B': 20, 'C': 24, 'D': 16, 'E': 16})

    _rotulo(ws, 3, 'Tipo de negocio:')
    _verde(ws, 'B3')
    ws['B3'].value = None
    _dv(ws, 'B3', [t[0] for t in TIPOS_NEGOCIO], 'Tipo de negocio no válido',
        'De aquí salen los dos umbrales del semáforo por VLOOKUP sobre la '
        'tabla de esta misma hoja. Si lo dejas en blanco, el semáforo usa el '
        '30 % / 35 % genérico, que es lo que hacía la versión 1.1 para todo '
        'el mundo.',
        'Elige uno de los seis tipos de la tabla de referencia de abajo.')

    _rotulo(ws, 4, 'Ventas Netas del Mes (€):')
    _verde(ws, 'B4', fmt=motor.FMT_EUR)
    _rotulo(ws, 5, 'Coste Laboral Total (€):')
    _formula(ws, 'B5', "=Nóminas!$G${}".format(FILA_TOT_03), motor.FMT_EUR)

    _rotulo(ws, 7, 'RATIO COSTE LABORAL (%):', negrita=True)
    _formula(ws, 'B7',
             '=IFERROR(IF(OR($B$4="",$B$4<=0),"",ROUND($B$5/$B$4,4)),"")',
             motor.FMT_PCT1)
    _rotulo(ws, 7, 'Ratio objetivo de tu tipo:', col=3)
    _formula(ws, 'D7', '=IFERROR(VLOOKUP($B$3,$A$14:$E$19,4,FALSE),0.3)',
             motor.FMT_PCT1)
    _rotulo(ws, 8, 'Máximo aceptable de tu tipo:', col=3)
    _formula(ws, 'D8', '=IFERROR(VLOOKUP($B$3,$A$14:$E$19,5,FALSE),0.35)',
             motor.FMT_PCT1)

    _rotulo(ws, 9, 'Semáforo:', negrita=True)
    _formula(ws, 'B9',
             '=IF($B$7="","— introduce las ventas del mes y las nóminas",'
             'IF($B$7<$D$7,"🟢 EXCELENTE (por debajo de tu objetivo)",'
             'IF($B$7<=$D$8,"🟡 VIGILAR (en el límite)",'
             '"🔴 ACCIÓN CORRECTIVA")))', 'General')
    ws['B9'].alignment = Alignment(vertical='center')

    _rotulo(ws, 10, '▸ Sin tipo de negocio elegido el semáforo cae al 30 % / '
                    '35 % genérico, que es como se comportaba la versión 1.1.')
    ws['A10'].font = Font(size=9, italic=True)

    _rotulo(ws, 12, 'Ratios de Referencia por Tipo', negrita=True)
    _cabecera(ws, 13, ['Tipo de Negocio', 'Ratio Objetivo', 'Rango Aceptable',
                       'Objetivo % (núm.)', 'Aceptable % (núm.)'])
    for i, fila in enumerate(TIPOS_NEGOCIO):
        r = 14 + i
        ws['A{}'.format(r)] = fila[0]
        ws['B{}'.format(r)] = fila[1]
        ws['C{}'.format(r)] = fila[2]
        ws['D{}'.format(r)] = fila[3]
        ws['E{}'.format(r)] = fila[4]

    _rotulo(ws, 20, '▸ Las dos columnas numéricas son el extremo superior de '
                    'los rangos de texto: es lo que lee el VLOOKUP del '
                    'semáforo, para que la tabla y el veredicto no puedan '
                    'contradecirse.')
    ws['A20'].font = Font(size=9, italic=True)
    _pie(ws, 22, 5)
    cambios.append('03:Ratio Coste Laboral!B3/D7/D8/B9: umbrales por VLOOKUP '
                   'sobre A14:E19 y veredicto en blanco con la hoja vacía '
                   '(DOM-16/TEC-10/TEC-11/COM-17)')


def _n03_prevision(wb, cambios):
    """§3 · DOM-09/TEC-15/TEC-20/COM-09 — cubiertos por SERVICIO, no por día.

    Lo que había: `B10='=CEILING(B4/B5,1)'` con B4 = 80 cubiertos al DÍA y
    B5 = 20 cubiertos por cocinero, o sea 4 cocineros, 7 camareros y 4 barras
    = **15 personas por turno** para un casual de 80 cubiertos; y un coste
    `=B13*B15*1.30` que multiplicaba esas 15 personas por el salario, sin
    pagas, sin días de apertura y sin factor de cobertura.

    Lo que hay: la MISMA cadena que la SPEC fija para el BONUS-02 —cubiertos
    por servicio → personal por servicio → presencias/día → horas/semana →
    FTE—, que con los valores por defecto da **7 FTE** y 16.292,50 €/mes.
    """
    ws = wb['Previsión por Servicio']
    motor._limpiar_dv(ws)
    for r in range(1, 31):
        for c in range(1, 7):
            ws.cell(row=r, column=c).value = None
    _anchos(ws, {'A': 44, 'B': 16, 'C': 14, 'D': 14, 'E': 18, 'F': 4})

    ws['A1'] = 'Previsión de Personal por Servicio'
    ws['A1'].font = Font(bold=True, size=14)
    ws['A2'] = 'AI Chef Pro · aichef.pro — Kit Gestión de Personal y Turnos'
    _seccion(ws, 3, 'ENTRADAS — edita sólo las celdas verdes', 5)

    entradas = [
        (4,  'Cubiertos previstos / día:', 80, motor.FMT_ENT),
        (5,  'Servicios al día (comida + cena):', 2, motor.FMT_ENT),
        (7,  'Cubiertos por cocinero y servicio:', 25, motor.FMT_ENT),
        (8,  'Cubiertos por camarero y servicio:', 22, motor.FMT_ENT),
        (9,  'Cubiertos por persona de barra y servicio:', 80, motor.FMT_ENT),
        (10, 'Horas efectivas por servicio:', 4, motor.FMT_ENT),
        (11, 'Días de apertura / semana:', 6, motor.FMT_ENT),
        (12, 'Jornada contratada (h/semana):', 40, motor.FMT_ENT),
        (13, 'Factor de cobertura (vacaciones, bajas y descansos):', 1.15,
         motor.FMT_DEC2),
        (14, 'Salario medio bruto (€/mes):', 1500, motor.FMT_EUR),
        (15, 'Nº de pagas / año:', 14, motor.FMT_ENT),
        (16, 'Tipo de SS a cargo de la empresa (%):', 0.33, motor.FMT_PCT1),
    ]
    for fila, rotulo, valor, fmt in entradas:
        _rotulo(ws, fila, rotulo)
        _verde(ws, 'B{}'.format(fila), valor, fmt)

    _rotulo(ws, 6, 'Cubiertos por SERVICIO:')
    _formula(ws, 'B6', '=IFERROR(IF(OR($B$4="",$B$5="",$B$5=0),"",'
                       'ROUND($B$4/$B$5,0)),"")', motor.FMT_ENT)
    ws['C6'] = '← es la cifra que dimensiona el turno, no los cubiertos del día'
    ws['C6'].font = Font(size=9, italic=True)

    _dv(ws, 'B5', ['1', '2', '3'], 'Servicios al día no válido',
        'Uno (sólo comidas o sólo cenas), dos (comida y cena) o tres (desayuno, '
        'comida y cena). Es lo que reparte los cubiertos del día entre turnos: '
        'ochenta cubiertos en dos servicios son cuarenta por servicio, y el '
        'equipo se dimensiona con esos cuarenta.',
        'Elige 1, 2 o 3.')

    _seccion(ws, 17, 'RESULTADO — de cubiertos a plantilla', 5)
    for i, txt in enumerate(['Cocina', 'Sala', 'Barra', 'Total / servicio']):
        cel = ws.cell(row=17, column=2 + i, value=txt)
        cel.font = Font(bold=True, size=10)
        cel.alignment = Alignment(horizontal='center')

    _rotulo(ws, 18, 'Personal por SERVICIO:')
    for col, ratio in (('B', '$B$7'), ('C', '$B$8'), ('D', '$B$9')):
        _formula(ws, '{}18'.format(col),
                 '=IFERROR(IF(OR($B$6="",{r}="",{r}=0),0,'
                 'CEILING($B$6/{r},1)),0)'.format(r=ratio), motor.FMT_ENT)
    _formula(ws, 'E18', '=IF($B$6="","",$B$18+$C$18+$D$18)', motor.FMT_ENT)

    _rotulo(ws, 19, 'Presencias al día (personas × servicios):')
    _formula(ws, 'B19', '=IF(OR($E$18="",$B$5=""),"",$E$18*$B$5)',
             motor.FMT_ENT)
    _rotulo(ws, 20, 'Horas de plantilla necesarias / semana:')
    _formula(ws, 'B20', '=IF(OR($B$19="",$B$10="",$B$11=""),"",'
                        '$B$19*$B$10*$B$11)', motor.FMT_ENT)
    _rotulo(ws, 21, 'Plantilla necesaria (FTE):', negrita=True)
    _formula(ws, 'B21', '=IFERROR(IF(OR($B$20="",$B$12="",$B$12=0),"",'
                        'CEILING($B$20/$B$12*$B$13,1)),"")', motor.FMT_ENT)
    _rotulo(ws, 22, 'Coste laboral estimado del equipo (€/mes):', negrita=True)
    _formula(ws, 'B22', '=IFERROR(IF(OR($B$21="",$B$14="",$B$15=""),"",'
                        'ROUND($B$21*$B$14*$B$15/12*(1+$B$16),2)),"")',
             motor.FMT_EUR)

    ws['A24'] = ('▸ FTE = personas a jornada completa, no personas por turno: '
                 'las 240 h/semana que salen por defecto son siete contratos '
                 'de 40 h con el 15 % de cobertura de libranzas, vacaciones y '
                 'bajas ya dentro.')
    ws['A25'] = ('▸ El coste es bruto de convenio × las pagas que elijas, '
                 'prorrateado a doce meses y con la cotización empresarial '
                 'encima. Para el coste REAL de tu equipo usa la hoja '
                 '«Nóminas», que parte de tus contratos.')
    for r in (24, 25):
        ws.cell(row=r, column=1).font = Font(size=9, italic=True)
        ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True,
                                                       vertical='top')
        ws.row_dimensions[r].height = 28
    _pie(ws, 26, 5)
    _merges(ws, ['A1:E1', 'A2:E2', 'A24:E24', 'A25:E25', 'A26:E26'])
    cambios.append('03:Previsión por Servicio!B6/B18:E18/B21/B22: un solo '
                   'modelo de dimensionamiento (cubiertos por SERVICIO → '
                   '7 FTE → 16.292,50 €/mes) — antes 15 personas por turno '
                   '(DOM-09/TEC-15/TEC-20/COM-09)')


def _n03_instrucciones(wb, cambios):
    ws = wb['Instrucciones']
    _instrucciones(ws, [
        '03 · Coste Laboral Mensual',
        None,
        'Cómo usar esta plantilla:',
        "▸ Vuelca los contratos en la hoja 'Nóminas': bruto mensual, número de "
        'pagas al año y horas contratadas por semana. Lo demás se calcula.',
        '▸ El tipo de cotización empresarial vive en UNA celda verde (C2 de '
        "'Nóminas'), no dentro de las fórmulas: ajústalo a tu CNAE, a tu tipo "
        'de contrato y a tu convenio. El 33 % por defecto es lo que ronda un '
        'indefinido general sumando contingencias comunes, desempleo, AT/EP, '
        'FOGASA, formación profesional y MEI.',
        '▸ Las pagas extra se PRORRATEAN: catorce pagas de 1.500 € no cuestan '
        '1.500 € al mes, cuestan 1.750 €. La columna «Bruto prorrateado/mes» '
        'es la que hay que mirar para presupuestar.',
        '▸ La columna «Coste/hora» es el número que hay que llevar a la '
        "tarifa horaria del fichero 02: es coste real de empresa, no el bruto "
        'del convenio.',
        "▸ La hoja 'Ratio Coste Laboral' compara ese coste con tus ventas "
        'netas del mes y lo juzga con los umbrales de TU tipo de negocio, '
        'elegido en la celda verde B3.',
        "▸ La hoja 'Previsión por Servicio' dimensiona el equipo al revés: de "
        'cubiertos por servicio a plantilla necesaria en jornadas completas.',
        None,
        'Lo que cambia respecto de la versión 1.1:',
        '▸ El semáforo ya no da «EXCELENTE» con la hoja en blanco: sin ventas '
        'introducidas no hay veredicto.',
        '▸ Y ya no suspende a la alta cocina: un fine dining al 38 % está '
        'donde debe estar, y un fast casual al 38 % está en pérdidas. Los dos '
        'umbrales salen de la tabla de referencia de esa misma hoja.',
        '▸ La previsión de personal razona por SERVICIO. Ochenta cubiertos al '
        'día en dos servicios son cuarenta por servicio: dimensionar el turno '
        'con los ochenta duplicaba la plantilla.',
        None,
        'Aviso: esto es una herramienta de gestión, no un cálculo de nómina. '
        'La cotización real depende de tu CNAE, del grupo de cotización, de '
        'las bonificaciones que te apliquen y del convenio. Contrástalo con '
        'tu gestoría antes de firmar nada.',
    ])
    cambios.append('03:Instrucciones!B2:B22: reescritas — desaparece «La '
                   'Seguridad Social empresa (~30%)» y el semáforo fijo de '
                   '30/35 % (DOM-08/COM-17)')


# ==========================================================================
# 04 · ONBOARDING NUEVO EMPLEADO  (SPEC §4, bloque 04)
# ==========================================================================
#: Las TRES tareas que faltaban y tienen plazo legal (DOM-15/§7-bis.3). Entran
#: al final del primer tramo, que pasa de 10 a 13 filas y con él el checklist
#: de 47 a **50** tareas. `(texto, plazo)`.
TAREAS_NUEVAS_04 = [
    ('Comunicación del contrato a Contrat@ (SEPE) — 10 días hábiles desde la '
     'firma', 'Día 7'),
    ('Copia básica del contrato a la representación legal de los trabajadores '
     '(RLT) — 10 días', 'Día 7'),
    ('Modelo 145 de IRPF firmado (situación personal y familiar para calcular '
     'la retención)', 'Día 1'),
]

#: DOM-15 · el alta en la Seguridad Social no es «papeleo del primer día»:
#: tiene que estar hecha ANTES de que el trabajador empiece a trabajar.
TAREA_ALTA_SS = ('Alta en Seguridad Social (TA.2/S) — OBLIGATORIO ANTES del '
                 'inicio de la jornada (art. 32.3 RD 84/1996)')

#: DOM-22/TEC-12 · la columna «Categoría» venía cortada a 14 caracteres
#: exactos («FORMACIÓN OBLI», «PERIODO DE PRU»): un `slice[:14]` del generador.
CATEGORIAS_04 = ['DOCUMENTACIÓN LEGAL', 'FORMACIÓN OBLIGATORIA',
                 'EQUIPAMIENTO Y ACCESOS', 'FORMACIÓN OPERATIVA',
                 'PERIODO DE PRUEBA']

#: §4 · «Fecha Límite» estaba vacía en las 47 filas. Se precarga con el plazo
#: real de cada tarea, en la escala del propio checklist: Día −1 (antes del
#: alta), Día 1, Día 7 y Día 30. El signo menos es un guion normal a propósito:
#: el U+2212 degenera al pasar por un heredoc del shell.
PLAZOS_04 = [
    # 1 · Documentación legal y administrativa (13)
    ['Día -1', 'Día -1', 'Día -1', 'Día -1', 'Día 1', 'Día 1', 'Día 1',
     'Día 1', 'Día 1', 'Día 7', 'Día 7', 'Día 7', 'Día 1'],
    # 2 · Formación obligatoria (8)
    ['Día 1', 'Día 7', 'Día 7', 'Día 1', 'Día 7', 'Día 7', 'Día 1', 'Día 30'],
    # 3 · Equipamiento y accesos (9)
    ['Día 1', 'Día 1', 'Día 1', 'Día 1', 'Día 7', 'Día 1', 'Día 1', 'Día 7',
     'Día 1'],
    # 4 · Formación operativa (12)
    ['Día 1', 'Día 1', 'Día 1', 'Día 1', 'Día 7', 'Día 7', 'Día 7', 'Día 7',
     'Día 7', 'Día 7', 'Día 30', 'Día 30'],
    # 5 · Periodo de prueba y evaluación (8)
    ['Día 1', 'Día 7', 'Día 30', 'Día 7', 'Día 30', 'Día 30', 'Día 30',
     'Día 30'],
]


def _n04(wb, cambios):
    """§4 · DOM-01/DOM-15/DOM-22/DOM-28/TEC-02/TEC-12/TEC-13/COM-03.

    El defecto estrella: `C68='=COUNTIF(F7:F65,"✓")'` barre un rango CONTINUO
    que se traga las cabeceras de las secciones 2ª a 5ª —`F19`, `F30`, `F42` y
    `F57` valen literalmente «✓»—, así que un checklist en blanco abre en
    «4 de 51 completadas» y un 8,51 %. Y es justo la mejora que el changelog
    v1.1 vende como estrella.

    Se hacen LAS DOS cosas que apunta la SPEC: las cabeceras pasan a decir
    «Hecho» (para que nunca vuelva a haber un «✓» que no sea una tarea hecha)
    **y** los contadores se acotan por tramo. Con una sola de las dos, el
    siguiente que añada una sección volvería a romperlo.
    """
    ws = wb['Checklist Onboarding']
    secciones = motor.secciones_04(ws)

    # 1) las tres tareas que faltaban (DOM-15). Centinela de idempotencia: el
    #    primer tramo mide 10 filas en la v1.1 y 13 cuando ya están puestas.
    r_tit, hdr, r0, r1 = secciones[0]
    if r1 - r0 + 1 == 10:
        for _ in TAREAS_NUEVAS_04:
            motor.insertar_fila(ws, r1 + 1)
        for i, par in enumerate(TAREAS_NUEVAS_04):
            f = r1 + 1 + i
            ws.cell(row=f, column=1, value=r1 - r0 + 2 + i)
            ws.cell(row=f, column=2, value=par[0])
        cambios.append('04:Checklist Onboarding!B{}:B{}: +3 tareas con plazo '
                       'legal (Contrat@/SEPE, copia básica a la RLT, modelo '
                       '145) — 47 → 50 (DOM-15)'.format(r1 + 1, r1 + 3))
        secciones = motor.secciones_04(ws)

    # 2) alta en la SS: ANTES del inicio de la jornada
    for f in range(secciones[0][2], secciones[0][3] + 1):
        v = ws.cell(row=f, column=2).value
        if isinstance(v, str) and v.startswith('Alta en Seguridad Social'):
            if v != TAREA_ALTA_SS:
                ws.cell(row=f, column=2).value = TAREA_ALTA_SS
                cambios.append('04:Checklist Onboarding!B{}: el alta en la SS '
                               'pasa a ser previa al inicio de la jornada '
                               '(art. 32.3 RD 84/1996, DOM-15)'.format(f))

    # 3) cabeceras «✓» → «Hecho», categorías completas y plazos
    tramos = []
    for i, sec in enumerate(secciones):
        r_tit, hdr, r0, r1 = sec
        tramos.append((r0, r1))
        ws.cell(row=hdr, column=6).value = 'Hecho'
        ws.cell(row=hdr, column=5).value = 'Fecha Límite'
        plazos = PLAZOS_04[i] if i < len(PLAZOS_04) else []
        for j, f in enumerate(range(r0, r1 + 1)):
            ws.cell(row=f, column=1).value = j + 1
            ws.cell(row=f, column=3).value = CATEGORIAS_04[i]
            if j < len(plazos):
                ws.cell(row=f, column=5).value = plazos[j]
    _anchos(ws, {'A': 5, 'B': 52, 'C': 22, 'D': 18, 'E': 14, 'F': 10,
                 'G': 24})

    # 4) validación de «Hecho» sobre TODOS los tramos, incluidas las 3 nuevas.
    #    Se retiran todas las DV de la hoja antes: la heredada de la v1.1
    #    enumeraba las 47 celdas una a una y no cubría las filas nuevas.
    ws.data_validations.dataValidation = []
    dv = DataValidation(
        type='list', formula1='"✓,✗,—"', allow_blank=True,
        showErrorMessage=True, errorTitle='Marca no válida',
        error='✓ hecha · ✗ pendiente · — no aplica a este puesto.',
        errorStyle='stop', showInputMessage=True,
        promptTitle='{} · Hecho'.format(MARCA_B),
        prompt='Marca «—» en lo que NO aplique a este puesto (un cocinero de '
               'partida no necesita el acceso al TPV): esas tareas salen del '
               'denominador y el progreso puede llegar al 100 %.')
    ws.add_data_validation(dv)
    for r0, r1 in tramos:
        dv.add('F{}:F{}'.format(r0, r1))

    # 5) los contadores, acotados por TRAMO
    fila_res = None
    for r in range(1, ws.max_row + 1):
        v = ws.cell(row=r, column=1).value
        if isinstance(v, str) and v.strip().upper() == 'RESUMEN':
            fila_res = r
            break
    if fila_res is None:
        return
    hechas = '+'.join('COUNTIF($F${}:$F${},"✓")'.format(a, b)
                      for a, b in tramos)
    total = '+'.join('COUNTIF($B${}:$B${},"?*")'.format(a, b)
                     for a, b in tramos)
    noaplica = '+'.join('COUNTIF($F${}:$F${},"—")'.format(a, b)
                        for a, b in tramos)
    f1, f2, f3 = fila_res + 1, fila_res + 2, fila_res + 3
    ws.cell(row=f1, column=2, value='Tareas completadas:')
    _formula(ws, 'C{}'.format(f1), '=' + hechas, motor.FMT_ENT)
    ws.cell(row=f1, column=4, value='de')
    _formula(ws, 'E{}'.format(f1), '=' + total, motor.FMT_ENT)
    ws.cell(row=f2, column=2,
            value='Total tareas aplicables (sin las marcadas «—»):')
    _formula(ws, 'C{}'.format(f2),
             '=$E${}-({})'.format(f1, noaplica), motor.FMT_ENT)
    ws.cell(row=f3, column=2, value='Progreso:')
    _formula(ws, 'C{}'.format(f3),
             '=IF($C${d}>0,$C${n}/$C${d},0)'.format(n=f1, d=f2),
             motor.FMT_PCT1)
    for f in (f1, f2, f3):
        ws.cell(row=f, column=2).font = Font(bold=True)
    ws.cell(row=fila_res, column=1).font = Font(bold=True, size=11)
    cambios.append('04:Checklist Onboarding!C{}/C{}/C{}: contadores acotados '
                   'por tramo y denominador sin las tareas «—» — el checklist '
                   'recién descargado marca 0 %, no 8,51 % '
                   '(DOM-01/DOM-28/TEC-02/TEC-13)'.format(f1, f2, f3))


def _n04_instrucciones(wb, cambios):
    ws = wb['Instrucciones']
    _instrucciones(ws, [
        '04 · Onboarding Nuevo Empleado',
        None,
        'Cómo usar esta plantilla:',
        '▸ Duplica el fichero para cada incorporación y escribe arriba el '
        'nombre, el puesto y la fecha de alta.',
        '▸ Marca cada tarea en la columna «Hecho»: ✓ hecha · ✗ pendiente · '
        '— no aplica a este puesto.',
        '▸ La «—» es importante: saca la tarea del denominador. Un cocinero '
        'de partida que no necesita el acceso al TPV puede llegar al 100 % '
        'igual que un jefe de sala.',
        '▸ La columna «Fecha Límite» viene precargada con el plazo de cada '
        'tarea en días desde el alta: Día -1 es ANTES de que empiece a '
        'trabajar. Sustitúyela por la fecha real si prefieres el calendario.',
        '▸ El resumen del final cuenta tramo a tramo, así que las cabeceras '
        'de sección ya no se cuelan como tareas hechas: un checklist en '
        'blanco marca 0 %.',
        None,
        'Categorías (cada sección lleva su color):',
        '▸ Azul = Documentación legal y administrativa',
        '▸ Naranja = Formación obligatoria',
        '▸ Verde = Equipamiento y accesos',
        '▸ Morado = Formación operativa',
        '▸ Rojo = Periodo de prueba y evaluación',
        None,
        'Plazos que no dependen de ti:',
        '▸ El alta en la Seguridad Social tiene que estar presentada ANTES '
        'del inicio de la jornada (art. 32.3 del RD 84/1996). No es papeleo '
        'del primer día: es requisito para que ese primer día sea legal.',
        '▸ El contrato se comunica a Contrat@ (SEPE) dentro de los 10 días '
        'hábiles siguientes a su formalización, y la copia básica va a la '
        'representación legal de los trabajadores en 10 días.',
        '▸ El modelo 145 lo firma la persona para que puedas calcular bien '
        'su retención de IRPF; sin él, la retención se aplica sin cargas '
        'familiares.',
        None,
        'Aviso: los plazos son los del Estatuto de los Trabajadores y su '
        'normativa de desarrollo a agosto de 2026. Tu convenio puede exigir '
        'más trámites, nunca menos.',
    ])
    cambios.append('04:Instrucciones!B2:B26: reescritas — «Hecho», el papel '
                   'de la marca «—» y los tres plazos legales nuevos')
