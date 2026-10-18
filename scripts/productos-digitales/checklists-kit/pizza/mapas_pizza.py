#!/usr/bin/env python3
"""
mapas_pizza.py — Pizza Shop Checklists Kit Pro (EN) · DELTA del Kit de Tareas para Pizzería (`kit-tareas-pizzeria`,
11 xlsx v2.0) sobre `mapas.py` (Restaurant Checklists Kit Pro). SPEC: `pizza/SPEC.md` (solo el delta). Cuarto hermano
vertical, hecho como el bar, la cafetería y el catering. Sesión Claude Code, 18-oct-2026.

Se usa con `--kit pizza` (kit.py). Importa `mapas.py` y SOLO añade o sobrescribe: producto, ficheros, títulos,
pestañas (la pizzería tiene la estructura del base, sin barra y con estación de horno, make line, repartidor e
inventario diario), glosario de pizzería (puestos, unidades del inventario), calendario (misma estructura que el base:
filas 5-26; cambian los días fuertes de una pizza shop US), POR_CELDA (caja 09 heredada TAL CUAL tras comprobar el
texto ES; 05 «Quarterly & Annual» con el horno de leña y NFPA 96; el orden del cierre del 08), VALORES_EN (mínimos
del inventario en lb / oz y como número), ADAPTAR, CLAVES (+ «⚠️ PEDIR») y REGLAS_US (+ masa en frío, make line,
mozzarella TCS, horno de leña, delivery). La hora de 12 h, la caja en dólares y el resto se heredan. Las funciones del
base que leen constantes (titulo_interior, autotest, cruzar_censo) se re-enlazan a ESTE módulo. Ejecutado como script:
autotest + cruce con pizza/censo_es.json + cruce con el base (lo heredado por celda tiene el mismo texto ES).

    python3 pizza/mapas_pizza.py
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
AQUI = os.path.dirname(os.path.abspath(__file__))              # pizza/ (el import * trae el AQUI del base)

ORIGEN_ES = 'kit-tareas-pizzeria'
PRODUCTO = 'Pizza Shop Checklists Kit Pro'
TITULO_SEO = 'Pizza Shop Checklists Kit Pro: Pizzeria Opening & Closing Checklist Templates for Excel'
SLUG = 'pizza-shop-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_PIZZA_SHOP_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
MARCA_ES = '— Kit de Tareas Recurrentes · Pizzería · AI Chef Pro · aichef.pro'
MARCA_EN = '— ' + PRODUCTO + ' · AI Chef Pro · aichef.pro'
VARIANTES_ES = ('Pizzería',)
# heredar.py: memoria con VARIAS fuentes, en orden de preferencia (base, bar, cafetería, catering; gana la primera)
_SUF = lambda v: [(' — Pizzería', ' — ' + v), (' · Pizzería', ' · ' + v)]  # noqa: E731
MEMORIA = [('base', '', _SUF('Restaurante Casual')), ('bar', 'bar', _SUF('Bar / Cocktails')),
           ('cafe', 'cafe', _SUF('Cafetería / Brunch')), ('catering', 'catering', _SUF('Catering / Eventos'))]
# heredar.py: EN heredado que en una pizza shop no vale tal cual → pendientes (motivo «contexto»). «shift lead» y
# «busser» vienen de la cafetería; «sidewalk cafe» (el permiso de terraza) sí vale.
RX_CONTEXTO_PENDIENTE = (r'(?i)\b(?:restaurants?(?! consultant)|host stands?|head chefs?|sous chefs?|MOD|'
                         r'coffee shops?|(?<!sidewalk )cafes?|baristas?|shift leads?|kitchen leads?|bussers?|'
                         r'pastry case|barbacks?|cocktails?|venues?|banquets?|BEOs?|commissary|line-up|brunch)\b')
# heredar.py: cadenas idénticas a una fuente cuyo EN no vale en la pizzería (→ pendientes → G1.json, con base_en)
NO_HEREDAR = {
    'Abrir persianas / puerta principal': 'ronda 1 m15 del bar: + salidas de emergencia despejadas y señales de salida',
}
# gates_en.py G2: términos de otros kits que NINGUNA celda EN de la pizzería puede llevar (la firma de autor,
# «restaurant consultant», queda fuera por el lookahead; «sidewalk cafe permit» por el lookbehind).
# TERMINO_PROHIBIDO_EJEMPLO: lo que inyecta el autotest.
TERMINOS_PROHIBIDOS = (r'(?i:\b(?:restaurants?(?! consultant)|host stands?|head chefs?|sous chefs?|coffee shops?|'
                       r'(?<!sidewalk )cafes?|baristas?|shift leads?|kitchen leads?|bussers?|barbacks?|banquets?|'
                       r'BEOs?|commissary|venues?|line-up)\b)|\bMOD\b')
TERMINO_PROHIBIDO_EJEMPLO = 'Ask the shift lead.'
REFERENCIAS_TRADUCTOR = ['pizza/SPEC.md', 'SPEC.md §0-§3 y §7.2 (brief)', 'textos_en/glosario.json (glosario de la '
                         'prosa del kit base)', 'pizza/textos_en/heredado.json (cómo se dijo ya cada cosa: base, bar, '
                         'cafetería y catering)', 'pizza/mapas_pizza.py: GLOSARIO, HOJAS, FICHEROS, TITULOS, '
                         'POR_CELDA, REGLAS_US', '../GLOSARIO-JERGA-ES-EN.md']
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v2.0'),
    ('keywords', 'pizza shop checklist, pizzeria checklist, pizza shop opening checklist, pizzeria closing checklist, '
                 'pizza kitchen cleaning checklist, pizza oven checklist, AI Chef Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

# ==========================================================================
# Ficheros (D5: sin volumen US medido en «pizza shop / pizzeria checklist»: los dos términos + la intención genérica
# «restaurant opening / closing checklist» en los títulos de la landing, no en los ficheros)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-apertura-cierre.xlsx', '01-pizza-shop-opening-closing-checklists.xlsx'),
    ('02-partidas-cocina.xlsx', '02-pizza-kitchen-station-checklists.xlsx'),
    ('03-tareas-manager.xlsx', '03-pizzeria-manager-checklist.xlsx'),
    ('04-tareas-perfiles.xlsx', '04-pizza-shop-duties-by-role.xlsx'),
    ('05-tareas-semanales-mensuales.xlsx', '05-pizzeria-cleaning-checklist-inventory-maintenance.xlsx'),
    ('06-eventos-festivos.xlsx', '06-pizza-shop-event-checklists.xlsx'),
    ('07-plantilla-personalizable.xlsx', '07-blank-pizza-shop-checklist-template.xlsx'),
    ('08-apertura-cierre-negocio.xlsx', '08-pizzeria-opening-closing-checklist.xlsx'),
    ('09-apertura-cierre-caja.xlsx', '09-cash-drawer-opening-closing.xlsx'),
    ('BONUS-01-briefing-servicio.xlsx', 'BONUS-01-pizza-shop-pre-shift-meeting-template.xlsx'),
    ('BONUS-02-calendario-anual-tareas.xlsx', 'BONUS-02-pizza-shop-holiday-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)
TITULOS = OrderedDict([
    ('01-pizza-shop-opening-closing-checklists.xlsx', 'Pizza Shop Opening & Closing Checklists: Kitchen, FOH & Delivery'),
    ('02-pizza-kitchen-station-checklists.xlsx',
     'Pizza Kitchen Station Checklists: Pizza Oven, Make Line, Apps & Pasta'),
    ('03-pizzeria-manager-checklist.xlsx', 'Pizzeria Manager Checklist: Daily, Weekly, Monthly & Shift Handover'),
    ('04-pizza-shop-duties-by-role.xlsx',
     'Pizza Shop Duties by Role: Pizza Maker, Line Cook, Shift Manager, Server & Driver'),
    ('05-pizzeria-cleaning-checklist-inventory-maintenance.xlsx',
     'Pizzeria Cleaning Checklist, Inventory & Maintenance Schedule'),
    ('06-pizza-shop-event-checklists.xlsx',
     "Pizza Shop Event Checklists: Game Night, Valentine's Day, Holidays & Patio"),
    ('07-blank-pizza-shop-checklist-template.xlsx', 'Blank Pizza Shop Checklist Template (Editable)'),
    ('08-pizzeria-opening-closing-checklist.xlsx', 'Pizzeria Opening & Closing Checklist (Whole Shop)'),
    ('09-cash-drawer-opening-closing.xlsx', 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log'),
    ('BONUS-01-pizza-shop-pre-shift-meeting-template.xlsx', 'BONUS: Pizza Shop Pre-Shift Meeting Template (Huddle Notes)'),
    ('BONUS-02-pizza-shop-holiday-calendar.xlsx', 'BONUS: Pizza Shop Holiday & Busy Days Calendar (US)'),
])
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

HOJAS = OrderedDict(_base.HOJAS)
HOJAS.update([
    ('Pizzero Horno', 'Pizza Oven Station'), ('Línea Montaje', 'Make Line'), ('Complementaria', 'Apps & Pasta'),
    ('Pizzero', 'Pizza Maker'), ('Cocinero Línea', 'Line Cook'), ('Encargado', 'Shift Manager'),
    ('Repartidor', 'Delivery Driver'), ('Inventario Diario', 'Daily Inventory'),
    ('Noche Fútbol', 'Game Night'), ('Navidad', 'Holiday Season'),
    ('Apertura del Negocio', 'Pizza Shop Opening'), ('Cierre del Negocio', 'Pizza Shop Closing'),
])
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Apertura Cocina', 'Apertura Sala', 'Cierre Cocina', 'Cierre Sala']),
    ('02', ['Instrucciones', 'Pizzero Horno', 'Línea Montaje', 'Complementaria']),
    ('03', ['Instrucciones', 'Diario Manager', 'Semanal Manager', 'Mensual Manager', 'Handover Turno']),
    ('04', ['Instrucciones', 'Pizzero', 'Cocinero Línea', 'Encargado', 'Camarero', 'Repartidor']),
    ('05', ['Instrucciones', 'Inventario Diario', 'Limpieza Semanal', 'FIFO Semanal', 'Mantenimiento Mensual',
            'Trimestral y Anual']),
    ('06', ['Instrucciones', 'Noche Fútbol', 'San Valentín', 'Navidad', 'Temporada Terraza']),
    ('07', ['Instrucciones', 'Por Franja Horaria', 'Por Área', 'Por Perfil']),
    ('08', ['Instrucciones', 'Apertura del Negocio', 'Cierre del Negocio']),
    ('09', ['Instrucciones', 'Apertura de Caja', 'Cierre de Caja', 'Registro Mensual']),
    ('B01', ['Instrucciones', 'Briefing']),
    ('B02', ['Instrucciones', 'Calendario Anual']),
])

# ==========================================================================
# GLOSARIO: el base entero (opcional en la pizzería) + celdas cortas de la pizzería. Jerga de pizza shop US: pizza
# maker, line cook, shift manager, delivery driver; unidades del inventario en lb / oz / qt (VALORES_EN).
# ==========================================================================
GLOSARIO = OrderedDict(_base.GLOSARIO)
_GLOSARIO_PIZZA = OrderedDict([
    ('Pizzero', 'Pizza maker'), ('Cocinero línea', 'Line cook'), ('Repartidor', 'Delivery driver'),
    ('Encargado/a', 'Shift manager'), ('Camarero/a', 'Server'), ('Turno saliente', 'Outgoing shift'),
    ('Responsable de caja', 'Cashier / shift manager'), ('Jefe de Cocina', 'Kitchen manager'),
    ('Jefe de Sala', 'FOH manager'), ('Recepción', 'Front counter'), ('Todos', 'All staff'),
    ('Auxiliar', 'Dishwasher / prep'),
    ('Horno', 'Oven'), ('Office', 'Office'), ('Almacén', 'Storage'), ('Cámara', 'Walk-in'),
    ('Primavera', 'Spring'), ('Otoño', 'Fall'), ('Dic 1', 'Dec 1'), ('23 Dic', 'Dec 23'),
    ('Día antes', 'Day before'), ('3 días antes', '3 days out'),
    # inventario (05): unidades US; los mínimos de kg y g cambian de cifra (VALORES_EN), los de L, ml y uds no
    ('kg', 'lb'), ('g', 'oz'), ('L', 'qt'), ('ml', 'fl oz'), ('uds', 'ea'), ('manojos', 'bunches'), ('Unidad', 'Unit'),
])
GLOSARIO.update(_GLOSARIO_PIZZA)
GLOSARIO_OPCIONAL = frozenset(_base.GLOSARIO)
PUESTOS_ES = frozenset(_base.PUESTOS_ES | {'Pizzero', 'Cocinero línea', 'Repartidor', 'Encargado/a', 'Camarero/a',
                                           'Turno saliente', 'Todos', 'Horno', 'Office', 'Almacén', 'Cámara'})

# ==========================================================================
# CLAVES: el inventario diario avisa con «⚠️ PEDIR» / «OK» (literales de fórmula)
# ==========================================================================
CLAVES = OrderedDict(_base.CLAVES)
CLAVES.update([('⚠️ PEDIR', '⚠️ REORDER'), ('OK', 'OK')])

# ==========================================================================
# BONUS-02 «Holiday Calendar»: misma estructura que el base (filas 5-26: A mes · B fecha/evento · C tareas ·
# D antelación). A, B y D fijados; C = traductor, con ADAPTAR donde la tarea de pizzería cambia. Los días fuertes de
# una pizza shop US (Super Bowl, viernes de Cuaresma, playoffs, Halloween, víspera de Thanksgiving, Nochevieja).
# fila → (mes, evento, antelación, ADAPTAR de C o None). Lo que no cambia, del base.
# ==========================================================================
CALENDARIO = OrderedDict(_base.CALENDARIO)
CALENDARIO.update([
    (5, ('January', "Jan 1 — New Year's Day", '1 week', None)),
    (6, ('February', 'Super Bowl Sunday (2nd Sunday in Feb)', '2 weeks',
         'Sustituye a Reyes. Uno de los días de más pizza a domicilio del año en EE. UU.: pedidos anticipados y '
         'grandes (party orders), más bolas de masa fermentando con antelación, repartidores y cajas extra, menú corto '
         'para sacar más pedidos por hora')),
    (9, ('March', "Mar 17 — St. Patrick's Day + March Madness", '2 weeks',
         'Sustituye al Día del Padre (en EE. UU. va en junio, fila 16). Tareas: especiales temáticos; los partidos del '
         'torneo universitario (March Madness, de mediados de marzo a principios de abril) suben el delivery: '
         'repartidores extra; cerveza solo con licencia y 21+ con ID')),
    (10, ('March–April', 'Lent Fridays + Easter Sunday (varies)', '2 weeks',
          'Sustituye a Semana Santa: el «menú de vigilia» son los viernes de Cuaresma sin carne (meatless Fridays): '
          'especiales de queso, verduras o marinara; Pascua: decidir el horario, pedidos familiares')),
    (12, ('May–June', 'Graduation season', '1 month',
          'Mismas tareas del ES (menú de grupo cerrado, depósito y precio por persona, zona privada); en EE. UU. son '
          'graduaciones y fiestas de fin de curso: pedidos grandes para llevar (party orders)')),
    (13, ('May', 'NBA & NHL playoffs (game nights)', '1 week',
          'Sustituye al 1 de mayo. Tareas: noches de partido = pico de delivery: repartidores y masa extra, ofertas '
          'para ver el partido (game-night deals), pantallas si tienes sala')),
    (14, ('May', "2nd Sunday — Mother's Day", '2 weeks', None)),
    (16, ('June', "3rd Sunday — Father's Day", '2 weeks',
          'Sustituye a San Juan. Tareas = las del Día del Padre del ES (fila 9): menú familiar, reservas ampliadas y '
          'pizza XL para compartir')),
    (17, ('July', 'Jul 4 — Independence Day', '1 week',
          'Sustituye a la fila de temporada alta (sus tareas pasan a la fila 18). Tareas: decidir el horario, patio a '
          'pleno rendimiento, pedidos grandes para las fiestas (party orders) y refuerzo de repartidores')),
    (18, ('July–August', 'Summer peak season', 'Ongoing',
          'Tareas = las de «Temporada alta» de la fila 17 del ES: personal extra, horario ampliado, carta de verano; '
          'más refuerzo de repartidores y patio a pleno rendimiento')),
    (19, ('September', 'Labor Day (1st Monday) + football season kickoff', '2 weeks',
          'Fin del verano. Tareas: carta de otoño, especiales de almuerzo (lunch specials) para la vuelta a la rutina y '
          'ofertas para los partidos de fútbol americano (game-day deals): domingos y lunes por la noche, pico de '
          'delivery')),
    (20, ('October', 'Oct 31 — Halloween', '1 week',
          'Noche fuerte de delivery: masa, cajas y repartidores extra; decoración temática y pizzas especiales (sin '
          'cócteles)')),
    (21, ('November', 'Thanksgiving Eve + Thanksgiving (4th Thursday)', '1 month',
          'Sustituye a Todos los Santos. La noche del miércoles anterior es de las de más delivery del año: masa, '
          'repartidores y turnos extra; decidir si se abre el jueves (muchos cierran)')),
    (23, ('Nov–Dec', 'Holiday gift card season', '2 weeks',
          'Sustituye al puente de la Constitución. Del Black Friday a Nochebuena. Tareas: promoción de tarjetas '
          'regalo, expositor junto a la caja (register), venta online y en la app de pedidos')),
    (24, ('December', 'Holiday parties (office orders)', '1 month',
          'Sustituye a las cenas de empresa. Tareas: pedidos de empresa para las fiestas de oficina (party trays y '
          'pizzas grandes con hora de entrega), reservas de grupo, turnos extra')),
    (26, ('December', "Dec 31 — New Year's Eve", '2 weeks',
          'Sin uvas, cava ni cotillón español. Una de las noches fuertes de delivery: masa y repartidores extra, '
          'horario de cierre; si abres la sala, party favors y brindis a medianoche (con alcohol solo si tu licencia '
          'lo permite; 21+ con ID), turnos de noche')),
])

# ==========================================================================
# POR_CELDA: lo heredado del base (mismo texto ES en la misma celda o en la fila equivalente; lo comprueba
# cruzar_base) + lo de la pizzería
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
    (('05', 'Inventario Diario', 'A46'), MARCA_EN + ' —'),
    # 05 · Instrucciones (errata ES, como en la cafetería): el inventario no está protegido y el ES lo promete
    (('05', 'Instrucciones', 'B24'), '▸ Checklist sheets with formulas are protected WITHOUT a password: the input cells '
                                     '(the green ones) are unlocked. The Daily Inventory sheet is left unprotected so '
                                     "you can add products: don't type over the Status column."),
    # 05 · Trimestral y Anual: servicios contratados US de una pizza shop (horno de leña: NFPA 96)
    (_T + ('B7',), 'Hood, duct and chimney cleaning by a certified contractor (NFPA 96): a system serving a wood-fired '
                   'or other solid-fuel oven is inspected monthly (Monthly Maintenance sheet) and cleaned whenever '
                   'buildup is found; gas or electric ovens only: quarterly if high volume, semiannual if moderate'),
    (_T + ('D7',), 'Hood cleaning co.'), (_T + ('E7',), 'Quarterly'),
    (_T + ('B8',), "Wood-fired oven checked by the oven manufacturer's tech or a qualified contractor: dome, floor, "
                   'door, flue and chimney cap'),
    (_T + ('D8',), 'Oven tech'),
    (_T + ('B9',), 'Annual extinguisher maintenance by a licensed fire protection company: new tag and record (OSHA '
                   '1910.157); hood fire suppression inspected every 6 months (NFPA 96)'),
    (_T + ('D9',), 'Fire safety co.'),
    (_T + ('B10',), 'Extinguisher hydrostatic test by the fire protection company: Class K (wet chemical) and CO2 '
                    'units every 5 years, dry chemical as its label says (OSHA 1910.157(f); NFPA 10)'),
    (_T + ('D10',), 'Fire safety co.'),
    (_T + ('B11',), 'Gas lines and appliance connections (gas oven, burners, range) checked by a licensed pro, as '
                    'often as your local code requires'),
    (_T + ('D11',), 'Licensed plumber'), (_T + ('E11',), 'Annual'),
    (_T + ('A12',), '  WATER, WASTE & TESTING'),
    (_T + ('B13',), 'Refrigeration service by an EPA 608-certified tech: walk-in, reach-ins and the make line (pizza '
                    'prep table) — coils, gaskets and refrigerant leak check'),
    (_T + ('D13',), 'Refrigeration tech'),
    (_T + ('B14',), 'Legionella: if you have a cooling tower or at-risk hot water, keep a water management program as '
                    'your local health code requires'),
    (_T + ('D14',), 'Water treatment co.'),
    (_T + ('B15',), "Water quality: on city water, read your utility's annual Consumer Confidence Report; on a private "
                    'well or tank, test it as your health department requires; service any filter or softener per its '
                    'maker (the water goes into every batch of dough)'),
    (_T + ('D15',), 'Water lab'),
    (_T + ('B16',), _base.POR_CELDA[('05', 'Trimestral y Anual', 'B16')]),
    (_T + ('D16',), 'Oil recycler'),
    (_T + ('B19',), "Review insurance (general liability, property, workers' comp; liquor liability if you serve "
                    'alcohol; hired and non-owned auto if drivers deliver in their own cars) and renewal dates'),
    (_T + ('B20',), 'POS check: software updates, sales tax rates and settings, user permissions — plus the online '
                    'ordering and delivery app integrations'),
])
# 01 · Cierre Sala (errata ES): la alarma y las luces iban ANTES que los baños. Mismas filas: los baños suben a la
# sección de delivery y caja y la sección final pasa a ser el cierre (luces, alarma y llave); las horas, con su tarea
_CS = ('01', 'Cierre Sala')
for _celda, _v in (
        ('A13', '  DELIVERY, REGISTER & RESTROOMS'),
        ('B18', 'Final restroom clean'), ('C18', 'Restrooms'), ('D18', 'Dishwasher / prep'), ('E18', '10:45 PM'),
        ('B19', 'Restock soap and paper towels'), ('C19', 'Restrooms'), ('D19', 'Dishwasher / prep'),
        ('E19', '10:45 PM'),
        ('A20', '  LOCK-UP'),
        ('B21', 'Turn off the FOH lights, HVAC and music'), ('C21', 'FOH'), ('D21', 'Shift manager'),
        ('E21', '11:00 PM'),
        ('B22', 'Set the alarm and lock up'), ('C22', 'FOH'), ('D22', 'Shift manager'), ('E22', '11:00 PM')):
    POR_CELDA[_CS + (_celda,)] = _v
# 08 · Cierre (errata ES): el horno de leña se apagaba DESPUÉS de la alarma y la llave. Toda la secuencia, mismas 14
# filas y mismos contadores (E = «Close»): el horno a enfriar al principio, luego el local, y alarma y llave al final
_CN = ('08', 'Cierre del Negocio')
_CIERRE = [
    ('Turn off background music', 'General', 'Shift manager'),
    ('Make sure no guests remain in the shop', 'FOH', 'Shift manager'),
    ('Clean and bring in the patio if used', 'Patio', 'Shift manager'),
    ('Wood-fired oven: let it cool down on its own, with the door and flue set as its manufacturer says (never douse '
     'it with water)', 'Kitchen', 'Shift manager'),
    ('Turn off the POS / card terminal (or leave on standby)', 'Register', 'Shift manager'),
    ('Bring in the outdoor signage', 'Outside', 'Shift manager'),
    ('Empty trash cans in common areas and restrooms', 'Restrooms', 'Shift manager'),
    ('Final safety check (gas, water, outlets and the oven)', 'General', 'Shift manager'),
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
for _fila, (_mes, _evento, _antel, _dir) in CALENDARIO.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'A%d' % _fila)] = _mes
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'B%d' % _fila)] = _evento
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'D%d' % _fila)] = _antel

# ==========================================================================
# VALORES_EN: (libro, hoja ES, celda) → (valor ES tal cual, valor EN). Los mínimos del «Inventario Diario» vienen
# como TEXTO en el ES («30»): la fórmula «B<D» compara un número con un texto y pide SIEMPRE (errata ES, como la
# cafetería). La EN los escribe como NÚMERO; los de kg, g y ml, convertidos a lb, oz y fl oz (redondeado a una cifra
# de pedido).
# ==========================================================================
_MINIMOS = [  # fila, ES, EN
    (6, '30', 30), (7, '10', 22), (8, '3', 7), (9, '100', 4), (10, '2', 4), (12, '5', 11), (13, '6', 6), (14, '1', 2),
    (15, '0.5', 1), (16, '4', 4), (18, '5', 5), (19, '10', 10), (20, '300', 10), (21, '2', 2), (22, '100', 3),
    (24, '2', 4), (25, '1', 2), (26, '1', 2), (27, '200', 7), (28, '0.5', 1), (30, '1', 2), (31, '0.5', 1),
    (32, '0.5', 1), (33, '0.5', 1), (34, '200', 7), (35, '0.5', 1), (36, '3', 3), (38, '40', 40), (39, '30', 30),
    (40, '15', 15), (41, '100', 100), (42, '30', 30),
]
VALORES_EN = OrderedDict((('05', 'Inventario Diario', 'D%d' % f), (es, en)) for f, es, en in _MINIMOS)

# ==========================================================================
# ADAPTAR (en español, con el dato US; las cifras y normas salen de REGLAS_US)
# ==========================================================================
_A = _base.ADAPTAR
_CAMARAS = _A[('01', 'Apertura Cocina', 'B18')]
_LAVADO = _A[('02', 'Fríos', 'B6')]
_DATE = _A[('01', 'Cierre Cocina', 'B6')]
_TIRA = 'sanitizante aprobado a la concentración de la etiqueta, medida con tira (test strip) (FDA Food Code 4-501.114)'
_ALERGENOS = ('Alérgenos US: los 9 principales (FALCPA + FASTER Act: leche, huevo, pescado, crustáceos, frutos de '
              'cáscara, cacahuete, trigo, soja y sésamo); en una pizzería, trigo y leche van en casi todo. El gluten en '
              'sí no es uno de los 9 (el trigo sí) y la lactosa es una intolerancia, no un alérgeno: se recogen igual; '
              'en UK, los 14 (cereales con gluten)')
_MAKE_LINE = ('Línea de montaje = make line (pizza prep table refrigerada): los inserts de salsa, queso y toppings a '
              '41 °F o menos (FDA Food Code 3-501.16)')
_MOZZ = ('La mozzarella es TCS: a 41 °F o menos (FDA Food Code 3-501.16); se corta en tandas pequeñas y vuelve a la '
         'cámara')
_MOZZ_FECHA = ('Mozzarella fresca abierta: tapada, a 41 °F o menos y con date marking: 7 días como máximo contando el '
               'día de apertura, sin pasar el use-by (FDA Food Code 3-501.17(B))')
_MASA_FRIO = ('Fermentación en frío (cold fermentation): las bolas, en cajas de masa (dough boxes) tapadas, a la cámara '
              'a 41 °F o menos y con la fecha (y la hora) de la masa; el plazo de uso lo marca tu receta (sin cifra)')
_CENIZA = ('La ceniza se retira en frío (si el horno sigue caliente al cierre, a la mañana siguiente antes de '
           'encender): a un contenedor METÁLICO con tapa, lejos de lo que arde; nunca a la basura ni a un cubo de '
           'plástico (NFPA 96, cocina con combustible sólido)')
_ENFRIAR = ('Lo cocinado se enfría de 135 °F a 70 °F en 2 h y a 41 °F en 4 h más (FDA Food Code 3-501.14) antes de '
            'guardarlo tapado')
_RECALENTAR = ('Lo hecho antes que se vaya a mantener en caliente se recalienta a 165 °F en 2 h como máximo (FDA Food '
               'Code 3-403.11) y se mantiene a 135 °F o más')
_HUEVO = ('con huevo pasteurizado, o aviso al consumidor en la carta si lleva huevo crudo o poco hecho (FDA Food Code '
          '3-603.11)')
_APPS = 'Plataformas US: DoorDash, Uber Eats y Grubhub (third-party delivery apps)'
_HORNO_F = '°F: 400-450 °C = 750–840 °F; 300 °C = 570 °F; el °C, solo entre paréntesis tras el °F'
_HEREDA_ADAPTAR = [('08', 'Apertura del Negocio', 'B8'), ('09', 'Cierre de Caja', 'B10'),
                   ('09', 'Registro Mensual', 'A37'),
                   ('B02', 'Instrucciones', 'B8')] + [k for k in _A if k[:2] == ('09', 'Instrucciones')]
ADAPTAR = OrderedDict((k, _A[k]) for k in _HEREDA_ADAPTAR)
ADAPTAR.update([
    # 01 · cocina
    (('01', 'Apertura Cocina', 'B7'), _A[('01', 'Apertura Cocina', 'B7')]),
    (('01', 'Apertura Cocina', 'B15'), 'Horno de leña, de gas o eléctrico (deck oven): precalentar el tiempo que diga su '
     'fabricante; 45-60 min como referencia del kit (el de leña suele necesitar más)'),
    (('01', 'Apertura Cocina', 'B16'), _HORNO_F + ' (napolitana)'),
    (('01', 'Apertura Cocina', 'B17'), 'Leña seca (o pellets) guardada lejos de la boca del horno y de cualquier fuente '
     'de calor, como digan el fabricante y tu fire marshal'),
    (('01', 'Apertura Cocina', 'B21'), _CAMARAS),
    (('01', 'Apertura Cocina', 'B25'), 'Si la salsa se cocina: ' + _ENFRIAR + ', a 41 °F o menos y con fecha'),
    (('01', 'Apertura Cocina', 'B26'), _MOZZ),
    (('01', 'Apertura Cocina', 'B28'), _LAVADO),
    (('01', 'Apertura Cocina', 'B29'), _MAKE_LINE),
    (('01', 'Apertura Cocina', 'B38'), 'Mesa de trabajo y de amasado: limpiar y luego sanitizar con ' + _TIRA),
    (('01', 'Apertura Sala', 'B18'), _APPS),
    (('01', 'Cierre Cocina', 'B6'), _MASA_FRIO),
    (('01', 'Cierre Cocina', 'B8'), _MOZZ_FECHA),
    (('01', 'Cierre Cocina', 'B10'), _DATE),
    (('01', 'Cierre Cocina', 'B13'), _CENIZA),
    (('01', 'Cierre Cocina', 'B15'), 'Con horno de leña, la campana no se apaga mientras quede fuego o brasas: lo que '
     'digan el fabricante del horno y el de la campana'),
    (('01', 'Cierre Cocina', 'B23'), _MASA_FRIO),
    (('01', 'Cierre Cocina', 'B26'), 'Descongelar en la cámara a 41 °F o menos (FDA Food Code 3-501.13), nunca a '
     'temperatura ambiente'),
    (('01', 'Cierre Sala', 'B7'), 'Limpiar las mesas y luego sanitizarlas con ' + _TIRA + '; paños en su cubo de '
     'sanitizante'),
    # 02 · estaciones
    (('02', 'Pizzero Horno', 'B6'), _HORNO_F),
    (('02', 'Línea Montaje', 'B6'), _MAKE_LINE),
    (('02', 'Línea Montaje', 'B7'), _MOZZ),
    (('02', 'Línea Montaje', 'B9'), 'Carne cruda (p. ej. salchicha italiana sin cocinar) en su propio insert y con su '
     'utensilio, separada de lo listo para consumir (FDA Food Code 3-302.11)'),
    (('02', 'Línea Montaje', 'B10'), _LAVADO + '; la rúcula y la albahaca van crudas al salir del horno'),
    (('02', 'Línea Montaje', 'B19'), 'Limpiar la make line completa y sanitizarla con ' + _TIRA),
    (('02', 'Complementaria', 'B6'), _LAVADO),
    (('02', 'Complementaria', 'B9'), 'Carbonara ' + _HUEVO),
    (('02', 'Complementaria', 'B10'), 'Tiramisú ' + _HUEVO + '; los postres TCS (tiramisú, panna cotta) a 41 °F o menos '
     'con date marking (7 días, FDA Food Code 3-501.17)'),
    (('02', 'Complementaria', 'B12'), _RECALENTAR + ' (salsas y pre-elaboraciones)'),
    (('02', 'Complementaria', 'B16'), _ENFRIAR + '; etiquetar con date marking (7 días como máximo contando el día de '
     'preparación, FDA Food Code 3-501.17)'),
    # 03
    (('03', 'Semanal Manager', 'B8'), _A[('03', 'Diario Manager', 'B29')] + ', más las apps de delivery'),
    # 04 · perfiles
    (('04', 'Pizzero', 'B19'), _MASA_FRIO),
    (('04', 'Pizzero', 'B21'), _CENIZA),
    (('04', 'Encargado', 'B9'), _APPS),
    (('04', 'Camarero', 'B12'), _ALERGENOS),
    (('04', 'Camarero', 'B13'), 'Cerveza y vino solo si tu licencia lo permite, a mayores de 21 con ID'),
    (('04', 'Camarero', 'B16'), _A[('04', 'Camarero', 'B20')]),
    (('04', 'Repartidor', 'A1'), 'Repartidor propio → in-house delivery driver (no las apps)'),
    (('04', 'Repartidor', 'B6'), 'En EE. UU. el repartidor suele usar su coche: combustible, luces y neumáticos; carnet y '
     'seguro del vehículo en vigor y archivados (el seguro personal puede excluir el reparto: que lo confirme con su '
     'aseguradora)'),
    (('04', 'Repartidor', 'B7'), 'Bolsa térmica = insulated delivery bag (hot bag): limpia y cerrada; lo caliente a 135 °F '
     'o más y lo frío (bebidas, ensaladas, postres) en una bolsa aparte a 41 °F o menos (FDA Food Code 3-501.16)'),
    (('04', 'Repartidor', 'B16'), 'Limpiar el interior de la bolsa, desinfectarlo con un sanitizante apto para '
     'superficies en contacto con alimentos y dejarla secar abierta'),
    (('04', 'Repartidor', 'B17'), 'El efectivo de los pedidos, al shift manager con sus tickets; las propinas del '
     'repartidor son suyas: el negocio no puede quedárselas (FLSA, 29 U.S.C. 203(m)(2)(B))'),
    # 05
    (('05', 'Instrucciones', 'B6'), 'Describe la lista US de «Quarterly & Annual»: control de plagas, campana, conductos y '
     'chimenea del horno de leña (NFPA 96), revisión del horno, extintores y su prueba hidrostática, extinción de la '
     'campana, gas, frío, legionela, agua, aceite usado, residuos, seguros y POS / sales tax. Sin DDD, BIE, Verifactu '
     'ni facturación española'),
    (('05', 'Limpieza Semanal', 'B8'), 'El equipo limpia la boca y lo accesible del tiro; el conducto y la chimenea los '
     'inspecciona y limpia el contratista (hojas «Monthly Maintenance» y «Quarterly & Annual», NFPA 96)'),
    (('05', 'Limpieza Semanal', 'B14'), 'Tablas de corte: lavar, aclarar y sanitizar con ' + _TIRA),
    (('05', 'FIFO Semanal', 'B6'), 'Masa preparada: la fecha (y la hora) de cada caja de masa; se usa en el plazo de tu '
     'receta, la más antigua primero'),
    (('05', 'FIFO Semanal', 'B7'), _MOZZ_FECHA),
    (('05', 'FIFO Semanal', 'B8'), 'Fiambres abiertos (jamón cocido): date marking, 7 días como máximo contando el día de '
     'apertura (FDA Food Code 3-501.17); el pepperoni curado y el prosciutto, según la etiqueta del fabricante'),
    (('05', 'FIFO Semanal', 'D29'), 'Descongela en la cámara a 41 °F o menos (FDA Food Code 3-501.13), nunca a '
     'temperatura ambiente'),
    (('05', 'Mantenimiento Mensual', 'B7'), 'Sistema de extracción del horno de leña (campana, conducto y chimenea): '
     'inspección MENSUAL de grasa y creosota por una persona cualificada y limpieza cuando haya depósitos (NFPA 96, '
     'cocina con combustible sólido)'),
    (('05', 'Mantenimiento Mensual', 'B14'), _A[('05', 'Mantenimiento Mensual', 'B21')]),
    (('05', 'Trimestral y Anual', 'B21'), _A[('05', 'Trimestral y Anual', 'B23')] + '; la sonda del horno, según su '
     'fabricante'),
    # 06
    (('06', 'Noche Fútbol', 'A1'), 'Fútbol → fútbol americano (NFL): «Game Night / Super Bowl — Delivery Rush»'),
    (('06', 'Noche Fútbol', 'B10'), 'Oferta para el partido (game-day deal / combo) en redes sociales'),
    (('06', 'San Valentín', 'B14'), 'Bebida de bienvenida para parejas: sin alcohol, o un prosecco solo donde tu licencia '
     'y tu estado permiten regalar alcohol (21+ con ID)'),
    (('06', 'Navidad', 'B6'), _ALERGENOS + '; por escrito'),
    (('06', 'Navidad', 'B13'), "Stock extra para los días en que tus proveedores no entregan (sobre todo Christmas Day y "
     "New Year's Day)"),
    (('06', 'Temporada Terraza', 'B10'), _A[('06', 'Temporada Terraza', 'B6')] + ': comprobar que está vigente y '
     'renovarlo si caduca esta temporada'),
    # 08
    (('08', 'Apertura del Negocio', 'B20'), 'Horno de leña: encenderlo con tiempo para que llegue a temperatura antes del '
     'servicio, el que diga su fabricante (1 h como referencia del kit; el de leña suele necesitar más)'),
    (('08', 'Apertura del Negocio', 'B21'), 'Si en esa barra expones porciones (pizza by the slice): en vitrina caliente a '
     '135 °F o más, o con time as a public health control: hora marcada y a la basura a las 4 h (FDA Food Code '
     '3-501.19)'),
])
# 08 B8 (ronda 1 m15 del bar, NO_HEREDAR): la apertura de puertas suma las salidas de emergencia
ADAPTAR[('08', 'Apertura del Negocio', 'B8')] = (_A[('08', 'Apertura del Negocio', 'B8')] + '; añade: salidas de '
                                                 'emergencia despejadas y señales de salida (exit signs) iluminadas')
for _fila, (_mes, _evento, _antel, _dir) in CALENDARIO.items():
    if _dir:
        ADAPTAR[(HOJA_CAL[0], HOJA_CAL[1], 'C%d' % _fila)] = 'Evento EN: «%s». %s' % (_evento, _dir)
# aplicar_en.objetivo_ajuste / G3 (errata ES): las tareas largas del ES no llevan ajuste de texto y salen cortadas por
# la celda vecina (en el base sí lo llevan); la EN activa el ajuste también donde el ES tampoco cabía
AJUSTE_MAQUETA_ES = True
# Celdas ES con °C cuya EN NO lleva cifra en °F: ninguna (las del horno, convertidas)
CELSIUS_SIN_F = frozenset()

# ==========================================================================
# REGLAS_US: las del base + las de la pizzería (fuente única de las cifras y normas que el kit puede afirmar)
# ==========================================================================
REGLAS_US = OrderedDict(_base.REGLAS_US)
REGLAS_US.update([
    ('masa_frio', ('masa en fermentación en frío a 41 °F o menos, tapada y con fecha; el plazo, el de la receta',
                   '[criterio del kit] la masa cruda no es TCS')),
    ('make_line', ('make line / pizza prep table: inserts a 41 °F o menos', 'FDA Food Code 2022 §3-501.16(A)(2)')),
    ('mozzarella', ('mozzarella TCS a 41 °F o menos; abierta, date marking 7 días desde la apertura sin pasar el use-by',
                    'FDA Food Code 2022 §3-501.16 y §3-501.17(B)')),
    ('descongelar', ('descongelar en refrigeración a 41 °F o menos', 'FDA Food Code 2022 §3-501.13')),
    ('crudo_separado', ('carne cruda separada de lo listo para consumir', 'FDA Food Code 2022 §3-302.11')),
    ('tphc', ('time as a public health control: hora marcada; servir o descartar DENTRO de las 4 h',
              'FDA Food Code 2022 §3-501.19(B)')),
    ('horno_temp', ('400-450 °C = 750-840 °F (napolitana) · 300 °C = 570 °F (romana)',
                    '[criterio del kit] cifras del ES convertidas')),
    ('horno_fabricante', ('precalentado, enfriado, campana y revisión del horno según el fabricante',
                          '[fabricante] manual del horno')),
    ('ceniza', ('ceniza en contenedor metálico con tapa, lejos de combustibles', 'NFPA 96, cap. 14 (solid fuel cooking)')),
    ('delivery', ('bolsa térmica: lo caliente a 135 °F o más y lo frío a 41 °F o menos; objetivo de entrega < 30 min',
                  'FDA Food Code 2022 §3-501.16; [criterio del kit] tiempo')),
    ('propinas_repartidor', ('el negocio no puede quedarse las propinas del personal', 'FLSA, 29 U.S.C. 203(m)(2)(B)')),
    ('seguro_reparto', ('hired and non-owned auto si se reparte con coche propio; el seguro personal puede excluir el '
                        'reparto', '[criterio del kit] práctica de seguros')),
    ('agua', ('red: Consumer Confidence Report anual de la compañía; pozo propio: análisis según el departamento de salud',
              '40 CFR Part 141, Subpart O; [local] departamento de salud')),
    ('alergenos_trigo', ('el trigo está entre los 9; el gluten en sí no, y la lactosa es una intolerancia',
                         'FALCPA 2004 + FASTER Act 2021')),
    ('edad_alcohol', ('21 años para comprar o consumir alcohol, en todos los estados',
                      'National Minimum Drinking Age Act of 1984 (23 U.S.C. 158)')),
    ('alcohol_gratis', ('regalar alcohol está restringido en algunos estados', '[estatal] ABC / liquor authority')),
    ('dias_fuertes', ('Super Bowl, viernes de Cuaresma, March Madness, playoffs NBA / NHL, Halloween, víspera de '
                      'Thanksgiving y Nochevieja, días fuertes de delivery', '[criterio del kit] calendario comercial US')),
    ('inventario', ('mínimos de kg → lb (×2,2), de g → oz (÷28,35) y de ml → fl oz (÷29,6); L → qt (1 qt ≈ 0,95 L)',
                    '[criterio del kit] conversión')),
])
# °F que el kit puede afirmar (G7): las del base + 32 (calibración) + las del horno
GRADOS_F_SPEC = {-31, -4, 0, 32, 41, 70, 100, 135, 165, 570, 750, 840}

# ==========================================================================
# Pistas y dependencias de la pizzería (extraer_textos.py)
# ==========================================================================
PISTAS_CAMBIO = {r'Kit de Tareas': 'D2: «Pizza Shop Checklists Kit Pro»'}
PISTAS_FUERA = (r'Restaurante Casual',)
PISTAS_EXTRA = [
    (r'Pizzería', 'D2: la EN no lleva el sufijo de variante: quita «— Pizzería»; pizzería → pizza shop / pizzeria'),
    (r'[Hh]orno', 'horno de leña → wood-fired oven; de piedra / solera → deck oven (stone deck); de cinta → conveyor '
                  'oven; boca → oven mouth; tiro / trampilla → draft / flue damper'),
    (r'[Pp]ala\b|[Cc]ortapizza|[Rr]asqueta|[Rr]odillo', 'pala → pizza peel; cortapizza → pizza cutter; rasqueta / '
                                                        'cortador de masa → dough cutter (bench scraper); rodillo → '
                                                        'rolling pin'),
    (r'[Bb]olas? de masa|[Mm]asa|[Ff]ermenta|[Tt]emperar|[Aa]masa', 'bolas de masa → dough balls; temperar → temper '
                                                                    '(bring to room temp); fermentación lenta en frío → '
                                                                    'cold fermentation; amasar → mix the dough; mesa de '
                                                                    'amasado → dough bench'),
    (r'[Ll][ií]nea de montaje|[Ii]nserts?|\bpase\b', 'línea de montaje → make line (pizza prep table); inserts → '
                                                     'inserts; pase → the pass / expo'),
    (r'[Bb]olsa térmica|[Bb]olsas delivery', 'bolsa térmica → insulated delivery bag (hot bag)'),
    (r'[Tt]ake-away|[Pp]ara llevar|[Dd]elivery|[Aa]pps', 'take-away → takeout / carryout; delivery apps → third-party '
                                                         'delivery apps (DoorDash, Uber Eats, Grubhub)'),
    (r'Glovo|Just Eat', 'Glovo / Just Eat → DoorDash / Grubhub (Uber Eats se queda)'),
    (r'[Rr]epartidor|[Rr]ider', 'repartidor / rider → delivery driver'),
    (r'[Pp]izzero', 'pizzero / maestro pizzero → pizza maker (pizzaiolo); cocinero de línea → line cook'),
    (r'[Ee]ncargad', 'encargado/a → shift manager (NUNCA «shift lead»)'),
    (r'[Ff]ior di latte|[Bb]ufala|[Ss]emola|[Hh]arina 00', 'fior di latte → fresh mozzarella (fior di latte); '
                                                          'mozzarella di bufala → buffalo mozzarella; semola → '
                                                          'semolina; harina 00 → 00 flour'),
    (r'[Ll]eopardo', 'leopardo → leopard spotting (leoparding)'),
    (r'[Cc]omanda', 'comanda → ticket; 86s → 86s (86\'d items)'),
    (r'TPV|[Dd]atáfono', 'TPV / datáfono → POS / card terminal'),
    (r'[Cc]uadrar caja', 'cuadrar caja → cash up / balance the drawer'),
    (r'[Cc]ontra reembolso', 'contra reembolso → cash on delivery'),
    (r'[Mm]ermas?', 'mermas → waste (waste log)'),
    (r'[Ff]útbol', 'fútbol → (American) football: NFL Sundays, Monday Night Football, Super Bowl; noche de partido → '
                   'game night'),
    (r'RRSS|redes', 'RRSS → social media'),
    (r'[Pp]izarra', 'pizarra → menu board / chalkboard'),
    (r'[Ll]ocal\b', 'el local → the shop / the pizzeria (nunca «restaurant» ni «venue»)'),
]
DEPENDENCIAS_EXTRA = OrderedDict([
    ('variante', ('Sufijo de variante «Pizzería»', r'— Pizzería|· Pizzería', 'D2: la EN no lleva sufijo')),
    ('horno', ('Horno de leña: ceniza, chimenea, campana', r'[Hh]orno de leña|[Cc]eniza|[Cc]himenea',
               'D-PIZ: NFPA 96 (combustible sólido) y el fabricante del horno')),
    ('masa', ('Masa y fermentación en frío', r'[Bb]olas de masa|[Ff]ermentaci', 'D-PIZ: 41 °F, fecha, plazo de la receta')),
    ('delivery', ('Reparto propio y apps', r'[Rr]epartidor|[Bb]olsa térmica|Glovo|Just Eat',
                  'D-PIZ: bolsas 135 / 41 °F, apps US, propinas del repartidor (FLSA)')),
    ('alcohol', ('Alcohol en la pizzería', r'[Pp]rosecco|[Cc]erveza|[Cc]ava\b', 'D-PIZ: solo con licencia, 21+ con ID; '
                 'regalarlo, según el estado')),
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
    if rx.search('sidewalk cafe permit') or rx.search('restaurant consultant'):
        err.append('TERMINOS_PROHIBIDOS caza lo permitido («sidewalk cafe permit», «restaurant consultant»)')
    for k, v in list(GLOSARIO.items()) + list(POR_CELDA.items()) + list(CLAVES.items()):
        if k not in _base.GLOSARIO or k in _GLOSARIO_PIZZA:
            if isinstance(v, str) and rx.search(v):
                err.append('texto EN fijado con un término prohibido: %r → %r' % (k, v))
    if CITA_AUTOTEST.strip('()').split()[-1] in ' '.join(f for _v, f in REGLAS_US.values()):
        err.append('CITA_AUTOTEST está en REGLAS_US: G7 no la cazaría')
    for k, v in POR_CELDA.items():
        if k[1] in ('Cierre Sala',) and k[2].startswith('E') and not re.match(r'^\d{1,2}:\d{2} (AM|PM)$', v):
            err.append('POR_CELDA: hora fijada %r sin formato US: %r' % (k, v))
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
    factor = {('kg', 'lb'): 2.2046, ('g', 'oz'): 1 / 28.35, ('ml', 'fl oz'): 1 / 29.57, ('L', 'qt'): 1,
              ('uds', 'ea'): 1, ('manojos', 'bunches'): 1}
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
    # las filas reordenadas del 08 y del 01 «Cierre Sala»: el ES tiene tarea en todas
    for fila in range(5, 5 + len(_CIERRE)):
        if (_CN[0], _CN[1], 'B%d' % fila) not in tx:
            err.append('08 cierre: B%d sin tarea en el ES' % fila)
    for coord in ('A13', 'B18', 'B19', 'A20', 'B21', 'B22'):
        if (_CS[0], _CS[1], coord) not in tx:
            err.append('01 Cierre Sala: %s sin texto en el ES' % coord)
    return err


def cruzar_base(p_pizza, p_base):
    """Lo heredado POR CELDA del base (POR_CELDA y ADAPTAR) tiene en la pizzería el mismo texto ES que en el base;
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
    tb, tr = textos(p_base), textos(p_pizza)
    for nombre, claves in (('POR_CELDA', _HEREDA_POR_CELDA), ('ADAPTAR', _HEREDA_ADAPTAR)):
        for k in claves:
            if tr.get(k) != tb.get(k):
                err.append('%s heredado %r: el texto ES de la pizzería %r ≠ base %r' % (nombre, k, tr.get(k),
                                                                                       tb.get(k)))
    # (el 05 «Trimestral y Anual» B16 toma el EN del base con otra redacción ES del mismo tema: aceite usado)
    equivalentes = [(('03', 'Mensual Manager', 'B9'), ('03', 'Mensual Manager', 'B16'))]
    for kc, kb in equivalentes:
        if tr.get(kc, '').split(' (')[0] != tb.get(kb, '').split(' (')[0]:
            err.append('%r de la pizzería no es la fila del base %r: %r ≠ %r' % (kc, kb, tr.get(kc), tb.get(kb)))
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
    print('mapas_pizza.py: {} ficheros · {} pestañas · {} glosario · {} por celda · {} valores · {} adaptar · '
          '{} reglas · {} errores'.format(len(FICHEROS), len(HOJAS), len(GLOSARIO), len(POR_CELDA), len(VALORES_EN),
                                          len(ADAPTAR), len(REGLAS_US), len(e)))
    raise SystemExit(1 if e else 0)
