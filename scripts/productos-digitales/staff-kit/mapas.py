#!/usr/bin/env python3
"""
mapas.py — Restaurant Staff Scheduling Kit Pro (EN) · mapas ES→EN del Kit Gestión de Personal y Turnos v2.0.

SPEC: `scripts/productos-digitales/staff-kit/SPEC.md` (D1-Dn). Sesión Claude Code, 3-oct-2026.
Copia adaptada de `haccp-kit/mapas.py`. Importable SIN efectos (solo constantes y funciones). Ejecutado
como script corre el autotest (pestañas ≤ 31 caracteres y sin caracteres prohibidos, listas de DV ≤ 255
caracteres y sin comas dentro de un ítem, claves EN sin comillas dobles, códigos de turno únicos, reglas US
con fuente) y, si existe `censo_es.json` al lado, comprueba que TODAS las pestañas, listas de DV, literales
de fórmula, de CF y de DV personalizada, y patrones con comparación numérica del censo tienen su EN, y que
**ningún literal EN cambia de color** en su rango de CF (los CF del kit usan SEARCH, que casa subcadenas
sin distinguir mayúsculas: «cook» contiene «ok»).

    python3 mapas.py

Contenido:
  · PRODUCTO / SLUG / URL_PRODUCTO / MARCA_ES / MARCA_EN / FOOTER_ES / FOOTER_EN       (D1, D2, D18)
  · FICHEROS, TITULOS                         nombres de fichero y título interior (D5)
  · HOJAS, HOJAS_ES_POR_LIBRO                 pestañas ES→EN (D6)
  · CODIGOS, TURNOS_EN, LEYENDAS              códigos de turno y de ausencia, tabla «Shifts» (D8)
  · CLAVES                                    ítems de DV, literales de fórmula/CF/DV personalizada (D7)
  · DV_LISTAS_ESPECIALES, DV_NUEVAS           listas que cambian de ítems (D11) y DV nuevas (D8, D10)
  · FORMULAS_EN                               patrones de fórmula que cambian (D8, D10), ya con pestañas EN
  · PATRONES_SIN_CAMBIO                       patrones con comparación numérica que no cambian
  · PARAMETROS                                celdas nuevas (D10: fila 3 de «Time Log»)
  · VALORES_EN                                números y fechas que cambian (D9-D16)
  · POR_CELDA                                 textos EN fijados por celda (rótulos con decisión legal)
  · FORMATOS_EN                               formatos de número (moneda fuera, fecha y hora US) (D17, D18)
  · REGLAS_US                                 cifras US/UK con su fuente (SPEC §3)
"""
import datetime
import json
import os
import re
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))

# ==========================================================================
# 0. Producto (D1, D2, D18)
# ==========================================================================
PRODUCTO = 'Restaurant Staff Scheduling Kit Pro'
SLUG = 'restaurant-schedule-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_STAFF_SCHEDULING_KIT'
VERSION_ES = '2.0'
MARCA_ES = 'AI Chef Pro · aichef.pro — Kit Gestión de Personal y Turnos'
MARCA_EN = 'AI Chef Pro · aichef.pro — ' + PRODUCTO
FOOTER_ES = 'AI Chef Pro · aichef.pro · Página &P de &N'
FOOTER_EN = 'AI Chef Pro · aichef.pro · Page &P of &N'

# ==========================================================================
# 1. Ficheros y títulos (D5: intención de búsqueda US/UK)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-cuadrante-turnos-semanal.xlsx', '01-restaurant-schedule-template.xlsx'),
    ('02-control-horas-extras.xlsx', '02-overtime-tracker.xlsx'),
    ('03-coste-laboral-mensual.xlsx', '03-labor-cost-calculator.xlsx'),
    ('04-onboarding-nuevo-empleado.xlsx', '04-new-hire-onboarding-checklist.xlsx'),
    ('05-planificacion-vacaciones.xlsx', '05-pto-vacation-planner.xlsx'),
    ('06-evaluacion-desempeno.xlsx', '06-employee-performance-review.xlsx'),
    ('07-directorio-plantilla.xlsx', '07-employee-directory.xlsx'),
    ('BONUS-01-briefing-cambio-turno.xlsx', 'BONUS-01-shift-handover-log.xlsx'),
    ('BONUS-02-calculadora-plantilla-optima.xlsx', 'BONUS-02-restaurant-staffing-calculator.xlsx'),
])
LIBROS_ES = list(FICHEROS)

TITULOS = OrderedDict([
    ('01-restaurant-schedule-template.xlsx', 'Restaurant Schedule Template: Weekly & Monthly Staff Rota'),
    ('02-overtime-tracker.xlsx', 'Overtime Tracker & Time Log (FLSA 40-Hour Week)'),
    ('03-labor-cost-calculator.xlsx', 'Restaurant Labor Cost Calculator (Payroll & Labor %)'),
    ('04-new-hire-onboarding-checklist.xlsx', 'New Hire Onboarding Checklist'),
    ('05-pto-vacation-planner.xlsx', 'PTO & Vacation Planner'),
    ('06-employee-performance-review.xlsx', 'Employee Performance Review Form'),
    ('07-employee-directory.xlsx', 'Employee Directory & Expiry Tracker'),
    ('BONUS-01-shift-handover-log.xlsx', 'BONUS: Shift Handover Log (Manager Log Book)'),
    ('BONUS-02-restaurant-staffing-calculator.xlsx', 'BONUS: Restaurant Staffing Calculator'),
])

# Título interior: Instructions!B2 = «NN · título» (D5)
def titulo_interior(fichero_es):
    en = FICHEROS[fichero_es]
    t = TITULOS[en]
    return t if t.startswith('BONUS') else '%s · %s' % (en[:2], t)


# ==========================================================================
# 2. Pestañas (D6) — nombres ≤ 31 caracteres, sin []:*?/\
# ==========================================================================
HOJAS = OrderedDict([
    ('Instrucciones', 'Instructions'),
    ('Turnos', 'Shifts'),
    ('Cuadrante Semanal', 'Weekly Schedule'),
    ('Cuadrante Mensual', 'Monthly Schedule'),
    ('Registro Horas', 'Time Log'),
    ('Resumen Mensual', 'Monthly OT Summary'),
    ('Nóminas', 'Payroll'),
    ('Ratio Coste Laboral', 'Labor Cost Ratio'),
    ('Previsión por Servicio', 'Staffing Forecast'),
    ('Checklist Onboarding', 'Onboarding Checklist'),
    ('Calendario Anual', 'Annual Calendar'),
    ('Solicitudes', 'PTO Requests'),
    ('Saldo Vacaciones', 'PTO Balance'),
    ('Cobertura', 'Coverage'),
    ('Ficha Evaluación', 'Review Form'),
    ('Ficha (ejemplo relleno)', 'Review Form (Sample)'),
    ('Histórico', 'Review History'),
    ('Plantilla', 'Staff Directory'),
    ('Vencimientos', 'Expiry Alerts'),
    ('Briefing', 'Shift Handover'),
    ('Calculadora', 'Staffing Calculator'),
    ('Ratios por Tipo', 'Ratios by Concept'),
])

HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Turnos', 'Cuadrante Semanal', 'Cuadrante Mensual']),
    ('02', ['Instrucciones', 'Registro Horas', 'Resumen Mensual']),
    ('03', ['Instrucciones', 'Nóminas', 'Ratio Coste Laboral', 'Previsión por Servicio']),
    ('04', ['Instrucciones', 'Checklist Onboarding']),
    ('05', ['Instrucciones', 'Calendario Anual', 'Solicitudes', 'Saldo Vacaciones', 'Cobertura']),
    ('06', ['Instrucciones', 'Ficha Evaluación', 'Ficha (ejemplo relleno)', 'Histórico']),
    ('07', ['Instrucciones', 'Plantilla', 'Vencimientos']),
    ('B01', ['Instrucciones', 'Briefing']),
    ('B02', ['Instrucciones', 'Calculadora', 'Ratios por Tipo']),
])
HOJA_PROHIBIDOS = set('[]:*?/\\')

# ==========================================================================
# 3. Códigos de turno y de ausencia (D8). Un solo paso ES→EN (nunca encadenado: P→SP y T→PM a la vez).
#    01 (8 de turno, ancho 14) y 05 (4 de ausencia, columnas de 2,4 de ancho: 1 letra)
# ==========================================================================
CODIGOS = OrderedDict([
    ('M', 'AM'), ('T', 'PM'), ('N', 'N'), ('P', 'SP'), ('D', 'DBL'), ('L', 'OFF'),
    ('V', 'V'), ('B', 'S'), ('F', 'H'), ('PE', 'L'),
])
# Tabla «Shifts» A5:F12: código, descripción, inicio, fin (horas reales h:mm AM/PM), pausa (h). Mismos horarios del ES.
TURNOS_EN = [
    ('AM', 'AM shift', '7:00 AM', '3:00 PM', 0),
    ('PM', 'PM shift', '3:00 PM', '11:00 PM', 0),
    ('N', 'Night / overnight', '11:00 PM', '7:00 AM', 0),
    ('SP', 'Split shift', '10:00 AM', '11:00 PM', 4),
    ('DBL', 'Double', '7:00 AM', '11:00 PM', 0),
    ('OFF', 'Day off', None, None, 0),
    ('V', 'Vacation / PTO', None, None, 0),
    ('S', 'Sick', None, None, 0),
]
LEYENDA_TURNOS = ['AM=AM shift', 'PM=PM shift', 'N=Night', 'SP=Split', 'DBL=Double', 'OFF=Day off',
                  'V=Vacation/PTO', 'S=Sick']
LEYENDA_AUSENCIAS = ['V=Vacation/PTO', 'S=Sick', 'H=Holiday', 'L=Other leave']
LEYENDAS = OrderedDict([
    (('01', 'Cuadrante Semanal'), ('B3:I3', LEYENDA_TURNOS)),
    (('01', 'Cuadrante Mensual'), ('B3:I3', LEYENDA_TURNOS)),
    (('05', 'Calendario Anual'), ('B3:E3', LEYENDA_AUSENCIAS)),
    (('05', 'Cobertura'), ('A6:A8', ['AM · AM shift', 'PM · PM shift', 'N · Night (close)'])),
])

# ==========================================================================
# 4. CLAVES (D7): ítems de DV, literales de fórmula, de CF y de DV personalizada. Sin comillas dobles
#    (irían dentro de un literal de fórmula) ni comas en ítems de DV. Los tokens de CF (SEARCH) se
#    traducen 1:1 y el autotest exige que cada mensaje EN conserve EXACTAMENTE su color.
# ==========================================================================
CLAVES = OrderedDict()
CLAVES.update(CODIGOS)
CLAVES.update([('S', 'Y')])                                     # «S/N» (sí/no) del 01 → Y/N; «N» se queda
CLAVES.update([
    # semáforo genérico de los rangos K-P del 01, J del 02 y del 05 (SEARCH)
    ('⛔', '⛔'), ('⚠', '⚠'), ('EXCESO', 'EXCESS'), ('OK', 'OK'),
    # 01 Cuadrante
    (' h', ' h'), (' h/semana', ' h/week'),
    ('⛔ 0 días', '⛔ 0 days off'),
    ('⚠ 1 día (el ET pide 1,5, acumulable en 14 días — art. 37.1)', '⚠ 6 days on: a 7th day in a row is premium pay in CA'),
    ('⛔ jornada > ', '⛔ shift > '),
    # menores (revisión final): las reglas federales de horario son de MENORES DE 16 (29 CFR 570.35); 16-17 = estado
    ('⛔ jornada > 8 h (MENOR)', '⛔ > 8 h (under-16 cap)'),
    ('⛔ MENOR: trabajo nocturno y turno doble prohibidos (art. 6 ET)',
     '⛔ UNDER 16: no work after 7 PM (9 PM Jun 1–Labor Day), 29 CFR 570.35; 16-17: state law'),
    ('⚠ menor: sin horas extra (art. 6.3 ET)', '⚠ Minor: under 16, PM/SP end after 7 PM — check 570.35 + state law'),
    ('⛔ media +', '⛔ avg +'),
    # 02 Registro y Resumen
    ('⚠ escribe la hora con dos puntos: 9:00, no 9', '⚠ type the time with a colon: 9:00 AM, not 9'),
    ('⚠ entrada y salida iguales: la jornada no suma', '⚠ clock-in equals clock-out: the shift adds 0 h'),
    ('⚠ la pausa es mayor que la jornada', '⚠ the break is longer than the shift'),
    ('⚠ ese nombre no está en el «Resumen Mensual»: sus horas no se agregan',
     '⚠ name not in Monthly OT Summary: its hours are not added'),
    ('Voluntaria', 'Pre-approved'), ('Obligatoria', 'Manager request'), ('Fuerza mayor', 'Emergency / call-in'),
    ('Compensada con descanso', 'Not approved'), ('Complementaria (contrato parcial)', 'Shift cover'),
    ('EXCEDE', 'OVER BUDGET'), ('cerca del límite', 'near budget'), ('dentro', 'within budget'),
    ('⛔ EXCEDE (', '⛔ OVER BUDGET ('), (' h)', ' h)'), ('⚠ cerca del límite', '⚠ near budget'),
    ('✓ dentro', '✓ within budget'),
    # 03 y B02 (tipos de negocio = claves de VLOOKUP: iguales en la DV, la tabla y la celda de ejemplo)
    ('Fast Casual / Comida Rápida', 'Fast casual / QSR'), ('Restaurante Casual', 'Casual dining'),
    ('Fine Dining / Alta Cocina', 'Fine dining'), ('Catering / Eventos', 'Catering & events'),
    ('Cafetería / Brunch', 'Café / brunch'), ('Bar / Cocktails', 'Bar / cocktail bar'),
    ('Pizzería', 'Pizzeria'), ('Dark Kitchen / Delivery', 'Ghost kitchen / delivery'),
    ('Hotel (restaurante)', 'Hotel restaurant'), ('Heladería / Obrador', 'Ice cream shop / bakery'),
    ('El coste total de cada empleado incluye un ', "Each employee's total cost includes "),
    (' de cotización empresarial sobre el bruto ya prorrateado',
     ' employer payroll taxes & insurance on top of gross pay (estimate: check yours)'),
    ('— introduce las VENTAS netas del mes (B4)', "— enter this month's net SALES (B4)"),
    ('— aún no hay coste: vuelca las nóminas en la hoja «Nóminas»', '— no cost yet: enter your team in the Payroll tab'),
    ('⚠ ratio implausible: revisa que estén TODAS las nóminas', '⚠ implausible ratio: check that ALL payroll is entered'),
    ('EXCELENTE', 'EXCELLENT'), ('VIGILAR', 'WATCH'), ('ACCIÓN CORRECTIVA', 'CORRECTIVE ACTION'),
    ('🟢 EXCELENTE (por debajo de tu objetivo)', '🟢 EXCELLENT (below your target)'),
    ('🟡 VIGILAR (en el límite)', '🟡 WATCH (at the limit)'),
    ('🔴 ACCIÓN CORRECTIVA', '🔴 CORRECTIVE ACTION'),
    ('— introduce el ticket medio y elige tu tipo de negocio', '— enter your average check and pick your concept'),
    ('INFRADIMENSIONADA', 'UNDERSTAFFED'), ('SOBREDIMENSIONADA', 'OVERSTAFFED'), ('CORRECTAMENTE', 'RIGHT-SIZED'),
    ('⚠ SOBREDIMENSIONADA (+', '⚠ OVERSTAFFED (+'), ('🔴 INFRADIMENSIONADA (', '🔴 UNDERSTAFFED ('),
    ('✓ DIMENSIONADA CORRECTAMENTE', '✓ RIGHT-SIZED'),
    # 04
    # (✓ ✗ — sin letras: invariables)
    # 05
    ('Calendario de Vacaciones — Año ', 'PTO & Vacation Calendar — Year '),
    ('Alta', 'High'), ('Normal', 'Normal'), ('TEMP. ALTA', 'HIGH SEASON'),
    ('⚠ EXCESO', '⚠ EXCESS'), ('⛔ EXCESO en TEMP. ALTA', '⛔ EXCESS in HIGH SEASON'), ('⛔ TEMP. ALTA', '⛔ HIGH SEASON'),
    ('N/A', 'N/A'), ('Pendiente', 'Pending'), ('Aprobado', 'Approved'), ('Denegado', 'Denied'),
    ('⚠ fechas invertidas', '⚠ dates reversed'),
    ('⚠ ese nombre no está en el calendario', '⚠ name not in the calendar'),
    ('⚠ la fecha de alta es posterior al cierre del año', '⚠ hire date is after year-end'),
    ('⚠ la fecha de baja es anterior a la de alta', '⚠ end date is before hire date'),
    ('⛔ saldo negativo', '⛔ negative balance'), ('⚠ sin días disponibles', '⚠ no days left'),
    ('Jefe/a de cocina', 'Head chef'), ('Segundo/a de cocina', 'Sous chef'), ('Cocinero/a', 'Line cook'),
    ('Ayudante de cocina', 'Prep cook'), ('Pastelero/a', 'Pastry cook'), ('Jefe/a de sala', 'FOH manager'),
    ('Camarero/a', 'Server'), ('Ayudante de camarero/a', 'Busser'), ('Barman / Bartender', 'Bartender'),
    ('Sumiller', 'Sommelier'), ('Host / Recepción', 'Host'), ('Encargado/a', 'Shift manager'),
    ('Office', 'Dishwasher'), ('Repartidor/a', 'Delivery driver'),
    # 06
    ('DEFICIENTE', 'UNSATISFACTORY'), ('MEJORABLE', 'NEEDS IMPROVEMENT'), ('ADECUADO', 'MEETS EXPECTATIONS'),
    ('BUENO', 'GOOD'), ('puntúa al menos', 'score at least'),
    ('⭐ EXCELENTE', '⭐ EXCELLENT'), ('✓ BUENO', '✓ GOOD'), ('→ ADECUADO', '→ MEETS EXPECTATIONS'),
    ('⚠ MEJORABLE', '⚠ NEEDS IMPROVEMENT'), ('✗ DEFICIENTE', '✗ UNSATISFACTORY'),
    ('⚠ puntúa al menos 5 competencias', '⚠ score at least 5 competencies'), (' de 10', ' of 10'),
    ('↑ Mejora', '↑ Improving'), ('→ Estable', '→ Stable'), ('↓ Baja', '↓ Declining'),
    # 07
    ('Indefinido', 'Permanent'), ('Temporal', 'Temporary'), ('Prácticas', 'Intern'), ('Formación', 'Trainee'),
    ('Fijo-discontinuo', 'Seasonal'), ('Completa', 'Full-time'), ('Parcial', 'Part-time'),
    ('⚠ MENOR DE EDAD: sin nocturnidad ni horas extra (art. 6 ET)', '⚠ UNDER 18: child labor rules apply (29 CFR 570)'),
    ('VENCIDO', 'OVERDUE'), ('URGENTE', 'URGENT'), ('PRONTO', 'SOON'),
    ('❌ VENCIDO hace ', '❌ OVERDUE BY '), (' d', ' d'), ('🟢 OK', '🟢 OK'),
    # B01
    ('Media', 'Medium'), ('Baja', 'Low'), ('Urgente', 'Urgent'),
    ('CUADRA', 'BALANCED'), ('FALTAN', 'SHORT'), ('SOBRAN', 'OVER'),
    ('✓ CUADRA', '✓ BALANCED'), ('⛔ FALTAN ', '⛔ SHORT '), ('⚠ SOBRAN ', '⚠ OVER '), (' €', ''),
    ('CONFORME', 'IN RANGE'), ('FUERA DE RANGO', 'OUT OF RANGE'),
    ('✓ CONFORME', '✓ IN RANGE'), ('⛔ FUERA DE RANGO', '⛔ OUT OF RANGE'),
])

# ==========================================================================
# 5. DV (D8, D10, D11)
# ==========================================================================
# Listas que cambian de ítems: pagas/año (12, 14, 15) → periodos de pago/año (semanal, quincenal US, bimensual, mensual)
DV_LISTAS_ESPECIALES = OrderedDict([
    (('03', 'Nóminas', 'D5:D34'), ('"12,14,15"', '"52,26,24,12"')),
    (('B02', 'Calculadora', 'B10'), ('"12,14,15"', '"52,26,24,12"')),
])
# DV nuevas (excepción declarada: +4)
DV_NUEVAS = OrderedDict([
    (('01', 'Turnos', 'C5:D12'), ('time', 'between', '0', '0.999305555555556',
                                  'Type a time like 7:00 AM or 3:30 PM (not a plain 7).')),
    (('02', 'Registro Horas', 'B3'), ('whole', 'between', '1', '7',
                                      'FLSA workweek = any fixed 7 days you choose. 2 = Monday (default: the same week '
                                      'as the schedule grid in file 01) · 1 = Sunday … 7 = Saturday.')),
    (('02', 'Registro Horas', 'D3'), ('decimal', 'between', '1', '80',
                                      'Federal overtime starts after 40 hours in the workweek (FLSA). UK: type your '
                                      'contract hours.')),
    (('02', 'Registro Horas', 'F3'), ('decimal', 'between', '1', '24',
                                      'Leave blank under federal law. California: 8 (also AK, NV). Colorado: 12.')),
])

# Mensajes de DV fijados por aparición (revisión final): pisan el texto por id de textos_en SOLO en esa DV,
# cuando la cadena es compartida y el arreglo no vale para todas sus apariciones. (libro, hoja ES, sqref, campo)
DV_MENSAJES_EN = OrderedDict([
    # c0170 «…the summary formulas look for this exact text»: en 07 y B01 no hay fórmula que busque esos valores
    # (en 02 «Time Log»!I y 05 «PTO Requests»!G sí: allí se queda)
    (('07', 'Plantilla', 'D5:D34', 'error'), 'Pick a value from the list.'),
    (('07', 'Plantilla', 'G5:G34', 'error'), 'Pick a value from the list.'),
    (('B01', 'Briefing', 'C17:C22', 'error'), 'Pick a value from the list.'),
    (('B01', 'Briefing', 'A25:A30', 'error'), 'Pick a value from the list.'),
])

# ==========================================================================
# 6. Fórmulas que cambian (D8, D10). Clave = patrón ES del censo; valor = patrón EN FINAL (pestañas EN).
# ==========================================================================
def _descanso(c1, c2, fin, ini1, ini2):
    es = ('=IF(OR(${a}{{r}}="",${b}{{r}}="",${a}{{r}}=0,${b}{{r}}=0),"",IF(${f}{{r}}<=${i}{{r}},${j}{{r}}-${f}{{r}},'
          '24-${f}{{r}}+${j}{{r}}))').format(a=c1, b=c2, f=fin, i=ini1, j=ini2)
    en = ('=IF(OR(${a}{{r}}="",${b}{{r}}="",${a}{{r}}=0,${b}{{r}}=0),"",ROUND(IF(${f}{{r}}<=${i}{{r}},'
          '${j}{{r}}-${f}{{r}},1-${f}{{r}}+${j}{{r}})*24,2))').format(a=c1, b=c2, f=fin, i=ini1, j=ini2)
    return es, en


_WS = '($B{r}-MOD(WEEKDAY($B{r})-$B$3,7))'
_CRIT = '$A$5:$A$304,$A{r}&"",$B$5:$B$304,">="&' + _WS + ',$B$5:$B$304,"<="&$B{r}'
_DIARIA = 'IF($F$3="",0,MAX(0,$F{r}-$F$3))'
_SEMANA_REG = ('SUMIFS($F$5:$F$304,' + _CRIT + ')-IF($F$3="",0,SUMIFS($F$5:$F$304,' + _CRIT +
               ',$F$5:$F$304,">"&$F$3)-$F$3*COUNTIFS(' + _CRIT + ',$F$5:$F$304,">"&$F$3))')
H_FLSA = ('=IF(OR($A{r}="",$B{r}="",$F{r}=""),"",ROUND(' + _DIARIA + '+IF($D$3="",0,MIN($F{r}-' + _DIARIA +
          ',MAX(0,' + _SEMANA_REG + '-$D$3))),2))')

FORMULAS_EN = OrderedDict([
    # 01 Shifts!E: horas de turno con horas reales (fracción de día) → ×24
    ('=IF(OR($C{r}="",$D{r}=""),"",ROUND(MOD($D{r}-$C{r},24)-IF($F{r}="",0,$F{r}),2))',
     '=IF(OR($C{r}="",$D{r}=""),"",ROUND(MOD($D{r}-$C{r},1)*24-IF($F{r}="",0,$F{r}),2))'),
])
for _c in (('R', 'S', 'AF', 'Y', 'Z'), ('S', 'T', 'AG', 'Z', 'AA'), ('T', 'U', 'AH', 'AA', 'AB'),
           ('U', 'V', 'AI', 'AB', 'AC'), ('V', 'W', 'AJ', 'AC', 'AD'), ('W', 'X', 'AK', 'AD', 'AE')):
    _es, _en = _descanso(*_c)
    FORMULAS_EN[_es] = _en                                        # 01 Weekly Schedule!AM:AR (descanso, h)
FORMULAS_EN.update([
    # 02 Time Log!H: horas extra FLSA (semana laboral > D3) + regla diaria estatal opcional (F3), sin doble cómputo
    ('=IF(OR($F{r}="",$G{r}=""),"",MAX(0,$F{r}-$G{r}))', H_FLSA),
    # 02 Monthly OT Summary!C: horas extra NO aprobadas (se pagan igual: 29 CFR 785.11-.13)
    ("=IF($A{r}=\"\",\"\",ROUND(SUMIFS('Registro Horas'!$H$5:$H$304,'Registro Horas'!$A$5:$A$304,$A{r}&\"\","
     "'Registro Horas'!$I$5:$I$304,\"Fuerza mayor\")+SUMIFS('Registro Horas'!$H$5:$H$304,'Registro Horas'!$A$5:"
     "$A$304,$A{r}&\"\",'Registro Horas'!$I$5:$I$304,\"Compensada con descanso\")+SUMIFS('Registro Horas'!$H$5:"
     "$H$304,'Registro Horas'!$A$5:$A$304,$A{r}&\"\",'Registro Horas'!$I$5:$I$304,\"Complementaria (contrato "
     "parcial)\"),2))",
     "=IF($A{r}=\"\",\"\",ROUND(SUMIFS('Time Log'!$H$5:$H$304,'Time Log'!$A$5:$A$304,$A{r}&\"\","
     "'Time Log'!$I$5:$I$304,\"Not approved\"),2))"),
    # 02 Monthly OT Summary!G: coste = todas las horas extra × tarifa × recargo (sin «compensadas»: no existen en US privado)
    ("=IF($B{r}=\"\",\"\",ROUND(($B{r}-SUMIFS('Registro Horas'!$H$5:$H$304,'Registro Horas'!$A$5:$A$304,$A{r}&\"\","
     "'Registro Horas'!$I$5:$I$304,\"Compensada con descanso\")-SUMIFS('Registro Horas'!$H$5:$H$304,'Registro "
     "Horas'!$A$5:$A$304,$A{r}&\"\",'Registro Horas'!$I$5:$I$304,\"Complementaria (contrato parcial)\"))*$B$3*$D$3+"
     "SUMIFS('Registro Horas'!$H$5:$H$304,'Registro Horas'!$A$5:$A$304,$A{r}&\"\",'Registro Horas'!$I$5:$I$304,"
     "\"Complementaria (contrato parcial)\")*$B$3,2))",
     '=IF($B{r}="","",ROUND($B{r}*$B$3*$D$3,2))'),
])

# Patrones con comparación numérica que NO cambian (clave = libro, hoja, primera celda del patrón)
PATRONES_SIN_CAMBIO = {
    ('01', 'Cuadrante Semanal', 'L6'),        # días libres 0/1 (solo cambian los mensajes)
    ('01', 'Cuadrante Semanal', 'N6'),        # 8 h para menores = 29 CFR 570.35(a) (día sin colegio)
    ('02', 'Registro Horas', 'F5'), ('02', 'Registro Horas', 'J5'),
    ('03', 'Ratio Coste Laboral', 'B11'), ('03', 'Ratio Coste Laboral', 'B13'),
    ('04', 'Checklist Onboarding', 'C73'),
    ('05', 'Saldo Vacaciones', 'I5'), ('05', 'Cobertura', 'B47'),
    ('06', 'Ficha Evaluación', 'C23'), ('06', 'Ficha (ejemplo relleno)', 'C23'), ('06', 'Histórico', 'G5'),
    ('07', 'Vencimientos', 'C7'), ('07', 'Vencimientos', 'E7'), ('07', 'Vencimientos', 'G7'),
    ('07', 'Vencimientos', 'I7'),
    ('B01', 'Briefing', 'F49'), ('B02', 'Calculadora', 'B48'),
}

# ==========================================================================
# 7. Celdas nuevas (D10): parámetros FLSA en la fila 3 de «Time Log» (vacía en el ES). Verdes y desbloqueadas.
# ==========================================================================
PARAMETROS = OrderedDict([
    (('02', 'Registro Horas', 'A3'), ('Workweek starts (1=Sun, 2=Mon):', None)),
    (('02', 'Registro Horas', 'B3'), (None, 2)),                 # lunes = la rejilla del 01 (lunes-domingo)
    (('02', 'Registro Horas', 'C3'), ('Weekly OT after (h):', None)),
    (('02', 'Registro Horas', 'D3'), (None, 40)),
    (('02', 'Registro Horas', 'E3'), ('Daily OT after (h):', None)),
    (('02', 'Registro Horas', 'F3'), (None, None)),               # vacía = regla federal (sin OT diaria)
])
CELDAS_VERDES_NUEVAS = [('02', 'Registro Horas', 'B3'), ('02', 'Registro Horas', 'D3'), ('02', 'Registro Horas', 'F3')]

# ==========================================================================
# 8. Números y fechas que cambian (D9-D16). (libro, hoja, celda) → valor EN
# ==========================================================================
VALORES_EN = OrderedDict([
    # 01 parámetros: alerta de turno largo (criterio del kit) y descanso «clopening» (Fair Workweek)
    (('01', 'Turnos', 'B2'), 10), (('01', 'Turnos', 'B3'), 10),
    # 02 tarifa de muestra, recargo FLSA, presupuesto anual de horas extra (criterio del kit)
    (('02', 'Resumen Mensual', 'B3'), 15), (('02', 'Resumen Mensual', 'D3'), 1.5), (('02', 'Resumen Mensual', 'F3'), 80),
    # 03 coste de empresa (estimación), semanas trabajadas (estimación), periodos de pago
    (('03', 'Nóminas', 'C2'), 0.10), (('03', 'Nóminas', 'F2'), 50), (('03', 'Nóminas', 'D5:D34'), 26),
    (('03', 'Previsión por Servicio', 'B14'), 1400), (('03', 'Previsión por Servicio', 'B15'), 26),
    (('03', 'Previsión por Servicio', 'B16'), 0.10),
    # 05 derecho anual en días naturales (14 = dos semanas) y semana 1 en domingo (semana laboral US por defecto)
    (('05', 'Saldo Vacaciones', 'B2'), 14), (('05', 'Calendario Anual', 'B5'), datetime.date(2027, 1, 3)),
    # B01 rangos de temperatura en °F (FDA Food Code 2022 §3-501.16: 41 °F frío, 135 °F caliente)
    (('B01', 'Briefing', 'B47'), 5),
    (('B01', 'Briefing', 'C56'), 32), (('B01', 'Briefing', 'D56'), 41),
    (('B01', 'Briefing', 'C57'), -22), (('B01', 'Briefing', 'D57'), 0),
    (('B01', 'Briefing', 'C58'), 32), (('B01', 'Briefing', 'D58'), 41),
    (('B01', 'Briefing', 'C59'), 135), (('B01', 'Briefing', 'D59'), 194),
    (('B01', 'Briefing', 'C60'), 135), (('B01', 'Briefing', 'D60'), 194),
    # B02 salario medio por periodo de pago, periodos, coste de empresa, ticket medio
    (('B02', 'Calculadora', 'B9'), 1400), (('B02', 'Calculadora', 'B10'), 26), (('B02', 'Calculadora', 'B11'), 0.10),
    (('B02', 'Calculadora', 'B15'), 35),
])

# ==========================================================================
# 9. Textos fijados por celda: rótulos que llevan una decisión legal o de mercado (no van a los traductores)
# ==========================================================================
POR_CELDA = OrderedDict([
    # 01 Shifts
    (('01', 'Turnos', 'A1'), 'Shifts & limits: edit them here, they apply to the whole kit'),
    (('01', 'Turnos', 'A2'), 'Long-shift alert after (h):'),
    (('01', 'Turnos', 'C2'), 'Kit rule (no federal daily cap)'),
    (('01', 'Turnos', 'A3'), 'Minimum rest between shifts (h):'),
    (('01', 'Turnos', 'C3'), 'Fair Workweek "clopening" rule'),
    (('01', 'Turnos', 'C4'), 'Start time'), (('01', 'Turnos', 'D4'), 'End time'),
    (('01', 'Cuadrante Semanal', 'J5'), 'Max hours/week (OT after 40)'),
    (('01', 'Cuadrante Semanal', 'O5'), 'Under 18? (Y/N)'),
    (('01', 'Cuadrante Mensual', 'I169'), 'Max hours/week (OT after 40)'),
    # 02 Monthly OT Summary (rótulos con la decisión D10)
    (('02', 'Resumen Mensual', 'A3'), 'Hourly rate for the OT cost estimate:'),
    (('02', 'Resumen Mensual', 'C3'), 'Overtime multiplier (FLSA: 1.5×):'),
    (('02', 'Resumen Mensual', 'E3'), 'Annual OT budget per person (h):'),
    (('02', 'Resumen Mensual', 'B5'), 'Total OT hours (this copy)'),
    (('02', 'Resumen Mensual', 'C5'), 'Unapproved OT hours (still payable)'),
    (('02', 'Resumen Mensual', 'D5'), 'Approved OT hours'),
    (('02', 'Resumen Mensual', 'E5'), 'OT hours year to date'),
    (('02', 'Resumen Mensual', 'F5'), 'Status vs. annual OT budget'),
    (('02', 'Resumen Mensual', 'G5'), 'Overtime cost'),
    (('02', 'Resumen Mensual', 'H5'), 'Worked − scheduled hours (this copy)'),
    (('02', 'Registro Horas', 'G4'), 'Scheduled hours'),
    (('02', 'Registro Horas', 'H4'), 'OT hours (FLSA)'),
    (('02', 'Registro Horas', 'I4'), 'OT type'),
    # 03 Payroll
    (('03', 'Nóminas', 'A2'), 'Employer payroll taxes & insurance (%):'),
    (('03', 'Nóminas', 'E2'), 'Weeks actually worked per year:'),
    (('03', 'Nóminas', 'B4'), 'Position'),
    (('03', 'Nóminas', 'C4'), 'Gross pay per pay period'),
    (('03', 'Nóminas', 'D4'), 'Pay periods per year'),
    (('03', 'Nóminas', 'E4'), 'Gross pay per month'),
    (('03', 'Nóminas', 'F4'), 'Employer taxes & insurance'),
    (('03', 'Nóminas', 'G4'), 'Total cost per month'),
    (('03', 'Nóminas', 'H4'), 'Scheduled hours per week'),
    (('03', 'Nóminas', 'I4'), 'Cost per hour worked'),
    (('03', 'Previsión por Servicio', 'A14'), 'Average gross pay per pay period:'),
    (('03', 'Previsión por Servicio', 'A15'), 'Pay periods per year:'),
    (('03', 'Previsión por Servicio', 'A16'), 'Employer payroll taxes & insurance (%):'),
    # 04 tareas con plazo legal US (el plazo del ES de cada fila se respeta: H = alta + desfase)
    (('04', 'Checklist Onboarding', 'B7'), 'Signed offer letter / employment agreement'),
    (('04', 'Checklist Onboarding', 'B8'), 'ID and work-authorization documents for Form I-9 (List A, or List B + C)'),
    (('04', 'Checklist Onboarding', 'B9'), 'Direct deposit authorization (bank details for payroll)'),
    (('04', 'Checklist Onboarding', 'B10'), 'Form I-9 Section 1: the employee completes it NO LATER THAN the first day of work (8 CFR 274a.2)'),
    (('04', 'Checklist Onboarding', 'B11'), 'Form I-9 Section 2: examine the original documents (legal limit: 3 business days after the first day)'),
    (('04', 'Checklist Onboarding', 'B12'), 'Employee handbook acknowledgment signed'),
    (('04', 'Checklist Onboarding', 'B14'), 'Written wage notice: pay rate, payday, OT rate and tip credit if used (required in states such as CA and NY)'),
    (('04', 'Checklist Onboarding', 'B15'), 'Time clock: how to clock in and out, breaks and meal periods'),
    (('04', 'Checklist Onboarding', 'B17'), 'State new-hire report filed (federal limit: 20 days after hire; some states sooner)'),
    (('04', 'Checklist Onboarding', 'B18'), "Workers' comp: injury-reporting procedure and required workplace posters shown"),
    (('04', 'Checklist Onboarding', 'B19'), 'Form W-4 and state withholding form signed (needed for the first payroll)'),
    (('04', 'Checklist Onboarding', 'B23'), 'Food handler card valid (required in some states and counties)'),
    (('04', 'Checklist Onboarding', 'B24'), 'Food safety / HACCP procedures of the restaurant'),
    (('04', 'Checklist Onboarding', 'B25'), 'Allergen awareness: the 9 major US allergens (UK: 14)'),
    (('04', 'Checklist Onboarding', 'B26'), 'Workplace safety (OSHA): knives, burns, slips, lifting, chemicals and SDS'),
    (('04', 'Checklist Onboarding', 'B28'), 'Anti-harassment policy and how to report (training required in CA, NY, IL and others)'),
    (('04', 'Checklist Onboarding', 'B30'), 'Alcohol server training (TIPS / ServSafe Alcohol) for servers and bartenders, where required'),
    # 05 semana 1 en domingo (D12)
    (('05', 'Calendario Anual', 'A5'), 'Week 1 starts on (Sunday) →'),
    (('05', 'Saldo Vacaciones', 'A2'), 'PTO days per year (calendar days):'),
    # 07 Staff Directory y Expiry Alerts
    (('07', 'Plantilla', 'B4'), 'Employee ID'),
    (('07', 'Plantilla', 'D4'), 'Employment type'),
    (('07', 'Plantilla', 'F4'), 'FLSA status (non-exempt / exempt)'),
    (('07', 'Plantilla', 'G4'), 'Full / part-time'),
    (('07', 'Plantilla', 'I4'), 'Pay type (hourly / salaried / tipped)'),
    (('07', 'Plantilla', 'J4'), 'SSN (last 4 digits only)'),
    (('07', 'Plantilla', 'K4'), 'Hire date'),
    (('07', 'Plantilla', 'L4'), 'End date (seasonal / temp)'),
    (('07', 'Plantilla', 'M4'), 'Introductory period ends'),
    (('07', 'Plantilla', 'N4'), 'Food handler card expires'),
    (('07', 'Plantilla', 'O4'), 'Alcohol server cert expires'),
    (('07', 'Plantilla', 'P4'), 'Pay rate'),
    (('07', 'Vencimientos', 'B6'), 'End date (seasonal / temp)'),
    (('07', 'Vencimientos', 'D6'), 'Introductory period ends'),
    (('07', 'Vencimientos', 'F6'), 'Food handler card'),
    (('07', 'Vencimientos', 'H6'), 'Alcohol server cert'),
    # B01 Shift Handover (°F)
    (('B01', 'Briefing', 'B55'), 'Temperature (°F)'), (('B01', 'Briefing', 'C55'), 'Min (°F)'),
    (('B01', 'Briefing', 'D55'), 'Max (°F)'),
    (('B01', 'Briefing', 'D48'), 'Cash sales per POS Z report'),
    # B02 Staffing Calculator
    (('B02', 'Calculadora', 'A9'), 'Average gross pay per pay period (team member, full-time):'),
    (('B02', 'Calculadora', 'A10'), 'Pay periods per year:'),
    (('B02', 'Calculadora', 'A11'), 'Employer payroll taxes & insurance (%):'),
    (('B02', 'Calculadora', 'A15'), 'Average check per cover, before sales tax:'),
])

# ==========================================================================
# 10. Formatos (D17, D18)
# ==========================================================================
FORMATOS_EN = OrderedDict([
    ('#,##0.00 €', '#,##0.00'), ('€#,##0.00', '#,##0.00'),
    ('dd/mm/yyyy', 'NUMFMT14'),                  # fecha corta del sistema (m/d/yyyy en US)
    ('dd/mm', 'm/d'),
    ('hh:mm', 'h:mm AM/PM'),
])
FMT_TURNOS = 'h:mm AM/PM;;'                    # Shifts!C5:D12: cero (día libre) en blanco

# Ajuste de texto (revisión final): rótulos que se cortaban. (libro, hoja ES, rango) → ajuste + alto de fila
# calculado (nunca menor que el que ya tenga la fila). Así se ven enteros también en visores que no autoajustan.
AJUSTE_TEXTO = [
    ('04', 'Checklist Onboarding', 'B7:B68'),
    ('B02', 'Calculadora', 'A9'), ('B02', 'Calculadora', 'A12'),
    ('05', 'Cobertura', 'A48'),
    ('05', 'Calendario Anual', 'A37:A39'),
]

# Nombre corto con el que un texto cita otro fichero del kit: file NN "nombre" (un solo nivel, sin subtítulo)
NOMBRES_CITA = OrderedDict([
    ('01', 'Restaurant Schedule Template'), ('02', 'Overtime Tracker & Time Log'),
    ('03', 'Restaurant Labor Cost Calculator'), ('04', 'New Hire Onboarding Checklist'),
    ('05', 'PTO & Vacation Planner'), ('06', 'Employee Performance Review Form'),
    ('07', 'Employee Directory & Expiry Tracker'),
])

# ==========================================================================
# 11. Reglas US/UK con fuente (SPEC §3). clave → (valor, fuente). [estimado] / [criterio del kit] = no es norma.
# ==========================================================================
REGLAS_US = OrderedDict([
    ('ot_semanal', ('40 h/workweek, 1.5× regular rate', 'FLSA 29 U.S.C. 207(a)(1); dol.gov/agencies/whd/overtime')),
    ('ot_diario_ca', ('8 h/day 1.5×, 12 h/day 2×', 'Cal. Labor Code §510(a)')),
    ('ot_no_aprobada', ('se paga igual', '29 CFR 785.11-785.13')),
    ('comp_time', ('no en empresa privada', 'FLSA 29 U.S.C. 207(o) (solo sector público)')),
    ('tip_credit_ot', ('OT sobre el salario mínimo completo', '29 CFR 531.60; DOL Fact Sheet #15')),
    ('descanso_turnos', ('10 h (NYC 11 h)', 'ORS 653.442; Seattle SMC 14.22.035; NYC Admin. Code §20-1231')),
    ('turno_largo', ('10 h', '[criterio del kit] la FLSA no fija máximo diario para adultos (dol.gov/agencies/whd/flsa)')),
    ('menores', ('< 16: 8 h día sin colegio, nada después de 7 PM (9 PM jun-Labor Day)', '29 CFR 570.35')),
    ('menores_18', ('< 18: ocupaciones peligrosas (cortafiambres, amasadoras)', '29 CFR 570.50-570.68')),
    ('dia_descanso', ('1 día de 7; 7.º día seguido con recargo', 'Cal. Labor Code §§551-552 y 510(a)')),
    ('fica', ('7.65 % (6.2 % SS + 1.45 % Medicare)', 'IRS Publication 15 (Circular E)')),
    ('futa', ('6.0 % − 5.4 % de crédito = 0.6 % sobre los primeros $7,000', 'IRS Topic 759')),
    ('coste_empresa', ('10 %', '[estimado] FICA 7.65 % + FUTA/SUTA + workers\' comp efectivos')),
    ('periodos_pago', ('52/26/24/12, 26 por defecto', 'BLS Current Employment Statistics, «Length of pay periods»')),
    ('semanas', ('50', '[estimado] 52 − 2 semanas pagadas sin trabajar; UK 52 − 5.6 (gov.uk/holiday-entitlement-rights)')),
    ('pto', ('14 días naturales', '[criterio del kit] sin obligación federal: dol.gov/general/topic/workhours/vacation_leave')),
    ('i9', ('S1 el primer día; S2 en 3 días hábiles', '8 CFR 274a.2(b)(1)(i)-(ii)')),
    ('new_hire', ('20 días', '42 U.S.C. 653a(b)(2)')),
    ('i9_conservar', ('3 años desde el alta o 1 desde la baja, lo que sea más tarde', '8 CFR 274a.2(b)(2)(i)(A)')),
    ('nominas_conservar', ('3 años; fichajes 2', '29 CFR 516.5 y 516.6')),
    ('temp', ('41 °F frío · 135 °F caliente', 'FDA Food Code 2022 §3-501.16')),
    ('uk_wtr', ('48 h media; 11 h entre jornadas; 24 h semanales; 20 min > 6 h', 'Working Time Regulations 1998 regs. 4, 10, 11, 12')),
    ('uk_vacaciones', ('5.6 semanas', 'gov.uk/holiday-entitlement-rights')),
    ('uk_ot', ('sin recargo legal', 'gov.uk/overtime-your-rights')),
    ('uk_ni', ('15 % sobre £5,000/año + 3 % pensión', 'gov.uk «Rates and thresholds for employers 2025 to 2026»')),
])


# ==========================================================================
# 12. utilidades
# ==========================================================================
def patron(formula):
    """Normaliza las filas de las referencias de celda a {r} (las referencias absolutas $X$n se respetan)."""
    return re.sub(r'(?<![A-Za-z_$])(\$?[A-Z]{1,3})(?<!\$)(\d+)(?![\d(])',
                  lambda m: m.group(1) + '{r}', formula)


def dv_lista(items):
    return '"' + ','.join(items) + '"'


RX_LIT = re.compile(r'"((?:[^"]|"")*)"')


def necesita_clave(lit):
    """Un literal va a CLAVES si lleva letras o €; los demás (formatos, comparadores, emojis sueltos) no cambian."""
    return any(ch.isalpha() for ch in lit) or '€' in lit


def tokens_en(texto, tokens):
    t = texto.lower()
    return {k for k in tokens if k.lower() in t}


# ==========================================================================
# 13. Autotest y cruce con el censo
# ==========================================================================
def autotest():
    err = []
    for es, en in HOJAS.items():
        if len(en) > 31 or set(en) & HOJA_PROHIBIDOS or en.startswith("'"):
            err.append('pestaña inválida: ' + en)
    for f, hs in HOJAS_ES_POR_LIBRO.items():
        ens = [HOJAS[h] for h in hs]
        if len(set(ens)) != len(ens):
            err.append('pestañas EN duplicadas en ' + f)
    if len(FICHEROS) != 9 or len(set(FICHEROS.values())) != 9:
        err.append('FICHEROS debe tener 9 nombres EN distintos')
    for es, en in FICHEROS.items():
        if en not in TITULOS:
            err.append('fichero sin título: ' + en)
        if not re.fullmatch(r'(BONUS-)?\d{2}-[a-z0-9-]+\.xlsx', en) or es.split('-')[0] != en.split('-')[0]:
            err.append('fichero EN mal formado: ' + en)
    for k, v in CLAVES.items():
        if '"' in v:
            err.append('comilla doble dentro de una clave EN: %r' % v)
        if re.search(r'[áíóúñÁÍÓÚÑ¿¡]', v):                   # «é» se admite: «Café / brunch»
            err.append('español en una clave EN: %r' % v)
    if len(set(CODIGOS.values())) != len(CODIGOS) or set(CODIGOS.values()) & {'Y'}:
        err.append('códigos EN repetidos o que chocan con Y/N')
    for c in ('V', 'S', 'H', 'L'):
        if len(c) > 1:
            err.append('código de ausencia de más de una letra (columnas de 2,4): ' + c)
    if [t[0] for t in TURNOS_EN] != [CODIGOS[c] for c in 'MTNPDLVB']:
        err.append('TURNOS_EN no sigue el orden de la tabla ES (M T N P D L V B)')
    for k, (es, en) in DV_LISTAS_ESPECIALES.items():
        if len(en) > 255:
            err.append('DV especial > 255: %r' % (k,))
    for k, v in POR_CELDA.items():
        if re.search(r'[áéíóúñ¿¡]|\bde\b|\by\b|€', v):
            err.append('POR_CELDA con español o €: %r' % (k,))
    for es, en in FORMULAS_EN.items():
        if re.search(r'[áéíóúñÁÉÍÓÚÑ¿¡]', en):
            err.append('español en FORMULAS_EN: ' + en[:60])
        for h in HOJAS:
            if h != HOJAS[h] and ("'%s'!" % h in en or re.search(r'(?<![\w\'])%s!' % re.escape(h), en)):
                err.append('pestaña ES dentro de FORMULAS_EN: ' + h)
    for k, (val, fuente) in REGLAS_US.items():
        if not fuente:
            err.append('regla sin fuente: ' + k)
    # límites de Excel en la DV: título ≤ 32, mensaje ≤ 255 (más largo = el fichero «se repara» al abrir)
    for k, v in DV_MENSAJES_EN.items():
        lim = 32 if k[3].endswith('Title') else 255
        if k[3] not in ('error', 'errorTitle', 'prompt', 'promptTitle') or len(v) > lim:
            err.append('DV_MENSAJES_EN inválido o > %d: %r' % (lim, k))
    for k, v in DV_NUEVAS.items():
        if len(v[4]) > 255:
            err.append('DV_NUEVAS: mensaje > 255 en %r' % (k,))
    for k, v in CLAVES.items():
        if len(v) > 255:
            err.append('clave EN > 255 (literal de fórmula): %r' % v[:40])
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
                esp = DV_LISTAS_ESPECIALES.get((c, h, dv['sqref']))
                if esp:
                    if esp[0] != f1:
                        err.append('DV especial cambiada en el ES: %s / %s / %s' % (c, h, dv['sqref']))
                    continue
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
    for es in FORMULAS_EN:
        if es not in patrones:
            err.append('patrón de mapas.FORMULAS_EN que no está en el censo: ' + es[:110])
    for k in PATRONES_SIN_CAMBIO - primeras:
        err.append('PATRONES_SIN_CAMBIO cita un patrón que no está en el censo: %r' % (k,))
    for (c, h, celda) in list(VALORES_EN) + list(POR_CELDA) + list(PARAMETROS):
        if not any(info['corto'] == c and h in info['hojas'] for info in censo['libros'].values()):
            err.append('celda en una hoja inexistente: %s / %s / %s' % (c, h, celda))
    for (c, h, sq, campo) in DV_MENSAJES_EN:
        info = next(i for i in censo['libros'].values() if i['corto'] == c)
        if not any(dv['sqref'] == sq for dv in info['hojas_detalle'].get(h, {}).get('dv', [])):
            err.append('DV_MENSAJES_EN cita una DV que no está en el censo: %s / %s / %s' % (c, h, sq))
    for (c, h, rg) in AJUSTE_TEXTO:
        if not any(info['corto'] == c and h in info['hojas'] for info in censo['libros'].values()):
            err.append('AJUSTE_TEXTO en una hoja inexistente: %s / %s / %s' % (c, h, rg))
    for (c, h, sq) in list(DV_NUEVAS):
        info = next(i for i in censo['libros'].values() if i['corto'] == c)
        for dv in info['hojas_detalle'][h]['dv']:
            if _celdas(dv['sqref']) & _celdas(sq):
                err.append('DV nueva solapa una DV del ES: %s / %s / %s' % (c, h, sq))
    return err


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
    for x in e:
        print('ERROR', x)
    print('mapas.py: {} ficheros · {} pestañas · {} claves · {} patrones de fórmula EN · {} errores'.format(
        len(FICHEROS), len(HOJAS), len(CLAVES), len(FORMULAS_EN), len(e)))
    raise SystemExit(1 if e else 0)
