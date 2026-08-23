#!/usr/bin/env python3
"""
contenido_kit_tareas_dark_kitchen.py — CONTENIDO propio de
«kit-tareas-dark-kitchen» (hermano ▸ completo, §3 de `kit-tareas-v2-SPEC.md`
aplicado a una cocina 100 % delivery multi-marca).

Fuente de los cambios: `auditorias/kit-tareas-hermanos/
kit-tareas-dark-kitchen-verif.json`, campo `contenido_pendiente` (8 hallazgos:
4 altas y 4 medias), más los equivalentes de §3 del representante que aplican a
un dark kitchen: orden seguro del gas, higiene personal al inicio, anisakis del
pescado crudo, aceite sólo en frío, mermas del día, registro diario de jornada,
hoja «Trimestral y Anual» de mantenimiento legal en el 05, alérgenos al aceptar
el pedido, calendario del sector, cámaras que se «comprueban» y vida útil de
congelación. Y, del verificador de la tanda 3
(`kit-tareas-dark-kitchen-ver2.json`, `hallazgos_nuevos`), el vocabulario de
sala y terraza que quedaba en 08-apertura-cierre-negocio.xlsx (`_f08`).

NO es de familia. `main.py` lo carga sólo con
`--producto kit-tareas-dark-kitchen` (compone el nombre del módulo con el pid,
guiones → guiones bajos), así que aquí se puede hablar de «Estación Fría», de
«Empaquetado» o de «Gestor Plataformas» por su nombre: son hojas de ESTE kit.

Contrato con `main.py`:
    post(wb, fname, cambios) -> bool
`True` = «he cambiado la ESTRUCTURA del libro» (filas u hoja nuevas) y hace que
`main.py` vuelva a pasar `motor.aplicar` antes de `motor.cerrar`: es lo que mete
las filas nuevas en el rango del contador, en la DV y en el formato condicional,
y lo que convierte la hoja nueva «Trimestral y Anual» en una hoja de la familia
(DV, contador, A4, protección) en vez de en una isla.

CONDICIONANTES MEDIDOS EN ESTE HERMANO (no supuestos — salen del dry-run del
motor sobre los 11 ficheros reales):
  · **Sus bloques NO llevan fila separadora en blanco**: en «Apertura Cocina»
    la banda «  MISE EN PLACE» va pegada a la última tarea de «  EQUIPOS». El
    `_insertar_bloque` de aquí lo detecta con `_hay_separadores` en vez de dar
    por hecho el molde del representante.
  · **La hora ancla del kit es 09:00** (`motor.contexto`: la hora más temprana
    de las hojas de apertura, con la que precarga el 08). Ninguna tarea nueva
    de este módulo lleva una hora anterior, o el ancla se movería entre pasadas
    y el gate de idempotencia lo cazaría.
  · **«Mantenimiento Mensual» trae 3 bloques de 5/4/2 tareas** (el del
    representante trae 3 de 6/4/4 y el de cafetería 4 de 4/3/5/3): el contenido
    de «Trimestral y Anual» está repartido a ESA medida exacta o
    `_hoja_trimestral` levanta `AnclaPerdida`.
  · **«Mensual Manager» decide su cabecera por mayoría**: 6 valores «Día 1»
    votan «Día» y 8 «Mensual» votan «Cadencia» (`motor.cadencia`). La tarea
    nueva de archivo de jornada lleva «Mensual» a propósito: con «Día 1» el
    margen del voto se quedaría en 16 ≥ 15 y cualquier retoque posterior
    volcaría la cabecera de «Cadencia» a «Día».
  · **Sí hay pescado de consumo crudo**: la «Estación Fría» se llama
    «Ensaladas, Bowls y Poke», monta «arroz sushi» y el 05 inventaría «Salmón /
    pescado». Por eso aquí sí entra la tarea de congelación preventiva del
    anisakis, que en pizzería se descartó.

ANCLAS, NO NÚMEROS DE FILA: este módulo corre DESPUÉS de `motor.aplicar`, que ya
insertó las 5 filas libres, reescribió los grados y las temperaturas y renombró
cabeceras. Si un ancla no aparece se levanta `AnclaPerdida`: es preferible que
se caiga el dry-run entero a publicar un kit con medio contenido aplicado.

IDEMPOTENCIA: cada operación mira primero si su resultado ya está en el libro.

Trampas del motor que condicionan la redacción (§8 de la SPEC):
  · `motor.texto_temperatura` cuelga objetivo y «— anota la lectura: ____ °C» de
    toda tarea con verbo + «temperatura» + equipo de frío. El texto nuevo de las
    cámaras YA trae esa coletilla, o la 2.ª pasada se la añadiría otra vez.
  · `motor.texto_grados` normaliza los grados: los signos menos se escriben aquí
    con U+2212 y las unidades con espacio, tal y como quedarán.
  · `motor.texto_appcc` cuelga una coletilla de toda celda con «APPCC»: ningún
    texto de aquí la menciona (y el grep del kit confirmó que no había ninguna).
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
        raise AnclaPerdida(f'«{ws.title}»: no encuentro {L(col)}=«{texto}» '
                           '(kit-tareas-dark-kitchen)')
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


def _vacia(ws, fila):
    return all(ws.cell(row=fila, column=c).value is None
               for c in range(1, NCOL + 1))


def _hay_separadores(ws):
    """¿Las bandas de sección van precedidas de una fila en blanco?

    En `kit-tareas` sí; en `kit-tareas-dark-kitchen` no (medido: «  MISE EN
    PLACE» va pegada a la última tarea de «  EQUIPOS»). De esto depende que un
    bloque nuevo case con los que ya están impresos.
    """
    g = motor.geometria(ws)
    if not g:
        return False
    tope = g['contador'] or ws.max_row
    for r in range(g['hr'] + 2, tope):
        if motor.es_fila_seccion(ws, r) and _vacia(ws, r - 1):
            return True
    return False


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


def _sustituir_con_zona(ws, viejo, nuevo, zona=None):
    """Sustitución 1:1 de la TAREA y, si procede, de su «Zona» (columna C).

    La zona NO se puede tocar con `_sustituir(col=3)`: sus valores se repiten
    («Sala» está en DOS filas de «Apertura del Negocio», y «Terraza», «General»
    o «Acceso» en varias), así que el ancla cazaría la primera fila que
    coincidiera y reescribiría la zona de otra tarea. Aquí la zona se escribe
    SIEMPRE en la fila de su propia tarea, localizada por el texto de B.

    Idempotente por partida doble: si B ya está reescrito se localiza por el
    texto NUEVO y sólo se repasa C, así que una pasada a medias (B escrito y C
    no) se termina en la siguiente en vez de levantar `AnclaPerdida`.

    Devuelve cuántas celdas ha escrito (0 = ya estaba todo).
    """
    r = _fila(ws, nuevo, 2)
    n = 0
    if r is None:
        r = _exige(ws, viejo, 2)
        ws.cell(row=r, column=2).value = nuevo
        n += 1
    if zona is not None and ws.cell(row=r, column=3).value != zona:
        ws.cell(row=r, column=3).value = zona
        n += 1
    return n


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
    if all(motor.texto_grados(ws.cell(row=f, column=2).value)
           == motor.texto_grados(t[0]) for f, t in zip(filas, tareas)):
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

    Respeta el molde de la hoja: sólo añade la fila separadora en blanco si el
    resto de bloques la tienen (`_hay_separadores`). En este kit no la tienen,
    así que pintarla metería una fila hueca en mitad de una tabla que no las
    usa y cantaría al imprimir.
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


def _instrucciones(wb, encabezado, lineas):
    """Añade un bloque al final de la hoja «Instrucciones».

    `motor.reescribir_instrucciones` (que corre después, en `cerrar`) relee la
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
# 01 — apertura y cierre de la cocina de producción
# ==========================================================================
#: DOM-12 (equivalente) — «  HIGIENE» estaba al FINAL de la apertura (filas
#: 31-34 del dry-run del motor): impreso, el equipo se lava las manos y se pone
#: el uniforme DESPUÉS de haber encendido los fogones y montado la mise en
#: place. El bloque personal sube al principio, que es cuando se hace.
HIGIENE = [
    ('Uniforme y calzado de trabajo limpios, delantal cambiado y pelo '
     'recogido (gorro o redecilla)', 'Cocina', 'Todo el equipo', '09:00'),
    ('Sin anillos, reloj ni pulseras; uñas cortas, limpias y sin esmalte',
     'Cocina', 'Todo el equipo', '09:00'),
    ('Heridas y cortes cubiertos con apósito impermeable de color visible y '
     'guante encima', 'Cocina', 'Todo el equipo', '09:00'),
    ('Lavado de manos al entrar y en cada cambio de tarea o de marca; '
     'lavamanos con jabón, papel y agua caliente', 'Cocina', 'Todo el equipo',
     '09:00'),
    ('Declarar síntomas digestivos o respiratorios: quien los tenga no '
     'manipula alimentos', 'Cocina', 'Encargado/a', '09:00'),
]

#: Con el bloque personal arriba, la primera tarea del bloque de higiene que
#: quedaba al final («Lavarse manos, uniforme completo») pasaba a decir dos
#: veces lo mismo. Se cambia por la comprobación diaria que no tenía nadie: la
#: mensual revisa la presión y la caducidad del extintor, no que se pueda
#: llegar hasta él con la cocina llena de cajas de packaging.
BOTIQUIN = ('Comprobar que el botiquín y el extintor están accesibles y sin '
            'cajas de packaging delante')
#: Y la banda se renombra: con «HIGIENE PERSONAL» arriba, una banda «HIGIENE» a
#: secas al final no dice de qué higiene habla.
BANDA_HIGIENE = '  HIGIENE DE SUPERFICIES Y BOTIQUÍN'

#: DOM-13 (equivalente, ALTA) — el orden impreso era el inseguro: «Encender
#: todos los equipos: plancha, horno, freidora, fogones» (fila 6) ANTES que la
#: campana (fila 7) y que «Verificar gas: llaves abiertas, sin fugas» (fila 10).
#: Se encendía llama antes de comprobar que no hubiera fuga. El bloque se
#: reescribe en el orden en que se hace de verdad: campana → gas → fuego.
#: DOM-24 (equivalente) — y las cámaras se COMPRUEBAN desde la noche anterior,
#: que es cuando fallan; el texto trae ya la coletilla de
#: `motor.texto_temperatura` («____ °C»), así que el motor lo deja como está.
EQUIPOS = [
    ('Encender la campana extractora y ventilar la cocina ANTES de encender '
     'nada más', 'Cocina', 'Cocinero apertura', '09:00'),
    ('Verificar el gas ANTES de encender nada: abrir la llave general y '
     'comprobar que NO huele a gas; si huele, no enciendas, ventila y avisa '
     'al mantenedor', 'Cocina', 'Cocinero apertura', '09:00'),
    ('Encender los equipos en este orden: plancha, horno, freidora y fogones',
     'Cocina', 'Cocinero apertura', '09:00'),
    ('Encender baño maría si aplica', 'Cocina', 'Cocinero apertura', '09:15'),
    ('Comprobar que las cámaras frigoríficas han funcionado toda la noche y '
     'registrar temperatura (refrigeración 0-4 °C) — anota la lectura: '
     '____ °C. Si hay desviación, no uses el género hasta valorarlo',
     'Cocina', 'Cocinero apertura', '09:00'),
]

#: Hallazgo «alérgenos ausentes en el flujo de delivery» (ALTA) — el kit activa
#: y actualiza los menús de tres plataformas sin comprobar ni una vez la
#: información de alérgenos, que en venta a distancia hay que dar ANTES de que
#: el cliente compre (RD 126/2015, art. 4).
ALERGENOS_TABLETS = [
    ('Verificar que la información de ALÉRGENOS de cada plato sigue publicada '
     'y actualizada en la ficha de cada marca: en venta a distancia es '
     'obligatorio darla antes de que el cliente compre', 'Office',
     'Encargado/a', '10:30'),
]

#: Hallazgo «temperatura del aceite de freidora al cambiarlo» (media) — «Filtrar
#: o cambiar aceite de freidora si toca» sin decir a qué temperatura. Es la
#: quemadura más habitual de un cierre de cocina.
ACEITE_CIERRE = ('Filtrar o cambiar el aceite de la freidora si toca: '
                 'manipularlo SÓLO por debajo de 40 °C, nunca en caliente, '
                 'con guantes y recipiente estable; el usado, al bidón del '
                 'gestor autorizado')

#: Hallazgo «vida útil de congelación por familia ausente» (media) — «Congelar
#: lo que no se usará mañana» sin plazo ni fecha, y sin ninguna referencia de
#: cuánto aguanta cada familia. La tabla vive al pie de «FIFO Semanal» (05).
CONGELAR = ('Congelar EN EL DÍA lo que no se usará mañana, en porciones de un '
            'solo uso y etiquetado con la fecha (vida útil por familia en la '
            'tabla del pie de «FIFO Semanal», en '
            '05-tareas-semanales-mensuales.xlsx)')

#: Hallazgo «registro de mermas ausente» (media) — el cierre de cocina no
#: anotaba la merma del día pese a manejar producto fresco de vida corta y a
#: cobrar comisiones del 25-30 % por pedido. «Anotar faltantes por marca» no es
#: lo mismo: el faltante es lo que hay que pedir, la merma es lo que se ha
#: tirado.
MERMAS_CIERRE = [
    ('Anotar las mermas del día por marca (producto, cantidad y motivo): sin '
     'ese dato el food cost por marca del mes sale mal', 'Cocina',
     'Cocinero cierre', '22:00'),
]


def _f01(wb, cambios):
    tocado = False
    ws = wb['Apertura Cocina']
    if _insertar_bloque(ws, '  EQUIPOS', '  HIGIENE PERSONAL', HIGIENE):
        cambios.append('«Apertura Cocina»: bloque «HIGIENE PERSONAL» al '
                       f'INICIO ({len(HIGIENE)} tareas), que estaba al final '
                       'del checklist — DOM-12 (equivalente)')
        tocado = True
    if _reordenar_bloque(ws, '  EQUIPOS', EQUIPOS):
        cambios.append('«Apertura Cocina»: «EQUIPOS» en orden seguro (campana '
                       '→ comprobar gas → encender fuego) y las cámaras se '
                       '«comprueban» desde la noche anterior, no se '
                       '«verifican» a secas — DOM-13 / DOM-24 (equivalentes, '
                       'alta)')
    if _insertar_tras(ws, 'Verificar que menús están actualizados (precios, '
                          'disponibilidad)', ALERGENOS_TABLETS):
        cambios.append('«Apertura Cocina»: comprobación diaria de la '
                       'información de ALÉRGENOS publicada en cada marca (RD '
                       '126/2015, venta a distancia) — DOM-19 (equivalente, '
                       'alta)')
        tocado = True
    if _sustituir(ws, 'Lavarse manos, uniforme completo', BOTIQUIN):
        cambios.append('«Apertura Cocina»: la tarea de higiene que quedaba '
                       'duplicada al final pasa a comprobar que botiquín y '
                       'extintor están accesibles — DOM-12 (equivalente)')
    if _sustituir(ws, '  HIGIENE', BANDA_HIGIENE, col=1):
        cambios.append('«Apertura Cocina»: la banda «HIGIENE» del final pasa a '
                       '«HIGIENE DE SUPERFICIES Y BOTIQUÍN», que es lo que '
                       'cubre ahora que la personal está arriba')
    motor.renumerar(ws)

    ws = wb['Cierre Cocina']
    if _sustituir(ws, 'Congelar lo que no se usará mañana', CONGELAR):
        cambios.append('«Cierre Cocina»: congelar EN EL DÍA, en porciones y '
                       'con fecha, remitiendo a la tabla de vida útil del 05 '
                       '— DOM-29 (equivalente)')
    if _insertar_tras(ws, CONGELAR, MERMAS_CIERRE):
        cambios.append('«Cierre Cocina»: registro de las mermas del día por '
                       'marca, que no existía — DOM-18 (equivalente)')
        tocado = True
    if _sustituir(ws, 'Filtrar o cambiar aceite de freidora si toca',
                  ACEITE_CIERRE):
        cambios.append('«Cierre Cocina»: el aceite se manipula por debajo de '
                       '40 °C y el usado va a gestor autorizado — DOM-27 '
                       '(equivalente)')
    motor.renumerar(ws)
    return tocado


# ==========================================================================
# 02 — estaciones de producción
# ==========================================================================
#: Hallazgo «anisakis / pescado crudo sin tarea de congelación» (ALTA) — la
#: «Estación Fría» se titula «Ensaladas, Bowls y Poke», monta «arroz sushi» y el
#: inventario del 05 lista «Salmón / pescado», pero ninguna hoja del kit exigía
#: la congelación previa que impone el Reglamento (CE) 853/2004 al pescado que
#: se sirve crudo, marinado o semicrudo. La palabra «ANISAKIS» va en el texto a
#: propósito: es la que el cocinero y el inspector buscan con Ctrl+F.
ANISAKIS = [
    ('Pescado que se sirve CRUDO, marinado o semicrudo (poke, sushi, tartar, '
     'ceviche) — prevención de ANISAKIS: usar sólo pescado congelado '
     'previamente ≥24 h a −20 °C (o 15 h a −35 °C), o exigir el certificado '
     'al proveedor, y anotar el lote', 'Cocina', 'Cocinero frío', '09:15'),
]

#: Equivalente de DOM-26 — «Lavar y desinfectar vegetales» no dice ni con qué ni
#: a qué dosis, y sin el aclarado final la lejía se sirve dentro del bowl. En un
#: dark kitchen de poke el vegetal crudo es la mitad de la carta.
VEGETALES = ('Lavar y desinfectar las hojas verdes y los vegetales que se '
             'sirven crudos con lejía apta para uso alimentario según la '
             'dosis del fabricante (habitual: 70 ppm, 5 min) y ACLARAR con '
             'agua potable abundante')

#: Hallazgo «alérgenos ausentes en el flujo de delivery» (ALTA), segunda pata:
#: el cliente de delivery declara su alergia en las NOTAS del pedido y nadie las
#: leía. La decisión honesta —cancelar si no puedes garantizarlo— va escrita,
#: porque en una línea multi-marca la contaminación cruzada es la norma.
ALERGENOS_COCINA = [
    ('Leer las NOTAS del ticket ANTES de cocinar: si el cliente declara '
     'alergia o intolerancia, confirmar que la receta y la línea están '
     'limpias de ese alérgeno; si no puedes garantizarlo, cancela el pedido y '
     'avísale por la plataforma', 'Cocina', 'Cocinero caliente', '—'),
]
ALERGENOS_EMPAQUE = [
    ('Identificar con una etiqueta VISIBLE los pedidos con alergia declarada '
     'y colocarlos separados en la estantería de expedición, para que no se '
     'crucen con el resto', 'Packaging', 'Empaquetador', '—'),
]

#: Hallazgo «registro de mermas ausente» (media) — ninguna de las dos estaciones
#: de cocina anotaba la merma del turno.
MERMAS_CALIENTE = [
    ('Anotar las mermas del turno (producto, cantidad y motivo): lo que se '
     'pasa de punto o se devuelve también cuesta dinero', 'Cocina',
     'Cocinero caliente', '22:00'),
]
MERMAS_FRIA = [
    ('Anotar las mermas del turno: fruta y aguacate cortados, inserts '
     'agotados y bowls montados que no se han vendido', 'Cocina',
     'Cocinero frío', '22:00'),
]


def _f02(wb, cambios):
    tocado = False
    ws = wb['Estación Caliente']
    if _insertar_tras(ws, 'Cocinar según tickets de cada marca',
                      ALERGENOS_COCINA):
        cambios.append('«Estación Caliente»: leer las notas de alergias del '
                       'ticket ANTES de cocinar y cancelar si no se puede '
                       'garantizar — DOM-19 (equivalente, alta)')
        tocado = True
    if _insertar_tras(ws, 'Guardar pre-elaboraciones etiquetadas',
                      MERMAS_CALIENTE):
        cambios.append('«Estación Caliente»: tarea de mermas del turno — '
                       'DOM-18 (equivalente)')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Estación Fría']
    if _sustituir(ws, 'Lavar y desinfectar vegetales', VEGETALES):
        cambios.append('«Estación Fría»: desinfección de los vegetales de '
                       'consumo crudo con dosis y aclarado — DOM-26 '
                       '(equivalente)')
    if _insertar_tras(ws, 'Preparar bases: arroz sushi, quinoa, lechuga',
                      ANISAKIS):
        cambios.append('«Estación Fría»: congelación preventiva frente al '
                       'ANISAKIS del pescado que se sirve crudo o marinado '
                       '(Rgto. CE 853/2004) — DOM-02 (equivalente, alta)')
        tocado = True
    if _insertar_tras(ws, 'Desechar fruta/vegetales que lleven +24h cortados',
                      MERMAS_FRIA):
        cambios.append('«Estación Fría»: tarea de mermas del turno — DOM-18 '
                       '(equivalente)')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Empaquetado']
    if _insertar_tras(ws, 'Colocar sticker de marca + ticket del pedido',
                      ALERGENOS_EMPAQUE):
        cambios.append('«Empaquetado»: los pedidos con alergia declarada se '
                       'etiquetan y se separan en la estantería de expedición '
                       '— DOM-19 (equivalente, alta)')
        tocado = True
    motor.renumerar(ws)
    return tocado


# ==========================================================================
# 03 — manager / operador
# ==========================================================================
#: Hallazgo «registro de jornada del equipo ausente» (media) — ninguna de las
#: cuatro hojas del 03 cerraba ni archivaba el registro horario, obligación
#: legal en España desde el RD-ley 8/2019 (conservación: 4 años).
JORNADA_DIARIA = [
    ('Cerrar y validar el registro diario de jornada del equipo (entradas, '
     'salidas y pausas)', 'Office', 'Manager', '22:30'),
]
#: «Mensual» y no «Día 1» a propósito: ver el condicionante de la cabecera de
#: «Mensual Manager» en el docstring del módulo.
JORNADA_MENSUAL = [
    ('Archivar los registros de jornada del mes (hay que conservarlos 4 '
     'años)', 'Office', 'Manager', 'Mensual'),
]

#: Hallazgo «alérgenos» (ALTA), tercera pata: la ficha de la plataforma es el
#: documento que ve el cliente, y cambia cada vez que cambia un ingrediente o
#: un proveedor. La revisión semanal es la única que lo caza.
ALERGENOS_SEMANAL = [
    ('Revisar que la ficha de cada plato declara sus alérgenos y que coincide '
     'con la receta REAL: si ha cambiado un ingrediente o un proveedor, ha '
     'cambiado el alérgeno', 'Office', 'Manager', 'Lunes'),
]

#: Hallazgo «temperatura del aceite» (media) — el handover informaba del estado
#: del aceite sin decir cuándo se cambia ni a qué temperatura.
ACEITE_HANDOVER = ('Estado del aceite de la freidora y fecha del último '
                   'cambio (el cambio se hace en frío, por debajo de 40 °C)')


def _f03(wb, cambios):
    tocado = False
    ws = wb['Diario Manager']
    if _insertar_tras(ws, 'Supervisar cierre de cocina', JORNADA_DIARIA):
        cambios.append('«Diario Manager»: cierre y validación del registro '
                       'diario de jornada (RD-ley 8/2019) — DOM-17 '
                       '(equivalente)')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Semanal Manager']
    if _insertar_tras(ws, 'Actualizar fotos de platos si hay cambios',
                      ALERGENOS_SEMANAL):
        cambios.append('«Semanal Manager»: revisión semanal de los alérgenos '
                       'declarados en la ficha de cada plato — DOM-19 '
                       '(equivalente, alta)')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Mensual Manager']
    if _insertar_tras(ws, 'Coste laboral vs facturación total',
                      JORNADA_MENSUAL):
        cambios.append('«Mensual Manager»: archivo de los registros de '
                       'jornada del mes, que se conservan 4 años — DOM-17 '
                       '(equivalente)')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Handover Turno']
    if _sustituir(ws, 'Estado del aceite de freidora', ACEITE_HANDOVER):
        cambios.append('«Handover Turno»: el estado del aceite incluye la '
                       'fecha del último cambio y que el cambio va en frío — '
                       'DOM-27 (equivalente)')
    return tocado


# ==========================================================================
# 05 — semanales, mensuales y (nueva) trimestral/anual
# ==========================================================================
#: Hallazgo «temperatura del aceite» (media), las otras dos apariciones.
ACEITE_FIFO = ('Verificar el estado del aceite de la freidora (color, olor, '
               'humo) y anotar la fecha del último cambio; si hay que '
               'cambiarlo, en frío: por debajo de 40 °C, nunca en caliente')
ACEITE_MENSUAL = ('Cambio completo del aceite de la freidora, SIEMPRE por '
                  'debajo de 40 °C y nunca en caliente; el usado se entrega '
                  'al gestor autorizado y se archiva el documento')

#: Hallazgo «vida útil de congelación por familia ausente» (media). La tabla va
#: al pie de «FIFO Semanal», DEBAJO de la firma y por tanto FUERA del rango del
#: contador: es una referencia, no una tarea que haya que marcar.
TITULO_TABLA = ('VIDA ÚTIL ORIENTATIVA EN CONGELACIÓN A −18 °C — ajústala a tu '
                'producto y a tu proveedor')
TABLA_VIDA_UTIL = [
    ('Pollo y pavo crudos en piezas', '6-9 meses',
     'Congélalos el día que llegan, no el día que caducan en fresco'),
    ('Carne picada y patties de hamburguesa', '2-3 meses',
     'Toda la superficie está expuesta: se enrancia mucho antes que una '
     'pieza entera'),
    ('Pescado azul (salmón, atún)', '2-3 meses',
     'La grasa se enrancia aunque esté congelado; si es para servir crudo, '
     'la congelación cuenta además como tratamiento anti-ANISAKIS'),
    ('Pescado blanco y marisco ya cocido', '3-6 meses',
     'Congélalo en porciones planas: se descongela antes y con menos pérdida'),
    ('Salsas, fondos y caldos propios', '3 meses',
     'Etiquetar con fecha de producción Y de congelación: la vida útil de '
     'esta tabla se cuenta desde la de congelación'),
    ('Arroz y pasta ya cocidos', '1 mes',
     'Congelar el mismo día en porciones planas y regenerar por encima de '
     '75 °C: el arroz cocido templado es el clásico de la toxiinfección'),
    ('Pan de burger, wraps y pita', '1-3 meses',
     'Pierde textura antes que seguridad; descongela y regenera en horno'),
    ('Vegetales que se sirven crudos (aguacate, pepino, lechuga)',
     'No congelar',
     'Se deshacen al descongelar: en un bowl se ven, así que se piden '
     'frescos y se rota con FIFO'),
]

HOJA_TRIMESTRAL = 'Trimestral y Anual'
TRIMESTRAL_TITULO = 'Mantenimiento Trimestral y Anual — Revisiones Contratadas'
#: El molde («Mantenimiento Mensual» de ESTE kit) trae 3 bloques de 5/4/2
#: tareas. El reparto de abajo respeta esa medida exacta o `_hoja_trimestral`
#: levanta `AnclaPerdida`.
TRIMESTRAL = [
    ('  CONTRATADO — EMPRESA AUTORIZADA', [
        ('Control de plagas (DDD): visita de la empresa autorizada, parte '
         'firmado y certificado en vigor', 'Empresa DDD', 'Trimestral'),
        ('Limpieza de campana y conductos de extracción por empresa '
         'homologada', 'Empresa externa', 'Anual'),
        ('Revisión de extintores y BIE por empresa mantenedora (etiqueta y '
         'acta de revisión)', 'Mantenedor', 'Anual'),
        ('Revisión periódica de la instalación de gas por empresa habilitada, '
         'si el local tiene gas', 'Instalador gas', 'Cada 5 años'),
        ('Prevención de legionela si hay agua caliente sanitaria de riesgo o '
         'torre de refrigeración', 'Empresa autorizada', 'Anual'),
    ]),
    ('  FRÍO, ACEITE Y RESIDUOS', [
        ('Revisión de cámaras y abatidor por frigorista: estanqueidad, juntas '
         'y gas refrigerante', 'Frigorista', 'Anual'),
        ('Retirada del aceite usado de la freidora por gestor autorizado y '
         'archivo del documento de entrega', 'Gestor autorizado',
         'Trimestral'),
        ('Retirada de cartón y plástico de packaging por gestor autorizado: '
         'contrato en vigor y albaranes archivados (un dark kitchen genera '
         'más envase que un restaurante de sala)', 'Gestor autorizado',
         'Trimestral'),
        ('Calibrar los termómetros y las sondas contra un patrón conocido '
         '(agua con hielo, 0 °C)', 'Manager', 'Anual'),
    ]),
    ('  ADMINISTRACIÓN Y PLATAFORMAS', [
        ('Revisar la póliza del local y la responsabilidad civil POR PRODUCTO: '
         'en delivery el plato se consume fuera y el seguro de sala no siempre '
         'lo cubre', 'Manager', 'Anual'),
        ('Revisar los contratos y las comisiones de cada plataforma y el '
         'software de facturación (requisitos antifraude / Verifactu)',
         'Manager', 'Anual'),
    ]),
]


def _tabla_vida_util(ws, cambios):
    """Tabla editable de vidas útiles al pie de «FIFO Semanal»."""
    if _fila(ws, TITULO_TABLA) is not None:
        return False
    firma = _exige_prefijo(ws, 'Firma encargado/a:')
    g = motor.geometria(ws)
    if not g:
        raise AnclaPerdida('«FIFO Semanal»: no es un checklist de la familia')
    banda = _exige(ws, '  CÁMARAS')
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
                   f'congelación ({len(TABLA_VIDA_UTIL)} familias) al pie, '
                   'fuera del rango del contador — DOM-29 (equivalente)')
    return True


def _hoja_trimestral(wb, cambios):
    """La capa de mantenimiento CONTRATADO, que no existía en este kit.

    «Mantenimiento Mensual» cubre equipos y tablets, pero no lo que se contrata
    y lo que pide un inspector: DDD, conductos, extintores, gas, legionela,
    frigorista, gestor de aceite y de cartón, seguro y Verifactu.
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
                   '(DDD, conductos, extintores y BIE, gas, legionela, '
                   'frigorista, gestor de aceite y de cartón, seguro de RC por '
                   'producto y Verifactu) con nº de parte y firma — DOM-16 '
                   '(equivalente)')
    return True


def _f05(wb, cambios):
    tocado = False
    # El molde de la hoja nueva es «Mantenimiento Mensual» TAL CUAL sale del
    # motor. En la 2.ª pasada la hoja ya existe y no se clona.
    if _hoja_trimestral(wb, cambios):
        tocado = True

    ws = wb['FIFO Semanal']
    if _sustituir(ws, 'Verificar aceite freidora', ACEITE_FIFO):
        cambios.append('«FIFO Semanal»: el estado del aceite lleva fecha del '
                       'último cambio y el cambio va en frío — DOM-27 '
                       '(equivalente)')
    if _tabla_vida_util(ws, cambios):
        tocado = True

    ws = wb['Mantenimiento Mensual']
    if _sustituir(ws, 'Cambio aceite freidora completo', ACEITE_MENSUAL):
        cambios.append('«Mantenimiento Mensual»: el cambio de aceite se hace '
                       'por debajo de 40 °C y el usado va a gestor autorizado '
                       '— DOM-27 (equivalente)')

    if _instrucciones(wb, 'Trimestral, anual y vida útil en congelación', [
            'La hoja «Trimestral y Anual» recoge el mantenimiento que se '
            'CONTRATA y que se pide en una inspección: DDD, conductos de '
            'extracción, extintores y BIE, instalación de gas, legionela, '
            'frigorista, retirada del aceite usado y del cartón de packaging, '
            'seguro y facturación.',
            'Anota el número de parte en la columna verde y firma cuando la '
            'empresa haya venido; en la columna «Cadencia» tienes cada cuánto '
            'toca cada revisión.',
            'Al pie de «FIFO Semanal» tienes una tabla editable de vida útil '
            'en congelación por familia: una regla única para todo el '
            'congelador o tiras producto bueno o das por bueno producto '
            'pasado.']):
        cambios.append('Instrucciones: hoja trimestral/anual y tabla de vida '
                       'útil — DOM-16 / DOM-29 (equivalentes)')
    return tocado


# ==========================================================================
# 06 — picos y eventos
# ==========================================================================
#: Hallazgo «alérgenos» (ALTA), cuarta pata y la más barata de todas: la ficha
#: de una marca nueva se crea una sola vez, y si nace sin alérgenos los arrastra
#: para siempre. La tarea va ANTES de «Activar marca en plataformas».
ALERGENOS_LANZAMIENTO = [
    ('Declarar los 14 alérgenos de cada plato en la ficha de la plataforma '
     'ANTES de activar la marca: en venta a distancia la información tiene '
     'que estar disponible antes de que el cliente compre', 'Office',
     'Manager', '1 sem antes'),
]


def _f06(wb, cambios):
    tocado = False
    ws = wb['Lanzamiento Marca']
    if _insertar_tras(ws, 'Crear perfil en plataformas: fotos, descripciones, '
                          'precios', ALERGENOS_LANZAMIENTO):
        cambios.append('«Lanzamiento Marca»: los 14 alérgenos se declaran en '
                       'la ficha ANTES de activar la marca — DOM-19 '
                       '(equivalente, alta)')
        tocado = True
    motor.renumerar(ws)
    return tocado


# ==========================================================================
# 08 — apertura y cierre del NEGOCIO (el marco del día)
# ==========================================================================
#: Hallazgo del verificador de la tanda 3 (media) — el 08 es el ÚNICO fichero
#: del kit que seguía escrito para un restaurante con comedor: mandaba
#: «Montar terraza si aplica (mesas, sillas, sombrillas/estufas)», «Revisar
#: reservas del día» y «Revisar estado del mobiliario (sillas, mesas...)» en un
#: negocio 100 % delivery donde no entra ni un comensal. Es el mismo defecto
#: que ya se corrigió en `BRIEFING` (BONUS-01) para ESTE kit, sólo que en el
#: fichero que el motor precarga como MARCO del día y que el cliente imprime
#: cada mañana.
#:
#: Todo son sustituciones 1:1: MISMO número de filas, ni una fila nueva, y las
#: columnas D («Responsable») y E («Hora Límite» / «Cuándo») no se tocan — las
#: escribe `motor.precargar_negocio` POR POSICIÓN (`filas[i]`, no por texto),
#: así que reescribir el texto de una tarea no puede mover su responsable ni su
#: hora, y el gate `negocio_precargado` (2 checklists, 33 tareas, 0 huecos)
#: sigue verde. Por eso `_f08` devuelve False: no cambia la estructura y
#: `main.py` no necesita volver a pasar el motor por este fichero.
#:
#: Redacción atada a las trampas del §8 del motor (idempotencia de la 2.ª
#: pasada): ningún texto de aquí dice «temperatura» (RX_TEMP + verbo + equipo
#: de frío es lo que dispara la coletilla «— anota la lectura: ____ °C»), ni
#: «APPCC», ni lleva grados ni «=», así que `forma_estable()` los devuelve tal
#: cual y el motor no puede reescribirlos en la segunda pasada.
#:
#: Y ninguno vuelve a decir «Encender ... TPV»: esa tarea es el hito legítimo
#: del fichero de negocio y ya la tiene B10; una segunda haría saltar el
#: recuento de TPV del gate de §6.
#:
#: MEDIDO — hay que volver a llamar a `motor.autoaltos()` después de escribir.
#: Es la trampa R3-d del motor vista desde el otro lado: `motor.aplicar` mide
#: las alturas al final de SU pasada, y como `_f08` corre DESPUÉS y no devuelve
#: True (no cambia la estructura, así que el motor no vuelve a pasar), en la
#: 1.ª pasada el motor midió los textos CORTOS del original y dejó la altura
#: fija de 24 pt, mientras que en la 2.ª leyó ya los largos de aquí y se la
#: quitó: 2 diferencias de idempotencia («cambia alturas» en las dos hojas del
#: 08) sin nada roto. Los siete textos nuevos son más largos que los que
#: sustituyen, así que con `wrap_text` y 24 pt se imprimirían RECORTADOS por el
#: final —justo donde está el dato— si no se volviera a medir. `autoaltos` es
#: idempotente (sólo QUITA la altura fija de la fila que no cabe, nunca la
#: pone), así que llamarlo aquí deja las dos pasadas en el mismo sitio.
#: (texto viejo, texto nuevo, zona nueva)
NEGOCIO_APERTURA = [
    # B11 — «sistema de reservas» en una cocina sin sala: lo que hay que
    # encender es lo que IMPRIME la comanda. No duplica la tarea de las
    # tablets (B20): las tablets reciben el pedido, la impresora lo saca.
    ('Encender sistema de reservas / tablet de pedidos',
     'Encender la pantalla de comandas y la impresora de tickets de cada '
     'plataforma y comprobar que imprimen: sin ticket impreso el pedido se '
     'queda sin salir',
     'Operaciones'),
    # B13 — no hay reservas que revisar; hay pedidos programados y un tiempo de
    # preparación publicado que es lo que decide si la plataforma te manda más
    # pedidos de los que puedes sacar.
    ('Revisar reservas del día y eventos especiales',
     'Revisar los pedidos programados del día y ajustar los tiempos de '
     'preparación publicados en cada plataforma a la carga prevista',
     'Operaciones'),
    # B16 — el mobiliario de un dark kitchen es la zona por la que entran y
    # salen los riders, que es justo la que nadie revisaba.
    ('Revisar estado del mobiliario (sillas, mesas, iluminación)',
     'Revisar la zona de recogida de riders: mostrador de entrega despejado, '
     'estanterías de expedición señalizadas por marca e iluminación en orden',
     'Recogida riders'),
    # B17 — en vez de montar la terraza, se monta el puesto de empaquetado, que
    # es el cuello de botella real de una cocina de delivery.
    ('Montar terraza si aplica (mesas, sillas, sombrillas/estufas)',
     'Montar el puesto de empaquetado y etiquetado: cajas, bolsas, tapas, '
     'cubiertos, precintos de seguridad y etiquetas de cada marca al alcance',
     'Packaging'),
    # B18 — la «carta» que toca el cliente de delivery no es un menú de mesa:
    # son las etiquetas y los impresos que van DENTRO de la bolsa. No se
    # convierte en una segunda revisión del menú publicado porque esa ya la
    # hace 01-apertura-cierre.xlsx y §2.5 prohíbe duplicar el marco.
    ('Comprobar que las cartas/menús están en orden',
     'Comprobar que las etiquetas de marca, los flyers y las fichas de '
     'alérgenos impresas están repuestos en el puesto de empaquetado',
     'Packaging'),
]

NEGOCIO_CIERRE = [
    # B6 — no quedan clientes porque nunca entraron: lo que hay que comprobar
    # es que no queda un rider esperando ni un pedido sin recoger en la
    # estantería (el pedido olvidado se paga y se reclama por la plataforma).
    ('Verificar que no quedan clientes en el local',
     'Verificar que no queda ningún rider esperando ni pedidos sin recoger en '
     'la estantería de expedición',
     'Recogida riders'),
    # B7 — la terraza que hay que recoger es el puesto de empaquetado y la zona
    # de entrega, que acaban el día llenos de cartón y de precintos.
    ('Limpiar y recoger terraza si aplica',
     'Limpiar y recoger la zona de recogida y el puesto de empaquetado: '
     'retirar cartón, precintos y etiquetas sobrantes y dejar el mostrador de '
     'entrega despejado',
     'Packaging'),
]


def _f08(wb, cambios):
    n = 0
    ws = wb['Apertura del Negocio']
    for viejo, nuevo, zona in NEGOCIO_APERTURA:
        n += _sustituir_con_zona(ws, viejo, nuevo, zona)
    motor.autoaltos(ws, cambios)
    if n:
        cambios.append('«Apertura del Negocio»: 5 tareas y sus zonas pasan del '
                       'vocabulario de restaurante con comedor (reservas, '
                       'mobiliario de sala, montar terraza, cartas) al de una '
                       'cocina 100 % delivery (impresoras de plataforma, '
                       'pedidos programados y tiempos de preparación '
                       'publicados, zona de recogida de riders, puesto de '
                       'empaquetado y etiquetado) — hallazgo de la tanda 3 '
                       '(media), 1:1 y sin tocar Responsable ni Hora Límite')
    m = 0
    ws = wb['Cierre del Negocio']
    for viejo, nuevo, zona in NEGOCIO_CIERRE:
        m += _sustituir_con_zona(ws, viejo, nuevo, zona)
    motor.autoaltos(ws, cambios)
    if m:
        cambios.append('«Cierre del Negocio»: las 2 tareas de sala y terraza '
                       '(«no quedan clientes en el local», «recoger terraza») '
                       'pasan a la zona de recogida de riders y al puesto de '
                       'empaquetado — hallazgo de la tanda 3 (media), 1:1 y '
                       'sin tocar Responsable ni Cuándo')
    return False                       # sólo texto: la estructura no cambia


# ==========================================================================
# BONUS-01 — briefing pre-servicio
# ==========================================================================
#: Hallazgo «alérgenos ausentes en el flujo de delivery» (ALTA), parte final: el
#: único rastro de «alérgenos» de todo el kit estaba en «Reservas con alérgenos
#: declarados», heredado de un restaurante con sala y reservas de mesa. El
#: briefing entero hablaba de comensales, mesas VIP, barra y carta en un negocio
#: 100 % delivery donde no entra nadie. Son sustituciones 1:1 en la columna B:
#: la hoja es un formulario (B rótulo / C respuesta) y `motor.briefing` pinta de
#: verde la C de toda fila cuyo rótulo acabe en «:», así que hay que conservar
#: los dos puntos finales de cada uno.
BRIEFING = [
    ('RESERVAS Y OCUPACIÓN', 'PEDIDOS Y PREVISIÓN'),
    ('Nº de reservas:',
     'Pedidos previstos (mismo día de la semana pasada):'),
    ('Nº de comensales previstos:',
     'Marcas activas hoy y horario de cada una:'),
    ('Mesas VIP / clientes especiales:',
     'Promos activas por plataforma:'),
    ('Grupos o eventos:',
     'Eventos que mueven la demanda (partido, festivo, lluvia):'),
    ('Ocupación estimada:', 'Saturación estimada de la cocina:'),
    ('Plato del día 1:', 'Plato destacado de la marca 1:'),
    ('Plato del día 2:', 'Plato destacado de la marca 2:'),
    ('Postre especial:', 'Extra o postre del día:'),
    ('Cambios en carta:', 'Cambios en el menú de las plataformas:'),
    ('Reservas con alérgenos declarados:',
     'Alérgenos a vigilar hoy (recetas o proveedores que han cambiado):'),
    ('Restricciones a comunicar:',
     'Platos que NO se pueden servir sin un alérgeno y hay que rechazar:'),
    ('Personal sala:', 'Personal de empaquetado y expedición:'),
    ('Personal barra:', 'Gestor de plataformas y tablets:'),
]


def _bonus01(wb, cambios):
    ws = wb['Briefing']
    n = 0
    for viejo, nuevo in BRIEFING:
        if _sustituir(ws, viejo, nuevo, col=2) is not None:
            n += 1
    if n:
        cambios.append(f'«Briefing»: {n} rótulos pasan del vocabulario de sala '
                       '(reservas, comensales, mesas VIP, barra, carta) al de '
                       'un negocio 100 % delivery, y el bloque de alérgenos '
                       'pasa a hablar de pedidos, no de reservas — DOM-19 '
                       '(equivalente, alta)')
    return False                       # sólo texto: la estructura no cambia


# ==========================================================================
# BONUS-02 — calendario anual
# ==========================================================================
#: Hallazgo «calendario anual no adaptado a dark kitchen» (ALTA), dos mitades.
#: Primera: faltan las cinco fechas que la SPEC exige incorporar en la v2.0
#: (DOM-20). Se insertan ANTES de renombrar nada, para que las anclas de la
#: columna B sigan siendo las del libro que salió del motor.
#: (ancla en col B, mes, evento, tareas, antelación)
FECHAS = [
    ('Carnaval (variable)', 'Marzo', '19 Mar — Día del Padre',
     'Menú para llevar de sobremesa familiar, promo de mediodía en cada '
     'marca', '2 semanas'),
    ('Apertura terraza', 'Abril-Junio', 'Comuniones y bautizos (temporada)',
     'Bandejas y menús de grupo para recoger o entregar, precio por persona '
     'y packaging para transporte', '1 mes'),
    ('Temporada alta', 'Agosto', '15 Ago — Asunción',
     'Servicio de festivo con equipo reducido: revisar qué marcas se '
     'mantienen activas y cuáles se pausan', '1 semana'),
    # Detrás de Halloween, no de «Vuelta al cole»: el 1 de noviembre va DESPUÉS
    # del 31 de octubre y el calendario es cronológico.
    ('31 Oct — Halloween', 'Noviembre', '1 Nov — Todos los Santos',
     'Festivo de mediodía familiar: pico temprano y stock para dos días '
     'seguidos', '1 semana'),
    ('Cierre terraza', 'Diciembre',
     '6-8 Dic — Puente de la Constitución y la Inmaculada',
     'Tres festivos seguidos: stock, refuerzo de turnos y horario publicado '
     'en cada plataforma', '2 semanas'),
]

#: Segunda mitad: el calendario estaba redactado para un restaurante con sala y
#: terraza. Aquí no hay comensales, ni mesas, ni cotillón: hay pedidos, riders,
#: packaging y fichas de plataforma. Las dos filas de terraza no se borran —el
#: buen y el mal tiempo SÍ mueven el delivery, sólo que al revés—, se reescriben
#: con lo que de verdad pasa en una dark kitchen esas semanas.
TEXTOS = [
    # (ancla col B, nuevo evento o None, nuevas tareas)
    ('1 Ene — Año Nuevo', None,
     'Decidir si se abre; si se cierra, pausar las marcas en TODAS las '
     'plataformas y publicar el horario con 1 semana'),
    ('6 Ene — Reyes', None,
     'Roscón y menú familiar para llevar, pico de mediodía'),
    ('14 Feb — San Valentín', None,
     'Menú para dos en formato delivery, packaging cuidado y refuerzo de la '
     'cena'),
    ('Carnaval (variable)', None,
     'Menú temático en plataformas y promo de fin de semana'),
    ('Semana Santa (variable)', None,
     'Menú de vigilia por marca (bacalao, potaje, torrijas) y refuerzo del '
     'mediodía'),
    ('Apertura terraza', 'Buen tiempo: cae el pedido de mediodía',
     'Ajustar producción y turnos a la baja, reforzar promos de cena y de fin '
     'de semana'),
    ('1 Mayo — Día del Trabajo', None,
     'Servicio de festivo: confirmar riders y horario publicado por marca'),
    ('Primer domingo — Día de la Madre', None,
     'Menú especial para llevar, packaging cuidado y refuerzo del pico de '
     'mediodía'),
    ('Inicio temporada alta', None,
     'Refuerzo de plantilla y stock de verano; revisar tiempos de preparación '
     'en pico'),
    ('24 Jun — San Juan', None,
     'Menú especial de noche, refuerzo del pico tardío y de la salida de '
     'riders'),
    ('Temporada alta', None,
     'Personal extra, horarios ampliados y menú de verano por marca'),
    ('Vuelta al cole / rutina', None,
     'Menú de otoño por marca y promo de mediodía para oficinas'),
    ('31 Oct — Halloween', None,
     'Menú y packaging temáticos, promo de noche en plataformas'),
    ('Cierre terraza', 'Frío y lluvia: sube el pedido',
     'Reforzar turnos y stock, vigilar los tiempos de preparación y el '
     'embalaje que aguanta el traslado'),
    ('Cenas de empresa', 'Pedidos de grupo y catering de oficina',
     'Menú cerrado por persona, packaging para transporte, confirmación con '
     'antelación y turnos extra'),
    ('24-25 Dic — Nochebuena/Navidad', None,
     'Menú navideño por marca, packaging especial y stock para la semana con '
     'menos entregas de proveedor'),
    ('31 Dic — Nochevieja', None,
     'Menú de gala para llevar, cierre temprano de pedidos y horario avisado '
     'en cada plataforma'),
]


def _bonus02(wb, cambios):
    ws = wb['Calendario Anual']
    tocado = False
    # 1) fechas que faltaban — SIEMPRE antes de renombrar, o el ancla se pierde
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

    # 2) vocabulario del sector: fuera terraza, comensales y cotillón
    n = 0
    for ancla, evento, tareas in TEXTOS:
        r = _fila(ws, ancla, 2)
        if r is None:
            if evento and _fila(ws, evento, 2) is not None:
                continue                               # ya reescrito
            raise AnclaPerdida(f'«Calendario Anual»: no encuentro B=«{ancla}»')
        if evento:
            ws.cell(row=r, column=2).value = evento
        if ws.cell(row=r, column=3).value != tareas:
            ws.cell(row=r, column=3).value = tareas
            n += 1
    if n:
        cambios.append(f'«Calendario Anual»: {n} fechas reescritas en '
                       'vocabulario de dark kitchen (pedidos, riders, '
                       'packaging y fichas de plataforma en vez de mesas, '
                       'comensales y terraza) y las dos filas de terraza pasan '
                       'a ser el efecto REAL del tiempo sobre el delivery — '
                       'hallazgo «calendario no adaptado» (alta)')
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
    '08-apertura-cierre-negocio.xlsx': _f08,
    'BONUS-01-briefing-servicio.xlsx': _bonus01,
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
