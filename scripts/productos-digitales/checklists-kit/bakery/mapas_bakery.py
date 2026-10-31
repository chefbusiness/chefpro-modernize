#!/usr/bin/env python3
"""
mapas_bakery.py — Bakery Checklists Kit Pro (EN) · DELTA del Kit de Tareas Recurrentes: Panadería / Obrador
(`kit-tareas-panaderia`, 11 xlsx v1.1, origen ChefBusiness) sobre `mapas.py` (Restaurant Checklists Kit Pro). SPEC:
`bakery/SPEC.md` (solo el delta). Decimotercer hermano vertical y el segundo en el MOLDE PLANO (como el food truck:
`foodtruck/SPEC.md` §0 y §0.1, ganchos ya hechos). Panadería de PAN (masa madre, hornos, tienda): no pisa al Pastry Shop
Checklists Kit Pro. Sesión Claude Code, 31-oct-2026.

Se usa con `--kit bakery` (kit.py). Importa `mapas.py` y SOLO añade o sobrescribe: producto, ficheros, títulos (A2 por
POR_CELDA), pestañas, glosario de panadería US (jerga del Bakery Business Plan Kit: head baker, baker, bakery assistant,
counter staff, deck / rack oven, proofer, retarder, sourdough starter), calendario (B02: A mes · B panes · C eventos y
encargos · D mantenimiento · E formación, filas 4-15), POR_CELDA (temperaturas de proceso del ES en °F, eventos ES del
08 → US) y ADAPTAR (TCS, etiquetas y alérgenos, sin gluten, orgánico, báscula, gas, plagas, caja) y REGLAS_US. Sin caja.
Ejecutado como script: autotest + cruce con bakery/censo_es.json.

    python3 bakery/mapas_bakery.py
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
AQUI = os.path.dirname(os.path.abspath(__file__))              # bakery/ (el import * trae el AQUI del base)

ORIGEN_ES = 'kit-tareas-panaderia'
PRODUCTO = 'Bakery Checklists Kit Pro'
TITULO_SEO = 'Bakery Checklists Kit Pro: Bread Bakery Opening, Production & Closing Checklist Templates for Excel'
SLUG = 'bakery-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_BAKERY_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
VERSION_ES = '1.1'                                               # productos-changelog.ts: kit-tareas-panaderia 1.1
MARCA_ES = 'ChefBusiness.co — Kit de Tareas Recurrentes: Panaderia / Obrador Pan'
MARCA_EN = 'AI Chef Pro · aichef.pro · ' + PRODUCTO             # sin «—» (lección del food truck)
VARIANTES_ES = ('— Panaderia', 'Panaderia / Obrador')
# Molde PLANO (foodtruck/SPEC.md §0.1): ganchos de aplicar_en / gates_en / extraer_textos
MOLDE = 'plano'
CELDA_TITULO = 'A2'
FILA_CABECERA = 3
# heredar.py: el base, el food truck (mismo origen ChefBusiness y molde) y la pastelería (oficio vecino)
_SUF = lambda v: [(' — Panaderia', ' — ' + v)]                   # noqa: E731
MEMORIA = [('foodtruck', 'foodtruck', _SUF('Food Truck')), ('base', '', _SUF('Restaurante Casual')),
           ('pastry', 'pastry', _SUF('Pastelería'))]
RX_CONTEXTO_PENDIENTE = (r'(?i)\b(?:restaurants?(?! consultant)|host stands?|head chefs?|sous chefs?|MOD|FOH|'
                         r'servers?|bartenders?|bussers?|dining rooms?|patio|food trucks?|trucks?|commissary|'
                         r'generators?|propane|vending|window staff|drivers?|cakes?|patisserie|pastry shops?)\b')
NO_HEREDAR = {}
# gates_en.py G2: términos que NINGUNA celda EN de la panadería puede llevar: puestos de un restaurante, el calco
# «workshop» / «obrador» (production / bakehouse) y lo del food truck que se cuela por herencia
TERMINOS_PROHIBIDOS = (r'(?i:\b(?:restaurants?(?! consultant)|host stands?|head chefs?|sous chefs?|line cooks?|'
                       r'bussers?|barbacks?|bartenders?|servers?|dining rooms?|workshops?|obrador|plancha|'
                       r'food trucks?|window staff)\b)|\bMOD\b|\bFOH\b')
TERMINO_PROHIBIDO_EJEMPLO = 'Sweep the workshop floor.'
REFERENCIAS_TRADUCTOR = ['bakery/SPEC.md', 'foodtruck/SPEC.md §0 (molde plano)', 'SPEC.md §0-§3 y §7.2 (brief)',
                         'bakery/mapas_bakery.py: GLOSARIO, HOJAS, FICHEROS, TITULOS, POR_CELDA, REGLAS_US',
                         '../business-plans-en-2/F1-research-us-delta.md (Bakery Business Plan Kit: jerga y ratios)',
                         '../GLOSARIO-JERGA-ES-EN.md']
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v' + VERSION_ES),
    ('keywords', 'bakery checklist, bakery opening checklist, bakery cleaning checklist, bakery production schedule, '
                 'bread bakery, sourdough starter, AI Chef Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

# ==========================================================================
# Ficheros (D5): DataForSEO US 31-oct: bakery opening checklist 30 · bakery checklist / cleaning checklist / cleaning
# schedule / production schedule / opening and closing checklist 10 · bread bakery 12.100 y sourdough bakery 6.600
# (intención local: el oficio). Pan, masa madre y hornos en los nombres: no compite con el Pastry Shop Checklists Kit
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-apertura-cierre-panaderia.xlsx', '01-bakery-opening-closing-checklist.xlsx'),
    ('02-masas-madre-fermentacion.xlsx', '02-sourdough-starter-fermentation-checklist.xlsx'),
    ('03-hornos-coccion.xlsx', '03-bakery-oven-baking-checklist.xlsx'),
    ('04-expositor-venta.xlsx', '04-bakery-display-counter-checklist.xlsx'),
    ('05-tareas-manager.xlsx', '05-bakery-manager-checklist.xlsx'),
    ('06-tareas-perfiles.xlsx', '06-bakery-duties-by-role.xlsx'),
    ('07-semanales-mensuales.xlsx', '07-bakery-cleaning-maintenance-schedule.xlsx'),
    ('08-eventos-estacionales.xlsx', '08-bakery-seasonal-holiday-checklist.xlsx'),
    ('09-plantilla-personalizable.xlsx', '09-blank-bakery-checklist-template.xlsx'),
    ('BONUS-01-briefing-produccion.xlsx', 'BONUS-01-bakery-daily-production-sheet.xlsx'),
    ('BONUS-02-calendario-anual.xlsx', 'BONUS-02-bakery-annual-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)
TITULOS = OrderedDict([
    ('01-bakery-opening-closing-checklist.xlsx',
     'Bakery Opening & Closing Checklist: Overnight Bake Shift, Production & Shop'),
    ('02-sourdough-starter-fermentation-checklist.xlsx',
     'Sourdough Starter & Fermentation Checklist: Starter, Bulk, Retard & Preferments'),
    ('03-bakery-oven-baking-checklist.xlsx', 'Bakery Oven Checklist: Deck & Rack Ovens, Steam and Bake Times'),
    ('04-bakery-display-counter-checklist.xlsx',
     'Bakery Display & Counter Checklist: Bread Case, Labels & Customer Service'),
    ('05-bakery-manager-checklist.xlsx',
     'Bakery Manager Checklist: Production Planning, Flour Orders, Waste & Food Cost'),
    ('06-bakery-duties-by-role.xlsx', 'Bakery Duties by Role: Head Baker, Baker, Bakery Assistant & Counter Staff'),
    ('07-bakery-cleaning-maintenance-schedule.xlsx',
     'Bakery Weekly & Monthly Checklists: Deep Cleaning, Maintenance & Inventory'),
    ('08-bakery-seasonal-holiday-checklist.xlsx',
     'Bakery Seasonal & Holiday Checklist: Seasonal Breads, Holiday Orders & Specialties'),
    ('09-blank-bakery-checklist-template.xlsx', 'Blank Bakery Checklist Template (Editable)'),
    ('BONUS-01-bakery-daily-production-sheet.xlsx', 'BONUS: Bakery Daily Production Sheet (Pre-Shift Briefing)'),
    ('BONUS-02-bakery-annual-calendar.xlsx',
     'BONUS: Bakery Annual Calendar: Seasonal Breads, Orders, Maintenance & Training (US)'),
])
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

HOJAS = OrderedDict(_base.HOJAS)
HOJAS.update([
    ('Apertura y Cierre', 'Opening & Closing'), ('Masas Madre', 'Starter & Fermentation'),
    ('Hornos y Coccion', 'Ovens & Baking'), ('Expositor y Venta', 'Display & Counter'),
    ('Tareas Manager', 'Manager Tasks'), ('Perfiles', 'Duties by Role'), ('Semanales y Mensuales', 'Weekly & Monthly'),
    ('Eventos y Temporadas', 'Seasons & Holidays'), ('Personalizable', 'Blank Template'),
    ('Briefing Produccion', 'Daily Production Sheet'), ('Calendario Anual', 'Annual Calendar'),
])
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Apertura y Cierre']), ('02', ['Masas Madre']), ('03', ['Hornos y Coccion']),
    ('04', ['Expositor y Venta']), ('05', ['Tareas Manager']), ('06', ['Perfiles']), ('07', ['Semanales y Mensuales']),
    ('08', ['Eventos y Temporadas']), ('09', ['Personalizable']), ('B01', ['Briefing Produccion']),
    ('B02', ['Calendario Anual']),
])
HOJA_DE = OrderedDict((c, hs[0]) for c, hs in HOJAS_ES_POR_LIBRO.items())

# ==========================================================================
# GLOSARIO: el base (opcional) + las celdas cortas de la panadería. Jerga del Bakery Business Plan Kit (EN, LIVE).
# ==========================================================================
GLOSARIO = OrderedDict(_base.GLOSARIO)
_GLOSARIO_PAN = OrderedDict([
    ('ChefBusiness Consultoria Gastronomica', 'AI Chef Pro'),
    # cabeceras (fila 3)
    ('Area', 'Area'), ('Hora', 'Time'), ('OK', 'OK'), ('Observaciones', 'Notes'), ('Tipo Masa', 'Dough Type'),
    ('Tarea / Control', 'Task / Check'), ('Frecuencia', 'Frequency'), ('Valor', 'Reading'), ('Tipo Horno', 'Oven Type'),
    ('Categoria', 'Category'), ('Prioridad', 'Priority'), ('Estado', 'Status'), ('Perfil', 'Role'), ('Momento', 'When'),
    ('Periodo', 'Period'), ('Dia/Semana', 'Day / Week'), ('Temporada/Evento', 'Season / Event'),
    ('Accion / Tarea', 'Action / Task'), ('Anticipacion', 'Lead time'), ('Seccion', 'Section'),
    ('Informacion', 'Information'), ('Detalle', 'Detail'), ('Mes', 'Month'), ('Panes Temporada', 'Seasonal Breads'),
    ('Eventos/Encargos', 'Events / Orders'), ('Mantenimiento', 'Maintenance'), ('Formacion', 'Training'),
    # zonas y categorías (columna A)
    ('Obrador', 'Production'), ('Tienda', 'Shop'), ('MM Natural', 'Starter'), ('Bulk', 'Bulk'),
    ('Retardo', 'Retard'), ('Final', 'Final proof'), ('Fresca', 'Fresh yeast'), ('Seca', 'Dry yeast'),
    ('Poolish', 'Poolish'), ('Biga', 'Biga'), ('Piso', 'Deck'), ('Rotativo', 'Rack'), ('Barra/Baguette', 'Baguette'),
    ('Hogaza rustica', 'Rustic loaf'), ('Chapata', 'Ciabatta'), ('Pan integral', 'Whole wheat'),
    ('Croissant', 'Croissant'), ('Brioche', 'Brioche'), ('Masa madre', 'Sourdough'), ('Expositor', 'Display'),
    ('Venta', 'Sales'), ('Produccion', 'Production'), ('Compras', 'Purchasing'), ('Stock', 'Inventory'),
    ('Proveedores', 'Suppliers'), ('Finanzas', 'Finance'), ('RRHH', 'Staff'), ('Marketing', 'Marketing'),
    ('Invierno', 'Winter'), ('Primavera', 'Spring'), ('Verano', 'Summer'), ('Otono', 'Fall'),
    ('Todo ano', 'Year-round'), ('Sin gluten', 'Gluten-free'), ('Ecologico', 'Organic'), ('Cereales', 'Grains'),
    # puestos (jerga del Bakery Business Plan Kit)
    ('Panadero', 'Baker'), ('Oficial', 'Baker'), ('Maestro', 'Head baker'), ('Ayudante', 'Bakery assistant'),
    ('Dependiente', 'Counter staff'), ('Encargado', 'Manager'), ('Equipo', 'Team'),
    # cuándo, frecuencia, antelación, prioridad
    ('Diario', 'Daily'), ('Pre-amasado', 'Before mixing'), ('2x dia', '2× a day'), ('Cada masa', 'Every batch'),
    ('Post-amasado', 'After mixing'), ('Segun receta', 'Per recipe'), ('Pre-horneado', 'Before baking'),
    ('Noche antes', 'Night before'), ('Pre-produccion', 'Before production'), ('Horneado', 'Baking'),
    ('Post-produccion', 'After production'), ('Por hornada', 'Every bake'), ('Bajo pedido', 'On order'),
    ('Estacional', 'Seasonal'), ('Madrugada', 'Overnight'), ('Post-horneado', 'After baking'),
    ('Apertura tienda', 'Shop opening'), ('Miercoles', 'Wednesday'), ('1a semana', '1st week'),
    ('2a semana', '2nd week'), ('3a semana', '3rd week'), ('4a semana', '4th week'), ('2 semanas', '2 weeks'),
    ('1 mes', '1 month'), ('Permanente', 'Ongoing'), ('Alta', 'High'), ('Media', 'Medium'),
    ('Obligatorio', 'Required'),
])
GLOSARIO.update(_GLOSARIO_PAN)
GLOSARIO_OPCIONAL = frozenset(_base.GLOSARIO)
PUESTOS_ES = frozenset(_base.PUESTOS_ES | {'Panadero', 'Oficial', 'Maestro', 'Ayudante', 'Dependiente', 'Encargado',
                                           'Equipo', 'Mantenimiento', 'Obrador', 'Tienda'})

# Sin libro de caja (como el food truck y la taquería): la caja del día son tareas del 01 (B24, B31), del 04 (B20) y
# del 06 (B25)
HOJA_CAJA = None
DENOMINACIONES = []
VALORES_DENOMINACION_EN = []
FORMULAS_POR_CELDA = OrderedDict()

# ==========================================================================
# BONUS-02 «Annual Calendar» (A mes · B panes de temporada · C eventos y encargos · D mantenimiento · E formación;
# filas 4-15). A y C fijados (calendario US de una panadería); B, D y E = traductor. fila → (mes, eventos y encargos)
# ==========================================================================
FILAS_CALENDARIO = range(4, 16)
CALENDARIO = OrderedDict([
    (4, ('January', "New Year's and corporate orders (slow month)")),
    (5, ('February', "Super Bowl party orders, Valentine's Day, Mardi Gras king cakes (varies)")),
    (6, ('March', "St. Patrick's Day (Irish soda bread), Easter prep (date varies)")),
    (7, ('April', 'Easter and Passover (dates vary), spring weddings')),
    (8, ('May', "Mother's Day (2nd Sunday), graduations, Memorial Day")),
    (9, ('June', "Father's Day (3rd Sunday), weddings, farmers market season")),
    (10, ('July', 'Jul 4 cookouts (buns and rolls), farmers markets')),
    (11, ('August', 'Back to school, end-of-summer events')),
    (12, ('September', 'Labor Day, Rosh Hashanah (round challah, date varies)')),
    (13, ('October', 'World Bread Day (Oct 16), Halloween, fall festivals')),
    (14, ('November', 'Thanksgiving pre-orders (dinner rolls, 4th Thursday), holiday corporate orders')),
    (15, ('December', "Christmas and holiday season (peak), New Year's Eve")),
])

# ==========================================================================
# POR_CELDA: textos EN fijados
# ==========================================================================
POR_CELDA = OrderedDict()
for _f in FICHEROS:
    _c = re.match(r'^(BONUS-)?(\d+)', _f)
    _corto = ('B' if _c.group(1) else '') + _c.group(2)
    _en = FICHEROS[_f]
    _t = TITULOS[_en]
    POR_CELDA[(_corto, HOJA_DE[_corto], CELDA_TITULO)] = _t if _t.startswith('BONUS') else '%s · %s' % (_en[:2], _t)
# Temperaturas de PROCESO del ES (no son normas) en °F: sala, agua, masa y masa madre al °F entero; hornos redondeados a
# 5 °F (la costumbre US). SPEC §3
for (_corto, _celda), _v in (
        (('01', 'B10'), 'Check bakehouse temperature (72–79 °F ideal)'),
        (('01', 'F9'), 'Summer 39–46 °F, winter 64–72 °F'),
        (('02', 'B7'), 'Check starter temperature (75–82 °F ideal)'),
        (('02', 'B12'), 'Dough temperature after mixing (75–79 °F target)'),
        (('02', 'B15'), 'Cold retard (37–41 °F) if used (12–72 h)'),
        (('02', 'B19'), 'Store at 36–39 °F; check the use-by date'),
        (('03', 'B6'), 'Check deck temperature with an infrared thermometer (430–500 °F, by bread)'),
        (('03', 'B18'), '465–480 °F with steam, 18–22 min'),
        (('03', 'B19'), '445–465 °F with steam, 35–45 min'),
        (('03', 'B20'), '445 °F with steam, 20–25 min'),
        (('03', 'B21'), '430–445 °F, 30–40 min'),
        (('03', 'B22'), '375–390 °F without steam, 15–18 min'),
        (('03', 'B23'), '355–375 °F, 20–25 min'),
        (('03', 'B24'), '445–465 °F with steam, 40–50 min (by size)')):
    POR_CELDA[(_corto, HOJA_DE[_corto], _celda)] = _v
# 08 · campañas españolas (Navidad con roscón y turrón, Semana Santa, Día del Pan, Comuniones) → calendario US
for _fila, (_a, _b) in ((11, ('Holiday season', 'Stollen, panettone, holiday breads and dinner rolls; pre-orders and '
                                                'gift boxes')),
                        (12, ('Easter', 'Hot cross buns and braided Easter breads (date varies)')),
                        (13, ("Valentine's Day", 'Heart-shaped breads and pastries, gift packaging')),
                        (14, ('Halloween', 'Pumpkin bread, themed pastries')),
                        (15, ('World Bread Day', 'Oct 16: promotions, tastings, open bakehouse')),
                        (16, ('Thanksgiving', 'Pre-orders: dinner rolls, stuffing bread, pumpkin bread (4th Thursday '
                                              'of November)'))):
    POR_CELDA[('08', 'Eventos y Temporadas', 'A%d' % _fila)] = _a
    POR_CELDA[('08', 'Eventos y Temporadas', 'B%d' % _fila)] = _b
for _fila, (_mes, _ev) in CALENDARIO.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'A%d' % _fila)] = _mes
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'C%d' % _fila)] = _ev

# ==========================================================================
# ADAPTAR (en español, con el dato US; las cifras y normas salen de REGLAS_US)
# ==========================================================================
_TIRA = 'sanitizante aprobado a la concentración de la etiqueta, medida con tira (test strip) (FDA Food Code 4-501.114)'
_LIMPIAR = 'Limpiar y luego sanitizar con ' + _TIRA
_TCS = ('Las empanadas con carne y lo relleno de crema o nata son TCS: frío a 41 °F o menos o caliente a 135 °F o más '
        '(FDA Food Code 3-501.16)')
_ETIQUETAS = ('Lo que embolsas o encajas en la tienda lleva etiqueta con nombre, ingredientes, peso neto y los alérgenos '
              'principales (FDA Food Code 3-602.11); lo que se vende sin envasar, aviso escrito de alérgenos donde tu '
              'estado haya adoptado el FDA Food Code 2022 (3-602.12(C))')
_ALERGENOS = ('Alérgenos US: los 9 principales (FALCPA + FASTER Act); en panadería pesan el trigo (no «gluten»), la '
              'leche, el huevo, la soja, el sésamo (semillas), los frutos de cáscara y el cacahuete; en UK, los 14')
_SIN_GLUTEN = ('«Gluten-free» solo si lo puedes sostener: menos de 20 ppm de gluten (21 CFR 101.91), y en un obrador '
               'con harina de trigo exige separación y control estrictos; «ecológico» → organic, con harina certificada '
               'y las reglas del USDA Organic (7 CFR Part 205) para llamarlo así')
_BASCULA = ('Si vendes al peso, la báscula de la tienda debe ser legal-for-trade (NTEP) y la inspecciona weights & '
            'measures de tu estado o condado')
_CAJA = 'Cierre de caja → cash count y over/short contra el POS Z report; cambio → starting bank (cash float)'
_GAS = ('Hornos de gas: quemadores, juntas y conexiones por un técnico con licencia, con la frecuencia de tu código '
        'local; si huele a gas, no encender nada, salir y llamar a la compañía de gas o al 911 desde fuera')
ADAPTAR = OrderedDict([
    # 01
    (('01', 'Apertura y Cierre', 'B5'), 'cámara de fermentación → proofer; horno de piso → deck oven; rotativo → rack '
                                        'oven'),
    (('01', 'Apertura y Cierre', 'B22'), _ALERGENOS + '. ' + _ETIQUETAS),
    (('01', 'Apertura y Cierre', 'B23'), _TCS),
    (('01', 'Apertura y Cierre', 'B24'), 'caja registradora → POS; ' + _CAJA),
    (('01', 'Apertura y Cierre', 'B25'), _LIMPIAR),
    (('01', 'Apertura y Cierre', 'B28'), _LIMPIAR),
    (('01', 'Apertura y Cierre', 'B29'), _GAS),
    (('01', 'Apertura y Cierre', 'B31'), _CAJA),
    # 04
    (('04', 'Expositor y Venta', 'B6'), _ETIQUETAS + '. ' + _BASCULA),
    (('04', 'Expositor y Venta', 'B7'), 'napolitanas → pain au chocolat; ensaimadas → danishes (o la bollería de tu '
                                        'carta)'),
    (('04', 'Expositor y Venta', 'B8'), 'cocas → flatbreads. ' + _TCS),
    (('04', 'Expositor y Venta', 'B9'), _SIN_GLUTEN),
    (('04', 'Expositor y Venta', 'B15'), _ALERGENOS),
    (('04', 'Expositor y Venta', 'B19'), _LIMPIAR),
    (('04', 'Expositor y Venta', 'B20'), _CAJA),
    # 05
    (('05', 'Tareas Manager', 'B12'), 'El «< 8 %» es el objetivo del kit: «target under 8% (kit target)»'),
    (('05', 'Tareas Manager', 'B13'), 'Ficha de harina US: proteína %, cenizas (ash), falling number y absorción; W y P/L '
                                      '(alveógrafo europeo) solo si tu molino los da'),
    (('05', 'Tareas Manager', 'B15'), 'Food cost: «target about 30% (US bakeries run 28–35%, kit benchmark)»'),
    (('05', 'Tareas Manager', 'B19'), 'RRSS → social media (Instagram, Google Business Profile)'),
    # 06
    (('06', 'Perfiles', 'B20'), _LIMPIAR),
    (('06', 'Perfiles', 'B25'), _CAJA),
    # 07
    (('07', 'Semanales y Mensuales', 'B5'), _LIMPIAR),
    (('07', 'Semanales y Mensuales', 'B7'), _BASCULA),
    (('07', 'Semanales y Mensuales', 'B12'), 'cámara de fermentación → proofer. ' + _LIMPIAR),
    (('07', 'Semanales y Mensuales', 'B14'), _GAS),
    (('07', 'Semanales y Mensuales', 'B16'), 'APPCC → HACCP: revisar los registros de temperaturas, limpieza y alérgenos'),
    (('07', 'Semanales y Mensuales', 'B21'), 'Control de plagas por un licensed pest control operator, con su informe; el '
                                             'equipo revisa trampas y señales en el almacén de harinas'),
    # 08
    (('08', 'Eventos y Temporadas', 'B19'), _SIN_GLUTEN),
    (('08', 'Eventos y Temporadas', 'B20'), _SIN_GLUTEN),
    # BONUS-02
    (('B02', 'Calendario Anual', 'B10'), 'Sin pan gazpacho ni coca: «flatbreads, light ciabatta»'),
    (('B02', 'Calendario Anual', 'B15'), 'Sin roscón ni turrones: «panettone, stollen, holiday breads»'),
    (('B02', 'Calendario Anual', 'D4'), 'post-Navidad → post-holiday'),
    (('B02', 'Calendario Anual', 'D14'), 'pre-Navidad → pre-holiday'),
    (('B02', 'Calendario Anual', 'E4'), 'Sin roscones: «sweet enriched doughs»'),
    (('B02', 'Calendario Anual', 'E14'), 'Sin roscones: «holiday breads: panettone and stollen»'),
])
AJUSTE_MAQUETA_ES = True
CELSIUS_SIN_F = frozenset()

# ==========================================================================
# REGLAS_US: las del base + las de la panadería
# ==========================================================================
REGLAS_US = OrderedDict(_base.REGLAS_US)
REGLAS_US.update([
    ('temperaturas_proceso', ('sala 72–79 °F; agua 39–46 °F (verano) y 64–72 °F (invierno); masa 75–79 °F; masa madre '
                              '75–82 °F; retardo 37–41 °F; levadura fresca 36–39 °F; hornos 355–500 °F (piso 430–500 '
                              '°F; barra 465–480 °F; hogaza y masa madre 445–465 °F; chapata 445 °F; integral 430–445 '
                              '°F; croissant 375–390 °F; brioche 355–375 °F)',
                              '[criterio del kit] las cifras de proceso del ES convertidas (hornos redondeados a 5 °F)')),
    ('tcs_panaderia', ('empanadas con carne y rellenos de crema = TCS: 41 °F o menos / 135 °F o más',
                       'FDA Food Code 2022 §1-201.10 (TCS) y §3-501.16')),
    ('etiquetas', ('lo envasado en la tienda: etiqueta con nombre, ingredientes, peso neto y alérgenos principales; lo '
                   'no envasado: aviso escrito', 'FDA Food Code 2022 §3-602.11(B)(5) y §3-602.12(C) (FDACS, Florida; '
                   'Illinois DPH, allergen FAQ)')),
    ('gluten_free', ('«gluten-free»: menos de 20 ppm de gluten', '21 CFR 101.91')),
    ('organico', ('«organic» con las reglas del USDA National Organic Program', '7 CFR Part 205')),
    ('bascula', ('báscula de venta al peso legal-for-trade (NTEP), inspeccionada por weights & measures',
                 '[local] NIST Handbook 44 / NTEP; weights & measures del estado o condado')),
    ('gas', ('hornos de gas revisados por un técnico con licencia con la frecuencia del código local',
             '[local] código de gas (como el base, 05 B10)')),
    ('plagas', ('control de plagas por un licensed pest control operator', '[estatal] licencia de PCO (base 05 B6)')),
    ('food_cost', ('food cost de una panadería US: 28-35 % (objetivo ~30 %)', 'research US del Bakery Business Plan Kit '
                   '§4 (pos.toasttab.com) [criterio del kit]')),
    ('cottage_food', ('una panadería con tienda es un food establishment con permiso: la cottage food no aplica',
                      'research US del Bakery Business Plan Kit §9 (stateline.org; ij.org)')),
    ('dias_fuertes', ('Super Bowl, Mardi Gras, Easter, Mother\'s Day, Jul 4, Rosh Hashanah, Thanksgiving, Christmas: el '
                      'calendario de una panadería US', '[criterio del kit] calendario comercial; 5 U.S.C. 6103 (base)')),
])
GRADOS_F_SPEC = {-31, -4, 0, 36, 37, 39, 41, 46, 64, 70, 72, 75, 79, 82, 100, 135, 165, 355, 375, 390, 430, 445, 465,
                 480, 500}

# ==========================================================================
# Pistas y dependencias de la panadería (el ES va SIN tildes: las regex las toleran)
# ==========================================================================
PISTAS_CAMBIO = {r'Kit de Tareas': 'D2: «Bakery Checklists Kit Pro»'}
PISTAS_FUERA = (r'Restaurante Casual',)
PISTAS_EXTRA = [
    (r'[Pp]anader', 'D2: sin el sufijo «— Panaderia»; panadería → bakery (bread bakery en el título); panadero → baker'),
    (r'[Oo]brador', 'obrador → production / bakehouse (NUNCA «workshop»)'),
    (r'[Mm]asa madre|MM Natural|[Rr]efresco', 'masa madre → sourdough starter (starter, levain); refresco → feeding; '
                                              'masa madre (pan) → sourdough'),
    (r'[Ff]ermentaci|[Bb]ulk|pointage|[Rr]etardo', 'primera fermentación → bulk fermentation; segunda / pointage → final '
                                                   'proof; fermentación en frío → cold retard; cámara de fermentación → '
                                                   'proofer; retardadora → retarder'),
    (r'[Hh]orno|[Ss]olera|[Rr]otativo', 'horno de piso / solera → deck oven / deck; rotativo → rack oven; tiro de vapor '
                                        '→ steam damper; escoba de horno → oven brush; pirómetro → infrared thermometer'),
    (r'[Gg]re[nñ]', 'greñar / greñado → score / scoring; cuchilla → lame'),
    (r'[Aa]masad|[Dd]ivisora', 'amasar → mix; amasadora → mixer (spiral mixer); divisora → divider'),
    (r'[Hh]ogaza|[Bb]arra|[Cc]hapata|[Ii]ntegral', 'barra → baguette; hogaza → rustic loaf (boule); chapata → ciabatta; '
                                                   'integral → whole wheat'),
    (r'[Bb]oller[ií]a|[Nn]apolitana|[Ee]nsaimada', 'bollería → pastries / viennoiserie; napolitana → pain au chocolat'),
    (r'[Ee]xpositor|[Vv]itrina', 'expositor → bread display / bakery case; vitrina → display case'),
    (r'[Ee]tiquet|[Aa]l[eé]rgen', 'alérgenos US: los 9 (trigo, no «gluten»; sésamo); etiqueta de lo envasado en tienda '
                                  '(FDA Food Code 3-602.11)'),
    (r'[Ss]in gluten|[Ee]col[oó]gic', 'sin gluten → gluten-free (21 CFR 101.91); ecológico → organic (7 CFR Part 205)'),
    (r'[Mm]ermas|[Ss]obrante', 'mermas → waste; pan sobrante → day-old bread (discount, donation, breadcrumbs)'),
    (r'[Cc]aja|[Cc]ambio', 'caja → POS / register; cambio → starting bank; cierre de caja → cash count y over/short'),
    (r'[Pp]an rallado|[Tt]ostadas', 'pan rallado → breadcrumbs; tostadas → croutons / toast'),
    (r'[Cc]aducidad', 'caducidad → use-by date'),
    (r'[Bb][aá]scula', 'báscula → scale (legal-for-trade si vendes al peso)'),
    (r'[Ee]ncargo', 'encargo → special order / pre-order'),
    (r'[Cc]uadrante', 'cuadrante de turnos → shift schedule (overnight shift)'),
    (r'RRSS|[Rr]edes', 'RRSS → social media'),
    (r'[Rr]osc[oó]n|[Tt]urr[oó]n|[Mm]onas|[Tt]orrijas|[Vv]igilia|Reyes|[Cc]omuniones|San Juan|[Nn]avid|[Gg]azpacho|'
     r'[Cc]oca\b', 'calendario US: sin roscón, turrones, monas, torrijas ni Reyes; Navidad → holiday season'),
    (r'[Mm]aestro|[Oo]ficial|[Aa]yudante|[Dd]ependiente', 'maestro panadero → head baker; oficial → baker; ayudante → '
                                                         'bakery assistant; dependiente → counter staff'),
]
DEPENDENCIAS_EXTRA = OrderedDict([
    ('variante', ('Sufijo «— Panaderia» en títulos', r'— Panaderia|Panaderia / Obrador', 'D2: la EN no lleva sufijo')),
    ('alergenos', ('Alérgenos (UE 14), con o sin tilde', r'[Aa]l[eé]rgenos|AL[EÉ]RGENOS', 'D10: 9 alérgenos US; UK 14')),
    ('caja', ('Caja española', r'[Cc]aja|[Cc]ambio', 'D12: POS, starting bank, over/short')),
    ('etiquetas', ('Etiquetado de lo envasado', r'[Ee]tiquet', 'D-PAN: 3-602.11 / 3-602.12(C)')),
    ('sin_gluten', ('Sin gluten y ecológico', r'[Ss]in gluten|[Ee]col[oó]gic', 'D-PAN: 21 CFR 101.91; 7 CFR 205')),
    ('eventos_es', ('Campañas españolas', r'[Rr]osc[oó]n|[Tt]urr[oó]n|[Mm]onas|[Tt]orrijas|[Vv]igilia|Reyes|'
                    r'[Cc]omuniones|Semana Santa|Dia del Pan|[Gg]azpacho', 'D14: calendario US (POR_CELDA)')),
])


def _rebind(f):
    return types.FunctionType(f.__code__, globals(), f.__name__, f.__defaults__, f.__closure__)


titulo_interior = _rebind(_base.titulo_interior)
_autotest_base = _rebind(_base.autotest)
_cruzar_censo_base = _rebind(_base.cruzar_censo)
_SIN_CAJA = ('DENOMINACIONES debe tener las 15 filas del ES',)
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
        err.append('la panadería no tiene caja: HOJA_CAJA None y sin denominaciones ni fórmulas por celda')
    rx = re.compile(TERMINOS_PROHIBIDOS)
    if not rx.search(TERMINO_PROHIBIDO_EJEMPLO):
        err.append('TERMINO_PROHIBIDO_EJEMPLO no lo caza TERMINOS_PROHIBIDOS')
    for ok in ('restaurant consultant', 'deck oven', 'head baker', 'counter staff', 'bakehouse', 'sourdough starter'):
        if rx.search(ok):
            err.append('TERMINOS_PROHIBIDOS caza lo permitido: %r' % ok)
    for k, v in list(GLOSARIO.items()) + list(POR_CELDA.items()) + list(CLAVES.items()) + list(HOJAS.items()):
        if (k not in _base.GLOSARIO or k in _GLOSARIO_PAN) and isinstance(v, str) and rx.search(v):
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
    usados = _grados(list(POR_CELDA.values()) + list(ADAPTAR.values()) + [v for v, _f in REGLAS_US.values()])
    if usados != GRADOS_F_SPEC:
        err.append('GRADOS_F_SPEC ≠ los °F de POR_CELDA / ADAPTAR / REGLAS_US: sobra %s, falta %s'
                   % (sorted(GRADOS_F_SPEC - usados), sorted(usados - GRADOS_F_SPEC)))
    if 'restaurant' in MARCA_EN.lower() or not MARCA_EN.endswith(PRODUCTO) or '—' in MARCA_EN:
        err.append('MARCA_EN debe acabar en el nombre del producto, sin «restaurant» ni «—»')
    if 'pastry shop' in TITULO_SEO.lower() or 'bread' not in TITULO_SEO.lower():
        err.append('TITULO_SEO: panadería de pan («bread»), sin pisar al Pastry Shop Checklists Kit Pro')
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
    for k, t in tx.items():
        if '°C' in t and k not in ADAPTAR and k not in POR_CELDA and k not in CELSIUS_SIN_F:
            err.append('celda ES con °C sin ADAPTAR ni POR_CELDA: %r → %r' % (k, t[:70]))
    for c, h in HOJA_DE.items():
        if tx.get((c, h, 'A1')) != 'ChefBusiness Consultoria Gastronomica':
            err.append('molde plano: %s!A1 no es la marca (%r)' % (c, tx.get((c, h, 'A1'))))
        if not tx.get((c, h, CELDA_TITULO)):
            err.append('molde plano: %s!%s sin título' % (c, CELDA_TITULO))
        if sum(1 for (cc, hh, _x), t in tx.items() if cc == c and hh == h and t == MARCA_ES) != 1:
            err.append('molde plano: %s sin UNA línea de marca %r' % (c, MARCA_ES))
    # lo que POR_CELDA reescribe es lo que el ES dice en esa celda (°C de proceso y campañas del 08)
    for k, v in POR_CELDA.items():
        if k[2] == CELDA_TITULO or k[0] == HOJA_CAL[0]:
            continue
        es = tx.get(k, '')
        if k[0] == '08':
            continue
        if '°C' not in es:
            err.append('POR_CELDA %r: el ES no trae la temperatura que se convierte (%r)' % (k, es))
    esperado = [(('08', 'Eventos y Temporadas', 'A11'), 'Navidad'), (('08', 'Eventos y Temporadas', 'A12'), 'Semana Santa'),
                (('08', 'Eventos y Temporadas', 'A13'), 'San Valentin'), (('08', 'Eventos y Temporadas', 'A14'), 'Halloween'),
                (('08', 'Eventos y Temporadas', 'A15'), 'Dia del Pan'), (('08', 'Eventos y Temporadas', 'A16'), 'Comuniones')]
    for k, ini in esperado:
        if not tx.get(k, '').startswith(ini):
            err.append('POR_CELDA %r: el ES no empieza por %r (trae %r)' % (k, ini, tx.get(k)))
    for fila in FILAS_CALENDARIO:
        for col in 'ABCDE':
            if not tx.get((HOJA_CAL[0], HOJA_CAL[1], '%s%d' % (col, fila))):
                err.append('B02: la fila %d no trae %s en el ES' % (fila, col))
    return err


CITA_AUTOTEST = '(FDA Food Code 3-501.18)'


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
    for x in e:
        print('ERROR', x)
    print('mapas_bakery.py: {} ficheros · {} pestañas · {} glosario · {} por celda · {} adaptar · {} reglas · '
          '{} errores'.format(len(FICHEROS), len(HOJAS), len(GLOSARIO), len(POR_CELDA), len(ADAPTAR), len(REGLAS_US),
                              len(e)))
    raise SystemExit(1 if e else 0)
