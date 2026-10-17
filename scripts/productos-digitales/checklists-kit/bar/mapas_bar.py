#!/usr/bin/env python3
"""
mapas_bar.py — Bar Checklists Kit Pro (EN) · DELTA del Kit de Tareas para Bar (`kit-tareas-bar`, 11 xlsx v2.0) sobre
`mapas.py` (Restaurant Checklists Kit Pro). SPEC: `bar/SPEC.md` (solo el delta). Sesión Claude Code, 18-oct-2026.

Se usa con `--kit bar` (kit.py). Importa `mapas.py` y SOLO añade o sobrescribe: producto, ficheros, títulos,
pestañas, glosario del bar, calendario (otra estructura: B fecha · C evento · D tareas · E antelación · F notas),
POR_CELDA (caja 09 y control de plagas 05 heredados TAL CUAL tras comprobar que el texto ES es el mismo; el resto,
del bar), ADAPTAR y REGLAS_US (+ alcohol, draft, hielo, música, ruido). La hora de 12 h, la caja en dólares y
CLAVES se heredan. Las funciones del base que leen constantes (titulo_interior, autotest, cruzar_censo) se
re-enlazan a ESTE módulo. Ejecutado como script: autotest + cruce con bar/censo_es.json + cruce con el base (que
lo heredado por celda tenga en el bar el mismo texto ES que en el kit base).

    python3 bar/mapas_bar.py
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
AQUI = os.path.dirname(os.path.abspath(__file__))              # bar/ (el import * trae el AQUI del base)

ORIGEN_ES = 'kit-tareas-bar'
PRODUCTO = 'Bar Checklists Kit Pro'
TITULO_SEO = 'Bar Checklists Kit Pro: Bar Opening & Closing Checklist Templates for Excel'
SLUG = 'bar-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_BAR_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
MARCA_ES = '— Kit de Tareas Recurrentes · Bar / Cocktails · AI Chef Pro · aichef.pro'
MARCA_EN = '— ' + PRODUCTO + ' · AI Chef Pro · aichef.pro'
VARIANTES_ES = ('Bar / Cocktails',)
# heredar.py: la cadena del bar que solo cambia en el sufijo de variante hereda el EN del base (que ya no lo lleva)
SUFIJO_A_BASE = [(' — Bar / Cocktails', ' — Restaurante Casual'), (' · Bar / Cocktails', ' · Restaurante Casual')]
# heredar.py: EN del base que en un bar no vale tal cual → pendientes (motivo «contexto»)
RX_CONTEXTO_PENDIENTE = (r'(?i)\b(?:restaurants?(?! consultant)|dining room|line cooks?|prep cooks?|head chef|'
                         r'sous chef|host stand|kitchen, FOH)\b')
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v2.0'),
    ('keywords', 'bar opening checklist, bar closing checklist, bartender checklist, bar cleaning checklist, '
                 'AI Chef Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

FICHEROS = OrderedDict([
    ('01-apertura-cierre.xlsx', '01-bar-opening-closing-checklists.xlsx'),
    ('02-partidas-cocina.xlsx', '02-bar-station-checklists-cocktails-beer-wine.xlsx'),
    ('03-tareas-manager.xlsx', '03-bar-manager-checklist.xlsx'),
    ('04-tareas-perfiles.xlsx', '04-bartender-checklist-duties-by-role.xlsx'),
    ('05-tareas-semanales-mensuales.xlsx', '05-bar-cleaning-checklist-inventory-maintenance.xlsx'),
    ('06-eventos-festivos.xlsx', '06-bar-event-checklists.xlsx'),
    ('07-plantilla-personalizable.xlsx', '07-blank-bar-checklist-template.xlsx'),
    ('08-apertura-cierre-negocio.xlsx', '08-venue-opening-closing-checklist.xlsx'),
    ('09-apertura-cierre-caja.xlsx', '09-cash-drawer-opening-closing.xlsx'),
    ('BONUS-01-briefing-servicio.xlsx', 'BONUS-01-bar-pre-shift-meeting-template.xlsx'),
    ('BONUS-02-calendario-anual-tareas.xlsx', 'BONUS-02-bar-events-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)
TITULOS = OrderedDict([
    ('01-bar-opening-closing-checklists.xlsx', 'Bar Opening & Closing Checklists: Bar Station, Coffee & Patio'),
    ('02-bar-station-checklists-cocktails-beer-wine.xlsx', 'Bar Station Checklists: Cocktails, Draft Beer & Wine'),
    ('03-bar-manager-checklist.xlsx', 'Bar Manager Checklist: Daily, Weekly & Monthly'),
    ('04-bartender-checklist-duties-by-role.xlsx',
     'Bartender Checklist & Daily Duties by Role (Head Bartender, Bartender, Barback, Server)'),
    ('05-bar-cleaning-checklist-inventory-maintenance.xlsx', 'Bar Cleaning Checklist, Inventory & Maintenance Schedule'),
    ('06-bar-event-checklists.xlsx', "Bar Event Checklists: Cocktail Night, New Year's Eve, Happy Hour & Tastings"),
    ('07-blank-bar-checklist-template.xlsx', 'Blank Bar Checklist Template (Editable)'),
    ('08-venue-opening-closing-checklist.xlsx', 'Bar Opening & Closing Checklist (Whole Venue)'),
    ('09-cash-drawer-opening-closing.xlsx', 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log'),
    ('BONUS-01-bar-pre-shift-meeting-template.xlsx', 'BONUS: Bar Pre-Shift Meeting Template (Line-Up Notes)'),
    ('BONUS-02-bar-events-calendar.xlsx', 'BONUS: Bar Holiday & Events Calendar (US)'),
])
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

HOJAS = OrderedDict(_base.HOJAS)
HOJAS.update([
    ('Coctelería Clásica', 'Cocktail Station'), ('Cerveza y Grifo', 'Draft Beer Station'),
    ('Vinos y Bodega', 'Wine & Cellar'),
    ('Head Bartender', 'Head Bartender'), ('Bartender', 'Bartender'), ('Barback', 'Barback'),
    ('Camarero Barra', 'Cocktail Server'),
    ('Inventario', 'Weekly Inventory'),
    ('Noche Cócteles', 'Cocktail Night'), ('Nochevieja', "New Year's Eve"), ('After Work', 'Happy Hour'),
    ('Maridaje Catas', 'Pairings & Tastings'),
    ('Por Zona', 'By Area'),
    ('Apertura del Negocio', 'Venue Opening'), ('Cierre del Negocio', 'Venue Closing'),
    ('Briefing Diario', 'Pre-Shift Meeting'),
])
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Apertura Barra', 'Cierre Barra']),
    ('02', ['Instrucciones', 'Coctelería Clásica', 'Cerveza y Grifo', 'Vinos y Bodega']),
    ('03', ['Instrucciones', 'Diario Manager', 'Semanal Manager', 'Mensual Manager']),
    ('04', ['Instrucciones', 'Head Bartender', 'Bartender', 'Barback', 'Camarero Barra']),
    ('05', ['Instrucciones', 'Limpieza Semanal', 'Mantenimiento Mensual', 'Inventario', 'Trimestral y Anual']),
    ('06', ['Instrucciones', 'Noche Cócteles', 'Nochevieja', 'After Work', 'Maridaje Catas']),
    ('07', ['Instrucciones', 'Por Franja Horaria', 'Por Zona', 'Por Perfil']),
    ('08', ['Instrucciones', 'Apertura del Negocio', 'Cierre del Negocio']),
    ('09', ['Instrucciones', 'Apertura de Caja', 'Cierre de Caja', 'Registro Mensual']),
    ('B01', ['Instrucciones', 'Briefing Diario']),
    ('B02', ['Instrucciones', 'Calendario Anual']),
])
# ==========================================================================
# GLOSARIO: el base entero (opcional en el bar) + celdas cortas del bar
# ==========================================================================
GLOSARIO = OrderedDict(_base.GLOSARIO)
_GLOSARIO_BAR = OrderedDict([
    ('Coctelería', 'Cocktails'), ('Café', 'Coffee'), ('Bodega', 'Stockroom'),
    ('Head Bartender', 'Head bartender'), ('Bartender', 'Bartender'), ('Barback', 'Barback'),
    ('Mantenimiento', 'Maintenance'),
    ('Continuo', 'Ongoing'), ('Pre-apertura', 'Pre-open'), ('Apertura', 'Opening'), ('Tarde', 'Evening'),
    ('Diario', 'Daily'), ('Cada 2h', 'Every 2 h'), ('Día antes', 'Day before'),
    ('1 día antes', '1 day out'), ('3 días antes', '3 days out'),
    ('1 sem antes', '1 week out'), ('2 sem antes', '2 weeks out'), ('3 sem antes', '3 weeks out'),
    ('1ª semana', 'Week 1'), ('2ª semana', 'Week 2'), ('3ª semana', 'Week 3'), ('4ª semana', 'Week 4'),
    ('1 semana', '1 week'), ('2 semanas', '2 weeks'), ('3 semanas', '3 weeks'), ('4 semanas', '4 weeks'),
    ('Fecha', 'Date'),
])
GLOSARIO.update(_GLOSARIO_BAR)
GLOSARIO_OPCIONAL = frozenset(_base.GLOSARIO)
PUESTOS_ES = frozenset(_base.PUESTOS_ES | {'Coctelería', 'Café', 'Bodega', 'Head Bartender', 'Bartender',
                                           'Barback', 'Mantenimiento'})

# ==========================================================================
# BONUS-02 «Holiday Calendar» del bar: filas 4-26; B fecha y C evento fijados; D tareas y F notas = traductor
# (con ADAPTAR cuando el evento cambia). fila → (fecha, evento, ADAPTAR de D o None, ADAPTAR de F o None)
# ==========================================================================
HOJA_CAL = ('B02', 'Calendario Anual')
FILAS_CALENDARIO = range(4, 27)
CALENDARIO = OrderedDict([
    (4, ('Jan 1', "New Year's Day", None, None)),
    (5, ('Feb 14', "Valentine's Day", None, None)),
    (6, ('Feb–Mar', 'Mardi Gras', 'Sustituye a Carnaval (Fat Tuesday, fecha variable): mismas tareas',
         'Fecha variable; enorme en Nueva Orleans y en la costa del Golfo')),
    (7, ('Mar 17', "St. Patrick's Day", 'Mismas tareas + control de ID en la puerta (21+)', None)),
    (8, ('Mar–Apr', 'Spring break', 'Sustituye a Semana Santa. Mismas tareas + control de ID (21+): público joven',
         None)),
    (9, ('Late May', 'Memorial Day weekend (last Mon of May)', 'Sustituye al 1 de mayo y sus puentes: horario de '
         'festivo, patio a pleno rendimiento y stock para varios días seguidos', '«Puente» → long weekend')),
    (10, ('May 5', 'Cinco de Mayo', None, 'En EE. UU. ya es una de las grandes noches de bar del año')),
    (11, ('Jun 20–21', 'First day of summer', None, 'Patio a pleno rendimiento')),
    (12, ('Jun–Sep', 'Summer season', None, None)),
    (13, ('Jul 4', 'Independence Day', 'Sustituye a la Asunción: servicio de festivo, refuerzo de turnos y stock '
          'extra de hielo y cítricos', 'Mira el calendario local: fuegos artificiales, desfiles y calles cortadas')),
    (14, ('Oct 31', 'Halloween', 'Hielo seco solo como decoración (nunca suelto dentro de la copa del cliente) y '
          'manipulado con guantes aislantes', None)),
    (15, ('Nov (3rd Thu)', 'Beaujolais Nouveau Day', None, None)),
    (16, ('Wed before Thanksgiving', 'Thanksgiving Eve', 'Sustituye al puente de diciembre: una de las noches de '
          'más barra del año. Tareas: refuerzo de bartenders y de puerta, control de ID (21+), stock extra; decidir '
          'si se abre el día de Thanksgiving', 'Arranca la temporada de fiestas (holiday season)')),
    (17, ('December', 'Holiday parties (company)', '«Barra libre» → open bar packages', None)),
    (18, ('Dec 24', 'Christmas Eve', 'Decidir el horario (muchos bares cierran pronto en Nochebuena y el 25), turno '
          'reducido y comunicar el horario en Google Business Profile y redes', None)),
    (19, ('Dec 31', "New Year's Eve", 'Champán / espumoso (SIN cava), fiesta, entrada con consumición (ticketed '
          'entry, drink included)', None)),
    (20, ('Varies', 'Local festivals & street fairs', 'Adaptar carta y horarios a los eventos locales (street fairs, '
          'desfiles, festivales)', None)),
    (21, ('Varies', 'Big games & sports nights', None, 'Super Bowl, March Madness, playoffs (NBA, NHL), World Series')),
    (22, ('May 13', 'World Cocktail Day', 'Sin «cóctel gratis»: regalar alcohol o rebajarlo está restringido en algunos '
          'estados; cóctel del día, taller y promo en redes («check your state\'s ABC/liquor authority»)', None)),
    (23, ('September', 'Negroni Week', None, None)),
    (24, ('Weekly', 'Happy hour', 'Happy hour recurrente y fidelización; algunos estados la limitan o la prohíben '
          '(p. ej. Massachusetts): «check your state\'s ABC/liquor authority»', None)),
    (25, ('Monthly', 'Tastings & pairings', None, None)),
    (26, ('Varies', 'DJ & live music nights', 'Sonido, decoración, stock extra y aforo máximo del cartel del fire '
          'marshal (occupancy limit)', 'Ordenanza de ruido de tu ciudad (horas y niveles)')),
])

# ==========================================================================
# POR_CELDA: lo heredado del base (mismo texto ES en la misma celda; lo comprueba cruzar_base) + lo del bar
# ==========================================================================
_HEREDA_POR_CELDA = [k for k in _base.POR_CELDA if k[0] == '09'] + [
    ('05', 'Trimestral y Anual', 'B6'), ('05', 'Trimestral y Anual', 'D6'), ('05', 'Trimestral y Anual', 'E6')]
POR_CELDA = OrderedDict((k, _base.POR_CELDA[k]) for k in _HEREDA_POR_CELDA)
_T = ('05', 'Trimestral y Anual')
POR_CELDA.update([
    # 03 · conservación de fichajes (antes B16 en el base; mismo texto EN)
    (('03', 'Mensual Manager', 'B10'), _base.POR_CELDA[('03', 'Mensual Manager', 'B16')]),
    # 05 · Trimestral y Anual: servicios contratados US del bar
    (_T + ('B7',), 'Annual extinguisher maintenance by a licensed fire protection company: new tag and record '
                   '(OSHA 1910.157); hydrostatic tests per the label'),
    (_T + ('D7',), 'Fire safety co.'),
    (_T + ('B8',), 'Hood and duct cleaning by a certified contractor if the bar has a kitchen or griddle (NFPA 96: '
                   'quarterly if high volume, semiannual if moderate); hood fire suppression inspected every 6 months'),
    (_T + ('D8',), 'Hood cleaning co.'), (_T + ('E8',), 'Semiannual'),
    (_T + ('B9',), 'Gas lines and appliance connections checked by a licensed pro (as often as your local code '
                   'requires); patio heaters: propane tanks, hoses and regulators per your local fire code'),
    (_T + ('D9',), 'Licensed plumber'), (_T + ('E9',), 'Annual'),
    (_T + ('B12',), 'Draft system service by your distributor or a draft tech: acid line cleaning, faucets and '
                    'couplers (Brewers Association: acid clean every 3 months, on top of the 2-week line cleaning)'),
    (_T + ('D12',), 'Draft tech'),
    (_T + ('B13',), 'Refrigeration service by an EPA 608-certified tech: walk-in, back-bar coolers and ice machine — '
                    'coils, gaskets and refrigerant leak check'),
    (_T + ('D13',), 'Refrigeration tech'),
    (_T + ('B15',), 'Legionella: if you run patio misters, a cooling tower or at-risk hot water, keep a water '
                    'management program as your local health code requires'),
    (_T + ('D15',), 'Water treatment co.'),
    (_T + ('B18',), "Music and noise: check your city's noise ordinance and any live entertainment permit (levels, "
                    'hours, complaint log)'),
    (_T + ('D18',), 'Manager'),
    (_T + ('B19',), "Liquor license and outdoor dining / sidewalk cafe permit: renewal dates, approved hours, tables "
                    "and area (check your state's ABC/liquor authority and your city)"),
    (_T + ('B20',), "Review insurance (general liability, property, liquor liability, workers' comp), music licenses "
                    '(ASCAP, BMI, SESAC, GMR) and the glass recycling contract'),
    (_T + ('B21',), 'POS check: software updates, sales tax rates and settings, user permissions; note the next '
                    'review date of each contract and file the signed service report'),
])
for _fila, (_fecha, _evento, _d, _f) in CALENDARIO.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'B%d' % _fila)] = _fecha
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'C%d' % _fila)] = _evento

# ==========================================================================
# ADAPTAR (en español, con el dato US; las cifras salen de REGLAS_US)
# ==========================================================================
_A = _base.ADAPTAR
_TEMP_FRIO = ('°F: cámaras y botellero a 41 °F o menos (FDA Food Code 3-501.16: garnish cortado, lácteos y zumos '
              'son TCS); coletilla «— log reading: ____ °F»; °C solo entre paréntesis si cabe')
_LINEAS = ('Brewers Association (Draught Beer Quality Manual): las líneas de cerveza se limpian cada 2 semanas y con '
           'ácido cada 3 meses; en esta lista, comprobar y firmar las limpiezas del periodo')
_HEREDA_ADAPTAR = [('08', 'Apertura del Negocio', 'B8'), ('09', 'Cierre de Caja', 'B10'),
                   ('09', 'Registro Mensual', 'A37')] + [k for k in _A if k[:2] == ('09', 'Instrucciones')]
ADAPTAR = OrderedDict((k, _A[k]) for k in _HEREDA_ADAPTAR)
ADAPTAR.update([
    # 01
    (('01', 'Apertura Barra', 'B7'), _A[('01', 'Apertura Cocina', 'B7')] + '. Y en EE. UU. nada de mano desnuda '
     'con alimentos listos para consumir (FDA Food Code 3-301.11): garnish e hielo con pinzas, palillos, pala o '
     'guantes; quita «sin guante»'),
    (('01', 'Apertura Barra', 'B9'), _A[('01', 'Apertura Cocina', 'B9')]),
    (('01', 'Apertura Barra', 'B10'), _A[('01', 'Apertura Cocina', 'B10')] + '; quien los tenga no manipula hielo, '
     'bebidas ni alimentos'),
    (('01', 'Apertura Barra', 'B16'), _TEMP_FRIO),
    (('01', 'Apertura Barra', 'B20'), 'Peso US: 65–110 lb (30–50 kg)'),
    (('01', 'Apertura Barra', 'B42'), _A[('01', 'Apertura Sala', 'B19')]),
    (('01', 'Cierre Barra', 'B6'), 'Last call 30 min antes del cierre; la hora de cierre y el fin de la venta de '
     "alcohol los fijan el estado y el municipio: «check your state's ABC/liquor authority»"),
    (('01', 'Cierre Barra', 'B34'), _A[('01', 'Apertura Sala', 'B19')]),
    # 02
    (('02', 'Coctelería Clásica', 'B11'), 'Alérgenos US: los 9 principales (FALCPA + FASTER Act): frutos de cáscara '
     '(almendra del orgeat), huevo (sours) y leche (flips); los sulfitos de vinos y vermuts se declaran como '
     'sensibilidad (no están entre los 9; en UK sí, entre los 14)'),
    (('02', 'Coctelería Clásica', 'B17'), 'FDA Food Code: el hielo es un alimento. Pala o pinzas, nunca el vaso; la '
     'pala se guarda fuera del hielo o con el mango hacia fuera'),
    (('02', 'Cerveza y Grifo', 'B6'), 'Presión de CO₂ en PSI: la que fijó tu técnico de draft o tu distribuidor para '
     'cada sistema (temperatura, altitud, tipo de gas); sin la cifra española en bar'),
    (('02', 'Cerveza y Grifo', 'B8'), 'Barriles a 38 °F (Brewers Association, Draught Beer Quality Manual); coletilla '
     '«— log reading: ____ °F»'),
    (('02', 'Vinos y Bodega', 'B6'), '°F: blancos y rosados a 46–50 °F (8–10 °C)'),
    (('02', 'Vinos y Bodega', 'B7'), '°F: tintos a temperatura ambiente o 61–64 °F (16–18 °C)'),
    (('02', 'Vinos y Bodega', 'B13'), '°F: bodega / vinoteca a 54–61 °F (12–16 °C)'),
    # 03
    (('03', 'Diario Manager', 'B16'), 'EE. UU.: edad legal para beber 21 en todos los estados; pedir ID a quien la '
     'política de la casa diga; nunca servir a quien esté visiblemente ebrio; aforo = el cartel del fire marshal '
     '(occupancy limit). UK: Challenge 25'),
    (('03', 'Semanal Manager', 'B15'), 'Añade: y que quien sirva alcohol tenga vigente el curso de servicio responsable '
     '(TIPS, ServSafe Alcohol u otro aprobado) donde el estado lo exija'),
    (('03', 'Semanal Manager', 'B19'), _TEMP_FRIO),
    (('03', 'Mensual Manager', 'B13'), _LINEAS),
    (('03', 'Mensual Manager', 'B15'), _TEMP_FRIO),
    (('03', 'Mensual Manager', 'B17'), _A[('05', 'Trimestral y Anual', 'B23')]),
    (('03', 'Mensual Manager', 'B23'), _A[('03', 'Diario Manager', 'B29')]),
    # 04
    (('04', 'Barback', 'B18'), _A[('01', 'Apertura Sala', 'B19')]),
    # 05
    (('05', 'Instrucciones', 'B12'), 'Describe la lista US de la hoja «Quarterly & Annual»: control de plagas, '
     'extintores, campana y sistema de extinción (si hay cocina), gas y calefactores de patio, servicio del sistema '
     'de draft, frío, filtros de agua, legionela, música y ruido, licencia de alcohol y permiso de patio, seguros y '
     'licencias de música, POS / sales tax. Sin DDD, BIE, limitador acústico ni facturación española'),
    (('05', 'Mantenimiento Mensual', 'B6'), _LINEAS),
    (('05', 'Inventario', 'C44'), 'Manda la fecha del barril (ver la nota): sin el «3-5 días»'),
    (('05', 'Inventario', 'D44'), 'Barril conectado a CO₂: manda la fecha del barril (Brewers Association: sin '
     'pasteurizar 45-60 días, pasteurizada 90-120 días desde el envasado) con el sistema equilibrado y las líneas '
     'limpias cada 2 semanas; los «3-5 días» solo valen para bombas de aire (party pumps)'),
    # 06
    (('06', 'Nochevieja', 'B10'), 'Champán / espumoso para el brindis de medianoche; SIN uvas ni cava'),
    (('06', 'Nochevieja', 'B15'), 'Champán / espumoso (sin cava)'),
    (('06', 'Nochevieja', 'B16'), _A[('06', 'Navidad', 'B23')]),
    (('06', 'Nochevieja', 'B17'), 'Aforo máximo del cartel del fire marshal (occupancy limit) y control de ID en la '
     'puerta (21+)'),
    (('06', 'After Work', 'B6'), 'Horario de 12 h (6:00–8:00 PM); algunos estados limitan o prohíben la happy hour '
     "(p. ej. Massachusetts): «check your state's ABC/liquor authority»"),
    # BONUS-02
    (('B02', 'Instrucciones', 'B7'), 'Añade la nota UK: bank holidays y Boxing Day; para abrir más allá del horario de '
     'tu premises licence, un Temporary Event Notice'),
])
for _fila, (_fecha, _evento, _d, _f) in CALENDARIO.items():
    if _d:
        ADAPTAR[(HOJA_CAL[0], HOJA_CAL[1], 'D%d' % _fila)] = 'Evento EN: «%s». %s' % (_evento, _d)
    if _f:
        ADAPTAR[(HOJA_CAL[0], HOJA_CAL[1], 'F%d' % _fila)] = 'Evento EN: «%s». %s' % (_evento, _f)
CELSIUS_SIN_F = frozenset()

# ==========================================================================
# REGLAS_US: las del base + las del bar (fuente única de las cifras y normas que el kit puede afirmar)
# ==========================================================================
REGLAS_US = OrderedDict(_base.REGLAS_US)
REGLAS_US.update([
    ('edad_alcohol', ('21 años para comprar o consumir alcohol, en todos los estados',
                      'National Minimum Drinking Age Act of 1984 (23 U.S.C. 158)')),
    ('servicio_responsable', ('curso de servicio responsable (TIPS, ServSafe Alcohol u otro aprobado), obligatorio en '
                              'algunos estados', '[estatal] p. ej. California RBS (AB 1221); Illinois BASSET')),
    ('ebrios', ('no servir a clientes visiblemente ebrios', '[estatal] leyes de bebidas y dram shop de cada estado')),
    ('last_call', ('hora de cierre y fin de la venta de alcohol', '[estatal] ABC / liquor authority y municipio')),
    ('happy_hour', ('happy hour y bebidas gratis restringidas o prohibidas en algunos estados',
                    '[estatal] p. ej. Massachusetts 204 CMR 4.03')),
    ('licencia_alcohol', ('renovación de la licencia de alcohol', '[estatal] ABC / liquor authority')),
    ('cerveza_temp', ('barril y servicio a 38 °F', 'Brewers Association, Draught Beer Quality Manual')),
    ('lineas', ('líneas cada 2 semanas; ácido cada 3 meses', 'Brewers Association, Draught Beer Quality Manual')),
    ('frescura_barril', ('sin pasteurizar 45-60 días; pasteurizada 90-120 días desde el envasado',
                         'Brewers Association, Draught Beer Quality Manual')),
    ('hielo', ('el hielo es un alimento: pala o pinzas, nunca el vaso', 'FDA Food Code 2022, «food» incluye el hielo')),
    ('mano_desnuda', ('sin mano desnuda en alimentos listos para consumir', 'FDA Food Code 2022 §3-301.11')),
    ('musica', ('licencias de ejecución pública: ASCAP, BMI, SESAC, GMR', '17 U.S.C. 106(4)')),
    ('ruido', ('ordenanza de ruido de la ciudad', '[local] ordenanza municipal')),
    ('aforo', ('aforo máximo del cartel (occupancy limit)', '[local] fire code')),
    ('vino_temp', ('blancos 46-50 °F · tintos 61-64 °F · bodega 54-61 °F', '[criterio del kit] °C del ES → °F')),
    ('peso_hielo', ('30-50 kg = 65-110 lb', '[criterio del kit] conversión')),
    ('uk_alcohol', ('UK: Challenge 25, personal licence, horario de la premises licence, Temporary Event Notice',
                    'Licensing Act 2003; Mandatory Licensing Conditions Order 2010')),
])
# SPEC bar §3: cada °F que el kit puede afirmar (REGLAS_US heredadas + bar)
GRADOS_F_SPEC = {-31, -4, 0, 32, 38, 41, 46, 50, 54, 61, 64, 70, 100, 135, 165}

# ==========================================================================
# Pistas y dependencias del bar (extraer_textos.py)
# ==========================================================================
PISTAS_CAMBIO = {r'Kit de Tareas': 'D2: «Bar Checklists Kit Pro»'}
PISTAS_FUERA = (r'Restaurante Casual',)
PISTAS_EXTRA = [
    (r'Bar / Cocktails', 'D2: la EN no lleva el sufijo de variante: quita «— Bar / Cocktails» (y «· Bar»)'),
    (r'[Bb]arra|[Bb]otellero', 'Jerga bar US: barra → bar; barra principal → main bar; botellero → back-bar cooler; '
                               'speed rail, well y back bar se quedan'),
    (r'[Hh]ielo|[Cc]ubeta', 'Hielo: cubeta → ice well / ice bin; pala → ice scoop; hielo pilé → crushed ice'),
    (r'[Gg]rifo|[Bb]arril|[Ll]íneas?|CO₂|[Bb]oquilla', 'Draft US: grifo → tap / faucet; barril → keg; líneas → draft '
                                                       'lines; boquilla → faucet nozzle; acoplamiento → coupler'),
    (r'[Cc]ristaler|[Ll]avavajillas de barra', 'cristalería → glassware; lavavajillas de barra → glass washer'),
    (r'[Mm]ermas|[Dd]errames', 'mermas → waste / spill log; pour cost se queda'),
    (r'[Úú]ltima ronda', 'última ronda → last call'),
    (r'[Ii]nvitaci', 'invitación → comp'),
    (r'[Cc]obrar|[Cc]uentas?\b', 'cuenta abierta → tab; cerrar cuentas → close out tabs; cobrar → cash out'),
    (r'[Aa]foro', 'aforo → occupancy limit (cartel del fire marshal)'),
    (r'[Mm]enores|DNI|[Ee]dad', 'edad legal 21; DNI → ID; comprobar la edad → check ID / card'),
    (r'[Cc]hupito', 'chupito → shot'),
    (r'[Bb]odega', 'bodega → stockroom (de vinos: wine cellar)'),
    (r'RRSS|redes', 'RRSS → social media'),
    (r'[Aa]fter[- ]?[Ww]ork', 'after-work → happy hour'),
    (r'[Cc]amarero', 'en el bar: camarero de sala o terraza → cocktail server; barback y head bartender se quedan'),
]
DEPENDENCIAS_EXTRA = OrderedDict([
    ('variante', ('Sufijo de variante «Bar / Cocktails»', r'Bar / Cocktails', 'D2: la EN no lleva sufijo')),
    ('alcohol', ('Servicio de alcohol: edad, ID, última ronda, promociones, aforo', r'[Mm]enores|DNI|[Úú]ltima ronda|'
                 r'[Hh]appy hour|gratis|[Ii]nvitaci|[Aa]foro', 'D-BAR: ID 21+, last call y promociones según el estado')),
    ('draft', ('Cerveza de barril: CO₂, temperatura, líneas', r'CO₂|[Bb]arril|[Ll]íneas? de', 'D-BAR: Brewers '
               'Association (38 °F, líneas cada 2 semanas, ácido cada 3 meses), presión en PSI')),
    ('hielo', ('Hielo como alimento', r'[Hh]ielo', 'D-BAR: FDA, el hielo es alimento: pala, nunca vaso')),
])


def _rebind(f):
    return types.FunctionType(f.__code__, globals(), f.__name__, f.__defaults__, f.__closure__)


titulo_interior = _rebind(_base.titulo_interior)
autotest = _rebind(_base.autotest)
cruzar_censo = _rebind(_base.cruzar_censo)


def cruzar_base(p_bar, p_base):
    """Lo heredado POR CELDA del base (POR_CELDA y ADAPTAR) tiene en el bar el mismo texto ES que en el base."""
    import json
    err = []

    def textos(p):
        d = {}
        for info in json.load(open(p, encoding='utf-8'))['libros'].values():
            for h, hd in info['hojas_detalle'].items():
                for coord, t in hd.get('textos', {}).items():
                    d[(info['corto'], h, coord)] = t
        return d
    tb, tr = textos(p_base), textos(p_bar)
    for nombre, claves in (('POR_CELDA', _HEREDA_POR_CELDA), ('ADAPTAR', _HEREDA_ADAPTAR)):
        for k in claves:
            if tr.get(k) != tb.get(k):
                err.append('%s heredado %r: el texto ES del bar %r ≠ base %r' % (nombre, k, tr.get(k), tb.get(k)))
    if tr.get(('03', 'Mensual Manager', 'B10'), '').split(' (')[0] != tb.get(('03', 'Mensual Manager', 'B16'), ''
                                                                             ).split(' (')[0]:
        err.append('03 Mensual B10 del bar no es la fila de fichajes del base (B16)')
    return err


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
        e += cruzar_base(pc, os.path.join(os.path.dirname(AQUI), 'censo_es.json'))
    for x in e:
        print('ERROR', x)
    print('mapas_bar.py: {} ficheros · {} pestañas · {} glosario · {} por celda · {} adaptar · {} reglas · '
          '{} errores'.format(len(FICHEROS), len(HOJAS), len(GLOSARIO), len(POR_CELDA), len(ADAPTAR),
                              len(REGLAS_US), len(e)))
    raise SystemExit(1 if e else 0)
