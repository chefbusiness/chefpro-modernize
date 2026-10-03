#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
enmiendas_churreria.py — enmiendas al CONTRATO de cruces (`datos_ejemplo.CRUCES`)
que pide la refutación de los 8 libros (auditorias/guia-churreria-xlsx-refutacion-
2026-10-03.md: R-04, R-05, R-06, R-13, R-14 y R-15).

POR QUÉ UN MÓDULO APARTE. Esos hallazgos necesitan cambiar `CRUCES`, y `CRUCES`
vive en `datos_ejemplo.py`, que en esta tanda no se toca. Este módulo aplica las
enmiendas EN MEMORIA, justo después de importar `datos_ejemplo`, y es lo único
que los 8 generadores y `gate_libros.py` leen: todos ven el MISMO contrato. Para
integrarlas en `datos_ejemplo.py` basta copiar `CRUCES_NUEVOS` (mismo formato que
`_ESPEC_CRUCES`), borrar los `CRUCES_QUITADOS` y sustituir `_pct_sala` por
`_pct_sala_fraccion`; entonces este módulo deja de hacer nada (es idempotente).

QUÉ CAMBIA (cada punto, con su hallazgo):

* R-05a  X1 bis   3 -> 1  kg fritos por kg de masa (era una verde propia en el 1 y
                           otra en el 3: un concepto, una fuente).
* R-05c  X9 bis   1 -> 2  superficie útil del local (verde propia en el 1 y en el 2).
* R-05b  X17      3 -> 2  los precios de los 12 insumos del stock inicial (el 2 los
                           volvía a teclear; sólo el aceite y el mix viajaban).
* R-04   X10 bis  2 -> 6  partidas del CAPEX que no se amortizan (entraban en el 6
                           como verde SIN rótulo ni CUADRE: cruce no declarado).
* R-06   X16 bis  5 -> 6  la contribución de julio y agosto de LAS TRES salidas
                           (el 6 sólo recibía la elegida y no podía enseñar el
                           «verano con fijos» de cada una).
* R-13   X16 ter  5 -> 6  las ventas sin IVA de julio y agosto de la salida elegida
                           (el 6 valoraba el verano con el ticket de invierno).
* R-14   X11      3 -> 6  el % de sala viaja como FRACCIÓN (0,70 con formato 0,0 %),
                           no como 70: sin la constante «Cien» en el 6.
* R-15   X7       5 -> 8  se QUITAN las cuatro horas de franja (sólo alimentaban una
                           suma de control y una presentación; el lector copiaba
                           cuatro cifras sin que moviesen ningún cálculo). Queda la
                           de las horas de refuerzo, que sí valora el coste de plantilla.
                 X2 bis  3 -> 4  se CONSERVA: el libro 4 la usa ahora para dar litros
                           y euros de aceite POR KILO DE MASA.

Las aristas no cambian: todas las nuevas viajan por aristas que ya existían
(3->1, 1->2, 3->2, 2->6, 5->6) y 5->8 sigue viva por las horas de refuerzo.

Via: Claude Code
"""
import re

#: Los 12 insumos del stock inicial cuyo precio ya no se teclea en el libro 2.
#: (Son los de `STOCK_INICIAL` menos el aceite y el mix, que ya viajaban por X17.)
INSUMOS_STOCK_X17 = ('preparado_taza', 'cobertura', 'cucurucho', 'vaso_llevar',
                     'papel_antigrasa', 'caja_kilo', 'cafe', 'leche', 'azucar',
                     'cacao_soluble', 'infusion', 'agua')

#: Horas de franja que dejan de viajar del 5 al 8 (R-15).
CRUCES_QUITADOS = ('_horas_desayuno', '_horas_media', '_horas_merienda', '_horas_noche')

#: (x, origen, receptor, concepto, unidad, hoja de origen, celda, función)
#: Mismo formato que `datos_ejemplo._ESPEC_CRUCES`. Las celdas de origen siguen el
#: contrato: rótulo en K y valor en L, desde la fila 5, en el orden de esta lista y
#: DESPUÉS de las que ya existían en esa hoja.
CRUCES_NUEVOS = [
    ('X1 bis', 3, 1, 'Kilos fritos que salen de un kilo de masa', 'kg/kg',
     'Parámetros', 'L9', '_kg_fritos_por_kg_masa'),
    ('X9 bis', 1, 2, 'Superficie útil del local', 'm²',
     'Zonas y m²', 'L5', '_m2_total'),
] + [
    ('X17', 3, 2, 'Precio del insumo «%s» del stock inicial (base imponible)' % k, '€/unidad',
     'Parámetros', 'L%d' % (10 + i), '_precio_insumo_' + k)
    for i, k in enumerate(INSUMOS_STOCK_X17)
] + [
    ('X10 bis', 2, 6, 'CAPEX que no se amortiza (fianza, stock inicial y marketing)', '€',
     'Resumen', 'L6', '_capex_no_amortizable'),
    ('X16 bis', 5, 6, 'Contribución de julio y agosto si cierras', '€',
     'El Verano (Tres Salidas)', 'L6', '_contribucion_verano_cerrar'),
    ('X16 bis', 5, 6, 'Contribución de julio y agosto con carta de verano', '€',
     'El Verano (Tres Salidas)', 'L7', '_contribucion_verano_carta'),
    ('X16 bis', 5, 6, 'Contribución de julio y agosto con ferias', '€',
     'El Verano (Tres Salidas)', 'L8', '_contribucion_verano_ferias'),
    ('X16 ter', 5, 6, 'Ventas sin IVA de julio y agosto de la salida elegida', '€',
     'El Verano (Tres Salidas)', 'L9', '_ventas_verano_elegida'),
]


def aplicar(D):
    """Aplica las enmiendas a `D` (el módulo `datos_ejemplo` ya importado). Idempotente."""
    if getattr(D, '_ENMIENDAS_CHURRERIA', False):
        return D

    # --- funciones de una línea que dan el valor de los cruces nuevos ---------------
    D._kg_fritos_por_kg_masa = lambda: D.P('kg_fritos_por_kg_masa')
    D._m2_total = lambda: D.dato(D.NEGOCIO, 'm2_total')
    for k in INSUMOS_STOCK_X17:
        setattr(D, '_precio_insumo_' + k, (lambda clave: (lambda: D.precio_insumo(clave)))(k))
    D._capex_no_amortizable = lambda: D.capex_total() - D.capex_amortizable()
    D._contribucion_verano_cerrar = lambda: D.contribucion_verano('cerrar')
    D._contribucion_verano_carta = lambda: D.contribucion_verano('carta de verano')
    D._contribucion_verano_ferias = lambda: D.contribucion_verano('ferias')
    D._ventas_verano_elegida = lambda: D.raciones_verano() * D.ticket_sin_iva('verano')
    # R-14: el % de sala viaja como fracción. `_pct_sala()` (en %) se queda tal cual
    # porque el texto de la decisión 1 del bonus 2 lo usa.
    D._pct_sala_fraccion = lambda: D.pct_raciones('sala')

    # --- R-15: fuera las cuatro horas de franja; R-14: otra función para el % ------
    D.CRUCES[:] = [c for c in D.CRUCES if c['calcula'] not in CRUCES_QUITADOS]
    for c in D.CRUCES:
        if c['calcula'] == '_pct_sala':
            c['calcula'] = '_pct_sala_fraccion'
            c['concepto'] = 'Raciones en sala, en fracción (0,70 = 70 %; el resto, para llevar)'
            c['unidad'] = '%'

    # --- cruces nuevos ---------------------------------------------------------------
    for (x, o, r, concepto, unidad, hoja, celda, fn) in CRUCES_NUEVOS:
        D.CRUCES.append({'n': 0, 'x': x, 'origen': o, 'receptor': r, 'concepto': concepto,
                         'unidad': unidad, 'fichero_origen': D.LIBROS[o], 'hoja_origen': hoja,
                         'celda_origen': celda, 'fichero_receptor': D.LIBROS[r],
                         'hoja_receptor': D._RECEPTORA[r], 'calcula': fn, 'valor_defecto': None})
    for n, c in enumerate(D.CRUCES, 1):
        c['n'] = n

    D._rellenar_valores_cruces()
    if D._ERROR_CRUCES:
        raise SystemExit('enmiendas_churreria: datos_ejemplo no pudo calcular los cruces: %s'
                         % D._ERROR_CRUCES)
    # contrato: una celda de origen, una cifra
    vistas = {}
    for c in D.CRUCES:
        clave = (c['fichero_origen'], c['hoja_origen'], c['celda_origen'])
        if vistas.setdefault(clave, c['calcula']) != c['calcula']:
            raise SystemExit('enmiendas_churreria: la celda %s!%s!%s lleva dos cifras' % clave)
    # las aristas no pueden salirse de las quince de §2.2
    if D.aristas() != D.ARISTAS_SPEC:
        raise SystemExit('enmiendas_churreria: aristas fuera de §2.2: %s'
                         % sorted(D.aristas() ^ D.ARISTAS_SPEC))
    # --- R-07, R-08 y R-09 (notas legales): lo que lee el comprador no nombra lo vetado ------
    _orig_nota = D.nota_legal

    def nota_legal(pid):
        propia = _nota_propia(D, pid)
        if propia:
            return propia
        texto = _orig_nota(pid)
        if texto and RX_NOTA_INTERNA.search(texto):
            # la ficha trae una frase del analista («PROHIBIDO ...»): se queda sólo norma y URL
            fila = D._carga_lista(D.VERIFICACION_LEGAL_CUN if pid.startswith('CUN-')
                                  else D.VERIFICACION_LEGAL_CHN).get(pid) or {}
            fecha = D.FECHA_VERIFICACION_CUN if pid.startswith('CUN-') else D.FECHA_VERIFICACION_CHN
            norma = re.sub(r'\s+', ' ', (fila.get('fuente_titulo') or '').strip())
            texto = 'Verificado el %s %s %s %s %s' % (fecha, MID, norma, MID, (fila.get('url') or '').strip())
        return texto

    D.nota_legal = nota_legal
    D._ENMIENDAS_CHURRERIA = True
    return D


MID = chr(183)
#: Frases del analista que no pueden llegar a una nota que lee el comprador.
RX_NOTA_INTERNA = re.compile(r'PROHIBIDO|\bSR-\d|\bV-\d{2}\b|datos_ejemplo|rama [AB]\b')


def _nota_propia(D, pid):
    """Notas que se escriben a mano porque la que arma `datos_ejemplo.nota_legal()` con la
    ficha publica algo que el producto no puede decir (R-07, R-08, R-09)."""
    if pid not in ('CUN-03', 'CUN-10', 'CUN-19'):
        return None
    fila = D._carga_lista(D.VERIFICACION_LEGAL_CUN).get(pid) or {}
    url = (fila.get('url') or '').strip()
    if not url:
        return None
    f = D.FECHA_VERIFICACION_CUN
    if pid == 'CUN-03':
        norma = ('Orden de 26 de enero de 1989 por la que se aprueba la Norma de Calidad para los '
                 'Aceites y Grasas Calentados (BOE-A-1989-2265), texto consolidado, art. 9 (vigente: '
                 'los arts. 7, 8, 10, 11 y 12 los derogó el Real Decreto 176/2013, art. 46)')
    elif pid == 'CUN-10':
        norma = ('Real Decreto Legislativo 1175/1990, de 28 de septiembre, por el que se aprueban las '
                 'tarifas y la instrucción del Impuesto sobre Actividades Económicas '
                 '(BOE-A-1990-23930), epígrafe 676 «Servicios en chocolaterías, heladerías y '
                 'horchaterías»')
    else:
        norma = ('Real Decreto 199/2010, de 26 de febrero, por el que se regula el ejercicio de la '
                 'venta ambulante o no sedentaria (BOE-A-2010-4173), apartado «Fecha de derogación»: '
                 '07/08/2021, derogado por el Real Decreto 538/2021')
    return 'Verificado el %s %s %s %s %s' % (f, MID, norma, MID, url)


# ==========================================================================================
# R-09: el texto interno de la fábrica no llega al comprador
# ==========================================================================================
#: Lo que el comprador de un producto de 65 € no debe leer: rutas de ficheros de OTRO producto,
#: nombres de funciones, códigos de decisión/hallazgo («D16», «SR-04», «V-01, rama A»), el
#: «PROHIBIDO» de la verificación legal y los slugs de otros productos. El libro 3 ya lo limpiaba
#: con `NOTAS_PUBLICAS`; esto lo hace igual para los otros siete, sobre el libro YA construido y
#: antes de guardarlo (no toca fórmulas ni la lógica: sólo cadenas de texto y comentarios).
HEREDADO = 'heredado de la Guía de la Chocolatería (supuesto declarado)'
SUSTITUCIONES = (
    (re.compile(r'heredado de la hermana o del motor \(guia-chocolateria/[^)]*\)'), HEREDADO),
    (re.compile(r'heredado: guia-chocolateria/[\w./\-]+\.py(?: [\w\[\]\-,() ]*?\])?'), HEREDADO),
    (re.compile(r'heredado: guia-chocolateria \(([^)]*)\)'),
     lambda m: 'heredado de la Guía de la Chocolatería (%s)' % (m.group(1)[:1].lower() + m.group(1)[1:])),
    (re.compile(r'calculado en datos_ejemplo: [\w()]+'), 'calculado'),
    (re.compile(r'heredado: datos_ejemplo\.[\w()]+ \(centenas\)'), 'calculado (redondeado a centenas)'),
    (re.compile(r'heredado: datos_ejemplo\.[\w()]+'), 'calculado'),
    (re.compile(r'\s*\((?:SR-\d+|V-\d+|N-\d+|D-?\d+|A\d+)(?:,[^)]*)?\)'), ''),
    (re.compile(r'plan-negocio-food-truck, kit-tareas-food-truck'),
     'Plan de Negocio: Food Truck, Tareas: Food Truck'),
    (re.compile(r'plan-negocio-cafeteria'), 'Plan de Negocio: Cafetería'),
    (re.compile(r'pack-appcc/(09-control-aceite-fritura\.xlsx)!(Control Aceite|Retirada de aceite usado)'),
     r'Pack Plantillas APPCC, fichero \1, hoja «\2»'),
)
#: Lo que NO puede quedar en ninguna cadena del libro (el gate de cierre y `gate_libros.py`).
RX_INTERNO = re.compile(
    r"\b(?:SR|V|N|D|A)-?\d+\b|datos_ejemplo|guia-chocolateria/|PROHIBIDO|rama [AB]\b|\(\w+\(\)\)"
    r"|heredado: guia|calculado en|pack-appcc|plan-negocio-|kit-tareas|\bkit-[a-z]|guia-[a-z]+-[a-z]+")
RX_ID_FUENTE = re.compile(r'\b(?:CHN|CHS|CUN|CUS|FC-IVA)-(?:[MVD])?[0-9]+[a-z]*\b')


def texto_publico(texto):
    for rx, nuevo in SUSTITUCIONES:
        texto = rx.sub(nuevo, texto)
    return texto


def interno_en(texto):
    """Lo que queda de interno en una cadena (vacío si está limpia). Los ids de fuente
    (`CUS-D6`), las URL, los códigos del BOE, los números de consulta de la DGT, las celdas
    (`Hoja!B41`) y la URL del producto no son texto interno."""
    t = RX_ID_FUENTE.sub('', texto)
    t = re.sub(r'https?://\S+', '', t)
    t = re.sub(r'aichef\.pro/[\w\-/]+', '', t)
    t = re.sub(r'BOE-[A-Z]-\d{4}-\d+', '', t)
    t = re.sub(r'\bV\d{4}-\d{2}\b', '', t)
    t = re.sub(r'![A-Z]{1,2}\d+', '', t)
    t = re.sub(r'\bRD \d+/\d+', '', t)
    return [m.group(0) for m in RX_INTERNO.finditer(t)]


def sanear_libro(wb):
    """Reescribe, en el libro YA construido y antes de guardar, las cadenas y comentarios con texto
    interno. Devuelve cuántas celdas ha tocado."""
    from openpyxl.comments import Comment
    n = 0
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.__class__.__name__ == 'MergedCell':
                    continue
                v = c.value
                if isinstance(v, str) and not v.startswith('='):
                    nv = texto_publico(v)
                    if nv != v:
                        c.value = nv
                        n += 1
                if c.comment is not None:
                    ct = c.comment.text
                    nt = texto_publico(ct)
                    if nt != ct:
                        old = c.comment
                        c.comment = Comment(nt, old.author, height=old.height, width=old.width)
                        n += 1
    return n
