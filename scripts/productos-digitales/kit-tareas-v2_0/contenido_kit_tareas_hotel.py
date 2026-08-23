#!/usr/bin/env python3
"""
contenido_kit_tareas_hotel.py — CONTENIDO propio de «kit-tareas-hotel»
(hermano de la familia, §5 de `kit-tareas-v2-SPEC.md`).

Fuente de los cambios: `auditorias/kit-tareas-hermanos/kit-tareas-hotel-verif.json`
campo `contenido_pendiente` (1 alta, 3 medias, 3 bajas) más los equivalentes de
§3 del representante que aplican a un hotel con F&B integral.

`main.py` lo carga sólo con `--producto kit-tareas-hotel` (compone el nombre del
módulo con el pid: `contenido_` + pid con guiones bajos), así que aquí se puede
hablar de «Buffet Almuerzo», «Banquetes y Eventos» o «RRHH Operativo» por su
nombre: son hojas de ESTE kit.

Contrato con `main.py`:
    post(wb, fname, cambios) -> bool

ESTE KIT ES DE MOLDE P4 EN 17 DE SUS 19 FICHEROS
================================================================================
`motor.aplicar` sólo reconoce el molde «▸» en 18 (negocio) y 19 (caja): los
01-15 y los dos BONUS llevan la cabecera «# | Tarea | Zona | Responsable | ✓ |
Hora | Notas» en la fila 5, con «✓» a secas en vez de «✓ Completada», y por eso
`hojas_reconocidas` los deja fuera. Reciben únicamente la normalización mínima
(`motor.normalizar_p4`: desplegable «✓,—,N/A», contador honesto, formato
condicional y bio), que `aplicar` les pasa antes de devolver `{}`.

Consecuencias que condicionan todo este módulo:

  · `motor.aplicar` devuelve `{}` (falsy), así que `main.py` **NO vuelve a pasar
    el motor** tras `post()` ni llama a `motor.cerrar`. Todo lo que dependa de
    la geometría nueva —rango del contador, formato condicional, desplegable de
    las filas nuevas, A4 y pie de una hoja nueva— **lo tiene que dejar hecho
    este módulo**. Por eso `post()` termina llamando a `motor.normalizar_p4` y
    por eso existen `_dv_extender` y `_hoja_legal`.
  · `motor.textos_de_tarea` (y con él `texto_grados`, `texto_appcc` y
    `texto_temperatura`) tampoco corre sobre P4: medido en
    `01-fb-buffet-desayuno.xlsx:Apertura Desayuno:B16`, que seguía con
    «(>65°C)» pegado después del motor. La normalización transversal de grados
    (DOM-R2-22) la aplica aquí `_normalizar_grados`, al FINAL de cada fichero, y
    todos los textos nuevos de este módulo ya se escriben en su forma final
    («≤ −18 °C», «0-4 °C») para que la 2.ª pasada no encuentre nada que cambiar.
  · el molde P4 REPITE la fila de cabecera en cada sección y **reinicia la
    numeración en 1** dentro de cada bloque: `motor.renumerar` (que va por
    `motor.geometria`, del molde ▸) devuelve None aquí. La numeración la rehace
    `_renumerar_p4`.
  · las columnas «Responsable» y «Hora» van VACÍAS en todo el molde P4 de este
    kit (son verdes, las rellena el hotel, que tiene turnos propios). Las tareas
    nuevas respetan eso y sólo escriben #, Tarea y Zona. La única excepción
    documentada es la hoja nueva «Trimestral y Anual», donde la CADENCIA de cada
    revisión es el dato y ocupa la columna F.
  · el color de la columna «Zona» depende del VALOR («Cocina» naranja, «Sala»
    lila, «Piscina» cian…). Copiar el estilo de la fila de anclaje pinta la zona
    equivocada, así que `_zona` busca en la propia hoja una fila con esa zona y
    le copia el relleno.

DÓNDE VA CADA HALLAZGO, Y POR QUÉ AHÍ
================================================================================
  · ANISAKIS (alta) → 01 «Apertura Desayuno» (salmón marinado/ahumado del buffet
    de desayuno), 02 «Buffet Almuerzo» (carpaccio y salmón de la estación fría)
    y 02 «Buffet Cena» (foie, tartar y ceviche de la estación premium). Son tres
    mises en place distintas, de tres servicios distintos y con tres equipos
    distintos: no es la misma tarea repetida.
  · CÁMARAS de la noche → 01 (cocina de desayunos, que abre a las 05:15 y es la
    primera que saca género) y 03 (office del restaurante à la carte, que abre
    a las 16:00 con sus propias cámaras). En 02 NO se repite: el buffet de
    almuerzo tira de la misma cocina central que ya comprobó el desayuno, y
    triplicar la comprobación es exactamente lo que §2.5 colapsa en el
    representante.
  · CAFETERAS → la limpieza DIARIA (backflush o ciclo con pastilla, según el
    modelo) va donde está la máquina y la hace quien la usa: 01 «Cierre
    Desayuno» y 04 «Lobby Bar». La DESCALCIFICACIÓN periódica, que se contrata
    o la hace el técnico, va a 13 «Mensual». Es el mismo reparto del ajuste
    DOM-15 del representante.
  · VIDA ÚTIL en congelación → al pie de 01 «Cierre Desayuno», que es la hoja
    cuya primera sección entera decide qué producto del buffet vuelve a cámara
    y qué se tira; es ahí donde el jefe de partida se pregunta cuánto aguanta.
  · HOJA «Trimestral y Anual» → 13-mantenimiento, que es el libro del jefe de
    SSTT y ya tiene las cadencias diaria, semanal y mensual: le faltaba la capa
    de lo que se CONTRATA y se pide por escrito en una inspección (DDD,
    conductos, legionela, OCA, extintores, gas, RITE, ascensores, seguros).
"""
import copy

import motor
from motor import get_column_letter as L

#: Los 17 ficheros de molde P4 de este kit son A:G; el calendario, A:F.
NCOL = 7
NCOL_CAL = 6

#: Relleno de la columna «Zona» por valor, medido en los 19 ficheros del kit.
#: Se usa sólo como respaldo: `_zona` prefiere copiar el estilo de una fila real
#: de la misma hoja, que además trae bordes y fuente.
ZONA_COLOR = {
    'Cocina': 'FFF3E0', 'Buffet': 'FFF3E0', 'Sala': 'F3E5F5',
    'Admin': 'FFF8E1', 'Limpieza': 'EFEBE9', 'Mantenimiento': 'FFF3E0',
    'Banquetes': 'F3E5F5', 'À la Carte': 'F3E5F5', 'RRHH': 'FFF8E1',
    'Lobby Bar': 'E0F2F1', 'Snack Bar': 'FFF3E0', 'Pool Bar': 'E0F7FA',
    'Piscina': 'E0F7FA',
    # columna «Impacto» del calendario (mismo índice de columna)
    'Almuerzo familiar': 'FFF3E0', 'Banquetes pico': 'F3E5F5',
    'Ocupación alta': 'E8F5E9',
}


class AnclaPerdida(RuntimeError):
    """El texto que este módulo esperaba encontrar ya no está en la hoja."""


# ==========================================================================
# Utilidades de anclaje
# ==========================================================================
def _norm(v):
    """Texto comparable: la normalización de grados que este módulo aplica.

    Así el mismo ancla vale en la 1.ª pasada (texto original, «(>65°C)») y en la
    2.ª (texto ya normalizado, «(>65 °C)»).
    """
    return motor.texto_grados(v) if isinstance(v, str) else v


def _fila(ws, texto, col=2):
    texto = _norm(texto)
    for r in range(1, ws.max_row + 1):
        if _norm(ws.cell(row=r, column=col).value) == texto:
            return r
    return None


def _exige(ws, texto, col=2):
    r = _fila(ws, texto, col)
    if r is None:
        raise AnclaPerdida('«{0}»: no encuentro {1}=«{2}» '
                           '(kit-tareas-hotel)'.format(ws.title, L(col), texto))
    return r


def _estilos(ws, fila, ncol=NCOL):
    return [copy.copy(ws.cell(row=fila, column=c)._style)
            for c in range(1, ncol + 1)]


def _pintar(ws, fila, estilos):
    for c, st in enumerate(estilos, start=1):
        ws.cell(row=fila, column=c)._style = copy.copy(st)


def _zona(ws, fila, valor):
    """Escribe la Zona y le pone el relleno que esa zona tiene en la hoja."""
    cel = ws.cell(row=fila, column=3)
    cel.value = valor
    for r in range(1, ws.max_row + 1):
        if r == fila:
            continue
        otra = ws.cell(row=r, column=3)
        if otra.value == valor and otra.fill is not None and \
                otra.fill.fill_type == 'solid':
            cel._style = copy.copy(otra._style)
            return
    color = ZONA_COLOR.get(valor)
    if color:
        motor._relleno(cel, color)


def _escribir_tarea(ws, fila, texto, zona, cadencia=None):
    """Fila de tarea del molde P4: # (lo pone `_renumerar_p4`), Tarea y Zona.

    «Responsable» y «Hora» se dejan vacías a propósito: en este kit son celdas
    verdes que el hotel rellena con sus turnos, y ninguna de las 400 tareas del
    molde P4 viene precargada. `cadencia` sólo se usa en la hoja legal nueva,
    donde la columna F deja de ser «Hora» y pasa a ser «Cadencia».
    """
    ws.cell(row=fila, column=1).value = 0
    ws.cell(row=fila, column=2).value = texto
    _zona(ws, fila, zona)
    if cadencia is not None:
        ws.cell(row=fila, column=6).value = cadencia


def _sustituir(ws, viejo, nuevo, col=2):
    """Sustitución 1:1 por texto. Devuelve la fila, o None si ya estaba."""
    if _fila(ws, nuevo, col) is not None:
        return None
    r = _exige(ws, viejo, col)
    ws.cell(row=r, column=col).value = nuevo
    return r


def _insertar_tras(ws, ancla, tareas):
    """Inserta `tareas` [(texto, zona), …] debajo de la fila cuya B es `ancla`."""
    if _fila(ws, tareas[0][0]) is not None:
        return False                                   # ya insertadas
    r = _exige(ws, ancla)
    est = _estilos(ws, r)
    motor.insertar_filas(ws, r + 1, len(tareas))
    for i, tarea in enumerate(tareas):
        _pintar(ws, r + 1 + i, est)
        _escribir_tarea(ws, r + 1 + i, tarea[0], tarea[1])
    return True


def _insertar_seccion(ws, antes_de, titulo, tareas):
    """Sección nueva del molde P4: banda + fila de cabecera + tareas.

    En P4 CADA sección repite su fila de cabecera; omitirla dejaría el bloque
    huérfano visualmente y, sobre todo, rompería la simetría que el contador da
    por hecha al restar `COUNTIF(B,"Tarea")`.

    Las tareas pueden ser (texto, zona) o (texto, zona, cadencia).
    """
    if _fila(ws, titulo, 1) is not None:
        return False
    idx = _exige(ws, antes_de, 1)
    est_banda = _estilos(ws, idx)
    est_cab = _estilos(ws, idx + 1)
    est_tarea = _estilos(ws, idx + 2)
    cabecera = [ws.cell(row=idx + 1, column=c).value
                for c in range(1, NCOL + 1)]
    motor.insertar_filas(ws, idx, len(tareas) + 2)
    _pintar(ws, idx, est_banda)
    ws.cell(row=idx, column=1).value = titulo
    motor._merge(ws, 'A{0}:{1}{0}'.format(idx, L(NCOL)))
    _pintar(ws, idx + 1, est_cab)
    for c, v in enumerate(cabecera, start=1):
        ws.cell(row=idx + 1, column=c).value = v
    for i, tarea in enumerate(tareas):
        _pintar(ws, idx + 2 + i, est_tarea)
        _escribir_tarea(ws, idx + 2 + i, tarea[0], tarea[1],
                        tarea[2] if len(tarea) > 2 else None)
    return True


def _renumerar_p4(ws):
    """Numeración del molde P4: reinicia en 1 en CADA sección.

    `motor.renumerar` no sirve: pasa por `motor.geometria`, que es del molde ▸ y
    devuelve None en estas hojas. Y renumerar de corrido rompería el molde: las
    cuatro secciones de «Apertura Desayuno» van 1-11, 1-12, 1-7, 1-7.
    """
    g = motor.geometria_p4(ws)
    if not g:
        return 0
    tope = g['contador'] or ws.max_row + 1
    n = total = 0
    for r in range(g['hr'] + 1, tope):
        if motor.es_fila_seccion(ws, r):
            n = 0
            continue
        if ws.cell(row=r, column=2).value == 'Tarea':      # cabecera repetida
            continue
        if isinstance(ws.cell(row=r, column=1).value, int):
            n += 1
            total += 1
            ws.cell(row=r, column=1).value = n
    return total


def _dv_extender(ws):
    """Mete las filas nuevas en el desplegable «✓,—,N/A» de la hoja.

    `motor.normalizar_p4` sólo REESCRIBE el `formula1` de las validaciones que
    ya existen; no amplía su `sqref`. Y `motor.cerrar` —que en el molde ▸ lo
    reconstruye todo— no llega a correr aquí. Sin esto, las tareas nuevas se
    entregarían sin desplegable en la única columna que hay que marcar.
    """
    g = motor.geometria_p4(ws)
    if not g:
        return
    dv = None
    for d in ws.data_validations.dataValidation:
        if d.type == 'list' and d.formula1 == motor.DV_LISTA:
            dv = d
            break
    if dv is None:
        return
    tope = g['contador'] or ws.max_row + 1
    for r in range(g['hr'] + 1, tope):
        if motor.es_fila_seccion(ws, r):
            continue
        if isinstance(ws.cell(row=r, column=1).value, int):
            dv.add(ws.cell(row=r, column=g['marca']))


def _normalizar_grados(ws, cambios):
    """DOM-R2-22 en el molde P4, al que `motor.textos_de_tarea` no llega."""
    n = 0
    for row in ws.iter_rows():
        for c in row:
            nuevo = motor.texto_grados(c.value)
            if isinstance(c.value, str) and nuevo != c.value:
                c.value = nuevo
                n += 1
    if n:
        cambios.append('«{0}»: {1} temperaturas normalizadas al signo menos '
                       'tipográfico y con espacio antes de la unidad '
                       '(DOM-R2-22, que el motor no aplica al molde P4)'
                       .format(ws.title, n))
    return n


def _instrucciones(wb, encabezado, lineas):
    """Bloque nuevo en «Instrucciones», ENCIMA de la bio y de la versión.

    `motor.reescribir_instrucciones` no corre en el molde P4, así que si el
    bloque se añadiera al final (como en los hermanos ▸) quedaría por debajo de
    la firma del autor y de la línea de versión, que son el cierre de la hoja.
    """
    if 'Instrucciones' not in wb.sheetnames:
        return False
    ws = wb['Instrucciones']
    col = 2 if any(isinstance(ws.cell(row=r, column=2).value, str)
                   for r in range(1, min(ws.max_row, 12) + 1)) else 1
    corte = None
    for r in range(1, ws.max_row + 1):
        v = ws.cell(row=r, column=col).value
        if not isinstance(v, str):
            continue
        if v == encabezado:
            return False                               # ya está
        if corte is None and (motor.RX_BIO.search(v)
                              or motor.RX_VERSION.match(v)):
            corte = r
    if corte is None:
        corte = ws.max_row + 1
    est_tit = copy.copy(ws.cell(row=corte, column=col)._style)
    est_txt = est_tit
    for r in range(1, ws.max_row + 1):
        v = ws.cell(row=r, column=col).value
        if isinstance(v, str) and v.startswith('▸ '):
            est_txt = copy.copy(ws.cell(row=r, column=col)._style)
            break
    for r in range(1, ws.max_row + 1):
        v = ws.cell(row=r, column=col).value
        if isinstance(v, str) and v.endswith(':') and not v.startswith('▸'):
            est_tit = copy.copy(ws.cell(row=r, column=col)._style)
            break
    motor.insertar_filas(ws, corte, len(lineas) + 2)
    ws.cell(row=corte, column=col).value = encabezado
    ws.cell(row=corte, column=col)._style = copy.copy(est_tit)
    for i, txt in enumerate(lineas, start=1):
        cel = ws.cell(row=corte + i, column=col)
        cel.value = '▸ ' + txt
        cel._style = copy.copy(est_txt)
    return True


# ==========================================================================
# 01-fb-buffet-desayuno.xlsx — «Apertura Desayuno» y «Cierre Desayuno»
# ==========================================================================
#: DOM-12 + DOM-13 + DOM-24 (equivalentes) — la jornada del hotel arrancaba con
#: «Encender hornos, planchas, baño maría y equipamiento»: nadie se lava las
#: manos, nadie mira la llave del gas y nadie comprueba que las cámaras han
#: aguantado la noche antes de sacar el género del desayuno. El buffet de
#: desayuno es el primer servicio del día y el de mayor número de comensales
#: simultáneos de todo el hotel. Orden interno: persona → frío → campana → gas
#: → fuego.
#: OJO — el título de esta banda NO puede llevar una hora. `motor.contexto`
#: barre la columna A de toda hoja cuyo título empiece por «Apertura» con
#: `RX_HORA_EN_TEXTO` para deducir la HORA ANCLA del kit, y un «(05:15-05:30)»
#: aquí adelantaba la apertura del kit de 05:30 a 05:15: la 2.ª pasada leía la
#: hora que había escrito la 1.ª y las 18 horas precargadas de
#: 18-apertura-cierre-negocio.xlsx bailaban 15 min (29 diferencias de
#: idempotencia, medidas). El horario de la sección va en el texto de la tarea,
#: no en la banda.
ARRANQUE = 'Higiene personal y arranque seguro de la cocina'
ARRANQUE_TAREAS = [
    ('Uniforme y calzado de trabajo limpios, delantal cambiado y pelo '
     'recogido (gorro o redecilla)', 'Cocina'),
    ('Sin anillos, reloj ni pulseras; uñas cortas, limpias y sin esmalte',
     'Cocina'),
    ('Heridas y cortes cubiertos con apósito impermeable de color visible y '
     'guante encima', 'Cocina'),
    ('Lavado de manos al entrar y en cada cambio de tarea: jabón, agua '
     'caliente y papel de un solo uso', 'Cocina'),
    ('Declarar síntomas digestivos o respiratorios: quien los tenga no '
     'manipula alimentos', 'Cocina'),
    ('Comprobar que las cámaras y neveras de la cocina de desayunos han '
     'funcionado toda la noche y registrar la temperatura (refrigeración '
     '0-4 °C / congelación ≤ −18 °C) — anota la lectura: ____ °C. Si hay '
     'desviación, no saques el género hasta valorarlo', 'Cocina'),
    ('Encender la campana extractora y ventilar la cocina ANTES de encender '
     'nada más', 'Cocina'),
    ('Si la cocina tiene gas: abrir la llave general y comprobar que NO huele '
     'a gas; si huele, no enciendas nada, ventila y avisa a mantenimiento',
     'Cocina'),
]

ENCENDER = ('Encender hornos, planchas, baño maría y equipamiento sólo '
            'después de la campana y del control del gas')

#: DOM-02 (equivalente, ALTA) — el buffet de desayuno de un hotel de 4-5 * sirve
#: salmón todos los días, y en ninguno de los 19 ficheros había una sola línea
#: sobre la congelación preventiva que exige el Reglamento (CE) 853/2004 para el
#: pescado que se sirve crudo, marinado o ahumado en frío. La palabra ANISAKIS
#: va en mayúsculas y completa a propósito: es la que se busca con Ctrl+F y la
#: que pregunta el inspector.
ANISAKIS_DESAYUNO = [
    ('Salmón marinado o ahumado en frío y cualquier pescado que se sirva crudo '
     '— prevención de ANISAKIS: usar sólo producto con congelación previa '
     'acreditada (≥ 24 h a −20 °C, o 15 h a −35 °C); si lo marinas en casa, '
     'congélalo tú antes y anota el lote', 'Buffet'),
]

#: DOM-18 (equivalente) — «Separar producto reutilizable (sin contaminar) de
#: merma» deja al criterio del que desmonta qué es «sin contaminar». En un
#: buffet de autoservicio lo que decide no es el aspecto: es si el cliente ha
#: podido tocarlo y si ha aguantado la temperatura toda la exposición.
SOBRANTES = ('Separar producto reutilizable de merma: lo que ha estado EXPUESTO '
             'en la línea del buffet (al alcance del cliente o fuera de '
             'temperatura) se retira; sólo vuelve a cámara lo que no ha salido '
             'del office y ha mantenido la cadena de frío o de calor')

#: DOM-29 (equivalente) — el etiquetado no daba ni temperatura ni plazo, en la
#: hoja que decide qué producto del buffet se guarda para el día siguiente.
ETIQUETAR = ('Etiquetar el producto reutilizable con el nombre, la fecha y la '
             'hora, y guardarlo tapado en refrigeración 0-4 °C: la vida útil '
             'por familia está en la tabla del pie de esta hoja')

#: DOM-15 (equivalente) — «Limpiar y desinfectar estación de zumos y café» no
#: dice lo único que de verdad estropea una cafetera de buffet: el grupo y el
#: circuito de leche. Un hotel tiene máquinas de dos tipos (súper-automática en
#: el buffet, semiautomática en el bar) y el ciclo no es el mismo.
CAFE_DESAYUNO = ('Limpiar y desinfectar la estación de zumos y café: ejecutar '
                 'el ciclo de limpieza de la cafetera (pastilla detergente o '
                 'backflush del grupo, según el modelo), lavar el circuito y '
                 'la jarra de leche, y desmontar y fregar la exprimidora')

TITULO_VIDA_UTIL = ('VIDA ÚTIL ORIENTATIVA EN CONGELACIÓN A −18 °C — ajústala a '
                    'tu producto y a tu proveedor')
VIDA_UTIL = [
    ('Carnes rojas y aves crudas, en pieza', '6-12 meses',
     'Porciona ANTES de congelar: descongelar y volver a congelar no se hace'),
    ('Carne picada y preparados de carne', '3 meses',
     'Más superficie expuesta: se enrancia y se oxida mucho antes que la '
     'pieza entera'),
    ('Pescado blanco y marisco crudo', '3-6 meses',
     'El tratamiento antianisakis (≥ 24 h a −20 °C) no sustituye a esta vida '
     'útil: se cuentan por separado'),
    ('Pescado azul (salmón, atún, boquerón)', '2-3 meses',
     'La grasa se enrancia aunque esté congelado: es el que antes se '
     'estropea'),
    ('Fondos, salsas y cremas de elaboración propia', '3 meses',
     'Etiqueta con la fecha de producción Y la de congelación: la vida útil '
     'se cuenta desde la de congelación'),
    ('Masas, bases de tarta y hojaldre crudos', '1-2 meses',
     'La levadura pierde fuerza: después sube mal aunque siga siendo seguro'),
    ('Bollería y pan ya horneados', '1-3 meses',
     'Pierde textura antes que seguridad; regenera en horno, nunca en '
     'microondas'),
    ('Verdura blanqueada, purés y guarniciones', '8-12 meses',
     'Blanquea antes de congelar: sin blanquear pierde color y textura en '
     'pocas semanas'),
    ('Producto que ya ha salido a la línea del buffet', 'No congelar',
     'Lo expuesto en sala o servido por el cliente no vuelve al congelador: '
     'se retira'),
]


def _tabla_vida_util(ws, cambios):
    """Tabla editable de vida útil al pie de «Cierre Desayuno».

    Va DEBAJO de la fila de firma, es decir, por debajo del contador y fuera
    del rango que éste cuenta: es una referencia, no una tarea que marcar.
    """
    if _fila(ws, TITULO_VIDA_UTIL, 1) is not None:
        return False
    g = motor.geometria_p4(ws)
    if not g:
        raise AnclaPerdida('«Cierre Desayuno»: no es una hoja del molde P4')
    firma = None
    for r in range(g['contador'] or 1, ws.max_row + 1):
        v = ws.cell(row=r, column=1).value
        if isinstance(v, str) and v.startswith('Firma responsable'):
            firma = r
            break
    if firma is None:
        raise AnclaPerdida('«Cierre Desayuno»: no encuentro la fila de firma')
    banda = _exige(ws, 'Retirada y registro de sobrantes', 1)
    est_titulo = _estilos(ws, banda)
    est_cab = _estilos(ws, g['hr'])
    est_dato = _estilos(ws, g['hr'] + 1)
    motor.insertar_filas(ws, firma + 1, 3 + len(VIDA_UTIL))
    fila = firma + 2
    _pintar(ws, fila, est_titulo)
    ws.cell(row=fila, column=1).value = TITULO_VIDA_UTIL
    motor._merge(ws, 'A{0}:{1}{0}'.format(fila, L(NCOL)))
    fila += 1
    _pintar(ws, fila, est_cab)
    ws.cell(row=fila, column=2).value = 'Familia'
    ws.cell(row=fila, column=3).value = 'Vida útil'
    ws.cell(row=fila, column=4).value = 'Notas'
    motor._merge(ws, 'D{0}:{1}{0}'.format(fila, L(NCOL)))
    for i, dato in enumerate(VIDA_UTIL, start=1):
        r = fila + i
        _pintar(ws, r, est_dato)
        ws.cell(row=r, column=1).value = None
        ws.cell(row=r, column=2).value = dato[0]
        ws.cell(row=r, column=3).value = dato[1]
        ws.cell(row=r, column=4).value = dato[2]
        for c in (2, 3, 4):
            motor._verde(ws.cell(row=r, column=c))
        motor._merge(ws, 'D{0}:{1}{0}'.format(r, L(NCOL)))
    cambios.append('«Cierre Desayuno»: tabla editable de vida útil en '
                   'congelación ({0} familias) al pie, fuera del rango del '
                   'contador — DOM-29 (equivalente)'.format(len(VIDA_UTIL)))
    return True


def _f01(wb, cambios):
    tocado = False
    ws = wb['Apertura Desayuno']
    if _insertar_seccion(ws, 'Cocina — Preparación (05:30-06:30)', ARRANQUE,
                         ARRANQUE_TAREAS):
        cambios.append('«Apertura Desayuno»: sección nueva «{0}» ({1} tareas) '
                       'delante de la primera que toca género: higiene '
                       'personal, comprobación nocturna de cámaras y orden '
                       'seguro campana → gas → equipos, que no existían — '
                       'DOM-12 / DOM-13 / DOM-24 (equivalentes)'
                       .format(ARRANQUE, len(ARRANQUE_TAREAS)))
        tocado = True
    if _sustituir(ws, 'Encender hornos, planchas, baño maría y equipamiento',
                  ENCENDER):
        cambios.append('«Apertura Desayuno»: la primera tarea de fuego remite '
                       'al orden seguro (campana y gas antes que nada) — '
                       'DOM-13 (equivalente)')
    if _insertar_tras(ws, 'Montar estación fría: embutidos, quesos, salmón, '
                          'ensaladas', ANISAKIS_DESAYUNO):
        cambios.append('«Apertura Desayuno»: congelación preventiva frente al '
                       'ANISAKIS del salmón marinado o ahumado del buffet '
                       '(Rgto. CE 853/2004), que no estaba en ninguno de los '
                       '19 ficheros — DOM-02 (equivalente, ALTA)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)

    ws = wb['Cierre Desayuno']
    if _sustituir(ws, 'Separar producto reutilizable (sin contaminar) de '
                      'merma', SOBRANTES):
        cambios.append('«Cierre Desayuno»: el criterio de los sobrantes deja '
                       'de ser «sin contaminar» y pasa a ser si ha estado '
                       'expuesto en la línea y si ha mantenido la temperatura '
                       '— DOM-18 (equivalente)')
    if _sustituir(ws, 'Etiquetar producto reutilizable con fecha y '
                      'temperatura', ETIQUETAR):
        cambios.append('«Cierre Desayuno»: el etiquetado lleva hora, '
                       'temperatura de conservación y remisión a la tabla de '
                       'vida útil — DOM-29 (equivalente)')
    if _sustituir(ws, 'Limpiar y desinfectar estación de zumos y café',
                  CAFE_DESAYUNO):
        cambios.append('«Cierre Desayuno»: la limpieza diaria de la cafetera '
                       'del buffet dice QUÉ se limpia (ciclo con pastilla o '
                       'backflush, según el modelo, y circuito de leche) — '
                       'DOM-15 (equivalente)')
    if _tabla_vida_util(ws, cambios):
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)
    if _instrucciones(wb, 'Seguridad alimentaria y arranque:', [
            'La primera sección de «Apertura Desayuno» es de higiene personal '
            'y de arranque seguro: cámaras primero (¿han aguantado la noche?), '
            'campana después, comprobación del gas y sólo entonces hornos, '
            'planchas y baño maría.',
            'El salmón marinado o ahumado en frío y cualquier pescado que se '
            'sirva crudo necesitan congelación previa: ≥ 24 h a −20 °C o 15 h '
            'a −35 °C. Pide el certificado al proveedor y anota el lote.',
            'Al pie de «Cierre Desayuno» tienes una tabla editable de vida '
            'útil en congelación por familia: ajústala a tu producto y a tu '
            'proveedor. Está fuera del contador porque es una referencia, no '
            'una tarea.']):
        cambios.append('Instrucciones: arranque seguro, anisakis y tabla de '
                       'vida útil — DOM-12 / DOM-02 / DOM-29')
        tocado = True
    return tocado


# ==========================================================================
# 02-fb-buffet-comida-cena.xlsx — «Buffet Almuerzo» y «Buffet Cena»
# ==========================================================================
#: DOM-26 (equivalente) — la estación de ensaladas mete en la misma línea lo que
#: se sirve crudo (lechuga, tomate) y lo que ya viene cocido (quinoa, pasta
#: fría). Lo único que necesita desinfección es lo primero, y sin el aclarado
#: final la lejía se sirve con la hoja.
ENSALADAS = ('Montar estación de ensaladas y fríos: lechuga, tomate, quinoa, '
             'pasta fría. Los vegetales que se sirven CRUDOS, desinfectados '
             'con lejía apta para uso alimentario según la dosis del '
             'fabricante (habitual: 70 ppm, 5 min) y ACLARADOS con agua '
             'potable abundante')

ANISAKIS_ALMUERZO = [
    ('Carpaccio, salmón y cualquier pescado que se sirva crudo o marinado — '
     'prevención de ANISAKIS: exigir al proveedor el certificado de '
     'congelación previa (≥ 24 h a −20 °C, o 15 h a −35 °C) o congelarlo tú, '
     'y anotar el lote', 'Buffet'),
]

ANISAKIS_CENA = [
    ('Tartar, ceviche y pescado crudo de la estación premium — prevención de '
     'ANISAKIS: sólo pescado con congelación previa acreditada (≥ 24 h a '
     '−20 °C, o 15 h a −35 °C); anota el lote y no lo montes hasta el momento '
     'del servicio', 'Buffet'),
]

#: DOM-R2-09 + §2.9 — «(registrar APPCC)» manda a un sitio que el hotel puede no
#: tener, y la tarea no deja dónde anotar la lectura que pide el inspector.
TEMP_ALMUERZO = ('Verificar temperaturas antes de abrir: caliente > 65 °C, '
                 'frío < 5 °C — anota la lectura: ____ °C (si tienes el Pack '
                 'APPCC, regístrala en su hoja de temperaturas; si no, en la '
                 'columna «Notas»)')


def _f02(wb, cambios):
    tocado = False
    ws = wb['Buffet Almuerzo']
    if _sustituir(ws, 'Montar estación de ensaladas y fríos: lechuga, tomate, '
                      'quinoa, pasta fría', ENSALADAS):
        cambios.append('«Buffet Almuerzo»: desinfección con dosis y aclarado '
                       'sólo para los vegetales que se sirven crudos — '
                       'DOM-26 (equivalente)')
    if _insertar_tras(ws, 'Montar estación de entrantes fríos: gazpacho, '
                          'carpaccio, salmón', ANISAKIS_ALMUERZO):
        cambios.append('«Buffet Almuerzo»: prevención de ANISAKIS en la '
                       'estación de carpaccio y salmón (Rgto. CE 853/2004) — '
                       'DOM-02 (equivalente, ALTA)')
        tocado = True
    if _sustituir(ws, 'Verificar temperaturas: caliente >65°C, frío <5°C '
                      '(registrar APPCC)', TEMP_ALMUERZO):
        cambios.append('«Buffet Almuerzo»: la referencia al APPCC deja de dar '
                       'por hecho que el hotel lo tiene y la tarea deja hueco '
                       'para la lectura — DOM-R2-09 / §2.9')
    _renumerar_p4(ws)
    _dv_extender(ws)

    ws = wb['Buffet Cena']
    if _insertar_tras(ws, 'Montar estación de entrantes premium: foie, tartar, '
                          'ceviche', ANISAKIS_CENA):
        cambios.append('«Buffet Cena»: prevención de ANISAKIS en la estación '
                       'de tartar y ceviche, que es la de mayor riesgo del '
                       'kit — DOM-02 (equivalente, ALTA)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)
    if _instrucciones(wb, 'Pescado crudo y vegetales:', [
            'Tartar, ceviche, carpaccio, salmón marinado o ahumado en frío: '
            'sólo con congelación previa acreditada (≥ 24 h a −20 °C o 15 h a '
            '−35 °C). Es obligación del Reglamento (CE) 853/2004 y en un '
            'buffet de autoservicio el riesgo se multiplica por el número de '
            'comensales.',
            'Los vegetales que se sirven crudos se desinfectan con lejía apta '
            'para uso alimentario a la dosis del fabricante y se ACLARAN con '
            'agua potable abundante; los que se blanquean, no.']):
        cambios.append('Instrucciones: anisakis y desinfección de vegetales — '
                       'DOM-02 / DOM-26')
        tocado = True
    return tocado


# ==========================================================================
# 03-fb-restaurante-carte.xlsx — «Apertura À la Carte»
# ==========================================================================
#: DOM-24 (equivalente) — el à la carte abre a las 16:00 con SUS cámaras y su
#: office, que llevan cerrados desde la noche anterior. La apertura comprobaba
#: la temperatura de la SALA (20-22 °C) y ninguna del frío.
CAMARAS_CARTE = [
    ('Comprobar con cocina que las cámaras y el office del restaurante han '
     'funcionado toda la noche y registrar la temperatura (refrigeración '
     '0-4 °C / congelación ≤ −18 °C) — anota la lectura: ____ °C. Si hay '
     'desviación, no montes el servicio hasta valorarlo', 'Cocina'),
]

#: DOM-19 (equivalente) — consultar la lista de alérgenos no sirve de nada si no
#: llega a quien sirve la mesa: el que responde a la pregunta del cliente es el
#: camarero, no el cartel.
ALERGENOS_CARTE = ('Consultar la lista de alérgenos y peticiones especiales '
                   '(celiaco, vegano) y trasladarlas POR ESCRITO a cocina y al '
                   'camarero que sirve cada mesa antes de abrir')


def _f03(wb, cambios):
    tocado = False
    ws = wb['Apertura À la Carte']
    if _sustituir(ws, 'Consultar lista de alérgenos y peticiones especiales '
                      '(celiaco, vegano)', ALERGENOS_CARTE):
        cambios.append('«Apertura À la Carte»: los alérgenos se trasladan por '
                       'escrito a cocina y al camarero de la mesa, que es '
                       'quien responde — DOM-19 (equivalente)')
    if _insertar_tras(ws, 'Comprobar temperatura de sala (20-22°C) y '
                          'ventilación', CAMARAS_CARTE):
        cambios.append('«Apertura À la Carte»: comprobación nocturna de las '
                       'cámaras y el office del restaurante, con objetivo y '
                       'hueco para la lectura; la apertura sólo miraba la '
                       'temperatura de la SALA — DOM-24 (equivalente)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)
    return tocado


# ==========================================================================
# 04-fb-outlets.xlsx — Pool Bar, Lobby Bar, Snack Bar
# ==========================================================================
#: DOM-15 (equivalente) — el lobby bar sirve café 24 h y su máquina es la que
#: más ciclos hace del hotel. «Limpiar máquina de café» no dice nada de lo
#: único que la mata: el grupo, la ducha y el circuito de leche.
CAFE_LOBBY = ('Limpieza diaria de la máquina de café: backflush del grupo con '
              'detergente específico, cambiar el filtro ciego, purgar y '
              'limpiar la lanza de vapor y el circuito de leche; después, el '
              'resto de equipos de barra')

#: §2.9 — la vitrina de un grab & go es autoservicio y sin vigilancia: la
#: lectura hay que anotarla, no sólo mirarla.
VITRINA_SNACK = ('Verificar temperatura de la vitrina refrigerada (< 5 °C) — '
                 'anota la lectura: ____ °C')

#: DOM-R2-09 — «registrar en hoja APPCC» da por hecho un documento que el hotel
#: puede no tener; y en el molde P4 de este kit sí existe la columna «Notas».
TEMP_SNACK = ('Verificar las temperaturas de cierre — anota la lectura: '
              '____ °C (si tienes el Pack APPCC, regístrala en su hoja de '
              'temperaturas; si no, en la columna «Notas»)')

#: DOM-29 (equivalente) — el pool bar guarda perecedero en cámara sin decir a
#: qué temperatura ni con qué etiqueta; es la hoja que más lejos está del
#: office y la que más rompe la cadena de frío.
CAMARA_POOL = ('Almacenar licores y producto perecedero en cámara '
               '(refrigeración 0-4 °C), tapado, etiquetado y con la fecha del '
               'día')


def _f04(wb, cambios):
    ws = wb['Lobby Bar - Lounge']
    if _sustituir(ws, 'Limpiar máquina de café y equipos de barra', CAFE_LOBBY):
        cambios.append('«Lobby Bar - Lounge»: la limpieza diaria de la máquina '
                       'de café pasa a ser backflush del grupo, filtro ciego, '
                       'lanza de vapor y circuito de leche — DOM-15 '
                       '(equivalente)')
    ws = wb['Snack Bar - Grab Go']
    if _sustituir(ws, 'Verificar temperatura de vitrina refrigerada (<5°C)',
                  VITRINA_SNACK):
        cambios.append('«Snack Bar - Grab Go»: la temperatura de la vitrina '
                       'deja hueco para la lectura — §2.9')
    if _sustituir(ws, 'Verificar temperaturas de cierre y registrar en hoja '
                      'APPCC', TEMP_SNACK):
        cambios.append('«Snack Bar - Grab Go»: la referencia al APPCC deja de '
                       'darse por hecha y se ofrece la columna «Notas» — '
                       'DOM-R2-09')
    ws = wb['Pool Bar']
    if _sustituir(ws, 'Almacenar licores y producto perecedero en cámara',
                  CAMARA_POOL):
        cambios.append('«Pool Bar»: el almacenamiento lleva temperatura, '
                       'tapado y fecha — DOM-29 (equivalente)')
    return False


# ==========================================================================
# 06-fb-banquetes-eventos.xlsx — «Banquetes y Eventos»
# ==========================================================================
#: DOM-19 (equivalente) — el kit SÍ nombraba los alérgenos, pero mezclados en
#: una sola tarea con «menú definitivo» y «distribución de mesas», y ya dentro
#: de la coordinación PRE-EVENTO, es decir, cuando el precio y las condiciones
#: llevan meses cerrados. Lo que hay que blindar por escrito se decide al
#: confirmar la reserva, y en un banquete de 200 comensales el que se olvida no
#: es el cocinero: es el contrato.
RESERVA = 'Al confirmar la reserva del evento'
RESERVA_TAREAS = [
    ('Recoger POR ESCRITO alérgenos, intolerancias y dietas especiales '
     '(religiosas, veganas, infantiles) con nombre y mesa de cada comensal',
     'Admin'),
    ('Cerrar con el cliente el nº de comensales garantizado y la fecha límite '
     'para modificarlo', 'Admin'),
    ('Cerrar por escrito el precio por comensal y QUÉ incluye: barra libre, '
     'recena, descorche, montaje, personal extra y horas de más', 'Admin'),
    ('Cerrar las condiciones de cancelación, la señal y el calendario de '
     'pagos, y guardarlo firmado con el BEO', 'Admin'),
    ('Confirmar por escrito los menús alternativos y quién los sirve: el plato '
     'especial sale identificado desde cocina', 'Cocina'),
    ('Comprobar aforo del salón, salidas de emergencia y seguro de '
     'responsabilidad civil para el formato contratado', 'Admin'),
]

MENU_DEFINITIVO = ('Confirmar con cocina el menú definitivo y la distribución '
                   'de mesas, y repasar los alérgenos ya recogidos al '
                   'confirmar la reserva contra el plano de sala')

ALERGENOS_MONTAJE = [
    ('Marcar en el plano de sala las posiciones con menú especial o alérgeno y '
     'asignar quién sirve cada una: el plato alternativo sale marcado desde '
     'cocina y no se cruza con el resto del pase', 'Banquetes'),
]


def _f06(wb, cambios):
    tocado = False
    ws = wb['Banquetes y Eventos']
    if _insertar_seccion(ws, 'Coordinación pre-evento', RESERVA,
                         RESERVA_TAREAS):
        cambios.append('«Banquetes y Eventos»: sección nueva «{0}» ({1} '
                       'tareas) delante de la coordinación pre-evento: '
                       'alérgenos por escrito con mesa, nº garantizado, precio '
                       'por comensal y qué incluye, condiciones de cancelación '
                       'y aforo — DOM-19 (equivalente)'
                       .format(RESERVA, len(RESERVA_TAREAS)))
        tocado = True
    if _sustituir(ws, 'Confirmar menú definitivo, alérgenos y distribución de '
                      'mesas', MENU_DEFINITIVO):
        cambios.append('«Banquetes y Eventos»: la tarea de menú deja de ser el '
                       'único sitio donde aparecen los alérgenos y pasa a '
                       'REPASAR los que ya se cerraron por escrito — DOM-19')
    if _insertar_tras(ws, 'Colocar centro de mesa, tarjetas de asiento y menú '
                          'impreso', ALERGENOS_MONTAJE):
        cambios.append('«Banquetes y Eventos»: en el montaje, las posiciones '
                       'con menú especial se marcan en el plano y tienen '
                       'camarero asignado — DOM-19 (equivalente, lado '
                       'servicio)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)
    if _instrucciones(wb, 'Antes de firmar el evento:', [
            'La primera sección se rellena AL CONFIRMAR LA RESERVA, no el día '
            'del banquete: alérgenos e intolerancias por escrito con nombre y '
            'mesa, nº de comensales garantizado, precio por comensal y qué '
            'incluye, condiciones de cancelación y aforo del salón.',
            'El día del evento sólo se REPASAN contra el plano de sala. Cada '
            'posición con menú especial lleva camarero asignado y el plato '
            'sale identificado desde cocina.']):
        cambios.append('Instrucciones: bloque «al confirmar la reserva» — '
                       'DOM-19 (equivalente)')
        tocado = True
    return tocado


# ==========================================================================
# 13-mantenimiento.xlsx — «Mensual» + hoja nueva «Trimestral y Anual»
# ==========================================================================
#: DOM-15 (equivalente) — el hotel tiene cafeteras en el buffet de desayuno, en
#: el lobby bar, en el à la carte y en room service, todas conectadas a la misma
#: agua. La limpieza diaria la hace el barista (01 y 04); la descalcificación y
#: el cambio de filtros son del técnico y no estaban en ninguna cadencia.
DESCALCIFICAR = [
    ('Descalcificar las cafeteras y los termos de agua de todos los outlets '
     '(buffet, lobby bar, à la carte, room service) o contratar la revisión al '
     'SAT, y cambiar los filtros descalcificadores del agua de aporte — anota '
     'la fecha y el nº de parte', 'Mantenimiento'),
]

HOJA_LEGAL = 'Trimestral y Anual'
TITULO_LEGAL = 'Mantenimiento Trimestral y Anual — Revisiones Contratadas'
#: DOM-16 (equivalente) — el fichero 13 tenía las cadencias diaria, semanal y
#: mensual y tres hojas por gremio (HVAC, fontanería, electricidad), pero
#: ninguna capa de lo que se CONTRATA y se pide por escrito en una inspección:
#: DDD, conductos de extracción, legionela, OCA de baja tensión, ascensores,
#: RITE, extintores, gas, seguros y formación. En un hotel esa capa no es un
#: extra: es la mitad de lo que mira quien viene a inspeccionar.
#: El último bloque es el que hereda las filas de la hoja clonada.
LEGAL = [
    ('Higiene alimentaria y control de plagas', [
        ('Control de plagas (DDD) de cocinas, almacenes y zonas comunes por '
         'empresa autorizada: visita, parte firmado y certificado en vigor',
         'Mantenimiento', 'Trimestral'),
        ('Limpieza de campanas y conductos de extracción de las cocinas por '
         'empresa homologada, con certificado', 'Mantenimiento', 'Anual'),
        ('Analítica de superficies, manipuladores y producto en laboratorio '
         'externo (verificación del plan de higiene)', 'Mantenimiento',
         'Semestral'),
        ('Revisar el plan APPCC y las fichas de proveedor: altas, bajas y '
         'cambios de carta y de buffet del año', 'Admin', 'Anual'),
        ('Renovar la formación en manipulación de alimentos y en alérgenos de '
         'todo el personal de F&B, extras incluidos', 'Admin', 'Anual'),
        ('Calibrar termómetros y sondas de cámaras, buffet y room service '
         'contra un patrón conocido (agua con hielo, 0 °C) y anotar la '
         'desviación', 'Mantenimiento', 'Trimestral'),
    ]),
    ('Agua, legionela, piscina y spa', [
        ('Limpieza y desinfección de ACS, aljibes y torres de refrigeración '
         'por empresa autorizada, con certificado (plan de prevención de '
         'legionelosis, RD 487/2022)', 'Mantenimiento', 'Semestral'),
        ('Analítica de legionela en laboratorio acreditado y registro en el '
         'libro de mantenimiento', 'Mantenimiento', 'Trimestral'),
        ('Revisar la temperatura de ACS en puntos terminales (> 50 °C) y '
         'purgar los de las habitaciones que llevan tiempo fuera de servicio',
         'Mantenimiento', 'Trimestral'),
        ('Analítica del agua de piscina y spa en laboratorio autorizado, '
         'además del control diario de cloro y pH', 'Mantenimiento',
         'Trimestral'),
        ('Vaciado, limpieza a fondo y revisión del vaso, la depuradora y las '
         'duchas de piscina y spa', 'Mantenimiento', 'Anual'),
    ]),
    ('Instalaciones, incendios y seguridad', [
        ('Revisión de extintores, BIE y sistema de detección por empresa '
         'mantenedora autorizada (etiqueta y acta)', 'Mantenimiento',
         'Trimestral'),
        ('Retimbrado de extintores y prueba de presión de las BIE',
         'Mantenimiento', 'Cada 5 años'),
        ('Revisión de la instalación de gas de las cocinas por empresa '
         'habilitada, con certificado', 'Mantenimiento', 'Cada 5 años'),
        ('Inspección de la instalación eléctrica de baja tensión por OCA '
         '(organismo de control autorizado)', 'Mantenimiento', 'Cada 5 años'),
        ('Inspección periódica de ascensores y montacargas por OCA, además '
         'del contrato de mantenimiento mensual', 'Mantenimiento',
         'Cada 2 años'),
        ('Revisión de la instalación térmica (RITE): calderas, enfriadoras y '
         'ACS, con el certificado de mantenimiento', 'Mantenimiento', 'Anual'),
        ('Simulacro de evacuación y repaso del plan de autoprotección con '
         'todos los turnos', 'Admin', 'Anual'),
        ('Retirada de residuos peligrosos y de aceite usado de cocina por '
         'gestor autorizado, y archivo del documento de entrega',
         'Mantenimiento', 'Trimestral'),
    ]),
    ('Documentación, seguros y personal', [
        ('Revisar las pólizas de responsabilidad civil y de continente y '
         'contenido: sumas aseguradas, aforos y actividades cubiertas',
         'Admin', 'Anual'),
        ('Archivar los registros de jornada del trimestre y revisar contratos '
         'y altas del personal eventual', 'Admin', 'Trimestral'),
        ('Revisión del PMS, del TPV y del software de facturación (requisitos '
         'antifraude / Verifactu)', 'Admin', 'Anual'),
        ('Renovar licencias y seguros obligatorios: actividad, ocupación, '
         'piscina y, si procede, terraza', 'Admin', 'Anual'),
        ('Actualizar escandallos, precios de carta y tarifas de banquete con '
         'los precios reales de proveedor', 'Admin', 'Trimestral'),
        ('Anotar en «Notas» el nº de parte de cada revisión y la fecha de la '
         'siguiente', 'Admin', 'Trimestral'),
    ]),
]


def _bloques_p4(ws, g):
    """[(fila de banda, fila de cabecera, [filas de tarea]), …] del molde P4."""
    tope = g['contador'] or ws.max_row + 1
    fuera = []
    for r in range(g['hr'] - 1, tope):
        if not motor.es_fila_seccion(ws, r):
            continue
        cab = r + 1 if ws.cell(row=r + 1, column=2).value == 'Tarea' else None
        filas = []
        for x in range((cab or r) + 1, tope):
            if motor.es_fila_seccion(ws, x):
                break
            if isinstance(ws.cell(row=x, column=1).value, int):
                filas.append(x)
            elif filas:
                break
        fuera.append((r, cab, filas))
    return fuera


def _hoja_legal(wb, cambios):
    """Crea «Trimestral y Anual» clonando «Mensual» y montando 4 bloques.

    Se clona en lugar de construirse a mano porque el clon trae anchos, alturas,
    bordes, combinaciones y la geometría exacta del molde P4; lo que NO trae
    (medido con openpyxl) son el desplegable, el pie de impresión y los paneles
    inmovilizados, y por eso se le aplican aquí uno a uno.

    «Mensual» tiene UN bloque de 8 filas: hereda el último de `LEGAL` (se le
    recortan o añaden filas) y los otros tres se insertan delante, en orden.
    """
    if HOJA_LEGAL in wb.sheetnames:
        return False
    modelo = wb['Mensual']
    ws = wb.copy_worksheet(modelo)
    ws.title = HOJA_LEGAL
    ws.cell(row=1, column=1).value = TITULO_LEGAL
    g = motor.geometria_p4(ws)
    if not g:
        raise AnclaPerdida('«Mensual»: el clon no es del molde P4')
    bloques = _bloques_p4(ws, g)
    if len(bloques) != 1:
        raise AnclaPerdida('«Mensual» tiene {0} bloques y se esperaba 1'
                           .format(len(bloques)))
    banda, cab, filas = bloques[0]
    if cab is None:
        raise AnclaPerdida('«Mensual»: el clon perdió la fila de cabecera')
    # La columna F deja de ser «Hora» y pasa a ser «Cadencia» ANTES de insertar
    # las otras secciones: `_insertar_seccion` copia la cabecera de ésta, así
    # que renombrarla después dejaría tres cabeceras diciendo «Hora».
    ws.cell(row=cab, column=6).value = 'Cadencia'
    titulo_ultimo, tareas_ultimo = LEGAL[-1]
    sobra = len(filas) - len(tareas_ultimo)
    if sobra > 0:
        motor.eliminar_filas(ws, filas[len(tareas_ultimo)], sobra)
    elif sobra < 0:
        est = _estilos(ws, filas[-1])
        motor.insertar_filas(ws, filas[-1] + 1, -sobra)
        for i in range(-sobra):
            _pintar(ws, filas[-1] + 1 + i, est)
    ws.cell(row=banda, column=1).value = titulo_ultimo
    for i, tarea in enumerate(tareas_ultimo):
        r = filas[0] + i
        ws.cell(row=r, column=1).value = 0
        ws.cell(row=r, column=2).value = tarea[0]
        _zona(ws, r, tarea[1])
        ws.cell(row=r, column=4).value = None
        ws.cell(row=r, column=6).value = tarea[2]
    for titulo, tareas in LEGAL[:-1]:
        if not _insertar_seccion(ws, titulo_ultimo, titulo, tareas):
            raise AnclaPerdida('«{0}»: no pude insertar el bloque «{1}»'
                               .format(HOJA_LEGAL, titulo))
    _renumerar_p4(ws)
    # Desplegable: el clon no hereda ninguno.
    dv = motor.DataValidation(
        type='list', formula1=motor.DV_LISTA, allow_blank=True,
        showErrorMessage=True, errorStyle='stop',
        errorTitle=motor.DV_ERROR_TIT, error=motor.DV_ERROR)
    ws.add_data_validation(dv)
    _dv_extender(ws)
    if not dv.sqref.ranges:
        raise AnclaPerdida('«{0}»: el desplegable quedó vacío'
                           .format(HOJA_LEGAL))
    # A4 + pie + fila de cabecera repetida al imprimir: `motor.cerrar` no corre
    # sobre el molde P4, así que sin esto la hoja nueva saldría del censo como
    # «noprint» (paperSize/fitToPage/pie son tres de sus comprobaciones).
    g = motor.geometria_p4(ws)
    motor.print_setup(ws, g['hr'], landscape=True)
    # La hoja va detrás de «Mensual», que es su cadencia anterior; `copy_worksheet`
    # la deja al final, después de las tres hojas por gremio.
    wb.move_sheet(ws, offset=wb.sheetnames.index('HVAC')
                  - wb.sheetnames.index(HOJA_LEGAL))
    n = sum(len(t) for _t, t in LEGAL)
    cambios.append('hoja nueva «{0}» en 13 ({1} tareas): mantenimiento y '
                   'documentación que se CONTRATA y que pide una inspección '
                   '(DDD, conductos, legionela y RD 487/2022, analíticas de '
                   'piscina y spa, extintores y BIE, gas, OCA de baja tensión, '
                   'ascensores, RITE, simulacro, residuos, pólizas, licencias '
                   'y Verifactu) — DOM-16 (equivalente); el kit sólo tenía '
                   'cadencias diaria, semanal y mensual'
                   .format(HOJA_LEGAL, n))
    return True


def _f13(wb, cambios):
    tocado = False
    ws = wb['Mensual']
    if _insertar_tras(ws, 'Revisar equipos de cocina industrial y campanas '
                          'extractoras', DESCALCIFICAR):
        cambios.append('«Mensual»: descalcificación de las cafeteras y los '
                       'termos de todos los outlets y cambio de filtros de '
                       'agua, que no estaba en ninguna cadencia — DOM-15 '
                       '(equivalente); la limpieza DIARIA del grupo va en 01 '
                       'y en 04, donde está la máquina')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)
    if _hoja_legal(wb, cambios):
        tocado = True
    # El rótulo de las Instrucciones promete un número de checklists: si no se
    # actualiza, el fichero se contradice a sí mismo en la primera línea.
    if 'Instrucciones' in wb.sheetnames:
        wsi = wb['Instrucciones']
        viejo = ('▸ 6 checklists: ronda diaria, semanal, mensual, HVAC, '
                 'fontanería, electricidad.')
        nuevo = ('▸ 7 checklists: ronda diaria, semanal, mensual, trimestral y '
                 'anual, HVAC, fontanería, electricidad.')
        r = _fila(wsi, viejo)
        if r:
            wsi.cell(row=r, column=2).value = nuevo
            cambios.append('Instrucciones: el rótulo dice 7 checklists, que '
                           'son los que hay tras añadir «{0}»'
                           .format(HOJA_LEGAL))
    if _instrucciones(wb, 'Más allá del mes:', [
            'La hoja «Trimestral y Anual» recoge lo que se CONTRATA y se pide '
            'por escrito en una inspección: DDD, conductos de extracción, '
            'legionela (RD 487/2022), analíticas de piscina y spa, extintores '
            'y BIE, instalación de gas, OCA de baja tensión, ascensores, RITE, '
            'simulacro de evacuación, residuos, pólizas, licencias y '
            'facturación.',
            'La columna «Cadencia» ya trae la periodicidad legal o recomendada '
            'de cada revisión; anota en «Notas» el número de parte y la fecha '
            'de la siguiente.',
            'La descalcificación de cafeteras y termos es mensual y va en la '
            'hoja «Mensual»; la limpieza diaria del grupo de café la hace quien '
            'usa la máquina, en 01 (buffet) y en 04 (lobby bar).']):
        cambios.append('Instrucciones: hoja «Trimestral y Anual» y reparto de '
                       'la limpieza del café — DOM-16 / DOM-15 (equivalentes)')
        tocado = True
    return tocado


# ==========================================================================
# 14-administracion.xlsx — «RRHH Operativo»
# ==========================================================================
#: DOM-17 (equivalente) — el registro horario es obligatorio en España desde el
#: RD-ley 8/2019 y hay que conservarlo 4 años a disposición de la Inspección de
#: Trabajo. El kit tenía la tarea diaria («controlar fichaje») pero ninguna de
#: cerrarlo, validarlo ni archivarlo, que es lo que se pide cuando llega la
#: Inspección. En un hotel el problema se agrava: turnos partidos, extras de
#: banquete y noches que cruzan el cambio de día.
FICHAJE = ('Cerrar y validar el registro de jornada del día (entradas, salidas '
           'y pausas) de todo el personal, extras de banquete y turnos de '
           'noche incluidos')

JORNADA_ARCHIVO = [
    ('Archivar el registro de jornada del mes cerrado (en papel o exportado '
     'del sistema de fichaje): hay que conservarlo 4 años a disposición de la '
     'Inspección de Trabajo', 'RRHH'),
]


def _f14(wb, cambios):
    tocado = False
    ws = wb['RRHH Operativo']
    if _sustituir(ws, 'Controlar fichaje de entrada/salida de todo el '
                      'personal', FICHAJE):
        cambios.append('«RRHH Operativo»: el fichaje se CIERRA y se VALIDA a '
                       'diario, con extras de banquete y turnos de noche '
                       'nombrados — DOM-17 (equivalente)')
    if _insertar_tras(ws, 'Gestionar incidencias de nómina: horas extra, '
                          'complementos, dietas', JORNADA_ARCHIVO):
        cambios.append('«RRHH Operativo»: archivo mensual del registro de '
                       'jornada, con la obligación de conservarlo 4 años '
                       '(RD-ley 8/2019), que no estaba en ningún fichero — '
                       'DOM-17 (equivalente)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)
    if _instrucciones(wb, 'Registro de jornada:', [
            'El registro horario es obligatorio (RD-ley 8/2019) y hay que '
            'conservarlo 4 AÑOS a disposición de la Inspección de Trabajo. En '
            '«RRHH Operativo» se cierra y se valida cada día, y se archiva al '
            'cerrar el mes.',
            'La revisión trimestral de contratos y del archivo de jornada está '
            'en la hoja «Trimestral y Anual» del fichero 13.']):
        cambios.append('Instrucciones: registro de jornada y su custodia — '
                       'DOM-17 (equivalente)')
        tocado = True
    return tocado


# ==========================================================================
# BONUS-02 — calendario anual F&B del hotel
# ==========================================================================
#: El calendario de hotel es, con el de catering, uno de los dos ficheros que el
#: motor no ve: `motor.fila_calendario` exige la pareja «Antelación» + una
#: columna de EVENTO, y esta cabecera es «Fecha / Período | Impacto». Se queda
#: sin contador y sin CF, pero `normalizar_p4` sí le pone la bio y la versión.
#:
#: DOM-20 (equivalente) — de las cinco fechas del representante, el 15 de agosto
#: ya está cubierto («Jul-Ago — Verano pleno», que en un hotel vacacional es el
#: pico de ocupación, y «Festivos locales»). Faltaban las otras cuatro, y en un
#: hotel las dos de puente pesan más que en un restaurante: son estancias, no
#: cubiertos.
FECHAS = [
    ('Marzo — Semana Santa',
     ('19 Mar — Día del Padre', 'Almuerzo familiar',
      'Almuerzo de mediodía y brunch familiar; tarta por encargo y paquete '
      'con alojamiento', '3 semanas')),
    ('Abril — Temporada media',
     ('Abr-Jun — Comuniones', 'Banquetes pico',
      'Menú de adultos e infantil cerrados, salón, photocall y barra libre '
      'infantil; se contratan con 3-6 meses', '3 meses')),
    ('Octubre — Halloween',
     ('1 Nov — Puente de Todos los Santos', 'Ocupación alta',
      'Primer puente de la temporada baja: escapada nacional de 3 noches, '
      'buffet reforzado y menú de temporada (caza, setas)', '4 semanas')),
    ('Nov — Black Friday gastro',
     ('6-8 Dic — Puente de la Constitución', 'Ocupación alta',
      'Tres días seguidos con cenas de empresa adelantadas: buffet reforzado, '
      'salones dobles y personal extra cerrado ANTES del puente', '6 semanas')),
]


def _bonus02(wb, cambios):
    ws = wb['Calendario']
    tocado = False
    nuevas = 0
    for ancla, fila in FECHAS:
        fecha, impacto, prep, antelacion = fila
        if _fila(ws, fecha) is not None:
            continue
        r = _exige(ws, ancla)
        est = _estilos(ws, r, ncol=NCOL_CAL)
        motor.insertar_filas(ws, r + 1, 1)
        _pintar(ws, r + 1, est)
        ws.cell(row=r + 1, column=1).value = 0
        ws.cell(row=r + 1, column=2).value = fecha
        _zona(ws, r + 1, impacto)
        ws.cell(row=r + 1, column=4).value = prep
        ws.cell(row=r + 1, column=5).value = antelacion
        nuevas += 1
        tocado = True
    total = 0
    for r in range(1, ws.max_row + 1):
        if isinstance(ws.cell(row=r, column=1).value, int):
            total += 1
            ws.cell(row=r, column=1).value = total
    if nuevas:
        cambios.append('«Calendario»: {0} fechas que faltaban (Día del Padre, '
                       'comuniones, puente de Todos los Santos y puente de '
                       'diciembre; el 15 de agosto ya estaba cubierto por '
                       '«Jul-Ago — Verano pleno») — DOM-20 (equivalente)'
                       .format(nuevas))
    # El rótulo y las Instrucciones prometen un número concreto de fechas: si
    # no se actualiza, el fichero se contradice a sí mismo en la primera línea.
    sub = ws.cell(row=2, column=1)
    nuevo = ('AI Chef Pro · aichef.pro — {0} fechas clave para F&B hotelero'
             .format(total))
    if isinstance(sub.value, str) and sub.value != nuevo:
        sub.value = nuevo
        cambios.append('«Calendario»: el subtítulo dice {0} fechas, que son '
                       'las que hay'.format(total))
    if 'Instrucciones' in wb.sheetnames:
        wsi = wb['Instrucciones']
        linea = ('▸ Las {0} fechas y temporadas clave para F&B en hoteles.'
                 .format(total))
        for r in range(1, wsi.max_row + 1):
            v = wsi.cell(row=r, column=2).value
            if isinstance(v, str) and v.startswith('▸ Las ') and \
                    v.endswith('clave para F&B en hoteles.'):
                if v != linea:
                    wsi.cell(row=r, column=2).value = linea
                    cambios.append('Instrucciones: el recuento de fechas pasa '
                                   'a {0}'.format(total))
                break
    return tocado


# ==========================================================================
# API
# ==========================================================================
FICHEROS = {
    '01-fb-buffet-desayuno.xlsx': _f01,
    '02-fb-buffet-comida-cena.xlsx': _f02,
    '03-fb-restaurante-carte.xlsx': _f03,
    '04-fb-outlets.xlsx': _f04,
    '06-fb-banquetes-eventos.xlsx': _f06,
    '13-mantenimiento.xlsx': _f13,
    '14-administracion.xlsx': _f14,
    'BONUS-02-calendario-anual-tareas.xlsx': _bonus02,
}


def post(wb, fname, cambios):
    """CONTENIDO sobre un libro ya normalizado por `motor.aplicar`.

    Devuelve True si ha cambiado la ESTRUCTURA. En el molde P4 ese valor no lo
    usa `main.py` (no hay 2.ª pasada del motor porque `aplicar` devolvió `{}`),
    así que la reconstrucción del contador, del formato condicional y del
    desplegable se hace AQUÍ antes de salir.
    """
    # 18 y 19 son del molde ▸ y los lleva el motor de punta a punta: si este
    # módulo entrase ahí, el `motor.REGISTRO.clear()` de abajo se llevaría por
    # delante las 81 fórmulas del arqueo que `aplicar` acababa de registrar y
    # `main.py` dejaría de verificar su cache. La detección es ESTRUCTURAL
    # (cabecera «✓ Completada»), no por nombre de fichero.
    if motor.hojas_reconocidas(wb):
        return False
    fn = FICHEROS.get(fname)
    tocado = bool(fn(wb, cambios)) if fn else False
    for ws in wb.worksheets:
        _normalizar_grados(ws, cambios)
    # Contador honesto y formato condicional con la geometría NUEVA. Es
    # idempotente: en la 2.ª pasada `motor.aplicar` ya lo dejó así y esto no
    # encuentra nada que cambiar.
    #
    # El registro se vacía ANTES porque las coordenadas que anotó `aplicar` son
    # las de la geometría VIEJA: al insertar la sección de higiene en «Apertura
    # Desayuno» el contador bajó de la fila 52 a la 62 y `main.py` seguía
    # preguntando por el cache de C52 —una celda que ahora es una tarea— y lo
    # declaraba «fórmula sin valor». Lo único que hay en el registro de un
    # fichero P4 son los contadores, y `normalizar_p4` los vuelve a registrar
    # todos con su coordenada actual.
    motor.REGISTRO.clear()
    motor.normalizar_p4(wb, cambios)
    return tocado
