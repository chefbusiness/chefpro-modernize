#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_checklist-equipamiento-y-proveedores-cacao.py — libro 9 de «Cómo Montar una
Chocolatería» (SPEC §2.2, fila 9; constructor C5).

Hojas: Instrucciones · Equipamiento · Variante del Formato · Proveedores y
EUDR · Clientes a los que Suministras · Contador.

QUÉ DECIDE ESTE LIBRO
---------------------
Qué compras, a quién, a qué precio real, con qué plazo, con qué papeles — y a
quién le vendes. Molde B del libro 7 de Pastelería
(`gen_checklist-equipamiento-y-proveedores.py`, 1.589 líneas) con **dos
columnas que Pastelería no necesita** (EUDR y cadmio/HAP) y **una tabla entera
que no existe en ningún libro del catálogo**: la de CLIENTES.

LAS TRES COSAS QUE ESTE LIBRO HACE Y NINGÚN CHECKLIST DEL MERCADO HACE
----------------------------------------------------------------------
1. **La base fiscal de cada precio** (regla 3 de §2.3, ampliada por A-2). Seis
   de las diecisiete líneas traen «no declarada» porque el distribuidor no lo
   dice: se tratan como base imponible y **se marcan**, que es lo honesto.
   Mezclarlas desvía la inversión un 21 %.
2. **El plazo de entrega**, que es lo que de verdad mueve la fecha de apertura,
   y por eso **viaja al libro 8** (séptimo cruce de §2.3, `CRUCES[6]`): este
   libro publica en `build/mapa-…json` la celda del plazo crítico, y el
   cronograma del 8 la trae por celda verde con su fila de CUADRE.
3. **D48, y son DOS tablas y un ÁRBOL, no una columna con semáforo.**
   (a) El art. 5.3.a) del EUDR (`CHN-24`) obliga a guardar los datos del
   proveedor SIEMPRE, pero los números de referencia de las declaraciones de
   diligencia debida **«únicamente en el caso de que su proveedor sea un
   operador»**. Un semáforo que se lo pidiera a todos SUSPENDERÍA a proveedores
   que cumplen: por eso hay un árbol de tres ramas y el nº de DDS sólo se exige
   en la primera. (b) La mitad b) del mismo artículo obliga a registrar a quien
   TÚ suministras: ésa es la segunda tabla, la de clientes, que se conserva
   **cinco años**.

EL CRUCE QUE RECIBE (D32): 9 <- 2
---------------------------------
La desviación contra el CAPEX del libro 2 llega por **celda verde** «trae aquí
la cifra de `calculadora-capex-chocolateria.xlsx!CAPEX por Bloque`», con su
valor por defecto declarado, **más una fila de CUADRE con semáforo**. Cero
fórmulas que nombren otro fichero: un vínculo entre ficheros se rompe en cuanto
alguien mueve una carpeta, y entonces el libro miente sin avisar.

DECISIONES TÉCNICAS
-------------------
* Cero constantes dentro de las fórmulas: el tipo de IVA, la horquilla, el
  umbral de desviación, las semanas hasta la apertura, el margen de seguridad y
  los años de conservación del registro viven en celdas de parámetros.
* `MAX` no admite condición sin fórmula matricial: el plazo crítico se calcula
  sobre una columna auxiliar declarada, no con `MAXIFS` (que pycel no evalúa) ni
  con `NETWORKDAYS` (prohibida).
* Estado del checklist en PALABRAS, no en símbolos: `☐`/`✓` no son WinAnsi.
* Prohibidas INDIRECT, COUNTA, PMT, OFFSET, XLOOKUP, LET, LAMBDA, RANK,
  NETWORKDAYS e IRR; `IFERROR(...,"")` en todo cociente; «sin dato» = `""`;
  semáforos con `ISNUMBER`; desplegables contra RANGO.
* Ninguna celda verde vacía: todas nacen con su valor por defecto declarado.

Salida fija: build/checklist-equipamiento-y-proveedores-cacao.xlsx
             + build/mapa-checklist-equipamiento-y-proveedores-cacao.json
Uso: /usr/local/bin/python3 gen_checklist-equipamiento-y-proveedores-cacao.py
Via: Claude Code
"""
import datetime
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import _comun_chocolateria as C                                # noqa: E402
import _comun_libros_8_9 as X                                  # noqa: E402
import datos_ejemplo as D                                      # noqa: E402
import motor                                                   # noqa: E402

NOMBRE = 'checklist-equipamiento-y-proveedores-cacao'
TITULO = 'Checklist de equipamiento y proveedores de cacao'

H_INS = 'Instrucciones'
H_EQ = 'Equipamiento'
H_VAR = 'Variante del Formato'
H_PROV = 'Proveedores y EUDR'
H_CLI = 'Clientes a los que Suministras'
H_CONT = 'Contador'

N = motor.NARROW

# --- vocabularios (en palabras: ☐ y ✓ no son WinAnsi) ---------------------
ESTADOS = ('Pendiente', 'Presupuestado', 'Pedido', 'Recibido', 'Instalado',
           'N/A')
ESTADO_DEFECTO = ESTADOS[0]
ESTADO_FINAL = ESTADOS[4]
PRIORIDADES = ('Crítico', 'Opcional')
BASES_IVA = ('sin IVA', 'con IVA', 'no declarada')
SI, NO, NOSE = 'Sí', 'No', 'No lo sé'
SI_NO = (SI, NO)
SI_NO_NOSE = (SI, NO, NOSE)
PROV_PENDIENTE = 'Pendiente: pide tres presupuestos'
DDS_PENDIENTE = 'Pendiente de pedir'
LIBRE = '(libre: escribe aquí tu cliente)'

# --- parámetros por defecto (todos SUPUESTOS declarados) ------------------
HORQUILLA_DEFECTO = 0.25
UMBRAL_DESVIACION = 0.10
SEMANAS_HASTA_APERTURA = 36
SEMANAS_MARGEN = 3
PEDIDO_MINIMO_DEFECTO = 250.0
PLAZO_PROVEEDOR_DEFECTO = 7
ANOS_CONSERVACION = 5
FECHA_BASE = datetime.date(2026, 9, 12)

EQUIPOS = list(D.EQUIPAMIENTO)
N_EQ = len(EQUIPOS)
BLOQUE_TEMPLADO = 'Equipo de templado y moldeado'

#: Origen del cruce 9 <- 2, leído del mapa que publica C1 (§2.5). El valor por
#: defecto se calcula aquí desde el juego de datos, no se teclea.
CRUCE2_REF = ('calculadora-capex-chocolateria.xlsx!CAPEX por Bloque!L33')
CRUCE2_DEFECTO = round(D.equipamiento_bloque_sin_iva(BLOQUE_TEMPLADO), 2)

#: Ids legales que este libro cita. `gate_legal()` corre antes de escribir una
#: sola nota.
IDS_LEGALES = {
    'CHN-24': D.IDS_LEGALES_REQUERIDOS['CHN-24'],
    'CHN-26': D.IDS_LEGALES_REQUERIDOS['CHN-26'],
    'CHN-25': D.IDS_LEGALES_REQUERIDOS['CHN-25'],
    'CHN-23': D.IDS_LEGALES_REQUERIDOS['CHN-23'],
    'CHN-22': D.IDS_LEGALES_REQUERIDOS['CHN-22'],
    'CHN-21': D.IDS_LEGALES_REQUERIDOS['CHN-21'],
    'CHN-20': D.IDS_LEGALES_REQUERIDOS['CHN-20'],
    'CHN-18': D.IDS_LEGALES_REQUERIDOS['CHN-18'],
    'CHN-16b': D.IDS_LEGALES_REQUERIDOS['CHN-16b'],
    'CHN-41': D.IDS_LEGALES_REQUERIDOS['CHN-41'],
    'CHN-48': D.IDS_LEGALES_REQUERIDOS['CHN-48'],
    'CHN-49c': D.IDS_LEGALES_REQUERIDOS['CHN-49c'],
    'CHN-47b': D.IDS_LEGALES_REQUERIDOS['CHN-47b'],
    'CHN-56': D.IDS_LEGALES_REQUERIDOS['CHN-56'],
    'CHN-61': D.IDS_LEGALES_REQUERIDOS['CHN-61'],
    'CHN-86': D.IDS_LEGALES_REQUERIDOS['CHN-86'],
}


def ie(expr):
    return motor.iferror(expr)


# ==========================================================================
# Filas y columnas de la hoja «Equipamiento»
# ==========================================================================
P_SEC = 5
P_CAB = 6
P_IVA = 7
P_HORQ = 8
P_UMBRAL = 9
P_SEM = 10
P_MARGEN = 11

EQ_SEC = 13
EQ_CAB = 14
EQ_INI = 15
EQ_FIN = EQ_INI + N_EQ - 1

RES_SEC = EQ_FIN + 2
R_LINEAS = RES_SEC + 1
R_REF_CRIT = R_LINEAS + 1
R_REF_TODO = R_LINEAS + 2
R_REAL_CRIT = R_LINEAS + 3
R_REAL_TODO = R_LINEAS + 4
R_NEGOCIA = R_LINEAS + 5
R_IVA_SOP = R_LINEAS + 6
R_DESEMB = R_LINEAS + 7
R_RANGOS = R_LINEAS + 8
R_DESDE = R_LINEAS + 9

CR_SEC = R_DESDE + 2
CR_VERDE = CR_SEC + 1
CR_REAL = CR_SEC + 2
CR_DIF = CR_SEC + 3
CR_PCT = CR_SEC + 4
CR_CUADRE = CR_SEC + 5

PL_SEC = CR_CUADRE + 2
R_PLAZO = PL_SEC + 1
R_PLAZO_LIN = PL_SEC + 2
R_MARGEN = PL_SEC + 3
R_VER_PLAZO = PL_SEC + 4
R_TARDE = PL_SEC + 5

LI_SEC = R_TARDE + 2
LI_CAB = LI_SEC + 1
LI_INI = LI_CAB + 1
LI_FIN = LI_INI + len(ESTADOS) - 1
C_CRIT = '$C$%d' % LI_INI
C_OPC = '$C$%d' % (LI_INI + 1)
C_CONIVA = '$E$%d' % (LI_INI + 1)
EQ_NOTA = LI_FIN + 2
EQ_PIE = EQ_NOTA + 4

COLS_EQ = [
    ('A', 'Estado'), ('B', 'Nº'), ('C', 'Partida'), ('D', 'Marca'),
    ('E', 'Modelo'), ('F', 'Categoría'), ('G', 'Bloque de CAPEX'),
    ('H', 'Prioridad'), ('I', 'Precio de referencia (€)'),
    ('J', '¿Lleva IVA?'), ('K', 'Tipo de IVA (%)'),
    ('L', 'Precio de referencia SIN IVA (€)'),
    ('M', 'Mínimo (€)'), ('N', 'Máximo (€)'),
    ('O', 'Precio real negociado (€, sin IVA)'),
    ('P', 'Desviación sobre la referencia (%)'), ('Q', 'Proveedor'),
    ('R', 'Plazo de entrega (semanas)'),
    ('S', 'Margen hasta la apertura (semanas)'),
    ('T', 'Aux' + N + '· mínimo publicado del rango'),
    ('U', 'Aux' + N + '· máximo publicado del rango'),
    ('V', 'Aux' + N + '· plazo de las líneas críticas'),
    ('W', 'Aux' + N + '· ¿el plazo se pasa? (1 = sí)'),
    ('X', 'Aux' + N + '· real del bloque de templado'),
    ('Y', 'Cómo se publica el precio'), ('Z', 'Fuente del precio'),
    ('AA', 'Nota'),
]

PUB_CERRADO = 'Precio cerrado'
PUB_RANGO = 'RANGO publicado (no es un precio)'
PUB_DESDE = 'DESDE: suelo comercial, presupuestar'
PUB_SUPUESTO = 'SUPUESTO declarado'


# ==========================================================================
# Hoja «Instrucciones»
# ==========================================================================
PASOS = [
    '1. Hoja «Equipamiento»: las diecisiete líneas de la dotación, con su '
    'precio de referencia y SU BASE FISCAL. Marca el estado, escribe el precio '
    'real que negocies (siempre SIN IVA), el proveedor y el plazo que te '
    'comprometan por escrito. La hoja te dice cuánto te desvías de la '
    'referencia, qué línea marca el plazo crítico y si llegas a la apertura.',
    '2. Hoja «Variante del Formato»: si te planteas bean-to-bar o chocolatería '
    'de taza y churros. El bean-to-bar va SIN CIFRAS DE MAQUINARIA a propósito '
    '-no existe precio público verificado-: lo que hay es la lista de la compra '
    'y las cinco preguntas que hay que hacerle al fabricante, con casilla para '
    'apuntar quién te ha contestado.',
    '3. Hoja «Proveedores y EUDR»: los seis proveedores con URL comprobada, y '
    'el árbol que decide qué papeles le tocan a cada uno. Pregúntale a cada '
    'proveedor si es operador, operador posterior o comerciante: el número de '
    'referencia de su declaración de diligencia debida SÓLO se le pide al '
    'primero. Y en las dos últimas columnas, los boletines de cadmio y de HAP.',
    '4. Hoja «Clientes a los que Suministras»: la otra mitad del mismo '
    'artículo, la que casi nadie conoce. Si vendes a hostelería, a empresas o a '
    'otra tienda, tienes que registrar a quién le has vendido qué, y conservar '
    'ese registro cinco años. La hoja calcula la fecha hasta la que hay que '
    'guardarlo.',
    '5. Hoja «Contador»: el avance de la compra en una pantalla, con el '
    'presupuesto, lo que llevas gastado y cuántos papeles te faltan.',
]

NOTAS_LIBRO = [
    'LA COLUMNA QUE NO TRAE NINGÚN CHECKLIST DEL MERCADO ES «¿LLEVA IVA?». '
    'Seis de las diecisiete líneas vienen de fichas de distribuidor que NO '
    'declaran su base fiscal: aquí se tratan como base imponible y se marcan '
    'como «no declarada», que es lo honesto. Si mezclas precios con IVA y sin '
    'IVA en la misma columna, tu inversión sale un 21' + N + '% desviada y no '
    'lo ves hasta que llega la primera factura.',
    'LOS PLAZOS DE ENTREGA SON SUPUESTOS: ningún distribuidor los publica. '
    'Sustitúyelos por el que te comprometan POR ESCRITO en el presupuesto. Son '
    'la columna que de verdad mueve la fecha de apertura, y por eso el '
    'cronograma del libro «checklist-legal-licencias-y-cacao» te pide que '
    'traigas aquí el plazo crítico y te avisa si tu ruta crítica es más corta '
    'que él.',
    'NO SE PUBLICAN LOS PROVEEDORES SIN VERIFICAR. El research recogió muchos '
    'más; aquí entran los seis con URL comprobada el 12 de septiembre de 2026. '
    'Un directorio con un enlace roto vale menos que uno corto.',
    'EL NÚMERO DE LA DDS NO SE LE PIDE A TODO EL MUNDO. El art. 5.3.a) del '
    'reglamento de deforestación obliga a guardar los datos de todos tus '
    'proveedores, pero los números de referencia de las declaraciones de '
    'diligencia debida «únicamente en el caso de que su proveedor sea un '
    'operador». Pedírselo a un comerciante es pedirle algo que no tiene.',
    'Y LA OTRA MITAD DEL ARTÍCULO OBLIGA A REGISTRAR A TUS CLIENTES. El mismo '
    '5.3, letra b), habla de los operadores posteriores y comerciantes «a los '
    'que hayan suministrado los productos pertinentes». Si sirves a la '
    'cafetería de al lado, a una empresa o a una tienda gourmet, esa tabla te '
    'toca. Se conserva cinco años.',
    'ESTE LIBRO NO CALCULA TU INVERSIÓN. Eso lo hace '
    '«calculadora-capex-chocolateria.xlsx». Aquí el CAPEX del libro 2 entra '
    'como CELDA VERDE que tú copias, con su valor por defecto declarado: en '
    'toda la guía no hay una sola fórmula que apunte a otro fichero.',
]

FRONTERA = [
    ('kit-tareas-chocolateria (12' + N + '€)',
     'Las curvas de templado, las fichas de moldeado y el calendario anual de '
     'campañas, ya construidos.',
     'Este libro decide el obrador que vas a COMPRAR; el kit organiza el que '
     'ya tienes montado. Ninguna de sus once plantillas sustituye a esta hoja.'),
    ('calculadora-capex-chocolateria.xlsx (libro 2 de esta guía)',
     'Los euros de la apertura ordenados en nueve bloques, con su IVA '
     'soportado y su calendario de tesorería.',
     'Aquí se anota lo que de verdad pagas, línea a línea, y se compara con lo '
     'que aquel libro presupuestó. La comparación viaja por celda verde, nunca '
     'por fórmula entre ficheros.'),
    ('checklist-legal-licencias-y-cacao.xlsx (libro 8 de esta guía)',
     'El expediente legal, el árbol del EUDR completo y el cronograma de '
     'apertura con su ruta crítica.',
     'Aquí sólo se resuelve el papel EUDR de cada PROVEEDOR y el registro de '
     'tus CLIENTES. Tu propio papel en la cadena lo decide el libro 8.'),
    ('sensibilidad-al-precio-del-cacao.xlsx (libro 3 de esta guía)',
     'El precio de la cobertura y qué pasa cuando el cacao sube.',
     'Este libro compra MÁQUINAS, no materia prima. El pedido mínimo de cada '
     'proveedor sí está aquí, porque es dinero parado en el almacén.'),
]


def hoja_instrucciones(wb):
    ws = wb.create_sheet(H_INS, 0)
    C.anchos(ws, {'A': 44, 'B': 44, 'C': 44})
    motor.val(ws, 'A1', TITULO)
    ws['A1'].font = Font(bold=True, size=16, color=C.ORO)
    ws.row_dimensions[1].height = 26
    motor.val(ws, 'A2', C.SUBTITULO)
    ws['A2'].font = Font(size=9)
    motor.val(ws, 'A3', 'Para qué sirve: saber qué compras, a quién, a qué '
                        'precio real, con qué plazo, con qué papeles — y a '
                        'quién le vendes.')
    ws['A3'].font = Font(italic=True, size=9)

    fila = 5
    C.seccion(ws, 'A%d' % fila, 'Instrucciones de uso')
    fila += 1
    for paso in PASOS:
        C.parrafo(ws, fila, paso, 'A', 'C', alto=64)
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, C.NOTA_VERDES)
    ws['A%d' % fila].fill = PatternFill('solid', fgColor=motor.VERDE)
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Lo que conviene saber antes de empezar')
    fila += 1
    for texto in NOTAS_LIBRO:
        C.parrafo(ws, fila, texto, 'A', 'C', alto=76)
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
        ws.row_dimensions[fila].height = 64
        fila += 1
    fila += 1

    C.seccion(ws, 'A%d' % fila, 'Cada cuánto se usa este libro')
    fila += 1
    C.parrafo(ws, fila,
              'Cadencia: la hoja «Equipamiento», UNA VEZ A LA SEMANA desde que '
              'pides el primer presupuesto hasta que se instala la última '
              'máquina. La de proveedores, cada vez que des de alta a uno '
              'nuevo, y entera una vez al año para refrescar los papeles del '
              'EUDR. La de clientes, CADA VEZ QUE SIRVAS A UNO NUEVO: es un '
              'registro, no un listado comercial, y se conserva cinco años.',
              'A', 'C', alto=76)
    fila += 2
    C.parrafo(ws, fila,
              'Frontera con el Kit de Tareas Chocolatería (12' + N + '€): si '
              'ya lo tienes, sus plantillas organizan el obrador montado. Este '
              'libro es el de la COMPRA, y no repite ninguna de ellas.',
              'A', 'C', alto=40)
    fila += 2
    C.parrafo(ws, fila, C.NOTA_DESPROTEGER, 'A', 'C', alto=28)
    fila += 2
    C.pie(ws, fila, 'A', 'C')
    C.pagina(ws, apaisado=False, area='A1:C%d' % (fila + 2))
    return ws


# ==========================================================================
# Hoja «Equipamiento»
# ==========================================================================
def _como_se_publica(eq):
    if eq['rango_min'] is not None:
        return PUB_RANGO
    if eq['es_desde']:
        return PUB_DESDE
    if eq['valor_verificado'] is None:
        return PUB_SUPUESTO
    return PUB_CERRADO


def hoja_equipamiento(wb):
    ws = wb.create_sheet(H_EQ)
    C.anchos(ws, {'A': 15, 'B': 5, 'C': 46, 'D': 13, 'E': 24, 'F': 12,
                  'G': 26, 'H': 11, 'I': 15, 'J': 13, 'K': 11, 'L': 16,
                  'M': 13, 'N': 13, 'O': 17, 'P': 13, 'Q': 26, 'R': 12,
                  'S': 14, 'T': 13, 'U': 13, 'V': 13, 'W': 13, 'X': 14,
                  'Y': 28, 'Z': 22, 'AA': 78})
    C.encabezar(ws, 'Equipamiento, línea a línea', col_fin='AA',
                nota_txt='Diecisiete líneas. Los precios con id `CHS-*` salen '
                         'de fichas de distribuidor leídas el 12-09-2026; el '
                         'resto son supuestos declarados. Cada uno con SU base '
                         'fiscal: mezclarlas desvía la inversión un 21'
                         + N + '%.')

    # --- parámetros -------------------------------------------------------
    C.seccion(ws, 'A%d' % P_SEC, 'Parámetros de esta hoja')
    C.cabecera(ws, P_CAB, [('A', 'Parámetro'), ('C', 'Valor'), ('D', 'Nota')],
               altura=20)
    ws.merge_cells('A%d:B%d' % (P_CAB, P_CAB))
    ws.merge_cells('D%d:AA%d' % (P_CAB, P_CAB))

    def par(fila, etiqueta, valor, fmt, nota):
        ws.merge_cells('A%d:B%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, etiqueta, bold=True)
        X.entrada(ws, 'C%d' % fila, valor, fmt=fmt, etiqueta=etiqueta)
        ws.merge_cells('D%d:AA%d' % (fila, fila))
        motor.val(ws, 'D%d' % fila, nota, wrap=True)
        ws['D%d' % fila].font = Font(italic=True, size=9)
        ws.row_dimensions[fila].height = 26

    par(P_IVA, 'Tipo de IVA general (%)', D.P('iva_general'), C.FMT_PCT,
        'La maquinaria, el mobiliario y el packaging van al tipo general: no '
        'hay tipo reducido para el equipamiento de un obrador. Cámbialo aquí y '
        'se recalcula toda la columna K.')
    par(P_HORQ, 'Horquilla del precio de referencia (' + chr(177) + '%)',
        HORQUILLA_DEFECTO, C.FMT_PCT,
        'SUPUESTO. Con cuánta amplitud quieres ver el mínimo y el máximo '
        'alrededor del precio de referencia. El 25' + N + '% es la banda entre '
        'lo que pide una ficha web y lo que se cierra con tres presupuestos. '
        'Las líneas que se publican COMO RANGO no la usan: llevan el suyo.')
    par(P_UMBRAL, 'Umbral de desviación admitida (%)', UMBRAL_DESVIACION,
        C.FMT_PCT,
        'SUPUESTO. Por encima de esta desviación contra el CAPEX del libro 2, '
        'la fila de CUADRE se pone en rojo: o has comprado de más, o el plan '
        'financiero está calculado con una inversión que ya no es la tuya.')
    par(P_SEM, 'Semanas que faltan hasta la apertura prevista',
        SEMANAS_HASTA_APERTURA, C.FMT_ENT,
        'SUPUESTO. Cuenta desde hoy hasta la fecha que tienes en la cabeza. El '
        'cronograma completo, con la ruta crítica del papeleo y de la obra, lo '
        'calcula la hoja «Cronograma y Ruta Crítica» del libro 8.')
    par(P_MARGEN, 'Margen de seguridad entre la entrega y la apertura '
                  '(semanas)', SEMANAS_MARGEN, C.FMT_ENT,
        'SUPUESTO. Lo que necesitas entre que llega la máquina y que abres: '
        'montaje, conexión, puesta en marcha y las pruebas de templado. Con '
        'menos de dos semanas, el primer ajuste de curva te pilla con la '
        'tienda abierta.')

    # --- la tabla ---------------------------------------------------------
    C.seccion(ws, 'A%d' % EQ_SEC, 'La dotación completa, línea a línea')
    C.cabecera(ws, EQ_CAB, COLS_EQ, altura=50)
    v_estado, v_precio, v_prov, v_plazo = [], [], [], []
    for i, eq in enumerate(EQUIPOS):
        r = EQ_INI + i
        prioridad = PRIORIDADES[1] if eq['opcional'] else PRIORIDADES[0]
        ref = eq['valor_verificado'] if eq['valor_verificado'] is not None \
            else eq['supuesto_por_defecto']
        sin_iva = round(D.precio_equipamiento_sin_iva(eq), 2)
        X.entrada(ws, 'A%d' % r, ESTADO_DEFECTO, etiqueta=eq['partida'],
                  align='center')
        v_estado.append('A%d' % r)
        motor.val(ws, 'B%d' % r, eq['n'], fmt=C.FMT_ENT, align='center')
        motor.val(ws, 'C%d' % r, eq['partida'], wrap=True)
        motor.val(ws, 'D%d' % r, eq['marca'] or '')
        motor.val(ws, 'E%d' % r, eq['modelo'] or '')
        motor.val(ws, 'F%d' % r, eq['categoria'])
        motor.val(ws, 'G%d' % r, eq['bloque_capex'])
        motor.val(ws, 'H%d' % r, prioridad, align='center')
        motor.val(ws, 'I%d' % r, ref, fmt=C.FMT_EUR)
        motor.val(ws, 'J%d' % r, eq['base_iva'], align='center')
        motor.f(ws, 'K%d' % r, '=$C$%d' % P_IVA, fmt=C.FMT_PCT)
        motor.f(ws, 'L%d' % r,
                '=IFERROR(IF($I{r}="","",IF($J{r}={ci},$I{r}/(1+$K{r}),'
                '$I{r})),"")'.format(r=r, ci=C_CONIVA), fmt=C.FMT_EUR)
        motor.val(ws, 'T%d' % r, eq['rango_min'] or 0, fmt=C.FMT_EUR)
        motor.val(ws, 'U%d' % r, eq['rango_max'] or 0, fmt=C.FMT_EUR)
        motor.f(ws, 'M%d' % r,
                '=IF($L{r}="","",IF($T{r}>0,$T{r},$L{r}*(1-$C${h})))'
                .format(r=r, h=P_HORQ), fmt=C.FMT_EUR)
        motor.f(ws, 'N%d' % r,
                '=IF($L{r}="","",IF($U{r}>0,$U{r},$L{r}*(1+$C${h})))'
                .format(r=r, h=P_HORQ), fmt=C.FMT_EUR)
        X.entrada(ws, 'O%d' % r, sin_iva, fmt=C.FMT_EUR,
                  etiqueta='Precio real de ' + eq['partida'])
        v_precio.append('O%d' % r)
        motor.f(ws, 'P%d' % r,
                '=IFERROR(IF(OR($O{r}="",$L{r}=""),"",$O{r}/$L{r}-1),"")'
                .format(r=r), fmt=C.FMT_PCT)
        X.entrada(ws, 'Q%d' % r, eq['marca'] or PROV_PENDIENTE,
                  etiqueta='Proveedor de ' + eq['partida'])
        v_prov.append('Q%d' % r)
        X.entrada(ws, 'R%d' % r, eq['plazo_semanas'], fmt=C.FMT_ENT,
                  etiqueta='Plazo de ' + eq['partida'], align='center')
        v_plazo.append('R%d' % r)
        motor.f(ws, 'S%d' % r,
                '=IFERROR(IF(OR($R{r}="",$C${s}="",$C${m}=""),"",'
                '$C${s}-$R{r}-$C${m}),"")'.format(r=r, s=P_SEM, m=P_MARGEN),
                fmt=C.FMT_ENT)
        motor.f(ws, 'V%d' % r, '=IF($H{r}={cr},$R{r},"")'
                .format(r=r, cr=C_CRIT), fmt=C.FMT_ENT)
        motor.f(ws, 'W%d' % r, '=IF($S{r}="","",IF($S{r}<0,1,0))'.format(r=r),
                fmt=C.FMT_ENT)
        motor.f(ws, 'X%d' % r,
                '=IF(AND($G{r}=$G${b},$H{r}={cr}),$O{r},"")'
                .format(r=r, b=EQ_INI, cr=C_CRIT), fmt=C.FMT_EUR)
        motor.val(ws, 'Y%d' % r, _como_se_publica(eq), wrap=True)
        motor.val(ws, 'Z%d' % r, eq['fuente'])
        motor.val(ws, 'AA%d' % r, eq['nota'] or '', wrap=True)
        ws.row_dimensions[r].height = 40
        if eq['fuente'].startswith('CHS-'):
            X.nota_fuente(ws, 'I%d' % r, eq['fuente'].split(' ')[0])
        if eq['n'] == 16:
            X.nota_celda(ws, 'C%d' % r, 'CHN-47b')
        if eq['n'] == 17:
            X.nota_celda(ws, 'C%d' % r, 'CHN-48')
        if eq['n'] == 13:
            X.nota_celda(ws, 'C%d' % r, 'CHN-61')

    # --- resumen ----------------------------------------------------------
    rng = lambda col: '${c}${a}:${c}${b}'.format(c=col, a=EQ_INI, b=EQ_FIN)  # noqa: E731

    def res(fila, etiqueta, formula, fmt=None, nota='', bold=True,
            verde=None, etiq_verde=''):
        ws.merge_cells('A%d:H%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, etiqueta, bold=bold, wrap=True)
        if verde is not None:
            X.entrada(ws, 'I%d' % fila, verde, fmt=fmt, etiqueta=etiq_verde)
        else:
            motor.f(ws, 'I%d' % fila, formula, fmt=fmt, bold=bold)
            ws['I%d' % fila].fill = PatternFill('solid', fgColor=C.CREMA)
        ws.merge_cells('K%d:AA%d' % (fila, fila))
        motor.val(ws, 'K%d' % fila, nota, wrap=True)
        ws['K%d' % fila].font = Font(italic=True, size=9)
        ws.row_dimensions[fila].height = 26
        return 'I%d' % fila

    C.seccion(ws, 'A%d' % RES_SEC, 'Resumen de la compra')
    res(R_LINEAS, 'Líneas del checklist',
        '=COUNTIF(%s,"<>")' % rng('C'), C.FMT_ENT,
        'Las diecisiete líneas de la dotación tipo de una bombonería con '
        'obrador, opcionales incluidas.')
    res(R_REF_CRIT, 'Total de referencia sin IVA, sólo líneas críticas (€)',
        '=SUMPRODUCT(--({h}={cr}),{l})'.format(h=rng('H'), cr=C_CRIT,
                                               l=rng('L')), C.FMT_EUR,
        'Lo que cuesta lo que no puedes dejar de comprar, a precio de '
        'referencia y en base imponible.')
    res(R_REF_TODO, 'Total de referencia sin IVA, todas las líneas (€)',
        '=SUM(%s)' % rng('L'), C.FMT_EUR,
        'Con la atemperadora de arranque, su cubeta y la chocolatera de la '
        'variante de taza dentro, que son opcionales según el formato.')
    res(R_REAL_CRIT, 'Total real negociado sin IVA, sólo líneas críticas (€)',
        '=SUMPRODUCT(--({h}={cr}),{o})'.format(h=rng('H'), cr=C_CRIT,
                                               o=rng('O')), C.FMT_EUR,
        'Lo mismo con TUS precios: es el número que se lleva al libro 2.')
    res(R_REAL_TODO, 'Total real negociado sin IVA, todas las líneas (€)',
        '=SUM(%s)' % rng('O'), C.FMT_EUR,
        'La base imponible de toda tu compra de equipamiento.')
    res(R_NEGOCIA, 'Lo que has ganado (o perdido) negociando (€)',
        ie('$I${a}-$I${b}'.format(a=R_REAL_TODO, b=R_REF_TODO)), C.FMT_EUR,
        'Negativo = has comprado por debajo del precio de referencia. Es el '
        'único sitio del paquete donde se mide lo que vale pedir tres '
        'presupuestos.')
    res(R_IVA_SOP, 'IVA soportado sobre el precio real (€)',
        '=SUMPRODUCT({o},{k})'.format(o=rng('O'), k=rng('K')), C.FMT_EUR,
        'Se recupera vía declaraciones, pero hay que ADELANTARLO el día que '
        'pagas la máquina. La hoja «IVA y Tesorería» del libro 2 dice cuándo '
        'vuelve.')
    res(R_DESEMB, 'Desembolso real con IVA (€)',
        ie('$I${a}+$I${b}'.format(a=R_REAL_TODO, b=R_IVA_SOP)), C.FMT_EUR,
        'Lo que sale de la cuenta corriente.')
    res(R_RANGOS, 'Líneas que sólo pueden publicarse COMO RANGO',
        '=COUNTIF({y},"{p}")'.format(y=rng('Y'), p=PUB_RANGO), C.FMT_ENT,
        'Los moldes de policarbonato: el dato medido es 24,20 a 42,83'
        + N + 'euros por unidad, y elegir un punto dentro de ese rango sería '
        'inventarse un precio. Su mínimo y su máximo van en las columnas T y U '
        'y mandan sobre la horquilla.')
    res(R_DESDE, 'Líneas que son un «desde» y hay que presupuestar',
        '=COUNTIF({y},"{p}")'.format(y=rng('Y'), p=PUB_DESDE), C.FMT_ENT,
        'El mantenedor se publica «desde 570,00' + N + 'euros»: es un suelo '
        'comercial, no el precio de la unidad que vas a comprar. Su techo sólo '
        'puede subir.')

    # --- CRUCE 9 <- 2 -----------------------------------------------------
    C.seccion(ws, 'A%d' % CR_SEC,
              'Cruce con el libro 2: la desviación contra el CAPEX '
              'presupuestado')
    res(CR_VERDE,
        'Trae aquí la base sin IVA del bloque «' + BLOQUE_TEMPLADO + '» de '
        + CRUCE2_REF,
        None, C.FMT_EUR,
        'VALOR POR DEFECTO DECLARADO: el bloque de templado y moldeado de La '
        'Almendra en base imponible, que es lo que suman sus seis líneas '
        'críticas. En cuanto tengas tu libro 2 relleno, copia aquí SU cifra: '
        'no la calcules otra vez. No hay ninguna fórmula que apunte a otro '
        'fichero.', verde=CRUCE2_DEFECTO,
        etiq_verde='CAPEX del bloque de templado traído del libro 2')
    X.CRUCES_VERDES.append((H_EQ, 'I%d' % CR_VERDE,
                            'CAPEX del bloque de templado (9 <- 2)'))
    res(CR_REAL, 'Lo que suman tus líneas críticas de ese mismo bloque (€)',
        ie('SUM(%s)' % rng('X')), C.FMT_EUR,
        'Se calcula sobre la columna auxiliar X, que sólo recoge las líneas '
        'CRÍTICAS cuyo bloque de CAPEX es el de templado y moldeado: comparar '
        'críticas contra críticas es lo único que da una desviación que '
        'significa algo.')
    res(CR_DIF, 'Desviación contra el libro 2 (€)',
        ie('IF($I${v}="","",$I${r}-$I${v})'.format(v=CR_VERDE, r=CR_REAL)),
        C.FMT_EUR,
        'Positivo = estás comprando más caro de lo que había presupuestado el '
        'plan.')
    res(CR_PCT, 'Desviación contra el libro 2 (%)',
        ie('IF($I${v}="","",$I${r}/$I${v}-1)'.format(v=CR_VERDE, r=CR_REAL)),
        C.FMT_PCT,
        'Se compara con el umbral que has fijado arriba.')
    ws.merge_cells('A%d:H%d' % (CR_CUADRE, CR_CUADRE))
    motor.val(ws, 'A%d' % CR_CUADRE, 'CUADRE CONTRA EL CAPEX DEL LIBRO 2',
              bold=True)
    X.cruce_cuadre(
        ws, 'I%d' % CR_CUADRE,
        '=IF($I${p}="","",IF(ABS($I${p})>$C${u},'
        '"NO CUADRA: rehaz el CAPEX del libro 2 con estos precios",'
        '"CUADRA con el CAPEX del libro 2"))'.format(p=CR_PCT, u=P_UMBRAL))
    C.destacado(ws, 'I%d' % CR_CUADRE)
    motor.semaforo_texto(
        ws, 'I%d' % CR_CUADRE,
        (('NO CUADRA: rehaz el CAPEX del libro 2 con estos precios',
          motor.CF_ROJO_BG, motor.CF_ROJO_FG),
         ('CUADRA con el CAPEX del libro 2',
          motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    ws.merge_cells('K%d:AA%d' % (CR_CUADRE, CR_CUADRE))
    motor.val(ws, 'K%d' % CR_CUADRE,
              'El plan financiero del libro 7 se calcula sobre el CAPEX del '
              'libro 2. Si esto se sale del umbral hay que rehacer los dos, no '
              'cambiar este número: es la diferencia entre un presupuesto y '
              'una lista de deseos.', wrap=True)
    ws['K%d' % CR_CUADRE].font = Font(italic=True, size=9)
    ws.row_dimensions[CR_CUADRE].height = 40

    # --- plazos -----------------------------------------------------------
    C.seccion(ws, 'A%d' % PL_SEC,
              'El plazo crítico, que es lo que de verdad mueve tu fecha de '
              'apertura')
    res(R_PLAZO, 'Plazo crítico de entrega (semanas)',
        ie('MAX(%s)' % rng('V')), C.FMT_ENT,
        'El plazo más largo de las líneas CRÍTICAS. Las opcionales no cuentan: '
        'si la atemperadora de arranque tarda un mes y no la necesitas para '
        'abrir, no puede mover tu fecha. ESTA ES LA CELDA QUE SE COPIA EN EL '
        'CRONOGRAMA DEL LIBRO 8.')
    res(R_PLAZO_LIN, 'Línea que marca el plazo crítico',
        ie('INDEX({c},MATCH($I${p},{v},0))'.format(c=rng('C'), p=R_PLAZO,
                                                   v=rng('V'))), None,
        'Ésta es la primera que hay que pedir, aunque sea de las últimas que '
        'vayas a instalar.')
    res(R_MARGEN, 'Margen del plazo crítico (semanas)',
        ie('IF(OR($C${s}="",$I${p}=""),"",$C${s}-$I${p}-$C${m})'
           .format(s=P_SEM, p=R_PLAZO, m=P_MARGEN)), C.FMT_ENT,
        'Semanas que te sobran entre pedir hoy el equipo de mayor plazo y '
        'abrir con el margen de seguridad dentro.')
    res(R_VER_PLAZO, 'Veredicto del plazo',
        ie('IF($I${m}="","",IF($I${m}<0,"El equipo de mayor plazo mueve la '
           'apertura: pídelo hoy o retrasa la fecha","Llegas con margen, pero '
           'pide primero el de mayor plazo"))'.format(m=R_MARGEN)), None,
        'Un obrador no abre porque falte una máquina, y la que falta casi '
        'siempre es la que se pidió la última.')
    res(R_TARDE, 'Líneas cuyo plazo se pasa de la apertura',
        ie('SUM(%s)' % rng('W')), C.FMT_ENT,
        'Cuenta también las opcionales: si la pides, tiene que llegar.')

    # --- listas -----------------------------------------------------------
    C.seccion(ws, 'A%d' % LI_SEC, 'Listas (origen de los desplegables)')
    C.cabecera(ws, LI_CAB, [('A', 'Estado'), ('C', 'Prioridad'),
                            ('E', 'Base del precio')], altura=20)
    for i, est in enumerate(ESTADOS):
        motor.val(ws, 'A%d' % (LI_INI + i), est)
    for i, pri in enumerate(PRIORIDADES):
        motor.val(ws, 'C%d' % (LI_INI + i), pri)
    for i, base in enumerate(BASES_IVA):
        motor.val(ws, 'E%d' % (LI_INI + i), base)

    C.parrafo(ws, EQ_NOTA,
              'CRÍTICO quiere decir «sin esto no abres», y es la lista que '
              'calcula el plazo crítico. OPCIONAL quiere decir «depende del '
              'formato»: la atemperadora de arranque y su cubeta (son la '
              'alternativa barata a la continua, no un complemento) y la '
              'chocolatera de la variante de taza. No hay un nivel intermedio '
              'a propósito: en una apertura, «recomendado» siempre acaba '
              'comprándose.', col_fin='AA', alto=44)
    C.parrafo(ws, EQ_NOTA + 1,
              'SEIS LÍNEAS TRAEN LA BASE FISCAL «NO DECLARADA»: el '
              'distribuidor no dice si su precio lleva IVA. Se tratan como '
              'base imponible y se marcan. La ficha de la atemperadora trae el '
              'indicio «Neto» en la línea de embalaje, que es un indicio, no '
              'una declaración. Pregúntalo por escrito antes de firmar: es un '
              '21' + N + '% de la partida más cara del obrador.',
              col_fin='AA', alto=44)
    C.parrafo(ws, EQ_NOTA + 2,
              'Los precios verificados llevan su id de fuente en la columna Z '
              'y su ficha completa en el comentario de la celda del precio. '
              'Están fechados el 12-09-2026 y pueden caducar: un catálogo de '
              'maquinaria se revisa un par de veces al año.',
              col_fin='AA', alto=32)

    # --- validación y semáforos -------------------------------------------
    C.dv_rango(ws, v_estado, '$A${a}:$A${b}'.format(a=LI_INI, b=LI_FIN),
               'Estado no válido',
               'Elige un estado de la lista del pie de la hoja: Pendiente, '
               'Presupuestado, Pedido, Recibido, Instalado o N/A.')
    motor.dv_numerica(ws, v_precio, minimo=0, titulo='Precio negociado',
                      mensaje='Escribe el precio SIN IVA, en euros.')
    motor.dv_numerica(ws, v_plazo, minimo=0, maximo=104,
                      titulo='Plazo de entrega',
                      mensaje='Escribe el plazo en SEMANAS (0 a 104).')
    motor.dv_porcentaje(ws, ['C%d' % P_IVA, 'C%d' % P_HORQ, 'C%d' % P_UMBRAL])
    motor.dv_numerica(ws, ['C%d' % P_SEM, 'C%d' % P_MARGEN], minimo=0,
                      maximo=104, titulo='Semanas',
                      mensaje='Escribe un número de semanas (0 a 104).')
    motor.dv_numerica(ws, ['I%d' % CR_VERDE], minimo=0,
                      titulo='CAPEX del libro 2',
                      mensaje='Escribe la base SIN IVA del bloque, en euros.')
    motor.semaforo_texto(ws, 'A%d:A%d' % (EQ_INI, EQ_FIN), motor.SEM_ESTADO)
    motor.semaforo_isnumber(ws, 'S%d:S%d' % (EQ_INI, EQ_FIN), '$S%d' % EQ_INI,
                            '<', '0')
    motor.regla_expresion(ws, 'P%d:P%d' % (EQ_INI, EQ_FIN),
                          '=AND(ISNUMBER($P{r}),$P{r}>$C${u})'
                          .format(r=EQ_INI, u=P_UMBRAL))
    motor.semaforo_isnumber(ws, 'I%d' % R_MARGEN, '$I$%d' % R_MARGEN, '<', '0')
    motor.regla_expresion(ws, 'I%d' % CR_PCT,
                          '=AND(ISNUMBER($I${d}),ABS($I${d})>$C${u})'
                          .format(d=CR_PCT, u=P_UMBRAL))
    C.pie(ws, EQ_PIE, 'A', 'F')
    ws.freeze_panes = 'C%d' % EQ_INI
    C.pagina(ws, titulos='$%d:$%d' % (EQ_CAB, EQ_CAB),
             area='A1:AA%d' % (EQ_PIE + 2))
    return ws


# ==========================================================================
# Hoja «Variante del Formato»
# ==========================================================================
BTB = D.VARIANTES['bean-to-bar']
TAZA = D.VARIANTES['taza-y-churros']
VARIANTES_LISTA = ('Bombonería (el caso del libro)',
                   'Bombonería + bean-to-bar',
                   'Bombonería + taza y churros')

V_SEC = 5
V_ELIGE = 6
V_AVISO = 7
V_BTB_SEC = 9
V_BTB_CAB = 10
V_BTB_INI = 11
V_BTB_FIN = V_BTB_INI + len(BTB['lista_de_la_compra']) - 1
V_BTB_TOT = V_BTB_FIN + 1
V_PRE_SEC = V_BTB_TOT + 2
V_PRE_CAB = V_PRE_SEC + 1
V_PRE_INI = V_PRE_CAB + 1
V_PRE_FIN = V_PRE_INI + len(BTB['preguntas_al_proveedor']) - 1
V_PRE_TOT = V_PRE_FIN + 1
V_BTB_VER = V_PRE_TOT + 1
V_TAZA_SEC = V_BTB_VER + 2
V_TAZA_CAB = V_TAZA_SEC + 1
V_TAZA_INI = V_TAZA_CAB + 1
V_TAZA_FIN = V_TAZA_INI + len(TAZA['equipos_sin_precio'])
V_TAZA_TOT = V_TAZA_FIN + 1
V_TAZA_VER = V_TAZA_FIN + 2
V_LIST_SEC = V_TAZA_VER + 2
V_LIST_CAB = V_LIST_SEC + 1
V_LIST_INI = V_LIST_CAB + 1
V_LIST_FIN = V_LIST_INI + max(len(VARIANTES_LISTA), len(SI_NO)) - 1
V_NOTA = V_LIST_FIN + 2
V_PIE = V_NOTA + 4


def hoja_variante(wb):
    ws = wb.create_sheet(H_VAR)
    C.anchos(ws, {'A': 6, 'B': 50, 'C': 20, 'D': 20, 'E': 18, 'F': 88})
    C.encabezar(ws, 'Variante del formato: bean-to-bar o taza y churros',
                'Dos caminos que NO son este producto y se deciden aquí. El '
                'bean-to-bar va SIN CIFRAS DE MAQUINARIA a propósito: no hay '
                'precio público verificado, y lo que se entrega es la lista de '
                'la compra y las preguntas que hay que hacer.', col_fin='F')

    refs, fila_listas = C.bloque_listas(
        ws, V_LIST_SEC, [('Variante', list(VARIANTES_LISTA)),
                         ('Sí o No', list(SI_NO))], col='A')

    C.seccion(ws, 'A%d' % V_SEC, 'Tu formato')
    motor.val(ws, 'A%d' % V_ELIGE, '¿Qué vas a montar?', bold=True)
    ws.merge_cells('A%d:B%d' % (V_ELIGE, V_ELIGE))
    X.entrada(ws, 'C%d' % V_ELIGE, VARIANTES_LISTA[0],
              etiqueta='Variante del formato')
    C.dv_rango(ws, ['C%d' % V_ELIGE], refs['Variante'], 'Elige una variante',
               'Elige una de las tres opciones de la lista del pie de la '
               'hoja.')
    ws.merge_cells('D%d:F%d' % (V_ELIGE, V_ELIGE))
    C.nota(ws, 'D%d' % V_ELIGE,
           'El libro 2 calcula el CAPEX de cada variante. Aquí sólo se '
           'resuelve QUÉ hay que comprar y QUÉ hay que preguntar.')
    motor.val(ws, 'A%d' % V_AVISO, 'Lo primero que cambia', bold=True)
    ws.merge_cells('A%d:B%d' % (V_AVISO, V_AVISO))
    motor.f(ws, 'C%d' % V_AVISO,
            ie('IF($C${e}=$A${b},"Si importas grano ERES OPERADOR a efectos '
               'del EUDR: diligencia debida completa y declaración presentada '
               'ANTES de introducir en el mercado",IF($C${e}=$A${t},"La '
               'chocolatería de taza NO está en el Anexo de la Ley 12/2012: '
               'el amparo frente a la licencia previa de actividad NO te '
               'cubre","Bombonería: el epígrafe 644.5 SÍ está en ese Anexo, '
               'hasta 750 metros cuadrados"))'
               .format(e=V_ELIGE, b=V_LIST_INI + 1, t=V_LIST_INI + 2)))
    ws.merge_cells('C%d:F%d' % (V_AVISO, V_AVISO))
    ws['C%d' % V_AVISO].alignment = Alignment(vertical='top', wrap_text=True)
    ws.row_dimensions[V_AVISO].height = 34
    X.nota_celda(ws, 'C%d' % V_AVISO, 'CHN-49c')

    # --- bean-to-bar ------------------------------------------------------
    C.seccion(ws, 'A%d' % V_BTB_SEC,
              'BEAN-TO-BAR: la lista de la compra, SIN precios (D2)')
    C.cabecera(ws, V_BTB_CAB,
               [('A', 'Nº'), ('B', 'Equipo del tren bean-to-bar'),
                ('C', '¿Lo necesitas?'), ('D', '¿Tienes precio por escrito?'),
                ('E', 'Plazo prometido (semanas)'), ('F', 'Notas')],
               altura=30)
    v_necesitas, v_precio_esc, v_plazo_btb = [], [], []
    for i, equipo in enumerate(BTB['lista_de_la_compra']):
        r = V_BTB_INI + i
        motor.val(ws, 'A%d' % r, i + 1, fmt=C.FMT_ENT, align='center')
        motor.val(ws, 'B%d' % r, equipo, wrap=True)
        X.entrada(ws, 'C%d' % r, NO, etiqueta='¿Necesitas ' + equipo + '?',
                  align='center')
        v_necesitas.append('C%d' % r)
        X.entrada(ws, 'D%d' % r, NO, etiqueta='Precio por escrito de ' + equipo,
                  align='center')
        v_precio_esc.append('D%d' % r)
        X.entrada(ws, 'E%d' % r, 0, fmt=C.FMT_ENT,
                  etiqueta='Plazo prometido de ' + equipo, align='center')
        v_plazo_btb.append('E%d' % r)
        motor.val(ws, 'F%d' % r, '', wrap=True)
    motor.val(ws, 'B%d' % V_BTB_TOT, 'Equipos que dices necesitar', bold=True)
    motor.f(ws, 'C%d' % V_BTB_TOT,
            ie('COUNTIF(C%d:C%d,"%s")' % (V_BTB_INI, V_BTB_FIN, SI)),
            fmt=C.FMT_ENT, bold=True)
    motor.f(ws, 'D%d' % V_BTB_TOT,
            ie('COUNTIF(D%d:D%d,"%s")' % (V_BTB_INI, V_BTB_FIN, SI)),
            fmt=C.FMT_ENT, bold=True)
    motor.f(ws, 'E%d' % V_BTB_TOT,
            ie('MAX(E%d:E%d)' % (V_BTB_INI, V_BTB_FIN)), fmt=C.FMT_ENT,
            bold=True)
    X.total_fila(ws, V_BTB_TOT, 'ABCDEF')
    C.nota(ws, 'F%d' % V_BTB_TOT,
           'Equipos que necesitas · con precio por escrito · plazo más largo '
           'prometido. Mientras las dos primeras cifras no coincidan, no '
           'tienes un presupuesto: tienes una intención.')

    C.seccion(ws, 'A%d' % V_PRE_SEC,
              'Las cinco preguntas que hay que hacerle al fabricante')
    C.cabecera(ws, V_PRE_CAB,
               [('A', 'Nº'), ('B', 'Pregunta'), ('C', '¿Te la han contestado?'),
                ('D', 'Quién te contestó'), ('E', 'Fecha'),
                ('F', 'Por qué importa')], altura=30)
    v_contestado = []
    for i, preg in enumerate(BTB['preguntas_al_proveedor']):
        r = V_PRE_INI + i
        motor.val(ws, 'A%d' % r, i + 1, fmt=C.FMT_ENT, align='center')
        motor.val(ws, 'B%d' % r, preg, wrap=True)
        X.entrada(ws, 'C%d' % r, NO, etiqueta='Pregunta %d contestada' % (i + 1),
                  align='center')
        v_contestado.append('C%d' % r)
        X.entrada(ws, 'D%d' % r, 'Pendiente',
                  etiqueta='Quién contestó la pregunta %d' % (i + 1))
        X.entrada(ws, 'E%d' % r, FECHA_BASE, fmt=C.FMT_FECHA,
                  etiqueta='Fecha de la pregunta %d' % (i + 1))
        motor.val(ws, 'F%d' % r, '', wrap=True)
        ws.row_dimensions[r].height = 40
    motor.val(ws, 'B%d' % V_PRE_TOT, 'Preguntas contestadas POR ESCRITO',
              bold=True)
    motor.f(ws, 'C%d' % V_PRE_TOT,
            ie('COUNTIF(C%d:C%d,"%s")' % (V_PRE_INI, V_PRE_FIN, SI)),
            fmt=C.FMT_ENT, bold=True)
    X.total_fila(ws, V_PRE_TOT, 'ABCDEF')
    motor.val(ws, 'B%d' % V_BTB_VER, 'VEREDICTO DEL BEAN-TO-BAR', bold=True)
    motor.f(ws, 'C%d' % V_BTB_VER,
            ie('IF($C${e}<>$A${b},"No es tu variante: no hay nada que '
               'presupuestar",IF(AND($C${t}>0,$D${t}=$C${t},$C${p}={n}),'
               '"Ya puedes presupuestarlo: tienes precio y respuesta de todo '
               'lo que necesitas","Te faltan precios por escrito o respuestas: '
               'no cierres el CAPEX del bean-to-bar todavía"))'
               .format(e=V_ELIGE, b=V_LIST_INI + 1, t=V_BTB_TOT, p=V_PRE_TOT,
                       n=len(BTB['preguntas_al_proveedor']))),
            bold=True)
    ws.merge_cells('C%d:F%d' % (V_BTB_VER, V_BTB_VER))
    ws['C%d' % V_BTB_VER].alignment = Alignment(vertical='top', wrap_text=True)
    ws.row_dimensions[V_BTB_VER].height = 34
    C.destacado(ws, 'C%d' % V_BTB_VER)
    X.nota_celda(ws, 'C%d' % V_BTB_VER, 'CHN-25')

    # --- taza y churros ---------------------------------------------------
    C.seccion(ws, 'A%d' % V_TAZA_SEC,
              'TAZA Y CHURROS: lo único con precio verificado, y lo que no lo '
              'tiene')
    C.cabecera(ws, V_TAZA_CAB,
               [('A', 'Nº'), ('B', 'Equipo'), ('C', 'Precio (€, sin IVA)'),
                ('D', '¿Lo necesitas?'), ('E', 'Fuente'), ('F', 'Notas')],
               altura=26)
    r = V_TAZA_INI
    eq_taza = TAZA['equipos_con_precio'][0]
    motor.val(ws, 'A%d' % r, 1, fmt=C.FMT_ENT, align='center')
    motor.val(ws, 'B%d' % r, eq_taza[0], wrap=True)
    motor.val(ws, 'C%d' % r, eq_taza[1], fmt=C.FMT_EUR)
    X.entrada(ws, 'D%d' % r, NO, etiqueta='¿Necesitas la chocolatera?',
              align='center')
    motor.val(ws, 'E%d' % r, eq_taza[2])
    motor.val(ws, 'F%d' % r, 'Base ' + eq_taza[3] + ' declarada por la ficha. '
                             'Es la única línea de esta variante con precio '
                             'público verificado.', wrap=True)
    X.nota_fuente(ws, 'C%d' % r, eq_taza[2])
    v_taza = ['D%d' % r]
    for i, equipo in enumerate(TAZA['equipos_sin_precio']):
        r = V_TAZA_INI + 1 + i
        motor.val(ws, 'A%d' % r, i + 2, fmt=C.FMT_ENT, align='center')
        motor.val(ws, 'B%d' % r, equipo, wrap=True)
        motor.val(ws, 'C%d' % r, '')
        X.entrada(ws, 'D%d' % r, NO, etiqueta='¿Necesitas ' + equipo + '?',
                  align='center')
        motor.val(ws, 'E%d' % r, 'CHS-49 (sin verificar)')
        motor.val(ws, 'F%d' % r, 'SIN PRECIO: los precios de churrera, '
                                 'freidora y extracción no están verificados. '
                                 'Presupuéstalo, no lo estimes.', wrap=True)
        v_taza.append('D%d' % r)
        ws.row_dimensions[r].height = 30
    motor.val(ws, 'B%d' % V_TAZA_TOT, 'Equipos de la variante que necesitas',
              bold=True)
    motor.f(ws, 'C%d' % V_TAZA_TOT,
            ie('COUNTIF(D%d:D%d,"%s")' % (V_TAZA_INI, V_TAZA_FIN, SI)),
            fmt=C.FMT_ENT, bold=True)
    X.total_fila(ws, V_TAZA_TOT, 'ABCDEF')
    motor.val(ws, 'B%d' % V_TAZA_VER, 'LO QUE TE OBLIGA ADEMÁS', bold=True)
    motor.f(ws, 'C%d' % V_TAZA_VER,
            ie('IF($C${e}<>$A${t},"No es tu variante","' + TAZA['obligacion_extra']
               .replace('(`CHN-48`)', '').replace('"', "'").strip().rstrip('.')
               + '")').format(e=V_ELIGE, t=V_LIST_INI + 2), bold=True)
    ws.merge_cells('C%d:F%d' % (V_TAZA_VER, V_TAZA_VER))
    ws['C%d' % V_TAZA_VER].alignment = Alignment(vertical='top', wrap_text=True)
    ws.row_dimensions[V_TAZA_VER].height = 46
    C.destacado(ws, 'C%d' % V_TAZA_VER)
    X.nota_celda(ws, 'C%d' % V_TAZA_VER, 'CHN-48')

    C.dv_rango(ws, v_necesitas + v_precio_esc + v_contestado + v_taza,
               refs['Sí o No'], 'Marca Sí o No',
               'Elige «Sí» o «No» de la lista del pie de la hoja.')
    motor.dv_numerica(ws, v_plazo_btb, minimo=0, maximo=104,
                      titulo='Plazo prometido',
                      mensaje='Escribe el plazo en SEMANAS (0 a 104).')

    C.parrafo(ws, V_NOTA,
              'POR QUÉ EL BEAN-TO-BAR VA SIN CIFRAS: no existe precio público '
              'verificado del tren completo. Los catálogos existen y están '
              'comprobados, pero la venta es a presupuesto o desde tiendas '
              'fuera de la Unión. Inventar aquí un número sería justo el '
              'patrón que esta casa prohíbe, y en una máquina de tostar el '
              'error se paga con la aduana dentro.', 'A', 'F', alto=48)
    C.parrafo(ws, V_NOTA + 1,
              'Y sube de valor por dos motivos legales: si importas grano eres '
              'OPERADOR a efectos del reglamento de deforestación -diligencia '
              'debida completa, declaración presentada previamente y registro '
              'durante cinco años-, y el TOSTADO te puede meter en el catálogo '
              'de actividades potencialmente contaminadoras de la atmósfera, '
              'cuya nota (2) sube de grupo C a B cuando la actividad está a '
              'menos de 500 metros de un núcleo de población: en ciudad, '
              'siempre.', 'A', 'F', alto=56)
    C.parrafo(ws, V_NOTA + 2,
              'Ojo con el encaje: «cacao» y «chocolate» tienen CERO '
              'ocurrencias en ese catálogo, así que meter el tostado de cacao '
              'en «café o similares» es una INTERPRETACIÓN, no una mención '
              'expresa. Pregúntalo en tu comunidad antes de comprar el '
              'tostador.', 'A', 'F', alto=40)
    C.pie(ws, V_PIE, 'A', 'C')
    ws.freeze_panes = 'A4'
    C.pagina(ws, area='A1:F%d' % (V_PIE + 2))
    return ws


# ==========================================================================
# Hoja «Proveedores y EUDR» (D48.a)
# ==========================================================================
PR_SEC = 5
PR_CAB = 6
PR_INI = 7
PR_FIN = PR_INI + len(D.PROVEEDORES) - 1
PR_RES_SEC = PR_FIN + 2
PR_TOT = PR_RES_SEC + 1
PR_TRAB = PR_RES_SEC + 2
PR_OPER = PR_RES_SEC + 3
PR_POST = PR_RES_SEC + 4
PR_COM = PR_RES_SEC + 5
PR_SINPAPEL = PR_RES_SEC + 6
PR_DDS = PR_RES_SEC + 7
PR_CADMIO = PR_RES_SEC + 8
PR_HAP = PR_RES_SEC + 9
PR_MIN = PR_RES_SEC + 10
PR_PLAZO = PR_RES_SEC + 11
PR_VER = PR_RES_SEC + 12
PR_LIST_SEC = PR_VER + 2
PR_LIST_CAB = PR_LIST_SEC + 1
PR_LIST_INI = PR_LIST_CAB + 1
#: +2: además de los tres papeles del EUDR, el desplegable de la columna G
#: lleva «No lo sé» y «No aplica: no vende producto del Anexo I» (B1).
PR_LIST_FIN = PR_LIST_INI + max(len(D.PAPELES_EUDR) + 2, len(SI_NO_NOSE)) - 1
PR_NOTA = PR_LIST_FIN + 2
PR_PIE = PR_NOTA + 5


def hoja_proveedores(wb):
    ws = wb.create_sheet(H_PROV)
    C.anchos(ws, {'A': 5, 'B': 32, 'C': 34, 'D': 46, 'E': 10, 'F': 13,
                  'G': 20, 'H': 15, 'I': 24, 'J': 14, 'K': 14, 'L': 15,
                  'M': 12, 'N': 54, 'O': 46, 'P': 78})
    C.encabezar(ws, 'Proveedores: operador, operador posterior o comerciante',
                'Los seis con URL comprobada el 12-09-2026. La columna que '
                'decide es la G: el número de referencia de la declaración de '
                'diligencia debida SÓLO se le pide a un operador. Pedírselo a '
                'un comerciante es pedirle algo que no tiene.', col_fin='P')

    # B1 (refutación 2026-09-12): el desplegable de la columna G lleva DOS
    # opciones más que las tres del EUDR, para las líneas donde el papel no
    # se sabe todavía o donde el proveedor ni siquiera vende un producto del
    # Anexo I -maquinaria, moldes de packaging, regalo corporativo-, que es
    # justo el caso de tres de los seis (`FUERA_AMBITO`).
    NOSE_PAPEL = 'No lo sé'
    FUERA_AMBITO = 'No aplica: no vende producto del Anexo I'
    PAPELES_PROV = list(D.PAPELES_EUDR) + [NOSE_PAPEL, FUERA_AMBITO]
    #: Índices (0-based, orden de `D.PROVEEDORES`) que NO comercializan cacao
    #: ni chocolate: Utilcentre (maquinaria), SelfPackaging (cajas) y Gift
    #: Campaign (regalo corporativo). Callebaut, la Asociación Bean-to-Bar
    #: (grano) y RestorHome (moldes) sí quedan en «No lo sé», a la espera de
    #: que el lector se lo pregunte -RestorHome vende utensilios, no producto
    #: del Anexo I, pero el hallazgo B1 sólo tumbó los tres primeros y no se
    #: amplía aquí el alcance del hallazgo.
    PROV_FUERA_AMBITO = {2, 4, 5}

    refs, fila_listas = C.bloque_listas(
        ws, PR_LIST_SEC, [('Papel en la cadena', PAPELES_PROV),
                          ('Sí, No o No lo sé', list(SI_NO_NOSE))], col='A')
    ref_papel = refs['Papel en la cadena']
    C_OPERADOR = '$A$%d' % PR_LIST_INI

    C.seccion(ws, 'A%d' % PR_SEC, 'Los seis proveedores verificados')
    C.cabecera(ws, PR_CAB, [
        ('A', 'Nº'), ('B', 'Proveedor'), ('C', 'Qué te vende'), ('D', 'URL'),
        ('E', 'Id'), ('F', '¿Trabajas con él?'),
        ('G', '¿Operador, operador posterior o comerciante?'),
        ('H', '¿Te ha dado el nº de su DDS?'),
        ('I', 'Nº de referencia de la DDS'),
        ('J', '¿Boletín de cadmio?'), ('K', '¿Boletín de HAP?'),
        ('L', 'Pedido mínimo (€)'), ('M', 'Plazo (días)'),
        ('N', 'Qué papeles le tocan a ÉL'),
        ('O', 'Semáforo de documentación'),
        ('P', 'Por qué está en la lista')], altura=52)

    v_trabaja, v_papel, v_dds_si, v_dds_num = [], [], [], []
    v_cadmio, v_hap, v_min, v_plazo = [], [], [], []
    for i, (nombre, cat, url, idps, papel, nota) in enumerate(D.PROVEEDORES):
        r = PR_INI + i
        motor.val(ws, 'A%d' % r, i + 1, fmt=C.FMT_ENT, align='center')
        motor.val(ws, 'B%d' % r, nombre, wrap=True)
        motor.val(ws, 'C%d' % r, cat, wrap=True)
        motor.val(ws, 'D%d' % r, url)
        motor.val(ws, 'E%d' % r, idps, align='center')
        X.entrada(ws, 'F%d' % r, NO, etiqueta='¿Trabajas con ' + nombre + '?',
                  align='center')
        v_trabaja.append('F%d' % r)
        X.entrada(ws, 'G%d' % r,
                  FUERA_AMBITO if i in PROV_FUERA_AMBITO else NOSE_PAPEL,
                  etiqueta='Papel EUDR de ' + nombre)
        v_papel.append('G%d' % r)
        X.entrada(ws, 'H%d' % r, NOSE, etiqueta='DDS de ' + nombre,
                  align='center')
        v_dds_si.append('H%d' % r)
        X.entrada(ws, 'I%d' % r, DDS_PENDIENTE,
                  etiqueta='Nº de DDS de ' + nombre)
        v_dds_num.append('I%d' % r)
        X.entrada(ws, 'J%d' % r, NOSE, etiqueta='Cadmio de ' + nombre,
                  align='center')
        v_cadmio.append('J%d' % r)
        X.entrada(ws, 'K%d' % r, NOSE, etiqueta='HAP de ' + nombre,
                  align='center')
        v_hap.append('K%d' % r)
        X.entrada(ws, 'L%d' % r, PEDIDO_MINIMO_DEFECTO, fmt=C.FMT_EUR,
                  etiqueta='Pedido mínimo de ' + nombre)
        v_min.append('L%d' % r)
        X.entrada(ws, 'M%d' % r, PLAZO_PROVEEDOR_DEFECTO, fmt=C.FMT_ENT,
                  etiqueta='Plazo de ' + nombre, align='center')
        v_plazo.append('M%d' % r)
        motor.f(ws, 'N%d' % r,
                ie('IF($G{r}="","",IF($G{r}={op},"Sus datos Y el nº de '
                   'referencia de su DDS (art. 5.3.a)",IF($G{r}="{fuera}",'
                   '"No le pidas papeles EUDR: no vende producto del Anexo '
                   'I",IF($G{r}="{nose}","Pregúntaselo por escrito antes de '
                   'comprar: de su respuesta depende qué papeles pedirle",'
                   '"Sus datos, su dirección y el producto: el nº de DDS NO '
                   'se le pide por el art. 5.3.a)"))))'
                   .format(r=r, op=C_OPERADOR, fuera=FUERA_AMBITO,
                           nose=NOSE_PAPEL)))
        ws['N%d' % r].alignment = Alignment(vertical='top', wrap_text=True)
        motor.f(ws, 'O%d' % r,
                ie('IF($G{r}="","",IF($G{r}={op},IF(AND($H{r}="{si}",'
                   '$I{r}<>"{pe}"),"Completa: tienes su nº de DDS",'
                   '"FALTA el nº de referencia de su DDS"),IF($G{r}="{fuera}"'
                   ',"No aplica: fuera del ámbito EUDR",IF($G{r}="{nose}",'
                   '"Pregúntaselo por escrito antes de comprar",'
                   'IF(OR($J{r}="{no}",$K{r}="{no}"),'
                   '"Pídele los boletines de cadmio y de HAP",'
                   '"Completa para su papel en la cadena")))))'
                   .format(r=r, op=C_OPERADOR, si=SI, no=NO,
                           pe=DDS_PENDIENTE, fuera=FUERA_AMBITO,
                           nose=NOSE_PAPEL)))
        ws['O%d' % r].alignment = Alignment(vertical='top', wrap_text=True)
        motor.val(ws, 'P%d' % r, nota or '', wrap=True)
        ws.row_dimensions[r].height = 60
    X.nota_celda(ws, 'G%d' % PR_CAB, 'CHN-24')
    X.nota_celda(ws, 'I%d' % PR_CAB, 'CHN-26')
    X.nota_celda(ws, 'K%d' % PR_CAB, 'CHN-18')

    C.dv_rango(ws, v_papel, ref_papel, 'Elige el papel en la cadena',
               'Operador, operador posterior o comerciante si te vende '
               'producto del Anexo I; «No lo sé» mientras no se lo hayas '
               'preguntado, y «No aplica» si ni siquiera te vende un '
               'producto pertinente (maquinaria, moldes, packaging, regalo '
               'corporativo). La diferencia decide qué papeles pedirle.')
    C.dv_rango(ws, v_trabaja + v_dds_si + v_cadmio + v_hap,
               refs['Sí, No o No lo sé'], 'Marca Sí, No o No lo sé',
               'Elige una de las tres opciones de la lista del pie.')
    motor.dv_numerica(ws, v_min, minimo=0, titulo='Pedido mínimo',
                      mensaje='Escribe el pedido mínimo en euros, sin IVA.')
    motor.dv_numerica(ws, v_plazo, minimo=0, maximo=180, titulo='Plazo',
                      mensaje='Escribe el plazo de entrega en días (0 a 180).')

    def res(fila, etiqueta, formula, fmt=None, nota='', bold=True):
        ws.merge_cells('A%d:E%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, etiqueta, bold=bold, wrap=True)
        motor.f(ws, 'F%d' % fila, formula, fmt=fmt, bold=bold)
        ws['F%d' % fila].fill = PatternFill('solid', fgColor=C.CREMA)
        ws.merge_cells('H%d:P%d' % (fila, fila))
        motor.val(ws, 'H%d' % fila, nota, wrap=True)
        ws['H%d' % fila].font = Font(italic=True, size=9)
        ws.row_dimensions[fila].height = 26

    C.seccion(ws, 'A%d' % PR_RES_SEC, 'Resumen de la cartera de proveedores')
    res(PR_TOT, 'Proveedores publicados en esta hoja',
        '=COUNTIF($B${a}:$B${b},"<>")'.format(a=PR_INI, b=PR_FIN), C.FMT_ENT,
        'Seis verificados con URL el 12-09-2026. Los que el research recogió '
        'sin verificar no entran.')
    res(PR_TRAB, 'Proveedores con los que ya trabajas',
        '=COUNTIF($F${a}:$F${b},"{s}")'.format(a=PR_INI, b=PR_FIN, s=SI),
        C.FMT_ENT,
        'Empieza por dos o tres: abrir ficha en seis proveedores a la vez es '
        'una semana de papeleo y ningún descuento.')
    res(PR_OPER, 'De ellos, OPERADORES (primera comercialización o '
                 'exportación)',
        '=COUNTIF($G${a}:$G${b},"{p}")'.format(a=PR_INI, b=PR_FIN,
                                               p=D.PAPELES_EUDR[0]),
        C.FMT_ENT,
        'A éstos, y sólo a éstos, hay que pedirles el número de referencia de '
        'su declaración de diligencia debida.')
    res(PR_POST, 'De ellos, operadores posteriores',
        '=COUNTIF($G${a}:$G${b},"{p}")'.format(a=PR_INI, b=PR_FIN,
                                               p=D.PAPELES_EUDR[1]),
        C.FMT_ENT,
        'Introducen en el mercado productos elaborados con otros YA amparados '
        'por una declaración. Es lo que normalmente será tu proveedor de '
        'cobertura.')
    res(PR_COM, 'De ellos, comerciantes',
        '=COUNTIF($G${a}:$G${b},"{p}")'.format(a=PR_INI, b=PR_FIN,
                                               p=D.PAPELES_EUDR[2]),
        C.FMT_ENT, 'Ni introducen ni exportan: comercian dentro.')
    res(PR_SINPAPEL, 'Proveedores a los que todavía no les has preguntado',
        ie('$F${t}-($F${o}+$F${p}+$F${c})'
           .format(t=PR_TOT, o=PR_OPER, p=PR_POST, c=PR_COM)), C.FMT_ENT,
        'Mientras esta cifra no sea cero, no sabes qué papeles te faltan. Es '
        'una pregunta de dos líneas en un correo.')
    res(PR_DDS, 'Operadores que todavía no te han dado su nº de DDS',
        '=SUMPRODUCT(--($G${a}:$G${b}="{p}"),--($I${a}:$I${b}="{pe}"))'
        .format(a=PR_INI, b=PR_FIN, p=D.PAPELES_EUDR[0], pe=DDS_PENDIENTE),
        C.FMT_ENT,
        'Sólo cuenta a los operadores: a los demás no se les pide, y un '
        'semáforo que se lo exigiera suspendería a proveedores que cumplen.')
    res(PR_CADMIO, 'Proveedores que NO te dan boletín de cadmio',
        '=COUNTIF($J${a}:$J${b},"{n}")'.format(a=PR_INI, b=PR_FIN, n=NO),
        C.FMT_ENT,
        'El boletín del proveedor es la primera línea de defensa: la analítica '
        'propia es la segunda. La hoja «Cadmio y Analíticas» del libro 8 '
        'decide si te hace falta y con qué frecuencia.')
    res(PR_HAP, 'Proveedores que NO te dan boletín de HAP',
        '=COUNTIF($K${a}:$K${b},"{n}")'.format(a=PR_INI, b=PR_FIN, n=NO),
        C.FMT_ENT,
        'Los hidrocarburos aromáticos policíclicos aparecen en el grano y en '
        'la fibra de cacao, no en la cobertura terminada: pídeselo sobre todo '
        'a quien te venda grano.')
    res(PR_MIN, 'Pedido mínimo acumulado si pides a todos a la vez (€)',
        '=SUM($L${a}:$L${b})'.format(a=PR_INI, b=PR_FIN), C.FMT_EUR,
        'Es dinero parado en el almacén el día que menos caja tienes. Los '
        'pedidos mínimos que vienen puestos son SUPUESTOS: te los confirma '
        'cada comercial.')
    res(PR_PLAZO, 'Plazo medio de entrega comprometido (días)',
        ie('AVERAGE($M${a}:$M${b})'.format(a=PR_INI, b=PR_FIN)), C.FMT_DEC,
        'Con qué antelación tienes que pedir. La antelación de compra por '
        'campaña la calcula «campanas-y-valle-del-ano.xlsx».')
    res(PR_VER, 'VEREDICTO DE LA DOCUMENTACIÓN',
        ie('IF($F${s}>0,"Te faltan proveedores por clasificar: pregúntales su '
           'papel en la cadena",IF($F${d}>0,"Te falta el nº de DDS de algún '
           'OPERADOR: sin él no puedes acreditar tu diligencia debida",'
           '"Documentación coherente con tu papel en la cadena"))'
           .format(s=PR_SINPAPEL, d=PR_DDS)))
    C.destacado(ws, 'F%d' % PR_VER)
    ws.merge_cells('F%d:G%d' % (PR_VER, PR_VER))
    ws['F%d' % PR_VER].alignment = Alignment(vertical='top', wrap_text=True)
    ws.row_dimensions[PR_VER].height = 40
    X.nota_celda(ws, 'F%d' % PR_VER, 'CHN-24')

    motor.semaforo_isnumber(ws, 'F%d' % PR_SINPAPEL, '$F$%d' % PR_SINPAPEL,
                            '>', '0', bg=motor.CF_AMBAR_BG,
                            fg=motor.CF_AMBAR_FG)
    motor.semaforo_isnumber(ws, 'F%d' % PR_DDS, '$F$%d' % PR_DDS, '>', '0')
    motor.semaforo_isnumber(ws, 'F%d' % PR_CADMIO, '$F$%d' % PR_CADMIO,
                            '>', '0', bg=motor.CF_AMBAR_BG,
                            fg=motor.CF_AMBAR_FG)

    C.parrafo(ws, PR_NOTA, D.NOTA_PROVEEDORES, 'A', 'P', alto=48)
    C.parrafo(ws, PR_NOTA + 1, D.NOTA_EUDR, 'A', 'P', alto=76)
    C.parrafo(ws, PR_NOTA + 2,
              'Directorio HORECA del grupo, con su certificado comprobado '
              'antes de publicarlo: ' + D.HOSPLY_URL, 'A', 'P', alto=28)
    C.parrafo(ws, PR_NOTA + 3,
              'Los pedidos mínimos, los plazos y la respuesta del papel en la '
              'cadena que vienen rellenos son SUPUESTOS para que la hoja '
              'funcione desde el primer minuto: no son las condiciones de '
              'estas empresas ni su clasificación real. Cada una te dará las '
              'suyas.', 'A', 'P', alto=40)
    C.pie(ws, PR_PIE, 'A', 'C')
    ws.freeze_panes = 'C%d' % PR_INI
    C.pagina(ws, titulos='$%d:$%d' % (PR_CAB, PR_CAB),
             area='A1:P%d' % (PR_PIE + 2))
    return ws


# ==========================================================================
# Hoja «Clientes a los que Suministras» (D48.b, art. 5.3.b)
# ==========================================================================
CLIENTES_LIBRES = 4
N_CLI = len(D.CLIENTES_B2B) + CLIENTES_LIBRES
#: El juego de datos escribe los literales SIN TILDE (es un módulo de datos que
#: viaja por heredocs); en el libro se publican bien escritos, con su mapa de
#: equivalencia para que el sembrado siga casando con el desplegable.
CANALES_CLI = ('B2B a hostelería', 'Regalo corporativo',
               'Minorista de distinta titularidad', 'Otro')
CANAL_DESDE_DATOS = {'B2B hosteleria': CANALES_CLI[0],
                     'Regalo corporativo': CANALES_CLI[1],
                     'Minorista de distinta titularidad': CANALES_CLI[2]}
TIPOS_CLI = ('Hostelería', 'Empresa', 'Minorista de distinta titularidad',
             'Consumidor final')
TIPO_DESDE_DATOS = {'Hosteleria': TIPOS_CLI[0], 'Empresa': TIPOS_CLI[1],
                    'Minorista de distinta titularidad': TIPOS_CLI[2]}

CL_PAR_SEC = 5
CL_ANOS = 6
CL_SEC = 8
CL_CAB = 9
CL_INI = 10
CL_FIN = CL_INI + N_CLI - 1
CL_RES_SEC = CL_FIN + 2
CL_TOT = CL_RES_SEC + 1
CL_B2B = CL_RES_SEC + 2
CL_CORP = CL_RES_SEC + 3
CL_MIN = CL_RES_SEC + 4
CL_RGSEAA = CL_RES_SEC + 5
CL_HASTA = CL_RES_SEC + 6
CL_VER = CL_RES_SEC + 7
CL_ART3 = CL_RES_SEC + 8
CL_LIST_SEC = CL_ART3 + 2
CL_LIST_CAB = CL_LIST_SEC + 1
CL_LIST_INI = CL_LIST_CAB + 1
CL_LIST_FIN = CL_LIST_INI + max(len(CANALES_CLI), len(TIPOS_CLI),
                                len(SI_NO_NOSE)) - 1
CL_NOTA = CL_LIST_FIN + 2
CL_PIE = CL_NOTA + 4


def hoja_clientes(wb):
    ws = wb.create_sheet(H_CLI)
    C.anchos(ws, {'A': 5, 'B': 34, 'C': 26, 'D': 26, 'E': 30, 'F': 44,
                  'G': 15, 'H': 17, 'I': 17, 'J': 62})
    C.encabezar(ws, 'Clientes a los que suministras: el registro del art. '
                    '5.3.b)',
                'La tabla que no existe en ningún otro libro del catálogo. El '
                'mismo artículo que te hace guardar los datos de tus '
                'proveedores te obliga a registrar a los operadores '
                'posteriores y comerciantes A LOS QUE TÚ HAS SUMINISTRADO. Se '
                'conserva cinco años.', col_fin='J')

    refs, fila_listas = C.bloque_listas(
        ws, CL_LIST_SEC, [('Canal', list(CANALES_CLI)),
                          ('Tipo de cliente', list(TIPOS_CLI)),
                          ('Sí, No o No lo sé', list(SI_NO_NOSE))], col='A')

    C.seccion(ws, 'A%d' % CL_PAR_SEC, 'Parámetro de esta hoja')
    motor.val(ws, 'A%d' % CL_ANOS, 'Años que hay que conservar el registro',
              bold=True)
    ws.merge_cells('A%d:B%d' % (CL_ANOS, CL_ANOS))
    X.entrada(ws, 'C%d' % CL_ANOS, ANOS_CONSERVACION, fmt=C.FMT_ENT,
              etiqueta='Años de conservación del registro', align='center')
    X.nota_celda(ws, 'C%d' % CL_ANOS, 'CHN-24')
    ws.merge_cells('D%d:J%d' % (CL_ANOS, CL_ANOS))
    C.nota(ws, 'D%d' % CL_ANOS,
           'Cinco años, y de ahí sale la columna «Conservar hasta». Está en '
           'celda verde porque es un parámetro normativo: si cambia, se cambia '
           'aquí y no en once fórmulas.')

    C.seccion(ws, 'A%d' % CL_SEC,
              'A quién le has suministrado, qué y cuándo')
    C.cabecera(ws, CL_CAB, [
        ('A', 'Nº'), ('B', 'Nombre del cliente'),
        ('C', 'Dirección o población'), ('D', 'Tipo'), ('E', 'Canal'),
        ('F', 'Producto suministrado'), ('G', 'Primer suministro'),
        ('H', '¿Inscrito en el RGSEAA?'), ('I', 'Conservar hasta'),
        ('J', 'Notas')], altura=36)

    v_nombre, v_canal, v_tipo, v_rgseaa, v_fecha = [], [], [], [], []
    for i in range(N_CLI):
        r = CL_INI + i
        if i < len(D.CLIENTES_B2B):
            nombre, tipo, canal, pob, producto = D.CLIENTES_B2B[i]
            tipo = TIPO_DESDE_DATOS[tipo]
            canal = CANAL_DESDE_DATOS[canal]
            nota_fila = ('Cliente de EJEMPLO declarado: sustitúyelo por el '
                         'tuyo. Lo que no es un ejemplo es la obligación de '
                         'tener esta tabla.')
        else:
            nombre, tipo, canal, pob, producto = (
                LIBRE, TIPOS_CLI[3], CANALES_CLI[3], 'Pendiente', 'Pendiente')
            nota_fila = 'Fila libre: escribe aquí tu cliente.'
        motor.val(ws, 'A%d' % r, i + 1, fmt=C.FMT_ENT, align='center')
        X.entrada(ws, 'B%d' % r, nombre, etiqueta='Cliente %d' % (i + 1))
        v_nombre.append('B%d' % r)
        X.entrada(ws, 'C%d' % r, pob,
                  etiqueta='Población del cliente %d' % (i + 1))
        X.entrada(ws, 'D%d' % r, tipo, etiqueta='Tipo del cliente %d' % (i + 1))
        v_tipo.append('D%d' % r)
        X.entrada(ws, 'E%d' % r, canal,
                  etiqueta='Canal del cliente %d' % (i + 1))
        v_canal.append('E%d' % r)
        X.entrada(ws, 'F%d' % r, producto,
                  etiqueta='Producto del cliente %d' % (i + 1), wrap=True)
        X.entrada(ws, 'G%d' % r, FECHA_BASE, fmt=C.FMT_FECHA,
                  etiqueta='Primer suministro al cliente %d' % (i + 1))
        v_fecha.append('G%d' % r)
        X.entrada(ws, 'H%d' % r, NOSE,
                  etiqueta='RGSEAA del cliente %d' % (i + 1), align='center')
        v_rgseaa.append('H%d' % r)
        motor.f(ws, 'I%d' % r,
                ie('IF($B{r}="{lb}","",DATE(YEAR($G{r})+$C${a},MONTH($G{r}),'
                   'DAY($G{r})))'.format(r=r, lb=LIBRE, a=CL_ANOS)),
                fmt=C.FMT_FECHA)
        motor.val(ws, 'J%d' % r, nota_fila, wrap=True)
        ws.row_dimensions[r].height = 32

    C.dv_rango(ws, v_canal, refs['Canal'], 'Elige el canal',
               'Elige el canal de la lista del pie de la hoja.')
    C.dv_rango(ws, v_tipo, refs['Tipo de cliente'], 'Elige el tipo de cliente',
               'Elige el tipo de la lista del pie de la hoja. «Minorista de '
               'distinta titularidad» es el que te mete en el art. 3 del RD '
               '1021/2022.')
    C.dv_rango(ws, v_rgseaa, refs['Sí, No o No lo sé'],
               'Marca Sí, No o No lo sé',
               'Elige una de las tres opciones de la lista del pie.')
    motor.dv_fecha(ws, v_fecha)

    def res(fila, etiqueta, formula, fmt=None, nota='', bold=True):
        ws.merge_cells('A%d:D%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, etiqueta, bold=bold, wrap=True)
        motor.f(ws, 'E%d' % fila, formula, fmt=fmt, bold=bold)
        ws['E%d' % fila].fill = PatternFill('solid', fgColor=C.CREMA)
        ws.merge_cells('G%d:J%d' % (fila, fila))
        motor.val(ws, 'G%d' % fila, nota, wrap=True)
        ws['G%d' % fila].font = Font(italic=True, size=9)
        ws.row_dimensions[fila].height = 26

    C.seccion(ws, 'A%d' % CL_RES_SEC, 'Resumen del registro')
    res(CL_TOT, 'Clientes registrados',
        '=SUMPRODUCT(--($B${a}:$B${b}<>"{lb}"))'
        .format(a=CL_INI, b=CL_FIN, lb=LIBRE), C.FMT_ENT,
        'Las filas libres no cuentan: cuentan las que tienen nombre.')
    res(CL_B2B, 'De ellos, B2B de hostelería',
        '=SUMPRODUCT(--($B${a}:$B${b}<>"{lb}"),--($E${a}:$E${b}="{c}"))'
        .format(a=CL_INI, b=CL_FIN, lb=LIBRE, c=CANALES_CLI[0]), C.FMT_ENT,
        'Cafeterías, hoteles y restaurantes. Es el canal que puede meterte en '
        'el art. 3 del RD 1021/2022.')
    res(CL_CORP, 'De ellos, regalo corporativo',
        '=SUMPRODUCT(--($B${a}:$B${b}<>"{lb}"),--($E${a}:$E${b}="{c}"))'
        .format(a=CL_INI, b=CL_FIN, lb=LIBRE, c=CANALES_CLI[1]), C.FMT_ENT,
        'El canal de diciembre. Su plazo verificado es de 14 días desde la '
        'aprobación de la muestra, con mínimos de 10 a 25 cajas.')
    res(CL_MIN, 'De ellos, minoristas de DISTINTA titularidad',
        '=SUMPRODUCT(--($B${a}:$B${b}<>"{lb}"),--($D${a}:$D${b}="{c}"))'
        .format(a=CL_INI, b=CL_FIN, lb=LIBRE, c=TIPOS_CLI[2]), C.FMT_ENT,
        'Se cuenta por el TIPO de cliente, no por el canal: a una tienda '
        'gourmet se le puede servir por la misma ruta que a una cafetería y '
        'sigue siendo un minorista de distinta titularidad. Éstos son los que '
        'abren la puerta del art. 3, y si tienes al menos uno la hoja '
        '«Suministro a Otros Minoristas» del libro 8 te toca entera.')
    res(CL_RGSEAA, 'Clientes inscritos en el RGSEAA',
        '=SUMPRODUCT(--($B${a}:$B${b}<>"{lb}"),--($H${a}:$H${b}="{s}"))'
        .format(a=CL_INI, b=CL_FIN, lb=LIBRE, s=SI), C.FMT_ENT,
        'BASTA UNO para romper el requisito de «restringido» del art. 3, y los '
        'tres requisitos son acumulativos. Es la casilla más cara de esta '
        'hoja.')
    res(CL_HASTA, 'Fecha hasta la que hay que conservar el registro',
        ie('MAX($I${a}:$I${b})'.format(a=CL_INI, b=CL_FIN)), C.FMT_FECHA,
        'La del suministro más reciente más los años del parámetro. Hasta esa '
        'fecha, esta tabla es un documento, no una lista de contactos.')
    res(CL_VER, 'VEREDICTO DEL REGISTRO',
        ie('IF($E${t}=0,"Todavía no suministras a nadie: el art. 5.3.b) no te '
           'pide nada","Tienes que conservar este registro, con nombre, '
           'dirección y producto, durante los años del parámetro")'
           .format(t=CL_TOT)))
    C.destacado(ws, 'E%d' % CL_VER)
    ws.merge_cells('E%d:F%d' % (CL_VER, CL_VER))
    ws['E%d' % CL_VER].alignment = Alignment(vertical='top', wrap_text=True)
    ws.row_dimensions[CL_VER].height = 40
    X.nota_celda(ws, 'E%d' % CL_VER, 'CHN-24')
    res(CL_ART3, 'Y lo que además te cambia de régimen SANITARIO',
        ie('IF($E${m}=0,"Ninguno de tus clientes es un minorista de distinta '
           'titularidad: el art. 3 del RD 1021/2022 no te aplica",'
           'IF($E${r}>0,"Tienes un cliente inscrito en el RGSEAA: pierdes '
           '«restringido» y el art. 3 deja de ampararte","Suministras a otros '
           'minoristas: resuelve los TRES semáforos del art. 3 en el libro '
           '8"))'.format(m=CL_MIN, r=CL_RGSEAA)))
    ws.merge_cells('E%d:F%d' % (CL_ART3, CL_ART3))
    ws['E%d' % CL_ART3].alignment = Alignment(vertical='top', wrap_text=True)
    ws.row_dimensions[CL_ART3].height = 44
    X.nota_celda(ws, 'E%d' % CL_ART3, 'CHN-41')
    motor.semaforo_isnumber(ws, 'E%d' % CL_RGSEAA, '$E$%d' % CL_RGSEAA,
                            '>', '0')

    C.parrafo(ws, CL_NOTA, D.NOTA_CLIENTES_B2B, 'A', 'J', alto=76)
    C.parrafo(ws, CL_NOTA + 1,
              'ESTA TABLA CIERRA EL CÍRCULO CON LA HOJA «Checklist Legal» DEL '
              'LIBRO 8: los canales que se salen de la nota del epígrafe 644.5 '
              '-online con envío, B2B a hostelería y regalo corporativo- son '
              'justo los que hay que registrar aquí. Un mismo cliente puede '
              'costarte una pregunta al asesor fiscal y una línea en este '
              'registro.', 'A', 'J', alto=48)
    C.parrafo(ws, CL_NOTA + 2,
              'Vender online AL CONSUMIDOR FINAL no entra aquí: esto es el '
              'registro de los operadores posteriores y comerciantes a los que '
              'suministras, no el de tus compradores particulares. Y vender '
              'online a toda España tampoco rompe por sí solo el requisito de '
              '«localizado» del art. 3, que habla del suministro a otros '
              'minoristas.', 'A', 'J', alto=44)
    X.nota_celda(ws, 'A%d' % (CL_NOTA + 2), 'CHN-56')
    C.pie(ws, CL_PIE, 'A', 'C')
    ws.freeze_panes = 'C%d' % CL_INI
    C.pagina(ws, titulos='$%d:$%d' % (CL_CAB, CL_CAB),
             area='A1:J%d' % (CL_PIE + 2))
    return ws


# ==========================================================================
# Hoja «Contador»
# ==========================================================================
K_SEC1 = 5
K_CAB1 = 6
K_TOT = 7
K_NA = 8
K_ALCANCE = 9
K_INST = 10
K_RECIB = 11
K_PEDIDO = 12
K_PRESU = 13
K_PEND = 14
K_AVANCE = 15
K_SEC2 = 17
K_CAB2 = 18
K_PRESUP = 19
K_GASTADO = 20
K_PENDIENTE_EUR = 21
K_SEC3 = 23
K_CAB3 = 24
K_PROV_TOT = 25
K_PROV_SIN = 26
K_PROV_DDS = 27
K_CLI_TOT = 28
K_CLI_RG = 29
K_SEC4 = 31
K_VEREDICTO = 32
K_NOTA = 34
K_PIE = K_NOTA + 4

QEQ = "'" + H_EQ + "'!"
QPR = "'" + H_PROV + "'!"
QCL = "'" + H_CLI + "'!"


def hoja_contador(wb):
    ws = wb.create_sheet(H_CONT)
    C.anchos(ws, {'A': 58, 'B': 18, 'C': 18, 'D': 86})
    C.encabezar(ws, 'Contador: cómo va la compra',
                'Todo lo que hay aquí sale de las hojas anteriores. No se '
                'teclea nada en esta pantalla.', col_fin='D')

    def linea(fila, etiqueta, formula, fmt=None, nota='', bold=None):
        motor.val(ws, 'A%d' % fila, etiqueta, wrap=True, bold=bold)
        motor.f(ws, 'B%d' % fila, formula, fmt=fmt, bold=bold)
        if nota:
            C.nota(ws, 'D%d' % fila, nota)
        return 'B%d' % fila

    C.seccion(ws, 'A%d' % K_SEC1, 'Avance del equipamiento')
    C.cabecera(ws, K_CAB1, [('A', 'Concepto'), ('B', 'Valor'), ('C', ''),
                            ('D', 'Notas')], altura=20)
    rango_estado = '{q}$A${a}:$A${b}'.format(q=QEQ, a=EQ_INI, b=EQ_FIN)
    linea(K_TOT, 'Líneas de equipamiento',
          "={q}I{r}".format(q=QEQ, r=R_LINEAS), C.FMT_ENT,
          'Las diecisiete de la dotación, opcionales incluidas.')
    linea(K_NA, 'Líneas marcadas como N/A',
          ie('COUNTIF({r},"{e}")'.format(r=rango_estado, e=ESTADOS[5])),
          C.FMT_ENT, 'Las que has decidido que no te tocan.')
    linea(K_ALCANCE, 'Líneas que de verdad vas a comprar',
          ie('B{t}-B{n}'.format(t=K_TOT, n=K_NA)), C.FMT_ENT, bold=True,
          nota='Es el denominador del avance: lo que no vas a comprar no '
               'puede contar como pendiente.')
    for fila, estado in ((K_INST, ESTADOS[4]), (K_RECIB, ESTADOS[3]),
                         (K_PEDIDO, ESTADOS[2]), (K_PRESU, ESTADOS[1]),
                         (K_PEND, ESTADOS[0])):
        linea(fila, 'Líneas en estado «%s»' % estado,
              ie('COUNTIF({r},"{e}")'.format(r=rango_estado, e=estado)),
              C.FMT_ENT)
    linea(K_AVANCE, 'Avance de la compra (%)',
          ie('IF(B{a}=0,"",B{i}/B{a})'.format(a=K_ALCANCE, i=K_INST)),
          C.FMT_PCT, bold=True,
          nota='Sólo cuenta «%s»: una máquina pedida y no montada no produce '
               'ni un bombón.' % ESTADO_FINAL)
    motor.semaforo_isnumber(ws, 'B%d' % K_AVANCE, '$B$%d' % K_AVANCE,
                            '<', '1', bg=motor.CF_AMBAR_BG,
                            fg=motor.CF_AMBAR_FG)

    C.seccion(ws, 'A%d' % K_SEC2, 'El dinero')
    C.cabecera(ws, K_CAB2, [('A', 'Concepto'), ('B', 'Importe'), ('C', ''),
                            ('D', 'Notas')], altura=20)
    linea(K_PRESUP, 'Presupuesto de referencia sin IVA, todas las líneas (€)',
          '={q}I{r}'.format(q=QEQ, r=R_REF_TODO), C.FMT_EUR)
    linea(K_GASTADO, 'Compromiso real negociado sin IVA (€)',
          '={q}I{r}'.format(q=QEQ, r=R_REAL_TODO), C.FMT_EUR)
    linea(K_PENDIENTE_EUR, 'Diferencia (real menos referencia, €)',
          ie('B{g}-B{p}'.format(g=K_GASTADO, p=K_PRESUP)), C.FMT_EUR,
          bold=True,
          nota='Negativo es buena noticia: has negociado por debajo de la '
               'referencia.')
    motor.semaforo_isnumber(ws, 'B%d' % K_PENDIENTE_EUR,
                            '$B$%d' % K_PENDIENTE_EUR, '>', '0')

    C.seccion(ws, 'A%d' % K_SEC3, 'Los papeles')
    C.cabecera(ws, K_CAB3, [('A', 'Concepto'), ('B', 'Valor'), ('C', ''),
                            ('D', 'Notas')], altura=20)
    linea(K_PROV_TOT, 'Proveedores publicados',
          '={q}F{r}'.format(q=QPR, r=PR_TOT), C.FMT_ENT)
    linea(K_PROV_SIN, 'Proveedores sin clasificar en la cadena EUDR',
          '={q}F{r}'.format(q=QPR, r=PR_SINPAPEL), C.FMT_ENT,
          nota='Una pregunta de dos líneas en un correo.')
    linea(K_PROV_DDS, 'Operadores que te deben su nº de DDS',
          '={q}F{r}'.format(q=QPR, r=PR_DDS), C.FMT_ENT,
          nota='Sólo los operadores: a los demás no se les pide.')
    linea(K_CLI_TOT, 'Clientes registrados (art. 5.3.b)',
          '={q}E{r}'.format(q=QCL, r=CL_TOT), C.FMT_ENT)
    linea(K_CLI_RG, 'Clientes inscritos en el RGSEAA',
          '={q}E{r}'.format(q=QCL, r=CL_RGSEAA), C.FMT_ENT,
          nota='Basta uno para perder «restringido» en el art. 3.')
    motor.semaforo_isnumber(ws, 'B%d' % K_PROV_SIN, '$B$%d' % K_PROV_SIN,
                            '>', '0', bg=motor.CF_AMBAR_BG,
                            fg=motor.CF_AMBAR_FG)
    motor.semaforo_isnumber(ws, 'B%d' % K_PROV_DDS, '$B$%d' % K_PROV_DDS,
                            '>', '0')
    motor.semaforo_isnumber(ws, 'B%d' % K_CLI_RG, '$B$%d' % K_CLI_RG,
                            '>', '0')

    C.seccion(ws, 'A%d' % K_SEC4, 'Lo que falta para abrir')
    motor.val(ws, 'A%d' % K_VEREDICTO, 'VEREDICTO', bold=True)
    motor.f(ws, 'B%d' % K_VEREDICTO,
            ie('IF(B{a}<1,"Todavía te falta equipo por instalar: mira la '
               'columna del plazo crítico antes de fijar la fecha",'
               'IF(B{d}>0,"El equipo está, pero te faltan papeles del EUDR",'
               '"Equipo instalado y papeles coherentes: la fecha ya no depende '
               'de la maquinaria"))'.format(a=K_AVANCE, d=K_PROV_DDS)),
            bold=True)
    ws.merge_cells('B%d:D%d' % (K_VEREDICTO, K_VEREDICTO))
    ws['B%d' % K_VEREDICTO].alignment = Alignment(vertical='top',
                                                  wrap_text=True)
    ws.row_dimensions[K_VEREDICTO].height = 40
    C.destacado(ws, 'B%d' % K_VEREDICTO)

    C.parrafo(ws, K_NOTA,
              'El plazo crítico de entrega -la celda «Plazo crítico de '
              'entrega (semanas)» de la hoja «Equipamiento»- es el dato que se '
              'copia en el cronograma del libro '
              '«checklist-legal-licencias-y-cacao.xlsx». Si tu ruta crítica de '
              'papeleo es más corta que ese plazo, la fecha de apertura la '
              'manda la maquinaria, no el ayuntamiento.', 'A', 'D', alto=48)
    C.parrafo(ws, K_NOTA + 1,
              'Y al revés: si el plazo crítico baja porque encuentras la '
              'máquina en stock, la fecha vuelve a mandarla el papeleo. Los '
              'dos libros hay que mirarlos juntos una vez por semana.',
              'A', 'D', alto=32)
    C.pie(ws, K_PIE, 'A', 'C')
    C.pagina(ws, apaisado=False, area='A1:D%d' % (K_PIE + 2))
    return ws


# ==========================================================================
# Mapa de celdas citables
# ==========================================================================
def mapa_celdas():
    m = [
        ('Tipo de IVA general del equipamiento', H_EQ, 'C%d' % P_IVA,
         'parametro'),
        ('Horquilla del precio de referencia', H_EQ, 'C%d' % P_HORQ,
         'parametro'),
        ('Umbral de desviación admitida', H_EQ, 'C%d' % P_UMBRAL, 'parametro'),
        ('Semanas hasta la apertura prevista', H_EQ, 'C%d' % P_SEM, 'entrada'),
        ('Margen de seguridad entre entrega y apertura', H_EQ,
         'C%d' % P_MARGEN, 'entrada'),
        ('Líneas del checklist de equipamiento', H_EQ, 'I%d' % R_LINEAS,
         'salida'),
        ('Total de referencia sin IVA, sólo líneas críticas', H_EQ,
         'I%d' % R_REF_CRIT, 'salida'),
        ('Total de referencia sin IVA, todas las líneas', H_EQ,
         'I%d' % R_REF_TODO, 'salida'),
        ('Total real negociado sin IVA, sólo líneas críticas', H_EQ,
         'I%d' % R_REAL_CRIT, 'salida'),
        ('Total real negociado sin IVA, todas las líneas', H_EQ,
         'I%d' % R_REAL_TODO, 'salida'),
        ('Lo ganado o perdido negociando', H_EQ, 'I%d' % R_NEGOCIA, 'salida'),
        ('IVA soportado sobre el precio real', H_EQ, 'I%d' % R_IVA_SOP,
         'salida'),
        ('Desembolso real con IVA', H_EQ, 'I%d' % R_DESEMB, 'salida'),
        ('Líneas que sólo pueden publicarse como rango', H_EQ,
         'I%d' % R_RANGOS, 'salida'),
        ('Líneas que son un «desde» y hay que presupuestar', H_EQ,
         'I%d' % R_DESDE, 'salida'),
        ('CAPEX del bloque de templado traído del libro 2 (celda verde del '
         'cruce)', H_EQ, 'I%d' % CR_VERDE, 'entrada'),
        ('Lo que suman tus líneas críticas del bloque de templado', H_EQ,
         'I%d' % CR_REAL, 'salida'),
        ('Desviación contra el CAPEX del libro 2 (€)', H_EQ, 'I%d' % CR_DIF,
         'salida'),
        ('Desviación contra el CAPEX del libro 2 (%)', H_EQ, 'I%d' % CR_PCT,
         'salida'),
        ('CUADRE contra el CAPEX del libro 2', H_EQ, 'I%d' % CR_CUADRE,
         'salida'),
        ('PLAZO CRÍTICO DE ENTREGA (semanas) — viaja al libro 8', H_EQ,
         'I%d' % R_PLAZO, 'salida'),
        ('Línea que marca el plazo crítico', H_EQ, 'I%d' % R_PLAZO_LIN,
         'salida'),
        ('Margen del plazo crítico (semanas)', H_EQ, 'I%d' % R_MARGEN,
         'salida'),
        ('Veredicto del plazo', H_EQ, 'I%d' % R_VER_PLAZO, 'salida'),
        ('Líneas cuyo plazo se pasa de la apertura', H_EQ, 'I%d' % R_TARDE,
         'salida'),
        ('Precio de referencia de la atemperadora continua', H_EQ,
         'I%d' % EQ_INI, 'salida'),
        ('Precio de la atemperadora continua en base imponible', H_EQ,
         'L%d' % EQ_INI, 'salida'),
        ('Plazo de entrega de la atemperadora continua', H_EQ,
         'R%d' % EQ_INI, 'entrada'),
        ('Variante del formato elegida', H_VAR, 'C%d' % V_ELIGE, 'entrada'),
        ('Equipos del tren bean-to-bar que dices necesitar', H_VAR,
         'C%d' % V_BTB_TOT, 'salida'),
        ('Preguntas al fabricante de bean-to-bar contestadas', H_VAR,
         'C%d' % V_PRE_TOT, 'salida'),
        ('Veredicto del bean-to-bar', H_VAR, 'C%d' % V_BTB_VER, 'salida'),
        ('Precio verificado de la chocolatera de taza', H_VAR,
         'C%d' % V_TAZA_INI, 'salida'),
        ('Proveedores publicados', H_PROV, 'F%d' % PR_TOT, 'salida'),
        ('Proveedores con los que ya trabajas', H_PROV, 'F%d' % PR_TRAB,
         'salida'),
        ('Proveedores que son OPERADORES del EUDR', H_PROV, 'F%d' % PR_OPER,
         'salida'),
        ('Proveedores que son operadores posteriores', H_PROV,
         'F%d' % PR_POST, 'salida'),
        ('Proveedores que son comerciantes', H_PROV, 'F%d' % PR_COM, 'salida'),
        ('Proveedores sin clasificar en la cadena', H_PROV,
         'F%d' % PR_SINPAPEL, 'salida'),
        ('Operadores que te deben el nº de su DDS', H_PROV, 'F%d' % PR_DDS,
         'salida'),
        ('Proveedores sin boletín de cadmio', H_PROV, 'F%d' % PR_CADMIO,
         'salida'),
        ('Proveedores sin boletín de HAP', H_PROV, 'F%d' % PR_HAP, 'salida'),
        ('Pedido mínimo acumulado de todos los proveedores', H_PROV,
         'F%d' % PR_MIN, 'salida'),
        ('Plazo medio de entrega de los proveedores', H_PROV,
         'F%d' % PR_PLAZO, 'salida'),
        ('Veredicto de la documentación de proveedores', H_PROV,
         'F%d' % PR_VER, 'salida'),
        ('Papeles que le tocan al primer proveedor', H_PROV, 'N%d' % PR_INI,
         'salida'),
        ('Años de conservación del registro de clientes', H_CLI,
         'C%d' % CL_ANOS, 'parametro'),
        ('Clientes registrados', H_CLI, 'E%d' % CL_TOT, 'salida'),
        ('Clientes de B2B de hostelería', H_CLI, 'E%d' % CL_B2B, 'salida'),
        ('Clientes de regalo corporativo', H_CLI, 'E%d' % CL_CORP, 'salida'),
        ('Clientes minoristas de distinta titularidad', H_CLI, 'E%d' % CL_MIN,
         'salida'),
        ('Clientes inscritos en el RGSEAA', H_CLI, 'E%d' % CL_RGSEAA,
         'salida'),
        ('Fecha hasta la que hay que conservar el registro', H_CLI,
         'E%d' % CL_HASTA, 'salida'),
        ('Veredicto del registro de clientes', H_CLI, 'E%d' % CL_VER,
         'salida'),
        ('Lo que el registro de clientes cambia en tu régimen sanitario',
         H_CLI, 'E%d' % CL_ART3, 'salida'),
        ('Conservar hasta, del primer cliente', H_CLI, 'I%d' % CL_INI,
         'salida'),
        ('Líneas que de verdad vas a comprar', H_CONT, 'B%d' % K_ALCANCE,
         'salida'),
        ('Avance de la compra', H_CONT, 'B%d' % K_AVANCE, 'salida'),
        ('Diferencia entre lo real y la referencia', H_CONT,
         'B%d' % K_PENDIENTE_EUR, 'salida'),
        ('Veredicto de la compra', H_CONT, 'B%d' % K_VEREDICTO, 'salida'),
    ]
    return m


NOTAS_MAPA = (
    'Libro 9 de la guía. El plazo crítico de entrega (hoja «' + H_EQ + '») es '
    'la celda que viaja al cronograma del libro 8 por CELDA VERDE con fila de '
    'cuadre: cero fórmulas que nombren otro fichero. La desviación contra el '
    'CAPEX llega en sentido contrario, desde el libro 2, con el mismo '
    'mecanismo. El número de referencia de la declaración de diligencia debida '
    'SÓLO se le pide al proveedor que es OPERADOR (art. 5.3.a del EUDR, '
    '`CHN-24`): está prohibido escribir «pide a todos tus proveedores el '
    'número de su DDS». Y está prohibido escribir «basta con registrar a tus '
    'proveedores»: el art. 5.3.b) obliga además a registrar a los operadores '
    'posteriores y comerciantes a los que TÚ suministras, y a conservarlo '
    'cinco años. Los precios sin id `CHS-*` son supuestos declarados y los '
    'plazos de entrega lo son todos: ningún distribuidor los publica.')


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

    # 1. La base fiscal manda: una línea «con IVA» se divide y una «sin IVA»
    #    no. Con la dotación real las diecisiete están declaradas «sin IVA» o
    #    «no declarada», así que L == I en todas.
    malas = []
    for i in range(N_EQ):
        r = EQ_INI + i
        bruto, neto = v(H_EQ, 'I%d' % r), v(H_EQ, 'L%d' % r)
        if abs(bruto - neto) > 0.01:
            malas.append(EQUIPOS[i]['n'])
    prueba('ninguna línea de la dotación parte de una base «con IVA», así que '
           'el precio sin IVA coincide con el de referencia', not malas,
           'difieren %r' % (malas,))
    exc_b = ExcelCompiler(ruta)
    exc_b.evaluate("'%s'!L%d" % (H_EQ, EQ_INI))
    exc_b.set_value("'%s'!J%d" % (H_EQ, EQ_INI), BASES_IVA[1])
    neto_b = exc_b.evaluate("'%s'!L%d" % (H_EQ, EQ_INI))
    prueba('al declarar la atemperadora «con IVA», su base imponible baja un '
           '21 %', neto_b < v(H_EQ, 'I%d' % EQ_INI) * 0.85,
           '%.2f euros' % neto_b)

    # 2. El plazo crítico sale de las líneas CRÍTICAS, no de las opcionales.
    plazo = v(H_EQ, 'I%d' % R_PLAZO)
    esperado = D.plazo_critico_semanas()
    prueba('el plazo crítico es el de las líneas críticas y coincide con el '
           'juego de datos', plazo == esperado,
           '%r frente a %r semanas' % (plazo, esperado))
    exc_c = ExcelCompiler(ruta)
    exc_c.evaluate("'%s'!I%d" % (H_EQ, R_PLAZO))
    opcional = next(EQ_INI + i for i, e in enumerate(EQUIPOS) if e['opcional'])
    exc_c.set_value("'%s'!R%d" % (H_EQ, opcional), 80)
    prueba('subir a 80 semanas el plazo de una línea OPCIONAL no mueve el '
           'plazo crítico',
           exc_c.evaluate("'%s'!I%d" % (H_EQ, R_PLAZO)) == esperado)

    # 3. D48: el número de DDS sólo se exige en la rama «operador». B1
    # (refutación 2026-09-12): el papel EUDR ya NO nace sembrado como
    # «operador posterior» a mano -eso era el defecto-, así que el estado de
    # PARTIDA del proveedor 1 (Callebaut) es «No lo sé» y se prueba
    # tocándolo con pycel, evaluando la salida ANTES de tocar la entrada.
    n0 = v(H_PROV, 'N%d' % PR_INI)
    o0 = v(H_PROV, 'O%d' % PR_INI)
    prueba('con el papel sin resolver, no se afirma ni se pide el nº de DDS',
           'Pregúntaselo por escrito' in n0, '%r / %r' % (n0, o0))
    exc_d = ExcelCompiler(ruta)
    exc_d.evaluate("'%s'!N%d" % (H_PROV, PR_INI))
    exc_d.evaluate("'%s'!O%d" % (H_PROV, PR_INI))
    exc_d.set_value("'%s'!G%d" % (H_PROV, PR_INI), D.PAPELES_EUDR[1])
    n_posterior = exc_d.evaluate("'%s'!N%d" % (H_PROV, PR_INI))
    o_posterior = exc_d.evaluate("'%s'!O%d" % (H_PROV, PR_INI))
    prueba('a un operador POSTERIOR no se le pide el nº de DDS',
           'NO se le pide' in n_posterior and 'FALTA el nº' not in o_posterior,
           '%r / %r' % (n_posterior, o_posterior))
    exc_d.set_value("'%s'!G%d" % (H_PROV, PR_INI), D.PAPELES_EUDR[0])
    n1 = exc_d.evaluate("'%s'!N%d" % (H_PROV, PR_INI))
    o1 = exc_d.evaluate("'%s'!O%d" % (H_PROV, PR_INI))
    prueba('al marcarlo como OPERADOR, el semáforo sí le reclama el nº de DDS',
           'nº de referencia de su DDS' in n1 and 'FALTA el nº' in o1,
           '%r / %r' % (n1, o1))

    # 4. El cruce 9 <- 2 cuadra de fábrica y se rompe al pisar un precio.
    cuadre = v(H_EQ, 'I%d' % CR_CUADRE)
    prueba('el CUADRE contra el CAPEX del libro 2 nace en verde',
           cuadre.startswith('CUADRA'), '%r' % (cuadre,))
    exc_e = ExcelCompiler(ruta)
    exc_e.evaluate("'%s'!I%d" % (H_EQ, CR_CUADRE))
    exc_e.set_value("'%s'!O%d" % (H_EQ, EQ_INI), 14000)
    prueba('al pagar 14.000 euros por la atemperadora, el CUADRE salta',
           exc_e.evaluate("'%s'!I%d" % (H_EQ, CR_CUADRE)).startswith('NO '
                                                                     'CUADRA'))

    # 5. El registro de clientes cuenta sólo las filas con nombre y calcula la
    #    conservación a cinco años.
    total_cli = v(H_CLI, 'E%d' % CL_TOT)
    prueba('el registro cuenta los cuatro clientes sembrados y no las filas '
           'libres', total_cli == len(D.CLIENTES_B2B), '%r' % (total_cli,))
    # pycel devuelve las fechas como número de serie de Excel (base 1899-12-30).
    hasta = v(H_CLI, 'I%d' % CL_INI)
    if not hasattr(hasta, 'year'):
        hasta = (datetime.date(1899, 12, 30)
                 + datetime.timedelta(days=int(hasta)))
    prueba('la fecha de conservación del primer cliente son cinco años más '
           'tarde',
           hasta.year == FECHA_BASE.year + ANOS_CONSERVACION
           and (hasta.month, hasta.day) == (FECHA_BASE.month, FECHA_BASE.day),
           '%s' % hasta.isoformat())
    exc_f = ExcelCompiler(ruta)
    exc_f.evaluate("'%s'!E%d" % (H_CLI, CL_RGSEAA))
    exc_f.evaluate("'%s'!E%d" % (H_CLI, CL_ART3))
    exc_f.set_value("'%s'!H%d" % (H_CLI, CL_INI), SI)
    art3 = exc_f.evaluate("'%s'!E%d" % (H_CLI, CL_ART3))
    prueba('con un cliente inscrito en el RGSEAA, la hoja avisa de que pierdes '
           '«restringido»', 'restringido' in art3, '%r' % (art3,))

    return ok, fallos


# ==========================================================================
def main():
    D.gate_legal(IDS_LEGALES)
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_equipamiento(wb)
    hoja_variante(wb)
    hoja_proveedores(wb)
    hoja_clientes(wb)
    hoja_contador(wb)

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
