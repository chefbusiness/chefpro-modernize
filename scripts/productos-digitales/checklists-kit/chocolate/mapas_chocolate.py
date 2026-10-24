#!/usr/bin/env python3
"""
mapas_chocolate.py — Chocolate Shop Checklists Kit Pro (EN) · DELTA del Kit de Tareas Chocolatería
(`kit-tareas-chocolateria`, 11 xlsx v2.1) sobre `mapas.py` (Restaurant Checklists Kit Pro). SPEC: `chocolate/SPEC.md`
(solo el delta). Octavo hermano vertical. Sesión Claude Code, 24-oct-2026.

Molde HÍBRIDO, como la heladería (lo mide el censo): el 01-07, el B01 y el B02 son el molde ligero del catering (# ·
Tarea · Zona · Responsable · ✓ · Hora · Notas; cabeceras internas por sección; contadores que restan «Tarea»; CF
`$E6="✓"`; sin protección; subtítulo A2 en vez de la línea de marca D19) y el 08 y el 09, los del kit base. El 09 NO es
idéntico al base: la venta al peso añade 2 tareas a «Apertura de Caja» (báscula y precio por kilo) y 2 a «Cierre de Caja»
(venta al peso y señales), así que el fondo (B23 → B25) y toda la tabla de billetes y el resumen (filas 24-54 → 26-56)
bajan 2 filas. Su POR_CELDA se hereda del base DESPLAZADO (`_mover`), DENOMINACIONES y FORMULAS_POR_CELDA se recalculan
y G5 corre con CASOS_G5 (el caso de SPEC §5 del base en las celdas nuevas), sin tocar código común.

Se usa con `--kit chocolate` (kit.py). Importa `mapas.py` y SOLO añade o sobrescribe: producto, ficheros, títulos,
pestañas, glosario (zonas de un obrador-tienda de chocolate: kitchen, tempering, molding, cool room, fridge, display
case; roles de una chocolate shop US: chocolatier, sales associate, shift lead), CLAVES (+ «Tarea»), CF_POR_CELDA (las
cabeceras internas no se pintan de verde), calendario del BONUS-02 (12 meses: A mes · B acciones · C productos · D
temporada), POR_CELDA (09 desplazado; 05 «Quarterly & Annual» de una chocolate shop US; el orden del cierre del 08;
las horas del 08 y del 09, +2 h; la tabla de vida útil del 02), ADAPTAR y REGLAS_US (templado en °F según el
fabricante, sala y conservación, ganache como TCS salvo análisis de aw, alérgenos de la vitrina 3-602.12(C), etiqueta
de lo envasado 3-602.11, báscula legal para el comercio). Las funciones del base que leen constantes (titulo_interior,
autotest, cruzar_censo) se re-enlazan a ESTE módulo. Ejecutado como script: autotest + cruce con chocolate/censo_es.json
+ cruce con el base (lo heredado por celda tiene el mismo texto ES).

    python3 chocolate/mapas_chocolate.py
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
AQUI = os.path.dirname(os.path.abspath(__file__))              # chocolate/ (el import * trae el AQUI del base)

ORIGEN_ES = 'kit-tareas-chocolateria'
PRODUCTO = 'Chocolate Shop Checklists Kit Pro'
# D2: H1 = title SEO (73 caracteres); «chocolate shop» 49.500/mes US; «Tempering» = lo que ningún kit genérico trae
# («chocolate tempering» 9.900/mes)
TITULO_SEO = 'Chocolate Shop Checklists Kit Pro: Opening, Closing & Tempering Templates'
SLUG = 'chocolate-shop-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_CHOCOLATE_SHOP_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
VERSION_ES = '2.1'                     # el ES va por la v2.1 (octubre 2026; 5 libros aún dicen 2.0): la EN, 2.1 en los 11
MARCA_ES = '— Kit de Tareas Recurrentes · Chocolatería · AI Chef Pro · aichef.pro'
MARCA_EN = '— ' + PRODUCTO + ' · AI Chef Pro · aichef.pro'
VARIANTES_ES = ('Chocolatería',)       # G2: «Chocolatería / Bombonería», «Chocolatería / Obrador de Chocolate»…
# heredar.py: memoria con VARIAS fuentes, en orden de preferencia (gana la primera que acierta). La heladería PRIMERO
# (mismo molde ligero: cabeceras, pies e «Instrucciones» del molde; tienda con obrador y mostrador), luego la cafetería
# (tienda con mostrador), el base, el catering, la pizzería, la hamburguesería, la ghost kitchen y el bar. Medido en la
# F1 (SPEC §4).
_SUF = lambda v: [(' — Chocolatería / Bombonería', ' — ' + v), (' — Chocolatería', ' — ' + v),  # noqa: E731
                  (' · Chocolatería', ' · ' + v)]
MEMORIA = [('icecream', 'icecream', _SUF('Heladería Artesanal')), ('cafe', 'cafe', _SUF('Cafetería / Brunch')),
           ('base', '', _SUF('Restaurante Casual')), ('catering', 'catering', _SUF('Catering / Eventos')),
           ('pizza', 'pizza', _SUF('Pizzería')), ('burger', 'burger', _SUF('Hamburguesería')),
           ('ghost', 'ghost', _SUF('Dark Kitchen')), ('bar', 'bar', _SUF('Bar / Cocktails'))]
# heredar.py: EN heredado que en una chocolatería no vale tal cual → pendientes (motivo «contexto»). Una chocolate shop
# es obrador + tienda de mostrador: sin sala con camareros, reservas, barra de copas, café de barista, cocina de línea,
# helado ni pasteurizador.
RX_CONTEXTO_PENDIENTE = (r'(?i)\b(?:dining rooms?|dine-in|FOH|host stands?|hostess|waitstaff|tables? service|servers?|'
                         r'reservations?|bartenders?|barbacks?|cocktails?|beer|liquor|wine|baristas?|espresso|'
                         r'coffee shops?|cafes?|bussers?|head chefs?|sous chefs?|line cooks?|prep cooks?|kitchen leads?|'
                         r'MOD|shift managers?|venues?|banquets?|BEOs?|line-up|pizzas?|pizzerias?|dough|burgers?|grill|'
                         r'fryers?|ghost kitchens?|packers?|app managers?|commissar(?:y|ies)|ice cream|gelato|scoops?|'
                         r'scoopers?|dipping cabinets?|batch freezers?|dipper wells?|pints?|toppings?|cones?|sundaes?|'
                         r'pasteuri[sz]\w*|restaurants?(?! consultant| supply))\b')
# heredar.py: cadenas idénticas a una fuente cuyo EN no vale en la chocolatería (→ pendientes → G1.json, con base_en)
NO_HEREDAR = {}
# gates_en.py G2: términos de otros kits que NINGUNA celda EN de la chocolatería puede llevar. «patio», «kitchen»,
# «liqueur» (bombones de licor), «hot chocolate», «coffee» (sabor), «restaurant supply» y la firma «restaurant
# consultant» quedan permitidos.
TERMINOS_PROHIBIDOS = (r'(?i:\b(?:dining rooms?|host stands?|hostess|waitstaff|table service|servers?|bartenders?|'
                       r'barbacks?|cocktails?|beer|liquor|baristas?|espresso|coffee shops?|cafes?|bussers?|head chefs?|'
                       r'sous chefs?|line cooks?|prep cooks?|banquets?|BEOs?|line-up|venues?|pizzas?|pizzerias?|dough|'
                       r'burgers?|ghost kitchens?|packers?|app managers?|ice cream|gelato|scoopers?|dipping cabinets?|'
                       r'batch freezers?|dipper wells?|restaurants?(?! consultant| supply))\b)|\b(?:MOD|FOH)\b')
TERMINO_PROHIBIDO_EJEMPLO = 'Ask the barista to restock the dipping cabinet before the bartender arrives.'
REFERENCIAS_TRADUCTOR = ['chocolate/SPEC.md', 'SPEC.md §0-§3 y §7.2 (brief)', 'textos_en/glosario.json (glosario de la '
                         'prosa del kit base)', 'chocolate/textos_en/heredado.json (cómo se dijo ya cada cosa: heladería, '
                         'cafetería, base, catering, pizzería, hamburguesería, ghost kitchen y bar)',
                         'chocolate/mapas_chocolate.py: GLOSARIO, HOJAS, FICHEROS, TITULOS, POR_CELDA, REGLAS_US',
                         '../GLOSARIO-JERGA-ES-EN.md (sección Chocolatería)']
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v2.1'),
    ('keywords', 'chocolate shop checklist, chocolate shop opening checklist, chocolatier, chocolate tempering, '
                 'bonbons, chocolate truffles, chocolate molds, chocolate store, AI Chef Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

# ==========================================================================
# Ficheros (D5: «chocolate shop» 49.500/mes US, «bonbons» 90.500, «chocolatier» 27.100, «chocolate truffles» 27.100,
# «chocolate tempering» 9.900, «chocolate molds» 9.900, «chocolate store» 9.900; las variantes con «checklist» sin
# volumen, como en los hermanos)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-apertura-cierre.xlsx', '01-chocolate-shop-opening-closing-checklists.xlsx'),
    ('02-partidas-produccion.xlsx', '02-chocolate-tempering-molding-checklists.xlsx'),
    ('03-tareas-manager.xlsx', '03-chocolate-shop-manager-checklist.xlsx'),
    ('04-tareas-perfiles.xlsx', '04-chocolate-shop-duties-by-role.xlsx'),
    ('05-tareas-semanales-mensuales.xlsx', '05-chocolate-shop-cleaning-checklist-maintenance.xlsx'),
    ('06-eventos-temporada.xlsx', '06-chocolate-shop-seasonal-checklists.xlsx'),
    ('07-plantilla-personalizable.xlsx', '07-blank-chocolate-shop-checklist-template.xlsx'),
    ('08-apertura-cierre-negocio.xlsx', '08-chocolate-store-opening-closing-checklist.xlsx'),
    ('09-apertura-cierre-caja.xlsx', '09-cash-drawer-opening-closing.xlsx'),
    ('BONUS-01-briefing-servicio.xlsx', 'BONUS-01-chocolate-shop-pre-shift-meeting-template.xlsx'),
    ('BONUS-02-calendario-anual-tareas.xlsx', 'BONUS-02-chocolate-shop-holiday-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)
TITULOS = OrderedDict([
    ('01-chocolate-shop-opening-closing-checklists.xlsx',
     'Chocolate Shop Opening & Closing Checklists: Kitchen, Display Case & Counter'),
    ('02-chocolate-tempering-molding-checklists.xlsx',
     'Chocolate Tempering & Molding Checklists: Dark, Milk & White, Bonbons & Bars'),
    ('03-chocolate-shop-manager-checklist.xlsx', 'Chocolate Shop Manager Checklist: Daily, Weekly & Monthly'),
    ('04-chocolate-shop-duties-by-role.xlsx',
     'Chocolate Shop Duties by Role: Chocolatier, Sales Associate & Shift Lead'),
    ('05-chocolate-shop-cleaning-checklist-maintenance.xlsx',
     'Chocolate Shop Cleaning Checklist, Inventory & Maintenance Schedule'),
    ('06-chocolate-shop-seasonal-checklists.xlsx',
     "Chocolate Shop Seasonal Checklists: Holiday Season, Valentine's Day & Easter"),
    ('07-blank-chocolate-shop-checklist-template.xlsx', 'Blank Chocolate Shop Checklist Template (Editable)'),
    ('08-chocolate-store-opening-closing-checklist.xlsx',
     'Chocolate Store Opening & Closing Checklist (Whole Shop)'),
    ('09-cash-drawer-opening-closing.xlsx', 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log'),
    ('BONUS-01-chocolate-shop-pre-shift-meeting-template.xlsx',
     'BONUS: Chocolate Shop Pre-Shift Meeting Template (Huddle Notes)'),
    ('BONUS-02-chocolate-shop-holiday-calendar.xlsx',
     'BONUS: Chocolate Shop Holiday Calendar & Product Planner (US)'),
])
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

HOJAS = OrderedDict(_base.HOJAS)
HOJAS.update([
    ('Apertura', 'Opening'), ('Cierre', 'Closing'),
    ('Templado', 'Tempering'), ('Moldeado', 'Molding & Bars'),
    # «Semanal» y «Mensual» salen en el 03 y en el 05: el mismo EN en los dos (únicas por libro)
    ('Diario', 'Daily Tasks'), ('Semanal', 'Weekly Tasks'), ('Mensual', 'Monthly Tasks'),
    ('Chocolatero', 'Chocolatier'), ('Dependiente', 'Sales Associate'), ('Encargado', 'Shift Lead'),
    # 06: la campaña de Navidad US es la «holiday season» (Christmas + Hanukkah + regalos de empresa)
    ('Navidad', 'Holiday Season'), ('Pascua', 'Easter'),
    ('Por Zona', 'By Area'), ('Por Turno', 'By Shift'),
    # 08: el «negocio» es la tienda (ni restaurante ni edificio)
    ('Apertura del Negocio', 'Shop Opening'), ('Cierre del Negocio', 'Shop Closing'),
    ('Calendario', 'Holiday Calendar'),
])
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Apertura', 'Cierre']),
    ('02', ['Instrucciones', 'Templado', 'Moldeado']),
    ('03', ['Instrucciones', 'Diario', 'Semanal', 'Mensual']),
    ('04', ['Instrucciones', 'Chocolatero', 'Dependiente', 'Encargado']),
    ('05', ['Instrucciones', 'Semanal', 'Mensual', 'Trimestral y Anual']),
    ('06', ['Instrucciones', 'Navidad', 'San Valentín', 'Pascua']),
    ('07', ['Instrucciones', 'Por Zona', 'Por Turno', 'Por Perfil']),
    ('08', ['Instrucciones', 'Apertura del Negocio', 'Cierre del Negocio']),
    ('09', ['Instrucciones', 'Apertura de Caja', 'Cierre de Caja', 'Registro Mensual']),
    ('B01', ['Instrucciones', 'Briefing']),
    ('B02', ['Instrucciones', 'Calendario']),
])

# ==========================================================================
# GLOSARIO: el base entero (opcional) + celdas cortas de una chocolatería. Jerga US de chocolate shop: kitchen (el
# obrador), tempering, molding, cool room (cámara de conservación 59–64 °F), fridge (nevera de rellenos), display case,
# dry storage, sales associate, shift lead.
# ==========================================================================
GLOSARIO = OrderedDict(_base.GLOSARIO)
_GLOSARIO_CHOCO = OrderedDict([
    # subtítulo de marca (A2) de las checklists del molde ligero: el producto EN, igual en todo el kit (como el catering)
    ('AI Chef Pro · aichef.pro — Kit de Tareas: Chocolatería / Obrador de Chocolate', 'AI Chef Pro · aichef.pro — '
     + PRODUCTO),
    ('Hora', 'Time'), ('Mes', 'Month'), ('Temporada', 'Season'), ('Semestral', 'Semiannual'),
    ('Acciones clave / Fechas señaladas', 'Key actions & dates'), ('Productos destacados', 'Featured products'),
    # zonas (columna C); 1 sobrescribe el base: Sala (FOH)
    ('Obrador', 'Kitchen'), ('Templado', 'Tempering'), ('Moldeado', 'Molding'), ('Conservación', 'Cool room'),
    ('Cámara', 'Fridge'), ('Vitrina', 'Display case'), ('Tienda', 'Shop'), ('Mostrador', 'Counter'),
    ('Packaging', 'Packaging'), ('Envasado', 'Wrapping'), ('Almacén', 'Dry storage'), ('Gestión', 'Management'),
    ('Producción', 'Production'), ('Equipo', 'Team'), ('RRSS', 'Social media'), ('Logística', 'Logistics'),
    ('Sala', 'Shop floor'),
    # puestos (08 y 09); 2 sobrescriben el base: Encargado (Shift manager) y Responsable de caja (Cashier / MOD)
    ('Encargado', 'Shift lead'), ('Responsable de caja', 'Cashier / shift lead'),
    # tabla de vida útil del 02 (la del base dice «Food group» / «Freezer time»: aquí es vida útil del chocolate)
    ('Familia', 'Product type'), ('Vida útil', 'Shelf life'),
])
GLOSARIO.update(_GLOSARIO_CHOCO)
GLOSARIO_OPCIONAL = frozenset(_base.GLOSARIO)
PUESTOS_ES = frozenset(_base.PUESTOS_ES | {'Obrador', 'Templado', 'Moldeado', 'Conservación', 'Cámara', 'Vitrina',
                                           'Tienda', 'Mostrador', 'Packaging', 'Envasado', 'Almacén', 'Gestión',
                                           'Producción', 'Equipo', 'RRSS', 'Logística'})

# ==========================================================================
# CLAVES: «Tarea» (los contadores del 01-07 y del B01 restan las cabeceras internas, como el catering)
# ==========================================================================
CLAVES = OrderedDict(_base.CLAVES)
CLAVES.update([('Tarea', 'Task')])

# ==========================================================================
# CF_POR_CELDA (desviación DECLARADA respecto del ES, la del catering ronda 1 M5 y la heladería D7): en las hojas con
# varias tablas, las cabeceras internas llevan «✓» en la columna E y la CF de «hecho» las pinta de verde. La EN excluye
# las filas cuyo B es la cabecera «Task». El 07 (cabecera fuera del rango, `$E5`) no.
# ==========================================================================
_CF_HOJAS = [('01', 'Apertura', 'A6:G38'), ('01', 'Cierre', 'A6:G27'), ('02', 'Templado', 'A6:G33'),
             ('02', 'Moldeado', 'A6:G33'), ('03', 'Diario', 'A6:G26'), ('03', 'Semanal', 'A6:G40'),
             ('03', 'Mensual', 'A6:G23'), ('04', 'Chocolatero', 'A6:G27'), ('04', 'Dependiente', 'A6:G30'),
             ('04', 'Encargado', 'A6:G23'), ('05', 'Semanal', 'A6:G34'), ('05', 'Mensual', 'A6:G25'),
             ('05', 'Trimestral y Anual', 'A6:G25'), ('06', 'Navidad', 'A6:G26'), ('06', 'San Valentín', 'A6:G23'),
             ('06', 'Pascua', 'A6:G24'), ('B01', 'Briefing', 'A6:G32')]
CF_POR_CELDA = OrderedDict(((c, h, sq), ('$E6="✓"', 'AND($E6="✓",$B6<>"%s")' % CLAVES['Tarea']))
                           for c, h, sq in _CF_HOJAS)
# G3: libros cuyo ES no trae la línea de marca D19 (solo el 08 y el 09; los demás, el subtítulo A2), como el catering
LIBROS_SIN_MARCA = ('01', '02', '03', '04', '05', '06', '07', 'B01', 'B02')

# ==========================================================================
# 09 (D12): el ES chocolatería trae 2 tareas más en la apertura y 2 en el cierre (venta al peso, señales): el fondo y la
# tabla de billetes bajan 2 filas. Recuento en dólares del base, en las filas del ES chocolatería.
# ==========================================================================
DESPLAZA_09 = 2
DENOMINACIONES = [(f + DESPLAZA_09, es, xes, en, xen) for f, es, xes, en, xen in _base.DENOMINACIONES]
VALORES_DENOMINACION_EN = sorted({d[4] for d in DENOMINACIONES})
FORMULAS_POR_CELDA = OrderedDict(
    ((HOJA_CAJA[0], HOJA_CAJA[1], 'C%d' % f), ('=B%d*%s' % (f, _num(xes)), '=B%d*%s' % (f, _num(xen))))
    for f, _es, xes, _en, xen in DENOMINACIONES)


def _mover(k):
    """Celda del 09 del base → la misma celda del ES chocolatería (fondo y tabla de caja, +2 filas)."""
    c, h, coord = k
    m = re.match(r'^([A-Z]+)(\d+)$', coord)
    col, fila = m.group(1), int(m.group(2))
    if (h == 'Apertura de Caja' and fila >= 23) or (h == 'Cierre de Caja' and fila >= 24):
        fila += DESPLAZA_09
    return (c, h, '%s%d' % (col, fila))


_H09 = {k: _mover(k) for k in _base.POR_CELDA if k[0] == '09'}
# G5: el caso de SPEC §5 del base, en las celdas del ES chocolatería (gates_en.caso_caja tiene fijas las del base)
_HA, _HC, _HR = 'Apertura de Caja', 'Cierre de Caja', 'Registro Mensual'
_F0 = DENOMINACIONES[0][0]                                      # $100 (29)
CASOS_G5 = [
    {'nombre': 'efectivo 1 de cada', 'entradas': {(_HC, 'B%d' % d[0]): 1 for d in DENOMINACIONES},
     'esperado': {(_HC, 'C45'): 204.91}},
    {'nombre': 'cierre 200 / 1,250 / 3,000 / 150 / Z 4,200', 'entradas': {
        (_HA, 'C25'): 200, (_HC, 'B%d' % _F0): 12, (_HC, 'B%d' % (_F0 + 1)): 1, (_HC, 'C52'): 3000,
        (_HC, 'C53'): 150, (_HC, 'C55'): 4200, (_HR, 'B5'): 200, (_HR, 'C5'): 1250, (_HR, 'D5'): 3000,
        (_HR, 'E5'): 150, (_HR, 'G5'): 4200},
     'esperado': {(_HC, 'C45'): 1250, (_HC, 'C49'): 1250, (_HC, 'C50'): 200, (_HC, 'C51'): 1050, (_HC, 'C54'): 4200,
                  (_HC, 'C56'): 0, (_HR, 'F5'): 4200, (_HR, 'H5'): 0}},
]
CELDA_CACHE_MAL = 'C52'                # autotest G6: «Card sales, excl. tips» (C50 en el base)

# ==========================================================================
# BONUS-02 «Holiday Calendar»: otra estructura (12 meses, filas 5-16: A mes · B acciones y fechas · C productos · D
# temporada · E ✓ · F notas). A, C y D fijados; B = traductor con ADAPTAR (fechas y tareas US, en orden). Temporada US
# de una chocolate shop: picos en Valentine's Day y en diciembre; alta en Easter, Mother's Day y noviembre; el verano,
# bajo (calor: envíos con cold packs). Sin alcohol, turrón, monas, comuniones ni panellets.
# fila → (mes EN, productos EN, temporada EN, ADAPTAR de B)
# ==========================================================================
HOJA_CAL = ('B02', 'Calendario')
FILAS_CALENDARIO = range(5, 17)
CALENDARIO = OrderedDict([
    (5, ('January', 'Truffles, Spiced Bonbons, Hot Chocolate', 'Low',
         'Sustituye a Reyes (6 de enero: no es fecha comercial en EE. UU.). Liquidar el stock de las fiestas (rebajas de '
         'enero), lanzar la colección de invierno, y preparar Valentine\'s Day: diseño, moldes y packaging; publicar la '
         'fecha límite de encargos')),
    (6, ('February', 'Hearts, Premium Bonbons, Personalized Bars', 'Peak',
         "Valentine's Day (14 de febrero), el gran pico del año: corazones y edición limitada; fecha límite de encargos "
         'el día 10 y entregas exprés el 13 y el 14; los envíos, con la fecha límite del transportista (shipping cutoff)')),
    (7, ('March', 'Eggs, Bunnies, Mint Bonbons', 'High',
         "Sustituye al Día del Padre (en EE. UU. va en junio, fila 10). St. Patrick's Day (17 de marzo): bombones de "
         'menta y en verde; preparar Easter (fecha variable, marzo o abril): huevos y conejos (bunnies); talleres '
         'infantiles')),
    (8, ('April', 'Eggs, Bunnies, Floral Bonbons', 'High',
         'Easter (fecha variable): huevos, conejos y cestas de Pascua (Easter baskets) por encargo. Sustituye a las '
         'comuniones: bodas y baby showers de primavera (detalles para invitados: favors) y cajas personalizadas')),
    (9, ('May', 'Premium Bonbons, Gift Boxes, Engraved Bars', 'High',
         "Mother's Day (2.º domingo de mayo, no el 1.º como en España): cajas premium por encargo, encargos cerrados "
         '2 weeks out; Teacher Appreciation Week (1.ª semana completa de mayo): cajas pequeñas de regalo; graduaciones '
         '(mayo-junio): regalos y cajas personalizadas')),
    (10, ('June', "Fruit Bars, Wedding Favors, Father's Day Boxes", 'Medium',
          "Father's Day (3.er domingo de junio); temporada de bodas (favors) y graduaciones; empieza el verano: adaptar "
          'el catálogo (menos ganache fresca, más tableta y producto estable) y preparar los envíos con calor (caja '
          'aislada y cold packs)')),
    (11, ('July', 'Souvenir Bars, Local-Flavor Bonbons', 'Low',
          'Verano: packs souvenir y colaboraciones locales si tu zona tiene turismo; 4 de julio (festivo federal): '
          'decide el horario; envíos con calor: caja aislada (insulated mailer) y cold packs, y enviar de lunes a '
          'miércoles para que no pase el fin de semana en un almacén; vigilar a diario la temperatura de tienda y '
          'vitrina')),
    (12, ('August', 'Reduced Production, Q4 Planning', 'Low',
          'Sustituye a la Asunción (el 15 de agosto no es festivo en EE. UU.). Verano bajo: mantenimiento profundo, '
          'vacaciones escalonadas y cerrar el pedido de cobertura (couverture) para el último trimestre; vuelta al '
          'cole (mediados-finales de agosto)')),
    (13, ('September', 'Nut Bonbons, Praline, Spiced Bonbons', 'Medium',
          'Labor Day (1.er lunes de septiembre); vuelta a la rutina; colección de otoño; ferias y festivales '
          'gastronómicos; abrir la agenda de regalos de empresa (corporate gifting) del último trimestre: catálogo y '
          'precios por volumen')),
    (14, ('October', 'Halloween Figures, Pumpkin Spice Bonbons, Dark Bars', 'Medium',
          'Halloween (31 de octubre): figuras y bombones de temporada; Sweetest Day (3.er sábado de octubre, sobre todo '
          'en el Medio Oeste) y National Chocolate Day (28 de octubre, fecha comercial): campaña en redes; producción '
          'de las fiestas (holidays) a pleno y publicar el catálogo de fiestas y el de regalos de empresa')),
    (15, ('November', 'Chocolate Turkeys, Host Gifts, Corporate Gift Boxes', 'High',
          'Sustituye a Todos los Santos (sin panellets ni huesos de santo). Thanksgiving (4.º jueves de noviembre): '
          'regalos para el anfitrión (host gifts) y centros de mesa de chocolate; Black Friday y Small Business '
          'Saturday (el sábado después de Thanksgiving); preventa de las fiestas; regalos de empresa')),
    (16, ('December', 'Peppermint Bark, Holiday Figures, Gelt, Gift Boxes', 'Peak',
          'Fiestas (holidays), máxima producción: Christmas y Hanukkah (fecha variable: gelt de chocolate); fecha límite '
          'de encargos y de envíos (shipping cutoff del transportista) y horarios especiales del 24 y el 31 (Christmas '
          'Eve y New Year\'s Eve). Sin turrones ni el puente de la Constitución')),
])

# ==========================================================================
# POR_CELDA: lo heredado del base (el 09, desplazado; mismo texto ES, lo comprueba cruzar_base) + lo de la chocolatería
# ==========================================================================
POR_CELDA = OrderedDict((_H09[k], _base.POR_CELDA[k]) for k in _H09)
_T = ('05', 'Trimestral y Anual')
_M = ('02', 'Moldeado')
POR_CELDA.update([
    # 03 · conservación de fichajes (B16 del base: mismo EN, FLSA)
    (('03', 'Mensual', 'B16'), _base.POR_CELDA[('03', 'Mensual Manager', 'B16')]),
    # 02 · Moldeado: tabla de vida útil (criterio del kit; la ganache de nata fresca, TCS: date marking de 7 días)
    (_M + ('A37',), 'TYPICAL SHELF LIFE AT 59–64 °F AND 50–60% HUMIDITY — adjust it to your recipes and your kitchen'),
    (_M + ('C39',), '12–18 months'), (_M + ('C40',), '6–12 months'), (_M + ('C41',), '7 days at 41 °F'),
    (_M + ('C42',), '4–8 weeks'), (_M + ('C43',), '2–4 months'), (_M + ('C44',), '3–4 weeks'),
    (_M + ('C45',), '3–6 months'), (_M + ('C46',), '1–3 months'), (_M + ('C47',), '3–4 weeks'),
    (_M + ('C48',), 'Never'),
    (_M + ('D41',), 'Treat it as TCS: 41 °F or below, 7 days max (FDA date marking). Let the box warm up CLOSED before '
                    'opening, or it sweats. Longer only with a lab water-activity test'),
    # 05 · Trimestral y Anual: servicios contratados y papeles de una chocolate shop US (sin DDD, BIE, legionela,
    # RGSEAA ni Verifactu)
    (_T + ('A4',), 'Pest control, hygiene & lab tests — contracted'),
    (_T + ('B6',), 'Pest control by a licensed operator: service visit and signed service report on file (write the '
                   'report # in the Notes column)'),
    (_T + ('F6',), 'Monthly'),
    (_T + ('B7',), 'Exhaust and ventilation: filters and fans cleaned as the manufacturer says; if you cook with grease '
                   'under a hood (NFPA 96), hood and duct cleaning by a certified contractor at its frequency for your '
                   'volume'),
    (_T + ('B8',), 'Lab tests by an outside lab: water activity (aw) of new ganaches and fillings, to set their shelf life '
                   'and confirm which ones are TCS (FDA Food Code 1-201.10); water testing only if you are on a private '
                   'well'),
    (_T + ('B9',), 'Food handler cards for all staff (renewals as your state or county requires) and a certified food '
                   'protection manager on the team (FDA Food Code 2-102.12)'),
    (_T + ('B15',), 'Refrigeration service by an EPA 608-certified tech: cool room, fridges and display cases — coils, '
                    'gaskets, refrigerant leak check and defrost cycle'),
    (_T + ('B17',), 'Annual extinguisher maintenance by a licensed fire protection company: new tag and record (OSHA '
                    '1910.157); hydrostatic tests as the label says (OSHA 1910.157(f))'),
    (_T + ('B18',), 'Gas lines and appliance connections checked by a licensed pro, if you have gas, as often as your '
                    'local code or gas utility requires'),
    (_T + ('F18',), 'Per local code'),
    (_T + ('B22',), "Renew insurance and review coverage: general and product liability, property, workers' comp, "
                    'business interruption and equipment breakdown with spoilage (a cool room down in July can melt the '
                    'stock)'),
    (_T + ('B23',), 'Check that your health permit (and, if your state requires one to make candy or to sell wholesale or '
                    'by mail, your food manufacturing license) is current and matches what you really do: kitchen, shop, '
                    'shipping'),
    (_T + ('B24',), 'POS check before year-end: software updates, sales tax rates and settings (many states tax candy '
                    'even where groceries are exempt), user permissions'),
])
# 08 · Cierre (errata ES): apagar las vitrinas y registrar la temperatura de cierre del obrador iba DESPUÉS de la alarma
# y la llave, y las persianas se cerraban antes de recoger la señalización y vaciar papeleras. Toda la secuencia, mismas
# 15 filas (E = «Close»): clientes y música → patio y señalización → vitrinas y temperatura → caja → papeleras y
# seguridad → el local → alarma, puertas y llave al final
_CN = ('08', 'Cierre del Negocio')
_CIERRE_08 = [  # fila ES de origen, EN, zona EN, responsable EN
    (6, 'Check no customers are left in the shop', 'Shop floor', 'Shift lead'),
    (5, 'Turn off background music', 'General', 'Shift lead'),
    (7, 'Clean up and bring in the patio, if you have one', 'Patio', 'Shift lead'),
    (12, 'Bring in the outdoor signage and sidewalk sign', 'Outside', 'Shift lead'),
    (18, 'Turn off the chocolate display cases once all the product is back in the cool room', 'Display case',
     'Shift lead'),
    (19, 'Log the closing temp of the kitchen (target 64–68 °F) — log reading: ____ °F', 'Kitchen', 'Shift lead'),
    (8, 'Turn off the POS / card terminal (or leave on standby)', 'Register', 'Shift lead'),
    (14, 'Empty trash cans in common areas and restrooms', 'Restrooms', 'Shift lead'),
    (15, 'Final safety check: gas appliances off (if you have gas), water off, small appliances unplugged — never the '
         'cool room or the fridges', 'General', 'Shift lead'),
    (13, 'Check that windows are closed', 'General', 'Shift lead'),
    (11, 'Turn off HVAC or set it to night mode: keep the shop below 68 °F if any chocolate stays out of the cool room',
     'General', 'Shift lead'),
    (10, 'Turn off lights (leave security lighting on)', 'General', 'Shift lead'),
    (16, 'Set the alarm', 'Entrance', 'Last one out'),
    (9, 'Close security gate and doors', 'Entrance', 'Last one out'),
    (17, 'Lock up and verify it is locked', 'Entrance', 'Last one out'),
]
# responsable que cambia (declarado): vitrinas y temperatura (ES «Último en salir») → el shift lead; alarma y
# persianas (ES «Encargado») → el último en salir, con la llave
_RESPONSABLE_CAMBIA = frozenset({18, 19, 16, 9})
for _fila, (_o, _b, _c, _d) in enumerate(_CIERRE_08, 5):
    for _col, _v in (('B', _b), ('C', _c), ('D', _d)):
        POR_CELDA[_CN + ('%s%d' % (_col, _fila),)] = _v
# 08 y 09 · horas (D9, criterio del kit): una chocolate shop US abre la tienda a las 10 AM (la producción empieza
# antes, en el 01): todas las horas límite del 08 «Apertura» y del 09 «Apertura de Caja» suben 2 h (07:00 → 9:00 AM),
# mismo orden y mismos intervalos. Fila → hora ES (la comprueba cruzar_censo)
_AN = ('08', 'Apertura del Negocio')
_AC9 = ('09', 'Apertura de Caja')
HORAS_ES = OrderedDict([(_AN + ('E%d' % f,), h) for f, h in zip(range(5, 22), ['07:00'] * 6 + ['07:15'] * 6
                                                                  + ['07:30'] * 5)]
                       + [(_AC9 + ('D%d' % f,), h) for f, h in zip(range(5, 18), ['07:15'] * 5 + ['07:30'] * 4
                                                                    + ['07:45'] * 4)])
DESPLAZAMIENTO_H = 2


def _mas(h, horas=DESPLAZAMIENTO_H):
    hh, mm = h.split(':')
    return hora_us('%02d:%s' % (int(hh) + horas, mm))


for _k, _h in HORAS_ES.items():
    POR_CELDA[_k] = _mas(_h)
for _fila, (_mes, _prod, _temp, _dir) in CALENDARIO.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'A%d' % _fila)] = _mes
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'C%d' % _fila)] = _prod
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'D%d' % _fila)] = _temp
VALORES_EN = OrderedDict()             # sin inventario con mínimos en el ES chocolatería (nada numérico cambia)

# ==========================================================================
# ADAPTAR (en español, con el dato US; las cifras y normas salen de REGLAS_US)
# ==========================================================================
_A = _base.ADAPTAR
_HACCP_KIT = _base._HACCP_KIT
_TIRA = 'sanitizante aprobado a la concentración de la etiqueta, medida con tira (test strip) (FDA Food Code 4-501.114)'
_SECO = '; y secar bien: el agua no puede tocar el chocolate'
_LOG = 'coletilla «— log reading: ____ °F»'
_LOG2 = 'coletilla «— log readings: ____ °F / ____ °F»'
_TEMPS = ('Objetivos US del kit en °F: obrador (kitchen) 64–68 °F (ES 18-20 °C); cuarto de conservación (cool room) '
          '59–64 °F (ES 15-18 °C) con 50–60 % de humedad; rellenos y ganaches en la nevera (fridge) a 41 °F o menos (FDA '
          'Food Code 3-501.16); vitrina de bombonería (display case) 60–64 °F (ES 16-18 °C)')
_CURVA = ('cifras del kit en °F; manda la curva de templado del fabricante de tu cobertura (couverture), que viene en el '
          'envase o en su ficha técnica')
_ALERGENOS = ('Alérgenos US: los 9 principales (FALCPA + FASTER Act): leche, huevo, frutos de cáscara (tree nuts), '
              'cacahuete, trigo (barquillos, galletas, crujientes), soja (también la lecitina), sésamo, pescado y '
              'crustáceos; los sulfitos no son uno de los 9 (si tu fruta confitada los lleva, déjalos en el cartel); '
              'en UK, los 14. Sin «cereales con gluten»: se dice «wheat»')
_VITRINA = ('Vitrina US: cartel de cada bandeja con nombre y precio (y precio por libra si vendes al peso) y aviso por '
            'escrito de los alérgenos principales de lo que se vende sin envasar (FDA Food Code 2022 3-602.12(C), donde '
            'tu estado lo haya adoptado; buena práctica en todo caso). ' + _ALERGENOS + '. «Trazas» → «may contain» '
            '(contacto cruzado en líneas compartidas): en EE. UU. es voluntario y tiene que ser veraz')
_ENVASADO = ('Etiqueta US de lo que se envasa en la tienda (tabletas, cajas cerradas, bolsas): nombre del producto, '
             'ingredientes por peso, contenido neto (oz y g), alérgenos principales y nombre y lugar del negocio (FDA '
             'Food Code 3-602.11); el lote y la fecha de consumo preferente (best-by) son criterio del kit: en EE. UU. '
             'la fecha es voluntaria salvo en la fórmula infantil')
_MUESTRAS = ('Muestras (samples) con pinzas, palillo o cápsula de un solo uso; nunca a mano desnuda (FDA Food Code '
             '3-301.11)')
_MANO = ('lo listo para consumir (bombones, trufas, muestras) no se toca con la mano desnuda: guantes, pinzas o papel '
         '(FDA Food Code 3-301.11)')
_BASCULA = ('la báscula de venta al peso tiene que ser legal para el comercio (legal-for-trade, NTEP) y la revisa y '
            'precinta la oficina de pesas y medidas de tu estado')
_FECHAS = ('fechas US: lo TCS (ganache de nata fresca, rellenos con actividad de agua alta) lleva date marking de 7 días '
           'a 41 °F como máximo, contando el día de elaboración como día 1 (FDA Food Code 3-501.17); el resto, consumo '
           'preferente (best-by, criterio del kit)')
_RESENAS = 'Plataformas US: Google Business Profile y Yelp'
_SEGURIDAD = ('APPCC → seguridad alimentaria (food safety): registros de temperatura y limpieza; ' + _HACCP_KIT)
_GAS_NO_LLAVE = ('en EE. UU. la llave general del gas no se abre ni se cierra cada día: sin «abrir/cerrar la llave '
                 'general»')
ADAPTAR = OrderedDict([
    # 01 · Instrucciones
    (('01', 'Instrucciones', 'B12'), 'A4 → US Letter'),
    (('01', 'Instrucciones', 'B15'), 'Sin «comprobación del gas» como paso de abrir llaves: «si tienes gas, comprueba '
     'que no huele a gas»; ' + _GAS_NO_LLAVE),
    (('01', 'Instrucciones', 'B16'), _TEMPS),
    (('01', 'Instrucciones', 'B17'), '20 °C → 68 °F'),
    # 01 · Apertura
    (('01', 'Apertura', 'B7'), _A[('01', 'Apertura Cocina', 'B7')]),
    (('01', 'Apertura', 'B8'), _A[('01', 'Apertura Cocina', 'B9')] + '; añade: ' + _MANO),
    (('01', 'Apertura', 'B10'), _A[('01', 'Apertura Cocina', 'B10')]),
    (('01', 'Apertura', 'B12'), _A[('01', 'Apertura Cocina', 'B14')] + '; ' + _GAS_NO_LLAVE),
    (('01', 'Apertura', 'B15'), 'Temperadora → tempering machine (melter); precalentar según el fabricante (el kit: '
     '113 °F, ES 45 °C)'),
    (('01', 'Apertura', 'B16'), 'Cámara de conservación → cool room a 59–64 °F con 50–60 % de humedad; ' + _LOG),
    (('01', 'Apertura', 'B17'), 'Nevera de rellenos y ganaches → fridge a 41 °F o menos (FDA Food Code 3-501.16); '
     + _LOG),
    (('01', 'Apertura', 'B19'), 'Vitrina de bombonería → display case a 60–64 °F, sin condensación; por encima de 68 °F '
     'la manteca de cacao funde; ' + _LOG),
    (('01', 'Apertura', 'B20'), 'Tienda a 68–72 °F'),
    (('01', 'Apertura', 'B21'), _HACCP_KIT + '; lectura en °F'),
    (('01', 'Apertura', 'B26'), _VITRINA),
    (('01', 'Apertura', 'B29'), _MUESTRAS),
    # 01 · Cierre
    (('01', 'Cierre', 'B10'), 'El mostrador donde se manipula producto: limpiar y luego sanitizar con ' + _TIRA
     + '; los cristales, con limpiacristales'),
    (('01', 'Cierre', 'B17'), 'Cool room a 59–64 °F y fridge de rellenos a 41 °F o menos; ' + _LOG2),
    (('01', 'Cierre', 'B18'), 'Limpiar y luego sanitizar las superficies de mármol o granito con ' + _TIRA + _SECO),
    (('01', 'Cierre', 'B19'), 'Mermas → waste log: producto, cantidad y motivo'),
    (('01', 'Cierre', 'B25'), 'Apagar los equipos de gas según el fabricante (si tienes gas) y comprobar agua y luces; '
     + _GAS_NO_LLAVE),
    # 02 · Instrucciones
    (('02', 'Instrucciones', 'B11'), 'Ajustar el templado a la curva del fabricante de cada cobertura (couverture)'),
    (('02', 'Instrucciones', 'B15'), 'Aire del obrador: 64–68 °F y 50–60 % de humedad (ES 18-20 °C)'),
    (('02', 'Instrucciones', 'B17'), 'añade: el granel de ganache se congela a 0 °F o menos'),
    # 02 · Templado
    (('02', 'Templado', 'B9'), 'Obrador a 64–68 °F y 50–60 % de humedad; ' + _LOG),
    (('02', 'Templado', 'B15'), 'Fundir a 122–131 °F (ES 50-55 °C); ' + _CURVA),
    (('02', 'Templado', 'B16'), 'Enfriar a 81–82 °F (ES 27-28 °C) sobre mármol (tabling) o por siembra (seeding); '
     + _CURVA),
    (('02', 'Templado', 'B17'), 'Recalentar a 88–90 °F (ES 31-32 °C), temperatura de trabajo; ' + _CURVA),
    (('02', 'Templado', 'B18'), 'El test seca en 3-5 min a 68 °F (ES 20 °C); snap = el chasquido al partir'),
    (('02', 'Templado', 'B23'), 'Fundir a 113–122 °F (ES 45-50 °C); ' + _CURVA),
    (('02', 'Templado', 'B24'), 'Enfriar a 79–81 °F (ES 26-27 °C) sobre mármol (tabling) o por siembra (seeding); '
     + _CURVA),
    (('02', 'Templado', 'B25'), 'Recalentar a 84–86 °F (ES 29-30 °C), temperatura de trabajo; ' + _CURVA),
    (('02', 'Templado', 'B26'), 'Test a 64–68 °F (ES 18-20 °C) desde la temperatura de trabajo de 84–86 °F (ES '
     '29-30 °C); ' + _CURVA),
    (('02', 'Templado', 'B30'), 'Fundir a 104–113 °F (ES 40-45 °C); ' + _CURVA),
    (('02', 'Templado', 'B31'), 'Enfriar a 77–79 °F (ES 25-26 °C) sobre mármol (tabling) o por siembra (seeding); '
     + _CURVA),
    (('02', 'Templado', 'B32'), 'Recalentar a 82–84 °F (ES 28-29 °C), temperatura de trabajo; ' + _CURVA),
    (('02', 'Templado', 'B33'), 'Test a 64–68 °F (ES 18-20 °C) desde la temperatura de trabajo de 82–84 °F (ES '
     '28-29 °C); ' + _CURVA),
    # 02 · Moldeado
    (('02', 'Moldeado', 'B6'), 'Moldes (polycarbonate molds) a 68–72 °F (ES 20-22 °C)'),
    (('02', 'Moldeado', 'B8'), 'Cáscara (shell) de 1/16–1/8 in (ES 2-3 mm)'),
    (('02', 'Moldeado', 'B10'), 'Enfriar a 54–57 °F (ES 12-14 °C) durante 10-15 min'),
    (('02', 'Moldeado', 'B13'), 'Sellar → cap (capping) con chocolate templado'),
    (('02', 'Moldeado', 'B23'), 'Enfriar a 54–57 °F (ES 12-14 °C) durante 20-30 min'),
    (('02', 'Moldeado', 'B25'), 'Papel de aluminio → foil; ' + _ENVASADO),
    (('02', 'Moldeado', 'B31'), _FECHAS),
    (('02', 'Moldeado', 'B33'), 'Producto terminado a 59–64 °F y 50–60 % de humedad, a oscuras y lejos de olores; '
     + _LOG),
    (('02', 'Moldeado', 'D42'), 'añade: solo si su actividad de agua está comprobada en laboratorio (no TCS); si no, '
     'como la ganache de nata fresca'),
    (('02', 'Moldeado', 'D45'), 'añade al final: «Alcohol-filled candy: check your state rules»'),
    (('02', 'Moldeado', 'D48'), '≤ −18 °C → 0 °F o menos; descongelar 24 h en la nevera (41 °F o menos) sin abrir'),
    # 03
    (('03', 'Instrucciones', 'B14'), 'Registro de jornada US: la FLSA obliga a registrar las horas trabajadas del '
     'personal por horas (non-exempt) (29 CFR 516.2), obrador y tienda; fichajes 2 años y nóminas 3 (29 CFR 516.5-516.6; '
     'algunos estados piden más, p. ej. NY 6). Sin RD-ley 8/2019 ni «4 años»'),
    (('03', 'Diario', 'B25'), _A[('03', 'Diario Manager', 'B35')] + '; obrador y tienda; sin RD-ley 8/2019 ni «4 años»'),
    (('03', 'Semanal', 'B14'), _FECHAS),
    (('03', 'Mensual', 'B23'), _RESENAS),
    # 04 · perfiles
    (('04', 'Chocolatero', 'B12'), _ENVASADO),
    (('04', 'Dependiente', 'B7'), _VITRINA),
    (('04', 'Dependiente', 'B8'), _MUESTRAS),
    (('04', 'Dependiente', 'B15'), 'añade: con guantes o pinzas, nunca a mano desnuda (FDA Food Code 3-301.11)'),
    (('04', 'Dependiente', 'B16'), 'Señal → deposit; encargos → pre-orders / custom orders'),
    (('04', 'Dependiente', 'B23'), 'Mostrador: limpiar y luego sanitizar con ' + _TIRA + '; cristales, con '
     'limpiacristales'),
    (('04', 'Dependiente', 'B24'), 'Tienda a 68–72 °F y vitrina a 60–64 °F; ' + _LOG),
    (('04', 'Encargado', 'B17'), _SEGURIDAD),
    # 05
    (('05', 'Instrucciones', 'B14'), 'Describe la lista US de la hoja «Quarterly & Annual»: control de plagas, extracción '
     '(NFPA 96 solo si se cocina con grasa bajo campana), análisis de actividad de agua de ganaches y rellenos, food '
     'handler cards y certified food protection manager, servicio técnico de la temperadora y del bombo (panning '
     'machine), frío (EPA 608), calibración de termómetros y báscula (legal-for-trade si vendes al peso), extintores '
     '(OSHA), gas, seguros, health permit (y licencia estatal de fabricación si la piden) y POS / sales tax. Sin DDD, '
     'BIE, legionela, RGSEAA ni facturación española'),
    (('05', 'Instrucciones', 'B15'), '«Cadencia» → "Frequency"; el nº de parte → el número del informe de servicio '
     '(service report #), en "Notes"; la cadencia es la habitual o la que pide la norma US de cada fila'),
    (('05', 'Semanal', 'B7'), 'Mármol: limpiar y luego sanitizar con ' + _TIRA + _SECO),
    (('05', 'Semanal', 'B9'), 'Superficies de envasado: limpiar y luego sanitizar con ' + _TIRA),
    (('05', 'Semanal', 'B18'), 'Zona de degustación: limpiar y luego sanitizar con ' + _TIRA),
    (('05', 'Semanal', 'B32'), 'Cool room a 59–64 °F y fridge de rellenos a 41 °F o menos; ' + _LOG2),
    (('05', 'Semanal', 'B34'), 'Báscula de precisión (obrador) con pesa patrón; añade: ' + _BASCULA),
    (('05', 'Mensual', 'B9'), 'Termómetros y sondas: comprobación en agua con hielo (32 °F)'),
    (('05', 'Mensual', 'B10'), _A[('05', 'Mantenimiento Mensual', 'B21')]),
    (('05', 'Mensual', 'B22'), _SEGURIDAD),
    (('05', 'Mensual', 'B23'), 'Plan de control de plagas → el del operador con licencia (licensed pest control operator)'),
    (('05', 'Mensual', 'B25'), 'Etiquetado: ingredientes, alérgenos (los 9 de EE. UU.) y lotes; la etiqueta de lo '
     'envasado en la tienda (FDA Food Code 3-602.11) y el aviso de alérgenos de la vitrina (3-602.12(C))'),
    (('05', 'Trimestral y Anual', 'B10'), 'Plan de autocontrol → tus procedimientos de seguridad alimentaria (food safety '
     'procedures); fichas técnicas → product specs y la tabla de alérgenos (allergen chart)'),
    (('05', 'Trimestral y Anual', 'B14'), 'SAT → el servicio técnico del fabricante; bombo → panning machine; tornillo → '
     'auger'),
    (('05', 'Trimestral y Anual', 'B16'), 'Termómetros y sondas por el punto de hielo (32 °F) o contra uno de referencia; '
     'la báscula de precisión, con pesa patrón; añade: ' + _BASCULA),
    (('05', 'Trimestral y Anual', 'B25'), 'Archivar los fichajes (time records) del trimestre (FLSA, 29 CFR 516) y anotar '
     'en "Notes" el número del informe de servicio de cada revisión y la fecha de la siguiente'),
    # 06
    (('06', 'Instrucciones', 'B6'), "Holiday season (Christmas y Hanukkah), Valentine's Day, Easter, Mother's Day y más"),
    (('06', 'Instrucciones', 'B14'), 'Señal → deposit'),
    (('06', 'Instrucciones', 'B15'), 'El día 22 → el 22 de diciembre; añade: y la fecha límite de envíos (shipping '
     'cutoff) de tu transportista'),
    (('06', 'Navidad', 'A1'), 'Holiday Season (Nov–Dec): Christmas, Hanukkah y regalos de empresa'),
    (('06', 'Navidad', 'B6'), 'Sin turrones: bark (peppermint bark), bombones, figuras (Santa, árboles, adornos) y gelt '
     'de Hanukkah'),
    (('06', 'Navidad', 'B11'), '24 y 31 → Christmas Eve y New Year\'s Eve; añade la fecha límite de envíos (shipping '
     'cutoff) según tu transportista'),
    (('06', 'Navidad', 'B15'), 'Sustituye a los turrones: bark, toffee, brittle (el guirlache) y trufas'),
    (('06', 'Navidad', 'B16'), 'Papá Noel → Santa'),
    (('06', 'Navidad', 'B18'), 'Cestas y lotes corporativos → corporate gift boxes y baskets'),
    (('06', 'Navidad', 'B26'), 'Señal → deposit; lugar de entrega → dirección de entrega'),
    (('06', 'San Valentín', 'B23'), 'Por debajo de 18 °C → por debajo de 64 °F, y nunca en el maletero al sol; añade: en '
     'los envíos, caja aislada (insulated mailer) y cold packs cuando haga calor en el destino'),
    (('06', 'Pascua', 'A1'), 'Easter (Mar–Apr)'),
    (('06', 'Pascua', 'B6'), 'Sin monas: huevos, conejos (bunnies) y cestas de Pascua (Easter baskets)'),
    (('06', 'Pascua', 'B9'), 'Sustituye a las monas: cestas de Pascua (Easter baskets) por encargo, si las ofreces'),
    (('06', 'Pascua', 'B14'), 'Conejos y pollitos → bunnies y chicks'),
    (('06', 'Pascua', 'B15'), 'Sustituye a las monas: huevos grandes decorados y rellenos (filled eggs) o centros de mesa '
     'de chocolate'),
    (('06', 'Pascua', 'B17'), _ENVASADO + '. ' + _ALERGENOS),
    # 08 (el cierre reordenado y las horas van por POR_CELDA)
    (('08', 'Apertura del Negocio', 'B8'), _A[('08', 'Apertura del Negocio', 'B8')]),
    (('08', 'Apertura del Negocio', 'B11'), 'Vitrinas temperadas → climate-controlled display cases'),
    (('08', 'Apertura del Negocio', 'B17'), 'Terraza → patio, si tienes, con el permiso de la ciudad si lo pide (mesas, '
     'sillas, sombrillas o estufas de exterior / patio heaters)'),
    (('08', 'Apertura del Negocio', 'B18'), 'Precio por kilo → precio por libra; los alérgenos a la vista, por escrito '
     '(FDA Food Code 2022 3-602.12(C), donde se haya adoptado); repuesto en la cool room'),
    (('08', 'Apertura del Negocio', 'B20'), 'Vitrinas a 60–64 °F y menos del 55 % de humedad; ' + _LOG),
    (('08', 'Apertura del Negocio', 'B21'), 'Obrador a 64–68 °F y 50–60 % de humedad; ' + _LOG),
    # 09 · lo propio de la venta al peso (el resto del 09, del base)
    (('09', 'Apertura de Caja', 'B9'), 'Báscula de mostrador: tara de bandejas y cajas y comprobación con pesa patrón; '
     'añade: ' + _BASCULA),
    (('09', 'Apertura de Caja', 'B10'), 'Precio por kilo → precio por libra (per lb) de cada referencia al peso, el mismo '
     'en el POS y en el cartel de la vitrina'),
    (('09', 'Cierre de Caja', 'B14'), 'Kilos → libras (lb) registradas en el POS frente a lo que falta de las bandejas'),
    (('09', 'Cierre de Caja', 'B15'), 'Señales → deposits de los encargos (pre-orders); no son venta del día'),
    # BONUS-01
    (('B01', 'Briefing', 'B10'), 'kg → lb (cobertura = couverture: dark / milk / white)'),
    (('B01', 'Briefing', 'B11'), 'Obrador: ____ °F / ____ % (objetivo 64–68 °F y 50–60 %)'),
    # BONUS-02
    (('B02', 'Instrucciones', 'B5'), "Año chocolatero de EE. UU.: Valentine's Day, Easter, Mother's Day (2.º domingo de "
     "mayo), Father's Day (3.er domingo de junio), Halloween, Thanksgiving (4.º jueves de noviembre) y las fiestas de "
     'diciembre (Christmas y Hanukkah). Sin fechas españolas'),
    (('B02', 'Instrucciones', 'B7'), 'Añade la nota UK: Mothering Sunday (marzo), bank holidays y Boxing Day'),
])
# 09: el ADAPTAR del base (mismas celdas y mismo texto ES: Instrucciones, Cierre B10 y Registro A37), tal cual
_HEREDA_ADAPTAR = [k for k in _A if k[0] == '09']
for _k in _HEREDA_ADAPTAR:
    ADAPTAR[_k] = _A[_k]
for _fila, (_mes, _prod, _temp, _dir) in CALENDARIO.items():
    ADAPTAR[(HOJA_CAL[0], HOJA_CAL[1], 'B%d' % _fila)] = 'Mes EN: «%s». %s' % (_mes, _dir)
# aplicar_en.objetivo_ajuste / G3 (como la pizzería, la hamburguesería, la ghost kitchen y la heladería): la EN activa
# el ajuste también donde el ES no cabía
AJUSTE_MAQUETA_ES = True
# Celdas ES con °C cuya EN NO lleva cifra: solo la fila 19 del cierre del 08 (su temperatura sube a la fila 10 con el
# reorden; en la 19 EN queda la llave). G7 la declara; el resto de °C del ES lleva su °F en la EN
CELSIUS_SIN_F = frozenset({('08', 'Cierre del Negocio', 'B19')})

# ==========================================================================
# REGLAS_US: las del base que aplican + las de la chocolatería (fuente única de las cifras y normas que el kit afirma)
# ==========================================================================
REGLAS_US = OrderedDict(_base.REGLAS_US)
# Fuera las del base que una chocolatería no hace (sin pescado crudo ni marisco, sin mantenimiento en caliente,
# enfriado ni recalentado, sin aviso de crudo, sin lavado de vegetales, sin campana de grasa con extinción ni separador
# FOG): así G7 caza cualquier 135, 165, 70 o −31 °F que se cuele y las cifras permitidas = GRADOS_F_SPEC
for _k in ('parasitos', 'recalentado', 'enfriamiento', 'caliente', 'moluscos', 'aviso_consumidor', 'lavado_vegetal',
           'supresion', 'grasas'):
    del REGLAS_US[_k]
REGLAS_US.update([
    ('choco_temps', ('obrador 64–68 °F; cool room 59–64 °F con 50–60 % de humedad; vitrina 60–64 °F y < 55 %; tienda '
                     '68–72 °F; por encima de 68 °F la manteca de cacao empieza a fundir; moldes a 68–72 °F; enfriado '
                     'de moldes a 54–57 °F; reparto por debajo de 64 °F',
                     '[criterio del kit] (cifras del ES: 18-20, 15-18, 16-18, 20-22, 12-14 y 18 °C)')),
    ('templado', ('negro: fundir 122–131 °F, enfriar 81–82 °F, trabajo 88–90 °F · con leche: 113–122 °F, 79–81 °F, '
                  '84–86 °F · blanco: 104–113 °F, 77–79 °F, 82–84 °F · temperadora precalentada a 113 °F · test a '
                  '64–68 °F; manda la curva del fabricante de cada cobertura',
                  '[fabricante] curva de templado de cada cobertura; [criterio del kit] cifras del ES en °F')),
    ('tcs_ganache', ('ganache de nata fresca y rellenos con actividad de agua alta: TCS (41 °F o menos; date marking 7 '
                     'días) salvo un análisis de laboratorio (aw) que demuestre que no lo son; el granel de ganache, '
                     'congelado a 0 °F o menos; el chocolate acabado no se congela',
                     'FDA Food Code 2022 §1-201.10 (TCS food, tablas A y B); §3-501.16(A)(2); §3-501.17')),
    ('mano_desnuda', ('sin contacto de la mano desnuda con lo listo para consumir (bombones, trufas, muestras)',
                      'FDA Food Code 2022 §3-301.11')),
    ('alergenos_vitrina', ('aviso por escrito de los alérgenos principales de lo que se vende sin envasar (cartel de '
                           'la vitrina, folleto); donde el estado haya adoptado el Food Code 2022',
                           'FDA Food Code 2022 §3-602.12(C); FDA, ficha de diciembre de 2024 sobre el Food Code 2022')),
    ('precautorio', ('«may contain» / contacto cruzado: voluntario y veraz', 'FDA, Questions and Answers Regarding Food '
                     'Allergens (Edition 5), 2022')),
    ('etiqueta_envasado', ('lo envasado en el local lleva nombre, ingredientes, contenido neto, nombre y lugar del '
                           'negocio y alérgenos; lo servido a petición del cliente no es «packaged»',
                           'FDA Food Code 2022 §3-602.11(B); §1-201.10 (Packaged)')),
    ('fecha_preferente', ('la fecha de consumo preferente (best-by) es voluntaria salvo la fórmula infantil',
                          'USDA FSIS, «Food Product Dating»; 21 CFR 107.20 (fórmula infantil)')),
    ('bascula', ('venta al peso con báscula legal para el comercio', '[estatal] pesas y medidas; NIST Handbook 44 (NTEP)')),
    ('cfpm', ('un certified food protection manager en el equipo; food handler cards según el estado',
              'FDA Food Code 2022 §2-102.12; [estatal]')),
    ('licencia_choco', ('health permit local; algunos estados piden además una licencia de fabricación de alimentos para '
                        'elaborar caramelos o vender al por mayor o por correo', '[estatal] departamento de agricultura '
                        'o de salud')),
    ('impuesto_candy', ('muchos estados gravan los caramelos (candy) aunque la alimentación esté exenta',
                        '[estatal] Streamlined Sales and Use Tax Agreement (definición de «candy»)')),
    ('licor', ('bombones con alcohol: norma estatal', '[estatal]')),
    ('campana', (_base.REGLAS_US['campana'][0] + '; solo si se cocina con grasa bajo campana; la extracción general del '
                 'obrador, según su fabricante', _base.REGLAS_US['campana'][1])),
    ('seguro_frio', ('equipment breakdown con spoilage; business interruption', '[criterio del kit] seguros US')),
    ('envios_calor', ('envíos con calor: caja aislada y cold packs, de lunes a miércoles', '[criterio del kit]')),
    ('temporada_choco', ("Valentine's Day (14 feb, el pico) · Easter (variable) · Mother's Day (2.º domingo de mayo) · "
                         'Teacher Appreciation Week (1.ª semana completa de mayo) · Sweetest Day (3.er sábado de '
                         'octubre) · National Chocolate Day (28 oct) · Thanksgiving · Small Business Saturday · '
                         'Christmas y Hanukkah', '5 U.S.C. 6103; 36 U.S.C. 117 y 109; [criterio del kit] fechas '
                         'comerciales (National PTA; American Express, 2010)')),
    ('plazos_kit', ('vida útil de la tabla del 02; food cost 30–35 %; cáscara 1/16–1/8 in; enfriado 10–30 min',
                    '[criterio del kit]')),
])
# °F que el kit puede afirmar (G7): sala y conservación (59, 60, 64, 68, 72), enfriado (54, 57), templado (77, 79, 81,
# 82, 84, 86, 88, 90, 104, 113, 122, 131), frío y congelado (41, 0), calibración (32) y lavamanos (100)
GRADOS_F_SPEC = {0, 32, 41, 54, 57, 59, 60, 64, 68, 72, 77, 79, 81, 82, 84, 86, 88, 90, 100, 104, 113, 122, 131}

# ==========================================================================
# Pistas y dependencias de la chocolatería (extraer_textos.py)
# ==========================================================================
PISTAS_CAMBIO = {r'Kit de Tareas': 'D2: «Chocolate Shop Checklists Kit Pro»'}
PISTAS_FUERA = (r'Restaurante Casual',)
PISTAS_EXTRA = [
    (r'[Cc]hocolater[ií]a|[Bb]ombonería', 'D2: la EN no lleva el sufijo «— Chocolatería»; chocolatería → chocolate shop '
                                          '(chocolatier si se habla del oficio; chocolate store en el 08)'),
    (r'[Cc]hocolatero', 'maestro chocolatero → chocolatier'),
    (r'[Tt]emperadora|[Tt]empl', 'temperadora → tempering machine (melter); templar → temper (tabling sobre mármol, '
                                 'seeding por siembra); punto de trabajo → working temperature'),
    (r'[Ss]iembra|[Mm]ármol', 'siembra → seeding; mármol → marble slab (tabling)'),
    (r'[Cc]obertura', 'cobertura → couverture (callets / wafers); negra / con leche / blanca → dark / milk / white'),
    (r'[Bb]omb[oó]n', 'bombón → bonbon (molded bonbon); cajas de bombones surtidos → assorted bonbon boxes'),
    (r'[Tt]rufa|[Rr]ocas', 'trufa → truffle; rocas → clusters'),
    (r'[Tt]ableta', 'tableta → bar (chocolate bar)'),
    (r'[Ff]igura', 'figuras → molded figures (huecas → hollow figures)'),
    (r'[Cc]áscara|[Ss]ellar|[Tt]apa\b', 'cáscara → shell; sellar / tapa → cap (capping)'),
    (r'[Gg]anache|[Rr]elleno', 'ganache → ganache; rellenos → fillings'),
    (r'[Pp]raliné|[Gg]ianduja|[Gg]uirlache|[Gg]arrapiñad|[Cc]onfitad',
     'praliné → praline (sin tilde); gianduja → gianduja; guirlache → nut brittle; garrapiñados → candied nuts; frutas '
     'confitadas → candied fruit'),
    (r'[Bb]ombo\b', 'bombo → panning machine (panning)'),
    (r'[Bb]loom|[Ss]nap|[Bb]rillo', 'fat bloom / sugar bloom; snap; brillo → shine (gloss)'),
    (r'[Vv]itrina|[Ee]scaparate', 'vitrina → display case; escaparate → store window'),
    (r'[Oo]brador', 'obrador → kitchen (chocolate kitchen / production kitchen)'),
    (r'[Cc]ámara|[Nn]evera', 'cámara de conservación → cool room (59–64 °F); nevera de rellenos → fridge'),
    (r'[Pp]ackaging|[Cc]ajas? regalo|[Pp]apel de seda|[Cc]intas|[Ll]azos',
     'cajas regalo → gift boxes; papel de seda → tissue paper; cintas / lazos → ribbons'),
    (r'[Dd]egustaci[oó]n|[Mm]aridaje', 'degustación → samples / tasting; maridajes → pairings'),
    (r'[Dd]ependiente', 'dependiente → sales associate'),
    (r'[Ee]ncargad[oa]', 'encargado → shift lead'),
    (r'[Ee]ncargos?|[Ss]eñal\b', 'encargos → pre-orders / custom orders; señal → deposit'),
    (r'[Ff]ood cost|[Mm]ateria prima', 'materia prima → ingredients; food cost se queda'),
    (r'RRSS|redes', 'RRSS → social media'),
    (r'TPV|[Dd]atáfono', 'TPV / datáfono → POS / card terminal'),
    (r'[Aa]rqueo|[Cc]uadr', 'arqueo / cuadre de caja → cash count / reconcile'),
    (r'[Tt]erraza', 'terraza → patio'),
    (r'[Ll]ocal\b', 'el local → the shop'),
    (r'APPCC', 'APPCC → food safety (HACCP solo si lo exige tu estado)'),
    (r'\bkg\b|[Kk]ilo|\bmm\b', 'kg / kilo → lb; mm → in'),
    (r'[Tt]urr[oó]n|[Mm]onas?\b|[Pp]anellets|[Cc]omuniones|Reyes',
     'sin turrón, monas, panellets, comuniones ni Reyes: su equivalente US (bark / toffee, Easter baskets, '
     'Thanksgiving, favors de bodas)'),
    (r'[Ll]icor', 'licor → liqueur (nunca «liquor»)'),
]
DEPENDENCIAS_EXTRA = OrderedDict([
    ('variante', ('Sufijo de variante «Chocolatería»', r'Chocolatería', 'D2: la EN no lleva sufijo')),
    ('temperaturas_choco', ('Temperaturas del chocolate (obrador, conservación, vitrina, templado, enfriado)',
                            r'\d+(?:-\d+)? °C', 'D-CHOC: °F de REGLAS_US (choco_temps, templado)')),
    ('alergenos_vitrina', ('Alérgenos en la vitrina y en lo envasado', r'[Aa]lérgenos', 'D-CHOC: los 9 de EE. UU.; '
                           '3-602.12(C) en la vitrina; 3-602.11 en lo envasado')),
    ('venta_peso', ('Venta al peso', r'por kilo|al peso|[Bb]áscula', 'D-CHOC: precio por libra; báscula legal para el '
                    'comercio (NTEP)')),
    ('registro_jornada', ('Registro de jornada (RD-ley 8/2019)', r'RD-ley|[Rr]egistro (diario )?de jornada|Inspección',
                          'D11: FLSA (29 CFR 516)')),
])

# aplicar_en / gates_en (autotest): la hoja con horas de celda y una hoja protegida con verdes desbloqueadas (el
# 01-07 del molde ligero no se protege), como el catering y la heladería
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
    for ok in ('chocolatier', 'tempering machine', 'display case', 'patio', 'shift lead', 'sales associate',
               'restaurant consultant', 'restaurant supply store', 'liqueur bonbons', 'hot chocolate',
               'coffee bonbons', 'kitchen', 'cool room', 'sprinkles'):
        if rx.search(ok):
            err.append('TERMINOS_PROHIBIDOS caza lo permitido (%r)' % ok)
    rx_ctx = re.compile(RX_CONTEXTO_PENDIENTE)
    for ok in ('chocolatier', 'patio', 'liqueur bonbons', 'hot chocolate', 'restaurant consultant', 'kitchen'):
        if rx_ctx.search(ok):
            err.append('RX_CONTEXTO_PENDIENTE caza lo permitido (%r)' % ok)
    for k, v in list(GLOSARIO.items()) + list(POR_CELDA.items()) + list(CLAVES.items()):
        if k not in _base.GLOSARIO or k in _GLOSARIO_CHOCO:
            if isinstance(v, str) and rx.search(v):
                err.append('texto EN fijado con un término prohibido: %r → %r' % (k, v))
    if CITA_AUTOTEST.strip('()').split()[-1] in ' '.join(f for _v, f in REGLAS_US.values()):
        err.append('CITA_AUTOTEST está en REGLAS_US: G7 no la cazaría')
    # 09 desplazado: las 15 filas de billetes en 29-35 y 37-44; el fondo en C25; CASOS_G5 dentro del 09
    if [d[0] for d in DENOMINACIONES] != list(range(29, 36)) + list(range(37, 45)):
        err.append('DENOMINACIONES: filas fuera de 29-35 / 37-44 (09 del ES chocolatería)')
    for caso in CASOS_G5:
        for (h, coord) in list(caso['entradas']) + list(caso['esperado']):
            if h not in HOJAS_ES_POR_LIBRO['09']:
                err.append('CASOS_G5 %s: hoja %r fuera del 09' % (caso['nombre'], h))
    if abs(sum(d[4] for d in DENOMINACIONES) - CASOS_G5[0]['esperado'][(_HC, 'C45')]) > 1e-6:
        err.append('CASOS_G5: el total de 1 de cada no es la suma de DENOMINACIONES')
    if set(_H09) != {k for k in _base.POR_CELDA if k[0] == '09'} or len(set(_H09.values())) != len(_H09):
        err.append('09: el desplazamiento del POR_CELDA del base no es una biyección')
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
    # calendario: mes, productos y temporada US; la temporada, de una lista cerrada
    for fila, (mes, prod, temp, _d) in CALENDARIO.items():
        if temp not in ('Peak', 'High', 'Medium', 'Low'):
            err.append('calendario fila %d: temporada %r fuera de Peak / High / Medium / Low' % (fila, temp))
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
        err.append('08 cierre: la fila con la temperatura de cierre (origen 19) no lleva °F')
    for k in CF_POR_CELDA:
        if k[:2] not in {(c, h) for c, hs in HOJAS_ES_POR_LIBRO.items() for h in hs}:
            err.append('CF_POR_CELDA en una hoja que no existe: %r' % (k,))
    for k, v in ADAPTAR.items():
        if re.search(r'\bliquor\b', v, re.I):
            err.append('ADAPTAR %r dice «liquor» (es «liqueur»)' % (k,))
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
    if not tx.get((_CN[0], _CN[1], 'B18'), '').startswith('Apagar las vitrinas') or \
            not tx.get((_CN[0], _CN[1], 'B16'), '').startswith('Activar alarma'):
        err.append('08 cierre: el ES ya no apaga las vitrinas después de la alarma (errata corregida en el ES)')
    # calendario: A (mes), C (productos) y D (temporada) con texto en el ES; la temporada ES es Baja/Media/Alta
    for fila in FILAS_CALENDARIO:
        for col in 'ABCD':
            if (HOJA_CAL[0], HOJA_CAL[1], '%s%d' % (col, fila)) not in tx:
                err.append('calendario: %s%d sin texto en el ES' % (col, fila))
        if tx.get((HOJA_CAL[0], HOJA_CAL[1], 'D%d' % fila)) not in ('Baja', 'Media', 'Alta'):
            err.append('calendario: D%d no es una temporada del ES' % fila)
    # la tabla de vida útil del 02: familias en B39-B48 y C con texto
    for f in range(39, 49):
        if (_M[0], _M[1], 'B%d' % f) not in tx or (_M[0], _M[1], 'C%d' % f) not in tx:
            err.append('02 vida útil: fila %d sin familia o sin plazo en el ES' % f)
    if 'nata fresca' not in tx.get(_M + ('B41',), ''):
        err.append('02 vida útil: B41 ya no es la ganache de nata fresca (C41/D41 fijados como TCS)')
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


def cruzar_base(p_choco, p_base):
    """Lo heredado POR CELDA del base (POR_CELDA del 09, desplazado, y ADAPTAR del 09 y del 08) tiene en la chocolatería
    el mismo texto ES que en el base."""
    import json
    err = []

    def textos(p):
        d = {}
        for info in json.load(open(p, encoding='utf-8'))['libros'].values():
            for h, hd in info['hojas_detalle'].items():
                for coord, t in hd.get('textos', {}).items():
                    d[(info['corto'], h, coord)] = t
        return d
    tb, tc = textos(p_base), textos(p_choco)
    for kb, kc in _H09.items():
        if tc.get(kc) != tb.get(kb):
            err.append('POR_CELDA 09 heredado %r → %r: el texto ES de la chocolatería %r ≠ base %r'
                       % (kb, kc, tc.get(kc), tb.get(kb)))
    for k in _HEREDA_ADAPTAR + [('08', 'Apertura del Negocio', 'B8')]:
        if tc.get(k) != tb.get(k):
            err.append('ADAPTAR heredado %r: el texto ES de la chocolatería %r ≠ base %r' % (k, tc.get(k), tb.get(k)))
    # filas equivalentes (otra celda, la misma tarea del base): mismo tema en el ES
    for k, palabra in ((('01', 'Apertura', 'B7'), 'anillos'), (('01', 'Apertura', 'B8'), 'manos'),
                       (('01', 'Apertura', 'B10'), 'vómitos'), (('01', 'Apertura', 'B12'), 'gas'),
                       (('03', 'Mensual', 'B16'), 'registros de jornada'),
                       (('03', 'Diario', 'B25'), 'registro diario de jornada'),
                       (('05', 'Mensual', 'B10'), 'extintores')):
        if palabra not in tc.get(k, ''):
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
    print('mapas_chocolate.py: {} ficheros · {} pestañas · {} glosario · {} por celda · {} cf por celda · {} adaptar · '
          '{} reglas · {} casos G5 · {} errores'.format(len(FICHEROS), len(HOJAS), len(GLOSARIO), len(POR_CELDA),
                                                        len(CF_POR_CELDA), len(ADAPTAR), len(REGLAS_US),
                                                        len(CASOS_G5), len(e)))
    raise SystemExit(1 if e else 0)
