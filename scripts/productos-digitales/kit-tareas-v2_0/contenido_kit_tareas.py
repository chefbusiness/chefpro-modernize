#!/usr/bin/env python3
"""
contenido_kit_tareas.py — §3 de `kit-tareas-v2-SPEC.md`: los cambios de
CONTENIDO propios del kit base (`kit-tareas`, el representante de la familia).

NO es de familia. `main.py` lo carga sólo cuando `--producto kit-tareas`
(el nombre del módulo se compone con el pid), así que aquí se puede hablar de
«Apertura Cocina» o de «FIFO Semanal» por su nombre: son hojas de ESTE kit.
Lo estructural —contador, filas libres, DV, verdes, protección, impresión,
Instrucciones, metadata— es del `motor`, y este módulo no lo duplica: inserta
las filas con `motor.insertar_filas` (que desplaza merges, DV y fórmulas) y
deja que el motor vuelva a medir.

Contrato con `main.py`:
    post(wb, fname, cambios) -> bool
El `True` significa «he cambiado la ESTRUCTURA de este libro» (filas nuevas u
hoja nueva) y hace que `main.py` vuelva a pasar `motor.aplicar` sobre el libro
antes de `motor.cerrar`. Es lo que garantiza que:
  · las filas nuevas entren en el rango del contador, en la DV y en el CF;
  · el cuerpo desbloqueado que recibe `proteger` sea el de DESPUÉS de insertar
    (con el cuerpo viejo, las últimas filas se publicaban bloqueadas);
  · la hoja nueva «Trimestral y Anual» sea una hoja de la familia y no una
    isla sin DV, sin contador, sin A4 y sin protección.

ANCLAS, NO NÚMEROS DE FILA. Todo se localiza por el TEXTO de la celda, porque
este módulo corre DESPUÉS de `motor.aplicar`, que ya ha insertado filas libres,
colapsado bloques duplicados y reescrito los textos de temperatura. Si un ancla
no aparece, se levanta `AnclaPerdida`: es preferible que el dry-run se caiga a
publicar un kit con la mitad del contenido aplicado.

IDEMPOTENCIA. Cada operación mira primero si su resultado ya está en el libro
(el texto nuevo, el rótulo del bloque, el título de la tabla, la hoja). La 2.ª
pasada de `main.py` no debe encontrar nada que hacer.

Dos trampas del motor que condicionan la redacción de los textos:
  · `motor.texto_temperatura` añade objetivo y «— anota la lectura: ____ °C» a
    toda tarea con verbo de registro + «temperatura» + equipo de frío. Los
    textos que escribimos aquí y encajan en ese patrón YA traen la coletilla,
    porque si no la 2.ª pasada se la añadiría y el gate de idempotencia
    cazaría la diferencia.
  · `motor.texto_appcc` añade «(si tienes el Pack APPCC…)» a toda celda con la
    palabra APPCC. Por eso ningún texto de este módulo la menciona.
Y una del contexto: `motor.contexto` saca la hora ancla del kit de la hora MÁS
TEMPRANA de las hojas de apertura. Ninguna tarea nueva puede llevar una hora
anterior a las 07:00 o el ancla se movería entre pasadas y con ella toda la
precarga del 08.
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
    # aplicar a la hoja (DOM-R2-22): este módulo corre después, así que buscar
    # «< 8°C» tal como está escrito aquí ya no encuentra nada — el motor lo ha
    # dejado en «< 8 °C» y `_exige` reventaría el dry-run entero.
    texto = motor.texto_grados(texto)
    for r in range(1, ws.max_row + 1):
        if motor.texto_grados(ws.cell(row=r, column=col).value) == texto:
            return r
    return None


def _exige(ws, texto, col=1):
    r = _fila(ws, texto, col)
    if r is None:
        raise AnclaPerdida(f'«{ws.title}»: no encuentro '
                           f'{L(col)}=«{texto}» (§3 de la SPEC)')
    return r


def _estilos(ws, fila):
    return [copy.copy(ws.cell(row=fila, column=c)._style)
            for c in range(1, NCOL + 1)]


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

    No mueve filas: reescribe valores, que es lo único que cambia de sitio.
    Así no hay que tocar merges, DV ni el rango del contador.
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
    """Bloque nuevo (banda + tareas + fila separadora) delante de otra banda."""
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


def _bloque_final(ws, titulo, tareas):
    """Bloque nuevo detrás del último bloque, ANTES de las filas libres."""
    if _fila(ws, titulo) is not None:
        return False
    g = motor.geometria(ws)
    if not g:
        raise AnclaPerdida(f'«{ws.title}»: no es un checklist de la familia')
    banda = max(r for r in range(g['hr'] + 1, g['ultima'])
                if motor.es_fila_seccion(ws, r))
    est_banda = _estilos(ws, banda)
    est_tarea = _estilos(ws, g['ultima'])
    blanca = _fila_blanca(ws, banda + 1)
    est_blanca = _estilos(ws, blanca) if blanca else [None] * NCOL
    idx = g['ultima'] + 1
    n = len(tareas) + 2
    motor.insertar_filas(ws, idx, n)
    if blanca:
        _pintar(ws, idx, est_blanca)
    _pintar(ws, idx + 1, est_banda)
    ws.cell(row=idx + 1, column=1).value = titulo
    motor._merge(ws, f'A{idx + 1}:{L(NCOL)}{idx + 1}')
    for i, t in enumerate(tareas):
        _pintar(ws, idx + 2 + i, est_tarea)
        _escribir_tarea(ws, idx + 2 + i, t)
    return True


def _intercambiar(ws, texto_a, texto_b):
    """Intercambia dos filas de tarea completas (B..NCOL) por su texto.

    DOM-R2-27 — dentro de un bloque, la única función del orden es marcar la
    secuencia, y la tarea 10 vencía antes que la 9 (11:45 y luego 11:30).
    Idempotente: si `texto_a` ya va por debajo de `texto_b`, no hace nada.
    """
    ra, rb = _fila(ws, texto_a, 2), _fila(ws, texto_b, 2)
    if ra is None or rb is None or ra > rb:
        return False
    for c in range(2, NCOL + 1):
        va = ws.cell(row=ra, column=c).value
        ws.cell(row=ra, column=c).value = ws.cell(row=rb, column=c).value
        ws.cell(row=rb, column=c).value = va
    return True


def _columna_de_bloque(ws, banda, col, valor):
    """Escribe `valor` en `col` para todas las tareas de un bloque."""
    _, filas = _filas_de_bloque(ws, banda)
    n = 0
    for r in filas:
        if ws.cell(row=r, column=col).value != valor:
            ws.cell(row=r, column=col).value = valor
            n += 1
    return n


def _instrucciones(wb, encabezado, lineas):
    """Añade un bloque al final de la hoja «Instrucciones».

    `motor.reescribir_instrucciones` (que corre DESPUÉS, en `cerrar`) relee la
    hoja línea a línea y la vuelve a emitir en el molde ▸, así que lo que se
    escriba aquí en crudo acaba maquetado como un bloque más. El encabezado no
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
     'manipula alimentos', 'Cocina', 'Jefe de Cocina', '07:00'),
]

#: DOM-13 — el orden IMPRESO era el inseguro (gas y fuego antes que la
#: extracción). DOM-24 — la primera tarea del producto daba por hecho que las
#: cámaras se apagan por la noche. Se reescribe el bloque entero en el orden
#: en que se hace de verdad, sin mover filas.
ENCENDIDO = [
    ('Encender la campana extractora y ventilar la cocina ANTES de encender '
     'nada más', 'Cocina', 'Cocinero apertura', '07:00'),
    # DOM-R2-19 — la prueba de fugas con agua jabonosa es MANTENIMIENTO (vive
    # en «Trimestral y Anual», revisión por empresa habilitada), no algo que un
    # cocinero haga cada mañana antes de encender: en la práctica nadie la hace
    # y la casilla se marca igual, que es la forma más rápida de que el equipo
    # deje de creerse el resto de la lista.
    ('Abrir la llave general de gas y comprobar que NO huele a gas; si huele, '
     'no enciendas nada, ventila y avisa al mantenedor',
     'Cocina', 'Cocinero apertura', '07:00'),
    ('Encender hornos y precalentar a temperatura de trabajo', 'Cocina',
     'Cocinero apertura', '07:15'),
    ('Encender planchas, freidoras y salamandra', 'Cocina',
     'Cocinero apertura', '07:15'),
    ('Encender lavavajillas y verificar nivel de producto', 'Cocina',
     'Auxiliar cocina', '07:15'),
    ('Comprobar que las cámaras han funcionado toda la noche y registrar '
     'temperatura (refrigeración 0-4 °C / congelación ≤ −18 °C) — anota la '
     'lectura: ____ °C. Si hay desviación, no uses el género hasta valorarlo',
     'Cocina', 'Cocinero apertura', '07:00'),
]

MERMAS_COCINA = [
    ('Anotar las mermas del día (producto, cantidad y motivo): sin este dato '
     'el food cost mensual sale mal', 'Cocina', 'Sous Chef', 'Cierre'),
]

CALEFACTORES = ('Verificar calefactores exteriores si la terraza opera en '
                'temporada fría')


def _f01(wb, cambios):
    tocado = False
    ws = wb['Apertura Cocina']
    if _insertar_bloque(ws, '  ENCENDIDO DE EQUIPOS', '  HIGIENE PERSONAL',
                        HIGIENE):
        cambios.append('«Apertura Cocina»: bloque «HIGIENE PERSONAL» al '
                       f'inicio ({len(HIGIENE)} tareas) — DOM-12')
        tocado = True
    if _reordenar_bloque(ws, '  ENCENDIDO DE EQUIPOS', ENCENDIDO):
        cambios.append('«Apertura Cocina»: «ENCENDIDO DE EQUIPOS» en orden '
                       'seguro (campana → gas → fuego) y las cámaras dejan de '
                       '«encenderse» — DOM-13 / DOM-24')
    motor.renumerar(ws)

    ws = wb['Apertura Sala']
    if _sustituir(ws, 'Verificar calefactores exteriores (invierno)',
                  CALEFACTORES):
        cambios.append('«Apertura Sala»: calefactores condicionados a que la '
                       'terraza opere en frío — COM-26')

    ws = wb['Cierre Cocina']
    if _insertar_tras(ws, 'Retirar producto caducado o deteriorado',
                      MERMAS_COCINA):
        cambios.append('«Cierre Cocina»: tarea de mermas del día — DOM-18')
        tocado = True
    motor.renumerar(ws)
    return tocado


# ==========================================================================
# 02 — partidas de cocina
# ==========================================================================
ANISAKIS_FRIOS = [
    ('Pescado para consumo crudo o semicrudo (tartar, ceviche, carpaccio) — '
     'prevención de ANISAKIS: confirmar congelación previa ≥24 h a −20 °C '
     '(o −35 °C 15 h) y anotar el lote', 'Cocina', 'Chef partida', '11:00'),
]
ANISAKIS_MEP = [
    # COM-R2-12 — la tarea estaba bien redactada pero la palabra que el chef y
    # el inspector tienen en la cabeza («anisakis») no aparecía en NINGÚN
    # fichero del kit, mientras el changelog la anunciaba: quien la buscase con
    # Ctrl+F concluía que el cambio no se había aplicado.
    ('Pescado y marisco para consumo crudo o semicrudo — prevención de '
     'ANISAKIS: confirmar congelación previa ≥24 h a −20 °C (o −35 °C 15 h) y '
     'anotar el lote', 'Cocina', 'Chef partida', '11:00'),
]
#: DOM-R2-14 — la primera redacción se comió el SUJETO («Lavar ... qué»), y en
#: la partida de fríos es la tarea con más riesgo del turno: un ayudante nuevo
#: puede entenderlo como las superficies o los trapos.
LECHUGAS = ('Lavar y desinfectar hojas verdes y vegetales de consumo crudo con '
            'lejía apta para uso alimentario según la dosis del fabricante '
            '(habitual: 70 ppm, 5 min) y ACLARAR con agua potable abundante')
EXPOSICION = ('Mantener la exposición a ≤ 4 °C para crudos de pescado y '
              'marisco; < 8 °C para vegetales y ensaladas')
ACEITE = ('Apagar la freidora al terminar y filtrar el aceite SÓLO por debajo '
          'de 40 °C, nunca en caliente, con guantes y recipiente estable; el '
          'aceite usado, al bidón del gestor autorizado')
#: DOM-R2-28 — §2.9 sólo tocó las tareas que empiezan por «Registrar
#: temperatura». Ésta se quedó sin objetivo ni hueco de lectura, y es la única
#: medición del kit que se toma DURANTE el servicio: justo la que un inspector
#: pide para el mantenimiento en caliente.
MANTENIMIENTO_CALIENTE = ('Control de temperatura de mantenimiento en caliente '
                          '(≥ 65 °C) — anota la lectura: ____ °C')
MERMAS_CALIENTES = [
    ('Anotar las mermas del turno (producto, cantidad y motivo)', 'Cocina',
     'Chef partida', 'Cierre'),
]


def _f02(wb, cambios):
    tocado = False
    ws = wb['Fríos']
    if _sustituir(ws, 'Lavar y desinfectar lechugas y vegetales', LECHUGAS):
        cambios.append('«Fríos»: desinfección de vegetales con dosis y '
                       'aclarado — DOM-26')
    if _sustituir(ws, 'Mantener temperatura de exposición < 8°C', EXPOSICION):
        cambios.append('«Fríos»: exposición de crudos a ≤ 4 °C — DOM-02')
    # Va DELANTE de «Porcionar carpaccios, ceviches, tartares»: la
    # comprobación no sirve de nada después de haber porcionado.
    if _insertar_tras(ws, 'Preparar bases de ensalada', ANISAKIS_FRIOS):
        cambios.append('«Fríos»: tarea de congelación preventiva frente al '
                       'anisakis (RD 1021/2022, art. 8.1, que derogó el '
                       'RD 1420/2006) — DOM-02')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Mise en Place']
    if _insertar_tras(ws, 'Marisco: limpio, desvenado si aplica',
                      ANISAKIS_MEP):
        cambios.append('«Mise en Place»: tarea de congelación preventiva '
                       'frente al anisakis — DOM-02')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Calientes']
    if _sustituir(ws, 'Control de temperatura de mantenimiento (>65 °C)',
                  MANTENIMIENTO_CALIENTE):
        cambios.append('«Calientes»: la temperatura de mantenimiento en '
                       'caliente lleva objetivo y hueco de lectura — DOM-R2-28')
    if _sustituir(ws, 'Filtrar y/o cambiar aceite de freidora', ACEITE):
        cambios.append('«Calientes»: el aceite se filtra en frío y se entrega '
                       'a gestor autorizado — DOM-27 / DOM-18')
    if _insertar_tras(ws, 'Limpiar mesa de pase', MERMAS_CALIENTES):
        cambios.append('«Calientes»: tarea de mermas del turno — DOM-18')
        tocado = True
    motor.renumerar(ws)
    return tocado


# ==========================================================================
# 03 — manager
# ==========================================================================
JORNADA_DIARIA = [
    ('Cerrar y validar el registro diario de jornada del equipo (entradas, '
     'salidas y pausas)', 'Admin', 'Manager', 'Cierre'),
]
JORNADA_MENSUAL = [
    ('Archivar los registros de jornada del mes (hay que conservarlos 4 años)',
     'Admin', 'Manager', 'Mensual'),
]
#: DOM-28 — los bloques se llamaban LUNES…VIERNES y el lunes es el día de
#: cierre más habitual en la hostelería española: quien cierre los lunes se
#: quedaba con cinco tareas huérfanas. Pasan a ser DÍA 1…DÍA 5 (el orden de la
#: semana, no el día del calendario) y el día real vive en la columna «Día»,
#: que es verde y editable.
DIAS_MANAGER = [
    ('  LUNES — PLANIFICACIÓN', '  DÍA 1 — PLANIFICACIÓN'),
    ('  MARTES — PROVEEDORES', '  DÍA 2 — PROVEEDORES'),
    ('  MIÉRCOLES — EQUIPO', '  DÍA 3 — EQUIPO'),
    ('  JUEVES — CALIDAD', '  DÍA 4 — CALIDAD'),
    ('  VIERNES — MARKETING Y ADMIN', '  DÍA 5 — MARKETING Y ADMIN'),
]
FIN_DE_SEMANA = [
    ('Control de tiempos de espera en los picos de mediodía y de noche',
     'Sala', 'Manager', 'Sábado'),
    ('Reposición entre servicios: barra, bodega y mise en place de la noche',
     'General', 'Encargado', 'Sábado'),
    ('Cerrar las reservas del domingo y confirmar por teléfono los grupos',
     'Admin', 'Manager', 'Sábado'),
    ('Recuento del producto crítico para el lunes y pedido de urgencia si '
     'falta', 'Cocina', 'Sous Chef', 'Domingo'),
]


def _f03(wb, cambios):
    tocado = False
    ws = wb['Diario Manager']
    if _intercambiar(ws, 'Briefing pre-servicio con equipo de sala',
                     'Revisar redes sociales: comentarios, reseñas nuevas'):
        cambios.append('«Diario Manager»: el briefing (11:45) baja al final '
                       'del bloque PRE-SERVICIO, detrás de la tarea de las '
                       '11:30 — DOM-R2-27')
    if _insertar_tras(ws, 'Registrar ventas totales', JORNADA_DIARIA):
        cambios.append('«Diario Manager»: registro diario de jornada '
                       '(obligatorio desde 2019) — DOM-17')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Mensual Manager']
    if _insertar_tras(ws, 'Revisar cumplimiento de horarios del mes',
                      JORNADA_MENSUAL):
        cambios.append('«Mensual Manager»: archivo de los registros de '
                       'jornada del mes — DOM-17')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Semanal Manager']
    n = sum(1 for viejo, nuevo in DIAS_MANAGER
            if _sustituir(ws, viejo, nuevo, col=1))
    if n:
        cambios.append(f'«Semanal Manager»: {n} bloques por FUNCIÓN (DÍA 1…5) '
                       'en vez de por día de la semana — DOM-28')
    # DOM-R2-11 — las Instrucciones explican que los bloques NO van por día del
    # calendario «porque muchos restaurantes cierran el lunes», y la columna
    # «Día» venía precargada con Lunes…Viernes: el problema que la nota dice
    # haber resuelto seguía impreso en la hoja. La columna pasa a llevar la
    # etiqueta del bloque; el día real lo escribe el cliente encima (es verde).
    g = motor.geometria(ws)
    col_dia = motor._col_tiempo(g['cols']) if g else None
    if col_dia:
        m = sum(_columna_de_bloque(ws, banda, col_dia,
                                   banda.strip().split(' — ')[0].capitalize())
                for _, banda in DIAS_MANAGER)
        if m:
            cambios.append(f'«Semanal Manager»: la columna «Día» deja de '
                           f'anclar {m} tareas a Lunes-Viernes y lleva la '
                           'etiqueta del bloque (Día 1…Día 5) — DOM-R2-11')
    if _bloque_final(ws, '  FIN DE SEMANA', FIN_DE_SEMANA):
        cambios.append('«Semanal Manager»: bloque «FIN DE SEMANA» '
                       f'({len(FIN_DE_SEMANA)} tareas) — DOM-28')
        tocado = True
    motor.renumerar(ws)

    if _instrucciones(wb, 'La semana va por DÍAS 1-5, no por lunes-viernes', [
            'Los bloques de «Semanal Manager» están numerados por orden de la '
            'semana, no por día del calendario: muchos restaurantes cierran '
            'el lunes y ese bloque se quedaba huérfano.',
            'La columna «Día» viene con Día 1…Día 5 (el orden de TU semana, '
            'no el del calendario): escribe encima el día real de tu local, '
            'es una celda verde. El bloque «FIN DE SEMANA» es el de sábado y '
            'domingo, que es cuando se factura la mitad de la semana.']):
        cambios.append('Instrucciones: cómo leer los DÍA 1-5 — DOM-28')
    return tocado


# ==========================================================================
# 05 — semanales, mensuales y (nuevo) trimestral/anual
# ==========================================================================
BACKFLUSH = ('Limpieza química del grupo con detergente (backflush) + remojo '
             'de portafiltros, filtros y duchas')
LAVAVAJILLAS = 'Limpiar filtros, brazos de lavado y cuba del lavavajillas'
DESCALCIFICAR = [
    ('Descalcificar el lavavajillas (frecuencia según la dureza del agua: '
     'mensual o trimestral)', 'Cocina', 'Técnico/Chef', 'Mensual'),
]
#: DOM-R2-29 — con cadencia «Trimestral» dentro de la hoja MENSUAL, teniendo el
#: fichero una hoja «Trimestral y Anual» creada en esta misma v2.0. Quien
#: imprima la mensual se llevaba una tarea que no toca ese mes. Va al bloque
#: ADMINISTRACIÓN Y EQUIPOS de la trimestral, que es donde la buscará.
DESCALCIFICAR_CAFE = [
    ('Descalcificar la máquina de café y revisar el descalcificador o las '
     'resinas (según la dureza del agua)', None, 'Técnico', 'Trimestral'),
]
VIDA_UTIL = ('Comprobar que ningún producto supera su vida útil de '
             'congelación (ver la tabla al pie de esta hoja)')
TITULO_TABLA = ('VIDA ÚTIL ORIENTATIVA EN CONGELACIÓN A −18 °C — ajústala a '
                'tu producto y a tu proveedor')
TABLA_VIDA_UTIL = [
    ('Pescado azul y marisco', '2-3 meses', 'La grasa se enrancia aunque esté '
     'congelado: es el que antes se estropea'),
    ('Pescado blanco', '4-6 meses', 'Entero aguanta menos que en porciones ya '
     'limpias y envasadas'),
    ('Carne de vacuno y caza', '8-12 meses', 'Piezas enteras; en filetes, la '
     'mitad'),
    ('Carne de cerdo y cordero', '4-6 meses', 'La grasa de cerdo limita la '
     'vida útil'),
    ('Aves y conejo', '6-9 meses', 'Enteros; troceados, 6 meses'),
    ('Carne picada, hamburguesas y elaborados', '2-3 meses', 'Mucha '
     'superficie expuesta: la más delicada'),
    ('Pan, masas y bollería', '1-3 meses', 'Pierde textura antes que '
     'seguridad'),
    ('Verdura escaldada y fruta', '8-12 meses', 'Sin escaldar previamente, '
     'la mitad'),
    # DOM-R2-10 — decía «fecha de producción, NO de congelación» catorce filas
    # debajo de la tarea «Verificar etiquetado y fechas de congelación», y la
    # vida útil de esta misma tabla se cuenta desde que el producto entra al
    # congelador: obedecer la nota dejaba la tabla inaplicable.
    ('Fondos, salsas y caldos propios', '3 meses', 'Etiquetar con fecha de '
     'producción Y de congelación: la vida útil de esta tabla se cuenta desde '
     'la de congelación'),
]

HOJA_TRIMESTRAL = 'Trimestral y Anual'
TRIMESTRAL_TITULO = 'Mantenimiento Trimestral y Anual — Revisiones Contratadas'
TRIMESTRAL = [
    ('  CONTRATADO — EMPRESA AUTORIZADA', [
        ('Control de plagas (DDD): visita de la empresa autorizada, parte '
         'firmado y certificado en vigor', 'Empresa DDD', 'Trimestral'),
        ('Limpieza de campana y conductos de extracción por empresa '
         'homologada', 'Empresa externa', 'Anual'),
        ('Revisión de extintores y BIE por empresa mantenedora (etiqueta y '
         'acta de revisión)', 'Mantenedor', 'Anual'),
        ('Retimbrado de extintores: prueba de presión cada 5 años desde su '
         'fabricación', 'Mantenedor', 'Cada 5 años'),
        ('Revisión periódica de la instalación de gas por empresa habilitada',
         'Instalador gas', 'Cada 5 años'),
        ('Revisión de los equipos de frío por frigorista (estanqueidad y gas '
         'refrigerante)', 'Frigorista', 'Anual'),
    ]),
    ('  AGUA, RESIDUOS Y ANALÍTICAS', [
        ('Prevención de legionela si hay torre de refrigeración, spa o agua '
         'caliente de riesgo', 'Empresa autorizada', 'Anual'),
        ('Analítica del agua de consumo si el local tiene depósito o captación '
         'propia', 'Laboratorio', 'Anual'),
        ('Retirada de aceite usado por gestor autorizado: archivar los '
         'documentos de entrega', 'Gestor autorizado', 'Trimestral'),
        ('Revisar el contrato de residuos y el acceso al punto limpio',
         'Manager', 'Anual'),
    ]),
    ('  ADMINISTRACIÓN Y EQUIPOS', [
        ('Revisar la póliza del local (continente, contenido y '
         'responsabilidad civil) y su vencimiento', 'Manager', 'Anual'),
        ('Revisión del TPV y del software de facturación (requisitos '
         'antifraude / Verifactu)', 'Manager', 'Anual'),
        ('Calibrar los termómetros y las sondas contra un patrón conocido',
         'Técnico', 'Anual'),
        ('Anotar la fecha de la próxima revisión de cada contrato y archivar '
         'el parte firmado', 'Manager', 'Trimestral'),
    ]),
]


def _tabla_vida_util(ws, cambios):
    """DOM-29 — tabla editable de vidas útiles al pie de «FIFO Semanal»."""
    if _fila(ws, TITULO_TABLA) is not None:
        return False
    firma = _exige(ws, 'Verificado por:')
    est_titulo = _estilos(ws, _exige(ws, '  CONGELADOR'))
    est_cab = _estilos(ws, motor.geometria(ws)['hr'])
    est_dato = _estilos(ws, motor.geometria(ws)['hr'] + 1)
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
    cambios.append(f'«FIFO Semanal»: tabla editable de vida útil en '
                   f'congelación ({len(TABLA_VIDA_UTIL)} familias) — DOM-29')
    return True


def _hoja_trimestral(wb, cambios):
    """DOM-16 — la capa de mantenimiento CONTRATADO, que no existía."""
    if HOJA_TRIMESTRAL in wb.sheetnames:
        return False
    modelo = wb['Mantenimiento Mensual']
    ws = wb.copy_worksheet(modelo)
    ws.title = HOJA_TRIMESTRAL
    ws.cell(row=1, column=1).value = TRIMESTRAL_TITULO
    g = motor.geometria(ws)
    ws.cell(row=g['hr'], column=3).value = 'Nº de parte'
    bandas = [r for r in range(g['hr'] + 1, g['contador'] or ws.max_row)
              if motor.es_fila_seccion(ws, r)]
    if len(bandas) != len(TRIMESTRAL):
        raise AnclaPerdida(f'«{modelo.title}» tiene {len(bandas)} bloques y el '
                           f'molde de «{HOJA_TRIMESTRAL}» espera '
                           f'{len(TRIMESTRAL)}')
    for banda, (titulo, tareas) in zip(bandas, TRIMESTRAL):
        ws.cell(row=banda, column=1).value = titulo
        filas = []
        for r in range(banda + 1, g['contador'] or ws.max_row):
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
                   '(DDD, conductos, extintores y BIE, gas, legionela, '
                   'seguro, Verifactu) con nº de parte y firma — DOM-16')
    return True


def _f05(wb, cambios):
    tocado = False
    ws = wb['Limpieza Semanal']
    if _sustituir(ws, 'Descalcificar lavavajillas', LAVAVAJILLAS):
        cambios.append('«Limpieza Semanal»: lo semanal del lavavajillas son '
                       'filtros y brazos, no descalcificar — DOM-15')
    if _sustituir(ws, 'Descalcificar máquina de café', BACKFLUSH):
        cambios.append('«Limpieza Semanal»: lo semanal de la cafetera es el '
                       'backflush, no descalcificar — DOM-15')

    # El molde de la hoja nueva es «Mantenimiento Mensual» TAL CUAL sale del
    # motor (bloques de 6/4/4 tareas), así que se clona ANTES de meterle los
    # dos descalcificados. En la 2.ª pasada la hoja ya existe y no se clona.
    if _hoja_trimestral(wb, cambios):
        tocado = True

    ws = wb['Mantenimiento Mensual']
    if _insertar_tras(ws, 'Verificar juntas de puertas de cámaras',
                      DESCALCIFICAR):
        cambios.append('«Mantenimiento Mensual»: descalcificado del '
                       'lavavajillas (aquí sí) — DOM-15')
        tocado = True
    motor.renumerar(ws)

    ws = wb[HOJA_TRIMESTRAL]
    if _insertar_tras(ws, 'Revisión del TPV y del software de facturación '
                          '(requisitos antifraude / Verifactu)',
                      DESCALCIFICAR_CAFE):
        cambios.append(f'«{HOJA_TRIMESTRAL}»: el descalcificado de la máquina '
                       'de café pasa de la hoja mensual a la trimestral, que '
                       'es su frecuencia real — DOM-R2-29')
        tocado = True
    motor.renumerar(ws)

    ws = wb['FIFO Semanal']
    if _sustituir(ws, 'Comprobar que no hay producto > 3 meses congelado',
                  VIDA_UTIL):
        cambios.append('«FIFO Semanal»: la regla plana de 3 meses pasa a ser '
                       'la vida útil por familia — DOM-29')
    if _tabla_vida_util(ws, cambios):
        tocado = True

    if _instrucciones(wb, 'Trimestral, anual y vida útil en congelación', [
            'La hoja «Trimestral y Anual» recoge el mantenimiento que se '
            'CONTRATA y que se pide en una inspección: DDD, conductos de '
            'extracción, extintores y BIE, instalación de gas, legionela, '
            'seguro y facturación.',
            'Anota el número de parte en la columna verde y firma cuando la '
            'empresa haya venido; la última tarea de la hoja es apuntar la '
            'fecha de la próxima revisión.',
            'Al pie de «FIFO Semanal» tienes una tabla editable de vida útil '
            'en congelación por familia: una regla única para todo el '
            'congelador o tira producto bueno o valida producto pasado.']):
        cambios.append('Instrucciones: hoja trimestral/anual y tabla de vida '
                       'útil — DOM-16 / DOM-29')
    return tocado


# ==========================================================================
# 06 — eventos y festivos
# ==========================================================================
TITULO_PRE = 'Checklist Pre-Evento (de la reserva al día del evento)'
RESERVA = [
    ('Recoger POR ESCRITO alérgenos, intolerancias y dietas especiales de los '
     'comensales y trasladarlos a cocina', 'Admin', 'Manager',
     'Al confirmar'),
    ('Cerrar por escrito el precio por comensal y qué incluye (bebida, café, '
     'tarta, extras)', 'Admin', 'Manager', 'Al confirmar'),
    ('Cobrar la señal o anticipo y dejar constancia del importe y la fecha',
     'Admin', 'Manager', 'Al confirmar'),
    ('Firmar la política de cancelación y el plazo para dar el número final '
     'de comensales', 'Admin', 'Manager', 'Al confirmar'),
    ('Acordar horario de entrada y salida del espacio y quién monta y '
     'desmonta', 'Admin', 'Manager', 'Al confirmar'),
]
#: TEC-17 — el bloque no iba de mayor a menor antelación y la licencia
#: municipal, la única con riesgo administrativo, quedaba la cuarta.
TERRAZA = [
    ('Solicitar licencia de terraza al Ayuntamiento si aplica', 'Terraza',
     'Manager', '1 mes antes'),
    ('Verificar estado de mesas y sillas: reparar/sustituir', 'Terraza',
     'Manager', '1 semana antes'),
    ('Verificar toldo/sombrilla: estado y funcionamiento', 'Terraza',
     'Manager', '1 semana antes'),
    ('Preparar carta de terraza si es diferente', 'Terraza', 'Jefe Cocina',
     '1 semana antes'),
    ('Limpiar a fondo todo el mobiliario de terraza', 'Terraza', 'Camareros',
     'Día apertura'),
    ('Verificar iluminación exterior', 'Terraza', 'Manager', 'Día apertura'),
]
DESMONTAR = ('Desmontar y guardar los calefactores exteriores si la terraza '
             'no opera en invierno')


def _f06(wb, cambios):
    tocado = False
    ws = wb['Pre-Evento']
    if ws.cell(row=1, column=1).value != TITULO_PRE:
        ws.cell(row=1, column=1).value = TITULO_PRE
        cambios.append('«Pre-Evento»: el título ya no promete 48 h cuando la '
                       'hoja arranca al confirmar la reserva — DOM-19')
    if _insertar_bloque(ws, '  48 HORAS ANTES', '  AL CONFIRMAR LA RESERVA',
                        RESERVA):
        cambios.append('«Pre-Evento»: bloque «AL CONFIRMAR LA RESERVA» '
                       '(alérgenos por escrito, señal, precio por comensal, '
                       'cancelación) — DOM-19')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Temporada Terraza']
    if _reordenar_bloque(ws, '  APERTURA DE TEMPORADA', TERRAZA):
        cambios.append('«Temporada Terraza»: apertura en orden cronológico, '
                       'la licencia municipal primero — TEC-17')
    if _sustituir(ws, 'Desmontar calefactores exteriores si aplica',
                  DESMONTAR):
        cambios.append('«Temporada Terraza»: el desmontaje de calefactores '
                       'deja de contradecir la apertura diaria — COM-26')

    ws = wb['Navidad']
    if _sustituir(ws, '  2 SEMANAS ANTES', '  2-3 SEMANAS ANTES', col=1):
        cambios.append('«Navidad»: el rótulo de la sección coincide con los '
                       'plazos de sus tareas (15 y 10 días) — TEC-22')
    return tocado


# ==========================================================================
# BONUS-02 — calendario anual
# ==========================================================================
ANO_NUEVO = ('Decidir si se abre; si se cierra, comunicarlo en Google '
             'Business Profile y en redes con 1 semana')
#: (texto de la fila DETRÁS de la que se inserta, mes, evento, tareas, antel.)
FECHAS = [
    ('Carnaval (variable)', 'Marzo', '19 Mar — Día del Padre',
     'Menú familiar de mediodía, reservas ampliadas, detalle para el padre',
     '2 semanas'),
    ('Apertura terraza', 'Abril-Junio', 'Comuniones y bautizos (temporada)',
     'Menú de grupo cerrado, señal y precio por comensal, sala privada',
     '1 mes'),
    ('Temporada alta', 'Agosto', '15 Ago — Asunción',
     'Servicio de festivo, refuerzo de turnos, terraza a pleno rendimiento',
     '1 semana'),
    # Detrás de Halloween, no de «Vuelta al cole»: el 1 de noviembre va
    # DESPUÉS del 31 de octubre y el calendario es cronológico.
    ('31 Oct — Halloween', 'Noviembre', '1 Nov — Todos los Santos',
     'Comida familiar de mediodía, menú de temporada (setas, castañas)',
     '1 semana'),
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
                       '— DOM-20')
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
                       'puente de diciembre) — DOM-20')
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
    """§3 sobre un libro ya normalizado por `motor.aplicar`.

    Devuelve True si ha cambiado la ESTRUCTURA (filas u hojas nuevas), que es
    la señal para que `main.py` vuelva a pasar el motor antes de cerrar.
    """
    fn = FICHEROS.get(fname)
    if fn is None:
        return False
    return bool(fn(wb, cambios))
