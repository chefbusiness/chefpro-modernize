#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_carta-de-apertura-y-escandallo-chocolate.py — libro 4 de «Cómo Montar una
Chocolatería» (SPEC §2.2 fila 4; decisiones D32, D37, D38, D40, D44, D47, D52 y
la regla de IVA de §2.3 ampliada a la materia prima, A-2).

Hojas: Instrucciones · Parámetros · Denominaciones y Mínimos Legales ·
Escandallo por Molde y Tanda · Merma de Templado y Recortes · Coste Hora y Mano
de Obra · Unidad vs Caja · Mix y Ticket Medio · Decisión de Surtido.

QUÉ DECIDE ESTE LIBRO
---------------------
Qué vendes, a cuánto, cómo lo puedes llamar y si la caja te gana o te cuesta
dinero. La unidad de costeo es la TANDA (piezas por molde por moldes por tanda),
no la pieza suelta, y la mano de obra entra dentro.

DECISIONES TÉCNICAS
-------------------
* **D37, dos capas, y la base de cálculo NO se invierte.** La capa (a) es lo que
  el escandallo SÍ calcula: el porcentaje de chocolate **sobre el peso TOTAL del
  producto acabado, relleno incluido** (`CHN-10`, aps. 1.10 y 1.13). Calcularlo
  descontando el relleno da un resultado más favorable que el legal y deja pasar
  por el semáforo una referencia que no cumple. La capa (b) son las TRES
  magnitudes que la norma pide de verdad —materia seca total de cacao, manteca
  y materia seca desgrasada— que la bolsa no trae: van en celdas verdes que el
  lector COPIA de la ficha técnica de su proveedor.
* **D40, DOS tasas de merma, y la regla es del kit** (`02-partidas-produccion.xlsx!Moldeado`):
  «El chocolate sin relleno y sin contaminar se puede refundir; el que lleva
  ganache o fruta, a residuo». La merma RECUPERABLE vuelve a la cuba y no es
  coste de materia —lo que cuesta es volver a templarla, y eso lo cobra la mano
  de obra—; la NO RECUPERABLE va a residuo y se reparte entre las piezas buenas.
* **Regla de IVA (§2.3, regla 3, ampliada a la materia prima).** `CHS-28a` está
  declarada CON IVA y `CHS-29` son precios de MOSTRADOR: el food cost se calcula
  SIEMPRE sobre base imponible en los DOS lados del cociente. El precio de
  cobertura llega del libro 3 en BASE IMPONIBLE, nunca el de base con IVA.
* **D32, cruce 4 ← 3, sin una sola fórmula entre ficheros.** El precio de cada
  cobertura es una celda VERDE «trae aquí la cifra de
  `sensibilidad-al-precio-del-cacao.xlsx!Coste de Cobertura por Referencia!<Celda>`»
  con su valor por defecto declarado, más una **fila de CUADRE** con semáforo.
* **El coste hora de obrador se CALCULA** desde `PLANTILLA` y `CONVENIO` (bruto
  por pagas por jornada, más Seguridad Social, entre las horas PRODUCTIVAS). No
  es un dato del sector y no se teclea.
* **La regla del margen es UNA SOLA:** «Parámetros» pide el food cost objetivo y
  DERIVA el margen bruto. Pedir los dos deja ponerlos incoherentes.
* Cero constantes dentro de fórmulas; `IFERROR(...,"")` en toda división; «sin
  dato» = `""`; semáforos con `ISNUMBER`; DV contra RANGO. Prohibidas INDIRECT,
  COUNTA, PMT, OFFSET, XLOOKUP, LET, LAMBDA, RANK, NETWORKDAYS e IRR.

FRONTERAS (SPEC §2.7), escritas en «Instrucciones»
--------------------------------------------------
* **D38** — `kit-escandallos/05-pasteleria.xlsx` **sí** tiene hoja `Tarta
  Chocolate`: costea una elaboración por unidad. Lo que no existe en el catálogo
  es el escandallo del obrador de bombonería, por molde y por tanda, con merma
  de templado, recorte recuperable y la caja como unidad de venta.
* **K1** — las curvas de templado y las fichas de moldeado son del Kit de Tareas
  Chocolatería (12 €). Aquí no hay técnica: hay euros.
* El método de costeo por lote y la ingeniería de menú son la Guía Food Cost
  (capítulo 17).

Salida fija: build/carta-de-apertura-y-escandallo-chocolate.xlsx + su mapa.
Uso: /usr/local/bin/python3 gen_carta-de-apertura-y-escandallo-chocolate.py
Via: Claude Code
"""
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Font

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import _comun_libros_4_6 as C                                  # noqa: E402
import datos_ejemplo as D                                      # noqa: E402
import motor                                                   # noqa: E402

NOMBRE = 'carta-de-apertura-y-escandallo-chocolate'
TITULO = 'Carta de Apertura y Escandallo del Obrador de Bombonería'

H_INS = 'Instrucciones'
H_PAR = 'Parámetros'
# Excel no admite un nombre de hoja de más de 31 caracteres y
# «Denominaciones y Mínimos Legales» tiene 32: la pestaña se acorta y el
# título completo va en A1.
H_DEN = 'Denominaciones y Mínimos'
# Ojo: Excel PROHÍBE la barra «/» en el nombre de una hoja (y `motor.RX_ILEGAL_HOJA`
# la caza). La SPEC escribe «Escandallo por Molde/Tanda»; el nombre publicable es
# «Escandallo por Molde y Tanda».
H_ESC = 'Escandallo por Molde y Tanda'
H_MER = 'Merma de Templado y Recortes'
H_MO = 'Coste Hora y Mano de Obra'
H_CAJ = 'Unidad vs Caja'
H_MIX = 'Mix y Ticket Medio'
H_SUR = 'Decisión de Surtido'

QPAR = "'" + H_PAR + "'!"
QESC = "'" + H_ESC + "'!"
QMER = "'" + H_MER + "'!"
QMO = "'" + H_MO + "'!"
QCAJ = "'" + H_CAJ + "'!"
QMIX = "'" + H_MIX + "'!"

CARTA = D.CARTA
NR = len(CARTA)                                   # 28
BOMBONES = [r for r in CARTA if r['familia'] == 'Bombones de coleccion']
CAJAS = [r for r in CARTA if D.es_caja(r)]
NB, NC = len(BOMBONES), len(CAJAS)                # 10 y 4

RELLENOS = list(D.RELLENOS.items())               # 13
ANADIDOS = sorted(set(D.ANADIDOS.values()))       # 2
LINEAS = [(k, ing, cant) for k, v in RELLENOS for ing, cant in v['lineas']]
NL = len(LINEAS)                                  # 42
INGREDIENTES = sorted(D.PRECIOS_COMPRA)           # 26
PERSONAL = [p for p in D.PLANTILLA if p[4] == 'OBRADOR']

#: Las cuatro coberturas, en el orden en que se publican.
COBS = ('negra', 'origen', 'leche', 'blanca')
#: Nombre con el que cada cobertura entra en la tabla de precios de compra: es
#: la clave de `PRECIOS_COMPRA`, para que haya UNA sola tabla de búsqueda.
COB_ING = {'negra': 'Cobertura negra', 'origen': 'Cobertura de origen',
           'leche': 'Cobertura con leche', 'blanca': 'Cobertura blanca'}

#: Celda EXACTA del libro 3 de la que sale cada precio, leída en
#: `build/mapa-sensibilidad-al-precio-del-cacao.json` el 12-09-2026. Son las
#: columnas de BASE IMPONIBLE (la G), nunca la de base con IVA (la D): `CHS-28a`
#: está declarada CON IVA y un escandallo con precios con IVA sale ~9 % alto.
CELDA_ORIGEN_COB = {'negra': 'Coste de Cobertura!G7',
                    'origen': 'Coste de Cobertura!G8',
                    'leche': 'Coste de Cobertura!G9',
                    'blanca': 'Coste de Cobertura!G10'}
FICHERO_LIBRO_3 = 'sensibilidad-al-precio-del-cacao.xlsx'

# ---------------------------------------------------------------- Parámetros
PER_CAB = 6
PER_INI = 7
PER_FIN = PER_INI + len(PERSONAL) - 1
PER_TOT = PER_FIN + 1

P_PAGAS = 'B%d' % (PER_TOT + 2)
P_SS = 'B%d' % (PER_TOT + 3)
P_HANIO = 'B%d' % (PER_TOT + 4)
P_RATIO = 'B%d' % (PER_TOT + 5)
P_CHORA = 'B%d' % (PER_TOT + 6)

SEC_IVA = PER_TOT + 8
P_IVAP = 'B%d' % (SEC_IVA + 1)
P_IVATZ = 'B%d' % (SEC_IVA + 2)

SEC_MAR = SEC_IVA + 4
P_FC = 'B%d' % (SEC_MAR + 1)
P_MB = 'B%d' % (SEC_MAR + 2)

SEC_COB = SEC_MAR + 4
COB_CAB = SEC_COB + 1
COB_INI = COB_CAB + 1
COB_FIN = COB_INI + len(COBS) - 1
COB_CUA = COB_FIN + 1                              # fila de CUADRE

SEC_OTR = COB_CUA + 2
P_TICK = 'B%d' % (SEC_OTR + 1)
P_PZTK = 'B%d' % (SEC_OTR + 2)
P_DIAS = 'B%d' % (SEC_OTR + 3)
P_PZDIA = 'B%d' % (SEC_OTR + 4)
P_PZANO = 'B%d' % (SEC_OTR + 5)
P_PACK = 'B%d' % (SEC_OTR + 6)
P_TOL = 'B%d' % (SEC_OTR + 7)
P_UFC = 'B%d' % (SEC_OTR + 8)
P_UMIX = 'B%d' % (SEC_OTR + 9)
P_UMER = 'B%d' % (SEC_OTR + 10)
P_UMAR = 'B%d' % (SEC_OTR + 11)

SEC_PRE = SEC_OTR + 13
PRE_CAB = SEC_PRE + 1
PRE_INI = PRE_CAB + 1
PRE_FIN = PRE_INI + len(INGREDIENTES) - 1
PAR_PIE = PRE_FIN + 2

TABLA_PRECIOS = '%s$A$%d:$B$%d' % (QPAR, PRE_INI, PRE_FIN)


def A(coord):
    """Referencia absoluta a una celda de «Parámetros»."""
    return QPAR + '$' + coord[0] + '$' + coord[1:]


# --------------------------------------------------------------- Escandallo
LIN_SEC = 5
LIN_CAB = 6
LIN_INI = LIN_CAB + 1
LIN_FIN = LIN_INI + NL - 1

REL_SEC = LIN_FIN + 2
REL_CAB = REL_SEC + 1
REL_INI = REL_CAB + 1
REL_FIN = REL_INI + len(RELLENOS) + len(ANADIDOS) - 1
TABLA_RELLENOS = '%s$A$%d:$B$%d' % (QESC, REL_INI, REL_FIN)

ESC_SEC = REL_FIN + 2
ESC_CAB = ESC_SEC + 1
ESC_INI = ESC_CAB + 1
ESC_FIN = ESC_INI + NR - 1

# ------------------------------------------------- Resto de hojas (una fila
# por referencia y en el MISMO orden en todas: así una fila es la misma
# referencia en las seis hojas y el lector no tiene que buscarla).
FIL_CAB = 6
FIL_INI = 7
FIL_FIN = FIL_INI + NR - 1
FIL_TOT = FIL_FIN + 1

#: Fila (en las hojas de una fila por referencia) de cada id.
FILA = dict((r['id'], FIL_INI + i) for i, r in enumerate(CARTA))
#: Fila en el bloque de escandallo.
FILA_ESC = dict((r['id'], ESC_INI + i) for i, r in enumerate(CARTA))

# --------------------------------------------------------------- Unidad vs Caja
CAJ_CAB = 6
CAJ_INI = 7
CAJ_FIN = CAJ_INI + NB - 1
CAJ_RES = CAJ_FIN + 3                    # primera fila del bloque de salidas
#: Columnas de las cuatro cajas en «Unidad vs Caja».
CAJ_COL = ('C', 'D', 'E', 'F')

# Etiquetas del bloque de salidas, en orden.
CAJ_FILAS = (
    'Unidades que lleva la caja',
    'Peso de chocolate de la caja (g)',
    'Peso total de la caja (g)',
    'Porcentaje de chocolate sobre el peso TOTAL',
    'Coste de materia de las piezas, sin merma (EUR)',
    'Coste de materia de la caja, con su merma de montaje (EUR)',
    'Coste de materia de esos bombones vendidos sueltos, con su merma (EUR)',
    'Coste de mano de obra de las piezas que lleva dentro (EUR)',
    'Coste de mano de obra del montaje de la caja (EUR)',
    'COSTE TOTAL DE LA CAJA (EUR)',
    'PVP de la caja, con IVA (EUR)',
    'PVP de la caja, sin IVA (EUR)',
    'PVP de esos bombones vendidos sueltos, con IVA (EUR)',
    'PVP de esos bombones vendidos sueltos, sin IVA (EUR)',
    'Precio por bombón EN CAJA, con IVA (EUR)',
    'Precio por bombón SUELTO, con IVA (EUR)',
    'Descuento que le haces al cliente por comprar la caja',
    'Contraste de mercado: EUR por bombón publicado (CHS-29)',
    'MARGEN DE LA CAJA (EUR)',
    'Margen vendiendo esos mismos bombones sueltos (EUR)',
    'Diferencia de margen: la caja menos el suelto (EUR)',
    'Veredicto',
)
F_UDS, F_PCHO, F_PTOT, F_PCT, F_MATSM, F_MATCM, F_MATSU, F_MOPZ, F_MOMON, \
    F_COSTE, F_PVPCI, F_PVPSI, F_SUECI, F_SUESI, F_PBCAJA, F_PBSUE, F_DTO, \
    F_CONTR, F_MARCA, F_MARSU, F_DIF, F_VER = \
    [CAJ_RES + i for i in range(len(CAJ_FILAS))]

# --------------------------------------------------------------- Mix, resumen
MIX_RES = FIL_TOT + 2
M_PVPA = 'B%d' % MIX_RES
M_PVPV = 'B%d' % (MIX_RES + 1)
M_PZTK = 'B%d' % (MIX_RES + 2)
M_TKCI = 'B%d' % (MIX_RES + 3)
M_TKSI = 'B%d' % (MIX_RES + 4)
M_TKVE = 'B%d' % (MIX_RES + 5)
M_FCA = 'B%d' % (MIX_RES + 6)
M_FCV = 'B%d' % (MIX_RES + 7)
M_PACK = 'B%d' % (MIX_RES + 8)
M_FCS = 'B%d' % (MIX_RES + 9)
M_DIF = 'B%d' % (MIX_RES + 10)
M_MBA = 'B%d' % (MIX_RES + 11)
M_MBV = 'B%d' % (MIX_RES + 12)
M_CAIDA = 'B%d' % (MIX_RES + 13)
M_CUADRE = 'B%d' % (MIX_RES + 14)

# --------------------------------------------------------------- Surtido
SUR_CNT = FIL_TOT + 2
VEREDICTOS = ('Mantener', 'Revisar precio', 'Retirar')

# --------------------------------------------------------------- Denominaciones
DEN_UMB = FIL_TOT + 2
U_25 = 'B%d' % (DEN_UMB + 1)
U_TAZA_T = 'B%d' % (DEN_UMB + 2)
U_TAZA_M = 'B%d' % (DEN_UMB + 3)
U_TAZA_D = 'B%d' % (DEN_UMB + 4)

CAPB_SEC = DEN_UMB + 6
CAPB_CAB = CAPB_SEC + 1
CAPB_INI = CAPB_CAB + 1
CAPB_FIN = CAPB_INI + len(COBS) - 1


def primer_id(fuente):
    """«CHN-03 + CHN-82» -> «CHN-03». Los ids se citan con su sufijo (D44)."""
    return fuente.split('+')[0].strip()


def etiqueta_relleno(r):
    """Nombre con el que la referencia busca su relleno o su materia añadida en
    la tabla de costes por kilo."""
    if r['relleno']:
        return r['relleno']
    if r['id'] in D.ANADIDOS:
        return D.ANADIDOS[r['id']]
    return None


# ==========================================================================
# Hoja «Instrucciones»
# ==========================================================================
PASOS = [
    '1. Hoja «Parámetros». Empieza por el bloque de personal de obrador: el '
    'coste de la hora de obrador NO es un dato del sector y no se teclea, se '
    'calcula con el bruto de tu convenio, las pagas, la jornada de cada '
    'persona y la Seguridad Social a cargo de la empresa. Justo debajo está el '
    'bloque del PRECIO DE COBERTURA, que viene del libro 3 y que es la celda '
    'más crítica de todo el paquete, y la tabla de precios de compra: es la '
    'única tabla donde se tocan los precios, y de ella beben las 42 líneas de '
    'las fórmulas de relleno.',
    '2. Hoja «Denominaciones y Mínimos Legales». Dos capas, y no son lo mismo. '
    'La capa (a) la calcula el libro solo, con los gramos que tú metes en el '
    'escandallo: el porcentaje de chocolate sobre el PESO TOTAL de la pieza, '
    'con el relleno dentro. La capa (b) son tres celdas verdes por cobertura '
    '-materia seca total de cacao, manteca de cacao y materia seca '
    'desgrasada- que tienes que COPIAR de la ficha técnica de tu proveedor: la '
    'bolsa sólo trae el total, y la norma trabaja con las tres.',
    '3. Hoja «Escandallo por Molde y Tanda». Arriba, las fórmulas de relleno: '
    'una línea por ingrediente, con la cantidad que entra en un kilo. Abajo, '
    'una fila por referencia con los gramos de chocolate y los gramos de '
    'relleno por pieza. El coste de materia sale solo. Las cajas no tienen '
    'escandallo propio: se componen de sus bombones.',
    '4. Hoja «Merma de Templado y Recortes». Dos tasas por referencia, y son '
    'distintas a propósito: el chocolate limpio que recortas vuelve a la cuba y '
    'no se pierde; el que lleva ganache o fruta va a residuo. La hoja te dice '
    'cuántos kilos al año vuelven, cuántos se van y cuánto te cuesta eso.',
    '5. Hoja «Coste Hora y Mano de Obra». Piezas por molde, moldes por tanda y '
    'minutos de la tanda. De ahí salen el coste de mano de obra por pieza, el '
    'coste total, el food cost, el margen en euros y el precio que te pide tu '
    'propia regla de margen. Es la hoja que enseña a dejar de regalar el '
    'trabajo del obrador.',
    '6. Hoja «Unidad vs Caja». Escribe cuántos bombones de cada tipo lleva '
    'cada caja. El libro compara el precio de la caja con la suma de sus '
    'unidades sueltas y te dice si la caja te gana o te cuesta dinero. Y aquí '
    'sí entra la mano de obra de los bombones de dentro: una caja no cuesta '
    'sólo lo que cuesta montarla.',
    '7. Hoja «Mix y Ticket Medio». Reparte el 100 % de tus unidades entre las '
    '28 referencias, y otra vez para julio y agosto, que no se vende lo mismo. '
    'De ahí sale tu ticket medio, que no se copia de ningún estudio porque no '
    'existe un ticket medio publicado de chocolatería.',
    '8. Hoja «Decisión de Surtido». Cruza margen y rotación y te dice qué '
    'mantener, a qué revisarle el precio y qué retirar. Repásala a los tres '
    'meses de abrir, con ventas reales, y otra vez al cambiar de temporada.',
]

NOTAS_LIBRO = [
    'EL 25 % DEL BOMBÓN SE CALCULA SOBRE EL PESO TOTAL, CON EL RELLENO DENTRO. '
    'La norma tiene DOS bases de cálculo opuestas y confundirlas cambia el '
    'veredicto: en los apartados 1.6 a 1.9, 1.11 y 1.12 los mínimos se '
    'calculan DESCONTANDO los ingredientes añadidos; en el 1.10 (chocolate '
    'relleno) y en el 1.13 (bombón) el contenido de chocolate se calcula SOBRE '
    'EL PESO TOTAL del producto acabado, relleno incluido. Calcular el 25 % '
    'del bombón descontando el relleno da un resultado más favorable que el '
    'legal y deja pasar una referencia que no cumple.',
    'LA BOLSA DE COBERTURA NO TRAE LO QUE LA NORMA PIDE. Una bolsa publica '
    '«54,5 %» y nada más. La norma no trabaja con «% de cacao»: trabaja con '
    'materia seca TOTAL de cacao, manteca de cacao y materia seca DESGRASADA. '
    'Son tres magnitudes y están en la ficha técnica del proveedor, no en el '
    'envase. Pídesela: es la misma ficha que te va a pedir el libro de '
    'proveedores para el boletín de cadmio.',
    'PRALINÉ NO ES UN NOMBRE COMERCIAL. El punto 10 de la parte A del Anexo I '
    'de la Directiva 2000/36/CE se titula «Bombón de chocolate o praliné»: es '
    'denominación de venta europea y le aplica el MISMO mínimo del 25 %. '
    '«Trufa», en cambio, no aparece ni una vez en el Real Decreto 1055/2003: '
    'es un TIPO de bombón, no una categoría legal.',
    'EL RECORTE LIMPIO NO ES MERMA, Y EL QUE LLEVA GANACHE SÍ. Lo dice el '
    'propio Kit de Tareas Chocolatería: «El chocolate sin relleno y sin '
    'contaminar se puede refundir; el que lleva ganache o fruta, a residuo». '
    'Por eso este libro lleva DOS tasas por referencia. La recuperable no '
    'encarece la materia -vuelve a la cuba-, pero sí cuesta volver a templarla, '
    'y ese trabajo lo paga la mano de obra. La no recuperable se reparte entre '
    'las piezas que salen bien.',
    'EL FOOD COST SE CALCULA CON LAS DOS PATAS EN LA MISMA BASE. El precio de '
    'cobertura publicado por el distribuidor viene CON IVA y el precio de la '
    'caja de bombones es un precio de mostrador, que también lo lleva. Un '
    'escandallo se calcula con precios SIN IVA, porque el soportado es '
    'deducible: con la base equivocada en un solo lado del cociente el food '
    'cost sale alrededor de un 9 % alto y el margen que crees tener no existe.',
    'LA REGLA DEL MARGEN ES UNA SOLA, DICHA DE DOS FORMAS. Food cost del 30 % y '
    'margen bruto del 70 % son el mismo número visto del derecho y del revés. '
    'Por eso «Parámetros» te pide UNO y calcula el otro: cualquier herramienta '
    'que te pida los dos te va a dejar ponerlos incoherentes.',
    'DÓNDE ESTÁ EL ESCANDALLO UNITARIO, QUE AQUÍ NO ESTÁ. El Kit de Escandallos '
    'trae una hoja de tarta de chocolate dentro de su libro de pastelería: '
    'costea una elaboración por unidad. Lo que no existe en el catálogo es el '
    'escandallo del obrador de bombonería -por molde y por tanda, con merma de '
    'templado, recorte recuperable y la caja como unidad de venta-, y eso es lo '
    'que construye esta guía. El método de costeo por lote y la ingeniería de '
    'menú son la Guía Food Cost, capítulo 17.',
    'DÓNDE ESTÁN LAS CURVAS DE TEMPLADO, QUE AQUÍ TAMPOCO. Las curvas y las '
    'fichas de moldeado son del Kit de Tareas Chocolatería (12 €), hoja '
    '«Templado» de su 02-partidas-produccion.xlsx. Esta guía no repite la '
    'técnica: pone los euros. Y los tres tipos de cobertura con los que se '
    'monta el escandallo son los que el propio kit precarga: negra del 55 al '
    '70 % de cacao, con leche del 35 al 40 % y blanca del 28 al 33 %.',
    'LOS PRECIOS DE COMPRA DEL EJEMPLO SON DE UNA BOMBONERÍA MODELADA. Sólo dos '
    'están verificados con fuente: la cobertura de marca y la de origen. El '
    'resto son supuestos declarados, porque no hay precio público de materia '
    'prima de relleno. Bórralos y pon tus albaranes: un escandallo con precios '
    'de otro no vale nada.',
]

CADENCIA = ('Cada cuánto se usa este libro: el precio de la cobertura y los '
            'precios de compra, CADA VEZ que te suba un proveedor y como '
            'mínimo una vez al trimestre -y el del cacao se mueve solo, por '
            'eso tiene un libro entero para él-. El escandallo y los minutos '
            'de la tanda, al montar la carta y cada vez que cambies un '
            'proceso. Las denominaciones, UNA VEZ por referencia y siempre que '
            'cambies de cobertura. El mix, el ticket medio y la decisión de '
            'surtido, a los tres meses de abrir y luego cada temporada, con el '
            'mix de julio y agosto aparte.')


def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS, 0)
    ws.column_dimensions['A'].width = 90.0
    C.cabecera_hoja(ws, TITULO)
    motor.val(ws, 'A3', 'Para qué sirve: decidir qué vendes, a cuánto, cómo lo '
                        'puedes llamar y si la caja te gana o te cuesta dinero.')
    ws['A3'].font = Font(italic=True, size=9)

    C.seccion(ws, 'A5', 'Instrucciones de uso')
    fila = 6
    for paso in PASOS:
        motor.val(ws, 'A%d' % fila, paso, wrap=True)
        ws.row_dimensions[fila].height = 72
        fila += 1
    fila += 1
    C.entrada(ws, 'A%d' % fila, C.LEYENDA_VERDE,
              etiqueta='Leyenda de celdas verdes')
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Lo que conviene saber antes de empezar')
    fila += 1
    for nota in NOTAS_LIBRO:
        motor.val(ws, 'A%d' % fila, nota, wrap=True)
        ws.row_dimensions[fila].height = 86
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, CADENCIA, wrap=True)
    ws.row_dimensions[fila].height = 62
    fila += 2
    motor.val(ws, 'A%d' % fila, C.DESPROTEGER, wrap=True)
    ws.row_dimensions[fila].height = 30
    fila += 2
    motor.val(ws, 'A%d' % fila, C.BIO, wrap=True)
    fila += 1
    motor.val(ws, 'A%d' % fila, C.VERSION_LINE)
    ws['A%d' % fila].font = Font(size=8, italic=True)
    C.setup(ws, landscape=False)
    return ws


# ==========================================================================
# Hoja «Parámetros»
# ==========================================================================
def par(ws, fila, etiqueta, valor, fmt, unidad, fuente, nota, formula=None,
        id_chn=None, id_chs=None):
    motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
    if formula is not None:
        cel = motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=True)
        C.crema(cel)
    else:
        cel = C.entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
    motor.val(ws, 'C%d' % fila, unidad)
    motor.val(ws, 'D%d' % fila, fuente)
    ws['D%d' % fila].font = Font(size=8, color=C.GRIS)
    motor.val(ws, 'E%d' % fila, nota, wrap=True)
    ws['E%d' % fila].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[fila].height = 42
    if id_chn:
        C.nota_celda(ws, cel.coordinate, id_chn)
    if id_chs:
        C.nota_sector(ws, cel.coordinate, id_chs)
    return cel


def hoja_parametros(wb):
    ws = wb.create_sheet(H_PAR)
    C.cabecera_hoja(ws, 'Parámetros')
    motor.val(ws, 'A3', 'Todo lo que el resto de hojas da por sabido vive aquí. '
                        'Ninguna fórmula de este libro lleva un número dentro.')
    ws['A3'].font = Font(italic=True, size=9)
    for letra, ancho in (('A', 52), ('B', 16), ('C', 14), ('D', 22), ('E', 78),
                         ('F', 16), ('G', 18), ('H', 46)):
        ws.column_dimensions[letra].width = ancho

    # --- personal de obrador ----------------------------------------------
    C.seccion(ws, 'A%d' % (PER_CAB - 1),
              'Personal de obrador y coste de la hora (se CALCULA, no se teclea)')
    C.encabezados(ws, PER_CAB, [
        ('A', 'Perfil (nombre literal del Kit de Tareas Chocolatería)', None),
        ('B', 'Jornada (1,0 = completa)', None),
        ('C', 'Grupo del convenio', None),
        ('D', 'Bruto mensual del grupo (EUR)', None),
        ('E', 'Bruto anual con pagas y jornada (EUR)', None),
        ('F', 'Coste de empresa con Seguridad Social (EUR)', None),
        ('G', 'Horas productivas al año', None),
        ('H', 'Nota', None)], alto=48)
    for i, (_pid, perfil, jornada, grupo, _area, _h, turno) in enumerate(PERSONAL):
        fila = PER_INI + i
        motor.val(ws, 'A%d' % fila, perfil)
        C.entrada(ws, 'B%d' % fila, jornada, fmt=C.DEC1,
                  etiqueta='Jornada de %s' % perfil)
        motor.val(ws, 'C%d' % fila, '%d - %s' % (grupo, D.CONVENIO[grupo - 1][1]))
        br = C.entrada(ws, 'D%d' % fila, D.CONVENIO[grupo - 1][2], fmt=C.EUR,
                       etiqueta='Bruto mensual de %s' % perfil)
        C.nota_celda(ws, br.coordinate, 'CHN-65b')
        motor.f(ws, 'E%d' % fila, '=D%d*%s*B%d' % (fila, A(P_PAGAS), fila),
                fmt=C.EUR)
        motor.f(ws, 'F%d' % fila, '=E%d*(1+%s)' % (fila, A(P_SS)), fmt=C.EUR)
        motor.f(ws, 'G%d' % fila,
                '=%s*B%d*%s' % (A(P_HANIO), fila, A(P_RATIO)), fmt=C.ENT)
        motor.val(ws, 'H%d' % fila,
                  'Turno %s. Tabla salarial de Madrid, marcada EJEMPLO: '
                  'sustitúyela por la de TU convenio.' % turno.lower(),
                  wrap=True)
        ws['H%d' % fila].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[fila].height = 38
    motor.val(ws, 'A%d' % PER_TOT, 'TOTAL del obrador', bold=True)
    for col in ('E', 'F', 'G'):
        motor.f(ws, '%s%d' % (col, PER_TOT),
                '=SUM(%s%d:%s%d)' % (col, PER_INI, col, PER_FIN),
                fmt=C.EUR if col != 'G' else C.ENT, bold=True)

    par(ws, PER_TOT + 2, 'Pagas del convenio al año', D.P('pagas_convenio'),
        C.ENT, 'pagas', 'CHN-65b',
        'El convenio de Madrid paga 15, no 14: cambia el coste mes a mes.',
        id_chn='CHN-65b')
    par(ws, PER_TOT + 3, 'Seguridad Social a cargo de la empresa',
        D.P('ss_empresa'), C.PCT, 'sobre bruto', 'motor.PARAMETROS',
        'Cotización empresarial aproximada sobre el bruto: contingencias '
        'comunes, desempleo, FOGASA y formación. Ajústala a tus contratos.')
    par(ws, PER_TOT + 4, 'Horas anuales de contrato a jornada completa',
        D.P('horas_anuales_contrato'), C.ENT, 'horas/año', 'supuesto',
        '40 horas por 52 semanas son 2.080, menos 30 días naturales de '
        'vacaciones y los festivos del calendario laboral.')
    par(ws, PER_TOT + 5, 'Parte de la jornada que se pasa a pie de mesa',
        D.P('ratio_horas_productivas'), C.PCT, 'sobre la jornada', 'supuesto',
        'El resto es recepción, limpieza, formación y reuniones. Repartir el '
        'coste entre las horas de contrato en vez de entre las productivas '
        'abarata la hora de obrador y sale un margen que no existe.')
    par(ws, PER_TOT + 6, 'COSTE DE LA HORA DE OBRADOR', None, C.EUR,
        'EUR/hora productiva', 'calculado',
        'Coste de empresa de las personas de obrador entre sus horas '
        'PRODUCTIVAS. Del bruto al coste de empresa hay un 33 %, y es el salto '
        'que más sorprende. No es el bruto ni el bruto con Seguridad Social.',
        formula='=IFERROR(F%d/G%d,"")' % (PER_TOT, PER_TOT))

    # --- IVA ---------------------------------------------------------------
    C.seccion(ws, 'A%d' % SEC_IVA, 'IVA por familia (regla 3 de la SPEC)')
    par(ws, SEC_IVA + 1, 'IVA del chocolate (entrega de un bien)',
        D.P('iva_producto'), C.PCT, 'sobre base', 'CHN-71',
        'El chocolate va al 10 % POR EXCLUSIÓN, no porque un precepto lo '
        'nombre: la lista del 4 % es cerrada y tiene siete letras, y el '
        'chocolate no está en ninguna ni entre las dos exclusiones del 10 %.',
        id_chn='CHN-71')
    par(ws, SEC_IVA + 2, 'IVA del chocolate a la taza servido en sala',
        D.P('iva_taza_servida'), C.PCT, 'sobre base', 'CHN-71c',
        'Servirlo en sala es prestación de servicio de hostelería, no entrega '
        'de un bien: va al 10 % por el art. 91.Uno.2.2.º. Si mañana cambia uno '
        'de los dos tipos, el libro no se toca: se cambia aquí.',
        id_chn='CHN-71c')

    # --- margen ------------------------------------------------------------
    C.seccion(ws, 'A%d' % SEC_MAR, 'La regla del margen, que es UNA SOLA')
    par(ws, SEC_MAR + 1, 'Food cost objetivo (coste de materia sobre PVP)',
        D.P('food_cost_objetivo'), C.PCT, 'sobre PVP sin IVA', 'supuesto',
        'SUPUESTO declarado: no existe dato público de food cost de '
        'bombonería. Es el ÚNICO de los dos números que se teclea.')
    par(ws, SEC_MAR + 2, 'Margen bruto objetivo (se DERIVA del anterior)', None,
        C.PCT, 'sobre PVP sin IVA', 'calculado',
        'Margen bruto y food cost son la misma regla dicha dos veces. '
        'Publicarlos como dos reglas independientes es un error de método: se '
        'pueden poner incoherentes y nadie se entera.',
        formula='=1-%s' % A(P_FC))

    # --- precio de cobertura: cruce 4 <- 3 ---------------------------------
    C.seccion(ws, 'A%d' % SEC_COB,
              'Precio de cobertura EN BASE IMPONIBLE: trae aquí la cifra de '
              + FICHERO_LIBRO_3 + '!Coste de Cobertura!G7 (negra; G8/G9/G10 '
              'para origen/leche/blanca en la fila de cada una, columna de '
              'base imponible, nunca la de base con IVA)')
    ws.row_dimensions[SEC_COB].height = 30
    C.apunte(ws, 'H%d' % SEC_COB,
             'Cruce 4 <- 3 de la SPEC: celda verde con su valor por defecto '
             'declarado y fila de CUADRE. NO hay fórmula entre ficheros.')
    C.encabezados(ws, COB_CAB, [
        ('A', 'Cobertura', None),
        ('B', 'Precio en BASE IMPONIBLE traído del libro 3 (EUR/kg)', None),
        ('C', 'Precio que publica hoy el libro 3 (EUR/kg)', None),
        ('D', 'Desviación', None),
        ('E', 'Base de IVA de la fuente, y nota', None),
        ('F', 'Celda exacta del libro 3', None)], alto=48)
    for i, k in enumerate(COBS):
        fila = COB_INI + i
        cob = D.COBERTURAS[k]
        base = round(D.precio_cobertura_base_imponible(k), 4)
        motor.val(ws, 'A%d' % fila, cob['nombre'], wrap=True)
        b = C.entrada(ws, 'B%d' % fila, base, fmt=C.EUR4,
                      etiqueta='Precio traído del libro 3 de %s' % cob['nombre'])
        C.entrada(ws, 'C%d' % fila, base, fmt=C.EUR4,
                  etiqueta='Precio que publica el libro 3 de %s' % cob['nombre'])
        motor.f(ws, 'D%d' % fila,
                '=IFERROR(ABS(B%d-C%d)/C%d,"")' % (fila, fila, fila), fmt=C.PCT)
        motor.val(ws, 'E%d' % fila,
                  'Base de la fuente: %s. %s' % (cob['base_iva'], cob['nota']),
                  wrap=True)
        ws['E%d' % fila].font = Font(size=8, color=C.GRIS)
        motor.val(ws, 'F%d' % fila,
                  '%s (cacao del %s al %s %% según el kit)'
                  % (CELDA_ORIGEN_COB[k],
                     ('%.0f' % cob['cacao_min_pct']),
                     ('%.0f' % cob['cacao_max_pct'])), wrap=True)
        ws.row_dimensions[fila].height = 44
        if cob['fuente_precio'].startswith('CHS-'):
            C.nota_sector(ws, b.coordinate, cob['fuente_precio'])
    motor.val(ws, 'A%d' % COB_CUA,
              'CUADRE: lo que has traído frente a lo que publica el libro 3',
              bold=True)
    motor.f(ws, 'B%d' % COB_CUA, '=MAX(D%d:D%d)' % (COB_INI, COB_FIN),
            fmt=C.PCT, bold=True)
    motor.val(ws, 'C%d' % COB_CUA, 'desviación máxima')
    motor.f(ws, 'D%d' % COB_CUA,
            '=IF(NOT(ISNUMBER(B%d)),"",IF(B%d<=%s,"CUADRA",'
            '"REVISA: lo que has traído no es lo que publica el libro 3"))'
            % (COB_CUA, COB_CUA, A(P_TOL)), bold=True)
    motor.val(ws, 'E%d' % COB_CUA,
              'Si el libro 3 cambia de escenario de precio, cambian las dos '
              'columnas. Esta fila existe para que no se quede una sola.',
              wrap=True)
    ws['E%d' % COB_CUA].font = Font(size=8, color=C.GRIS)
    motor.semaforo_isnumber(ws, 'B%d' % COB_CUA, '$B$%d' % COB_CUA, '>',
                            A(P_TOL))

    # --- volumen, packaging y umbrales -------------------------------------
    C.seccion(ws, 'A%d' % SEC_OTR, 'Volumen, packaging y umbrales')
    par(ws, SEC_OTR + 1, 'Clientes al día en velocidad de crucero',
        D.P('tickets_dia_crucero'), C.ENT, 'clientes/día', 'supuesto',
        'NO es un dato del sector: no existe ticket medio publicado de '
        'chocolatería. Mídelo con tu TPV en dos semanas.')
    par(ws, SEC_OTR + 2, 'Piezas por ticket', D.P('piezas_por_ticket'), C.DEC1,
        'piezas/ticket', 'supuesto',
        'En bombonería es BAJO porque la unidad de venta real es la caja: '
        'quien entra a por un regalo se lleva UNA caja, no ocho bombones.')
    par(ws, SEC_OTR + 3, 'Días de apertura al año',
        D.NEGOCIO['dias_apertura_anio'], C.ENT, 'días', 'supuesto',
        D.NEGOCIO['nota_dias_apertura'])
    par(ws, SEC_OTR + 4, 'Piezas vendidas al día', None, C.DEC1, 'piezas/día',
        'calculado', 'Clientes al día por piezas por ticket.',
        formula='=IFERROR(%s*%s,"")' % (A(P_TICK), A(P_PZTK)))
    par(ws, SEC_OTR + 5, 'Piezas vendidas al año', None, C.ENT, 'piezas/año',
        'calculado',
        'Es el volumen con el que la hoja de merma pasa de euros por pieza a '
        'euros al año, y el que reparte el mix en unidades.',
        formula='=IFERROR(%s*%s,"")' % (A(P_PZDIA), A(P_DIAS)))
    par(ws, SEC_OTR + 6, 'Packaging sobre el coste de la pieza',
        D.P('packaging_pct_coste'), C.PCT, 'sobre el coste', 'supuesto',
        'En bombonería pesa más que en pastelería: en las campañas de regalo '
        'la caja ES el producto. Es lo que separa el food cost de escandallo '
        'del food cost servido.')
    par(ws, SEC_OTR + 7, 'Tolerancia de las filas de CUADRE', 0.02, C.PCT,
        'desviación', 'supuesto',
        'Por encima de esta desviación, la fila de CUADRE avisa de que lo que '
        'has traído de otro libro ya no es lo que aquel publica.')
    par(ws, SEC_OTR + 8, 'Food cost por encima del cual la hoja avisa', 0.35,
        C.PCT, 'sobre PVP', 'supuesto',
        'Criterio de la casa, no del sector. Una referencia por encima no es '
        'necesariamente mala: puede ser la que trae gente. Pero tiene que ser '
        'una decisión, no un descuido.')
    par(ws, SEC_OTR + 9, 'Rotación mínima para no revisar una referencia', 2.0,
        C.DEC1, '% del mix', 'supuesto',
        'Por debajo de este peso en el mix, la referencia entra en la '
        'decisión de surtido aunque tenga buen margen: ocupa molde, cámara y '
        'cabeza.')
    par(ws, SEC_OTR + 10, 'Merma NO recuperable por encima de la cual avisa',
        0.05, C.PCT, 'sobre la tanda', 'supuesto',
        'La recuperable no dispara nada: vuelve a la cuba. La que se tira, sí.')
    par(ws, SEC_OTR + 11, 'Margen mínimo por pieza', 0.90, C.EUR, 'EUR/pieza',
        'supuesto',
        'Umbral de la decisión de surtido. Es el margen en EUROS, no el '
        'porcentaje: un 70 % sobre una pieza de 0,40 EUR no paga el alquiler.')

    # --- precios de compra -------------------------------------------------
    C.seccion(ws, 'A%d' % SEC_PRE,
              'Precios de compra: la ÚNICA tabla donde se tocan los precios')
    C.encabezados(ws, PRE_CAB, [
        ('A', 'Ingrediente', None),
        ('B', 'Precio de compra SIN IVA (EUR)', None),
        ('C', 'Unidad de compra', None),
        ('D', 'De dónde sale', None),
        ('E', 'Nota', None)], alto=32)
    for i, ing in enumerate(INGREDIENTES):
        fila = PRE_INI + i
        precio, unidad, fuente = D.precio_compra(ing)
        motor.val(ws, 'A%d' % fila, ing)
        if ing in D.COBERTURA_DE_INGREDIENTE:
            k = D.COBERTURA_DE_INGREDIENTE[ing]
            origen = 'B%d' % (COB_INI + COBS.index(k))
            motor.f(ws, 'B%d' % fila, '=%s' % origen, fmt=C.EUR4)
            nota = ('Un concepto, una fuente: el precio de esta cobertura vive '
                    'en el bloque de arriba, que es el que trae la cifra del '
                    'libro 3. No se teclea dos veces.')
        else:
            C.entrada(ws, 'B%d' % fila, precio, fmt=C.EUR4, etiqueta=ing)
            nota = ('SUPUESTO declarado: el research no verificó ningún precio '
                    'de materia prima de relleno. Ponlo de tu albarán.')
        motor.val(ws, 'C%d' % fila, unidad)
        motor.val(ws, 'D%d' % fila, fuente)
        ws['D%d' % fila].font = Font(size=8, color=C.GRIS)
        motor.val(ws, 'E%d' % fila, nota, wrap=True)
        ws['E%d' % fila].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[fila].height = 30

    motor.val(ws, 'A%d' % PAR_PIE, C.VERSION_LINE)
    ws['A%d' % PAR_PIE].font = Font(size=8, italic=True)
    C.setup(ws, landscape=True, titulos='%d:%d' % (PRE_CAB, PRE_CAB))
    return ws


# ==========================================================================
# Hoja «Denominaciones y Mínimos Legales» (D37, dos capas)
# ==========================================================================
def hoja_denominaciones(wb):
    ws = wb.create_sheet(H_DEN)
    C.cabecera_hoja(ws, 'Denominaciones y Mínimos Legales')
    motor.val(ws, 'A3', 'Capa (a): lo que el escandallo SÍ calcula -el 25 % '
                        'sobre el PESO TOTAL, relleno incluido-. Capa (b): las '
                        'tres magnitudes que se COPIAN de la ficha técnica del '
                        'proveedor, porque la bolsa no las trae.')
    ws['A3'].font = Font(italic=True, size=9)

    C.seccion(ws, 'A5', 'Capa (a): el mínimo que sale de tus propios gramajes')
    C.encabezados(ws, FIL_CAB, [
        ('A', 'Id', 8), ('B', 'Referencia', 46), ('C', 'Familia', 24),
        ('D', 'Denominación legal', 34), ('E', 'Fuente verificada', 22),
        ('F', 'Mínimo aplicable', 58), ('G', '¿Obliga la mención «cacao: X % mínimo»?', 18),
        ('H', 'Vía de despacho', 20), ('I', 'Gramos de chocolate', 12),
        ('J', 'Gramos de relleno o materia añadida', 14),
        ('K', 'Peso total de la pieza (g)', 13),
        ('L', 'Chocolate sobre el PESO TOTAL', 15),
        ('M', '¿Le aplica el 25 %?', 13), ('N', 'Veredicto', 36),
        ('O', 'Nota', 70)], alto=62)
    for i, r in enumerate(CARTA):
        fila = FIL_INI + i
        e = FILA_ESC[r['id']]
        motor.val(ws, 'A%d' % fila, r['id'])
        motor.val(ws, 'B%d' % fila, r['nombre'], wrap=True)
        motor.val(ws, 'C%d' % fila, r['familia'])
        motor.val(ws, 'D%d' % fila, r['denominacion_legal'], wrap=True)
        fu = motor.val(ws, 'E%d' % fila, r['fuente_denominacion'])
        ws['E%d' % fila].font = Font(size=8, color=C.GRIS)
        C.nota_celda(ws, fu.coordinate, primer_id(r['fuente_denominacion']))
        motor.val(ws, 'F%d' % fila, r['minimo_legal'], wrap=True)
        ws['F%d' % fila].font = Font(size=8)
        motor.val(ws, 'G%d' % fila, 'Sí' if r['mencion_cacao'] else 'No')
        motor.val(ws, 'H%d' % fila, r['via'])
        motor.f(ws, 'I%d' % fila, '=%sE%d' % (QESC, e), fmt=C.DEC1)
        motor.f(ws, 'J%d' % fila, '=%sF%d' % (QESC, e), fmt=C.DEC1)
        motor.f(ws, 'K%d' % fila, '=%sG%d' % (QESC, e), fmt=C.DEC1)
        motor.f(ws, 'L%d' % fila, '=IFERROR(I%d/K%d,"")' % (fila, fila),
                fmt=C.PCT)
        motor.val(ws, 'M%d' % fila, 'Sí' if D.exige_25_pct(r) else 'No')
        # B10 (refutación 2026-09-12): una caja surtida («Chocolates rellenos
        # surtidos») no entra por el 25 % en su fila -aps. 1.10/1.13 son un
        # mínimo POR PIEZA-: el mensaje se lo dice al lector explícitamente
        # en vez del genérico «no aplica su denominación».
        no_aplica = ('La denominación va por pieza: el 25 %% lo comprueba '
                     'cada bombón en su propia fila, no el agregado de la '
                     'caja' if D.es_caja(r)
                     else 'No aplica: su mínimo es el de su denominación')
        motor.f(ws, 'N%d' % fila,
                '=IF(M%d="No","%s",'
                'IF(NOT(ISNUMBER(L%d)),"",IF(L%d>=%s,"CUMPLE el 25 %% sobre el '
                'peso total","NO CUMPLE: no puede llamarse así")))'
                % (fila, no_aplica, fila, fila, '$B$%d' % (DEN_UMB + 1)))
        motor.val(ws, 'O%d' % fila, r['nota'], wrap=True)
        ws['O%d' % fila].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[fila].height = 54
    motor.semaforo_isnumber(ws, 'L%d:L%d' % (FIL_INI, FIL_FIN),
                            '$L%d' % FIL_INI, '<', '$B$%d' % (DEN_UMB + 1))

    # vía de despacho: las dos columnas de D47
    C.nota_celda(ws, 'H%d' % FIL_CAB, 'CHN-30')
    motor.val(ws, 'A%d' % FIL_TOT,
              'ENVASADO CON ETIQUETA: %s' % D.VIAS_DESPACHO_TEXTO['envasado con etiqueta'],
              wrap=True)
    ws['A%d' % FIL_TOT].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[FIL_TOT].height = 46

    # --- umbrales ----------------------------------------------------------
    C.seccion(ws, 'A%d' % DEN_UMB, 'Los mínimos que usa el semáforo')
    u25 = C.entrada(ws, U_25, D.MINIMO_25_PCT / 100.0, fmt=C.PCT,
                    etiqueta='Chocolate mínimo sobre el peso total')
    motor.val(ws, 'A%d' % (DEN_UMB + 1),
              'Chocolate mínimo sobre el PESO TOTAL del bombón y del chocolate '
              'relleno (aps. 1.10 y 1.13, y la base es el peso total CON el '
              'relleno dentro)', wrap=True)
    C.nota_celda(ws, u25.coordinate, 'CHN-10')
    ws.row_dimensions[DEN_UMB + 1].height = 40
    for coord, etiqueta, valor in (
            (U_TAZA_T, 'Materia seca TOTAL de cacao del chocolate a la taza '
                       '(ap. 1.11)', 0.35),
            (U_TAZA_M, 'Manteca de cacao del chocolate a la taza (ap. 1.11)',
             0.18),
            (U_TAZA_D, 'Materia seca DESGRASADA de cacao del chocolate a la '
                       'taza (ap. 1.11)', 0.14)):
        fila = int(coord[1:])
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
        cel = C.entrada(ws, coord, valor, fmt=C.PCT, etiqueta=etiqueta)
        C.nota_celda(ws, cel.coordinate, 'CHN-05')
        ws.row_dimensions[fila].height = 30

    # --- capa (b) ----------------------------------------------------------
    C.seccion(ws, 'A%d' % CAPB_SEC,
              'Capa (b): las tres magnitudes que la norma pide y la bolsa no '
              'trae. Cópialas de la ficha técnica de tu proveedor')
    ws.row_dimensions[CAPB_SEC].height = 28
    C.encabezados(ws, CAPB_CAB, [
        ('A', 'Cobertura', None),
        ('B', 'Materia seca TOTAL de cacao', None),
        ('C', 'Manteca de cacao', None),
        ('D', 'Materia seca DESGRASADA de cacao', None),
        ('E', '¿Llega a los tres umbrales de materia seca del ap. 1.11?',
         None),
        ('F', 'Qué te dice eso, y qué no', None),
        ('G', 'Nota', None)], alto=48)
    for i, k in enumerate(COBS):
        fila = CAPB_INI + i
        cob = D.COBERTURAS[k]
        motor.val(ws, 'A%d' % fila, cob['nombre'], wrap=True)
        C.entrada(ws, 'B%d' % fila, cob['materia_seca_total_pct'] / 100.0,
                  fmt=C.PCT, etiqueta='Materia seca total de %s' % k)
        C.entrada(ws, 'C%d' % fila, cob['manteca_pct'] / 100.0, fmt=C.PCT,
                  etiqueta='Manteca de %s' % k)
        C.entrada(ws, 'D%d' % fila, cob['desgrasada_pct'] / 100.0, fmt=C.PCT,
                  etiqueta='Materia seca desgrasada de %s' % k)
        motor.f(ws, 'E%d' % fila,
                '=IF(OR(NOT(ISNUMBER(B%d)),NOT(ISNUMBER(C%d)),'
                'NOT(ISNUMBER(D%d))),"",IF(AND(B%d>=$B$%d,C%d>=$B$%d,'
                'D%d>=$B$%d),"Sí","No"))'
                % (fila, fila, fila, fila, DEN_UMB + 2, fila, DEN_UMB + 3,
                   fila, DEN_UMB + 4))
        # El umbral es ARITMÉTICO y la denominación no lo es: llegar a
        # 35/18/14 no convierte una cobertura con leche en «chocolate a la
        # taza», que además tiene su propia composición y su tope de harina o
        # almidón. El veredicto dice lo que el número demuestra y se para ahí.
        motor.f(ws, 'F%d' % fila,
                '=IF(E%d="","",IF(E%d="Sí","Pasa los tres umbrales de materia '
                'seca. Eso NO decide la denominación por sí solo: depende '
                'además de qué lleva (leche, harina o almidón hasta el 8 %%), '
                'y lo confirma la ficha técnica de tu proveedor","No llega a '
                'los tres umbrales: con esta cobertura no puedes ir por esa '
                'denominación"))' % (fila, fila))
        motor.val(ws, 'G%d' % fila, cob['nota'], wrap=True)
        ws['G%d' % fila].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[fila].height = 48

    fila = CAPB_FIN + 2
    motor.val(ws, 'A%d' % fila,
              'Las tres magnitudes de arriba son SUPUESTOS de ejemplo, no un '
              'dato de tu proveedor: la bolsa de una cobertura de marca publica '
              'un solo número («54,5 %») y la norma necesita tres. Es la misma '
              'ficha técnica que te va a pedir el libro de proveedores para el '
              'boletín de cadmio, así que se pide una sola vez.', wrap=True)
    ws['A%d' % fila].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[fila].height = 46

    # B9 (refutación 2026-09-12): las cuatro filas que NOMBRAN el tope del
    # 40 % del ap. 3 (materias comestibles añadidas) sólo lo citaban como
    # texto; aquí SÍ se comprueba, con los mismos gramos de la Capa (a).
    fila += 2
    C.seccion(ws, 'A%d' % fila, 'El tope del 40 % de materias añadidas (ap. 3)')
    fila_umbral = fila + 1
    motor.val(ws, 'A%d' % fila_umbral, 'Tope de materias añadidas del ap. 3',
              bold=True)
    u40 = C.entrada(ws, 'B%d' % fila_umbral,
                    D.TOPE_MATERIA_ANADIDA_PCT / 100.0, fmt=C.PCT,
                    etiqueta='Tope de materias añadidas del ap. 3')
    C.nota_celda(ws, u40.coordinate, 'CHN-09')
    fila_cab = fila_umbral + 2
    C.encabezados(ws, fila_cab, [
        ('A', 'Id', None), ('B', 'Referencia', None),
        ('C', 'Materia añadida sobre el peso total', None),
        ('D', 'Veredicto', None)], alto=24)
    fila_ini_40 = fila_cab + 1
    fila = fila_ini_40
    for r in CARTA:
        if '40 %' not in r['minimo_legal']:
            continue
        e = FILA_ESC[r['id']]
        motor.val(ws, 'A%d' % fila, r['id'])
        motor.val(ws, 'B%d' % fila, r['nombre'], wrap=True)
        motor.f(ws, 'C%d' % fila,
                '=IFERROR(%sF%d/%sG%d,"")' % (QESC, e, QESC, e), fmt=C.PCT)
        motor.f(ws, 'D%d' % fila,
                '=IF(NOT(ISNUMBER(C%d)),"",IF(C%d<=$B$%d,"CUMPLE el tope del '
                '40 %%","NO CUMPLE: revisa el gramaje"))'
                % (fila, fila, fila_umbral))
        fila += 1
    fila_fin_40 = fila - 1
    motor.semaforo_isnumber(ws, 'C%d:C%d' % (fila_ini_40, fila_fin_40),
                            '$C%d' % fila_ini_40, '>', '$B$%d' % fila_umbral)
    fila += 1

    motor.val(ws, 'A%d' % (fila + 2), C.VERSION_LINE)
    ws['A%d' % (fila + 2)].font = Font(size=8, italic=True)
    C.setup(ws, landscape=True, titulos='%d:%d' % (FIL_CAB, FIL_CAB))
    return ws


# ==========================================================================
# Hoja «Escandallo por Molde y Tanda»
# ==========================================================================
def hoja_escandallo(wb):
    ws = wb.create_sheet(H_ESC)
    C.cabecera_hoja(ws, 'Escandallo por Molde y Tanda')
    motor.val(ws, 'A3', 'Arriba, lo que cuesta un kilo de cada relleno. Abajo, '
                        'lo que cuesta una pieza. Las cajas no tienen '
                        'escandallo propio: se componen de sus bombones.')
    ws['A3'].font = Font(italic=True, size=9)

    # --- fórmulas de relleno ----------------------------------------------
    C.seccion(ws, 'A%d' % LIN_SEC,
              'Fórmulas de relleno: cantidad que entra en UN KILO')
    C.encabezados(ws, LIN_CAB, [
        ('A', 'Relleno', 34), ('B', 'Ingrediente', 34),
        ('C', 'Cantidad por kilo', 14), ('D', 'Precio de compra (EUR)', 14),
        ('E', 'Unidad de compra', 14), ('F', 'Coste de la línea (EUR)', 14),
        ('G', 'Nota', 60)], alto=32)
    for i, (clave, ing, cant) in enumerate(LINEAS):
        fila = LIN_INI + i
        motor.val(ws, 'A%d' % fila, clave)
        motor.val(ws, 'B%d' % fila, ing)
        C.entrada(ws, 'C%d' % fila, cant, fmt=C.DEC3,
                  etiqueta='%s: %s por kilo' % (clave, ing))
        motor.f(ws, 'D%d' % fila,
                '=IFERROR(VLOOKUP(B%d,%s,2,FALSE),"")' % (fila, TABLA_PRECIOS),
                fmt=C.EUR4)
        motor.val(ws, 'E%d' % fila, D.PRECIOS_COMPRA[ing][1])
        motor.f(ws, 'F%d' % fila, '=IFERROR(C%d*D%d,"")' % (fila, fila),
                fmt=C.EUR4)
    motor.val(ws, 'G%d' % LIN_INI,
              'Fórmulas de EJEMPLO, declaradas. Este producto NO es un '
              'recetario y no publica curvas de templado: una curva mal '
              'publicada arruina producción. Lo que hacen estas líneas es dar '
              'al libro algo que costear.', wrap=True)
    ws['G%d' % LIN_INI].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[LIN_INI].height = 46

    # --- coste por kilo ----------------------------------------------------
    C.seccion(ws, 'A%d' % REL_SEC,
              'Coste por kilo de cada relleno y de cada materia añadida')
    C.encabezados(ws, REL_CAB, [
        ('A', 'Relleno o materia añadida', None),
        ('B', 'Coste por kilo (EUR)', None),
        ('C', 'Familia de vida útil del kit (se CITA, no se reescribe)', None),
        ('D', 'Plazo orientativo que publica el kit', None),
        ('E', 'Nota', None)], alto=40)
    inicio = LIN_INI
    for i, (clave, datos) in enumerate(RELLENOS):
        fila = REL_INI + i
        n = len(datos['lineas'])
        motor.val(ws, 'A%d' % fila, clave)
        motor.f(ws, 'B%d' % fila,
                '=SUM(F%d:F%d)' % (inicio, inicio + n - 1), fmt=C.EUR4)
        plazo, nota_kit, fuente = D.vida_util_kit_de(datos['familia_kit'])
        motor.val(ws, 'C%d' % fila, datos['familia_kit'], wrap=True)
        motor.val(ws, 'D%d' % fila, plazo)
        motor.val(ws, 'E%d' % fila, datos['nota'], wrap=True)
        ws['E%d' % fila].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[fila].height = 40
        inicio += n
    for j, ing in enumerate(ANADIDOS):
        fila = REL_INI + len(RELLENOS) + j
        motor.val(ws, 'A%d' % fila, ing)
        motor.f(ws, 'B%d' % fila,
                '=IFERROR(VLOOKUP(A%d,%s,2,FALSE),"")' % (fila, TABLA_PRECIOS),
                fmt=C.EUR4)
        motor.val(ws, 'C%d' % fila, 'No es un relleno: es materia comestible '
                                    'añadida del ap. 3', wrap=True)
        motor.val(ws, 'D%d' % fila, 'la de la referencia que la lleva')
        motor.val(ws, 'E%d' % fila,
                  'Va en la misma tabla para que el escandallo busque en un '
                  'solo sitio, lleve relleno o lleve almendra.', wrap=True)
        ws['E%d' % fila].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[fila].height = 32

    # --- escandallo por referencia ----------------------------------------
    C.seccion(ws, 'A%d' % ESC_SEC, 'Escandallo por referencia')
    C.encabezados(ws, ESC_CAB, [
        ('A', 'Id', 8), ('B', 'Referencia', 46), ('C', 'Familia', 24),
        ('D', 'Cobertura', 26), ('E', 'Gramos de chocolate por pieza', 13),
        ('F', 'Gramos de relleno o materia por pieza', 14),
        ('G', 'Peso total de la pieza (g)', 12),
        ('H', 'Relleno o materia añadida', 30),
        ('I', 'Precio de la cobertura (EUR/kg)', 13),
        ('J', 'Coste del chocolate (EUR)', 12),
        ('K', 'Coste por kilo del relleno (EUR)', 13),
        ('L', 'Coste del relleno (EUR)', 12),
        ('M', 'COSTE DE MATERIA SIN MERMA (EUR)', 15),
        ('N', 'Merma NO recuperable', 13),
        ('O', 'COSTE DE MATERIA CON EL RECORTE QUE NO VUELVE (EUR)', 17),
        ('P', 'Procedencia y nota', 70)], alto=62)
    for i, r in enumerate(CARTA):
        fila = ESC_INI + i
        mer = FILA[r['id']]
        motor.val(ws, 'A%d' % fila, r['id'])
        motor.val(ws, 'B%d' % fila, r['nombre'], wrap=True)
        motor.val(ws, 'C%d' % fila, r['familia'])
        if D.es_caja(r):
            col = CAJ_COL[CAJAS.index(r)]
            motor.val(ws, 'D%d' % fila, 'No aplica: caja surtida')
            motor.f(ws, 'E%d' % fila, '=%s%s%d' % (QCAJ, col, F_PCHO),
                    fmt=C.DEC1)
            motor.f(ws, 'F%d' % fila,
                    '=IFERROR(%s%s%d-%s%s%d,"")'
                    % (QCAJ, col, F_PTOT, QCAJ, col, F_PCHO), fmt=C.DEC1)
            motor.f(ws, 'G%d' % fila, '=IFERROR(E%d+F%d,"")' % (fila, fila),
                    fmt=C.DEC1)
            motor.val(ws, 'H%d' % fila, 'Se compone de sus bombones')
            motor.f(ws, 'M%d' % fila, '=%s%s%d' % (QCAJ, col, F_MATSM),
                    fmt=C.EUR4, bold=True)
            nota = ('Una caja no tiene escandallo propio: su coste de materia '
                    'es el de los bombones que lleva dentro, y se calcula en '
                    'la hoja «Unidad vs Caja». Lo que sí tiene propio es la '
                    'merma de montaje y los minutos de montar y lazar.')
        else:
            motor.val(ws, 'D%d' % fila, COB_ING[r['cobertura']])
            C.entrada(ws, 'E%d' % fila, r['g_chocolate'], fmt=C.DEC1,
                      etiqueta='Gramos de chocolate de %s' % r['id'])
            C.entrada(ws, 'F%d' % fila, r['g_relleno'], fmt=C.DEC1,
                      etiqueta='Gramos de relleno de %s' % r['id'])
            motor.f(ws, 'G%d' % fila, '=IFERROR(E%d+F%d,"")' % (fila, fila),
                    fmt=C.DEC1)
            et = etiqueta_relleno(r)
            motor.f(ws, 'I%d' % fila,
                    '=IFERROR(VLOOKUP(D%d,%s,2,FALSE),"")'
                    % (fila, TABLA_PRECIOS), fmt=C.EUR4)
            motor.f(ws, 'J%d' % fila,
                    '=IFERROR(E%d/1000*I%d,"")' % (fila, fila), fmt=C.EUR4)
            if et:
                motor.val(ws, 'H%d' % fila, et)
                motor.f(ws, 'K%d' % fila,
                        '=IFERROR(VLOOKUP(H%d,%s,2,FALSE),"")'
                        % (fila, TABLA_RELLENOS), fmt=C.EUR4)
            else:
                motor.val(ws, 'H%d' % fila, 'No lleva')
                motor.val(ws, 'K%d' % fila, 0.0, fmt=C.EUR4)
            motor.f(ws, 'L%d' % fila,
                    '=IFERROR(F%d/1000*K%d,"")' % (fila, fila), fmt=C.EUR4)
            motor.f(ws, 'M%d' % fila, '=IFERROR(J%d+L%d,"")' % (fila, fila),
                    fmt=C.EUR4, bold=True)
            nota = r['nota']
        motor.f(ws, 'N%d' % fila, '=%sE%d' % (QMER, mer), fmt=C.PCT)
        motor.f(ws, 'O%d' % fila, '=IFERROR(M%d/(1-N%d),"")' % (fila, fila),
                fmt=C.EUR4, bold=True)
        motor.val(ws, 'P%d' % fila, nota, wrap=True)
        ws['P%d' % fila].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[fila].height = 54

    fila = ESC_FIN + 2
    motor.val(ws, 'A%d' % fila, C.VERSION_LINE)
    ws['A%d' % fila].font = Font(size=8, italic=True)
    C.setup(ws, landscape=True, titulos='%d:%d' % (ESC_CAB, ESC_CAB))
    return ws


# ==========================================================================
# Hoja «Merma de Templado y Recortes» (D40, dos tasas)
# ==========================================================================
LITERAL_KIT_MERMA = ('El chocolate sin relleno y sin contaminar se puede '
                     'refundir; el que lleva ganache o fruta, a residuo')


def hoja_merma(wb):
    ws = wb.create_sheet(H_MER)
    C.cabecera_hoja(ws, 'Merma de Templado y Recortes')
    motor.val(ws, 'A3', 'DOS tasas por referencia, y la regla es del kit: «%s» '
                        '(02-partidas-produccion.xlsx!Moldeado). Lo que vuelve '
                        'a la cuba no encarece la materia; lo que se tira, sí.'
              % LITERAL_KIT_MERMA)
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, FIL_CAB, [
        ('A', 'Id', 8), ('B', 'Referencia', 46),
        ('C', '¿Lleva ganache, relleno o fruta?', 16),
        ('D', 'Merma RECUPERABLE (vuelve a la cuba)', 15),
        ('E', 'Merma NO RECUPERABLE (a residuo)', 15),
        ('F', 'Coste de materia sin merma (EUR)', 14),
        ('G', 'Coste real con el recorte que vuelve (EUR)', 16),
        ('H', 'Sobrecoste de la merma (EUR)', 14),
        ('I', 'Sobrecoste sobre el coste', 13),
        ('J', 'Chocolate limpio que vuelve a la cuba (g/pieza)', 15),
        ('K', 'Producto que va a residuo (g/pieza)', 15),
        ('L', 'Unidades al año', 13),
        ('M', 'Kilos al año que vuelven a la cuba', 15),
        ('N', 'Kilos al año a residuo', 14),
        ('O', 'Coste anual de la merma no recuperable (EUR)', 16),
        ('P', 'Nota', 66)], alto=70)
    for i, r in enumerate(CARTA):
        fila = FIL_INI + i
        e = FILA_ESC[r['id']]
        con_relleno = bool(r['relleno']) or D.es_caja(r) or r['id'] in D.ANADIDOS
        motor.val(ws, 'A%d' % fila, r['id'])
        motor.val(ws, 'B%d' % fila, r['nombre'], wrap=True)
        motor.val(ws, 'C%d' % fila, 'Sí' if con_relleno else 'No')
        C.entrada(ws, 'D%d' % fila, r['merma_recuperable_pct'], fmt=C.PCT,
                  etiqueta='Merma recuperable de %s' % r['id'])
        C.entrada(ws, 'E%d' % fila, r['merma_no_recuperable_pct'], fmt=C.PCT,
                  etiqueta='Merma no recuperable de %s' % r['id'])
        motor.f(ws, 'F%d' % fila, '=%sM%d' % (QESC, e), fmt=C.EUR4)
        motor.f(ws, 'G%d' % fila, '=%sO%d' % (QESC, e), fmt=C.EUR4)
        motor.f(ws, 'H%d' % fila, '=IFERROR(G%d-F%d,"")' % (fila, fila),
                fmt=C.EUR4)
        motor.f(ws, 'I%d' % fila, '=IFERROR(H%d/F%d,"")' % (fila, fila),
                fmt=C.PCT)
        motor.f(ws, 'J%d' % fila,
                '=IFERROR(%sE%d*D%d,"")' % (QESC, e, fila), fmt=C.DEC3)
        motor.f(ws, 'K%d' % fila,
                '=IFERROR(%sG%d*E%d,"")' % (QESC, e, fila), fmt=C.DEC3)
        motor.f(ws, 'L%d' % fila, '=%sK%d' % (QMIX, fila), fmt=C.ENT)
        motor.f(ws, 'M%d' % fila, '=IFERROR(J%d*L%d/1000,"")' % (fila, fila),
                fmt=C.DEC1)
        motor.f(ws, 'N%d' % fila, '=IFERROR(K%d*L%d/1000,"")' % (fila, fila),
                fmt=C.DEC1)
        motor.f(ws, 'O%d' % fila, '=IFERROR(H%d*L%d,"")' % (fila, fila),
                fmt=C.EUR)
        motor.val(ws, 'P%d' % fila,
                  'El recorte limpio vuelve a la cuba: no es coste de materia, '
                  'pero hay que volver a templarlo y ese trabajo lo paga la '
                  'mano de obra.' if not con_relleno else
                  'Lleva ganache, relleno o fruta: lo que se recorta va a '
                  'residuo y se reparte entre las piezas que salen bien.',
                  wrap=True)
        ws['P%d' % fila].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[fila].height = 40
    motor.val(ws, 'A%d' % FIL_TOT, 'TOTAL del año', bold=True)
    for col, fmt in (('M', C.DEC1), ('N', C.DEC1), ('O', C.EUR)):
        motor.f(ws, '%s%d' % (col, FIL_TOT),
                '=SUM(%s%d:%s%d)' % (col, FIL_INI, col, FIL_FIN), fmt=fmt,
                bold=True)
    motor.semaforo_isnumber(ws, 'E%d:E%d' % (FIL_INI, FIL_FIN),
                            '$E%d' % FIL_INI, '>', A(P_UMER))

    fila = FIL_TOT + 2
    motor.val(ws, 'A%d' % fila,
              'Los kilos que vuelven a la cuba NO son un ahorro que apuntar en '
              'ningún sitio: son chocolate que ya has pagado y que no vuelves a '
              'pagar. Lo que sí es una decisión es cuánto recortas: si la '
              'columna de residuo se dispara, el problema no es el precio del '
              'cacao, es el molde o la mano.', wrap=True)
    ws['A%d' % fila].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[fila].height = 46
    motor.val(ws, 'A%d' % (fila + 2), C.VERSION_LINE)
    ws['A%d' % (fila + 2)].font = Font(size=8, italic=True)
    C.setup(ws, landscape=True, titulos='%d:%d' % (FIL_CAB, FIL_CAB))
    return ws


# ==========================================================================
# Hoja «Coste Hora y Mano de Obra»
# ==========================================================================
def hoja_mano_obra(wb):
    ws = wb.create_sheet(H_MO)
    C.cabecera_hoja(ws, 'Coste Hora y Mano de Obra')
    motor.val(ws, 'A3', 'La unidad de costeo es la TANDA: piezas por molde por '
                        'moldes por tanda. Los minutos se reparten entre las '
                        'piezas que SALEN BIEN, no entre las que entran.')
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, FIL_CAB, [
        ('A', 'Id', 8), ('B', 'Referencia', 46),
        ('C', 'Piezas por molde', 12), ('D', 'Moldes por tanda', 12),
        ('E', 'Piezas por tanda', 12),
        ('F', 'Minutos de la tanda', 12),
        ('G', 'Piezas buenas por tanda', 13),
        ('H', 'Minutos por pieza buena', 13),
        ('I', 'Coste de mano de obra de la tanda o el montaje (EUR)', 15),
        ('J', 'Coste de mano de obra de las piezas de dentro (EUR)', 15),
        ('K', 'COSTE DE MANO DE OBRA POR PIEZA (EUR)', 15),
        ('L', 'Coste de materia con merma (EUR)', 14),
        ('M', 'COSTE TOTAL POR PIEZA (EUR)', 14),
        ('N', 'PVP con IVA (EUR)', 12), ('O', 'Tipo de IVA', 11),
        ('P', 'PVP sin IVA (EUR)', 12), ('Q', 'Food cost', 11),
        ('R', 'Margen (EUR)', 12), ('S', 'Margen sobre PVP', 11),
        ('T', 'PVP sin IVA que pide tu regla de margen (EUR)', 14),
        ('U', 'PVP con IVA que pide tu regla de margen (EUR)', 14),
        ('V', 'Nota', 60)], alto=70)
    for i, r in enumerate(CARTA):
        fila = FIL_INI + i
        e = FILA_ESC[r['id']]
        caja = D.es_caja(r)
        motor.val(ws, 'A%d' % fila, r['id'])
        motor.val(ws, 'B%d' % fila, r['nombre'], wrap=True)
        C.entrada(ws, 'C%d' % fila, r['piezas_molde'], fmt=C.ENT,
                  etiqueta='Piezas por molde de %s' % r['id'])
        C.entrada(ws, 'D%d' % fila, r['moldes_tanda'], fmt=C.ENT,
                  etiqueta='Moldes por tanda de %s' % r['id'])
        motor.f(ws, 'E%d' % fila, '=C%d*D%d' % (fila, fila), fmt=C.ENT)
        C.entrada(ws, 'F%d' % fila, r['minutos_mo_tanda'], fmt=C.ENT,
                  etiqueta='Minutos de la tanda de %s' % r['id'])
        motor.f(ws, 'G%d' % fila,
                '=IFERROR(E%d*(1-%sE%d),"")' % (fila, QMER, fila), fmt=C.DEC1)
        motor.f(ws, 'H%d' % fila, '=IFERROR(F%d/G%d,"")' % (fila, fila),
                fmt=C.DEC3)
        motor.f(ws, 'I%d' % fila,
                '=IFERROR(H%d/60*%s,"")' % (fila, A(P_CHORA)), fmt=C.EUR4)
        if caja:
            col = CAJ_COL[CAJAS.index(r)]
            motor.f(ws, 'J%d' % fila, '=%s%s%d' % (QCAJ, col, F_MOPZ),
                    fmt=C.EUR4)
            nota = ('Una caja cuesta lo que cuesta montarla MÁS lo que cuesta '
                    'hacer los bombones que lleva. La columna I es sólo el '
                    'montaje; la J trae el trabajo de dentro desde la hoja '
                    '«Unidad vs Caja». Sumar sólo el montaje infla el margen '
                    'de la caja y es el error que hace vender cajas a pérdida.')
        else:
            motor.val(ws, 'J%d' % fila, 0.0, fmt=C.EUR4)
            nota = ('Cero real, no «sin dato»: esta referencia no lleva piezas '
                    'terminadas dentro.')
        motor.f(ws, 'K%d' % fila, '=IFERROR(I%d+J%d,"")' % (fila, fila),
                fmt=C.EUR4, bold=True)
        motor.f(ws, 'L%d' % fila, '=%sO%d' % (QESC, e), fmt=C.EUR4)
        motor.f(ws, 'M%d' % fila, '=IFERROR(K%d+L%d,"")' % (fila, fila),
                fmt=C.EUR4, bold=True)
        C.entrada(ws, 'N%d' % fila, r['pvp_con_iva'], fmt=C.EUR,
                  etiqueta='PVP con IVA de %s' % r['id'])
        iva = P_IVATZ if r['id'] == 'CT3' else P_IVAP
        motor.f(ws, 'O%d' % fila, '=%s' % A(iva), fmt=C.PCT)
        motor.f(ws, 'P%d' % fila,
                '=IFERROR(N%d/(1+O%d),"")' % (fila, fila), fmt=C.EUR4)
        motor.f(ws, 'Q%d' % fila, '=IFERROR(L%d/P%d,"")' % (fila, fila),
                fmt=C.PCT)
        motor.f(ws, 'R%d' % fila, '=IFERROR(P%d-M%d,"")' % (fila, fila),
                fmt=C.EUR4)
        motor.f(ws, 'S%d' % fila, '=IFERROR(R%d/P%d,"")' % (fila, fila),
                fmt=C.PCT)
        motor.f(ws, 'T%d' % fila,
                '=IFERROR(L%d/%s,"")' % (fila, A(P_FC)), fmt=C.EUR4)
        motor.f(ws, 'U%d' % fila,
                '=IFERROR(T%d*(1+O%d),"")' % (fila, fila), fmt=C.EUR4)
        motor.val(ws, 'V%d' % fila, nota, wrap=True)
        ws['V%d' % fila].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[fila].height = 46
    motor.val(ws, 'A%d' % FIL_TOT, 'Media de la carta', bold=True)
    motor.f(ws, 'Q%d' % FIL_TOT,
            '=IFERROR(AVERAGE(Q%d:Q%d),"")' % (FIL_INI, FIL_FIN), fmt=C.PCT,
            bold=True)
    motor.f(ws, 'R%d' % FIL_TOT,
            '=IFERROR(AVERAGE(R%d:R%d),"")' % (FIL_INI, FIL_FIN), fmt=C.EUR4,
            bold=True)
    motor.f(ws, 'S%d' % FIL_TOT,
            '=IFERROR(AVERAGE(S%d:S%d),"")' % (FIL_INI, FIL_FIN), fmt=C.PCT,
            bold=True)
    motor.semaforo_isnumber(ws, 'Q%d:Q%d' % (FIL_INI, FIL_FIN),
                            '$Q%d' % FIL_INI, '>', A(P_UFC))

    fila = FIL_TOT + 2
    motor.val(ws, 'A%d' % fila,
              'La media de la última fila es una media SIMPLE de las 28 '
              'referencias y sirve para ver dispersión, no para decidir: el '
              'food cost que hay que mirar es el ponderado por lo que de verdad '
              'vendes, y ése lo calcula la hoja «Mix y Ticket Medio».',
              wrap=True)
    ws['A%d' % fila].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[fila].height = 40
    motor.val(ws, 'A%d' % (fila + 2), C.VERSION_LINE)
    ws['A%d' % (fila + 2)].font = Font(size=8, italic=True)
    C.setup(ws, landscape=True, titulos='%d:%d' % (FIL_CAB, FIL_CAB))
    return ws


# ==========================================================================
# Hoja «Unidad vs Caja»
# ==========================================================================
#: Precio por bombón que publica el mercado para cada formato (`CHS-29`). La
#: caja de 24 del estuche corporativo no tiene contraste publicado.
CONTRASTE_CHS29 = {'CJ1': 1.67, 'CJ2': 1.40, 'CJ3': 1.29, 'CJ4': None}


def hoja_caja(wb):
    ws = wb.create_sheet(H_CAJ)
    C.cabecera_hoja(ws, 'Unidad vs Caja')
    motor.val(ws, 'A3', 'La caja es la unidad de venta real de una bombonería, '
                        'y por eso tiene hoja propia: el precio por bombón cae '
                        'según crece la caja, y el trabajo de hacer esos '
                        'bombones no desaparece.')
    ws['A3'].font = Font(italic=True, size=9)

    C.seccion(ws, 'A5', 'Qué lleva dentro cada caja')
    cols = [('A', 'Id', 8), ('B', 'Bombón', 46)]
    for j, r in enumerate(CAJAS):
        cols.append((CAJ_COL[j], r['nombre'], 16))
    cols += [('G', 'PVP suelto con IVA (EUR)', 14),
             ('H', 'Coste de materia sin merma (EUR)', 15),
             ('I', 'Coste de mano de obra por pieza (EUR)', 15),
             ('J', 'Nota', 60)]
    C.encabezados(ws, CAJ_CAB, cols, alto=56)
    for i, b in enumerate(BOMBONES):
        fila = CAJ_INI + i
        motor.val(ws, 'A%d' % fila, b['id'])
        motor.val(ws, 'B%d' % fila, b['nombre'], wrap=True)
        for j, caja in enumerate(CAJAS):
            cant = dict(caja['composicion_caja']).get(b['id'], 0)
            C.entrada(ws, '%s%d' % (CAJ_COL[j], fila), cant, fmt=C.ENT,
                      etiqueta='%s en %s' % (b['id'], caja['id']))
        motor.f(ws, 'G%d' % fila, '=%sN%d' % (QMO, FILA[b['id']]), fmt=C.EUR)
        motor.f(ws, 'H%d' % fila, '=%sM%d' % (QESC, FILA_ESC[b['id']]),
                fmt=C.EUR4)
        motor.f(ws, 'I%d' % fila, '=%sK%d' % (QMO, FILA[b['id']]), fmt=C.EUR4)
        ws.row_dimensions[fila].height = 30
    motor.val(ws, 'J%d' % CAJ_INI,
              'Un cero aquí es un cero REAL: ese bombón no entra en esa caja. '
              'Cambia las cantidades y todo lo de abajo se mueve.', wrap=True)
    ws['J%d' % CAJ_INI].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[CAJ_INI].height = 34

    C.seccion(ws, 'A%d' % (CAJ_RES - 1), 'Lo que sale de cada caja')
    for i, etiqueta in enumerate(CAJ_FILAS):
        motor.val(ws, 'A%d' % (CAJ_RES + i), etiqueta, wrap=True)
        ws.row_dimensions[CAJ_RES + i].height = 26
    esc_b = '%s$E$%d:$E$%d' % (QESC, FILA_ESC['BC1'], FILA_ESC['BC10'])
    esc_g = '%s$G$%d:$G$%d' % (QESC, FILA_ESC['BC1'], FILA_ESC['BC10'])
    esc_o = '%s$O$%d:$O$%d' % (QESC, FILA_ESC['BC1'], FILA_ESC['BC10'])
    for j, caja in enumerate(CAJAS):
        col = CAJ_COL[j]
        r_mo = FILA[caja['id']]
        rng = '$%s$%d:$%s$%d' % (col, CAJ_INI, col, CAJ_FIN)
        motor.f(ws, '%s%d' % (col, F_UDS),
                '=SUM(%s%d:%s%d)' % (col, CAJ_INI, col, CAJ_FIN), fmt=C.ENT,
                bold=True)
        motor.f(ws, '%s%d' % (col, F_PCHO),
                '=SUMPRODUCT(%s,%s)' % (rng, esc_b), fmt=C.DEC1)
        motor.f(ws, '%s%d' % (col, F_PTOT),
                '=SUMPRODUCT(%s,%s)' % (rng, esc_g), fmt=C.DEC1)
        motor.f(ws, '%s%d' % (col, F_PCT),
                '=IFERROR(%s%d/%s%d,"")' % (col, F_PCHO, col, F_PTOT),
                fmt=C.PCT)
        motor.f(ws, '%s%d' % (col, F_MATSM),
                '=SUMPRODUCT(%s,$H$%d:$H$%d)' % (rng, CAJ_INI, CAJ_FIN),
                fmt=C.EUR4)
        motor.f(ws, '%s%d' % (col, F_MATCM),
                '=IFERROR(%s%d/(1-%sE%d),"")' % (col, F_MATSM, QMER, r_mo),
                fmt=C.EUR4)
        motor.f(ws, '%s%d' % (col, F_MATSU),
                '=SUMPRODUCT(%s,%s)' % (rng, esc_o), fmt=C.EUR4)
        motor.f(ws, '%s%d' % (col, F_MOPZ),
                '=SUMPRODUCT(%s,$I$%d:$I$%d)' % (rng, CAJ_INI, CAJ_FIN),
                fmt=C.EUR4)
        motor.f(ws, '%s%d' % (col, F_MOMON), '=%sI%d' % (QMO, r_mo),
                fmt=C.EUR4)
        motor.f(ws, '%s%d' % (col, F_COSTE),
                '=IFERROR(%s%d+%s%d+%s%d,"")'
                % (col, F_MATCM, col, F_MOPZ, col, F_MOMON), fmt=C.EUR,
                bold=True)
        motor.f(ws, '%s%d' % (col, F_PVPCI), '=%sN%d' % (QMO, r_mo), fmt=C.EUR)
        motor.f(ws, '%s%d' % (col, F_PVPSI), '=%sP%d' % (QMO, r_mo), fmt=C.EUR)
        motor.f(ws, '%s%d' % (col, F_SUECI),
                '=SUMPRODUCT(%s,$G$%d:$G$%d)' % (rng, CAJ_INI, CAJ_FIN),
                fmt=C.EUR)
        motor.f(ws, '%s%d' % (col, F_SUESI),
                '=IFERROR(%s%d/(1+%sO%d),"")' % (col, F_SUECI, QMO, r_mo),
                fmt=C.EUR)
        motor.f(ws, '%s%d' % (col, F_PBCAJA),
                '=IFERROR(%s%d/%s%d,"")' % (col, F_PVPCI, col, F_UDS),
                fmt=C.EUR)
        motor.f(ws, '%s%d' % (col, F_PBSUE),
                '=IFERROR(%s%d/%s%d,"")' % (col, F_SUECI, col, F_UDS),
                fmt=C.EUR)
        motor.f(ws, '%s%d' % (col, F_DTO),
                '=IFERROR(1-%s%d/%s%d,"")' % (col, F_PBCAJA, col, F_PBSUE),
                fmt=C.PCT)
        contraste = CONTRASTE_CHS29[caja['id']]
        if contraste is None:
            motor.val(ws, '%s%d' % (col, F_CONTR), 'sin dato publicado')
        else:
            cel = motor.val(ws, '%s%d' % (col, F_CONTR), contraste, fmt=C.EUR)
            C.nota_sector(ws, cel.coordinate, 'CHS-29')
        motor.f(ws, '%s%d' % (col, F_MARCA),
                '=IFERROR(%s%d-%s%d,"")' % (col, F_PVPSI, col, F_COSTE),
                fmt=C.EUR, bold=True)
        motor.f(ws, '%s%d' % (col, F_MARSU),
                '=IFERROR(%s%d-%s%d-%s%d,"")'
                % (col, F_SUESI, col, F_MATSU, col, F_MOPZ), fmt=C.EUR)
        motor.f(ws, '%s%d' % (col, F_DIF),
                '=IFERROR(%s%d-%s%d,"")' % (col, F_MARCA, col, F_MARSU),
                fmt=C.EUR, bold=True)
        # Tres ramas, no dos: una caja que deja MENOS que vender sueltos no
        # es necesariamente una caja a pérdida. Fundir los dos casos en «te
        # cuesta dinero» diría que pierdes dinero donde sólo estás haciendo un
        # descuento, y es la clase de veredicto que hace retirar un producto
        # que funciona.
        motor.f(ws, '%s%d' % (col, F_VER),
                '=IF(OR(NOT(ISNUMBER(%s%d)),NOT(ISNUMBER(%s%d))),"",'
                'IF(%s%d<=0,"La caja te cuesta dinero: su margen es cero o '
                'negativo",IF(%s%d>=0,"La caja te gana dinero: deja más que '
                'vender esos bombones sueltos","Ganas MENOS que vendiendo '
                'sueltos: es un descuento, decide si lo quieres")))'
                % (col, F_DIF, col, F_MARCA, col, F_MARCA, col, F_DIF),
                bold=True)
    motor.semaforo_isnumber(ws, '%s%d:%s%d' % (CAJ_COL[0], F_DIF,
                                               CAJ_COL[-1], F_DIF),
                            '%s$%d' % (CAJ_COL[0], F_DIF), '<', '0')

    fila = F_VER + 2
    motor.val(ws, 'A%d' % fila,
              'El contraste de mercado de la fila «EUR por bombón publicado» no '
              'es tu precio: es lo que se ve en el escaparate de otra casa, con '
              'IVA, y baja del formato pequeño al grande. Sirve para saber si tu '
              'descuento por caja se parece al del mercado, no para copiarlo. '
              'Y el estuche corporativo no tiene contraste publicado: se '
              'presupuesta por pedido, con su plazo mínimo de 14 días desde que '
              'el cliente aprueba la muestra.', wrap=True)
    ws['A%d' % fila].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[fila].height = 62
    motor.val(ws, 'A%d' % (fila + 2), C.VERSION_LINE)
    ws['A%d' % (fila + 2)].font = Font(size=8, italic=True)
    ws.column_dimensions['A'].width = 58
    C.setup(ws, landscape=True)
    return ws


# ==========================================================================
# Hoja «Mix y Ticket Medio»
# ==========================================================================
def hoja_mix(wb):
    ws = wb.create_sheet(H_MIX)
    C.cabecera_hoja(ws, 'Mix y Ticket Medio')
    motor.val(ws, 'A3', 'Dos mixes, porque en julio y en agosto no se vende lo '
                        'mismo: el turista no compra ganache, compra souvenir '
                        'que viaja. Los dos tienen que sumar 100 %.')
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, FIL_CAB, [
        ('A', 'Id', 8), ('B', 'Referencia', 46), ('C', 'Familia', 24),
        ('D', 'Mix de todo el año (%)', 13),
        ('E', 'Mix de julio y agosto (%)', 13),
        ('F', 'PVP con IVA (EUR)', 12), ('G', 'PVP sin IVA (EUR)', 12),
        ('H', 'Coste de materia con merma (EUR)', 14),
        ('I', 'Aportación al PVP medio del año (EUR)', 14),
        ('J', 'Aportación al PVP medio de julio y agosto (EUR)', 14),
        ('K', 'Unidades al año', 13), ('L', 'Nota', 62)], alto=60)
    for i, r in enumerate(CARTA):
        fila = FIL_INI + i
        motor.val(ws, 'A%d' % fila, r['id'])
        motor.val(ws, 'B%d' % fila, r['nombre'], wrap=True)
        motor.val(ws, 'C%d' % fila, r['familia'])
        C.entrada(ws, 'D%d' % fila, r['mix_pct'], fmt=C.DEC1,
                  etiqueta='Mix del año de %s' % r['id'])
        C.entrada(ws, 'E%d' % fila, r['mix_verano_pct'], fmt=C.DEC1,
                  etiqueta='Mix de julio y agosto de %s' % r['id'])
        motor.f(ws, 'F%d' % fila, '=%sN%d' % (QMO, fila), fmt=C.EUR)
        motor.f(ws, 'G%d' % fila, '=%sP%d' % (QMO, fila), fmt=C.EUR4)
        motor.f(ws, 'H%d' % fila, '=%sL%d' % (QMO, fila), fmt=C.EUR4)
        motor.f(ws, 'I%d' % fila, '=IFERROR(F%d*D%d/100,"")' % (fila, fila),
                fmt=C.EUR4)
        motor.f(ws, 'J%d' % fila, '=IFERROR(F%d*E%d/100,"")' % (fila, fila),
                fmt=C.EUR4)
        motor.f(ws, 'K%d' % fila,
                '=IFERROR(%s*D%d/100,"")' % (A(P_PZANO), fila), fmt=C.ENT)
        ws.row_dimensions[fila].height = 26
    motor.val(ws, 'A%d' % FIL_TOT, 'TOTAL', bold=True)
    for col, fmt in (('D', C.DEC1), ('E', C.DEC1), ('I', C.EUR4),
                     ('J', C.EUR4), ('K', C.ENT)):
        motor.f(ws, '%s%d' % (col, FIL_TOT),
                '=SUM(%s%d:%s%d)' % (col, FIL_INI, col, FIL_FIN), fmt=fmt,
                bold=True)

    filas = (
        (M_PVPA, 'PVP medio ponderado con IVA (todo el año)', '=I%d' % FIL_TOT,
         C.EUR),
        (M_PVPV, 'PVP medio ponderado con IVA (julio y agosto)',
         '=J%d' % FIL_TOT, C.EUR),
        (M_PZTK, 'Piezas por ticket', '=%s' % A(P_PZTK), C.DEC1),
        (M_TKCI, 'TICKET MEDIO con IVA (todo el año)',
         '=IFERROR(%s*%s,"")' % (M_PVPA, M_PZTK), C.EUR),
        (M_TKSI, 'Ticket medio SIN IVA (todo el año)',
         '=IFERROR(%s/(1+%s),"")' % (M_TKCI, A(P_IVAP)), C.EUR),
        (M_TKVE, 'Ticket medio con IVA (julio y agosto)',
         '=IFERROR(%s*%s,"")' % (M_PVPV, M_PZTK), C.EUR),
        (M_FCA, 'Food cost de escandallo de la carta (todo el año)',
         '=IFERROR(SUMPRODUCT(H%d:H%d,D%d:D%d)/SUMPRODUCT(G%d:G%d,D%d:D%d),"")'
         % (FIL_INI, FIL_FIN, FIL_INI, FIL_FIN, FIL_INI, FIL_FIN, FIL_INI,
            FIL_FIN), C.PCT),
        (M_FCV, 'Food cost de escandallo de la carta (julio y agosto)',
         '=IFERROR(SUMPRODUCT(H%d:H%d,E%d:E%d)/SUMPRODUCT(G%d:G%d,E%d:E%d),"")'
         % (FIL_INI, FIL_FIN, FIL_INI, FIL_FIN, FIL_INI, FIL_FIN, FIL_INI,
            FIL_FIN), C.PCT),
        (M_PACK, 'Packaging sobre el coste de la pieza', '=%s' % A(P_PACK),
         C.PCT),
        (M_FCS, 'FOOD COST SERVIDO (el que va al plan financiero)',
         '=IFERROR(%s*(1+%s),"")' % (M_FCA, M_PACK), C.PCT),
        (M_DIF, 'Diferencia entre el de escandallo y el servido',
         '=IFERROR(%s-%s,"")' % (M_FCS, M_FCA), C.PCT),
        (M_MBA, 'Margen bruto medio con el mix de todo el año',
         '=IFERROR(1-%s,"")' % M_FCA, C.PCT),
        (M_MBV, 'Margen bruto medio con el mix de julio y agosto',
         '=IFERROR(1-%s,"")' % M_FCV, C.PCT),
        (M_CAIDA, 'Caída del margen al cambiar el mix en verano',
         '=IFERROR(%s-%s,"")' % (M_MBV, M_MBA), C.PCT),
    )
    for coord, etiqueta, formula, fmt in filas:
        fila = int(coord[1:])
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
        C.crema(motor.f(ws, coord, formula, fmt=fmt, bold=True))
        ws.row_dimensions[fila].height = 24
    fila = int(M_CUADRE[1:])
    motor.val(ws, 'A%d' % fila, 'Comprobación: los dos mixes suman 100 %',
              bold=True)
    motor.f(ws, M_CUADRE,
            '=IF(OR(NOT(ISNUMBER(D%d)),NOT(ISNUMBER(E%d))),"",'
            'IF(AND(D%d=100,E%d=100),"CUADRAN los dos mixes",'
            '"REVISA: alguno de los dos mixes no suma 100"))'
            % (FIL_TOT, FIL_TOT, FIL_TOT, FIL_TOT), bold=True)

    fila += 2
    motor.val(ws, 'A%d' % fila,
              'El food cost de escandallo y el que llega a la cuenta de '
              'resultados NO coinciden, y está bien: al de la pieza hay que '
              'sumarle el packaging, que en bombonería pesa porque la caja ES '
              'el producto. Esa diferencia es tu colchón, no un error. Y el '
              'ticket medio de aquí es el tuyo: no existe un ticket medio '
              'publicado de chocolatería, así que mídelo con el TPV en dos '
              'semanas y sustitúyelo.', wrap=True)
    ws['A%d' % fila].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[fila].height = 62
    ws.column_dimensions['A'].width = 56
    motor.val(ws, 'A%d' % (fila + 2), C.VERSION_LINE)
    ws['A%d' % (fila + 2)].font = Font(size=8, italic=True)
    C.setup(ws, landscape=True, titulos='%d:%d' % (FIL_CAB, FIL_CAB))
    return ws


# ==========================================================================
# Hoja «Decisión de Surtido»
# ==========================================================================
def hoja_surtido(wb):
    ws = wb.create_sheet(H_SUR)
    C.cabecera_hoja(ws, 'Decisión de Surtido')
    motor.val(ws, 'A3', 'Margen en EUROS por pieza contra rotación. Un 70 % de '
                        'margen sobre una pieza de 0,40 EUR no paga el '
                        'alquiler, y una referencia que no rota ocupa molde, '
                        'cámara y cabeza.')
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, FIL_CAB, [
        ('A', 'Id', 8), ('B', 'Referencia', 46), ('C', 'Familia', 24),
        ('D', 'Margen por pieza (EUR)', 13), ('E', 'Margen sobre PVP', 12),
        ('F', 'Unidades al año', 13), ('G', 'Margen al año (EUR)', 14),
        ('H', 'Peso en el mix (%)', 12),
        ('I', '¿Margen por encima del umbral?', 14),
        ('J', '¿Rotación por encima del umbral?', 14),
        ('K', 'Veredicto', 20), ('L', 'Qué hacer', 66)], alto=56)
    for i, r in enumerate(CARTA):
        fila = FIL_INI + i
        motor.val(ws, 'A%d' % fila, r['id'])
        motor.val(ws, 'B%d' % fila, r['nombre'], wrap=True)
        motor.val(ws, 'C%d' % fila, r['familia'])
        motor.f(ws, 'D%d' % fila, '=%sR%d' % (QMO, fila), fmt=C.EUR4)
        motor.f(ws, 'E%d' % fila, '=%sS%d' % (QMO, fila), fmt=C.PCT)
        motor.f(ws, 'F%d' % fila, '=%sK%d' % (QMIX, fila), fmt=C.ENT)
        motor.f(ws, 'G%d' % fila, '=IFERROR(D%d*F%d,"")' % (fila, fila),
                fmt=C.EUR)
        motor.f(ws, 'H%d' % fila, '=%sD%d' % (QMIX, fila), fmt=C.DEC1)
        motor.f(ws, 'I%d' % fila,
                '=IF(NOT(ISNUMBER(D%d)),"",IF(D%d>=%s,"Sí","No"))'
                % (fila, fila, A(P_UMAR)))
        motor.f(ws, 'J%d' % fila,
                '=IF(NOT(ISNUMBER(H%d)),"",IF(H%d>=%s,"Sí","No"))'
                % (fila, fila, A(P_UMIX)))
        motor.f(ws, 'K%d' % fila,
                '=IF(OR(I%d="",J%d=""),"",IF(AND(I%d="Sí",J%d="Sí"),"%s",'
                'IF(I%d="Sí","%s","%s")))'
                % (fila, fila, fila, fila, VEREDICTOS[0], fila, VEREDICTOS[1],
                   VEREDICTOS[2]))
        motor.val(ws, 'L%d' % fila,
                  'Retirar una referencia de campaña por rotación sería un '
                  'error: no rota todo el año porque sólo se vende unas '
                  'semanas. Léela con el libro de campañas al lado.'
                  if r['familia'] == 'Turrones, figuras y temporada' else
                  'Si sale «Revisar precio», el primer sitio donde mirar es la '
                  'columna del PVP que pide tu regla de margen, en la hoja de '
                  'mano de obra.', wrap=True)
        ws['L%d' % fila].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[fila].height = 34
    motor.val(ws, 'A%d' % FIL_TOT, 'TOTAL', bold=True)
    motor.f(ws, 'G%d' % FIL_TOT,
            '=SUM(G%d:G%d)' % (FIL_INI, FIL_FIN), fmt=C.EUR, bold=True)
    motor.semaforo_texto(ws, 'K%d:K%d' % (FIL_INI, FIL_FIN),
                         ((VEREDICTOS[2], 'FFC7CE', '9C0006'),
                          (VEREDICTOS[1], 'FFEB9C', '9C6500'),
                          (VEREDICTOS[0], 'C6EFCE', '006100')))

    for j, v in enumerate(VEREDICTOS):
        fila = SUR_CNT + j
        motor.val(ws, 'A%d' % fila, 'Referencias con veredicto «%s»' % v)
        motor.f(ws, 'B%d' % fila,
                '=COUNTIF(K%d:K%d,"%s")' % (FIL_INI, FIL_FIN, v), fmt=C.ENT,
                bold=True)
    fila = SUR_CNT + len(VEREDICTOS) + 1
    motor.val(ws, 'A%d' % fila,
              'Los dos umbrales están en «Parámetros» y son criterio de la '
              'casa, no del sector: súbelos o bájalos con tus números. Lo que '
              'no se puede es decidir el surtido con el margen en PORCENTAJE, '
              'que es lo que hace parecer rentable lo que sólo es barato.',
              wrap=True)
    ws['A%d' % fila].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[fila].height = 46
    ws.column_dimensions['A'].width = 46
    motor.val(ws, 'A%d' % (fila + 2), C.VERSION_LINE)
    ws['A%d' % (fila + 2)].font = Font(size=8, italic=True)
    C.setup(ws, landscape=True, titulos='%d:%d' % (FIL_CAB, FIL_CAB))
    return ws


# ==========================================================================
# Mapa de celdas citables
# ==========================================================================
def mapa_celdas():
    m = [
        ('Coste de la hora de obrador', H_PAR, P_CHORA, 'salida'),
        ('Pagas del convenio al año', H_PAR, P_PAGAS, 'parametro'),
        ('Seguridad Social a cargo de la empresa', H_PAR, P_SS, 'parametro'),
        ('IVA del chocolate', H_PAR, P_IVAP, 'parametro'),
        ('IVA del chocolate a la taza servido en sala', H_PAR, P_IVATZ,
         'parametro'),
        ('Food cost objetivo', H_PAR, P_FC, 'entrada'),
        ('Margen bruto objetivo derivado del food cost', H_PAR, P_MB, 'salida'),
        ('Precio de la cobertura negra en base imponible', H_PAR,
         'B%d' % COB_INI, 'entrada'),
        ('Precio de la cobertura de origen en base imponible', H_PAR,
         'B%d' % (COB_INI + 1), 'entrada'),
        ('Desviacion maxima del cuadre del precio de cobertura', H_PAR,
         'B%d' % COB_CUA, 'salida'),
        ('Veredicto del cuadre del precio de cobertura', H_PAR,
         'D%d' % COB_CUA, 'salida'),
        ('Piezas vendidas al dia', H_PAR, P_PZDIA, 'salida'),
        ('Piezas vendidas al ano', H_PAR, P_PZANO, 'salida'),
        ('Packaging sobre el coste de la pieza', H_PAR, P_PACK, 'parametro'),
        ('Chocolate minimo sobre el peso total del bombon', H_DEN, U_25,
         'parametro'),
        ('Materia seca total de cacao del chocolate a la taza', H_DEN,
         U_TAZA_T, 'parametro'),
        ('Coste por kilo de la ganache negra fresca', H_ESC,
         'B%d' % REL_INI, 'salida'),
        ('Kilos al ano que vuelven a la cuba', H_MER, 'M%d' % FIL_TOT,
         'salida'),
        ('Kilos al ano que van a residuo', H_MER, 'N%d' % FIL_TOT, 'salida'),
        ('Coste anual de la merma no recuperable', H_MER, 'O%d' % FIL_TOT,
         'salida'),
        ('Food cost medio simple de la carta', H_MO, 'Q%d' % FIL_TOT, 'salida'),
        ('Margen medio simple por pieza', H_MO, 'R%d' % FIL_TOT, 'salida'),
        ('PVP medio ponderado con IVA del ano', H_MIX, M_PVPA, 'salida'),
        ('Ticket medio con IVA del ano', H_MIX, M_TKCI, 'salida'),
        ('Ticket medio sin IVA del ano', H_MIX, M_TKSI, 'salida'),
        ('Ticket medio con IVA de julio y agosto', H_MIX, M_TKVE, 'salida'),
        ('Food cost de escandallo de la carta', H_MIX, M_FCA, 'salida'),
        ('Food cost de escandallo con el mix de julio y agosto', H_MIX, M_FCV,
         'salida'),
        ('Food cost servido, el que va al plan financiero', H_MIX, M_FCS,
         'salida'),
        ('Margen bruto medio con el mix del ano', H_MIX, M_MBA, 'salida'),
        ('Margen bruto medio con el mix de julio y agosto', H_MIX, M_MBV,
         'salida'),
        ('Caida del margen al cambiar el mix en verano', H_MIX, M_CAIDA,
         'salida'),
        ('Comprobacion de que los dos mixes suman 100', H_MIX, M_CUADRE,
         'salida'),
        ('Margen de la carta al ano', H_SUR, 'G%d' % FIL_TOT, 'salida'),
        ('Referencias con veredicto Mantener', H_SUR, 'B%d' % SUR_CNT,
         'salida'),
        ('Referencias con veredicto Revisar precio', H_SUR,
         'B%d' % (SUR_CNT + 1), 'salida'),
        ('Referencias con veredicto Retirar', H_SUR, 'B%d' % (SUR_CNT + 2),
         'salida'),
    ]
    for r in CARTA:
        fila = FILA[r['id']]
        m.append(('Food cost de %s' % r['nombre'], H_MO, 'Q%d' % fila,
                  'salida'))
        m.append(('Margen por pieza de %s' % r['nombre'], H_MO, 'R%d' % fila,
                  'salida'))
        if D.exige_25_pct(r):
            m.append(('Chocolate sobre el peso total de %s' % r['nombre'],
                      H_DEN, 'L%d' % fila, 'salida'))
    for j, caja in enumerate(CAJAS):
        col = CAJ_COL[j]
        m += [
            ('Coste total de %s' % caja['nombre'], H_CAJ,
             '%s%d' % (col, F_COSTE), 'salida'),
            ('Margen de %s' % caja['nombre'], H_CAJ, '%s%d' % (col, F_MARCA),
             'salida'),
            ('Descuento por comprar %s' % caja['nombre'], H_CAJ,
             '%s%d' % (col, F_DTO), 'salida'),
            ('Precio por bombon en %s' % caja['nombre'], H_CAJ,
             '%s%d' % (col, F_PBCAJA), 'salida'),
            ('Veredicto de %s' % caja['nombre'], H_CAJ, '%s%d' % (col, F_VER),
             'salida'),
        ]
    return m


NOTAS_MAPA = (
    'Libro 4 del pack. Cruce 4 <- 3 (D32): el precio de cada cobertura es una '
    'celda VERDE de «Parámetros» que trae la cifra de '
    'sensibilidad-al-precio-del-cacao.xlsx!Coste de Cobertura por Referencia, '
    'SIEMPRE la de BASE IMPONIBLE y nunca la de base con IVA, con su valor por '
    'defecto declarado y su fila de CUADRE. No hay ni una fórmula entre '
    'ficheros. El 25 % del bombón se calcula SOBRE EL PESO TOTAL con el relleno '
    'dentro (CHN-10, aps. 1.10 y 1.13): invertir la base da un resultado más '
    'favorable que el legal. La merma va en DOS tasas (D40): la recuperable '
    'vuelve a la cuba y no encarece la materia; la no recuperable se reparte '
    'entre las piezas buenas. Frontera con el catálogo (D38): el Kit de '
    'Escandallos tiene hoja de Tarta Chocolate -costea una elaboración por '
    'unidad-; lo que no existe es el escandallo del obrador de bombonería por '
    'molde y tanda, con merma de templado y la caja como unidad de venta.'
)


# ==========================================================================
# Demostraciones con pycel
# ==========================================================================
def demo(ruta):
    from pycel import ExcelCompiler
    ok, fallos = [], []

    def prueba(nombre, cond, detalle=''):
        (ok if cond else fallos).append(nombre + (' - ' + detalle if detalle
                                                  else ''))

    exc = ExcelCompiler(ruta)

    def v(hoja, coord):
        return exc.evaluate("'%s'!%s" % (hoja, coord))

    # 1. El 25 % del bombón se calcula sobre el peso TOTAL, relleno incluido.
    f_bc1 = FILA['BC1']
    pct = v(H_DEN, 'L%d' % f_bc1)
    gch = v(H_ESC, 'E%d' % FILA_ESC['BC1'])
    gre = v(H_ESC, 'F%d' % FILA_ESC['BC1'])
    prueba('el 25 % del bombón se calcula sobre el peso TOTAL, con el relleno '
           'dentro', abs(pct - gch / (gch + gre)) < 1e-6,
           'BC1 da %.4f y el chocolate sobre el peso total es %.4f'
           % (pct, gch / (gch + gre)))

    # 2. Invertir la base (descontar el relleno) daría el 100 %: por eso está
    #    prohibido. Se comprueba que el libro NO publica ese número.
    prueba('el libro no publica el porcentaje calculado descontando el relleno',
           abs(pct - 1.0) > 0.01, 'daría 100 % y el semáforo no vería nada')

    # 3. La merma recuperable NO encarece la materia y la no recuperable SÍ.
    exc2 = ExcelCompiler(ruta)
    e_bc1 = FILA_ESC['BC1']
    antes = exc2.evaluate("'%s'!O%d" % (H_ESC, e_bc1))
    exc2.evaluate("'%s'!D%d" % (H_MER, f_bc1))
    exc2.set_value("'%s'!D%d" % (H_MER, f_bc1), 0.30)
    con_recuperable = exc2.evaluate("'%s'!O%d" % (H_ESC, e_bc1))
    exc3 = ExcelCompiler(ruta)
    exc3.evaluate("'%s'!O%d" % (H_ESC, e_bc1))
    exc3.set_value("'%s'!E%d" % (H_MER, f_bc1), 0.30)
    con_residuo = exc3.evaluate("'%s'!O%d" % (H_ESC, e_bc1))
    prueba('subir la merma RECUPERABLE no encarece la materia, y subir la NO '
           'recuperable sí', abs(con_recuperable - antes) < 1e-9
           and con_residuo > antes + 1e-6,
           'recuperable %.6f -> %.6f · no recuperable %.6f -> %.6f'
           % (antes, con_recuperable, antes, con_residuo))

    # 4. El food cost se calcula con las dos patas en la misma base: si se
    #    usara el PVP con IVA, saldría ~9 % más bajo. Se comprueba la relación.
    q = v(H_MO, 'Q%d' % f_bc1)
    materia = v(H_MO, 'L%d' % f_bc1)
    pvp_si = v(H_MO, 'P%d' % f_bc1)
    pvp_ci = v(H_MO, 'N%d' % f_bc1)
    prueba('el food cost usa el PVP SIN IVA en el denominador',
           abs(q - materia / pvp_si) < 1e-9 and abs(q - materia / pvp_ci) > 1e-4,
           '%.4f con base imponible frente a %.4f con el PVP de mostrador'
           % (q, materia / pvp_ci))

    # 5. La caja incluye la mano de obra de los bombones que lleva dentro.
    col = CAJ_COL[0]
    mo_piezas = v(H_CAJ, '%s%d' % (col, F_MOPZ))
    mo_montaje = v(H_CAJ, '%s%d' % (col, F_MOMON))
    coste = v(H_CAJ, '%s%d' % (col, F_COSTE))
    materia_caja = v(H_CAJ, '%s%d' % (col, F_MATCM))
    prueba('el coste de la caja incluye la mano de obra de sus bombones',
           mo_piezas > mo_montaje
           and abs(coste - (materia_caja + mo_piezas + mo_montaje)) < 1e-6,
           'montaje %.4f EUR frente a %.4f EUR de las piezas de dentro'
           % (mo_montaje, mo_piezas))

    # 6. El CUADRE del precio de cobertura avisa al alejarse del libro 3.
    exc4 = ExcelCompiler(ruta)
    exc4.evaluate("'%s'!D%d" % (H_PAR, COB_CUA))
    cuadra = exc4.evaluate("'%s'!D%d" % (H_PAR, COB_CUA))
    exc4.set_value("'%s'!B%d" % (H_PAR, COB_INI), 40.0)
    revisa = exc4.evaluate("'%s'!D%d" % (H_PAR, COB_CUA))
    prueba('la fila de CUADRE avisa si el precio traído se aleja del libro 3',
           cuadra == 'CUADRA' and revisa.startswith('REVISA'),
           'antes %r, después %r' % (cuadra, revisa))

    # 7. Los dos mixes suman 100 y el veredicto lo dice.
    cu = v(H_MIX, M_CUADRE)
    prueba('los dos mixes suman 100 % en el ejemplo publicado',
           cu.startswith('CUADRAN'), 'devuelve %r' % (cu,))

    return ok, fallos


# ==========================================================================
def main():
    D.gate_legal()
    if len(CARTA) != 28:
        raise SystemExit('La carta tiene %d referencias y la SPEC firma 28'
                         % len(CARTA))
    for familia, n in D.FAMILIAS_ESPERADO.items():
        reales = len(D.por_familia(familia))
        if reales != n:
            raise SystemExit('La familia «%s» tiene %d referencias y la SPEC '
                             'firma %d' % (familia, reales, n))
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_parametros(wb)
    hoja_denominaciones(wb)
    hoja_escandallo(wb)
    hoja_merma(wb)
    hoja_mano_obra(wb)
    hoja_caja(wb)
    hoja_mix(wb)
    hoja_surtido(wb)

    res = C.cerrar(wb, NOMBRE, TITULO, mapa_celdas(), NOTAS_MAPA)

    print('escrito: %s' % res['ruta'])
    print('hojas: %d · fórmulas: %d · celdas verdes: %d · verdes vacías: %d'
          % (res['hojas'], res['formulas'], res['verdes'],
             len(res['verdes_vacias'])))
    print('fórmulas que devuelven «sin dato» a propósito: %d' % res['sin_dato'])
    print('notas legales: %d · etiquetas en el mapa: %d'
          % (res['notas_legales'], res['mapa']))
    print('celdas «trae aquí la cifra de»: %d · filas de CUADRE: %d'
          % (res['trae'], res['cuadre']))
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
