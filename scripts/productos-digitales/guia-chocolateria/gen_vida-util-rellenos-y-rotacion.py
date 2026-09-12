#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_vida-util-rellenos-y-rotacion.py — libro 5 de «Cómo Montar una
Chocolatería» (SPEC §2.2, fila 5; constructor C2).

Hojas: Instrucciones · Parámetros · Tipo de Relleno y aw · Vida Útil Declarada ·
Etiquetado o Granel · Temperatura y Vitrina · Lote y Merma por Caducidad.

QUÉ DECIDE ESTE LIBRO
---------------------
Cuánto dura cada bombón, en qué vitrina va, con qué papel legal, y de cuánto
haces cada lote. En euros: lo que se te caduca al año por producir tandas más
grandes de lo que vendes dentro de la vida útil.

LAS TRES REGLAS DURAS QUE GOBIERNAN ESTE LIBRO
----------------------------------------------
1. **`CHN-30`: la vida útil la declara el operador en su plan de APPCC.** El
   libro NUNCA la calcula ni la presenta como norma. Es celda verde, con un
   valor de partida declarado como supuesto, y así lo dice la propia hoja.
2. **D30, frontera con el kit:** los diez plazos orientativos son los del Kit
   de Tareas Chocolatería (`02-partidas-produccion.xlsx!Moldeado`). La guía los
   CITA, no los reescribe. Lo que construye es lo que el kit no tiene:
   actividad de agua, etiqueta o granel, lote económico y merma en euros/año.
3. **D31, la vitrina:** el semáforo SÓLO avisa por encima de 20 °C, que es
   donde la manteca de cacao empieza a fundir. Está PROHIBIDO un semáforo que
   ponga en rojo los 16-18 °C que el propio kit publica como objetivo.

D47, Y NO ES UN MATIZ: ETIQUETADO Y GRANEL NO SON EL MISMO RÉGIMEN
------------------------------------------------------------------
El art. 4.2 del RD 1021/2022 fija la temperatura de conservación POR LA
ETIQUETA que pone quien ha producido y envasado: se aplica a la referencia que
sale envasada con su etiqueta. Para el bombón despachado a granel en la vitrina
no hay etiqueta, así que la referencia no es el 4.2 sino tu propio sistema de
autocontrol. `CHN-87`: «chocolate», «cacao», «bombón» y «confitería» aparecen
CERO veces en todo el RD 1021/2022. Por eso la hoja «Etiquetado o Granel» lleva
una celda verde de dos valores y la salida cambia de COLUMNA en cada caso.

DECISIONES TÉCNICAS
-------------------
* Cero constantes dentro de las fórmulas; `IFERROR(...,"")` en toda división;
  «sin dato» = `""`, nunca `0`; semáforos con `ISNUMBER`; DV contra RANGO.
  Prohibidas INDIRECT, COUNTA, PMT, OFFSET, XLOOKUP, LET, LAMBDA, RANK,
  NETWORKDAYS e IRR: cero usos.
* El coste de materia por pieza llega por celda verde con su valor por defecto
  declarado: el precio de la cobertura vive en el libro 3 y el escandallo en el
  4 (regla «un concepto, una fuente»). **No hay ninguna fórmula que nombre otro
  fichero.**
* Un surtido caduca con su pieza más corta, no con la media: las cuatro cajas
  llevan columna propia con la pieza más corta que llevan dentro y su semáforo.

Salida fija: build/vida-util-rellenos-y-rotacion.xlsx
             + build/mapa-vida-util-rellenos-y-rotacion.json
Uso: /usr/local/bin/python3 gen_vida-util-rellenos-y-rotacion.py
Via: Claude Code
"""
import datetime
import os
import re
import sys

from openpyxl import Workbook
from openpyxl.styles import Font

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import _comun_chocolateria as C                                # noqa: E402
import _comun_libros_3_5 as X                                  # noqa: E402
import datos_ejemplo as D                                      # noqa: E402
import motor                                                   # noqa: E402

NOMBRE = 'vida-util-rellenos-y-rotacion'
TITULO = 'Vida Útil de los Rellenos y Rotación'

H_INS = 'Instrucciones'
H_PAR = 'Parámetros'
H_AW = 'Tipo de Relleno y aw'
H_VU = 'Vida Útil Declarada'
H_ETQ = 'Etiquetado o Granel'
H_TMP = 'Temperatura y Vitrina'
H_LOT = 'Lote y Merma por Caducidad'

QPAR = "'" + H_PAR + "'!"
QAW = "'" + H_AW + "'!"
QVU = "'" + H_VU + "'!"
QETQ = "'" + H_ETQ + "'!"
QLOT = "'" + H_LOT + "'!"

N = motor.NARROW

# --- Parámetros: coordenadas ----------------------------------------------
P_TICK = 'B6'
P_PZT = 'B7'
P_DIAS = 'B8'
P_PZANO = 'B9'
P_SEM = 'B10'
P_AW = 'B11'
P_TALARMA = 'B12'
P_HRMAX = 'B13'
P_LANZA = 'B14'
P_MANT = 'B15'
P_UMBMERMA = 'B16'

A = lambda coord: QPAR + '$' + coord[0] + '$' + coord[1:]      # noqa: E731

# --- Filas ----------------------------------------------------------------
REF_CAB = 15
REF_INI = 16
REF_FIN = REF_INI + len(D.CARTA) - 1             # 43
REF_TOT = REF_FIN + 1                            # 44

VIAS_INI = 7                                     # bloque de las dos vías
VIAS_FIN = VIAS_INI + 1

CLIMA_ORDEN = ('obrador', 'camara', 'nevera_rellenos', 'sala_tienda', 'vitrina')
CLIMA_CAB = 6
CLIMA_INI = 7
CLIMA_FIN = CLIMA_INI + len(CLIMA_ORDEN) - 1     # 11

VIT_CAB = 14
VIT_INI = 15                                     # tres entradas + umbral
VIT_TMIN = VIT_INI
VIT_TMAX = VIT_INI + 1
VIT_HR = VIT_INI + 2
VIT_UMB = VIT_INI + 3                            # 18

TMP_CAB = 21
TMP_INI = 22
TMP_FIN = TMP_INI + len(D.CARTA) - 1             # 49
TMP_TOT = TMP_FIN + 1

LISTAS_AW = 60
LISTAS_VU = 60
LISTAS_ETQ = 60

IDS_LEGALES = ('CHN-30', 'CHN-30b', 'CHN-87', 'CHN-35', 'CHN-36', 'CHN-89',
               'CHN-38', 'CHN-33', 'CHN-31')

# --- Supuestos declarados de este libro -----------------------------------
AW_SIN_RELLENO = 0.40
FUENTE_AW_SIN_RELLENO = 'supuesto'
AW_UMBRAL = 0.85
T_DECLARADA_VITRINA = 18.0
T_DECLARADA_FRIO = 4.0
VITRINA_TMIN = 16.0
VITRINA_TMAX = 18.0
VITRINA_HR = 50.0
COSTE_LANZAMIENTO = 35.0
COSTE_MANTENIMIENTO = 0.25
UMBRAL_MERMA = 150.0
SEMANAS_ANO = 52
FECHA_ELABORACION = datetime.date(2026, 9, 14)

TIPOS_FECHA = ('consumo preferente', 'caducidad')
ORIGEN_AW = ('medida con higrómetro', 'estimada por ti')

_UNIDAD_DIAS = {'dias': 1, 'semanas': 7, 'meses': 30}
_RX_PLAZO = re.compile(r'^(\d+)-(\d+)\s+(dias|semanas|meses)$')


# --------------------------------------------------------------------------
# Datos derivados de `datos_ejemplo`
# --------------------------------------------------------------------------
def plazo_en_dias(plazo):
    """Equivalencia en DÍAS del plazo literal del kit. La conversión es
    aritmética NUESTRA -el kit escribe «4-8 semanas»- y así se dice en la hoja;
    el plazo literal se publica al lado, sin tocar."""
    m = _RX_PLAZO.match(plazo)
    if not m:
        return None, None
    u = _UNIDAD_DIAS[m.group(3)]
    return int(m.group(1)) * u, int(m.group(2)) * u


PLAZOS = {}
for _fam, _pl, _nota in D.VIDA_UTIL_KIT:
    PLAZOS[_fam] = (_pl, _nota) + plazo_en_dias(_pl)


def aw_de(r):
    """Actividad de agua de la pieza. Con relleno, la del relleno; sin relleno,
    el supuesto del chocolate templado; una caja, la MÁS ALTA de lo que lleva
    dentro, porque un surtido se comporta como su pieza más delicada."""
    if D.es_caja(r):
        return max(aw_de(D.ref(i)) for i, _n in r['composicion_caja'])
    if r['relleno']:
        return D.RELLENOS[r['relleno']]['aw']
    return AW_SIN_RELLENO


def fuente_aw_de(r):
    if D.es_caja(r):
        return 'la más alta de las piezas que lleva dentro'
    if r['relleno']:
        return D.RELLENOS[r['relleno']]['fuente_aw']
    return FUENTE_AW_SIN_RELLENO


def tipo_relleno_de(r):
    if D.es_caja(r):
        return 'Surtido: varias piezas con rellenos distintos'
    if r['relleno']:
        return D.RELLENOS[r['relleno']]['nombre']
    return 'Sin relleno: chocolate templado'


def pieza_mas_corta(r):
    """Días de la pieza más corta de un surtido. Sólo para las cajas."""
    if not D.es_caja(r):
        return None
    return min(PLAZOS[D.ref(i)['familia_vida_util']][2]
               for i, _n in r['composicion_caja'])


def ventas_semana(r):
    piezas = (D.P('tickets_dia_crucero') * D.P('piezas_por_ticket')
              * D.NEGOCIO['dias_apertura_anio'])
    return piezas * r['mix_pct'] / 100.0 / SEMANAS_ANO


def lote_por_defecto(r):
    """Tamaño de tanda de partida. Para una pieza moldeada, los moldes por
    tanda del libro 4; para una caja -que se monta, no se moldea- lo que vendes
    en una semana."""
    if D.es_caja(r):
        return max(1, int(round(ventas_semana(r))))
    return D.piezas_por_tanda(r)


def vida_util_por_defecto(r):
    """Valor de PARTIDA de la celda verde, y sólo eso: el extremo BAJO del
    plazo orientativo del kit para su familia, y en una caja el de su pieza más
    corta. NO es una vida útil: la tuya la declaras tú en tu APPCC
    (`CHN-30`)."""
    base = PLAZOS[r['familia_vida_util']][2]
    corta = pieza_mas_corta(r)
    return min(base, corta) if corta else base


def temperatura_por_defecto(r):
    """T de conservación de partida. La ganache fresca va a la nevera de
    rellenos (0-4 °C, tarea 3 del kit); el resto, a la vitrina. Una caja
    hereda el criterio de SU PIEZA MÁS DELICADA (hallazgo B6, refutación
    2026-09-12): si lleva dentro una pieza de nevera (nata fresca), la caja
    entera va a nevera, igual que ya heredaba la aw y la vida útil."""
    if D.es_caja(r):
        if any(D.ref(i)['familia_vida_util'] == 'Bombones de ganache con nata fresca'
               for i, _n in r['composicion_caja']):
            return T_DECLARADA_FRIO
        return T_DECLARADA_VITRINA
    if r['familia_vida_util'] == 'Bombones de ganache con nata fresca':
        return T_DECLARADA_FRIO
    return T_DECLARADA_VITRINA


def familia_mas_restrictiva(r):
    """Familia de vida útil de la pieza que MENOS aguanta dentro de una caja
    (hallazgo A2, refutación 2026-09-12): el plazo del kit que se compara en
    la fila de la caja (columnas D/E/F) tiene que ser el de la pieza que de
    verdad manda, no el de una familia fija mal etiquetada («nata UHT» en un
    surtido cuya pieza corta es de nata FRESCA)."""
    if not D.es_caja(r):
        return r['familia_vida_util']
    return min(
        ((D.ref(i)['familia_vida_util'],
          PLAZOS[D.ref(i)['familia_vida_util']][2])
         for i, _n in r['composicion_caja']),
        key=lambda par: par[1])[0]


FILAS = []
for _r in D.CARTA:
    FILAS.append({
        'r': _r,
        'aw': aw_de(_r),
        'fuente_aw': fuente_aw_de(_r),
        'tipo': tipo_relleno_de(_r),
        'corta': pieza_mas_corta(_r),
        'vida': vida_util_por_defecto(_r),
        'temp': temperatura_por_defecto(_r),
        'ventas': round(ventas_semana(_r), 1),
        'lote': lote_por_defecto(_r),
        'coste': round(D.coste_materia_unidad(_r), 4),
    })

#: Fila de esta hoja para cada id de `D.CARTA` (posición en `FILAS` == posición
#: en `D.CARTA`, y la fila de hoja es `REF_INI + posición`). Se usa para que
#: `L40:L43` (A2) sea una FÓRMULA `MIN` sobre la columna G de las piezas que
#: componen cada caja, en vez de la constante congelada de la auditoría.
FILA_DE_ID = {p['r']['id']: REF_INI + i for i, p in enumerate(FILAS)}


# --------------------------------------------------------------------------
# Hoja «Instrucciones»
# --------------------------------------------------------------------------
def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS)
    C.anchos(ws, {'A': 26, 'B': 34, 'C': 62})
    C.encabezar(ws, TITULO, C.NOTA_VERDES, col_fin='C')
    C.pagina(ws, apaisado=False)

    fila = 5
    C.seccion(ws, 'A%d' % fila, 'Qué Decide Este Libro')
    fila += 1
    C.parrafo(ws, fila,
              'Cuánto dura cada referencia, en qué mueble va, con qué papel '
              'legal la despachas y de cuánto haces cada tanda. Y, sobre todo, '
              'lo que te cuesta al año equivocarte de tamaño de lote: eso es '
              'la merma por caducidad, y casi nadie la mide.',
              col_fin='C', alto=46)
    fila += 2

    C.seccion(ws, 'A%d' % fila,
              'La Regla que Manda: la Vida Útil la Declaras Tú')
    fila += 1
    C.parrafo(ws, fila,
              'No existe una tabla legal con la vida útil del chocolate. La '
              'vida útil de tu producto la fijas TÚ y consta en tu plan de '
              'APPCC, con el criterio que puedas defender. Por eso la columna '
              '«vida útil que TÚ declaras» es una celda verde y NUNCA la '
              'calcula el libro: lo que ves escrito es un valor de partida '
              'tomado del extremo bajo del plazo orientativo del kit, para que '
              'la hoja funcione desde el primer minuto.',
              col_fin='C', alto=70)
    fila += 2

    C.seccion(ws, 'A%d' % fila,
              'Frontera con el Kit de Tareas Chocolatería')
    fila += 1
    C.parrafo(ws, fila,
              'Los diez plazos orientativos por familia son los del Kit de '
              'Tareas Chocolatería (12 €), fichero '
              '02-partidas-produccion.xlsx, hoja Moldeado. Esta guía los CITA '
              'y no los reescribe: lo que construye es lo que el kit no tiene '
              '-la actividad de agua por tipo de relleno, la decisión de '
              'etiqueta o granel, el tamaño de lote y la merma por caducidad '
              'en euros al año-. Si tienes el kit, ten su tabla al lado; si no '
              'lo tienes, aquí está citada fila a fila.',
              col_fin='C', alto=70)
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Etiqueta o Granel: No Es el Mismo Papel')
    fila += 1
    C.parrafo(ws, fila,
              'Si la referencia sale ENVASADA con su etiqueta, la temperatura '
              'de conservación que tú has escrito en esa etiqueta te obliga a '
              'ti (art. 4.2 del RD 1021/2022). Si se despacha A GRANEL en la '
              'vitrina no hay etiqueta, así que la referencia no es ese '
              'artículo: es tu propio sistema de autocontrol, donde la '
              'temperatura y la vida útil las declaras tú. No hay una '
              '«temperatura legal del chocolate»: el RD 1021/2022 no nombra el '
              'chocolate ni una sola vez.',
              col_fin='C', alto=70)
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Las Hojas, y Qué Hace Cada Una')
    fila += 1
    for hoja, texto in (
        (H_PAR, 'El volumen de venta, los umbrales que tú te pones y los dos '
                'costes con los que se calcula el lote. Nada de esto está '
                'escrito dentro de una fórmula.'),
        (H_AW, 'El agua disponible de cada relleno, que es lo que de verdad '
               'separa una ganache de diez días de una de dos meses. Se mide '
               'con higrómetro; mientras no la midas, es una estimación tuya y '
               'la hoja lo dice.'),
        (H_VU, 'La vida útil que TÚ declaras, al lado del plazo orientativo '
               'del kit, y la fecha que va a ir en la etiqueta. Con el aviso '
               'de las cajas: un surtido caduca con su pieza más corta.'),
        (H_ETQ, 'Envasado con etiqueta o a granel, referencia a referencia, y '
                'qué te toca en cada caso. La salida cambia de columna: no son '
                'dos formas de decir lo mismo.'),
        (H_TMP, 'Las cinco temperaturas del kit, el rango de trabajo de TU '
                'vitrina y la temperatura que declaras para cada referencia. '
                'El semáforo sólo se enciende por encima de 20' + N + '°C.'),
        (H_LOT, 'De cuánto haces cada tanda, cuánto vendes dentro de la vida '
                'útil y lo que se te caduca al año en euros. Es la hoja que '
                'paga este libro.'),
    ):
        motor.val(ws, 'A%d' % fila, hoja, bold=True)
        ws.merge_cells('B%d:C%d' % (fila, fila))
        motor.val(ws, 'B%d' % fila, texto, wrap=True)
        ws['B%d' % fila].font = Font(size=9)
        ws.row_dimensions[fila].height = 46
        fila += 1
    fila += 1

    C.seccion(ws, 'A%d' % fila, 'Cada Cuánto Se Usa')
    fila += 1
    C.parrafo(ws, fila,
              'La hoja de vida útil y la de etiqueta o granel se revisan cada '
              'vez que entra o sale una referencia de la carta, y cuando '
              'cambias una formulación. La de lote y merma, una vez al mes con '
              'las ventas reales del TPV delante: es la que te dice si estás '
              'moldeando tandas que no vendes.',
              col_fin='C', alto=46)
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'De Dónde Salen los Números del Ejemplo')
    fila += 1
    C.parrafo(ws, fila,
              'Las actividades de agua son SUPUESTOS declarados: la aw se '
              'mide, y hasta que la midas no es un dato. Los plazos '
              'orientativos son los del kit, citados. El coste de materia por '
              'pieza es el del caso de ejemplo «La Almendra» y sale del libro '
              '3 (precio de la cobertura) y del libro 4 (escandallo): aquí '
              'entra como celda verde, no como fórmula entre ficheros, así que '
              'si cambias el escandallo tienes que traerlo a mano.',
              col_fin='C', alto=70)
    fila += 2

    C.parrafo(ws, fila, C.NOTA_DESPROTEGER, col_fin='C', alto=30)
    fila += 2
    C.pie(ws, fila, col='A', col_fin='C')
    return ws


# --------------------------------------------------------------------------
# Hoja «Parámetros»
# --------------------------------------------------------------------------
def par(ws, fila, etiqueta, valor, fmt, unidad, origen, nota, formula=None):
    motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
    if formula is None:
        cel = X.entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
    else:
        cel = motor.f(ws, 'B%d' % fila, formula, fmt=fmt)
    motor.val(ws, 'C%d' % fila, unidad)
    motor.val(ws, 'D%d' % fila, origen)
    motor.val(ws, 'E%d' % fila, nota, wrap=True)
    ws['E%d' % fila].font = Font(size=9)
    ws.row_dimensions[fila].height = 36
    return cel


def hoja_parametros(wb):
    ws = wb.create_sheet(H_PAR)
    C.anchos(ws, {'A': 50, 'B': 14, 'C': 16, 'D': 22, 'E': 78})
    C.encabezar(ws, H_PAR,
                'Los umbrales de este libro te los pones TÚ: ninguno es un '
                'límite legal, y la hoja lo dice en cada nota.', col_fin='E')
    C.pagina(ws, apaisado=True)
    C.cabecera(ws, 5, (('A', 'Parámetro'), ('B', 'Valor'), ('C', 'Unidad'),
                       ('D', 'De dónde sale'), ('E', 'Nota')), altura=24)
    C.inmovilizar(ws, 5)

    par(ws, 6, 'Clientes al día en velocidad de crucero',
        D.P('tickets_dia_crucero'), C.FMT_ENT, 'tickets/día', 'supuesto',
        D.PARAMS['tickets_dia_crucero'][2])
    par(ws, 7, 'Piezas por ticket', D.P('piezas_por_ticket'), C.FMT_DEC1,
        'piezas/ticket', 'supuesto', D.PARAMS['piezas_por_ticket'][2])
    par(ws, 8, 'Días de apertura al año', D.NEGOCIO['dias_apertura_anio'],
        C.FMT_ENT, 'días/año', 'supuesto', D.NEGOCIO['nota_dias_apertura'])
    par(ws, 9, 'Piezas vendibles al año', None, C.FMT_ENT, 'piezas/año',
        'calculado',
        'Clientes al día por piezas por ticket por días de apertura. Con el '
        'mix de cada referencia se reparte en ventas por semana, que es lo que '
        'gobierna el tamaño del lote.',
        formula='=IFERROR(%s*%s*%s,"")' % (A(P_TICK), A(P_PZT), A(P_DIAS)))
    par(ws, 10, 'Semanas al año', SEMANAS_ANO, C.FMT_ENT, 'semanas',
        'supuesto',
        'Se usa para pasar la venta anual a venta semanal y la vida útil de '
        'días a semanas.')
    c = par(ws, 11, 'Umbral de vigilancia de actividad de agua (aw)',
            AW_UMBRAL, C.FMT_DEC, 'aw', 'supuesto',
            'El punto a partir del cual TÚ decides tratar la referencia como '
            'producto de vida corta y refrigerada. NO es un límite legal ni un '
            'umbral microbiológico publicado: es tu criterio, y tiene que '
            'constar en tu plan de APPCC con el argumento que lo sostiene.')
    X.nota_celda(ws, c.coordinate, 'CHN-30')
    c = par(ws, 12, 'Temperatura a la que salta la alarma de la vitrina',
            D.VITRINA_UMBRAL_ALARMA_C, C.FMT_DEC1, 'grados C',
            'kit 01-apertura-cierre.xlsx',
            'Es el punto en el que la manteca de cacao empieza a fundir, y el '
            'que publica el kit en su hoja de apertura. El semáforo de la '
            'vitrina SÓLO se enciende por encima de este número: los 16-18 '
            'grados C de objetivo del propio kit no se ponen nunca en rojo.')
    par(ws, 13, 'Humedad máxima de trabajo de la vitrina', D.CLIMA['vitrina']['hr_max'],
        C.FMT_DEC1, '% de HR', 'kit 08-apertura-cierre-negocio.xlsx',
        'Objetivo del kit para la vitrina temperada: menos del 55 % antes de '
        'montar el género. Por encima, el bombón coge humedad y aparece el '
        'velo de azúcar.')
    par(ws, 14, 'Coste de poner en marcha una tanda', COSTE_LANZAMIENTO,
        C.FMT_EUR, '€/tanda', 'supuesto',
        'Lo que cuesta arrancar una tanda al margen de su tamaño: templar, '
        'preparar moldes, limpiar y cambiar de referencia. Es el número que '
        'empuja a hacer tandas grandes; la caducidad es el que las frena.')
    par(ws, 15, 'Coste de tener una pieza parada un año', COSTE_MANTENIMIENTO,
        C.FMT_PCT, 'sobre su coste', 'supuesto',
        'Financiación, espacio de cámara y riesgo, en porcentaje del coste de '
        'materia de la pieza. Es la otra mitad del cálculo del lote.')
    par(ws, 16, 'Merma por caducidad a partir de la cual quieres un aviso',
        UMBRAL_MERMA, C.FMT_EUR, '€/año', 'supuesto',
        'Tu línea roja, no la de nadie más. Por encima de esta cifra la hoja '
        'de lote marca la referencia en rojo: no es que esté mal, es que ahí '
        'hay dinero que se está yendo a la basura.')
    return ws


# --------------------------------------------------------------------------
# Hoja «Tipo de Relleno y aw»
# --------------------------------------------------------------------------
def hoja_aw(wb):
    ws = wb.create_sheet(H_AW)
    C.anchos(ws, {'A': 9, 'B': 44, 'C': 26, 'D': 42, 'E': 10, 'F': 20,
                  'G': 40, 'H': 15, 'I': 54, 'J': 62})
    C.encabezar(ws, H_AW,
                'El agua disponible es lo que separa una ganache de diez días '
                'de una de dos meses. Se MIDE con un higrómetro de actividad '
                'de agua; mientras no la midas, lo que hay aquí es una '
                'estimación tuya, y así se marca.', col_fin='J')
    C.pagina(ws, apaisado=True)

    listas, _f = C.bloque_listas(
        ws, LISTAS_AW, (('Origen del dato', ORIGEN_AW),), col='A')

    C.seccion(ws, 'A5', 'Qué Mide Esta Hoja')
    motor.val(ws, 'A6',
              'La actividad de agua (aw) va de 0 a 1 y dice cuánta agua del '
              'relleno está DISPONIBLE para que crezca algo. No es la humedad: '
              'un praliné puede tener grasa de sobra y aw bajísima. Las dos '
              'palancas que la bajan son el azúcar y el alcohol, y son las que '
              'explican por qué la misma pieza dura tres o cinco veces más '
              'según cómo la formules. Esta hoja no calcula la aw: la recoge, '
              'la compara con el umbral que tú te has puesto y te dice de qué '
              'va a morir cada referencia.', wrap=True)
    ws.merge_cells('A6:J6')
    ws['A6'].font = Font(italic=True, size=9)
    ws.row_dimensions[6].height = 56

    C.cabecera(ws, REF_CAB, (
        ('A', 'Id'), ('B', 'Referencia'), ('C', 'Familia de la carta'),
        ('D', 'Tipo de relleno'), ('E', 'aw'), ('F', 'Origen del dato'),
        ('G', 'Familia de vida útil del kit'),
        ('H', 'Plazo orientativo del kit'),
        ('I', 'De qué va a morir esta referencia'),
        ('J', 'Lo que dice el kit de esa familia')), altura=46)
    C.inmovilizar(ws, REF_CAB, col='C')

    for i, p in enumerate(FILAS):
        fila = REF_INI + i
        r = p['r']
        motor.val(ws, 'A%d' % fila, r['id'])
        motor.val(ws, 'B%d' % fila, r['nombre'], wrap=True)
        motor.val(ws, 'C%d' % fila, r['familia'])
        motor.val(ws, 'D%d' % fila, p['tipo'], wrap=True)
        X.entrada(ws, 'E%d' % fila, p['aw'], fmt=C.FMT_DEC,
                  etiqueta='Actividad de agua de ' + r['id'])
        X.entrada(ws, 'F%d' % fila, ORIGEN_AW[1],
                  etiqueta='Origen de la aw de ' + r['id'])
        motor.val(ws, 'G%d' % fila, r['familia_vida_util'], wrap=True)
        motor.val(ws, 'H%d' % fila, PLAZOS[r['familia_vida_util']][0])
        motor.f(ws, 'I%d' % fila,
                '=IF(ISNUMBER($E%d),IF($E%d>=%s,"Agua disponible ALTA: trátala '
                'como producto de vida corta y en frío, y justifícalo en tu '
                'APPCC","Agua disponible baja: la vida la manda el rancio de '
                'la grasa y la humedad del ambiente, no el microbio"),"")'
                % (fila, fila, A(P_AW)))
        motor.val(ws, 'J%d' % fila, PLAZOS[r['familia_vida_util']][1],
                  wrap=True)
        ws.row_dimensions[fila].height = 30

    C.dv_rango(ws, ['F%d' % (REF_INI + i) for i in range(len(FILAS))],
               listas['Origen del dato'], 'Origen no válido',
               'Sólo hay dos: la has medido con un higrómetro de actividad de '
               'agua o la has estimado. Ponerlo importa: una estimación no '
               'sostiene una vida útil delante de un inspector.')
    motor.semaforo_isnumber(ws, 'E%d:E%d' % (REF_INI, REF_FIN),
                            '$E%d' % REF_INI, operador='>=',
                            umbral=A(P_AW))

    motor.val(ws, 'A%d' % REF_TOT, 'RECUENTO', bold=True)
    motor.val(ws, 'B%d' % REF_TOT,
              'Referencias con el agua disponible por encima de tu umbral',
              bold=True, wrap=True)
    motor.f(ws, 'E%d' % REF_TOT,
            '=COUNTIF(E%d:E%d,">="&%s)' % (REF_INI, REF_FIN, A(P_AW)),
            fmt=C.FMT_ENT, bold=True)
    motor.val(ws, 'F%d' % REF_TOT, 'Medidas de verdad:', bold=True)
    motor.f(ws, 'G%d' % REF_TOT,
            '=COUNTIF(F%d:F%d,$A$%d)' % (REF_INI, REF_FIN, LISTAS_AW + 2),
            fmt=C.FMT_ENT, bold=True)
    motor.val(ws, 'I%d' % REF_TOT,
              'Mientras la segunda cifra sea cero, toda la columna de aw es '
              'una estimación: el higrómetro de actividad de agua es la compra '
              'que convierte esta hoja en un documento defendible.', wrap=True)
    ws.merge_cells('I%d:J%d' % (REF_TOT, REF_TOT))
    ws['I%d' % REF_TOT].font = Font(italic=True, size=9)
    ws.row_dimensions[REF_TOT].height = 34
    return ws


# --------------------------------------------------------------------------
# Hoja «Vida Útil Declarada»
# --------------------------------------------------------------------------
def hoja_vida_util(wb):
    ws = wb.create_sheet(H_VU)
    C.anchos(ws, {'A': 9, 'B': 44, 'C': 40, 'D': 15, 'E': 12, 'F': 12,
                  'G': 14, 'H': 18, 'I': 14, 'J': 15, 'K': 12, 'L': 16,
                  'M': 58})
    C.encabezar(ws, H_VU,
                'La vida útil la declaras TÚ y consta en tu plan de APPCC. '
                'Esta hoja NO la calcula: la recoge, la pone al lado del plazo '
                'orientativo del kit y te avisa si te has salido.', col_fin='M')
    C.pagina(ws, apaisado=True)

    listas, _f = C.bloque_listas(
        ws, LISTAS_VU, (('Tipo de fecha', TIPOS_FECHA),), col='A')

    C.seccion(ws, 'A5', 'La Tabla del Kit, Citada Fila a Fila')
    motor.val(ws, 'A6',
              'Los diez plazos de abajo son los del Kit de Tareas '
              'Chocolatería, fichero 02-partidas-produccion.xlsx, hoja '
              'Moldeado, tabla «vida útil y conservación orientativas a 15-18 '
              'grados C y 50-60 % de humedad». Son ORIENTATIVOS y de la casa, '
              'no de una norma: ninguna norma publica la vida útil del '
              'chocolate. La equivalencia en días de la columna E y F es '
              'aritmética nuestra -el kit escribe «4-8 semanas»- y está para '
              'que el semáforo pueda comparar.', wrap=True)
    ws.merge_cells('A6:M6')
    ws['A6'].font = Font(italic=True, size=9)
    ws.row_dimensions[6].height = 46

    C.cabecera(ws, REF_CAB, (
        ('A', 'Id'), ('B', 'Referencia'),
        ('C', 'Familia de vida útil del kit'),
        ('D', 'Plazo orientativo del kit'),
        ('E', 'Equivalencia mínima (días)'),
        ('F', 'Equivalencia máxima (días)'),
        ('G', 'Vida útil que TÚ declaras (días)'), ('H', 'Tipo de fecha'),
        ('I', 'Fecha de elaboración'), ('J', 'Fecha que va en la etiqueta'),
        ('K', 'Vida útil (semanas)'),
        ('L', 'Pieza más corta del surtido (días)'),
        ('M', 'Veredicto')), altura=52)
    C.inmovilizar(ws, REF_CAB, col='C')
    X.nota_celda(ws, 'G%d' % REF_CAB, 'CHN-30')
    X.nota_celda(ws, 'H%d' % REF_CAB, 'CHN-35')
    X.nota_celda(ws, 'J%d' % REF_CAB, 'CHN-36')

    for i, p in enumerate(FILAS):
        fila = REF_INI + i
        r = p['r']
        # A2: para una caja, el plazo del kit que se compara es el de la
        # pieza que MENOS aguanta dentro, no el de una familia fija.
        fam = familia_mas_restrictiva(r)
        motor.val(ws, 'A%d' % fila, r['id'])
        motor.val(ws, 'B%d' % fila, r['nombre'], wrap=True)
        motor.val(ws, 'C%d' % fila, fam, wrap=True)
        motor.val(ws, 'D%d' % fila, PLAZOS[fam][0])
        motor.val(ws, 'E%d' % fila, PLAZOS[fam][2], fmt=C.FMT_ENT)
        motor.val(ws, 'F%d' % fila, PLAZOS[fam][3], fmt=C.FMT_ENT)
        X.entrada(ws, 'G%d' % fila, p['vida'], fmt=C.FMT_ENT,
                  etiqueta='Vida útil declarada de ' + r['id'])
        X.entrada(ws, 'H%d' % fila,
                  TIPOS_FECHA[0] if p['vida'] > 30 else TIPOS_FECHA[1],
                  etiqueta='Tipo de fecha de ' + r['id'])
        X.entrada(ws, 'I%d' % fila, FECHA_ELABORACION, fmt=C.FMT_FECHA,
                  etiqueta='Fecha de elaboración de ' + r['id'])
        motor.f(ws, 'J%d' % fila, '=IFERROR($I%d+$G%d,"")' % (fila, fila),
                fmt=C.FMT_FECHA)
        motor.f(ws, 'K%d' % fila, '=IFERROR($G%d/7,"")' % fila, fmt=C.FMT_DEC1)
        if p['corta']:
            # A2: FÓRMULA, no constante — MIN de la «Vida útil que TÚ
            # declaras» (columna G) de cada pieza que compone la caja, así
            # que si el lector cambia G de una pieza, la caja se entera.
            refs_l = ['$G$%d' % FILA_DE_ID[cid] for cid, _n in r['composicion_caja']]
            motor.f(ws, 'L%d' % fila, '=MIN(%s)' % ','.join(refs_l),
                    fmt=C.FMT_ENT)
        motor.f(ws, 'M%d' % fila,
                '=IF(ISNUMBER($G{f}),IF(AND(ISNUMBER($L{f}),$G{f}>$L{f}),'
                '"Por encima de la pieza más corta que llevas dentro: un '
                'surtido caduca con ella",IF($G{f}>$F{f},"Por encima del plazo '
                'orientativo del kit: sostenlo con analítica y con tu APPCC",'
                'IF($G{f}<$E{f},"Por debajo del plazo del kit: conservador, y '
                'es decisión tuya","Dentro del plazo orientativo del kit"))),'
                '"")'.format(f=fila))
        ws.row_dimensions[fila].height = 28

    C.dv_rango(ws, ['H%d' % (REF_INI + i) for i in range(len(FILAS))],
               listas['Tipo de fecha'], 'Tipo de fecha no válido',
               'Consumo preferente o caducidad. No son intercambiables: la de '
               'caducidad es la que convierte el producto en no seguro cuando '
               'pasa, y en bombonería la lleva lo que se va a frío.')

    motor.val(ws, 'A%d' % REF_TOT, 'RECUENTO', bold=True)
    motor.val(ws, 'B%d' % REF_TOT,
              'Referencias con fecha de CADUCIDAD (las demás, de consumo '
              'preferente)', bold=True, wrap=True)
    motor.f(ws, 'H%d' % REF_TOT,
            '=COUNTIF(H%d:H%d,$A$%d)' % (REF_INI, REF_FIN, LISTAS_VU + 3),
            fmt=C.FMT_ENT, bold=True)
    motor.f(ws, 'G%d' % REF_TOT,
            '=IFERROR(MIN(G%d:G%d),"")' % (REF_INI, REF_FIN), fmt=C.FMT_ENT,
            bold=True)
    motor.val(ws, 'K%d' % REF_TOT, 'La más corta de la carta (días)',
              wrap=True)
    ws.merge_cells('K%d:M%d' % (REF_TOT, REF_TOT))
    ws['K%d' % REF_TOT].font = Font(italic=True, size=9)

    fila = REF_TOT + 2
    C.seccion(ws, 'A%d' % fila, 'Las Diez Filas del Kit, Tal Como Están')
    fila += 1
    C.cabecera(ws, fila, (('A', 'Familia'), ('D', 'Plazo'),
                          ('F', 'Lo que dice el kit')), altura=24)
    global KIT_INI
    KIT_INI = fila + 1
    for j, (fam, plazo, nota) in enumerate(D.VIDA_UTIL_KIT):
        f2 = KIT_INI + j
        motor.val(ws, 'A%d' % f2, fam, wrap=True)
        ws.merge_cells('A%d:C%d' % (f2, f2))
        motor.val(ws, 'D%d' % f2, plazo)
        ws.merge_cells('D%d:E%d' % (f2, f2))
        motor.val(ws, 'F%d' % f2, nota, wrap=True)
        ws.merge_cells('F%d:M%d' % (f2, f2))
        ws['F%d' % f2].font = Font(size=9)
        ws.row_dimensions[f2].height = 28
    f2 = KIT_INI + len(D.VIDA_UTIL_KIT)
    motor.val(ws, 'A%d' % f2,
              'Fuente: ' + D.FUENTE_VIDA_UTIL + '. La última fila no es un '
              'plazo: es una prohibición. El chocolate acabado NO se congela; '
              'al descongelar condensa, el agua disuelve el azúcar de la '
              'superficie y deja velo. Sólo el granel de ganache admite frío '
              'negativo, y con condiciones.', wrap=True)
    ws.merge_cells('A%d:M%d' % (f2, f2))
    ws['A%d' % f2].font = Font(italic=True, size=9)
    ws.row_dimensions[f2].height = 34
    X.nota_celda(ws, 'A%d' % f2, 'CHN-38')
    return ws


# --------------------------------------------------------------------------
# Hoja «Etiquetado o Granel» (D47)
# --------------------------------------------------------------------------
def hoja_etiquetado(wb):
    ws = wb.create_sheet(H_ETQ)
    C.anchos(ws, {'A': 9, 'B': 44, 'C': 22, 'D': 60, 'E': 60, 'F': 46,
                  'G': 46, 'H': 16, 'I': 46})
    C.encabezar(ws, H_ETQ,
                'No son dos formas de decir lo mismo: son dos regímenes. Elige '
                'la vía de cada referencia y la hoja cambia de COLUMNA, no de '
                'matiz.', col_fin='I')
    C.pagina(ws, apaisado=True)

    C.seccion(ws, 'A5', 'Las Dos Vías')
    C.cabecera(ws, 6, (('A', 'Vía'), ('B', 'Qué significa'),
                       ('F', 'La referencia que te toca')), altura=24)
    for i, via in enumerate(D.VIAS_DESPACHO):
        fila = VIAS_INI + i
        motor.val(ws, 'A%d' % fila, via, bold=True)
        motor.val(ws, 'B%d' % fila, D.VIAS_DESPACHO_TEXTO[via], wrap=True)
        ws.merge_cells('B%d:E%d' % (fila, fila))
        ws['B%d' % fila].font = Font(size=9)
        ws.row_dimensions[fila].height = 76
    ws.merge_cells('F%d:I%d' % (VIAS_INI, VIAS_INI))
    motor.val(ws, 'F%d' % VIAS_INI,
              'Art. 4.2 del RD 1021/2022: la temperatura de conservación que '
              'TÚ has puesto en la etiqueta te obliga a ti.', wrap=True)
    ws['F%d' % VIAS_INI].font = Font(size=9)
    ws.merge_cells('F%d:I%d' % (VIAS_FIN, VIAS_FIN))
    motor.val(ws, 'F%d' % VIAS_FIN,
              'Tu plan de APPCC: la temperatura y la vida útil las declaras tú '
              'y tienen que constar en él.', wrap=True)
    ws['F%d' % VIAS_FIN].font = Font(size=9)
    X.nota_celda(ws, 'F%d' % VIAS_INI, 'CHN-87')
    X.nota_celda(ws, 'F%d' % VIAS_FIN, 'CHN-30')
    X.nota_celda(ws, 'A%d' % VIAS_FIN, 'CHN-89')

    motor.val(ws, 'A10',
              'Y una frontera que conviene tener clara: el RD 1021/2022 no '
              'nombra el chocolate ni una sola vez, pero una tarta de '
              'chocolate SÍ entra en su tabla de comidas preparadas. Si además '
              'de bombones vendes pastelería con nata o crema, esa parte del '
              'mostrador va por otro régimen.', wrap=True)
    ws.merge_cells('A10:I10')
    ws['A10'].font = Font(italic=True, size=9)
    ws.row_dimensions[10].height = 34
    X.nota_celda(ws, 'A10', 'CHN-30b')

    listas, _f = C.bloque_listas(
        ws, LISTAS_ETQ, (('Vías de despacho', D.VIAS_DESPACHO),), col='A')

    C.seccion(ws, 'A13', 'Vía de Cada Referencia')
    C.cabecera(ws, REF_CAB, (
        ('A', 'Id'), ('B', 'Referencia'), ('C', '¿Cómo la despachas?'),
        ('D', 'Si va ENVASADA CON ETIQUETA, esto te obliga'),
        ('E', 'Si va A GRANEL, esto tiene que constar'),
        ('F', 'La referencia normativa que te toca'),
        ('G', '¿Tiene que llevar lote?'),
        ('H', 'Fecha que va en la etiqueta'),
        ('I', 'Cómo se informan los alérgenos')), altura=52)
    C.inmovilizar(ws, REF_CAB, col='C')
    X.nota_celda(ws, 'G%d' % REF_CAB, 'CHN-36')
    X.nota_celda(ws, 'I%d' % REF_CAB, 'CHN-33')

    for i, p in enumerate(FILAS):
        fila = REF_INI + i
        r = p['r']
        motor.val(ws, 'A%d' % fila, r['id'])
        motor.val(ws, 'B%d' % fila, r['nombre'], wrap=True)
        X.entrada(ws, 'C%d' % fila, r['via'],
                  etiqueta='Vía de despacho de ' + r['id'])
        motor.f(ws, 'D%d' % fila,
                '=IF($C%d=$A$%d,$B$%d,"")' % (fila, VIAS_INI, VIAS_INI))
        motor.f(ws, 'E%d' % fila,
                '=IF($C%d=$A$%d,$B$%d,"")' % (fila, VIAS_FIN, VIAS_FIN))
        motor.f(ws, 'F%d' % fila,
                '=IF($C%d=$A$%d,$F$%d,IF($C%d=$A$%d,$F$%d,""))'
                % (fila, VIAS_INI, VIAS_INI, fila, VIAS_FIN, VIAS_FIN))
        motor.f(ws, 'G%d' % fila,
                '=IF($C%d=$A$%d,"Sí, y no viene del Rgto. 1169/2011 sino del '
                'RD 1808/1991: la letra L delante salvo que el lote sea la '
                'propia fecha","Comprueba las tres exenciones del RD '
                '1808/1991; si ninguna te vale, también")'
                % (fila, VIAS_INI))
        motor.f(ws, 'H%d' % fila, '=%sJ%d' % (QVU, fila), fmt=C.FMT_FECHA)
        motor.f(ws, 'I%d' % fila,
                '=IF($C%d=$A$%d,"En la lista de ingredientes y destacados '
                'tipográficamente","Pueden ir en un cartel visible en el punto '
                'de venta; la FECHA no puede")' % (fila, VIAS_INI))
        ws.row_dimensions[fila].height = 30

    C.dv_rango(ws, ['C%d' % (REF_INI + i) for i in range(len(FILAS))],
               listas['Vías de despacho'], 'Vía no válida',
               'Sólo hay dos: envasado con etiqueta o a granel. Y no son el '
               'mismo régimen: elige la que de verdad usas en mostrador.')

    motor.val(ws, 'A%d' % REF_TOT, 'RECUENTO', bold=True)
    motor.val(ws, 'B%d' % REF_TOT, 'Referencias envasadas con etiqueta',
              bold=True, wrap=True)
    motor.f(ws, 'C%d' % REF_TOT,
            '=COUNTIF(C%d:C%d,$A$%d)' % (REF_INI, REF_FIN, LISTAS_ETQ + 2),
            fmt=C.FMT_ENT, bold=True)
    motor.val(ws, 'D%d' % REF_TOT, 'Referencias a granel', bold=True)
    motor.f(ws, 'E%d' % REF_TOT,
            '=COUNTIF(C%d:C%d,$A$%d)' % (REF_INI, REF_FIN, LISTAS_ETQ + 3),
            fmt=C.FMT_ENT, bold=True)
    motor.val(ws, 'F%d' % REF_TOT,
              'Cada referencia que pasa de granel a envasada te añade doce '
              'menciones obligatorias y el lote. No es una decisión de '
              'etiquetado: es una decisión de canal.', wrap=True)
    ws.merge_cells('F%d:I%d' % (REF_TOT, REF_TOT))
    ws['F%d' % REF_TOT].font = Font(italic=True, size=9)
    ws.row_dimensions[REF_TOT].height = 34
    X.nota_celda(ws, 'F%d' % REF_TOT, 'CHN-35')
    return ws


# --------------------------------------------------------------------------
# Hoja «Temperatura y Vitrina» (D31)
# --------------------------------------------------------------------------
def hoja_temperatura(wb):
    ws = wb.create_sheet(H_TMP)
    C.anchos(ws, {'A': 9, 'B': 44, 'C': 22, 'D': 16, 'E': 30, 'F': 46,
                  'G': 46, 'H': 54, 'I': 20, 'J': 20})
    C.encabezar(ws, H_TMP,
                'Las cinco temperaturas del kit, el rango de trabajo de TU '
                'vitrina y la que declaras para cada referencia. El semáforo '
                'sólo se enciende por encima de 20' + N + 'grados C.',
                col_fin='J')
    C.pagina(ws, apaisado=True)

    C.seccion(ws, 'A5', 'Las Cinco Temperaturas del Kit')
    C.cabecera(ws, CLIMA_CAB, (
        ('A', 'Zona'), ('C', 'Temperatura objetivo'), ('D', 'Humedad'),
        ('E', 'De dónde sale'), ('F', 'Literal del kit')), altura=24)
    for i, clave in enumerate(CLIMA_ORDEN):
        fila = CLIMA_INI + i
        z = D.CLIMA[clave]
        motor.val(ws, 'A%d' % fila, z['concepto'], wrap=True)
        ws.merge_cells('A%d:B%d' % (fila, fila))
        motor.val(ws, 'C%d' % fila, '%g a %g%sgrados C'
                  % (z['t_min'], z['t_max'], N))
        if z['hr_max'] is None:
            motor.val(ws, 'D%d' % fila, 'no la fija')
        elif z['hr_min'] is None:
            motor.val(ws, 'D%d' % fila, 'menos del %g %%' % z['hr_max'])
        else:
            motor.val(ws, 'D%d' % fila, '%g a %g %%' % (z['hr_min'],
                                                        z['hr_max']))
        motor.val(ws, 'E%d' % fila, z['fuente'], wrap=True)
        motor.val(ws, 'F%d' % fila, z['literal'], wrap=True)
        ws.merge_cells('F%d:J%d' % (fila, fila))
        ws['F%d' % fila].font = Font(size=9)
        ws.row_dimensions[fila].height = 28

    motor.val(ws, 'A%d' % (CLIMA_FIN + 1),
              'Confundir la temperatura de la SALA con la de la CÁMARA es uno '
              'de los errores que más caro salen: son dos cosas distintas y '
              'conviven en el mismo local. Y la nevera de 0-4 grados C es la '
              'del RELLENO, no la del bombón acabado: el chocolate terminado '
              'no va a esa temperatura, condensa.', wrap=True)
    ws.merge_cells('A%d:J%d' % (CLIMA_FIN + 1, CLIMA_FIN + 1))
    ws['A%d' % (CLIMA_FIN + 1)].font = Font(italic=True, size=9)
    ws.row_dimensions[CLIMA_FIN + 1].height = 30

    C.seccion(ws, 'A13', 'Tu Vitrina')
    C.cabecera(ws, VIT_CAB, (('A', 'Dato'), ('D', 'Valor'), ('E', 'Unidad'),
                             ('F', 'Qué dice el libro')), altura=24)
    for fila, etiqueta, valor, fmt, unidad in (
        (VIT_TMIN, 'Temperatura mínima de trabajo de tu vitrina',
         VITRINA_TMIN, C.FMT_DEC1, 'grados C'),
        (VIT_TMAX, 'Temperatura máxima de trabajo de tu vitrina',
         VITRINA_TMAX, C.FMT_DEC1, 'grados C'),
        (VIT_HR, 'Humedad de trabajo de tu vitrina', VITRINA_HR, C.FMT_DEC1,
         '% de HR'),
    ):
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
        ws.merge_cells('A%d:C%d' % (fila, fila))
        X.entrada(ws, 'D%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
        motor.val(ws, 'E%d' % fila, unidad)
    motor.val(ws, 'A%d' % VIT_UMB, 'Temperatura a la que salta la alarma',
              wrap=True)
    ws.merge_cells('A%d:C%d' % (VIT_UMB, VIT_UMB))
    motor.f(ws, 'D%d' % VIT_UMB, '=%s' % A(P_TALARMA), fmt=C.FMT_DEC1)
    motor.val(ws, 'E%d' % VIT_UMB, 'grados C')

    motor.f(ws, 'F%d' % VIT_TMIN,
            '=IF(AND(ISNUMBER($D%d),ISNUMBER($D%d)),IF($D%d>$D%d,"Revisa: el '
            'mínimo está por encima del máximo","Rango correcto"),"")'
            % (VIT_TMIN, VIT_TMAX, VIT_TMIN, VIT_TMAX))
    motor.f(ws, 'F%d' % VIT_TMAX,
            '=IF(AND(ISNUMBER($D%d),ISNUMBER($D%d)),IF($D%d>$D%d,"Por encima '
            'de la alarma: a esa temperatura la manteca de cacao empieza a '
            'fundir y el género se pierde","Dentro de lo que aguanta el '
            'chocolate"),"")' % (VIT_TMAX, VIT_UMB, VIT_TMAX, VIT_UMB))
    motor.f(ws, 'F%d' % VIT_HR,
            '=IF(AND(ISNUMBER($D%d),ISNUMBER(%s)),IF($D%d>%s,"Por encima del '
            'objetivo del kit: el bombón coge humedad y sale velo de azúcar",'
            '"Dentro del objetivo del kit"),"")'
            % (VIT_HR, A(P_HRMAX), VIT_HR, A(P_HRMAX)))
    for fila, umbral in ((VIT_TMAX, A(P_TALARMA)), (VIT_HR, A(P_HRMAX))):
        motor.semaforo_isnumber(ws, 'D%d' % fila, '$D$%d' % fila,
                                operador='>', umbral=umbral)
    motor.val(ws, 'H%d' % VIT_TMIN,
              'El objetivo operativo del kit para la vitrina es 16-18 grados '
              'C con menos del 55 % de humedad, y es lo que viene puesto. El '
              'RANGO DE TRABAJO del equipo es otra cosa: una vitrina de '
              'bombonería real trabaja, por ejemplo, entre +14 y +17 grados C. '
              'Pon el de la tuya, que viene en su ficha técnica. El semáforo '
              'no se enciende por estar en 16-18: sólo por pasar de 20.',
              wrap=True)
    ws.merge_cells('H%d:J%d' % (VIT_TMIN, VIT_HR))
    ws['H%d' % VIT_TMIN].font = Font(italic=True, size=9)

    C.seccion(ws, 'A20', 'Temperatura Declarada de Cada Referencia')
    C.cabecera(ws, TMP_CAB, (
        ('A', 'Id'), ('B', 'Referencia'), ('C', '¿Cómo la despachas?'),
        ('D', 'Temperatura que TÚ declaras'), ('E', 'Dónde va'),
        ('F', '¿La mantiene tu vitrina?'), ('G', 'Aviso'),
        ('H', 'Qué tiene que constar'), ('I', 'aw'),
        ('J', 'Vida útil (días)')), altura=52)
    C.inmovilizar(ws, TMP_CAB, col='C')
    X.nota_celda(ws, 'D%d' % TMP_CAB, 'CHN-30')
    X.nota_celda(ws, 'H%d' % TMP_CAB, 'CHN-87')

    for i, p in enumerate(FILAS):
        fila = TMP_INI + i
        ref = REF_INI + i
        r = p['r']
        motor.val(ws, 'A%d' % fila, r['id'])
        motor.val(ws, 'B%d' % fila, r['nombre'], wrap=True)
        motor.f(ws, 'C%d' % fila, '=%sC%d' % (QETQ, ref))
        X.entrada(ws, 'D%d' % fila, p['temp'], fmt=C.FMT_DEC1,
                  etiqueta='Temperatura declarada de ' + r['id'])
        motor.f(ws, 'E%d' % fila,
                '=IF(ISNUMBER($D%d),IF($D%d<$D$%d,"Nevera de rellenos, no '
                'vitrina","Vitrina temperada"),"")'
                % (fila, fila, VIT_TMIN))
        motor.f(ws, 'F%d' % fila,
                '=IF(AND(ISNUMBER($D%d),ISNUMBER($D$%d),ISNUMBER($D$%d)),'
                'IF(AND($D%d>=$D$%d,$D%d<=$D$%d),"Sí, está dentro del rango de '
                'tu vitrina","No con esta vitrina: o cambias la temperatura '
                'declarada o necesitas otro mueble"),"")'
                % (fila, VIT_TMIN, VIT_TMAX, fila, VIT_TMIN, fila, VIT_TMAX))
        motor.f(ws, 'G%d' % fila,
                '=IF(ISNUMBER($D%d),IF($D%d>%s,"Por encima de la alarma: a esa '
                'temperatura la manteca de cacao funde",""),"")'
                % (fila, fila, A(P_TALARMA)))
        motor.f(ws, 'H%d' % fila,
                '=IF($C%d=%sA$%d,"En la etiqueta, y esa temperatura te obliga '
                'a ti","En tu plan de APPCC, con el registro diario que lo '
                'demuestre")' % (fila, QETQ, VIAS_INI))
        motor.f(ws, 'I%d' % fila, '=%sE%d' % (QAW, ref), fmt=C.FMT_DEC)
        motor.f(ws, 'J%d' % fila, '=%sG%d' % (QVU, ref), fmt=C.FMT_ENT)
        ws.row_dimensions[fila].height = 28

    motor.semaforo_isnumber(ws, 'D%d:D%d' % (TMP_INI, TMP_FIN),
                            '$D%d' % TMP_INI, operador='>',
                            umbral=A(P_TALARMA))

    motor.val(ws, 'A%d' % TMP_TOT, 'RECUENTO', bold=True)
    motor.val(ws, 'B%d' % TMP_TOT,
              'Referencias por encima de la alarma de 20 grados C', bold=True,
              wrap=True)
    motor.f(ws, 'D%d' % TMP_TOT,
            '=COUNTIF(D%d:D%d,">"&%s)' % (TMP_INI, TMP_FIN, A(P_TALARMA)),
            fmt=C.FMT_ENT, bold=True)
    motor.val(ws, 'E%d' % TMP_TOT, 'Referencias que van a nevera', bold=True,
              wrap=True)
    motor.f(ws, 'F%d' % TMP_TOT,
            '=COUNTIF(D%d:D%d,"<"&$D$%d)' % (TMP_INI, TMP_FIN, VIT_TMIN),
            fmt=C.FMT_ENT, bold=True)
    return ws


# --------------------------------------------------------------------------
# Hoja «Lote y Merma por Caducidad»
# --------------------------------------------------------------------------
def hoja_lote(wb):
    ws = wb.create_sheet(H_LOT)
    C.anchos(ws, {'A': 9, 'B': 44, 'C': 13, 'D': 13, 'E': 13, 'F': 12,
                  'G': 12, 'H': 15, 'I': 14, 'J': 14, 'K': 14, 'L': 15,
                  'M': 15, 'N': 14, 'O': 13, 'P': 14, 'Q': 14, 'R': 50})
    C.encabezar(ws, H_LOT,
                'El coste de arrancar una tanda empuja a hacerlas grandes; la '
                'caducidad las frena. Esta hoja pone las dos fuerzas juntas y '
                'te dice lo que se va a la basura cada año.', col_fin='R')
    C.pagina(ws, apaisado=True)

    motor.val(ws, 'A5',
              'El modelo es deliberadamente simple y conviene saberlo: supone '
              'que produces tandas completas del tamaño que pones en la '
              'columna E y que no ajustas sobre la marcha. Lo que no vendas '
              'dentro de la vida útil declarada, se pierde. Si tú escalonas la '
              'producción, tu merma real será menor -y ésa es justamente la '
              'conclusión-.', wrap=True)
    ws.merge_cells('A5:R5')
    ws['A5'].font = Font(italic=True, size=9)
    ws.row_dimensions[5].height = 34

    C.seccion(ws, 'A13', 'Tamaño de Tanda y Merma por Caducidad')
    C.cabecera(ws, REF_CAB, (
        ('A', 'Id'), ('B', 'Referencia'), ('C', 'Ventas a la semana (uds)'),
        ('D', 'Demanda al año (uds)'), ('E', 'Tamaño de tanda actual (uds)'),
        ('F', 'Vida útil declarada (días)'), ('G', 'Vida útil (semanas)'),
        ('H', 'Lo que vendes dentro de la vida útil (uds)'),
        ('I', 'Coste de materia por pieza (€)'),
        ('J', 'Coste de tenerla parada un año (€)'),
        ('K', 'Tanda económica teórica (uds)'),
        ('L', 'Tanda máxima que permite la caducidad (uds)'),
        ('M', 'Tanda recomendada (uds)'),
        ('N', 'Piezas que caducan por tanda'), ('O', 'Tandas al año'),
        ('P', 'Piezas caducadas al año'),
        ('Q', 'Merma por caducidad (€/año)'), ('R', 'Veredicto')), altura=58)
    C.inmovilizar(ws, REF_CAB, col='C')

    for i, p in enumerate(FILAS):
        fila = REF_INI + i
        r = p['r']
        motor.val(ws, 'A%d' % fila, r['id'])
        motor.val(ws, 'B%d' % fila, r['nombre'], wrap=True)
        X.entrada(ws, 'C%d' % fila, p['ventas'], fmt=C.FMT_DEC1,
                  etiqueta='Ventas semanales de ' + r['id'])
        motor.f(ws, 'D%d' % fila, '=IFERROR($C%d*%s,"")' % (fila, A(P_SEM)),
                fmt=C.FMT_ENT)
        X.entrada(ws, 'E%d' % fila, p['lote'], fmt=C.FMT_ENT,
                  etiqueta='Tamaño de tanda de ' + r['id'])
        motor.f(ws, 'F%d' % fila, '=%sG%d' % (QVU, fila), fmt=C.FMT_ENT)
        motor.f(ws, 'G%d' % fila, '=IFERROR($F%d/7,"")' % fila, fmt=C.FMT_DEC1)
        motor.f(ws, 'H%d' % fila, '=IFERROR($C%d*$G%d,"")' % (fila, fila),
                fmt=C.FMT_ENT)
        X.entrada(ws, 'I%d' % fila, p['coste'], fmt=C.FMT_DEC,
                  etiqueta='Coste de materia por pieza de ' + r['id'])
        motor.f(ws, 'J%d' % fila, '=IFERROR($I%d*%s,"")' % (fila, A(P_MANT)),
                fmt=C.FMT_DEC)
        motor.f(ws, 'K%d' % fila,
                '=IFERROR(SQRT(2*$D%d*%s/$J%d),"")' % (fila, A(P_LANZA), fila),
                fmt=C.FMT_ENT)
        motor.f(ws, 'L%d' % fila, '=IFERROR($H%d,"")' % fila, fmt=C.FMT_ENT)
        motor.f(ws, 'M%d' % fila, '=IFERROR(MIN($K%d,$L%d),"")' % (fila, fila),
                fmt=C.FMT_ENT)
        motor.f(ws, 'N%d' % fila,
                '=IFERROR(MAX(0,$E%d-$H%d),"")' % (fila, fila), fmt=C.FMT_ENT)
        motor.f(ws, 'O%d' % fila, '=IFERROR($D%d/$E%d,"")' % (fila, fila),
                fmt=C.FMT_DEC1)
        motor.f(ws, 'P%d' % fila, '=IFERROR($N%d*$O%d,"")' % (fila, fila),
                fmt=C.FMT_ENT)
        motor.f(ws, 'Q%d' % fila, '=IFERROR($P%d*$I%d,"")' % (fila, fila),
                fmt=C.FMT_EUR)
        motor.f(ws, 'R%d' % fila,
                '=IF(ISNUMBER($Q{f}),IF($Q{f}>{u},"Tanda demasiado grande para '
                'lo que dura: baja a la tanda recomendada",IF($N{f}>0,"Se te '
                'queda algo en cada tanda, pero es asumible","La tanda cabe '
                'entera dentro de la vida útil")),"")'.format(
                    f=fila, u=A(P_UMBMERMA)))
        ws.row_dimensions[fila].height = 28

    motor.semaforo_isnumber(ws, 'Q%d:Q%d' % (REF_INI, REF_FIN),
                            '$Q%d' % REF_INI, operador='>',
                            umbral=A(P_UMBMERMA))

    motor.val(ws, 'A%d' % REF_TOT, 'TOTAL', bold=True)
    motor.val(ws, 'B%d' % REF_TOT, 'Las %d referencias de la carta'
              % len(D.CARTA), bold=True)
    motor.f(ws, 'D%d' % REF_TOT, '=SUM(D%d:D%d)' % (REF_INI, REF_FIN),
            fmt=C.FMT_ENT, bold=True)
    motor.f(ws, 'P%d' % REF_TOT, '=SUM(P%d:P%d)' % (REF_INI, REF_FIN),
            fmt=C.FMT_ENT, bold=True)
    motor.f(ws, 'Q%d' % REF_TOT, '=SUM(Q%d:Q%d)' % (REF_INI, REF_FIN),
            fmt=C.FMT_EUR, bold=True)

    fila = REF_TOT + 2
    motor.val(ws, 'A%d' % fila,
              'Referencias con la tanda demasiado grande para lo que duran',
              wrap=True)
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.f(ws, 'D%d' % fila,
            '=COUNTIF($Q$%d:$Q$%d,">"&%s)' % (REF_INI, REF_FIN, A(P_UMBMERMA)),
            fmt=C.FMT_ENT)
    motor.val(ws, 'F%d' % fila,
              'Cada una de ellas es dinero que ya has pagado -cobertura, '
              'relleno y horas de obrador- y que va a acabar en la basura. Se '
              'arregla sin comprar nada: bajando la tanda y repitiéndola más a '
              'menudo.', wrap=True)
    ws.merge_cells('F%d:R%d' % (fila, fila))
    ws['F%d' % fila].font = Font(italic=True, size=9)
    ws.row_dimensions[fila].height = 30

    fila += 1
    motor.val(ws, 'A%d' % fila,
              'Merma por caducidad sobre el coste de materia del año',
              wrap=True)
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.f(ws, 'D%d' % fila,
            '=IFERROR($Q$%d/SUMPRODUCT($I$%d:$I$%d,$D$%d:$D$%d),"")'
            % (REF_TOT, REF_INI, REF_FIN, REF_INI, REF_FIN), fmt=C.FMT_PCT)

    fila += 1
    motor.val(ws, 'A%d' % fila,
              'Las dos ganaches: lo que cuesta al año la formulación fresca '
              'frente a la estabilizada', wrap=True)
    ws.merge_cells('A%d:C%d' % (fila, fila))
    f_bc1 = REF_INI + [p['r']['id'] for p in FILAS].index('BC1')
    f_bc2 = REF_INI + [p['r']['id'] for p in FILAS].index('BC2')
    motor.f(ws, 'D%d' % fila, '=IFERROR($Q%d-$Q%d,"")' % (f_bc1, f_bc2),
            fmt=C.FMT_EUR)
    motor.val(ws, 'F%d' % fila,
              'La misma pieza con dos formulaciones: la de nata fresca dura '
              '10-15 días y la estabilizada 4-8 semanas. La diferencia de '
              'merma al año es esta cifra, y es una decisión de modelo de '
              'negocio -no una decisión técnica-.', wrap=True)
    ws.merge_cells('F%d:R%d' % (fila, fila))
    ws['F%d' % fila].font = Font(italic=True, size=9)
    ws.row_dimensions[fila].height = 30
    return ws


# --------------------------------------------------------------------------
# Mapa de celdas citables
# --------------------------------------------------------------------------
def mapa_celdas():
    idx = [p['r']['id'] for p in FILAS]
    f_bc1 = REF_INI + idx.index('BC1')
    f_bc2 = REF_INI + idx.index('BC2')
    f_cj1 = REF_INI + idx.index('CJ1')
    f_tb1 = REF_INI + idx.index('TB1')
    t_bc1 = TMP_INI + idx.index('BC1')

    m = [
        ('Umbral de vigilancia de actividad de agua', H_PAR, P_AW, 'parametro'),
        ('Temperatura a la que salta la alarma de la vitrina', H_PAR,
         P_TALARMA, 'parametro'),
        ('Humedad máxima de trabajo de la vitrina', H_PAR, P_HRMAX,
         'parametro'),
        ('Coste de poner en marcha una tanda', H_PAR, P_LANZA, 'parametro'),
        ('Coste de tener una pieza parada un año', H_PAR, P_MANT, 'parametro'),
        ('Merma por caducidad que dispara el aviso', H_PAR, P_UMBMERMA,
         'parametro'),
        ('Piezas vendibles al año', H_PAR, P_PZANO, 'salida'),
        ('Referencias con el agua disponible por encima del umbral', H_AW,
         'E%d' % REF_TOT, 'salida'),
        ('Actividades de agua medidas de verdad', H_AW, 'G%d' % REF_TOT,
         'salida'),
        ('Actividad de agua de la ganache de nata fresca', H_AW,
         'E%d' % f_bc1, 'entrada'),
        ('Actividad de agua de la ganache estabilizada', H_AW, 'E%d' % f_bc2,
         'entrada'),
        ('Vida útil declarada de la ganache de nata fresca', H_VU,
         'G%d' % f_bc1, 'entrada'),
        ('Vida útil declarada de la ganache estabilizada', H_VU,
         'G%d' % f_bc2, 'entrada'),
        ('Vida útil declarada de la caja surtida de 12', H_VU, 'G%d' % f_cj1,
         'entrada'),
        ('Pieza más corta que lleva dentro la caja surtida de 12', H_VU,
         'L%d' % f_cj1, 'salida'),
        ('Fecha que va en la etiqueta de la ganache de nata fresca', H_VU,
         'J%d' % f_bc1, 'salida'),
        ('Vida útil más corta de toda la carta (días)', H_VU, 'G%d' % REF_TOT,
         'salida'),
        ('Referencias con fecha de caducidad', H_VU, 'H%d' % REF_TOT,
         'salida'),
        ('Referencias envasadas con etiqueta', H_ETQ, 'C%d' % REF_TOT,
         'salida'),
        ('Referencias que se despachan a granel', H_ETQ, 'E%d' % REF_TOT,
         'salida'),
        ('La referencia normativa que le toca a un bombón a granel', H_ETQ,
         'F%d' % f_bc1, 'salida'),
        ('La referencia normativa que le toca a una caja envasada', H_ETQ,
         'F%d' % f_cj1, 'salida'),
        ('Temperatura mínima de trabajo de la vitrina del ejemplo', H_TMP,
         'D%d' % VIT_TMIN, 'entrada'),
        ('Temperatura máxima de trabajo de la vitrina del ejemplo', H_TMP,
         'D%d' % VIT_TMAX, 'entrada'),
        ('Veredicto de la vitrina del ejemplo', H_TMP, 'F%d' % VIT_TMAX,
         'salida'),
        ('Referencias por encima de la alarma de la vitrina', H_TMP,
         'D%d' % TMP_TOT, 'salida'),
        ('Referencias que van a nevera y no a vitrina', H_TMP,
         'F%d' % TMP_TOT, 'salida'),
        ('Temperatura declarada de la ganache de nata fresca', H_TMP,
         'D%d' % t_bc1, 'entrada'),
        ('Tanda actual de la ganache de nata fresca', H_LOT, 'E%d' % f_bc1,
         'entrada'),
        ('Lo que vendes de ganache fresca dentro de su vida útil', H_LOT,
         'H%d' % f_bc1, 'salida'),
        ('Tanda recomendada de la ganache de nata fresca', H_LOT,
         'M%d' % f_bc1, 'salida'),
        ('Tanda recomendada de la ganache estabilizada', H_LOT, 'M%d' % f_bc2,
         'salida'),
        ('Merma por caducidad de la ganache de nata fresca', H_LOT,
         'Q%d' % f_bc1, 'salida'),
        ('Merma por caducidad de la ganache estabilizada', H_LOT,
         'Q%d' % f_bc2, 'salida'),
        ('Merma por caducidad de la tableta de origen', H_LOT, 'Q%d' % f_tb1,
         'salida'),
        ('Piezas que se caducan al año en toda la carta', H_LOT,
         'P%d' % REF_TOT, 'salida'),
        ('Merma por caducidad de toda la carta', H_LOT, 'Q%d' % REF_TOT,
         'salida'),
        ('Referencias con la tanda demasiado grande para lo que duran', H_LOT,
         'D%d' % (REF_TOT + 2), 'salida'),
        ('Merma por caducidad sobre el coste de materia del año', H_LOT,
         'D%d' % (REF_TOT + 3), 'salida'),
        ('Lo que cuesta al año la ganache fresca frente a la estabilizada',
         H_LOT, 'D%d' % (REF_TOT + 4), 'salida'),
    ]
    return m


NOTAS_MAPA = (
    'La vida útil NO la calcula este libro: la declara el operador en su plan '
    'de APPCC (`CHN-30`), y aquí es celda verde con un valor de partida '
    'declarado como supuesto -el extremo bajo del plazo orientativo del kit-. '
    'Los diez plazos por familia son los del Kit de Tareas Chocolatería '
    '(' + D.FUENTE_VIDA_UTIL + '), CITADOS y no reescritos (D30); la '
    'equivalencia en días es aritmética nuestra y así se dice en la hoja. El '
    'semáforo de la vitrina sólo avisa por encima de '
    + ('%g' % D.VITRINA_UMBRAL_ALARMA_C) + N + 'grados C y NUNCA pone en rojo '
    'los 16-18 grados C que el propio kit publica como objetivo (D31). '
    'Etiquetado y granel no son el mismo régimen (D47): el art. 4.2 del RD '
    '1021/2022 se aplica a la referencia que sale ENVASADA con su etiqueta; a '
    'granel la referencia es tu sistema de autocontrol, y `CHN-87` lo sostiene '
    '-«chocolate», «cacao», «bombón» y «confitería» aparecen 0 veces en todo '
    'el RD 1021/2022-. El coste de materia por pieza de la hoja «' + H_LOT
    + '» entra por celda verde: el precio de la cobertura vive en el libro 3 y '
    'el escandallo en el libro 4, y aquí no hay ninguna fórmula que nombre '
    'otro fichero.'
)


# --------------------------------------------------------------------------
# Demostraciones con pycel
# --------------------------------------------------------------------------
def demo(ruta):
    from pycel import ExcelCompiler
    ok, fallos = [], []
    idx = [p['r']['id'] for p in FILAS]
    f_bc1 = REF_INI + idx.index('BC1')
    f_bc2 = REF_INI + idx.index('BC2')
    f_cj1 = REF_INI + idx.index('CJ1')

    def prueba(nombre, cond, detalle=''):
        (ok if cond else fallos).append(
            nombre + (' — ' + detalle if detalle else ''))

    exc = ExcelCompiler(ruta)

    def v(hoja, coord):
        return exc.evaluate("'%s'!%s" % (hoja, coord))

    # 1. La fecha de la etiqueta es la de elaboración más la vida útil que TÚ
    #    has declarado: el libro no la calcula por su cuenta.
    dias = v(H_VU, 'G%d' % f_bc1)
    elab = v(H_VU, 'I%d' % f_bc1)
    etiq = v(H_VU, 'J%d' % f_bc1)
    prueba('la fecha de la etiqueta es la de elaboración más los días que tú '
           'declaras', abs(etiq - elab - dias) < 0.001,
           '%r + %r = %r' % (elab, dias, etiq))

    # 2. La caja avisa de que caduca con su pieza más corta.
    veredicto = v(H_VU, 'M%d' % f_cj1)
    prueba('la caja surtida avisa de que caduca con su pieza más corta cuando '
           'te pasas', isinstance(veredicto, str) and veredicto != '',
           '%r' % (veredicto,))
    exc_b = ExcelCompiler(ruta)
    exc_b.evaluate("'%s'!M%d" % (H_VU, f_cj1))
    exc_b.set_value("'%s'!G%d" % (H_VU, f_cj1), 60)
    prueba('al declarar 60 días en la caja, el veredicto cambia al aviso del '
           'surtido',
           'surtido' in (exc_b.evaluate("'%s'!M%d" % (H_VU, f_cj1)) or ''),
           '%r' % (exc_b.evaluate("'%s'!M%d" % (H_VU, f_cj1)),))

    # 3. D47: la salida cambia de COLUMNA según la vía, y sólo una de las dos
    #    está rellena.
    d = v(H_ETQ, 'D%d' % f_bc1)
    e = v(H_ETQ, 'E%d' % f_bc1)
    prueba('un bombón a granel llena la columna de granel y deja vacía la de '
           'etiqueta', d in ('', None) and isinstance(e, str) and e != '',
           'etiqueta=%r' % (d,))
    exc2 = ExcelCompiler(ruta)
    # pycel sólo recalcula lo que ya está en el grafo: hay que EVALUAR las dos
    # salidas antes de tocar la entrada, o la segunda se lee sin actualizar.
    exc2.evaluate("'%s'!D%d" % (H_ETQ, f_bc1))
    exc2.evaluate("'%s'!E%d" % (H_ETQ, f_bc1))
    exc2.set_value("'%s'!C%d" % (H_ETQ, f_bc1), D.VIAS_DESPACHO[0])
    d2 = exc2.evaluate("'%s'!D%d" % (H_ETQ, f_bc1))
    e2 = exc2.evaluate("'%s'!E%d" % (H_ETQ, f_bc1))
    prueba('al pasarlo a envasado con etiqueta, las dos columnas se '
           'intercambian',
           isinstance(d2, str) and d2 != '' and e2 in ('', None))

    # 4. D31: el semáforo de la vitrina NO se enciende con el objetivo del kit
    #    y SÍ por encima de 20 grados C.
    tmax = v(H_TMP, 'D%d' % VIT_TMAX)
    ver = v(H_TMP, 'F%d' % VIT_TMAX)
    prueba('con la vitrina en el objetivo del kit el veredicto NO es de alarma',
           tmax <= 18 and 'Dentro' in ver, '%g grados C -> %r' % (tmax, ver))
    exc3 = ExcelCompiler(ruta)
    exc3.evaluate("'%s'!F%d" % (H_TMP, VIT_TMAX))
    exc3.set_value("'%s'!D%d" % (H_TMP, VIT_TMAX), 21)
    ver2 = exc3.evaluate("'%s'!F%d" % (H_TMP, VIT_TMAX))
    prueba('a 21 grados C sí salta el aviso de la manteca de cacao',
           'encima' in ver2, '%r' % (ver2,))

    # 5. La tanda recomendada nunca supera lo que vendes dentro de la vida
    #    útil: en chocolate manda la caducidad, no el lote económico.
    malas = []
    for i in range(len(FILAS)):
        fila = REF_INI + i
        rec, tope = v(H_LOT, 'M%d' % fila), v(H_LOT, 'H%d' % fila)
        if isinstance(rec, (int, float)) and isinstance(tope, (int, float)) \
                and rec > tope + 0.5:
            malas.append(FILAS[i]['r']['id'])
    prueba('la tanda recomendada nunca supera lo que vendes dentro de la vida '
           'útil', not malas, 'fallan %r' % (malas,))

    # 6. Acortar la vida útil sube la merma: es la relación que el libro
    #    vende, y tiene que verse al tocarla.
    antes = v(H_LOT, 'Q%d' % f_bc2)
    exc4 = ExcelCompiler(ruta)
    exc4.evaluate("'%s'!Q%d" % (H_LOT, f_bc2))
    exc4.set_value("'%s'!G%d" % (H_VU, f_bc2), 7)
    despues = exc4.evaluate("'%s'!Q%d" % (H_LOT, f_bc2))
    prueba('al acortar la vida útil de la ganache estabilizada, su merma sube',
           despues > antes, '%.2f -> %.2f euros/año' % (antes, despues))

    # 7. El total de merma es la suma de las 28 filas.
    filas = [v(H_LOT, 'Q%d' % (REF_INI + i)) for i in range(len(FILAS))]
    total = v(H_LOT, 'Q%d' % REF_TOT)
    prueba('la merma total del año suma las 28 referencias',
           abs(sum(filas) - total) < 0.01,
           '%.2f frente a %.2f' % (sum(filas), total))

    return ok, fallos


# --------------------------------------------------------------------------
def main():
    D.gate_legal(IDS_LEGALES)
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_parametros(wb)
    hoja_aw(wb)
    hoja_vida_util(wb)
    hoja_etiquetado(wb)
    hoja_temperatura(wb)
    hoja_lote(wb)

    res = X.cerrar(wb, NOMBRE, TITULO, mapa_celdas(), NOTAS_MAPA)

    print('escrito: %s' % res['ruta'])
    print('hojas: %d · fórmulas: %d · celdas verdes: %d · verdes vacías: %d'
          % (res['hojas'], res['formulas'], res['verdes'],
             len(res['verdes_vacias'])))
    print('fórmulas que devuelven «sin dato» a propósito: %d' % res['sin_dato'])
    print('notas legales: %d · notas de fuente sectorial: %d · etiquetas en el '
          'mapa: %d' % (res['notas_legales'], res['notas_sector'], res['mapa']))
    print('inject_cache: %s' % res['cache'])
    ok, fallos = demo(res['ruta'])
    for t in ok:
        print('  demo OK  · %s' % t)
    for t in fallos:
        print('  demo FALLA · %s' % t)
    if fallos:
        raise SystemExit('demos con fallos: %d' % len(fallos))


if __name__ == '__main__':
    main()
