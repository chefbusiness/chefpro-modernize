#!/usr/bin/env python3
"""
contenido_kit_tareas_restaurante_creativo.py — CONTENIDO propio de
«kit-tareas-restaurante-creativo» (hermano de la familia, §5 de
`kit-tareas-v2-SPEC.md`).

Fuente de los cambios: `auditorias/kit-tareas-hermanos/
kit-tareas-restaurante-creativo-verif.json`, campo `contenido_pendiente`
(1 alta + 1 media + 1 baja que NO llevan la marca «(motor)») más los
equivalentes de §3 del representante que aplican a un restaurante creativo /
de autor con menú degustación.

`main.py` lo carga sólo con `--producto kit-tareas-restaurante-creativo`
(compone el nombre del módulo con el pid), así que aquí se puede hablar de
«Pre-elab Día», «Partida Fría» o «Cenas Especiales» por su nombre: son hojas
de ESTE kit.

Contrato con `main.py`:
    post(wb, fname, cambios) -> bool

ESTE KIT ES DE MOLDE P4 EN 11 DE SUS 13 FICHEROS
================================================================================
`motor.aplicar` sólo reconoce el molde «▸» en 10-apertura-cierre-negocio.xlsx y
11-apertura-cierre-caja.xlsx. Los 01-09 y los dos BONUS son molde P4 y reciben
únicamente `motor.normalizar_p4` (desplegable «✓,—,N/A», contador honesto,
formato condicional y bio). En consecuencia, para los ficheros que toca este
módulo:

  · `motor.aplicar` devuelve `{}` (falsy), así que `main.py` **NO vuelve a
    pasar el motor** tras `post()` ni llama a `motor.cerrar`. Todo lo que
    dependa de la geometría nueva —rango del contador, formato condicional,
    desplegable de las filas nuevas, A4 y pie de una hoja nueva— lo tiene que
    dejar hecho este módulo. Por eso `post()` termina llamando a
    `motor.normalizar_p4` y por eso existen `_dv_extender` y `_hoja_legal`.
  · `motor.textos_de_tarea` (y con él `texto_grados`, `texto_appcc` y
    `texto_temperatura`) tampoco corre sobre P4: medido en
    `02-mise-en-place-degustacion.xlsx:Pre-elab Medio:B6`, que sigue con
    «63°C» en la forma sin espacio después del motor. La normalización
    transversal de grados (DOM-R2-22) la aplica aquí `_normalizar_grados`, al
    FINAL de cada fichero, y todos los textos nuevos de este módulo ya se
    escriben en su forma final para que la 2.ª pasada no encuentre nada que
    cambiar.
  · el molde P4 REPITE la fila de cabecera («# | Tarea | Zona | Responsable |
    ✓ | Hora | Notas») en cada sección y **reinicia la numeración en 1**
    dentro de cada bloque (medido en `01:Apertura AM`: 1-8, 1-8, 1-8).
    `motor.renumerar` va por `motor.geometria`, que es del molde ▸ y devuelve
    None aquí: la numeración la rehace `_renumerar_p4`.
  · las columnas «Responsable» y «Hora» van VACÍAS en todo el molde P4 de este
    kit (son verdes, las rellena el cliente). Las tareas nuevas respetan eso y
    sólo escriben #, Tarea y Zona. La única excepción documentada es la hoja
    nueva «Trimestral y Anual», donde la CADENCIA es el dato y ocupa la
    columna F.
  · el color de la columna «Zona» depende del VALOR (medido: Cocina FFF3E0,
    I+D E8EAF6, Cámara E8F5E9, Admin FFF8E1, Limpieza EFEBE9, Eventos
    E0F7FA…). Copiar el estilo de la fila de anclaje pinta la zona
    equivocada, así que `_zona` busca una fila con esa zona —primero en la
    hoja, después en TODO el libro— y le copia el relleno.

DÓNDE VAN LOS HALLAZGOS Y POR QUÉ
================================================================================
El nombre de los ficheros de este kit SÍ describe su contenido (comprobado
hoja a hoja), pero la numeración no coincide con la del representante:

  01-apertura-cierre.xlsx            → «Apertura AM» / «Cierre PM» de cocina
                                       y sala (el «01» del representante)
  02-mise-en-place-degustacion.xlsx  → pre-elaboraciones por tiempo + plating
                                       bible (el «02» de fríos/mise en place)
  03-id-desarrollo-menu.xlsx         → I+D. NO es el «03 Manager»: aquí no hay
                                       gestión de personal ninguna
  05-tareas-semanales-mensuales.xlsx → el «05» del representante, tal cual
  07-chefs-table-eventos.xlsx        → el «06 Eventos» del representante
  09-plantilla-personalizable.xlsx   → el «07» del representante. Sus tres
                                       hojas se entregaban EN BLANCO (DOM-07)
                                       y, después, con las MISMAS tres filas
                                       de ejemplo: el motor no puede llenarlas
                                       —no sabe de qué va el kit— ni las
                                       reconoce (se llaman «Plantilla A/B/C»,
                                       no «Por Franja Horaria»…), así que el
                                       eje de cada hoja y sus ejemplos los
                                       pone este módulo (`_f09` / `EJES`)

Por eso:
  · el registro diario de jornada (DOM-17) va al cierre de 01, que es la única
    hoja del kit que cierra el día con la brigada dentro, y su archivo mensual
    al bloque de finanzas de 05 — NO al 03, que es un libro de I+D donde
    nadie ficha;
  · la tabla de vida útil en congelación (DOM-29) va al pie de 05
    «Semanales», que es el fichero que el propio hallazgo señala y donde vive
    el inventario y la rotación de stock;
  · la hoja «Trimestral y Anual» (DOM-16) se crea en 05, que es el libro de
    CADENCIAS del kit (el representante la pone en su 03 porque allí el 03 es
    el libro del manager; aquí ese papel no existe).

TODA TAREA NUEVA SE CRUZA CONTRA LAS VIEJAS DE SU HOJA
================================================================================
Insertar una sección nueva DELANTE de una vieja no es sólo añadir: si la vieja
cubre el mismo hecho, el cliente se encuentra dos casillas para una sola cosa y
marca las dos. Le pasó a «Cenas Especiales» (07): la sección «AL CONFIRMAR LA
RESERVA» pedía los alérgenos por escrito y nueve filas más abajo seguía viva
«Alérgenos y preferencias confirmados», que es la misma cosa dicha peor.

La regla del módulo, aplicada a todas sus inserciones:

  · la tarea vieja NO se borra —descuadraría el contador y el cliente que ya
    usa la hoja perdería su fila—: se REESCRIBE en el momento del ciclo que la
    nueva no cubre (pactar → producir → cotejar en el pase → facturar);
  · el cruce se hace contra TODA la hoja, no contra las filas contiguas, y
    contra las otras hojas del mismo fichero cuando el título de la sección
    nueva las nombra (por eso «Chef's Table» dejó de confirmar comensales y
    alérgenos por segunda vez: la sección nueva dice «cena privada, evento o
    chef's table»);
  · dos tareas del mismo tema NO son un duplicado si son actos distintos:
    «Verificar flores comestibles (frescura, color)» y desinfectarlas conviven,
    igual que «cargar N2O según el menú» y «guardar los cartuchos en vertical
    lejos del calor». Lo que no puede haber es el MISMO control dos veces.
"""
import copy

import motor
from motor import get_column_letter as L

#: Los 11 ficheros de molde P4 de este kit son A:G; el calendario, A:F.
NCOL = 7

#: Relleno de la columna «Zona» por valor, MEDIDO sobre los 13 ficheros del
#: kit (censo de la copia del dry-run). Se usa sólo como respaldo: `_zona`
#: prefiere copiar el estilo de una fila real con esa misma zona, que además
#: trae bordes, fuente y alineación.
ZONA_COLOR = {
    'Cocina': 'FFF3E0', 'Frío': 'FFF3E0', 'Caliente': 'FFF3E0',
    'Emplatado': 'FFF3E0', 'Mise en place': 'FFF3E0', 'Pase': 'FFF3E0',
    'I+D': 'E8EAF6', 'Fichas': 'E8EAF6', 'Técnica': 'E8EAF6',
    'Cámara': 'E8F5E9', 'Stock': 'E8F5E9', 'Proveedores': 'E8F5E9',
    'Admin': 'FFF8E1', 'Food cost': 'FFF8E1',
    'Limpieza': 'EFEBE9', 'Pastelería': 'FCE4EC', 'Petit fours': 'FCE4EC',
    'Bodega': 'F3E5F5', 'Sumiller': 'F3E5F5', 'Maridaje': 'F3E5F5',
    'Sala': 'E3F2FD', 'Maître': 'E3F2FD', 'Camarero': 'E3F2FD',
    'Servicio': 'E3F2FD', 'Storytelling': 'E3F2FD',
    'Eventos': 'E0F7FA', "Chef's table": 'E0F7FA',
    'Fotografía': 'F1F8E9', 'RRSS': 'F1F8E9', 'Prensa': 'F1F8E9',
    'Marketing': 'F1F8E9',
}


class AnclaPerdida(RuntimeError):
    """El texto que este módulo esperaba encontrar ya no está en la hoja."""


# ==========================================================================
# Utilidades de anclaje
# ==========================================================================
def _norm(v):
    """Texto comparable: la normalización de grados que este módulo aplica.

    Así el mismo ancla vale en la 1.ª pasada (texto original, «63°C») y en la
    2.ª (texto ya normalizado, «63 °C»).
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
        raise AnclaPerdida('«{}»: no encuentro {}=«{}» '
                           '(kit-tareas-restaurante-creativo)'
                           .format(ws.title, L(col), texto))
    return r


def _estilos(ws, fila, ncol=NCOL):
    return [copy.copy(ws.cell(row=fila, column=c)._style)
            for c in range(1, ncol + 1)]


def _pintar(ws, fila, estilos):
    for c, st in enumerate(estilos, start=1):
        ws.cell(row=fila, column=c)._style = copy.copy(st)


def _zona(ws, fila, valor):
    """Escribe la Zona y le pone el relleno que esa zona tiene en el kit.

    Primero busca en la propia hoja; si no la encuentra —el caso de la hoja
    nueva «Trimestral y Anual», clonada de «Mensuales», que no tiene ni
    «Cámara» ni «Stock»— busca en el resto del libro antes de caer al mapa de
    colores medidos.
    """
    cel = ws.cell(row=fila, column=3)
    cel.value = valor
    hojas = [ws] + [h for h in ws.parent.worksheets if h is not ws]
    for hoja in hojas:
        for r in range(1, hoja.max_row + 1):
            if hoja is ws and r == fila:
                continue
            otra = hoja.cell(row=r, column=3)
            if otra.value == valor and otra.fill is not None and \
                    otra.fill.fill_type == 'solid':
                cel._style = copy.copy(otra._style)
                return
    color = ZONA_COLOR.get(valor)
    if color:
        motor._relleno(cel, color)


def _escribir_tarea(ws, fila, texto, zona):
    """Fila de tarea del molde P4: # (lo pone `_renumerar_p4`), Tarea y Zona.

    «Responsable» y «Hora» se dejan vacías a propósito: en este kit son celdas
    verdes que el cliente rellena, y ninguna de las tareas del molde P4 viene
    precargada.
    """
    ws.cell(row=fila, column=1).value = 0
    ws.cell(row=fila, column=2).value = texto
    _zona(ws, fila, zona)


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
    for i, (texto, zona) in enumerate(tareas):
        _pintar(ws, r + 1 + i, est)
        _escribir_tarea(ws, r + 1 + i, texto, zona)
    return True


def _insertar_seccion(ws, antes_de, titulo, tareas):
    """Sección nueva del molde P4: banda + fila de cabecera + tareas.

    En P4 CADA sección repite su fila de cabecera; omitirla dejaría el bloque
    huérfano visualmente y, sobre todo, descuadraría el contador, cuyo
    denominador resta `COUNTIF(B,"Tarea")` dando por hecho que hay una
    cabecera por sección.
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
    motor._merge(ws, 'A{}:{}{}'.format(idx, L(NCOL), idx))
    _pintar(ws, idx + 1, est_cab)
    for c, v in enumerate(cabecera, start=1):
        ws.cell(row=idx + 1, column=c).value = v
    for i, (texto, zona) in enumerate(tareas):
        _pintar(ws, idx + 2 + i, est_tarea)
        _escribir_tarea(ws, idx + 2 + i, texto, zona)
    return True


def _renumerar_p4(ws):
    """Numeración del molde P4: reinicia en 1 en CADA sección.

    `motor.renumerar` no sirve: pasa por `motor.geometria`, que es del molde ▸
    y devuelve None en estas hojas. Y renumerar de corrido rompería el molde:
    las tres secciones de «Apertura AM» van 1-8, 1-8, 1-8.
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
        cambios.append('«{}»: {} temperaturas normalizadas al signo menos '
                       'tipográfico y con espacio antes de la unidad '
                       '(DOM-R2-22, que el motor no aplica al molde P4)'
                       .format(ws.title, n))
    return n


def _instrucciones(wb, encabezado, lineas):
    """Bloque nuevo en «Instrucciones», ENCIMA de la bio y de la versión.

    `motor.reescribir_instrucciones` no corre en el molde P4, así que si el
    bloque se añadiera al final (como en los hermanos ▸) quedaría por debajo
    de la firma del autor y de la línea de versión, que son el cierre de la
    hoja.
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
# 01-apertura-cierre.xlsx — «Apertura AM» y «Cierre PM»
# ==========================================================================
#: DOM-12 + DOM-13 (equivalentes) — la hoja abría el día encendiendo el Roner:
#: la PRIMERA tarea del kit era «Encender baños térmicos / Roner / equipos
#: sous-vide», y en los 13 ficheros no había una sola línea de higiene
#: personal ni una sola mención a la campana o al gas (barrido: cero
#: apariciones de «campana», «gas» salvo el inventario de «butano sopletes»,
#: «uñas», «joyas», «lavado de manos»). Una cocina de vanguardia enciende
#: hornos, sopletes de butano y cargadores de N2O todos los días.
#: Orden interno: persona → campana → gas → fuego.
ARRANQUE = '🧼 APERTURA — HIGIENE PERSONAL Y ARRANQUE SEGURO'
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
    ('Encender la campana extractora y ventilar la cocina ANTES de encender '
     'nada más', 'Cocina'),
    ('Si la cocina tiene gas: abrir la llave general y comprobar que NO huele '
     'a gas; si huele, no enciendas nada, ventila y avisa al mantenedor',
     'Cocina'),
    ('Cartuchos de butano de los sopletes y cargadores de N2O: cerrados, en '
     'vertical y lejos de hornos, salamandra y focos de calor', 'Cocina'),
]

#: DOM-13 (equivalente) — la tarea que encendía el primer equipo del día pasa
#: a decir de qué depende. Es la misma tarea, no una nueva: el cliente que ya
#: usa la hoja la reconoce.
RONER = ('Encender baños térmicos / Roner / equipos sous-vide (sólo después '
         'de la campana y del control del gas)')

#: DOM-24 (equivalente) — «Verificar cámaras de maduración (temp., humedad)»
#: no dice qué se verifica de la NOCHE, que es cuando fallan, ni deja dónde
#: anotar la lectura, ni qué hacer si no cuadra. En un restaurante que madura
#: piezas durante semanas, una noche de avería se lleva el género entero.
CAMARAS_MADURACION = ('Comprobar que las cámaras de maduración han '
                      'funcionado toda la noche: temperatura y humedad dentro '
                      'de tus parámetros — anota la lectura: ____ °C / ____ % '
                      'HR. Si hay desviación, no uses la pieza hasta '
                      'valorarla')

#: DOM-24 (equivalente, la mitad que FALTABA) — la apertura controlaba las
#: cámaras de maduración y NINGUNA cámara frigorífica ni el congelador. El
#: cierre sí las registra (Cierre PM), así que el kit medía la temperatura al
#: acostarse y no al levantarse: justo al revés de donde está el riesgo.
CAMARAS_FRIO = [
    ('Comprobar que las cámaras frigoríficas y el congelador han funcionado '
     'toda la noche y registrar la temperatura (refrigeración 0-4 °C / '
     'congelación ≤ −18 °C) — anota la lectura: ____ °C. Si hay desviación, '
     'no uses el género hasta valorarlo', 'Cámara'),
]

#: §2.9 / DOM-14 (equivalente) — la tarea de cierre pedía «registrar
#: temperaturas» sin decir contra qué se comparan ni dónde se anotan.
CAMARAS_CIERRE = ('Registrar la temperatura de todas las cámaras '
                  'frigoríficas y del congelador (refrigeración 0-4 °C / '
                  'congelación ≤ −18 °C) — anota la lectura: ____ °C')

#: DOM-29 (equivalente) — «Etiquetar TODAS las pre-elaboraciones (fecha, hora,
#: contenido)» no dice hasta cuándo vale lo etiquetado, en un kit que produce
#: a 48-72 h y congela.
ETIQUETAR = ('Etiquetar TODAS las pre-elaboraciones (fecha, hora, contenido) '
             'y anotar la fecha límite de uso: la vida útil por familia en '
             'congelación está en la tabla del pie de «Semanales» '
             '(05-tareas-semanales-mensuales)')

#: DOM-18 (equivalente) — «Registrar mermas significativas del servicio» deja
#: al criterio del que cierra qué es «significativo», y no pide ni cantidad ni
#: motivo, que es lo único con lo que después se corrige un escandallo.
MERMAS = ('Anotar las mermas del día (producto, cantidad y motivo): es el '
          'dato que corrige el escandallo del plato y el pedido de mañana')

#: DOM-17 (equivalente) — el registro de jornada es obligatorio en España
#: desde el RD-ley 8/2019 y hay que conservarlo 4 años. Barrido de los 13
#: ficheros del kit: cero menciones a «jornada» o «fichaje». En un menú
#: degustación, donde la brigada entra a las 9 y sale pasada la medianoche, es
#: exactamente el sitio donde una inspección de Trabajo mira primero.
JORNADA_DIA = [
    ('Cerrar y validar el registro diario de jornada de toda la brigada '
     '(cocina y sala), con las horas reales de entrada y salida: es '
     'obligatorio y hay que conservarlo 4 años', 'Admin'),
]


def _f01(wb, cambios):
    tocado = False
    ws = wb['Apertura AM']
    if _insertar_seccion(ws, '🌅 APERTURA — EQUIPAMIENTO VANGUARDIA',
                         ARRANQUE, ARRANQUE_TAREAS):
        cambios.append('«Apertura AM»: sección nueva «{}» ({} tareas) DELANTE '
                       'de la de equipamiento: higiene personal y orden '
                       'seguro campana → gas → equipos, que no existían en '
                       'ninguno de los 13 ficheros — DOM-12 / DOM-13 '
                       '(equivalentes)'
                       .format(ARRANQUE, len(ARRANQUE_TAREAS)))
        tocado = True
    if _sustituir(ws, 'Encender baños térmicos / Roner / equipos sous-vide',
                  RONER):
        cambios.append('«Apertura AM»: el primer equipo del día ya no se '
                       'enciende antes que la campana — DOM-13 (equivalente)')
    if _sustituir(ws, 'Verificar cámaras de maduración (temp., humedad)',
                  CAMARAS_MADURACION):
        cambios.append('«Apertura AM»: las cámaras de maduración se COMPRUEBAN '
                       'desde la noche anterior, con hueco para la lectura de '
                       'temperatura y humedad y qué hacer si hay desviación — '
                       'DOM-24 (equivalente)')
    if _insertar_tras(ws, CAMARAS_MADURACION, CAMARAS_FRIO):
        cambios.append('«Apertura AM»: comprobación nocturna de las cámaras '
                       'frigoríficas y del congelador con objetivo '
                       '(0-4 °C / ≤ −18 °C), que la apertura NO tenía (sólo '
                       'miraba las de maduración) — DOM-24 (equivalente)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)

    ws = wb['Cierre PM']
    if _sustituir(ws, 'Registrar temperaturas de todas las cámaras '
                      'frigoríficas', CAMARAS_CIERRE):
        cambios.append('«Cierre PM»: la temperatura de cierre lleva el '
                       'objetivo y el hueco para la lectura — §2.9 / DOM-14 '
                       '(equivalente)')
    if _sustituir(ws, 'Etiquetar TODAS las pre-elaboraciones (fecha, hora, '
                      'contenido)', ETIQUETAR):
        cambios.append('«Cierre PM»: el etiquetado pide también la fecha '
                       'límite de uso y remite a la tabla de vida útil — '
                       'DOM-29 (equivalente)')
    if _sustituir(ws, 'Registrar mermas significativas del servicio', MERMAS):
        cambios.append('«Cierre PM»: las mermas se anotan con producto, '
                       'cantidad y motivo, sin dejar «significativas» al '
                       'criterio del turno — DOM-18 (equivalente)')
    if _insertar_tras(ws, 'Confirmar reservas y alérgenos para mañana',
                      JORNADA_DIA):
        cambios.append('«Cierre PM»: cierre y validación del registro diario '
                       'de jornada de la brigada (RD-ley 8/2019, conservación '
                       '4 años); el kit no mencionaba «jornada» ni «fichaje» '
                       'en ninguno de sus 13 ficheros — DOM-17 (equivalente)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)

    if _instrucciones(wb, 'Antes de encender nada:', [
            'La primera sección de «Apertura AM» es de higiene personal y de '
            'arranque seguro: campana primero, comprobación del gas después y '
            'sólo entonces Roner, hornos, deshidratador y sopletes.',
            'Las cámaras no se «encienden» por la mañana: se COMPRUEBA que '
            'han funcionado toda la noche. Anota la lectura en la propia '
            'tarea (refrigeración 0-4 °C, congelación ≤ −18 °C, y en las de '
            'maduración también la humedad).',
            'El cierre incluye el registro diario de jornada de la brigada: '
            'es obligatorio, se valida cada día y se conserva 4 años.']):
        cambios.append('Instrucciones: arranque seguro, comprobación nocturna '
                       'de cámaras y registro de jornada — DOM-12 / DOM-13 / '
                       'DOM-24 / DOM-17')
        tocado = True
    return tocado


# ==========================================================================
# 02-mise-en-place-degustacion.xlsx — «Pre-elab Largo» y «Pre-elab Día»
# ==========================================================================
#: DOM-02 (equivalente, ALTA) — «Tartares y ceviches (cortar en el momento, no
#: antes de 2h)» resuelve la temperatura y se olvida del parásito. El barrido
#: de los 13 xlsx del kit no encontró NI UNA mención a «anisakis» ni a
#: «congela», y este kit sirve crudos en varios pases del menú degustación.
#: La palabra ANISAKIS va en mayúsculas y completa a propósito: es la que se
#: busca con Ctrl+F y la que pregunta el inspector.
ANISAKIS_DIA = ('Tartares y ceviches: cortar en el momento, nunca más de 2 h '
                'antes del pase. Prevención de ANISAKIS: el pescado que se '
                'sirve crudo o semicrudo debe haberse congelado antes ≥24 h a '
                '−20 °C (o 15 h a −35 °C) — exige el certificado al proveedor '
                'o congélalo tú, y anota el lote')

#: DOM-02 (equivalente) — el marinado largo de pescado (boquerón, salmón
#: curado, ahumado en frío) es el otro vector clásico, y aquí compartía línea
#: con las carnes como si fuera el mismo riesgo.
ANISAKIS_LARGO = ('Marinados largos (carnes/pescados en aceite, sal, '
                  'especias): el pescado que no se cocine por encima de 60 °C '
                  '—marinado, curado o ahumado en frío— tiene que venir de '
                  'congelación preventiva frente al ANISAKIS (ver «Pre-elab '
                  'Día»)')

#: DOM-26 (equivalente) — el kit verifica «frescura y color» de microbrotes y
#: flores comestibles y NUNCA los lava. En un restaurante de autor esos brotes
#: van crudos encima de casi todos los pases, sin ningún paso térmico
#: posterior: son el vector de contaminación más directo de la carta.
DESINFECCION = [
    ('Desinfectar microbrotes, flores comestibles y hierbas que van CRUDOS al '
     'plato: lejía apta para uso alimentario según la dosis del fabricante '
     '(habitual: 70 ppm, 5 min) y ACLARAR con agua potable abundante',
     'Cocina'),
]


def _f02(wb, cambios):
    tocado = False
    ws = wb['Pre-elab Día']
    if _sustituir(ws, 'Tartares y ceviches (cortar en el momento, no antes '
                      'de 2h)', ANISAKIS_DIA):
        cambios.append('«Pre-elab Día»: congelación preventiva frente al '
                       'ANISAKIS del pescado que se sirve crudo o semicrudo '
                       '(RD 1420/2006 · Rgto. CE 853/2004), que no estaba en '
                       'ninguno de los 13 ficheros — DOM-02 (equivalente, '
                       'ALTA)')
    if _insertar_tras(ws, 'Verificar flores comestibles (frescura, color)',
                      DESINFECCION):
        cambios.append('«Pre-elab Día»: desinfección con dosis y aclarado de '
                       'los microbrotes, flores y hierbas que van crudos al '
                       'plato; el kit sólo verificaba su «frescura y color» — '
                       'DOM-26 (equivalente)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)

    ws = wb['Pre-elab Largo']
    if _sustituir(ws, 'Marinados largos (carnes/pescados en aceite, sal, '
                      'especias)', ANISAKIS_LARGO):
        cambios.append('«Pre-elab Largo»: el marinado, el curado y el ahumado '
                       'en frío de pescado se separan de las carnes y '
                       'remiten a la congelación preventiva — DOM-02 '
                       '(equivalente)')
    _renumerar_p4(ws)
    _dv_extender(ws)

    if _instrucciones(wb, 'Pescado crudo y producto que va crudo al plato:', [
            'Todo pescado que se sirva crudo o semicrudo (tartar, ceviche, '
            'marinado, curado, ahumado en frío) necesita congelación previa: '
            '≥24 h a −20 °C o 15 h a −35 °C. Pide el certificado al proveedor '
            'y anota el lote; el cítrico del ceviche NO mata el anisakis.',
            'Microbrotes, flores comestibles y hierbas van crudos al pase y '
            'no reciben ningún tratamiento térmico después: se desinfectan y '
            'se ACLARAN con agua potable antes de entrar en la estación de '
            'emplatado.']):
        cambios.append('Instrucciones: anisakis y desinfección del producto '
                       'que va crudo al plato — DOM-02 / DOM-26')
        tocado = True
    return tocado


# ==========================================================================
# 04-tareas-brigada-creativa.xlsx — hoja «Partida Fría»
# ==========================================================================
#: DOM-02 (equivalente) — el hallazgo señala el 02, pero quien ejecuta el
#: crudo todos los días es la partida fría, y su hoja de rol repetía la misma
#: media verdad («cortar máx. 2h antes») sin nombrar el parásito. Si la
#: prevención sólo vive en el libro de mise en place, el cocinero que trabaja
#: con su hoja de rol delante no la ve nunca.
ANISAKIS_FRIA = ('Ceviches y tartares: cortar máx. 2 h antes del servicio y '
                 'SÓLO con pescado que haya pasado la congelación preventiva '
                 'frente al ANISAKIS (ver 02 · «Pre-elab Día»)')

#: DOM-02 (equivalente) — el marinado rápido con cítrico es justo el caso en
#: el que la cocina cree que el limón «cocina» el pescado. No lo hace, y este
#: es el único sitio del kit donde alguien podría creerlo.
MARINADO_FRIA = ('Marinados rápidos (cítricos, vinagres): el ácido NO mata el '
                 'anisakis ni sustituye a la congelación previa — sólo cambia '
                 'la textura')


def _f04(wb, cambios):
    ws = wb['Partida Fría']
    if _sustituir(ws, 'Ceviches y tartares: cortar máx. 2h antes de servicio',
                  ANISAKIS_FRIA):
        cambios.append('«Partida Fría»: la hoja de rol de quien corta el crudo '
                       'todos los días remite a la congelación preventiva — '
                       'DOM-02 (equivalente)')
    if _sustituir(ws, 'Marinados rápidos (cítricos, vinagres)',
                  MARINADO_FRIA):
        cambios.append('«Partida Fría»: el marinado con cítrico deja de '
                       'parecer un tratamiento de seguridad — DOM-02 '
                       '(equivalente)')
    _renumerar_p4(ws)
    _dv_extender(ws)
    return False


# ==========================================================================
# 05-tareas-semanales-mensuales.xlsx — «Semanales», «Mensuales» y la hoja
# nueva «Trimestral y Anual»
# ==========================================================================
#: DOM-29 — el hallazgo señala este fichero, y encaja: «Semanales» es donde
#: vive el inventario y la rotación de stock. La tarea nueva es la que hace
#: útil la tabla del pie.
CONGELADOR = [
    ('Revisar el congelador y el arcón: rotación FIFO, etiquetas legibles y '
     'descarte de lo que ha superado la vida útil de la tabla del pie de esta '
     'hoja', 'Stock'),
]

#: DOM-27 (equivalente) — este kit no tiene freidora en ninguna tarea, pero sí
#: fríe: «Preparar crujientes de última hora (tempura, chip)» en 02 y los
#: crujientes de pastelería. La tarea va condicionada y con el desplegable
#: «N/A» a mano para la cocina que no fríe, así que nadie tiene que marcar
#: algo que no hace. Lo que NO puede quedar sin decir es la temperatura: el
#: aceite se filtra o se cambia en frío.
ACEITE = [
    ('Si tu cocina fríe (tempura, crujientes, buñuelos): filtrar o cambiar el '
     'aceite SOLO en frío, por debajo de 40 °C — nunca en caliente — y '
     'entregarlo a gestor autorizado', 'Limpieza'),
]

#: FUSIÓN 5 (mismo patrón, esta vez contra la hoja NUEVA) — «Trimestral y
#: Anual» trae «Calibración externa certificada de las básculas de precisión
#: (0,01 g)» y «Contraste de sondas y termómetros contra un patrón conocido».
#: «Mensuales» ya decía «Calibración profesional de básculas y termómetros»,
#: que es exactamente eso pedido cada mes: nadie contrata al metrólogo doce
#: veces al año, así que la tarea no se hacía y la casilla se marcaba igual.
#: Se queda con lo que SÍ se hace en casa cada mes —la báscula contra su pesa
#: patrón— y remite a la hoja nueva para lo demás. Queda una escalera sin
#: solape: semanal (comprobación rápida) → mensual (pesa patrón) → trimestral
#: (sondas contra agua con hielo) → anual (calibración externa certificada).
CALIBRACION_MES = ('Verificación interna de las básculas con su pesa patrón y '
                   'ajuste si hace falta (el contraste de sondas y '
                   'termómetros y la calibración externa certificada van en '
                   '«Trimestral y Anual»)')

#: DOM-17 (equivalente) — la otra mitad del registro de jornada: el archivo
#: mensual. Va al bloque de finanzas y gestión, que es el único del kit donde
#: alguien se sienta a cerrar el mes.
JORNADA_MES = [
    ('Archivar los registros de jornada del mes junto a nóminas y contratos: '
     'hay que conservarlos 4 años y es lo primero que pide una inspección de '
     'Trabajo', 'Admin'),
]

TITULO_VIDA_UTIL = ('VIDA ÚTIL ORIENTATIVA EN CONGELACIÓN A −18 °C — ajústala '
                    'a tu producto y a tu proveedor')
VIDA_UTIL = [
    ('Carnes rojas y aves crudas, en pieza', '6-12 meses',
     'Porciona ANTES de congelar: descongelar y volver a congelar no se hace'),
    ('Carne picada y preparados de carne', '3 meses',
     'Más superficie expuesta, se enrancia antes'),
    ('Pescado azul (atún, caballa, sardina)', '2-3 meses',
     'La grasa se oxida: envasa al vacío y ponle fecha de entrada'),
    ('Pescado blanco y marisco crudo', '3-6 meses',
     'Si va a servirse crudo, la congelación cuenta además como tratamiento '
     'anti-ANISAKIS: ≥24 h a −20 °C'),
    ('Fondos, glacés, caldos y consomés', '4-6 meses',
     'Congela en porciones de servicio: descongelar un bloque entero para un '
     'pase es merma segura'),
    ('Sous-vide ya cocinado y abatido, en su bolsa', '3 meses',
     'Abate primero a ≤ −18 °C; la bolsa intacta o la vida útil no vale'),
    ('Purés, cremas y bases de helado', '3-4 meses',
     'Las que llevan huevo o lácteo, en el tramo corto'),
    ('Masas crudas, hojaldres y crujientes sin hornear', '2-3 meses',
     'Pierden gasificación: rotúlalas con la fecha de elaboración'),
    ('Frutas y verduras blanqueadas o en puré', '8-12 meses',
     'Blanquea antes de congelar: sin blanquear pierden color y textura en '
     'pocas semanas'),
    ('Producto que ya ha salido a un pase o a la mesa', 'No congelar',
     'Lo que ha salido a sala o ha roto la cadena de frío no vuelve al '
     'congelador: se retira y se anota como merma'),
]


def _tabla_vida_util(ws, cambios):
    """Tabla editable de vida útil al pie de «Semanales».

    Va DEBAJO de la fila de firma, es decir, por debajo del contador y fuera
    del rango que éste cuenta: es una referencia, no una tarea que marcar.
    """
    if _fila(ws, TITULO_VIDA_UTIL, 1) is not None:
        return False
    g = motor.geometria_p4(ws)
    if not g:
        raise AnclaPerdida('«Semanales»: no es una hoja del molde P4')
    firma = None
    for r in range(g['contador'] or 1, ws.max_row + 1):
        v = ws.cell(row=r, column=1).value
        if isinstance(v, str) and v.startswith('Firma responsable'):
            firma = r
            break
    if firma is None:
        raise AnclaPerdida('«Semanales»: no encuentro la fila de firma')
    banda = _exige(ws, '📦 INVENTARIO Y STOCK SEMANAL', 1)
    est_titulo = _estilos(ws, banda)
    est_cab = _estilos(ws, g['hr'])
    est_dato = _estilos(ws, g['hr'] + 1)
    motor.insertar_filas(ws, firma + 1, 3 + len(VIDA_UTIL))
    fila = firma + 2
    _pintar(ws, fila, est_titulo)
    ws.cell(row=fila, column=1).value = TITULO_VIDA_UTIL
    motor._merge(ws, 'A{}:{}{}'.format(fila, L(NCOL), fila))
    fila += 1
    _pintar(ws, fila, est_cab)
    ws.cell(row=fila, column=2).value = 'Familia'
    ws.cell(row=fila, column=3).value = 'Vida útil'
    ws.cell(row=fila, column=4).value = 'Notas'
    motor._merge(ws, 'D{}:{}{}'.format(fila, L(NCOL), fila))
    for i, (familia, vida, nota) in enumerate(VIDA_UTIL, start=1):
        r = fila + i
        _pintar(ws, r, est_dato)
        ws.cell(row=r, column=1).value = None
        ws.cell(row=r, column=2).value = familia
        ws.cell(row=r, column=3).value = vida
        ws.cell(row=r, column=4).value = nota
        for c in (2, 3, 4):
            motor._verde(ws.cell(row=r, column=c))
        motor._merge(ws, 'D{}:{}{}'.format(r, L(NCOL), r))
    cambios.append('«Semanales»: tabla editable de vida útil en congelación '
                   '({} familias) al pie, fuera del rango del contador — '
                   'DOM-29'.format(len(VIDA_UTIL)))
    return True


HOJA_LEGAL = 'Trimestral y Anual'
TITULO_LEGAL = 'Mantenimiento Trimestral y Anual — Revisiones Contratadas'
#: DOM-16 (equivalente) — el kit tenía «Semanales» y «Mensuales» y se acababa
#: ahí: ni una línea sobre lo que se CONTRATA y se pide por escrito en una
#: inspección. Barrido de los 13 ficheros: cero apariciones de «DDD»,
#: «plagas», «extintor», «legionela», «conductos», «Verifactu» y «póliza».
#: Se crea aquí, en el libro de cadencias del kit, porque este producto no
#: tiene libro de manager (el 03 es I+D).
LEGAL = [
    ('🐜 HIGIENE, PLAGAS Y AGUA — empresa autorizada', [
        ('Control de plagas (DDD): visita de la empresa autorizada, parte '
         'firmado y certificado en vigor', 'Admin', 'Trimestral'),
        ('Limpieza de campana y conductos de extracción por empresa '
         'homologada, con certificado', 'Limpieza', 'Anual'),
        ('Analítica de superficies y de producto en laboratorio externo '
         '(verificación del plan de limpieza)', 'Cocina', 'Semestral'),
        ('Revisar el plan APPCC y las fichas de proveedor: altas, bajas y '
         'cambios de carta del año', 'Admin', 'Anual'),
        ('Renovar los carnés de manipulador de alimentos de toda la brigada, '
         'extras incluidos', 'Admin', 'Anual'),
        ('Comprobar que el registro sanitario (RGSEAA) recoge la actividad y '
         'las instalaciones actuales', 'Admin', 'Anual'),
    ]),
    ('🔧 EQUIPOS, FRÍO Y GAS', [
        ('Revisión de la instalación de gas por empresa habilitada, si la '
         'cocina tiene gas', 'Cocina', 'Cada 5 años'),
        ('Revisión de cámaras frigoríficas y de maduración por frigorista: '
         'gas, juntas, sondas y desescarche', 'Cámara', 'Anual'),
        ('Calibración externa certificada de las básculas de precisión '
         '(0,01 g)', 'Cocina', 'Anual'),
        ('Revisión por el SAT de Roner/baños térmicos, abatidor, '
         'deshidratador, Pacojet y sifones', 'Cocina', 'Anual'),
        ('Contraste de sondas y termómetros contra un patrón conocido (agua '
         'con hielo, 0 °C) y anotar la desviación', 'Cocina', 'Trimestral'),
        ('Retirada del aceite de fritura usado por gestor autorizado y '
         'archivo del documento de entrega', 'Limpieza', 'Trimestral'),
    ]),
    ('🧯 SEGURIDAD DEL LOCAL', [
        ('Revisión de extintores y BIE por empresa mantenedora (etiqueta y '
         'acta)', 'Admin', 'Anual'),
        ('Revisión del sistema de detección y de las luces de emergencia',
         'Admin', 'Anual'),
        ('Plan de prevención de legionela si hay torre de refrigeración, spa '
         'o agua caliente sanitaria de riesgo', 'Admin', 'Semestral'),
        ('Revisión de la instalación eléctrica por instalador autorizado '
         '(local de pública concurrencia)', 'Admin', 'Cada 5 años'),
        ('Simulacro y repaso del plan de emergencia con la brigada y con '
         'sala', 'Admin', 'Anual'),
    ]),
    ('📄 DOCUMENTACIÓN, SEGUROS Y FISCAL', [
        ('Revisar la póliza de responsabilidad civil: suma asegurada, aforo y '
         "actividades cubiertas (chef's table, pop-ups, showcookings)",
         'Admin', 'Anual'),
        ('Archivar los registros de jornada del trimestre y revisar '
         'contratos, altas y horas extra', 'Admin', 'Trimestral'),
        ('Revisión del TPV y del software de facturación (requisitos '
         'antifraude / Verifactu)', 'Admin', 'Anual'),
        ('Actualizar escandallos y precios de carta con los precios reales de '
         'proveedor', 'Food cost', 'Trimestral'),
        ('Renovar licencias, tasa de terraza y seguros del local', 'Admin',
         'Anual'),
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
    """Crea «Trimestral y Anual» clonando «Mensuales» y ajustando bloques.

    Se clona en lugar de construirse a mano porque el clon trae anchos,
    alturas, bordes, combinaciones y la geometría exacta del molde P4; lo que
    NO trae (medido con openpyxl) son el desplegable, el pie de impresión y
    los paneles inmovilizados, y por eso se le aplican aquí uno a uno.

    A diferencia del hermano de catering, aquí los bloques se ajustan en los
    DOS sentidos: «Mensuales» tiene bloques de 4-5-6-4 filas y esta hoja pide
    6-6-5-6, así que hay que INSERTAR filas, no sólo recortarlas.
    """
    if HOJA_LEGAL in wb.sheetnames:
        return False
    modelo = wb['Mensuales']
    ws = wb.copy_worksheet(modelo)
    ws.title = HOJA_LEGAL
    ws.cell(row=1, column=1).value = TITULO_LEGAL
    g = motor.geometria_p4(ws)
    if not g:
        raise AnclaPerdida('«Mensuales»: el clon no es del molde P4')
    bloques = _bloques_p4(ws, g)
    if len(bloques) != len(LEGAL):
        raise AnclaPerdida('«Mensuales» tiene {} bloques y «{}» espera {}'
                           .format(len(bloques), HOJA_LEGAL, len(LEGAL)))
    # De ABAJO hacia ARRIBA: tocar un bloque mueve los de debajo, no los de
    # encima, así que las filas ya medidas siguen siendo válidas.
    for (banda, cab, filas), (_titulo, tareas) in reversed(
            list(zip(bloques, LEGAL))):
        if not filas:
            raise AnclaPerdida('«{}»: bloque sin filas de tarea'
                               .format(HOJA_LEGAL))
        sobra = len(filas) - len(tareas)
        if sobra > 0:
            motor.eliminar_filas(ws, filas[len(tareas)], sobra)
        elif sobra < 0:
            est = _estilos(ws, filas[-1])
            motor.insertar_filas(ws, filas[-1] + 1, -sobra)
            for i in range(-sobra):
                _pintar(ws, filas[-1] + 1 + i, est)
                # El «#» tiene que quedar como ENTERO ya: `_bloques_p4`
                # reconoce una fila de tarea por `isinstance(A, int)` y, sin
                # esto, la segunda medición cortaba el bloque en la última
                # fila del original y las filas recién insertadas quedaban
                # huérfanas («quedó con 4 filas para 6 tareas»).
                ws.cell(row=filas[-1] + 1 + i, column=1).value = 0
    g = motor.geometria_p4(ws)
    bloques = _bloques_p4(ws, g)
    for (banda, cab, filas), (titulo, tareas) in zip(bloques, LEGAL):
        ws.cell(row=banda, column=1).value = titulo
        if cab:
            ws.cell(row=cab, column=6).value = 'Cadencia'
        if len(filas) != len(tareas):
            raise AnclaPerdida('«{}»: el bloque «{}» quedó con {} filas para '
                               '{} tareas'.format(HOJA_LEGAL, titulo,
                                                  len(filas), len(tareas)))
        for r, (texto, zona, cadencia) in zip(filas, tareas):
            ws.cell(row=r, column=2).value = texto
            _zona(ws, r, zona)
            ws.cell(row=r, column=4).value = None
            ws.cell(row=r, column=6).value = cadencia
    _renumerar_p4(ws)
    # Desplegable: el clon no hereda ninguno.
    dv = motor.DataValidation(
        type='list', formula1=motor.DV_LISTA, allow_blank=True,
        showErrorMessage=True, errorStyle='stop',
        errorTitle=motor.DV_ERROR_TIT, error=motor.DV_ERROR)
    ws.add_data_validation(dv)
    _dv_extender(ws)
    if not dv.sqref.ranges:
        raise AnclaPerdida('«{}»: el desplegable quedó vacío'
                           .format(HOJA_LEGAL))
    # A4 + pie + fila de cabecera repetida al imprimir: `motor.cerrar` no corre
    # sobre el molde P4, así que sin esto la hoja nueva saldría del censo como
    # «noprint» (paperSize/fitToPage/pie son tres de sus comprobaciones).
    motor.print_setup(ws, g['hr'], landscape=True)
    cambios.append('hoja nueva «{}» en 05: mantenimiento y documentación que '
                   'se CONTRATA y que pide una inspección (DDD, conductos, '
                   'analíticas, gas, frigorista, calibración de básculas y '
                   'sondas, extintores, legionela, eléctrica, RGSEAA, carnés '
                   'de manipulador, póliza, Verifactu y escandallos) — '
                   'DOM-16 (equivalente); el kit se acababa en «Mensuales»'
                   .format(HOJA_LEGAL))
    return True


def _f05(wb, cambios):
    tocado = False
    ws = wb['Semanales']
    if _insertar_tras(ws, 'Verificar stock de microbrotes y flores '
                          'comestibles', CONGELADOR):
        cambios.append('«Semanales»: rotación FIFO del congelador y descarte '
                       'por vida útil, que hace útil la tabla del pie — '
                       'DOM-29')
        tocado = True
    if _insertar_tras(ws, 'Mantenimiento sifones: juntas, válvulas, limpieza',
                      ACEITE):
        cambios.append('«Semanales»: el aceite de fritura se filtra o se '
                       'cambia SOLO por debajo de 40 °C; la tarea va '
                       'condicionada («si tu cocina fríe») y el desplegable '
                       'tiene N/A para quien no fría — DOM-27 (equivalente)')
        tocado = True
    if _tabla_vida_util(ws, cambios):
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)

    ws = wb['Mensuales']
    if _sustituir(ws, 'Calibración profesional de básculas y termómetros',
                  CALIBRACION_MES):
        cambios.append('«Mensuales»: «Calibración profesional de básculas y '
                       'termómetros» pedía cada mes lo que la hoja nueva '
                       '«Trimestral y Anual» contrata cada año; pasa a ser la '
                       'verificación interna con pesa patrón y remite a la '
                       'hoja nueva — mismo patrón de duplicado que el '
                       'verificador señaló en 07')
    if _insertar_tras(ws, 'Revisión de mermas mensuales y plan de reducción',
                      JORNADA_MES):
        cambios.append('«Mensuales»: archivo mensual de los registros de '
                       'jornada (conservación 4 años) — DOM-17 (equivalente)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)

    if _hoja_legal(wb, cambios):
        tocado = True

    if _instrucciones(wb, 'Más allá del mes:', [
            'La hoja «Trimestral y Anual» recoge lo que se CONTRATA y se pide '
            'por escrito en una inspección: DDD, conductos de extracción, '
            'analíticas, instalación de gas, frigorista, calibración de '
            'básculas y sondas, extintores, legionela, eléctrica, RGSEAA, '
            'carnés de manipulador, póliza y facturación.',
            'Anota en «Notas» el número de parte de cada revisión y la fecha '
            'de la siguiente; la columna «Cadencia» ya trae la periodicidad '
            'legal o recomendada de cada una.',
            'Al pie de «Semanales» tienes una tabla editable de vida útil en '
            'congelación por familia: ajústala a tu producto y a tu '
            'proveedor. Está fuera del contador porque es una referencia, no '
            'una tarea.']):
        cambios.append('Instrucciones: hoja «Trimestral y Anual», tabla de '
                       'vida útil y registro de jornada — DOM-16 / DOM-29 / '
                       'DOM-17')
        tocado = True
    return tocado


# ==========================================================================
# 07-chefs-table-eventos.xlsx — hoja «Cenas Especiales»
# ==========================================================================
#: DOM-19 (equivalente) — «Alérgenos y preferencias confirmados» y
#: «Presupuesto aprobado y facturación preparada» son las dos únicas líneas
#: que el kit dedica a cerrar una cena privada, y las dos van DESPUÉS de
#: diseñar el menú. Falta lo que se pacta al aceptar la reserva: alérgenos por
#: escrito (no de palabra, que es como se pierde el juicio), número cerrado,
#: precio por comensal, señal y condiciones de cancelación. En un restaurante
#: de menú degustación una mesa privada de 12 que no aparece es la
#: facturación de la noche.
RESERVA = '📝 AL CONFIRMAR LA RESERVA (cena privada, evento o chef\'s table)'
RESERVA_TAREAS = [
    ('Alérgenos e intolerancias de TODOS los comensales por escrito (correo o '
     'formulario), nunca de palabra, y con nombre de la mesa', 'Admin'),
    ('Número de comensales cerrado y fecha límite para cambios, anotada en la '
     'ficha del evento', 'Admin'),
    ('Precio por comensal y qué incluye (menú, maridaje, extras, servicio, '
     'IVA) confirmado por escrito', 'Admin'),
    ('Señal o anticipo cobrado y condiciones de cancelación aceptadas por '
     'escrito', 'Admin'),
    ('Menú definitivo cerrado con cocina, con las alternativas de cada '
     'alérgeno ya resueltas y probadas', 'Cocina'),
    ('Peticiones especiales anotadas en la ficha: dieta, celebración, '
     'decoración, tarta, horario de salida', 'Eventos'),
]

#: FUSIÓN 1 (verificador tanda 3) — la sección nueva se insertó DELANTE de
#: «🕯️ CENAS PRIVADAS» sin retirar las tareas viejas que cubren el mismo
#: hecho, y el cliente se encontraba dos controles para una sola cosa a nueve
#: filas de distancia. La regla que se aplica aquí, y que vale para cualquier
#: `_insertar_seccion` futuro de este módulo, es: la tarea vieja NO se borra
#: —rompería el contador y el cliente que ya usa la hoja perdería su fila—,
#: se REESCRIBE en el momento del ciclo que la nueva no cubre. La nueva pacta
#: al CONFIRMAR; la vieja pasa a ser el control del SERVICIO.
#:
#: «Alérgenos y preferencias confirmados» (Cenas Especiales, la 2.ª de CENAS
#: PRIVADAS) era la versión débil del control nuevo: «confirmados» no dice ni
#: por quién, ni cómo, ni contra qué se cotejan. Ahora es el cotejo del pase.
ALERGENOS_PASE = ('Cotejar en el pase los alérgenos confirmados por escrito '
                  'con la comanda de cada comensal')

#: FUSIÓN 2 — «Menú personalizado según solicitud del cliente» repetía, ya
#: dentro de la cena, el «Menú definitivo cerrado con cocina…» de la sección
#: nueva. Pasa a ser lo que de verdad ocurre después: producirlo.
MENU_PRIVADA = ('Producir el menú ya cerrado con el cliente: pedido '
                'específico, mise en place y prueba de los pases exclusivos '
                'de esta mesa')

#: FUSIÓN 3 — «Presupuesto aprobado y facturación preparada» solapaba a
#: medias con «Precio por comensal y qué incluye… confirmado por escrito»: el
#: precio se pacta al confirmar (sección nueva) y la factura se cierra al
#: terminar la cena, con lo realmente consumido. Se separan los dos momentos.
FACTURA_PRIVADA = ('Cerrar la facturación al terminar la cena: extras '
                   'realmente consumidos, señal ya cobrada descontada e IVA '
                   'aplicado')

#: FUSIÓN 4 — el título de la sección nueva dice «(cena privada, evento o
#: chef's table)», así que también absorbe la 1.ª tarea de la hoja «Chef's
#: Table», que confirmaba comensales y alérgenos por segunda vez y sin exigir
#: que fuera por escrito. No está «a pocas filas» —está en otra hoja del mismo
#: fichero—, pero es el mismo defecto: dos controles para el mismo hecho.
#: Pasa a ser el repaso del día, que es lo que falta cuando la reserva ya se
#: cerró por escrito semanas antes.
CHEFS_TABLE_REPASO = ('Repasar con cocina el número final de comensales y los '
                      'alérgenos ya confirmados por escrito al reservar (ver '
                      '«Cenas Especiales» → «AL CONFIRMAR LA RESERVA»)')


def _f07(wb, cambios):
    tocado = False
    ws = wb['Cenas Especiales']
    if _insertar_seccion(ws, '🕯️ CENAS PRIVADAS', RESERVA, RESERVA_TAREAS):
        cambios.append('«Cenas Especiales»: sección nueva «{}» ({} tareas) '
                       'delante de la operativa de la cena: alérgenos por '
                       'escrito, número cerrado, precio por comensal, señal y '
                       'condiciones de cancelación — DOM-19 (equivalente)'
                       .format(RESERVA, len(RESERVA_TAREAS)))
        tocado = True
    if _sustituir(ws, 'Alérgenos y preferencias confirmados', ALERGENOS_PASE):
        cambios.append('«Cenas Especiales»: la tarea vieja «Alérgenos y '
                       'preferencias confirmados» dejaba DOS controles para el '
                       'mismo hecho a nueve filas de la sección nueva; pasa a '
                       'ser el control de SERVICIO (cotejo en el pase contra '
                       'la comanda) — fusión pedida por el verificador')
    if _sustituir(ws, 'Menú personalizado según solicitud del cliente',
                  MENU_PRIVADA):
        cambios.append('«Cenas Especiales»: «Menú personalizado según '
                       'solicitud del cliente» repetía el cierre de menú de la '
                       'sección nueva; pasa a ser la PRODUCCIÓN de ese menú '
                       '(pedido, mise en place y prueba de los pases)')
    if _sustituir(ws, 'Presupuesto aprobado y facturación preparada',
                  FACTURA_PRIVADA):
        cambios.append('«Cenas Especiales»: el presupuesto se pacta al '
                       'confirmar (sección nueva) y la factura se cierra al '
                       'terminar, con los extras realmente consumidos y la '
                       'señal descontada: dejan de solapar')
    _renumerar_p4(ws)
    _dv_extender(ws)

    ws = wb["Chef's Table"]
    if _sustituir(ws, 'Confirmar número de comensales y alérgenos',
                  CHEFS_TABLE_REPASO):
        cambios.append('«Chef\'s Table»: la sección nueva ya cubre el chef\'s '
                       'table, así que la 1.ª tarea de esta hoja duplicaba la '
                       'confirmación de comensales y alérgenos; pasa a ser el '
                       'repaso del día contra lo confirmado por escrito')
    _renumerar_p4(ws)
    _dv_extender(ws)

    if _instrucciones(wb, 'Antes de aceptar una reserva privada:', [
            'La primera sección de «Cenas Especiales» es lo que se pacta AL '
            'CONFIRMAR: alérgenos e intolerancias por escrito, número de '
            'comensales cerrado, precio por comensal, señal y condiciones de '
            'cancelación. Lo de palabra no se puede demostrar después.',
            'Los alérgenos llegan por escrito y se resuelven con cocina antes '
            'de cerrar el menú, no la misma noche: en un degustación de diez '
            'pases, una alternativa improvisada rompe la secuencia entera.',
            'La noche de la cena no se vuelve a «confirmar» nada: lo que se '
            'hace en el pase es COTEJAR los alérgenos ya confirmados por '
            'escrito con la comanda de cada comensal. Uno pacta y el otro '
            'comprueba; no son dos veces el mismo control.']):
        cambios.append('Instrucciones: bloque de confirmación de reserva — '
                       'DOM-19 (equivalente)')
        tocado = True
    return tocado


# ==========================================================================
# 09-plantilla-personalizable.xlsx — «Plantilla A», «B» y «C»
# ==========================================================================
#: DOM-07 — las tres plantillas se entregan con la cabecera puesta y las 25
#: filas siguientes EN BLANCO: el cliente abre la hoja y no tiene ni una pista
#: de qué escribir ni con qué nivel de detalle. El motor no puede arreglarlo
#: (no sabe de qué va el kit), así que el contenido lo pone aquí el módulo:
#: tres filas de EJEMPLO con el vocabulario de la casa —menú degustación,
#: chef's table, I+D, plating bible—, en gris y en cursiva para que se lean
#: como lo que son.
#:
#: Van MARCADAS «N/A» a propósito, y ésa es la parte que protege el contador:
#: el denominador del molde P4 es
#: `COUNTIF(B,"?*") - COUNTIF(B,"Tarea") - COUNTIF(✓,"N/A")`,
#: así que una fila de ejemplo marcada N/A no suma. Sin la marca, cada
#: plantilla se entregaría diciendo «0 de 3» y —peor— `gate_recuento` de
#: `main.py` sumaría 9 tareas de mentira al recuento del kit, que es la cifra
#: que va a la landing. Con la marca, el contador sigue en «0 de 0» y el
#: recuento del producto no se mueve ni una tarea.
#: DOM-07 RESIDUAL (verificación ver3, tanda 5) — las tres filas de ejemplo
#: arreglaron la hoja EN BLANCO, pero las escribían IGUALES en «Plantilla A»,
#: «B» y «C»: el fichero seguía entregando la misma plantilla tres veces y la
#: SPEC §2.3 pide justo lo contrario, tres EJES distintos. El motor no lo
#: alcanza aquí (`diferenciar_07` pasa por `motor.geometria`, del molde ▸, y
#: además exige que la hoja se llame «Por Franja Horaria» / «Por Área» / «Por
#: Perfil»: estas se llaman «Plantilla A/B/C» y son molde P4), así que el eje
#: lo pone este módulo.
#:
#: El eje se escribe en TRES sitios de la hoja, todos celdas que YA existen:
#:   · el rótulo A1 (banda de título, merge A1:G1) — con el mismo formato que
#:     ya usan chocolatería y heladería en su 07: «Plantilla Personalizable —
#:     Por Zona / Por Turno / Por Perfil»;
#:   · el texto de las tres tareas de ejemplo, que abren con el valor del eje
#:     en mayúsculas (MISE EN PLACE DE MAÑANA / PARTIDA DE FRÍO / SUMILLER…);
#:   · la columna «Zona» de esas tres filas y, SÓLO en «Plantilla C»,
#:     «Responsable» — que es lo que §2.3 pide para «Por Perfil» y lo que
#:     distingue a C de las otras dos de un vistazo.
#:
#: Lo que NO se toca, a propósito:
#:   · el NOMBRE de la pestaña («Plantilla A»), que es el ancla de este módulo
#:     y de las Instrucciones del fichero;
#:   · la fila 2, que en los 11 ficheros P4 de este kit es la MISMA línea de
#:     marca («AI Chef Pro · aichef.pro — Kit de Tareas: Restaurante Creativo /
#:     De Autor»): cambiarla sólo en tres hojas rompería la uniformidad del
#:     producto entero para decir algo que ya dice A1;
#:   · el contador (fila 30), el rango que cuenta, el merge, los anchos y las
#:     alturas: las filas de ejemplo siguen siendo las tres primeras LIBRES
#:     dentro del rango y siguen marcadas «N/A».
#:
#: Los rótulos van a 39-46 caracteres. Es el margen medido del kit: los A1 del
#: molde P4 van de 16 a 57 caracteres (el más largo, «Mantenimiento Trimestral
#: y Anual — Revisiones Contratadas», lo escribe este mismo módulo en 05) y
#: ninguno lleva altura de fila propia, así que pasarse obligaría a fijar la
#: altura de una celda combinada — maquetación, justo lo que no se toca.
PLANTILLAS = ('Plantilla A', 'Plantilla B', 'Plantilla C')
GRIS_EJEMPLO = 'FF999999'

#: Por qué estos tres ejes y no otros: son los que pide el orquestador sobre
#: la §2.3 y los que ya promete la landing del producto («por partida, por
#: turno y por perfil»); «franja horaria» es además el nombre canónico de la
#: familia (`motor.SINONIMOS_07` mapea «por turno» fuera y «por franja» →
#: «Por Franja Horaria»).
#:
#: Cada hoja lleva TRES ejemplos —los mismos tres que ya tenía, no se añade ni
#: se quita ninguna fila— y el eje de B y de C tiene CUATRO valores, así que
#: el cuarto (pastelería · jefe de partida) no tiene ejemplo escrito: se
#: enumera en las Instrucciones. Preferible a meter dos partidas en una línea,
#: que es exactamente el duplicado que este módulo persigue en el resto del
#: kit.
EJES = {
    'Plantilla A': {
        'rotulo': 'Plantilla Personalizable A — Por Franja Horaria',
        'eje': 'franja horaria',
        'valores': 'mise en place de mañana, pase y cierre',
        'ejemplos': (
            ('Ejemplo — MISE EN PLACE DE MAÑANA (escribe encima o borra la '
             'fila): sacar las pre-elaboraciones del día y cotejarlas con el '
             'pase del menú degustación', 'Mise en place', None),
            ('Ejemplo — PASE (escribe encima o borra la fila): briefing con '
             'la brigada antes del primer pase — comensales, alérgenos y '
             'storytelling', 'Pase', None),
            ('Ejemplo — CIERRE (escribe encima o borra la fila): anotar las '
             'mermas del día (producto, cantidad y motivo) y cerrar cámaras '
             'y pase', 'Cocina', None),
        ),
    },
    'Plantilla B': {
        'rotulo': 'Plantilla Personalizable B — Por Partida',
        'eje': 'partida',
        'valores': 'I+D, frío, caliente y pastelería',
        'ejemplos': (
            ('Ejemplo — PARTIDA DE I+D (escribe encima o borra la fila): '
             'cerrar la ficha del plato nuevo — pases, orden en el menú y '
             'tiempos', 'I+D', None),
            ('Ejemplo — PARTIDA DE FRÍO (escribe encima o borra la fila): '
             'repasar encurtidos, fermentados y flores comestibles del menú',
             'Frío', None),
            ('Ejemplo — PARTIDA DE CALIENTE (escribe encima o borra la '
             'fila): baños térmicos, fondos y salsas a punto antes del primer '
             'pase', 'Caliente', None),
        ),
    },
    'Plantilla C': {
        'rotulo': 'Plantilla Personalizable C — Por Perfil',
        'eje': 'perfil',
        'valores': ('jefe de cocina, jefe de partida, sumiller y jefe de '
                    'sala'),
        'ejemplos': (
            ('Ejemplo — JEFE DE COCINA (escribe encima o borra la fila): '
             'validar escandallo y ficha del plato nuevo antes de que entre '
             'en el menú', 'Cocina', 'Jefe de cocina'),
            ('Ejemplo — SUMILLER (escribe encima o borra la fila): repasar el '
             'maridaje pase a pase y las botellas abiertas (nivel y fecha)',
             'Bodega', 'Sumiller'),
            ('Ejemplo — JEFE DE SALA (escribe encima o borra la fila): '
             'repartir rangos y repasar alérgenos por mesa con la brigada de '
             'sala', 'Sala', 'Jefe de sala'),
        ),
    },
}

#: Las dos líneas de «Instrucciones» que este cambio deja MINTIENDO. La
#: primera decía «hojas en blanco» cuando ya traen ejemplos —el mismo desfase
#: que el verificador anotó sobre la landing— y la segunda afirmaba
#: literalmente lo que la SPEC §2.3 prohíbe. Sustitución 1:1, sin mover filas.
INSTR_09 = [
    ('▸ Usa estas hojas en blanco para crear tus propios checklists.',
     '▸ Usa estas tres hojas para montar tus propios checklists: cada una '
     'trae tres filas de ejemplo que puedes reescribir o borrar.'),
    ('▸ Las 3 plantillas son idénticas para que tengas margen.',
     '▸ Cada plantilla va por un eje distinto (A franja horaria · B partida · '
     'C perfil): el detalle, más abajo.'),
]


def _fila_ejemplo(ws, fila, texto, zona, marca, responsable=None):
    """Fila de ejemplo: tarea normal + marca «N/A» + gris y cursiva.

    `responsable` sólo lo usa «Plantilla C»: en el eje POR PERFIL el dato que
    diferencia la fila es la persona, y §2.3 pide precisamente «Responsable
    precargado» en esa hoja. En A y B se deja vacía, como en todo el molde P4
    de este kit.
    """
    _escribir_tarea(ws, fila, texto, zona)
    ws.cell(row=fila, column=marca).value = 'N/A'
    if responsable:
        ws.cell(row=fila, column=4).value = responsable
    for c in range(1, NCOL + 1):
        cel = ws.cell(row=fila, column=c)
        f = cel.font
        cel.font = motor.Font(name=f.name, sz=f.sz, b=f.b, i=True,
                              underline=f.underline, strike=f.strike,
                              color=GRIS_EJEMPLO)


def _f09(wb, cambios):
    tocado = False
    for titulo in PLANTILLAS:
        if titulo not in wb.sheetnames:
            raise AnclaPerdida('09-plantilla-personalizable: no encuentro la '
                               'hoja «{}»'.format(titulo))
        ws = wb[titulo]
        cfg = EJES[titulo]
        ejemplos = cfg['ejemplos']
        # 1) El rótulo de la hoja dice de qué EJE es. Va primero y aparte del
        #    bloque de ejemplos: si compartiera el `continue` de más abajo, la
        #    2.ª pasada saltaría el rótulo sin haberlo comprobado nunca.
        if ws.cell(row=1, column=1).value != cfg['rotulo']:
            ws.cell(row=1, column=1).value = cfg['rotulo']
            cambios.append('«{}»: el rótulo A1 pasa a «{}» — las tres hojas '
                           'eran la MISMA plantilla renombrada (DOM-07 '
                           'residual, SPEC §2.3)'
                           .format(titulo, cfg['rotulo']))
            tocado = True
        if _fila(ws, ejemplos[0][0]) is not None:
            continue                                   # ya están (2.ª pasada)
        g = motor.geometria_p4(ws)
        if not g:
            raise AnclaPerdida('«{}»: no es una hoja del molde P4'
                               .format(titulo))
        # Sólo filas LIBRES y DENTRO del rango que cuenta el contador
        # (`hr+1` … `contador-1`): ni se inserta ni se desplaza nada.
        tope = g['contador'] or ws.max_row + 1
        libres = []
        for r in range(g['hr'] + 1, tope):
            if any(ws.cell(row=r, column=c).value is not None
                   for c in range(1, NCOL + 1)):
                continue
            libres.append(r)
            if len(libres) == len(ejemplos):
                break
        if len(libres) < len(ejemplos):
            cambios.append('«{}»: NO se han puesto las filas de ejemplo — '
                           'sólo hay {} filas libres dentro del rango del '
                           'contador y hacen falta {} (DOM-07)'
                           .format(titulo, len(libres), len(ejemplos)))
            continue
        for fila, (texto, zona, resp) in zip(libres, ejemplos):
            _fila_ejemplo(ws, fila, texto, zona, g['marca'], resp)
        _renumerar_p4(ws)
        cambios.append('«{}»: {} filas de EJEMPLO en gris y cursiva, una por '
                       'cada valor del eje POR {} ({}), marcadas «N/A» para '
                       'que no cuenten en el contador ni en el recuento del '
                       'producto — DOM-07'
                       .format(titulo, len(ejemplos), cfg['eje'].upper(),
                               cfg['valores']))
        tocado = True
    ws_i = wb['Instrucciones'] if 'Instrucciones' in wb.sheetnames else None
    if ws_i is not None:
        for viejo, nuevo in INSTR_09:
            if _sustituir(ws_i, viejo, nuevo) is not None:
                cambios.append('Instrucciones: «{}» → «{}» (DOM-07 residual: '
                               'la hoja ya no está en blanco y las tres '
                               'plantillas ya no son idénticas)'
                               .format(viejo, nuevo))
                tocado = True
    if _instrucciones(wb, 'Cada plantilla tiene su propio eje:', [
            'Plantilla A — POR FRANJA HORARIA: una fila por momento del día '
            '(mise en place de mañana, pase y cierre). Es la que se imprime y '
            'se cuelga en el pase.',
            'Plantilla B — POR PARTIDA: una fila por partida (I+D, frío, '
            'caliente y pastelería). Reparte el trabajo del menú entre quien '
            'lo ejecuta.',
            'Plantilla C — POR PERFIL: una fila por persona (jefe de cocina, '
            'jefe de partida, sumiller y jefe de sala), con el perfil escrito '
            'en la columna «Responsable».',
            'Los ejemplos cubren tres valores de cada eje; el cuarto de B '
            '(pastelería) y el de C (jefe de partida) los escribes tú en la '
            'primera fila verde libre.']):
        cambios.append('Instrucciones: qué eje lleva cada plantilla y qué '
                       'valores cubre — DOM-07 residual (SPEC §2.3)')
        tocado = True
    if _instrucciones(wb, 'Las tres filas de ejemplo:', [
            'Cada plantilla arranca con tres filas de EJEMPLO en gris y en '
            'cursiva: están para enseñarte el nivel de detalle que funciona, '
            'no para hacerlas. Escribe encima o bórralas.',
            'Van marcadas «N/A» a propósito, que es como no cuentan en '
            '«Tareas completadas». Si escribes tu tarea sobre una de ellas, '
            'cambia esa marca o la fila seguirá sin sumar.',
            'El vocabulario es el de esta casa (menú degustación, mise en '
            'place, pase, partidas, maridaje): cámbialo por el tuyo.']):
        cambios.append('Instrucciones: qué son las tres filas de ejemplo y por '
                       'qué van marcadas «N/A» — DOM-07')
        tocado = True
    return tocado


# ==========================================================================
# BONUS-02-calendario-anual.xlsx — fechas del calendario español
# ==========================================================================
#: DOM-20 (equivalente) — el calendario de este kit es POR MES (una celda de
#: prosa por mes), no una lista de fechas, así que las cinco del representante
#: se añaden dentro de la celda de su mes en lugar de como filas nuevas. Se
#: comprobó una a una cuáles faltaban: Año Nuevo, San Valentín, Semana Santa,
#: Navidad, Nochebuena y Nochevieja YA estaban; Día del Padre, comuniones
#: (abr-jun), Día de la Madre, 15 de agosto, 1 de noviembre y el puente del
#: 6-8 de diciembre NO aparecían en ninguna de las doce celdas.
FECHAS = [
    ('Marzo',
     'CAMBIO CARTA PRIMAVERA. Espárragos, guisantes, habas. Sesiones I+D '
     'nuevos platos primavera. Festival gastronómico local (revisar).',
     'CAMBIO CARTA PRIMAVERA. Espárragos, guisantes, habas. Sesiones I+D '
     'nuevos platos primavera. 19 mar — Día del Padre: mediodía familiar, '
     'menú especial. Festival gastronómico local (revisar).'),
    ('Abril',
     'Carta primavera rodada. Semana Santa: aforo alto, menú especial. '
     'Alcachofas, flores comestibles. Preparar pop-up de temporada.',
     'Carta primavera rodada. Semana Santa: aforo alto, menú especial. '
     'Arranca la temporada de comuniones (abr-jun): grupos familiares de '
     'mediodía, menú cerrado y reserva con antelación. Alcachofas, flores '
     'comestibles. Preparar pop-up de temporada.'),
    ('Mayo',
     'Cerezas, fresas, nísperos. Espárragos trigueros. Atún rojo (inicio '
     'temporada). Preparar cambio carta verano.',
     'Comuniones en plena temporada + Día de la Madre (1.er domingo): dos de '
     'los mediodías más llenos del año. Cerezas, fresas, nísperos. Espárragos '
     'trigueros. Atún rojo (inicio temporada). Preparar cambio carta verano.'),
    ('Junio',
     'CAMBIO CARTA VERANO. Tomates de temporada, melocotón, albaricoque. '
     'Gazpachos y sopas frías de autor. Terraza / cenas al aire libre.',
     'CAMBIO CARTA VERANO. Últimas comuniones del año. Tomates de temporada, '
     'melocotón, albaricoque. Gazpachos y sopas frías de autor. Terraza / '
     'cenas al aire libre.'),
    ('Agosto',
     'Verano alta ocupación. Pimientos, berenjenas, calabacín. Helados de '
     'autor (producción extra). Prep. cambio carta otoño.',
     'Verano alta ocupación. 15 ago (Asunción): festivo nacional, aforo alto y '
     'plantilla de vacaciones — cierra los turnos con semanas de antelación. '
     'Pimientos, berenjenas, calabacín. Helados de autor (producción extra). '
     'Prep. cambio carta otoño.'),
    ('Noviembre',
     'Trufa negra (inicio temporada). Caza mayor y menor. Prep. menús '
     'Navidad. Reservas navideñas abiertas.',
     '1 nov (Todos los Santos): puente y aforo alto. Trufa negra (inicio '
     'temporada). Caza mayor y menor. Prep. menús Navidad. Reservas navideñas '
     'abiertas.'),
    ('Diciembre',
     'CAMBIO CARTA INVIERNO. Menús Navidad, Nochebuena, Nochevieja. Trufa, '
     'foie, marisco, caviar. Máxima facturación del año.',
     'CAMBIO CARTA INVIERNO. Puente 6-8 dic (Constitución e Inmaculada): tres '
     'días seguidos de aforo alto, justo antes de las comidas de empresa. '
     'Menús Navidad, Nochebuena, Nochevieja. Trufa, foie, marisco, caviar. '
     'Máxima facturación del año.'),
]


def _bonus02(wb, cambios):
    ws = wb['Calendario Anual']
    nuevas = 0
    for mes, viejo, nuevo in FECHAS:
        fila = _fila(ws, mes, 1)
        if fila is None:
            raise AnclaPerdida('«Calendario Anual»: no encuentro el mes «{}»'
                               .format(mes))
        actual = ws.cell(row=fila, column=2).value
        if actual == nuevo:
            continue
        if actual != viejo:
            raise AnclaPerdida('«Calendario Anual»: «{}» no tiene el texto '
                               'que este módulo esperaba'.format(mes))
        ws.cell(row=fila, column=2).value = nuevo
        nuevas += 1
    if nuevas:
        cambios.append('«Calendario Anual»: {} meses con las fechas del '
                       'calendario español que faltaban (Día del Padre, '
                       'comuniones abr-jun, Día de la Madre, 15 de agosto, '
                       '1 de noviembre y el puente del 6-8 de diciembre); Año '
                       'Nuevo, San Valentín, Semana Santa y Navidad ya '
                       'estaban — DOM-20 (equivalente)'.format(nuevas))
    return False


# ==========================================================================
# API
# ==========================================================================
FICHEROS = {
    '01-apertura-cierre.xlsx': _f01,
    '02-mise-en-place-degustacion.xlsx': _f02,
    '04-tareas-brigada-creativa.xlsx': _f04,
    '05-tareas-semanales-mensuales.xlsx': _f05,
    '07-chefs-table-eventos.xlsx': _f07,
    '09-plantilla-personalizable.xlsx': _f09,
    'BONUS-02-calendario-anual.xlsx': _bonus02,
}

#: Ficheros del molde P4 a los que sólo hay que aplicarles la normalización
#: transversal de grados (no tienen cambios de contenido propios).
SOLO_GRADOS = ('03-id-desarrollo-menu.xlsx', '06-sumiller-maridajes.xlsx',
               '08-fotografia-storytelling.xlsx',
               'BONUS-01-briefing-servicio.xlsx')


def post(wb, fname, cambios):
    """CONTENIDO sobre un libro ya normalizado por `motor.aplicar`.

    Devuelve True si ha cambiado la ESTRUCTURA. En el molde P4 ese valor no lo
    usa `main.py` (no hay 2.ª pasada del motor porque `aplicar` devolvió `{}`),
    así que la reconstrucción del contador, del formato condicional y del
    desplegable se hace AQUÍ antes de salir.
    """
    fn = FICHEROS.get(fname)
    if fn is None and fname not in SOLO_GRADOS:
        return False
    tocado = bool(fn(wb, cambios)) if fn else False
    for ws in wb.worksheets:
        _normalizar_grados(ws, cambios)
    # Contador honesto y formato condicional con la geometría NUEVA. Es
    # idempotente: en la 2.ª pasada `motor.aplicar` ya lo dejó así y esto no
    # encuentra nada que cambiar.
    #
    # El registro se vacía ANTES porque las coordenadas que anotó `aplicar` son
    # las de la geometría VIEJA: al insertar diez filas en «Apertura AM» el
    # contador baja de la fila 36 a la 46 y `main.py` seguiría preguntando por
    # el cache de E36 —una celda que ahora es una tarea— y lo declararía
    # «fórmula sin valor». Lo único que hay en el registro de un fichero P4 son
    # los contadores, y `normalizar_p4` los vuelve a registrar todos con su
    # coordenada actual.
    motor.REGISTRO.clear()
    motor.normalizar_p4(wb, cambios)
    return tocado
