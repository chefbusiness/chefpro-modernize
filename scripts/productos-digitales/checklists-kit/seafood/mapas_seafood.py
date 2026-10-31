#!/usr/bin/env python3
"""
mapas_seafood.py — Seafood Restaurant Checklists Kit Pro (EN) · DELTA del Kit de Tareas Recurrentes: Marisquería con
Vivero y APPCC (`kit-tareas-marisqueria`, 11 xlsx v1.1, origen ChefBusiness) sobre `mapas.py`. SPEC: `seafood/SPEC.md`.
Decimocuarto hermano y el tercero (último) en el MOLDE PLANO (`foodtruck/SPEC.md` §0 y §0.1: ganchos ya hechos).
Sesión Claude Code, 31-oct-2026.

Se usa con `--kit seafood` (kit.py). Importa `mapas.py` y SOLO añade o sobrescribe: producto, ficheros, títulos (A2 por
POR_CELDA), pestañas, glosario de marisquería US (raw bar, live tank, walk-in, receiving, fish / shellfish station,
FOH manager, CCP), calendario (B02: A mes · B temporada · C eventos · D mantenimiento · E formación, filas 4-15),
POR_CELDA (alérgenos US, parásitos, recepción, cocción, etiquetas de shellstock, temporadas y eventos US del 08) y ADAPTAR
(°F, vivero sin cifras inventadas, hielo, histamina, NSSP, aviso al consumidor, lonja → distribuidor) y REGLAS_US.

    python3 seafood/mapas_seafood.py
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
AQUI = os.path.dirname(os.path.abspath(__file__))              # seafood/

ORIGEN_ES = 'kit-tareas-marisqueria'
PRODUCTO = 'Seafood Restaurant Checklists Kit Pro'
TITULO_SEO = 'Seafood Restaurant Checklists Kit Pro: Raw Bar, Receiving & Opening Checklist Templates for Excel'
SLUG = 'seafood-restaurant-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_SEAFOOD_RESTAURANT_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
VERSION_ES = '1.1'                                               # productos-changelog.ts: kit-tareas-marisqueria 1.1
MARCA_ES = 'ChefBusiness.co — Kit de Tareas Recurrentes: Marisqueria'
MARCA_EN = 'AI Chef Pro · aichef.pro · ' + PRODUCTO
VARIANTES_ES = ('— Marisqueria', 'Marisquería con Vivero')
MOLDE = 'plano'
CELDA_TITULO = 'A2'
FILA_CABECERA = 3
_SUF = lambda v: [(' — Marisqueria', ' — ' + v)]                 # noqa: E731
MEMORIA = [('foodtruck', 'foodtruck', _SUF('Food Truck')), ('bakery', 'bakery', _SUF('Panaderia')),
           ('base', '', _SUF('Restaurante Casual'))]
RX_CONTEXTO_PENDIENTE = (r'(?i)\b(?:food trucks?|trucks?|commissary|window staff|generators?|propane|vending|'
                         r'drivers?|bakery|bakers?|bakehouse|sourdough|starter|proofer|ovens?|dough|bread)\b')
NO_HEREDAR = {}
# gates_en.py G2: lo que ninguna celda EN puede llevar: calcos («plancha», «mariscada», «lonja», «vivero»), la subasta de
# lonja (no es la compra US), la numeración UE de alérgenos y lo del food truck / panadería que se cuela por herencia
TERMINOS_PROHIBIDOS = (r'(?i:\b(?:plancha|mariscadas?|lonjas?|viveros?|auctions?|workshops?|obrador|food trucks?|'
                       r'window staff|butane|allergen (?:2|14))\b)|\bMOD\b')
TERMINO_PROHIBIDO_EJEMPLO = 'Confirm the order before the auction closes.'
# gates_en.py G2 (FRASES_OK += FRASES_OK_EXTRA): la uva con su eñe (ronda de revisión); no es español en la EN
FRASES_OK_EXTRA = ('Albariño', 'albariño')
REFERENCIAS_TRADUCTOR = ['seafood/SPEC.md', 'foodtruck/SPEC.md §0 (molde plano)', 'SPEC.md §0-§3 y §7.2 (brief)',
                         'seafood/mapas_seafood.py: GLOSARIO, HOJAS, FICHEROS, TITULOS, POR_CELDA, REGLAS_US',
                         '../GLOSARIO-JERGA-ES-EN.md']
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v' + VERSION_ES),
    ('keywords', 'seafood restaurant checklist, raw bar checklist, oyster bar, shellfish tags, seafood receiving, '
                 'live lobster tank, AI Chef Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

# ==========================================================================
# Ficheros (D5). DataForSEO US 31-oct: seafood restaurant 301.000 · fish market 165.000 · seafood market 90.500 ·
# oyster bar 74.000 · raw bar 9.900 (intención local: el oficio) · restaurant opening checklist 260 · raw bar setup 30;
# seafood restaurant checklist / opening checklist / shellfish tag log / seafood receiving log sin volumen
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-apertura-cierre-marisqueria.xlsx', '01-seafood-restaurant-opening-closing-checklist.xlsx'),
    ('02-vivero-lonjas-pescado.xlsx', '02-live-tank-seafood-receiving-checklist.xlsx'),
    ('03-trazabilidad-appcc-marisco.xlsx', '03-seafood-haccp-traceability-shellfish-tags.xlsx'),
    ('04-expositor-barra-mariscos.xlsx', '04-raw-bar-seafood-display-checklist.xlsx'),
    ('05-tareas-manager.xlsx', '05-seafood-restaurant-manager-checklist.xlsx'),
    ('06-tareas-perfiles.xlsx', '06-seafood-restaurant-duties-by-role.xlsx'),
    ('07-semanales-mensuales.xlsx', '07-seafood-restaurant-weekly-monthly-checklist.xlsx'),
    ('08-eventos-estacionales.xlsx', '08-seafood-seasons-events-checklist.xlsx'),
    ('09-plantilla-personalizable.xlsx', '09-blank-seafood-restaurant-checklist-template.xlsx'),
    ('BONUS-01-briefing-servicio.xlsx', 'BONUS-01-seafood-pre-shift-meeting-template.xlsx'),
    ('BONUS-02-calendario-anual.xlsx', 'BONUS-02-seafood-restaurant-annual-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)
TITULOS = OrderedDict([
    ('01-seafood-restaurant-opening-closing-checklist.xlsx',
     'Seafood Restaurant Opening & Closing Checklist: Live Tank, Display, Kitchen & Dining Room'),
    ('02-live-tank-seafood-receiving-checklist.xlsx',
     'Live Tank & Seafood Receiving Checklist: Water Quality, Suppliers & Freshness Signs'),
    ('03-seafood-haccp-traceability-shellfish-tags.xlsx',
     'Seafood HACCP & Traceability Checklist: Shellfish Tags, Allergens & Critical Control Points'),
    ('04-raw-bar-seafood-display-checklist.xlsx', 'Raw Bar & Seafood Display Checklist: Ice Display, Service & Close'),
    ('05-seafood-restaurant-manager-checklist.xlsx',
     'Seafood Restaurant Manager Checklist: Purchasing, Market Price, Waste & Food Cost'),
    ('06-seafood-restaurant-duties-by-role.xlsx',
     'Seafood Restaurant Duties by Role: Head Chef, Fish & Shellfish Stations, FOH Manager & Server'),
    ('07-seafood-restaurant-weekly-monthly-checklist.xlsx',
     'Seafood Restaurant Weekly & Monthly Checklists: Live Tank, Walk-Ins, Maintenance & Audits'),
    ('08-seafood-seasons-events-checklist.xlsx', 'Seafood Seasons & Events Checklist: US Seasons, Holidays & Regulations'),
    ('09-blank-seafood-restaurant-checklist-template.xlsx', 'Blank Seafood Restaurant Checklist Template (Editable)'),
    ('BONUS-01-seafood-pre-shift-meeting-template.xlsx', "BONUS: Seafood Pre-Shift Meeting Template (Today's Catch)"),
    ('BONUS-02-seafood-restaurant-annual-calendar.xlsx',
     'BONUS: Seafood Restaurant Annual Calendar: Seasons, Events, Maintenance & Training (US)'),
])
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

HOJAS = OrderedDict(_base.HOJAS)
HOJAS.update([
    ('Apertura y Cierre', 'Opening & Closing'), ('Vivero y Lonjas', 'Live Tank & Receiving'),
    ('Trazabilidad APPCC', 'HACCP & Traceability'), ('Expositor y Barra', 'Raw Bar & Display'),
    ('Tareas Manager', 'Manager Tasks'), ('Perfiles', 'Duties by Role'), ('Semanales y Mensuales', 'Weekly & Monthly'),
    ('Eventos y Temporadas', 'Seasons & Events'), ('Personalizable', 'Blank Template'),
    ('Briefing Servicio', 'Pre-Shift Meeting'), ('Calendario Anual', 'Annual Calendar'),
])
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Apertura y Cierre']), ('02', ['Vivero y Lonjas']), ('03', ['Trazabilidad APPCC']),
    ('04', ['Expositor y Barra']), ('05', ['Tareas Manager']), ('06', ['Perfiles']), ('07', ['Semanales y Mensuales']),
    ('08', ['Eventos y Temporadas']), ('09', ['Personalizable']), ('B01', ['Briefing Servicio']),
    ('B02', ['Calendario Anual']),
])
HOJA_DE = OrderedDict((c, hs[0]) for c, hs in HOJAS_ES_POR_LIBRO.items())

# ==========================================================================
# GLOSARIO: el base (opcional) + las celdas cortas de la marisquería
# ==========================================================================
GLOSARIO = OrderedDict(_base.GLOSARIO)
_GLOSARIO_MAR = OrderedDict([
    ('ChefBusiness Consultoria Gastronomica', 'AI Chef Pro'),
    # cabeceras
    ('Area', 'Area'), ('Hora', 'Time'), ('OK', 'OK'), ('Observaciones', 'Notes'), ('Categoria', 'Category'),
    ('Tarea / Control', 'Task / Check'), ('Frecuencia', 'Frequency'), ('Valor', 'Reading'), ('Registro', 'Record'),
    ('Detalle / Procedimiento', 'Detail / Procedure'), ('Prioridad', 'Priority'), ('Estado', 'Status'),
    ('Perfil', 'Role'), ('Momento', 'When'), ('Periodo', 'Period'), ('Dia/Semana', 'Day / Week'),
    ('Temporada/Evento', 'Season / Event'), ('Accion / Tarea', 'Action / Task'), ('Anticipacion', 'Lead time'),
    ('Seccion', 'Section'), ('Informacion', 'Information'), ('Detalle', 'Detail'), ('Mes', 'Month'),
    ('Temporada Pesca', 'Seafood Season'), ('Eventos Comerciales', 'Sales Events'), ('Mantenimiento', 'Maintenance'),
    ('Formacion', 'Training'),
    # zonas y categorías (columna A)
    ('Vivero', 'Live tank'), ('Expositor', 'Display'), ('Camaras', 'Walk-ins'), ('Barra', 'Raw bar'),
    ('Lonja', 'Buying'), ('Proveedor', 'Receiving'), ('Pescado', 'Fish'), ('Marisco', 'Shellfish'),
    ('Registro lotes', 'Lot log'), ('Etiquetado', 'Labeling'), ('Temperatura', 'Temperature'),
    ('Caducidad', 'Shelf life'), ('Descongelacion', 'Thawing'), ('Cruzada', 'Cross-contact'), ('Carta', 'Menu'),
    ('Formacion', 'Training'), ('PCC1', 'CCP 1'), ('PCC2', 'CCP 2'), ('PCC3', 'CCP 3'), ('PCC4', 'CCP 4'),
    ('PCC5', 'CCP 5'), ('Compras', 'Purchasing'), ('Stock', 'Inventory'), ('Equipo', 'Team'),
    ('Revenue', 'Revenue'), ('Calidad', 'Quality'), ('RRHH', 'Staff'), ('Marketing', 'Marketing'),
    ('Pescados', 'Fish station'), ('Mariscos', 'Shellfish station'), ('Maitre', 'FOH manager'),
    ('Pescado fresco', 'Fresh fish'), ('Marisco vivo', 'Live shellfish'), ('Fuera de carta', 'Off-menu special'),
    ('Alergenos', 'Allergens'), ('Intolerancias', 'Intolerances'), ('Reservas', 'Reservations'), ('VIP', 'VIP'),
    ('Eventos', 'Events'), ('Vinos', 'Wine'), ('Vedas', 'Seasons'), ('Regulacion', 'Regulation'),
    # puestos
    ('Jefe cocina', 'Head chef'), ('Partida salsas', 'Sauce station'), ('Partida caldos', 'Stock station'),
    ('Parrilla', 'Grill cook'), ('Plancha', 'Griddle cook'), ('Gerencia', 'Management'),
    ('Sala+Cocina', 'FOH + kitchen'),
    # cuándo, frecuencia, antelación, prioridad
    ('Diario', 'Daily'), ('2x dia', '2× a day'), ('Segun pauta', 'Per schedule'), ('Cada lote', 'Every lot'),
    ('Cada entrega', 'Every delivery'), ('Cada vez', 'Every time'), ('Permanente', 'Ongoing'), ('Siempre', 'Always'),
    ('Cada cambio', 'Every menu change'), ('Continuo', 'Ongoing'), ('Cada servicio', 'Every service'),
    ('Cada 90 min', 'Every 90 min'), ('Cada 60 min', 'Every 60 min'), ('Segun necesidad', 'As needed'),
    ('Bajo pedido', 'To order'), ('Madrugada', 'Early morning'), ('Manana', 'Morning'),
    ('Post-servicio', 'After service'), ('Cada compra', 'Every purchase'), ('Segun veda', 'Per season closures'),
    ('Miercoles', 'Wednesday'), ('1a semana', '1st week'), ('2a semana', '2nd week'), ('3a semana', '3rd week'),
    ('4a semana', '4th week'), ('1 semana', '1 week'), ('2 semanas', '2 weeks'), ('3 semanas', '3 weeks'),
    ('1 mes', '1 month'), ('Alta', 'High'), ('Media', 'Medium'),
])
GLOSARIO.update(_GLOSARIO_MAR)
GLOSARIO_OPCIONAL = frozenset(_base.GLOSARIO)
PUESTOS_ES = frozenset(_base.PUESTOS_ES | {'Jefe cocina', 'Partida salsas', 'Partida caldos', 'Parrilla', 'Plancha',
                                           'Maitre', 'Compras', 'Gerencia', 'Sala+Cocina', 'Mantenimiento', 'Marketing',
                                           'Vivero', 'Expositor', 'Camaras'})

HOJA_CAJA = None
DENOMINACIONES = []
VALORES_DENOMINACION_EN = []
FORMULAS_POR_CELDA = OrderedDict()

# ==========================================================================
# BONUS-02 (A mes · B temporada · C eventos · D mantenimiento · E formación; filas 4-15). A, B y C fijados: el producto de
# temporada US es orientativo («dates vary by state»; SPEC D14); D y E = traductor. fila → (mes, temporada, eventos)
# ==========================================================================
FILAS_CALENDARIO = range(4, 16)
CALENDARIO = OrderedDict([
    (4, ('January', 'Oysters, Dungeness and stone crab, scallops', "New Year's Day, corporate dinners")),
    (5, ('February', 'Oysters, crawfish (season starts), Dungeness crab',
         "Valentine's Day, Mardi Gras crawfish boils, Lent begins (date varies)")),
    (6, ('March', 'Crawfish, oysters, halibut (season opens in Alaska)', "Lent Fridays (fish Fridays), St. Patrick's Day")),
    (7, ('April', 'Crawfish (peak), halibut, soft-shell crabs (start)', 'Lent Fridays and Easter (date varies)')),
    (8, ('May', 'Wild salmon (season opens), soft-shell crabs, crawfish', "Mother's Day (2nd Sunday), Memorial Day")),
    (9, ('June', 'Wild salmon, soft-shell crabs, lobster', "Father's Day (3rd Sunday), summer patio and raw bar")),
    (10, ('July', 'Lobster, wild salmon, blue crab, clams', 'Jul 4 — Independence Day, peak summer, tourism')),
    (11, ('August', 'Lobster, blue crab, wild salmon, clams', 'Peak summer, clambakes and lobster bakes')),
    (12, ('September', 'Blue crab, lobster, oysters (cold-month season starts)', 'Labor Day, back to routine')),
    (13, ('October', 'Stone crab (Florida opens), king crab (Alaska), oysters',
          'Oyster and seafood festivals (local), Halloween')),
    (14, ('November', 'Dungeness crab (opener varies), bay scallops, oysters',
          'Thanksgiving (4th Thursday), Black Friday, holiday pre-sales')),
    (15, ('December', 'Oysters, Dungeness and stone crab, lobster',
          "Christmas Eve (Feast of the Seven Fishes), New Year's Eve, holiday parties")),
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
_T3 = ('03', 'Trazabilidad APPCC')
for _celda, _v in (
        # alérgenos US (la numeración 2 / 14 es la UE): pescado y crustáceos son de los 9; los moluscos, no (UK: sí)
        ('A11', 'ALLERGENS — Fish & Shellfish'), ('A12', 'Crustaceans'), ('A13', 'Molluscs'),
        ('F6', 'FDA Seafood List (market names)'),
        ('B18', 'Receiving: fresh fish at 41 °F or below; frozen food received frozen solid (0 °F or below is the '
                'common target); shellstock per NSSP rules (on ice, or shipped at 45 °F air or 50 °F internal or below), '
                'then held at 41 °F (FDA Food Code 3-202.11)'),
        ('F18', 'Reject if above 41 °F'),
        ('B20', 'Cooking: whole fish and shellfish to 145 °F for 15 s internal; comminuted fish 155 °F for 17 s; '
                'stuffed fish 165 °F (FDA Food Code 3-401.11)'),
        ('B22', 'Raw or undercooked fish (crudo, ceviche, tartare) — parasite destruction (FDA Food Code 3-402.11; '
                'some species are exempt, see 3-402.11(B)): '
                'frozen and stored at −4 °F or below for 7 days, or frozen at −31 °F or below until solid and stored at '
                '−31 °F or below for 15 h, or frozen at −31 °F or below until solid and stored at −4 °F or below for '
                '24 h; keep the record 90 days (FDA Food Code 3-402.12) and the consumer advisory on the menu (FDA Food '
                'Code 3-603.11)'),
        ('F22', 'Required (FDA Food Code 3-402.11)')):
    POR_CELDA[_T3 + (_celda,)] = _v
# Ronda de revisión (31-oct): el orden por horas del 01. Apertura «Cocina»: la descongelación (7:30 AM, ES B21) va
# tras las comprobaciones de las 7:00 AM; cierre: la cubertería de sala (11:00 PM, ES B35) tras el vivero (11:00 PM).
# Mismas filas; B, C y D (y A en el cierre) se mueven con su tarea. Sin cifras nuevas
_AC = ('01', 'Apertura y Cierre')
_MOVIDAS_01 = [  # fila destino, fila ES de origen, A EN (None = la de la fila no cambia), B EN, C EN, D EN
    (17, 21, None, "Thaw scheduled products (FIFO, lot log): in the walk-in at 41 °F or below or under cold running water at 70 °F or below (FDA Food Code 3-501.13); take vacuum-packed (ROP) frozen fish out of the bag when thawing", 'Kitchen', '7:30 AM'),
    (18, 17, None, "Mise en place sauces: cocktail sauce, mignonette, tartar, remoulade, drawn butter", 'Sauce station', '8:00 AM'),
    (19, 18, None, "Make today's fish stock / fumet", 'Stock station', '8:00 AM'),
    (20, 19, None, "Check side stock: potatoes, peppers, greens", 'Kitchen', '8:30 AM'),
    (21, 20, None, "Set up mise en place for the flat-top griddle / grill", 'Grill cook', '8:30 AM'),
    (31, 35, 'FOH', "Collect the seafood service tools, wash and store them", 'FOH', '11:00 PM'),
    (32, 31, 'Kitchen', "Fish / shellfish inventory: stock left vs. tomorrow's order", 'Head chef', '11:15 PM'),
    (33, 32, 'Kitchen', "Log today's waste (high-value product)", 'Head chef', '11:15 PM'),
    (34, 33, 'Kitchen', "Deep clean the fish area and cutting boards, then sanitize at label strength, checked with test strips (FDA Food Code 4-501.114)", 'Kitchen', '11:30 PM'),
    (35, 34, 'Kitchen', "Check walk-ins: temperature and doors closed", 'Kitchen', '11:30 PM'),
]
for _d, _o, _a, _b, _c, _h in _MOVIDAS_01:
    if _a:
        POR_CELDA[_AC + ('A%d' % _d,)] = _a
    POR_CELDA[_AC + ('B%d' % _d,)] = _b
    POR_CELDA[_AC + ('C%d' % _d,)] = _c
    POR_CELDA[_AC + ('D%d' % _d,)] = _h
POR_CELDA[('02', 'Vivero y Lonjas', 'B15')] = (
    'Paperwork for every lot: shellstock tags (harvest area and date, certified shipper number) kept 90 days after the '
    'container is emptied (FDA Food Code 3-203.12); finfish: species, origin and supplier on the invoice')
# 08 · temporadas de pesca de España → temporadas US (orientativas: «dates vary by state»; SPEC D14)
_T8 = ('08', 'Eventos y Temporadas')
for _fila, (_a, _b) in ((5, ('Winter–Spring', 'Crawfish season (Gulf states; peak in spring)')),
                        (6, ('Spring', 'Soft-shell crabs (Mid-Atlantic and Gulf)')),
                        (7, ('Spring–Summer', 'Wild salmon runs (Pacific Northwest and Alaska; openers vary)')),
                        (8, ('Summer', 'Lobster peak season (Northeast, summer and fall)')),
                        (9, ('Fall', 'Stone crab (Florida) and king crab (Alaska) seasons open')),
                        (10, ('Fall–Winter', 'Scallops: bay scallop seasons (dates vary by state)')),
                        (11, ('Sep–Apr', 'Oysters: peak in the cold months (R months)')),
                        (12, ('Year-round', 'Shrimp, farmed oysters and mussels (with seasonal closures)')),
                        # eventos españoles → US
                        (14, ('Christmas Eve', 'Feast of the Seven Fishes: special order with your distributor + '
                                               'reservations')),
                        (15, ("New Year's Eve", 'Year-end seafood towers: lobster, crab, oysters, caviar')),
                        (16, ("Valentine's Day", 'Seafood tasting menu for couples')),
                        (17, ('Lent', 'Lent Fridays: fish specials, fish fry, lobster and seafood boils')),
                        (18, ('Local festivals', 'Oyster and seafood festivals (adapt to your city)')),
                        (19, ('Summer', 'Patio and raw bar: chilled seafood, oysters, ceviche'))):
    POR_CELDA[_T8 + ('A%d' % _fila,)] = _a
    POR_CELDA[_T8 + ('B%d' % _fila,)] = _b
POR_CELDA[_T8 + ('F5',)] = 'Peak varies by year'
POR_CELDA[_T8 + ('F6',)] = 'Star item'
POR_CELDA[_T8 + ('B21',)] = ("Check your state's seasons and closures (state fish and wildlife agency, NOAA Fisheries)")
POR_CELDA[_T8 + ('B24',)] = ('Shellfish display tank: only with a health department variance and HACCP plan (FDA Food '
                             'Code); health permit current')
for _fila, (_mes, _temp, _ev) in CALENDARIO.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'A%d' % _fila)] = _mes
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'B%d' % _fila)] = _temp
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'C%d' % _fila)] = _ev

# ==========================================================================
# ADAPTAR (en español, con el dato US; cifras y normas de REGLAS_US)
# ==========================================================================
_TIRA = 'sanitizante aprobado a la concentración de la etiqueta, medida con tira (test strip) (FDA Food Code 4-501.114)'
_LIMPIAR = 'Limpiar y luego sanitizar con ' + _TIRA
_FRIO = ('Frío: 41 °F o menos (FDA Food Code 3-501.16); congelado, 0 °F o menos; coletilla «— log reading: ____ °F»')
_VIVERO = ('Temperatura del agua del vivero (live tank) por especie, según tu proveedor y el fabricante del tanque (sin '
           'las cifras del ES, que son de especies europeas); coletilla «— log reading: ____ °F»')
_HIELO = ('Expositor sobre hielo escurrido (drained ice) a 41 °F o menos (FDA Food Code 3-501.16; 3-303.12); el hielo '
          'del expositor no se usa como ingrediente (FDA Food Code 3-303.11)')
_HISTAMINA = ('Pescado formador de histamina (atún, caballa, mahi-mahi, sardina, anchoa): siempre frío; rechazar lo que '
              'llegue caliente; la cocción no destruye la histamina (FDA Fish and Fishery Products Hazards Guide, cap. 7)')
_NSSP = ('Moluscos (ostras, almejas, mejillones) solo de proveedores aprobados de la lista NSSP (Interstate Certified '
         'Shellfish Shippers List; FDA Food Code 3-201.15), con su etiqueta (tag) guardada 90 días (FDA Food Code '
         '3-203.12)')
_AVISO = 'aviso al consumidor en la carta para lo crudo o poco hecho (FDA Food Code 3-603.11)'
_DISTRIBUIDOR = ('Lonja → seafood distributor / dock-to-door supplier (en EE. UU. el restaurante no compra en subasta)')
_ALERGENOS = ('Alérgenos US: pescado y crustáceos son de los 9 principales (FALCPA + FASTER Act); los moluscos NO lo son '
              'en EE. UU. (dilo si preguntan) y sí en UK (uno de los 14); sin los números 2 y 14 de la UE')
_CAJA = 'Cierre de caja → cash count y over/short contra el POS Z report; propinas según tu tip pool (FLSA, 29 U.S.C. 203(m)(2)(B))'
_ALCOHOL = 'vino con la licencia de alcohol del local; mayores de 21 con ID (23 U.S.C. 158)'
ADAPTAR = OrderedDict([
    # 01
    (('01', 'Apertura y Cierre', 'B5'), _VIVERO),
    (('01', 'Apertura y Cierre', 'B9'), _HIELO),
    (('01', 'Apertura y Cierre', 'B11'), 'Precio y origen: en EE. UU. el origen en la carta no es obligatorio para un '
                                         'restaurante (salvo leyes estatales): estándar de la casa'),
    (('01', 'Apertura y Cierre', 'B12'), _HIELO),
    (('01', 'Apertura y Cierre', 'B14'), _FRIO + '; pescado sobre hielo en el walk-in'),
    (('01', 'Apertura y Cierre', 'B16'), _FRIO),
    (('01', 'Apertura y Cierre', 'B26'), 'Barra de aperitivos → raw bar: ostras y almejas sobre hielo. ' + _NSSP),
    (('01', 'Apertura y Cierre', 'B36'), _DISTRIBUIDOR),
    (('01', 'Apertura y Cierre', 'B37'), _CAJA),
    # 02
    (('02', 'Vivero y Lonjas', 'B5'), _VIVERO),
    (('02', 'Vivero y Lonjas', 'B13'), _DISTRIBUIDOR + '; transporte refrigerado a 41 °F o menos'),
    (('02', 'Vivero y Lonjas', 'B14'), _DISTRIBUIDOR),
    (('02', 'Vivero y Lonjas', 'B16'), 'Recepción: ' + _FRIO + '. ' + _HISTAMINA),
    (('02', 'Vivero y Lonjas', 'B19'), _DISTRIBUIDOR),
    (('02', 'Vivero y Lonjas', 'B26'), _NSSP),
    # 03 (A11-A13, F6, B18, F18, B20, B22, F22 por POR_CELDA)
    (('03', 'Trazabilidad APPCC', 'B5'), 'zona FAO → origen (país o zona de captura)'),
    (('03', 'Trazabilidad APPCC', 'B6'), 'Nombre de mercado aceptado (FDA Seafood List) + nombre científico, origen y '
                                         'método; sin el Reglamento UE'),
    (('03', 'Trazabilidad APPCC', 'B7'), 'Recepción: ' + _FRIO + '; sin los «0-2 °C» del ES'),
    (('03', 'Trazabilidad APPCC', 'B9'), 'Las «48 h» son el estándar de la casa; lo cocinado y listo para comer, date '
                                         'marking: 7 días como máximo a 41 °F (FDA Food Code 3-501.17)'),
    (('03', 'Trazabilidad APPCC', 'B10'), 'Descongelación (FDA Food Code 3-501.13); el pescado congelado al vacío (ROP) se '
                                          'saca de la bolsa al descongelar'),
    (('03', 'Trazabilidad APPCC', 'B12'), 'Crustáceos (shrimp, prawns, lobster, crab, langoustines): alérgeno principal '
                                          'US (crustacean shellfish)'),
    (('03', 'Trazabilidad APPCC', 'B13'), _ALERGENOS),
    (('03', 'Trazabilidad APPCC', 'B15'), 'Aviso escrito de alérgenos en la carta donde tu estado haya adoptado el FDA '
                                          'Food Code 2022 (3-602.12(C)); sin los símbolos UE'),
    (('03', 'Trazabilidad APPCC', 'B21'), _HIELO + '; rotación cada 2 h'),
    (('03', 'Trazabilidad APPCC', 'B23'), _LIMPIAR),
    # 04
    (('04', 'Expositor y Barra', 'B5'), _HIELO),
    (('04', 'Expositor y Barra', 'B6'), 'bogavante → lobster; langosta → spiny lobster; centollo y nécoras → crab; '
                                        'cigalas → langoustines'),
    (('04', 'Expositor y Barra', 'B7'), 'Bivalvos US: oysters, clams (littlenecks, cherrystones), mussels, razor clams. '
                                        + _NSSP),
    (('04', 'Expositor y Barra', 'B9'), 'lubina → branzino; rodaballo → turbot; besugo → sea bream; merluza → hake'),
    (('04', 'Expositor y Barra', 'B10'), 'Precio por especie; el origen, estándar de la casa'),
    (('04', 'Expositor y Barra', 'B13'), _HIELO),
    (('04', 'Expositor y Barra', 'B18'), 'Abrir (shuck) al momento; guardar la etiqueta del lote; ' + _AVISO),
    (('04', 'Expositor y Barra', 'B19'), 'plancha → flat-top griddle'),
    (('04', 'Expositor y Barra', 'B24'), _LIMPIAR),
    # 05
    (('05', 'Tareas Manager', 'B5'), _DISTRIBUIDOR + ': confirmar antes de su hora de corte'),
    (('05', 'Tareas Manager', 'B8'), 'lonja vs directo vs importación → distributor vs dock-to-door vs imported'),
    (('05', 'Tareas Manager', 'B15'), 'Producto de lonja → market price (MP) items'),
    (('05', 'Tareas Manager', 'B22'), 'El «< 32 %» es el objetivo del kit: «target under 32% (kit target)»'),
    # 06
    (('06', 'Perfiles', 'B5'), _DISTRIBUIDOR),
    (('06', 'Perfiles', 'B14'), 'Cocción: 145 °F durante 15 s en el centro (FDA Food Code 3-401.11); coletilla «— log '
                                'reading: ____ °F»'),
    (('06', 'Perfiles', 'B25'), 'Servicio de mariscada → seafood tower / seafood platter'),
    (('06', 'Perfiles', 'B26'), _ALERGENOS),
    (('06', 'Perfiles', 'B32'), _ALCOHOL),
    # 07
    (('07', 'Semanales y Mensuales', 'B5'), 'Limpieza profunda del live tank según el fabricante y tu departamento de '
                                            'salud'),
    (('07', 'Semanales y Mensuales', 'B9'), _LIMPIAR),
    (('07', 'Semanales y Mensuales', 'B15'), 'APPCC → HACCP; Sanidad → health inspection'),
    (('07', 'Semanales y Mensuales', 'B18'), 'Equipos de frío: técnico certificado EPA 608'),
    (('07', 'Semanales y Mensuales', 'B22'), 'Control de plagas por un licensed pest control operator, con su informe'),
    # 08 (A5-A12, B5-B12, F5, F6, A14-A19, B14-B19, B21, B24 por POR_CELDA)
    (('08', 'Eventos y Temporadas', 'B22'), 'Talla mínima legal por especie (langosta y cangrejo, sobre todo): la de tu '
                                            'estado'),
    (('08', 'Eventos y Temporadas', 'B23'), 'Pesca ilegal → IUU seafood (illegal, unreported, unregulated)'),
    # BONUS-01
    (('B01', 'Briefing Servicio', 'B16'), 'Sin «alérgeno 2»: «Dishes with crustacean shellfish:»'),
    (('B01', 'Briefing Servicio', 'B17'), 'Sin «alérgeno 14»: «Dishes with molluscs (UK allergen):»'),
    (('B01', 'Briefing Servicio', 'B20'), 'cubiertos → covers'),
    (('B01', 'Briefing Servicio', 'B23'), _ALCOHOL),
])
AJUSTE_MAQUETA_ES = True
CELSIUS_SIN_F = frozenset()

# ==========================================================================
# REGLAS_US: las del base + las de la marisquería
# ==========================================================================
REGLAS_US = OrderedDict(_base.REGLAS_US)
REGLAS_US.update([
    ('coccion_pescado', ('pescado entero y marisco 145 °F 15 s; pescado picado 155 °F 17 s; relleno 165 °F',
                         'FDA Food Code 2022 §3-401.11(A)(1), (A)(2) y (A)(3)')),
    ('parasitos_exentos', ('algunas especies quedan exentas de la congelación', 'FDA Food Code 2022 §3-402.11(B)')),
    ('recepcion', ('pescado fresco 41 °F o menos; congelado 0 °F y duro; shellstock según NSSP (en hielo o transporte a '
                   '45 °F de aire o 50 °F interna como máximo) y luego 41 °F', 'FDA Food Code 2022 §3-202.11 (B: la '
                   'temperatura de la ley del marisco); NSSP Guide (ISSC); S.C. Code Regs. 61-25 §3-202')),
    ('nssp', ('moluscos de proveedores de la Interstate Certified Shellfish Shippers List', 'FDA Food Code 2022 '
              '§3-201.15')),
    ('hielo', ('expositor sobre hielo escurrido; hielo de expositor no es ingrediente', 'FDA Food Code 2022 §3-303.12; '
               '§3-303.11')),
    ('descongelacion', ('walk-in a 41 °F o menos; agua fría corriente a 70 °F o menos; ROP fuera de la bolsa',
                        'FDA Food Code 2022 §3-501.13')),
    ('histamina', ('pescado formador de histamina siempre frío; rechazar lo que llegue caliente; la cocción no la '
                   'destruye', 'FDA Fish and Fishery Products Hazards and Controls Guidance, cap. 7')),
    ('vivero_moluscos', ('tanque de exposición de moluscos solo con variance y HACCP plan', '[local] variance del '
                         'departamento de salud (FDA Food Code 2022: molluscan shellfish life support system display '
                         'tank)')),
    ('aviso_alergenos', ('aviso escrito de los alérgenos principales en lo que se sirve sin envasar', 'FDA Food Code 2022 '
                         '§3-602.12(C)')),
    ('moluscos_alergeno', ('los moluscos no son alérgeno principal US; UK: sí (uno de los 14)', 'FALCPA + FASTER Act; '
                           'Food Information Regulations 2014')),
    ('nombres', ('nombre de mercado aceptado de la FDA Seafood List', 'FDA Guidance: The Seafood List')),
    ('propinas_pool', ('managers y supervisors no se quedan propinas del equipo', 'FLSA, 29 U.S.C. 203(m)(2)(B)')),
    ('edad_alcohol', ('21 años para comprar o consumir alcohol', 'National Minimum Drinking Age Act (23 U.S.C. 158)')),
    ('temporadas', ('temporadas US orientativas (crawfish, soft-shell, salmon, lobster, stone y king crab, scallops, '
                    'oysters): las fechas, del estado', '[criterio del kit]; [estatal] agencias de pesca; NOAA Fisheries')),
    ('dias_fuertes', ('Lent Fridays, Valentine\'s, Mother\'s Day, Jul 4, Thanksgiving, Christmas Eve (Seven Fishes), '
                      'NYE', '[criterio del kit] calendario comercial; 5 U.S.C. 6103 (base)')),
])
GRADOS_F_SPEC = {-31, -4, 0, 41, 45, 50, 70, 100, 135, 145, 155, 165}

# ==========================================================================
# Pistas y dependencias (el ES va SIN tildes: las regex las toleran)
# ==========================================================================
PISTAS_CAMBIO = {r'Kit de Tareas': 'D2: «Seafood Restaurant Checklists Kit Pro»'}
PISTAS_FUERA = (r'Restaurante Casual',)
PISTAS_EXTRA = [
    (r'[Mm]arisquer', 'D2: sin el sufijo «— Marisqueria»; marisquería → seafood restaurant'),
    (r'[Vv]ivero', 'vivero → live tank (lobster tank); oxígeno → dissolved oxygen'),
    (r'[Ll]onja|[Ss]ubasta', 'lonja → seafood distributor / dock-to-door supplier (NUNCA «auction»)'),
    (r'[Mm]ariscada', 'mariscada → seafood tower / seafood platter (NUNCA «mariscada»)'),
    (r'[Ee]xpositor|[Hh]ielo', 'expositor → seafood display (on drained ice); hielo picado → crushed ice'),
    (r'[Cc]amara', 'cámara → walk-in (cooler / freezer)'),
    (r'[Bb]ivalvos|[Oo]stras|[Aa]lmejas|[Nn]avajas|[Mm]ejillon|[Bb]erberech|[Zz]amburi|[Vv]ieira',
     'ostras → oysters; almejas → clams; navajas → razor clams; mejillones → mussels; berberechos → cockles; zamburiñas → '
     'queen scallops; vieiras → scallops'),
    (r'[Cc]rustaceos|[Bb]ogavante|[Ll]angost|[Cc]entoll|[Nn]ecora|[Cc]igala|[Gg]amba|[Pp]ercebe',
     'bogavante → lobster; langosta → spiny lobster; centollo / nécora → crab; cigala → langoustine; gamba / langostino → '
     'shrimp / prawns; percebes → gooseneck barnacles'),
    (r'[Cc]efalopodos|[Pp]ulpo|[Cc]alamar|[Ss]epia|[Cc]hipir', 'cefalópodos → cephalopods; pulpo → octopus; calamar → '
                                                               'squid; sepia → cuttlefish; chipirones → baby squid'),
    (r'[Ll]ubina|[Rr]odaballo|[Bb]esugo|[Mm]erluza|[Bb]acalao|[Rr]ape|[Bb]onito|[Aa]tun|[Ss]ardin|[Bb]oquer',
     'lubina → branzino; rodaballo → turbot; besugo → sea bream; merluza → hake; bacalao → cod; rape → monkfish; '
     'bonito → bonito; atún → tuna; sardinas → sardines; boquerones → anchovies'),
    (r'[Pp]lancha|[Pp]arrilla', 'plancha → flat-top griddle (NUNCA «plancha»); parrilla → grill'),
    (r'[Tt]enazas|[Pp]inchos|[Bb]aberos|finger', 'tenazas → crackers; pinchos → seafood picks; baberos → bibs; finger '
                                                  'bowls → finger bowls'),
    (r'[Ff]umet|[Cc]aldo', 'fumet → fish stock (fumet)'),
    (r'[Aa]l[eé]rgen', 'alérgenos US: pescado y crustáceos (de los 9); moluscos no (UK sí); sin números UE'),
    (r'APPCC|PCC|[Ss]anidad', 'APPCC → HACCP; PCC → CCP; Sanidad → health department / health inspection'),
    (r'[Aa]nisakis|[Cc]rudo|[Mm]arinad|[Cc]eviche|[Tt]artar', 'crudo / marinado → raw or undercooked: parásitos '
                                                              '3-402.11 + aviso 3-603.11'),
    (r'[Vv]edas?|[Tt]alla minima|[Cc]omunidad', 'veda → season closure; talla mínima → minimum legal size; comunidad '
                                               'autónoma → your state'),
    (r'FAO|[Aa]rte de pesca', 'zona FAO → harvest area / origin; arte de pesca → catch method'),
    (r'[Mm]ermas', 'mermas → waste (waste log)'),
    (r'[Cc]aja', 'caja → POS; cierre de caja → cash count, over/short'),
    (r'[Aa]lbari|[Gg]odello|[Tt]xakoli|[Vv]inos', 'vinos: Albariño (con eñe: FRASES_OK_EXTRA), '
                                                 'Sauvignon Blanc, Muscadet, Chablis; 21+ con ID'),
    (r'RRSS', 'RRSS → social media'),
    (r'[Mm]aitre|[Jj]efe (de )?cocina|[Cc]amarero|[Pp]artida', 'maître → FOH manager; jefe de cocina → head chef; '
                                                                'camarero → server; partida → station'),
    (r'[Nn]avidad|[Nn]ochevieja|Reyes|[Cc]omuniones|[Vv]igilia|Semana Santa|[Cc]hiringuito|[Tt]erraza',
     'calendario US: Christmas Eve (Seven Fishes), NYE, Lent Fridays; terraza → patio; sin chiringuitos'),
]
DEPENDENCIAS_EXTRA = OrderedDict([
    ('variante', ('Sufijo «— Marisqueria»', r'— Marisqueria', 'D2: la EN no lleva sufijo')),
    ('alergenos', ('Alérgenos UE (2 y 14), con o sin tilde', r'[Aa]l[eé]rgen', 'D-MAR: 9 US; moluscos no; UK 14')),
    ('lonja', ('Lonja y subasta', r'[Ll]onja|[Ss]ubasta', 'D-MAR: seafood distributor / dock-to-door')),
    ('vivero', ('Vivero de marisco vivo', r'[Vv]ivero', 'D-MAR: live tank; moluscos con variance')),
    ('trazabilidad', ('Trazabilidad UE (FAO, Reglamento, RD)', r'FAO|Reglamento|RD \d|[Aa]nisakis',
                      'D-MAR: shellstock tags 3-203.12, parásitos 3-402.11')),
    ('temporadas_es', ('Temporadas y vedas de España', r'[Gg]alleg|[Rr]ias|Huelva|[Cc]osta da|[Vv]eda|[Cc]omunidad',
                       'D14: temporadas US (POR_CELDA)')),
    ('caja', ('Caja española', r'[Cc]aja', 'D12: POS, over/short, tip pool')),
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
        err.append('la marisquería no tiene caja: HOJA_CAJA None y sin denominaciones ni fórmulas por celda')
    rx = re.compile(TERMINOS_PROHIBIDOS)
    if not rx.search(TERMINO_PROHIBIDO_EJEMPLO):
        err.append('TERMINO_PROHIBIDO_EJEMPLO no lo caza TERMINOS_PROHIBIDOS')
    for ok in ('raw bar', 'live tank', 'seafood distributor', 'flat-top griddle', 'seafood tower', 'head chef',
               'restaurant'):
        if rx.search(ok):
            err.append('TERMINOS_PROHIBIDOS caza lo permitido: %r' % ok)
    for k, v in list(GLOSARIO.items()) + list(POR_CELDA.items()) + list(CLAVES.items()) + list(HOJAS.items()):
        if (k not in _base.GLOSARIO or k in _GLOSARIO_MAR) and isinstance(v, str) and rx.search(v):
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
    if not MARCA_EN.endswith(PRODUCTO) or '—' in MARCA_EN:
        err.append('MARCA_EN debe acabar en el nombre del producto, sin «—»')
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
    esperado = [(_T3 + ('A12',), 'Alergeno 2'), (_T3 + ('A13',), 'Alergeno 14'), (_T3 + ('B22',), 'Anisakis'),
                (_T3 + ('B18',), 'Recepcion'), (_T3 + ('B20',), 'Coccion'), (_T3 + ('F6',), 'Reglamento UE'),
                (('02', 'Vivero y Lonjas', 'B15'), 'Etiquetado obligatorio'),
                (_T8 + ('A14',), 'Navidad'), (_T8 + ('A15',), 'Nochevieja'), (_T8 + ('A17',), 'Semana Santa'),
                (_T8 + ('B21',), 'Consultar calendario de vedas'), (_T8 + ('B24',), 'Licencia sanitaria')]
    # filas movidas del 01: el ES de la fila de origen es la tarea que se mueve
    for _d, _o, _a, _b, _c, _h in _MOVIDAS_01:
        if not tx.get(_AC + ('B%d' % _o,)) or not RX_HORA_CELDA.match(tx.get(_AC + ('D%d' % _o,), '')):
            err.append('01 fila de origen %d sin tarea u hora en el ES' % _o)
        if hora_us(tx.get(_AC + ('D%d' % _o,), '00:00')) != _h:
            err.append('01 fila %d: la hora %r no es la del ES de la fila %d' % (_d, _h, _o))
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
    print('mapas_seafood.py: {} ficheros · {} pestañas · {} glosario · {} por celda · {} adaptar · {} reglas · '
          '{} errores'.format(len(FICHEROS), len(HOJAS), len(GLOSARIO), len(POR_CELDA), len(ADAPTAR), len(REGLAS_US),
                              len(e)))
    raise SystemExit(1 if e else 0)
