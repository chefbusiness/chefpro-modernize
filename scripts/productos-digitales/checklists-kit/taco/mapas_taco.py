#!/usr/bin/env python3
"""
mapas_taco.py — Taco Shop Checklists Kit Pro (EN) · DELTA del Kit de Tareas Recurrentes: Taquería Mexicana
(`kit-tareas-taqueria`, 11 xlsx v2.0) sobre `mapas.py` (Restaurant Checklists Kit Pro). SPEC: `taco/SPEC.md` (solo el
delta). Undécimo hermano vertical. Sesión Claude Code, 31-oct-2026.

Se usa con `--kit taco` (kit.py). Importa `mapas.py` y SOLO añade o sobrescribe: producto, ficheros, títulos, pestañas
(mapa de libros propio en el molde del kit base: 01-08 checklists P4, 09 = la plantilla en blanco del 07 base, B01 y
B02 del base; SIN libro de caja), glosario de taquería (taquero, griddle cook, tortilla maker, salsa prep cook,
counter, salsa bar, receiving, códigos MX / US / All del 08), calendario (B02 propio: filas 5-31), POR_CELDA (el
orden del cono y el montaje del 01, fichajes FLSA, pescado crudo 3-402.11), ADAPTAR (°F, trompo, salsas TCS, masa,
recalentado, alérgenos US, propinas, gas, alcohol) y REGLAS_US. La hora de 12 h y el resto se heredan. Sin caja:
`HOJA_CAJA = None`, `DENOMINACIONES` y `FORMULAS_POR_CELDA` vacíos (la F2 añade el gancho en gates_en.py, SPEC §1
D12). Las funciones del base que leen constantes (titulo_interior, autotest, cruzar_censo) se re-enlazan a ESTE
módulo. Ejecutado como script: autotest + cruce con taco/censo_es.json.

    python3 taco/mapas_taco.py
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
AQUI = os.path.dirname(os.path.abspath(__file__))              # taco/ (el import * trae el AQUI del base)

ORIGEN_ES = 'kit-tareas-taqueria'
PRODUCTO = 'Taco Shop Checklists Kit Pro'
TITULO_SEO = 'Taco Shop Checklists Kit Pro: Taqueria Opening & Closing Checklist Templates for Excel'
SLUG = 'taco-shop-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_TACO_SHOP_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
MARCA_ES = '— Kit de Tareas Recurrentes · Taquería Mexicana · AI Chef Pro · aichef.pro'
MARCA_EN = '— ' + PRODUCTO + ' · AI Chef Pro · aichef.pro'
VARIANTES_ES = ('Taquería Mexicana',)
# heredar.py: memoria con VARIAS fuentes, en orden de preferencia (gana la primera): el base (las Instrucciones son
# las suyas) y los hermanos de mostrador y delivery
_SUF = lambda v: [(' — Taquería Mexicana', ' — ' + v), (' · Taquería Mexicana', ' · ' + v)]  # noqa: E731
MEMORIA = [('base', '', _SUF('Restaurante Casual')), ('pizza', 'pizza', _SUF('Pizzería')),
           ('burger', 'burger', _SUF('Hamburguesería')), ('cafe', 'cafe', _SUF('Cafetería / Brunch')),
           ('ghost', 'ghost', _SUF('Dark Kitchen'))]
# heredar.py: EN heredado que en una taquería no vale tal cual → pendientes (motivo «contexto»)
RX_CONTEXTO_PENDIENTE = (r'(?i)\b(?:restaurants?(?! consultant)|host stands?|head chefs?|sous chefs?|MOD|'
                         r'coffee shops?|(?<!sidewalk )cafes?|baristas?|shift leads?|kitchen leads?|bussers?|'
                         r'pastry case|barbacks?|bartenders?|cocktails?|venues?|banquets?|BEOs?|commissary|'
                         r'line-up|brunch|pizzas?|pizzerias?|pizza makers?|dough|mozzarella|wood-fired|ovens?|'
                         r'burgers?|grill cooks?|servers?|FOH|packers?|virtual brands?)\b')
NO_HEREDAR = {}
# gates_en.py G2: términos de otros kits (y calcos) que NINGUNA celda EN de la taquería puede llevar. «plancha» es el
# calco que la jerga US no usa (flat-top griddle, research US §9 n.º 14); «Tex-Mex» no es sinónimo (research §9).
# «restaurant consultant» (firma) y «sidewalk cafe permit» quedan fuera por el lookahead / lookbehind.
TERMINOS_PROHIBIDOS = (r'(?i:\b(?:restaurants?(?! consultant)|host stands?|head chefs?|sous chefs?|coffee shops?|'
                       r'(?<!sidewalk )cafes?|baristas?|shift leads?|kitchen leads?|bussers?|barbacks?|banquets?|'
                       r'BEOs?|commissary|venues?|line-up|pizzas?|pizzerias?|burgers?|plancha|tex-mex)\b)|\bMOD\b')
TERMINO_PROHIBIDO_EJEMPLO = 'Scrape the plancha.'
# gates_en.py G2 (FRASES_OK += FRASES_OK_EXTRA): nombres de plato US con palabra funcional española
FRASES_OK_EXTRA = ('al pastor', 'Al pastor', 'Al Pastor', 'tinga de pollo', 'Tinga de pollo')
REFERENCIAS_TRADUCTOR = ['taco/SPEC.md', 'SPEC.md §0-§3 y §7.2 (brief)', 'textos_en/glosario.json (glosario de la '
                         'prosa del kit base)', 'taco/textos_en/heredado.json (cómo se dijo ya cada cosa: base, '
                         'pizzería, hamburguesería, cafetería y ghost kitchen)', 'taco/mapas_taco.py: GLOSARIO, '
                         'HOJAS, FICHEROS, TITULOS, POR_CELDA, REGLAS_US', '../business-plans-en-12/'
                         'F1-research-us-delta.md §6 y §9 (jerga del Taco Shop Business Plan Kit)',
                         '../GLOSARIO-JERGA-ES-EN.md (sección Taquería)']
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v2.0'),
    ('keywords', 'taco shop checklist, taqueria checklist, taco shop opening checklist, taco shop closing checklist, '
                 'salsa bar checklist, trompo, al pastor, AI Chef Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

# ==========================================================================
# Ficheros (D5): «taco shop» (nombre) y «taqueria» (sin tilde) como el Taco Shop Business Plan Kit; trompo, comal,
# salsa bar, nixtamal y masa son jerga US (research US §9)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-apertura-cierre-taqueria.xlsx', '01-taco-shop-opening-closing-checklists.xlsx'),
    ('02-trompo-plancha-comal.xlsx', '02-trompo-griddle-comal-checklists.xlsx'),
    ('03-appcc-salsas-alergenos.xlsx', '03-taco-shop-food-safety-salsa-bar-allergens.xlsx'),
    ('04-nixtamal-tortilla-guisados.xlsx', '04-nixtamal-masa-tortilla-guisados-checklists.xlsx'),
    ('05-tareas-manager.xlsx', '05-taqueria-manager-checklist.xlsx'),
    ('06-tareas-perfiles.xlsx', '06-taco-shop-duties-by-role.xlsx'),
    ('07-semanales-mensuales.xlsx', '07-taco-shop-weekly-monthly-cleaning-checklist.xlsx'),
    ('08-eventos-estacionales.xlsx', '08-taco-shop-event-seasonal-checklists.xlsx'),
    ('09-plantilla-personalizable.xlsx', '09-blank-taco-shop-checklist-template.xlsx'),
    ('BONUS-01-briefing-servicio.xlsx', 'BONUS-01-taco-shop-pre-shift-meeting-template.xlsx'),
    ('BONUS-02-calendario-anual.xlsx', 'BONUS-02-taco-shop-annual-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)
TITULOS = OrderedDict([
    ('01-taco-shop-opening-closing-checklists.xlsx',
     'Taco Shop Opening & Closing Checklists: Trompo, Salsa Bar, Tortillas & Counter'),
    ('02-trompo-griddle-comal-checklists.xlsx',
     'Trompo, Griddle & Comal Checklists: Al Pastor Marinade, Stacking & Carving'),
    ('03-taco-shop-food-safety-salsa-bar-allergens.xlsx',
     'Taco Shop Food Safety Checklists: Temperature Logs, Salsa Bar & Allergens'),
    ('04-nixtamal-masa-tortilla-guisados-checklists.xlsx', 'Nixtamal, Masa, Tortilla & Guisados Checklists'),
    ('05-taqueria-manager-checklist.xlsx', 'Taqueria Manager Checklist: Daily & Weekly'),
    ('06-taco-shop-duties-by-role.xlsx',
     'Taco Shop Duties by Role: Taquero, Tortilla Maker, Salsa Prep, Griddle, Counter & Driver'),
    ('07-taco-shop-weekly-monthly-cleaning-checklist.xlsx',
     'Taco Shop Weekly & Monthly Checklists: Deep Cleaning, Inventory & Maintenance'),
    ('08-taco-shop-event-seasonal-checklists.xlsx',
     'Taco Shop Event & Seasonal Checklists: Holidays, Busy Days & Seasonal Ingredients'),
    ('09-blank-taco-shop-checklist-template.xlsx', 'Blank Taco Shop Checklist Template (Editable)'),
    ('BONUS-01-taco-shop-pre-shift-meeting-template.xlsx', 'BONUS: Taco Shop Pre-Shift Meeting Template (Huddle Notes)'),
    ('BONUS-02-taco-shop-annual-calendar.xlsx', 'BONUS: Taco Shop Annual Calendar: Holidays, Busy Days & Upkeep (US)'),
])
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

# Pestañas (D6): ≤ 31 caracteres, sin comas (rompen el área de impresión) ni []:*?/\
HOJAS = OrderedDict(_base.HOJAS)
HOJAS.update([
    ('Apertura Taquería', 'Taco Shop Opening'), ('Cierre Taquería', 'Taco Shop Closing'),
    ('Marinado y Montaje del Trompo', 'Marinade & Trompo Stacking'), ('Corte, Plancha y Comal', 'Carving + Griddle + Comal'),
    ('Temperaturas y Trazabilidad', 'Temp Logs & Receiving'), ('Barra de Salsas', 'Salsa Bar'),
    ('Alérgenos y Cruzada', 'Allergens & Cross-Contact'),
    ('Nixtamal y Molienda', 'Nixtamal & Masa Milling'), ('Tortilla y Comal', 'Tortillas & Comal'),
    ('Guisados y Rotación', 'Guisados & Rotation'),
    ('Tareas Diarias Manager', 'Manager Daily'), ('Tareas Semanales Manager', 'Manager Weekly'),
    ('Taquero del Trompo', 'Taquero (Trompo)'), ('Tortillería', 'Tortilla Maker'), ('Salsas', 'Salsa Prep'),
    ('Plancha y Freidora', 'Griddle & Fryer'), ('Mostrador y Caja', 'Counter & Register'),
    ('Reparto y Delivery', 'Delivery Driver'),
    ('Tareas Semanales', 'Weekly Tasks'), ('Tareas Mensuales', 'Monthly Tasks'),
    ('Temporadas y Producto', 'Seasonal Ingredients'), ('Calendario de Eventos', 'Event Calendar'),
    ('Plantilla en Blanco', 'Blank Template'), ('Briefing Pre-Servicio', 'Pre-Shift Meeting'),
    ('Calendario Anual', 'Annual Calendar'),
])
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Apertura Taquería', 'Cierre Taquería']),
    ('02', ['Instrucciones', 'Marinado y Montaje del Trompo', 'Corte, Plancha y Comal']),
    ('03', ['Instrucciones', 'Temperaturas y Trazabilidad', 'Barra de Salsas', 'Alérgenos y Cruzada']),
    ('04', ['Instrucciones', 'Nixtamal y Molienda', 'Tortilla y Comal', 'Guisados y Rotación']),
    ('05', ['Instrucciones', 'Tareas Diarias Manager', 'Tareas Semanales Manager']),
    ('06', ['Instrucciones', 'Taquero del Trompo', 'Tortillería', 'Salsas', 'Plancha y Freidora', 'Mostrador y Caja',
            'Reparto y Delivery']),
    ('07', ['Instrucciones', 'Tareas Semanales', 'Tareas Mensuales']),
    ('08', ['Instrucciones', 'Temporadas y Producto', 'Calendario de Eventos']),
    ('09', ['Instrucciones', 'Plantilla en Blanco']),
    ('B01', ['Instrucciones', 'Briefing Pre-Servicio']),
    ('B02', ['Instrucciones', 'Calendario Anual']),
])

# ==========================================================================
# GLOSARIO: el base entero (opcional en la taquería) + celdas cortas de la taquería (celda ENTERA, sin columna: una
# palabra que es zona y puesto lleva un solo EN). Jerga US del Taco Shop Business Plan Kit (research US §9):
# taquero · flat-top griddle (nunca «plancha») · comal · tortilleria · salsa bar.
# ==========================================================================
GLOSARIO = OrderedDict(_base.GLOSARIO)
_GLOSARIO_TACO = OrderedDict([
    # zonas (C)
    ('Cámara', 'Walk-in'), ('Barra', 'Salsa bar'), ('Tortillería', 'Tortilleria'), ('Mostrador', 'Counter'),
    ('Sala', 'Dining area'), ('Recepción', 'Receiving'), ('Almacén', 'Storage'), ('Oficina', 'Office'),
    ('Delivery', 'Delivery'),
    # 08 «Calendario de Eventos» C: dónde pesa la fecha (MX = calendario mexicano; ES y US-es → US; Todos → All)
    ('MX', 'MX'), ('ES', 'US'), ('US-es', 'US'), ('Todos', 'All'),
    # puestos (D)
    ('Taquero', 'Taquero'), ('Plancha', 'Griddle cook'), ('Tortillero/a', 'Tortilla maker'),
    ('Salsero/a', 'Salsa prep cook'), ('Repartidor', 'Delivery driver'),
    # cuándo (E)
    ('1º de mes', '1st of month'), ('Quincenal', 'Biweekly'), ('Fin de mes', 'Month-end'),
    ('Al confirmar', 'When confirmed'), ('2 semanas antes', '2 weeks out'), ('Víspera', 'Day before'),
])
GLOSARIO.update(_GLOSARIO_TACO)
GLOSARIO_OPCIONAL = frozenset(_base.GLOSARIO)
PUESTOS_ES = frozenset(_base.PUESTOS_ES | {'Cámara', 'Barra', 'Tortillería', 'Mostrador', 'Almacén', 'Oficina',
                                           'Delivery', 'MX', 'ES', 'US-es', 'Todos', 'Taquero', 'Plancha',
                                           'Tortillero/a', 'Salsero/a', 'Repartidor'})

# ==========================================================================
# Sin libro de caja (D12): el ES no trae 08 de negocio ni 09 de caja (01 «Instrucciones» B35 lo dice). La caja del
# día son 3 tareas del 01 «Cierre» y 1 del 05 (ADAPTAR / pistas: POS, starting bank, cash count, over/short)
# ==========================================================================
HOJA_CAJA = None
DENOMINACIONES = []
VALORES_DENOMINACION_EN = []
FORMULAS_POR_CELDA = OrderedDict()

# ==========================================================================
# BONUS-02 «Annual Calendar»: el molde del base (A mes · B fecha/evento · C tareas · D antelación) con 27 filas
# (5-31) + 5 libres. A, B y D fijados; C = traductor, con ADAPTAR donde la fecha cambia o pide dato US. Las fechas
# mexicanas se quedan (la clientela de una taquería US las celebra); las españolas pasan a su equivalente US.
# fila → (mes, evento, antelación, ADAPTAR de C o None)
# ==========================================================================
_HACCP_KIT = _base.ADAPTAR[('05', 'Instrucciones', 'B8')]
_GAS = ('Gas en EE. UU.: el personal hace la inspección visual (mangueras, conexiones y llaves del trompo, la plancha '
        '(griddle) y el comal; sin olor a gas); la instalación la revisa un profesional con licencia con la frecuencia '
        'que pida tu código local, y se archiva su informe. Si huele a gas: no encender nada, salir y llamar a la '
        'compañía de gas o al 911 desde fuera')
_CAMPANA = ('Campana (hood): los filtros los desengrasa el equipo; los conductos y la campana completa, una empresa '
            'certificada (NFPA 96)')
_ALCOHOL = ('Mezcal, tequila y cerveza solo si tu taquería tiene la licencia de alcohol del estado (beer & wine o '
            'liquor license); venta a mayores de 21 con ID')
_DISTRIBUIDOR = ('En EE. UU. el chile seco, la masa harina y el maíz para nixtamal se compran a un distribuidor de '
                 'productos mexicanos (Mexican food distributor), no a un «importador»')
FILAS_CALENDARIO = range(5, 32)
CALENDARIO = OrderedDict([
    (5, ('January', 'Jan 6 — Three Kings Day', '2 weeks',
         'Las familias mexicanas y latinas de EE. UU. lo celebran: rosca de Reyes (escrito así) encargada a tu '
         'panadería o proveedor y turno reforzado ese día')),
    (6, ('January', 'Staff time off (slow weeks)', '1 month',
         'En EE. UU. pocas taquerías cierran por vacaciones: reparte el time off del equipo en las semanas flojas de '
         'enero y, si cierras unos días, avísalo en Google Business Profile, Yelp y las apps de delivery')),
    (7, ('February', 'Feb 2 — Candelaria + Super Bowl Sunday (2nd Sunday in Feb)', '2 weeks',
         'Candelaria: tamales y aviso en Google Business Profile y redes (como el ES). Añade la Super Bowl, de los '
         'días fuertes de pedidos para llevar en EE. UU. [criterio del kit]: pedidos anticipados de bandejas (party '
         'trays, taco bar), personal extra de mostrador y de delivery')),
    (8, ('February', 'Gas equipment check', '1 month', _GAS)),
    (9, ('February–April', 'Lent Fridays (from Ash Wednesday, varies)', '2 weeks',
         'Viernes de Cuaresma: reforzar tacos de pescado y capeados (battered fish); el pescado crudo de aguachiles y '
         'tostadas, con su registro de destrucción de parásitos (FDA Food Code 3-402.11) y el aviso al consumidor en '
         'la carta (FDA Food Code 3-603.11)')),
    (10, ('March', 'Thermometer calibration', '2 weeks',
          'Calibrar sondas y termómetros por el método del punto de hielo (32 °F) y anotar la desviación')),
    (11, ('March', 'Spring menu costing review', '2 weeks', None)),
    (12, ('April', 'Corn mill deep clean', '2 weeks', None)),
    (13, ('May', 'May 5 — Cinco de Mayo', '1 week',
          'En EE. UU. es de los días más fuertes del año para una taquería [criterio del kit]: pedidos anticipados, '
          'producto extra (tortillas, al pastor, salsas), personal y horario ampliados; en México se celebra sobre todo '
          'en Puebla (la fiesta nacional es el 16 de septiembre). Margaritas o cerveza solo con licencia, 21+ con ID')),
    (14, ('May', 'Patio season prep (before Memorial Day)', '2 weeks',
          'Terraza = patio; el permiso es el «outdoor dining / sidewalk cafe permit» de la ciudad: renovarlo, revisar '
          'el aforo autorizado y ampliar el horario')),
    (15, ('May–June', 'Summer kickoff (Memorial Day, last Monday of May)', '1 week', None)),
    (16, ('June', 'Online review check', '1 week', 'Plataformas US: Google y Yelp')),
    (17, ('June', 'Supplier audit (dried chiles & masa)', '1 month', _DISTRIBUIDOR + ': auditar plazos, incidencias y '
          'documentación')),
    (18, ('July–September', 'Jul 15 to late Sep — Chiles en nogada season', '1 month',
          'Reservar con el proveedor la nuez fresca (fresh walnuts; sin «nuez de Castilla») y la granada; la '
          'temporada depende de la cosecha')),
    (19, ('July', 'Avocado price check', '2 weeks', None)),
    (20, ('August', 'Chiles en nogada peak', '1 week', None)),
    (21, ('August', 'Pest control check (hottest month)', '2 weeks',
          'Control de plagas por un licensed pest control operator; el equipo revisa señales en el almacén seco')),
    (22, ('September', 'Sep 15–16 — Mexican Independence Day (the Grito)', '2 weeks',
          'En EE. UU. es de las fechas fuertes para la clientela mexicana y latina [criterio del kit]: pozole y '
          'especiales; mezcal o tequila solo con licencia, 21+ con ID')),
    (23, ('September', 'HACCP plan review', '1 month', _HACCP_KIT)),
    (24, ('October', 'Day of the Dead prep', '1 month',
          'Encargar con antelación el pan de muerto (escrito así) y la calabaza para la calabaza en tacha')),
    (25, ('October', 'Hood filter cleaning', '2 weeks', _CAMPANA)),
    (26, ('November', 'Nov 1–2 — Day of the Dead', '2 weeks', 'Pan de muerto (escrito así) y calabaza en tacha')),
    (27, ('November', 'Thanksgiving + holiday party bookings', '1 month',
          'Thanksgiving (4.º jueves de noviembre): decidir si se abre (muchos cierran). Y, como el ES, cerrar menús y '
          'aforos de las fiestas de empresa de diciembre (holiday parties: bandejas y taco bar para oficinas)')),
    (28, ('November', 'Bar inventory (if licensed)', '2 weeks', _ALCOHOL + '; inventario antes de diciembre')),
    (29, ('December', 'Dec 12 — Our Lady of Guadalupe', '2 weeks', None)),
    (30, ('December', 'Dec 16–24 — Posadas + holiday parties', '1 month', None)),
    (31, ('December', "Christmas & New Year's Eve", '2 weeks',
          'Sin uvas ni cava. Como el ES: turnos de cierre y previsión de delivery de fin de año reforzados; decidir el '
          'horario del 24-25 y del 31 (muchos cierran el 25)')),
])

# ==========================================================================
# POR_CELDA: textos EN fijados (no van al traductor)
# ==========================================================================
POR_CELDA = OrderedDict()
# 01 · Apertura (errata ES, §5): el cono recibido se comprobaba DESPUÉS de montar el trompo. Mismas filas y horas:
# la comprobación sube a la 14 (11:00) y el montaje baja a la 15 (11:05)
_AP = ('01', 'Apertura Taquería')
POR_CELDA[_AP + ('B14',)] = 'Check the cone as received: frozen at 0 °F or below, or refrigerated at 41 °F or below'
POR_CELDA[_AP + ('B15',)] = "Stack the day's trompo: layer order, fat, pineapple and onion; note weight and time"
# 03 · pescado crudo de aguachiles y tostadas: destrucción de parásitos (base, FDA Food Code 3-402.11/3-402.12) +
# aviso al consumidor (3-603.11)
POR_CELDA[('03', 'Temperaturas y Trazabilidad', 'B20')] = (
    'Raw fish for aguachiles and tostadas — parasite destruction (FDA Food Code 3-402.11): confirm it was frozen and '
    'stored at −4 °F or below for 7 days, or frozen at −31 °F or below until solid and stored at −31 °F or below for '
    '15 h, or frozen at −31 °F or below until solid and stored at −4 °F or below for 24 h; keep the record 90 days '
    '(FDA Food Code 3-402.12) and the consumer advisory on the menu (FDA Food Code 3-603.11)')
# fichajes FLSA (B16 del base: 29 CFR 516.5-516.6)
POR_CELDA[('05', 'Tareas Semanales Manager', 'B16')] = (
    "Review, approve and file the week's time-clock punches (FLSA minimum: time cards 2 years, payroll 3 years; some "
    'states require longer, e.g. NY 6)')
POR_CELDA[('07', 'Tareas Mensuales', 'B13')] = _base.POR_CELDA[('03', 'Mensual Manager', 'B16')]
for _fila, (_mes, _evento, _antel, _dir) in CALENDARIO.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'A%d' % _fila)] = _mes
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'B%d' % _fila)] = _evento
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'D%d' % _fila)] = _antel

# ==========================================================================
# ADAPTAR (en español, con el dato US; las cifras y normas salen de REGLAS_US). Toda celda ES con °C lleva el suyo
# (cruzar_censo lo exige).
# ==========================================================================
_A = _base.ADAPTAR
_FRIO = _A[('01', 'Apertura Cocina', 'B21')]                  # 41 °F / 0 °F, «— log reading: ____ °F»
_CALIENTE = ('Mantenimiento en caliente (steam table): 135 °F o más (FDA Food Code 3-501.16); si la tarea pide '
             'lectura, coletilla «— log reading: ____ °F»')
_CONO = ('Cono (cone) recibido: congelado a 0 °F o menos o refrigerado a 41 °F o menos (FDA Food Code 3-501.16); si '
         'la tarea pide lectura, «____ °F»')
_TROMPO = ('Al pastor en el trompo (vertical broiler): la capa que se corta, al menos 145 °F (cerdo entero en capas, '
           'FDA Food Code 3-401.11) o la cifra de tu condado si es más estricta (algunos piden 155 °F); los 70 °C del ES '
           'NO se convierten (son la guía española); coletilla «— log reading: ____ °F»')
_LIMITE = (_HACCP_KIT + '; la hora límite la fija tu plan HACCP o tu departamento de salud (sin cifra)')
_TROMPO_LIMITE = (_LIMITE + '; en el trompo, también el tiempo máximo en el broiler que fije tu condado')
_SALSA_TCS = ('Pico de gallo y salsas con tomate cortado son TCS (FDA Food Code 1-201.10): a 41 °F o menos; el '
              'guacamole, trátalo como TCS; si la barra no mantiene 41 °F, time as a public health control con '
              'procedimiento escrito: hora de puesta marcada y descarte a las 4 h (FDA Food Code 3-501.19). Coletilla '
              '«— log reading: ____ °F» si la tarea pide lectura')
_RECALENTAR = ('Recalentado para mantener en caliente: 165 °F durante 15 s en el centro, en 2 h como máximo (FDA Food '
               'Code 3-403.11); sin la «1 hora» ni los 74 °C del ES')
_ENFRIAR = ('Enfriado (sin «abatir»): de 135 °F a 70 °F en 2 h y a 41 °F en 4 h más (FDA Food Code 3-501.14); tapado y '
            'con date marking: 7 días como máximo a 41 °F, día 1 = el de preparación (FDA Food Code 3-501.17)')
_POLLO = 'Aves: 165 °F en el centro, instantáneo (FDA Food Code 3-401.11); sin «74 °C durante ≥ 1 s»'
_MASA = ('La masa fresca y el nixtamal son alimento vegetal tratado por calor, TCS (FDA Food Code 1-201.10): a 41 °F o '
         'menos, o time as a public health control con procedimiento escrito (FDA Food Code 3-501.19); si la tarea '
         'pide lectura, coletilla «— log reading: ____ °F»')
_TIRA = 'sanitizante aprobado a la concentración de la etiqueta, medida con tira (test strip) (FDA Food Code 4-501.114)'
_ALERGENOS = ('Alérgenos US: los 9 principales (FALCPA + FASTER Act: leche, huevo, pescado, crustáceos, frutos de '
              'cáscara, cacahuete, trigo, soja y sésamo); en una taquería: salsa macha = cacahuete y/o sésamo, moles = '
              'frutos de cáscara, cacahuete o sésamo según la receta, tortilla de harina = trigo, queso y crema = '
              'leche; en UK, los 14')
_GLUTEN = ('Trigo, no «gluten»: el alérgeno US es el trigo (wheat). La tortilla de maíz no lleva gluten por receta, '
           'pero con freidora o comal compartidos NO se promete «gluten-free» (21 CFR 101.91)')
_AVISO = ('Aviso ESCRITO de los alérgenos principales en lo que se sirve sin envasar (carta, cartel o tarjeta), donde tu '
          'estado haya adoptado el FDA Food Code 2022 (3-602.12(C)); sin «14 de declaración obligatoria» ni «gratuita»')
_PROPINAS = ('Propinas: según tu política escrita de tip pool; los managers y supervisors no se quedan propinas (FLSA, '
             '29 U.S.C. 203(m)(2)(B))')
_DELIVERY = ('Bolsa térmica (insulated delivery bag): lo caliente a 135 °F o más y lo frío aparte a 41 °F o menos (FDA '
             'Food Code 3-501.16); coletilla «— log reading: ____ °F»')
_APPS = 'Plataformas US: DoorDash, Uber Eats y Grubhub (third-party delivery apps)'
_LAVAR = 'lavar, aclarar y sanitizar con ' + _TIRA + '; el lavado es lo que quita el alérgeno, no el sanitizante'
ADAPTAR = OrderedDict([
    # 01 · Apertura
    (_AP + ('B6',), _FRIO + '; carne marinada en el walk-in'),
    (_AP + ('B7',), _FRIO), (_AP + ('B8',), _FRIO), (_AP + ('B9',), _SALSA_TCS),
    (_AP + ('B13',), _A[('01', 'Apertura Cocina', 'B14')]),
    (_AP + ('B20',), _SALSA_TCS), (_AP + ('B21',), _ALERGENOS + '; cartel = allergen sign'),
    (_AP + ('B27',), _CALIENTE), (_AP + ('B35',), _APPS),
    # 01 · Cierre
    (('01', 'Cierre Taquería', 'B7'), 'Carne sobrante del trompo: reutilizarla solo si tu departamento de salud lo '
                                      'permite (la regla del cono sobrante la fija el condado); si se guarda: ' + _ENFRIAR),
    (('01', 'Cierre Taquería', 'B15'), _ENFRIAR),
    (('01', 'Cierre Taquería', 'B19'), 'Barra de salsas: limpiar y luego sanitizar con ' + _TIRA),
    (('01', 'Cierre Taquería', 'B21'), 'Licuadora y molcajete: ' + _LAVAR),
    (('01', 'Cierre Taquería', 'B26'), 'Arqueo → cash count; descuadre → over/short (cash drawer contra el POS Z report)'),
    (('01', 'Cierre Taquería', 'B27'), _PROPINAS),
    # 02
    (('02', 'Marinado y Montaje del Trompo', 'B7'), _FRIO + '; el tiempo de marinado, el de tu receta (sin cifra)'),
    (('02', 'Marinado y Montaje del Trompo', 'B11'), _FRIO),
    (('02', 'Marinado y Montaje del Trompo', 'B13'), _CONO),
    (('02', 'Marinado y Montaje del Trompo', 'B15'), _TROMPO_LIMITE),
    (('02', 'Marinado y Montaje del Trompo', 'B18'), _TROMPO),
    (('02', 'Corte, Plancha y Comal', 'B6'), _TROMPO),
    (('02', 'Corte, Plancha y Comal', 'B9'), _TROMPO_LIMITE),
    (('02', 'Corte, Plancha y Comal', 'B12'), _CALIENTE),
    (('02', 'Corte, Plancha y Comal', 'B24'), _GLUTEN),
    # 03
    (('03', 'Temperaturas y Trazabilidad', 'B6'), _FRIO), (('03', 'Temperaturas y Trazabilidad', 'B7'), _FRIO),
    (('03', 'Temperaturas y Trazabilidad', 'B9'), _CALIENTE),
    (('03', 'Temperaturas y Trazabilidad', 'B10'), _SALSA_TCS),
    (('03', 'Temperaturas y Trazabilidad', 'B15'), _CONO),
    (('03', 'Temperaturas y Trazabilidad', 'B23'), _RECALENTAR),
    (('03', 'Temperaturas y Trazabilidad', 'B24'), _RECALENTAR),
    (('03', 'Temperaturas y Trazabilidad', 'B25'), _RECALENTAR),
    (('03', 'Barra de Salsas', 'B6'), _SALSA_TCS), (('03', 'Barra de Salsas', 'B7'), _SALSA_TCS),
    (('03', 'Barra de Salsas', 'B9'), _ALERGENOS), (('03', 'Barra de Salsas', 'B16'), _SALSA_TCS),
    (('03', 'Barra de Salsas', 'B21'), 'Recipientes: limpiar y luego sanitizar con ' + _TIRA),
    (('03', 'Alérgenos y Cruzada', 'B9'), 'Licuadora y molcajete tras la salsa macha: ' + _LAVAR),
    (('03', 'Alérgenos y Cruzada', 'B11'), _GLUTEN), (('03', 'Alérgenos y Cruzada', 'B16'), _ALERGENOS),
    (('03', 'Alérgenos y Cruzada', 'B20'), _ALERGENOS), (('03', 'Alérgenos y Cruzada', 'B22'), _AVISO),
    # 04
    (('04', 'Nixtamal y Molienda', 'B12'), 'Molino: limpiar y luego sanitizar con ' + _TIRA),
    (('04', 'Nixtamal y Molienda', 'B13'), _MASA), (('04', 'Nixtamal y Molienda', 'B18'), _LIMITE + '. ' + _MASA),
    (('04', 'Nixtamal y Molienda', 'B21'), _MASA), (('04', 'Nixtamal y Molienda', 'B22'), _LIMITE),
    (('04', 'Guisados y Rotación', 'B8'), _POLLO), (('04', 'Guisados y Rotación', 'B11'), _CALIENTE),
    (('04', 'Guisados y Rotación', 'B14'), _RECALENTAR), (('04', 'Guisados y Rotación', 'B17'), _LIMITE),
    (('04', 'Guisados y Rotación', 'B18'), _ENFRIAR),
    # 05
    (('05', 'Tareas Diarias Manager', 'B18'), 'Arqueo y cuadre → cash count y over/short; ' + _PROPINAS),
    (('05', 'Tareas Diarias Manager', 'B20'), 'Plataformas US: Google y Yelp'),
    (('05', 'Tareas Semanales Manager', 'B6'), _DISTRIBUIDOR),
    (('05', 'Tareas Semanales Manager', 'B9'), _ALCOHOL),
    # 06
    (('06', 'Taquero del Trompo', 'B6'), _CONO), (('06', 'Taquero del Trompo', 'B8'), _TROMPO),
    (('06', 'Taquero del Trompo', 'B12'), _CALIENTE),
    (('06', 'Tortillería', 'B7'), 'Molino: limpiar y luego sanitizar con ' + _TIRA),
    (('06', 'Tortillería', 'B8'), _MASA), (('06', 'Tortillería', 'B9'), _LIMITE),
    (('06', 'Salsas', 'B9'), _SALSA_TCS), (('06', 'Salsas', 'B14'), _LAVAR),
    (('06', 'Mostrador y Caja', 'B7'), _AVISO),
    (('06', 'Mostrador y Caja', 'B11'), 'Ticket → receipt, con el sales tax desglosado'),
    (('06', 'Reparto y Delivery', 'B6'), 'Precinto de garantía → tamper-evident seal (etiqueta o bolsa sellada)'),
    (('06', 'Reparto y Delivery', 'B8'), _DELIVERY),
    # 07
    (('07', 'Tareas Semanales', 'B6'), _CAMPANA), (('07', 'Tareas Semanales', 'B10'),
                                                    'Barra de salsas y utensilios: limpiar y luego sanitizar con ' + _TIRA),
    (('07', 'Tareas Semanales', 'B12'), 'Control de plagas por un licensed pest control operator; el equipo revisa '
                                        'señales en el almacén seco'),
    (('07', 'Tareas Semanales', 'B15'), _ALCOHOL),
    (('07', 'Tareas Mensuales', 'B6'), _GAS), (('07', 'Tareas Mensuales', 'B7'), _A[('05', 'Trimestral y Anual', 'B23')]),
    (('07', 'Tareas Mensuales', 'B8'), _CAMPANA), (('07', 'Tareas Mensuales', 'B9'), _GAS + '. ' + _CAMPANA),
    (('07', 'Tareas Mensuales', 'A10'), _HACCP_KIT), (('07', 'Tareas Mensuales', 'B11'), _HACCP_KIT),
    (('07', 'Tareas Mensuales', 'B16'), _DISTRIBUIDOR), (('07', 'Tareas Mensuales', 'B19'), _ALCOHOL),
    # 08 · Temporadas: proveedores US
    (('08', 'Temporadas y Producto', 'B6'), _DISTRIBUIDOR + '; nuez de Castilla → fresh walnuts'),
    # 08 · Calendario de Eventos: las fechas españolas pasan a su equivalente US; las mexicanas se quedan
    (('08', 'Calendario de Eventos', 'B6'), 'Three Kings Day (6-ene): rosca de Reyes (escrito así) y turno reforzado'),
    (('08', 'Calendario de Eventos', 'B8'), 'Viernes de Cuaresma (Lent Fridays): tacos de pescado y capeados (battered '
                                            'fish); para el pescado crudo, el registro de destrucción de parásitos '
                                            '(FDA Food Code 3-402.11)'),
    (('08', 'Calendario de Eventos', 'B9'), 'Sustituye a Semana Santa: «Holy Week & Easter (varies)»: revisar aforo y '
                                            'previsión con el equipo; decidir el horario del domingo de Pascua'),
    (('08', 'Calendario de Eventos', 'B11'), 'Cinco de Mayo: en EE. UU. es de los días más fuertes del año para una '
                                             'taquería [criterio del kit]; en México se celebra sobre todo en Puebla'),
    (('08', 'Calendario de Eventos', 'B12'), 'Sustituye a las terrazas: «Patio season»: permiso de la ciudad (outdoor '
                                             'dining / sidewalk cafe permit), aforo y horario ampliado'),
    (('08', 'Calendario de Eventos', 'B13'), 'Sustituye al inicio de verano: «Memorial Day weekend (last Monday of '
                                             'May)»: previsión de clientes, grupos y pedidos grandes'),
    (('08', 'Calendario de Eventos', 'B16'), 'Grito e Independencia (15-16 sep): fecha fuerte para la clientela '
                                             'mexicana y latina de EE. UU.; pozole; ' + _ALCOHOL),
    (('08', 'Calendario de Eventos', 'B22'), 'Posadas (16-24 dic) y fiestas de empresa (holiday parties: bandejas y '
                                             'taco bar para oficinas): cerrar aforos y menús cerrados'),
    # BONUS-01
    (('B01', 'Briefing Pre-Servicio', 'B5'), 'kg → lb'),
    (('B01', 'Briefing Pre-Servicio', 'B7'), _LIMITE),
    (('B01', 'Briefing Pre-Servicio', 'B25'), 'Mole: frutos de cáscara, cacahuete o sésamo según la receta'),
    (('B01', 'Briefing Pre-Servicio', 'B26'), 'Tortilla de harina = trigo (wheat), no «gluten»'),
    # BONUS-02 · Instrucciones
    (('B02', 'Instrucciones', 'B6'), 'A4 apaisado → US Letter apaisado (landscape)'),
    (('B02', 'Instrucciones', 'B8'), _A[('B02', 'Instrucciones', 'B8')]),
])
for _fila, (_mes, _evento, _antel, _dir) in CALENDARIO.items():
    if _dir:
        ADAPTAR[(HOJA_CAL[0], HOJA_CAL[1], 'C%d' % _fila)] = 'Evento EN: «%s». %s' % (_evento, _dir)
# aplicar_en.objetivo_ajuste / G3: la EN activa el ajuste también donde el ES tampoco cabía (lección de la pizzería)
AJUSTE_MAQUETA_ES = True
# Celdas ES con °C cuya EN NO lleva cifra en °F: ninguna (todas llevan su ADAPTAR o su POR_CELDA)
CELSIUS_SIN_F = frozenset()

# ==========================================================================
# REGLAS_US: las del base + las de la taquería (fuente única de las cifras y normas que el kit puede afirmar)
# ==========================================================================
REGLAS_US = OrderedDict(_base.REGLAS_US)
REGLAS_US.update([
    ('trompo', ('al pastor (cerdo entero en capas) ≥ 145 °F 15 s en la capa que se corta; la cifra del condado si es más '
                'estricta (algunos piden 155 °F); el tiempo máximo en el broiler y el cono sobrante, los del condado',
                'FDA Food Code 2022 §3-401.11(A)(1); [local] guías de vertical broiler (research US §6.2: Sacramento y '
                'Orange 145 °F; Alameda y Marin 155 °F)')),
    ('aves', ('aves 165 °F instantáneo', 'FDA Food Code 2022 §3-401.11(A)(3)')),
    ('tcs_vegetal', ('tomate cortado (pico de gallo, salsas frescas) y alimento vegetal tratado por calor (masa fresca, '
                     'nixtamal) = TCS; guacamole tratado como TCS', 'FDA Food Code 2022 §1-201.10 (definición de TCS); '
                     '[criterio del kit] guacamole (research US §6.1)')),
    ('tphc', ('time as a public health control: procedimiento escrito; hora marcada; servir o descartar DENTRO de las 4 h',
              'FDA Food Code 2022 §3-501.19(B)')),
    ('aviso_alergenos', ('aviso escrito de los alérgenos principales en lo que se sirve sin envasar, donde se haya '
                         'adoptado el Food Code 2022', 'FDA Food Code 2022 §3-602.12(C)')),
    ('alergenos_taqueria', ('salsa macha = cacahuete y/o sésamo; moles = frutos de cáscara, cacahuete, sésamo; tortilla '
                            'de harina = trigo; queso y crema = leche', 'FALCPA 2004 + FASTER Act 2021; research US §6.5')),
    ('gluten_free', ('no prometer «gluten-free» con freidora o comal compartidos con la tortilla de harina',
                     '21 CFR 101.91')),
    ('propinas_pool', ('managers y supervisors no se quedan propinas del equipo', 'FLSA, 29 U.S.C. 203(m)(2)(B)')),
    ('delivery', ('bolsa térmica: lo caliente a 135 °F o más y lo frío a 41 °F o menos', 'FDA Food Code 2022 §3-501.16')),
    ('licencia_alcohol', ('mezcal, tequila y cerveza solo con la licencia estatal / local', '[estatal] ABC / liquor '
                          'authority (research US §6.7)')),
    ('edad_alcohol', ('21 años para comprar o consumir alcohol, en todos los estados',
                      'National Minimum Drinking Age Act of 1984 (23 U.S.C. 158)')),
    ('gas', ('instalación de gas revisada por un profesional con licencia con la frecuencia del código local; el '
             'personal, solo la inspección visual', '[local] código de gas y fire code (como el base, 05 B10)')),
    ('calibracion', ('calibración de termómetros por el punto de hielo (32 °F)', '[criterio del kit] método; FDA Food '
                     'Code 2022 §4-502.11(B)')),
    ('dias_fuertes', ('Cinco de Mayo, Super Bowl, viernes de Cuaresma, Grito (15-16 sep), Día de Muertos, Guadalupe '
                      '(12 dic), Posadas: días fuertes de una taquería US', '[criterio del kit] calendario comercial; '
                      'research ES §7.3 (Cinco de Mayo, fiesta sobre todo de EE. UU.)')),
    ('unidades', ('kg → lb, litros → qt', '[criterio del kit] conversión')),
])
# °F que el kit puede afirmar (G7): las del base que usa la taquería + 32 (calibración) + 145 / 155 (trompo)
GRADOS_F_SPEC = {-31, -4, 0, 32, 41, 70, 135, 145, 155, 165}

# ==========================================================================
# Pistas y dependencias de la taquería (extraer_textos.py)
# ==========================================================================
PISTAS_CAMBIO = {r'Kit de Tareas': 'D2: «Taco Shop Checklists Kit Pro»'}
PISTAS_FUERA = (r'Restaurante Casual',)
PISTAS_EXTRA = [
    (r'Taquería|[Tt]aquería', 'D2: sin el sufijo «— Taquería Mexicana»; taquería → taco shop (nombre) / taqueria (sin '
                              'tilde, en prosa); nunca «Tex-Mex» ni «restaurant»'),
    (r'[Tt]rompo|[Aa]sador vertical|[Cc]ono\b', 'trompo → trompo; asador vertical → vertical broiler; cono → cone '
                                                '(stack); montar el trompo → stack the trompo; cortar → carve / slice'),
    (r'[Pp]astor', 'al pastor → al pastor (tacos al pastor; nunca «pastor style»)'),
    (r'[Pp]lancha', 'plancha → flat-top griddle / griddle (NUNCA «plancha»); el puesto «Plancha» → griddle cook'),
    (r'[Cc]omal|[Tt]ortillador|[Tt]ortiller', 'comal → comal; tortilladora → tortilla machine; prensa → tortilla '
                                              'press; tortillería → tortilleria; tortillero/a → tortilla maker; cajón '
                                              'térmico → tortilla warmer'),
    (r'[Nn]ixtamal|[Mm]olino|[Mm]olienda|\bcal\b|[Mm]asa\b', 'nixtamal → nixtamal; masa → masa; molino → corn mill '
                                                             '(molino); moler → grind; cal → food-grade lime (cal); '
                                                             'harina de maíz nixtamalizado → masa harina'),
    (r'[Gg]uisado|[Cc]azuela', 'guisados (cazuelas de relleno) → guisados (stews in clay pots / hotel pans)'),
    (r'[Bb]año maría', 'baño maría → steam table'),
    (r'[Bb]arra (de salsas|fría)|[Bb]arra\b', 'barra de salsas → salsa bar; barra fría → cold salsa bar; la zona «Barra» '
                                              '→ salsa bar (no es una barra de bar)'),
    (r'[Mm]acha', 'salsa macha → salsa macha (peanuts and/or sesame: los dos son alérgenos principales US)'),
    (r'[Mm]olcajete|[Ll]icuadora', 'molcajete → molcajete; licuadora → blender'),
    (r'[Tt]otopos|[Cc]apeados|[Tt]ostadas?|[Aa]guachile', 'totopos → tortilla chips; capeados → battered (fish); '
                                                          'tostadas y aguachiles → tostadas, aguachile'),
    (r'[Ee]scandallo|[Rr]endimiento', 'escandallo (costeo) → taco costing / food cost per taco; rendimiento → yield '
                                      '(trompo yield, tacos per pound)'),
    (r'\bkg\b|kilo|litros?', 'kg → lb; tacos por kilo → tacos per pound; litros → quarts (qt)'),
    (r'[Mm]ermas?', 'mermas → waste (waste log)'),
    (r'[Gg]luten', 'el alérgeno US es el trigo (wheat): «tortilla de harina (gluten)» → «flour tortilla (wheat)»; '
                   'nunca prometer «gluten-free»'),
    (r'[Ii]mportador|[Ii]mportación', 'importador → Mexican food distributor (en EE. UU. no se importa)'),
    (r'[Aa]lbar[aá]n|[Cc]aducidad', 'albarán → invoice / packing slip; caducidad → use-by / expiration date'),
    (r'[Aa]batir|[Aa]batid', 'abatir → cool (enfriado 135 → 70 °F en 2 h y → 41 °F en 4 h más, FDA Food Code '
                             '3-501.14); abatidor → blast chiller'),
    (r'PEPS', 'PEPS → FIFO'),
    (r'[Mm]ezcal|[Tt]equila|[Bb]ebida', 'mezcal, tequila y cerveza solo con licencia de alcohol, 21+ con ID'),
    (r'[Rr]epartidor|[Dd]elivery|[Aa]pps', 'repartidor → delivery driver; apps de delivery → DoorDash, Uber Eats, '
                                           'Grubhub; bolsa térmica → insulated delivery bag'),
    (r'[Pp]ropinas', 'propinas → tips (tip pool por escrito; managers fuera del pool)'),
    (r'[Ee]ncargad', 'encargado/a → shift manager (NUNCA «shift lead»); el responsable sanitario = person in charge'),
    (r'[Mm]ostrador', 'mostrador → counter; el puesto «Mostrador» → counter (staff)'),
    (r'[Ss]alsero', 'salsero/a → salsa prep cook'),
    (r'[Cc]omanda', 'comanda → ticket; 86 → 86\'d'),
    (r'[Rr]eseñas|redes|RRSS', 'reseñas → reviews (Google, Yelp); redes → social media'),
    (r'Reyes|rosca', 'Día de Reyes → Three Kings Day; rosca → rosca de Reyes (con R mayúscula, así)'),
    (r'[Mm]uertos', 'Día de Muertos → Day of the Dead (sin tilde ni «Día»); pan de muerto → pan de muerto (así)'),
    (r'Grito|Guadalupe|Posadas|Candelaria', 'Grito → the Grito / Mexican Independence Day (nunca «El Grito»: el '
                                            'gate lee «el» como español); Virgen de Guadalupe → Our Lady of '
                                            'Guadalupe; Posadas → Posadas; Candelaria → Candelaria (Candlemas)'),
    (r'[Nn]ogada|[Nn]uez de Castilla|panochera|lechera|criollo', 'chiles en nogada → chiles en nogada; nuez de '
                                                                 'Castilla → fresh walnuts; manzana panochera, pera '
                                                                 'lechera, durazno criollo → panochera apples, '
                                                                 'lechera pears, criollo peaches'),
]
DEPENDENCIAS_EXTRA = OrderedDict([
    ('variante', ('Sufijo de variante «Taquería Mexicana»', r'Taquería Mexicana', 'D2: la EN no lleva sufijo')),
    ('trompo', ('Trompo: cocción, corte y cono', r'[Tt]rompo|[Aa]sador vertical|[Cc]ono\b',
                'D-TAC: 145 °F o la cifra del condado (3-401.11); límites del condado')),
    ('masa', ('Nixtamal, masa y tortilla', r'[Nn]ixtamal|[Mm]asa\b|[Mm]olino', 'D-TAC: masa TCS (1-201.10), 41 °F o '
              'TPHC')),
    ('salsas', ('Salsas crudas y barra de salsas', r'[Ss]alsas? crudas?|[Bb]arra (de salsas|fría)|guacamole|pico de gallo',
                'D-TAC: TCS 41 °F o TPHC 4 h (3-501.19)')),
    ('alcohol', ('Alcohol en la taquería', r'[Mm]ezcal|[Tt]equila|[Cc]erveza', 'D-TAC: solo con licencia, 21+ con ID')),
    ('delivery', ('Reparto propio y apps', r'[Rr]epartidor|[Bb]olsas? térmicas?|apps', 'D-TAC: bolsa 135 / 41 °F, apps '
                  'US')),
    ('importacion', ('Importador de producto mexicano', r'[Ii]mportador|[Ii]mportación', 'D-TAC: Mexican food '
                     'distributor')),
])


def _rebind(f):
    return types.FunctionType(f.__code__, globals(), f.__name__, f.__defaults__, f.__closure__)


titulo_interior = _rebind(_base.titulo_interior)
_autotest_base = _rebind(_base.autotest)
_cruzar_censo_base = _rebind(_base.cruzar_censo)
_SIN_CAJA = ('DENOMINACIONES debe tener las 15 filas del ES',)   # D12: la taquería no tiene libro de caja
RX_F = re.compile(r'(−?\d+)(?:–(−?\d+))? °F')


def _grados(textos):
    out = set()
    for t in textos:
        for m in RX_F.finditer(t):
            for g in m.groups():
                if g:
                    out.add(int(g.replace('−', '-')))
    return out


def autotest():
    err = [e for e in _autotest_base() if e not in _SIN_CAJA]
    if HOJA_CAJA is not None or DENOMINACIONES or FORMULAS_POR_CELDA:
        err.append('la taquería no tiene caja: HOJA_CAJA None y sin denominaciones ni fórmulas por celda')
    rx = re.compile(TERMINOS_PROHIBIDOS)
    if not rx.search(TERMINO_PROHIBIDO_EJEMPLO):
        err.append('TERMINO_PROHIBIDO_EJEMPLO no lo caza TERMINOS_PROHIBIDOS')
    for ok in ('sidewalk cafe permit', 'restaurant consultant', 'flat-top griddle', 'tacos al pastor'):
        if rx.search(ok):
            err.append('TERMINOS_PROHIBIDOS caza lo permitido: %r' % ok)
    for k, v in list(GLOSARIO.items()) + list(POR_CELDA.items()) + list(CLAVES.items()) + list(HOJAS.items()):
        if (k not in _base.GLOSARIO or k in _GLOSARIO_TACO) and isinstance(v, str) and rx.search(v):
            if k in _base.HOJAS and k not in HOJAS_ES_POR_LIBRO_TODAS:
                continue
            err.append('texto EN fijado con un término prohibido: %r → %r' % (k, v))
    for es in HOJAS_ES_POR_LIBRO_TODAS:
        if ',' in HOJAS[es]:
            err.append('pestaña con coma (rompe el área de impresión): %r' % HOJAS[es])
    if CITA_AUTOTEST.strip('()').split()[-1] in ' '.join(f for _v, f in REGLAS_US.values()):
        err.append('CITA_AUTOTEST está en REGLAS_US: G7 no la cazaría')
    # G7: los °F que dicen POR_CELDA, ADAPTAR y las reglas propias de la taquería son exactamente GRADOS_F_SPEC
    usados = _grados(list(POR_CELDA.values()) + list(ADAPTAR.values())
                     + [v for k, (v, _f) in REGLAS_US.items() if k not in _base.REGLAS_US])
    if usados != GRADOS_F_SPEC:
        err.append('GRADOS_F_SPEC ≠ los °F de POR_CELDA / ADAPTAR / reglas de la taquería: sobra %s, falta %s'
                   % (sorted(GRADOS_F_SPEC - usados), sorted(usados - GRADOS_F_SPEC)))
    for f in FRASES_OK_EXTRA:                                    # solo platos con palabra funcional ES (si no, sobra)
        if not re.search(r'\b(?:al|de|del|con|en)\b', f.lower()):
            err.append('FRASES_OK_EXTRA sin palabra funcional ES (no hace falta): %r' % f)
    return err


HOJAS_ES_POR_LIBRO_TODAS = frozenset(h for hs in HOJAS_ES_POR_LIBRO.values() for h in hs)


def cruzar_censo(p):
    import json
    err = _cruzar_censo_base(p)
    censo = json.load(open(p, encoding='utf-8'))
    tx = {}
    for info in censo['libros'].values():
        for h, hd in info['hojas_detalle'].items():
            for coord, t in hd.get('textos', {}).items():
                tx[(info['corto'], h, coord)] = t
    # toda celda ES con °C lleva ADAPTAR o POR_CELDA (o está declarada en CELSIUS_SIN_F)
    for k, t in tx.items():
        if '°C' in t and k not in ADAPTAR and k not in POR_CELDA and k not in CELSIUS_SIN_F:
            err.append('celda ES con °C sin ADAPTAR ni POR_CELDA: %r → %r' % (k, t[:70]))
    # lo que POR_CELDA reescribe es lo que el ES dice en esa celda
    esperado = [(_AP + ('B14',), 'Montar el trompo del día'), (_AP + ('B15',), 'Comprobar el cono recibido'),
                (('03', 'Temperaturas y Trazabilidad', 'B20'), 'Verificar la congelación del pescado crudo'),
                (('05', 'Tareas Semanales Manager', 'B16'), 'Cerrar y firmar el registro de jornada'),
                (('07', 'Tareas Mensuales', 'B13'), 'Revisar el registro de jornada')]
    for k, ini in esperado:
        if not tx.get(k, '').startswith(ini):
            err.append('POR_CELDA %r: el ES no empieza por %r (trae %r)' % (k, ini, tx.get(k)))
    for fila in FILAS_CALENDARIO:
        if not tx.get((HOJA_CAL[0], HOJA_CAL[1], 'C%d' % fila)):
            err.append('B02: la fila %d no trae tareas (C) en el ES' % fila)
    if tx.get((HOJA_CAL[0], HOJA_CAL[1], 'A%d' % (FILAS_CALENDARIO[-1] + 1))) != '(Tu fecha)':
        err.append('B02: tras la fila %d no empiezan las filas libres' % FILAS_CALENDARIO[-1])
    return err


CITA_AUTOTEST = '(FDA Food Code 3-501.18)'                     # autotest G7: una cita que NO está en REGLAS_US


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
    for x in e:
        print('ERROR', x)
    print('mapas_taco.py: {} ficheros · {} pestañas · {} glosario · {} por celda · {} adaptar · {} reglas · '
          '{} errores'.format(len(FICHEROS), len(HOJAS), len(GLOSARIO), len(POR_CELDA), len(ADAPTAR), len(REGLAS_US),
                              len(e)))
    raise SystemExit(1 if e else 0)
