#!/usr/bin/env python3
"""
grupo_a.py — Línea A de la familia «Planes de Negocio» v2.0 (§2 de la SPEC).

Convierte el plan financiero de los CINCO productos de línea A en un MODELO:
una sola hoja de entrada (`0. Supuestos`) y todo lo demás derivado por fórmula,
más dos hojas nuevas (`Tesorería 12 meses` y `Financiación`) y el checklist de
apertura con el contenido legal vigente.

    SPEC: scripts/productos-digitales/planes-v2-SPEC.md §2 (§2.1 a §2.12)

POR MOLDE, NUNCA POR POSICIÓN FIJA (§1.1 / §7-bis.9)
----------------------------------------------------
La línea A tiene DOS moldes y este módulo se escribió mirando los tres ficheros
a la vez, no sólo el del representante:

  * **A-α** — `plan-negocio-bar-restaurante`. Hojas numeradas
    (`'1. Inversion Inicial'`…`'5. Personal'`), ingresos = cubiertos × ticket ×
    días en filas de input, hoja `Personal` CON columna «Personas».
  * **A-β** — `tapas-bar`, `cafeteria`, `panaderia`, `food-truck`. Hojas sin
    numerar (`'Inversion Inicial'`, `'PyG 3 Anos'`, …), ingresos = **4 líneas
    tecleadas por familia de producto** y **ningún input de ticket ni de
    cubiertos en el P&L** (viven en `Punto Equilibrio` y en `Escenarios`, con
    dos calendarios distintos — `NUEVO-03`), hoja `Personal` **SIN** columna
    «Personas» y con las notas en la columna F.

Todo acceso a hoja va por `motor.hoja()` (insensible a tildes: §1.7 renombra
`'PyG 3 Anos'` → `'PyG 3 Años'` DESPUÉS de este grupo) y toda fila se localiza
por su RÓTULO normalizado, nunca por su número. Las dos únicas cosas que este
módulo da por sabidas son las que la SPEC fija: la rejilla de `0. Supuestos`
(§2.1) y que la columna A lleva el concepto.

DE DÓNDE SALE CADA NÚMERO
-------------------------
1. `0. Supuestos` — lo escribe este grupo con los valores de
   `contenido_<pid>/a.py`, que es donde vive TODO lo específico del producto
   (importes, rótulos, plantilla, umbrales) con la fuente de cada cifra.
2. El resto del libro se deriva de ahí por fórmula. Ningún número se teclea dos
   veces y ningún literal sobrevive dentro de una fórmula ni de un rótulo
   (§7-bis.11): los rótulos que hoy llevan el porcentaje escrito pasan a
   llevarlo en la NOTA, generada con `TEXT()` desde la celda del parámetro.
3. Las partidas que el fichero ya traía y que son datos del cliente (las líneas
   de inversión, los costes fijos que no son driver) se CONSERVAN como celdas
   de input verdes (§1.3): no se borra ningún número que el cliente pueda estar
   usando. Lo que cambia de valor se anota en el informe (`RECALIBRADO`).

DECISIONES QUE ESTE MÓDULO TOMA Y POR QUÉ
-----------------------------------------
a) **Reconstrucción de hoja, no inserción de filas.** `ws.insert_rows()` de
   openpyxl no mueve validaciones, formato condicional ni celdas combinadas, y
   no reescribe fórmulas: insertar dejaría el libro incoherente. Cada hoja se
   vacía en su zona de datos y se reescribe entera desde el modelo. Es lo que
   hace que la 2.ª pasada sea idéntica a la 1.ª (idempotencia = 0 diferencias,
   que `main.py` comprueba por huella).
b) **Los rótulos NO llevan fórmula; la nota SÍ.** §7-bis.11 exige que los
   números de los rótulos («Food cost (30% sobre ingresos)», «Colchon operativo
   (3 meses…)») dejen de estar escritos a mano. Se cumple quitándolos del
   rótulo y generando la frase con `TEXT()` en la columna de NOTAS. No se
   ponen fórmulas en la columna A porque `motor._rotulo_de_fila()` ignora las
   celdas que empiezan por «=»: el motor perdería el rótulo y con él la regla
   de formatos por tipo (§1.4) y la validación por rótulo (§1.5).
c) **Sin referencia circular.** El fondo de maniobra depende de los costes
   fijos, los costes fijos de los intereses y los intereses del préstamo: si el
   préstamo se derivara de la inversión, Excel daría referencia circular. Por
   eso **recursos propios y préstamo son INPUT** y la hoja `Financiación`
   compara orígenes contra usos con un semáforo (§2.8: «cuadrando con
   `'1. Inversion Inicial'!B46`»).
d) **Cuadro de amortización ANUAL.** La cuota va como anualidad algebraica
   (pycel no implementa `PMT`, §7-bis.16). Se usa periodicidad anual en el
   cuadro y en tesorería se reparte en doce partes iguales, con la nota puesta:
   mezclar un cuadro mensual con un P&L anual descuadra los intereses.
e) **Todo cálculo va envuelto en `IFERROR(...;"")`.** Con el libro en blanco no
   puede quedar ni un semáforo verde ni un «0,0 %» falso: «sin dato» se escribe
   `""` (convención de familia), y el formato condicional lleva la guarda
   `ISNUMBER` que pone el motor (§1.6).
f) **Umbrales al lado del ratio.** El formato condicional compara contra una
   celda de la MISMA hoja (columna «Umbral»), no contra `Instrucciones`: las
   referencias entre hojas dentro de una regla de formato condicional no las
   admiten todas las versiones de Excel, y así además el lector ve el umbral al
   lado del ratio que audita (TEC-12, §2.9).

CONTRATO CON `contenido_<pid>/a.py`
-----------------------------------
Todo es opcional: sin módulo de contenido el grupo sigue funcionando leyendo el
fichero (peor calibrado, pero coherente). Claves que lee:

    CONCEPTO           str — nombre del negocio para los rótulos
    SUPUESTOS          {clave: (coord, etiqueta, valor, fmt, nota, fuente)}
    LINEAS_INGRESO     [(rótulo, peso, 'comida'|'bebida', nota, fuente)]
    PLANTILLA          [(puesto, personas, bruto_mes_total, nota, fuente)]
    FIJOS              {rótulo_norm: (accion, nota)}  accion: 'suprimir'|número
    FIJOS_EXTRA        [(rótulo, importe, nota, fuente)]
    INVERSION          {rótulo_norm: (accion, nota)}
    INVERSION_EXTRA    [(bloque, rótulo, importe, nota, fuente)]
    AMORTIZABLE        {'obra': [regex], 'maquinaria': [regex], 'no': [regex]}
    UMBRALES           [(clave, rótulo, valor, comentario)]
    ESCENARIOS         {'pesimista': (cub, ticket, días), 'optimista': (...)}
    ESTACIONALIDAD     [12 pesos que suman 1]
    CHECKLIST          {'reemplazos', 'altas', 'suprimir', 'fases'}
    INSTRUCCIONES      {'uso': [...], 'referencias': [(rótulo, valor, nota)]}
    RECALIBRADO        [(concepto, valor_v1, valor_v2, motivo)]

IDS DEL R1 QUE CIERRA (mapa §8 de la SPEC)
------------------------------------------
TEC-01/04/05/06/07/10/11/12/16/17/18/19/20/21/22/23/25 · DOM-01/04/05/07/08/09/
10/11/12/13/14/15/17/19/23/24/25/26/30/32/33/34 · COM-03/04/06/08/11/12/13/14/
17/20/21/22/25 · NUEVO-01/02/03/06. Los de §1 (formatos, tildes, altos, DV,
metadata) los cierra `motor.py`; los de §4 y §5, `documentos.py` y T10.
"""
import copy
import math
import os
import re
import shutil

from openpyxl.styles import Alignment, Border, Font, PatternFill, Protection
from openpyxl.utils import column_index_from_string, get_column_letter
from openpyxl.worksheet.cell_range import CellRange

import motor

LETRA = 'a'
SPEC = 'planes-v2-SPEC.md §2'

#: Ficheros que este grupo construye ENTEROS (ninguno: el §1 transversal del
#: motor se aplica a los dos ficheros que toca).
PROPIOS = []

FINO = motor.FINO          # U+202F — SIEMPRE por escape (regla dura 5)
GUION = motor.GUION        # U+2011

# ==========================================================================
# Nombres de hoja por molde (§1.1). A-α numera; A-β no.
# ==========================================================================
HOJAS = {
    'inversion': ('1. Inversion Inicial', 'Inversion Inicial'),
    'pyg': ('2. P&L 3 Anos', 'PyG 3 Anos'),
    'equilibrio': ('3. Punto Equilibrio', 'Punto Equilibrio'),
    'escenarios': ('4. Escenarios', 'Escenarios'),
    'personal': ('5. Personal', 'Personal'),
}
#: Hojas nuevas de §2.7 y §2.8. El prefijo numérico se decide por el molde.
NUEVAS = (('tesoreria', 'Tesorería 12 meses', '6. '),
          ('financiacion', 'Financiación', '7. '))

MOLDES = ('A-alfa', 'A-beta')

# ==========================================================================
# Rejilla de `0. Supuestos` (§2.1). El motor reserva B20:B22 y B37:B40.
# ==========================================================================
#: (clave, coord, etiqueta, valor por defecto, formato, nota).
#: El valor por defecto sólo se usa si el módulo de contenido no trae el suyo y
#: no se puede leer del fichero: es el último recurso, nunca la fuente.
SUPUESTOS_BASE = (
    ('cubiertos_dia', 'B4', 'Cubiertos/día (media del año 1)', None,
     motor.FMT_ENT,
     'Comensales servidos al día de media, contando todos los servicios'),
    ('ticket_medio', 'B5', 'Ticket medio SIN IVA (€)', None, motor.FMT_EUR,
     'Gasto medio por comensal sin IVA. En la nota de al lado tienes el PVP '
     'equivalente con IVA'),
    ('dias_apertura', 'B6', 'Días de apertura al año', None, motor.FMT_ENT,
     'El MISMO dato lo usan el P&L, el punto de equilibrio y los escenarios'),
    ('crec_a2', 'B7', 'Crecimiento de volumen del año 2', 0.10,
     motor.FMT_PCT, 'Se aplica a los cubiertos y al coste de personal'),
    ('crec_a3', 'B8', 'Crecimiento de volumen del año 3', 0.06,
     motor.FMT_PCT, 'Se aplica sobre el año 2'),
    ('pct_comida', 'B11', 'Ventas de COMIDA sobre el total', None,
     motor.FMT_PCT, 'Se calcula sumando el peso de las líneas de comida'),
    ('pct_bebida', 'B12', 'Ventas de BEBIDA sobre el total', None,
     motor.FMT_PCT, 'El resto de las ventas'),
    ('coste_comida', 'B13', 'Coste de mercancía sobre las ventas de COMIDA',
     0.30, motor.FMT_PCT,
     'Food cost real: se aplica SOLO a la comida, nunca al total'),
    ('coste_bebida', 'B14', 'Coste de mercancía sobre las ventas de BEBIDA',
     0.22, motor.FMT_PCT, 'Se aplica SOLO a la bebida'),
    ('pct_consumibles', 'B15', 'Consumibles sobre ventas', 0.015,
     motor.FMT_PCT, 'Servilletas, limpieza, envases, papel de TPV'),
    ('pct_delivery', 'B16', 'Ventas por delivery sobre el total', 0.0,
     motor.FMT_PCT,
     'A CERO por defecto: si no repartes, no arrastras un coste inventado'),
    ('comision_delivery', 'B17', 'Comisión de la plataforma de delivery',
     0.28, motor.FMT_PCT,
     'Se aplica solo sobre las ventas del canal, no sobre el total'),
    ('comision_tpv', 'B18', 'Comisión de los medios de pago', 0.008,
     motor.FMT_PCT, 'Tarjeta y bizum sobre el total facturado'),
    ('alquiler_mes', 'B24', 'Alquiler mensual del local (€)', None,
     motor.FMT_EUR0, 'De aquí salen la fianza, el primer mes y el ratio '
     'alquiler/ventas'),
    ('fianza_meses', 'B25', 'Fianza del alquiler (meses)', 3, motor.FMT_ENT,
     'Meses de renta que pide el arrendador como fianza'),
    ('suministros_mes', 'B26', 'Suministros mensuales de luz, agua y gas (€)', None, motor.FMT_EUR0,
     'Luz, agua y gas'),
    ('seguros_ano', 'B27', 'Seguros (€/año)', None, motor.FMT_EUR0,
     'Responsabilidad civil + multirriesgo del local'),
    ('pct_varios', 'B28', 'Varios e imprevistos sobre ventas', 0.02,
     motor.FMT_PCT, 'Colchón de gasto corriente no presupuestado'),
    ('recursos_propios', 'B30', 'Recursos propios aportados (€)', None,
     motor.FMT_EUR0, 'Capital y aportaciones de los socios'),
    ('prestamo', 'B31', 'Préstamo bancario solicitado (€)', None,
     motor.FMT_EUR0, 'Importe del principal. La hoja de Financiación monta el '
     'cuadro de amortización'),
    ('tipo_prestamo', 'B32', 'Tipo de interés nominal anual', 0.06,
     motor.FMT_PCT, 'Pide oferta a dos entidades antes de fijarlo'),
    ('plazo_prestamo', 'B33', 'Plazo del préstamo (años)', 7, motor.FMT_ENT,
     'Años totales, carencia incluida'),
    ('carencia_prestamo', 'B34', 'Carencia de principal (años)', 1,
     motor.FMT_ENT,
     'Durante la carencia sólo se pagan intereses. Si iguala o supera al '
     'plazo, la hoja la anula'),
    ('meses_fondo', 'B35', 'Fondo de maniobra (meses de costes fijos)', 3,
     motor.FMT_ENT,
     'Las Instrucciones de este libro exigen 3 meses como mínimo'),
    ('iva_soportado', 'B41', 'IVA soportado en compras e inversión', 0.21,
     motor.FMT_PCT, 'Recuperable vía modelo 303, pero hay que adelantarlo'),
    ('bin_inicial', 'B42', 'Bases negativas de ejercicios anteriores (€)', 0,
     motor.FMT_EUR0,
     'Pérdidas pendientes de compensar al empezar (art. 26 LIS)'),
    ('vida_obra', 'B44', 'Vida útil de obra e instalaciones (años)', 10,
     motor.FMT_ENT,
     'Coeficientes de la tabla del art. 12.1 LIS; confírmalo con tu asesor'),
    ('vida_maquinaria', 'B45',
     'Vida útil de maquinaria y mobiliario (años)', 8, motor.FMT_ENT,
     'Coeficientes de la tabla del art. 12.1 LIS; confírmalo con tu asesor'),
    ('ipc', 'B48', 'Subida anual de los costes fijos', 0.0, motor.FMT_PCT,
     'A CERO: las tres columnas están en euros del año 1 (términos reales). '
     'Súbela si quieres proyectar en euros corrientes'),
)

#: Bloque extra que este grupo cuelga debajo de la rejilla del motor.
BLOQUE_EXTRA = ('A47', 'CRECIMIENTO Y ACTUALIZACIÓN DE COSTES')

# ==========================================================================
# Clasificación de partidas (por RÓTULO: sirve para A-α con bloques y para
# A-β, que es una lista plana sin bloques)
# ==========================================================================
RX_CANON_INV = re.compile(
    r'fianza|primer mes.*alquiler|fondo de maniobra|colch[oó]n operativo|'
    r'iva soportado|base amortizable|amortizaci[oó]n anual|'
    r'necesidad total de caja', re.I)
#: ⚠️ «comisiones» a secas se tragaba «Comisiones de reservas online», que es
#: una partida NUEVA y preservable: al excluirla del barrido, la 2.ª pasada la
#: volvía a añadir al final y las dos últimas filas de costes fijos cambiaban
#: de orden. El patrón nombra sólo las dos comisiones que genera este grupo.
RX_CANON_PYG = re.compile(
    r'^(alquiler|n[oó]minas|salarios|personal|suministros|seguros?|'
    r'amortizaci[oó]n|cuota pr[eé]stamo|gastos financieros|'
    r'varios e imprevistos|coste de mercanc[ií]a|food cost|bebidas? cost|'
    r'consumibles|comisiones de (delivery|los medios|medios)|'
    r'ingresos|cubiertos|clientes|ticket|d[ií]as|'
    r'ventas |otros \(|coste (materias|cafe|ingredientes|bebidas|cocteles)|'
    r'packaging)', re.I)
RX_INGRESO = re.compile(r'^(ventas|ingresos|otros\b)', re.I)

#: Qué partidas de la inversión son inmovilizado y con qué vida útil (§2.3.6,
#: TEC-20 y `NUEVO-02`: la base NO puede incluir circulante, stock ni
#: imprevistos).
AMORT_DEFECTO = {
    'obra': (r'obra civil|adecuaci|reforma|instalaci|fontaner|el[eé]ctric|'
             r'climatizaci|extracci|proyecto t[eé]cnico|decoraci|interiorismo|'
             r'rotulaci|campana extractora|licencia de obras',),
    'maquinaria': (r'equipamiento|maquina|m[aá]quina|horno|nevera|c[aá]mara|'
                   r'vitrina|mobiliario|barra|mostrador|tpv|vajilla|'
                   r'cristaler|cuberter|menaje|plancha|molinillo|lavavajillas|'
                   r'grifo|freidora|cafetera|batidora|tostadora|mesa|silla|'
                   r'taburete|estanter|fregadero|vinoteca|terraza|'
                   r'sandwichera|expositor|comandero|software|utensilios',),
    'no': (r'fianza|primer mes|inmobiliaria|stock|fondo de maniobra|'
           r'colch[oó]n|imprevisto|marketing|lanzamiento|campa[ñn]a '
           r'lanzamiento|web|'
           r'constituci|notar[ií]a|registro|gestor[ií]a|seguro|licencia de '
           r'actividad|permiso|tasa|iva|marca|dise[ñn]o',),
}
# ⚠️ «campana extractora» convive con «Campaña lanzamiento RRSS» en el mismo
# libro y la primera va SIN tilde: por eso la lista de «no amortizable» exige
# la palabra «lanzamiento» detrás y la extractora se declara obra a mano. Es
# la trampa que `CLAUDE.md` documenta para el gate de ortografía.

# ==========================================================================
# Utilidades de escritura
# ==========================================================================


def ref(ws, coord):
    """Referencia con NOMBRE DE HOJA ACTUAL.

    Imprescindible: §1.7 renombra `'PyG 3 Anos'` → `'PyG 3 Años'` en
    `motor.cerrar()`, DESPUÉS de este grupo, y reescribe las referencias que
    encuentre. En la 2.ª pasada la hoja ya se llama con tilde y escribir el
    nombre viejo dejaría la fórmula apuntando a una hoja inexistente, que es
    justo lo que caza `gate_referencias`.
    """
    return "'" + ws.title + "'!" + coord


def _sin_comillas(formula):
    return re.sub(r'"[^"]*"', '', formula)


def fx(ws, coord, formula, fmt=None, align=None):
    """`motor.f()` con la guarda de §1.5 puesta de oficio.

    TODA fórmula del grupo va envuelta en `IFERROR(...,"")`, no sólo las
    divisiones. Motivo medido: con el libro en blanco el ticket es un número y
    el coste variable unitario es `""`, así que una simple RESTA devuelve
    `#¡VALOR!` y el error se propaga a la cifra estrella. Envolviéndolo todo,
    «sin dato» se escribe `""` (convención de familia) y el semáforo, que
    lleva la guarda `ISNUMBER` del §1.6, no pinta verde una celda vacía.

    Se hace aquí y no confiando en `motor.guardas()` porque el motor pasa por
    el libro ANTES que el grupo: lo que escribe el grupo ya no lo ve.
    """
    if not motor.RX_YA_GUARDADA.match(formula):
        formula = motor.iferror(formula)
    return motor.f(ws, coord, formula, fmt, align)


def _limpiar_area(ws, r0, r1, ncols):
    """Vacía valores, estilos, combinadas, DV y CF de la zona de datos.

    Reconstruir es más seguro que insertar filas: `insert_rows` de openpyxl no
    mueve validaciones, formato condicional ni combinadas, y no reescribe
    fórmulas.
    """
    if r1 < r0:
        return
    for m in list(ws.merged_cells.ranges):
        cr = CellRange(str(m))
        if cr.max_row >= r0 and cr.min_row <= r1:
            ws.unmerge_cells(str(m))
    vacio = PatternFill()
    borde = Border()
    for r in range(r0, r1 + 1):
        for c in range(1, ncols + 1):
            cel = ws.cell(row=r, column=c)
            cel.value = None
            cel.fill = vacio
            cel.border = borde
            cel.font = Font()
            cel.alignment = Alignment()
            cel.number_format = 'General'
            cel.protection = Protection(locked=True)
            cel.hyperlink = None
        ws.row_dimensions[r].height = None
    _purgar_dv_area(ws, r0, r1)
    _purgar_cf_area(ws, r0, r1)
    ws._pl_cabeceras = None          # la cabecera cambia: invalida la caché
    ws._pl_editables = set()
    ws._pl_negativos = set()


def _rangos_fuera(sqref, r0, r1):
    fuera = []
    for r in str(sqref).split():
        try:
            cr = CellRange(r)
        except Exception:                                    # noqa: BLE001
            continue
        if cr.max_row >= r0 and cr.min_row <= r1:
            continue
        fuera.append(str(cr))
    return fuera


def _purgar_dv_area(ws, r0, r1):
    quedan = []
    for dv in ws.data_validations.dataValidation:
        restos = _rangos_fuera(dv.sqref, r0, r1)
        if not restos:
            continue
        dv.sqref = ' '.join(restos)
        quedan.append(dv)
    ws.data_validations.dataValidation = quedan


def _purgar_cf_area(ws, r0, r1):
    from openpyxl.formatting.formatting import ConditionalFormattingList
    supervivientes = []
    for cf in ws.conditional_formatting:
        restos = _rangos_fuera(cf.sqref, r0, r1)
        if not restos:
            continue
        supervivientes.append((' '.join(restos), list(cf.rules)))
    nueva = ConditionalFormattingList()
    for sqref, reglas in supervivientes:
        for r in reglas:
            nueva.add(sqref, r)
    ws.conditional_formatting = nueva


def _cabecera(ws):
    """Fila de cabecera de la tabla (la que tiene 3+ rótulos)."""
    fila, _ = motor._fila_cabecera(ws)
    return fila or 4


def _es_mayusculas(texto):
    letras = [c for c in motor.norm(texto) if c.isalpha()]
    if not letras:
        return False
    return str(texto).upper() == str(texto)


def _ancho_combinado(ws, fila):
    for m in ws.merged_cells.ranges:
        cr = CellRange(str(m))
        if cr.min_row <= fila <= cr.max_row:
            return cr.max_col
    return 1


def _pie(ws, r0):
    """Filas de pie («ChefBusiness.co — …», «NOTA: …») para reponerlas."""
    fuera = []
    for r in range(r0, ws.max_row + 1):
        v = ws.cell(row=r, column=1).value
        if isinstance(v, str) and re.match(r'^(NOTA|ChefBusiness|\*)', v):
            fuera.append(v)
    return fuera


class Rejilla(object):
    """Constructor de filas en dos fases.

    Primero se declaran todas las filas (con las fórmulas como funciones que
    reciben el resolvedor de coordenadas) y después se escriben: así una fila
    puede referenciar a otra que todavía no existía cuando se declaró, sin que
    el módulo tenga que saber números de fila.
    """

    def __init__(self, ws, fila0):
        self.ws = ws
        self.fila0 = fila0
        self.filas = []
        self._pos = {}

    def add(self, clave=None, **kw):
        self.filas.append(dict(kw, clave=clave))
        if clave:
            self._pos[clave] = self.fila0 + len(self.filas) - 1
        return self.fila0 + len(self.filas) - 1

    def fila(self, clave):
        return self._pos[clave]

    def c(self, clave, col='B', absoluta=False):
        fila = self._pos[clave]
        if absoluta:
            return '$' + col + '$' + str(fila)
        return col + str(fila)

    def r(self, clave, col='B'):
        """Referencia con hoja: para que la use otra hoja del libro."""
        return ref(self.ws, self.c(clave, col, absoluta=True))

    @property
    def ultima(self):
        return self.fila0 + len(self.filas) - 1


def escribir(rej, cols_texto=('A',)):
    """Vuelca las filas declaradas. `formulas`/`valores` por columna."""
    ws = rej.ws
    for i, spec in enumerate(rej.filas):
        fila = rej.fila0 + i
        rot = spec.get('rot')
        if rot is not None:
            motor.val(ws, 'A' + str(fila), rot,
                      bold=spec.get('bold', False),
                      wrap=spec.get('wrap'))
        verdes = spec.get('verdes')
        for col, valor in sorted((spec.get('valores') or {}).items()):
            editable = (col in verdes) if verdes is not None \
                else spec.get('verde', False)
            motor.val(ws, col + str(fila), valor, spec.get('fmt_' + col)
                      or spec.get('fmt'), verde_=editable,
                      bold=spec.get('bold', False))
        for col, fabrica in sorted((spec.get('formulas') or {}).items()):
            formula = fabrica(rej) if callable(fabrica) else fabrica
            if formula is None:
                continue
            fx(ws, col + str(fila), formula,
               spec.get('fmt_' + col) or spec.get('fmt'))
            if spec.get('bold'):
                cel = ws[col + str(fila)]
                cel.font = Font(bold=True, size=cel.font.size)
        if spec.get('alto'):
            ws.row_dimensions[fila].height = spec['alto']


def texto_pct(refcelda, prefijo, sufijo=''):
    """Frase con el porcentaje GENERADO desde la celda (§7-bis.11).

    Se usa `"0%"` a propósito: `TEXT()` con decimales imprime el separador
    anglosajón en el valor cacheado y este libro ya arrastraba el defecto de
    mezclar «57.9» con «10,73» en la misma frase (TEC-21).
    """
    return ('="' + prefijo + '"&TEXT(' + refcelda + ',"0%")&"' + sufijo + '"')


def texto_num(refcelda, prefijo, sufijo='', fmt='0'):
    return ('="' + prefijo + '"&TEXT(' + refcelda + ',"' + fmt + '")&"'
            + sufijo + '"')


# ==========================================================================
# Lectura del fichero de partida
# ==========================================================================


#: Paréntesis que sólo contienen un parámetro numérico: se van del rótulo
#: porque mienten en cuanto se toca la celda (§7-bis.11). El dato vuelve en la
#: columna de notas, generado con `TEXT()`.
RX_PARENTESIS_NUM = re.compile(
    r'\s*\((?:incl\.?\s*)?[^()]*?\d+(?:[.,]\d+)?\s*'
    r'(?:%|a[ñn]os?|meses|mes)\b[^()]*\)', re.I)


def _limpiar_rotulo(rotulo):
    """«Imprevistos (8%)» → «Imprevistos». Devuelve (rótulo, cambió)."""
    nuevo = RX_PARENTESIS_NUM.sub('', rotulo).strip(' -—:')
    if nuevo and nuevo != rotulo:
        return nuevo, True
    return rotulo, False


def _seccion(ws, cab, rx_inicio, rx_fin):
    """Rango de filas de una SECCIÓN, acotado por sus rótulos.

    Buscar dentro de la hoja entera no falla: acierta en el sitio equivocado.
    Sin acotar, el barrido de «costes fijos» del P&L de A-β se llevaba por
    delante el EBITDA, el impuesto y el resultado neto, que están debajo y
    también tienen número. (Misma lección que los regex de sección del blog.)
    """
    ini = fin = None
    for r in range(cab, ws.max_row + 1):
        rot = motor._rotulo_de_fila(ws, r, max_col=1)
        if not rot:
            continue
        if ini is None:
            if re.search(rx_inicio, rot, re.I):
                ini = r + 1
            continue
        if re.search(rx_fin, rot, re.I):
            fin = r - 1
            break
    if ini is None:
        return None, None
    return ini, (fin if fin is not None else ws.max_row)


def _partidas(ws, cab, col_importe=2, canon=None, desde=None, hasta=None):
    """Partidas de una tabla: (fila, rótulo, importe, nota, bloque).

    Distingue encabezado de bloque (texto en mayúsculas sin importe **o con
    importe de fórmula**, que es como quedan tras el subtotal de §2.2) de
    partida (rótulo + número) y de pie. Funciona igual sobre el fichero
    original y sobre el reconstruido: de eso depende la idempotencia.
    """
    bloque = None
    fuera = []
    for r in range(desde or (cab + 1), (hasta or ws.max_row) + 1):
        rot = motor._rotulo_de_fila(ws, r, max_col=1)
        if not rot:
            continue
        v = ws.cell(row=r, column=col_importe).value
        if _es_mayusculas(rot) and not motor._es_numero(v):
            if not motor.RX_TOTAL.match(rot):
                bloque = rot
            continue
        if motor.RX_TOTAL.match(rot) or re.match(r'^(NOTA|ChefBusiness|\*)',
                                                 rot):
            continue
        if canon is not None and canon.search(rot):
            continue
        if not motor._es_numero(v):
            continue
        nota = None
        for c in range(col_importe + 1, min(ws.max_column, 6) + 1):
            vv = ws.cell(row=r, column=c).value
            if isinstance(vv, str) and vv.strip() \
                    and not vv.startswith('=') and '%' not in (
                        ws.cell(row=r, column=c).number_format or ''):
                nota = vv.strip()
                break
        fuera.append((r, rot, float(v), nota, bloque))
    return fuera


def _clasificar_amortizable(rotulo, tablas):
    for grupo in ('no', 'obra', 'maquinaria'):
        for rx in tablas.get(grupo, ()):
            if re.search(rx, rotulo, re.I):
                return grupo
    return 'no'


def _num(valor, defecto=None):
    if motor._es_numero(valor):
        return float(valor)
    return defecto


# ==========================================================================
# El modelo del producto
# ==========================================================================
class Plan(object):

    def __init__(self, wb, det, pid, params, contenido, cambios):
        self.wb = wb
        self.det = det
        self.pid = pid
        self.p = params
        self.c = contenido
        self.cambios = cambios
        self.molde = det['molde']
        self.numerado = self.molde == 'A-alfa'
        self.concepto = self.dato('CONCEPTO', pid)
        self.rej = {}
        #: Rejillas declaradas y pendientes de volcar. El volcado va al FINAL
        #: de todo (§ ver `post`): las hojas se citan entre sí en las dos
        #: direcciones —el P&L lee los intereses de Financiación y el fondo de
        #: maniobra de Inversión sale de los costes fijos del P&L—, así que
        #: ninguna fórmula puede resolverse hasta que estén todas colocadas.
        self.pendientes = []
        if det['tipo'] != 'plan_financiero':
            # el checklist comparte módulo de contenido pero no tiene ni
            # supuestos ni hojas de modelo: se construye sin ellas
            return
        for clave, nombres in HOJAS.items():
            ws = None
            for nombre in nombres:
                ws = motor.hoja(wb, nombre)
                if ws is not None:
                    break
            setattr(self, 'ws_' + clave, ws)
        self.ws_sup = motor.hoja(wb, motor.HOJA_SUPUESTOS, obligatoria=True)
        self.ws_ins = motor.hoja(wb, 'Instrucciones', obligatoria=True)
        for clave, nombre, prefijo in NUEVAS:
            titulo = (prefijo if self.numerado else '') + nombre
            ws = motor.hoja(wb, titulo) or motor.hoja(wb, nombre)
            if ws is None:
                ws = wb.create_sheet(titulo)
            setattr(self, 'ws_' + clave, ws)

    # -- acceso al módulo de contenido -----------------------------------
    def dato(self, clave, defecto=None):
        if self.c is None:
            return defecto
        valor = getattr(self.c, clave, None)
        if valor is None and isinstance(getattr(self.c, 'CONTENIDO', None),
                                        dict):
            valor = self.c.CONTENIDO.get(clave)
        return defecto if valor is None else valor

    def anota(self, texto):
        self.cambios.append(texto)

    # -- §2.1 -------------------------------------------------------------
    def supuestos_altas(self):
        """`0. Supuestos`: da de alta los parámetros y sus refs (§2.1).

        Va ANTES que ninguna otra hoja: todas cablean contra `p.ref(clave)`.
        """
        ws = self.ws_sup
        motor.val(ws, 'A1', 'SUPUESTOS — aquí se teclean las TASAS y los '
                  'DRIVERS del modelo', bold=True)
        motor.val(ws, 'A2', 'Cambia las celdas VERDES: el resto del libro se '
                  'recalcula solo. Las partidas de gasto se teclean en su '
                  'hoja (también en verde) y no se repiten aquí.', wrap=True)
        motor.val(ws, BLOQUE_EXTRA[0], BLOQUE_EXTRA[1], bold=True)
        propios = self.dato('SUPUESTOS', {}) or {}
        leidos = self._leer_drivers()
        for clave, coord, etiqueta, defecto, fmt, nota in SUPUESTOS_BASE:
            fuente = 'valor por defecto del grupo A'
            valor = defecto
            if clave in leidos and leidos[clave] is not None:
                valor, fuente = leidos[clave], 'leído del fichero original'
            if clave in propios:
                spec = propios[clave]
                etiqueta = spec[1] or etiqueta
                valor = spec[2] if spec[2] is not None else valor
                fmt = spec[3] or fmt
                nota = spec[4] or nota
                fuente = spec[5] or 'contenido del producto'
                coord = spec[0] or coord
            if valor is None:
                valor = 0
            self.p.alta(clave, etiqueta, valor, fmt, nota, coord=coord)
            self.cambios.append('Supuestos!' + coord + ' ' + clave + ' = '
                                + str(valor) + ' (' + fuente + ')')
        motor.anchos(ws, {'A': 48, 'B': 16, 'C': 74})

    def supuestos_calculadas(self):
        """Las DOS celdas de `0. Supuestos` que no se teclean (§2.1).

        `pct_comida` sale de sumar el peso de las líneas de comida del P&L y
        `pct_bebida` es el resto: así el mix nunca puede sumar distinto de
        100 % y la mezcla vive en un solo sitio. Se escriben al final porque
        necesitan las coordenadas del P&L, que se declara después.
        """
        ws = self.ws_sup
        rej = self.rej['pyg']
        comida = [i for i, l in enumerate(self.lineas_ingreso())
                  if l[2] == 'comida']
        suma = ('+'.join(rej.r('lin_%d' % i, 'E') for i in comida)
                if comida else '0')
        fx(ws, 'B11', '=' + suma, motor.FMT_PCT)
        motor.val(ws, 'C11', 'Suma del peso de las líneas de COMIDA del P&L: '
                  'el mix vive en un solo sitio')
        fx(ws, 'B12', '=1-B11', motor.FMT_PCT)
        motor.val(ws, 'C12', 'Se calcula como el resto: comida + bebida = '
                  '100 %')
        # nota generada: el PVP con IVA equivalente al ticket sin IVA (TEC-11)
        red, gen = self._loc('iva_reducido'), self._loc('iva_general')
        tic = self._loc('ticket_medio')
        motor.val(ws, 'A9', 'PVP equivalente con IVA (calculado)')
        fx(ws, 'B9', '=' + tic + '*(B11*(1+' + red + ')+B12*(1+' + gen + '))',
           motor.FMT_EUR)
        fx(ws, 'C9', '="Es el ticket sin IVA con el IVA de cada familia: '
           '"&TEXT(' + red + ',"0%")&" en comida y "&TEXT(' + gen + ',"0%")&'
           '" en bebida. Compáralo con el rango del sector, que va con IVA."')
        for coord in ('B11', 'B12'):
            ws[coord].fill = PatternFill()
            ws[coord].protection = Protection(locked=True)
        motor.anchos(ws, {'A': 48, 'B': 16, 'C': 74})
        motor.print_setup(ws)

    def _loc(self, clave):
        """Coordenada de un parámetro DENTRO de `0. Supuestos` (sin hoja)."""
        return self.p.ref(clave).split('!')[-1]

    def _leer_drivers(self):
        """Drivers que el fichero ya trae, para no inventarlos (§1.3).

        En A-α están en el P&L; en A-β viven repartidos entre `Escenarios`
        (clientes/día, ticket, días) y `Punto Equilibrio` — con DOS calendarios
        distintos, que es `NUEVO-03`. Se toma el de `Escenarios`, que es el que
        declara días/año.
        """
        fuera = {}

        def por_rotulo(ws, patron, col='B'):
            if ws is None:
                return None
            for r in range(1, ws.max_row + 1):
                rot = motor._rotulo_de_fila(ws, r, max_col=1)
                if rot and re.search(patron, rot, re.I):
                    return _num(ws[col + str(r)].value)
            return None

        fuera['cubiertos_dia'] = por_rotulo(
            self.ws_pyg, r'^cubiertos') or por_rotulo(
                self.ws_escenarios, r'^(clientes|cubiertos)', 'C')
        fuera['ticket_medio'] = por_rotulo(
            self.ws_pyg, r'^ticket') or por_rotulo(
                self.ws_escenarios, r'^ticket', 'C')
        fuera['dias_apertura'] = por_rotulo(
            self.ws_pyg, r'^d[ií]as') or por_rotulo(
                self.ws_escenarios, r'd[ií]as', 'C')
        fuera['alquiler_mes'] = None
        alq = por_rotulo(self.ws_pyg, r'^alquiler')
        if alq:
            fuera['alquiler_mes'] = round(alq / 12.0, 2)
        sum_ = por_rotulo(self.ws_pyg, r'^suministros')
        if sum_:
            fuera['suministros_mes'] = round(sum_ / 12.0, 2)
        seg = por_rotulo(self.ws_pyg, r'^seguros?')
        if seg:
            fuera['seguros_ano'] = seg
        return fuera

    # -- líneas de ingreso -------------------------------------------------
    def lineas_ingreso(self):
        """Las líneas de venta y su peso. Une A-α (1 línea) con A-β (4)."""
        if getattr(self, '_lineas', None) is not None:
            return self._lineas
        propias = self.dato('LINEAS_INGRESO')
        if propias:
            self._lineas = [tuple(l) for l in propias]
            return self._lineas
        ws = self.ws_pyg
        cab = _cabecera(ws)
        # ACOTAR la sección antes de buscar dentro: fuera del bloque de
        # ingresos hay más filas que empiezan por «Ventas» o «Otros».
        r0, r1 = _seccion(ws, cab, r'^ingresos$|^ingresos\b',
                          r'^(total ingresos|ingresos brutos|ingresos '
                          r'totales|costes variables)')
        total = None
        lineas = []
        for r in range(r0 or cab + 1, (r1 or ws.max_row) + 1):
            rot = motor._rotulo_de_fila(ws, r, max_col=1)
            if not rot:
                continue
            if motor.RX_TOTAL.match(rot) or _es_mayusculas(rot):
                v = _num(ws.cell(row=r, column=2).value)
                if v and re.search(r'ingreso', rot, re.I):
                    total = v
                continue
            if not RX_INGRESO.match(rot):
                continue
            peso = _num(ws.cell(row=r, column=5).value)
            importe = _num(ws.cell(row=r, column=2).value)
            lineas.append([rot, peso, importe])
        if not lineas:
            self._lineas = [('Ingresos de comida', 0.65, 'comida', None,
                             'reparto por defecto del grupo A'),
                            ('Ingresos de bebida', 0.35, 'bebida', None,
                             'el resto')]
            return self._lineas
        suma = sum(l[2] for l in lineas if l[2]) or 1.0
        fuera = []
        for rot, peso, importe in lineas:
            if peso is None:
                peso = round((importe or 0) / (total or suma), 4)
            grupo = 'bebida' if re.search(
                r'bebida|c[oó]ctel|caf[eé]|vino|cerveza|refresco|zumo|'
                r'destilado|barra', rot, re.I) else 'comida'
            fuera.append((rot, peso, grupo, None, 'leído del fichero'))
        self._lineas = fuera
        return self._lineas

    # -- §2.6 -------------------------------------------------------------
    def personal(self):
        """`Personal`: SS en celda, fila cuadrada y TOTAL cerrado (§2.6)."""
        ws = self.ws_personal
        cab = _cabecera(ws)
        plantilla = self.dato('PLANTILLA') or self._leer_plantilla(ws, cab)
        # el pie del fichero v1.1 lleva el tipo de Seguridad Social escrito a
        # mano («33.4%»): repetiría un parámetro que ahora vive en celda y
        # quedaría desmintiendo a la propia columna (§7-bis.11)
        pie = [t for t in _pie(ws, cab)
               if not re.search(r'\d+[.,]?\d*\s*%', t)]
        for t in _pie(ws, cab):
            if re.search(r'\d+[.,]?\d*\s*%', t):
                self.anota('Personal: fuera la nota con el porcentaje escrito '
                           'a mano «' + t[:60] + '» (§7-bis.11)')
        _limpiar_area(ws, cab, ws.max_row, 8)
        # ⚠️ Las cabeceras llevan «(€)» a propósito: `motor.formatos_por_tipo`
        # decide por la CABECERA de la columna, y «Bruto mes» contiene la
        # palabra «mes», que el motor lee como recuento y le quitaría el
        # formato de euro a toda la columna.
        cabeceras = ('Puesto', 'Personas', 'Bruto mes (€, total del puesto)',
                     'Seg. Social a cargo de la empresa (€)',
                     'Coste mes (€, total del puesto)', 'Coste año (€)',
                     'Notas')
        for i, texto in enumerate(cabeceras):
            motor.val(ws, get_column_letter(i + 1) + str(cab), texto,
                      bold=True, wrap=True)
        rej = Rejilla(ws, cab + 1)
        self.rej['personal'] = rej
        ss = self.p.ref('ss_empresa')
        pagas = self.p.ref('pagas')
        for i, fila in enumerate(plantilla):
            puesto, personas, bruto, nota, fuente = (list(fila) + [None] * 5)[:5]
            clave = 'p_%d' % i
            rej.add(clave, rot=puesto,
                    valores={'B': personas, 'C': bruto, 'G': nota or ''},
                    fmt_B=motor.FMT_ENT, fmt_C=motor.FMT_EUR,
                    verde=True,
                    formulas={
                        'D': (lambda R, k=clave: '=' + R.c(k, 'C') + '*' + ss),
                        'E': (lambda R, k=clave: '=' + R.c(k, 'C') + '+'
                              + R.c(k, 'D')),
                        'F': (lambda R, k=clave: '=' + R.c(k, 'E') + '*'
                              + pagas)},
                    fmt=motor.FMT_EUR)
        primero, ultimo = 'p_0', 'p_%d' % (len(plantilla) - 1)
        rej.add('total', rot='TOTAL PLANTILLA', bold=True,
                formulas=dict(
                    (col, (lambda R, c=col: '=SUM(' + R.c(primero, c) + ':'
                           + R.c(ultimo, c) + ')'))
                    for col in ('B', 'C', 'D', 'E', 'F')),
                fmt=motor.FMT_EUR, fmt_B=motor.FMT_ENT)
        self.pendientes.append(rej)
        # el bruto/persona NUNCA por debajo del SMI (§2.6)
        rango = rej.c(primero, 'C') + ':' + rej.c(ultimo, 'C')
        smi = self.p.ref('smi_anual')
        base = ('IFERROR(' + rej.c(primero, 'C') + '/' + rej.c(primero, 'B')
                + ',0)*' + pagas)
        motor.semaforo_num(ws, rango, rojo_si=base + '<' + smi + '*IFERROR('
                           + rej.c(primero, 'B') + '/' + rej.c(primero, 'B')
                           + ',1)')
        fila_nota = rej.ultima + 2
        motor.val(ws, 'A' + str(fila_nota),
                  'Las columnas «Bruto mes», «Seg. Social», «Coste mes» y '
                  '«Coste año» son TOTALES de la fila: en un puesto con dos '
                  'personas incluyen a las dos. El tipo de Seguridad Social y '
                  'el número de pagas están en la hoja «0. Supuestos».',
                  wrap=True)
        motor.val(ws, 'A' + str(fila_nota + 1),
                  'El SMI de referencia está en la hoja «0. Supuestos» y es '
                  'el suelo por jornada completa; las jornadas parciales lo '
                  'llevan en proporción. El convenio aplicable es el '
                  'PROVINCIAL de hostelería: no existe una tabla salarial '
                  'estatal única.', wrap=True)
        for i, texto in enumerate(pie):
            motor.val(ws, 'A' + str(fila_nota + 2 + i), texto)
        motor.anchos(ws, {'A': 34, 'B': 10, 'C': 16, 'D': 18, 'E': 16,
                          'F': 16, 'G': 40})
        motor.print_setup(ws, header_row=cab)
        return rej

    def _leer_plantilla(self, ws, cab):
        """Plantilla del fichero, homogeneizada a totales de fila (TEC-16)."""
        cabeceras = dict((motor.norm(c.value), c.column) for c in ws[cab]
                         if isinstance(c.value, str))
        col_personas = cabeceras.get('personas')
        col_bruto = None
        for clave in ('bruto/mes', 'salario bruto mes', 'bruto mes',
                      'bruto mes (total del puesto)'):
            if clave in cabeceras:
                col_bruto = cabeceras[clave]
                break
        col_bruto = col_bruto or (3 if col_personas else 2)
        col_nota = cabeceras.get('notas')
        fuera = []
        for r in range(cab + 1, ws.max_row + 1):
            rot = motor._rotulo_de_fila(ws, r, max_col=1)
            if not rot or motor.RX_TOTAL.match(rot) \
                    or re.match(r'^(\*|NOTA|ChefBusiness)', rot):
                continue
            bruto = _num(ws.cell(row=r, column=col_bruto).value)
            if bruto is None:
                continue
            personas = _num(ws.cell(row=r, column=col_personas).value, 1) \
                if col_personas else 1
            nota = ws.cell(row=r, column=col_nota).value if col_nota else None
            fuera.append((rot, int(personas), bruto * personas,
                          nota if isinstance(nota, str) else None,
                          'leído del fichero (bruto × personas)'))
        return fuera

    # -- §2.2 -------------------------------------------------------------
    def inversion(self):
        """`Inversión Inicial`: subtotales, fondo calculado e IVA (§2.2)."""
        ws = self.ws_inversion
        cab = _cabecera(ws)
        canon = self.dato('INVERSION_CANON') or RX_CANON_INV
        partidas = _partidas(ws, cab, canon=canon)
        reglas = self.dato('INVERSION', {}) or {}
        extras = self.dato('INVERSION_EXTRA', []) or []
        tablas = self.dato('AMORTIZABLE') or AMORT_DEFECTO
        pie = _pie(ws, cab)
        _limpiar_area(ws, cab, ws.max_row, 5)
        for i, texto in enumerate(('Concepto', 'Importe', '% s/inversión',
                                   'Notas')):
            motor.val(ws, get_column_letter(i + 1) + str(cab), texto,
                      bold=True)
        # agrupar por bloque conservando el orden
        bloques, orden = {}, []
        for _r, rot, importe, nota, bloque in partidas:
            # el rótulo se limpia ANTES de consultar las reglas: en la 2.ª
            # pasada ya viene limpio y la clave tiene que ser la misma o el
            # fichero dejaría de ser idempotente
            rot, cambiado = _limpiar_rotulo(rot)
            if cambiado:
                self.anota('Inversión: rótulo con parámetro escrito a mano → '
                           '«' + rot + '» (§7-bis.11)')
            accion = reglas.get(motor.norm(rot))
            if accion and accion[0] == 'suprimir':
                self.anota('Inversión: fuera «' + rot + '» — '
                           + (accion[1] or 'lo pide el módulo de contenido'))
                continue
            if accion and motor._es_numero(accion[0]):
                self.anota('Inversión: «' + rot + '» ' + str(importe) + ' → '
                           + str(accion[0]) + ' — ' + (accion[1] or ''))
                importe, nota = float(accion[0]), accion[1] or nota
            bloque = bloque or 'INVERSIÓN'
            if bloque not in bloques:
                bloques[bloque] = []
                orden.append(bloque)
            bloques[bloque].append((rot, importe, nota))
        for bloque, rot, importe, nota, _fuente in [
                tuple(list(e) + [None] * 5)[:5] for e in extras]:
            bloque = bloque or (orden[0] if orden else 'INVERSIÓN')
            if bloque not in bloques:
                bloques[bloque] = []
                orden.append(bloque)
            bloques[bloque].append((rot, importe, nota))

        rej = Rejilla(ws, cab + 1)
        self.rej['inversion'] = rej
        alq = self.p.ref('alquiler_mes')
        fianza_m = self.p.ref('fianza_meses')
        claves_bloque, amortiza = [], {'obra': [], 'maquinaria': []}
        # un bloque sin partidas (el «FONDO DE MANIOBRA» original, cuya única
        # línea es canónica y la regenera este grupo) no se escribe: dejarlo
        # produciría un `SUM` sobre sí mismo, que Excel marca como referencia
        # circular
        orden = [b for b in orden if bloques.get(b)]
        for bloque in orden:
            clave_b = 'b_' + str(len(claves_bloque))
            claves_bloque.append(clave_b)
            rej.add(clave_b, rot=bloque, bold=True, fmt=motor.FMT_EUR0,
                    fmt_C=motor.FMT_PCT)
            primero = None
            for rot, importe, nota in bloques[bloque]:
                clave = 'i_%d' % len(rej.filas)
                primero = primero or clave
                grupo = _clasificar_amortizable(rot, tablas)
                if grupo in amortiza:
                    amortiza[grupo].append(clave)
                rej.add(clave, rot=rot,
                        valores={'B': importe, 'D': nota or ''},
                        fmt=motor.FMT_EUR0, verde=True,
                        formulas={'C': (lambda R, k=clave:
                                        '=' + R.c(k) + '/'
                                        + R.c('total', absoluta=True))},
                        fmt_C=motor.FMT_PCT)
            # las derivadas del alquiler, dentro de su bloque
            if bloque == orden[0]:
                rej.add('fianza', rot='Fianza del alquiler',
                        fmt=motor.FMT_EUR0, fmt_C=motor.FMT_PCT,
                        formulas={
                            'B': '=' + alq + '*' + fianza_m,
                            'C': (lambda R: '=' + R.c('fianza') + '/'
                                  + R.c('total', absoluta=True)),
                            'D': texto_num(fianza_m, '', ' meses de renta, al '
                                           'tipo de la hoja de Supuestos')})
                rej.add('renta1', rot='Primera mensualidad de alquiler',
                        fmt=motor.FMT_EUR0, fmt_C=motor.FMT_PCT,
                        formulas={
                            'B': '=' + alq,
                            'C': (lambda R: '=' + R.c('renta1') + '/'
                                  + R.c('total', absoluta=True)),
                            'D': '="Se paga por adelantado junto con la '
                                 'fianza"'})
            ultimo_b = rej.filas[-1]['clave']
            rej.filas[rej.fila(clave_b) - rej.fila0]['formulas'] = {
                'B': ((lambda R, a=primero, b=ultimo_b:
                       '=SUM(' + R.c(a) + ':' + R.c(b) + ')')
                      if primero and ultimo_b != clave_b else '=0'),
                'C': (lambda R, k=clave_b: '=' + R.c(k) + '/'
                      + R.c('total', absoluta=True))}
        # fondo de maniobra (TEC-07, DOM-12, NUEVO-01)
        clave_b = 'b_fondo'
        claves_bloque.append(clave_b)
        rej.add(clave_b, rot='FONDO DE MANIOBRA', bold=True,
                fmt=motor.FMT_EUR0, fmt_C=motor.FMT_PCT,
                formulas={'B': (lambda R: '=' + R.c('fondo')),
                          'C': (lambda R: '=' + R.c(clave_b) + '/'
                                + R.c('total', absoluta=True))})
        meses = self.p.ref('meses_fondo')
        rej.add('fondo', rot='Colchón operativo hasta alcanzar el equilibrio',
                fmt=motor.FMT_EUR0, fmt_C=motor.FMT_PCT,
                formulas={
                    # ⚠️ una referencia a una celda VACÍA devuelve 0, no
                    # `""`: sin este guarda, un libro en blanco dota un fondo
                    # de «0 €» y el semáforo de la tesorería se pone verde
                    'B': (lambda R: '=IF(' + meses + '*'
                          + self.rej['pyg'].r('tcf') + '=0,"",' + meses + '*'
                          + self.rej['pyg'].r('tcf') + '/12)'),
                    'C': (lambda R: '=' + R.c('fondo') + '/'
                          + R.c('total', absoluta=True)),
                    'D': texto_num(meses, 'Cubre ', ' meses de costes fijos '
                                   'del año 1, que es el mínimo que exigen '
                                   'las Instrucciones de este libro')})
        rej.add('total', rot='INVERSIÓN TOTAL (suma de los bloques)',
                bold=True, fmt=motor.FMT_EUR0,
                formulas={'B': (lambda R: '=' + '+'.join(
                    R.c(k) for k in claves_bloque))})
        # IVA soportado (TEC-11): suma a la caja aunque sea recuperable
        sin_iva = ['fianza', 'fondo']
        rej.add('iva', rot='IVA soportado sobre la inversión (recuperable)',
                fmt=motor.FMT_EUR0,
                formulas={
                    'B': (lambda R: '=(' + R.c('total') + '-'
                          + '-'.join(R.c(k) for k in sin_iva) + ')*'
                          + self.p.ref('iva_soportado')),
                    'D': texto_pct(self.p.ref('iva_soportado'),
                                   'Al ', ' sobre todo menos la fianza y el '
                                   'fondo de maniobra. Se recupera con el '
                                   'modelo 303, pero hay que adelantarlo')})
        rej.add('caja', rot='NECESIDAD TOTAL DE CAJA AL ARRANQUE', bold=True,
                fmt=motor.FMT_EUR0,
                formulas={'B': (lambda R: '=' + R.c('total') + '+'
                                + R.c('iva')),
                          'D': '="Es la cifra que tiene que cubrir la hoja de '
                               'Financiación"'})
        # bases de amortización (TEC-20, NUEVO-02)
        rej.add('b_amort', rot='BASES DE AMORTIZACIÓN (no suman a la '
                'inversión)', bold=True)
        for grupo, etiqueta, vida in (
                ('obra', 'Obra, instalaciones y acondicionamiento',
                 self.p.ref('vida_obra')),
                ('maquinaria', 'Maquinaria, mobiliario y equipos',
                 self.p.ref('vida_maquinaria'))):
            claves = amortiza[grupo]
            rej.add('base_' + grupo, rot=etiqueta, fmt=motor.FMT_EUR0,
                    formulas={
                        'B': (lambda R, ks=tuple(claves):
                              '=' + ('+'.join(R.c(k) for k in ks) if ks
                                     else '0')),
                        'D': texto_num(vida, 'Se amortiza en ', ' años')})
        rej.add('amort', rot='Amortización anual del inmovilizado', bold=True,
                fmt=motor.FMT_EUR0,
                formulas={
                    'B': (lambda R: '=' + R.c('base_obra') + '/'
                          + self.p.ref('vida_obra') + '+'
                          + R.c('base_maquinaria') + '/'
                          + self.p.ref('vida_maquinaria')),
                    'D': '="El fondo de maniobra, el stock y los imprevistos '
                         "NO se amortizan: no son inmovilizado\""})
        self.pendientes.append(rej)
        motor.semaforo_num(ws, rej.c('caja') + ':' + rej.c('caja'),
                           verde_si=rej.c('caja') + '>0')
        fila = rej.ultima + 2
        for i, texto in enumerate(pie):
            motor.val(ws, 'A' + str(fila + i), texto, wrap=True)
        motor.anchos(ws, {'A': 46, 'B': 15, 'C': 13, 'D': 58})
        motor.print_setup(ws, header_row=cab)
        return rej

    # -- §2.3 -------------------------------------------------------------
    def pyg(self):
        """`P&L 3 Años`: la cadena completa desde los supuestos (§2.3)."""
        ws = self.ws_pyg
        cab = _cabecera(ws)
        fijos = self._fijos(ws, cab)
        pie = _pie(ws, cab)
        _limpiar_area(ws, cab, ws.max_row, 7)
        for i, texto in enumerate(('Concepto', 'Año 1', 'Año 2', 'Año 3',
                                   '% s/ventas (año 1)', 'Notas')):
            motor.val(ws, get_column_letter(i + 1) + str(cab), texto,
                      bold=True, wrap=True)
        rej = Rejilla(ws, cab + 1)
        self.rej['pyg'] = rej
        P = self.p.ref
        crec2, crec3, ipc = P('crec_a2'), P('crec_a3'), P('ipc')

        def pct(clave):
            return (lambda R, k=clave: '=' + R.c(k) + '/' + R.c(
                'ingresos', absoluta=True))

        rej.add(rot='INGRESOS', bold=True)
        rej.add('cub', rot='Cubiertos/día (media)', fmt=motor.FMT_ENT,
                formulas={'B': '=' + P('cubiertos_dia'),
                          'C': (lambda R: '=' + R.c('cub') + '*(1+' + crec2
                                + ')'),
                          'D': (lambda R: '=' + R.c('cub', 'C') + '*(1+'
                                + crec3 + ')'),
                          'F': '="El crecimiento de los años 2 y 3 está en la '
                               'hoja de Supuestos"'})
        rej.add('ticket', rot='Ticket medio sin IVA', fmt=motor.FMT_EUR,
                formulas={'B': '=' + P('ticket_medio'),
                          'C': (lambda R: '=' + R.c('ticket')),
                          'D': (lambda R: '=' + R.c('ticket', 'C')),
                          'F': '="Constante en euros del año 1: una subida de '
                               'precios es una decisión aparte"'})
        rej.add('dias', rot='Días de apertura al año', fmt=motor.FMT_ENT,
                formulas={'B': '=' + P('dias_apertura'),
                          'C': (lambda R: '=' + R.c('dias')),
                          'D': (lambda R: '=' + R.c('dias', 'C'))})
        rej.add('ingresos', rot='INGRESOS TOTALES (sin IVA)', bold=True,
                fmt=motor.FMT_EUR0, fmt_E=motor.FMT_PCT,
                formulas=dict(
                    [(col, (lambda R, c=col: '=IF(' + R.c('cub', c) + '*'
                            + R.c('ticket', c) + '*' + R.c('dias', c)
                            + '=0,"",' + R.c('cub', c) + '*'
                            + R.c('ticket', c) + '*' + R.c('dias', c) + ')'))
                     for col in ('B', 'C', 'D')]
                    + [('E', '=1')]))
        lineas = self.lineas_ingreso()
        for i, linea in enumerate(lineas):
            rot, peso, grupo, nota, _fuente = (list(linea) + [None] * 5)[:5]
            clave = 'lin_%d' % i
            ultimo = i == len(lineas) - 1
            spec = {
                'rot': rot, 'fmt': motor.FMT_EUR0, 'fmt_E': motor.FMT_PCT,
                'formulas': dict(
                    (col, (lambda R, c=col, k=clave: '=' + R.c('ingresos', c)
                           + '*' + R.c(k, 'E', absoluta=True)))
                    for col in ('B', 'C', 'D')),
                'valores': {'F': nota or ('Bebida' if grupo == 'bebida'
                                          else 'Comida')},
            }
            if ultimo and len(lineas) > 1:
                otros = ['lin_%d' % j for j in range(len(lineas) - 1)]
                spec['formulas']['E'] = (lambda R, ks=tuple(otros):
                                         '=1-' + '-'.join(R.c(k, 'E')
                                                          for k in ks))
            else:
                spec['valores']['E'] = peso
                spec['verde'] = True
            rej.add(clave, **spec)
        rej.add(rot='COSTES VARIABLES', bold=True)
        rej.add('cv_comida', rot='Coste de mercancía — comida',
                fmt=motor.FMT_EUR0, fmt_E=motor.FMT_PCT,
                formulas=dict(
                    [(col, (lambda R, c=col: '=' + R.c('ingresos', c) + '*'
                            + P('pct_comida') + '*' + P('coste_comida')))
                     for col in ('B', 'C', 'D')]
                    + [('E', pct('cv_comida')),
                       ('F', texto_pct(P('coste_comida'), 'Al ',
                                       ' de las ventas de COMIDA, no del '
                                       'total: la bebida tiene su propia '
                                       'línea'))]))
        rej.add('cv_bebida', rot='Coste de mercancía — bebida',
                fmt=motor.FMT_EUR0, fmt_E=motor.FMT_PCT,
                formulas=dict(
                    [(col, (lambda R, c=col: '=' + R.c('ingresos', c) + '*'
                            + P('pct_bebida') + '*' + P('coste_bebida')))
                     for col in ('B', 'C', 'D')]
                    + [('E', pct('cv_bebida')),
                       ('F', texto_pct(P('coste_bebida'), 'Al ',
                                       ' de las ventas de BEBIDA'))]))
        rej.add('cv_cons', rot='Consumibles y envases', fmt=motor.FMT_EUR0,
                fmt_E=motor.FMT_PCT,
                formulas=dict(
                    [(col, (lambda R, c=col: '=' + R.c('ingresos', c) + '*'
                            + P('pct_consumibles')))
                     for col in ('B', 'C', 'D')]
                    + [('E', pct('cv_cons'))]))
        rej.add('cv_deliv', rot='Comisiones de delivery',
                fmt=motor.FMT_EUR0, fmt_E=motor.FMT_PCT,
                formulas=dict(
                    [(col, (lambda R, c=col: '=' + R.c('ingresos', c) + '*'
                            + P('pct_delivery') + '*' + P('comision_delivery')))
                     for col in ('B', 'C', 'D')]
                    + [('E', pct('cv_deliv')),
                       ('F', '="Sobre las ventas DEL CANAL. Con 0 % de '
                        'delivery en Supuestos, esta línea vale cero"')]))
        rej.add('cv_tpv', rot='Comisiones de los medios de pago',
                fmt=motor.FMT_EUR0, fmt_E=motor.FMT_PCT,
                formulas=dict(
                    [(col, (lambda R, c=col: '=' + R.c('ingresos', c) + '*'
                            + P('comision_tpv')))
                     for col in ('B', 'C', 'D')]
                    + [('E', pct('cv_tpv'))]))
        rej.add('tcv', rot='TOTAL COSTES VARIABLES', bold=True,
                fmt=motor.FMT_EUR0, fmt_E=motor.FMT_PCT,
                formulas=dict(
                    [(col, (lambda R, c=col: '=SUM(' + R.c('cv_comida', c)
                            + ':' + R.c('cv_tpv', c) + ')'))
                     for col in ('B', 'C', 'D')] + [('E', pct('tcv'))]))
        rej.add('mb', rot='MARGEN BRUTO', bold=True, fmt=motor.FMT_EUR0,
                fmt_E=motor.FMT_PCT,
                formulas=dict(
                    [(col, (lambda R, c=col: '=' + R.c('ingresos', c) + '-'
                            + R.c('tcv', c)))
                     for col in ('B', 'C', 'D')] + [('E', pct('mb'))]))
        rej.add(rot='COSTES FIJOS', bold=True)
        claves_fijos = []

        def fijo(clave, rot, formula_b, nota=None, verde=False, valor=None,
                 crece_con_volumen=False):
            claves_fijos.append(clave)
            spec = {'rot': rot, 'fmt': motor.FMT_EUR0,
                    'fmt_E': motor.FMT_PCT,
                    'formulas': {'E': pct(clave)}}
            if valor is not None:
                spec['valores'] = {'B': valor}
                spec['verdes'] = ('B',)     # la nota no se pinta de verde
            else:
                spec['formulas']['B'] = formula_b
            factor2 = '*(1+' + ipc + ')'
            factor3 = '*(1+' + ipc + ')'
            if crece_con_volumen:
                factor2 = '*(1+' + crec2 + ')*(1+' + ipc + ')'
                factor3 = '*(1+' + crec3 + ')*(1+' + ipc + ')'
            spec['formulas']['C'] = (lambda R, k=clave, f=factor2:
                                     '=' + R.c(k) + f)
            spec['formulas']['D'] = (lambda R, k=clave, f=factor3:
                                     '=' + R.c(k, 'C') + f)
            if nota:
                destino = ('formulas' if str(nota).startswith('=')
                           else 'valores')
                spec.setdefault(destino, {})['F'] = nota
            rej.add(clave, **spec)

        fijo('cf_alquiler', 'Alquiler del local',
             '=' + P('alquiler_mes') + '*12',
             nota='="El importe mensual está en la hoja de Supuestos; aquí '
                  'se multiplica por doce"')
        fijo('cf_personal', 'Personal (nóminas + Seguridad Social)',
             (lambda R: '=' + self.rej['personal'].r('total', 'F')),
             nota='="Sale de la hoja de Personal: es el MISMO número, no una '
                  'estimación aparte"', crece_con_volumen=True)
        fijo('cf_suministros', 'Suministros (luz, agua, gas)',
             '=' + P('suministros_mes') + '*12')
        fijo('cf_seguros', 'Seguros (RC + multirriesgo)',
             '=' + P('seguros_ano'))
        for i, (rot, importe, nota) in enumerate(fijos):
            fijo('cf_p%d' % i, rot, None, valor=importe,
                 nota=nota if isinstance(nota, str) else None)
        fijo('cf_amort', 'Amortización del inmovilizado',
             (lambda R: '=' + self.rej['inversion'].r('amort')),
             nota='="Sale de las bases de amortización de la hoja de '
                  'Inversión: sólo inmovilizado real"')
        fijo('cf_int', 'Gastos financieros (intereses del préstamo)',
             (lambda R: '=' + self.rej['financiacion'].r('int_1')),
             nota='="Sólo los INTERESES son gasto. La devolución del '
                  'principal va en la hoja de Tesorería"')
        rej.filas[rej.fila('cf_int') - rej.fila0]['formulas']['C'] = (
            lambda R: '=' + self.rej['financiacion'].r('int_2'))
        rej.filas[rej.fila('cf_int') - rej.fila0]['formulas']['D'] = (
            lambda R: '=' + self.rej['financiacion'].r('int_3'))
        fijo('cf_varios', 'Varios e imprevistos',
             (lambda R: '=' + R.c('ingresos') + '*' + P('pct_varios')),
             nota=texto_pct(P('pct_varios'), 'Al ', ' de las ventas'))
        for col, otro in (('C', 'C'), ('D', 'D')):
            rej.filas[rej.fila('cf_varios') - rej.fila0]['formulas'][col] = (
                lambda R, c=col: '=' + R.c('ingresos', c) + '*'
                + P('pct_varios'))
        rej.add('tcf', rot='TOTAL COSTES FIJOS', bold=True,
                fmt=motor.FMT_EUR0, fmt_E=motor.FMT_PCT,
                formulas=dict(
                    [(col, (lambda R, c=col: '=SUM(' + R.c(claves_fijos[0], c)
                            + ':' + R.c(claves_fijos[-1], c) + ')'))
                     for col in ('B', 'C', 'D')] + [('E', pct('tcf'))]))
        rej.add('rai', rot='RESULTADO ANTES DE IMPUESTOS', bold=True,
                fmt=motor.FMT_EUR0, fmt_E=motor.FMT_PCT,
                formulas=dict(
                    [(col, (lambda R, c=col: '=' + R.c('mb', c) + '-'
                            + R.c('tcf', c)))
                     for col in ('B', 'C', 'D')] + [('E', pct('rai'))]))
        # Impuesto de Sociedades con BIN y tipo de nueva creación (TEC-06)
        rej.add('bin_ini', rot='Bases negativas pendientes al inicio',
                fmt=motor.FMT_EUR0,
                formulas={'B': '=' + P('bin_inicial'),
                          'C': (lambda R: '=' + R.c('bin_fin')),
                          'D': (lambda R: '=' + R.c('bin_fin', 'C')),
                          'F': '="Art. 26 LIS: las pérdidas de un ejercicio '
                               'se compensan con los beneficios de los '
                               'siguientes"'})
        rej.add('base', rot='Base imponible (después de compensar)',
                fmt=motor.FMT_EUR0,
                formulas=dict(
                    (col, (lambda R, c=col: '=MAX(0,' + R.c('rai', c) + '-'
                           + R.c('bin_ini', c) + ')'))
                    for col in ('B', 'C', 'D')))
        rej.add('acum', rot='Ejercicios con base positiva (acumulado)',
                fmt=motor.FMT_ENT,
                formulas={'B': (lambda R: '=IF(' + R.c('base') + '>0,1,0)'),
                          'C': (lambda R: '=' + R.c('acum') + '+IF('
                                + R.c('base', 'C') + '>0,1,0)'),
                          'D': (lambda R: '=' + R.c('acum', 'C') + '+IF('
                                + R.c('base', 'D') + '>0,1,0)')})
        rej.add('tipo', rot='Tipo de Impuesto de Sociedades aplicado',
                fmt=motor.FMT_PCT,
                formulas=dict(
                    [(col, (lambda R, c=col: '=IF(' + R.c('base', c)
                            + '<=0,"",IF(' + R.c('acum', c) + '<=2,'
                            + P('is_nueva') + ',' + P('is_general') + '))'))
                     for col in ('B', 'C', 'D')]
                    + [('F', '="Art. 29.1 LIS: el tipo reducido de entidad de '
                        'nueva creación se aplica a los DOS primeros '
                        'ejercicios con base positiva, no al primer año"')]))
        rej.add('is', rot='Impuesto de Sociedades', fmt=motor.FMT_EUR0,
                formulas=dict(
                    (col, (lambda R, c=col: '=IF(' + R.c('tipo', c)
                           + '="",0,' + R.c('base', c) + '*' + R.c('tipo', c)
                           + ')'))
                    for col in ('B', 'C', 'D')))
        rej.add('bin_fin', rot='Bases negativas pendientes al cierre',
                fmt=motor.FMT_EUR0,
                formulas=dict(
                    (col, (lambda R, c=col: '=MAX(0,' + R.c('bin_ini', c)
                           + '-' + R.c('rai', c) + ')'))
                    for col in ('B', 'C', 'D')))
        rej.add('neto', rot='RESULTADO NETO', bold=True, fmt=motor.FMT_EUR0,
                fmt_E=motor.FMT_PCT,
                formulas=dict(
                    [(col, (lambda R, c=col: '=' + R.c('rai', c) + '-'
                            + R.c('is', c)))
                     for col in ('B', 'C', 'D')] + [('E', pct('neto'))]))
        # ---- ratios que auditan (TEC-12, §2.9) --------------------------
        rej.add(rot='RATIOS CLAVE', bold=True)
        rej.add('cab_ratios', rot='Ratio', bold=True,
                valores={'B': 'Año 1', 'C': 'Año 2', 'D': 'Año 3',
                         'E': 'Umbral', 'F': 'Comentario'})
        umbrales = dict((u[0], u) for u in (self.dato('UMBRALES') or ()))

        def ratio(clave, rot, numerador, umbral, comentario, verde_si_menor,
                  fmt_um=motor.FMT_PCT):
            u = umbrales.get(clave)
            valor = u[2] if u else umbral
            texto = u[3] if u else comentario
            rej.add(clave, rot=rot, fmt=motor.FMT_PCT, fmt_E=fmt_um,
                    valores={'E': valor, 'F': texto}, verde=True,
                    formulas=dict(
                        (col, (lambda R, c=col, n=numerador:
                               '=' + R.c(n, c) + '/' + R.c('ingresos', c)))
                        for col in ('B', 'C', 'D')))
            ancla = rej.c(clave)
            comparador = ('<=' if verde_si_menor else '>=')
            contrario = ('>' if verde_si_menor else '<')
            motor.semaforo_num(
                rej.ws, ancla + ':' + rej.c(clave, 'D'),
                verde_si=ancla + comparador + rej.c(clave, 'E', absoluta=True),
                rojo_si=ancla + contrario + rej.c(clave, 'E', absoluta=True))

        ratio('r_mb', 'Margen bruto / Ventas', 'mb', 0.65,
              'Objetivo del formato; por debajo, revisa precios o compras',
              False)
        rej.add('cogs', rot='Coste de mercancía (comida + bebida)',
                fmt=motor.FMT_EUR0, fmt_E=motor.FMT_PCT,
                formulas=dict(
                    (col, (lambda R, c=col: '=' + R.c('cv_comida', c) + '+'
                           + R.c('cv_bebida', c)))
                    for col in ('B', 'C', 'D')))
        ratio('r_cogs', 'Coste de mercancía / Ventas', 'cogs', 0.32,
              'El food cost REAL del libro, calculado, no tecleado', True)
        ratio('r_personal', 'Coste de personal / Ventas', 'cf_personal', 0.35,
              'Techo que fijan las Instrucciones de este mismo libro', True)
        ratio('r_alquiler', 'Alquiler / Ventas', 'cf_alquiler', 0.10,
              'Por encima del 10 % el local se come el margen', True)
        ratio('r_neto', 'Resultado neto / Ventas', 'neto', 0.05,
              'Suelo de rentabilidad del sector', False)
        rej.add('r_be', rot='Punto de equilibrio alcanzado',
                formulas={
                    'B': (lambda R: '=IF(' + R.c('ingresos') + '="","",IF('
                          + R.c('ingresos') + '>='
                          + self.rej['equilibrio'].r('ingresos_be')
                          + ',"Sí","No"))'),
                    'C': (lambda R: '=IF(' + R.c('ingresos', 'C')
                          + '="","",IF(' + R.c('ingresos', 'C') + '>='
                          + self.rej['equilibrio'].r('ingresos_be')
                          + ',"Sí","No"))'),
                    'D': (lambda R: '=IF(' + R.c('ingresos', 'D')
                          + '="","",IF(' + R.c('ingresos', 'D') + '>='
                          + self.rej['equilibrio'].r('ingresos_be')
                          + ',"Sí","No"))'),
                    'F': '="Compara las ventas del año con el umbral que '
                         'calcula la hoja de Punto de Equilibrio"'})
        motor.semaforo_texto(rej.ws, rej.c('r_be') + ':' + rej.c('r_be', 'D'),
                             (('Sí', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
                              ('No', motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
        self.pendientes.append(rej)
        fila = rej.ultima + 2
        motor.val(ws, 'A' + str(fila),
                  'Todas las cifras van SIN IVA. Las columnas de los años 2 '
                  'y 3 están en euros del año 1 salvo que subas la '
                  'actualización de costes en la hoja de Supuestos.',
                  wrap=True)
        for i, texto in enumerate(pie):
            motor.val(ws, 'A' + str(fila + 1 + i), texto)
        motor.anchos(ws, {'A': 42, 'B': 15, 'C': 15, 'D': 15, 'E': 13,
                          'F': 60})
        motor.print_setup(ws, header_row=cab)
        return rej

    def _fijos(self, ws, cab):
        """Costes fijos que se CONSERVAN como input (§1.3)."""
        reglas = self.dato('FIJOS', {}) or {}
        fuera = []
        # SOLO el bloque de costes fijos: debajo están el EBITDA, el impuesto
        # y el resultado neto, que también son números en la columna B.
        r0, r1 = _seccion(ws, cab, r'^costes fijos',
                          r'^total costes fijos')
        if r0 is None:
            self.anota('P&L: no se encuentra el bloque «COSTES FIJOS» en '
                       + ws.title + ': sólo se escriben las partidas del '
                       'módulo de contenido (no se adivina)')
            r0 = r1 = cab
        for _r, rot, importe, nota, _bloque in _partidas(
                ws, cab, canon=RX_CANON_PYG, desde=r0, hasta=r1):
            rot, cambiado = _limpiar_rotulo(rot)
            if cambiado:
                self.anota('P&L: rótulo con parámetro escrito a mano → «'
                           + rot + '» (§7-bis.11)')
            accion = reglas.get(motor.norm(rot))
            if accion and accion[0] == 'suprimir':
                self.anota('P&L: fuera «' + rot + '» — '
                           + (accion[1] or 'lo pide el módulo de contenido'))
                continue
            if accion and motor._es_numero(accion[0]):
                self.anota('P&L: «' + rot + '» ' + str(importe) + ' → '
                           + str(accion[0]) + ' — ' + (accion[1] or ''))
                importe, nota = float(accion[0]), accion[1] or nota
            fuera.append((rot, importe, nota))
        # los extras se añaden UNA vez: en la 2.ª pasada ya están dentro del
        # bloque de costes fijos y `_partidas` los devuelve como preservados
        ya = set(motor.norm(r) for r, _i, _n in fuera)
        for extra in (self.dato('FIJOS_EXTRA', []) or []):
            rot, importe, nota, _fuente = (list(extra) + [None] * 4)[:4]
            if motor.norm(rot) in ya:
                continue
            ya.add(motor.norm(rot))
            fuera.append((rot, importe, nota))
        return fuera

    # -- §2.4 -------------------------------------------------------------
    def equilibrio(self):
        """`Punto de Equilibrio`: uno solo, derivado, con sensibilidad."""
        ws = self.ws_equilibrio
        cab = _cabecera(ws)
        pie = _pie(ws, cab)
        _limpiar_area(ws, cab, ws.max_row + 20, 6)
        for i, texto in enumerate(('Variable', 'Valor', 'Notas')):
            motor.val(ws, get_column_letter(i + 1) + str(cab), texto,
                      bold=True)
        rej = Rejilla(ws, cab + 1)
        self.rej['equilibrio'] = rej
        pyg = self.rej['pyg']
        rej.add(rot='DATOS BASE (año 1)', bold=True)
        rej.add('cf_mes', rot='Costes fijos mensuales', fmt=motor.FMT_EUR,
                formulas={'B': '=' + pyg.r('tcf') + '/12',
                          'C': '="Los MISMOS costes fijos del P&L, divididos '
                               'entre doce"'})
        rej.add('cf_ano', rot='Costes fijos anuales', fmt=motor.FMT_EUR,
                formulas={'B': '=' + pyg.r('tcf')})
        rej.add('ticket', rot='Ticket medio sin IVA', fmt=motor.FMT_EUR,
                formulas={'B': '=' + pyg.r('ticket')})
        rej.add('cvu', rot='Coste variable por cubierto', fmt=motor.FMT_EUR,
                formulas={'B': '=' + pyg.r('tcv') + '/(' + pyg.r('cub') + '*'
                          + pyg.r('dias') + ')',
                          'C': '="Sale del total de costes variables del P&L, '
                               'no de una estimación aparte"'})
        rej.add('mc', rot='Margen de contribución por cubierto',
                fmt=motor.FMT_EUR,
                formulas={'B': (lambda R: '=' + R.c('ticket') + '-'
                                + R.c('cvu')),
                          'C': '="Ticket menos coste variable unitario"'})
        rej.add('dias', rot='Días de apertura al año', fmt=motor.FMT_ENT,
                formulas={'B': '=' + pyg.r('dias'),
                          'C': '="El mismo calendario que el P&L y que los '
                               'escenarios"'})
        rej.add(rot='PUNTO DE EQUILIBRIO', bold=True)
        rej.add('cub_ano', rot='Cubiertos necesarios al año',
                fmt=motor.FMT_ENT,
                formulas={'B': (lambda R: '=IF(' + R.c('mc')
                                + '<=0,"Margen de contribución negativo",'
                                + R.c('cf_ano') + '/' + R.c('mc') + ')')})
        rej.add('cub_dia', rot='Cubiertos necesarios al día',
                fmt=motor.FMT_DEC,
                formulas={'B': (lambda R: '=' + R.c('cub_ano') + '/'
                                + R.c('dias'))})
        rej.add('ingresos_be', rot='Ingresos necesarios al año',
                fmt=motor.FMT_EUR0, bold=True,
                formulas={'B': (lambda R: '=' + R.c('cub_ano') + '*'
                                + R.c('ticket'))})
        rej.add('cub_plan', rot='Cubiertos/día previstos en el plan',
                fmt=motor.FMT_ENT, formulas={'B': '=' + pyg.r('cub')})
        rej.add('holgura', rot='Holgura sobre el punto de equilibrio (%)',
                fmt=motor.FMT_PCT,
                formulas={'B': (lambda R: '=' + R.c('cub_plan') + '/'
                                + R.c('cub_dia') + '-1'),
                          'C': '="Cuánto puedes caer antes de entrar en '
                               'pérdidas"'})
        motor.semaforo_num(ws, rej.c('holgura') + ':' + rej.c('holgura'),
                           verde_si=rej.c('holgura') + '>=0.15',
                           ambar_si=rej.c('holgura') + '>=0',
                           rojo_si=rej.c('holgura') + '<0')
        rej.add(rot='INTERPRETACIÓN', bold=True)
        rej.add('texto', wrap=True, alto=46,
                formulas={'A': (lambda R:
                                '="Con el ticket medio sin IVA de la fila de '
                                'arriba necesitas servir "&TEXT('
                                + R.c('cub_dia') + ',"0")&" cubiertos al día '
                                'durante los "&TEXT(' + R.c('dias') + ',"0")&'
                                '" días que abres para cubrir todos los '
                                'costes fijos y variables; en la fila '
                                '«Ingresos necesarios al año» tienes esa '
                                'misma cifra en euros. Por debajo el negocio '
                                'pierde dinero y por encima cada cubierto '
                                'aporta el margen de contribución de la fila '
                                'de arriba."')})
        self.pendientes.append(rej)
        fila = self._sensibilidad(ws, rej) + 2
        for i, texto in enumerate(pie):
            motor.val(ws, 'A' + str(fila + i), texto)
        motor.anchos(ws, {'A': 44, 'B': 16, 'C': 46, 'D': 14, 'E': 14,
                          'F': 14})
        motor.print_setup(ws, header_row=cab)
        return rej

    def _sensibilidad(self, ws, rej):
        """Tabla de sensibilidad al ticket y al coste variable (TEC-19)."""
        fila0 = rej.ultima + 2
        motor.val(ws, 'A' + str(fila0), 'SENSIBILIDAD DEL PUNTO DE '
                  'EQUILIBRIO', bold=True)
        motor.val(ws, 'A' + str(fila0 + 1),
                  'Cubiertos/día necesarios para cubrir costes según el '
                  'ticket medio (columnas) y el coste variable por cubierto '
                  '(filas). En verde, los que están por debajo de los '
                  'cubiertos que prevé el plan.', wrap=True)
        ws.row_dimensions[fila0 + 1].height = 30
        cabf = fila0 + 3
        motor.val(ws, 'A' + str(cabf), 'Coste variable / cubierto', bold=True,
                  wrap=True)
        tk = rej.c('ticket', absoluta=True)
        for j, delta in enumerate((-2, 0, 2, 4)):
            col = get_column_letter(2 + j)
            fx(ws, col + str(cabf), '=' + tk + ('+' + str(delta) if delta
                                                else ''), motor.FMT_EUR)
            ws[col + str(cabf)].font = Font(bold=True)
        cv = rej.c('cvu', absoluta=True)
        cf = rej.c('cf_ano', absoluta=True)
        dias = rej.c('dias', absoluta=True)
        plan = rej.c('cub_plan', absoluta=True)
        for i, factor in enumerate((0.85, 0.925, 1.0, 1.075, 1.15)):
            fila = cabf + 1 + i
            fx(ws, 'A' + str(fila), '=' + cv + '*' + str(factor),
               motor.FMT_EUR)
            for j in range(4):
                col = get_column_letter(2 + j)
                cabecera = '$' + col + '$' + str(cabf)
                fx(ws, col + str(fila),
                   '=IF(' + cabecera + '-$A' + str(fila) + '<=0,"",' + cf
                   + '/(' + cabecera + '-$A' + str(fila) + ')/' + dias + ')',
                   motor.FMT_DEC)
        rango = 'B' + str(cabf + 1) + ':E' + str(cabf + 5)
        motor.semaforo_num(ws, rango, verde_si='B' + str(cabf + 1) + '<='
                           + plan, rojo_si='B' + str(cabf + 1) + '>' + plan)
        return cabf + 5

    # -- §2.5 -------------------------------------------------------------
    def escenarios(self):
        """`Escenarios`: el MISMO motor que el P&L (§2.5, TEC-02)."""
        ws = self.ws_escenarios
        cab = _cabecera(ws)
        pie = _pie(ws, cab)
        anteriores = self._leer_escenarios(ws, cab)
        _limpiar_area(ws, cab, ws.max_row, 6)
        for i, texto in enumerate(('Métrica', 'Pesimista', 'Realista',
                                   'Optimista', 'Notas')):
            motor.val(ws, get_column_letter(i + 1) + str(cab), texto,
                      bold=True)
        rej = Rejilla(ws, cab + 1)
        self.rej['escenarios'] = rej
        pyg = self.rej['pyg']
        P = self.p.ref
        cols = ('B', 'C', 'D')

        def driver(clave, rot, ref_pyg, fmt, idx):
            rej.add(clave, rot=rot, fmt=fmt, verde=True,
                    valores={'B': anteriores['pesimista'][idx],
                             'D': anteriores['optimista'][idx]},
                    formulas={'C': '=' + ref_pyg})

        driver('cub', 'Cubiertos/día', pyg.r('cub'), motor.FMT_ENT, 0)
        driver('ticket', 'Ticket medio sin IVA', pyg.r('ticket'),
               motor.FMT_EUR, 1)
        driver('dias', 'Días de apertura al año', pyg.r('dias'),
               motor.FMT_ENT, 2)
        rej.add('ingresos', rot='INGRESOS ANUALES (sin IVA)', bold=True,
                fmt=motor.FMT_EUR0,
                formulas=dict(
                    (col, (lambda R, c=col: '=IF(' + R.c('cub', c) + '*'
                           + R.c('ticket', c) + '*' + R.c('dias', c)
                           + '=0,"",' + R.c('cub', c) + '*'
                           + R.c('ticket', c) + '*' + R.c('dias', c) + ')'))
                    for col in cols))
        for clave, rot, factor in (
                ('cv_comida', 'Coste de mercancía — comida',
                 P('pct_comida') + '*' + P('coste_comida')),
                ('cv_bebida', 'Coste de mercancía — bebida',
                 P('pct_bebida') + '*' + P('coste_bebida')),
                ('cv_cons', 'Consumibles y envases', P('pct_consumibles')),
                ('cv_deliv', 'Comisiones de delivery',
                 P('pct_delivery') + '*' + P('comision_delivery')),
                ('cv_tpv', 'Comisiones de los medios de pago',
                 P('comision_tpv'))):
            rej.add(clave, rot=rot, fmt=motor.FMT_EUR0,
                    formulas=dict(
                        (col, (lambda R, c=col, f=factor:
                               '=' + R.c('ingresos', c) + '*' + f))
                        for col in cols))
        rej.add('tcv', rot='TOTAL COSTES VARIABLES', fmt=motor.FMT_EUR0,
                formulas=dict(
                    (col, (lambda R, c=col: '=SUM(' + R.c('cv_comida', c)
                           + ':' + R.c('cv_tpv', c) + ')')) for col in cols))
        rej.add('mb', rot='MARGEN BRUTO', fmt=motor.FMT_EUR0,
                formulas=dict(
                    (col, (lambda R, c=col: '=' + R.c('ingresos', c) + '-'
                           + R.c('tcv', c))) for col in cols))
        rej.add('cf', rot='COSTES FIJOS (los del P&L)', fmt=motor.FMT_EUR0,
                formulas=dict(
                    [(col, '=' + pyg.r('tcf')) for col in cols]
                    + [('E', '="Los costes fijos no cambian con el escenario: '
                        'por eso son fijos"')]))
        rej.add('rai', rot='RESULTADO ANTES DE IMPUESTOS', bold=True,
                fmt=motor.FMT_EUR0,
                formulas=dict(
                    (col, (lambda R, c=col: '=' + R.c('mb', c) + '-'
                           + R.c('cf', c))) for col in cols))
        rej.add('is', rot='Impuesto de Sociedades', fmt=motor.FMT_EUR0,
                formulas=dict(
                    [(col, (lambda R, c=col: '=MAX(0,' + R.c('rai', c) + '-'
                            + P('bin_inicial') + ')*' + P('is_nueva')))
                     for col in cols]
                    + [('E', '="Al tipo de entidad de nueva creación, '
                        'compensando las bases negativas anteriores"')]))
        rej.add('neto', rot='RESULTADO NETO', bold=True, fmt=motor.FMT_EUR0,
                formulas=dict(
                    (col, (lambda R, c=col: '=' + R.c('rai', c) + '-'
                           + R.c('is', c))) for col in cols))
        rej.add('be', rot='Cubiertos/día para el equilibrio',
                fmt=motor.FMT_DEC,
                formulas=dict(
                    (col, (lambda R, c=col: '=IF(' + R.c('ticket', c) + '-'
                           + R.c('tcv', c) + '/(' + R.c('cub', c) + '*'
                           + R.c('dias', c) + ')<=0,"",' + R.c('cf', c) + '/('
                           + R.c('ticket', c) + '-' + R.c('tcv', c) + '/('
                           + R.c('cub', c) + '*' + R.c('dias', c) + '))/'
                           + R.c('dias', c) + ')')) for col in cols))
        self.pendientes.append(rej)
        fila = rej.ultima + 2
        motor.val(ws, 'A' + str(fila),
                  'La columna «Realista» lee sus tres datos de la hoja de '
                  'Supuestos, así que reproduce EXACTAMENTE el año 1 del P&L. '
                  'Los otros dos escenarios usan las mismas tasas de coste: '
                  'lo único que cambia son los cubiertos, el ticket y los '
                  'días.', wrap=True)
        ws.row_dimensions[fila].height = 44
        for i, texto in enumerate(pie):
            motor.val(ws, 'A' + str(fila + 1 + i), texto)
        motor.anchos(ws, {'A': 40, 'B': 16, 'C': 16, 'D': 16, 'E': 52})
        motor.print_setup(ws, header_row=cab)
        return rej

    def _leer_escenarios(self, ws, cab):
        """Cubiertos/ticket/días de los escenarios extremos del fichero."""
        propios = self.dato('ESCENARIOS') or {}
        fuera = {'pesimista': [None, None, None],
                 'optimista': [None, None, None]}
        patrones = ((r'^(clientes|cubiertos)', 0), (r'^ticket', 1),
                    (r'd[ií]as', 2))
        for r in range(cab + 1, ws.max_row + 1):
            rot = motor._rotulo_de_fila(ws, r, max_col=1)
            if not rot:
                continue
            for patron, idx in patrones:
                if re.search(patron, rot, re.I):
                    fuera['pesimista'][idx] = _num(ws['B' + str(r)].value)
                    fuera['optimista'][idx] = _num(ws['D' + str(r)].value)
        base = [self.p.valor('cubiertos_dia'), self.p.valor('ticket_medio'),
                self.p.valor('dias_apertura')]
        for clave, factor in (('pesimista', 0.72), ('optimista', 1.25)):
            if clave in propios:
                fuera[clave] = list(propios[clave])
            for i in range(3):
                if fuera[clave][i] is None:
                    ref_ = _num(base[i], 0) or 0
                    fuera[clave][i] = round(ref_ * (factor if i < 2 else 1), 2)
        return fuera

    # -- §2.7 -------------------------------------------------------------
    def tesoreria(self):
        """`Tesorería 12 meses`: en qué mes se agota la caja (§2.7)."""
        ws = self.ws_tesoreria
        _limpiar_area(ws, 1, max(ws.max_row, 60), 15)
        motor.val(ws, 'A1', 'PREVISIÓN DE TESORERÍA — AÑO 1', bold=True)
        motor.val(ws, 'A2', 'El P&L dice si el negocio gana dinero; esta hoja '
                  'dice si le queda caja para llegar a fin de mes. Es la '
                  'primera que mira un banco.', wrap=True)
        cab = 4
        motor.val(ws, 'A' + str(cab), 'Concepto', bold=True)
        # el «(€)» de la cabecera no es adorno: sin él, `motor` lee «Mes» como
        # recuento y borra el formato de euro de las doce columnas
        meses = tuple('Mes ' + str(i) + ' (€)' for i in range(1, 13))
        cols = [get_column_letter(2 + i) for i in range(12)]
        for i, nombre in enumerate(meses):
            motor.val(ws, cols[i] + str(cab), nombre, bold=True)
        motor.val(ws, 'N' + str(cab), 'Año (€)', bold=True)
        rej = Rejilla(ws, cab + 1)
        self.rej['tesoreria'] = rej
        pyg = self.rej['pyg']
        inv = self.rej['inversion']
        fin = self.rej['financiacion']
        P = self.p.ref
        estacion = list(self.dato('ESTACIONALIDAD') or ([1.0 / 12] * 12))

        def por_meses(clave, rot, ref_anual, nota=None, signo='', fmt=None):
            formulas = dict(
                (cols[i], (lambda R, c=cols[i], k=clave:
                           '=' + signo + ref_anual + '*' + R.c('peso', c)))
                for i in range(12))
            formulas['N'] = (lambda R, k=clave: '=SUM(' + R.c(k, cols[0])
                             + ':' + R.c(k, cols[11]) + ')')
            rej.add(clave, rot=rot, fmt=fmt or motor.FMT_EUR0,
                    formulas=formulas, valores={'O': nota} if nota else None)

        rej.add('peso', rot='Reparto de la actividad por mes',
                fmt=motor.FMT_PCT, verde=True,
                valores=dict((cols[i], round(estacion[i], 4))
                             for i in range(12)),
                formulas={'N': (lambda R: '=SUM(' + R.c('peso', cols[0]) + ':'
                                + R.c('peso', cols[11]) + ')')})
        motor.semaforo_num(ws, rej.c('peso', 'N') + ':' + rej.c('peso', 'N'),
                           verde_si=rej.c('peso', 'N') + '=1',
                           rojo_si=rej.c('peso', 'N') + '<>1')
        rej.add(rot='COBROS', bold=True)
        por_meses('cobros', 'Ventas cobradas (con IVA repercutido)',
                  '(' + pyg.r('ingresos') + '+' + pyg.r('ingresos') + '*('
                  + P('pct_comida') + '*' + P('iva_reducido') + '+'
                  + P('pct_bebida') + '*' + P('iva_general') + '))')
        rej.add(rot='PAGOS', bold=True)
        por_meses('p_comida', 'Compras de comida (IVA incluido)',
                  pyg.r('cv_comida') + '*(1+' + P('iva_reducido') + ')',
                  signo='-')
        por_meses('p_bebida', 'Compras de bebida (IVA incluido)',
                  pyg.r('cv_bebida') + '*(1+' + P('iva_general') + ')',
                  signo='-')
        por_meses('p_otros', 'Otros pagos de explotación (IVA incluido)',
                  '(' + pyg.r('tcv') + '-' + pyg.r('cv_comida') + '-'
                  + pyg.r('cv_bebida') + '+' + pyg.r('tcf') + '-'
                  + pyg.r('cf_personal') + '-' + pyg.r('cf_amort') + '-'
                  + pyg.r('cf_int') + ')*(1+' + P('iva_soportado') + ')',
                  signo='-')
        por_meses('p_personal', 'Nóminas y Seguridad Social',
                  pyg.r('cf_personal'), signo='-')
        por_meses('p_int', 'Intereses del préstamo', fin.r('int_1'),
                  signo='-')
        por_meses('p_principal', 'Devolución de principal del préstamo',
                  fin.r('cap_1'), signo='-')
        # liquidación trimestral de IVA
        formulas = {}
        for i in range(12):
            if i + 1 in (4, 7, 10):
                a, b = i - 3, i - 1
                formulas[cols[i]] = (
                    lambda R, a=a, b=b: '=-MAX(0,SUM(' + R.c('iva_rep', cols[a])
                    + ':' + R.c('iva_rep', cols[b]) + ')-SUM('
                    + R.c('iva_sop', cols[a]) + ':' + R.c('iva_sop', cols[b])
                    + '))')
            else:
                formulas[cols[i]] = '=0'
        formulas['N'] = (lambda R: '=SUM(' + R.c('iva_liq', cols[0]) + ':'
                         + R.c('iva_liq', cols[11]) + ')')
        rej.add('iva_rep', rot='IVA repercutido del mes (memoria)',
                fmt=motor.FMT_EUR0,
                formulas=dict(
                    [(cols[i], (lambda R, c=cols[i]: '=' + pyg.r('ingresos')
                                + '*' + R.c('peso', c) + '*(' + P('pct_comida')
                                + '*' + P('iva_reducido') + '+'
                                + P('pct_bebida') + '*' + P('iva_general')
                                + ')')) for i in range(12)]
                    + [('N', (lambda R: '=SUM(' + R.c('iva_rep', cols[0]) + ':'
                              + R.c('iva_rep', cols[11]) + ')'))]))
        rej.add('iva_sop', rot='IVA soportado del mes (memoria)',
                fmt=motor.FMT_EUR0,
                formulas=dict(
                    [(cols[i], (lambda R, c=cols[i]:
                                '=(' + pyg.r('cv_comida') + '*'
                                + P('iva_reducido') + '+' + pyg.r('cv_bebida')
                                + '*' + P('iva_general') + '+(' + pyg.r('tcv')
                                + '-' + pyg.r('cv_comida') + '-'
                                + pyg.r('cv_bebida') + '+' + pyg.r('tcf')
                                + '-' + pyg.r('cf_personal') + '-'
                                + pyg.r('cf_amort') + '-' + pyg.r('cf_int')
                                + ')*' + P('iva_soportado') + ')*'
                                + R.c('peso', c))) for i in range(12)]
                    + [('N', (lambda R: '=SUM(' + R.c('iva_sop', cols[0]) + ':'
                              + R.c('iva_sop', cols[11]) + ')'))]))
        rej.add('iva_liq', rot='Liquidación trimestral de IVA (modelo 303)',
                fmt=motor.FMT_EUR0, formulas=formulas)
        rej.add('flujo', rot='FLUJO DEL MES', bold=True, fmt=motor.FMT_EUR0,
                formulas=dict(
                    [(cols[i], (lambda R, c=cols[i]: '=SUM(' + R.c('cobros', c)
                                + ':' + R.c('p_principal', c) + ')+'
                                + R.c('iva_liq', c))) for i in range(12)]
                    + [('N', (lambda R: '=SUM(' + R.c('flujo', cols[0]) + ':'
                              + R.c('flujo', cols[11]) + ')'))]))
        rej.add('saldo', rot='SALDO ACUMULADO DE CAJA', bold=True,
                fmt=motor.FMT_EUR0,
                formulas=dict(
                    [(cols[0], (lambda R: '=' + inv.r('fondo') + '+'
                                + R.c('flujo', cols[0])))]
                    + [(cols[i], (lambda R, c=cols[i], p=cols[i - 1]:
                                  '=' + R.c('saldo', p) + '+'
                                  + R.c('flujo', c))) for i in range(1, 12)]))
        motor.semaforo_num(ws, rej.c('saldo', cols[0]) + ':'
                           + rej.c('saldo', cols[11]),
                           verde_si=rej.c('saldo', cols[0]) + '>0',
                           rojo_si=rej.c('saldo', cols[0]) + '<0')
        # `MIN` sobre doce celdas vacías devuelve 0, y un 0 aquí pinta el
        # semáforo de VERDE en un libro sin datos: hay que preguntar antes si
        # hay algún número que comparar
        rej.add('minimo', rot='Saldo mínimo del año', fmt=motor.FMT_EUR0,
                formulas={'B': (lambda R: '=IF(COUNT(' + R.c('saldo', cols[0])
                                + ':' + R.c('saldo', cols[11]) + ')=0,"",MIN('
                                + R.c('saldo', cols[0]) + ':'
                                + R.c('saldo', cols[11]) + '))'),
                          'D': '="Si es negativo, sube el fondo de maniobra o '
                               'el préstamo: te quedas sin caja"'})
        motor.semaforo_num(ws, rej.c('minimo') + ':' + rej.c('minimo'),
                           verde_si=rej.c('minimo') + '>=0',
                           rojo_si=rej.c('minimo') + '<0')
        # payback ÚNICO del proyecto (DOM-17)
        rej.add(rot='RETORNO DE LA INVERSIÓN', bold=True)
        for i, clave in enumerate(('fcf_1', 'fcf_2', 'fcf_3')):
            col = ('B', 'C', 'D')[i]
            rej.add(clave, rot='Flujo de caja libre del año ' + str(i + 1),
                    fmt=motor.FMT_EUR0,
                    formulas={'B': '=' + pyg.r('neto', col) + '+'
                              + pyg.r('cf_amort', col)})
        rej.add('inv_recup', rot='Inversión a recuperar', fmt=motor.FMT_EUR0,
                formulas={
                    'B': '=' + inv.r('total') + '-' + inv.r('fondo'),
                    'D': '="La inversión SIN el fondo de maniobra (que se '
                         'recupera al cerrar) ni el IVA soportado (que '
                         'devuelve Hacienda): es lo que de verdad hay que '
                         'amortizar con el negocio"'})
        rej.add('payback', rot='Payback del proyecto (años)',
                fmt=motor.FMT_DEC, bold=True,
                formulas={
                    'B': (lambda R: '=IF(' + R.c('fcf_1') + '>='
                          + R.c('inv_recup') + ',' + R.c('inv_recup') + '/'
                          + R.c('fcf_1') + ',IF(' + R.c('fcf_1') + '+'
                          + R.c('fcf_2') + '>=' + R.c('inv_recup') + ',1+('
                          + R.c('inv_recup') + '-' + R.c('fcf_1') + ')/'
                          + R.c('fcf_2') + ',IF(' + R.c('fcf_1') + '+'
                          + R.c('fcf_2') + '+' + R.c('fcf_3') + '>='
                          + R.c('inv_recup') + ',2+(' + R.c('inv_recup') + '-'
                          + R.c('fcf_1') + '-' + R.c('fcf_2') + ')/'
                          + R.c('fcf_3') + ',"Más de 3 años")))'),
                    'D': '="ÚNICO payback del pack: inversión a recuperar '
                         'entre el flujo de caja libre de los tres años. El '
                         'Word cita esta celda, no recalcula"'})
        self.pendientes.append(rej)
        fila = rej.ultima + 2
        motor.val(ws, 'A' + str(fila),
                  'El IVA del cuarto trimestre se liquida en enero del año '
                  'siguiente, así que no aparece en este cuadro. El Impuesto '
                  'de Sociedades del año 1 se paga en julio del año 2. La '
                  'cuota del préstamo se reparte en doce partes iguales '
                  'siguiendo el cuadro ANUAL de la hoja de Financiación.',
                  wrap=True)
        ws.row_dimensions[fila].height = 44
        motor.anchos(ws, dict([('A', 44)] + [(c, 12) for c in cols]
                              + [('N', 14)]))
        motor.print_setup(ws, header_row=cab, landscape=True,
                          congelar='B' + str(cab + 1))
        return rej

    # -- §2.8 -------------------------------------------------------------
    def financiacion(self):
        """`Financiación`: usos y orígenes + cuadro francés (§2.8)."""
        ws = self.ws_financiacion
        _limpiar_area(ws, 1, max(ws.max_row, 60), 8)
        motor.val(ws, 'A1', 'PLAN DE FINANCIACIÓN', bold=True)
        motor.val(ws, 'A2', 'Qué hace falta, de dónde sale y cuánto cuesta '
                  'devolverlo. Es la hoja que el banco pide junto con el P&L.',
                  wrap=True)
        cab = 4
        for i, texto in enumerate(('Concepto', 'Importe', 'Notas')):
            motor.val(ws, get_column_letter(i + 1) + str(cab), texto,
                      bold=True)
        rej = Rejilla(ws, cab + 1)
        self.rej['financiacion'] = rej
        P = self.p.ref
        rej.add(rot='ORIGEN DE FONDOS', bold=True)
        rej.add('propios', rot='Recursos propios de los socios',
                fmt=motor.FMT_EUR0, formulas={'B': '=' + P('recursos_propios')})
        rej.add('prestamo', rot='Préstamo bancario', fmt=motor.FMT_EUR0,
                formulas={'B': '=' + P('prestamo')})
        for clave, rot, nota in (
                ('ico', 'Línea ICO (avalada por el ICO, la concede tu banco)',
                 'Consulta las líneas del ejercicio en curso en ico.es'),
                ('enisa', 'Préstamo participativo ENISA',
                 'Para sociedades; sin garantías personales'),
                ('angeles', 'Business angels o socios inversores',
                 'Entra en el capital: diluye, no se devuelve'),
                ('subvencion', 'Subvenciones autonómicas o locales',
                 'Suelen cobrarse DESPUÉS de justificar el gasto')):
            rej.add(clave, rot=rot, fmt=motor.FMT_EUR0, verde=True,
                    valores={'B': 0, 'C': nota})
        rej.add('origen', rot='TOTAL ORIGEN DE FONDOS', bold=True,
                fmt=motor.FMT_EUR0,
                formulas={'B': (lambda R: '=SUM(' + R.c('propios') + ':'
                                + R.c('subvencion') + ')')})
        rej.add(rot='USOS', bold=True)
        rej.add('usos', rot='Necesidad total de caja al arranque',
                fmt=motor.FMT_EUR0,
                formulas={'B': '=' + self.rej['inversion'].r('caja'),
                          'C': '="Inversión más el IVA que hay que adelantar"'})
        rej.add('dif', rot='Diferencia (origen − usos)', bold=True,
                fmt=motor.FMT_EUR0,
                formulas={'B': (lambda R: '=' + R.c('origen') + '-'
                                + R.c('usos')),
                          'C': '="En rojo significa que el plan no está '
                               'financiado: sube los recursos propios o el '
                               'préstamo"'})
        motor.semaforo_num(ws, rej.c('dif') + ':' + rej.c('dif'),
                           verde_si=rej.c('dif') + '>=0',
                           rojo_si=rej.c('dif') + '<0')
        rej.add(rot='CONDICIONES DEL PRÉSTAMO', bold=True)
        # sin préstamo declarado el cuadro entero se apaga: un «0 €» de
        # capital pendiente al vencimiento pintaría de verde un libro vacío
        rej.add('importe', rot='Importe del principal', fmt=motor.FMT_EUR0,
                formulas={'B': '=IF(' + P('prestamo') + '=0,"",'
                          + P('prestamo') + ')'})
        rej.add('tipo', rot='Tipo de interés nominal anual',
                fmt=motor.FMT_PCT, formulas={'B': '=' + P('tipo_prestamo')})
        rej.add('plazo', rot='Plazo total (años)', fmt=motor.FMT_ENT,
                formulas={'B': '=' + P('plazo_prestamo')})
        rej.add('carencia', rot='Carencia de principal aplicada (años)',
                fmt=motor.FMT_ENT,
                formulas={'B': '=IF(' + P('carencia_prestamo') + '>='
                          + P('plazo_prestamo') + ',0,'
                          + P('carencia_prestamo') + ')',
                          'C': '="Una carencia igual o mayor que el plazo no '
                               'existe: la hoja la anula en origen"'})
        rej.add('cuota', rot='Cuota anual durante la amortización',
                fmt=motor.FMT_EUR, bold=True,
                formulas={'B': (lambda R: '=IF(' + R.c('plazo') + '-'
                                + R.c('carencia') + '<=0,"",' + R.c('importe')
                                + '*' + R.c('tipo') + '/(1-(1+' + R.c('tipo')
                                + ')^-(' + R.c('plazo') + '-'
                                + R.c('carencia') + ')))'),
                          'C': '="Sistema francés, anualidad algebraica. Tu '
                               'banco te dará el desglose mensual"'})
        rej.add(rot='CUADRO DE AMORTIZACIÓN', bold=True)
        rej.add('cab_cuadro', rot='Año', bold=True,
                valores={'B': 'Capital pendiente', 'C': 'Intereses',
                         'D': 'Amortización de principal', 'E': 'Cuota total',
                         'F': 'Capital al cierre'})
        plazo_max = 10
        for i in range(1, plazo_max + 1):
            clave = 'y_%d' % i
            anterior = 'y_%d' % (i - 1)
            rej.add(clave, valores={'A': i}, fmt=motor.FMT_EUR,
                    fmt_A=motor.FMT_ENT,
                    formulas={
                        # pasada la última anualidad el cuadro se APAGA
                        # entero (decisión 14): sin el guarda del plazo, la
                        # fila del año 8 imprimía «0 €» de capital pendiente
                        # en un préstamo a 7 años
                        'B': ((lambda R: '=' + R.c('importe')) if i == 1 else
                              (lambda R, a=anterior, n=i: '=IF(OR(' + str(n)
                               + '>' + R.c('plazo') + ',' + R.c(a, 'F')
                               + '=""),"",' + R.c(a, 'F') + ')')),
                        'C': (lambda R, k=clave, n=i: '=IF(OR(' + str(n) + '>'
                              + R.c('plazo') + ',' + R.c(k) + '=""),"",'
                              + R.c(k) + '*' + R.c('tipo') + ')'),
                        'D': (lambda R, k=clave, n=i: '=IF(OR(' + str(n) + '>'
                              + R.c('plazo') + ',' + R.c(k) + '=""),"",IF('
                              + str(n) + '<=' + R.c('carencia') + ',0,MIN('
                              + R.c(k) + ',' + R.c('cuota') + '-' + R.c(k, 'C')
                              + ')))'),
                        'E': (lambda R, k=clave: '=IF(' + R.c(k, 'C')
                              + '="","",' + R.c(k, 'C') + '+' + R.c(k, 'D')
                              + ')'),
                        'F': (lambda R, k=clave: '=IF(' + R.c(k, 'D')
                              + '="","",' + R.c(k) + '-' + R.c(k, 'D') + ')')})
        rej.add('cierre', rot='Capital pendiente al vencimiento',
                fmt=motor.FMT_EUR,
                formulas={'B': (lambda R: '=IF(' + R.c('importe')
                                + '="","",IF(' + R.c('y_%d' % plazo_max, 'F')
                                + '="",0,' + R.c('y_%d' % plazo_max, 'F')
                                + '))'),
                          'C': '="Tiene que ser cero: si no, el cuadro no '
                               'cierra"'})
        motor.semaforo_num(ws, rej.c('cierre') + ':' + rej.c('cierre'),
                           verde_si=rej.c('cierre') + '<=0.5',
                           rojo_si=rej.c('cierre') + '>0.5')
        # las tres celdas que lee el P&L y la tesorería
        for i in (1, 2, 3):
            rej.add('int_%d' % i, rot='Intereses del año ' + str(i),
                    fmt=motor.FMT_EUR0,
                    formulas={'B': (lambda R, n=i: '=IF(' + R.c('y_%d' % n, 'C')
                                    + '="",0,' + R.c('y_%d' % n, 'C') + ')')})
            rej.add('cap_%d' % i, rot='Devolución de principal del año '
                    + str(i), fmt=motor.FMT_EUR0,
                    formulas={'B': (lambda R, n=i: '=IF(' + R.c('y_%d' % n, 'D')
                                    + '="",0,' + R.c('y_%d' % n, 'D') + ')')})
        rej.add(rot='COBERTURA DEL SERVICIO DE LA DEUDA (DSCR)', bold=True)
        pyg = self.rej['pyg']
        for i, col in enumerate(('B', 'C', 'D'), start=1):
            rej.add('dscr_%d' % i, rot='DSCR del año ' + str(i),
                    fmt=motor.FMT_DEC2,
                    formulas={'B': (lambda R, n=i, c=col:
                                    '=(' + pyg.r('rai', c) + '+'
                                    + pyg.r('cf_amort', c) + '+'
                                    + R.c('int_%d' % n) + ')/('
                                    + R.c('int_%d' % n) + '+'
                                    + R.c('cap_%d' % n) + ')')})
            motor.semaforo_num(ws, rej.c('dscr_%d' % i) + ':'
                               + rej.c('dscr_%d' % i),
                               verde_si=rej.c('dscr_%d' % i) + '>=1.25',
                               ambar_si=rej.c('dscr_%d' % i) + '>=1',
                               rojo_si=rej.c('dscr_%d' % i) + '<1')
        self.pendientes.append(rej)
        fila = rej.ultima + 2
        motor.val(ws, 'A' + str(fila),
                  'El DSCR se calcula ANTES de la deuda: al resultado antes '
                  'de impuestos se le devuelven la amortización contable y '
                  'los intereses, y el resultado se divide entre lo que hay '
                  'que pagar ese año. Por debajo de 1 el negocio no genera '
                  'para pagar el préstamo.', wrap=True)
        ws.row_dimensions[fila].height = 44
        motor.anchos(ws, {'A': 44, 'B': 18, 'C': 16, 'D': 22, 'E': 16,
                          'F': 18})
        motor.print_setup(ws, header_row=cab)
        return rej

    # -- §2.9 -------------------------------------------------------------
    def instrucciones(self):
        """`Instrucciones`: textos ciertos y ratios que auditan (§2.9)."""
        ws = self.ws_ins
        col = motor._col_texto(ws)
        letra = get_column_letter(col)
        # se limpia sólo el cuerpo: `motor.cierre_instrucciones()` reescribe
        # después su bloque (desproteger + cross-sell + bio + versión)
        _limpiar_area(ws, 1, ws.max_row, col + 4)
        motor.val(ws, letra + '1', 'INSTRUCCIONES DE USO — Plan financiero '
                  + str(self.concepto), bold=True)
        fila = 3
        pyg = self.rej['pyg']
        inv = self.rej['inversion']
        eq = self.rej['equilibrio']
        lineas = [
            'CÓMO SE USA ESTE LIBRO',
            'Este plan financiero es un MODELO: sólo se teclea en las celdas '
            'VERDES y el resto se recalcula solo.',
            '1. «0. Supuestos» es la hoja de mando: cubiertos, ticket sin '
            'IVA, días de apertura, mezcla de comida y bebida, coste de '
            'mercancía, alquiler, financiación e impuestos.',
            '2. Las partidas de la inversión, los costes fijos y la plantilla '
            'se teclean en su propia hoja, también en verde. Ningún número se '
            'escribe dos veces.',
            '3. El punto de equilibrio, los escenarios, la tesorería y el '
            'cuadro del préstamo se derivan de lo anterior: no hay que '
            'tocarlos.',
            '4. Todas las cifras van SIN IVA. Para pasar un PVP a precio sin '
            'IVA, divide entre 1,10 en comida y entre 1,21 en bebida '
            'alcohólica; el IVA de la inversión se adelanta y se recupera con '
            'el modelo 303.',
            '5. Si cambias la plantilla, el P&L la lee sola: el coste de '
            'personal sale de la hoja «Personal», no de una estimación '
            'aparte.',
        ]
        for texto in (self.dato('INSTRUCCIONES', {}) or {}).get('uso', []):
            lineas.append(texto)
        for texto in lineas:
            motor.val(ws, letra + str(fila), texto, wrap=True,
                      bold=texto.isupper())
            fila += 1
        fila += 1
        motor.val(ws, letra + str(fila), 'RATIOS QUE AUDITA EL LIBRO',
                  bold=True)
        fila += 1
        motor.val(ws, letra + str(fila),
                  'Los umbrales viven en la columna «Umbral» del bloque '
                  'RATIOS CLAVE del P&L: cámbialos ahí y el semáforo cambia '
                  'con ellos.', wrap=True)
        fila += 2
        cabecera = fila
        for i, texto in enumerate(('Ratio', 'Valor del año 1', 'Umbral',
                                   'Estado')):
            motor.val(ws, get_column_letter(col + i) + str(fila), texto,
                      bold=True)
        fila += 1
        for clave, rot in (('r_cogs', 'Coste de mercancía / Ventas'),
                           ('r_personal', 'Coste de personal / Ventas'),
                           ('r_alquiler', 'Alquiler / Ventas'),
                           ('r_neto', 'Resultado neto / Ventas'),
                           ('r_mb', 'Margen bruto / Ventas')):
            motor.val(ws, letra + str(fila), rot)
            fx(ws, get_column_letter(col + 1) + str(fila),
               '=' + pyg.r(clave), motor.FMT_PCT)
            fx(ws, get_column_letter(col + 2) + str(fila),
               '=' + pyg.r(clave, 'E'), motor.FMT_PCT)
            menor = clave in ('r_cogs', 'r_personal', 'r_alquiler')
            c1 = get_column_letter(col + 1) + str(fila)
            c2 = get_column_letter(col + 2) + str(fila)
            fx(ws, get_column_letter(col + 3) + str(fila),
               '=IF(OR(' + c1 + '="",' + c2 + '=""),"",IF(' + c1
               + ('<=' if menor else '>=') + c2 + ',"CUMPLE","REVISAR"))')
            fila += 1
        motor.semaforo_texto(
            ws, get_column_letter(col + 3) + str(cabecera + 1) + ':'
            + get_column_letter(col + 3) + str(fila - 1),
            (('CUMPLE', motor.CF_VERDE_BG, motor.CF_VERDE_FG),
             ('REVISAR', motor.CF_ROJO_BG, motor.CF_ROJO_FG)))
        fila += 1
        motor.val(ws, letra + str(fila), 'CIFRAS DE ESTE PLAN', bold=True)
        fila += 1
        for rot, formula, fmt in (
                ('Inversión total (suma de los bloques)',
                 '=' + inv.r('total'), motor.FMT_EUR0),
                ('Necesidad total de caja al arranque',
                 '=' + inv.r('caja'), motor.FMT_EUR0),
                ('Fondo de maniobra dotado', '=' + inv.r('fondo'),
                 motor.FMT_EUR0),
                ('Facturación prevista del año 1', '=' + pyg.r('ingresos'),
                 motor.FMT_EUR0),
                ('Resultado neto del año 1', '=' + pyg.r('neto'),
                 motor.FMT_EUR0),
                ('Cubiertos/día para el punto de equilibrio',
                 '=' + eq.r('cub_dia'), motor.FMT_DEC),
                ('Payback del proyecto (años)',
                 '=' + self.rej['tesoreria'].r('payback'), motor.FMT_DEC)):
            motor.val(ws, letra + str(fila), rot)
            fx(ws, get_column_letter(col + 1) + str(fila), formula, fmt)
            fila += 1
        fila += 1
        motor.val(ws, letra + str(fila),
                  'DATOS DE REFERENCIA DEL SECTOR', bold=True)
        fila += 1
        for rot, valor, nota in (self.dato('INSTRUCCIONES', {}) or {}).get(
                'referencias', []):
            motor.val(ws, letra + str(fila), rot)
            motor.val(ws, get_column_letter(col + 1) + str(fila), valor)
            motor.val(ws, get_column_letter(col + 2) + str(fila), nota)
            fila += 1
        motor.anchos(ws, {letra: 62,
                          get_column_letter(col + 1): 18,
                          get_column_letter(col + 2): 16,
                          get_column_letter(col + 3): 14})
        motor.print_setup(ws)
        return fila

    # -- §2.10 ------------------------------------------------------------
    def checklist(self, ws_libro):
        """Checklist de apertura: legal vigente y sin inventos (§2.10)."""
        reglas = self.dato('CHECKLIST', {}) or {}
        reemplazos = reglas.get('reemplazos', [])
        altas = reglas.get('altas', [])
        suprimir = [motor.norm(s) for s in reglas.get('suprimir', [])]
        fases = reglas.get('fases', {})
        tocados, anadidos = 0, 0
        for ws in ws_libro.worksheets:
            if motor.norm(ws.title) in motor.HOJAS_MOTOR:
                continue
            cab = _cabecera(ws)
            cols = dict((motor.norm(c.value), c.column) for c in ws[cab]
                        if isinstance(c.value, str))
            col_tarea = (cols.get('tramite / tarea') or cols.get('tarea')
                         or cols.get('tramite / accion') or cols.get('hito'))
            if col_tarea is None:
                continue
            # (a) reemplazos de contenido, celda a celda
            for r in range(1, ws.max_row + 1):
                for c in range(1, ws.max_column + 1):
                    cel = ws.cell(row=r, column=c)
                    if not isinstance(cel.value, str):
                        continue
                    for patron, nuevo in reemplazos:
                        if re.search(patron, cel.value, re.I):
                            if cel.value != nuevo:
                                self.anota(ws.title + '!' + cel.coordinate
                                           + ': «' + cel.value[:48]
                                           + '» → «' + nuevo[:48] + '»')
                                cel.value = nuevo
                                tocados += 1
                            break
            # (b) cabeceras de fase con el cronograma ÚNICO (DOM-23)
            for r in range(1, ws.max_row + 1):
                v = ws.cell(row=r, column=1).value
                if not isinstance(v, str):
                    continue
                for patron, nuevo in fases.items():
                    if re.search(patron, v, re.I) and v != nuevo:
                        self.anota(ws.title + '!A' + str(r) + ': cronograma «'
                                   + v[:44] + '» → «' + nuevo[:44] + '»')
                        ws.cell(row=r, column=1).value = nuevo
                        tocados += 1
            # (c) filas suprimidas (duplicados y trámites que no aplican)
            if suprimir:
                for r in range(cab + 1, ws.max_row + 1):
                    v = ws.cell(row=r, column=col_tarea).value
                    if isinstance(v, str) and motor.norm(v) in suprimir:
                        for c in range(1, ws.max_column + 1):
                            ws.cell(row=r, column=c).value = None
                        tocados += 1
                        self.anota(ws.title + ': fila ' + str(r)
                                   + ' suprimida — ' + v[:60])
            # (d) altas al final de su fase
            destino = altas if len(ws_libro.worksheets) <= 2 else [
                a for a in altas if re.search(a[0], ws.title, re.I)]
            if destino:
                anadidos += self._altas_checklist(
                    ws, cab, col_tarea, destino,
                    cabecera=reglas.get('cabecera_altas'))
        self.anota('Checklist: ' + str(tocados) + ' celdas corregidas y '
                   + str(anadidos) + ' trámites nuevos (§2.10)')
        return tocados, anadidos

    def _altas_checklist(self, ws, cab, col_tarea, altas, cabecera=None):
        """Añade trámites conservando la estructura de fases del fichero.

        IDEMPOTENTE por CONTENIDO: los que ya están no se vuelven a añadir. Sin
        esto la 2.ª pasada duplicaba los diez trámites nuevos y el contador del
        checklist pasaba de 59 a 69 sin que nadie lo hubiera pedido.
        """
        existentes = set()
        for r in range(cab + 1, ws.max_row + 1):
            v = ws.cell(row=r, column=col_tarea).value
            if isinstance(v, str) and v.strip():
                existentes.add(motor.norm(v))
        altas = [a for a in altas if motor.norm(a[2]) not in existentes]
        if not altas:
            return 0
        # última fila con contenido en la columna de tarea
        ultima = cab
        for r in range(cab + 1, ws.max_row + 1):
            if isinstance(ws.cell(row=r, column=col_tarea).value, str) \
                    and ws.cell(row=r, column=col_tarea).value.strip():
                ultima = r
        pie = []
        for r in range(ultima + 1, ws.max_row + 1):
            fila = [(c, ws.cell(row=r, column=c).value)
                    for c in range(1, ws.max_column + 1)
                    if ws.cell(row=r, column=c).value is not None]
            if fila:
                pie.append((r, fila, _ancho_combinado(ws, r)))
        # el pie va COMBINADO a lo ancho de la tabla: si se mueve sin
        # deshacer la combinación, `MergedCell.value` es de sólo lectura y la
        # escritura revienta con AttributeError
        for r, fila, _ancho in pie:
            for m in list(ws.merged_cells.ranges):
                cr = CellRange(str(m))
                if cr.min_row <= r <= cr.max_row:
                    ws.unmerge_cells(str(m))
            for c, _v in fila:
                ws.cell(row=r, column=c).value = None
        cols = dict((motor.norm(c.value), c.column) for c in ws[cab]
                    if isinstance(c.value, str))
        fila = ultima + 1
        n = 0
        usa_fase = 'fase' in cols
        if cabecera and altas:
            motor.val(ws, 'A' + str(fila), cabecera, bold=True)
            ws.merge_cells(start_row=fila, start_column=1, end_row=fila,
                           end_column=ws.max_column)
            fila += 1
        for _hoja, fase, tarea, responsable, plazo, nota in altas:
            valores = {col_tarea: tarea}
            if usa_fase:
                valores[cols['fase']] = fase
            if 'responsable' in cols:
                valores[cols['responsable']] = responsable
            if 'plazo' in cols:
                valores[cols['plazo']] = plazo
            if 'notas' in cols:
                valores[cols['notas']] = nota
            for c, v in valores.items():
                motor.val(ws, get_column_letter(c) + str(fila), v, wrap=True)
            fila += 1
            n += 1
        fila += 1
        for _r, contenido, ancho in pie:
            for c, v in contenido:
                motor.val(ws, get_column_letter(c) + str(fila), v)
            if ancho > 1:
                ws.merge_cells(start_row=fila, start_column=1, end_row=fila,
                               end_column=ancho)
            fila += 1
        # el resaltado de fila del molde C1 se reancla al cuerpo nuevo
        for cf in list(ws.conditional_formatting):
            reglas = list(cf.rules)
            if not reglas or reglas[0].type != 'expression':
                continue
            _purgar_cf_area(ws, cab, ws.max_row)
            nuevo = ('A' + str(cab) + ':'
                     + get_column_letter(ws.max_column) + str(fila))
            ws.conditional_formatting.add(nuevo, reglas[0])
            break
        return n


# ==========================================================================
# Ganchos que consume `main.py`
# ==========================================================================
def ficheros(dets, contenido=None):
    """Los xlsx de línea A: el plan financiero y el checklist de apertura."""
    fuera = []
    for fname, det in (dets or {}).items():
        if det['tipo'] == 'plan_financiero' and det['molde'] in MOLDES:
            fuera.append(fname)
        elif det['tipo'] == 'checklist' and det['molde'] in ('C1', 'C2'):
            fuera.append(fname)
    return fuera


def post(wb, fname, det, pid, params, cambios, contenido, carpeta=None):
    """§2 completo, DESPUÉS del §1 transversal y ANTES del cierre del motor."""
    if det['tipo'] == 'checklist':
        plan = Plan(wb, det, pid, params, contenido, cambios)
        plan.checklist(wb)
        return
    if det['molde'] not in MOLDES:
        return
    plan = Plan(wb, det, pid, params, contenido, cambios)
    # ORDEN: los supuestos primero (todo cuelga de ellos) y las hojas nuevas
    # ANTES del P&L, porque el P&L lee los intereses de `Financiación` y el
    # fondo de maniobra sale de los costes fijos del P&L. Las rejillas se
    # construyen en dos fases (declarar y escribir), así que una hoja puede
    # citar coordenadas de otra que todavía no se ha volcado.
    plan.supuestos_altas()
    # ORDEN DE DECLARACIÓN: cada hoja cita coordenadas de las anteriores; las
    # citas «hacia atrás» (el P&L pide los intereses a Financiación, que
    # todavía no existe) van como función y se resuelven en el volcado final.
    plan.personal()
    plan.pyg()
    plan.inversion()
    plan.equilibrio()
    plan.escenarios()
    plan.financiacion()
    plan.tesoreria()
    for rej in plan.pendientes:
        escribir(rej)
    plan.instrucciones()          # cita celdas de todas las anteriores
    plan.supuestos_calculadas()   # necesita las coordenadas del P&L
    recalibrado = plan.dato('RECALIBRADO', []) or []
    for entrada in recalibrado:
        cambios.append('RECALIBRADO · ' + ' · '.join(str(x) for x in entrada))
    cambios.append('§2 aplicado sobre el molde ' + det['molde'] + ' de '
                   + fname)


# ==========================================================================
# Demostraciones §2.11 (bloqueantes)
# ==========================================================================
def _pycel(path):
    from pycel import ExcelCompiler
    return ExcelCompiler(filename=path)


def _ev(xl, ref_):
    import contextlib
    with open(os.devnull, 'w') as dn, contextlib.redirect_stderr(dn):
        try:
            return xl.evaluate(ref_)
        except Exception as e:                               # noqa: BLE001
            return 'ERR:' + type(e).__name__ + ':' + str(e)[:80]


def _clon(origen, destino, cambios):
    """Copia con los inputs cambiados: nunca se toca el entregable."""
    import openpyxl
    shutil.copy2(origen, destino)
    wb = openpyxl.load_workbook(destino)
    for hoja_, coord, valor in cambios:
        ws = motor.hoja(wb, hoja_, obligatoria=True)
        ws[coord] = valor
    wb.save(destino)
    return destino


def _pf(carpeta):
    for n in sorted(os.listdir(carpeta)):
        if n.startswith('plan-financiero') and n.endswith('.xlsx'):
            return os.path.join(carpeta, n)
    return None


def _mapa(path):
    """Coordenadas por rótulo, para que la demo no dependa de la posición."""
    import openpyxl
    wb = openpyxl.load_workbook(path)
    mapa = {}
    for ws in wb.worksheets:
        for r in range(1, ws.max_row + 1):
            rot = motor._rotulo_de_fila(ws, r, max_col=1)
            if rot:
                mapa.setdefault(motor.norm(ws.title), {}).setdefault(
                    motor.norm(rot), r)
    return wb, mapa


#: Cubiertos/día del ensayo de la demo 5. Con 65 el año 1 pierde, el año 2
#: gana menos de lo que arrastra en bases negativas y el año 3 tributa al tipo
#: reducido: las tres ramas del impuesto quedan demostradas de una vez.
DEMO5_CUBIERTOS = 65


def demos(carpeta, demos_dir, pid, origen=None):
    """Las 8 demostraciones de §2.11, evaluadas con pycel."""
    res = {'fallos': [], 'demostraciones_2_11': {}}
    path = _pf(carpeta)
    if path is None:
        return res
    os.makedirs(demos_dir, exist_ok=True)
    wb, mapa = _mapa(path)
    nombres = dict((motor.norm(ws.title), ws.title) for ws in wb.worksheets)

    def R(hoja_, rotulo, col='B'):
        clave = motor.norm(hoja_)
        fila = mapa.get(clave, {}).get(motor.norm(rotulo))
        if fila is None:
            return None
        return "'" + nombres[clave] + "'!" + col + str(fila)

    sup = [k for k in nombres if k.startswith('0. supuestos')]
    sup = nombres[sup[0]] if sup else motor.HOJA_SUPUESTOS
    pyg = [k for k in nombres if 'p&l' in k or k.startswith('pyg')]
    pyg = nombres[pyg[0]] if pyg else None
    eq = [k for k in nombres if 'equilibrio' in k]
    eq = nombres[eq[0]] if eq else None
    esc = [k for k in nombres if 'escenario' in k]
    esc = nombres[esc[0]] if esc else None
    tes = [k for k in nombres if 'tesorer' in k]
    tes = nombres[tes[0]] if tes else None
    fin = [k for k in nombres if 'financiaci' in k]
    fin = nombres[fin[0]] if fin else None
    per = [k for k in nombres if k.endswith('personal')]
    per = nombres[per[0]] if per else None
    inv = [k for k in nombres if 'inversi' in k]
    inv = nombres[inv[0]] if inv else None
    if not all((pyg, eq, esc, tes, fin, per, inv)):
        res['fallos'].append('grupo_a: faltan hojas en ' + path)
        return res

    celdas = {
        'cubiertos': R(sup, 'Cubiertos/día (media del año 1)'),
        'delivery': R(sup, 'Ventas por delivery sobre el total'),
        'plazo': R(sup, 'Plazo del préstamo (años)'),
        'carencia': R(sup, 'Carencia de principal (años)'),
        'ingresos': R(pyg, 'INGRESOS TOTALES (sin IVA)'),
        'rai': R(pyg, 'RESULTADO ANTES DE IMPUESTOS'),
        'neto': R(pyg, 'RESULTADO NETO'),
        'personal_pyg': R(pyg, 'Personal (nóminas + Seguridad Social)'),
        'personal_hoja': R(per, 'TOTAL PLANTILLA', 'F'),
        'r_personal': R(pyg, 'Coste de personal / Ventas'),
        'u_personal': R(pyg, 'Coste de personal / Ventas', 'E'),
        'deliv_pyg': R(pyg, 'Comisiones de delivery'),
        'is1': R(pyg, 'Impuesto de Sociedades'),
        'is2': R(pyg, 'Impuesto de Sociedades', 'C'),
        'is3': R(pyg, 'Impuesto de Sociedades', 'D'),
        'tipo3': R(pyg, 'Tipo de Impuesto de Sociedades aplicado', 'D'),
        'rai2': R(pyg, 'RESULTADO ANTES DE IMPUESTOS', 'C'),
        'bin_ini2': R(pyg, 'Bases negativas pendientes al inicio', 'C'),
        'be_dia': R(eq, 'Cubiertos necesarios al día'),
        'esc_rai': R(esc, 'RESULTADO ANTES DE IMPUESTOS', 'C'),
        'esc_neto': R(esc, 'RESULTADO NETO', 'C'),
        'saldo_min': R(tes, 'Saldo mínimo del año'),
        'fondo': R(inv, 'Colchón operativo hasta alcanzar el equilibrio'),
        'cierre': R(fin, 'Capital pendiente al vencimiento'),
        'y4': R(fin, None) if False else None,
    }
    faltan = [k for k, v in celdas.items() if v is None and k != 'y4']
    if faltan:
        res['fallos'].append('grupo_a: no se localizan las filas '
                             + ', '.join(sorted(faltan)))
        return res

    xl = _pycel(path)
    base = dict((k, _ev(xl, v)) for k, v in celdas.items() if v)
    res['demostraciones_2_11']['caso_base'] = dict(
        (k, (round(v, 2) if isinstance(v, float) else v))
        for k, v in base.items())

    def num(v):
        return v if isinstance(v, (int, float)) and not isinstance(v, bool) \
            else None

    # 1 — mover los cubiertos mueve las cuatro cifras estrella
    p1 = _clon(path, os.path.join(demos_dir, 'd1.xlsx'),
               [(sup, celdas['cubiertos'].split('!')[-1],
                 (num(base['cubiertos']) or 55) * 1.4)])
    x1 = _pycel(p1)
    mov = {}
    for clave in ('ingresos', 'rai', 'be_dia', 'esc_rai'):
        mov[clave] = [base[clave], _ev(x1, celdas[clave])]
    quietas = [k for k, v in mov.items()
               if num(v[0]) is not None and num(v[1]) is not None
               and abs(v[0] - v[1]) < 0.01]
    res['demostraciones_2_11']['1_cubiertos_mueven_el_libro'] = {
        'celda': celdas['cubiertos'], 'valor_nuevo': round(
            (num(base['cubiertos']) or 55) * 1.4, 2),
        'movimiento': dict((k, [round(v[0], 2) if num(v[0]) is not None
                                else v[0],
                                round(v[1], 2) if num(v[1]) is not None
                                else v[1]]) for k, v in mov.items()),
        'ok': not quietas}
    if quietas:
        res['fallos'].append('§2.11.1: al subir los cubiertos NO se mueven '
                             + ', '.join(quietas))

    # 2 — el escenario Realista reproduce el P&L al céntimo
    d2 = None
    if num(base['esc_rai']) is not None and num(base['rai']) is not None:
        d2 = round(abs(base['esc_rai'] - base['rai']), 4)
    res['demostraciones_2_11']['2_realista_igual_al_pyg'] = {
        'escenarios_realista': base['esc_rai'], 'pyg_ano_1': base['rai'],
        'diferencia': d2, 'ok': d2 is not None and d2 <= 0.01}
    if d2 is None or d2 > 0.01:
        res['fallos'].append('§2.11.2: «Realista» y el año 1 del P&L difieren '
                             + str(d2))

    # 3 — el P&L lee el personal de su hoja y el ratio cumple su umbral
    d3 = None
    if num(base['personal_pyg']) is not None \
            and num(base['personal_hoja']) is not None:
        d3 = round(abs(base['personal_pyg'] - base['personal_hoja']), 4)
    ratio_ok = (num(base['r_personal']) is not None
                and num(base['u_personal']) is not None
                and base['r_personal'] <= base['u_personal'] + 1e-9)
    res['demostraciones_2_11']['3_personal_del_pyg_es_el_de_su_hoja'] = {
        'pyg': base['personal_pyg'], 'hoja_personal': base['personal_hoja'],
        'diferencia': d3, 'ratio': base['r_personal'],
        'umbral': base['u_personal'], 'ok': (d3 == 0) and ratio_ok}
    if d3 != 0:
        res['fallos'].append('§2.11.3: el P&L no imputa el coste de la hoja '
                             'Personal (diferencia ' + str(d3) + ')')
    if not ratio_ok:
        res['fallos'].append('§2.11.3 / DOM-13: el caso base NO pasa su '
                             'propio semáforo de personal ('
                             + str(base['r_personal']) + ' > '
                             + str(base['u_personal']) + ')')

    # 4 — delivery a cero deja la línea a cero
    p4 = _clon(path, os.path.join(demos_dir, 'd4.xlsx'),
               [(sup, celdas['delivery'].split('!')[-1], 0)])
    x4 = _pycel(p4)
    v4 = _ev(x4, celdas['deliv_pyg'])
    res['demostraciones_2_11']['4_delivery_a_cero'] = {
        'linea_delivery': v4, 'ok': num(v4) == 0}
    if num(v4) != 0:
        res['fallos'].append('§2.11.4: con delivery al 0 % la línea vale '
                             + str(v4))

    # 5 — IS: pérdida en el año 1, BIN compensada en el 2, tipo reducido
    # El escenario se elige para que se vean las TRES ramas: año 1 en
    # pérdidas (impuesto cero), año 2 con base positiva MENOR que la base
    # negativa pendiente (impuesto cero por compensación) y año 3 tributando
    # al tipo de entidad de nueva creación, que es su primer ejercicio con
    # base positiva.
    p5 = _clon(path, os.path.join(demos_dir, 'd5.xlsx'),
               [(sup, celdas['cubiertos'].split('!')[-1], DEMO5_CUBIERTOS)])
    x5 = _pycel(p5)
    is1, is2, is3 = (_ev(x5, celdas['is1']), _ev(x5, celdas['is2']),
                     _ev(x5, celdas['is3']))
    rai1, rai2 = _ev(x5, celdas['rai']), _ev(x5, celdas['rai2'])
    tipo3 = _ev(x5, celdas['tipo3'])
    bin2 = _ev(x5, celdas['bin_ini2'])
    ok5 = (num(rai1) is not None and rai1 < 0 and num(is1) == 0
           and num(rai2) is not None and rai2 > 0 and num(is2) == 0
           and num(bin2) is not None and bin2 > rai2
           and num(tipo3) is not None and abs(tipo3 - 0.15) < 1e-9
           and num(is3) is not None and is3 > 0)
    res['demostraciones_2_11']['5_IS_con_BIN_y_tipo_de_nueva_creacion'] = {
        'cubiertos_del_ensayo': DEMO5_CUBIERTOS,
        'rai_ano_1': rai1, 'is_ano_1': is1,
        'rai_ano_2': rai2, 'bin_pendiente_ano_2': bin2, 'is_ano_2': is2,
        'is_ano_3': is3, 'tipo_ano_3': tipo3, 'ok': ok5}
    if not ok5:
        res['fallos'].append('§2.11.5: no se demuestran las tres ramas del '
                             'impuesto (RAI1 ' + str(rai1) + ', IS1 '
                             + str(is1) + ', RAI2 ' + str(rai2) + ', BIN2 '
                             + str(bin2) + ', IS2 ' + str(is2) + ', tipo3 '
                             + str(tipo3) + ', IS3 ' + str(is3) + ')')

    # 6 — la caja nunca se agota con el fondo dotado
    ok6 = num(base['saldo_min']) is not None and base['saldo_min'] >= 0
    res['demostraciones_2_11']['6_tesoreria_sin_saldo_negativo'] = {
        'saldo_minimo': base['saldo_min'], 'fondo': base['fondo'], 'ok': ok6}
    if not ok6:
        res['fallos'].append('§2.11.6: el saldo mínimo de tesorería es '
                             + str(base['saldo_min'])
                             + ': hay que subir el fondo de maniobra')

    # 7 — carencia >= plazo: se anula y el cuadro cierra en cero
    p7 = _clon(path, os.path.join(demos_dir, 'd7.xlsx'),
               [(sup, celdas['plazo'].split('!')[-1], 3),
                (sup, celdas['carencia'].split('!')[-1], 3)])
    x7 = _pycel(p7)
    cierre = _ev(x7, celdas['cierre'])
    # las filas del cuadro llevan el AÑO como número en la columna A, así que
    # no tienen rótulo de texto y no se pueden buscar por él
    apagados = []
    import openpyxl as _px
    ws7 = motor.hoja(_px.load_workbook(p7), fin, obligatoria=True)
    for anio in (4, 5):
        for r in range(1, ws7.max_row + 1):
            if ws7.cell(row=r, column=1).value == anio:
                for col in ('C', 'D', 'E'):
                    apagados.append([anio, col,
                                     _ev(x7, "'" + fin + "'!" + col + str(r))])
                break
    ok7 = (num(cierre) is not None and abs(cierre) <= 0.5
           and len(apagados) == 6
           and all(v in ('', None) or num(v) == 0
                   for _a, _c, v in apagados))
    res['demostraciones_2_11']['7_carencia_igual_al_plazo'] = {
        'capital_al_vencimiento': cierre, 'cuotas_anos_4_y_5': apagados,
        'ok': ok7}
    if not ok7:
        res['fallos'].append('§2.11.7: con plazo 3 y carencia 3 el cuadro no '
                             'cierra en cero o los años 4-5 siguen vivos ('
                             + str(cierre) + ', ' + str(apagados) + ')')

    # 8 — libro EN BLANCO: ni un semáforo verde ni un 0,0 % falso
    # se vacían TODAS las celdas de entrada de la hoja de supuestos, no una:
    # el libro en blanco es el estado en el que un semáforo verde o un
    # «0,0 %» mienten más caro
    import openpyxl as _px2
    wb8 = _px2.load_workbook(path)
    ws8 = motor.hoja(wb8, sup, obligatoria=True)
    blancos = [(sup, c.coordinate, None) for row in ws8.iter_rows()
               for c in row if motor.es_verde(c)]
    p8 = _clon(path, os.path.join(demos_dir, 'd8.xlsx'), blancos)
    x8 = _pycel(p8)
    vacias = {}
    for clave in ('ingresos', 'rai', 'neto', 'r_personal', 'be_dia',
                  'esc_rai', 'saldo_min', 'cierre'):
        vacias[clave] = _ev(x8, celdas[clave])
    falsos = [k for k, v in vacias.items()
              if isinstance(v, (int, float)) and not isinstance(v, bool)]
    res['demostraciones_2_11']['8_libro_en_blanco_sin_falsos_verdes'] = {
        'valores': vacias, 'ok': not falsos}
    if falsos:
        res['fallos'].append('§2.11.8: con el libro en blanco siguen dando '
                             'número (y por tanto semáforo) ' + ', '.join(
                                 falsos))
    return res
