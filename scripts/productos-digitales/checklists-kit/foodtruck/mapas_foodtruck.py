#!/usr/bin/env python3
"""
mapas_foodtruck.py — Food Truck Checklists Kit Pro (EN) · DELTA del Kit de Tareas Recurrentes: Food Truck
(`kit-tareas-food-truck`, 11 xlsx v1.1, origen ChefBusiness) sobre `mapas.py` (Restaurant Checklists Kit Pro). SPEC:
`foodtruck/SPEC.md` (solo el delta). Duodécimo hermano vertical y el PRIMERO en el MOLDE PLANO (SPEC §0): una hoja por
libro, cabecera en la fila 3, sin columna Nº, sin hoja «Instrucciones», sin contadores ni fórmulas, sin protección, sin
línea de versión; A1 = marca, A2 = título, última fila = línea de marca. Sesión Claude Code, 31-oct-2026.

Se usa con `--kit foodtruck` (kit.py). Importa `mapas.py` y SOLO añade o sobrescribe: producto, ficheros, títulos (el
título interior va en A2 por POR_CELDA), pestañas, glosario de food truck (cabeceras de las 11 hojas, fases, crew,
window staff, driver / tech, pre-trip, frecuencias, prioridades, duraciones), calendario (B02 propio: A mes · B
eventos · C menú · D mantenimiento · E marketing, filas 4-15), POR_CELDA (cabeceras C3/D3 cruzadas del 02 y el 03,
temperaturas de cocción FDA, permisos y seguros US, eventos españoles del 08 → US), ADAPTAR (°F, agua potable y
residual, propano, generador, extintores, vehículo, permisos, alérgenos, caja) y REGLAS_US. Sin caja: `HOJA_CAJA =
None`, `DENOMINACIONES` y `FORMULAS_POR_CELDA` vacíos (como la taquería). Las funciones del base que leen constantes
(titulo_interior, autotest, cruzar_censo) se re-enlazan a ESTE módulo. Ejecutado como script: autotest + cruce con
foodtruck/censo_es.json.

    python3 foodtruck/mapas_foodtruck.py
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
AQUI = os.path.dirname(os.path.abspath(__file__))              # foodtruck/ (el import * trae el AQUI del base)

ORIGEN_ES = 'kit-tareas-food-truck'
PRODUCTO = 'Food Truck Checklists Kit Pro'
TITULO_SEO = 'Food Truck Checklists Kit Pro: Inspection, Setup & Teardown Checklist Templates for Excel'
SLUG = 'food-truck-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_FOOD_TRUCK_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
VERSION_ES = '1.1'                                               # productos-changelog.ts: kit-tareas-food-truck 1.1
# Marca (D19 + precedente D34 del Restaurant Business Plan Kit): A1 «ChefBusiness Consultoria Gastronomica» → «AI Chef
# Pro» (GLOSARIO) y la última fila de cada hoja, la línea de marca
MARCA_ES = 'ChefBusiness.co — Kit de Tareas Recurrentes: Food Truck'
MARCA_EN = 'AI Chef Pro · aichef.pro — ' + PRODUCTO
VARIANTES_ES = ('— Food Truck',)
# Molde PLANO (SPEC §0): lo leen los ganchos de la F2 en aplicar_en.py y gates_en.py (título interior en A2 de la única
# hoja, sin hoja de instrucciones ni línea de versión, tareas sin número en A). Hasta entonces, solo documentan.
MOLDE = 'plano'
CELDA_TITULO = 'A2'
FILA_CABECERA = 3
# heredar.py: memoria con VARIAS fuentes (la primera que acierta gana): el base y los hermanos de eventos y mostrador.
# El molde y la fuente (ChefBusiness, sin tildes) son otros: se espera una herencia casi nula (SPEC §4)
_SUF = lambda v: [(' — Food Truck', ' — ' + v)]                  # noqa: E731
MEMORIA = [('base', '', _SUF('Restaurante Casual')), ('catering', 'catering', _SUF('Catering / Eventos')),
           ('taco', 'taco', _SUF('Taquería Mexicana')), ('burger', 'burger', _SUF('Hamburguesería')),
           ('ghost', 'ghost', _SUF('Dark Kitchen'))]
# heredar.py: EN heredado que en un food truck no vale tal cual → pendientes (motivo «contexto»)
RX_CONTEXTO_PENDIENTE = (r'(?i)\b(?:restaurants?(?! consultant)|host stands?|head chefs?|sous chefs?|MOD|FOH|'
                         r'servers?|bartenders?|baristas?|bussers?|barbacks?|dining rooms?|walk-ins?|patio|'
                         r'trompo|taquero|banquets?|BEOs?|line-up|shift leads?|pizzerias?|coffee shops?)\b')
NO_HEREDAR = {}
# gates_en.py G2: términos que NINGUNA celda EN del food truck puede llevar: puestos y zonas de un local fijo, el calco
# «plancha» (flat-top griddle) y el butano (en EE. UU. el truck va con propano). «restaurant consultant» queda fuera.
TERMINOS_PROHIBIDOS = (r'(?i:\b(?:restaurants?(?! consultant)|host stands?|head chefs?|sous chefs?|bussers?|'
                       r'barbacks?|bartenders?|baristas?|banquets?|BEOs?|line-up|servers?|dining rooms?|plancha|'
                       r'butane)\b)|\bMOD\b|\bFOH\b|\bITV\b')
TERMINO_PROHIBIDO_EJEMPLO = 'Check the butane cylinder.'
REFERENCIAS_TRADUCTOR = ['foodtruck/SPEC.md', 'SPEC.md §0-§3 y §7.2 (brief)', 'textos_en/glosario.json (glosario de '
                         'la prosa del kit base)', 'foodtruck/mapas_foodtruck.py: GLOSARIO, HOJAS, FICHEROS, TITULOS, '
                         'POR_CELDA, REGLAS_US', '../business-plans-en/F1-research-us.md §5 y SPEC.md §2.3 y §4.2 (jerga '
                         'y trámites del Food Truck Business Plan Kit)', '../GLOSARIO-JERGA-ES-EN.md']
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v' + VERSION_ES),
    ('keywords', 'food truck checklist, food truck inspection checklist, food truck health inspection checklist, '
                 'food truck setup checklist, food truck commissary, pre-trip inspection, AI Chef Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

# ==========================================================================
# Ficheros (D5): DataForSEO US 31-oct: food truck inspection checklist 170 · health inspection checklist 110 · food
# truck checklist 50 · fire inspection checklist 40 · opening 10 · closing / template / setup: sin volumen. PAA de
# «food truck inspection checklist»: «What are the 7 steps for a pre-trip inspection?»
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-setup-teardown-food-truck.xlsx', '01-food-truck-setup-teardown-checklist.xlsx'),
    ('02-operaciones-moviles-vehiculo.xlsx', '02-food-truck-pre-trip-vehicle-checklist.xlsx'),
    ('03-appcc-seguridad-alimentaria-movil.xlsx', '03-food-truck-health-inspection-food-safety-checklist.xlsx'),
    ('04-permisos-eventos-localizaciones.xlsx', '04-food-truck-permits-events-locations-checklist.xlsx'),
    ('05-tareas-manager.xlsx', '05-food-truck-manager-checklist.xlsx'),
    ('06-tareas-perfiles.xlsx', '06-food-truck-duties-by-role.xlsx'),
    ('07-semanales-mensuales.xlsx', '07-food-truck-weekly-monthly-cleaning-maintenance-checklist.xlsx'),
    ('08-eventos-estacionales.xlsx', '08-food-truck-events-seasons-checklist.xlsx'),
    ('09-plantilla-personalizable.xlsx', '09-blank-food-truck-checklist-template.xlsx'),
    ('BONUS-01-briefing-pre-evento.xlsx', 'BONUS-01-food-truck-pre-event-briefing-template.xlsx'),
    ('BONUS-02-calendario-anual.xlsx', 'BONUS-02-food-truck-annual-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)
TITULOS = OrderedDict([
    ('01-food-truck-setup-teardown-checklist.xlsx',
     'Food Truck Setup & Teardown Checklist: Arrival, Kitchen, Service & Closing'),
    ('02-food-truck-pre-trip-vehicle-checklist.xlsx',
     'Food Truck Pre-Trip & Vehicle Checklist: Generator, Propane, Water & Waste'),
    ('03-food-truck-health-inspection-food-safety-checklist.xlsx',
     'Food Truck Food Safety & Health Inspection Prep Checklist (FDA Food Code)'),
    ('04-food-truck-permits-events-locations-checklist.xlsx', 'Food Truck Permits, Events & Locations Checklist'),
    ('05-food-truck-manager-checklist.xlsx', 'Food Truck Manager Checklist: Route, Inventory, Food Cost & Marketing'),
    ('06-food-truck-duties-by-role.xlsx', 'Food Truck Duties by Role: Chef, Prep Cook, Window Staff & Driver'),
    ('07-food-truck-weekly-monthly-cleaning-maintenance-checklist.xlsx',
     'Food Truck Weekly & Monthly Checklists: Deep Cleaning, Maintenance & Inventory'),
    ('08-food-truck-events-seasons-checklist.xlsx',
     'Food Truck Event & Seasonal Checklists: Festivals, Fairs, Markets & Weddings'),
    ('09-blank-food-truck-checklist-template.xlsx', 'Blank Food Truck Checklist Template (Editable)'),
    ('BONUS-01-food-truck-pre-event-briefing-template.xlsx', 'BONUS: Food Truck Pre-Event Briefing Template'),
    ('BONUS-02-food-truck-annual-calendar.xlsx',
     'BONUS: Food Truck Annual Calendar: Events, Menu, Maintenance & Marketing (US)'),
])
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

# Pestañas (D6): ≤ 31 caracteres, sin comas (rompen el área de impresión) ni []:*?/\. Una hoja por libro.
HOJAS = OrderedDict(_base.HOJAS)
HOJAS.update([
    ('Setup y Teardown', 'Setup & Teardown'), ('Operaciones Moviles', 'Vehicle & Mobile Ops'),
    ('APPCC Movil', 'Food Safety & Inspection'), ('Permisos y Eventos', 'Permits & Events'),
    ('Tareas Manager', 'Manager Tasks'), ('Perfiles', 'Duties by Role'), ('Semanales y Mensuales', 'Weekly & Monthly'),
    ('Eventos y Temporadas', 'Events & Seasons'), ('Personalizable', 'Blank Template'),
    ('Briefing Pre-Evento', 'Pre-Event Briefing'), ('Calendario Anual', 'Annual Calendar'),
])
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Setup y Teardown']), ('02', ['Operaciones Moviles']), ('03', ['APPCC Movil']),
    ('04', ['Permisos y Eventos']), ('05', ['Tareas Manager']), ('06', ['Perfiles']), ('07', ['Semanales y Mensuales']),
    ('08', ['Eventos y Temporadas']), ('09', ['Personalizable']), ('B01', ['Briefing Pre-Evento']),
    ('B02', ['Calendario Anual']),
])
HOJA_DE = OrderedDict((c, hs[0]) for c, hs in HOJAS_ES_POR_LIBRO.items())

# ==========================================================================
# GLOSARIO: el base entero (opcional) + las celdas cortas del food truck (celda ENTERA, sin columna: una palabra que es
# fase y responsable lleva un solo EN; los 8 «Servicio» que son PUESTO van por POR_CELDA → «Window staff»). Jerga US del
# Food Truck Business Plan Kit (SPEC §2.3 de business-plans-en): commissary, mobile vending, food handler card.
# ==========================================================================
GLOSARIO = OrderedDict(_base.GLOSARIO)
_GLOSARIO_FT = OrderedDict([
    # marca A1 (precedente D34 del Restaurant Business Plan Kit)
    ('ChefBusiness Consultoria Gastronomica', 'AI Chef Pro'),
    # cabeceras (fila 3) de las 11 hojas
    ('Fase', 'Phase'), ('Tiempo', 'Time'), ('OK', 'OK'), ('Observaciones', 'Notes'), ('Categoria', 'Category'),
    ('Tarea / Control', 'Task / Check'), ('Frecuencia', 'Frequency'), ('Registro', 'Records'),
    ('Detalle / Procedimiento', 'Detail / Procedure'), ('Tipo', 'Type'), ('Tarea / Requisito', 'Task / Requirement'),
    ('Anticipacion', 'Lead time'), ('Prioridad', 'Priority'), ('Estado', 'Status'), ('Perfil', 'Role'),
    ('Momento', 'When'), ('Periodo', 'Period'), ('Dia/Semana', 'Day / Week'), ('Temporada/Evento', 'Season / Event'),
    ('Accion / Tarea', 'Action / Task'), ('Area', 'Area'), ('Seccion', 'Section'), ('Informacion', 'Information'),
    ('Detalle', 'Detail'), ('Mes', 'Month'), ('Tipo Eventos', 'Event Types'), ('Menu Sugerido', 'Suggested Menu'),
    ('Mantenimiento', 'Maintenance'), ('Marketing', 'Marketing'),
    # fases y categorías (columna A)
    ('Llegada', 'Arrival'), ('Cierre', 'Teardown'), ('Vehiculo', 'Vehicle'), ('Generador', 'Generator'),
    ('Gas', 'Propane'), ('Agua', 'Water'), ('Residuos', 'Waste'), ('Temp. frio', 'Cold temps'),
    ('Temp. coccion', 'Cooking temps'), ('Temp. expo', 'Hot holding'), ('Descongelacion', 'Thawing'),
    ('Higiene', 'Hygiene'), ('Superficies', 'Surfaces'), ('Cruzada', 'Cross-contamination'), ('Utensilios', 'Utensils'),
    ('Basura', 'Trash'), ('Alergenos', 'Allergens'), ('Permisos', 'Permits'), ('Licencia', 'License'),
    ('Seguro', 'Insurance'), ('Fiscal', 'Tax'), ('Mercado', 'Market'), ('Festival', 'Festival'),
    ('Corporativo', 'Corporate'), ('Bodas', 'Weddings'), ('Deportivo', 'Sports'), ('Fijo', 'Regular spot'),
    ('Planificacion', 'Planning'), ('Stock', 'Inventory'), ('Calidad', 'Quality'), ('Revenue', 'Revenue'),
    ('Food cost', 'Food cost'), ('Pricing', 'Pricing'), ('Fees', 'Event fees'), ('Caja', 'Cash'),
    ('RRSS', 'Social media'), ('Reviews', 'Reviews'), ('Networking', 'Networking'), ('Fidelizacion', 'Loyalty'),
    ('Ayudante', 'Prep cook'), ('Conductor', 'Driver'), ('Primavera', 'Spring'), ('Verano', 'Summer'),
    ('Otono', 'Fall'), ('Invierno', 'Winter'), ('Bodas temporada', 'Wedding season'), ('Black Friday', 'Black Friday'),
    ('Nochevieja', "New Year's Eve"),
    # responsables (columnas C / D): un truck tiene crew, no sala
    ('Tecnico', 'Driver / tech'), ('Equipo', 'Crew'), ('Encargado', 'Manager'),
    # cuándo, frecuencia, antelación, prioridad, duración
    ('Pre-salida', 'Pre-trip'), ('Post-servicio', 'After service'), ('Pre-evento', 'Pre-event'),
    ('En ruta', 'In transit'), ('Setup', 'Setup'), ('Teardown', 'Teardown'), ('Pre-servicio', 'Before service'),
    ('Continuo', 'Ongoing'), ('Pre/post', 'Before & after'), ('Siempre', 'Always'), ('Cada 2h', 'Every 2 h'),
    ('Diario', 'Daily'), ('2-3x semana', '2–3× a week'), ('3x semana', '3× a week'), ('Permanente', 'Ongoing'),
    ('Segun uso', 'As needed'), ('1a semana', '1st week'), ('2a semana', '2nd week'), ('3a semana', '3rd week'),
    ('4a semana', '4th week'), ('Inicio actividad', 'Before opening'), ('1 semana', '1 week'), ('3 dias', '3 days'),
    ('2 semanas', '2 weeks'), ('1 mes', '1 month'), ('2 meses', '2 months'), ('Alta', 'High'), ('Media', 'Medium'),
    ('2 min', '2 min'), ('3 min', '3 min'), ('5 min', '5 min'), ('10 min', '10 min'), ('15 min', '15 min'),
])
GLOSARIO.update(_GLOSARIO_FT)
GLOSARIO_OPCIONAL = frozenset(_base.GLOSARIO)
PUESTOS_ES = frozenset(_base.PUESTOS_ES | {'Conductor', 'Tecnico', 'Equipo', 'Encargado', 'Ayudante', 'Chef',
                                           'Marketing', 'Cocina', 'Servicio'})

# ==========================================================================
# Sin libro de caja (D12, como la taquería): la caja del día son tareas del 01 (B19, B28), del 05 (B15) y del 06 (B18)
# ==========================================================================
HOJA_CAJA = None
DENOMINACIONES = []
VALORES_DENOMINACION_EN = []
FORMULAS_POR_CELDA = OrderedDict()

# ==========================================================================
# BONUS-02 «Annual Calendar»: OTRO molde que el base (A mes · B tipo de eventos · C menú sugerido · D mantenimiento ·
# E marketing; 12 filas, 4-15, sin filas libres). A y B fijados (fechas US); C, D y E = traductor (con ADAPTAR donde
# el ES dice algo que en EE. UU. no vale). fila → (mes, eventos)
# ==========================================================================
FILAS_CALENDARIO = range(4, 16)
CALENDARIO = OrderedDict([
    (4, ('January', 'Indoor events and winter markets (slow season)')),
    (5, ('February', "Super Bowl Sunday (party orders), Valentine's Day, Mardi Gras (varies), indoor events")),
    (6, ('March', "Outdoor markets reopen, St. Patrick's Day (Mar 17), spring break")),
    (7, ('April', 'Easter (varies), spring festivals, food truck rallies')),
    (8, ('May', 'Cinco de Mayo, Memorial Day weekend (last Monday), graduations, wedding season starts')),
    (9, ('June', "Music festivals, street fairs, graduations, Father's Day (3rd Sunday)")),
    (10, ('July', 'Jul 4 — Independence Day, county fairs, festivals, weddings')),
    (11, ('August', 'Peak season: county and state fairs, festivals, summer tourism')),
    (12, ('September', 'Labor Day (1st Monday), back to school (campus and office routes), fall festivals')),
    (13, ('October', 'Fall festivals and food markets, Halloween (Oct 31)')),
    (14, ('November', 'Thanksgiving (4th Thursday), holiday markets, corporate events')),
    (15, ('December', "Holiday markets, corporate holiday parties, New Year's Eve")),
])

# ==========================================================================
# POR_CELDA: textos EN fijados (no van al traductor)
# ==========================================================================
POR_CELDA = OrderedDict()
# título interior (D5): A2 de la única hoja = «NN · título» (mapas.titulo_interior; los bonus ya empiezan por «BONUS:»)
for _f in FICHEROS:
    _c = re.match(r'^(BONUS-)?(\d+)', _f)
    _corto = ('B' if _c.group(1) else '') + _c.group(2)
    _en = FICHEROS[_f]
    _t = TITULOS[_en]
    POR_CELDA[(_corto, HOJA_DE[_corto], CELDA_TITULO)] = _t if _t.startswith('BONUS') else '%s · %s' % (_en[:2], _t)
# errata ES (§5): en el 02 y el 03 las cabeceras C3 / D3 van cruzadas (C trae responsables, D frecuencias)
for _corto in ('02', '03'):
    POR_CELDA[(_corto, HOJA_DE[_corto], 'C3')] = 'Assigned to'
    POR_CELDA[(_corto, HOJA_DE[_corto], 'D3')] = 'Frequency'
# «Servicio» como PUESTO (01 C18-C20 y el perfil del 06 A17-A21): window staff (la ventanilla); como fase o momento,
# «Service» (GLOSARIO base)
for _celda in ('C18', 'C19', 'C20'):
    POR_CELDA[('01', 'Setup y Teardown', _celda)] = 'Window staff'
for _fila in range(17, 22):
    POR_CELDA[('06', 'Perfiles', 'A%d' % _fila)] = 'Window staff'
# 03 · temperaturas de cocción (FDA Food Code 3-401.11; el ES dice «>=74 °C aves, >=63 °C otros»)
POR_CELDA[('03', 'APPCC Movil', 'B8')] = (
    'Probe internal cooking temps: poultry 165 °F; ground beef and other ground meats 155 °F for 17 s; fish and '
    'whole-muscle pork or beef 145 °F for 15 s (FDA Food Code 3-401.11) — log reading: ____ °F')
POR_CELDA[('03', 'APPCC Movil', 'F19')] = '9 major US allergens (UK: 14)'
# 04 · permisos, seguros y alta fiscal US (research US del Food Truck Business Plan Kit §5 y SPEC §4.2)
POR_CELDA[('04', 'Permisos y Eventos', 'B6')] = (
    'Mobile food unit health permit from your local (county or city) health department (plan review + '
    'inspection), with your commissary agreement')
POR_CELDA[('04', 'Permisos y Eventos', 'B7')] = (
    'General liability insurance (events and property owners often ask for $1M per occurrence and a certificate of '
    'insurance naming them)')
POR_CELDA[('04', 'Permisos y Eventos', 'B9')] = (
    "Business license (city or county) + state sales tax registration (seller's permit); free EIN from the IRS "
    '(needed with employees or a multi-member LLC)')
# 08 · eventos españoles (MadrEat, Van Van Market, San Isidro / Fallas / Feria de Abril) → su equivalente US
for _fila, (_a, _b) in ((13, ('Food truck festivals', 'Regional food truck festivals and rallies (vendor application)')),
                        (14, ('Farmers & night markets', 'Farmers markets and night markets in several towns '
                                                         '(seasonal vendor spot)')),
                        (15, ('County & state fairs', 'County and state fairs, street fairs and local festivals '
                                                      '(apply when vendor applications open)'))):
    POR_CELDA[('08', 'Eventos y Temporadas', 'A%d' % _fila)] = _a
    POR_CELDA[('08', 'Eventos y Temporadas', 'B%d' % _fila)] = _b
for _fila, (_mes, _ev) in CALENDARIO.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'A%d' % _fila)] = _mes
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'B%d' % _fila)] = _ev

# ==========================================================================
# ADAPTAR (en español, con el dato US; las cifras y normas salen de REGLAS_US). Toda celda ES con °C lleva el suyo o
# va por POR_CELDA (cruzar_censo lo exige).
# ==========================================================================
_A = _base.ADAPTAR
_FRIO = ('Frío: 41 °F o menos; congelado, 0 °F o menos (FDA Food Code 3-501.16); nevera portátil → cooler, mesa '
         'refrigerada → refrigerated prep table; si la tarea pide lectura, coletilla «— log reading: ____ °F»')
_CALIENTE = ('Mantenimiento en caliente: 135 °F o más (FDA Food Code 3-501.16), o time as a public health control '
             'con procedimiento escrito: hora marcada y servir o descartar en 4 h (FDA Food Code 3-501.19); sin los '
             '«65 °C» ni las «2 h» del ES; coletilla «— log reading: ____ °F»')
_ENFRIAR = ('Enfriado: de 135 °F a 70 °F en 2 h y a 41 °F en 4 h más (FDA Food Code 3-501.14), tapado y con date '
            'marking (7 días como máximo a 41 °F, día 1 = el de preparación; FDA Food Code 3-501.17); se guarda en el '
            'commissary')
_TIRA = 'sanitizante aprobado a la concentración de la etiqueta, medida con tira (test strip) (FDA Food Code 4-501.114)'
_LIMPIAR = 'Limpiar y luego sanitizar con ' + _TIRA
_RESIDUALES = ('Las aguas residuales (wastewater / gray water) solo se vacían en el commissary o en un servicing area '
               'aprobado, nunca en la calle, en el suelo ni en un sumidero de pluviales (storm drain) (FDA Food Code '
               '5-402.14)')
_AGUA = ('Agua potable de una fuente aprobada (FDA Food Code 5-101.11), cargada en el commissary con una manguera de '
         'agua potable (food-grade) que no se usa para nada más')
_TANQUES = ('Depósito limpio → fresh (potable) water tank, lleno; depósito residual → wastewater (gray water) tank, '
            'vacío y al menos un 15 % mayor que el de agua limpia (FDA Food Code 5-401.11); agua caliente en el '
            'lavamanos, 100 °F o más (FDA Food Code 5-202.12)')
_PROPANO = ('Propano (en EE. UU. no se usa butano): bombonas → propane cylinders (tanks), sujetas en vertical y con la '
            'válvula cerrada en ruta; sistema según NFPA 58 y la inspección de tu fire marshal')
_FUGAS = ('Prueba de fugas con agua jabonosa, nunca con llama, en las conexiones y tras cada cambio de bombona (NFPA 1 '
          '/ NFPA 58, según la edición que aplique tu fire marshal)')
_GENERADOR = ('Generador fuera del truck, lejos de la ventanilla, de las tomas de aire y de la gente (monóxido de '
              'carbono), donde lo permitan el organizador y el fire marshal; cables sin riesgo de tropiezo')
_EXTINTORES = ('Extintores: uno ABC y, con freidora, otro de clase K (NFPA 10); inspección visual mensual y '
               'mantenimiento anual con etiqueta (29 CFR 1910.157(e)(2)-(3)); el sistema de extinción de la campana, '
               'cada 6 meses (NFPA 96)')
_CAMPANA = ('Campana (hood): los filtros los desengrasa el equipo; la campana y los conductos, una empresa certificada '
            'con la frecuencia de NFPA 96; el sistema de extinción de la campana, cada 6 meses (NFPA 96)')
_VEHICULO = ('Sin ITV: registro y título del vehículo en el DMV de tu estado al día y seguro commercial auto en vigor; '
             'inspección de seguridad del vehículo solo donde tu estado la exija; licencia CDL solo si el GVWR es de '
             '26,001 lb o más (49 CFR 383.91)')
_SEPARACION = ('Muchos fire marshals exigen al menos 10 ft libres entre el truck y edificios, otros vehículos y '
               'materiales combustibles (NFPA 1 / NFPA 96, según la edición que aplique tu jurisdicción)')
_PARKING = ('Solo donde lo permitan las normas de venta y aparcamiento de tu ciudad (vending zones, horarios y '
            'distancias) o con permiso escrito del dueño en propiedad privada')
_VENTA = ('Licencia de venta ambulante → mobile vending license de la ciudad (o del condado), una por truck e '
          'intransferible, además del mobile food unit permit del departamento de salud del condado')
_ALERGENOS = ('Alérgenos US: los 9 principales (FALCPA + FASTER Act: leche, huevo, pescado, crustáceos, frutos de '
              'cáscara, cacahuete, trigo, soja y sésamo); aviso escrito en el menú o en la ventanilla donde tu estado '
              'haya adoptado el FDA Food Code 2022 (3-602.12(C)); en UK, los 14')
_GLUTEN = ('«Sin gluten» → «gluten-free» solo si lo puedes sostener: con freidora o plancha (flat-top griddle) '
           'compartidas, no se promete (21 CFR 101.91)')
_PROPINAS = ('Propinas: según tu política escrita de tip pool; los managers y supervisors no se quedan propinas (FLSA, '
             '29 U.S.C. 203(m)(2)(B))')
_CAJA = ('Cierre de caja → cash count y over/short (cash drawer contra el POS Z report; ventas con tarjeta sin '
         'propinas); ' + _PROPINAS)
_REDES = ('RRSS → social media; Google Maps → Google Business Profile; añade las food truck apps (Roaming Hunger, '
          'StreetFoodFinder)')
_COI = ('Seguro RC → general liability insurance; muchos eventos piden un certificate of insurance (COI) con el '
        'organizador como additional insured')
ADAPTAR = OrderedDict([
    # 01 · Setup y Teardown
    (('01', 'Setup y Teardown', 'B5'), _PARKING + '; calzos → wheel chocks'),
    (('01', 'Setup y Teardown', 'B6'), _GENERADOR),
    (('01', 'Setup y Teardown', 'B7'), _PROPANO),
    (('01', 'Setup y Teardown', 'B11'), 'plancha → flat-top griddle; antes de encender, campana y sistema de extinción '
                                        '(hood suppression) operativos; si huele a gas: no encender nada, cerrar la '
                                        'bombona, salir y llamar al 911 desde fuera'),
    (('01', 'Setup y Teardown', 'B12'), _FRIO),
    (('01', 'Setup y Teardown', 'B19'), 'TPV → POS; datáfono → card reader; cambio en efectivo → starting bank (cash '
                                        'float)'),
    (('01', 'Setup y Teardown', 'B21'), _TANQUES),
    (('01', 'Setup y Teardown', 'B23'), 'Y cerrar las válvulas de las bombonas de propano (propane cylinders)'),
    (('01', 'Setup y Teardown', 'B24'), _ENFRIAR),
    (('01', 'Setup y Teardown', 'B25'), _LIMPIAR + '; plancha → flat-top griddle'),
    (('01', 'Setup y Teardown', 'B26'), _RESIDUALES),
    (('01', 'Setup y Teardown', 'B28'), _CAJA),
    (('01', 'Setup y Teardown', 'B30'), 'Incluye las bombonas de propano sujetas y con la válvula cerrada para el '
                                        'trayecto'),
    # 02 · Vehicle & Mobile Ops
    (('02', 'Operaciones Moviles', 'B8'), _VEHICULO),
    (('02', 'Operaciones Moviles', 'B10'), _EXTINTORES),
    (('02', 'Operaciones Moviles', 'B12'), 'Gasolina o diésel (o propano, según el generador); repostar con el '
                                           'generador apagado y frío, como indique su manual'),
    (('02', 'Operaciones Moviles', 'B15'), 'Según las horas de uso que marque el manual del fabricante'),
    (('02', 'Operaciones Moviles', 'B16'), _PROPANO),
    (('02', 'Operaciones Moviles', 'B17'), _FUGAS),
    (('02', 'Operaciones Moviles', 'B19'), _AGUA + '; capacidad = la que fije tu permiso'),
    (('02', 'Operaciones Moviles', 'B20'), _RESIDUALES),
    (('02', 'Operaciones Moviles', 'B23'), 'Aceite usado → used cooking oil, en contenedor cerrado para el reciclador '
                                           'con licencia (licensed recycler) o el del commissary'),
    (('02', 'Operaciones Moviles', 'B24'), 'Punto limpio → plan de residuos del evento: basura, grasa y aguas '
                                           'residuales al commissary o a la zona que indique el organizador; nada al '
                                           'suelo ni al storm drain (FDA Food Code 5-402.14)'),
    # 03 · Food Safety & Inspection (B8 y F19 van por POR_CELDA)
    (('03', 'APPCC Movil', 'B5'), _FRIO + '; sin los «0-4 °C» del ES'),
    (('03', 'APPCC Movil', 'B6'), _FRIO + '; lectura en ruta'),
    (('03', 'APPCC Movil', 'B7'), _FRIO),
    (('03', 'APPCC Movil', 'B9'), _CALIENTE),
    (('03', 'APPCC Movil', 'B10'), 'Descongelar en el refrigerador a 41 °F o menos, bajo agua corriente fría a 70 °F o '
                                   'menos, en el microondas si se cocina enseguida o como parte de la cocción (FDA Food '
                                   'Code 3-501.13); nunca a temperatura ambiente; cámara/nevera → refrigerator'),
    (('03', 'APPCC Movil', 'B12'), 'Lavamanos (handwashing sink) con agua caliente, 100 °F o más (FDA Food Code '
                                   '5-202.12), jabón y toallas de papel; el gel (hand sanitizer) solo DESPUÉS de '
                                   'lavarse, nunca en su lugar (FDA Food Code 2-301.16)'),
    (('03', 'APPCC Movil', 'B13'), 'Sin contacto de mano desnuda con alimento listo para comer: guantes, pinzas o papel '
                                   '(FDA Food Code 3-301.11); guantes nuevos al cambiar de tarea'),
    (('03', 'APPCC Movil', 'B14'), _LIMPIAR),
    (('03', 'APPCC Movil', 'B19'), _ALERGENOS + '; carta de alérgenos → allergen chart'),
    (('03', 'APPCC Movil', 'B21'), 'Sin «libro de registro sanitario»: el health permit de la unidad móvil a la vista y, '
                                   'en el truck, los registros de temperaturas y el commissary log (o el commissary '
                                   'agreement) para la inspección'),
    (('03', 'APPCC Movil', 'B22'), 'Carnet de manipulador → food handler card (según el estado) para el equipo y un '
                                   'Certified Food Protection Manager (CFPM, p. ej. ServSafe Manager) como person in '
                                   'charge (FDA Food Code 2-102.12)'),
    (('03', 'APPCC Movil', 'B23'), _VENTA),
    (('03', 'APPCC Movil', 'B24'), _COI),
    # 04 · Permits & Events (B6, B7 y B9 van por POR_CELDA)
    (('04', 'Permisos y Eventos', 'B5'), _VENTA + '; renovación anual'),
    (('04', 'Permisos y Eventos', 'B8'), 'Seguro del vehículo con cobertura comercial → commercial auto insurance'),
    (('04', 'Permisos y Eventos', 'B10'), 'POS configurado para cobrar y declarar el sales tax según el lugar de venta; '
                                          'recibo (receipt) si el cliente lo pide; sin «factura» española'),
    (('04', 'Permisos y Eventos', 'B16'), 'Permiso temporal del evento (temporary food event permit) si lo pide el '
                                          'departamento de salud, y los requisitos del organizador (COI, inspección '
                                          'del fire marshal). ' + _SEPARACION),
    (('04', 'Permisos y Eventos', 'B17'), _REDES),
    (('04', 'Permisos y Eventos', 'B19'), 'street food markets → food truck parks, farmers markets y night markets'),
    (('04', 'Permisos y Eventos', 'B20'), 'fiestas patronales → county fairs y street fairs'),
    (('04', 'Permisos y Eventos', 'B24'), 'polígono → business park; ' + _PARKING),
    # 05 · Manager Tasks
    (('05', 'Tareas Manager', 'B5'), _PARKING),
    (('05', 'Tareas Manager', 'B12'), 'Sin el «<25 %» del ES (sin base US): food cost % contra el objetivo de tu plan; '
                                      'referencia del kit: «about 28–35% for a US food truck (kit benchmark)»'),
    (('05', 'Tareas Manager', 'B15'), _CAJA),
    (('05', 'Tareas Manager', 'B17'), _REDES),
    (('05', 'Tareas Manager', 'B19'), 'Plataformas US: Google y Yelp'),
    # 06 · Duties by Role
    (('06', 'Perfiles', 'B5'), 'cocina base → commissary: la mise en place se prepara en el commissary o en el truck, '
                               'nunca en una cocina de casa (FDA Food Code 3-201.11)'),
    (('06', 'Perfiles', 'B9'), _LIMPIAR),
    (('06', 'Perfiles', 'B18'), 'TPV → POS; Bizum → pagos con el móvil (tap to pay: Apple Pay, Google Pay)'),
    (('06', 'Perfiles', 'B20'), _ALERGENOS + '. ' + _GLUTEN),
    (('06', 'Perfiles', 'B25'), _GENERADOR + '; ruido y horario según las normas del evento y de la ciudad'),
    (('06', 'Perfiles', 'B26'), 'fresh water tank / wastewater (gray water) tank; ' + _RESIDUALES),
    # 07 · Weekly & Monthly
    (('07', 'Semanales y Mensuales', 'B6'), _CAMPANA),
    (('07', 'Semanales y Mensuales', 'B8'), 'test de polares → TPM tester o tiras (total polar materials); el aceite '
                                            'usado, al reciclador con licencia'),
    (('07', 'Semanales y Mensuales', 'B9'), 'Propano (sin butano): nivel de las bombonas y ' + _FUGAS[0].lower()
     + _FUGAS[1:]),
    (('07', 'Semanales y Mensuales', 'B10'), 'Limpiar y sanitizar el depósito de agua potable, la bomba y la manguera '
                                             'como pida tu departamento de salud; ' + _RESIDUALES),
    (('07', 'Semanales y Mensuales', 'B14'), 'Según las horas de uso que marque el manual del fabricante'),
    (('07', 'Semanales y Mensuales', 'B16'), 'APPCC → HACCP: revisar los registros de temperaturas, de limpieza y el '
                                             'commissary log'),
    (('07', 'Semanales y Mensuales', 'B19'), 'Health permit de la unidad móvil, mobile vending license de cada ciudad, '
                                             'commissary agreement, inspección del fire marshal, registro del DMV y '
                                             'seguros'),
    (('07', 'Semanales y Mensuales', 'B21'), 'Incluye las food handler cards del equipo al día'),
    # 08 · Events & Seasons (A13-A15 y B13-B15 van por POR_CELDA)
    (('08', 'Eventos y Temporadas', 'B5'), 'ferias → festivals; mercados al aire libre → farmers markets y food truck '
                                           'rallies'),
    (('08', 'Eventos y Temporadas', 'B6'), 'Temporada alta US (de Memorial Day a Labor Day): festivales, playas, county '
                                           'fairs y el 4 de julio; sin «chiringuitos»'),
    (('08', 'Eventos y Temporadas', 'B8'), 'jornadas de otoño → fall festivals'),
    (('08', 'Eventos y Temporadas', 'B11'), 'Navidad: mercadillos navideños → holiday markets; eventos de empresa → '
                                            'corporate holiday parties'),
    (('08', 'Eventos y Temporadas', 'B18'), 'Nochevieja = New Year\'s Eve: eventos de cuenta atrás (countdown) y fiestas '
                                            'privadas; sin uvas; nada de alcohol sin licencia'),
    # BONUS-01 · Pre-Event Briefing
    (('B01', 'Briefing Pre-Evento', 'C13'), 'Fee de entrada → vendor fee (fijo o % de las ventas)'),
    (('B01', 'Briefing Pre-Evento', 'C18'), 'Allergen chart con los 9 alérgenos principales de EE. UU., impresa y a la '
                                            'vista'),
    # BONUS-02 · Annual Calendar (A y B por POR_CELDA)
    (('B02', 'Calendario Anual', 'C15'), 'Sin champán: un food truck no sirve alcohol sin licencia; bebidas festivas sin '
                                         'alcohol'),
    (('B02', 'Calendario Anual', 'D4'), 'post-Navidad → post-holiday'),
    (('B02', 'Calendario Anual', 'D5'), 'Sin ITV: inspección de seguridad del vehículo solo si tu estado la exige; '
                                        'renovar el registro del DMV si toca'),
    (('B02', 'Calendario Anual', 'E13'), 'eventos de Navidad → holiday events (holiday markets y fiestas de empresa)'),
    (('B02', 'Calendario Anual', 'E14'), 'campaña de Navidad y empresa → holiday and corporate catering campaign'),
])
# aplicar_en.objetivo_ajuste / G3: la EN activa el ajuste también donde el ES tampoco cabía (lección de la pizzería)
AJUSTE_MAQUETA_ES = True
CELSIUS_SIN_F = frozenset()

# ==========================================================================
# REGLAS_US: las del base + las del food truck (fuente única de las cifras y normas que el kit puede afirmar)
# ==========================================================================
REGLAS_US = OrderedDict(_base.REGLAS_US)
REGLAS_US.update([
    ('coccion', ('aves 165 °F instantáneo; carne picada 155 °F 17 s; pescado y piezas enteras de cerdo o vacuno '
                 '145 °F 15 s', 'FDA Food Code 2022 §3-401.11(A)')),
    ('descongelacion', ('refrigerador a 41 °F o menos; agua corriente a 70 °F o menos; microondas con cocción '
                        'inmediata; o como parte de la cocción', 'FDA Food Code 2022 §3-501.13')),
    ('tphc', ('time as a public health control: procedimiento escrito; hora marcada; servir o descartar DENTRO de las 4 h',
              'FDA Food Code 2022 §3-501.19(B)')),
    ('mano_desnuda', ('sin contacto de mano desnuda con alimento listo para comer', 'FDA Food Code 2022 §3-301.11')),
    ('antiseptico', ('el hand sanitizer no sustituye al lavado de manos', 'FDA Food Code 2022 §2-301.16')),
    ('casa', ('nada preparado en una cocina de casa', 'FDA Food Code 2022 §3-201.11(B)')),
    ('cfpm', ('Certified Food Protection Manager como person in charge; food handler cards según el estado',
              'FDA Food Code 2022 §2-102.12; [estatal] (research US del Food Truck Business Plan Kit §5)')),
    ('aviso_alergenos', ('aviso escrito de los alérgenos principales en lo que se sirve sin envasar, donde se haya '
                         'adoptado el Food Code 2022', 'FDA Food Code 2022 §3-602.12(C)')),
    ('gluten_free', ('no prometer «gluten-free» con freidora o plancha compartidas', '21 CFR 101.91')),
    ('agua_potable', ('agua potable de fuente aprobada; manguera de agua potable dedicada', 'FDA Food Code 2022 '
                      '§5-101.11; Part 5-3 (mobile water tank) [criterio del kit] la manguera dedicada')),
    ('tanque_residual', ('depósito de aguas residuales al menos un 15 % mayor que el de agua potable',
                         'FDA Food Code 2022 §5-401.11(A) (adoptado por los estados: MN 4626.1180, WA 246-215-05400)')),
    ('residuales', ('aguas residuales solo en un servicing area aprobado (commissary), nunca al suelo ni al storm drain',
                    'FDA Food Code 2022 §5-402.14; «servicing area» = §1-201.10; [local] ordenanzas de pluviales')),
    ('commissary', ('commissary agreement y commissary log', '[local] la mayoría de health departments (research US '
                    '§5: cabq.gov, chicago.gov)')),
    ('permisos', ('mobile vending license por ciudad, intransferible; mobile food unit health permit con plan review e '
                  'inspección; temporary food event permit', '[local] research US del Food Truck Business Plan Kit §5 '
                  '(cabq.gov, chicago.gov)')),
    ('alta_fiscal', ("business license + seller's permit (sales tax estatal); EIN del IRS", 'research US §5 '
                     '(sba.gov, irs.gov)')),
    ('sales_tax_pos', ('POS que cobra y declara el sales tax por lugar de venta', 'Food Truck Business Plan Kit SPEC '
                       '§4.2')),
    ('seguro_eventos', ('general liability, a menudo $1M por siniestro, y COI para el organizador', 'Food Truck '
                        'Business Plan Kit SPEC §4.2; [criterio del kit] COI + additional insured (catering EN)')),
    ('vehiculo', ('registro y título en el DMV; CDL solo con GVWR de 26,001 lb o más', '49 CFR 383.5 y 383.91 '
                  '(research US §5)')),
    ('propano', ('propano según NFPA 58; inspección del fire marshal (propano, extintores, extinción)', 'NFPA 58; '
                 '[local] fire marshal (research US §5)')),
    ('fugas', ('prueba de fugas con agua jabonosa tras cada cambio de bombona', 'NFPA 1 §50.7 / NFPA 58 (fichas de '
               'bomberos: Orangeburg SC, North Port FL; la numeración cambia con la edición)')),
    ('separacion', ('al menos 10 ft libres de edificios, otros vehículos y combustibles', 'NFPA 1 §50.8 / NFPA 96 '
                    'cap. 17, según la edición adoptada (NFPA Food Truck Safety Fact Sheet; TAMU EHS 2024)')),
    ('extintor_k', ('extintor de clase K donde se fríe con aceite o grasa', 'NFPA 10')),
    ('generador', ('generador fuera del truck, lejos de la ventanilla y de las tomas de aire (monóxido de carbono); '
                   'repostar apagado y frío', '[criterio del kit] + manual del fabricante; [local] organizador y fire '
                   'marshal')),
    ('propinas_pool', ('managers y supervisors no se quedan propinas del equipo', 'FLSA, 29 U.S.C. 203(m)(2)(B)')),
    ('apps', ('food truck apps: Roaming Hunger, StreetFoodFinder', 'Food Truck Business Plan Kit SPEC §4.2')),
    ('food_cost', ('food cost de un food truck US: 28-35 % (referencia del kit)', 'research US del Food Truck Business '
                   'Plan Kit §4 (beancount.io, resumen) [criterio del kit]')),
    ('dias_fuertes', ('Super Bowl, Cinco de Mayo, Memorial Day, 4 de julio, county fairs, Labor Day, Thanksgiving: el '
                      'calendario de un food truck US', '[criterio del kit] calendario comercial; 5 U.S.C. 6103 (base)')),
])
# °F que el kit puede afirmar (G7 = las cifras °F de mapas: POR_CELDA, ADAPTAR y REGLAS_US, también las del base): las
# del base sin el 10 (helado) ni el 32 (calibración) + 145 / 155 (cocción)
GRADOS_F_SPEC = {-31, -4, 0, 41, 70, 100, 135, 145, 155, 165}

# ==========================================================================
# Pistas y dependencias del food truck (extraer_textos.py). El ES viene SIN tildes («electrica», «deposito»): las
# regex las toleran.
# ==========================================================================
PISTAS_CAMBIO = {r'Kit de Tareas': 'D2: «Food Truck Checklists Kit Pro»'}
PISTAS_FUERA = (r'Restaurante Casual',)
PISTAS_EXTRA = [
    (r'[Ff]ood [Tt]ruck', 'D2: sin el sufijo «— Food Truck» de los títulos; food truck → food truck; el camión → the '
                          'truck; nunca «restaurant»'),
    (r'[Ss]etup|[Tt]eardown|[Mm]ontaje|[Dd]esmontaje', 'setup → setup; teardown → teardown (breakdown); montar → set '
                                                       'up; recoger → pack up'),
    (r'[Gg]enerador', 'generador → generator (fuera del truck, lejos de la ventanilla: monóxido de carbono)'),
    (r'[Bb]ombona|[Pp]ropano|[Bb]utano|\b[Gg]as\b', 'bombona → propane cylinder (tank); butano → NO (en EE. UU., '
                                                    'propano); prueba de fugas con agua jabonosa'),
    (r'[Dd]ep[oó]sito|agua (limpia|residual)|[Bb]omba de agua', 'depósito de agua limpia → fresh (potable) water tank; '
                                                                'residual → wastewater (gray water) tank; bomba → water '
                                                                'pump'),
    (r'TPV|[Dd]at[aá]fono|[Cc]ambio|[Ee]fectivo', 'TPV → POS; datáfono → card reader; cambio → starting bank (cash '
                                                  'float); efectivo → cash'),
    (r'Bizum', 'Bizum → tap to pay / mobile wallet (Apple Pay, Google Pay)'),
    (r'\bITV\b', 'ITV → no existe: DMV registration; state vehicle safety inspection solo donde se exija'),
    (r'RGSEAA|[Rr]egistro sanitario|[Ll]ibro de registro', 'registro sanitario → mobile food unit health permit '
                                                           '(county); plan review; commissary agreement'),
    (r'[Vv]enta ambulante|[Ll]icencia', 'licencia de venta ambulante → mobile vending license (city)'),
    (r'\bIAE\b|[Ff]acturaci|[Ff]actura|\bticket\b', "IAE → business license + seller's permit; ticket/factura → "
                                                    'receipt; el POS cobra el sales tax'),
    (r'\bEUR\b|€', 'D13: sin euros (en EE. UU. el dato va en dólares solo si lo fija POR_CELDA)'),
    (r'[Cc]arnet de manipulador', 'carnet de manipulador → food handler card; responsable → Certified Food Protection '
                                  'Manager (CFPM)'),
    (r'RRSS|Instagram|TikTok|Google Maps|[Rr]edes', 'RRSS → social media; Google Maps → Google Business Profile; food '
                                                    'truck apps (Roaming Hunger, StreetFoodFinder)'),
    (r'[Rr]ese[nñ]as|[Rr]eviews', 'reseñas → reviews (Google, Yelp)'),
    (r'[Pp]ol[ií]gono|[Cc]ampus|[Oo]ficinas', 'polígono → business park; zona de oficinas → office district; campus → '
                                              'campus'),
    (r'[Mm]ercad', 'mercados gastronómicos / street food markets → food truck parks, farmers markets, night markets; '
                   'mercadillos navideños → holiday markets'),
    (r'[Ff]iestas (patronales|locales)|[Ff]estivales|[Ff]eria', 'fiestas patronales / locales → county fairs, street '
                                                                'fairs, local festivals; ferias → festivals / fairs'),
    (r'[Cc]hiringuito|[Pp]layas', 'chiringuitos → fuera; playas → beaches (boardwalk)'),
    (r'[Cc]abalgatas|[Rr]ebajas|[Cc]arnaval|Fallas|San Isidro|Feria de Abril|Semana Santa|[Vv]endimia|[Nn]ochevieja|'
     r'[Nn]avid|San Valentin', 'calendario US (Super Bowl, Memorial Day, 4 de julio, Labor Day, Thanksgiving, '
                               "holiday markets, New Year's Eve): sin fiestas españolas"),
    (r'[Mm]ermas', 'mermas → waste (waste log)'),
    (r'[Pp]olares', 'test de polares → TPM (total polar materials) tester o tiras'),
    (r'[Cc]alzos', 'calzos → wheel chocks'),
    (r'[Ss]e[nñ]al[eé]tica|[Tt]oldo|[Mm]arquesina|[Pp]izarra|[Bb]anner', 'señalética → signage; toldo / marquesina → '
                                                                          'awning; pizarra → menu board'),
    (r'[Pp]unto limpio|[Aa]ceite usado', 'punto limpio → commissary / approved disposal; aceite usado → used cooking '
                                         'oil (licensed recycler)'),
    (r'[Nn]evera|[Mm]esa refrigerada|[Cc][aá]mara', 'nevera portátil → cooler; mesa refrigerada → refrigerated prep '
                                                    'table; cámara / nevera → refrigerator (en el truck no hay walk-in)'),
    (r'[Gg]el hidroalcoh', 'gel hidroalcohólico → hand sanitizer: solo después de lavarse las manos (FDA Food Code '
                           '2-301.16)'),
    (r'[Ee]ncargad|[Cc]ajer|[Aa]yudante|[Cc]onductor|[Tt][eé]cnico', 'encargado → manager; cajero → cashier; ayudante '
                                                                    'de cocina → prep cook; conductor → driver; técnico '
                                                                    '→ driver / tech; servicio (puesto) → window staff'),
    (r'[Ee]quipo\b', 'equipo (personas) → crew'),
    (r'[Cc]ocina base', 'cocina base → commissary'),
    (r'[Pp]lancha', 'plancha → flat-top griddle (NUNCA «plancha»)'),
    (r'sin gluten|vegano', 'vegano → vegan; sin gluten → gluten-free solo si se puede sostener (21 CFR 101.91)'),
    (r'[Ff]ee|% sobre ventas', 'fee de entrada → vendor fee (flat or % of sales)'),
    (r'[Cc]hamp[aá]n|[Aa]lcohol', 'alcohol: un food truck no lo vende sin licencia'),
    (r'[Mm]enu\b|[Cc]arta\b', 'menú / carta → menu (menu board en la ventanilla)'),
    (r'[Pp]ackaging|[Ee]mplatado', 'packaging → to-go packaging; emplatado → plating / order assembly'),
    (r'[Ff]idelidad|[Ff]idelizaci', 'tarjeta de fidelidad → loyalty program (punch card o en el POS)'),
]
DEPENDENCIAS_EXTRA = OrderedDict([
    ('variante', ('Sufijo «— Food Truck» en títulos', r'— Food Truck', 'D2: la EN no lleva sufijo')),
    ('alergenos', ('Alérgenos (UE 14), con o sin tilde', r'[Aa]l[eé]rgenos|AL[EÉ]RGENOS', 'D10: 9 alérgenos US; UK 14')),
    ('caja', ('Caja española: TPV, datáfono, Bizum, cuadre', r'TPV|[Dd]at[aá]fono|Bizum|[Cc]uadre|[Cc]ierre de caja',
              'D12: POS, card reader, starting bank, over/short, propinas por tip pool')),
    ('vehiculo', ('Vehículo: ITV y seguro', r'\bITV\b|[Ss]eguro del veh', 'D-FT: DMV, commercial auto, CDL ≥ 26,001 lb')),
    ('agua', ('Depósitos de agua limpia y residual', r'[Dd]ep[oó]sito|agua (limpia|residual)',
              'D-FT: fresh / wastewater tank, 15 % (5-401.11), commissary (5-402.14)')),
    ('gas', ('Propano y butano', r'[Bb]ombona|[Pp]ropano|[Bb]utano|\b[Gg]as\b', 'D-FT: propano (NFPA 58), fugas')),
    ('generador', ('Generador', r'[Gg]enerador', 'D-FT: fuera del truck, CO, normas del organizador')),
    ('permisos', ('Permisos españoles: venta ambulante, RGSEAA, IAE, carnet de manipulador',
                  r'[Vv]enta ambulante|RGSEAA|\bIAE\b|[Rr]egistro sanitario|[Cc]arnet de manipulador|[Ll]icencia',
                  'D-FT: mobile vending license, mobile food unit permit, commissary, CFPM')),
    ('ubicacion', ('Aparcamiento y ubicación', r'[Aa]parcar|[Uu]bicaci|[Pp]ol[ií]gono|[Rr]uta',
                   'D-FT: vending zones y permiso escrito en propiedad privada')),
    ('eventos_es', ('Eventos y fiestas españolas', r'Madreat|MadrEat|Van Van|San Isidro|Fallas|Feria de Abril|'
                    r'[Cc]abalgatas|[Cc]arnaval|Semana Santa|[Nn]ochevieja|[Vv]endimia|[Cc]hiringuito',
                    'D14: calendario US (CALENDARIO, POR_CELDA del 08)')),
])


def _rebind(f):
    return types.FunctionType(f.__code__, globals(), f.__name__, f.__defaults__, f.__closure__)


titulo_interior = _rebind(_base.titulo_interior)
_autotest_base = _rebind(_base.autotest)
_cruzar_censo_base = _rebind(_base.cruzar_censo)
_SIN_CAJA = ('DENOMINACIONES debe tener las 15 filas del ES',)   # D12: el food truck no tiene libro de caja
RX_F = re.compile(r'(−?\d+)(?:–(−?\d+))? °F')


def _grados(textos):
    out = set()
    for t in textos:
        for m in RX_F.finditer(t):
            for g in m.groups():
                if g:
                    out.add(int(g.replace('−', '-')))
    return out


HOJAS_ES_POR_LIBRO_TODAS = frozenset(h for hs in HOJAS_ES_POR_LIBRO.values() for h in hs)


def autotest():
    err = [e for e in _autotest_base() if e not in _SIN_CAJA]
    if HOJA_CAJA is not None or DENOMINACIONES or FORMULAS_POR_CELDA:
        err.append('el food truck no tiene caja: HOJA_CAJA None y sin denominaciones ni fórmulas por celda')
    rx = re.compile(TERMINOS_PROHIBIDOS)
    if not rx.search(TERMINO_PROHIBIDO_EJEMPLO):
        err.append('TERMINO_PROHIBIDO_EJEMPLO no lo caza TERMINOS_PROHIBIDOS')
    for ok in ('restaurant consultant', 'flat-top griddle', 'propane cylinder', 'commissary agreement', 'Window staff',
               'event venue', 'food truck park'):
        if rx.search(ok):
            err.append('TERMINOS_PROHIBIDOS caza lo permitido: %r' % ok)
    for k, v in list(GLOSARIO.items()) + list(POR_CELDA.items()) + list(CLAVES.items()) + list(HOJAS.items()):
        if (k not in _base.GLOSARIO or k in _GLOSARIO_FT) and isinstance(v, str) and rx.search(v):
            if k in _base.HOJAS and k not in HOJAS_ES_POR_LIBRO_TODAS:
                continue
            err.append('texto EN fijado con un término prohibido: %r → %r' % (k, v))
    for es in HOJAS_ES_POR_LIBRO_TODAS:
        if ',' in HOJAS[es]:
            err.append('pestaña con coma (rompe el área de impresión): %r' % HOJAS[es])
    for c, hs in HOJAS_ES_POR_LIBRO.items():
        if len(hs) != 1:
            err.append('molde plano: el libro %s debe tener UNA hoja' % c)
    for f in FICHEROS:
        c = re.match(r'^(BONUS-)?(\d+)', f)
        corto = ('B' if c.group(1) else '') + c.group(2)
        if POR_CELDA.get((corto, HOJA_DE[corto], CELDA_TITULO)) != titulo_interior(f):
            err.append('título interior de %s ≠ mapas.titulo_interior (POR_CELDA %s)' % (corto, CELDA_TITULO))
    if CITA_AUTOTEST.strip('()').split()[-1] in ' '.join(f for _v, f in REGLAS_US.values()):
        err.append('CITA_AUTOTEST está en REGLAS_US: G7 no la cazaría')
    # G7: los °F que dicen POR_CELDA, ADAPTAR y REGLAS_US (con las del base) son exactamente GRADOS_F_SPEC
    usados = _grados(list(POR_CELDA.values()) + list(ADAPTAR.values()) + [v for v, _f in REGLAS_US.values()])
    if usados != GRADOS_F_SPEC:
        err.append('GRADOS_F_SPEC ≠ los °F de POR_CELDA / ADAPTAR / REGLAS_US: sobra %s, falta %s'
                   % (sorted(GRADOS_F_SPEC - usados), sorted(usados - GRADOS_F_SPEC)))
    if 'restaurant' in MARCA_EN.lower() or not MARCA_EN.endswith(PRODUCTO):
        err.append('MARCA_EN debe acabar en el nombre del producto y sin «restaurant»')
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
    # toda celda ES con °C lleva ADAPTAR o POR_CELDA (o está declarada en CELSIUS_SIN_F)
    for k, t in tx.items():
        if '°C' in t and k not in ADAPTAR and k not in POR_CELDA and k not in CELSIUS_SIN_F:
            err.append('celda ES con °C sin ADAPTAR ni POR_CELDA: %r → %r' % (k, t[:70]))
    # molde plano: A1 = la marca ChefBusiness (→ GLOSARIO), A2 = título, una línea de marca por hoja
    for c, h in HOJA_DE.items():
        if tx.get((c, h, 'A1')) != 'ChefBusiness Consultoria Gastronomica':
            err.append('molde plano: %s!A1 no es la marca (%r)' % (c, tx.get((c, h, 'A1'))))
        if not tx.get((c, h, CELDA_TITULO)):
            err.append('molde plano: %s!%s sin título' % (c, CELDA_TITULO))
        if sum(1 for (cc, hh, _x), t in tx.items() if cc == c and hh == h and t == MARCA_ES) != 1:
            err.append('molde plano: %s sin UNA línea de marca %r' % (c, MARCA_ES))
    # lo que POR_CELDA reescribe es lo que el ES dice en esa celda
    esperado = [(('02', 'Operaciones Moviles', 'C3'), 'Frecuencia'), (('02', 'Operaciones Moviles', 'D3'), 'Responsable'),
                (('03', 'APPCC Movil', 'C3'), 'Frecuencia'), (('03', 'APPCC Movil', 'D3'), 'Responsable'),
                (('03', 'APPCC Movil', 'B8'), 'Control temperatura interna'), (('03', 'APPCC Movil', 'F19'), '14 alergenos'),
                (('04', 'Permisos y Eventos', 'B6'), 'Registro sanitario'),
                (('04', 'Permisos y Eventos', 'B7'), 'Seguro de responsabilidad civil'),
                (('04', 'Permisos y Eventos', 'B9'), 'Alta en IAE'),
                (('08', 'Eventos y Temporadas', 'A13'), 'Madreat'), (('08', 'Eventos y Temporadas', 'A14'), 'Van Van'),
                (('08', 'Eventos y Temporadas', 'A15'), 'Fiestas locales')]
    esperado += [(('01', 'Setup y Teardown', c), 'Servicio') for c in ('C18', 'C19', 'C20')]
    esperado += [(('06', 'Perfiles', 'A%d' % f), 'Servicio') for f in range(17, 22)]
    for k, ini in esperado:
        if not tx.get(k, '').startswith(ini):
            err.append('POR_CELDA %r: el ES no empieza por %r (trae %r)' % (k, ini, tx.get(k)))
    for fila in FILAS_CALENDARIO:
        for col in 'ABCDE':
            if not tx.get((HOJA_CAL[0], HOJA_CAL[1], '%s%d' % (col, fila))):
                err.append('B02: la fila %d no trae %s en el ES' % (fila, col))
    if tx.get((HOJA_CAL[0], HOJA_CAL[1], 'A%d' % (FILAS_CALENDARIO[-1] + 1))):
        err.append('B02: tras la fila %d hay más meses' % FILAS_CALENDARIO[-1])
    return err


CITA_AUTOTEST = '(FDA Food Code 3-501.18)'                     # autotest G7: una cita que NO está en REGLAS_US


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
    for x in e:
        print('ERROR', x)
    print('mapas_foodtruck.py: {} ficheros · {} pestañas · {} glosario · {} por celda · {} adaptar · {} reglas · '
          '{} errores'.format(len(FICHEROS), len(HOJAS), len(GLOSARIO), len(POR_CELDA), len(ADAPTAR), len(REGLAS_US),
                              len(e)))
    raise SystemExit(1 if e else 0)
