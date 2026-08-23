#!/usr/bin/env python3
"""
contenido_kit_tareas_catering.py — CONTENIDO propio de «kit-tareas-catering»
(hermano de la familia, §5 de `kit-tareas-v2-SPEC.md`).

Fuente de los cambios: `auditorias/kit-tareas-hermanos/kit-tareas-catering-verif.json`
campo `contenido_pendiente` (1 alta, 1 media, 3 bajas) más los equivalentes de
§3 del representante que aplican a una empresa de catering / eventos.

`main.py` lo carga sólo con `--producto kit-tareas-catering` (compone el nombre
del módulo con el pid: `contenido_` + pid con guiones bajos), así que aquí se
puede hablar de «Producción», «Transporte» o «Cocktail Standing» por su nombre:
son hojas de ESTE kit.

Contrato con `main.py`:
    post(wb, fname, cambios) -> bool

ESTE KIT ES DE MOLDE P4 EN 10 DE SUS 11 FICHEROS — la diferencia que lo
condiciona todo
================================================================================
`motor.aplicar` sólo reconoce el molde «▸» en 08 y 09. Los 01-07 y BONUS-01 son
molde P4 y reciben únicamente la normalización mínima (`motor.normalizar_p4`:
desplegable, contador honesto, formato condicional y bio). En consecuencia,
para los ficheros que toca este módulo:

  · `motor.aplicar` devuelve `{}` (falsy), así que `main.py` **NO vuelve a pasar
    el motor** tras `post()` ni llama a `motor.cerrar`. Todo lo que dependa de
    la geometría nueva —rango del contador, formato condicional, desplegable de
    las filas nuevas, A4 y pie de una hoja nueva— **lo tiene que dejar hecho
    este módulo**. Por eso `post()` termina llamando a `motor.normalizar_p4` y
    por eso existen `_dv_extender` y `_alta_de_hoja`.
  · `motor.textos_de_tarea` (y con él `texto_grados`, `texto_appcc` y
    `texto_temperatura`) tampoco corre sobre P4: medido en
    `02-partidas-cocina.xlsx:Transporte:B8`, que seguía con «≤-18°C» en guion
    ASCII después del motor. La normalización transversal de grados (DOM-R2-22)
    la aplica aquí `_normalizar_grados`, al FINAL de cada fichero, y todos los
    textos nuevos de este módulo ya se escriben en su forma final para que la
    2.ª pasada no encuentre nada que cambiar.
  · el molde P4 REPITE la fila de cabecera («# | Tarea | Zona | Responsable | ✓
    | Hora | Notas») en cada sección y **reinicia la numeración en 1** dentro de
    cada bloque: `motor.renumerar` (que va por `motor.geometria`, del molde ▸)
    devuelve None aquí. La numeración la rehace `_renumerar_p4`.
  · las columnas «Responsable» y «Hora» van VACÍAS en todo el molde P4 de este
    kit (son verdes, las rellena el cliente). Las tareas nuevas respetan eso y
    sólo escriben #, Tarea y Zona. La única excepción documentada es la hoja
    nueva «Trimestral y Anual», donde el responsable y la cadencia son el dato.
  · el color de la columna «Zona» depende del VALOR («Admin» crema, «Producción»
    naranja, «Transporte» azul…). Copiar el estilo de la fila de anclaje pinta
    la zona equivocada, así que `_zona` busca en la propia hoja una fila con esa
    zona y le copia el relleno.

DÓNDE VAN LOS HALLAZGOS QUE EN EL REPRESENTANTE VIVEN EN OTRO FICHERO
================================================================================
El nombre de los ficheros de este kit viene heredado del kit base y NO describe
su contenido (comprobado hoja a hoja, no supuesto):

  01-apertura-cierre.xlsx            → «Producción» off-site (planificación,
                                        D-1 y día D). No hay apertura de local.
  02-partidas-cocina.xlsx            → «Transporte» y logística. No hay partidas.
  05-tareas-semanales-mensuales.xlsx → «Montaje» y «Desmontaje» del venue. No
                                        hay ninguna cadencia semanal ni mensual.

Por eso:
  · la tabla de vida útil en congelación (DOM-29) va al pie de 01 «Producción»,
    que es la hoja que congela y produce con antelación, y no al 05, que monta
    sillas;
  · la hoja «Trimestral y Anual» de mantenimiento legal (DOM-16) se crea en
    03-tareas-manager.xlsx, el libro del director, que es quien contrata la DDD,
    renueva el ATP del vehículo y paga la póliza — no en un libro de montaje;
  · el orden seguro campana → gas → equipos (DOM-13) y la higiene personal
    (DOM-12) van a 01 «Producción», que es donde se enciende la cocina.

LA EXCEPCIÓN: el 08 TAMBIÉN lleva contenido propio (molde «▸»)
================================================================================
El 11.º fichero, `08-apertura-cierre-negocio.xlsx`, sí es molde «▸» y sí lo
normaliza el motor, pero su LISTA DE TAREAS es la genérica del generador v1.1,
la misma en los 12 kits de la familia: un checklist de restaurante con sala
abierta al público (pizarra de menú, sistema de reservas, música ambiente,
cartas/menús, terraza) dentro de un kit de producción off-site. El motor no
puede arreglarlo —es contenido de sector, no estructura—, así que se traduce
aquí, 1:1 y en la misma fila. Detalle y reglas, en el bloque del 08, más abajo.
"""
import copy

import motor
from motor import get_column_letter as L

#: Los 10 ficheros de molde P4 de este kit son A:G; el calendario, A:F.
NCOL = 7

#: Relleno de la columna «Zona» por valor. El generador los pinta así en TODAS
#: las hojas del kit (medido: Admin FFF8E1, Producción FFF3E0, Transporte
#: E3F2FD, Limpieza EFEBE9, Montaje F3E5F5, Servicio E8F5E9, Desmontaje FCE4EC).
#: Se usa sólo como respaldo: `_zona` prefiere copiar el estilo de una fila real
#: de la misma hoja, que además trae bordes y fuente.
ZONA_COLOR = {
    'Admin': 'FFF8E1', 'Producción': 'FFF3E0', 'Transporte': 'E3F2FD',
    'Limpieza': 'EFEBE9', 'Montaje': 'F3E5F5', 'Servicio': 'E8F5E9',
    'Desmontaje': 'FCE4EC',
}


class AnclaPerdida(RuntimeError):
    """El texto que este módulo esperaba encontrar ya no está en la hoja."""


# ==========================================================================
# Utilidades de anclaje
# ==========================================================================
def _norm(v):
    """Texto comparable: la normalización de grados que este módulo aplica.

    Así el mismo ancla vale en la 1.ª pasada (texto original, «≤-18°C») y en la
    2.ª (texto ya normalizado, «≤ −18 °C»).
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
        raise AnclaPerdida(f'«{ws.title}»: no encuentro '
                           f'{L(col)}=«{texto}» (kit-tareas-catering)')
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


def _escribir_tarea(ws, fila, texto, zona):
    """Fila de tarea del molde P4: # (lo pone `_renumerar_p4`), Tarea y Zona.

    «Responsable» y «Hora» se dejan vacías a propósito: en este kit son celdas
    verdes que el cliente rellena, y ninguna de las 300 tareas del molde P4
    viene precargada.
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


def _renumerar_p4(ws):
    """Numeración del molde P4: reinicia en 1 en CADA sección.

    `motor.renumerar` no sirve: pasa por `motor.geometria`, que es del molde ▸ y
    devuelve None en estas hojas. Y renumerar de corrido rompería el molde: las
    cuatro secciones de «Event Manager» van 1-8, 1-9, 1-8, 1-7.
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
        cambios.append(f'«{ws.title}»: {n} temperaturas normalizadas al signo '
                       'menos tipográfico y con espacio antes de la unidad '
                       '(DOM-R2-22, que el motor no aplica al molde P4)')
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
# 01-apertura-cierre.xlsx — hoja «Producción» (producción off-site)
# ==========================================================================
#: DOM-12 + DOM-13 (equivalentes) — la hoja arrancaba la jornada de cocina en
#: «Recepción y control de mercancía»: nadie se lava las manos, nadie enciende
#: la campana y nadie mira la llave del gas antes de encender el horno y la
#: freidora que sí aparecen en el bloque D-1 (sous-vide, confitados) y en el día
#: D («hornear, grillar, freír»). El bloque va DELANTE de «Producción D-1», que
#: es la primera sección en la que se toca género; las tres primeras tareas de
#: la hoja son administrativas (ficha del evento, menú, compras) y no lo
#: necesitan. Orden interno: persona → campana → gas → fuego.
ARRANQUE = 'Higiene personal y arranque seguro de la cocina'
ARRANQUE_TAREAS = [
    ('Uniforme y calzado de trabajo limpios, delantal cambiado y pelo '
     'recogido (gorro o redecilla)', 'Producción'),
    ('Sin anillos, reloj ni pulseras; uñas cortas, limpias y sin esmalte',
     'Producción'),
    ('Heridas y cortes cubiertos con apósito impermeable de color visible y '
     'guante encima', 'Producción'),
    ('Lavado de manos al entrar y en cada cambio de tarea: jabón, agua '
     'caliente y papel de un solo uso', 'Producción'),
    ('Declarar síntomas digestivos o respiratorios: quien los tenga no '
     'manipula alimentos', 'Producción'),
    ('Encender la campana extractora y ventilar la cocina ANTES de encender '
     'nada más', 'Producción'),
    ('Si la cocina tiene gas: abrir la llave general y comprobar que NO huele '
     'a gas; si huele, no enciendas nada, ventila y avisa al mantenedor',
     'Producción'),
    ('Encender hornos, sous-vide, abatidor y freidora sólo después de la '
     'campana y del control del gas', 'Producción'),
]

#: DOM-02 (equivalente, ALTA) — el kit monta ceviches y tartares en las
#: estaciones de acción de 06 y porciona proteínas aquí, y en ninguno de los 11
#: ficheros había una sola línea sobre la congelación preventiva que exige el
#: Reglamento (CE) 853/2004 para pescado que se sirve crudo o semicrudo. En
#: catering el margen de reacción es cero: el comensal come en el venue, a
#: kilómetros de la cocina. La palabra ANISAKIS va en mayúsculas y completa a
#: propósito: es la que se busca con Ctrl+F y la que pregunta el inspector.
ANISAKIS_PRODUCCION = [
    ('Pescado que se servirá crudo o semicrudo (ceviche, tartar, marinados, '
     'ahumado en frío) — prevención de ANISAKIS: exigir al proveedor el '
     'certificado de congelación previa (≥24 h a −20 °C, o 15 h a −35 °C) o '
     'congelarlo tú, y anotar el lote', 'Producción'),
]

#: DOM-24 (equivalente) — «Verificar temperaturas de cámaras y producto
#: almacenado» no dice qué se verifica de la NOCHE, que es cuando fallan, ni
#: deja dónde anotar la lectura, ni qué hacer si no cuadra.
CAMARAS = ('Comprobar que las cámaras han funcionado toda la noche y '
           'registrar la temperatura (refrigeración 0-4 °C / congelación '
           '≤ −18 °C) — anota la lectura: ____ °C. Si hay desviación, no '
           'cargues el género hasta valorarlo')

#: DOM-29 (equivalente) — «Almacenar correctamente: refrigeración,
#: congelación, secos» no da ni un objetivo ni un plazo, en un kit que produce
#: a D-3 para varios eventos. Se le pone la temperatura y se le remite a la
#: tabla del pie.
ALMACENAR = ('Almacenar correctamente (refrigeración 0-4 °C, congelación '
             '≤ −18 °C, secos) y etiquetar con la fecha: la vida útil por '
             'familia está en la tabla del pie de esta hoja')

#: DOM-R2-09 — «(registrar en APPCC)» manda a un sitio que el cliente puede no
#: tener, y en el molde P4 no existe la columna «Notas» del representante… pero
#: sí la columna G «Notas» de este kit, así que la coletilla honesta puede
#: apuntar a la propia hoja.
PRE_TRANSPORTE = ('Control de temperatura antes de cargar — anota la lectura: '
                  '____ °C (si tienes el Pack APPCC, regístrala en su hoja de '
                  'temperaturas; si no, en la columna «Notas»)')

#: DOM-26 (equivalente) — «Preparar guarniciones y vegetales: lavar, cortar,
#: blanquear» mete en la misma línea lo que se blanquea (donde el calor resuelve)
#: y lo que se sirve crudo (crudités, ensaladas, brotes de la estación de
#: cocktail), que es lo único que necesita desinfección. Y sin el aclarado final
#: la lejía se sirve con la hoja.
VEGETALES = ('Preparar guarniciones y vegetales: lavar, cortar y blanquear. '
             'Los que se sirvan CRUDOS, desinfectar con lejía apta para uso '
             'alimentario según la dosis del fabricante (habitual: 70 ppm, '
             '5 min) y ACLARAR con agua potable abundante')

#: DOM-18 (equivalente) — el kit anota mermas en el post-evento del 03 (lo que
#: sobra del servicio), pero nunca la merma de PRODUCCIÓN, que es la que
#: desvía el escandallo del evento siguiente.
MERMAS = [
    ('Anotar las mermas de producción del día (producto, cantidad y motivo): '
     'es el dato que corrige el escandallo del próximo evento', 'Producción'),
]

TITULO_VIDA_UTIL = ('VIDA ÚTIL ORIENTATIVA EN CONGELACIÓN A −18 °C — ajústala '
                    'a tu producto y a tu proveedor')
VIDA_UTIL = [
    ('Carnes rojas y aves crudas, en pieza', '6-12 meses',
     'Porciona ANTES de congelar: descongelar y volver a congelar no se hace'),
    ('Carne picada y preparados de carne', '3 meses',
     'Más superficie expuesta: se enrancia y se oxida mucho antes que la '
     'pieza entera'),
    ('Pescado blanco y marisco crudo', '3-6 meses',
     'El tratamiento antianisakis (≥24 h a −20 °C) no sustituye a esta vida '
     'útil: se cuentan por separado'),
    ('Pescado azul (salmón, atún, boquerón)', '2-3 meses',
     'La grasa se enrancia aunque esté congelado: es el que antes se '
     'estropea'),
    ('Fondos, salsas, cremas y reducciones propias', '3 meses',
     'Etiqueta con la fecha de producción Y la de congelación: la vida útil '
     'se cuenta desde la de congelación'),
    ('Masas crudas, bases de tarta y hojaldre', '1-2 meses',
     'La levadura pierde fuerza: después sube mal aunque siga siendo seguro'),
    ('Pan y bollería ya horneados', '1-3 meses',
     'Pierde textura antes que seguridad; regenera en horno, nunca en '
     'microondas'),
    ('Canapés y bocados montados', '1 mes',
     'Sólo los que admiten congelación: con mayonesa, gelatina o nata montada '
     'NO se congelan'),
    ('Verdura blanqueada, purés y guarniciones', '8-12 meses',
     'Blanquea antes de congelar: sin blanquear pierde color y textura en '
     'pocas semanas'),
    ('Producto que ya ha salido a un servicio', 'No congelar',
     'Lo que ha estado expuesto en sala o ha roto la cadena de frío no vuelve '
     'al congelador: se retira'),
]


def _tabla_vida_util(ws, cambios):
    """Tabla editable de vida útil al pie de «Producción».

    Va DEBAJO de la fila de firma, es decir, por debajo del contador y fuera
    del rango que éste cuenta: es una referencia, no una tarea que marcar.
    """
    if _fila(ws, TITULO_VIDA_UTIL, 1) is not None:
        return False
    g = motor.geometria_p4(ws)
    if not g:
        raise AnclaPerdida('«Producción»: no es una hoja del molde P4')
    firma = None
    for r in range(g['contador'] or 1, ws.max_row + 1):
        v = ws.cell(row=r, column=1).value
        if isinstance(v, str) and v.startswith('Firma responsable'):
            firma = r
            break
    if firma is None:
        raise AnclaPerdida('«Producción»: no encuentro la fila de firma')
    banda = _exige(ws, 'Planificación previa (48-72h antes)', 1)
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
    cambios.append('«Producción»: tabla editable de vida útil en congelación '
                   f'({len(VIDA_UTIL)} familias) al pie, fuera del rango del '
                   'contador — DOM-29 (equivalente)')
    return True


def _f01(wb, cambios):
    tocado = False
    ws = wb['Producción']
    if _insertar_seccion(ws, 'Producción D-1 (día anterior)', ARRANQUE,
                         ARRANQUE_TAREAS):
        cambios.append(f'«Producción»: sección nueva «{ARRANQUE}» '
                       f'({len(ARRANQUE_TAREAS)} tareas) delante de la primera '
                       'sección que toca género: higiene personal y orden '
                       'seguro campana → gas → equipos, que no existían — '
                       'DOM-12 / DOM-13 (equivalentes)')
        tocado = True
    if _insertar_tras(ws, 'Cortar y porcionar proteínas según ficha técnica',
                      ANISAKIS_PRODUCCION):
        cambios.append('«Producción»: congelación preventiva frente al '
                       'ANISAKIS del pescado que se sirve crudo o semicrudo '
                       '(Rgto. CE 853/2004), que no estaba en ninguno de los '
                       '11 ficheros — DOM-02 (equivalente, ALTA)')
        tocado = True
    if _insertar_tras(ws, 'Verificar utensilios, menaje y material de '
                          'servicio empaquetado', MERMAS):
        cambios.append('«Producción»: mermas de producción del día — DOM-18 '
                       '(equivalente)')
        tocado = True
    if _sustituir(ws, 'Verificar temperaturas de cámaras y producto '
                      'almacenado', CAMARAS):
        cambios.append('«Producción»: las cámaras se COMPRUEBAN desde la noche '
                       'anterior, con objetivo, hueco para la lectura y qué '
                       'hacer si hay desviación — DOM-24 (equivalente)')
    if _sustituir(ws, 'Almacenar correctamente: refrigeración, congelación, '
                      'secos', ALMACENAR):
        cambios.append('«Producción»: el almacenamiento lleva temperatura, '
                       'fecha y remisión a la tabla de vida útil — DOM-29 '
                       '(equivalente)')
    if _sustituir(ws, 'Preparar guarniciones y vegetales: lavar, cortar, '
                      'blanquear', VEGETALES):
        cambios.append('«Producción»: desinfección con dosis y aclarado sólo '
                       'para los vegetales que se sirven crudos, separada del '
                       'blanqueado — DOM-26 (equivalente)')
    if _sustituir(ws, 'Control de temperatura pre-transporte (registrar en '
                      'APPCC)', PRE_TRANSPORTE):
        cambios.append('«Producción»: la referencia al APPCC deja de dar por '
                       'hecho que el cliente lo tiene y ofrece la columna '
                       '«Notas» como alternativa — DOM-R2-09')
    if _tabla_vida_util(ws, cambios):
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)
    if _instrucciones(wb, 'Seguridad y vida útil:', [
            'La primera sección de «Producción» es de higiene personal y de '
            'arranque seguro de la cocina: campana primero, comprobación del '
            'gas después y sólo entonces hornos, sous-vide y freidora.',
            'El pescado que se sirve crudo o semicrudo (ceviche, tartar, '
            'marinados, ahumado en frío) necesita congelación previa: ≥24 h a '
            '−20 °C o 15 h a −35 °C. Pide el certificado al proveedor y anota '
            'el lote.',
            'Al pie de la hoja tienes una tabla editable de vida útil en '
            'congelación por familia: ajústala a tu producto y a tu '
            'proveedor. Está fuera del contador porque es una referencia, no '
            'una tarea.']):
        cambios.append('Instrucciones: higiene y arranque seguro, anisakis y '
                       'tabla de vida útil — DOM-12 / DOM-02 / DOM-29')
        tocado = True
    return tocado


# ==========================================================================
# 02-partidas-cocina.xlsx — hoja «Transporte»
# ==========================================================================
#: La columna vertebral del catering es el vehículo, y su documentación no se
#: nombraba: el certificado de conformidad ATP es lo que autoriza a transportar
#: alimentos a temperatura regulada y es lo primero que pide una inspección en
#: carretera.
DOC_VEHICULO = ('Verificar combustible, documentación, seguro y certificado '
                'ATP en vigor del vehículo isotermo o frigorífico')

#: El hallazgo «temperaturas con signo no normalizado» de la verificación es
#: justamente esta celda. `_normalizar_grados` la dejaría en «≤−18 °C» —el signo
#: pegado al «≤», que es lo que produce `motor.RX_MENOS` cuando el original no
#: tenía espacio—, y en la misma hoja B15 diría «≤ −18 °C». Se escribe entera en
#: la forma canónica del motor (`motor.OBJ_CONG` = «≤ −18 °C») para que las dos
#: se lean igual.
PREENFRIAR = ('Pre-enfriar el vehículo a la temperatura objetivo (refrigerado '
              '≤ 5 °C / congelado ≤ −18 °C)')

#: «Registrar temperatura de cada GN/contenedor antes de cargar» no dice contra
#: qué se compara ni deja dónde apuntarla.
TEMP_CARGA = ('Registrar la temperatura de cada GN o contenedor antes de '
              'cargar (refrigerado 0-4 °C / congelado ≤ −18 °C) — anota la '
              'lectura: ____ °C')
TEMP_RUTA = ('Monitorizar la temperatura cada 30 min durante el trayecto — '
             'anota la lectura: ____ °C (si tienes el Pack APPCC, regístrala '
             'en su hoja de temperaturas; si no, en la columna «Notas»)')
TEMP_DESCARGA = ('Registrar la temperatura del producto al descargar — anota '
                 'la lectura: ____ °C (si tienes el Pack APPCC, regístrala en '
                 'su hoja de temperaturas; si no, en la columna «Notas»)')


def _f02(wb, cambios):
    ws = wb['Transporte']
    if _sustituir(ws, 'Pre-enfriar vehículo a temperatura objetivo (≤5°C '
                      'frío, ≤-18°C congelado)', PREENFRIAR):
        cambios.append('«Transporte»: la temperatura de pre-enfriado se '
                       'escribe con el signo menos tipográfico y en la misma '
                       'forma que el resto del corpus («≤ −18 °C»), que era el '
                       'hallazgo de temperaturas sin normalizar — DOM-R2-22')
    if _sustituir(ws, 'Verificar combustible, documentación y seguro del '
                      'vehículo', DOC_VEHICULO):
        cambios.append('«Transporte»: el certificado ATP del vehículo entra en '
                       'la comprobación previa a la carga (contenido de '
                       'sector: es la autorización para transportar alimentos '
                       'a temperatura regulada)')
    if _sustituir(ws, 'Registrar temperatura de cada GN/contenedor antes de '
                      'cargar', TEMP_CARGA):
        cambios.append('«Transporte»: la temperatura de carga lleva objetivo y '
                       'hueco para la lectura — §2.9')
    if _sustituir(ws, 'Monitorizar temperatura cada 30 min (registrar en hoja '
                      'APPCC)', TEMP_RUTA):
        cambios.append('«Transporte»: la referencia al APPCC deja de darse por '
                       'hecha y se ofrece la columna «Notas» — DOM-R2-09')
    if _sustituir(ws, 'Registrar temperatura de producto al descargar (APPCC)',
                  TEMP_DESCARGA):
        cambios.append('«Transporte»: ídem en la descarga, con hueco para la '
                       'lectura — DOM-R2-09 / §2.9')
    return False


# ==========================================================================
# 03-tareas-manager.xlsx — hoja «Event Manager» + hoja nueva legal
# ==========================================================================
#: DOM-17 (equivalente) — el registro horario es obligatorio en España desde el
#: RD-ley 8/2019 y hay que conservarlo 4 años. En catering es donde más se
#: incumple: el equipo del evento son extras que entran a montar a las 8 y
#: salen de desmontar a las 3 de la madrugada, y nadie firma nada.
JORNADA = [
    ('Cerrar y validar el registro de jornada de todo el equipo del evento, '
     'extras incluidos (montaje, servicio y desmontaje), y archivarlo con el '
     'del mes: hay que conservarlo 4 años', 'Admin'),
]

HOJA_LEGAL = 'Trimestral y Anual'
TITULO_LEGAL = 'Mantenimiento Trimestral y Anual — Revisiones Contratadas'
#: El kit no tenía NINGUNA capa de mantenimiento contratado: los 11 ficheros son
#: de evento (producción, transporte, montaje, servicio, desmontaje). Todo lo
#: que una inspección pide por escrito —DDD de la cocina central, conductos,
#: extintores, ATP del vehículo, póliza de eventos, carnés de manipulador— no
#: aparecía en ninguna parte. Se crea aquí, en el libro del director, y no en
#: el 05, que en ESTE kit es «Montaje y Desmontaje del Venue».
LEGAL = [
    ('Higiene y plagas — empresa autorizada', [
        ('Control de plagas (DDD) de la cocina central: visita de la empresa '
         'autorizada, parte firmado y certificado en vigor', 'Admin',
         'Trimestral'),
        ('Limpieza de campana y conductos de extracción por empresa '
         'homologada, con certificado', 'Admin', 'Anual'),
        ('Analítica de superficies y de producto en laboratorio externo '
         '(verificación del plan de higiene)', 'Producción', 'Semestral'),
        ('Revisar el plan APPCC y las fichas de proveedor: altas, bajas y '
         'cambios de menú del año', 'Admin', 'Anual'),
        ('Renovar los carnés de manipulador de alimentos del equipo fijo y '
         'archivar los de los extras habituales', 'Admin', 'Anual'),
        ('Comprobar que el registro sanitario (RGSEAA) recoge la actividad de '
         'catering y las cocinas que usas', 'Admin', 'Anual'),
    ]),
    ('Vehículos y cadena de frío', [
        ('Renovar el certificado de conformidad ATP del vehículo isotermo o '
         'frigorífico', 'Transporte', 'Anual'),
        ('Revisión del equipo de frío del vehículo por frigorista: gas, '
         'estanqueidad y termógrafo', 'Transporte', 'Semestral'),
        ('Calibrar termómetros y sondas contra un patrón conocido (agua con '
         'hielo, 0 °C) y anotar la desviación', 'Producción', 'Trimestral'),
        ('ITV del vehículo y revisión del extintor de a bordo', 'Transporte',
         'Anual'),
        ('Limpieza y desinfección a fondo del vehículo con registro firmado',
         'Transporte', 'Trimestral'),
    ]),
    ('Equipos, gas y residuos', [
        ('Revisión periódica de la instalación de gas por empresa habilitada, '
         'si la cocina tiene gas', 'Producción', 'Cada 5 años'),
        ('Revisión de cámaras, abatidor y hornos por el SAT: juntas, sondas y '
         'consumo', 'Producción', 'Anual'),
        ('Revisión de extintores y BIE de la cocina central por empresa '
         'mantenedora (etiqueta y acta)', 'Admin', 'Anual'),
        ('Retirada del aceite usado por gestor autorizado y archivo del '
         'documento de entrega', 'Producción', 'Trimestral'),
    ]),
    ('Documentación, seguros y facturación', [
        ('Revisar la póliza de responsabilidad civil de eventos: suma '
         'asegurada, aforos cubiertos y actividades excluidas', 'Admin',
         'Anual'),
        ('Revisar los contratos y las altas de personal eventual del '
         'trimestre y archivar los registros de jornada', 'Admin',
         'Trimestral'),
        ('Revisión del TPV y del software de facturación (requisitos '
         'antifraude / Verifactu)', 'Admin', 'Anual'),
        ('Actualizar precios de escandallo y tarifas de evento con los '
         'precios reales de proveedor', 'Admin', 'Trimestral'),
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
    """Crea «Trimestral y Anual» clonando «Event Manager» y ajustando bloques.

    Se clona en lugar de construirse a mano porque el clon trae anchos, alturas,
    bordes, combinaciones y la geometría exacta del molde P4; lo que NO trae
    (medido con openpyxl) son el desplegable, el pie de impresión y los paneles
    inmovilizados, y por eso se le aplican aquí uno a uno.
    """
    if HOJA_LEGAL in wb.sheetnames:
        return False
    modelo = wb['Event Manager']
    ws = wb.copy_worksheet(modelo)
    ws.title = HOJA_LEGAL
    ws.cell(row=1, column=1).value = TITULO_LEGAL
    g = motor.geometria_p4(ws)
    if not g:
        raise AnclaPerdida('«Event Manager»: el clon no es del molde P4')
    bloques = _bloques_p4(ws, g)
    if len(bloques) != len(LEGAL):
        raise AnclaPerdida(f'«Event Manager» tiene {len(bloques)} bloques y '
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
    cambios.append(f'hoja nueva «{HOJA_LEGAL}» en 03: mantenimiento y '
                   'documentación que se CONTRATA y que pide una inspección '
                   '(DDD, conductos, ATP del vehículo, calibración de sondas, '
                   'gas, extintores, aceite usado, RGSEAA, carnés de '
                   'manipulador, póliza de eventos y Verifactu) — DOM-16 '
                   '(equivalente); el kit no tenía ninguna capa anual')
    return True


def _f03(wb, cambios):
    tocado = False
    ws = wb['Event Manager']
    if _insertar_tras(ws, 'Reunión de retrospectiva con equipo (feedback y '
                          'mejoras)', JORNADA):
        cambios.append('«Event Manager»: cierre, validación y archivo del '
                       'registro de jornada del equipo del evento, extras '
                       'incluidos (RD-ley 8/2019, conservación 4 años) — '
                       'DOM-17 (equivalente)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)
    if _hoja_legal(wb, cambios):
        tocado = True
    if _instrucciones(wb, 'Más allá del evento:', [
            'La hoja «Trimestral y Anual» recoge lo que se CONTRATA y se pide '
            'por escrito en una inspección: DDD de la cocina central, '
            'conductos de extracción, extintores, instalación de gas, '
            'certificado ATP del vehículo, calibración de sondas, aceite '
            'usado, RGSEAA, carnés de manipulador, póliza de eventos y '
            'facturación.',
            'Anota en «Notas» el número de parte de cada revisión y la fecha '
            'de la siguiente; la columna «Cadencia» ya viene con la '
            'periodicidad legal o recomendada de cada una.',
            'En el post-evento se cierra y se valida el registro de jornada '
            'de todo el equipo, extras incluidos: montaje y desmontaje '
            'también son horas y hay que conservarlas 4 años.']):
        cambios.append('Instrucciones: hoja «Trimestral y Anual» y registro de '
                       'jornada — DOM-16 / DOM-17 (equivalentes)')
        tocado = True
    return tocado


# ==========================================================================
# 05-tareas-semanales-mensuales.xlsx — «Montaje» y «Desmontaje» del venue
# ==========================================================================
#: DOM-19 (equivalente) — la señalización decía «nombre y alérgenos» sin más. En
#: un buffet los 14 alérgenos declarados son obligación, y quien responde no es
#: el cartel sino el camarero al que le preguntan.
SENALIZACION = ('Colocar la señalización de cada plato con su nombre y los 14 '
                'alérgenos declarados, y comprobar que sala y cocina saben '
                'responder sin consultar')

#: DOM-18 (equivalente) — «Gestionar sobrantes: lo recuperable a contenedores,
#: lo descartable a basura» deja al criterio del que desmonta a las 3 de la
#: mañana qué es «recuperable». Lo que decide no es el aspecto: es si ha salido
#: a sala y si ha mantenido la cadena de frío.
SOBRANTES = ('Gestionar los sobrantes: lo que NO ha salido a sala y ha '
             'mantenido la cadena de frío, a contenedor limpio, etiquetado, '
             'fechado y refrigerado; lo que ha estado expuesto, a residuo. '
             'Anotar la merma del evento')


def _f05(wb, cambios):
    ws = wb['Montaje']
    if _sustituir(ws, 'Colocar señalización de platos con nombre y alérgenos',
                  SENALIZACION):
        cambios.append('«Montaje»: la señalización nombra los 14 alérgenos '
                       'declarados y exige que sala y cocina sepan '
                       'responderlos — DOM-19 (equivalente)')
    ws = wb['Desmontaje']
    if _sustituir(ws, 'Gestionar sobrantes: lo recuperable a contenedores, lo '
                      'descartable a basura', SOBRANTES):
        cambios.append('«Desmontaje»: el criterio de los sobrantes deja de ser '
                       '«lo recuperable» y pasa a ser si ha salido a sala y si '
                       'ha mantenido la cadena de frío; se anota la merma — '
                       'DOM-18 (equivalente)')
    return False


# ==========================================================================
# 06-eventos-festivos.xlsx — checklists por tipo de evento
# ==========================================================================
#: DOM-19 (equivalente) — en una boda el alérgeno no basta con conocerlo: hay
#: que saber en qué SILLA se sienta, porque el plato alternativo sale con el
#: pase y el camarero tiene que llevarlo a un sitio concreto.
ALERGENOS_BODA = [
    ('Recoger POR ESCRITO alérgenos e intolerancias de cada comensal y '
     'situarlos en el plano de asientos; cerrar con cocina los platos '
     'alternativos y quién los sirve', 'Admin'),
]

#: DOM-02 (equivalente, ALTA) — «Preparar estaciones de acción: ceviche,
#: tartar, wok» servidas al momento y sin cocción posterior era el hallazgo de
#: contenido más grave del kit.
ANISAKIS_COCKTAIL = [
    ('Ceviche, tartar y cualquier pescado que se sirva crudo o semicrudo — '
     'prevención de ANISAKIS: usar sólo pescado con congelación previa '
     'acreditada (≥24 h a −20 °C, o 15 h a −35 °C) y anotar el lote',
     'Producción'),
    ('Cada camarero debe saber los alérgenos de la bandeja que pasa: ficha de '
     'alérgenos por bandeja y repaso en el briefing', 'Servicio'),
]

ALERGENOS_CORP = ('Confirmar POR ESCRITO alérgenos, intolerancias y dietas '
                  'especiales de los asistentes, y pasarlos a cocina y a sala')

#: En exterior la regla de las 2 horas se acorta: es el error clásico del
#: catering de verano y la tarea no daba ninguna cifra.
EXPOSICION = ('Duplicar los controles de temperatura: al aire libre los '
              'alimentos se calientan mucho más rápido. Máximo 2 h entre 5 °C '
              'y 65 °C, y con más de 30 °C de ambiente, 1 h')


def _f06(wb, cambios):
    tocado = False
    ws = wb['Bodas']
    if _insertar_tras(ws, 'Verificar menú infantil y nº de niños',
                      ALERGENOS_BODA):
        cambios.append('«Bodas»: alérgenos e intolerancias por escrito y '
                       'situados en el plano de asientos al confirmar la '
                       'reserva — DOM-19 (equivalente)')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)

    ws = wb['Cocktail Standing']
    if _insertar_tras(ws, 'Preparar estaciones de acción: ceviche, tartar, '
                          'wok', ANISAKIS_COCKTAIL):
        cambios.append('«Cocktail Standing»: prevención de ANISAKIS en las '
                       'estaciones de ceviche y tartar (Rgto. CE 853/2004) y '
                       'alérgenos por bandeja — DOM-02 (equivalente, ALTA) / '
                       'DOM-19')
        tocado = True
    _renumerar_p4(ws)
    _dv_extender(ws)

    ws = wb['Corporativo']
    if _sustituir(ws, 'Confirmar restricciones dietéticas de asistentes',
                  ALERGENOS_CORP):
        cambios.append('«Corporativo»: las restricciones se confirman POR '
                       'ESCRITO y se pasan a cocina y a sala — DOM-19 '
                       '(equivalente)')

    ws = wb['Outdoor - Exterior']
    if _sustituir(ws, 'Duplicar controles de temperatura (alimentos se '
                      'calientan más rápido)', EXPOSICION):
        cambios.append('«Outdoor - Exterior»: la regla de las 2 h entre 5 °C y '
                       '65 °C, y 1 h con más de 30 °C de ambiente, en cifras '
                       '— §2.9 (equivalente)')
    return tocado


# ==========================================================================
# BONUS-02 — calendario anual de temporada alta
# ==========================================================================
#: El calendario de catering es el ÚNICO fichero del kit que el motor no ve:
#: `motor.fila_calendario` exige la pareja «Antelación» + una columna de EVENTO,
#: y esta cabecera es «Fecha / Período | Tipo». Se quedaba sin bio y con la
#: versión 1.1 mientras los otros diez ficheros pasaban a 2.0. Aquí se le pone
#: la autoría con la misma función del motor (§2.6); la detección en sí es un
#: hueco del motor y va anotada para el orquestador.
#:
#: DOM-20 (equivalente) — de las cinco fechas del representante, tres ya están
#: cubiertas por este calendario con su vocabulario propio (comuniones en marzo
#: y mayo, el 15 de agosto dentro de «Julio-Agosto — Bodas de verano», el 1 de
#: noviembre dentro de «Todo el año — Funerales / Tanatorio»). Faltaban las dos
#: que no tienen equivalente: el Día del Padre y el puente de diciembre, que en
#: catering es un bloque de tres días con bodas de invierno y cenas de empresa
#: adelantadas.
FECHAS = [
    ('Marzo — Comuniones (inicio)',
     ('19 Mar — Día del Padre', 'Festividad',
      'Comidas familiares de mediodía y detalles de empresa; menús cerrados y '
      'tartas por encargo', '3 semanas')),
    ('Noviembre — Black Friday gastro',
     ('6-8 Dic — Puente de la Constitución', 'Mixto',
      'Tres días seguidos de eventos: bodas de invierno, cenas de empresa '
      'adelantadas y comidas familiares. Cerrar personal eventual y stock '
      'ANTES del puente', '4 semanas')),
]


def _bonus02(wb, cambios):
    ws = wb['Calendario']
    tocado = False
    nuevas = 0
    for ancla, (fecha, tipo, prep, antelacion) in FECHAS:
        if _fila(ws, fecha) is not None:
            continue
        r = _exige(ws, ancla)
        est = _estilos(ws, r, ncol=6)
        motor.insertar_filas(ws, r + 1, 1)
        _pintar(ws, r + 1, est)
        for c, v in enumerate((0, fecha, tipo, prep, antelacion), start=1):
            ws.cell(row=r + 1, column=c).value = v
        nuevas += 1
        tocado = True
    total = 0
    for r in range(1, ws.max_row + 1):
        if isinstance(ws.cell(row=r, column=1).value, int):
            total += 1
            ws.cell(row=r, column=1).value = total
    if nuevas:
        cambios.append(f'«Calendario»: {nuevas} fechas que faltaban (Día del '
                       'Padre y puente de diciembre; las otras tres del '
                       'representante ya estaban cubiertas con vocabulario de '
                       'catering) — DOM-20 (equivalente)')
    # El rótulo y las Instrucciones prometen un número concreto de fechas: si
    # no se actualiza, el fichero se contradice a sí mismo en la primera línea.
    sub = ws.cell(row=2, column=1)
    nuevo = (f'AI Chef Pro · aichef.pro — {total} fechas clave para '
             'planificar tu año')
    if isinstance(sub.value, str) and sub.value != nuevo:
        sub.value = nuevo
        cambios.append(f'«Calendario»: el subtítulo dice {total} fechas, que '
                       'son las que hay')
    if 'Instrucciones' in wb.sheetnames:
        wsi = wb['Instrucciones']
        linea = (f'▸ Las {total} fechas clave del año para empresas de '
                 'catering.')
        for r in range(1, wsi.max_row + 1):
            v = wsi.cell(row=r, column=2).value
            if isinstance(v, str) and v.startswith('▸ Las ') and \
                    v.endswith('fechas clave del año para empresas de '
                               'catering.'):
                if v != linea:
                    wsi.cell(row=r, column=2).value = linea
                    cambios.append('Instrucciones: el recuento de fechas '
                                   f'pasa a {total}')
                break
    antes = len(cambios)
    motor.bio_en_instrucciones(wb, cambios)
    if len(cambios) > antes:
        cambios.append('BONUS-02: la bio y la versión 2.0 las pone este '
                       'módulo porque `motor.fila_calendario` no reconoce la '
                       'cabecera «Fecha / Período | Tipo» de catering — hueco '
                       'del motor, anotado para el orquestador')
    return tocado


# ==========================================================================
# 08-apertura-cierre-negocio.xlsx — el único fichero de molde «▸» de este
# módulo: vocabulario del OFICIO
# ==========================================================================
#: El 08 y el 09 son los dos únicos ficheros de este kit que el motor reconoce
#: como molde «▸», y su contenido viene del generador v1.1 GENÉRICO de los 12
#: kits: una lista pensada para un restaurante con sala abierta al público.
#: `kit-tareas-catering-ver3.json` §7 lo censó como hallazgo BAJO —«pizarra de
#: menú», «sistema de reservas», «música ambiente», «cartas/menús»— en una
#: empresa que produce off-site y a la que no entra un comensal por la puerta.
#: Aquí se traduce al oficio, tarea a tarea y EN LA MISMA FILA.
#:
#: Tres cosas condicionan este bloque y no se pueden perder de vista:
#:
#:  · **Es 1:1 y sólo de texto.** Ni una fila nueva, ni una borrada: el
#:    recuento del kit (346 tareas, `gates.recuento_tareas`, que desde T-03 es
#:    la fuente de la landing) tiene que salir idéntico antes y después.
#:  · **Las columnas D («Responsable») y E («Hora Límite» / «Cuándo») NO se
#:    tocan.** Las precarga `motor.precargar_negocio` POR ÍNDICE de fila, no
#:    por el texto de la tarea, así que reescribir la B no mueve una sola hora
#:    (comprobado leyendo la función: `resp`/`hora` salen de `i`, no de la
#:    celda). Escribir ahí desde aquí, en cambio, rompería el gate
#:    `negocio_precargado`.
#:  · **El texto se escribe en su FORMA ESTABLE.** A diferencia del molde P4,
#:    aquí `motor.textos_de_tarea` sí corre —y corre ANTES que este módulo, en
#:    `aplicar`—, así que en la 2.ª pasada volvería a leer lo que se escriba
#:    aquí. `_reescribir` lo pasa por `motor.forma_estable` (grados, Pack APPCC
#:    y §2.9), que es idempotente: si el texto ya está en su forma final, no
#:    encuentra nada que cambiar y la idempotencia se mantiene en 0.
#:
#: La columna C («Zona») sí se ajusta cuando la zona heredada nombra un sitio
#: que este negocio no tiene («Sala», «Terraza»). No la usa ningún gate ni
#: ninguna fórmula —T-04 descartó a propósito la columna «Zona» como fuente de
#: los paréntesis de «Se conecta con» justamente porque es la misma en los 12
#: kits— y en el molde «▸» va en verde y desbloqueada, es decir, es una celda
#: que el cliente edita. Las zonas nuevas son todas zonas que ya existen en la
#: propia hoja (Logística, Almacén, Oficina, Exterior): no se inventa ninguna.
#:
#: Lo que NO se toca: B10 («Encender TPV / POS / datáfono»), que es el hito de
#: T-02 y el gate `tpv_duplicado` cuenta; y las Instrucciones del 08 y del 09,
#: que las reescribe `motor.reescribir_instrucciones` en cada pasada (meter
#: aquí una línea sería una diferencia nueva en cada pasada).

#: Carga de isotermos: el texto se compone con `motor.LECTURA` para que el
#: hueco de la lectura sea EXACTAMENTE el mismo literal del resto del corpus.
#: El detalle (pre-enfriado, temperatura por GN, ruta y descarga) vive en la
#: hoja «Transporte» de 02, y la frase de T-08 que el propio fichero imprime
#: admite ese solape: «una es el hito y la otra el detalle».
CARGA_ISOTERMOS = (
    'Cargar los isotermos de los eventos que salen primero y registrar la '
    'temperatura de salida' + motor.LECTURA +
    ' (el detalle de la carga va en la hoja «Transporte» de '
    '02-partidas-cocina.xlsx)')

#: (viejo, nuevo, zona nueva o None para dejar la que tiene)
NEGOCIO_APERTURA = [
    ('Desactivar alarma del local',
     'Desactivar la alarma y abrir el obrador, el almacén de material y el '
     'muelle de carga', None),
    ('Montar señalización exterior / pizarra de menú',
     CARGA_ISOTERMOS, None),
    ('Encender sistema de reservas / tablet de pedidos',
     'Entregar a cada conductor la hoja de ruta de su vehículo: eventos, '
     'direcciones, horas de entrega y teléfono de contacto', 'Logística'),
    ('Poner música ambiente al volumen adecuado',
     'Imprimir las órdenes de servicio del día y repartirlas: una para '
     'producción, una para transporte y una para el responsable de cada '
     'evento', 'Oficina'),
    ('Revisar reservas del día y eventos especiales',
     'Confirmar con cada cliente el número definitivo de comensales y los '
     'cambios de última hora', None),
    ('Comprobar baños: papel, jabón, limpieza, ambientador',
     'Comprobar aseos y vestuario del personal: papel, jabón, papel de manos '
     'y limpieza', None),
    ('Revisar estado del mobiliario (sillas, mesas, iluminación)',
     'Revisar el mobiliario y la mantelería que salen hoy (mesas, sillas y '
     'tableros) y apartar lo dañado', 'Almacén'),
    ('Montar terraza si aplica (mesas, sillas, sombrillas/estufas)',
     'Preparar el material de exterior si hay evento al aire libre: carpas, '
     'sombrillas, estufas y lastres', 'Exterior'),
    ('Comprobar que las cartas/menús están en orden',
     'Confirmar con cada recinto el acceso y el horario de montaje: muelle, '
     'ascensor, permisos y persona de contacto', 'Oficina'),
    ('Encender displays / pantallas informativas si las hay',
     'Briefing con el equipo del día: eventos, horas críticas, alérgenos y '
     'quién va en cada servicio (el guion completo está en '
     'BONUS-01-briefing-servicio.xlsx)', None),
]

NEGOCIO_CIERRE = [
    ('Apagar música ambiente',
     'Apagar los equipos del obrador que no queden en marcha (hornos, '
     'freidora, campana) y dejar cámaras y abatidor encendidos', None),
    ('Verificar que no quedan clientes en el local',
     'Verificar que no queda personal ni visitas en el obrador antes de '
     'cerrar', 'General'),
    ('Limpiar y recoger terraza si aplica',
     'Recoger y guardar el material de exterior que haya vuelto (carpas, '
     'sombrillas y estufas)', 'Exterior'),
    ('Recoger señalización exterior',
     'Despejar y baldear el muelle de carga: sin carros, sin palés y sin '
     'residuos', None),
]


def _reescribir(ws, viejo, nuevo, zona=None):
    """Sustitución 1:1 en la columna «Tarea» del molde «▸». Devuelve la fila
    si ha cambiado algo, o None si ya estaba como debe.

    `motor.forma_estable` deja el texto tal y como lo dejaría el motor: es la
    garantía de que la 2.ª pasada no encuentre nada que reescribir.
    """
    nuevo = motor.forma_estable(nuevo)
    cambiada = _sustituir(ws, viejo, nuevo) is not None
    fila = _exige(ws, nuevo)
    if zona is not None:
        cel = ws.cell(row=fila, column=3)
        if cel.value != zona:
            cel.value = zona
            cambiada = True
    return fila if cambiada else None


def _f08(wb, cambios):
    """Devuelve SIEMPRE False: no cambia la estructura del libro.

    Si devolviera True, `main.py` volvería a pasar el motor entero sobre un
    libro cuya geometría es la misma — trabajo inútil y una oportunidad más de
    que algo se mueva.
    """
    for hoja, filas in (('Apertura del Negocio', NEGOCIO_APERTURA),
                        ('Cierre del Negocio', NEGOCIO_CIERRE)):
        ws = wb[hoja]
        tocadas = [_reescribir(ws, viejo, nuevo, zona)
                   for viejo, nuevo, zona in filas]
        tocadas = [r for r in tocadas if r]
        # R3-d, la misma lección que documenta `motor.autoaltos`: la pasada de
        # alturas va DESPUÉS del último cambio de texto. `aplicar` ya la hizo,
        # pero midiendo el texto VIEJO (corto): 10 de estas tareas son más
        # largas y con altura fija de 24 pt se imprimirían recortadas por el
        # final. Sin esto, la 1.ª pasada dejaba 24 y la 2.ª —que ya lee el
        # texto nuevo— lo ponía en `None`: 12 diferencias de idempotencia sin
        # nada roto. `autoalto` sólo QUITA la altura fija, nunca la repone, así
        # que repetirlo no mueve nada.
        motor.autoaltos(ws, cambios)
        if tocadas:
            cambios.append(
                '«%s»: %d tareas reescritas del vocabulario de restaurante '
                'con sala (pizarra de menú, reservas, música ambiente, '
                'cartas/menús, terraza) al oficio del catering —órdenes de '
                'servicio, hoja de ruta de vehículos, carga de isotermos con '
                'temperatura de salida, material por evento y accesos del '
                'recinto— en las filas %s; D y E (Responsable y Hora) '
                'intactas — ver3 §7'
                % (ws.title, len(tocadas),
                   ', '.join('B' + str(r) for r in tocadas)))
    return False


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

#: Ficheros del molde P4 a los que sólo hay que aplicarles la normalización
#: transversal de grados (no tienen cambios de contenido propios).
SOLO_GRADOS = ('04-tareas-perfiles.xlsx', '07-plantilla-personalizable.xlsx',
               'BONUS-01-briefing-servicio.xlsx')

#: Ficheros de molde «▸» con contenido propio. Van por una rama APARTE porque
#: la cola de `post()` es del molde P4 y aquí haría daño: `motor.REGISTRO.clear()`
#: borraría las fórmulas que acaba de registrar `motor.aplicar` (el gate de
#: cache dejaría de comprobarlas) y `motor.normalizar_p4` no tiene nada que
#: hacer en un libro que ya pasó por el molde ▸ y que aún tiene por delante
#: `motor.cerrar`.
FICHEROS_FLECHA = {
    '08-apertura-cierre-negocio.xlsx': _f08,
}


def post(wb, fname, cambios):
    """CONTENIDO sobre un libro ya normalizado por `motor.aplicar`.

    Devuelve True si ha cambiado la ESTRUCTURA. En el molde P4 ese valor no lo
    usa `main.py` (no hay 2.ª pasada del motor porque `aplicar` devolvió `{}`),
    así que la reconstrucción del contador, del formato condicional y del
    desplegable se hace AQUÍ antes de salir.
    """
    flecha = FICHEROS_FLECHA.get(fname)
    if flecha is not None:
        return flecha(wb, cambios)
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
    # las de la geometría VIEJA: al insertar una tarea en «Event Manager» el
    # contador bajó de la fila 47 a la 48 y `main.py` seguía preguntando por el
    # cache de E47 —una celda que ahora es una tarea— y lo declaraba «fórmula
    # sin valor». Tres falsos fallos así tumbaban el dry-run con el fichero
    # perfectamente cacheado (inject_cache 4/4). Lo único que hay en el
    # registro de un fichero P4 son los contadores, y `normalizar_p4` los
    # vuelve a registrar todos con su coordenada actual.
    motor.REGISTRO.clear()
    motor.normalizar_p4(wb, cambios)
    return tocado
