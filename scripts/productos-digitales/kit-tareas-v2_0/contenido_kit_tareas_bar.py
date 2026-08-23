#!/usr/bin/env python3
"""
contenido_kit_tareas_bar.py — CONTENIDO propio de «kit-tareas-bar» (hermano
▸ completo de la familia, §5 de `kit-tareas-v2-SPEC.md`).

Fuente de los cambios: `auditorias/kit-tareas-hermanos/kit-tareas-bar-verif.json`
campo `contenido_pendiente` (3 hallazgos: 2 medias, 1 baja) más los
equivalentes de §3 del representante que aplican a un bar de coctelería.

`main.py` lo carga sólo con `--producto kit-tareas-bar` (compone el nombre del
módulo con el pid), así que aquí se puede hablar de «Apertura Barra» o de
«Coctelería Clásica» por su nombre: son hojas de ESTE kit.

Contrato con `main.py`:
    post(wb, fname, cambios) -> bool
`True` = «he cambiado la ESTRUCTURA del libro» (filas u hoja nuevas) y hace que
`main.py` vuelva a pasar `motor.aplicar` antes de `motor.cerrar`, que es lo que
mete las filas nuevas en el rango del contador, en la DV y en el CF, y lo que
convierte la hoja nueva en una hoja de la familia (DV, contador, A4, protección).

QUÉ ES ESTE KIT Y QUÉ NO. Un bar de cócteles NO tiene cocina de partidas: no
hay pescado crudo (anisakis), no hay freidora (aceite en frío) y no hay ni una
tarea de gas en los 11 ficheros. Los equivalentes del representante que sí
aplican se han traducido al oficio de barra, y los que no, están en
`no_aplicados` del informe con su motivo. El riesgo alimentario de un bar no
está en el pescado: está en el HIELO, en los CÍTRICOS y en el garnish, que se
manipulan con la mano desnuda todo el turno, y en los ALÉRGENOS de la carta de
cócteles (el orgeat lleva almendra, el sour clara de huevo, el flip lácteos).

DIFERENCIAS DE MOLDE frente al representante (medidas, no supuestas):
  · este kit SÍ deja fila en blanco entre bloques, así que `_insertar_bloque`
    pinta separadora (a diferencia del de cafetería, que no la usa);
  · no hay hoja «FIFO Semanal» ni congelador de género: la tabla de vida útil
    se traduce a PRODUCTO ABIERTO Y ELABORADO EN BARRA (zumos, jarabes,
    batches, vermut, barril conectado) y vive al pie de «Inventario»;
  · el molde de la hoja nueva «Trimestral y Anual» es «Mantenimiento Mensual»
    de ESTE kit, que trae 3 bloques de 3/4/4 tareas (el del representante trae
    3 de 6/4/4): el contenido está repartido a esa medida, y la revisión de la
    instalación de gas entra después como fila insertada, no forzando el molde;
  · el BONUS-02 de bar es el segundo molde de calendario de la familia
    («# | Fecha | Evento | Preparación Especial | Antelación | Notas», 6
    columnas y la numeración en TEXTO), no el «Mes | Fecha / Evento | …» del
    representante: las fechas nuevas se escriben a esa cabecera y la columna
    «#» se renumera a mano.

RONDA 2 (post motor 2.3) — lo añadido tras `kit-tareas-bar-ver2.json`:
  · DOM-23 de CONTENIDO. El bloque «Se conecta con» de las Instrucciones lo
    pone el motor, pero el hallazgo original tenía una segunda mitad que es de
    contenido: TAREAS que hacen lo mismo que otro fichero del kit sin remitir a
    él. Aquí eran TRES recuentos del mismo dinero —«Cierre de Caja» (09),
    «Cuadrar caja / cierre de TPV» (01) y «Revisar caja y cuadrar con TPV»
    (03)— y DOS anotaciones de la misma merma (01 y 03). Ninguna fila se borra
    (el contador cuenta el rango entero): se reescriben 1:1 como comprobación
    o validación, nombrando el fichero dueño. La parte de APPCC del DOM-23 no
    aplica: `grep APPCC` sobre los 11 ficheros da 0 resultados.
  · Barrido de jefe de barra: separador decimal español en la presión de CO₂,
    «CO2»→«CO₂» en el 08, «Peychaud»→«Peychaud's», «seg»→«segundos»,
    «si necesario»→«si hace falta», «maridaje food»→«la comida del maridaje»,
    los meses del calendario que iban en inglés («13 May», «Sep») y el doble
    paréntesis que dejaba la cola de §2.9 sobre «(limpieza, temperatura)».
  · Vocabulario: un bar de cócteles NO tiene cocina de partidas, así que dos
    textos propios que la nombraban («trasladarlos a barra y cocina», «cierre
    temprano de cocina») pasan a hablar de quien prepara la comida y del
    horario. Queda «si hay cocina de barra», que es una condición legítima.

ANCLAS, NO NÚMEROS DE FILA: este módulo corre DESPUÉS de `motor.aplicar`, que
ya insertó las 5 filas libres, reescribió las temperaturas y renombró las
cabeceras. Si un ancla no aparece se levanta `AnclaPerdida`: mejor caerse que
publicar medio kit.

IDEMPOTENCIA: cada operación mira primero si su resultado ya está en el libro.

Trampas del motor que condicionan la redacción (§8 de la SPEC):
  · `motor.texto_temperatura` añade objetivo y «— anota la lectura: ____ °C» a
    toda tarea con verbo + «temperatura» + equipo de frío. Aquí las anclas y
    los textos nuevos se normalizan con `motor.forma_estable`, que es la
    composición de las cuatro normalizaciones del motor: así el ancla se busca
    tal y como el motor la dejó y lo que escribimos es ya lo que la 2.ª pasada
    volvería a escribir.
  · `motor.texto_appcc` cuelga una coletilla de toda celda con «APPCC»: ningún
    texto de aquí la menciona.
Y del contexto: `motor.contexto` toma la hora ancla del kit de la hora MÁS
TEMPRANA de las hojas de apertura (aquí **15:30**, sacar el mobiliario de
terraza). El bloque de higiene se precarga a esa misma hora —es lo primero que
se hace al entrar— y ninguna tarea nueva lleva una hora anterior, o el ancla se
movería entre pasadas y con ella toda la precarga del 08.
"""
import copy

import motor
from motor import get_column_letter as L

NCOL = 7                     # los 11 checklists del kit son A:G
NCOL_CAL = 6                 # el calendario del BONUS-02 es A:F
VERDE = motor.VERDE

#: `motor.EDITABLES` decide qué columnas se pintan de verde (= desbloqueadas).
#: La hoja nueva «Trimestral y Anual» usa la columna C para el nº de parte del
#: mantenedor, que el cliente TIENE que poder escribir.
motor.EDITABLES.add('Nº de parte')


class AnclaPerdida(RuntimeError):
    """El texto que este módulo esperaba encontrar ya no está en la hoja."""


# ==========================================================================
# Utilidades
# ==========================================================================
def _estable(v):
    """El texto tal y como el motor lo deja (grados, APPCC, temperatura)."""
    return motor.forma_estable(v)


def _fila(ws, texto, col=1):
    # Las dos partes de la comparación pasan por la MISMA normalización que el
    # motor acaba de aplicar a la hoja: buscar «(verificar temperatura 2-4 °C)»
    # tal como está escrito aquí ya no encuentra nada, porque el motor le ha
    # colgado «— anota la lectura: ____ °C» (§2.9 / DOM-R2-22).
    texto = _estable(texto)
    for r in range(1, ws.max_row + 1):
        if _estable(ws.cell(row=r, column=col).value) == texto:
            return r
    return None


def _exige(ws, texto, col=1):
    r = _fila(ws, texto, col)
    if r is None:
        raise AnclaPerdida(f'«{ws.title}»: no encuentro '
                           f'{L(col)}=«{texto}» (kit-tareas-bar)')
    return r


def _estilos(ws, fila, ncol=NCOL):
    return [copy.copy(ws.cell(row=fila, column=c)._style)
            for c in range(1, ncol + 1)]


def _pintar(ws, fila, estilos):
    for c, st in enumerate(estilos, start=1):
        ws.cell(row=fila, column=c)._style = copy.copy(st)


def _fila_blanca(ws, desde):
    """Primera fila del todo vacía a partir de `desde` (la separadora)."""
    for r in range(desde, ws.max_row + 1):
        if all(ws.cell(row=r, column=c).value is None
               for c in range(1, NCOL + 1)):
            return r
    return None


def _escribir_tarea(ws, fila, tarea):
    """(texto, zona, responsable, cuándo) en una fila de tarea."""
    ws.cell(row=fila, column=1).value = 0        # renumerar() pone el ordinal
    for c, v in enumerate(tarea, start=2):
        ws.cell(row=fila, column=c).value = _estable(v)


def _sustituir(ws, viejo, nuevo, col=2):
    """Sustitución 1:1 por texto. Devuelve la fila, o None si ya estaba."""
    if _fila(ws, nuevo, col) is not None:
        return None
    r = _exige(ws, viejo, col)
    ws.cell(row=r, column=col).value = _estable(nuevo)
    return r


def _insertar_tras(ws, ancla, tareas, col=2):
    """Inserta `tareas` justo debajo de la fila cuya col B es `ancla`."""
    if _fila(ws, tareas[0][0], 2) is not None:
        return False                                   # ya insertadas
    r = _exige(ws, ancla, col)
    est = _estilos(ws, r)
    motor.insertar_filas(ws, r + 1, len(tareas))
    for i, t in enumerate(tareas):
        _pintar(ws, r + 1 + i, est)
        _escribir_tarea(ws, r + 1 + i, t)
    return True


def _insertar_bloque(ws, antes_de, titulo, tareas):
    """Bloque nuevo (banda + tareas + fila separadora) delante de otra banda.

    En este kit los bloques SÍ van separados por una fila en blanco (medido en
    «Apertura Barra»: banda 5, tareas 6-16, blanca 17, banda 18): no pintarla
    dejaría el bloque nuevo pegado al siguiente y sólo en esta hoja.
    """
    if _fila(ws, titulo) is not None:
        return False
    idx = _exige(ws, antes_de)
    est_banda = _estilos(ws, idx)
    est_tarea = _estilos(ws, idx + 1)
    blanca = _fila_blanca(ws, idx + 1)
    est_blanca = _estilos(ws, blanca) if blanca else [None] * NCOL
    n = len(tareas) + 2
    motor.insertar_filas(ws, idx, n)
    _pintar(ws, idx, est_banda)
    ws.cell(row=idx, column=1).value = titulo
    motor._merge(ws, f'A{idx}:{L(NCOL)}{idx}')
    for i, t in enumerate(tareas):
        _pintar(ws, idx + 1 + i, est_tarea)
        _escribir_tarea(ws, idx + 1 + i, t)
    if blanca:
        _pintar(ws, idx + n - 1, est_blanca)
    return True


def _instrucciones(wb, encabezado, lineas):
    """Añade un bloque al final de la hoja «Instrucciones».

    `motor.reescribir_instrucciones` (que corre después, en `cerrar`) relee la
    hoja línea a línea y la vuelve a emitir en el molde ▸. El encabezado no
    puede estar en `motor.MIS_BLOQUES` o lo descartaría por ser suyo.
    """
    if 'Instrucciones' not in wb.sheetnames:
        return False
    ws = wb['Instrucciones']
    col = 2 if any(isinstance(ws.cell(row=r, column=2).value, str)
                   for r in range(1, min(ws.max_row, 12) + 1)) else 1
    for r in range(1, ws.max_row + 1):
        if ws.cell(row=r, column=col).value == encabezado:
            return False                               # ya está
    fila = ws.max_row + 2
    ws.cell(row=fila, column=col).value = encabezado
    for i, txt in enumerate(lineas, start=1):
        ws.cell(row=fila + i, column=col).value = '▸ ' + txt
    return True


# ==========================================================================
# 01 — apertura y cierre de barra
# ==========================================================================
#: DOM-12 (equivalente) — la apertura arrancaba encendiendo luces y cortando
#: cítricos. En un bar el manipulador de alimentos es el barback: toca hielo,
#: fruta y garnish con la mano toda la noche, y no había ni una línea de
#: higiene personal en los 11 ficheros. El bloque va al PRINCIPIO, que es
#: cuando se hace, y a las 15:30 —la hora más temprana que ya existe en la
#: hoja—, para no mover la hora ancla del kit entre pasadas.
HIGIENE = [
    ('Uniforme y delantal limpios, pelo recogido y calzado antideslizante '
     '(detrás de la barra el suelo se moja siempre)', 'Barra',
     'Todo el equipo', '15:30'),
    ('Sin anillos, reloj ni pulseras; uñas cortas, limpias y sin esmalte: se '
     'manipulan hielo, cítricos y garnish sin guante', 'Barra',
     'Todo el equipo', '15:30'),
    ('Heridas y cortes cubiertos con apósito impermeable de color visible y '
     'guante encima', 'Barra', 'Todo el equipo', '15:30'),
    ('Lavado de manos al entrar y en cada cambio de tarea; lavamanos de barra '
     'con jabón, papel y agua caliente', 'Barra', 'Todo el equipo', '15:30'),
    ('Declarar síntomas digestivos o respiratorios: quien los tenga no '
     'manipula hielo ni alimentos', 'Barra', 'Head Bartender', '15:30'),
]

#: DOM-24 (equivalente) — «Encender cámaras de barra» daba por hecho que las
#: cámaras se apagan por la noche. No se apagan: lo que hay que hacer al
#: entrar es COMPROBAR que han funcionado y leer la temperatura, porque si el
#: botellero ha estado parado ocho horas el problema no es encenderlo, es el
#: género que hay dentro.
CAMARAS_VIEJO = 'Encender cámaras de barra (verificar temperatura 2-4 °C)'
CAMARAS = ('Comprobar que las cámaras y el botellero de barra han funcionado '
           'toda la noche y registrar temperatura (2-4 °C) — anota la '
           'lectura: ____ °C. Si hay desviación, no sirvas el producto hasta '
           'valorarlo')

#: DOM-18 (equivalente) — el manager anota mermas al cierre del día, pero
#: quien sabe qué se ha roto y qué se ha derramado es la barra, y el pour cost
#: del mes se calcula con ese dato. La tarea entra en el cierre administrativo,
#: junto al inventario rápido de botellas abiertas.
MERMAS_BARRA = [
    ('Anotar las mermas del turno (cristalería rota, derrames, cócteles '
     'devueltos y botella caída): sin este dato el pour cost del mes sale mal',
     'Admin', 'Bartender', '02:15'),
]

#: DOM-23 — «Cuadrar caja / cierre de TPV» en el CIERRE DE BARRA es, palabra
#: por palabra, lo que hacen las 12 tareas de «Cierre de Caja» del fichero 09,
#: y no remitía a él (es el caso literal del hallazgo: «01:Cierre Sala:B21
#: 'Contar efectivo y cuadrar con TPV' sin ninguna referencia al fichero 09,
#: que es exactamente eso»). Repetir un arqueo no es redundancia inocua: son
#: dos recuentos con dos criterios que pueden no cuadrar, y el bartender acaba
#: dando por bueno el que no hizo. No se borra la fila —el contador cuenta el
#: rango entero—: se reescribe 1:1 como lo que sí aporta el cierre de barra,
#: la COMPROBACIÓN de que el hito está hecho, con la remisión al fichero dueño.
CUADRAR_VIEJO = 'Cuadrar caja / cierre de TPV'
CUADRAR = ('Comprobar que el arqueo del día ha quedado cerrado y firmado: el '
           'recuento no se repite aquí, se hace en «Cierre de Caja» del '
           'fichero 09-apertura-cierre-caja.xlsx')

#: Errata de barra: «si necesario» es una elisión que en español pide verbo.
FREGADERO_VIEJO = 'Limpiar fregadero de barra (desatascar si necesario)'
FREGADERO = 'Limpiar fregadero de barra (desatascar si hace falta)'

#: Errata: «seg» no es la abreviatura de segundo (el símbolo es «s») y en una
#: hoja que se imprime conviene la palabra entera, que no se confunde con nada.
MOLIENDA_VIEJO = 'Verificar molienda y calibrar (espresso 25-30 seg, 25-30 ml)'
MOLIENDA = ('Verificar molienda y calibrar (espresso 25-30 segundos, '
            '25-30 ml)')


def _f01(wb, cambios):
    tocado = False
    ws = wb['Apertura Barra']
    if _insertar_bloque(ws, '  Mise en Place de Barra', '  HIGIENE PERSONAL',
                        HIGIENE):
        cambios.append('«Apertura Barra»: bloque «HIGIENE PERSONAL» al inicio '
                       f'({len(HIGIENE)} tareas) — DOM-12 (equivalente)')
        tocado = True
    if _sustituir(ws, CAMARAS_VIEJO, CAMARAS):
        cambios.append('«Apertura Barra»: las cámaras se COMPRUEBAN, no se '
                       'encienden, y la desviación bloquea el género — '
                       'DOM-24 (equivalente)')
    if _sustituir(ws, MOLIENDA_VIEJO, MOLIENDA):
        cambios.append('«Apertura Barra»: «25-30 seg» → «25-30 segundos» '
                       '(«seg» no es abreviatura de segundo)')
    motor.renumerar(ws)

    ws = wb['Cierre Barra']
    if _insertar_tras(ws, 'Registrar botellas abiertas (inventario rápido)',
                      MERMAS_BARRA):
        cambios.append('«Cierre Barra»: tarea de mermas del turno con su '
                       'consecuencia (pour cost) — DOM-18 (equivalente)')
        tocado = True
    if _sustituir(ws, CUADRAR_VIEJO, CUADRAR):
        cambios.append('«Cierre Barra»: el arqueo se COMPRUEBA aquí y se hace '
                       'en «Cierre de Caja» del 09 — antes eran dos recuentos '
                       'paralelos sin remisión — DOM-23')
    if _sustituir(ws, FREGADERO_VIEJO, FREGADERO):
        cambios.append('«Cierre Barra»: «si necesario» → «si hace falta»')
    motor.renumerar(ws)
    return tocado


# ==========================================================================
# 02 — partidas de barra
# ==========================================================================
#: DOM-19 (equivalente, punto de PEDIDO) — el bar prepara orgeat (ALMENDRA),
#: sours con clara de huevo, flips con lácteos y sirve vinos y vermuts con
#: SULFITOS, y en todo el kit no había una sola línea de alérgenos. El
#: Reglamento 1169/2011 obliga a tener la información disponible también en
#: bebidas y en producto sin envasar; el momento de comprobarlo es el
#: pre-servicio, no cuando el cliente ya ha preguntado.
ALERGENOS_CARTA = [
    ('Tener por escrito los alérgenos de la carta de cócteles y que todo el '
     'equipo sepa dónde consultarlos: el orgeat lleva ALMENDRA, los sours '
     'CLARA DE HUEVO, los flips LÁCTEOS y los vinos y vermuts SULFITOS',
     'Coctelería', 'Head Bartender', '16:00'),
]

#: La pala no es una manía: coger hielo con el vaso es la vía más rápida de
#: meter un cristal roto en la cubeta, y entonces hay que vaciarla entera en
#: mitad del servicio.
HIELO_VIEJO = 'Reponer hielo cada hora (o antes si hay pico)'
HIELO = ('Reponer hielo cada hora (o antes si hay pico) SIEMPRE con pala o '
         'pinzas, nunca con el vaso: un vaso roto obliga a vaciar la cubeta '
         'entera')

#: Errata: en español el separador decimal es la COMA. «2.5-3.0 bar» además se
#: lee como dos cifras distintas según el Excel del cliente (el punto es
#: separador de miles en la configuración española).
CO2_VIEJO = 'Verificar presión de CO₂ de barriles (2.5-3.0 bar)'
CO2 = 'Verificar presión de CO₂ de barriles (2,5-3,0 bar)'

#: Errata de barra: el bitter de Nueva Orleans es «Peychaud's» (con genitivo:
#: es el apellido del boticario), «bitters» va en plural cuando se habla de la
#: familia, y «orange bitters» no es nombre propio, así que en minúscula.
BITTER_VIEJO = 'Verificar stock de bitter: Angostura, Peychaud, Orange bitters'
BITTER = ("Verificar stock de bitters: Angostura, Peychaud's y orange bitters")


def _f02(wb, cambios):
    tocado = False
    ws = wb['Coctelería Clásica']
    if _insertar_tras(ws, 'Preparar jarabes especiales: miel-jengibre, '
                          'canela, lavanda, orgeat', ALERGENOS_CARTA):
        cambios.append('«Coctelería Clásica»: alérgenos de la carta de '
                       'cócteles por escrito antes del servicio — DOM-19 '
                       '(equivalente)')
        tocado = True
    if _sustituir(ws, HIELO_VIEJO, HIELO):
        cambios.append('«Coctelería Clásica»: el hielo se repone con pala o '
                       'pinzas, nunca con el vaso')
    if _sustituir(ws, BITTER_VIEJO, BITTER):
        cambios.append('«Coctelería Clásica»: «Peychaud» → «Peychaud\'s» y '
                       '«bitter/Orange bitters» → «bitters/orange bitters» '
                       '(nombre real de la marca y minúscula en el genérico)')
    motor.renumerar(ws)

    ws = wb['Cerveza y Grifo']
    if _sustituir(ws, CO2_VIEJO, CO2):
        cambios.append('«Cerveza y Grifo»: «2.5-3.0 bar» → «2,5-3,0 bar» '
                       '(separador decimal español)')
    motor.renumerar(ws)
    return tocado


# ==========================================================================
# 03 — manager
# ==========================================================================
#: DOM-17 (equivalente) — hallazgo `contenido_pendiente` #1 del verif.json: un
#: bar tiene exactamente el mismo registro horario obligatorio que cualquier
#: hostelería (desde 2019) y ni «Diario Manager» ni «Mensual Manager» lo
#: mencionaban. Con turnos de noche y cierres a las 02:30 es, además, donde
#: más horas extra se discuten.
JORNADA_DIARIA = [
    ('Cerrar y validar el registro diario de jornada del equipo (entradas, '
     'salidas y pausas), incluidas las horas de cierre pasadas las 00:00',
     'Admin', 'Manager', 'Cierre'),
]
JORNADA_MENSUAL = [
    ('Archivar los registros de jornada del mes (hay que conservarlos 4 años '
     'a disposición de la Inspección de Trabajo)', 'Admin', 'Manager',
     '1ª semana'),
]

#: DOM-23 — tercer recuento del mismo dinero: «Cierre de Caja» (09) lo cuenta,
#: «Cierre Barra» (01) lo cuadraba otra vez y el manager, aquí, un tercera.
#: El trabajo del responsable no es volver a contar: es MIRAR EL DESCUADRE que
#: ya calcula la hoja del 09 y firmarlo. Con la remisión al fichero dueño.
CAJA_MANAGER_VIEJO = 'Revisar caja y cuadrar con TPV'
CAJA_MANAGER = ('Revisar el DESCUADRE que ha quedado en «Cierre de Caja» del '
                'fichero 09-apertura-cierre-caja.xlsx y firmarlo: el manager '
                'valida el arqueo, no lo vuelve a contar')

#: Y el mismo dato dos veces: la barra anota las mermas del turno al cierre
#: (01, DOM-18) porque es quien sabe qué se ha roto; si el manager las «anota»
#: también, salen dos cifras distintas y el pour cost del mes se calcula con la
#: que se mire primero. Aquí se revisa lo anotado y se traslada al control.
MERMAS_MANAGER_VIEJO = ('Anotar mermas (rotura cristalería, derrames, '
                        'producto caducado)')
MERMAS_MANAGER = ('Revisar las mermas que ha anotado la barra al cierre '
                  '(cristalería rota, derrames, cócteles devueltos y producto '
                  'caducado) y trasladarlas al control del pour cost')

#: El motor cuelga «(refrigeración 0-4 °C) — anota la lectura: ____ °C» a toda
#: tarea de frío (§2.9), y esta ya terminaba en su propio paréntesis: el
#: cliente leía «(limpieza, temperatura) (refrigeración 0-4 °C)». Se reescribe
#: la base con dos puntos para que la cola del motor case sin chocar.
CAMARAS_MENSUAL_VIEJO = 'Revisar estado de cámaras frigoríficas (limpieza, temperatura)'
CAMARAS_MENSUAL = ('Revisar el estado de las cámaras frigoríficas: limpieza, '
                   'cierre de puertas y temperatura')


def _f03(wb, cambios):
    tocado = False
    ws = wb['Diario Manager']
    if _insertar_tras(ws, 'Planificar necesidades del día siguiente',
                      JORNADA_DIARIA):
        cambios.append('«Diario Manager»: registro diario de jornada '
                       '(obligatorio desde 2019) — DOM-17 (equivalente)')
        tocado = True
    if _sustituir(ws, CAJA_MANAGER_VIEJO, CAJA_MANAGER):
        cambios.append('«Diario Manager»: el manager VALIDA el descuadre del '
                       '09 en vez de hacer un tercer recuento del mismo '
                       'dinero, y la tarea remite al fichero dueño — DOM-23')
    if _sustituir(ws, MERMAS_MANAGER_VIEJO, MERMAS_MANAGER):
        cambios.append('«Diario Manager»: las mermas se ANOTAN una sola vez '
                       '(en «Cierre Barra», DOM-18) y aquí se revisan: dos '
                       'anotaciones daban dos cifras para el mismo pour cost '
                       '— DOM-23')
    motor.renumerar(ws)

    ws = wb['Mensual Manager']
    if _insertar_tras(ws, 'Revisar rentabilidad por categoría (cócteles, '
                          'cerveza, vino, café)', JORNADA_MENSUAL):
        cambios.append('«Mensual Manager»: archivo de los registros de '
                       'jornada del mes — DOM-17 (equivalente)')
        tocado = True
    if _sustituir(ws, CAMARAS_MENSUAL_VIEJO, CAMARAS_MENSUAL):
        cambios.append('«Mensual Manager»: se va el doble paréntesis '
                       '«(limpieza, temperatura) (refrigeración 0-4 °C)» que '
                       'dejaba la cola de §2.9 del motor')
    motor.renumerar(ws)

    if _instrucciones(wb, 'El registro de jornada es obligatorio', [
            'Desde 2019 hay que registrar cada día la entrada, la salida y '
            'las pausas de todo el equipo, y conservar esos registros cuatro '
            'años. En un bar con cierres a las 02:30 es también la única '
            'prueba de las horas que se han hecho de más.',
            'La tarea diaria está en «Diario Manager» (cerrar y validar el '
            'registro del día) y la mensual en «Mensual Manager» (archivar el '
            'mes). El kit no sustituye a tu sistema de fichaje: te recuerda '
            'cerrarlo y guardarlo.']):
        cambios.append('Instrucciones: el registro de jornada y su archivo — '
                       'DOM-17 (equivalente)')
    return tocado


# ==========================================================================
# 05 — semanales, mensuales y (nueva) trimestral/anual
# ==========================================================================
#: DOM-15 (equivalente) — «Descalcificar máquina de espresso» con cadencia
#: mensual fija. La frecuencia real la manda la dureza del agua: en Madrid y
#: en Levante no es la misma cuenta, y descalcificar de más también come
#: juntas. El texto lo dice y remite al análisis de dureza, que vive en la
#: hoja trimestral.
DESCALCIFICAR_VIEJO = 'Descalcificar máquina de espresso'
DESCALCIFICAR = ('Descalcificar la máquina de espresso: la frecuencia depende '
                 'de la dureza de tu agua (mensual con agua dura, trimestral '
                 'con agua blanda o con filtro) — ver la analítica en '
                 '«Trimestral y Anual»')

HOJA_TRIMESTRAL = 'Trimestral y Anual'
TRIMESTRAL_TITULO = 'Mantenimiento Trimestral y Anual — Revisiones Contratadas'
#: El molde es «Mantenimiento Mensual» de este kit: 3 bloques de 3/4/4 tareas.
#: Si el motor cambiara esa geometría, `_hoja_trimestral` aborta en vez de
#: escribir el contenido a medias.
TRIMESTRAL = [
    ('  CONTRATADO — EMPRESA AUTORIZADA', [
        ('Control de plagas (DDD): visita de la empresa autorizada, parte '
         'firmado y certificado en vigor', 'Empresa DDD', 'Trimestral'),
        ('Revisión de extintores y BIE por empresa mantenedora: etiqueta, '
         'acta de revisión y retimbrado a los 5 años', 'Mantenedor', 'Anual'),
        ('Limpieza de la campana y de los conductos de extracción por empresa '
         'homologada (si hay cocina de barra o plancha)', 'Empresa externa',
         'Anual'),
    ]),
    ('  BARRA, FRÍO Y AGUA', [
        ('Limpieza profunda de las líneas de cerveza por el distribuidor o '
         'una empresa especializada, además de la mensual del equipo',
         'Distribuidor', 'Trimestral'),
        ('Revisión de las cámaras, del botellero y de la máquina de hielo por '
         'frigorista: estanqueidad y carga de gas refrigerante', 'Frigorista',
         'Anual'),
        ('Cambiar el filtro de agua de la máquina de hielo y del espresso, y '
         'analizar la dureza del agua para fijar la frecuencia de '
         'descalcificado', 'Técnico', 'Trimestral'),
        ('Prevención de legionela si hay nebulizadores de terraza, torre de '
         'refrigeración o agua caliente de riesgo', 'Empresa autorizada',
         'Anual'),
    ]),
    ('  LICENCIAS, RUIDO Y ADMINISTRACIÓN', [
        ('Revisar el limitador-registrador acústico y su precinto si el local '
         'tiene música: certificado del técnico y descarga de los registros',
         'Técnico acústico', 'Anual'),
        ('Renovar la licencia de terraza y de veladores: horario autorizado, '
         'número de mesas y superficie ocupada', 'Manager', 'Anual'),
        ('Revisar la póliza del local (continente, contenido y '
         'responsabilidad civil), el contrato con las entidades de gestión de '
         'derechos musicales y el del gestor de vidrio', 'Manager', 'Anual'),
        ('Revisión del TPV y del software de facturación (requisitos '
         'antifraude / Verifactu); anotar la fecha de la próxima revisión de '
         'cada contrato y archivar el parte firmado', 'Manager', 'Anual'),
    ]),
]
#: El gas no cabe en el molde de 3/4/4 sin echar fuera algo que sí se
#: inspecciona. Entra después como fila insertada, que es lo que el motor sabe
#: hacer sin romper el contador ni la DV.
GAS_TRIMESTRAL = [
    ('Revisión periódica de la instalación de gas por empresa habilitada y '
     'revisión de las bombonas y los latiguillos de los calefactores de '
     'terraza', None, 'Instalador gas', 'Cada 5 años'),
]

#: DOM-29 (equivalente) — un bar no congela género, así que la tabla de vida
#: útil en congelación no tiene dónde aplicarse. Lo que sí caduca, y nadie
#: anota, es el producto ABIERTO y ELABORADO de la barra: el zumo del día, los
#: jarabes de la casa, los batches y el barril conectado. La tabla va al pie de
#: «Inventario», que es la hoja donde se cuenta, y es editable: las cifras son
#: orientativas y dependen del producto y del local.
TITULO_TABLA = ('VIDA ÚTIL ORIENTATIVA DEL PRODUCTO ABIERTO Y ELABORADO EN '
                'BARRA — ajústala a tu producto y a tu proveedor')
TABLA_VIDA_UTIL = [
    ('Zumo de cítricos recién exprimido', '24 h en frío',
     'Pasado el día pierde acidez y aroma: se exprime por servicio, no por '
     'semana'),
    ('Jarabe simple (1:1)', '3-4 semanas en frío',
     'Un golpe de vodka alarga la vida útil; si enturbia o huele a fermento, '
     'fuera'),
    ('Jarabes con fruta, hierbas o frutos secos (orgeat, gomme)',
     '1-2 semanas en frío',
     'Etiquetar con la fecha de elaboración; el orgeat lleva ALMENDRA y va '
     'declarado en la carta'),
    ('Batch de cóctel SIN cítrico (Negroni, Manhattan)', '2-3 meses',
     'Sólo destilados y vinos fortificados: botella tapada, en frío y fuera '
     'de la luz'),
    ('Batch de cóctel CON cítrico', '2-3 días en frío',
     'Manda el zumo: pasado ese plazo el batch amarga aunque el alcohol '
     'aguante'),
    ('Vermut y vinos fortificados abiertos', '1 mes en cámara',
     'Tapón hermético y frío: también los rojos, que se dejan fuera por '
     'costumbre'),
    ('Vino abierto por copa', '2-3 días',
     'Con argón o sistema de conservación, más; anota la fecha en la propia '
     'botella'),
    ('Barril de cerveza conectado', '3-5 días',
     'Depende de la limpieza de líneas: pasado el plazo sabe a línea sucia, '
     'no a cerveza'),
    ('Garnish cortado (cítricos, pepino, hierbas)', 'El servicio',
     'Se corta por turno: lo del día anterior se ve en la copa y se nota en '
     'el trago'),
    ('Nata montada, claras pasteurizadas y lácteos abiertos',
     '24-48 h en frío',
     'Fecha de apertura en la etiqueta; en duda, fuera: son los alérgenos que '
     'más se sirven en barra'),
]
VIDA_UTIL_TAREA = [
    ('Revisar fechas de jarabes, batches, zumos y botellas abiertas y retirar '
     'lo que supere su vida útil (ver la tabla al pie de esta hoja)', 'Barra',
     'Bartender', 'Lunes'),
]


def _tabla_vida_util(ws, cambios):
    """Tabla editable al pie de «Inventario», debajo de la firma.

    Va FUERA del rango del contador: es una referencia de consulta, no una
    tarea que haya que marcar.
    """
    if _fila(ws, TITULO_TABLA) is not None:
        return False
    firma = _exige(ws, 'Verificado por:')
    g = motor.geometria(ws)
    if not g:
        raise AnclaPerdida('«Inventario»: no es un checklist de la familia')
    banda = _exige(ws, '  Consumibles')
    est_titulo = _estilos(ws, banda)
    est_cab = _estilos(ws, g['hr'])
    est_dato = _estilos(ws, banda + 1)
    n = 3 + len(TABLA_VIDA_UTIL)                  # blanca + título + cabecera
    idx = firma + 1
    motor.insertar_filas(ws, idx, n)
    fila = idx + 1
    _pintar(ws, fila, est_titulo)
    ws.cell(row=fila, column=1).value = TITULO_TABLA
    motor._merge(ws, f'A{fila}:{L(NCOL)}{fila}')
    fila += 1
    _pintar(ws, fila, est_cab)
    ws.cell(row=fila, column=2).value = 'Producto'
    ws.cell(row=fila, column=3).value = 'Vida útil'
    ws.cell(row=fila, column=4).value = 'Notas'
    motor._merge(ws, f'D{fila}:{L(NCOL)}{fila}')
    for i, (familia, vida, nota) in enumerate(TABLA_VIDA_UTIL, start=1):
        r = fila + i
        _pintar(ws, r, est_dato)
        ws.cell(row=r, column=1).value = None
        ws.cell(row=r, column=2).value = familia
        ws.cell(row=r, column=3).value = vida
        ws.cell(row=r, column=4).value = nota
        for c in (2, 3, 4):
            motor._verde(ws.cell(row=r, column=c))
        motor._merge(ws, f'D{r}:{L(NCOL)}{r}')
    cambios.append('«Inventario»: tabla editable de vida útil del producto '
                   f'abierto y elaborado en barra ({len(TABLA_VIDA_UTIL)} '
                   'familias) — DOM-29 (equivalente)')
    return True


def _hoja_trimestral(wb, cambios):
    """DOM-16 (equivalente) — la capa de mantenimiento CONTRATADO.

    «Mantenimiento Mensual» cubre los equipos de la barra (líneas de grifo,
    espresso, cámaras) pero no lo que se CONTRATA y se pide en una inspección:
    DDD, extintores, conductos, gas, legionela, limitador acústico, licencia de
    terraza, seguro y Verifactu. En un bar con música y terraza esa capa es la
    que trae las multas, y no existía en el kit.
    """
    if HOJA_TRIMESTRAL in wb.sheetnames:
        return False
    modelo = wb['Mantenimiento Mensual']
    ws = wb.copy_worksheet(modelo)
    ws.title = HOJA_TRIMESTRAL
    ws.cell(row=1, column=1).value = TRIMESTRAL_TITULO
    g = motor.geometria(ws)
    if not g:
        raise AnclaPerdida(f'«{modelo.title}» no es un checklist de la familia')
    ws.cell(row=g['hr'], column=3).value = 'Nº de parte'
    tope = g['contador'] or ws.max_row
    bandas = [r for r in range(g['hr'] + 1, tope)
              if motor.es_fila_seccion(ws, r)]
    if len(bandas) != len(TRIMESTRAL):
        raise AnclaPerdida(f'«{modelo.title}» tiene {len(bandas)} bloques y el '
                           f'molde de «{HOJA_TRIMESTRAL}» espera '
                           f'{len(TRIMESTRAL)}')
    for banda, (titulo, tareas) in zip(bandas, TRIMESTRAL):
        ws.cell(row=banda, column=1).value = titulo
        filas = []
        for r in range(banda + 1, tope):
            if motor.es_fila_seccion(ws, r):
                break
            if isinstance(ws.cell(row=r, column=1).value, int):
                filas.append(r)
            elif filas:
                break
        if len(filas) != len(tareas):
            raise AnclaPerdida(f'«{HOJA_TRIMESTRAL}»: el bloque '
                               f'«{titulo.strip()}» tiene {len(filas)} filas '
                               f'y el contenido trae {len(tareas)}')
        for r, (texto, resp, cad) in zip(filas, tareas):
            ws.cell(row=r, column=2).value = _estable(texto)
            ws.cell(row=r, column=3).value = None      # lo escribe el cliente
            ws.cell(row=r, column=4).value = resp
            ws.cell(row=r, column=5).value = cad
    cambios.append(f'hoja nueva «{HOJA_TRIMESTRAL}»: mantenimiento contratado '
                   '(DDD, extintores y BIE, conductos, gas, frigorista, '
                   'legionela, limitador acústico, licencia de terraza, '
                   'seguro y Verifactu) con nº de parte y firma — DOM-16 '
                   '(equivalente)')
    return True


def _f05(wb, cambios):
    tocado = False
    # El molde de la hoja nueva es «Mantenimiento Mensual» TAL CUAL sale del
    # motor, así que se clona ANTES de reescribirle el descalcificado. En la
    # 2.ª pasada la hoja ya existe y no se clona.
    if _hoja_trimestral(wb, cambios):
        tocado = True

    ws = wb['Mantenimiento Mensual']
    if _sustituir(ws, DESCALCIFICAR_VIEJO, DESCALCIFICAR):
        cambios.append('«Mantenimiento Mensual»: el descalcificado del '
                       'espresso deja de ser mensual por decreto y depende de '
                       'la dureza del agua — DOM-15 (equivalente)')

    ws = wb[HOJA_TRIMESTRAL]
    if _insertar_tras(ws, 'Limpieza de la campana y de los conductos de '
                          'extracción por empresa homologada (si hay cocina '
                          'de barra o plancha)', GAS_TRIMESTRAL):
        cambios.append(f'«{HOJA_TRIMESTRAL}»: revisión periódica de la '
                       'instalación de gas y de las bombonas de los '
                       'calefactores de terraza — DOM-16 (equivalente)')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Inventario']
    if _insertar_tras(ws, 'Contar stock de café en grano y leches',
                      VIDA_UTIL_TAREA):
        cambios.append('«Inventario»: tarea de retirada de producto abierto '
                       'que ha pasado su vida útil — DOM-29 (equivalente)')
        tocado = True
    motor.renumerar(ws)
    if _tabla_vida_util(ws, cambios):
        tocado = True

    if _instrucciones(wb, 'Trimestral, anual y vida útil del producto abierto',
                      [
            'La hoja «Trimestral y Anual» recoge el mantenimiento que se '
            'CONTRATA y que se pide en una inspección: DDD, extintores y BIE, '
            'conductos de extracción, instalación de gas, frigorista, '
            'legionela, limitador acústico, licencia de terraza, seguro y '
            'facturación.',
            'Anota el número de parte en la columna verde y firma cuando la '
            'empresa haya venido; la última tarea de la hoja es apuntar la '
            'fecha de la próxima revisión de cada contrato.',
            'Al pie de «Inventario» tienes una tabla editable con la vida '
            'útil del producto abierto y elaborado de la barra: zumos, '
            'jarabes, batches, vermut abierto y barril conectado. Son cifras '
            'orientativas — ajústalas a tu producto y a tu rotación.']):
        cambios.append('Instrucciones: hoja trimestral/anual y tabla de vida '
                       'útil en barra — DOM-16 / DOM-29 (equivalentes)')
    return tocado


# ==========================================================================
# 06 — eventos y festivos
# ==========================================================================
#: DOM-19 (equivalente) — hallazgo `contenido_pendiente` #2 del verif.json:
#: «Maridaje Catas» sirve quesos, chocolates y tapas a un grupo cerrado y no
#: pedía los alérgenos por ningún sitio; también es el único evento del kit con
#: reserva, señal y número final de asistentes, y nada de eso estaba por
#: escrito. El bloque va DELANTE de «Preparación»: no sirve de nada preguntar
#: por las intolerancias cuando ya has comprado el queso.
RESERVA = [
    # Un bar de cócteles no tiene cocina de partidas (ver la cabecera del
    # módulo): el maridaje de una cata lo monta la barra o un proveedor.
    ('Recoger POR ESCRITO alérgenos, intolerancias y dietas de los asistentes '
     'y trasladarlos a la barra y a quien prepare la comida del maridaje (en '
     'una cata, frutos secos y sulfitos son los dos que siempre aparecen)',
     'Admin', 'Manager', 'Al confirmar'),
    ('Cerrar por escrito el precio por persona y qué incluye: número de '
     'piezas, maridaje de comida, copa de despedida y si hay botella para '
     'llevar', 'Admin', 'Manager', 'Al confirmar'),
    ('Cobrar la señal o el anticipo y dejar constancia del importe y la fecha',
     'Admin', 'Manager', 'Al confirmar'),
    ('Firmar la política de cancelación y el plazo para dar el número final '
     'de asistentes', 'Admin', 'Manager', 'Al confirmar'),
    ('Acordar la hora de entrada y de salida del espacio y quién monta y '
     'desmonta la sala', 'Admin', 'Manager', 'Al confirmar'),
]

#: La misma obligación, en el evento que se repite cada semana: la tapa de
#: cortesía es gratis, pero la información de alérgenos no es opcional por
#: serlo.
ALERGENOS_SNACKS = [
    ('Tener por escrito los alérgenos de los snacks y las tapas de cortesía y '
     'que el equipo sepa dónde consultarlos: que sean gratis no exime de '
     'informar', 'Barra', 'Manager', '17:30'),
]

#: Errata: «maridaje food» es medio inglés y medio español y no significa nada
#: en ninguno de los dos. Además tiene que decir lo mismo que la tarea que
#: ahora abre la hoja («…y a quien prepare la comida del maridaje»).
MARIDAJE_VIEJO = 'Preparar maridaje food (quesos, chocolates, tapas)'
MARIDAJE = 'Preparar la comida del maridaje (quesos, chocolates y tapas)'


def _f06(wb, cambios):
    tocado = False
    ws = wb['Maridaje Catas']
    if _insertar_bloque(ws, '  Preparación', '  AL CONFIRMAR LA RESERVA',
                        RESERVA):
        cambios.append('«Maridaje Catas»: bloque «AL CONFIRMAR LA RESERVA» '
                       '(alérgenos por escrito, precio por persona, señal, '
                       'cancelación) — DOM-19 (equivalente)')
        tocado = True
    if _sustituir(ws, MARIDAJE_VIEJO, MARIDAJE):
        cambios.append('«Maridaje Catas»: «maridaje food» → «la comida del '
                       'maridaje» (ni inglés ni español, y ahora dice lo mismo '
                       'que la tarea de alérgenos que abre la hoja)')
    motor.renumerar(ws)

    ws = wb['After Work']
    if _insertar_tras(ws, 'Preparar snacks / tapas de cortesía (si aplica)',
                      ALERGENOS_SNACKS):
        cambios.append('«After Work»: alérgenos de los snacks de cortesía — '
                       'DOM-19 (equivalente)')
        tocado = True
    motor.renumerar(ws)

    if _instrucciones(wb, 'Antes de cerrar una cata o un evento privado', [
            'La hoja «Maridaje Catas» arranca ahora en el momento en que se '
            'confirma la reserva, no dos días antes: alérgenos e '
            'intolerancias por escrito, precio por persona y qué incluye, '
            'señal cobrada, política de cancelación y plazo para el número '
            'final de asistentes.',
            'Los alérgenos también van en la barra del día a día: la carta de '
            'cócteles los declara en «Coctelería Clásica» (02) y los snacks '
            'de cortesía del after-work, en su propia hoja. Que un producto '
            'sea gratis o sea una bebida no exime de informar.']):
        cambios.append('Instrucciones: qué se cierra al confirmar una cata y '
                       'dónde están los alérgenos — DOM-19 (equivalente)')
    return tocado


# ==========================================================================
# 08 — apertura y cierre del negocio
# ==========================================================================
#: Errata de consistencia: el kit escribe «CO₂» con subíndice en los otros dos
#: sitios donde aparece el gas de la cerveza («Cerveza y Grifo» del 02 y
#: «Mantenimiento Mensual» del 05) y aquí lo dejaba como «CO2». Es el mismo
#: gas y el mismo equipo, y esta es la hoja que se imprime todos los días.
#: NO se toca nada más del 08: es el fichero precargado por el motor.
CO2_NEGOCIO_VIEJO = 'Verificar grifos de cerveza y presión CO2'
CO2_NEGOCIO = 'Verificar grifos de cerveza y presión de CO₂'


def _f08(wb, cambios):
    ws = wb['Apertura del Negocio']
    if _sustituir(ws, CO2_NEGOCIO_VIEJO, CO2_NEGOCIO):
        cambios.append('«Apertura del Negocio»: «presión CO2» → «presión de '
                       'CO₂», como en «Cerveza y Grifo» (02) y «Mantenimiento '
                       'Mensual» (05)')
    return False                                   # sin cambio estructural


# ==========================================================================
# BONUS-02 — calendario anual
# ==========================================================================
#: Hallazgo `contenido_pendiente` #3 del verif.json: 17 fechas frente a las 22
#: del representante, y las que faltaban no son de relleno — son los festivos
#: y puentes en los que un bar factura el doble y tiene que pedir stock con
#: semanas de antelación. Fila = (evento ancla, antes/después, columnas B..F).
#: El molde de este calendario es «# | Fecha | Evento | Preparación Especial |
#: Antelación | Notas» y la numeración va en TEXTO, así que se renumera aparte.
FECHAS = [
    ('San Valentín', 'antes',
     ('1 Enero', 'Año Nuevo',
      'Decidir si se abre; si se cierra, comunicarlo en Google Business '
      'Profile y en RRSS con una semana',
      '1 semana', 'La madrugada del 1 es la resaca de la noche más fuerte '
      'del año')),
    ('San Valentín', 'despues',
     ('Feb-Mar', 'Carnaval',
      'Cócteles temáticos, decoración, horario ampliado y control de aforo '
      'con disfraces',
      '2 semanas', 'Variable según zona; en muchas ciudades es la noche del '
      'año')),
    ('Semana Santa', 'despues',
     ('1 Mayo', 'Día del Trabajo y puentes de primavera',
      'Horario de festivo, terraza a pleno rendimiento y stock para varios '
      'días seguidos',
      '2 semanas', 'Un puente mueve más que un sábado normal y se pide con '
      'el mismo plazo')),
    ('Temporada Verano', 'despues',
     ('15 Agosto', 'Asunción y fiestas de agosto',
      'Servicio de festivo, refuerzo de turnos y stock extra de hielo y '
      'cítricos',
      '1 semana', 'Muchas fiestas patronales caen esa semana: mira el '
      'calendario local')),
    ('Beaujolais Nouveau', 'despues',
     ('6-8 Diciembre', 'Puente de la Constitución y la Inmaculada',
      'Horario de festivo, refuerzo de mediodía y stock para tres días '
      'seguidos',
      '2 semanas', 'Arranca de hecho la temporada de cenas de empresa')),
    ('Navidad/Empresas', 'despues',
     ('24 Diciembre', 'Nochebuena',
      'Decidir el horario (muchos bares cierran la tarde y abren sólo la '
      'madrugada), turno reducido y comunicar el horario del día en Google '
      'Business Profile y en RRSS',
      '3 semanas', 'La copa de después de la cena familiar es un pico corto '
      'y muy rentable')),
]

#: Erratas del calendario heredado: dos eventos llevan el mes EN INGLÉS y
#: abreviado en mitad de una hoja escrita en español («13 May», «Sep»). Son la
#: columna «Evento» (C), que es la que se lee de un vistazo.
MESES_CAL = [
    ('World Cocktail Day (13 May)', 'World Cocktail Day (13 de mayo)'),
    ('Negroni Week (Sep)', 'Negroni Week (septiembre)'),
]


def _bonus02(wb, cambios):
    ws = wb['Calendario Anual']
    hr = motor.fila_calendario(ws)
    if hr is None:
        raise AnclaPerdida('«Calendario Anual»: no reconozco la cabecera del '
                           'calendario (¿ha cambiado el molde?)')
    nuevas = 0
    for ancla, donde, fila in FECHAS:
        if _fila(ws, fila[1], 3) is not None:
            continue                                   # ya insertada
        r = _exige(ws, ancla, 3)
        est = _estilos(ws, r, NCOL_CAL)
        destino = r if donde == 'antes' else r + 1
        motor.insertar_filas(ws, destino, 1)
        _pintar(ws, destino, est)
        for c, v in enumerate(fila, start=2):
            ws.cell(row=destino, column=c).value = v
        nuevas += 1
    if nuevas:
        cambios.append(f'«Calendario Anual»: {nuevas} fechas que faltaban '
                       '(Año Nuevo, Carnaval, 1 de mayo, 15 de agosto, puente '
                       'de diciembre y Nochebuena)')
    for viejo, nuevo in MESES_CAL:
        if _sustituir(ws, viejo, nuevo, col=3):
            cambios.append(f'«Calendario Anual»: «{viejo}» → «{nuevo}» (el '
                           'mes iba en inglés y abreviado)')
    # La columna «#» de este molde es TEXTO y no la renumera el motor: sin
    # esto, el calendario se publicaría con dos «1» y saltando del 3 al 5.
    n = 0
    for r in range(hr + 1, ws.max_row + 1):
        v = ws.cell(row=r, column=2).value
        if not (isinstance(v, str) and v.strip()):
            continue
        if motor.es_fila_seccion(ws, r):
            continue
        n += 1
        cel = ws.cell(row=r, column=1)
        if cel.value != str(n):
            cel.value = str(n)
    return bool(nuevas)


# ==========================================================================
# API
# ==========================================================================
FICHEROS = {
    '01-apertura-cierre.xlsx': _f01,
    '02-partidas-cocina.xlsx': _f02,
    '03-tareas-manager.xlsx': _f03,
    '05-tareas-semanales-mensuales.xlsx': _f05,
    '06-eventos-festivos.xlsx': _f06,
    '08-apertura-cierre-negocio.xlsx': _f08,
    'BONUS-02-calendario-anual-tareas.xlsx': _bonus02,
}


def post(wb, fname, cambios):
    """CONTENIDO sobre un libro ya normalizado por `motor.aplicar`.

    Devuelve True si ha cambiado la ESTRUCTURA (filas u hojas nuevas), que es
    la señal para que `main.py` vuelva a pasar el motor antes de cerrar.
    """
    fn = FICHEROS.get(fname)
    if fn is None:
        return False
    return bool(fn(wb, cambios))
