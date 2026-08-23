#!/usr/bin/env python3
"""
contenido_kit_tareas_heladeria.py — CONTENIDO propio de «kit-tareas-heladeria»
(hermano de la familia, §5 de `kit-tareas-v2-SPEC.md`).

Fuente de los cambios: `auditorias/kit-tareas-hermanos/kit-tareas-heladeria-verif.json`
campo `contenido_pendiente` (1 alta, 2 medias, 2 bajas) más los equivalentes de
§3 del representante que aplican a una HELADERÍA ARTESANAL con obrador propio.
`kit-tareas-heladeria-ver2.json` (tanda 3, campo `hallazgos_nuevos`) añade la
errata «manteccar»/«Manteccar» (doble C, severidad media) que corrige
`_arreglar_erratas` — sustitución por REGEX en CUALQUIER celda, no por ancla,
porque la errata puede repetirse con distinta redacción alrededor.

`kit-tareas-heladeria-ver3.json` (tanda 4, campo `hallazgos_nuevos`) añade dos
más, los dos en 08 y ya resueltos aquí: la MISMA lectura de la vitrina pedida
DOS VECES (01!«Apertura»!B16 y 08!«Apertura del Negocio»!B20-B21, con dos
huecos «____ °C» separados — severidad media) y la zona «Recepción» de la
tarea del sistema de reservas / tablet de pedidos (08!C11), que no encaja en
una heladería de mostrador directo (severidad baja).

`main.py` lo carga sólo con `--producto kit-tareas-heladeria` (compone el nombre
del módulo con el pid: `contenido_` + pid con guiones bajos), así que aquí se
puede hablar de «Mantecación», «Catering Eventos» o «Gestión Semanal» por su
nombre: son hojas de ESTE kit.

Contrato con `main.py`:
    post(wb, fname, cambios) -> bool

DOS MOLDES EN EL MISMO KIT, Y CADA UNO PIDE UNA COSA DISTINTA
================================================================================
`motor.aplicar` sólo reconoce el molde «▸» en 08 y 09 (kit «solo 08/09»). Los
01-07 y los dos BONUS son molde P4 y reciben únicamente la normalización mínima
(`motor.normalizar_p4`: desplegable «✓,—,N/A», contador honesto, formato
condicional y bio). De ahí salen las dos ramas de `post()`:

  · **08 (molde ▸)** — `motor.aplicar` devuelve estado truthy, así que `main.py`
    llamará a `motor.cerrar` por su cuenta. Aquí sólo se hacen sustituciones
    1:1 (no se toca la geometría) y se vuelve a pasar `motor.autoaltos`: la
    altura de fila se mide sobre el TEXTO, y si la 1.ª pasada la midió sobre el
    texto corto del motor y la 2.ª sobre el largo que escribe este módulo, el
    gate de idempotencia sale en rojo sin que nada esté roto (es exactamente el
    fallo que documenta `motor.autoaltos`, medido en este mismo fichero).
  · **01-07 y BONUS (molde P4)** — `motor.aplicar` devuelve `{}` (falsy), así
    que `main.py` **NO vuelve a pasar el motor** tras `post()` ni llama a
    `motor.cerrar`. Todo lo que dependa de la geometría nueva —rango del
    contador, formato condicional, desplegable de las filas nuevas, A4 y pie de
    la hoja nueva— **lo tiene que dejar hecho este módulo**. Por eso `post()`
    termina llamando a `motor.normalizar_p4` y por eso existen `_dv_extender` y
    `_hoja_legal`.
  · `motor.textos_de_tarea` (y con él `texto_grados`) tampoco corre sobre P4:
    medido en `02-partidas-produccion.xlsx:Mantecación:B21`, que seguía con
    «-18°C» en guion ASCII después del motor. La normalización transversal de
    grados (DOM-R2-22) la aplica aquí `_normalizar_grados`, al FINAL de cada
    fichero, y todos los textos nuevos de este módulo ya se escriben en su forma
    final para que la 2.ª pasada no encuentre nada que cambiar.
  · el molde P4 REPITE la fila de cabecera («# | Tarea | Zona | Responsable | ✓
    | Hora | Notas») en cada sección y **reinicia la numeración en 1** dentro de
    cada bloque: `motor.renumerar` (que va por `motor.geometria`, del molde ▸)
    devuelve None aquí. La numeración la rehace `_renumerar_p4`.
  · en este kit los bloques P4 van separados por una fila EN BLANCO (medido en
    «Apertura»: banda 4, cabecera 5, tareas 6-11, blanca 12, banda 13), así que
    `_insertar_seccion` pinta también la separadora. Y la sección nueva se
    inserta en la fila de la PRIMERA banda: así la cabecera repetida del bloque
    nuevo cae en la fila 5, que es donde `geometria_p4`, `freeze_panes` y
    `print_title_rows` esperan encontrarla.
  · «Responsable» y «Hora» van VACÍAS en todo el molde P4 de este kit (son
    verdes, las rellena el cliente). Las tareas nuevas respetan eso y sólo
    escriben #, Tarea y Zona. La excepción documentada es la hoja nueva
    «Trimestral y Anual», donde la CADENCIA es el dato.

QUÉ ES UNA HELADERÍA Y QUÉ NO (por qué no se copian los hallazgos del kit base)
================================================================================
No hay pescado crudo (ANISAKIS no aplica), no hay freidora (el aceite en frío no
aplica) y la única llama posible es la de una gofrera o una crepera, que el kit
menciona sólo como producto complementario de temporada baja: por eso el orden
seguro del gas entra como tarea CONDICIONAL y no como bloque. El riesgo de una
heladería está en otro sitio y es muy concreto:

  · **la temperatura tiene TRES niveles**, no dos, y confundirlos arruina el
    género: conservación −18 °C, servicio de vitrina −14 a −12 °C y maduración
    de la mezcla 2-4 °C. El hallazgo ALTA del verif.json es justo eso: el motor
    inyectó «(refrigeración 0-4 °C)» en la tarea de las vitrinas de 08 porque su
    patrón genérico no distingue una vitrina de sala de un expositor de helado;
  · **las vitrinas NO se apagan** con género dentro: pasan a modo conservación
    por la noche y vuelven a servicio por la mañana. «Encender vitrinas» es el
    DOM-24 de este kit;
  · **los alérgenos viajan en la pala**: pistacho, avellana y almendra pasan de
    una cubeta a otra con el porcionador, y el barquillo lleva gluten.

TRAMPAS DEL MOTOR QUE CONDICIONAN LA REDACCIÓN (§8 de la SPEC)
================================================================================
  · `motor.texto_temperatura` añade objetivo y «— anota la lectura: ____ °C» a
    toda tarea con verbo + «temperatura» + equipo de frío, PERO se retira si el
    texto ya trae «____ °C». Todos los textos de temperatura que escribe este
    módulo lo llevan, así que la 2.ª pasada del motor los deja intactos.
  · `motor.texto_appcc` cuelga una coletilla de toda celda con «APPCC» en el
    molde ▸: ningún texto nuevo de 08 la menciona. En P4 no corre, y las
    referencias al APPCC de 01 y de la hoja nueva se escriben ya honestas
    (DOM-R2-09) apuntando a la columna «Notas», que en este kit sí existe.
  · `motor.contexto` toma la hora ancla del kit de las hojas cuyo título empieza
    por «apertura», leyendo también los `hh:mm` sueltos de la COLUMNA A. Ningún
    rótulo de sección nuevo lleva una hora, o el ancla se movería entre pasadas
    y con ella toda la precarga de 08.

ANCLAS, NO NÚMEROS DE FILA: este módulo corre DESPUÉS de `motor.aplicar`. Si un
ancla no aparece se levanta `AnclaPerdida`: mejor caerse que publicar medio kit.
IDEMPOTENCIA: cada operación mira primero si su resultado ya está en el libro.
"""
import copy
import re

import motor
from motor import get_column_letter as L

#: Los checklists de este kit son A:G; el calendario del BONUS-02, A:F.
NCOL = 7
NCOL_CAL = 6

F01 = '01-apertura-cierre.xlsx'
F02 = '02-partidas-produccion.xlsx'
F03 = '03-tareas-manager.xlsx'
F04 = '04-tareas-perfiles.xlsx'
F05 = '05-tareas-semanales-mensuales.xlsx'
F06 = '06-eventos-temporada.xlsx'
F07 = '07-plantilla-personalizable.xlsx'
F08 = '08-apertura-cierre-negocio.xlsx'
B01 = 'BONUS-01-briefing-servicio.xlsx'
B02 = 'BONUS-02-calendario-anual-tareas.xlsx'

HOJA_LEGAL = 'Trimestral y Anual'

#: Relleno de la columna «Zona» por valor. Se usa sólo como respaldo: `_zona`
#: prefiere copiar el estilo de una fila real con la misma zona (de la propia
#: hoja primero y del libro después), que además trae bordes y fuente.
ZONA_COLOR = {
    'Admin': 'FFF8E1', 'Obrador': 'FFF3E0', 'Vitrina': 'E1F5FE',
    'Cámara': 'E3F2FD', 'Maduración': 'F3E5F5', 'Mostrador': 'FFF8E1',
    'Limpieza': 'EFEBE9', 'Almacén': 'ECEFF1', 'Equipo': 'E8F5E9',
    'Servicio': 'E8F5E9', 'General': 'F5F5F5', 'Logística': 'E3F2FD',
}


class AnclaPerdida(RuntimeError):
    """El texto que este módulo esperaba encontrar ya no está en la hoja."""


# ==========================================================================
# Utilidades de anclaje
# ==========================================================================
def _norm(v):
    """Texto comparable en el molde P4: sólo la normalización de grados.

    Así el mismo ancla vale en la 1.ª pasada (texto original, «-18°C») y en la
    2.ª (texto ya normalizado, «−18 °C»). NO se aplica `texto_appcc` ni
    `texto_temperatura`: en P4 el motor no los pasa, y aplicarlos aquí colgaría
    coletillas que el fichero entregado no tiene.
    """
    return motor.texto_grados(v) if isinstance(v, str) else v


def _estable(v):
    """Texto comparable en el molde ▸ (08): lo que el motor deja tras `aplicar`."""
    return motor.forma_estable(v)


def _fila(ws, texto, col=2, norm=_norm):
    texto = norm(texto)
    for r in range(1, ws.max_row + 1):
        if norm(ws.cell(row=r, column=col).value) == texto:
            return r
    return None


def _exige(ws, texto, col=2, norm=_norm):
    r = _fila(ws, texto, col, norm)
    if r is None:
        raise AnclaPerdida(f'«{ws.title}»: no encuentro '
                           f'{L(col)}=«{texto}» (kit-tareas-heladeria)')
    return r


def _estilos(ws, fila, ncol=NCOL):
    return [copy.copy(ws.cell(row=fila, column=c)._style)
            for c in range(1, ncol + 1)]


def _pintar(ws, fila, estilos):
    for c, st in enumerate(estilos, start=1):
        if st is not None:
            ws.cell(row=fila, column=c)._style = copy.copy(st)


def _zona(ws, fila, valor):
    """Escribe la Zona y le pone el relleno que esa zona tiene en el kit.

    El color de «Zona» depende del VALOR, no de la fila: copiar el estilo de la
    fila de anclaje pintaría la zona equivocada. Se busca primero en la propia
    hoja y después en el resto del libro, porque hay zonas («Obrador») que
    existen en 02 y no en la hoja «Apertura» de 01.
    """
    cel = ws.cell(row=fila, column=3)
    cel.value = valor
    for hoja in [ws] + [h for h in ws.parent.worksheets if h is not ws]:
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
    ws.cell(row=fila, column=2).value = _norm(texto)
    _zona(ws, fila, zona)


def _sustituir(ws, viejo, nuevo, col=2, norm=_norm):
    """Sustitución 1:1 por texto. Devuelve la fila, o None si ya estaba."""
    if _fila(ws, nuevo, col, norm) is not None:
        return None
    r = _exige(ws, viejo, col, norm)
    ws.cell(row=r, column=col).value = norm(nuevo)
    return r


def _fila_blanca(ws, desde):
    """Primera fila del todo vacía a partir de `desde` (la separadora)."""
    for r in range(desde, ws.max_row + 1):
        if all(ws.cell(row=r, column=c).value is None
               for c in range(1, NCOL + 1)):
            return r
    return None


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
    """Sección nueva del molde P4: banda + cabecera repetida + tareas + blanca.

    En P4 CADA sección repite su fila de cabecera; omitirla dejaría el bloque
    huérfano y, sobre todo, rompería la simetría que el contador da por hecha al
    restar `COUNTIF(B,"Tarea")`. Y la separadora en blanco existe en este kit:
    sin ella el bloque nuevo quedaría pegado al siguiente y sólo en esta hoja.
    """
    if _fila(ws, titulo, 1) is not None:
        return False
    idx = _exige(ws, antes_de, 1)
    est_banda = _estilos(ws, idx)
    est_cab = _estilos(ws, idx + 1)
    est_tarea = _estilos(ws, idx + 2)
    cabecera = [ws.cell(row=idx + 1, column=c).value
                for c in range(1, NCOL + 1)]
    blanca = _fila_blanca(ws, idx + 2)
    est_blanca = _estilos(ws, blanca) if blanca else [None] * NCOL
    n = len(tareas) + 3
    motor.insertar_filas(ws, idx, n)
    _pintar(ws, idx, est_banda)
    ws.cell(row=idx, column=1).value = titulo
    motor._merge(ws, f'A{idx}:{L(NCOL)}{idx}')
    _pintar(ws, idx + 1, est_cab)
    for c, v in enumerate(cabecera, start=1):
        ws.cell(row=idx + 1, column=c).value = v
    for i, (texto, zona) in enumerate(tareas):
        _pintar(ws, idx + 2 + i, est_tarea)
        _escribir_tarea(ws, idx + 2 + i, texto, zona)
    _pintar(ws, idx + n - 1, est_blanca)
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
        cambios.append(f'«{ws.title}»: {n} temperaturas normalizadas al signo '
                       'menos tipográfico y con espacio antes de la unidad '
                       '(DOM-R2-22, que el motor no aplica al molde P4)')
    return n


#: Hallazgo MEDIA de `kit-tareas-heladeria-ver2.json` (§`hallazgos_nuevos`):
#: «manteccar»/«Manteccar» (doble C) repetido 4 veces (03!Tareas Diarias!B9,
#: 04!Heladero-Obrador!B6 y B14, BONUS-01!Briefing Diario!B7) en vez de
#: «mantecar»/«Mantecar». La forma correcta ya existe en el mismo kit
#: (02!Mantecación!B32: «Mezcla base pasteurizada, sin mantecar»), lo que
#: confirma que es errata y no una variante de redacción. «mantecc» no es
#: sustituible por ancla exacta (`_sustituir`) porque el mismo error puede
#: repetirse con texto distinto alrededor y en hojas que este módulo ni
#: siquiera anota (04 y BONUS-01 están en `SOLO_GRADOS`, sin función propia):
#: se corrige por REGEX insensible a mayúsculas en CUALQUIER celda del kit.
RX_ERRATAS = [(re.compile(r'mantecc', re.IGNORECASE), 'mantec')]


def texto_erratas(v):
    """Corrige erratas conocidas del kit. Pura e idempotente: en la 2.ª pasada
    ya no encuentra «mantecc» y devuelve `v` sin tocar.
    """
    if not isinstance(v, str) or v.startswith('='):    # texto, no fórmula
        return v
    for patt, raiz in RX_ERRATAS:
        def _caso(m, raiz=raiz):
            hallado = m.group(0)
            if hallado.isupper():
                return raiz.upper()
            if hallado[0].isupper():
                return raiz[0].upper() + raiz[1:]
            return raiz
        v = patt.sub(_caso, v)
    return v


def _arreglar_erratas(ws, cambios):
    """Barre TODAS las celdas de texto de `ws` corrigiendo erratas conocidas.

    Sustitución 1:1 de texto: no toca geometría, estilos ni fórmulas. A
    diferencia de `_sustituir`, no necesita un ancla exacta —vale para
    cualquier celda del kit, esté o no anotada en las listas de este módulo—.
    """
    n = 0
    for row in ws.iter_rows():
        for c in row:
            nuevo = texto_erratas(c.value)
            if nuevo != c.value:
                c.value = nuevo
                n += 1
    if n:
        cambios.append(f'«{ws.title}»: {n} errata(s) corregidas («mantecc» '
                       'doble C → «mantec») — hallazgo MEDIA de '
                       'kit-tareas-heladeria-ver2.json (hallazgos_nuevos); la '
                       'forma correcta ya estaba en 02!Mantecación!B32')
    return n


def _instrucciones(wb, encabezado, lineas):
    """Bloque nuevo en «Instrucciones», ENCIMA de la bio y de la versión.

    `motor.reescribir_instrucciones` no corre en el molde P4, así que si el
    bloque se añadiera al final quedaría por debajo de la firma del autor y de
    la línea de versión, que son el cierre de la hoja.
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
        cel.value = _norm('▸ ' + txt)
        cel._style = copy.copy(est_txt)
    return True


# ==========================================================================
# 01-apertura-cierre.xlsx — hojas «Apertura» y «Cierre»
# ==========================================================================
#: DOM-12 + DOM-13 (equivalentes) — la jornada arrancaba encendiendo vitrinas.
#: En una heladería el manipulador sirve con porcionador, monta fruta cortada y
#: toca cucuruchos con la mano toda la tarde, y en los 11 ficheros no había una
#: sola línea de higiene personal. El bloque va DELANTE del primero, que es
#: cuando se hace. El gas entra como tarea condicional y no como bloque: la
#: única llama posible es la de la gofrera o la crepera, que este kit menciona
#: sólo como producto complementario de temporada baja (06!«Temporada Baja»!B7).
ARRANQUE = 'Higiene personal y arranque seguro'
ARRANQUE_TAREAS = [
    ('Uniforme y delantal limpios, pelo recogido con gorro o redecilla y '
     'calzado antideslizante', 'General'),
    ('Sin anillos, reloj ni pulseras; uñas cortas, limpias y sin esmalte: se '
     'sirve con porcionador y se manipulan cucuruchos y toppings', 'General'),
    ('Heridas y cortes cubiertos con apósito impermeable de color visible y '
     'guante encima', 'General'),
    ('Lavado de manos al entrar y en cada cambio de tarea: jabón, agua '
     'caliente y papel de un solo uso', 'General'),
    ('Declarar síntomas digestivos o respiratorios: quien los tenga no '
     'manipula helado, fruta ni toppings', 'General'),
    ('Encender la extracción del obrador y ventilar antes de poner en marcha '
     'pasteurizador y mantecadora', 'Obrador'),
    ('Si el obrador o la zona de gofres/crepes tiene GAS: abrir la llave '
     'general y comprobar que NO huele a gas ANTES de encender nada. Si '
     'huele, no enciendas, ventila y avisa al mantenedor', 'Obrador'),
]

#: DOM-24 (equivalente) — «Encender vitrinas de exposición» da por hecho que la
#: vitrina se apaga por la noche. Con género dentro NO se apaga: pasa a modo
#: conservación (−18 °C) y por la mañana vuelve a servicio (−14 a −12 °C). Lo
#: que hay que hacer al entrar es COMPROBAR que ha mantenido la temperatura,
#: porque si ha estado parada ocho horas el problema no es encenderla.
VITRINAS_VIEJO = 'Encender vitrinas de exposición y verificar temperatura -14°C/-12°C'
VITRINAS = ('Pasar las vitrinas de exposición de conservación nocturna '
            '(−18 °C) a modo servicio (−14 a −12 °C) y comprobar que han '
            'mantenido la temperatura toda la noche — anota la lectura: '
            '____ °C')

CAMARAS_VIEJO = 'Verificar cámaras de conservación a -18°C'
CAMARAS = ('Comprobar que las cámaras de conservación han funcionado toda la '
           'noche y registrar la temperatura (≤ −18 °C) — anota la lectura: '
           '____ °C. Si hay desviación, no sirvas el producto hasta valorarlo')

MADURACION_VIEJO = 'Verificar cámara de maduración a 2-4°C'
MADURACION = ('Comprobar la cámara de maduración (2-4 °C) — anota la lectura: '
              '____ °C: por encima de 4 °C una mezcla pasteurizada vuelve a '
              'ser un caldo de cultivo')

#: DOM-R2-09 — «Registrar temperaturas en hoja de control APPCC» manda a un
#: sitio que el cliente puede no tener. En este molde sí existe la columna G
#: «Notas», así que la alternativa honesta está a mano.
APPCC_VIEJO = 'Registrar temperaturas en hoja de control APPCC'
APPCC = ('Registrar las temperaturas del día (vitrinas, cámaras y maduración): '
         'si tienes el Pack APPCC, en su hoja de temperaturas; si no, en la '
         'columna «Notas» de esta hoja')

#: DOM-26 (equivalente) — la fruta de los toppings y de los sorbetes se sirve
#: CRUDA: es el único punto del kit donde un vegetal llega al cliente sin pasar
#: por el pasteurizador. Sin el aclarado final, la lejía se sirve con la fresa.
TOPPINGS_VIEJO = 'Montar toppings frescos: fruta, frutos secos, virutas de chocolate'
TOPPINGS = ('Montar toppings frescos: la FRUTA que se sirve cruda, lavada y '
            'desinfectada con lejía apta para uso alimentario según la dosis '
            'del fabricante (habitual: 70 ppm, 5 min) y ACLARADA con agua '
            'potable abundante; frutos secos y virutas, en recipiente cerrado')

#: DOM-19 (equivalente, punto de SERVICIO) — el kit habla de alérgenos tres
#: veces («recordar foco en alérgenos», «formación en alérgenos», «test de
#: alérgenos») y ninguna dice qué hacer en el mostrador. En una heladería el
#: alérgeno viaja en la pala: el pistacho pasa a la cubeta de al lado y de ahí
#: al cucurucho de quien no puede comerlo.
ALERGENOS = [
    ('Un porcionador por cubeta y enjuague entre sabores: el pistacho, la '
     'avellana y la almendra viajan de una cubeta a otra en la pala y son '
     'ALÉRGENOS de declaración obligatoria', 'Mostrador'),
    ('Tener a la vista la carta de ALÉRGENOS por sabor y comprobar que se '
     'corresponde con las cubetas que hay hoy en vitrina (leche, frutos '
     'secos, huevo, gluten del barquillo y la galleta, soja y sulfitos)',
     'Mostrador'),
]

CONSERVA_VIEJO = 'Pasar vitrinas a modo conservación -18°C'
CONSERVA = ('Pasar las vitrinas de exposición a modo conservación (−18 °C): no '
            'se apagan — con género dentro, una parada nocturna se lleva por '
            'delante la partida entera')

#: DOM-18 (equivalente) — la tarea existía pero sin unidad ni motivo, que es
#: justo lo que la convierte en un dato utilizable.
MERMAS_VIEJO = 'Registrar mermas del día (sabores agotados, producto desechado)'
MERMAS = ('Anotar las mermas del día (sabor, kg y motivo: agotado, desechado, '
          'cristalizado o descongelado): es el dato que corrige el food cost y '
          'la planificación de producción de mañana')


def _f01(wb, cambios):
    tocado = False
    ws = wb['Apertura']
    if _insertar_seccion(ws, 'Encendido y verificación de equipos', ARRANQUE,
                         ARRANQUE_TAREAS):
        cambios.append(f'«Apertura»: sección nueva «{ARRANQUE}» '
                       f'({len(ARRANQUE_TAREAS)} tareas) al INICIO de la hoja: '
                       'higiene personal, extracción antes de encender y '
                       'comprobación del gas si lo hay, que no existían en '
                       'ninguno de los 11 ficheros — DOM-12 / DOM-13 '
                       '(equivalentes)')
        tocado = True
    if _sustituir(ws, VITRINAS_VIEJO, VITRINAS):
        cambios.append('«Apertura»: las vitrinas no se ENCIENDEN, pasan de '
                       'conservación (−18 °C) a servicio (−14 a −12 °C) y se '
                       'COMPRUEBA que han aguantado la noche — DOM-24 '
                       '(equivalente)')
    if _sustituir(ws, CAMARAS_VIEJO, CAMARAS):
        cambios.append('«Apertura»: las cámaras se comprueban desde la noche '
                       'anterior, con objetivo, hueco para la lectura y qué '
                       'hacer si hay desviación — DOM-24 (equivalente)')
    if _sustituir(ws, MADURACION_VIEJO, MADURACION):
        cambios.append('«Apertura»: la cámara de maduración lleva hueco para '
                       'la lectura y la consecuencia de pasarse de 4 °C — '
                       'DOM-14 (equivalente)')
    if _sustituir(ws, APPCC_VIEJO, APPCC):
        cambios.append('«Apertura»: la referencia al APPCC deja de dar por '
                       'hecho que el cliente lo tiene y ofrece la columna '
                       '«Notas» como alternativa — DOM-R2-09')
    if _sustituir(ws, TOPPINGS_VIEJO, TOPPINGS):
        cambios.append('«Apertura»: la fruta de los toppings se sirve CRUDA — '
                       'desinfección con dosis y aclarado con agua potable — '
                       'DOM-26 (equivalente)')
    if _insertar_tras(ws, TOPPINGS, ALERGENOS):
        cambios.append('«Apertura»: contaminación cruzada de ALÉRGENOS en el '
                       'mostrador (un porcionador por cubeta) y carta de '
                       'alérgenos contrastada con la vitrina del día — DOM-19 '
                       '(equivalente, punto de servicio)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)

    ws = wb['Cierre']
    if _sustituir(ws, CONSERVA_VIEJO, CONSERVA):
        cambios.append('«Cierre»: el modo conservación se explica como lo que '
                       'es (la vitrina no se apaga) — DOM-24 (equivalente)')
    if _sustituir(ws, MERMAS_VIEJO, MERMAS):
        cambios.append('«Cierre»: las mermas del día con sabor, kg y motivo, y '
                       'para qué sirve el dato — DOM-18 (equivalente)')
    _renumerar_p4(ws)
    _dv_extender(ws)

    # Coherencia: la portada del fichero seguía prometiendo «encendido de
    # vitrinas» tres filas por encima del bloque que explica que no se apagan.
    if _sustituir(wb['Instrucciones'],
                  '▸ Incluye encendido de vitrinas, cámaras, montaje de '
                  'servicio y cierre.',
                  '▸ Incluye el paso de las vitrinas a modo servicio, la '
                  'comprobación de cámaras, el montaje y el cierre.'):
        cambios.append('Instrucciones: la portada ya no promete «encendido de '
                       'vitrinas» — con género dentro no se apagan (DOM-24)')

    if _instrucciones(wb, 'Higiene, alérgenos y temperaturas:', [
            'La primera sección de «Apertura» es de higiene personal y de '
            'arranque seguro: extracción primero y, si tienes gas para gofres '
            'o crepes, comprobación de olor antes de encender nada.',
            'Las tres temperaturas de una heladería son distintas y no se '
            'mezclan: conservación −18 °C, servicio de vitrina −14 a −12 °C y '
            'maduración de la mezcla 2-4 °C. Las vitrinas NO se apagan por la '
            'noche: pasan a conservación.',
            'Los alérgenos viajan en la pala: un porcionador por cubeta y '
            'enjuague entre sabores. El barquillo y la galleta llevan gluten, '
            'y pistacho, avellana y almendra son de declaración obligatoria.']):
        cambios.append('Instrucciones: higiene y arranque seguro, los tres '
                       'niveles de temperatura y los alérgenos del mostrador '
                       '— DOM-12 / DOM-14 / DOM-19')
        tocado = True
    return tocado


# ==========================================================================
# 02-partidas-produccion.xlsx — hoja «Mantecación»
# ==========================================================================
#: DOM-29 (equivalente) — «Etiquetar cubeta: … caducidad …» no dice CUÁL es esa
#: caducidad, y el kit produce con antelación y congela. La tabla va al pie,
#: debajo de la firma, es decir, fuera del rango que cuenta el contador: es una
#: referencia, no una tarea que marcar.
TITULO_VIDA_UTIL = ('VIDA ÚTIL ORIENTATIVA — ajústala a tu producto, a tu '
                    'maquinaria y a tu proveedor')
VIDA_UTIL = [
    ('Helado y sorbete artesanal en cubeta tapada', '2-3 meses a −18 °C',
     'En vitrina de servicio la calidad cae en 3-5 días: rota por sabor, no '
     'por la fecha larga de la cámara'),
    ('Mezcla base pasteurizada, sin mantecar', '3-5 días a 2-4 °C',
     'La base no se congela: al descongelar se separa y pierde estructura'),
    ('Tarta helada y semifrío montados', '1 mes a −18 °C',
     'Envueltos y en caja: absorben el olor de la cámara con una facilidad '
     'enorme'),
    ('Fruta y purés de fruta congelados', '6-12 meses a −18 °C',
     'Congela en porciones de un solo uso: descongelar y volver a congelar no '
     'se hace'),
    ('Frutos secos, pastas y pralinés', '6 meses a −18 °C · 2-3 meses en frío',
     'La grasa del fruto seco se enrancia sin avisar: fecha de apertura en el '
     'bote, siempre'),
    ('Variegatos, salsas y toppings abiertos', 'Lo que diga el fabricante',
     'El plazo cuenta desde la APERTURA: anótala en el envase el mismo día'),
]

ETIQUETAR_VIEJO = 'Etiquetar cubeta: sabor, fecha producción, caducidad, lote'
ETIQUETAR = ('Etiquetar cubeta: sabor, fecha de producción, caducidad y lote — '
             'la vida útil por familia está en la tabla del pie de esta hoja')


def _tabla_vida_util(ws, cambios):
    if _fila(ws, TITULO_VIDA_UTIL, 1) is not None:
        return False
    g = motor.geometria_p4(ws)
    if not g:
        raise AnclaPerdida('«Mantecación»: no es una hoja del molde P4')
    firma = None
    for r in range(g['contador'] or 1, ws.max_row + 1):
        v = ws.cell(row=r, column=1).value
        if isinstance(v, str) and v.startswith('Firma responsable'):
            firma = r
            break
    if firma is None:
        raise AnclaPerdida('«Mantecación»: no encuentro la fila de firma')
    banda = _exige(ws, 'Abatimiento y almacenaje', 1)
    est_titulo = _estilos(ws, banda)
    est_cab = _estilos(ws, g['hr'])
    est_dato = _estilos(ws, g['hr'] + 1)
    motor.insertar_filas(ws, firma + 1, 3 + len(VIDA_UTIL))
    fila = firma + 2
    _pintar(ws, fila, est_titulo)
    ws.cell(row=fila, column=1).value = TITULO_VIDA_UTIL
    motor._merge(ws, f'A{fila}:{L(NCOL)}{fila}')
    fila += 1
    _pintar(ws, fila, est_cab)
    ws.cell(row=fila, column=1).value = None
    ws.cell(row=fila, column=2).value = 'Familia'
    ws.cell(row=fila, column=3).value = 'Vida útil'
    ws.cell(row=fila, column=4).value = 'Notas'
    motor._merge(ws, f'D{fila}:{L(NCOL)}{fila}')
    for i, (familia, vida, nota) in enumerate(VIDA_UTIL, start=1):
        r = fila + i
        _pintar(ws, r, est_dato)
        ws.cell(row=r, column=1).value = None
        ws.cell(row=r, column=2).value = _norm(familia)
        ws.cell(row=r, column=3).value = _norm(vida)
        ws.cell(row=r, column=4).value = _norm(nota)
        for c in (2, 3, 4):
            motor._verde(ws.cell(row=r, column=c))
        motor._merge(ws, f'D{r}:{L(NCOL)}{r}')
    cambios.append('«Mantecación»: tabla editable de vida útil '
                   f'({len(VIDA_UTIL)} familias) al pie, fuera del rango del '
                   'contador — DOM-29 (equivalente)')
    return True


def _f02(wb, cambios):
    tocado = False
    ws = wb['Mantecación']
    if _sustituir(ws, ETIQUETAR_VIEJO, ETIQUETAR):
        cambios.append('«Mantecación»: la etiqueta remite a la tabla de vida '
                       'útil, que es la que dice qué caducidad escribir — '
                       'DOM-29 (equivalente)')
    if _tabla_vida_util(ws, cambios):
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)
    if _instrucciones(wb, 'Vida útil y caducidades:', [
            'Al pie de «Mantecación» tienes una tabla editable de vida útil '
            'por familia: ajústala a tu producto y a tu proveedor. Está fuera '
            'del contador porque es una referencia, no una tarea.',
            'La mezcla base pasteurizada NO se congela: se madura a 2-4 °C y '
            'se manteca en 3-5 días. Lo que se congela es el producto '
            'terminado, a −18 °C.']):
        cambios.append('Instrucciones: tabla de vida útil y por qué la base '
                       'no se congela — DOM-29 (equivalente)')
        tocado = True
    return tocado


# ==========================================================================
# 03-tareas-manager.xlsx — registro de jornada (RD-ley 8/2019)
# ==========================================================================
#: DOM-17 (equivalente) — hallazgo `contenido_pendiente` #3 del verif.json: no
#: hay ninguna tarea de registro horario en las cuatro hojas del 03. Una
#: heladería contrata refuerzo de temporada y hace jornadas largas en agosto:
#: es justo donde más horas se discuten, y el registro es obligatorio desde
#: 2019 para toda la plantilla.
JORNADA_DIARIA = [
    ('Cerrar y validar el registro diario de jornada del equipo (entradas, '
     'salidas y descansos) y que cada persona lo firme el mismo día: es '
     'obligatorio desde el RD-ley 8/2019, también para el refuerzo de '
     'temporada', 'Equipo'),
]
JORNADA_MENSUAL = [
    ('Archivar los registros de jornada del mes y conservarlos 4 años a '
     'disposición de la Inspección de Trabajo y de los representantes de los '
     'trabajadores', 'Equipo'),
]


def _f03(wb, cambios):
    tocado = False
    ws = wb['Tareas Diarias']
    if _insertar_tras(ws, 'Gestionar incidencias del turno anterior (libro de '
                          'novedades)', JORNADA_DIARIA):
        cambios.append('«Tareas Diarias»: cierre y validación del registro '
                       'diario de jornada, que no estaba en ninguna de las 4 '
                       'hojas del 03 — DOM-17 (equivalente)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)

    ws = wb['Tareas Mensuales']
    if _insertar_tras(ws, 'Planificar turnos y vacaciones del mes siguiente',
                      JORNADA_MENSUAL):
        cambios.append('«Tareas Mensuales»: archivo y conservación 4 años de '
                       'los registros de jornada — DOM-17 (equivalente)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)

    if _instrucciones(wb, 'Registro de jornada:', [
            'El registro horario diario es obligatorio para toda la plantilla '
            'desde el RD-ley 8/2019, temporeros incluidos: se cierra y se '
            'firma cada día y se archiva cada mes.',
            'Los registros se conservan 4 años y tienen que estar a '
            'disposición de la Inspección de Trabajo y de los representantes '
            'de los trabajadores.']):
        cambios.append('Instrucciones: obligación y plazo de conservación del '
                       'registro de jornada — DOM-17 (equivalente)')
        tocado = True
    return tocado


# ==========================================================================
# 05-tareas-semanales-mensuales.xlsx — mantenimiento legal y café
# ==========================================================================
#: DOM-15 (equivalente) — hallazgo `contenido_pendiente` #5: en el kit no hay
#: ni una mención a «café», «cafetera» o «descalcificar», pero 06!«Temporada
#: Baja»!B7 manda incorporar chocolate caliente, gofres y crepes, y la mayoría
#: de las heladerías con terraza sirven café. La tarea entra CONDICIONAL: si el
#: local no sirve café, se marca N/A y sale del contador.
CAFE = [
    ('Si sirves café o bebidas calientes: backflush del grupo con detergente, '
     'cambio de junta si toca y ciclo de limpieza del lavavajillas (filtros y '
     'brazos de lavado)', 'Obrador'),
]

TITULO_LEGAL_HOJA = 'Mantenimiento Trimestral y Anual'
#: DOM-16 (equivalente) — el kit tiene capa diaria, semanal y mensual, y ahí se
#: acaba. Todo lo que una inspección pide y que se CONTRATA fuera (DDD,
#: conductos, gases fluorados, extintores, legionela, pólizas) no aparecía en
#: ningún sitio. Los tres bloques se reparten a la medida del molde de «Tareas
#: Mensuales» de ESTE kit, que trae 4/3/5 filas de tarea.
LEGAL = [
    ('Trimestral — control por empresa externa', [
        ('Servicio de DDD (desinsectación y desratización) por empresa '
         'inscrita en el registro oficial: exige el parte firmado y anota su '
         'nº en «Notas»', 'Limpieza', 'Trimestral'),
        ('Limpieza de la campana y de los conductos de extracción del obrador '
         'por empresa autorizada, con certificado', 'Limpieza', 'Trimestral'),
        ('Revisión de la instalación frigorífica y control de fugas de gases '
         'fluorados (Rgto. UE 517/2014), con anotación en el libro del equipo',
         'Cámara', 'Trimestral'),
        ('Calibración externa de sondas y termómetros de vitrinas, cámaras y '
         'pasteurizador, con certificado: sin calibrar, el registro de '
         'temperaturas no prueba nada', 'Obrador', 'Semestral'),
    ]),
    ('Anual — seguridad de las instalaciones', [
        ('Revisión anual de extintores y BIE por empresa autorizada (y '
         'retimbrado del extintor cada 5 años): guarda el parte', 'Admin',
         'Anual'),
        ('Revisión de la instalación de gas si la hay (gofrera, crepera, agua '
         'caliente) y de la instalación eléctrica según la periodicidad que '
         'te corresponda', 'Admin', 'Anual'),
        ('Prevención de legionela si tienes agua caliente sanitaria de riesgo '
         'o nebulizadores de terraza: plan, tratamiento y registro', 'Admin',
         'Anual'),
    ]),
    ('Anual — documentación, seguros y sistemas', [
        ('Comprobar que el registro sanitario del establecimiento sigue '
         'vigente y que los datos que constan son los actuales', 'Admin',
         'Anual'),
        ('Revisar la formación en manipulación de alimentos y en alérgenos de '
         'TODA la plantilla, refuerzo de verano incluido', 'Admin', 'Anual'),
        ('Renovar la póliza y revisar coberturas, en especial la de pérdida de '
         'mercancía por avería del frío: una cámara parada en agosto se lleva '
         'la temporada entera', 'Admin', 'Anual'),
        ('Revisar con tu asesoría el TPV y el sistema de facturación '
         'verificable antes del cierre del ejercicio', 'Admin', 'Anual'),
        ('Archivar los registros de temperatura y limpieza del año y revisar '
         'el plan de autocontrol si has cambiado equipos, recetas o '
         'proveedores', 'Admin', 'Anual'),
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
    """Crea «Trimestral y Anual» clonando «Tareas Mensuales» y ajustando bloques.

    Se clona en lugar de construirse a mano porque el clon trae anchos, bordes,
    combinaciones y la geometría exacta del molde P4; lo que NO trae (medido con
    openpyxl) son el desplegable, el pie de impresión y los paneles
    inmovilizados, y por eso se le aplican aquí uno a uno.
    """
    if HOJA_LEGAL in wb.sheetnames:
        return False
    modelo = wb['Tareas Mensuales']
    ws = wb.copy_worksheet(modelo)
    ws.title = HOJA_LEGAL
    kit = motor.CTX.get('kit') or ''
    ws.cell(row=1, column=1).value = (TITULO_LEGAL_HOJA
                                      + (f' — {kit}' if kit else ''))
    g = motor.geometria_p4(ws)
    if not g:
        raise AnclaPerdida('«Tareas Mensuales»: el clon no es del molde P4')
    bloques = _bloques_p4(ws, g)
    if len(bloques) != len(LEGAL):
        raise AnclaPerdida(f'«Tareas Mensuales» tiene {len(bloques)} bloques y '
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
            ws.cell(row=r, column=2).value = _norm(texto)
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
                   '(DDD, conductos, gases fluorados, calibración de sondas, '
                   'extintores, gas, legionela, registro sanitario, formación '
                   'en alérgenos, póliza del frío y facturación) — DOM-16 '
                   '(equivalente); el kit no tenía ninguna capa anual')
    return True


def _f05(wb, cambios):
    tocado = False
    ws = wb['Gestión Semanal']
    if _insertar_tras(ws, 'Revisar estado de utensilios: espátulas, '
                          'porcionadores, moldes', CAFE):
        cambios.append('«Gestión Semanal»: mantenimiento semanal de la '
                       'cafetera y del lavavajillas, condicionado a que el '
                       'local sirva bebidas calientes (si no, N/A y sale del '
                       'contador) — DOM-15 (equivalente)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)
    if _hoja_legal(wb, cambios):
        tocado = True
    if _instrucciones(wb, 'Lo que no es semanal ni mensual:', [
            'La hoja «Trimestral y Anual» recoge lo que se contrata fuera y lo '
            'que pide una inspección: DDD, conductos de extracción, gases '
            'fluorados, calibración de sondas, extintores, gas, legionela, '
            'registro sanitario, formación en alérgenos, póliza y facturación.',
            'En esa hoja la columna «Cadencia» sustituye a «Hora», y el número '
            'de parte del mantenedor se anota en «Notas»: sin el parte '
            'firmado, la tarea no está hecha a efectos de inspección.',
            'La cobertura de pérdida de mercancía por avería del frío no es un '
            'extra en una heladería: es la que responde cuando una cámara se '
            'para en agosto.']):
        cambios.append('Instrucciones: para qué sirve la hoja «Trimestral y '
                       'Anual» y cómo se usa — DOM-16 (equivalente)')
        tocado = True
    return tocado


# ==========================================================================
# 06-eventos-temporada.xlsx — hoja «Catering Eventos»
# ==========================================================================
#: DOM-19 (equivalente, punto de PEDIDO) — hallazgo `contenido_pendiente` #4:
#: la hoja arranca en «Diseñar carta catering», es decir, con el pedido ya
#: aceptado. Lo que se pacta ANTES (alérgenos por escrito, comensales, señal y
#: cancelación) no estaba en ninguna parte, y en heladería el producto se
#: fabrica a medida: si el evento se cae, el helado no se revende.
CONFIRMAR = 'Al confirmar el pedido o el evento'
CONFIRMAR_TAREAS = [
    ('Recoger POR ESCRITO los alérgenos e intolerancias de los comensales y '
     'confirmar qué sabores puedes servir: una carta de heladería concentra '
     'LECHE, FRUTOS SECOS, HUEVO, GLUTEN (barquillo y galleta), SOJA y '
     'SULFITOS', 'Admin'),
    ('Confirmar por escrito nº de comensales, formatos, hora y lugar del '
     'servicio, y quién recibe el material en el sitio', 'Admin'),
    ('Fijar el precio por comensal (o por kg) y cobrar SEÑAL antes de '
     'producir: el helado se hace a medida y no se revende', 'Admin'),
    ('Acordar por escrito las condiciones de cancelación y hasta cuándo se '
     'puede cambiar el número de comensales', 'Admin'),
    ('Comprobar que hay hueco en cámara a −18 °C para todo el pedido ANTES de '
     'aceptarlo', 'Logística'),
]

LLEGADA_VIEJO = 'Verificar temperatura de producto a la llegada (<-12°C)'
LLEGADA = ('Verificar la temperatura del producto a la llegada (≤ −12 °C) — '
           'anota la lectura: ____ °C. Por encima, no lo sirvas: valóralo '
           'antes')


def _f06(wb, cambios):
    tocado = False
    ws = wb['Catering Eventos']
    if _insertar_seccion(ws, 'Preparación del evento', CONFIRMAR,
                         CONFIRMAR_TAREAS):
        cambios.append(f'«Catering Eventos»: sección nueva «{CONFIRMAR}» '
                       f'({len(CONFIRMAR_TAREAS)} tareas) delante de la '
                       'preparación: alérgenos por escrito, comensales, señal, '
                       'cancelación y hueco de cámara — DOM-19 (equivalente)')
        tocado = True
    if _sustituir(ws, LLEGADA_VIEJO, LLEGADA):
        cambios.append('«Catering Eventos»: la temperatura de llegada lleva '
                       'hueco para la lectura y qué hacer si no cuadra — '
                       'DOM-14 (equivalente)')
    _renumerar_p4(ws)
    _dv_extender(ws)
    if _instrucciones(wb, 'Antes de aceptar un evento:', [
            'La primera sección de «Catering Eventos» es lo que se pacta ANTES '
            'de producir: alérgenos por escrito, nº de comensales, precio, '
            'señal y condiciones de cancelación.',
            'Pide siempre señal: el helado de un evento se produce a medida y, '
            'si el evento se cae, no se revende.']):
        cambios.append('Instrucciones: qué se cierra por escrito antes de '
                       'aceptar un evento — DOM-19 (equivalente)')
        tocado = True
    return tocado


# ==========================================================================
# 08-apertura-cierre-negocio.xlsx — molde ▸ (el motor sí llega aquí)
# ==========================================================================
#: HALLAZGO ALTA del verif.json. `motor.texto_temperatura` inyectó
#: «(refrigeración 0-4 °C)» en la tarea de las vitrinas porque su patrón
#: `RX_EQUIPO_FRIO` no distingue una vitrina de sala de un expositor de helado.
#: 0-4 °C es temperatura de nevera: un helado a 0 °C es un batido. El propio
#: kit ya lo dice bien en 01!«Apertura»!B6 («-14°C/-12°C») y en 01!«Cierre»!B7
#: («modo conservación -18°C»), así que el libro se contradecía a sí mismo y un
#: empleado que siguiera 08 habría registrado como correcta una lectura que
#: significa que ha perdido la vitrina entera.
#: HALLAZGO MEDIA de `kit-tareas-heladeria-ver3.json` (§`hallazgos_nuevos`,
#: sin resolver hasta esta versión) — 01!«Apertura»!B16 y estas dos tareas de
#: 08 pedían la MISMA lectura de la MISMA vitrina en el mismo turno con DOS
#: huecos «____ °C» separados: uno en el detalle por ÁREA (01) y otro en el
#: checklist del LOCAL (08). El valor objetivo coincidía en los dos —no había
#: contradicción de dato, sólo trabajo duplicado—, así que la lectura se deja
#: SOLO en 01 (que es el detalle, §2.5 de la SPEC) y 08 pasa a ser el HITO sin
#: hueco, con referencia explícita al fichero que sí lleva la casilla.
NEG_VITRINAS_VIEJO = 'Comprobar temperaturas de todas las vitrinas'
NEG_VITRINAS = ('Vitrinas de helado en temperatura (−12/−14 °C; lectura '
                'anotada en 01-apertura-cierre)')

NEG_ENCENDER_VIEJO = 'Encender vitrinas/mantecadoras'
NEG_ENCENDER = ('Vitrinas de helado en modo servicio y mantecadoras '
                'encendidas (con género dentro no se apagan por la noche; '
                'detalle en 01-apertura-cierre)')

#: HALLAZGO MEDIA del verif.json — «Registrar temperaturas de cierre» no lleva
#: ni objetivo ni hueco de lectura porque no nombra ningún equipo y el patrón
#: del motor no la ve. Queda una asimetría absurda: la apertura pide la lectura
#: y el cierre no, en el mismo fichero.
NEG_CIERRE_VIEJO = 'Registrar temperaturas de cierre'
NEG_CIERRE = ('Registrar las temperaturas de cierre: vitrinas de exposición ya '
              'en modo conservación (−18 °C) y cámaras (≤ −18 °C) — anota la '
              'lectura: ____ °C')


def _zona_08(ws, tarea, zona_vieja, zona_nueva, cambios, motivo):
    """Sustitución 1:1 de la Zona (col. 3) de una tarea del molde ▸.

    Ancla por el TEXTO de la tarea (col. 2, con `_estable`), nunca por número
    de fila. Sólo cambia el VALOR de la celda — nunca su relleno ni su
    estilo, que ya trae el generador base — igual que `_sustituir` con el
    texto. Idempotente: si `zona_nueva` ya está puesta, no hace nada.
    """
    r = _fila(ws, tarea, col=2, norm=_estable)
    if r is None:
        raise AnclaPerdida(f'«{ws.title}»: no encuentro la tarea «{tarea}» '
                           '(kit-tareas-heladeria, zona)')
    actual = ws.cell(row=r, column=3).value
    if actual == zona_nueva:
        return False                                   # ya aplicado
    if actual != zona_vieja:
        raise AnclaPerdida(f'«{ws.title}»: la fila de «{tarea}» tiene Zona '
                           f'«{actual}», esperaba «{zona_vieja}»')
    ws.cell(row=r, column=3).value = zona_nueva
    cambios.append(f'«{ws.title}»: Zona de «{tarea}» «{zona_vieja}» → '
                   f'«{zona_nueva}» — {motivo}')
    return True


def _f08(wb, cambios):
    """Sustituciones 1:1 en el molde ▸. NO cambia la geometría (devuelve False).

    Al final se repasa `motor.autoaltos`: la 1.ª pasada del motor midió la
    altura de fila con SU texto (corto) y la 2.ª la mediría con el de aquí
    (largo), y esa diferencia de una fila tumba el gate de idempotencia. Es
    barato y es idempotente: `autoalto` sólo QUITA la altura fija, nunca la
    devuelve.
    """
    ws = wb['Apertura del Negocio']
    if _sustituir(ws, NEG_ENCENDER_VIEJO, NEG_ENCENDER, norm=_estable):
        cambios.append('«Apertura del Negocio»: la vitrina de helado no se '
                       'enciende, se pasa de conservación a servicio, y el '
                       'texto queda como HITO (sin repetir el detalle de 01) '
                       '— DOM-24 (equivalente)')
    if _sustituir(ws, NEG_VITRINAS_VIEJO, NEG_VITRINAS, norm=_estable):
        cambios.append('«Apertura del Negocio»: temperatura de vitrina de '
                       'EXPOSICIÓN DE HELADO (−14/−12 °C) en lugar del «0-4 '
                       '°C» genérico que inyectó el motor, que contradecía al '
                       'propio 01 y daba por buena una lectura de vitrina '
                       'perdida (hallazgo ALTA de kit-tareas-heladeria-ver3.'
                       'json). El hueco «____ °C» se retira de AQUÍ: 01 y 08 '
                       'pedían anotar la MISMA lectura dos veces, y la '
                       'casilla se deja SOLO en 01, que es el detalle por '
                       'ÁREA — hallazgo MEDIA de la misma verificación')
    if _zona_08(ws, 'Encender sistema de reservas / tablet de pedidos',
                'Recepción', 'Mostrador', cambios,
                'una heladería de mostrador directo no tiene una zona de '
                '«Recepción» separada del propio mostrador de venta — '
                'hallazgo BAJA de kit-tareas-heladeria-ver3.json'):
        pass
    motor.autoaltos(ws, cambios)

    ws = wb['Cierre del Negocio']
    if _sustituir(ws, NEG_CIERRE_VIEJO, NEG_CIERRE, norm=_estable):
        cambios.append('«Cierre del Negocio»: la temperatura de cierre lleva '
                       'objetivo y hueco para la lectura, igual que la de '
                       'apertura — hallazgo MEDIA de la verificación')
    motor.autoaltos(ws, cambios)

    for hoja in wb.worksheets:
        _arreglar_erratas(hoja, cambios)
    return False


# ==========================================================================
# BONUS-02 — calendario anual (tercer molde de la familia: una fila por MES)
# ==========================================================================
#: DOM-20 (equivalente) — este calendario no es el «# | Fecha | Evento» de los
#: hermanos ▸ ni el «Mes | Fecha / Evento» del representante: es «Mes |
#: Acciones clave / Fechas señaladas | Sabores destacados | Temporada | ✓ |
#: Notas», doce filas fijas. Las fechas que faltaban se añaden DENTRO del texto
#: del mes que les corresponde, sin tocar la geometría.
#:
#: Y de paso se corrige un error de fecha que estaba publicado: el Día de la
#: Madre figuraba en JUNIO. En España es el primer domingo de MAYO — un mes
#: entero de diferencia en la campaña de tartas heladas por encargo, que es la
#: que hay que producir con antelación.
CALENDARIO = [
    ('Marzo',
     'Semana Santa: sabores temáticos (torrija, mona). Preparar temporada '
     'alta: stock, equipo.',
     'Semana Santa: sabores temáticos (torrija, mona). 19 de marzo, Día del '
     'Padre: tartas heladas por encargo. Preparar temporada alta: stock, '
     'equipo.'),
    ('Abril',
     'Inicio primavera: ampliar carta con frutales. Reforzar equipo, '
     'formación.',
     'Inicio primavera: ampliar carta con frutales. Arranca la campaña de '
     'COMUNIONES (abril-junio): tartas heladas y catering, con señal y '
     'encargos cerrados 2 semanas antes. Reforzar equipo, formación.'),
    ('Mayo',
     'Inicio temporada alta. Carta completa 18-24 sabores. Abrir terraza.',
     'Inicio temporada alta. Carta completa 18-24 sabores. Abrir terraza. Día '
     'de la Madre (primer domingo de mayo) y comuniones: tartas heladas por '
     'encargo.'),
    ('Junio',
     'Inicio verano: máxima producción. Día de la Madre: tartas heladas. '
     'Campaña RRSS.',
     'Inicio verano: máxima producción. Fin de curso y San Juan (23-24): '
     'pedidos de grupo y noche larga de terraza. Campaña RRSS.'),
    ('Agosto',
     'Pico de temporada. Stock +50%. Catering eventos de verano.',
     'Pico de temporada. Stock +50%. 15 de agosto (Asunción), festivo nacional '
     'y día grande de muchas fiestas patronales. Catering eventos de verano.'),
    ('Noviembre',
     'Temporada baja. Productos complementarios: chocolate caliente, gofres. '
     'Mantenimiento.',
     'Temporada baja. 1 de noviembre (Todos los Santos), festivo: con buen '
     'tiempo sigue siendo día de terraza. Productos complementarios: chocolate '
     'caliente, gofres. Mantenimiento.'),
    ('Diciembre',
     'Navidad: turrón, polvorón, edición limitada. Catering empresas fin de '
     'año. Tartas heladas.',
     'Puente del 6-8 de diciembre: primer pico de la campaña. Navidad: turrón, '
     'polvorón, edición limitada. Catering empresas fin de año. Tartas '
     'heladas.'),
]


def _bonus02(wb, cambios):
    ws = wb['Calendario Anual']
    n = 0
    for mes, viejo, nuevo in CALENDARIO:
        r = _fila(ws, mes, 1)
        if r is None:
            raise AnclaPerdida(f'«Calendario Anual»: no encuentro el mes '
                               f'«{mes}» en la columna A')
        actual = ws.cell(row=r, column=2).value
        if _norm(actual) == _norm(nuevo):
            continue                                   # ya aplicado
        if _norm(actual) != _norm(viejo):
            raise AnclaPerdida(f'«Calendario Anual»: {mes} no dice lo que '
                               f'esperaba ({actual!r})')
        ws.cell(row=r, column=2).value = _norm(nuevo)
        n += 1
    if n:
        cambios.append(f'«Calendario Anual»: {n} meses con las fechas que '
                       'faltaban (Día del Padre, campaña de comuniones, San '
                       'Juan, 15 de agosto, 1 de noviembre y puente del 6-8 de '
                       'diciembre) — DOM-20 (equivalente); y el Día de la '
                       'Madre pasa de junio a MAYO, que es cuando es en España')
    if _instrucciones(wb, 'Fechas del calendario:', [
            'Las fechas nacionales están puestas para España: Día del Padre '
            '(19 de marzo), comuniones (abril-junio), Día de la Madre (primer '
            'domingo de mayo), San Juan, 15 de agosto, 1 de noviembre y el '
            'puente del 6-8 de diciembre.',
            'Cambia las que no apliquen en tu comunidad y añade las fiestas '
            'patronales de tu ciudad: son las que mueven una heladería de '
            'barrio.']):
        cambios.append('Instrucciones: de dónde salen las fechas del '
                       'calendario y qué hay que adaptar — DOM-20 '
                       '(equivalente)')
    return False


# ==========================================================================
# API
# ==========================================================================
#: Ficheros del molde P4 con cambios de contenido propios.
FICHEROS_P4 = {
    F01: _f01,
    F02: _f02,
    F03: _f03,
    F05: _f05,
    F06: _f06,
    B02: _bonus02,
}

#: Ficheros del molde P4 sin cambios propios: sólo la normalización transversal
#: de grados y el repaso de `normalizar_p4` con la geometría del momento.
SOLO_GRADOS = (F04, F07, B01)

#: Ficheros del molde ▸ (los que el motor sí reconoce en este kit).
FICHEROS_MARCO = {F08: _f08}


def post(wb, fname, cambios):
    """CONTENIDO sobre un libro ya normalizado por `motor.aplicar`.

    Devuelve True si ha cambiado la ESTRUCTURA. En el molde ▸ ese valor lo usa
    `main.py` para volver a pasar el motor antes de cerrar; en el molde P4 no
    (no hay 2.ª pasada porque `aplicar` devolvió `{}`), así que la
    reconstrucción del contador, del formato condicional y del desplegable se
    hace AQUÍ antes de salir.
    """
    fn = FICHEROS_MARCO.get(fname)
    if fn is not None:
        return bool(fn(wb, cambios))
    fn = FICHEROS_P4.get(fname)
    if fn is None and fname not in SOLO_GRADOS:
        return False
    tocado = bool(fn(wb, cambios)) if fn else False
    for ws in wb.worksheets:
        _normalizar_grados(ws, cambios)
        _arreglar_erratas(ws, cambios)
    # Contador honesto y formato condicional con la geometría NUEVA. Es
    # idempotente: en la 2.ª pasada `motor.aplicar` ya lo dejó así y esto no
    # encuentra nada que cambiar.
    #
    # El registro se vacía ANTES porque las coordenadas que anotó `aplicar` son
    # las de la geometría VIEJA: al insertar una sección en «Apertura» el
    # contador baja de fila y `main.py` seguiría preguntando por el cache de una
    # celda que ahora es una tarea, declarándola «fórmula sin valor». Lo único
    # que hay en el registro de un fichero P4 son los contadores, y
    # `normalizar_p4` los vuelve a registrar todos con su coordenada actual.
    motor.REGISTRO.clear()
    motor.normalizar_p4(wb, cambios)
    return tocado
