#!/usr/bin/env python3
"""
contenido_kit_tareas_chocolateria.py — CONTENIDO propio de
«kit-tareas-chocolateria» (hermano de la familia, §5 de `kit-tareas-v2-SPEC.md`).

Fuente de los cambios: `auditorias/kit-tareas-hermanos/
kit-tareas-chocolateria-verif.json` campo `contenido_pendiente` (2 medias, 1
baja) más los equivalentes de §3 del representante que aplican a una
chocolatería / bombonería con obrador y tienda. Sobre motor 2.3 se añaden los
dos `hallazgos_nuevos` de severidad media de `…-ver2.json` (tanda 3): el
criterio de paso/no-paso del test de templado, que sólo estaba escrito para el
chocolate negro, y DOM-09 —tres tareas de 01 que duplicaban hitos de 08 y 09
sin remisión—. DOM-09 es de MOTOR, pero `colapsar_duplicados` sólo corre en el
molde ▸ y aquí 01 es P4: se resuelve desde contenido, reescribiendo las tres
filas 1:1 (ninguna se borra) como comprobación con la referencia «(hito en
08/09)».

`main.py` lo carga sólo con `--producto kit-tareas-chocolateria` (compone el
nombre del módulo con el pid: `contenido_` + pid con guiones bajos), así que
aquí se puede hablar de «Templado», «Moldeado» o «Dependiente» por su nombre:
son hojas de ESTE kit.

Contrato con `main.py`:
    post(wb, fname, cambios) -> bool

DOS MOLDES EN EL MISMO PRODUCTO — la diferencia que lo condiciona todo
================================================================================
`motor.aplicar` sólo reconoce el molde «▸» en 08 y 09 (medido: «en alcance
2/11»). Los 01-07 y los dos BONUS son molde P4 y reciben únicamente la
normalización mínima (`motor.normalizar_p4`: desplegable, contador honesto,
formato condicional y bio). En consecuencia:

  · P4 — `motor.aplicar` devuelve `{}` (falsy), así que `main.py` **NO vuelve a
    pasar el motor** tras `post()` ni llama a `motor.cerrar`. Todo lo que
    dependa de la geometría nueva —rango del contador, formato condicional,
    desplegable de las filas nuevas, A4 y pie de una hoja nueva— **lo tiene que
    dejar hecho este módulo**. Por eso `post()` termina llamando a
    `motor.normalizar_p4` y por eso existen `_dv_extender`, `_freeze` y
    `_hoja_legal`.
  · P4 — `motor.textos_de_tarea` (y con él `texto_grados` y `texto_appcc`)
    tampoco corre: medido en `02-partidas-produccion.xlsx:Templado:B14`, que
    seguía con «50-55°C» pegado después del motor. Lo aplica aquí
    `_normalizar_textos`, al FINAL de cada fichero, y todos los textos nuevos
    de este módulo ya se escriben en su forma final para que la 2.ª pasada no
    encuentre nada que cambiar (DOM-R2-22).
  · P4 — el molde REPITE la fila de cabecera («# | Tarea | Zona | Responsable |
    ✓ | Hora | Notas») en cada sección y **reinicia la numeración en 1** dentro
    de cada bloque: `motor.renumerar` (que va por `motor.geometria`, del molde
    ▸) devuelve None aquí. La numeración la rehace `_renumerar_p4`.
  · P4 — «Responsable» y «Hora» van VACÍAS en las 11 hojas del molde (son
    verdes, las rellena el cliente). Las tareas nuevas respetan eso y sólo
    escriben #, Tarea y Zona. La única excepción documentada es la hoja nueva
    «Trimestral y Anual», donde la cadencia ES el dato.
  · ▸ (08 y 09) — aquí es al revés: `post()` devuelve True, `main.py` vuelve a
    pasar `motor.aplicar` y luego `motor.cerrar`, así que las filas nuevas
    heredan verdes, desplegable, formato condicional, protección y las
    precargas de Responsable/Hora sin que este módulo toque nada de eso. Sólo
    hay que dejar un entero en la columna «#» y renumerar con
    `motor.renumerar`. Y **no se tocan sus «Instrucciones»**: las reescribe
    entera `motor.reescribir_instrucciones` y cualquier línea que se añadiera
    aquí se perdería en el mismo guardado.

ANCLAS: el texto que se busca es el que el motor YA DEJÓ
================================================================================
`post()` corre DESPUÉS de `motor.aplicar`, así que en 08/09 los textos vienen
pasados por `forma_estable` y en P4 (2.ª pasada) por el `_normalizar_textos` de
este módulo. Por eso `_fila` normaliza LOS DOS LADOS con la misma función y
`_NORM` cambia según el molde del fichero en curso: si se comparase el literal
crudo, la 1.ª pasada encontraría el ancla y la 2.ª no, y el gate de
idempotencia se caería con «hoja sólo en una pasada».

QUÉ NO SE HA APLICADO (y por qué), del §3 del representante
================================================================================
  · **anisakis** (DOM-02): no hay pescado, ni crudo ni de ninguna clase, en las
    11 hojas del kit. Meterlo sería ruido en un obrador de chocolate.
  · **aceite de freidora en frío** (DOM-27): no hay freidora ni fritura.
  · **backflush del grupo de café / lavavajillas** (DOM-15): no hay cafetera
    ni tren de lavado; el equipo semanal de este kit es la temperadora.
  · **tabla de vida útil en CONGELACIÓN** (DOM-29): se ha portado como tabla de
    **conservación**, que es lo que un obrador de chocolate necesita. Congelar
    chocolate acabado es un error de oficio —la condensación al descongelar
    disuelve el azúcar de la superficie y deja *sugar bloom*—, así que la tabla
    lo dice explícitamente y reserva la congelación para el granel de ganache.
  · **07 diferenciado** (§2.3): es MOTOR (`motor.diferenciar_07`), y en este kit
    el 07 es molde P4, fuera de su alcance. No se toca desde contenido.

BARRIDO DE VOCABULARIO DE SALA EN 08/09 (tanda 5)
================================================================================
`…-ver3.json` señaló como BAJA que el 08 —el único fichero del kit con el molde
genérico de los 12 hermanos— seguía hablando como un restaurante con comedor.
Barridos los dos ficheros del molde ▸ y sus «Instrucciones» con «carta»,
«pizarra», «menú», «mesa» y «comensal», el censo son SEIS celdas, todas en
`08:'Apertura del Negocio'` menos la última:

  · B9 «pizarra de menú», B11 «sistema de reservas», B13 «reservas del día»,
    B16 «(sillas, mesas, iluminación)» y B18 «las cartas/menús» → reescritas
    1:1 (constantes `SENALIZACION`, `VITRINA_ENCENDER`, `ENCARGOS_08`,
    `MOBILIARIO` y `VITRINA_ETIQUETAS`).
  · B17 «Montar terraza si aplica (mesas, sillas, sombrillas/estufas)» → **SE
    QUEDA**, justificada: es la única de las seis que va CONDICIONADA («si
    aplica»), describe una terraza —donde sí hay mesas y sillas— y tiene
    pareja en el cierre (`'Cierre del Negocio'!B7`, «Limpiar y recoger terraza
    si aplica»). Una chocolatería con degustación es un caso real del oficio y
    reescribirla le quitaría al cliente una tarea que puede necesitar; lo que
    no era honesto es afirmar sillas y mesas como el mobiliario del local, que
    es lo que decía B16 sin condicionar. Es además el caso que `critico-2.json`
    tiene abierto como DECISIÓN DEL ORQUESTADOR para toda la familia.
  · Ni «comensal» ni «menú» aparecen en 09, y las «Instrucciones» de 08 y 09
    —que reescribe entera `motor.reescribir_instrucciones`— no contienen
    ninguno de los cinco términos.

FUERA DE ESTE BARRIDO, PERO MEDIDO (para el orquestador)
================================================================================
El mismo vocabulario sobrevive en dos celdas de los ficheros P4, que el encargo
de esta tanda no incluía: `01-apertura-cierre.xlsx:'Apertura'!B21` («Colocar
pizarra con novedades y productos destacados» — defendible: es una pizarra de
NOVEDADES dentro de la tienda, no una carta) y
`03-tareas-manager.xlsx:'Mensual'!B20` («Actualizar carta y etiquetado si hay
cambios» — aquí «carta» sí es el término del restaurante; en una bombonería lo
que se actualiza es el SURTIDO). No se tocan sin encargo: quedan citadas para
que el orquestador decida.
"""
import copy

import motor
from motor import get_column_letter as L

#: Las 10 hojas de checklist del molde P4 de este kit son A:G; el calendario,
#: A:F (y no es P4: su cabecera no tiene columna «Tarea»).
NCOL = 7

#: Relleno de la columna «Zona» por valor, medido en las 11 hojas del kit. Se
#: usa sólo como último recurso: `_zona` prefiere copiar el estilo de una fila
#: real con esa misma zona —primero de la propia hoja, luego del libro—, que
#: además trae bordes y fuente.
ZONA_COLOR = {
    'Admin': 'FFF8E1', 'Gestión': 'FFF8E1', 'Equipo': 'FFF8E1',
    'RRSS': 'FFF8E1', 'Obrador': 'FFF3E0', 'Templado': 'FFF3E0',
    'Moldeado': 'FFF3E0', 'Envasado': 'FFF3E0', 'Producción': 'FFF3E0',
    'Conservación': 'E0F7FA', 'Cámara': 'E0F7FA', 'Vitrina': 'E3F2FD',
    'Mostrador': 'F3E5F5', 'Packaging': 'F1F8E9', 'Limpieza': 'EFEBE9',
    'Tienda': 'E8F5E9', 'Almacén': 'E8F5E9', 'Caja': 'E8F5E9',
    'General': 'E8F5E9', 'Logística': 'E8F5E9',
}


class AnclaPerdida(RuntimeError):
    """El texto que este módulo esperaba encontrar ya no está en la hoja."""


# ==========================================================================
# Normalización de anclas (depende del molde del fichero en curso)
# ==========================================================================
def _norm_p4(v):
    """Lo que `_normalizar_textos` deja en las hojas del molde P4."""
    return motor.texto_appcc(motor.texto_grados(v))


def _norm_trio(v):
    """Lo que `motor.textos_de_tarea` deja en 08 y 09 (molde ▸)."""
    return motor.forma_estable(v)


#: Lo fija `post()` antes de tocar cada fichero. Global y no parámetro porque
#: `main.py` procesa los 11 ficheros en SERIE y así las ~40 llamadas a `_fila`
#: no arrastran el mismo argumento.
_NORM = _norm_p4


def _norm(v):
    return _NORM(v) if isinstance(v, str) else v


# ==========================================================================
# Utilidades de anclaje
# ==========================================================================
def _fila(ws, texto, col=2):
    texto = _norm(texto)
    for r in range(1, ws.max_row + 1):
        if _norm(ws.cell(row=r, column=col).value) == texto:
            return r
    return None


def _exige(ws, texto, col=2):
    r = _fila(ws, texto, col)
    if r is None:
        raise AnclaPerdida(f'«{ws.title}»: no encuentro '
                           f'{L(col)}=«{texto}» (kit-tareas-chocolateria)')
    return r


def _estilos(ws, fila, ncol=NCOL):
    return [copy.copy(ws.cell(row=fila, column=c)._style)
            for c in range(1, ncol + 1)]


def _pintar(ws, fila, estilos):
    for c, st in enumerate(estilos, start=1):
        ws.cell(row=fila, column=c)._style = copy.copy(st)


def _zona(ws, fila, valor):
    """Escribe la Zona y le pone el relleno que esa zona tiene en el kit.

    Copiar el estilo de la fila de anclaje pintaría la zona equivocada: el color
    de la columna «Zona» depende del VALOR (medido: Admin FFF8E1, Templado
    FFF3E0, Conservación E0F7FA, Vitrina E3F2FD, Mostrador F3E5F5, Packaging
    F1F8E9, Limpieza EFEBE9, Tienda/Almacén/Caja E8F5E9). Se busca primero en
    la PROPIA hoja porque «Obrador» y «Tienda» no llevan el mismo color en
    todos los libros.
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
    """Fila de tarea del molde P4: # (lo pone `_renumerar_p4`), Tarea y Zona."""
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


def _fila_en_seccion(ws, banda, texto, col=2):
    """Como `_fila`, pero acotado a la sección cuya banda (columna A) es `banda`.

    En «Templado» el texto de fábrica «Test de templado y registrar lote» está
    DOS veces —una en «Chocolate con leche» y otra en «Chocolate blanco»,
    medido en el fichero de origen— y `_fila` devuelve siempre la primera. Sin
    acotar, las dos sustituciones caerían sobre la misma fila o dependerían del
    orden en que se llamen, que es justo la clase de acierto por casualidad que
    §2.5 prohíbe (un regex sin acotar no falla: acierta en el sitio
    equivocado).

    El corte de la sección es la siguiente celda de la columna A que sea texto
    y no la «#» de la cabecera repetida: la banda de la sección siguiente o,
    al final del cuerpo, la fila de firma.
    """
    ini = _exige(ws, banda, 1)
    texto = _norm(texto)
    for r in range(ini + 1, ws.max_row + 1):
        v = ws.cell(row=r, column=1).value
        if isinstance(v, str) and v != '#':
            return None
        if _norm(ws.cell(row=r, column=col).value) == texto:
            return r
    return None


def _sustituir_en_seccion(ws, banda, viejo, nuevo, col=2):
    """`_sustituir` acotado a una sección. Devuelve la fila, o None si ya estaba."""
    if _fila(ws, nuevo, col) is not None:
        return None
    r = _fila_en_seccion(ws, banda, viejo, col)
    if r is None:
        raise AnclaPerdida(f'«{ws.title}» / «{banda}»: no encuentro '
                           f'{L(col)}=«{viejo}» (kit-tareas-chocolateria)')
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
    huérfano visualmente y, sobre todo, rompería la simetría que el contador da
    por hecha al restar `COUNTIF(B,"Tarea")`.
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
    motor._merge(ws, f'A{idx}:{L(NCOL)}{idx}')
    _pintar(ws, idx + 1, est_cab)
    for c, v in enumerate(cabecera, start=1):
        ws.cell(row=idx + 1, column=c).value = v
    for i, (texto, zona) in enumerate(tareas):
        _pintar(ws, idx + 2 + i, est_tarea)
        _escribir_tarea(ws, idx + 2 + i, texto, zona)
    return True


def _seccion_final(ws, titulo, tareas):
    """Sección nueva al FINAL del cuerpo, justo encima del contador.

    `_insertar_seccion` necesita una banda DELANTE de la cual meterse, y para
    un bloque de fin de semana eso obliga a colarlo antes del viernes: la hoja
    quedaría lunes, martes, miércoles, jueves, SÁBADO Y DOMINGO, viernes.
    TEC-17 pide orden cronológico, así que aquí se inserta en la fila del
    contador —que baja— con la fila en blanco de separación que el molde pone
    delante de cada banda.
    """
    if _fila(ws, titulo, 1) is not None:
        return False
    g = motor.geometria_p4(ws)
    if not g or not g['contador']:
        raise AnclaPerdida(f'«{ws.title}»: sin contador, no sé dónde acaba el '
                           'cuerpo')
    banda = next((r for r in range(g['hr'] - 1, g['contador'])
                  if motor.es_fila_seccion(ws, r)), None)
    if banda is None or banda < 2:
        raise AnclaPerdida(f'«{ws.title}»: no encuentro ninguna banda de '
                           'sección de la que copiar el estilo')
    idx = g['contador']
    est_blanco = _estilos(ws, banda - 1)
    est_banda = _estilos(ws, banda)
    est_cab = _estilos(ws, g['hr'])
    est_tarea = _estilos(ws, g['hr'] + 1)
    cabecera = [ws.cell(row=g['hr'], column=c).value
                for c in range(1, NCOL + 1)]
    motor.insertar_filas(ws, idx, len(tareas) + 3)
    _pintar(ws, idx, est_blanco)
    for c in range(1, NCOL + 1):
        ws.cell(row=idx, column=c).value = None
    _pintar(ws, idx + 1, est_banda)
    ws.cell(row=idx + 1, column=1).value = titulo
    motor._merge(ws, f'A{idx + 1}:{L(NCOL)}{idx + 1}')
    _pintar(ws, idx + 2, est_cab)
    for c, v in enumerate(cabecera, start=1):
        ws.cell(row=idx + 2, column=c).value = v
    for i, (texto, zona) in enumerate(tareas):
        _pintar(ws, idx + 3 + i, est_tarea)
        _escribir_tarea(ws, idx + 3 + i, texto, zona)
    return True


def _renumerar_p4(ws):
    """Numeración del molde P4: reinicia en 1 en CADA sección."""
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


def _freeze(ws):
    """Reancla el panel inmovilizado a la cabecera REAL.

    Las 10 hojas P4 se entregan con `freeze_panes='A6'` porque su cabecera está
    en la 5. La sección de higiene de «Apertura» se inserta ANTES de la primera
    banda, así que la cabecera baja nueve filas y el panel congelado se quedaba
    partiendo el bloque nuevo por la mitad: al desplazarse, la fila que queda
    fija arriba deja de ser «# | Tarea | Zona | …».
    """
    g = motor.geometria_p4(ws)
    if g and ws.freeze_panes:
        ws.freeze_panes = f'A{g["hr"] + 1}'


def _es_tarea(ws, cel):
    """La celda es el TEXTO de una tarea, no un rótulo ni una banda.

    `motor.textos_de_tarea` acota §2.5 con `col_tarea` por esto mismo, y en
    este kit importa: la banda de sección `05:Mensual!A20` se llama «APPCC y
    seguridad» y sin acotar salía impresa como «APPCC y seguridad (si tienes el
    Pack APPCC, regístralo allí; si no, anótalo junto a la tarea)» — una
    coletilla de registro colgando de un TÍTULO. Medido en la 1.ª versión de
    este módulo.
    """
    return (cel.column == 2 and cel.value != 'Tarea'
            and not motor.es_fila_seccion(ws, cel.row))


def _normalizar_textos(ws, cambios):
    """DOM-R2-22 y §2.5 en el molde P4, al que `motor.textos_de_tarea` no llega.

    Se aplican las DOS que el motor aplica a todo el corpus: el signo menos
    tipográfico con espacio antes de la unidad (en TODA la hoja) y la
    referencia honesta al Pack APPCC (sólo en la columna «Tarea», igual que
    hace el motor con `col_tarea`). `texto_temperatura` NO se aplica aquí a
    propósito: en P4 el motor tampoco la aplica y los objetivos de este kit no
    son los genéricos de refrigeración, sino los del chocolate (16-18 °C en
    vitrina, 15-18 °C en conservación), que se escriben a mano tarea por tarea.
    """
    n = 0
    for row in ws.iter_rows():
        for c in row:
            if not isinstance(c.value, str):
                continue
            nuevo = motor.texto_grados(c.value)
            if _es_tarea(ws, c):
                nuevo = motor.texto_appcc(nuevo)
            if nuevo != c.value:
                c.value = nuevo
                n += 1
    if n:
        cambios.append(f'«{ws.title}»: {n} textos normalizados (grados con '
                       'signo menos tipográfico y espacio antes de la unidad, '
                       'referencia honesta al Pack APPCC) — DOM-R2-22 / §2.5, '
                       'que el motor no aplica al molde P4')
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
# Utilidades del molde ▸ (08 y 09) — el motor vuelve a pasar detrás
# ==========================================================================
def _insertar_trio(ws, ancla, tareas):
    """Filas nuevas en un checklist ▸ debajo de la fila cuya B es `ancla`.

    Sólo se escribe «#» y «Tarea»: `motor.precargar_negocio` /
    `precargar_caja` rellenan Responsable y Hora en la 2.ª pasada del motor,
    y `normalizar_checklist` pinta los verdes, el desplegable y el formato
    condicional. Escribirlos aquí a mano los dejaría fuera del escalonado de
    horas que el motor calcula sobre el número TOTAL de tareas.
    """
    if _fila(ws, tareas[0]) is not None:
        return False
    g = motor.geometria(ws)
    if not g:
        raise AnclaPerdida(f'«{ws.title}»: no es un checklist del molde ▸')
    ncol = motor.ncol_cabecera(ws, g['hr'])
    r = _exige(ws, ancla)
    est = _estilos(ws, r, ncol)
    motor.insertar_filas(ws, r + 1, len(tareas))
    for i, texto in enumerate(tareas):
        f = r + 1 + i
        _pintar(ws, f, est)
        for c in range(1, ncol + 1):
            ws.cell(row=f, column=c).value = None
        ws.cell(row=f, column=1).value = 0
        ws.cell(row=f, column=2).value = texto
    motor.renumerar(ws)
    return True


# ==========================================================================
# 01-apertura-cierre.xlsx — «Apertura» y «Cierre» de chocolatería
# ==========================================================================
#: DOM-12 + DOM-13 (equivalentes) — la hoja arrancaba la jornada en «Encendido y
#: verificación de equipos»: nadie se lava las manos, nadie enciende la
#: extracción y nadie mira la llave del gas antes de poner en marcha la
#: temperadora. En un obrador de chocolate la manipulación es CON LAS MANOS
#: (moldes, desmoldado, estuchado) y el producto no lleva después ningún paso
#: que destruya patógenos: la higiene personal no es un trámite, es el único
#: control que hay. Orden interno: persona → extracción → gas → equipos.
HIGIENE = 'Higiene personal y arranque seguro del obrador'
HIGIENE_TAREAS = [
    ('Uniforme y calzado de trabajo limpios, delantal cambiado y pelo '
     'recogido bajo gorro o redecilla', 'Obrador'),
    ('Sin anillos, pulseras, reloj ni pendientes colgantes; uñas cortas, '
     'limpias y sin esmalte ni postizos', 'Obrador'),
    ('Lavado de manos con jabón y secado con papel de un solo uso, y otra vez '
     'en cada cambio de tarea (el chocolate acabado ya no lleva ningún paso '
     'que destruya patógenos)', 'Obrador'),
    ('Heridas y cortes cubiertos con apósito impermeable de color visible y '
     'guante encima', 'Obrador'),
    ('Quien tenga vómitos, diarrea, fiebre o lesiones cutáneas infectadas NO '
     'manipula producto: comunicarlo al encargado y reasignar tarea',
     'Obrador'),
    ('Encender la extracción del obrador ANTES que ningún otro equipo',
     'Obrador'),
    ('Si el obrador tiene instalación de gas (fogón, marmita o quemador): '
     'comprobar que no hay olor, abrir la llave general y sólo después '
     'encender los equipos', 'Obrador'),
]

#: DOM-24 (equivalente) — «Verificar cámara a 15-18 °C» no dice QUÉ se verifica
#: ni qué se hace si la lectura está fuera. Lo que importa por la mañana no es
#: la temperatura de ahora: es si el equipo ha aguantado las 14 horas que el
#: local ha estado cerrado. Un bombón que ha pasado la noche a 24 °C está
#: perdido aunque a las 07:00 la cámara marque 16 °C.
CAMARA = ('Comprobar que la cámara de conservación ha funcionado toda la noche '
          '(sin cortes ni alarmas) y registrar la temperatura: objetivo '
          '15-18 °C y 50-60 % de humedad — anota la lectura: ____ °C')
NEVERA = ('Comprobar que la nevera de rellenos y ganaches ha funcionado toda '
          'la noche y registrar la temperatura: objetivo 0-4 °C — anota la '
          'lectura: ____ °C')
#: Hallazgo «Vitrinas temperadas sin objetivo de temperatura propio» (media).
#: El punto crítico de una vitrina de bombonería no es que encienda: es que
#: MANTENGA por debajo del punto de fusión de la manteca de cacao. Por encima
#: de 20 °C el bombón suda, pierde brillo y sale fat bloom en 48 h.
VITRINA = ('Comprobar que la vitrina de bombonería mantiene 16-18 °C y no '
           'condensa antes de montar el género (por encima de 20 °C la '
           'manteca de cacao funde y el bombón pierde brillo) — anota la '
           'lectura: ____ °C')
#: §2.5 / DOM-23 — la tarea daba por hecho que el cliente tiene el Pack APPCC.
REGISTRO_TEMP = ('Registrar las temperaturas de obrador, cámara y nevera: si '
                 'tienes el Pack APPCC, en su hoja de temperaturas; si no, '
                 'aquí mismo en «Notas»')
#: DOM-19 (equivalente) — el etiquetado del expositor es lo único que ve el
#: cliente alérgico. En chocolatería los alérgenos NO son un caso raro: leche,
#: frutos secos, soja (lecitina) y trazas están en casi toda la vitrina.
ETIQUETADO = ('Verificar el etiquetado de cada producto expuesto: '
              'denominación, precio (y precio por kilo si se vende al peso) y '
              'los alérgenos declarados — leche, frutos secos, soja, gluten, '
              'huevo y sésamo— más las trazas')

CIERRE_CAMARAS = ('Comprobar y registrar las temperaturas antes de cerrar: '
                  'cámara de conservación 15-18 °C y nevera de rellenos '
                  '0-4 °C — anota las lecturas: ____ °C / ____ °C')
#: DOM-18 (equivalente) — el kit registraba mermas en producción (02) y en el
#: perfil del chocolatero (04), pero no al cerrar, que es cuando se sabe lo que
#: se ha roto en tienda y lo que se ha quedado sin vender.
MERMAS_CIERRE = [
    ('Anotar las mermas del día: producto, cantidad y motivo (rotura, mal '
     'templado, bloom, caducidad, degustación o prueba)', 'Admin'),
]
GAS_CIERRE = ('Cerrar la llave general de gas si el obrador la tiene y '
              'verificar que agua y luces quedan apagadas')

#: DOM-09 — 01 es el checklist GENERAL del local y en este kit es molde P4, así
#: que `motor.colapsar_duplicados` (y con él la remisión «→ ver 08/09» de §2.5)
#: no llega: tres tareas suyas repetían, con otras palabras, hitos que ya manda
#: el fichero 09 de caja y el 08 de negocio. Repetir un arqueo no es redundancia
#: inocua: son dos recuentos con dos criterios que pueden no cuadrar, y el
#: encargado acaba dando por hecho el que no hizo. No se borra ninguna fila —el
#: molde P4 numera por bloque y el contador cuenta el rango entero—: se
#: reescriben 1:1 como lo que sí aporta el checklist del local, una COMPROBACIÓN
#: de que el hito está hecho, con la remisión al fichero que manda.
TPV_APERTURA = ('Comprobar que el TPV está activo y que el fondo de caja ya se '
                'ha contado y anotado antes de abrir la puerta: el recuento no '
                'se repite aquí, se hace en «Apertura de Caja» del fichero 09 '
                '(hito en 08/09)')
CUADRE_CIERRE = ('Comprobar que el arqueo del día ha quedado cerrado y firmado '
                 'y las ventas registradas: el cuadre no se repite aquí, se '
                 'hace en «Cierre de Caja» del fichero 09 (hito en 08/09)')
TPV_CIERRE = ('Comprobar que el TPV y el terminal de pago quedan cerrados '
              'DESPUÉS del arqueo, nunca antes: el cierre de terminal se manda '
              'en «Cierre del Negocio» del fichero 08 (hito en 08/09)')


def _f01(wb, cambios):
    tocado = False
    ws = wb['Apertura']
    if _insertar_seccion(ws, 'Encendido y verificación de equipos', HIGIENE,
                         HIGIENE_TAREAS):
        cambios.append(f'«Apertura»: sección nueva «{HIGIENE}» '
                       f'({len(HIGIENE_TAREAS)} tareas) DELANTE del encendido '
                       'de equipos: higiene personal y orden seguro '
                       'extracción → gas → equipos, que no existían en ninguno '
                       'de los 11 ficheros — DOM-12 / DOM-13 (equivalentes)')
        tocado = True
    if _sustituir(ws, 'Verificar cámara de conservación a 15-18 °C (bombones)',
                  CAMARA):
        cambios.append('«Apertura»: la cámara se COMPRUEBA desde la noche '
                       'anterior, con objetivo de temperatura y de humedad y '
                       'hueco para la lectura — DOM-24 (equivalente)')
    if _sustituir(ws, 'Verificar nevera de rellenos y ganaches a 4 °C',
                  NEVERA):
        cambios.append('«Apertura»: la nevera de rellenos igual, y su objetivo '
                       'pasa de «4 °C» a la banda real de refrigeración '
                       '0-4 °C — DOM-24 (equivalente)')
    if _insertar_tras(ws, 'Encender iluminación de vitrina y sala de tienda',
                      [(VITRINA, 'Vitrina')]):
        cambios.append('«Apertura»: control de temperatura de la VITRINA '
                       'temperada (16-18 °C) antes de montar el género — el '
                       'kit sólo mandaba encenderla, y en bombonería el punto '
                       'crítico es que mantenga por debajo del punto de fusión '
                       'de la manteca de cacao (hallazgo «Vitrinas temperadas '
                       'sin objetivo de temperatura propio», media)')
        tocado = True
    if _sustituir(ws, 'Registrar temperaturas en hoja de control APPCC',
                  REGISTRO_TEMP):
        cambios.append('«Apertura»: la referencia al APPCC deja de dar por '
                       'hecho que el cliente lo tiene y ofrece «Notas» como '
                       'alternativa — §2.5 / DOM-23 (equivalente)')
    if _sustituir(ws, 'Verificar etiquetado de alérgenos en cada producto '
                      'expuesto', ETIQUETADO):
        cambios.append('«Apertura»: el etiquetado nombra los alérgenos que de '
                       'verdad hay en una vitrina de bombonería y añade el '
                       'precio por kilo de la venta al peso — DOM-19 '
                       '(equivalente)')
    if _sustituir(ws, 'Activar TPV y verificar fondo de caja', TPV_APERTURA):
        cambios.append('«Apertura»: el TPV y el fondo de caja se COMPRUEBAN '
                       'aquí y se cuentan en «Apertura de Caja» del 09, que es '
                       'donde está el arqueo — antes eran dos recuentos '
                       'paralelos sin remisión — DOM-09')
    _renumerar_p4(ws)
    _dv_extender(ws)
    _freeze(ws)

    ws = wb['Cierre']
    if _sustituir(ws, 'Cuadre de caja y registro de ventas del día',
                  CUADRE_CIERRE):
        cambios.append('«Cierre»: el cuadre de caja deja de duplicar el arqueo '
                       'entero de «Cierre de Caja» (09) y pasa a comprobar que '
                       'está cerrado y firmado, con la remisión — DOM-09')
    if _sustituir(ws, 'Apagar TPV y cerrar terminal de pago', TPV_CIERRE):
        cambios.append('«Cierre»: apagar el TPV era el mismo hito que «Cierre '
                       'del Negocio» (08) B8; aquí queda la comprobación de '
                       'que se hizo DESPUÉS del arqueo, que es el orden que se '
                       'salta todo el mundo — DOM-09')
    if _sustituir(ws, 'Verificar temperaturas de cámaras y registrar',
                  CIERRE_CAMARAS):
        cambios.append('«Cierre»: las dos temperaturas de cierre con su '
                       'objetivo y su hueco de lectura (la de apertura ya lo '
                       'tenía y la de cierre no) — §2.9')
    if _insertar_tras(ws, 'Limpiar superficies de mármol/granito de obrador',
                      MERMAS_CIERRE):
        cambios.append('«Cierre»: mermas del día con producto, cantidad y '
                       'motivo — no se anotaban en ningún cierre — DOM-18 '
                       '(equivalente)')
        tocado = True
    if _sustituir(ws, 'Verificar que gas, agua y luces quedan apagadas',
                  GAS_CIERRE):
        cambios.append('«Cierre»: el gas se CIERRA por la llave general, no se '
                       '«verifica apagado» — cierra el par que abre la '
                       'apertura — DOM-13 (equivalente)')
    _renumerar_p4(ws)
    _dv_extender(ws)
    _freeze(ws)

    if _instrucciones(wb, 'Higiene y temperaturas:', [
            'La primera sección de «Apertura» es de higiene personal y de '
            'arranque seguro: extracción primero, comprobación del gas '
            'después (si lo tienes) y sólo entonces temperadora, vitrinas y '
            'climatización.',
            'Las cámaras no se «encienden»: se comprueba que han funcionado '
            'toda la noche y se anota la lectura. Objetivos de este oficio: '
            'obrador 18-20 °C, conservación 15-18 °C con 50-60 % de humedad, '
            'rellenos y ganaches 0-4 °C, vitrina de bombonería 16-18 °C.',
            'Por encima de 20 °C la manteca de cacao empieza a fundir: el '
            'bombón suda, pierde brillo y en dos días aparece el fat bloom. '
            'Es la razón de que la vitrina lleve su propio control.']):
        cambios.append('Instrucciones: higiene personal, arranque seguro y los '
                       'cuatro objetivos de temperatura del oficio — DOM-12 / '
                       'DOM-13 / DOM-24')
        tocado = True
    return tocado


# ==========================================================================
# 02-partidas-produccion.xlsx — «Templado» y «Moldeado»
# ==========================================================================
#: El control que decide si el día sale bien o se tira: templar con el obrador
#: a 24 °C no cristaliza la manteca en forma β y el bombón sale mate, blando y
#: con bloom en 48 h. No estaba en ninguna de las 11 hojas.
CLIMA_OBRADOR = [
    ('Comprobar la temperatura y la humedad del obrador ANTES de templar: '
     'objetivo 18-20 °C y menos del 60 % de humedad (por encima, la manteca '
     'no cristaliza y aparece bloom) — anota la lectura: ____ °C', 'Obrador'),
]
TEST_NEGRO = ('Test de templado en punta de espátula: debe secar en 3-5 min a '
              '20 °C, con brillo, snap seco y contracción en el molde. Si no, '
              'volver a fundir y templar — no se moldea «a ver si sale»')
#: Hallazgo de la tanda 3 (media) — el criterio de paso/no-paso del test SÓLO
#: estaba en la sección de chocolate negro. Las de leche y blanco —mismo
#: control, mismo riesgo, y encima con menos margen: la manteca lleva grasa
#: láctea y cristaliza más blanda— se quedaron con el «Test de templado y
#: registrar lote» de fábrica, que no dice contra qué se compara ni qué se hace
#: si el lote no pasa. Se les escribe el criterio con el punto de trabajo de SU
#: cobertura, porque es lo que cambia entre las tres curvas de la hoja.
TEST_LECHE = ('Test de templado en capa fina sobre papel: a 18-20 °C debe '
              'cristalizar en 3-5 min, con brillo uniforme y sin vetas, '
              'partiendo del punto de trabajo de 29-30 °C. Si no, volver a '
              'fundir y retemplar — no se moldea «a ver si sale». Registrar el '
              'lote, la hora y la temperatura final')
TEST_BLANCO = ('Test de templado en capa fina sobre papel: a 18-20 °C debe '
               'cristalizar en 3-5 min, con brillo uniforme y sin vetas, '
               'partiendo del punto de trabajo de 28-29 °C. Si no, volver a '
               'fundir y retemplar — no se moldea «a ver si sale». Registrar '
               'el lote, la hora y la temperatura final')
#: El punto de trabajo de la cobertura blanca de la hoja era 27-28 °C y el
#: criterio del test que pide la tanda 3 son 28-29 °C (la curva estándar de
#: cobertura blanca: fundir 40-45, sembrar a 25-26 y subir a 28-29). Dejar los
#: dos números enfrentados DENTRO del mismo bloque de cinco filas sería peor
#: que cualquiera de los dos por separado: el chocolatero leería «recalentar a
#: 27-28» en una fila y «partiendo de 28-29» en la de debajo. Se alinean las
#: dos al valor de oficio.
TRABAJO_BLANCO = 'Recalentar a 28-29 °C — punto de trabajo'
#: DOM-18 (equivalente) — «Registrar mermas y chocolate descartado» no dice qué
#: se hace con ellas, y en chocolatería la diferencia es dinero: el chocolate
#: sin relleno y sin contaminar se refunde; el que lleva ganache, no.
MERMAS_MOLDEADO = ('Anotar las mermas del día: producto, cantidad y motivo '
                   '(rotura, mal templado, bloom, prueba). El chocolate sin '
                   'relleno y sin contaminar se puede refundir; el que lleva '
                   'ganache o fruta, a residuo')
ALMACENAR = ('Almacenar el producto terminado a 15-18 °C y 50-60 % de '
             'humedad, en oscuridad y lejos de olores fuertes (el cacao los '
             'absorbe) — anota la lectura: ____ °C')
LOTE_VIDA = [
    ('Etiquetar cada lote con fecha de producción y consumo preferente según '
     'su familia (tabla al pie de la hoja)', 'Admin'),
]

TITULO_VIDA = ('VIDA ÚTIL Y CONSERVACIÓN ORIENTATIVAS A 15-18 °C Y 50-60 % DE '
               'HUMEDAD — ajústala a tu fórmula y a tu obrador')
VIDA_UTIL = [
    ('Tabletas y chocolate sin relleno', '12-18 meses',
     'El enemigo no es el tiempo: es la humedad, la luz y los olores. Sellado '
     'y en oscuridad'),
    ('Figuras huecas y piezas macizas', '6-12 meses',
     'Igual que la tableta, pero la pieza hueca se raja con los cambios '
     'bruscos de temperatura'),
    ('Bombones de ganache con nata fresca', '10-15 días',
     'Actividad de agua alta: en refrigeración a 0-4 °C y atemperar CERRADOS '
     'antes de abrir, o condensan'),
    ('Bombones de ganache con nata UHT, sorbato o alcohol', '4-8 semanas',
     'El conservante y el alcohol bajan la actividad de agua; sin ellos no se '
     'llega ni a la mitad'),
    ('Bombones de praliné, gianduja y frutos secos', '2-4 meses',
     'La grasa del fruto seco se enrancia y el frío no lo evita: manda la '
     'fecha, no el aspecto'),
    ('Trufas y rocas recubiertas', '3-4 semanas',
     'Si llevan nata o mantequilla, se cuentan como ganache fresca'),
    ('Bombones de licor y cristalizados', '3-6 meses',
     'Vigilar la cristalización del azúcar en la cáscara: revienta y gotea'),
    ('Frutos secos garrapiñados y frutas confitadas bañadas', '1-3 meses',
     'Se apelmazan con la humedad; envasado hermético con desecante si tu '
     'obrador es húmedo'),
    ('Barquillos y crujientes bañados', '3-4 semanas',
     'Pierden el crujiente mucho antes que la seguridad: se retiran por '
     'calidad'),
    ('Chocolate acabado: NO congelar', 'Nunca',
     'Al descongelar condensa, el agua disuelve el azúcar de la superficie y '
     'deja sugar bloom. Sólo el granel de ganache admite ≤ −18 °C 1-2 meses, '
     'descongelado 24 h en cámara y sin abrir'),
]


def _tabla_vida(ws, cambios):
    """Tabla editable de vida útil al pie de «Moldeado».

    Va DEBAJO de la fila de firma, es decir, por debajo del contador y fuera
    del rango que éste cuenta: es una referencia, no una tarea que marcar.
    """
    if _fila(ws, TITULO_VIDA, 1) is not None:
        return False
    g = motor.geometria_p4(ws)
    if not g:
        raise AnclaPerdida('«Moldeado»: no es una hoja del molde P4')
    firma = None
    for r in range(g['contador'] or 1, ws.max_row + 1):
        v = ws.cell(row=r, column=1).value
        if isinstance(v, str) and v.startswith('Firma responsable'):
            firma = r
            break
    if firma is None:
        raise AnclaPerdida('«Moldeado»: no encuentro la fila de firma')
    banda = _exige(ws, 'Moldeado de bombones', 1)
    est_titulo = _estilos(ws, banda)
    est_cab = _estilos(ws, g['hr'])
    est_dato = _estilos(ws, g['hr'] + 1)
    motor.insertar_filas(ws, firma + 1, 3 + len(VIDA_UTIL))
    fila = firma + 2
    _pintar(ws, fila, est_titulo)
    ws.cell(row=fila, column=1).value = TITULO_VIDA
    motor._merge(ws, f'A{fila}:{L(NCOL)}{fila}')
    fila += 1
    _pintar(ws, fila, est_cab)
    ws.cell(row=fila, column=2).value = 'Familia'
    ws.cell(row=fila, column=3).value = 'Vida útil'
    ws.cell(row=fila, column=4).value = 'Notas'
    motor._merge(ws, f'D{fila}:{L(NCOL)}{fila}')
    for i, (familia, vida, nota) in enumerate(VIDA_UTIL, start=1):
        r = fila + i
        _pintar(ws, r, est_dato)
        ws.cell(row=r, column=1).value = None
        ws.cell(row=r, column=2).value = familia
        ws.cell(row=r, column=3).value = vida
        ws.cell(row=r, column=4).value = nota
        for c in (2, 3, 4):
            motor._verde(ws.cell(row=r, column=c))
        motor._merge(ws, f'D{r}:{L(NCOL)}{r}')
    cambios.append('«Moldeado»: tabla editable de vida útil y conservación '
                   f'({len(VIDA_UTIL)} familias) al pie, fuera del rango del '
                   'contador — DOM-29 (equivalente, portado de CONGELACIÓN a '
                   'CONSERVACIÓN: congelar chocolate acabado provoca sugar '
                   'bloom y la tabla lo dice)')
    return True


def _f02(wb, cambios):
    tocado = False
    ws = wb['Templado']
    if _insertar_tras(ws, 'Verificar stock de cobertura blanca (28-33% cacao)',
                      CLIMA_OBRADOR):
        cambios.append('«Templado»: temperatura y humedad del OBRADOR antes de '
                       'templar — la hoja controlaba las tres curvas de '
                       'cobertura al grado y no el aire de la sala, que es lo '
                       'que decide si cristaliza — §2.9 (equivalente)')
        tocado = True
    if _sustituir(ws, 'Test de templado: brillo, snap, contracción en molde',
                  TEST_NEGRO):
        cambios.append('«Templado»: el test de templado pasa de enumerar tres '
                       'palabras a decir el criterio (3-5 min a 20 °C) y qué '
                       'hacer si no lo pasa')
    if _sustituir_en_seccion(ws, 'Proceso de templado — Chocolate con leche',
                             'Test de templado y registrar lote', TEST_LECHE):
        cambios.append('«Templado»: el test de la cobertura CON LECHE deja de '
                       'ser «test de templado y registrar lote» y trae el '
                       'criterio de paso/no-paso (capa fina sobre papel, '
                       'cristaliza en 3-5 min a 18-20 °C con brillo uniforme y '
                       'sin vetas) desde su punto de trabajo (29-30 °C), más '
                       'qué hacer si no lo pasa — el criterio sólo estaba en '
                       'la sección de chocolate negro (hallazgo media de la '
                       'tanda 3)')
    if _sustituir_en_seccion(ws, 'Proceso de templado — Chocolate blanco',
                             'Recalentar a 27-28°C — punto de trabajo',
                             TRABAJO_BLANCO):
        cambios.append('«Templado»: el punto de trabajo de la cobertura BLANCA '
                       'pasa de 27-28 °C a los 28-29 °C de la curva estándar, '
                       'que es contra los que se lee su test de templado — sin '
                       'esto, las dos filas contiguas del mismo bloque darían '
                       'dos temperaturas distintas')
    if _sustituir_en_seccion(ws, 'Proceso de templado — Chocolate blanco',
                             'Test de templado y registrar lote', TEST_BLANCO):
        cambios.append('«Templado»: el test de la cobertura BLANCA, igual: '
                       'criterio de paso/no-paso desde su punto de trabajo '
                       '(28-29 °C) y qué hacer si no cristaliza — la blanca es '
                       'la que menos margen tiene, porque la grasa láctea la '
                       'deja más blanda (hallazgo media de la tanda 3)')
    _renumerar_p4(ws)
    _dv_extender(ws)

    ws = wb['Moldeado']
    if _sustituir(ws, 'Registrar mermas y chocolate descartado',
                  MERMAS_MOLDEADO):
        cambios.append('«Moldeado»: las mermas llevan motivo y el criterio de '
                       'qué se refunde y qué va a residuo — DOM-18 '
                       '(equivalente)')
    if _sustituir(ws, 'Almacenar producto terminado a 15-18 °C', ALMACENAR):
        cambios.append('«Moldeado»: el almacenamiento lleva humedad, oscuridad '
                       'y la advertencia de los olores, y remite a la tabla de '
                       'vida útil — DOM-29 (equivalente)')
    if _insertar_tras(ws, 'Registrar lotes de producción: producto, cantidad, '
                          'fecha', LOTE_VIDA):
        cambios.append('«Moldeado»: etiquetado de lote con consumo preferente '
                       'por familia — DOM-29 (equivalente)')
        tocado = True
    if _tabla_vida(ws, cambios):
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)

    if _instrucciones(wb, 'Templado y conservación:', [
            'Antes de templar se comprueba el AIRE del obrador: 18-20 °C y '
            'menos del 60 % de humedad. Las tres curvas de cobertura de esta '
            'hoja sólo funcionan dentro de esa ventana.',
            'Al pie de «Moldeado» tienes una tabla editable de vida útil por '
            'familia: ajústala a tu fórmula. Está fuera del contador porque '
            'es una referencia, no una tarea.',
            'El chocolate acabado NO se congela: al descongelar condensa, el '
            'agua disuelve el azúcar de la superficie y deja sugar bloom. '
            'Sólo el granel de ganache admite congelación.']):
        cambios.append('Instrucciones: ventana de templado, tabla de vida útil '
                       'y por qué no se congela el chocolate acabado — DOM-29 '
                       '(equivalente)')
        tocado = True
    return tocado


# ==========================================================================
# 03-tareas-manager.xlsx — «Diario», «Semanal» y «Mensual»
# ==========================================================================
#: DOM-17 (equivalente) — el registro horario es obligatorio en España desde el
#: RD-ley 8/2019 y hay que conservarlo 4 años. En una chocolatería el obrador
#: entra de madrugada en campaña y la tienda cierra a las 20:30: son dos
#: jornadas distintas en el mismo libro y ninguna se cerraba en ninguna parte.
JORNADA_DIA = [
    ('Cerrar y validar el registro diario de jornada de todo el equipo, '
     'obrador y tienda: es obligatorio (RD-ley 8/2019) y hay que conservarlo '
     '4 años', 'Admin'),
]
JORNADA_MES = [
    ('Archivar los registros de jornada del mes firmados y guardarlos a '
     'disposición de la Inspección de Trabajo (4 años)', 'Admin'),
]
#: DOM-28 (equivalente) — el semanal iba de lunes a viernes y se acababa en el
#: food cost. En una chocolatería con tienda el 40 % de la venta cae en sábado
#: y domingo, que era justo lo que no tenía ni una línea.
FINDE = 'Sábado y domingo — Tienda a pleno'
FINDE_TAREAS = [
    ('Reponer la vitrina antes de cada pico: media mañana y media tarde, sin '
     'esperar a que se vacíe', 'Vitrina'),
    ('Revisar el stock de packaging de regalo: cajas, lazos y bolsas se '
     'agotan el sábado y no hay proveedor hasta el lunes', 'Packaging'),
    ('Anotar las roturas de stock y qué se dejó de vender, para la '
     'planificación del lunes', 'Gestión'),
]


def _f03(wb, cambios):
    tocado = False
    ws = wb['Diario']
    if _insertar_tras(ws, 'Anotar incidencias y notas para el día siguiente',
                      JORNADA_DIA):
        cambios.append('«Diario»: cierre y validación del registro diario de '
                       'jornada del equipo (RD-ley 8/2019, conservación 4 '
                       'años) — DOM-17 (equivalente)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)

    ws = wb['Semanal']
    # Al FINAL, no delante del viernes: la hoja va por días y meterlo en medio
    # dejaba «lunes, martes, miércoles, jueves, sábado y domingo, viernes».
    if _seccion_final(ws, FINDE, FINDE_TAREAS):
        cambios.append(f'«Semanal»: sección nueva «{FINDE}» '
                       f'({len(FINDE_TAREAS)} tareas) — el semanal terminaba '
                       'el viernes en una tienda que factura sábado y domingo '
                       '— DOM-28 (equivalente)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)
    _freeze(ws)

    ws = wb['Mensual']
    if _insertar_tras(ws, 'Revisar y actualizar procedimientos operativos',
                      JORNADA_MES):
        cambios.append('«Mensual»: archivo mensual de los registros de jornada '
                       '— DOM-17 (equivalente)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)

    if _instrucciones(wb, 'Obligaciones del encargado:', [
            'El registro de jornada se cierra y se valida CADA DÍA (obrador y '
            'tienda) y se archiva cada mes: es obligatorio desde el RD-ley '
            '8/2019 y hay que conservarlo 4 años.',
            'El bloque de fin de semana del «Semanal» existe porque en una '
            'chocolatería con tienda el sábado y el domingo son el pico de '
            'venta, y la planificación del lunes se hace con lo que allí se '
            'anota.']):
        cambios.append('Instrucciones: registro de jornada y bloque de fin de '
                       'semana — DOM-17 / DOM-28 (equivalentes)')
        tocado = True
    return tocado


# ==========================================================================
# 04-tareas-perfiles.xlsx — «Chocolatero», «Dependiente», «Encargado»
# ==========================================================================
#: DOM-19 (equivalente) — «Gestionar encargos especiales» dejaba al criterio del
#: dependiente lo que hay que apuntar. Lo que genera la reclamación es siempre
#: lo mismo: nadie preguntó por los alérgenos y nadie fijó la hora de recogida.
ENCARGOS = ('Gestionar encargos y pedidos por adelantado: al CONFIRMAR el '
            'encargo, dejar por escrito alérgenos e intolerancias, unidades, '
            'fecha y hora de recogida, precio, señal cobrada y condiciones de '
            'cancelación')
ETIQUETADO_TIENDA = ('Verificar el etiquetado de cada referencia: precio, '
                     'precio por kilo si se vende al peso, y los alérgenos '
                     'declarados (leche, frutos secos, soja, gluten, huevo y '
                     'sésamo) más las trazas')
TEMP_TIENDA = ('Vigilar la temperatura de la tienda (20-22 °C) y la de la '
               'vitrina (16-18 °C): por encima el bombón suda y pierde brillo '
               '— anota la lectura: ____ °C')


def _f04(wb, cambios):
    ws = wb['Dependiente']
    if _sustituir(ws, 'Verificar etiquetado de precios y alérgenos',
                  ETIQUETADO_TIENDA):
        cambios.append('«Dependiente»: el etiquetado nombra los alérgenos '
                       'reales de una vitrina de bombonería y el precio por '
                       'kilo de la venta al peso — DOM-19 (equivalente)')
    if _sustituir(ws, 'Gestionar encargos especiales y pedidos por adelantado',
                  ENCARGOS):
        cambios.append('«Dependiente»: al confirmar el encargo se dejan por '
                       'escrito alérgenos, hora de recogida, señal y '
                       'cancelación — DOM-19 (equivalente)')
    if _sustituir(ws, 'Vigilar temperatura de tienda (20-22 °C ideal)',
                  TEMP_TIENDA):
        cambios.append('«Dependiente»: la vigilancia de temperatura incluye la '
                       'VITRINA, que es la que estropea el género, y trae '
                       'hueco para la lectura — §2.9 (equivalente)')
    _renumerar_p4(ws)
    _dv_extender(ws)
    return False


# ==========================================================================
# 05-tareas-semanales-mensuales.xlsx — «Semanal», «Mensual» y hoja nueva
# ==========================================================================
TEMP_SEMANAL = ('Verificar y registrar las temperaturas de los equipos de '
                'frío: cámara de conservación 15-18 °C y nevera de rellenos '
                '0-4 °C — anota las lecturas: ____ °C / ____ °C')

HOJA_LEGAL = 'Trimestral y Anual'
TITULO_LEGAL = 'Mantenimiento Trimestral y Anual — Revisiones Contratadas'
#: DOM-16 (equivalente) — el kit tenía capa diaria, semanal y mensual, y nada
#: por encima. Todo lo que una inspección pide POR ESCRITO —DDD, conductos,
#: extintores, calibración de sondas y báscula, RGSEAA, carnés de manipulador,
#: póliza y facturación— no aparecía en ninguno de los 11 ficheros. Se crea
#: clonando «Mensual», que tiene exactamente 3 bloques de 5 / 5 / 4 filas.
LEGAL = [
    ('Higiene, plagas y analíticas — empresa autorizada', [
        ('Control de plagas (DDD) por empresa autorizada: visita, parte '
         'firmado y certificado en vigor', 'Admin', 'Trimestral'),
        ('Limpieza de los conductos de extracción del obrador por empresa '
         'homologada, con certificado', 'General', 'Anual'),
        ('Analítica de superficies, de producto y del agua de la red interior '
         'en laboratorio externo (legionela sólo si tienes torre de '
         'refrigeración o acumulador de agua caliente)', 'Admin', 'Semestral'),
        ('Renovar los carnés de manipulador de alimentos del equipo y '
         'archivar los certificados', 'Equipo', 'Anual'),
        # Sin la sigla a propósito: `motor.texto_appcc` le colgaría «si tienes
        # el Pack APPCC, regístralo allí», que en la tarea que MANDA REVISAR el
        # plan es circular.
        ('Revisar el plan de autocontrol de higiene y las fichas técnicas de '
         'producto: altas, bajas y cambios de proveedor del año', 'Admin',
         'Anual'),
    ]),
    ('Equipos, instalaciones y seguridad', [
        ('Revisión de la temperadora y del bombo por el SAT: sondas, '
         'resistencias, juntas y desgaste del tornillo', 'Templado', 'Anual'),
        ('Revisión de cámaras y neveras por frigorista: gas, estanqueidad, '
         'juntas y ciclo de desescarche', 'Conservación', 'Semestral'),
        ('Calibrar termómetros, sondas y báscula de precisión contra un '
         'patrón conocido y anotar la desviación', 'Obrador', 'Trimestral'),
        ('Revisión de extintores y BIE por empresa mantenedora (etiqueta y '
         'acta)', 'General', 'Anual'),
        ('Revisión de la instalación de gas por empresa habilitada, si el '
         'obrador la tiene', 'General', 'Cada 5 años'),
    ]),
    ('Documentación, seguros y facturación', [
        ('Revisar la póliza de responsabilidad civil y de continuidad de '
         'negocio: sumas aseguradas y actividades excluidas', 'Admin',
         'Anual'),
        ('Comprobar que el registro sanitario (RGSEAA) recoge la actividad y '
         'las instalaciones reales, obrador incluido', 'Admin', 'Anual'),
        ('Revisión del TPV y del software de facturación (requisitos '
         'antifraude / Verifactu)', 'Admin', 'Anual'),
        ('Archivar los registros de jornada del trimestre y anotar en '
         '«Notas» el nº de parte de cada revisión y la fecha de la '
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
    """Crea «Trimestral y Anual» clonando «Mensual» y ajustando sus bloques.

    Se clona en lugar de construirse a mano porque el clon trae anchos,
    alturas, bordes, combinaciones y la geometría exacta del molde P4; lo que
    NO trae (medido con openpyxl) son el desplegable y el pie de impresión, y
    por eso se le aplican aquí uno a uno.
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
    if len(bloques) != len(LEGAL):
        raise AnclaPerdida(f'«Mensual» tiene {len(bloques)} bloques y '
                           f'«{HOJA_LEGAL}» espera {len(LEGAL)}')
    # De ABAJO hacia ARRIBA: recortar un bloque mueve los de debajo, no los de
    # encima, así que las filas ya medidas siguen siendo válidas.
    for (banda, cab, filas), (_titulo, tareas) in reversed(
            list(zip(bloques, LEGAL))):
        sobra = len(filas) - len(tareas)
        if sobra < 0:
            raise AnclaPerdida(f'«{HOJA_LEGAL}»: el bloque de {len(filas)} '
                               f'filas no cabe {len(tareas)} tareas')
        if sobra:
            motor.eliminar_filas(ws, filas[len(tareas)], sobra)
    g = motor.geometria_p4(ws)
    bloques = _bloques_p4(ws, g)
    for (banda, cab, filas), (titulo, tareas) in zip(bloques, LEGAL):
        ws.cell(row=banda, column=1).value = titulo
        if cab:
            ws.cell(row=cab, column=6).value = 'Cadencia'
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
        raise AnclaPerdida(f'«{HOJA_LEGAL}»: el desplegable quedó vacío')
    # A4 + pie + fila de cabecera repetida al imprimir: `motor.cerrar` no corre
    # sobre el molde P4, así que sin esto la hoja nueva saldría del censo como
    # «noprint» (paperSize/fitToPage/pie son tres de sus comprobaciones).
    motor.print_setup(ws, g['hr'], landscape=True)
    cambios.append(f'hoja nueva «{HOJA_LEGAL}» en 05: mantenimiento y '
                   'documentación que se CONTRATA y que pide una inspección '
                   '(DDD, conductos, analíticas, carnés, SAT de temperadora y '
                   'cámaras, calibración de sondas y báscula, extintores, gas, '
                   'RGSEAA, póliza y Verifactu) — DOM-16 (equivalente); el kit '
                   'no tenía ninguna capa por encima del mes')
    return True


def _f05(wb, cambios):
    tocado = False
    ws = wb['Semanal']
    if _sustituir(ws, 'Verificar temperaturas de cámaras frigoríficas',
                  TEMP_SEMANAL):
        cambios.append('«Semanal»: la verificación semanal de frío nombra los '
                       'dos equipos con su objetivo y trae hueco para las '
                       'lecturas — §2.9 (equivalente)')
    _renumerar_p4(ws)
    _dv_extender(ws)
    if _hoja_legal(wb, cambios):
        tocado = True
    if _instrucciones(wb, 'Más allá del mes:', [
            'La hoja «Trimestral y Anual» recoge lo que se CONTRATA y se pide '
            'por escrito en una inspección: DDD, conductos de extracción, '
            'analíticas, carnés de manipulador, SAT de temperadora y cámaras, '
            'calibración de sondas y báscula, extintores, instalación de gas, '
            'RGSEAA, póliza y facturación.',
            'Anota en «Notas» el número de parte de cada revisión y la fecha '
            'de la siguiente; la columna «Cadencia» ya viene con la '
            'periodicidad legal o recomendada de cada una.']):
        cambios.append('Instrucciones: hoja «Trimestral y Anual» — DOM-16 '
                       '(equivalente)')
        tocado = True
    return tocado


# ==========================================================================
# 06-eventos-temporada.xlsx — «Navidad», «San Valentín», «Pascua»
# ==========================================================================
#: DOM-19 (equivalente) — el pedido corporativo de Navidad es el que más dinero
#: mueve y el que peor se documenta: se cierra por teléfono en octubre y se
#: entrega en diciembre, con seis semanas para que nadie recuerde qué se dijo.
CORPORATIVOS = ('Gestionar los pedidos corporativos: al CONFIRMAR cada pedido, '
                'dejar por escrito alérgenos e intolerancias, unidades, fecha '
                'y lugar de entrega, precio unitario, señal y condiciones de '
                'cancelación')
FECHA_LIMITE = [
    ('Fijar y publicar la FECHA LÍMITE de encargos de Navidad y los horarios '
     'de recogida del 24 y el 31 (en tienda, en la web y en RRSS)', 'Admin'),
]
DOMICILIO = ('Gestionar los pedidos especiales y las entregas a domicilio: '
             'confirmar por escrito alérgenos, dirección, franja de entrega y '
             'quién recibe; en reparto propio, el producto viaja por debajo '
             'de 18 °C y nunca en el maletero al sol')
ENVASAR_PASCUA = ('Envasar y etiquetar la colección de Pascua: denominación, '
                  'peso neto, lote, consumo preferente y alérgenos declarados '
                  '(leche, frutos secos, soja, gluten y huevo)')


def _f06(wb, cambios):
    tocado = False
    ws = wb['Navidad']
    if _sustituir(ws, 'Gestionar pedidos corporativos: presupuestos y '
                      'entregas', CORPORATIVOS):
        cambios.append('«Navidad»: al confirmar el pedido corporativo se dejan '
                       'por escrito alérgenos, entrega, señal y cancelación — '
                       'DOM-19 (equivalente)')
    if _insertar_tras(ws, 'Lanzar preventa en web y RRSS', FECHA_LIMITE):
        cambios.append('«Navidad»: fecha límite de encargos y horarios del 24 '
                       'y el 31 publicados en octubre — el kit planificaba la '
                       'producción y no el corte de pedidos, que es lo que '
                       'revienta la última semana — TEC-22 (equivalente)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)

    ws = wb['San Valentín']
    if _sustituir(ws, 'Gestionar pedidos especiales y entregas a domicilio',
                  DOMICILIO):
        cambios.append('«San Valentín»: la entrega a domicilio confirma '
                       'alérgenos y franja, y fija el límite térmico del '
                       'reparto (18 °C) — DOM-19 (equivalente)')
    _renumerar_p4(ws)
    _dv_extender(ws)

    ws = wb['Pascua']
    if _sustituir(ws, 'Envasar y etiquetar colección de Pascua',
                  ENVASAR_PASCUA):
        cambios.append('«Pascua»: el etiquetado enumera lo que exige el '
                       'Rgto. 1169/2011 (denominación, peso neto, lote, '
                       'consumo preferente y alérgenos) — DOM-19 (equivalente)')
    _renumerar_p4(ws)
    _dv_extender(ws)

    if _instrucciones(wb, 'Antes de cerrar una campaña:', [
            'Todo encargo —de particular o de empresa— se confirma POR '
            'ESCRITO con alérgenos e intolerancias, unidades, fecha y hora de '
            'entrega, precio, señal y condiciones de cancelación.',
            'Publica la fecha límite de encargos de cada campaña antes de '
            'abrir la preventa: lo que revienta la última semana no es la '
            'producción, es el pedido que entra el día 22.']):
        cambios.append('Instrucciones: confirmación por escrito de los '
                       'encargos y fecha límite de campaña — DOM-19 / TEC-22 '
                       '(equivalentes)')
        tocado = True
    return tocado


# ==========================================================================
# BONUS-01-briefing-servicio.xlsx — «Briefing»
# ==========================================================================
CLIMA_BRIEFING = [
    ('Temperatura y humedad del obrador al arrancar: ____ °C / ____ % '
     '(objetivo 18-20 °C y menos del 60 %)', 'Producción'),
]


def _bonus01(wb, cambios):
    ws = wb['Briefing']
    if _insertar_tras(ws, 'Coberturas necesarias: negra ___ kg / leche ___ kg '
                          '/ blanca ___ kg', CLIMA_BRIEFING):
        cambios.append('«Briefing»: la reunión de 5 minutos empieza por el '
                       'dato que condiciona toda la producción del día —el '
                       'aire del obrador— y que no se pedía en ninguna parte '
                       '— §2.9 (equivalente)')
        _renumerar_p4(ws)
        _dv_extender(ws)
        return True
    return False


# ==========================================================================
# BONUS-02-calendario-anual-tareas.xlsx — «Calendario»
# ==========================================================================
#: DOM-20 (equivalente) — faltaban Reyes, las comuniones (abr-jun), el 15 de
#: agosto, el 1 de noviembre y el puente del 6-8 de diciembre, que en una
#: chocolatería española son días de tienda llena. Y las «15 fechas clave» que
#: prometían las Instrucciones no estaban por ninguna parte: la hoja tiene 12
#: filas, una por mes.
FECHAS = [
    ('Enero',
     'Rebajas post-Navidad, lanzar colección invierno, planificar San '
     'Valentín',
     'Reyes (6): liquidar turrón y figuras de Navidad · rebajas post-Navidad '
     '· lanzar la colección de invierno · planificar San Valentín'),
    ('Febrero',
     'San Valentín (14), producción corazones y edición limitada, entregas '
     'express',
     'San Valentín (14): corazones y edición limitada · fecha límite de '
     'encargos el día 10 · entregas exprés los días 13 y 14'),
    ('Marzo',
     'Día del Padre (19 España), preparación Pascua, talleres infantiles',
     'Día del Padre (19) · preparación de Pascua (fecha móvil) · talleres '
     'infantiles de Semana Santa'),
    ('Abril',
     'Semana Santa / Pascua, monas y huevos, colección primavera',
     'Semana Santa y Pascua: monas y huevos · arrancan las COMUNIONES '
     '(abril-junio): detalles de mesa, figuras y cajas personalizadas'),
    ('Mayo',
     'Día de la Madre (1er domingo), edición regalo premium',
     'Día de la Madre (1.er domingo) · pico de COMUNIONES · edición regalo '
     'premium'),
    ('Junio',
     'Inicio verano, adaptar catálogo (menos bombones, más tabletas)',
     'Últimas comuniones · inicio del verano: adaptar catálogo (menos ganache '
     'fresca, más tableta y producto estable)'),
    ('Julio',
     'Temporada turística, packs regalo turista, colaboraciones locales',
     'Temporada turística: packs souvenir y colaboraciones locales · vigilar '
     'a diario la temperatura de tienda y vitrina'),
    ('Agosto',
     'Mantenimiento profundo obrador, vacaciones escalonadas, stock Navidad',
     'Asunción (15): festivo nacional, la tienda abre para el turista aunque '
     'el obrador pare · mantenimiento profundo · vacaciones escalonadas · '
     'cerrar el pedido de coberturas de Navidad'),
    ('Septiembre',
     'Vuelta a la rutina, lanzar colección otoño, ferias gastronómicas',
     'Vuelta a la rutina · colección de otoño · ferias gastronómicas · abrir '
     'la agenda de pedidos corporativos de Navidad'),
    ('Octubre',
     'Halloween (31), producción figuras terror, preparación Navidad intensa',
     'Halloween (31): figuras y bombones de temporada · producción navideña a '
     'pleno · publicar el catálogo de Navidad'),
    ('Noviembre',
     'Black Friday, preventa Navidad, producción de turrones y cestas',
     'Todos los Santos (1): panellets y huesos de santo bañados · Black '
     'Friday (último viernes) · preventa de Navidad · turrones y cestas'),
    ('Diciembre',
     'NAVIDAD — máxima producción: turrones, figuras, cestas, regalos '
     'corporativos',
     'NAVIDAD, máxima producción · puente de la Constitución y la Inmaculada '
     '(6-8): fin de semana largo de máxima venta en tienda · fecha límite de '
     'encargos y horarios especiales del 24 y el 31'),
]
PRODUCTOS_NOV = ('Panellets y huesos de santo bañados, turrones, cestas '
                 'corporativas, figuras navideñas')


def _bonus02(wb, cambios):
    ws = wb['Calendario']
    n = 0
    for mes, viejo, nuevo in FECHAS:
        r = _fila(ws, mes, 1)
        if r is None:
            raise AnclaPerdida(f'«Calendario»: no encuentro el mes «{mes}»')
        actual = ws.cell(row=r, column=2).value
        if _norm(actual) == _norm(nuevo):
            continue
        if _norm(actual) != _norm(viejo):
            raise AnclaPerdida(f'«Calendario»: {mes} no dice lo que este '
                               f'módulo esperaba ({actual!r})')
        ws.cell(row=r, column=2).value = nuevo
        n += 1
    r = _fila(ws, 'Noviembre', 1)
    if r and ws.cell(row=r, column=3).value != PRODUCTOS_NOV:
        ws.cell(row=r, column=3).value = PRODUCTOS_NOV
        n += 1
    if n:
        cambios.append('«Calendario»: Reyes, comuniones de abril a junio, '
                       'Asunción del 15 de agosto, Todos los Santos y el '
                       'puente del 6-8 de diciembre — cinco fechas de tienda '
                       'llena que no estaban — DOM-20 (equivalente)')
    ws = wb['Instrucciones']
    viejo = '▸ 15 fechas clave para chocolaterías con preparación especial.'
    nuevo = ('▸ Un mes por fila con las 12 campañas y fechas señaladas del año '
             'chocolatero español.')
    for f in range(1, ws.max_row + 1):
        if ws.cell(row=f, column=2).value == viejo:
            ws.cell(row=f, column=2).value = nuevo
            cambios.append('Instrucciones: la portada prometía «15 fechas '
                           'clave» y la hoja tiene 12 filas, una por mes; '
                           'ahora dice lo que hay (12 campañas contadas una a '
                           'una) — COM-24 (equivalente)')
            break
    return False


# ==========================================================================
# 08-apertura-cierre-negocio.xlsx — molde ▸, el motor vuelve a pasar detrás
# ==========================================================================
#: Hallazgo «Vitrinas temperadas sin objetivo» (media) — «Encender vitrinas
#: temperadas» es una tarea de interruptor. Lo que hay que comprobar antes de
#: montar el género es que la vitrina HA ALCANZADO su rango.
#:
#: Desde la tanda 5 la tarea se parte en dos porque las dos mitades caen en
#: momentos distintos de la mañana y el molde ya trae DOS filas para ellas: se
#: ENCIENDE al entrar (B11, hora precargada temprana) y se COMPRUEBA justo
#: antes de montar el género (B20, hora precargada tarde). Tal y como estaba,
#: la única fila que hablaba de vitrinas era la 20 y mandaba encenderlas y
#: comprobar su rango en el mismo gesto: o se enciende tarde o se comprueba un
#: equipo que lleva dos minutos en marcha. La humedad entra aquí y no en la de
#: encendido porque es lo que se mide sobre la vitrina YA en régimen.
VITRINA_08 = ('Comprobar que las vitrinas temperadas han alcanzado 16-18 °C y '
              'menos del 55 % de humedad antes de montar el género — anota la '
              'lectura: ____ °C')
#: Hallazgo «Temperatura de cierre del obrador sin objetivo ni hueco de
#: lectura» (media) — la tarea de apertura sí llevaba el rango (18-20 °C) y la
#: de cierre no llevaba nada: se pedía un registro sin decir contra qué se
#: compara ni dónde se anota.
OBRADOR_CIERRE = ('Registrar la temperatura de cierre del obrador: objetivo '
                  '18-20 °C — anota la lectura: ____ °C')
OBRADOR_APERTURA = ('Verificar la temperatura y la humedad del obrador: '
                    'objetivo 18-20 °C y 50-60 % — anota la lectura: ____ °C')
VITRINA_CIERRE = ('Apagar las vitrinas temperadas una vez retirado el género a '
                  'la cámara de conservación')

# --------------------------------------------------------------------------
# Vocabulario de restaurante con sala en el 08 (hallazgo BAJA de
# kit-tareas-chocolateria-ver3.json, y el mismo patrón que critico-2.json tiene
# abierto para toda la familia)
# --------------------------------------------------------------------------
# El 08 es el ÚNICO fichero del kit escrito con el molde genérico de los 12
# hermanos, y por eso conservaba el vocabulario de un restaurante con comedor
# abierto: «pizarra de menú» (B9), «sistema de reservas» (B11), «reservas del
# día» (B13), «mobiliario (sillas, mesas…)» (B16) y «cartas/menús» (B18). Una
# bombonería de mostrador no tiene carta que repasar ni reservas que confirmar:
# lo que tiene es una VITRINA que hay que enfriar, montar, etiquetar y reponer,
# unas CAJAS de regalo con las que se estucha y unos ENCARGOS que alguien viene
# a recoger a una hora.
#
# Todo son sustituciones 1:1: mismo número de filas, ni una fila nueva. Las
# columnas D («Responsable») y E («Hora Límite») NO se tocan — las escribe
# `motor.precargar_negocio` POR POSICIÓN (`filas[i]`, no por texto), así que
# reescribir el texto de una tarea no puede mover ni su responsable ni su hora
# y el gate `negocio_precargado` sigue verde.
#
# Redacción atada a la idempotencia de la 2.ª pasada del motor: ningún texto de
# aquí lleva «=» (`texto_facturado`), ni «APPCC» (`texto_appcc`), ni la palabra
# «temperatura» sin el hueco «____ °C» ya escrito (`texto_temperatura` pica con
# temperatura + verbo de registro + equipo de frío, y «vitrina» ES equipo de
# frío). Los rangos van «16-18 °C», que es la forma que ya deja `texto_grados`.
#
# Y ninguno vuelve a decir «Encender … TPV»: ese hito es de B10 y una segunda
# aparición dispararía el gate `tpv_duplicado` de §6.

#: B9 — la señalización exterior se queda (su pareja de cierre, B12 «Recoger
#: señalización exterior», es la misma tarea al revés), pero lo que se cuelga
#: fuera de una bombonería no es una pizarra de menú: es el horario, el cartel
#: de encargos y un escaparate que, si le da el sol, funde el género que hay
#: dentro. El escaparate al sol es el defecto de tienda más caro del oficio y
#: no lo vigilaba ninguna de las 11 hojas.
SENALIZACION = ('Montar la señalización exterior y el cartel de encargos por '
                'adelantado, y comprobar que al escaparate no le da el sol '
                'directo: el chocolate expuesto se funde y pierde el brillo')
#: B11 — no hay «sistema de reservas» que encender. Lo que hay que encender al
#: entrar es la vitrina, que es lo que más tarda: aquí queda el ENCENDIDO y en
#: B20 la comprobación del rango, que es donde el molde la había puesto (fila
#: 20, con hora precargada más tardía).
VITRINA_ENCENDER = ('Encender las vitrinas temperadas de bombones y tabletas '
                    'nada más entrar: tardan en bajar y el género no se monta '
                    'hasta que estén en rango')
#: B13 — una bombonería no toma reservas, toma ENCARGOS, y lo que descoloca la
#: mañana es que a las 11:00 llegue alguien a recoger una caja que nadie ha
#: estuchado. Se queda en el nivel de MARCO (qué hay comprometido para hoy y
#: quién lo prepara); el detalle de la agenda y de los pedidos online sigue en
#: 01-apertura-cierre.xlsx y la señal cobrada, en 09.
ENCARGOS_08 = ('Revisar los encargos comprometidos para hoy: unidades, '
               'hora de recogida y quién los prepara, y dejar preparadas '
               'las cajas de regalo y las cintas de los que se recojan por '
               'la mañana')
#: B16 — el mobiliario de una bombonería de mostrador no son sillas y mesas.
#: Se queda en ESTADO (desperfectos, bombillas, cristales rayados) y no en
#: limpieza, que ya es tarea propia de 01 («Verificar limpieza de cristales de
#: vitrina»).
MOBILIARIO = ('Revisar el estado del mobiliario de tienda: mostrador, '
              'estanterías y escaparate sin desperfectos, sin bombillas '
              'fundidas y sin cristales rayados')
#: B18 — la «carta» de una bombonería es la etiqueta que hay delante de cada
#: bandeja: denominación, precio, precio por kilo del granel y alérgenos. Aquí
#: va el HITO —no se abre la puerta con una bandeja sin etiquetar— y de paso la
#: reposición, que es lo que decide si a las 12:00 queda vitrina o queda hueco.
#: El repaso referencia a referencia es de 01-apertura-cierre.xlsx:«Apertura»,
#: que es el detalle; el 08 comprueba que está hecho.
VITRINA_ETIQUETAS = ('Comprobar antes de abrir que ninguna bandeja de la '
                     'vitrina se queda sin su etiqueta de precio (y sin el '
                     'precio por kilo, si se vende al peso) ni sin sus '
                     'alérgenos a la vista, y que hay repuesto en cámara para '
                     'reponer durante el día')


def _zona_neg(ws, fila, vieja, nueva):
    """Zona (col. 3) de una tarea del molde ▸: sólo el VALOR, nunca el estilo.

    En 08 el relleno de la columna «Zona» es la CEBRA de la fila (medido:
    FFFFFF y F5F5F5 alternos en las 17 filas de «Apertura del Negocio»), no
    depende del VALOR como en las hojas P4 de este kit. Por eso aquí no se
    copia el estilo de ninguna parte —lo haría `_zona`, que es del molde P4— y
    se escribe sólo el texto. Idempotente, y con centinela: si la zona vieja no
    es la esperada, el molde ha cambiado y se para.
    """
    cel = ws.cell(row=fila, column=3)
    if cel.value == nueva:
        return False
    if cel.value != vieja:
        raise AnclaPerdida(f'«{ws.title}»: C{fila} tiene Zona «{cel.value}», '
                           f'esperaba «{vieja}» (kit-tareas-chocolateria)')
    cel.value = nueva
    return True


def _tarea_neg(ws, viejo, nuevo, zona_vieja=None, zona_nueva=None):
    """Sustitución 1:1 de una tarea de 08: texto y, si procede, su «Zona».

    Ancla por TEXTO (nunca por número de fila) y con la misma normalización
    que el motor deja en el molde ▸ (`_NORM` = `motor.forma_estable`).
    Devuelve True si ha cambiado algo.
    """
    r = _fila(ws, nuevo)
    cambiado = False
    if r is None:
        r = _exige(ws, viejo)
        ws.cell(row=r, column=2).value = nuevo
        cambiado = True
    if zona_nueva:
        cambiado = _zona_neg(ws, r, zona_vieja, zona_nueva) or cambiado
    return cambiado


def _f08(wb, cambios):
    # Devuelve True ante CUALQUIER cambio, no sólo ante uno estructural: en el
    # molde ▸ es lo que hace que `main.py` vuelva a pasar el motor, y
    # `motor.autoaltos` mide la ALTURA de fila por la longitud del texto. Sin
    # la 2.ª pasada, la 1.ª medía el texto viejo («Apagar vitrinas temperadas»,
    # 26 caracteres) y la 2.ª el nuevo (86): dos alturas distintas para el
    # mismo fichero y el gate de idempotencia en rojo. Medido: 2 diferencias en
    # las dos hojas de 08.
    tocado = False
    ws = wb['Apertura del Negocio']
    if _tarea_neg(ws, 'Encender vitrinas temperadas', VITRINA_08,
                  'Tienda', 'Vitrina'):
        tocado = True
        cambios.append('«Apertura del Negocio»: B20 pasa de encender la '
                       'vitrina a COMPROBAR que ha alcanzado su rango '
                       '(16-18 °C y menos del 55 % de humedad) antes de '
                       'montar el género, con hueco para la lectura; el '
                       'encendido se '
                       'va a B11, que es la fila con la hora temprana. Zona '
                       '«Tienda» → «Vitrina» (hallazgo «Vitrinas temperadas '
                       'sin objetivo de temperatura propio», media, + la '
                       'humedad, que no vigilaba ninguna hoja)')
    if _sustituir(ws, 'Verificar temperatura obrador (18-20 °C)',
                  OBRADOR_APERTURA):
        tocado = True
        cambios.append('«Apertura del Negocio»: la temperatura del obrador '
                       'añade la humedad y el hueco de lectura, y queda '
                       'simétrica con la de cierre — §2.9')
    if _tarea_neg(ws, 'Montar señalización exterior / pizarra de menú',
                  SENALIZACION):
        tocado = True
        cambios.append('«Apertura del Negocio»: B9 deja de mandar montar una '
                       '«pizarra de menú» que una bombonería no tiene y monta '
                       'lo que sí cuelga fuera —horario y cartel de encargos— '
                       'más la comprobación del sol sobre el escaparate, que '
                       'funde el género y no la hacía ninguna de las 11 hojas '
                       '(hallazgo baja de …-ver3.json)')
    if _tarea_neg(ws, 'Encender sistema de reservas / tablet de pedidos',
                  VITRINA_ENCENDER, 'Recepción', 'Vitrina'):
        tocado = True
        cambios.append('«Apertura del Negocio»: B11 pasa del «sistema de '
                       'reservas» de un restaurante al ENCENDIDO de las '
                       'vitrinas temperadas, que es lo que hay que poner en '
                       'marcha nada más entrar porque es lo que más tarda en '
                       'bajar; su comprobación de rango se queda en B20. Zona '
                       '«Recepción» → «Vitrina»: no hay recepción en un '
                       'mostrador (hallazgo baja de …-ver3.json)')
    if _tarea_neg(ws, 'Revisar reservas del día y eventos especiales',
                  ENCARGOS_08, 'Recepción', 'Mostrador'):
        tocado = True
        cambios.append('«Apertura del Negocio»: B13 pasa de «reservas del '
                       'día» a los ENCARGOS comprometidos para hoy (unidades, '
                       'hora '
                       'de recogida, quién los prepara) y al estuchado de los '
                       'de la mañana con sus cajas de regalo — el marco: la '
                       'agenda y los pedidos online siguen en 01 y la señal '
                       'cobrada, en 09. Zona «Recepción» → «Mostrador» '
                       '(hallazgo baja de …-ver3.json)')
    if _tarea_neg(ws, 'Revisar estado del mobiliario (sillas, mesas, '
                      'iluminación)', MOBILIARIO):
        tocado = True
        cambios.append('«Apertura del Negocio»: B16 revisaba «sillas, mesas» '
                       'en un local sin comedor; pasa al mobiliario que sí '
                       'hay (mostrador, estanterías y escaparate) y se queda '
                       'en ESTADO, no en limpieza, que ya es tarea de 01 — '
                       'barrido de «mesa» del 08/09')
    if _tarea_neg(ws, 'Comprobar que las cartas/menús están en orden',
                  VITRINA_ETIQUETAS, 'Sala', 'Vitrina'):
        tocado = True
        cambios.append('«Apertura del Negocio»: B18 pasa de repasar «las '
                       'cartas/menús» —que una bombonería no tiene— a '
                       'comprobar que ninguna bandeja de la vitrina se abre '
                       'sin etiqueta de precio, precio por kilo del granel y '
                       'alérgenos, y que hay repuesto en cámara. Zona '
                       '«Sala» → «Vitrina» (hallazgo baja de …-ver3.json)')
    ws = wb['Cierre del Negocio']
    if _sustituir(ws, 'Registrar temperatura de cierre del obrador',
                  OBRADOR_CIERRE):
        tocado = True
        cambios.append('«Cierre del Negocio»: la temperatura de cierre del '
                       'obrador ya trae objetivo (18-20 °C) y hueco para la '
                       'lectura; era la única de las dos que no lo tenía '
                       '(hallazgo «Temperatura de cierre del obrador sin '
                       'objetivo ni hueco de lectura», media)')
    if _tarea_neg(ws, 'Apagar vitrinas temperadas', VITRINA_CIERRE,
                  'Tienda', 'Vitrina'):
        tocado = True
        cambios.append('«Cierre del Negocio»: la vitrina no se apaga con el '
                       'género dentro — primero se retira a la cámara de '
                       'conservación. Zona «Tienda» → «Vitrina», la misma que '
                       'su pareja de apertura')
    return tocado


# ==========================================================================
# 09-apertura-cierre-caja.xlsx — molde ▸
# ==========================================================================
#: Hallazgo «09 no distingue caja de mostrador / venta al peso» (baja). Las 23
#: tareas de caja eran las genéricas de hostelería (TPV, datáfono, Bizum). En
#: una bombonería la mitad del ticket sale de una BÁSCULA: se vende al peso, se
#: estucha a mano y se cobra una señal por los encargos. Nada de eso se abría
#: ni se cuadraba.
PESO_APERTURA = [
    'Encender la báscula de mostrador, comprobar la tara de bandejas y '
    'estuches y verificarla con un peso patrón (venta al peso)',
    'Comprobar que el precio por kilo de cada referencia a granel coincide '
    'con el del TPV y con el cartel de la vitrina',
]
PESO_CIERRE = [
    'Cuadrar la venta al peso: kilos registrados en el TPV frente a lo '
    'descontado de las bandejas del día, y anotar la diferencia',
    'Registrar las señales cobradas por encargos y la lista de encargos '
    'pendientes de recoger (no son venta del día)',
]


def _f09(wb, cambios):
    tocado = False
    ws = wb['Apertura de Caja']
    if _insertar_trio(ws, 'Verificar cambio suficiente (monedas, billetes '
                          'pequeños)', PESO_APERTURA):
        cambios.append('«Apertura de Caja»: báscula de mostrador (tara y peso '
                       'patrón) y cuadre del precio por kilo entre cartel y '
                       'TPV — el fichero de caja era el genérico de hostelería '
                       'y en bombonería media caja sale de la báscula '
                       '(hallazgo «09 no distingue caja de mostrador/venta al '
                       'peso», baja)')
        tocado = True
    ws = wb['Cierre de Caja']
    if _insertar_trio(ws, 'Registrar anulaciones del día', PESO_CIERRE):
        cambios.append('«Cierre de Caja»: cuadre de la venta al peso y '
                       'registro de las señales de encargos, que no son venta '
                       'del día y descuadraban la Z (hallazgo «09 no distingue '
                       'caja de mostrador/venta al peso», baja)')
        tocado = True
    return tocado


# ==========================================================================
# API
# ==========================================================================
#: Ficheros del molde P4 con cambios de contenido propios.
P4 = {
    '01-apertura-cierre.xlsx': _f01,
    '02-partidas-produccion.xlsx': _f02,
    '03-tareas-manager.xlsx': _f03,
    '04-tareas-perfiles.xlsx': _f04,
    '05-tareas-semanales-mensuales.xlsx': _f05,
    '06-eventos-temporada.xlsx': _f06,
    'BONUS-01-briefing-servicio.xlsx': _bonus01,
    'BONUS-02-calendario-anual-tareas.xlsx': _bonus02,
}

#: Ficheros del molde ▸ (los 2 que el motor reconoce en este kit).
TRIO = {
    '08-apertura-cierre-negocio.xlsx': _f08,
    '09-apertura-cierre-caja.xlsx': _f09,
}

#: Molde P4 sin cambios propios: sólo la normalización transversal de textos.
#: El 07 son tres plantillas EN BLANCO y su diferenciación es MOTOR (§2.3),
#: fuera de alcance en este kit por ser P4.
SOLO_TEXTOS = ('07-plantilla-personalizable.xlsx',)


def post(wb, fname, cambios):
    """CONTENIDO sobre un libro ya normalizado por `motor.aplicar`.

    Devuelve True si ha cambiado la ESTRUCTURA (filas u hojas nuevas). En el
    molde ▸ ese valor hace que `main.py` vuelva a pasar el motor, que es quien
    reconstruye verdes, desplegable, formato condicional y precargas sobre la
    geometría nueva. En el molde P4 no lo usa nadie (no hay 2.ª pasada porque
    `aplicar` devolvió `{}`), así que la reconstrucción del contador, del
    formato condicional y del desplegable se hace AQUÍ antes de salir.
    """
    global _NORM
    if fname in TRIO:
        _NORM = _norm_trio
        return bool(TRIO[fname](wb, cambios))
    _NORM = _norm_p4
    fn = P4.get(fname)
    if fn is None and fname not in SOLO_TEXTOS:
        return False
    tocado = bool(fn(wb, cambios)) if fn else False
    for ws in wb.worksheets:
        _normalizar_textos(ws, cambios)
    # Contador honesto, formato condicional y bio con la geometría NUEVA. Es
    # idempotente: en la 2.ª pasada `motor.aplicar` ya lo dejó así y esto no
    # encuentra nada que cambiar.
    #
    # El registro se vacía ANTES porque las coordenadas que anotó `aplicar` son
    # las de la geometría VIEJA: al insertar siete tareas de higiene en
    # «Apertura» el contador bajó de la fila 29 a la 38 y `main.py` seguía
    # preguntando por el cache de C29 —una celda que ahora es una tarea— y lo
    # declaraba «fórmula sin valor». Lo único que hay en el registro de un
    # fichero P4 son los contadores, y `normalizar_p4` los vuelve a registrar
    # todos con su coordenada actual.
    motor.REGISTRO.clear()
    motor.normalizar_p4(wb, cambios)
    return tocado
