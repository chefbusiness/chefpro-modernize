#!/usr/bin/env python3
"""
grupo_a.py — §2 de `guias-v2-SPEC.md`: las **plantillas financieras** de la
familia «Guías Cómo Montar» v2.0.

Ficheros (§2): `calculadora-ticket-medio.xlsx`, `pl-mensual-escenarios.xlsx`,
`plan-financiero-3-anos.xlsx`, `cash-flow-break-even.xlsx` y
`calculadora-capex.xlsx`, en las **7** guías que los llevan.
`guia-dark-kitchen` NO entra: su `calculadora-viabilidad-dark-kitchen.xlsx`
ya calcula y **sólo recibe §1** (SPEC §2, cabecera) — por eso `ficheros()` es
una función y devuelve `[]` para ese pid.

REGLA DE FAMILIA (la razón de ser de este módulo): **nada por posición fija sin
comprobar la etiqueta**. Medido el 2026-08-29 abriendo los ficheros vivos:

  · `pl-mensual-escenarios!'Pesimista'!EBITDA` está en la fila **30** en casual
    y en la **31** en japonés; el `'P&L Mensual'` de `plan-financiero` tiene
    `TOTAL COSTES FIJOS` en la **28** (casual) y en la **29** (japonés).
  · `calculadora-ticket-medio` tiene **tres** rejillas distintas: 3 escenarios
    en columnas B/C/D (representante), una sola columna B con pares %/precio
    (5 hermanos) y una tabla de **mix de producto** con `PVP €` / `Mix % ventas`
    / `Aporte €` (panadería).
  · `cash-flow-break-even` tiene **tres**: `Cash Flow 12 Meses` con columna de
    total (representante), `Cash Flow` + `Break-Even` (hermanos) y
    `Cash Flow 24m` (panadería).
  · `calculadora-capex` tiene **tres**: rangos bajo/medio/alto (representante),
    `CAPEX Desglosado` con `#`/`Categoría`/`Partida` (hermanos) e
    `Importe Mínimo`/`Importe Máximo` (panadería).

Por eso cada fichero se resuelve en dos pasos: **(1) detectar la variante por
firma estructural** —y **abortar** con `VarianteDesconocida` si no encaja, nunca
«aplica la del representante»— y **(2) localizar cada fila por su ETIQUETA**
(`_fila()`, sin acentos y por regex). Lo que cambia de guía a guía —cifras de
ejemplo, mapa de conceptos, notas— vive en `contenido_<pid>/a.py` y llega por el
parámetro `contenido`; este módulo no teclea ni un importe del oficio.

Qué implementa, por id de la SPEC:
  §2.1  TEC-01/DOM-08/COM-04 — el ticket medio se calcula (ponderado por mix),
        con fila de control «% de comensales asignado» y facturación día/mes.
  §2.2  TEC-02/DOM-07/COM-05 + §7-bis.14 — P&L de 3 escenarios ENCADENADO, en
        las tres variantes, con el «Pesimista» recalibrado (malo, no inviable).
  §2.3  TEC-07/08/09/10, DOM-06/22/26/27, COM-07 — hoja «Proyección 3 Años»
        nueva, EBITDA que NO resta amortización + EBIT, hoja «Financiación» con
        cuadro francés (anualidad algebraica: pycel no implementa `PMT`), fondo
        de maniobra dimensionado (≥ 6 meses) y la correspondencia 22→12 del
        CAPEX (§2.3.6).
  §2.4  TEC-03/DOM-09/COM-06 — totales, flujo neto, acumulado, las tres filas
        de IVA del modelo 303, la cuota del préstamo y el break-even en meses
        y en €.
  §2.5  NUEVO-01 (el `P&L Mensual` de los 5 hermanos sin ni un total) y
        NUEVO-02 (panadería: EBITDA = facturación, margen 122,97 %).
  §7-bis.13 — «sin dato» se escribe `""`, **nunca `0`**: con el libro en blanco
        ningún margen dice «0,0 %» ni se enciende un semáforo.

Lo que NO hace (§1.13/§7.1): no crea ficheros, no renombra, no escribe
`externalLink` entre libros (la cuota del préstamo se REPITE en el cash flow
como celda verde con la nota de dónde sale), no toca `paperSize` de las hojas
que ya existen —a las que CREA sí les pone el A4 completo, o `demo_a4` las
contaría como `noprint`— y no borra ninguna fila que el cliente pueda haber
rellenado.

⚠️ U+202F (espacio fino) y U+2011 (guion no separable) se referencian por
escape desde `motor.NARROW` / `motor.NOBRK`, nunca escribiendo el carácter.
"""
import re
import unicodedata

from openpyxl.styles import Alignment, Font
from openpyxl.worksheet.page import PageMargins
from openpyxl.worksheet.properties import PageSetupProperties

import motor
from motor import FMT_ENT, FMT_EUR, FMT_PCT

SPEC = 'guias-v2-SPEC.md §2'

FICHEROS = ['calculadora-ticket-medio.xlsx',
            'pl-mensual-escenarios.xlsx',
            'plan-financiero-3-anos.xlsx',
            'cash-flow-break-even.xlsx',
            'calculadora-capex.xlsx']

#: `motor.aplicar`/`motor.cerrar` se aplican a los cinco: el grupo sólo añade.
PROPIOS = []

#: `guia-dark-kitchen` no tiene ninguno de los cinco. Sin esta guarda,
#: `main.ficheros_a_tocar()` añadiría los cinco nombres a la lista de trabajo y
#: `procesar()` intentaría abrir un fichero que no existe.
SIN_GRUPO_A = ('guia-dark-kitchen',)


def ficheros(ctx):
    pid = (ctx or {}).get('producto')
    return [] if pid in SIN_GRUPO_A else list(FICHEROS)


class VarianteDesconocida(Exception):
    """§1.1/§7-bis.11 aplicado al grupo A: el módulo NO adivina una rejilla."""


# ==========================================================================
# Localización por ETIQUETA (nunca por posición fija)
# ==========================================================================
def _sin_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                   if unicodedata.category(c) != 'Mn')


def _norm(v):
    """Etiqueta normalizada: sin acentos, sin dobles espacios, en minúscula.

    También normaliza el ESPACIO FINO (U+202F) y el GUION NO SEPARABLE (U+2011)
    de la familia a sus equivalentes normales: un `.md`/`.xlsx` de esta familia
    puede traerlos y un patrón escrito con espacio normal no encontraría nada.
    """
    if not isinstance(v, str):
        return ''
    t = v.replace(motor.NARROW, ' ').replace(motor.NOBRK, '-')
    t = _sin_acentos(t).lower()
    return re.sub(r'\s+', ' ', t).strip()


def etiquetas(ws, col=1, desde=1, hasta=None):
    """[(fila, etiqueta normalizada, etiqueta cruda)] de una columna."""
    fuera = []
    tope = hasta or ws.max_row
    for r in range(desde, tope + 1):
        v = ws.cell(row=r, column=col).value
        if isinstance(v, str) and v.strip():
            fuera.append((r, _norm(v), v))
    return fuera


def _fila(ws, patron, col=1, desde=1, hasta=None, obligatoria=True,
          fname='', saltar=()):
    """Primera fila cuya etiqueta case con `patron` (regex, ya normalizado).

    Devuelve la PRIMERA coincidencia de arriba abajo: es lo que hace estable la
    2.ª pasada cuando el grupo ha añadido más abajo una etiqueta parecida (p. ej.
    `FLUJO DE CAJA NETO` en la fila 21 y `FLUJO DE CAJA NETO CON IVA Y DEUDA` en
    la 30). `saltar` excluye filas concretas por si la etiqueta nueva es un
    prefijo exacto de la vieja.
    """
    rx = re.compile(patron)
    for r, norm, _crudo in etiquetas(ws, col, desde, hasta):
        if r in saltar:
            continue
        if rx.search(norm):
            return r
    if obligatoria:
        raise VarianteDesconocida(
            (fname + ':' if fname else '') + ws.title + ': no hay ninguna fila '
            'cuya etiqueta case con ' + repr(patron) + ' en la columna '
            + str(col) + '. El grupo A NO escribe por posición fija: revisa la '
            'rejilla o añade el patrón en contenido_<pid>/a.py.')
    return None


RX_MES = re.compile(r'^(mes\s*\d+|m\d+|ene|feb|mar|abr|may|jun|jul|ago|sep|'
                    r'set|oct|nov|dic|enero|febrero|marzo|abril|mayo|junio|'
                    r'julio|agosto|septiembre|octubre|noviembre|diciembre)$')
RX_TOTAL_COL = re.compile(r'^(total|total anual|anual|ano \d|total ano)')


def columnas_mes(ws, fila_cab):
    """(columnas de mes, columna de total) leídas de la CABECERA.

    Representante: `Mes 1`…`Mes 12` + `Total Anual`. Hermanos: `Ene`…`Dic` sin
    columna de total. Panadería: `M1`…`M12` + `Año 1` + `Año 2`. Tres rejillas,
    una sola lectura.
    """
    from openpyxl.utils import get_column_letter as gcl
    meses, totales = [], []
    for c in range(2, ws.max_column + 1):
        cab = _norm(ws.cell(row=fila_cab, column=c).value)
        if RX_MES.match(cab):
            meses.append(gcl(c))
        elif RX_TOTAL_COL.match(cab):
            totales.append(gcl(c))
    return meses, (totales[0] if totales else None)


def _a4(ws):
    """A4 completo en una hoja NUEVA (§1.13: el motor protege las que ya
    existían, no las que no existen; sin esto `demo_a4` la cuenta `noprint`)."""
    ws.page_setup.paperSize = 9
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    if ws.sheet_properties.pageSetUpPr is None:
        ws.sheet_properties.pageSetUpPr = PageSetupProperties()
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins = PageMargins(left=0.59, right=0.59, top=0.59,
                                  bottom=0.59, header=0.3, footer=0.3)
    ws.oddFooter.center.text = 'AI Chef Pro · aichef.pro · Página &P de &N'
    ws.oddFooter.center.size = 8


def hoja(wb, nombre, tras=None):
    """Hoja `nombre`, creándola (con A4) si falta. Idempotente."""
    if nombre in wb.sheetnames:
        return wb[nombre], False
    indice = None
    if tras and tras in wb.sheetnames:
        indice = wb.sheetnames.index(tras) + 1
    ws = wb.create_sheet(nombre) if indice is None \
        else wb.create_sheet(nombre, indice)
    _a4(ws)
    return ws, True


def cabecera(ws, titulo, subtitulo, columnas, fila=4, ancho_a=44):
    """Título + subtítulo + fila de cabecera con el molde de la familia."""
    motor.val(ws, 'A1', titulo, bold=True)
    ws['A1'].font = Font(bold=True, size=14)
    motor.val(ws, 'A2', subtitulo)
    ws['A2'].font = Font(italic=True, size=9)
    from openpyxl.utils import get_column_letter as gcl
    for i, texto in enumerate(columnas):
        cel = ws.cell(row=fila, column=i + 1, value=texto)
        cel.font = Font(bold=True, color='FFFFFF', size=10)
        cel.fill = motor.PatternFill('solid', fgColor='2D2D2D')
        cel.alignment = Alignment(horizontal='center', vertical='center',
                                  wrap_text=True)
    ws.column_dimensions['A'].width = ancho_a
    for i in range(1, len(columnas)):
        L = gcl(i + 1)
        if not ws.column_dimensions[L].width:
            ws.column_dimensions[L].width = 16.0


def nota(ws, coord, texto):
    """Línea de nota en cursiva pequeña (no es dato: no la mira ningún gate)."""
    motor.val(ws, coord, texto, wrap=True)
    ws[coord].font = Font(italic=True, size=9)


def apunta(cambios, fname, ws, texto):
    cambios.append(fname + ':' + ws.title + ': ' + texto)


# ==========================================================================
# §2.1 · calculadora-ticket-medio.xlsx
# ==========================================================================
#: Etiqueta de la fila de control que el grupo AÑADE (§2.1). Se guarda como
#: constante porque el detector de pares tiene que EXCLUIRLA en la 2.ª pasada:
#: empieza por «%» y, si no se saltara, se leería como un tramo de mix más.
ETIQUETA_MIX = '% de comensales asignado (debe sumar 100 %)'
RX_ETIQUETA_MIX = re.compile(r'^% de comensales asignado')

RX_PCT_FILA = re.compile(r'^%\s')
RX_PRECIO_FILA = re.compile(r'\(\s*(eur|€)\s*\)|precio|ticket')
RX_TICKET_RES = re.compile(r'^ticket medio (ponderado|estimado|proyectado)')


def variante_ticket(wb, fname=''):
    """`'escenarios-3col'` | `'columna-unica'` | `'mix-producto'`.

    Firma estructural MEDIDA (2026-08-29), nunca el nombre de la guía:
      · 3 columnas de escenario en la cabecera (`Escenario 1/2/3`) → rep.
      · sin fila de cabecera y valores sólo en B → los 5 hermanos.
      · cabecera `PVP …` + `Mix % ventas` + `Aporte …` → panadería.
    """
    if 'Ticket Medio' not in wb.sheetnames:
        raise VarianteDesconocida(
            fname + ': no hay hoja «Ticket Medio». Hojas: '
            + repr(wb.sheetnames))
    ws = wb['Ticket Medio']
    for fila in (3, 4):
        cab = [_norm(ws.cell(row=fila, column=c).value)
               for c in range(1, ws.max_column + 1)]
        if any(c.startswith('escenario ') for c in cab):
            return 'escenarios-3col', fila
        if any('mix' in c for c in cab) and any('aporte' in c for c in cab):
            return 'mix-producto', fila
    if _fila(ws, RX_TICKET_RES.pattern, obligatoria=False):
        return 'columna-unica', None
    raise VarianteDesconocida(
        fname + ':' + ws.title + ': rejilla de ticket medio no reconocida. '
        'fila3=' + repr([ws.cell(row=3, column=c).value
                         for c in range(1, ws.max_column + 1)])
        + ' fila4=' + repr([ws.cell(row=4, column=c).value
                            for c in range(1, ws.max_column + 1)]))


def pares_mix(ws, desde, hasta):
    """[(fila_%, fila_precio)] + [filas de precio INCONDICIONAL] del bloque.

    Regla estructural, la misma para las tres rejillas: una fila cuya etiqueta
    empieza por «%» es un TRAMO del mix y su precio es la fila inmediatamente
    siguiente; una fila de precio que no viene precedida de un «%» la pide el
    100 % de los comensales y entra SIN ponderar. Es exactamente el caso que la
    SPEC describe en japonés (`B7` «Precio medio ramen/principal» sin `%`) y el
    del representante (cinco pares y ningún incondicional).
    """
    filas = dict((r, n) for r, n, _ in etiquetas(ws, 1, desde, hasta))
    pares, sueltos, consumidas = [], [], set()
    for r in sorted(filas):
        if r in consumidas or RX_ETIQUETA_MIX.match(filas[r]):
            continue
        if RX_PCT_FILA.match(filas[r]):
            siguiente = r + 1
            if siguiente in filas and RX_PRECIO_FILA.search(filas[siguiente]):
                pares.append((r, siguiente))
                consumidas.add(siguiente)
            continue
        if RX_PRECIO_FILA.search(filas[r]):
            sueltos.append(r)
    return pares, sueltos


def _formula_ticket(col, pares, sueltos):
    trozos = [col + str(p) + '*' + col + str(q) for p, q in pares]
    trozos += [col + str(r) for r in sueltos]
    return '=' + '+'.join(trozos)


def ticket_escenarios_3col(wb, fname, cambios, contenido):
    """Representante: tres escenarios en B/C/D (TEC-01, DOM-08, COM-04)."""
    ws = wb['Ticket Medio']
    cols = [c for c in ('B', 'C', 'D')
            if _norm(ws[c + '4'].value).startswith('escenario ')]
    f_ticket = _fila(ws, RX_TICKET_RES.pattern, fname=fname)
    f_cub = _fila(ws, r'^cubiertos\s*/\s*d[ií]a|^cubiertos por dia',
                  hasta=ws.max_row, fname=fname)
    f_fdia = _fila(ws, r'^facturacion diaria', fname=fname)
    f_dias = _fila(ws, r'^dias abierto', fname=fname)
    f_fmes = _fila(ws, r'^facturacion mensual', fname=fname)
    pares, sueltos = pares_mix(ws, 5, f_ticket - 1)
    if not pares:
        raise VarianteDesconocida(
            fname + ':' + ws.title + ': 0 pares %/precio entre las filas 5 y '
            + str(f_ticket - 1) + ': la rejilla no es la que este código sabe '
            'leer.')

    # fila de control del mix, en el hueco que ya existe sobre el resultado
    f_mix = f_ticket - 1
    if _norm(ws['A' + str(f_mix)].value):
        f_mix = None                      # no hay hueco: no se pisa contenido
    conf = (contenido.TICKET if contenido and hasattr(contenido, 'TICKET')
            else {})
    tramos = conf.get('filas_mix')        # regex de las filas que suman 100 %
    if f_mix and tramos:
        filas_mix = [p for p, _q in pares
                     if any(re.search(t, _norm(ws['A' + str(p)].value))
                            for t in tramos)]
        if filas_mix:
            motor.val(ws, 'A' + str(f_mix), ETIQUETA_MIX)
            for col in cols:
                motor.f(ws, col + str(f_mix),
                        '=' + '+'.join(col + str(p) for p in filas_mix),
                        fmt=FMT_PCT)
            motor.regla_expresion(
                ws, cols[0] + str(f_mix) + ':' + cols[-1] + str(f_mix),
                '=AND(ISNUMBER(' + cols[0] + str(f_mix) + '),'
                + cols[0] + str(f_mix) + '<>1)')
            nota(ws, 'E' + str(f_mix),
                 'Los tramos del menú se reparten el 100 % de los comensales. '
                 'El maridaje y la copa NO entran aquí: son consumo adicional '
                 'sobre el mismo comensal, por eso pueden sumar más de 100 %.')
            apunta(cambios, fname, ws, 'fila de control del mix en A'
                   + str(f_mix) + ' (§2.1) sobre ' + str(len(filas_mix))
                   + ' tramos')

    for col in cols:
        motor.f(ws, col + str(f_ticket), _formula_ticket(col, pares, sueltos),
                fmt=FMT_EUR, bold=True)
        motor.f(ws, col + str(f_fdia),
                '=' + col + str(f_ticket) + '*' + col + str(f_cub),
                fmt=FMT_EUR)
        motor.f(ws, col + str(f_fmes),
                '=' + col + str(f_fdia) + '*' + col + str(f_dias),
                fmt=FMT_EUR)
    # el verde se retira SÓLO de las filas que ahora calcula el libro: las de
    # `Cubiertos/día` y `Días abierto/mes` siguen siendo entradas del cliente
    # (TEC-01 pinta de verde las cinco, incluidas las tres de resultado).
    for r in (f_ticket, f_fdia, f_fmes):
        motor.quitar_verde(ws, cols[0] + str(r) + ':' + cols[-1] + str(r))
    apunta(cambios, fname, ws, str(len(pares)) + ' pares %/precio + '
           + str(len(sueltos)) + ' incondicionales → ticket ponderado en la '
           'fila ' + str(f_ticket) + ', facturación día/mes (TEC-01, DOM-08)')
    _precargar_ticket(ws, cols, conf, cambios, fname)


def _precargar_ticket(ws, cols, conf, cambios, fname):
    """§7-bis.7 — cifras de ejemplo que el propio producto ya defiende.

    Van en celda VERDE (editables) y salen de `contenido_<pid>/a.py`, con la
    fuente anotada allí. Si el módulo de contenido no las trae, la hoja queda
    con sus fórmulas y sin ejemplo: no se inventa ninguna cifra aquí.
    """
    escenarios = (conf or {}).get('escenarios')
    if not escenarios:
        return
    puestas = 0
    for col in cols:
        datos = escenarios.get(col)
        if not datos:
            continue
        for patron, valor in datos.items():
            r = _fila(ws, patron, obligatoria=False)
            if r is None:
                continue
            cel = ws[col + str(r)]
            if cel.data_type == 'f':
                continue
            motor.val(ws, col + str(r), valor, verde_=True)
            puestas += 1
    if puestas:
        apunta(cambios, fname, ws, str(puestas) + ' celdas de ejemplo '
               'precargadas en verde (§7-bis.7)')


def ticket_columna_unica(wb, fname, cambios, contenido):
    """Los 5 hermanos: una sola columna B, con `TICKET MEDIO ESTIMADO` vacío.

    Además de la fórmula que falta, se AÑADEN debajo `Cubiertos/día`,
    `Días abierto/mes`, `Facturación diaria` y `Facturación mensual`, que hoy no
    existen en el hermano y sí en el representante (§2.1).
    """
    ws = wb['Ticket Medio']
    f_ticket = _fila(ws, RX_TICKET_RES.pattern, fname=fname)
    pares, sueltos = pares_mix(ws, 4, f_ticket - 1)
    if not pares:
        raise VarianteDesconocida(
            fname + ':' + ws.title + ': 0 pares %/precio antes de la fila '
            + str(f_ticket))
    motor.f(ws, 'B' + str(f_ticket), _formula_ticket('B', pares, sueltos),
            fmt=FMT_EUR, bold=True)
    motor.quitar_verde(ws, 'B' + str(f_ticket))
    conf = (contenido.TICKET if contenido and hasattr(contenido, 'TICKET')
            else {})
    base = f_ticket + 2
    filas = (('Cubiertos/día', conf.get('cubiertos_dia'), FMT_ENT, True),
             ('Días abierto/mes', conf.get('dias_mes'), FMT_ENT, True),
             ('Facturación diaria (€)', None, FMT_EUR, False),
             ('Facturación mensual (€)', None, FMT_EUR, False))
    for i, (etiqueta, valor, fmt, editable) in enumerate(filas):
        r = base + i
        motor.val(ws, 'A' + str(r), etiqueta)
        if editable:
            motor.val(ws, 'B' + str(r), valor, fmt=fmt,
                      verde_=valor is not None)
            if valor is None:
                motor.verde(ws, 'B' + str(r))
    motor.f(ws, 'B' + str(base + 2),
            '=B' + str(f_ticket) + '*B' + str(base), fmt=FMT_EUR)
    motor.f(ws, 'B' + str(base + 3),
            '=B' + str(base + 2) + '*B' + str(base + 1), fmt=FMT_EUR)
    apunta(cambios, fname, ws, 'ticket ponderado en B' + str(f_ticket)
           + ' (' + str(len(pares)) + ' pares, ' + str(len(sueltos))
           + ' incondicionales) + cubiertos/día, días/mes y facturación '
             'día/mes en A' + str(base) + ':B' + str(base + 3) + ' (§2.1)')


def ticket_mix_producto(wb, fname, cambios, contenido, fila_cab):
    """Panadería: `PVP €` × `Mix % ventas` / 100 → `Aporte €`, ya calculado.

    Lo que falta es el CONTROL: la columna de mix suma 100 y nadie lo comprueba,
    y el ticket resultante (3,77 €) no cuadra con el 5,80 € que usa el P&L de la
    misma guía. Se añade el semáforo del mix y las filas de facturación.
    """
    ws = wb['Ticket Medio']
    f_tot = _fila(ws, r'^ticket medio', fname=fname)
    from openpyxl.utils import get_column_letter as gcl
    col_mix = col_aporte = None
    for c in range(2, ws.max_column + 1):
        cab = _norm(ws.cell(row=fila_cab, column=c).value)
        if 'mix' in cab:
            col_mix = gcl(c)
        elif 'aporte' in cab:
            col_aporte = gcl(c)
    if not (col_mix and col_aporte):
        raise VarianteDesconocida(fname + ':' + ws.title
                                  + ': falta la columna de mix o la de aporte')
    ultima = f_tot - 1
    while ultima > fila_cab and ws['A' + str(ultima)].value is None:
        ultima -= 1
    motor.f(ws, col_mix + str(f_tot),
            '=SUM(' + col_mix + str(fila_cab + 1) + ':' + col_mix
            + str(ultima) + ')', fmt=FMT_ENT, bold=True)
    motor.f(ws, col_aporte + str(f_tot),
            '=SUM(' + col_aporte + str(fila_cab + 1) + ':' + col_aporte
            + str(ultima) + ')', fmt=FMT_EUR, bold=True)
    motor.regla_expresion(
        ws, col_mix + str(f_tot),
        '=AND(ISNUMBER(' + col_mix + str(f_tot) + '),' + col_mix + str(f_tot)
        + '<>100)')
    apunta(cambios, fname, ws, 'mix y aporte totalizados en la fila '
           + str(f_tot) + ' con semáforo si el mix no suma 100 (§2.1)')


def ticket_medio(wb, fname, cambios, contenido):
    variante, fila_cab = variante_ticket(wb, fname)
    if variante == 'escenarios-3col':
        ticket_escenarios_3col(wb, fname, cambios, contenido)
    elif variante == 'columna-unica':
        ticket_columna_unica(wb, fname, cambios, contenido)
    else:
        ticket_mix_producto(wb, fname, cambios, contenido, fila_cab)
    return variante


# ==========================================================================
# §2.2 · pl-mensual-escenarios.xlsx  (TEC-02, DOM-07, COM-05, §7-bis.14)
# ==========================================================================
#: Patrones de fila, normalizados. Sirven para las TRES variantes porque los
#: tres generadores heredaron los mismos rótulos: lo que cambia es la fila.
RX_TOT_INGRESOS = r'^total ingresos|^facturacion total mensual'
RX_FOOD_COST = r'^food cost|^materia prima|^coste materias primas$'
RX_TOT_VARIABLES = r'^total costes variables'
RX_TOT_FIJOS = r'^total costes fijos'
RX_EBITDA = r'^ebitda(?! anual)'
RX_PCT_EBITDA = r'^% ebitda|^margen ebitda'
RX_BLOQUE_ING = r'^ingresos$'
RX_BLOQUE_VAR = r'^costes variables$'
RX_BLOQUE_FIJ = r'^costes fijos$'


def _ultimo_detalle(ws, desde, hasta, saltar_rx):
    """Última fila con etiqueta entre `desde` y `hasta` que no sea un total."""
    ultima = None
    for r, norm, _c in etiquetas(ws, 1, desde, hasta):
        if any(re.search(rx, norm) for rx in saltar_rx):
            continue
        ultima = r
    return ultima


def pl_escenarios_columnas(wb, fname, cambios, contenido):
    """Representante: una hoja `Escenarios`, tres columnas B/C/D.

    Hoy: 0 fórmulas, 0 valores y `B17:D22` en VERDE, es decir, la hoja le pide
    al cliente que teclee él el EBITDA (TEC-02).
    """
    ws = wb['Escenarios']
    cols = [c for c in ('B', 'C', 'D')
            if isinstance(ws[c + '4'].value, str)]
    f_cub_com = _fila(ws, r'^cubiertos.*comida', fname=fname)
    f_cub_cena = _fila(ws, r'^cubiertos.*cena', fname=fname)
    f_tk_com = _fila(ws, r'^ticket medio comida', fname=fname)
    f_tk_cena = _fila(ws, r'^ticket medio cena', fname=fname)
    f_dias = _fila(ws, r'^dias abierto', fname=fname)
    f_fc = _fila(ws, r'^food cost', fname=fname)
    f_pers = _fila(ws, r'^coste personal', fname=fname)
    f_res = _fila(ws, r'^resultados$', fname=fname)
    f_otros = _ultimo_detalle(ws, f_pers, f_res - 1, ())
    f_fact = _fila(ws, r'^facturacion mensual', desde=f_res, fname=fname)
    f_mp = _fila(ws, r'^coste materia prima', desde=f_res, fname=fname)
    f_mb = _fila(ws, r'^margen bruto', desde=f_res, fname=fname)
    f_cf = _fila(ws, r'^costes fijos totales', desde=f_res, fname=fname)
    f_eb = _fila(ws, RX_EBITDA, desde=f_res, fname=fname)
    f_me = _fila(ws, RX_PCT_EBITDA, desde=f_res, fname=fname)

    for col in cols:
        motor.f(ws, col + str(f_fact),
                '=(' + col + str(f_cub_com) + '*' + col + str(f_tk_com) + '+'
                + col + str(f_cub_cena) + '*' + col + str(f_tk_cena) + ')*'
                + col + str(f_dias), fmt=FMT_EUR)
        motor.f(ws, col + str(f_mp),
                '=' + col + str(f_fact) + '*' + col + str(f_fc), fmt=FMT_EUR)
        motor.f(ws, col + str(f_mb),
                '=' + col + str(f_fact) + '-' + col + str(f_mp), fmt=FMT_EUR)
        motor.f(ws, col + str(f_cf),
                '=SUM(' + col + str(f_pers) + ':' + col + str(f_otros) + ')',
                fmt=FMT_EUR)
        motor.f(ws, col + str(f_eb),
                '=' + col + str(f_mb) + '-' + col + str(f_cf), fmt=FMT_EUR,
                bold=True)
        # §7-bis.13: un mes sin una sola venta NO tiene un margen del «0,0 %»
        motor.f(ws, col + str(f_me),
                '=IF(' + col + str(f_fact) + '=0,"",' + col + str(f_eb) + '/'
                + col + str(f_fact) + ')', fmt=FMT_PCT)
        motor.quitar_verde(ws, col + str(f_fact) + ':' + col + str(f_me))
    _semaforo_negativo(ws, cols, (f_eb, f_me))
    apunta(cambios, fname, ws, 'P&L encadenado en las filas ' + str(f_fact)
           + '-' + str(f_me) + ' para ' + str(len(cols))
           + ' escenarios; verde retirado de los resultados (TEC-02, DOM-07)')
    _precargar_pl(ws, cols, contenido, cambios, fname)


def _semaforo_negativo(ws, cols, filas):
    """§1.6 — rojo si el resultado es negativo, con la guarda `ISNUMBER`.

    Sin ella Excel evalúa `""<0` como FALSO y cualquier TEXTO como VERDADERO:
    el semáforo pintaría de rojo justo la celda que dice que no hay dato.
    """
    for r in filas:
        rango = cols[0] + str(r) + ':' + cols[-1] + str(r)
        motor.semaforo_isnumber(ws, rango, '$' + cols[0] + '$' + str(r)
                                if len(cols) == 1 else cols[0] + str(r))


def _precargar_pl(ws, cols, contenido, cambios, fname, clave='PL'):
    conf = getattr(contenido, clave, None) if contenido else None
    if not conf or not conf.get('escenarios'):
        return
    puestas = 0
    for col in cols:
        for patron, valor in (conf['escenarios'].get(col) or {}).items():
            r = _fila(ws, patron, obligatoria=False)
            if r is None or ws[col + str(r)].data_type == 'f':
                continue
            motor.val(ws, col + str(r), valor, verde_=True)
            puestas += 1
    for patron, texto in (conf.get('notas') or {}).items():
        r = _fila(ws, patron, obligatoria=False)
        if r is not None:
            nota(ws, 'E' + str(r), texto)
    if puestas:
        apunta(cambios, fname, ws, str(puestas) + ' celdas de ejemplo en verde '
               '(§7-bis.7/§7-bis.14: el Pesimista es un escenario malo, no '
               'inviable)')


def pl_tres_hojas(wb, fname, cambios, contenido):
    """Los 5 hermanos: `Pesimista`/`Realista`/`Optimista` con TODO tecleado.

    §1.2/§7-bis.12: las líneas de detalle se quedan VERDES con su valor actual
    como ejemplo y los TOTALES pasan a fórmula. El food cost sale del rótulo
    («Food cost (33%)») y baja a una celda verde: hoy va multiplicado a mano.
    La columna `D % s/Ventas` está rotulada y **no existe**.
    """
    conf = getattr(contenido, 'PL', None) if contenido else None
    for nombre in ('Pesimista', 'Realista', 'Optimista'):
        ws = wb[nombre]
        f_ing = _fila(ws, RX_BLOQUE_ING, fname=fname)
        f_tot_ing = _fila(ws, RX_TOT_INGRESOS, fname=fname)
        f_var = _fila(ws, RX_BLOQUE_VAR, fname=fname)
        f_fc = _fila(ws, RX_FOOD_COST, desde=f_var, fname=fname)
        f_tot_var = _fila(ws, RX_TOT_VARIABLES, fname=fname)
        f_fij = _fila(ws, RX_BLOQUE_FIJ, fname=fname)
        f_tot_fij = _fila(ws, RX_TOT_FIJOS, fname=fname)
        f_eb = _fila(ws, RX_EBITDA, desde=f_tot_fij, fname=fname)
        f_pct = _fila(ws, RX_PCT_EBITDA, desde=f_eb, obligatoria=False)
        cols = ['B']
        col_anual = 'C' if _norm(ws['C4'].value).startswith('anual') else None
        col_pct = 'D' if 's/ventas' in _norm(ws['D4'].value) else None

        motor.verde(ws, 'B' + str(f_ing + 1) + ':B' + str(f_tot_ing - 1))
        motor.verde(ws, 'B' + str(f_fij + 1) + ':B' + str(f_tot_fij - 1))
        motor.a_formula(ws, 'B' + str(f_tot_ing),
                        '=SUM(B' + str(f_ing + 1) + ':B' + str(f_tot_ing - 1)
                        + ')', fmt=FMT_EUR, informe=cambios, fname=fname)
        # el food cost deja de ir en el rótulo y baja a celda verde
        celda_fc = _celda_food_cost(ws, f_fc, conf, cambios, fname)
        motor.a_formula(ws, 'B' + str(f_fc),
                        '=B' + str(f_tot_ing) + '*' + celda_fc, fmt=FMT_EUR,
                        informe=cambios, fname=fname)
        motor.verde(ws, 'B' + str(f_fc + 1) + ':B' + str(f_tot_var - 1))
        motor.a_formula(ws, 'B' + str(f_tot_var),
                        '=SUM(B' + str(f_fc) + ':B' + str(f_tot_var - 1) + ')',
                        fmt=FMT_EUR, informe=cambios, fname=fname)
        motor.a_formula(ws, 'B' + str(f_tot_fij),
                        '=SUM(B' + str(f_fij + 1) + ':B' + str(f_tot_fij - 1)
                        + ')', fmt=FMT_EUR, informe=cambios, fname=fname)
        motor.a_formula(ws, 'B' + str(f_eb),
                        '=B' + str(f_tot_ing) + '-B' + str(f_tot_var) + '-B'
                        + str(f_tot_fij), fmt=FMT_EUR, informe=cambios,
                        fname=fname)
        if f_pct:
            motor.f(ws, 'B' + str(f_pct),
                    '=IF(B' + str(f_tot_ing) + '=0,"",B' + str(f_eb) + '/B'
                    + str(f_tot_ing) + ')', fmt=FMT_PCT)
        if col_anual:
            for r, _n, _c in etiquetas(ws, 1, f_ing, f_eb):
                if ws['B' + str(r)].value is None:
                    continue
                motor.a_formula(ws, col_anual + str(r),
                                '=B' + str(r) + '*12', fmt=FMT_EUR,
                                informe=cambios, fname=fname)
            cols.append(col_anual)
        if col_pct:
            for r, _n, _c in etiquetas(ws, 1, f_ing, f_eb):
                if ws['B' + str(r)].value is None:
                    continue
                motor.f(ws, col_pct + str(r),
                        '=IF($B$' + str(f_tot_ing) + '=0,"",B' + str(r)
                        + '/$B$' + str(f_tot_ing) + ')', fmt=FMT_PCT)
        _semaforo_negativo(ws, ['B'], [f_eb] + ([f_pct] if f_pct else []))
        apunta(cambios, fname, ws, 'totales y % s/ventas encadenados; food '
               'cost en ' + celda_fc + ' (§2.2 variante tres hojas)')
        if conf and conf.get('escenarios', {}).get(nombre):
            _precargar_hoja(ws, nombre, conf, cambios, fname)


def _celda_food_cost(ws, f_fc, conf, cambios, fname):
    """Saca el food cost del rótulo «Food cost (33%)» y lo pone en celda verde.

    Se escribe en la columna E de la propia fila (libre en las tres hojas
    medidas). El porcentaje se LEE del rótulo: es el dato que el generador dejó
    ahí, no una cifra inventada.
    """
    crudo = ws['A' + str(f_fc)].value or ''
    m = re.search(r'(\d+(?:[.,]\d+)?)\s*%', crudo)
    pct = float(m.group(1).replace(',', '.')) / 100 if m else None
    if (conf or {}).get('food_cost') is not None:
        pct = conf['food_cost']
    destino = 'E' + str(f_fc)
    if ws[destino].value is None and pct is not None:
        motor.val(ws, destino, pct, fmt=FMT_PCT, verde_=True)
        nota(ws, 'F' + str(f_fc),
             'Food cost objetivo. Estaba escrito dentro del rótulo y '
             'multiplicado a mano: ahora se cambia aquí y se recalcula.')
        apunta(cambios, fname, ws, 'food cost ' + str(pct) + ' extraído del '
               'rótulo ' + repr(crudo[:40]) + ' a la celda verde ' + destino)
    return '$' + destino[0] + '$' + destino[1:]


def _precargar_hoja(ws, nombre, conf, cambios, fname):
    puestas = 0
    for patron, valor in (conf['escenarios'][nombre] or {}).items():
        r = _fila(ws, patron, obligatoria=False)
        if r is None or ws['B' + str(r)].data_type == 'f':
            continue
        motor.val(ws, 'B' + str(r), valor, verde_=True)
        puestas += 1
    if puestas:
        apunta(cambios, fname, ws, str(puestas)
               + ' líneas recalibradas (§7-bis.14)')


def pl_hoja_unica(wb, fname, cambios, contenido):
    """Panadería: `P&L 3 escenarios`, que YA calcula. Sólo §1 más el margen.

    Se le añade la fila de margen EBITDA (%), que no tiene, y el semáforo.
    """
    ws = wb['P&L 3 escenarios']
    f_fact = _fila(ws, r'^facturacion total mensual', fname=fname)
    f_eb = _fila(ws, r'^ebitda mensual', fname=fname)
    cols = [c for c in ('B', 'C', 'D')]
    f_pct = _fila(ws, r'^margen ebitda', obligatoria=False)
    if f_pct is None:
        f_pct = ws.max_row + 1
        motor.val(ws, 'A' + str(f_pct), 'Margen EBITDA (%)')
    for col in cols:
        motor.f(ws, col + str(f_pct),
                '=IF(' + col + str(f_fact) + '=0,"",' + col + str(f_eb) + '/'
                + col + str(f_fact) + ')', fmt=FMT_PCT)
    _semaforo_negativo(ws, cols, (f_eb, f_pct))
    apunta(cambios, fname, ws, 'margen EBITDA (%) en la fila ' + str(f_pct)
           + ' + semáforo ISNUMBER (§2.2 variante hoja única)')


def pl_mensual(wb, fname, cambios, contenido):
    variante = motor.variante_pl(wb)
    if variante == 'escenarios-columnas':
        pl_escenarios_columnas(wb, fname, cambios, contenido)
    elif variante == 'tres-hojas':
        pl_tres_hojas(wb, fname, cambios, contenido)
    elif variante == 'hoja-unica':
        pl_hoja_unica(wb, fname, cambios, contenido)
    else:
        raise VarianteDesconocida(
            fname + ': `motor.variante_pl` no reconoce las hojas '
            + repr(wb.sheetnames))
    return variante


# ==========================================================================
# §2.3 · plan-financiero-3-anos.xlsx
# ==========================================================================
HOJA_PROY = 'Proyección 3 Años'
HOJA_FIN = 'Financiación'
AVISO_CARENCIA = 'La carencia no puede igualar ni superar el plazo'
ANOS_CUADRO = 10          # filas del cuadro francés; la nota explica ampliarlo


def variante_plan(wb, fname=''):
    """`'inversion-conceptos'` | `'inversion-categorias'` | `'pl-3-anos'`."""
    hojas = set(wb.sheetnames)
    if 'P&L 3 años' in hojas:
        return 'pl-3-anos'
    if 'Inversión' in hojas and 'P&L Mensual' in hojas:
        cab = _norm(wb['Inversión']['B4'].value)
        if cab == 'concepto':
            return 'inversion-conceptos'
        if cab == 'partida':
            return 'inversion-categorias'
    raise VarianteDesconocida(
        fname + ': plan financiero no reconocido. Hojas=' + repr(wb.sheetnames)
        + ' Inversión!B4=' + repr(wb['Inversión']['B4'].value
                                  if 'Inversión' in hojas else None))


def _celda(col, fila, fijo=False):
    return ('$' + col + '$' + str(fila)) if fijo else (col + str(fila))


# --------------------------------------------------------------------------
# 2.3.2 · el EBITDA deja de restar la amortización (TEC-08, DOM-26)
# --------------------------------------------------------------------------
def _pl_mensual_representante(wb, fname, cambios, contenido):
    ws = wb['P&L Mensual']
    f_tot_ing = _fila(ws, RX_TOT_INGRESOS, fname=fname)
    f_tot_var = _fila(ws, RX_TOT_VARIABLES, fname=fname)
    f_mb = _fila(ws, r'^margen bruto', fname=fname)
    f_fij = _fila(ws, RX_BLOQUE_FIJ, fname=fname)
    f_tot_fij = _fila(ws, RX_TOT_FIJOS, fname=fname)
    f_amort = _fila(ws, r'^amortizacion equipamiento', desde=f_fij,
                    hasta=f_tot_fij, fname=fname)
    f_eb = _fila(ws, RX_EBITDA, desde=f_tot_fij, fname=fname)
    f_me = _fila(ws, RX_PCT_EBITDA, desde=f_eb, fname=fname)

    # TOTAL COSTES FIJOS sin la amortización: lo que la hoja llamaba EBITDA era
    # un EBIT. Con ventas 140.000 € y amortización 6.000 €, el R1 midió 26.000 €
    # donde el EBITDA es 32.000 € (−23 %).
    trozos = []
    if f_amort > f_fij + 1:
        trozos.append('SUM(B' + str(f_fij + 1) + ':B' + str(f_amort - 1) + ')')
    if f_amort < f_tot_fij - 1:
        trozos.append('SUM(B' + str(f_amort + 1) + ':B' + str(f_tot_fij - 1)
                      + ')')
    motor.f(ws, 'B' + str(f_tot_fij), '=' + '+'.join(trozos), fmt=FMT_EUR)
    motor.f(ws, 'B' + str(f_eb), '=B' + str(f_mb) + '-B' + str(f_tot_fij),
            fmt=FMT_EUR, bold=True)
    motor.val(ws, 'A' + str(f_tot_fij),
              'TOTAL COSTES FIJOS (sin amortización)')
    # 2.3.3 · el margen es un ratio, no un importe (TEC-09) — se CLAVA porque
    # la cabecera de la columna B dice «Importe (€)» y la regla de columna del
    # §1.4 lo devolvería a euros.
    motor.f(ws, 'B' + str(f_me),
            '=IF(B' + str(f_tot_ing) + '=0,"",B' + str(f_eb) + '/B'
            + str(f_tot_ing) + ')')
    motor.fijar_formato(ws, 'B' + str(f_me), FMT_PCT)

    # filas nuevas: la amortización recuperada y el EBIT
    f_amo2, f_ebit = f_me + 1, f_me + 2
    motor.val(ws, 'A' + str(f_amo2),
              'Amortización (fuera del EBITDA, ver fila ' + str(f_amort) + ')')
    motor.f(ws, 'B' + str(f_amo2), '=B' + str(f_amort), fmt=FMT_EUR)
    motor.val(ws, 'A' + str(f_ebit), 'EBIT (resultado de explotación)')
    motor.f(ws, 'B' + str(f_ebit), '=B' + str(f_eb) + '-B' + str(f_amo2),
            fmt=FMT_EUR, bold=True)

    # 2.3.3 · la columna «% s/Ventas» deja de decir «0,0 %» con el libro en
    # blanco (§7-bis.13) y C35 deja de dividir un porcentaje entre la
    # facturación (TEC-10): esa fila ya no tiene eco en la columna de %.
    # Criterio: es fila de DATO la que tiene etiqueta y no es un encabezado de
    # bloque. No sirve mirar si B está vacía —en el representante lo está
    # ENTERA, porque el P&L es del cliente— y vaciar por eso la columna de %
    # borraría 24 fórmulas legítimas.
    rx_bloque = re.compile(r'^(ingresos|costes variables|costes fijos)$')
    limpiadas, rehechas = [], 0
    for r, norm, _c in etiquetas(ws, 1, 5, f_ebit):
        if r == f_me or rx_bloque.match(norm):
            if ws['C' + str(r)].value is not None:
                motor.limpiar_rango(ws, 'C' + str(r))
                limpiadas.append('C' + str(r))
            continue
        motor.f(ws, 'C' + str(r),
                '=IF($B$' + str(f_tot_ing) + '=0,"",B' + str(r) + '/$B$'
                + str(f_tot_ing) + ')', fmt=FMT_PCT)
        rehechas += 1
    _semaforo_negativo(ws, ['B'], (f_eb, f_ebit))
    motor.permitir_negativo(ws, 'B' + str(f_eb) + ':B' + str(f_ebit))
    apunta(cambios, fname, ws,
           'EBITDA sin amortización (B' + str(f_tot_fij) + '=' + '+'.join(trozos)
           + '), EBIT en la fila ' + str(f_ebit) + ', margen en % (TEC-08/09), '
           + str(rehechas) + ' celdas de «% s/Ventas» con "" en vez de 0 y '
           + str(len(limpiadas)) + ' vaciadas ' + str(limpiadas) + ' (TEC-10)')
    return {'tot_ing': f_tot_ing, 'tot_var': f_tot_var, 'margen': f_mb,
            'tot_fij': f_tot_fij, 'amort': f_amort, 'ebitda': f_eb,
            'ebit': f_ebit}


# --------------------------------------------------------------------------
# 2.5 NUEVO-01 · el P&L Mensual de los 5 hermanos no tiene NI UN total
# --------------------------------------------------------------------------
def _pl_mensual_hermanos(wb, fname, cambios, contenido):
    ws = wb['P&L Mensual']
    fila_cab = 4
    meses, total = columnas_mes(ws, fila_cab)
    if len(meses) < 12:
        raise VarianteDesconocida(
            fname + ':' + ws.title + ': se esperaban 12 columnas de mes y se '
            'han leído ' + str(len(meses)) + ' en la cabecera de la fila '
            + str(fila_cab))
    f_ing = _fila(ws, RX_BLOQUE_ING, fname=fname)
    f_tot_ing = _fila(ws, RX_TOT_INGRESOS, fname=fname)
    f_var = _fila(ws, RX_BLOQUE_VAR, fname=fname)
    f_fc = _fila(ws, RX_FOOD_COST, desde=f_var, fname=fname)
    f_tot_var = _fila(ws, RX_TOT_VARIABLES, fname=fname)
    f_fij = _fila(ws, RX_BLOQUE_FIJ, fname=fname)
    f_tot_fij = _fila(ws, RX_TOT_FIJOS, fname=fname)
    f_eb = _fila(ws, RX_EBITDA, desde=f_tot_fij, fname=fname)
    f_pct = _fila(ws, RX_PCT_EBITDA, desde=f_eb, obligatoria=False)
    conf = getattr(contenido, 'PLAN', None) if contenido else None
    celda_fc = _celda_food_cost_grid(ws, f_fc, conf, cambios, fname, meses)

    for col in meses + ([total] if total else []):
        if col == total:
            motor.f(ws, col + str(f_tot_ing),
                    '=SUM(' + meses[0] + str(f_tot_ing) + ':' + meses[-1]
                    + str(f_tot_ing) + ')', fmt=FMT_EUR)
            motor.f(ws, col + str(f_fc),
                    '=SUM(' + meses[0] + str(f_fc) + ':' + meses[-1]
                    + str(f_fc) + ')', fmt=FMT_EUR)
        else:
            motor.f(ws, col + str(f_tot_ing),
                    '=SUM(' + col + str(f_ing + 1) + ':' + col
                    + str(f_tot_ing - 1) + ')', fmt=FMT_EUR)
            motor.f(ws, col + str(f_fc),
                    '=' + col + str(f_tot_ing) + '*' + celda_fc, fmt=FMT_EUR)
        motor.f(ws, col + str(f_tot_var),
                '=SUM(' + col + str(f_fc) + ':' + col + str(f_tot_var - 1)
                + ')', fmt=FMT_EUR)
        motor.f(ws, col + str(f_tot_fij),
                '=SUM(' + col + str(f_fij + 1) + ':' + col + str(f_tot_fij - 1)
                + ')', fmt=FMT_EUR)
        motor.f(ws, col + str(f_eb),
                '=' + col + str(f_tot_ing) + '-' + col + str(f_tot_var) + '-'
                + col + str(f_tot_fij), fmt=FMT_EUR, bold=True)
        if f_pct:
            motor.f(ws, col + str(f_pct),
                    '=IF(' + col + str(f_tot_ing) + '=0,"",' + col + str(f_eb)
                    + '/' + col + str(f_tot_ing) + ')', fmt=FMT_PCT)
    todas = meses + ([total] if total else [])
    _semaforo_negativo(ws, todas, [f_eb] + ([f_pct] if f_pct else []))
    apunta(cambios, fname, ws, 'NUEVO-01: totales, food cost, EBITDA y % '
           'EBITDA calculados en las ' + str(len(todas)) + ' columnas '
           '(filas ' + str(f_tot_ing) + '/' + str(f_fc) + '/' + str(f_tot_var)
           + '/' + str(f_tot_fij) + '/' + str(f_eb) + ')')
    return {'tot_ing': f_tot_ing, 'tot_var': f_tot_var, 'tot_fij': f_tot_fij,
            'ebitda': f_eb, 'meses': meses, 'total': total, 'amort': None}


def _celda_food_cost_grid(ws, f_fc, conf, cambios, fname, meses):
    """El food cost del rótulo («Food cost (33%)») a una celda verde ABSOLUTA.

    Se coloca en la primera columna libre a la derecha de la rejilla para no
    pisar ningún mes.
    """
    from openpyxl.utils import get_column_letter as gcl, column_index_from_string
    crudo = ws['A' + str(f_fc)].value or ''
    m = re.search(r'(\d+(?:[.,]\d+)?)\s*%', crudo)
    pct = float(m.group(1).replace(',', '.')) / 100 if m else None
    if (conf or {}).get('food_cost') is not None:
        pct = conf['food_cost']
    col = gcl(column_index_from_string(meses[-1]) + 2)
    destino = col + str(f_fc)
    motor.val(ws, col + str(f_fc - 1), 'Food cost objetivo (%)')
    if pct is not None and ws[destino].data_type != 'f':
        motor.val(ws, destino, pct, fmt=FMT_PCT, verde_=True)
    motor.fijar_formato(ws, destino, FMT_PCT)
    apunta(cambios, fname, ws, 'food cost ' + repr(pct) + ' extraído del '
           'rótulo ' + repr(crudo[:34]) + ' a la celda verde ' + destino)
    return '$' + col + '$' + str(f_fc)


# --------------------------------------------------------------------------
# 2.3.4 · hoja «Financiación» — cuadro francés con anualidad ALGEBRAICA
# --------------------------------------------------------------------------
def hoja_financiacion(wb, fname, cambios, contenido, subtitulo):
    """DOM-22: hoy no hay una sola línea de préstamo en los 141 ficheros.

    `pycel` **no implementa `PMT`** (SPEC, cabecera): la cuota va como anualidad
    algebraica `importe*i/(1-(1+i)^-n)`. El cuadro es ANUAL y con el tipo anual,
    así que el capital pendiente cierra exactamente en 0; la cuota mensual se da
    aparte (es la que se lleva al cash flow) con el tipo mensual.

    Dos guardas heredadas del kit plan-financiero, que allí se pagaron caras:
      · **carencia ≥ plazo** → aviso de TEXTO en la columna `Cuota`, dejando
        `Capital inicial`, `Intereses` y `Capital pendiente` NUMÉRICAS: de los
        intereses vive el P&L y del capital pendiente el encadenado del año
        siguiente, así que un texto ahí propagaría `#¡VALOR!` por todo el libro.
      · **pasado el vencimiento** el cuadro se apaga a `0` numérico, o el
        capital pendiente se vuelve negativo y el préstamo «cobra» al banco.
    """
    ws, nueva = hoja(wb, HOJA_FIN, tras='P&L Mensual')
    conf = ((getattr(contenido, 'PLAN', None) or {}).get('financiacion')
            if contenido else None) or {}
    cabecera(ws, 'Financiación del proyecto', subtitulo,
             ['Año', 'Capital inicial (€)', 'Cuota (€)', 'Intereses (€)',
              'Amortización del principal (€)', 'Capital pendiente (€)'],
             fila=17, ancho_a=46)
    motor.val(ws, 'A4', 'PARÁMETROS DEL PRÉSTAMO', bold=True)
    campos = (
        (5, 'Importe del préstamo (€)', conf.get('importe'), FMT_EUR),
        (6, 'Plazo (años)', conf.get('plazo'), FMT_ENT),
        (7, 'Tipo de interés nominal anual (%)', conf.get('tipo'), FMT_PCT),
        (8, 'Carencia (años, sólo intereses)', conf.get('carencia'), FMT_ENT))
    for fila, etiqueta, valor, fmt in campos:
        motor.val(ws, 'A' + str(fila), etiqueta)
        motor.val(ws, 'B' + str(fila), valor, fmt=fmt, verde_=True)
        motor.fijar_formato(ws, 'B' + str(fila), fmt)
    motor.val(ws, 'A10', 'Tipo mensual (%)')
    motor.f(ws, 'B10', '=B7/12')
    motor.fijar_formato(ws, 'B10', '0.000%')
    motor.val(ws, 'A11', 'Nº de cuotas (meses)')
    motor.f(ws, 'B11', '=B6*12', fmt=FMT_ENT)
    motor.val(ws, 'A12', 'Cuota MENSUAL (€) — la que se lleva al cash flow')
    motor.f(ws, 'B12',
            '=IF(B5=0,"",IFERROR(B5*B10/(1-(1+B10)^-B11),""))', fmt=FMT_EUR,
            bold=True)
    motor.val(ws, 'A13', 'Cuota ANUAL del cuadro tras la carencia (€)')
    motor.f(ws, 'B13',
            '=IF(B5=0,"",IF(B6-B8<=0,"",IFERROR(B5*B7/(1-(1+B7)^-(B6-B8)),'
            '"")))', fmt=FMT_EUR)
    nota(ws, 'A14',
         'La cuota se calcula como anualidad: importe × i / (1 − (1+i)^−n). '
         'El cuadro de abajo es ANUAL y usa el tipo anual, por eso el capital '
         'pendiente cierra en 0 exacto; la cuota mensual de B12 usa el tipo '
         'mensual y es la que se repite en cash-flow-break-even.xlsx.')
    nota(ws, 'A15',
         'Durante la carencia sólo se pagan intereses: el capital pendiente no '
         'baja. El cuadro cubre ' + str(ANOS_CUADRO) + ' años; si tu plazo es '
         'mayor, copia la última fila hacia abajo.')

    fila0 = 18
    for i in range(ANOS_CUADRO):
        r = fila0 + i
        ano = i + 1
        motor.val(ws, 'A' + str(r), ano, fmt=FMT_ENT)
        if i == 0:
            motor.f(ws, 'B' + str(r), '=$B$5', fmt=FMT_EUR)
        else:
            motor.f(ws, 'B' + str(r), '=F' + str(r - 1), fmt=FMT_EUR)
        motor.f(ws, 'D' + str(r), '=B' + str(r) + '*$B$7', fmt=FMT_EUR)
        motor.f(ws, 'C' + str(r),
                '=IF($B$8>=$B$6,"' + AVISO_CARENCIA + '",'
                'IF(A' + str(r) + '>$B$6,0,'
                'IF(A' + str(r) + '<=$B$8,D' + str(r) + ',$B$13)))',
                fmt=FMT_EUR)
        motor.f(ws, 'E' + str(r),
                '=IF(ISNUMBER(C' + str(r) + '),C' + str(r) + '-D' + str(r)
                + ',0)', fmt=FMT_EUR)
        motor.f(ws, 'F' + str(r), '=B' + str(r) + '-E' + str(r), fmt=FMT_EUR)
    ws.column_dimensions['A'].width = 46.0
    motor.regla_expresion(ws, 'F' + str(fila0) + ':F'
                          + str(fila0 + ANOS_CUADRO - 1),
                          '=AND(ISNUMBER($F' + str(fila0) + '),$F' + str(fila0)
                          + '<0)')
    apunta(cambios, fname, ws, ('hoja CREADA' if nueva else 'hoja rehecha')
           + ': parámetros, cuota mensual y anual y cuadro francés de '
           + str(ANOS_CUADRO) + ' años con las dos guardas (DOM-22, §2.3.4)')
    return {'primer_ano': fila0, 'cuota_mensual': 'B12'}


# --------------------------------------------------------------------------
# 2.3.1 · hoja «Proyección 3 Años» (TEC-07, DOM-06, COM-07)
# --------------------------------------------------------------------------
def hoja_proyeccion(wb, fname, cambios, contenido, subtitulo, pl, fin):
    """La pestaña que `Instrucciones!A9` anuncia y que no existe en ninguna
    de las 7 guías.

    Año 1 va **por referencia** al P&L mensual (nunca constantes) y toda la
    cadena está guardada por `$B$<ingresos>=""`: con el libro en blanco la hoja
    devuelve `""`, no una proyección de ceros (§7-bis.13).
    """
    ws, nueva = hoja(wb, HOJA_PROY, tras='P&L Mensual')
    conf = ((getattr(contenido, 'PLAN', None) or {}).get('proyeccion')
            if contenido else None) or {}
    cabecera(ws, 'Proyección a 3 años', subtitulo,
             ['Concepto', 'Año 1', 'Año 2', 'Año 3', 'Notas'], fila=4,
             ancho_a=46)
    ws.column_dimensions['E'].width = 52.0
    pl_ing = "'P&L Mensual'!B" + str(pl['tot_ing'])
    pl_var = "'P&L Mensual'!B" + str(pl['tot_var'])
    pl_fij = "'P&L Mensual'!B" + str(pl['tot_fij'])
    pl_amo = ("'P&L Mensual'!B" + str(pl['amort'])) if pl.get('amort') else None

    motor.val(ws, 'A5', 'PARÁMETROS', bold=True)
    motor.val(ws, 'A6', 'Crecimiento de ventas (%)')
    motor.val(ws, 'A7', 'Inflación de costes (%)')
    motor.val(ws, 'A8', 'Tipo del Impuesto de Sociedades (%)')
    nota(ws, 'E6', 'Sobre el año anterior. El Año 1 es la base: sale del P&L '
                   'mensual de este mismo libro.')
    nota(ws, 'E8', 'Tipo general 25 %. Una entidad de NUEVA CREACIÓN tributa '
                   'al 15 % en el primer ejercicio con base positiva y en el '
                   'siguiente (art. 29.1 LIS).')
    for col in ('C', 'D'):
        motor.val(ws, col + '6', (conf.get('crecimiento') or {}).get(col),
                  fmt=FMT_PCT, verde_=True)
        motor.val(ws, col + '7', (conf.get('inflacion') or {}).get(col),
                  fmt=FMT_PCT, verde_=True)
        motor.permitir_negativo(ws, col + '6:' + col + '7')
    for col in ('B', 'C', 'D'):
        motor.val(ws, col + '8', conf.get('impuesto_sociedades'), fmt=FMT_PCT,
                  verde_=True)

    filas = ((11, 'Ingresos (€)'), (12, 'Costes variables (€)'),
             (13, 'Margen bruto (€)'), (14, 'Costes fijos sin amortización (€)'),
             (15, 'EBITDA (€)'), (16, 'Amortización (€)'),
             (17, 'EBIT — resultado de explotación (€)'),
             (18, 'Gastos financieros (€)'), (19, 'BAI — beneficio antes de '
                                                  'impuestos (€)'),
             (20, 'Impuesto de Sociedades (€)'), (21, 'Resultado neto (€)'),
             (22, 'Margen EBITDA (%)'))
    motor.val(ws, 'A10', 'CUENTA DE RESULTADOS PREVISIONAL', bold=True)
    for r, etiqueta in filas:
        motor.val(ws, 'A' + str(r), etiqueta)
    guarda = '=IF($B$11="","",'

    motor.f(ws, 'B11', '=IF(' + pl_ing + '=0,"",' + pl_ing + '*12)',
            fmt=FMT_EUR)
    motor.f(ws, 'B12', guarda + pl_var + '*12)', fmt=FMT_EUR)
    motor.f(ws, 'B14', guarda + pl_fij + '*12)', fmt=FMT_EUR)
    motor.f(ws, 'B16', guarda + (pl_amo + '*12)' if pl_amo else '0)'),
            fmt=FMT_EUR)
    for i, col in enumerate(('C', 'D')):
        ant = 'BC'[i]
        motor.f(ws, col + '11', guarda + ant + '11*(1+' + col + '6))',
                fmt=FMT_EUR)
        motor.f(ws, col + '12',
                guarda + ant + '12*(1+' + col + '6)*(1+' + col + '7))',
                fmt=FMT_EUR)
        motor.f(ws, col + '14', guarda + ant + '14*(1+' + col + '7))',
                fmt=FMT_EUR)
        motor.f(ws, col + '16', guarda + ant + '16)', fmt=FMT_EUR)
    for i, col in enumerate(('B', 'C', 'D')):
        f_fin = fin['primer_ano'] + i
        motor.f(ws, col + '13', guarda + col + '11-' + col + '12)',
                fmt=FMT_EUR)
        motor.f(ws, col + '15', guarda + col + '13-' + col + '14)',
                fmt=FMT_EUR, bold=True)
        motor.f(ws, col + '17', guarda + col + '15-' + col + '16)',
                fmt=FMT_EUR)
        motor.f(ws, col + '18',
                guarda + "IF(ISNUMBER('" + HOJA_FIN + "'!D" + str(f_fin)
                + "),'" + HOJA_FIN + "'!D" + str(f_fin) + ',0))', fmt=FMT_EUR)
        motor.f(ws, col + '19', guarda + col + '17-' + col + '18)',
                fmt=FMT_EUR)
        motor.f(ws, col + '20',
                guarda + 'IF(' + col + '19<=0,0,' + col + '19*' + col + '8))',
                fmt=FMT_EUR)
        motor.f(ws, col + '21', guarda + col + '19-' + col + '20)',
                fmt=FMT_EUR, bold=True)
        motor.f(ws, col + '22',
                guarda + 'IFERROR(' + col + '15/' + col + '11,""))',
                fmt=FMT_PCT)
    nota(ws, 'E11', 'Año 1 = P&L Mensual × 12. Si cambias el P&L, cambia la '
                    'proyección entera: no hay ni una constante aquí.')
    nota(ws, 'E18', 'Intereses del año, tomados del cuadro francés de la hoja '
                    '«' + HOJA_FIN + '».')
    _semaforo_negativo(ws, ['B', 'C', 'D'], (15, 21, 22))
    apunta(cambios, fname, ws, ('hoja CREADA' if nueva else 'hoja rehecha')
           + ': Año 1 por referencia al P&L, EBITDA→EBIT→BAI→IS→resultado '
             'neto, todo guardado con "" (TEC-07, DOM-06, COM-07)')


# --------------------------------------------------------------------------
# 2.3.5 · fondo de maniobra dimensionado  ·  2.3.6 · fuente única de CAPEX
# --------------------------------------------------------------------------
def fondo_de_maniobra(wb, fname, cambios, contenido, pl, hoja_inv, col_pres):
    """DOM-01/COM-30: el fondo de maniobra deja de ser un importe tecleado.

    `= (coste fijo mensual sin amortización + coste variable del mes) × meses`,
    con los meses en celda verde y **mínimo 6**, que es lo que pide el propio
    consejo del capítulo 4 («un gastronómico tarda 6-12 meses en alcanzar
    velocidad de crucero»). El rótulo NO se toca (§2.3.5).
    """
    ws = wb[hoja_inv]
    f_fondo = _fila(ws, r'^fondo de maniobra', obligatoria=False)
    if f_fondo is None:
        return None
    conf = ((getattr(contenido, 'PLAN', None) or {}).get('fondo_maniobra')
            if contenido else None) or {}
    meses = conf.get('meses', 6)
    base = ws.max_row + 2
    motor.val(ws, 'A' + str(base), 'FONDO DE MANIOBRA — cómo se calcula la '
              'fila ' + str(f_fondo), bold=True)
    motor.val(ws, 'A' + str(base + 1), 'Meses de colchón (mínimo 6)')
    motor.val(ws, col_pres + str(base + 1), meses, fmt=FMT_ENT, verde_=True)
    motor.fijar_formato(ws, col_pres + str(base + 1), FMT_ENT)
    motor.val(ws, 'A' + str(base + 2),
              'Coste mensual de estructura (fijos sin amortización + '
              'variables) (€)')
    motor.f(ws, col_pres + str(base + 2),
            "='P&L Mensual'!B" + str(pl['tot_fij']) + "+'P&L Mensual'!B"
            + str(pl['tot_var']), fmt=FMT_EUR)
    motor.val(ws, 'A' + str(base + 3), 'Fondo de maniobra necesario (€)')
    motor.f(ws, col_pres + str(base + 3),
            '=IF(' + col_pres + str(base + 2) + '=0,"",' + col_pres
            + str(base + 2) + '*' + col_pres + str(base + 1) + ')',
            fmt=FMT_EUR, bold=True)
    nota(ws, 'A' + str(base + 4),
         'Los 60.000 / 120.000 / 200.000 € que traía la tabla no cubren ni '
         'cuatro meses de la nómina más barata que describe el propio libro. '
         'Aquí se dimensiona con TUS costes: rellena el P&L Mensual y esta '
         'fila se calcula sola.')
    motor.f(ws, col_pres + str(f_fondo),
            '=IF(' + col_pres + str(base + 3) + '="","",' + col_pres
            + str(base + 3) + ')', fmt=FMT_EUR)
    motor.regla_expresion(ws, col_pres + str(base + 1),
                          '=AND(ISNUMBER(' + col_pres + str(base + 1) + '),'
                          + col_pres + str(base + 1) + '<6)')
    apunta(cambios, fname, ws, 'fondo de maniobra CALCULADO en ' + col_pres
           + str(f_fondo) + ' = estructura mensual × meses (verde en '
           + col_pres + str(base + 1) + ', mínimo 6) — DOM-01, COM-30')
    return base


def correspondencia_capex(wb, fname, cambios, contenido, hoja_inv, fila_cab):
    """§2.3.6 (TEC-26, COM-32) — los dos CAPEX se reconcilian SIN fusionar.

    `calculadora-capex.xlsx` queda como **hoja de rangos de mercado** y
    `plan-financiero!'Inversión'` como **«Mi CAPEX»**. La correspondencia se
    escribe en una columna nueva de la propia hoja, no con `externalLink`: un
    `.xlsx` movido de carpeta daría `#REF!` al cliente (§1.13, §7.1).
    """
    from openpyxl.utils import get_column_letter as gcl
    mapa = ((getattr(contenido, 'PLAN', None) or {}).get('capex_map')
            if contenido else None)
    if not mapa:
        return 0
    ws = wb[hoja_inv]
    col = gcl(ws.max_column + 1)
    cel = ws.cell(row=fila_cab, column=ws.max_column + 1,
                  value='Categoría equivalente en calculadora-capex.xlsx')
    cel.font = Font(bold=True, color='FFFFFF', size=10)
    cel.fill = motor.PatternFill('solid', fgColor='2D2D2D')
    cel.alignment = Alignment(horizontal='center', wrap_text=True)
    ws.column_dimensions[col].width = 34.0
    puestas = 0
    for patron, categoria in mapa.items():
        r = _fila(ws, patron, desde=fila_cab + 1, obligatoria=False)
        if r is None:
            continue
        motor.val(ws, col + str(r), categoria)
        puestas += 1
    apunta(cambios, fname, ws, 'columna ' + col + ' con la correspondencia de '
           + str(puestas) + ' conceptos hacia las categorías de '
           'calculadora-capex.xlsx (§2.3.6, TEC-26/COM-32)')
    return puestas


def instruccion(wb, texto, rx=None):
    """Línea en la hoja `Instrucciones`, sin duplicar en la 2.ª pasada."""
    if 'Instrucciones' not in wb.sheetnames:
        return None
    return motor.linea_instrucciones(wb['Instrucciones'], texto, rx)


RX_INSTR_FUENTE = re.compile(r'^Fuente de cada cifra:')
RX_INSTR_PROY = re.compile(r'^La pesta.a «Proyecci')
RX_INSTR_FIN = re.compile(r'^La pesta.a «Financiaci')


def plan_representante(wb, fname, cambios, contenido, subtitulo):
    pl = _pl_mensual_representante(wb, fname, cambios, contenido)
    fin = hoja_financiacion(wb, fname, cambios, contenido, subtitulo)
    hoja_proyeccion(wb, fname, cambios, contenido, subtitulo, pl, fin)
    fondo_de_maniobra(wb, fname, cambios, contenido, pl, 'Inversión', 'C')
    correspondencia_capex(wb, fname, cambios, contenido, 'Inversión', 4)
    _desviacion_sin_dato(wb['Inversión'], fname, cambios, 'C', 'D', 'E')
    instruccion(wb, 'La pestaña «' + HOJA_PROY + '» ya existe: el Año 1 sale '
                    'del P&L Mensual por referencia y los años 2 y 3 de los '
                    'dos porcentajes verdes.', RX_INSTR_PROY)
    instruccion(wb, 'La pestaña «' + HOJA_FIN + '» calcula la cuota del '
                    'préstamo y su cuadro de amortización; sus intereses '
                    'alimentan la proyección y su cuota mensual se repite en '
                    'cash-flow-break-even.xlsx.', RX_INSTR_FIN)
    instruccion(wb, 'Fuente de cada cifra: esta hoja «Inversión» es TU CAPEX '
                    '(el que va al banco). calculadora-capex.xlsx es la hoja '
                    'de RANGOS DE MERCADO, con el desglose por categorías; la '
                    'última columna de «Inversión» dice a qué categoría suya '
                    'corresponde cada concepto.', RX_INSTR_FUENTE)
    return 'inversion-conceptos'


def _desviacion_sin_dato(ws, fname, cambios, col_prev, col_real, col_desv):
    """§7-bis.13 en la columna de desviación de `Inversión`.

    Representante: `=IF(C5=0,0,(D5-C5)/C5)` pinta **0,0 %** en las 22 filas de
    un libro en blanco, como si el presupuesto cuadrase. Hermanos: `=D5-C5`
    pinta **−110.000 €** de «Diferencia» antes de que el cliente haya escrito
    un solo importe real. Las dos formas mienten con el libro vacío.
    """
    fila_cab = 4
    tocadas = 0
    for r in range(fila_cab + 1, ws.max_row + 1):
        cel = ws[col_desv + str(r)]
        if cel.data_type != 'f':
            continue
        motor.f(ws, col_desv + str(r),
                '=IF(' + col_real + str(r) + '="","",IFERROR((' + col_real
                + str(r) + '-' + col_prev + str(r) + ')/' + col_prev + str(r)
                + ',""))', fmt=FMT_PCT)
        tocadas += 1
    if tocadas:
        apunta(cambios, fname, ws, str(tocadas) + ' celdas de desviación que '
               'ya no dicen «0,0 %» ni una diferencia falsa con el libro en '
               'blanco (§7-bis.13)')
    return tocadas


def plan_hermanos(wb, fname, cambios, contenido, subtitulo):
    pl = _pl_mensual_hermanos(wb, fname, cambios, contenido)
    fin = hoja_financiacion(wb, fname, cambios, contenido, subtitulo)
    hoja_proyeccion(wb, fname, cambios, contenido, subtitulo, pl, fin)
    ws_inv = wb['Inversión']
    f_tot = _fila(ws_inv, r'^total inversion', col=2, obligatoria=False)
    fondo_de_maniobra(wb, fname, cambios, contenido, pl, 'Inversión', 'C')
    _diferencia_hermanos(ws_inv, fname, cambios)
    instruccion(wb, 'La pestaña «' + HOJA_PROY + '» ya existe: el Año 1 sale '
                    'del P&L Mensual por referencia.', RX_INSTR_PROY)
    instruccion(wb, 'La pestaña «' + HOJA_FIN + '» calcula la cuota del '
                    'préstamo y su cuadro de amortización.', RX_INSTR_FIN)
    return 'inversion-categorias', f_tot


def _diferencia_hermanos(ws, fname, cambios):
    """`E5='=D5-C5'` → `''` mientras `D` esté vacía (§7-bis.13)."""
    tocadas = 0
    for r in range(5, ws.max_row + 1):
        cel = ws['E' + str(r)]
        if cel.data_type != 'f' or 'SUM' in str(cel.value).upper():
            continue
        motor.f(ws, 'E' + str(r),
                '=IF(D' + str(r) + '="","",D' + str(r) + '-C' + str(r) + ')',
                fmt=FMT_EUR)
        tocadas += 1
    if tocadas:
        apunta(cambios, fname, ws, str(tocadas) + ' celdas de «Diferencia» que '
               'dejaban de mentir un −110.000 € con la columna Real vacía')
    return tocadas


def plan_panaderia(wb, fname, cambios, contenido, subtitulo):
    """NUEVO-02 (§2.5) — el EBITDA que vale exactamente la facturación.

    `B23` sumaba dos veces `B14:B16` y se dejaba fuera `B21`; `B24` restaba una
    fila **vacía** (`B22`), así que el «EBITDA» cacheado era 300.000 €, la
    FACTURACIÓN TOTAL; y `B25` dividía el total de COSTES entre la facturación
    y publicaba un margen del 122,97 % junto a una nota que dice «15-22 %
    objetivo». Las tres fórmulas se rehacen por estructura: del primer bloque de
    coste a la última línea de coste, sin saltarse ninguna ni repetir ninguna.
    """
    ws = wb['P&L 3 años']
    f_fact = _fila(ws, r'^facturacion total', fname=fname)
    f_var = _fila(ws, RX_BLOQUE_VAR, fname=fname)
    f_tot = _fila(ws, r'^total costes', fname=fname)
    f_eb = _fila(ws, RX_EBITDA, desde=f_tot, fname=fname)
    f_pct = _fila(ws, RX_PCT_EBITDA, desde=f_eb, fname=fname)
    ultima = _ultimo_detalle(ws, f_var + 1, f_tot - 1, (RX_BLOQUE_FIJ,))
    cols = ['B', 'C', 'D']
    for col in cols:
        motor.a_formula(ws, col + str(f_tot),
                        '=SUM(' + col + str(f_var + 1) + ':' + col
                        + str(ultima) + ')', fmt=FMT_EUR, informe=cambios,
                        fname=fname,
                        nota='NUEVO-02: sumaba dos veces el bloque de energía '
                             'y se dejaba fuera «Seguros + tasas + '
                             'amortización»')
        motor.a_formula(ws, col + str(f_eb),
                        '=' + col + str(f_fact) + '-' + col + str(f_tot),
                        fmt=FMT_EUR, informe=cambios, fname=fname,
                        nota='NUEVO-02: restaba una fila VACÍA, así que el '
                             'EBITDA era la facturación entera')
        motor.a_formula(ws, col + str(f_pct),
                        '=IF(' + col + str(f_fact) + '=0,"",' + col + str(f_eb)
                        + '/' + col + str(f_fact) + ')', fmt=FMT_PCT,
                        informe=cambios, fname=fname,
                        nota='NUEVO-02: dividía el TOTAL DE COSTES entre la '
                             'facturación y publicaba 122,97 %')
    _semaforo_negativo(ws, cols, (f_eb, f_pct))
    apunta(cambios, fname, ws, 'NUEVO-02 corregido: TOTAL COSTES = SUM('
           + str(f_var + 1) + ':' + str(ultima) + '), EBITDA = facturación − '
           'costes, margen = EBITDA / facturación')
    return 'pl-3-anos'


def plan_financiero(wb, fname, cambios, contenido, subtitulo):
    variante = variante_plan(wb, fname)
    if variante == 'inversion-conceptos':
        plan_representante(wb, fname, cambios, contenido, subtitulo)
    elif variante == 'inversion-categorias':
        plan_hermanos(wb, fname, cambios, contenido, subtitulo)
    else:
        plan_panaderia(wb, fname, cambios, contenido, subtitulo)
    return variante


# ==========================================================================
# §2.4 · cash-flow-break-even.xlsx  (TEC-03, DOM-09, COM-06, DOM-03, DOM-22)
# ==========================================================================
ET_NETO_IVA = 'FLUJO DE CAJA NETO CON IVA Y DEUDA'
ET_ACUM_IVA = 'FLUJO ACUMULADO CON IVA Y DEUDA'
ET_BE_MES = 'Mes de break-even de caja'


def variante_cash(wb, fname=''):
    hojas = set(wb.sheetnames)
    if 'Cash Flow 12 Meses' in hojas:
        return '12-meses-total', 'Cash Flow 12 Meses', None
    if 'Cash Flow' in hojas and 'Break-Even' in hojas:
        return 'cash-y-breakeven', 'Cash Flow', 'Break-Even'
    caja = [h for h in wb.sheetnames if _norm(h).startswith('cash flow')]
    if caja:
        return 'cash-plurianual', caja[0], None
    raise VarianteDesconocida(
        fname + ': libro de cash flow no reconocido. Hojas=' + repr(
            wb.sheetnames))


def _bloque_iva_y_deuda(ws, meses, total, fila_neto, fila_acum, cambios, fname,
                        contenido):
    """Las tres filas de IVA del modelo 303 + la cuota del préstamo (§2.4).

    El cash flow va **con IVA porque es caja**, y el IVA soportado del CAPEX
    (105-189 k€ sobre una inversión de 500-900 k€) es tesorería adelantada que
    hoy no aparece por ningún lado. Se monta como una CAPA sobre el flujo de
    la fila del flujo neto, sin insertar filas: `openpyxl.insert_rows` no
    reescribe las fórmulas y partiría los `SUM` horizontales que ya existen.
    """
    base = ws.max_row + 2
    motor.val(ws, 'A' + str(base),
              'IVA (MODELO 303) Y SERVICIO DE LA DEUDA', bold=True)
    celda_iva = motor.escribir_parametro(ws, base + 1, 'A', 'B',
                                         'iva_restauracion')
    motor.fijar_formato(ws, celda_iva, FMT_PCT)
    nota(ws, 'A' + str(base + 2),
         motor.PARAMETROS['iva_restauracion']['nota'] + ' Las filas de arriba '
         'se escriben SIN IVA, igual que el P&L; esta capa lo añade porque el '
         'cash flow es caja.')
    filas = {
        'repercutido': (base + 3, '(+) IVA repercutido (cobrado con las '
                                  'ventas)'),
        'soportado': (base + 4, '(-) IVA soportado (compras y gastos con IVA; '
                                'las nóminas y la Seguridad Social no llevan)'),
        'liquidacion': (base + 5, '(-) Liquidación de IVA (modelo 303) — '
                                  'trimestre natural, se ingresa del 1 al 20 '
                                  'del mes siguiente'),
        'cuota': (base + 6, '(-) Cuota del préstamo (capital + intereses) — la '
                            'calcula plan-financiero-3-anos.xlsx, hoja «'
                            + HOJA_FIN + '»'),
        'neto': (base + 7, ET_NETO_IVA),
        'acum': (base + 8, ET_ACUM_IVA),
        'q4': (base + 9, 'IVA del 4.º trimestre — se liquida en enero del año '
                         'siguiente (no es caja de este ejercicio)'),
    }
    for clave, (r, etiqueta) in filas.items():
        motor.val(ws, 'A' + str(r), etiqueta,
                  bold=clave in ('neto', 'acum'))
    conf = ((getattr(contenido, 'CASH', None) or {}) if contenido else {})
    cuota = (conf.get('cuota_mensual'))
    f_rep, f_sop = filas['repercutido'][0], filas['soportado'][0]
    f_liq, f_cuo = filas['liquidacion'][0], filas['cuota'][0]
    f_net, f_acu = filas['neto'][0], filas['acum'][0]

    for i, col in enumerate(meses):
        motor.f(ws, col + str(f_rep),
                '=' + col + str(fila_neto['ingresos']) + '*' + celda_iva,
                fmt=FMT_EUR)
        motor.val(ws, col + str(f_sop), None, fmt=FMT_EUR)
        motor.verde(ws, col + str(f_sop))
        motor.val(ws, col + str(f_cuo), cuota, fmt=FMT_EUR, verde_=True)
        # liquidación trimestral: abril, julio y octubre liquidan el trimestre
        # natural anterior (el 4.º cae fuera de los 12 meses y va en su fila)
        if i in (3, 6, 9):
            ini, fin = meses[i - 3], meses[i - 1]
            motor.f(ws, col + str(f_liq),
                    '=SUM(' + ini + str(f_rep) + ':' + fin + str(f_rep)
                    + ')-SUM(' + ini + str(f_sop) + ':' + fin + str(f_sop)
                    + ')', fmt=FMT_EUR)
        motor.f(ws, col + str(f_net),
                '=' + col + str(fila_neto['neto']) + '+' + col + str(f_rep)
                + '-' + col + str(f_sop) + '-' + ('IF(ISNUMBER(' + col
                + str(f_liq) + '),' + col + str(f_liq) + ',0)') + '-'
                + col + str(f_cuo), fmt=FMT_EUR, bold=True)
        if i == 0:
            motor.f(ws, col + str(f_acu), '=' + col + str(f_net), fmt=FMT_EUR,
                    bold=True)
        else:
            ant = meses[i - 1]
            motor.f(ws, col + str(f_acu),
                    '=' + ant + str(f_acu) + '+' + col + str(f_net),
                    fmt=FMT_EUR, bold=True)
    ultimo, primero = meses[-1], meses[0]
    motor.f(ws, (total or ultimo) + str(filas['q4'][0]),
            '=SUM(' + meses[9] + str(f_rep) + ':' + ultimo + str(f_rep)
            + ')-SUM(' + meses[9] + str(f_sop) + ':' + ultimo + str(f_sop)
            + ')', fmt=FMT_EUR)
    if total:
        for r in (f_rep, f_sop, f_liq, f_cuo, f_net):
            motor.f(ws, total + str(r),
                    '=SUM(' + primero + str(r) + ':' + ultimo + str(r) + ')',
                    fmt=FMT_EUR)
    motor.semaforo_isnumber(ws, primero + str(f_acu) + ':' + ultimo
                            + str(f_acu), primero + str(f_acu))
    apunta(cambios, fname, ws, 'capa de IVA (303) y cuota del préstamo en las '
           'filas ' + str(f_rep) + '-' + str(filas['q4'][0])
           + '; flujo neto y acumulado CON IVA y deuda en ' + str(f_net) + '/'
           + str(f_acu) + ' (DOM-03, DOM-22, §2.4)')
    return {'neto': f_net, 'acum': f_acu, 'liquidacion': f_liq,
            'cuota': f_cuo, 'iva': celda_iva}


def _bloque_break_even(ws, capa, meses, cambios, fname, contenido):
    """Break-even en MESES y en € (TEC-03, DOM-09, COM-06).

    El mes se lee sobre el acumulado **con IVA y deuda**: un break-even sin
    cuota de préstamo es un break-even falso (DOM-22). `MATCH(TRUE,INDEX(...))`
    está verificado con pycel en esta versión (SPEC, cabecera).
    """
    conf = ((getattr(contenido, 'CASH', None) or {}).get('break_even')
            if contenido else None) or {}
    base = ws.max_row + 2
    motor.val(ws, 'A' + str(base), 'BREAK-EVEN', bold=True)
    campos = ((base + 1, 'Costes fijos mensuales (€)', conf.get('costes_fijos'),
               FMT_EUR, True),
              (base + 2, 'Margen de contribución (%)',
               conf.get('margen_contribucion'), FMT_PCT, True),
              (base + 3, 'Umbral de ventas mensual (€)', None, FMT_EUR, False),
              (base + 4, 'Ticket medio (€)', conf.get('ticket_medio'),
               FMT_EUR, True),
              (base + 5, 'Días abierto/mes', conf.get('dias_mes'), FMT_ENT,
               True),
              (base + 6, 'Cubiertos/día necesarios', None, FMT_ENT, False),
              (base + 7, ET_BE_MES, None, 'General', False))
    for fila, etiqueta, valor, fmt, editable in campos:
        motor.val(ws, 'A' + str(fila), etiqueta)
        if editable:
            motor.val(ws, 'B' + str(fila), valor, fmt=fmt, verde_=True)
            motor.fijar_formato(ws, 'B' + str(fila), fmt)
    motor.f(ws, 'B' + str(base + 3),
            '=IFERROR(B' + str(base + 1) + '/B' + str(base + 2) + ',"")',
            fmt=FMT_EUR, bold=True)
    motor.f(ws, 'B' + str(base + 6),
            '=IFERROR(B' + str(base + 3) + '/(B' + str(base + 4) + '*B'
            + str(base + 5) + '),"")', fmt=FMT_ENT, bold=True)
    motor.fijar_formato(ws, 'B' + str(base + 3), FMT_EUR)
    motor.fijar_formato(ws, 'B' + str(base + 6), FMT_ENT)
    motor.f(ws, 'B' + str(base + 7),
            '=IFERROR(MATCH(TRUE,INDEX(' + meses[0] + str(capa['acum']) + ':'
            + meses[-1] + str(capa['acum']) + '>0,0),0),"No alcanzado")',
            bold=True)
    nota(ws, 'A' + str(base + 8),
         'El mes de break-even se lee sobre el FLUJO ACUMULADO CON IVA Y '
         'DEUDA: un punto de equilibrio sin la cuota del préstamo es un punto '
         'de equilibrio falso. Si el acumulado nunca cruza a positivo, la '
         'celda dice «No alcanzado» — no un número.')
    apunta(cambios, fname, ws, 'break-even en meses y en € en las filas '
           + str(base + 1) + '-' + str(base + 7) + ' (TEC-03, DOM-09, COM-06)')
    return base


def cash_flow(wb, fname, cambios, contenido, subtitulo):
    variante, nombre_caja, nombre_be = variante_cash(wb, fname)
    ws = wb[nombre_caja]
    fila_cab = motor.fila_cabecera_tabla(ws) or 4
    meses, total = columnas_mes(ws, fila_cab)
    if len(meses) < 12:
        raise VarianteDesconocida(
            fname + ':' + ws.title + ': ' + str(len(meses)) + ' columnas de '
            'mes leídas en la cabecera de la fila ' + str(fila_cab)
            + ' (se esperaban 12)')
    meses = meses[:12]

    f_ing_bloque = _fila(ws, r'^ingresos$|^entradas$', fname=fname)
    f_tot_ing = _fila(ws, r'^total ingresos$|^total entradas$', fname=fname)
    f_gas_bloque = _fila(ws, r'^gastos$|^salidas$', fname=fname)
    f_tot_gas = _fila(ws, r'^total gastos$|^total salidas$', fname=fname)
    f_neto = _fila(ws, r'^flujo de caja neto$|^flujo neto mensual$',
                   fname=fname)
    f_acum = _fila(ws, r'^flujo acumulado$|^saldo acumulado$', fname=fname)
    f_saldo = _fila(ws, r'^saldo inicial$', obligatoria=False)

    for i, col in enumerate(meses):
        motor.f(ws, col + str(f_tot_ing),
                '=SUM(' + col + str(f_ing_bloque + 1) + ':' + col
                + str(f_tot_ing - 1) + ')', fmt=FMT_EUR)
        motor.f(ws, col + str(f_tot_gas),
                '=SUM(' + col + str(f_gas_bloque + 1) + ':' + col
                + str(f_tot_gas - 1) + ')', fmt=FMT_EUR)
        motor.f(ws, col + str(f_neto),
                '=' + col + str(f_tot_ing) + '-' + col + str(f_tot_gas),
                fmt=FMT_EUR, bold=True)
        if i == 0:
            arranque = ('=' + col + str(f_saldo) + '+' + col + str(f_neto)) \
                if f_saldo else ('=' + col + str(f_neto))
            motor.f(ws, col + str(f_acum), arranque, fmt=FMT_EUR, bold=True)
        else:
            ant = meses[i - 1]
            motor.f(ws, col + str(f_acum),
                    '=' + ant + str(f_acum) + '+' + col + str(f_neto),
                    fmt=FMT_EUR, bold=True)
            if f_saldo:
                motor.f(ws, col + str(f_saldo), '=' + ant + str(f_acum),
                        fmt=FMT_EUR)
    if total:
        for r in (f_tot_ing, f_tot_gas, f_neto):
            motor.f(ws, total + str(r),
                    '=SUM(' + meses[0] + str(r) + ':' + meses[-1] + str(r)
                    + ')', fmt=FMT_EUR)
    motor.semaforo_isnumber(ws, meses[0] + str(f_acum) + ':' + meses[-1]
                            + str(f_acum), meses[0] + str(f_acum))
    apunta(cambios, fname, ws, 'totales, flujo neto y flujo acumulado en las '
           'filas ' + str(f_tot_ing) + '/' + str(f_tot_gas) + '/' + str(f_neto)
           + '/' + str(f_acum) + ' sobre ' + str(len(meses))
           + ' meses (TEC-03, DOM-09)')

    capa = _bloque_iva_y_deuda(ws, meses, total,
                               {'ingresos': f_tot_ing, 'neto': f_neto},
                               f_acum, cambios, fname, contenido)
    destino = wb[nombre_be] if nombre_be else ws
    if nombre_be:
        _break_even_hoja_propia(destino, capa, meses, ws.title, cambios, fname,
                                contenido)
    else:
        _bloque_break_even(ws, capa, meses, cambios, fname, contenido)
    instruccion(wb, 'El break-even se lee sobre el flujo acumulado CON IVA y '
                    'con la cuota del préstamo: sin la cuota, el punto de '
                    'equilibrio sale antes de tiempo.',
                re.compile(r'^El break-even se lee'))
    return variante


def _break_even_hoja_propia(ws, capa, meses, hoja_caja, cambios, fname,
                            contenido):
    """Hermanos: la hoja `Break-Even` YA existe con `B11` y `B12` y deja
    **vacía justo `B13` «Break-Even (meses)»** — la celda que da nombre al
    fichero."""
    conf = ((getattr(contenido, 'CASH', None) or {}).get('break_even')
            if contenido else None) or {}
    f_fact = _fila(ws, r'^facturacion mensual estimada', obligatoria=False)
    f_margen = _fila(ws, r'^margen contribucion|^margen de contribucion',
                     obligatoria=False)
    f_be = _fila(ws, r'^break-?even \(meses\)|^break-?even$', fname=fname)
    f_cf = _fila(ws, r'^costes fijos mensuales', obligatoria=False)
    motor.f(ws, 'B' + str(f_be),
            "=IFERROR(MATCH(TRUE,INDEX('" + hoja_caja + "'!" + meses[0]
            + str(capa['acum']) + ':' + meses[-1] + str(capa['acum'])
            + ">0,0),0),\"No alcanzado\")", bold=True)
    base = ws.max_row + 2
    motor.val(ws, 'A' + str(base), 'Umbral de ventas mensual (€)')
    if f_cf and f_margen:
        motor.f(ws, 'B' + str(base),
                '=IFERROR(B' + str(f_cf) + '/(1-B' + str(
                    _fila(ws, r'^food cost', fname=fname)) + '),"")',
                fmt=FMT_EUR, bold=True)
    nota(ws, 'A' + str(base + 1),
         'El mes de break-even se lee sobre el flujo acumulado CON IVA y '
         'deuda de la hoja «' + hoja_caja + '». Si nunca cruza a positivo, '
         'dice «No alcanzado».')
    apunta(cambios, fname, ws, 'B' + str(f_be) + ' (la celda que da nombre al '
           'fichero) deja de estar vacía + umbral de ventas (TEC-03, DOM-09)')


# ==========================================================================
# §2.3.6 · calculadora-capex.xlsx — hoja de RANGOS de mercado
# ==========================================================================
RX_INSTR_RANGOS = re.compile(r'^Esta calculadora es la hoja de RANGOS')


def variante_capex(wb, fname=''):
    """`'rangos'` | `'desglosado'` | `'min-max'`, por la CABECERA."""
    for ws in wb.worksheets:
        if ws.title == 'Instrucciones':
            continue
        for fila in (3, 4):
            cab = [_norm(ws.cell(row=fila, column=c).value)
                   for c in range(1, ws.max_column + 1)]
            if any(c.startswith('rango bajo') for c in cab):
                return 'rangos', ws, fila
            if any(c.startswith('importe minimo') for c in cab):
                return 'min-max', ws, fila
            if 'partida' in cab and any(c.startswith('estimado') for c in cab):
                return 'desglosado', ws, fila
    raise VarianteDesconocida(
        fname + ': calculadora de CAPEX no reconocida. Hojas='
        + repr(wb.sheetnames))


def _fila_total(ws, fila_cab):
    """Fila TOTAL y última fila de datos por encima de ella, MEDIDAS."""
    f_total = None
    for r in range(fila_cab + 1, ws.max_row + 1):
        for c in range(1, ws.max_column + 1):
            v = _norm(ws.cell(row=r, column=c).value)
            if v.startswith('total'):
                f_total = r
                break
        if f_total:
            break
    if f_total is None:
        return None, None
    ultima = f_total - 1
    while ultima > fila_cab and all(
            ws.cell(row=ultima, column=c).value is None
            for c in range(1, ws.max_column + 1)):
        ultima -= 1
    return f_total, ultima


def calculadora_capex(wb, fname, cambios, contenido, subtitulo):
    variante, ws, fila_cab = variante_capex(wb, fname)
    f_total, ultima = _fila_total(ws, fila_cab)
    if f_total is None:
        raise VarianteDesconocida(fname + ':' + ws.title
                                  + ': no encuentro la fila TOTAL')
    # Los SUM del total se rehacen SIEMPRE contra el rango MEDIDO. En panadería
    # `B31='=SUM(B4:B27)'` se dejaba fuera «Licencias + proyectos + tasas» y
    # «Fondo maniobra 4 meses»: 113.700 € cacheados donde la suma correcta es
    # 136.200 € (y 278.100 € frente a 316.100 € en el máximo).
    reparadas = []
    for c in range(1, ws.max_column + 1):
        cel = ws.cell(row=f_total, column=c)
        if cel.data_type != 'f' or 'SUM' not in str(cel.value).upper():
            continue
        from openpyxl.utils import get_column_letter as gcl
        col = gcl(c)
        nueva = '=SUM(' + col + str(fila_cab + 1) + ':' + col + str(ultima) \
            + ')'
        if _norm(cel.value) != _norm(nueva):
            reparadas.append(col + str(f_total) + ': ' + str(cel.value)
                             + ' → ' + nueva)
        motor.f(ws, col + str(f_total), nueva, fmt=FMT_EUR, bold=True)
    if reparadas:
        apunta(cambios, fname, ws, 'rango del TOTAL rehecho contra las filas '
               'MEDIDAS ' + str(fila_cab + 1) + '-' + str(ultima) + ': '
               + str(reparadas))

    # semáforo «tu presupuesto frente al rango», sólo donde hay rango
    if variante in ('rangos', 'min-max'):
        cols = _columnas_rango(ws, fila_cab)
        if cols:
            bajo, alto, propio = cols
            fila = f_total + 2
            motor.val(ws, 'A' + str(fila),
                      'Tu presupuesto frente al rango de mercado')
            motor.f(ws, propio + str(fila),
                    '=IF(' + propio + str(f_total) + '=0,"",IF(' + propio
                    + str(f_total) + '<' + bajo + str(f_total)
                    + ',"Por debajo del rango bajo",IF(' + propio
                    + str(f_total) + '>' + alto + str(f_total)
                    + ',"Por encima del rango alto","Dentro del rango")))')
            apunta(cambios, fname, ws, 'aviso de encaje del presupuesto propio '
                   'en ' + propio + str(fila) + ' (§2.3.6)')
    instruccion(wb, 'Esta calculadora es la hoja de RANGOS DE MERCADO. TU '
                    'CAPEX, el que va al banco, se rellena en '
                    'plan-financiero-3-anos.xlsx, hoja «Inversión», que trae '
                    'la correspondencia concepto → categoría de esta hoja. Los '
                    'dos libros se comparan; ninguno lee del otro (un .xlsx '
                    'movido de carpeta daría #REF!).', RX_INSTR_RANGOS)
    return variante


def _columnas_rango(ws, fila_cab):
    from openpyxl.utils import get_column_letter as gcl
    bajo = alto = propio = None
    for c in range(2, ws.max_column + 1):
        cab = _norm(ws.cell(row=fila_cab, column=c).value)
        if cab.startswith('rango bajo') or cab.startswith('importe minimo'):
            bajo = gcl(c)
        elif cab.startswith('rango alto') or cab.startswith('importe maximo'):
            alto = gcl(c)
        elif cab.startswith('tu presupuesto') or cab.startswith('tu importe'):
            propio = gcl(c)
    return (bajo, alto, propio) if (bajo and alto and propio) else None


# ==========================================================================
# CONTRATO con main.py
# ==========================================================================
DESPACHO = {
    'calculadora-ticket-medio.xlsx': ticket_medio,
    'pl-mensual-escenarios.xlsx': pl_mensual,
    'plan-financiero-3-anos.xlsx': plan_financiero,
    'cash-flow-break-even.xlsx': cash_flow,
    'calculadora-capex.xlsx': calculadora_capex,
}
VARIANTES = {}


def _subtitulo(wb):
    for ws in wb.worksheets:
        v = ws['A2'].value
        if isinstance(v, str) and v.strip():
            return v.strip()
    return 'AI Chef Pro · aichef.pro'


def post(wb, fname, cambios, registro, contenido):
    """Se ejecuta DESPUÉS de `motor.aplicar` y ANTES de `motor.cerrar`.

    Las fórmulas se escriben con `motor.f`, así que quedan registradas y
    `main.py` verifica una por una que acabaron con valor cacheado.
    """
    fn = DESPACHO.get(fname)
    if fn is None:
        return
    subtitulo = _subtitulo(wb)
    if fn is ticket_medio or fn is pl_mensual:
        variante = fn(wb, fname, cambios, contenido)
    else:
        variante = fn(wb, fname, cambios, contenido, subtitulo)
    VARIANTES[fname] = variante
    cambios.append(fname + ': grupo_a variante ' + repr(variante) + ' ('
                   + SPEC + ')')


# ==========================================================================
# DEMOSTRACIONES (pycel) — sobre COPIAS desechables, nunca sobre entregables
# ==========================================================================
def _compilar(carpeta, destino, fname):
    import os
    import shutil
    from pycel import ExcelCompiler
    os.makedirs(destino, exist_ok=True)
    copia = os.path.join(destino, 'a_' + fname)
    shutil.copy2(os.path.join(carpeta, fname), copia)
    return ExcelCompiler(filename=copia)


def _ev(xl, ref):
    import contextlib
    import os
    with open(os.devnull, 'w') as dn, contextlib.redirect_stderr(dn):
        try:
            return xl.evaluate(ref)
        except Exception as e:                               # noqa: BLE001
            return 'ERR:' + type(e).__name__ + ':' + str(e)[:90]


def _set(xl, ref, valor):
    _ev(xl, ref)
    xl.set_value(ref, valor)


def _num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def _busca(carpeta, fname, hoja, patron):
    """Fila por etiqueta en el fichero YA escrito (las demos no adivinan)."""
    import os
    import openpyxl
    wb = openpyxl.load_workbook(os.path.join(carpeta, fname))
    if hoja not in wb.sheetnames:
        return None, wb
    return _fila(wb[hoja], patron, obligatoria=False), wb


def demos(carpeta, destino, contenido):
    import os
    fuera, fallos = {}, []
    for nombre, fn in (('ticket_medio', _demo_ticket),
                       ('pl_escenarios', _demo_pl),
                       ('plan_financiero', _demo_plan),
                       ('cash_flow', _demo_cash),
                       ('capex', _demo_capex)):
        try:
            r = fn(carpeta, destino)
        except Exception as e:                               # noqa: BLE001
            r = {'error': type(e).__name__ + ': ' + str(e)[:200]}
        if r is None:
            continue
        fallos += r.pop('fallos', [])
        fuera[nombre] = r
    if not any(os.path.isfile(os.path.join(carpeta, f)) for f in FICHEROS):
        return {'grupo_a': {'aplica': False}, 'fallos': []}
    return {'grupo_a': fuera, 'fallos': fallos}


def _demo_ticket(carpeta, destino):
    import os
    fname = 'calculadora-ticket-medio.xlsx'
    if not os.path.isfile(os.path.join(carpeta, fname)):
        return None
    f_ticket, wb = _busca(carpeta, fname, 'Ticket Medio',
                          RX_TICKET_RES.pattern)
    if f_ticket is None:
        return {'fallos': [fname + ': no hay fila de TICKET MEDIO tras el '
                           'grupo A']}
    ws = wb['Ticket Medio']
    f_mix = _fila(ws, RX_ETIQUETA_MIX.pattern, obligatoria=False)
    f_fmes = _fila(ws, r'^facturacion mensual', obligatoria=False)
    f_dias = _fila(ws, r'^dias abierto', obligatoria=False)
    pares, sueltos = pares_mix(ws, 4, f_ticket - 1)
    xl = _compilar(carpeta, destino, fname)
    P = "'Ticket Medio'!"
    fallos = []
    r = {'fichero': fname, 'celda_ticket': 'B' + str(f_ticket),
         'pares': pares, 'incondicionales': sueltos}
    r['ticket_base'] = _ev(xl, P + 'B' + str(f_ticket))
    # (1) mover un PRECIO sube el ticket
    precio = 'B' + str(pares[0][1])
    v0 = _ev(xl, P + precio)
    _set(xl, P + precio, (v0 or 0) + 10)
    r['ticket_tras_subir_' + precio + '_10eur'] = _ev(xl, P + 'B'
                                                      + str(f_ticket))
    if _num(r['ticket_base']) and _num(r['ticket_tras_subir_' + precio
                                         + '_10eur']):
        if r['ticket_tras_subir_' + precio + '_10eur'] <= r['ticket_base']:
            fallos.append(fname + ': subir ' + precio + ' 10 € NO sube el '
                          'ticket ponderado')
    _set(xl, P + precio, v0)
    # (2) los días del mes sólo mueven la facturación mensual
    if f_fmes and f_dias:
        r['fact_mes_base'] = _ev(xl, P + 'B' + str(f_fmes))
        d0 = _ev(xl, P + 'B' + str(f_dias))
        _set(xl, P + 'B' + str(f_dias), (d0 or 0) + 4)
        r['fact_mes_mas_4_dias'] = _ev(xl, P + 'B' + str(f_fmes))
        if _num(r['fact_mes_base']) and _num(r['fact_mes_mas_4_dias']) \
                and r['fact_mes_mas_4_dias'] <= r['fact_mes_base']:
            fallos.append(fname + ': +4 días abiertos NO sube la facturación '
                          'mensual')
        _set(xl, P + 'B' + str(f_dias), d0)
    # (3) el control del mix se dispara si los tramos no suman 100 %
    if f_mix:
        r['mix_base'] = _ev(xl, P + 'B' + str(f_mix))
        tramos = [p for p, _q in pares
                  if ws['B' + str(f_mix)].value
                  and ('B' + str(p)) in ws['B' + str(f_mix)].value]
        for p in tramos:
            _set(xl, P + 'B' + str(p), 0.4)
        r['tramos_del_control'] = tramos
        r['mix_con_los_tres_al_40pct'] = _ev(xl, P + 'B' + str(f_mix))
        if _num(r['mix_base']) and abs(r['mix_base'] - 1) > 0.001:
            fallos.append(fname + ': el ejemplo precargado NO suma 100 % de '
                          'comensales (' + str(r['mix_base']) + ')')
        if _num(r['mix_con_los_tres_al_40pct']) \
                and abs(r['mix_con_los_tres_al_40pct'] - 1.2) > 0.001:
            fallos.append(fname + ': con los tres tramos al 40 % el control '
                          'debería dar 1,2 y da '
                          + str(r['mix_con_los_tres_al_40pct']))
    return dict(r, fallos=fallos)


def _demo_pl(carpeta, destino):
    import os
    fname = 'pl-mensual-escenarios.xlsx'
    ruta = os.path.join(carpeta, fname)
    if not os.path.isfile(ruta):
        return None
    import openpyxl
    wb = openpyxl.load_workbook(ruta)
    variante = motor.variante_pl(wb)
    hoja_nombre = ('Escenarios' if variante == 'escenarios-columnas'
                   else ('Pesimista' if variante == 'tres-hojas'
                         else 'P&L 3 escenarios'))
    ws = wb[hoja_nombre]
    xl = _compilar(carpeta, destino, fname)
    P = "'" + hoja_nombre + "'!"
    fallos, r = [], {'fichero': fname, 'variante': variante,
                     'hoja': hoja_nombre}
    f_fact = _fila(ws, r'^facturacion mensual|^total ingresos'
                       r'|^facturacion total mensual', obligatoria=False)
    f_eb = _fila(ws, RX_EBITDA, obligatoria=False)
    f_me = _fila(ws, RX_PCT_EBITDA, obligatoria=False)
    f_mov = _fila(ws, r'^cubiertos.*comida|^ventas sala|^tickets/dia',
                  obligatoria=False)
    if not (f_fact and f_eb):
        return {'fallos': [fname + ': no encuentro facturación o EBITDA tras '
                           'el grupo A'], 'variante': variante}
    for clave, fila in (('facturacion', f_fact), ('ebitda', f_eb),
                        ('margen', f_me)):
        if fila:
            r[clave + '_base'] = _ev(xl, P + 'B' + str(fila))
    if f_mov:
        v0 = _ev(xl, P + 'B' + str(f_mov))
        if _num(v0):
            _set(xl, P + 'B' + str(f_mov), v0 * 1.2)
            r['facturacion_mas_20pct_entrada'] = _ev(xl, P + 'B' + str(f_fact))
            r['ebitda_mas_20pct_entrada'] = _ev(xl, P + 'B' + str(f_eb))
            for clave in ('facturacion', 'ebitda'):
                a, b = r.get(clave + '_base'), r.get(clave + '_mas_20pct_entrada')
                if _num(a) and _num(b) and b <= a:
                    fallos.append(fname + ': subir «'
                                  + str(ws['A' + str(f_mov)].value)[:40]
                                  + '» un 20 % NO sube ' + clave
                                  + ' (' + str(a) + ' → ' + str(b) + ')')
            _set(xl, P + 'B' + str(f_mov), v0)
    # con ingresos a 0 el margen devuelve "" (§7-bis.13), nunca «0,0 %»
    if f_me:
        for fila_ing in _lineas_de_ingreso(ws, f_fact):
            _set(xl, P + 'B' + str(fila_ing), 0)
        r['margen_con_ingresos_cero'] = _ev(xl, P + 'B' + str(f_me))
        if r['margen_con_ingresos_cero'] not in ('', None):
            fallos.append(fname + ': con la facturación a 0 el margen devuelve '
                          + repr(r['margen_con_ingresos_cero'])
                          + ' en vez de "" (§7-bis.13)')
    return dict(r, fallos=fallos)


def _lineas_de_ingreso(ws, f_fact):
    """Celdas de entrada que alimentan la facturación (para ponerla a cero)."""
    f_ing = _fila(ws, RX_BLOQUE_ING, obligatoria=False)
    if f_ing and f_ing < f_fact:
        return list(range(f_ing + 1, f_fact))
    return [r for r, _n, _c in etiquetas(ws, 1, 5, f_fact - 1)
            if ws['B' + str(r)].data_type != 'f']


def _demo_plan(carpeta, destino):
    import os
    fname = 'plan-financiero-3-anos.xlsx'
    ruta = os.path.join(carpeta, fname)
    if not os.path.isfile(ruta):
        return None
    import openpyxl
    wb = openpyxl.load_workbook(ruta)
    fallos, r = [], {'fichero': fname, 'hojas': wb.sheetnames}
    xl = _compilar(carpeta, destino, fname)

    # (1) EBITDA que NO resta amortización + EBIT (TEC-08): el caso medido del
    #     R1 — ventas 140.000 €, amortización 6.000 € → EBITDA 32.000 € y
    #     EBIT 26.000 €, donde la v1.1 daba 26.000 € rotulado «EBITDA».
    if 'P&L Mensual' in wb.sheetnames:
        ws = wb['P&L Mensual']
        P = "'P&L Mensual'!"
        f_ing = _fila(ws, RX_TOT_INGRESOS, obligatoria=False)
        f_amort = _fila(ws, r'^amortizacion equipamiento', obligatoria=False)
        f_eb = _fila(ws, RX_EBITDA, obligatoria=False)
        f_me = _fila(ws, RX_PCT_EBITDA, obligatoria=False)
        f_ebit = _fila(ws, r'^ebit ', obligatoria=False)
        f_ing_bloque = _fila(ws, RX_BLOQUE_ING, obligatoria=False)
        f_fij = _fila(ws, RX_BLOQUE_FIJ, obligatoria=False)
        f_tot_fij = _fila(ws, RX_TOT_FIJOS, obligatoria=False)
        if f_ing and f_amort and f_eb and f_ebit:
            r['margen_formato'] = ws['B' + str(f_me)].number_format
            if r['margen_formato'] != FMT_PCT:
                fallos.append(fname + ": 'P&L Mensual'!B" + str(f_me)
                              + ' sigue en ' + repr(r['margen_formato'])
                              + ' y no en 0.0% (TEC-09)')
            r['margen_con_libro_en_blanco'] = _ev(xl, P + 'B' + str(f_me))
            if r['margen_con_libro_en_blanco'] not in ('', None):
                fallos.append(fname + ': con el libro en blanco el margen dice '
                              + repr(r['margen_con_libro_en_blanco'])
                              + ' (§7-bis.13: debe ser "")')
            _set(xl, P + 'B' + str(f_ing_bloque + 1), 140000)
            for fila in range(f_fij + 1, f_tot_fij):
                _set(xl, P + 'B' + str(fila), 0)
            _set(xl, P + 'B' + str(f_amort), 6000)
            r['ventas'] = _ev(xl, P + 'B' + str(f_ing))
            r['costes_fijos_sin_amortizacion'] = _ev(xl, P + 'B'
                                                     + str(f_tot_fij))
            r['ebitda'] = _ev(xl, P + 'B' + str(f_eb))
            r['ebit'] = _ev(xl, P + 'B' + str(f_ebit))
            if not (_num(r['ebitda']) and abs(r['ebitda'] - 140000) < 0.01):
                fallos.append(fname + ': con ventas 140.000 € y amortización '
                              '6.000 € (y el resto de fijos a 0) el EBITDA '
                              'debería ser 140.000 € y es ' + str(r['ebitda']))
            if not (_num(r['ebit']) and abs(r['ebit'] - 134000) < 0.01):
                fallos.append(fname + ': el EBIT debería ser el EBITDA menos '
                              'los 6.000 € de amortización y es '
                              + str(r['ebit']))
            r['diferencia_ebitda_ebit'] = (
                round(r['ebitda'] - r['ebit'], 2)
                if _num(r['ebitda']) and _num(r['ebit']) else None)

    # (2) cuadro francés: valor de control de la familia
    if HOJA_FIN in wb.sheetnames:
        F = "'" + HOJA_FIN + "'!"
        xl2 = _compilar(carpeta, destino, fname)
        _set(xl2, F + 'B5', 100000)
        _set(xl2, F + 'B6', 5)
        _set(xl2, F + 'B7', 0.05)
        _set(xl2, F + 'B8', 0)
        r['cuota_mensual_100k_5pct_60meses'] = _ev(xl2, F + 'B12')
        cuota = r['cuota_mensual_100k_5pct_60meses']
        if not (_num(cuota) and abs(cuota - 1887.12) < 0.01):
            fallos.append(fname + ': la anualidad de 100.000 € al 5 % en 60 '
                          'meses debe dar 1.887,12 €/mes y da ' + str(cuota))
        r['cuadro_100k_5anos'] = [
            {'ano': _ev(xl2, F + 'A' + str(18 + i)),
             'capital_inicial': _ev(xl2, F + 'B' + str(18 + i)),
             'cuota': _ev(xl2, F + 'C' + str(18 + i)),
             'intereses': _ev(xl2, F + 'D' + str(18 + i)),
             'pendiente': _ev(xl2, F + 'F' + str(18 + i))}
            for i in range(ANOS_CUADRO)]
        pend = r['cuadro_100k_5anos'][4]['pendiente']
        if not (_num(pend) and abs(pend) < 0.01):
            fallos.append(fname + ': con plazo 5 el capital pendiente al final '
                          'del año 5 debería ser 0 y es ' + str(pend))
        apagados = r['cuadro_100k_5anos'][5:]
        if any(not _num(x['cuota']) or abs(x['cuota']) > 0.01
               for x in apagados):
            fallos.append(fname + ': pasado el vencimiento el cuadro no se '
                          'apaga a 0 numérico: '
                          + repr([x['cuota'] for x in apagados]))
        # carencia >= plazo: aviso de TEXTO en C, numéricas B, D y F
        xl3 = _compilar(carpeta, destino, fname)
        _set(xl3, F + 'B5', 100000)
        _set(xl3, F + 'B6', 3)
        _set(xl3, F + 'B7', 0.05)
        _set(xl3, F + 'B8', 3)
        r['carencia_igual_al_plazo'] = {
            'C18': _ev(xl3, F + 'C18'), 'B18': _ev(xl3, F + 'B18'),
            'D18': _ev(xl3, F + 'D18'), 'F18': _ev(xl3, F + 'F18')}
        g = r['carencia_igual_al_plazo']
        if g['C18'] != AVISO_CARENCIA:
            fallos.append(fname + ': con carencia = plazo, C18 debería avisar '
                          'y dice ' + repr(g['C18']))
        for celda in ('B18', 'D18', 'F18'):
            if not _num(g[celda]):
                fallos.append(fname + ': con carencia = plazo, ' + celda
                              + ' deja de ser numérica (' + repr(g[celda])
                              + '): propagaría #¡VALOR! al P&L')

    # (3) la proyección sigue al P&L y responde a los dos porcentajes
    if HOJA_PROY in wb.sheetnames and 'P&L Mensual' in wb.sheetnames:
        ws = wb['P&L Mensual']
        f_ing_bloque = _fila(ws, RX_BLOQUE_ING, obligatoria=False)
        Q = "'" + HOJA_PROY + "'!"
        xl4 = _compilar(carpeta, destino, fname)
        r['proyeccion_con_libro_en_blanco'] = {
            'B11': _ev(xl4, Q + 'B11'), 'D21': _ev(xl4, Q + 'D21')}
        if r['proyeccion_con_libro_en_blanco']['B11'] not in ('', None):
            fallos.append(fname + ': con el P&L en blanco la proyección '
                          'devuelve ' + repr(
                              r['proyeccion_con_libro_en_blanco']['B11'])
                          + ' en vez de "" (§7-bis.13)')
        _set(xl4, "'P&L Mensual'!B" + str(f_ing_bloque + 1), 140000)
        r['proy_ano1'] = _ev(xl4, Q + 'B11')
        r['proy_ano3_base'] = _ev(xl4, Q + 'D11')
        if not (_num(r['proy_ano1']) and abs(r['proy_ano1'] - 1680000) < 1):
            fallos.append(fname + ': el Año 1 de la proyección debería ser '
                          '140.000 × 12 = 1.680.000 € y es '
                          + str(r['proy_ano1']))
        c0 = _ev(xl4, Q + 'C6')
        _set(xl4, Q + 'C6', (c0 or 0) + 0.1)
        r['proy_ano3_con_10pct_mas_de_crecimiento'] = _ev(xl4, Q + 'D11')
        a, b = r['proy_ano3_base'], r['proy_ano3_con_10pct_mas_de_crecimiento']
        if _num(a) and _num(b) and b <= a:
            fallos.append(fname + ': +10 puntos de crecimiento en el año 2 NO '
                          'suben los ingresos del año 3 (' + str(a) + ' → '
                          + str(b) + ')')
    return dict(r, fallos=fallos)


def _demo_cash(carpeta, destino):
    import os
    fname = 'cash-flow-break-even.xlsx'
    ruta = os.path.join(carpeta, fname)
    if not os.path.isfile(ruta):
        return None
    import openpyxl
    wb = openpyxl.load_workbook(ruta)
    variante, nombre_caja, nombre_be = variante_cash(wb, fname)
    ws = wb[nombre_caja]
    fila_cab = motor.fila_cabecera_tabla(ws) or 4
    meses, _total = columnas_mes(ws, fila_cab)
    meses = meses[:12]
    f_ing_bloque = _fila(ws, r'^ingresos$|^entradas$', obligatoria=False)
    f_tot_ing = _fila(ws, r'^total ingresos$|^total entradas$',
                      obligatoria=False)
    f_gas_bloque = _fila(ws, r'^gastos$|^salidas$', obligatoria=False)
    f_tot_gas = _fila(ws, r'^total gastos$|^total salidas$', obligatoria=False)
    f_acum = _fila(ws, r'^flujo acumulado$|^saldo acumulado$',
                   obligatoria=False)
    f_acum_iva = _fila(ws, r'^flujo acumulado con iva', obligatoria=False)
    ws_be = wb[nombre_be] if nombre_be else ws
    f_be = _fila(ws_be, r'^mes de break-?even|^break-?even \(meses\)',
                 obligatoria=False)
    f_umbral = _fila(ws_be, r'^umbral de ventas', obligatoria=False)
    f_mc = _fila(ws_be, r'^margen de contribucion', obligatoria=False)
    P = "'" + nombre_caja + "'!"
    B = "'" + ws_be.title + "'!"
    fallos, r = [], {'fichero': fname, 'variante': variante,
                     'meses': meses, 'fila_acumulado_con_iva': f_acum_iva}

    xl = _compilar(carpeta, destino, fname)
    # serie que cruza a positivo en el mes 4
    entradas = list(range(f_ing_bloque + 1, f_tot_ing))
    salidas = list(range(f_gas_bloque + 1, f_tot_gas))
    for i, col in enumerate(meses):
        _set(xl, P + col + str(entradas[0]), 10000 * (i + 1))
        for fila in entradas[1:]:
            _set(xl, P + col + str(fila), 0)
        _set(xl, P + col + str(salidas[0]), 25000)
        for fila in salidas[1:]:
            _set(xl, P + col + str(fila), 0)
    r['acumulado'] = [_ev(xl, P + c + str(f_acum)) for c in meses]
    r['acumulado_con_iva_y_deuda'] = [_ev(xl, P + c + str(f_acum_iva))
                                      for c in meses] if f_acum_iva else None
    serie = r['acumulado']
    if all(_num(x) for x in serie):
        encadena = all(abs(serie[i] - (serie[i - 1] + (serie[i] - serie[i - 1])))
                       < 0.01 for i in range(1, len(serie)))
        r['encadena'] = encadena and serie[-1] > serie[0]
        if not r['encadena']:
            fallos.append(fname + ': el flujo acumulado no encadena mes a mes: '
                          + repr(serie))
    else:
        fallos.append(fname + ': el flujo acumulado no evalúa: ' + repr(serie))
    if f_be:
        r['mes_break_even'] = _ev(xl, B + 'B' + str(f_be))
        if not _num(r['mes_break_even']):
            fallos.append(fname + ': con una serie que cruza a positivo, el '
                          'mes de break-even devuelve '
                          + repr(r['mes_break_even']) + ' en vez de un número')
        # serie SIEMPRE negativa → «No alcanzado», nunca #N/A
        xl2 = _compilar(carpeta, destino, fname)
        for col in meses:
            for fila in entradas:
                _set(xl2, P + col + str(fila), 0)
            _set(xl2, P + col + str(salidas[0]), 25000)
        r['mes_break_even_serie_negativa'] = _ev(xl2, B + 'B' + str(f_be))
        if r['mes_break_even_serie_negativa'] != 'No alcanzado':
            fallos.append(fname + ': con una serie siempre negativa el mes de '
                          'break-even devuelve '
                          + repr(r['mes_break_even_serie_negativa'])
                          + ' en vez de "No alcanzado"')
    if f_umbral and f_mc:
        xl3 = _compilar(carpeta, destino, fname)
        _set(xl3, B + 'B' + str(f_mc), 0)
        r['umbral_con_margen_de_contribucion_cero'] = _ev(
            xl3, B + 'B' + str(f_umbral))
        if r['umbral_con_margen_de_contribucion_cero'] not in ('', None):
            fallos.append(fname + ': con margen de contribución 0 el umbral '
                          'devuelve '
                          + repr(r['umbral_con_margen_de_contribucion_cero'])
                          + ' en vez de "" (debería atraparlo IFERROR)')
    return dict(r, fallos=fallos)


def _demo_capex(carpeta, destino):
    import os
    fname = 'calculadora-capex.xlsx'
    ruta = os.path.join(carpeta, fname)
    if not os.path.isfile(ruta):
        return None
    import openpyxl
    wb = openpyxl.load_workbook(ruta)
    variante, ws, fila_cab = variante_capex(wb, fname)
    f_total, ultima = _fila_total(ws, fila_cab)
    xl = _compilar(carpeta, destino, fname)
    P = "'" + ws.title + "'!"
    fallos, r = [], {'fichero': fname, 'variante': variante,
                     'fila_total': f_total, 'ultima_fila_de_datos': ultima}
    from openpyxl.utils import get_column_letter as gcl
    r['totales'] = {}
    for c in range(2, ws.max_column + 1):
        cel = ws.cell(row=f_total, column=c)
        if cel.data_type != 'f':
            continue
        col = gcl(c)
        total = _ev(xl, P + col + str(f_total))
        suma = 0.0
        for fila in range(fila_cab + 1, ultima + 1):
            v = _ev(xl, P + col + str(fila))
            if _num(v):
                suma += v
        r['totales'][col + str(f_total)] = {'formula': cel.value,
                                            'valor': total,
                                            'suma_celda_a_celda': round(suma,
                                                                        2)}
        if _num(total) and abs(total - suma) > 0.01:
            fallos.append(fname + ':' + ws.title + '!' + col + str(f_total)
                          + ': el TOTAL vale ' + str(total) + ' y la suma de '
                          'sus filas ' + str(round(suma, 2)))
    return dict(r, fallos=fallos)
