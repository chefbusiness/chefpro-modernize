#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_calculadora-capex-chocolateria.py — libro 2 de «Cómo Montar una
Chocolatería» (SPEC §2.2 fila 2; decisiones D1, D2, D11, D23a/b/c, D32, D42c
y §3.3).

Hojas: Instrucciones · Parámetros · CAPEX por Bloque · Variante del Formato ·
Traspaso vs Obra Nueva · IVA y Tesorería · Resumen.

QUÉ DECIDE ESTE LIBRO
---------------------
Cuánto dinero necesitas de verdad para abrir, y si sale mejor un traspaso o
una obra nueva. Las dos se contestan mal por el mismo motivo: se suman precios
que unos llevan IVA y otros no, y se compara el precio de un traspaso con el
coste de una obra sin meter la renta de los años siguientes.

MOLDE Y DIFERENCIAS CON LA HERMANA (SPEC §2.4)
----------------------------------------------
Se calca `guia-pasteleria/gen_calculadora-capex-pasteleria.py` (CAPEX por
bloque, traspaso contra obra nueva, IVA y tesorería, resumen). **Nuevo: las
variantes bean-to-bar y taza y churros, la columna franquicia contra
independiente y el contador de plástico.**

LAS CUATRO REGLAS QUE NO SE NEGOCIAN, Y CÓMO SE MATERIALIZAN AQUÍ
-----------------------------------------------------------------
* **NUEVE BLOQUES, y el fondo de maniobra conserva SU FILA PROPIA** (§3.3 y
  R4-M1). No son los ocho del molde calcados: son esos ocho con
  **climatización y deshumidificación** y **TPV, informática y rótulo** en
  lugar de marketing de apertura.
* **«MESES DE COLCHÓN» NO ES ENTRADA DE ESTE LIBRO** (D32, R4-A1). El fondo de
  maniobra es «meses de colchón x gastos fijos mensuales» y **los DOS factores
  viven en el libro 7**, así que lo que viaja es la **magnitud ya calculada**:
  una celda verde «trae aquí el fondo de maniobra de
  `plan-financiero-3-anos-chocolateria.xlsx!Inversión Inicial`», con su valor
  por defecto declarado, más una **fila de CUADRE con semáforo**. Si este libro
  lo calculase por su cuenta, el fondo se calcularía dos veces y los dos libros
  publicarían **dos inversiones totales distintas con el mismo nombre**, que es
  el defecto ALTO que esta familia ya pagó en Pastelería.
* **La columna de IVA es lo que hace que la suma signifique algo** (D23, regla
  3 de §2.3). Cada línea declara la base que publica SU FUENTE -«sin IVA»,
  «con IVA» o «no declarada»- y, aparte, si el importe que TÚ has escrito lleva
  IVA. La hoja lleva todo a base imponible antes de sumar. Sin eso, mezclar la
  vitrina Docriluc (base sin IVA declarada) con las fichas Selmi (base no
  declarada) desvía el CAPEX un 21 % y nadie lo ve.
* **Ningún sumando sin fuente propia entra como número cerrado** (D23a/b).
  Los moldes de policarbonato van como **RANGO** (580,80-1.027,92 €, porque el
  único dato medido es 24,20-42,83 €/ud) y **nunca como «24 x 30 €»**; el
  mantenedor es un «**desde 570,00 €**», que es un suelo comercial y no el
  precio de la unidad que vas a comprar.
* **Los dos escenarios de dotación publicados entran como RANGO y con la
  etiqueta pegada** (D23c): «BASE MIXTA de IVA, no es presupuesto de
  apertura». **Está prohibido restarlos o compararlos como cifras fiscales**,
  y por eso esta hoja publica dónde CAE tu dotación dentro del rango y no
  calcula ninguna desviación porcentual contra él.

LO QUE NO HACE, Y DÓNDE SE HACE
-------------------------------
* **No es el checklist de compra.** A quién compras, a qué precio negociado y
  en cuántas semanas te sirven es el libro 9. Aquí la máquina entra sólo por su
  importe.
* **No es el plan financiero.** El P&L a tres años, la tesorería mes a mes, el
  servicio de la deuda, los gastos fijos y los meses de colchón son el libro 7.
* **No calcula capacidad ni clima.** Si ese equipo da los bombones que
  necesitas y si el local se puede climatizar es el libro 1.
* **No explica el impuesto al plástico**: emite una ALERTA cuando pasas el
  umbral del art. 75.f). La explicación entera vive en el capítulo 13.

Salida fija: build/calculadora-capex-chocolateria.xlsx + su mapa de celdas.
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
import _comun_chocolateria as C                                # noqa: E402

motor.CTX['producto'] = C.PID

NOMBRE = 'calculadora-capex-chocolateria'
TITULO = 'Calculadora de inversión inicial (CAPEX)'

H_PAR = 'Parámetros'
H_CAP = 'CAPEX por Bloque'
H_VAR = 'Variante del Formato'
H_TRA = 'Traspaso vs Obra Nueva'
H_IVA = 'IVA y Tesorería'
H_RES = 'Resumen'

IDS_LEGALES = {
    'CHN-71': ('IVA del chocolate: 10 % por exclusión, no por mención', 2),
    'CHN-75': ('Verifactu no es 2026, es 2027', 2),
    'CHN-39': ('La comunicación al registro autonómico no habilita para abrir',
               2),
    'CHN-49': ('Ninguna licencia previa de actividad hasta 750 m2', 2),
    'CHN-49c': ('La chocolatería de taza NO entra en la Ley 12/2012', 2),
    'CHN-48': ('Gas: inspección cada cinco años', 2),
    'CHN-47b': ('La nota (2) del CAPCA incluye los NÚCLEOS DE POBLACIÓN', 2),
    'CHN-25': ('EUDR: qué exige al operador que importa grano', 2),
    'CHN-62': ('Impuesto al plástico: quién lo paga y cuánto', 2),
    'CHN-62b': ('La exención de 5 kg/mes tiene DOS límites', 2),
    'CHN-62c': ('Los moldes de policarbonato NO pagan el impuesto', 2),
}

SI_NO = ('Sí', 'No')
NECESIDAD = ('Sí', 'No', 'Por decidir')
POR_ESCRITO = ('Sí', 'No', 'Por pedir')

#: Coste de obra por m2 de La Almendra: los 28.500 € de `datos_ejemplo.CAPEX`
#: repartidos entre los 75 m2. Es SUPUESTO declarado, igual que el importe.
OBRA_EUR_M2 = round([importe for b, _p, importe, _bi, _t, _f, _n in D.CAPEX
                     if b == 'Obra y adecuacion'][0] / D.NEGOCIO['m2_total'], 2)

#: Nombres de bloque tal y como salen de `datos_ejemplo` (sin tildes, porque
#: así están escritos allí) y su rótulo de pantalla.
ROTULO_BLOQUE = {
    'Obra y adecuacion': 'Obra y adecuación',
    'Climatizacion y deshumidificacion': 'Climatización y deshumidificación',
    'Equipo de templado y moldeado': 'Equipo de templado y moldeado',
    'Frio': 'Frío (cámara, nevera de rellenos y vitrina)',
    'Mobiliario y tienda': 'Mobiliario y tienda',
    'Packaging y moldes': 'Packaging y moldes',
    'TPV, informatica y rotulo': 'TPV, informática y rótulo',
    'Fianza y licencias': 'Fianza y licencias',
    'Fondo de maniobra': 'Fondo de maniobra',
}


# --------------------------------------------------------------------------
# Parámetros
# --------------------------------------------------------------------------
P_INI = 6
PARAMS_LIBRO = [
    ('Superficie total del local', D.NEGOCIO['m2_total'], 'm2',
     D.NEGOCIO['fuente_m2'],
     'Los mismos 75 m2 del libro 1. Si los cambias, cambia la obra: es la '
     'única partida del CAPEX que no se teclea.'),
    ('Coste de obra y adecuación por m2', OBRA_EUR_M2, '€/m2', 'supuesto',
     'SUPUESTO DECLARADO: ninguna fuente del research publica un coste de obra '
     'por m2 de obrador de chocolate. Es más barata que la de una pastelería '
     'por un motivo estructural, no por suerte: un obrador de chocolate NO '
     'genera humos, así que no hay conducto a cubierta ni la conversación con '
     'la comunidad de propietarios que lo acompaña. Pide tres presupuestos y '
     'sustitúyelo.'),
    ('Obra y adecuación calculada', None, '€', 'Se calcula',
     'Superficie x precio por m2.'),
    ('IVA general', D.P('iva_general'), '%',
     D.PARAMS['iva_general'][1],
     'Tipo general: obra, equipamiento, mobiliario, proyecto y clima. Es el '
     'valor por defecto de la columna «tipo de IVA» de cada línea, pero cada '
     'línea tiene el suyo.'),
    ('IVA del chocolate que vas a vender', D.P('iva_producto'), '%', 'CHN-71',
     'No entra en el CAPEX: está aquí porque es el IVA que repercutirás y '
     'contra el que se compensa el que adelantas ahora. El chocolate va al '
     '10 % POR EXCLUSIÓN, no porque un precepto lo nombre: la lista del 4 % es '
     'cerrada y tiene siete letras, y el chocolate no está en ninguna.'),
    ('IVA de tasas y trámites', 0.0, '%', 'supuesto',
     'Las tasas municipales y la comunicación al registro autonómico no llevan '
     'IVA. Se declara como parámetro para que la columna de la hoja de CAPEX '
     'no tenga que hacer una excepción escondida.'),
    ('Renta mensual del local', D.NEGOCIO['renta_mensual'], '€/mes',
     D.NEGOCIO['fuente_renta'], D.NEGOCIO['nota_renta']),
    ('Meses de fianza', D.NEGOCIO['meses_fianza'], 'meses',
     D.NEGOCIO['fuente_fianza'],
     'La fianza no es un gasto: es un depósito que se recupera. Va en el CAPEX '
     'porque hay que tenerla el día de la firma, y por eso no se amortiza.'),
    ('Horizonte de comparación', D.P('horizonte_comparacion_anios'), 'años',
     D.PARAMS['horizonte_comparacion_anios'][1],
     'Años sobre los que se compara el traspaso con la obra nueva. Cinco es lo '
     'habitual de un contrato con obligado cumplimiento; ponle los del tuyo.'),
    ('Periodicidad de la declaración de IVA', 3, 'meses', 'supuesto',
     'Trimestral en el régimen general de una bombonería que arranca. Si te '
     'inscribes en el registro de devolución mensual, esto es 1 y el IVA de la '
     'inversión vuelve mucho antes.'),
    ('Meses hasta recuperar el IVA de la inversión', 4, 'meses', 'supuesto',
     'El trimestre en el que compras más el plazo de presentación. Y ojo: en '
     'régimen general lo normal no es que te lo devuelvan, es que lo compenses '
     'contra el IVA que repercutes, así que tarda lo que tardes en facturar.'),
    ('Financiación bancaria disponible', round(D.principal_prestamo(), 2), '€',
     D.FINANCIACION['fuente'],
     'El 60 % de la inversión total, que es la estructura 40/60 supuesta en el '
     'libro 7. No se teclea allí ni aquí como número fijo: se deriva, para que '
     'si cambia una partida del CAPEX la estructura siga saliendo exacta.'),
    ('Colchón mínimo aceptable antes de avisar', 3, 'meses', 'supuesto',
     'Umbral del veredicto de caja. Es el mínimo que te exiges TÚ, no los '
     'meses con los que se dota el fondo: esos se deciden en el libro 7, que '
     'es donde están los gastos fijos con los que se multiplican.'),
    ('Kg de plástico no reciclado importado o adquirido en otro país de la UE',
     D.PLASTICO['kg_mes_ejemplo'], 'kg al mes', D.PLASTICO['fuente_kg_mes'],
     'Kilos de plástico no reciclado de los ENVASES que importas o compras en '
     'otro país de la UE, al mes. NO son los kilos totales de packaging: lo '
     'que compras en España a un proveedor español ya lo lleva repercutido. '
     'Por eso la pregunta es dónde compras, no cuánto.'),
    ('Umbral de la exención del impuesto al plástico',
     D.PLASTICO['umbral_kg_mes'], 'kg al mes', D.PLASTICO['fuente_umbral'],
     'El art. 75.f) exime la importación o adquisición intracomunitaria que no '
     'exceda de 5 kilogramos en un mes, y SÓLO de los envases del art. 68.1.a): '
     'NO exime la fabricación, ni los semielaborados, ni los cierres.'),
    ('Tipo del impuesto al plástico', D.PLASTICO['tipo_euros_kg'], '€/kg',
     D.PLASTICO['fuente_tipo'],
     'Se aplica sobre los kilos de plástico NO RECICLADO contenidos en el '
     'envase, no sobre el peso del envase entero.'),
]
P_M2, P_EURM2, P_OBRA = 0, 1, 2
P_IVA_GEN, P_IVA_PROD, P_IVA_CERO = 3, 4, 5
P_RENTA, P_FIANZA, P_HORIZ = 6, 7, 8
P_PERIOD, P_MESES_IVA, P_FINAN, P_COLCHON_MIN = 9, 10, 11, 12
P_KG_PLAST, P_UMBRAL_PLAST, P_TIPO_PLAST = 13, 14, 15


def fp(i):
    return P_INI + i


# --------------------------------------------------------------------------
# Líneas del CAPEX
# --------------------------------------------------------------------------
X_INI = 6


def lineas_capex():
    """(bloque, partida, comprar, procedencia, base declarada, lleva_iva,
    clave de tipo, mínimo, máximo, tu importe, horquilla, nota, id legal).

    `mínimo`, `máximo` y `tu importe` son números, o una clave de fórmula
    ('FORMULA_OBRA', 'FORMULA_FIANZA', 'VERDE_FONDO').
    """
    filas = []
    obra = [(b, p, imp, f, n) for b, p, imp, _bi, _t, f, n in D.CAPEX
            if b == 'Obra y adecuacion'][0]
    filas.append((obra[0], obra[1], 'Sí', obra[3], 'sin IVA', 'No', 'IVA_GEN',
                  'FORMULA_OBRA', 'FORMULA_OBRA', 'FORMULA_OBRA',
                  'La calcula «Parámetros» con tus metros y tu precio por m2',
                  obra[4], None))

    for eq in D.EQUIPAMIENTO:
        verificado = eq['valor_verificado'] is not None
        importe = (eq['valor_verificado'] if verificado
                   else eq['supuesto_por_defecto'])
        minimo = eq['rango_min'] if eq['rango_min'] is not None else importe
        maximo = eq['rango_max'] if eq['rango_max'] is not None else importe
        lleva = 'Sí' if eq['base_iva'] == 'con IVA' else 'No'
        nombre = eq['partida']
        if eq['marca']:
            nombre += ' — ' + eq['marca']
            if eq['modelo']:
                nombre += ' ' + eq['modelo']
        if eq['rango_min'] is not None:
            horq = ('RANGO, no precio cerrado: %s (D23a)' % eq['fuente'])
        elif eq['es_desde']:
            horq = ('«DESDE», suelo comercial: presupuéstalo (%s, D23b)'
                    % eq['fuente'])
        elif verificado:
            horq = 'Precio de ficha de distribuidor (%s)' % eq['fuente']
        else:
            horq = 'Sin precio publicado: valor por defecto SUPUESTO'
        notatxt = eq['nota'] or ''
        if not verificado and eq['rango_min'] is None:
            notatxt = ('SUPUESTO, no precio de ficha. ' + notatxt).strip()
        if eq['base_iva'] == 'no declarada':
            notatxt = ('La ficha NO declara si el precio lleva IVA: se trata '
                       'como base imponible y SE MARCA, que es lo honesto. '
                       + notatxt)
        if eq['opcional']:
            notatxt = 'OPCIONAL: viene con «¿la compras?» en No. ' + notatxt
        idl = None
        if eq['n'] == 15:
            idl = 'CHN-75'
        elif eq['n'] == 12:
            idl = 'CHN-62c'
        elif eq['n'] == 17:
            idl = 'CHN-49c'
        filas.append((eq['bloque_capex'], nombre,
                      'No' if eq['opcional'] else 'Sí', eq['fuente'],
                      eq['base_iva'], lleva, 'IVA_GEN',
                      float(minimo), float(maximo), float(importe),
                      horq, notatxt.strip(), idl))

    for bloque, partida, importe, base, tipo, fuente, notatxt in D.CAPEX:
        if bloque == 'Obra y adecuacion':
            continue
        if importe is None and bloque != 'Fondo de maniobra':
            continue                       # se calcula desde EQUIPAMIENTO
        if bloque == 'Fondo de maniobra':
            filas.append((bloque, partida, 'Sí', fuente, base, 'No',
                          'IVA_CERO', 'VERDE_FONDO', 'VERDE_FONDO',
                          'VERDE_FONDO',
                          'LLEGA DEL LIBRO 7 (cruce 2 <- 7): no se calcula '
                          'aquí', notatxt, None))
            continue
        clave = 'IVA_CERO' if tipo == 0.0 else 'IVA_GEN'
        idl = None
        if 'registro autonomico' in partida or 'registro autonómico' in partida:
            idl = 'CHN-39'
        elif 'Tasas municipales' in partida:
            idl = 'CHN-49'
        if partida.startswith('Fianza de arrendamiento'):
            filas.append((bloque, partida, 'Sí', fuente, base, 'No', clave,
                          'FORMULA_FIANZA', 'FORMULA_FIANZA',
                          'FORMULA_FIANZA', 'Renta mensual x meses de fianza',
                          notatxt, idl))
            continue
        filas.append((bloque, partida, 'Sí', fuente, base, 'No', clave,
                      float(importe), float(importe), float(importe),
                      ('Importe publicado (%s)' % fuente)
                      if fuente.startswith(('CHS-', 'CHN-'))
                      else 'SUPUESTO declarado: pídelo, no lo copies',
                      notatxt, idl))
    return filas


LINEAS = lineas_capex()
X_FIN = X_INI + len(LINEAS) - 1
B_INI = X_FIN + 3                       # primera fila del resumen por bloque
B_FIN = B_INI + len(D.BLOQUES_CAPEX) - 1
R_TOT = B_FIN + 1
R_IVA = R_TOT + 1
R_CIVA = R_TOT + 2
R_SINFONDO = R_TOT + 4
R_FONDO = R_TOT + 5
R_INV = R_TOT + 6
R_COMP = R_TOT + 8
#: Cruce 2 <- 7: celda verde traída del libro 7 + fila de CUADRE.
R_CRUCE = R_TOT + 11
R_CRUCE_USO = R_CRUCE + 1
R_CRUCE_DIF = R_CRUCE + 2
R_CRUCE_VER = R_CRUCE + 3
#: Los dos escenarios de dotación publicados (D23c), SIN aritmética.
R_ESC = R_CRUCE + 6


# --------------------------------------------------------------------------
def nl(idd):
    n = D.nota_legal(idd)
    if n is None:
        raise SystemExit('nota_legal(%s) devolvió None: gate_legal debería '
                         'haberlo cazado antes.' % idd)
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
    '1. Hoja «Parámetros»: los metros del local, el precio por m2 de la obra, '
    'los tipos de IVA, la renta, el horizonte de comparación y los kilos de '
    'plástico que importas. Todo lo que calcula el libro sale de aquí.',
    '2. Hoja «CAPEX por Bloque»: una fila por partida. Escribe el mínimo y el '
    'máximo que te hayan presupuestado y el importe con el que trabajas, di si '
    'ESE importe lleva IVA y a qué tipo, y marca «No» en lo que no vayas a '
    'comprar. La hoja lleva todo a base imponible antes de sumar, que es la '
    'única forma de que el total signifique algo. Abajo va el cruce con el '
    'libro 7: el fondo de maniobra llega YA CALCULADO de allí.',
    '3. Hoja «Variante del Formato»: tu chocolatería puede no ser la del '
    'ejemplo. Tres variantes -bombonería, bean-to-bar y taza y churros-, la '
    'lista de la compra del bean-to-bar SIN precios inventados, y la '
    'comparación con la franquicia.',
    '4. Hoja «Traspaso vs Obra Nueva»: el precio del traspaso no es lo que '
    'cuesta el traspaso. Mete la renta de los dos casos, los meses que estarás '
    'parado en cada uno y los años del contrato, y compara el coste completo. '
    'Abajo, ocho traspasos reales para que veas la horquilla.',
    '5. Hoja «IVA y Tesorería»: cuánto IVA adelantas, cuándo vuelve, cuánta '
    'caja tienes que tener el día que abres y si el impuesto al plástico te '
    'afecta o no. Es la hoja que más sorprende.',
    '6. Hoja «Resumen»: las cifras que hay que llevar al banco, todas '
    'calculadas desde las hojas anteriores.',
]

NOTAS_LIBRO = [
    'LA COLUMNA «¿EL PRECIO LLEVA IVA?» ES LA QUE HACE QUE LA SUMA SIRVA. Unos '
    'distribuidores publican con IVA, otros sin él, y hay fichas que no lo '
    'dicen: en este presupuesto la vitrina viene con base SIN IVA declarada y '
    'las máquinas de templado, con base NO DECLARADA. Sumar los dos tipos de '
    'precio desvía la inversión un 21 % y no lo ve nadie, porque el total sale '
    '«razonable». Aquí cada línea declara la base de SU FUENTE y, aparte, la '
    'del importe que escribes tú.',
    'LO QUE NO TIENE PRECIO PUBLICADO VIENE MARCADO «SUPUESTO», Y LO QUE TIENE '
    'RANGO VIENE COMO RANGO. Los moldes de policarbonato NO son «24 x 30 €»: '
    'el único dato medido es 24,20-42,83 € por unidad, así que 24 moldes valen '
    'entre 580,80 y 1.027,92 €, y el valor por defecto es el punto medio. El '
    'mantenedor es un «desde 570 €», que es un suelo comercial y no el precio '
    'de la unidad que vas a comprar. Escribir una multiplicación con un precio '
    'unitario elegido a ojo es el error que esta guía no comete.',
    'EL FONDO DE MANIOBRA NO SE CALCULA AQUÍ, Y ES A PROPÓSITO. Es «meses de '
    'colchón x gastos fijos mensuales», y los dos factores viven en el libro 7 '
    '(plan financiero), que es donde están los gastos fijos. Así que este '
    'libro no te pide los meses de colchón: recibe el fondo YA CALCULADO en '
    'una celda verde y lo cuadra. Si cada libro lo calculase por su cuenta, los '
    'dos publicarían dos inversiones totales distintas con el mismo nombre, y '
    'ésa es exactamente la clase de error que se paga delante del banco.',
    'EL PRECIO DE UN TRASPASO NO ES LO QUE CUESTA UN TRASPASO. Los ocho de la '
    'tabla son precios PEDIDOS en anuncios leídos el 12-09-2026, no precios '
    'pagados, y ninguno viene con su cuenta de resultados. Sirven para ver la '
    'horquilla y para negociar, nunca para valorar un negocio. Y tres de ellos '
    'son de churrería-chocolatería, que es OTRO formato: están marcados.',
    'LA FIANZA NO ES UN GASTO Y EL PACKAGING TAMPOCO ES INVERSIÓN. La primera '
    'es un depósito que vuelve; el segundo son existencias. Los dos hay que '
    'tenerlos el día de la firma, así que están en el CAPEX, pero salen de la '
    'comparación con cualquier presupuesto de obra y equipamiento: si no, '
    'estarías comparando dos cosas distintas.',
    'LAS DOS CIFRAS DE DOTACIÓN QUE CIRCULAN POR AHÍ NO SON PRESUPUESTOS DE '
    'APERTURA. El arranque mínimo con atemperadora de sobremesa y el '
    'profesional con continua se diferencian en un factor 4, y ése es el '
    'hallazgo que hay que quedarse: cualquier cifra publicada que no diga cuál '
    'de los dos describe no sirve para decidir nada. Los dos rangos están en '
    'la hoja de CAPEX, con su etiqueta pegada, y esta guía NO los resta ni los '
    'compara como si fueran cifras fiscales, porque mezclan bases de IVA.',
]

CADENCIA = ('Cadencia: se rellena UNA VEZ al preparar el plan y se revisa cada '
            'vez que entra un presupuesto nuevo, hasta la firma. Después de '
            'abrir sólo se vuelve a él para comparar lo presupuestado con lo '
            'gastado de verdad -que es la hoja «Equipamiento» del libro 9- y '
            'eso es lo que enseña a presupuestar el siguiente.')


def hoja_instrucciones(wb):
    ws = wb.create_sheet('Instrucciones', 0)
    C.anchos(ws, {'A': 46, 'B': 46, 'C': 46})
    motor.val(ws, 'A1', TITULO)
    ws['A1'].font = Font(bold=True, size=16, color=C.ORO)
    ws.row_dimensions[1].height = 30
    motor.val(ws, 'A2', C.SUBTITULO)
    motor.val(ws, 'A3', 'Para qué sirve: saber cuánto dinero necesitas de '
                        'verdad para abrir una chocolatería, y si sale mejor '
                        'un traspaso o una obra nueva.')
    ws['A3'].font = Font(italic=True, size=9)

    C.seccion(ws, 'A5', 'Instrucciones de uso')
    fila = 6
    for paso in PASOS:
        ws.merge_cells('A%d:C%d' % (fila, fila))
        motor.val(ws, 'A%d' % fila, paso, wrap=True)
        ws.row_dimensions[fila].height = 68
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
        ws.row_dimensions[fila].height = 80
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
         'Libro 9: checklist-equipamiento-y-proveedores-cacao.xlsx',
         'Aquí la máquina entra sólo por su importe. El plazo de entrega no '
         'cambia el CAPEX: cambia la fecha de apertura, y eso es el libro 8.'),
        ('El P&L a tres años, la tesorería mes a mes, los gastos fijos y el '
         'cuadro de la deuda',
         'Libro 7: plan-financiero-3-anos-chocolateria.xlsx',
         'De ese libro sale el FONDO DE MANIOBRA ya calculado, que aquí llega '
         'en una celda verde con su fila de cuadre. Los meses de colchón se '
         'deciden allí, no aquí: si se decidieran en los dos sitios, el fondo '
         'se calcularía dos veces.'),
        ('Si ese local sirve, si se puede climatizar y cuántos bombones al día '
         'aguanta el equipo',
         'Libro 1: capacidad-obrador-y-clima.xlsx',
         'Comprar bien empieza por saber qué necesitas, no cuánto cuesta. Los '
         'dos libros comparten los mismos 75 m2 y la misma columna de IVA.'),
        ('Qué papeles te tocan, en qué orden y cuándo abres',
         'Libro 8: checklist-legal-licencias-y-cacao.xlsx',
         'Las tasas, el proyecto técnico y la comunicación al registro '
         'autonómico están aquí como IMPORTE; el procedimiento y el calendario, '
         'allí.'),
        ('Cómo funciona el impuesto al plástico y qué tienes que registrar',
         'Capítulo 13 de la guía',
         'Esta hoja sólo emite la ALERTA cuando pasas el umbral de los 5 kg al '
         'mes. Explicarlo entero dentro de una calculadora sería esconder la '
         'explicación donde nadie la lee.'),
        # B11 (refutación 2026-09-12): este era el único libro del pack sin
        # cruzarse con el Kit de Tareas Chocolatería, y sin la frase que evita
        # que el comprador crea que la guía repite lo que ya tiene.
        ('Presupuestos de proveedor por partida y hoja de compra',
         'kit-tareas-chocolateria/02-partidas-produccion.xlsx (kit de 12 €)',
         'El kit trae la plantilla de negociación por proveedor; esta '
         'calculadora sólo suma lo que ya has decidido comprar. No cubre la '
         'inversión: es la ficha con la que la negocias.'),
    ]
    for que, donde, porque in FRONTERAS:
        motor.val(ws, 'A%d' % fila, que, wrap=True)
        motor.val(ws, 'B%d' % fila, donde, wrap=True)
        motor.val(ws, 'C%d' % fila, porque, wrap=True)
        ws.row_dimensions[fila].height = 62
        fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila,
              'Es COPIA declarada, no vínculo: en toda la guía no hay ni una '
              'fórmula que apunte a otro fichero. Un enlace entre libros se '
              'rompe en cuanto alguien mueve una carpeta, y entonces el libro '
              'miente sin avisar. Donde una celda verde trae un dato de otro '
              'libro, viene con su valor por defecto declarado y con una fila '
              'de CUADRE que te avisa si lo que has tecleado se aleja del '
              'origen.', wrap=True)
    ws['A%d' % fila].font = Font(italic=True, size=9)
    ws.row_dimensions[fila].height = 62
    fila += 2

    C.seccion(ws, 'A%d' % fila, 'Cada cuánto se usa este libro')
    fila += 1
    ws.merge_cells('A%d:C%d' % (fila, fila))
    motor.val(ws, 'A%d' % fila, CADENCIA, wrap=True)
    ws.row_dimensions[fila].height = 56
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
    C.anchos(ws, {'A': 52, 'B': 16, 'C': 18, 'D': 22, 'E': 86})
    C.encabezar(ws, 'Parámetros',
                'Todo lo que el libro calcula sale de aquí. Ni un número vive '
                'dentro de una fórmula.', col_fin='E')
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
        elif unidad in ('€', '€/mes', '€/m2', '€/kg'):
            motor.val(ws, 'B%d' % fila, float(valor), fmt=C.FMT_EUR,
                      verde_=True)
        elif unidad in ('m2', 'kg al mes'):
            motor.val(ws, 'B%d' % fila, float(valor), fmt=C.FMT_DEC1,
                      verde_=True)
        else:
            motor.val(ws, 'B%d' % fila, valor, fmt=C.FMT_ENT, verde_=True)
        motor.val(ws, 'C%d' % fila, unidad)
        motor.val(ws, 'D%d' % fila, fuente)
        motor.val(ws, 'E%d' % fila, notatxt, wrap=True)
        ws.row_dimensions[fila].height = 50

    motor.f(ws, 'B%d' % fp(P_OBRA),
            motor.iferror('B%d*B%d' % (fp(P_M2), fp(P_EURM2))), fmt=C.FMT_EUR)
    nota_legal_celda(ws, 'A%d' % fp(P_IVA_PROD), 'CHN-71')
    nota_legal_celda(ws, 'A%d' % fp(P_UMBRAL_PLAST), 'CHN-62b')
    nota_legal_celda(ws, 'A%d' % fp(P_TIPO_PLAST), 'CHN-62')

    fila = fp(len(PARAMS_LIBRO)) + 1
    C.parrafo(ws, fila,
              'AQUÍ NO ESTÁN LOS MESES DE COLCHÓN DE TESORERÍA, Y NO ES UN '
              'OLVIDO. El fondo de maniobra es «meses de colchón x gastos '
              'fijos mensuales», y los DOS factores viven en el libro 7, que es '
              'donde se calculan los gastos fijos. Este libro recibe el fondo '
              'YA CALCULADO en la celda verde del cruce, al pie de la hoja '
              '«CAPEX por Bloque». Si lo pidiera aquí, el fondo se calcularía '
              'dos veces y los dos libros publicarían dos inversiones totales '
              'distintas con el mismo nombre.',
              col_ini='A', col_fin='E', alto=68)
    fila += 2
    C.parrafo(ws, fila,
              'Los valores marcados «supuesto» son los de la bombonería de '
              'ejemplo «La Almendra» (75 m2 en una ciudad media española, '
              'obrador propio y tienda a calle). NO son datos de sector: son un '
              'punto de partida coherente para que puedas ver el libro '
              'funcionando antes de meter los tuyos.',
              col_ini='A', col_fin='E', alto=48)
    C.pagina(ws, apaisado=True, titulos='5:5')
    return ws


# --------------------------------------------------------------------------
def hoja_capex(wb):
    ws = wb.create_sheet(H_CAP)
    C.anchos(ws, {'A': 5, 'B': 30, 'C': 48, 'D': 13, 'E': 22, 'F': 15,
                  'G': 13, 'H': 11, 'I': 14, 'J': 14, 'K': 14, 'L': 14,
                  'M': 14, 'N': 14, 'O': 40, 'P': 86})
    C.encabezar(ws, 'CAPEX por bloque',
                'Nueve bloques, y el fondo de maniobra tiene fila propia '
                'porque llega del libro 7. Todas las líneas se llevan a base '
                'imponible antes de sumar: sin la columna de IVA, el total se '
                'desvía un 21 %.', col_fin='P')
    C.cabecera(ws, 5, [
        ('A', 'Nº'), ('B', 'Bloque'), ('C', 'Partida'), ('D', '¿La compras?'),
        ('E', 'Procedencia'), ('F', 'Base declarada por la fuente'),
        ('G', '¿Tu precio lleva IVA?'), ('H', 'Tipo de IVA'), ('I', 'Mínimo'),
        ('J', 'Máximo'), ('K', 'Tu importe'), ('L', 'Base sin IVA'),
        ('M', 'IVA soportado'), ('N', 'Total con IVA'),
        ('O', 'Cómo se publica el precio'), ('P', 'Nota')], altura=58)

    ref_iva = {'IVA_GEN': "'%s'!$B$%d" % (H_PAR, fp(P_IVA_GEN)),
               'IVA_CERO': "'%s'!$B$%d" % (H_PAR, fp(P_IVA_CERO))}
    fila = X_INI
    for i, (bloque, partida, comprar, proc, base, lleva, tipo, minimo, maximo,
            importe, horq, notatxt, idl) in enumerate(LINEAS):
        motor.val(ws, 'A%d' % fila, i + 1, fmt=C.FMT_ENT)
        motor.val(ws, 'B%d' % fila, ROTULO_BLOQUE[bloque], wrap=True)
        motor.val(ws, 'C%d' % fila, partida, wrap=True)
        motor.val(ws, 'D%d' % fila, comprar, verde_=True)
        motor.val(ws, 'E%d' % fila, proc, wrap=True)
        motor.val(ws, 'F%d' % fila, base)
        motor.val(ws, 'G%d' % fila, lleva, verde_=True)
        motor.f(ws, 'H%d' % fila, '=' + ref_iva[tipo], fmt=C.FMT_PCT)
        if minimo == 'FORMULA_OBRA':
            origen = "='%s'!B%d" % (H_PAR, fp(P_OBRA))
            for col in ('I', 'J', 'K'):
                motor.f(ws, '%s%d' % (col, fila), origen, fmt=C.FMT_EUR)
        elif minimo == 'FORMULA_FIANZA':
            origen = motor.iferror("'%s'!B%d*'%s'!B%d"
                                   % (H_PAR, fp(P_RENTA), H_PAR,
                                      fp(P_FIANZA)))
            for col in ('I', 'J', 'K'):
                motor.f(ws, '%s%d' % (col, fila), origen, fmt=C.FMT_EUR)
        elif minimo == 'VERDE_FONDO':
            # A6 (refutación 2026-09-12): antes eran TRES celdas verdes
            # independientes con el mismo importe -el lector lo tecleaba dos
            # veces, y la fila de CUADRE comparaba el libro contra sí mismo,
            # no contra el libro 7-. Ahora son FÓRMULA sobre la ÚNICA celda
            # verde del concepto, el cruce 2 <- 7 de más abajo (`R_CRUCE`,
            # fila %d): mismo patrón que `FORMULA_OBRA`/`FORMULA_FIANZA`.
            origen = '=$L$%d' % R_CRUCE
            for col in ('I', 'J', 'K'):
                motor.f(ws, '%s%d' % (col, fila), origen, fmt=C.FMT_EUR)
        else:
            motor.val(ws, 'I%d' % fila, minimo, fmt=C.FMT_EUR, verde_=True)
            motor.val(ws, 'J%d' % fila, maximo, fmt=C.FMT_EUR, verde_=True)
            motor.val(ws, 'K%d' % fila, importe, fmt=C.FMT_EUR, verde_=True)
        motor.f(ws, 'L%d' % fila,
                '=IF(D%d="No","",IFERROR(IF(G%d="Sí",K%d/(1+H%d),K%d),""))'
                % (fila, fila, fila, fila, fila), fmt=C.FMT_EUR)
        motor.f(ws, 'M%d' % fila,
                '=IF(L%d="","",IFERROR(L%d*H%d,""))' % (fila, fila, fila),
                fmt=C.FMT_EUR)
        motor.f(ws, 'N%d' % fila,
                '=IF(L%d="","",IFERROR(L%d+M%d,""))' % (fila, fila, fila),
                fmt=C.FMT_EUR)
        motor.val(ws, 'O%d' % fila, horq, wrap=True)
        motor.val(ws, 'P%d' % fila, notatxt, wrap=True)
        if idl:
            nota_legal_celda(ws, 'P%d' % fila, idl)
        ws.row_dimensions[fila].height = 56
        fila += 1

    C.seccion(ws, 'B%d' % (X_FIN + 2), 'Resumen por bloque (los NUEVE)')
    for k, bloque in enumerate(D.BLOQUES_CAPEX):
        f = B_INI + k
        motor.val(ws, 'C%d' % f, ROTULO_BLOQUE[bloque])
        for col in ('L', 'M', 'N'):
            motor.f(ws, '%s%d' % (col, f),
                    '=SUMIF($B$%d:$B$%d,C%d,%s$%d:%s$%d)'
                    % (X_INI, X_FIN, f, col, X_INI, col, X_FIN),
                    fmt=C.FMT_EUR)
        motor.f(ws, 'O%d' % f, motor.iferror('L%d/$L$%d' % (f, R_TOT)),
                fmt=C.FMT_PCT)
    motor.val(ws, 'C%d' % R_TOT, 'CAPEX TOTAL (los nueve bloques)', bold=True)
    for col in ('L', 'M', 'N'):
        motor.f(ws, '%s%d' % (col, R_TOT),
                '=SUM(%s%d:%s%d)' % (col, B_INI, col, B_FIN), fmt=C.FMT_EUR,
                bold=True)
        C.destacado(ws, '%s%d' % (col, R_TOT))
    motor.val(ws, 'C%d' % R_IVA, 'Del cual, IVA que hay que adelantar')
    motor.f(ws, 'L%d' % R_IVA, '=M%d' % R_TOT, fmt=C.FMT_EUR)
    motor.val(ws, 'C%d' % R_CIVA, 'Desembolso total con IVA')
    motor.f(ws, 'L%d' % R_CIVA, '=N%d' % R_TOT, fmt=C.FMT_EUR, bold=True)

    i_fondo = D.BLOQUES_CAPEX.index('Fondo de maniobra')
    motor.val(ws, 'C%d' % R_SINFONDO,
              'CAPEX SIN el fondo de maniobra (la cifra que viaja al libro 7)',
              bold=True, wrap=True)
    motor.f(ws, 'L%d' % R_SINFONDO,
            motor.iferror('L%d-L%d' % (R_TOT, B_INI + i_fondo)),
            fmt=C.FMT_EUR, bold=True)
    C.destacado(ws, 'L%d' % R_SINFONDO)
    motor.val(ws, 'P%d' % R_SINFONDO,
              'ES ESTA LÍNEA, Y NO EL TOTAL, LA QUE VIAJA AL LIBRO 7 (cruce '
              '7 <- 2). El total incluye el bloque «fondo de maniobra», y el '
              'libro 7 vuelve a dotar el fondo con sus propios meses de '
              'colchón: llevarle el total entero lo contaría DOS VECES y '
              'publicaría dos inversiones totales distintas para la misma '
              'bombonería.', wrap=True)
    ws.row_dimensions[R_SINFONDO].height = 62
    motor.val(ws, 'C%d' % R_FONDO,
              'Del cual, fondo de maniobra (es caja, no inversión)', wrap=True)
    motor.f(ws, 'L%d' % R_FONDO, '=L%d' % (B_INI + i_fondo), fmt=C.FMT_EUR)
    motor.val(ws, 'C%d' % R_INV, 'INVERSIÓN TOTAL (las dos líneas de arriba)',
              bold=True)
    motor.f(ws, 'L%d' % R_INV,
            motor.iferror('L%d+L%d' % (R_SINFONDO, R_FONDO)), fmt=C.FMT_EUR,
            bold=True)
    C.destacado(ws, 'L%d' % R_INV)

    motor.val(ws, 'C%d' % R_COMP,
              'Subtotal COMPARABLE con un presupuesto de obra y equipamiento '
              '(seis bloques)', wrap=True)
    motor.f(ws, 'L%d' % R_COMP,
            '=' + '+'.join('L%d' % (B_INI + D.BLOQUES_CAPEX.index(b))
                           for b in D.BLOQUES_COMPARABLES), fmt=C.FMT_EUR,
            bold=True)
    motor.val(ws, 'P%d' % R_COMP,
              'Obra y adecuación, climatización, equipo de templado y '
              'moldeado, frío, mobiliario y tienda, y TPV/rótulo. Fuera quedan '
              'ENTEROS «fianza y licencias» (un depósito y unas tasas), '
              '«packaging y moldes» (existencias) y el fondo de maniobra '
              '(caja): un depósito no se compara contra un presupuesto de obra. '
              'Y el bloque de fianza y licencias sale entero, no medio: '
              'partirlo para rescatar las licencias sería inventar un décimo '
              'bloque sin dato propio.', wrap=True)
    ws.row_dimensions[R_COMP].height = 68

    # --- cruce 2 <- 7: fondo de maniobra ---------------------------------
    C.seccion(ws, 'B%d' % (R_CRUCE - 1),
              'Cruce con el libro 7: el fondo de maniobra llega ya calculado')
    motor.val(ws, 'C%d' % R_CRUCE,
              'Trae aquí el fondo de maniobra de '
              'plan-financiero-3-anos-chocolateria.xlsx!Inversión Inicial!B16',
              wrap=True)
    motor.val(ws, 'L%d' % R_CRUCE, round(D.fondo_maniobra(), 2),
              fmt=C.FMT_EUR, verde_=True)
    motor.val(ws, 'P%d' % R_CRUCE,
              'VALOR POR DEFECTO DECLARADO: seis meses de los gastos fijos de '
              'La Almendra en velocidad de crucero. Es un SUPUESTO, como los '
              'dos factores de los que sale. En cuanto tengas tu libro 7 '
              'relleno, copia aquí SU cifra: no la calcules otra vez.',
              wrap=True)
    ws.row_dimensions[R_CRUCE].height = 56
    motor.val(ws, 'C%d' % R_CRUCE_USO,
              'Fondo de maniobra que está usando la fila del bloque', wrap=True)
    motor.f(ws, 'L%d' % R_CRUCE_USO, '=K%d' % (X_FIN,), fmt=C.FMT_EUR)
    motor.val(ws, 'C%d' % R_CRUCE_DIF, 'Diferencia')
    motor.f(ws, 'L%d' % R_CRUCE_DIF,
            motor.iferror('L%d-L%d' % (R_CRUCE_USO, R_CRUCE)), fmt=C.FMT_EUR)
    motor.val(ws, 'C%d' % R_CRUCE_VER, 'CUADRE DEL FONDO DE MANIOBRA',
              bold=True)
    motor.f(ws, 'L%d' % R_CRUCE_VER,
            '=IF(OR(L%d="",L%d=""),"",IF(ABS(L%d)<0.01,"CUADRA",'
            '"NO CUADRA: alguien ha pisado la fila del bloque"))'
            % (R_CRUCE, R_CRUCE_USO, R_CRUCE_DIF), bold=True)
    C.destacado(ws, 'L%d' % R_CRUCE_VER)
    motor.semaforo_texto(ws, 'L%d' % R_CRUCE_VER,
                         (('NO CUADRA: alguien ha pisado la fila del bloque',
                           motor.CF_ROJO_BG, motor.CF_ROJO_FG),
                          ('CUADRA', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    motor.val(ws, 'P%d' % R_CRUCE_VER,
              'En toda la guía NO hay una sola fórmula que apunte a otro '
              'fichero: un enlace entre libros se rompe en cuanto alguien mueve '
              'una carpeta, y entonces el libro miente sin avisar. Lo que hay '
              'es esto: una celda verde con su valor por defecto y una fila que '
              'te dice, a la cara, si la fila del bloque y la cifra traída del '
              'libro 7 han dejado de decir lo mismo.', wrap=True)
    ws.row_dimensions[R_CRUCE_VER].height = 68

    # --- los dos escenarios publicados (D23c), SIN aritmética -------------
    C.seccion(ws, 'B%d' % (R_ESC - 1),
              'Los dos escenarios de dotación que se publican, con su etiqueta '
              'pegada')
    C.cabecera(ws, R_ESC, [('C', 'Escenario'), ('I', 'Mínimo publicado'),
                           ('J', 'Máximo publicado'), ('K', 'Fuente'),
                           ('O', 'Etiqueta'), ('P', 'Qué incluye')],
               altura=30)
    fila = R_ESC + 1
    for clave in ('A', 'B'):
        e = D.ESCENARIOS_DOTACION[clave]
        motor.val(ws, 'C%d' % fila, e['nombre'], wrap=True)
        motor.val(ws, 'I%d' % fila, e['min'], fmt=C.FMT_EUR)
        motor.val(ws, 'J%d' % fila, e['max'], fmt=C.FMT_EUR)
        motor.val(ws, 'K%d' % fila, e['fuente'])
        motor.val(ws, 'O%d' % fila, e['etiqueta'], wrap=True)
        motor.val(ws, 'P%d' % fila, e['nota'], wrap=True)
        ws.row_dimensions[fila].height = 62
        fila += 1
    f_dot = fila
    i_tm = D.BLOQUES_CAPEX.index('Equipo de templado y moldeado')
    motor.val(ws, 'C%d' % f_dot,
              'Tu equipo de templado y moldeado, en base imponible')
    motor.f(ws, 'I%d' % f_dot, '=L%d' % (B_INI + i_tm), fmt=C.FMT_EUR)
    f_pos = f_dot + 1
    motor.val(ws, 'C%d' % f_pos,
              '¿Dónde cae respecto al escenario profesional de entrada?',
              bold=True)
    motor.f(ws, 'I%d' % f_pos,
            '=IF(I%d="","",IF(I%d<I%d,"Por debajo del rango publicado",'
            'IF(I%d>J%d,"Por encima del rango publicado",'
            '"Dentro del rango publicado")))'
            % (f_dot, f_dot, R_ESC + 1, f_dot, R_ESC + 1), bold=True)
    C.destacado(ws, 'I%d' % f_pos)
    motor.val(ws, 'P%d' % f_pos,
              'ES UNA POSICIÓN, NO UNA DESVIACIÓN, y por eso no hay ningún '
              'porcentaje en esta celda. Los dos escenarios publicados mezclan '
              'bases de IVA -seis líneas con base no declarada, una «sin '
              'impuestos» y otra con un indicio «/Neto» no confirmable-, así '
              'que restarlos de tu presupuesto o compararlos entre sí como si '
              'fueran cifras fiscales está prohibido en esta guía. Lo que sí se '
              'conserva es el hallazgo: entre el arranque mínimo y el '
              'profesional de entrada hay un FACTOR 4, y cualquier cifra de '
              'inversión publicada que no diga cuál de los dos describe no '
              'sirve para decidir nada.', wrap=True)
    ws.row_dimensions[f_pos].height = 90

    fila = f_pos + 3
    refs, fila = C.bloque_listas(
        ws, fila, [('¿La compras?', SI_NO), ('¿Lleva IVA?', SI_NO)], col='C')
    C.dv_rango(ws, ['D%d' % r for r in range(X_INI, X_FIN + 1)],
               refs['¿La compras?'], '¿La compras?',
               'Elige «Sí» o «No» de la lista.')
    C.dv_rango(ws, ['G%d' % r for r in range(X_INI, X_FIN + 1)],
               refs['¿Lleva IVA?'], '¿Tu precio lleva IVA?',
               'Elige «Sí» o «No» de la lista.')
    C.parrafo(ws, fila,
              'Mínimo y máximo son para TUS presupuestos: vienen sembrados con '
              'el mismo valor de partida salvo donde la fuente publica un rango '
              '-los moldes de policarbonato-, y en cuanto tengas dos ofertas de '
              'verdad se ve de un vistazo cuánto se mueve cada partida. El '
              'total sólo usa «tu importe». Y la columna «Base declarada por la '
              'fuente» no es decorativa: dice si el precio que has copiado de '
              'una ficha venía con IVA, sin él, o sin decirlo.',
              col_ini='C', col_fin='P', alto=62)
    C.pagina(ws, apaisado=True, titulos='5:5')
    return ws


# --------------------------------------------------------------------------
# Hoja «Variante del Formato»  (D1, D2, D11)
# --------------------------------------------------------------------------
V_TAB = 6


def hoja_variante(wb):
    ws = wb.create_sheet(H_VAR)
    C.anchos(ws, {'A': 5, 'B': 44, 'C': 20, 'D': 16, 'E': 16, 'F': 16,
                  'G': 16, 'H': 88})
    C.encabezar(ws, 'Variante del formato',
                'Tu chocolatería puede no ser la del ejemplo. Tres variantes, '
                'y dos de ellas SIN cifras de maquinaria a propósito: no hay '
                'precio público verificado, y lo que se entrega es la lista de '
                'la compra y las preguntas.', col_fin='H')

    # --- las tres variantes ----------------------------------------------
    C.seccion(ws, 'B5', 'Las tres variantes, y qué cambia en cada una')
    C.cabecera(ws, V_TAB, [('B', 'Variante'), ('C', 'Fuente'),
                           ('D', '¿Es la tuya?'),
                           ('E', 'CAPEX extra cifrable'),
                           ('H', 'Qué cambia, y qué NO se puede cifrar')],
               altura=40)
    fila = V_TAB + 1
    V_FILA = {}
    V_FILA['bombonería'] = fila
    motor.val(ws, 'B%d' % fila,
              'Bombonería con obrador propio y tienda a calle (el caso de esta '
              'guía)', wrap=True)
    motor.val(ws, 'C%d' % fila, 'CHS-03')
    motor.val(ws, 'D%d' % fila, 'Sí', verde_=True)
    motor.f(ws, 'E%d' % fila, "='%s'!L%d" % (H_CAP, R_INV), fmt=C.FMT_EUR)
    motor.val(ws, 'H%d' % fila,
              'Es el eje del producto y el caso que calcula la hoja «CAPEX por '
              'Bloque» entera: 60-100 m2 y 1-2 empleados. Las otras dos son '
              'columnas de escenario, no productos aparte.', wrap=True)
    ws.row_dimensions[fila].height = 56
    fila += 1

    V_FILA['bean'] = fila
    v = D.VARIANTES['bean-to-bar']
    motor.val(ws, 'B%d' % fila, v['nombre'], wrap=True)
    motor.val(ws, 'C%d' % fila, v['fuente'])
    motor.val(ws, 'D%d' % fila, 'No', verde_=True)
    motor.val(ws, 'E%d' % fila, 'Sin cifra')
    motor.val(ws, 'H%d' % fila, v['nota'], wrap=True)
    ws.row_dimensions[fila].height = 120
    nota_legal_celda(ws, 'H%d' % fila, 'CHN-25')
    fila += 1

    V_FILA['taza'] = fila
    t = D.VARIANTES['taza-y-churros']
    motor.val(ws, 'B%d' % fila, t['nombre'], wrap=True)
    motor.val(ws, 'C%d' % fila, t['fuente'])
    motor.val(ws, 'D%d' % fila, 'No', verde_=True)
    motor.val(ws, 'E%d' % fila, t['equipos_con_precio'][0][1], fmt=C.FMT_EUR)
    motor.val(ws, 'H%d' % fila, t['nota'], wrap=True)
    ws.row_dimensions[fila].height = 120
    nota_legal_celda(ws, 'H%d' % fila, 'CHN-49c')
    fila += 1
    v_fin = fila - 1
    motor.val(ws, 'F%d' % V_FILA['taza'], 'Sólo la chocolatera')
    motor.val(ws, 'G%d' % V_FILA['taza'], t['equipos_con_precio'][0][3])

    # --- bean-to-bar: lista de la compra y preguntas ----------------------
    bt = v_fin + 2
    C.seccion(ws, 'B%d' % bt,
              'Bean-to-bar: la lista de la compra, SIN precios inventados')
    ws.merge_cells('B%d:H%d' % (bt + 1, bt + 1))
    motor.val(ws, 'B%d' % (bt + 1),
              'NO HAY UNA SOLA CIFRA DE MAQUINARIA EN ESTE BLOQUE, Y ES A '
              'PROPÓSITO. Los catálogos existen y están verificados, pero los '
              'precios NO son públicos: se vende a presupuesto, o la tienda '
              'está fuera de la UE y el precio puesto en España depende del '
              'transporte y de la aduana. Inventarlos sería justo el patrón que '
              'esta casa prohíbe. Lo que sí se entrega es la lista de lo que '
              'hay que comprar y las cinco preguntas que hay que hacer antes de '
              'pedir un número.', wrap=True)
    ws['B%d' % (bt + 1)].font = Font(italic=True, size=9)
    ws.row_dimensions[bt + 1].height = 72
    C.cabecera(ws, bt + 2, [('B', 'Equipo del tren bean-to-bar'),
                            ('D', '¿Lo necesitas?'),
                            ('E', '¿Tienes presupuesto por escrito?'),
                            ('H', 'Qué mirar')], altura=30)
    fila = bt + 3
    B_LISTA_INI = fila
    coords_nec, coords_esc = [], []
    NOTAS_BEAN = {
        'Tostador de grano': 'El equipo que te puede meter en el CAPCA: la '
                             'nota (2) de su Anexo sube de grupo C a B cuando '
                             'la actividad se desarrolla a menos de 500 m de '
                             'un núcleo de población, es decir, en ciudad '
                             'SIEMPRE. Y ojo: «cacao» y «chocolate» tienen 0 '
                             'ocurrencias en el CAPCA, así que encajar el '
                             'tostado en «café o similares» es INTERPRETACIÓN, '
                             'no mención expresa.',
        'Winnower (aventadora)': 'Junto con el tostador, el equipo ruidoso de '
                                 'un obrador que por lo demás es silencioso. '
                                 'Pregunta los dB a un metro antes de firmar '
                                 'el alquiler.',
        'Melanger o refinadora de piedra': 'Trabaja durante días seguidos: su '
                                           'consumo es un gasto fijo del libro '
                                           '7, no una compra.',
    }
    for eq in v['lista_de_la_compra']:
        motor.val(ws, 'B%d' % fila, eq, wrap=True)
        motor.val(ws, 'D%d' % fila, 'Por decidir', verde_=True)
        coords_nec.append('D%d' % fila)
        motor.val(ws, 'E%d' % fila, 'Por pedir', verde_=True)
        coords_esc.append('E%d' % fila)
        motor.val(ws, 'H%d' % fila, NOTAS_BEAN.get(eq, ''), wrap=True)
        ws.row_dimensions[fila].height = 40 if eq not in NOTAS_BEAN else 72
        fila += 1
    B_LISTA_FIN = fila - 1
    nota_legal_celda(ws, 'H%d' % B_LISTA_INI, 'CHN-47b')

    fila += 1
    C.seccion(ws, 'B%d' % fila, 'Las cinco preguntas al proveedor de '
                                'bean-to-bar')
    fila += 1
    B_PREG_INI = fila
    for preg in v['preguntas_al_proveedor']:
        motor.val(ws, 'B%d' % fila, preg, wrap=True)
        ws.merge_cells('B%d:C%d' % (fila, fila))
        motor.val(ws, 'E%d' % fila, 'Por pedir', verde_=True)
        coords_esc.append('E%d' % fila)
        ws.row_dimensions[fila].height = 52
        fila += 1
    B_PREG_FIN = fila - 1

    fila += 1
    B_CONT = fila
    motor.val(ws, 'B%d' % fila, 'Equipos del tren que dices necesitar')
    motor.f(ws, 'E%d' % fila,
            '=COUNTIF(D%d:D%d,"Sí")' % (B_LISTA_INI, B_LISTA_FIN),
            fmt=C.FMT_ENT)
    motor.val(ws, 'B%d' % (fila + 1),
              'Respuestas que ya tienes por escrito (equipos y preguntas)')
    motor.f(ws, 'E%d' % (fila + 1),
            '=COUNTIF(E%d:E%d,"Sí")+COUNTIF(E%d:E%d,"Sí")'
            % (B_LISTA_INI, B_LISTA_FIN, B_PREG_INI, B_PREG_FIN),
            fmt=C.FMT_ENT)
    motor.val(ws, 'B%d' % (fila + 2), 'VEREDICTO DEL BEAN-TO-BAR', bold=True)
    motor.f(ws, 'E%d' % (fila + 2),
            '=IF(E%d=0,"No es tu variante: no hay nada que presupuestar",'
            'IF(E%d=0,"No tienes ni un precio: no puedes presupuestar esto '
            'todavía","Tienes presupuestos: llévalos al CAPEX como partidas"))'
            % (fila, fila + 1), bold=True)
    C.destacado(ws, 'E%d' % (fila + 2))
    motor.semaforo_texto(ws, 'E%d' % (fila + 2),
                         (('No tienes ni un precio: no puedes presupuestar '
                           'esto todavía', motor.CF_AMBAR_BG,
                           motor.CF_AMBAR_FG),
                          ('No es tu variante: no hay nada que presupuestar',
                           motor.CF_GRIS_BG, motor.CF_GRIS_FG),
                          ('Tienes presupuestos: llévalos al CAPEX como '
                           'partidas', motor.CF_VERDE_BG,
                           motor.CF_VERDE_FG)))

    # --- taza y churros ---------------------------------------------------
    tz = B_CONT + 4
    C.seccion(ws, 'B%d' % tz,
              'Chocolatería de taza y churros: lo único cifrable y lo que no')
    C.cabecera(ws, tz + 1, [('B', 'Equipo'), ('C', 'Fuente'),
                            ('D', '¿Lo necesitas?'), ('E', 'Precio'),
                            ('F', 'Base de IVA'),
                            ('H', 'Qué mirar')], altura=30)
    fila = tz + 2
    T_INI = fila
    for nombre, precio, fuente, base in t['equipos_con_precio']:
        motor.val(ws, 'B%d' % fila, nombre, wrap=True)
        motor.val(ws, 'C%d' % fila, fuente)
        motor.val(ws, 'D%d' % fila, 'Por decidir', verde_=True)
        coords_nec.append('D%d' % fila)
        motor.val(ws, 'E%d' % fila, precio, fmt=C.FMT_EUR, verde_=True)
        motor.val(ws, 'F%d' % fila, base)
        motor.val(ws, 'H%d' % fila,
                  'Base SIN IVA declarada literalmente por la ficha. Es el '
                  'ÚNICO equipo de esta variante con precio verificado, y por '
                  'eso es el único que lleva número.', wrap=True)
        ws.row_dimensions[fila].height = 52
        fila += 1
    for nombre in t['equipos_sin_precio']:
        motor.val(ws, 'B%d' % fila, nombre, wrap=True)
        motor.val(ws, 'C%d' % fila, 'CHS-49 (sin precio verificado)')
        motor.val(ws, 'D%d' % fila, 'Por decidir', verde_=True)
        coords_nec.append('D%d' % fila)
        motor.val(ws, 'E%d' % fila, 'Sin cifra')
        motor.val(ws, 'H%d' % fila,
                  'SIN PRECIO VERIFICADO: no se publica ninguna cifra. '
                  'Presupuéstalo y llévalo al CAPEX como partida propia.',
                  wrap=True)
        ws.row_dimensions[fila].height = 44
        fila += 1
    T_FIN = fila - 1
    motor.val(ws, 'B%d' % fila, 'Obligación extra de esta variante', bold=True)
    ws.merge_cells('C%d:H%d' % (fila, fila))
    motor.val(ws, 'C%d' % fila, t['obligacion_extra'], wrap=True)
    ws.row_dimensions[fila].height = 56
    nota_legal_celda(ws, 'C%d' % fila, 'CHN-48')
    fila += 2

    # --- franquicia frente a independiente (D11) --------------------------
    fq = fila
    C.seccion(ws, 'B%d' % fq,
              'Franquicia frente a independiente: orden de magnitud publicado, '
              'nunca dato auditado')
    C.cabecera(ws, fq + 1, [('B', 'Marca'), ('C', 'Formato'),
                            ('D', 'Inversión desde'), ('E', 'Canon'),
                            ('F', 'm2 mínimos'), ('G', 'Fuente y fecha'),
                            ('H', 'Etiqueta y nota')], altura=40)
    fila = fq + 2
    FQ_INI = fila
    for fr in D.FRANQUICIAS:
        motor.val(ws, 'B%d' % fila, fr['marca'])
        motor.val(ws, 'C%d' % fila, fr['formato'], wrap=True)
        if fr['inversion_desde'] is not None:
            motor.val(ws, 'D%d' % fila, fr['inversion_desde'], fmt=C.FMT_EUR)
        else:
            motor.val(ws, 'D%d' % fila, 'Sin cifra con id')
        if fr['canon'] is not None:
            motor.val(ws, 'E%d' % fila, fr['canon'], fmt=C.FMT_EUR)
        else:
            motor.val(ws, 'E%d' % fila, 'Sin cifra con id')
        if fr['m2_minimos'] is not None:
            motor.val(ws, 'F%d' % fila, fr['m2_minimos'], fmt=C.FMT_ENT)
        else:
            motor.val(ws, 'F%d' % fila, '')
        motor.val(ws, 'G%d' % fila,
                  '%s%s' % (fr['fuente'],
                            ' · ' + fr['fecha_consulta']
                            if fr['fecha_consulta'] else ''))
        motor.val(ws, 'H%d' % fila,
                  '%s — %s' % (fr['etiqueta'], fr['nota']), wrap=True)
        ws.row_dimensions[fila].height = 96
        fila += 1
    FQ_FIN = fila - 1
    motor.val(ws, 'B%d' % fila, 'Tu inversión total como independiente',
              bold=True)
    motor.f(ws, 'D%d' % fila, "='%s'!L%d" % (H_CAP, R_INV), fmt=C.FMT_EUR,
            bold=True)
    f_fq_mia = fila
    fila += 1
    motor.val(ws, 'B%d' % fila,
              'Diferencia con la inversión «desde» de la franquicia con ficha',
              wrap=True)
    motor.f(ws, 'D%d' % fila,
            motor.iferror('D%d-D%d' % (f_fq_mia, FQ_INI)), fmt=C.FMT_EUR)
    motor.val(ws, 'H%d' % fila,
              'La diferencia se lee CON LA ETIQUETA DELANTE: los 100.000 € de '
              'la franquicia son lo que publica un portal de franquicias, no '
              'una cuenta auditada, y encima no incluyen el royalty mensual ni '
              'la compra obligada a central, que son gasto recurrente y no '
              'inversión. La columna existe para que compares, no para '
              'recomendar.', wrap=True)
    ws.row_dimensions[fila].height = 68
    fila += 2
    ws.merge_cells('B%d:H%d' % (fila, fila))
    motor.val(ws, 'B%d' % fila, D.NOTA_FRANQUICIAS, wrap=True)
    ws['B%d' % fila].font = Font(italic=True, size=9)
    ws.row_dimensions[fila].height = 56
    fila += 2

    refs, fila = C.bloque_listas(
        ws, fila, [('¿Lo necesitas?', NECESIDAD),
                   ('¿Por escrito?', POR_ESCRITO),
                   ('¿Es la tuya?', SI_NO)], col='B')
    C.dv_rango(ws, coords_nec, refs['¿Lo necesitas?'], '¿Lo necesitas?',
               'Elige «Sí», «No» o «Por decidir» de la lista.')
    C.dv_rango(ws, coords_esc, refs['¿Por escrito?'], '¿Por escrito?',
               'Elige «Sí», «No» o «Por pedir» de la lista.')
    C.dv_rango(ws, ['D%d' % V_FILA[k] for k in ('bombonería', 'bean', 'taza')],
               refs['¿Es la tuya?'], '¿Es la tuya?',
               'Elige «Sí» o «No» de la lista.')
    C.parrafo(ws, fila,
              'LA VARIANTE DE TAZA Y CHURROS ES OTRO NEGOCIO, Y LA NORMA LO '
              'SEPARA SOLA. El Anexo de la Ley 12/2012 incluye el epígrafe '
              '644.5 «Comercio al por menor de bombones y caramelos» y NO '
              'contiene ningún grupo de la agrupación 67, donde está la '
              'chocolatería de taza: la bombonería se libra de la licencia '
              'previa hasta 750 m2 y la de taza no. Lo que sí aporta la taza es '
              'ticket: el chocolate convierte una ración de churros de 2,50 € '
              'en 3,50-4 €. Lo que cuesta es freidora, extracción de humos y la '
              'licencia que la bombonería se ahorra.',
              col_ini='B', col_fin='H', alto=80)
    C.pagina(ws, apaisado=True, titulos='%d:%d' % (V_TAB, V_TAB))
    return ws, {'fq_ini': FQ_INI, 'fq_fin': FQ_FIN, 'fq_mia': f_fq_mia,
                'bean_ini': B_LISTA_INI, 'bean_fin': B_LISTA_FIN,
                'bean_cont': B_CONT, 'taza_ini': T_INI, 'taza_fin': T_FIN,
                'v_fila': V_FILA}


# --------------------------------------------------------------------------
T_PT, T_TAD, T_TREN, T_TPAR = 6, 7, 8, 9
T_ON, T_OREN, T_OPAR, T_HOR = 10, 11, 12, 13
T_CT, T_CO, T_RT, T_RO, T_TOT_T, T_TOT_O, T_DIF, T_VER = (15, 16, 17, 18, 19,
                                                          20, 21, 22)
T_TAB_CAB = 25
T_TAB_INI = 26


def hoja_traspaso(wb):
    ws = wb.create_sheet(H_TRA)
    C.anchos(ws, {'A': 54, 'B': 26, 'C': 18, 'D': 14, 'E': 16, 'F': 15,
                  'G': 16, 'H': 18, 'I': 14, 'J': 82})
    C.encabezar(ws, 'Traspaso contra obra nueva',
                'El precio de un traspaso no es lo que cuesta un traspaso: la '
                'renta de los años del contrato pesa más que el precio.',
                col_fin='J')

    C.seccion(ws, 'A5', 'El local que estás mirando (traspaso)')
    entradas = [
        (T_PT, 'Precio de traspaso que te piden', 26000.0, C.FMT_EUR,
         'CHS-38a',
         'Sembrado con el caso más informativo del censo: 26.000 € por 90 m2 '
         'de pastelería-bombonería CON OBRADOR EQUIPADO y 40 años de clientela, '
         'en El Prat de Llobregat. Es un precio PEDIDO en un anuncio, no un '
         'precio pagado.'),
        (T_TAD, 'Inversión de adecuación que aún tendrías que hacer', 18000.0,
         C.FMT_EUR, 'supuesto',
         'Un traspaso casi nunca se abre tal cual. En chocolate hay una '
         'partida que casi seguro falta: la CLIMATIZACIÓN con '
         'deshumidificación del obrador. Una pastelería traspasada tiene '
         'hornos, no clima de 18-20 grados C. Míralo con la ficha de visita '
         'del libro 1 en la mano.'),
        (T_TREN, 'Renta mensual del local traspasado', 1100.0, C.FMT_EUR,
         'CHS-38a',
         'La renta consta en tres de los ocho traspasos leídos. En los otros '
         'cinco el anuncio no la dice, que ya es un dato.'),
        (T_TPAR, 'Meses parado hasta abrir con el traspaso', 1, C.FMT_ENT,
         'supuesto',
         'Pagas renta desde la firma y no facturas hasta que abres.'),
    ]
    for fila, etq, valor, fmt, fuente, notatxt in entradas:
        motor.val(ws, 'A%d' % fila, etq, wrap=True)
        motor.val(ws, 'C%d' % fila, valor, fmt=fmt, verde_=True)
        motor.val(ws, 'B%d' % fila, fuente)
        motor.val(ws, 'J%d' % fila, notatxt, wrap=True)
        ws.row_dimensions[fila].height = 56

    motor.val(ws, 'A%d' % T_ON,
              'CAPEX comparable de la obra nueva (de «CAPEX por Bloque»)',
              wrap=True)
    motor.f(ws, 'C%d' % T_ON, "='%s'!L%d" % (H_CAP, R_COMP), fmt=C.FMT_EUR)
    motor.val(ws, 'J%d' % T_ON,
              'Los seis bloques comparables: sin fianza, sin packaging y sin '
              'fondo de maniobra. Los dos lados de la comparación los '
              'necesitan igual, así que sumarlos a uno solo falsearía el '
              'resultado.', wrap=True)
    ws.row_dimensions[T_ON].height = 48
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
    ws.row_dimensions[T_OPAR].height = 44
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
              'adelante ni permite climatizar el obrador. Pasa el local '
              'traspasado por la ficha de visita del libro 1 antes de hacerle '
              'caso a esta celda.', wrap=True)
    ws.row_dimensions[T_VER].height = 62

    C.seccion(ws, 'A24',
              'Ocho traspasos reales, para ver la horquilla. Son precios '
              'PEDIDOS, no pagados')
    C.cabecera(ws, T_TAB_CAB, [
        ('A', 'Ciudad o zona'), ('B', 'Tipo de negocio'), ('C', 'm2'),
        ('D', 'Precio pedido'), ('E', 'Renta mensual'), ('F', '€ por m2'),
        ('G', 'Coste en el horizonte'), ('H', 'Fuente'),
        ('I', '¿Mismo formato?')], altura=30)
    fila = T_TAB_INI
    todos = ([(c, t, m2, p, r, f, 'Sí') for c, t, m2, p, r, f in D.TRASPASOS]
             + [(c, 'Churrería-chocolatería', m2, p, r, f, 'No')
                for c, m2, p, r, f in D.TRASPASOS_VARIANTE_TAZA])
    for ciudad, tipo, m2, precio, renta, fuente, mismo in todos:
        motor.val(ws, 'A%d' % fila, ciudad)
        motor.val(ws, 'B%d' % fila, tipo, wrap=True)
        if m2 is not None:
            motor.val(ws, 'C%d' % fila, m2, fmt=C.FMT_ENT)
        if precio is not None:
            motor.val(ws, 'D%d' % fila, precio, fmt=C.FMT_EUR)
        else:
            motor.val(ws, 'D%d' % fila, '')
        if renta is not None:
            motor.val(ws, 'E%d' % fila, renta, fmt=C.FMT_EUR)
        motor.f(ws, 'F%d' % fila,
                '=IF(AND(ISNUMBER(C%d),ISNUMBER(D%d)),IFERROR(D%d/C%d,""),"")'
                % (fila, fila, fila, fila), fmt=C.FMT_EUR)
        motor.f(ws, 'G%d' % fila,
                '=IF(AND(ISNUMBER(D%d),ISNUMBER(E%d)),'
                'IFERROR(D%d+E%d*12*$C$%d,""),"")'
                % (fila, fila, fila, fila, T_HOR), fmt=C.FMT_EUR)
        motor.val(ws, 'H%d' % fila, fuente)
        motor.val(ws, 'I%d' % fila, mismo)
        ws.row_dimensions[fila].height = 32
        fila += 1
    t_fin = fila - 1
    motor.semaforo_texto(ws, 'I%d:I%d' % (T_TAB_INI, t_fin),
                         (('No', motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          ('Sí', motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
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

    C.parrafo(ws, f + 6, D.NOTA_TRASPASOS, col_ini='A', col_fin='J', alto=62)
    C.parrafo(ws, f + 8,
              'Y lo que ninguno de los ocho trae: la cuenta de resultados. Un '
              'traspaso se valora por lo que gana el negocio, no por lo que '
              'pide el anuncio. Pide los modelos 303 y 390 de los tres últimos '
              'años y el resumen de la Seguridad Social de la plantilla; si no '
              'te los enseñan, ya sabes lo que estás comprando. Y en chocolate, '
              'una pregunta más: qué clima tiene el obrador hoy. Un obrador de '
              'pastelería traspasado no viene climatizado a 18-20 grados C, y '
              'esa partida no está en el precio del anuncio.',
              col_ini='A', col_fin='J', alto=68)
    C.pagina(ws, apaisado=True, titulos='%d:%d' % (T_TAB_CAB, T_TAB_CAB))
    return ws, {'tab_ini': T_TAB_INI, 'tab_fin': t_fin, 'resumen': f}


# --------------------------------------------------------------------------
I_INI = 6
I_TOT = I_INI + len(D.BLOQUES_CAPEX)
I_PER, I_MES, I_ADEL = I_TOT + 2, I_TOT + 3, I_TOT + 4
I_BASE, I_IVA, I_DES, I_FON, I_FIN, I_APO, I_VER = (
    I_TOT + 7, I_TOT + 8, I_TOT + 9, I_TOT + 10, I_TOT + 11, I_TOT + 12,
    I_TOT + 13)
I_PL_CAB = I_VER + 3
I_PL_KG, I_PL_UMB, I_PL_SUP, I_PL_TIPO, I_PL_COSTE, I_PL_VER = (
    I_PL_CAB + 1, I_PL_CAB + 2, I_PL_CAB + 3, I_PL_CAB + 4, I_PL_CAB + 5,
    I_PL_CAB + 6)
I_PL_MOLDES = I_PL_VER + 1


def hoja_iva(wb):
    ws = wb.create_sheet(H_IVA)
    C.anchos(ws, {'A': 58, 'B': 18, 'C': 18, 'D': 16, 'E': 90})
    C.encabezar(ws, 'IVA y tesorería del arranque',
                'El IVA de la inversión sale de tu bolsillo meses antes de '
                'volver. Y abajo, el contador que dice si el impuesto al '
                'plástico te afecta o no: lo que decide es DÓNDE compras, no '
                'cuánto.', col_fin='E')
    C.seccion(ws, 'A5', 'IVA soportado por bloque')
    C.cabecera(ws, I_INI - 1, [('A', 'Bloque'), ('B', 'Base sin IVA'),
                               ('C', 'IVA soportado'), ('D', 'Total con IVA')])
    for k, bloque in enumerate(D.BLOQUES_CAPEX):
        f = I_INI + k
        motor.val(ws, 'A%d' % f, ROTULO_BLOQUE[bloque])
        for col_dst, col_src in (('B', 'L'), ('C', 'M'), ('D', 'N')):
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
              'vuelve al ritmo al que factures, no en una fecha. Y el chocolate '
              'que vendes va al 10 %, mientras que el IVA que adelantas es del '
              '21 %: la compensación tarda más de lo que parece. Si te '
              'inscribes en el registro de devolución mensual, la periodicidad '
              'pasa a 1 y la espera se acorta mucho.', wrap=True)
    ws.row_dimensions[I_ADEL].height = 74

    C.seccion(ws, 'A%d' % (I_BASE - 1), 'La caja del día que abres')
    motor.val(ws, 'A%d' % I_BASE, 'CAPEX sin IVA (los nueve bloques)')
    motor.f(ws, 'B%d' % I_BASE, '=B%d' % I_TOT, fmt=C.FMT_EUR)
    motor.val(ws, 'A%d' % I_IVA, 'IVA soportado')
    motor.f(ws, 'B%d' % I_IVA, '=C%d' % I_TOT, fmt=C.FMT_EUR)
    motor.val(ws, 'A%d' % I_DES, 'Desembolso total con IVA', bold=True)
    motor.f(ws, 'B%d' % I_DES, '=D%d' % I_TOT, fmt=C.FMT_EUR, bold=True)
    C.destacado(ws, 'B%d' % I_DES)
    motor.val(ws, 'A%d' % I_FON,
              'Del cual, fondo de maniobra (es caja, no inversión)', wrap=True)
    motor.f(ws, 'B%d' % I_FON, "='%s'!L%d" % (H_CAP, R_FONDO), fmt=C.FMT_EUR)
    motor.val(ws, 'E%d' % I_FON,
              'Llega del libro 7 ya calculado, con su fila de cuadre. Este '
              'libro NO lo recalcula: si lo hiciera, los dos publicarían dos '
              'inversiones totales distintas con el mismo nombre.', wrap=True)
    ws.row_dimensions[I_FON].height = 48
    motor.val(ws, 'A%d' % I_FIN, 'Financiación bancaria disponible')
    motor.f(ws, 'B%d' % I_FIN, "='%s'!B%d" % (H_PAR, fp(P_FINAN)),
            fmt=C.FMT_EUR)
    motor.val(ws, 'A%d' % I_APO, 'Aportación propia necesaria', bold=True)
    motor.f(ws, 'B%d' % I_APO, motor.iferror('B%d-B%d' % (I_DES, I_FIN)),
            fmt=C.FMT_EUR, bold=True)
    C.destacado(ws, 'B%d' % I_APO)
    motor.val(ws, 'A%d' % I_VER, 'VEREDICTO DE LA CAJA', bold=True)
    motor.f(ws, 'B%d' % I_VER,
            '=IF(B%d="","",IF(B%d<=0,"La financiación cubre el desembolso",'
            '"Necesitas aportación propia"))' % (I_APO, I_APO), bold=True)
    C.destacado(ws, 'B%d' % I_VER)
    motor.semaforo_texto(ws, 'B%d' % I_VER,
                         (('Necesitas aportación propia', motor.CF_AMBAR_BG,
                           motor.CF_AMBAR_FG),
                          ('La financiación cubre el desembolso',
                           motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    motor.val(ws, 'E%d' % I_VER,
              'Que necesites aportación propia no es una mala noticia: ningún '
              'banco financia el 100 % de una apertura, y el que lo hiciera te '
              'estaría dejando sin margen de maniobra. Lo que sí es mala '
              'noticia es descubrirlo el mes de la firma. Cuántos meses de '
              'gastos fijos cubre ese fondo te lo dice el libro 7, que es donde '
              'viven los gastos fijos: aquí no se recalcula.', wrap=True)
    ws.row_dimensions[I_VER].height = 74

    # --- contador de plástico --------------------------------------------
    C.seccion(ws, 'A%d' % I_PL_CAB,
              'Contador del impuesto al plástico: ¿te afecta o no?')
    motor.val(ws, 'A%d' % I_PL_KG,
              'Kg al mes de plástico no reciclado IMPORTADO o adquirido en '
              'otro país de la UE', wrap=True)
    motor.f(ws, 'B%d' % I_PL_KG, "='%s'!B%d" % (H_PAR, fp(P_KG_PLAST)),
            fmt=C.FMT_DEC1)
    motor.val(ws, 'E%d' % I_PL_KG,
              'LO QUE DECIDE ES DÓNDE COMPRAS Y QUÉ COMPRAS, NO CUÁNTO. El '
              'impuesto grava la fabricación, la importación y la adquisición '
              'intracomunitaria de envases no reutilizables que contengan '
              'plástico. Lo que compras en España a un proveedor español ya lo '
              'lleva repercutido en la factura: no cuenta aquí.', wrap=True)
    ws.row_dimensions[I_PL_KG].height = 62
    motor.val(ws, 'A%d' % I_PL_UMB, 'Umbral de la exención del art. 75.f)')
    motor.f(ws, 'B%d' % I_PL_UMB, "='%s'!B%d" % (H_PAR, fp(P_UMBRAL_PLAST)),
            fmt=C.FMT_DEC1)
    motor.val(ws, 'E%d' % I_PL_UMB,
              'La exención tiene DOS límites, no uno: sólo cubre la importación '
              'o adquisición intracomunitaria que no exceda de 5 kg en un mes, '
              'y sólo los envases del art. 68.1.a). NO exime la fabricación, ni '
              'los semielaborados, ni los cierres.', wrap=True)
    ws.row_dimensions[I_PL_UMB].height = 56
    nota_legal_celda(ws, 'A%d' % I_PL_UMB, 'CHN-62b')
    motor.val(ws, 'A%d' % I_PL_SUP, '¿Superas el umbral?', bold=True)
    motor.f(ws, 'B%d' % I_PL_SUP,
            '=IF(OR(B%d="",B%d=""),"",IF(B%d>B%d,'
            '"SÍ: mira el registro territorial y la liquidación",'
            '"No: por debajo de la exención del art. 75.f)"))'
            % (I_PL_KG, I_PL_UMB, I_PL_KG, I_PL_UMB), bold=True)
    C.destacado(ws, 'B%d' % I_PL_SUP)
    motor.semaforo_texto(ws, 'B%d' % I_PL_SUP,
                         (('SÍ: mira el registro territorial y la liquidación',
                           motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          ('No: por debajo de la exención del art. 75.f)',
                           motor.CF_VERDE_BG, motor.CF_VERDE_FG)))
    motor.val(ws, 'A%d' % I_PL_TIPO, 'Tipo del impuesto')
    motor.f(ws, 'B%d' % I_PL_TIPO, "='%s'!B%d" % (H_PAR, fp(P_TIPO_PLAST)),
            fmt=C.FMT_EUR)
    motor.val(ws, 'A%d' % I_PL_COSTE,
              'Coste anual estimado si estás por encima del umbral')
    motor.f(ws, 'B%d' % I_PL_COSTE,
            '=IF(OR(B%d="",B%d=""),"",IF(B%d<=B%d,"",'
            'IFERROR(B%d*12*B%d,"")))'
            % (I_PL_KG, I_PL_UMB, I_PL_KG, I_PL_UMB, I_PL_KG, I_PL_TIPO),
            fmt=C.FMT_EUR)
    motor.val(ws, 'E%d' % I_PL_COSTE,
              'Se queda en blanco mientras estés por debajo del umbral: un cero '
              'ahí se leería como «ya lo he calculado y sale cero», y lo que '
              'pasa es que no aplica. Cuando aplique, recuerda que el art. 82.3 '
              'obliga además a inscribirse en el Registro territorial, «salvo '
              'aquellos que se determine mediante Orden».', wrap=True)
    ws.row_dimensions[I_PL_COSTE].height = 62
    motor.val(ws, 'A%d' % I_PL_VER, 'ALERTA DEL PLÁSTICO', bold=True)
    motor.f(ws, 'B%d' % I_PL_VER,
            '=IF(B%d="","",IF(B%d>B%d,"Revisa el impuesto al plástico con tu '
            'asesor","Sin alerta"))' % (I_PL_KG, I_PL_KG, I_PL_UMB), bold=True)
    C.destacado(ws, 'B%d' % I_PL_VER)
    motor.semaforo_texto(ws, 'B%d' % I_PL_VER,
                         (('Revisa el impuesto al plástico con tu asesor',
                           motor.CF_AMBAR_BG, motor.CF_AMBAR_FG),
                          ('Sin alerta', motor.CF_VERDE_BG,
                           motor.CF_VERDE_FG)))
    motor.val(ws, 'A%d' % I_PL_MOLDES,
              'Y los moldes de policarbonato NO pagan', bold=True)
    motor.val(ws, 'B%d' % I_PL_MOLDES, 'No sujetos')
    motor.val(ws, 'E%d' % I_PL_MOLDES,
              'No están sujetos por el art. 73.d): pudiendo contener, no están '
              'diseñados para entregarse junto con la mercancía, y además el '
              'impuesto sólo grava envases NO reutilizables. Están prohibidas '
              'las dos frases fáciles, «el impuesto no te afecta si compras los '
              'envases» y su contraria «te afecta siempre»: lo que decide es '
              'dónde compras y qué compras.', wrap=True)
    ws.row_dimensions[I_PL_MOLDES].height = 68
    nota_legal_celda(ws, 'A%d' % I_PL_MOLDES, 'CHN-62c')

    C.parrafo(ws, I_PL_MOLDES + 2,
              'Esta hoja NO explica el impuesto al plástico: emite la alerta '
              'cuando pasas el umbral. La explicación entera -qué es un envase '
              'a estos efectos, qué papel tiene tu proveedor y qué hay que '
              'registrar- está en el capítulo 13 de la guía, que es donde se '
              'lee.',
              col_ini='A', col_fin='E', alto=48)
    C.pagina(ws, apaisado=False, titulos='%d:%d' % (I_INI - 1, I_INI - 1))
    return ws


# --------------------------------------------------------------------------
S_INI = 6


def hoja_resumen(wb):
    ws = wb.create_sheet(H_RES)
    C.anchos(ws, {'A': 60, 'B': 20, 'C': 24, 'D': 88})
    C.encabezar(ws, 'Resumen',
                'Las cifras que hay que llevar al banco. Todas calculadas '
                'desde las hojas anteriores; aquí no se teclea nada.',
                col_fin='D')
    C.cabecera(ws, S_INI - 1, [('A', 'Cifra'), ('B', 'Valor'),
                               ('C', 'De dónde sale'), ('D', 'Qué dice')])
    i_fondo = D.BLOQUES_CAPEX.index('Fondo de maniobra')
    i_tm = D.BLOQUES_CAPEX.index('Equipo de templado y moldeado')
    i_frio = D.BLOQUES_CAPEX.index('Frio')
    i_clima = D.BLOQUES_CAPEX.index('Climatizacion y deshumidificacion')
    filas = [
        ('Obra y adecuación', "='%s'!B%d" % (H_PAR, fp(P_OBRA)), C.FMT_EUR,
         H_PAR, 'Metros por el precio por m2. Es la única partida del CAPEX '
         'que no se teclea, y la que más se desvía en la ejecución: lo que no '
         'está en el proyecto se paga aparte.'),
        ('CAPEX SIN el fondo de maniobra',
         "='%s'!L%d" % (H_CAP, R_SINFONDO), C.FMT_EUR, H_CAP,
         'LA CIFRA QUE VIAJA AL LIBRO 7. No es «el CAPEX total»: el total '
         'incluye el bloque «fondo de maniobra», y el libro 7 vuelve a dotar '
         'el fondo con sus propios meses de colchón.'),
        ('Del cual, fondo de maniobra (es caja, no inversión)',
         "='%s'!L%d" % (H_CAP, R_FONDO), C.FMT_EUR, H_CAP,
         'Llega del libro 7 ya calculado, en celda verde y con fila de cuadre. '
         'Es caja, no una compra: no se consume como el resto de partidas. '
         'Pero hay que APORTARLA o FINANCIARLA igual que a ellas, y por eso '
         'está dentro del total que se lleva al banco.'),
        ('INVERSIÓN TOTAL (las dos líneas de arriba)',
         "='%s'!L%d" % (H_CAP, R_INV), C.FMT_EUR, H_CAP,
         'La suma de las dos. Sale IDÉNTICA a la del libro 7 por construcción, '
         'porque el fondo se calcula UNA sola vez y en un solo sitio.'),
        ('IVA soportado', "='%s'!M%d" % (H_CAP, R_TOT), C.FMT_EUR, H_CAP,
         'Dinero tuyo que adelantas y que vuelve al ritmo al que factures. '
         'Adelantas al 21 % y repercutes al 10 %.'),
        ('Desembolso total con IVA', "='%s'!N%d" % (H_CAP, R_TOT), C.FMT_EUR,
         H_CAP, 'Lo que sale de la cuenta. Es el número de la conversación con '
         'el banco.'),
        ('Subtotal comparable con un presupuesto de obra y equipamiento',
         "='%s'!L%d" % (H_CAP, R_COMP), C.FMT_EUR, H_CAP,
         'Seis bloques. Sin fianza, sin packaging y sin fondo de maniobra: un '
         'depósito, unas existencias y una caja no se comparan contra un '
         'presupuesto de obra.'),
        ('Climatización y deshumidificación',
         "='%s'!L%d" % (H_CAP, B_INI + i_clima), C.FMT_EUR, H_CAP,
         'LA PARTIDA QUE NADIE PRESUPUESTA, y en chocolate no es confort: es '
         'la que decide si la cobertura cristaliza. Su dimensionado se '
         'contrasta en el libro 1.'),
        ('Equipo de templado y moldeado',
         "='%s'!L%d" % (H_CAP, B_INI + i_tm), C.FMT_EUR, H_CAP,
         'Sin los opcionales, que vienen marcados «No». Es el bloque que se '
         'compara con el escenario profesional de entrada.'),
        ('Frío (cámara, nevera de rellenos y vitrina)',
         "='%s'!L%d" % (H_CAP, B_INI + i_frio), C.FMT_EUR, H_CAP,
         'Tres equipos con tres temperaturas distintas. Sólo la vitrina tiene '
         'precio verificado; los otros dos son supuestos declarados.'),
        ('Cuadre del fondo de maniobra con el libro 7',
         "='%s'!L%d" % (H_CAP, R_CRUCE_VER), None, H_CAP,
         'Si dice que no cuadra, alguien ha pisado la fila del bloque: '
         'arréglalo antes de enseñarle el plan a nadie.'),
        ('Aportación propia necesaria', "='%s'!B%d" % (H_IVA, I_APO),
         C.FMT_EUR, H_IVA, 'Desembolso menos financiación bancaria.'),
        ('Veredicto de la caja', "='%s'!B%d" % (H_IVA, I_VER), None, H_IVA,
         'Si la financiación cubre el desembolso o hace falta poner dinero.'),
        ('Alerta del impuesto al plástico',
         "='%s'!B%d" % (H_IVA, I_PL_VER), None, H_IVA,
         'Salta sólo si importas o compras en otro país de la UE más de 5 kg '
         'al mes de plástico no reciclado en envases.'),
        ('Coste del traspaso en el horizonte',
         "='%s'!C%d" % (H_TRA, T_TOT_T), C.FMT_EUR, H_TRA,
         'Precio pedido, adecuación y renta de todos los años, más los meses '
         'parado.'),
        ('Coste de la obra nueva en el horizonte',
         "='%s'!C%d" % (H_TRA, T_TOT_O), C.FMT_EUR, H_TRA,
         'CAPEX comparable y renta de todos los años, más los meses de obra.'),
        ('Traspaso o obra nueva', "='%s'!C%d" % (H_TRA, T_VER), None, H_TRA,
         'Compara dinero. La distribución del local, la clientela y si el '
         'obrador se puede climatizar no salen en esta celda.'),
    ]
    fila = S_INI
    S_FILA = {}
    for etq, formula, fmt, hoja, notatxt in filas:
        S_FILA[etq] = fila
        motor.val(ws, 'A%d' % fila, etq, wrap=True)
        motor.f(ws, 'B%d' % fila, formula, fmt=fmt)
        motor.val(ws, 'C%d' % fila, hoja)
        motor.val(ws, 'D%d' % fila, notatxt, wrap=True)
        ws.row_dimensions[fila].height = 52
        fila += 1
    C.destacado(ws, 'B%d' % S_FILA['INVERSIÓN TOTAL (las dos líneas de arriba)'])
    C.destacado(ws, 'B%d' % S_FILA['CAPEX SIN el fondo de maniobra'])
    C.parrafo(ws, fila + 1,
              'Si alguna de estas cifras no te cuadra, no la cambies aquí: '
              'esta hoja no tiene ni una celda editable. Vuelve a la hoja donde '
              'nace y cambia el parámetro o el importe. Es lo que evita que un '
              'resumen y su origen digan cosas distintas.',
              col_ini='A', col_fin='D', alto=44)
    C.parrafo(ws, fila + 3,
              'LAS DOS PRIMERAS LÍNEAS DE DINERO SON DOS Y NO UNA A PROPÓSITO. '
              '«CAPEX sin el fondo de maniobra» es lo que le llevas al libro 7 '
              'y lo que se parece a lo que el sector llama «inversión de '
              'apertura»; el fondo de maniobra es caja, no inversión, y lo dota '
              'el libro 7 con sus meses de colchón y sus gastos fijos. La suma '
              'de las dos es la inversión total, y sale idéntica en los dos '
              'libros porque el fondo se calcula UNA vez. Publicar un único '
              '«CAPEX total» y pedir además el fondo en el otro libro es el '
              'error que hace que un mismo negocio aparezca con dos '
              'inversiones distintas en el mismo pack.',
              col_ini='A', col_fin='D', alto=80)
    C.pagina(ws, apaisado=False, titulos='%d:%d' % (S_INI - 1, S_INI - 1))
    return ws


# --------------------------------------------------------------------------
def mapa_celdas(var, tra):
    m = {}

    def add(etq, hoja, celda, tipo):
        m[etq] = {'ref': '%s.xlsx!%s!%s' % (NOMBRE, hoja, celda),
                  'tipo': tipo}

    add('Superficie del local', H_PAR, 'B%d' % fp(P_M2), 'entrada')
    add('Coste de obra y adecuación por m2', H_PAR, 'B%d' % fp(P_EURM2),
        'entrada')
    add('Obra y adecuación calculada', H_PAR, 'B%d' % fp(P_OBRA), 'salida')
    add('IVA general', H_PAR, 'B%d' % fp(P_IVA_GEN), 'parametro')
    add('IVA del chocolate', H_PAR, 'B%d' % fp(P_IVA_PROD), 'parametro')
    add('Renta mensual del local', H_PAR, 'B%d' % fp(P_RENTA), 'entrada')
    add('Horizonte de comparación (años)', H_PAR, 'B%d' % fp(P_HORIZ),
        'entrada')
    add('Financiación bancaria disponible', H_PAR, 'B%d' % fp(P_FINAN),
        'entrada')
    add('Kg de plástico importado al mes', H_PAR, 'B%d' % fp(P_KG_PLAST),
        'entrada')
    add('Umbral de la exención del plástico', H_PAR,
        'B%d' % fp(P_UMBRAL_PLAST), 'parametro')
    add('Tipo del impuesto al plástico', H_PAR, 'B%d' % fp(P_TIPO_PLAST),
        'parametro')

    for k, bloque in enumerate(D.BLOQUES_CAPEX):
        add('Base sin IVA del bloque: ' + ROTULO_BLOQUE[bloque], H_CAP,
            'L%d' % (B_INI + k), 'salida')
        add('IVA soportado del bloque: ' + ROTULO_BLOQUE[bloque], H_CAP,
            'M%d' % (B_INI + k), 'salida')
    add('CAPEX total sin IVA (los nueve bloques)', H_CAP, 'L%d' % R_TOT,
        'salida')
    add('IVA soportado total', H_CAP, 'M%d' % R_TOT, 'salida')
    add('Desembolso total con IVA', H_CAP, 'N%d' % R_TOT, 'salida')
    add('CAPEX SIN el fondo de maniobra (viaja al libro 7)', H_CAP,
        'L%d' % R_SINFONDO, 'salida')
    add('Del cual, fondo de maniobra (es caja, no inversión)', H_CAP,
        'L%d' % R_FONDO, 'salida')
    add('INVERSIÓN TOTAL', H_CAP, 'L%d' % R_INV, 'salida')
    add('Subtotal comparable (seis bloques)', H_CAP, 'L%d' % R_COMP, 'salida')
    add('Fondo de maniobra traído del libro 7 (celda verde del cruce)', H_CAP,
        'L%d' % R_CRUCE, 'entrada')
    add('Fondo de maniobra que usa la fila del bloque', H_CAP,
        'L%d' % R_CRUCE_USO, 'salida')
    add('CUADRE del fondo de maniobra', H_CAP, 'L%d' % R_CRUCE_VER, 'salida')
    add('Escenario de dotación A, mínimo publicado', H_CAP,
        'I%d' % (R_ESC + 1), 'parametro')
    add('Escenario de dotación A, máximo publicado', H_CAP,
        'J%d' % (R_ESC + 1), 'parametro')
    add('Escenario de dotación B, mínimo publicado', H_CAP,
        'I%d' % (R_ESC + 2), 'parametro')
    add('Escenario de dotación B, máximo publicado', H_CAP,
        'J%d' % (R_ESC + 2), 'parametro')
    add('Tu equipo de templado y moldeado en base imponible', H_CAP,
        'I%d' % (R_ESC + 3), 'salida')
    add('Dónde cae tu dotación respecto al escenario profesional', H_CAP,
        'I%d' % (R_ESC + 4), 'salida')
    add('Importe de la línea de obra y adecuación', H_CAP, 'K%d' % X_INI,
        'salida')
    add('Importe de la atemperadora continua', H_CAP, 'K%d' % (X_INI + 1),
        'entrada')
    add('Mínimo del rango de moldes de policarbonato', H_CAP,
        'I%d' % (X_INI + 12), 'entrada')
    add('Máximo del rango de moldes de policarbonato', H_CAP,
        'J%d' % (X_INI + 12), 'entrada')

    add('Inversión total de la variante bombonería', H_VAR,
        'E%d' % var['v_fila']['bombonería'], 'salida')
    add('Equipos del tren bean-to-bar que dices necesitar', H_VAR,
        'E%d' % var['bean_cont'], 'salida')
    add('Respuestas del bean-to-bar que tienes por escrito', H_VAR,
        'E%d' % (var['bean_cont'] + 1), 'salida')
    add('VEREDICTO DEL BEAN-TO-BAR', H_VAR, 'E%d' % (var['bean_cont'] + 2),
        'salida')
    add('Precio de la chocolatera de la variante de taza', H_VAR,
        'E%d' % var['taza_ini'], 'entrada')
    add('Inversión desde de la franquicia con ficha', H_VAR,
        'D%d' % var['fq_ini'], 'parametro')
    add('Tu inversión total como independiente', H_VAR,
        'D%d' % var['fq_mia'], 'salida')
    add('Diferencia con la franquicia', H_VAR, 'D%d' % (var['fq_mia'] + 1),
        'salida')

    add('Precio de traspaso que te piden', H_TRA, 'C%d' % T_PT, 'entrada')
    add('Renta mensual del local traspasado', H_TRA, 'C%d' % T_TREN,
        'entrada')
    add('CAPEX comparable de la obra nueva', H_TRA, 'C%d' % T_ON, 'salida')
    add('Coste total del traspaso en el horizonte', H_TRA, 'C%d' % T_TOT_T,
        'salida')
    add('Coste total de la obra nueva en el horizonte', H_TRA,
        'C%d' % T_TOT_O, 'salida')
    add('Diferencia entre traspaso y obra nueva', H_TRA, 'C%d' % T_DIF,
        'salida')
    add('Veredicto de traspaso contra obra nueva', H_TRA, 'C%d' % T_VER,
        'salida')
    add('Traspasos con renta publicada', H_TRA, 'D%d' % tra['resumen'],
        'salida')
    add('Precio pedido más bajo de los ocho', H_TRA,
        'D%d' % (tra['resumen'] + 1), 'salida')
    add('Precio pedido más alto de los ocho', H_TRA,
        'D%d' % (tra['resumen'] + 2), 'salida')
    add('Precio pedido medio de los ocho', H_TRA,
        'D%d' % (tra['resumen'] + 3), 'salida')

    add('IVA que tienes que adelantar', H_IVA, 'B%d' % I_ADEL, 'salida')
    add('Desembolso total con IVA (tesorería)', H_IVA, 'B%d' % I_DES,
        'salida')
    add('Fondo de maniobra dentro del desembolso', H_IVA, 'B%d' % I_FON,
        'salida')
    add('Aportación propia necesaria', H_IVA, 'B%d' % I_APO, 'salida')
    add('VEREDICTO DE LA CAJA', H_IVA, 'B%d' % I_VER, 'salida')
    add('¿Superas el umbral del plástico?', H_IVA, 'B%d' % I_PL_SUP, 'salida')
    # A7 (refutación 2026-09-12): «Coste anual del impuesto al plástico» sale
    # de fábrica en "" (no hay plástico importado en «La Almendra») y un
    # capítulo que citara esa etiqueta imprimiría nada sin avisar. Se saca del
    # mapa; el veredicto de abajo sí es citable en los dos estados.
    add('ALERTA DEL PLÁSTICO', H_IVA, 'B%d' % I_PL_VER, 'salida')
    return m


# --------------------------------------------------------------------------
def construir():
    D.gate_legal(IDS_LEGALES)
    wb = Workbook()
    wb.remove(wb.active)
    hoja_instrucciones(wb)
    hoja_parametros(wb)
    hoja_capex(wb)
    _wsv, var = hoja_variante(wb)
    _wst, tra = hoja_traspaso(wb)
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
    return ruta, verdes, var, tra


def gate_totales(ruta):
    wbv = openpyxl.load_workbook(ruta, data_only=True)
    incoherentes = C.gate_sum_rango(wbv)
    wbv.close()
    if incoherentes:
        raise SystemExit('TOTALES con caché incoherente:\n  '
                         + '\n  '.join(incoherentes))


def gate_sin_referencias_externas():
    """Ninguna fórmula puede nombrar otro fichero (SPEC §2.3, cuarta regla
    dura), y ninguna puede usar las funciones prohibidas."""
    malas = [(h, c, f) for h, c, f in motor.REGISTRO
             if '.xlsx' in f or '[' in f]
    if malas:
        raise SystemExit('Fórmulas que cruzan ficheros:\n  '
                         + '\n  '.join('%s!%s  %s' % m for m in malas))
    prohibidas = ('INDIRECT', 'COUNTA', 'PMT', 'OFFSET', 'XLOOKUP', 'LET(',
                  'LAMBDA', 'RANK', 'NETWORKDAYS', 'IRR')
    usos = [(h, c, f) for h, c, f in motor.REGISTRO
            for p in prohibidas if p in f.upper()]
    if usos:
        raise SystemExit('Funciones prohibidas:\n  '
                         + '\n  '.join('%s!%s  %s' % u for u in usos))


def verificar_y_mapear(ruta, var, tra):
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
    m = mapa_celdas(var, tra)
    for etq, d in m.items():
        _f, hoja, celda = d['ref'].split('!')
        v = wb[hoja][celda].value
        if v is None:
            # Una fórmula que devuelve "" se cachea como None: se le pregunta a
            # pycel para que el mapa publique la cadena vacía y no un `null`,
            # que un capítulo leería como «no se pudo calcular».
            v = calc.evaluate("'%s'!%s" % (hoja, celda))
        d['valor'] = v
    with open(os.path.join(os.path.dirname(ruta), 'mapa-' + NOMBRE + '.json'),
              'w', encoding='utf-8') as fh:
        json.dump(m, fh, ensure_ascii=False, indent=1)
    return fallos, m, vacias


# --------------------------------------------------------------------------
def demo(ruta, var):
    """Comportamientos del libro, probados con pycel.

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

    A_TOT = "'%s'!L%d" % (H_CAP, R_TOT)
    A_SINF = "'%s'!L%d" % (H_CAP, R_SINFONDO)
    A_FON = "'%s'!L%d" % (H_CAP, R_FONDO)
    A_INV = "'%s'!L%d" % (H_CAP, R_INV)
    A_CUADRE = "'%s'!L%d" % (H_CAP, R_CRUCE_VER)
    A_OBRA = "'%s'!B%d" % (H_PAR, fp(P_OBRA))
    A_VERT = "'%s'!C%d" % (H_TRA, T_VER)
    A_DIF = "'%s'!C%d" % (H_TRA, T_DIF)
    A_PLA = "'%s'!B%d" % (H_IVA, I_PL_VER)
    A_PLC = "'%s'!B%d" % (H_IVA, I_PL_COSTE)

    # 1. Los nueve bloques suman el total, y las dos líneas suman la inversión.
    c = ExcelCompiler(ruta)
    tot = c.evaluate(A_TOT)
    suma = sum(c.evaluate("'%s'!L%d" % (H_CAP, B_INI + k))
               for k in range(len(D.BLOQUES_CAPEX)))
    sinf, fon, inv = (c.evaluate(A_SINF), c.evaluate(A_FON), c.evaluate(A_INV))
    prueba('Los nueve bloques suman el CAPEX total, y las dos líneas del '
           'resumen suman la inversión total',
           abs(tot - suma) < 0.01 and abs((sinf + fon) - inv) < 0.01
           and abs(inv - tot) < 0.01,
           'total=%.2f · suma=%.2f · sin fondo=%.2f + fondo=%.2f = %.2f'
           % (tot, suma, sinf, fon, inv))

    # 2. El fondo de maniobra cuadra con el libro 7, y se detecta si lo pisan.
    c = compilador([A_CUADRE])
    cuadre0 = c.evaluate(A_CUADRE)
    c.set_value("'%s'!K%d" % (H_CAP, X_FIN), 40000.0)
    cuadre1 = c.evaluate(A_CUADRE)
    prueba('La fila de CUADRE avisa si alguien pisa el fondo de maniobra del '
           'bloque',
           cuadre0 == 'CUADRA'
           and cuadre1 == 'NO CUADRA: alguien ha pisado la fila del bloque',
           'antes=%r · después=%r' % (cuadre0, cuadre1))

    # 3. El precio por m2 de obra mueve el CAPEX.
    c = compilador([A_OBRA, A_TOT])
    obra0, tot0 = c.evaluate(A_OBRA), c.evaluate(A_TOT)
    c.set_value("'%s'!B%d" % (H_PAR, fp(P_EURM2)), OBRA_EUR_M2 * 2)
    obra1, tot1 = c.evaluate(A_OBRA), c.evaluate(A_TOT)
    prueba('Cambiar el precio por m2 recalcula la obra y el CAPEX total',
           abs(obra1 - obra0 * 2) < 0.01 and abs((tot1 - tot0) - obra0) < 0.01,
           'obra %.0f -> %.0f · CAPEX %.0f -> %.0f'
           % (obra0, obra1, tot0, tot1))

    # 4. La columna de IVA hace su trabajo: marcar «Sí» baja la base un 21 %.
    fila_vitrina = None
    for i, ln in enumerate(LINEAS):
        if 'Docriluc' in ln[1]:
            fila_vitrina = X_INI + i
    A_L = "'%s'!L%d" % (H_CAP, fila_vitrina)
    c = compilador([A_L])
    base = c.evaluate(A_L)
    c.set_value("'%s'!G%d" % (H_CAP, fila_vitrina), 'Sí')
    base2 = c.evaluate(A_L)
    prueba('Declarar que el precio lleva IVA baja la base imponible un 21 %',
           abs(base2 - base / (1 + D.P('iva_general'))) < 0.01,
           'base %.2f -> %.2f' % (base, base2))

    # 5. Marcar «No» en «¿la compras?» saca la línea del total por su importe.
    c = compilador([A_TOT])
    t0 = c.evaluate(A_TOT)
    c.set_value("'%s'!D%d" % (H_CAP, fila_vitrina), 'No')
    t1 = c.evaluate(A_TOT)
    esperado = D.precio_equipamiento_sin_iva(
        [e for e in D.EQUIPAMIENTO if 'Docriluc' == (e['marca'] or '')][0])
    prueba('Marcar «No» saca la línea del total por su importe exacto',
           abs((t0 - t1) - esperado) < 0.01,
           'baja %.2f, esperado %.2f' % (t0 - t1, esperado))

    # 6. El veredicto de traspaso cambia al subir el precio pedido.
    c = compilador([A_VERT, A_DIF])
    ver0, dif0 = c.evaluate(A_VERT), c.evaluate(A_DIF)
    c.set_value("'%s'!C%d" % (H_TRA, T_PT), 400000.0)
    ver1 = c.evaluate(A_VERT)
    prueba('Un traspaso desorbitado da la vuelta al veredicto',
           ver0 == 'Sale mejor el TRASPASO'
           and ver1 == 'Sale mejor la OBRA NUEVA',
           'antes=%s (dif %.0f) · después=%s' % (ver0, dif0, ver1))

    # 7. El contador de plástico salta al pasar de 5 kg/mes, y no antes.
    c = compilador([A_PLA, A_PLC])
    pla0, plc0 = c.evaluate(A_PLA), c.evaluate(A_PLC)
    c.set_value("'%s'!B%d" % (H_PAR, fp(P_KG_PLAST)), 8.0)
    pla1, plc1 = c.evaluate(A_PLA), c.evaluate(A_PLC)
    prueba('El contador de plástico salta al pasar los 5 kg/mes, y por debajo '
           'deja el coste en blanco (no en cero)',
           pla0 == 'Sin alerta' and plc0 == ''
           and pla1 == 'Revisa el impuesto al plástico con tu asesor'
           and abs(plc1 - 8.0 * 12 * D.PLASTICO['tipo_euros_kg']) < 0.01,
           'con 3,2 kg: %r / %r · con 8 kg: %r / %.2f'
           % (pla0, plc0, pla1, plc1))

    # 8. Las tasas municipales no generan IVA soportado.
    c = ExcelCompiler(ruta)
    fila_tasas = None
    for i, ln in enumerate(LINEAS):
        if 'Tasas municipales' in ln[1]:
            fila_tasas = X_INI + i
    iva_tasas = c.evaluate("'%s'!M%d" % (H_CAP, fila_tasas))
    iva_total = c.evaluate("'%s'!B%d" % (H_IVA, I_ADEL))
    prueba('Las tasas municipales van a tipo 0 y no generan IVA soportado',
           iva_tasas == 0 and iva_total > 0,
           'IVA de las tasas=%s · IVA total a adelantar=%.2f'
           % (iva_tasas, iva_total))
    return resultados


# --------------------------------------------------------------------------
def main():
    ruta, verdes, var, tra = construir()
    print('escrito:', ruta)
    gate_sin_referencias_externas()
    fallos, m, vacias = verificar_y_mapear(ruta, var, tra)
    gate_totales(ruta)
    res = demo(ruta, var)
    print('-' * 70)
    print('líneas de CAPEX      : %d en %d bloques'
          % (len(LINEAS), len(D.BLOQUES_CAPEX)))
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
    print('-' * 70)
    print('RESULTADO:', 'VERDE' if todo_ok else 'ROJO')
    return 0 if todo_ok else 1


if __name__ == '__main__':
    sys.exit(main())
