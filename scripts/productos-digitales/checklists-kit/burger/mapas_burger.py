#!/usr/bin/env python3
"""
mapas_burger.py — Burger Joint Checklists Kit Pro (EN) · DELTA del Kit de Tareas para Hamburguesería
(`kit-tareas-hamburgueseria`, 11 xlsx v2.0) sobre `mapas.py` (Restaurant Checklists Kit Pro). SPEC: `burger/SPEC.md`
(solo el delta). Quinto hermano vertical, hecho como el bar, la cafetería, el catering y la pizzería. Sesión Claude
Code, 18-oct-2026.

Se usa con `--kit burger` (kit.py). Importa `mapas.py` y SOLO añade o sobrescribe: producto, ficheros, títulos,
pestañas (la hamburguesería tiene la estructura de la pizzería: sin barra, con estación de plancha, make line,
freidora, parrillero, freidurista e inventario diario), glosario de hamburguesería (puestos, unidades del inventario),
calendario (misma estructura que el base: filas 5-26; cambian los días fuertes de un burger joint US), POR_CELDA (caja
09 heredada TAL CUAL; 05 «Quarterly & Annual» con plancha, freidoras y aceite usado; el orden de la apertura de cocina
del 01 y del cierre del 08), VALORES_EN (mínimos del inventario en lb / oz y como número), ADAPTAR, CLAVES (+ «⚠️
PEDIR») y REGLAS_US (+ carne picada a 155 °F / aviso al consumidor, TCS crudo, pollo, aceite según el fabricante,
alérgenos del pan). La hora de 12 h, la caja en dólares y el resto se heredan. Las funciones del base que leen
constantes (titulo_interior, autotest, cruzar_censo) se re-enlazan a ESTE módulo. Ejecutado como script: autotest +
cruce con burger/censo_es.json + cruce con el base (lo heredado por celda tiene el mismo texto ES).

    python3 burger/mapas_burger.py
"""
import os
import sys
import types
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
import mapas as _base                                            # noqa: E402
from mapas import *                                              # noqa: E402,F401,F403
from mapas import _h12, _num, _celdas                            # noqa: E402,F401
AQUI = os.path.dirname(os.path.abspath(__file__))              # burger/ (el import * trae el AQUI del base)

ORIGEN_ES = 'kit-tareas-hamburgueseria'
PRODUCTO = 'Burger Joint Checklists Kit Pro'
TITULO_SEO = 'Burger Joint Checklists Kit Pro: Burger Restaurant Opening & Closing Checklist Templates for Excel'
SLUG = 'burger-joint-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_BURGER_JOINT_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
MARCA_ES = '— Kit de Tareas Recurrentes · Hamburguesería · AI Chef Pro · aichef.pro'
MARCA_EN = '— ' + PRODUCTO + ' · AI Chef Pro · aichef.pro'
VARIANTES_ES = ('Hamburguesería',)
# heredar.py: memoria con VARIAS fuentes, en orden de preferencia (base, bar, cafetería, catering, pizzería; gana la
# primera que acierta)
_SUF = lambda v: [(' — Hamburguesería', ' — ' + v), (' · Hamburguesería', ' · ' + v)]  # noqa: E731
MEMORIA = [('base', '', _SUF('Restaurante Casual')), ('bar', 'bar', _SUF('Bar / Cocktails')),
           ('cafe', 'cafe', _SUF('Cafetería / Brunch')), ('catering', 'catering', _SUF('Catering / Eventos')),
           ('pizza', 'pizza', _SUF('Pizzería'))]
# heredar.py: EN heredado que en un burger joint no vale tal cual → pendientes (motivo «contexto»). «restaurant» SÍ
# vale aquí («burger restaurant»); lo de la pizzería (masa, horno de leña, repartidor propio), la cafetería, el bar y
# el catering, no. «sidewalk cafe» (el permiso de terraza) sí vale.
RX_CONTEXTO_PENDIENTE = (r'(?i)\b(?:pizzas?|pizzerias?|pizza makers?|dough|mozzarella|wood-fired|peels?|slices?|'
                         r'ovens?|pizza prep table|delivery drivers?|host stands?|head chefs?|sous chefs?|'
                         r'MOD|coffee shops?|(?<!sidewalk )cafes?|baristas?|shift leads?|kitchen leads?|bussers?|'
                         r'pastry case|barbacks?|bartenders?|cocktails?|venues?|banquets?|BEOs?|commissary|'
                         r'line-up|brunch)\b')
# heredar.py: cadenas idénticas a una fuente cuyo EN no vale en la hamburguesería (→ pendientes → G1.json, con base_en)
NO_HEREDAR = {
    'Abrir persianas / puerta principal': 'ronda 1 m15 del bar: + salidas de emergencia despejadas y señales de salida',
    'Pan brioche': 'en una hamburguesería es el pan de la burger: «Brioche buns» (la cafetería dice «bread»)',
    'Guardar pan sobrante en bolsa hermética': 'en una hamburguesería son los buns: «leftover buns» (la cafetería dice '
                                               '«bread»)',
}
# gates_en.py G2: términos de otros kits que NINGUNA celda EN de la hamburguesería puede llevar. «restaurant» está
# permitido («burger restaurant»); «sidewalk cafe permit» queda fuera por el lookbehind.
# TERMINO_PROHIBIDO_EJEMPLO: lo que inyecta el autotest.
TERMINOS_PROHIBIDOS = (r'(?i:\b(?:pizzas?|pizzerias?|dough|mozzarella|wood-fired|host stands?|head chefs?|'
                       r'sous chefs?|coffee shops?|(?<!sidewalk )cafes?|baristas?|tip jars?|shift leads?|'
                       r'kitchen leads?|bussers?|barbacks?|cocktails?|banquets?|BEOs?|commissary|venues?|line-up)\b)'
                       r'|\bMOD\b')
TERMINO_PROHIBIDO_EJEMPLO = 'Ask the shift lead.'
REFERENCIAS_TRADUCTOR = ['burger/SPEC.md', 'SPEC.md §0-§3 y §7.2 (brief)', 'textos_en/glosario.json (glosario de la '
                         'prosa del kit base)', 'burger/textos_en/heredado.json (cómo se dijo ya cada cosa: base, bar, '
                         'cafetería, catering y pizzería)', 'burger/mapas_burger.py: GLOSARIO, HOJAS, FICHEROS, '
                         'TITULOS, POR_CELDA, REGLAS_US', '../GLOSARIO-JERGA-ES-EN.md']
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v2.0'),
    ('keywords', 'burger joint checklist, burger restaurant checklist, burger shop opening checklist, burger restaurant '
                 'closing checklist, burger kitchen cleaning checklist, grill station checklist, AI Chef Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

# ==========================================================================
# Ficheros (D5: «burger joint» 60.500/mes US con intención local, «burger shop» 14.800, variantes de checklist sin
# volumen: los ficheros combinan burger joint / burger shop / burger restaurant)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-apertura-cierre.xlsx', '01-burger-joint-opening-closing-checklists.xlsx'),
    ('02-partidas-cocina.xlsx', '02-burger-kitchen-station-checklists.xlsx'),
    ('03-tareas-manager.xlsx', '03-burger-restaurant-manager-checklist.xlsx'),
    ('04-tareas-perfiles.xlsx', '04-burger-shop-duties-by-role.xlsx'),
    ('05-tareas-semanales-mensuales.xlsx', '05-burger-restaurant-cleaning-checklist-inventory-maintenance.xlsx'),
    ('06-eventos-festivos.xlsx', '06-burger-joint-event-checklists.xlsx'),
    ('07-plantilla-personalizable.xlsx', '07-blank-burger-shop-checklist-template.xlsx'),
    ('08-apertura-cierre-negocio.xlsx', '08-burger-restaurant-opening-closing-checklist.xlsx'),
    ('09-apertura-cierre-caja.xlsx', '09-cash-drawer-opening-closing.xlsx'),
    ('BONUS-01-briefing-servicio.xlsx', 'BONUS-01-burger-joint-pre-shift-meeting-template.xlsx'),
    ('BONUS-02-calendario-anual-tareas.xlsx', 'BONUS-02-burger-joint-holiday-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)
TITULOS = OrderedDict([
    ('01-burger-joint-opening-closing-checklists.xlsx',
     'Burger Joint Opening & Closing Checklists: Kitchen, FOH & Takeout'),
    ('02-burger-kitchen-station-checklists.xlsx', 'Burger Kitchen Station Checklists: Grill, Make Line & Fry Station'),
    ('03-burger-restaurant-manager-checklist.xlsx',
     'Burger Restaurant Manager Checklist: Daily, Weekly, Monthly & Shift Handover'),
    ('04-burger-shop-duties-by-role.xlsx',
     'Burger Shop Duties by Role: Grill Cook, Line Cook, Fry Cook, Shift Manager & Server'),
    ('05-burger-restaurant-cleaning-checklist-inventory-maintenance.xlsx',
     'Burger Restaurant Cleaning Checklist, Inventory & Maintenance Schedule'),
    ('06-burger-joint-event-checklists.xlsx', 'Burger Joint Event Checklists: Game Night, Burger Week, Holidays & Patio'),
    ('07-blank-burger-shop-checklist-template.xlsx', 'Blank Burger Shop Checklist Template (Editable)'),
    ('08-burger-restaurant-opening-closing-checklist.xlsx',
     'Burger Restaurant Opening & Closing Checklist (Whole Building)'),
    ('09-cash-drawer-opening-closing.xlsx', 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log'),
    ('BONUS-01-burger-joint-pre-shift-meeting-template.xlsx',
     'BONUS: Burger Joint Pre-Shift Meeting Template (Huddle Notes)'),
    ('BONUS-02-burger-joint-holiday-calendar.xlsx', 'BONUS: Burger Joint Holiday & Busy Days Calendar (US)'),
])
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

HOJAS = OrderedDict(_base.HOJAS)
HOJAS.update([
    ('Plancha Grill', 'Grill Station'), ('Línea Montaje', 'Make Line'), ('Freidora', 'Fry Station'),
    ('Parrillero', 'Grill Cook'), ('Cocinero Línea', 'Line Cook'), ('Freidurista', 'Fry Cook'),
    ('Encargado', 'Shift Manager'), ('Inventario Diario', 'Daily Inventory'),
    ('Noche Fútbol', 'Game Night'), ('Burger Week', 'Burger Week'), ('Navidad', 'Holiday Season'),
])
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Apertura Cocina', 'Apertura Sala', 'Cierre Cocina', 'Cierre Sala']),
    ('02', ['Instrucciones', 'Plancha Grill', 'Línea Montaje', 'Freidora']),
    ('03', ['Instrucciones', 'Diario Manager', 'Semanal Manager', 'Mensual Manager', 'Handover Turno']),
    ('04', ['Instrucciones', 'Parrillero', 'Cocinero Línea', 'Freidurista', 'Encargado', 'Camarero']),
    ('05', ['Instrucciones', 'Inventario Diario', 'Limpieza Semanal', 'FIFO Semanal', 'Mantenimiento Mensual',
            'Trimestral y Anual']),
    ('06', ['Instrucciones', 'Noche Fútbol', 'Burger Week', 'Navidad', 'Temporada Terraza']),
    ('07', ['Instrucciones', 'Por Franja Horaria', 'Por Área', 'Por Perfil']),
    ('08', ['Instrucciones', 'Apertura del Negocio', 'Cierre del Negocio']),
    ('09', ['Instrucciones', 'Apertura de Caja', 'Cierre de Caja', 'Registro Mensual']),
    ('B01', ['Instrucciones', 'Briefing']),
    ('B02', ['Instrucciones', 'Calendario Anual']),
])

# ==========================================================================
# GLOSARIO: el base entero (opcional en la hamburguesería) + celdas cortas del burger joint. Jerga US: grill cook,
# fry cook, line cook, shift manager; unidades del inventario en lb / oz / qt (VALORES_EN).
# ==========================================================================
GLOSARIO = OrderedDict(_base.GLOSARIO)
_GLOSARIO_BURGER = OrderedDict([
    ('Parrillero', 'Grill cook'), ('Cocinero plancha', 'Grill cook'), ('Freidurista', 'Fry cook'),
    ('Cocinero freidora', 'Fry cook'), ('Cocinero línea', 'Line cook'),
    ('Encargado/a', 'Shift manager'), ('Camarero/a', 'Server'), ('Turno saliente', 'Outgoing shift'),
    ('Responsable de caja', 'Cashier / shift manager'), ('Jefe de Cocina', 'Kitchen manager'),
    ('Jefe de Sala', 'FOH manager'), ('Recepción', 'Front counter'), ('Todos', 'All staff'),
    ('Auxiliar', 'Dishwasher / prep'),
    ('Office', 'Office'), ('Almacén', 'Storage'), ('Cámara', 'Walk-in'),
    ('Primavera', 'Spring'), ('Otoño', 'Fall'),
    # inventario (05): unidades US; los mínimos de kg y g cambian de cifra (VALORES_EN), los de L y uds no
    ('kg', 'lb'), ('g', 'oz'), ('L', 'qt'), ('uds', 'ea'), ('Unidad', 'Unit'),
])
GLOSARIO.update(_GLOSARIO_BURGER)
GLOSARIO_OPCIONAL = frozenset(_base.GLOSARIO)
PUESTOS_ES = frozenset(_base.PUESTOS_ES | {'Parrillero', 'Cocinero plancha', 'Freidurista', 'Cocinero freidora',
                                           'Cocinero línea', 'Encargado/a', 'Camarero/a', 'Turno saliente', 'Todos',
                                           'Office', 'Almacén', 'Cámara'})

# ==========================================================================
# CLAVES: el inventario diario avisa con «⚠️ PEDIR» / «OK» (literales de fórmula)
# ==========================================================================
CLAVES = OrderedDict(_base.CLAVES)
CLAVES.update([('⚠️ PEDIR', '⚠️ REORDER'), ('OK', 'OK')])

# ==========================================================================
# BONUS-02 «Holiday Calendar»: misma estructura que el base (filas 5-26: A mes · B fecha/evento · C tareas ·
# D antelación). A, B y D fijados; C = traductor, con ADAPTAR donde la tarea de la hamburguesería cambia. Los días
# fuertes de un burger joint US (Super Bowl, March Madness, el mes de la hamburguesa, el 4 de julio, la temporada de
# fútbol americano, Halloween, Nochevieja). fila → (mes, evento, antelación, ADAPTAR de C o None). Orden cronológico.
# ==========================================================================
CALENDARIO = OrderedDict(_base.CALENDARIO)
CALENDARIO.update([
    (6, ('February', 'Super Bowl Sunday (2nd Sunday in Feb)', '2 weeks',
         'Sustituye a Reyes. Uno de los días de más pedidos para llevar y a domicilio del año en EE. UU.: pedidos '
         'grandes y anticipados (party orders), más patties y pan, cajas extra y menú corto para sacar más pedidos por '
         'hora')),
    # orden cronológico (lección m10 de la pizzería): la Cuaresma empieza en febrero → filas 9↔10; el mes de la
    # hamburguesa (mayo) antes que «May–June» → filas 12↔13. Su C (las tareas) va por POR_CELDA (_CAL_C) con el EN ya
    # traducido de su fila de origen
    (9, ('February–April', 'Lent Fridays + Easter Sunday (varies)', '2 weeks', None)),
    (10, ('March', "Mar 17 — St. Patrick's Day + March Madness", '2 weeks', None)),
    (12, ('May', 'National Burger Month (May 28: National Hamburger Day)', '2 weeks', None)),
    (13, ('May–June', 'Graduation season', '1 month', None)),
    (14, ('May', "2nd Sunday — Mother's Day", '2 weeks', None)),
    (16, ('June', "3rd Sunday — Father's Day", '2 weeks',
          'Sustituye a San Juan. Tareas = las del Día del Padre del ES (fila 9): menú familiar de mediodía, reservas '
          'ampliadas y burger XL para compartir')),
    (17, ('July', 'Jul 4 — Independence Day', '1 week',
          'Sustituye a la fila de temporada alta (sus tareas pasan a la fila 18). Tareas: decidir el horario (muchos '
          'cierran o abren solo de día), patio a pleno rendimiento, pedidos grandes para las fiestas (party orders)')),
    (18, ('July–August', 'Summer peak season', 'Ongoing',
          'Tareas = las de «Temporada alta» de la fila 17 del ES (sin el calco «servicio de festivo»): personal extra, '
          'horario ampliado, carta de verano; más refuerzo de turnos y de delivery y patio a pleno rendimiento')),
    (19, ('September', 'Labor Day (1st Monday) + football season + Sep 18: National Cheeseburger Day', '2 weeks',
          'Fin del verano. Tareas: carta de otoño, lunch specials de la vuelta al cole (sin el calco «vuelta a la '
          'rutina»), combos para el fútbol americano (jueves, domingo y lunes por la noche y el universitario del '
          'sábado) y una oferta de cheeseburger el día 18')),
    (20, ('October', 'Oct 31 — Halloween', '1 week',
          'Decoración temática y una burger especial de Halloween; noche fuerte de delivery: packaging y turnos extra')),
    (21, ('November', 'Thanksgiving (4th Thursday) + Black Friday', '1 month',
          'Sustituye a Todos los Santos. Decidir si se abre el jueves (muchos cierran); el viernes (Black Friday), '
          'burger de temporada y refuerzo del mediodía para la gente que sale de compras')),
    (23, ('Nov–Dec', 'Holiday gift card season', '2 weeks',
          'Sustituye al puente de la Constitución. Del Black Friday a Nochebuena. Tareas: promoción de tarjetas '
          'regalo, expositor junto a la caja (register), venta online y en la app de pedidos')),
    (24, ('December', 'Holiday parties (office orders)', '1 month',
          'Sustituye a las cenas de empresa. Tareas: pedidos de empresa para las fiestas de oficina (burgers y sides '
          'para grupos, con hora de recogida o entrega), reservas de grupo, turnos extra')),
    (26, ('December', "Dec 31 — New Year's Eve", '2 weeks',
          'Sin uvas, cava ni cotillón español. Horario de cierre y turnos de noche; si abres la sala hasta tarde, '
          'party favors y brindis a medianoche (con alcohol solo si tu licencia lo permite, 21+ con ID; regalarlo, '
          'solo donde tu estado lo permita)')),
])

# ==========================================================================
# POR_CELDA: lo heredado del base (mismo texto ES en la misma celda o en la fila equivalente; lo comprueba
# cruzar_base) + lo de la hamburguesería
# ==========================================================================
_HEREDA_POR_CELDA = [k for k in _base.POR_CELDA if k[0] == '09'] + [
    ('05', 'Trimestral y Anual', 'B6'), ('05', 'Trimestral y Anual', 'D6'), ('05', 'Trimestral y Anual', 'E6')]
POR_CELDA = OrderedDict((k, _base.POR_CELDA[k]) for k in _HEREDA_POR_CELDA)
_T = ('05', 'Trimestral y Anual')
POR_CELDA.update([
    # 03 · conservación de fichajes (B16 en el base; mismo texto EN)
    (('03', 'Mensual Manager', 'B9'), _base.POR_CELDA[('03', 'Mensual Manager', 'B16')]),
    # 05 · Inventario: la línea de marca va con otro formato en el ES (dos puntos y raya final) → la del kit con su
    # raya final (no es la línea D19: G3 cuenta las MARCA_EN contra las MARCA_ES del ES)
    (('05', 'Inventario Diario', 'A40'), MARCA_EN + ' —'),
    # 05 · Instrucciones (errata ES, como en la cafetería y la pizzería): el inventario no está protegido y el ES lo
    # promete
    (('05', 'Instrucciones', 'B24'), '▸ Checklist sheets with formulas are protected WITHOUT a password: the input cells '
                                     '(the green ones) are unlocked. The Daily Inventory sheet is left unprotected so '
                                     "you can add products: don't type over the Status column."),
    # 05 · Trimestral y Anual: servicios contratados US de un burger joint (plancha y freidoras: NFPA 96)
    (_T + ('B7',), 'Hood and duct cleaning by a certified contractor (NFPA 96): quarterly if high volume or charbroil, '
                   'semiannual if moderate — the griddle and the fryers together grease up the duct fast'),
    (_T + ('D7',), 'Hood cleaning co.'), (_T + ('E7',), 'Quarterly'),
    (_T + ('B8',), 'Annual extinguisher maintenance by a licensed fire protection company: new tag and record (OSHA '
                   '1910.157); hood fire suppression inspected every 6 months (NFPA 96)'),
    (_T + ('D8',), 'Fire safety co.'),
    (_T + ('B9',), 'Extinguisher hydrostatic test by the fire protection company: Class K (wet chemical) and CO2 '
                   'units every 5 years, dry chemical as its label says (OSHA 1910.157(f); NFPA 10)'),
    (_T + ('D9',), 'Fire safety co.'),
    (_T + ('B10',), 'Gas lines and appliance connections (griddle, fryers, range) checked by a licensed pro, as often '
                    'as your local code requires'),
    (_T + ('D10',), 'Licensed plumber'), (_T + ('E10',), 'Annual'),
    (_T + ('B11',), 'Refrigeration service by an EPA 608-certified tech: walk-in, reach-ins and the make line — coils, '
                    'gaskets and refrigerant leak check'),
    (_T + ('D11',), 'Refrigeration tech'),
    (_T + ('A12',), '  WATER, WASTE & USED OIL'),
    (_T + ('B13',), 'Used fryer oil pickup by a licensed recycler: file the pickup receipts (with fryers running all '
                    'day, it is one of the biggest waste streams in a burger joint)'),
    (_T + ('D13',), 'Oil recycler'),
    (_T + ('B14',), 'Review the waste and recycling hauler contract and local recycling rules: takeout and delivery '
                    'multiply the cardboard and packaging'),
    (_T + ('B15',), 'Legionella: if you have a cooling tower or at-risk hot water, keep a water management program as '
                    'your local health code requires'),
    (_T + ('D15',), 'Water treatment co.'),
    (_T + ('B16',), "Water quality: on city water, read your utility's annual Consumer Confidence Report; on a private "
                    'well or tank, test it as your health department requires; service any filter or softener per its '
                    'maker'),
    (_T + ('D16',), 'Water lab'),
    (_T + ('B18',), "Review insurance (general liability, property, workers' comp; liquor liability if you serve "
                    'alcohol) and renewal dates'),
    (_T + ('B19',), 'POS check: software updates, sales tax rates and settings, user permissions — plus the online '
                    'ordering and delivery app integrations'),
])
# 01 · Apertura Cocina (errata ES): la comprobación de que la campana tira iba DESPUÉS de encender plancha y freidora.
# Mismas filas 12-18 (zona y responsable iguales en todas): campana → que tire → gas → plancha → freidora → tostador →
# temperatura del aceite. El °C del ES (B14 y B16) pasa con su tarea a B15 y B18 (CELSIUS_SIN_F declara B14 y B16)
_AC = ('01', 'Apertura Cocina')
_APERTURA = [
    ('Turn on the hood and ventilate the kitchen BEFORE any equipment: the griddle and the fryers are the two big '
     'sources of smoke and grease', '10:45 AM'),
    ('Check the hood really draws (a napkin held against the filters stays put) and the filters are in place and '
     'clean', '10:45 AM'),
    ("Open the main gas valve and make sure there is NO gas smell before lighting anything; if you smell gas, don't "
     'turn anything on or touch a switch: get out and call the gas utility or 911 from outside', '10:45 AM'),
    ('Turn on the flat-top griddle / grill and preheat it (about 400–450 °F)', '11:00 AM'),
    ('Turn on the fryers and check the oil level', '11:00 AM'),
    ('Turn on the bun toaster or oven if you toast the buns in it', '11:00 AM'),
    ('Check the fryer oil temperature (350–355 °F for fries)', '11:15 AM'),
]
for _fila, (_b, _e) in enumerate(_APERTURA, 12):
    POR_CELDA[_AC + ('B%d' % _fila,)] = _b
    POR_CELDA[_AC + ('E%d' % _fila,)] = _e
# 08 · Cierre (errata ES): limpiar planchas y filtrar el aceite iba DESPUÉS de la alarma y la llave. Toda la secuencia,
# mismas 14 filas y mismos contadores (E = «Close»): plancha y freidoras al principio (con la campana aún en marcha),
# luego el local, y alarma y llave al final
_CN = ('08', 'Cierre del Negocio')
_CIERRE = [
    ('Turn off background music', 'General', 'Shift manager'),
    ('Make sure no guests remain inside', 'FOH', 'Shift manager'),
    ('Clean and bring in the patio if used', 'Patio', 'Shift manager'),
    ('Griddles and fryers: clean the griddles and filter or change the fryer oil as the fryer maker says, before the '
     'hood goes off', 'Kitchen', 'Closing line cook'),
    ('Turn off the POS / card terminal (or leave on standby)', 'Register', 'Shift manager'),
    ('Bring in the outdoor signage', 'Outside', 'Shift manager'),
    ('Empty trash cans in common areas and restrooms', 'Restrooms', 'Shift manager'),
    ('Final safety check (gas, water, outlets; griddles and fryers off)', 'General', 'Shift manager'),
    ('Check that windows are closed', 'General', 'Shift manager'),
    ('Turn off HVAC', 'General', 'Shift manager'),
    ('Turn off lights (leave security lighting)', 'General', 'Shift manager'),
    ('Set the alarm', 'Entrance', 'Last one out'),
    ('Close security gate and doors', 'Entrance', 'Last one out'),
    ('Lock up and verify it is locked', 'Entrance', 'Last one out'),
]
for _fila, (_b, _c, _d) in enumerate(_CIERRE, 5):
    for _col, _v in (('B', _b), ('C', _c), ('D', _d)):
        POR_CELDA[_CN + ('%s%d' % (_col, _fila),)] = _v
# las tareas (C) de las filas intercambiadas del calendario, con su EN (el G1 de su fila de origen)
_CAL_C = OrderedDict([
    (9, 'Meatless Fridays in Lent: a fish or veggie burger option; Easter Sunday: decide hours'),
    (10, 'Burger special of the day; March Madness games fill the dining room and lift delivery: extra shifts; beer only '
         'with a license and 21+ with ID, no 2-for-1 drink deals (several states ban them)'),
    (12, 'Burger special of the month; May 28 deal on social media and the delivery apps; extra beef and buns'),
    (13, 'Set group menu, deposit and price per person, private area; big carryout party orders for graduations'),
])
for _fila, _v in _CAL_C.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'C%d' % _fila)] = _v
# lecciones de la ronda 1 de la pizzería (pizza/revision/REVISION-F2.md) en las mismas celdas de la hamburguesería
for _k, _v in (
        (('01', 'Apertura Cocina', 'D10'), 'Shift manager'),                    # m13: el control de salud, el PIC
        (('08', 'Apertura del Negocio', 'E20'), '11:00 AM'),                     # m2: plancha y freidoras con la
        (('08', 'Apertura del Negocio', 'E21'), '11:00 AM'),                     # campana, a la hora del 01
        (('07', 'Por Área', 'A19'), '  COUNTER / BAR — type your counter or bar tasks below'),   # m21
        (('B01', 'Briefing', 'B26'), 'Counter staff (and bar staff, if any):'),           # m21
        (('B01', 'Briefing', 'B6'), 'Expected covers + takeout / delivery orders:')):     # m21
    POR_CELDA[_k] = _v
for _f in range(20, 25):
    POR_CELDA[('07', 'Por Área', 'C%d' % _f)] = 'Counter / bar'                   # m21: «Barra» = mostrador
for _fila, (_mes, _evento, _antel, _dir) in CALENDARIO.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'A%d' % _fila)] = _mes
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'B%d' % _fila)] = _evento
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'D%d' % _fila)] = _antel

# ==========================================================================
# VALORES_EN: (libro, hoja ES, celda) → (valor ES tal cual, valor EN). Los mínimos del «Inventario Diario» vienen
# como TEXTO en el ES («40»): la fórmula «B<D» compara un número con un texto y pide SIEMPRE (errata ES, como la
# cafetería y la pizzería). La EN los escribe como NÚMERO; los de kg y g, convertidos a lb y oz (redondeado a una
# cifra de pedido); los de L (→ qt) y uds (→ ea), con la misma cifra.
# ==========================================================================
_MINIMOS = [  # fila, ES, EN
    (6, '40', 40), (7, '50', 50), (8, '2', 4), (9, '20', 20), (11, '40', 40), (12, '20', 20), (13, '20', 20),
    (15, '50', 50), (16, '20', 20), (17, '300', 11), (18, '20', 20), (20, '5', 5), (21, '8', 8), (22, '5', 5),
    (23, '0.5', 1), (24, '300', 11), (25, '1', 1), (26, '0.5', 0.5), (27, '0.5', 0.5), (28, '0.5', 0.5),
    (30, '10', 22), (31, '2', 4), (32, '30', 30), (33, '1', 2), (35, '40', 40), (36, '40', 40), (37, '30', 30),
    (38, '100', 100),
]
VALORES_EN = OrderedDict((('05', 'Inventario Diario', 'D%d' % f), (es, en)) for f, es, en in _MINIMOS)

# ==========================================================================
# ADAPTAR (en español, con el dato US; las cifras y normas salen de REGLAS_US)
# ==========================================================================
_A = _base.ADAPTAR
_CAMARAS = _A[('01', 'Apertura Cocina', 'B18')]
_TEMP_FRIO = _A[('01', 'Cierre Cocina', 'B12')]
_LAVADO = _A[('02', 'Fríos', 'B6')]
_DATE = _A[('01', 'Cierre Cocina', 'B6')]
_TIRA = 'sanitizante aprobado a la concentración de la etiqueta, medida con tira (test strip) (FDA Food Code 4-501.114)'
_ALERGENOS = ('Alérgenos US: los 9 principales (FALCPA + FASTER Act: leche, huevo, pescado, crustáceos, frutos de '
              'cáscara, cacahuete, trigo, soja y sésamo); en una hamburguesería, el pan (bun) suele llevar trigo, leche, '
              'huevo, soja y sésamo, el queso lleva leche y las salsas, huevo. El gluten en sí no es uno de los 9 (el '
              'trigo sí), la mostaza tampoco (en UK sí) y la lactosa es una intolerancia, no un alérgeno: se recogen '
              'igual; en UK, los 14')
_TCS_CRUDO = ('La carne picada cruda es TCS: sale de la cámara en tandas pequeñas y se mantiene a 41 °F o menos hasta '
              'la plancha (cajón refrigerado bajo la plancha o reach-in), sin «temperarla» a temperatura ambiente (FDA '
              'Food Code 3-501.16); si se trabaja con time as a public health control: procedimiento escrito, hora '
              'marcada y a la basura a las 4 h (FDA Food Code 3-501.19)')
_PICADA = ('Carne picada (ground beef): 155 °F durante 17 s en el centro, medida con termómetro de sonda (FDA Food Code '
           '3-401.11(A)(2); equivalentes de la tabla: 145 °F 3 min · 150 °F 1 min · 158 °F al instante). Poco hecha '
           'solo si el cliente la pide y la carta lleva el aviso al consumidor (consumer advisory, FDA Food Code '
           '3-603.11); la del menú infantil, siempre hecha (3-401.11(D)). Sin los 75 °C del ES')
_PUNTO = ('Punto de la carne → doneness: 155 °F durante 17 s salvo que el cliente la pida poco hecha y la carta lleve el '
          'aviso al consumidor (FDA Food Code 3-401.11 y 3-603.11); la del menú infantil, siempre hecha')
_POLLO = ('Pollo (nuggets, tenders, crispy): hasta 165 °F en el centro, comprobado con sonda (FDA Food Code '
          '3-401.11(A)(3)); se fríe desde congelado como diga el fabricante')
_ACEITE = ('Filtrar o cambiar el aceite como diga el fabricante de la freidora (muchas llevan filtrado incorporado '
           'pensado para el aceite caliente; otras piden dejarlo enfriar), con guantes resistentes al calor, delantal y '
           'gafas. Sin cifra de temperatura del kit')
_TPM = ('Test polares → medidor de TPM (total polar materials, oil quality tester); en EE. UU. no hay límite federal: '
        'el aceite se cambia según el fabricante del medidor y de la freidora (sin cifra)')
_ENFRIAR = ('Lo cocinado se enfría de 135 °F a 70 °F en 2 h y a 41 °F en 4 h más (FDA Food Code 3-501.14) antes de '
            'guardarlo tapado')
_RECALENTAR = ('Lo hecho antes que se vaya a mantener en caliente se recalienta a 165 °F en 2 h como máximo (FDA Food '
               'Code 3-403.11) y se mantiene a 135 °F o más')
_BACON = 'Bacon precocinado: si se guarda, ' + _ENFRIAR[0].lower() + _ENFRIAR[1:] + '; si se mantiene en caliente, ' + \
    _RECALENTAR[0].lower() + _RECALENTAR[1:]
_HUEVO = ('con huevo pasteurizado, o aviso al consumidor en la carta si lleva huevo crudo o poco hecho (FDA Food Code '
          '3-603.11)')
_CARNE_GUARDAR = ('Carne picada cruda: tapada, con fecha, a 41 °F o menos y en la balda de abajo, por debajo de lo listo '
                  'para consumir (FDA Food Code 3-302.11)')
_PATTIES = ('Patties formados con antelación: tapados, con fecha, a 41 °F o menos y separados de lo listo para consumir '
            '(FDA Food Code 3-302.11)')
_APPS = 'Plataformas US: DoorDash, Uber Eats y Grubhub (third-party delivery apps)'
_HEREDA_ADAPTAR = [('01', 'Apertura Cocina', 'B9'), ('01', 'Apertura Cocina', 'B10'),
                   ('08', 'Apertura del Negocio', 'B8'), ('09', 'Cierre de Caja', 'B10'),
                   ('09', 'Registro Mensual', 'A37'),
                   ('B02', 'Instrucciones', 'B8')] + [k for k in _A if k[:2] == ('09', 'Instrucciones')]
ADAPTAR = OrderedDict((k, _A[k]) for k in _HEREDA_ADAPTAR)
ADAPTAR.update([
    # 01 · cocina (filas 12-18 de la apertura: POR_CELDA)
    (('01', 'Apertura Cocina', 'B7'), _A[('01', 'Apertura Cocina', 'B7')]),
    (('01', 'Apertura Cocina', 'B20'), _CAMARAS),
    (('01', 'Apertura Cocina', 'B21'), _TCS_CRUDO),
    (('01', 'Apertura Cocina', 'B25'), 'Si la salsa se cocina (BBQ): ' + _ENFRIAR + '; la burger sauce o la mayonesa '
     'casera, ' + _HUEVO),
    (('01', 'Apertura Cocina', 'B27'), _BACON),
    (('01', 'Apertura Cocina', 'B32'), 'Coleslaw (col cortada, TCS): a 41 °F o menos y con date marking: 7 días como '
     'máximo contando el día de preparación (FDA Food Code 3-501.16 y 3-501.17)'),
    (('01', 'Apertura Cocina', 'B38'), 'Lavarse las manos y ponerse guantes nuevos al pasar de la carne cruda a lo listo '
     'para consumir: pan, toppings y salsas (FDA Food Code 2-301.14 y 3-304.15); tabla, pinzas y espátula de crudo, '
     'aparte (FDA Food Code 3-302.11)'),
    (('01', 'Apertura Cocina', 'B39'), 'Superficies de trabajo: limpiar y luego sanitizar con ' + _TIRA),
    (('01', 'Apertura Sala', 'B14'), _APPS),
    (('01', 'Cierre Cocina', 'B6'), _CARNE_GUARDAR),
    (('01', 'Cierre Cocina', 'B7'), 'Los toppings cortados (tomate, lechuga, cebolla) son TCS: tapados, a 41 °F o menos '
     'y con date marking (7 días como máximo, FDA Food Code 3-501.17)'),
    (('01', 'Cierre Cocina', 'B8'), 'Salsas caseras: tapadas, a 41 °F o menos y con fecha; 5 días como máximo (criterio '
     'del kit, dentro de los 7 del date marking de la FDA, 3-501.17)'),
    (('01', 'Cierre Cocina', 'B10'), _DATE),
    (('01', 'Cierre Cocina', 'B14'), _ACEITE),
    (('01', 'Cierre Cocina', 'B15'), 'Apagar la plancha y el horno; la campana, la última, cuando la freidora y la '
     'plancha ya se hayan enfriado'),
    (('01', 'Cierre Cocina', 'B16'), _TEMP_FRIO),
    (('01', 'Cierre Cocina', 'B23'), _PATTIES),
    (('01', 'Cierre Cocina', 'B26'), 'Descongelar en la cámara a 41 °F o menos (FDA Food Code 3-501.13), nunca a '
     'temperatura ambiente'),
    (('01', 'Cierre Sala', 'B6'), 'Limpiar las mesas y luego sanitizarlas con ' + _TIRA + '; paños en su cubo de '
     'sanitizante'),
    # 02 · estaciones
    (('02', 'Plancha Grill', 'B6'), '°F: 200-230 °C ≈ 400–450 °F (plancha = flat-top griddle); el °C, solo entre '
     'paréntesis tras el °F'),
    (('02', 'Plancha Grill', 'B9'), _BACON),
    (('02', 'Plancha Grill', 'B11'), 'Utensilios de crudo (tabla, pinzas, espátula) marcados y separados de los del pan '
     'y los toppings (FDA Food Code 3-302.11)'),
    (('02', 'Plancha Grill', 'B13'), 'Bola de 80-100 g = 3–3.5 oz'),
    (('02', 'Plancha Grill', 'B14'), _PICADA),
    (('02', 'Plancha Grill', 'B15'), 'Campana para fundir = melting dome (basting cover)'),
    (('02', 'Plancha Grill', 'B21'), 'Prensa y espátulas: lavar, aclarar y sanitizar con ' + _TIRA),
    (('02', 'Línea Montaje', 'B6'), _LAVADO + '; los inserts, en la mesa refrigerada de la make line a 41 °F o menos '
     '(FDA Food Code 3-501.16)'),
    (('02', 'Línea Montaje', 'B10'), 'Huevo frito con la yema líquida = poco hecho: aviso al consumidor en la carta (FDA '
     'Food Code 3-603.11), o bien hecho'),
    (('02', 'Línea Montaje', 'B18'), 'Limpiar la make line completa y sanitizarla con ' + _TIRA),
    (('02', 'Freidora', 'B6'), _TPM),
    (('02', 'Freidora', 'B7'), '°F: 175-180 °C ≈ 350–355 °F; el °C, solo entre paréntesis tras el °F'),
    (('02', 'Freidora', 'B10'), _POLLO),
    (('02', 'Freidora', 'B19'), _ACEITE),
    # 03
    (('03', 'Diario Manager', 'B11'), 'Tiempos = ticket times: menos de 12 min por burger'),
    (('03', 'Diario Manager', 'B12'), _PUNTO),
    (('03', 'Diario Manager', 'B21'), 'Orden lógico del cierre: primero el gas, luego las luces y, al final, la '
     'alarma'),
    (('03', 'Semanal Manager', 'B8'), _A[('03', 'Diario Manager', 'B29')] + ', más las apps de delivery'),
    (('03', 'Semanal Manager', 'B19'), _TPM),
    (('03', 'Mensual Manager', 'B17'), _A[('03', 'Mensual Manager', 'B23')] + '; botiquín (first aid kit) completo'),
    # 04 · perfiles
    (('04', 'Parrillero', 'B7'), _TCS_CRUDO),
    (('04', 'Parrillero', 'B9'), _BACON),
    (('04', 'Parrillero', 'B11'), _PUNTO),
    (('04', 'Parrillero', 'B18'), _CARNE_GUARDAR),
    (('04', 'Parrillero', 'B19'), _PATTIES),
    (('04', 'Cocinero Línea', 'B15'), 'Inserts tapados y a 41 °F o menos (FDA Food Code 3-501.16)'),
    (('04', 'Cocinero Línea', 'B16'), 'Limpiar la make line y sanitizarla con ' + _TIRA),
    (('04', 'Freidurista', 'B10'), _POLLO),
    (('04', 'Freidurista', 'B15'), _ACEITE),
    (('04', 'Encargado', 'B9'), _APPS),
    (('04', 'Camarero', 'B11'), _ALERGENOS + '; y el punto de la carne → doneness: poco hecha solo con el aviso al '
     'consumidor en la carta, nunca la del menú infantil'),
    # 05
    (('05', 'Instrucciones', 'B6'), 'Describe la lista US de «Quarterly & Annual»: control de plagas, campana y '
     'conductos (NFPA 96), extintores y su prueba hidrostática, extinción de la campana, gas, frío, aceite usado, '
     'residuos y envases, legionela, agua, seguros, POS / sales tax y calibración de termómetros. Sin DDD, BIE, '
     'Verifactu ni facturación española'),
    (('05', 'Inventario Diario', 'A6'), 'Patties de 150 g = 1/3 lb («1/3 lb patties»)'),
    (('05', 'Inventario Diario', 'A7'), 'Bolas de 80 g = 3 oz'),
    (('05', 'Limpieza Semanal', 'B9'), 'El equipo limpia los filtros de la campana; el conducto lo limpia el '
     'contratista (hoja «Quarterly & Annual», NFPA 96)'),
    (('05', 'FIFO Semanal', 'B6'), 'Carne picada fresca: 3 días como máximo (criterio del kit) y nunca más allá de la '
     'fecha del proveedor'),
    (('05', 'FIFO Semanal', 'B7'), 'Quesos abiertos: tapados, con la fecha de apertura y sin pasar la del fabricante'),
    (('05', 'FIFO Semanal', 'B8'), 'Salsas caseras: 5 días como máximo (criterio del kit; el date marking de la FDA '
     'permite 7 contando el de preparación, 3-501.17)'),
    (('05', 'FIFO Semanal', 'B15'), _TPM),
    (('05', 'FIFO Semanal', 'D30'), 'Del congelador a la freidora, como diga el fabricante; el pollo, hasta 165 °F en el '
     'centro (FDA Food Code 3-401.11(A)(3))'),
    (('05', 'Mantenimiento Mensual', 'B14'), 'Salidas de emergencia despejadas; añade: señales de salida (exit signs) '
     'iluminadas'),
    (('05', 'Trimestral y Anual', 'B20'), _A[('05', 'Trimestral y Anual', 'B23')] + '; la sonda de la plancha, según su '
     'fabricante'),
    # 06
    (('06', 'Noche Fútbol', 'A1'), 'Fútbol → fútbol americano (NFL): «Game Night / Super Bowl — Peak Sales»'),
    (('06', 'Noche Fútbol', 'B10'), 'Combo para el partido (game-day combo) en redes sociales'),
    (('06', 'Burger Week', 'A1'), '«Burger Week» se dice igual en EE. UU. (muchas ciudades tienen la suya): «Burger '
     'Week / Limited-Edition Burgers»'),
    (('06', 'Burger Week', 'B7'), 'Wagyu, trufa y foie gras, este solo donde sea legal venderlo (en California está '
     'prohibido)'),
    (('06', 'Navidad', 'B6'), _ALERGENOS + '; por escrito'),
    (('06', 'Navidad', 'B7'), 'Cruce = cross-contact (alérgenos): plancha, espátulas, línea y el aceite compartido de la '
     'freidora (rebozados)'),
    (('06', 'Temporada Terraza', 'B10'), _A[('06', 'Temporada Terraza', 'B6')] + ': comprobar que está vigente y '
     'renovarlo si caduca esta temporada'),
    # 08
    (('08', 'Apertura del Negocio', 'B20'), 'Con la campana ya encendida (hoja «Kitchen Opening»): encender planchas y '
     'freidoras y precalentarlas el tiempo que diga su fabricante (20 min como referencia del kit)'),
])
# 08 B8 (ronda 1 m15 del bar, NO_HEREDAR): la apertura de puertas suma las salidas de emergencia
ADAPTAR[('08', 'Apertura del Negocio', 'B8')] = (_A[('08', 'Apertura del Negocio', 'B8')] + '; añade: salidas de '
                                                 'emergencia despejadas y señales de salida (exit signs) iluminadas')
for _fila, (_mes, _evento, _antel, _dir) in CALENDARIO.items():
    if _dir:
        ADAPTAR[(HOJA_CAL[0], HOJA_CAL[1], 'C%d' % _fila)] = 'Evento EN: «%s». %s' % (_evento, _dir)
# aplicar_en.objetivo_ajuste / G3 (errata ES, como la pizzería): las tareas largas del ES no llevan ajuste de texto y
# salen cortadas por la celda vecina; la EN activa el ajuste también donde el ES tampoco cabía
AJUSTE_MAQUETA_ES = True
# aplicar_en.capa_ajuste (errata ES): 05 «Instrucciones» B2, el título, ya va cortado en el ES (2 líneas en 26 pt de
# alto); la EN sube la fila a 50.5, el alto de los títulos de dos líneas de los demás libros
ALTOS_FILA = {('05', 'Instrucciones', 2): 50.5}
# Celdas ES con °C cuya EN NO lleva cifra en °F: el filtrado del aceite (según el fabricante) y las dos filas de la
# apertura de cocina cuyo °C se mueve con su tarea (B14 → B15, B16 → B18; lo comprueba el autotest)
CELSIUS_SIN_F = frozenset({('01', 'Cierre Cocina', 'B14'), ('02', 'Freidora', 'B19'),
                           ('01', 'Apertura Cocina', 'B14'), ('01', 'Apertura Cocina', 'B16')})

# ==========================================================================
# REGLAS_US: las del base + las de la hamburguesería (fuente única de las cifras y normas que el kit puede afirmar)
# ==========================================================================
REGLAS_US = OrderedDict(_base.REGLAS_US)
REGLAS_US.update([
    ('picada', ('carne picada: 155 °F durante 17 s; equivalentes 145 °F 3 min · 150 °F 1 min · 158 °F al instante',
                'FDA Food Code 2022 §3-401.11(A)(2)')),
    ('poco_hecha', ('poco hecha solo a petición del cliente y con aviso al consumidor; nunca la picada del menú '
                    'infantil', 'FDA Food Code 2022 §3-401.11(D) y §3-603.11')),
    ('pollo', ('aves: 165 °F al instante', 'FDA Food Code 2022 §3-401.11(A)(3)')),
    ('tcs_crudo', ('carne picada cruda a 41 °F o menos hasta la plancha', 'FDA Food Code 2022 §3-501.16(A)(2)')),
    ('tphc', ('time as a public health control: procedimiento escrito; hora marcada; servir o descartar DENTRO de las 4 h',
              'FDA Food Code 2022 §3-501.19(B)')),
    ('descongelar', ('descongelar en refrigeración a 41 °F o menos', 'FDA Food Code 2022 §3-501.13')),
    ('crudo_separado', ('carne cruda separada de lo listo para consumir', 'FDA Food Code 2022 §3-302.11')),
    ('manos_guantes', ('manos lavadas y guantes nuevos al pasar de crudo a listo para consumir',
                       'FDA Food Code 2022 §2-301.14 y §3-304.15')),
    ('make_line', ('make line: inserts de toppings cortados y salsas a 41 °F o menos; coleslaw y toppings con date '
                   'marking', 'FDA Food Code 2022 §3-501.16(A)(2) y §3-501.17')),
    ('temperaturas', ('plancha 200-230 °C ≈ 400–450 °F · aceite 175-180 °C ≈ 350–355 °F',
                      '[criterio del kit] cifras del ES convertidas')),
    ('aceite', ('filtrado y cambio del aceite según el fabricante de la freidora; TPM sin límite federal',
                '[fabricante] manual de la freidora y del medidor')),
    ('plazos_kit', ('carne picada fresca 3 días; salsas caseras 5 días; 12 min por burger', '[criterio del kit]')),
    ('agua', ('red: Consumer Confidence Report anual de la compañía; pozo propio: análisis según el departamento de salud',
              '40 CFR Part 141, Subpart O; [local] departamento de salud')),
    ('alergenos_pan', ('el trigo está entre los 9; el gluten en sí no, ni la mostaza (en UK sí); la lactosa es una '
                       'intolerancia', 'FALCPA 2004 + FASTER Act 2021; Food Information Regulations 2014 (UK)')),
    ('edad_alcohol', ('21 años para comprar o consumir alcohol, en todos los estados',
                      'National Minimum Drinking Age Act of 1984 (23 U.S.C. 158)')),
    ('alcohol_licencia', ('alcohol solo con licencia; promociones y regalos, según el estado',
                          '[estatal] ABC / liquor authority')),
    ('foie', ('foie gras: venta prohibida en California', 'California Health and Safety Code §25982')),
    ('dias_fuertes', ('Super Bowl, March Madness, National Burger Month (28 de mayo: National Hamburger Day), 4 de '
                      'julio, temporada de fútbol americano, 18 de septiembre: National Cheeseburger Day, Halloween y '
                      'Nochevieja', '[criterio del kit] calendario comercial US')),
    ('inventario', ('mínimos de kg → lb (×2,2) y de g → oz (÷28,35); L → qt (1 qt ≈ 0,95 L); 150 g ≈ 1/3 lb',
                    '[criterio del kit] conversión')),
])
# °F que el kit puede afirmar (G7): las del base + 32 (calibración) + carne picada, plancha y aceite
GRADOS_F_SPEC = {-31, -4, 0, 32, 41, 70, 100, 135, 145, 150, 155, 158, 165, 350, 355, 400, 450}

# ==========================================================================
# Pistas y dependencias de la hamburguesería (extraer_textos.py)
# ==========================================================================
PISTAS_CAMBIO = {r'Kit de Tareas': 'D2: «Burger Joint Checklists Kit Pro»'}
PISTAS_FUERA = (r'Restaurante Casual',)
PISTAS_EXTRA = [
    (r'Hamburgueser[ií]a', 'D2: la EN no lleva el sufijo de variante: quita «— Hamburguesería»; hamburguesería → '
                           'burger joint / burger shop / burger restaurant'),
    (r'[Pp]lancha|[Gg]rill\b|[Pp]rensa|[Rr]asqueta|[Ee]spátula', 'plancha → flat-top griddle (the grill); prensa smash '
                                                                  '→ smash press (burger press); rasqueta → griddle '
                                                                  'scraper; espátula → spatula (turner)'),
    (r'[Ff]reidora|[Cc]esta|[Cc]ucurucho|[Pp]olares', 'freidora → fryer (fry station); cesta → fry basket; cucurucho → '
                                                      'paper cone; test polares → TPM oil test'),
    (r'[Pp]atatas|[Aa]ros|[Rr]ebozad|[Nn]uggets|[Cc]oleslaw', 'patatas → fries; aros de cebolla → onion rings; rebozar '
                                                               '→ batter / bread; sides → sides'),
    (r'[Pp]an de burger|[Pp]anecillos|[Bb]rioche|[Ss][eé]samo', 'pan de burger → buns (brioche, pretzel, sesame seed); '
                                                                'horno para panecillos → bun toaster (or oven)'),
    (r'[Ll][ií]nea de montaje|[Ii]nserts?|[Bb]iber[oó]n|[Pp]alillo', 'línea de montaje → make line; inserts → inserts; '
                                                                     'biberones → squeeze bottles; palillo / flag → '
                                                                     'frill pick (burger flag)'),
    (r'[Cc]arne picada|[Pp]atties|[Bb]lend|[Pp]unto', 'carne picada → ground beef; patties → patties; blend → custom '
                                                      'blend; punto de la carne → doneness'),
    (r'[Cc]omanda|[Tt]iempos|\bpase\b', 'comanda → ticket; tiempos → ticket times; pase → the pass / expo'),
    (r'[Tt]ake-away|[Pp]ara llevar|[Dd]elivery|[Aa]pps|[Pp]ackaging|[Cc]ajas', 'take-away → takeout / carryout; apps → '
                                                                               'third-party delivery apps (DoorDash, '
                                                                               'Uber Eats, Grubhub); cajas burger → '
                                                                               'burger boxes (clamshells)'),
    (r'Glovo|Just Eat', 'Glovo / Just Eat → DoorDash / Grubhub (Uber Eats se queda)'),
    (r'[Pp]arrillero|[Ff]reidurista|[Cc]ocinero', 'parrillero / cocinero plancha → grill cook; freidurista / cocinero '
                                                  'freidora → fry cook; cocinero de línea → line cook'),
    (r'[Ee]ncargad', 'encargado/a → shift manager (NUNCA «shift lead»)'),
    (r'TPV|[Dd]atáfono', 'TPV / datáfono → POS / card terminal'),
    (r'[Cc]uadrar caja', 'cuadrar caja → cash up / balance the drawer'),
    (r'[Mm]ermas?', 'mermas → waste (waste log)'),
    (r'[Ff]útbol', 'fútbol → (American) football: NFL Sundays, Monday Night Football, Super Bowl; noche de partido → '
                   'game night'),
    (r'RRSS|redes', 'RRSS → social media'),
    (r'[Pp]izarra', 'pizarra → menu board / chalkboard'),
    (r'[Ll]ocal\b', 'el local → the restaurant / the burger joint (nunca «venue»)'),
    (r'[Cc]ruce', 'cruce de alérgenos → cross-contact'),
]
DEPENDENCIAS_EXTRA = OrderedDict([
    ('variante', ('Sufijo de variante «Hamburguesería»', r'— Hamburguesería|· Hamburguesería',
                  'D2: la EN no lleva sufijo')),
    ('picada', ('Carne picada: punto, temperatura y crudo', r'[Cc]arne picada|[Pp]atties|[Pp]unto|[Tt]emperar',
                'D-BUR: 155 °F / 17 s o aviso al consumidor; TCS a 41 °F; crudo separado')),
    ('freidora', ('Freidora y aceite', r'[Ff]reidora|[Aa]ceite|[Pp]olares', 'D-BUR: filtrado y cambio según el '
                  'fabricante; TPM sin cifra; 350–355 °F')),
    ('delivery', ('Delivery por apps', r'[Tt]ablets?|Glovo|Just Eat|[Aa]pps', 'D-BUR: DoorDash, Uber Eats, Grubhub')),
    ('alcohol', ('Alcohol en el calendario', r'[Cc]ava\b|[Cc]ocktails|[Cc]erveza', 'D-BUR: solo con licencia, 21+ con '
                 'ID; sin cócteles')),
])


def _rebind(f):
    return types.FunctionType(f.__code__, globals(), f.__name__, f.__defaults__, f.__closure__)


titulo_interior = _rebind(_base.titulo_interior)
_autotest_base = _rebind(_base.autotest)
_cruzar_censo_base = _rebind(_base.cruzar_censo)


def autotest():
    import re
    err = _autotest_base()
    for k, (es, en) in VALORES_EN.items():
        if not isinstance(en, (int, float)) or isinstance(en, bool) or en <= 0:
            err.append('VALORES_EN: el EN de %r debe ser un número > 0: %r' % (k, en))
        if k in POR_CELDA or k in ADAPTAR:
            err.append('VALORES_EN y POR_CELDA/ADAPTAR sobre la misma celda: %r' % (k,))
    rx = re.compile(TERMINOS_PROHIBIDOS)
    if not rx.search(TERMINO_PROHIBIDO_EJEMPLO):
        err.append('TERMINO_PROHIBIDO_EJEMPLO no lo caza TERMINOS_PROHIBIDOS')
    for ok in ('sidewalk cafe permit', 'restaurant consultant', 'burger restaurant', 'the restaurant'):
        if rx.search(ok):
            err.append('TERMINOS_PROHIBIDOS caza lo permitido (%r)' % ok)
    for k, v in list(GLOSARIO.items()) + list(POR_CELDA.items()) + list(CLAVES.items()):
        if k not in _base.GLOSARIO or k in _GLOSARIO_BURGER:
            if isinstance(v, str) and rx.search(v):
                err.append('texto EN fijado con un término prohibido: %r → %r' % (k, v))
    if CITA_AUTOTEST.strip('()').split()[-1] in ' '.join(f for _v, f in REGLAS_US.values()):
        err.append('CITA_AUTOTEST está en REGLAS_US: G7 no la cazaría')
    for k, v in POR_CELDA.items():
        if k[:2] in (_AC,) and k[2].startswith('E') and not re.match(r'^\d{1,2}:\d{2} (AM|PM)$', v):
            err.append('POR_CELDA: hora fijada %r sin formato US: %r' % (k, v))
    # el °C del ES de B14 y B16 viaja con su tarea a B15 y B18: esas llevan °F y las declaradas, ninguna temperatura
    for c in ('B15', 'B18'):
        if '°F' not in POR_CELDA[_AC + (c,)]:
            err.append('01 Apertura Cocina %s: la tarea movida debe llevar su °F' % c)
    for k in CELSIUS_SIN_F:
        if k in POR_CELDA and ('°' in POR_CELDA[k]):
            err.append('CELSIUS_SIN_F %r con temperatura en el EN fijado' % (k,))
    return err


def cruzar_censo(p):
    import json
    err = _cruzar_censo_base(p)
    censo = json.load(open(p, encoding='utf-8'))
    tx = {}
    for info in censo['libros'].values():
        for h, hd in info['hojas_detalle'].items():
            for coord, t in hd.get('textos', {}).items():
                tx[(info['corto'], h, coord)] = t
    for k, (es, en) in VALORES_EN.items():
        if tx.get(k) != es:
            err.append('VALORES_EN: %r no trae en el ES %r (trae %r)' % (k, es, tx.get(k)))
    factor = {('kg', 'lb'): 2.2046, ('g', 'oz'): 1 / 28.35, ('L', 'qt'): 1, ('uds', 'ea'): 1}
    for f, es, en in _MINIMOS:
        c = ('05', 'Inventario Diario', 'C%d' % f)
        u_es = tx.get(c)
        u_en = POR_CELDA.get(c) or GLOSARIO.get(u_es)
        x = factor.get((u_es, u_en))
        if x is None:
            err.append('VALORES_EN: unidad %s → %s sin factor en la fila %d' % (u_es, u_en, f))
        elif x == 1 and float(es) != en:
            err.append('VALORES_EN: fila %d en %s no cambia de cifra (%s → %s)' % (f, u_es, es, en))
        elif x != 1 and not (0.5 <= en / (float(es) * x) <= 1.5):
            err.append('VALORES_EN: fila %d, %s %s → %s %s fuera de la conversión' % (f, es, u_es, en, u_en))
    # las filas reordenadas del 08 y de la apertura de cocina del 01: el ES tiene tarea en todas, misma zona y
    # responsable en las del 01, y el °C del ES está donde dice CELSIUS_SIN_F
    for fila in range(5, 5 + len(_CIERRE)):
        if (_CN[0], _CN[1], 'B%d' % fila) not in tx:
            err.append('08 cierre: B%d sin tarea en el ES' % fila)
    filas = range(12, 12 + len(_APERTURA))
    for fila in filas:
        if (_AC[0], _AC[1], 'B%d' % fila) not in tx:
            err.append('01 apertura de cocina: B%d sin tarea en el ES' % fila)
    for col in ('C', 'D'):
        if len({tx.get((_AC[0], _AC[1], '%s%d' % (col, f))) for f in filas}) != 1:
            err.append('01 apertura de cocina: la columna %s cambia entre las filas reordenadas' % col)
    for _f in range(20, 25):
        if tx.get(('07', 'Por Área', 'C%d' % _f)) != 'Barra':
            err.append('07 Por Área C%d: el ES no dice «Barra»' % _f)
    for k in (('01', 'Apertura Cocina', 'D10'), ('B01', 'Briefing', 'B6'), ('B01', 'Briefing', 'B26'),
              ('07', 'Por Área', 'A19')) + tuple((HOJA_CAL[0], HOJA_CAL[1], 'C%d' % f) for f in _CAL_C):
        if k not in tx:
            err.append('POR_CELDA %r sin texto en el ES' % (k,))
    for f in filas:
        con_c = '°C' in tx.get((_AC[0], _AC[1], 'B%d' % f), '')
        if con_c != ((_AC[0], _AC[1], 'B%d' % f) in CELSIUS_SIN_F):
            err.append('01 apertura de cocina: B%d °C en el ES ≠ CELSIUS_SIN_F' % f)
    return err


def cruzar_base(p_burger, p_base):
    """Lo heredado POR CELDA del base (POR_CELDA y ADAPTAR) tiene en la hamburguesería el mismo texto ES que en el base;
    las filas equivalentes (otra celda, mismo contenido) se comparan por su texto."""
    import json
    err = []

    def textos(p):
        d = {}
        for info in json.load(open(p, encoding='utf-8'))['libros'].values():
            for h, hd in info['hojas_detalle'].items():
                for coord, t in hd.get('textos', {}).items():
                    d[(info['corto'], h, coord)] = t
        return d
    tb, tr = textos(p_base), textos(p_burger)
    for nombre, claves in (('POR_CELDA', _HEREDA_POR_CELDA), ('ADAPTAR', _HEREDA_ADAPTAR)):
        for k in claves:
            if tr.get(k) != tb.get(k):
                err.append('%s heredado %r: el texto ES de la hamburguesería %r ≠ base %r' % (nombre, k, tr.get(k),
                                                                                             tb.get(k)))
    equivalentes = [(('03', 'Mensual Manager', 'B9'), ('03', 'Mensual Manager', 'B16'))]
    for kc, kb in equivalentes:
        if tr.get(kc, '').split(' (')[0] != tb.get(kb, '').split(' (')[0]:
            err.append('%r de la hamburguesería no es la fila del base %r: %r ≠ %r' % (kc, kb, tr.get(kc), tb.get(kb)))
    return err


CITA_AUTOTEST = '(FDA Food Code 3-501.18)'                     # autotest G7: una cita que NO está en REGLAS_US


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
        e += cruzar_base(pc, os.path.join(os.path.dirname(AQUI), 'censo_es.json'))
    for x in e:
        print('ERROR', x)
    print('mapas_burger.py: {} ficheros · {} pestañas · {} glosario · {} por celda · {} valores · {} adaptar · '
          '{} reglas · {} errores'.format(len(FICHEROS), len(HOJAS), len(GLOSARIO), len(POR_CELDA), len(VALORES_EN),
                                          len(ADAPTAR), len(REGLAS_US), len(e)))
    raise SystemExit(1 if e else 0)
