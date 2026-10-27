#!/usr/bin/env python3
"""
mapas_hotel.py — Hotel Checklists Kit Pro (EN) · DELTA del Kit de Tareas Hotel Completo (`kit-tareas-hotel`, 19 xlsx
v2.0, 636 tareas) sobre `mapas.py` (Restaurant Checklists Kit Pro). SPEC: `hotel/SPEC.md` (solo el delta). Décimo
hermano vertical. Sesión Claude Code, 27-oct-2026.

Molde (lo mide el censo): 19 libros, numeración 01-15, 18, 19 y 2 bonus (no hay 16 ni 17).
  · 01-15 y BONUS-01: molde LIGERO del catering y la heladería (# · Tarea · Zona · Responsable · ✓ · Hora · Notas;
    cabeceras internas por sección; contadores que restan «Tarea»; CF `$E6="✓"`; sin protección; subtítulo A2 en vez de
    la línea de marca D19; sin horas ni responsables precargados).
  · 18 y 19: el 08 y el 09 del kit base con la variante «Hotel Completo» (el 18 con 5 tareas de hotel más; el 19
    idéntico al 09 del base salvo la variante y las horas: su POR_CELDA y su ADAPTAR se heredan con la clave
    renumerada, lo comprueba cruzar_base).
  · BONUS-02: calendario propio (24 fechas, filas 5-28: A # · B fecha · C impacto · D preparación F&B · E antelación).

Se usa con `--kit hotel` (kit.py). Importa `mapas.py` y SOLO añade o sobrescribe: producto, 19 ficheros, títulos,
pestañas (74), glosario (zonas y puestos de hotel US), CLAVES (+ «Tarea»), CF_POR_CELDA (27 hojas con cabeceras
internas dentro del rango), caja del 19 (la del base), calendario US del BONUS-02, POR_CELDA (caja; 18 «Closing
Rounds» reordenado; 13 «Quarterly & Annual» de un hotel US; fichajes del 14), ADAPTAR y REGLAS_US (FDA Food Code 2022
en el F&B; MAHC 2024 en piscina y spa; ASHRAE 188 / CDC en legionela; OSHA, NFPA y códigos estatales en
mantenimiento; FLSA e I-9 en RR. HH.; regla de la FTC sobre tarifas en revenue). Las funciones del base que leen
constantes (titulo_interior, autotest, cruzar_censo) se re-enlazan a ESTE módulo. Ejecutado como script: autotest +
cruce con hotel/censo_es.json + cruce con el base (lo heredado por celda tiene el mismo texto ES).

    python3 hotel/mapas_hotel.py
"""
import os
import re
import sys
import types
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
import mapas as _base                                            # noqa: E402
from mapas import *                                              # noqa: E402,F401,F403
from mapas import _h12, _num, _celdas                            # noqa: E402,F401
AQUI = os.path.dirname(os.path.abspath(__file__))              # hotel/ (el import * trae el AQUI del base)

ORIGEN_ES = 'kit-tareas-hotel'
N_LIBROS = 19
PRODUCTO = 'Hotel Checklists Kit Pro'
# D2: H1 = title SEO (69 caracteres). «hotel housekeeping checklist» 260/mes US (la misma serie que «hotel room cleaning
# checklist» y «hotel cleaning checklist»), «hotel maintenance checklist» 70, «front desk checklist» 30
TITULO_SEO = 'Hotel Checklists Kit Pro: Housekeeping, Front Desk, F&B & Maintenance'
SLUG = 'hotel-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_HOTEL_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
PRECIO_USD = 29
# El 18 y el 19 traen la variante «Apertura y Cierre» en la línea de marca (glitch del generador ES) y «Hotel Completo»
# en los títulos A1; el 01-15 y los bonus, «Hotel Integral» en el subtítulo A2 (GLOSARIO)
MARCA_ES = '— Kit de Tareas Recurrentes · Apertura y Cierre · AI Chef Pro · aichef.pro'
MARCA_EN = '— ' + PRODUCTO + ' · AI Chef Pro · aichef.pro'
VARIANTES_ES = ('Hotel Completo', 'Hotel Integral')
# heredar.py: memoria con varias fuentes, en orden de preferencia. El BASE primero (el 18 y el 19 son su 08 y su 09);
# luego los del molde ligero (catering, heladería, chocolatería: instrucciones y pies comunes) y el resto.
_SUF = lambda v: [(' — Hotel Completo', ' — ' + v), (' · Hotel Completo', ' · ' + v)]  # noqa: E731
MEMORIA = [('base', '', _SUF('Restaurante Casual')), ('catering', 'catering', _SUF('Catering / Eventos')),
           ('icecream', 'icecream', _SUF('Heladería Artesanal')), ('chocolate', 'chocolate', _SUF('Chocolatería')),
           ('bar', 'bar', _SUF('Bar / Cocktails')), ('cafe', 'cafe', _SUF('Cafetería / Brunch')),
           ('pastry', 'pastry', _SUF('Pastelería / Obrador')), ('pizza', 'pizza', _SUF('Pizzería')),
           ('burger', 'burger', _SUF('Hamburguesería')), ('ghost', 'ghost', _SUF('Dark Kitchen'))]
# heredar.py: EN heredado que en un hotel no vale tal cual → pendientes (motivo «contexto»). El hotel tiene restaurante,
# bares y banquetes, pero lo heredado que dice «restaurant», «FOH», «host stand» o «shift manager» habla del local
# entero de otro kit: el traductor lo ve con su base_en y decide.
RX_CONTEXTO_PENDIENTE = (r'(?i)\b(?:restaurants?(?! consultant| supply)|FOH|host stands?|shift managers?|venues?|'
                         r'pizzas?|pizzerias?|burgers?|ghost kitchens?|packers?|app managers?|commissar(?:y|ies)|'
                         r'coffee shops?|cafes?|ice cream shops?|scoop shops?|dipping cabinets?|batch freezers?|'
                         r'scoopers?|pastry shops?|bakery cases?|chocolate shops?|food trucks?)\b')
NO_HEREDAR = {}
# gates_en.py G2: términos de otros kits que NINGUNA celda EN del hotel puede llevar. «restaurant», «bartender»,
# «server», «host stand», «banquet», «BEO», «line cook» y «coffee machine» son de hotel y quedan permitidos.
TERMINOS_PROHIBIDOS = (r'(?i:\b(?:pizzas?|pizzerias?|burgers?|ghost kitchens?|packers?|app managers?|commissar(?:y|ies)|'
                       r'coffee shops?|ice cream shops?|scoop shops?|dipping cabinets?|batch freezers?|scoopers?|'
                       r'pastry shops?|bakery cases?|chocolate shops?|food trucks?)\b)|\bFOH\b')
TERMINO_PROHIBIDO_EJEMPLO = 'Ask the scooper to restock the dipping cabinet before the pizza delivery.'
REFERENCIAS_TRADUCTOR = ['hotel/SPEC.md', 'SPEC.md §0-§3 y §7.2 (brief)', 'textos_en/glosario.json (glosario de la '
                         'prosa del kit base)', 'hotel/textos_en/heredado.json (cómo se dijo ya cada cosa: base, '
                         'catering, heladería, chocolatería y el resto)', 'hotel/mapas_hotel.py: GLOSARIO, HOJAS, '
                         'FICHEROS, TITULOS, POR_CELDA, REGLAS_US', '../GLOSARIO-JERGA-ES-EN.md (secciones Checklists y '
                         'Hotel)']
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v2.0'),
    ('keywords', 'hotel housekeeping checklist, hotel room cleaning checklist, hotel maintenance checklist, hotel front '
                 'desk checklist, night audit checklist, hotel checklist template, AI Chef Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

# ==========================================================================
# Ficheros (D5: intención US, DataForSEO 27-oct-2026; SPEC §R)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-fb-buffet-desayuno.xlsx', '01-hotel-breakfast-buffet-checklists.xlsx'),
    ('02-fb-buffet-comida-cena.xlsx', '02-hotel-lunch-dinner-buffet-checklists.xlsx'),
    ('03-fb-restaurante-carte.xlsx', '03-hotel-restaurant-opening-closing-checklists.xlsx'),
    ('04-fb-outlets.xlsx', '04-hotel-bar-grab-and-go-checklists.xlsx'),
    ('05-fb-room-service-minibar.xlsx', '05-in-room-dining-minibar-checklists.xlsx'),
    ('06-fb-banquetes-eventos.xlsx', '06-hotel-banquet-event-checklist.xlsx'),
    ('07-recepcion-turnos.xlsx', '07-hotel-front-desk-checklists-night-audit.xlsx'),
    ('08-guest-services.xlsx', '08-concierge-guest-experience-checklists.xlsx'),
    ('09-housekeeping.xlsx', '09-hotel-housekeeping-checklists.xlsx'),
    ('10-areas-publicas.xlsx', '10-hotel-public-area-cleaning-checklists.xlsx'),
    ('11-piscina.xlsx', '11-hotel-pool-checklists.xlsx'),
    ('12-terraza.xlsx', '12-hotel-patio-terrace-checklists.xlsx'),
    ('13-mantenimiento.xlsx', '13-hotel-preventive-maintenance-checklists.xlsx'),
    ('14-administracion.xlsx', '14-hotel-back-office-checklists.xlsx'),
    ('15-spa-wellness.xlsx', '15-hotel-spa-checklists.xlsx'),
    ('18-apertura-cierre-negocio.xlsx', '18-hotel-daily-opening-closing-rounds.xlsx'),
    ('19-apertura-cierre-caja.xlsx', '19-cash-drawer-opening-closing.xlsx'),
    ('BONUS-01-briefing-servicio.xlsx', 'BONUS-01-hotel-daily-fb-briefing-template.xlsx'),
    ('BONUS-02-calendario-anual-tareas.xlsx', 'BONUS-02-hotel-fb-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)
TITULOS = OrderedDict([
    ('01-hotel-breakfast-buffet-checklists.xlsx', 'Hotel Breakfast Buffet Checklists: Setup, Service & Closing'),
    ('02-hotel-lunch-dinner-buffet-checklists.xlsx', 'Hotel Lunch & Dinner Buffet Checklists'),
    ('03-hotel-restaurant-opening-closing-checklists.xlsx',
     'Hotel Restaurant Opening & Closing Checklists (À la Carte)'),
    ('04-hotel-bar-grab-and-go-checklists.xlsx',
     'Hotel Bar & Outlet Checklists: Pool Bar, Lobby Bar & Grab-and-Go'),
    ('05-in-room-dining-minibar-checklists.xlsx', 'In-Room Dining (Room Service) & Minibar Checklists'),
    ('06-hotel-banquet-event-checklist.xlsx', 'Hotel Banquet & Event Checklist: From BEO to Breakdown'),
    ('07-hotel-front-desk-checklists-night-audit.xlsx',
     'Hotel Front Desk Checklists: AM, PM & Night Audit Shifts, Check-In & Check-Out'),
    ('08-concierge-guest-experience-checklists.xlsx', 'Concierge & Guest Experience Checklists'),
    ('09-hotel-housekeeping-checklists.xlsx',
     'Hotel Housekeeping Checklists: Checkout & Stayover Room Cleaning, Turndown, Deep Cleaning & Linen'),
    ('10-hotel-public-area-cleaning-checklists.xlsx',
     'Hotel Public Area Cleaning Checklists: Lobby, Corridors & Elevators, Restrooms & Parking'),
    ('11-hotel-pool-checklists.xlsx',
     'Hotel Pool Checklists: Daily Opening & Closing, Weekly Maintenance & Towel Service'),
    ('12-hotel-patio-terrace-checklists.xlsx', 'Hotel Patio & Terrace Checklists: Seasonal Setup & Daily Service'),
    ('13-hotel-preventive-maintenance-checklists.xlsx',
     'Hotel Preventive Maintenance Checklists: Daily Rounds to Annual, HVAC, Plumbing & Electrical'),
    ('14-hotel-back-office-checklists.xlsx',
     'Hotel Back-Office Checklists: Revenue Management, Reservations, Accounting & HR'),
    ('15-hotel-spa-checklists.xlsx',
     'Hotel Spa & Wellness Checklists: Opening, Closing, Treatment Rooms & Locker Rooms'),
    ('18-hotel-daily-opening-closing-rounds.xlsx',
     'Hotel Daily Opening & Closing Rounds: F&B Outlets & Public Areas'),
    ('19-cash-drawer-opening-closing.xlsx', 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log'),
    ('BONUS-01-hotel-daily-fb-briefing-template.xlsx', 'BONUS: Hotel Daily F&B Briefing Template (Stand-Up Notes)'),
    ('BONUS-02-hotel-fb-calendar.xlsx', 'BONUS: Hotel F&B Calendar: 24 Key Dates & Seasons (US)'),
])
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

HOJAS = OrderedDict(_base.HOJAS)
HOJAS.update([
    ('Apertura Desayuno', 'Breakfast Opening'), ('Cierre Desayuno', 'Breakfast Closing'),
    ('Buffet Almuerzo', 'Lunch Buffet'), ('Buffet Cena', 'Dinner Buffet'),
    ('Apertura À la Carte', 'Restaurant Opening'), ('Cierre À la Carte', 'Restaurant Closing'),
    ('Pool Bar', 'Pool Bar'), ('Lobby Bar - Lounge', 'Lobby Bar & Lounge'),
    ('Snack Bar - Grab Go', 'Snack Bar & Grab-and-Go'),
    ('Room Service', 'In-Room Dining'), ('Minibar', 'Minibar'),
    ('Banquetes y Eventos', 'Banquets & Events'),
    ('Turno Mañana', 'AM Shift'), ('Turno Tarde', 'PM Shift'), ('Turno Noche', 'Night Audit Shift'),
    ('Check-in Check-out', 'Check-In & Check-Out'),
    ('Conserjería', 'Concierge'), ('Guest Experience', 'Guest Experience'),
    ('Limpieza Checkout', 'Checkout Room Cleaning'), ('Limpieza Estancia', 'Stayover Room Cleaning'),
    ('Turndown Service', 'Turndown Service'), ('Deep Cleaning', 'Deep Cleaning'), ('Control Lencería', 'Linen Control'),
    ('Lobby', 'Lobby'), ('Pasillos y Ascensores', 'Corridors & Elevators'), ('Baños Públicos', 'Public Restrooms'),
    ('Parking', 'Parking'),
    ('Apertura Piscina', 'Pool Opening'), ('Cierre Piscina', 'Pool Closing'),
    ('Mant. Semanal', 'Weekly Pool Maintenance'), ('Servicio Toallas', 'Towel Service'),
    ('Montaje Temporada', 'Seasonal Setup'), ('Servicio Diario', 'Daily Service'),
    ('Ronda Diaria', 'Daily Rounds'), ('Semanal', 'Weekly PM'), ('Mensual', 'Monthly PM'),
    ('HVAC', 'HVAC'), ('Fontanería', 'Plumbing'), ('Electricidad', 'Electrical'),
    ('Revenue Management', 'Revenue Management'), ('Reservas', 'Reservations'), ('Contabilidad', 'Accounting'),
    ('RRHH Operativo', 'HR Operations'),
    ('Apertura Spa', 'Spa Opening'), ('Cierre Spa', 'Spa Closing'), ('Cabinas Tratamientos', 'Treatment Rooms'),
    ('Vestuarios', 'Locker Rooms'),
    # 18: el hotel no cierra (recepción 24 h): son las rondas de apertura y cierre de los outlets y las zonas públicas
    ('Apertura del Negocio', 'Opening Rounds'), ('Cierre del Negocio', 'Closing Rounds'),
    ('Briefing', 'Daily F&B Briefing'), ('Calendario', 'F&B Calendar'),
])
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Apertura Desayuno', 'Cierre Desayuno']),
    ('02', ['Instrucciones', 'Buffet Almuerzo', 'Buffet Cena']),
    ('03', ['Instrucciones', 'Apertura À la Carte', 'Cierre À la Carte']),
    ('04', ['Instrucciones', 'Pool Bar', 'Lobby Bar - Lounge', 'Snack Bar - Grab Go']),
    ('05', ['Instrucciones', 'Room Service', 'Minibar']),
    ('06', ['Instrucciones', 'Banquetes y Eventos']),
    ('07', ['Instrucciones', 'Turno Mañana', 'Turno Tarde', 'Turno Noche', 'Check-in Check-out']),
    ('08', ['Instrucciones', 'Conserjería', 'Guest Experience']),
    ('09', ['Instrucciones', 'Limpieza Checkout', 'Limpieza Estancia', 'Turndown Service', 'Deep Cleaning',
            'Control Lencería']),
    ('10', ['Instrucciones', 'Lobby', 'Pasillos y Ascensores', 'Baños Públicos', 'Parking']),
    ('11', ['Instrucciones', 'Apertura Piscina', 'Cierre Piscina', 'Mant. Semanal', 'Servicio Toallas']),
    ('12', ['Instrucciones', 'Montaje Temporada', 'Servicio Diario']),
    ('13', ['Instrucciones', 'Ronda Diaria', 'Semanal', 'Mensual', 'Trimestral y Anual', 'HVAC', 'Fontanería',
            'Electricidad']),
    ('14', ['Instrucciones', 'Revenue Management', 'Reservas', 'Contabilidad', 'RRHH Operativo']),
    ('15', ['Instrucciones', 'Apertura Spa', 'Cierre Spa', 'Cabinas Tratamientos', 'Vestuarios']),
    ('18', ['Instrucciones', 'Apertura del Negocio', 'Cierre del Negocio']),
    ('19', ['Instrucciones', 'Apertura de Caja', 'Cierre de Caja', 'Registro Mensual']),
    ('B01', ['Instrucciones', 'Briefing']),
    ('B02', ['Instrucciones', 'Calendario']),
])

# ==========================================================================
# GLOSARIO: el base entero (opcional) + celdas cortas de un hotel US. Departamentos US: front desk, housekeeping,
# engineering (mantenimiento), in-room dining, banquets; puesto de guardia: manager on duty (MOD).
# ==========================================================================
GLOSARIO = OrderedDict(_base.GLOSARIO)
_GLOSARIO_HOTEL = OrderedDict([
    # subtítulo de marca (A2) del molde ligero: el producto EN, igual en todo el kit (como el catering y la heladería)
    ('AI Chef Pro · aichef.pro — Kit de Tareas: Hotel Integral', 'AI Chef Pro · aichef.pro — ' + PRODUCTO),
    ('Hora', 'Time'), ('Semestral', 'Semiannual'), ('Cada 2 años', 'Every 2 years'),
    # zonas (columna C); 6 sobrescriben el base: Admin (Office), Recepción (Host stand), Sala (FOH), Zonas comunes
    # (Common areas) y, en los puestos, Encargado (Shift manager)
    ('Admin', 'Admin'), ('Recepción', 'Front desk'), ('Sala', 'Dining room'), ('Zonas comunes', 'Public areas'),
    ('Housekeeping', 'Housekeeping'), ('Mantenimiento', 'Engineering'), ('Buffet', 'Buffet'), ('Piscina', 'Pool'),
    ('Room Service', 'In-room dining'), ('Banquetes', 'Banquets'), ('Spa', 'Spa'), ('Pool Bar', 'Pool bar'),
    ('À la Carte', 'Restaurant'), ('Conserjería', 'Concierge'), ('Minibar', 'Minibar'), ('Guest Exp.', 'Guest exp.'),
    ('Lencería', 'Linen room'), ('Snack Bar', 'Snack bar'), ('Vestuarios', 'Locker rooms'), ('Lobby Bar', 'Lobby bar'),
    ('Lobby', 'Lobby'), ('Pasillos', 'Corridors'), ('Parking', 'Parking'), ('Fontanería', 'Plumbing'),
    ('Electricidad', 'Electrical'), ('Revenue', 'Revenue'), ('Reservas', 'Reservations'),
    ('Contabilidad', 'Accounting'), ('RRHH', 'HR'), ('HVAC', 'HVAC'), ('Seguridad', 'Security'),
    # puestos (18 y 19)
    ('Encargado', 'Manager on duty'),
    # tabla de vida útil en congelación del 01 «Cierre Desayuno» (Familia / Vida útil y las 4 cadencias del base ya están)
    ('6-12 meses', '6–12 months'), ('3-6 meses', '3–6 months'), ('1-2 meses', '1–2 months'),
    ('No congelar', 'Do not freeze'),
    # cabeceras del BONUS-02
    ('Fecha / Período', 'Date / Period'), ('Impacto', 'Impact'), ('Preparación F&B', 'F&B Prep'),
])
GLOSARIO.update(_GLOSARIO_HOTEL)
GLOSARIO_OPCIONAL = frozenset(_base.GLOSARIO)
PUESTOS_ES = frozenset(_base.PUESTOS_ES | {
    'Housekeeping', 'Mantenimiento', 'Buffet', 'Piscina', 'Room Service', 'Banquetes', 'Spa', 'Pool Bar', 'À la Carte',
    'Conserjería', 'Minibar', 'Guest Exp.', 'Lencería', 'Snack Bar', 'Vestuarios', 'Lobby Bar', 'Lobby', 'Pasillos',
    'Parking', 'Fontanería', 'Electricidad', 'Revenue', 'Reservas', 'Contabilidad', 'RRHH', 'HVAC', 'Seguridad'})

# ==========================================================================
# CLAVES: «Tarea» (los contadores del molde ligero restan las cabeceras internas, como el catering y la heladería)
# ==========================================================================
CLAVES = OrderedDict(_base.CLAVES)
CLAVES.update([('Tarea', 'Task')])

# ==========================================================================
# CF_POR_CELDA (desviación DECLARADA respecto del ES, la del catering ronda 1 M5 y la heladería D7): en las 27 hojas
# cuyo rango de CF contiene una cabecera interna («Tarea» en B, «✓» en E), la CF de «hecho» la pintaba de verde. La EN
# excluye esas filas. Las otras 22 hojas del molde ligero (solo la cabecera de la fila 5, fuera del rango) no cambian.
# ==========================================================================
_CF_HOJAS = [('01', 'Apertura Desayuno', 'A6:G62'), ('01', 'Cierre Desayuno', 'A6:G29'),
             ('02', 'Buffet Almuerzo', 'A6:G32'), ('02', 'Buffet Cena', 'A6:G22'),
             ('03', 'Apertura À la Carte', 'A6:G23'), ('03', 'Cierre À la Carte', 'A6:G21'),
             ('04', 'Pool Bar', 'A6:G28'), ('04', 'Lobby Bar - Lounge', 'A6:G19'), ('04', 'Snack Bar - Grab Go', 'A6:G19'),
             ('05', 'Room Service', 'A6:G40'), ('05', 'Minibar', 'A6:G20'), ('06', 'Banquetes y Eventos', 'A6:G50'),
             ('07', 'Turno Mañana', 'A6:G20'), ('07', 'Turno Tarde', 'A6:G20'), ('07', 'Turno Noche', 'A6:G19'),
             ('07', 'Check-in Check-out', 'A6:G21'), ('08', 'Conserjería', 'A6:G20'), ('08', 'Guest Experience', 'A6:G19'),
             ('09', 'Limpieza Checkout', 'A6:G27'), ('09', 'Limpieza Estancia', 'A6:G17'),
             ('09', 'Control Lencería', 'A6:G19'), ('11', 'Apertura Piscina', 'A6:G16'), ('12', 'Servicio Diario', 'A6:G18'),
             ('13', 'Trimestral y Anual', 'A6:G36'), ('15', 'Apertura Spa', 'A6:G16'), ('15', 'Cierre Spa', 'A6:G16'),
             ('B01', 'Briefing', 'A6:G35')]
CF_POR_CELDA = OrderedDict(((c, h, sq), ('$E6="✓"', 'AND($E6="✓",$B6<>"%s")' % CLAVES['Tarea']))
                           for c, h, sq in _CF_HOJAS)
# G3: libros cuyo ES no trae la línea de marca D19 (el molde ligero y el calendario: subtítulo A2)
LIBROS_SIN_MARCA = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', 'B01',
                    'B02')

# ==========================================================================
# Caja (D12): el 19 es el 09 del base (mismas filas 27-42, mismo resumen): sus denominaciones, fórmulas y rótulos US
# con la clave renumerada. gates_en.py lee el libro de la caja de HOJA_CAJA[0] (código común, F1 del hotel).
# ==========================================================================
HOJA_CAJA = ('19', 'Cierre de Caja')
DENOMINACIONES = list(_base.DENOMINACIONES)
VALORES_DENOMINACION_EN = sorted({d[4] for d in DENOMINACIONES})
FORMULAS_POR_CELDA = OrderedDict(
    ((HOJA_CAJA[0], HOJA_CAJA[1], 'C%d' % f), ('=B%d*%s' % (f, _num(xes)), '=B%d*%s' % (f, _num(xen))))
    for f, _es, xes, _en, xen in DENOMINACIONES)
_R = lambda k: ('19',) + k[1:] if k[0] == '09' else k            # noqa: E731  clave del 09 del base → 19

# ==========================================================================
# BONUS-02 «F&B Calendar»: 24 filas (5-28) en orden cronológico y las anuales al final, como el ES. B (fecha), C
# (impacto) y E (antelación) fijados; D (preparación F&B) = traductor con ADAPTAR. Sin Reyes, Semana Santa, Día del
# Padre en marzo, comuniones, caza, puentes ni Nochebuena con turrón. fila → (fecha EN, impacto EN, antelación EN, ADAPTAR)
# ==========================================================================
HOJA_CAL = ('B02', 'Calendario')
FILAS_CALENDARIO = range(5, 29)
CALENDARIO = OrderedDict([
    (5, ("Jan 1 — New Year's Day", 'Brunch & late checkout', '3 weeks',
         'Sustituye a Reyes. Brunch de Año Nuevo y salidas tardías (late checkout) tras Nochevieja: buffet de brunch '
         'ampliado y horario de desayuno alargado')),
    (6, ("Feb 14 — Valentine's Day", 'Themed dinner', '4 weeks',
         'Menú para parejas, decoración y paquetes de cena + alojamiento; amenity romántico en la habitación')),
    (7, ("Mar 17 — St. Patrick's Day", 'Bar event', '3 weeks',
         'Sustituye a Semana Santa en esta fila. Evento en el lobby bar y el pool bar: especiales verdes y de cerveza; '
         'comprobar la edad (21+) de todo el que pida alcohol')),
    (8, ('Mar–Apr — Spring break & Easter (varies)', 'High occupancy', '6 weeks',
         'Lo de Semana Santa del ES: familias y spring break; brunch de Pascua (Easter brunch), refuerzo de personal y '
         'buffet ampliado')),
    (9, ('April — Shoulder season', 'Groups & conferences', '2 months',
         'Paquetes de coffee break y almuerzos de trabajo para grupos y congresos (MICE)')),
    (10, ('Apr–Jun — Proms, graduations & showers', 'Banquet peak', '3 months',
          'Sustituye a las comuniones: proms, graduaciones y baby/bridal showers; menús cerrados de adultos e '
          'infantil, salón y photo booth; sin alcohol para menores (21+); se contratan con 3-6 meses')),
    (11, ("2nd Sunday of May — Mother's Day", 'Brunch peak', '6 weeks',
          'Sustituye al Día del Padre de marzo (en EE. UU. va en junio): es el día de más brunch del año: brunch '
          'especial, reservas ampliadas y detalle para las madres')),
    (12, ('May–Oct — Wedding season', 'Banquet peak', '6–12 months',
          'Lo de «Bodas (inicio)» del ES: personal extra de banquetes reservado y proveedores de boda confirmados; '
          'las bodas se contratan con 6-12 meses')),
    (13, ('Memorial Day (last Monday of May) — Summer starts', 'Max occupancy', '3 months',
          'Lo de «Junio — Temporada alta» del ES: buffet con horario ampliado, más show cooking y el pool bar a pleno')),
    (14, ('Jun–Aug — Summer peak (incl. Jul 4)', 'Resort & pool season', '3 months',
          "Lo de «Verano pleno» del ES: carta fresca, helados, BBQ y el pool bar; Father's Day (3.er domingo de junio) y "
          'el 4 de julio (fuegos artificiales, BBQ y pedidos de grupo); sin «chiringuito»')),
    (15, ('September — Labor Day & conference season', 'Corporate peak', '2 months',
          'Lo de «Vuelta congresos» del ES: Labor Day (1.er lunes de septiembre) cierra el verano; kick-offs y '
          'convenciones: paquetes de banquetes')),
    (16, ('October — Fall menus', 'Special menu', '4 weeks',
          'Sustituye a la temporada de caza: carta y buffet de otoño (calabaza, manzana, setas y caza solo de un '
          'proveedor aprobado)')),
    (17, ('Oct 31 — Halloween', 'Themed event', '4 weeks', None)),
    (18, ('Nov — Thanksgiving (4th Thursday)', 'High occupancy', '6 weeks',
          'Sustituye al puente de Todos los Santos: buffet o menú prix fixe de Thanksgiving (pavo), turnos cerrados '
          'antes y paquetes de fin de semana largo')),
    (19, ('Nov — Black Friday & Cyber Monday', 'Promotion', '4 weeks',
          'Lo de «Black Friday gastro» del ES: paquetes de cena + alojamiento, brunch dominical y tarjetas regalo (gift '
          'cards)')),
    (20, ('Dec 1–20 — Holiday parties', 'Banquet peak', '3 months',
          'Sustituye al puente de la Constitución y a las cenas de empresa: la mayor demanda de banquetes corporativos '
          '(holiday parties) del año; personal extra cerrado antes')),
    (21, ('Dec 24 — Christmas Eve', 'Special dinner', '2 months',
          'Menú premium de Nochebuena con reserva anticipada; sin turrón')),
    (22, ('Dec 25 — Christmas Day', 'Family brunch', '2 months',
          'Buffet o brunch de Navidad ampliado (prime rib, jamón glaseado, postres de temporada); sin turrones')),
    (23, ("Dec 31 — New Year's Eve", 'Gala night', '3 months',
          'Sin cotillón ni uvas: cena de gala, party favors (gorros, matasuegras), barra libre (open bar) con '
          'comprobación de edad 21+ y brindis con champán a medianoche; personal al máximo')),
    (24, ('Year-round — Sunday brunch', 'Fixed outlet', 'Weekly',
          'Brunch premium con champán y mimosas, huevos benedict y show cooking')),
    (25, ('Year-round — VIP amenities', 'In-room dining', 'Monthly stock',
          'Welcome drinks, cestas de fruta y chocolate del turndown; el alcohol solo para huéspedes de 21+')),
    (26, ('Year-round — Groups & conferences (MICE)', 'Banquets', '1–3 months',
          'Coffee breaks, almuerzos de trabajo y cenas de gala, cada uno con su BEO')),
    (27, ('Local events & holidays', 'Varies', '4–6 weeks',
          'Sustituye a los festivos locales españoles: eventos de tu ciudad (ferias, partidos, convenciones del '
          'centro de congresos, festivales); añade la nota UK: bank holidays, Mothering Sunday y Boxing Day')),
    (28, ('Health inspection', 'Unannounced', 'Always',
          'Sustituye a «Inspección sanidad — documentación APPCC»: la inspección del departamento de salud llega sin '
          'avisar: registros de temperatura, food handler cards, certified food protection manager y, si tu estado '
          'o una varianza lo exige, el plan HACCP')),
])

# ==========================================================================
# POR_CELDA: lo heredado del base (el 09 entero → 19; mismo texto ES, lo comprueba cruzar_base) + lo del hotel
# ==========================================================================
_HEREDA_POR_CELDA = [k for k in _base.POR_CELDA if k[0] == '09']
POR_CELDA = OrderedDict((_R(k), _base.POR_CELDA[k]) for k in _HEREDA_POR_CELDA)
# 14 · RRHH: conservación de fichajes (B16 del 03 del base: mismo EN, FLSA)
POR_CELDA[('14', 'RRHH Operativo', 'B12')] = _base.POR_CELDA[('03', 'Mensual Manager', 'B16')]

# 13 · Trimestral y Anual: servicios contratados y papeles de un hotel US (sin DDD, BIE, OCA, RITE, RD 487/2022 ni
# Verifactu). (fila → B, F); F = None si la cadencia del ES se queda (glosario)
_T13 = ('13', 'Trimestral y Anual')
_SERVICIOS_13 = OrderedDict([
    (6, ('Pest control by a licensed pest management company: kitchens, storerooms, public areas and a rotating sample '
         'of guest rooms for bed bugs — service visit and signed service report on file', 'Monthly')),
    (7, ('Kitchen hood and duct cleaning by a certified contractor at the NFPA 96 frequency for your cooking volume '
         '(quarterly if high volume, semiannual if moderate): service report on file', 'Semiannual')),
    (8, ('Optional third-party food safety audit or ATP swab testing to verify your cleaning (many brands require an '
         'annual audit)', None)),
    (9, ('Review your food safety plan (HACCP if your health department or a variance requires one) and supplier '
         'approvals: the menu and buffet changes of the year', None)),
    (10, ('Renew food handler cards and allergen training for all F&B staff, banquet extras included, and check a '
          'certified food protection manager is on the F&B management team (FDA Food Code 2-102.12; card rules vary '
          'by state)', None)),
    (11, ('Calibrate the thermometers and probes of walk-ins, buffet and in-room dining in ice water (32 °F) and log '
          'any offset', None)),
    (14, ('Cooling towers and domestic hot water: cleaning and disinfection under your Legionella water management '
          'program (ASHRAE 188); cooling towers registered, inspected and tested where your state or city requires '
          'it (New York State and New York City do)', None)),
    (15, ('Legionella sampling by an accredited lab at the frequency your water management program sets; results '
          'logged and corrective actions recorded', None)),
    (16, ('Hot water temperature at outlets: stored at 140 °F or above and circulating at 120 °F or above (CDC); '
          'thermostatic mixing valves keep the guest outlets scald-safe; flush the outlets of rooms out of order or '
          'out of service for a week or more', None)),
    (17, ('Pool and spa water: lab or health-department testing where your state code requires it, on top of the '
          'free chlorine and pH log (MAHC 2024: before opening and every 2 or 4 hours)', None)),
    (18, ('Drain, deep-clean and inspect pool and spa shells, filters and showers; check every drain cover is '
          'VGB-compliant and within its service life (15 U.S.C. 8003)', None)),
    (21, ('Fire sprinkler, standpipe and fire alarm inspections by a licensed fire protection company at the NFPA 25 '
          'and NFPA 72 intervals (quarterly and annual items): tags and reports on file', None)),
    (22, ('Annual extinguisher maintenance by a licensed fire protection company: new tag and record (OSHA '
          '1910.157(e)(3)); hydrostatic tests as each extinguisher label says', 'Annual')),
    (23, ('Gas lines and kitchen appliance connections checked by a licensed pro, as often as your local code or gas '
          'utility requires', 'Annual')),
    (24, ('Electrical maintenance program (NFPA 70B): infrared scan of main panels and switchgear by a qualified '
          'electrician', 'Annual')),
    (25, ('Elevator and dumbwaiter inspection by a licensed elevator inspector, as your state or city requires '
          '(certificate posted in each car), on top of the monthly maintenance contract', 'Annual')),
    (26, ('Boilers and water heaters: inspection for the state boiler certificate where your state requires one; '
          'chiller and HVAC plant service with its report', None)),
    (27, ('Evacuation drill with every shift, as often as your local fire code requires, and review of the emergency '
          'action plan', None)),
    (28, ('Used cooking oil pickup by a licensed recycler and hazardous waste (lamps, batteries, chemicals) by a '
          'licensed hauler: keep receipts and manifests', None)),
    (31, ("Review insurance: general liability, property, liquor liability, workers' comp and pool and spa coverage — "
          'insured values, capacities and covered activities', None)),
    (32, ("File the quarter's time records (FLSA: time cards 2 years, payroll 3) and check every new hire has a Form "
          'I-9, seasonal and banquet extras included', None)),
    (33, ('PMS and POS review: software updates, user permissions, sales and occupancy tax rates, and PCI DSS for card '
          'data', None)),
    (34, ('Renew permits and licenses: business license, health permit for each food outlet, liquor license, pool and '
          'spa operating permit and, if you have one, outdoor dining permit', None)),
])
for _f, (_b, _cad) in _SERVICIOS_13.items():
    POR_CELDA[_T13 + ('B%d' % _f,)] = _b
    if _cad:
        POR_CELDA[_T13 + ('F%d' % _f,)] = _cad

# 18 · Cierre (errata ES y contexto de hotel): en el ES, «Verificar check-outs pendientes» y «Apagar iluminación de zonas
# nobles» van DESPUÉS de activar la alarma y cerrar con llave, y las persianas se cierran antes de recoger la
# señalización. Un hotel no cierra: el 18 cierra los outlets de F&B y deja las zonas públicas en modo noche. Mismas 15
# filas (E = «Close»): el outlet → patio y señalización → caja → papeleras → recepción y zonas públicas → el local →
# persiana, alarma y llave al final.
_CN = ('18', 'Cierre del Negocio')
_CIERRE_18 = [  # fila ES de origen, EN, zona EN, responsable EN
    (5, 'Turn off background music in the outlet', 'General', 'Manager on duty'),
    (6, 'Check no guests are left in the outlet', 'Dining room', 'Manager on duty'),
    (7, 'Clean up and bring in the patio, if you have one', 'Patio', 'Manager on duty'),
    (12, 'Bring in the outdoor signage and menu boards', 'Outside', 'Manager on duty'),
    (8, 'Turn off the outlet POS / card terminal (or leave on standby)', 'Register', 'Manager on duty'),
    (14, 'Empty trash cans in public areas and restrooms', 'Restrooms', 'Manager on duty'),
    (18, "Review pending check-outs and tomorrow's departures with the night auditor", 'Front desk', 'Manager on duty'),
    (19, 'Lobby and public-area lighting to night mode (exit signs and egress lighting always stay on)', 'Public areas',
     'Manager on duty'),
    (13, 'Check that the outlet windows are closed', 'General', 'Manager on duty'),
    (11, 'Turn off HVAC in the closed outlets (guest floors and lobby stay on)', 'General', 'Manager on duty'),
    (10, 'Turn off the outlet lights (leave security lighting on)', 'General', 'Manager on duty'),
    (15, 'Final safety check of the outlets: gas, water, small appliances unplugged', 'General', 'Manager on duty'),
    (9, "Close the outlet's security gate and doors", 'Entrance', 'Last one out'),
    (16, 'Arm the outlet alarm, if it has one', 'Entrance', 'Last one out'),
    (17, 'Lock up and verify it is locked', 'Entrance', 'Last one out'),
]
# responsables que cambian (declarado): check-outs y zonas públicas (ES «Último en salir») → el MOD; persiana y alarma
# (ES «Encargado») → el último en salir, con la llave
_RESPONSABLE_CAMBIA = frozenset({18, 19, 9, 16})
for _fila, (_o, _b, _c, _d) in enumerate(_CIERRE_18, 5):
    for _col, _v in (('B', _b), ('C', _c), ('D', _d)):
        POR_CELDA[_CN + ('%s%d' % (_col, _fila),)] = _v

for _fila, (_fecha, _impacto, _antel, _dir) in CALENDARIO.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'B%d' % _fila)] = _fecha
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'C%d' % _fila)] = _impacto
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'E%d' % _fila)] = _antel
for _f, _es, _xes, _en, _xen in DENOMINACIONES:
    POR_CELDA[(HOJA_CAJA[0], HOJA_CAJA[1], 'A%d' % _f)] = _en
VALORES_EN = OrderedDict()             # sin inventario con mínimos en el ES hotel (nada numérico cambia)

# ==========================================================================
# ADAPTAR (en español, con el dato US; las cifras y normas salen de REGLAS_US)
# ==========================================================================
_A = _base.ADAPTAR
_HACCP_KIT = _base._HACCP_KIT
_TEMP_FRIO = _base._TEMP_FRIO
_LAVADO = _A[('02', 'Fríos', 'B6')]
_LOG = 'coletilla «— log reading: ____ °F»'
_TIRA = 'sanitizante aprobado a la concentración de la etiqueta, medida con tira (test strip) (FDA Food Code 4-501.114)'
_CALIENTE_FRIO = ('FDA Food Code 3-501.16: caliente a 135 °F o más y frío a 41 °F o menos (ES 65 °C / 5 °C); ' + _LOG)
_PARASITOS = ('Pescado crudo o marinado (salmón curado o ahumado en frío, tartar, ceviche, carpaccio): destrucción de '
              'parásitos de la FDA Food Code 3-402.11: congelado a −4 °F o menos 7 días, o a −31 °F hasta sólido y 15 h '
              'a −31 °F, o a −31 °F hasta sólido y 24 h a −4 °F; carta o registro del proveedor guardado 90 días '
              '(3-402.12). Sin «anisakis», «−20 °C 24 h» ni Reglamento (CE) 853/2004')
_ALERGENOS = ('Alérgenos US: los 9 principales (FALCPA + FASTER Act: leche, huevo, pescado, crustáceos, frutos de '
              'cáscara, cacahuete, trigo, soja y sésamo); en UK, los 14. Sin «14 obligatorios»')
_RESENAS = 'Plataformas US: Google, TripAdvisor y Expedia (Booking.com si tu clientela es internacional)'
_SALA = 'Temperatura de sala US: 68–72 °F (ES 20-22 °C)'
_BUFFET = ('Buffet de autoservicio US: protector (sneeze guard) o vitrina (FDA Food Code 3-306.11), utensilio de '
           'servicio en cada fuente, plato limpio en cada vuelta (3-304.16) y un empleado formado vigilando el buffet '
           '(3-306.13)')
_FICHAJE = _A[('03', 'Diario Manager', 'B35')]
_PISCINA_QUIMICA = ('MAHC 2024 (código modelo de los CDC; manda el código estatal o local): cloro libre mínimo 1.0 ppm '
                    '(2.0 ppm con ácido cianúrico / estabilizante) y pH 7.0–7.8; medir antes de abrir y cada 2 h con '
                    'dosificación manual o cada 4 h con automática; registro guardado 3 años y a disposición del '
                    'inspector. Sin «libro obligatorio» ni «comunidad autónoma»')
_ESPECIFICO_ESTADO = 'normativa de piscinas del estado o del condado (state / county pool code)'
_MAHC_CARTEL = ('Cartel US si no hay socorrista: «No Lifeguard on Duty» y que los menores de 14 años necesitan la '
                'supervisión directa de un adulto de 18 o más, con el horario (MAHC 2024 §6.4.2.2.3.4); profundidades '
                'y normas visibles')
_LEGIONELA = ('Legionela US: programa de gestión del agua (water management program) según ASHRAE 188 y la guía de '
              'los CDC; agua caliente almacenada a 140 °F o más y en circulación a 120 °F o más (CDC); válvulas '
              'termostáticas en los puntos de uso contra quemaduras. Sin RD 487/2022 ni «> 50 °C»')
_SPA_TEMP = ('Spa / hot tub US: nunca por encima de 104 °F (MAHC 2024 §5.7.4.7.2); el ES dice 35-38 °C = 95–100 °F: '
             'deja ese rango como objetivo del kit y el máximo de 104 °F; cartel obligatorio del hot tub (104 °F, '
             'sin niños menores de 5, sin alcohol, embarazo y problemas cardiacos)')
_OSHA_SANGRE = ('Añade: agujas, sangre o fluidos solo con guantes y el kit de bloodborne pathogens; las agujas al '
                'contenedor de objetos punzantes (sharps), nunca con la mano (OSHA 29 CFR 1910.1030)')
ADAPTAR = OrderedDict([
    # 01 · Instrucciones
    (('01', 'Instrucciones', 'B11'), 'Categoría del hotel → «economy, midscale, upscale or luxury» (en EE. UU. no hay '
     'estrellas oficiales)'),
    (('01', 'Instrucciones', 'B12'), 'A4 → US Letter; «sala de desayunos» → breakfast room'),
    (('01', 'Instrucciones', 'B16'), _PARASITOS),
    (('01', 'Instrucciones', 'B17'), 'La tabla del pie de «Cierre Desayuno» está a 0 °F (ES −18 °C)'),
    # 01 · Apertura Desayuno
    (('01', 'Apertura Desayuno', 'B7'), _A[('01', 'Apertura Cocina', 'B7')]),
    (('01', 'Apertura Desayuno', 'B9'), _A[('01', 'Apertura Cocina', 'B9')]),
    (('01', 'Apertura Desayuno', 'B10'), _A[('01', 'Apertura Cocina', 'B10')]),
    (('01', 'Apertura Desayuno', 'B11'), _TEMP_FRIO + '; «cámaras» = walk-in cooler y walk-in freezer'),
    (('01', 'Apertura Desayuno', 'B13'), _A[('01', 'Apertura Cocina', 'B14')] + '; avisa a engineering'),
    (('01', 'Apertura Desayuno', 'B26'), _CALIENTE_FRIO),
    (('01', 'Apertura Desayuno', 'B31'), _BUFFET),
    (('01', 'Apertura Desayuno', 'B33'), _PARASITOS + '; si lo curas en casa, congélalo tú antes y guarda el registro'),
    (('01', 'Apertura Desayuno', 'B38'), 'Rótulo con el nombre del plato y sus alérgenos: ' + _ALERGENOS),
    (('01', 'Apertura Desayuno', 'B41'), _SALA),
    (('01', 'Apertura Desayuno', 'B51'), 'Peticiones especiales: sin gluten, vegano y alergias (los 9 de EE. UU.)'),
    (('01', 'Apertura Desayuno', 'B60'), 'Limpiar y luego sanitizar con ' + _TIRA),
    # 01 · Cierre Desayuno
    (('01', 'Cierre Desayuno', 'B7'), 'Lo que estuvo expuesto en la línea del buffet (al alcance del cliente o fuera de '
     'temperatura) no se reutiliza [criterio del kit]; lo que no salió a la línea y se guarda caliente se enfría de '
     '135 °F a 70 °F en 2 h y a 41 °F en 4 h más (FDA Food Code 3-501.14)'),
    (('01', 'Cierre Desayuno', 'B8'), 'Etiqueta con nombre, fecha y hora, tapado a 41 °F o menos; date marking: 7 días '
     'contando el de preparación (FDA Food Code 3-501.17)'),
    (('01', 'Cierre Desayuno', 'B17'), 'Limpiar y luego sanitizar con ' + _TIRA),
    (('01', 'Cierre Desayuno', 'A33'), 'Título de la tabla en °F: «at 0 °F» (ES −18 °C); mismas MAYÚSCULAS'),
    (('01', 'Cierre Desayuno', 'D37'), 'La destrucción de parásitos (FDA Food Code 3-402.11: −4 °F 7 días, o −31 °F) '
     'no sustituye a esta vida útil: se cuentan por separado'),
    # 02
    (('02', 'Instrucciones', 'B7'), 'Tipos de hotel US: resort, hotel urbano (full-service o select-service) y '
     'all-inclusive'),
    (('02', 'Instrucciones', 'B14'), _PARASITOS + '; en un buffet de autoservicio el riesgo se multiplica por el número '
     'de comensales'),
    (('02', 'Instrucciones', 'B15'), _LAVADO),
    (('02', 'Buffet Almuerzo', 'B7'), _LAVADO),
    (('02', 'Buffet Almuerzo', 'B9'), _PARASITOS),
    (('02', 'Buffet Almuerzo', 'B14'), 'Rótulo con nombre y alérgenos: ' + _ALERGENOS),
    (('02', 'Buffet Almuerzo', 'B16'), _CALIENTE_FRIO + '; ' + _HACCP_KIT),
    (('02', 'Buffet Cena', 'B8'), _PARASITOS),
    # 03
    (('03', 'Instrucciones', 'B7'), 'Restaurante del hotel US: signature restaurant, steakhouse o grill, o temático'),
    (('03', 'Apertura À la Carte', 'B7'), 'Alergias por escrito a cocina y al server de cada mesa: ' + _ALERGENOS),
    (('03', 'Apertura À la Carte', 'B18'), _SALA + ' y ventilación'),
    (('03', 'Apertura À la Carte', 'B19'), _TEMP_FRIO),
    # 04
    (('04', 'Instrucciones', 'B11'), 'Categoría del hotel → «upscale, luxury or resort» (en EE. UU. no hay estrellas '
     'oficiales)'),
    (('04', 'Pool Bar', 'B11'), 'Pulseras / toallas → wristbands del all-inclusive o del pool access; aforo según el '
     'permiso de la piscina'),
    (('04', 'Pool Bar', 'B17'), 'Añade: alcohol solo a mayores de 21 (comprobar ID) y sin servir a quien ya está '
     'ebrio (ley estatal de alcohol y dram shop)'),
    (('04', 'Pool Bar', 'B18'), 'Añade: en la zona de piscina NADA de vidrio: vasos y platos irrompibles (MAHC 2024 '
     '§5.6.9.2)'),
    (('04', 'Pool Bar', 'B25'), 'Cristalería → vasos y menaje: en la zona de piscina no hay vidrio (MAHC 2024 '
     '§5.6.9.2)'),
    (('04', 'Pool Bar', 'B27'), 'Perecedero tapado, etiquetado y a 41 °F o menos (FDA Food Code 3-501.16); los licores '
     'no necesitan frío: al almacén cerrado con llave'),
    (('04', 'Snack Bar - Grab Go', 'B7'), 'Vitrina refrigerada a 41 °F o menos (FDA Food Code 3-501.16); ' + _LOG),
    (('04', 'Snack Bar - Grab Go', 'B10'), 'FIFO y date marking: 7 días contando el de preparación (FDA Food Code '
     '3-501.17); lo envasado en el hotel para autoservicio lleva etiqueta con ingredientes y alérgenos (3-602.11)'),
    (('04', 'Snack Bar - Grab Go', 'B19'), 'Temperaturas de cierre en °F; ' + _LOG + '; ' + _HACCP_KIT),
    # 05
    (('05', 'Room Service', 'B16'), 'Pedido: habitación, número de comensales, alergias (los 9 de EE. UU.) y hora; '
     'alcohol solo a mayores de 21 (comprobar ID en la entrega)'),
    (('05', 'Minibar', 'B6'), 'Añade: el alcohol del minibar solo para huéspedes de 21+ (ley estatal)'),
    # 06
    (('06', 'Instrucciones', 'B14'), 'Al confirmar la reserva todo va al BEO (banquet event order): alergias por '
     'escrito con nombre y mesa, número garantizado (guarantee), precio por persona y qué incluye, cancelación y aforo '
     'del salón (fire marshal capacity)'),
    (('06', 'Banquetes y Eventos', 'B6'), 'Alergias e intolerancias por escrito con nombre y mesa, en el BEO: ' +
     _ALERGENOS),
    # 07
    (('07', 'Instrucciones', 'B10'), 'PMS habituales en EE. UU.: Oracle OPERA Cloud, Mews, Cloudbeds, etc.'),
    (('07', 'Instrucciones', 'B11'), 'Estándares de marca (brand standards) de tu cadena o franquicia'),
    (('07', 'Turno Mañana', 'B10'), 'Caja del turno: starting bank, cambio y card terminal operativo'),
    (('07', 'Turno Tarde', 'B15'), 'Walk-ins y overbooking: si no hay habitación, «walk the guest» según la política '
     '(hotel cercano pagado, transporte y llamada)'),
    (('07', 'Turno Noche', 'B8'), 'Informes: ocupación, ADR, RevPAR y revenue por departamento'),
    (('07', 'Check-in Check-out', 'B7'), 'Documento de identidad con foto y tarjeta de crédito para incidentales '
     '(incidentals hold); sin parte de viajeros'),
    (('07', 'Check-in Check-out', 'B20'), _RESENAS),
    # 08
    (('08', 'Instrucciones', 'B7'), 'Hoteles 4-5* → hoteles upscale y de lujo (en EE. UU. no hay estrellas oficiales)'),
    (('08', 'Guest Experience', 'B9'), _RESENAS + ' (responder a todas)'),
    # 09
    (('09', 'Instrucciones', 'B7'), 'Camarera de pisos → room attendant'),
    (('09', 'Instrucciones', 'B10'), 'Categoría del hotel → «midscale, upscale or luxury» (en EE. UU. no hay estrellas '
     'oficiales)'),
    (('09', 'Limpieza Checkout', 'B6'), 'Llamar y anunciarse («Housekeeping!») antes de entrar; añade: lleva el botón '
     'de pánico (panic button) si tu ciudad o estado lo exige (Chicago, Seattle, New Jersey…) y la puerta abierta '
     'mientras limpias'),
    (('09', 'Limpieza Checkout', 'B7'), 'Añade: al quitar la ropa de cama, revisa costuras del colchón y del somier '
     'por chinches (bed bugs) y avisa a tu supervisor si ves algo'),
    (('09', 'Limpieza Checkout', 'B9'), _OSHA_SANGRE),
    (('09', 'Limpieza Checkout', 'B14'), 'Limpiar y luego desinfectar con el producto registrado en la EPA, respetando '
     'su tiempo de contacto (etiqueta) y su ficha SDS (OSHA HazCom)'),
    (('09', 'Limpieza Estancia', 'B7'), 'Cartel «Do Not Disturb» (DND): respetarlo y avisar al supervisor para la '
     'comprobación de bienestar (welfare check) que marque la política del hotel o de la marca'),
    (('09', 'Turndown Service', 'B13'), 'Temperatura nocturna estándar US: 68–72 °F (ES 20-22 °C)'),
    (('09', 'Control Lencería', 'B8'), 'Albarán → ticket de entrega con el conteo (linen count sheet) para la '
     'lavandería exterior'),
    (('09', 'Control Lencería', 'B16'), 'Par de lencería: 3 juegos por cama (par 3: uno en la habitación, uno en la '
     'lavandería y uno en el office de planta) [criterio del kit]'),
    # 10
    (('10', 'Lobby', 'B12'), 'Ceniceros exteriores solo donde tu ciudad o estado permita fumar (suele exigirse una '
     'distancia a la puerta)'),
    (('10', 'Baños Públicos', 'B10'), 'Contenedores de higiene femenina → sanitary napkin receptacles; ' + _OSHA_SANGRE),
    (('10', 'Parking', 'B10'), 'Extintores: inspección visual mensual (OSHA 1910.157(e)(2)); señalización de salida '
     '(exit signs) iluminada'),
    # 11 · piscina
    (('11', 'Instrucciones', 'B6'), 'Control de químicos, seguridad y cumplimiento: MAHC 2024 y el ' + _ESPECIFICO_ESTADO),
    (('11', 'Instrucciones', 'B7'), _PISCINA_QUIMICA),
    (('11', 'Instrucciones', 'B10'), 'Comunidad autónoma → «your state or county pool code»: el MAHC es un código '
     'modelo; muchos estados exigen un operador cualificado (p. ej. Texas acepta el curso CPO)'),
    (('11', 'Apertura Piscina', 'B6'), _PISCINA_QUIMICA + '; ' + 'con la lectura «— FC: ____ ppm · pH: ____»'),
    (('11', 'Apertura Piscina', 'B14'), _MAHC_CARTEL),
    (('11', 'Apertura Piscina', 'B15'), 'Material de rescate US: aro salvavidas (ring buoy) con cuerda, pértiga '
     '(reaching pole), botiquín y teléfono de emergencia operativos'),
    (('11', 'Cierre Piscina', 'B8'), 'Segunda lectura de cloro libre y pH en el registro de la piscina (pool log); '
     'cada 2 o 4 h según la dosificación (MAHC 2024 §5.7.5)'),
    (('11', 'Cierre Piscina', 'B12'), 'Cerrar el acceso: puerta de autocierre y pestillo (self-closing, self-latching '
     'gate) según el código de tu estado'),
    (('11', 'Mant. Semanal', 'B8'), 'Productos químicos: almacenados aparte, etiquetados, con su ficha SDS y el EPP a '
     'mano (OSHA HazCom 29 CFR 1910.1200); alcalinidad total semanal (MAHC 2024 §5.7.5)'),
    (('11', 'Mant. Semanal', 'B9'), 'Añade: tapas de los sumideros (drain covers) enteras, atornilladas y dentro de su '
     'vida útil: Virginia Graeme Baker Act (15 U.S.C. 8003)'),
    (('11', 'Mant. Semanal', 'B12'), 'Libro de mantenimiento obligatorio → el registro de la piscina (pool log): se '
     'guarda 3 años (MAHC 2024 §6.4.1.2.1)'),
    # 12
    (('12', 'Servicio Diario', 'B8'), 'Ceniceros solo si tu ciudad o estado permite fumar en el patio (muchos lo '
     'prohíben): dilo así'),
    (('12', 'Montaje Temporada', 'B8'), 'Montaje según el plano aprobado y, si la ciudad lo pide, el permiso de '
     'outdoor dining / sidewalk café'),
    # 13
    (('13', 'Instrucciones', 'B14'), 'Describe la lista US de la hoja «Quarterly & Annual»: control de plagas, campanas '
     '(NFPA 96), plan de seguridad alimentaria y formación, calibración, legionela (ASHRAE 188) y torres de '
     'refrigeración, agua de piscina y spa, rociadores y alarma de incendios (NFPA 25 y 72), extintores (OSHA), gas, '
     'electricidad (NFPA 70B), ascensores y calderas (inspector estatal o municipal), simulacro, residuos, seguros, '
     'I-9 y fichajes, PMS / POS y permisos. Sin DDD, BIE, OCA, RITE, RD 487/2022 ni Verifactu'),
    (('13', 'Ronda Diaria', 'B6'), 'Calderas y agua caliente sanitaria (domestic hot water): 140 °F o más en el '
     'acumulador (CDC)'),
    (('13', 'Ronda Diaria', 'B8'), 'Grupo electrógeno → emergency generator'),
    (('13', 'Semanal', 'B7'), 'Extintores (inspección visual, OSHA 1910.157(e)(2): mensual como mínimo) y armarios de '
     'manguera / standpipes: precintos, manómetro en verde y acceso libre. Sin «BIEs»'),
    (('13', 'Semanal', 'B12'), 'Alumbrado de emergencia: prueba funcional de 30 s cada mes y de 90 min al año, con '
     'registro (NFPA 101 §7.9.3)'),
    (('13', 'Mensual', 'B10'), 'Puertas cortafuegos (fire doors): cierre automático, retenedores magnéticos y '
     'señalización; la inspección periódica de las puertas, por un profesional (NFPA 80)'),
    (('13', 'Mensual', 'B11'), 'Prueba mensual del grupo electrógeno (emergency generator) bajo carga, como digan el '
     'fabricante y tu código de incendios; sin «obligatorio» genérico'),
    (('13', 'HVAC', 'B7'), 'El personal no toca el refrigerante: solo un técnico certificado EPA 608 (40 CFR Part 82); '
     'el equipo comprueba presiones y alarmas y avisa'),
    (('13', 'Fontanería', 'B7'), _LEGIONELA),
    (('13', 'Fontanería', 'B11'), 'Añade: la grifería de habitaciones sin uso se purga cada semana (legionela, CDC)'),
    # 14
    (('14', 'Instrucciones', 'B13'), 'Registro de jornada → «Time records:»'),
    (('14', 'Instrucciones', 'B14'), 'US: la FLSA obliga a registrar las horas del personal por horas (non-exempt); '
     'fichajes 2 años y nóminas 3 (29 CFR 516.5-516.6; algunos estados piden más, p. ej. NY 6), y el I-9 de cada '
     'contratación. En «HR Operations» se aprueban a diario y se archivan al cerrar el mes. Sin RD-ley 8/2019 ni '
     '«Inspección de Trabajo»'),
    (('14', 'Revenue Management', 'B7'), 'Paridad de tarifas en las OTAs (Expedia, Booking.com) y el canal directo; '
     'añade: el precio anunciado incluye las tarifas obligatorias (resort fee) desde el primer momento: regla de la '
     'FTC sobre tarifas (16 CFR Part 464, desde el 12-may-2025)'),
    (('14', 'Revenue Management', 'B9'), 'Restricciones: estancia mínima (MLOS), CTA y CTD'),
    (('14', 'Contabilidad', 'B9'), 'Conciliar los cobros con el lote (batch) del procesador de tarjetas (Visa, '
     'Mastercard, Amex)'),
    (('14', 'Contabilidad', 'B12'), 'Remesas bancarias → depósitos bancarios (bank deposits)'),
    (('14', 'RRHH Operativo', 'B7'), _FICHAJE + '; extras de banquete y turno de noche incluidos; sin «registro de '
     'jornada» español'),
    (('14', 'RRHH Operativo', 'B11'), 'Incidencias de nómina US: horas extra (overtime de la FLSA por encima de 40 h '
     'semanales), propinas y bonus'),
    # 15
    (('15', 'Instrucciones', 'B6'), 'Hot tub (whirlpool spa), sauna y baño de vapor (steam room); la piscina '
     'climatizada interior'),
    (('15', 'Apertura Spa', 'B6'), _SPA_TEMP + '; añade: cloro libre del hot tub 3.0 ppm como mínimo (MAHC 2024)'),
    (('15', 'Cierre Spa', 'B9'), 'Limpiar y luego desinfectar con el producto registrado en la EPA, respetando su '
     'tiempo de contacto'),
    (('15', 'Cabinas Tratamientos', 'B7'), 'Desinfectar con el producto registrado en la EPA, respetando su tiempo de '
     'contacto (etiqueta)'),
    (('15', 'Cabinas Tratamientos', 'B10'), 'Temperatura de cabina US: 75–79 °F (ES 24-26 °C)'),
    # 18 (el cierre reordenado va por POR_CELDA)
    (('18', 'Instrucciones', 'B6'), 'El hotel no cierra (recepción 24 h): este es el checklist de los OUTLETS de F&B y '
     'las zonas públicas que abren y cierran cada día; úsalo como marco del día'),
    (('18', 'Apertura del Negocio', 'B5'), 'Desactivar la alarma del outlet (restaurante o bar) si la tiene: el hotel '
     'sigue abierto'),
    (('18', 'Apertura del Negocio', 'B8'), _A[('08', 'Apertura del Negocio', 'B8')] + ' del outlet'),
    (('18', 'Apertura del Negocio', 'B11'), 'Sistema de reservas del restaurante (OpenTable, Resy…) y tablet de pedidos'),
    (('18', 'Apertura del Negocio', 'B13'), 'Reservas del día y eventos especiales (BEOs del día)'),
    (('18', 'Apertura del Negocio', 'B17'), 'Terraza → patio (mesas, sillas, sombrillas o patio heaters)'),
    # BONUS-01
    (('B01', 'Instrucciones', 'B7'), 'Reparte a los jefes de departamento → department heads (F&B, front desk, '
     'housekeeping, engineering)'),
    (('B01', 'Briefing', 'B16'), 'Alergias críticas (los 9 de EE. UU.): habitación, tipo y protocolo'),
])
# 19 (= 09 del base): el ADAPTAR del base, tal cual, con la clave renumerada
_HEREDA_ADAPTAR = [k for k in _A if k[0] == '09']
for _k in _HEREDA_ADAPTAR:
    ADAPTAR[_R(_k)] = _A[_k]
for _fila, (_fecha, _impacto, _antel, _dir) in CALENDARIO.items():
    ADAPTAR[(HOJA_CAL[0], HOJA_CAL[1], 'D%d' % _fila)] = 'Fecha EN: «%s».%s' % (_fecha, ' ' + _dir if _dir else '')
# aplicar_en.objetivo_ajuste / G3: la EN activa el ajuste también donde el ES no cabía (como los hermanos)
AJUSTE_MAQUETA_ES = True
CELSIUS_SIN_F = frozenset()

# ==========================================================================
# REGLAS_US: las del base que aplican + las del hotel (fuente única de las cifras y normas que el kit puede afirmar)
# ==========================================================================
REGLAS_US = OrderedDict(_base.REGLAS_US)
# Fuera: recalentado y aviso al consumidor (el ES hotel no tiene esas tareas); el resto del base aplica al F&B del hotel
for _k in ('recalentado',):
    del REGLAS_US[_k]
REGLAS_US.update([
    ('buffet', ('sneeze guard o vitrina; plato limpio en cada vuelta; buffet vigilado por personal formado; lo expuesto '
                'no se reutiliza [criterio del kit]', 'FDA Food Code 2022 §3-306.11, §3-304.16, §3-306.13')),
    ('etiqueta_envasado', ('lo envasado en el hotel para autoservicio lleva etiqueta con alérgenos',
                           'FDA Food Code 2022 §3-602.11')),
    ('cfpm', ('certified food protection manager; food handler cards según el estado', 'FDA Food Code 2022 §2-102.12; '
                                                                                      '[estatal]')),
    ('piscina_quimica', ('cloro libre ≥ 1.0 ppm (2.0 con CYA); spa ≥ 3.0 ppm; pH 7.0–7.8; medir antes de abrir y cada '
                         '2 h (manual) o 4 h (automático); registros 3 años',
                         'CDC MAHC 2024 (5.ª ed.) §5.7.3.1.1.2, §5.7.3.4.1, §5.7.5, §6.4.1.2.1; [estatal] código de '
                         'piscinas')),
    ('piscina_operador', ('operador cualificado (curso reconocido; p. ej. CPO en Texas)',
                          'MAHC 2024 §6.1; 25 TAC Ch. 265 (Texas)')),
    ('piscina_heces', ('heces formadas o vómito: 2 ppm 25 min, pH ≤ 7.5, agua ≥ 77 °F; diarrea: 20 ppm 12,75 h',
                       'MAHC 2024 §6.5.3; CDC Fecal Incident Response')),
    ('piscina_vidrio', ('sin envases de vidrio en la zona de bañistas', 'MAHC 2024 §5.6.9.2')),
    ('piscina_cartel', ('«No Lifeguard on Duty» + menores de 14 con adulto de 18+', 'MAHC 2024 §6.4.2.2.3.4')),
    ('vgb', ('tapas de sumidero antiatrapamiento (ASME A112.19.8)', '15 U.S.C. 8003 (Virginia Graeme Baker Pool and '
                                                                    'Spa Safety Act)')),
    ('hazcom', ('productos químicos con etiqueta, SDS y formación', '29 CFR 1910.1200')),
    ('spa_temp', ('hot tub ≤ 104 °F; cartel del spa; objetivo del kit 95–100 °F (ES 35-38 °C)',
                  'MAHC 2024 §5.7.4.7.2 y §6.4.2.2.3.7; [criterio del kit]')),
    ('legionela', ('programa de gestión del agua; agua caliente almacenada ≥ 140 °F y en circulación ≥ 120 °F; purgar '
                   'las salidas sin uso; torres de refrigeración registradas donde se exija',
                   'ASHRAE 188; CDC Legionella toolkit (potable water module); NYC Local Law 77 (2015); 10 NYCRR '
                   'Part 4')),
    ('incendios', ('rociadores y standpipes según NFPA 25; alarma según NFPA 72; puertas cortafuegos NFPA 80; '
                   'alumbrado de emergencia 30 s/mes y 90 min/año', 'NFPA 25; NFPA 72; NFPA 80; NFPA 101 §7.9.3')),
    ('generador', ('prueba mensual bajo carga del generador de emergencia', '[fabricante] [local] código de incendios')),
    ('electricidad', ('programa de mantenimiento eléctrico; termografía de cuadros [criterio del kit: anual]',
                      'NFPA 70B (2023)')),
    ('ascensores', ('inspección anual del inspector estatal o municipal; certificado en la cabina',
                    '[estatal] ASME A17.1 / A17.3; p. ej. Texas Health and Safety Code Ch. 754')),
    ('calderas', ('certificado estatal de calderas', '[estatal] NBIC; p. ej. 522 CMR 4.05 (Massachusetts)')),
    ('sangre', ('agujas y sangre: guantes, kit y contenedor de punzantes; plan de control de exposición',
                '29 CFR 1910.1030')),
    ('panico', ('botón de pánico para quien limpia solo en habitaciones (donde la ley local lo exige)',
                '[local] Chicago (2017), Seattle (2016), New Jersey (2019)')),
    ('chinches', ('revisión de chinches en la limpieza y en el control de plagas', 'EPA (bed bugs) [estatal]')),
    ('ada', ('mantener utilizables los elementos accesibles; elevador de piscina; animales de servicio',
             '2010 ADA Standards §242, §1009; 28 CFR 36.211, 36.302(c)')),
    ('alcohol', ('alcohol solo a mayores de 21', '[estatal] ley de alcohol')),
    ('tarifas_ftc', ('precio total con las tarifas obligatorias (resort fee) en el alojamiento',
                     '16 CFR Part 464 (FTC, desde el 12-may-2025)')),
    ('i9', ('Form I-9 de cada contratación; 3 años desde la contratación o 1 desde la baja', '8 CFR 274a.2(b)(2)')),
    ('pci', ('datos de tarjeta según PCI DSS (norma del sector, no ley)', 'PCI DSS')),
    ('temperaturas_sala', ('sala 68–72 °F; cabina de spa 75–79 °F; par de lencería 3 [criterio del kit]',
                           '[criterio del kit]')),
    ('uk_legionela', ('agua caliente 60 °C almacenada y 50 °C distribuida; fría < 20 °C', 'HSE ACOP L8')),
    ('uk_incendios', ('evaluación de riesgos de incendio del «responsible person»', 'Regulatory Reform (Fire Safety) '
                                                                                   'Order 2005')),
])
# °F que el kit puede afirmar (G7): F&B (−31, −4, 0, 32, 41, 70, 100, 135), sala y spa (68, 72, 75, 79, 95, 100, 104),
# legionela (120, 140) y la respuesta a incidentes fecales de la piscina (77)
GRADOS_F_SPEC = {-31, -4, 0, 32, 41, 68, 70, 72, 75, 77, 79, 95, 100, 104, 120, 135, 140}

# ==========================================================================
# Pistas y dependencias del hotel (extraer_textos.py)
# ==========================================================================
PISTAS_CAMBIO = {r'Kit de Tareas': 'D2: «Hotel Checklists Kit Pro»'}
PISTAS_FUERA = (r'Restaurante Casual',)
PISTAS_EXTRA = [
    (r'[Cc]amarer[ao]s? de pisos|[Gg]obernant', 'camarera de pisos → room attendant; gobernanta → executive '
                                               'housekeeper / housekeeping supervisor (inspector)'),
    (r'[Rr]ecepci[oó]n|[Rr]ecepcionista', 'recepción → front desk; recepcionista → front desk agent (guest service '
                                         'agent); jefe de recepción → front office manager'),
    (r'[Aa]uditor[ií]a nocturna|[Nn]ight audit', 'auditoría nocturna → night audit; quien la hace → night auditor'),
    (r'[Ll]ogbook|[Rr]ack', 'logbook → shift log (pass-on log); rack de habitaciones → room status in the PMS'),
    (r'[Bb]ell boys?|[Mm]aleter', 'bell boys → bell staff (bellperson)'),
    (r'[Rr]oom service', 'room service → in-room dining (IRD); «room service» se entiende, úsalo entre paréntesis'),
    (r'[Bb]anquete|[Mm]a[iî]tre', 'banquetes → banquets; maître de banquetes → banquet captain; la reserva del evento → '
                                  'BEO (banquet event order)'),
    (r'[Ll]encer[ií]a|[Ll]avander[ií]a|[Aa]lbar[aá]n|par stock', 'lencería → linen (linen room); lavandería '
                                                                 'industrial → outside laundry; albarán → count '
                                                                 'sheet / delivery ticket; par stock → linen par'),
    (r'[Nn]o molestar|[Ee]stancia|[Ss]alida|[Cc]heckout', 'estancia (ocupada) → stayover; salida → checkout (departure '
                                                          'room); «No molestar» → Do Not Disturb (DND)'),
    (r'[Mm]antenimiento|[Pp]arte de aver[ií]as|[Pp]reventiv', 'mantenimiento → engineering (maintenance); jefe → chief '
                                                              'engineer; parte de averías → work orders; preventivo → '
                                                              'preventive maintenance (PM)'),
    (r'ACS|[Gg]rupo electr[oó]geno|[Cc]uadros? el[eé]ctric|[Ff]ancoil', 'ACS → domestic hot water; grupo electrógeno → '
                                                                       'emergency generator; cuadro eléctrico → '
                                                                       'electrical panel; fancoil → fan coil unit'),
    (r'[Tt]umbonas?|[Ss]ocorrist|[Vv]aso|[Pp]laya|[Rr]etrolavado|[Ll]impiafondos|[Ss]kimmer',
     'tumbonas → loungers (pool chairs); socorrista → lifeguard; vaso → pool shell; playa → pool deck; retrolavado → '
     'backwash; limpiafondos → pool vacuum'),
    (r'[Cc]abina|[Cc]amilla|[Tt]erapeuta|[Jj]acuzzi|[Vv]apor', 'cabina → treatment room; camilla → treatment table; '
                                                               'terapeuta → therapist; jacuzzi → hot tub (whirlpool '
                                                               'spa); baño de vapor → steam room'),
    (r'ADR|RevPAR|[Pp]ickup|OTA|[Pp]aridad|CTA|CTD', 'revenue: ADR, RevPAR, pickup, OTAs, rate parity, CTA/CTD se quedan '
                                                     '(jerga US)'),
    (r'[Cc]argos? a habitaci[oó]n|[Rr][eé]gimen|[Pp]ulsera', 'cargo a habitación → room charge (post to room); '
                                                             'régimen → rate plan / meal plan; pulsera → wristband'),
    (r'[Oo]ffice de sala|[Oo]utlets?', 'office de sala → server station; outlet → outlet (F&B outlet)'),
    (r'\d\*|[Ee]strellas', 'categoría en estrellas → economy / midscale / upscale / luxury (en EE. UU. no hay '
                           'estrellas oficiales)'),
    (r'[Ee]ncargad', 'encargado → manager on duty (MOD)'),
    (r'[Tt]erraza', 'terraza → patio (o rooftop / pool deck si el texto lo dice)'),
    (r'[Bb]ooking|[Ee]xpedia|TripAdvisor', 'reseñas y OTAs US: Google, TripAdvisor, Expedia; Booking.com detrás'),
    (r'APPCC', 'APPCC → food safety plan (HACCP solo si lo exige el departamento de salud)'),
    (r'[Cc]loro|\bpH\b', 'cloro → free chlorine (FC), en ppm; pH se queda'),
    (r'[Dd]esinfect', 'desinfectar → sanitize (superficies de alimentos) o disinfect (baños, superficies duras, con '
                      'producto registrado en la EPA)'),
]
DEPENDENCIAS_EXTRA = OrderedDict([
    ('variante', ('Sufijo de variante «Hotel Completo / Integral»', r'Hotel Completo|Hotel Integral',
                  'D2: la EN no lleva sufijo')),
    ('piscina', ('Piscina: cloro, pH y libro obligatorio', r'[Cc]loro|\bpH\b|libro (de mantenimiento )?obligatorio|'
                 r'comunidad autónoma', 'D-HOT: MAHC 2024 + código estatal (ADAPTAR)')),
    ('legionela', ('Legionela y ACS (RD 487/2022)', r'[Ll]egionel|\bACS\b|RD 487', 'D-HOT: ASHRAE 188 + CDC (140 / '
                                                                                   '120 °F)')),
    ('instalaciones', ('Inspecciones españolas (OCA, RITE, BIE, retimbrado)', r'\bOCA\b|RITE|BIEs?\b|[Rr]etimbrado',
                       'D11: NFPA, OSHA, inspector estatal o municipal (POR_CELDA del 13)')),
    ('registro_jornada', ('Registro de jornada (RD-ley 8/2019)', r'RD-ley|[Rr]egistro (horario|de jornada)|'
                          r'Inspección de Trabajo', 'D11: FLSA (29 CFR 516) + I-9')),
    ('otas', ('OTAs y reseñas', r'Booking|Expedia|TripAdvisor|OTAs', 'D16: Google, TripAdvisor, Expedia')),
    ('estrellas', ('Categoría en estrellas', r'\d\*', 'economy / midscale / upscale / luxury')),
])

# aplicar_en / gates_en (autotest): horas de celda y hoja protegida con verdes desbloqueadas en el 18 (el molde ligero no
# protege); el 06 del hotel tiene una sola checklist (la mutación de área de impresión va a ella)
HOJA_HORAS = ('18', 'Apertura del Negocio')
HOJA_VERDE = ('18', 'Apertura del Negocio')
HOJA_AREA_AUTOTEST = 'Banquetes y Eventos'
CITA_AUTOTEST = '(FDA Food Code 3-501.19)'                     # autotest G7: una cita que NO está en REGLAS_US


def _rebind(f):
    return types.FunctionType(f.__code__, globals(), f.__name__, f.__defaults__, f.__closure__)


titulo_interior = _rebind(_base.titulo_interior)
_autotest_base = _rebind(_base.autotest)
_cruzar_censo_base = _rebind(_base.cruzar_censo)


def autotest():
    # el «11» fijo del base (FICHEROS debe tener 11 nombres) se cambia por N_LIBROS, como la pastelería
    err = [e for e in _autotest_base() if e != 'FICHEROS debe tener 11 nombres EN distintos']
    if len(FICHEROS) != N_LIBROS or len(set(FICHEROS.values())) != N_LIBROS:
        err.append('FICHEROS debe tener %d nombres EN distintos' % N_LIBROS)
    if CLAVES['Tarea'] != GLOSARIO['Tarea']:
        err.append('CLAVES["Tarea"] debe ser el EN de la cabecera (GLOSARIO): los contadores la restan')
    rx = re.compile(TERMINOS_PROHIBIDOS)
    if not rx.search(TERMINO_PROHIBIDO_EJEMPLO):
        err.append('TERMINO_PROHIBIDO_EJEMPLO no lo caza TERMINOS_PROHIBIDOS')
    for ok in ('restaurant', 'room attendant', 'night auditor', 'pool bar', 'in-room dining', 'banquet captain',
               'bartender', 'server', 'patio', 'front desk', 'coffee machine', 'host stand', 'restaurant consultant'):
        if rx.search(ok):
            err.append('TERMINOS_PROHIBIDOS caza lo permitido (%r)' % ok)
    rx_ctx = re.compile(RX_CONTEXTO_PENDIENTE)
    for ok in ('room attendant', 'night auditor', 'pool bar', 'in-room dining', 'banquet captain', 'manager on duty',
               'restaurant consultant'):
        if rx_ctx.search(ok):
            err.append('RX_CONTEXTO_PENDIENTE caza lo permitido (%r)' % ok)
    for k, v in list(GLOSARIO.items()) + list(POR_CELDA.items()) + list(CLAVES.items()):
        if (k not in _base.GLOSARIO or k in _GLOSARIO_HOTEL) and isinstance(v, str) and rx.search(v):
            err.append('texto EN fijado con un término prohibido: %r → %r' % (k, v))
    if CITA_AUTOTEST.strip('()').split()[-1] in ' '.join(f for _v, f in REGLAS_US.values()):
        err.append('CITA_AUTOTEST está en REGLAS_US: G7 no la cazaría')
    if HOJA_CAJA[0] not in HOJAS_ES_POR_LIBRO or HOJA_CAJA[1] not in HOJAS_ES_POR_LIBRO[HOJA_CAJA[0]]:
        err.append('HOJA_CAJA %r no es una hoja del kit' % (HOJA_CAJA,))
    if HOJA_AREA_AUTOTEST not in HOJAS_ES_POR_LIBRO['06']:
        err.append('HOJA_AREA_AUTOTEST no es una hoja del 06')
    # 18 cierre: permutación de 5-19 y persiana, alarma y llave al final
    if sorted(o for o, *_r in _CIERRE_18) != list(range(5, 20)):
        err.append('18 cierre: las filas de origen no son una permutación de 5-19')
    if [o for o, *_r in _CIERRE_18][-3:] != [9, 16, 17]:
        err.append('18 cierre: persiana, alarma y llave tienen que ser las 3 últimas')
    if [o for o, *_r in _CIERRE_18].index(18) > [o for o, *_r in _CIERRE_18].index(16):
        err.append('18 cierre: los check-outs pendientes van antes de la alarma')
    # G7 (gates_en.permitidas): las °F de REGLAS_US (valor y fuente), POR_CELDA y ADAPTAR son EXACTAMENTE GRADOS_F_SPEC
    rx_g7 = re.compile(r'([−-]?\d+(?:\.\d+)?)\s*(?:(?:–|-|to|and)\s*([−-]?\d+(?:\.\d+)?)\s*)?°\s*F')
    vistos = set()
    for t in [x for v_f in REGLAS_US.values() for x in v_f] + list(POR_CELDA.values()) + list(ADAPTAR.values()):
        for m in rx_g7.finditer(t):
            vistos.update(float(g.replace('−', '-')) for g in m.groups() if g)
    if vistos != {float(x) for x in GRADOS_F_SPEC}:
        err.append('°F de mapas ≠ GRADOS_F_SPEC: sobran %s, faltan %s' % (
            sorted(vistos - {float(x) for x in GRADOS_F_SPEC}), sorted({float(x) for x in GRADOS_F_SPEC} - vistos)))
    # °F de los textos fijados y de los ADAPTAR dentro de GRADOS_F_SPEC (G7 lo mide luego en los xlsx)
    rx_f = re.compile(r'(−|-)?(\d+)(?:–(\d+))? °F')
    for nombre, dic in (('POR_CELDA', POR_CELDA), ('ADAPTAR', ADAPTAR)):
        for k, v in dic.items():
            for m in rx_f.finditer(v):
                for g in (m.group(2), m.group(3)):
                    if g is None:
                        continue
                    x = -int(g) if (m.group(1) and g == m.group(2)) else int(g)
                    if x not in GRADOS_F_SPEC:
                        err.append('%s %r: %s °F fuera de GRADOS_F_SPEC' % (nombre, k, x))
    for k in CF_POR_CELDA:
        if k[:2] not in {(c, h) for c, hs in HOJAS_ES_POR_LIBRO.items() for h in hs}:
            err.append('CF_POR_CELDA en una hoja que no existe: %r' % (k,))
    for k in list(POR_CELDA) + list(ADAPTAR):
        if k[0] not in HOJAS_ES_POR_LIBRO or k[1] not in HOJAS_ES_POR_LIBRO[k[0]]:
            err.append('celda fijada en una hoja que no existe: %r' % (k,))
    return err


def cruzar_censo(p):
    import json
    from openpyxl.utils import range_boundaries
    err = _cruzar_censo_base(p)
    censo = json.load(open(p, encoding='utf-8'))
    tx = {}
    for info in censo['libros'].values():
        for h, hd in info['hojas_detalle'].items():
            for coord, t in hd.get('textos', {}).items():
                tx[(info['corto'], h, coord)] = t
    cfs = {(info['corto'], h, cf['sqref']): cf['formula'] for info in censo['libros'].values()
           for h, hd in info['hojas_detalle'].items() for cf in hd['cf']}
    for k, (es, en) in CF_POR_CELDA.items():
        if cfs.get(k) != [es]:
            err.append('CF_POR_CELDA %r: el ES trae %r, no %r' % (k, cfs.get(k), es))
    # CF de «hecho» del molde ligero: va en CF_POR_CELDA si y solo si su rango contiene una cabecera interna «Tarea»
    for k, f in cfs.items():
        if f != ['$E6="✓"']:
            continue
        _c1, r1, _c2, r2 = range_boundaries(k[2])
        interna = any(tx.get((k[0], k[1], 'B%d' % r)) == 'Tarea' for r in range(r1, r2 + 1))
        if interna != (k in CF_POR_CELDA):
            err.append('CF de «hecho» %r: cabecera interna en el rango = %s, en CF_POR_CELDA = %s' % (
                k, interna, k in CF_POR_CELDA))
    # 18 cierre: el ES tiene tarea en la fila de origen; zona EN = glosario de la zona ES de esa fila; responsable ES =
    # el esperado salvo _RESPONSABLE_CAMBIA
    for o, _b, c_en, d_en in _CIERRE_18:
        if (_CN[0], _CN[1], 'B%d' % o) not in tx:
            err.append('18 cierre: B%d sin tarea en el ES' % o)
        z_es = tx.get((_CN[0], _CN[1], 'C%d' % o))
        if GLOSARIO.get(z_es) != c_en:
            err.append('18 cierre: la zona de la fila %d (%r → %r) no es %r' % (o, z_es, GLOSARIO.get(z_es), c_en))
        r_es = tx.get((_CN[0], _CN[1], 'D%d' % o))
        if GLOSARIO.get(r_es) != d_en and o not in _RESPONSABLE_CAMBIA:
            err.append('18 cierre: el responsable de la fila %d (%r) no es %r' % (o, r_es, d_en))
    if not tx.get((_CN[0], _CN[1], 'B18'), '').startswith('Verificar registro de check-outs') or \
            not tx.get((_CN[0], _CN[1], 'B16'), '').startswith('Activar alarma'):
        err.append('18 cierre: el ES ya no revisa los check-outs después de la alarma (errata corregida en el ES)')
    # 13 · Trimestral y Anual: cada fila fijada tiene tarea en el ES y las B de servicios del ES quedan TODAS fijadas
    # salvo las dos de gestión (escandallos y nº de parte) que traduce el traductor
    tareas_13 = {int(c[1:]) for (lb, h, c) in tx if (lb, h) == _T13 and c.startswith('B') and c[1:].isdigit()
                 and tx[(lb, h, c)] not in ('Tarea', 'Tareas completadas:')}
    sin_fijar = sorted(tareas_13 - set(_SERVICIOS_13))
    if sin_fijar != [35, 36]:
        err.append('13 Trimestral y Anual: filas de tarea sin POR_CELDA %r (se esperaban las 35 y 36)' % sin_fijar)
    # calendario: B, C, D, E con texto en el ES en las 24 filas
    for fila in FILAS_CALENDARIO:
        for col in 'BCDE':
            if (HOJA_CAL[0], HOJA_CAL[1], '%s%d' % (col, fila)) not in tx:
                err.append('calendario: %s%d sin texto en el ES' % (col, fila))
    # todo texto ES con °C tiene su °F fijado (POR_CELDA) o un ADAPTAR que lo da
    for k, t in tx.items():
        if '°C' in t and k not in CELSIUS_SIN_F:
            dic = POR_CELDA.get(k) or ADAPTAR.get(k) or ''
            if '°F' not in dic:
                err.append('°C del ES sin °F en POR_CELDA/ADAPTAR: %r' % (k,))
    # horas de celda: solo en el 18 y el 19 (D9: hora_us sin desplazar; las de los títulos de sección, el traductor)
    horas = sorted({(k[0], k[1]) for k, t in tx.items() if RX_HORA_CELDA.match(t)})
    if horas != [('18', 'Apertura del Negocio'), ('19', 'Apertura de Caja')]:
        err.append('horas de celda fuera del 18 «Apertura» y el 19 «Apertura de Caja»: %r' % horas)
    return err


def cruzar_base(p_hot, p_base):
    """Lo heredado POR CELDA del base (POR_CELDA y ADAPTAR del 09 → 19, el ADAPTAR del 08 B8 → 18 y el fichaje del 03
    → 14) tiene en el hotel el mismo texto ES (o la misma tarea) que en el base."""
    import json
    err = []

    def textos(p):
        d = {}
        for info in json.load(open(p, encoding='utf-8'))['libros'].values():
            for h, hd in info['hojas_detalle'].items():
                for coord, t in hd.get('textos', {}).items():
                    d[(info['corto'], h, coord)] = t
        return d
    tb, th = textos(p_base), textos(p_hot)
    for nombre, claves in (('POR_CELDA', _HEREDA_POR_CELDA), ('ADAPTAR', _HEREDA_ADAPTAR)):
        for k in claves:
            if th.get(_R(k)) != tb.get(k):
                err.append('%s heredado %r: el texto ES del hotel %r ≠ base %r' % (nombre, k, th.get(_R(k)), tb.get(k)))
    if th.get(('18', 'Apertura del Negocio', 'B8')) != tb.get(('08', 'Apertura del Negocio', 'B8')):
        err.append('ADAPTAR 18 B8 heredado del 08 B8: otro texto ES')
    # filas equivalentes (otra celda, la misma tarea del base): mismo tema en el ES
    for k, palabra in ((('01', 'Apertura Desayuno', 'B7'), 'anillos'), (('01', 'Apertura Desayuno', 'B9'), 'manos'),
                       (('01', 'Apertura Desayuno', 'B10'), 'síntomas'), (('01', 'Apertura Desayuno', 'B13'), 'gas'),
                       (('14', 'RRHH Operativo', 'B12'), 'registro de jornada'),
                       (('14', 'RRHH Operativo', 'B7'), 'registro de jornada'),
                       (('02', 'Buffet Almuerzo', 'B7'), 'lejía'), (('02', 'Instrucciones', 'B15'), 'lejía')):
        if palabra not in th.get(k, ''):
            err.append('%r ya no es la tarea equivalente del base (falta %r)' % (k, palabra))
    # la caja del 19: mismas fórmulas que el 09 del base en las hojas de caja
    fx = {}
    for nombre, p in (('base', p_base), ('hotel', p_hot)):
        for info in json.load(open(p, encoding='utf-8'))['libros'].values():
            if info['corto'] in ('09', '19'):
                for h, hd in info['hojas_detalle'].items():
                    if h in ('Cierre de Caja', 'Registro Mensual'):
                        fx[(nombre, h)] = hd['formulas']
    for h in ('Cierre de Caja', 'Registro Mensual'):
        if fx.get(('base', h)) != fx.get(('hotel', h)):
            diff = sorted(set(fx.get(('base', h), {}).items()) ^ set(fx.get(('hotel', h), {}).items()))
            # los contadores de tareas (C23/E23 del hotel, otra fila) no cuentan: solo la caja y el registro
            diff = [d for d in diff if 'COUNTIF' not in d[1]]
            if diff:
                err.append('19 %s: fórmulas distintas del 09 del base %r' % (h, diff[:4]))
    return err


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
        e += cruzar_base(pc, os.path.join(os.path.dirname(AQUI), 'censo_es.json'))
    for x in e:
        print('ERROR', x)
    print('mapas_hotel.py: {} ficheros · {} pestañas · {} glosario · {} por celda · {} cf por celda · {} adaptar · '
          '{} reglas · {} errores'.format(len(FICHEROS), len(HOJAS), len(GLOSARIO), len(POR_CELDA), len(CF_POR_CELDA),
                                          len(ADAPTAR), len(REGLAS_US), len(e)))
    raise SystemExit(1 if e else 0)
