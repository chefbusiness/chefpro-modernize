#!/usr/bin/env python3
"""
mapas_finedining.py — Fine Dining Checklists Kit Pro (EN) · DELTA del Kit de Tareas Recurrentes: Restaurante Creativo /
De Autor (`kit-tareas-restaurante-creativo`, 13 xlsx v2.0) sobre `mapas.py` (Restaurant Checklists Kit Pro). SPEC:
`finedining/SPEC.md` (solo el delta). Decimoquinto hermano. Sesión Claude Code, 31-oct-2026.

Molde HÍBRIDO, como la heladería y el hotel (lo mide el censo):
  · 01-09 y los dos bonus: molde LIGERO (# · Tarea · Zona · Responsable · ✓ · Hora · Notas; cabeceras internas por
    sección; contadores que restan «Tarea»; CF `$E6="✓"`; sin protección; subtítulo A2 en vez de la línea de marca).
  · 10 y 11: el 08 y el 09 del kit base con la variante «Restaurante Creativo» (protegidos; el 11 con la tabla de
    billetes y el registro mensual: su POR_CELDA y su ADAPTAR se heredan del 09 con la clave renumerada; lo comprueba
    cruzar_base).

Se usa con `--kit finedining` (kit.py). Importa `mapas.py` y SOLO añade o sobrescribe lo del vertical. Las funciones del
base que leen constantes se re-enlazan a ESTE módulo. Ejecutado como script: autotest + cruce con el censo + cruce con
el base.

    python3 finedining/mapas_finedining.py
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
AQUI = os.path.dirname(os.path.abspath(__file__))              # finedining/

ORIGEN_ES = 'kit-tareas-restaurante-creativo'
N_LIBROS = 13
PRODUCTO = 'Fine Dining Checklists Kit Pro'
TITULO_SEO = "Fine Dining Checklists Kit Pro: Tasting Menu, Brigade & Chef's Table Checklist Templates for Excel"
SLUG = 'fine-dining-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_FINE_DINING_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
PRECIO_USD = 19
MARCA_ES = '— Kit de Tareas Recurrentes · Restaurante Creativo · AI Chef Pro · aichef.pro'
MARCA_EN = '— ' + PRODUCTO + ' · AI Chef Pro · aichef.pro'
VARIANTES_ES = ('Restaurante Creativo', 'De Autor')
_SUF = lambda v: [(' — Restaurante Creativo / De Autor', ' — ' + v), (' · Restaurante Creativo', ' · ' + v),  # noqa
                  (' — Restaurante Creativo', ' — ' + v)]
# heredar.py: el BASE primero (el 10 y el 11 son su 08 y su 09); luego los del molde ligero (instrucciones y pies)
MEMORIA = [('base', '', _SUF('Restaurante Casual')), ('hotel', 'hotel', _SUF('Hotel Completo')),
           ('icecream', 'icecream', _SUF('Heladería Artesanal')), ('catering', 'catering', _SUF('Catering / Eventos')),
           ('chocolate', 'chocolate', _SUF('Chocolatería')), ('pastry', 'pastry', _SUF('Pastelería / Obrador'))]
RX_CONTEXTO_PENDIENTE = (r'(?i)\b(?:hotels?(?! pans?)|guests? rooms?|front desk|housekeeping|room attendants?|pool|spa|'
                         r'ice cream shops?|scoop shops?|scoopers?|dipping cabinets?|batch freezers?|pastry shops?|'
                         r'bakery cases?|chocolate shops?|catering|banquets?|BEOs?|venues?|commissary|food trucks?|'
                         r'shift leads?|casual)\b')
NO_HEREDAR = {}
# gates_en.py G2: términos que ninguna celda EN del fine dining puede llevar (otros kits y calcos)
TERMINOS_PROHIBIDOS = (r'(?i:\b(?:hotels?(?! pans?)|housekeeping|front desk|room attendants?|ice cream shops?|scoop shops?|'
                       r'scoopers?|dipping cabinets?|pastry shops?|bakery cases?|chocolate shops?|food trucks?|'
                       r'commissary|plancha|workshops?|obrador|casual dining)\b)')
TERMINO_PROHIBIDO_EJEMPLO = 'Ask housekeeping to restock the dipping cabinet.'
# gates_en.py G2 (FRASES_OK += FRASES_OK_EXTRA): la brigada francesa que usa la cocina US, con «de» funcional ES
FRASES_OK_EXTRA = ('chef de partie', 'Chef de partie', 'CHEF DE PARTIE', 'chefs de partie', 'Chefs de partie',
                   'CHEFS DE PARTIE', 'chef de cuisine', 'Chef de cuisine', 'CHEF DE CUISINE', 'Chef de Cuisine',
                   'Chef de Partie')
REFERENCIAS_TRADUCTOR = ['finedining/SPEC.md', 'SPEC.md §0-§3 y §7.2 (brief)', 'textos_en/glosario.json (glosario de '
                         'la prosa del kit base)', 'finedining/textos_en/heredado.json', 'finedining/mapas_finedining.py: '
                         'GLOSARIO, HOJAS, FICHEROS, TITULOS, POR_CELDA, REGLAS_US', '../GLOSARIO-JERGA-ES-EN.md']
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v2.0'),
    ('keywords', "fine dining checklist, tasting menu, chef's table, fine dining steps of service, mise en place "
                 'checklist, kitchen brigade, sommelier, AI Chef Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

# ==========================================================================
# Ficheros (D5: DataForSEO US 31-oct: fine dining restaurant 135.000 · fine dining 74.000 · chef's table 33.100 ·
# tasting menu 8.100 · kitchen brigade 2.900 · fine dining steps of service 210; checklists sin volumen)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-apertura-cierre.xlsx', '01-fine-dining-opening-closing-checklist.xlsx'),
    ('02-mise-en-place-degustacion.xlsx', '02-tasting-menu-mise-en-place-checklist.xlsx'),
    ('03-id-desarrollo-menu.xlsx', '03-menu-development-rd-checklist.xlsx'),
    ('04-tareas-brigada-creativa.xlsx', '04-kitchen-brigade-duties-by-role.xlsx'),
    ('05-tareas-semanales-mensuales.xlsx', '05-fine-dining-weekly-monthly-maintenance-checklist.xlsx'),
    ('06-sumiller-maridajes.xlsx', '06-sommelier-wine-pairing-checklist.xlsx'),
    ('07-chefs-table-eventos.xlsx', '07-chefs-table-special-events-checklist.xlsx'),
    ('08-fotografia-storytelling.xlsx', '08-food-photography-social-media-press-checklist.xlsx'),
    ('09-plantilla-personalizable.xlsx', '09-blank-fine-dining-checklist-template.xlsx'),
    ('10-apertura-cierre-negocio.xlsx', '10-restaurant-opening-closing-checklist.xlsx'),
    ('11-apertura-cierre-caja.xlsx', '11-cash-drawer-opening-closing.xlsx'),
    ('BONUS-01-briefing-servicio.xlsx', 'BONUS-01-fine-dining-pre-shift-meeting-template.xlsx'),
    ('BONUS-02-calendario-anual.xlsx', 'BONUS-02-fine-dining-annual-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)
TITULOS = OrderedDict([
    ('01-fine-dining-opening-closing-checklist.xlsx',
     'Fine Dining Opening & Closing Checklist: Kitchen, Modernist Equipment & Dining Room'),
    ('02-tasting-menu-mise-en-place-checklist.xlsx',
     'Tasting Menu Mise en Place Checklist: Long, Mid & Same-Day Prep + Plating Bible'),
    ('03-menu-development-rd-checklist.xlsx', 'Menu Development & R&D Checklist: Test Sessions & Recipe Documentation'),
    ('04-kitchen-brigade-duties-by-role.xlsx',
     'Kitchen Brigade Duties by Role: Executive Chef, Sous Chef, Chefs de Partie, Pastry, Sommelier & Maître'),
    ('05-fine-dining-weekly-monthly-maintenance-checklist.xlsx',
     'Fine Dining Weekly, Monthly, Quarterly & Annual Checklists'),
    ('06-sommelier-wine-pairing-checklist.xlsx', 'Sommelier & Wine Pairing Checklist: Tasting Menu Pairing & Wine Cellar'),
    ('07-chefs-table-special-events-checklist.xlsx', "Chef's Table & Special Events Checklist: Pop-Ups & Wine Dinners"),
    ('08-food-photography-social-media-press-checklist.xlsx',
     'Food Photography, Social Media & Press Checklist (Storytelling & Guides)'),
    ('09-blank-fine-dining-checklist-template.xlsx', 'Blank Fine Dining Checklist Templates (Editable)'),
    ('10-restaurant-opening-closing-checklist.xlsx', 'Restaurant Opening & Closing Checklist (Whole Building)'),
    ('11-cash-drawer-opening-closing.xlsx', 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log'),
    ('BONUS-01-fine-dining-pre-shift-meeting-template.xlsx', 'BONUS: Fine Dining Pre-Shift Meeting Template'),
    ('BONUS-02-fine-dining-annual-calendar.xlsx', 'BONUS: Fine Dining Annual Calendar: Menu Changes, Key Dates & Seasons (US)'),
])
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

HOJAS = OrderedDict(_base.HOJAS)
HOJAS.update([
    ('Apertura AM', 'AM Opening'), ('Cierre PM', 'PM Closing'),
    ('Pre-elab Largo', 'Long-Lead Prep'), ('Pre-elab Medio', 'Mid-Lead Prep'), ('Pre-elab Día', 'Same-Day Prep'),
    ('Plating Bible', 'Plating Bible'),
    ('Sesiones I+D', 'R&D Sessions'), ('Documentación', 'Recipe Documentation'),
    ('Chef Ejecutivo', 'Executive Chef'), ('Sous-Chef', 'Sous Chef'), ('Partida Caliente', 'Hot Line'),
    ('Partida Fría', 'Garde Manger'), ('Chef Pastelero', 'Pastry Chef'), ('Sumiller', 'Sommelier'),
    ('Maître-Sala', 'Maître & Dining Room'),
    ('Semanales', 'Weekly'), ('Mensuales', 'Monthly'),
    ('Maridaje Menú', 'Tasting Menu Pairing'), ('Gestión Bodega', 'Wine Cellar'),
    ("Chef's Table", "Chef's Table"), ('Pop-ups', 'Pop-Up Events'), ('Cenas Especiales', 'Special Dinners'),
    ('Fotografía Platos', 'Food Photography'), ('RRSS', 'Social Media'), ('Prensa-Guías', 'Press & Guides'),
    ('Plantilla A', 'Template A'), ('Plantilla B', 'Template B'), ('Plantilla C', 'Template C'),
    ('Briefing Servicio', 'Pre-Shift Meeting'), ('Calendario Anual', 'Annual Calendar'),
])
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Apertura AM', 'Cierre PM']),
    ('02', ['Instrucciones', 'Pre-elab Largo', 'Pre-elab Medio', 'Pre-elab Día', 'Plating Bible']),
    ('03', ['Instrucciones', 'Sesiones I+D', 'Documentación']),
    ('04', ['Instrucciones', 'Chef Ejecutivo', 'Sous-Chef', 'Partida Caliente', 'Partida Fría', 'Chef Pastelero',
            'Sumiller', 'Maître-Sala']),
    ('05', ['Instrucciones', 'Semanales', 'Mensuales', 'Trimestral y Anual']),
    ('06', ['Instrucciones', 'Maridaje Menú', 'Gestión Bodega']),
    ('07', ['Instrucciones', "Chef's Table", 'Pop-ups', 'Cenas Especiales']),
    ('08', ['Instrucciones', 'Fotografía Platos', 'RRSS', 'Prensa-Guías']),
    ('09', ['Instrucciones', 'Plantilla A', 'Plantilla B', 'Plantilla C']),
    ('10', ['Instrucciones', 'Apertura del Negocio', 'Cierre del Negocio']),
    ('11', ['Instrucciones', 'Apertura de Caja', 'Cierre de Caja', 'Registro Mensual']),
    ('B01', ['Instrucciones', 'Briefing Servicio']),
    ('B02', ['Instrucciones', 'Calendario Anual']),
])

# ==========================================================================
# GLOSARIO: el base (opcional) + celdas cortas de un fine dining US (brigada: executive chef, sous chef, chef de
# partie, garde manger, pastry chef, sommelier, maître d'; FOH: dining room, the pass, wine cellar)
# ==========================================================================
GLOSARIO = OrderedDict(_base.GLOSARIO)
_GLOSARIO_FD = OrderedDict([
    ('AI Chef Pro · aichef.pro — Kit de Tareas: Restaurante Creativo / De Autor', 'AI Chef Pro · aichef.pro — ' + PRODUCTO),
    ('Hora', 'Time'), ('Semestral', 'Semiannual'),
    # zonas (columna C del molde ligero); 1 sobrescribe el base: Sala (FOH → Dining room)
    ('Sala', 'Dining room'), ('I+D', 'R&D'), ('Emplatado', 'Plating'), ('Maridaje', 'Pairing'), ('RRSS', 'Social media'),
    ('Eventos', 'Events'), ('Fotografía', 'Photography'), ('Sumiller', 'Sommelier'), ('Pastelería', 'Pastry'),
    ('Maître', "Maître d'"), ('Bodega', 'Wine cellar'), ('Fichas', 'Recipe cards'), ('Proveedores', 'Suppliers'),
    ('Cámara', 'Walk-in'), ('Stock', 'Inventory'), ('Frío', 'Garde manger'), ('Food cost', 'Food cost'),
    ("Chef's table", "Chef's table"), ('Técnica', 'Technique'), ('Caliente', 'Hot line'),
    ('Storytelling', 'Storytelling'), ('Mise en place', 'Mise en place'), ('Prensa', 'Press'), ('Pase', 'The pass'),
    ('Marketing', 'Marketing'),
    # tabla de vida útil en congelación del 05 «Semanales» (Familia / Vida útil y 4 cadencias del base ya están)
    ('6-12 meses', '6–12 months'), ('3-6 meses', '3–6 months'), ('3-4 meses', '3–4 months'),
    ('No congelar', 'Do not freeze'),
    # BONUS-02 (cabeceras y demanda)
    ('Mes', 'Month'), ('Acciones clave / Fechas señaladas', 'Key Actions / Key Dates'),
    ('Producto estrella', 'Star Ingredients'), ('Demanda', 'Demand'), ('Alta', 'High'), ('Media', 'Medium'),
    ('Baja', 'Low'), ('Muy alta', 'Very high'), ('✓', '✓'),
])
GLOSARIO.update(_GLOSARIO_FD)
GLOSARIO_OPCIONAL = frozenset(_base.GLOSARIO) | frozenset({'Baja', 'Muy alta', '✓'})
PUESTOS_ES = frozenset(_base.PUESTOS_ES | {
    'I+D', 'Emplatado', 'Maridaje', 'RRSS', 'Eventos', 'Fotografía', 'Sumiller', 'Pastelería', 'Maître', 'Bodega',
    'Fichas', 'Proveedores', 'Cámara', 'Stock', 'Frío', 'Food cost', "Chef's table", 'Técnica', 'Caliente',
    'Storytelling', 'Mise en place', 'Prensa', 'Pase', 'Marketing'})

# ==========================================================================
# CLAVES: «Tarea» (los contadores del molde ligero restan las cabeceras internas)
# ==========================================================================
CLAVES = OrderedDict(_base.CLAVES)
CLAVES.update([('Tarea', 'Task')])

# CF_POR_CELDA (desviación DECLARADA, la del catering, la heladería y el hotel): en las hojas cuyo rango de CF contiene
# una cabecera interna («Tarea» en B, «✓» en E) la EN excluye esas filas. La lista la fija el censo (cruzar_censo
# exige que coincida): F1
_CF_HOJAS = [('01', 'Apertura AM', 'A6:G46'), ('01', 'Cierre PM', 'A6:G33'), ('02', 'Pre-elab Largo', 'A6:G27'),
             ('02', 'Pre-elab Medio', 'A6:G18'), ('02', 'Pre-elab Día', 'A6:G28'), ('02', 'Plating Bible', 'A6:G28'),
             ('03', 'Sesiones I+D', 'A6:G34'), ('03', 'Documentación', 'A6:G41'), ('04', 'Maître-Sala', 'A6:G20'),
             ('05', 'Semanales', 'A6:G35'), ('05', 'Mensuales', 'A6:G33'), ('05', 'Trimestral y Anual', 'A6:G37'),
             ('06', 'Maridaje Menú', 'A6:G24'), ('06', 'Gestión Bodega', 'A6:G27'), ('07', "Chef's Table", 'A6:G20'),
             ('07', 'Pop-ups', 'A6:G19'), ('07', 'Cenas Especiales', 'A6:G34'), ('08', 'Fotografía Platos', 'A6:G20'),
             ('08', 'RRSS', 'A6:G20'), ('08', 'Prensa-Guías', 'A6:G18'), ('B01', 'Briefing Servicio', 'A6:G37')]
CF_POR_CELDA = OrderedDict(((c, h, sq), ('$E6="✓"', 'AND($E6="✓",$B6<>"%s")' % CLAVES['Tarea']))
                           for c, h, sq in _CF_HOJAS)
LIBROS_SIN_MARCA = ('01', '02', '03', '04', '05', '06', '07', '08', '09', 'B01', 'B02')

# ==========================================================================
# Caja (D12): el 11 es el 09 del base (mismas filas 27-42 y mismo resumen)
# ==========================================================================
HOJA_CAJA = ('11', 'Cierre de Caja')
DENOMINACIONES = list(_base.DENOMINACIONES)
VALORES_DENOMINACION_EN = sorted({d[4] for d in DENOMINACIONES})
FORMULAS_POR_CELDA = OrderedDict(
    ((HOJA_CAJA[0], HOJA_CAJA[1], 'C%d' % f), ('=B%d*%s' % (f, _num(xes)), '=B%d*%s' % (f, _num(xen))))
    for f, _es, xes, _en, xen in DENOMINACIONES)
_R = lambda k: ('11',) + k[1:] if k[0] == '09' else (('10',) + k[1:] if k[0] == '08' else k)  # noqa: E731

# ==========================================================================
# BONUS-02 (A mes · B acciones y fechas · C producto estrella · D demanda · E ✓ · F notas; filas 5-16). A y D por
# glosario; B y C = traductor con ADAPTAR (fechas US). CALENDARIO = fila → ADAPTAR de B
# ==========================================================================
HOJA_CAL = ('B02', 'Calendario Anual')
FILAS_CALENDARIO = range(5, 17)
CALENDARIO = OrderedDict([
    (5, 'Sin cambios de fecha: menú de Año Nuevo (1 ene) y planificación anual; trufa negra y caza (si tu proveedor la '
        'tiene: la caza silvestre no se vende en EE. UU., va de granja con inspección)'),
    (6, "San Valentín se queda (Valentine's Day, 14 feb): menú degustación para parejas"),
    (7, 'Sin el «19 mar — Día del Padre» español: Father\'s Day US es el 3.er domingo de junio (fila de junio); '
        'añade St. Patrick\'s (17 mar) solo si encaja con tu casa'),
    (8, 'Semana Santa → Easter y Passover (fechas variables); comuniones → spring celebrations y graduaciones '
        '(mayo-junio): grupos de mediodía, menú cerrado y depósito'),
    (9, "Día de la Madre US: 2.º domingo de mayo (no el 1.º); comuniones → graduaciones; Memorial Day (último lunes)"),
    (10, "Últimas comuniones → graduaciones y bodas; Father's Day (3.er domingo de junio); terraza → patio"),
    (11, 'Añade el 4 de julio (Independence Day): decidir horario'),
    (12, 'Sin el 15 ago (Asunción): agosto US sin festivo federal; vacaciones del equipo escalonadas'),
    (13, 'Añade Labor Day (1.er lunes de septiembre); cenas maridaje de vendimia (harvest) con bodegas'),
    (14, 'Halloween (31 oct) si encaja; festival gastronómico local de otoño'),
    (15, 'Sin «1 nov Todos los Santos»: Thanksgiving (4.º jueves de noviembre): decidir si se abre o menú prix fixe; '
         'reservas de diciembre abiertas'),
    (16, 'Sin el puente 6-8 dic: holiday parties (cenas de empresa), Christmas Eve / Christmas (muchos cierran el 25), '
         "New Year's Eve (menú de gala, brindis con champán solo 21+)"),
])

# ==========================================================================
# POR_CELDA: lo heredado del base (el 09 entero → 11) + lo del fine dining
# ==========================================================================
_HEREDA_POR_CELDA = [k for k in _base.POR_CELDA if k[0] == '09']
POR_CELDA = OrderedDict((_R(k), _base.POR_CELDA[k]) for k in _HEREDA_POR_CELDA)
# 05 · Trimestral y Anual: servicios contratados y papeles de un restaurante US (sin DDD, BIE, RGSEAA, Verifactu ni
# «empresa homologada»). (fila → B, F); F = None si la cadencia del ES se queda (glosario)
_T05 = ('05', 'Trimestral y Anual')
_SERVICIOS_05 = OrderedDict([
    (6, ('Pest control by a licensed pest management company: service visit and signed service report on file',
         'Monthly')),
    (7, ('Hood and duct cleaning by a certified contractor at the NFPA 96 frequency for your cooking volume (quarterly '
         'if high volume, semiannual if moderate): service report on file', 'Semiannual')),
    (8, ('Optional third-party food safety audit or ATP swab testing to verify your cleaning plan', None)),
    (9, ('Review your food safety plan (HACCP where your health department or a variance requires one, e.g. sous vide or '
         'reduced oxygen packaging) and supplier approvals: the menu changes of the year', None)),
    (10, ('Check food handler cards are current for the whole brigade, extras included (as your state requires), and '
          'that a certified food protection manager is on staff (FDA Food Code 2-102.12)', None)),
    (11, ('Check your health permit covers your current activity and equipment (sous vide, curing, dry aging and '
          'reduced oxygen packaging may need a variance)', None)),
    (15, ('Gas lines and appliance connections checked by a licensed pro (as often as your local code requires)',
          'Annual')),
    (16, ('Refrigeration and dry-aging cabinets serviced by an EPA 608-certified tech: coils, gaskets, probes, defrost '
          'and refrigerant leak check', None)),
    (19, ('Calibrate probes and thermometers in ice water (32 °F) and log any offset', None)),
    (20, ('Used cooking oil pickup by a licensed recycler: file the pickup receipts', None)),
    (24, ('Annual extinguisher maintenance by a licensed fire protection company: new tag and record (OSHA '
          '1910.157(e)(3)); hood fire suppression system every 6 months (NFPA 96)', None)),
    (25, ('Fire alarm inspection (NFPA 72) and emergency lighting tests (NFPA 101: 30 s monthly, 90 min yearly)', None)),
    (26, ('Legionella water management program (ASHRAE 188) only if you have a cooling tower, decorative fountain or '
          'high-risk hot water system', None)),
    (27, ('Electrical maintenance (NFPA 70B): infrared scan of main panels by a qualified electrician', 'Annual')),
    (28, ('Emergency action plan review and evacuation walk-through with kitchen and dining room staff, as your local '
          'fire code requires', None)),
    (32, ("Review insurance (general liability, property, liquor liability, workers' comp): limits, capacity and covered "
          "activities (chef's table, pop-ups, off-site events)", None)),
    (33, ("File the quarter's time records (FLSA: time cards 2 years, payroll 3 years; some states require longer) and "
          'review overtime and new-hire paperwork (Form I-9)', None)),
    (34, ('POS check: software updates, sales tax rates and settings, user permissions and PCI DSS for card data',
          None)),
    (36, ('Renew permits and licenses: business license, health permit, liquor license and, if you have one, outdoor '
          'dining permit; insurance renewal dates', None)),
])
for _f, (_b, _cad) in _SERVICIOS_05.items():
    POR_CELDA[_T05 + ('B%d' % _f,)] = _b
    if _cad:
        POR_CELDA[_T05 + ('F%d' % _f,)] = _cad
# 10 · Cierre (errata ES): «Retirar decoración» y «Actualizar carta de vinos» van DESPUÉS de activar la alarma y cerrar
# con llave, y las persianas se cierran antes de recoger la señalización. Mismas 15 filas (E = «Close»): sala → patio y
# señalización → caja → papeleras → el local → persiana, alarma y llave al final (como el 18 del hotel)
_CN = ('10', 'Cierre del Negocio')
_CIERRE_10 = [  # fila ES de origen, EN, zona EN, responsable EN
    (5, 'Turn off background music', 'General', 'Shift manager'),
    (6, 'Check no guests are left in the restaurant', 'Dining room', 'Shift manager'),
    (18, 'Remove fresh table decorations', 'Dining room', 'Shift manager'),
    (19, 'Update the wine list if anything changed', 'Dining room', 'Shift manager'),
    (7, 'Clean up and bring in the patio, if you have one', 'Patio', 'Shift manager'),
    (12, 'Bring in the outdoor signage', 'Outside', 'Shift manager'),
    (8, 'Turn off the POS / card terminal (or leave it on standby)', 'Register', 'Shift manager'),
    (14, 'Empty trash cans in common areas and restrooms', 'Restrooms', 'Shift manager'),
    (13, 'Check that windows are closed', 'General', 'Shift manager'),
    (11, 'Turn off HVAC', 'General', 'Shift manager'),
    (10, 'Turn off lights (leave security lighting on)', 'General', 'Shift manager'),
    (15, 'Final safety check (gas, water, outlets)', 'General', 'Shift manager'),
    (9, 'Close the security gate / shutters and doors', 'Entrance', 'Last one out'),
    (16, 'Arm the alarm', 'Entrance', 'Last one out'),
    (17, 'Lock up and verify it is locked', 'Entrance', 'Last one out'),
]
_RESPONSABLE_CAMBIA = frozenset({18, 19, 9, 16})
for _fila, (_o, _b, _c, _d) in enumerate(_CIERRE_10, 5):
    for _col, _v in (('B', _b), ('C', _c), ('D', _d)):
        POR_CELDA[_CN + ('%s%d' % (_col, _fila),)] = _v
for _f, _es, _xes, _en, _xen in DENOMINACIONES:
    POR_CELDA[(HOJA_CAJA[0], HOJA_CAJA[1], 'A%d' % _f)] = _en
VALORES_EN = OrderedDict()

# ==========================================================================
# ADAPTAR (en español, con el dato US; cifras y normas de REGLAS_US)
# ==========================================================================
_A = _base.ADAPTAR
_HACCP_KIT = _base._HACCP_KIT
_TEMP_FRIO = _base._TEMP_FRIO
_LOG = 'coletilla «— log reading: ____ °F»'
_TIRA = 'sanitizante aprobado a la concentración de la etiqueta, medida con tira (test strip) (FDA Food Code 4-501.114)'
_PARASITOS = ('Pescado crudo o poco hecho (tartar, ceviche, crudo, marinado, curado o ahumado en frío, es decir, que no '
              'llega a 145 °F): destrucción de parásitos de la FDA Food Code 3-402.11: congelado a −4 °F o menos 7 días, '
              'o a −31 °F hasta sólido y 15 h a −31 °F, o a −31 °F hasta sólido y 24 h a −4 °F; carta o registro del '
              'proveedor guardado 90 días (3-402.12) y aviso al consumidor en la carta (3-603.11). Sin «anisakis» ni '
              '«−20 °C 24 h»; el ácido del ceviche no sustituye a la congelación')
_ALERGENOS = ('Alérgenos US: los 9 principales (FALCPA + FASTER Act: leche, huevo, pescado, crustáceos, frutos de '
              'cáscara, cacahuete, trigo, soja y sésamo); aviso escrito de los de cada plato donde tu estado haya adoptado '
              'el FDA Food Code 2022 (3-602.12(C)); en UK, los 14. Sin «14 UE»')
_FICHAJE = ('Registro de fichajes US (time records): FLSA, fichajes 2 años y nóminas 3 (algunos estados piden más, p. ej. '
            'NY 6). Sin «registro de jornada» ni «4 años»')
_ALCOHOL = 'Alcohol: con la licencia del local y solo a mayores de 21 con ID (23 U.S.C. 158)'
_IVA = ('IVA → sales tax según tu estado; un service charge obligatorio es ingreso del negocio, no propina (IRS Rev. '
        'Rul. 2012-18): dilo por escrito al cliente')
_GUIAS = ('Guías US: Michelin Guide (en las ciudades que cubre), The World\'s 50 Best / North America\'s 50 Best, OAD, '
          'James Beard Awards y la prensa local; sin Repsol')
_SOUS_VIDE = ('Sous vide en EE. UU.: cocción a la temperatura y el tiempo de tu receta validada; si se enfría y se '
              'guarda en bolsa (reduced oxygen packaging), HACCP plan o variance del departamento de salud (FDA Food '
              'Code 3-502.11 / 3-502.12); enfriado de 135 °F a 70 °F en 2 h y a 41 °F en 4 h más (3-501.14)')
_HUEVO = ('63 °C → 145 °F (FDA Food Code 3-401.11, huevo para servicio inmediato); si queda poco hecho, aviso al '
          'consumidor (3-603.11)')
ADAPTAR = OrderedDict([
    # 01
    (('01', 'Instrucciones', 'B18'), _TEMP_FRIO + '; las cámaras de maduración: temperatura y humedad (% RH) dentro de '
                                     'tus parámetros'),
    (('01', 'Instrucciones', 'B19'), _FICHAJE),
    (('01', 'Apertura AM', 'B7'), _A[('01', 'Apertura Cocina', 'B7')]),
    (('01', 'Apertura AM', 'B9'), _A[('01', 'Apertura Cocina', 'B9')]),
    (('01', 'Apertura AM', 'B10'), _A[('01', 'Apertura Cocina', 'B10')]),
    (('01', 'Apertura AM', 'B12'), _A[('01', 'Apertura Cocina', 'B14')] + '; mantenedor → licensed gas technician'),
    (('01', 'Apertura AM', 'B20'), 'Cámara de maduración (dry-aging cabinet): temperatura y humedad dentro de tus '
                                   'parámetros — «log reading: ____ °F / ____ % RH»'),
    (('01', 'Apertura AM', 'B21'), _TEMP_FRIO),
    (('01', 'Apertura AM', 'B35'), '0,01 g → 0.01 g (punto decimal)'),
    (('01', 'Cierre PM', 'B6'), _TEMP_FRIO),
    (('01', 'Cierre PM', 'B10'), 'Date marking US: 7 días como máximo a 41 °F, día 1 = el de preparación (FDA Food Code '
                                 '3-501.17); la tabla de vida útil en congelación está en «Weekly» (fichero 05)'),
    (('01', 'Cierre PM', 'B32'), _FICHAJE),
    # 02
    (('02', 'Instrucciones', 'B17'), _PARASITOS),
    (('02', 'Instrucciones', 'B18'), _A[('02', 'Fríos', 'B6')]),
    (('02', 'Pre-elab Largo', 'B17'), _PARASITOS),
    (('02', 'Pre-elab Largo', 'B23'), _SOUS_VIDE),
    (('02', 'Pre-elab Medio', 'B6'), _HUEVO),
    (('02', 'Pre-elab Día', 'B18'), _PARASITOS + '; las «2 h» antes del pase son el estándar de la casa'),
    (('02', 'Pre-elab Día', 'B24'), _A[('02', 'Fríos', 'B6')]),
    # 03
    (('03', 'Instrucciones', 'B12'), '0,01g → 0.01 g'),
    (('03', 'Sesiones I+D', 'B22'), _ALERGENOS),
    (('03', 'Documentación', 'B7'), '0,01g → 0.01 g'),
    (('03', 'Documentación', 'B12'), _ALERGENOS),
    # 04
    (('04', 'Partida Fría', 'B9'), _PARASITOS),
    # 05
    (('05', 'Instrucciones', 'B15'), 'Describe la lista US de «Quarterly & Annual»: plagas (licensed pest control), '
                                     'campana y conductos NFPA 96, gas, frío EPA 608, sondas a 32 °F, aceite usado, '
                                     'extintores OSHA y extinción de campana, alarma NFPA 72 y luces de emergencia NFPA '
                                     '101, legionela ASHRAE 188 si aplica, eléctrica NFPA 70B, plan de emergencia, '
                                     'seguros, fichajes FLSA, POS y sales tax, permisos y licencias. Sin DDD, BIE, '
                                     'RGSEAA, carnés ni Verifactu'),
    (('05', 'Semanales', 'B29'), _A[('02', 'Calientes', 'B27')]),
    (('05', 'Semanales', 'A39'), 'Vida útil orientativa en congelación a 0 °F (sin «−18 °C»)'),
    (('05', 'Semanales', 'D44'), 'Si va crudo: además, la destrucción de parásitos (FDA Food Code 3-402.11: −4 °F 7 '
                                 'días o −31 °F)'),
    (('05', 'Semanales', 'D46'), 'Enfriar primero (135 °F → 70 °F en 2 h, → 41 °F en 4 h más; FDA Food Code 3-501.14) y '
                                 'congelar a 0 °F'),
    (('05', 'Mensuales', 'B26'), _FICHAJE),
    # 06
    (('06', 'Maridaje Menú', 'B23'), _ALCOHOL),
    # 07
    (('07', 'Cenas Especiales', 'B17'), _IVA),
    (('07', 'Cenas Especiales', 'B27'), _IVA + '; señal → deposit'),
    # 08
    (('08', 'Prensa-Guías', 'B16'), _GUIAS),
    # 10 (= 08 del base)
    (('10', 'Apertura del Negocio', 'B8'), _A[('08', 'Apertura del Negocio', 'B8')]),
    (('10', 'Apertura del Negocio', 'B17'), 'Terraza → patio (mesas, sillas, sombrillas o patio heaters)'),
])
# 11 (= 09 del base): el ADAPTAR del base, con la clave renumerada
_HEREDA_ADAPTAR = [k for k in _A if k[0] == '09']
for _k in _HEREDA_ADAPTAR:
    ADAPTAR[_R(_k)] = _A[_k]
for _fila, _dir in CALENDARIO.items():
    ADAPTAR[(HOJA_CAL[0], HOJA_CAL[1], 'B%d' % _fila)] = _dir
AJUSTE_MAQUETA_ES = True
CELSIUS_SIN_F = frozenset({('05', 'Semanales', 'B29')})

# ==========================================================================
# REGLAS_US: las del base + las del fine dining
# ==========================================================================
REGLAS_US = OrderedDict(_base.REGLAS_US)
REGLAS_US.update([
    ('huevo', ('huevo para servicio inmediato 145 °F 15 s; poco hecho = aviso al consumidor', 'FDA Food Code 2022 '
               '§3-401.11(A)(1); §3-603.11')),
    ('sous_vide_rop', ('reduced oxygen packaging y cocción sous vide con almacenaje: HACCP plan o variance',
                       'FDA Food Code 2022 §3-502.11, §3-502.12')),
    ('cfpm', ('certified food protection manager; food handler cards según el estado', 'FDA Food Code 2022 §2-102.12; '
              '[estatal]')),
    ('aviso_alergenos', ('aviso escrito de los alérgenos principales en lo que se sirve sin envasar', 'FDA Food Code '
                         '2022 §3-602.12(C)')),
    ('edad_alcohol', ('21 años para comprar o consumir alcohol', 'National Minimum Drinking Age Act (23 U.S.C. 158)')),
    ('licencia_alcohol', ('alcohol solo con la licencia estatal / local', '[estatal] ABC / liquor authority')),
    ('propinas_pool', ('managers y supervisors no se quedan propinas del equipo', 'FLSA, 29 U.S.C. 203(m)(2)(B)')),
    ('service_charge', ('el service charge obligatorio es ingreso del negocio, no propina', 'IRS Rev. Rul. 2012-18')),
    ('incendios', ('alarma según NFPA 72; luces de emergencia 30 s al mes y 90 min al año', 'NFPA 72; NFPA 101 §7.9.3')),
    ('electrica', ('mantenimiento eléctrico con termografía anual', 'NFPA 70B (2023)')),
    ('legionela', ('programa de gestión del agua si hay torre, fuente decorativa o agua caliente de riesgo',
                   'ASHRAE 188; CDC Legionella toolkit')),
    ('calibracion', ('calibración de sondas por el punto de hielo (32 °F)', '[criterio del kit] método; FDA Food Code '
                     '2022 §4-502.11(B)')),
    ('guias', ('Michelin Guide, World\'s 50 Best, OAD, James Beard Awards', '[criterio del kit]')),
    ('dias_fuertes', ("Valentine's, Easter, Mother's Day (2.º domingo de mayo), graduaciones, Father's Day, Thanksgiving, "
                      "holiday parties, NYE", '[criterio del kit] calendario comercial; 5 U.S.C. 6103; 36 U.S.C. 117 y '
                      '109 (base)')),
])
GRADOS_F_SPEC = {-31, -4, 0, 32, 41, 70, 100, 135, 145, 165}

# ==========================================================================
# Pistas (el ES lleva tildes: molde v2.0)
# ==========================================================================
PISTAS_CAMBIO = {r'Kit de Tareas': 'D2: «Fine Dining Checklists Kit Pro»'}
PISTAS_FUERA = (r'Restaurante Casual',)
PISTAS_EXTRA = [
    (r'Restaurante Creativo|[Dd]e [Aa]utor', 'D2: sin el sufijo «— Restaurante Creativo / De Autor»; restaurante '
                                             'creativo / de autor → fine dining restaurant; cocina de autor → signature '
                                             'cuisine / chef-driven'),
    (r'[Mm]en[uú] degustaci', 'menú degustación → tasting menu; pase → course; pase (lugar) → the pass'),
    (r'[Pp]artida|[Bb]rigada', 'brigada → brigade; partida → station; chef de partida → chef de partie; partida fría → '
                               'garde manger; partida caliente → hot line'),
    (r'[Ss]umiller|[Mm]aridaje|[Bb]odega', 'sumiller → sommelier; maridaje → pairing (wine pairing); bodega (local) → '
                                           'wine cellar; bodega (productor) → winery'),
    (r'[Mm]a[iî]tre|[Jj]efe de sala|[Ss]ala', "maître → maître d'; jefe de sala → dining room manager; sala → dining "
                                              'room; camarero → server; ayudante de sala → back server / busser; '
                                              'runner → food runner; capitán → captain'),
    (r'I\+D', 'I+D → R&D (test kitchen)'),
    (r'[Pp]re-?elab', 'pre-elaboraciones → prep (long-lead / mid-lead / same-day)'),
    (r'[Ee]mplatad|[Pp]lating', 'emplatado → plating; plating bible → plating bible'),
    (r'[Hh]idrocoloide|[Ee]sferificaci|[Gg]elificaci|xantana|agar|gellan', 'hidrocoloides → hydrocolloids; '
                                                                           'esferificación → spherification'),
    (r'[Rr]oner|[Ss]ous-?vide|[Bb]años? térmicos?', 'Roner / baño térmico → immersion circulator (water bath); '
                                                    'sous-vide → sous vide'),
    (r'[Ss]if[oó]n|N2O', 'sifón → whipping siphon (ISI); cargas de N2O → N2O chargers'),
    (r'[Dd]eshidratador|[Pp]acojet|[Aa]batidor', 'deshidratador → dehydrator; abatidor → blast chiller; Pacojet → '
                                                 'Pacojet'),
    (r'[Mm]icrobrotes|[Ff]lores comestibles', 'microbrotes → microgreens; flores comestibles → edible flowers'),
    (r'[Ff]ondo|[Gg]lac[eé]|[Dd]emi', 'fondo oscuro → brown stock; glacé → glace; demi-glace → demi-glace'),
    (r'[Mm]aduraci', 'maduración → dry aging (dry-aging cabinet)'),
    (r'[Cc]ubiertos|covers|comensal', 'cubiertos / comensales → covers / guests'),
    (r'[Ee]scandallo', 'escandallo → recipe costing / plate cost'),
    (r'[Mm]ermas', 'mermas → waste (waste log)'),
    (r'RRSS|[Rr]edes', 'RRSS → social media'),
    (r'[Gg]u[ií]as|Michelin|Repsol', 'guías → guides (Michelin Guide, World\'s 50 Best, OAD, James Beard); sin Repsol'),
    (r'[Ss]eñal|[Aa]nticipo', 'señal → deposit'),
    (r'IVA', 'IVA → sales tax'),
    (r'[Cc]omuniones|Semana Santa|Reyes|Navidad|Nochevieja|Todos los Santos|Asunci|Constituci|Inmaculada|Día del Padre|'
     r'Día de la Madre', 'calendario US (Easter, Mother\'s Day 2.º domingo de mayo, Father\'s Day 3.er domingo de junio, '
                         'Thanksgiving, holiday parties, NYE)'),
    (r'[Pp]op-?up', 'pop-up → pop-up'),
    (r"[Cc]hef's [Tt]able", "chef's table → chef's table"),
]
DEPENDENCIAS_EXTRA = OrderedDict([
    ('variante', ('Sufijo «Restaurante Creativo / De Autor»', r'Restaurante Creativo|De Autor', 'D2: la EN no lleva '
                  'sufijo')),
    ('anisakis', ('Anisakis y congelación UE', r'[Aa]nisakis|ANISAKIS', 'D10: parásitos 3-402.11 + aviso 3-603.11')),
    ('guias', ('Guías españolas', r'Repsol|Soles', 'D-FD: guías US')),
])
HOJA_HORAS = ('10', 'Apertura del Negocio')
HOJA_VERDE = ('10', 'Apertura del Negocio')
CITA_AUTOTEST = '(FDA Food Code 3-501.19)'


def _rebind(f):
    return types.FunctionType(f.__code__, globals(), f.__name__, f.__defaults__, f.__closure__)


titulo_interior = _rebind(_base.titulo_interior)
_autotest_base = _rebind(_base.autotest)
_cruzar_censo_base = _rebind(_base.cruzar_censo)
HOJAS_ES_POR_LIBRO_TODAS = frozenset(h for hs in HOJAS_ES_POR_LIBRO.values() for h in hs)


def autotest():
    err = [e for e in _autotest_base() if e != 'FICHEROS debe tener 11 nombres EN distintos']
    if len(FICHEROS) != N_LIBROS or len(set(FICHEROS.values())) != N_LIBROS:
        err.append('FICHEROS debe tener %d nombres EN distintos' % N_LIBROS)
    if CLAVES['Tarea'] != GLOSARIO['Tarea']:
        err.append('CLAVES["Tarea"] debe ser el EN de la cabecera (GLOSARIO): los contadores la restan')
    rx = re.compile(TERMINOS_PROHIBIDOS)
    if not rx.search(TERMINO_PROHIBIDO_EJEMPLO):
        err.append('TERMINO_PROHIBIDO_EJEMPLO no lo caza TERMINOS_PROHIBIDOS')
    for ok in ('restaurant', 'sommelier', "maître d'", 'sous chef', 'chef de partie', 'garde manger', 'pastry chef',
               'host stand', 'server', 'bartender', 'restaurant consultant', "chef's table"):
        if rx.search(ok):
            err.append('TERMINOS_PROHIBIDOS caza lo permitido (%r)' % ok)
    for k, v in list(GLOSARIO.items()) + list(POR_CELDA.items()) + list(CLAVES.items()):
        if (k not in _base.GLOSARIO or k in _GLOSARIO_FD) and isinstance(v, str) and rx.search(v):
            err.append('texto EN fijado con un término prohibido: %r → %r' % (k, v))
    for es in HOJAS_ES_POR_LIBRO_TODAS:
        if ',' in HOJAS[es]:
            err.append('pestaña con coma: %r' % HOJAS[es])
    if CITA_AUTOTEST.strip('()').split()[-1] in ' '.join(f for _v, f in REGLAS_US.values()):
        err.append('CITA_AUTOTEST está en REGLAS_US: G7 no la cazaría')
    rx_g7 = re.compile(r'([−-]?\d+(?:\.\d+)?)\s*(?:(?:–|-|to|and)\s*([−-]?\d+(?:\.\d+)?)\s*)?°\s*F')
    vistos = set()
    for t in [x for v_f in REGLAS_US.values() for x in v_f] + list(POR_CELDA.values()) + list(ADAPTAR.values()):
        for m in rx_g7.finditer(t):
            vistos.update(float(g.replace('−', '-')) for g in m.groups() if g)
    if vistos != {float(x) for x in GRADOS_F_SPEC}:
        err.append('°F de mapas ≠ GRADOS_F_SPEC: sobran %s, faltan %s' % (
            sorted(vistos - {float(x) for x in GRADOS_F_SPEC}), sorted({float(x) for x in GRADOS_F_SPEC} - vistos)))
    for k in list(POR_CELDA) + list(ADAPTAR) + list(CF_POR_CELDA):
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
    for k, f in cfs.items():
        if f != ['$E6="✓"']:
            continue
        _c1, r1, _c2, r2 = range_boundaries(k[2])
        interna = any(tx.get((k[0], k[1], 'B%d' % r)) == 'Tarea' for r in range(r1, r2 + 1))
        if interna != (k in CF_POR_CELDA):
            err.append('CF de «hecho» %r: cabecera interna en el rango = %s, en CF_POR_CELDA = %s' % (
                k, interna, k in CF_POR_CELDA))
    tareas_05 = {int(c[1:]) for (lb, h, c) in tx if (lb, h) == _T05 and c.startswith('B') and c[1:].isdigit()
                 and tx[(lb, h, c)] not in ('Tarea', 'Tareas completadas:')}
    sin_fijar = sorted(tareas_05 - set(_SERVICIOS_05))
    if sin_fijar != [17, 18, 35, 37]:
        err.append('05 Trimestral y Anual: filas de tarea sin POR_CELDA %r (se esperaban 17, 18, 35 y 37)' % sin_fijar)
    for fila in FILAS_CALENDARIO:
        for col in 'ABCD':
            if (HOJA_CAL[0], HOJA_CAL[1], '%s%d' % (col, fila)) not in tx:
                err.append('calendario: %s%d sin texto en el ES' % (col, fila))
    for k, t in tx.items():
        if '°C' in t and k not in CELSIUS_SIN_F:
            dic = POR_CELDA.get(k) or ADAPTAR.get(k) or ''
            if '°F' not in dic:
                err.append('°C del ES sin °F en POR_CELDA/ADAPTAR: %r → %r' % (k, t[:60]))
    # 10 cierre: permutación de 5-19 con persiana, alarma y llave al final; zona y responsable = los del ES salvo los
    # declarados
    if sorted(o for o, *_r in _CIERRE_10) != list(range(5, 20)) or [o for o, *_r in _CIERRE_10][-3:] != [9, 16, 17]:
        err.append('10 cierre: no es una permutación de 5-19 con persiana, alarma y llave al final')
    for o, _b, c_en, d_en in _CIERRE_10:
        z_es = tx.get((_CN[0], _CN[1], 'C%d' % o))
        if GLOSARIO.get(z_es) != c_en:
            err.append('10 cierre: la zona de la fila %d (%r) no es %r' % (o, z_es, c_en))
        r_es = tx.get((_CN[0], _CN[1], 'D%d' % o))
        if GLOSARIO.get(r_es) != d_en and o not in _RESPONSABLE_CAMBIA:
            err.append('10 cierre: el responsable de la fila %d (%r) no es %r' % (o, r_es, d_en))
    if not tx.get((_CN[0], _CN[1], 'B18'), '').startswith('Retirar decoración') or \
            not tx.get((_CN[0], _CN[1], 'B16'), '').startswith('Activar alarma'):
        err.append('10 cierre: el ES ya no trae la errata del orden (¿corregida en el ES?)')
    horas = sorted({(k[0], k[1]) for k, t in tx.items() if RX_HORA_CELDA.match(t)})
    if horas != [('10', 'Apertura del Negocio'), ('11', 'Apertura de Caja')]:
        err.append('horas de celda fuera del 10 «Apertura» y el 11 «Apertura de Caja»: %r' % horas)
    return err


def cruzar_base(p_fd, p_base):
    """Lo heredado POR CELDA del base (POR_CELDA y ADAPTAR del 09 → 11; el ADAPTAR del 08 B8 → 10) tiene aquí el mismo
    texto ES que en el base; la caja del 11 tiene las mismas fórmulas que el 09."""
    import json
    err = []

    def cargar(p):
        d, fx = {}, {}
        for info in json.load(open(p, encoding='utf-8'))['libros'].values():
            for h, hd in info['hojas_detalle'].items():
                for coord, t in hd.get('textos', {}).items():
                    d[(info['corto'], h, coord)] = t
                fx[(info['corto'], h)] = hd['formulas']
        return d, fx
    (tb, fb), (tf, ff) = cargar(p_base), cargar(p_fd)
    for nombre, claves in (('POR_CELDA', _HEREDA_POR_CELDA), ('ADAPTAR', _HEREDA_ADAPTAR)):
        for k in claves:
            if tf.get(_R(k)) != tb.get(k):
                err.append('%s heredado %r: ES %r ≠ base %r' % (nombre, k, (tf.get(_R(k)) or '')[:60],
                                                               (tb.get(k) or '')[:60]))
    if tf.get(('10', 'Apertura del Negocio', 'B8')) != tb.get(('08', 'Apertura del Negocio', 'B8')):
        err.append('ADAPTAR 10 B8 heredado del 08 B8: otro texto ES')
    for h in ('Cierre de Caja', 'Registro Mensual'):
        a, b = fb.get(('09', h), {}), ff.get(('11', h), {})
        diff = [d for d in sorted(set(a.items()) ^ set(b.items())) if 'COUNTIF' not in d[1]]
        if diff:
            err.append('11 %s: fórmulas distintas del 09 del base %r' % (h, diff[:4]))
    return err


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
        e += cruzar_base(pc, os.path.join(os.path.dirname(AQUI), 'censo_es.json'))
    for x in e:
        print('ERROR', x)
    print('mapas_finedining.py: {} ficheros · {} pestañas · {} glosario · {} por celda · {} cf por celda · {} adaptar · '
          '{} reglas · {} errores'.format(len(FICHEROS), len(HOJAS), len(GLOSARIO), len(POR_CELDA), len(CF_POR_CELDA),
                                          len(ADAPTAR), len(REGLAS_US), len(e)))
    raise SystemExit(1 if e else 0)
