#!/usr/bin/env python3
"""
contenido_kit_tareas_sushi_bar.py — CONTENIDO propio de «kit-tareas-sushi-bar»,
REPRESENTANTE de la sub-familia ChefBusiness (§2.1 de
`kit-tareas-cb-v2-SPEC.md`, tanda T2.2 de §9).

Fuente de los cambios: `auditorias/kit-tareas-sushi-bar-R1.json` (76 hallazgos:
DOM 31 · TEC 20 · COM 25) y `auditorias/kit-tareas-cb-v2-censo.json` (censo
transversal T0.1). Aquí van los **39 ids de CONTENIDO** del mapa §8 y las **8
hojas NUEVAS** de §2.1. Lo que es del MOTOR (tildes CB-E1, contador de la
plantilla CB-E2, formatos de registro CB-E3, «Cómo personalizar» por tipo
CB-E4, legibilidad CB-E9) NO se toca desde aquí.

Contrato con `main.py` (idéntico al de los hermanos ▸ ya en producción):
    post(wb, fname, cambios) -> bool
`True` = «he cambiado la ESTRUCTURA del libro» (filas u hojas nuevas) y hace
que `main.py` vuelva a pasar `motor.aplicar` antes de `motor.cerrar`: es lo que
mete las filas nuevas en el rango del contador, en la DV y en el CF, y lo que
convierte una hoja recién creada en una hoja de la familia (desplegable,
contador, formatos de registro, A4, protección y pie).

Además exporta tres tablas que `main.py` lee con `getattr` y que sólo existen
para este kit (así los otros diez kits LIVE de la familia no ven gates nuevos):
  · `PROMESAS`       → gate `promesas`      (§1.3): término de la landing ↔ corpus
  · `EQUIPOS_LIMITE` → gate `limite_unico`  (§1.3): un solo rango por equipo
  · `PLANTILLA_09`   → demostración CB-E2 «8 tareas escritas → x de 8»

ANCLAS NORMALIZADAS, NO NÚMEROS DE FILA. Este módulo corre DESPUÉS de
`motor.aplicar` y ANTES de `motor.ortografia`, así que el texto que ve todavía
NO tiene tildes pero SÍ tiene los grados normalizados (`−20 °C` con U+2212) y
las coletillas que el motor añade (`— anota la lectura: ____ °C`,
`(si tienes el Pack APPCC, …)`). Por eso `_clave()` compara sin tildes, sin
mayúsculas y con los grados ya normalizados, y los anclajes de tarea van por
PREFIJO. Si un ancla no aparece se levanta `AnclaPerdida`: mejor caerse que
publicar medio kit.

IDEMPOTENCIA: cada operación mira primero si su resultado ya está en el libro,
y todo texto que se escribe pasa por `motor.forma_estable` (o por
`_est_texto`), que es el punto fijo de las cuatro reescrituras del motor. Sin
eso la 2.ª pasada volvería a añadir la coletilla y el gate se pondría rojo.

DOS PARCHES A LAS TABLAS DEL MOTOR, al importar (mismo patrón que el
`motor.EDITABLES.add(...)` de cafetería):
  · `motor.SUST_APPCC` recibe dos reglas IDENTIDAD. `texto_appcc` cuelga
    «(si tienes el Pack APPCC, regístralo allí; …)» de TODA celda que diga
    APPCC, y en este kit eso alcanzaba al TÍTULO del fichero
    (`03:Instrucciones!B2`) y a la línea de firma
    (`03:'Registro Congelación'!B29`), donde la coletilla no significa nada.
    Medido en el dry-run del 2026-08-29.
  · `motor.EDITABLES` recibe los rótulos de las columnas nuevas que el cliente
    tiene que poder escribir en las hojas de checklist nuevas.

NORMATIVA — la lista blanca de §2.0 está DESACTUALIZADA en un punto y aquí se
sigue la vigente, que es además la que ya exige el gate del motor
(`motor.PROHIBIDAS`) y la que la landing ya publica: el **RD 1420/2006 quedó
derogado el 22-dic-2022** por la disposición derogatoria única.h) del
**RD 1021/2022**, cuyo **art. 8.1** es hoy el que obliga a la congelación
antiparasitaria. Citar el 1420/2006 como norma viva pone el dry-run en rojo.
"""
import copy
import re
import unicodedata

import motor
from motor import get_column_letter as L

NCOL = 7                     # los 11 ficheros del kit son A:G


class AnclaPerdida(RuntimeError):
    """El texto que este módulo esperaba encontrar ya no está en la hoja."""


# ==========================================================================
# Parches a las tablas del motor (se aplican al IMPORTAR el módulo, que
# `main.py` hace antes de `motor.contexto` y del bucle de proceso)
# ==========================================================================
TITULO_03 = 'Seguridad Alimentaria, Anisakis y APPCC — Sushi Bar'
FIRMA_03 = 'Responsable del plan APPCC: _________________    Firma: _________'

for _rx, _bueno in (
        (re.compile(r'^Seguridad Alimentaria, Anisakis y APPCC — Sushi Bar$'),
         TITULO_03),
        (re.compile(r'^Responsable del plan APPCC: _+\s+Firma: _+$'), FIRMA_03),
        (re.compile(r'^Responsable APPCC: _+\s+Firma: _+$'), FIRMA_03)):
    if not any(r.pattern == _rx.pattern for r, _ in motor.SUST_APPCC):
        motor.SUST_APPCC.append((_rx, _bueno))

# Columnas nuevas de las hojas de checklist nuevas que el cliente rellena.
motor.EDITABLES.update({'Cuándo', 'Nº de lote'})


# ==========================================================================
# Utilidades de anclaje
# ==========================================================================
def _clave(v):
    """Texto comparable: grados normalizados, sin tildes ni ñ, en minúsculas.

    El módulo corre ANTES de `motor.ortografia`, así que la hoja todavía dice
    «Verificar temperatura camara pescado crudo…» mientras el fichero que se
    entrega dirá «cámara». Comparar la cadena cruda dejaría el módulo inútil en
    cuanto el barrido de tildes cambie una letra.
    """
    if not isinstance(v, str):
        return v
    v = motor.texto_grados(v)
    v = unicodedata.normalize('NFD', v)
    v = ''.join(c for c in v if unicodedata.category(c) != 'Mn')
    return ' '.join(v.split()).lower()


def _fila(ws, texto, col=1):
    """Fila cuya celda `col` EMPIEZA por `texto` (clave normalizada), o None.

    Prefijo y no igualdad porque `motor.texto_temperatura` y
    `motor.texto_appcc` le cuelgan una cola a la tarea original: la celda que
    en `dl/` decía «Verificar temperatura camara pescado crudo (-2 a 0°C)» ya
    dice «… (−2 a 0 °C) — anota la lectura: ____ °C».
    """
    k = _clave(texto)
    if not k:
        return None
    for r in range(1, ws.max_row + 1):
        v = _clave(ws.cell(row=r, column=col).value)
        if isinstance(v, str) and v.startswith(k):
            return r
    return None


def _exige(ws, texto, col=1):
    r = _fila(ws, texto, col)
    if r is None:
        raise AnclaPerdida(f'«{ws.title}»: no encuentro {L(col)} que empiece '
                           f'por «{texto}» (kit-tareas-sushi-bar)')
    return r


def _est_texto(v):
    """Punto fijo de las reescrituras que el motor aplica a CUALQUIER celda."""
    return motor.texto_grados(motor.texto_appcc(motor.texto_facturado(v)))


def _est_tarea(v):
    """Punto fijo de las reescrituras del motor en la columna «Tarea»."""
    return motor.forma_estable(v)


def _estilos(ws, fila, ncol=NCOL):
    return [copy.copy(ws.cell(row=fila, column=c)._style)
            for c in range(1, ncol + 1)]


def _pintar(ws, fila, estilos):
    for c, st in enumerate(estilos, start=1):
        ws.cell(row=fila, column=c)._style = copy.copy(st)


def _escribir_tarea(ws, fila, tarea):
    """(texto, zona, responsable, cuándo) en una fila de tarea."""
    ws.cell(row=fila, column=1).value = 0        # renumerar() pone el ordinal
    ws.cell(row=fila, column=2).value = _est_tarea(tarea[0])
    for c, v in enumerate(tarea[1:], start=3):
        ws.cell(row=fila, column=c).value = v


def _sustituir(ws, viejo, nuevo, col=2, tarea=True):
    """Sustitución 1:1 por prefijo. Devuelve la fila, o None si ya estaba."""
    nuevo = _est_tarea(nuevo) if tarea else _est_texto(nuevo)
    if _fila(ws, nuevo, col) is not None:
        return None
    r = _exige(ws, viejo, col)
    ws.cell(row=r, column=col).value = nuevo
    return r


def _poner(ws, fila, col, valor):
    ws.cell(row=fila, column=col).value = valor


def _insertar_tras(ws, ancla, tareas, col=2):
    """Inserta `tareas` justo debajo de la fila cuya col B empieza por `ancla`."""
    if _fila(ws, _est_tarea(tareas[0][0]), 2) is not None:
        return False                                   # ya insertadas
    r = _exige(ws, ancla, col)
    est = _estilos(ws, r)
    motor.insertar_filas(ws, r + 1, len(tareas))
    for i, t in enumerate(tareas):
        _pintar(ws, r + 1 + i, est)
        _escribir_tarea(ws, r + 1 + i, t)
    return True


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


def _insertar_bloque(ws, antes_de, titulo, tareas, separadora=True):
    """Bloque nuevo (banda + tareas) delante de otra banda.

    Este kit SÍ deja una fila en blanco entre bloques (medido en
    `01:'Apertura Barra Sushi'`: bandas en A5, A12, A20 y A31 con la fila
    anterior vacía), al revés que cafetería.
    """
    if _fila(ws, titulo) is not None:
        return False
    idx = _exige(ws, antes_de)
    est_banda = _estilos(ws, idx)
    est_tarea = _estilos(ws, idx + 1)
    n = len(tareas) + 1 + (1 if separadora else 0)
    motor.insertar_filas(ws, idx, n)
    fila = idx + (1 if separadora else 0)
    _pintar(ws, fila, est_banda)
    ws.cell(row=fila, column=1).value = titulo
    motor._merge(ws, f'A{fila}:{L(NCOL)}{fila}')
    for i, t in enumerate(tareas):
        _pintar(ws, fila + 1 + i, est_tarea)
        _escribir_tarea(ws, fila + 1 + i, t)
    return True


def _bloque_al_final(ws, titulo, tareas):
    """Bloque nuevo pegado DESPUÉS del último bloque de la tabla.

    Se ancla en la fila del contador (o en «Verificado por:») y deja el bloque
    DENTRO del rango: `normalizar_checklist` de la 2.ª pasada lo mete en el
    COUNTIF y le repone sus 5 filas libres detrás.
    """
    if _fila(ws, titulo) is not None:
        return False
    g = motor.geometria(ws)
    if not g:
        raise AnclaPerdida(f'«{ws.title}»: no es un checklist de la familia')
    idx = g['contador'] or (ws.max_row + 1)
    est_banda = _estilos(ws, _exige(ws, '  ', 1) if False else g['hr'] + 1)
    # El estilo de banda se toma de la PRIMERA banda de la hoja, que siempre
    # existe en este kit (todas las hojas de checklist arrancan con una).
    primera = None
    for r in range(g['hr'] + 1, idx):
        if motor.es_fila_seccion(ws, r):
            primera = r
            break
    if primera is None:
        raise AnclaPerdida(f'«{ws.title}»: no encuentro ninguna banda de '
                           'sección de la que copiar el estilo')
    est_banda = _estilos(ws, primera)
    est_tarea = _estilos(ws, primera + 1)
    motor.insertar_filas(ws, idx, len(tareas) + 2)
    fila = idx + 1
    _pintar(ws, fila, est_banda)
    ws.cell(row=fila, column=1).value = titulo
    motor._merge(ws, f'A{fila}:{L(NCOL)}{fila}')
    for i, t in enumerate(tareas):
        _pintar(ws, fila + 1 + i, est_tarea)
        _escribir_tarea(ws, fila + 1 + i, t)
    return True


def _instrucciones(wb, encabezado, lineas):
    """Añade un bloque al final de la hoja «Instrucciones».

    `motor.reescribir_instrucciones` (que corre después, en `cerrar`) relee la
    hoja línea a línea y la vuelve a emitir en el molde ▸. El encabezado no
    puede estar en `motor.MIS_BLOQUES` o lo descartaría por ser suyo, y las
    líneas no pueden casar con `motor.RX_OBSOLETO` o las borraría.
    """
    if 'Instrucciones' not in wb.sheetnames:
        return False
    ws = wb['Instrucciones']
    col = 2 if any(isinstance(ws.cell(row=r, column=2).value, str)
                   for r in range(1, min(ws.max_row, 12) + 1)) else 1
    for r in range(1, ws.max_row + 1):
        if ws.cell(row=r, column=col).value == encabezado:
            return False                               # ya está
    for txt in lineas:
        if motor.RX_OBSOLETO.search(txt):
            raise AnclaPerdida(f'la línea «{txt[:50]}…» del bloque '
                               f'«{encabezado}» casa con RX_OBSOLETO y el '
                               'motor la borraría al reescribir')
    fila = ws.max_row + 2
    ws.cell(row=fila, column=col).value = encabezado
    for i, txt in enumerate(lineas, start=1):
        ws.cell(row=fila + i, column=col).value = '▸ ' + _est_texto(txt)
    return True


# ==========================================================================
# Constructor genérico de HOJA DE REGISTRO (§7-bis.1 y §7-bis.14)
# ==========================================================================
def _crear_registro(wb, modelo, titulo, encabezado, subtitulo, cabeceras,
                    filas, notas, anchos, totales=None):
    """Hoja nueva del molde REGISTRO, al FINAL del libro.

    §7-bis.14: `create_sheet()` SIN índice — mover una pestaña reordena
    `print_title_rows`, `print_area` y las referencias cacheadas, y rompería la
    idempotencia en la 2.ª pasada.

    La firma que `motor.fila_registro_appcc` exige: «#» en A4, cinco rótulos o
    más, ninguno «Tarea», y al menos un campo de registro (`Fecha`, `Temp`,
    `Especie`, `Lote`, `Proveedor`, `Verif.`, `Firma`…). Con eso el motor de la
    2.ª pasada le pone formato de fecha, formato «0,0 °C», desplegable en la
    columna de verificación, alto de cabecera, A4, protección y pie.

    `totales` = [(rótulo, {columna: fórmula})] va DEBAJO de las filas
    numeradas, o sea FUERA del cuerpo que `proteger` desbloquea: las fórmulas
    quedan bloqueadas y sin relleno verde, que es justo lo contrario de lo que
    pasaría dentro de la tabla.
    """
    if titulo in wb.sheetnames:
        return False
    ws = wb.create_sheet(titulo)
    ncol = len(cabeceras)
    est_tit = copy.copy(wb[modelo].cell(row=1, column=1)._style)
    hr_mod, _ = motor.cabecera_checklist(wb[modelo])
    if hr_mod is None:
        hr_mod, _ = motor.fila_registro_appcc(wb[modelo])
    if hr_mod is None:
        raise AnclaPerdida(f'«{modelo}» no sirve de modelo de estilos: no '
                           'tiene cabecera reconocible')
    est_cab = copy.copy(wb[modelo].cell(row=hr_mod, column=2)._style)
    est_dato = copy.copy(wb[modelo].cell(row=hr_mod + 1, column=2)._style)
    est_num = copy.copy(wb[modelo].cell(row=hr_mod + 1, column=1)._style)

    ws.cell(row=1, column=1).value = _est_texto(encabezado)
    ws.cell(row=1, column=1)._style = copy.copy(est_tit)
    ws.cell(row=2, column=1).value = _est_texto(subtitulo)
    for c in range(1, ncol + 1):
        cel = ws.cell(row=4, column=c)
        cel.value = cabeceras[c - 1]
        cel._style = copy.copy(est_cab)
    for i in range(filas):
        r = 5 + i
        ws.cell(row=r, column=1).value = i + 1
        ws.cell(row=r, column=1)._style = copy.copy(est_num)
        for c in range(2, ncol + 1):
            ws.cell(row=r, column=c)._style = copy.copy(est_dato)
    fila = 5 + filas
    if totales:
        for rotulo, formulas in totales:
            fila += 1
            ws.cell(row=fila, column=1).value = rotulo
            motor._merge(ws, f'A{fila}:{L(min(2, ncol))}{fila}')
            for col, formula in formulas.items():
                ws.cell(row=fila, column=col).value = formula
                motor.reg(ws, f'{L(col)}{fila}', formula)
    for nota in notas:
        fila += 2 if nota is notas[0] else 1
        ws.cell(row=fila, column=1).value = _est_texto(nota)
    for letra, ancho in anchos.items():
        ws.column_dimensions[letra].width = ancho
    return True


# ==========================================================================
# Constructor genérico de HOJA DE CHECKLIST nueva (clon del molde del kit)
# ==========================================================================
def _crear_checklist(wb, modelo, titulo, encabezado, bloques):
    """Hoja nueva del molde ▸, clonada de una hermana del mismo libro.

    `wb.copy_worksheet` deja la copia AL FINAL (§7-bis.14) con los estilos, los
    anchos y las bandas del modelo. Aquí se le ajusta el número de filas de
    cuerpo al contenido —insertando o borrando con las utilidades del motor,
    que sí mueven merges, DV y fórmulas— y se reescriben bandas y tareas. La
    2.ª pasada del motor le pone contador, 5 filas libres, DV, CF, A4 y pie.
    """
    if titulo in wb.sheetnames:
        return False
    ws = wb.copy_worksheet(wb[modelo])
    ws.title = titulo
    ws.cell(row=1, column=1).value = encabezado
    g = motor.geometria(ws)
    if not g:
        raise AnclaPerdida(f'«{modelo}»: el clon no conserva la geometría de '
                           'checklist de la familia')
    tope = g['contador'] or (ws.max_row + 1)
    primera = None
    for r in range(g['hr'] + 1, tope):
        if motor.es_fila_seccion(ws, r):
            primera = r
            break
    if primera is None:
        raise AnclaPerdida(f'«{modelo}»: sin bandas de sección de las que '
                           'copiar estilo')
    est_banda = _estilos(ws, primera)
    est_tarea = _estilos(ws, primera + 1)
    est_libre = _estilos(ws, tope - 1)

    # Cuerpo actual (de la cabecera al contador, sin contar el contador) y
    # cuerpo necesario: una banda + sus tareas por bloque, con la fila en
    # blanco de separación que este kit usa entre bloques.
    largo_actual = tope - (g['hr'] + 1)
    largo_nuevo = sum(1 + len(t) for _, t in bloques) + (len(bloques) - 1)
    if largo_nuevo > largo_actual:
        motor.insertar_filas(ws, tope, largo_nuevo - largo_actual)
    elif largo_nuevo < largo_actual:
        motor.eliminar_filas(ws, g['hr'] + 1 + largo_nuevo,
                             largo_actual - largo_nuevo)

    fila = g['hr'] + 1
    for i, (banda, tareas) in enumerate(bloques):
        if i:
            _pintar(ws, fila, est_libre)
            for c in range(1, NCOL + 1):
                ws.cell(row=fila, column=c).value = None
            fila += 1
        motor._desmerge_fila(ws, fila)
        _pintar(ws, fila, est_banda)
        for c in range(1, NCOL + 1):
            ws.cell(row=fila, column=c).value = None
        ws.cell(row=fila, column=1).value = banda
        motor._merge(ws, f'A{fila}:{L(NCOL)}{fila}')
        fila += 1
        for t in tareas:
            motor._desmerge_fila(ws, fila)
            _pintar(ws, fila, est_tarea)
            for c in range(1, NCOL + 1):
                ws.cell(row=fila, column=c).value = None
            _escribir_tarea(ws, fila, t)
            fila += 1
    motor.renumerar(ws)
    return True


# ==========================================================================
# FUENTES — ninguna cifra ni norma sin su origen (regla dura 6 del encargo)
# ==========================================================================
#: ⚠️ El **RD 1420/2006 está DEROGADO** desde el 22-dic-2022 (disposición
#: derogatoria única.h del RD 1021/2022). La lista blanca de §2.0 de la SPEC
#: todavía lo cita como norma viva; `motor.PROHIBIDAS` lo prohíbe y la landing
#: (`kit-tareas-sushi-bar.ts`, líneas 126 y 197) ya publica la cita correcta.
#: Aquí manda la vigente. La única mención permitida del número viejo es la que
#: dice que fue derogado, y así se escribe.
NORMA_ANISAKIS = ('RD 1021/2022, art. 8.1 (que derogó el RD 1420/2006) y '
                  'Rgto. (CE) 853/2004, Anexo III, Secc. VIII, Cap. III.D, en '
                  'la redacción del Rgto. (UE) 1276/2011')
FUENTE_ANISAKIS = 'Fuente: ' + NORMA_ANISAKIS + '.'
EXCEPCION_ACUICULTURA = (
    'Excepción (Rgto. (UE) 1276/2011): quedan exentos los productos de la '
    'acuicultura criados con pienso que no puede contener parásitos y en un '
    'entorno libre de parásitos vivos, siempre que el proveedor lo acredite '
    'por escrito. Archiva esa acreditación junto a este registro.')
FUENTE_INFORMAR = ('Fuente: RD 1021/2022, art. 8.2 — hay que informar al '
                   'consumidor de que el pescado ha sido congelado, por '
                   'cartel, carta o menú.')
FUENTE_ALERGENOS = ('Fuente: Anexo II del Rgto. (UE) 1169/2011 — son los 14 '
                    'alérgenos de declaración obligatoria; la información se '
                    'da por escrito y también verbalmente si el cliente la '
                    'pide.')
FUENTE_FRESCO = ('Fuente: Rgto. (CE) 853/2004, Anexo III, Secc. VIII, '
                 'Cap. VII — los productos frescos de la pesca se conservan a '
                 'una temperatura próxima a la de fusión del hielo. Este kit '
                 'usa 0-2 °C como rango único de la cámara de pescado crudo.')
FUENTE_PH = ('Fuente: 4,6 es el umbral internacional que separa los alimentos '
             'ácidos de los poco ácidos (Codex Alimentarius, CXC 23-1979) y '
             'es el límite crítico que el plan APPCC del local fija para el '
             'arroz avinagrado: en España no hay ninguna norma que dé un pH '
             'al arroz de sushi. Tiras de rango 4,0-5,0 con resolución 0,2; '
             'el pHmetro de punción calibrado es más preciso y es la opción '
             'recomendada si trabajas mucho volumen.')
FUENTE_TEMPERATURAS = ('Fuente: criterio único de la familia (§7-bis.19) — '
                       'cocción ≥70 °C en el centro del alimento (≥75 °C en '
                       'aves, picados y recalentados) según las '
                       'recomendaciones de AESAN, y mantenimiento en caliente '
                       '≥65 °C y en frío ≤4 °C según el RD 3484/2000 de '
                       'comidas preparadas.')
FUENTE_RIPCI = ('Fuente: RD 513/2017 (RIPCI) — revisión TRIMESTRAL a cargo del '
                'titular y revisión ANUAL por empresa mantenedora habilitada; '
                'retimbrado del extintor a los 5 años. Son dos obligaciones '
                'distintas, por eso van en dos filas.')
FUENTE_RGSEAA = ('Fuente: RD 191/2011 — la inscripción en el RGSEAA no se '
                 'renueva periódicamente: lo que obliga es comunicar las '
                 'modificaciones y el cese de la actividad.')
FUENTE_TEMPORADAS = ('Fuente: costera del bonito del norte (jun-oct, pico '
                     'jul-sep) y almadraba de atún rojo de Cádiz (abr-jun), '
                     'campañas publicadas por el MAPA. Contrasta cada año con '
                     'tu lonja: las campañas se abren y se cierran por cuota.')
FUENTE_MERMAS = ('Cómo se usa: una línea por descarte, el mismo día. El coste '
                 'total de la línea es kg × €/kg y los totales del pie los '
                 'calcula la hoja. Es el número que justifica el kit: sin '
                 'medir la merma no se puede bajar.')

TEXTO_ANISAKIS = (
    'Congelación previa obligatoria para el pescado que se sirva crudo, '
    'marinado, en salazón, ahumado en frío o poco cocinado: −20 °C en la '
    'totalidad del producto durante al menos 24 h, o −35 °C durante al menos '
    '15 h')


# ==========================================================================
# 01 — apertura y cierre por área  (fichero de ÁREAS del kit)
# ==========================================================================
#: DOM-25 — «Encender vitrina neta case y verificar 2-4 °C» a las 10:00 es
#: imposible (una vitrina recién encendida tarda 30-45 min en estabilizar) y
#: además fija por escrito una mala práctica: la neta case no se apaga de
#: noche. Se parte en dos: la comprobación normal y el caso de apagado.
VITRINA_OK = ('Comprobar que la vitrina neta case ha estado encendida toda la '
              'noche y registrar su temperatura (2-4 °C) — anota la lectura: '
              '____ °C')
VITRINA_APAGADA = [
    ('Si la vitrina estuvo apagada: encenderla y NO cargar pescado hasta que '
     'marque 2-4 °C estables (mínimo 45 min)', 'Barra sushi', 'Itamae',
     '10:00'),
]
#: DOM-12 / COM-15 — la misma cámara con dos límites en el mismo fichero
#: («−2 a 0 °C» en apertura, «0-2 °C» en cierre) y un tercero en 03. Se unifica
#: en 0-2 °C, que es el rango de hielo fundente del Rgto. 853/2004; −2 °C es
#: superchilling y no es el estándar de una cámara de servicio diario.
CAMARA_CRUDO = ('Verificar temperatura de la cámara de pescado crudo '
                '(0-2 °C, hielo fundente) — anota la lectura: ____ °C')
CAMARA_CIERRE = ('Envolver el pescado restante, etiquetarlo con su nº de lote '
                 'y devolverlo a la cámara (0-2 °C)')
#: DOM-08 — tres tareas de tres ficheros remitían a una «hoja de control» de
#: mermas que no existía. Ahora existe (03).
MERMAS_01 = ('Registrar las mermas de pescado del turno en la hoja «Registro '
             'de Mermas» del fichero 03: kg, motivo y coste')
#: DOM-10 — la regla de las 2 h estaba aplicada a piezas que están DENTRO de
#: una vitrina a 2-4 °C, donde por definición no están «fuera de
#: refrigeración»: obligaba a tirar la neta case entera cada dos horas.
DOS_HORAS_01 = ('Descartar las piezas que hayan estado más de 2 h FUERA de '
                'refrigeración (tabla del itamae o barra sin frío); las de la '
                'vitrina a 2-4 °C se consumen dentro de la jornada')
#: DOM-29 — «bamboo mats» es makisu y «plastic wrap» es film transparente.
MAKISU_APERTURA = ('Preparar los makisu (esterillas de bambú) con film '
                   'transparente nuevo')
MAKISU_CIERRE = ('Retirar el film transparente usado de los makisu; lavarlos, '
                 'secarlos y guardarlos secos')
#: DOM-26 — «NUNCA jabón» escrito en un documento de autocontroles es una no
#: conformidad servida, y contradice al propio kit, que sí sumerge las tablas
#: en solución desinfectante.
HANGIRI = ('Hangiri: lavar con agua caliente y cepillo, sin abrasivos; si usas '
           'detergente apto para uso alimentario, aclarar a fondo. Secar boca '
           'abajo al aire y no guardarlo húmedo')
#: DOM-24 — la lonja no cierra «temprano» por la noche: los pedidos se cursan
#: por la tarde. En el cierre queda anotar lo observado; el manager confirma.
PEDIDO_CIERRE = ('Anotar las necesidades de pescado observadas en el servicio '
                 'para el pedido de mañana (lo confirma el manager antes de '
                 'la hora de corte del proveedor)')
#: COM-22 + promesa «cierre completo y arqueo» de la landing (grid.templates[0],
#: `kit-tareas-sushi-bar.ts:116`), que el corpus no cumplía: 0 apariciones de
#: «arqueo» en los 11 ficheros. Dueño único: el encargado, en el 01.
ARQUEO = ('Arqueo de caja y cierre de TPV: contar el efectivo, cotejarlo con '
          'la Z del TPV y anotar el descuadre')
#: DOM-03 / COM-18 — la cadena horaria del arroz era físicamente imposible
#: (reposo de 30 min de 10:20 a 10:25) y no cuadraba con la de 02. Ésta es la
#: misma línea temporal en los dos ficheros, calculada hacia atrás desde el
#: primer servicio (12:00).
HORAS_01_ARROZ = {
    'Lavar arroz': '09:35',
    'Cocer arroz': '10:10',
    'Preparar sushi-zu': '10:45',
    'Mezclar arroz cocido con sushi-zu': '10:52',
    'Verificar pH del arroz': '11:00',
    'Cubrir arroz con pa': '11:05',
}
PH_01 = ('Medir el pH del arroz avinagrado con tiras de rango 4,0-5,0 '
         '(resolución 0,2) o pHmetro de punción y anotarlo en «Registro de pH '
         'del Arroz» del fichero 03 — límite crítico ≤4,6')


def _f01(wb, cambios):
    tocado = False
    ws = wb['Apertura Barra Sushi']
    if _sustituir(ws, 'Encender vitrina neta case', VITRINA_OK):
        cambios.append('«Apertura Barra Sushi»: la vitrina neta case se '
                       'COMPRUEBA desde la noche anterior, no se enciende a '
                       'las 10:00 — DOM-25')
    if _insertar_tras(ws, VITRINA_OK, VITRINA_APAGADA):
        cambios.append('«Apertura Barra Sushi»: tarea nueva para el caso de '
                       'vitrina apagada (45 min hasta 2-4 °C estables antes '
                       'de cargar producto) — DOM-25')
        tocado = True
    if _sustituir(ws, 'Verificar temperatura camara pescado crudo',
                  CAMARA_CRUDO):
        cambios.append('«Apertura Barra Sushi»: la cámara de pescado crudo '
                       'pasa de «−2 a 0 °C» al rango ÚNICO del kit, 0-2 °C '
                       '(hielo fundente) — DOM-12 / COM-15')
    if _sustituir(ws, 'Preparar bamboo mats', MAKISU_APERTURA):
        cambios.append('«Apertura Barra Sushi»: makisu (esterilla de bambú) y '
                       'film transparente en vez de «bamboo mats» y «plastic '
                       'wrap» — DOM-29')
    if _sustituir(ws, 'Verificar pH del arroz', PH_01):
        cambios.append('«Apertura Barra Sushi»: el pH se mide con tiras '
                       '4,0-5,0 (resolución 0,2) o pHmetro y se REGISTRA en '
                       'la hoja nueva del 03 — DOM-04 / §7-bis.20')
    # DOM-03 / COM-18: la columna de horas del bloque del arroz.
    n = 0
    for pref, hora in HORAS_01_ARROZ.items():
        r = _fila(ws, pref, 2)
        if r and ws.cell(row=r, column=5).value != hora:
            ws.cell(row=r, column=5).value = hora
            n += 1
    r = _fila(ws, 'Encender arrocera', 2)
    if r and ws.cell(row=r, column=5).value != '09:30':
        ws.cell(row=r, column=5).value = '09:30'
        n += 1
    if n:
        cambios.append(f'«Apertura Barra Sushi»: {n} horas del bloque del '
                       'arroz recalculadas y alineadas con 02 (reposo de 30 '
                       'min que empezaba a las 10:20 y cocía a las 10:25) — '
                       'DOM-03 / COM-18')
    motor.renumerar(ws)

    ws = wb['Cierre Barra Sushi']
    if _sustituir(ws, 'Registrar mermas de pescado en hoja de control',
                  MERMAS_01):
        cambios.append('«Cierre Barra Sushi»: las mermas remiten a la hoja '
                       '«Registro de Mermas», que ahora existe — DOM-08')
    if _sustituir(ws, 'Envolver pescado restante', CAMARA_CIERRE):
        cambios.append('«Cierre Barra Sushi»: la cámara de pescado crudo dice '
                       '0-2 °C, el mismo rango que la apertura y que 03, y se '
                       'etiqueta el lote — DOM-12 / DOM-14 / COM-15')
    if _sustituir(ws, 'Descartar piezas con mas de 2h', DOS_HORAS_01):
        cambios.append('«Cierre Barra Sushi»: la regla de las 2 h se aplica a '
                       'lo que está FUERA de refrigeración, no a la vitrina '
                       'a 2-4 °C — DOM-10')
    if _sustituir(ws, 'Descartar bamboo mats', MAKISU_CIERRE):
        cambios.append('«Cierre Barra Sushi»: makisu y film transparente '
                       '(y los makisu se lavan, no se tiran) — DOM-29')
    if _sustituir(ws, 'Limpiar hangiri', HANGIRI):
        cambios.append('«Cierre Barra Sushi»: el hangiri se lava con agua '
                       'caliente y cepillo; se retira el «NUNCA jabón», que '
                       'en un documento de autocontroles es una no '
                       'conformidad — DOM-26')
    if _sustituir(ws, 'Preparar pedido pescado para', PEDIDO_CIERRE):
        cambios.append('«Cierre Barra Sushi»: en el cierre se ANOTAN las '
                       'necesidades; el pedido lo confirma el manager antes '
                       'de la hora de corte — DOM-24 / COM-22')
    if _sustituir(ws, 'Cuadre de caja y cierre TPV', ARQUEO):
        cambios.append('«Cierre Barra Sushi»: ARQUEO de caja con Z del TPV y '
                       'descuadre (la landing lo promete en '
                       '`kit-tareas-sushi-bar.ts:116` y el corpus no lo tenía '
                       'ni una vez) — COM-22 / gate promesas')
    motor.renumerar(ws)

    if _instrucciones(wb, 'Turno de almuerzo y turno de cena', [
            'Las horas de estas hojas son las del turno de ALMUERZO, con la '
            'barra abierta a las 12:00. Para el turno de cena, súmale a cada '
            'hora la diferencia entre tus dos aperturas y marca la casilla '
            '«Cena» de la cabecera.',
            'El arroz avinagrado caduca 4 h después de mezclarse con el '
            'sushi-zu, así que la cena necesita SU PROPIO lote: el protocolo '
            'del segundo lote está en el fichero '
            '02-preparacion-arroz-pescado.xlsx.',
            'Lo que cambia de un turno a otro son las horas, no las tareas: '
            'imprime la misma hoja dos veces y anota el turno arriba.']):
        cambios.append('Instrucciones: turno de almuerzo y de cena, y el '
                       'segundo lote de arroz — DOM-11')
    if _instrucciones(wb, 'Temperaturas y arqueo de este fichero', [
            'Cámara de pescado crudo: 0-2 °C en las tres hojas donde aparece '
            '(aquí, en el cierre y en «Temperaturas Diario» del 03). '
            + FUENTE_FRESCO,
            'Cámara de congelación de anisakis: −20 °C o menos. Es un límite '
            'crítico distinto del congelador general (−18 °C) y NO se '
            'mezclan. ' + FUENTE_ANISAKIS,
            'El arqueo de caja se hace UNA vez y lo hace el encargado, en la '
            'hoja de cierre de este fichero. El manager lo revisa al día '
            'siguiente desde 05-tareas-manager.xlsx: no se cuenta el cajón '
            'dos veces.']):
        cambios.append('Instrucciones: rango único por equipo y dueño único '
                       'del arqueo, con la fuente — DOM-12 / COM-15 / COM-22')
    return tocado


# ==========================================================================
# 02 — arroz y corte de pescado
# ==========================================================================
#: DOM-03 / COM-18 — la misma línea temporal que 01, calculada hacia atrás
#: desde el primer servicio: reposo real de 30 min y cocción real en arrocera.
HORAS_02 = {
    'Pesar arroz sushi': '09:30',
    'Lavar arroz 3-4 veces': '09:35',
    'Dejar reposar arroz en agua 30 min': '09:40',
    'Cocer arroz': '10:10',
    'Dejar reposar 10 min tras': '10:40',
    'Preparar sushi-zu': '10:45',
    'Calentar mezcla': '10:47',
    'Transferir arroz cocido a hangiri': '10:50',
    'Verter sushi-zu': '10:52',
    'Abanicar arroz': '10:55',
    'Medir pH': '11:00',
    'Cubrir con pa': '11:05',
    'Textura:': '11:10',
    'Temperatura:': '11:10',
    'Brillo:': '11:10',
    'Si pH': '11:10',
    'Anotar hora de prepara': '11:10',
}
#: DOM-22 — «por 500g arroz» no decía si crudo o cocido (la diferencia es del
#: doble largo) y la dosis quedaba por debajo del ~10 % de avinagrado que hace
#: falta para bajar de 4,6 con seguridad.
SUSHI_ZU = ('Preparar el sushi-zu por cada 1 kg de arroz CRUDO (≈2,2 kg '
            'cocido): 200 ml de vinagre de arroz de acidez ≥4,3 %, 60-100 g '
            'de azúcar y 30 g de sal')
PH_02 = ('Medir el pH del arroz avinagrado con tiras de rango 4,0-5,0 '
         '(resolución 0,2) o pHmetro de punción calibrado, y anotar el valor '
         'en «Registro de pH del Arroz» del fichero 03 — límite crítico ≤4,6')
#: DOM-21 — «Si pH >4.6: descartar lote» convierte un ajuste de dos minutos en
#: una pérdida diaria. Escalado de acciones correctoras.
PH_CORRECTORA = ('Si el pH sale >4,6: 1) añadir sushi-zu poco a poco, mezclar '
                 'y volver a medir; 2) si sigue alto tras dos correcciones, '
                 'no dejarlo a temperatura ambiente: refrigerar a ≤5 °C y '
                 'usarlo en elaboraciones cocinadas; 3) descartar sólo si no '
                 'sirve para ningún uso. Anotar la acción tomada')
ACIDIFICACION = ('Anotar el sushi-zu realmente añadido (ml por kg de arroz '
                 'cocido) en «Registro de pH del Arroz»: es la acidificación '
                 'MEDIDA que respalda el pH del lote')
DESCARTE_4H = ('Anotar la hora de avinagrado en la hoja de pH: el lote se '
               'descarta 4 h después y nunca se guarda para el día siguiente')
#: DOM-11 — el kit sólo cubría un servicio al día.
SEGUNDO_LOTE = [
    ('Programar el segundo lote de arroz para la cena: el del almuerzo caduca '
     '4 h después de avinagrarse', 'Cocina', 'Ayudante sushi', '16:00'),
    ('Repetir el protocolo completo (lavado, reposo, cocción y sushi-zu) para '
     'el turno de cena', 'Cocina', 'Ayudante sushi', '17:00'),
    ('Medir el pH del segundo lote y anotarlo en «Registro de pH del Arroz» '
     'del fichero 03', 'Cocina', 'Itamae', '18:30'),
    ('Descartar el arroz del turno de almuerzo: no se mezcla nunca con el '
     'lote nuevo', 'Cocina', 'Ayudante sushi', '17:00'),
]
#: DOM-14 — nadie comprobaba, ANTES de cortar, que la pieza que se va a servir
#: cruda pertenece a un lote con la congelación terminada; y no había ni una
#: mención de la descongelación, que es donde se rompe la cadena.
LOTE_ANTES = [
    ('Comprobar la etiqueta del lote ANTES de cortar para consumo en crudo: '
     'congelación antiparasitaria terminada y validada, o acreditación de '
     'acuicultura del proveedor', 'Cámara', 'Itamae', '10:55'),
    ('Descongelar en cámara a 0-2 °C, nunca a temperatura ambiente ni bajo el '
     'grifo, y anotar en «Registro Congelación» la fecha y la hora de entrada '
     'y de uso', 'Cámara', 'Itamae', '10:55'),
]
#: TEC-20 (c) — la landing vende «yanagiba, sashimi, nigiri y maki» y «maki» no
#: aparecía ni una vez en el corpus.
ATUN = ('Atún (maguro): corte en bloque y láminas de 8-10 mm para nigiri, '
        'sashimi y relleno de maki')
#: DOM-29 — hamachi es Seriola quinqueradiata; el pez limón español es
#: Seriola dumerili, que es otra especie.
HAMACHI = ('Hamachi / seriola japonesa (Seriola quinqueradiata; sustituto '
           'local: lecha o pez limón, Seriola dumerili): fileteado y corte '
           'fino para sashimi')
#: DOM-30 — el aburaage no se «hidrata»: se escalda para desgrasarlo y se cuece
#: en dashi. Y «tofu piel» no es la denominación de nada.
INARI = ('Inari (aburaage): escaldar para desgrasar, escurrir y cocer en '
         'dashi con soja, mirin y azúcar; enfriar y escurrir antes de rellenar')


def _f02(wb, cambios):
    tocado = False
    ws = wb['Protocolo Arroz Sushi']
    n = 0
    for pref, hora in HORAS_02.items():
        r = _fila(ws, pref, 2)
        if r and ws.cell(row=r, column=5).value != hora:
            ws.cell(row=r, column=5).value = hora
            n += 1
    if n:
        cambios.append(f'«Protocolo Arroz Sushi»: {n} horas recalculadas — el '
                       'reposo de 30 min empezaba a las 10:20 y la cocción a '
                       'las 10:25, y la línea no cuadraba con la de 01 — '
                       'DOM-03 / COM-18')
    if _sustituir(ws, 'Preparar sushi-zu: 80ml', SUSHI_ZU):
        cambios.append('«Protocolo Arroz Sushi»: el sushi-zu se dosifica por '
                       'kg de arroz CRUDO, con la acidez del vinagre y una '
                       'dosis que sí baja de 4,6 — DOM-22')
    if _sustituir(ws, 'Medir pH con tiras reactivas', PH_02):
        cambios.append('«Protocolo Arroz Sushi»: tiras de rango 4,0-5,0 con '
                       'resolución 0,2 (o pHmetro) y registro del valor, que '
                       'no tenía dónde anotarse — DOM-04 / §7-bis.20')
    if _sustituir(ws, 'Si pH', PH_CORRECTORA):
        cambios.append('«Protocolo Arroz Sushi»: acción correctora ESCALADA '
                       'del PCC de pH en vez de «descartar el lote» — DOM-21')
    if _sustituir(ws, 'Anotar hora de prepara', DESCARTE_4H):
        cambios.append('«Protocolo Arroz Sushi»: la hora de avinagrado se '
                       'anota en la hoja de pH — DOM-04')
    if _insertar_tras(ws, 'Abanicar arroz',
                      [(ACIDIFICACION, 'Cocina', 'Ayudante sushi', '10:57')]):
        cambios.append('«Protocolo Arroz Sushi»: acidificación MEDIDA (ml de '
                       'sushi-zu por kg de arroz cocido) registrada junto al '
                       'pH — §7-bis.20')
        tocado = True
    if _bloque_al_final(ws, '  SEGUNDO LOTE (TURNO CENA)', SEGUNDO_LOTE):
        cambios.append('«Protocolo Arroz Sushi»: bloque nuevo «SEGUNDO LOTE '
                       '(TURNO CENA)» — el kit sólo cubría un servicio al día '
                       'con un arroz que caduca a las 4 h — DOM-11')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Protocolo Corte Pescado']
    if _insertar_tras(ws, 'Inspeccionar filetes', LOTE_ANTES):
        cambios.append('«Protocolo Corte Pescado»: comprobación del LOTE '
                       'antes de cortar en crudo y descongelación controlada '
                       'en cámara (0 apariciones de «descongel» en el kit) — '
                       'DOM-14')
        tocado = True
    if _sustituir(ws, 'Atun (maguro)', ATUN):
        cambios.append('«Protocolo Corte Pescado»: el corte del atún nombra '
                       'nigiri, sashimi y MAKI, que la landing vende y el '
                       'corpus no tenía — TEC-20')
    if _sustituir(ws, 'Hamachi (pez limon)', HAMACHI):
        cambios.append('«Protocolo Corte Pescado»: hamachi y pez limón son '
                       'especies distintas (Seriola quinqueradiata frente a '
                       'Seriola dumerili) — DOM-29')
    if _sustituir(ws, 'Tofu piel (inari)', INARI):
        cambios.append('«Protocolo Corte Pescado»: el aburaage se escalda y se '
                       'cuece en dashi, no se «hidrata» — DOM-30')
    motor.renumerar(ws)

    if _instrucciones(wb, 'pH del arroz: cómo se mide y dónde se anota', [
            'El pH es el límite crítico del arroz y hasta ahora no tenía '
            'dónde anotarse. Se mide con tiras de rango 4,0-5,0 y resolución '
            '0,2 —las de rango ancho no distinguen 4,5 de 4,7, que es justo '
            'la decisión— o con pHmetro de punción calibrado.',
            'Cada lote se anota en la hoja «Registro de pH del Arroz» del '
            'fichero 03-seguridad-anisakis-appcc.xlsx, con los ml de sushi-zu '
            'por kg de arroz cocido: esa acidificación medida es la que '
            'respalda el valor.',
            FUENTE_PH]):
        cambios.append('Instrucciones: método del pH y su registro, con la '
                       'fuente — DOM-04 / DOM-21 / DOM-22 / §7-bis.20')
    return tocado


# ==========================================================================
# 03 — anisakis, APPCC y las CUATRO hojas nuevas
# ==========================================================================
ALERGENOS_14 = ['Gluten', 'Crustáceos', 'Huevos', 'Pescado', 'Cacahuetes',
                'Soja', 'Leche', 'Frutos de cáscara', 'Apio', 'Mostaza',
                'Sésamo', 'Sulfitos', 'Altramuces', 'Moluscos']

HOJA_ALERGENOS = 'Matriz de Alérgenos'
HOJA_PH = 'Registro de pH del Arroz'
HOJA_RECEPCION = 'Control de Recepción'
HOJA_MERMAS = 'Registro de Mermas'

#: DOM-01 / COM-01 / TEC-11 / censo T0.1 — «-20 °C durante mínimo 7 días»
#: atribuido a la norma es falso (7 días es criterio para congeladores
#: domésticos, no el requisito del establecimiento) y multiplica por 7 la
#: cámara que el cliente cree necesitar.
INSTR_03 = [
    ('Este registro es OBLIGATORIO para servir pescado crudo, marinado, en '
     'salazón, ahumado en frío o poco cocinado',
     'Este registro es OBLIGATORIO por la legislacion espanola'),
    (TEXTO_ANISAKIS, 'El pescado debe congelarse a'),
    ('Registra CADA lote con su especie, nº de lote, fecha de entrada, inicio '
     'y fin de congelación', 'Registra CADA lote de pescado'),
    ('La inspección de Sanidad verificará estos registros — tenlos siempre al '
     'día', 'La inspeccion de Sanidad verificara'),
]

NOTA_B27 = ('IMPORTANTE: el límite crítico de este PCC es −20 °C. Si la '
            'temperatura sube por encima de −20 °C en cualquier momento del '
            'tratamiento, éste NO es válido: reinicia el cómputo completo de '
            'las 24 h. El −18 °C es el límite del congelador general y no '
            'sirve para el tratamiento antiparasitario.')

#: DOM-23 — dos de las siete filas del registro de temperaturas no servían como
#: puntos de control: «Arrocera (100 °C)» no se puede desviar y el arroz de
#: servicio traía una horquilla de 17 grados que además contradecía al 02.
TEMPS_03 = [
    ('Camara pescado crudo', 'Cámara de pescado crudo (0-2 °C)'),
    ('Arrocera (temp coccion)',
     'Aceite de fritura de la cocina caliente (170-180 °C)'),
    ('Arroz servicio (ambiente)',
     'Arroz de servicio al montar el nigiri (35-37 °C)'),
]
NOTA_TEMPS = (
    'Anota aquí la lectura de APERTURA de cada equipo, una por día. La '
    'lectura de CIERRE se marca y se firma en el checklist de cierre del '
    'fichero 01. Si una lectura se sale del rango que declara su fila, la '
    'celda se pone en ROJO sola: apunta debajo la acción correctora.')
NOTA_TEMPS_2 = 'Acción correctora / incidencia de la semana: ________________'


def _f03(wb, cambios):
    tocado = False
    ws = wb['Instrucciones']
    for nuevo, viejo in INSTR_03:
        r = _fila(ws, '▸ ' + nuevo, 2)
        if r is not None:
            continue
        r = _exige(ws, '▸ ' + viejo, 2)
        ws.cell(row=r, column=2).value = '▸ ' + _est_texto(nuevo)
    cambios.append('«Instrucciones» de 03: la congelación antiparasitaria se '
                   'cita bien (−20 °C ≥ 24 h o −35 °C ≥ 15 h) y ya no se '
                   'atribuye a la norma un plazo de 7 días — DOM-01 / COM-01 '
                   '/ TEC-11')
    if _instrucciones(wb, 'La norma, con su fuente', [
            TEXTO_ANISAKIS + '. ' + FUENTE_ANISAKIS,
            EXCEPCION_ACUICULTURA,
            'Si tu local quiere un margen propio por encima del mínimo legal, '
            'escríbelo como criterio TUYO («mínimo legal 24 h; en esta casa '
            '48 h»), nunca como si lo pidiera la norma.',
            FUENTE_INFORMAR,
            FUENTE_FRESCO]):
        cambios.append('«Instrucciones» de 03: bloque «La norma, con su '
                       'fuente» con la excepción de acuicultura del Rgto. (UE) '
                       '1276/2011, que faltaba — DOM-15 / §2.0')

    # --- Registro Congelación: columnas de lote y de origen ----------------
    hoja = ('Registro Congelación' if 'Registro Congelación' in wb.sheetnames
            else 'Registro Congelacion')
    ws = wb[hoja]
    hr, cols = motor.fila_registro_appcc(ws)
    if hr is None:
        raise AnclaPerdida(f'«{hoja}»: no la reconoce fila_registro_appcc')
    if 'Nº de lote' not in cols:
        col_especie = next(c for k, c in cols.items()
                           if _clave(k).startswith('especie'))
        motor.insertar_columna(ws, col_especie + 1)
        ws.cell(row=hr, column=col_especie + 1).value = 'Nº de lote'
        ws.column_dimensions[L(col_especie + 1)].width = 14
        hr, cols = motor.fila_registro_appcc(ws)
        col_prov = next(c for k, c in cols.items()
                        if _clave(k).startswith('proveedor'))
        motor.insertar_columna(ws, col_prov + 1)
        ws.cell(row=hr, column=col_prov + 1).value = 'Origen y acreditación'
        ws.column_dimensions[L(col_prov + 1)].width = 22
        cambios.append(f'«{hoja}»: columnas nuevas «Nº de lote» y «Origen y '
                       'acreditación» (salvaje / acuicultura + nº de '
                       'certificado), que el registro no tenía — DOM-14 / '
                       'DOM-15')
        tocado = True
    r = _fila(ws, 'Normativa:', 1) or _fila(ws, 'Normativa:', 2)
    if r:
        col = 1 if _clave(ws.cell(row=r, column=1).value or '').startswith(
            'normativa') else 2
        nuevo = _est_texto(
            'Normativa: ' + NORMA_ANISAKIS + ' — obligatorio en todo '
            'establecimiento que sirva pescado crudo, marinado, en salazón, '
            'ahumado en frío o poco cocinado.')
        if ws.cell(row=r, column=col).value != nuevo:
            ws.cell(row=r, column=col).value = nuevo
            cambios.append(f'«{hoja}»: la cita normativa del encabezado pasa '
                           'al RD 1021/2022 art. 8.1, que derogó el '
                           'RD 1420/2006, con la duración correcta — DOM-01 / '
                           'COM-01')
    r = _fila(ws, 'IMPORTANTE:', 2)
    if r and ws.cell(row=r, column=2).value != _est_texto(NOTA_B27):
        ws.cell(row=r, column=2).value = _est_texto(NOTA_B27)
        cambios.append(f'«{hoja}»: UN solo límite crítico. El aviso de '
                       'reinicio se disparaba a −18 °C y validaba lotes a '
                       '−19 °C que incumplen —20 °C — DOM-02 / COM-16 / '
                       'TEC-11')
    r = _fila(ws, 'Responsable APPCC:', 2)
    if r:
        for texto in (EXCEPCION_ACUICULTURA, FUENTE_ANISAKIS):
            if _fila(ws, texto, 2) is None:
                motor.insertar_filas(ws, r, 1)
                ws.cell(row=r, column=2).value = _est_texto(texto)
                tocado = True
        cambios.append(f'«{hoja}»: nota al pie con la excepción de acuicultura '
                       'y la fuente de la norma — DOM-15 / §2.0')

    # --- Temperaturas Diario ----------------------------------------------
    ws = wb['Temperaturas Diario']
    for viejo, nuevo in TEMPS_03:
        _sustituir(ws, viejo, nuevo, col=2, tarea=False)
    cambios.append('«Temperaturas Diario»: la cámara de pescado crudo dice '
                   '0-2 °C (rango único del kit); la arrocera a 100 °C y el '
                   'arroz «20-37 °C» —una horquilla de 17 grados— se sustituyen '
                   'por dos controles que sí se pueden desviar — DOM-12 / '
                   'DOM-23')
    r = _fila(ws, 'Registrar 2 veces al dia', 2)
    if r:
        ws.cell(row=r, column=2).value = _est_texto(NOTA_TEMPS)
        if _fila(ws, NOTA_TEMPS_2, 2) is None:
            motor.insertar_filas(ws, r + 1, 1)
            ws.cell(row=r + 1, column=2).value = _est_texto(NOTA_TEMPS_2)
            tocado = True
        cambios.append('«Temperaturas Diario»: la instrucción pedía DOS '
                       'lecturas diarias en una rejilla con una sola celda '
                       'por equipo y día. Ahora pide la de apertura y manda '
                       'la de cierre al checklist de 01, que sí la tiene, y '
                       'añade la línea de acción correctora — DOM-13 / TEC-09')

    # --- Trazabilidad Pescado ---------------------------------------------
    ws = wb['Trazabilidad Pescado']
    hr, cols = motor.fila_registro_appcc(ws)
    if hr and not any(_clave(k).startswith('temp') for k in cols):
        col_firma = next((c for k, c in cols.items()
                          if _clave(k).startswith('firma')), max(cols.values()))
        motor.insertar_columna(ws, col_firma)
        ws.cell(row=hr, column=col_firma).value = 'Temp recepción (°C)'
        ws.column_dimensions[L(col_firma)].width = 16
        cambios.append('«Trazabilidad Pescado»: columna «Temp recepción (°C)» '
                       '— el registro anotaba la compra pero no la '
                       'temperatura con la que llegó — DOM-27')
        tocado = True

    # --- Las cuatro hojas nuevas ------------------------------------------
    modelo = 'Trazabilidad Pescado'
    anchos_al = {'A': 5, 'B': 30, 'Q': 22, 'R': 16}
    for i in range(14):
        anchos_al[L(3 + i)] = 4.5
    if _crear_registro(
            wb, modelo, HOJA_ALERGENOS,
            'Matriz de Alérgenos por Plato — Sushi Bar',
            'Carta vigente desde: ___/___/______    Revisada por: __________',
            ['#', 'Plato o elaboración'] + ALERGENOS_14
            + ['Contaminación cruzada (indicar)', 'Revisado por (firma)'],
            18,
            ['Marca con una X la casilla del alérgeno que el plato CONTIENE. '
             'En «contaminación cruzada» anota el alérgeno que puede llegar '
             'por freidora, tabla, plancha o utensilio compartido: en un '
             'sushi bar es el caso del gluten (panko y tempura), del sésamo y '
             'de los crustáceos.',
             'Alérgenos propios de la carta japonesa: PESCADO, crustáceos, '
             'moluscos, soja (shoyu, miso), gluten (shoyu, panko, tempura, '
             'surimi), sésamo, huevo (tamago, mayonesas), sulfitos y frutos '
             'de cáscara.',
             FUENTE_ALERGENOS],
            anchos_al):
        cambios.append(f'hoja nueva «{HOJA_ALERGENOS}»: matriz plato × 14 '
                       'alérgenos del Anexo II del Rgto. (UE) 1169/2011 con '
                       'columna de contaminación cruzada — la landing la '
                       'vende dentro de este fichero y no existía — DOM-07 / '
                       'TEC-12')
        tocado = True
    if _crear_registro(
            wb, modelo, HOJA_PH,
            'Registro de pH del Arroz Avinagrado — Sushi Bar',
            'Semana del ___/___/______ al ___/___/______',
            ['#', 'Fecha', 'Lote / hora de avinagrado', 'kg de arroz cocido',
             'Sushi-zu añadido (ml/kg)', 'pH medido', 'Acción correctora',
             'Verif.', 'Firma'],
            20,
            ['Una línea por LOTE de arroz, no por día: si haces arroz para el '
             'almuerzo y para la cena, son dos líneas. El límite crítico es '
             'pH ≤ 4,6.',
             'La columna «Sushi-zu añadido» es la acidificación MEDIDA: es lo '
             'que permite repetir el resultado y lo que se enseña si un '
             'inspector pregunta por qué el arroz se mantiene a temperatura '
             'ambiente.',
             FUENTE_PH],
            {'A': 5, 'B': 12, 'C': 22, 'D': 16, 'E': 18, 'F': 11, 'G': 34,
             'H': 9, 'I': 16}):
        cambios.append(f'hoja nueva «{HOJA_PH}»: el PCC estrella del kit no '
                       'tenía NINGUNA celda donde anotarse pese a que las '
                       'Instrucciones mandaban «registrar cada lote» — '
                       'DOM-04 / DOM-21 / DOM-22')
        tocado = True
    if _crear_registro(
            wb, modelo, HOJA_RECEPCION,
            'Control de Recepción de Pescado y Marisco — Sushi Bar',
            'Semana del ___/___/______ al ___/___/______',
            ['#', 'Fecha', 'Hora', 'Proveedor / lonja', 'Especie', 'kg',
             'Temp recepción (°C)', 'Aspecto (ojos, agallas, olor, textura)',
             'Etiquetado y zona FAO', 'Verif.', 'Aceptado / Rechazado',
             'Motivo del rechazo', 'Firma'],
            20,
            ['Criterio de aceptación: pescado fresco a temperatura próxima a '
             'la de fusión del hielo (0-2 °C), ojos brillantes y salientes, '
             'agallas rojas y húmedas, olor a mar y carne firme al tacto. '
             'Congelado: −18 °C o menos y sin signos de descongelación '
             '(escarcha suelta, bloque deformado).',
             'Si rechazas, anota el motivo y guarda el albarán: el rechazo '
             'documentado es lo que demuestra el control, no la ausencia de '
             'incidencias.',
             FUENTE_FRESCO],
            {'A': 5, 'B': 12, 'C': 8, 'D': 20, 'E': 16, 'F': 8, 'G': 16,
             'H': 30, 'I': 18, 'J': 9, 'K': 18, 'L': 24, 'M': 14}):
        cambios.append(f'hoja nueva «{HOJA_RECEPCION}»: la recepción es el '
                       'primer punto de control de cualquier APPCC de pescado '
                       'y el kit sólo tenía una línea de checklist sin '
                       'soporte — DOM-27')
        tocado = True
    if _crear_registro(
            wb, modelo, HOJA_MERMAS,
            'Registro de Mermas de Pescado y Producto — Sushi Bar',
            'Mes: _______________    Responsable: _________________________',
            ['#', 'Fecha', 'Turno', 'Especie / producto', 'kg descartados',
             'Motivo', 'Coste €/kg', 'Coste total €', 'Firma'],
            22,
            [FUENTE_MERMAS,
             'Motivos que conviene distinguir, porque cada uno se corrige de '
             'una forma: caducado, más de 2 h fuera de refrigeración, corte '
             'defectuoso, sobreproducción, devolución de sala y rechazo en '
             'recepción.'],
            {'A': 5, 'B': 12, 'C': 12, 'D': 26, 'E': 15, 'F': 30, 'G': 12,
             'H': 14, 'I': 16},
            totales=[('TOTAL del periodo',
                      {5: '=SUM(E5:E26)', 8: '=SUM(H5:H26)'})]):
        cambios.append(f'hoja nueva «{HOJA_MERMAS}»: tres tareas de tres '
                       'ficheros (01, 05 y 06) remitían a una «hoja de '
                       'control» de mermas que no existía en el kit — DOM-08 '
                       '/ §2.2')
        tocado = True

    if _instrucciones(wb, 'Las cuatro hojas nuevas de este fichero', [
            f'«{HOJA_ALERGENOS}»: una fila por plato y una columna por cada '
            'uno de los 14 alérgenos del Anexo II del Rgto. (UE) 1169/2011, '
            'más la casilla de contaminación cruzada. Es la información que '
            'sala tiene que poder dar en el momento.',
            f'«{HOJA_PH}»: una línea por lote de arroz con el pH medido y los '
            'ml de sushi-zu por kg. Es el registro del límite crítico del '
            'producto estrella.',
            f'«{HOJA_RECEPCION}»: temperatura, aspecto, etiquetado y decisión '
            'de aceptar o rechazar, con el motivo. Es el primer punto de '
            'control del pescado.',
            f'«{HOJA_MERMAS}»: kg y coste de lo que se tira, con totales del '
            'periodo. Es el número con el que se justifica el kit.']):
        cambios.append('«Instrucciones» de 03: las cuatro hojas nuevas, '
                       'explicadas — DOM-04 / DOM-07 / DOM-08 / DOM-27')
    return tocado


# ==========================================================================
# 04 — barra y vitrina neta case
# ==========================================================================
FIFO_04 = ('Rotación FIFO por lotes: dentro de la vitrina a 2-4 °C el pescado '
           'se consume en la jornada; fuera de refrigeración, máximo 2 h')
MONTAJE_04 = ('Anotar la hora de montaje y el nº de lote de cada bandeja: en '
              'vitrina a 2-4 °C se consume dentro de la jornada, fuera de '
              'refrigeración el tope son 2 h')
REPONER_04 = ('Reponer piezas en la vitrina desde cámara por FIFO: primero el '
              'lote más antiguo, anotando su nº de lote de «Trazabilidad '
              'Pescado» (fichero 03)')
DOS_HORAS_04 = ('Descartar las piezas que hayan estado más de 2 h FUERA de '
                'refrigeración; las de la vitrina a 2-4 °C, al cierre')
MAKISU_04 = ('Preparar makisu (esterillas de bambú) nuevos con film '
             'transparente')
MAKISU_04B = ('Renovar el film transparente de los makisu cada 2 horas')


def _f04(wb, cambios):
    ws = wb['Instrucciones']
    if _sustituir(ws, '▸ Rotacion FIFO', '▸ ' + FIFO_04, col=2, tarea=False):
        cambios.append('«Instrucciones» de 04: la regla de las 2 h deja de '
                       'aplicarse a lo que está DENTRO de una vitrina '
                       'refrigerada — DOM-10')
    ws = wb['Mise en Place Barra']
    if _sustituir(ws, 'Anotar hora de montaje', MONTAJE_04):
        cambios.append('«Mise en Place Barra»: hora de montaje Y nº de lote, '
                       'con las dos reglas separadas — DOM-10 / TEC-20')
    if _sustituir(ws, 'Reponer piezas en vitrina desde camara', REPONER_04):
        cambios.append('«Mise en Place Barra»: el FIFO es POR LOTES, como '
                       'promete la landing; el nº de lote sale de 03 — '
                       'TEC-20')
    if _sustituir(ws, 'Descartar piezas con mas de 2h', DOS_HORAS_04):
        cambios.append('«Mise en Place Barra»: misma redacción de la regla de '
                       'las 2 h que en 01, no dos — DOM-10')
    if _sustituir(ws, 'Preparar bamboo mats', MAKISU_04):
        cambios.append('«Mise en Place Barra»: makisu y film transparente — '
                       'DOM-29')
    if _sustituir(ws, 'Renovar plastic wrap de bamboo mats', MAKISU_04B):
        cambios.append('«Mise en Place Barra»: makisu y film transparente '
                       '(renovación cada 2 h) — DOM-29')
    motor.renumerar(ws)
    return False


# ==========================================================================
# 05 — manager: dos hojas nuevas y el reparto de dueños
# ==========================================================================
HOJA_COMPARATIVA = 'Comparativa de Proveedores'
HOJA_REPORTING = 'Reporting Semanal'

RECEPCION_05 = ('Verificar la recepción del pedido de pescado y anotarla en '
                '«Control de Recepción» del fichero 03: temperatura, aspecto '
                'y decisión de aceptar o rechazar')
MERMAS_05 = ('Controlar las mermas del día en «Registro de Mermas» del '
             'fichero 03: kg, motivo y coste')
PEDIDO_05 = ('Confirmar el pedido de pescado de mañana ANTES de la hora de '
             'corte de tu proveedor (por defecto 18:00; anota aquí la tuya: '
             '____)')
CAJA_05 = ('Revisar el arqueo de caja del turno y el descuadre que anotó el '
           'encargado en el fichero 01 (el arqueo se hace una sola vez)')
SEMANALES_05 = [
    ('Comparar el precio €/kg por especie entre los proveedores de la semana '
     'en la hoja «Comparativa de Proveedores»', 'Oficina', 'Manager',
     'Lunes'),
    ('Rellenar y enviar el «Reporting Semanal»: ventas, comensales, ticket '
     'medio, compras de pescado, food cost y mermas', 'Oficina', 'Manager',
     'Domingo'),
]


def _f05(wb, cambios):
    tocado = False
    ws = wb['Instrucciones']
    if _sustituir(ws, '▸ Checklist diario, semanal y mensual',
                  '▸ Checklist diario y semanal del gerente o encargado, más '
                  'la comparativa de proveedores y el reporting semanal; las '
                  'tareas mensuales de mantenimiento van en el fichero '
                  '07-semanales-mensuales.xlsx', col=2, tarea=False):
        cambios.append('«Instrucciones» de 05: el fichero anunciaba tres '
                       'checklists y traía dos — COM-17')
    ws = wb['Tareas Diarias Manager']
    if _sustituir(ws, 'Verificar recepcion pedido pescado', RECEPCION_05):
        cambios.append('«Tareas Diarias Manager»: la recepción se REGISTRA en '
                       'la hoja nueva del 03 — DOM-27')
    if _sustituir(ws, 'Controlar mermas', MERMAS_05):
        cambios.append('«Tareas Diarias Manager»: las mermas se anotan en la '
                       'hoja «Registro de Mermas» — DOM-08')
    r = _sustituir(ws, 'Confirmar pedido de pescado para', PEDIDO_05)
    if r:
        ws.cell(row=r, column=5).value = '18:00'
        cambios.append('«Tareas Diarias Manager»: el pedido se confirma a las '
                       '18:00, no a las 22:00 «porque la lonja cierra '
                       'temprano» — DOM-24')
    if _sustituir(ws, 'Cuadre de caja', CAJA_05):
        cambios.append('«Tareas Diarias Manager»: el arqueo lo hace el '
                       'encargado en 01 y el manager lo REVISA: dueño único '
                       'por tarea, que es lo que la landing promete — COM-22')
    motor.renumerar(ws)

    ws = wb['Tareas Semanales Manager']
    if _insertar_tras(ws, 'Pedido semanal:', SEMANALES_05):
        cambios.append('«Tareas Semanales Manager»: comparativa de '
                       'proveedores y reporting, prometidos en la tarjeta del '
                       'manager y con 0 apariciones en el fichero — DOM-28 / '
                       'COM-24 / TEC-20')
        tocado = True
    motor.renumerar(ws)

    modelo = 'Tareas Diarias Manager'
    if _crear_registro(
            wb, modelo, HOJA_COMPARATIVA,
            'Comparativa de Proveedores de Pescado — Sushi Bar',
            'Semana del ___/___/______ al ___/___/______',
            ['#', 'Fecha', 'Especie', 'Proveedor A (€/kg)',
             'Proveedor B (€/kg)', 'Proveedor C (€/kg)',
             'Mejor precio (€/kg) y proveedor',
             'Calidad y observaciones (talla, frescura, servicio)', 'Firma'],
            20,
            ['Una línea por especie y semana. El precio más bajo no siempre '
             'gana: anota en «calidad y observaciones» la talla, el estado de '
             'llegada y el cumplimiento de horario, que es lo que hace cara '
             'una compra barata.',
             'Lleva esta hoja a la negociación: un histórico de €/kg por '
             'especie es el único argumento que mueve a un mayorista.'],
            {'A': 5, 'B': 12, 'C': 20, 'D': 16, 'E': 16, 'F': 16, 'G': 26,
             'H': 40, 'I': 14}):
        cambios.append(f'hoja nueva «{HOJA_COMPARATIVA}»: la landing la vende '
                       'en la tarjeta del manager y el fichero no tenía ni '
                       'una celda numérica — DOM-28 / COM-24')
        tocado = True
    if _crear_registro(
            wb, modelo, HOJA_REPORTING,
            'Reporting Semanal del Sushi Bar',
            'Semana del ___/___/______ al ___/___/______',
            ['#', 'Fecha', 'Ventas (€)', 'Comensales', 'Ticket medio (€)',
             'Compras de pescado (€)', 'Mermas (€)', 'Incidencias del día',
             'Firma'],
            7,
            ['Una línea por día de servicio. El ticket medio y el food cost '
             'de pescado del pie los calcula la hoja: tú sólo escribes '
             'ventas, comensales, compras y mermas.',
             'El food cost de pescado se calcula sobre las COMPRAS de la '
             'semana, que es lo que se puede medir sin inventario. Si haces '
             'inventario, sustitúyelo por consumo = existencias iniciales + '
             'compras − existencias finales.'],
            {'A': 5, 'B': 12, 'C': 14, 'D': 13, 'E': 14, 'F': 20, 'G': 13,
             'H': 40, 'I': 14},
            totales=[
                ('TOTAL de la semana',
                 {3: '=SUM(C5:C11)', 4: '=SUM(D5:D11)',
                  5: '=IF(SUM(D5:D11)=0,"",SUM(C5:C11)/SUM(D5:D11))',
                  6: '=SUM(F5:F11)', 7: '=SUM(G5:G11)'}),
                ('Food cost de pescado (% sobre ventas)',
                 {3: '=IF(SUM(C5:C11)=0,"",SUM(F5:F11)/SUM(C5:C11))'})]):
        cambios.append(f'hoja nueva «{HOJA_REPORTING}»: ventas, comensales, '
                       'ticket medio, compras, food cost y mermas con totales '
                       'de la semana — DOM-28 / COM-24 / TEC-20')
        tocado = True

    if _instrucciones(wb, 'Las dos hojas nuevas del manager', [
            f'«{HOJA_COMPARATIVA}»: el €/kg por especie y proveedor, semana a '
            'semana. Es el histórico con el que se negocia.',
            f'«{HOJA_REPORTING}»: una línea por día y el cierre de la semana '
            'calculado (ticket medio y food cost de pescado sobre ventas).',
            'Las tareas mensuales de mantenimiento no están aquí: van en '
            '07-semanales-mensuales.xlsx, y el arqueo de caja en '
            '01-apertura-cierre-sushi.xlsx.']):
        cambios.append('«Instrucciones» de 05: las dos hojas nuevas y dónde '
                       'están las tareas mensuales — COM-17 / COM-24')
    return tocado


# ==========================================================================
# 06 — perfiles: alérgenos, cocina caliente y DOS hojas nuevas
# ==========================================================================
HOJA_DELIVERY = 'Delivery y Take Away'
HOJA_OFFICE = 'Office y Lavado'

#: DOM-07 — la única tarea de alérgenos del kit enumeraba cuatro y omitía el
#: PESCADO, que es el alérgeno principal de un sushi bar.
ALERGENOS_06 = (
    'Informar de los 14 alérgenos del Anexo II del Rgto. (UE) 1169/2011; en '
    'carta japonesa vigilar sobre todo PESCADO, crustáceos, moluscos, soja y '
    'gluten (shoyu, panko, tempura, surimi), sésamo, huevo, sulfitos y frutos '
    'de cáscara. La matriz por plato está en el fichero 03')
#: DOM-31 + §7-bis.19 — la hoja de cocina caliente tenía 6 tareas y ninguna de
#: aceite, temperatura de servicio, enfriamiento ni alérgenos.
CALIENTE_06 = [
    ('Comprobar con sonda que las elaboraciones cocinadas alcanzan ≥70 °C en '
     'el centro (≥75 °C en aves, carne picada y recalentados)', 'Cocina',
     'Cocinero', 'Servicio'),
    ('Servir y mantener caldos, ramen y sopas a ≥65 °C; por debajo, regenerar '
     'o descartar', 'Cocina', 'Cocinero', 'Servicio'),
    ('Enfriar las elaboraciones que se guarden de 65 °C a 10 °C en menos de '
     '2 h (abatidor o baño de hielo) y etiquetar con fecha y hora', 'Cocina',
     'Cocinero', 'Cierre'),
    ('Filtrar el aceite de la freidora al cierre y cambiarlo cuando humee, '
     'espume o esté oscuro; anotar la fecha del cambio y entregar el usado a '
     'gestor autorizado', 'Cocina', 'Cocinero', 'Cierre'),
    ('No freír en el mismo aceite productos con gluten (panko, tempura) y '
     'productos sin gluten: el aceite arrastra el alérgeno', 'Cocina',
     'Cocinero', 'Servicio'),
]
DELIVERY = [
    ('  RECEPCIÓN Y PREPARACIÓN DEL PEDIDO', [
        ('Confirmar el pedido y anotar alérgenos y preferencias antes de '
         'montar nada', 'Barra sushi', 'Encargado sala', 'Al recibir'),
        ('Consultar la «Matriz de Alérgenos» del fichero 03 si el pedido '
         'declara un alérgeno', 'Barra sushi', 'Itamae', 'Al recibir'),
        ('Preparar el pedido lo más cerca posible de la hora de recogida: el '
         'sushi no espera montado', 'Barra sushi', 'Itamae', 'Al recibir'),
        ('Elaborar con guantes limpios y utensilio propio, sin cruzar con el '
         'servicio de barra', 'Barra sushi', 'Itamae', 'Al recibir'),
    ]),
    ('  MONTAJE, SELLADO Y ETIQUETADO', [
        ('Separar el arroz del pescado crudo y de las salsas en compartimentos '
         'o envases distintos', 'Barra sushi', 'Ayudante sushi',
         'Antes de salir'),
        ('Envasar con tapa y sellado íntegro; nada de film suelto ni bandejas '
         'abiertas', 'Barra sushi', 'Ayudante sushi', 'Antes de salir'),
        ('Etiquetar cada envase con el plato, la hora de preparación y los '
         'alérgenos que contiene (Rgto. (UE) 1169/2011)', 'Barra sushi',
         'Ayudante sushi', 'Antes de salir'),
        ('Meter en bolsa isoterma con acumulador de frío; jengibre, wasabi y '
         'palillos aparte', 'Barra sushi', 'Ayudante sushi',
         'Antes de salir'),
    ]),
    ('  SALIDA, ENTREGA E INCIDENCIAS', [
        ('Comprobar y anotar la temperatura del pedido al salir: el pescado '
         'crudo sale entre 0 y 4 °C — anota la lectura: ____ °C',
         'Barra sushi', 'Itamae', 'A la salida'),
        ('Entregar en 30 minutos o menos; si el reparto se alarga por encima '
         'de 60 minutos, avisar al cliente y no servir pescado crudo',
         'Sala', 'Encargado sala', 'A la salida'),
        ('Anotar la hora de salida y la de entrega para poder medir el tiempo '
         'real de reparto', 'Oficina', 'Encargado sala', 'A la salida'),
        ('Registrar la incidencia (retraso, envase abierto, plato erróneo) y '
         'lo que se ha hecho con el pedido devuelto', 'Oficina',
         'Encargado sala', 'Cierre'),
        ('Descartar cualquier pedido devuelto que haya estado fuera de '
         'refrigeración: no se reutiliza ni se sirve en barra', 'Barra sushi',
         'Itamae', 'Cierre'),
    ]),
]
OFFICE = [
    ('  LAVADO Y LAVAVAJILLAS', [
        ('Arrancar el lavavajillas y comprobar la temperatura de lavado '
         '(55-65 °C) y la de aclarado (≥80 °C) — anota la lectura: ____ °C',
         'Office', 'Office', 'Apertura'),
        ('Comprobar el nivel de detergente y abrillantador y anotar el cambio '
         'de garrafa', 'Office', 'Office', 'Apertura'),
        ('Limpiar filtros y brazos de aclarado y vaciar la cuba al menos una '
         'vez por servicio', 'Office', 'Office', 'Servicio'),
        ('Secar la vajilla al aire, nunca con paño: el paño reintroduce '
         'contaminación', 'Office', 'Office', 'Servicio'),
    ]),
    ('  MATERIAL DEL ITAMAE Y TABLAS', [
        ('Lavar a mano y secar de inmediato los cuchillos japoneses; NO van '
         'al lavavajillas', 'Barra sushi', 'Office', 'Cierre'),
        ('Lavar los makisu, retirar el film usado y guardarlos secos', 'Barra '
         'sushi', 'Office', 'Cierre'),
        ('Mantener las tablas separadas por uso (pescado crudo, cocinado y '
         'vegetal) y sumergirlas en solución desinfectante al cierre',
         'Barra sushi', 'Office', 'Cierre'),
        ('Retirar de servicio la vajilla desportillada o agrietada: no se '
         'puede higienizar', 'Office', 'Office', 'Cierre'),
    ]),
    ('  RESIDUOS Y CIERRE', [
        ('Separar residuos por fracción (orgánico, envases, papel, vidrio) y '
         'sacarlos a la hora que permita tu ordenanza', 'Office', 'Office',
         'Cierre'),
        ('Depositar el aceite usado en el bidón del gestor autorizado y '
         'guardar el documento de entrega', 'Cocina', 'Office', 'Cierre'),
        ('Limpiar y desinfectar el cubo, la zona de basuras y el sumidero',
         'Office', 'Office', 'Cierre'),
        ('Dejar el office seco y despejado y avisar de cualquier avería del '
         'lavavajillas', 'Office', 'Office', 'Cierre'),
    ]),
]


def _f06(wb, cambios):
    tocado = False
    ws = wb['Sala y Servicio']
    if _sustituir(ws, 'Informar a clientes sobre alergenos', ALERGENOS_06):
        cambios.append('«Sala y Servicio»: los 14 alérgenos del Anexo II del '
                       'Rgto. (UE) 1169/2011, con el PESCADO —que faltaba en '
                       'la lista de un sushi bar— y remisión a la matriz de '
                       '03 — DOM-07 / TEC-12')
    motor.renumerar(ws)

    ws = wb['Cocina Caliente']
    if _insertar_tras(ws, 'Control temperatura aceite fritura', CALIENTE_06):
        cambios.append('«Cocina Caliente»: 5 tareas nuevas (cocción ≥70 °C / '
                       '≥75 °C, mantenimiento ≥65 °C, enfriamiento rápido, '
                       'aceite y alérgenos en freidora) — DOM-31 / §7-bis.19')
        tocado = True
    motor.renumerar(ws)

    if _crear_checklist(wb, 'Sala y Servicio', HOJA_DELIVERY,
                        'Checklist: Delivery y Take Away', DELIVERY):
        cambios.append(f'hoja nueva «{HOJA_DELIVERY}»: la landing y el '
                       'dashboard prometen un perfil de delivery y el corpus '
                       'tenía 0 apariciones de «deliver|take away|reparto» — '
                       'DOM-06 / COM-06')
        tocado = True
    if _crear_checklist(wb, 'Sala y Servicio', HOJA_OFFICE,
                        'Checklist: Office y Lavado', OFFICE):
        cambios.append(f'hoja nueva «{HOJA_OFFICE}»: el fichero afirma que '
                       '«cada perfil tiene responsabilidades claras» y no '
                       'había perfil de office, que en un japonés maneja la '
                       'vajilla, las tablas y el material del itamae — '
                       'DOM-31')
        tocado = True

    if _instrucciones(wb, 'Perfiles nuevos: delivery y office', [
            f'«{HOJA_DELIVERY}» cubre el pedido para llevar de punta a punta: '
            'alérgenos, separación de arroz y pescado, sellado, etiquetado, '
            'bolsa isoterma, temperatura de salida, tiempo de entrega e '
            'incidencias.',
            f'«{HOJA_OFFICE}» cubre el lavado: temperaturas del lavavajillas, '
            'cuchillería japonesa a mano, tablas por uso, vajilla '
            'desportillada, residuos y aceite usado.',
            'Los alérgenos que sala tiene que saber decir están en la hoja '
            '«Matriz de Alérgenos» del fichero '
            '03-seguridad-anisakis-appcc.xlsx. ' + FUENTE_ALERGENOS,
            FUENTE_TEMPERATURAS]):
        cambios.append('«Instrucciones» de 06: los dos perfiles nuevos y el '
                       'criterio único de temperaturas, con su fuente — '
                       'DOM-06 / DOM-31 / §7-bis.19')
    return tocado


# ==========================================================================
# 07 — semanales y mensuales (§7-bis.21: una sola tabla de frecuencias)
# ==========================================================================
CALIBRACION_07 = ('Calibrar los termómetros y sondas contra un patrón conocido '
                  '(agua con hielo, 0 °C) y anotar la desviación')
FRIO_07 = ('Revisión MENSUAL del sistema de frío por el titular: temperaturas, '
           'juntas, escarcha y desagües (la revisión anual la hace la empresa '
           'frigorista)')
EXTINTOR_TRIM = ('Revisión TRIMESTRAL de extintores y BIE por el titular: '
                 'presión, precinto, accesibilidad y señalización '
                 '(RD 513/2017, RIPCI)')
EXTINTOR_ANUAL = [
    ('Revisión ANUAL de extintores por empresa mantenedora habilitada y '
     'retimbrado a los 5 años (RD 513/2017, RIPCI)', 'General', 'Mantenedor',
     'Anual'),
]
APPCC_07 = ('Auditoría interna MENSUAL de los registros APPCC y del archivo de '
            'congelación de anisakis (la auditoría anual completa está en el '
            'BONUS-02)')
HANGIRI_07 = [
    ('Sanitizar el hangiri según el plan de L+D: agua caliente, cepillo y '
     'desinfectante apto para uso alimentario, con aclarado abundante y '
     'secado al aire', 'Cocina', 'Ayudante sushi', 'Lunes'),
]


def _f07(wb, cambios):
    tocado = False
    ws = wb['Tareas Semanales']
    if _insertar_tras(ws, 'Desinfeccion tablas de corte', HANGIRI_07):
        cambios.append('«Tareas Semanales»: el hangiri entra en el plan de '
                       'L+D, que es lo que faltaba para poder retirar el '
                       '«NUNCA jabón» del cierre — DOM-26')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Tareas Mensuales']
    if _sustituir(ws, 'Calibracion termometros', CALIBRACION_07):
        cambios.append('«Tareas Mensuales»: la calibración de termómetros dice '
                       'CÓMO se calibra; la cadencia mensual se propaga al '
                       'BONUS-02 — COM-10 / §7-bis.21')
    if _sustituir(ws, 'Revision sistema de frio', FRIO_07):
        cambios.append('«Tareas Mensuales»: revisión de frío mensual del '
                       'titular + anual de la empresa, que son cosas '
                       'distintas — COM-10 / §7-bis.21')
    if _sustituir(ws, 'Verificar extintores', EXTINTOR_TRIM):
        cambios.append('«Tareas Mensuales»: la revisión del titular es '
                       'TRIMESTRAL, con su norma — COM-10 / §7-bis.21')
    if _insertar_tras(ws, EXTINTOR_TRIM, EXTINTOR_ANUAL):
        cambios.append('«Tareas Mensuales»: fila nueva para la revisión ANUAL '
                       'por empresa autorizada y el retimbrado a 5 años: son '
                       'DOS obligaciones, no una — COM-10 / §7-bis.21')
        tocado = True
    if _sustituir(ws, 'Auditar registros APPCC', APPCC_07):
        cambios.append('«Tareas Mensuales»: la auditoría mensual interna y la '
                       'anual completa quedan diferenciadas — COM-10')
    motor.renumerar(ws)

    if _instrucciones(wb, 'Frecuencias: una sola tabla para 07 y el BONUS-02', [
            'Calibración de termómetros: MENSUAL. Revisión del sistema de '
            'frío: mensual por el titular y anual por empresa frigorista.',
            'Extintores: revisión trimestral del titular y revisión anual por '
            'empresa mantenedora habilitada, con retimbrado a los 5 años. '
            + FUENTE_RIPCI,
            'Registros APPCC: auditoría interna mensual aquí y auditoría '
            'anual completa en el calendario del BONUS-02. Donde las dos '
            'hojas discrepaban, manda la más frecuente.']):
        cambios.append('«Instrucciones» de 07: tabla única de frecuencias con '
                       'la fuente del RIPCI — COM-10 / §7-bis.21')
    return tocado


# ==========================================================================
# 08 — eventos y temporadas
# ==========================================================================
#: DOM-09 / DOM-18 / COM-03 — bonito y atún rojo estaban CRUZADOS respecto a
#: las campañas españolas y respecto a lo que la propia landing afirma; la
#: sardina estaba en su peor momento (marzo, en desove) y la lubina salvaje en
#: otoño en vez de en invierno.
TEMPORADAS_08 = [
    ('Anotar disponibilidad: besugo, merluza, rape',
     'Anotar disponibilidad de invierno: besugo, merluza, rape, vieira y '
     'lubina salvaje (nov-mar)'),
    ('Negociar precio atun rojo de temporada',
     'Cerrar precio del atún rojo de almadraba ANTES de la campaña (abr-jun)'),
    ('Anotar disponibilidad: bonito, sardina, boqueron, sepia',
     'Anotar disponibilidad de primavera: atún rojo de almadraba (abr-jun), '
     'sepia y boquerón'),
    ('Menu primavera: piezas ligeras, sashimi de bonito',
     'Menú de primavera: piezas ligeras y sashimi de atún rojo de almadraba'),
    ('Anotar disponibilidad: atun rojo, pez espada, chipiron, gamba roja',
     'Anotar disponibilidad de verano: bonito del norte (jun-oct), sardina '
     '(jun-sep), pez espada, chipirón y gamba roja'),
    ('Carta verano: sushi frio, rolls con frutas tropicales',
     'Carta de verano: sushi frío, tataki de bonito del norte y rolls con '
     'fruta de temporada'),
    ('Anotar disponibilidad: gamba, langostino, calamar, lubina',
     'Anotar disponibilidad de otoño: gamba, langostino, calamar y bonito del '
     'norte hasta octubre'),
]
PREVALENCIA = [
    ('Sardina, boquerón y caballa tienen alta prevalencia de anisakis: '
     'congelación previa obligatoria antes de cualquier preparación cruda, '
     'marinada, en salazón o ahumada en frío', 'Cámara', 'Itamae', 'Junio'),
]
FESTIVOS_08 = [
    ('Hanami (finales de marzo a mediados de abril): menú de temporada y '
     'reservas de terraza', 'Oficina', 'Manager/Itamae', 'Marzo'),
    ('Tanabata (7 de julio): menú temático y decoración de sala', 'Sala',
     'Manager', 'Junio'),
    ('Cenas de empresa y comidas de Navidad: captación en octubre, servicio '
     'en noviembre y diciembre', 'Oficina', 'Manager', 'Octubre'),
    ('Día de la Madre (primer domingo de mayo): menú cerrado y doble turno',
     'Oficina', 'Manager', 'Abril'),
]


def _f08(wb, cambios):
    tocado = False
    hoja = ('Temporadas Pescado España'
            if 'Temporadas Pescado España' in wb.sheetnames
            else 'Temporadas Pescado Espana')
    ws = wb[hoja]
    n = 0
    for viejo, nuevo in TEMPORADAS_08:
        if _sustituir(ws, viejo, nuevo):
            n += 1
    if n:
        cambios.append(f'«{hoja}»: {n} líneas de temporada corregidas — el '
                       'bonito del norte va de junio a octubre y el atún rojo '
                       'de almadraba de abril a junio; el kit los tenía '
                       'cruzados y contradecía a su propia landing — DOM-09 / '
                       'DOM-18 / COM-03')
    r = _fila(ws, 'Negociar precio atun rojo', 2) or _fila(
        ws, 'Cerrar precio del atun rojo', 2)
    if r and ws.cell(row=r, column=5).value != 'Febrero':
        ws.cell(row=r, column=5).value = 'Febrero'
        cambios.append(f'«{hoja}»: el precio de la almadraba se cierra en '
                       'febrero, antes de la campaña — DOM-09')
    if _insertar_tras(ws, 'Anotar disponibilidad de verano', PREVALENCIA):
        cambios.append(f'«{hoja}»: aviso de prevalencia de anisakis en '
                       'sardina, boquerón y caballa, que se listaban como '
                       'disponibilidad sin una sola advertencia — DOM-18')
        tocado = True
    motor.renumerar(ws)

    ws = wb['Eventos Especiales']
    if _bloque_al_final(ws, '  FESTIVOS JAPONESES Y CENAS DE EMPRESA',
                        FESTIVOS_08):
        cambios.append('«Eventos Especiales»: bloque nuevo con Hanami, '
                       'Tanabata, cenas de empresa (el mayor pico del año, '
                       'que no estaba) y Día de la Madre — DOM-19 / COM-08')
        tocado = True
    motor.renumerar(ws)

    if _instrucciones(wb, 'De dónde salen estas temporadas', [
            FUENTE_TEMPORADAS,
            'Sardina, boquerón y caballa son las especies con mayor '
            'prevalencia de anisakis: pasan por congelación previa antes de '
            'cualquier uso crudo, marinado, en salazón o ahumado en frío. '
            + FUENTE_ANISAKIS,
            'El salmón que se sirve en sushi es de acuicultura y está '
            'disponible todo el año: no tiene temporada que calendarizar.']):
        cambios.append('«Instrucciones» de 08: fuente de las temporadas y '
                       'aviso de anisakis por especie — DOM-18 / COM-07')
    return tocado


# ==========================================================================
# BONUS-02 — calendario anual (hoja sin molde: se edita celda a celda)
# ==========================================================================
MESES = {'Ene': 2, 'Feb': 3, 'Mar': 4, 'Abr': 5, 'May': 6, 'Jun': 7,
         'Jul': 8, 'Ago': 9, 'Sep': 10, 'Oct': 11, 'Nov': 12, 'Dic': 13}
TODOS = list(MESES)

CAL_TEXTOS = [
    ('Besugo, merluza, rape (invierno)',
     'Besugo, merluza, rape, vieira y lubina salvaje (invierno)',
     ['Ene', 'Feb', 'Mar', 'Nov', 'Dic']),
    ('Bonito, sardina, boqueron (primavera)',
     'Atún rojo de almadraba, sepia y boquerón (primavera)',
     ['Abr', 'May', 'Jun']),
    ('Atun rojo, gamba roja (verano)',
     'Bonito del norte, sardina, pez espada y gamba roja (verano)',
     ['Jun', 'Jul', 'Ago', 'Sep', 'Oct']),
    ('Lubina, langostino, calamar (otono)',
     'Gamba, langostino y calamar (otoño)', ['Sep', 'Oct', 'Nov']),
    ('Halloween / otono tematico',
     'Cenas de empresa y comidas de Navidad (captación en octubre)',
     ['Oct', 'Nov', 'Dic']),
    ('Revision sistema de frio (tecnico)',
     'Revisión del sistema de frío por el titular (mensual)', TODOS),
    ('Calibracion termometros', 'Calibración de termómetros (mensual)', TODOS),
    ('Revision extintores y emergencia',
     'Revisión trimestral de extintores y BIE por el titular (RD 513/2017)',
     ['Mar', 'Jun', 'Sep', 'Dic']),
    ('Renovar registro sanitario',
     'Revisar los datos del RGSEAA y comunicar modificaciones o cese '
     '(no se renueva)', ['Ene']),
    ('Auditar registros APPCC anual',
     'Auditoría anual completa del plan APPCC (la mensual va en el 07)',
     ['Jun', 'Dic']),
]
#: DOM-19 / DOM-20 / COM-08 / COM-09 / §2.2 — lo que la landing promete y el
#: calendario no tenía: festivos asiáticos en plural, cierres por vacaciones y
#: las obligaciones anuales reales.
CAL_NUEVAS = [
    ('Hanami (menú de temporada y terraza)', ['Mar', 'Abr'],
     'Ano Nuevo japones'),
    ('Tanabata (7 de julio, menú temático)', ['Jul'], 'Ano Nuevo japones'),
    ('Día de la Madre (menú cerrado, doble turno)', ['May'],
     'Ano Nuevo japones'),
    ('Cierre por vacaciones / plantilla reducida', ['Ago', 'Dic'],
     'Ano Nuevo japones'),
    ('Planificar las vacaciones del equipo', ['Mar'], 'Ano Nuevo japones'),
    ('Revisión anual del sistema de frío por empresa frigorista', ['Mar'],
     'Calibracion termometros'),
    ('Revisión anual de extintores por empresa autorizada y retimbrado a los '
     '5 años (RD 513/2017)', ['Jun'], 'Calibracion termometros'),
    ('DDD (desinsectación y desratización) por empresa autorizada, con '
     'certificado', ['Mar', 'Sep'], 'Calibracion termometros'),
    ('Formación de manipuladores de alimentos', ['Feb', 'Sep'],
     'Formacion seguridad alimentaria'),
]


def _f_bonus02(wb, cambios):
    tocado = False
    ws = wb['Calendario Anual']
    n = 0
    for viejo, nuevo, meses in CAL_TEXTOS:
        r = _fila(ws, nuevo, 1)
        if r is None:
            r = _fila(ws, viejo, 1)
            if r is None:
                raise AnclaPerdida(f'«Calendario Anual»: no encuentro «{viejo}»')
            ws.cell(row=r, column=1).value = _est_texto(nuevo)
            n += 1
        for col in range(2, 14):
            ws.cell(row=r, column=col).value = None
        for m in meses:
            ws.cell(row=r, column=MESES[m]).value = '●'
    if n:
        cambios.append(f'«Calendario Anual»: {n} filas reescritas — '
                       'temporadas descruzadas, frecuencias alineadas con el '
                       '07 y el registro sanitario que «se renovaba» cada '
                       'enero — DOM-09 / DOM-19 / COM-03 / COM-10 / COM-21 / '
                       '§7-bis.21')
    for texto, meses, tras in CAL_NUEVAS:
        if _fila(ws, texto, 1) is not None:
            continue
        r = _exige(ws, tras, 1)
        est = _estilos(ws, r, 13)
        motor.insertar_filas(ws, r + 1, 1)
        _pintar(ws, r + 1, est)
        ws.cell(row=r + 1, column=1).value = _est_texto(texto)
        for col in range(2, 14):
            ws.cell(row=r + 1, column=col).value = None
        for m in meses:
            ws.cell(row=r + 1, column=MESES[m]).value = '●'
        tocado = True
    if tocado:
        cambios.append('«Calendario Anual»: filas nuevas de festivos '
                       'japoneses (Hanami, Tanabata), Día de la Madre, '
                       'CIERRE POR VACACIONES y planificación de vacaciones —'
                       ' prometidas en la landing y con 0 apariciones en los '
                       '11 ficheros —, más DDD, formación de manipuladores y '
                       'las revisiones anuales de frío y extintores — DOM-19 '
                       '/ DOM-20 / COM-08 / COM-09 / §2.2')

    ws = wb['Instrucciones']
    if _sustituir(ws, '▸ Marca con ✓ las tareas completadas cada mes',
                  '▸ El punto ● marca el mes en que toca cada tarea; escribe '
                  'encima la fecha real en que la hiciste, que es lo que '
                  'demuestra que se hizo', col=2, tarea=False):
        cambios.append('«Instrucciones» del BONUS-02: las casillas del mes ya '
                       'tienen el ● de planificación, así que marcar ✓ '
                       'destruiría el dato — TEC-13')
    if _instrucciones(wb, 'Cadencias de este calendario', [
            'Calibración de termómetros y revisión del sistema de frío por el '
            'titular: los doce meses, igual que en el fichero 07. Antes este '
            'calendario las marcaba dos veces al año y el 07 las pedía todos '
            'los meses.',
            FUENTE_RIPCI,
            FUENTE_RGSEAA,
            FUENTE_TEMPORADAS]):
        cambios.append('«Instrucciones» del BONUS-02: cadencias y fuentes — '
                       'COM-10 / COM-21 / §7-bis.21')
    return tocado


# ==========================================================================
# BONUS-01 — briefing (formulario: se edita celda a celda)
# ==========================================================================
BRIEF_NUEVAS = [
    ('Lote apto para crudo (nº de «Registro Congelación»): __________',
     'Nota general: __________'),
    ('Alérgeno crítico de hoy (pescado, crustáceos, moluscos, soja, gluten, '
     'sésamo, huevo, sulfitos, frutos de cáscara): __________',
     'Nota general: __________'),
    ('Pedido de pescado de mañana confirmado antes de la hora de corte: '
     '☐ Sí ☐ No', 'Nota equipo: __________'),
]


def _f_bonus01(wb, cambios):
    ws = wb['Briefing Servicio']
    tocado = False
    for texto, tras in BRIEF_NUEVAS:
        if _fila(ws, texto, 2) is not None:
            continue
        r = _exige(ws, tras, 2)
        est = [copy.copy(ws.cell(row=r, column=c)._style) for c in (1, 2, 3)]
        motor.insertar_filas(ws, r + 1, 1)
        for i, c in enumerate((1, 2, 3)):
            ws.cell(row=r + 1, column=c)._style = copy.copy(est[i])
        ws.cell(row=r + 1, column=2).value = _est_texto(texto)
        tocado = True
    if tocado:
        cambios.append('«Briefing Servicio»: líneas nuevas de lote apto para '
                       'crudo, alérgeno crítico del día y confirmación del '
                       'pedido — DOM-14 / DOM-24 / TEC-12')
    return tocado


# ==========================================================================
# Tablas que lee `main.py` (gates propios de este kit)
# ==========================================================================
#: Gate `promesas` (§1.3). Cada término distintivo del grid, del CTA o de los
#: bonus de `astro-site/src/data/productos/tareas/kit-tareas-sushi-bar.ts` con
#: el fichero donde tiene que aparecer. `fichero=None` = en cualquiera.
#: FUERA a propósito: «salmón salvaje» (líneas 151 y 231), que NO es corregible
#: en el fichero —en España no hay temporada comercial de salmón salvaje— y se
#: arregla en la capa de producto (§3.3, COM-07).
PROMESAS = [
    {'termino': 'arqueo', 'rx': r'(?i)arqueo',
     'fichero': '01-apertura-cierre-sushi.xlsx',
     'origen': 'kit-tareas-sushi-bar.ts:116 grid.templates[0] «cierre completo y arqueo»'},
    {'termino': 'maki', 'rx': r'(?i)\bmaki\b',
     'fichero': '02-preparacion-arroz-pescado.xlsx',
     'origen': 'kit-tareas-sushi-bar.ts:121 grid.templates[1] «nigiri y maki»'},
    {'termino': 'alérgenos', 'rx': r'(?i)al[eé]rgeno',
     'fichero': '03-seguridad-anisakis-appcc.xlsx',
     'origen': 'kit-tareas-sushi-bar.ts:126 grid.templates[2] «alérgenos»'},
    {'termino': 'lote (FIFO por lotes)', 'rx': r'(?i)\blote',
     'fichero': '04-barra-sushi-neta-case.xlsx',
     'origen': 'kit-tareas-sushi-bar.ts:131 grid.templates[3] «rotación FIFO por lotes»'},
    {'termino': 'comparativa de proveedores', 'rx': r'(?i)comparativa',
     'fichero': '05-tareas-manager.xlsx',
     'origen': 'kit-tareas-sushi-bar.ts:136 grid.templates[4]'},
    {'termino': 'reporting', 'rx': r'(?i)reporting',
     'fichero': '05-tareas-manager.xlsx',
     'origen': 'kit-tareas-sushi-bar.ts:136 grid.templates[4]'},
    {'termino': 'delivery / take away', 'rx': r'(?i)(delivery|take away)',
     'fichero': '06-tareas-perfiles.xlsx',
     'origen': 'kit-tareas-sushi-bar.ts:141 grid.templates[5] y :286 cta.items[4]'},
    {'termino': 'festivos asiáticos (≥2)', 'rx': r'(?i)(hanami|tanabata|oshogatsu|a[ñn]o nuevo japon)',
     'fichero': None, 'minimo': 2,
     'origen': 'kit-tareas-sushi-bar.ts:151 y :287 «festivos asiáticos» (plural)'},
    {'termino': 'cierres por vacaciones', 'rx': r'(?i)vacacion',
     'fichero': 'BONUS-02-calendario-anual.xlsx',
     'origen': 'kit-tareas-sushi-bar.ts:166 y :231 bonus.items[1]'},
    {'termino': 'omakase', 'rx': r'(?i)omakase', 'fichero': None,
     'origen': 'kit-tareas-sushi-bar.ts:136 y :287'},
    {'termino': 'mermas', 'rx': r'(?i)merma', 'fichero': None,
     'origen': '§2.2 — sostiene el argumento «€14 frente a €40/mes»'},
]

#: Gate `limite_unico` (§7-bis.23, ABORTA). Un equipo con dos rangos distintos
#: en el mismo kit es exactamente el defecto que se viene a arreglar.
EQUIPOS_LIMITE = [
    ('cámara de pescado crudo', r'(?i)c[áa]mara (de )?(el )?pescado crudo'),
    ('cámara de congelación de anisakis',
     r'(?i)c[áa]mara (de )?congelaci[óo]n (de )?anisakis'),
    ('vitrina neta case', r'(?i)vitrina( neta case)?'),
    ('congelador general', r'(?i)congelador general'),
    ('cámara de refrigeración general', r'(?i)c[áa]mara (de )?refrigeraci[óo]n general'),
    ('aceite de fritura', r'(?i)aceite (de )?fritura'),
    ('arroz de servicio', r'(?i)arroz de servicio'),
]

#: Demostración CB-E2: la plantilla en blanco con 8 tareas escritas.
PLANTILLA_09 = {'fichero': '09-plantilla-personalizable.xlsx',
                'hoja': 'Plantilla en Blanco', 'tareas': 8, 'marcadas': 3}


# ==========================================================================
# Entrada
# ==========================================================================
_FICHEROS = {
    '01-apertura-cierre-sushi.xlsx': _f01,
    '02-preparacion-arroz-pescado.xlsx': _f02,
    '03-seguridad-anisakis-appcc.xlsx': _f03,
    '04-barra-sushi-neta-case.xlsx': _f04,
    '05-tareas-manager.xlsx': _f05,
    '06-tareas-perfiles.xlsx': _f06,
    '07-semanales-mensuales.xlsx': _f07,
    '08-eventos-estacionales.xlsx': _f08,
    'BONUS-01-briefing-servicio.xlsx': _f_bonus01,
    'BONUS-02-calendario-anual.xlsx': _f_bonus02,
}


def post(wb, fname, cambios):
    """True si ha cambiado la ESTRUCTURA del libro (filas u hojas nuevas)."""
    fn = _FICHEROS.get(fname)
    if fn is None:
        return False
    return bool(fn(wb, cambios))
