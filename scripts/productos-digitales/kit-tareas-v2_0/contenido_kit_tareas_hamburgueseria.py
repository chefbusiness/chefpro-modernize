#!/usr/bin/env python3
"""
contenido_kit_tareas_hamburgueseria.py — §3 de `kit-tareas-v2-SPEC.md` aplicado
al hermano `kit-tareas-hamburgueseria`, con el vocabulario del sector (plancha
smash, patties, línea de montaje, freidora, delivery).

NO es de familia. `main.py` lo carga sólo cuando
`--producto kit-tareas-hamburgueseria` (el nombre del módulo se compone con el
pid, guiones → guiones bajos), así que aquí se puede hablar de «Apertura
Cocina», «Plancha Grill» o «FIFO Semanal» por su nombre: son hojas de ESTE kit.

Origen de cada cambio:
`auditorias/kit-tareas-hermanos/kit-tareas-hamburgueseria-verif.json`, campo
`contenido_pendiente` (una entrada por tema), más los equivalentes del
representante que aplican a una hamburguesería.

Contrato con `main.py`:
    post(wb, fname, cambios) -> bool
El `True` significa «he cambiado la ESTRUCTURA de este libro» (filas nuevas u
hoja nueva) y hace que `main.py` vuelva a pasar `motor.aplicar` antes de
`motor.cerrar`: es lo que mete las filas nuevas en el rango del contador, en la
DV y en el formato condicional, y lo que convierte la hoja nueva «Trimestral y
Anual» en una hoja de la familia (DV, contador, A4, protección) y no en una
isla.

ANCLAS, NO NÚMEROS DE FILA. Todo se localiza por el TEXTO de la celda, porque
este módulo corre DESPUÉS de `motor.aplicar`, que ya ha insertado las 5 filas
libres y reescrito los textos de grados. Si un ancla no aparece se levanta
`AnclaPerdida`: es preferible que el dry-run se caiga a publicar un kit con la
mitad del contenido aplicado.

Condicionantes MEDIDOS en este hermano (lo que lo separa del representante y de
sus hermanos ya hechos):

  · **Sus bandas de sección NO llevan fila separadora en blanco** (en
    «Apertura Cocina» la banda «  MISE EN PLACE BURGERS» va pegada a la tarea
    13 del bloque anterior). `_insertar_bloque` lo detecta con
    `_hay_separadores` en vez de dar por hecho el molde del kit base.
  · **La hora ancla del kit es 10:00**, la más temprana de las hojas de
    apertura («Verificar stock de carne», 01!'Apertura Cocina'). `motor.contexto`
    la saca del mínimo y con ella precarga el 08, así que ninguna hora nueva de
    este módulo baja de las 10:00 o el ancla se movería entre pasadas y el gate
    de idempotencia cazaría la diferencia.
  · **«Mantenimiento Mensual» tiene 2 bandas (5 y 3 tareas), no 3.** El molde de
    `_hoja_trimestral` redimensiona el bloque que se queda corto y añade el
    tercero al final (`_anadir_bloque_final`).
  · **En «FIFO Semanal» la fila siguiente a la cabecera es una BANDA, no una
    tarea** (fila 4 cabecera, fila 5 «  CÁMARAS», fila 6 primera tarea). El
    molde del representante coge `hr + 1` como estilo de dato y aquí eso pintaría
    la tabla de vida útil con el relleno oscuro de sección: `_primera_tarea` busca
    la primera fila con ordinal.
  · **No hay pescado crudo ni semicrudo en la carta del kit** (comprobadas las
    tres partidas del 02: Plancha Grill, Línea Montaje y Freidora), así que no se
    añade la tarea de congelación preventiva frente al anisakis. Su equivalente
    real en este sector es el **núcleo de la carne PICADA**: a diferencia de una
    pieza entera, la contaminación no se queda en la superficie, y ese sí se
    corrige (§ 02, «Plancha Grill»).

Dos trampas del motor que condicionan la redacción:
  · `motor.texto_temperatura` añade objetivo y «— anota la lectura: ____ °C» a
    toda tarea con verbo de registro + «temperatura» + equipo de frío. El texto
    de las cámaras se compone con `motor.OBJ_AMBOS` y `motor.LECTURA` para que
    salga YA en su forma final y la 2.ª pasada no encuentre nada que añadir.
  · `motor.texto_appcc` añade «(si tienes el Pack APPCC…)» a toda celda con la
    palabra APPCC. Por eso ningún texto de este módulo la menciona.
"""
import copy

import motor
from motor import get_column_letter as L

NCOL = 7                     # los 11 ficheros del kit son A:G

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
    # aplicar a la hoja (DOM-R2-22): este módulo corre después.
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


def _vacia(ws, fila):
    return all(ws.cell(row=fila, column=c).value is None
               for c in range(1, NCOL + 1))


def _hay_separadores(ws):
    """¿Las bandas de sección van precedidas de una fila en blanco?

    En `kit-tareas` sí; en `kit-tareas-hamburgueseria` no. De esto depende que
    un bloque nuevo case con los que ya están impresos.
    """
    g = motor.geometria(ws)
    if not g:
        return False
    tope = g['contador'] or ws.max_row
    for r in range(g['hr'] + 2, tope):
        if motor.es_fila_seccion(ws, r) and _vacia(ws, r - 1):
            return True
    return False


def _primera_tarea(ws, g):
    """Primera fila con ordinal. En este kit `hr + 1` es una BANDA."""
    for r in range(g['hr'] + 1, (g['contador'] or ws.max_row)):
        if isinstance(ws.cell(row=r, column=1).value, int):
            return r
    raise AnclaPerdida(f'«{ws.title}»: no encuentro ninguna fila de tarea')


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


def _insertar_al_inicio(ws, banda, tareas):
    """Inserta `tareas` como PRIMERAS tareas de un bloque ya existente.

    Es lo que exige el orden seguro de encendido: la campana y el gas no valen
    de nada detrás de «Encender plancha/grill y precalentar».
    """
    if _fila(ws, tareas[0][0], 2) is not None:
        return False
    b = _exige(ws, banda)
    est = _estilos(ws, b + 1)
    motor.insertar_filas(ws, b + 1, len(tareas))
    for i, t in enumerate(tareas):
        _pintar(ws, b + 1 + i, est)
        _escribir_tarea(ws, b + 1 + i, t)
    return True


def _insertar_bloque(ws, antes_de, titulo, tareas):
    """Bloque nuevo (banda + tareas) delante de otra banda.

    Respeta el molde de la hoja: sólo añade la fila separadora en blanco si el
    resto de bloques la tienen (`_hay_separadores`).
    """
    if _fila(ws, titulo) is not None:
        return False
    idx = _exige(ws, antes_de)
    sep = _hay_separadores(ws)
    est_banda = _estilos(ws, idx)
    est_tarea = _estilos(ws, idx + 1)
    est_blanca = None
    if sep:
        for r in range(idx - 1, motor.geometria(ws)['hr'], -1):
            if _vacia(ws, r):
                est_blanca = _estilos(ws, r)
                break
    n = len(tareas) + 1 + (1 if sep else 0)
    motor.insertar_filas(ws, idx, n)
    _pintar(ws, idx, est_banda)
    ws.cell(row=idx, column=1).value = titulo
    motor._merge(ws, f'A{idx}:{L(NCOL)}{idx}')
    for i, t in enumerate(tareas):
        _pintar(ws, idx + 1 + i, est_tarea)
        _escribir_tarea(ws, idx + 1 + i, t)
    if sep and est_blanca:
        _pintar(ws, idx + n - 1, est_blanca)
    return True


def _anadir_bloque_final(ws, titulo, n):
    """Banda nueva + `n` filas de tarea vacías DETRÁS del último bloque.

    Va antes de las 5 filas libres (que no llevan ordinal), así que las nuevas
    entran en el rango del contador en cuanto el motor vuelva a medir.
    Devuelve la lista de filas creadas, o None si el bloque ya existía.
    """
    if _fila(ws, titulo) is not None:
        return None
    g = motor.geometria(ws)
    if not g:
        raise AnclaPerdida(f'«{ws.title}»: no es un checklist de la familia')
    bandas = [r for r in range(g['hr'] + 1, g['contador'] or ws.max_row)
              if motor.es_fila_seccion(ws, r)]
    est_banda = _estilos(ws, bandas[-1])
    est_tarea = _estilos(ws, g['ultima'])
    idx = g['ultima'] + 1
    motor.insertar_filas(ws, idx, n + 1)
    _pintar(ws, idx, est_banda)
    ws.cell(row=idx, column=1).value = titulo
    motor._merge(ws, f'A{idx}:{L(NCOL)}{idx}')
    filas = []
    for i in range(n):
        _pintar(ws, idx + 1 + i, est_tarea)
        ws.cell(row=idx + 1 + i, column=1).value = 0
        filas.append(idx + 1 + i)
    return filas


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
#: contenido_pendiente «Higiene personal al inicio de apertura»: en el producto
#: la única mención («Lavarse manos, uniforme completo») es la tarea 21 de 22,
#: detrás de porcionar carne picada, cortar el pan y montar la línea. Aquí sube
#: al principio, antes de tocar alimento.
HIGIENE = [
    ('Uniforme y calzado de trabajo limpios, delantal cambiado y pelo '
     'recogido (gorro o redecilla)', 'Cocina', 'Todo el equipo', '10:00'),
    ('Sin anillos, reloj ni pulseras; uñas cortas, limpias y sin esmalte: la '
     'carne picada y el montaje se tocan a mano', 'Cocina', 'Todo el equipo',
     '10:00'),
    ('Heridas y cortes cubiertos con apósito impermeable de color visible y '
     'guante encima', 'Cocina', 'Todo el equipo', '10:00'),
    ('Lavado de manos al entrar y en cada cambio de tarea; lavamanos con '
     'jabón, papel y agua caliente', 'Cocina', 'Todo el equipo', '10:00'),
    ('Declarar síntomas digestivos o respiratorios: quien los tenga no '
     'manipula alimentos', 'Cocina', 'Cocinero', '10:00'),
]

#: contenido_pendiente «Orden de encendido inseguro»: el producto enciende
#: plancha (tarea 1), freidora (2) y comprueba el aceite (3) ANTES de la campana
#: (4), y no comprueba el gas en ningún sitio. Equivalente de DOM-13.
ENCENDIDO = [
    ('Encender la campana extractora y ventilar la cocina ANTES que ningún '
     'equipo: la plancha y la freidora son los dos focos de humo y grasa del '
     'local', 'Cocina', 'Cocinero', '10:45'),
    ('Abrir la llave general de gas y comprobar que NO huele a gas antes de '
     'prender nada; si huele, no enciendas ni la luz, ventila y avisa al '
     'mantenedor', 'Cocina', 'Cocinero', '10:45'),
]

#: La tarea 4 del producto («Encender campana extractora») se queda sin sentido
#: en cuanto la campana pasa a ser el primer paso: se reconvierte en la
#: comprobación de que la campana TIRA, que es lo que nadie hace.
CAMPANA_OK = ('Comprobar que la campana tira de verdad (una servilleta pegada '
              'a la rejilla se queda sujeta) y que los filtros están puestos y '
              'limpios')

#: contenido_pendiente «Verificación de cámaras al abrir»: el único control de
#: temperatura del kit está en el CIERRE. Equivalente de DOM-24. Va al inicio
#: del bloque de mise en place porque su primera tarea es justamente sacar la
#: carne picada de la cámara.
CAMARAS = [
    ('Comprobar que las cámaras han funcionado toda la noche y registrar '
     'temperatura' + motor.OBJ_AMBOS + motor.LECTURA + '. Si hay desviación, '
     'no uses la carne ni el género hasta valorarlo',
     'Cámara', 'Cocinero', '10:15'),
]

#: La higiene que se queda en el bloque final deja de duplicar el lavado del
#: inicio y pasa a cubrir el cruce que de verdad enferma en una hamburguesería:
#: carne picada cruda → pan, toppings y salsas.
LAVADO_CRUZADO = ('Lavarse las manos y cambiar de guantes al pasar de la carne '
                  'CRUDA al pan, los toppings o las salsas; tabla, pinzas y '
                  'espátula de crudo no vuelven a la línea de montaje')

#: contenido_pendiente «Registro de mermas del día». Lo más cercano del producto
#: («Anotar faltantes para pedido») es reposición, no merma.
MERMAS_COCINA = [
    ('Anotar las mermas del día (producto, cantidad y motivo): patties pasados '
     'de punto o caídos, pan seco, toppings retirados y pedidos devueltos — sin '
     'este dato el food cost del mes sale mal', 'Cocina', 'Cocinero', '22:30'),
]

#: contenido_pendiente «Aceite de freidora en frío», severidad ALTA y única
#: inconsistencia INTERNA del kit: «Cierre Cocina» filtra el aceite ANTES de
#: apagar la freidora, y «Freidora» (02) lo hace bien. Se corrige el orden con
#: dos sustituciones 1:1 y se recupera el apagado de la campana, que iba
#: encadenado en el texto viejo.
APAGAR_ANTES = ('Apagar la freidora al terminar el servicio y dejar que el '
                'aceite se enfríe; la campana sigue en marcha mientras tanto')
FILTRAR_FRIO = ('Filtrar o cambiar el aceite SOLO por debajo de 40 °C, nunca '
                'en caliente: al filtrarlo hirviendo salpica y es la quemadura '
                'más habitual del cierre')
APAGAR_RESTO = [
    ('Apagar plancha, horno y campana extractora cuando la freidora y la '
     'plancha ya estén frías', 'Cocina', 'Cocinero', '22:45'),
]


def _f01(wb, cambios):
    tocado = False
    ws = wb['Apertura Cocina']
    if _sustituir(ws, '  STOCK E HIGIENE', '  STOCK Y DESINFECCIÓN', col=1):
        cambios.append('«Apertura Cocina»: la sección final pasa a llamarse '
                       '«STOCK Y DESINFECCIÓN» — la higiene PERSONAL ya no '
                       'vive ahí, vive al principio del turno')
    if _sustituir(ws, 'Lavarse manos, uniforme completo', LAVADO_CRUZADO):
        cambios.append('«Apertura Cocina»: el lavado de manos del final deja '
                       'de duplicar el del inicio y cubre el cruce carne '
                       'picada CRUDA → pan, toppings y salsas')
    if _sustituir(ws, 'Encender campana extractora', CAMPANA_OK):
        cambios.append('«Apertura Cocina»: encender la campana pasa a ser el '
                       'primer paso del bloque, así que la tarea 4 se '
                       'reconvierte en comprobar que TIRA y que lleva filtros')
    if _insertar_bloque(ws, '  PLANCHA Y FREIDORA', '  HIGIENE PERSONAL',
                        HIGIENE):
        cambios.append('«Apertura Cocina»: bloque «HIGIENE PERSONAL» al '
                       f'inicio ({len(HIGIENE)} tareas), antes de tocar carne, '
                       'pan, queso o salsas')
        tocado = True
    if _insertar_al_inicio(ws, '  PLANCHA Y FREIDORA', ENCENDIDO):
        cambios.append('«Apertura Cocina»: orden seguro al abrir el bloque '
                       'PLANCHA Y FREIDORA (campana → comprobar gas → '
                       f'encender equipos), {len(ENCENDIDO)} tareas nuevas')
        tocado = True
    if _insertar_al_inicio(ws, '  MISE EN PLACE BURGERS', CAMARAS):
        cambios.append('«Apertura Cocina»: comprobación de que las cámaras '
                       'han funcionado toda la noche, con registro de '
                       'temperatura, ANTES de sacar la carne picada')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Cierre Cocina']
    if _sustituir(ws, 'Filtrar o cambiar aceite de freidora', APAGAR_ANTES):
        cambios.append('«Cierre Cocina»: primero se apaga la freidora y se '
                       'deja enfriar el aceite (antes se filtraba con la '
                       'freidora todavía encendida)')
    if _sustituir(ws, 'Apagar freidora, plancha, horno, campana',
                  FILTRAR_FRIO):
        cambios.append('«Cierre Cocina»: el filtrado del aceite pasa detrás '
                       'del apagado y se acota a menos de 40 °C — coherente '
                       'con 02!«Freidora», que ya lo hacía bien')
    if _insertar_tras(ws, FILTRAR_FRIO, APAGAR_RESTO):
        cambios.append('«Cierre Cocina»: apagado de plancha, horno y campana '
                       'como paso propio, cuando los equipos ya están fríos')
        tocado = True
    if _insertar_tras(ws, 'Anotar faltantes para pedido', MERMAS_COCINA):
        cambios.append('«Cierre Cocina»: registro DIARIO de mermas con '
                       'producto, cantidad y motivo')
        tocado = True
    motor.renumerar(ws)
    return tocado


# ==========================================================================
# 02 — partidas de cocina
# ==========================================================================
#: Equivalente sectorial del anisakis del representante: en una hamburguesería
#: el patógeno no viaja en el pescado, viaja en la carne PICADA. En una pieza
#: entera la contaminación se queda en la superficie y se sella; al picarla se
#: reparte por dentro, y por eso el punto «poco hecho» que es normal en un
#: entrecot no lo es en un patty. El producto decía sólo «medio, hecho, muy
#: hecho», sin una sola cifra.
PUNTO_CARNE = ('Controlar el punto con termómetro de sonda: la carne PICADA '
               'necesita 70 °C en el CENTRO (75 °C si la sirves a niños, '
               'embarazadas o personas mayores) — al picarla, lo de fuera pasa '
               'a estar dentro')
#: Cruce de crudo a listo para comer en la propia partida de plancha.
UTENSILIO_CRUDO = [
    ('Separar el utillaje de crudo: tabla, pinzas y espátula de la carne cruda '
     'marcadas y distintas de las del pan y los toppings', 'Cocina',
     'Cocinero plancha', '11:00'),
]

#: contenido_pendiente «Aceite de freidora en frío», rama del 02: aquí el orden
#: YA era correcto (apagar → filtrar), sólo faltaba la cifra.
FILTRAR_02 = ('Filtrar el aceite o cambiarlo si está oscuro o huele — SOLO por '
              'debajo de 40 °C, nunca en caliente')

#: DOM-26 en su versión hamburguesería: la lechuga y el tomate van CRUDOS entre
#: el patty y el pan, sin ningún paso térmico posterior.
INSERTS = ('Montar inserts: lechuga, tomate, cebolla y pepinillos — los de '
           'consumo crudo (lechuga, tomate, cebolla) se lavan y desinfectan '
           'con lejía apta para uso alimentario a la dosis del fabricante '
           '(habitual: 70 ppm, 5 min) y se ACLARAN con agua potable '
           'abundante')

#: contenido_pendiente «Registro de mermas», rama de la partida.
MERMAS_LINEA = [
    ('Anotar las mermas del turno (producto, cantidad y motivo): inserts que '
     'no se pueden guardar, lonchas de queso rotas, pan aplastado y burgers '
     'mal montadas', 'Cocina', 'Cocinero línea', '22:30'),
]


def _f02(wb, cambios):
    tocado = False
    ws = wb['Plancha Grill']
    if _sustituir(ws, 'Controlar punto de carne: medio, hecho, muy hecho',
                  PUNTO_CARNE):
        cambios.append('«Plancha Grill»: el punto de la carne PICADA se fija '
                       'en 70 °C de núcleo (75 °C en población de riesgo) y '
                       'con sonda — antes sólo decía «medio, hecho, muy hecho»')
    if _insertar_tras(ws, 'Verificar espátulas, prensas, termómetro',
                      UTENSILIO_CRUDO):
        cambios.append('«Plancha Grill»: utillaje de crudo separado y marcado, '
                       'antes de que empiece el servicio')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Línea Montaje']
    if _sustituir(ws, 'Montar inserts: lechuga, tomate, cebolla, pepinillos',
                  INSERTS):
        cambios.append('«Línea Montaje»: los vegetales que van crudos dentro '
                       'de la burger se lavan y desinfectan con dosis y '
                       'aclarado')
    if _insertar_tras(ws, 'Limpiar línea completa', MERMAS_LINEA):
        cambios.append('«Línea Montaje»: registro de mermas del turno '
                       '(producto, cantidad y motivo)')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Freidora']
    if _sustituir(ws, 'Filtrar aceite o cambiar si está oscuro/huele',
                  FILTRAR_02):
        cambios.append('«Freidora»: el filtrado del aceite se acota a menos '
                       'de 40 °C (el orden apagar → enfriar → filtrar ya era '
                       'correcto en esta partida)')
    motor.renumerar(ws)
    return tocado


# ==========================================================================
# 03 — manager
# ==========================================================================
#: contenido_pendiente «Registro de jornada del equipo»: obligación legal de
#: registro horario en España desde 2019, y ninguna de las 4 hojas del 03 la
#: recogía. Equivalente de DOM-17.
JORNADA_DIARIA = [
    ('Cerrar y validar el registro diario de jornada del equipo (entradas, '
     'salidas y pausas)', 'Office', 'Manager', '22:45'),
]
JORNADA_MENSUAL = [
    ('Archivar los registros de jornada del mes (hay que conservarlos 4 años)',
     'Office', 'Manager', 'Mensual'),
]


def _f03(wb, cambios):
    tocado = False
    ws = wb['Diario Manager']
    if _insertar_tras(ws, 'Anotar incidencias y 86s del día', JORNADA_DIARIA):
        cambios.append('«Diario Manager»: cierre y validación del registro '
                       'diario de jornada (obligatorio desde 2019)')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Mensual Manager']
    if _insertar_tras(ws, 'Coste laboral vs facturación', JORNADA_MENSUAL):
        cambios.append('«Mensual Manager»: archivo de los registros de '
                       'jornada del mes (conservación 4 años)')
        tocado = True
    motor.renumerar(ws)
    return tocado


# ==========================================================================
# 05 — semanales, mensuales y (nueva) trimestral/anual
# ==========================================================================
#: contenido_pendiente «Hoja Trimestral y Anual ausente». Dos de las tareas que
#: hoy figuran como MENSUALES lo son a medias: lo mensual es la comprobación del
#: usuario, lo anual es la revisión contratada.
EXTINTOR = ('Extintor: comprobación visual del usuario (aguja en zona verde, '
            'precinto intacto, acceso libre); la revisión oficial la hace el '
            'mantenedor y está en la hoja «Trimestral y Anual»')
CAMPANA = ('Campana: motor y filtros; la limpieza de los CONDUCTOS de '
           'extracción por empresa homologada está en la hoja «Trimestral y '
           'Anual»')

HOJA_TRIMESTRAL = 'Trimestral y Anual'
TRIMESTRAL_TITULO = ('Mantenimiento Trimestral y Anual — Revisiones '
                     'Contratadas')
#: (título de la banda, [(tarea, responsable, cadencia)])
TRIMESTRAL = [
    ('  CONTRATADO — EMPRESA AUTORIZADA', [
        ('Control de plagas (DDD): visita de la empresa autorizada, parte '
         'firmado y certificado en vigor', 'Empresa DDD', 'Trimestral'),
        ('Limpieza de la campana y de los CONDUCTOS de extracción por empresa '
         'homologada: plancha y freidora juntas engrasan el conducto el doble '
         'de rápido', 'Empresa externa', 'Anual'),
        ('Revisión de extintores y BIE por empresa mantenedora (etiqueta y '
         'acta de revisión)', 'Mantenedor', 'Anual'),
        ('Retimbrado de extintores: prueba de presión cada 5 años desde su '
         'fabricación', 'Mantenedor', 'Cada 5 años'),
        ('Revisión periódica de la instalación de gas por empresa habilitada '
         '(plancha, freidora y cocina de gas)', 'Instalador gas',
         'Cada 5 años'),
        ('Revisión de los equipos de frío por frigorista (estanqueidad y gas '
         'refrigerante)', 'Frigorista', 'Anual'),
    ]),
    ('  AGUA, RESIDUOS Y ACEITE USADO', [
        ('Retirada del aceite usado de fritura por gestor autorizado y archivo '
         'de los documentos de entrega: en una hamburguesería es el residuo '
         'que más volumen genera', 'Gestor autorizado', 'Trimestral'),
        ('Revisar el contrato de residuos y la retirada de cartón y envases: '
         'el delivery multiplica el volumen de envase', 'Manager',
         'Trimestral'),
        ('Prevención de legionela si hay torre de refrigeración o agua '
         'caliente sanitaria de riesgo', 'Empresa autorizada', 'Anual'),
        ('Analítica del agua de consumo si el local tiene depósito propio o '
         'descalcificador', 'Laboratorio', 'Anual'),
    ]),
    ('  ADMINISTRACIÓN Y EQUIPOS', [
        ('Revisar la póliza del local (continente, contenido y '
         'responsabilidad civil) y su vencimiento', 'Manager', 'Anual'),
        ('Revisión del TPV y del software de facturación (requisitos '
         'antifraude / Verifactu), también el de las apps de delivery',
         'Manager', 'Anual'),
        ('Calibrar los termómetros y la sonda de la plancha contra un patrón '
         'conocido: de esa sonda depende el núcleo de la carne picada',
         'Técnico', 'Anual'),
        ('Anotar la fecha de la próxima revisión de cada contrato y archivar '
         'el parte firmado', 'Manager', 'Trimestral'),
    ]),
]

#: contenido_pendiente «Vida útil de congelación por familia de producto».
#: «FIFO Semanal» cubre fechas de fresco pero nada de congelación.
VIDA_UTIL_TAREA = [
    ('Comprobar que ningún producto congelado supera su vida útil (ver la '
     'tabla al pie de esta hoja)', 'Cámara', 'Cocinero', 'Lunes'),
]
TITULO_TABLA = ('VIDA ÚTIL ORIENTATIVA EN CONGELACIÓN A −18 °C — '
                'ajústala a tu producto y a tu proveedor')
TABLA_VIDA_UTIL = [
    ('Patties y carne picada cruda', '3-4 meses', 'Congélalos ya porcionados '
     'y separados con papel: la picada tiene mucha superficie expuesta y se '
     'enrancia antes que la pieza entera'),
    ('Bacon y panceta', '1-2 meses', 'La grasa se enrancia aunque esté '
     'congelada: es lo primero que sabe a viejo'),
    ('Pollo crudo (crispy, tenders, nuggets)', '3-6 meses', 'Del congelador a '
     'la freidora, sin descongelar: si se atempera suelta agua y el rebozado '
     'se despega'),
    ('Pan de burger (brioche, pretzel, sésamo)', '2-3 meses', 'Congélalo el '
     'día que llega, no cuando ya se está pasando; descongela a temperatura '
     'ambiente dentro de su bolsa'),
    ('Patatas prefritas congeladas', '6-12 meses', 'NUNCA se descongelan: van '
     'del congelador al aceite o quedan blandas y salpican'),
    ('Aros de cebolla y rebozados', '6 meses', 'Igual que las patatas: '
     'directos al aceite'),
    ('Queso en lonchas', '2-3 meses', 'Se vuelve quebradizo al descongelar '
     'pero funde igual: úsalo sólo para fundir, no en frío'),
    ('Salsas caseras y fondos', '3 meses', 'Etiquetar con fecha de producción '
     'Y de congelación: la vida útil de esta tabla se cuenta desde la de '
     'congelación'),
    ('Verdura escaldada (cebolla, pimiento)', '8-12 meses', 'Sin escaldar '
     'previamente, la mitad'),
]


def _hoja_trimestral(wb, cambios):
    """La capa de mantenimiento CONTRATADO, que no existía en este kit.

    Se clona «Mantenimiento Mensual» (mismo molde, mismas columnas) y se
    reescribe: el bloque que se queda corto se redimensiona y el tercero se
    añade al final. El representante podía dar por hecho 3 bandas; aquí el
    modelo tiene 2, de 5 y 3 filas.
    """
    if HOJA_TRIMESTRAL in wb.sheetnames:
        return False
    modelo = wb['Mantenimiento Mensual']
    ws = wb.copy_worksheet(modelo)
    ws.title = HOJA_TRIMESTRAL
    ws.cell(row=1, column=1).value = TRIMESTRAL_TITULO
    g = motor.geometria(ws)
    if not g:
        raise AnclaPerdida(f'«{HOJA_TRIMESTRAL}»: el clon de '
                           f'«{modelo.title}» no es un checklist')
    ws.cell(row=g['hr'], column=3).value = 'Nº de parte'
    bandas = [r for r in range(g['hr'] + 1, g['contador'] or ws.max_row)
              if motor.es_fila_seccion(ws, r)]
    if len(bandas) > len(TRIMESTRAL):
        raise AnclaPerdida(f'«{modelo.title}» tiene {len(bandas)} bloques y el '
                           f'molde de «{HOJA_TRIMESTRAL}» sólo trae '
                           f'{len(TRIMESTRAL)}')
    # De ATRÁS hacia delante: redimensionar un bloque desplaza los de abajo.
    for i in range(len(bandas) - 1, -1, -1):
        titulo, tareas = TRIMESTRAL[i]
        banda = bandas[i]
        ws.cell(row=banda, column=1).value = titulo
        _, filas = _filas_de_bloque(ws, titulo)
        if len(filas) > len(tareas):
            raise AnclaPerdida(f'«{HOJA_TRIMESTRAL}»: el bloque '
                               f'«{titulo.strip()}» hereda {len(filas)} filas '
                               f'y el contenido sólo trae {len(tareas)}')
        if len(filas) < len(tareas):
            # `ultima` se fija ANTES del bucle: con `filas[-1]` dentro, cada
            # append movía el ancla y la segunda fila nueva caía sobre la BANDA
            # del bloque siguiente (celda combinada → `MergedCell` de sólo
            # lectura, y el rótulo de sección machacado con un 0).
            ultima = filas[-1]
            est = _estilos(ws, ultima)
            n = len(tareas) - len(filas)
            motor.insertar_filas(ws, ultima + 1, n)
            for k in range(n):
                _pintar(ws, ultima + 1 + k, est)
                filas.append(ultima + 1 + k)
        for r, (texto, resp, cad) in zip(filas, tareas):
            ws.cell(row=r, column=1).value = 0
            ws.cell(row=r, column=2).value = texto
            ws.cell(row=r, column=3).value = None      # lo escribe el cliente
            ws.cell(row=r, column=4).value = resp
            ws.cell(row=r, column=5).value = cad
            ws.cell(row=r, column=6).value = None
            ws.cell(row=r, column=7).value = None
    for titulo, tareas in TRIMESTRAL[len(bandas):]:
        filas = _anadir_bloque_final(ws, titulo, len(tareas))
        for r, (texto, resp, cad) in zip(filas, tareas):
            ws.cell(row=r, column=2).value = texto
            ws.cell(row=r, column=3).value = None
            ws.cell(row=r, column=4).value = resp
            ws.cell(row=r, column=5).value = cad
    motor.renumerar(ws)
    cambios.append(f'hoja nueva «{HOJA_TRIMESTRAL}»: mantenimiento contratado '
                   '(DDD, conductos de extracción, extintores y BIE, gas, '
                   'frigorista, aceite usado por gestor autorizado, legionela, '
                   'agua, seguro y Verifactu) con nº de parte y firma')
    return True


def _tabla_vida_util(ws, cambios):
    """Tabla editable de vidas útiles al pie de «FIFO Semanal»."""
    if _fila(ws, TITULO_TABLA) is not None:
        return False
    firma = motor._buscar_prefijo(ws, 'Firma encargado/a')
    if firma is None:
        raise AnclaPerdida('«FIFO Semanal»: no encuentro la fila de firma '
                           'bajo la que colgar la tabla de vida útil')
    g = motor.geometria(ws)
    est_titulo = _estilos(ws, _exige(ws, '  CÁMARAS'))
    est_cab = _estilos(ws, g['hr'])
    est_dato = _estilos(ws, _primera_tarea(ws, g))
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
                   f'congelación ({len(TABLA_VIDA_UTIL)} familias de una '
                   'hamburguesería)')
    return True


def _f05(wb, cambios):
    tocado = False
    # El molde de la hoja nueva es «Mantenimiento Mensual» TAL CUAL sale del
    # motor, así que se clona ANTES de matizarle el extintor y la campana.
    if _hoja_trimestral(wb, cambios):
        tocado = True

    ws = wb['Mantenimiento Mensual']
    if _sustituir(ws, 'Extintor: presión, caducidad', EXTINTOR):
        cambios.append('«Mantenimiento Mensual»: el extintor mensual es la '
                       'comprobación VISUAL del usuario; la revisión '
                       'contratada vive en «Trimestral y Anual»')
    if _sustituir(ws, 'Campana: motor, filtros', CAMPANA):
        cambios.append('«Mantenimiento Mensual»: lo mensual de la campana son '
                       'motor y filtros; la limpieza de CONDUCTOS por empresa '
                       'homologada vive en «Trimestral y Anual»')

    ws = wb['FIFO Semanal']
    if _insertar_tras(ws, 'Desechar caducado', VIDA_UTIL_TAREA):
        cambios.append('«FIFO Semanal»: comprobación de vida útil en '
                       'congelación por familia')
        tocado = True
    if _tabla_vida_util(ws, cambios):
        tocado = True
    motor.renumerar(ws)

    if _instrucciones(wb, 'Trimestral, anual y vida útil en congelación', [
            'La hoja «Trimestral y Anual» recoge el mantenimiento que se '
            'CONTRATA y que se pide en una inspección: DDD, conductos de '
            'extracción, extintores y BIE, instalación de gas, frigorista, '
            'aceite usado por gestor autorizado, legionela, agua, seguro y '
            'facturación.',
            'Anota el número de parte en la columna verde y firma cuando la '
            'empresa haya venido; la última tarea de la hoja es apuntar la '
            'fecha de la próxima revisión.',
            'En la hoja mensual quedan las comprobaciones que hace tu propio '
            'equipo (filtros de campana, vista del extintor): no sustituyen a '
            'la revisión contratada, la preparan.',
            'Al pie de «FIFO Semanal» tienes una tabla editable de vida útil '
            'en congelación por familia: una regla única para todo el '
            'congelador o tiras patatas buenas o sirves bacon rancio.']):
        cambios.append('Instrucciones: hoja trimestral/anual y tabla de vida '
                       'útil en congelación')
    return tocado


# ==========================================================================
# 06 — eventos y festivos
# ==========================================================================
#: contenido_pendiente «Alérgenos al confirmar reservas/eventos», severidad
#: baja porque el grueso del negocio es walk-in y delivery. El único evento del
#: kit que SÍ se reserva por adelantado es la cena de empresa de «Navidad», y
#: ahí es donde va el bloque: en una burger el gluten del pan, la lactosa del
#: queso, el huevo de las salsas y el SÉSAMO del pan son la norma, no la
#: excepción.
RESERVA = [
    ('Recoger POR ESCRITO alérgenos, intolerancias y dietas de los comensales '
     'y trasladarlos a cocina: pan (gluten y sésamo), queso (lactosa), salsas '
     '(huevo y mostaza) y rebozados están en casi toda la carta', 'Office',
     'Manager', 'Al confirmar'),
    ('Confirmar qué alternativas hay y que se pueden servir de verdad: pan sin '
     'gluten, burger vegana, sin queso — y cómo se evita el cruce en plancha y '
     'en línea', 'Cocina', 'Manager', 'Al confirmar'),
    ('Cerrar por escrito el precio por comensal y qué incluye (burger, sides, '
     'bebida y postre)', 'Office', 'Manager', 'Al confirmar'),
    ('Cobrar la señal o anticipo y dejar constancia del importe y la fecha',
     'Office', 'Manager', 'Al confirmar'),
    ('Firmar la política de cancelación y el plazo para dar el número final '
     'de comensales', 'Office', 'Manager', 'Al confirmar'),
    ('Acordar la hora de entrada y de salida de la mesa y reservar carne y pan '
     'suficientes para el grupo el día anterior', 'Sala', 'Manager',
     'Al confirmar'),
]


def _f06(wb, cambios):
    tocado = False
    ws = wb['Navidad']
    if _insertar_bloque(ws, '  PREPARACIÓN', '  AL CONFIRMAR LA RESERVA',
                        RESERVA):
        cambios.append('«Navidad»: bloque «AL CONFIRMAR LA RESERVA» '
                       '(alérgenos por escrito con gluten, sésamo, lactosa, '
                       'huevo y mostaza; alternativas y cruce; precio por '
                       'comensal, señal, cancelación y género reservado) — es '
                       'el momento en que se cierra una cena de empresa, no '
                       'el día del evento')
        tocado = True
    motor.renumerar(ws)
    return tocado


# ==========================================================================
# BONUS-02 — calendario anual
# ==========================================================================
#: El 1 de enero de una hamburguesería no es un «brunch de recuperación»: es
#: una decisión de abrir o no, y hay que comunicarla también en las apps.
ANO_NUEVO = ('Decidir si se abre; si se cierra, comunicarlo en Google '
             'Business Profile, en la web y en las apps de delivery con '
             '1 semana')
#: contenido_pendiente «Calendario con fechas nuevas del v2.0» (DOM-20).
#: (texto de la fila DETRÁS de la que se inserta, mes, evento, tareas, antel.)
FECHAS = [
    ('Carnaval (variable)', 'Marzo', '19 Mar — Día del Padre',
     'Menú familiar de mediodía, reservas ampliadas y burger XL para '
     'compartir', '2 semanas'),
    ('Apertura terraza', 'Abril-Junio', 'Comuniones y bautizos (temporada)',
     'Menú de grupo cerrado, señal y precio por comensal, sala o terraza '
     'privatizada', '1 mes'),
    ('Temporada alta', 'Agosto', '15 Ago — Asunción',
     'Servicio de festivo, refuerzo de turnos y de repartidores, terraza a '
     'pleno rendimiento', '1 semana'),
    # Detrás de Halloween, no de «Vuelta al cole»: el 1 de noviembre va
    # DESPUÉS del 31 de octubre y el calendario es cronológico.
    ('31 Oct — Halloween', 'Noviembre', '1 Nov — Todos los Santos',
     'Comida familiar de mediodía, burger de temporada y refuerzo del '
     'mediodía', '1 semana'),
    ('Cierre terraza', 'Diciembre',
     '6-8 Dic — Puente de la Constitución y la Inmaculada',
     'Horario de festivo, refuerzo de mediodía y de delivery, carne y pan '
     'para tres días seguidos', '2 semanas'),
]


def _bonus02(wb, cambios):
    ws = wb['Calendario Anual']
    tocado = False
    fila_ano = _fila(ws, '1 Ene — Año Nuevo', 2)
    if fila_ano and ws.cell(row=fila_ano, column=3).value != ANO_NUEVO:
        ws.cell(row=fila_ano, column=3).value = ANO_NUEVO
        cambios.append('«Calendario Anual»: el 1 de enero pasa a ser una '
                       'DECISIÓN (abrir o no, y comunicarlo también en las '
                       'apps de delivery), no un brunch dado por hecho')
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
                       'puente de diciembre)')
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
