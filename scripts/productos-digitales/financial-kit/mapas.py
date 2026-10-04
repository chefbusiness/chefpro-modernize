#!/usr/bin/env python3
"""
mapas.py — Restaurant Financial Plan Kit Pro (EN) · mapas ES→EN del Kit Plan Financiero v2.0.

SPEC: `scripts/productos-digitales/financial-kit/SPEC.md` (D1-Dn). Sesión Claude Code, 3-oct-2026.
Copia adaptada de `staff-kit/mapas.py`. Importable SIN efectos (solo constantes y funciones). Ejecutado como
script corre el autotest (pestañas ≤ 31 caracteres y sin caracteres prohibidos, claves EN sin comillas dobles
ni español, límites de Excel en DV, reglas US con fuente) y, si existe `censo_es.json` al lado, comprueba que
TODAS las pestañas, listas de DV, literales de fórmula, de CF y de DV personalizada, y patrones con
comparación numérica del censo tienen su EN, y que **ningún literal EN cambia de color** en su rango de CF
(los `containsText` del kit usan SEARCH, que casa subcadenas sin distinguir mayúsculas).

    python3 mapas.py

Contenido:
  · PRODUCTO / SLUG / URL_PRODUCTO / MARCA_ES / MARCA_EN / FOOTER_ES / FOOTER_EN       (D1, D2, D20)
  · FICHEROS, TITULOS, NOMBRES_CITA            nombres de fichero, título interior y cita corta (D5)
  · HOJAS, HOJAS_ES_POR_LIBRO                  pestañas ES→EN (D6)
  · CLAVES                                     literales de fórmula/CF/DV e ítems de lista (D7)
  · FIJOS                                      cadenas con decisión de mercado, por TEXTO (cualquier celda)
  · POR_CELDA                                  textos EN fijados por celda (cuando el mismo texto ES va a dos EN)
  · DV_PARTIDAS, DV_NUEVAS                     DV que se parten (D10: vida útil) y DV nuevas
  · FORMULAS_EN, PATRONES_SIN_CAMBIO           patrones de fórmula que cambian / que comparan y no cambian
  · VALORES_EN                                 números que cambian (D9-D14)
  · FORMATOS_EN                                formatos de número (moneda fuera, p.p., fecha) (D18, D19)
  · REGLAS_US                                  cifras US/UK con su fuente (SPEC §3)
"""
import json
import os
import re
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))

# ==========================================================================
# 0. Producto (D1, D2, D20)
# ==========================================================================
PRODUCTO = 'Restaurant Financial Plan Kit Pro'
SLUG = 'restaurant-financial-plan-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_FINANCIAL_PLAN_KIT'
PRECIO = '$49'
VERSION_ES = '2.0'
MARCA_ES = 'AI Chef Pro · aichef.pro — Kit Plan Financiero para Restaurantes'
MARCA_EN = 'AI Chef Pro · aichef.pro — ' + PRODUCTO
FOOTER_ES = 'AI Chef Pro · aichef.pro · Página &P de &N'
FOOTER_EN = 'AI Chef Pro · aichef.pro · Page &P of &N'

# ==========================================================================
# 1. Ficheros y títulos (D5: intención de búsqueda US)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-plan-financiero-previsional.xlsx', '01-restaurant-financial-projections-3-year.xlsx'),
    ('01b-plan-financiero-previsional-5-anos.xlsx', '01b-restaurant-financial-projections-5-year.xlsx'),
    ('02-calculadora-punto-equilibrio.xlsx', '02-restaurant-break-even-calculator.xlsx'),
    ('03-cash-flow-forecast.xlsx', '03-restaurant-cash-flow-forecast.xlsx'),
    ('04-presupuesto-inversion-capex.xlsx', '04-restaurant-startup-costs-budget.xlsx'),
    ('05-pyl-mensual-real-vs-presupuesto.xlsx', '05-restaurant-pl-template-budget-vs-actual.xlsx'),
    ('06-dashboard-ratios-financieros.xlsx', '06-restaurant-kpi-ratios-dashboard.xlsx'),
    ('07-informe-viabilidad-bancos.xlsx', '07-restaurant-loan-proposal-lender-summary.xlsx'),
    ('BONUS-08-simulador-escenarios.xlsx', 'BONUS-08-what-if-scenario-simulator.xlsx'),
    ('BONUS-09-checklist-pre-apertura.xlsx', 'BONUS-09-pre-opening-financial-checklist.xlsx'),
])
LIBROS_ES = list(FICHEROS)

TITULOS = OrderedDict([
    ('01-restaurant-financial-projections-3-year.xlsx', 'Restaurant Financial Projections: 3-Year Pro Forma P&L'),
    ('01b-restaurant-financial-projections-5-year.xlsx', 'Restaurant Financial Projections: 5-Year Pro Forma P&L'),
    ('02-restaurant-break-even-calculator.xlsx', 'Restaurant Break-Even Calculator'),
    ('03-restaurant-cash-flow-forecast.xlsx', 'Restaurant Cash Flow Forecast (12 Months)'),
    ('04-restaurant-startup-costs-budget.xlsx', 'Restaurant Startup Costs & Capex Budget'),
    ('05-restaurant-pl-template-budget-vs-actual.xlsx', 'Restaurant P&L Template: Monthly Budget vs Actual'),
    ('06-restaurant-kpi-ratios-dashboard.xlsx', 'Restaurant Financial Ratios & KPI Dashboard'),
    ('07-restaurant-loan-proposal-lender-summary.xlsx', 'Restaurant Loan Proposal: Lender & Investor Summary'),
    ('BONUS-08-what-if-scenario-simulator.xlsx', 'BONUS: What-If Scenario Simulator'),
    ('BONUS-09-pre-opening-financial-checklist.xlsx', 'BONUS: Pre-Opening Financial Checklist (54 Tasks)'),
])

# Nombre corto con el que un texto cita otro fichero: file NN "nombre" (UN nivel, sin subtítulo; staff-kit §6.5)
NOMBRES_CITA = OrderedDict([
    ('01', '3-Year Financial Projections'), ('01b', '5-Year Financial Projections'),
    ('02', 'Break-Even Calculator'), ('03', 'Cash Flow Forecast'), ('04', 'Startup Costs & Capex Budget'),
    ('05', 'Monthly P&L Budget vs Actual'), ('06', 'KPI & Ratios Dashboard'), ('07', 'Lender & Investor Summary'),
    ('B08', 'What-If Scenario Simulator'), ('B09', 'Pre-Opening Financial Checklist'),
])


def corto_de(fichero):
    m = re.match(r'^(BONUS-)?(\d+b?)', fichero)
    return ('B' if m.group(1) else '') + m.group(2)


# Título interior: Instructions!B2 = «NN · título» (D5); el BONUS lleva «BONUS 08 · …» como el ES
def titulo_interior(fichero_es):
    en = FICHEROS[fichero_es]
    t = TITULOS[en]
    if t.startswith('BONUS: '):
        return 'BONUS %s · %s' % (en[6:8], t[len('BONUS: '):])
    return '%s · %s' % (en.split('-')[0], t)


# ==========================================================================
# 2. Pestañas (D6) — nombres ≤ 31 caracteres, sin []:*?/\
# ==========================================================================
MESES = OrderedDict([('Ene', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Abr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'),
                     ('Jul', 'Jul'), ('Ago', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dic', 'Dec')])
HOJAS = OrderedDict([
    ('Instrucciones', 'Instructions'),
    ('Año 1', 'Year 1'), ('Año 2', 'Year 2'), ('Año 3', 'Year 3'), ('Año 4', 'Year 4'), ('Año 5', 'Year 5'),
    ('Resumen', 'Summary'),
    ('Datos', 'Inputs'), ('Break-Even', 'Break-Even'), ('Escenarios', 'Scenarios'),
    ('Parámetros', 'Assumptions'), ('Flujo Mensual', 'Monthly Cash Flow'), ('Alertas', 'Cash Alerts'),
    ('Obra', 'Build-Out'), ('Equipamiento Cocina', 'Kitchen Equipment'), ('Mobiliario Sala', 'Dining Room FF&E'),
    ('Tecnología', 'Technology'), ('Licencias', 'Licenses & Permits'),
    ('Otros conceptos de apertura', 'Other Opening Costs'),
])
HOJAS.update(MESES)
HOJAS.update([
    ('Resumen Anual', 'Annual Summary'),
    ('Ratios', 'Ratios'), ('Benchmarks', 'Benchmarks'),
    ('Resumen Ejecutivo', 'Executive Summary'), ('Proyecciones', 'Projections'), ('Financiación', 'Loan Schedule'),
    ('Garantías', 'Collateral'),
    ('Simulador', 'Simulator'), ('Comparativa', 'Comparison'),
    ('Checklist', 'Checklist'),
])

HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Año 1', 'Año 2', 'Año 3', 'Resumen']),
    ('01b', ['Instrucciones', 'Año 1', 'Año 2', 'Año 3', 'Año 4', 'Año 5', 'Resumen']),
    ('02', ['Instrucciones', 'Datos', 'Break-Even', 'Escenarios']),
    ('03', ['Instrucciones', 'Parámetros', 'Flujo Mensual', 'Alertas']),
    ('04', ['Instrucciones', 'Obra', 'Equipamiento Cocina', 'Mobiliario Sala', 'Tecnología', 'Licencias',
            'Otros conceptos de apertura', 'Resumen']),
    ('05', ['Instrucciones'] + list(MESES) + ['Resumen Anual']),
    ('06', ['Instrucciones', 'Ratios', 'Benchmarks']),
    ('07', ['Instrucciones', 'Resumen Ejecutivo', 'Proyecciones', 'Financiación', 'Ratios', 'Garantías']),
    ('B08', ['Instrucciones', 'Simulador', 'Comparativa']),
    ('B09', ['Instrucciones', 'Checklist']),
])
HOJA_PROHIBIDOS = set('[]:*?/\\')

# ==========================================================================
# 3. Claves (D7): literales de fórmula, de CF y de DV, e ítems de lista. Un solo paso ES→EN.
#    Los tokens de CF (SEARCH, subcadena) se traducen 1:1 y ningún mensaje EN cambia de color.
# ==========================================================================
CLAVES = OrderedDict([
    # semáforos genéricos
    ('OK', 'OK'), ('—', '—'), ('✅', '✅'), ('⚠️', '⚠️'), ('🔴', '🔴'),
    # 02 Break-Even
    ('Revisa el % de coste variable (no puede ser 100 %)', 'Check the variable cost % (it cannot be 100%)'),
    ('Indica los días de apertura', 'Enter the opening days'),
    ('Indica el ticket medio', 'Enter the average check'),
    ('Indica los cubiertos/día previstos', 'Enter the expected covers/day'),
    # 03 Alertas
    ('⚠️ BAJO MÍNIMO', '⚠️ BELOW MINIMUM'), ('BAJO MÍNIMO', 'BELOW MINIMUM'),
    # 05 semáforo con signo
    ('✅ OK', '✅ OK'), ('⚠️ Atención', '⚠️ Watch'), ('🔴 Alerta', '🔴 Alert'),
    # 06 semáforo de ratios
    ('✅ Excelente', '✅ Excellent'), ('⚠️ Aceptable', '⚠️ Acceptable'), ('🔴 Alto', '🔴 High'),
    ('✅ Sano', '✅ Healthy'), ('⚠️ Ajustado', '⚠️ Tight'), ('🔴 Peligro', '🔴 Danger'),
    ('Indica las ventas', 'Enter sales'), ('Indica las ventas de barra', 'Enter bar sales'),
    ('Indica plazas y horas', 'Enter seats and hours'), ('Indica los cubiertos', 'Enter covers'),
    ('Indica los m² de sala', 'Enter the dining room sq ft'),
    # 07
    ('No se recupera en 5 años', 'Not paid back within 5 years'),
    ('La carencia no puede igualar ni superar el plazo', 'The interest-only period must be shorter than the term'),
    ('Indica deuda y fondos propios', 'Enter debt and equity'), ('Indica el préstamo', 'Enter the loan'),
    ('Indica el balance', 'Enter the balance sheet'), ('Indica la facturación', 'Enter revenue'),
    ('Indica la inversión', 'Enter the investment'), ('Indica el EBITDA', 'Enter EBITDA'),
    # BONUS-09 estados (DV de lista + COUNTIF + CF)
    ('Pendiente', 'Pending'), ('En curso', 'In progress'), ('Completada', 'Completed'),
])

# ==========================================================================
# 4. DV (D10): la DV «C… H…» (porcentaje 0-1) de las 5 pestañas de CAPEX se parte: C sigue en 0-1, H pasa a vida
#    útil en años. (libro, hoja ES, sqref ES) → (sqref que conserva la DV ES, sqref de la DV nueva, tipo, op, f1, f2,
#    mensaje, título ≤ 32)
# ==========================================================================
_VIDA = ('Useful life in years (straight line). Leave blank for items you expense, such as license fees. Building '
         'permits and design fees are part of the build-out: same life.')


def _col(c, r1, r2):
    return ' '.join('%s%d' % (c, r) for r in range(r1, r2 + 1))


DV_PARTIDAS = OrderedDict()
for _h, _r2 in (('Obra', 14), ('Equipamiento Cocina', 16), ('Mobiliario Sala', 14), ('Tecnología', 12),
                ('Licencias', 12)):
    DV_PARTIDAS[('04', _h, _col('C', 5, _r2) + ' ' + _col('H', 5, _r2))] = (
        _col('C', 5, _r2), _col('H', 5, _r2), 'decimal', 'between', '0', '50', _VIDA, 'Invalid useful life')
# D27 (revisión final): el plazo de proveedores del 03 se limita a 0-30 días (el flujo solo paga este mes o el que
# viene; con más días la fila 16 salía negativa). La DV «≥ 0» de C5 C6 C26 se parte: C5 y C26 la conservan.
DV_PARTIDAS[('03', 'Parámetros', 'C5 C6 C26')] = (
    'C5 C26', 'C6', 'decimal', 'between', '0', '30',
    'Enter 0 to 30 days. This sheet pays each month\'s purchases this month or next, so longer terms count as 30.',
    'Invalid payment terms')
DV_NUEVAS = OrderedDict()                   # ninguna celda nueva

# ==========================================================================
# 5. Fórmulas que cambian (D10). Clave = patrón ES del censo; valor = patrón EN FINAL (pestañas EN).
# ==========================================================================
FORMULAS_EN = OrderedDict([
    # 04 CAPEX, columna I: dotación anual = coste / vida útil (años), lineal; vida vacía o 0 → 0 (se gasta)
    ('=$B{r}*$H{r}', '=IFERROR($B{r}/$H{r},0)'),
])

# --------------------------------------------------------------------------
# 5b. Revisión final (SPEC D25-D31): cambios de fórmula CELDA A CELDA, escritos en ESPACIO ES (pestañas y literales
#     ES; el Transformador los pasa a EN como cualquier otra fórmula). Así la caché de referencia del gate G6 los aplica
#     sobre el ES publicado y el gate G1 sigue exigiendo el resto de fórmulas idénticas al ES.
#   · PARCHES_FORMULA: (libro, hoja ES, rango) → (viejo, nuevo): sustitución de subcadena (todas las apariciones) en
#     cada celda con fórmula del rango; «{c}» = letra de columna de la celda. Aborta si `viejo` no está.
#   · FORMULAS_NUEVAS: celdas SIN fórmula en el ES (vacías o inputs) que pasan a fórmula. ESTILO_DE = celda de la
#     misma hoja de la que copian el estilo (y con él, bloqueo y relleno: dejan de ser input verde).
#   · CF_SQREF_EN: rangos de formato condicional que se amplían para cubrir una fila nueva.
# --------------------------------------------------------------------------
PARCHES_FORMULA = OrderedDict([
    # D25 DSCR a cuota completa: el denominador es la cuota anual constante (C8), no la del año 1 (que con
    # interest-only es solo intereses y daba un DSCR inflado)
    (('07', 'Ratios', 'C5'), ("'Financiación'!$C$12", "'Financiación'!$C$8")),
    # D29 tipo 0 %: la anualidad francesa divide por 0 → el capital se reparte a partes iguales en el plazo restante
    (('07', 'Financiación', 'C8'), ('IFERROR($C$4*$C$5/(1-(1+$C$5)^(-($C$6-$C$7))),0)',
                                     'IF($C$5=0,$C$4/($C$6-$C$7),IFERROR($C$4*$C$5/(1-(1+$C$5)^(-($C$6-$C$7))),0))')),
    # D27 plazo de proveedores: el flujo reparte las compras entre este mes y el siguiente; > 30 días daba pagos
    # negativos → tope 30 (y DV 0-30 en DV_PARTIDAS)
    (('03', 'Flujo Mensual', 'B16:M16'), ('Parámetros!$C$6', 'MIN(Parámetros!$C$6,30)')),
    # D28 base del sales tax: dine-in + bar + eventos (filas 7, 8, 10). Fuera: delivery de marketplaces (el marketplace
    # cobra e ingresa el impuesto en la mayoría de estados) y «otros cobros» (capital, préstamos, devoluciones)
    (('03', 'Flujo Mensual', 'B36:M36'), ('{c}12-{c}12/(1+Parámetros!$C$7)',
                                         '({c}7+{c}8+{c}10)-({c}7+{c}8+{c}10)/(1+Parámetros!$C$7)')),
    # D30 ventas por sq ft: cifra ANUAL (convención US); las ventas de la hoja son mensuales
    (('06', 'Ratios', 'C30'), ('$C$6/$C$11', '$C$6*12/$C$11')),
])
FORMULAS_NUEVAS = OrderedDict([
    # D31 los datos de balance del 07 que ya están en el libro se enlazan en vez de teclearse dos veces
    (('07', 'Ratios', 'C15'), "='Resumen Ejecutivo'!$C$14"),        # fondos propios = aportación del resumen
    (('07', 'Ratios', 'C16'), "='Financiación'!$C$4"),              # deuda = importe del préstamo
    # D32 06: la ocupación (alquiler / ventas) tenía benchmark y nadie la evaluaba → fila 26 con su semáforo
    (('06', 'Ratios', 'C26'), '=IFERROR($C$38/$C$6,"Indica las ventas")'),
    (('06', 'Ratios', 'D26'), '=Benchmarks!$D$8'),
    (('06', 'Ratios', 'E26'), '=IFERROR(IF(ISNUMBER($C26),IF($C26<Benchmarks!$F$8,"✅ Excelente",'
                              'IF($C26<=Benchmarks!$G$8,"⚠️ Aceptable","🔴 Alto")),"—"),"—")'),
    (('06', 'Ratios', 'F26'), '=Benchmarks!$F$8'),
])
ESTILO_DE = OrderedDict([
    (('07', 'Ratios', 'C15'), 'C17'), (('07', 'Ratios', 'C16'), 'C17'),
    (('06', 'Ratios', 'B26'), 'B25'), (('06', 'Ratios', 'C26'), 'C25'), (('06', 'Ratios', 'D26'), 'D25'),
    (('06', 'Ratios', 'E26'), 'E25'), (('06', 'Ratios', 'F26'), 'F25'),
])
CF_SQREF_EN = OrderedDict([(('06', 'Ratios', 'E17:E25'), 'E17:E26')])


def _celdas_rango(ref):
    m = re.fullmatch(r'([A-Z]+)(\d+)(?::([A-Z]+)(\d+))?', ref)
    c1, r1 = m.group(1), int(m.group(2))
    c2, r2 = (m.group(3), int(m.group(4))) if m.group(3) else (c1, r1)
    def n(c):
        x = 0
        for ch in c:
            x = x * 26 + ord(ch) - 64
        return x
    def l(i):
        out = ''
        while i:
            i, r = divmod(i - 1, 26)
            out = chr(65 + r) + out
        return out
    return ['%s%d' % (l(c), r) for r in range(r1, r2 + 1) for c in range(n(c1), n(c2) + 1)]


_PARCHE_POR_CELDA = {}
for (_c, _h, _rg), _par in PARCHES_FORMULA.items():
    for _x in _celdas_rango(_rg):
        _PARCHE_POR_CELDA[(_c, _h, _x)] = _par


def parchear_formula_es(corto, hoja_es, coord, f):
    """Fórmula ES con el parche de la revisión final aplicado (o la misma si la celda no tiene parche)."""
    par = _PARCHE_POR_CELDA.get((corto, hoja_es, coord))
    if par is None:
        return f
    col = re.match(r'[A-Z]+', coord).group(0)
    viejo, nuevo = par[0].replace('{c}', col), par[1].replace('{c}', col)
    if viejo not in f:
        raise ValueError('PARCHES_FORMULA %s %s!%s: %r no está en %r' % (corto, hoja_es, coord, viejo, f[:120]))
    return f.replace(viejo, nuevo)


def celdas_parcheadas(corto=None):
    return sorted(k for k in _PARCHE_POR_CELDA if corto is None or k[0] == corto)


# Patrones con comparación numérica que NO cambian (clave = libro, hoja ES, primera celda del patrón)
PATRONES_SIN_CAMBIO = {('05', _m, _c) for _m in MESES for _c in ('B27', 'C27')}   # food cost % «<=0» → ""
PATRONES_SIN_CAMBIO |= {
    ('06', 'Ratios', 'C17'),                                   # ventas de comida <= 0 → aviso
    ('07', 'Proyecciones', 'B15'), ('07', 'Proyecciones', 'C15'), ('07', 'Proyecciones', 'D15'),
    ('07', 'Proyecciones', 'E15'), ('07', 'Proyecciones', 'F15'),   # impuesto solo con beneficio > 0
    ('07', 'Proyecciones', 'B26'),                             # payback: flujo acumulado < 0
    ('07', 'Financiación', 'C8'),                              # interest-only >= plazo → aviso
}

# ==========================================================================
# 6. Números que cambian (D9-D14). (libro, hoja ES, celda o rango de una columna) → valor EN
# ==========================================================================
VALORES_EN = OrderedDict([
    # 03 Assumptions (D8): % cobrado con tarjeta, impuesto sobre ventas (ejemplo), impuesto recuperable US = 0
    (('03', 'Parámetros', 'C4'), 0.80), (('03', 'Parámetros', 'C7'), 0.08),
    (('03', 'Parámetros', 'C8'), 0), (('03', 'Parámetros', 'C9'), 0),
    # 04 (D9-D10): impuesto recuperable US = 0 (el sales tax va dentro del coste) · vida útil en años (libro)
    (('04', 'Obra', 'C5:C14'), 0), (('04', 'Obra', 'H5:H14'), 10),
    (('04', 'Equipamiento Cocina', 'C5:C16'), 0), (('04', 'Equipamiento Cocina', 'H5:H16'), 7),
    (('04', 'Mobiliario Sala', 'C5:C14'), 0), (('04', 'Mobiliario Sala', 'H5:H14'), 7),
    (('04', 'Tecnología', 'C5:C12'), 0), (('04', 'Tecnología', 'H5:H12'), 5),
    (('04', 'Licencias', 'H5'), None),          # D10: licencias y tasas = gasto → vida útil VACÍA (IFERROR → 0)
    (('04', 'Licencias', 'H6:H7'), 10),         # D33: licencia de obras y proyecto técnico se capitalizan con la obra
    (('04', 'Licencias', 'H8:H12'), None),
    (('04', 'Otros conceptos de apertura', 'C5'), 0), (('04', 'Otros conceptos de apertura', 'C7'), 0),
    (('04', 'Otros conceptos de apertura', 'C8'), 0), (('04', 'Otros conceptos de apertura', 'C10'), 0),
    (('04', 'Otros conceptos de apertura', 'C12'), 0),
    # 06 (D14, D15): 80 m² → 860 sq ft · benchmarks US de personal (30/35 %) y ocupación (6/10 %)
    (('06', 'Ratios', 'C11'), 860),
    (('06', 'Benchmarks', 'F5'), 0.30), (('06', 'Benchmarks', 'G5'), 0.35),
    (('06', 'Benchmarks', 'F8'), 0.06), (('06', 'Benchmarks', 'G8'), 0.10),
    # D34 GOP = EBITDA + ocupación: objetivo 15 + 6 = 21 %, límite 10 + 6 = 16 % (antes 20/15, incoherente)
    (('06', 'Benchmarks', 'F7'), 0.21), (('06', 'Benchmarks', 'G7'), 0.16),
    # 07 (D12, D13): ejemplo de préstamo tipo SBA 7(a) (10 %, 10 años) · aportación propia mínima SBA 10 %
    (('07', 'Financiación', 'C5'), 0.10), (('07', 'Financiación', 'C6'), 10),
    (('07', 'Ratios', 'G9'), 0.10),
])

# ==========================================================================
# 7. Textos fijados (no van a los traductores)
# ==========================================================================
FIJOS = OrderedDict([
    # ---- transversal: base sin impuesto (D8)
    ('Todas las cifras van SIN IVA; en el 03 (tesorería) van CON IVA porque es caja.',
     'All figures EXCLUDE sales tax; only file 03 "Cash Flow Forecast" includes it, because it is cash.'),
    # ---- 02 (D11)
    ('Coste total de personal fijo (salario bruto + SS empresa)',
     'Total fixed labor cost (gross wages + employer payroll taxes)'),
    ('€/mes — ≈ bruto × 1,32; es coste de EMPRESA, no bruto',
     'per month — ≈ gross wages × 1.10 (more with benefits): the EMPLOYER cost, not gross pay'),
    # ---- 03 (D8, D11)
    ("▸ El IVA trimestral se calcula solo con los tipos de 'Parámetros' y el calendario del modelo 303 (abril, julio y "
     "octubre); enero queda como input, porque liquida el 4T del año anterior.",
     '▸ Sales tax / VAT is paid once a quarter: the payment row fills itself from the rates in "Assumptions" in '
     'April, July and October; January stays as an input because it pays last year\'s Q4.'),
    ('▸ El bloque gris del final («datos base») no es caja: son las compras y la Seguridad Social devengada del mes, de '
     'donde salen el pago a proveedores, la SS del mes siguiente y el IVA.',
     '▸ The gray block at the bottom ("base data") is not cash: it holds the month\'s food purchases and accrued '
     'employer payroll taxes, which drive supplier payments, next month\'s payroll tax deposit and the tax rows.'),
    ('Todas las cifras de esta plantilla van CON IVA: es caja. En el resto del kit (01, 01b, 02, 05, 06 y 07) van SIN IVA.',
     'Every figure in this template INCLUDES the sales tax you collect: it is cash. The rest of the kit (files 01, 01b, '
     '02, 05, 06 and 07) EXCLUDES sales tax.'),
    ('IVA repercutido en ventas (%)', 'Sales tax / VAT charged on sales (%)'),
    ('Restauración: 10 %.',
     "US: your combined state + local rate on meals (8% is the kit's example). UK: 20% VAT. The tax row uses dine-in, "
     'bar and events (rows 7, 8 and 10): third-party delivery marketplaces usually collect and remit the sales tax on '
     'their orders in most US states; owner capital, loans and refunds are not taxable sales.'),
    ('IVA soportado en compras de alimentación (%)', 'Recoverable tax on food purchases (%)'),
    ('Alimentación: 10 % (4 % en algunos básicos).',
     'US: 0 (sales tax has no input credit; buy food for resale with a resale certificate). UK: most food is 0%.'),
    ('IVA soportado en el resto de gastos (%)', 'Recoverable tax on other expenses (%)'),
    ('Alquiler, suministros, marketing, gestoría: 21 %.',
     'US: 0. UK (VAT-registered): 20% on most expenses; on rent only if the landlord opted to tax.'),
    ('Calendario del modelo 303: se presenta del 1 al 20 de abril, julio y octubre, y del 1 al 30 de enero. Por eso la '
     'liquidación sólo calcula en esos meses.',
     "Quarterly filer: each quarter's tax is paid the month after it ends (April, July, October; January = last "
     "year's Q4). Monthly filer? Unprotect the sheet and type each payment. UK VAT: due 1 month and 7 days after "
     "your VAT quarter ends."),
    ('Pago de Seguridad Social (la del mes anterior)', "Employer payroll taxes deposited (last month's)"),
    ('Retenciones IRPF (mod. 111)', 'Employee taxes withheld, deposited (income tax + FICA)'),
    ('Liquidación de IVA (mod. 303) · enero = input (4T anterior)',
     'Sales tax / VAT payment (quarterly) · January = input (last Q4)'),
    ('Seguridad Social devengada del mes', 'Employer payroll taxes accrued this month'),
    ('IVA repercutido del mes', 'Sales tax / VAT collected this month (rows 7, 8 and 10)'),
    ('IVA soportado del mes', 'Recoverable tax paid this month (UK VAT; US: 0)'),
    # ---- 04 (D9, D10)
    ('▸ Cada partida lleva Base, IVA % e IVA (€): el desembolso real es la columna «Total con IVA», que con un 21 % es un '
     'quinto más de lo que enseña el presupuesto.',
     '▸ Each line has Cost, Recoverable tax % and Tax. US: sales tax is NOT recoverable, so include it in the cost '
     'and leave the tax % at 0. UK (VAT-registered): type the net cost and 20%; "Total incl. tax" is the cash you '
     'advance.'),
    ('▸ El coeficiente de amortización por pestaña (obra 3 %, cocina 12 %, mobiliario 10 %, tecnología 25 %) da la '
     'dotación anual que pide el 07.',
     '▸ Each line has a useful life in years (build-out 10, kitchen equipment 7, furniture 7, technology 5; straight '
     'line, book basis): it gives the annual depreciation that file 07 "Lender & Investor Summary" needs. Tax '
     'depreciation (MACRS, Section 179, '
     'bonus) is a separate calculation for your CPA.'),
    ("▸ Lo que no es CAPEX —traspaso, fianza, stock inicial, nóminas pre-apertura, imprevistos y fondo de maniobra— va en "
     "la pestaña 'Otros conceptos de apertura'.",
     '▸ What is not capex (key money, security deposit, opening inventory, pre-opening payroll, contingency and '
     'working capital) goes in the "Other Opening Costs" tab.'),
    ('Base (€)', 'Cost'), ('IVA %', 'Recoverable tax %'), ('IVA (€)', 'Tax'), ('Total con IVA (€)', 'Total incl. tax'),
    ('Coef. amortización', 'Useful life (years)'), ('Dotación anual (€)', 'Annual depreciation'),
    ('Licencia de apertura', 'Business license & certificate of occupancy'),
    ('Licencia de obras', 'Building permits'),
    ('Proyecto técnico (arquitecto)', 'Architect / engineer drawings'),
    ('Certificado energético', 'Health department plan review & permit'),
    ('Plan de autoprotección', 'Fire inspection & occupancy permit'),
    ('Alta Hacienda / SS', 'Liquor license'),
    ('Registro sanitario', 'Sign permit'),
    ('SGAE / Derechos música', 'Music licensing (ASCAP, BMI, SESAC)'),
    ('Traspaso del local', 'Key money / business purchase (if any)'),
    ('Fianza y primeras rentas', 'Security deposit & first rent'),
    ('Constitución, notaría y registro', 'Entity formation, legal & filing fees'),
    ('DESEMBOLSO TOTAL DE APERTURA (base + IVA)', 'TOTAL OPENING OUTLAY (cost + tax)'),
    ('▸ El «IVA (€)» de la fila 12 es IVA soportado: se recupera vía modelo 303, pero hay que ADELANTARLO. El préstamo '
     'tiene que cubrirlo.',
     '▸ The "Tax" in row 12 is recoverable VAT (UK): it comes back on your VAT return, but you pay it FIRST, so the '
     'loan has to cover it. US sales tax is not recoverable: it is already inside the cost.'),
    # ---- 06 (D14, D15)
    ('m² de sala', 'Dining room area (sq ft)'),
    ('Ventas por m² de sala (€, sin IVA)', 'Annual sales per sq ft (excl. sales tax)'),
    ('RevPASH (€/plaza/hora)', 'RevPASH (per seat-hour)'),
    ('> 6€', '> 6'), ('3€ - 6€', '3 - 6'), ('< 3€', '< 3'),
    ('▸ Labor Cost %: óptimo < 25% · peligro > 30% (los números viven en Benchmarks!F:G).',
     '▸ Labor Cost %: target < 30% · danger > 35% (the numbers live in "Benchmarks" F:G).'),
    ('Las columnas «Óptimo (nº)» y «Límite (nº)» son la ÚNICA fuente de umbrales del kit: el semáforo de la pestaña '
     'Ratios las lee, y los textos de la izquierda se generan desde ellas. Edítalas y todo el dashboard se mueve con ellas.',
     'The "Target (no.)" and "Limit (no.)" columns are the kit\'s ONLY source of thresholds: the traffic light in the '
     '"Ratios" tab reads them. The text columns on the left are a reading guide: if you edit the numbers, update them too.'),
    ('€', 'Amount'),                                        # título del eje de valores de los gráficos
    # ---- 07 (D11-D13)
    ('Superficie total (m²)', 'Total area (sq ft)'),
    ('Impuesto sobre Sociedades', 'Income tax'),
    ('EBITDA menos el Impuesto de Sociedades calculado SIN intereses. Es la fila que alimenta la TIR, el VAN y el '
     'payback de abajo.',
     'EBITDA minus income tax computed WITHOUT interest. This row feeds the IRR, NPV and payback below.'),
    ('Es el coste de capital que exige quien pone el dinero. Un 8 % es la referencia habitual en hostelería; súbela si '
     'tu riesgo es mayor.',
     "It is the return expected by whoever puts in the money. 8% is the kit's starting point; raise it if your risk "
     "is higher."),
    ('Tipo del Impuesto sobre Sociedades (%)', 'Effective income tax rate (%)'),
    ('Tipo general 25 %. Entidad de NUEVA CREACIÓN: 15 % los dos primeros ejercicios con base positiva (art. 29.1 LIS). '
     'Si tributas por IRPF (autónomo), pon 0 aquí y calcula el IRPF fuera.',
     "US C corp: 21% federal + your state's rate (25% is the kit's example). LLC, S corp or sole proprietor "
     "(pass-through): 0 here, the tax is paid on the owners' returns. UK: corporation tax 19% to 25%."),
    ('TIN, no TAE. (valor orientativo — cámbialo)', 'Nominal rate, not APR. (example: change it)'),
    ('Plazo TOTAL, carencia incluida. (valor orientativo — cámbialo)',
     'TOTAL term, interest-only period included. SBA 7(a): up to 10 years for equipment and working capital. '
     '(example: change it)'),
    ('Carencia de capital (años)', 'Interest-only period (years)'),
    ('Anualidad constante (sistema francés), calculada sobre el plazo posterior a la carencia. La carencia tiene que ser '
     'MENOR que el plazo: si no, no queda ningún año sobre el que repartir el capital y aquí sale un aviso en vez de una '
     'cifra.',
     'Level annual payment (standard amortization) over the term left after the interest-only period, which must be '
     'SHORTER than the term: otherwise no year is left to repay the principal and you get a warning here instead.'),
    ('Con carencia, los primeros años la columna «Amortización de capital» sale a 0 y el capital pendiente no baja: es lo '
     'que de verdad pasa en un ICO de apertura.',
     'With an interest-only period, "Principal repaid" shows 0 in the first years and the balance does not go down: '
     'that is how an interest-only start really works.'),
    ('Referencia Bancaria', 'Typical lender guideline (indicative)'),
    ('Aval personal del promotor', 'Personal guarantee (SBA: owners of 20%+)'),
    ('Pignoración de depósitos', 'Pledged deposits / cash collateral'),
    ('Aval SGR (Sociedad de Garantía Recíproca)', 'Blanket lien on business assets (UCC-1)'),
    ('Seguro de caución', 'Assignment of life insurance (SBA lenders)'),
    ('Fianza / depósito adicional', 'Additional deposit'),
    # ---- BONUS-09 (D16): tareas con trámite español → equivalente US (nota UK solo en Instrucciones)
    ('▸ Fase 7: Personal y obligaciones laborales (SS, RETA, apertura del centro de trabajo, contratos del convenio, '
     'altas previas, registro de jornada y modelo 111).',
     "▸ Phase 7: Staff and employer obligations (state employer registration, workers' comp, labor law posters, "
     "I-9 and W-4, new-hire reporting, payroll tax deposits). UK: PAYE registration and right-to-work checks."),
    ('Elegir forma jurídica (SL, autónomo, cooperativa)',
     'Choose the legal entity (LLC, S corp, C corp or sole proprietorship)'),
    ('Escritura de constitución ante notario', 'File the articles of organization or incorporation with the state'),
    ('Inscripción en Registro Mercantil', 'Register a DBA (assumed name) if you trade under another name'),
    ('Obtener NIF/CIF definitivo', 'Get your EIN from the IRS (free, online)'),
    ('Libro de actas y libro de socios', 'Operating agreement or bylaws, and ownership records'),
    ('Alta en el Censo de Empresarios (Modelo 036/037)', "Register with the state tax agency (sales tax / seller's permit)"),
    ('Registro de marca / nombre comercial (OEPM)', 'Trademark search and registration (USPTO)'),
    ('Solicitar préstamo ICO / línea de crédito', 'Apply for an SBA 7(a) loan or a line of credit'),
    ('Evaluar subvenciones autonómicas/locales', 'Look for state and local grants or incentives'),
    ('Negociar condiciones bancarias (tipo, plazo, carencia)', 'Negotiate loan terms (rate, term, interest-only period)'),
    ('Licencia de actividad / apertura', 'Business license and certificate of occupancy'),
    ('Licencia de obras (si reformas)', 'Building permits (if you renovate)'),
    ('Proyecto técnico (arquitecto/ingeniero)', 'Architect / engineer drawings for the permits'),
    ('Certificado de solidez / estructura', 'Fire department inspection and occupancy load'),
    ('Autorización sanitaria (Registro Sanitario)', 'Health department plan review and food service permit'),
    ('Inscripción RGSEAA (si elaboración)', 'Liquor license (apply early: it can take months)'),
    ('Plan de autoprotección (si aforo > 50)', 'Sign permit and sidewalk seating permit (if any)'),
    ('Contrato de gestión de residuos', 'Waste, recycling and grease trap service contracts'),
    ('Contratar servicio de desratización (DDD)', 'Hire a licensed pest control service'),
    ('Seguro de responsabilidad civil', 'General liability insurance'),
    ('Seguro multirriesgo del local', 'Commercial property insurance (or a BOP)'),
    ('Seguro de accidentes de trabajo', "Workers' compensation insurance (required in most states)"),
    ('Seguro de pérdida de beneficios', 'Business interruption insurance'),
    ('Seguro de mercancías (cámaras frías)', 'Food spoilage and equipment breakdown coverage'),
    ('Seguro de responsabilidad de administradores', 'Liquor liability insurance (if you serve alcohol)'),
    ('Seguro de ciberriesgos (si TPV/web)', 'Cyber liability insurance (POS and online orders)'),
    ('Seguro de caución (si aplica)', 'Surety bond (if your state or a license requires one)'),
    ('Configurar software de facturación (Veri*factu)', 'Set up accounting software and sales tax reporting'),
    ('Definir política de propinas', 'Define the tip policy (tip pooling and tip credit rules)'),
    ('Inscribir la empresa en la Seguridad Social y obtener el CCC',
     'Register as an employer with your state (unemployment insurance account)'),
    ('Alta del promotor/a en el RETA (o régimen que corresponda)',
     "Set up the owner's pay: salary (S or C corp) or draws (LLC, sole proprietor)"),
    ('Comunicación de apertura del centro de trabajo a la autoridad laboral',
     'Display the required federal and state labor law posters'),
    ('Contratos según el convenio provincial de hostelería',
     'Offer letters and handbook: pay rates, tip credit and overtime policy'),
    ('Alta de los trabajadores en la SS ANTES del inicio de la jornada',
     'Form I-9 and W-4 for every hire, plus new-hire reporting to the state'),
    ('Registro de jornada y calendario de nóminas y del modelo 111',
     'Time clock, payroll calendar and payroll tax deposits (Form 941)'),
])

# Celdas cuyo texto ES se repite en otro sitio con otro EN (los umbrales que cambian en D15)
POR_CELDA = OrderedDict([
    (('06', 'Benchmarks', 'C5'), '< 30%'), (('06', 'Benchmarks', 'D5'), '30% - 35%'),
    (('06', 'Benchmarks', 'E5'), '> 35%'),
    (('06', 'Benchmarks', 'B8'), 'Occupancy (rent) / Sales'),
    (('06', 'Benchmarks', 'C8'), '< 6%'), (('06', 'Benchmarks', 'D8'), '6% - 10%'), (('06', 'Benchmarks', 'E8'), '> 10%'),
    # D35 RevPASH: umbrales para el mercado y la moneda de cada uno
    (('06', 'Benchmarks', 'B13'), 'RevPASH (per seat-hour, your market)'),
])
# Rótulos de umbral SIN letras en el ES (no están en textos_es.json: «invariables») que cambian con la cifra (D34)
UMBRALES_TEXTO_EN = OrderedDict([
    (('06', 'Benchmarks', 'C7'), '> 21%'), (('06', 'Benchmarks', 'D7'), '16% - 21%'), (('06', 'Benchmarks', 'E7'), '< 16%'),
])

# Textos en celdas SIN texto en el ES (revisión final). (libro, hoja ES, celda) → (texto, celda de la que copia estilo
# o None = conserva el suyo). Aviso legal D36 en las 10 Instrucciones, justo debajo de la línea de versión.
AVISO_EN = ('Planning tool, not financial, tax or legal advice. Requirements vary by state and city — check with your '
            'accountant and local authorities.')
AVISO_B09_EN = 'This checklist is a starting point, not an exhaustive list.'
FILA_VERSION = OrderedDict([('01', 27), ('01b', 23), ('02', 19), ('03', 25), ('04', 23), ('05', 16), ('06', 24),
                            ('07', 25), ('B08', 19), ('B09', 28)])
TEXTOS_NUEVOS = OrderedDict()
for _c, _f in FILA_VERSION.items():
    TEXTOS_NUEVOS[(_c, 'Instrucciones', 'B%d' % (_f + 1))] = (AVISO_EN, 'B%d' % (_f - 2))
TEXTOS_NUEVOS[('B09', 'Instrucciones', 'B%d' % (FILA_VERSION['B09'] + 2))] = (AVISO_B09_EN, 'B%d' % (FILA_VERSION['B09'] - 2))
TEXTOS_NUEVOS.update([
    (('06', 'Ratios', 'B26'), ('Occupancy (rent) / Sales', 'B25')),                                  # D32
    (('06', 'Benchmarks', 'B18'), ('RevPASH thresholds (6 and 3 per seat-hour) assume US dollars: set them for your '
                                   'currency and market.', 'B17')),                                   # D35
    (('06', 'Benchmarks', 'B19'), ('GOP thresholds (21% / 16%) = EBITDA thresholds (15% / 10%) + 6 points of '
                                   'occupancy (rent).', 'B17')),                                      # D34
    (('04', 'Licencias', 'J6'), ('Capitalized with the build-out: same useful life.', None)),         # D33
    (('04', 'Licencias', 'J7'), ('Capitalized with the build-out: same useful life.', None)),
])

# ==========================================================================
# 8. Formatos (D18, D19)
# ==========================================================================
FORMATOS_EN = OrderedDict([
    ('#,##0.00 €', '#,##0.00'), ('€#,##0.00', '#,##0.00'), ('#,##0 €', '#,##0'),
    ('dd/mm/yyyy', 'NUMFMT14'),                  # fecha corta del sistema (m/d/yyyy en US)
    ('DD/MM/YYYY', 'NUMFMT14'),
    ('0.0" p.p."', '0.0%'),                      # I1: 0,02 se veía «0,0 p.p.»; en % se ve 2.0%
    ('0.00" años"', '0.00" years"'), ('0.0" años"', '0.0" years"'),
])

# D10: la columna H del 04 pasa de coeficiente (0.0%) a vida útil en años → formato numérico sin % (admite 7.5)
FORMATOS_POR_RANGO = OrderedDict(
    ((('04', _h, 'H5:H%d' % _r2)), 'General') for _h, _r2 in (('Obra', 14), ('Equipamiento Cocina', 16),
                                                               ('Mobiliario Sala', 14), ('Tecnología', 12),
                                                               ('Licencias', 12)))
FORMATOS_POR_RANGO[('06', 'Ratios', 'C26')] = '0.0%'           # D32: la fila nueva de ocupación, como la 25
FORMATOS_POR_RANGO[('06', 'Ratios', 'F26')] = '0.0%'

# Mensajes de DV fijados por APARICIÓN (revisión final; vacío de salida) y rótulos con ajuste de texto + alto de fila
DV_MENSAJES_EN = OrderedDict()
# Medido en el dry-run (F2-NOTAS §4): rótulos y notas EN que el vecino cortaba o que salían del ancho impreso
AJUSTE_TEXTO = [
    ('02', 'Datos', 'B7'), ('02', 'Datos', 'D7'), ('02', 'Datos', 'D15'), ('02', 'Datos', 'D17'),
    ('03', 'Parámetros', 'D4:D9'),
    ('04', 'Mobiliario Sala', 'A13'),
    ('07', 'Financiación', 'D4:D8'),
    ('B08', 'Simulador', 'A11'),
    # revisión final: rótulos que se cortaban (D37) y los textos nuevos
    ('01', 'Año 1', 'A27'), ('01', 'Año 2', 'A27'), ('01', 'Año 3', 'A27'),
    ('01b', 'Año 1', 'A27'), ('01b', 'Año 2', 'A27'), ('01b', 'Año 3', 'A27'), ('01b', 'Año 4', 'A27'),
    ('01b', 'Año 5', 'A27'),
    ('04', 'Equipamiento Cocina', 'A15'),
    ('B09', 'Checklist', 'B53:B58'), ('B09', 'Checklist', 'C5:C58'),
    ('06', 'Ratios', 'D16'), ('06', 'Ratios', 'B30'),
    ('07', 'Ratios', 'D3'),
    ('06', 'Benchmarks', 'B17:B19'),
]
AJUSTE_TEXTO += [(_c, _h, _x) for (_c, _h, _x), (_t, _e) in TEXTOS_NUEVOS.items() if _h == 'Instrucciones']
# Columnas de rótulos de tabla que el sufijo «(excl. sales tax)» desborda: más ancho en vez de filas de dos líneas
ANCHOS = OrderedDict([(('01', _h), {'A': 36}) for _h in ('Año 1', 'Año 2', 'Año 3', 'Resumen')])
ANCHOS.update((('01b', _h), {'A': 36}) for _h in ('Año 1', 'Año 2', 'Año 3', 'Año 4', 'Año 5', 'Resumen'))
ANCHOS.update((('05', _m), {'A': 36}) for _m in MESES)
ANCHOS[('02', 'Break-Even')] = {'B': 52}
ANCHOS[('07', 'Resumen Ejecutivo')] = {'B': 44}


def dv_lista(items):
    return '"' + ','.join(items) + '"'


# ==========================================================================
# 9. Reglas US/UK con fuente (SPEC §3). clave → (valor, fuente). [kit estimate] = no es norma.
# ==========================================================================
REGLAS_US = OrderedDict([
    ('sales_tax', ('US: impuesto de un solo escalón, sin crédito por compras; reventa con resale certificate; tipo '
                   'state + local de cada usuario; 8 % = ejemplo [kit estimate]',
                   'Tax Foundation, «State and Local Sales Tax Rates» (taxfoundation.org) [8 % = kit estimate]')),
    ('vat_uk', ('20 % estándar (comer en el local y comida caliente); la mayoría de alimentos 0 %',
                'HMRC VAT Notice 709/1 «Catering and take-away food»')),
    ('vat_uk_plazo', ('declaración y pago 1 mes y 7 días tras el trimestre', 'gov.uk/vat-returns/deadlines')),
    ('payroll_deposit', ('depositante mensual: el 15 del mes siguiente', 'IRS Publication 15 (Circular E), §11')),
    ('fica', ('7.65 % (6.2 % SS + 1.45 % Medicare)', 'IRS Publication 15 (Circular E)')),
    ('futa', ('6.0 % − 5.4 % de crédito = 0.6 % sobre los primeros $7,000', 'IRS Topic 759')),
    ('coste_empresa', ('≈ salario × 1.10 (FICA + FUTA/SUTA + workers\' comp)', '[kit estimate] sobre IRS Pub. 15 y Topic 759')),
    ('uk_paye', ('PAYE y NI mensuales, el 22 (pago electrónico)', 'gov.uk/pay-paye-tax')),
    ('impuesto_sociedades', ('21 % federal (C corp)', 'IRC §11(b) (Tax Cuts and Jobs Act 2017)')),
    ('pass_through', ('LLC, S corp, autónomo: tributa el dueño', 'IRS «Business structures» (irs.gov)')),
    ('uk_ct', ('19 % hasta £50,000; 25 % desde £250,000; marginal relief entre medias', 'gov.uk/corporation-tax-rates')),
    ('amortizacion_libro', ('lineal; leasehold improvements: el menor de plazo del alquiler y vida útil; vidas 10/7/7/5',
                            'ASC 842-20-35-12 [vidas = kit estimate]')),
    ('macrs', ('equipamiento de restaurante 5 años (clase 57.0), mobiliario 7, QIP 15; Section 179 y bonus',
               'IRS Publication 946; IRC §168(e)(6)')),
    ('uk_aia', ('Annual Investment Allowance £1,000,000', 'gov.uk/capital-allowances/annual-investment-allowance')),
    ('sba_plazo', ('hasta 10 años (equipo, circulante); 25 inmuebles', '13 CFR 120.212; sba.gov «7(a) loans»')),
    ('sba_tipo', ('máximo = Prime + diferencial; 10 % = ejemplo [kit estimate]', '13 CFR 120.213-120.214')),
    ('dscr_limite', ('1.15× = «Limit» editable del kit, SIN etiqueta SBA: el suelo SBA depende de la operación y del '
                     'SOP vigente (revisión final)', '[kit estimate]; SBA SOP 50 10 vigente')),
    ('dscr_banco', ('1.25× objetivo habitual del prestamista (orientativo)', '[kit estimate] práctica de banca')),
    ('aportacion_sba', ('aportación propia habitual ≈ 10 % en start-ups (orientativo; lo deciden el prestamista y el '
                        'SOP vigente)', 'SBA SOP 50 10 vigente [orientativo]')),
    ('aval_sba', ('aval personal de socios con 20 % o más', '13 CFR 120.160(a)')),
    ('benchmarks', ('food 28-32 %, labor 30-35 %, prime 60-65 %, ocupación 6-10 %, bebida 18-24 %, EBITDA 10-15 %, '
                    'GOP 16-21 % (= EBITDA + 6 pts de ocupación)',
                    '[kit estimate] reglas habituales del full-service US')),
    ('revpash', ('6 / 3 por plaza-hora, pensado en USD: cada usuario lo ajusta a su moneda y mercado', '[kit estimate]')),
    ('sqft', ('1 m² = 10.764 sq ft → 80 m² ≈ 860 sq ft', 'NIST SP 811, Appendix B')),
    ('tarjeta', ('80 % de ventas con tarjeta', '[kit estimate]')),
])


# ==========================================================================
# utilidades
# ==========================================================================
def patron(formula):
    """Normaliza las filas de las referencias de celda a {r} (las referencias absolutas $X$n se respetan)."""
    return re.sub(r'(?<![A-Za-z_$])(\$?[A-Z]{1,3})(?<!\$)(\d+)(?![\d(])',
                  lambda m: m.group(1) + '{r}', formula)


RX_LIT = re.compile(r'"((?:[^"]|"")*)"')


def necesita_clave(lit):
    """Un literal va a CLAVES si lleva letras, € o un emoji de semáforo; los demás (comparadores) no cambian."""
    return any(ch.isalpha() for ch in lit) or '€' in lit or lit in ('—', '✅', '⚠️', '🔴')


def tokens_en(texto, tokens):
    t = texto.lower()
    return {k for k in tokens if k.lower() in t}


# ==========================================================================
# autotest y cruce con el censo
# ==========================================================================
RX_ES = re.compile(r'[áíóúñÁÍÓÚÑ¿¡€]|\b(?:de|del|los|las|con|sin|para|por|IVA)\b')


def autotest():
    err = []
    for es, en in HOJAS.items():
        if len(en) > 31 or set(en) & HOJA_PROHIBIDOS or en.startswith("'"):
            err.append('pestaña inválida: ' + en)
    for f, hs in HOJAS_ES_POR_LIBRO.items():
        ens = [HOJAS[h] for h in hs]
        if len(set(ens)) != len(ens):
            err.append('pestañas EN duplicadas en ' + f)
    if len(FICHEROS) != 10 or len(set(FICHEROS.values())) != 10:
        err.append('FICHEROS debe tener 10 nombres EN distintos')
    for es, en in FICHEROS.items():
        if en not in TITULOS:
            err.append('fichero sin título: ' + en)
        if not re.fullmatch(r'(BONUS-)?\d{2}b?-[a-z0-9-]+\.xlsx', en) or corto_de(es) != corto_de(en):
            err.append('fichero EN mal formado: ' + en)
        if corto_de(es) not in NOMBRES_CITA:
            err.append('libro sin nombre de cita: ' + es)
    for k, v in CLAVES.items():
        if '"' in v or RX_ES.search(v):
            err.append('comilla o español en una clave EN: %r' % v)
        if len(v) > 255:
            err.append('clave EN > 255 (literal de fórmula): %r' % v[:40])
    for nombre, d in (('FIJOS', FIJOS), ('POR_CELDA', POR_CELDA)):
        for k, v in d.items():
            if RX_ES.search(v) or re.search(r'\d,\d', v):
                err.append('%s con español, € o coma decimal: %r' % (nombre, v[:60]))
            if re.search(r'\b(?:SPEC|D\d{1,2}|kit estimate|TEC-\d+)\b', v):
                err.append('%s con un ID interno: %r' % (nombre, v[:60]))
    for es, en in FORMULAS_EN.items():
        if RX_ES.search(en):
            err.append('español en FORMULAS_EN: ' + en[:60])
    for k, (t, _e) in TEXTOS_NUEVOS.items():
        if RX_ES.search(t) or re.search(r'\d,\d', t) or re.search(r'\b(?:SPEC|D\d{1,2}|kit estimate)\b', t):
            err.append('TEXTOS_NUEVOS con español, coma decimal o ID interno: %r' % t[:60])
    for k in list(FORMULAS_NUEVAS) + list(ESTILO_DE):
        if k in _PARCHE_POR_CELDA:
            err.append('celda con parche y fórmula nueva a la vez: %r' % (k,))
    for k in FORMULAS_NUEVAS:
        if k not in ESTILO_DE:
            err.append('FORMULAS_NUEVAS sin ESTILO_DE: %r' % (k,))
    for (c, h, x), (viejo, nuevo) in PARCHES_FORMULA.items():
        if viejo == nuevo or RX_ES.search(nuevo.replace('Parámetros', '').replace('Financiación', '')):
            err.append('PARCHES_FORMULA vacío o con español: %r' % ((c, h, x),))
    for k, v in DV_PARTIDAS.items():
        if len(v[6]) > 255 or len(v[7]) > 32 or not set(v[0].split()) | set(v[1].split()) == set(k[2].split()):
            err.append('DV_PARTIDAS mal partida o mensaje > 255: %r' % (k[:2],))
    for k, (val, fuente) in REGLAS_US.items():
        if not fuente:
            err.append('regla sin fuente: ' + k)
    return err


def _celdas(sqref):
    from openpyxl.utils import range_boundaries, get_column_letter
    s = set()
    for rng in sqref.split():
        c1, r1, c2, r2 = range_boundaries(rng)
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                s.add(get_column_letter(c) + str(r))
    return s


def cruzar_censo(p):
    censo = json.load(open(p, encoding='utf-8'))
    err = []
    patrones = {}
    primeras = set()
    for f, info in censo['libros'].items():
        if f not in FICHEROS:
            err.append('libro sin nombre EN: ' + f)
        c = info['corto']
        if HOJAS_ES_POR_LIBRO.get(c) != info['hojas']:
            err.append('HOJAS_ES_POR_LIBRO no coincide con el censo en ' + c)
        for h in info['hojas']:
            if h not in HOJAS:
                err.append('pestaña sin EN: %s / %s' % (f, h))
        for h, hd in info['hojas_detalle'].items():
            for dv in hd['dv']:
                f1 = dv['formula1'] or ''
                if f1.startswith('"'):
                    for it in f1.strip('"').split(','):
                        if necesita_clave(it) and it not in CLAVES:
                            err.append('ítem de DV sin EN: %s / %s / %r' % (c, h, it))
                for lit in dv.get('literales', []):
                    if necesita_clave(lit) and lit not in CLAVES:
                        err.append('literal de DV personalizada sin EN: %s / %s / %r' % (c, h, lit))
            for lit in list(hd['literales']) + list(hd['literales_cf']):
                if necesita_clave(lit) and lit not in CLAVES:
                    err.append('literal sin EN: %s / %s / %r' % (c, h, lit))
            for pat in hd['patrones_formula']:
                clave = (c, h, pat['celdas'].split('..')[0])
                patrones[pat['patron']] = clave
                primeras.add(clave)
                if pat['cifras'] and pat['patron'] not in FORMULAS_EN and clave not in PATRONES_SIN_CAMBIO:
                    err.append('fórmula con comparación numérica sin decidir: %s / %s / %s' % (c, h, pat['patron'][:110]))
            # CF: cada mensaje EN conserva exactamente sus tokens (SEARCH, sin mayúsculas) en su rango
            por_rango = OrderedDict()
            for cf in hd['cf']:
                por_rango.setdefault(cf['sqref'], []).extend(cf['tokens'])
            for rng, toks in por_rango.items():
                toks_en = [CLAVES.get(t, t) for t in toks]
                if len(set(t.lower() for t in toks_en)) != len(set(t.lower() for t in toks)):
                    err.append('tokens de CF EN no inyectivos en %s / %s / %s' % (c, h, rng))
                for t_es, t_en in zip(toks, toks_en):
                    for t2_es, t2_en in zip(toks, toks_en):
                        if t_es != t2_es and t_en.lower() in t2_en.lower() and t_es.lower() not in t2_es.lower():
                            err.append('token EN %r contenido en %r (%s / %s / %s)' % (t_en, t2_en, c, h, rng))
                cs = _celdas(rng)
                for lit, celdas in hd['literales'].items():
                    if not (cs & set(celdas)) or not necesita_clave(lit):
                        continue
                    en = CLAVES.get(lit, lit)
                    esperado = {CLAVES.get(t, t).lower() for t in tokens_en(lit, toks)}
                    real = {t.lower() for t in tokens_en(en, toks_en)}
                    if esperado != real:
                        err.append('el literal %r cambia de color en %s / %s / %s: %s → %s' % (
                            en, c, h, rng, sorted(esperado), sorted(real)))
        for (c2, h, sq) in DV_PARTIDAS:
            if c2 == c and not any(dv['sqref'] == sq for dv in info['hojas_detalle'].get(h, {}).get('dv', [])):
                err.append('DV_PARTIDAS cita una DV que no está en el censo: %s / %s' % (c, h))
    for es in FORMULAS_EN:
        if es not in patrones:
            err.append('patrón de mapas.FORMULAS_EN que no está en el censo: ' + es[:110])
    for k in PATRONES_SIN_CAMBIO - primeras:
        err.append('PATRONES_SIN_CAMBIO cita un patrón que no está en el censo: %r' % (k,))
    for (c, h, celda) in list(VALORES_EN) + list(POR_CELDA):
        if not any(info['corto'] == c and h in info['hojas'] for info in censo['libros'].values()):
            err.append('celda en una hoja inexistente: %s / %s / %s' % (c, h, celda))
    return err


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
    for x in e:
        print('ERROR', x)
    print('mapas.py: {} ficheros · {} pestañas · {} claves · {} fijos · {} patrones de fórmula EN · {} errores'.format(
        len(FICHEROS), len(HOJAS), len(CLAVES), len(FIJOS), len(FORMULAS_EN), len(e)))
    raise SystemExit(1 if e else 0)
