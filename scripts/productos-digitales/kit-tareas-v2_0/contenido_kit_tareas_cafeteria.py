#!/usr/bin/env python3
"""
contenido_kit_tareas_cafeteria.py — CONTENIDO propio de «kit-tareas-cafeteria»
(hermano ▸ completo de la familia, §5 de `kit-tareas-v2-SPEC.md`).

Fuente de los cambios: `auditorias/kit-tareas-hermanos/kit-tareas-cafeteria-verif.json`
campo `contenido_pendiente` (8 hallazgos: 2 altas, 4 medias, 2 bajas) más los
equivalentes de §3 del representante que aplican a una cafetería / brunch.

`main.py` lo carga sólo con `--producto kit-tareas-cafeteria` (compone el
nombre del módulo con el pid), así que aquí se puede hablar de «Apertura Barra
Café» o de «Pastelería Vitrina» por su nombre: son hojas de ESTE kit.

Contrato con `main.py`:
    post(wb, fname, cambios) -> bool
`True` = «he cambiado la ESTRUCTURA del libro» (filas u hoja nuevas) y hace que
`main.py` vuelva a pasar `motor.aplicar` antes de `motor.cerrar`, que es lo que
mete las filas nuevas en el rango del contador, en la DV y en el CF, y lo que
convierte la hoja nueva en una hoja de la familia (DV, contador, A4, protección).

DIFERENCIAS DE MOLDE frente al representante (medidas, no supuestas):
  · este kit NO deja fila en blanco entre bloques (el representante sí), así que
    `_insertar_bloque` no pinta separadora: pintarla metería una fila hueca en
    mitad de una tabla que no las usa;
  · «FIFO Semanal» no tiene «Verificado por:» sino «Firma encargado/a: …», y no
    tiene banda «  CONGELADOR»: la tabla de vida útil se ancla por PREFIJO y
    toma sus estilos de «  FRESCOS»;
  · el molde de la hoja nueva «Trimestral y Anual» es «Mantenimiento Mensual» de
    ESTE kit, que trae 4 bloques de 4/3/5/3 tareas (el del representante trae 3
    de 6/4/4): el contenido está repartido a esa medida o `AnclaPerdida` para el
    dry-run entero.

ANCLAS, NO NÚMEROS DE FILA: este módulo corre DESPUÉS de `motor.aplicar`, que ya
insertó filas libres, reescribió temperaturas y renombró cabeceras. Si un ancla
no aparece se levanta `AnclaPerdida`: mejor caerse que publicar medio kit.

IDEMPOTENCIA: cada operación mira primero si su resultado ya está en el libro.

Trampas del motor que condicionan la redacción (§8 de la SPEC):
  · `motor.texto_temperatura` añade objetivo y «— anota la lectura: ____ °C» a
    toda tarea con verbo + «temperatura» + equipo de frío. Los textos de aquí
    que encajan en ese patrón YA traen la coletilla, o la 2.ª pasada se la
    añadiría y la idempotencia se caería.
  · `motor.texto_grados` normaliza los grados: los signos menos se escriben con
    U+2212 y las unidades con espacio, tal y como quedarán.
  · `motor.texto_appcc` cuelga una coletilla de toda celda con «APPCC»: ningún
    texto de aquí la menciona.
Y del contexto: `motor.contexto` toma la hora ancla del kit de la hora más
temprana de las hojas de apertura (aquí 06:45, la máquina de espresso). Ninguna
tarea nueva lleva una hora anterior a esa.
"""
import copy

import motor
from motor import get_column_letter as L

NCOL = 7                     # los 11 ficheros del kit son A:G
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
def _fila(ws, texto, col=1):
    # El ancla se normaliza con la MISMA regla de grados que el motor acaba de
    # aplicar a la hoja (DOM-R2-22).
    texto = motor.texto_grados(texto)
    for r in range(1, ws.max_row + 1):
        if motor.texto_grados(ws.cell(row=r, column=col).value) == texto:
            return r
    return None


def _exige(ws, texto, col=1):
    r = _fila(ws, texto, col)
    if r is None:
        raise AnclaPerdida(f'«{ws.title}»: no encuentro '
                           f'{L(col)}=«{texto}» (kit-tareas-cafeteria)')
    return r


def _fila_prefijo(ws, prefijo, col=1):
    for r in range(1, ws.max_row + 1):
        v = ws.cell(row=r, column=col).value
        if isinstance(v, str) and v.startswith(prefijo):
            return r
    return None


def _exige_prefijo(ws, prefijo, col=1):
    r = _fila_prefijo(ws, prefijo, col)
    if r is None:
        raise AnclaPerdida(f'«{ws.title}»: no encuentro ninguna fila que '
                           f'empiece por «{prefijo}» en {L(col)}')
    return r


def _estilos(ws, fila):
    return [copy.copy(ws.cell(row=fila, column=c)._style)
            for c in range(1, NCOL + 1)]


def _pintar(ws, fila, estilos):
    for c, st in enumerate(estilos, start=1):
        ws.cell(row=fila, column=c)._style = copy.copy(st)


def _escribir_tarea(ws, fila, tarea):
    """(texto, zona, responsable, tiempo) en una fila de tarea."""
    ws.cell(row=fila, column=1).value = 0        # renumerar() pone el ordinal
    for c, v in enumerate(tarea, start=2):
        ws.cell(row=fila, column=c).value = v


def _sustituir(ws, viejo, nuevo, col=2):
    """Sustitución 1:1 por texto. Devuelve la fila, o None si ya estaba."""
    if _fila(ws, nuevo, col) is not None:
        return None
    r = _exige(ws, viejo, col)
    ws.cell(row=r, column=col).value = nuevo
    return r


def _filas_de_bloque(ws, banda):
    """(fila de la banda, filas de tarea) de un bloque de sección."""
    b = _exige(ws, banda)
    filas = []
    for r in range(b + 1, ws.max_row + 1):
        if motor.es_fila_seccion(ws, r):
            break
        if isinstance(ws.cell(row=r, column=1).value, int):
            filas.append(r)
        elif filas:
            break
    return b, filas


def _reordenar_bloque(ws, banda, tareas):
    """Reescribe EN ORDEN las tareas de un bloque (mismo número de filas).

    No mueve filas: reescribe valores, que es lo único que cambia de sitio, así
    que no hay que tocar merges, DV ni el rango del contador.
    """
    b, filas = _filas_de_bloque(ws, banda)
    if len(filas) != len(tareas):
        raise AnclaPerdida(f'«{ws.title}»: el bloque «{banda.strip()}» tiene '
                           f'{len(filas)} tareas y esperaba {len(tareas)}')
    if all(ws.cell(row=f, column=2).value == t[0]
           for f, t in zip(filas, tareas)):
        return False                                   # ya reordenado
    for f, t in zip(filas, tareas):
        _escribir_tarea(ws, f, t)
    return True


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
    """Bloque nuevo (banda + tareas) delante de otra banda.

    SIN fila separadora: en este kit los bloques van pegados (banda, tareas,
    banda). Pintar una separadora como hace el representante metería una fila
    hueca en mitad de la tabla y en un molde que no las usa canta.
    """
    if _fila(ws, titulo) is not None:
        return False
    idx = _exige(ws, antes_de)
    est_banda = _estilos(ws, idx)
    est_tarea = _estilos(ws, idx + 1)
    motor.insertar_filas(ws, idx, len(tareas) + 1)
    _pintar(ws, idx, est_banda)
    ws.cell(row=idx, column=1).value = titulo
    motor._merge(ws, f'A{idx}:{L(NCOL)}{idx}')
    for i, t in enumerate(tareas):
        _pintar(ws, idx + 1 + i, est_tarea)
        _escribir_tarea(ws, idx + 1 + i, t)
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
# 01 — apertura y cierre por área
# ==========================================================================
#: DOM-12 (equivalente) — la cafetería tenía «HIGIENE Y SEGURIDAD» al FINAL de
#: la apertura de cocina: impreso, el equipo se lava las manos y se pone el
#: uniforme DESPUÉS de haber tocado el género. El bloque personal sube al
#: principio, que es cuando se hace.
HIGIENE = [
    ('Uniforme y calzado de trabajo limpios, delantal cambiado y pelo '
     'recogido (gorro o redecilla)', 'Cocina', 'Todo el equipo', '07:00'),
    ('Sin anillos, reloj ni pulseras; uñas cortas, limpias y sin esmalte',
     'Cocina', 'Todo el equipo', '07:00'),
    ('Heridas y cortes cubiertos con apósito impermeable de color visible y '
     'guante encima', 'Cocina', 'Todo el equipo', '07:00'),
    ('Lavado de manos al entrar y en cada cambio de tarea; lavamanos con '
     'jabón, papel y agua caliente', 'Cocina', 'Todo el equipo', '07:00'),
    ('Declarar síntomas digestivos o respiratorios: quien los tenga no '
     'manipula alimentos', 'Cocina', 'Encargado/a', '07:00'),
]

#: Con el bloque personal arriba, la primera tarea del bloque de higiene que
#: quedaba al final («Lavarse las manos y colocarse uniforme completo») pasaba a
#: decir dos veces lo mismo. Se cambia por la comprobación diaria que NO tenía
#: nadie: la mensual revisa presión y caducidad del extintor, no que se pueda
#: llegar a él.
BOTIQUIN = ('Comprobar que el botiquín y el extintor están accesibles y sin '
            'nada delante')

#: DOM-13 (equivalente, ALTA) — el orden impreso era el inseguro: horno (fila 6)
#: y plancha (fila 7) ANTES que la campana (fila 8), y ningún paso de gas. Se
#: inserta la comprobación de gas y se reescribe el bloque entero en el orden en
#: que se hace de verdad: campana → gas → fuego.
GAS = [
    ('Si el local tiene gas: abrir la llave general y comprobar que NO huele '
     'a gas; si huele, no enciendas nada, ventila y avisa al mantenedor',
     'Cocina', 'Cocinero apertura', '07:00'),
]
ENCENDIDO = [
    ('Encender la campana extractora y ventilar la cocina ANTES de encender '
     'nada más', 'Cocina', 'Cocinero apertura', '07:00'),
    ('Si el local tiene gas: abrir la llave general y comprobar que NO huele '
     'a gas; si huele, no enciendas nada, ventila y avisa al mantenedor',
     'Cocina', 'Cocinero apertura', '07:00'),
    ('Encender el horno y precalentar para croissants, quiches y bollería',
     'Cocina', 'Cocinero apertura', '07:00'),
    ('Encender plancha/grill y tostadora para tostadas y brunch', 'Cocina',
     'Cocinero apertura', '07:00'),
    ('Encender baño maría (si aplica)', 'Cocina', 'Cocinero apertura',
     '07:15'),
    # DOM-24 (equivalente): «Verificar cámaras: temperaturas OK» no dice qué se
    # verifica de la NOCHE, que es cuando fallan. Trae ya la coletilla de
    # `motor.texto_temperatura` (contiene «____ °C», así que el motor la deja).
    ('Comprobar que las cámaras frigoríficas han funcionado toda la noche y '
     'registrar temperatura (refrigeración 0-4 °C) — anota la lectura: '
     '____ °C. Si hay desviación, no uses el género hasta valorarlo',
     'Cocina', 'Cocinero apertura', '07:00'),
]

#: Hallazgo «aceite en frío (freidora)» (media) — B16 mandaba vaciar la freidora
#: sin decir a qué temperatura. Es la quemadura más habitual de un cierre.
ACEITE = ('Vaciar y limpiar la freidora (si aplica): manipular el aceite SÓLO '
          'por debajo de 40 °C, nunca en caliente, con guantes y recipiente '
          'estable; el aceite usado, al bidón del gestor autorizado')


def _f01(wb, cambios):
    tocado = False
    ws = wb['Apertura Cocina']
    if _insertar_bloque(ws, '  ENCENDIDO DE EQUIPOS', '  HIGIENE PERSONAL',
                        HIGIENE):
        cambios.append('«Apertura Cocina»: bloque «HIGIENE PERSONAL» al '
                       f'inicio ({len(HIGIENE)} tareas), que estaba al final '
                       'del checklist — DOM-12 (equivalente)')
        tocado = True
    if _sustituir(ws, 'Lavarse las manos y colocarse uniforme completo',
                  BOTIQUIN):
        cambios.append('«Apertura Cocina»: la tarea de higiene que quedaba '
                       'duplicada al final pasa a comprobar botiquín y '
                       'extintor accesibles — DOM-12 (equivalente)')
    if _insertar_tras(ws, 'Encender campana extractora', GAS):
        cambios.append('«Apertura Cocina»: comprobación de la llave de gas '
                       'ANTES de encender fuego, que no existía — DOM-13 '
                       '(equivalente, alta)')
        tocado = True
    if _reordenar_bloque(ws, '  ENCENDIDO DE EQUIPOS', ENCENDIDO):
        cambios.append('«Apertura Cocina»: «ENCENDIDO DE EQUIPOS» en orden '
                       'seguro (campana → gas → fuego) y las cámaras se '
                       '«comprueban» desde la noche anterior — DOM-13 / '
                       'DOM-24 (equivalentes)')
    motor.renumerar(ws)

    ws = wb['Cierre Cocina']
    if _sustituir(ws, 'Vaciar y limpiar freidora (si aplica)', ACEITE):
        cambios.append('«Cierre Cocina»: el aceite se manipula por debajo de '
                       '40 °C y se entrega a gestor autorizado — DOM-27 '
                       '(equivalente)')
    return tocado


# ==========================================================================
# 02 — partidas de cocina
# ==========================================================================
#: Hallazgo «anisakis / pescado listo para consumo» (media) — el kit maneja
#: salmón ahumado en la mise en place de Calientes y en el pedido del brunch, y
#: no mencionaba en ninguna hoja la congelación previa que exige el Reglamento
#: (CE) 853/2004 para pescado que se sirve sin cocción completa (el ahumado en
#: frío incluido). La palabra «ANISAKIS» va en el texto a propósito: es la que
#: el cocinero y el inspector buscan con Ctrl+F.
ANISAKIS = [
    ('Salmón ahumado y pescado que se sirve sin cocinar — prevención de '
     'ANISAKIS: exigir al proveedor el certificado de congelación previa '
     '(≥24 h a −20 °C o −35 °C 15 h) o congelarlo tú, y anotar el lote',
     'Cocina', 'Cocinero calientes', '07:15'),
]

#: Equivalente de DOM-26: «Lavar y desinfectar vegetales frescos» no dice ni con
#: qué ni a qué dosis, y sin el aclarado final la lejía se sirve en el bowl.
LECHUGAS = ('Lavar y desinfectar las hojas verdes y los vegetales que se '
            'sirven crudos con lejía apta para uso alimentario según la dosis '
            'del fabricante (habitual: 70 ppm, 5 min) y ACLARAR con agua '
            'potable abundante')

#: Hallazgo «mermas» (media) — ninguna de las tres hojas de cocina anotaba la
#: merma del día pese a manejar producto fresco de vida corta. «Anotar consumos»
#: no es lo mismo: el consumo es lo que se vende, la merma es lo que se tira.
MERMAS_CALIENTES = [
    ('Anotar las mermas del turno (producto, cantidad y motivo): sin este '
     'dato el food cost del mes sale mal', 'Cocina', 'Cocinero calientes',
     '15:00'),
]
MERMAS_FRIOS = [
    ('Anotar las mermas del turno: fruta cortada, aguacate y bowls montados '
     'que no se han vendido', 'Cocina', 'Cocinero fríos', '15:00'),
]
#: En la vitrina la merma ya tenía media tarea («vendido vs producido»), así que
#: se amplía en 1:1 en vez de insertar una fila que diría casi lo mismo.
MERMAS_VITRINA = ('Anotar producción, ventas y MERMA del día (piezas '
                  'retiradas, regaladas o al personal): es el dato que ajusta '
                  'la producción de mañana')


def _f02(wb, cambios):
    tocado = False
    ws = wb['Calientes']
    if _insertar_tras(ws, 'Preparar mise en place: bacon, huevos, salmón '
                          'ahumado', ANISAKIS):
        cambios.append('«Calientes»: congelación preventiva frente al '
                       'ANISAKIS del salmón ahumado (Rgto. CE 853/2004) — '
                       'DOM-02 (equivalente)')
        tocado = True
    if _insertar_tras(ws, 'Anotar consumos del día para pedidos',
                      MERMAS_CALIENTES):
        cambios.append('«Calientes»: tarea de mermas del turno — DOM-18 '
                       '(equivalente)')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Fríos']
    if _sustituir(ws, 'Lavar y desinfectar vegetales frescos', LECHUGAS):
        cambios.append('«Fríos»: desinfección de vegetales de consumo crudo '
                       'con dosis y aclarado — DOM-26 (equivalente)')
    if _insertar_tras(ws, 'Anotar consumos para pedidos', MERMAS_FRIOS):
        cambios.append('«Fríos»: tarea de mermas del turno — DOM-18 '
                       '(equivalente)')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Pastelería Vitrina']
    if _sustituir(ws, 'Anotar lo que se ha vendido vs producido (para '
                      'ajustar)', MERMAS_VITRINA):
        cambios.append('«Pastelería Vitrina»: la merma del día se anota con '
                       'la producción y la venta — DOM-18 (equivalente)')
    return tocado


# ==========================================================================
# 03 — manager
# ==========================================================================
#: Hallazgo «registro de jornada» (ALTA) — no había ninguna tarea de cierre ni
#: de archivo del registro horario en las cuatro hojas del 03, y es obligación
#: legal en España desde el RD-ley 8/2019 (conservación 4 años).
JORNADA_DIARIA = [
    ('Cerrar y validar el registro diario de jornada del equipo (entradas, '
     'salidas y pausas)', 'Office', 'Manager', '17:15'),
]
JORNADA_MENSUAL = [
    ('Archivar los registros de jornada del mes (hay que conservarlos 4 '
     'años)', 'Office', 'Manager', 'Día 1'),
]


def _f03(wb, cambios):
    tocado = False
    ws = wb['Diario Manager']
    if _insertar_tras(ws, 'Revisar planificación de personal para mañana',
                      JORNADA_DIARIA):
        cambios.append('«Diario Manager»: cierre y validación del registro '
                       'diario de jornada (RD-ley 8/2019) — DOM-17 '
                       '(equivalente, alta)')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Mensual Manager']
    if _insertar_tras(ws, 'Actualizar cuadrante de vacaciones',
                      JORNADA_MENSUAL):
        cambios.append('«Mensual Manager»: archivo de los registros de '
                       'jornada del mes — DOM-17 (equivalente, alta)')
        tocado = True
    motor.renumerar(ws)
    return tocado


# ==========================================================================
# 05 — semanales, mensuales y (nueva) trimestral/anual
# ==========================================================================
#: Hallazgo «vida útil de congelación» (baja) — «Revisar pan: congelar lo que no
#: se usará» sin plazo, y ninguna referencia de cuánto aguanta cada familia.
VIDA_UTIL = ('Revisar el pan y la bollería: congelar EN EL DÍA lo que no se '
             'usará y etiquetar con la fecha (vida útil por familia en la '
             'tabla del pie de esta hoja)')
TITULO_TABLA = ('VIDA ÚTIL ORIENTATIVA EN CONGELACIÓN A −18 °C — ajústala a tu '
                'producto y a tu proveedor')
TABLA_VIDA_UTIL = [
    ('Croissants y masas de bollería crudas', '1-2 meses',
     'La levadura pierde fuerza: después sube mal aunque sea seguro comerlo'),
    ('Pan y bollería ya horneada', '1-3 meses',
     'Pierde textura antes que seguridad; descongela y regenera en horno'),
    ('Tartas y bizcochos sin nata montada', '2-3 meses',
     'La nata montada y las cremas de huevo NO aguantan la congelación'),
    ('Salmón ahumado y pescado azul', '2-3 meses',
     'La grasa se enrancia aunque esté congelado: es el que antes se '
     'estropea'),
    ('Bacon, jamón y embutido loncheado', '1-2 meses',
     'La sal acelera el enranciamiento de la grasa'),
    ('Fruta troceada y pulpas para bowls', '8-12 meses',
     'Congélala el mismo día del corte y en porciones de un solo uso'),
    ('Caldos, cremas y salsas propias', '3 meses',
     'Etiquetar con fecha de producción Y de congelación: la vida útil de '
     'esta tabla se cuenta desde la de congelación'),
    ('Café en grano', 'No congelar',
     'Para uso diario no se congela: la condensación de abrir y cerrar la '
     'bolsa arruina el grano'),
]

HOJA_TRIMESTRAL = 'Trimestral y Anual'
TRIMESTRAL_TITULO = 'Mantenimiento Trimestral y Anual — Revisiones Contratadas'
#: El molde («Mantenimiento Mensual» de este kit) trae 4 bloques de 4/3/5/3
#: tareas. El reparto de abajo respeta esa medida exacta.
TRIMESTRAL = [
    ('  CONTRATADO — EMPRESA AUTORIZADA', [
        ('Control de plagas (DDD): visita de la empresa autorizada, parte '
         'firmado y certificado en vigor', 'Empresa DDD', 'Trimestral'),
        ('Limpieza de campana y conductos de extracción por empresa '
         'homologada', 'Empresa externa', 'Anual'),
        ('Revisión de extintores y BIE por empresa mantenedora (etiqueta y '
         'acta de revisión)', 'Mantenedor', 'Anual'),
        ('Prevención de legionela si hay torre de refrigeración o agua '
         'caliente sanitaria de riesgo', 'Empresa autorizada', 'Anual'),
    ]),
    ('  GAS, FRÍO Y RESIDUOS', [
        ('Revisión periódica de la instalación de gas por empresa habilitada, '
         'si el local tiene gas', 'Instalador gas', 'Cada 5 años'),
        ('Revisión de cámaras y vitrinas refrigeradas por frigorista: '
         'estanqueidad y gas refrigerante', 'Frigorista', 'Anual'),
        ('Retirada del aceite usado por gestor autorizado y archivo del '
         'documento de entrega, si hay freidora', 'Gestor autorizado',
         'Trimestral'),
    ]),
    ('  AGUA Y EQUIPOS DE CAFÉ', [
        ('Cambiar el filtro descalcificador de agua de la máquina de espresso '
         'y anotar la fecha del cambio', 'Técnico SAT', 'Trimestral'),
        ('Medir la dureza del agua (GH/KH) y ajustar el filtro: el agua es '
         'casi todo lo que hay en la taza', 'Barista', 'Trimestral'),
        ('Revisión técnica completa de la máquina de espresso por el SAT: '
         'juntas, presión y válvula de seguridad', 'Técnico SAT', 'Anual'),
        ('Revisar el desgaste de las muelas del molinillo por kilos molidos '
         '(orientativo: planas 400-600 kg, cónicas 800-1.200 kg) y '
         'cambiarlas si toca', 'Técnico SAT', 'Anual'),
        ('Calibrar los termómetros y las sondas contra un patrón conocido '
         '(agua con hielo, 0 °C)', 'Manager', 'Anual'),
    ]),
    ('  ADMINISTRACIÓN Y SEGUROS', [
        ('Revisar la póliza del local (continente, contenido y '
         'responsabilidad civil) y su fecha de vencimiento', 'Manager',
         'Anual'),
        ('Revisión del TPV y del software de facturación (requisitos '
         'antifraude / Verifactu)', 'Manager', 'Anual'),
        ('Anotar la fecha de la próxima revisión de cada contrato y archivar '
         'el parte firmado', 'Manager', 'Trimestral'),
    ]),
]


def _tabla_vida_util(ws, cambios):
    """Tabla editable de vidas útiles al pie de «FIFO Semanal».

    Va DEBAJO de la firma, fuera del rango del contador: es una referencia, no
    una tarea que haya que marcar.
    """
    if _fila(ws, TITULO_TABLA) is not None:
        return False
    firma = _exige_prefijo(ws, 'Firma encargado/a:')
    g = motor.geometria(ws)
    if not g:
        raise AnclaPerdida('«FIFO Semanal»: no es un checklist de la familia')
    banda_frescos = _exige(ws, '  FRESCOS')
    est_titulo = _estilos(ws, banda_frescos)
    est_cab = _estilos(ws, g['hr'])
    est_dato = _estilos(ws, banda_frescos + 1)
    n = 3 + len(TABLA_VIDA_UTIL)                  # blanca + título + cabecera
    idx = firma + 1
    motor.insertar_filas(ws, idx, n)
    fila = idx + 1
    _pintar(ws, fila, est_titulo)
    ws.cell(row=fila, column=1).value = TITULO_TABLA
    motor._merge(ws, f'A{fila}:{L(NCOL)}{fila}')
    fila += 1
    _pintar(ws, fila, est_cab)
    ws.cell(row=fila, column=2).value = 'Familia'
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
    cambios.append('«FIFO Semanal»: tabla editable de vida útil en '
                   f'congelación ({len(TABLA_VIDA_UTIL)} familias) — DOM-29 '
                   '(equivalente)')
    return True


def _hoja_trimestral(wb, cambios):
    """La capa de mantenimiento CONTRATADO, que no existía en este kit.

    «Mantenimiento Mensual» cubre equipos (espresso, molinillo, horno) pero no
    lo que se contrata y se pide en una inspección: DDD, conductos, extintores,
    gas, legionela, seguro y Verifactu.
    """
    if HOJA_TRIMESTRAL in wb.sheetnames:
        return False
    modelo = wb['Mantenimiento Mensual']
    ws = wb.copy_worksheet(modelo)
    ws.title = HOJA_TRIMESTRAL
    ws.cell(row=1, column=1).value = TRIMESTRAL_TITULO
    g = motor.geometria(ws)
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
            ws.cell(row=r, column=2).value = texto
            ws.cell(row=r, column=3).value = None      # lo escribe el cliente
            ws.cell(row=r, column=4).value = resp
            ws.cell(row=r, column=5).value = cad
    cambios.append(f'hoja nueva «{HOJA_TRIMESTRAL}»: mantenimiento contratado '
                   '(DDD, conductos, extintores y BIE, gas, legionela, filtro '
                   'de agua del espresso, seguro y Verifactu) con nº de parte '
                   'y firma — DOM-16 (equivalente)')
    return True


def _f05(wb, cambios):
    tocado = False
    # El molde de la hoja nueva es «Mantenimiento Mensual» TAL CUAL sale del
    # motor. En la 2.ª pasada la hoja ya existe y no se clona.
    if _hoja_trimestral(wb, cambios):
        tocado = True

    ws = wb['FIFO Semanal']
    if _sustituir(ws, 'Revisar pan: congelar lo que no se usará', VIDA_UTIL):
        cambios.append('«FIFO Semanal»: congelar el pan EN EL DÍA y con fecha, '
                       'remitiendo a la tabla de vida útil — DOM-29 '
                       '(equivalente)')
    if _tabla_vida_util(ws, cambios):
        tocado = True

    if _instrucciones(wb, 'Trimestral, anual y vida útil en congelación', [
            'La hoja «Trimestral y Anual» recoge el mantenimiento que se '
            'CONTRATA y que se pide en una inspección: DDD, conductos de '
            'extracción, extintores y BIE, instalación de gas, legionela, '
            'filtro de agua del espresso, seguro y facturación.',
            'Anota el número de parte en la columna verde y firma cuando la '
            'empresa haya venido; la última tarea de la hoja es apuntar la '
            'fecha de la próxima revisión.',
            'Al pie de «FIFO Semanal» tienes una tabla editable de vida útil '
            'en congelación por familia: una regla única para todo el '
            'congelador o tira producto bueno o valida producto pasado.']):
        cambios.append('Instrucciones: hoja trimestral/anual y tabla de vida '
                       'útil — DOM-16 / DOM-29 (equivalentes)')
    return tocado


# ==========================================================================
# 06 — eventos y festivos
# ==========================================================================
#: Hallazgo «alérgenos en eventos» (media) — las dos hojas que aceptan reservas
#: no recogían alérgenos ni intolerancias por escrito. En una cafetería de
#: brunch es el dato crítico: leches vegetales, gluten y frutos secos están en
#: casi todas las comandas.
ALERGENOS_SV = [
    ('Al confirmar cada reserva, recoger POR ESCRITO alérgenos e '
     'intolerancias y pasarlos a cocina y a barra (gluten, frutos secos, '
     'lactosa, huevo)', 'Office', 'Manager', 'Al confirmar'),
]
#: El valor de la columna de tiempo es «Al confirmar», no «Al reservar», y no es
#: cosmético: `motor.cadencia` vota la cabecera por el CONTENIDO de la columna y
#: «al confirmar» es de los literales que `RX_ANTELACION` reconoce. Con «Al
#: reservar» el voto se iba a «otro», la mayoría de «Antelación» se quedaba en
#: 4 de 9 y la cabecera de «San Valentín» degeneraba de «Antelación» a «Cuándo»
#: — una regresión de la v2.0 provocada por una tarea de contenido. Medido.
ALERGENOS_BRUNCH = [
    ('Al confirmar cada reserva, anotar POR ESCRITO alérgenos, intolerancias '
     'y número real de comensales, y pasarlo a cocina y a barra', 'Office',
     'Manager', 'Sábado'),
]

#: Equivalente de TEC-17 — la apertura de temporada no iba en orden: el permiso
#: municipal, lo único que puede impedir abrir la terraza, era la última tarea
#: del bloque y sin antelación propia.
TERRAZA = [
    ('Verificar el permiso/licencia de terraza vigente y renovarlo si caduca '
     'esta temporada', 'Office', 'Manager', '1 mes antes'),
    ('Sacar mobiliario de almacén / desembalar', 'Terraza', 'Auxiliar',
     'Primavera'),
    ('Verificar estado: tornillos, estabilidad, pintura', 'Terraza',
     'Manager', 'Primavera'),
    ('Limpiar todas las mesas y sillas a fondo', 'Terraza', 'Auxiliar',
     'Primavera'),
    ('Colocar sombrillas/toldos y verificar mecanismo', 'Terraza', 'Auxiliar',
     'Primavera'),
    ('Delimitar zona de terraza (vallas, maceteros)', 'Terraza', 'Manager',
     'Primavera'),
    ('Colocar macetas, plantas y decoración', 'Terraza', 'Camarero/a',
     'Primavera'),
]


def _f06(wb, cambios):
    tocado = False
    ws = wb['San Valentín']
    if _insertar_tras(ws, 'Publicar oferta en RRSS y aceptar reservas',
                      ALERGENOS_SV):
        cambios.append('«San Valentín»: alérgenos e intolerancias por escrito '
                       'al confirmar la reserva — DOM-19 (equivalente)')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Brunch Dominical']
    if _insertar_tras(ws, 'Confirmar reservas de brunch del domingo',
                      ALERGENOS_BRUNCH):
        cambios.append('«Brunch Dominical»: alérgenos, intolerancias y '
                       'comensales por escrito al confirmar — DOM-19 '
                       '(equivalente)')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Temporada Terraza']
    if _reordenar_bloque(ws, '  APERTURA DE TERRAZA (PRIMAVERA)', TERRAZA):
        cambios.append('«Temporada Terraza»: apertura en orden cronológico, '
                       'el permiso municipal primero y con 1 mes de '
                       'antelación — TEC-17 (equivalente)')
    return tocado


# ==========================================================================
# BONUS-02 — calendario anual
# ==========================================================================
#: Hallazgo «fechas del calendario» (baja) — faltaban las mismas cuatro que
#: identificó el representante (DOM-20), y el 1 de enero venía como servicio
#: dado por hecho cuando en una cafetería es una DECISIÓN.
ANO_NUEVO = ('Decidir si se abre; si se cierra, comunicarlo en Google '
             'Business Profile y en redes con 1 semana')
#: (texto de la fila DETRÁS de la que se inserta, mes, evento, tareas, antel.)
FECHAS = [
    ('Carnaval (variable)', 'Marzo', '19 Mar — Día del Padre',
     'Desayuno/brunch familiar, reservas ampliadas, detalle para el padre',
     '2 semanas'),
    ('Apertura terraza', 'Abril-Junio', 'Comuniones y bautizos (temporada)',
     'Menú de grupo cerrado, señal y precio por comensal, tartas por encargo',
     '1 mes'),
    ('Temporada alta', 'Agosto', '15 Ago — Asunción',
     'Servicio de festivo, refuerzo de turnos, terraza a pleno rendimiento',
     '1 semana'),
    # Detrás de Halloween, no de «Vuelta al cole»: el 1 de noviembre va DESPUÉS
    # del 31 de octubre y el calendario es cronológico.
    ('31 Oct — Halloween', 'Noviembre', '1 Nov — Todos los Santos',
     'Brunch familiar de mediodía, bollería de temporada (huesos de santo, '
     'panellets)', '1 semana'),
    ('Cierre terraza', 'Diciembre',
     '6-8 Dic — Puente de la Constitución y la Inmaculada',
     'Horario de festivo, refuerzo de mediodía, stock para tres días seguidos',
     '2 semanas'),
]


def _bonus02(wb, cambios):
    ws = wb['Calendario Anual']
    tocado = False
    fila_ano = _fila(ws, '1 Ene — Año Nuevo', 2)
    if fila_ano and ws.cell(row=fila_ano, column=3).value != ANO_NUEVO:
        ws.cell(row=fila_ano, column=3).value = ANO_NUEVO
        cambios.append('«Calendario Anual»: el 1 de enero pasa a ser una '
                       'DECISIÓN (abrir o no), no un servicio dado por hecho '
                       '— DOM-20 (equivalente)')
    nuevas = 0
    for ancla, mes, evento, tareas, antelacion in FECHAS:
        if _fila(ws, evento, 2) is not None:
            continue
        r = _exige(ws, ancla, 2)
        est = _estilos(ws, r)
        motor.insertar_filas(ws, r + 1, 1)
        _pintar(ws, r + 1, est)
        for c, v in enumerate((mes, evento, tareas, antelacion), start=1):
            ws.cell(row=r + 1, column=c).value = v
        nuevas += 1
        tocado = True
    if nuevas:
        cambios.append(f'«Calendario Anual»: {nuevas} fechas que faltaban '
                       '(Día del Padre, comuniones, 15-Ago, Todos los Santos, '
                       'puente de diciembre) — DOM-20 (equivalente)')
    return tocado


# ==========================================================================
# API
# ==========================================================================
FICHEROS = {
    '01-apertura-cierre.xlsx': _f01,
    '02-partidas-cocina.xlsx': _f02,
    '03-tareas-manager.xlsx': _f03,
    '05-tareas-semanales-mensuales.xlsx': _f05,
    '06-eventos-festivos.xlsx': _f06,
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
