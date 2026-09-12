#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_checklist-legal-licencias-y-cacao.py — libro 8 de «Cómo Montar una
Chocolatería» (SPEC §2.2, fila 8; constructor C5).

Hojas: Instrucciones · Checklist Legal (F1-F6) · Árbol de Registro Sanitario ·
Suministro a Otros Minoristas · Ruta Doméstica · Cadmio y Analíticas ·
EUDR — Tu Papel en la Cadena · Registro de Formación · Cronograma y Ruta
Crítica.

QUÉ DECIDE ESTE LIBRO
---------------------
Qué papel te toca, en qué orden, y qué te obliga la norma del cacao. Es el libro
más diferencial del bloque legal: las cinco hojas de familia se heredan de
`guia-pasteleria/gen_checklist-legal-y-licencias.py` (1.710 líneas) y las dos
nuevas —cadmio y EUDR— no tienen molde en ningún producto de la casa.

LAS SEIS REGLAS DURAS QUE GOBIERNAN ESTE LIBRO
----------------------------------------------
1. **D19 — el 644.5 se publica SIEMPRE con su límite dentro, y la hoja NO emite
   un epígrafe de IAE por canal.** La nota del epígrafe es literal y tres de los
   cinco canales caen fuera de ella; ninguna fuente dice a qué epígrafe te
   mandan, así que la salida es **la pregunta redactada para el asesor**, no un
   veredicto. Es el mismo patrón con el que D33 resolvió la carga térmica.
2. **`CHN-39`/`CHN-43` — la comunicación autonómica NO habilita.** Y el mismo
   trámite funciona distinto en cada comunidad. Prohibido decir qué trámite pide
   un ayuntamiento concreto (`CHN-49d` está en EXCLUIDOS).
3. **D34 — el art. 3 es un ÁRBOL, no «tres umbrales».** Puerta de entrada; luego
   tres condiciones ACUMULATIVAS, y dentro de «marginal» dos vías ALTERNATIVAS
   (25 % del volumen anual **o** 500 kg/semana, dos entradas distintas).
   Prohibido «los 500 kg incluyen el mostrador»: el art. 3 habla del suministro
   a otros minoristas de distinta titularidad.
4. **D21 — la ruta doméstica tiene CINCO letras y la quinta es abierta**, y los
   TRES requisitos del art. 13.9 (`PA-29c`) **sólo se activan si tu comunidad ha
   ampliado la lista por la letra e)**. Para el bombón la ruta no está abierta
   por defecto: un semáforo sin esa condición delante sugiere que la ruta
   existe. Prohibido «hacer bombones en casa para vender es ilegal en España».
5. **`CHN-16b`/`CHN-84` — lo que es chocolate para la denominación no lo es para
   los contaminantes.** La nota (14) del Anexo I del Rgto. 2023/915 remite sólo
   a los puntos 2, 3 y 4 de la parte A del Anexo I de la Directiva 2000/36/CE.
   El **bombón no tiene límite propio de cadmio**: se le aplica la regla de
   alimentos compuestos. Prohibido «tu bombón tiene un límite de cadmio de X».
6. **D5 — el EUDR con su FECHA DE REVISIÓN dentro de la hoja**, y el paso «una
   chocolatería que compra cobertura es operador posterior, así que el
   aplazamiento del art. 38.3 no le alcanza» va como **inferencia declarada**,
   con el art. 2.15 ter como condición. Prohibido «tu fecha es el 30-12-2026
   pase lo que pase».

EL CRUCE QUE RECIBE (D32): 8 <- 9
---------------------------------
El cronograma calcula la fecha de apertura con duraciones SUPUESTAS; lo que de
verdad la mueve es el plazo de entrega de la maquinaria, que el lector teclea en
el libro 9. Llega por **celda verde** «trae aquí el plazo en semanas de
`checklist-equipamiento-y-proveedores-cacao.xlsx!Equipamiento`» con su valor por
defecto declarado, **más una fila de CUADRE** que avisa si la ruta crítica es más
corta que ese plazo: entonces la fecha la manda la maquinaria. Cero fórmulas que
nombren otro fichero.

DECISIONES TÉCNICAS
-------------------
* La ruta crítica se calcula con **aritmética de índices de mes**, no con
  funciones de fecha: `NETWORKDAYS` está prohibida en toda la familia. La
  holgura sale de una matriz de dependencias visible, con un valor centinela
  bloqueado (no verde: es un truco de cálculo, no un dato del lector).
* Estado de los trámites en PALABRAS: `☐`/`✓` no son WinAnsi.
* Los trámites sin importe conocido NO se rellenan a ojo: la celda dice «A
  presupuestar» y un contador te dice cuántos te faltan por pedir.
* Cada dato legal lleva su nota «Verificado el 12-09-2026 · norma · URL»;
  `gate_legal()` corre antes de escribir una sola. `PA-29c` es la única
  procedencia reutilizada de Pastelería (verificada el 10-09-2026) y se marca
  como tal.

Salida fija: build/checklist-legal-licencias-y-cacao.xlsx
             + build/mapa-checklist-legal-licencias-y-cacao.json
Uso: /usr/local/bin/python3 gen_checklist-legal-licencias-y-cacao.py
Via: Claude Code
"""
import datetime
import json
import os
import re
import sys

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Font, PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import _comun_chocolateria as C                                # noqa: E402
import _comun_libros_8_9 as X                                  # noqa: E402
import datos_ejemplo as D                                      # noqa: E402
import motor                                                   # noqa: E402

NOMBRE = 'checklist-legal-licencias-y-cacao'
TITULO = 'Checklist legal, licencias y la norma del cacao'

H_INS = 'Instrucciones'
H_CHK = 'Checklist Legal (F1-F6)'
H_ARB = 'Árbol de Registro Sanitario'
H_SUM = 'Suministro a Otros Minoristas'
H_DOM = 'Ruta Doméstica'
H_CAD = 'Cadmio y Analíticas'
H_EUDR = 'EUDR — Tu Papel en la Cadena'
H_FOR = 'Registro de Formación'
H_GAN = 'Cronograma y Ruta Crítica'

N = motor.NARROW

HECHO, PENDIENTE, NOAPLICA = 'Hecho', 'Pendiente', 'N/A'
SI, NO, NOSE = 'Sí', 'No', 'No lo sé'
SI_NO = (SI, NO)
SI_NO_NOSE = (SI, NO, NOSE)
SIN_IMPORTE = 'A presupuestar'
SIN_PAGAR = 'Sin pagar'
SIN_DEP = '-'
FECHA_BASE = datetime.date(2026, 9, 12)
CCAA_LISTA = list(D.CCAA_EJEMPLO) + ['Otra (busca su decreto)']

#: `datos_ejemplo` declara la respuesta del 644.5 sin tildes («no lo se»); el
#: desplegable de la hoja usa el vocabulario de la familia. Sin este mapa, el
#: valor sembrado no casaría con su propia validación de datos.
RESP_644 = {'si': SI, 'no': NO, 'no lo se': NOSE}

#: LA CITA DEL 644.5 SE TOMA DE LA VERIFICACIÓN LEGAL, NO DE `datos_ejemplo`.
#: `datos_ejemplo.NOTA_644_5` trae el entrecomillado con los acentos quitados
#: («la fabricacion de bombones…»), y la SPEC §2.3 dice que sólo se entrecomilla
#: lo que está en el BOE y que la verificación legal manda sobre la síntesis. La
#: `cita_literal` de `CHN-72` es la buena, y se usa TAMBIÉN dentro de la pregunta
#: al asesor, sustituyendo exactamente el mismo fragmento: si la cita cambia en
#: una celda y no en la de al lado, el lector ve dos versiones de la misma norma.
CITA_644 = X.cita_legal('CHN-72') or D.NOTA_644_5
_FRAGMENTO_SIN_TILDES = ('siempre que su comercializacion se realice en las '
                         'propias dependencias de venta')
_FRAGMENTO_LITERAL = ('siempre que su comercialización se realice en las '
                      'propias dependencias de venta')


def con_cita_literal(texto):
    """Repone el fragmento entrecomillado del 644.5 en su forma literal."""
    return texto.replace(_FRAGMENTO_SIN_TILDES, _FRAGMENTO_LITERAL)

#: Fecha en que se verificó la reutilización de Pastelería (SPEC §2.2, fila 8).
FECHA_PA = '10-09-2026'

#: Ids legales de este libro. `gate_legal()` corre antes de escribir una nota.
IDS_LEGALES = dict(
    (k, v) for k, v in D.IDS_LEGALES_REQUERIDOS.items() if v[1] == 8)


def ie(expr):
    return motor.iferror(expr)


def nota_reutilizada(ws, coord, pid):
    """Nota de procedencia de un id `PA-*` del JSON común: la CUARTA
    procedencia válida que declara la SPEC para este libro. Ninguna ficha
    `CHN-*` cubre los tres requisitos del art. 13.9, así que se cita como
    REUTILIZACIÓN de Pastelería, con SU fecha de verificación (10-09-2026), y
    así se dice dentro de la propia nota."""
    f = D.ficha(pid)
    if not f:
        raise SystemExit('ficha(%r): ese id no existe en el JSON común' % pid)
    texto = ('Verificado el %s %s %s %s %s %s Reutilizado de la verificación '
             'legal de «Cómo Montar una Pastelería» (%s): ninguna ficha CHN-* '
             'de este producto cubre el art. 13.9.'
             % (FECHA_PA, chr(183), f.get('fuente_titulo') or pid, chr(183),
                f.get('url') or '', chr(183), pid))
    ws[coord].comment = Comment(texto, 'AI Chef Pro', height=140, width=470)
    X.NOTAS_LEGALES.append((ws.title, coord, pid))
    return texto


# --------------------------------------------------------------------------
# Cruce 8 <- 9: el plazo de entrega crítico lo publica el libro 9 en su mapa.
# --------------------------------------------------------------------------
MAPA9 = os.path.join(C.BUILD_DIR,
                     'mapa-checklist-equipamiento-y-proveedores-cacao.json')
CRUCE9_ETIQUETA = 'PLAZO CRÍTICO DE ENTREGA (semanas) — viaja al libro 8'
CRUCE9_REF = ('checklist-equipamiento-y-proveedores-cacao.xlsx!Equipamiento')
CRUCE9_DEFECTO = float(D.plazo_critico_semanas())
if os.path.exists(MAPA9):
    with open(MAPA9, encoding='utf-8') as _fh:
        _m9 = json.load(_fh)
    if CRUCE9_ETIQUETA in _m9:
        CRUCE9_REF = _m9[CRUCE9_ETIQUETA]['ref'].split('.xlsx!', 1)[1]
        CRUCE9_REF = ('checklist-equipamiento-y-proveedores-cacao.xlsx!'
                      + CRUCE9_REF)
        CRUCE9_DEFECTO = float(_m9[CRUCE9_ETIQUETA]['valor'])


# ==========================================================================
# Filas de la hoja «Checklist Legal (F1-F6)»
# ==========================================================================
K_CAB = 5
_fila = K_CAB + 1
FASES = []
for _f in sorted(D.FASES_CHECKLIST):
    _items = [i for i, it in enumerate(D.CHECKLIST_LEGAL) if it[0] == _f]
    _sec = _fila
    _ini = _sec + 1
    _fin = _ini + len(_items) - 1
    _cont = _fin + 1
    FASES.append((_f, D.FASES_CHECKLIST[_f], _sec, _ini, _fin, _cont, _items))
    _fila = _cont + 2
K_INI = FASES[0][3]
K_FIN = FASES[-1][4]

K_SEC_RES = _fila
K_TOTAL = K_SEC_RES + 1
K_HECHOS = K_SEC_RES + 2
K_NA = K_SEC_RES + 3
K_AVANCE = K_SEC_RES + 4
K_PREV = K_SEC_RES + 5
K_REAL = K_SEC_RES + 6
K_DESV = K_SEC_RES + 7
K_SINIMP = K_SEC_RES + 8
K_CCAA_N = K_SEC_RES + 9

K_TU_SEC = K_CCAA_N + 2
K_TU_CCAA = K_TU_SEC + 1
K_ARTES = K_TU_SEC + 2

K_CAN_SEC = K_ARTES + 2
K_CAN_CAB = K_CAN_SEC + 1
K_CAN_INI = K_CAN_CAB + 1
K_CAN_FIN = K_CAN_INI + len(D.CANALES) - 1
K_CAN_USO = K_CAN_FIN + 1
K_CAN_FUERA = K_CAN_FIN + 2
K_CAN_NOSE = K_CAN_FIN + 3
K_CAN_VER = K_CAN_FIN + 4
K_CAN_PREG = K_CAN_FIN + 5

K_NOTA = K_CAN_PREG + 2
K_LISTAS = K_NOTA + 4


# ==========================================================================
# Hoja «Instrucciones»
# ==========================================================================
PASOS = [
    '1. Hoja «Checklist Legal (F1-F6)»: los treinta y tres trámites en el orden '
    'en que hay que hacerlos, repartidos en seis fases. Marca el estado, '
    'escribe el coste que te presupuestan y el que acabas pagando, y pon las '
    'dos fechas. Debajo, dos bloques propios de este negocio: la artesanía '
    'alimentaria y, sobre todo, la tabla de CANALES, que te dice cuáles de los '
    'cinco se salen de la nota del epígrafe 644.5.',
    '2. Hoja «Árbol de Registro Sanitario»: tres preguntas y un veredicto. '
    'Corrige el error más caro del sector: una chocolatería que vende al '
    'consumidor final está EXCLUIDA del registro estatal (RGSEAA), y lo que le '
    'toca es una comunicación o declaración responsable a su comunidad '
    'autónoma, que además NO habilita para abrir.',
    '3. Hoja «Suministro a Otros Minoristas»: el árbol del art. 3 del '
    'RD 1021/2022, con su puerta de entrada delante. Si no sirves a otros '
    'comercios de distinta titularidad, este artículo no te aplica y la hoja te '
    'lo dice en la primera línea. Si te aplica, las tres condiciones son '
    'ACUMULATIVAS y dentro de «marginal» hay DOS vías alternativas.',
    '4. Hoja «Ruta Doméstica»: si te planteas empezar desde casa. La lista '
    'estatal del art. 13.8 tiene CINCO letras y la quinta la rellena cada '
    'comunidad: por eso la hoja te pregunta primero si la tuya lo ha hecho, y '
    'sólo entonces te enseña los tres requisitos del art. 13.9.',
    '5. Hoja «Cadmio y Analíticas»: la hoja que nadie tiene. Lo que es '
    'chocolate para la denominación NO lo es para los contaminantes, y el '
    'bombón no tiene límite propio de cadmio. Aquí se decide si necesitas '
    'analítica propia, con qué frecuencia y cuánto te cuesta al año.',
    '6. Hoja «EUDR — Tu Papel en la Cadena»: cuatro preguntas y sabes si eres '
    'operador, operador posterior o comerciante, qué te toca y qué fecha te '
    'corre. Lleva DENTRO su fecha de revisión: es la norma más viva de todas '
    'las que tocan a este negocio.',
    '7. Hoja «Registro de Formación»: una línea por persona con la fecha, el '
    'contenido y la caducidad que TÚ fijas. El «carnet de manipulador» no '
    'existe: lo que hay que tener es este registro, y la responsabilidad de '
    'tenerlo es de la empresa.',
    '8. Hoja «Cronograma y Ruta Crítica»: trece hitos con su duración y sus '
    'dependencias. La hoja calcula cuándo empieza y acaba cada uno, cuánta '
    'holgura tiene, cuáles están en la ruta crítica y en qué mes acabas '
    'abriendo, y te avisa si esa fecha cae dentro de una campaña alta o si el '
    'plazo de la maquinaria es más largo que todo tu papeleo.',
]

NOTAS_LIBRO = [
    'EL ARGUMENTO MÁS ÚTIL DE ESTE PRODUCTO, Y SU LÍMITE, VAN JUNTOS. Puedes '
    'fabricar bombones sin darte de alta como industria mientras los vendas en '
    'tu propia tienda: la nota del epígrafe 644.5 lo dice con todas las '
    'letras. En el momento en que sirves a otros comercios, a empresas o envías '
    'fuera, eso cambia — y la tabla de canales de la primera hoja te dice '
    'exactamente cuándo.',
    'PERO ESTA HOJA NO TE DA UN EPÍGRAFE DE IAE POR CANAL, Y NO ES UN OLVIDO: '
    'NINGUNA FUENTE LO DA. Lo que sí está verificado es que una cuota faculta '
    'EXCLUSIVAMENTE para su actividad, que la venta online al consumidor SIGUE '
    'SIENDO comercio al por menor, y que el epígrafe industrial faculta para '
    'vender al por mayor y al por menor pero te saca del amparo de la Ley '
    '12/2012. Con eso, la salida correcta es la PREGUNTA redactada para tu '
    'asesor fiscal, que la hoja te escribe entera.',
    'LA COMUNICACIÓN AUTONÓMICA NO HABILITA PARA ABRIR, y eso corta en los dos '
    'sentidos: no tienes que esperar a que te contesten, pero tampoco te '
    'protege de nada si el resto no está en regla. Y el mismo trámite funciona '
    'distinto en cada comunidad: en una se presenta al inicio de la actividad y '
    'no habilita; en otra es condición única y suficiente para iniciar, y lleva '
    'tasa.',
    'NINGÚN AYUNTAMIENTO PUEDE EXIGIRTE LICENCIA PREVIA DE ACTIVIDAD hasta 750 '
    'metros cuadrados, porque el Anexo de la Ley 12/2012 incluye el epígrafe '
    '644.5. OJO: ese Anexo NO contiene ningún grupo de la agrupación 67, así '
    'que la chocolatería de TAZA queda fuera de ese amparo. Y está PROHIBIDO '
    'que este producto te diga qué trámite pide Madrid o Barcelona: no se ha '
    'abierto ninguna ordenanza municipal.',
    'EL BOMBÓN NO TIENE LÍMITE PROPIO DE CADMIO. Lo que es «producto de cacao y '
    'de chocolate» para los contaminantes son el cacao en polvo, el chocolate y '
    'el chocolate con leche: al bombón se le aplica la regla de los alimentos '
    'compuestos. Cualquiera que te venda una analítica diciéndote «tu bombón '
    'tiene un límite de X» te está vendiendo una cifra que no existe.',
    'EL CARNET DE MANIPULADOR NO EXISTE. La obligación viva es del empresario: '
    'garantizar la formación de cada persona de acuerdo con su actividad '
    'laboral y PODER ACREDITARLA. Eso es un registro, no un carnet, y lo monta '
    'la séptima hoja.',
    'ESTE LIBRO NO ES UN DICTAMEN JURÍDICO. Cada dato normativo lleva en su '
    'celda un comentario con la norma, el artículo y el enlace al texto '
    'consolidado, verificados el 12 de septiembre de 2026. Lo que hay que hacer '
    'con eso es leerlos y contrastarlos con tu ayuntamiento y con tu comunidad, '
    'no fiarte de una casilla.',
]

FRONTERA = [
    ('kit-tareas-chocolateria (12' + N + '€)',
     'Las curvas de templado, las fichas de moldeado, el calendario anual y las '
     'tareas por perfil.',
     'El kit NO tiene una sola hoja legal. Todo lo de este libro es nuevo para '
     'quien ya lo tenga.'),
    ('pack-appcc (21 xlsx)',
     'Los registros del plan de APPCC ya montados y listos para rellenar, y la '
     'matriz de alérgenos por elaboración.',
     'Aquí sólo hay una FILA de checklist que dice «redacta el plan y designa '
     'por su nombre al responsable». El plan en sí es aquel producto.'),
    ('checklist-equipamiento-y-proveedores-cacao.xlsx (libro 9 de esta guía)',
     'El plazo de entrega de cada equipo y el papel EUDR de cada PROVEEDOR.',
     'El cronograma de este libro trabaja en MESES y con duraciones supuestas. '
     'El plazo real de la maquinaria lo tecleas allí y lo traes aquí a la celda '
     'verde del cruce: es lo que de verdad mueve tu fecha de apertura.'),
    ('plan-financiero-3-anos-chocolateria.xlsx (libro 7 de esta guía)',
     'Los euros: qué cuesta cada bloque de inversión y cuándo sale de caja.',
     'Los costes de este checklist son los de los TRÁMITES. La obra, el '
     'equipamiento y el fondo de maniobra están allí.'),
]


def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS, 0)
    C.anchos(ws, {'A': 44, 'B': 44, 'C': 44})
    motor.val(ws, 'A1', TITULO)
    ws['A1'].font = Font(bold=True, size=16, color=C.ORO)
    ws.row_dimensions[1].height = 26
    motor.val(ws, 'A2', C.SUBTITULO)
    ws['A2'].font = Font(size=9)
    motor.val(ws, 'A3', 'Para qué sirve: saber qué papel te toca, en qué orden, '
                        'y qué te obliga la norma del cacao.')
    ws['A3'].font = Font(italic=True, size=9)

    fila = 5
    C.seccion(ws, 'A%d' % fila, 'Instrucciones de uso')
    fila += 1
    for paso in PASOS:
        C.parrafo(ws, fila, paso, 'A', 'C', alto=68)
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, C.NOTA_VERDES)
    ws['A%d' % fila].fill = PatternFill('solid', fgColor=motor.VERDE)
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Lo que conviene saber antes de empezar')
    fila += 1
    for texto in NOTAS_LIBRO:
        C.parrafo(ws, fila, texto, 'A', 'C', alto=84)
        fila += 1
    fila += 1

    C.seccion(ws, 'A%d' % fila,
              'Qué hace este libro y qué hace otro (para no teclear dos veces)')
    fila += 1
    C.cabecera(ws, fila, [('A', 'Producto o libro'), ('B', 'Qué aporta'),
                          ('C', 'Qué NO hace este libro')], altura=26)
    fila += 1
    for producto, aporta, no_hace in FRONTERA:
        motor.val(ws, 'A%d' % fila, producto, bold=True, wrap=True)
        motor.val(ws, 'B%d' % fila, aporta, wrap=True)
        motor.val(ws, 'C%d' % fila, no_hace, wrap=True)
        ws.row_dimensions[fila].height = 68
        fila += 1
    fila += 1

    C.seccion(ws, 'A%d' % fila, 'Cada cuánto se usa este libro')
    fila += 1
    C.parrafo(ws, fila,
              'Cadencia: el checklist y el cronograma, UNA VEZ A LA SEMANA '
              'desde que decides abrir hasta que abres. Los árboles -registro '
              'sanitario, suministro a otros minoristas y ruta doméstica-, UNA '
              'VEZ AL PRINCIPIO y otra CADA VEZ QUE CAMBIES DE CANAL: el día '
              'que aceptes servir a la cafetería de al lado estarás cambiando '
              'de régimen sin darte cuenta. La hoja del EUDR, cada vez que '
              'cambies de proveedor y, en todo caso, en la fecha de revisión '
              'que ella misma lleva dentro. El registro de formación, cada vez '
              'que entra alguien y cuando caduca la formación de alguien.',
              'A', 'C', alto=92)
    fila += 2
    C.parrafo(ws, fila, C.NOTA_DESPROTEGER, 'A', 'C', alto=28)
    fila += 2
    C.pie(ws, fila, 'A', 'C')
    C.pagina(ws, apaisado=False, area='A1:C%d' % (fila + 2))
    return ws


# ==========================================================================
# Hoja «Checklist Legal (F1-F6)»
# ==========================================================================
def hoja_checklist(wb):
    ws = wb.create_sheet(H_CHK)
    C.anchos(ws, {'A': 15, 'B': 7, 'C': 62, 'D': 16, 'E': 12, 'F': 16,
                  'G': 16, 'H': 14, 'I': 14, 'J': 15, 'K': 96})
    C.encabezar(ws, 'Checklist legal y de licencias, en seis fases',
                'Treinta y tres trámites en el orden en que hay que hacerlos. '
                'Marca el estado, escribe lo que te presupuestan y lo que '
                'acabas pagando, y pon las dos fechas. Lo que cambia según tu '
                'comunidad autónoma va marcado en su columna.', col_fin='K')
    C.cabecera(ws, K_CAB,
               [('A', 'Estado'), ('B', 'Fase'), ('C', 'Trámite'),
                ('D', 'Responsable'), ('E', 'Plazo (días)'),
                ('F', 'Coste previsto (€)'), ('G', 'Coste real (€)'),
                ('H', 'Fecha objetivo'), ('I', 'Fecha hecha'),
                ('J', '¿Cambia por CCAA?'), ('K', 'Notas')])

    refs, fila_listas = C.bloque_listas(
        ws, K_LISTAS,
        [('Estado del trámite', [PENDIENTE, HECHO, NOAPLICA]),
         ('Sí o No', list(SI_NO)),
         ('Sí, No o No lo sé', list(SI_NO_NOSE)),
         ('Comunidad autónoma', CCAA_LISTA)], col='A')

    casillas, ccaas = [], []
    for fase, titulo, sec, ini, fin, cont, items in FASES:
        C.seccion(ws, 'A%d' % sec, '%s' % fase + ' ' + chr(183) + ' ' + titulo)
        for letra in 'BCDEFGHIJK':
            motor.val(ws, letra + str(sec), '')
            ws[letra + str(sec)].fill = PatternFill('solid',
                                                    fgColor=C.CABECERA)
        for pos, idx in enumerate(items):
            (f, tramite, responsable, plazo, coste, fuente, cambia,
             nota_txt) = D.CHECKLIST_LEGAL[idx]
            fila = ini + pos
            X.entrada(ws, 'A%d' % fila, PENDIENTE, etiqueta=tramite,
                      align='center')
            casillas.append('A%d' % fila)
            motor.val(ws, 'B%d' % fila, fase, align='center')
            motor.val(ws, 'C%d' % fila, tramite, wrap=True)
            motor.val(ws, 'D%d' % fila, responsable)
            X.entrada(ws, 'E%d' % fila, plazo, fmt=C.FMT_ENT, etiqueta=tramite,
                      align='center')
            X.entrada(ws, 'F%d' % fila,
                      coste if coste is not None else SIN_IMPORTE,
                      fmt=(C.FMT_EUR if coste is not None else None),
                      etiqueta=tramite)
            X.entrada(ws, 'G%d' % fila, SIN_PAGAR, etiqueta=tramite)
            X.entrada(ws, 'H%d' % fila, FECHA_BASE, fmt=C.FMT_FECHA,
                      etiqueta=tramite)
            X.entrada(ws, 'I%d' % fila, FECHA_BASE, fmt=C.FMT_FECHA,
                      etiqueta=tramite)
            X.entrada(ws, 'J%d' % fila, SI if cambia else NO, etiqueta=tramite,
                      align='center')
            ccaas.append('J%d' % fila)
            C.nota(ws, 'K%d' % fila,
                   (nota_txt or '') + ('  [Fuente: %s]' % fuente if fuente
                                       else ''))
            ws.row_dimensions[fila].height = 40
            for chn in re.findall(r'CHN-[0-9]+[a-z]*(?:-int)?', fuente):
                if D.nota_legal(chn):
                    X.nota_celda(ws, 'C%d' % fila, chn)
                    break
        motor.val(ws, 'C%d' % cont, 'AVANCE DE LA FASE ' + fase, bold=True)
        motor.f(ws, 'D%d' % cont,
                ie('COUNTIF(A%d:A%d,"%s")' % (ini, fin, HECHO)), fmt=C.FMT_ENT,
                bold=True)
        motor.f(ws, 'E%d' % cont,
                ie('COUNTIF(B%d:B%d,"%s")' % (ini, fin, fase)), fmt=C.FMT_ENT)
        motor.f(ws, 'F%d' % cont, ie('SUMIF(F%d:F%d,">=0")' % (ini, fin)),
                fmt=C.FMT_EUR)
        motor.f(ws, 'G%d' % cont, ie('SUMIF(G%d:G%d,">=0")' % (ini, fin)),
                fmt=C.FMT_EUR)
        motor.f(ws, 'J%d' % cont,
                ie('IF(E{0}=0,"",(D{0}+COUNTIF(A{1}:A{2},"{3}"))/E{0})'
                   .format(cont, ini, fin, NOAPLICA)), fmt=C.FMT_PCT,
                bold=True)
        X.total_fila(ws, cont, 'ABCDEFGHIJK')
        motor.semaforo_isnumber(ws, 'J%d:J%d' % (cont, cont), '$J$%d' % cont,
                                operador='<', umbral='1',
                                bg=motor.CF_AMBAR_BG, fg=motor.CF_AMBAR_FG)
        C.nota(ws, 'K%d' % cont,
               'Hechos ' + chr(183) + ' trámites de la fase ' + chr(183)
               + ' coste previsto ' + chr(183) + ' coste real ' + chr(183)
               + ' % de avance (los «N/A» cuentan como resueltos).')

    C.dv_rango(ws, casillas, refs['Estado del trámite'],
               'Marca el estado del trámite',
               'Elige %s, %s o %s de la lista del pie de la hoja.'
               % (PENDIENTE, HECHO, NOAPLICA))
    C.dv_rango(ws, ccaas, refs['Sí o No'], 'Marca Sí o No',
               'Elige «Sí» o «No» de la lista del pie de la hoja.')

    # --- resumen ----------------------------------------------------------
    C.seccion(ws, 'A%d' % K_SEC_RES, 'RESUMEN DE TODO EL EXPEDIENTE')
    for letra in 'BCDEFGHIJK':
        motor.val(ws, letra + str(K_SEC_RES), '')
        ws[letra + str(K_SEC_RES)].fill = PatternFill('solid',
                                                      fgColor=C.CABECERA)

    def res(fila, etiqueta, formula, fmt=None, nota_txt=None, bold=None):
        motor.val(ws, 'C%d' % fila, etiqueta, bold=bold)
        motor.f(ws, 'D%d' % fila, formula, fmt=fmt, bold=bold)
        if nota_txt:
            C.nota(ws, 'K%d' % fila, nota_txt)

    res(K_TOTAL, 'Trámites del expediente',
        ie('COUNTIF(B%d:B%d,"F*")' % (K_INI, K_FIN)), C.FMT_ENT)
    res(K_HECHOS, 'Trámites hechos',
        ie('COUNTIF(A%d:A%d,"%s")' % (K_INI, K_FIN, HECHO)), C.FMT_ENT)
    res(K_NA, 'Trámites que no te aplican (N/A)',
        ie('COUNTIF(A%d:A%d,"%s")' % (K_INI, K_FIN, NOAPLICA)), C.FMT_ENT)
    res(K_AVANCE, 'Avance del expediente (%)',
        ie('IF(D{0}=0,"",(D{1}+D{2})/D{0})'
           .format(K_TOTAL, K_HECHOS, K_NA)), C.FMT_PCT, bold=True)
    motor.semaforo_isnumber(ws, 'D%d:D%d' % (K_AVANCE, K_AVANCE),
                            '$D$%d' % K_AVANCE, operador='<', umbral='1',
                            bg=motor.CF_AMBAR_BG, fg=motor.CF_AMBAR_FG)
    res(K_PREV, 'Coste previsto total del checklist (€)',
        ie('SUMIF(F%d:F%d,">=0")' % (K_INI, K_FIN)), C.FMT_EUR,
        'OJO: esta suma NO es «lo que cuestan los papeles». Dentro está la obra '
        'civil y la climatización, que son dos líneas de la fase F4 y se llevan '
        'ellas solas la mayor parte. Los euros de la apertura, ordenados por '
        'bloques y con su IVA, están en «calculadora-capex-chocolateria.xlsx»: '
        'aquí sólo se controla que cada trámite tenga su importe y su fecha.')
    res(K_REAL, 'Coste real total del checklist (€)',
        ie('SUMIF(G%d:G%d,">=0")' % (K_INI, K_FIN)), C.FMT_EUR,
        'Se rellena solo a medida que vas pagando. Mientras esté a cero, la '
        'desviación de abajo no dice nada.')
    res(K_DESV, 'Desviación (real menos previsto, €)',
        ie('D%d-D%d' % (K_REAL, K_PREV)), C.FMT_EUR, bold=True)
    motor.semaforo_isnumber(ws, 'D%d:D%d' % (K_DESV, K_DESV),
                            '$D$%d' % K_DESV, operador='>', umbral='0')
    res(K_SINIMP, 'Trámites sin importe (a presupuestar)',
        ie('COUNTIF(F%d:F%d,"%s")' % (K_INI, K_FIN, SIN_IMPORTE)), C.FMT_ENT,
        'Son los que dependen de tu ayuntamiento, de tu comunidad o de un '
        'proveedor. No se rellenan a ojo: se piden. Mientras esta cifra no sea '
        'cero, tu presupuesto de apertura está incompleto.')
    motor.semaforo_isnumber(ws, 'D%d:D%d' % (K_SINIMP, K_SINIMP),
                            '$D$%d' % K_SINIMP, operador='>', umbral='0',
                            bg=motor.CF_AMBAR_BG, fg=motor.CF_AMBAR_FG)
    res(K_CCAA_N, 'Trámites que cambian según tu comunidad autónoma',
        ie('COUNTIF(J%d:J%d,"%s")' % (K_INI, K_FIN, SI)), C.FMT_ENT,
        'Cada uno de éstos hay que confirmarlo con TU comunidad. Los ejemplos '
        'del libro son Madrid, Cataluña, Andalucía y la Comunitat Valenciana, y '
        'son eso: ejemplos.')
    X.total_fila(ws, K_AVANCE, 'CD')
    X.total_fila(ws, K_DESV, 'CD')

    # --- tu comunidad y la artesanía (D10) --------------------------------
    C.seccion(ws, 'A%d' % K_TU_SEC, 'TU COMUNIDAD Y LA ARTESANÍA ALIMENTARIA')
    for letra in 'BCDEFGHIJK':
        motor.val(ws, letra + str(K_TU_SEC), '')
        ws[letra + str(K_TU_SEC)].fill = PatternFill('solid',
                                                     fgColor=C.CABECERA)
    motor.val(ws, 'C%d' % K_TU_CCAA, '¿En qué comunidad autónoma vas a abrir?',
              bold=True)
    X.entrada(ws, 'D%d' % K_TU_CCAA, CCAA_LISTA[0],
              etiqueta='Comunidad autónoma')
    C.dv_rango(ws, ['D%d' % K_TU_CCAA], refs['Comunidad autónoma'],
               'Elige tu comunidad',
               'Cuatro comunidades de EJEMPLO más «Otra». Si la tuya no está, '
               'busca «registro sanitario establecimientos alimentarios '
               'menores» más el nombre de tu comunidad: el decreto que salga es '
               'el tuyo.')
    C.nota(ws, 'K%d' % K_TU_CCAA,
           'El mismo trámite funciona distinto en cada comunidad: en Madrid se '
           'presenta simultáneamente al inicio de la actividad y no habilita; '
           'en la Comunitat Valenciana es condición única y suficiente para '
           'iniciar, y lleva tasa. Cuatro de EJEMPLO, no una lista cerrada.')
    X.nota_celda(ws, 'D%d' % K_TU_CCAA, 'CHN-43')
    motor.val(ws, 'C%d' % K_ARTES, D.FILA_ARTESANIA['pregunta'], bold=True,
              wrap=True)
    X.entrada(ws, 'D%d' % K_ARTES, NOSE, etiqueta='Artesanía alimentaria',
              align='center')
    C.dv_rango(ws, ['D%d' % K_ARTES], refs['Sí, No o No lo sé'],
               'Marca Sí, No o No lo sé',
               'Es una acreditación VOLUNTARIA: nadie te obliga a inscribirte.')
    C.nota(ws, 'K%d' % K_ARTES, D.FILA_ARTESANIA['nota'])
    X.nota_celda(ws, 'D%d' % K_ARTES, 'CHN-52')
    ws.row_dimensions[K_ARTES].height = 40

    # --- canales y el 644.5 (D19) -----------------------------------------
    C.seccion(ws, 'A%d' % K_CAN_SEC,
              'TUS CANALES: ¿TE SACAN DE LA NOTA DEL EPÍGRAFE 644.5?')
    for letra in 'BCDEFGHIJK':
        motor.val(ws, letra + str(K_CAN_SEC), '')
        ws[letra + str(K_CAN_SEC)].fill = PatternFill('solid',
                                                      fgColor=C.CABECERA)
    C.cabecera(ws, K_CAN_CAB,
               [('A', 'Nº'), ('B', 'Canal'), ('C', '¿Vas a vender por él?'),
                ('D', '¿Te saca de la nota?'), ('E', 'Fuente'),
                ('F', 'Qué está verificado'), ('K', 'La nota literal del '
                                                    'epígrafe')], altura=32)
    ws.merge_cells('F%d:J%d' % (K_CAN_CAB, K_CAN_CAB))
    v_usa, v_saca = [], []
    for i, fila_canal in enumerate(D.filas_canal_644_5()):
        r = K_CAN_INI + i
        motor.val(ws, 'A%d' % r, i + 1, fmt=C.FMT_ENT, align='center')
        motor.val(ws, 'B%d' % r, fila_canal['canal'], wrap=True)
        X.entrada(ws, 'C%d' % r, SI if i == 0 else NO,
                  etiqueta='¿Vendes por ' + fila_canal['canal'] + '?',
                  align='center')
        v_usa.append('C%d' % r)
        X.entrada(ws, 'D%d' % r, RESP_644[fila_canal['sale_de_la_nota']],
                  etiqueta='¿' + fila_canal['canal'] + ' te saca del 644.5?',
                  align='center')
        v_saca.append('D%d' % r)
        motor.val(ws, 'E%d' % r, fila_canal['fuente'])
        ws.merge_cells('F%d:J%d' % (r, r))
        motor.val(ws, 'F%d' % r,
                  con_cita_literal(fila_canal['pregunta_al_asesor']),
                  wrap=True)
        ws['F%d' % r].font = Font(size=9)
        motor.val(ws, 'K%d' % r, CITA_644, wrap=True)
        ws['K%d' % r].font = Font(italic=True, size=9)
        ws.row_dimensions[r].height = 66
        for chn in re.findall(r'CHN-[0-9]+[a-z]*', fila_canal['fuente']):
            if D.nota_legal(chn):
                X.nota_celda(ws, 'B%d' % r, chn)
                break
    C.dv_rango(ws, v_usa, refs['Sí o No'], 'Marca Sí o No',
               'Elige «Sí» o «No» de la lista del pie de la hoja.')
    C.dv_rango(ws, v_saca, refs['Sí, No o No lo sé'],
               'Marca Sí, No o No lo sé',
               'Tres de los cinco canales vienen marcados «No lo sé» A '
               'PROPÓSITO: ninguna fuente resuelve si rompen la condición de '
               'la nota. Es lo que hay que preguntarle al asesor.')

    def can(fila, etiqueta, formula, fmt=None, nota_txt=None, bold=True):
        motor.val(ws, 'B%d' % fila, etiqueta, bold=bold, wrap=True)
        motor.f(ws, 'C%d' % fila, formula, fmt=fmt, bold=bold)
        if nota_txt:
            C.nota(ws, 'K%d' % fila, nota_txt)

    can(K_CAN_USO, 'Canales por los que vas a vender',
        ie('COUNTIF(C%d:C%d,"%s")' % (K_CAN_INI, K_CAN_FIN, SI)), C.FMT_ENT,
        'De los cinco del plan financiero. El mostrador no se discute; el resto '
        'sí.')
    can(K_CAN_FUERA, 'De ellos, los que SÍ te sacan de la nota',
        '=SUMPRODUCT(--($C${a}:$C${b}="{s}"),--($D${a}:$D${b}="{s}"))'
        .format(a=K_CAN_INI, b=K_CAN_FIN, s=SI), C.FMT_ENT,
        'En cuanto uno de éstos esté en «Sí», deja de valerte la nota del '
        '644.5 tal cual: el alta que cubre los cinco canales es la industrial '
        '421.1, y ésa te saca del amparo de la Ley 12/2012.')
    can(K_CAN_NOSE, 'Canales sin resolver (pendientes del asesor)',
        '=SUMPRODUCT(--($C${a}:$C${b}="{s}"),--($D${a}:$D${b}="{n}"))'
        .format(a=K_CAN_INI, b=K_CAN_FIN, s=SI, n=NOSE), C.FMT_ENT,
        'No es un hueco del producto: es que ninguna fuente lo resuelve. La '
        'columna F trae la pregunta ya redactada para que la copies y la '
        'envíes.')
    can(K_CAN_VER, 'VEREDICTO DE LOS CANALES',
        ie('IF(C{n}>0,"Llévale a tu asesor fiscal la pregunta de la columna F '
           'de los canales sin resolver: la respuesta puede cambiarte el alta",'
           'IF(C{f}>0,"Tienes canales que se salen de la nota del 644.5: '
           'confirma con tu asesor qué alta te toca","Todos tus canales caben '
           'en la nota del 644.5: fabricas y vendes en las propias '
           'dependencias"))'.format(n=K_CAN_NOSE, f=K_CAN_FUERA)))
    ws.merge_cells('C%d:J%d' % (K_CAN_VER, K_CAN_VER))
    ws['C%d' % K_CAN_VER].alignment = Alignment(vertical='top', wrap_text=True)
    ws.row_dimensions[K_CAN_VER].height = 36
    C.destacado(ws, 'C%d' % K_CAN_VER)
    X.nota_celda(ws, 'C%d' % K_CAN_VER, 'CHN-94')
    motor.val(ws, 'B%d' % K_CAN_PREG, 'Lo que NO hace esta hoja', bold=True)
    motor.val(ws, 'C%d' % K_CAN_PREG,
              'No te da un epígrafe de IAE por canal, y no es un olvido: '
              'ninguna fuente lo da. Lo verificado es que una cuota faculta '
              'EXCLUSIVAMENTE para su actividad (Regla 4.ª.1), que la venta '
              'online al consumidor SIGUE SIENDO comercio al por menor porque '
              'se define por el destino y comprende el realizado sin '
              'establecimiento (Regla 4.ª.2.D), y que el epígrafe industrial '
              'faculta para vender al por mayor y al por menor (Regla '
              '4.ª.2.A). Lo que no está verificado es si la condición de la '
              'nota sobre la FABRICACIÓN se rompe al comercializar fuera de '
              'tus dependencias.', wrap=True)
    ws.merge_cells('C%d:K%d' % (K_CAN_PREG, K_CAN_PREG))
    ws['C%d' % K_CAN_PREG].font = Font(italic=True, size=9)
    ws.row_dimensions[K_CAN_PREG].height = 62
    X.nota_celda(ws, 'C%d' % K_CAN_PREG, 'CHN-95')
    motor.semaforo_isnumber(ws, 'C%d' % K_CAN_NOSE, '$C$%d' % K_CAN_NOSE,
                            '>', '0', bg=motor.CF_AMBAR_BG,
                            fg=motor.CF_AMBAR_FG)
    motor.semaforo_isnumber(ws, 'C%d' % K_CAN_FUERA, '$C$%d' % K_CAN_FUERA,
                            '>', '0', bg=motor.CF_AMBAR_BG,
                            fg=motor.CF_AMBAR_FG)

    C.parrafo(ws, K_NOTA,
              'Los plazos en días son ORIENTATIVOS y casi todos dependen de un '
              'tercero: el ayuntamiento, la comunidad de propietarios, el '
              'ingeniero, el instalador. El único que controlas del todo es el '
              'de pedir las cosas pronto.', 'A', 'K', alto=36)
    C.parrafo(ws, K_NOTA + 1,
              'PUEDES FABRICAR BOMBONES SIN DARTE DE ALTA COMO INDUSTRIA '
              'MIENTRAS LOS VENDAS EN TU PROPIA TIENDA. En el momento en que '
              'sirves a otros comercios, a empresas o envías fuera, esto '
              'cambia — y ésa es exactamente la tabla de canales de arriba. '
              'Está PROHIBIDO leer el 644.5 como «con esto puedo vender a '
              'hostelería, a empresas y por envío sin más».',
              'A', 'K', alto=44)
    C.parrafo(ws, K_NOTA + 2,
              'Y ojo con el alta censal: hoy se comunican DOS códigos, no uno. '
              'El CNAE-2025 (10.82 «Fabricación de cacao, chocolate y '
              'productos de confitería» y 47.24 «Comercio al por menor de pan, '
              'productos de panadería y confitería») y además el CNAE-2009 '
              'mientras no entre en vigor la tarifa de primas adaptada.',
              'A', 'K', alto=40)
    ws.freeze_panes = 'C%d' % (K_CAB + 1)
    C.pagina(ws, titulos='$%d:$%d' % (K_CAB, K_CAB),
             area='A1:K%d' % fila_listas)
    return ws


# ==========================================================================
# Hoja «Árbol de Registro Sanitario»
# ==========================================================================
A = {'sec_preg': 5, 'final': 6, 'b2b': 7, 'obrador': 8, 'sucursales': 9,
     'sec_ver': 11, 'regimen': 12, 'tramite': 13, 'habilita': 14,
     'plazo': 15, 'aviso_suc': 16,
     'sec_tabla': 18, 'cab': 19, 'caso1': 20, 'caso2': 21, 'caso3': 22,
     'nota': 24, 'listas': 27}

CASOS_REGISTRO = (
    ('Vendes sólo al consumidor final, en tu establecimiento y por tu web',
     'Comunicación o declaración responsable al registro de tu comunidad '
     'autónoma',
     'Estás EXCLUIDO del RGSEAA por norma. Tener obrador NO te saca del '
     'régimen minorista, y vender por internet tampoco: la venta a distancia '
     'ya está dentro de la definición de minorista.'),
    ('Suministras además a otros minoristas de DISTINTA titularidad, y cumples '
     'las tres condiciones del art. 3',
     'La misma comunicación autonómica, MÁS declaración responsable del art. '
     '3.5 y registro de destinatarios, cantidades y fechas',
     'Sigues fuera del RGSEAA, pero con papeles añadidos. La hoja «Suministro '
     'a Otros Minoristas» comprueba las tres condiciones una a una.'),
    ('Suministras a otros minoristas y NO cumples alguna de las tres',
     'Inscripción en el RGSEAA',
     'Basta con fallar una: las tres son acumulativas. La que más fácil se '
     'rompe es «restringido», y basta un cliente inscrito en el RGSEAA.'),
)


def hoja_arbol(wb):
    ws = wb.create_sheet(H_ARB)
    C.anchos(ws, {'A': 60, 'B': 30, 'C': 100})
    C.encabezar(ws, '¿Registro autonómico o RGSEAA?',
                'Cuatro preguntas y un veredicto. Es la hoja que corrige el '
                'error más caro del sector: hay consultoras cobrando por '
                'tramitar un registro estatal que a una chocolatería minorista '
                'no le hace falta.', col_fin='C')

    refs, fila_listas = C.bloque_listas(
        ws, A['listas'], [('Sí o No', list(SI_NO))], col='A')

    def sec(fila, texto):
        C.seccion(ws, 'A%d' % fila, texto)
        for letra in 'BC':
            motor.val(ws, letra + str(fila), '')
            ws[letra + str(fila)].fill = PatternFill('solid',
                                                     fgColor=C.CABECERA)

    def linea(fila, etiqueta, formula=None, fmt=None, nota_txt=None,
              verde=None, chn=None, bold=None):
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True, bold=bold)
        if verde is not None:
            X.entrada(ws, 'B%d' % fila, verde, fmt=fmt, etiqueta=etiqueta,
                      align='center')
        else:
            motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=bold)
        if chn:
            X.nota_celda(ws, 'B%d' % fila, chn)
        if nota_txt:
            C.nota(ws, 'C%d' % fila, nota_txt)
        return 'B%d' % fila

    sec(A['sec_preg'], 'LAS CUATRO PREGUNTAS')
    linea(A['final'], '¿Vendes al consumidor final en tu propio '
                      'establecimiento?', verde=SI, chn='CHN-39',
          nota_txt='Si la respuesta es sí, eres comercio al por menor y estás '
                   'EXCLUIDO del Registro General Sanitario de Empresas '
                   'Alimentarias y Alimentos.')
    linea(A['b2b'], '¿Suministras a otros establecimientos MINORISTAS de '
                    'distinta titularidad?', verde=NO, chn='CHN-41',
          nota_txt='Ésta es la pregunta que de verdad decide. Vender al '
                   'consumidor final, aunque sea por internet y a toda España, '
                   'NO es suministrar a otros minoristas.')
    linea(A['obrador'], '¿Tienes obrador propio?', verde=SI, chn='CHN-40b',
          nota_txt='Tener obrador NO te saca del régimen minorista. Es el mito '
                   'más caro del sector: fabricar para vender en tu propia '
                   'tienda sigue siendo comercio al por menor.')
    linea(A['sucursales'], '¿Vas a tener más de un establecimiento (obrador '
                           'central y tiendas)?', verde=NO, chn='CHN-42',
          nota_txt='Un obrador central que abastece a tus propias sucursales '
                   'no es «suministro a otros minoristas»: la titularidad es la '
                   'misma. Pero cada establecimiento tiene su propia '
                   'comunicación.')
    C.dv_rango(ws, ['B%d' % A['final'], 'B%d' % A['b2b'],
                    'B%d' % A['obrador'], 'B%d' % A['sucursales']],
               refs['Sí o No'], 'Marca Sí o No',
               'Elige «Sí» o «No» de la lista del pie de la hoja.')

    sec(A['sec_ver'], 'EL VEREDICTO')
    linea(A['regimen'], 'Tu régimen sanitario',
          ie('IF(B{f}="{no}","Revísalo: si no vendes al consumidor final, esto '
             'no es una chocolatería minorista",IF(B{b}="{si}","Minorista con '
             'suministro a otros minoristas: resuelve el art. 3","Comercio al '
             'por menor: EXCLUIDO del RGSEAA"))'
             .format(f=A['final'], b=A['b2b'], si=SI, no=NO)), bold=True,
          chn='CHN-39')
    linea(A['tramite'], 'El trámite que te toca',
          ie('IF(B{b}="{si}","La comunicación autonómica MÁS la declaración '
             'responsable del art. 3.5 y el registro de destinatarios",'
             '"Comunicación o declaración responsable al registro de tu '
             'comunidad autónoma")'.format(b=A['b2b'], si=SI)), bold=True,
          chn='CHN-43')
    linea(A['habilita'], '¿Ese trámite te habilita para abrir?',
          ie('IF(B{r}="","","NO. La comunicación autonómica no habilita: ni '
             'tienes que esperar respuesta, ni te protege si el resto no está '
             'en regla")'.format(r=A['regimen'])), bold=True, chn='CHN-39')
    linea(A['plazo'], 'Cuándo se presenta',
          ie('IF(B{r}="","","Antes de empezar la actividad. En una comunidad '
             'se presenta simultáneamente al inicio y no habilita; en otra es '
             'condición única y suficiente para iniciar, y lleva tasa: '
             'compruébalo en la tuya")'.format(r=A['regimen'])), chn='CHN-43')
    linea(A['aviso_suc'], 'Si tienes varios establecimientos',
          ie('IF(B{s}="{no}","Un solo establecimiento: una sola '
             'comunicación","Cada establecimiento lleva su propia '
             'comunicación, aunque la titularidad sea la misma")'
             .format(s=A['sucursales'], no=NO)), chn='CHN-42')
    for f in (A['regimen'], A['tramite'], A['habilita'], A['plazo'],
              A['aviso_suc']):
        ws['B%d' % f].alignment = Alignment(vertical='top', wrap_text=True)
        ws.row_dimensions[f].height = 46
    C.destacado(ws, 'B%d' % A['regimen'])

    sec(A['sec_tabla'], 'LOS TRES CASOS, PARA QUE VEAS DÓNDE CAES')
    C.cabecera(ws, A['cab'], [('A', 'Tu situación'), ('B', 'Lo que te toca'),
                              ('C', 'Por qué')], altura=26)
    for i, (situacion, toca, porque) in enumerate(CASOS_REGISTRO):
        r = A['caso1'] + i
        motor.val(ws, 'A%d' % r, situacion, wrap=True)
        motor.val(ws, 'B%d' % r, toca, wrap=True)
        motor.val(ws, 'C%d' % r, porque, wrap=True)
        ws.row_dimensions[r].height = 56

    C.parrafo(ws, A['nota'],
              'HAY CONSULTORAS COBRANDO POR TRAMITAR UN REGISTRO QUE NO HACE '
              'FALTA, y hay quien retrasa una apertura semanas esperando una '
              'inscripción que nadie le ha pedido. Si vendes al consumidor '
              'final desde tu propio establecimiento, tu sitio es el registro '
              'de tu comunidad autónoma, no el estatal. Está PROHIBIDO '
              'escribir «necesitas el RGSEAA para abrir».', 'A', 'C', alto=56)
    C.parrafo(ws, A['nota'] + 1,
              'La clave y las actividades del RGSEAA existen y están '
              'verificadas, pero sólo entran en juego cuando SÍ te toca '
              'inscribirte: cuando suministras a otros minoristas y fallas '
              'alguna de las tres condiciones del art. 3.', 'A', 'C', alto=40)
    ws.freeze_panes = 'A4'
    C.pagina(ws, apaisado=False, area='A1:C%d' % fila_listas)
    return ws


# ==========================================================================
# Hoja «Suministro a Otros Minoristas» (D34)
# ==========================================================================
DESTINATARIOS = [
    ('Cafetería El Mirador', 18.0, 0.05, 2.0, NO),
    ('Hotel Plaza Mayor (A&B)', 22.0, 0.06, 4.0, NO),
    ('Tienda gourmet La Despensa', 9.0, 0.03, 12.0, NOSE),
    ('(libre)', 0.0, 0.0, 0.0, NO),
    ('(libre)', 0.0, 0.0, 0.0, NO),
    ('(libre)', 0.0, 0.0, 0.0, NO),
]

U = {'sec_puerta': 5, 'puerta': 6, 'aviso_puerta': 7,
     'sec_dest': 9, 'cab': 10, 'ini': 11, 'fin': 16, 'tot': 17,
     'sec_marg': 19, 'umbral_a': 20, 'tu_pct': 21, 'via_a': 22,
     'umbral_b': 23, 'total_kg': 24, 'via_b': 25, 'marginal': 26,
     'sec_loc': 28, 'misma_zona': 29, 'radio': 30, 'max_km': 31,
     'otra_ccaa': 32, 'localizado': 33,
     'sec_res': 35, 'inscritos': 36, 'restringido': 37,
     'sec_ver': 39, 'cumplidas': 40, 'veredicto': 41, 'ademas': 42,
     'nota': 44, 'listas': 48}


def hoja_suministro(wb):
    ws = wb.create_sheet(H_SUM)
    C.anchos(ws, {'A': 58, 'B': 20, 'C': 20, 'D': 14, 'E': 20, 'F': 96})
    C.encabezar(ws, 'Suministro a otros minoristas: el árbol del art. 3',
                'Primero la puerta de entrada: esto SÓLO te aplica si '
                'suministras a establecimientos minoristas de DISTINTA '
                'titularidad. Si entras, las tres condiciones son '
                'ACUMULATIVAS, y dentro de «marginal» hay dos vías '
                'ALTERNATIVAS.', col_fin='F')

    refs, fila_listas = C.bloque_listas(
        ws, U['listas'], [('Sí o No', list(SI_NO)),
                          ('Sí, No o No lo sé', list(SI_NO_NOSE))], col='A')

    def sec(fila, texto):
        C.seccion(ws, 'A%d' % fila, texto)
        for letra in 'BCDEF':
            motor.val(ws, letra + str(fila), '')
            ws[letra + str(fila)].fill = PatternFill('solid',
                                                     fgColor=C.CABECERA)

    def linea(fila, etiqueta, formula=None, fmt=None, nota_txt=None,
              verde=None, chn=None, bold=None):
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True, bold=bold)
        if verde is not None:
            X.entrada(ws, 'B%d' % fila, verde, fmt=fmt, etiqueta=etiqueta,
                      align='center')
        else:
            motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=bold)
        if chn:
            X.nota_celda(ws, 'B%d' % fila, chn)
        if nota_txt:
            C.nota(ws, 'F%d' % fila, nota_txt)
        return 'B%d' % fila

    # B2 (refutación 2026-09-12): el valor de partida NO se teclea a mano —se
    # deriva del propio juego de datos («La Almendra» SÍ tiene un minorista
    # de distinta titularidad, `Tienda gourmet La Despensa», que además está
    # tres filas más abajo en la tabla de destinatarios de esta misma
    # hoja—, para que la puerta de entrada y la tabla no puedan volver a
    # contradecirse.
    _HAY_MINORISTA_B2B = any(
        c[1] == 'Minorista de distinta titularidad' for c in D.CLIENTES_B2B)
    sec(U['sec_puerta'], 'PUERTA DE ENTRADA: ¿TE APLICA SIQUIERA?')
    linea(U['puerta'],
          '¿Suministras bombones de producción propia a establecimientos '
          'MINORISTAS de distinta titularidad?',
          verde=(SI if _HAY_MINORISTA_B2B else NO), chn='CHN-41',
          nota_txt='Si la respuesta es «No», el art. 3 no te aplica y puedes '
                   'saltarte el resto de la hoja. Vender al consumidor final, '
                   'aunque sea por internet y a toda España, NO es suministrar '
                   'a otros minoristas.')
    C.dv_rango(ws, ['B%d' % U['puerta']], refs['Sí o No'], 'Marca Sí o No',
               'Elige «Sí» o «No» de la lista del pie.')
    motor.val(ws, 'A%d' % U['aviso_puerta'], 'Lectura de la puerta de entrada')
    motor.f(ws, 'B%d' % U['aviso_puerta'],
            ie('IF(B{0}="{1}","El art. 3 NO te aplica: nada de lo de abajo te '
               'obliga","Te aplica: sigue con las tres condiciones")'
               .format(U['puerta'], NO)))
    ws.merge_cells('B%d:E%d' % (U['aviso_puerta'], U['aviso_puerta']))

    sec(U['sec_dest'], 'TUS DESTINATARIOS')
    C.cabecera(ws, U['cab'],
               [('A', 'Destinatario'),
                ('B', 'Kilos a la semana que le sirves'),
                ('C', '% de tu volumen anual'), ('D', 'Kilómetros'),
                ('E', '¿Inscrito en el RGSEAA?'), ('F', 'Notas')], altura=32)
    v_rgseaa = []
    for i, (nombre, kg, pct, km, inscrito) in enumerate(DESTINATARIOS):
        fila = U['ini'] + i
        X.entrada(ws, 'A%d' % fila, nombre,
                  etiqueta='Destinatario %d' % (i + 1))
        X.entrada(ws, 'B%d' % fila, kg, fmt=C.FMT_DEC1,
                  etiqueta='Kilos a la semana del destinatario %d' % (i + 1))
        X.entrada(ws, 'C%d' % fila, pct, fmt='0.00%',
                  etiqueta='Porcentaje anual del destinatario %d' % (i + 1))
        X.entrada(ws, 'D%d' % fila, km, fmt=C.FMT_DEC1,
                  etiqueta='Kilómetros al destinatario %d' % (i + 1))
        X.entrada(ws, 'E%d' % fila, inscrito,
                  etiqueta='RGSEAA del destinatario %d' % (i + 1),
                  align='center')
        v_rgseaa.append('E%d' % fila)
    C.dv_rango(ws, v_rgseaa, refs['Sí, No o No lo sé'],
               'Marca Sí, No o No lo sé',
               'Elige una de las tres opciones de la lista del pie.')
    motor.val(ws, 'A%d' % U['tot'], 'TOTAL', bold=True)
    motor.f(ws, 'B%d' % U['tot'],
            ie('SUM(B%d:B%d)' % (U['ini'], U['fin'])), fmt=C.FMT_DEC1,
            bold=True)
    motor.f(ws, 'C%d' % U['tot'],
            ie('SUM(C%d:C%d)' % (U['ini'], U['fin'])), fmt='0.00%', bold=True)
    motor.f(ws, 'D%d' % U['tot'],
            ie('MAX(D%d:D%d)' % (U['ini'], U['fin'])), fmt=C.FMT_DEC1,
            bold=True)
    motor.f(ws, 'E%d' % U['tot'],
            ie('COUNTIF(E%d:E%d,"%s")' % (U['ini'], U['fin'], SI)),
            fmt=C.FMT_ENT, bold=True)
    X.total_fila(ws, U['tot'], 'ABCDEF')
    C.nota(ws, 'F%d' % U['tot'],
           'Los kilos y el porcentaje se suman; los kilómetros se toman al '
           'MÁXIMO (el destinatario más lejano es el que decide) y en la última '
           'columna se cuentan los que están inscritos en el RGSEAA.')

    sec(U['sec_marg'], 'CONDICIÓN 1 ' + chr(183) + ' MARGINAL (dos vías '
                       'ALTERNATIVAS: basta con cumplir una)')
    linea(U['umbral_a'], 'Vía a) ' + chr(183) + ' Umbral del volumen anual (%)',
          verde=0.25, fmt=C.FMT_PCT, chn='CHN-41',
          nota_txt='El suministro a otros minoristas no puede pasar del 25'
                   + N + '% de tu volumen anual de alimentos comercializados.')
    linea(U['tu_pct'], 'Tu porcentaje a otros minoristas',
          ie('C%d' % U['tot']), '0.00%')
    linea(U['via_a'], '¿Cumples la vía a)?',
          ie('IF(B{0}<=B{1},"{2}","{3}")'
             .format(U['tu_pct'], U['umbral_a'], SI, NO)), bold=True)
    linea(U['umbral_b'],
          'Vía b) ' + chr(183) + ' Máximo a la semana a otros minoristas (kg)',
          verde=500, fmt=C.FMT_ENT, chn='CHN-41',
          nota_txt='Es el máximo del suministro A OTROS MINORISTAS. El art. 3 '
                   'habla del suministro a establecimientos minoristas de '
                   'distinta titularidad: está PROHIBIDO leer estos 500'
                   + N + 'kg como si incluyeran lo que despachas en tu propio '
                   'mostrador, porque eso describe una trampa que no existe.')
    linea(U['total_kg'], 'Lo que sirves a otros minoristas a la semana (kg)',
          ie('B%d' % U['tot']), C.FMT_DEC1)
    linea(U['via_b'], '¿Cumples la vía b)?',
          ie('IF(B{0}<=B{1},"{2}","{3}")'
             .format(U['total_kg'], U['umbral_b'], SI, NO)), bold=True)
    linea(U['marginal'], '¿ES MARGINAL?',
          ie('IF(OR(B{0}="{2}",B{1}="{2}"),"{2}","{3}")'
             .format(U['via_a'], U['via_b'], SI, NO)), bold=True,
          nota_txt='Basta con cumplir UNA de las dos vías: son alternativas, '
                   'no acumulativas. Un obrador que sirve 600' + N + 'kg a la '
                   'semana a otros minoristas sigue siendo marginal si eso no '
                   'llega al 25' + N + '% de su volumen anual.')
    motor.regla_expresion(ws, 'B%d:B%d' % (U['marginal'], U['marginal']),
                          '=$B$%d="%s"' % (U['marginal'], NO))

    sec(U['sec_loc'], 'CONDICIÓN 2 ' + chr(183) + ' LOCALIZADO')
    linea(U['misma_zona'],
          '¿Todos tus destinatarios están en tu unidad sanitaria local, zona de '
          'salud o territorio equivalente, o en una zona limítrofe?', verde=SI,
          chn='CHN-41',
          nota_txt='El texto no habla de kilómetros dentro de la misma '
                   'comunidad: habla de unidad sanitaria local, zona de salud o '
                   'territorio equivalente. Los kilómetros aparecen sólo para '
                   'el comercio ENTRE comunidades autónomas.')
    linea(U['radio'],
          'Radio máximo entre establecimientos de comunidades DISTINTAS (km)',
          verde=50, fmt=C.FMT_ENT, chn='CHN-41',
          nota_txt='Y sólo si los registros sanitarios autonómicos de origen y '
                   'destino son públicos y accesibles de forma efectiva.')
    linea(U['max_km'], 'Distancia al destinatario más lejano (km)',
          ie('D%d' % U['tot']), C.FMT_DEC1)
    linea(U['otra_ccaa'],
          '¿Alguno de tus destinatarios está en otra comunidad autónoma?',
          verde=NO)
    linea(U['localizado'], '¿ES LOCALIZADO?',
          ie('IF(AND(B{0}="{4}",OR(B{1}="{5}",B{2}<=B{3})),"{4}","{5}")'
             .format(U['misma_zona'], U['otra_ccaa'], U['max_km'], U['radio'],
                     SI, NO)), bold=True)
    motor.regla_expresion(ws, 'B%d:B%d' % (U['localizado'], U['localizado']),
                          '=$B$%d="%s"' % (U['localizado'], NO))
    C.dv_rango(ws, ['B%d' % U['misma_zona'], 'B%d' % U['otra_ccaa']],
               refs['Sí o No'], 'Marca Sí o No',
               'Elige «Sí» o «No» de la lista del pie.')

    sec(U['sec_res'], 'CONDICIÓN 3 ' + chr(183) + ' RESTRINGIDO')
    linea(U['inscritos'], 'Destinatarios inscritos en el RGSEAA',
          ie('E%d' % U['tot']), C.FMT_ENT, chn='CHN-41',
          nota_txt='Una actividad es restringida cuando NO se suministran '
                   'productos a establecimientos inscritos en el RGSEAA. Es el '
                   'requisito que más fácil se rompe: basta UN cliente '
                   'inscrito. Si tienes alguno en «No lo sé», pregúntaselo: la '
                   'hoja lo cuenta como no inscrito y puede estar '
                   'tranquilizándote de más.')
    linea(U['restringido'], '¿ES RESTRINGIDO?',
          ie('IF(B%d=0,"%s","%s")' % (U['inscritos'], SI, NO)), bold=True)
    motor.regla_expresion(ws, 'B%d:B%d' % (U['restringido'], U['restringido']),
                          '=$B$%d="%s"' % (U['restringido'], NO))

    sec(U['sec_ver'], 'EL VEREDICTO')
    linea(U['cumplidas'], 'Condiciones cumplidas (de tres)',
          ie('COUNTIF(B{0}:B{0},"{3}")+COUNTIF(B{1}:B{1},"{3}")'
             '+COUNTIF(B{2}:B{2},"{3}")'
             .format(U['marginal'], U['localizado'], U['restringido'], SI)),
          C.FMT_ENT, bold=True)
    linea(U['veredicto'], 'VEREDICTO',
          ie('IF(B{0}="{n}","El art. 3 no te aplica: no suministras a otros '
             'minoristas de distinta titularidad",IF(B{1}=3,"Cumples las tres: '
             'sigues FUERA del RGSEAA, con la declaración responsable y el '
             'registro del art. 3.5","Te toca inscribirte en el RGSEAA: falla '
             'al menos una de las tres condiciones"))'
             .format(U['puerta'], U['cumplidas'], n=NO)), bold=True,
          chn='CHN-41')
    ws.merge_cells('B%d:E%d' % (U['veredicto'], U['veredicto']))
    ws['B%d' % U['veredicto']].alignment = Alignment(vertical='top',
                                                     wrap_text=True)
    ws.row_dimensions[U['veredicto']].height = 40
    C.destacado(ws, 'B%d' % U['veredicto'])
    linea(U['ademas'], 'Lo que además tienes que hacer si haces B2B',
          ie('IF(B{0}="{1}","Nada de esto te aplica","Presentar declaración '
             'responsable de que cumples el art. 3 y llevar registro de '
             'destinatarios, cantidades y fechas")'
             .format(U['puerta'], NO)))
    ws.merge_cells('B%d:E%d' % (U['ademas'], U['ademas']))
    ws['B%d' % U['ademas']].alignment = Alignment(vertical='top',
                                                  wrap_text=True)
    ws.row_dimensions[U['ademas']].height = 34

    C.parrafo(ws, U['nota'],
              'LAS TRES CONDICIONES SON ACUMULATIVAS: hay que cumplir marginal '
              'Y localizado Y restringido. Lo que es alternativo son las dos '
              'vías DENTRO de «marginal». Fallar una sola te manda al RGSEAA.',
              'A', 'F', alto=40)
    C.parrafo(ws, U['nota'] + 1,
              'LOS 500 KILOS NO INCLUYEN TU MOSTRADOR. El art. 3 regula el '
              'suministro a otros establecimientos minoristas de distinta '
              'titularidad, y es ahí donde se miden. Leerlo como «puedo servir '
              'a quien quiera mientras entre todo no pase de 500» es inventarse '
              'una trampa que la norma no pone — y confundirse en el otro '
              'sentido, creyendo que el mostrador te consume el cupo, te hace '
              'renunciar a un canal que sí podías tener.', 'A', 'F', alto=56)
    C.parrafo(ws, U['nota'] + 2,
              'Y la tabla de clientes que esto te obliga a llevar es la misma '
              'que te pide el reglamento de deforestación por otra vía: está '
              'construida en la hoja «Clientes a los que Suministras» del libro '
              '«checklist-equipamiento-y-proveedores-cacao.xlsx».',
              'A', 'F', alto=36)
    ws.freeze_panes = 'A4'
    C.pagina(ws, area='A1:F%d' % fila_listas)
    return ws


# ==========================================================================
# Hoja «Ruta Doméstica» (D21)
# ==========================================================================
LISTA_BLANCA = (
    ('a)', 'Comidas preparadas con tratamiento térmico suficiente',
     'El bombón no es una comida preparada.'),
    ('b)', 'Productos de panadería y repostería ESTABLES A TEMPERATURA '
           'AMBIENTE',
     'Por defecto el chocolate NO encaja aquí, y eso es una INTERPRETACIÓN '
     'declarada, no nivel A: compruébalo en tu comunidad. Una comunidad añade '
     '«confitería» a esta letra, pero NO «chocolate».'),
    ('c)', 'Mermeladas, confituras y jaleas con tratamiento térmico después '
           'del envasado',
     'Las que se envasan en frío quedan fuera.'),
    ('d)', 'Conservas vegetales con pH inferior a 4,5',
     'Ahí el riesgo cambia de categoría.'),
    ('e)', 'Otros alimentos que las autoridades competentes de las comunidades '
           'autónomas permitan en sus territorios',
     'LA LETRA ABIERTA. Nada por defecto: está vacía hasta que TU comunidad la '
     'rellene. Es la única puerta por la que el bombón podría entrar, y por eso '
     'la pregunta de arriba manda sobre todo lo demás.'),
)

M = {'sec_datos': 5, 'ccaa': 6, 'amplia': 7, 'enlace': 8, 'aviso': 9,
     'sec_blanca': 11, 'cab_blanca': 12, 'blanca_ini': 13, 'blanca_fin': 17,
     'sec_lim': 19, 'cita': 20, 'm2': 21, 'kg': 22, 'tope': 23, 'sem_tope': 24,
     'prop': 25, 'sem_prop': 26, 'demostrable': 27, 'sem_dem': 28,
     'sec_ver': 30, 'cumplidos': 31, 'veredicto': 32,
     'nota': 34, 'listas': 38}


def hoja_domestica(wb):
    ws = wb.create_sheet(H_DOM)
    C.anchos(ws, {'A': 60, 'B': 24, 'C': 100})
    C.encabezar(ws, 'Ruta doméstica: elaborar en vivienda particular',
                'Para el bombón esta ruta NO está abierta por defecto. La '
                'lista estatal tiene CINCO letras y la quinta la rellena cada '
                'comunidad: por eso lo primero que pregunta la hoja es si la '
                'tuya lo ha hecho. Los tres requisitos del art. 13.9 sólo se '
                'activan a partir de ahí.', col_fin='C')

    refs, fila_listas = C.bloque_listas(
        ws, M['listas'], [('Sí, No o No lo sé', list(SI_NO_NOSE)),
                          ('Comunidad autónoma', CCAA_LISTA)], col='A')

    def sec(fila, texto):
        C.seccion(ws, 'A%d' % fila, texto)
        for letra in 'BC':
            motor.val(ws, letra + str(fila), '')
            ws[letra + str(fila)].fill = PatternFill('solid',
                                                     fgColor=C.CABECERA)

    def linea(fila, etiqueta, formula=None, fmt=None, nota_txt=None,
              verde=None, chn=None, bold=None):
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True, bold=bold)
        if verde is not None:
            X.entrada(ws, 'B%d' % fila, verde, fmt=fmt, etiqueta=etiqueta,
                      align='center')
        else:
            motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=bold)
        if chn:
            X.nota_celda(ws, 'B%d' % fila, chn)
        if nota_txt:
            C.nota(ws, 'C%d' % fila, nota_txt)
        return 'B%d' % fila

    sec(M['sec_datos'], 'LA PREGUNTA QUE MANDA SOBRE TODO LO DEMÁS')
    linea(M['ccaa'], '¿En qué comunidad autónoma estarías?',
          verde=CCAA_LISTA[0], chn='CHN-43')
    C.dv_rango(ws, ['B%d' % M['ccaa']], refs['Comunidad autónoma'],
               'Elige tu comunidad', 'Cuatro de EJEMPLO más «Otra».')
    linea(M['amplia'],
          '¿Tu comunidad ha ampliado la lista del art. 13.8 por la letra e) '
          'para incluir el chocolate?', verde=NO, chn='CHN-44',
          nota_txt='La lista estatal tiene CINCO letras y la quinta es ABIERTA: '
                   '«otros alimentos que las autoridades competentes de las '
                   'comunidades autónomas permitan en sus territorios». Por '
                   'defecto el chocolate no encaja en la letra b), pero eso es '
                   'INTERPRETACIÓN DECLARADA, no nivel A. Está PROHIBIDO '
                   'escribir «hacer bombones en casa para vender es ilegal en '
                   'España».')
    C.dv_rango(ws, ['B%d' % M['amplia']], refs['Sí, No o No lo sé'],
               'Marca Sí, No o No lo sé',
               'Si no lo sabes, búscalo en el registro de tu comunidad antes '
               'de descartar la ruta o de darla por buena.')
    motor.val(ws, 'A%d' % M['enlace'], 'Dónde se comprueba', bold=True)
    motor.val(ws, 'B%d' % M['enlace'], 'Registro autonómico', wrap=True)
    C.nota(ws, 'C%d' % M['enlace'],
           'Busca «registro sanitario establecimientos alimentarios menores» '
           'más el nombre de tu comunidad: el decreto que salga es el tuyo, y '
           'es donde consta si ha usado la letra e). Y ojo con una confusión '
           'frecuente: el repertorio de ARTESANÍA ALIMENTARIA de una comunidad '
           '-que sí incluye los chocolates- es otro registro, otra competencia '
           'y otro fin; no sirve como prueba de qué es «repostería» para el RD '
           '1021/2022.')
    X.nota_celda(ws, 'B%d' % M['enlace'], 'CHN-52')
    linea(M['aviso'], 'Lectura de esa respuesta',
          ie('IF(B{0}="{s}","Tu comunidad ha abierto la puerta: sigue con los '
             'TRES requisitos del art. 13.9",IF(B{0}="{n}","Con la lista '
             'estatal en la mano, el bombón no entra: la ruta doméstica NO '
             'está abierta para ti","Compruébalo antes de decidir nada: ni la '
             'ruta está abierta ni está cerrada mientras no lo mires"))'
             .format(M['amplia'], s=SI, n=NO)), bold=True)
    ws.merge_cells('B%d:C%d' % (M['aviso'], M['aviso']))
    ws['B%d' % M['aviso']].alignment = Alignment(vertical='top',
                                                 wrap_text=True)
    ws.row_dimensions[M['aviso']].height = 40
    C.destacado(ws, 'B%d' % M['aviso'])

    sec(M['sec_blanca'], 'LA LISTA BLANCA DEL ART. 13.8, CON SUS CINCO LETRAS')
    C.cabecera(ws, M['cab_blanca'],
               [('A', 'Letra'), ('B', 'Qué permite'),
                ('C', 'Qué NO cubre, y por qué importa aquí')], altura=26)
    for i, (letra, permite, ojo) in enumerate(LISTA_BLANCA):
        r = M['blanca_ini'] + i
        motor.val(ws, 'A%d' % r, letra, align='center')
        motor.val(ws, 'B%d' % r, permite, wrap=True)
        motor.val(ws, 'C%d' % r, ojo, wrap=True)
        ws.row_dimensions[r].height = 52
    X.nota_celda(ws, 'B%d' % (M['blanca_ini'] + 1), 'CHN-44b')
    X.nota_celda(ws, 'B%d' % (M['blanca_ini'] + 4), 'CHN-44')

    sec(M['sec_lim'], 'LOS TRES REQUISITOS DEL ART. 13.9 (sólo si la letra e) '
                      'te ha abierto la puerta)')
    motor.val(ws, 'A%d' % M['cita'], 'La cita, literal', bold=True)
    motor.val(ws, 'B%d' % M['cita'], D.ficha('PA-29c')['cita_literal'],
              wrap=True)
    ws.merge_cells('B%d:C%d' % (M['cita'], M['cita']))
    ws['B%d' % M['cita']].font = Font(italic=True, size=9)
    ws.row_dimensions[M['cita']].height = 46
    nota_reutilizada(ws, 'B%d' % M['cita'], 'PA-29c')
    linea(M['m2'], 'Metros cuadrados útiles de la zona de elaboración',
          verde=12.0, fmt=C.FMT_DEC1,
          nota_txt='SUPUESTO sembrado. La norma no da un número de kilos por '
                   'metro cuadrado: da un criterio, la proporcionalidad. Ponlo '
                   'tú y defiéndelo.')
    linea(M['kg'], 'Kilos de producto que prevés elaborar a la semana',
          verde=35.0, fmt=C.FMT_DEC1)
    linea(M['tope'], 'Tope absoluto del art. 13.9 (kg a la semana)', verde=100,
          fmt=C.FMT_ENT)
    linea(M['sem_tope'], 'Requisito 1 ' + chr(183) + ' ¿estás por debajo del '
                         'tope de kilos?',
          ie('IF(B{a}<>"{s}","No procede: la ruta no está abierta",'
             'IF(B{k}<=B{t},"{si}","{no}"))'
             .format(a=M['amplia'], k=M['kg'], t=M['tope'], s=SI, si=SI,
                     no=NO)), bold=True,
          nota_txt='El tope de 100' + N + 'kg casi nunca se alcanza en una '
                   'cocina doméstica: no es el que de verdad limita.')
    linea(M['prop'], 'Kilos por metro cuadrado que te salen',
          ie('IF(B{m}=0,"",B{k}/B{m})'.format(m=M['m2'], k=M['kg'])),
          C.FMT_DEC1)
    linea(M['sem_prop'], 'Requisito 2 ' + chr(183) + ' ¿es proporcional al '
                         'tamaño de las instalaciones?',
          ie('IF(B{a}<>"{s}","No procede: la ruta no está abierta",'
             '"Lo decide la autoridad, no una fórmula: la norma da un CRITERIO, '
             'no un número. Éste es el requisito que de verdad limita")'
             .format(a=M['amplia'], s=SI)), bold=True,
          nota_txt='Aquí no hay semáforo de sí o no A PROPÓSITO: inventarse un '
                   'umbral de kilos por metro cuadrado sería publicar como '
                   'norma un número que la norma no da.')
    linea(M['demostrable'], '¿Puedes demostrarlo documentalmente?', verde=NO,
          nota_txt='Registro de producción, albaranes, plan de limpieza. «Lo '
                   'cual se demostrará documentalmente» está en la propia '
                   'cita: no es un añadido de este producto.')
    linea(M['sem_dem'], 'Requisito 3 ' + chr(183) + ' ¿está demostrado?',
          ie('IF(B{a}<>"{s}","No procede: la ruta no está abierta",B{d})'
             .format(a=M['amplia'], d=M['demostrable'], s=SI)), bold=True)
    C.dv_rango(ws, ['B%d' % M['demostrable']], refs['Sí, No o No lo sé'],
               'Marca Sí, No o No lo sé',
               'Elige una de las tres opciones de la lista del pie.')

    sec(M['sec_ver'], 'EL VEREDICTO')
    linea(M['cumplidos'], 'Requisitos resueltos en verde (de los dos que se '
                          'pueden medir)',
          ie('COUNTIF(B{0}:B{0},"{s}")+COUNTIF(B{1}:B{1},"{s}")'
             .format(M['sem_tope'], M['sem_dem'], s=SI)), C.FMT_ENT,
          bold=True)
    linea(M['veredicto'], 'VEREDICTO',
          ie('IF(B{a}="{n}","Con la lista estatal en la mano, la ruta '
             'doméstica no está abierta para el bombón en tu comunidad",'
             'IF(B{a}="{ns}","Sin resolver: comprueba en tu comunidad si ha '
             'usado la letra e) antes de dar por buena o por mala esta ruta",'
             'IF(B{c}=2,"Tu comunidad la ha abierto y cumples los dos '
             'requisitos medibles: queda el de proporcionalidad, que lo valora '
             'la autoridad","Tu comunidad la ha abierto pero te falta algún '
             'requisito del art. 13.9")))'
             .format(a=M['amplia'], c=M['cumplidos'], n=NO, ns=NOSE)),
          bold=True)
    ws.merge_cells('B%d:C%d' % (M['veredicto'], M['veredicto']))
    ws['B%d' % M['veredicto']].alignment = Alignment(vertical='top',
                                                     wrap_text=True)
    ws.row_dimensions[M['veredicto']].height = 46
    C.destacado(ws, 'B%d' % M['veredicto'])

    C.parrafo(ws, M['nota'],
              'POR QUÉ ESTA HOJA EMPIEZA POR LA LETRA e) Y NO POR LOS KILOS: '
              'porque para el bombón la ruta doméstica no está abierta por '
              'defecto. Un semáforo de «100 kilos a la semana» puesto delante '
              'sugiere que la ruta existe y que sólo hay que no pasarse, y eso '
              'es lo contrario de lo que dice la norma estatal.',
              'A', 'C', alto=48)
    C.parrafo(ws, M['nota'] + 1,
              'Y el argumento que circula por ahí, el de que un decreto '
              'autonómico de ARTESANÍA ALIMENTARIA incluye los chocolates y por '
              'tanto son «repostería», no vale: es otro registro, otra '
              'competencia y otro fin. Lo que sí es un dato duro es que '
              '«chocolate», «cacao», «bombón» y «confitería» aparecen CERO '
              'veces en todo el RD 1021/2022.', 'A', 'C', alto=48)
    X.nota_celda(ws, 'A%d' % (M['nota'] + 1), 'CHN-87')
    C.parrafo(ws, M['nota'] + 2,
              'Está PROHIBIDO escribir «hacer bombones en casa para vender es '
              'ilegal en España»: la letra e) existe, y una comunidad puede '
              'haberla usado. Lo honesto es lo que hace esta hoja: preguntarlo '
              'primero.', 'A', 'C', alto=36)
    ws.freeze_panes = 'A4'
    C.pagina(ws, apaisado=False, area='A1:C%d' % fila_listas)
    return ws


# ==========================================================================
# Hoja «Cadmio y Analíticas» (nueva, sin molde)
# ==========================================================================
FAMILIAS_CADMIO = (
    ('Cacao en polvo vendido como tal', SI,
     'Es uno de los tres puntos a los que remite la nota (14) del Anexo I: '
     'tiene límite propio.'),
    ('Tabletas de chocolate y chocolate con leche', SI,
     'Los otros dos puntos. Si vendes tableta, esto te toca directamente.'),
    ('Bombones y chocolate relleno', NO,
     'NO TIENEN LÍMITE PROPIO. Se les aplica la regla de los alimentos '
     'compuestos: el límite se calcula sobre los ingredientes que sí lo tienen '
     'y su proporción en el producto.'),
    ('Turrones, figuras y confitería con cacao', NO,
     'Mismo caso que el bombón: alimento compuesto.'),
    ('Chocolate a la taza en polvo', NOSE,
     'Depende de si encaja en «cacao en polvo» o es una preparación con otros '
     'ingredientes. Míralo referencia a referencia con la denominación legal '
     'que le hayas dado en el libro 4.'),
)

CA = {'sec_que': 5, 'cab_que': 6, 'que_ini': 7, 'que_fin': 11,
      'sec_tu': 13, 'grano': 14, 'boletin': 15, 'tableta': 16,
      'lotes': 17, 'frec': 18, 'coste': 19,
      'sec_res': 21, 'analiticas': 22, 'coste_anio': 23, 'pct': 24,
      'veredicto': 25, 'obligacion': 26,
      'sec_otros': 28, 'ocra': 29, 'hap': 30,
      'nota': 32, 'listas': 37}


def hoja_cadmio(wb):
    ws = wb.create_sheet(H_CAD)
    C.anchos(ws, {'A': 56, 'B': 22, 'C': 100})
    C.encabezar(ws, 'Cadmio y analíticas: qué te aplica de verdad',
                'Lo que es chocolate para la DENOMINACIÓN no lo es para los '
                'CONTAMINANTES. La hoja separa una cosa de la otra y decide si '
                'necesitas analítica propia, con qué frecuencia y cuánto te '
                'cuesta al año.', col_fin='C')

    refs, fila_listas = C.bloque_listas(
        ws, CA['listas'], [('Sí, No o No lo sé', list(SI_NO_NOSE))], col='A')

    def sec(fila, texto):
        C.seccion(ws, 'A%d' % fila, texto)
        for letra in 'BC':
            motor.val(ws, letra + str(fila), '')
            ws[letra + str(fila)].fill = PatternFill('solid',
                                                     fgColor=C.CABECERA)

    def linea(fila, etiqueta, formula=None, fmt=None, nota_txt=None,
              verde=None, chn=None, bold=None):
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True, bold=bold)
        if verde is not None:
            X.entrada(ws, 'B%d' % fila, verde, fmt=fmt, etiqueta=etiqueta,
                      align='center')
        else:
            motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=bold)
        if chn:
            X.nota_celda(ws, 'B%d' % fila, chn)
        if nota_txt:
            C.nota(ws, 'C%d' % fila, nota_txt)
        return 'B%d' % fila

    sec(CA['sec_que'], 'QUÉ ES «PRODUCTO DE CACAO Y DE CHOCOLATE» A EFECTOS DE '
                       'CADMIO')
    C.cabecera(ws, CA['cab_que'],
               [('A', 'Lo que vendes'), ('B', '¿Límite propio de cadmio?'),
                ('C', 'Por qué')], altura=26)
    for i, (que, tiene, porque) in enumerate(FAMILIAS_CADMIO):
        r = CA['que_ini'] + i
        motor.val(ws, 'A%d' % r, que, wrap=True)
        motor.val(ws, 'B%d' % r, tiene, align='center', bold=True)
        motor.val(ws, 'C%d' % r, porque, wrap=True)
        ws.row_dimensions[r].height = 44
    X.nota_celda(ws, 'B%d' % CA['que_ini'], 'CHN-16b')
    X.nota_celda(ws, 'B%d' % (CA['que_ini'] + 2), 'CHN-84')
    motor.semaforo_texto(ws, 'B%d:B%d' % (CA['que_ini'], CA['que_fin']),
                         ((SI, motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          (NO, motor.CF_VERDE_BG, motor.CF_VERDE_FG)))

    sec(CA['sec_tu'], 'TU SITUACIÓN')
    linea(CA['grano'], '¿Importas grano de cacao o compras cobertura ya '
                       'hecha?', verde=NO, chn='CHN-18',
          nota_txt='Marca «Sí» sólo si importas GRANO. El grano y la fibra de '
                   'cacao son donde aparecen los hidrocarburos aromáticos '
                   'policíclicos, y quien importa grano es quien tiene que '
                   'vigilarlos.')
    linea(CA['boletin'], '¿Tu proveedor te da boletín de análisis por lote?',
          verde=NOSE,
          nota_txt='Es la primera línea de defensa y la más barata: pídelo en '
                   'el alta de cliente. Si te lo da, tu analítica propia pasa a '
                   'ser una comprobación, no un control.')
    linea(CA['tableta'], '¿Vendes tableta o cacao en polvo como tal?',
          verde=SI, chn='CHN-16',
          nota_txt='Si sólo vendes bombón relleno, ninguna de tus referencias '
                   'tiene límite propio: se les aplica la regla de alimentos '
                   'compuestos.')
    linea(CA['lotes'], 'Lotes de cobertura distintos que compras al año',
          verde=6, fmt=C.FMT_ENT,
          nota_txt='SUPUESTO sembrado. Cuenta orígenes y proveedores '
                   'distintos, no palés: lo que cambia el riesgo es el origen '
                   'del cacao.')
    linea(CA['frec'], 'Analíticas propias que decides hacer al año',
          verde=1, fmt=C.FMT_ENT,
          nota_txt='LO DECIDES TÚ, y va en tu plan de APPCC. La norma no fija '
                   'una frecuencia de muestreo para un obrador minorista: fija '
                   'un límite que no se puede superar al comercializar.')
    linea(CA['coste'], 'Coste de cada analítica de metales pesados (€)',
          verde=90.0, fmt=C.FMT_EUR,
          nota_txt='SUPUESTO sembrado: pide presupuesto a un laboratorio '
                   'acreditado de tu provincia. Cambia mucho según cuántos '
                   'parámetros metas en el mismo boletín.')
    C.dv_rango(ws, ['B%d' % CA['grano'], 'B%d' % CA['boletin'],
                    'B%d' % CA['tableta']], refs['Sí, No o No lo sé'],
               'Marca Sí, No o No lo sé',
               'Elige una de las tres opciones de la lista del pie.')

    sec(CA['sec_res'], 'LO QUE SALE DE AHÍ')
    linea(CA['analiticas'], 'Analíticas al año',
          ie('B%d' % CA['frec']), C.FMT_ENT, bold=True)
    linea(CA['coste_anio'], 'Coste anual de analíticas (€)',
          ie('B{f}*B{c}'.format(f=CA['frec'], c=CA['coste'])), C.FMT_EUR,
          bold=True,
          nota_txt='Es una partida de gasto fijo del libro 7, pequeña y fácil '
                   'de olvidar hasta que hace falta enseñar un boletín.')
    linea(CA['pct'], 'Lotes cubiertos por tus analíticas (%)',
          ie('IF(B{l}=0,"",B{f}/B{l})'.format(l=CA['lotes'], f=CA['frec'])),
          C.FMT_PCT,
          nota_txt='Si tu proveedor te da boletín por lote, este porcentaje no '
                   'tiene que ser el 100' + N + '%: tu analítica es la '
                   'comprobación, la suya es el control.')
    linea(CA['veredicto'], 'VEREDICTO',
          ie('IF(B{g}="{s}","Importas grano: te tocan cadmio Y '
             'hidrocarburos, y eres tú quien responde de lo que introduce",'
             'IF(B{b}="{s}","Tu proveedor te da boletín: con una analítica '
             'propia de comprobación al año cubres tu parte",'
             '"Sin boletín del proveedor, la analítica propia es tu única '
             'prueba: pídesela a él antes de pagarla tú"))'
             .format(g=CA['grano'], b=CA['boletin'], s=SI)), bold=True)
    ws.merge_cells('B%d:C%d' % (CA['veredicto'], CA['veredicto']))
    ws['B%d' % CA['veredicto']].alignment = Alignment(vertical='top',
                                                      wrap_text=True)
    ws.row_dimensions[CA['veredicto']].height = 44
    C.destacado(ws, 'B%d' % CA['veredicto'])
    linea(CA['obligacion'], 'Lo que la norma SÍ te obliga a hacer',
          ie('IF(B{v}="","","No comercializar producto por encima del límite, '
             'no mezclar para diluir y no descontaminar por vías no '
             'autorizadas. La frecuencia del muestreo la decides tú en tu '
             'APPCC")'.format(v=CA['veredicto'])), chn='CHN-19')
    ws.merge_cells('B%d:C%d' % (CA['obligacion'], CA['obligacion']))
    ws['B%d' % CA['obligacion']].alignment = Alignment(vertical='top',
                                                       wrap_text=True)
    ws.row_dimensions[CA['obligacion']].height = 40

    sec(CA['sec_otros'], 'LOS OTROS DOS CONTAMINANTES DEL CACAO')
    linea(CA['ocra'], 'Ocratoxina A', ie('"Tiene su propio límite en el mismo '
                                         'reglamento: pregúntalo en el mismo '
                                         'boletín, no cuesta más"'),
          chn='CHN-17')
    linea(CA['hap'], 'Hidrocarburos aromáticos policíclicos (HAP)',
          ie('IF(B{g}="{s}","Te tocan: aparecen en el GRANO y en la fibra de '
             'cacao","Si compras cobertura ya hecha, el control es de quien '
             'tuesta: pídele el boletín")'.format(g=CA['grano'], s=SI)),
          chn='CHN-18')
    for f in (CA['ocra'], CA['hap']):
        ws.merge_cells('B%d:C%d' % (f, f))
        ws['B%d' % f].alignment = Alignment(vertical='top', wrap_text=True)
        ws.row_dimensions[f].height = 34

    C.parrafo(ws, CA['nota'],
              'LA TRAMPA DE ESTA HOJA, Y ES CARA: lo que es chocolate para la '
              'denominación no lo es para los contaminantes. La nota que fija '
              'el límite de cadmio remite SÓLO a tres puntos -cacao en polvo, '
              'chocolate y chocolate con leche-, así que tu bombón relleno no '
              'tiene un límite propio: se le aplica la regla de los alimentos '
              'compuestos. Está PROHIBIDO que nadie te diga «tu bombón tiene un '
              'límite de cadmio de X».', 'A', 'C', alto=60)
    C.parrafo(ws, CA['nota'] + 1,
              'Este producto NO publica los valores numéricos de los límites a '
              'propósito: están en el Anexo I del reglamento, cambian, y lo que '
              'tienes que mirar es la fila que le corresponde a TU referencia '
              'con la denominación legal que le hayas dado en el libro 4. El '
              'enlace al texto consolidado está en el comentario de las celdas '
              'de esta hoja.', 'A', 'C', alto=48)
    C.parrafo(ws, CA['nota'] + 2,
              'Y una lectura práctica: el boletín del proveedor es más barato y '
              'más frecuente que tu analítica. Pídelo en el alta de cliente, '
              'que es cuando tienes fuerza para pedirlo. La columna está en la '
              'hoja «Proveedores y EUDR» del libro '
              '«checklist-equipamiento-y-proveedores-cacao.xlsx».',
              'A', 'C', alto=44)
    ws.freeze_panes = 'A4'
    C.pagina(ws, apaisado=False, area='A1:C%d' % fila_listas)
    return ws


# ==========================================================================
# Hoja «EUDR — Tu Papel en la Cadena» (D5, D48)
# ==========================================================================
ORIGENES = ('Compro cobertura ya comercializada en la UE',
            'Importo grano de cacao de fuera de la UE',
            'Compro cobertura y además importo grano')

E = {'sec_rev': 5, 'verificado': 6, 'revisado': 7, 'meses': 8, 'sem_rev': 9,
     'sec_preg': 11, 'origen': 12, 'amparada': 13, 'exporta': 14, 'pyme': 15,
     'sec_ver': 17, 'papel': 18, 'fecha': 19, 'docu': 20, 'inferencia': 21,
     'sec_tabla': 23, 'cab': 24, 'ini': 25, 'fin': 27,
     'nota': 29, 'listas': 34}


def hoja_eudr(wb):
    ws = wb.create_sheet(H_EUDR)
    C.anchos(ws, {'A': 58, 'B': 26, 'C': 104})
    C.encabezar(ws, 'EUDR: tu papel en la cadena y qué fecha te corre',
                'Cuatro preguntas. La norma más viva de todas las que tocan a '
                'este negocio, y por eso la hoja lleva DENTRO su fecha de '
                'revisión.', col_fin='C')

    refs, fila_listas = C.bloque_listas(
        ws, E['listas'], [('Sí, No o No lo sé', list(SI_NO_NOSE)),
                          ('De dónde viene tu cacao', list(ORIGENES))],
        col='A')

    def sec(fila, texto):
        C.seccion(ws, 'A%d' % fila, texto)
        for letra in 'BC':
            motor.val(ws, letra + str(fila), '')
            ws[letra + str(fila)].fill = PatternFill('solid',
                                                     fgColor=C.CABECERA)

    def linea(fila, etiqueta, formula=None, fmt=None, nota_txt=None,
              verde=None, chn=None, bold=None):
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True, bold=bold)
        if verde is not None:
            X.entrada(ws, 'B%d' % fila, verde, fmt=fmt, etiqueta=etiqueta)
        else:
            motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=bold)
        if chn:
            X.nota_celda(ws, 'B%d' % fila, chn)
        if nota_txt:
            C.nota(ws, 'C%d' % fila, nota_txt)
        return 'B%d' % fila

    # --- fecha de revisión DENTRO de la hoja (D5) -------------------------
    sec(E['sec_rev'], 'FECHA DE REVISIÓN DE ESTA HOJA')
    motor.val(ws, 'A%d' % E['verificado'],
              'Verificado contra el texto consolidado el', bold=True)
    motor.val(ws, 'B%d' % E['verificado'], D.FECHA_VERIFICACION_LEGAL,
              align='center', bold=True)
    C.nota(ws, 'C%d' % E['verificado'],
           'Comprueba el estado del EUDR ANTES de comprar cacao. El calendario '
           'de esta norma se ha movido más de una vez, y lo que aquí se afirma '
           'está fechado a propósito para que sepas cuándo deja de ser '
           'fiable.')
    X.nota_celda(ws, 'B%d' % E['verificado'], 'CHN-21')
    X.entrada(ws, 'B%d' % E['revisado'], FECHA_BASE, fmt=C.FMT_FECHA,
              etiqueta='Fecha en que TÚ lo has revisado')
    motor.val(ws, 'A%d' % E['revisado'],
              'La última vez que lo comprobaste TÚ', bold=True)
    motor.dv_fecha(ws, ['B%d' % E['revisado']])
    X.entrada(ws, 'B%d' % E['meses'], 6, fmt=C.FMT_ENT,
              etiqueta='Meses entre revisiones', align='center')
    motor.val(ws, 'A%d' % E['meses'],
              'Cada cuántos meses quieres revisarlo', bold=True)
    C.nota(ws, 'C%d' % E['meses'],
           'SUPUESTO. Seis meses es razonable mientras la norma siga '
           'moviéndose; si compras cacao dos veces al año, revísalo antes de '
           'cada compra.')
    linea(E['sem_rev'], 'Fecha en la que toca volver a mirarlo',
          ie('DATE(YEAR(B{r}),MONTH(B{r})+B{m},DAY(B{r}))'
             .format(r=E['revisado'], m=E['meses'])), C.FMT_FECHA, bold=True,
          nota_txt='Apúntala en el calendario. Es la única hoja de todo el '
                   'producto que caduca sola.')
    C.destacado(ws, 'B%d' % E['sem_rev'])

    # --- las cuatro preguntas --------------------------------------------
    sec(E['sec_preg'], 'LAS CUATRO PREGUNTAS')
    linea(E['origen'], '¿De dónde viene tu cacao?', verde=ORIGENES[0],
          chn='CHN-20',
          nota_txt='El Anexo I incluye la partida 1806, «chocolate y demás '
                   'preparaciones alimenticias que contengan cacao», así que el '
                   'producto terminado está dentro. Y el reglamento cubre '
                   'también la EXPORTACIÓN.')
    C.dv_rango(ws, ['B%d' % E['origen']], refs['De dónde viene tu cacao'],
               'Elige el origen de tu cacao',
               'Elige una de las tres opciones de la lista del pie.')
    linea(E['amparada'],
          '¿Tu cobertura llega amparada por una declaración de diligencia '
          'debida?', verde=NOSE, chn='CHN-23',
          nota_txt='Pregúntaselo a tu proveedor por escrito: es la condición de '
                   'la que cuelga todo lo demás. Si no está amparada (compra '
                   'anterior al EUDR, o proveedor que no lo acredita), tu '
                   'calificación deja de ser automática.')
    linea(E['exporta'], '¿Exportas producto fuera de la Unión Europea?',
          verde=NO, chn='CHN-60',
          nota_txt='Exportar también está sujeto. Un pedido corporativo a una '
                   'filial fuera de la Unión cuenta.')
    linea(E['pyme'],
          '¿Eres persona física, microempresa o pequeña empresa, y estabas '
          'establecida como tal a 31 de diciembre de 2024?', verde=NO,
          chn='CHN-22',
          nota_txt='Esta pregunta sólo cambia algo si además eres OPERADOR: el '
                   'aplazamiento del art. 38.3 es para operadores, y el art. '
                   '2.15 excluye de esa palabra a los operadores posteriores.')
    C.dv_rango(ws, ['B%d' % E['amparada'], 'B%d' % E['exporta'],
                    'B%d' % E['pyme']], refs['Sí, No o No lo sé'],
               'Marca Sí, No o No lo sé',
               'Elige una de las tres opciones de la lista del pie.')

    # --- veredicto --------------------------------------------------------
    sec(E['sec_ver'], 'TU PAPEL, TU FECHA Y TUS PAPELES')
    # Las tres opciones de origen viven en la columna B del bloque de listas
    # (la primera lista ocupa la A): grano = 2.ª y 3.ª opción.
    B_GRANO = E['listas'] + 3
    B_MIXTO = E['listas'] + 4
    linea(E['papel'], 'Tu papel en la cadena',
          ie('IF(OR($B${o}=$B${g},$B${o}=$B${gc}),"OPERADOR: importas grano, '
             'así que haces la primera comercialización en el mercado de la '
             'Unión",IF($B${e}="{s}","OPERADOR: exportar también está sujeto",'
             'IF($B${a}="{s}","OPERADOR POSTERIOR (art. 2.15 ter)",'
             '"Sin resolver: pregunta a tu proveedor si tu cobertura está '
             'amparada por una declaración")))'
             .format(o=E['origen'], g=B_GRANO, gc=B_MIXTO,
                     e=E['exporta'], a=E['amparada'], s=SI)), bold=True,
          chn='CHN-23')
    linea(E['fecha'], 'La fecha que te corre',
          ie('IF($B${p}="","",IF(LEFT($B${p},18)="OPERADOR POSTERIOR",'
             '"30 de diciembre de 2026",IF($B${p}="Sin resolver: pregunta a tu '
             'proveedor si tu cobertura está amparada por una declaración",'
             '"Sin resolver: primero aclara tu papel",IF($B${y}="{s}",'
             '"30 de junio de 2027 SI confirmas que el aplazamiento del art. '
             '38.3 te alcanza; si no, 30 de diciembre de 2026",'
             '"30 de diciembre de 2026"))))'
             .format(p=E['papel'], y=E['pyme'], s=SI)), bold=True,
          chn='CHN-21')
    linea(E['docu'], 'Lo que te toca',
          ie('IF($B${p}="","",IF(LEFT($B${p},18)="OPERADOR POSTERIOR",'
             '"Recoger y conservar los números de referencia de las '
             'declaraciones de tus proveedores que sean OPERADORES, y '
             'registrar a quién suministras tú",IF(LEFT($B${p},8)="OPERADOR",'
             '"Diligencia debida COMPLETA antes de introducir en el mercado, '
             'declaración presentada previamente, asunción de responsabilidad '
             'y registro de las declaraciones durante cinco años",'
             '"Primero aclara tu papel: sin eso no se sabe qué te toca")))'
             .format(p=E['papel'])), chn='CHN-24')
    linea(E['inferencia'], 'Y esto va DECLARADO, no como nivel A',
          ie('IF(B{p}="","","El paso «una chocolatería que compra cobertura es '
             'operador posterior, así que el aplazamiento del art. 38.3 no le '
             'alcanza» es una INFERENCIA nuestra, con el art. 2.15 ter como '
             'condición. Si tu cobertura NO está amparada, la calificación deja '
             'de ser automática y hay que revisarla")'.format(p=E['papel'])),
          chn='CHN-22')
    for f in (E['papel'], E['fecha'], E['docu'], E['inferencia']):
        ws.merge_cells('B%d:C%d' % (f, f))
        ws['B%d' % f].alignment = Alignment(vertical='top', wrap_text=True)
        ws.row_dimensions[f].height = 52
    C.destacado(ws, 'B%d' % E['papel'])
    C.destacado(ws, 'B%d' % E['fecha'])

    # --- los tres papeles -------------------------------------------------
    sec(E['sec_tabla'], 'LOS TRES PAPELES, Y QUÉ LE PIDES A CADA PROVEEDOR')
    C.cabecera(ws, E['cab'], [('A', 'Papel'), ('B', '¿Le pides el nº de DDS?'),
                              ('C', 'Qué significa')], altura=26)
    for i, papel in enumerate(D.PAPELES_EUDR):
        r = E['ini'] + i
        motor.val(ws, 'A%d' % r, papel, bold=True)
        motor.val(ws, 'B%d' % r, SI if i == 0 else NO, align='center',
                  bold=True)
        motor.val(ws, 'C%d' % r, D.PAPELES_EUDR_TEXTO[papel], wrap=True)
        ws.row_dimensions[r].height = 62
    X.nota_celda(ws, 'B%d' % E['ini'], 'CHN-24')
    X.nota_celda(ws, 'C%d' % E['ini'], 'CHN-25')
    motor.semaforo_texto(ws, 'B%d:B%d' % (E['ini'], E['fin']),
                         ((SI, motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          (NO, motor.CF_VERDE_BG, motor.CF_VERDE_FG)))

    C.parrafo(ws, E['nota'], D.NOTA_EUDR, 'A', 'C', alto=92)
    C.parrafo(ws, E['nota'] + 1,
              'EL NÚMERO DE LA DDS NO SE LE PIDE A TODO EL MUNDO. El art. 5.3 '
              'obliga a guardar los datos de todos tus proveedores, pero los '
              'números de referencia de las declaraciones «únicamente en el '
              'caso de que su proveedor sea un operador». El árbol que lo '
              'resuelve proveedor a proveedor está en la hoja «Proveedores y '
              'EUDR» del libro «checklist-equipamiento-y-proveedores-cacao».',
              'A', 'C', alto=52)
    C.parrafo(ws, E['nota'] + 2,
              'Y la otra mitad del mismo artículo obliga a registrar a los '
              'operadores posteriores y comerciantes A LOS QUE TÚ SUMINISTRAS, '
              'y a conservarlo cinco años: ésa es la hoja «Clientes a los que '
              'Suministras» del mismo libro. Está PROHIBIDO escribir «basta con '
              'registrar a tus proveedores».', 'A', 'C', alto=44)
    ws.freeze_panes = 'A4'
    C.pagina(ws, apaisado=False, area='A1:C%d' % fila_listas)
    return ws


# ==========================================================================
# Hoja «Registro de Formación»
# ==========================================================================
R_CAB = 6
R_INI = 7
R_FIN = R_INI + len(D.PLANTILLA) + 2      # tres filas libres de más
R_SEC_PAR = R_FIN + 2
R_VALIDEZ = R_SEC_PAR + 1
R_CONTROL = R_SEC_PAR + 2
R_AVISO = R_SEC_PAR + 3
R_SEC_RES = R_SEC_PAR + 5
R_CON = R_SEC_RES + 1
R_CADUCADAS = R_SEC_RES + 2
R_PROXIMAS = R_SEC_RES + 3
R_VER = R_SEC_RES + 4
R_NOTA = R_SEC_RES + 6
R_PIE = R_NOTA + 4
LIBRE_P = '(libre: añade aquí a tu persona)'


def hoja_formacion(wb):
    ws = wb.create_sheet(H_FOR)
    C.anchos(ws, {'A': 6, 'B': 30, 'C': 22, 'D': 16, 'E': 40, 'F': 16,
                  'G': 16, 'H': 22, 'I': 78})
    C.encabezar(ws, 'Registro de formación del personal',
                'El «carnet de manipulador» no existe. Lo que la norma exige es '
                'que la EMPRESA garantice la formación de cada persona de '
                'acuerdo con su actividad laboral y pueda ACREDITARLA. Eso es '
                'esta tabla.', col_fin='I')

    C.seccion(ws, 'A5', 'Una línea por persona')
    C.cabecera(ws, R_CAB,
               [('A', 'Nº'), ('B', 'Persona'), ('C', 'Perfil'),
                ('D', 'Jornada'), ('E', 'Contenido de la formación'),
                ('F', 'Fecha de la formación'), ('G', 'Caduca el'),
                ('H', 'Estado'), ('I', 'Notas')], altura=30)

    v_fecha, v_conten, v_persona = [], [], []
    n_filas = R_FIN - R_INI + 1
    for i in range(n_filas):
        r = R_INI + i
        if i < len(D.PLANTILLA):
            pid, perfil, fte, _orden, zona, horas, turno = D.PLANTILLA[i]
            persona = 'Persona %d (%s)' % (i + 1, perfil)
            contenido = ('Higiene, alérgenos y trazabilidad aplicados a '
                         + ('el obrador' if zona == 'OBRADOR' else 'la tienda'))
        else:
            perfil, turno = D.PERFILES_KIT[0], ''
            persona, contenido = LIBRE_P, 'Pendiente'
        motor.val(ws, 'A%d' % r, i + 1, fmt=C.FMT_ENT, align='center')
        X.entrada(ws, 'B%d' % r, persona, etiqueta='Persona %d' % (i + 1))
        v_persona.append('B%d' % r)
        X.entrada(ws, 'C%d' % r, perfil, etiqueta='Perfil %d' % (i + 1))
        motor.val(ws, 'D%d' % r, turno or 'Pendiente', wrap=True)
        X.entrada(ws, 'E%d' % r, contenido, etiqueta='Contenido %d' % (i + 1),
                  wrap=True)
        v_conten.append('E%d' % r)
        X.entrada(ws, 'F%d' % r, FECHA_BASE, fmt=C.FMT_FECHA,
                  etiqueta='Fecha de formación %d' % (i + 1))
        v_fecha.append('F%d' % r)
        motor.f(ws, 'G%d' % r,
                ie('IF($B{r}="{lb}","",DATE(YEAR($F{r}),MONTH($F{r})+$C${v},'
                   'DAY($F{r})))'.format(r=r, lb=LIBRE_P, v=R_VALIDEZ)),
                fmt=C.FMT_FECHA)
        motor.f(ws, 'H%d' % r,
                ie('IF($B{r}="{lb}","",IF($G{r}<$C${c},"CADUCADA",'
                   'IF($G{r}<$C${c}+$C${p},"Caduca pronto","Vigente")))'
                   .format(r=r, lb=LIBRE_P, c=R_CONTROL, p=R_AVISO)),
                bold=True)
        motor.val(ws, 'I%d' % r, '', wrap=True)
        ws.row_dimensions[r].height = 28
    X.nota_celda(ws, 'B%d' % R_CAB, 'CHN-69')
    motor.dv_fecha(ws, v_fecha)
    motor.semaforo_texto(ws, 'H%d:H%d' % (R_INI, R_FIN),
                         (('CADUCADA', motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('Caduca pronto', motor.CF_AMBAR_BG,
                           motor.CF_AMBAR_FG),
                          ('Vigente', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))

    C.seccion(ws, 'A%d' % R_SEC_PAR, 'Parámetros de esta hoja')
    motor.val(ws, 'A%d' % R_VALIDEZ, 'Validez que TÚ fijas (meses)', bold=True)
    ws.merge_cells('A%d:B%d' % (R_VALIDEZ, R_VALIDEZ))
    X.entrada(ws, 'C%d' % R_VALIDEZ, 24, fmt=C.FMT_ENT,
              etiqueta='Validez de la formación en meses', align='center')
    C.nota(ws, 'I%d' % R_VALIDEZ,
           'LA NORMA NO FIJA UNA CADUCIDAD, porque no hay carnet que caduque. '
           'Lo que hay es una obligación continua del empresario. Poner dos '
           'años es un criterio razonable de la casa para que el registro no se '
           'quede dormido; súbelo o bájalo, pero déjalo escrito en tu APPCC.')
    motor.val(ws, 'A%d' % R_CONTROL, 'Fecha de control', bold=True)
    ws.merge_cells('A%d:B%d' % (R_CONTROL, R_CONTROL))
    X.entrada(ws, 'C%d' % R_CONTROL, FECHA_BASE, fmt=C.FMT_FECHA,
              etiqueta='Fecha de control del registro')
    motor.dv_fecha(ws, ['C%d' % R_CONTROL])
    C.nota(ws, 'I%d' % R_CONTROL,
           'La fecha desde la que se mira si algo ha caducado. Ponla en «hoy» '
           'cada vez que revises el registro.')
    motor.val(ws, 'A%d' % R_AVISO, 'Aviso de «caduca pronto» (días antes)',
              bold=True)
    ws.merge_cells('A%d:B%d' % (R_AVISO, R_AVISO))
    X.entrada(ws, 'C%d' % R_AVISO, 60, fmt=C.FMT_ENT,
              etiqueta='Días de aviso antes de caducar', align='center')
    C.nota(ws, 'I%d' % R_AVISO,
           'SUPUESTO. Con cuánta antelación quieres que el registro te avise. '
           'Dos meses dan tiempo a organizar una sesión sin parar el obrador.')

    C.seccion(ws, 'A%d' % R_SEC_RES, 'Resumen')

    def res(fila, etiqueta, formula, fmt=None, nota_txt=None, bold=True):
        motor.val(ws, 'B%d' % fila, etiqueta, bold=bold, wrap=True)
        motor.f(ws, 'C%d' % fila, formula, fmt=fmt, bold=bold)
        if nota_txt:
            C.nota(ws, 'I%d' % fila, nota_txt)

    res(R_CON, 'Personas con formación registrada',
        '=SUMPRODUCT(--($B${a}:$B${b}<>"{lb}"))'
        .format(a=R_INI, b=R_FIN, lb=LIBRE_P), C.FMT_ENT)
    res(R_CADUCADAS, 'Formaciones CADUCADAS',
        ie('COUNTIF(H%d:H%d,"CADUCADA")' % (R_INI, R_FIN)), C.FMT_ENT,
        'Cada una de éstas es una persona trabajando sin la acreditación que '
        'la empresa tiene que poder enseñar.')
    res(R_PROXIMAS, 'Formaciones que caducan pronto',
        ie('COUNTIF(H%d:H%d,"Caduca pronto")' % (R_INI, R_FIN)), C.FMT_ENT)
    res(R_VER, 'VEREDICTO',
        ie('IF(C{c}>0,"Tienes formación caducada: es lo primero que se pide en '
           'una inspección",IF(C{p}>0,"Programa ya las que caducan pronto",'
           '"Registro al día"))'.format(c=R_CADUCADAS, p=R_PROXIMAS)))
    ws.merge_cells('C%d:H%d' % (R_VER, R_VER))
    ws['C%d' % R_VER].alignment = Alignment(vertical='top', wrap_text=True)
    ws.row_dimensions[R_VER].height = 32
    C.destacado(ws, 'C%d' % R_VER)
    motor.semaforo_isnumber(ws, 'C%d' % R_CADUCADAS, '$C$%d' % R_CADUCADAS,
                            '>', '0')
    motor.semaforo_isnumber(ws, 'C%d' % R_PROXIMAS, '$C$%d' % R_PROXIMAS,
                            '>', '0', bg=motor.CF_AMBAR_BG,
                            fg=motor.CF_AMBAR_FG)

    C.parrafo(ws, R_NOTA,
              'EL CARNET DE MANIPULADOR NO EXISTE. Lo que existe es la '
              'obligación de la empresa de garantizar que cada persona tiene la '
              'formación que su puesto requiere y de poder acreditarlo. Quien '
              'te venda un «carnet» te está vendiendo un papel sin valor legal; '
              'lo que vale es este registro, con su contenido y su fecha.',
              'A', 'I', alto=48)
    C.parrafo(ws, R_NOTA + 1,
              'Los tres perfiles que vienen sembrados son los del ejemplo del '
              'producto y llevan los nombres del Kit de Tareas Chocolatería '
              '(Chocolatero, Dependiente y Encargado), para que las dos cosas '
              'casen si tienes los dos. Las filas libres son para tu equipo '
              'real.', 'A', 'I', alto=40)
    C.pie(ws, R_PIE, 'A', 'C')
    ws.freeze_panes = 'B%d' % R_INI
    C.pagina(ws, titulos='$%d:$%d' % (R_CAB, R_CAB),
             area='A1:I%d' % (R_PIE + 2))
    return ws


# ==========================================================================
# Hoja «Cronograma y Ruta Crítica»
# ==========================================================================
COLS_MAT = ('C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O')
FMT_CENTINELA = '#,##0.0;;;'

G_ARRANQUE = 5
G_CENTINELA = 6
G_CAB = 8
G_INI = 9
G_FIN = G_INI + len(D.GANTT) - 1
G_SEC_MAT = G_FIN + 2
G_MAT_CAB = G_SEC_MAT + 1
G_MAT_INI = G_MAT_CAB + 1
G_MAT_FIN = G_MAT_INI + len(D.GANTT) - 1
G_SEC_RES = G_MAT_FIN + 2
G_DURACION = G_SEC_RES + 1
G_CRITICOS = G_SEC_RES + 2
G_MES_AP = G_SEC_RES + 3
G_NOMBRE_MES = G_SEC_RES + 4
G_TEMPORADA = G_SEC_RES + 5
G_AVISO = G_SEC_RES + 6
G_CRU_SEC = G_AVISO + 2
G_CRU_VERDE = G_CRU_SEC + 1
G_CRU_SEMMES = G_CRU_SEC + 2
G_CRU_MESES = G_CRU_SEC + 3
G_CRU_RUTA = G_CRU_SEC + 4
G_CRU_DIF = G_CRU_SEC + 5
G_CRU_CUADRE = G_CRU_SEC + 6
G_SEC_CAMP = G_CRU_CUADRE + 2
G_CAMP_CAB = G_SEC_CAMP + 1
G_CAMP_INI = G_CAMP_CAB + 1
G_CAMP_FIN = G_CAMP_INI + len(D.CAMPANAS) - 1
G_NOTA = G_CAMP_FIN + 2
G_LISTAS = G_NOTA + 4

NOTAS_GANTT = {
    'H4': 'Declaración responsable, NO licencia previa: ningún ayuntamiento '
          'puede exigirte licencia de actividad hasta 750 metros cuadrados, '
          'porque el epígrafe 644.5 está en el Anexo de la Ley 12/2012.',
    'H6': 'ES EL HITO QUE MUEVE LA FECHA. Su duración aquí es un SUPUESTO; el '
          'plazo real lo tecleas en el libro 9 y lo traes al cruce de abajo.',
    'H7': 'La partida que nadie presupuesta y la que decide si la cobertura '
          'cristaliza. Va después de la obra porque necesita los cerramientos '
          'hechos.',
    'H9': 'Comunicación o declaración responsable a tu comunidad: NO habilita '
          'para abrir, así que no la esperes sentado, pero preséntala antes de '
          'vender.',
    'H12': 'Las pruebas de templado no son un trámite: son la semana en que '
           'descubres si tu clima y tu máquina se llevan bien.',
}


def hoja_gantt(wb):
    ws = wb.create_sheet(H_GAN)
    C.anchos(ws, dict([('A', 8), ('B', 52)]
                      + [(c, 11) for c in COLS_MAT] + [('P', 13), ('Q', 88)]))
    C.encabezar(ws, 'Cronograma y ruta crítica de la apertura',
                'Trece hitos con su duración y sus dependencias. Todo en MESES '
                'y con aritmética de índices: no hay ni una función de fecha, '
                'porque el calendario laboral no decide nada aquí.',
                col_fin='Q')

    refs, fila_listas = C.bloque_listas(
        ws, G_LISTAS,
        [('Hitos y «sin dependencia»', [SIN_DEP] + [h[0] for h in D.GANTT]),
         ('Meses del año', list(D.MESES))], col='A')
    # `bloque_listas` devuelve la referencia con «=» delante (lista para
    # una validación de datos); dentro de una fórmula hay que quitárselo.
    ref_meses = refs['Meses del año'].lstrip('=')

    motor.val(ws, 'A%d' % G_ARRANQUE, 'Mes en que arranca el proyecto (1-12)')
    ws.merge_cells('A%d:B%d' % (G_ARRANQUE, G_ARRANQUE))
    X.entrada(ws, 'C%d' % G_ARRANQUE, D.MES_INICIO_PROYECTO, fmt=C.FMT_ENT,
              etiqueta='Mes de arranque del proyecto', align='center')
    C.nota(ws, 'Q%d' % G_ARRANQUE,
           'El mes natural en el que das el primer paso. De aquí sale la fecha '
           'de apertura estimada, y por eso conviene probar dos o tres: mover '
           'el arranque dos meses puede meterte en Navidad o sacarte de ella. '
           'El ejemplo arranca en octubre para abrir el 1 de junio, que es mes '
           'de temporada media, con seis meses de rodaje antes de Navidad y con '
           'el valle de agosto dentro del arranque, que es cuando sale barato.')
    motor.val(ws, 'A%d' % G_CENTINELA,
              'Valor centinela de la matriz de dependencias (meses)')
    ws.merge_cells('A%d:B%d' % (G_CENTINELA, G_CENTINELA))
    motor.val(ws, 'C%d' % G_CENTINELA, 999, fmt=C.FMT_ENT, align='center')
    C.nota(ws, 'Q%d' % G_CENTINELA,
           'Truco de cálculo, no un dato: en la matriz de dependencias las '
           'casillas que no aplican llevan este número en vez de quedarse '
           'vacías, para que MIN pueda trabajar sólo con números. El formato lo '
           'esconde. Por eso NO está en verde: si alguien escribe aquí un 3, '
           'las trece holguras y la ruta crítica cambian sin un solo aviso.')

    C.cabecera(ws, G_CAB,
               [('A', 'Id'), ('B', 'Hito'), ('C', 'Duración (meses)'),
                ('D', 'Depende de (1)'), ('E', 'Depende de (2)'),
                ('F', 'Depende de (3)'), ('G', 'Empieza (mes del proyecto)'),
                ('H', 'Acaba (mes del proyecto)'), ('I', 'Holgura (meses)'),
                ('J', '¿Ruta crítica?'), ('K', 'Mes natural de fin'),
                ('Q', 'Notas')])

    deps_coords = []
    for i, (hid, hito, dur, deps) in enumerate(D.GANTT):
        fila = G_INI + i
        motor.val(ws, 'A%d' % fila, hid, align='center')
        motor.val(ws, 'B%d' % fila, hito, wrap=True)
        X.entrada(ws, 'C%d' % fila, dur, fmt=C.FMT_DEC1,
                  etiqueta='Duración de ' + hid, align='center')
        lista = list(deps) + [SIN_DEP] * (3 - len(deps))
        for j, letra in enumerate(('D', 'E', 'F')):
            X.entrada(ws, '%s%d' % (letra, fila), lista[j],
                      etiqueta='Dependencia %d de %s' % (j + 1, hid),
                      align='center')
            deps_coords.append('%s%d' % (letra, fila))
        arriba = fila - 1
        trozos = []
        for letra in ('D', 'E', 'F'):
            trozos.append('IFERROR(INDEX($H$%d:H%d,MATCH(%s%d,$A$%d:A%d,0)),0)'
                          % (G_CAB, arriba, letra, fila, G_CAB, arriba))
        motor.f(ws, 'G%d' % fila, ie('MAX(%s)' % ','.join(trozos)),
                fmt=C.FMT_DEC1)
        motor.f(ws, 'H%d' % fila, ie('G%d+C%d' % (fila, fila)),
                fmt=C.FMT_DEC1)
        if hid in NOTAS_GANTT:
            C.nota(ws, 'Q%d' % fila, NOTAS_GANTT[hid])
        ws.row_dimensions[fila].height = 26
    C.dv_rango(ws, deps_coords, refs['Hitos y «sin dependencia»'],
               'Elige un hito o «-»',
               'Escribe el identificador de otro hito, o «-» si este hito no '
               'depende de ninguno. Sólo puede depender de hitos que estén MÁS '
               'ARRIBA en la tabla.')
    X.nota_celda(ws, 'B%d' % (G_INI + 3), 'CHN-49')

    # --- matriz de dependencias -------------------------------------------
    C.seccion(ws, 'A%d' % G_SEC_MAT,
              'MATRIZ DE DEPENDENCIAS: QUÉ HITO BLOQUEA A CUÁL')
    for letra in list('B') + list(COLS_MAT) + ['Q']:
        motor.val(ws, letra + str(G_SEC_MAT), '')
        ws[letra + str(G_SEC_MAT)].fill = PatternFill('solid',
                                                      fgColor=C.CABECERA)
    C.cabecera(ws, G_MAT_CAB,
               [('A', 'Sucesor'), ('B', 'empieza en el mes...')]
               + [(COLS_MAT[k], D.GANTT[k][0]) for k in range(len(D.GANTT))]
               + [('Q', 'Notas')], altura=22)
    for i, (hid, hito, dur, deps) in enumerate(D.GANTT):
        fila = G_MAT_INI + i
        fila_h = G_INI + i
        motor.val(ws, 'A%d' % fila, hid, align='center')
        motor.f(ws, 'B%d' % fila, ie('G%d' % fila_h), fmt=C.FMT_DEC1)
        for k in range(len(D.GANTT)):
            fila_pred = G_INI + k
            motor.f(ws, '%s%d' % (COLS_MAT[k], fila),
                    ie('IF(OR($D${0}=$A${1},$E${0}=$A${1},$F${0}=$A${1}),'
                       '$G${0},$C${2})'
                       .format(fila_h, fila_pred, G_CENTINELA)),
                    fmt=FMT_CENTINELA)
    C.nota(ws, 'Q%d' % G_MAT_INI,
           'Se lee por COLUMNAS: en la columna de H6 aparece el mes en que '
           'empieza cada hito que depende de H6. La holgura de H6 es la '
           'distancia entre cuando acaba y el primero de esos meses. Las '
           'casillas que parecen vacías no lo están: llevan el centinela y el '
           'formato las esconde.')

    for i, (hid, hito, dur, deps) in enumerate(D.GANTT):
        fila_h = G_INI + i
        col = COLS_MAT[i]
        rango = '%s%d:%s%d' % (col, G_MAT_INI, col, G_MAT_FIN)
        motor.f(ws, 'I%d' % fila_h,
                ie('MIN(MIN({0}),MAX($H${1}:$H${2}))-H{3}'
                   .format(rango, G_INI, G_FIN, fila_h)), fmt=C.FMT_DEC1)
        motor.f(ws, 'J%d' % fila_h,
                ie('IF(ROUND(I{0},3)<=0,"{1}","{2}")'.format(fila_h, SI, NO)))
        motor.f(ws, 'K%d' % fila_h,
                ie('INDEX({0},ROUNDDOWN(MOD($C${1}-1+H{2},12),0)+1)'
                   .format(ref_meses, G_ARRANQUE, fila_h)))
    motor.regla_expresion(ws, 'J%d:J%d' % (G_INI, G_FIN),
                          '=$J%d="%s"' % (G_INI, SI),
                          bg=motor.CF_AMBAR_BG, fg=motor.CF_AMBAR_FG)

    # --- resultados --------------------------------------------------------
    C.seccion(ws, 'A%d' % G_SEC_RES, 'LO QUE SALE DE TODO ESTO')
    for letra in list('B') + list(COLS_MAT) + ['Q']:
        motor.val(ws, letra + str(G_SEC_RES), '')
        ws[letra + str(G_SEC_RES)].fill = PatternFill('solid',
                                                      fgColor=C.CABECERA)

    def res(fila, etiqueta, formula, fmt=None, nota_txt=None, bold=None,
            verde=None, etiq_verde=''):
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True, bold=bold)
        ws.merge_cells('A%d:B%d' % (fila, fila))
        if verde is not None:
            X.entrada(ws, 'C%d' % fila, verde, fmt=fmt, etiqueta=etiq_verde)
        else:
            motor.f(ws, 'C%d' % fila, formula, fmt=fmt, bold=bold)
        if nota_txt:
            C.nota(ws, 'Q%d' % fila, nota_txt)

    res(G_DURACION, 'Duración total del proyecto (meses)',
        ie('MAX(H%d:H%d)' % (G_INI, G_FIN)), C.FMT_DEC1, bold=True,
        nota_txt='Desde el primer día de búsqueda de local hasta el día que '
                 'abres la puerta. No incluye lo que tardes en decidirte.')
    res(G_CRITICOS, 'Hitos SIN holgura (ruta crítica)',
        ie('COUNTIF(J%d:J%d,"%s")' % (G_INI, G_FIN, SI)), C.FMT_ENT,
        nota_txt='Los que si se retrasan un día retrasan la apertura un día. '
                 'Cuenta TODOS los de holgura cero, que son más que los del '
                 'camino más largo: dos hitos en paralelo de la misma duración '
                 'no tienen holgura ninguno de los dos.')
    res(G_MES_AP, 'Mes natural en el que abres (1-12)',
        ie('ROUNDDOWN(MOD($C${0}-1+C{1},12),0)+1'
           .format(G_ARRANQUE, G_DURACION)), C.FMT_ENT, bold=True)
    res(G_NOMBRE_MES, 'Nombre de ese mes',
        ie('INDEX(%s,C%d)' % (ref_meses, G_MES_AP)), None, bold=True)
    res(G_TEMPORADA, 'Temporada de ese mes, según el calendario del kit',
        ie('INDEX($C${0}:$C${1},C{2})'.format(G_CAMP_INI, G_CAMP_FIN,
                                              G_MES_AP)), None, bold=True,
        nota_txt='Las doce filas de temporada son copia declarada del '
                 'calendario anual del Kit de Tareas Chocolatería: siete meses '
                 'Alta, cuatro Media y uno Baja.')
    res(G_AVISO, 'Aviso',
        ie('IF(C{0}="Alta","Abres DENTRO de temporada ALTA: el equipo estrena '
           'obrador el mes de más carga del año, y eso se paga en mermas y en '
           'encargos que no salen",IF(C{0}="Baja","Abres en agosto, que es el '
           'único mes Baja: el obrador para y la tienda vive del turista. Es '
           'barato para rodar, pero no mide nada","Abres en temporada media: '
           'tienes rodaje antes del siguiente pico"))'.format(G_TEMPORADA)),
        bold=True)
    ws.merge_cells('C%d:O%d' % (G_AVISO, G_AVISO))
    ws['C%d' % G_AVISO].alignment = Alignment(vertical='top', wrap_text=True)
    ws.row_dimensions[G_AVISO].height = 34
    motor.regla_expresion(ws, 'C%d:C%d' % (G_TEMPORADA, G_TEMPORADA),
                          '=$C$%d="Alta"' % G_TEMPORADA,
                          bg=motor.CF_AMBAR_BG, fg=motor.CF_AMBAR_FG)

    # --- CRUCE 8 <- 9 ------------------------------------------------------
    C.seccion(ws, 'A%d' % G_CRU_SEC,
              'CRUCE CON EL LIBRO 9: el plazo de la maquinaria contra tu ruta '
              'crítica')
    for letra in list('B') + list(COLS_MAT) + ['Q']:
        motor.val(ws, letra + str(G_CRU_SEC), '')
        ws[letra + str(G_CRU_SEC)].fill = PatternFill('solid',
                                                      fgColor=C.CABECERA)
    res(G_CRU_VERDE,
        'Trae aquí el plazo crítico en semanas de ' + CRUCE9_REF,
        None, C.FMT_DEC1,
        nota_txt='VALOR POR DEFECTO DECLARADO: el plazo más largo de las líneas '
                 'críticas de la dotación de ejemplo. Los plazos de entrega son '
                 'SUPUESTOS en todo el producto -ningún distribuidor los '
                 'publica-, así que en cuanto tengas uno POR ESCRITO en un '
                 'presupuesto, tráelo aquí. No hay ninguna fórmula que apunte a '
                 'otro fichero: esto es una copia declarada.',
        verde=CRUCE9_DEFECTO,
        etiq_verde='Plazo crítico de maquinaria traído del libro 9')
    X.CRUCES_VERDES.append((H_GAN, 'C%d' % G_CRU_VERDE,
                            'Plazo crítico de maquinaria (8 <- 9)'))
    res(G_CRU_SEMMES, 'Semanas que tiene un mes medio', None, C.FMT_DEC1,
        nota_txt='Constante de conversión, en celda para que no viva dentro '
                 'de ninguna fórmula: 52 semanas repartidas en 12 meses dan '
                 '4,33 semanas por mes.',
        verde=4.33, etiq_verde='Semanas por mes')
    res(G_CRU_MESES, 'Ese plazo, en meses',
        ie('IF(C{s}=0,"",C{v}/C{s})'.format(v=G_CRU_VERDE, s=G_CRU_SEMMES)),
        C.FMT_DEC1,
        nota_txt='Se convierte a meses para poder compararlo con la ruta '
                 'crítica, que trabaja en meses decimales.')
    res(G_CRU_RUTA, 'Tu ruta crítica, en meses',
        ie('C%d' % G_DURACION), C.FMT_DEC1)
    res(G_CRU_DIF, 'Margen entre la ruta crítica y el plazo (meses)',
        ie('C{r}-C{m}'.format(r=G_CRU_RUTA, m=G_CRU_MESES)), C.FMT_DEC1,
        nota_txt='Negativo = la máquina llega después de que esté todo el '
                 'papeleo hecho.')
    motor.val(ws, 'A%d' % G_CRU_CUADRE,
              'CUADRE: ¿quién manda tu fecha de apertura?', bold=True)
    ws.merge_cells('A%d:B%d' % (G_CRU_CUADRE, G_CRU_CUADRE))
    X.cruce_cuadre(
        ws, 'C%d' % G_CRU_CUADRE,
        '=IF(OR(C{d}="",C{m}=""),"",IF(C{d}<0,'
        '"LA MANDA LA MAQUINARIA: tu ruta crítica es más corta que el plazo de '
        'entrega, así que la fecha de apertura la fija el equipo, no el '
        'papeleo","CUADRA: el papeleo es lo más largo, y es lo que fija la '
        'fecha"))'.format(d=G_CRU_DIF, m=G_CRU_MESES))
    ws.merge_cells('C%d:O%d' % (G_CRU_CUADRE, G_CRU_CUADRE))
    ws['C%d' % G_CRU_CUADRE].alignment = Alignment(vertical='top',
                                                   wrap_text=True)
    ws.row_dimensions[G_CRU_CUADRE].height = 40
    C.destacado(ws, 'C%d' % G_CRU_CUADRE)
    motor.semaforo_texto(
        ws, 'C%d' % G_CRU_CUADRE,
        (('LA MANDA LA MAQUINARIA: tu ruta crítica es más corta que el plazo '
          'de entrega, así que la fecha de apertura la fija el equipo, no el '
          'papeleo', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
         ('CUADRA: el papeleo es lo más largo, y es lo que fija la fecha',
          motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    C.nota(ws, 'Q%d' % G_CRU_CUADRE,
           'Sin esta fila, leerías una fecha de apertura en este libro y un '
           'plazo incompatible en el 9 sin un solo aviso. Es el defecto que '
           'este cruce viene a cerrar.')

    # --- las doce filas del calendario ------------------------------------
    C.seccion(ws, 'A%d' % G_SEC_CAMP,
              'EL CALENDARIO DEL AÑO (copia declarada del Kit de Tareas '
              'Chocolatería)')
    for letra in list('B') + list(COLS_MAT) + ['Q']:
        motor.val(ws, letra + str(G_SEC_CAMP), '')
        ws[letra + str(G_SEC_CAMP)].fill = PatternFill('solid',
                                                       fgColor=C.CABECERA)
    C.cabecera(ws, G_CAMP_CAB,
               [('A', 'Mes'), ('B', 'Campaña'), ('C', 'Temporada'),
                ('D', 'Nº de mes'), ('Q', 'Notas')], altura=22)
    for i, camp in enumerate(D.CAMPANAS):
        fila = G_CAMP_INI + i
        motor.val(ws, 'A%d' % fila, camp['nombre_mes'])
        motor.val(ws, 'B%d' % fila, camp['campana'], wrap=True)
        motor.val(ws, 'C%d' % fila, camp['temporada'], align='center')
        motor.val(ws, 'D%d' % fila, camp['mes'], fmt=C.FMT_ENT, align='center')
    motor.semaforo_texto(ws, 'C%d:C%d' % (G_CAMP_INI, G_CAMP_FIN),
                         (('Alta', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          ('Baja', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    C.nota(ws, 'Q%d' % G_CAMP_INI,
           'Los euros de cada campaña y si tu equipo aguanta el pico están en '
           '«campanas-y-valle-del-ano.xlsx». Aquí sólo se usan los meses y su '
           'temporada, para avisarte de en qué punto del año vas a abrir.')

    C.parrafo(ws, G_NOTA,
              'LAS DURACIONES SON SUPUESTOS y casi todas dependen de un '
              'tercero. Cámbialas por las tuyas en cuanto tengas un plazo por '
              'escrito, empezando por el del equipamiento: es el que más '
              'silenciosamente mueve la fecha de apertura, porque no falla, '
              'sólo llega tarde. La hoja no usa funciones de fecha a propósito: '
              'trabaja en meses decimales, así que medio mes es 0,5 y se puede '
              'sumar sin discutir con el calendario laboral.', 'A', 'Q',
              alto=56)
    C.parrafo(ws, G_NOTA + 1,
              'Y lo que NO está aquí: qué trámite pide tu ayuntamiento. No se '
              'ha abierto ninguna ordenanza municipal para este producto, así '
              'que afirmarlo sería inventárselo. Lo que sí está verificado, y '
              'es lo que de verdad te protege, es que ningún ayuntamiento puede '
              'exigirte licencia PREVIA de actividad hasta 750 metros '
              'cuadrados.', 'A', 'Q', alto=48)
    ws.freeze_panes = 'C%d' % (G_CAB + 1)
    C.pagina(ws, titulos='$%d:$%d' % (G_CAB, G_CAB),
             area='A1:Q%d' % fila_listas)
    return ws


# ==========================================================================
# Mapa de celdas citables
# ==========================================================================
def mapa_celdas():
    m = [
        ('Trámites del expediente', H_CHK, 'D%d' % K_TOTAL, 'salida'),
        ('Trámites hechos', H_CHK, 'D%d' % K_HECHOS, 'salida'),
        ('Trámites que no te aplican', H_CHK, 'D%d' % K_NA, 'salida'),
        ('Avance del expediente', H_CHK, 'D%d' % K_AVANCE, 'salida'),
        ('Coste previsto total del checklist', H_CHK, 'D%d' % K_PREV,
         'salida'),
        ('Coste real total del checklist', H_CHK, 'D%d' % K_REAL, 'salida'),
        ('Desviación del coste del checklist', H_CHK, 'D%d' % K_DESV,
         'salida'),
        ('Trámites sin importe (a presupuestar)', H_CHK, 'D%d' % K_SINIMP,
         'salida'),
        ('Trámites que cambian según la comunidad autónoma', H_CHK,
         'D%d' % K_CCAA_N, 'salida'),
        ('Comunidad autónoma del ejemplo', H_CHK, 'D%d' % K_TU_CCAA,
         'entrada'),
        ('¿Vas a inscribirte como artesano alimentario?', H_CHK,
         'D%d' % K_ARTES, 'entrada'),
        ('Canales por los que vas a vender', H_CHK, 'C%d' % K_CAN_USO,
         'salida'),
        ('Canales que SÍ te sacan de la nota del 644.5', H_CHK,
         'C%d' % K_CAN_FUERA, 'salida'),
        ('Canales sin resolver, pendientes del asesor', H_CHK,
         'C%d' % K_CAN_NOSE, 'salida'),
        ('VEREDICTO DE LOS CANALES', H_CHK, 'C%d' % K_CAN_VER, 'salida'),
        ('La pregunta redactada para el asesor, canal del mostrador', H_CHK,
         'F%d' % K_CAN_INI, 'salida'),
        ('Avance de la fase F1', H_CHK, 'J%d' % FASES[0][5], 'salida'),
        ('Trámites de la fase F5', H_CHK, 'E%d' % FASES[4][5], 'salida'),
        ('Tu régimen sanitario', H_ARB, 'B%d' % A['regimen'], 'salida'),
        ('El trámite sanitario que te toca', H_ARB, 'B%d' % A['tramite'],
         'salida'),
        ('¿La comunicación autonómica habilita para abrir?', H_ARB,
         'B%d' % A['habilita'], 'salida'),
        ('¿Suministras a otros minoristas de distinta titularidad?', H_ARB,
         'B%d' % A['b2b'], 'entrada'),
        ('¿Tienes obrador propio?', H_ARB, 'B%d' % A['obrador'], 'entrada'),
        ('Puerta de entrada del art. 3', H_SUM, 'B%d' % U['puerta'],
         'entrada'),
        ('Lectura de la puerta de entrada del art. 3', H_SUM,
         'B%d' % U['aviso_puerta'], 'salida'),
        ('Umbral de la vía a) del art. 3 (% del volumen anual)', H_SUM,
         'B%d' % U['umbral_a'], 'parametro'),
        ('Umbral de la vía b) del art. 3 (kg a la semana)', H_SUM,
         'B%d' % U['umbral_b'], 'parametro'),
        ('Kilos a la semana a otros minoristas', H_SUM, 'B%d' % U['total_kg'],
         'salida'),
        ('¿Cumples la vía a)?', H_SUM, 'B%d' % U['via_a'], 'salida'),
        ('¿Cumples la vía b)?', H_SUM, 'B%d' % U['via_b'], 'salida'),
        ('¿ES MARGINAL?', H_SUM, 'B%d' % U['marginal'], 'salida'),
        ('¿ES LOCALIZADO?', H_SUM, 'B%d' % U['localizado'], 'salida'),
        ('¿ES RESTRINGIDO?', H_SUM, 'B%d' % U['restringido'], 'salida'),
        ('Condiciones del art. 3 cumplidas', H_SUM, 'B%d' % U['cumplidas'],
         'salida'),
        ('VEREDICTO DEL ART. 3', H_SUM, 'B%d' % U['veredicto'], 'salida'),
        ('¿Tu comunidad ha ampliado la lista por la letra e)?', H_DOM,
         'B%d' % M['amplia'], 'entrada'),
        ('Lectura de la letra e)', H_DOM, 'B%d' % M['aviso'], 'salida'),
        ('Tope absoluto del art. 13.9 (kg a la semana)', H_DOM,
         'B%d' % M['tope'], 'parametro'),
        ('Kilos por metro cuadrado de la ruta doméstica', H_DOM,
         'B%d' % M['prop'], 'salida'),
        ('Requisito 1 del art. 13.9 (tope de kilos)', H_DOM,
         'B%d' % M['sem_tope'], 'salida'),
        ('Requisito 2 del art. 13.9 (proporcionalidad)', H_DOM,
         'B%d' % M['sem_prop'], 'salida'),
        ('Requisito 3 del art. 13.9 (demostrable documentalmente)', H_DOM,
         'B%d' % M['sem_dem'], 'salida'),
        ('VEREDICTO DE LA RUTA DOMÉSTICA', H_DOM, 'B%d' % M['veredicto'],
         'salida'),
        ('¿Importas grano de cacao?', H_CAD, 'B%d' % CA['grano'], 'entrada'),
        ('Analíticas propias al año', H_CAD, 'B%d' % CA['analiticas'],
         'salida'),
        ('Coste anual de analíticas', H_CAD, 'B%d' % CA['coste_anio'],
         'salida'),
        ('Lotes cubiertos por tus analíticas', H_CAD, 'B%d' % CA['pct'],
         'salida'),
        ('VEREDICTO DEL CADMIO', H_CAD, 'B%d' % CA['veredicto'], 'salida'),
        ('Lo que la norma de contaminantes SÍ te obliga a hacer', H_CAD,
         'B%d' % CA['obligacion'], 'salida'),
        ('¿El bombón tiene límite propio de cadmio?', H_CAD,
         'B%d' % (CA['que_ini'] + 2), 'salida'),
        ('Fecha de verificación legal del EUDR', H_EUDR,
         'B%d' % E['verificado'], 'parametro'),
        ('Fecha en la que toca volver a revisar el EUDR', H_EUDR,
         'B%d' % E['sem_rev'], 'salida'),
        ('De dónde viene tu cacao', H_EUDR, 'B%d' % E['origen'], 'entrada'),
        ('¿Tu cobertura llega amparada por una DDS?', H_EUDR,
         'B%d' % E['amparada'], 'entrada'),
        # B12 (refutación 2026-09-12): con la siembra honesta «No lo sé» en
        # `amparada`, estas tres salen «Sin resolver...» de fábrica. Antes se
        # llamaban «TU PAPEL EN LA CADENA EUDR» y podían citarse como si
        # fueran la conclusión del caso «La Almendra»; ahora el nombre dice
        # lo que de verdad son: el estado ANTES de que el lector conteste.
        ('Estado de la hoja EUDR antes de que rellenes tu papel', H_EUDR,
         'B%d' % E['papel'], 'salida'),
        ('La fecha del EUDR que te corre (una vez resuelto tu papel)', H_EUDR,
         'B%d' % E['fecha'], 'salida'),
        ('La documentación EUDR que te toca (una vez resuelto tu papel)',
         H_EUDR, 'B%d' % E['docu'], 'salida'),
        ('El aviso de inferencia declarada del EUDR', H_EUDR,
         'B%d' % E['inferencia'], 'salida'),
        ('Personas con formación registrada', H_FOR, 'C%d' % R_CON, 'salida'),
        ('Formaciones caducadas', H_FOR, 'C%d' % R_CADUCADAS, 'salida'),
        ('Validez de la formación en meses', H_FOR, 'C%d' % R_VALIDEZ,
         'parametro'),
        ('VEREDICTO DEL REGISTRO DE FORMACIÓN', H_FOR, 'C%d' % R_VER,
         'salida'),
        ('Mes en que arranca el proyecto', H_GAN, 'C%d' % G_ARRANQUE,
         'entrada'),
        ('Duración total del proyecto (meses)', H_GAN, 'C%d' % G_DURACION,
         'salida'),
        ('Hitos sin holgura (ruta crítica)', H_GAN, 'C%d' % G_CRITICOS,
         'salida'),
        ('Mes natural en el que abres', H_GAN, 'C%d' % G_MES_AP, 'salida'),
        ('Nombre del mes de apertura', H_GAN, 'C%d' % G_NOMBRE_MES, 'salida'),
        ('Temporada del mes de apertura', H_GAN, 'C%d' % G_TEMPORADA,
         'salida'),
        ('Aviso sobre el mes de apertura', H_GAN, 'C%d' % G_AVISO, 'salida'),
        ('Plazo crítico de maquinaria traído del libro 9 (celda verde del '
         'cruce)', H_GAN, 'C%d' % G_CRU_VERDE, 'entrada'),
        ('Ese plazo, en meses', H_GAN, 'C%d' % G_CRU_MESES, 'salida'),
        ('Margen entre la ruta crítica y el plazo de maquinaria', H_GAN,
         'C%d' % G_CRU_DIF, 'salida'),
        ('CUADRE de quién manda la fecha de apertura', H_GAN,
         'C%d' % G_CRU_CUADRE, 'salida'),
        ('Duración del hito de búsqueda de local', H_GAN, 'C%d' % G_INI,
         'entrada'),
        ('Mes en que acaba el pedido de equipamiento', H_GAN,
         'K%d' % (G_INI + 5), 'salida'),
    ]
    return m


NOTAS_MAPA = (
    'Libro 8 de la guía. La hoja «' + H_CHK + '» NO emite un epígrafe de IAE '
    'por canal, y no es una omisión: ninguna fuente lo da. Lo que publica es la '
    'nota literal del 644.5, la respuesta sí/no/no lo sé por canal y LA '
    'PREGUNTA REDACTADA PARA EL ASESOR. Está prohibido escribir «con el 644.5 '
    'puedes vender a hostelería, a empresas y por envío sin más». La ruta '
    'doméstica empieza por la letra e) del art. 13.8 y los TRES requisitos del '
    'art. 13.9 (`PA-29c`, reutilizado de Pastelería y verificado el 10-09-2026) '
    'sólo se activan si la comunidad ha ampliado la lista: para el bombón la '
    'ruta no está abierta por defecto. El bombón NO tiene límite propio de '
    'cadmio (`CHN-84`): la nota (14) del Anexo I del Rgto. 2023/915 remite sólo '
    'a los puntos 2, 3 y 4 de la Directiva 2000/36/CE (`CHN-16b`). El paso «una '
    'chocolatería que compra cobertura es operador posterior, así que el '
    'aplazamiento del art. 38.3 no le alcanza» es INFERENCIA DECLARADA, con el '
    'art. 2.15 ter como condición, y la hoja del EUDR lleva su fecha de '
    'revisión dentro (D5). El plazo de entrega de maquinaria llega del libro 9 '
    'por celda verde con fila de cuadre: cero fórmulas que nombren otro '
    'fichero.')


# ==========================================================================
# Demostraciones con pycel
# ==========================================================================
def demo(ruta):
    from pycel import ExcelCompiler
    ok, fallos = [], []

    def prueba(nombre, cond, detalle=''):
        (ok if cond else fallos).append(
            nombre + (' — ' + detalle if detalle else ''))

    exc = ExcelCompiler(ruta)

    def v(hoja, coord):
        return exc.evaluate("'%s'!%s" % (hoja, coord))

    # 1. La ruta crítica y el mes de apertura coinciden con el juego de datos.
    total = v(H_GAN, 'C%d' % G_DURACION)
    esperado, _c, _h = D.ruta_critica()
    prueba('la duración total del proyecto coincide con la ruta crítica del '
           'juego de datos', abs(total - esperado) < 0.001,
           '%r frente a %r meses' % (total, esperado))
    mes = v(H_GAN, 'C%d' % G_MES_AP)
    prueba('el mes de apertura calculado es el del juego de datos',
           int(mes) == D.mes_apertura_calculado(),
           '%r frente a %r' % (mes, D.mes_apertura_calculado()))

    # 2. El cruce 8 <- 9: con el plazo por defecto manda el papeleo; al subirlo,
    #    manda la maquinaria.
    cuadre = v(H_GAN, 'C%d' % G_CRU_CUADRE)
    prueba('con el plazo por defecto, la fecha la manda el papeleo',
           cuadre.startswith('CUADRA'), '%r' % (cuadre,))
    exc_b = ExcelCompiler(ruta)
    exc_b.evaluate("'%s'!C%d" % (H_GAN, G_CRU_CUADRE))
    exc_b.set_value("'%s'!C%d" % (H_GAN, G_CRU_VERDE), 52)
    prueba('con un plazo de 52 semanas, la fecha la manda la maquinaria',
           exc_b.evaluate("'%s'!C%d" % (H_GAN, G_CRU_CUADRE))
           .startswith('LA MANDA LA MAQUINARIA'))

    # 3. D21: los tres requisitos del art. 13.9 NO se activan si la comunidad
    #    no ha abierto la letra e).
    t1 = v(H_DOM, 'B%d' % M['sem_tope'])
    ver = v(H_DOM, 'B%d' % M['veredicto'])
    prueba('con la letra e) sin abrir, los requisitos del art. 13.9 dicen «no '
           'procede» y el veredicto no da la ruta por buena',
           'No procede' in t1 and 'no está abierta' in ver,
           '%r / %r' % (t1, ver))
    exc_c = ExcelCompiler(ruta)
    exc_c.evaluate("'%s'!B%d" % (H_DOM, M['sem_tope']))
    exc_c.evaluate("'%s'!B%d" % (H_DOM, M['veredicto']))
    exc_c.set_value("'%s'!B%d" % (H_DOM, M['amplia']), SI)
    prueba('al abrir la letra e), el tope de 100 kg empieza a evaluarse de '
           'verdad', exc_c.evaluate("'%s'!B%d" % (H_DOM, M['sem_tope'])) == SI,
           '%r' % (exc_c.evaluate("'%s'!B%d" % (H_DOM, M['sem_tope'])),))

    # 4. D19: los canales. Con sólo el mostrador no hay nada que preguntar; al
    #    encender el B2B aparece la pregunta para el asesor.
    ver_can = v(H_CHK, 'C%d' % K_CAN_VER)
    prueba('vendiendo sólo por mostrador, todos los canales caben en la nota '
           'del 644.5', 'caben en la nota' in ver_can, '%r' % (ver_can,))
    exc_d = ExcelCompiler(ruta)
    exc_d.evaluate("'%s'!C%d" % (H_CHK, K_CAN_VER))
    exc_d.set_value("'%s'!C%d" % (H_CHK, K_CAN_INI + 2), SI)
    ver_d = exc_d.evaluate("'%s'!C%d" % (H_CHK, K_CAN_VER))
    prueba('al encender el B2B a hostelería, la hoja te manda al asesor con la '
           'pregunta escrita', 'asesor fiscal' in ver_d, '%r' % (ver_d,))

    # 5. El árbol del art. 3: la puerta de entrada corta la hoja entera.
    # B2 (refutación 2026-09-12): el valor de PARTIDA ya no es «No» a mano:
    # se deriva de `D.CLIENTES_B2B`, y «La Almendra» SÍ tiene un minorista
    # de distinta titularidad -está tres filas más abajo en esta misma
    # hoja-, así que hoy la puerta está abierta y las tres condiciones se
    # cumplen. El caso «puerta cerrada» se prueba aparte, tocando la entrada.
    ver3 = v(H_SUM, 'B%d' % U['veredicto'])
    prueba('con el destinatario de "La Almendra", el art. 3 SÍ aplica y las '
           'tres condiciones se cumplen',
           'Cumples las tres' in ver3, '%r' % (ver3,))
    exc_p = ExcelCompiler(ruta)
    exc_p.evaluate("'%s'!B%d" % (H_SUM, U['veredicto']))
    exc_p.set_value("'%s'!B%d" % (H_SUM, U['puerta']), NO)
    ver3_sin = exc_p.evaluate("'%s'!B%d" % (H_SUM, U['veredicto']))
    prueba('sin suministro a otros minoristas, el art. 3 no aplica',
           'no te aplica' in ver3_sin, '%r' % (ver3_sin,))
    exc_e = ExcelCompiler(ruta)
    exc_e.evaluate("'%s'!B%d" % (H_SUM, U['veredicto']))
    exc_e.evaluate("'%s'!B%d" % (H_SUM, U['restringido']))
    exc_e.set_value("'%s'!B%d" % (H_SUM, U['puerta']), SI)
    exc_e.set_value("'%s'!E%d" % (H_SUM, U['ini']), SI)
    ver3b = exc_e.evaluate("'%s'!B%d" % (H_SUM, U['veredicto']))
    prueba('con un destinatario inscrito en el RGSEAA se pierde «restringido» '
           'y el veredicto manda al registro estatal',
           'RGSEAA' in ver3b and 'falla' in ver3b, '%r' % (ver3b,))

    # 6. El EUDR: operador posterior por defecto; al importar grano, operador.
    papel = v(H_EUDR, 'B%d' % E['papel'])
    prueba('sin confirmar que la cobertura está amparada, el papel EUDR queda '
           'SIN RESOLVER y no se afirma una fecha automática',
           'Sin resolver' in papel, '%r' % (papel,))
    exc_f = ExcelCompiler(ruta)
    exc_f.evaluate("'%s'!B%d" % (H_EUDR, E['papel']))
    exc_f.set_value("'%s'!B%d" % (H_EUDR, E['origen']), ORIGENES[1])
    papel_f = exc_f.evaluate("'%s'!B%d" % (H_EUDR, E['papel']))
    prueba('al importar grano, el papel pasa a OPERADOR',
           papel_f.startswith('OPERADOR:'), '%r' % (papel_f,))

    # 7. El contador del checklist y su porcentaje de avance.
    total_t = v(H_CHK, 'D%d' % K_TOTAL)
    prueba('el checklist cuenta los treinta y tres trámites',
           int(total_t) == len(D.CHECKLIST_LEGAL), '%r' % (total_t,))
    avance = v(H_CHK, 'D%d' % K_AVANCE)
    prueba('con todo pendiente, el avance del expediente es cero',
           avance == 0, '%r' % (avance,))

    return ok, fallos


# ==========================================================================
def main():
    D.gate_legal(IDS_LEGALES)
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_checklist(wb)
    hoja_arbol(wb)
    hoja_suministro(wb)
    hoja_domestica(wb)
    hoja_cadmio(wb)
    hoja_eudr(wb)
    hoja_formacion(wb)
    hoja_gantt(wb)

    res = X.cerrar(wb, NOMBRE, TITULO, mapa_celdas(), NOTAS_MAPA)

    print('escrito: %s' % res['ruta'])
    print('hojas: %d · fórmulas: %d · celdas verdes: %d · verdes vacías: %d'
          % (res['hojas'], res['formulas'], res['verdes'],
             len(res['verdes_vacias'])))
    print('fórmulas que devuelven «sin dato» a propósito: %d' % res['sin_dato'])
    print('notas legales: %d · notas de fuente sectorial: %d · etiquetas en el '
          'mapa: %d · cruces con fila de cuadre: %d'
          % (res['notas_legales'], res['notas_sector'], res['mapa'],
             res['cruces']))
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
