#!/usr/bin/env python3
"""
mapas_ghost.py — Ghost Kitchen Checklists Kit Pro (EN) · DELTA del Kit de Tareas para Dark Kitchen
(`kit-tareas-dark-kitchen`, 11 xlsx v2.0) sobre `mapas.py` (Restaurant Checklists Kit Pro). SPEC: `ghost/SPEC.md`
(solo el delta). Sexto hermano vertical, hecho como el bar, la cafetería, el catering, la pizzería y la hamburguesería.
Sesión Claude Code, 18-oct-2026.

Se usa con `--kit ghost` (kit.py). Importa `mapas.py` y SOLO añade o sobrescribe: producto, ficheros, títulos,
pestañas (cocina 100 % delivery multi-marca: sin sala ni barra; estación caliente, estación fría, empaquetado,
cocinero multi-marca, empaquetador, gestor de plataformas y encargado de operaciones; 43 hojas), glosario (zonas y
puestos de una ghost kitchen, unidades del inventario), calendario (filas 5-26 como el base; días fuertes del delivery
US), POR_CELDA (caja 09 heredada TAL CUAL; 05 «Quarterly & Annual» de una ghost kitchen; el orden de la apertura y el
cierre del 08 y los bloques sin sala ni barra del 07), VALORES_EN (mínimos del inventario en lb / qt y como número),
ADAPTAR, CLAVES (+ «⚠️ PEDIR») y REGLAS_US (+ precintos, alérgenos en las apps, parásitos, arroz de sushi, caliente y
frío en el pase, cocción, permisos). La hora de 12 h, la caja en dólares y el resto se heredan. Las funciones del base
que leen constantes (titulo_interior, autotest, cruzar_censo) se re-enlazan a ESTE módulo. Ejecutado como script:
autotest + cruce con ghost/censo_es.json + cruce con el base (lo heredado por celda tiene el mismo texto ES).

    python3 ghost/mapas_ghost.py
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
AQUI = os.path.dirname(os.path.abspath(__file__))              # ghost/ (el import * trae el AQUI del base)

ORIGEN_ES = 'kit-tareas-dark-kitchen'
PRODUCTO = 'Ghost Kitchen Checklists Kit Pro'
# D2: el H1 del brief (113 caracteres) se recorta a ~70 manteniendo ghost + cloud kitchen y la intención principal
TITULO_SEO = 'Ghost Kitchen Checklists Kit Pro: Cloud Kitchen Opening & Closing Templates'
SLUG = 'ghost-kitchen-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_GHOST_KITCHEN_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
MARCA_ES = '— Kit de Tareas Recurrentes · Dark Kitchen · AI Chef Pro · aichef.pro'
MARCA_EN = '— ' + PRODUCTO + ' · AI Chef Pro · aichef.pro'
VARIANTES_ES = ('Dark Kitchen',)
# heredar.py: memoria con VARIAS fuentes, en orden de preferencia (base, bar, cafetería, catering, pizzería y
# hamburguesería; gana la primera que acierta)
_SUF = lambda v: [(' — Dark Kitchen', ' — ' + v), (' · Dark Kitchen', ' · ' + v)]  # noqa: E731
MEMORIA = [('base', '', _SUF('Restaurante Casual')), ('bar', 'bar', _SUF('Bar / Cocktails')),
           ('cafe', 'cafe', _SUF('Cafetería / Brunch')), ('catering', 'catering', _SUF('Catering / Eventos')),
           ('pizza', 'pizza', _SUF('Pizzería')), ('burger', 'burger', _SUF('Hamburguesería'))]
# heredar.py: EN heredado que en una ghost kitchen no vale tal cual → pendientes (motivo «contexto»). Sin sala, barra,
# terraza ni clientes en el local; «restaurant» suelto va al traductor salvo «virtual / delivery-only restaurant».
# «delivery driver(s)» y «commissary» SÍ valen aquí (repartidores de las apps, cocina compartida).
RX_CONTEXTO_PENDIENTE = (r'(?i)\b(?:dining rooms?|dine-in|FOH|host stands?|hosts?|hostess|servers?|waitstaff|'
                         r'guests?|tables? service|reservations?|patios?|sidewalk|bars?|bartenders?|barbacks?|'
                         r'cocktails?|beer|liquor|baristas?|coffee shops?|cafes?|tip jars?|bussers?|head chefs?|'
                         r'sous chefs?|MOD|shift leads?|kitchen leads?|venues?|banquets?|BEOs?|line-up|pizzas?|'
                         r'pizzerias?|dough|burger joints?|burger shops?|(?<!virtual )(?<!delivery-only )'
                         r'restaurants?(?! consultant))\b')
# heredar.py: cadenas idénticas a una fuente cuyo EN no vale en la ghost kitchen (→ pendientes → G1.json, con base_en)
NO_HEREDAR = {
    'Abrir persianas / puerta principal': 'ronda 1 m15 del bar: + salidas de emergencia despejadas y señales de salida',
    'Abrir local y desactivar alarma': 'la cafetería dice «the shop»: en una ghost kitchen es la cocina (the kitchen / '
                                       'the site)',
    'Fecha: ___/___/______    Turno: ☐ Mañana  ☐ Noche    Responsable: ________________':
        'la pizzería dice «☐ AM ☐ Mid ☐ PM»: el ES trae DOS turnos (☐ AM ☐ PM) y el responsable (Assigned to)',
}
# gates_en.py G2: términos de otros kits que NINGUNA celda EN de la ghost kitchen puede llevar (no hay sala, barra,
# terraza, alcohol ni personal de sala). «restaurant» queda permitido («virtual / delivery-only restaurant»);
# «commissary» y «delivery drivers» también. TERMINO_PROHIBIDO_EJEMPLO: lo que inyecta el autotest.
TERMINOS_PROHIBIDOS = (r'(?i:\b(?:dining rooms?|dine-in|host stands?|hostess|servers?|waitstaff|table service|'
                       r'patios?|bars?|bartenders?|barbacks?|cocktails?|beer|liquor|baristas?|coffee shops?|cafes?|'
                       r'tip jars?|bussers?|head chefs?|sous chefs?|shift leads?|kitchen leads?|venues?|banquets?|'
                       r'BEOs?|line-up|pizzerias?|dough)\b)|\b(?:MOD|FOH)\b')
TERMINO_PROHIBIDO_EJEMPLO = 'Seat the walk-in party in the dining room.'
REFERENCIAS_TRADUCTOR = ['ghost/SPEC.md', 'SPEC.md §0-§3 y §7.2 (brief)', 'textos_en/glosario.json (glosario de la '
                         'prosa del kit base)', 'ghost/textos_en/heredado.json (cómo se dijo ya cada cosa: base, bar, '
                         'cafetería, catering, pizzería y hamburguesería)', 'ghost/mapas_ghost.py: GLOSARIO, HOJAS, '
                         'FICHEROS, TITULOS, POR_CELDA, REGLAS_US', '../GLOSARIO-JERGA-ES-EN.md']
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v2.0'),
    ('keywords', 'ghost kitchen checklist, cloud kitchen checklist, virtual kitchen checklist, delivery-only restaurant '
                 'checklist, ghost kitchen opening checklist, ghost kitchen closing checklist, virtual brands, AI Chef '
                 'Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

# ==========================================================================
# Ficheros (D5: «cloud kitchen» 8.100/mes US, «virtual kitchen» 590, «virtual restaurant» 390, «delivery only
# restaurant» 170; «ghost kitchen» manda en el glosario de jerga; las variantes de checklist sin volumen: los ficheros
# combinan ghost kitchen / cloud kitchen / virtual kitchen / delivery-only kitchen)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-apertura-cierre.xlsx', '01-ghost-kitchen-opening-closing-checklists.xlsx'),
    ('02-partidas-cocina.xlsx', '02-cloud-kitchen-station-checklists.xlsx'),
    ('03-tareas-manager.xlsx', '03-ghost-kitchen-manager-checklist.xlsx'),
    ('04-tareas-perfiles.xlsx', '04-virtual-kitchen-duties-by-role.xlsx'),
    ('05-tareas-semanales-mensuales.xlsx', '05-cloud-kitchen-cleaning-checklist-inventory-maintenance.xlsx'),
    ('06-eventos-festivos.xlsx', '06-ghost-kitchen-peak-and-event-checklists.xlsx'),
    ('07-plantilla-personalizable.xlsx', '07-blank-ghost-kitchen-checklist-template.xlsx'),
    ('08-apertura-cierre-negocio.xlsx', '08-delivery-only-kitchen-opening-closing-checklist.xlsx'),
    ('09-apertura-cierre-caja.xlsx', '09-cash-drawer-opening-closing.xlsx'),
    ('BONUS-01-briefing-servicio.xlsx', 'BONUS-01-ghost-kitchen-pre-shift-meeting-template.xlsx'),
    ('BONUS-02-calendario-anual-tareas.xlsx', 'BONUS-02-ghost-kitchen-delivery-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)
TITULOS = OrderedDict([
    ('01-ghost-kitchen-opening-closing-checklists.xlsx',
     'Ghost Kitchen Opening & Closing Checklists: Kitchen, Packing & Delivery Apps'),
    ('02-cloud-kitchen-station-checklists.xlsx', 'Cloud Kitchen Station Checklists: Hot Station, Cold Station & Packing'),
    ('03-ghost-kitchen-manager-checklist.xlsx',
     'Ghost Kitchen Manager Checklist: Daily, Weekly, Monthly & Shift Handover'),
    ('04-virtual-kitchen-duties-by-role.xlsx',
     'Virtual Kitchen Duties by Role: Cook, Packer, App Manager & Operations Manager'),
    ('05-cloud-kitchen-cleaning-checklist-inventory-maintenance.xlsx',
     'Cloud Kitchen Cleaning Checklist, Inventory & Maintenance Schedule'),
    ('06-ghost-kitchen-peak-and-event-checklists.xlsx',
     'Ghost Kitchen Peak Checklists: Friday Rush, Game Night, Brand Launch & Holidays'),
    ('07-blank-ghost-kitchen-checklist-template.xlsx', 'Blank Ghost Kitchen Checklist Template (Editable)'),
    ('08-delivery-only-kitchen-opening-closing-checklist.xlsx',
     'Delivery-Only Kitchen Opening & Closing Checklist (Whole Site)'),
    ('09-cash-drawer-opening-closing.xlsx', 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log'),
    ('BONUS-01-ghost-kitchen-pre-shift-meeting-template.xlsx',
     'BONUS: Ghost Kitchen Pre-Shift Meeting Template (Huddle Notes)'),
    ('BONUS-02-ghost-kitchen-delivery-calendar.xlsx', 'BONUS: Ghost Kitchen Holiday & Peak Delivery Days Calendar (US)'),
])
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

HOJAS = OrderedDict(_base.HOJAS)
HOJAS.update([
    ('Estación Caliente', 'Hot Station'), ('Estación Fría', 'Cold Station'), ('Empaquetado', 'Packing Station'),
    ('Cocinero Multi-Marca', 'Multi-Brand Cook'), ('Empaquetador', 'Packer'), ('Gestor Plataformas', 'App Manager'),
    ('Encargado Operaciones', 'Operations Manager'), ('Inventario Diario', 'Daily Inventory'),
    ('Pico Viernes Noche', 'Friday Night Rush'), ('Noche Fútbol', 'Game Night'), ('Lanzamiento Marca', 'Brand Launch'),
    ('Navidad Fin Año', 'Holiday Season'),
    # 08: el «negocio» es la cocina entera (sin restaurante abierto al público)
    ('Apertura del Negocio', 'Site Opening'), ('Cierre del Negocio', 'Site Closing'),
])
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Apertura Cocina', 'Cierre Cocina']),
    ('02', ['Instrucciones', 'Estación Caliente', 'Estación Fría', 'Empaquetado']),
    ('03', ['Instrucciones', 'Diario Manager', 'Semanal Manager', 'Mensual Manager', 'Handover Turno']),
    ('04', ['Instrucciones', 'Cocinero Multi-Marca', 'Empaquetador', 'Gestor Plataformas', 'Encargado Operaciones']),
    ('05', ['Instrucciones', 'Inventario Diario', 'Limpieza Semanal', 'FIFO Semanal', 'Mantenimiento Mensual',
            'Trimestral y Anual']),
    ('06', ['Instrucciones', 'Pico Viernes Noche', 'Noche Fútbol', 'Lanzamiento Marca', 'Navidad Fin Año']),
    ('07', ['Instrucciones', 'Por Franja Horaria', 'Por Área', 'Por Perfil']),
    ('08', ['Instrucciones', 'Apertura del Negocio', 'Cierre del Negocio']),
    ('09', ['Instrucciones', 'Apertura de Caja', 'Cierre de Caja', 'Registro Mensual']),
    ('B01', ['Instrucciones', 'Briefing']),
    ('B02', ['Instrucciones', 'Calendario Anual']),
])

# ==========================================================================
# GLOSARIO: el base entero (opcional en la ghost kitchen) + celdas cortas de una cocina 100 % delivery. Jerga US:
# line cook, packer, app manager, shift manager, driver pickup; unidades del inventario en lb / qt / ea (VALORES_EN).
# ==========================================================================
GLOSARIO = OrderedDict(_base.GLOSARIO)
_GLOSARIO_GHOST = OrderedDict([
    # zonas (C)
    ('Packaging', 'Packing'), ('Office', 'Office'), ('Operaciones', 'Operations'), ('Recogida riders', 'Driver pickup'),
    ('Almacén', 'Storage'), ('Cámara', 'Walk-in'),
    # puestos (D); 4 sobrescriben el base: Auxiliar, Jefe de Cocina, Responsable de caja y Todos
    ('Cocinero caliente', 'Hot station cook'), ('Cocinero frío', 'Cold station cook'), ('Empaquetador', 'Packer'),
    ('Gestor', 'App manager'), ('Encargado/a', 'Shift manager'), ('Turno saliente', 'Outgoing shift'),
    ('Responsable de caja', 'Cashier / shift manager'), ('Jefe de Cocina', 'Kitchen manager'), ('Todos', 'All staff'),
    ('Auxiliar', 'Dishwasher / prep'),
    # cuándo (E): «2 weeks out», como el bar
    ('Viernes AM', 'Friday AM'), ('Viernes 17:00', 'Friday 5:00 PM'), ('Día antes', 'Day before'),
    ('2 días antes', '2 days out'), ('3 días antes', '3 days out'), ('1 sem antes', '1 week out'),
    ('2 sem antes', '2 weeks out'), ('15 días antes', '2 weeks out'), ('Día 1-7', 'Days 1–7'), ('Día 7', 'Day 7'), ('Dic', 'Dec'),
    ('31 Dic', 'Dec 31'), ('Diario', 'Daily'),
    # tabla de congelación del 05 (el resto, del base)
    ('3-6 meses', '3–6 months'), ('1 mes', '1 month'), ('No congelar', 'Do not freeze'),
    # inventario (05): unidades US; los mínimos de kg cambian de cifra (VALORES_EN), los de L, uds y sets no
    ('kg', 'lb'), ('L', 'qt'), ('uds', 'ea'), ('sets', 'sets'), ('Unidad', 'Unit'),
])
GLOSARIO.update(_GLOSARIO_GHOST)
GLOSARIO_OPCIONAL = frozenset(_base.GLOSARIO)
PUESTOS_ES = frozenset(_base.PUESTOS_ES | {'Packaging', 'Office', 'Operaciones', 'Recogida riders', 'Almacén',
                                           'Cámara', 'Cocinero caliente', 'Cocinero frío', 'Empaquetador', 'Gestor',
                                           'Encargado/a', 'Turno saliente', 'Todos'})

# ==========================================================================
# CLAVES: el inventario diario avisa con «⚠️ PEDIR» / «OK» (literales de fórmula)
# ==========================================================================
CLAVES = OrderedDict(_base.CLAVES)
CLAVES.update([('⚠️ PEDIR', '⚠️ REORDER'), ('OK', 'OK')])

# ==========================================================================
# BONUS-02 «Holiday Calendar»: misma estructura que el base (filas 5-26: A mes · B fecha/evento · C tareas ·
# D antelación). A, B y D fijados; C = traductor, con ADAPTAR donde el evento o sus tareas cambian. Días fuertes del
# delivery US (Super Bowl, March Madness, el 4 de julio, la temporada de fútbol americano, Halloween, el frío). Orden
# cronológico (lección m10 de la pizzería). fila → (mes, evento, antelación, ADAPTAR de C o None).
# ==========================================================================
CALENDARIO = OrderedDict([
    (5, ('January', "Jan 1 — New Year's Day", '1 week', None)),
    (6, ('February', 'Super Bowl Sunday (2nd Sunday in Feb)', '2 weeks',
         'Sustituye a Reyes. Uno de los días con más pedidos a domicilio del año en EE. UU.: pedidos de grupo y '
         'anticipados (party orders), combos para compartir, stock y packaging extra, tiempos de preparación de cada '
         'app ajustados al pico y refuerzo del empaquetado')),
    (7, ('February', "Feb 14 — Valentine's Day", '2 weeks', None)),
    (8, ('February–March', 'Mardi Gras (varies)', '1 week', None)),
    (9, ('February–April', 'Lent Fridays + Easter Sunday (varies)', '2 weeks',
         'Sustituye al Día del Padre (en EE. UU. va en junio, fila 16). Tareas = las de Semana Santa del ES (fila 10), '
         'adaptadas: los viernes de Cuaresma, opción de pescado o vegetal (meatless Fridays) en las marcas que '
         'encajen; el domingo de Pascua, decidir el horario y publicarlo en cada app. Sin bacalao, potaje ni '
         'torrijas')),
    (10, ('March', "Mar 17 — St. Patrick's Day + March Madness", '2 weeks',
          'Sustituye a Semana Santa (pasa a la fila 9). Tareas: un especial de St. Patrick en las apps; los partidos de '
          'March Madness (marzo-abril) suben el delivery de tarde y de fin de semana: combos para compartir, stock, '
          'packaging y turnos extra. Sin alcohol (la cocina no lo vende)')),
    (11, ('March–April', 'Warm weather: lunch orders drop', '1 month', None)),
    (12, ('May', 'May 5 — Cinco de Mayo', '1 week',
          'Sustituye a las comuniones (sus tareas pasan a la fila 15, graduaciones). Tareas: especiales mexicanos en '
          'las marcas que encajen (tacos, bowls), promo en las apps y refuerzo de la cena. Sin margaritas ni alcohol')),
    (13, ('May', "2nd Sunday — Mother's Day", '2 weeks',
          'Sustituye al 1 de mayo (el Labor Day de EE. UU. va en septiembre, fila 19). Tareas = las del Día de la Madre '
          'del ES (fila 14): menú especial para llevar, packaging cuidado y refuerzo del pico de mediodía')),
    (14, ('May', 'Memorial Day (last Monday)', '1 month',
          'Sustituye al Día de la Madre (pasa a la fila 13). Empieza el verano (ronda 1 M3: en delivery NO es temporada '
          'alta): decidir el horario del festivo y publicarlo en cada app, montar la carta de verano y planificar la '
          'plantilla para las semanas más flojas del verano')),
    (15, ('May–June', 'Graduation season', '1 month',
          'Sustituye a «Inicio temporada alta» (pasa a la fila 14). Tareas = las de las comuniones del ES (fila 12): '
          'bandejas y menús de grupo para recoger o entregar (graduation parties), precio por persona y packaging '
          'para el transporte')),
    (16, ('June', "3rd Sunday — Father's Day", '2 weeks',
          'Sustituye a San Juan. Tareas = las del Día del Padre del ES (fila 9): menú para llevar de comida familiar y '
          'promo de mediodía en cada marca')),
    (17, ('July', 'Jul 4 — Independence Day', '1 week',
          'Sustituye a la fila de temporada alta (sus tareas pasan a la fila 18). Tareas: decidir el horario (muchos '
          'cierran o abren solo de día) y publicarlo en cada app; pedidos grandes para las fiestas (party orders) con '
          'hora de entrega')),
    (18, ('July–August', 'Summer slowdown (warm weather, vacations, school break)', 'Ongoing',
          'Sustituye a la Asunción (el 15 de agosto no es festivo en EE. UU.). Ronda 1 M3: en verano el delivery suele '
          'BAJAR (calor, vacaciones, sin colegio; como la fila 11 y el 10-K de DoorDash): recortar producción y turnos, '
          'mantener el horario, combos de mediodía y platos de calor (bowls, ensaladas, bebidas frías) y preparar la '
          'carta de otoño; junto a playas, zonas turísticas o eventos de verano puede ir al revés')),
    (19, ('September', 'Labor Day (1st Monday) + football season', '2 weeks',
          'Sustituye a la vuelta al cole. Tareas = las del ES (menú de otoño por marca y promo de mediodía para '
          'oficinas, sin el calco «vuelta a la rutina»), más combos para el fútbol americano (jueves, domingo y lunes '
          'por la noche y el universitario del sábado)')),
    (20, ('October', 'Oct 31 — Halloween', '1 week', None)),
    (21, ('November', 'Thanksgiving (4th Thursday) + Black Friday', '2 weeks',
          'Sustituye a Todos los Santos. Decidir si se abre el jueves (muchos cierran) y, si se cierra, pausar las '
          'marcas en TODAS las apps; el viernes (Black Friday), refuerzo del mediodía y stock para dos días seguidos')),
    (22, ('November', 'Cold, rainy days: orders go up', '1 week', None)),
    (23, ('Nov–Dec', 'Holiday shopping weekends', '2 weeks',
          'Sustituye al puente de la Constitución (en EE. UU. no existe). Del Black Friday a Nochebuena, los fines de '
          'semana de compras y de frío: stock, refuerzo de turnos y horario publicado en cada app')),
    (24, ('December', 'Holiday office parties (group orders)', '1 month', None)),
    (25, ('December', 'Dec 24–25 — Christmas', '2 weeks',
          'Decidir si se abre el día de Navidad (muchos cierran) y, si se cierra, pausar las marcas en TODAS las apps y '
          'publicar el horario; menú de temporada por marca, packaging especial y stock para la semana con menos '
          'entregas de proveedor')),
    (26, ('December', "Dec 31 — New Year's Eve", '2 weeks',
          'Menú de Nochevieja para pedir a domicilio (sin el calco «menú de gala»), cierre temprano de pedidos y horario '
          'avisado en cada app. Sin uvas, cava ni alcohol')),
])

# ==========================================================================
# POR_CELDA: lo heredado del base (mismo texto ES en la misma celda o en la fila equivalente; lo comprueba
# cruzar_base) + lo de la ghost kitchen
# ==========================================================================
_HEREDA_POR_CELDA = [k for k in _base.POR_CELDA if k[0] == '09'] + [
    ('05', 'Trimestral y Anual', 'B6'), ('05', 'Trimestral y Anual', 'D6'), ('05', 'Trimestral y Anual', 'E6')]
POR_CELDA = OrderedDict((k, _base.POR_CELDA[k]) for k in _HEREDA_POR_CELDA)
_T = ('05', 'Trimestral y Anual')
POR_CELDA.update([
    # 03 · conservación de fichajes (B16 en el base; mismo texto ES y EN)
    (('03', 'Mensual Manager', 'B11'), _base.POR_CELDA[('03', 'Mensual Manager', 'B16')]),
    # 05 · Inventario: la línea de marca va con otro formato en el ES (dos puntos y raya final) → la del kit con su
    # raya final (no es la línea D19: G3 cuenta las MARCA_EN contra las MARCA_ES del ES)
    (('05', 'Inventario Diario', 'A45'), MARCA_EN + ' —'),
    # 05 · Instrucciones (errata ES, como la cafetería, la pizzería y la hamburguesería): el inventario no está
    # protegido y el ES lo promete (mismo EN que la hamburguesería)
    (('05', 'Instrucciones', 'B23'), '▸ Checklist sheets with formulas are protected WITHOUT a password: the input cells '
                                     '(the green ones) are unlocked. The Daily Inventory sheet is left unprotected so '
                                     "you can add products: don't type over the Status column."),
    # 05 · Trimestral y Anual: servicios contratados US de una cocina multi-marca que cocina todo el día (NFPA 96)
    (_T + ('B7',), 'Hood and duct cleaning by a certified contractor (NFPA 96): quarterly if high volume (24-hour '
                   'cooking, charbroiling or wok), semiannual if moderate — a multi-brand kitchen cooking from morning to '
                   'night often goes quarterly: your hood contractor and fire marshal decide'),
    (_T + ('D7',), 'Hood cleaning co.'), (_T + ('E7',), 'Quarterly'),
    (_T + ('B8',), 'Hood fire suppression inspected every 6 months (NFPA 96) and annual extinguisher maintenance by a '
                   'licensed fire protection company: new tag and record (OSHA 1910.157); hydrostatic tests as the label '
                   'says (OSHA 1910.157(f))'),
    (_T + ('D8',), 'Fire safety co.'), (_T + ('E8',), 'Semiannual'),
    (_T + ('B9',), 'Gas lines and appliance connections (griddle, range, oven, fryer) checked by a licensed pro, as '
                   'often as your local code requires'),
    (_T + ('D9',), 'Licensed plumber'), (_T + ('E9',), 'Annual'),
    (_T + ('B10',), 'Legionella: if you have a cooling tower or at-risk hot water, keep a water management program as '
                    'your local health code requires'),
    (_T + ('D10',), 'Water treatment co.'),
    (_T + ('A11',), '  REFRIGERATION, USED OIL & WASTE'),
    (_T + ('B12',), 'Refrigeration service by an EPA 608-certified tech: walk-in, reach-ins, prep-table coolers and the '
                    'blast chiller if you have one — coils, gaskets and refrigerant leak check'),
    (_T + ('D12',), 'Refrigeration tech'),
    (_T + ('B13',), 'Used fryer oil: pickups by a licensed recycler as often as your volume needs; every quarter, check '
                    'the receipts are on file and the outdoor container is closed and not leaking'),
    (_T + ('D13',), 'Oil recycler'),
    (_T + ('B14',), 'Review the cardboard and plastic recycling contract with your hauler (pickups usually run weekly or '
                    'more: a ghost kitchen goes through far more packaging than a regular restaurant) and keep the grease '
                    'trap pumping manifests, as often as your local FOG rules require'),
    (_T + ('D14',), 'Waste hauler'),
    (_T + ('B15',), 'Once a year, have the oven and griddle thermostats and any built-in probes checked against a known '
                    'standard; the probe thermometers get an ice-point check (32 °F) at opening (Hot Station tab in 02, '
                    'task #1) and after any drop'),
    (_T + ('A16',), '  INSURANCE, DELIVERY APPS & SALES TAX'),
    (_T + ('B17',), "Review insurance: general liability with products coverage (the food is eaten off-site), property "
                    "and workers' comp, plus renewal dates"),
    (_T + ('B18',), "Review each delivery app's contract and commission plan, plus your POS and sales tax settings: who "
                    "collects and remits the sales tax on app orders depends on your state's marketplace facilitator "
                    'rules'),
])
# 08 · Apertura (errata ES): la impresora de cada plataforma, el timbre de riders con las indicaciones de cada app y los
# tiempos de preparación se comprobaban ANTES de encender las tablets (fila 20) y las marcas se activaban a las 09:30,
# una hora antes que en el 01 y el 04 (10:30). Filas 11-22 reordenadas: local → recogida y empaquetado → tablets →
# impresoras, timbre y tiempos → marcas activas a las 10:30. (EN, zona, hora; D = «Encargado» en todas). Las filas 5-10
# no cambian. Cada tupla lleva la fila ES de origen (la comprueba cruzar_censo)
_AN = ('08', 'Apertura del Negocio')
_APERTURA_08 = [  # fila ES de origen, EN, zona EN, hora EN
    (14, 'Check restrooms: paper, soap, cleanliness, air freshener', 'Restrooms', '9:15 AM'),
    (15, 'Check cleanliness of common areas (entrance, hallways)', 'Common areas', '9:15 AM'),
    (16, 'Check the driver pickup area: handoff counter clear, pickup shelves labeled by brand and the lighting '
         'working', 'Driver pickup', '9:15 AM'),
    (17, "Set up the packing and labeling station: boxes, bags, lids, utensils, tamper-evident seals and each brand's "
         'labels within reach', 'Packing', '9:30 AM'),
    (18, 'Check the packing station is restocked with brand labels, flyers and the printed allergen sheets',
     'Packing', '9:30 AM'),
    (19, 'Turn on displays / info screens if any', 'General', '9:30 AM'),
    (21, 'Check packaging stock', 'Storage', '9:30 AM'),
    (20, 'Turn on the delivery app tablets (DoorDash, Uber Eats, Grubhub)', 'Operations', '10:00 AM'),
    (11, "Turn on the kitchen display (KDS) and each app's ticket printer and check they print: no printed ticket, the "
         'order never goes out', 'Operations', '10:30 AM'),
    (12, 'Check the driver door bell or intercom works and the pickup instructions posted on each app are still '
         'correct', 'Entrance', '10:30 AM'),
    (13, "Review today's scheduled orders and set the prep times posted on each app to the expected volume",
     'Operations', '10:30 AM'),
    (22, 'Turn on the brands on every app and check each one shows as OPEN and is receiving orders', 'Operations',
     '10:30 AM'),
]
for _fila, (_o, _b, _c, _e) in enumerate(_APERTURA_08, 11):
    for _col, _v in (('B', _b), ('C', _c), ('E', _e)):
        POR_CELDA[_AN + ('%s%d' % (_col, _fila),)] = _v
# 01 «Apertura Cocina» y 04 «Gestor Plataformas» (ronda 1 M4, la errata del 08 en otras dos hojas): las marcas se
# encendían ANTES de comprobar la impresora, las cartas y los 86. Mismas filas (zona «Office», responsable el mismo en
# todas); None = la celda conserva su EN (G1). Fila ES de origen en cada tupla (la comprueba cruzar_censo)
_AC = ('01', 'Apertura Cocina')
_TABLETS_01 = [  # fila, fila ES de origen, EN (None = la de su fila), hora EN
    (31, 31, None, '10:00 AM'), (32, 32, None, '10:00 AM'),
    (33, 36, 'Check the ticket printer works', '10:15 AM'), (34, 34, None, '10:15 AM'), (35, 35, None, '10:15 AM'),
    (36, 37, '86 anything out of stock: pause that dish or brand in each app', '10:30 AM'),
    (37, 33, 'Turn on all brands in DoorDash, Uber Eats and Grubhub — last, once the tablets, printer, menus and 86s are '
             'checked', '10:30 AM'),
]
for _f, _o, _b, _e in _TABLETS_01:
    if _b:
        POR_CELDA[_AC + ('B%d' % _f,)] = _b
    POR_CELDA[_AC + ('E%d' % _f,)] = _e
_GP = ('04', 'Gestor Plataformas')
_APPS_04 = [(7, 8, 'Check that menus are up to date'), (8, 10, '86 the dishes that are out of stock'), (9, 9, None),
            (10, 7, 'Turn on all brands in DoorDash, Uber Eats and Grubhub')]
for _f, _o, _b in _APPS_04:
    if _b:
        POR_CELDA[_GP + ('B%d' % _f,)] = _b
# 08 E5 (ronda 1 m12): la alarma a la hora del 04 «Encargado Operaciones» B6 (08:45), antes que la campana del 01
POR_CELDA[('08', 'Apertura del Negocio', 'E5')] = '8:45 AM'
# 05 · Inventario (ronda 1 m11): los 0,5 L → 1 pt (como la hamburguesería)
for _f in (24, 25, 27):
    POR_CELDA[('05', 'Inventario Diario', 'C%d' % _f)] = 'pt'
# 08 · Cierre (errata ES): desactivar las marcas y apagar las tablets iba DESPUÉS de la alarma y la llave, y las
# persianas se cerraban antes de recoger la señalización y vaciar papeleras. Toda la secuencia, mismas 15 filas (E =
# «Close»): pedidos y riders → marcas y tablets → empaquetado y caja → el local → alarma, puertas y llave al final
_CN = ('08', 'Cierre del Negocio')
_CIERRE_08 = [  # fila ES de origen, EN, zona EN, responsable EN
    (5, 'Pause new orders on every brand: from here on, only finish the orders already accepted', 'Operations',
     'Shift manager'),
    (6, 'Check no driver is still waiting and no orders are left on the pickup shelf', 'Driver pickup',
     'Shift manager'),
    (18, 'Turn off the brands on every app and check none is still OPEN taking orders', 'Operations', 'Shift manager'),
    (19, 'Turn off the app tablets', 'Operations', 'Shift manager'),
    (7, 'Clean and clear the pickup area and the packing station: toss cardboard and leftover seals and labels, and '
        'leave the handoff counter clear', 'Packing', 'Shift manager'),
    (8, 'Turn off the POS / card terminal (or leave on standby)', 'Register', 'Shift manager'),
    (12, 'Bring in the outdoor signage', 'Outside', 'Shift manager'),
    (14, 'Empty trash cans in common areas and restrooms', 'Restrooms', 'Shift manager'),
    (15, 'Final safety check (gas, water, outlets)', 'General', 'Shift manager'),
    (13, 'Check that windows are closed', 'General', 'Shift manager'),
    (11, 'Turn off HVAC', 'General', 'Shift manager'),
    (10, 'Turn off lights (leave security lighting)', 'General', 'Shift manager'),
    (16, 'Set the alarm', 'Entrance', 'Last one out'),
    (9, 'Close security gate and doors', 'Entrance', 'Last one out'),
    (17, 'Lock up and verify it is locked', 'Entrance', 'Last one out'),
]
# responsable que cambia (declarado): marcas y tablets (ES «Último en salir») → el encargado; alarma y persianas (ES
# «Encargado») → el último en salir, con la llave
_RESPONSABLE_CAMBIA = frozenset({18, 19, 16, 9})
for _fila, (_o, _b, _c, _d) in enumerate(_CIERRE_08, 5):
    for _col, _v in (('B', _b), ('C', _c), ('D', _d)):
        POR_CELDA[_CN + ('%s%d' % (_col, _fila),)] = _v
# 07 (errata ES): la plantilla trae bloques de SALA y BARRA, que una ghost kitchen no tiene → empaquetado y recogida,
# office y apps; en «Por Perfil», el jefe de sala → el empaquetador
for _k, _v in (
        (('07', 'Por Área', 'A12'), '  PACKING & PICKUP — type your packing and driver pickup tasks below'),
        (('07', 'Por Área', 'A19'), '  OFFICE & APPS — type your tablet and delivery app tasks below'),
        (('07', 'Por Perfil', 'A12'), '  PACKING — type your packing and pickup tasks below')):
    POR_CELDA[_k] = _v
for _f in range(13, 18):
    POR_CELDA[('07', 'Por Área', 'C%d' % _f)] = 'Packing'
    POR_CELDA[('07', 'Por Perfil', 'D%d' % _f)] = 'Packer'
for _f in range(20, 25):
    POR_CELDA[('07', 'Por Área', 'C%d' % _f)] = 'Office'
for _fila, (_mes, _evento, _antel, _dir) in CALENDARIO.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'A%d' % _fila)] = _mes
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'B%d' % _fila)] = _evento
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'D%d' % _fila)] = _antel

# ==========================================================================
# VALORES_EN: (libro, hoja ES, celda) → (valor ES tal cual, valor EN). Los mínimos del «Inventario Diario» van como
# NÚMERO; los de kg, convertidos a lb y redondeados a un formato de compra de EE. UU. (cajas y bolsas de 5 / 10 lb,
# lección D2 de la pizzería; ×1,6 como máximo); los de L (→ qt), uds (→ ea) y sets, con la misma cifra, salvo los
# 0,5 L → 1 pt (ronda 1 m11).
# ==========================================================================
_MINIMOS = [  # fila, ES, EN
    (6, '5', 10), (7, '3', 10), (8, '2', 5), (9, '1', 2), (11, '5', 10), (12, '3', 5), (13, '30', 30), (14, '1', 2),
    (16, '2', 5), (17, '2', 5), (18, '2', 5), (19, '8', 8), (20, '1', 2), (21, '0.5', 1),
    (23, '1', 1), (24, '0.5', 1), (25, '0.5', 1), (26, '1', 1), (27, '0.5', 1), (28, '2', 2),
    (30, '50', 50), (31, '50', 50), (32, '50', 50), (33, '50', 50), (35, '40', 40), (36, '40', 40), (37, '40', 40),
    (38, '40', 40), (40, '60', 60), (41, '100', 100), (42, '60', 60), (43, '20', 20),
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
# ronda 1 m3: el máximo de la FDA, o el plazo más corto del propio kit
_DATE_KIT = (_DATE + '; o menos donde la hoja «FIFO Semanal» del 05 fije un plazo más corto (salsas caseras 5 días, '
             'proteínas 3, vegetales cortados 2)')
_TIRA = 'sanitizante aprobado a la concentración de la etiqueta, medida con tira (test strip) (FDA Food Code 4-501.114)'
_APPS = 'Plataformas US: DoorDash, Uber Eats y Grubhub (third-party delivery apps); tablets → order tablets'
_PRECINTO = ('Precinto de seguridad → tamper-evident seal (sticker o cinta que se rompe al abrir la bolsa): California '
             'lo exige para la comida lista para consumir que recoge un repartidor de app (AB 3336, desde 2021); en '
             'el resto, revisa la norma de tu ciudad o estado (check local rules) y las apps lo recomiendan')
_ALERGENOS = ('Alérgenos US: los 9 principales (FALCPA + FASTER Act: leche, huevo, pescado, crustáceos, frutos de '
              'cáscara, cacahuete, trigo, soja y sésamo); el gluten en sí no es uno de los 9 (el trigo sí) y la '
              'lactosa es una intolerancia, no un alérgeno: se recogen igual; en UK, los 14')
_ALERGENOS_APP = ('El cliente no puede preguntar en un mostrador: los alérgenos de cada plato (los 9 principales de '
                  'EE. UU.; en UK, los 14), en la ficha del plato de cada app. En EE. UU. no hay una norma federal que '
                  'lo exija a la comida de restaurante, pero las apps tienen el campo y algunos estados o ciudades '
                  'piden avisos propios (check local rules); en UK es obligatorio en la venta a distancia: antes de '
                  'comprar y al entregar')
_ACEITE = ('Filtrar el aceite como diga el fabricante de la freidora (muchas llevan filtrado incorporado pensado para '
           'el aceite caliente; otras piden dejarlo enfriar) y cambiarlo cuando lo diga el medidor de TPM (sin límite '
           'federal; ronda 1 M1), con guantes resistentes al calor, delantal y gafas; el usado, al contenedor del '
           'reciclador (used cooking oil recycler). Sin cifra de temperatura del kit')
_ENFRIAR = ('Lo cocinado se enfría de 135 °F a 70 °F en 2 h y a 41 °F en 4 h más (FDA Food Code 3-501.14) antes de '
            'guardarlo tapado')
_RECALENTAR = ('Lo hecho antes que se vaya a mantener en caliente se recalienta a 165 °F en 2 h como máximo (FDA Food '
               'Code 3-403.11) y se mantiene a 135 °F o más')
_CALIENTE = 'Mantenimiento en caliente: 135 °F o más (FDA Food Code 3-501.16)'
_HUEVO = ('con huevo pasteurizado, o aviso al consumidor en la ficha del plato si lleva huevo crudo (FDA Food Code '
          '3-603.11)')
_PARASITOS = ('Destrucción de parásitos US, las TRES opciones de FDA Food Code 3-402.11 (ronda 1 M2): congelado y '
              'guardado a −4 °F o menos 7 días; o congelado a −31 °F o menos hasta sólido y guardado a −31 °F o menos '
              '15 h; o congelado a −31 °F o menos hasta sólido y guardado a −4 °F o menos 24 h. El registro (o la '
              'declaración escrita del proveedor) se guarda 90 días (3-402.12); aviso al consumidor en la ficha del '
              'plato de cada app (FDA Food Code 3-603.11). Sin «≥24 h a −20 °C» ni la palabra «anisakis» como norma')
_ARROZ = ('Arroz de sushi: si se acidifica para tenerlo fuera de frío hace falta una varianza del departamento de '
          'salud y un plan HACCP que él aprueba (FDA Food Code 3-502.11; ronda 1 m18); si no, a 41 °F o menos, o con time as a public health '
          'control: procedimiento escrito, hora marcada y a la basura a las 4 h (FDA Food Code 3-501.19)')
_COCCION = ('Cocinar cada proteína a su temperatura, comprobada con sonda en el centro: pollo 165 °F, carne picada '
            '155 °F durante 17 s, pescado 145 °F durante 15 s (FDA Food Code 3-401.11); crudo debajo de lo listo '
            'para consumir, con el pollo crudo abajo del todo, debajo de la carne y del pescado (FDA Food Code '
            '3-302.11; ronda 1 m10)')
_UTENSILIOS = ('añade: pinzas, espátulas, cucharas de servir y tablas de corte, lavadas, aclaradas y sanitizadas cada '
               '4 h como mínimo en servicio, o cambiadas por unas limpias (FDA Food Code 4-602.11; ronda 1 m4)')
_SEPARAR = ('añade: lo caliente y lo frío en bolsas o compartimentos separados, para que lo caliente siga a 135 °F o '
            'más y lo frío a 41 °F o menos hasta que lo recoja el repartidor (FDA Food Code 3-501.16)')
_COMISIONES = ('Comisiones US: DoorDash, Uber Eats y Grubhub cobran según el plan contratado (más o menos del 15 al 30 '
               '%); algunas ciudades las limitan (Nueva York, San Francisco): revisa tu contrato y la norma local. Sin '
               'cifras por plataforma')
_PERMISO = ('añade: cada cocina lleva su permiso sanitario (health permit); las marcas virtuales suelen ir con el de la '
            'cocina, pero algunas ciudades piden comunicarlas o registrarlas, y el nombre comercial de cada marca '
            '(DBA) se registra si tu estado lo pide: compruébalo con tu departamento de salud (check local rules)')
_HEREDA_ADAPTAR = [('01', 'Apertura Cocina', 'B10'), ('09', 'Cierre de Caja', 'B10'),
                   ('09', 'Registro Mensual', 'A37'),
                   ('B02', 'Instrucciones', 'B8')] + [k for k in _A if k[:2] == ('09', 'Instrucciones')
                                                      and k != ('09', 'Instrucciones', 'B6')]
ADAPTAR = OrderedDict((k, _A[k]) for k in _HEREDA_ADAPTAR)
ADAPTAR.update([
    # 01 · Apertura Cocina (el orden del ES ya es campana → gas → equipos; la campana suma su comprobación de tiro)
    (('01', 'Apertura Cocina', 'B7'), _A[('01', 'Apertura Cocina', 'B7')]),
    (('01', 'Apertura Cocina', 'B9'), _A[('01', 'Apertura Cocina', 'B9')]),
    (('01', 'Apertura Cocina', 'B12'), 'Añade: comprobar que tira (una servilleta contra los filtros se queda pegada) y '
     'que los filtros están puestos y limpios'),
    (('01', 'Apertura Cocina', 'B13'), _A[('01', 'Apertura Cocina', 'B14')]),
    (('01', 'Apertura Cocina', 'B15'), 'Baño maría → steam table / hot well: ' + _CALIENTE),
    (('01', 'Apertura Cocina', 'B16'), _CAMARAS),
    (('01', 'Apertura Cocina', 'B19'), 'Si la salsa se cocina: ' + _ENFRIAR + '; la mayonesa casera (sriracha mayo, '
     'alioli), ' + _HUEVO),
    (('01', 'Apertura Cocina', 'B18'), 'Añade: sobre superficies ya limpias y sanitizadas (tarea #30; ronda 1 m14)'),
    (('01', 'Apertura Cocina', 'B21'), _ENFRIAR + '; si se mantienen en caliente: ' + _RECALENTAR),
    (('01', 'Apertura Cocina', 'B28'), _PRECINTO),
    (('01', 'Apertura Cocina', 'B35'), _ALERGENOS_APP),
    (('01', 'Apertura Cocina', 'B40'), 'Superficies de trabajo: limpiar y luego sanitizar con ' + _TIRA),
    # 01 · Cierre Cocina
    (('01', 'Cierre Cocina', 'B6'), _DATE_KIT),
    (('01', 'Cierre Cocina', 'B8'), 'Tapada y a 41 °F o menos; lo cocinado, enfriado antes: ' + _ENFRIAR),
    (('01', 'Cierre Cocina', 'B9'), 'Congelador a 0 °F o menos; la tabla de vida útil, en la hoja «FIFO Semanal» del 05 '
     '(nombres EN de la hoja y del fichero)'),
    (('01', 'Cierre Cocina', 'B13'), _ACEITE),
    (('01', 'Cierre Cocina', 'B14'), 'Apagar la campana la última, cuando la plancha, el horno y la freidora ya se hayan '
     'enfriado'),
    (('01', 'Cierre Cocina', 'B15'), _TEMP_FRIO),
    (('01', 'Cierre Cocina', 'B18'), 'Limpiar todas las superficies y estaciones y luego sanitizarlas con ' + _TIRA),
    (('01', 'Cierre Cocina', 'B26'), 'Cuadrar → reconcile: los pedidos del día contra el informe de ventas o de pagos '
     '(payouts) de cada app'),
    (('01', 'Cierre Cocina', 'B30'), 'Descongelar en la cámara a 41 °F o menos (FDA Food Code 3-501.13), nunca a '
     'temperatura ambiente'),
    # 02 · estaciones
    (('02', 'Estación Caliente', 'B6'), 'Añade: comprobar el termómetro de sonda en agua con hielo (32 °F) y '
     'recalibrarlo si no marca bien (ronda 1 m5)'),
    (('02', 'Estación Caliente', 'B7'), _COCCION),
    (('02', 'Estación Caliente', 'B8'), _CALIENTE + '; lo que se guarde, ' + _ENFRIAR[0].lower() + _ENFRIAR[1:]),
    (('02', 'Estación Caliente', 'B11'), _UTENSILIOS),
    (('02', 'Estación Caliente', 'B14'), _CALIENTE + ' hasta que el plato pasa al empaquetado'),
    (('02', 'Estación Caliente', 'B18'), _DATE_KIT),
    (('02', 'Estación Fría', 'B6'), _LAVADO),
    (('02', 'Estación Fría', 'B7'), _ARROZ),
    (('02', 'Estación Fría', 'B8'), _PARASITOS),
    (('02', 'Estación Fría', 'B11'), 'Inserts tapados y a 41 °F o menos en la mesa fría (FDA Food Code 3-501.16)'),
    (('02', 'Estación Fría', 'B15'), _UTENSILIOS),
    (('02', 'Estación Fría', 'B17'), _DATE_KIT),
    (('02', 'Estación Fría', 'B18'), 'Criterio del kit (calidad), el mismo de la hoja «FIFO Semanal» del 05 (ronda 1 '
     'm2): fruta cortada 24 h y vegetales cortados 2 días; las hojas verdes, el tomate y el melón cortados son TCS: a '
     '41 °F o menos y con date marking (FDA Food Code 3-501.16 y 3-501.17)'),
    (('02', 'Empaquetado', 'B8'), _PRECINTO),
    (('02', 'Empaquetado', 'B11'), 'Empaquetar en el envase de la marca; ' + _SEPARAR),
    (('02', 'Empaquetado', 'B15'), _PRECINTO),
    (('02', 'Empaquetado', 'B16'), 'Estantería de expedición → driver pickup shelf, por app'),
    # 03
    (('03', 'Diario Manager', 'B24'), _A[('03', 'Diario Manager', 'B35')]),
    (('03', 'Semanal Manager', 'B18'), _ALERGENOS),
    (('03', 'Mensual Manager', 'B8'), _COMISIONES),
    (('03', 'Mensual Manager', 'B21'), 'Ronda 1 m15: el equipo desengrasa los filtros cada semana (hoja «Weekly Deep '
     'Clean» del 05); el técnico revisa motor, correas y filtros cada mes; el contratista limpia el conducto (hoja '
     '«Quarterly & Annual», NFPA 96)'),
    (('03', 'Mensual Manager', 'B22'), _A[('03', 'Mensual Manager', 'B23')] + '; botiquín (first aid kit) completo'),
    (('03', 'Handover Turno', 'B12'), 'Estado del aceite (última lectura de TPM) y fecha del último cambio; el cambio, '
     'cuando lo diga el medidor de TPM y según el fabricante (sin cifra de temperatura del kit)'),
    # 04 · perfiles
    (('04', 'Cocinero Multi-Marca', 'B18'), 'Tapada y a 41 °F o menos (FDA Food Code 3-501.16)'),
    (('04', 'Cocinero Multi-Marca', 'B19'), 'Limpiar la estación y luego sanitizarla con ' + _TIRA),
    (('04', 'Empaquetador', 'B15'), _PRECINTO),
    (('04', 'Cocinero Multi-Marca', 'B13'), 'Tiempos = ticket times: pedidos listos en 8-12 min, como el 02 (criterio '
     'del kit; ronda 1 m13)'),
    # 05
    (('05', 'Instrucciones', 'B6'), 'Describe la lista US de «Quarterly & Annual»: control de plagas, campana y '
     'conductos (NFPA 96), extintores y extinción de la campana, gas, legionela, frío, aceite usado, cartón y '
     'plástico del packaging, separador de grasas (grease trap), calibración de termómetros, seguros, contratos de las apps y sales tax. Sin DDD, BIE, '
     'Verifactu ni facturación española'),
    (('05', 'Limpieza Semanal', 'B7'), 'El equipo desmonta y desengrasa los FILTROS de la campana (no la campana); el '
     'conducto lo limpia el contratista (hoja «Quarterly & Annual», NFPA 96)'),
    (('05', 'Limpieza Semanal', 'B9'), 'Tablas de corte: limpieza a fondo y revisión semanal (frotar, sanitizar con '
     + _TIRA + ', y repasar o cambiar las de cortes hondos o manchas); en uso se lavan, aclaran y sanitizan cada 4 h '
     'como mínimo (FDA Food Code 4-602.11; ronda 1 m4)'),
    (('05', 'Limpieza Semanal', 'B10'), 'Limpieza a fondo de la freidora (boil-out) como diga su fabricante'),
    (('05', 'FIFO Semanal', 'B6'), 'Proteínas frescas: 3 días como máximo (criterio del kit) y nunca más allá de la '
     'fecha del proveedor'),
    (('05', 'FIFO Semanal', 'B7'), 'Salsas caseras: 5 días como máximo (criterio del kit; el date marking de la FDA '
     'permite 7 contando el de preparación, 3-501.17)'),
    (('05', 'FIFO Semanal', 'B8'), 'Vegetales cortados: 2 días como máximo (criterio del kit, dentro de los 7 del date '
     'marking de la FDA, 3-501.17)'),
    (('05', 'FIFO Semanal', 'B14'), 'Medidor de TPM o tiras (color, olor y humo solo como respaldo); anotar la fecha '
     'del último cambio; sin límite federal: cambiarlo cuando lo diga el medidor y según el fabricante (ronda 1 M1; '
     'sin cifra de temperatura del kit)'),
    (('05', 'FIFO Semanal', 'D29'), 'La congelación solo cuenta como destrucción de parásitos a −4 °F o menos 7 días, o '
     'a −31 °F hasta sólido y luego 15 h a −31 °F o 24 h a −4 °F (FDA Food Code 3-402.11), con registro o la '
     'declaración del proveedor (3-402.12): un congelador normal a 0 °F no llega; sin «anisakis» (ronda 1 M2)'),
    (('05', 'FIFO Semanal', 'D32'), 'Congelar el mismo día en porciones planas; para servirlo caliente, recalentar a '
     '165 °F en 2 h como máximo (FDA Food Code 3-403.11). El arroz cocido templado es el clásico de la intoxicación '
     '(Bacillus cereus)'),
    (('05', 'Mantenimiento Mensual', 'B7'), 'Ronda 1 M1: revisión de la freidora según el fabricante (termostato y '
     'límite de seguridad, válvula de vaciado, cestas y el filtrado incorporado o la máquina de filtrar); el aceite se '
     'cambia cuando lo diga el medidor de TPM (sin límite federal), no una vez al mes; el boil-out es semanal (hoja '
     '«Weekly Deep Clean»). Sin cifra de temperatura del kit'),
    (('05', 'Mantenimiento Mensual', 'B8'), 'Lavavajillas: filtros y niveles de químicos (la sal descalcificadora, solo '
     'si hay descalcificador)'),
    (('05', 'Mantenimiento Mensual', 'B17'), _A[('05', 'Mantenimiento Mensual', 'B21')]),
    # 06
    (('06', 'Noche Fútbol', 'A1'), 'Fútbol → fútbol americano (NFL y el universitario): «Game Night / Big Game — Peak '
     'Delivery»'),
    (('06', 'Lanzamiento Marca', 'B8'), 'Crear el perfil de la marca en cada app; ' + _PERMISO),
    (('06', 'Lanzamiento Marca', 'B9'), _ALERGENOS_APP + '; y, si un plato lleva pescado crudo o poco hecho (poke, '
     'sushi), el aviso al consumidor en su ficha (FDA Food Code 3-603.11)'),
    # 08 (la apertura y el cierre reordenados van por POR_CELDA)
    (('08', 'Instrucciones', 'B11'), 'Añade al final (ronda 1 m17): en una cocina compartida (una unidad de un cloud kitchen park o una commissary), marca N/A lo que lleva el '
     'operador del edificio (alarma, climatización, baños, zonas comunes, sala de repartidores) y quédate con las tareas '
     'de tu unidad'),
    (('08', 'Apertura del Negocio', 'B8'), _A[('08', 'Apertura del Negocio', 'B8')] + '; añade: salidas de emergencia '
     'despejadas y señales de salida (exit signs) iluminadas'),
    (('08', 'Apertura del Negocio', 'B9'), 'Punto de recogida de riders → driver pickup (los repartidores de las apps); '
     'el cartel con el horario de cada marca'),
])
# 09 «Instrucciones» B6 (ronda 1 m16): para qué sirve la caja en una cocina solo delivery
ADAPTAR[('09', 'Instrucciones', 'B6')] = (_A[('09', 'Instrucciones', 'B6')] + '; añade al final: en una cocina solo '
                                          'delivery los pedidos de las apps vienen pagados y los liquida cada app (se '
                                          'cuadran contra el informe de pagos de cada app, 01 «Kitchen Closing», tarea '
                                          '#18); este fichero es para lo que se cobra en tu mostrador: recogida en '
                                          'persona, pedidos por teléfono o por la web propia pagados al recoger')
for _fila, (_mes, _evento, _antel, _dir) in CALENDARIO.items():
    if _dir:
        ADAPTAR[(HOJA_CAL[0], HOJA_CAL[1], 'C%d' % _fila)] = 'Evento EN: «%s». %s' % (_evento, _dir)
# aplicar_en.objetivo_ajuste / G3 (errata ES, como la pizzería y la hamburguesería): las tareas largas del ES no
# llevan ajuste de texto y salen cortadas por la celda vecina; la EN activa el ajuste también donde el ES no cabía
AJUSTE_MAQUETA_ES = True
# aplicar_en.capa_ajuste (gancho de la hamburguesería; F2 real): 05 «FIFO Semanal» fila 34 (la última de la tabla de
# congelación) ya va cortada en el ES (dos líneas en 24.5 pt; el EN necesita 27.2) → 27.5. El título del 05 NO necesita
# alto propio: aquí el ES cabe en una línea y capa_ajuste ya lo sube a 50.5 como en los demás libros
ALTOS_FILA = {('05', 'FIFO Semanal', 34): 27.5}
# aplicar_en.capa_ajuste (gancho nuevo, F2 real): 01 «Cierre Cocina» B9 ya va cortada en el ES (sin ajuste) y su EN cita
# «05-cloud-kitchen-cleaning-checklist-inventory-maintenance.xlsx», más largo que la columna B: se activa el ajuste
AJUSTE_FORZADO = frozenset({('01', 'Cierre Cocina', 'B9')})
# Celdas ES con °C cuya EN NO lleva cifra en °F: el aceite (manipularlo «por debajo de 40 °C» → según el fabricante)
CELSIUS_SIN_F = frozenset({('01', 'Cierre Cocina', 'B13'), ('03', 'Handover Turno', 'B12'),
                           ('05', 'FIFO Semanal', 'B14'), ('05', 'Mantenimiento Mensual', 'B7')})

# ==========================================================================
# REGLAS_US: las del base + las de la ghost kitchen (fuente única de las cifras y normas que el kit puede afirmar)
# ==========================================================================
REGLAS_US = OrderedDict(_base.REGLAS_US)
REGLAS_US.update([
    ('coccion', ('aves 165 °F al instante; carne picada 155 °F durante 17 s; pescado 145 °F durante 15 s',
                 'FDA Food Code 2022 §3-401.11(A)')),
    ('crudo_separado', ('carne y pescado crudos separados de lo listo para consumir', 'FDA Food Code 2022 §3-302.11')),
    ('descongelar', ('descongelar en refrigeración a 41 °F o menos', 'FDA Food Code 2022 §3-501.13')),
    ('tphc', ('time as a public health control: procedimiento escrito; hora marcada; servir o descartar DENTRO de las 4 h',
              'FDA Food Code 2022 §3-501.19(B)')),
    ('arroz_sushi', ('acidificar el arroz para tenerlo fuera de frío exige varianza y plan HACCP',
                     'FDA Food Code 2022 §3-502.11(D)')),
    ('parasitos_proveedor', ('la declaración escrita del proveedor sustituye al registro propio',
                             'FDA Food Code 2022 §3-402.12(B)')),
    ('pase', ('lo caliente a 135 °F o más y lo frío a 41 °F o menos hasta la recogida; caliente y frío separados en el '
              'empaquetado', 'FDA Food Code 2022 §3-501.16; [criterio del kit] empaquetado')),
    ('precintos', ('cierre a prueba de manipulación de la comida lista para consumir que recoge un repartidor de app',
                   'California AB 3336 (2020, en vigor desde el 1-ene-2021); [local] resto de ciudades y estados')),
    ('alergenos_app', ('EE. UU.: sin norma federal para la comida de restaurante; UK: en la venta a distancia, antes '
                       'de comprar y al entregar', 'FALCPA 2004 + FASTER Act 2021; Food Information Regulations 2014 '
                       '(UK) y guía de la FSA')),
    ('permisos', ('un permiso sanitario por cocina; las marcas virtuales, según la ciudad; DBA según el estado',
                  '[local] departamento de salud; [estatal] registro de nombre comercial')),
    ('comisiones', ('comisiones de las apps según el plan; topes en Nueva York (15 % + 5 %) y San Francisco (15 %)',
                    '[local] NYC Local Law 2021; ordenanza de San Francisco')),
    ('sales_tax', ('quién cobra el sales tax de los pedidos por app depende del estado',
                   '[estatal] marketplace facilitator laws')),
    ('make_line', ('inserts de la mesa fría a 41 °F o menos; vegetales cortados TCS con date marking',
                   'FDA Food Code 2022 §3-501.16(A)(2) y §3-501.17')),
    ('plazos_kit', ('proteínas frescas 3 días; salsas caseras 5 días; vegetales cortados 2 días; fruta cortada 24 h; '
                    '8-12 min por pedido; aceptar en menos de 30 s', '[criterio del kit]')),
    ('aceite', ('filtrado según el fabricante de la freidora; cambio cuando lo diga el medidor de TPM (sin límite '
                'federal); boil-out semanal según el fabricante', '[fabricante] manual de la freidora y del medidor')),
    ('utensilios_4h', ('utensilios en uso con TCS: lavar, enjuagar y desinfectar cada 4 h como mínimo',
                       'FDA Food Code 2022 §4-602.11(C)')),
    ('estacionalidad', ('el delivery baja con el calor y en las vacaciones de verano; sube con frío y mal tiempo',
                        'DoorDash, Form 10-K FY2025 (Seasonality)')),
    ('dias_fuertes', ('Super Bowl, March Madness, Cinco de Mayo, 4 de julio, temporada de fútbol americano, Halloween, '
                      'Thanksgiving + Black Friday, días de frío y lluvia', '[criterio del kit] calendario del '
                      'delivery US')),
    ('inventario', ('mínimos de kg → lb (×2,2) redondeados a formato de compra; L → qt (1 qt ≈ 0,95 L); 0,5 L → 1 pt',
                    '[criterio del kit] conversión')),
])
# °F que el kit puede afirmar (G7): las del base + 32 (calibración) + la cocción (145, 155)
GRADOS_F_SPEC = {-31, -4, 0, 32, 41, 70, 100, 135, 145, 155, 165}

# ==========================================================================
# Pistas y dependencias de la ghost kitchen (extraer_textos.py)
# ==========================================================================
PISTAS_CAMBIO = {r'Kit de Tareas': 'D2: «Ghost Kitchen Checklists Kit Pro»'}
PISTAS_FUERA = (r'Restaurante Casual',)
PISTAS_EXTRA = [
    (r'[Dd]ark [Kk]itchen', 'D2: la EN no lleva el sufijo de variante: quita «— Dark Kitchen»; dark kitchen → ghost '
                            'kitchen (o cloud kitchen / virtual kitchen / delivery-only kitchen; NUNCA «dark kitchen»)'),
    (r'[Mm]arcas?\b|[Mm]ulti-[Mm]arca', 'marca → brand (virtual brand); multi-marca → multi-brand'),
    (r'[Pp]lataformas?|[Tt]ablets?', 'plataformas → delivery apps (third-party delivery apps: DoorDash, Uber Eats, '
                                     'Grubhub); tablets → order tablets'),
    (r'Glovo|Just ?Eat|UberEats', 'Glovo / Just Eat → DoorDash / Grubhub (Uber Eats se queda, con espacio)'),
    (r'[Rr]iders?', 'rider → delivery driver (los repartidores de las apps); recogida de riders → driver pickup'),
    (r'[Ee]xpedici[oó]n|[Ee]stanter[ií]a', 'estantería de expedición → driver pickup shelf; expedición → pickup / '
                                           'dispatch'),
    (r'[Pp]recint|[Ss]ello de seguridad', 'precinto / sello de seguridad → tamper-evident seal (sticker)'),
    (r'[Ee]mpaquet|[Pp]ackaging|[Ee]nvases?', 'empaquetado → packing; empaquetador → packer; packaging → packaging; '
                                              'envases → containers (boxes, bowls, clamshells)'),
    (r'[Tt]iempos? de preparaci[oó]n|[Tt]iempos\b', 'tiempos de preparación → prep times (los que se publican en la '
                                                    'app); tiempos → ticket times'),
    (r'\b86s?\b', '86 → 86 (jerga US: «86 an item»)'),
    (r'[Pp]ausar', 'pausar una marca → pause the brand (in the app)'),
    (r'[Rr]atings?|[Rr]eseñas', 'ratings / reseñas → ratings and reviews'),
    (r'[Rr]eembolsos?|[Cc]ancelaci', 'reembolsos → refunds; cancelaciones → cancellations'),
    (r'[Ff]acturaci[oó]n', 'facturación → sales (o revenue); facturación de plataformas → app sales / payouts'),
    (r'[Cc]omanda|[Tt]ickets?', 'pantalla de comandas → KDS (kitchen display); comanda / ticket → ticket'),
    (r'[Bb]año mar[ií]a', 'baño maría → steam table / hot well'),
    (r'[Mm]ermas?', 'mermas → waste (waste log)'),
    (r'TPV|[Dd]atáfono', 'TPV / datáfono → POS / card terminal'),
    (r'[Cc]uadrar', 'cuadrar → reconcile / balance'),
    (r'[Ff]útbol', 'fútbol → (American) football: NFL Sundays, Monday Night Football, college football Saturdays'),
    (r'RRSS|redes', 'RRSS → social media'),
    (r'[Ll]ocal\b', 'el local → the kitchen / the site (nunca «venue» ni «restaurant» para el local)'),
    (r'[Tt]imbre|[Ii]nterfono', 'timbre / interfono → door bell / intercom'),
    (r'[Gg]estor de plataformas|[Gg]estor\b', 'gestor de plataformas → app manager (delivery apps and tablets); gestor '
                                              'autorizado → licensed hauler / recycler'),
    (r'[Pp]oke|[Ss]ushi|[Tt]artar|[Cc]eviche', 'poke, sushi, tartare, ceviche (sin tildes en EN)'),
]
DEPENDENCIAS_EXTRA = OrderedDict([
    ('variante', ('Sufijo de variante «Dark Kitchen»', r'— Dark Kitchen|· Dark Kitchen', 'D2: la EN no lleva sufijo')),
    ('plataformas', ('Plataformas de delivery españolas', r'Glovo|Just ?Eat|UberEats',
                     'D-GHO: DoorDash, Uber Eats, Grubhub')),
    ('alergenos_app', ('Alérgenos en la venta a distancia', r'venta a distancia|14 alérgenos',
                       'D-GHO: los 9 de EE. UU. (sin norma federal); UK, los 14, antes de comprar y al entregar')),
    ('precintos', ('Precintos de seguridad', r'[Pp]recint|[Ss]ello de seguridad', 'D-GHO: tamper-evident; California '
                   'AB 3336; el resto, norma local')),
    ('parasitos', ('Pescado crudo (anisakis)', r'ANISAKIS|anisakis|−20 °C|−35 °C', 'D-GHO: FDA 3-402.11 (−4 °F 7 días '
                   'o −31 °F + 15 h) y aviso al consumidor')),
    ('aceite', ('Aceite manipulado en frío', r'40 °C', 'D-GHO: según el fabricante (CELSIUS_SIN_F)')),
    ('comisiones', ('Comisiones de las plataformas', r'[Cc]omisiones', 'D-GHO: según el plan; topes locales')),
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
    for ok in ('delivery-only restaurant', 'virtual restaurant', 'commissary kitchen', 'prep table', 'barcode',
               'driver pickup shelf', 'delivery drivers', 'the restaurant'):
        if rx.search(ok):
            err.append('TERMINOS_PROHIBIDOS caza lo permitido (%r)' % ok)
    rx_ctx = re.compile(RX_CONTEXTO_PENDIENTE)
    for ok in ('virtual restaurant', 'delivery-only restaurant', 'delivery drivers', 'commissary kitchen'):
        if rx_ctx.search(ok):
            err.append('RX_CONTEXTO_PENDIENTE caza lo permitido (%r)' % ok)
    for k, v in list(GLOSARIO.items()) + list(POR_CELDA.items()) + list(CLAVES.items()):
        if k not in _base.GLOSARIO or k in _GLOSARIO_GHOST:
            if isinstance(v, str) and rx.search(v):
                err.append('texto EN fijado con un término prohibido: %r → %r' % (k, v))
    if CITA_AUTOTEST.strip('()').split()[-1] in ' '.join(f for _v, f in REGLAS_US.values()):
        err.append('CITA_AUTOTEST está en REGLAS_US: G7 no la cazaría')
    for k, v in POR_CELDA.items():
        if k[:2] == _AN and k[2].startswith('E') and not re.match(r'^\d{1,2}:\d{2} (AM|PM)$', v):
            err.append('POR_CELDA: hora fijada %r sin formato US: %r' % (k, v))
    for nombre, lista, filas in (('08 apertura', _APERTURA_08, range(11, 23)), ('08 cierre', _CIERRE_08, range(5, 20))):
        if sorted(o for o, *_r in lista) != list(filas):
            err.append('%s: las filas de origen no son una permutación de %d-%d' % (nombre, filas[0], filas[-1]))
    for nombre, lista, filas in (('01 tablets', _TABLETS_01, range(31, 38)), ('04 apps', _APPS_04, range(7, 11))):
        if sorted(t[1] for t in lista) != list(filas) or [t[0] for t in lista] != list(filas):
            err.append('%s: las filas de origen no son una permutación de %d-%d' % (nombre, filas[0], filas[-1]))
        for t in lista:
            if (t[0] == t[1]) != (t[2] is None):
                err.append('%s: la fila %d cambia de tarea sin EN fijado (o al revés)' % (nombre, t[0]))
    h01 = [POR_CELDA[_AC + ('E%d' % f,)] for f in range(31, 38)]
    if any(not re.match(r'^\d{1,2}:\d{2} (AM|PM)$', h) for h in h01) or h01 != sorted(h01, key=lambda h: (
            int(h.split(':')[0]) % 12 * 60 + int(h.split(':')[1][:2]))):
        err.append('01 tablets: horas fijadas sin formato US o fuera de orden: %r' % h01)
    horas = [POR_CELDA[_AN + ('E%d' % f,)] for f in range(11, 23)]
    minutos = [int(h.split(':')[0]) % 12 * 60 + int(h.split(':')[1][:2]) for h in horas]
    if minutos != sorted(minutos):
        err.append('08 apertura: las horas fijadas no van en orden: %r' % horas)
    for k in CELSIUS_SIN_F:
        if k in POR_CELDA and ('°' in POR_CELDA[k]):
            err.append('CELSIUS_SIN_F %r con temperatura en el EN fijado' % (k,))
        if k in ADAPTAR and '°F' in ADAPTAR[k]:
            err.append('CELSIUS_SIN_F %r con °F en el ADAPTAR' % (k,))
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
    factor = {('kg', 'lb'): 2.2046, ('L', 'qt'): 1, ('L', 'pt'): 2.113, ('uds', 'ea'): 1, ('sets', 'sets'): 1}
    for f, es, en in _MINIMOS:
        c = ('05', 'Inventario Diario', 'C%d' % f)
        u_es = tx.get(c)
        u_en = POR_CELDA.get(c) or GLOSARIO.get(u_es)
        x = factor.get((u_es, u_en))
        if x is None:
            err.append('VALORES_EN: unidad %s → %s sin factor en la fila %d' % (u_es, u_en, f))
        elif x == 1 and float(es) != en:
            err.append('VALORES_EN: fila %d en %s no cambia de cifra (%s → %s)' % (f, u_es, es, en))
        elif x != 1 and not (0.5 <= en / (float(es) * x) <= 1.6):   # 1.6: redondeo a formato de compra
            err.append('VALORES_EN: fila %d, %s %s → %s %s fuera de la conversión' % (f, es, u_es, en, u_en))
    # las filas reordenadas del 08: el ES tiene tarea en la fila de origen, la zona EN es la del glosario de la zona
    # ES de esa fila, y el responsable ES es el esperado (apertura: «Encargado» en todas; cierre: el de su fila salvo
    # los de _RESPONSABLE_CAMBIA)
    for nombre, hoja, lista, col_x in (('apertura', _AN, _APERTURA_08, None), ('cierre', _CN, _CIERRE_08, 'D')):
        for i, t in enumerate(lista):
            o = t[0]
            if (hoja[0], hoja[1], 'B%d' % o) not in tx:
                err.append('08 %s: B%d sin tarea en el ES' % (nombre, o))
            z_es = tx.get((hoja[0], hoja[1], 'C%d' % o))
            if GLOSARIO.get(z_es) != t[2]:
                err.append('08 %s: la zona de la fila %d (%r → %r) no es %r' % (nombre, o, z_es, GLOSARIO.get(z_es),
                                                                               t[2]))
            if col_x:
                r_es = tx.get((hoja[0], hoja[1], 'D%d' % o))
                if GLOSARIO.get(r_es) != t[3] and o not in _RESPONSABLE_CAMBIA:
                    err.append('08 cierre: el responsable de la fila %d (%r) no es %r' % (o, r_es, t[3]))
    for f in range(11, 23):
        if tx.get((_AN[0], _AN[1], 'D%d' % f)) != 'Encargado':
            err.append('08 apertura D%d: el ES no dice «Encargado»' % f)
    if not tx.get((_AN[0], _AN[1], 'B20'), '').startswith('Encender tablets'):
        err.append('08 apertura B20: el ES ya no enciende las tablets')
    if not tx.get((_CN[0], _CN[1], 'B18'), '').startswith('Desactivar las marcas'):
        err.append('08 cierre B18: el ES ya no desactiva las marcas')
    for hoja, lista in ((_AC, _TABLETS_01), (_GP, _APPS_04)):
        filas = [t[0] for t in lista]
        for col in ('C', 'D'):
            if len({tx.get((hoja[0], hoja[1], '%s%d' % (col, f))) for f in filas}) != 1:
                err.append('%s: la columna %s cambia entre las filas reordenadas' % (hoja[1], col))
        for t in lista:
            if (hoja[0], hoja[1], 'B%d' % t[1]) not in tx:
                err.append('%s: B%d sin tarea en el ES' % (hoja[1], t[1]))
    if not tx.get((_AC[0], _AC[1], 'B33'), '').startswith('Activar todas las marcas') or \
            not tx.get((_GP[0], _GP[1], 'B7'), '').startswith('Activar todas las marcas'):
        err.append('01 B33 / 04 B7: el ES ya no enciende las marcas ahí')
    # 07: sala y barra del ES
    for f in range(13, 18):
        if tx.get(('07', 'Por Área', 'C%d' % f)) != 'Sala':
            err.append('07 Por Área C%d: el ES no dice «Sala»' % f)
        if tx.get(('07', 'Por Perfil', 'D%d' % f)) != 'Jefe de Sala':
            err.append('07 Por Perfil D%d: el ES no dice «Jefe de Sala»' % f)
    for f in range(20, 25):
        if tx.get(('07', 'Por Área', 'C%d' % f)) != 'Barra':
            err.append('07 Por Área C%d: el ES no dice «Barra»' % f)
    for k in (('07', 'Por Área', 'A12'), ('07', 'Por Área', 'A19'), ('07', 'Por Perfil', 'A12')):
        if 'SALA' not in tx.get(k, '') and 'BARRA' not in tx.get(k, ''):
            err.append('POR_CELDA %r: el ES no es un bloque de sala o barra (%r)' % (k, tx.get(k)))
    # Trimestral: las filas fijadas existen en el ES
    for k in POR_CELDA:
        if k[:2] == _T and k[2][0] in 'AB' and k not in tx:
            err.append('POR_CELDA %r sin texto en el ES' % (k,))
    # CELSIUS_SIN_F: el ES de esas celdas trae °C
    for k in CELSIUS_SIN_F:
        if '°C' not in tx.get(k, ''):
            err.append('CELSIUS_SIN_F %r: el ES no trae °C' % (k,))
    for k in ADAPTAR:
        if k not in tx:
            err.append('ADAPTAR %r sin texto en el ES' % (k,))
    return err


def cruzar_base(p_ghost, p_base):
    """Lo heredado POR CELDA del base (POR_CELDA y ADAPTAR) tiene en la ghost kitchen el mismo texto ES que en el base;
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
    tb, tg = textos(p_base), textos(p_ghost)
    for nombre, claves in (('POR_CELDA', _HEREDA_POR_CELDA), ('ADAPTAR', _HEREDA_ADAPTAR)):
        for k in claves:
            if tg.get(k) != tb.get(k):
                err.append('%s heredado %r: el texto ES de la ghost kitchen %r ≠ base %r' % (nombre, k, tg.get(k),
                                                                                             tb.get(k)))
    equivalentes = [(('03', 'Mensual Manager', 'B11'), ('03', 'Mensual Manager', 'B16')),
                    (('01', 'Apertura Cocina', 'B7'), ('01', 'Apertura Cocina', 'B7')),
                    (('03', 'Diario Manager', 'B24'), ('03', 'Diario Manager', 'B35'))]
    for kc, kb in equivalentes:
        if tg.get(kc) != tb.get(kb):
            err.append('%r de la ghost kitchen no es la fila del base %r: %r ≠ %r' % (kc, kb, tg.get(kc), tb.get(kb)))
    # 01 B13 (gas) usa el ADAPTAR del base B14 (otra redacción del ES, la misma práctica US)
    if 'gas' not in tg.get(('01', 'Apertura Cocina', 'B13'), ''):
        err.append('01 Apertura Cocina B13: el ES ya no es la comprobación del gas')
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
    print('mapas_ghost.py: {} ficheros · {} pestañas · {} glosario · {} por celda · {} valores · {} adaptar · '
          '{} reglas · {} errores'.format(len(FICHEROS), len(HOJAS), len(GLOSARIO), len(POR_CELDA), len(VALORES_EN),
                                          len(ADAPTAR), len(REGLAS_US), len(e)))
    raise SystemExit(1 if e else 0)
