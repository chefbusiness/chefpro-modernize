#!/usr/bin/env python3
"""
mapas.py — Restaurant Checklists Kit Pro (EN) · mapas ES→EN del Kit de Tareas Recurrentes v2.0 (`kit-tareas`).

SPEC: `scripts/productos-digitales/checklists-kit/SPEC.md` (D1-Dn). Sesión Claude Code, 17-oct-2026.
Copia adaptada de `staff-kit/mapas.py`. Importable SIN efectos (solo constantes y funciones). Ejecutado como
script corre el autotest (pestañas ≤ 31 caracteres y sin caracteres prohibidos, nombres EN únicos por libro,
claves sin comillas, horas a reloj de 12 h, denominaciones coherentes, reglas US con fuente, textos fijados sin
español) y, si existe `censo_es.json` al lado, comprueba que TODAS las pestañas, listas de DV, literales de
fórmula y de CF y patrones con comparación numérica del censo tienen su decisión, que cada celda citada por
`POR_CELDA`, `ADAPTAR`, `FORMULAS_POR_CELDA` existe en el ES con texto o fórmula, y que **ningún literal EN
cambia de color** en su rango de CF.

    python3 mapas.py

Contenido:
  · PRODUCTO / SLUG / URL_PRODUCTO / MARCA_ES / MARCA_EN / FOOTER_ES / FOOTER_EN       (D1, D2, D19)
  · FICHEROS, TITULOS, NOMBRES_CITA            nombres de fichero, título interior y cita corta (D5)
  · HOJAS, HOJAS_ES_POR_LIBRO                  pestañas ES→EN (D6)
  · GLOSARIO                                   celdas cortas repetidas: cabeceras, zonas, puestos, cuándo (D7, D8)
  · hora_us, RX_HORA_CELDA                     «07:00» → «7:00 AM» (D9)
  · DENOMINACIONES, FORMULAS_POR_CELDA         recuento de caja en dólares (D12)
  · CALENDARIO                                 BONUS-02: 22 fechas US (D14)
  · POR_CELDA                                  textos EN fijados por celda (rótulos con decisión legal o de caja)
  · ADAPTAR                                    instrucciones de adaptación para los traductores, por celda
  · CLAVES, PATRONES_SIN_CAMBIO                literales de fórmula/CF (D7)
  · FORMATOS_EN                                formatos de número (moneda fuera) (D13)
  · REGLAS_US                                  cifras US/UK con su fuente (SPEC §3)
"""
import json
import os
import re
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))

# ==========================================================================
# 0. Producto (D1, D2, D19)
# ==========================================================================
PRODUCTO = 'Restaurant Checklists Kit Pro'
TITULO_SEO = 'Restaurant Checklists Kit Pro: Opening, Closing & Cleaning Checklist Templates for Excel'
SLUG = 'restaurant-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_RESTAURANT_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
VERSION_ES = '2.0'
MARCA_ES = '— Kit de Tareas Recurrentes · Restaurante Casual · AI Chef Pro · aichef.pro'
MARCA_EN = '— ' + PRODUCTO + ' · AI Chef Pro · aichef.pro'
FOOTER_ES = 'AI Chef Pro · aichef.pro · Página &P de &N'
FOOTER_EN = 'AI Chef Pro · aichef.pro · Page &P of &N'
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v2.0'),
    ('keywords', 'restaurant opening checklist, restaurant closing checklist, restaurant cleaning checklist, '
                 'AI Chef Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

# ==========================================================================
# 1. Ficheros y títulos (D5: intención de búsqueda US; DataForSEO 17-oct)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-apertura-cierre.xlsx', '01-opening-closing-checklists-kitchen-foh-bar.xlsx'),
    ('02-partidas-cocina.xlsx', '02-kitchen-station-checklists.xlsx'),
    ('03-tareas-manager.xlsx', '03-restaurant-manager-checklist.xlsx'),
    ('04-tareas-perfiles.xlsx', '04-daily-duties-side-work-by-role.xlsx'),
    ('05-tareas-semanales-mensuales.xlsx', '05-restaurant-cleaning-schedule.xlsx'),
    ('06-eventos-festivos.xlsx', '06-event-holiday-checklists.xlsx'),
    ('07-plantilla-personalizable.xlsx', '07-blank-checklist-template.xlsx'),
    ('08-apertura-cierre-negocio.xlsx', '08-restaurant-opening-closing-checklist.xlsx'),
    ('09-apertura-cierre-caja.xlsx', '09-cash-drawer-opening-closing.xlsx'),
    ('BONUS-01-briefing-servicio.xlsx', 'BONUS-01-pre-shift-meeting-template.xlsx'),
    ('BONUS-02-calendario-anual-tareas.xlsx', 'BONUS-02-restaurant-holiday-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)

TITULOS = OrderedDict([
    ('01-opening-closing-checklists-kitchen-foh-bar.xlsx', 'Opening & Closing Checklists: Kitchen, FOH & Bar'),
    ('02-kitchen-station-checklists.xlsx', 'Kitchen Checklists by Station (Hot Line, Cold Station, Mise en Place)'),
    ('03-restaurant-manager-checklist.xlsx', 'Restaurant Manager Checklist: Daily, Weekly, Monthly & Shift Handover'),
    ('04-daily-duties-side-work-by-role.xlsx', 'Daily Duties & Side Work Checklists by Role'),
    ('05-restaurant-cleaning-schedule.xlsx', 'Restaurant Cleaning Schedule & Maintenance Checklists'),
    ('06-event-holiday-checklists.xlsx', 'Event & Holiday Checklists'),
    ('07-blank-checklist-template.xlsx', 'Blank Restaurant Checklist Template (Editable)'),
    ('08-restaurant-opening-closing-checklist.xlsx', 'Restaurant Opening & Closing Checklist (Whole Building)'),
    ('09-cash-drawer-opening-closing.xlsx', 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log'),
    ('BONUS-01-pre-shift-meeting-template.xlsx', 'BONUS: Pre-Shift Meeting Template (Line-Up Notes)'),
    ('BONUS-02-restaurant-holiday-calendar.xlsx', 'BONUS: Restaurant Holiday & Events Calendar (US)'),
])


def titulo_interior(fichero_es):
    """Instructions!B2 = «NN · título» (D5); los bonus ya empiezan por «BONUS:»."""
    en = FICHEROS[fichero_es]
    t = TITULOS[en]
    return t if t.startswith('BONUS') else '%s · %s' % (en[:2], t)


# Cita de otro fichero dentro de un texto: el nombre de fichero EN, tal cual (los textos ES citan el .xlsx).
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

# ==========================================================================
# 2. Pestañas (D6) — ≤ 31 caracteres, sin []:*?/\ ni apóstrofo al principio o al final
# ==========================================================================
HOJAS = OrderedDict([
    ('Instrucciones', 'Instructions'),
    ('Apertura Cocina', 'Kitchen Opening'), ('Apertura Sala', 'FOH Opening'), ('Apertura Barra', 'Bar Opening'),
    ('Cierre Cocina', 'Kitchen Closing'), ('Cierre Sala', 'FOH Closing'), ('Cierre Barra', 'Bar Closing'),
    ('Calientes', 'Hot Line'), ('Fríos', 'Cold Station'), ('Mise en Place', 'Mise en Place'),
    ('Diario Manager', 'Manager Daily'), ('Semanal Manager', 'Manager Weekly'),
    ('Mensual Manager', 'Manager Monthly'), ('Handover Turno', 'Shift Handover'),
    ('Jefe de Cocina', 'Head Chef'), ('Sous Chef', 'Sous Chef'), ('Jefe de Sala', 'FOH Manager'),
    ('Camarero', 'Server'), ('Barman', 'Bartender'),
    ('Limpieza Semanal', 'Weekly Deep Clean'), ('FIFO Semanal', 'Weekly FIFO Check'),
    ('Mantenimiento Mensual', 'Monthly Maintenance'), ('Trimestral y Anual', 'Quarterly & Annual'),
    ('Pre-Evento', 'Pre-Event'), ('San Valentín', "Valentine's Day"), ('Navidad', 'Christmas & NYE'),
    ('Temporada Terraza', 'Patio Season'),
    ('Por Franja Horaria', 'By Time of Day'), ('Por Área', 'By Area'), ('Por Perfil', 'By Role'),
    ('Apertura del Negocio', 'Restaurant Opening'), ('Cierre del Negocio', 'Restaurant Closing'),
    ('Apertura de Caja', 'Cash Drawer Opening'), ('Cierre de Caja', 'Cash Drawer Closing'),
    ('Registro Mensual', 'Monthly Cash Log'),
    ('Briefing', 'Pre-Shift Meeting'),
    ('Calendario Anual', 'Holiday Calendar'),
])

HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Apertura Cocina', 'Apertura Sala', 'Apertura Barra', 'Cierre Cocina', 'Cierre Sala',
            'Cierre Barra']),
    ('02', ['Instrucciones', 'Calientes', 'Fríos', 'Mise en Place']),
    ('03', ['Instrucciones', 'Diario Manager', 'Semanal Manager', 'Mensual Manager', 'Handover Turno']),
    ('04', ['Instrucciones', 'Jefe de Cocina', 'Sous Chef', 'Jefe de Sala', 'Camarero', 'Barman']),
    ('05', ['Instrucciones', 'Limpieza Semanal', 'FIFO Semanal', 'Mantenimiento Mensual', 'Trimestral y Anual']),
    ('06', ['Instrucciones', 'Pre-Evento', 'San Valentín', 'Navidad', 'Temporada Terraza']),
    ('07', ['Instrucciones', 'Por Franja Horaria', 'Por Área', 'Por Perfil']),
    ('08', ['Instrucciones', 'Apertura del Negocio', 'Cierre del Negocio']),
    ('09', ['Instrucciones', 'Apertura de Caja', 'Cierre de Caja', 'Registro Mensual']),
    ('B01', ['Instrucciones', 'Briefing']),
    ('B02', ['Instrucciones', 'Calendario Anual']),
])
HOJA_PROHIBIDOS = set('[]:*?/\\')

# ==========================================================================
# 3. GLOSARIO (D7, D8): celdas cortas repetidas que valen la celda ENTERA (cabeceras de columna, zona, puesto,
#    cuándo). Jerga US (GLOSARIO-JERGA-ES-EN.md). Lo fija mapas.py para que los 11 libros digan lo mismo.
# ==========================================================================
GLOSARIO = OrderedDict([
    # cabeceras y pie de cada checklist
    ('Nº', '#'), ('Tarea', 'Task'), ('Zona', 'Area'), ('Responsable', 'Assigned to'), ('Hora Límite', 'Due by'),
    ('Cuándo', 'When'), ('✓ Completada', '✓ Done'), ('Firma', 'Initials'), ('Día', 'Day'), ('Cadencia', 'Frequency'),
    ('Antelación', 'Lead time'), ('Notas', 'Notes'), ('Nº de parte', 'Report #'),
    ('Tareas completadas:', 'Tasks done:'), ('de', 'of'), ('Verificado por:', 'Verified by:'),
    ('Firma:', 'Signature:'),
    # zonas (columna C)
    ('Cocina', 'Kitchen'), ('Sala', 'FOH'), ('Barra', 'Bar'), ('Admin', 'Office'), ('General', 'General'),
    ('Limpieza', 'Cleaning'), ('Evento', 'Event'), ('Terraza', 'Patio'), ('Acceso', 'Entrance'),
    ('Exterior', 'Outside'), ('Caja', 'Register'), ('Recepción', 'Host stand'), ('Baños', 'Restrooms'),
    ('Zonas comunes', 'Common areas'),
    # puestos (columna D) — US: line cook, prep cook, server, bartender, porter, shift manager, MOD
    ('Manager', 'Manager'), ('Gerente', 'GM'), ('Encargado', 'Shift manager'),
    ('Encargado saliente', 'Outgoing manager'), ('Encargado entrante', 'Incoming manager'),
    ('Ambos', 'Both'), ('Último en salir', 'Last one out'),
    ('Jefe de Cocina', 'Head chef'), ('Jefe Cocina', 'Head chef'), ('Sous Chef', 'Sous chef'),
    ('Chef partida', 'Lead line cook'), ('Cocinero', 'Line cook'), ('Cocineros', 'Line cooks'),
    ('Cocinero partida', 'Line cook'), ('Cocinero apertura', 'Opening line cook'),
    ('Cocinero cierre', 'Closing line cook'), ('Auxiliar cocina', 'Prep cook'), ('Auxiliar', 'Prep cook'),
    ('Pastelero', 'Pastry cook'), ('Pastelero/Cocinero', 'Pastry / line cook'), ('Chef', 'Chef'),
    ('Equipo cocina', 'Kitchen team'),
    ('Jefe de Sala', 'FOH manager'), ('Jefe Sala', 'FOH manager'), ('Camarero', 'Server'),
    ('Camareros', 'Servers'), ('Camarero apertura', 'Opening server'), ('Barman', 'Bartender'),
    ('Todo el equipo', 'All staff'), ('Todo equipo', 'All staff'), ('Todo equipo sala', 'All FOH staff'),
    ('Personal limpieza', 'Porter'), ('Responsable de caja', 'Cashier / MOD'),
    ('Técnico', 'Technician'), ('Técnico/Chef', 'Tech / chef'), ('Empresa externa', 'Contractor'),
    ('(Responsable)', '(Assigned to)'), ('(Hora)', '(Time)'),
    # cuándo / día / cadencia (columna E)
    ('Cierre', 'Close'), ('Servicio', 'Service'), ('Cambio', 'Shift change'), ('Según entrega', 'On delivery'),
    ('Si aplica', 'If needed'), ('Semanal', 'Weekly'), ('Mensual', 'Monthly'), ('Trimestral', 'Quarterly'),
    ('Anual', 'Annual'), ('Cada 5 años', 'Every 5 years'),
    ('Lunes', 'Monday'), ('Martes', 'Tuesday'), ('Miércoles', 'Wednesday'), ('Jueves', 'Thursday'),
    ('Viernes', 'Friday'), ('Sábado', 'Saturday'), ('Domingo', 'Sunday'), ('Martes-Miérc', 'Tue–Wed'),
    ('Cada día', 'Daily'), ('30 diciembre', 'Dec 30'),
    ('Día 1', 'Day 1'), ('Día 2', 'Day 2'), ('Día 3', 'Day 3'), ('Día 4', 'Day 4'), ('Día 5', 'Day 5'),
    ('Día 1-3', 'Days 1–3'),
    ('Al confirmar', 'At booking'), ('48h antes', '48 h out'), ('24h antes', '24 h out'),
    ('Mañana', 'Morning'), ('30 min antes', '30 min prior'), ('Post-evento', 'After event'),
    ('Día siguiente', 'Next day'), ('Pre-servicio', 'Pre-shift'),
    ('7 días antes', '7 days out'), ('5 días antes', '5 days out'), ('10 días antes', '10 days out'),
    ('15 días antes', '15 days out'), ('1 semana antes', '1 week out'), ('1 mes antes', '1 month out'),
    ('Día apertura', 'Opening day'), ('Último día', 'Last day'),
    # BONUS-02 (marcadores de las filas libres) y tabla de congelación del 05
    ('(Tu fecha)', '(Your date)'), ('(Añade aquí)', '(Add here)'), ('(Tareas específicas)', '(Key tasks)'),
    ('(Antelación)', '(Lead time)'),
    ('Familia', 'Food group'), ('Vida útil', 'Freezer time'),
    ('2-3 meses', '2–3 months'), ('4-6 meses', '4–6 months'), ('8-12 meses', '8–12 months'),
    ('6-9 meses', '6–9 months'), ('1-3 meses', '1–3 months'), ('3 meses', '3 months'),
])

# Zonas y puestos (columnas C y D): lo que el censo cuenta como «puestos y zonas de la hostelería española»
_DESDE, _HASTA = list(GLOSARIO).index('Cocina'), list(GLOSARIO).index('(Responsable)')
PUESTOS_ES = frozenset(list(GLOSARIO)[_DESDE:_HASTA + 1])
# Claves de GLOSARIO que pueden no aparecer en el ES (un vertical hereda el glosario base entero; kit.py)
GLOSARIO_OPCIONAL = frozenset()

# ==========================================================================
# 4. Horas (D9): las horas límite son TEXTO «07:00» (no son horas de Excel) → «7:00 AM». Las que van dentro de una
#    frase («antes de las 18:00») las escribe el traductor con la misma regla (pista).
# ==========================================================================
RX_HORA_CELDA = re.compile(r'^(\d{2}):(\d{2})(?:-(\d{2}):(\d{2}))?$')


def _h12(h, m):
    h, m = int(h), int(m)
    suf = 'AM' if h < 12 else 'PM'
    return '%d:%02d' % (h % 12 or 12, m), suf


def hora_us(texto):
    """«07:00» → «7:00 AM» · «18:00» → «6:00 PM» · «00:00» → «12:00 AM» · «10:00-11:30» → «10:00–11:30 AM»."""
    m = RX_HORA_CELDA.match(texto)
    if not m:
        raise ValueError('no es una hora de celda: %r' % texto)
    a, sa = _h12(m.group(1), m.group(2))
    if not m.group(3):
        return '%s %s' % (a, sa)
    b, sb = _h12(m.group(3), m.group(4))
    return '%s–%s %s' % (a, b, sb) if sa == sb else '%s %s–%s %s' % (a, sa, b, sb)


# ==========================================================================
# 5. Recuento de caja en dólares (D12). Mismas 15 filas del ES (7 billetes + 8 monedas). Fila → (ES, ×ES, EN, ×EN).
#    Las 2 filas de monedas que sobran en US (no hay 2 ni 20 céntimos) llevan cartuchos (rolls): 40 quarters = $10,
#    50 dimes = $5. Rótulos cortos: la columna A mide 10 (BILLS / COINS ya lo dicen).
#    El centavo ya no se acuña (12-nov-2025) pero sigue siendo de curso legal: su fila se queda.
# ==========================================================================
HOJA_CAJA = ('09', 'Cierre de Caja')
DENOMINACIONES = [
    (27, '500 €', 500, '$100', 100), (28, '200 €', 200, '$50', 50), (29, '100 €', 100, '$20', 20),
    (30, '50 €', 50, '$10', 10), (31, '20 €', 20, '$5', 5), (32, '10 €', 10, '$2', 2), (33, '5 €', 5, '$1', 1),
    (35, '2 €', 2, '$1 coin', 1), (36, '1 €', 1, '50¢', 0.5), (37, '0,50 €', 0.5, '25¢', 0.25),
    (38, '0,20 €', 0.2, '10¢', 0.1), (39, '0,10 €', 0.1, '5¢', 0.05), (40, '0,05 €', 0.05, '1¢', 0.01),
    (41, '0,02 €', 0.02, '25¢ roll', 10), (42, '0,01 €', 0.01, '10¢ roll', 5),
]
VALORES_DENOMINACION_EN = sorted({d[4] for d in DENOMINACIONES})


def _num(x):
    return ('%g' % x)


FORMULAS_POR_CELDA = OrderedDict(
    ((HOJA_CAJA[0], HOJA_CAJA[1], 'C%d' % f), ('=B%d*%s' % (f, _num(xes)), '=B%d*%s' % (f, _num(xen))))
    for f, _es, xes, _en, xen in DENOMINACIONES)
FORMULAS_EN = OrderedDict()            # patrones que cambian en TODO el kit: ninguno (los contadores no cambian)
PATRONES_SIN_CAMBIO = set()            # patrones con comparación numérica que no cambian (los rellena el censo)

# ==========================================================================
# 6. BONUS-02 «Holiday Calendar» (D14): 22 filas, mismo orden por meses. (fila → mes, fecha/evento, antelación)
#    Las tareas (columna C) las escribe el traductor: con ADAPTAR cuando el evento cambia.
# ==========================================================================
HOJA_CAL = ('B02', 'Calendario Anual')
FILAS_CALENDARIO = range(5, 27)        # filas del BONUS-02 que cubre CALENDARIO (un vertical puede tener otras)
CALENDARIO = OrderedDict([
    (5, ('January', "Jan 1 — New Year's Day", '1 week', None)),
    (6, ('February', 'Super Bowl Sunday (2nd Sunday in Feb)', '2 weeks',
         'Sustituye a Reyes. Tareas: pedidos anticipados para llevar (wings, party platters), pantallas en la barra, '
         'personal extra de barra y de delivery')),
    (7, ('February', "Feb 14 — Valentine's Day", '2 weeks', None)),
    (8, ('February–March', 'Mardi Gras (varies)', '1 week', None)),
    (9, ('March', "Mar 17 — St. Patrick's Day", '2 weeks',
         'Sustituye al Día del Padre (en EE. UU. va en junio, fila 16). Tareas: especiales irlandeses y de cerveza, '
         'refuerzo de barra, comprobar identificación (ID) a todo el que pida alcohol')),
    (10, ('March–April', 'Easter Sunday (varies)', '2 weeks',
          'Sustituye a Semana Santa. Tareas: brunch de Pascua, especiales (jamón asado, cordero), reservas ampliadas')),
    (11, ('March–April', 'Patio opening', '1 month',
          'La licencia es el «outdoor dining / sidewalk cafe permit» de la ciudad. Tareas: montaje, permiso, carta '
          'de patio')),
    (12, ('May–June', 'Graduation season', '1 month',
          'Mismas tareas del ES (menú de grupo cerrado, depósito y precio por persona, sala privada); en EE. UU. '
          'son graduaciones, baby/bridal showers y comuniones')),
    (13, ('May', 'May 5 — Cinco de Mayo', '1 week',
          'Sustituye al 1 de mayo. Tareas: especiales de margaritas y tacos, refuerzo de barra')),
    (14, ('May', "2nd Sunday — Mother's Day", '2 weeks',
          'En EE. UU. es el segundo domingo de mayo y es día de brunch: menú especial de brunch, reservas ampliadas, '
          'detalle para las madres')),
    (15, ('May', 'Memorial Day (last Monday)', '1 month',
          'Sustituye a «Inicio temporada alta». Tareas: reforzar plantilla, stock de verano, patio a pleno')),
    (16, ('June', "3rd Sunday — Father's Day", '2 weeks',
          'Sustituye a San Juan. Tareas: especiales de carne y barbacoa (steak, BBQ), reservas ampliadas')),
    (17, ('July', 'Jul 4 — Independence Day', '1 week',
          'Sustituye a la fila de temporada alta (sus tareas pasan a la fila 18). Tareas: decidir horario (muchos '
          'cierran o abren solo de día), patio a pleno rendimiento, especiales de barbacoa')),
    (18, ('July–August', 'Summer peak season', 'Ongoing',
          'Tareas = las de «Temporada alta» de la fila 17 del ES: personal extra, horario ampliado, carta de verano')),
    (19, ('September', 'Labor Day (1st Monday) + back to school', '2 weeks',
          'Fin del verano. Tareas: carta de otoño y especiales de almuerzo (lunch specials) para la vuelta a la '
          'rutina')),
    (20, ('October', 'Oct 31 — Halloween', '1 week', None)),
    (21, ('November', 'Thanksgiving (4th Thursday)', '1 month',
          'Sustituye a Todos los Santos. Tareas: decidir si se abre (menú prix fixe de Thanksgiving o pedidos para '
          'llevar), pedido de pavo, turnos; la noche del miércoles anterior es de las de más barra del año')),
    (22, ('November', 'Patio closing', '1 week', None)),
    (23, ('Nov–Dec', 'Holiday gift card season', '2 weeks',
          'Sustituye al puente de la Constitución. Del Black Friday a Nochebuena. Tareas: promoción de tarjetas regalo '
          '(bonus card), expositor en la host stand, venta online')),
    (24, ('December', 'Holiday parties (company)', '1 month', None)),
    (25, ('December', 'Dec 24–25 — Christmas', '2 weeks',
          'Decidir si se abre el día de Navidad (muchos cierran). Tareas: menú, decoración, stock especial')),
    (26, ('December', "Dec 31 — New Year's Eve", '2 weeks',
          'Sin uvas ni cava ni cotillón español. Tareas: menú de gala o prix fixe, party favors (gorros, matasuegras), '
          'brindis con champán a medianoche, turnos de noche')),
])

# ==========================================================================
# 7. POR_CELDA: textos EN fijados por celda (no van a los traductores). Solo lo que lleva una decisión legal,
#    de caja o un hecho comprobable. (libro, hoja ES, celda) → EN
# ==========================================================================
POR_CELDA = OrderedDict([
    # 09 · Apertura de Caja (D12)
    (('09', 'Apertura de Caja', 'B23'), 'Starting bank (opening float)'),
    # 09 · Cierre de Caja: tareas de tarjetas y otros medios (D12: propinas fuera de ventas)
    (('09', 'Cierre de Caja', 'B8'), 'Batch out the card terminal; note card sales WITHOUT tips'),
    (('09', 'Cierre de Caja', 'B9'), 'Note other tenders (gift cards, house accounts) + card tips paid in cash'),
    (('09', 'Cierre de Caja', 'A24'), '💰 Cash Count by Denomination'),
    (('09', 'Cierre de Caja', 'A25'), 'Denomination'), (('09', 'Cierre de Caja', 'B25'), 'Quantity'),
    (('09', 'Cierre de Caja', 'C25'), 'Subtotal'),
    (('09', 'Cierre de Caja', 'A26'), 'BILLS'), (('09', 'Cierre de Caja', 'A34'), 'COINS'),
    (('09', 'Cierre de Caja', 'A43'), 'TOTAL CASH'),
    (('09', 'Cierre de Caja', 'A45'), '📊 Closing Summary'),
    (('09', 'Cierre de Caja', 'A46'), 'Item'), (('09', 'Cierre de Caja', 'C46'), 'Amount'),
    (('09', 'Cierre de Caja', 'A47'), 'Total cash (count)'),
    (('09', 'Cierre de Caja', 'A48'), 'Starting bank (−)'),
    (('09', 'Cierre de Caja', 'A49'), 'Net cash (counted − starting bank)'),
    (('09', 'Cierre de Caja', 'A50'), 'Card sales, excl. tips'),
    (('09', 'Cierre de Caja', 'A51'), 'Other tenders + card tips paid in cash'),
    (('09', 'Cierre de Caja', 'A52'), 'TOTAL COLLECTED'),
    (('09', 'Cierre de Caja', 'A53'), 'POS Z report: sales + tax, excl. tips'),
    (('09', 'Cierre de Caja', 'A54'), 'OVER / SHORT'),
    # 09 · Registro Mensual: cabecera de la tabla y totales
    (('09', 'Registro Mensual', 'A4'), 'Day'), (('09', 'Registro Mensual', 'B4'), 'Starting Bank'),
    (('09', 'Registro Mensual', 'C4'), 'Cash Counted'), (('09', 'Registro Mensual', 'D4'), 'Card Sales (no tips)'),
    (('09', 'Registro Mensual', 'E4'), 'Other + Tips Paid'),
    (('09', 'Registro Mensual', 'F4'), 'Total Collected'), (('09', 'Registro Mensual', 'G4'), 'POS Z (+ tax, no tips)'),
    (('09', 'Registro Mensual', 'H4'), 'Over/Short'), (('09', 'Registro Mensual', 'I4'), 'Bank Deposit'),
    (('09', 'Registro Mensual', 'J4'), 'Closed by'), (('09', 'Registro Mensual', 'A36'), 'TOTALS'),
    # 02 · pescado crudo: destrucción de parásitos (D10, FDA Food Code 3-402.11/3-402.12 y 3-203.12)
    # (errata de texto del 18-oct-2026, desde la ronda 1 M2 de la ghost kitchen: las TRES opciones de 3-402.11, con la
    # temperatura de cada tramo; el registro es 3-402.12)
    (('02', 'Fríos', 'B10'),
     'Raw or undercooked fish (tartare, ceviche, crudo) — parasite destruction (FDA Food Code 3-402.11): confirm it was '
     'frozen and stored at −4 °F or below for 7 days, or frozen at −31 °F or below until solid and stored at −31 °F or '
     'below for 15 h, or frozen at −31 °F or below until solid and stored at −4 °F or below for 24 h; keep the record '
     '90 days (FDA Food Code 3-402.12)'),
    (('02', 'Mise en Place', 'B10'),
     'Raw or undercooked fish and shellfish — fish: frozen for parasites (−4 °F or below for 7 days; or −31 °F or below '
     'until solid, then 15 h at −31 °F or below or 24 h at −4 °F or below; FDA Food Code 3-402.11), record kept 90 days '
     '(FDA Food Code 3-402.12); raw oysters and clams: shellstock tags kept 90 days'),
    # 03 · conservación de fichajes (D11, 29 CFR 516.5-516.6)
    (('03', 'Mensual Manager', 'B16'),
     "File this month's time-clock records (FLSA minimum: time cards 2 years, payroll 3 years; some states require "
     "longer, e.g. NY 6)"),
    # 05 · Trimestral y Anual: servicios contratados US (D11; NFPA 96, OSHA 1910.157, EPA 608, normas locales)
    (('05', 'Trimestral y Anual', 'B6'),
     'Pest control by a licensed operator: service visit and signed service report on file'),
    (('05', 'Trimestral y Anual', 'D6'), 'Pest control co.'), (('05', 'Trimestral y Anual', 'E6'), 'Monthly'),
    (('05', 'Trimestral y Anual', 'B7'),
     'Hood and duct cleaning by a certified contractor (NFPA 96: quarterly if high volume or charbroil, '
     'semiannual if moderate)'),
    (('05', 'Trimestral y Anual', 'D7'), 'Hood cleaning co.'), (('05', 'Trimestral y Anual', 'E7'), 'Semiannual'),
    (('05', 'Trimestral y Anual', 'B8'),
     'Annual extinguisher maintenance by a licensed fire protection company: new tag and record (OSHA 1910.157)'),
    (('05', 'Trimestral y Anual', 'D8'), 'Fire safety co.'),
    (('05', 'Trimestral y Anual', 'B9'),
     'Hood fire suppression system inspection every 6 months (NFPA 96); extinguisher hydrostatic tests per label'),
    (('05', 'Trimestral y Anual', 'D9'), 'Fire safety co.'), (('05', 'Trimestral y Anual', 'E9'), 'Semiannual'),
    (('05', 'Trimestral y Anual', 'B10'),
     'Gas lines and appliance connections checked by a licensed pro (as often as your local code requires)'),
    (('05', 'Trimestral y Anual', 'D10'), 'Licensed plumber'), (('05', 'Trimestral y Anual', 'E10'), 'Annual'),
    (('05', 'Trimestral y Anual', 'B11'),
     'Refrigeration service by an EPA 608-certified tech: coils, gaskets and refrigerant leak check'),
    (('05', 'Trimestral y Anual', 'D11'), 'Refrigeration tech'),
    (('05', 'Trimestral y Anual', 'A13'), '  WATER, GREASE & WASTE'),
    (('05', 'Trimestral y Anual', 'B14'),
     'Backflow preventer test by a certified tester (most water utilities require it yearly)'),
    (('05', 'Trimestral y Anual', 'D14'), 'Backflow tester'),
    (('05', 'Trimestral y Anual', 'B15'),
     'Grease trap pumped by a licensed hauler: keep the manifest (frequency per local FOG rules)'),
    (('05', 'Trimestral y Anual', 'D15'), 'Grease hauler'), (('05', 'Trimestral y Anual', 'E15'), 'Quarterly'),
    (('05', 'Trimestral y Anual', 'B16'),
     'Used cooking oil pickup by a licensed recycler: file the pickup receipts'),
    (('05', 'Trimestral y Anual', 'D16'), 'Oil recycler'),
    (('05', 'Trimestral y Anual', 'B17'),
     'Review the waste and recycling hauler contract and local recycling rules'),
    (('05', 'Trimestral y Anual', 'B20'),
     "Review insurance (general liability, property, liquor liability, workers' comp) and renewal dates"),
    (('05', 'Trimestral y Anual', 'B21'),
     'POS check: software updates, sales tax rates and settings, user permissions'),
])
for _f, _es, _xes, _en, _xen in DENOMINACIONES:
    POR_CELDA[(HOJA_CAJA[0], HOJA_CAJA[1], 'A%d' % _f)] = _en
for _fila, (_mes, _evento, _antel, _dir) in CALENDARIO.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'A%d' % _fila)] = _mes
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'B%d' % _fila)] = _evento
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'D%d' % _fila)] = _antel

# ==========================================================================
# 8. ADAPTAR: lo que el traductor ADAPTA (no traduce literal) en una celda concreta. En español, con el dato US.
#    (libro, hoja ES, celda) → instrucción. Las cifras salen de SPEC §3 (REGLAS_US).
# ==========================================================================
_TEMP_FRIO = ('°F: cámara 41 °F o menos, congelador 0 °F o menos (FDA Food Code 3-501.16); coletilla «— log '
              'reading: ____ °F»; °C solo entre paréntesis si cabe')
_HACCP_KIT = ('«Pack APPCC» → «HACCP Food Safety Kit Pro» (nuestro kit EN: aichef.pro/en/digital-products/'
              'haccp-templates)')
ADAPTAR = OrderedDict([
    # 01
    (('01', 'Apertura Cocina', 'B7'), 'FDA Food Code 2-303.11: sin joyas en manos y brazos SALVO un anillo liso '
                                      '(alianza); uñas cortas y limpias, sin esmalte ni postizas salvo con guantes'),
    (('01', 'Apertura Cocina', 'B9'), 'Lavamanos = handwashing sink, con agua caliente (al menos 100 °F, FDA Food '
                                      'Code 5-202.12), jabón y papel'),
    (('01', 'Apertura Cocina', 'B10'), 'FDA Food Code 2-201.11: el responsable (person in charge) comprueba que nadie '
                                       'tiene vómitos, diarrea, ictericia, dolor de garganta con fiebre o una herida '
                                       'infectada; quien los tenga no manipula alimentos'),
    (('01', 'Apertura Cocina', 'B14'), 'Práctica US: si huele a gas, no enciendas nada ni toques interruptores, sal '
                                       'y llama a la compañía de gas o al 911 desde fuera'),
    (('01', 'Apertura Cocina', 'B18'), _TEMP_FRIO + '; «cámaras» = walk-in cooler y walk-in freezer'),
    (('01', 'Apertura Cocina', 'B21'), _TEMP_FRIO),
    (('01', 'Apertura Cocina', 'B22'), _TEMP_FRIO),
    (('01', 'Apertura Cocina', 'B23'), _TEMP_FRIO),
    (('01', 'Apertura Cocina', 'B24'), _HACCP_KIT + '; lectura en °F'),
    (('01', 'Apertura Sala', 'B12'), 'Alérgenos US: los 9 principales (FALCPA + FASTER Act); «carta de alérgenos» '
                                     '→ allergen chart / allergen matrix'),
    (('01', 'Apertura Sala', 'B19'), 'Ceniceros solo si tu ciudad o estado permite fumar en el patio (muchos lo '
                                     'prohíben): dilo así'),
    (('01', 'Cierre Cocina', 'B6'), 'Date marking US: etiqueta con fecha; lo preparado y listo para comer aguanta '
                                    '7 días a 41 °F, contando el día de preparación como día 1 (FDA Food Code '
                                    '3-501.17)'),
    (('01', 'Cierre Cocina', 'B12'), _TEMP_FRIO),
    # 02
    (('02', 'Calientes', 'B20'), 'Mantenimiento en caliente: 135 °F o más (FDA Food Code 3-501.16); coletilla '
                                 '«— log reading: ____ °F»'),
    (('02', 'Calientes', 'B27'), 'Filtrar según el procedimiento del fabricante de la freidora (los filtros integrados '
                                 'trabajan a temperatura de servicio; a mano, dejar enfriar antes, guantes '
                                 'resistentes al calor y recipiente estable), sin cifra de temperatura; el aceite '
                                 'usado va al contenedor del reciclador (used cooking oil recycler), no a un «gestor '
                                 'autorizado»'),
    (('02', 'Fríos', 'B6'), 'FDA Food Code 3-302.15: lavar bajo agua potable corriente; si se usa un producto de '
                            'lavado o cloro, solo uno apto para frutas y verduras, a la dosis de la etiqueta, y '
                            'ACLARAR. Sin «70 ppm, 5 min» ni «lejía»'),
    (('02', 'Fríos', 'B17'), 'FDA Food Code 3-501.16: todo alimento TCS a 41 °F o menos, también pescado y marisco '
                             'crudo, hojas verdes cortadas, tomate cortado y melón cortado. Sin el «< 8 °C» español'),
    (('02', 'Mise en Place', 'B28'), 'Atemperar helado: de 0 °F a unos 10 °F'),
    # 03
    (('03', 'Diario Manager', 'B29'), 'Plataformas US: Google, Yelp y TripAdvisor'),
    (('03', 'Diario Manager', 'B35'), 'US: revisar y aprobar los fichajes del equipo (time-clock punches: entradas, '
                                      'salidas y pausas) en el POS o en la app de fichaje'),
    (('03', 'Semanal Manager', 'B26'), _HACCP_KIT),
    (('03', 'Mensual Manager', 'B18'), 'US: la nómina por horas no es mensual (semanal o quincenal según la ley '
                                       'estatal de frecuencia de pago): CONCILIAR las nóminas del mes con propinas, '
                                       'horas extra y bonus'),
    (('03', 'Mensual Manager', 'B23'), 'OSHA 29 CFR 1910.157(e)(2): inspección visual MENSUAL de los extintores'),
    (('03', 'Mensual Manager', 'B30'), '«Google Maps» → Google Business Profile'),
    # 04
    (('04', 'Camarero', 'B20'), 'Costumbre US: la cuenta se lleva cuando la mesa ha terminado o la pide, sin meter '
                                'prisa; escríbelo así'),
    # 05
    (('05', 'Instrucciones', 'B8'), _HACCP_KIT),
    (('05', 'Instrucciones', 'B12'), 'Describe la lista US de la hoja «Quarterly & Annual»: control de plagas, '
                                     'limpieza de campana y conductos, extintores y sistema de extinción de la '
                                     'campana, gas, frío, backflow, separador de grasas, aceite usado, residuos, '
                                     'seguros y POS / sales tax. Sin DDD, BIE, legionela ni facturación española'),
    (('05', 'Mantenimiento Mensual', 'B21'), 'Inspección visual mensual (OSHA 1910.157(e)(2)): manómetro en verde, '
                                             'pasador y precinto, acceso libre, etiqueta firmada'),
    (('05', 'Trimestral y Anual', 'B23'), 'Calibración por el método del punto de hielo (32 °F)'),
    # 06
    (('06', 'Navidad', 'B8'), 'Pedidos navideños US: prime rib, marisco, postres de temporada (sin turrón ni cordero)'),
    (('06', 'Navidad', 'B17'), 'Champán / espumoso (sin cava)'),
    (('06', 'Navidad', 'B21'), 'Party favors (gorros, matasuegras) y cuenta atrás; SIN uvas'),
    (('06', 'Navidad', 'B22'), 'Preparar el brindis con champán para la cuenta atrás de medianoche (sin uvas ni '
                               'campanadas)'),
    (('06', 'Navidad', 'B23'), 'Brindis a medianoche solo para mayores de 21 (comprobar ID) y opción sin alcohol'),
    (('06', 'Temporada Terraza', 'B6'), 'Permiso de la ciudad: outdoor dining / sidewalk cafe permit'),
    # 08
    (('08', 'Apertura del Negocio', 'B8'), 'Persianas → security gate / shutters'),
    # 09
    (('09', 'Instrucciones', 'B6'), 'Arqueo → cash count; Z del TPV → POS Z report; descuadre → over/short'),
    (('09', 'Instrucciones', 'B14'), 'Añade al final: la tabla trae billetes y monedas de EE. UU. (el penny ya no se '
                                     'acuña pero sigue siendo de curso legal; un «25¢ roll» cuenta $10 y un «10¢ '
                                     'roll» $5); en UK, Canadá o Australia, desprotege la hoja (sin contraseña) y '
                                     'cambia el rótulo y el valor de cada fila'),
    (('09', 'Instrucciones', 'B15'), 'Las tres cifras EN: card sales WITHOUT tips, other tenders + card tips paid out '
                                     'in cash, y la Z del POS = ventas netas + sales tax, SIN propinas (rótulos de la '
                                     'hoja, entre comillas)'),
    (('09', 'Instrucciones', 'B16'), 'Fórmula con los rótulos EN: TOTAL COLLECTED = (cash counted − starting bank) + '
                                     'card sales + other'),
    (('09', 'Instrucciones', 'B17'), 'DESCUADRE → OVER / SHORT; TOTAL FACTURADO → TOTAL COLLECTED'),
    (('09', 'Cierre de Caja', 'B10'), 'Total collected = (cash counted − starting bank) + card sales + other'),
    (('09', 'Registro Mensual', 'A37'), 'Usa los rótulos EN de la fila 4 («Cash Counted», «Starting Bank», '
                                        '«Over/Short»); «100 € de descuadre» → «100 of over/short»; añade: «Card '
                                        'Sales» sin propinas y «Other + Tips Paid» = otros medios + propinas de '
                                        'tarjeta pagadas en efectivo del cajón; «POS Z» = ventas netas + sales tax, '
                                        'sin propinas'),
    # BONUS-02
    (('B02', 'Instrucciones', 'B8'), 'Añade la nota UK: Mothering Sunday (marzo), bank holidays y Boxing Day en las '
                                     'filas libres'),
])
# Celdas ES con °C cuya EN NO lleva cifra en °F (decisión de la ronda 1 de F2: el filtrado del aceite sigue el
# procedimiento del fabricante, sin temperatura). G7 no les exige °F.
CELSIUS_SIN_F = frozenset({('02', 'Calientes', 'B27')})
for _fila, (_mes, _evento, _antel, _dir) in CALENDARIO.items():
    if _dir:
        ADAPTAR[(HOJA_CAL[0], HOJA_CAL[1], 'C%d' % _fila)] = 'Evento EN: «%s». %s' % (_evento, _dir)

# ==========================================================================
# 9. CLAVES (D7): literales de fórmula, de CF y de DV. El kit solo usa ✓, —, N/A, «?*», «>0», «<0»: N/A es
#    igual en inglés. Nada cambia de color.
# ==========================================================================
CLAVES = OrderedDict([('N/A', 'N/A')])
DV_LISTAS_ESPECIALES = OrderedDict()
DV_NUEVAS = OrderedDict()
VALORES_EN = OrderedDict()             # ningún número ni fecha cambia (las cifras de caja van en FORMULAS_POR_CELDA);
                                       # un vertical: (libro, hoja ES, celda) → (valor ES, número EN) (mapas_cafe)

# ==========================================================================
# 10. Formatos (D13)
# ==========================================================================
# G2 (gates_en.py): RX de términos que ninguna celda EN puede llevar (p. ej. roles de restaurante en un vertical) y el
# texto que inyecta el autotest. None en el base (y en el bar): el gate no se activa y su salida no cambia.
TERMINOS_PROHIBIDOS = None
TERMINO_PROHIBIDO_EJEMPLO = None

FORMATOS_EN = OrderedDict([('#,##0.00 €', '#,##0.00'), ('€#,##0.00', '#,##0.00')])

# ==========================================================================
# 11. Reglas US/UK con fuente (SPEC §3). [criterio del kit] / [local] = no es una cifra federal.
# ==========================================================================
REGLAS_US = OrderedDict([
    ('frio', ('41 °F o menos (TCS); congelador 0 °F', 'FDA Food Code 2022 §3-501.16(A)(2); 0 °F = referencia USDA')),
    ('caliente', ('135 °F o más', 'FDA Food Code 2022 §3-501.16(A)(1)')),
    ('parasitos', ('−4 °F 168 h · −31 °F hasta sólido + 15 h · −31 °F sólido + −4 °F 24 h; registro 90 días',
                   'FDA Food Code 2022 §3-402.11 y §3-402.12')),
    ('moluscos', ('etiquetas shellstock 90 días', 'FDA Food Code 2022 §3-203.12')),
    ('date_marking', ('7 días a 41 °F, día 1 = preparación', 'FDA Food Code 2022 §3-501.17')),
    ('joyas', ('solo anillo liso', 'FDA Food Code 2022 §2-303.11')),
    ('enfermos', ('vómitos, diarrea, ictericia, garganta con fiebre', 'FDA Food Code 2022 §2-201.11')),
    ('lavamanos', ('agua a 100 °F mínimo', 'FDA Food Code 2022 §5-202.12')),
    ('lavado_vegetal', ('agua potable; químicos aprobados a dosis de etiqueta', 'FDA Food Code 2022 §3-302.15')),
    ('alergenos', ('9 principales (sésamo desde 1-ene-2023)', 'FALCPA 2004 + FASTER Act 2021')),
    ('extintor_mes', ('inspección visual mensual', '29 CFR 1910.157(e)(2)')),
    ('extintor_ano', ('mantenimiento anual registrado', '29 CFR 1910.157(e)(3)')),
    ('hidrostatica', ('según el tipo y la etiqueta', '29 CFR 1910.157(f), tabla L-1; NFPA 10')),
    ('campana', ('trimestral alto volumen · semestral moderado · mensual combustible sólido · anual bajo',
                 'NFPA 96, tabla 11.4')),
    ('supresion', ('cada 6 meses', 'NFPA 96 §11.2; NFPA 17A')),
    ('refrigerante', ('técnico certificado EPA 608', '40 CFR Part 82, Subpart F')),
    ('fichajes', ('fichajes 2 años; nóminas 3 años (mínimo federal; algunos estados piden más: NY 6)',
                  '29 CFR 516.5-516.6; NY Labor Law §195(4)')),
    ('frecuencia_pago', ('nómina por horas semanal o quincenal según el estado (no mensual)',
                         '[estatal] CA Labor Code §204; NY Labor Law §191; TX Labor Code §61.011')),
    ('enfriamiento', ('135 → 70 °F en 2 h; 70 → 41 °F en 4 h más', 'FDA Food Code 2022 §3-501.14')),
    ('recalentado', ('165 °F durante 15 s en 2 h como máximo (para mantener en caliente)',
                     'FDA Food Code 2022 §3-403.11(A)')),
    ('sanitizante', ('concentración medida con tiras (test kit); ppm de la etiqueta', 'FDA Food Code 2022 §4-302.14; '
                                                                                      '§4-501.114')),
    ('aviso_consumidor', ('aviso al consumidor en la carta para crudo o poco hecho', 'FDA Food Code 2022 §3-603.11')),
    ('centavo', ('no se acuña desde el 12-nov-2025; curso legal', 'U.S. Mint, acto del 12-nov-2025 (Coin World)')),
    ('backflow', ('test anual habitual', '[local] programa de cross-connection de la compañía de agua')),
    ('grasas', ('frecuencia de la ordenanza FOG', '[local] ordenanza municipal de grasas (FOG)')),
    ('propinas', ('propinas de tarjeta fuera de las ventas', '[criterio del kit] práctica de caja US')),
    ('festivos', ('Memorial Day último lunes de mayo · Labor Day primer lunes de septiembre · Thanksgiving 4.º jueves '
                  'de noviembre', '5 U.S.C. 6103')),
    ('madre_padre', ("Mother's Day 2.º domingo de mayo · Father's Day 3.er domingo de junio", '36 U.S.C. 117 y 109')),
    ('uk_temp', ('8 °C frío · 63 °C caliente', 'Food Safety and Hygiene (England) Regulations 2013, sched. 4')),
    ('uk_alergenos', ('14 alérgenos', 'Food Information Regulations 2014')),
])


# ==========================================================================
# 12. utilidades
# ==========================================================================
def patron(formula):
    """Normaliza las filas de las referencias de celda a {r} (las referencias absolutas $X$n se respetan)."""
    return re.sub(r'(?<![A-Za-z_$])(\$?[A-Z]{1,3})(?<!\$)(\d+)(?![\d(])',
                  lambda m: m.group(1) + '{r}', formula)


RX_LIT = re.compile(r'"((?:[^"]|"")*)"')
RX_ESPANOL = re.compile(r'[áéíóúñÁÉÍÓÚÑ¿¡]|\b(de|del|la|las|los|el|y|con|para|por|sin)\b')


def necesita_clave(lit):
    """Un literal va a CLAVES si lleva letras o €; los demás («?*», «✓», «>0») no cambian."""
    return any(ch.isalpha() for ch in lit) or '€' in lit


def tokens_en(texto, tokens):
    t = texto.lower()
    return {k for k in tokens if k.lower() in t}


def numeros_formula(f):
    return {float(x) for x in re.findall(r'(?<![\w$.])-?\d+(?:\.\d+)?', RX_LIT.sub('""', f))}


# ==========================================================================
# 13. Autotest y cruce con el censo
# ==========================================================================
def autotest():
    err = []
    for es, en in HOJAS.items():
        if len(en) > 31 or set(en) & HOJA_PROHIBIDOS or en.startswith("'") or en.endswith("'"):
            err.append('pestaña inválida: ' + en)
    for f, hs in HOJAS_ES_POR_LIBRO.items():
        ens = [HOJAS[h] for h in hs]
        if len(set(e.lower() for e in ens)) != len(ens):
            err.append('pestañas EN duplicadas en ' + f)
    if len(FICHEROS) != 11 or len(set(FICHEROS.values())) != 11:
        err.append('FICHEROS debe tener 11 nombres EN distintos')
    for es, en in FICHEROS.items():
        if en not in TITULOS:
            err.append('fichero sin título: ' + en)
        if not re.fullmatch(r'(BONUS-)?\d{2}-[a-z0-9-]+\.xlsx', en) or es.split('-')[0] != en.split('-')[0]:
            err.append('fichero EN mal formado: ' + en)
        if es.startswith('BONUS') != TITULOS.get(en, '').startswith('BONUS'):
            err.append('el título de un bonus debe empezar por «BONUS:» (y solo él): ' + en)
    if 'Cleaning' in TITULO_SEO and not any('cleaning' in t.lower() for t in TITULOS.values()):
        err.append('el title SEO promete «Cleaning» y ningún fichero es de limpieza')
    if not TITULO_SEO.startswith(PRODUCTO + ': '):
        err.append('TITULO_SEO debe ser «nombre: descriptor» (Forma B)')
    for k, v in list(CLAVES.items()) + list(GLOSARIO.items()) + list(POR_CELDA.items()):
        if '"' in v:
            err.append('comilla doble recta dentro de un texto EN fijado: %r' % (k,))
        if RX_ESPANOL.search(v.replace('Cinco de Mayo', '')):
            err.append('español en un texto EN fijado: %r → %r' % (k, v))
        if '€' in v or '°C' in v:
            err.append('€ o °C en un texto EN fijado: %r' % (k,))
    for k in GLOSARIO:
        if k != k.strip():
            err.append('clave de GLOSARIO con espacios: %r' % k)
    casos = {'07:00': '7:00 AM', '11:45': '11:45 AM', '12:00': '12:00 PM', '15:30': '3:30 PM', '18:00': '6:00 PM',
             '23:30': '11:30 PM', '00:00': '12:00 AM', '10:00-11:30': '10:00–11:30 AM',
             '11:00-13:00': '11:00 AM–1:00 PM'}
    for es, en in casos.items():
        if hora_us(es) != en:
            err.append('hora_us(%r) = %r, esperaba %r' % (es, hora_us(es), en))
    if len(DENOMINACIONES) != 15 or len({d[0] for d in DENOMINACIONES}) != 15:
        err.append('DENOMINACIONES debe tener las 15 filas del ES')
    for f, es, xes, en, xen in DENOMINACIONES:
        m = re.search(r'\$(\d+)|(\d+)¢', en)
        cara = float(m.group(1)) if m and m.group(1) else (float(m.group(2)) / 100 if m else None)
        if en.endswith(' roll'):
            cara = {0.25: 10.0, 0.1: 5.0}.get(cara)              # 40 quarters · 50 dimes
        if len(en) > 10:
            err.append('rótulo de denominación > 10 caracteres (ancho de la columna A): %s' % en)
        if cara != xen:
            err.append('denominación con valor distinto del rótulo: %s ×%s' % (en, xen))
    if sorted(CALENDARIO) != list(FILAS_CALENDARIO):
        err.append('CALENDARIO debe cubrir las filas %d-%d del BONUS-02' % (FILAS_CALENDARIO[0], FILAS_CALENDARIO[-1]))
    for k, (val, fuente) in REGLAS_US.items():
        if not fuente:
            err.append('regla sin fuente: ' + k)
    for k, v in ADAPTAR.items():
        if k in POR_CELDA:
            err.append('ADAPTAR y POR_CELDA sobre la misma celda: %r' % (k,))
        if not v.strip():
            err.append('ADAPTAR vacío: %r' % (k,))
    for k, (es, en) in FORMULAS_POR_CELDA.items():
        nuevos = numeros_formula(en) - numeros_formula(es) - set(VALORES_DENOMINACION_EN) - {float(k[2][1:])}
        if nuevos:
            err.append('FORMULAS_POR_CELDA con cifras no declaradas %s: %r' % (sorted(nuevos), k))
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
    textos_celda = {}
    formulas_celda = {}
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
            for coord, txt in hd.get('textos', {}).items():
                textos_celda[(c, h, coord)] = txt
            for coord, fx in hd.get('formulas', {}).items():
                formulas_celda[(c, h, coord)] = fx
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
            por_rango = OrderedDict()
            for cf in hd['cf']:
                por_rango.setdefault(cf['sqref'], []).extend(cf['tokens'])
            for rng, toks in por_rango.items():
                toks_en = [CLAVES.get(t, t) for t in toks]
                if len(set(t.lower() for t in toks_en)) != len(set(t.lower() for t in toks)):
                    err.append('tokens de CF EN no inyectivos en %s / %s / %s' % (c, h, rng))
                cs = _celdas(rng)
                for lit, celdas in hd['literales'].items():
                    if not (cs & set(celdas)) or not necesita_clave(lit):
                        continue
                    en = CLAVES.get(lit, lit)
                    esperado = {CLAVES.get(t, t).lower() for t in tokens_en(lit, toks)}
                    real = {t.lower() for t in tokens_en(en, toks_en)}
                    if esperado != real:
                        err.append('el literal %r cambia de color en %s / %s / %s' % (en, c, h, rng))
    for es in FORMULAS_EN:
        if es not in patrones:
            err.append('patrón de mapas.FORMULAS_EN que no está en el censo: ' + es[:110])
    for k in PATRONES_SIN_CAMBIO - primeras:
        err.append('PATRONES_SIN_CAMBIO cita un patrón que no está en el censo: %r' % (k,))
    for k, (es, en) in FORMULAS_POR_CELDA.items():
        if formulas_celda.get(k) != es:
            err.append('FORMULAS_POR_CELDA: %r no tiene en el ES la fórmula %r (tiene %r)' % (k, es, formulas_celda.get(k)))
    for nombre, dic in (('POR_CELDA', POR_CELDA), ('ADAPTAR', ADAPTAR)):
        for k in dic:
            if k not in textos_celda:
                err.append('%s cita una celda sin texto en el ES: %r' % (nombre, k))
    for f, es, xes, en, xen in DENOMINACIONES:
        if textos_celda.get((HOJA_CAJA[0], HOJA_CAJA[1], 'A%d' % f)) != es:
            err.append('DENOMINACIONES: la fila %d del ES no es %r' % (f, es))
    todos = set(textos_celda.values())
    for k in GLOSARIO:
        if k not in todos and k not in GLOSARIO_OPCIONAL:
            err.append('GLOSARIO con una clave que no es una celda del ES: %r' % k)
    return err


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
    for x in e:
        print('ERROR', x)
    print('mapas.py: {} ficheros · {} pestañas · {} glosario · {} por celda · {} adaptar · {} fórmulas por celda · '
          '{} errores'.format(len(FICHEROS), len(HOJAS), len(GLOSARIO), len(POR_CELDA), len(ADAPTAR),
                              len(FORMULAS_POR_CELDA), len(e)))
    raise SystemExit(1 if e else 0)
