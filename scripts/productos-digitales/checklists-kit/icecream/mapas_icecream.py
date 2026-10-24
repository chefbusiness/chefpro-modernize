#!/usr/bin/env python3
"""
mapas_icecream.py — Ice Cream Shop Checklists Kit Pro (EN) · DELTA del Kit de Tareas Heladería
(`kit-tareas-heladeria`, 11 xlsx v2.0) sobre `mapas.py` (Restaurant Checklists Kit Pro). SPEC: `icecream/SPEC.md`
(solo el delta). Séptimo hermano vertical. Sesión Claude Code, 24-oct-2026.

Molde HÍBRIDO (lo mide el censo): el 01-07, el B01 y el B02 son el molde ligero del catering (# · Tarea · Zona ·
Responsable · ✓ · Hora · Notas; cabeceras internas por sección; contadores que restan «Tarea»; CF `$E6="✓"`; sin
protección; subtítulo A2 en vez de la línea de marca D19) y el 08 y el 09 son los del kit base (el 09, idéntico al base
salvo el nombre de la variante: su POR_CELDA y su ADAPTAR se heredan TAL CUAL, lo comprueba cruzar_base).

Se usa con `--kit icecream` (kit.py). Importa `mapas.py` y SOLO añade o sobrescribe: producto, ficheros, títulos,
pestañas (38), glosario (zonas de una heladería: obrador, pasteurizador, mantecadora, maduración, abatidor, vitrina,
mostrador; roles de una scoop shop US: shift lead, cashier), CLAVES (+ «Tarea»: los contadores la restan), CF_POR_CELDA
(las cabeceras internas no se pintan de verde, como el catering), calendario del BONUS-02 (otra estructura: 12 meses, A
mes · B acciones · C sabores · D temporada), POR_CELDA (caja 09 del base; 05 «Quarterly & Annual» de una heladería US;
el orden del cierre del 08; las horas del 08 y del 09, +3 h; la tabla de vida útil del 02), ADAPTAR y REGLAS_US
(temperaturas del helado en °F, pasteurización y licencia estatal, dipper well, alérgenos y contacto cruzado en el
scoop, etiqueta de los pints preenvasados, menores de edad en temporada). Las funciones del base que leen constantes
(titulo_interior, autotest, cruzar_censo) se re-enlazan a ESTE módulo. Ejecutado como script: autotest + cruce con
icecream/censo_es.json + cruce con el base (lo heredado por celda tiene el mismo texto ES).

    python3 icecream/mapas_icecream.py
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
AQUI = os.path.dirname(os.path.abspath(__file__))              # icecream/ (el import * trae el AQUI del base)

ORIGEN_ES = 'kit-tareas-heladeria'
PRODUCTO = 'Ice Cream Shop Checklists Kit Pro'
# D2: H1 = title SEO (74 caracteres); «ice cream shop» 246.000/mes US; «Production» = lo que ningún kit genérico trae
TITULO_SEO = 'Ice Cream Shop Checklists Kit Pro: Opening, Closing & Production Templates'
SLUG = 'ice-cream-shop-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
MARCA_ES = '— Kit de Tareas Recurrentes · Heladería Artesanal · AI Chef Pro · aichef.pro'
MARCA_EN = '— ' + PRODUCTO + ' · AI Chef Pro · aichef.pro'
VARIANTES_ES = ('Heladería Artesanal',)
# heredar.py: memoria con VARIAS fuentes, en orden de preferencia (gana la primera que acierta). La cafetería PRIMERO,
# incluso antes que el base (tienda con mostrador: «shift lead», «the WHOLE SHOP»; medido: 87 heredadas frente a 84 con
# el base delante y 86 con el catering, cuyo molde ligero apenas comparte textos con la heladería); luego el base, el
# catering, la pizzería, la hamburguesería, la ghost kitchen y el bar.
_SUF = lambda v: [(' — Heladería Artesanal', ' — ' + v), (' · Heladería Artesanal', ' · ' + v)]  # noqa: E731
MEMORIA = [('cafe', 'cafe', _SUF('Cafetería / Brunch')), ('base', '', _SUF('Restaurante Casual')),
           ('catering', 'catering', _SUF('Catering / Eventos')), ('pizza', 'pizza', _SUF('Pizzería')),
           ('burger', 'burger', _SUF('Hamburguesería')), ('ghost', 'ghost', _SUF('Dark Kitchen')),
           ('bar', 'bar', _SUF('Bar / Cocktails'))]
# heredar.py: EN heredado que en una heladería no vale tal cual → pendientes (motivo «contexto»). Una scoop shop es
# servicio de mostrador: sin sala con camareros, host stand, reservas, barra de copas, cocina de línea, commissary
# ni delivery-only.
# «server» SÍ vale (ice cream server), y «patio», «tip jar», «toppings bar» y «ice cream bars» también.
RX_CONTEXTO_PENDIENTE = (r'(?i)\b(?:dining rooms?|dine-in|FOH|host stands?|hostess|waitstaff|tables? service|'
                         r'reservations?|bartenders?|barbacks?|cocktails?|beer|liquor|wine|baristas?|coffee shops?|'
                         r'cafes?|bussers?|head chefs?|sous chefs?|line cooks?|prep cooks?|kitchen leads?|MOD|'
                         r'shift managers?|venues?|banquets?|BEOs?|line-up|pizzas?|pizzerias?|pizza dough|burgers?|grill|'
                         r'fryers?|ghost kitchens?|packers?|app managers?|commissar(?:y|ies)|restaurants?(?! consultant| supply))\b')
# heredar.py: cadenas idénticas a una fuente cuyo EN no vale en la heladería (→ pendientes → G1.json, con base_en)
NO_HEREDAR = {}
# gates_en.py G2: términos de otros kits que NINGUNA celda EN de la heladería puede llevar. «server», «patio», «tip
# jar», «toppings bar», «cookie dough», «venue» (el recinto del cliente en el catering) y «restaurant supply» quedan
# permitidos (y la firma «restaurant consultant»).
TERMINOS_PROHIBIDOS = (r'(?i:\b(?:dining rooms?|host stands?|hostess|waitstaff|table service|bartenders?|barbacks?|'
                       r'cocktails?|beer|liquor|baristas?|coffee shops?|cafes?|bussers?|head chefs?|sous chefs?|'
                       r'line cooks?|prep cooks?|banquets?|BEOs?|line-up|pizzas?|pizzerias?|burgers?|'
                       r'ghost kitchens?|packers?|app managers?|restaurants?(?! consultant| supply))\b)|\b(?:MOD|FOH)\b')
TERMINO_PROHIBIDO_EJEMPLO = 'Ask the bartender to seat the party in the dining room.'
REFERENCIAS_TRADUCTOR = ['icecream/SPEC.md', 'SPEC.md §0-§3 y §7.2 (brief)', 'textos_en/glosario.json (glosario de la '
                         'prosa del kit base)', 'icecream/textos_en/heredado.json (cómo se dijo ya cada cosa: base, '
                         'cafetería, catering, pizzería, hamburguesería, ghost kitchen y bar)', 'icecream/mapas_icecream.py: '
                         'GLOSARIO, HOJAS, FICHEROS, TITULOS, POR_CELDA, REGLAS_US', '../GLOSARIO-JERGA-ES-EN.md']
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v2.0'),
    ('keywords', 'ice cream shop checklist, ice cream shop opening checklist, ice cream parlor, scoop shop, gelato '
                 'shop, ice cream production, batch freezer, dipping cabinet, AI Chef Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

# ==========================================================================
# Ficheros (D5: «ice cream shop» 246.000/mes US, «ice cream parlor» 27.100, «gelato shop» 27.100, «scoop shop» 4.400,
# «ice cream catering» 1.600; las variantes con «checklist» sin volumen, como en los hermanos)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-apertura-cierre.xlsx', '01-ice-cream-shop-opening-closing-checklists.xlsx'),
    ('02-partidas-produccion.xlsx', '02-ice-cream-production-checklists.xlsx'),
    ('03-tareas-manager.xlsx', '03-ice-cream-shop-manager-checklist.xlsx'),
    ('04-tareas-perfiles.xlsx', '04-ice-cream-shop-duties-by-role.xlsx'),
    ('05-tareas-semanales-mensuales.xlsx', '05-ice-cream-shop-cleaning-checklist-maintenance.xlsx'),
    ('06-eventos-temporada.xlsx', '06-ice-cream-shop-seasonal-catering-checklists.xlsx'),
    ('07-plantilla-personalizable.xlsx', '07-blank-ice-cream-shop-checklist-template.xlsx'),
    ('08-apertura-cierre-negocio.xlsx', '08-ice-cream-parlor-opening-closing-checklist.xlsx'),
    ('09-apertura-cierre-caja.xlsx', '09-cash-drawer-opening-closing.xlsx'),
    ('BONUS-01-briefing-servicio.xlsx', 'BONUS-01-ice-cream-shop-pre-shift-meeting-template.xlsx'),
    ('BONUS-02-calendario-anual-tareas.xlsx', 'BONUS-02-ice-cream-shop-seasonal-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)
TITULOS = OrderedDict([
    ('01-ice-cream-shop-opening-closing-checklists.xlsx',
     'Ice Cream Shop Opening & Closing Checklists: Dipping Cabinets, Toppings & Counter'),
    ('02-ice-cream-production-checklists.xlsx',
     'Ice Cream & Gelato Production Checklists: Pasteurizing, Aging & Batch Freezing'),
    ('03-ice-cream-shop-manager-checklist.xlsx', 'Ice Cream Shop Manager Checklist: Daily, Weekly & Monthly'),
    ('04-ice-cream-shop-duties-by-role.xlsx',
     'Ice Cream Shop Duties by Role: Ice Cream Maker, Scooper & Shift Lead'),
    ('05-ice-cream-shop-cleaning-checklist-maintenance.xlsx',
     'Ice Cream Shop Cleaning Checklist & Maintenance Schedule'),
    ('06-ice-cream-shop-seasonal-catering-checklists.xlsx',
     'Ice Cream Shop Seasonal Checklists: Peak Season, Off-Season & Ice Cream Catering'),
    ('07-blank-ice-cream-shop-checklist-template.xlsx', 'Blank Ice Cream Shop Checklist Template (Editable)'),
    ('08-ice-cream-parlor-opening-closing-checklist.xlsx',
     'Ice Cream Parlor Opening & Closing Checklist (Whole Shop)'),
    ('09-cash-drawer-opening-closing.xlsx', 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log'),
    ('BONUS-01-ice-cream-shop-pre-shift-meeting-template.xlsx',
     'BONUS: Ice Cream Shop Pre-Shift Meeting Template (Huddle Notes)'),
    ('BONUS-02-ice-cream-shop-seasonal-calendar.xlsx',
     'BONUS: Ice Cream Shop Seasonal Calendar & Flavor Planner (US)'),
])
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

HOJAS = OrderedDict(_base.HOJAS)
HOJAS.update([
    ('Apertura', 'Opening'), ('Cierre', 'Closing'),
    ('Pasteurización', 'Pasteurizing'), ('Mantecación', 'Batch Freezing'),
    ('Tareas Diarias', 'Daily Tasks'), ('Tareas Semanales', 'Weekly Tasks'), ('Tareas Mensuales', 'Monthly Tasks'),
    ('Heladero-Obrador', 'Ice Cream Maker'), ('Dependiente-Mostrador', 'Scooper & Counter'),
    ('Encargado Turno', 'Shift Lead'),
    ('Gestión Semanal', 'Weekly Upkeep & Stock'),
    ('Temporada Alta', 'Peak Season'), ('Temporada Baja', 'Off-Season'), ('Catering Eventos', 'Ice Cream Catering'),
    ('Por Zona', 'By Area'), ('Por Turno', 'By Shift'),
    # 08: el «negocio» es la tienda (ni restaurante ni edificio)
    ('Apertura del Negocio', 'Shop Opening'), ('Cierre del Negocio', 'Shop Closing'),
    ('Briefing Diario', 'Pre-Shift Huddle'), ('Calendario Anual', 'Seasonal Calendar'),
])
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Apertura', 'Cierre']),
    ('02', ['Instrucciones', 'Pasteurización', 'Mantecación']),
    ('03', ['Instrucciones', 'Tareas Diarias', 'Tareas Semanales', 'Tareas Mensuales']),
    ('04', ['Instrucciones', 'Heladero-Obrador', 'Dependiente-Mostrador', 'Encargado Turno']),
    ('05', ['Instrucciones', 'Limpieza Semanal', 'Gestión Semanal', 'Tareas Mensuales', 'Trimestral y Anual']),
    ('06', ['Instrucciones', 'Temporada Alta', 'Temporada Baja', 'Catering Eventos']),
    ('07', ['Instrucciones', 'Por Zona', 'Por Turno', 'Por Perfil']),
    ('08', ['Instrucciones', 'Apertura del Negocio', 'Cierre del Negocio']),
    ('09', ['Instrucciones', 'Apertura de Caja', 'Cierre de Caja', 'Registro Mensual']),
    ('B01', ['Instrucciones', 'Briefing Diario']),
    ('B02', ['Instrucciones', 'Calendario Anual']),
])

# ==========================================================================
# GLOSARIO: el base entero (opcional) + celdas cortas de una heladería. Jerga US de scoop shop: dipping cabinet, batch
# freezer, aging (maduración), hardening (abatidor), scooper, shift lead, front counter.
# ==========================================================================
GLOSARIO = OrderedDict(_base.GLOSARIO)
_GLOSARIO_ICE = OrderedDict([
    # subtítulo de marca (A2) de las checklists del molde ligero: el producto EN, igual en todo el kit (como el catering)
    ('AI Chef Pro · aichef.pro — Kit de Tareas: Heladería Artesanal', 'AI Chef Pro · aichef.pro — ' + PRODUCTO),
    ('Hora', 'Time'), ('Mes', 'Month'), ('Temporada', 'Season'), ('Semestral', 'Semiannual'),
    # zonas (columna C); 2 sobrescriben el base: Sala (FOH) y Recepción (Host stand)
    ('Obrador', 'Production'), ('Pasteurizador', 'Pasteurizer'), ('Mantecadora', 'Batch freezer'),
    ('Maduración', 'Aging'), ('Abatidor', 'Hardening'), ('Cámara', 'Freezer'), ('Vitrina', 'Dipping cabinet'),
    ('Mostrador', 'Counter'), ('Almacén', 'Storage'), ('Equipo', 'Team'), ('RRSS', 'Social media'),
    ('Logística', 'Logistics'), ('Tienda', 'Shop'), ('Sala', 'Seating area'), ('Recepción', 'Front counter'),
    # puestos (08 y 09); 2 sobrescriben el base: Encargado (Shift manager) y Responsable de caja (Cashier / MOD)
    ('Encargado', 'Shift lead'), ('Responsable de caja', 'Cashier / shift lead'),
    # tabla de vida útil del 02 (la del base dice «Freezer time»: aquí hay frío y congelación)
    ('Vida útil', 'Shelf life'),
])
GLOSARIO.update(_GLOSARIO_ICE)
GLOSARIO_OPCIONAL = frozenset(_base.GLOSARIO)
PUESTOS_ES = frozenset(_base.PUESTOS_ES | {'Obrador', 'Pasteurizador', 'Mantecadora', 'Maduración', 'Abatidor',
                                           'Cámara', 'Vitrina', 'Mostrador', 'Almacén', 'Equipo', 'RRSS',
                                           'Logística', 'Tienda'})

# ==========================================================================
# CLAVES: «Tarea» (los contadores del 01-07 y del B01 restan las cabeceras internas, como el catering)
# ==========================================================================
CLAVES = OrderedDict(_base.CLAVES)
CLAVES.update([('Tarea', 'Task')])

# ==========================================================================
# CF_POR_CELDA (desviación DECLARADA respecto del ES, la del catering ronda 1 M5; SPEC §1 D7): en las hojas con varias
# tablas, las cabeceras internas llevan «✓» en la columna E y la CF de «hecho» las pinta de verde. La EN excluye las
# filas cuyo B es la cabecera «Task» (los contadores ya las restan). El 07 (una sola cabecera, fuera del rango) no.
# ==========================================================================
_CF_HOJAS = [('01', 'Apertura', 'A6:G40'), ('01', 'Cierre', 'A6:G28'), ('02', 'Pasteurización', 'A6:G24'),
             ('02', 'Mantecación', 'A6:G25'), ('03', 'Tareas Diarias', 'A6:G24'), ('03', 'Tareas Semanales', 'A6:G22'),
             ('03', 'Tareas Mensuales', 'A6:G25'), ('04', 'Heladero-Obrador', 'A6:G25'),
             ('04', 'Dependiente-Mostrador', 'A6:G25'), ('04', 'Encargado Turno', 'A6:G24'),
             ('05', 'Limpieza Semanal', 'A6:G23'), ('05', 'Gestión Semanal', 'A6:G16'),
             ('05', 'Tareas Mensuales', 'A6:G23'), ('05', 'Trimestral y Anual', 'A6:G23'),
             ('06', 'Temporada Alta', 'A6:G19'), ('06', 'Temporada Baja', 'A6:G17'),
             ('06', 'Catering Eventos', 'A6:G30'), ('B01', 'Briefing Diario', 'A6:G24')]
CF_POR_CELDA = OrderedDict(((c, h, sq), ('$E6="✓"', 'AND($E6="✓",$B6<>"%s")' % CLAVES['Tarea']))
                           for c, h, sq in _CF_HOJAS)
# G3: libros cuyo ES no trae la línea de marca D19 (solo el 08 y el 09; los demás, el subtítulo A2), como el catering
LIBROS_SIN_MARCA = ('01', '02', '03', '04', '05', '06', '07', 'B01', 'B02')

# ==========================================================================
# BONUS-02 «Seasonal Calendar»: otra estructura (12 meses, filas 5-16: A mes · B acciones y fechas · C sabores · D
# temporada · E ✓ · F notas). A, C y D fijados; B = traductor con ADAPTAR (fechas y tareas US, en orden). Temporada
# US: alta de Memorial Day a Labor Day (junio-agosto); mayo y septiembre, «Shoulder» (el ES pone mayo en alta: en EE.
# UU. el pico empieza el último lunes de mayo); el invierno, baja. Sin alcohol (eggnog sin alcohol).
# fila → (mes EN, sabores EN, temporada EN, ADAPTAR de B)
# ==========================================================================
HOJA_CAL = ('B02', 'Calendario Anual')
FILAS_CALENDARIO = range(5, 17)
CALENDARIO = OrderedDict([
    (5, ('January', 'Chocolate, Cinnamon, Coffee, Peppermint', 'Low',
         'Sustituye a Reyes y al roscón. Temporada baja: carta reducida; tartas heladas y pints para cumpleaños; '
         'mantenimiento y recetas nuevas; si tu heladería es de temporada y está cerrada, es el mes de reformas, '
         'proveedores y presupuesto')),
    (6, ('February', 'Strawberry, Raspberry, Red Velvet, White Chocolate', 'Low',
         "Valentine's Day (14 de febrero): edición limitada (fresa, frambuesa, red velvet), tartas heladas en forma de "
         'corazón por encargo, con señal (deposit); desarrollar las recetas de primavera')),
    (7, ('March', 'Mint Chocolate Chip, Coffee, Vanilla, Lemon', 'Shoulder',
         "Sustituye a Semana Santa y al Día del Padre (en EE. UU. va en junio, fila 10). St. Patrick's Day (17 de "
         'marzo): menta (mint chip) y verde; muchas heladerías de temporada reabren: anuncia el día de apertura '
         '(Opening Day); preparar la temporada: stock, contratación y equipo')),
    (8, ('April', 'Strawberry, Lemon, Mango, Vanilla Bean', 'Shoulder',
         'Sustituye a las comuniones. Easter (fecha variable): sabores de primavera y tartas heladas por encargo; '
         'ampliar la carta con frutales; contratar y formar al equipo de verano (muchos son menores: horarios de la '
         'FLSA, hoja «Peak Season» del 06) y preparar el patio y su permiso')),
    (9, ('May', 'Strawberry, Pistachio, Mango, Raspberry', 'Shoulder',
         "Mother's Day (2.º domingo de mayo): tartas heladas por encargo, con señal y encargos cerrados 2 weeks out; "
         'graduaciones (mayo-junio): pedidos de grupo y catering; Memorial Day (último lunes): EMPIEZA la temporada '
         'alta: carta completa de 18-24 sabores, patio abierto y horario ampliado')),
    (10, ('June', 'Peach, Cherry, Cantaloupe, Coconut', 'Peak',
          "Sustituye a San Juan. Fin de curso y graduaciones; Father's Day (3.er domingo de junio): tartas heladas por "
          'encargo; Juneteenth (19 de junio, festivo federal): decide el horario; máxima producción y campaña en '
          'redes')),
    (11, ('July', 'Watermelon, Peach, Blueberry, Sorbets', 'Peak',
          'National Ice Cream Month (todo julio) y National Ice Cream Day (3.er domingo de julio): sabor o promoción '
          'del día, colas y refuerzo de personal; 4 de julio: horario del festivo y pedidos de grupo (sabores red, '
          'white & blue); máxima producción y horario ampliado')),
    (12, ('August', 'Peach, Blackberry, Lemonade Sorbet, Passion Fruit', 'Peak',
          'Sustituye a la Asunción (el 15 de agosto no es festivo en EE. UU.). Pico de temporada: stock +50 %; ferias '
          'y festivales de verano (county fairs) y catering de eventos; la vuelta al cole (mediados-finales de '
          'agosto) se lleva a parte del equipo joven: cierra los turnos de septiembre')),
    (13, ('September', 'Apple, Caramel, Maple, Coffee', 'Shoulder',
          'Labor Day (1.er lunes de septiembre): último gran fin de semana del verano; después, transición: reducir la '
          'carta poco a poco y promociones para familias (back to school); muchas heladerías de temporada cierran '
          'tras Labor Day o en octubre')),
    (14, ('October', 'Pumpkin, Apple Cider, Caramel, Chocolate', 'Low',
          'Halloween (31 de octubre): sabores temáticos (pumpkin, caramel apple) y toppings de temporada; reducir la '
          'carta a 10-14 sabores; si cierras por temporada: fecha de cierre, aviso a clientes y equipo')),
    (15, ('November', 'Pumpkin Pie, Pecan, Maple, Cinnamon', 'Low',
          'Sustituye a Todos los Santos. Thanksgiving (4.º jueves de noviembre): helado para acompañar las tartas (pie '
          'à la mode), pints y quarts por encargo; decidir el horario (muchos cierran); Black Friday y Small Business '
          'Saturday: tarjetas regalo (gift cards); mantenimiento')),
    (16, ('December', 'Peppermint, Eggnog, Gingerbread, Cinnamon', 'Low',
          'Sustituye al puente de la Constitución. Fiestas (holidays): peppermint, eggnog (sin alcohol) y gingerbread; '
          'tartas heladas y pints de regalo, tarjetas regalo y catering de empresas; Navidad (25) y Nochevieja (31): '
          'decidir el horario. Sin turrón, polvorón, mazapán ni alcohol')),
])

# ==========================================================================
# POR_CELDA: lo heredado del base (el 09 entero; mismo texto ES, lo comprueba cruzar_base) + lo de la heladería
# ==========================================================================
_HEREDA_POR_CELDA = [k for k in _base.POR_CELDA if k[0] == '09']
POR_CELDA = OrderedDict((k, _base.POR_CELDA[k]) for k in _HEREDA_POR_CELDA)
_T = ('05', 'Trimestral y Anual')
POR_CELDA.update([
    # 03 · conservación de fichajes (B16 del base: mismo EN, FLSA)
    (('03', 'Tareas Mensuales', 'B15'), _base.POR_CELDA[('03', 'Mensual Manager', 'B16')]),
    # 02 · Mantecación: tabla de vida útil (criterio del kit, en °F)
    (('02', 'Mantecación', 'C31'), '2–3 months at 0 °F'), (('02', 'Mantecación', 'C32'), '3–5 days at 36–39 °F'),
    (('02', 'Mantecación', 'C33'), '1 month at 0 °F'), (('02', 'Mantecación', 'C34'), '6–12 months at 0 °F'),
    (('02', 'Mantecación', 'C35'), '6 months at 0 °F · 2–3 months refrigerated'),
    (('02', 'Mantecación', 'C36'), "Per the manufacturer's label"),
    # 05 · Trimestral y Anual: servicios contratados y papeles de una heladería US (sin DDD, BIE, gases fluorados,
    # legionela ni facturación verificable)
    (_T + ('A4',), 'Contracted services — quarterly & semiannual'),
    (_T + ('B6',), 'Pest control by a licensed operator: service visit and signed service report on file (write the '
                   'report # in the Notes column)'),
    (_T + ('F6',), 'Monthly'),
    (_T + ('B7',), 'Exhaust hood and ducts: if you cook with grease (waffle irons, crepes) under a hood, cleaning by a '
                   'certified contractor per NFPA 96; a steam-only hood over the pasteurizer, as its manufacturer says'),
    (_T + ('F7',), 'Semiannual'),
    (_T + ('B8',), 'Refrigeration service by an EPA 608-certified tech: walk-in and reach-in freezers, dipping cabinets, '
                   'batch freezer and blast freezer — coils, gaskets and refrigerant leak check'),
    (_T + ('B9',), 'Calibration check of the dipping cabinet, freezer and pasteurizer thermometers against a reference '
                   'thermometer; if your state licenses your pasteurizer, its recording thermometer is checked as that '
                   'license requires'),
    (_T + ('A11',), 'Annual — fire, gas & water safety'),
    (_T + ('B13',), 'Annual extinguisher maintenance by a licensed fire protection company: new tag and record (OSHA '
                    '1910.157); hydrostatic tests as the label says (OSHA 1910.157(f))'),
    (_T + ('B14',), 'Gas lines and appliance connections (waffle iron, crepe griddle, water heater) checked by a '
                    'licensed pro if you have gas, and the electrical system, as often as your local code requires'),
    (_T + ('B15',), 'Backflow preventers tested by a certified tester where your water utility requires it (most do, '
                    'yearly): dipper wells, ice machine and espresso machine all hook up to the water supply'),
    (_T + ('A17',), 'Annual — permits, training, insurance & systems'),
    (_T + ('B19',), 'Check your health permit is current and posted — and, if you make your own ice cream or '
                    'pasteurize your own mix, your state frozen dessert / dairy license too'),
    (_T + ('B20',), 'Review food handler cards and allergen training for ALL staff, summer hires included, and that a '
                    'certified food protection manager is on the team (FDA Food Code 2-102.12)'),
    (_T + ('B21',), "Renew insurance and review coverage: general liability, property, workers' comp and equipment "
                    'breakdown with food spoilage — a freezer down in July can take the whole season with it'),
    (_T + ('B22',), 'POS check before year-end: software updates, sales tax rates and settings, user permissions'),
    (_T + ('B23',), "File the year's temperature, cleaning and batch logs, and update your food safety plan when you "
                    'change equipment, recipes or suppliers'),
])
# 08 · Cierre (errata ES): cubrir las vitrinas y registrar las temperaturas de cierre iba DESPUÉS de la alarma y la
# llave, y las persianas se cerraban antes de recoger la señalización y vaciar papeleras. Toda la secuencia, mismas 15
# filas (E = «Close»): clientes y música → patio y señalización → vitrinas y temperaturas → caja → papeleras y
# seguridad → el local → alarma, puertas y llave al final
_CN = ('08', 'Cierre del Negocio')
_CIERRE_08 = [  # fila ES de origen, EN, zona EN, responsable EN
    (6, 'Check no customers are left in the shop', 'Seating area', 'Shift lead'),
    (5, 'Turn off background music', 'General', 'Shift lead'),
    (7, 'Clean up and bring in the patio, if you have one', 'Patio', 'Shift lead'),
    (12, 'Bring in the outdoor signage and sidewalk sign', 'Outside', 'Shift lead'),
    (18, 'Put the night covers on the dipping cabinets: they stay ON, in storage mode', 'Shop', 'Shift lead'),
    (19, 'Log the closing temps: dipping cabinets already in storage mode (0 °F) and freezers (0 °F or below) — log '
         'reading: ____ °F', 'Shop', 'Shift lead'),
    (8, 'Turn off the POS / card terminal (or leave on standby)', 'Register', 'Shift lead'),
    (14, 'Empty trash cans in common areas and restrooms', 'Restrooms', 'Shift lead'),
    (15, 'Final safety check: gas off, water off, small appliances unplugged — never the freezers or dipping cabinets',
     'General', 'Shift lead'),
    (13, 'Check that windows are closed', 'General', 'Shift lead'),
    (11, 'Turn off HVAC', 'General', 'Shift lead'),
    (10, 'Turn off lights (leave security lighting on)', 'General', 'Shift lead'),
    (16, 'Set the alarm', 'Entrance', 'Last one out'),
    (9, 'Close security gate and doors', 'Entrance', 'Last one out'),
    (17, 'Lock up and verify it is locked', 'Entrance', 'Last one out'),
]
# responsable que cambia (declarado): vitrinas y temperaturas (ES «Último en salir») → el shift lead; alarma y
# persianas (ES «Encargado») → el último en salir, con la llave
_RESPONSABLE_CAMBIA = frozenset({18, 19, 16, 9})
for _fila, (_o, _b, _c, _d) in enumerate(_CIERRE_08, 5):
    for _col, _v in (('B', _b), ('C', _c), ('D', _d)):
        POR_CELDA[_CN + ('%s%d' % (_col, _fila),)] = _v
# 08 y 09 · horas (D9, criterio del kit): una scoop shop US abre a media mañana (11 AM - mediodía), no a las 8:
# todas las horas límite del 08 «Apertura» y del 09 «Apertura de Caja» suben 3 h (07:00 → 10:00 AM), mismo orden y
# mismos intervalos; la puerta abre a las 11:00 AM. Fila → hora ES (la comprueba cruzar_censo)
_AN = ('08', 'Apertura del Negocio')
_AC9 = ('09', 'Apertura de Caja')
HORAS_ES = OrderedDict([(_AN + ('E%d' % f,), h) for f, h in zip(range(5, 23), ['07:00'] * 6 + ['07:15'] * 6
                                                                  + ['07:30'] * 6)]
                       + [(_AC9 + ('D%d' % f,), h) for f, h in zip(range(5, 16), ['07:15'] * 4 + ['07:30'] * 4
                                                                    + ['07:45'] * 3)])
DESPLAZAMIENTO_H = 3


def _mas(h, horas=DESPLAZAMIENTO_H):
    hh, mm = h.split(':')
    return hora_us('%02d:%s' % (int(hh) + horas, mm))


for _k, _h in HORAS_ES.items():
    POR_CELDA[_k] = _mas(_h)
# 08 · Apertura B20-B21 (errata ES: las mantecadoras no se encienden al abrir, solo para mantecar: hoja «Batch
# Freezing» del 02) y la cita del 01, que el ES escribe sin «.xlsx»: fijadas aquí con la cita corta «file 01»
POR_CELDA[_AN + ('B20',)] = ('Dipping cabinets switched to service mode — they stay on overnight with product inside '
                             '(details in file 01, Opening tab)')
POR_CELDA[_AN + ('B21',)] = 'Dipping cabinets at serving temp (6–10 °F; reading logged in file 01, Opening tab)'
for _fila, (_mes, _sabores, _temp, _dir) in CALENDARIO.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'A%d' % _fila)] = _mes
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'C%d' % _fila)] = _sabores
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'D%d' % _fila)] = _temp
VALORES_EN = OrderedDict()             # sin inventario con mínimos en el ES heladería (nada numérico cambia)

# ==========================================================================
# ADAPTAR (en español, con el dato US; las cifras y normas salen de REGLAS_US)
# ==========================================================================
_A = _base.ADAPTAR
_HACCP_KIT = _base._HACCP_KIT
_LAVADO = _A[('02', 'Fríos', 'B6')]
_TIRA = 'sanitizante aprobado a la concentración de la etiqueta, medida con tira (test strip) (FDA Food Code 4-501.114)'
_LOG = 'coletilla «— log reading: ____ °F»'
_TEMPS = ('Temperaturas US del kit: conservación a 0 °F o menos (ES −18 °C); servicio en la vitrina (dipping cabinet) a '
          '6–10 °F (ES −14 a −12 °C; fabricante); maduración de la mezcla (aging) a 36–39 °F y nunca por encima de '
          '41 °F (ES 2-4 °C; FDA Food Code 3-501.16)')
_ALERGENOS = ('Alérgenos US: los 9 principales (FALCPA + FASTER Act): leche, huevo, frutos de cáscara (pistacho, '
              'avellana, almendra), cacahuete, trigo (cucuruchos, barquillos y galletas), soja y sésamo, además de '
              'pescado y crustáceos; los sulfitos no son uno de los 9 (si los usas, déjalos en tu carta); en UK, los '
              '14. El gluten se dice «wheat» (el trigo es el alérgeno)')
_SCOOP = ('Práctica US: el scoop, entre bola y bola, en el dipper well de agua corriente (FDA Food Code 3-304.12) o '
          'un scoop por sabor; el agua corriente NO quita los alérgenos: para un pedido con alergia, manos lavadas, '
          'guantes nuevos, scoop limpio y sanitizado y, si se puede, una cubeta que no haya tocado otro scoop (criterio '
          'del kit)')
_SALSAS = ('Salsas y toppings como diga su etiqueta (fabricante); lo lácteo abierto (dulce de leche, nata montada) y la '
           'fruta cortada, tapados y a 41 °F o menos (FDA Food Code 3-501.16); el hot fudge, en su calentador según el '
           'fabricante')
_ENFRIAR_MEZCLA = ('La mezcla pasteurizada es TCS: enfriarla de 135 °F a 70 °F en 2 h y a 41 °F o menos en 4 h más '
                   '(FDA Food Code 3-501.14); el ciclo de enfriamiento del pasteurizador suele hacerlo mucho antes '
                   '(fabricante)')
_LICENCIA = ('pasteurizar la mezcla propia suele exigir una licencia ESTATAL de fabricante de frozen dessert o de lácteos '
             '(Vermont, Georgia, Arizona…) y algunos estados la piden incluso para mantecar una mezcla ya pasteurizada o '
             'tener una máquina de soft serve (Vermont, Massachusetts); con mezcla comprada ya pasteurizada suele '
             'bastar el health permit: compruébalo con el departamento de agricultura de tu estado')
_PASTEURIZAR = ('Cifra del kit en °F: 185 °F durante 15 s (ES 85 °C 15 s, alta pasteurización); añade, breve, que '
                'mandan el programa validado de tu pasteurizador y el mínimo de tu licencia estatal (la nota de la '
                'licencia va en «Instructions» B6)')
_NORMA = ('el helado («ice cream») tiene que pesar al menos 4,5 lb por galón (21 CFR 135.110): un overrun demasiado '
          'alto lo deja fuera de la norma; el gelato no tiene norma federal')
_EMPAQUE = ('Envases para llevar US: pints y quarts (al peso, solo con una báscula legal para el comercio, '
            'legal-for-trade, que revisa la oficina estatal de pesas y medidas); los pints que se envasan antes para el '
            'congelador de autoservicio llevan etiqueta con nombre, ingredientes y alérgenos principales (FDA Food Code '
            '3-602.11); los que se llenan al momento para el cliente, no')
_MENORES = ('añade: en verano muchos son menores: con 14-15 años, horario limitado por la FLSA (29 CFR 570.35: fuera del '
            'horario escolar, hasta las 7 PM y hasta las 9 PM del 1 de junio al Labor Day, con máximos por día y por '
            'semana) y solo los equipos que permite 29 CFR 570.34; el permiso de trabajo (work permit), según el estado')
_PROBAR = 'Probar con una cuchara limpia cada vez, nunca la misma dos veces (FDA Food Code 3-301.12)'
_RESENAS = 'Plataformas US: Google Business Profile y Yelp'
_SEGURIDAD = ('APPCC → seguridad alimentaria (food safety): los registros de temperatura, limpieza y lotes; un plan '
              'HACCP solo si tu licencia estatal o una varianza lo exige')
ADAPTAR = OrderedDict([
    # 01 · Instrucciones
    (('01', 'Instrucciones', 'B12'), 'A4 → US Letter'),
    (('01', 'Instrucciones', 'B16'), _TEMPS + '. Las vitrinas NO se apagan por la noche: pasan a conservación'),
    (('01', 'Instrucciones', 'B17'), 'Scoop (porcionador) y dipper well: ' + _SCOOP + '. ' + _ALERGENOS + '. Sin «de '
     'declaración obligatoria»: en EE. UU. la etiqueta es para lo envasado (FDA Food Code 3-602.11)'),
    # 01 · Apertura
    (('01', 'Apertura', 'B7'), _A[('01', 'Apertura Cocina', 'B7')] + '; y sin tocar con la mano desnuda lo listo para '
     'consumir: cucuruchos por el envoltorio o con servilleta o guantes, toppings con utensilio (FDA Food Code '
     '3-301.11)'),
    (('01', 'Apertura', 'B9'), _A[('01', 'Apertura Cocina', 'B9')]),
    (('01', 'Apertura', 'B10'), _A[('01', 'Apertura Cocina', 'B10')]),
    (('01', 'Apertura', 'B12'), _A[('01', 'Apertura Cocina', 'B14')]),
    (('01', 'Apertura', 'B16'), 'Vitrinas → dipping cabinets: de modo conservación (0 °F) a modo servicio (6–10 °F; '
     'fabricante); ' + _LOG),
    (('01', 'Apertura', 'B17'), 'Cámaras de conservación → walk-in / reach-in freezers a 0 °F o menos; ' + _LOG),
    (('01', 'Apertura', 'B18'), 'Cámara de maduración → aging cooler (o tanque de maduración) a 36–39 °F; por encima de '
     '41 °F la mezcla pasteurizada deja de estar segura (FDA Food Code 3-501.16); ' + _LOG),
    (('01', 'Apertura', 'B19'), 'Abatidor de temperatura → blast freezer / hardening cabinet'),
    (('01', 'Apertura', 'B21'), _HACCP_KIT + '; lectura en °F'),
    (('01', 'Apertura', 'B25'), _LAVADO + '; frutos secos y virutas (sprinkles), en recipiente cerrado'),
    (('01', 'Apertura', 'B26'), _SCOOP),
    (('01', 'Apertura', 'B27'), _ALERGENOS + '; «carta de alérgenos» → allergen chart'),
    (('01', 'Apertura', 'B28'), _SALSAS),
    # 01 · Cierre
    (('01', 'Cierre', 'B7'), 'Modo conservación a 0 °F (ES −18 °C): con producto dentro no se apagan'),
    (('01', 'Cierre', 'B8'), 'Mermas → waste log: sabor, cantidad (lb o cubetas) y motivo'),
    (('01', 'Cierre', 'B14'), 'Limpiar y luego sanitizar con ' + _TIRA),
    (('01', 'Cierre', 'B16'), 'Scoops y espátulas: lavar, aclarar y sanitizar con ' + _TIRA + '; añade: vaciar, '
     'frotar y sanitizar el dipper well'),
    (('01', 'Cierre', 'B17'), 'Mostrador, báscula y zona de cobro: limpiar y luego sanitizar con ' + _TIRA),
    # 02 · producción
    (('02', 'Instrucciones', 'B16'), 'La mezcla base pasteurizada NO se congela: se madura a 36–39 °F (nunca por encima '
     'de 41 °F) y se manteca en 3-5 días (criterio del kit, dentro de los 7 del date marking de la FDA, 3-501.17); lo '
     'que se congela es el helado terminado, a 0 °F o menos'),
    (('02', 'Instrucciones', 'B6'), 'Añade al final una nota corta del kit: ' + _LICENCIA),
    (('02', 'Pasteurización', 'B13'), _PASTEURIZAR),
    (('02', 'Pasteurización', 'B14'), '40-50 °C → 104–122 °F'),
    (('02', 'Pasteurización', 'B15'), _ENFRIAR_MEZCLA),
    (('02', 'Pasteurización', 'B16'), 'Temperatura final de la mezcla: 41 °F o menos (lo ideal, 36–39 °F)'),
    (('02', 'Pasteurización', 'B22'), 'Maduración (aging): mínimo 4 h, lo óptimo 8-12 h, a 36–39 °F (criterio del kit)'),
    (('02', 'Pasteurización', 'B23'), 'Limpiar y luego sanitizar el pasteurizador tras cada uso, como diga su '
     'fabricante; ' + _TIRA),
    (('02', 'Mantecación', 'B8'), 'Temperatura de extracción (draw temperature) según el fabricante de la mantecadora '
     '(batch freezer): helado 16–19 °F | sorbete 10–14 °F (ES −7/−9 °C y −10/−12 °C)'),
    (('02', 'Mantecación', 'B9'), 'Cubetas (pans) pre-enfriadas en el congelador a −4 °F (ES −20 °C)'),
    (('02', 'Mantecación', 'B17'), 'Pesar la cubeta y anotar rendimiento y overrun; añade: ' + _NORMA),
    (('02', 'Mantecación', 'B21'), 'Endurecer (harden) la cubeta a 0 °F o menos en el abatidor (blast freezer / '
     'hardening cabinet)'),
    (('02', 'Mantecación', 'B22'), 'Al congelador de conservación, de 0 °F a −4 °F (ES −18/−20 °C)'),
    (('02', 'Mantecación', 'B24'), 'Desmontar y limpiar la mantecadora como diga su fabricante (cuchillas / dasher, '
     'junta y cilindro) y luego sanitizarla'),
    (('02', 'Mantecación', 'B25'), 'Superficies del obrador y utensilios: limpiar y luego sanitizar con ' + _TIRA),
    # 03
    (('03', 'Instrucciones', 'B15'), 'Registro de jornada US: la FLSA obliga a registrar con exactitud las horas '
     'trabajadas del personal por horas (non-exempt), temporada incluida (29 CFR 516.2); sin RD-ley 8/2019'),
    (('03', 'Instrucciones', 'B16'), 'Conservación US: fichajes 2 años y nóminas 3 (29 CFR 516.5-516.6; algunos estados '
     'piden más, p. ej. NY 6), a disposición del Department of Labor; sin «Inspección de Trabajo» ni «representantes de '
     'los trabajadores»'),
    (('03', 'Tareas Diarias', 'B8'), 'Registros de temperatura APPCC → los registros de temperatura del turno anterior '
     '(temperature logs, en °F)'),
    (('03', 'Tareas Diarias', 'B17'), _A[('03', 'Diario Manager', 'B35')] + '; temporada y menores incluidos; sin '
     'RD-ley 8/2019'),
    (('03', 'Tareas Diarias', 'B23'), _PROBAR),
    (('03', 'Tareas Diarias', 'B24'), _RESENAS),
    (('03', 'Tareas Mensuales', 'B23'), _RESENAS),
    (('03', 'Tareas Mensuales', 'B25'), _SEGURIDAD),
    # 04 · perfiles
    (('04', 'Heladero-Obrador', 'B21'), 'Mantecadora: desmontar, limpiar y sanitizar (cuchillas y junta) como diga su '
     'fabricante'),
    (('04', 'Heladero-Obrador', 'B23'), 'Superficies, balanzas y utensilios: limpiar y luego sanitizar con ' + _TIRA),
    (('04', 'Dependiente-Mostrador', 'B13'), 'Añade: las muestras (samples), con cucharilla de un solo uso (tasting '
     'spoon) que nunca vuelve a la cubeta (criterio del kit)'),
    (('04', 'Dependiente-Mostrador', 'B23'), 'Lo perecedero, tapado y a 41 °F o menos (FDA Food Code 3-501.16); lo seco, '
     'en recipiente cerrado'),
    (('04', 'Encargado Turno', 'B9'), 'Temperaturas de vitrinas (6–10 °F) y congeladores (0 °F o menos) en el registro '
     '(temperature log)'),
    (('04', 'Encargado Turno', 'B15'), 'Vitrinas a 6–10 °F durante el servicio (fabricante)'),
    # 05
    (('05', 'Instrucciones', 'B6'), 'APPCC → seguridad alimentaria (food safety)'),
    (('05', 'Instrucciones', 'B14'), 'Describe la lista US de la hoja «Quarterly & Annual»: control de plagas, campana y '
     'conductos (si se cocina con grasa, NFPA 96), frío (EPA 608), calibración de termómetros, extintores (OSHA), gas, '
     'backflow, health permit y licencia estatal de frozen dessert si fabricas, food handler cards y alérgenos, seguros '
     '(con la pérdida de género por avería del frío) y POS / sales tax. Sin DDD, BIE, gases fluorados, legionela ni '
     'facturación española'),
    (('05', 'Instrucciones', 'B15'), '«Cadencia» → "Frequency"; el nº de parte → el número del informe de servicio '
     '(service report #), en "Notes": sin el informe firmado, la tarea no está hecha a efectos de inspección'),
    (('05', 'Instrucciones', 'B16'), 'Seguro US: equipment breakdown con cobertura de género estropeado (food spoilage): '
     'la que responde cuando un congelador se para en julio'),
    (('05', 'Limpieza Semanal', 'B8'), 'Dispensadores de salsas y toppings: desmontar, lavar, aclarar y sanitizar con '
     + _TIRA),
    (('05', 'Limpieza Semanal', 'B17'), 'Máquina de hielo: limpieza y desinfección como diga su fabricante'),
    (('05', 'Gestión Semanal', 'B7'), 'Errata ES: el personal no toca el refrigerante (solo un técnico certificado EPA '
     '608, hoja «Quarterly & Annual»): el equipo comprueba que cada equipo de frío mantiene su temperatura, sin escarcha '
     'ni ruidos raros, y si no, avisa al técnico'),
    (('05', 'Gestión Semanal', 'B8'), 'Báscula: comprobación con pesas patrón; si vendes al peso, la báscula tiene que '
     'ser legal para el comercio (legal-for-trade, NTEP) y la revisa la oficina de pesas y medidas de tu estado'),
    (('05', 'Tareas Mensuales', 'B6'), 'Termómetros de sonda: comprobación en agua con hielo (32 °F); los de vitrinas y '
     'congeladores, contra uno de referencia'),
    (('05', 'Tareas Mensuales', 'B20'), _SEGURIDAD),
    (('05', 'Tareas Mensuales', 'B21'), 'Alérgenos: etiquetas de los pints preenvasados (FDA Food Code 3-602.11) y la '
     'carta de alérgenos al día con las recetas (los 9 de EE. UU.)'),
    # 06
    (('06', 'Instrucciones', 'B6'), 'Temporada alta US: de Memorial Day (último lunes de mayo) a Labor Day (primer lunes '
     'de septiembre); la primavera es la pretemporada'),
    (('06', 'Temporada Alta', 'A12'), 'Mayo-septiembre → «Memorial Day–Labor Day»'),
    (('06', 'Temporada Alta', 'B7'), 'Reforzar el equipo: contratar 2 semanas antes; ' + _MENORES),
    (('06', 'Temporada Alta', 'B15'), 'Terraza → patio, con el permiso de la ciudad si lo pide (outdoor seating / '
     'patio permit)'),
    (('06', 'Temporada Alta', 'B16'), '2 dependientes → 2 scoopers como mínimo'),
    (('06', 'Temporada Alta', 'B18'), _EMPAQUE),
    (('06', 'Temporada Baja', 'B6'), 'Carta de invierno US: 10-14 sabores (chocolate, peppermint, eggnog sin alcohol, '
     'canela, pumpkin); sin turrón'),
    (('06', 'Temporada Baja', 'B7'), 'Complementos: chocolate caliente, gofres (waffles), crepes y tartas heladas (ice '
     'cream cakes) para cumpleaños y fiestas'),
    (('06', 'Catering Eventos', 'B6'), _ALERGENOS),
    (('06', 'Catering Eventos', 'B7'), 'Añade: en un evento público, el permiso temporal del condado (temporary food '
     'establishment permit) si lo pide, y agua para lavarse las manos en el puesto (norma local)'),
    (('06', 'Catering Eventos', 'B8'), 'Señal → deposit; precio por persona (o por pint / galón)'),
    (('06', 'Catering Eventos', 'B10'), 'Hueco en el congelador a 0 °F o menos'),
    (('06', 'Catering Eventos', 'B16'), 'Producir 24-48 h antes y guardar a 0 °F o menos'),
    (('06', 'Catering Eventos', 'B21'), 'Cadena de frío: cajas isotérmicas (insulated carriers) y hielo seco (dry ice: '
     'con guantes, sin tocar el helado y con el vehículo ventilado; criterio del kit)'),
    (('06', 'Catering Eventos', 'B23'), 'A la llegada, 10 °F o menos (ES −12 °C); ' + _LOG),
    # 07
    (('07', 'Instrucciones', 'B13'), 'A4 → US Letter'),
    # 08 (el cierre reordenado y las horas van por POR_CELDA)
    (('08', 'Apertura del Negocio', 'B8'), _A[('08', 'Apertura del Negocio', 'B8')]),
    (('08', 'Apertura del Negocio', 'B11'), 'Una heladería no reserva: «Turn on the online-order tablet (pickup and '
     'delivery apps), if you use one»'),
    (('08', 'Apertura del Negocio', 'B13'), 'Reservas → los encargos del día (tartas heladas, pints por encargo, '
     'catering) y los eventos especiales'),
    (('08', 'Apertura del Negocio', 'B17'), 'Terraza → patio (mesas, sillas, sombrillas o estufas de exterior / patio '
     'heaters)'),
    (('08', 'Apertura del Negocio', 'B18'), 'Cartas → menu boards y lista de sabores'),
    # BONUS-02
    (('B02', 'Instrucciones', 'B15'), "Fechas US del calendario: Valentine's Day, St. Patrick's Day, Easter, Mother's "
     "Day (2.º domingo de mayo), Memorial Day–Labor Day, Father's Day (3.er domingo de junio), 4 de julio, National Ice "
     'Cream Month (julio) y National Ice Cream Day (3.er domingo de julio), Halloween, Thanksgiving (4.º jueves de '
     'noviembre) y las fiestas de diciembre. Sin fechas españolas'),
    (('B02', 'Instrucciones', 'B16'), 'Fiestas patronales → las fiestas de tu ciudad (county fair, festivales de verano, '
     'partidos del instituto); añade la nota UK: Mothering Sunday (marzo), bank holidays y Boxing Day'),
])
# 09 (idéntico al base salvo la variante): el ADAPTAR del base, tal cual
_HEREDA_ADAPTAR = [k for k in _A if k[0] == '09']
for _k in _HEREDA_ADAPTAR:
    ADAPTAR[_k] = _A[_k]
for _fila, (_mes, _sabores, _temp, _dir) in CALENDARIO.items():
    ADAPTAR[(HOJA_CAL[0], HOJA_CAL[1], 'B%d' % _fila)] = 'Mes EN: «%s». %s' % (_mes, _dir)
# aplicar_en.objetivo_ajuste / G3 (como la pizzería, la hamburguesería y la ghost kitchen): la EN activa el ajuste
# también donde el ES no cabía
AJUSTE_MAQUETA_ES = True
# F2: 02 «Mantecación» fila 35 (tabla de vida útil). En el ES la fila es automática y la crece C35 (3 líneas en la
# columna de 14); en la EN, `capa_ajuste` le pone 30 pt por la nota combinada de la D (2 líneas) y ese alto fijo corta
# C35 «6 months at 0 °F · 2–3 months refrigerated» (3 líneas = 45 pt)
ALTOS_FILA = {('02', 'Mantecación', 35): 45.0}
# Celdas ES con °C cuya EN NO lleva cifra: solo la fila 19 del cierre del 08 (sus temperaturas suben a la fila 10 con el
# reorden; en la 19 EN queda la llave). G7 la declara; el resto de °C del ES lleva su °F en la EN
CELSIUS_SIN_F = frozenset({('08', 'Cierre del Negocio', 'B19')})

# ==========================================================================
# REGLAS_US: las del base + las de la heladería (fuente única de las cifras y normas que el kit puede afirmar)
# ==========================================================================
REGLAS_US = OrderedDict(_base.REGLAS_US)
# Fuera las dos del base que una heladería no hace (SPEC §3: «sin recalentado: no aplica»; sin pescado crudo): así G7
# caza cualquier 165 °F o −31 °F que se cuele y las cifras permitidas = GRADOS_F_SPEC
for _k in ('parasitos', 'recalentado'):
    del REGLAS_US[_k]
REGLAS_US.update([
    ('helado_temps', ('conservación 0 °F o menos; vitrina 6–10 °F; maduración 36–39 °F (≤ 41 °F); extracción helado '
                      '16–19 °F / sorbete 10–14 °F; cubetas a −4 °F; llegada del catering ≤ 10 °F',
                      '[fabricante] dipping cabinet y batch freezer; [criterio del kit]; FDA Food Code 2022 §3-501.11 y '
                      '§3-501.16(A)(2)')),
    ('pasteurizacion', ('185 °F durante 15 s (cifra del kit, ES 85 °C); mínimos y registro, los de la licencia estatal '
                        'y el pasteurizador', '[criterio del kit]; [estatal] licencia de frozen dessert / dairy')),
    ('licencia_helado', ('fabricar o pasteurizar la mezcla propia: licencia estatal; con mezcla pasteurizada comprada '
                         'suele bastar el health permit; algunos estados licencian la mantecación y el soft serve',
                         '[estatal] Vermont Agency of Agriculture (Frozen Dessert / Milk Handlers License); '
                         'Massachusetts DPH (frozen dessert licensing); Arizona Dept. of Agriculture (frozen dessert; '
                         'exención de 2019); Ga. Comp. R. & Regs. 40-2-8-.01')),
    ('enfriar_mezcla', ('mezcla pasteurizada: 135 → 70 °F en 2 h y → 41 °F en 4 h más', 'FDA Food Code 2022 §3-501.14')),
    ('dipper_well', ('utensilios en pausa: en agua corriente que arrastre las partículas (dipper well, helado) o en agua '
                     'a 135 °F o más', 'FDA Food Code 2022 §3-304.12(D) y (F)')),
    ('mano_desnuda', ('sin contacto de la mano desnuda con lo listo para consumir', 'FDA Food Code 2022 §3-301.11')),
    ('catar', ('cuchara limpia cada vez que se prueba', 'FDA Food Code 2022 §3-301.12')),
    ('etiqueta_envasado', ('lo envasado en el local lleva nombre, ingredientes y alérgenos; lo servido a petición del '
                           'cliente no es «packaged»', 'FDA Food Code 2022 §3-602.11; §1-201.10 (Packaged)')),
    ('norma_helado', ('ice cream: al menos 4,5 lb por galón y 10 % de grasa láctea', '21 CFR 135.110')),
    ('menores', ('14-15 años: fuera del horario escolar, 7 AM - 7 PM (9 PM del 1 de junio al Labor Day), máximos por '
                 'día y semana; equipos permitidos', '29 CFR 570.35 y 570.34; [estatal] work permits')),
    ('bascula', ('venta al peso con báscula legal para el comercio', '[estatal] pesas y medidas; NIST Handbook 44 (NTEP)')),
    ('cfpm', ('un certified food protection manager en el equipo; food handler cards según el estado',
              'FDA Food Code 2022 §2-102.12; [estatal]')),
    ('seguro_frio', ('equipment breakdown con food spoilage', '[criterio del kit] seguros US')),
    ('temporada', ('alta de Memorial Day a Labor Day; National Ice Cream Month (julio) y National Ice Cream Day (3.er '
                   'domingo de julio); Juneteenth (19 de junio)', 'Proclamation 5219 (1984); 5 U.S.C. 6103')),
    ('hielo_seco', ('guantes, sin contacto con el helado, vehículo ventilado', '[criterio del kit]')),
    ('plazos_kit', ('mezcla 3-5 días; maduración 4-12 h; vida útil de la tabla del 02; 18-24 sabores en verano y 10-14 '
                    'en invierno; food cost < 28-32 %', '[criterio del kit]')),
])
# °F que el kit puede afirmar (G7): helado (−4, 0, 6, 10, 14, 16, 19), mezcla (36, 39, 41, 70, 104, 122, 135, 185),
# calibración (32) y lavamanos (100)
GRADOS_F_SPEC = {-4, 0, 6, 10, 14, 16, 19, 32, 36, 39, 41, 70, 100, 104, 122, 135, 185}

# ==========================================================================
# Pistas y dependencias de la heladería (extraer_textos.py)
# ==========================================================================
PISTAS_CAMBIO = {r'Kit de Tareas': 'D2: «Ice Cream Shop Checklists Kit Pro»'}
PISTAS_FUERA = (r'Restaurante Casual',)
PISTAS_EXTRA = [
    (r'[Hh]elader[ií]a', 'D2: la EN no lleva el sufijo «— Heladería Artesanal»; heladería → ice cream shop (o scoop '
                         'shop / ice cream parlor; gelato shop solo si el texto habla de gelato)'),
    (r'[Vv]itrinas?', 'vitrina de helado → dipping cabinet (gelato case si es de gelato); cristales → glass'),
    (r'[Mm]antecador', 'mantecadora → batch freezer; mantecar → batch-freeze / churn'),
    (r'[Mm]aduraci[oó]n|[Mm]adurar', 'maduración de la mezcla → aging (age the mix)'),
    (r'[Aa]batid', 'abatidor → blast freezer / hardening cabinet; abatir → harden'),
    (r'[Oo]brador', 'obrador → production room (o kitchen)'),
    (r'[Pp]orcionador|[Pp]ala\b|[Ee]spátula', 'porcionador / pala → scoop (dipper); espátula → spade'),
    (r'[Cc]ubetas?', 'cubeta → pan (tub / tray de la vitrina)'),
    (r'[Cc]ucuruchos?|[Bb]arquillos?|[Cc]onos?', 'cucurucho → cone (waffle cone, sugar cone); barquillo → wafer'),
    (r'[Tt]arrinas?', 'tarrina → cup; tarrina para llevar → pint / quart'),
    (r'[Cc]ucharillas?', 'cucharilla → spoon (tasting spoon para las muestras)'),
    (r'[Tt]oppings?|[Vv]irutas', 'toppings → toppings; virutas → sprinkles'),
    (r'[Vv]ariegato|[Ii]nclusiones|[Rr]ipple', 'variegato / ripple → swirl (ripple); inclusiones → mix-ins / inclusions'),
    (r'[Ss]orbete', 'sorbete → sorbet'),
    (r'[Tt]arta helada|[Ss]emifr[ií]o', 'tarta helada → ice cream cake; semifrío → semifreddo'),
    (r'[Dd]ependiente|[Hh]eladero', 'dependiente → scooper (counter staff); heladero/obrador → ice cream maker'),
    (r'[Ee]ncargado', 'encargado → shift lead'),
    (r'[Dd]egustaci[oó]n|[Pp]robar', 'degustación → samples / tasting'),
    (r'[Ff]ood cost|MP\b|[Mm]aterias? primas?', 'materias primas (MP) → ingredients (raw materials); food cost se queda'),
    (r'[Ff]idelizaci', 'tarjeta de fidelización → loyalty card / punch card'),
    (r'[Ss]eñal\b', 'señal → deposit'),
    (r'RRSS|redes', 'RRSS → social media'),
    (r'TPV|[Dd]atáfono', 'TPV / datáfono → POS / card terminal'),
    (r'[Cc]uadre|[Cc]uadrar', 'cuadre de caja → cash count / reconcile'),
    (r'[Tt]erraza', 'terraza → patio'),
    (r'[Ll]ocal\b', 'el local → the shop'),
    (r'APPCC', 'APPCC → food safety (HACCP solo si lo exige la licencia)'),
    (r'\bkg\b|0\.5L|1L', 'kg → lb; tarrinas de 0,5 L y 1 L → pints y quarts'),
]
DEPENDENCIAS_EXTRA = OrderedDict([
    ('variante', ('Sufijo de variante «Heladería Artesanal»', r'Heladería Artesanal', 'D2: la EN no lleva sufijo')),
    ('temperaturas_helado', ('Temperaturas del helado (conservación, vitrina, maduración, mantecación)',
                             r'−1[248] °C|−20 °C|−[79] °C|2-4 °C|85 °C', 'D-ICE: °F de REGLAS_US (helado_temps)')),
    ('pasteurizacion', ('Pasteurización propia', r'[Pp]asteuri', 'D-ICE: 185 °F (cifra del kit) + licencia estatal')),
    ('alergenos_scoop', ('Alérgenos en el scoop y en la carta', r'ALÉRGENOS|[Aa]lérgenos', 'D-ICE: los 9 de EE. UU.; '
                         'dipper well 3-304.12; scoop limpio para alergias')),
    ('registro_jornada', ('Registro de jornada (RD-ley 8/2019)', r'RD-ley|[Rr]egistro (diario )?de jornada|Inspección',
                          'D11: FLSA (29 CFR 516)')),
])

# aplicar_en / gates_en (autotest): la hoja con horas de celda y una hoja protegida con verdes desbloqueadas (el
# 01-07 del molde ligero no se protege), como el catering
HOJA_HORAS = ('08', 'Apertura del Negocio')
HOJA_VERDE = ('08', 'Apertura del Negocio')
CITA_AUTOTEST = '(FDA Food Code 3-501.18)'                     # autotest G7: una cita que NO está en REGLAS_US


def _rebind(f):
    return types.FunctionType(f.__code__, globals(), f.__name__, f.__defaults__, f.__closure__)


titulo_interior = _rebind(_base.titulo_interior)
_autotest_base = _rebind(_base.autotest)
_cruzar_censo_base = _rebind(_base.cruzar_censo)


def _minutos(h):
    m = re.match(r'^(\d{1,2}):(\d{2}) (AM|PM)$', h)
    return (int(m.group(1)) % 12 + (12 if m.group(3) == 'PM' else 0)) * 60 + int(m.group(2))


def autotest():
    err = _autotest_base()                       # pestañas, ficheros, glosario, POR_CELDA, billetes, calendario…
    if CLAVES['Tarea'] != GLOSARIO['Tarea']:
        err.append('CLAVES["Tarea"] debe ser el EN de la cabecera (GLOSARIO): los contadores la restan')
    rx = re.compile(TERMINOS_PROHIBIDOS)
    if not rx.search(TERMINO_PROHIBIDO_EJEMPLO):
        err.append('TERMINO_PROHIBIDO_EJEMPLO no lo caza TERMINOS_PROHIBIDOS')
    for ok in ('ice cream server', 'tip jar', 'patio', 'toppings bar', 'ice cream bars', 'restaurant supply store',
               'restaurant consultant', 'shift lead', 'scooper', 'dipping cabinet'):
        if rx.search(ok):
            err.append('TERMINOS_PROHIBIDOS caza lo permitido (%r)' % ok)
    rx_ctx = re.compile(RX_CONTEXTO_PENDIENTE)
    for ok in ('ice cream server', 'tip jar', 'patio', 'toppings bar', 'restaurant consultant'):
        if rx_ctx.search(ok):
            err.append('RX_CONTEXTO_PENDIENTE caza lo permitido (%r)' % ok)
    for k, v in list(GLOSARIO.items()) + list(POR_CELDA.items()) + list(CLAVES.items()):
        if k not in _base.GLOSARIO or k in _GLOSARIO_ICE:
            if isinstance(v, str) and rx.search(v):
                err.append('texto EN fijado con un término prohibido: %r → %r' % (k, v))
    if CITA_AUTOTEST.strip('()').split()[-1] in ' '.join(f for _v, f in REGLAS_US.values()):
        err.append('CITA_AUTOTEST está en REGLAS_US: G7 no la cazaría')
    # horas: formato US, mismo orden que el ES y +DESPLAZAMIENTO_H exactas
    for k, h_es in HORAS_ES.items():
        en = POR_CELDA[k]
        if not re.match(r'^\d{1,2}:\d{2} (AM|PM)$', en):
            err.append('hora fijada sin formato US: %r → %r' % (k, en))
        elif _minutos(en) - (int(h_es[:2]) * 60 + int(h_es[3:])) != DESPLAZAMIENTO_H * 60:
            err.append('hora fijada que no es ES + %d h: %r (%s → %s)' % (DESPLAZAMIENTO_H, k, h_es, en))
    for hoja in (_AN, _AC9):
        hs = [_minutos(POR_CELDA[k]) for k in HORAS_ES if k[:2] == hoja]
        if hs != sorted(hs):
            err.append('%s: las horas fijadas no van en orden' % hoja[1])
    if sorted(o for o, *_r in _CIERRE_08) != list(range(5, 20)):
        err.append('08 cierre: las filas de origen no son una permutación de 5-19')
    if [o for o, *_r in _CIERRE_08][-3:] != [16, 9, 17]:
        err.append('08 cierre: alarma, puertas y llave tienen que ser las 3 últimas')
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
    for k in CELSIUS_SIN_F:
        if '°' in POR_CELDA.get(k, '') or '°F' in ADAPTAR.get(k, ''):
            err.append('CELSIUS_SIN_F %r con temperatura en el EN fijado o en el ADAPTAR' % (k,))
    if '°F' not in POR_CELDA[_CN + ('B%d' % (5 + [o for o, *_r in _CIERRE_08].index(19)),)]:
        err.append('08 cierre: la fila con las temperaturas de cierre (origen 19) no lleva °F')
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
    cfs = {(info['corto'], h, cf['sqref']): cf['formula'] for info in censo['libros'].values()
           for h, hd in info['hojas_detalle'].items() for cf in hd['cf']}
    for k, (es, en) in CF_POR_CELDA.items():
        if cfs.get(k) != [es]:
            err.append('CF_POR_CELDA %r: el ES trae %r, no %r' % (k, cfs.get(k), es))
    # hojas con CF de «hecho» en la columna E que no van en CF_POR_CELDA: solo el 07 (cabecera fuera del rango)
    for k, f in cfs.items():
        if f == ['$E6="✓"'] and k not in CF_POR_CELDA:
            err.append('CF de «hecho» con cabeceras internas sin CF_POR_CELDA: %r' % (k,))
    for k, h in HORAS_ES.items():
        if tx.get(k) != h:
            err.append('HORAS_ES: %r no trae en el ES %r (trae %r)' % (k, h, tx.get(k)))
    horas_es = {k for k, t in tx.items() if RX_HORA_CELDA.match(t)}
    if horas_es != set(HORAS_ES):
        err.append('horas de celda del ES fuera de HORAS_ES: %r' % sorted(horas_es ^ set(HORAS_ES)))
    # 08 cierre: el ES tiene tarea en la fila de origen; la zona EN es la del glosario de la zona ES de esa fila y el
    # responsable ES es el esperado salvo los de _RESPONSABLE_CAMBIA
    for o, _b, c_en, d_en in _CIERRE_08:
        if (_CN[0], _CN[1], 'B%d' % o) not in tx:
            err.append('08 cierre: B%d sin tarea en el ES' % o)
        z_es = tx.get((_CN[0], _CN[1], 'C%d' % o))
        if GLOSARIO.get(z_es) != c_en:
            err.append('08 cierre: la zona de la fila %d (%r → %r) no es %r' % (o, z_es, GLOSARIO.get(z_es), c_en))
        r_es = tx.get((_CN[0], _CN[1], 'D%d' % o))
        if GLOSARIO.get(r_es) != d_en and o not in _RESPONSABLE_CAMBIA:
            err.append('08 cierre: el responsable de la fila %d (%r) no es %r' % (o, r_es, d_en))
    if not tx.get((_CN[0], _CN[1], 'B18'), '').startswith('Cubrir vitrinas') or \
            not tx.get((_CN[0], _CN[1], 'B16'), '').startswith('Activar alarma'):
        err.append('08 cierre: el ES ya no cubre las vitrinas después de la alarma (errata corregida en el ES)')
    # calendario: A (mes), C (sabores) y D (temporada) con texto en el ES; la temporada ES es Baja/Alta/Transición
    for fila in FILAS_CALENDARIO:
        for col in 'ABCD':
            if (HOJA_CAL[0], HOJA_CAL[1], '%s%d' % (col, fila)) not in tx:
                err.append('calendario: %s%d sin texto en el ES' % (col, fila))
        if tx.get((HOJA_CAL[0], HOJA_CAL[1], 'D%d' % fila)) not in ('Baja', 'Alta', 'Transición'):
            err.append('calendario: D%d no es una temporada del ES' % fila)
    # la tabla de vida útil del 02 trae °C donde se fija
    for f in range(31, 36):
        if '°C' not in tx.get(('02', 'Mantecación', 'C%d' % f), ''):
            err.append('02 vida útil C%d: el ES no trae °C' % f)
    # todo texto ES con °C tiene su °F fijado (POR_CELDA) o un ADAPTAR que lo da
    for k, t in tx.items():
        if '°C' in t and k not in CELSIUS_SIN_F:
            dic = POR_CELDA.get(k) or ADAPTAR.get(k) or ''
            if '°F' not in dic:
                err.append('°C del ES sin °F en POR_CELDA/ADAPTAR: %r' % (k,))
    for k in ADAPTAR:
        if k not in tx:
            err.append('ADAPTAR %r sin texto en el ES' % (k,))
    return err


def cruzar_base(p_ice, p_base):
    """Lo heredado POR CELDA del base (POR_CELDA y ADAPTAR del 09 y del 08) tiene en la heladería el mismo texto ES que
    en el base."""
    import json
    err = []

    def textos(p):
        d = {}
        for info in json.load(open(p, encoding='utf-8'))['libros'].values():
            for h, hd in info['hojas_detalle'].items():
                for coord, t in hd.get('textos', {}).items():
                    d[(info['corto'], h, coord)] = t
        return d
    tb, ti = textos(p_base), textos(p_ice)
    for nombre, claves in (('POR_CELDA', _HEREDA_POR_CELDA),
                           ('ADAPTAR', _HEREDA_ADAPTAR + [('08', 'Apertura del Negocio', 'B8')])):
        for k in claves:
            if ti.get(k) != tb.get(k):
                err.append('%s heredado %r: el texto ES de la heladería %r ≠ base %r' % (nombre, k, ti.get(k),
                                                                                         tb.get(k)))
    # filas equivalentes (otra celda, la misma tarea del base): mismo tema en el ES
    for k, palabra in ((('01', 'Apertura', 'B7'), 'anillos'), (('01', 'Apertura', 'B9'), 'manos'),
                       (('01', 'Apertura', 'B10'), 'síntomas'), (('01', 'Apertura', 'B12'), 'GAS'),
                       (('03', 'Tareas Mensuales', 'B15'), 'registros de jornada'),
                       (('03', 'Tareas Diarias', 'B17'), 'registro diario de jornada')):
        if palabra not in ti.get(k, ''):
            err.append('%r ya no es la tarea equivalente del base (falta %r)' % (k, palabra))
    return err


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
        e += cruzar_base(pc, os.path.join(os.path.dirname(AQUI), 'censo_es.json'))
    for x in e:
        print('ERROR', x)
    print('mapas_icecream.py: {} ficheros · {} pestañas · {} glosario · {} por celda · {} cf por celda · {} adaptar · '
          '{} reglas · {} errores'.format(len(FICHEROS), len(HOJAS), len(GLOSARIO), len(POR_CELDA), len(CF_POR_CELDA),
                                          len(ADAPTAR), len(REGLAS_US), len(e)))
    raise SystemExit(1 if e else 0)
