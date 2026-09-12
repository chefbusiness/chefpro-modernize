#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_carta-de-apertura-y-escandallo.py — libro 4 de «Cómo Montar una Pastelería»
(SPEC §2.2 fila 4; decisiones D10, D11, D17, D21 y D23; reglas R3 y R4).

Hojas: Instrucciones · Parámetros · Escandallo por Tanda · Coste Hora y Mano de
Obra · Decisión de Huevo y Temperatura · Mix y Ticket Medio · Decisión de
Surtido.

QUÉ DECIDE ESTE LIBRO
---------------------
Qué vendes, a cuánto, y con qué vía legal de huevo — con su temperatura y su
plazo. La unidad de costeo es la TANDA, no la pieza, y la mano de obra entra
dentro: es lo que separa un escandallo de una lista de la compra.

DECISIONES TÉCNICAS
-------------------
* **D23, regla ÚNICA de margen.** «Parámetros» pide UN número, el food cost
  objetivo, y DERIVA de él el margen bruto objetivo. En ningún sitio se piden
  los dos: margen bruto y food cost son la misma regla dicha dos veces.
* **D11 y D10, dos salidas separadas y cada una con su artículo.** La
  temperatura es el MÍNIMO de los techos que apliquen —fila 9 del art. 4.1 y
  art. 9.3 del RD 1021/2022— y la hoja dice cuál manda; el «Plazo legal
  (art. 9.3)» es 24' + horas o «No aplica». No hay «conflicto 4/8 °C»: son dos
  techos distintos. La «Vida útil declarada por ti» es celda verde y el libro
  NO la calcula para ninguna de las 30 referencias.
* **El coste hora de obrador se CALCULA** desde la plantilla y el convenio
  (bruto por pagas por jornada, más Seguridad Social, dividido por las horas
  productivas). No es un dato del sector y no se teclea.
* **Los precios de compra viven en UNA sola tabla** («Parámetros», bloque
  «Precios de compra»): cada línea del escandallo los lee con `VLOOKUP` exacto.
  Cambiar el precio de la mantequilla cambia las trece referencias que la usan.
* Los agregados por referencia van con `SUMPRODUCT(--(rango=celda), …)`, nunca
  con `SUMIF` sobre una celda-criterio: pycel evalúa los dos brazos del `IF` de
  forma ansiosa y una fila vacía dejaba el libro entero sin caché.
  `COUNTIF` sólo con etiqueta FIJA.
* Cero constantes dentro de fórmulas; `IFERROR(...,"")` en toda división;
  «sin dato» = `""`; semáforos con `ISNUMBER`; DV contra RANGO. Prohibidas
  INDIRECT, COUNTA, PMT, OFFSET, XLOOKUP, LET, LAMBDA, RANK, NETWORKDAYS e
  IRR: cero usos.

FRONTERAS (SPEC §2.3), escritas en «Instrucciones»
--------------------------------------------------
* **R3** — aquí NO hay declaración de alérgenos: la de vitrina es el
  `12-control-alergenos-vitrina.xlsx` del Kit de Tareas Pastelería y la de carta
  es el `08` del `pack-appcc`. Nunca dos declaraciones completas en el mismo
  catálogo.
* **R4** — aquí NO se rehacen las vidas útiles ni el registro de temperaturas:
  eso es el `13-registro-temperaturas-recepcion.xlsx` del kit. Lo que sí es
  nuestro, y no existe en ningún fichero del catálogo, es la hoja de DECISIÓN
  de huevo y temperatura.
* El escandallo unitario de tres elaboraciones es `kit-escandallos/05-pasteleria.xlsx`
  y el método de costeo por lote es el capítulo 17 de la Guía Food Cost. Las
  tres referencias que comparten con este libro llevan el MISMO escandallo,
  copiado y declarado, nunca vinculado.

Salida fija: build/carta-de-apertura-y-escandallo.xlsx + su mapa.
Uso: /usr/local/bin/python3 gen_carta-de-apertura-y-escandallo.py
Via: Claude Code
"""
import os
import sys

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Font, PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import _comun_libros_3_4 as C                                  # noqa: E402
import datos_ejemplo as D                                      # noqa: E402
import motor                                                   # noqa: E402

NOMBRE = 'carta-de-apertura-y-escandallo'
TITULO = 'Carta de Apertura y Escandallo por Tanda'

H_INS = 'Instrucciones'
H_PAR = 'Parámetros'
H_ESC = 'Escandallo por Tanda'
H_MO = 'Coste Hora y Mano de Obra'
H_HUE = 'Decisión de Huevo y Temperatura'
H_MIX = 'Mix y Ticket Medio'
H_SUR = 'Decisión de Surtido'

QPAR = "'" + H_PAR + "'!"
QESC = "'" + H_ESC + "'!"
QMO = "'" + H_MO + "'!"
QMIX = "'" + H_MIX + "'!"

NR = len(D.CARTA)                                # 30
LINEAS = [(r, l) for r in D.CARTA for l in r['lineas']]
NL = len(LINEAS)                                 # 226

# --- Parámetros: filas ------------------------------------------------------
PER_CAB = 5
PER_INI = 6
PERSONAL = [p for p in D.PLANTILLA if p[4] == 'OBRADOR']
PER_FIN = PER_INI + len(PERSONAL) - 1
PER_TOT = PER_FIN + 1

P_PAGAS = 'B%d' % (PER_TOT + 2)
P_SS = 'B%d' % (PER_TOT + 3)
P_HANIO = 'B%d' % (PER_TOT + 4)
P_RATIO = 'B%d' % (PER_TOT + 5)
P_HPROD = 'B%d' % (PER_TOT + 6)
P_CHORA = 'B%d' % (PER_TOT + 7)

SEC_IVA = PER_TOT + 9
P_IVAP = 'B%d' % (SEC_IVA + 1)
P_IVAPAN = 'B%d' % (SEC_IVA + 2)
P_IVADEG = 'B%d' % (SEC_IVA + 3)

SEC_MAR = SEC_IVA + 5
P_FC = 'B%d' % (SEC_MAR + 1)
P_MB = 'B%d' % (SEC_MAR + 2)

SEC_LEG = SEC_MAR + 4
P_T41 = 'B%d' % (SEC_LEG + 1)
P_T93 = 'B%d' % (SEC_LEG + 2)
P_PLAZO = 'B%d' % (SEC_LEG + 3)
P_GLUTEN = 'B%d' % (SEC_LEG + 4)

SEC_OTR = SEC_LEG + 6
P_MERMA = 'B%d' % (SEC_OTR + 1)
P_PACK = 'B%d' % (SEC_OTR + 2)
P_PIEZAS = 'B%d' % (SEC_OTR + 3)
P_UMBRAL = 'B%d' % (SEC_OTR + 4)

SEC_PRE = SEC_OTR + 6
PRE_CAB = SEC_PRE + 1
PRE_INI = PRE_CAB + 1
INGREDIENTES = sorted(D.PRECIOS_COMPRA)
PRE_FIN = PRE_INI + len(INGREDIENTES) - 1
PRE_PIE = PRE_FIN + 2

TABLA_PRECIOS = '%s$A$%d:$C$%d' % (QPAR, PRE_INI, PRE_FIN)

# --- Escandallo -------------------------------------------------------------
ESC_CAB = 5
ESC_INI = 6
ESC_FIN = ESC_INI + NL - 1
ESC_TOT = ESC_FIN + 1

RES_CAB = ESC_TOT + 3
RES_INI = RES_CAB + 1
RES_FIN = RES_INI + NR - 1
RES_TOT = RES_FIN + 1

# --- Resto de hojas ---------------------------------------------------------
MO_CAB, MO_INI = 5, 6
MO_FIN = MO_INI + NR - 1
MO_TOT = MO_FIN + 1

HU_CAB, HU_INI = 5, 6
HU_FIN = HU_INI + NR - 1
HU_RES = HU_FIN + 3
HU_LIS = HU_RES + 12

MX_CAB, MX_INI = 5, 6
MX_FIN = MX_INI + NR - 1
MX_TOT = MX_FIN + 1
MX_RES = MX_TOT + 2

SU_CAB, SU_INI = 5, 6
SU_FIN = SU_INI + NR - 1
SU_TOT = SU_FIN + 1
SU_RES = SU_TOT + 2

VEREDICTOS = ('Mantener', 'Revisar precio', 'Retirar')
SI_NO = ('Sí', 'No')

A = lambda coord: QPAR + '$' + coord[0] + '$' + coord[1:]      # noqa: E731

#: Las tres que se copian EXACTAS del kit de escandallos (SPEC §3).
COPIADAS = dict((i, h) for i, h in D.COPIADAS_DEL_KIT)


def procedencia(ref):
    if ref['id'] in COPIADAS:
        return ('COPIA EXACTA de kit-escandallos/05-pasteleria.xlsx, hoja «%s». '
                'Mismo escandallo en los dos productos: un cliente con los dos '
                'no puede ver dos costes distintos de la misma pieza.'
                % COPIADAS[ref['id']])
    return ref['fuente_escandallo']


# --------------------------------------------------------------------------
# Hoja «Instrucciones»
# --------------------------------------------------------------------------
PASOS = [
    '1. Hoja «Parámetros»: empieza por el bloque de personal de obrador. El '
    'coste hora de obrador NO es un dato del sector y no se teclea: se calcula '
    'con el bruto de tu convenio, las pagas, la jornada de cada persona y la '
    'Seguridad Social a cargo de la empresa. Debajo están los precios de '
    'compra, uno por ingrediente: es la única tabla donde se tocan los precios '
    'y de ella beben las 226 líneas del escandallo.',
    '2. Hoja «Escandallo por Tanda»: una fila por ingrediente y por '
    'referencia. La unidad de costeo es LA TANDA, no la pieza: es como se '
    'trabaja en un obrador y es la única forma de que la mano de obra cuadre. '
    'Escribe la cantidad neta que usas, el factor que convierte la unidad de '
    'compra en la de uso (12 para pasar de docena a unidad, 1 si coinciden) y '
    'la merma. El coste de la línea sale solo.',
    '3. Hoja «Coste Hora y Mano de Obra»: los minutos que te lleva cada tanda '
    'y el precio de venta. De ahí salen el coste de mano de obra por pieza, el '
    'coste total, el food cost y el margen en euros. Es el capítulo que enseña '
    'a dejar de regalar tu trabajo.',
    '4. Hoja «Decisión de Huevo y Temperatura»: para cada referencia, elige la '
    'vía legal del huevo, di si va rellena y si el producto terminado es '
    'estable a temperatura ambiente. El libro devuelve la temperatura de '
    'conservación, cuál de los dos artículos manda y el plazo legal del '
    'art. 9.3. La vida útil la declaras tú.',
    '5. Hoja «Mix y Ticket Medio»: reparte el 100' + C.N + '% de tus unidades '
    'entre las 30 referencias. De ahí sale tu ticket medio, que no se copia de '
    'ningún estudio porque no existe un ticket medio publicado de pastelería.',
    '6. Hoja «Decisión de Surtido»: cruza margen y rotación y te dice qué '
    'mantener, a qué revisarle el precio y qué retirar. Repásala a los tres '
    'meses de abrir, con ventas reales, y otra vez al cambiar de temporada.',
]

NOTAS_LIBRO = [
    'LA REGLA DEL MARGEN ES UNA SOLA, DICHA DE DOS FORMAS. Margen bruto del '
    '65-70' + C.N + '% y food cost del 30-35' + C.N + '% son el mismo número '
    'visto del derecho y del revés: si el food cost es el 32' + C.N + '%, el '
    'margen bruto es el 68' + C.N + '%. Por eso «Parámetros» te pide UNO y '
    'calcula el otro. Cualquier herramienta que te pida los dos te va a dejar '
    'ponerlos incoherentes.',
    'NO HAY NINGÚN «CONFLICTO 4/8' + C.N + '°C». Son dos techos distintos del '
    'mismo Real Decreto y manda el más bajo de los que te apliquen. La fila 9 '
    'del art. 4.1 pone 4' + C.N + '°C a los productos de pastelería RELLENOS '
    'salvo que sean estables a temperatura ambiente. El art. 9.3 pone '
    '8' + C.N + '°C a lo elaborado por la vía del art. 9.1.a) que no sea '
    'estable y a lo hecho con ovoproducto. Si te aplican los dos, mandan los '
    '4' + C.N + '°C. Y lo que casi nadie cuenta: el art. 9.3 obliga además a '
    'consumir en 24 horas y a REGISTRAR la fecha y la hora de elaboración.',
    'LA VIDA ÚTIL NO LA CALCULA ESTE LIBRO, Y NINGÚN LIBRO PUEDE. El '
    'RD 1021/2022 no la establece: la fijas tú, con tu proceso y tus '
    'analíticas, y tiene que constar en tu plan de APPCC. Lo que sí es legal y '
    'está en la hoja es el PLAZO del art. 9.3, que es otra cosa y va en su '
    'propia columna.',
    'DÓNDE ESTÁN LOS ALÉRGENOS, QUE AQUÍ NO ESTÁN. La declaración de vitrina es '
    'el «12-control-alergenos-vitrina.xlsx» del Kit de Tareas Pastelería '
    '(12' + C.N + '€) y la de carta es el «08» del Pack APPCC (14' + C.N + '€). '
    'Este libro lleva una sola fila de checklist -«matriz de alérgenos '
    'publicada antes de abrir»- y no repite ninguna de las dos: nunca dos '
    'declaraciones completas de alérgenos en el mismo catálogo.',
    'DÓNDE ESTÁN LAS TEMPERATURAS DIARIAS, QUE AQUÍ TAMPOCO. El registro de '
    'temperaturas y vidas útiles es el «13-registro-temperaturas-recepcion.xlsx» '
    'del mismo kit. Lo que hace este libro es la DECISIÓN previa: qué vía legal '
    'eliges para cada elaboración y qué temperatura te obliga esa elección. Eso '
    'no está en ningún fichero del catálogo.',
    'EL ESCANDALLO UNITARIO Y EL MÉTODO. Si quieres la ficha de escandallo '
    'unitaria de tres elaboraciones, es el '
    '«kit-escandallos/05-pasteleria.xlsx»; si quieres el método de costeo por '
    'lote y la ingeniería de menú, es la Guía Food Cost (capítulo 17 y '
    'capítulos 1 a 16). Tarta de chocolate 70' + C.N + '%, croissants y '
    'macarons llevan aquí el MISMO escandallo que el kit: copiado y declarado, '
    'nunca vinculado. Un cliente con los dos productos no puede ver dos costes '
    'distintos del mismo croissant.',
    'EL FOOD COST DEL ESCANDALLO Y EL DEL PLAN FINANCIERO NO COINCIDEN, Y ESTÁ '
    'BIEN. El de la pieza sólo cuenta materia prima. Al que llega a la cuenta '
    'de resultados hay que sumarle la merma real, el packaging, el producto de '
    'terceros que revende el despacho y la subida de la materia prima. La hoja '
    '«Mix y Ticket Medio» calcula los dos y enseña la diferencia: ése es tu '
    'colchón, no un error.',
    'LOS PRECIOS DE COMPRA DEL EJEMPLO SON DE UN OBRADOR MODELADO. Los '
    'diecinueve primeros son copia exacta del kit de escandallos; el resto son '
    'supuestos plausibles de compra profesional en España en 2026. Bórralos y '
    'pon tus albaranes: un escandallo con precios de otro no vale nada.',
]

CADENCIA = ('Cada cuánto se usa este libro: los precios de compra, CADA VEZ que '
            'te suba un proveedor, y como mínimo una vez al trimestre. El '
            'escandallo y los minutos de mano de obra, al montar la carta y '
            'cada vez que cambies un proceso. La decisión de huevo y '
            'temperatura, UNA VEZ por referencia y siempre que añadas una '
            'nueva: es la que decide cuántos metros de vitrina refrigerada '
            'necesitas. El mix, el ticket medio y la decisión de surtido, a '
            'los tres meses de abrir y luego cada temporada.')


def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS, 0)
    ws.column_dimensions['A'].width = 90.0   # hallazgo A11b (2026-09-10): tope 90
    C.cabecera_hoja(ws, TITULO)
    motor.val(ws, 'A3', 'Para qué sirve: decidir qué vendes, a cuánto, y con '
                        'qué vía legal de huevo -con su temperatura y su plazo-.')
    ws['A3'].font = Font(italic=True, size=9)

    C.seccion(ws, 'A5', 'Instrucciones de uso')
    fila = 6
    for paso in PASOS:
        motor.val(ws, 'A%d' % fila, paso, wrap=True)
        ws.row_dimensions[fila].height = 62
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, C.LEYENDA_VERDE, verde_=True)
    C.VERDES.append((H_INS, 'A%d' % fila, 'Leyenda de celdas verdes',
                     C.LEYENDA_VERDE))
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Lo que conviene saber antes de empezar')
    fila += 1
    for nota in NOTAS_LIBRO:
        motor.val(ws, 'A%d' % fila, nota, wrap=True)
        ws.row_dimensions[fila].height = 72
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, CADENCIA, wrap=True)
    ws.row_dimensions[fila].height = 58
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


# --------------------------------------------------------------------------
# Hoja «Parámetros»
# --------------------------------------------------------------------------
def par(ws, fila, etiqueta, valor, fmt, unidad, fuente, nota, formula=None,
        id_pa=None):
    motor.val(ws, 'A%d' % fila, etiqueta, wrap=True)
    if formula is not None:
        cel = C.crema(motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=True))
    else:
        cel = C.entrada(ws, 'B%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
    motor.val(ws, 'C%d' % fila, unidad)
    motor.val(ws, 'D%d' % fila, fuente)
    ws['D%d' % fila].font = Font(size=8, color=C.GRIS)
    motor.val(ws, 'G%d' % fila, nota, wrap=True)
    ws['G%d' % fila].font = Font(size=8, color=C.GRIS)
    ws.row_dimensions[fila].height = 42
    if id_pa:
        C.nota_celda(ws, cel.coordinate, id_pa)
    return cel


def hoja_parametros(wb):
    ws = wb.create_sheet(H_PAR)
    C.cabecera_hoja(ws, 'Parámetros')
    for letra, ancho in (('A', 46), ('B', 15), ('C', 14), ('D', 17), ('E', 15),
                         ('F', 15), ('G', 78)):
        ws.column_dimensions[letra].width = ancho
    motor.val(ws, 'A3', 'El coste hora de obrador se CALCULA aquí desde tu '
                        'plantilla y tu convenio. No es un dato del sector.')
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, PER_CAB, [
        ('A', 'Personal de obrador', None), ('B', 'Jornada', None),
        ('C', 'Grupo de convenio', None),
        ('D', 'Bruto mensual del convenio (€)', None),
        ('E', 'Bruto anual con las pagas (€)', None),
        ('F', 'Coste de empresa anual con SS (€)', None),
        ('G', 'Nota', None)], alto=40)

    for i, (pid, perfil, jornada, grupo, _area, _h, turno) in enumerate(PERSONAL):
        r = PER_INI + i
        motor.val(ws, 'A%d' % r, '%s (%s)' % (perfil, pid))
        C.entrada(ws, 'B%d' % r, jornada, fmt=C.DEC,
                  etiqueta='Jornada de %s' % perfil)
        motor.val(ws, 'C%d' % r, '%d · %s' % (grupo, D.CONVENIO[grupo - 1][1]))
        cel = C.entrada(ws, 'D%d' % r, D.CONVENIO[grupo - 1][2], fmt=C.EUR,
                        etiqueta='Bruto mensual de %s' % perfil)
        C.nota_celda(ws, cel.coordinate, 'PA-33')
        motor.f(ws, 'E%d' % r, '=IFERROR(D{r}*{p},"")'.format(r=r, p=A(P_PAGAS)),
                fmt=C.EUR)
        motor.f(ws, 'F%d' % r,
                '=IFERROR(E{r}*B{r}*(1+{s}),"")'.format(r=r, s=A(P_SS)),
                fmt=C.EUR)
        motor.val(ws, 'G%d' % r, 'Turno: %s. Sólo el área OBRADOR entra en el '
                                 'coste hora: el despacho no fabrica.' % turno,
                  wrap=True)
        ws['G%d' % r].font = Font(size=8, color=C.GRIS)

    motor.val(ws, 'A%d' % PER_TOT, 'TOTAL OBRADOR', bold=True)
    C.crema(motor.f(ws, 'B%d' % PER_TOT,
                    '=SUM(B{a}:B{b})'.format(a=PER_INI, b=PER_FIN), fmt=C.DEC,
                    bold=True))
    C.crema(motor.f(ws, 'F%d' % PER_TOT,
                    '=SUM(F{a}:F{b})'.format(a=PER_INI, b=PER_FIN), fmt=C.EUR,
                    bold=True))
    # A16 (2026-09-10): la fila del total viaja al libro dentro de la tabla que
    # explica el coste hora, y sin unidad ni origen se leía «TOTAL OBRADOR |
    # 2,50 | | ». Son jornadas equivalentes, y salen de sumar los tres perfiles.
    motor.val(ws, 'C%d' % PER_TOT, 'jornadas', bold=True)
    motor.val(ws, 'D%d' % PER_TOT, 'suma de los tres perfiles', bold=True)

    f = PER_TOT + 2
    par(ws, f, 'Pagas del convenio al año', D.CONVENIO_PAGAS, C.ENT, 'pagas',
        D.FUENTE_CONVENIO,
        'El convenio de la Comunidad de Madrid (código %s, revisión 2026 en el '
        '%s) paga 15, no 14. Sustitúyelo por el de tu convenio provincial.'
        % (D.CONVENIO_CODIGO, D.CONVENIO_PUBLICACION), id_pa='PA-33')
    par(ws, f + 1, 'Seguridad Social a cargo de la empresa', D.P('ss_empresa'),
        C.PCT, 'sobre bruto', 'motor.PARAMETROS',
        'Cotización empresarial aproximada sobre el bruto: contingencias '
        'comunes, desempleo, FOGASA y formación. Es el renglón que convierte '
        'un bruto en un coste, y el que más sorprende.')
    par(ws, f + 2, 'Horas anuales de contrato', D.P('horas_anuales_contrato'),
        C.ENT, 'horas/año', 'supuesto',
        '40 horas por 52 semanas son 2.080, menos 30 días naturales de '
        'vacaciones y los festivos del calendario laboral.')
    par(ws, f + 3, 'Horas productivas sobre la jornada',
        D.P('ratio_horas_productivas'), C.PCT, 'de la jornada', 'supuesto',
        'Parte de la jornada que se pasa a pie de mesa. El resto es recepción, '
        'limpieza, formación y reuniones: horas que pagas y no producen.')
    par(ws, f + 4, 'Horas productivas del obrador al año', None, C.ENT,
        'horas/año', 'calculado',
        'Jornadas de obrador por horas anuales de contrato por el ratio '
        'productivo.',
        formula='=IFERROR($B${t}*{h}*{r},"")'.format(t=PER_TOT, h=A(P_HANIO),
                                                     r=A(P_RATIO)))
    # Hallazgo B7 (2026-09-10): el pack publica tres costes por hora distintos
    # para la misma plantilla (17,94 aquí; 14,89 en plantilla-turnos; 13,36 en
    # estacionalidad), los tres bien calculados pero midiendo cosas distintas.
    # El título deja el denominador explícito para que un lector que salte de
    # libro no los confunda.
    par(ws, f + 5, 'COSTE HORA PRODUCTIVA DE OBRADOR', None, C.EUR, '€/hora',
        'calculado',
        'Coste de empresa anual del obrador dividido por sus horas '
        'PRODUCTIVAS (con el factor de %.0f %% de más arriba). Éste es el '
        'número que hay que meter en cada tanda, y el que casi nadie imputa. '
        'NO lo confundas con el «coste medio por hora PAGADA de la plantilla» '
        'del libro 8 (14,89 €, plantilla-turnos-y-coste-personal.xlsx) ni con '
        'el «coste por hora PAGADA del refuerzo» del libro 3 (13,36 €, '
        'estacionalidad-y-picos.xlsx): las tres son correctas y las tres '
        'miden un denominador distinto.'
        % (D.P('ratio_horas_productivas') * 100),
        formula='=IFERROR($F${t}/{h},"")'.format(t=PER_TOT, h=A(P_HPROD)))

    C.seccion(ws, 'A%d' % SEC_IVA, 'IVA por familia de producto')
    par(ws, SEC_IVA + 1, 'IVA de pastelería, bollería y confitería',
        D.P('iva_producto'), C.PCT, 'sobre base', 'PA-36',
        'Regla general de alimentos del art. 91.Uno.1.1.º de la Ley 37/1992: '
        'no porque un precepto los nombre, sino porque no están en la lista '
        'cerrada del 4' + C.N + '% ni excluidos del 10' + C.N + '%.',
        id_pa='PA-36')
    par(ws, SEC_IVA + 2, 'IVA del pan del RD 308/2019', D.P('iva_pan'), C.PCT,
        'sobre base', 'PA-36b',
        'Todos los productos del RD 308/2019 -pan común, pan especial y '
        'semielaborados, con o sin gluten- van al 4' + C.N + '% desde la '
        'Resolución vinculante de la DGT de 24-02-2025, que acoge la STS '
        '1610/2024. El cruasán sigue al 10' + C.N + '%: el RD 308/2019 sólo '
        'regula el pan y no menciona la bollería.', id_pa='PA-36b')
    par(ws, SEC_IVA + 3, 'IVA en zona de degustación', D.P('iva_degustacion'),
        C.PCT, 'sobre base', 'PA-36c',
        'Si pones mesas, ahí no vendes un bien: prestas un servicio de '
        'hostelería (art. 91.Uno.2.2.º). Tu TPV tiene que separar los tipos.',
        id_pa='PA-36c')

    C.seccion(ws, 'A%d' % SEC_MAR,
              'La regla del margen: UN número, y el otro se deriva')
    par(ws, SEC_MAR + 1, 'Food cost objetivo', D.P('food_cost_objetivo'), C.PCT,
        'sobre PVP sin IVA', 'PS-56',
        'Éste es el ÚNICO número de margen que se teclea. La banda del sector '
        'es 30-35' + C.N + '% de food cost SOBRE EL PRECIO DE VENTA (PS-56), '
        'que equivale a un margen bruto del 65-70' + C.N + '% sobre ese mismo '
        'precio de venta. Cuidado con las fuentes que dan el margen SOBRE '
        'COSTE: PS-55 publica ese mismo 65-70' + C.N + '% sobre coste, y eso '
        'es un food cost del 59-61' + C.N + '%, mucho más flojo. Antes de '
        'comparar tu margen con el de nadie, pregunta sobre qué base está '
        'calculado.')
    par(ws, SEC_MAR + 2, 'Margen bruto objetivo (derivado)', None, C.PCT,
        'sobre PVP sin IVA', 'calculado',
        'Uno menos el food cost objetivo. No se teclea a propósito: pedir los '
        'dos números permite ponerlos incoherentes y es el error de método más '
        'repetido del oficio.',
        formula='=IFERROR(1-{f},"")'.format(f=A(P_FC)))

    C.seccion(ws, 'A%d' % SEC_LEG,
              'Techos y plazos legales (RD 1021/2022, verificado el %s)'
              % D.FECHA_VERIFICACION_LEGAL)
    par(ws, SEC_LEG + 1, 'Techo de la fila 9 del art. 4.1', 4, C.ENT, '°C',
        'PA-12',
        'Productos de pastelería RELLENOS, salvo que sean estables a '
        'temperatura ambiente. Es el techo más bajo de los dos y por eso suele '
        'mandar él.', id_pa='PA-12')
    par(ws, SEC_LEG + 2, 'Techo del art. 9.3', 8, C.ENT, '°C', 'PA-15',
        'Lo elaborado por la vía del art. 9.1.a) que no sea estable a '
        'temperatura ambiente, y lo hecho con ovoproducto del art. 9.2.',
        id_pa='PA-15')
    par(ws, SEC_LEG + 3, 'Plazo de consumo del art. 9.3', 24, C.ENT, 'horas',
        'PA-15',
        'Desde la elaboración, con REGISTRO de fecha y hora. No es una vida '
        'útil: es un plazo legal, y sólo alcanza a lo que dice el propio '
        'art. 9.3.', id_pa='PA-15')
    par(ws, SEC_LEG + 4, 'Umbral analítico de «sin gluten»', 20, C.ENT,
        'mg/kg', 'PA-23',
        'No es una declaración libre: por debajo de 20' + C.N + 'mg/kg de '
        'gluten en el producto tal y como se vende. Con harina de arroz no '
        'basta si el obrador comparte utillaje con harina de trigo.',
        id_pa='PA-23')

    C.seccion(ws, 'A%d' % SEC_OTR, 'Merma, packaging y comercial')
    par(ws, SEC_OTR + 1, 'Merma objetivo', D.P('merma_objetivo'), C.PCT,
        'de la producción', 'kit-tareas-pasteleria/10',
        'Objetivo precargado en el plan de producción del kit. En una '
        'pastelería artesanal se mueve entre el 3 y el 8' + C.N + '%; por '
        'encima del 10' + C.N + '% hay que revisar el plan de producción, no '
        'el escandallo.')
    par(ws, SEC_OTR + 2, 'Packaging sobre el coste del producto',
        D.P('packaging_pct_coste'), C.PCT, 'del coste', 'PS-59',
        'Entre el 5 y el 15' + C.N + '% del coste total del producto. Aquí, el '
        'punto medio. En pastelería la caja no es un extra: es parte del '
        'producto.')
    par(ws, SEC_OTR + 3, 'Piezas por cliente', D.P('piezas_por_ticket'), C.DEC,
        'piezas/ticket', 'supuesto',
        'De aquí sale el ticket medio, que NO se teclea. No existe un ticket '
        'medio publicado de pastelería: el tuyo se calcula desde tu carta y tu '
        'mix, y por eso se puede publicar diciendo lo que es.')
    par(ws, SEC_OTR + 4, 'Umbral de rotación del semáforo de surtido',
        1.0, C.DEC, '% del mix', 'supuesto',
        'Por debajo de este porcentaje del mix, la referencia se considera de '
        'rotación baja en la hoja «Decisión de Surtido». Criterio de la casa, '
        'no del sector: súbelo si tu carta es más corta.')

    # --- precios de compra -------------------------------------------------
    C.seccion(ws, 'A%d' % SEC_PRE, 'Precios de compra (la única tabla de precios)')
    C.encabezados(ws, PRE_CAB, [
        ('A', 'Ingrediente', None), ('B', 'Precio de compra (€)', None),
        ('C', 'Unidad de compra', None), ('D', 'De dónde sale', None),
        ('E', '', None), ('F', '', None),
        ('G', 'Nota', None)], alto=30)
    for i, ing in enumerate(INGREDIENTES):
        r = PRE_INI + i
        precio, unidad, fuente = D.PRECIOS_COMPRA[ing]
        motor.val(ws, 'A%d' % r, ing)
        C.entrada(ws, 'B%d' % r, precio, fmt=C.EUR,
                  etiqueta='Precio de compra de %s' % ing)
        motor.val(ws, 'C%d' % r, unidad)
        motor.val(ws, 'D%d' % r, 'copiado del kit' if fuente.startswith('kit-')
                  else fuente)
        ws['D%d' % r].font = Font(size=8, color=C.GRIS)
    motor.val(ws, 'A%d' % PRE_PIE,
              'Los diecinueve precios marcados «copiado del kit» son los mismos '
              'que usa el «kit-escandallos/05-pasteleria.xlsx»: son los que '
              'hacen que el mismo croissant cueste lo mismo en los dos '
              'productos. Ojo con la mantequilla: la cotización de commodity a '
              'granel que publican los observatorios NO es el precio de la '
              'mantequilla de laminado 82-84' + C.N + '% que compra un obrador. '
              'Sirve para modelar la volatilidad, nunca para fijar un precio.',
              wrap=True)
    ws.merge_cells('A%d:G%d' % (PRE_PIE, PRE_PIE))
    ws['A%d' % PRE_PIE].font = Font(size=9)
    ws.row_dimensions[PRE_PIE].height = 46
    motor.val(ws, 'A%d' % (PRE_PIE + 2), C.VERSION_LINE)
    ws['A%d' % (PRE_PIE + 2)].font = Font(size=8, italic=True)

    motor.dv_porcentaje(ws, [P_SS, P_RATIO, P_FC, P_MERMA, P_PACK])
    motor.dv_porcentaje(ws, [P_IVAP, P_IVAPAN, P_IVADEG], titulo='Tipo de IVA',
                        prompt='Se escribe en tanto por uno: 0,10 = 10 %.')
    motor.dv_numerica(ws, ['B%d' % r for r in range(PER_INI, PER_FIN + 1)],
                      minimo=0, maximo=1, titulo='Jornada',
                      mensaje='La jornada va de 0 a 1 (0,5 = media jornada).')
    C.setup(ws)
    return ws


# --------------------------------------------------------------------------
# Hoja «Escandallo por Tanda»
# --------------------------------------------------------------------------
def hoja_escandallo(wb):
    ws = wb.create_sheet(H_ESC)
    C.cabecera_hoja(ws, 'Escandallo por Tanda')
    motor.val(ws, 'A3', 'La unidad de costeo es LA TANDA, no la pieza. Los '
                        'precios salen de la tabla única de «Parámetros».')
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, ESC_CAB, [
        ('A', 'Ref', 7), ('B', 'Referencia', 28), ('C', 'Familia', 19),
        ('D', 'Ingrediente', 34), ('E', 'Cantidad neta', 11),
        ('F', 'Unidad de uso', 10), ('G', 'Factor de conversión', 10),
        ('H', 'Merma', 9), ('I', 'Cantidad bruta', 11),
        ('J', 'Precio de compra (€)', 11), ('K', 'Unidad de compra', 11),
        ('L', 'Coste de la línea (€)', 12),
        ('M', 'Procedencia', 66)])

    for i, (ref, linea) in enumerate(LINEAS):
        r = ESC_INI + i
        ingrediente, cantidad, ud_uso, factor, merma = linea
        primera = (i == 0 or LINEAS[i - 1][0]['id'] != ref['id'])
        motor.val(ws, 'A%d' % r, ref['id'])
        motor.val(ws, 'B%d' % r, ref['nombre'] if primera else '')
        motor.val(ws, 'C%d' % r, ref['familia'] if primera else '')
        motor.val(ws, 'D%d' % r, ingrediente)
        C.entrada(ws, 'E%d' % r, cantidad, fmt='#,##0.000',
                  etiqueta='%s · %s · cantidad neta' % (ref['id'], ingrediente))
        motor.val(ws, 'F%d' % r, ud_uso)
        C.entrada(ws, 'G%d' % r, factor, fmt=C.DEC,
                  etiqueta='%s · %s · factor' % (ref['id'], ingrediente))
        C.entrada(ws, 'H%d' % r, merma, fmt=C.PCT,
                  etiqueta='%s · %s · merma' % (ref['id'], ingrediente))
        motor.f(ws, 'I%d' % r, '=IFERROR(E{r}/(1-H{r}),"")'.format(r=r),
                fmt='#,##0.000')
        motor.f(ws, 'J%d' % r,
                '=IFERROR(VLOOKUP($D{r},{t},2,FALSE),"")'.format(r=r,
                                                                 t=TABLA_PRECIOS),
                fmt=C.EUR)
        motor.val(ws, 'K%d' % r, D.PRECIOS_COMPRA[ingrediente][1])
        motor.f(ws, 'L%d' % r, '=IFERROR(I{r}/G{r}*J{r},"")'.format(r=r),
                fmt=C.EUR)
        if primera:
            motor.val(ws, 'M%d' % r, procedencia(ref), wrap=True)
            ws['M%d' % r].font = Font(size=8, color=C.GRIS)

    motor.val(ws, 'A%d' % ESC_TOT, 'TOTAL', bold=True)
    C.crema(motor.f(ws, 'L%d' % ESC_TOT,
                    '=SUM(L{a}:L{b})'.format(a=ESC_INI, b=ESC_FIN), fmt=C.EUR,
                    bold=True))
    motor.val(ws, 'M%d' % ESC_TOT,
              'Materia prima de una tanda de cada una de las 30 referencias. No '
              'es un coste de producción: es la suma de las 30 tandas.')
    ws['M%d' % ESC_TOT].font = Font(size=8, color=C.GRIS)

    # --- resumen por referencia -------------------------------------------
    C.seccion(ws, 'A%d' % (RES_CAB - 1), 'Coste de materia por referencia')
    C.encabezados(ws, RES_CAB, [
        ('A', 'Ref', None), ('B', 'Referencia', None), ('C', 'Familia', None),
        ('D', 'Uds por tanda', None), ('E', 'Líneas del escandallo', None),
        ('F', 'Coste de materia de la tanda (€)', None),
        ('G', 'Coste de materia por unidad (€)', None),
        ('H', 'Gramaje (g)', None),
        ('I', 'Coste de materia por kg (€)', None),
        ('J', '', None), ('K', '', None), ('L', '', None),
        ('M', 'Procedencia del escandallo', None)], alto=40)

    for i, ref in enumerate(D.CARTA):
        r = RES_INI + i
        motor.val(ws, 'A%d' % r, ref['id'])
        motor.val(ws, 'B%d' % r, ref['nombre'], bold=(ref['id'] in COPIADAS))
        motor.val(ws, 'C%d' % r, ref['familia'])
        C.entrada(ws, 'D%d' % r, ref['tanda'], fmt=C.ENT,
                  etiqueta='Uds por tanda de %s' % ref['nombre'])
        # `IFERROR` por fuera del `SUMPRODUCT` a propósito, igual que en la
        # columna F: sin él, pycel devuelve el recuento bien en la celda pero
        # el `SUM` de la fila de total lo cachea como 0 y el libro se publica
        # con un total falso sin un solo aviso. Medido en este mismo libro.
        motor.f(ws, 'E%d' % r,
                '=IFERROR(SUMPRODUCT(--($A${a}:$A${b}=$A{r}),'
                '--($D${a}:$D${b}<>"")),"")'.format(a=ESC_INI, b=ESC_FIN, r=r),
                fmt=C.ENT)
        motor.f(ws, 'F%d' % r,
                '=IFERROR(SUMPRODUCT(--($A${a}:$A${b}=$A{r}),$L${a}:$L${b}),"")'
                .format(a=ESC_INI, b=ESC_FIN, r=r), fmt=C.EUR)
        motor.f(ws, 'G%d' % r, '=IFERROR(F{r}/D{r},"")'.format(r=r), fmt=C.EUR)
        C.entrada(ws, 'H%d' % r, ref['gramaje_g'], fmt=C.ENT,
                  etiqueta='Gramaje de %s' % ref['nombre'])
        motor.f(ws, 'I%d' % r, '=IFERROR(G{r}/H{r}*1000,"")'.format(r=r),
                fmt=C.EUR)
        motor.val(ws, 'M%d' % r, procedencia(ref), wrap=True)
        ws['M%d' % r].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[r].height = 26

    motor.val(ws, 'A%d' % RES_TOT, 'TOTAL', bold=True)
    # El recuento total se cuenta DIRECTO sobre la tabla de líneas, no sumando
    # la columna E: pycel cachea como 0 un `SUM` sobre una columna de
    # `SUMPRODUCT`, y el libro se publicaría con un total falso. La coherencia
    # entre las dos vías la vigila el aviso de la columna G.
    C.crema(motor.f(ws, 'E%d' % RES_TOT,
                    '=IFERROR(SUMPRODUCT(--($A${a}:$A${b}<>""),'
                    '--($D${a}:$D${b}<>"")),"")'.format(a=ESC_INI, b=ESC_FIN),
                    fmt=C.ENT, bold=True))
    C.crema(motor.f(ws, 'F%d' % RES_TOT,
                    '=SUM(F{a}:F{b})'.format(a=RES_INI, b=RES_FIN), fmt=C.EUR,
                    bold=True))
    # Tolerancia a propósito: comparar dos sumas de coma flotante con `=0`
    # da «descuadre» por un residuo de 1e-13 y el aviso deja de significar nada.
    motor.f(ws, 'G%d' % RES_TOT,
            '=IF(ABS(F{t}-{e})<=0.005,"Cuadra","DESCUADRE")'
            .format(t=RES_TOT, e='L%d' % ESC_TOT))
    motor.val(ws, 'M%d' % RES_TOT,
              'La columna E cuenta las líneas directamente sobre la tabla de '
              'arriba y la columna G comprueba que el coste repartido por '
              'referencia cuadra con el coste de las líneas. Si aparece '
              '«DESCUADRE», hay una fila cuyo Ref no está en la lista de '
              'referencias: su coste se suma arriba y no se le imputa a nadie.')
    ws['M%d' % RES_TOT].font = Font(size=8, color=C.GRIS)

    motor.dv_porcentaje(ws, ['H%d' % r for r in range(ESC_INI, ESC_FIN + 1)],
                        titulo='Merma (%)',
                        prompt='Se escribe en tanto por uno: 0,08 = 8 %. La '
                               'merma entra como cantidad neta / (1 - merma).',
                        maximo=0.95)
    ws.freeze_panes = 'D6'
    C.setup(ws)
    return ws


# --------------------------------------------------------------------------
# Hoja «Coste Hora y Mano de Obra»
# --------------------------------------------------------------------------
def hoja_mano_obra(wb):
    ws = wb.create_sheet(H_MO)
    C.cabecera_hoja(ws, 'Coste Hora y Mano de Obra')
    motor.val(ws, 'A3', 'La mano de obra imputada por pieza. Es el capítulo que '
                        'enseña a dejar de regalar tu trabajo.')
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, MO_CAB, [
        ('A', 'Ref', 7), ('B', 'Referencia', 28), ('C', 'Familia', 19),
        ('D', 'Uds por tanda', 9),
        ('E', 'Minutos de mano de obra por tanda', 11),
        ('F', 'Horas de mano de obra por tanda', 10),
        ('G', 'Coste hora de obrador (€)', 10),
        ('H', 'Coste de mano de obra de la tanda (€)', 11),
        ('I', 'Coste de mano de obra por unidad (€)', 11),
        ('J', 'Coste de materia por unidad (€)', 11),
        ('K', 'Coste total por unidad (€)', 11),
        ('L', 'PVP con IVA (€)', 10), ('M', 'IVA', 8),
        ('N', 'PVP sin IVA (€)', 10), ('O', 'Food cost', 10),
        ('P', 'Margen bruto', 10), ('Q', 'Margen por unidad (€)', 11),
        ('R', 'Peso de la mano de obra sobre el coste', 11),
        ('S', 'Minutos por pieza', 10)])

    for i, ref in enumerate(D.CARTA):
        r = MO_INI + i
        rr = RES_INI + i
        motor.val(ws, 'A%d' % r, ref['id'])
        motor.val(ws, 'B%d' % r, ref['nombre'])
        motor.val(ws, 'C%d' % r, ref['familia'])
        motor.f(ws, 'D%d' % r, '={q}D{x}'.format(q=QESC, x=rr), fmt=C.ENT)
        C.entrada(ws, 'E%d' % r, ref['minutos_mo_tanda'], fmt=C.ENT,
                  etiqueta='Minutos de mano de obra de %s' % ref['nombre'])
        motor.f(ws, 'F%d' % r, '=IFERROR(E{r}/60,"")'.format(r=r), fmt=C.DEC)
        motor.f(ws, 'G%d' % r, '={c}'.format(c=A(P_CHORA)), fmt=C.EUR)
        motor.f(ws, 'H%d' % r, '=IFERROR(F{r}*G{r},"")'.format(r=r), fmt=C.EUR)
        motor.f(ws, 'I%d' % r, '=IFERROR(H{r}/D{r},"")'.format(r=r), fmt=C.EUR)
        motor.f(ws, 'J%d' % r, '={q}G{x}'.format(q=QESC, x=rr), fmt=C.EUR)
        motor.f(ws, 'K%d' % r, '=IFERROR(I{r}+J{r},"")'.format(r=r), fmt=C.EUR)
        C.entrada(ws, 'L%d' % r, ref['pvp_con_iva'], fmt=C.EUR,
                  etiqueta='PVP con IVA de %s' % ref['nombre'])
        cel = C.entrada(ws, 'M%d' % r, ref['iva'], fmt=C.PCT,
                        etiqueta='IVA de %s' % ref['nombre'])
        C.nota_celda(ws, cel.coordinate,
                     'PA-36b' if ref['familia'] == 'Panes de acompañamiento'
                     else 'PA-36')
        motor.f(ws, 'N%d' % r, '=IFERROR(L{r}/(1+M{r}),"")'.format(r=r),
                fmt=C.EUR)
        motor.f(ws, 'O%d' % r, '=IFERROR(J{r}/N{r},"")'.format(r=r), fmt=C.PCT)
        motor.f(ws, 'P%d' % r, '=IFERROR(1-O{r},"")'.format(r=r), fmt=C.PCT)
        motor.f(ws, 'Q%d' % r, '=IFERROR(N{r}-K{r},"")'.format(r=r), fmt=C.EUR)
        motor.f(ws, 'R%d' % r, '=IFERROR(I{r}/K{r},"")'.format(r=r), fmt=C.PCT)
        motor.f(ws, 'S%d' % r, '=IFERROR(E{r}/D{r},"")'.format(r=r), fmt=C.DEC)

    motor.val(ws, 'A%d' % MO_TOT, 'MEDIA / TOTAL', bold=True)
    C.crema(motor.f(ws, 'H%d' % MO_TOT,
                    '=SUM(H{a}:H{b})'.format(a=MO_INI, b=MO_FIN), fmt=C.EUR,
                    bold=True))
    C.crema(motor.f(ws, 'O%d' % MO_TOT,
                    '=IFERROR(AVERAGE(O{a}:O{b}),"")'.format(a=MO_INI, b=MO_FIN),
                    fmt=C.PCT, bold=True))
    C.crema(motor.f(ws, 'Q%d' % MO_TOT,
                    '=IFERROR(AVERAGE(Q{a}:Q{b}),"")'.format(a=MO_INI, b=MO_FIN),
                    fmt=C.EUR, bold=True))
    C.crema(motor.f(ws, 'R%d' % MO_TOT,
                    '=IFERROR(AVERAGE(R{a}:R{b}),"")'.format(a=MO_INI, b=MO_FIN),
                    fmt=C.PCT, bold=True))

    motor.semaforo_isnumber(ws, 'O%d:O%d' % (MO_INI, MO_FIN), '$O%d' % MO_INI,
                            operador='>', umbral=A(P_FC))
    motor.semaforo_isnumber(ws, 'Q%d:Q%d' % (MO_INI, MO_FIN), '$Q%d' % MO_INI,
                            operador='<=', umbral='0')

    fila = MO_TOT + 2
    for texto in (
        'El food cost de esta hoja compara MATERIA con PVP sin IVA, que es la '
        'definición del sector. La mano de obra no entra en el food cost: '
        'entra en el coste total y se le come el margen. Por eso una '
        'referencia puede tener un food cost estupendo y dejarte menos dinero '
        'que otra peor: mira siempre las dos columnas juntas.',
        'El margen bruto de la columna P es uno menos el food cost, calculado, '
        'no tecleado. Es la misma regla dicha del revés, y por eso el libro no '
        'te pide los dos números en ningún sitio.',
        'La columna R es la que duele: en las referencias de más trabajo la '
        'mano de obra es más de la mitad del coste. Ahí no se gana bajando el '
        'precio de la harina, se gana cambiando el proceso o el precio.',
        'Las celdas en rojo del food cost son las que se pasan de tu objetivo '
        'de «Parámetros»; las del margen, las que no dejan dinero. Lo que '
        'hacer con ellas está en la hoja «Decisión de Surtido».',
    ):
        motor.val(ws, 'A%d' % fila, texto, wrap=True)
        ws.merge_cells('A%d:S%d' % (fila, fila))
        ws['A%d' % fila].font = Font(size=9)
        ws.row_dimensions[fila].height = 44
        fila += 1
    motor.val(ws, 'A%d' % (fila + 1), C.VERSION_LINE)
    ws['A%d' % (fila + 1)].font = Font(size=8, italic=True)

    motor.dv_porcentaje(ws, ['M%d' % r for r in range(MO_INI, MO_FIN + 1)],
                        titulo='Tipo de IVA',
                        prompt='Se escribe en tanto por uno: 0,10 = 10 %.')
    motor.dv_numerica(ws, ['E%d' % r for r in range(MO_INI, MO_FIN + 1)],
                      minimo=1, maximo=1440, titulo='Minutos por tanda',
                      mensaje='Escribe los minutos de mano de obra de la tanda '
                              'entera (1 a 1.440).')
    ws.freeze_panes = 'D6'
    C.setup(ws)
    return ws


# --------------------------------------------------------------------------
# Hoja «Decisión de Huevo y Temperatura»
# --------------------------------------------------------------------------
def hoja_huevo(wb):
    ws = wb.create_sheet(H_HUE)
    C.cabecera_hoja(ws, 'Decisión de Huevo y Temperatura')
    motor.val(ws, 'A3', 'Dos salidas separadas, cada una con su artículo: la '
                        'TEMPERATURA (el más bajo de los techos que apliquen) y '
                        'el PLAZO legal del art. 9.3. La vida útil la declaras tú.')
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, HU_CAB, [
        ('A', 'Ref', 7), ('B', 'Referencia', 28), ('C', 'Familia', 19),
        ('D', 'Vía legal del huevo', 22),
        ('E', '¿Producto relleno?', 10),
        ('F', '¿Estable a temperatura ambiente?', 12),
        ('G', 'Techo del art. 4.1 fila 9 (°C)', 11),
        ('H', 'Techo del art. 9.3 (°C)', 11),
        ('I', 'Temperatura de conservación (°C)', 12),
        ('J', 'Cuál manda', 52),
        ('K', 'Plazo legal (art. 9.3)', 12),
        ('L', 'Vida útil declarada por ti (días)', 13),
        ('M', 'Dónde va en el mostrador', 14),
        ('N', 'Qué dice esa vía', 62),
        ('O', 'Coherencia D / F', 34)])
    # Hallazgo B1 (2026-09-10): toda la hoja construye su decisión sobre las
    # tres vías del art. 9 del RD 1021/2022 y no llevaba ni una nota de PA-14
    # («Huevo crudo: las tres vías legales del art. 9»), que es el id que
    # contiene la cita literal de esas vías. Las notas de la hoja apuntaban
    # sólo a las CONSECUENCIAS (PA-15, art. 9.3) y al art. 4.1 (PA-12), nunca
    # al artículo que las CREA.
    C.nota_celda(ws, 'D%d' % HU_CAB, 'PA-14')

    for i, ref in enumerate(D.CARTA):
        r = HU_INI + i
        motor.val(ws, 'A%d' % r, ref['id'])
        motor.val(ws, 'B%d' % r, ref['nombre'])
        motor.val(ws, 'C%d' % r, ref['familia'])
        C.entrada(ws, 'D%d' % r, ref['via_huevo'],
                  etiqueta='Vía legal del huevo de %s' % ref['nombre'])
        C.entrada(ws, 'E%d' % r, 'Sí' if ref['relleno'] else 'No',
                  etiqueta='¿%s es producto relleno?' % ref['nombre'])
        C.entrada(ws, 'F%d' % r, 'Sí' if ref['estable_ambiente'] else 'No',
                  etiqueta='¿%s es estable a temperatura ambiente?'
                           % ref['nombre'])
        g = motor.f(ws, 'G%d' % r,
                    '=IF(AND($E{r}="Sí",$F{r}="No"),{t},"")'.format(r=r,
                                                                    t=A(P_T41)),
                    fmt=C.ENT)
        C.nota_celda(ws, g.coordinate, 'PA-12')
        h = motor.f(ws, 'H%d' % r,
                    '=IF(AND(OR($D{r}="70/2",$D{r}="ovoproducto"),$F{r}="No"),'
                    '{t},"")'.format(r=r, t=A(P_T93)), fmt=C.ENT)
        C.nota_celda(ws, h.coordinate, 'PA-15')
        motor.f(ws, 'I%d' % r,
                '=IF(AND(G{r}="",H{r}=""),"",IF(G{r}="",H{r},'
                'IF(H{r}="",G{r},MIN(G{r},H{r}))))'.format(r=r), fmt=C.ENT)
        motor.f(ws, 'J%d' % r,
                '=IF(AND(G{r}="",H{r}=""),'
                '"Ni la fila 9 del art. 4.1 ni el art. 9.3 le fijan techo: '
                'vitrina de ambiente.",'
                'IF(AND(G{r}<>"",H{r}<>""),'
                '"Le aplican los DOS techos y manda el más bajo, el de la fila 9 '
                'del art. 4.1. No es un conflicto: son dos topes distintos.",'
                'IF(G{r}<>"",'
                '"Manda la fila 9 del art. 4.1: producto de pastelería relleno '
                'que no es estable a temperatura ambiente.",'
                '"Manda el art. 9.3: elaborado por la vía del art. 9.1.a) sin '
                'ser estable, o con ovoproducto del art. 9.2.")))'.format(r=r))
        ws['J%d' % r].alignment = Alignment(wrap_text=True, vertical='top')
        k = motor.f(ws, 'K%d' % r,
                    '=IF(AND(OR($D{r}="70/2",$D{r}="ovoproducto"),$F{r}="No"),'
                    '{p},"No aplica")'.format(r=r, p=A(P_PLAZO)), fmt=C.ENT)
        C.nota_celda(ws, k.coordinate, 'PA-15')
        C.entrada(ws, 'L%d' % r, 'Por declarar en tu APPCC',
                  etiqueta='Vida útil declarada de %s' % ref['nombre'])
        motor.f(ws, 'M%d' % r,
                '=IF(I{r}="","Vitrina de ambiente","Vitrina refrigerada")'
                .format(r=r))
        motor.val(ws, 'N%d' % r, D.VIAS_HUEVO_TEXTO[ref['via_huevo']],
                  wrap=True)
        ws['N%d' % r].font = Font(size=8, color=C.GRIS)
        # Hallazgo B5 (2026-09-10): «estable a ambiente» (B54) YA significa
        # «vía 1.a) y el producto terminado ES estable», así que la vía queda
        # exenta del plazo del 9.3 (K) pase lo que pase en F. El bug era que
        # eso pasaba EN SILENCIO cuando F decía «No», contradiciendo la propia
        # vía elegida: se avisa en vez de resolverlo callado y en la dirección
        # permisiva.
        o_cel = motor.f(ws, 'O%d' % r,
                        '=IF(AND($D{r}="estable a ambiente",$F{r}="No"),'
                        '"Incoherente: has elegido la vía de producto '
                        'estable y luego has dicho que no lo es","")'
                        .format(r=r))
        o_cel.alignment = Alignment(wrap_text=True, vertical='top')
        ws.row_dimensions[r].height = 40

    motor.regla_expresion(ws, 'O%d:O%d' % (HU_INI, HU_FIN),
                          '=$O%d<>""' % HU_INI)

    # --- resumen -----------------------------------------------------------
    C.seccion(ws, 'A%d' % (HU_RES - 1), 'Lo que sale de esta hoja')
    resumen = [
        ('Referencias que necesitan vitrina REFRIGERADA',
         '=COUNTIF(M{a}:M{b},"Vitrina refrigerada")'.format(a=HU_INI, b=HU_FIN),
         C.ENT,
         'Cuántos metros de vitrina refrigerada tienes que comprar lo decide '
         'esta cuenta, no el gusto.'),
        ('Referencias que van en vitrina de AMBIENTE',
         '=COUNTIF(M{a}:M{b},"Vitrina de ambiente")'.format(a=HU_INI, b=HU_FIN),
         C.ENT,
         'Palmeras, Sacher, huesos de santo, turrón y panes. Son las que se '
         'pueden adelantar y las que aguantan el pico.'),
        ('Referencias con el techo de la fila 9 del art. 4.1',
         '=SUMPRODUCT(--(G{a}:G{b}<>""))'.format(a=HU_INI, b=HU_FIN), C.ENT,
         'Producto relleno que no es estable a temperatura ambiente.'),
        ('Referencias con el techo del art. 9.3',
         '=SUMPRODUCT(--(H{a}:H{b}<>""))'.format(a=HU_INI, b=HU_FIN), C.ENT,
         'Vía del art. 9.1.a) sin ser estable, u ovoproducto del art. 9.2.'),
        ('Referencias a las que aplican LOS DOS techos',
         '=SUMPRODUCT(--(G{a}:G{b}<>""),--(H{a}:H{b}<>""))'.format(a=HU_INI,
                                                                   b=HU_FIN),
         C.ENT,
         'Aquí manda el más bajo. Es el caso que la SERP vende como «conflicto '
         'sin resolver» y no lo es.'),
        ('Referencias con plazo legal de 24 horas',
         '=SUMPRODUCT(--(K{a}:K{b}<>"No aplica"))'.format(a=HU_INI, b=HU_FIN),
         C.ENT,
         'Con registro de fecha y hora de elaboración. Es la obligación del '
         'art. 9.3 que casi nadie cuenta.'),
        ('Referencias que no llevan huevo en ninguna forma',
         '=COUNTIF(D{a}:D{b},"sin huevo")'.format(a=HU_INI, b=HU_FIN), C.ENT,
         'El art. 9 no les aplica.'),
        ('Referencias por la vía 63/20 con consumo inmediato',
         '=COUNTIF(D{a}:D{b},"63/20")'.format(a=HU_INI, b=HU_FIN), C.ENT,
         'Debería salir cero: la vía del art. 9.1.b) es la de los huevos '
         'fritos y las tortillas, no la de la pastelería. Está en la lista '
         'para que sepas que existe y que NO es tuya.'),
    ]
    for i, (etiqueta, formula, fmt, nota) in enumerate(resumen):
        r = HU_RES + i
        motor.val(ws, 'B%d' % r, etiqueta)
        C.crema(motor.f(ws, 'G%d' % r, formula, fmt=fmt, bold=True))
        motor.val(ws, 'J%d' % r, nota, wrap=True)
        ws['J%d' % r].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[r].height = 26

    # --- listas para los desplegables --------------------------------------
    motor.val(ws, 'A%d' % (HU_LIS - 1),
              'Listas de los desplegables (no se tocan)', bold=True)
    ws['A%d' % (HU_LIS - 1)].font = Font(bold=True, size=9, color=C.GRIS)
    for i, via in enumerate(D.VIAS_HUEVO):
        motor.val(ws, 'A%d' % (HU_LIS + i), via)
        motor.val(ws, 'B%d' % (HU_LIS + i), D.VIAS_HUEVO_TEXTO[via], wrap=True)
        ws['B%d' % (HU_LIS + i)].font = Font(size=8, color=C.GRIS)
        if via in ('70/2', '63/20', 'ovoproducto'):
            # Hallazgo B1: las tres vías legales del art. 9 son la cita
            # literal de PA-14 (70/2 = art. 9.1.a; 63/20 = art. 9.1.b;
            # ovoproducto = art. 9.2).
            C.nota_celda(ws, 'A%d' % (HU_LIS + i), 'PA-14')
    for i, s in enumerate(SI_NO):
        motor.val(ws, 'D%d' % (HU_LIS + i), s)
    rango_vias = "'%s'!$A$%d:$A$%d" % (H_HUE, HU_LIS, HU_LIS + len(D.VIAS_HUEVO) - 1)
    rango_sino = "'%s'!$D$%d:$D$%d" % (H_HUE, HU_LIS, HU_LIS + 1)
    C.dv_rango(ws, ['D%d' % r for r in range(HU_INI, HU_FIN + 1)], rango_vias,
               'Vía legal del huevo',
               'Elige una de las cinco vías del art. 9 del RD 1021/2022 de la '
               'lista.')
    C.dv_rango(ws, ['E%d' % r for r in range(HU_INI, HU_FIN + 1)]
               + ['F%d' % r for r in range(HU_INI, HU_FIN + 1)], rango_sino,
               'Sí o No', 'Elige «Sí» o «No» de la lista.')

    fila = HU_LIS + len(D.VIAS_HUEVO) + 2
    for texto in (
        'CÓMO SE LEE ESTA HOJA. Eliges la vía legal del huevo, dices si la pieza '
        'va rellena y si el producto TERMINADO es estable a temperatura '
        'ambiente. Con eso el libro te devuelve la temperatura a la que tienes '
        'que conservarla, cuál de los dos artículos manda y si te aplica el '
        'plazo de 24 horas. Nada más, y nada menos.',
        'LA VIDA ÚTIL ES TUYA. La columna L viene con el texto «Por declarar en '
        'tu APPCC» a propósito: el RD 1021/2022 NO establece vidas útiles y '
        'este libro no se las va a inventar para tus 30 referencias. La fijas '
        'tú, con tu proceso y tus analíticas, y tiene que constar en tu plan de '
        'APPCC. El plazo del art. 9.3 de la columna K es otra cosa: es legal, '
        'es de 24 horas y sólo alcanza a lo que dice el artículo.',
        'LO QUE ESTA HOJA CAMBIA EN TU DINERO. Cada referencia que sale '
        '«Vitrina refrigerada» son metros de mueble frigorífico que hay que '
        'comprar, y cada una con plazo de 24 horas es producto que no se puede '
        'adelantar: hay que hacerlo el mismo día, también el 5 de enero. Por '
        'eso esta hoja se lee ANTES de cerrar la carta y ANTES de comprar la '
        'vitrina.',
        'DÓNDE NO ESTÁ LO DEMÁS. Los alérgenos de vitrina son el '
        '«12-control-alergenos-vitrina.xlsx» del Kit de Tareas Pastelería y el '
        '«08» del Pack APPCC; el registro diario de temperaturas y de vidas '
        'útiles es el «13-registro-temperaturas-recepcion.xlsx» del mismo kit. '
        'Este libro no los rehace: hace la decisión previa, que no está en '
        'ningún fichero del catálogo.',
        'LA NORMA DEROGADA QUE SIGUE VIVA EN INTERNET. Casi todo lo que vas a '
        'leer sobre «huevo a 8' + C.N + '°C y 24 horas» cita el RD 1254/1991, '
        'derogado el 22 de diciembre de 2022. Y en producto relleno no estable '
        'no mandan los 8' + C.N + '°C: mandan los 4' + C.N + '°C de la fila 9 '
        'del art. 4.1. Cada celda con dato legal de esta hoja lleva su nota con '
        'la norma, el artículo y el enlace al BOE, verificados el '
        + D.FECHA_VERIFICACION_LEGAL + '.',
        # Hallazgo B1 (2026-09-10): declaración explícita de alcance para los
        # cuatro ids que IDS_LEGALES_REQUERIDOS asigna al libro 4 y que esta
        # hoja NO resuelve en celda (el comentario de esta fila lleva las
        # cuatro notas «Verificado · norma · URL», para que la cobertura no
        # dependa sólo de este párrafo).
        'ALCANCE LEGAL DE ESTA HOJA: QUÉ NO RESUELVE Y POR QUÉ. La congelación '
        '(PA-13, art. 5) es del PROCESO, no de la vitrina: va en el APPCC y en '
        'el «13-registro-temperaturas-recepcion.xlsx» del Kit de Tareas, no '
        'aquí. Los 14 alérgenos (PA-21) tienen su propia matriz dedicada, el '
        '«12-control-alergenos-vitrina.xlsx»: repetirlos en esta tabla sería '
        'mantener el mismo dato en dos sitios y que se desincronicen. El RD '
        '496/2010 de calidad (PA-24) fija denominaciones y composición, no '
        'temperaturas ni plazos: no cambia ni una celda de esta hoja. Y el RD '
        '308/2019 del pan (PA-25) sólo aplica si tu carta incluye pan de '
        'verdad, cosa que decides en el libro 6, no aquí.',
    ):
        motor.val(ws, 'A%d' % fila, texto, wrap=True)
        ws.merge_cells('A%d:N%d' % (fila, fila))
        ws['A%d' % fila].font = Font(size=9)
        ws.row_dimensions[fila].height = 56
        fila += 1
    fila_alcance = fila - 1
    _notas_alcance = [D.nota_legal(pid) for pid in
                      ('PA-13', 'PA-21', 'PA-24', 'PA-25')]
    ws['A%d' % fila_alcance].comment = Comment(
        '\n'.join('%s: %s' % (pid, n) for pid, n in
                  zip(('PA-13', 'PA-21', 'PA-24', 'PA-25'), _notas_alcance)),
        'AI Chef Pro', height=170, width=460)
    for pid in ('PA-13', 'PA-21', 'PA-24', 'PA-25'):
        C.NOTAS_LEGALES.append((ws.title, 'A%d' % fila_alcance, pid))
    motor.val(ws, 'A%d' % (fila + 1), C.VERSION_LINE)
    ws['A%d' % (fila + 1)].font = Font(size=8, italic=True)
    ws.freeze_panes = 'D6'
    C.setup(ws)
    return ws


# --------------------------------------------------------------------------
# Hoja «Mix y Ticket Medio»
# --------------------------------------------------------------------------
def hoja_mix(wb):
    ws = wb.create_sheet(H_MIX)
    C.cabecera_hoja(ws, 'Mix y Ticket Medio')
    motor.val(ws, 'A3', 'No existe un ticket medio publicado de pastelería. El '
                        'tuyo se calcula desde tu carta y tu mix.')
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, MX_CAB, [
        ('A', 'Ref', 7), ('B', 'Referencia', 28), ('C', 'Familia', 19),
        ('D', 'Mix (% de las unidades)', 11),
        ('E', 'PVP con IVA (€)', 11), ('F', 'PVP sin IVA (€)', 11),
        ('G', 'Aporte al PVP medio con IVA (€)', 12),
        ('H', 'Aporte al ticket medio (€)', 12),
        ('I', 'Ingresos relativos sin IVA', 12),
        ('J', 'Materia relativa', 12),
        ('K', 'Margen relativo', 12),
        ('L', 'Food cost de la referencia', 11),
        ('M', 'Qué aporta esta referencia', 56)])

    for i, ref in enumerate(D.CARTA):
        r = MX_INI + i
        mo = MO_INI + i
        rr = RES_INI + i
        motor.val(ws, 'A%d' % r, ref['id'])
        motor.val(ws, 'B%d' % r, ref['nombre'])
        motor.val(ws, 'C%d' % r, ref['familia'])
        C.entrada(ws, 'D%d' % r, ref['mix_pct'], fmt=C.DEC,
                  etiqueta='Mix de %s' % ref['nombre'])
        motor.f(ws, 'E%d' % r, '={q}L{x}'.format(q=QMO, x=mo), fmt=C.EUR)
        motor.f(ws, 'F%d' % r, '={q}N{x}'.format(q=QMO, x=mo), fmt=C.EUR)
        motor.f(ws, 'G%d' % r, '=IFERROR(E{r}*D{r}/100,"")'.format(r=r),
                fmt=C.EUR)
        motor.f(ws, 'H%d' % r,
                '=IFERROR(G{r}*{p},"")'.format(r=r, p=A(P_PIEZAS)), fmt=C.EUR)
        motor.f(ws, 'I%d' % r, '=IFERROR(F{r}*D{r}/100,"")'.format(r=r),
                fmt=C.EUR)
        motor.f(ws, 'J%d' % r,
                '=IFERROR({q}G{x}*D{r}/100,"")'.format(q=QESC, x=rr, r=r),
                fmt=C.EUR)
        motor.f(ws, 'K%d' % r,
                '=IFERROR({q}Q{x}*D{r}/100,"")'.format(q=QMO, x=mo, r=r),
                fmt=C.EUR)
        motor.f(ws, 'L%d' % r, '={q}O{x}'.format(q=QMO, x=mo), fmt=C.PCT)

    motor.val(ws, 'A%d' % MX_TOT, 'TOTAL DE LA CARTA', bold=True)
    for col, fmt in (('D', C.DEC), ('G', C.EUR), ('H', C.EUR), ('I', C.EUR),
                     ('J', C.EUR), ('K', C.EUR)):
        C.crema(motor.f(ws, '%s%d' % (col, MX_TOT),
                        '=SUM({c}{a}:{c}{b})'.format(c=col, a=MX_INI, b=MX_FIN),
                        fmt=fmt, bold=True))
    motor.val(ws, 'M%d' % MX_TOT,
              'La suma del mix tiene que dar 100,00. Si no, la celda se pone en '
              'rojo: el ticket medio de abajo estaría mintiendo.')
    ws['M%d' % MX_TOT].font = Font(size=8, color=C.GRIS)
    motor.regla_expresion(ws, 'D%d' % MX_TOT,
                          '=AND(ISNUMBER($D${t}),ABS($D${t}-100)>0.01)'
                          .format(t=MX_TOT))

    C.seccion(ws, 'A%d' % MX_RES, 'El ticket medio de tu pastelería')
    resumen = [
        ('PVP medio ponderado con IVA', '=IFERROR($G${t},"")'.format(t=MX_TOT),
         C.EUR,
         'Suma de los aportes de las 30 referencias, ponderados por el mix de '
         'unidades.'),
        ('Piezas por cliente', '={p}'.format(p=A(P_PIEZAS)), C.DEC,
         'Parámetro de la hoja «Parámetros». Es lo único que se supone: el '
         'resto sale de tu carta.'),
        ('TICKET MEDIO CON IVA',
         '=IFERROR($G${t}*{p},"")'.format(t=MX_TOT, p=A(P_PIEZAS)), C.EUR,
         'PVP medio ponderado por piezas por cliente. No se copia de ningún '
         'estudio porque no hay ninguno: éste es el tuyo, y por eso se puede '
         'defender delante de un banco.'),
        ('Ticket medio sin IVA',
         '=IFERROR($I${t}*{p},"")'.format(t=MX_TOT, p=A(P_PIEZAS)), C.EUR,
         'El que entra en el plan financiero: la cuenta de resultados va sin '
         'IVA.'),
        ('IVA medio de la carta',
         '=IFERROR($G${t}/$I${t}-1,"")'.format(t=MX_TOT), C.PCT,
         'No es un tipo legal: es el que hace falta para pasar de caja a '
         'ventas netas, y existe porque los panes van al 4' + C.N + '% y el '
         'resto al 10' + C.N + '%.'),
        ('Food cost de MATERIA de la carta',
         '=IFERROR($J${t}/$I${t},"")'.format(t=MX_TOT), C.PCT,
         'Ponderado por euros vendidos, que es como se pondera de verdad, no '
         'por piezas.'),
        ('Food cost SERVIDO (con merma y packaging)',
         '=IFERROR($J${t}/$I${t}/(1-{m})*(1+{p}),"")'.format(t=MX_TOT,
                                                             m=A(P_MERMA),
                                                             p=A(P_PACK)),
         C.PCT,
         'El de escandallo más lo que se produce y no se vende, más la caja. '
         'Es el que se acerca al de la cuenta de resultados.'),
        ('Food cost objetivo de la casa', '={f}'.format(f=A(P_FC)), C.PCT,
         'El de «Parámetros». La regla del sector es 30-35' + C.N + '%.'),
        ('Margen de contribución medio por pieza (€)',
         '=IFERROR($K${t}/$D${t}*100,"")'.format(t=MX_TOT), C.EUR,
         'Después de materia Y de mano de obra. Es el euro que queda para '
         'pagar alquiler, luz y tu sueldo.'),
    ]
    for i, (etiqueta, formula, fmt, nota) in enumerate(resumen):
        r = MX_RES + 1 + i
        motor.val(ws, 'B%d' % r, etiqueta,
                  bold=etiqueta.startswith('TICKET'))
        C.crema(motor.f(ws, 'F%d' % r, formula, fmt=fmt, bold=True))
        motor.val(ws, 'I%d' % r, nota, wrap=True)
        ws['I%d' % r].font = Font(size=8, color=C.GRIS)
        ws.row_dimensions[r].height = 26
    ws.merge_cells('I%d:M%d' % (MX_RES + 1, MX_RES + 1))

    fila = MX_RES + len(resumen) + 3
    for texto in (
        'POR QUÉ EL FOOD COST DE LA CARTA Y EL DEL PLAN FINANCIERO NO COINCIDEN. '
        'El de escandallo sólo cuenta materia prima de lo que tú fabricas. Al '
        'que llega a la cuenta de resultados hay que sumarle cuatro cosas, en '
        'este orden de tamaño: el producto de TERCEROS que revende el despacho '
        '-bebida, café, helado, bombonería comprada-, que no tiene escandallo '
        'propio; la merma real, que en producto fresco se va por encima del '
        'objetivo; el packaging; y la subida de la materia prima, que en '
        'mantequilla y cacao no es teórica. Por eso el plan financiero se '
        'proyecta con la regla del sector y no con tu escandallo: es el '
        'supuesto conservador. La diferencia entre los dos números es tu '
        'colchón.',
        'EL MIX SE MIDE, NO SE ADIVINA. El del ejemplo es un supuesto. El tuyo '
        'lo saca tu TPV en dos clics a los tres meses de abrir, y hasta '
        'entonces cualquier ticket medio que calcules es una hipótesis. '
        'Dilo así cuando lo lleves al banco.',
    ):
        motor.val(ws, 'A%d' % fila, texto, wrap=True)
        ws.merge_cells('A%d:M%d' % (fila, fila))
        ws['A%d' % fila].font = Font(size=9)
        ws.row_dimensions[fila].height = 76
        fila += 1
    motor.val(ws, 'A%d' % (fila + 1), C.VERSION_LINE)
    ws['A%d' % (fila + 1)].font = Font(size=8, italic=True)

    motor.dv_numerica(ws, ['D%d' % r for r in range(MX_INI, MX_FIN + 1)],
                      minimo=0, maximo=100, titulo='Mix (%)',
                      mensaje='El mix se escribe en porcentaje de 0 a 100 '
                              '(12 = 12 %). Los 30 tienen que sumar 100.')
    ws.freeze_panes = 'D6'
    C.setup(ws)
    return ws


# --------------------------------------------------------------------------
# Hoja «Decisión de Surtido»
# --------------------------------------------------------------------------
def hoja_surtido(wb):
    ws = wb.create_sheet(H_SUR)
    C.cabecera_hoja(ws, 'Decisión de Surtido')
    motor.val(ws, 'A3', 'Margen contra rotación: qué mantener, a qué revisarle '
                        'el precio y qué retirar.')
    ws['A3'].font = Font(italic=True, size=9)

    C.encabezados(ws, SU_CAB, [
        ('A', 'Ref', 7), ('B', 'Referencia', 28), ('C', 'Familia', 19),
        ('D', 'Food cost', 10),
        ('E', 'Margen por unidad (€)', 11),
        ('F', 'Mix (% de las unidades)', 11),
        ('G', 'Margen ponderado (€)', 11),
        ('H', '¿Food cost dentro del objetivo?', 11),
        ('I', '¿Rotación por encima del umbral?', 11),
        ('J', 'Veredicto', 16),
        ('K', 'Por qué', 70)])

    for i, ref in enumerate(D.CARTA):
        r = SU_INI + i
        mo = MO_INI + i
        mx = MX_INI + i
        motor.val(ws, 'A%d' % r, ref['id'])
        motor.val(ws, 'B%d' % r, ref['nombre'])
        motor.val(ws, 'C%d' % r, ref['familia'])
        motor.f(ws, 'D%d' % r, '={q}O{x}'.format(q=QMO, x=mo), fmt=C.PCT)
        motor.f(ws, 'E%d' % r, '={q}Q{x}'.format(q=QMO, x=mo), fmt=C.EUR)
        motor.f(ws, 'F%d' % r, '={q}D{x}'.format(q=QMIX, x=mx), fmt=C.DEC)
        motor.f(ws, 'G%d' % r, '=IFERROR(E{r}*F{r}/100,"")'.format(r=r),
                fmt=C.EUR)
        motor.f(ws, 'H%d' % r,
                '=IF(NOT(ISNUMBER(D{r})),"",IF(D{r}<={f},"Sí","No"))'
                .format(r=r, f=A(P_FC)))
        motor.f(ws, 'I%d' % r,
                '=IF(NOT(ISNUMBER(F{r})),"",IF(F{r}>={u},"Sí","No"))'
                .format(r=r, u=A(P_UMBRAL)))
        motor.f(ws, 'J%d' % r,
                '=IF(OR(H{r}="",I{r}=""),"",'
                'IF(AND(H{r}="No",I{r}="No"),"Retirar",'
                'IF(H{r}="No","Revisar precio","Mantener")))'.format(r=r))
        motor.f(ws, 'K%d' % r,
                '=IF(J{r}="","",'
                'IF(J{r}="Retirar",'
                '"Se pasa del food cost objetivo Y casi no rota: ocupa vitrina, '
                'genera merma y no paga el hueco. Fuera de la carta de apertura.",'
                'IF(J{r}="Revisar precio",'
                '"Rota bien pero se pasa del food cost objetivo: sube el precio, '
                'cambia el gramaje o renegocia el ingrediente que la encarece. '
                'Retirarla te quitaría rotación.",'
                '"Dentro del objetivo y con rotación: es la que sostiene la '
                'carta. Vigila que no se te vaya el coste de materia.")))'
                .format(r=r))
        ws['K%d' % r].alignment = Alignment(wrap_text=True, vertical='top')
        ws.row_dimensions[r].height = 32

    motor.val(ws, 'A%d' % SU_TOT, 'TOTAL DE LA CARTA', bold=True)
    C.crema(motor.f(ws, 'G%d' % SU_TOT,
                    '=SUM(G{a}:G{b})'.format(a=SU_INI, b=SU_FIN), fmt=C.EUR,
                    bold=True))
    C.crema(motor.f(ws, 'F%d' % SU_TOT,
                    '=SUM(F{a}:F{b})'.format(a=SU_INI, b=SU_FIN), fmt=C.DEC,
                    bold=True))
    motor.val(ws, 'K%d' % SU_TOT,
              'El margen ponderado del total es el margen de contribución de '
              '100 piezas vendidas con este mix.')
    ws['K%d' % SU_TOT].font = Font(size=8, color=C.GRIS)

    C.seccion(ws, 'A%d' % SU_RES, 'Cómo queda la carta')
    for i, v in enumerate(VEREDICTOS):
        r = SU_RES + 1 + i
        motor.val(ws, 'B%d' % r, 'Referencias con veredicto «%s»' % v)
        C.crema(motor.f(ws, 'E%d' % r,
                        '=COUNTIF(J{a}:J{b},"{v}")'.format(a=SU_INI, b=SU_FIN,
                                                           v=v),
                        fmt=C.ENT, bold=True))
        motor.f(ws, 'F%d' % r,
                '=IFERROR(SUMPRODUCT(--(J{a}:J{b}="{v}"),G{a}:G{b}),"")'
                .format(a=SU_INI, b=SU_FIN, v=v), fmt=C.EUR)
        motor.val(ws, 'G%d' % r, 'euros de margen ponderado que aportan')
        ws['G%d' % r].font = Font(size=8, color=C.GRIS)
    r = SU_RES + 1 + len(VEREDICTOS)
    motor.val(ws, 'B%d' % r, 'Margen ponderado medio de la carta (€)')
    C.crema(motor.f(ws, 'E%d' % r,
                    '=IFERROR(AVERAGE(G{a}:G{b}),"")'.format(a=SU_INI, b=SU_FIN),
                    fmt=C.EUR, bold=True))

    motor.semaforo_texto(ws, 'J%d:J%d' % (SU_INI, SU_FIN),
                         ((('Mantener'), 'C8E6C9', '1B5E20'),
                          (('Revisar precio'), 'FFF3C4', '7A5C00'),
                          (('Retirar'), 'FFCDD2', 'B71C1C')))
    motor.semaforo_texto(ws, 'H%d:H%d' % (SU_INI, SU_FIN),
                         ((('No'), 'FFCDD2', 'B71C1C'),))
    motor.semaforo_texto(ws, 'I%d:I%d' % (SU_INI, SU_FIN),
                         ((('No'), 'FFCDD2', 'B71C1C'),))
    motor.semaforo_isnumber(ws, 'E%d:E%d' % (SU_INI, SU_FIN), '$E%d' % SU_INI,
                            operador='<=', umbral='0')

    fila = r + 3
    for texto in (
        'CÓMO SE DECIDE. Dos preguntas, no cuatro. ¿El food cost está dentro de '
        'tu objetivo? ¿La referencia rota por encima de tu umbral? Si falla el '
        'margen y además no rota, fuera. Si falla sólo el margen, el problema '
        'es de precio o de proceso, no de carta: retirarla te quitaría '
        'rotación. Si no falla ninguna, se queda.',
        'ESTO NO ES INGENIERÍA DE MENÚ. La ingeniería de menú -Kasavana-Smith, '
        'Miller, Pavesic, Goal Value- está en la Guía Food Cost, con sus cuatro '
        'métodos y su comparativa. Aquí hay una decisión de surtido de '
        'APERTURA, que es otra cosa: se toma antes de vender nada y con el mix '
        'que TÚ supones.',
        'CUÁNDO SE VUELVE A MIRAR. A los tres meses de abrir, con ventas reales '
        'del TPV en la columna del mix, y luego cada cambio de temporada. Una '
        'carta de apertura que sigue igual al año es una carta que nadie ha '
        'mirado.',
        'UNA REFERENCIA PUEDE QUEDARSE AUNQUE PIERDA DINERO, Y HAY QUE SABERLO. '
        'El pan de barra es el caso clásico: margen corto y mucha rotación, '
        'pero es lo que trae al cliente todos los días. Si decides mantener '
        'algo que el semáforo manda retirar, escríbelo y ponle una fecha para '
        'revisarlo: eso es una decisión, no un despiste.',
    ):
        motor.val(ws, 'A%d' % fila, texto, wrap=True)
        ws.merge_cells('A%d:K%d' % (fila, fila))
        ws['A%d' % fila].font = Font(size=9)
        ws.row_dimensions[fila].height = 46
        fila += 1
    motor.val(ws, 'A%d' % (fila + 1), C.VERSION_LINE)
    ws['A%d' % (fila + 1)].font = Font(size=8, italic=True)
    ws.freeze_panes = 'D6'
    C.setup(ws)
    return ws


# --------------------------------------------------------------------------
# Mapa de celdas citables
# --------------------------------------------------------------------------
def mapa_celdas():
    m = [
        ('Coste de empresa anual del obrador', H_PAR, 'F%d' % PER_TOT,
         'salida'),
        ('Jornadas de obrador', H_PAR, 'B%d' % PER_TOT, 'salida'),
        ('Pagas del convenio al año', H_PAR, P_PAGAS, 'parametro'),
        ('Seguridad Social a cargo de la empresa', H_PAR, P_SS, 'parametro'),
        ('Horas anuales de contrato', H_PAR, P_HANIO, 'parametro'),
        ('Horas productivas sobre la jornada', H_PAR, P_RATIO, 'parametro'),
        ('Horas productivas del obrador al año', H_PAR, P_HPROD, 'salida'),
        ('Coste hora productiva de obrador', H_PAR, P_CHORA, 'salida'),
        ('IVA de pastelería', H_PAR, P_IVAP, 'parametro'),
        ('IVA del pan', H_PAR, P_IVAPAN, 'parametro'),
        ('IVA en zona de degustación', H_PAR, P_IVADEG, 'parametro'),
        ('Food cost objetivo', H_PAR, P_FC, 'parametro'),
        ('Margen bruto objetivo derivado', H_PAR, P_MB, 'salida'),
        ('Techo de la fila 9 del art. 4.1', H_PAR, P_T41, 'parametro'),
        ('Techo del art. 9.3', H_PAR, P_T93, 'parametro'),
        ('Plazo de consumo del art. 9.3', H_PAR, P_PLAZO, 'parametro'),
        ('Umbral analítico de sin gluten', H_PAR, P_GLUTEN, 'parametro'),
        ('Merma objetivo', H_PAR, P_MERMA, 'parametro'),
        ('Packaging sobre el coste del producto', H_PAR, P_PACK, 'parametro'),
        ('Piezas por cliente', H_PAR, P_PIEZAS, 'parametro'),
        ('Umbral de rotación del semáforo de surtido', H_PAR, P_UMBRAL,
         'parametro'),
        ('Bruto mensual del Jefe Pastelero', H_PAR, 'D%d' % PER_INI,
         'parametro'),
        ('Coste de empresa anual del Jefe Pastelero', H_PAR, 'F%d' % PER_INI,
         'salida'),
        ('Líneas del escandallo de las 30 referencias', H_ESC,
         'E%d' % RES_TOT, 'salida'),
        ('Aviso de descuadre entre líneas y referencias', H_ESC,
         'G%d' % RES_TOT, 'salida'),
        ('Materia prima de una tanda de cada referencia', H_ESC,
         'F%d' % RES_TOT, 'salida'),
        ('Coste de mano de obra de las 30 tandas', H_MO, 'H%d' % MO_TOT,
         'salida'),
        ('Food cost medio simple de las 30 referencias', H_MO, 'O%d' % MO_TOT,
         'salida'),
        ('Margen medio por unidad de las 30 referencias', H_MO,
         'Q%d' % MO_TOT, 'salida'),
        ('Peso medio de la mano de obra sobre el coste', H_MO, 'R%d' % MO_TOT,
         'salida'),
        ('Referencias que necesitan vitrina refrigerada', H_HUE,
         'G%d' % HU_RES, 'salida'),
        ('Referencias que van en vitrina de ambiente', H_HUE,
         'G%d' % (HU_RES + 1), 'salida'),
        ('Referencias con el techo de la fila 9 del art. 4.1', H_HUE,
         'G%d' % (HU_RES + 2), 'salida'),
        ('Referencias con el techo del art. 9.3', H_HUE, 'G%d' % (HU_RES + 3),
         'salida'),
        ('Referencias a las que aplican los dos techos', H_HUE,
         'G%d' % (HU_RES + 4), 'salida'),
        ('Referencias con plazo legal de 24 horas', H_HUE,
         'G%d' % (HU_RES + 5), 'salida'),
        ('Referencias sin huevo', H_HUE, 'G%d' % (HU_RES + 6), 'salida'),
        ('Referencias por la vía 63/20', H_HUE, 'G%d' % (HU_RES + 7),
         'salida'),
        ('Suma del mix de la carta', H_MIX, 'D%d' % MX_TOT, 'salida'),
        ('PVP medio ponderado con IVA', H_MIX, 'F%d' % (MX_RES + 1), 'salida'),
        ('Ticket medio con IVA', H_MIX, 'F%d' % (MX_RES + 3), 'salida'),
        ('Ticket medio sin IVA', H_MIX, 'F%d' % (MX_RES + 4), 'salida'),
        ('IVA medio de la carta', H_MIX, 'F%d' % (MX_RES + 5), 'salida'),
        ('Food cost de materia de la carta', H_MIX, 'F%d' % (MX_RES + 6),
         'salida'),
        ('Food cost servido con merma y packaging', H_MIX,
         'F%d' % (MX_RES + 7), 'salida'),
        ('Margen de contribución medio por pieza', H_MIX,
         'F%d' % (MX_RES + 9), 'salida'),
        ('Margen ponderado de 100 piezas de la carta', H_SUR, 'G%d' % SU_TOT,
         'salida'),
        ('Margen ponderado medio de la carta', H_SUR,
         'E%d' % (SU_RES + 1 + len(VEREDICTOS)), 'salida'),
    ]
    for i, v in enumerate(VEREDICTOS):
        m.append(('Referencias con veredicto «%s»' % v, H_SUR,
                  'E%d' % (SU_RES + 1 + i), 'salida'))
        m.append(('Margen ponderado de las referencias «%s»' % v, H_SUR,
                  'F%d' % (SU_RES + 1 + i), 'salida'))
    # --- las tres que se copian del kit, celda a celda ---------------------
    for ref_id in ('B1', 'PI3', 'T1'):
        i = [j for j, r in enumerate(D.CARTA) if r['id'] == ref_id][0]
        nombre = D.CARTA[i]['nombre']
        m += [
            ('Coste de materia por unidad de %s' % nombre, H_ESC,
             'G%d' % (RES_INI + i), 'salida'),
            ('Coste de materia de la tanda de %s' % nombre, H_ESC,
             'F%d' % (RES_INI + i), 'salida'),
            ('Coste de mano de obra por unidad de %s' % nombre, H_MO,
             'I%d' % (MO_INI + i), 'salida'),
            ('Coste total por unidad de %s' % nombre, H_MO,
             'K%d' % (MO_INI + i), 'salida'),
            ('Food cost de %s' % nombre, H_MO, 'O%d' % (MO_INI + i), 'salida'),
            ('Margen por unidad de %s' % nombre, H_MO, 'Q%d' % (MO_INI + i),
             'salida'),
            ('Uds por tanda de %s' % nombre, H_ESC, 'D%d' % (RES_INI + i),
             'entrada'),
            ('Minutos de mano de obra de la tanda de %s' % nombre, H_MO,
             'E%d' % (MO_INI + i), 'entrada'),
            ('PVP con IVA de %s' % nombre, H_MO, 'L%d' % (MO_INI + i),
             'entrada'),
        ]
    # Tres precios de compra citables: los que más mueven el coste de la carta.
    for ing in ('Mantequilla seca (82% MG)', 'Chocolate negro 70%',
                'Harina de fuerza'):
        j = INGREDIENTES.index(ing)
        m.append(('Precio de compra de %s' % ing, H_PAR, 'B%d' % (PRE_INI + j),
                  'entrada'))
    # --- una salida clave por referencia -----------------------------------
    for i, ref in enumerate(D.CARTA):
        n = ref['nombre']
        m += [
            ('Plazo legal del art. 9.3 de %s' % n, H_HUE, 'K%d' % (HU_INI + i),
             'salida'),
            ('Cuál manda en la temperatura de %s' % n, H_HUE,
             'J%d' % (HU_INI + i), 'salida'),
            ('Dónde va %s en el mostrador' % n, H_HUE, 'M%d' % (HU_INI + i),
             'salida'),
            ('Veredicto de surtido de %s' % n, H_SUR, 'J%d' % (SU_INI + i),
             'salida'),
        ]
        # La temperatura sólo se cita donde EXISTE: las referencias estables a
        # temperatura ambiente no tienen techo, y la celda está vacía a
        # propósito. Citar una celda vacía metería un hueco silencioso en el
        # prompt del redactor (D35).
        if D.temperatura_legal(ref)[0] is not None:
            m.append(('Temperatura de conservación de %s' % n, H_HUE,
                      'I%d' % (HU_INI + i), 'salida'))
    return m


NOTAS_MAPA = (
    'D23: la regla de margen es una sola. «Parámetros» pide el food cost '
    'objetivo y DERIVA el margen bruto; en ningún sitio se piden los dos. '
    'D11: la temperatura es el MÍNIMO de los techos que apliquen (fila 9 del '
    'art. 4.1 y art. 9.3) y el plazo del art. 9.3 va en su propia columna; la '
    'vida útil NO se calcula para ninguna de las 30 referencias: es celda '
    'verde con el texto «Por declarar en tu APPCC». R3 y R4: aquí no hay '
    'declaración de alérgenos ni registro de temperaturas; están en el Kit de '
    'Tareas Pastelería y en el Pack APPCC. Tarta de chocolate 70 %, croissants '
    'y macarons llevan el escandallo EXACTO de kit-escandallos/05-pasteleria.xlsx, '
    'copiado y declarado, nunca vinculado.'
)


# --------------------------------------------------------------------------
# Demostraciones con pycel
# --------------------------------------------------------------------------
def demo(ruta):
    from pycel import ExcelCompiler
    ok, fallos = [], []

    def prueba(nombre, cond, detalle=''):
        (ok if cond else fallos).append(nombre + (' — ' + detalle if detalle
                                                  else ''))

    exc = ExcelCompiler(ruta)

    def v(hoja, coord):
        return exc.evaluate("'%s'!%s" % (hoja, coord))

    # 1. La suma por referencia cuadra con la suma de las 226 líneas.
    tot_lineas = v(H_ESC, 'L%d' % ESC_TOT)
    tot_refs = v(H_ESC, 'F%d' % RES_TOT)
    prueba('el coste por referencia suma exactamente las 226 líneas',
           abs(tot_lineas - tot_refs) < 0.005,
           '%.4f frente a %.4f' % (tot_lineas, tot_refs))

    # 1bis. El recuento de líneas cuadra y los dos avisos dicen «Cuadra».
    prueba('el recuento de líneas del escandallo cuadra con las %d que hay' % NL,
           v(H_ESC, 'E%d' % RES_TOT) == NL
           and v(H_ESC, 'G%d' % RES_TOT) == 'Cuadra',
           'recuento %r · aviso de descuadre %r'
           % (v(H_ESC, 'E%d' % RES_TOT), v(H_ESC, 'G%d' % RES_TOT)))

    # 2. La napolitana de crema (rellena y no estable, vía 70/2) tiene los DOS
    #    techos y manda el de 4 °C; y le aplica el plazo de 24 h.
    i_b3 = [j for j, r in enumerate(D.CARTA) if r['id'] == 'B3'][0]
    r_b3 = HU_INI + i_b3
    prueba('la napolitana de crema sale a 4 °C, con los dos techos y el más '
           'bajo mandando',
           v(H_HUE, 'G%d' % r_b3) == 4 and v(H_HUE, 'H%d' % r_b3) == 8
           and v(H_HUE, 'I%d' % r_b3) == 4 and v(H_HUE, 'K%d' % r_b3) == 24,
           'fila 9 = %r · art. 9.3 = %r · conservación = %r · plazo = %r'
           % (v(H_HUE, 'G%d' % r_b3), v(H_HUE, 'H%d' % r_b3),
              v(H_HUE, 'I%d' % r_b3), v(H_HUE, 'K%d' % r_b3)))

    # 3. El croissant, estable a temperatura ambiente, no arrastra ningún techo
    #    ni ningún plazo: la hoja no se lo inventa.
    i_b1 = [j for j, r in enumerate(D.CARTA) if r['id'] == 'B1'][0]
    r_b1 = HU_INI + i_b1
    prueba('el croissant, estable a ambiente, sale sin techo y sin plazo',
           v(H_HUE, 'I%d' % r_b1) in ('', None)
           and v(H_HUE, 'K%d' % r_b1) == 'No aplica'
           and v(H_HUE, 'M%d' % r_b1) == 'Vitrina de ambiente',
           'conservación %r · plazo %r' % (v(H_HUE, 'I%d' % r_b1),
                                           v(H_HUE, 'K%d' % r_b1)))

    # 4. El semáforo de surtido no se enciende con texto: sin food cost, el
    #    veredicto queda vacío en vez de decir «Retirar».
    exc2 = ExcelCompiler(ruta)
    exc2.evaluate("'%s'!J%d" % (H_SUR, SU_INI))
    exc2.set_value("'%s'!L%d" % (H_MO, MO_INI), '')
    prueba('sin PVP tecleado, el veredicto de surtido queda vacío',
           exc2.evaluate("'%s'!J%d" % (H_SUR, SU_INI)) in ('', None),
           'devuelve %r' % (exc2.evaluate("'%s'!J%d" % (H_SUR, SU_INI)),))

    # 5. El veredicto CAMBIA al mover una entrada: con el food cost objetivo
    #    al 1 %, todo se sale de objetivo y nada puede quedar en «Mantener».
    antes = v(H_SUR, 'E%d' % (SU_RES + 1))          # cuántas «Mantener»
    exc3 = ExcelCompiler(ruta)
    exc3.evaluate("'%s'!E%d" % (H_SUR, SU_RES + 1))
    exc3.set_value("'%s'!%s" % (H_PAR, P_FC), 0.01)
    despues = exc3.evaluate("'%s'!E%d" % (H_SUR, SU_RES + 1))
    prueba('el veredicto de surtido cambia al mover el food cost objetivo',
           antes > 0 and despues == 0,
           '«Mantener» pasa de %r a %r' % (antes, despues))

    # 6. La regla de margen es una sola: el margen bruto es 1 menos el food
    #    cost, y se mueve solo.
    fc = v(H_PAR, P_FC)
    mb = v(H_PAR, P_MB)
    prueba('el margen bruto objetivo se deriva del food cost objetivo',
           abs(fc + mb - 1.0) < 1e-9, 'food cost %.2f + margen %.2f' % (fc, mb))

    # 7. El coste hora de obrador sale del convenio y de la SS, no del bruto.
    chora = v(H_PAR, P_CHORA)
    prueba('el coste hora de obrador se calcula desde plantilla y convenio',
           abs(chora - D.coste_hora_obrador()) < 0.01,
           '%.4f €/h frente a %.4f del juego de datos'
           % (chora, D.coste_hora_obrador()))

    # 8. El mix suma 100 y el ticket medio sale de la carta, no de un estudio.
    mix = v(H_MIX, 'D%d' % MX_TOT)
    ticket = v(H_MIX, 'F%d' % (MX_RES + 3))
    prueba('el mix suma 100 y el ticket medio sale de la carta',
           abs(mix - 100.0) < 0.001
           and abs(ticket - D.ticket_medio_con_iva()) < 0.01,
           'mix %.2f · ticket %.2f €' % (mix, ticket))

    return ok, fallos


# --------------------------------------------------------------------------
def main():
    D.gate_legal()
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_parametros(wb)
    hoja_escandallo(wb)
    hoja_mano_obra(wb)
    hoja_huevo(wb)
    hoja_mix(wb)
    hoja_surtido(wb)

    res = C.cerrar(wb, NOMBRE, TITULO, mapa_celdas(), NOTAS_MAPA)

    print('escrito: %s' % res['ruta'])
    print('hojas: %d · fórmulas: %d · celdas verdes: %d · verdes vacías: %d'
          % (res['hojas'], res['formulas'], res['verdes'],
             len(res['verdes_vacias'])))
    if res['verdes_vacias']:
        print('  VERDES VACÍAS: ' + ', '.join(res['verdes_vacias']))
    print('fórmulas que devuelven «sin dato» a propósito: %d' % res['sin_dato'])
    print('notas legales: %d · etiquetas en el mapa: %d'
          % (res['notas_legales'], res['mapa']))
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
