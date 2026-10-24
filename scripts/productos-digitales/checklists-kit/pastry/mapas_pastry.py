#!/usr/bin/env python3
"""
mapas_pastry.py — Pastry Shop Checklists Kit Pro (EN) · DELTA del Kit de Tareas Pastelería (`kit-tareas-pasteleria`,
15 xlsx v2.0/2.1: los 01-09 del molde base, cuatro libros propios 10-13 y los 2 bonus) sobre `mapas.py`. SPEC:
`pastry/SPEC.md` (solo el delta). Noveno hermano vertical. Sesión Claude Code, 24-oct-2026.

Se usa con `--kit pastry` (kit.py). Importa `mapas.py` y SOLO añade o sobrescribe: producto, los 15 ficheros, títulos,
pestañas, glosario de pastelería (zonas, puestos, cuándo, categorías y referencias del 10 y el 12, alérgenos), CLAVES
(desplegables y literales de los libros 10-13), el 09 propio (otra maqueta: billetes en A21:C36, resumen en A39:B47,
CASOS_G5), CF_POR_CELDA (umbrales en °F del registro de temperaturas y de la recepción del 13), calendario B02 (otra
estructura: filas 4-20, B fecha · D evento · F antelación fijados; E y G = traductor con ADAPTAR), POR_CELDA, ADAPTAR y
REGLAS_US. Las funciones del base que leen constantes se re-enlazan a ESTE módulo. Los libros 10-13 no necesitan código
común: el circuito recorre `FICHEROS` / `LIBROS_ES`; el único «11» fijo del circuito es el de `mapas.autotest`, que este
delta sustituye por 15 (ver `autotest`). Ejecutado como script: autotest + cruce con pastry/censo_es.json.

    python3 pastry/mapas_pastry.py
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
AQUI = os.path.dirname(os.path.abspath(__file__))              # pastry/ (el import * trae el AQUI del base)

ORIGEN_ES = 'kit-tareas-pasteleria'
PRODUCTO = 'Pastry Shop Checklists Kit Pro'
# Title SEO = H1 (Forma B, 72 caracteres): «cake order form» 480/mes US, la intención propia más fuerte del kit (SPEC §R)
TITULO_SEO = 'Pastry Shop Checklists Kit Pro: Opening, Closing & Cake Order Templates'
SLUG = 'pastry-shop-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_PASTRY_SHOP_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
N_LIBROS = 15
MARCA_ES = '— Kit de Tareas Recurrentes · Pastelería / Obrador · AI Chef Pro · aichef.pro'
MARCA_EN = '— ' + PRODUCTO + ' · AI Chef Pro · aichef.pro'
VARIANTES_ES = ('Pastelería / Obrador', 'Pastelería con Tienda')
# heredar.py: memoria con VARIAS fuentes, en orden de preferencia (gana la primera que acierta). La cafetería primero
# (vitrina de bollería, mostrador, «shift lead», el 08 «Whole Shop»), después el base, la heladería (obrador + tienda,
# otro molde) y el resto. Medido el 24-oct (SPEC §4).
_SUF = lambda v: [(' — Pastelería / Obrador', ' — ' + v), (' · Pastelería / Obrador', ' · ' + v)]  # noqa: E731
MEMORIA = [('cafe', 'cafe', _SUF('Cafetería / Brunch')), ('base', '', _SUF('Restaurante Casual')),
           ('icecream', 'icecream', _SUF('Heladería Artesanal')), ('catering', 'catering', _SUF('Catering / Eventos')),
           ('pizza', 'pizza', _SUF('Pizzería')), ('burger', 'burger', _SUF('Hamburguesería')),
           ('ghost', 'ghost', _SUF('Dark Kitchen')), ('bar', 'bar', _SUF('Bar / Cocktails'))]
# heredar.py: EN heredado que en una pastelería con tienda no vale tal cual → pendientes (motivo «contexto»). Servicio de
# mostrador con obrador: sin sala ni camareros, host stand, barra de copas, cocina de línea, espresso como oficio,
# helado, catering de eventos ni delivery-only.
RX_CONTEXTO_PENDIENTE = (r'(?i)\b(?:dining rooms?|dine-in|FOH|host stands?|hostess|waitstaff|servers?|tables? service|'
                         r'reservations?|bartenders?|barbacks?|cocktails?|beer|liquor|wine|baristas?|espresso|'
                         r'coffee shops?|cafes?|bussers?|head chefs?|sous chefs?|line cooks?|prep cooks?|kitchen leads?|'
                         r'MOD|GM|shift managers?|banquets?|BEOs?|line-up|pizzas?|pizzerias?|burgers?|grill|'
                         r'ghost kitchens?|packers?|app managers?|commissar(?:y|ies)|ice cream|gelato|dipping cabinets?|'
                         r'batch freezers?|scoopers?|(?:your|the|a) bar|restaurants?(?! consultant| supply))\b')
NO_HEREDAR = {}
# gates_en.py G2: términos de otros kits que NINGUNA celda EN de la pastelería puede llevar. Permitidos: «venue» (el
# lugar de la celebración del 06), «cookie scoop», «coffee machine» (zona de degustación del 08), «restaurant
# consultant» (firma) y «restaurant supply».
TERMINOS_PROHIBIDOS = (r'(?i:\b(?:dining rooms?|host stands?|hostess|waitstaff|servers?|table service|bartenders?|'
                       r'barbacks?|cocktails?|beer|liquor|baristas?|coffee shops?|bussers?|head chefs?|sous chefs?|'
                       r'line cooks?|prep cooks?|banquets?|BEOs?|line-up|pizzas?|pizzerias?|burgers?|ghost kitchens?|'
                       r'packers?|app managers?|ice cream shops?|dipping cabinets?|batch freezers?|scoopers?|'
                       r'restaurants?(?! consultant| supply))\b)|\b(?:MOD|FOH|GM)\b')
TERMINO_PROHIBIDO_EJEMPLO = 'Ask the server to seat the party in the dining room.'
REFERENCIAS_TRADUCTOR = ['pastry/SPEC.md', 'SPEC.md §0-§3 y §7.2 (brief)', 'textos_en/glosario.json (glosario de la '
                         'prosa del kit base)', 'pastry/textos_en/heredado.json (cómo se dijo ya cada cosa: cafetería, '
                         'base, heladería y demás hermanos)', 'pastry/mapas_pastry.py: GLOSARIO, HOJAS, FICHEROS, '
                         'TITULOS, CITAS_LIBRO, POR_CELDA, REGLAS_US', '../GLOSARIO-JERGA-ES-EN.md (secciones Checklists '
                         'y Pastelería)', '../guia-pasteleria-en/F1-research-us.md §3, §7, §8 y §13']
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v2.0'),
    ('keywords', 'pastry shop checklist, bakery opening checklist, bakery cleaning schedule, cake order form, bakery '
                 'production schedule, bakery allergen chart, food temperature log, receiving log, AI Chef Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

# ==========================================================================
# Ficheros (D5, DataForSEO US 24-oct: pastry shop 40.500 · bakery case 590 · cake order form 480 · allergen chart 320 ·
# food temperature log 320 · bakery order form 260 · temperature log sheet 210 · receiving log 140 · pastry chef duties
# 110; las variantes con «checklist» de 0 a 30, como en los hermanos)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-apertura-cierre.xlsx', '01-pastry-kitchen-bakery-case-opening-closing-checklists.xlsx'),
    ('02-partidas-cocina.xlsx', '02-pastry-kitchen-production-checklists.xlsx'),
    ('03-tareas-manager.xlsx', '03-pastry-shop-manager-checklist.xlsx'),
    ('04-tareas-perfiles.xlsx', '04-pastry-chef-duties-by-role.xlsx'),
    ('05-tareas-semanales-mensuales.xlsx', '05-bakery-cleaning-schedule-maintenance-inventory.xlsx'),
    ('06-eventos-festivos.xlsx', '06-pastry-shop-holiday-event-checklists.xlsx'),
    ('07-plantilla-personalizable.xlsx', '07-blank-pastry-shop-checklist-template.xlsx'),
    ('08-apertura-cierre-negocio.xlsx', '08-pastry-shop-opening-closing-checklist.xlsx'),
    ('09-apertura-cierre-caja.xlsx', '09-cash-drawer-opening-closing.xlsx'),
    ('10-plan-produccion-semanal.xlsx', '10-bakery-production-schedule-waste-log.xlsx'),
    ('11-control-encargos.xlsx', '11-cake-order-form-order-log.xlsx'),
    ('12-control-alergenos-vitrina.xlsx', '12-bakery-allergen-chart.xlsx'),
    ('13-registro-temperaturas-recepcion.xlsx', '13-food-temperature-log-receiving-log.xlsx'),
    ('BONUS-01-briefing-servicio.xlsx', 'BONUS-01-pastry-shop-pre-shift-meeting-template.xlsx'),
    ('BONUS-02-calendario-anual-tareas.xlsx', 'BONUS-02-pastry-shop-holiday-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)
TITULOS = OrderedDict([
    ('01-pastry-kitchen-bakery-case-opening-closing-checklists.xlsx',
     'Pastry Kitchen & Bakery Case Opening and Closing Checklists'),
    ('02-pastry-kitchen-production-checklists.xlsx',
     'Pastry Kitchen Production Checklists: Doughs, Creams & Fillings, Decorating'),
    ('03-pastry-shop-manager-checklist.xlsx', 'Pastry Shop Manager Checklist: Daily, Weekly, Monthly & Shift Handover'),
    ('04-pastry-chef-duties-by-role.xlsx',
     'Pastry Chef Duties by Role: Head Pastry Chef, Pastry Cook, Assistant & Counter'),
    ('05-bakery-cleaning-schedule-maintenance-inventory.xlsx',
     'Bakery Cleaning Schedule, Equipment Maintenance & Weekly Inventory'),
    ('06-pastry-shop-holiday-event-checklists.xlsx',
     'Pastry Shop Holiday & Event Checklists: Holidays, Valentine\'s, Easter, Mother\'s Day, Celebration Cakes & '
     'Thanksgiving'),
    ('07-blank-pastry-shop-checklist-template.xlsx', 'Blank Pastry Shop Checklist Template (Editable)'),
    ('08-pastry-shop-opening-closing-checklist.xlsx', 'Pastry Shop Opening & Closing Checklist (Whole Shop)'),
    ('09-cash-drawer-opening-closing.xlsx', 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log'),
    ('10-bakery-production-schedule-waste-log.xlsx',
     'Bakery Production Schedule & Waste Log: Weekly Plan, Made vs. Sold & Summary'),
    ('11-cake-order-form-order-log.xlsx', 'Cake Order Form & Custom Order Log: Order Form, Log, Pickups & Today\'s Orders'),
    ('12-bakery-allergen-chart.xlsx', 'Bakery Allergen Chart (9 Major Allergens, UK 14): Matrix, Chart, Case Sign & Labels'),
    ('13-food-temperature-log-receiving-log.xlsx',
     'Food Temperature Log, Receiving Log, Prep Labels & Shelf Life Chart'),
    ('BONUS-01-pastry-shop-pre-shift-meeting-template.xlsx',
     'BONUS: Pastry Shop Pre-Shift Meeting Template (Huddle Notes)'),
    ('BONUS-02-pastry-shop-holiday-calendar.xlsx', 'BONUS: Pastry Shop Holiday & Events Calendar (US)'),
])
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

HOJAS = OrderedDict(_base.HOJAS)
HOJAS.update([
    ('Apertura Obrador', 'Kitchen Opening'), ('Cierre Obrador', 'Kitchen Closing'),
    ('Masas y Fermentación', 'Doughs & Fermentation'), ('Cremas y Rellenos', 'Creams & Fillings'),
    ('Decoración y Acabado', 'Decorating & Finishing'),
    ('Jefe Pastelero', 'Head Pastry Chef'), ('Pastelero', 'Pastry Cook'), ('Ayudante', 'Pastry Assistant'),
    ('Dependiente Vitrina', 'Counter Associate'),
    ('Inventario', 'Weekly Inventory'),
    ('Navidad', 'Holiday Season'), ('Semana Santa', 'Easter'), ('Día Madre-Padre', "Mother's & Father's Day"),
    ('Comuniones (Abr-Jun)', 'Celebration Cakes (Apr-Jun)'), ('Todos los Santos (Oct-Nov)', 'Thanksgiving (Nov)'),
    ('Por Zona', 'By Area'),
    ('Apertura del Negocio', 'Shop Opening'), ('Cierre del Negocio', 'Shop Closing'),
    ('Plan Semanal', 'Weekly Plan'), ('Producido vs Vendido', 'Made vs Sold'),
    ('Resumen por Partida', 'Summary by Category'),
    ('Ficha de Encargo', 'Order Form'), ('Registro de Encargos', 'Order Log'), ('Agenda de Entregas', 'Pickup Schedule'),
    ('Encargos de Hoy', "Today's Orders"),
    ('Matriz Alérgenos', 'Allergen Matrix'), ('Carta de Alérgenos', 'Allergen Chart'), ('Cartel Vitrina', 'Case Sign'),
    ('Etiquetas Vitrina', 'Case Labels'),
    ('Registro de Temperaturas', 'Temperature Log'), ('Recepción de Mercancía', 'Receiving Log'),
    ('Etiquetas de Elaborado', 'Prep Labels'), ('Vidas Útiles', 'Shelf Life'),
    ('Briefing Diario', 'Pre-Shift Huddle'),
])
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Apertura Obrador', 'Cierre Obrador']),
    ('02', ['Instrucciones', 'Masas y Fermentación', 'Cremas y Rellenos', 'Decoración y Acabado']),
    ('03', ['Instrucciones', 'Diario Manager', 'Semanal Manager', 'Mensual Manager', 'Handover Turno']),
    ('04', ['Instrucciones', 'Jefe Pastelero', 'Pastelero', 'Ayudante', 'Dependiente Vitrina']),
    ('05', ['Instrucciones', 'Limpieza Semanal', 'Mantenimiento Mensual', 'Inventario']),
    ('06', ['Instrucciones', 'Navidad', 'San Valentín', 'Semana Santa', 'Día Madre-Padre', 'Comuniones (Abr-Jun)',
            'Todos los Santos (Oct-Nov)']),
    ('07', ['Instrucciones', 'Por Franja Horaria', 'Por Zona', 'Por Perfil']),
    ('08', ['Instrucciones', 'Apertura del Negocio', 'Cierre del Negocio']),
    ('09', ['Instrucciones', 'Apertura de Caja', 'Cierre de Caja', 'Registro Mensual']),
    ('10', ['Instrucciones', 'Plan Semanal', 'Producido vs Vendido', 'Resumen por Partida']),
    ('11', ['Instrucciones', 'Ficha de Encargo', 'Registro de Encargos', 'Agenda de Entregas', 'Encargos de Hoy']),
    ('12', ['Instrucciones', 'Matriz Alérgenos', 'Carta de Alérgenos', 'Cartel Vitrina', 'Etiquetas Vitrina']),
    ('13', ['Instrucciones', 'Registro de Temperaturas', 'Recepción de Mercancía', 'Etiquetas de Elaborado',
            'Vidas Útiles']),
    ('B01', ['Instrucciones', 'Briefing Diario']),
    ('B02', ['Instrucciones', 'Calendario Anual']),
])
# Citas a otro libro dentro de un texto («→ 13 Registro de Temperaturas · hoja Etiquetas de Elaborado»): el EN fijo de
# cada libro (y la hoja, con el EN de HOJAS entre comillas dobles rectas: ‹· sheet "Prep Labels"›). Va al traductor
# como pista (PISTAS_EXTRA) y la comprueba la revisión de la F2.
CITAS_LIBRO = OrderedDict([
    ('01 Apertura y Cierre', '01 Opening & Closing'),
    ('06 Eventos y Festivos', '06 Holiday & Event Checklists'),
    ('08 Apertura y Cierre del Negocio', '08 Shop Opening & Closing'),
    ('09 Apertura y Cierre de Caja', '09 Cash Drawer Opening & Closing'),
    ('10 Plan de Producción Semanal', '10 Production Schedule & Waste Log'),
    ('11 Control de Encargos', '11 Cake Orders'),
    ('12 Control de Alérgenos de Vitrina', '12 Bakery Allergen Chart'),
    ('13 Registro de Temperaturas', '13 Temperature & Receiving Logs'),
    ('BONUS-01 Briefing de Servicio', 'BONUS-01 Pre-Shift Meeting'),
])

# ==========================================================================
# GLOSARIO: el base entero (opcional) + celdas cortas de la pastelería. Jerga US (guía EN §13.1 y D9): obrador →
# kitchen (pastry kitchen), vitrina → bakery case, despacho → counter, dependiente → counter associate, encargado →
# shift lead, bollería → viennoiserie. Las referencias del 10 y el 12 (mismo texto en las dos hojas) van aquí para
# que digan lo mismo en los dos libros; las categorías, además, en CLAVES (desplegable del 10 + SUMIF del resumen).
# ==========================================================================
GLOSARIO = OrderedDict(_base.GLOSARIO)
_GLOSARIO_PAS = OrderedDict([
    # cabeceras y formularios
    ('Parámetro / Objetivo', 'Target / Spec'), ('Hora', 'Time'), ('Fecha', 'Date'), ('Producto', 'Product'),
    ('Partida', 'Category'), ('Estado', 'Status'), ('Cliente', 'Customer'), ('Teléfono', 'Phone'),
    ('Raciones', 'Servings'), ('Observaciones', 'Notes'), ('TOTALES', 'TOTALS'), ('☐ Sí   ☐ No', '☐ Yes   ☐ No'),
    ('Producido', 'Made'), ('Vendido', 'Sold'), ('Sobrante', 'Leftover'), ('Merma %', 'Waste %'),
    ('Coste merma (€)', 'Waste cost'), ('Tarde', 'Afternoon'),
    ('Lun', 'Mon'), ('Mar', 'Tue'), ('Mié', 'Wed'), ('Jue', 'Thu'), ('Vie', 'Fri'), ('Sáb', 'Sat'), ('Dom', 'Sun'),
    # zonas (columna C)
    ('Obrador', 'Kitchen'), ('Vitrina', 'Bakery case'), ('Despacho', 'Counter'), ('Tienda', 'Shop'),
    ('Horno', 'Ovens'), ('Almacén', 'Storage'), ('Equipo', 'Team'),
    # puestos (columna D)
    ('Jefe Pastelero', 'Head pastry chef'), ('Ayudante', 'Pastry assistant'), ('Dependiente', 'Counter associate'),
    ('Encargado', 'Shift lead'), ('Mantenimiento', 'Maintenance'), ('Saliente', 'Outgoing shift'),
    # cuándo (columna E)
    ('Continuo', 'Ongoing'), ('Recepción', 'On delivery'), ('Inicio de turno', 'Start of shift'),
    ('1ª semana', 'Week 1'), ('2ª semana', 'Week 2'), ('3ª semana', 'Week 3'), ('4ª semana', 'Week 4'),
    ('Día antes', 'Day before'), ('Día de la entrega', 'Delivery day'), ('1 sem antes', '1 week out'),
    ('2 sem antes', '2 weeks out'), ('3 sem antes', '3 weeks out'), ('4 sem antes', '4 weeks out'),
    ('4-6 sem antes', '4–6 weeks out'), ('2 días antes', '2 days out'), ('48 h tras la visita', '48 h after meeting'),
    ('Enero', 'January'), ('Febrero', 'February'), ('Feb-Mar', 'Feb–Mar'), ('Julio', 'July'),
    # 06 «Holiday Season» y «Valentine's Day»: fechas (D14: formato US, mismas fechas)
    ('1 Nov', 'Nov 1'), ('5 Nov', 'Nov 5'), ('10 Nov', 'Nov 10'), ('15 Nov', 'Nov 15'), ('20 Nov', 'Nov 20'),
    ('1-15 Dic', 'Dec 1–15'), ('20-24 Dic', 'Dec 20–24'), ('15-24 Dic', 'Dec 15–24'), ('20 Dic', 'Dec 20'),
    ('22-24 Dic', 'Dec 22–24'), ('23-24 Dic', 'Dec 23–24'), ('29 Dic', 'Dec 29'), ('31 Dic', 'Dec 31'),
    ('2 Ene', 'Jan 2'), ('3 Ene', 'Jan 3'), ('04-05 Ene', 'Jan 4–5'), ('05-06 Ene', 'Jan 5–6'), ('7 Ene', 'Jan 7'),
    ('1 Feb', 'Feb 1'), ('5 Feb', 'Feb 5'), ('10 Feb', 'Feb 10'), ('12 Feb', 'Feb 12'), ('13 Feb', 'Feb 13'),
    ('14 Feb', 'Feb 14'), ('15 Feb', 'Feb 15'),
    # 06 «Easter»: Semana Santa → Easter (Holy Week)
    ('Dom Ramos', 'Palm Sunday'), ('V. Dolores → D. Resurrección', 'Holy Week'), ('Mié-Vie Santo', 'Wed–Good Friday'),
    ('Vie Santo', 'Good Friday'), ('Jue-Sáb Santo', 'Thu–Sat before Easter'), ('Sáb Santo', 'Holy Saturday'),
    ('Mar tras Pascua', 'Tue after Easter'),
    # 10 y 12: categorías (= CLAVES) y referencias de ejemplo, adaptadas a una pastry shop US con su perfil de
    # alérgenos (la matriz del 12 viene premarcada: cada referencia EN tiene el mismo perfil que la ES; SPEC D-PAS)
    ('Bollería', 'Viennoiserie'), ('Pastelería', 'Cakes & pastries'), ('Pan', 'Bread'), ('Salado', 'Savory'),
    ('Bizcochería', 'Cookies & small cakes'), ('Temporada', 'Seasonal'), ('Elaboración base', 'Base recipes'),
    ('Croissant de mantequilla', 'Butter croissant'), ('Pain au chocolat', 'Pain au chocolat'),
    ('Napolitana de crema', 'Custard danish'), ('Ensaimada', 'Concha (pan dulce)'), ('Brioche', 'Brioche'),
    ('Caracola de pasas', 'Pain aux raisins'), ('Palmera de hojaldre', 'Palmier'),
    ('Croissant relleno de crema', 'Cream-filled croissant'), ('Tarta de queso', 'Cheesecake'),
    ('Tarta de manzana', 'Apple pie'), ('Milhojas', 'Napoleon'), ('Éclair', 'Eclair'),
    ('Tarta de zanahoria', 'Carrot cake'), ('Tarta Sacher', 'Chocolate layer cake'),
    ('Entremet individual', 'Individual mousse cake'), ('Macarons (caja de 6)', 'French macarons (box of 6)'),
    ('Tartaleta de frutas', 'Fresh fruit tart'), ('Lionesa o profiterol', 'Cream puff'), ('Barra', 'Baguette'),
    ('Hogaza de masa madre', 'Sourdough boule'), ('Chapata', 'Ciabatta'), ('Pan de molde', 'Sandwich loaf'),
    ('Focaccia', 'Focaccia'), ('Quiche', 'Quiche'), ('Empanada', 'Empanada'),
    ('Croissant de jamón y queso', 'Ham & cheese croissant'), ('Magdalena', 'Muffin'),
    ('Cookie de chocolate', 'Chocolate chip cookie'), ('Brownie', 'Brownie'), ('Galleta de mantequilla', 'Butter cookie'),
    ('Bizcocho de yogur', 'Pound cake'), ('Financier de almendra', 'Almond financier'),
    ('Roscón de Reyes', 'Three Kings bread (rosca)'), ('Torrijas', 'Hot cross buns'),
    ('Buñuelos de viento', 'Paczki (filled doughnuts)'), ('Huesos de santo', 'Amaretti cookies'),
    ('Panellets', 'Pignoli cookies'), ('Polvorón o mantecado', 'Polvorones (Mexican wedding cookies)'),
    ('Turrón de almendra', 'Almond nougat (torrone)'), ('Mona de Pascua', 'Chocolate Easter cake'),
    ('Empanada de atún', 'Tuna empanada'), ('Crema pastelera', 'Pastry cream'), ('Ganache de chocolate', 'Chocolate ganache'),
    ('Nata montada', 'Whipped cream'),
    # 12: los 14 alérgenos UE → los 9 de EE. UU. en sus mismas columnas + 5 marcados para UK/UE (D-PAS; mismas columnas,
    # mismos símbolos: el trigo es el alérgeno US de la columna «Gluten»; los sulfitos se declaran en EE. UU. desde
    # 10 ppm sin ser «major allergen»)
    ('Gluten', 'Wheat (gluten)'), ('Crustáceos', 'Shellfish'), ('Huevos', 'Eggs'), ('Pescado', 'Fish'),
    ('Cacahuetes', 'Peanuts'), ('Soja', 'Soy'), ('Lácteos', 'Milk'), ('Frutos de cáscara', 'Tree nuts'),
    ('Apio', 'Celery (UK)'), ('Mostaza', 'Mustard (UK)'), ('Sésamo', 'Sesame'), ('Sulfitos', 'Sulfites'),
    ('Altramuces', 'Lupin (UK)'), ('Moluscos', 'Mollusks (UK)'),
    # (cabeceras giradas 90° en una fila de 95 pt: ≤ 15 caracteres, como el ES más largo que cabe)
    # 13: etiquetas de elaborado (date marking 3-501.17) y conservación de la tabla de vidas útiles
    ('Producto:', 'Item:'), ('Fecha y hora de elaboración:', 'Made (date & time):'),
    ('Fecha y hora límite de consumo:', 'Use by (date & time):'), ('Lote:', 'Batch #:'), ('Responsable:', 'Made by:'),
    ('0 a 4 °C', '32 to 41 °F'), ('≤ −18 °C', '0 °F or below'), ('24 h', '24 h'),
])
GLOSARIO.update(_GLOSARIO_PAS)
GLOSARIO_OPCIONAL = frozenset(_base.GLOSARIO)
_ZONAS_PUESTOS = {'Obrador', 'Vitrina', 'Despacho', 'Tienda', 'Horno', 'Almacén', 'Equipo', 'Jefe Pastelero', 'Ayudante',
                  'Dependiente', 'Encargado', 'Mantenimiento', 'Saliente'}
PUESTOS_ES = frozenset(_base.PUESTOS_ES | _ZONAS_PUESTOS)
CATEGORIAS = ('Bollería', 'Pastelería', 'Pan', 'Salado', 'Bizcochería')

# ==========================================================================
# CLAVES: desplegables y literales de fórmula de los libros 10-13 (los del 01-09 son los del base: ✓ — N/A)
# ==========================================================================
CLAVES = OrderedDict(_base.CLAVES)
CLAVES.update([(k, GLOSARIO[k]) for k in CATEGORIAS])
# G6: la «Carta de Alérgenos» del 12 copia por fórmula las referencias de la matriz; su texto calculado EN es el del
# GLOSARIO (gates_en compara con CLAVES.get(es))
_REFERENCIAS = [k for k in _GLOSARIO_PAS if list(_GLOSARIO_PAS).index('Croissant de mantequilla') <= list(
    _GLOSARIO_PAS).index(k) <= list(_GLOSARIO_PAS).index('Nata montada')]
CLAVES.update([(k, GLOSARIO[k]) for k in _REFERENCIAS])
CLAVES.update([
    # 10 «Made vs Sold» K: qué hacer con el sobrante (cada opción lleva su condición; SPEC D-PAS)
    ('Vender −30 % última hora', 'Last-hour sale (30% off)'),
    ('Congelar (SOLO producto no expuesto del día y abatido antes de −18 °C)',
     'Freeze (ONLY same-day product never displayed; blast-freeze to 0 °F)'),
    ('Reprocesar (SOLO producto seco de menos de 24 h; registrar lote destino)',
     'Rework (ONLY dry product under 24 h old; log the batch it goes into)'),
    ('Donar', 'Donate'), ('Desechar', 'Discard'),
    # 10 «Summary by Category»: lectura del objetivo de merma
    ('OK', 'OK'), ('Revisar', 'Review'), ('Dentro del objetivo', 'On target'),
    ('Por encima del objetivo: revisa el plan', 'Above target: review the plan'),
    # 11: estado, forma de pago y canal del encargo
    ('Pendiente', 'Pending'), ('En producción', 'In production'), ('Listo', 'Ready'), ('Entregado', 'Delivered'),
    ('Cancelado', 'Canceled'),
    ('Efectivo', 'Cash'), ('Tarjeta', 'Card'), ('Bizum', 'Zelle / Venmo'), ('Transferencia', 'Bank transfer'),
    ('Pendiente de pago', 'Not paid yet'),
    ('Tienda', 'In store'), ('Teléfono', 'Phone'), ('WhatsApp', 'Text / WhatsApp'), ('Web', 'Website'),
    ('Otro', 'Other'),
    # 12: estado de cada referencia de la matriz
    ('NO PUBLICAR', 'DO NOT PUBLISH'), ('Verificado', 'Verified'),
    # 13 «Receiving Log»: vehículo y embalaje, y decisión
    ('Correcto', 'Good'), ('Deficiente', 'Poor'), ('Aceptado', 'Accepted'), ('Rechazado', 'Rejected'),
    ('Aceptado con reserva', 'Accepted with note'),
])

# ==========================================================================
# 09 PROPIO (otra maqueta que el base): «Apertura de Caja» con el fondo en C17; «Cierre de Caja» con 12 tareas, billetes
# en A21:C27, monedas en A29:C36, total en C37 y resumen en A39:B47; «Registro Mensual» con «Ventas Efectivo» (ya sin
# el fondo). Mismas 15 denominaciones y valores que el base (D12), en sus filas.
# ==========================================================================
HOJA_CAJA = ('09', 'Cierre de Caja')
_FILAS_CAJA = list(range(21, 28)) + list(range(29, 37))
DENOMINACIONES = [(f, es, xes, en, xen) for f, (_f0, es, xes, en, xen) in zip(_FILAS_CAJA, _base.DENOMINACIONES)]
VALORES_DENOMINACION_EN = sorted({d[4] for d in DENOMINACIONES})
FORMULAS_POR_CELDA = OrderedDict(
    ((HOJA_CAJA[0], HOJA_CAJA[1], 'C%d' % f), ('=B%d*%s' % (f, _num(xes)), '=B%d*%s' % (f, _num(xen))))
    for f, _es, xes, _en, xen in DENOMINACIONES)
_HA, _HC, _HR = 'Apertura de Caja', 'Cierre de Caja', 'Registro Mensual'
CASOS_G5 = [
    {'nombre': 'efectivo 1 de cada', 'entradas': {(_HC, 'B%d' % d[0]): 1 for d in DENOMINACIONES},
     'esperado': {(_HC, 'C37'): 204.91, (_HC, 'B41'): 204.91}},
    {'nombre': 'cierre 200 / 1,250 / 3,000 / 150 / Z 4,200', 'entradas': {
        (_HA, 'C17'): 200, (_HC, 'B21'): 12, (_HC, 'B22'): 1, (_HC, 'B43'): 3000, (_HC, 'B44'): 150,
        (_HC, 'B46'): 4200, (_HR, 'B5'): 200, (_HR, 'C5'): 1050, (_HR, 'D5'): 3000, (_HR, 'E5'): 150,
        (_HR, 'G5'): 4200},
     'esperado': {(_HC, 'C37'): 1250, (_HC, 'B41'): 1250, (_HC, 'B42'): 200, (_HC, 'B45'): 4200, (_HC, 'B47'): 0,
                  (_HR, 'F5'): 4200, (_HR, 'H5'): 0}},
]
CELDA_CACHE_MAL = 'B43'                # autotest G6: «Card sales, excl. tips» (C50 en el base)

# ==========================================================================
# BONUS-02 «Holiday Calendar»: otra estructura (filas 4-20: A nº · B fecha · C fecha de este año · D evento ·
# E producción · F antelación · G notas). B, D y F fijados; E y G = traductor con ADAPTAR (fila → (fecha, evento,
# antelación, ADAPTAR de E, ADAPTAR de G)). Cronológico (las fechas variables al final, como el ES). Fuentes: guía EN
# §7 (Rosca de Reyes + King cake, Pi Day / St. Patrick's, Mother's Day 2.º domingo de mayo, First Communion y
# graduaciones, Day of the Dead + Thanksgiving) y 36 U.S.C. / 5 U.S.C. 6103.
# ==========================================================================
HOJA_CAL = ('B02', 'Calendario Anual')
FILAS_CALENDARIO = range(4, 21)
CALENDARIO = OrderedDict([
    (4, ('Jan 6 → Mardi Gras', "Three Kings Day & King cake season", '2 weeks',
         'Rosca de Reyes (Three Kings bread) para el 6 de enero y King cake hasta el Mardi Gras (relleno de crema, '
         'cream cheese o praliné); sin «nata, trufa» españolas',
         'Fuerte en las comunidades hispanas y en la costa del Golfo (Luisiana); el muñequito, aparte para que lo meta '
         'el cliente')),
    (5, ('Feb 14', "Valentine's Day", '2 weeks', None, None)),
    (6, ('Mar 14 · Mar 17', "Pi Day & St. Patrick's Day", '1 week',
         'Sustituye al Día del Padre (en EE. UU. va en junio: nota de la fila 8). Tartas (pies) el 14 de marzo; Irish '
         'soda bread, galletas de trébol y cupcakes verdes para el 17',
         'Primer pico de la primavera')),
    (7, ('Mar–Apr (varies)', 'Easter', '3 weeks',
         'Sustituye a torrijas y monas: hot cross buns (Viernes Santo), carrot cake, huevos y conejos de chocolate, '
         'galletas decoradas',
         None)),
    (8, ('2nd Sunday in May', "Mother's Day", '2 weeks',
         'Tartas con dedicatoria, cupcakes, cajas de macarons y bollería para el brunch',
         'Pico muy fuerte: refuerza el mostrador. Father\'s Day es el 3.er domingo de junio (más flojo)')),
    (9, ('May–Jun (varies)', 'First Communions & graduations', '2–3 months (catalog by February)',
         'Tartas personalizadas, mesas dulces (dessert tables) y galletas decoradas (en graduaciones, con los colores '
         'del colegio)',
         'Cita la hoja «Celebration Cakes (Apr-Jun)» del 06 con su EN exacto: «→ 06 Holiday & Event Checklists · '
         'sheet "Celebration Cakes (Apr-Jun)"»')),
    (10, ('Jun–Aug', 'Summer (Memorial Day → Labor Day) & July 4', '4 weeks',
          'Sustituye a «helados, tartas frías, granizados»: tartas de fruta (fruit pies y tarts), icebox cakes y, para '
          'el 4 de julio, tarta bandera y cupcakes rojo, blanco y azul',
          'Con calor, todo lo relleno de crema en la vitrina refrigerada a 41 °F o menos')),
    (11, ('Oct 31', 'Halloween', '2 weeks', None, None)),
    (12, ('Nov 1–2 · 4th Thursday of Nov', 'Day of the Dead & Thanksgiving', '3 weeks',
          'Sustituye a Todos los Santos: pan de muerto (1-2 de noviembre) y, para Thanksgiving, pies (pumpkin, pecan, '
          'apple, sweet potato) y dinner rolls',
          'El miércoles antes de Thanksgiving es el día de más recogidas de pies del año: pedidos anticipados y franjas '
          'de recogida; cita «→ 06 Holiday & Event Checklists · sheet "Thanksgiving (Nov)"»')),
    (13, ('Day after Thanksgiving', 'Black Friday & Small Business Saturday', '1 week',
          'Promociones en lotes y cajas regalo, latas de galletas de Navidad (cookie tins), tarjetas regalo',
          'Oportunidad de venta online; el sábado es el Small Business Saturday')),
    (14, ('December', 'Christmas & holiday season', '6 weeks',
          'Sustituye a turrones, polvorones y mazapanes: bandejas de galletas de Navidad, Yule logs (troncos), stollen y '
          'panettone, pies y galletas de jengibre (gingerbread)',
          None)),
    (15, ('Dec 31', "New Year's Eve", '1 week',
          'Tartas para la cena, petit fours y macarons',
          'Pedidos mayoristas (wholesale) de otros negocios de comida; sin la palabra «restaurant»')),
    (16, ('Varies', 'Local festivals & fairs', '3 weeks',
          'Los dulces tradicionales de tu zona', None)),
    (17, ('Varies (peak May–Oct)', 'Wedding season', '2–3 months',
          'Tartas de boda, mesas dulces (dessert tables) y detalles para los invitados (favors)',
          'De mayo a octubre, pico de bodas')),
    (18, ('Varies', 'Corporate orders', '2 weeks',
          'Cajas de bollería para desayunos de empresa, bandejas para el coffee break y cajas regalo', None)),
    (19, ('Varies', 'Birthdays', '3–7 days', None, None)),
    (20, ('Varies', 'Baptisms, showers & anniversaries', '3–4 weeks',
          'Sustituye a «bautizos/comuniones» (las comuniones van en la fila 9): bautizos, baby y bridal showers y '
          'aniversarios; tartas temáticas y galletas personalizadas',
          None)),
])

# ==========================================================================
# POR_CELDA: textos EN fijados (caja, cifras de proceso en °F, alérgenos, registros, calendario). (libro, hoja ES, celda)
# ==========================================================================
_MD, _CR, _DA = ('02', 'Masas y Fermentación'), ('02', 'Cremas y Rellenos'), ('02', 'Decoración y Acabado')
_RT, _RM, _VU = ('13', 'Registro de Temperaturas'), ('13', 'Recepción de Mercancía'), ('13', 'Vidas Útiles')
_FE, _CV = ('11', 'Ficha de Encargo'), ('12', 'Cartel Vitrina')
_TS = ('06', 'Todos los Santos (Oct-Nov)')
POR_CELDA = OrderedDict([
    # 09 · Apertura de Caja (D12)
    (('09', _HA, 'B17'), 'Starting bank (opening float)'),
    # 09 · Cierre de Caja: tareas de tarjetas y otros medios (D12: propinas fuera de ventas; mismo EN que el base)
    (('09', _HC, 'B8'), _base.POR_CELDA[('09', 'Cierre de Caja', 'B8')]),
    (('09', _HC, 'B9'), _base.POR_CELDA[('09', 'Cierre de Caja', 'B9')]),
    (('09', _HC, 'A18'), 'Cash Count by Denomination'), (('09', _HC, 'A19'), 'Denomination'),
    (('09', _HC, 'B19'), 'Quantity'), (('09', _HC, 'C19'), 'Subtotal'),
    (('09', _HC, 'A20'), 'BILLS'), (('09', _HC, 'A28'), 'COINS'), (('09', _HC, 'A37'), 'TOTAL CASH'),
    (('09', _HC, 'A39'), 'Closing Summary'), (('09', _HC, 'A40'), 'Item'), (('09', _HC, 'B40'), 'Amount'),
    (('09', _HC, 'A41'), 'Total cash (count)'), (('09', _HC, 'A42'), 'Starting bank (−)'),
    (('09', _HC, 'A43'), 'Card sales, excl. tips'), (('09', _HC, 'A44'), 'Other tenders + card tips paid in cash'),
    (('09', _HC, 'A45'), 'TOTAL COLLECTED'), (('09', _HC, 'A46'), 'POS Z report: sales + tax, excl. tips'),
    (('09', _HC, 'A47'), 'OVER / SHORT'),
    # 09 · Registro Mensual: cabecera (la C ya es efectivo neto: el ES la llama «Ventas Efectivo») y totales
    (('09', _HR, 'A4'), 'Day'), (('09', _HR, 'B4'), 'Starting Bank'), (('09', _HR, 'C4'), 'Cash Sales (net)'),
    (('09', _HR, 'D4'), 'Card Sales (no tips)'), (('09', _HR, 'E4'), 'Other + Tips Paid'),
    (('09', _HR, 'F4'), 'Total Collected'), (('09', _HR, 'G4'), 'POS Z (+ tax, no tips)'),
    (('09', _HR, 'H4'), 'Over/Short'), (('09', _HR, 'I4'), 'Bank Deposit'), (('09', _HR, 'J4'), 'Closed by'),
    (('09', _HR, 'A36'), 'TOTALS'),
    # 02 · «Target / Spec»: cifras de proceso en °F [criterio del kit: conversión exacta redondeada al °F; los hornos, a
    # los escalones US de 25 °F] y las de seguridad, las de la FDA (REGLAS_US)
    (_MD + ('C7',), 'Feed 1:1:1 · rest at 75–79 °F'),
    (_MD + ('C10',), '72–75 °F · 68–72 °F if it goes straight to chilling'),
    (_MD + ('C11',), '1 h in the blast chiller or 12 h in the walk-in at 37–39 °F'),
    (_MD + ('C12',), 'Overnight retard · ramps up to 75–79 °F · doubles in size'),
    (_MD + ('C13',), '375–400 °F · 14–18 min · in the case before 8:00 AM'),
    (_MD + ('C14',), 'Dough and butter at 54–57 °F · final thickness 1/8 in (3–3.5 mm)'),
    (_MD + ('C16',), '75–79 °F (82 °F max) · 75–80% RH · 2.5–3 h · doubles in size'),
    (_MD + ('C18',), '375–400 °F · 14–18 min'),
    (_MD + ('C21',), '12–16 h at 39–43 °F'),
    (_MD + ('C24',), '45–60 min at 75–79 °F'),
    (_MD + ('C26',), '450–480 °F · steam 3–5 min · vent open the last 5–8 min'),
    (_MD + ('C30',), 'Softened butter at 64–68 °F'),
    (_MD + ('C31',), 'Rest at least 1 h at 39 °F'),
    (_MD + ('C33',), '350 °F · 15 min'),
    (_MD + ('C34',), '350 °F · 5 more min'),
    (_MD + ('C35',), 'Down to 68–72 °F'),
    (_CR + ('C7',), '135 °F → 70 °F within 2 h, then 41 °F or below within 4 more h (FDA Food Code 3-501.14)'),
    (_CR + ('C8',), 'Syrup at 244–250 °F · butter at 64–68 °F'),
    (_CR + ('C9',), 'Filling 2:1 chocolate:cream · glaze 1:1 · cream at 175–185 °F'),
    (_CR + ('C11',), 'Cook to 180–183 °F'),
    (_CR + ('C12',), 'Kit target: use within 24 h at 41 °F or below (legal max 7 days, FDA Food Code 3-501.17)'),
    (_CR + ('C15',), 'Chocolate at 113–122 °F · final mix at 82–86 °F'),
    (_CR + ('C16',), 'Gelatin 10–12 g per liter (0.35–0.4 oz per quart) · puree at 77–86 °F'),
    (_CR + ('C18',), 'Toast at 325 °F for 12–15 min · caramel at 340 °F'),
    (_CR + ('C20',), 'At least 4 h at 0 °F in the blast freezer · 12 h in the freezer'),
    (_CR + ('C24',), 'Dark 122–131 °F → 82–84 °F → 88–90 °F · milk 113 °F → 81–82 °F → 84–86 °F · white 104–113 °F → '
                     '79–81 °F → 82–84 °F'),
    (_CR + ('C25',), 'Use at 95–99 °F'),
    (_CR + ('C26',), 'Syrup at 250 °F'),
    (_CR + ('C27',), '320–340 °F'),
    (_DA + ('C6',), 'Piece at 0 °F · no condensation'),
    (_DA + ('C7',), 'Glaze at 90–95 °F · piece at 0 °F'),
    (_DA + ('C16',), 'Refrigerated case at 41 °F or below (FDA Food Code 3-501.16)'),
    (_DA + ('C18',), 'The 9 major food allergens (UK: 14)'),
    # 06 · zona corregida (errata ES §5: producción en «Admin», mostrador en «Obrador»)
    (('06', 'Semana Santa', 'C8'), 'Kitchen'), (('06', 'San Valentín', 'C17'), 'Bakery case'),
    (('06', 'Día Madre-Padre', 'C14'), 'Bakery case'),
    # 06 · «Mother's & Father's Day»: «Día» = el día señalado
    (('06', 'Día Madre-Padre', 'E13'), 'On the day'), (('06', 'Día Madre-Padre', 'E14'), 'On the day'),
    (('06', 'Día Madre-Padre', 'E15'), 'On the day'),
    # 06 · «Thanksgiving (Nov)»: plazos relativos al 4.º jueves de noviembre (sustituye a Todos los Santos, D14)
    (_TS + ('E6',), '5 weeks out'), (_TS + ('E7',), '4 weeks out'), (_TS + ('E8',), '3 weeks out'),
    (_TS + ('E9',), '3 weeks out'), (_TS + ('E12',), 'Mon–Tue'), (_TS + ('E13',), 'Mon–Tue'),
    (_TS + ('E14',), 'Tue–Wed'), (_TS + ('E15',), 'Tue'), (_TS + ('E16',), 'Mon'), (_TS + ('E19',), 'Sun before'),
    (_TS + ('E20',), 'Tue'), (_TS + ('E21',), 'Wed'), (_TS + ('E22',), 'Tue–Wed'), (_TS + ('E25',), 'Fri after'),
    # 10 · coste por unidad (D13: sin símbolo)
    (('10', 'Producido vs Vendido', 'I4'), 'Unit cost'),
    # 11 · importes (D13) y tamaño en pulgadas
    (_FE + ('A36',), 'Total price (incl. sales tax, if any)'), (_FE + ('A37',), 'Deposit paid (toward the total)'),
    (_FE + ('A38',), 'Balance due'), (_FE + ('A17',), 'Size (inches)'),
    (('11', 'Registro de Encargos', 'J4'), 'Total'), (('11', 'Registro de Encargos', 'K4'), 'Deposit'),
    (('11', 'Registro de Encargos', 'L4'), 'Balance due'),
    # 11 · alérgenos que declara el cliente: los 9 de EE. UU. + gluten (celíacos) + sulfitos + los 3 de UK que faltan
    (_FE + ('A24',), '☐  Milk'), (_FE + ('C24',), '☐  Crustacean shellfish'),
    (_FE + ('A25',), '☐  Eggs'), (_FE + ('C25',), '☐  Fish'),
    (_FE + ('A26',), '☐  Peanuts'), (_FE + ('C26',), '☐  Soy'),
    (_FE + ('A27',), '☐  Wheat'), (_FE + ('C27',), '☐  Tree nuts'),
    (_FE + ('A28',), '☐  Sesame'), (_FE + ('C28',), '☐  Gluten (celiac)'),
    (_FE + ('A29',), '☐  Sulfites'), (_FE + ('C29',), '☐  Mustard (UK)'),
    (_FE + ('A30',), '☐  Celery (UK)'), (_FE + ('C30',), '☐  Lupin / mollusks (UK)'),
    # 12 · cartel: título, qué incluye cada alérgeno (US; UK entre paréntesis) y base legal
    (_CV + ('B10',), 'The 9 major food allergens (US) + 5 more for UK customers'),
    (_CV + ('C12',), 'Wheat and wheat products (US); for UK customers, all cereals with gluten: rye, barley, oats, spelt'),
    (_CV + ('C13',), 'Crustacean shellfish: crab, lobster, shrimp and products made from them'),
    (_CV + ('C14',), 'Eggs and egg products'),
    (_CV + ('C15',), 'Fish (such as tuna, cod, salmon) and fish products'),
    (_CV + ('C16',), 'Peanuts and peanut products'),
    (_CV + ('C17',), 'Soybeans and soy products, including soy lecithin'),
    (_CV + ('C18',), 'Milk and milk products, including butter, cream and lactose'),
    (_CV + ('C19',), 'Almonds, hazelnuts, walnuts, cashews, pistachios, pecans, Brazil nuts, macadamias, pine nuts'),
    (_CV + ('C20',), 'Celery and celery products (UK allergen; not a US major allergen)'),
    (_CV + ('C21',), 'Mustard and mustard products (UK allergen; not a US major allergen)'),
    (_CV + ('C22',), 'Sesame seeds and sesame products (US major allergen since 2023)'),
    (_CV + ('C23',), 'Sulfites at 10 ppm or more (declared in the US; a UK allergen)'),
    (_CV + ('C24',), 'Lupin and lupin products (UK allergen; not a US major allergen)'),
    (_CV + ('C25',), 'Mollusks such as clams, mussels, squid (UK allergen; not a US major allergen)'),
    (_CV + ('B28',), 'US: FALCPA + FASTER Act (9 major food allergens); FDA Food Code 2022 §3-602.12(C), written notice '
                     'for unpackaged food where your state has adopted it. UK: Food Information Regulations 2014 (14).'),
    # 13 · cabeceras del registro de temperaturas (CF_POR_CELDA con los mismos umbrales) y de la recepción
    (_RT + ('B4',), 'Walk-in cooler\n(32 to 41 °F)'), (_RT + ('D4',), 'Dough retarder\n(36 to 41 °F)'),
    (_RT + ('F4',), 'Freezer\n(0 °F or below)'), (_RT + ('H4',), 'Bakery case 1\n(32 to 41 °F)'),
    (_RT + ('J4',), 'Bakery case 2\n(32 to 41 °F)'),
    (_RT + ('L4',), 'Blast chiller\n(135 °F → 70 °F in 2 h, then 41 °F within 4 h)'), (_RT + ('L5',), 'Temp at 2 h'),
    (_RM + ('G4',), 'Temp at delivery (°F)'),
    # 13 · vidas útiles: conservación y notas legales US (sustituyen al art. 9.3 y al art. 4.1 del RD 1021/2022)
    (_VU + ('B5',), '32 to 41 °F, film touching the surface'),
    (_VU + ('D5',), 'Kit target 24 h (eggs); legal max 7 days at 41 °F (FDA Food Code 3-501.17). Cool in a thin layer, '
                    'never in the pot'),
    (_VU + ('D8',), 'Kit target 24 h (eggs); legal max 7 days (3-501.17). Assembled, not finished'),
    (_VU + ('D9',), 'Kit target 24 h (egg whites); legal max 7 days (3-501.17). Covered, away from moisture'),
    (_VU + ('D11',), 'Kit target 24 h (eggs) unless a shelf-life study shows more; legal max 7 days at 41 °F '
                     '(3-501.17). In a sanitized jar'),
    (_VU + ('D16',), 'Cream-filled: case at 41 °F or below (FDA Food Code 3-501.16)'),
    (_VU + ('D17',), 'Next day: day-old discount or waste. Cream-filled: case at 41 °F or below (3-501.16)'),
])
for _f, _es, _xes, _en, _xen in DENOMINACIONES:
    POR_CELDA[(HOJA_CAJA[0], HOJA_CAJA[1], 'A%d' % _f)] = _en
for _fila, (_fecha, _evento, _antel, _ae, _ag) in CALENDARIO.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'B%d' % _fila)] = _fecha
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'D%d' % _fila)] = _evento
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'F%d' % _fila)] = _antel
FORMATOS_EN = OrderedDict(_base.FORMATOS_EN)
FORMATOS_EN.update([('dd/mm/yyyy', 'mm/dd/yyyy')])             # fechas del 10, el 11 y el 13 (D-PAS)
VALORES_EN = OrderedDict()             # el inventario del ES pastelería no trae mínimos numéricos (deuda adf52a52: no aplica)

# ==========================================================================
# CF_POR_CELDA (desviación declarada, D7): umbrales de color del 13 en °F; mismas reglas, mismos rangos
# ==========================================================================
CF_POR_CELDA = OrderedDict([
    (_RT + ('B6:C36',), ('AND(B6<>"",OR(B6<0,B6>4))', 'AND(B6<>"",OR(B6<32,B6>41))')),
    (_RT + ('D6:E36',), ('AND(D6<>"",OR(D6<2,D6>6))', 'AND(D6<>"",OR(D6<36,D6>41))')),
    (_RT + ('F6:G36',), ('AND(F6<>"",F6>-18)', 'AND(F6<>"",F6>0)')),
    (_RT + ('H6:I36',), ('AND(H6<>"",OR(H6<0,H6>4))', 'AND(H6<>"",OR(H6<32,H6>41))')),
    (_RT + ('J6:K36',), ('AND(J6<>"",OR(J6<0,J6>4))', 'AND(J6<>"",OR(J6<32,J6>41))')),
    (_RT + ('L6:L36',), ('AND(L6<>"",L6>10)', 'AND(L6<>"",L6>70)')),
    (_RM + ('G5:G34',), ('4', '41')),
])

# ==========================================================================
# ADAPTAR (en español, con el dato US; las cifras salen de REGLAS_US)
# ==========================================================================
_A = _base.ADAPTAR
_HACCP_KIT = _base._HACCP_KIT
_TIRA = 'sanitizante aprobado a la concentración de la etiqueta, medida con tira (test strip) (FDA Food Code 4-501.114)'
_LOG = 'coletilla «— log reading: ____ °F»'
_VITRINA = ('°F: vitrinas refrigeradas (refrigerated bakery cases) a 41 °F o menos para lo TCS: cremas, nata, '
            'cheesecake, rellenos (FDA Food Code 3-501.16); sin «RD 1021/2022»')
_FICHAS = 'Citas de libro: usa el EN de CITAS_LIBRO y las pestañas entre comillas dobles rectas (‹· sheet "…"›)'
_ALERGENOS = ('Alérgenos US: los 9 principales (FALCPA + FASTER Act): leche, huevo, trigo, soja, frutos de cáscara (tree '
              'nuts), cacahuete, sésamo, pescado y crustáceos; en UK, los 14; aviso por escrito en lo que se vende sin '
              'envasar (FDA Food Code 2022 3-602.12(C))')
_MENORES = ('añade: si contratas menores de 18, no pueden usar ni limpiar amasadoras, batidoras industriales, '
            'laminadoras ni divisoras (FLSA, 29 CFR 570.62; salvo batidoras de sobremesa de 5 quarts o menos); con '
            '14-15 años, nada de hornear (29 CFR 570.33(h))')
_HUEVO_CRUDO = ('Merengue cocido (italiano o suizo) o claras pasteurizadas en lo que no se hornea (FDA Food Code '
                '3-302.13); dilo así, sin más cifras')
_REG_EGG = ('Sin «art. 9.3» ni «RD 1021/2022»: en EE. UU. lo elaborado listo para comer y TCS lleva fecha (date marking) '
            'y dura como mucho 7 días a 41 °F, día 1 = el de elaboración (FDA Food Code 3-501.17); las 24 h del kit '
            'son un objetivo de calidad [criterio del kit], no un tope legal')
ADAPTAR = OrderedDict([
    # 01
    (('01', 'Apertura Obrador', 'B25'), _VITRINA + '; «comprobar que están a 41 °F o menos antes de montar»; ' + _FICHAS),
    (('01', 'Apertura Obrador', 'B21'), 'Sanitizar con ' + _TIRA),
    (('01', 'Apertura Obrador', 'B27'), _ALERGENOS + '; ' + _FICHAS),
    (('01', 'Cierre Obrador', 'B6'), 'Etiqueta con fecha (date marking, FDA Food Code 3-501.17); ' + _FICHAS),
    (('01', 'Cierre Obrador', 'B9'), 'Limpiar y sanitizar con ' + _TIRA + '; mármol: producto apto para piedra'),
    (('01', 'Cierre Obrador', 'B13'), '°F: cámaras (walk-in) a 41 °F o menos, congelador a 0 °F o menos (FDA Food Code '
                                      '3-501.16); ' + _LOG + '; ' + _FICHAS),
    # 02
    (_MD + ('B8',), 'Harina de fuerza: en EE. UU. no hay «W»: «bread flour»'),
    (_MD + ('C8',), 'EE. UU.: harina de fuerza alta en proteína (bread flour, 12,5-13,5 % de proteína) y mantequilla de '
                    'laminado de 82 % de grasa (European-style butter); sin «W 300-330»'),
    (_MD + ('B10',), '°F: 72–75 °F; 68–72 °F si va directa al bloque de frío'),
    (_MD + ('C15',), 'Pesos US: onzas primero y gramos entre paréntesis: 2.3–2.5 oz (65–70 g) y 2.5–2.6 oz (70–75 g)'),
    (_MD + ('B16',), '°F: sin pasar de 82 °F'),
    (_MD + ('B18',), '°F: 375–400 °F, 14–18 min'),
    (_MD + ('C22',), 'Pesos US: baguette 9–10 oz (250–280 g) · boule 28–32 oz (800–900 g)'),
    (_MD + ('C32',), 'Espesor: 1/8 in (2.5–3 mm)'),
    (_CR + ('C19',), 'Aro de 6–7 in (16–18 cm) · inserto congelado'),
    (_MD + ('B33',), '°F: 350 °F, 15 min'),
    (_CR + ('B7',), 'Enfriar en baño de hielo (ice bath) o abatidor (blast chiller): 135 → 70 °F en 2 h y a 41 °F en 4 h '
                    'más (FDA Food Code 3-501.14); tapar y etiquetar con fecha'),
    (_CR + ('B12',), _REG_EGG + '; ' + _FICHAS),
    (_CR + ('B15',), _HUEVO_CRUDO),
    (_CR + ('B16',), _HUEVO_CRUDO),
    (_CR + ('B20',), '°F: al menos 4 h en el abatidor a 0 °F o 12 h en el congelador'),
    (_CR + ('B26',), '°F: almíbar a 250 °F'),
    (_CR + ('B27',), '°F: 320–340 °F'),
    (_DA + ('B11',), 'Fotos para redes sociales (social media)'),
    (_DA + ('B18',), _ALERGENOS + '; ' + _FICHAS),
    (_DA + ('C20',), 'Cada 2 h; lo de ayer, fuera de la vitrina normal (day-old)'),
    # 03
    (('03', 'Diario Manager', 'B14'), '°F: cámaras y vitrinas a 41 °F o menos (FDA Food Code 3-501.16); ' + _FICHAS),
    (('03', 'Semanal Manager', 'B19'), _ALERGENOS + '; ' + _FICHAS),
    (('03', 'Mensual Manager', 'B16'), 'Calibración por el método del punto de hielo (32 °F)'),
    (('03', 'Mensual Manager', 'B23'), 'Redes sociales (social media); plataformas US: Instagram, Google Business '
                                       'Profile y Yelp'),
    # 04
    (('04', 'Jefe Pastelero', 'B20'), 'Escandallo → recipe costing (cost card)'),
    (('04', 'Dependiente Vitrina', 'B7'), _ALERGENOS + '; ' + _FICHAS),
    (('04', 'Dependiente Vitrina', 'B9'), _ALERGENOS + '; ' + _FICHAS),
    # 05
    (('05', 'Limpieza Semanal', 'B11'), 'Filtros de la campana (hood filters) por el equipo; la limpieza de conductos, '
                                        'por una empresa certificada si se cocina con grasa (NFPA 96)'),
    (('05', 'Mantenimiento Mensual', 'B8'), 'Calibrar el termostato del horno con un termómetro de horno o sonda '
                                             '(oven thermometer); sin cifras'),
    (('05', 'Mantenimiento Mensual', 'B13'), '°F: lectura real frente al display con sonda; 41 °F o menos (FDA Food '
                                              'Code 3-501.16); ' + _FICHAS),
    (('05', 'Mantenimiento Mensual', 'B21'), 'Calibrar la báscula; si vendes al peso, báscula legal para el comercio '
                                             '(legal-for-trade, certificada por pesas y medidas del estado)'),
    (('05', 'Inventario', 'B9'), 'Huevos con cáscara (shell eggs) y huevo líquido pasteurizado (liquid egg)'),
    (('05', 'Inventario', 'B17'), 'Aromas: vainilla, café; licores solo para cocinar'),
    # 06
    (('06', 'Instrucciones', 'B5'), 'Sin la cifra del 40 % (no tiene fuente): «buena parte de las ventas del año se '
                                    'concentra en unas pocas temporadas clave»'),
    (('06', 'Instrucciones', 'B6'), 'Campañas US del kit, en el orden de las pestañas: Holiday Season (Navidad, Fin de '
                                    'Año y Three Kings Day / King cake), Valentine\'s Day, Easter, Mother\'s & Father\'s '
                                    'Day, Celebration Cakes (First Communions, graduations, showers) y Thanksgiving'),
    (('06', 'Navidad', 'A1'), 'Título US: «Holiday Season (Nov–Jan)»'),
    (('06', 'Navidad', 'B6'), 'Catálogo US: bandejas de galletas de Navidad, Yule logs (bûche de Noël sin tilde: «Yule '
                              'log»), stollen y panettone, pies y rosca de Reyes; sin turrón, polvorones ni roscón'),
    (('06', 'Navidad', 'B8'), 'Ingredientes de temporada US: almendra y mazapán (marzipan), fruta confitada (candied '
                              'fruit), especias de gingerbread; sin turrón'),
    (('06', 'Navidad', 'B9'), 'Personal de temporada (holiday help); ' + _MENORES),
    (('06', 'Navidad', 'B12'), 'Fechas: Nochebuena, Navidad y Nochevieja (Dec 24, 25 y 31) y Three Kings Day (Jan 6); '
                               'sin el 1 de enero como día de venta especial'),
    (('06', 'Navidad', 'A14'), '«Holiday Baking (December)»'),
    (('06', 'Navidad', 'B15'), 'Sustituye a turrones: «bandejas y latas de galletas de Navidad (2-3 semanas antes)»'),
    (('06', 'Navidad', 'B16'), 'Sustituye a polvorones: «stollen y panettone»'),
    (('06', 'Navidad', 'B17'), 'Troncos de Navidad = Yule logs'),
    (('06', 'Navidad', 'B18'), 'Cestas y lotes → holiday gift boxes'),
    (('06', 'Navidad', 'A21'), '«Pickups & New Year\'s Eve (Dec 22–31)»'),
    (('06', 'Navidad', 'B22'), 'Encargos de Nochebuena y Navidad (Christmas Eve y Christmas Day); ' + _FICHAS),
    (('06', 'Navidad', 'B25'), 'Encargos de Nochevieja (New Year\'s Eve): postres y bandejas de dulces'),
    (('06', 'Navidad', 'A28'), '«Three Kings Day (Jan 2–6)»'),
    (('06', 'Navidad', 'B29'), 'Encargos de rosca de Reyes (y King cake si lo haces); ' + _FICHAS),
    (('06', 'Navidad', 'B30'), 'Masas de rosca de Reyes (fermentación 24-48 h)'),
    (('06', 'Navidad', 'B31'), 'Primera hornada de roscas la madrugada del 4 al 5 (60-70 % del volumen, para la venta de '
                               'la tarde del 5)'),
    (('06', 'Navidad', 'B33'), 'Rellenos US de la rosca o del King cake: nata montada, crema pastelera, cream cheese; '
                               'sin «trufa» ni «cabello de ángel»'),
    (('06', 'Navidad', 'B34'), 'Decorar con ate (pasta de membrillo o guayaba) y fruta confitada, azúcar y corona; el '
                               'King cake, con azúcar morado, verde y dorado'),
    (('06', 'Navidad', 'B35'), 'Práctica US: el muñequito del niño Jesús (o el «baby» del King cake) va APARTE en la caja '
                               'para que lo meta el cliente (riesgo de atragantamiento); sin haba'),
    (('06', 'Navidad', 'B39'), _FICHAS),
    (('06', 'San Valentín', 'B8'), 'Redes sociales (social media)'),
    (('06', 'San Valentín', 'B12'), 'Bombones y trufas → chocolates y truffles'),
    (('06', 'Semana Santa', 'A1'), 'Título US: «Easter (Lent & Holy Week)»'),
    (('06', 'Semana Santa', 'B6'), 'Producción de Pascua US: hot cross buns, Easter breads, huevos y conejos de chocolate, '
                                   'carrot cake; sin torrijas ni monas'),
    (('06', 'Semana Santa', 'B9'), 'Encargos de tartas de Pascua (Easter cakes) en lugar de monas; ' + _FICHAS),
    (('06', 'Semana Santa', 'B12'), 'Sustituye a torrijas: «Hornear hot cross buns a diario — pico el Viernes Santo '
                                    '(Good Friday)»'),
    (('06', 'Semana Santa', 'B13'), 'Sustituye a pestiños y leche frita: «Hornear los Easter breads (trenza dulce, '
                                    'colomba)»'),
    (('06', 'Semana Santa', 'B14'), 'Sustituye a buñuelos de Cuaresma: «Hornear carrot cakes y coconut cakes para el fin '
                                    'de semana de Pascua»'),
    (('06', 'Semana Santa', 'B15'), 'Sustituye a monas: «Montar las tartas de Pascua con decoración de chocolate para '
                                    'recoger el sábado y el Domingo de Pascua»'),
    (('06', 'Semana Santa', 'B17'), 'Sustituye a hornazo: «Preparar los pedidos del brunch de Pascua (quiches y pasteles '
                                    'salados)»'),
    (('06', 'Semana Santa', 'B20'), 'Escaparate de Pascua (Easter window display)'),
    (('06', 'Semana Santa', 'B21'), 'Encargos de tartas de Pascua y huevos de chocolate personalizados; ' + _FICHAS),
    (('06', 'Día Madre-Padre', 'A1'), 'Título US: «Mother\'s Day (2nd Sunday in May) & Father\'s Day (3rd Sunday in '
                                      'June) — this year\'s dates: ____/____ and ____/____»'),
    (('06', 'Día Madre-Padre', 'B6'), 'Anotar las fechas de este año: Mother\'s Day (2.º domingo de mayo) y Father\'s Day '
                                      '(3.er domingo de junio)'),
    (('06', 'Día Madre-Padre', 'B15'), 'Reparto a domicilio (local delivery), si lo haces'),
    (('06', 'Comuniones (Abr-Jun)', 'A1'), 'Título US: «Celebration Cakes: First Communions, Graduations & Showers '
                                           '(Apr–Jun)»'),
    (('06', 'Comuniones (Abr-Jun)', 'B6'), 'Catálogo de tartas de celebración (tiered cakes), mesas dulces (dessert '
                                           'tables) y detalles (favors)'),
    (('06', 'Comuniones (Abr-Jun)', 'B14'), 'Depósito (deposit) del 30-50 % [criterio del kit]: práctica habitual, no ley; '
                                            'revisa las reglas de tu estado sobre depósitos no reembolsables; ' + _FICHAS),
    (('06', 'Comuniones (Abr-Jun)', 'B24'), 'Transporte: caja rígida (cake box), base antideslizante, vehículo con aire '
                                            'acondicionado o refrigerado; lo relleno de crema, a 41 °F o menos'),
    (('06', 'Comuniones (Abr-Jun)', 'B27'), 'Firmar la entrega con el cliente y cobrar el pendiente (balance due) si no se '
                                            'cobró antes; ' + _FICHAS),
    (('06', 'Todos los Santos (Oct-Nov)', 'A1'), 'Título US: «Thanksgiving Pies (4th Thursday of November)»'),
    (('06', 'Todos los Santos (Oct-Nov)', 'A5'), '«Planning (October)»'),
    (('06', 'Todos los Santos (Oct-Nov)', 'B6'), 'Carta de Thanksgiving: pies (pumpkin, pecan, apple, sweet potato), '
                                                 'pumpkin rolls y dinner rolls; sin huesos de santo, panellets ni '
                                                 'buñuelos'),
    (('06', 'Todos los Santos (Oct-Nov)', 'B7'), 'Pedir con antelación puré de calabaza (pumpkin purée), nueces pecanas, '
                                                 'manzanas, mantequilla y boniato (sweet potato)'),
    (('06', 'Todos los Santos (Oct-Nov)', 'B8'), 'Publicar la carta y abrir los pedidos anticipados (pie pre-orders)'),
    (('06', 'Todos los Santos (Oct-Nov)', 'B9'), 'Calcular la producción por día de la semana de Thanksgiving (lunes a '
                                                 'miércoles)'),
    (('06', 'Todos los Santos (Oct-Nov)', 'A11'), '«Production (Thanksgiving week)»'),
    (('06', 'Todos los Santos (Oct-Nov)', 'B12'), 'Sustituye a huesos de santo: «Hacer la masa quebrada (pie dough) y '
                                                  'forrar los moldes»'),
    (('06', 'Todos los Santos (Oct-Nov)', 'B13'), 'Sustituye a panellets: «Hornear los pies de fruta (apple, pecan)»'),
    (('06', 'Todos los Santos (Oct-Nov)', 'B14'), 'Sustituye a buñuelos de viento: «Hornear los pies de crema (pumpkin, '
                                                  'sweet potato), enfriarlos y guardarlos a 41 °F o menos: son TCS (FDA '
                                                  'Food Code 3-501.16)»'),
    (('06', 'Todos los Santos (Oct-Nov)', 'B15'), 'Alérgenos de temporada US: nuez pecana (tree nuts), trigo, leche y '
                                                  'huevo están en casi todos los pies; ' + _FICHAS),
    (('06', 'Todos los Santos (Oct-Nov)', 'B16'), 'Escaparate de temporada y lista de precios por pie (no al peso)'),
    (('06', 'Todos los Santos (Oct-Nov)', 'A18'), '«Pre-Orders & Pickups (Sun–Wed)»'),
    (('06', 'Todos los Santos (Oct-Nov)', 'B19'), 'Cerrar los pedidos anticipados (pre-order cutoff); ' + _FICHAS),
    (('06', 'Todos los Santos (Oct-Nov)', 'B20'), 'Franjas de recogida del miércoles antes de Thanksgiving'),
    (('06', 'Todos los Santos (Oct-Nov)', 'B21'), 'Reforzar el mostrador el miércoles antes de Thanksgiving (turno doble)'),
    (('06', 'Todos los Santos (Oct-Nov)', 'B22'), 'Reponer la vitrina cada 2 h: los pies de crema salen de la vitrina '
                                                  'refrigerada'),
    (('06', 'Todos los Santos (Oct-Nov)', 'B25'), _FICHAS),
    # 07
    (('07', 'Instrucciones', 'B10'), _base.ADAPTAR.get(('07', 'Instrucciones', 'B10'), 'Imprime en US Letter')),
    (('07', 'Por Perfil', 'A5'), 'Head Pastry Chef (sin «Chef Pâtissier»)'),
    # 08
    (('08', 'Instrucciones', 'B7'), _VITRINA + ' — en EE. UU. el tope es 41 °F para lo TCS (FDA Food Code 3-501.16), no '
                                    'un real decreto; horas en reloj de 12 h (6:45 AM, 7:45 AM, 8:00 AM)'),
    (('08', 'Apertura del Negocio', 'A2'), 'Temperatura en °F: «Case temp at opening: ______ °F»'),
    (('08', 'Apertura del Negocio', 'B5'), _VITRINA + '; anotar la lectura (41 °F o menos); ' + _FICHAS),
    (('08', 'Apertura del Negocio', 'B7'), '°F: la tienda entre 68 y 72 °F'),
    (('08', 'Apertura del Negocio', 'B8'), 'TPV → POS; datáfono → card terminal'),
    (('08', 'Apertura del Negocio', 'B14'), '°F: vitrinas a 41 °F o menos antes de montar'),
    (('08', 'Apertura del Negocio', 'B24'), _base.ADAPTAR[('08', 'Apertura del Negocio', 'B8')]),
    (('08', 'Cierre del Negocio', 'A2'), 'Temperatura en °F: «Case temp at closing: ______ °F»'),
    (('08', 'Cierre del Negocio', 'B10'), 'Donación: la Bill Emerson Good Samaritan Food Donation Act (42 U.S.C. 1791) '
                                          'protege lo donado de buena fe; ' + _FICHAS),
    (('08', 'Cierre del Negocio', 'B12'), 'Z del TPV → POS Z report; arquear → count the cash; descuadre → over/short; ' +
     _FICHAS),
    (('08', 'Cierre del Negocio', 'B22'), _base.ADAPTAR[('08', 'Apertura del Negocio', 'B8')]),
    # 09
    (('09', 'Instrucciones', 'B5'), 'Arqueo → cash count; Z del TPV → POS Z report'),
    (('09', 'Instrucciones', 'B9'), 'Cita el rótulo EN de la celda: "Starting bank (opening float)"'),
    (('09', 'Instrucciones', 'B10'), 'Z del POS; tarjetas SIN propinas; otros medios + propinas de tarjeta pagadas en '
                                     'efectivo del cajón'),
    (('09', 'Instrucciones', 'B11'), _base.ADAPTAR[('09', 'Instrucciones', 'B16')]),
    (('09', 'Instrucciones', 'B12'), _base.ADAPTAR[('09', 'Instrucciones', 'B17')]),
    (('09', 'Instrucciones', 'B13'), 'Registro: efectivo neto (sin el fondo), tarjetas sin propinas, otros + propinas '
                                     'pagadas y la Z; el over/short se calcula solo'),
    (('09', 'Instrucciones', 'B17'), _base.ADAPTAR[('09', 'Instrucciones', 'B14')]),
    (('09', 'Apertura de Caja', 'B7'), 'Cita el rótulo EN de la celda: "Starting bank (opening float)"'),
    (('09', 'Apertura de Caja', 'B9'), 'TPV → POS'),
    (('09', 'Apertura de Caja', 'B10'), 'X de apertura → X report'),
    (('09', 'Apertura de Caja', 'B12'), 'Datáfono → card terminal'),
    (('09', 'Cierre de Caja', 'B5'), 'Z de cierre → POS Z report'),
    (('09', 'Cierre de Caja', 'B10'), _base.ADAPTAR[('09', 'Cierre de Caja', 'B10')]),
    (('09', 'Cierre de Caja', 'B11'), 'Z del TPV → POS Z report; descuadre → over/short'),
    (('09', 'Registro Mensual', 'A37'), 'El fondo es un saldo, no una venta: en «TOTALS» la columna «Starting Bank» '
                                        'muestra el fondo medio de los días anotados, no su suma (rótulos EN de la fila 4)'),
    # 10
    (('10', 'Instrucciones', 'B5'), 'Sin euros: «with the cost in your currency»'),
    (('10', 'Instrucciones', 'B11'), 'Escandallo → recipe costing; coste de materia prima → ingredient cost'),
    (('10', 'Instrucciones', 'B16'), 'Registra lo que decides: es lo que te deja defender tu criterio ante el inspector '
                                     'de sanidad (health inspector)'),
    (('10', 'Producido vs Vendido', 'A257'), 'Criterio del kit (food safety): lo expuesto en la vitrina NO se congela para '
                                             'venderlo después; solo se congela producto del día que no ha salido a la '
                                             'venta, abatido a 0 °F. Si vendes algo que estuvo congelado, dilo [criterio '
                                             'del kit: no hay obligación federal para la bollería sin envasar]. Antes que '
                                             'tirar, dona: la Bill Emerson Good Samaritan Food Donation Act (42 U.S.C. '
                                             '1791) protege la donación de buena fe; revisa también las reglas de tu '
                                             'estado y tu condado. Sin APPCC ni leyes españolas'),
    (('10', 'Resumen por Partida', 'A16'), 'Mantén los porcentajes como criterio del kit (3-8 %, 10 %)'),
    # 11
    (('11', 'Instrucciones', 'B9'), 'Lee en voz alta el mensaje de la tarta (cake message) y la fecha de recogida antes '
                                    'de cobrar el depósito (deposit)'),
    (('11', 'Instrucciones', 'B17'), 'Privacidad US [criterio del kit], sin RGPD: la ficha recoge datos personales y de '
                                     'salud (alergias); recoge solo lo necesario, la casilla de consentimiento de las '
                                     'alergias es distinta de la de marketing y ninguna va marcada de antemano; guarda '
                                     'las fichas bajo llave, no a la vista, y destrúyelas (shred) al mes de la entrega '
                                     'salvo lo que necesites para impuestos; revisa la ley de privacidad de tu estado'),
    (('11', 'Instrucciones', 'B20'), 'Menú de Excel EN: «Data › Data Validation»; rótulos «Status», «Payment method» y '
                                     '«Order channel»'),
    (('11', 'Instrucciones', 'B21'), 'Política de depósito (deposit policy)'),
    (('11', 'Ficha de Encargo', 'A20'), 'Mensaje de la tarta: «Cake message (PRINT CLEARLY IN CAPITALS)»'),
    (('11', 'Ficha de Encargo', 'A22'), '«Customer\'s Allergies & Intolerances»'),
    (('11', 'Ficha de Encargo', 'A23'), 'Añade: los 9 primeros son los alérgenos principales de EE. UU. (FALCPA + FASTER '
                                        'Act); el resto, gluten para celíacos y los de UK; ' + _FICHAS),
    (('11', 'Ficha de Encargo', 'A31'), 'ALERGIA CONFIRMADA → «CONFIRMED ALLERGY» (no es una preferencia)'),
    (('11', 'Ficha de Encargo', 'A32'), 'Consentimiento US sin «art. 9.2.a RGPD»: «Acepto que uséis la información de '
                                        'alergias de esta ficha solo para preparar mi encargo con seguridad. Sin este '
                                        'consentimiento no podemos aceptar un encargo con alergias.»'),
    (('11', 'Ficha de Encargo', 'A39'), 'Política de depósito: práctica habitual, no ley (p. ej. «el depósito no se '
                                        'devuelve si el encargo se cancela con menos de 48 h»); revisa las reglas de tu '
                                        'estado sobre depósitos no reembolsables antes de imprimirla'),
    (('11', 'Ficha de Encargo', 'A44'), '«Privacy Notice»'),
    (('11', 'Ficha de Encargo', 'A45'), '«Business name and contact»'),
    (('11', 'Ficha de Encargo', 'A46'), 'Aviso de privacidad US [criterio del kit], sin RGPD ni bases jurídicas: quién (el '
                                        'negocio de esta ficha), para qué (tomar, preparar, entregar y facturar este '
                                        'encargo), alergias (solo para preparar el encargo con seguridad, con el '
                                        'consentimiento de arriba), datos de otras personas (con su permiso), cuánto se '
                                        'guarda (se destruye al mes de la entrega salvo lo que pidan los impuestos), no '
                                        'se vende ni se comparte, y dudas en el mostrador'),
    (('11', 'Ficha de Encargo', 'A49'), 'Casilla opcional de marketing, sin marcar: «Quiero recibir novedades y ofertas '
                                        'por email o mensaje de texto»; los mensajes de texto de marketing piden '
                                        'consentimiento escrito previo (TCPA, 47 CFR 64.1200) y los emails, una forma de '
                                        'darse de baja (CAN-SPAM)'),
    # 12
    (('12', 'Instrucciones', 'B7'), 'Ley US: los 9 alérgenos principales (FALCPA + FASTER Act) en lo envasado; en lo que '
                                    'se vende sin envasar (vitrina, mostrador), aviso por escrito según el FDA Food Code '
                                    '2022 3-602.12(C) donde tu estado lo haya adoptado; UK: 14 alérgenos (Food '
                                    'Information Regulations 2014). Sin Reglamento UE ni RD 126/2015'),
    (('12', 'Instrucciones', 'B8'), 'Producto sin envasar: información POR ESCRITO accesible antes de comprar (3-602.12(C): '
                                    'folleto, cartel, etiqueta de la vitrina o carta); sin la vía oral española'),
    (('12', 'Instrucciones', 'B9'), 'El «may contain» es voluntario y tiene que ser veraz: no sustituye a declarar los '
                                    'alérgenos que llevas a propósito'),
    (('12', 'Instrucciones', 'B14'), 'Con las referencias EN del GLOSARIO: pain aux raisins y fruta confitada (sulfitos, '
                                     '10 ppm o más se declaran), almond nougat / torrone (clara de huevo), coberturas y '
                                     'chips de chocolate (lecitina de soja), polvorones (sésamo y mantequilla)'),
    (('12', 'Instrucciones', 'B15'), 'Declarar «los 9» (o «los 14») cuando no trabajas con pescado ni crustáceos es el «may '
                                     'contain» genérico que no sirve'),
    (('12', 'Instrucciones', 'B16'), 'Inspector → health inspector'),
    (('12', 'Matriz Alérgenos', 'V10'), 'Sulfitos: las pasas suelen ir sulfitadas; desde 10 ppm se declaran (comprobar la '
                                        'ficha técnica = spec sheet)'),
    (('12', 'Matriz Alérgenos', 'V23'), 'Sulfitos: comprobar en la ficha técnica de la fruta confitada y del ate'),
    (('12', 'Matriz Alérgenos', 'V24'), 'Sulfitos: si las pasas o la piel confitada llevan sulfitos (10 ppm o más), '
                                        'decláralos como ingrediente, no como traza'),
    (('12', 'Matriz Alérgenos', 'V28'), 'Sésamo: algunos polvorones llevan ajonjolí; leche: el perfil propuesto es con '
                                        'manteca (lard o shortening); con mantequilla, la leche es ●'),
    (('12', 'Matriz Alérgenos', 'V29'), 'Clara de huevo: el torrone duro la lleva; algunos turrones blandos no: verifica la '
                                        'receta o la marca'),
    (('12', 'Carta de Alérgenos', 'A54'), 'Frase de contaminación cruzada (cross-contact) con los alérgenos US: trigo '
                                          '(gluten), huevo, leche, frutos de cáscara, soja y sésamo'),
    (('12', 'Cartel Vitrina', 'B7'), 'Misma frase que la carta, con los alérgenos US: trigo (gluten), huevo, leche, frutos '
                                     'de cáscara, soja y sésamo'),
    (('12', 'Etiquetas Vitrina', 'B2'), 'Abreviaturas US fijas: «W wheat · E eggs · M milk · TN tree nuts · S soy · SE '
                                        'sesame · SU sulfites»; imprimir en cartulina (card stock)'),
    # 13
    (('13', 'Instrucciones', 'B6'), 'Los tres registros que pide el inspector de sanidad (health inspector)'),
    (('13', 'Instrucciones', 'B11'), 'Albarán → invoice / packing slip'),
    (('13', 'Instrucciones', 'B12'), 'Date marking US: todo lo que entra en la cámara sale etiquetado con fecha; lo TCS '
                                     'listo para comer, como mucho 7 días a 41 °F (FDA Food Code 3-501.17); la hora, en '
                                     'lo elaborado con huevo [criterio del kit]; sin RD 1021/2022'),
    (('13', 'Instrucciones', 'B13'), _REG_EGG),
    (('13', 'Instrucciones', 'B16'), 'Rangos US: cámara 32 a 41 °F · cámara de masas (dough retarder) 36 a 41 °F · '
                                     'congelador 0 °F o menos · vitrinas 32 a 41 °F · abatidor de 135 a 70 °F en 2 h y a '
                                     '41 °F en 4 h más (FDA Food Code 3-501.14 y 3-501.16)'),
    (('13', 'Instrucciones', 'B17'), 'Ajusta los rangos a tu plan de seguridad alimentaria (food safety plan) desde «Home › '
                                     'Conditional Formatting › Manage Rules»; los 41 °F de lo TCS no se suben: es el tope '
                                     'del FDA Food Code (3-501.16)'),
    (('13', 'Instrucciones', 'B21'), _FICHAS),
    (('13', 'Registro de Temperaturas', 'A40'), 'Criterio del kit: si lo TCS ha estado por encima de 41 °F más de 2 h, o '
                                                'no sabes cuánto, tíralo y anótalo como merma (solo un procedimiento '
                                                'escrito de tiempo como control permite hasta 4 h sin frío, FDA Food Code '
                                                '3-501.19); ' + _FICHAS),
    (('13', 'Recepción de Mercancía', 'A2'), 'Albarán → invoice'),
    (('13', 'Recepción de Mercancía', 'A38'), 'Criterios US: refrigerado TCS por encima de 41 °F; huevos con cáscara en un '
                                              'camión a más de 45 °F de aire; leche y nata, hasta 45 °F si la ley de '
                                              'lácteos lo permite y se enfrían a 41 °F en 4 h (FDA Food Code 3-202.11 y '
                                              '3-501.14); congelado con signos de descongelación; envase roto; fecha a '
                                              'menos de 2 días; camión sucio o sin frío; factura que no coincide. Albarán '
                                              '→ invoice'),
    (('13', 'Etiquetas de Elaborado', 'B2'), _REG_EGG + '; rótulos EN de la etiqueta («Made (date & time):», «Use by (date '
                                             '& time):»)'),
    (('13', 'Vidas Útiles', 'A24'), _REG_EGG + '; lo relleno, en vitrina a 41 °F o menos (3-501.16); el resto de vidas '
                                    'útiles son orientativas: las fija tu plan de seguridad alimentaria (food safety plan); '
                                    'si dudas, consulta a tu asesor o a tu departamento de salud (health department)'),
    # B01
    (('B01', 'Briefing Diario', 'B6'), 'Con las referencias EN del GLOSARIO: viennoiserie (croissants, custard danishes, '
                                       'conchas...)'),
    (('B01', 'Briefing Diario', 'B17'), _ALERGENOS + '; ' + _FICHAS),
    # B02
    (('B02', 'Instrucciones', 'B6'), 'Fechas móviles US: Mardi Gras, Easter, Mother\'s Day, Father\'s Day, Thanksgiving '
                                     'y Black Friday (columna verde «This year\'s date»)'),
    (('B02', 'Instrucciones', 'B7'), 'Añade la nota UK: Mothering Sunday (marzo), bank holidays y Boxing Day en las filas '
                                     'libres'),
])
for _fila, (_fecha, _evento, _antel, _ae, _ag) in CALENDARIO.items():
    if _ae:
        ADAPTAR[(HOJA_CAL[0], HOJA_CAL[1], 'E%d' % _fila)] = 'Evento EN: «%s». %s' % (_evento, _ae)
    if _ag:
        ADAPTAR[(HOJA_CAL[0], HOJA_CAL[1], 'G%d' % _fila)] = 'Evento EN: «%s». %s' % (_evento, _ag)
# Celdas ES con °C cuya EN NO lleva cifra en °F (G7 no les exige °F): ninguna
CELSIUS_SIN_F = frozenset()
AJUSTE_MAQUETA_ES = True

# ==========================================================================
# REGLAS_US: las del base que aplican + las de la pastelería (fuente única de lo que el kit puede afirmar)
# ==========================================================================
REGLAS_US = OrderedDict(_base.REGLAS_US)
for _k in ('parasitos', 'moluscos', 'recalentado', 'aviso_consumidor', 'campana', 'supresion', 'refrigerante',
           'fichajes', 'frecuencia_pago', 'backflow', 'grasas', 'extintor_mes', 'extintor_ano', 'hidrostatica',
           'lavado_vegetal', 'joyas', 'enfermos', 'lavamanos'):
    del REGLAS_US[_k]
REGLAS_US.update([
    ('vitrina_tcs', ('vitrina refrigerada a 41 °F o menos para lo TCS: cremas, natillas, nata, cheesecake, pies de crema',
                     'FDA Food Code 2022 §3-501.16(A)(2); §1-201.10 (TCS)')),
    ('enfriar_cremas', ('135 → 70 °F en 2 h y → 41 °F en 4 h más (crema pastelera, curd, ganache con nata)',
                        'FDA Food Code 2022 §3-501.14')),
    ('date_marking_kit', ('7 días a 41 °F como máximo legal; 24 h como objetivo del kit en lo elaborado con huevo',
                          'FDA Food Code 2022 §3-501.17; [criterio del kit]')),
    ('huevo_crudo', ('huevo pasteurizado o merengue cocido en lo que no se cocina (mousse, merengue sin hornear)',
                     'FDA Food Code 2022 §3-302.13')),
    ('tphc', ('hasta 4 h sin frío solo con procedimiento escrito y hora marcada; si no, más de 2 h por encima de 41 °F o '
              'tiempo desconocido → a la basura (criterio del kit)', 'FDA Food Code 2022 §3-501.19; [criterio del kit]')),
    ('recepcion', ('refrigerado TCS a 41 °F o menos; huevos con cáscara en aire a 45 °F o menos; leche hasta 45 °F si la '
                   'ley lo permite, enfriada a 41 °F en 4 h; congelado, congelado', 'FDA Food Code 2022 §3-202.11(A), '
                                                                                   '(B), (C), (E); §3-501.14')),
    ('aviso_alergenos', ('aviso escrito de los alérgenos principales en lo que se vende sin envasar',
                         'FDA Food Code 2022 §3-602.12(C) (donde el estado lo haya adoptado)')),
    ('formacion_alergenos', ('formación del equipo en alergias según su puesto', 'FDA Food Code 2022 §2-103.11(O)')),
    ('sulfitos', ('sulfitos de 10 ppm o más: se declaran (no son «major allergen»)', '21 CFR 101.100(a)(4)')),
    ('may_contain', ('«may contain» voluntario y veraz; no sustituye a declarar lo que se lleva a propósito',
                     '[fuente] FDA, guía de alérgenos (advisory labeling); [criterio del kit]')),
    ('donacion', ('donación de buena fe protegida salvo negligencia grave o dolo', '42 U.S.C. 1791 (Bill Emerson Good '
                                                                                 'Samaritan Food Donation Act)')),
    ('menores_hornear', ('menores de 18: sin amasadoras, batidoras industriales, laminadoras ni divisoras (también '
                         'limpiarlas), salvo batidoras de sobremesa ≤ 5 quarts; 14-15 años: sin hornear',
                         '29 CFR 570.62 (HO 11); 29 CFR 570.33(h); DOL Fact Sheet #58')),
    ('marketing', ('mensajes de texto de marketing con consentimiento escrito previo; emails con baja',
                   '47 CFR 64.1200 (TCPA); 15 U.S.C. 7704 (CAN-SPAM)')),
    ('deposito', ('depósito del 30-50 %: práctica habitual, no ley; reglas estatales sobre depósitos no reembolsables',
                  '[criterio del kit]; guía EN §8')),
    ('bascula', ('venta al peso con báscula legal para el comercio', '[estatal] pesas y medidas; NIST Handbook 44')),
    ('campana_pas', ('filtros por el equipo; conductos por empresa certificada si se cocina con grasa',
                     'NFPA 96; [local]')),
    ('conversion', ('°C → °F redondeado al grado; hornos a los escalones habituales de EE. UU. (350, 375, 400, 450 °F); '
                    'pesos en oz (g); espesores en in (mm)',
                    '[criterio del kit]')),
    ('rosca_baby', ('el muñequito va aparte para que lo meta el cliente', '[criterio del kit] riesgo de atragantamiento')),
    ('temporada_pas', ('Mother\'s Day 2.º domingo de mayo; Father\'s Day 3.er domingo de junio; Thanksgiving 4.º jueves '
                       'de noviembre; King cake de Epiphany (6-ene) a Mardi Gras',
                       '36 U.S.C. 117 y 109; 5 U.S.C. 6103; guía EN §7')),
    ('plazos_kit', ('food cost 28-35 %; merma < 5 % (3-8 % habitual, revisar > 10 %); señal 30-50 %; vidas útiles de la '
                    'tabla del 13', '[criterio del kit]')),
])
# °F que el kit puede afirmar (G7): seguridad (0, 32, 41, 45, 70, 135), cámara de masas (36), proceso del 02 y del 13
# (conversiones de POR_CELDA y ADAPTAR) y hornos
GRADOS_F_SPEC = {0, 32, 36, 37, 39, 41, 43, 45, 54, 57, 64, 68, 70, 72, 75, 77, 79, 81, 82, 84, 86, 88, 90, 95, 99,
                 104, 113, 122, 131, 135, 175, 180, 183, 185, 244, 250, 320, 325, 340, 350, 375, 400, 450, 480}

# ==========================================================================
# Pistas y dependencias de la pastelería (extraer_textos.py)
# ==========================================================================
PISTAS_CAMBIO = {r'Kit de Tareas': 'D2: «Pastry Shop Checklists Kit Pro»'}
PISTAS_FUERA = (r'Restaurante Casual',)
HOJAS_CITADAS = ('Producido vs Vendido', 'Plan Semanal', 'Etiquetas de Elaborado', 'Vidas Útiles',
                 'Registro de Temperaturas', 'Ficha de Encargo', 'Encargos de Hoy', 'Etiquetas Vitrina', 'Cartel Vitrina',
                 'Carta de Alérgenos', 'Matriz Alérgenos', 'Apertura de Caja', 'Cierre de Caja', 'Apertura del Negocio',
                 'Cierre del Negocio', 'Apertura Obrador', 'Cierre Obrador', 'Comuniones (Abr-Jun)')
_PISTA_CITAS = ('Citas de libro (→ NN …): ' + ' · '.join('«%s» → «%s»' % kv for kv in CITAS_LIBRO.items()) +
                '. Hoja citada (con «hoja», «hojas» o sola tras «·») → ‹sheet "EN"› / ‹sheets "EN" and "EN"›, entre '
                'comillas dobles rectas: ' + ' · '.join('%s → "%s"' % (h, HOJAS[h]) for h in HOJAS_CITADAS) +
                '; «columna Acción» → ‹"Action" column›; «fichero 08» → «file 08»')
PISTAS_EXTRA = [
    (r'→ ?(?:BONUS-)?\d{2} |fichero \d{2}|hoja [A-ZÁÉÍÓÚ]', _PISTA_CITAS),
    (r'Pastelería / Obrador|Pastelería con Tienda', 'D2: la EN no lleva el sufijo de variante: quita «— Pastelería / '
                                                    'Obrador» / «Pastelería con Tienda»'),
    (r'[Pp]astelería', 'pastelería → pastry shop (bakery solo si el texto habla de pan)'),
    (r'[Oo]brador', 'obrador → kitchen / pastry kitchen (production kitchen); nunca «workshop»'),
    (r'[Vv]itrina', 'vitrina → bakery case (refrigerada: refrigerated bakery case); despacho → counter'),
    (r'[Dd]ependiente', 'dependiente → counter associate'),
    (r'[Ee]ncargad|[Rr]esponsable (de )?turno', 'encargado / responsable de turno → shift lead'),
    (r'[Jj]efe [Pp]astelero|[Pp]âtissier', 'jefe pastelero → head pastry chef'),
    (r'[Bb]oller[ií]a', 'bollería → viennoiserie (cliente: breakfast pastries)'),
    (r'[Ee]ncargo', 'encargo → custom order (pedido anticipado: pre-order); ficha de encargo → order form'),
    (r'[Ss]eñal\b|[Aa] cuenta', 'señal → deposit; pendiente de cobro → balance due'),
    (r'[Dd]edicatoria', 'dedicatoria → cake message'),
    (r'[Rr]ecogida', 'recogida → pickup; franja de recogida → pickup slot'),
    (r'[Mm]ermas?', 'merma → waste (waste log); producto del día anterior → day-old'),
    (r'[Ee]scandallo', 'escandallo → recipe costing (cost card)'),
    (r'[Aa]batidor', 'abatidor → blast chiller (para congelar: blast freezer)'),
    (r'[Cc]ámara de fermentación|[Rr]etardador', 'cámara de fermentación controlada → retarder-proofer; retardador → '
                                                 'retarder; fermentadora → proofer'),
    (r'[Ll]aminadora|[Ll]aminar', 'laminadora → dough sheeter; laminar → laminate'),
    (r'[Aa]masadora|[Bb]atidora|[Pp]lanetaria', 'amasadora → spiral mixer; batidora planetaria → planetary mixer'),
    (r'[Mm]asa madre|[Pp]refermento', 'masa madre → sourdough starter (levain); prefermento → preferment'),
    (r'[Hh]orno', 'horno de pisos → deck oven; de convección → convection oven; hornada → bake'),
    (r'[Bb]andejas?|[Mm]oldes?', 'bandeja → sheet pan (sheet tray); molde → pan / mold; rejilla → cooling rack'),
    (r'[Mm]angas?|[Bb]oquillas?', 'manga pastelera → piping bag; boquilla → piping tip'),
    (r'[Bb]londas?|[Pp]apel antigrasa', 'blondas → doilies; papel antigrasa → parchment / bakery tissue'),
    (r'[Mm]ármol', 'mesa de mármol → marble slab / marble bench'),
    (r'[Ff]icha técnica', 'ficha técnica → spec sheet'),
    (r'[Aa]lbar[aá]n', 'albarán → invoice / packing slip'),
    (r'RRSS|redes', 'RRSS → social media'),
    (r'TPV|[Dd]atáfono', 'TPV / datáfono → POS / card terminal'),
    (r'[Cc]uadr', 'cuadre de caja → cash count / reconcile'),
    (r'APPCC', 'APPCC → food safety plan (HACCP-based)'),
    (r'[Ll]ocal\b', 'el local → the shop'),
    (r'[Ii]nspecci', 'inspección → health inspection'),
    (r'\bkg\b|\d g\b|\bmm\b|\bcm\b|litro', 'Unidades US: oz/lb primero y g entre paréntesis; in (mm); qt (L)'),
]
DEPENDENCIAS_EXTRA = OrderedDict([
    ('variante', ('Sufijo de variante «Pastelería / Obrador»', r'Pastelería / Obrador|Pastelería con Tienda',
                  'D2: la EN no lleva sufijo')),
    ('norma_pasteleria', ('Normativa española de pastelería (RD 1021/2022, art. 9.3 y 4.1, RD 126/2015, Reglamento UE '
                          '1169/2011, RGPD)', r'RD 1021|art\. 9\.3|art\. 4\.1|RD 126|1169/2011|RGPD|Real Decreto|'
                          r'Reglamento \(UE\)', 'D-PAS: FDA Food Code 2022 (3-501.16, 3-501.17, 3-602.12(C)), FALCPA + '
                          'FASTER; privacidad US [criterio del kit]')),
    ('festivos_pasteleria', ('Campañas y dulces españoles', r'Roscón|roscón|[Tt]orrijas|[Mm]onas?\b|[Pp]estiños|hornazo|'
                             r'[Hh]uesos de santo|[Pp]anellets|[Pp]olvor[oó]n|[Tt]urr[oó]n|[Cc]omuniones|Todos los '
                             r'Santos|Reyes|Semana Santa|19 de marzo|Día del Padre|Día de la Madre',
                             'D14 / D-PAS: campañas US (06 y B02)')),
    ('alergenos_ue', ('14 alérgenos UE', r'14 [Aa]lérgenos|[Ll]os 14|Altramuces|Apio|Mostaza|Moluscos',
                      'D-PAS: 9 de EE. UU. en las mismas columnas + 5 marcados UK')),
    ('unidades', ('Pesos y medidas métricas', r'\d ?(?:g|kg|mm|cm)\b|por litro|W \d{3}', 'D-PAS: oz/lb (g), in (mm)')),
])

# aplicar_en / gates_en (autotest): la hoja con horas de celda (el 01 las trae, como el base) y hoja con verdes
HOJA_HORAS = ('01', 'Apertura Obrador')
# G3: libros cuyo ES no trae la línea de marca D19 (el 09 de la pastelería cierra con «© AI Chef Pro — aichef.pro»)
LIBROS_SIN_MARCA = ('09',)
CITA_AUTOTEST = '(FDA Food Code 3-501.18)'                     # autotest G7: una cita que NO está en REGLAS_US


def _rebind(f):
    return types.FunctionType(f.__code__, globals(), f.__name__, f.__defaults__, f.__closure__)


titulo_interior = _rebind(_base.titulo_interior)
_autotest_base = _rebind(_base.autotest)
_cruzar_censo_base = _rebind(_base.cruzar_censo)


def autotest():
    # el «11» fijo del base (FICHEROS debe tener 11 nombres) es el único supuesto del molde que no vale aquí: se cambia
    # por N_LIBROS sin tocar código común
    err = [e for e in _autotest_base() if e != 'FICHEROS debe tener 11 nombres EN distintos']
    if len(FICHEROS) != N_LIBROS or len(set(FICHEROS.values())) != N_LIBROS:
        err.append('FICHEROS debe tener %d nombres EN distintos' % N_LIBROS)
    if len(TITULO_SEO) > 75:
        err.append('TITULO_SEO > 75 caracteres (D2)')
    rx = re.compile(TERMINOS_PROHIBIDOS)
    if not rx.search(TERMINO_PROHIBIDO_EJEMPLO):
        err.append('TERMINO_PROHIBIDO_EJEMPLO no lo caza TERMINOS_PROHIBIDOS')
    for ok in ('head pastry chef', 'counter associate', 'shift lead', 'bakery case', 'cookie scoop', 'venue',
               'coffee machine', 'restaurant consultant', 'restaurant supply store', 'pastry cook'):
        if rx.search(ok):
            err.append('TERMINOS_PROHIBIDOS caza lo permitido (%r)' % ok)
    rx_ctx = re.compile(RX_CONTEXTO_PENDIENTE)
    for ok in ('head pastry chef', 'counter associate', 'bakery case', 'restaurant consultant'):
        if rx_ctx.search(ok):
            err.append('RX_CONTEXTO_PENDIENTE caza lo permitido (%r)' % ok)
    for k, v in list(GLOSARIO.items()) + list(POR_CELDA.items()) + list(CLAVES.items()):
        if (k not in _base.GLOSARIO or k in _GLOSARIO_PAS) and isinstance(v, str) and rx.search(v):
            err.append('texto EN fijado con un término prohibido: %r → %r' % (k, v))
        if isinstance(v, str) and ('°C' in v or '€' in v):
            err.append('°C o € en un texto EN fijado: %r' % (k,))
    for k in ('Gluten', 'Crustáceos', 'Huevos', 'Pescado', 'Cacahuetes', 'Soja', 'Lácteos', 'Frutos de cáscara', 'Apio',
              'Mostaza', 'Sésamo', 'Sulfitos', 'Altramuces', 'Moluscos'):
        if len(GLOSARIO[k]) > 15:
            err.append('alérgeno %r: %r > 15 caracteres (cabecera girada de 95 pt)' % (k, GLOSARIO[k]))
    for k in CATEGORIAS:
        if CLAVES[k] != GLOSARIO[k]:
            err.append('categoría %r: CLAVES y GLOSARIO distintos (el SUMIF del resumen no casaría)' % k)
    _dup = [v for v in set(CLAVES.values()) if sum(1 for x in CLAVES.values() if x == v) > 1]
    if _dup:
        err.append('CLAVES con EN repetidos: %r' % _dup)
    if CITA_AUTOTEST.strip('()').split()[-1] in ' '.join(f for _v, f in REGLAS_US.values()):
        err.append('CITA_AUTOTEST está en REGLAS_US: G7 no la cazaría')
    # °F de los textos fijados, de los ADAPTAR y de las CLAVES dentro de GRADOS_F_SPEC (G7 lo mide luego en los xlsx)
    rx_f = re.compile(r'((?:[−-]?\d{1,3}\s*(?:–|→|to|y|and|a)?\s*)+)°F')
    for nombre, dic in (('POR_CELDA', POR_CELDA), ('ADAPTAR', ADAPTAR), ('CLAVES', CLAVES)):
        for k, v in dic.items():
            for m in rx_f.finditer(v):
                for num in re.findall(r'[−-]?\d{1,3}', m.group(1)):
                    x = int(num.replace('−', '-'))
                    if x not in GRADOS_F_SPEC:
                        err.append('%s %r: %s °F fuera de GRADOS_F_SPEC' % (nombre, k, x))
    # CF_POR_CELDA: los umbrales EN, en GRADOS_F_SPEC
    for k, (es, en) in CF_POR_CELDA.items():
        for x in re.findall(r'[<>]=?(-?\d+)|^(\d+)$', en):
            v = int(x[0] or x[1])
            if v not in GRADOS_F_SPEC:
                err.append('CF_POR_CELDA %r: %s fuera de GRADOS_F_SPEC' % (k, v))
    # 09: las 15 filas de billetes y monedas, CASOS_G5 coherente con DENOMINACIONES
    if [d[0] for d in DENOMINACIONES] != _FILAS_CAJA:
        err.append('DENOMINACIONES: filas fuera de 21-27 / 29-36 (09 del ES pastelería)')
    if abs(sum(d[4] for d in DENOMINACIONES) - CASOS_G5[0]['esperado'][(_HC, 'C37')]) > 1e-6:
        err.append('CASOS_G5: el total de 1 de cada no es la suma de DENOMINACIONES')
    for caso in CASOS_G5:
        for h, _c in list(caso['entradas']) + list(caso['esperado']):
            if h not in HOJAS_ES_POR_LIBRO['09']:
                err.append('CASOS_G5 %s: hoja %r fuera del 09' % (caso['nombre'], h))
    c2 = CASOS_G5[1]
    neto = c2['entradas'][(_HC, 'B21')] * 100 + c2['entradas'][(_HC, 'B22')] * 50 - c2['entradas'][(_HA, 'C17')]
    if neto + 3000 + 150 != c2['esperado'][(_HC, 'B45')] or c2['entradas'][(_HR, 'C5')] != neto:
        err.append('CASOS_G5: el caso 2 no cuadra (neto %s)' % neto)
    # calendario: B, D y F fijados en las 17 filas; cronológico hasta la fila 16 (después, «Varies»)
    for fila in FILAS_CALENDARIO:
        for col in 'BDF':
            if (HOJA_CAL[0], HOJA_CAL[1], '%s%d' % (col, fila)) not in POR_CELDA:
                err.append('calendario: %s%d sin texto fijado' % (col, fila))
    meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    orden = []
    for fila in range(4, 16):
        t = CALENDARIO[fila][0]
        m = next((i for i, x in enumerate(meses) if t.startswith(x) or (' ' + x) in t[:6]), None)
        if m is None:
            m = {'2nd Sunday in May': 4, 'December': 11, 'Day after Thanksgiving': 10}.get(t)
        orden.append(m)
    if None in orden or orden != sorted(orden):
        err.append('calendario B02: las filas 4-15 no van en orden cronológico (%r)' % orden)
    for k in CF_POR_CELDA:
        if k[:2] not in {(c, h) for c, hs in HOJAS_ES_POR_LIBRO.items() for h in hs}:
            err.append('CF_POR_CELDA en una hoja que no existe: %r' % (k,))
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
    if len(censo['libros']) != N_LIBROS:
        err.append('el censo trae %d libros, no %d' % (len(censo['libros']), N_LIBROS))
    cfs = {(info['corto'], h, cf['sqref']): cf['formula'] for info in censo['libros'].values()
           for h, hd in info['hojas_detalle'].items() for cf in hd['cf']}
    for k, (es, en) in CF_POR_CELDA.items():
        if cfs.get(k) != [es]:
            err.append('CF_POR_CELDA %r: el ES trae %r, no %r' % (k, cfs.get(k), es))
    # todo texto ES con °C tiene su °F fijado (POR_CELDA/GLOSARIO/CLAVES) o un ADAPTAR que lo da
    for k, t in tx.items():
        if '°C' in t and k not in CELSIUS_SIN_F:
            dic = POR_CELDA.get(k) or ADAPTAR.get(k) or GLOSARIO.get(t) or ''
            if '°F' not in dic:
                err.append('°C del ES sin °F en POR_CELDA/ADAPTAR/GLOSARIO: %r' % (k,))
    # las referencias del 10 y el 12 y las categorías: todas en GLOSARIO
    for (c, h, coord), t in tx.items():
        if (c, h) in (('10', 'Plan Semanal'), ('10', 'Producido vs Vendido'), ('12', 'Matriz Alérgenos')) and \
                re.match(r'[AB]\d+$', coord) and int(coord[1:]) >= 5 and coord[0] == ('B' if h == 'Producido vs Vendido'
                                                                                   else 'A'):
            if not t.startswith('  ') and t not in GLOSARIO and int(coord[1:]) < 52:
                err.append('referencia del %s sin GLOSARIO: %r (%s)' % (c, t, coord))
    # 12: las 14 cabeceras de alérgenos, en las mismas columnas de la matriz (C-P) y de la carta (B-O)
    al = ['Gluten', 'Crustáceos', 'Huevos', 'Pescado', 'Cacahuetes', 'Soja', 'Lácteos', 'Frutos de cáscara', 'Apio',
          'Mostaza', 'Sésamo', 'Sulfitos', 'Altramuces', 'Moluscos']
    for i, a in enumerate(al):
        if tx.get(('12', 'Matriz Alérgenos', '%s4' % chr(ord('C') + i))) != a:
            err.append('matriz: la columna %s ya no es %r' % (chr(ord('C') + i), a))
        if tx.get(('12', 'Carta de Alérgenos', '%s5' % chr(ord('B') + i))) != a:
            err.append('carta: la columna %s ya no es %r' % (chr(ord('B') + i), a))
        if tx.get(('12', 'Cartel Vitrina', 'B%d' % (12 + i))) != a:
            err.append('cartel: la fila %d ya no es %r' % (12 + i, a))
    # 09: los rótulos de denominación del ES en sus filas
    for f, es, _x, _en, _xen in DENOMINACIONES:
        if tx.get(('09', _HC, 'A%d' % f)) != es:
            err.append('09: A%d no es %r' % (f, es))
    # calendario: B, D, F con texto en el ES
    for fila in FILAS_CALENDARIO:
        for col in 'BDEF':
            if (HOJA_CAL[0], HOJA_CAL[1], '%s%d' % (col, fila)) not in tx:
                err.append('calendario: %s%d sin texto en el ES' % (col, fila))
    for k in ADAPTAR:
        if k not in tx:
            err.append('ADAPTAR %r sin texto en el ES' % (k,))
    return err


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
    for x in e:
        print('ERROR', x)
    print('mapas_pastry.py: {} ficheros · {} pestañas · {} glosario · {} claves · {} por celda · {} cf por celda · '
          '{} adaptar · {} reglas · {} errores'.format(len(FICHEROS), len(HOJAS), len(GLOSARIO), len(CLAVES),
                                                      len(POR_CELDA), len(CF_POR_CELDA), len(ADAPTAR), len(REGLAS_US),
                                                      len(e)))
    raise SystemExit(1 if e else 0)
