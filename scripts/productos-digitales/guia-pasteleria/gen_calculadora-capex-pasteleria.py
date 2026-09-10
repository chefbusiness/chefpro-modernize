#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_calculadora-capex-pasteleria.py — libro 2 de «Cómo Montar una Pastelería»
(SPEC §2.2 fila 2; decisiones D17, D21 y D22).

Hojas: Instrucciones · Parámetros · CAPEX por Bloque · Variante del Formato ·
Traspaso vs Obra Nueva · IVA y Tesorería · Resumen.

QUÉ DECIDE ESTE LIBRO
---------------------
Cuánto dinero necesitas de verdad para abrir, y si sale mejor un traspaso o
una obra nueva. Las dos preguntas se contestan mal por el mismo motivo: se
suman precios que unos llevan IVA y otros no, y se compara el precio de un
traspaso con el coste de una obra sin meter la renta de los años siguientes.

LO QUE NO HACE, Y DÓNDE SE HACE
-------------------------------
* **No es el checklist de compra.** A quién le compras cada máquina, a qué
  precio real la negocias y en cuántas semanas te la sirven es el libro 7. Aquí
  la máquina entra sólo por su importe.
* **No es el plan financiero.** Los gastos fijos mensuales entran como UN
  parámetro para calcular el fondo de maniobra; el P&L a tres años, la
  tesorería mes a mes y el servicio de la deuda son el libro 5.
* **No calcula capacidad.** Si ese equipo da las piezas que necesitas, y si el
  local sirve, es el libro 1.

DECISIONES TÉCNICAS
-------------------
* **La columna de IVA es lo que hace que la suma signifique algo (D17).** Cada
  línea declara si el importe que has escrito lleva IVA y a qué tipo, y la
  hoja lleva TODAS a base imponible antes de sumar. Sin eso, mezclar una ficha
  publicada con IVA (el horno UNOX) con otra publicada sin él (el abatidor
  Irinox) desvía el CAPEX un 21 % y nadie lo ve. Las tasas municipales y la
  comunicación al registro autonómico van a tipo 0: no llevan IVA.
* **Las líneas sin precio publicado NO se rellenan a ojo en silencio (D21).**
  Traen un valor por defecto declarado como supuesto, con la horquilla
  publicada al lado cuando existe, y la nota dice que pidas tres presupuestos.
  Ninguna celda verde queda vacía y ninguna finge ser un precio de ficha.
* **La obra civil y el fondo de maniobra son FÓRMULA, no importe tecleado:**
  la obra sale de los metros por el precio del escenario elegido, y el fondo,
  de los meses de colchón por los gastos fijos. Cambiar el escenario recalcula
  el libro entero.
* **El comparador de traspaso mete la renta dentro.** Un traspaso de 43.000 €
  con 1.250 €/mes cuesta a cinco años bastante más que su precio, y una obra
  nueva paga renta desde que empieza la obra y todavía no factura. Los dos
  lados llevan sus meses parados. Y la tabla dice a la cara que son precios
  PEDIDOS en un anuncio, no precios pagados.
* Cero constantes dentro de las fórmulas; `IFERROR(...,"")` en toda división;
  «sin dato» = `""`; semáforos con `ISNUMBER`; desplegables contra RANGO;
  prohibidas `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`,
  `LAMBDA`, `RANK`, `NETWORKDAYS` e `IRR`: cero usos. Textos WinAnsi (cp1252).

Salida fija: build/calculadora-capex-pasteleria.xlsx + su mapa de celdas.
Via: Claude Code
"""
import json
import os
import subprocess
import sys

import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..'))
sys.path.insert(0, os.path.join(RAIZ, 'guias-v2_0'))
sys.path.insert(0, AQUI)

import motor                                                   # noqa: E402
import datos_ejemplo as D                                      # noqa: E402
import _comun_pasteleria as C                                  # noqa: E402

motor.CTX['producto'] = C.PID

NOMBRE = 'calculadora-capex-pasteleria'
TITULO = 'Calculadora de inversión inicial (CAPEX)'

H_PAR = 'Parámetros'
H_CAP = 'CAPEX por Bloque'
H_VAR = 'Variante del Formato'
H_TRA = 'Traspaso vs Obra Nueva'
H_IVA = 'IVA y Tesorería'
H_RES = 'Resumen'

IDS_LEGALES = {
    'PA-04': ('La comunicación al registro autonómico no es una licencia', 2),
    'PA-36': ('IVA: el 10 % de la pastelería y la lista cerrada del 4 %', 2),
    'PA-37': ('Verifactu: el software que compres ya tiene que estar adaptado', 2),
    'PA-13': ('El abatidor del art. 5: un arcón no vale', 2),
    'PA-07b': ('El aire de la campana es AE4 y no comparte conducto', 2),
}

SI_NO = ('Sí', 'No')
ESCENARIOS = ('Bajo', 'Medio', 'Alto')

BLOQUES = ('Obra civil e instalaciones', 'Equipamiento de obrador',
           'Tienda y vitrina', 'Licencias y proyecto técnico',
           'Fianza y garantías', 'Packaging inicial', 'Marketing de apertura',
           'Fondo de maniobra')
#: Los cinco bloques que entran en la comparación con el escenario publicado
#: (PS-85h): la fianza es un depósito, el packaging son existencias y el fondo
#: de maniobra es caja. Compararlos contra un presupuesto de obra y
#: equipamiento sería comparar dos cosas distintas.
BLOQUES_COMPARABLES = ('Obra civil e instalaciones', 'Equipamiento de obrador',
                       'Tienda y vitrina', 'Licencias y proyecto técnico',
                       'Marketing de apertura')
ESCENARIO_PUBLICADO = 137000.0          # PS-85h

#: Horquilla publicada por línea de equipamiento, cuando la hay. No es un
#: precio: es lo que el research encontró dicho, con su id.
HORQUILLA = {
    9: 'Sin precio publicado: Salva vende por presupuesto (PS-73)',
    10: 'Hasta 19.438 € en la gama alta de la categoría (PS-83)',
    11: '«Puede superar los 6.000 €» (PS-84)',
    12: '4.000-8.000 € para «amasadora industrial», sin marca (PS-75)',
    13: '7.000-15.000 € para «vitrinas refrigeradas», sin marca (PS-75)',
}


# --------------------------------------------------------------------------
# Parámetros
# --------------------------------------------------------------------------
P_INI = 6
PARAMS_LIBRO = [
    ('Superficie total del local', D.NEGOCIO['m2_total'], 'm2',
     D.NEGOCIO['fuente_m2'],
     'Los mismos 90 m2 del libro 1. Es la superficie del caso publicado sobre '
     'la que casan los tres escenarios de obra: con 110 m2 el escenario medio '
     'se iría a 99.000 € y toda la comparación cambiaría.'),
    ('Obra civil, escenario bajo', D.ESCENARIOS_OBRA['Bajo'][0], '€/m2',
     'PS-85a', 'Local que ya venía de un uso alimentario y sólo hay que '
     'adecuar.'),
    ('Obra civil, escenario medio', D.ESCENARIOS_OBRA['Medio'][0], '€/m2',
     'PS-85b', 'Local diáfano en bruto: instalaciones nuevas, sin sorpresas '
     'estructurales. Es el escenario de referencia.'),
    ('Obra civil, escenario alto', D.ESCENARIOS_OBRA['Alto'][0], '€/m2',
     'PS-85c', 'Local con refuerzos, acometidas nuevas, patinillo de humos '
     'que hay que abrir o protección del edificio.'),
    ('Escenario de obra elegido', D.ESCENARIO_OBRA_BASE, 'Bajo, Medio o Alto',
     'supuesto',
     'Cámbialo y se recalculan la obra civil, el CAPEX, la comparación con el '
     'traspaso y el IVA soportado.'),
    ('Precio por m2 aplicado', None, '€/m2', 'Se calcula',
     'El del escenario que hayas elegido arriba.'),
    ('Obra civil calculada', None, '€', 'Se calcula',
     'Superficie × precio por m2. Es la única partida del CAPEX que no se '
     'teclea: sale del escenario.'),
    ('IVA general', D.P('iva_general'), '%', 'art. 90.Uno de la Ley 37/1992',
     'Tipo general: obra, equipamiento, mobiliario, proyecto y marketing. Es '
     'el valor por defecto de la columna «tipo de IVA» de cada línea, pero '
     'cada línea tiene el suyo.'),
    ('IVA de la pastelería que vas a vender', D.P('iva_producto'), '%',
     'PA-36',
     'No entra en el CAPEX: está aquí porque es el IVA que repercutirás y '
     'contra el que se compensa el que adelantas ahora. Bollería, pastelería, '
     'confitería y repostería van al 10 % por la regla general de alimentos.'),
    ('IVA de tasas y trámites', 0.0, '%', 'supuesto',
     'Las tasas municipales y la comunicación al registro autonómico no llevan '
     'IVA. Se declara como parámetro para que la columna de la hoja de CAPEX '
     'no tenga que hacer una excepción escondida.'),
    ('Meses de colchón de tesorería', D.P('meses_colchon_fondo_maniobra'),
     'meses', 'supuesto',
     'Meses de gastos fijos que tienes que tener en caja el día que abres. Es '
     'una partida del CAPEX, no una propina: sin ella, el negocio depende de '
     'facturar desde el primer día, que es justo lo que no pasa.'),
    # Hallazgo A6 (2026-09-10): el «3» del veredicto de caja estaba tecleado
    # dentro de la fórmula (IF(B27<3,...)) en vez de venir de un parámetro, y
    # además el aviso salía muerto de fábrica (B27 = B16 por construcción, así
    # que con el B16 por defecto nunca podía decir «te falta colchón»). Se
    # separa el umbral del veredicto (este parámetro) de los meses de colchón
    # que se USAN para dotar el fondo de maniobra (el de arriba): así el
    # lector puede bajar sus meses reales de colchón sin que el aviso quede
    # inerte.
    ('Colchón mínimo aceptable antes de avisar (meses)', 3, 'meses',
     'supuesto',
     'Umbral del veredicto de caja de más abajo. Si tu banco exige más, súbelo '
     'aquí; no lo cambies confundiéndolo con los meses que de verdad dotas '
     'arriba.'),
    ('Gastos fijos mensuales estimados', round(D.gastos_fijos_mensuales(), 2),
     '€/mes', 'supuesto',
     'Personal con Seguridad Social, retribución del propietario, alquiler, '
     'suministros, seguros, gestoría, amortización e intereses DEL AÑO 1 '
     '(la carga máxima, antes de que corra la carencia). Es un valor por '
     'defecto para que el fondo de maniobra tenga un número: el cálculo '
     'bueno, mes a mes -con el interés del año de crucero, más bajo-, es el '
     'libro 5 (plan-financiero-3-anos-pasteleria.xlsx). Por eso el CAPEX y el '
     'fondo de maniobra de este libro difieren en unos 134 € de los del '
     'libro 5: para citar la INVERSIÓN TOTAL, usa siempre el libro 5, no '
     'éste.'),
    ('Fondo de maniobra calculado', None, '€', 'Se calcula',
     'Meses de colchón × gastos fijos mensuales.'),
    ('Renta mensual del local', D.NEGOCIO['renta_mensual'], '€/mes',
     D.NEGOCIO['fuente_renta'], D.NEGOCIO['nota_renta']),
    ('Meses de fianza', D.NEGOCIO['meses_fianza'], 'meses',
     D.NEGOCIO['fuente_fianza'],
     'La fianza no es un gasto: es un depósito que se recupera. Va en el CAPEX '
     'porque hay que tenerla el día de la firma.'),
    ('Horizonte de comparación', D.HORIZONTE_COMPARACION_ANIOS, 'años',
     D.FUENTE_HORIZONTE,
     'Años sobre los que se compara el traspaso con la obra nueva. Cinco es lo '
     'habitual de un contrato con obligado cumplimiento; ponle los del tuyo.'),
    ('Periodicidad de la declaración de IVA', 3, 'meses', 'supuesto',
     'Trimestral en el régimen general de una pastelería que arranca. Si te '
     'inscribes en el registro de devolución mensual, esto es 1 y el IVA de la '
     'inversión vuelve mucho antes.'),
    ('Meses hasta recuperar el IVA de la inversión', 4, 'meses', 'supuesto',
     'El trimestre en el que compras más el plazo de presentación. Y ojo: en '
     'régimen general lo normal no es que te lo devuelvan, es que lo compenses '
     'contra el IVA que repercutes, así que tarda lo que tardes en facturar.'),
    ('Financiación bancaria disponible', D.FINANCIACION['principal'], '€',
     D.FINANCIACION['fuente'], D.FINANCIACION['nota']),
]
P_M2, P_BAJO, P_MEDIO, P_ALTO, P_ESC, P_EURM2, P_OBRA = 0, 1, 2, 3, 4, 5, 6
P_IVA_GEN, P_IVA_PROD, P_IVA_CERO = 7, 8, 9
P_MESES_COL, P_COLCHON_MIN, P_FIJOS, P_FONDO = 10, 11, 12, 13
P_RENTA, P_FIANZA, P_HORIZ, P_PERIOD, P_MESES_IVA, P_FINAN = 14, 15, 16, 17, 18, 19


def fp(i):
    return P_INI + i


# --------------------------------------------------------------------------
# Las 10 variantes de formato (PS-01 a PS-09 y PS-11: PS-10 no existe en el
# JSON de research). Los coeficientes son SUPUESTOS declarados y editables:
# desvían el caso central de «La Clara», que es PS-05. Las dos columnas de
# «publicado» sí son cifras del research, y por eso NO son celdas verdes.
#
# (nombre, id, coef obra, equip, tienda, licencias, otros, pub_min, pub_max,
#  qué cambia además)
# --------------------------------------------------------------------------
V_INI = 15
VARIANTES = [
    ('Pastelería mediana: obrador propio y despacho a calle (el caso de este '
     'libro)', 'PS-05', 1.00, 1.00, 1.00, 1.00, 1.00, 100000.0, 150000.0,
     'Es el caso central: todos los coeficientes valen 1,00, así que la '
     'inversión de apertura es exactamente el CAPEX total de la hoja anterior '
     'menos el fondo de maniobra, y la columna de la derecha se lo suma otra '
     'vez para devolver el total.'),
    ('Obrador en casa, venta directa al consumidor final', 'PS-01',
     0.05, 0.15, 0.00, 0.10, 0.20, 3000.0, 30000.0,
     'No es un local: es tu vivienda, con la lista cerrada del art. 13.8 del '
     'RD 1021/2022 y el matiz autonómico de la letra e). Comunicación al '
     'registro autonómico, NO inscripción en el RGSEAA. Sin obra, sin tienda '
     'y sin fianza; la hoja «Ruta Doméstica» del libro 6 es la que manda.'),
    ('Obrador a puerta cerrada, sólo producción', 'PS-02',
     0.45, 0.45, 0.00, 0.60, 0.50, 8000.0, 20000.0,
     'Sin escaparate ni mobiliario de venta, pero con el umbral del art. 3 '
     'encima en cuanto suministres a otros minoristas de distinta '
     'titularidad. El árbol del art. 3 está en el libro 6.'),
    ('Local con venta o despacho, sin obrador propio', 'PS-03',
     0.35, 0.10, 1.00, 0.70, 0.60, 15000.0, 50000.0,
     'Compras elaborado o semielaborado: casi todo el equipamiento de obrador '
     'desaparece y la vitrina se queda entera. Si no fabricas, no puedes usar '
     'la mención «elaboración propia» (art. 11 del RD 1021/2022).'),
    ('Cafetería-pastelería con obrador', 'PS-04',
     1.25, 1.05, 1.60, 1.30, 1.20, 60000.0, 100000.0,
     'Suma sala, barra, máquina de café y aseos de público. En cuanto hay '
     'comidas preparadas cambian el marco sanitario, probablemente el '
     'convenio y el IVA aplicable en la zona de degustación, que es del 10 % '
     'por ser servicio de hostelería.'),
    ('Punto caliente pequeño', 'PS-06',
     0.55, 0.30, 1.00, 0.70, 0.70, 60000.0, 100000.0,
     'Regenera producto congelado: hornos y vitrina sí, obrador de verdad no. '
     'No fabrica, así que tampoco puede decir «elaboración propia».'),
    ('Local céntrico o grande', 'PS-07',
     1.80, 1.30, 1.80, 1.40, 1.50, 150000.0, 250000.0,
     'La obra y el alquiler dominan la inversión, y la renta que no aparece '
     'aquí se come el margen todos los meses. Mira la hoja «Traspaso vs Obra '
     'Nueva» con la renta real antes de enamorarte de la calle.'),
    ('Franquicia de panadería-pastelería', 'PS-08',
     1.10, 1.00, 1.20, 1.00, 1.10, 83000.0, 180000.0,
     'Las cifras publicadas de una misma marca varían del doble según la '
     'fuente. Y falta lo que este libro no calcula: canon de entrada y '
     'royalty mensual, que son gasto recurrente, no inversión.'),
    ('Obrador B2B para hostelería', 'PS-09',
     1.40, 1.60, 0.20, 1.10, 1.30, None, None,
     'Sin cifra de inversión publicada: el caso conocido son 320 m2 entre dos '
     'locales con el 30 % de la venta a restauración. Producción a volumen, '
     'venta a crédito y casi nada de escaparate. Es donde se rompe el '
     'requisito de «restringido» del art. 3.'),
    ('Pastelería sin salida de humos', 'PS-11',
     0.95, 1.10, 1.00, 1.00, 1.00, None, None,
     'No tiene rango publicado porque no es un formato de negocio, es una '
     'restricción del local: te ahorras el conducto de acero inoxidable (que '
     '«puede superar los 6.000 €») a cambio de hornos 100 % eléctricos, '
     'campana de condensación, desagüe en el punto del horno y un surtido sin '
     'fritos. Compruébalo antes en la ficha de visita del libro 1.'),
]


# --------------------------------------------------------------------------
def nl(idd):
    n = D.nota_legal(idd)
    if n is None:
        raise SystemExit('nota_legal(%s) devolvió None.' % idd)
    return n


NOTAS_LEGALES = {'n': 0}


def nota_legal_celda(ws, coord, idd):
    from openpyxl.comments import Comment
    com = Comment(nl(idd), 'AI Chef Pro')
    com.width = 420
    com.height = 130
    ws[coord].comment = com
    NOTAS_LEGALES['n'] += 1


# --------------------------------------------------------------------------
PASOS = [
    '1. Hoja «Parámetros»: los metros del local, los tres precios por m2 de '
    'obra, el escenario que eliges, los meses de colchón y los tipos de IVA. '
    'Todo lo que calcula el libro sale de aquí.',
    '2. Hoja «CAPEX por Bloque»: una fila por partida. Escribe el mínimo y el '
    'máximo que te hayan presupuestado y el importe con el que trabajas, di si '
    'ESE importe lleva IVA y a qué tipo, y marca «No» en lo que no vayas a '
    'comprar. La hoja lleva todo a base imponible antes de sumar, que es la '
    'única forma de que el total signifique algo.',
    '3. Hoja «Variante del Formato»: tu pastelería puede no ser la del '
    'ejemplo. Diez formatos con un coeficiente editable por bloque sobre el '
    'caso central, y al lado el rango de inversión que publica el sector, para '
    'que veas si tu cuenta y la suya se parecen.',
    '4. Hoja «Traspaso vs Obra Nueva»: el precio del traspaso no es lo que '
    'cuesta el traspaso. Mete la renta de los dos casos, los meses que estarás '
    'parado en cada uno y los años del contrato, y compara el coste completo. '
    'Abajo, quince traspasos reales para que veas la horquilla.',
    '5. Hoja «IVA y Tesorería»: cuánto IVA adelantas, cuándo vuelve y cuánta '
    'caja tienes que tener el día que abres. Es la hoja que más sorprende: el '
    'IVA de la inversión es dinero que sale de tu bolsillo meses antes de '
    'volver.',
    '6. Hoja «Resumen»: las quince cifras que hay que llevar al banco, todas '
    'calculadas desde las hojas anteriores.',
]

NOTAS_LIBRO = [
    'LA COLUMNA «¿EL PRECIO LLEVA IVA?» ES LA QUE HACE QUE LA SUMA SIRVA. Unos '
    'distribuidores publican con IVA y otros sin él, y hay fichas que no lo '
    'dicen. Sumar los dos tipos de precio desvía la inversión un 21 % y no lo '
    've nadie, porque el total sale «razonable». Aquí cada línea declara su '
    'base y la hoja las lleva todas a base imponible antes de sumar.',
    'LO QUE NO TIENE PRECIO PUBLICADO VIENE MARCADO «SUPUESTO». Fermentación, '
    'frío de conservación, mobiliario, TPV, packaging, fianza y fondo de '
    'maniobra no se venden por catálogo: se presupuestan. La celda trae un '
    'valor por defecto para que el libro funcione desde el primer minuto, y la '
    'columna «horquilla publicada» te dice si existe algún rango de referencia '
    'y de dónde sale. Pide tres presupuestos y sustitúyelo.',
    'EL PRECIO DE UN TRASPASO NO ES LO QUE CUESTA UN TRASPASO. Los quince de '
    'la tabla son precios PEDIDOS en anuncios leídos el 10-09-2026, no precios '
    'pagados, y ninguno viene con su cuenta de resultados. Sirven para ver la '
    'horquilla y para negociar, nunca para valorar un negocio.',
    'EL FONDO DE MANIOBRA ES PARTE DE LA INVERSIÓN. Cuatro meses de gastos '
    'fijos en caja el día que abres no son prudencia: son la diferencia entre '
    'aguantar la rampa de arranque y cerrar en el mes ocho con el negocio '
    'funcionando. Va dentro del CAPEX, y por eso el total de este libro es '
    'más alto que cualquier presupuesto de obra y maquinaria.',
    'LA FIANZA NO ES UN GASTO Y EL PACKAGING TAMPOCO ES INVERSIÓN. La primera '
    'es un depósito que vuelve; el segundo son existencias. Los dos hay que '
    'tenerlos el día de la firma, así que están en el CAPEX, pero salen de la '
    'comparación con los presupuestos de obra y equipamiento que publica el '
    'sector: si no, estarías comparando dos cosas distintas.',
]

CADENCIA = ('Cadencia: se rellena UNA VEZ al preparar el plan y se revisa cada '
            'vez que entra un presupuesto nuevo, hasta la firma. Después de '
            'abrir sólo se vuelve a él para comparar lo presupuestado con lo '
            'gastado de verdad, que es lo que enseña a presupuestar el '
            'siguiente.')


def hoja_instrucciones(wb):
    ws = wb.create_sheet('Instrucciones', 0)
    C.anchos(ws, {'A': 46, 'B': 46, 'C': 46})
    motor.val(ws, 'A1', TITULO)
    ws['A1'].font = Font(bold=True, size=16, color=C.ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', C.SUBTITULO)
    motor.val(ws, 'A3', 'Para qué sirve: saber cuánto dinero necesitas de '
                        'verdad para abrir, y si sale mejor un traspaso o una '
                        'obra nueva.')
    ws['A3'].font = Font(italic=True, size=9)

    C.seccion(ws, 'A5', 'Instrucciones de uso')
    fila = 6
    for paso in PASOS:
        ws.merge_cells('A%d:C%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, paso, wrap=True)
        ws.row_dimensions[fila].height = 62
        fila += 1
    fila += 1
    motor.val(ws, 'A%d' % fila, C.NOTA_VERDES)
    ws['A%d' % fila].fill = PatternFill('solid', fgColor=motor.VERDE)
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Lo que conviene saber antes de empezar')
    fila += 1
    for texto in NOTAS_LIBRO:
        ws.merge_cells('A%d:C%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, texto, wrap=True)
        ws.row_dimensions[fila].height = 68
        fila += 1
    fila += 1

    C.seccion(ws, 'A%d' % fila, 'Dónde acaba este libro y dónde sigue otro')
    fila += 1
    C.cabecera(ws, fila, [('A', 'Lo que necesitas'), ('B', 'Dónde está'),
                          ('C', 'Por qué no está aquí')], altura=26)
    fila += 1
    FRONTERAS = [
        ('A quién compras cada máquina, a qué precio negociado y con qué plazo '
         'de entrega',
         'Libro 7: checklist-equipamiento-y-proveedores.xlsx',
         'Aquí la máquina entra sólo por su importe. El plazo de entrega no '
         'cambia el CAPEX; cambia la fecha de apertura, y eso es el libro 6.'),
        ('El P&L a tres años, la tesorería mes a mes y el cuadro de la deuda',
         'Libro 5: plan-financiero-3-anos-pasteleria.xlsx',
         'De ese libro sale el gasto fijo mensual de verdad. Aquí entra como '
         'un parámetro con valor por defecto, sólo para calcular el fondo de '
         'maniobra.'),
        ('Si ese local sirve y cuántas piezas al día aguanta el equipo',
         'Libro 1: capacidad-obrador-y-local.xlsx',
         'Comprar bien empieza por saber qué necesitas, no cuánto cuesta. Los '
         'dos libros comparten los mismos 90 m2 y la misma columna de IVA.'),
        ('Qué papeles te tocan, en qué orden y cuándo abres',
         'Libro 6: checklist-legal-y-licencias.xlsx',
         'Las tasas y el proyecto técnico están aquí como importe; el '
         'procedimiento y el calendario, allí.'),
    ]
    for que, donde, porque in FRONTERAS:
        motor.val(ws, 'A%d' % fila, que, wrap=True)
        motor.val(ws, 'B%d' % fila, donde, wrap=True)
        motor.val(ws, 'C%d' % fila, porque, wrap=True)
        ws.row_dimensions[fila].height = 56
        fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila,
              'Es COPIA declarada, no vínculo: en toda la guía no hay ni una '
              'fórmula que apunte a otro fichero. Donde una celda verde '
              'traería un dato de otro libro o del Kit de Tareas Pastelería, '
              'viene con un valor por defecto propio, declarado como supuesto, '
              'y su nota te dice qué lo sustituye.', wrap=True)
    ws['A%d' % fila].font = Font(italic=True, size=9)
    ws.row_dimensions[fila].height = 56
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Cada cuánto se usa este libro')
    fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila, CADENCIA, wrap=True)
    ws.row_dimensions[fila].height = 44
    fila += 2
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila, C.NOTA_DESPROTEGER, wrap=True)
    fila += 2
    C.pie(ws, fila)
    C.pagina(ws, apaisado=False)
    return ws


# --------------------------------------------------------------------------
def hoja_parametros(wb):
    ws = wb.create_sheet(H_PAR)
    C.anchos(ws, {'A': 46, 'B': 16, 'C': 18, 'D': 20, 'E': 80})
    C.encabezar(ws, 'Parámetros',
                'Cambia el escenario de obra y se recalcula el libro entero.',
                col_fin='E')
    C.cabecera(ws, 5, [('A', 'Parámetro'), ('B', 'Valor'), ('C', 'Unidad'),
                       ('D', 'Procedencia'), ('E', 'Qué es y de dónde sale')])
    for i, (etq, valor, unidad, fuente, notatxt) in enumerate(PARAMS_LIBRO):
        fila = fp(i)
        motor.val(ws, 'A%d' % fila, etq, wrap=True)
        if valor is None:
            pass
        elif unidad == '%':
            motor.val(ws, 'B%d' % fila, valor, fmt=C.FMT_PCT, verde_=True)
        elif isinstance(valor, str):
            motor.val(ws, 'B%d' % fila, valor, verde_=True)
        elif unidad in ('€', '€/mes', '€/m2'):
            motor.val(ws, 'B%d' % fila, float(valor), fmt=C.FMT_EUR,
                      verde_=True)
        elif unidad == 'm2':
            motor.val(ws, 'B%d' % fila, float(valor), fmt=C.FMT_DEC1,
                      verde_=True)
        else:
            motor.val(ws, 'B%d' % fila, valor, fmt=C.FMT_ENT, verde_=True)
        motor.val(ws, 'C%d' % fila, unidad)
        motor.val(ws, 'D%d' % fila, fuente)
        motor.val(ws, 'E%d' % fila, notatxt, wrap=True)
        ws.row_dimensions[fila].height = 46

    # Hallazgo A11c (2026-09-10): con el escenario vacío o mal escrito, la
    # fórmula caía en silencio en «Medio» en vez de devolver «sin dato» (""),
    # que es la convención de la casa. La DV lo impedía mientras la hoja
    # estuviera protegida, pero un «sin dato» no se resuelve solo.
    motor.f(ws, 'B%d' % fp(P_EURM2),
            '=IF(B%d="","",IF(B%d="Bajo",B%d,IF(B%d="Alto",B%d,'
            'IF(B%d="Medio",B%d,""))))'
            % (fp(P_ESC), fp(P_ESC), fp(P_BAJO), fp(P_ESC), fp(P_ALTO),
               fp(P_ESC), fp(P_MEDIO)),
            fmt=C.FMT_EUR)
    motor.f(ws, 'B%d' % fp(P_OBRA),
            motor.iferror('B%d*B%d' % (fp(P_M2), fp(P_EURM2))), fmt=C.FMT_EUR)
    motor.f(ws, 'B%d' % fp(P_FONDO),
            motor.iferror('B%d*B%d' % (fp(P_MESES_COL), fp(P_FIJOS))),
            fmt=C.FMT_EUR)
    nota_legal_celda(ws, 'A%d' % fp(P_IVA_PROD), 'PA-36')

    fila = fp(len(PARAMS_LIBRO)) + 1
    refs, fila = C.bloque_listas(ws, fila,
                                 [('Escenario de obra', ESCENARIOS)], col='A')
    C.dv_rango(ws, ['B%d' % fp(P_ESC)], refs['Escenario de obra'],
               'Escenario de obra', 'Elige «Bajo», «Medio» o «Alto».')
    C.parrafo(ws, fila,
              'Los tres precios por m2 son los del caso publicado de un '
              'escenario de 90 m2, así que casan con esta superficie sin '
              'retoques. Si cambias los metros, cambia la obra pero NO cambian '
              'los €/m2: pídelos otra vez, porque un local pequeño sale más '
              'caro por metro que uno grande.',
              col_ini='A', col_fin='E', alto=44)
    C.pagina(ws, apaisado=True, titulos='5:5')
    return ws


# --------------------------------------------------------------------------
# CAPEX por bloque
# --------------------------------------------------------------------------
X_INI = 6


def lineas_capex():
    """(bloque, partida, comprar, procedencia, lleva_iva, tipo, importe o
    fórmula, horquilla, nota, id legal)."""
    filas = []
    filas.append(('Obra civil e instalaciones',
                  'Obra civil del escenario elegido', 'Sí', 'PS-85a/b/c',
                  'No', 'IVA_GEN', 'FORMULA_OBRA',
                  '600, 900 o 1.200 €/m2 sobre 90 m2 (PS-85a/b/c)',
                  'La calcula la hoja «Parámetros» con los metros y el '
                  'escenario. Es la partida que más se desvía en la ejecución: '
                  'lo que no está en el proyecto se paga aparte.', None))
    for eq in D.EQUIPAMIENTO:
        verificado = eq['valor_verificado'] is not None
        importe = (eq['valor_verificado'] if verificado
                   else eq['supuesto_por_defecto'])
        lleva = 'Sí' if eq['base_iva'] == 'con IVA' else 'No'
        nombre = eq['partida']
        if eq['marca']:
            nombre += ' — ' + eq['marca']
            if eq['modelo']:
                nombre += ' ' + eq['modelo']
        horq = HORQUILLA.get(eq['n'], '')
        if verificado and not horq:
            horq = 'Precio de ficha de distribuidor (%s)' % eq['fuente']
        elif not verificado and not horq:
            horq = 'Sin precio publicado: valor por defecto SUPUESTO'
        notatxt = eq['nota'] or ''
        if not verificado:
            notatxt = (('SUPUESTO, no precio de ficha. ' + notatxt).strip())
        if eq['base_iva'] == 'no declarada':
            notatxt = ('La ficha NO declara si el precio lleva IVA: se trata '
                       'como base imponible y se marca. ' + notatxt)
        if eq['opcional']:
            notatxt = 'OPCIONAL: viene con «¿la compras?» en No. ' + notatxt
        idl = None
        if eq['n'] == 5:
            idl = 'PA-13'
        elif eq['n'] == 11:
            idl = 'PA-07b'
        elif eq['n'] == 19:
            idl = 'PA-37'
        filas.append((eq['bloque_capex'], nombre,
                      'No' if eq['opcional'] else 'Sí', eq['fuente'], lleva,
                      'IVA_GEN', float(importe), horq, notatxt.strip(), idl))
    for bloque, partida, importe, _base, tipo, fuente, notatxt in D.CAPEX:
        if bloque in ('Equipamiento de obrador', 'Tienda y vitrina',
                      'Obra civil e instalaciones'):
            continue                       # ya están, línea a línea
        if bloque == 'Fondo de maniobra':
            filas.append((bloque, partida, 'Sí', fuente, 'No', 'IVA_CERO',
                          'FORMULA_FONDO',
                          'Meses de colchón × gastos fijos mensuales',
                          notatxt, None))
            continue
        if bloque == 'Fianza y garantías':
            filas.append((bloque, partida, 'Sí', fuente, 'No', 'IVA_CERO',
                          'FORMULA_FIANZA', 'Renta mensual × meses de fianza',
                          notatxt, None))
            continue
        clave = 'IVA_CERO' if tipo == 0.0 else 'IVA_GEN'
        idl = 'PA-04' if 'registro autonómico' in partida else None
        filas.append((bloque, partida, 'Sí', fuente, 'No', clave,
                      float(importe),
                      ('Importe publicado (%s)' % fuente) if fuente.startswith('PS-')
                      else 'SUPUESTO: el importe cambia en cada ayuntamiento',
                      notatxt, idl))
    return filas


LINEAS = lineas_capex()
X_FIN = X_INI + len(LINEAS) - 1
B_INI = X_FIN + 3                       # primera fila del resumen por bloque
B_FIN = B_INI + len(BLOQUES) - 1
R_TOT = B_FIN + 1
R_IVA = R_TOT + 1
R_CIVA = R_TOT + 2
R_COMP = R_TOT + 4
R_PUB = R_TOT + 5
R_DESV = R_TOT + 6


def hoja_capex(wb):
    ws = wb.create_sheet(H_CAP)
    C.anchos(ws, {'A': 5, 'B': 27, 'C': 46, 'D': 12, 'E': 16, 'F': 13,
                  'G': 11, 'H': 14, 'I': 14, 'J': 14, 'K': 14, 'L': 14,
                  'M': 14, 'N': 34, 'O': 78})
    C.encabezar(ws, 'CAPEX por bloque',
                'Todas las líneas se llevan a base imponible antes de sumar. '
                'Sin la columna de IVA, el total se desvía un 21 %.',
                col_fin='O')
    C.cabecera(ws, 5, [
        ('A', 'Nº'), ('B', 'Bloque'), ('C', 'Partida'), ('D', '¿La compras?'),
        ('E', 'Procedencia'), ('F', '¿El precio lleva IVA?'),
        ('G', 'Tipo de IVA'), ('H', 'Mínimo'), ('I', 'Máximo'),
        ('J', 'Tu importe'), ('K', 'Base sin IVA'), ('L', 'IVA soportado'),
        ('M', 'Total con IVA'), ('N', 'Horquilla publicada'), ('O', 'Nota')],
        altura=48)

    ref_iva = {'IVA_GEN': "'%s'!$B$%d" % (H_PAR, fp(P_IVA_GEN)),
               'IVA_CERO': "'%s'!$B$%d" % (H_PAR, fp(P_IVA_CERO))}
    fila = X_INI
    for i, (bloque, partida, comprar, proc, lleva, tipo, importe, horq,
            notatxt, idl) in enumerate(LINEAS):
        motor.val(ws, 'A%d' % fila, i + 1, fmt=C.FMT_ENT)
        motor.val(ws, 'B%d' % fila, bloque, wrap=True)
        motor.val(ws, 'C%d' % fila, partida, wrap=True)
        motor.val(ws, 'D%d' % fila, comprar, verde_=True)
        motor.val(ws, 'E%d' % fila, proc)
        motor.val(ws, 'F%d' % fila, lleva, verde_=True)
        motor.f(ws, 'G%d' % fila, '=' + ref_iva[tipo], fmt=C.FMT_PCT)
        if isinstance(importe, str):
            origen = {'FORMULA_OBRA': "='%s'!B%d" % (H_PAR, fp(P_OBRA)),
                      'FORMULA_FONDO': "='%s'!B%d" % (H_PAR, fp(P_FONDO)),
                      'FORMULA_FIANZA': motor.iferror(
                          "'%s'!B%d*'%s'!B%d"
                          % (H_PAR, fp(P_RENTA), H_PAR, fp(P_FIANZA)))}[importe]
            motor.f(ws, 'H%d' % fila, origen, fmt=C.FMT_EUR)
            motor.f(ws, 'I%d' % fila, origen, fmt=C.FMT_EUR)
            motor.f(ws, 'J%d' % fila, origen, fmt=C.FMT_EUR)
        else:
            motor.val(ws, 'H%d' % fila, importe, fmt=C.FMT_EUR, verde_=True)
            motor.val(ws, 'I%d' % fila, importe, fmt=C.FMT_EUR, verde_=True)
            motor.val(ws, 'J%d' % fila, importe, fmt=C.FMT_EUR, verde_=True)
        motor.f(ws, 'K%d' % fila,
                '=IF(D%d="No","",IFERROR(IF(F%d="Sí",J%d/(1+G%d),J%d),""))'
                % (fila, fila, fila, fila, fila), fmt=C.FMT_EUR)
        motor.f(ws, 'L%d' % fila,
                '=IF(K%d="","",IFERROR(K%d*G%d,""))' % (fila, fila, fila),
                fmt=C.FMT_EUR)
        motor.f(ws, 'M%d' % fila,
                '=IF(K%d="","",IFERROR(K%d+L%d,""))' % (fila, fila, fila),
                fmt=C.FMT_EUR)
        motor.val(ws, 'N%d' % fila, horq, wrap=True)
        motor.val(ws, 'O%d' % fila, notatxt, wrap=True)
        if idl:
            nota_legal_celda(ws, 'O%d' % fila, idl)
        ws.row_dimensions[fila].height = 48
        fila += 1

    C.seccion(ws, 'B%d' % (X_FIN + 2), 'Resumen por bloque')
    for k, bloque in enumerate(BLOQUES):
        f = B_INI + k
        motor.val(ws, 'C%d' % f, bloque)
        for col in ('K', 'L', 'M'):
            motor.f(ws, '%s%d' % (col, f),
                    '=SUMIF($B$%d:$B$%d,C%d,%s$%d:%s$%d)'
                    % (X_INI, X_FIN, f, col, X_INI, col, X_FIN),
                    fmt=C.FMT_EUR)
        motor.f(ws, 'N%d' % f, motor.iferror('K%d/$K$%d' % (f, R_TOT)),
                fmt=C.FMT_PCT)
    motor.val(ws, 'C%d' % R_TOT, 'CAPEX TOTAL', bold=True)
    for col in ('K', 'L', 'M'):
        motor.f(ws, '%s%d' % (col, R_TOT),
                '=SUM(%s%d:%s%d)' % (col, B_INI, col, B_FIN), fmt=C.FMT_EUR,
                bold=True)
        C.destacado(ws, '%s%d' % (col, R_TOT))
    motor.val(ws, 'C%d' % R_IVA, 'Del cual, IVA que hay que adelantar')
    motor.f(ws, 'K%d' % R_IVA, '=L%d' % R_TOT, fmt=C.FMT_EUR)
    motor.val(ws, 'C%d' % R_CIVA, 'Desembolso total con IVA')
    motor.f(ws, 'K%d' % R_CIVA, '=M%d' % R_TOT, fmt=C.FMT_EUR, bold=True)

    motor.val(ws, 'C%d' % R_COMP,
              'Subtotal comparable (obra, equipamiento, tienda, licencias y '
              'marketing)', wrap=True)
    motor.f(ws, 'K%d' % R_COMP,
            '=' + '+'.join('K%d' % (B_INI + BLOQUES.index(b))
                           for b in BLOQUES_COMPARABLES), fmt=C.FMT_EUR,
            bold=True)
    motor.val(ws, 'C%d' % R_PUB,
              'Escenario publicado del sector para 90 m2 (PS-85h)')
    motor.val(ws, 'K%d' % R_PUB, ESCENARIO_PUBLICADO, fmt=C.FMT_EUR)
    motor.val(ws, 'C%d' % R_DESV, 'Desviación sobre el escenario publicado')
    motor.f(ws, 'K%d' % R_DESV,
            motor.iferror('K%d/K%d-1' % (R_COMP, R_PUB)), fmt=C.FMT_PCT)
    motor.regla_expresion(ws, 'K%d' % R_DESV,
                          '=AND(ISNUMBER($K$%d),ABS($K$%d)>0.5)'
                          % (R_DESV, R_DESV))
    motor.val(ws, 'O%d' % R_DESV,
              'Son dos fuentes independientes: este presupuesto, línea a línea '
              'y en una sola base fiscal, y un escenario publicado de 90 m2 '
              '(proyecto 5.000 € + obra media 81.000 € + equipamiento de nivel '
              'alto 46.000 € + marketing 5.000 €). Que estén en el mismo orden '
              'de magnitud es la comprobación; que coincidan al euro sería '
              'sospechoso. La desviación se lee y se explica, no se maquilla. '
              'El semáforo salta si te vas más de un 50 %.', wrap=True)
    ws.row_dimensions[R_DESV].height = 62

    fila = R_DESV + 3
    refs, fila = C.bloque_listas(
        ws, fila, [('¿La compras?', SI_NO), ('¿Lleva IVA?', SI_NO)], col='C')
    C.dv_rango(ws, ['D%d' % r for r in range(X_INI, X_FIN + 1)],
               refs['¿La compras?'], '¿La compras?',
               'Elige «Sí» o «No» de la lista.')
    C.dv_rango(ws, ['F%d' % r for r in range(X_INI, X_FIN + 1)],
               refs['¿Lleva IVA?'], '¿El precio lleva IVA?',
               'Elige «Sí» o «No» de la lista.')
    C.parrafo(ws, fila,
              'Mínimo y máximo son para TUS presupuestos: vienen sembrados con '
              'el mismo valor de partida para que el libro funcione desde el '
              'primer minuto, y en cuanto tengas dos ofertas de verdad se ve '
              'de un vistazo cuánto se mueve cada partida. El total sólo usa '
              '«tu importe».',
              col_ini='C', col_fin='O', alto=44)
    C.pagina(ws, apaisado=True, titulos='5:5')
    return ws


# --------------------------------------------------------------------------
def hoja_variante(wb):
    ws = wb.create_sheet(H_VAR)
    C.anchos(ws, {'A': 5, 'B': 44, 'C': 16, 'D': 11, 'E': 12, 'F': 11,
                  'G': 12, 'H': 11, 'I': 16, 'J': 16, 'K': 14, 'L': 14,
                  'M': 14, 'N': 80, 'O': 34})
    C.encabezar(ws, 'Variante del formato',
                'Tu pastelería puede no ser la del ejemplo. Los coeficientes '
                'son supuestos editables sobre el caso central; los rangos de '
                'la derecha son cifras publicadas. «Inversión de apertura» es '
                'el CAPEX sin el fondo de maniobra, que es como publica sus '
                'cifras el sector.', col_fin='N')

    C.seccion(ws, 'B5', 'Bases del caso central (vienen de «CAPEX por Bloque»)')
    bases = [
        ('Obra civil e instalaciones', 6),
        ('Equipamiento de obrador', 7),
        ('Tienda y vitrina', 8),
        ('Licencias y proyecto técnico', 9),
    ]
    for bloque, fila in bases:
        motor.val(ws, 'B%d' % fila, bloque)
        motor.f(ws, 'C%d' % fila,
                "='%s'!K%d" % (H_CAP, B_INI + BLOQUES.index(bloque)),
                fmt=C.FMT_EUR)
    motor.val(ws, 'B10', 'Otros de apertura (fianza, packaging y marketing)')
    motor.f(ws, 'C10',
            "='%s'!K%d+'%s'!K%d+'%s'!K%d"
            % (H_CAP, B_INI + BLOQUES.index('Fianza y garantías'),
               H_CAP, B_INI + BLOQUES.index('Packaging inicial'),
               H_CAP, B_INI + BLOQUES.index('Marketing de apertura')),
            fmt=C.FMT_EUR)
    motor.val(ws, 'B11', 'Fondo de maniobra')
    motor.f(ws, 'C11', "='%s'!K%d"
            % (H_CAP, B_INI + BLOQUES.index('Fondo de maniobra')),
            fmt=C.FMT_EUR)

    C.cabecera(ws, V_INI - 1, [
        ('A', 'Nº'), ('B', 'Variante'), ('C', 'Id del research'),
        ('D', 'Coef. obra'), ('E', 'Coef. equipamiento'), ('F', 'Coef. tienda'),
        ('G', 'Coef. licencias'), ('H', 'Coef. otros'),
        ('I', 'Inversión de apertura'), ('J', 'Con fondo de maniobra'),
        ('K', 'Publicado mínimo'), ('L', 'Publicado máximo'),
        ('M', 'Desviación sobre el punto medio'),
        ('N', 'Qué cambia además'),
        ('O', '¿Cuadra con el rango publicado?')],
        altura=48)
    fila = V_INI
    for i, (nombre, idd, co, ce, ct, cl, cx, pmin, pmax,
            notatxt) in enumerate(VARIANTES):
        motor.val(ws, 'A%d' % fila, i + 1, fmt=C.FMT_ENT)
        motor.val(ws, 'B%d' % fila, nombre, wrap=True)
        motor.val(ws, 'C%d' % fila, idd)
        for col, coef in (('D', co), ('E', ce), ('F', ct), ('G', cl),
                          ('H', cx)):
            motor.val(ws, '%s%d' % (col, fila), coef, fmt=C.FMT_DEC,
                      verde_=True)
        motor.f(ws, 'I%d' % fila,
                motor.iferror('$C$6*D%d+$C$7*E%d+$C$8*F%d+$C$9*G%d+$C$10*H%d'
                              % (fila, fila, fila, fila, fila)), fmt=C.FMT_EUR)
        motor.f(ws, 'J%d' % fila,
                motor.iferror('I%d+$C$11*H%d' % (fila, fila)), fmt=C.FMT_EUR)
        if pmin is not None:
            motor.val(ws, 'K%d' % fila, pmin, fmt=C.FMT_EUR)
            motor.val(ws, 'L%d' % fila, pmax, fmt=C.FMT_EUR)
        motor.f(ws, 'M%d' % fila,
                '=IF(OR(K%d="",L%d=""),"",IFERROR(I%d/((K%d+L%d)/2)-1,""))'
                % (fila, fila, fila, fila, fila), fmt=C.FMT_PCT)
        motor.val(ws, 'N%d' % fila, notatxt, wrap=True)
        # Hallazgo B8 (2026-09-10): el semáforo de color de M ya marcaba estas
        # filas, pero color no se ve en un volcado a texto ni en el mapa que
        # cita el guion. Columna explícita, en palabras, para PS-02 (+404 %) y
        # PS-04 (+151 %): el propio A3/B29 de esta hoja avisa de que, si se va
        # a más del doble, sospecha primero del rango publicado.
        motor.f(ws, 'O%d' % fila,
                '=IF(M%d="","",IF(ABS(M%d)>1,'
                '"Se van a más del doble: mira el rango antes que la cuenta",'
                '"En el mismo orden de magnitud"))' % (fila, fila))
        ws.row_dimensions[fila].height = 68
        fila += 1
    v_fin = fila - 1
    motor.regla_expresion(ws, 'M%d:M%d' % (V_INI, v_fin),
                          '=AND(ISNUMBER($M%d),ABS($M%d)>0.5)'
                          % (V_INI, V_INI))
    motor.semaforo_texto(ws, 'O%d:O%d' % (V_INI, v_fin),
                         (('Se van a más del doble: mira el rango antes que '
                           'la cuenta', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          ('En el mismo orden de magnitud', motor.CF_VERDE_BG,
                           motor.CF_VERDE_FG)))

    f = v_fin + 2
    motor.val(ws, 'B%d' % f, 'Variantes con rango de inversión publicado')
    motor.f(ws, 'I%d' % f, '=COUNT(K%d:K%d)' % (V_INI, v_fin), fmt=C.FMT_ENT)
    motor.val(ws, 'B%d' % (f + 1),
              'Variantes que se van más de un 50 % del punto medio publicado')
    motor.f(ws, 'I%d' % (f + 1),
            '=COUNTIF(M%d:M%d,">0.5")+COUNTIF(M%d:M%d,"<-0.5")'
            % (V_INI, v_fin, V_INI, v_fin), fmt=C.FMT_ENT)

    C.parrafo(ws, f + 3,
              'LOS COEFICIENTES SON SUPUESTOS, Y EDITABLES A PROPÓSITO. No '
              'salen de ninguna estadística: son la desviación razonable de '
              'cada formato sobre el caso central, puesta para que puedas '
              'moverla. Lo que sí es dato publicado son las dos columnas de la '
              'derecha, con su id. Si tu cuenta y el rango publicado se van a '
              'más del doble, uno de los dos está mal, y suele ser el rango: '
              'casi ninguna de esas cifras dice si lleva IVA, si incluye la '
              'obra o si cuenta el fondo de maniobra.',
              col_ini='B', col_fin='N', alto=62)
    C.parrafo(ws, f + 5,
              'Dos variantes no traen rango: el obrador B2B, del que sólo hay '
              'un caso con metros pero sin inversión publicada, y la '
              'pastelería sin salida de humos, que no es un formato de negocio '
              'sino una restricción del local. En las dos, la columna de '
              'desviación se queda vacía a propósito: un cero ahí sería decir '
              'que la cuenta cuadra, y lo que pasa es que no hay con qué '
              'compararla.',
              col_ini='B', col_fin='N', alto=48)
    C.pagina(ws, apaisado=True, titulos='14:14')
    return ws


# --------------------------------------------------------------------------
T_PT, T_TAD, T_TREN, T_TPAR = 6, 7, 8, 9
T_ON, T_OREN, T_OPAR, T_HOR = 10, 11, 12, 13
T_CT, T_CO, T_RT, T_RO, T_TOT_T, T_TOT_O, T_DIF, T_VER = (15, 16, 17, 18, 19,
                                                          20, 21, 22)
T_TAB_CAB = 25
T_TAB_INI = 26


def hoja_traspaso(wb):
    ws = wb.create_sheet(H_TRA)
    C.anchos(ws, {'A': 52, 'B': 26, 'C': 18, 'D': 12, 'E': 16, 'F': 15,
                  'G': 14, 'H': 18, 'I': 12, 'J': 78})
    C.encabezar(ws, 'Traspaso contra obra nueva',
                'El precio de un traspaso no es lo que cuesta un traspaso: la '
                'renta de los años del contrato pesa más que el precio.',
                col_fin='J')

    C.seccion(ws, 'A5', 'El local que estás mirando (traspaso)')
    entradas = [
        (T_PT, 'Precio de traspaso que te piden', 43000.0, C.FMT_EUR, True,
         'PS-69',
         'Sembrado con el traspaso de Gràcia (85 m2, 43.000 €), que es el más '
         'parecido en metros a los 90 m2 del caso. Es un precio PEDIDO.'),
        (T_TAD, 'Inversión de adecuación que aún tendrías que hacer', 25000.0,
         C.FMT_EUR, True, 'supuesto',
         'Un traspaso casi nunca se abre tal cual: pintura, vitrina, rótulo y '
         'la máquina que falta. Míralo con la ficha de visita del libro 1 en '
         'la mano.'),
        (T_TREN, 'Renta mensual del local traspasado', 1250.0, C.FMT_EUR, True,
         'PS-69',
         'La renta sólo consta en los cinco traspasos de Barcelona. En los '
         'otros diez, el anuncio no la dice, que ya es un dato.'),
        (T_TPAR, 'Meses parado hasta abrir con el traspaso', 1, C.FMT_ENT,
         True, 'supuesto',
         'Pagas renta desde la firma y no facturas hasta que abres.'),
    ]
    for fila, etq, valor, fmt, verde, fuente, notatxt in entradas:
        motor.val(ws, 'A%d' % fila, etq, wrap=True)
        motor.val(ws, 'C%d' % fila, valor, fmt=fmt, verde_=verde)
        motor.val(ws, 'B%d' % fila, fuente)
        motor.val(ws, 'J%d' % fila, notatxt, wrap=True)
        ws.row_dimensions[fila].height = 40

    motor.val(ws, 'A%d' % T_ON,
              'CAPEX comparable de la obra nueva (de «CAPEX por Bloque»)',
              wrap=True)
    motor.f(ws, 'C%d' % T_ON, "='%s'!K%d" % (H_CAP, R_COMP), fmt=C.FMT_EUR)
    motor.val(ws, 'J%d' % T_ON,
              'Sin fianza, packaging ni fondo de maniobra: los dos lados de la '
              'comparación los necesitan igual, así que sumarlos a uno solo '
              'falsearía el resultado.', wrap=True)
    ws.row_dimensions[T_ON].height = 40
    motor.val(ws, 'A%d' % T_OREN, 'Renta mensual del local en obra nueva')
    motor.f(ws, 'C%d' % T_OREN, "='%s'!B%d" % (H_PAR, fp(P_RENTA)),
            fmt=C.FMT_EUR)
    motor.val(ws, 'A%d' % T_OPAR, 'Meses de obra sin facturar')
    motor.val(ws, 'C%d' % T_OPAR, 4, fmt=C.FMT_ENT, verde_=True)
    motor.val(ws, 'B%d' % T_OPAR, 'supuesto')
    motor.val(ws, 'J%d' % T_OPAR,
              'Renta que pagas mientras el local está en obras. Es la partida '
              'que casi nadie mete y la que más se parece a una sorpresa.',
              wrap=True)
    ws.row_dimensions[T_OPAR].height = 40
    motor.val(ws, 'A%d' % T_HOR, 'Horizonte de comparación (años)')
    motor.f(ws, 'C%d' % T_HOR, "='%s'!B%d" % (H_PAR, fp(P_HORIZ)),
            fmt=C.FMT_ENT)

    C.seccion(ws, 'A14', 'La comparación')
    salidas = [
        (T_CT, 'Coste del traspaso a lo largo del horizonte',
         motor.iferror('C%d+C%d+C%d*12*C%d' % (T_PT, T_TAD, T_TREN, T_HOR))),
        (T_CO, 'Coste de la obra nueva a lo largo del horizonte',
         motor.iferror('C%d+C%d*12*C%d' % (T_ON, T_OREN, T_HOR))),
        (T_RT, 'Renta pagada sin facturar, traspaso',
         motor.iferror('C%d*C%d' % (T_TREN, T_TPAR))),
        (T_RO, 'Renta pagada sin facturar, obra nueva',
         motor.iferror('C%d*C%d' % (T_OREN, T_OPAR))),
        (T_TOT_T, 'TOTAL del traspaso',
         motor.iferror('C%d+C%d' % (T_CT, T_RT))),
        (T_TOT_O, 'TOTAL de la obra nueva',
         motor.iferror('C%d+C%d' % (T_CO, T_RO))),
        (T_DIF, 'Diferencia (traspaso menos obra nueva)',
         motor.iferror('C%d-C%d' % (T_TOT_T, T_TOT_O))),
    ]
    for fila, etq, formula in salidas:
        motor.val(ws, 'A%d' % fila, etq, wrap=True,
                  bold=fila in (T_TOT_T, T_TOT_O, T_DIF))
        motor.f(ws, 'C%d' % fila, formula, fmt=C.FMT_EUR,
                bold=fila in (T_TOT_T, T_TOT_O, T_DIF))
    C.destacado(ws, 'C%d' % T_TOT_T)
    C.destacado(ws, 'C%d' % T_TOT_O)
    motor.val(ws, 'A%d' % T_VER, 'VEREDICTO', bold=True)
    motor.f(ws, 'C%d' % T_VER,
            '=IF(C%d="","",IF(C%d<0,"Sale mejor el TRASPASO",'
            '"Sale mejor la OBRA NUEVA"))' % (T_DIF, T_DIF), bold=True)
    C.destacado(ws, 'C%d' % T_VER)
    motor.semaforo_texto(ws, 'C%d' % T_VER,
                         (('Sale mejor el TRASPASO', motor.CF_VERDE_BG,
                           motor.CF_VERDE_FG),
                          ('Sale mejor la OBRA NUEVA', motor.CF_AMBAR_BG,
                           motor.CF_AMBAR_FG)))
    motor.val(ws, 'J%d' % T_VER,
              'El veredicto compara dinero, y el dinero no lo es todo: un '
              'traspaso te da una clientela y un local que ya funcionó, y te '
              'ata a una distribución de zonas que igual no admite marcha '
              'adelante. Pasa el local traspasado por la ficha de visita del '
              'libro 1 antes de hacerle caso a esta celda.', wrap=True)
    ws.row_dimensions[T_VER].height = 56

    C.seccion(ws, 'A24', 'Quince traspasos reales, para ver la horquilla')
    C.cabecera(ws, T_TAB_CAB, [
        ('A', 'Ciudad o zona'), ('B', 'Tipo de negocio'), ('C', 'm2'),
        ('D', 'Precio pedido'), ('E', 'Renta mensual'), ('F', '€ por m2'),
        ('G', 'Coste en el horizonte'), ('H', 'Fuente')], altura=30)
    fila = T_TAB_INI
    for ciudad, tipo, m2, precio, renta, fuente in D.TRASPASOS:
        motor.val(ws, 'A%d' % fila, ciudad)
        motor.val(ws, 'B%d' % fila, tipo)
        if m2 is not None:
            motor.val(ws, 'C%d' % fila, m2, fmt=C.FMT_ENT)
        motor.val(ws, 'D%d' % fila, precio, fmt=C.FMT_EUR)
        if renta is not None:
            motor.val(ws, 'E%d' % fila, renta, fmt=C.FMT_EUR)
        motor.f(ws, 'F%d' % fila,
                '=IF(ISNUMBER(C%d),IFERROR(D%d/C%d,""),"")'
                % (fila, fila, fila), fmt=C.FMT_EUR)
        motor.f(ws, 'G%d' % fila,
                '=IF(ISNUMBER(E%d),IFERROR(D%d+E%d*12*$C$%d,""),"")'
                % (fila, fila, fila, T_HOR), fmt=C.FMT_EUR)
        motor.val(ws, 'H%d' % fila, fuente)
        fila += 1
    t_fin = fila - 1
    f = t_fin + 1
    motor.val(ws, 'A%d' % f, 'Traspasos con renta publicada', bold=True)
    motor.f(ws, 'D%d' % f, '=COUNT(E%d:E%d)' % (T_TAB_INI, t_fin),
            fmt=C.FMT_ENT)
    motor.val(ws, 'A%d' % (f + 1), 'Precio pedido más bajo')
    motor.f(ws, 'D%d' % (f + 1),
            motor.iferror('MIN(D%d:D%d)' % (T_TAB_INI, t_fin)), fmt=C.FMT_EUR)
    motor.val(ws, 'A%d' % (f + 2), 'Precio pedido más alto')
    motor.f(ws, 'D%d' % (f + 2),
            motor.iferror('MAX(D%d:D%d)' % (T_TAB_INI, t_fin)), fmt=C.FMT_EUR)
    motor.val(ws, 'A%d' % (f + 3), 'Precio pedido medio')
    motor.f(ws, 'D%d' % (f + 3),
            motor.iferror('AVERAGE(D%d:D%d)' % (T_TAB_INI, t_fin)),
            fmt=C.FMT_EUR)
    motor.val(ws, 'A%d' % (f + 4), 'El que te piden, sobre la media')
    motor.f(ws, 'D%d' % (f + 4),
            motor.iferror('C%d/D%d-1' % (T_PT, f + 3)), fmt=C.FMT_PCT)

    C.parrafo(ws, f + 6, D.NOTA_TRASPASOS, col_ini='A', col_fin='J', alto=48)
    C.parrafo(ws, f + 8,
              'Y lo que ninguna de las quince trae: la cuenta de resultados. '
              'Un traspaso se valora por lo que gana el negocio, no por lo que '
              'pide el anuncio. Pide los modelos 303 y 390 de los tres últimos '
              'años y el resumen de la Seguridad Social de la plantilla; si no '
              'te los enseñan, ya sabes lo que estás comprando.',
              col_ini='A', col_fin='J', alto=48)
    C.pagina(ws, apaisado=True, titulos='25:25')
    return ws


# --------------------------------------------------------------------------
I_INI = 6
I_TOT = I_INI + len(BLOQUES)
I_PER, I_MES, I_ADEL = I_TOT + 2, I_TOT + 3, I_TOT + 4
I_BASE, I_IVA, I_DES, I_FON, I_FIN, I_APO, I_MESES, I_VER = (
    I_TOT + 7, I_TOT + 8, I_TOT + 9, I_TOT + 10, I_TOT + 11, I_TOT + 12,
    I_TOT + 13, I_TOT + 14)


def hoja_iva(wb):
    ws = wb.create_sheet(H_IVA)
    C.anchos(ws, {'A': 54, 'B': 18, 'C': 18, 'D': 16, 'E': 84})
    C.encabezar(ws, 'IVA y tesorería del arranque',
                'El IVA de la inversión sale de tu bolsillo meses antes de '
                'volver. Es la sorpresa más cara del primer trimestre.',
                col_fin='E')
    C.seccion(ws, 'A5', 'IVA soportado por bloque')
    C.cabecera(ws, I_INI - 1, [('A', 'Bloque'), ('B', 'Base sin IVA'),
                               ('C', 'IVA soportado'), ('D', 'Total con IVA')])
    for k, bloque in enumerate(BLOQUES):
        f = I_INI + k
        motor.val(ws, 'A%d' % f, bloque)
        for col_dst, col_src in (('B', 'K'), ('C', 'L'), ('D', 'M')):
            motor.f(ws, '%s%d' % (col_dst, f),
                    "='%s'!%s%d" % (H_CAP, col_src, B_INI + k), fmt=C.FMT_EUR)
    motor.val(ws, 'A%d' % I_TOT, 'TOTAL', bold=True)
    for col in ('B', 'C', 'D'):
        motor.f(ws, '%s%d' % (col, I_TOT),
                '=SUM(%s%d:%s%d)' % (col, I_INI, col, I_TOT - 1),
                fmt=C.FMT_EUR, bold=True)
        C.destacado(ws, '%s%d' % (col, I_TOT))

    C.seccion(ws, 'A%d' % (I_PER - 1), 'Cuándo vuelve ese IVA')
    motor.val(ws, 'A%d' % I_PER, 'Periodicidad de tu declaración (meses)')
    motor.f(ws, 'B%d' % I_PER, "='%s'!B%d" % (H_PAR, fp(P_PERIOD)),
            fmt=C.FMT_ENT)
    motor.val(ws, 'A%d' % I_MES, 'Meses hasta recuperarlo')
    motor.f(ws, 'B%d' % I_MES, "='%s'!B%d" % (H_PAR, fp(P_MESES_IVA)),
            fmt=C.FMT_ENT)
    motor.val(ws, 'A%d' % I_ADEL, 'IVA que tienes que adelantar', bold=True)
    motor.f(ws, 'B%d' % I_ADEL, '=C%d' % I_TOT, fmt=C.FMT_EUR, bold=True)
    C.destacado(ws, 'B%d' % I_ADEL)
    motor.val(ws, 'E%d' % I_ADEL,
              'En régimen general lo normal NO es que Hacienda te lo devuelva: '
              'es que lo compenses contra el IVA que repercutes. O sea, que '
              'vuelve al ritmo al que factures, no en una fecha. Si te '
              'inscribes en el registro de devolución mensual, la periodicidad '
              'pasa a 1 y la espera se acorta mucho: pregúntale a tu asesor '
              'antes de firmar la primera factura, no después.', wrap=True)
    ws.row_dimensions[I_ADEL].height = 62

    C.seccion(ws, 'A%d' % (I_BASE - 1), 'La caja del día que abres')
    motor.val(ws, 'A%d' % I_BASE, 'CAPEX sin IVA')
    motor.f(ws, 'B%d' % I_BASE, '=B%d' % I_TOT, fmt=C.FMT_EUR)
    motor.val(ws, 'A%d' % I_IVA, 'IVA soportado')
    motor.f(ws, 'B%d' % I_IVA, '=C%d' % I_TOT, fmt=C.FMT_EUR)
    motor.val(ws, 'A%d' % I_DES, 'Desembolso total con IVA', bold=True)
    motor.f(ws, 'B%d' % I_DES, '=D%d' % I_TOT, fmt=C.FMT_EUR, bold=True)
    C.destacado(ws, 'B%d' % I_DES)
    motor.val(ws, 'A%d' % I_FON, 'Del cual, fondo de maniobra (es caja, no '
                                 'inversión)', wrap=True)
    motor.f(ws, 'B%d' % I_FON,
            "='%s'!K%d" % (H_CAP, B_INI + BLOQUES.index('Fondo de maniobra')),
            fmt=C.FMT_EUR)
    motor.val(ws, 'A%d' % I_FIN, 'Financiación bancaria disponible')
    motor.f(ws, 'B%d' % I_FIN, "='%s'!B%d" % (H_PAR, fp(P_FINAN)),
            fmt=C.FMT_EUR)
    motor.val(ws, 'A%d' % I_APO, 'Aportación propia necesaria', bold=True)
    motor.f(ws, 'B%d' % I_APO, motor.iferror('B%d-B%d' % (I_DES, I_FIN)),
            fmt=C.FMT_EUR, bold=True)
    C.destacado(ws, 'B%d' % I_APO)
    motor.val(ws, 'A%d' % I_MESES,
              'Meses de gastos fijos que cubre el fondo de maniobra')
    motor.f(ws, 'B%d' % I_MESES,
            motor.iferror("B%d/'%s'!B%d" % (I_FON, H_PAR, fp(P_FIJOS))),
            fmt=C.FMT_DEC1)
    # Hallazgo A6 (2026-09-10): el umbral ya no va tecleado («3») dentro de la
    # regla ni de la fórmula: viene de 'Parámetros'!B%d (P_COLCHON_MIN), que
    # el lector puede subir si su banco exige más colchón.
    umbral_colchon = "'%s'!$B$%d" % (H_PAR, fp(P_COLCHON_MIN))
    motor.semaforo_isnumber(ws, 'B%d' % I_MESES, '$B$%d' % I_MESES,
                            operador='<', umbral=umbral_colchon)
    motor.val(ws, 'E%d' % I_MESES,
              'Por debajo del colchón mínimo de «Parámetros», el negocio '
              'depende de facturar desde la primera semana. Es la causa de '
              'cierre más frecuente de un local que por lo demás funcionaba.',
              wrap=True)
    ws.row_dimensions[I_MESES].height = 44
    motor.val(ws, 'A%d' % I_VER, 'VEREDICTO DE LA CAJA', bold=True)
    motor.f(ws, 'B%d' % I_VER,
            '=IF(B%d="","",IF(B%d<=0,"La financiación cubre el desembolso",'
            'IF(B%d<%s,"Te falta colchón: revisa el fondo de maniobra",'
            '"Necesitas aportación propia")))'
            % (I_APO, I_APO, I_MESES, umbral_colchon),
            bold=True)
    C.destacado(ws, 'B%d' % I_VER)
    motor.semaforo_texto(ws, 'B%d' % I_VER,
                         (('Te falta colchón: revisa el fondo de maniobra',
                           motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('Necesitas aportación propia', motor.CF_AMBAR_BG,
                           motor.CF_AMBAR_FG),
                          ('La financiación cubre el desembolso',
                           motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    C.parrafo(ws, I_VER + 2,
              'Que necesites aportación propia no es una mala noticia: ningún '
              'banco financia el 100 % de una apertura, y el que lo hiciera te '
              'estaría dejando sin margen de maniobra. Lo que sí es mala '
              'noticia es descubrirlo el mes de la firma.',
              col_ini='A', col_fin='E', alto=40)
    C.pagina(ws, apaisado=False, titulos='%d:%d' % (I_INI - 1, I_INI - 1))
    return ws


# --------------------------------------------------------------------------
S_INI = 6


def hoja_resumen(wb):
    ws = wb.create_sheet(H_RES)
    C.anchos(ws, {'A': 58, 'B': 20, 'C': 22, 'D': 84})
    C.encabezar(ws, 'Resumen',
                'Las cifras que hay que llevar al banco. Todas calculadas '
                'desde las hojas anteriores; aquí no se teclea nada.',
                col_fin='D')
    C.cabecera(ws, S_INI - 1, [('A', 'Cifra'), ('B', 'Valor'),
                               ('C', 'De dónde sale'), ('D', 'Qué dice')])
    filas = [
        ('Escenario de obra elegido', "='%s'!B%d" % (H_PAR, fp(P_ESC)), None,
         H_PAR, 'Bajo, medio o alto. Cambiarlo recalcula todo el libro.'),
        ('Obra civil', "='%s'!B%d" % (H_PAR, fp(P_OBRA)), C.FMT_EUR, H_PAR,
         'Metros por el precio del escenario. La partida más grande y la que '
         'más se desvía en la ejecución.'),
        ('CAPEX total sin IVA', "='%s'!K%d" % (H_CAP, R_TOT), C.FMT_EUR,
         H_CAP, 'Todo llevado a base imponible: es la cifra que se compara '
         'con cualquier otro presupuesto.'),
        ('IVA soportado', "='%s'!L%d" % (H_CAP, R_TOT), C.FMT_EUR, H_CAP,
         'Dinero tuyo que adelantas y que vuelve al ritmo al que factures.'),
        ('Desembolso total con IVA', "='%s'!M%d" % (H_CAP, R_TOT), C.FMT_EUR,
         H_CAP, 'Lo que sale de la cuenta. Es el número de la conversación '
         'con el banco.'),
        ('Subtotal comparable con el sector',
         "='%s'!K%d" % (H_CAP, R_COMP), C.FMT_EUR, H_CAP,
         'Obra, equipamiento, tienda, licencias y marketing: lo que incluyen '
         'los presupuestos publicados.'),
        ('Desviación sobre el escenario publicado',
         "='%s'!K%d" % (H_CAP, R_DESV), C.FMT_PCT, H_CAP,
         'Dos fuentes independientes en el mismo orden de magnitud. La '
         'desviación se explica, no se maquilla.'),
        ('Equipamiento de obrador',
         "='%s'!K%d" % (H_CAP, B_INI + BLOQUES.index('Equipamiento de obrador')),
         C.FMT_EUR, H_CAP, 'Sin los opcionales, que vienen marcados «No».'),
        ('Tienda y vitrina',
         "='%s'!K%d" % (H_CAP, B_INI + BLOQUES.index('Tienda y vitrina')),
         C.FMT_EUR, H_CAP, 'Vitrina, mobiliario de despacho y TPV.'),
        ('Fondo de maniobra',
         "='%s'!K%d" % (H_CAP, B_INI + BLOQUES.index('Fondo de maniobra')),
         C.FMT_EUR, H_CAP, 'Meses de colchón por gastos fijos. Es inversión, '
         'no prudencia.'),
        ('Aportación propia necesaria', "='%s'!B%d" % (H_IVA, I_APO),
         C.FMT_EUR, H_IVA, 'Desembolso menos financiación bancaria.'),
        ('Meses de gastos fijos cubiertos', "='%s'!B%d" % (H_IVA, I_MESES),
         C.FMT_DEC1, H_IVA, 'Por debajo de tres, el negocio depende de '
         'facturar desde la primera semana.'),
        ('Veredicto de la caja', "='%s'!B%d" % (H_IVA, I_VER), None, H_IVA,
         'Si la financiación cubre el desembolso o hace falta poner dinero.'),
        ('Coste del traspaso en el horizonte',
         "='%s'!C%d" % (H_TRA, T_TOT_T), C.FMT_EUR, H_TRA,
         'Precio pedido, adecuación y renta de todos los años, más la parada.'),
        ('Coste de la obra nueva en el horizonte',
         "='%s'!C%d" % (H_TRA, T_TOT_O), C.FMT_EUR, H_TRA,
         'CAPEX comparable y renta de todos los años, más los meses de obra.'),
        ('Traspaso o obra nueva', "='%s'!C%d" % (H_TRA, T_VER), None, H_TRA,
         'Compara dinero. La distribución del local y la clientela no salen '
         'en esta celda.'),
    ]
    fila = S_INI
    for etq, formula, fmt, hoja, notatxt in filas:
        motor.val(ws, 'A%d' % fila, etq, wrap=True)
        motor.f(ws, 'B%d' % fila, formula, fmt=fmt)
        motor.val(ws, 'C%d' % fila, hoja)
        motor.val(ws, 'D%d' % fila, notatxt, wrap=True)
        ws.row_dimensions[fila].height = 40
        fila += 1
    C.parrafo(ws, fila + 1,
              'Si alguna de estas cifras no te cuadra, no la cambies aquí: '
              'esta hoja no tiene ni una celda editable. Vuelve a la hoja '
              'donde nace y cambia el parámetro o el importe. Es lo que evita '
              'que un resumen y su origen digan cosas distintas.',
              col_ini='A', col_fin='D', alto=40)
    C.pagina(ws, apaisado=False, titulos='%d:%d' % (S_INI - 1, S_INI - 1))
    return ws


# --------------------------------------------------------------------------
def mapa_celdas():
    m = {}

    def add(etq, hoja, celda, tipo):
        m[etq] = {'ref': '%s.xlsx!%s!%s' % (NOMBRE, hoja, celda),
                  'tipo': tipo}

    add('Superficie del local', H_PAR, 'B%d' % fp(P_M2), 'entrada')
    add('Obra civil, escenario bajo (€/m2)', H_PAR, 'B%d' % fp(P_BAJO),
        'entrada')
    add('Obra civil, escenario medio (€/m2)', H_PAR, 'B%d' % fp(P_MEDIO),
        'entrada')
    add('Obra civil, escenario alto (€/m2)', H_PAR, 'B%d' % fp(P_ALTO),
        'entrada')
    add('Escenario de obra elegido', H_PAR, 'B%d' % fp(P_ESC), 'entrada')
    add('Precio por m2 aplicado', H_PAR, 'B%d' % fp(P_EURM2), 'salida')
    add('Obra civil calculada', H_PAR, 'B%d' % fp(P_OBRA), 'salida')
    add('IVA general', H_PAR, 'B%d' % fp(P_IVA_GEN), 'parametro')
    add('IVA de la pastelería', H_PAR, 'B%d' % fp(P_IVA_PROD), 'parametro')
    add('Meses de colchón de tesorería', H_PAR, 'B%d' % fp(P_MESES_COL),
        'entrada')
    add('Gastos fijos mensuales estimados', H_PAR, 'B%d' % fp(P_FIJOS),
        'entrada')
    add('Fondo de maniobra calculado', H_PAR, 'B%d' % fp(P_FONDO), 'salida')
    add('Renta mensual del local', H_PAR, 'B%d' % fp(P_RENTA), 'entrada')
    add('Horizonte de comparación (años)', H_PAR, 'B%d' % fp(P_HORIZ),
        'entrada')
    add('Financiación bancaria disponible', H_PAR, 'B%d' % fp(P_FINAN),
        'entrada')

    for k, bloque in enumerate(BLOQUES):
        add('Base sin IVA del bloque: ' + bloque, H_CAP, 'K%d' % (B_INI + k),
            'salida')
        add('IVA soportado del bloque: ' + bloque, H_CAP, 'L%d' % (B_INI + k),
            'salida')
    add('CAPEX total sin IVA', H_CAP, 'K%d' % R_TOT, 'salida')
    add('IVA soportado total', H_CAP, 'L%d' % R_TOT, 'salida')
    add('Desembolso total con IVA', H_CAP, 'M%d' % R_TOT, 'salida')
    add('Subtotal comparable con el sector', H_CAP, 'K%d' % R_COMP, 'salida')
    add('Escenario publicado del sector (PS-85h)', H_CAP, 'K%d' % R_PUB,
        'parametro')
    add('Desviación sobre el escenario publicado', H_CAP, 'K%d' % R_DESV,
        'salida')
    add('Importe de la línea de obra civil', H_CAP, 'J%d' % X_INI, 'salida')
    add('Importe del abatidor de temperatura', H_CAP, 'J%d' % (X_INI + 5),
        'entrada')
    add('Base sin IVA del horno de convección de 6 bandejas', H_CAP,
        'K%d' % (X_INI + 1), 'salida')

    for i, v in enumerate(VARIANTES):
        add('Inversión de apertura de la variante ' + v[1], H_VAR,
            'I%d' % (V_INI + i), 'salida')
        add('Inversión total de la variante ' + v[1], H_VAR,
            'J%d' % (V_INI + i), 'salida')
    add('Variantes con rango publicado', H_VAR,
        'I%d' % (V_INI + len(VARIANTES) + 1), 'salida')

    add('Precio de traspaso que te piden', H_TRA, 'C%d' % T_PT, 'entrada')
    add('Renta mensual del local traspasado', H_TRA, 'C%d' % T_TREN,
        'entrada')
    add('CAPEX comparable de la obra nueva', H_TRA, 'C%d' % T_ON, 'salida')
    add('Coste total del traspaso en el horizonte', H_TRA, 'C%d' % T_TOT_T,
        'salida')
    add('Coste total de la obra nueva en el horizonte', H_TRA, 'C%d' % T_TOT_O,
        'salida')
    add('Diferencia entre traspaso y obra nueva', H_TRA, 'C%d' % T_DIF,
        'salida')
    add('Veredicto de traspaso contra obra nueva', H_TRA, 'C%d' % T_VER,
        'salida')
    t_fin = T_TAB_INI + len(D.TRASPASOS) - 1
    add('Traspasos con renta publicada', H_TRA, 'D%d' % (t_fin + 1), 'salida')
    add('Precio pedido más bajo de los quince', H_TRA, 'D%d' % (t_fin + 2),
        'salida')
    add('Precio pedido más alto de los quince', H_TRA, 'D%d' % (t_fin + 3),
        'salida')
    add('Precio pedido medio de los quince', H_TRA, 'D%d' % (t_fin + 4),
        'salida')

    add('IVA que tienes que adelantar', H_IVA, 'B%d' % I_ADEL, 'salida')
    add('Desembolso total con IVA (tesorería)', H_IVA, 'B%d' % I_DES,
        'salida')
    add('Fondo de maniobra dentro del desembolso', H_IVA, 'B%d' % I_FON,
        'salida')
    add('Aportación propia necesaria', H_IVA, 'B%d' % I_APO, 'salida')
    add('Meses de gastos fijos que cubre el fondo', H_IVA, 'B%d' % I_MESES,
        'salida')
    add('VEREDICTO DE LA CAJA', H_IVA, 'B%d' % I_VER, 'salida')
    return m


# --------------------------------------------------------------------------
def construir():
    D.gate_legal(IDS_LEGALES)
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_parametros(wb)
    hoja_capex(wb)
    hoja_variante(wb)
    hoja_traspaso(wb)
    hoja_iva(wb)
    hoja_resumen(wb)

    wb.properties.creator = 'AI Chef Pro'
    wb.properties.lastModifiedBy = 'AI Chef Pro'
    wb.properties.title = TITULO
    wb.properties.subject = C.PRODUCTO + ' · Versión 1.0 · septiembre 2026'

    verdes = {}
    for ws in wb.worksheets:
        motor.retirar_verde_de_calculadas(ws)
        verdes[ws.title] = motor.proteger(ws)
    wb.calculation.fullCalcOnLoad = True

    destino = os.path.join(AQUI, 'build')
    if not os.path.isdir(destino):
        os.makedirs(destino)
    ruta = os.path.join(destino, NOMBRE + '.xlsx')
    wb.save(ruta)
    C.barrer_cp1252(wb)
    return ruta, verdes


def gate_totales(ruta):
    """`=SUM(rango)` recalculado a mano contra el caché (hallazgos A1/A3,
    2026-09-10): `pycel` cachea como 0 un `SUM` sobre una columna de
    `SUMPRODUCT`. Se llama DESPUÉS de `inject_cache.py`."""
    wbv = openpyxl.load_workbook(ruta, data_only=True)
    incoherentes = C.gate_sum_rango(wbv)
    wbv.close()
    if incoherentes:
        raise SystemExit('TOTALES con caché incoherente:\n  '
                         + '\n  '.join(incoherentes))


def verificar_y_mapear(ruta):
    """`inject_cache` + comprobación `data_only` de CADA fórmula registrada.

    Una fórmula que devuelve `""` se lee como `None` con `data_only=True`,
    igual que una que se quedó sin cachear: se distinguen preguntándole a
    pycel, y sólo se acepta el `None` cuando la fórmula vale cadena vacía.
    """
    import logging
    logging.disable(logging.CRITICAL)
    from pycel import ExcelCompiler
    subprocess.check_call(['/usr/local/bin/python3',
                           os.path.join(RAIZ, 'inject_cache.py'), ruta])
    wb = openpyxl.load_workbook(ruta, data_only=True)
    calc = ExcelCompiler(ruta)
    fallos, vacias = [], 0
    for hoja, coord, formula in motor.REGISTRO:
        v = wb[hoja][coord].value
        if isinstance(v, str) and v.startswith('#'):
            fallos.append('%s!%s = %s (%s)' % (hoja, coord, v, formula[:60]))
            continue
        if v is not None:
            continue
        esperado = calc.evaluate("'%s'!%s" % (hoja, coord))
        if esperado == '':
            vacias += 1
        else:
            fallos.append('%s!%s SIN VALOR, pycel dice %r (%s)'
                          % (hoja, coord, esperado, formula[:60]))
    m = mapa_celdas()
    for etq, d in m.items():
        _f, hoja, celda = d['ref'].split('!')
        v = wb[hoja][celda].value
        if v is None and wb[hoja][celda].data_type != 'n':
            v = calc.evaluate("'%s'!%s" % (hoja, celda))
        d['valor'] = v
    with open(os.path.join(os.path.dirname(ruta), 'mapa-' + NOMBRE + '.json'),
              'w', encoding='utf-8') as fh:
        json.dump(m, fh, ensure_ascii=False, indent=1)
    return fallos, m, vacias


# --------------------------------------------------------------------------
def demo(ruta):
    """Cinco comportamientos del libro, probados con pycel.

    Igual que en el libro 1: hay que EVALUAR LA SALIDA ANTES de tocar la
    entrada, porque `set_value()` sólo invalida los nodos que ya están en el
    grafo y los que no lo están se construyen leyendo el valor cacheado.
    """
    import logging
    logging.disable(logging.CRITICAL)
    from pycel import ExcelCompiler
    resultados = []

    def prueba(nombre, ok, detalle=''):
        resultados.append((nombre, bool(ok), detalle))

    def compilador(salidas):
        c = ExcelCompiler(ruta)
        for a in salidas:
            c.evaluate(a)
        return c

    A_TOT = "'%s'!K%d" % (H_CAP, R_TOT)
    A_OBRA = "'%s'!B%d" % (H_PAR, fp(P_OBRA))
    A_COMP = "'%s'!K%d" % (H_CAP, R_COMP)
    A_VERT = "'%s'!C%d" % (H_TRA, T_VER)
    A_DIF = "'%s'!C%d" % (H_TRA, T_DIF)
    A_IVA = "'%s'!B%d" % (H_IVA, I_ADEL)

    # 1. Los bloques suman el total.
    c = ExcelCompiler(ruta)
    tot = c.evaluate(A_TOT)
    suma = sum(c.evaluate("'%s'!K%d" % (H_CAP, B_INI + k))
               for k in range(len(BLOQUES)))
    prueba('El resumen por bloque suma exactamente el CAPEX total',
           abs(tot - suma) < 0.01,
           'total=%.2f · suma de bloques=%.2f' % (tot, suma))

    # 2. El escenario de obra mueve el CAPEX.
    c = compilador([A_OBRA, A_TOT])
    obra_medio, tot_medio = c.evaluate(A_OBRA), c.evaluate(A_TOT)
    c.set_value("'%s'!B%d" % (H_PAR, fp(P_ESC)), 'Alto')
    obra_alto, tot_alto = c.evaluate(A_OBRA), c.evaluate(A_TOT)
    prueba('Cambiar el escenario de obra recalcula la obra y el CAPEX total',
           obra_alto > obra_medio and tot_alto > tot_medio
           and abs(obra_alto - D.ESCENARIOS_OBRA['Alto'][1]) < 0.01,
           'obra %.0f -> %.0f · CAPEX %.0f -> %.0f'
           % (obra_medio, obra_alto, tot_medio, tot_alto))

    # 3. La columna de IVA hace su trabajo: marcar «Sí» baja la base.
    A_K = "'%s'!K%d" % (H_CAP, X_INI + 5)          # abatidor, publicado sin IVA
    c = compilador([A_K])
    base = c.evaluate(A_K)
    c.set_value("'%s'!F%d" % (H_CAP, X_INI + 5), 'Sí')
    base2 = c.evaluate(A_K)
    prueba('Declarar que el precio lleva IVA baja la base imponible un 21 %',
           abs(base2 - base / (1 + D.P('iva_general'))) < 0.01,
           'base %.2f -> %.2f' % (base, base2))

    # 4. Marcar «No» en «¿la compras?» saca la línea del total.
    c = compilador([A_TOT, A_COMP])
    tot0 = c.evaluate(A_TOT)
    c.set_value("'%s'!D%d" % (H_CAP, X_INI + 5), 'No')
    tot1 = c.evaluate(A_TOT)
    esperado = D.precio_equipamiento_sin_iva(
        [e for e in D.EQUIPAMIENTO if e['n'] == 5][0])
    prueba('Marcar «No» saca la línea del total por su importe exacto',
           abs((tot0 - tot1) - esperado) < 0.01,
           'baja %.2f, esperado %.2f' % (tot0 - tot1, esperado))

    # 5. El veredicto de traspaso cambia al subir el precio pedido.
    c = compilador([A_VERT, A_DIF])
    ver0, dif0 = c.evaluate(A_VERT), c.evaluate(A_DIF)
    c.set_value("'%s'!C%d" % (H_TRA, T_PT), 400000.0)
    ver1 = c.evaluate(A_VERT)
    prueba('Un traspaso desorbitado da la vuelta al veredicto',
           ver0 == 'Sale mejor el TRASPASO'
           and ver1 == 'Sale mejor la OBRA NUEVA',
           'antes=%s (dif %.0f) · después=%s' % (ver0, dif0, ver1))

    # 6. Las tasas municipales no generan IVA soportado.
    c = ExcelCompiler(ruta)
    fila_tasas = None
    for i, ln in enumerate(LINEAS):
        if 'Tasas municipales' in ln[1]:
            fila_tasas = X_INI + i
    iva_tasas = c.evaluate("'%s'!L%d" % (H_CAP, fila_tasas))
    iva_total = c.evaluate(A_IVA)
    prueba('Las tasas municipales van a tipo 0 y no generan IVA soportado',
           iva_tasas == 0 and iva_total > 0,
           'IVA de las tasas=%s · IVA total a adelantar=%.2f'
           % (iva_tasas, iva_total))
    return resultados


# --------------------------------------------------------------------------
def main():
    ruta, verdes = construir()
    print('escrito:', ruta)
    fallos, m, vacias = verificar_y_mapear(ruta)
    gate_totales(ruta)
    res = demo(ruta)
    print('-' * 66)
    print('fórmulas registradas : %d' % len(motor.REGISTRO))
    print('fórmulas sin valor   : %d' % len(fallos))
    for x in fallos[:20]:
        print('   ', x)
    print('fórmulas que dan ""  : %d  (sin dato legítimo)' % vacias)
    print('celdas verdes        : %d  %s' % (sum(verdes.values()), verdes))
    print('notas legales        : %d' % NOTAS_LEGALES['n'])
    print('etiquetas del mapa   : %d' % len(m))
    print('demos:')
    for nombre, ok, detalle in res:
        print('   [%s] %s — %s' % ('OK' if ok else 'FALLA', nombre, detalle))
    todo_ok = not fallos and all(ok for _n, ok, _d in res)
    print('-' * 66)
    print('RESULTADO:', 'VERDE' if todo_ok else 'ROJO')
    return 0 if todo_ok else 1


if __name__ == '__main__':
    sys.exit(main())
